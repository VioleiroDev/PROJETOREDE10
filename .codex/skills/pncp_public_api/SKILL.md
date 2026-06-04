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

## Fontes oficiais

- API Swagger: `https://pncp.gov.br/api/consulta/swagger-ui/index.html`
- OpenAPI JSON: `https://pncp.gov.br/pncp-consulta/v3/api-docs`
- Dados abertos PNCP: `https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos`
