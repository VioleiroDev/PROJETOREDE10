---
name: pncp-public-api
description: Use esta skill quando o usuário pedir pesquisa de preços, contratações, licitações, editais, atas, contratos ou precedentes PNCP, especialmente em contratações públicas brasileiras de TIC dos últimos 2 anos.
---

# PNCP Public API

Esta skill conecta o trabalho do Codex à API pública de consultas do Portal Nacional de Contratações Públicas (PNCP), sem login, para localizar contratações, contratos e atas semelhantes ao objeto informado pelo usuário.

## Regra de uso

Sempre que esta skill for acionada, execute pelo menos uma consulta online à API pública do PNCP antes de responder. O cache local só pode ser usado como apoio ou fallback quando a API estiver indisponível, lenta ou retornar erro documentado.

Quando a tarefa envolver DFD, ETP, Termo de Referência, pesquisa de preços, estimativa de valor, precedentes ou comparação de contratação pública:

1. Consulte a API pública do PNCP antes de afirmar que não existem precedentes, preços ou contratações similares.
2. Use janela padrão de 730 dias quando o usuário pedir "últimos 2 anos".
3. Busque por termos técnicos do objeto e por sinônimos.
4. Separe:
   - resultados com `numeroControlePNCP`;
   - resultados apenas de contratos/atas;
   - referências auxiliares sem preço unitário.
5. Não invente preço unitário. Se a API retornar apenas valor global, marque como "valor global" e não como preço unitário.
6. Se a API oficial estiver instável, registre a falha e use cache local/links públicos apenas como apoio.
7. Registre na resposta ou no artefato a data da consulta, termos usados, janela pesquisada e eventuais limitações.

## Scripts

Os scripts ficam em `scripts/`:

### Pesquisa padrão de preços por objeto

Use primeiro `price_search_pncp.py` quando o usuário pedir preços, contratações semelhantes, itens homologados/estimados ou referências por objeto. Esse fluxo usa a busca textual pública do PNCP (`https://pncp.gov.br/api/search/`), consulta itens da compra e, quando disponível, resultados do item. Ele é mais rápido e mais aderente que a varredura por período quando há uma descrição técnica clara.

Exemplo para serviços de telecomunicações:

```powershell
python .codex\skills\pncp_public_api\scripts\price_search_pncp.py `
  --query "internet 2 Gbps anti-ddos" `
  --required "internet,2 gbps,ddos" `
  --forbidden "satélite,starlink,móvel" `
  --max-prices 10 `
  --output PNCP_CACHE\internet_2gbps_ddos.json `
  --markdown PNCP_CACHE\internet_2gbps_ddos.md
```

Regras deste fluxo:

- Priorize evidências com `tipo_valor = homologado`; use `estimado` quando não houver resultado.
- Use `--required` para termos técnicos essenciais, como capacidade, tecnologia, Anti-DDoS, MPLS, SD-WAN ou IP fixo.
- Use `--forbidden` para excluir falsos positivos, como satélite, móvel, Starlink, material médico, acessórios, telefonia ou serviços que não compõem o objeto.
- Não use automaticamente documentos de contrato como fonte de item de compra. O script extrai preço unitário apenas de documentos de `/compras/...`; contratos podem servir como referência documental auxiliar.
- Quando o item PNCP vier genérico, como "Serviço de Link Via Cabo", valide a aderência pelo texto do edital/aviso e pelos documentos baixados antes de usar como preço principal.

### Baixar documentos de processos selecionados

Depois de selecionar bons controles PNCP, use `download_pncp_process.py` para baixar detalhe, itens, lista de arquivos e anexos documentais.

```powershell
python .codex\skills\pncp_public_api\scripts\download_pncp_process.py `
  --controls "33892175000100-1-000033/2026,26963645000113-1-000038/2025" `
  --out PNCP_REFERENCIAS_SELECIONADAS
```

Se o PNCP estiver lento para anexos, use `--metadata-only` para salvar detalhe, itens e arquivos sem baixar PDFs.

### Busca tradicional por janela

Use `search_pncp.py` como fallback simples por período quando a busca textual não trouxer resultados suficientes.

```powershell
python .codex\skills\pncp_public_api\scripts\search_pncp.py --query "link MPLS comunicação de dados" --days 730 --top 20 --out PNCP_CACHE\mpls.json
```

Exportação resumida em Markdown:

```powershell
python .codex\skills\pncp_public_api\scripts\search_pncp.py --query "link dedicado 10 Gbps LAN-to-LAN" --days 730 --top 15 --markdown PNCP_CACHE\links_dedicados.md
```

Download/cache incremental de objetos TIC:

```powershell
python .codex\skills\pncp_public_api\scripts\cache_tic_pncp.py --days 730 --out PNCP_CACHE\tic_ultimos_2_anos.jsonl --max-pages 200
```

Varredura ampla por perfis técnicos:

```powershell
python .codex\skills\pncp_public_api\scripts\pesquisa_ampla_rede10.py --single-pass --from-date 2024-06-13 --to-date 2026-06-12 --modalidades 6,8,9 --max-pages 1 --out-dir PNCP_PESQUISA_AMPLA
```

Use a varredura ampla quando o usuário pedir levantamento exploratório, mapeamento de mercado ou quando a busca textual por objeto não capturar itens suficientes.

## Fontes oficiais

- API Swagger: `https://pncp.gov.br/api/consulta/swagger-ui/index.html`
- OpenAPI JSON: `https://pncp.gov.br/pncp-consulta/v3/api-docs`
- Dados abertos PNCP: `https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos`
