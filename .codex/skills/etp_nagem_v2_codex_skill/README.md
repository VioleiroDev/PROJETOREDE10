# ETP NAGEM V2 — Codex Skill

Skill para uso no OpenAI Codex em tarefas de contratações públicas brasileiras de TIC: DFD, ETP, Termo de Referência, matriz de riscos, requisitos, precedentes PNCP e planejamento da contratação.

## Instalação

Copie a pasta `etp_nagem_v2_codex_skill` para o diretório de skills usado pelo seu Codex ou pelo ambiente compatível com Agent Skills.

Estrutura principal:

```text
etp_nagem_v2_codex_skill/
  SKILL.md
  scripts/search_knowledge.py
  references/knowledge/
```

## Uso

No Codex, invoque a skill pelo nome `etp-nagem-v2` ou solicite uma tarefa compatível com sua descrição.

Exemplo:

```text
Use a skill etp-nagem-v2 para elaborar um ETP de contratação de solução de service desk.
```

Para busca manual de precedentes:

```bash
python scripts/search_knowledge.py "service desk" --top 8
```

## Observação

A base original foi preservada em `references/knowledge/`. O próprio pacote informa status "APTO COM RESSALVAS"; portanto, resultados incompletos devem ser tratados como precedentes fracos ou lacunas, não como fundamento conclusivo.
