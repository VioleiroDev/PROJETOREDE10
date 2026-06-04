#!/usr/bin/env python
"""Busca objetos semelhantes na API publica PNCP.

Exemplo:
  python search_pncp.py --query "link MPLS comunicação de dados" --days 730 --top 20 --out resultados.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterable, List

import pncp_client as pncp


DEFAULT_TIC_TERMS = [
    "tecnologia", "informática", "informatica", "software", "hardware", "rede", "redes",
    "telecom", "telecomunicação", "telecomunicacao", "internet", "link", "mpls",
    "lan-to-lan", "metro ethernet", "fibra", "datacenter", "data center", "segurança",
    "seguranca", "firewall", "sd-wan", "vpn", "nuvem", "backup", "servidor",
]

NEGATIVE_TERMS = [
    "rede de agua", "redes de agua", "esgoto", "hidraulico", "hidraulica",
    "material esportivo", "redes esportivas", "fibra de vidro", "embarcacao",
    "jet sentado", "tubos", "conexoes", "fossa", "trofeus", "medalhas",
]

TELECOM_CORE_TERMS = [
    "internet", "link", "links", "telecom", "telecomunicacao", "telecomunicacoes",
    "mpls", "sd-wan", "sdwan", "fibra optica", "metro ethernet", "lan-to-lan",
    "comunicacao de dados", "dados", "vpn",
]


def norm(text: Any) -> str:
    value = unicodedata.normalize("NFKD", str(text or ""))
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return value.lower()


def tokens(text: str) -> List[str]:
    return [t for t in re.split(r"[^a-z0-9]+", norm(text)) if len(t) >= 3]


def searchable_text(row: Dict[str, Any]) -> str:
    parts = [
        row.get("objetoCompra"),
        row.get("informacaoComplementar"),
        row.get("numeroCompra"),
        row.get("processo"),
        row.get("numeroControlePNCP"),
        row.get("modalidadeNome"),
        row.get("situacaoCompraNome"),
    ]
    orgao = row.get("orgaoEntidade") or {}
    unidade = row.get("unidadeOrgao") or {}
    parts += [orgao.get("razaoSocial"), unidade.get("nomeUnidade"), unidade.get("ufSigla"), unidade.get("municipioNome")]
    return " ".join(str(p or "") for p in parts)


def score(row: Dict[str, Any], query: str) -> float:
    hay = norm(searchable_text(row))
    query_terms = tokens(query)
    if not query_terms:
        return 0
    score_value = 0.0
    for term in query_terms:
        if term in hay:
            score_value += 3.0
    phrase = norm(query)
    if phrase and phrase in hay:
        score_value += 10.0
    for term in DEFAULT_TIC_TERMS:
        if norm(term) in hay:
            score_value += 0.7
    for term in NEGATIVE_TERMS:
        if norm(term) in hay:
            score_value -= 8.0
    query_has_telecom = any(norm(term) in norm(query) for term in TELECOM_CORE_TERMS)
    hay_has_telecom = any(norm(term) in hay for term in TELECOM_CORE_TERMS)
    if query_has_telecom and not hay_has_telecom:
        score_value -= 8.0
    # Preferir registros com valores documentados e numero PNCP.
    if row.get("numeroControlePNCP") or row.get("numeroControlePncp"):
        score_value += 1.0
    for key in ("valorTotalEstimado", "valorTotalHomologado", "valorGlobal", "valorGlobalContrato", "valorInicial"):
        if row.get(key) not in (None, "", 0):
            score_value += 1.5
            break
    return score_value


def dedupe(rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    out = []
    for row in rows:
        key = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp") or json.dumps(row, sort_keys=True, ensure_ascii=False)[:300]
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def add_links(row: Dict[str, Any]) -> Dict[str, Any]:
    row = dict(row)
    control = row.get("numeroControlePNCP") or row.get("numeroControlePncp")
    if control:
        parts = pncp.split_control(control)
        if parts:
            row["linkPncp"] = f"https://pncp.gov.br/app/editais/{parts['cnpj']}/{parts['ano']}/{parts['sequencial']}"
    return row


def collect(args: argparse.Namespace) -> List[Dict[str, Any]]:
    end = dt.datetime.strptime(args.to_date, "%Y-%m-%d").date() if args.to_date else dt.date.today()
    start = dt.datetime.strptime(args.from_date, "%Y-%m-%d").date() if args.from_date else end - dt.timedelta(days=args.days)
    modalidades = [int(x) for x in str(args.modalidades).split(",") if x.strip()]
    rows: List[Dict[str, Any]] = []
    errors: List[str] = []

    windows = [(start, end)]
    if args.monthly_windows and (end - start).days > 45:
        windows = []
        cur = dt.date(start.year, start.month, 1)
        while cur <= end:
            nxt = dt.date(cur.year + 1, 1, 1) if cur.month == 12 else dt.date(cur.year, cur.month + 1, 1)
            windows.append((max(cur, start), min(nxt - dt.timedelta(days=1), end)))
            cur = nxt

    for win_start, win_end in windows:
        for modalidade in modalidades:
            try:
                rows.extend(pncp.contratacoes_por_publicacao(win_start, win_end, modalidade=modalidade, max_pages=args.max_pages, uf=args.uf))
            except Exception as exc:
                errors.append(f"contratacoes/publicacao modalidade {modalidade} {win_start}..{win_end}: {exc}")
            try:
                rows.extend(pncp.contratacoes_por_atualizacao(win_start, win_end, modalidade=modalidade, max_pages=args.max_pages, uf=args.uf))
            except Exception as exc:
                errors.append(f"contratacoes/atualizacao modalidade {modalidade} {win_start}..{win_end}: {exc}")

        if args.include_contracts:
            try:
                rows.extend(pncp.contratos_por_publicacao(win_start, win_end, max_pages=args.max_pages, uf=args.uf))
            except Exception as exc:
                errors.append(f"contratos {win_start}..{win_end}: {exc}")

    ranked = []
    effective_min_score = args.min_score
    if any(norm(term) in norm(args.query) for term in TELECOM_CORE_TERMS):
        effective_min_score = max(effective_min_score, 10.0)
    for row in dedupe(rows):
        s = score(row, args.query)
        if s >= effective_min_score:
            item = add_links(row)
            item["_scoreSimilaridade"] = round(s, 2)
            ranked.append(item)
    ranked.sort(key=lambda r: r.get("_scoreSimilaridade", 0), reverse=True)
    result = ranked[: args.top]
    if errors:
        result.append({"_avisosConsulta": errors})
    return result


def to_markdown(rows: List[Dict[str, Any]]) -> str:
    lines = [
        "| Score | Órgão | UF | Número PNCP / contrato | Modalidade | Objeto | Valor documentado | Link |",
        "| ---: | --- | --- | --- | --- | --- | ---: | --- |",
    ]
    for row in rows:
        if "_avisosConsulta" in row:
            continue
        orgao = (row.get("orgaoEntidade") or {}).get("razaoSocial") or row.get("nomeOrgao") or ""
        unidade = row.get("unidadeOrgao") or {}
        uf = unidade.get("ufSigla") or row.get("uf") or ""
        numero = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp") or row.get("numeroContratoEmpenho") or ""
        modalidade = row.get("modalidadeNome") or row.get("modalidadeContratacaoNome") or ""
        objeto = str(row.get("objetoCompra") or row.get("objetoContrato") or row.get("objeto") or "").replace("|", "/")
        valor = row.get("valorTotalHomologado") or row.get("valorTotalEstimado") or row.get("valorGlobal") or row.get("valorInicial") or ""
        link = row.get("linkPncp") or row.get("linkSistemaOrigem") or ""
        lines.append(f"| {row.get('_scoreSimilaridade','')} | {orgao} | {uf} | {numero} | {modalidade} | {objeto[:300]} | {valor} | {link} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Pesquisa PNCP por similaridade textual")
    parser.add_argument("--query", required=True, help="Objeto ou termos de busca")
    parser.add_argument("--days", type=int, default=730)
    parser.add_argument("--from-date")
    parser.add_argument("--to-date")
    parser.add_argument("--modalidades", default="6", help="Codigos separados por virgula. Padrao: 6 (Pregao eletronico)")
    parser.add_argument("--uf")
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--min-score", type=float, default=3.0)
    parser.add_argument("--include-contracts", action="store_true")
    parser.add_argument("--monthly-windows", action="store_true", help="Percorre a janela em blocos mensais para melhorar cobertura de buscas longas")
    parser.add_argument("--out")
    parser.add_argument("--markdown")
    args = parser.parse_args()

    rows = collect(args)
    payload = {
        "query": args.query,
        "generatedAt": dt.datetime.now().isoformat(timespec="seconds"),
        "source": "https://pncp.gov.br/api/consulta",
        "results": rows,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding="utf-8")
    if args.markdown:
        Path(args.markdown).parent.mkdir(parents=True, exist_ok=True)
        Path(args.markdown).write_text(to_markdown(rows), encoding="utf-8")
    if not args.out and not args.markdown:
        print(text)
    else:
        print(f"{len([r for r in rows if '_avisosConsulta' not in r])} resultados gravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
