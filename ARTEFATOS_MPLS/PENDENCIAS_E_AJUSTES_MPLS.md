# PENDENCIAS E AJUSTES REMANESCENTES

## Artefatos revisados

- DFD_MPLS_TRT10.md
- ETP_MPLS_TRT10.md
- TR_MPLS_TRT10.md

## Ajustes realizados

1. Incluida a logica arquitetural de MPLS integrado a SD-WAN.
2. Registrado que o MPLS sera preferencial para trafego critico e institucional.
3. Registrado que a SD-WAN permanecera preferencial para trafego de Internet.
4. Incluida a contingencia cruzada: MPLS e SD-WAN poderao transportar todos os tipos de trafego em caso de indisponibilidade ou degradacao.
5. Incluida no ETP a analise comparativa das tres solucoes possiveis:
   - MPLS integrado a SD-WAN;
   - links satelitais;
   - links comuns de Internet com VPN ponto a ponto.
6. Defendida a Solucao 1 como alternativa preferencial, com base em disponibilidade, seguranca, QoS, governanca, aproveitamento da SD-WAN existente e centralizacao na Sede.
7. Reforcados os requisitos de roteamento, QoS, failover, projeto executivo, relatorios mensais e testes de aceite.
8. Incluida clausula de subcontratacao no TR.
9. Ampliada a matriz resumida de riscos do TR.

## Pendencias para fechamento formal

| Pendencia | Impacto | Responsavel sugerido |
|---|---|---|
| Pesquisa de precos atual para MPLS, links satelitais e VPN sobre Internet | Necessaria para estimativa oficial, escolha da solucao e vantajosidade | Area de planejamento/contratacoes com apoio da CDTEC |
| Validacao de capacidade por localidade | Evita superdimensionamento ou subdimensionamento dos circuitos | CDTEC |
| Definicao final de metas de latencia, perda de pacotes e jitter | Necessaria para SLA mensuravel | CDTEC |
| Confirmacao de item PCA/SIGPLAC/SIGEO e dotacao | Necessaria para instrucao administrativa | Area administrativa/orcamentaria |
| Confirmacao das vigencias dos contratos correlatos | Evita conflito com SD-WAN, Internet, Anti-DDoS e Infovia | Gestao contratual |
| Projeto executivo de enderecamento, roteamento, VRF, QoS e failover | Necessario para implantacao e aceite | CDTEC e futura contratada |
| Mapa de riscos completo em artefato proprio | Reforca planejamento, gestao e controles | Equipe de planejamento |
| Definicao de criterios quantitativos de qualificacao tecnica | Reduz risco de restricao indevida ou exigencia insuficiente | Equipe de planejamento/juridico |
| Validacao juridica da vigencia pretendida de 5 anos | Necessaria para fundamentacao da contratacao continuada | Area juridica/administrativa |
| Confirmacao de exigencia regulatoria aplicavel junto a Anatel | Necessaria para habilitacao e execucao do servico | Equipe de planejamento |

## Observacao

A base local da skill etp-nagem-v2 nao retornou precedentes PNCP uteis para MPLS, SD-WAN, links satelitais ou VPN ponto a ponto. Assim, as melhorias inseridas nos artefatos foram tratadas como inferencias tecnicas e hipoteses de trabalho, dependentes de validacao por pesquisa de mercado e pela equipe de planejamento.
