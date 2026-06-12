#!/usr/bin/env python
"""Pesquisa ampla PNCP para itens de conectividade do Projeto Rede10.

O script consulta a API pública do PNCP, detalha contratações, coleta itens,
baixa anexos selecionados e gera um relatório Markdown consolidado.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pncp_client as pncp
import search_pncp


PNCP_LEGACY = "https://pncp.gov.br/pncp-api/v1"


PROFILES = {
    "mpls_1gbps": {
        "label": "MPLS 1 Gbps",
        "queries": [
            "MPLS 1 Gbps comunicação de dados",
            "rede privada MPLS 1000 Mbps",
            "L3VPN MPLS 1 Gbps fibra óptica",
            "link MPLS 1GB comunicação dados",
        ],
        "must": ["mpls"],
        "nice": ["1 gbps", "1000 mbps", "1gb", "l3vpn", "rede privada", "fibra"],
    },
    "mpls_500mbps": {
        "label": "MPLS 500 Mbps",
        "queries": [
            "MPLS 500 Mbps comunicação de dados",
            "rede privada MPLS 500 Mbps fibra",
            "L3VPN MPLS 500 Mbps",
            "link MPLS 500MB",
        ],
        "must": ["mpls"],
        "nice": ["500 mbps", "500mb", "l3vpn", "rede privada", "fibra"],
    },
    "mpls_100mbps": {
        "label": "MPLS 100 Mbps",
        "queries": [
            "MPLS 100 Mbps comunicação de dados",
            "rede privada MPLS 100 Mbps fibra",
            "L3VPN MPLS 100 Mbps",
            "link MPLS 100MB",
        ],
        "must": ["mpls"],
        "nice": ["100 mbps", "100mb", "l3vpn", "rede privada", "fibra"],
    },
    "internet_4gbps_antiddos": {
        "label": "Internet dedicada 4 Gbps com Anti-DDoS e IP fixo",
        "queries": [
            "internet dedicada 4 Gbps Anti-DDoS IP fixo",
            "link dedicado internet 4000 Mbps DDoS",
            "internet corporativa 4Gbps anti ddos",
            "acesso corporativo internet 4 Gbps cidr",
        ],
        "must": ["internet"],
        "nice": ["4 gbps", "4000 mbps", "4gb", "ddos", "anti-ddos", "ip fixo", "cidr"],
    },
    "internet_2gbps_antiddos": {
        "label": "Internet dedicada 2 Gbps com Anti-DDoS e IP fixo",
        "queries": [
            "internet dedicada 2 Gbps Anti-DDoS IP fixo",
            "link dedicado internet 2000 Mbps DDoS",
            "internet corporativa 2Gbps anti ddos",
            "acesso dedicado internet 2 Gbps cidr",
        ],
        "must": ["internet"],
        "nice": ["2 gbps", "2000 mbps", "2gb", "ddos", "anti-ddos", "ip fixo", "cidr"],
    },
    "link_dedicado_25gbps": {
        "label": "Link dedicado ponto-a-ponto 25 Gbps / alta capacidade",
        "queries": [
            "link dedicado ponto a ponto 25 Gbps",
            "LAN-to-LAN 25 Gbps fibra óptica",
            "Metro Ethernet 25Gbps",
            "link dedicado ponto a ponto 10 Gbps LAN-to-LAN",
            "Metro Ethernet 10 Gbps comunicação ponto a ponto",
            "interligação datacenter 10 Gbps fibra dedicada",
        ],
        "must": ["link"],
        "nice": ["25 gbps", "25gb", "10 gbps", "10gb", "lan-to-lan", "metro ethernet", "ponto a ponto", "fibra"],
    },
}


ARTIFACT_TERMS = [
    "edital", "termo", "referencia", "referência", "tr", "estudo", "etp",
    "cotacao", "cotação", "proposta", "mapa", "preco", "preço",
    "memoria", "memória", "calculo", "cálculo", "anexo",
]


def norm(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"\s+", " ", text.lower()).strip()
    return text


def safe_name(value: str, limit: int = 90) -> str:
    clean = re.sub(r"[^A-Za-z0-9._-]+", "_", norm(value)).strip("_")
    return (clean or "pncp")[:limit]


def control_parts(row: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    control = row.get("numeroControlePNCP") or row.get("numeroControlePncp")
    return pncp.split_control(control) if control else None


def legacy_json(path: str, retries: int = 1, timeout: int = 25) -> Any:
    url = PNCP_LEGACY + path
    last = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Codex-PNCP-Rede10/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else None
        except Exception as exc:
            last = exc
            if attempt < retries:
                time.sleep(attempt)
    raise RuntimeError(f"Falha em {url}: {last}")


def download_url(url: str, dest: Path, retries: int = 3) -> bool:
    last = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Codex-PNCP-Rede10/1.0"})
            with urllib.request.urlopen(req, timeout=90) as response:
                dest.write_bytes(response.read())
            return True
        except Exception as exc:
            last = exc
            if attempt < retries:
                time.sleep(attempt)
    print(f"AVISO: falha ao baixar {url}: {last}")
    return False


def get_items(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    parts = control_parts(row)
    if not parts:
        return []
    try:
        data = legacy_json(f"/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}/itens")
        return data if isinstance(data, list) else []
    except Exception:
        return []


def get_files(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    parts = control_parts(row)
    if not parts:
        return []
    try:
        data = legacy_json(f"/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}/arquivos")
        return data if isinstance(data, list) else []
    except Exception:
        return []


def item_text(item: Dict[str, Any]) -> str:
    return " ".join(str(item.get(k) or "") for k in [
        "descricao", "descricaoItem", "materialOuServicoNome", "criterioJulgamentoNome",
        "unidadeMedida", "valorUnitarioEstimado", "valorTotal",
    ])


def profile_score(profile: Dict[str, Any], row: Dict[str, Any], items: List[Dict[str, Any]]) -> float:
    text = norm(search_pncp.searchable_text(row) + " " + " ".join(item_text(i) for i in items))
    score = float(row.get("_scoreSimilaridade") or 0)
    for term in profile.get("must", []):
        if norm(term) in text:
            score += 5
        else:
            score -= 2
    for term in profile.get("nice", []):
        if norm(term) in text:
            score += 3
    for bad in search_pncp.NEGATIVE_TERMS:
        if norm(bad) in text:
            score -= 10
    return round(score, 2)


def item_matches(profile: Dict[str, Any], items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    matched = []
    terms = [norm(t) for t in profile.get("must", []) + profile.get("nice", [])]
    for item in items:
        text = norm(item_text(item))
        hits = [t for t in terms if t and t in text]
        if hits:
            x = dict(item)
            x["_hitsPerfil"] = hits
            matched.append(x)
    return matched


def collect_for_profile(profile_key: str, profile: Dict[str, Any], args: argparse.Namespace) -> List[Dict[str, Any]]:
    seen = {}
    start = dt.date.today() - dt.timedelta(days=args.days)
    end = dt.date.today()
    for query in profile["queries"]:
        ns = argparse.Namespace(
            query=query,
            days=args.days,
            from_date=start.isoformat(),
            to_date=end.isoformat(),
            modalidades=args.modalidades,
            uf=args.uf,
            max_pages=args.max_pages,
            top=args.top_per_query,
            min_score=args.min_score,
            include_contracts=args.include_contracts,
            monthly_windows=args.monthly_windows,
            out=None,
            markdown=None,
        )
        print(f"[{profile_key}] consulta: {query}")
        for row in search_pncp.collect(ns):
            if "_avisosConsulta" in row:
                continue
            key = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp")
            if not key:
                continue
            if key not in seen or row.get("_scoreSimilaridade", 0) > seen[key].get("_scoreSimilaridade", 0):
                row["_queryPerfil"] = query
                seen[key] = row

    preliminary = sorted(seen.values(), key=lambda x: x.get("_scoreSimilaridade", 0), reverse=True)[: args.detail_limit_per_profile]
    enriched = []
    for row in preliminary:
        detail = {}
        try:
            detail = pncp.contratacao_por_controle(row.get("numeroControlePNCP") or row.get("numeroControlePncp"))
        except Exception:
            detail = {}
        items = get_items(row)
        files = get_files(row)
        final = dict(row)
        final["_detalheContratacao"] = detail
        final["_itens"] = items
        final["_itensAderentes"] = item_matches(profile, items)
        final["_arquivos"] = files
        final["_scorePerfil"] = profile_score(profile, row, items)
        enriched.append(final)
    enriched.sort(key=lambda x: x.get("_scorePerfil", 0), reverse=True)
    return enriched[: args.top_per_profile]


def row_pre_score(profile: Dict[str, Any], row: Dict[str, Any]) -> float:
    text = norm(search_pncp.searchable_text(row))
    score = 0.0
    for term in profile.get("must", []):
        score += 5 if norm(term) in text else -1
    for term in profile.get("nice", []):
        if norm(term) in text:
            score += 3
    for term in ["link", "internet", "mpls", "fibra", "telecom", "comunicacao de dados", "comunicação de dados"]:
        if norm(term) in text:
            score += 1
    for bad in search_pncp.NEGATIVE_TERMS:
        if norm(bad) in text:
            score -= 10
    return round(score, 2)


def month_windows(start: dt.date, end: dt.date):
    cur = dt.date(start.year, start.month, 1)
    while cur <= end:
        nxt = dt.date(cur.year + 1, 1, 1) if cur.month == 12 else dt.date(cur.year, cur.month + 1, 1)
        yield max(cur, start), min(nxt - dt.timedelta(days=1), end)
        cur = nxt


def arg_date(value: Optional[str], default: dt.date) -> dt.date:
    return dt.datetime.strptime(value, "%Y-%m-%d").date() if value else default


    rows_by_key: Dict[str, Dict[str, Any]] = {}
def load_candidate_inputs(paths: str) -> Dict[str, Dict[str, Any]]:
    rows_by_key: Dict[str, Dict[str, Any]] = {}
    for pattern in paths.split(","):
        for path in sorted(Path().glob(pattern.strip())):
            try:
                rows = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                print(f"AVISO: falha ao ler {path}: {exc}")
                continue
            for row in rows:
                key = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp")
                if key:
                    rows_by_key.setdefault(key, row)
    return rows_by_key


def collect_single_pass(profile_keys: List[str], args: argparse.Namespace) -> Dict[str, List[Dict[str, Any]]]:
    rows_by_key: Dict[str, Dict[str, Any]] = {}
    if args.candidate_input:
        rows_by_key = load_candidate_inputs(args.candidate_input)
    else:
        default_end = dt.date.today()
        default_start = default_end - dt.timedelta(days=args.days)
        start = arg_date(args.from_date, default_start)
        end = arg_date(args.to_date, default_end)
        modalidades = [int(x) for x in str(args.modalidades).split(",") if x.strip()]
        for win_start, win_end in month_windows(start, end):
            print(f"[single-pass] janela {win_start}..{win_end}")
            for modalidade in modalidades:
                for label, fn in [
                    ("publicacao", pncp.contratacoes_por_publicacao),
                    ("atualizacao", pncp.contratacoes_por_atualizacao),
                ]:
                    try:
                        for row in fn(win_start, win_end, modalidade=modalidade, max_pages=args.max_pages, uf=args.uf):
                            key = row.get("numeroControlePNCP") or row.get("numeroControlePncp")
                            if not key:
                                continue
                            text = norm(search_pncp.searchable_text(row))
                            if not any(t in text for t in ["link", "internet", "mpls", "fibra", "telecom", "comunicacao", "comunicação", "lan-to-lan", "metro ethernet", "sd-wan", "sdwan"]):
                                continue
                            row["_singlePassOrigem"] = f"{label}:{modalidade}:{win_start}:{win_end}"
                            rows_by_key.setdefault(key, row)
                    except Exception as exc:
                        print(f"AVISO {label} modalidade {modalidade} {win_start}..{win_end}: {exc}")
            if args.include_contracts:
                try:
                    for row in pncp.contratos_por_publicacao(win_start, win_end, max_pages=args.max_pages, uf=args.uf):
                        key = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp")
                        if key:
                            rows_by_key.setdefault(key, row)
                except Exception as exc:
                    print(f"AVISO contratos {win_start}..{win_end}: {exc}")

    all_rows = list(rows_by_key.values())
    print(f"[single-pass] candidatos telecom/TIC: {len(all_rows)}")
    if args.candidate_cache:
        Path(args.candidate_cache).parent.mkdir(parents=True, exist_ok=True)
        Path(args.candidate_cache).write_text(json.dumps(all_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.candidate_cache_only:
        return {key: [] for key in profile_keys}
    results: Dict[str, List[Dict[str, Any]]] = {}
    detail_cache: Dict[str, Dict[str, Any]] = {}
    item_cache: Dict[str, List[Dict[str, Any]]] = {}
    file_cache: Dict[str, List[Dict[str, Any]]] = {}
    for key in profile_keys:
        profile = PROFILES[key]
        preliminary = sorted(all_rows, key=lambda row: row_pre_score(profile, row), reverse=True)[: args.detail_limit_per_profile]
        enriched = []
        for row in preliminary:
            control = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp") or ""
            if args.skip_detail:
                detail_cache[control] = {}
            elif control not in detail_cache:
                try:
                    detail_cache[control] = pncp.contratacao_por_controle(control) if control else {}
                except Exception:
                    detail_cache[control] = {}
            if control not in item_cache:
                item_cache[control] = get_items(row)
            if args.skip_files:
                file_cache[control] = []
            elif control not in file_cache:
                file_cache[control] = get_files(row)
            detail = detail_cache[control]
            items = item_cache[control]
            files = file_cache[control]
            final = dict(search_pncp.add_links(row))
            final["_detalheContratacao"] = detail
            final["_itens"] = items
            final["_itensAderentes"] = item_matches(profile, items)
            final["_arquivos"] = files
            final["_scorePerfil"] = profile_score(profile, final, items)
            enriched.append(final)
        enriched.sort(key=lambda x: x.get("_scorePerfil", 0), reverse=True)
        results[key] = enriched[: args.top_per_profile]
    return results


def should_download(file_info: Dict[str, Any]) -> bool:
    text = norm(" ".join(str(file_info.get(k) or "") for k in file_info.keys()))
    return any(norm(term) in text for term in ARTIFACT_TERMS)


def persist_profile(profile_key: str, rows: List[Dict[str, Any]], root: Path, max_downloads: int) -> None:
    folder = root / profile_key
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "resultados.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    downloads = 0
    for row in rows:
        control = row.get("numeroControlePNCP") or row.get("numeroControlePncp")
        if not control:
            continue
        parts = control_parts(row)
        if not parts:
            continue
        org = ((row.get("orgaoEntidade") or {}).get("razaoSocial") or "orgao")
        proc_dir = folder / f"{safe_name(control)}_{safe_name(org, 35)}"
        proc_dir.mkdir(parents=True, exist_ok=True)
        (proc_dir / "detalhe.json").write_text(json.dumps(row.get("_detalheContratacao") or {}, ensure_ascii=False, indent=2), encoding="utf-8")
        (proc_dir / "itens.json").write_text(json.dumps(row.get("_itens") or [], ensure_ascii=False, indent=2), encoding="utf-8")
        (proc_dir / "itens_aderentes.json").write_text(json.dumps(row.get("_itensAderentes") or [], ensure_ascii=False, indent=2), encoding="utf-8")
        (proc_dir / "arquivos.json").write_text(json.dumps(row.get("_arquivos") or [], ensure_ascii=False, indent=2), encoding="utf-8")
        for idx, f in enumerate(row.get("_arquivos") or [], 1):
            if downloads >= max_downloads:
                return
            if not should_download(f):
                continue
            url = f.get("url") or f.get("uri")
            if not url:
                continue
            name = f.get("titulo") or f.get("nome") or f.get("tipoDocumentoNome") or f"arquivo_{idx}"
            ext = ".pdf" if ".pdf" in norm(name) or True else ""
            dest = proc_dir / f"{idx:02d}_{safe_name(name, 70)}{ext}"
            if download_url(url, dest):
                downloads += 1


def md_value(row: Dict[str, Any]) -> str:
    detail = row.get("_detalheContratacao") or {}
    value = (
        detail.get("valorTotalHomologado")
        or detail.get("valorTotalEstimado")
        or row.get("valorTotalHomologado")
        or row.get("valorTotalEstimado")
        or ""
    )
    return str(value)


def row_org(row: Dict[str, Any]) -> str:
    return ((row.get("orgaoEntidade") or {}).get("razaoSocial") or (row.get("_detalheContratacao") or {}).get("orgaoEntidade", {}).get("razaoSocial") or "")


def make_report(all_results: Dict[str, List[Dict[str, Any]]], out: Path, args: argparse.Namespace) -> None:
    lines = [
        "# Pesquisa ampla PNCP - Projeto Rede10",
        "",
        f"Data da pesquisa: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Janela: últimos {args.days} dias",
        f"Modalidades pesquisadas: {args.modalidades}",
        f"UF: {args.uf or 'todas'}",
        "",
        "## Observações metodológicas",
        "",
        "- A pesquisa usou a API pública de consulta do PNCP e os endpoints públicos de itens e arquivos.",
        "- Valores globais não foram convertidos automaticamente em preço unitário quando o item não trouxe quantidade/unidade suficiente.",
        "- A coluna de itens aderentes indica achados textuais nos itens do PNCP; a validação final deve conferir edital/TR/planilha do órgão.",
        "",
    ]
    for key, rows in all_results.items():
        profile = PROFILES[key]
        lines += [
            f"## {profile['label']}",
            "",
            "| Score | Órgão | PNCP | Modalidade | Objeto | Valor documentado | Itens aderentes | Link |",
            "| ---: | --- | --- | --- | --- | ---: | --- | --- |",
        ]
        for row in rows:
            control = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or ""
            modalidade = row.get("modalidadeNome") or (row.get("_detalheContratacao") or {}).get("modalidadeNome") or ""
            objeto = str(row.get("objetoCompra") or (row.get("_detalheContratacao") or {}).get("objetoCompra") or "").replace("|", "/")
            link = row.get("linkPncp") or ""
            itens = row.get("_itensAderentes") or []
            itens_txt = "; ".join(
                f"{i.get('numeroItem','')}: {str(i.get('descricao') or i.get('descricaoItem') or '')[:90]}"
                for i in itens[:3]
            )
            lines.append(
                f"| {row.get('_scorePerfil','')} | {row_org(row)} | {control} | {modalidade} | {objeto[:180]} | {md_value(row)} | {itens_txt} | {link} |"
            )
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Pesquisa ampla PNCP para contratação de rede/Internet")
    parser.add_argument("--days", type=int, default=730)
    parser.add_argument("--from-date")
    parser.add_argument("--to-date")
    parser.add_argument("--modalidades", default="6,8,9")
    parser.add_argument("--uf")
    parser.add_argument("--max-pages", type=int, default=8)
    parser.add_argument("--top-per-query", type=int, default=35)
    parser.add_argument("--top-per-profile", type=int, default=12)
    parser.add_argument("--detail-limit-per-profile", type=int, default=25)
    parser.add_argument("--min-score", type=float, default=3.0)
    parser.add_argument("--monthly-windows", action="store_true")
    parser.add_argument("--include-contracts", action="store_true")
    parser.add_argument("--max-downloads-per-profile", type=int, default=30)
    parser.add_argument("--out-dir", default="PNCP_PESQUISA_AMPLA_REDE10")
    parser.add_argument("--profiles", help="Lista de perfis separados por virgula. Padrao: todos")
    parser.add_argument("--single-pass", action="store_true", help="Enumera PNCP uma vez por janelas mensais e reusa candidatos para todos os perfis")
    parser.add_argument("--candidate-cache")
    parser.add_argument("--candidate-input", help="Glob ou lista de globs separados por virgula com candidatos JSON")
    parser.add_argument("--candidate-cache-only", action="store_true")
    parser.add_argument("--skip-detail", action="store_true", help="Nao consulta detalhe da compra; usa apenas dados da listagem e itens")
    parser.add_argument("--skip-files", action="store_true", help="Nao consulta lista de arquivos nem baixa anexos")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    all_results: Dict[str, List[Dict[str, Any]]] = {}
    profile_keys = [p.strip() for p in args.profiles.split(",")] if args.profiles else list(PROFILES)
    if args.single_pass:
        all_results = collect_single_pass(profile_keys, args)
        for key, rows in all_results.items():
            persist_profile(key, rows, out_dir, args.max_downloads_per_profile)
            print(f"[{key}] {len(rows)} resultados")
    else:
        for key in profile_keys:
            profile = PROFILES[key]
            rows = collect_for_profile(key, profile, args)
            all_results[key] = rows
            persist_profile(key, rows, out_dir, args.max_downloads_per_profile)
            print(f"[{key}] {len(rows)} resultados")

    (out_dir / "resultados_consolidados.json").write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8")
    make_report(all_results, out_dir / "RELATORIO_PESQUISA_AMPLA_PNCP.md", args)
    print(f"Relatório: {out_dir / 'RELATORIO_PESQUISA_AMPLA_PNCP.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
