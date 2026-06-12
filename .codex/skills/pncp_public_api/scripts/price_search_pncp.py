#!/usr/bin/env python
"""Pesquisa textual de precos no PNCP com evidencias auditaveis.

Este script usa o endpoint publico https://pncp.gov.br/api/search/ para
localizar editais, atas e contratos por texto, depois consulta itens e
resultados da compra para extrair valor unitario estimado ou homologado.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable, Optional


SEARCH_URL = "https://pncp.gov.br/api/search/"
ITEM_BASES = [
    "https://pncp.gov.br/pncp-api/v1",
    "https://pncp.gov.br/api/pncp/v1",
]


@dataclass
class Evidence:
    fonte_nome: str
    dominio: str
    url_publica: str
    url_api_itens: str
    url_api_resultado: str
    titulo: str
    descricao_documento: str
    preco_brl: float
    tipo_valor: str
    fornecedor: str = ""
    orgao: str = ""
    uf: str = ""
    modalidade: str = ""
    numero_controle_pncp: str = ""
    numero_item: str = ""
    quantidade: Optional[float] = None
    unidade_medida: str = ""
    valor_total: Optional[float] = None
    data_publicacao_pncp: str = ""
    data_resultado: str = ""
    evidencia_textual: str = ""
    score_correspondencia: float = 0.0
    observacoes: str = ""
    data_hora_coleta: str = field(default_factory=lambda: dt.datetime.now().isoformat(timespec="seconds"))


def ascii_lower(text: Any) -> str:
    return unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode("ascii").lower()


def normalize_spaces(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "").replace("\xa0", " ")).strip()


def token_similarity(a: str, b: str) -> float:
    a_tokens = set(re.findall(r"[a-z0-9]{2,}", ascii_lower(a)))
    b_tokens = set(re.findall(r"[a-z0-9]{2,}", ascii_lower(b)))
    if not a_tokens or not b_tokens:
        return SequenceMatcher(None, ascii_lower(a), ascii_lower(b)).ratio()
    overlap = len(a_tokens & b_tokens) / max(1, len(a_tokens | b_tokens))
    seq = SequenceMatcher(None, " ".join(sorted(a_tokens)), " ".join(sorted(b_tokens))).ratio()
    return max(overlap, seq * 0.75)


def request_json(url: str, params: Optional[dict[str, Any]] = None, timeout: int = 45, retries: int = 2, delay: float = 0.0) -> Any:
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "", [])})
    last: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Codex-PNCP-PriceSearch/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                raw = response.read().decode("utf-8", errors="replace")
            if delay > 0:
                time.sleep(delay)
            return json.loads(raw) if raw else None
        except Exception as exc:
            last = exc
            if attempt < retries:
                time.sleep(attempt)
    raise RuntimeError(f"Falha ao consultar {url}: {last}")


def split_control(control: str) -> Optional[dict[str, Any]]:
    try:
        left, year = control.split("/")
        cnpj, _, seq = left.split("-")
        return {"cnpj": cnpj, "ano": int(year), "sequencial": int(seq)}
    except Exception:
        return None


def build_queries(query: str, extras: Iterable[str]) -> list[str]:
    candidates = [query, *extras]
    # Gera variantes úteis sem aspas e com termos comuns de telecom.
    q = ascii_lower(query)
    if "anti" in q and "ddos" in q:
        candidates.append(re.sub(r"anti[- ]?ddos", "DDoS", query, flags=re.I))
    if "gbps" in q:
        candidates.append(re.sub(r"\bgbps\b", "Gbps", query, flags=re.I))
    unique: list[str] = []
    seen: set[str] = set()
    for item in candidates:
        clean = normalize_spaces(str(item).replace('"', ""))
        key = ascii_lower(clean)
        if clean and key not in seen:
            unique.append(clean)
            seen.add(key)
    return unique


def pncp_search(query: str, doc_types: list[str], limit_per_query: int, delay: float) -> tuple[list[dict[str, Any]], list[str]]:
    found: list[dict[str, Any]] = []
    alerts: list[str] = []
    seen: set[tuple[Any, ...]] = set()
    for doc_type in doc_types:
        try:
            payload = request_json(SEARCH_URL, {"q": query, "tipos_documento": doc_type}, delay=delay)
        except Exception as exc:
            alerts.append(f"Falha PNCP search para '{query}'/{doc_type}: {exc}")
            continue
        rows = payload.get("items", []) if isinstance(payload, dict) else []
        for doc in rows:
            key = (
                doc.get("numero_controle_pncp"),
                doc.get("orgao_cnpj"),
                doc.get("ano"),
                doc.get("numero_sequencial"),
                doc.get("document_type"),
            )
            if key in seen:
                continue
            seen.add(key)
            found.append(doc)
            if len(found) >= limit_per_query:
                return found, alerts
    return found, alerts


def item_urls(doc: dict[str, Any]) -> list[str]:
    item_url = str(doc.get("item_url") or "")
    if item_url and not item_url.startswith("/compras/"):
        return []
    cnpj = doc.get("orgao_cnpj")
    ano = doc.get("ano")
    seq = doc.get("numero_sequencial")
    control = doc.get("numero_controle_pncp") or ""
    if (not cnpj or not ano or not seq) and control:
        parts = split_control(control)
        if parts:
            cnpj, ano, seq = parts["cnpj"], parts["ano"], parts["sequencial"]
    if not cnpj or not ano or not seq:
        return []
    return [f"{base}/orgaos/{cnpj}/compras/{ano}/{int(seq)}/itens" for base in ITEM_BASES]


def result_url(items_url: str, numero_item: Any) -> str:
    return f"{items_url}/{numero_item}/resultados"


def get_items(doc: dict[str, Any], delay: float) -> tuple[list[dict[str, Any]], str, list[str]]:
    alerts: list[str] = []
    for url in item_urls(doc):
        try:
            payload = request_json(url, delay=delay)
            if isinstance(payload, list):
                return payload, url, alerts
        except Exception as exc:
            alerts.append(f"Falha ao consultar itens {url}: {exc}")
    return [], "", alerts


def required_ok(text: str, required: list[str]) -> bool:
    lower = ascii_lower(text)
    return all(ascii_lower(term) in lower for term in required)


def forbidden_ok(text: str, forbidden: list[str]) -> bool:
    lower = ascii_lower(text)
    return not any(ascii_lower(term) in lower for term in forbidden)


def price_from_item(item: dict[str, Any], result_rows: list[dict[str, Any]]) -> tuple[float, str, str, str]:
    fornecedor = ""
    data_resultado = ""
    if result_rows:
        best = result_rows[0]
        price = float(best.get("valorUnitarioHomologado") or best.get("valorUnitario") or 0.0)
        fornecedor = normalize_spaces(best.get("nomeRazaoSocialFornecedor") or best.get("niFornecedor") or "")
        data_resultado = normalize_spaces(best.get("dataResultado") or "")
        if price > 0:
            return price, "homologado", fornecedor, data_resultado
    price = float(item.get("valorUnitarioEstimado") or 0.0)
    return price, "estimado", fornecedor, data_resultado


def public_url(doc: dict[str, Any]) -> str:
    item_url = doc.get("item_url") or ""
    if item_url.startswith("/"):
        return "https://pncp.gov.br/app" + item_url
    control = doc.get("numero_controle_pncp") or ""
    parts = split_control(control)
    if parts:
        return f"https://pncp.gov.br/app/editais/{parts['cnpj']}/{parts['ano']}/{parts['sequencial']}"
    return "https://pncp.gov.br/app"


def collect(args: argparse.Namespace) -> dict[str, Any]:
    required = [term.strip() for term in args.required.split(",") if term.strip()]
    forbidden = [term.strip() for term in args.forbidden.split(",") if term.strip()]
    docs_by_key: dict[str, dict[str, Any]] = {}
    alerts: list[str] = []
    for query in build_queries(args.query, args.extra_query or []):
        docs, search_alerts = pncp_search(query, args.doc_types.split(","), args.limit_per_query, args.delay_seconds)
        alerts.extend(search_alerts)
        for doc in docs:
            key = doc.get("numero_controle_pncp") or f"{doc.get('orgao_cnpj')}/{doc.get('ano')}/{doc.get('numero_sequencial')}"
            docs_by_key.setdefault(str(key), doc)

    cutoff = dt.datetime.now() - dt.timedelta(days=args.days) if args.days else None
    evidences: list[Evidence] = []
    seen: set[tuple[Any, ...]] = set()
    for doc in docs_by_key.values():
        if cutoff:
            raw_date = doc.get("data_publicacao_pncp") or doc.get("createdAt") or ""
            try:
                parsed = dt.datetime.fromisoformat(str(raw_date).replace("Z", "+00:00").replace("+00:00", ""))
                if parsed < cutoff:
                    continue
            except Exception:
                pass
        doc_text = normalize_spaces(" ".join(str(doc.get(k) or "") for k in ["title", "description", "orgao_nome", "numero_controle_pncp"]))
        if not required_ok(doc_text, required) or not forbidden_ok(doc_text, forbidden):
            continue

        items, items_url, item_alerts = get_items(doc, args.delay_seconds)
        alerts.extend(item_alerts)
        for item in items:
            item_text = normalize_spaces(" ".join(str(item.get(k) or "") for k in [
                "descricao", "descricaoItem", "materialOuServicoNome", "catalogo", "categoriaItemCatalogo",
                "informacaoComplementar", "unidadeMedida",
            ]))
            full_text = normalize_spaces(f"{doc_text} {item_text}")
            if not required_ok(full_text, required) or not forbidden_ok(full_text, forbidden):
                continue

            api_result = result_url(items_url, item.get("numeroItem")) if items_url else ""
            result_rows: list[dict[str, Any]] = []
            if api_result and item.get("temResultado"):
                try:
                    payload = request_json(api_result, delay=args.delay_seconds)
                    result_rows = payload if isinstance(payload, list) else []
                except Exception as exc:
                    alerts.append(f"Falha ao consultar resultado {api_result}: {exc}")
            price, kind, supplier, result_date = price_from_item(item, result_rows)
            if price <= 0:
                continue
            evidence_key = (doc.get("numero_controle_pncp"), item.get("numeroItem"), round(price, 2), kind)
            if evidence_key in seen:
                continue
            seen.add(evidence_key)
            score = max(token_similarity(args.query, full_text), token_similarity(" ".join(required), full_text))
            evidences.append(Evidence(
                fonte_nome=f"PNCP / {supplier or doc.get('orgao_nome') or 'sem fornecedor'}",
                dominio="pncp.gov.br",
                url_publica=public_url(doc),
                url_api_itens=items_url,
                url_api_resultado=api_result,
                titulo=item_text[:240] or normalize_spaces(doc.get("title") or ""),
                descricao_documento=normalize_spaces(doc.get("description") or ""),
                preco_brl=price,
                tipo_valor=kind,
                fornecedor=supplier,
                orgao=normalize_spaces(doc.get("orgao_nome") or ""),
                uf=normalize_spaces(doc.get("uf") or ""),
                modalidade=normalize_spaces(doc.get("modalidade_licitacao_nome") or ""),
                numero_controle_pncp=normalize_spaces(doc.get("numero_controle_pncp") or ""),
                numero_item=str(item.get("numeroItem") or ""),
                quantidade=float(item["quantidade"]) if item.get("quantidade") not in (None, "") else None,
                unidade_medida=normalize_spaces(item.get("unidadeMedida") or ""),
                valor_total=float(item["valorTotal"]) if item.get("valorTotal") not in (None, "") else None,
                data_publicacao_pncp=normalize_spaces(doc.get("data_publicacao_pncp") or ""),
                data_resultado=result_date,
                evidencia_textual=full_text[:1200],
                score_correspondencia=round(min(score, 1.0), 4),
                observacoes=f"Preco publico nacional extraido do PNCP ({kind}).",
            ))
            evidences.sort(key=lambda e: (e.score_correspondencia, e.tipo_valor == "homologado", e.data_publicacao_pncp), reverse=True)
            if len(evidences) >= args.max_prices:
                return {
                    "consulta": query_metadata(args, len(docs_by_key), alerts),
                    "evidencias": [asdict(e) for e in evidences],
                    "alertas": alerts,
                }
    evidences.sort(key=lambda e: (e.score_correspondencia, e.tipo_valor == "homologado", e.data_publicacao_pncp), reverse=True)
    return {
        "consulta": query_metadata(args, len(docs_by_key), alerts),
        "evidencias": [asdict(e) for e in evidences[: args.max_prices]],
        "alertas": alerts,
    }


def query_metadata(args: argparse.Namespace, docs_count: int, alerts: list[str]) -> dict[str, Any]:
    return {
        "query": args.query,
        "required": [term.strip() for term in args.required.split(",") if term.strip()],
        "forbidden": [term.strip() for term in args.forbidden.split(",") if term.strip()],
        "days": args.days,
        "doc_types": args.doc_types.split(","),
        "documentos_localizados": docs_count,
        "status": "parcial_com_alertas" if alerts else "completo",
        "data_hora": dt.datetime.now().isoformat(timespec="seconds"),
    }


def write_markdown(payload: dict[str, Any], path: Path) -> None:
    consulta = payload["consulta"]
    lines = [
        "# Pesquisa de preços PNCP",
        "",
        f"Data da consulta: {consulta['data_hora']}",
        f"Consulta textual: `{consulta['query']}`",
        f"Termos obrigatórios: {', '.join(consulta['required']) or 'não definidos'}",
        f"Termos proibidos: {', '.join(consulta['forbidden']) or 'não definidos'}",
        f"Janela: últimos {consulta['days']} dias" if consulta["days"] else "Janela: sem filtro local de data",
        f"Documentos localizados: {consulta['documentos_localizados']}",
        "",
        "| Score | Órgão | UF | PNCP | Modalidade | Item | Valor | Tipo | Qtd. | Total | Link |",
        "| ---: | --- | --- | --- | --- | --- | ---: | --- | ---: | ---: | --- |",
    ]
    for e in payload["evidencias"]:
        lines.append(
            f"| {e['score_correspondencia']} | {e['orgao']} | {e['uf']} | {e['numero_controle_pncp']} | "
            f"{e['modalidade']} | {str(e['titulo']).replace('|', '/')} | {e['preco_brl']:.2f} | {e['tipo_valor']} | "
            f"{e.get('quantidade') or ''} | {e.get('valor_total') or ''} | {e['url_publica']} |"
        )
    if payload.get("alertas"):
        lines += ["", "## Alertas", ""]
        lines.extend(f"- {alert}" for alert in payload["alertas"][:30])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Pesquisa textual de precos PNCP por objeto")
    parser.add_argument("--query", required=True, help="Texto principal de busca")
    parser.add_argument("--extra-query", action="append", help="Consulta adicional; pode repetir")
    parser.add_argument("--required", default="", help="Termos obrigatorios separados por virgula, avaliados no documento+item")
    parser.add_argument("--forbidden", default="", help="Termos proibidos separados por virgula")
    parser.add_argument("--days", type=int, default=730, help="Filtro local por data de publicacao PNCP")
    parser.add_argument("--doc-types", default="edital", help="tipos_documento separados por virgula; use edital para extrair itens de compras")
    parser.add_argument("--limit-per-query", type=int, default=30)
    parser.add_argument("--max-prices", type=int, default=10)
    parser.add_argument("--delay-seconds", type=float, default=0.5)
    parser.add_argument("--output", help="Arquivo JSON de saida")
    parser.add_argument("--markdown", help="Arquivo Markdown de saida")
    args = parser.parse_args()

    payload = collect(args)
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(text, encoding="utf-8")
    if args.markdown:
        Path(args.markdown).parent.mkdir(parents=True, exist_ok=True)
        write_markdown(payload, Path(args.markdown))
    if not args.output and not args.markdown:
        print(text)
    else:
        print(args.output or args.markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
