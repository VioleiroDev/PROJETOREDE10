#!/usr/bin/env python
"""Cliente simples para a API publica de consulta do PNCP.

Usa apenas biblioteca padrao para funcionar em ambientes Codex/Windows sem
instalacao de dependencias. A API de consulta publica nao exige token.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Iterator, List, Optional


BASE_URL = "https://pncp.gov.br/api/consulta"
OPENAPI_URL = "https://pncp.gov.br/pncp-consulta/v3/api-docs"


class PncpError(RuntimeError):
    pass


def _compact_params(params: Dict[str, Any]) -> str:
    clean = {k: v for k, v in params.items() if v not in (None, "", [])}
    return urllib.parse.urlencode(clean)


def get_json(path: str, params: Optional[Dict[str, Any]] = None, retries: int = 3, sleep: float = 1.0) -> Dict[str, Any]:
    url = BASE_URL + path
    if params:
        url += "?" + _compact_params(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Codex-PNCP-Consulta/1.0"})
    last_error: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise PncpError(f"HTTP {exc.code} em {url}: {body[:600]}") from exc
        except Exception as exc:  # pragma: no cover - rede externa
            last_error = exc
            if attempt < retries:
                time.sleep(sleep * attempt)
    raise PncpError(f"Falha ao consultar {url}: {last_error}")


def yyyymmdd(date_value: dt.date) -> str:
    return date_value.strftime("%Y%m%d")


def parse_date(value: str) -> dt.date:
    return dt.datetime.strptime(value, "%Y-%m-%d").date()


def split_control(numero_controle: str) -> Optional[Dict[str, int | str]]:
    """Extrai cnpj, ano e sequencial de numeroControlePNCP.

    Exemplo: 12345678000199-1-000123/2025
    """

    try:
        left, year = numero_controle.split("/")
        cnpj, _, seq = left.split("-")
        return {"cnpj": cnpj, "ano": int(year), "sequencial": int(seq)}
    except Exception:
        return None


@dataclass
class Page:
    data: List[Dict[str, Any]]
    total_registros: Optional[int] = None
    total_paginas: Optional[int] = None


def _page_from_response(payload: Dict[str, Any]) -> Page:
    return Page(
        data=payload.get("data") or [],
        total_registros=payload.get("totalRegistros") or payload.get("total_registros"),
        total_paginas=payload.get("totalPaginas") or payload.get("total_paginas"),
    )


def iter_pages(path: str, params: Dict[str, Any], max_pages: int = 20, tamanho_pagina: int = 50) -> Iterator[Dict[str, Any]]:
    for pagina in range(1, max_pages + 1):
        req_params = dict(params)
        req_params["pagina"] = pagina
        req_params["tamanhoPagina"] = max(10, tamanho_pagina)
        payload = get_json(path, req_params)
        page = _page_from_response(payload)
        for item in page.data:
            yield item
        if not page.data:
            break
        if page.total_paginas and pagina >= page.total_paginas:
            break


def contratacoes_por_publicacao(
    data_inicial: dt.date,
    data_final: dt.date,
    modalidade: int = 6,
    max_pages: int = 20,
    uf: Optional[str] = None,
) -> Iterator[Dict[str, Any]]:
    params: Dict[str, Any] = {
        "dataInicial": yyyymmdd(data_inicial),
        "dataFinal": yyyymmdd(data_final),
        "codigoModalidadeContratacao": modalidade,
        "uf": uf,
    }
    yield from iter_pages("/v1/contratacoes/publicacao", params, max_pages=max_pages)


def contratacoes_por_atualizacao(
    data_inicial: dt.date,
    data_final: dt.date,
    modalidade: int = 6,
    max_pages: int = 20,
    uf: Optional[str] = None,
) -> Iterator[Dict[str, Any]]:
    params: Dict[str, Any] = {
        "dataInicial": yyyymmdd(data_inicial),
        "dataFinal": yyyymmdd(data_final),
        "codigoModalidadeContratacao": modalidade,
        "uf": uf,
    }
    yield from iter_pages("/v1/contratacoes/atualizacao", params, max_pages=max_pages)


def contratos_por_publicacao(data_inicial: dt.date, data_final: dt.date, max_pages: int = 20, uf: Optional[str] = None) -> Iterator[Dict[str, Any]]:
    # O endpoint de contratos nao aceita UF diretamente na especificacao publica.
    params = {"dataInicial": yyyymmdd(data_inicial), "dataFinal": yyyymmdd(data_final)}
    for item in iter_pages("/v1/contratos", params, max_pages=max_pages):
        if uf and (item.get("unidadeOrgao") or {}).get("ufSigla") != uf:
            continue
        yield item


def atas_por_atualizacao(data_inicial: dt.date, data_final: dt.date, max_pages: int = 20) -> Iterator[Dict[str, Any]]:
    params = {"dataInicial": yyyymmdd(data_inicial), "dataFinal": yyyymmdd(data_final)}
    yield from iter_pages("/v1/atas/atualizacao", params, max_pages=max_pages)


def contratacao_por_controle(numero_controle: str) -> Dict[str, Any]:
    parts = split_control(numero_controle)
    if not parts:
        raise ValueError(f"numeroControlePNCP invalido: {numero_controle}")
    return get_json(f"/v1/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Cliente PNCP basico")
    parser.add_argument("--control", help="numeroControlePNCP para detalhar uma contratacao")
    parser.add_argument("--from-date", default=(dt.date.today() - dt.timedelta(days=30)).isoformat())
    parser.add_argument("--to-date", default=dt.date.today().isoformat())
    parser.add_argument("--modalidade", type=int, default=6)
    parser.add_argument("--max-pages", type=int, default=2)
    args = parser.parse_args()

    if args.control:
        print(json.dumps(contratacao_por_controle(args.control), ensure_ascii=False, indent=2))
        return 0

    start = parse_date(args.from_date)
    end = parse_date(args.to_date)
    rows = list(contratacoes_por_publicacao(start, end, modalidade=args.modalidade, max_pages=args.max_pages))
    print(json.dumps(rows, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
