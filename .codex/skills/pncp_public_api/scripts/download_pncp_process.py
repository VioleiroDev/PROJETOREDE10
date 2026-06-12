#!/usr/bin/env python
"""Baixa artefatos PNCP a partir de numeros de controle.

Uso:
  python download_pncp_process.py --controls 11294386000108-1-000244/2024 --out PNCP_REFERENCIAS
"""

from __future__ import annotations

import argparse
import json
import re
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

import pncp_client as pncp


BASE_CONSULTA = "https://pncp.gov.br/api/consulta/v1"
BASE_LEGACY = "https://pncp.gov.br/pncp-api/v1"

DOCUMENT_TERMS = [
    "edital",
    "termo",
    "referencia",
    "referência",
    "tr",
    "etp",
    "estudo",
    "dfd",
    "mapa",
    "preco",
    "preço",
    "cotacao",
    "cotação",
    "memoria",
    "memória",
    "calculo",
    "cálculo",
    "proposta",
    "anexo",
]


def norm(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"\s+", " ", text.lower()).strip()
    return text


def safe_name(value: Any, limit: int = 100) -> str:
    clean = re.sub(r"[^A-Za-z0-9._-]+", "_", norm(value)).strip("_")
    return (clean or "pncp")[:limit]


def request_json(url: str, retries: int = 3, timeout: int = 45) -> Any:
    last: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Codex-PNCP-Rede10/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                raw = response.read().decode("utf-8", errors="replace")
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            last = exc
        except Exception as exc:
            last = exc
        if attempt < retries:
            time.sleep(attempt)
    raise RuntimeError(f"Falha ao consultar {url}: {last}")


def download(url: str, dest: Path, retries: int = 3) -> bool:
    last: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Codex-PNCP-Rede10/1.0"})
            with urllib.request.urlopen(req, timeout=120) as response:
                dest.write_bytes(response.read())
            return True
        except Exception as exc:
            last = exc
            if attempt < retries:
                time.sleep(attempt)
    print(f"AVISO: falha ao baixar {url}: {last}")
    return False


def file_url(parts: Dict[str, Any], index: int) -> str:
    return f"{BASE_LEGACY}/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}/arquivos/{index}"


def should_download(file_info: Dict[str, Any], all_files: bool) -> bool:
    if all_files:
        return True
    text = norm(" ".join(str(v) for v in file_info.values()))
    return any(norm(term) in text for term in DOCUMENT_TERMS)


def extract_file_name(file_info: Dict[str, Any], index: int) -> str:
    name = (
        file_info.get("titulo")
        or file_info.get("nome")
        or file_info.get("nomeArquivo")
        or file_info.get("tipoDocumentoNome")
        or file_info.get("tipoDocumento")
        or f"arquivo_{index}"
    )
    suffix = Path(str(name)).suffix
    if not suffix:
        content = norm(file_info.get("tipo") or file_info.get("contentType") or "")
        suffix = ".pdf" if "pdf" in content else ".bin"
    return f"{index:02d}_{safe_name(name, 75)}{suffix}"


def process_control(control: str, out_dir: Path, all_files: bool, metadata_only: bool) -> Dict[str, Any]:
    parts = pncp.split_control(control)
    if not parts:
        raise ValueError(f"Controle PNCP invalido: {control}")

    detail_url = f"{BASE_CONSULTA}/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}"
    items_url = f"{BASE_LEGACY}/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}/itens"
    files_url = f"{BASE_LEGACY}/orgaos/{parts['cnpj']}/compras/{parts['ano']}/{parts['sequencial']}/arquivos"

    errors = []
    try:
        detail = request_json(detail_url) or {}
    except Exception as exc:
        detail = {}
        errors.append(f"detalhe: {exc}")
        print(f"AVISO: detalhe indisponivel para {control}: {exc}")
    try:
        items = request_json(items_url) or []
    except Exception as exc:
        items = []
        errors.append(f"itens: {exc}")
        print(f"AVISO: itens indisponiveis para {control}: {exc}")
    try:
        files = request_json(files_url) or []
    except Exception as exc:
        files = []
        errors.append(f"arquivos: {exc}")
        print(f"AVISO: arquivos indisponiveis para {control}: {exc}")
    org = ((detail.get("orgaoEntidade") or {}).get("razaoSocial") or "orgao")
    folder = out_dir / f"{safe_name(control)}_{safe_name(org, 45)}"
    folder.mkdir(parents=True, exist_ok=True)

    (folder / "detalhe_contratacao.json").write_text(json.dumps(detail, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "itens.json").write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "arquivos.json").write_text(json.dumps(files, ensure_ascii=False, indent=2), encoding="utf-8")

    downloaded = []
    for idx, file_info in enumerate(files, 1):
        if not should_download(file_info, all_files):
            continue
        url = file_info.get("url") or file_info.get("uri") or file_url(parts, idx)
        dest = folder / extract_file_name(file_info, idx)
        ok = False if metadata_only else download(url, dest)
        downloaded.append({"index": idx, "url": url, "ok": ok, "arquivo": str(dest), "metadados": file_info})

    manifest = {
        "numeroControlePNCP": control,
        "orgao": org,
        "objeto": detail.get("objetoCompra"),
        "valorTotalEstimado": detail.get("valorTotalEstimado"),
        "valorTotalHomologado": detail.get("valorTotalHomologado"),
        "itens": len(items) if isinstance(items, list) else None,
        "arquivos": len(files) if isinstance(files, list) else None,
        "downloads": downloaded,
        "erros": errors,
        "pasta": str(folder),
    }
    (folder / "download_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def write_index(manifests: List[Dict[str, Any]], out_dir: Path) -> None:
    lines = ["# Downloads PNCP selecionados", ""]
    for item in manifests:
        lines += [
            f"## {item.get('numeroControlePNCP')}",
            "",
            f"- Orgao: {item.get('orgao')}",
            f"- Objeto: {item.get('objeto')}",
            f"- Valor estimado: {item.get('valorTotalEstimado')}",
            f"- Valor homologado: {item.get('valorTotalHomologado')}",
            f"- Pasta: `{item.get('pasta')}`",
            "",
            "| Arquivo | URL | Status |",
            "| --- | --- | --- |",
        ]
        for dl in item.get("downloads") or []:
            lines.append(f"| `{dl.get('arquivo')}` | {dl.get('url')} | {'ok' if dl.get('ok') else 'falha'} |")
        lines.append("")
    (out_dir / "INDICE_DOWNLOADS_PNCP.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Baixa detalhe, itens e arquivos de controles PNCP")
    parser.add_argument("--controls", required=True, help="Controles separados por virgula ou caminho de txt com um controle por linha")
    parser.add_argument("--out", default="PNCP_DOWNLOADS")
    parser.add_argument("--all-files", action="store_true", help="Baixa todos os arquivos; por padrao baixa so artefatos documentais provaveis")
    parser.add_argument("--metadata-only", action="store_true", help="Salva detalhe, itens e lista de arquivos sem baixar anexos")
    args = parser.parse_args()

    source = Path(args.controls)
    if source.exists():
        controls = [line.strip() for line in source.read_text(encoding="utf-8").splitlines() if line.strip() and not line.strip().startswith("#")]
    else:
        controls = [part.strip() for part in args.controls.split(",") if part.strip()]

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifests = []
    for control in controls:
        print(f"Baixando {control}...")
        manifests.append(process_control(control, out_dir, args.all_files, args.metadata_only))
    (out_dir / "download_summary.json").write_text(json.dumps(manifests, ensure_ascii=False, indent=2), encoding="utf-8")
    write_index(manifests, out_dir)
    print(f"Indice: {out_dir / 'INDICE_DOWNLOADS_PNCP.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
