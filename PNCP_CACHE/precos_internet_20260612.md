# Memória de cálculo - links de Internet centralizados

Data da atualização: 12/06/2026.

## Referências PNCP utilizadas

| Uso | Órgão | Pregão/licitação, processo e PNCP | Objeto e valor extraído | Observação |
|---|---|---|---|---|
| Referência direta para 4 Gbps com Anti-DDoS | Município de Ipojuca/PE | Pregão Eletrônico nº 035/PMI-SMAD/2024; Processo nº 188/PMI-SMAD/2024; PNCP nº 11294386000108-1-000244/2024; https://pncp.gov.br/app/editais/11294386000108/2024/244 | Internet dedicada 4 Gbps, circuito de dados, Anti-DDoS e faixa de IP fixo CIDR/29. Valor mensal unitário: R$ 15.687,33. | Referência mais aderente para os links de 4 Gbps. O PNCP também registra exigência de links principal e redundante por empresas diferentes. |
| Ajuste para bloco de 32 IPs | Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026; https://pncp.gov.br/app/editais/83021808000182/2026/200 | Memória de cálculo com item de IP /27 cotado a R$ 1.920,00/mês e links dedicados de Internet de 5 Gbps com valores de R$ 8.500,00 e R$ 7.500,00/mês. | Utilizado para ajustar a referência de Ipojuca, que contém CIDR/29, ao requisito do TRT10 de 32 IPs fixos por link. |
| Referência de Anti-DDoS e composição 1 Gbps | Ministério da Defesa | Dispensa com Disputa nº 292/2025; Processo nº 60591.000013/2025-64; PNCP nº 03277610000125-1-000586/2025; https://pncp.gov.br/app/editais/03277610000125/2025/586 | Proposta comercial com link dedicado 1 Gbps a R$ 5.161,89/mês e Anti-DDoS a R$ 1.450,00/mês. | Utilizada para composição paramétrica conservadora dos links de 2 Gbps do Foro. |
| Referência técnica para 2 Gbps | Município de Itaipulândia/PR | Pregão Eletrônico nº 52/2025; Processo nº 98/2025; PNCP nº 95725057000164-1-000097/2025; https://pncp.gov.br/app/editais/95725057000164/2025/97 | Contratação de links dedicados simétricos de 2 Gbps por fibra óptica. Valor global estimado: R$ 450.000,00. | Usada como evidência de disponibilidade de serviço 2 Gbps; não usada diretamente como preço unitário por não isolar mensalidade por link com Anti-DDoS e /27. |
| Referência auxiliar de 2 Gbps com Anti-DDoS | CAU/BA | Dispensa nº 5/2025; Processo nº 00152.000202/2025-84; PNCP nº 15158665000103-1-000011/2025; https://pncp.gov.br/app/editais/15158665000103/2025/11 | Relatório de cotação anexo contém referência de serviço de acesso dedicado à Internet com Anti-DDoS em 2 Gbps. | Tratada como referência auxiliar de mercado, sem uso direto na média por divergência de unidade de medida e por não ser o item principal da contratação do CAU/BA. |
| Referência de arquitetura híbrida com DDoS | ANCINE | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025; https://pncp.gov.br/app/editais/04884574000120/2025/56 | Link de Internet com proteção contra DDoS, 2 links de 1 Gbps, valor mensal unitário de R$ 7.296,87. | Usada como validação técnica de exigência de Anti-DDoS, suporte 24x7 e prazos de mitigação. |

## Fórmulas adotadas

- Link de Internet Sede 4 Gbps com Anti-DDoS e 32 IPs fixos = referência Ipojuca 4 Gbps com Anti-DDoS e CIDR/29 + ajuste Chapecó para bloco /27 = R$ 15.687,33 + R$ 1.920,00 = R$ 17.607,33 por link/mês.
- Total Sede = 3 links x R$ 17.607,33 = R$ 52.821,99 por mês = R$ 633.863,88 por ano.
- Link de Internet Foro 2 Gbps com Anti-DDoS e 32 IPs fixos = (componente de acesso 1 Gbps Ministério da Defesa x 2) + Anti-DDoS Ministério da Defesa + ajuste /27 Chapecó = (R$ 5.161,89 x 2) + R$ 1.450,00 + R$ 1.920,00 = R$ 13.693,78 por link/mês.
- Total Foro = 2 links x R$ 13.693,78 = R$ 27.387,56 por mês = R$ 328.650,72 por ano.
- Subtotal Internet centralizada = R$ 52.821,99 + R$ 27.387,56 = R$ 80.209,55 por mês = R$ 962.514,60 por ano.
- Subtotal MPLS = R$ 29.445,00 por mês = R$ 353.340,00 por ano.
- Link dedicado Sede-Foro 25 Gbps = R$ 45.000,00 por mês = R$ 540.000,00 por ano.
- Total geral = R$ 29.445,00 + R$ 45.000,00 + R$ 80.209,55 = R$ 154.654,55 por mês = R$ 1.855.854,60 por ano.
