#!/usr/bin/env python3
"""
Busca simples na base JSONL da skill ETP NAGEM V2.

Uso:
  python scripts/search_knowledge.py "service desk" --top 8
  python scripts/search_knowledge.py "licenciamento software" --domain software --top 10 --json
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "references" / "knowledge"

TEXT_FIELDS = [
    "retrieval_text",
    "similarity_retrieval_text",
    "objeto",
    "summary",
    "technology_domain",
    "subdomain",
    "solution_cluster",
    "procurement_type",
    "risk_level",
    "orgao",
    "numeroControlePNCP",
    "record_type",
    "knowledge_id",
]

STOPWORDS = {
    "a", "o", "e", "de", "da", "do", "das", "dos", "em", "para", "por",
    "com", "sem", "um", "uma", "os", "as", "no", "na", "nos", "nas",
    "ao", "à", "que", "se", "ou", "como", "contratacao", "contratação",
    "publica", "pública", "tic", "solucao", "solução",
}

def normalize(text: Any) -> str:
    if text is None:
        return ""
    text = str(text).lower()
    text = re.sub(r"[\W_]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())

def tokens(text: str) -> List[str]:
    return [t for t in normalize(text).split() if len(t) > 2 and t not in STOPWORDS]

def iter_jsonl_records() -> Iterable[Tuple[Path, int, Dict[str, Any]]]:
    for path in sorted(KNOWLEDGE_DIR.glob("*.jsonl")):
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(record, dict):
                    yield path, lineno, record

def record_text(record: Dict[str, Any]) -> str:
    parts: List[str] = []
    for field in TEXT_FIELDS:
        value = record.get(field)
        if value:
            parts.append(str(value))
    for key, value in record.items():
        if key in TEXT_FIELDS:
            continue
        if isinstance(value, str) and len(value) < 1000:
            parts.append(value)
    return " ".join(parts)

def field_match(record: Dict[str, Any], field: str, expected: str | None) -> bool:
    if not expected:
        return True
    return normalize(expected) in normalize(record.get(field, ""))

def score_record(query_terms: Counter, record: Dict[str, Any]) -> float:
    text = record_text(record)
    rec_terms = Counter(tokens(text))
    if not rec_terms:
        return 0.0

    overlap = sum(min(query_terms[t], rec_terms[t]) for t in query_terms)
    if overlap == 0:
        return 0.0

    # Weighted boosts matching the GPT priority rule.
    boost = 1.0
    weighted_fields = [
        ("technology_domain", 3.0),
        ("subdomain", 2.5),
        ("solution_cluster", 2.2),
        ("procurement_type", 1.7),
        ("risk_level", 1.3),
        ("ano", 1.1),
    ]
    qset = set(query_terms)
    for field, weight in weighted_fields:
        value_terms = set(tokens(str(record.get(field, ""))))
        if value_terms & qset:
            boost += weight

    # Prefer records that carry citation fields.
    if record.get("numeroControlePNCP"):
        boost += 0.8
    if record.get("etp_id") or record.get("tr_id"):
        boost += 0.8
    if record.get("orgao"):
        boost += 0.3
    if record.get("ano"):
        boost += 0.2

    norm = math.sqrt(sum(v * v for v in rec_terms.values()))
    return (overlap / max(norm, 1.0)) * boost

def citation(record: Dict[str, Any]) -> str:
    bits = []
    for field in ["etp_id", "tr_id", "orgao", "ano", "technology_domain", "subdomain", "solution_cluster", "procurement_type", "risk_level", "numeroControlePNCP"]:
        value = record.get(field)
        if value not in (None, "", []):
            bits.append(f"{field}={value}")
    return "; ".join(bits) if bits else "sem metadados de citação suficientes"

def main() -> int:
    parser = argparse.ArgumentParser(description="Busca precedentes na base local ETP NAGEM V2.")
    parser.add_argument("query", help="Termos da solução ou contratação")
    parser.add_argument("--top", type=int, default=8, help="Quantidade de resultados")
    parser.add_argument("--domain", help="Filtro por technology_domain")
    parser.add_argument("--subdomain", help="Filtro por subdomain")
    parser.add_argument("--cluster", help="Filtro por solution_cluster")
    parser.add_argument("--procurement-type", help="Filtro por procurement_type")
    parser.add_argument("--risk-level", help="Filtro por risk_level")
    parser.add_argument("--json", action="store_true", help="Emitir JSON em vez de texto")
    args = parser.parse_args()

    qterms = Counter(tokens(args.query))
    if not qterms:
        raise SystemExit("Consulta vazia após normalização.")

    results = []
    for path, lineno, rec in iter_jsonl_records():
        if not field_match(rec, "technology_domain", args.domain):
            continue
        if not field_match(rec, "subdomain", args.subdomain):
            continue
        if not field_match(rec, "solution_cluster", args.cluster):
            continue
        if not field_match(rec, "procurement_type", args.procurement_type):
            continue
        if not field_match(rec, "risk_level", args.risk_level):
            continue
        s = score_record(qterms, rec)
        if s > 0:
            results.append({
                "score": round(s, 4),
                "file": str(path.relative_to(ROOT)),
                "line": lineno,
                "record_type": rec.get("record_type"),
                "knowledge_id": rec.get("knowledge_id"),
                "numeroControlePNCP": rec.get("numeroControlePNCP"),
                "etp_id": rec.get("etp_id"),
                "tr_id": rec.get("tr_id"),
                "orgao": rec.get("orgao"),
                "ano": rec.get("ano"),
                "technology_domain": rec.get("technology_domain"),
                "subdomain": rec.get("subdomain"),
                "solution_cluster": rec.get("solution_cluster"),
                "procurement_type": rec.get("procurement_type"),
                "risk_level": rec.get("risk_level"),
                "objeto": rec.get("objeto"),
                "summary": rec.get("summary"),
                "citation": citation(rec),
            })

    results.sort(key=lambda r: r["score"], reverse=True)
    results = results[: max(args.top, 1)]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    if not results:
        print("Nenhum precedente encontrado na base local.")
        return 0

    for i, r in enumerate(results, 1):
        print(f"\n[{i}] score={r['score']} | {r.get('record_type') or 'registro'} | {r['file']}:{r['line']}")
        print(f"    citação: {r['citation']}")
        if r.get("objeto"):
            print(f"    objeto: {r['objeto']}")
        elif r.get("summary"):
            print(f"    resumo: {r['summary']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
