# Relatório curado da pesquisa PNCP - Projeto Rede10

Data da consolidação: 12/06/2026.

## 1. Escopo pesquisado

A pesquisa buscou contratações públicas compatíveis com os itens do projeto: links MPLS de 100 Mbps, 500 Mbps e 1 Gbps para unidades; links dedicados de Internet centralizados de 4 Gbps para a Sede e 2 Gbps para o Foro, com 32 IPs fixos por link e proteção Anti-DDoS; e link dedicado ponto a ponto de alta capacidade para interligação entre Sede e Foro.

Foram usadas a API pública de consulta do PNCP e os endpoints públicos de itens e arquivos. Como o PNCP não oferece endpoint público de busca textual ampla por palavra-chave em contratações, a estratégia adotada foi enumerar janelas de publicação/atualização, filtrar localmente por termos técnicos e detalhar itens dos candidatos mais aderentes.

## 2. Fontes e artefatos gerados

| Artefato local | Conteúdo |
| --- | --- |
| `PNCP_PESQUISA_AMPLA_REDE10/candidatos_2024_2.json` | Candidatos TIC/telecom de 13/06/2024 a 31/12/2024. |
| `PNCP_PESQUISA_AMPLA_REDE10/candidatos_2025_1.json` | Candidatos TIC/telecom de 01/01/2025 a 30/06/2025. |
| `PNCP_PESQUISA_AMPLA_REDE10/candidatos_2025_2.json` | Candidatos TIC/telecom de 01/07/2025 a 31/12/2025. |
| `PNCP_PESQUISA_AMPLA_REDE10/candidatos_2026_1.json` | Candidatos TIC/telecom de 01/01/2026 a 12/06/2026. |
| `PNCP_PESQUISA_AMPLA_REDE10/classificacao_itens/RELATORIO_PESQUISA_AMPLA_PNCP.md` | Classificação automática por perfil técnico, com itens aderentes. |
| `PNCP_REFERENCIAS_MPLS/INDICE_REFERENCIAS_MPLS.md` | Índice de referências MPLS com valores de itens e arquivos baixados. |
| `PNCP_CACHE/precos_internet_20260612.md` | Memória de cálculo anterior dos links de Internet com referências diretas e auxiliares. |
| `PNCP_PESQUISA_AMPLA_REDE10/metadados_selecionados` | Metadados adicionais baixados por controle PNCP para IPEA e Acre. |

Foram coletados 1.345 candidatos TIC/telecom por varredura ampla. Houve instabilidade recorrente no endpoint de detalhe da API oficial em 12/06/2026, com timeouts em consultas pontuais. Para mitigar, foram usados os endpoints públicos de itens/arquivos e os caches locais produzidos em consultas anteriores ao PNCP, sem converter valor global em preço unitário quando a unidade não estava suficientemente clara.

## 3. Referências de maior aderência

| Item do projeto | Referência PNCP | Órgão e certame | Aderência | Valor documentado |
| --- | --- | --- | --- | --- |
| Internet 4 Gbps com Anti-DDoS e IP fixo | 11294386000108-1-000244/2024 | Município de Ipojuca/PE, Pregão Eletrônico nº 035/PMI-SMAD/2024, Processo nº 188/PMI-SMAD/2024 | Referência direta para Internet dedicada 4 Gbps com Anti-DDoS e faixa CIDR. | R$ 15.687,33 por link/mês. |
| Complemento para 32 IPs fixos | 83021808000182-1-000200/2026 | Município de Chapecó/SC, Pregão Eletrônico nº 153/2026, Processo nº 153/2026 | Memória de cálculo com bloco /27 de IP público. | R$ 1.920,00 por mês para bloco /27. |
| Internet 5 Gbps e rede MPLS | 83021808000182-1-000200/2026 | Município de Chapecó/SC, Pregão Eletrônico nº 153/2026 | Referência direta de serviço de Internet dedicada de alta capacidade e rede privada MPLS. | Internet 5 Gbps: R$ 8.500,00/mês; Internet backup 5 Gbps: R$ 7.500,00/mês; MPLS 500 Mbps para 205 pontos: R$ 84.050,00/mês; MPLS 1 Gbps para 20 pontos: R$ 11.480,00/mês. |
| Internet 2 Gbps com Anti-DDoS | 33892175000100-1-000033/2026 | Instituto de Pesquisa Econômica Aplicada - IPEA, Pregão Eletrônico, PNCP 2026/33 | Referência direta para 2 links dedicados de Internet, cada um com 2 Gbps simétricos e proteção contra ataques distribuídos, conforme objeto capturado no cache PNCP; itens disponíveis no endpoint público. | Dois itens de R$ 3.600,00 por mês, quantidade 12, total R$ 43.200,00 por item. |
| Internet 2 Gbps com Anti-DDoS e eBGP | 63606479000124-1-000357/2024 | Estado do Acre, Pregão Eletrônico, PNCP 2024/357 | Referência técnica de 2 Gbps simétrico com eBGP e proteção DDoS em backbone, conforme objeto capturado no cache PNCP; itens disponíveis no endpoint público. | Itens anuais de R$ 368.728,20, R$ 66.780,00, R$ 215.091,96 e R$ 10.000,00, todos com quantidade 2. |
| Internet 1 Gbps com Anti-DDoS | 03277610000125-1-000586/2025 | Ministério da Defesa, Dispensa com Disputa nº 292/2025, Processo nº 60591.000013/2025-64 | Referência auxiliar de composição paramétrica para acesso dedicado e Anti-DDoS. | Link 1 Gbps: R$ 5.161,89/mês; Anti-DDoS: R$ 1.450,00/mês. |
| Internet/MPLS/SD-WAN | 04884574000120-1-000056/2025 | Agência Nacional do Cinema - ANCINE, Pregão Eletrônico nº 90007/2025, Processo nº 01416.005548/2024-11 | Referência auxiliar para arquitetura híbrida com Internet dedicada, Anti-DDoS, MPLS e SD-WAN. | Link de Internet 1 Gbps com proteção DDoS: R$ 7.296,87/mês, conforme memória local; itens PNCP globais vinculados ao certame. |
| MPLS 1 Gbps | 04253881000103-1-000025/2026 | SENAR/MS, Pregão Eletrônico nº 009/2026, Processo nº 018/2026 | Referência direta de link dedicado MPLS 1 Gbps. | R$ 6.950,00 por mês, quantidade 12, total R$ 83.400,00. |
| MPLS 1 Gbps | 83102343000194-1-000064/2026 | Município de Brusque/SC, Pregão Eletrônico nº 011/2026, Processo nº 33/2026 | Referência direta de acesso privado entre prefeitura e datacenter por MPLS de ao menos 1 Gbps. | R$ 7.295,00 por mês, quantidade 72, total R$ 525.240,00. |
| MPLS 500 Mbps e 1 Gbps | 83021808000182-1-000200/2026 | Município de Chapecó/SC, Pregão Eletrônico nº 153/2026 | Referência direta para MPLS em massa, com itens separados para 500 Mbps e 1 Gbps. | 500 Mbps: R$ 84.050,00/mês para 205 pontos; 1 Gbps: R$ 11.480,00/mês para 20 pontos. |
| MPLS 100 Mbps e faixas inferiores | 76208867000107-1-000429/2025 | Município de Cascavel/PR, Pregão Eletrônico nº 90129/2025, Processo nº 115968 | Referência de rede IP/MPLS com múltiplas faixas de enlaces. | Itens mensais: R$ 22.800,00; R$ 8.040,00; R$ 6.200,04; R$ 4.407,96; R$ 1.940,04, com quantidades por grupo. |
| MPLS WAN nacional | 00399857000126-1-000049/2025 | CODEVASF, Pregão Eletrônico nº 90003/2025, Processo nº 59500002693202462 | Referência de rede corporativa WAN MPLS nacional. | Valor estimado: R$ 1.433.232,00; homologado: R$ 670.023,00. |

## 4. Referências descartadas ou apenas auxiliares

Foram descartados como base de preço os achados que continham termos coincidentes, mas objeto não aderente, como aquisição de fibra óptica para uso médico, equipamentos de vídeo com fibra, link compartilhado residencial ou banda larga sem dedicação, telefonia móvel com franquia de dados e serviços gerais de TI sem item isolado de telecomunicações.

Também foram tratados como auxiliares, e não como referência unitária principal, os registros em que o PNCP apresentava apenas valor global sem memória de quantidade compatível, ou em que a descrição pública do item vinha genérica como "Serviço de Link Via Cabo", sem o anexo disponível no momento da consulta para confirmar banda, SLA, Anti-DDoS, quantidade de IPs ou prazo.

## 5. Fórmula de cálculo recomendada para o ETP

### 5.1 Links de Internet da Sede - 4 Gbps

Preço unitário estimado por link:

`R$ 15.687,33 + R$ 1.920,00 = R$ 17.607,33 por mês`

Memória:

- R$ 15.687,33/mês: referência Ipojuca para Internet dedicada 4 Gbps com Anti-DDoS e CIDR.
- R$ 1.920,00/mês: referência Chapecó para bloco /27, compatível com 32 IPs fixos.

Quantidade:

`3 links x R$ 17.607,33 = R$ 52.821,99 por mês`

Valor anual:

`R$ 52.821,99 x 12 = R$ 633.863,88`

### 5.2 Links de Internet do Foro - 2 Gbps

Preço unitário estimado por link, usando referência direta mais recente do IPEA:

`R$ 3.600,00 + R$ 1.920,00 = R$ 5.520,00 por mês`

Memória:

- R$ 3.600,00/mês: item PNCP do IPEA para link dedicado de 2 Gbps com proteção Anti-DDoS, conforme objeto da contratação e item público.
- R$ 1.920,00/mês: referência Chapecó para bloco /27, compatível com 32 IPs fixos.

Quantidade:

`2 links x R$ 5.520,00 = R$ 11.040,00 por mês`

Valor anual:

`R$ 11.040,00 x 12 = R$ 132.480,00`

Como análise crítica, a referência do IPEA é muito aderente, porém significativamente menor que referências auxiliares de 1 Gbps/Anti-DDoS e 2 Gbps/eBGP. Para estimativa conservadora, pode-se manter a fórmula anteriormente adotada com Ministério da Defesa:

`(R$ 5.161,89 x 2) + R$ 1.450,00 + R$ 1.920,00 = R$ 13.693,78 por link/mês`

Nesse cenário conservador:

`2 links x R$ 13.693,78 = R$ 27.387,56 por mês = R$ 328.650,72 por ano`

### 5.3 MPLS

Para MPLS, recomenda-se manter cálculo por capacidade e quantidade de localidades do projeto, usando referências diretas de Chapecó, SENAR/MS, Brusque, Cascavel e CODEVASF. Sempre que houver divergência entre preço por ponto e preço por grupo de pontos, a memória deve explicitar a normalização adotada e preservar a fonte original sem converter valor global quando o PNCP não trouxer quantidade unitária confiável.

### 5.4 Link dedicado Sede-Foro 25 Gbps

Não foi encontrada, nesta rodada, referência PNCP pública diretamente equivalente a link dedicado ponto a ponto de 25 Gbps entre dois prédios com o mesmo nível de aderência das referências de Internet e MPLS. A pesquisa localizou referências de alta capacidade, Metro Ethernet, LAN-to-LAN e ponto a ponto, mas sem preço unitário isolado para 25 Gbps.

Para o ETP, o valor de referência deve ser tratado como estimativa técnica paramétrica e justificado pela criticidade da interligação Sede-Foro, capacidade superior à soma dos links de Internet centralizados, baixa latência, isolamento lógico/físico e suporte à replicação e contingência. A referência deve permanecer marcada como paramétrica até que se obtenham cotações diretas ou contratação pública com item equivalente.

## 6. Conclusão operacional

A pesquisa PNCP confirma a existência de contratações públicas recentes para Internet dedicada com Anti-DDoS, IP fixo, links de 2 Gbps, links de 4/5 Gbps, redes MPLS de 100 Mbps a 1 Gbps e arquiteturas híbridas MPLS/Internet/SD-WAN. A base mais sólida para preços unitários é formada por Ipojuca, Chapecó, IPEA, Ministério da Defesa, ANCINE, SENAR/MS e Brusque.

Para atualização do ETP, as tabelas de estimativa devem citar expressamente o número PNCP, órgão, modalidade, número do pregão/processo quando disponível, objeto, valor extraído, unidade de medida, fórmula de cálculo e justificativa de uso direto ou auxiliar.
