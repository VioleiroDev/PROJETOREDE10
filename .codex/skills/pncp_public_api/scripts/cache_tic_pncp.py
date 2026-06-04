#!/usr/bin/env python
"""Cria cache JSONL de contratações TIC recentes do PNCP.

Este script nao tenta baixar "todo o PNCP"; ele consulta janelas mensais e
mantem apenas registros com vocabulário TIC. Use max-pages alto se quiser
ampliar a coleta, sempre respeitando estabilidade da API.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Dict, Iterable, List

import search_pncp


TIC_QUERIES = [
    "tecnologia informação software hardware informática",
    "serviço rede telecom internet link fibra",
    "MPLS SD-WAN VPN comunicação dados",
    "firewall segurança cibernética datacenter nuvem backup",
]


def month_windows(start: dt.date, end: dt.date):
    cur = dt.date(start.year, start.month, 1)
    while cur <= end:
        if cur.month == 12:
            nxt = dt.date(cur.year + 1, 1, 1)
        else:
            nxt = dt.date(cur.year, cur.month + 1, 1)
        yield max(cur, start), min(nxt - dt.timedelta(days=1), end)
        cur = nxt


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Cache TIC PNCP em JSONL")
    parser.add_argument("--days", type=int, default=730)
    parser.add_argument("--out", default="PNCP_CACHE/tic_ultimos_2_anos.jsonl")
    parser.add_argument("--max-pages", type=int, default=50)
    parser.add_argument("--top-per-query", type=int, default=200)
    parser.add_argument("--modalidades", default="6")
    args = parser.parse_args()

    end = dt.date.today()
    start = end - dt.timedelta(days=args.days)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    seen = set()
    count = 0

    with out.open("w", encoding="utf-8") as fh:
        for win_start, win_end in month_windows(start, end):
            for query in TIC_QUERIES:
                ns = argparse.Namespace(
                    query=query,
                    days=args.days,
                    from_date=win_start.isoformat(),
                    to_date=win_end.isoformat(),
                    modalidades=args.modalidades,
                    uf=None,
                    max_pages=args.max_pages,
                    top=args.top_per_query,
                    min_score=3.0,
                    include_contracts=True,
                    out=None,
                    markdown=None,
                )
                for row in search_pncp.collect(ns):
                    if "_avisosConsulta" in row:
                        continue
                    key = row.get("numeroControlePNCP") or row.get("numeroControlePncp") or row.get("idContratoPncp") or json.dumps(row, sort_keys=True, ensure_ascii=False)[:300]
                    if key in seen:
                        continue
                    seen.add(key)
                    row["_cacheQuery"] = query
                    row["_cacheWindow"] = f"{win_start.isoformat()}..{win_end.isoformat()}"
                    fh.write(json.dumps(row, ensure_ascii=False) + "\n")
                    count += 1
            print(f"{win_start}..{win_end}: {count} registros acumulados")
    print(f"Cache final: {out} ({count} registros)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
