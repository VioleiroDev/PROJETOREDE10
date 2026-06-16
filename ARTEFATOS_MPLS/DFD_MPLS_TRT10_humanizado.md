# DOCUMENTO DE FORMALIZAÇÃO DE DEMANDA (DFD)

**Órgão:** Tribunal Regional do Trabalho da 10ª Região - TRT10

**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC

**Objeto:** Contratação de serviços continuados de comunicação de dados por MPLS para interconexão das unidades do TRT10 à Sede, em arquitetura integrada com a SD-WAN vigente; contratação de link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília; e contratação de links dedicados de Internet centralizados na Sede e no Foro, com Anti-DDoS e 32 IPs fixos por link.

**Versão:** Minuta técnica - arquitetura de redundância total MPLS/SD-WAN, link dedicado Sede-Foro e Internet centralizada - versão humanizada

**Data:** 12/06/2026

## 1. Unidade Demandante

### 1.1 Nome da Unidade

Coordenadoria de Infraestrutura de Tecnologia.

### 1.2 Sigla da Unidade

CDTEC.

## 2. Justificativa da Necessidade da Contratação

### 2.1 Justificativa da necessidade

O TRT10 depende de conectividade permanente, segura e resiliente entre suas unidades para sustentar o Processo Judicial Eletrônico, sistemas administrativos, serviços internos de TIC, autenticação, colaboração institucional, acesso a redes externas, contingência, suporte técnico e atividades de atendimento ao público.

A demanda compreende uma arquitetura integrada, composta por três blocos complementares:

- rede MPLS para interconectar as 10 localidades à Sede, com capacidades equivalentes às capacidades dos links SD-WAN vigentes em cada localidade;
- link dedicado ponto-a-ponto de 25 Gbps entre o Edifício Sede e o Foro de Brasília, para replicação, sincronização, backup, continuidade, redundância da Sede e uso do Foro como ponto contingencial de acesso das unidades;
- links dedicados de Internet centralizados, sendo 3 links de 4 Gbps na Sede e 2 links de 2 Gbps no Foro de Brasília, cada link com Anti-DDoS e 32 IPs fixos, em itens separados e com provedores distintos por localidade.

O escopo da contratação contempla os links de Internet dedicada como componente essencial da arquitetura de conectividade do Tribunal. Esses serão os únicos links de Internet do TRT10 no desenho pretendido, estruturando o acesso externo em pontos centrais controlados, monitorados e protegidos. A Sede funcionará como ponto principal de egressão; o Foro de Brasília funcionará como ponto redundante, preparado para assumir tráfego de Internet e acesso das unidades em cenário de indisponibilidade, manutenção ou degradação relevante da Sede.

A exigência de 3 provedores distintos na Sede e 2 provedores distintos no Foro reduz o risco de falha comum, indisponibilidade regional, bloqueio operacional, erro de roteamento, ataque volumétrico, falha de backbone ou incidente comercial afetar simultaneamente todos os acessos de uma mesma localidade. Cada link de Internet será licitado como item próprio. A mesma empresa não poderá vencer mais de um link de Internet na mesma localidade, mas poderá vencer um item da Sede e um item do Foro, pois os domínios de falha e as rotas físicas devem ser analisados por localidade.

A exigência de Anti-DDoS por link é compatível com a função dos enlaces, pois a Internet centralizada concentrará tráfego institucional e se tornará ponto crítico para proteção da disponibilidade dos serviços digitais. O bloco de 32 IPs fixos por link viabiliza publicação controlada de serviços, NAT, segmentação de borda, regras de segurança, balanceamento, contingência, reputação de endereços e segregação de ambientes, devendo ser entregue como bloco IPv4 público fixo /27 ou arranjo equivalente que disponibilize 32 endereços públicos fixos por link, observadas as reservas técnicas usuais quando aplicáveis.

A uso de MPLS com a mesma capacidade nominal dos links SD-WAN reduz o risco de subdimensionamento em cenários de crise, elimina a necessidade de escolher previamente quais sistemas seriam degradados durante falha de uma camada e preserva a experiência operacional das unidades. O link dedicado de 25 Gbps entre Sede e Foro não integra a malha MPLS; ele constitui interligação dedicada de alta capacidade para replicação, backup, continuidade e contingência.

### 2.1.1 Soluções possíveis consideradas

| Alternativa | Síntese | Avaliação |
|---|---|---|
| Solução 1 - MPLS integrado à SD-WAN, link dedicado Sede-Foro e Internet centralizada | Contratar MPLS para tráfego crítico, manter convivência com a SD-WAN vigente, contratar link dedicado de 25 Gbps entre Sede e Foro e centralizar a Internet em 3 links de 4 Gbps na Sede e 2 links de 2 Gbps no Foro, todos com Anti-DDoS e 32 IPs fixos. | Alternativa preferencial. Combina rede privada, redundância total por capacidade, alta capacidade entre pontos centrais, proteção Anti-DDoS, centralização de segurança e provedores distintos nos pontos de Internet. |
| Solução 2 - Internet distribuída em todas as unidades com VPN/SD-WAN | Contratar ou manter saídas de Internet em cada localidade e criar túneis até os pontos centrais. | Aumenta a superfície de ataque, dispersa políticas de segurança, amplia a complexidade de monitoramento e reduz o controle centralizado. Pode ser útil apenas como contingência excepcional. |
| Solução 3 - Somente MPLS/rede privada sem links de Internet centralizados | Contratar apenas a camada privada e depender de saídas de Internet apartadas. | Não atende ao requisito técnico de Internet centralizada em pontos redundantes e protegidos por Anti-DDoS. |
| Solução 4 - Links satelitais como meio principal | Substituir a malha terrestre por enlaces satelitais. | Pode apoiar contingência extrema, mas não é solução principal adequada por latência, variabilidade e custo por Mbps para tráfego crítico. |

A Solução 1 fica indicada como solução preferencial, porque resolve simultaneamente a interconexão privada das unidades, a redundância entre camadas, a replicação Sede-Foro e a centralização segura do acesso à Internet.

### 2.2 A necessidade de contratação decorre de exigência legal?

Não há exigência legal específica para contratar MPLS, link dedicado de 25 Gbps ou Internet dedicada como tecnologias determinadas. A necessidade decorre da obrigação administrativa de assegurar continuidade, disponibilidade, segurança e desempenho dos serviços de TIC que suportam a atividade jurisdicional e administrativa.

A demanda se relaciona com a Lei nº 14.133/2021, especialmente quanto ao planejamento da contratação, ETP e Termo de Referência, e com a ENTIC-JUD 2021-2026, instituída pela Resolução CNJ nº 370/2021, que orienta a governança de TIC do Poder Judiciário e a disponibilidade dos serviços digitais.

### 2.3 Quais unidades serão beneficiadas?

Serão beneficiadas todas as unidades do TRT10 atendidas pela rede institucional:

| Item | Unidade / Localidade | Endereço | Município | UF | CEP |
|---|---|---|---|---|---|
| 1 | Edifício Sede | SAS Quadra 1, Bloco D, Praça dos Tribunais Superiores | Brasília | DF | 70.097-900 |
| 2 | Foro de Brasília | SEPN 513, Bloco B, Lotes 2/3 | Brasília | DF | 70.760-522 |
| 3 | Foro de Taguatinga | Quadra C12, Bloco O, Lotes 1 a 5 e 8 a 12 | Taguatinga | DF | 72.010-120 |
| 4 | Vara do Gama | Área Especial 01, Praça 02, Lote 06 | Gama | DF | 72.405-610 |
| 5 | Foro de Araguaína | Av. Neief Murad, 1131, Jardim Goiás | Araguaína | TO | 77.824-022 |
| 6 | Foro de Palmas | Quadra 302 Norte, Conjunto QI 12, Alameda 2, Lote IA | Palmas | TO | 77.066-338 |
| 7 | Vara de Gurupi | Rua Antônio Lisboa da Cruz, 2031, Centro, Setor Central | Gurupi | TO | 77.405-100 |
| 8 | Vara de Dianópolis | Avenida Wolney Filho, Qd. 69 A, Setor Novo Horizonte | Dianópolis | TO | 77.300-000 |
| 9 | Vara de Guaraí | Avenida Araguaia, esquina com Av. Bernardo Sayão, 1360 | Guaraí | TO | 77.700-000 |
| 10 | Prédio de Apoio | SGAN 916 Norte, Lote AI, Asa Norte | Brasília | DF | 70.790-160 |

A Sede será beneficiada como concentrador principal de rede, segurança, egressão à Internet e integração institucional. O Foro de Brasília será beneficiado como unidade de atendimento, ponto de Internet redundante, ambiente de replicação e concentrador contingencial para acesso das unidades.

### 2.4 Consequências do não atendimento da demanda

- Permanência de maior dependência de uma única camada de conectividade para tráfego crítico.
- Permanência de saídas de Internet dispersas ou insuficientemente padronizadas, com maior superfície de ataque e menor uniformidade de segurança.
- Risco de indisponibilidade relevante da Internet institucional caso a Sede sofra falha sem ponto redundante no Foro.
- Dificuldade de garantir provedores distintos, Anti-DDoS e endereçamento fixo suficiente nos pontos centrais.
- Menor previsibilidade para tráfego crítico, replicação, backup, autenticação, monitoramento e suporte remoto.
- Dificuldade de cumprir diretrizes de continuidade, disponibilidade, segurança e governança de TIC.

## 3. Descrição Sucinta do Objeto

### 3.1 Objeto da contratação

Contratação de serviços continuados de telecomunicações e comunicação de dados, incluindo fornecimento, instalação, configuração, equipamentos necessários, monitoramento, suporte técnico, manutenção e garantia de níveis de serviço, composta pelos seguintes blocos:

- circuitos MPLS para as 10 localidades do TRT10, com capacidades equivalentes às capacidades SD-WAN vigentes por localidade;
- link dedicado ponto-a-ponto de 25 Gbps entre o Edifício Sede e o Foro de Brasília, por fibra óptica, LAN-to-LAN, Metro Ethernet, clear channel, E-Line, E-LAN ou tecnologia equivalente, separado da rede MPLS;
- 3 links dedicados de Internet de 4 Gbps na Sede, cada um com provedor distinto, Anti-DDoS e 32 IPs fixos;
- 2 links dedicados de Internet de 2 Gbps no Foro de Brasília, cada um com provedor distinto, Anti-DDoS e 32 IPs fixos.

A contratação deve permitir centralização do acesso à Internet do TRT10, redundância entre Sede e Foro, contingência cruzada entre MPLS e SD-WAN, QoS, segregação lógica, roteamento controlado, monitoramento 24x7, relatórios mensais e glosas por descumprimento de SLA.

## 4. Quantidade a Ser Contratada

### 4.1 Quantidade estimada por ano

| Item | Localidade | Capacidade SD-WAN vigente | Capacidade MPLS requerida | Quantidade | Unidade |
|---|---:|---:|---:|---:|---|
| 1 | Edifício Sede | 1 Gbps | 1 Gbps | 1 | mês |
| 2 | Foro de Brasília | 1 Gbps | 1 Gbps | 1 | mês |
| 3 | Prédio de Apoio | 500 Mbps | 500 Mbps | 1 | mês |
| 4 | Foro de Taguatinga | 500 Mbps | 500 Mbps | 1 | mês |
| 5 | Foro de Palmas | 500 Mbps | 500 Mbps | 1 | mês |
| 6 | Vara do Gama | 100 Mbps | 100 Mbps | 1 | mês |
| 7 | Foro de Araguaína | 100 Mbps | 100 Mbps | 1 | mês |
| 8 | Vara de Gurupi | 100 Mbps | 100 Mbps | 1 | mês |
| 9 | Vara de Dianópolis | 100 Mbps | 100 Mbps | 1 | mês |
| 10 | Vara de Guaraí | 100 Mbps | 100 Mbps | 1 | mês |

| Item | Enlace dedicado | Tecnologia / função | Capacidade | Quantidade | Unidade |
|---|---|---|---:|---:|---|
| 11 | Sede ↔ Foro de Brasília | Link dedicado ponto-a-ponto; replicação, backup e redundância | 25 Gbps | 1 | mês |

| Item | Localidade | Serviço | Capacidade | Requisitos mínimos | Quantidade | Unidade |
|---|---|---|---:|---|---:|---|
| 12 | Sede | Link dedicado de Internet 1 | 4 Gbps | Provedor distinto dos itens 13 e 14; Anti-DDoS; 32 IPs fixos | 1 | mês |
| 13 | Sede | Link dedicado de Internet 2 | 4 Gbps | Provedor distinto dos itens 12 e 14; Anti-DDoS; 32 IPs fixos | 1 | mês |
| 14 | Sede | Link dedicado de Internet 3 | 4 Gbps | Provedor distinto dos itens 12 e 13; Anti-DDoS; 32 IPs fixos | 1 | mês |
| 15 | Foro de Brasília | Link dedicado de Internet 1 | 2 Gbps | Provedor distinto do item 16; Anti-DDoS; 32 IPs fixos | 1 | mês |
| 16 | Foro de Brasília | Link dedicado de Internet 2 | 2 Gbps | Provedor distinto do item 15; Anti-DDoS; 32 IPs fixos | 1 | mês |

Para os itens de Internet, a adjudicação deverá impedir que uma mesma empresa, CNPJ, grupo econômico ou provedor operacionalmente dependente seja contratado para mais de um link na mesma localidade. A mesma empresa poderá vencer um item da Sede e um item do Foro, desde que respeitados os requisitos de capacidade, Anti-DDoS, 32 IPs fixos e independência física/lógica exigidos para cada item.

### 4.2 A estimativa é baseada no histórico demandado?

Sim. A estimativa considera o histórico de contratações de comunicação de dados e Internet do TRT10, a topologia SD-WAN vigente, registros de redundância e monitoramento, e a centralização dos acessos de Internet do Tribunal na Sede e no Foro.

## 5. Estimativa Preliminar do Valor da Contratação

### 5.1 Valor estimado da contratação

Foram priorizadas referências públicas do PNCP e documentos anexos aos processos consultados. A estimativa de planejamento adota preços públicos diretos quando há aderência suficiente e metodologia paramétrica quando não foram localizados três itens idênticos em capacidade, localidade, Anti-DDoS e bloco de IPs.

| Grupo / item | Referências e fórmula | Quantidade | Valor mensal unitário | Valor mensal | Valor anual |
|---|---|---:|---:|---:|---:|
| MPLS 1 Gbps | Mediana PNCP documentada no ETP: SENAR/MS, Brusque/SC, Chapecó/SC e ANCINE | 2 | R$ 7.122,50 | R$ 14.245,00 | R$ 170.940,00 |
| MPLS 500 Mbps | Mediana PNCP documentada no ETP: Chapecó/SC, ANCINE e Cascavel/PR | 3 | R$ 1.900,00 | R$ 5.700,00 | R$ 68.400,00 |
| MPLS 100 Mbps | Mediana PNCP documentada no ETP: CODEVASF, Cascavel/PR e Chapecó/SC | 5 | R$ 1.900,00 | R$ 9.500,00 | R$ 114.000,00 |
| Link dedicado Sede-Foro 25 Gbps | Faixa paramétrica de alta capacidade: (R$ 30.000,00 + R$ 60.000,00) / 2 | 1 | R$ 45.000,00 | R$ 45.000,00 | R$ 540.000,00 |
| Internet Sede 4 Gbps com Anti-DDoS e 32 IPs fixos | Ipojuca 4 Gbps com Anti-DDoS R$ 15.687,33 + ajuste Chapecó /27 R$ 1.920,00 | 3 | R$ 17.607,33 | R$ 52.821,99 | R$ 633.863,88 |
| Internet Foro 2 Gbps com Anti-DDoS e 32 IPs fixos | Mediana conservadora de referências normalizadas: IPEA R$ 5.520,00; composição Ministério da Defesa + /27 R$ 13.693,78; CLDF R$ 23.520,00 | 2 | R$ 13.693,78 | R$ 27.387,56 | R$ 328.650,72 |
| **Total geral estimado** | MPLS + link dedicado 25 Gbps + Internet centralizada | 16 itens | - | **R$ 154.654,55** | **R$ 1.855.854,60** |

### 5.2 Referências PNCP para MPLS

| Capacidade / uso | Referência | Pregão/licitação, processo e PNCP | Valor documentado | Uso na estimativa |
|---|---|---|---:|---|
| MPLS 1 Gbps | SENAR/MS | Pregão Eletrônico nº 009/2026; Processo nº 018/2026; PNCP nº 04253881000103-1-000025/2026 | R$ 6.950,00/mês | Referência direta de link dedicado MPLS de 1 Gbps. |
| MPLS 1 Gbps | Município de Brusque/SC | Pregão Eletrônico nº 11/2026; Processo nº 33/2026; PNCP nº 83102343000194-1-000064/2026 | R$ 7.295,00/mês | Referência direta de acesso privado por MPLS de ao menos 1 Gbps. |
| MPLS 1 Gbps e 500 Mbps | Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026 | R$ 11.480,00/mês para grupo de 20 pontos de 1 Gbps; R$ 84.050,00/mês para grupo de 205 pontos de 500 Mbps | Referência de rede privada MPLS em escala, usada como apoio de mercado e validação de capacidade. |
| MPLS/SD-WAN | ANCINE | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025 | Itens mensais de R$ 87.562,44, R$ 98.541,28 e R$ 70.505,04, com quantidades distintas | Referência auxiliar de solução híbrida Internet/MPLS/SD-WAN, normalizada no ETP conforme capacidade e escopo. |
| MPLS 100 Mbps e faixas inferiores | Município de Cascavel/PR | Pregão Eletrônico nº 90129/2025; Processo nº 115968; PNCP nº 76208867000107-1-000429/2025 | Itens mensais de R$ 22.800,00; R$ 8.040,00; R$ 6.200,04; R$ 4.407,96; R$ 1.940,04 | Referência por faixas de capacidade para estimativa dos enlaces de 100 Mbps e apoio aos enlaces de 500 Mbps. |
| WAN MPLS nacional | CODEVASF | Pregão Eletrônico nº 90003/2025; Processo nº 59500002693202462; PNCP nº 00399857000126-1-000049/2025 | Valor estimado R$ 1.433.232,00; homologado R$ 670.023,00 | Referência de rede corporativa WAN MPLS nacional, usada como validação técnica e referência auxiliar para 100 Mbps. |

### 5.3 Referências PNCP para o link dedicado Sede-Foro de 25 Gbps

| Referência | Pregão/licitação e PNCP | Objeto / item localizado | Valor documentado | Uso na estimativa |
|---|---|---|---:|---|
| Município de Candeias/BA | Edital nº 023/2026; PNCP nº 13830336000123-1-000051/2026 | Comunicação de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra óptica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos | Referência técnica sem preço unitário isolado usado diretamente | Referência técnica para interligação privativa de alta capacidade por fibra entre pontos centrais. |
| Município de Ubarana/SP | Edital nº 19/2026; PNCP nº 65708786000141-1-000038/2026 | Serviço continuado de interligação de dados entre setores da Administração Pública; rede LAN-to-LAN por fibra óptica dedicada, capacidade agregada de até 10 Gbps, ponto concentrador e link dedicado | R$ 138.000,00 homologado para item de interligação de dados; valor total registrado R$ 184.399,92 | Referência técnica auxiliar de contratação de conectividade privada entre pontos administrativos, sem equivalência direta com 25 Gbps. |
| Município de Água Clara/MS | Pregão Eletrônico; PNCP nº 03184066000177-1-000029/2025 | Serviços LAN-to-LAN de 1 Gbps para múltiplas unidades | Itens homologados em torno de R$ 765,43/mês por ponto de 1 Gbps | Referência técnica de contratação por pontos LAN-to-LAN, sem equivalência direta com 25 Gbps. |
| Município de Jaguariúna/SP | Edital PL-674/2024; PE nº 90081/2024; PNCP nº 46410866000171-1-000610/2024 | Link dedicado simétrico de 10 Gbps e link compartilhado de Internet | Referência auxiliar sem uso direto como preço unitário do enlace de 25 Gbps | Referência técnica para enlace dedicado de alta capacidade, simétrico e com requisitos de desempenho. |
| Justiça Federal do Rio Grande do Sul / TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços nº 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Serviços de comunicação de dados dedicados e exclusivos para acesso à Internet e comunicação ponto-a-ponto entre sites via Metro Ethernet/LAN-to-LAN, camada 2 | Referência técnica sem valor unitário usado diretamente | Referência para modelagem do enlace Sede-Foro como link dedicado ponto-a-ponto, e não como MPLS. |

Não foi localizada referência pública plenamente equivalente a enlace dedicado ponto-a-ponto de 25 Gbps entre dois prédios com a mesma finalidade de replicação e contingência. Por isso, a estimativa do item 11 usa faixa paramétrica de alta capacidade, com ponto médio de R$ 45.000,00/mês, calculado por `(R$ 30.000,00 + R$ 60.000,00) / 2`. As referências acima demonstram aderência técnica de mercado para LAN-to-LAN, Metro Ethernet, fibra dedicada e interligação privada de pontos centrais, mas não foram tratadas como equivalentes perfeitas de preço.

### 5.4 Referências PNCP para links dedicados de Internet

| Referência | Pregão/licitação e PNCP | Valor usado | Uso na estimativa |
|---|---|---:|---|
| Município de Ipojuca/PE | Pregão Eletrônico nº 035/PMI-SMAD/2024; Processo nº 188/PMI-SMAD/2024; PNCP nº 11294386000108-1-000244/2024; https://pncp.gov.br/app/editais/11294386000108/2024/244 | R$ 15.687,33/mês por link | Base direta para Internet dedicada 4 Gbps com Anti-DDoS. |
| Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026; https://pncp.gov.br/app/editais/83021808000182/2026/200 | R$ 1.920,00/mês para IP /27; R$ 8.500,00 e R$ 7.500,00/mês para links de 5 Gbps | Ajuste para bloco de 32 IPs e referência de alta capacidade. |
| Câmara Legislativa do Distrito Federal | Aviso de Contratação Direta nº 90021/2025; PNCP nº 26963645000113-1-000038/2025; https://pncp.gov.br/app/compras/26963645000113/2025/38 | R$ 21.600,00 homologado para link de dados de 2 Gbps com Anti-DDoS; R$ 23.520,00 com ajuste /27 | Referência direta homologada para 2 Gbps com Anti-DDoS. |
| Instituto de Pesquisa Econômica Aplicada - IPEA | Pregão Eletrônico nº 90047/2026; PNCP nº 33892175000100-1-000033/2026; https://pncp.gov.br/app/compras/33892175000100/2026/33 | R$ 3.600,00/mês estimado por link de 2 Gbps com Anti-DDoS; R$ 5.520,00 com ajuste /27 | Referência direta estimada para 2 Gbps com Anti-DDoS. |
| Ministério da Defesa | Dispensa com Disputa nº 292/2025; Processo nº 60591.000013/2025-64; PNCP nº 03277610000125-1-000586/2025; https://pncp.gov.br/app/editais/03277610000125/2025/586 | R$ 5.161,89/mês para link 1 Gbps; R$ 1.450,00/mês para Anti-DDoS | Composição paramétrica dos links de 2 Gbps do Foro. |
| Município de Itaipulândia/PR | Pregão Eletrônico nº 52/2025; Processo nº 98/2025; PNCP nº 95725057000164-1-000097/2025; https://pncp.gov.br/app/editais/95725057000164/2025/97 | Valor global estimado R$ 450.000,00 | Referência técnica para links dedicados simétricos de 2 Gbps. |
| CAU/BA | Dispensa nº 5/2025; Processo nº 00152.000202/2025-84; PNCP nº 15158665000103-1-000011/2025; https://pncp.gov.br/app/editais/15158665000103/2025/11 | Relatório de cotação com referência de 2 Gbps Anti-DDoS | Referência auxiliar, sem uso direto na fórmula. |
| ANCINE | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025; https://pncp.gov.br/app/editais/04884574000120/2025/56 | R$ 7.296,87/mês por link de Internet 1 Gbps com DDoS | Validação de prática de Anti-DDoS e SLA. |

### 5.5 Como se chegou ao valor preliminar?

Para MPLS 1 Gbps, foi adotada mediana das referências PNCP normalizadas de SENAR/MS, Brusque/SC, Chapecó/SC e ANCINE, resultando em R$ 7.122,50 por circuito/mês. Como há 2 localidades com essa capacidade, o valor mensal do grupo é `2 x R$ 7.122,50 = R$ 14.245,00`.

Para MPLS 500 Mbps, foi adotada mediana das referências PNCP de Chapecó/SC, ANCINE e Cascavel/PR, resultando em R$ 1.900,00 por circuito/mês. Como há 3 localidades com essa capacidade, o valor mensal do grupo é `3 x R$ 1.900,00 = R$ 5.700,00`.

Para MPLS 100 Mbps, foi adotada mediana das referências PNCP de CODEVASF, Cascavel/PR e Chapecó/SC, resultando em R$ 1.900,00 por circuito/mês. Como há 5 localidades com essa capacidade, o valor mensal do grupo é `5 x R$ 1.900,00 = R$ 9.500,00`.

Para o link dedicado Sede-Foro de 25 Gbps, a estimativa utiliza faixa paramétrica de alta capacidade, pois as referências PNCP localizadas confirmam a viabilidade técnica de LAN-to-LAN, Metro Ethernet e fibra dedicada, mas não apresentam três itens idênticos de 25 Gbps com a mesma finalidade. O valor unitário adotado é o ponto médio da faixa: `(R$ 30.000,00 + R$ 60.000,00) / 2 = R$ 45.000,00 por mês`.

Para os links de Internet da Sede, a referência de Ipojuca/PE foi utilizada por possuir aderência direta a Internet dedicada de 4 Gbps com Anti-DDoS e regra de links por empresas diferentes. Como o requisito do TRT10 exige 32 IPs fixos por link, acrescentou-se o valor de IP /27 identificado na memória de cálculo de Chapecó/SC: `R$ 15.687,33 + R$ 1.920,00 = R$ 17.607,33 por link/mês`. Como são 3 links, o valor mensal do grupo é `3 x R$ 17.607,33 = R$ 52.821,99`.

Para os links de Internet do Foro, a estimativa adotou mediana conservadora entre referência direta estimada do IPEA, referência direta homologada da Câmara Legislativa do Distrito Federal e composição paramétrica do Ministério da Defesa, acrescidas ou comparadas ao ajuste /27 de Chapecó/SC quando o item de origem não trazia bloco de 32 IPs fixos. O valor unitário adotado é R$ 13.693,78 por link/mês. Como são 2 links, o valor mensal do grupo é `2 x R$ 13.693,78 = R$ 27.387,56`.

### 5.6 Contratações similares a manter nos autos

Devem compor a instrução de preços as referências MPLS, LAN-to-LAN/link dedicado e Internet descritas neste item, juntamente com os artefatos baixados em `PNCP_REFERENCIAS_MPLS`, `PNCP_REFERENCIAS_INTERNET`, `PNCP_PESQUISA_AMPLA_REDE10` e `PNCP_CACHE`. Devem ser preservados detalhes da contratação, itens, resultados, arquivos anexos, editais, termos de referência, propostas, relatórios de cotação e memórias de cálculo.

## 6. Data Pretendida para Conclusão da Contratação

### 6.1 Data de início de vigência

A contratação deve estar vigente em tempo hábil para implantação, testes, operação assistida e entrada em produção controlada, preservando a continuidade da conectividade das unidades e dos acessos de Internet.

### 6.2 É serviço continuado?

Sim. É serviço continuado de telecomunicações e comunicação de dados, essencial para o funcionamento permanente das unidades do TRT10.

## 7. Grau de Prioridade da Contratação

| Critério | Marcação sugerida | Justificativa |
|---|---|---|
| Impacto se não atendida | Grave | Pode afetar disponibilidade, desempenho, segurança, acesso à Internet, contingência e comunicação institucional. |
| Urgência | Alta para planejamento | Há necessidade de pesquisa de preços, implantação, testes e entrada em produção dos acessos de Internet centralizados. |
| Tendência do problema | Irá piorar | A demanda por tráfego, segurança centralizada, Anti-DDoS, replicação e continuidade tende a crescer. |

## 8. Vinculação ou Dependência com Outra Demanda

A demanda possui vinculação técnica com o contrato SD-WAN vigente, redes JT, Infovia, firewalls, segurança perimetral, monitoramento, datacenter, DNS, autenticação, roteamento e políticas de continuidade. Os links de Internet centralizados fazem parte do objeto e deverão operar como os pontos oficiais de egressão à Internet do Tribunal.

## 9. Objetivo Estratégico

A contratação se alinha ao objetivo estratégico de aprimorar a governança de TIC e a proteção de dados, contribuindo para disponibilidade, continuidade, segurança, monitoramento e desempenho dos serviços digitais do TRT10.

## 10. Informações SIGEO

### 10.1 Processo administrativo da contratação em vigor

**Processos de referência histórica:** SEI 0000030-87.2023.5.10.8000, SEI 0007608-72.2021.5.10.8000 e SEI 0002027-76.2021.5.10.8000.

### 10.2 Contrato ou ARP em vigor

Contrato 131/2023 relacionado a link IP dedicado com SD-WAN. A área de contratos deverá conferir instrumentos vigentes que interajam com a conectividade institucional para preservar continuidade operacional durante a implantação.

### 10.3 Item SIGEO

Serviços continuados de telecomunicações, comunicação de dados, Internet dedicada, Anti-DDoS e interconexão de unidades.

### 10.4 Estimativa para 12 meses no SIGEO

Estimativa de planejamento: **R$ 1.855.854,60** para 12 meses.

## 11. Servidor Responsável pela Demanda

Nome: Edson Mateus de Sousa - Coordenador da CDTEC

E-mail funcional: cdtec@trt10.jus.br

Telefone: (61) 3348-1249 / 1288 / 1280 / 1188

## 12. Figura 1 - Arquitetura Proposta

![Figura 1 - Arquitetura proposta MPLS, SD-WAN, link dedicado Sede-Foro e Internet centralizada](../diagrama_topologia_revisada.png)
