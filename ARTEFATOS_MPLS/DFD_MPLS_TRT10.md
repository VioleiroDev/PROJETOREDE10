# DOCUMENTO DE FORMALIZAÇÃO DE DEMANDA (DFD)

**Órgão:** Tribunal Regional do Trabalho da 10ª Região - TRT10

**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC

**Objeto:** Contratação de serviços continuados de comunicação de dados por MPLS para interconexão das unidades do TRT10 à Sede, em arquitetura integrada com a SD-WAN vigente, com capacidades MPLS equivalentes às capacidades dos links SD-WAN por localidade, e contratação de grupo específico de link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, para replicação, redundância da Sede e continuidade de acesso das unidades.

**Versão:** Minuta técnica - arquitetura de redundância total MPLS/SD-WAN

**Data:** 02/06/2026

## 1. Unidade Demandante

### 1.1 Nome da Unidade

Coordenadoria de Infraestrutura de Tecnologia.

### 1.2 Sigla da Unidade

CDTEC.

## 2. Justificativa da Necessidade da Contratação

### 2.1 Justificativa da necessidade

O TRT10 depende de conectividade permanente, segura e resiliente entre suas unidades para sustentar o Processo Judicial Eletrônico, sistemas administrativos, serviços internos de TIC, autenticação, colaboração institucional, acesso a redes externas, contingência, suporte técnico e atividades de atendimento ao público.

Os documentos de contratações anteriores demonstram histórico recorrente de contratação de links de comunicação de dados, links de Internet, redundância de acesso e serviços de suporte associados. Em especial:

- o processo SEI 0000030-87.2023.5.10.8000 registra a contratação de link IP dedicado com SD-WAN para 10 localidades, com bandas de 1 Gbps na Sede e no Foro de Brasília, 500 Mbps no Foro de Taguatinga, Foro de Palmas e Prédio de Apoio, e 100 Mbps nas demais unidades;

- o mesmo processo registra disponibilidade mínima de 99,90% para a Sede e 99,70% para as demais localidades;

- os processos anteriores de Internet e links das unidades indicam a necessidade de redundância, monitoramento, disponibilidade, abertura de chamados, glosas por indisponibilidade e manutenção da continuidade dos serviços;

- documentos de 2021/2022 já registravam que Foro de Brasília e Prédio de Apoio se conectavam à Sede por MPLS e Infovia, demonstrando que a concentração de tráfego na Sede e a interconexão privada das unidades fazem parte do histórico arquitetural do Tribunal.

A demanda consiste em contratar serviços MPLS para interconectar todas as localidades à Sede, em convivência operacional com a SD-WAN vigente, estabelecendo uma camada corporativa privada, previsível e controlada para tráfego institucional crítico. A Sede deverá operar como concentrador preferencial de saída de Internet e das redes institucionais, considerando a existência de 3 saídas de Internet redundantes na Sede.

A contratação define, desde sua concepção, duas camadas de conectividade com capacidades nominais equivalentes por localidade: a camada MPLS, voltada à rede privada corporativa, e a camada SD-WAN vigente, voltada ao transporte por Internet dedicada e a políticas dinâmicas de tráfego. A equivalência de capacidades decorre da necessidade de redundância total: em caso de indisponibilidade, manutenção, degradação severa ou falha operacional de uma das camadas, a outra deverá ter capacidade nominal suficiente para absorver integralmente o perfil de tráfego esperado da unidade, sem redução planejada da banda contratada. Na operação normal, o MPLS poderá ser priorizado para sistemas críticos, serviços corporativos internos, autenticação, integrações institucionais, administração de rede e demais fluxos definidos pela CDTEC; a SD-WAN poderá ser priorizada para acesso à Internet e serviços públicos externos. Em contingência, ambas as camadas deverão estar aptas a transportar qualquer classe de tráfego, conforme políticas de roteamento, QoS e failover definidas no projeto executivo.

A adoção de MPLS com a mesma capacidade nominal dos links SD-WAN reduz o risco de subdimensionamento em cenários de crise, elimina a necessidade de escolher previamente quais sistemas seriam degradados durante falha de uma camada e preserva a experiência operacional das unidades. Essa premissa é aderente à criticidade da prestação jurisdicional, à continuidade do PJe, à autenticação, à colaboração institucional, aos serviços de TIC e às rotinas de suporte remoto.

Adicionalmente, a demanda contempla grupo próprio para interligação direta entre o Edifício Sede e o Foro de Brasília por link dedicado ponto-a-ponto de 25 Gbps, distinto da rede MPLS. Esse enlace dedicado deverá funcionar como infraestrutura de alta capacidade para replicação de dados, sincronização de ambientes, tráfego de backup, continuidade operacional, redundância da Sede e eventual redirecionamento do acesso das unidades ao Foro de Brasília em cenários de indisponibilidade ou degradação relevante da Sede. Por se tratar de comunicação de alto desempenho entre dois pontos institucionais específicos, a tecnologia adequada é link dedicado/LAN-to-LAN/Metro Ethernet ou equivalente funcional, e não MPLS de acesso das localidades.

### 2.1.1 Soluções possíveis consideradas

Foram consideradas três alternativas arquiteturais para atendimento da necessidade:

| Alternativa | Síntese | Avaliação preliminar |
|---|---|---|
| Solução 1 - MPLS integrado à SD-WAN | Contratar MPLS para tráfego crítico e manter SD-WAN para Internet, com contingência cruzada entre as camadas. | Alternativa preferencial, por combinar rede privada, QoS, centralização na Sede, aproveitamento da SD-WAN existente e resiliência operacional. |
| Solução 2 - Links satelitais | Contratar enlaces satelitais para cumprir papel equivalente ao MPLS na interconexão das unidades. | Alternativa útil para contingência extrema ou localidades sem cobertura terrestre, mas com maior latência, possível variabilidade e menor aderência ao tráfego crítico sensível. |
| Solução 3 - Links de Internet comuns com VPN ponto a ponto | Usar acessos convencionais de Internet com túneis VPN entre unidades e Sede. | Alternativa de menor complexidade inicial, porém com menor previsibilidade, maior esforço de operação, maior exposição e maior dependência da qualidade da Internet local. |

A Solução 1 é indicada como preferencial para desenvolvimento no ETP por combinar a SD-WAN vigente com uma camada privada para tráfego crítico e permitir que a Sede, dotada de 3 saídas redundantes de Internet, concentre políticas de segurança, controle e observabilidade.

### 2.2 A necessidade de contratação decorre de exigência legal?

Não há exigência legal específica para contratar MPLS como tecnologia. A necessidade decorre da obrigação administrativa de assegurar continuidade, disponibilidade, segurança e desempenho dos serviços de TIC que suportam a atividade jurisdicional e administrativa.

A demanda se relaciona com a Lei nº 14.133/2021, especialmente quanto ao planejamento da contratação, ETP e Termo de Referência, e com a ENTIC-JUD 2021-2026, instituída pela Resolução CNJ nº 370/2021, que orienta a governança de TIC do Poder Judiciário e a disponibilidade dos serviços digitais. Os documentos anteriores também citam diretriz de prover links suficientes entre unidades e órgão, bem como links de comunicação com a Internet preferencialmente com operadoras distintas.

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
| 9 | Vara de Guaraí | Avenida Araguaia, esquina com Av. Bernardo Sayao, 1360 | Guaraí | TO | 77.700-000 |
| 10 | Prédio de Apoio | SGAN 916 Norte, Lote AI, Asa Norte | Brasília | DF | 70.790-160 |

O Foro de Brasília, além de unidade beneficiada como localidade de atendimento, passa a ter papel técnico adicional como ponto de redundância da Sede, ambiente de replicação e concentrador contingencial para acesso das unidades, condicionado ao projeto executivo de roteamento, segurança, capacidade e continuidade.

### 2.4 Consequências do não atendimento da demanda

- Permanência de maior dependência da SD-WAN como única camada estruturada de interconexão corporativa.

- Menor previsibilidade para tráfego crítico em cenários de degradação dos enlaces de Internet.

- Dificuldade de concentrar políticas de segurança, monitoramento, filtragem e controle de tráfego na Sede.

- Risco de indisponibilidade ou degradação de acesso a sistemas judiciais e administrativos.

- Menor resiliência para rotas de contingência, suporte, replicação, autenticação e serviços institucionais.

- Dificuldade de evoluir para arquitetura com saída de Internet preferencial centralizada na Sede, uso de 3 saídas redundantes e separação lógica entre tráfego crítico e tráfego de Internet.

- Risco de descumprimento de diretrizes de governança de TIC relativas a disponibilidade, capacidade, segurança e continuidade.

## 3. Descrição Sucinta do Objeto

### 3.1 Objeto da contratação

Contratação de empresa especializada para prestação de serviços continuados de comunicação de dados por meio de rede MPLS, incluindo fornecimento, instalação, configuração, equipamentos necessários, monitoramento, suporte técnico, manutenção e garantia de níveis de serviço, para interconexão das unidades do TRT10 à Sede e integração operacional com a SD-WAN vigente.

A contratação deverá:

- interconectar todas às demais localidades à Sede por MPLS;

- manter compatibilidade com a topologià SD-WAN existente;

- permitir uso preferencial do MPLS para tráfego crítico e da SD-WAN para tráfego de Internet;

- permitir contingência cruzada, de modo que MPLS e SD-WAN possam transportar trafegos críticos ou de Internet em caso de indisponibilidade ou degradação de uma das camadas;

- permitir roteamento controlado para saída de Internet preferencial pela Sede;

- integrar-se às redes JT, Infovia e demais redes institucionais conforme definição técnica do TRT10;

- possibilitar QoS, segregação lógica e priorizacao de tráfego crítico;

- contemplar suporte, monitoramento e relatórios mensais de disponibilidade;

- evitar especificação por marca, fabricante ou modelo, salvo quando indispensável e tecnicamente justificado em etapa posterior.

O objeto também contempla, em grupo específico e tecnicamente segregado, link dedicado ponto-a-ponto de 25 Gbps entre o Edifício Sede e o Foro de Brasília, por fibra óptica, LAN-to-LAN, Metro Ethernet, clear channel, E-Line, E-LAN ou tecnologia equivalente, com banda simétrica, full duplex, baixa latência, SLA, monitoramento e equipamentos em comodato ou fornecidos como parte do serviço, destinado à replicação, redundância, continuidade e acesso contingencial das unidades.

## 4. Quantidade a Ser Contratada

### 4.1 Quantidade estimada por ano

| Item | Localidade | Capacidade SD-WAN vigente | Capacidade MPLS requerida | Quantidade | Unidade |
|---|---|---|---|---|---|
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

Grupo específico de interligação dedicada Sede-Foro:

| Item | Enlace dedicado | Tecnologia / função | Capacidade | Quantidade | Unidade |
|---|---|---|---|---|---|
| 11 | Edifício Sede ↔ Foro de Brasília | link dedicado ponto-a-ponto por fibra óptica, LAN-to-LAN/Metro Ethernet ou equivalente; replicação e redundância da Sede | 25 Gbps | 1 | mês |

As capacidades MPLS requeridas correspondem às capacidades SD-WAN vigentes em cada localidade, com a finalidade de assegurar redundância total entre as camadas de conectividade. O dimensionamento deverá ser validado por meio de análise de tráfego, criticidade dos sistemas, simultaneidade, QoS, crescimento esperado, desempenho da SD-WAN vigente, capacidade de processamento dos CPEs e pesquisa de mercado.

O enlace dedicado de 25 Gbps não integra a malha MPLS das localidades. Ele constitui grupo próprio por possuir finalidade, escala, tecnologia, precificação e requisitos de desempenho distintos: interligação de alta capacidade entre dois pontos centrais, suporte à replicação e possibilidade de o Foro assumir papel contingencial de concentrador.

### 4.2 A estimativa e baseada no histórico demandado?

Sim. A estimativa considera o histórico de contratações de comunicação de dados do TRT10, notadamente:

- Contrato 131/2023, referente a link IP dedicado com SD-WAN para 10 localidades, com vigência inicial de 5 anos e possibilidade de prorrogação;

- contratações anteriores de Internet com Anti-DDoS para a Sede, Foro de Brasília e Prédio de Apoio;

- contratação anterior de links de Internet para unidades do Tocantins;

- menções documentais a conectividade MPLS e Infovia como meios de redundância e interconexão com à Sede.

## 5. Estimativa Preliminar do Valor da Contratação

### 5.1 Valor estimado da contratação

O valor oficial deverá ser apurado pela área competente em pesquisa de preços formal. Para memória preliminar, foram levantadas referências públicas de contratações similares de MPLS, L2L ou rede privada corporativa, com capacidades de 100 Mbps, 500 Mbps e 1 Gbps. A amostra abaixo não substitui a pesquisa formal do processo, pois os preços variam conforme localidade, interiorização, rota física, dupla abordagem, SLA, CPE/roteador, prazo contratual, volume de pontos e escopo de monitoramento.

Com base nas referências localizadas, adota-se apenas como estimativa inicial a média simples dos valores mensais unitários por capacidade. A memória de cálculo utiliza as seguintes fórmulas:

- Preço médio mensal por capacidade = soma dos preços mensais unitários das referências / número de referências válidas;

- Valor mensal por capacidade = preço médio mensal por capacidade x quantidade de links TRT10 naquela capacidade;

- Valor anual por capacidade = valor mensal por capacidade x 12;

- Total mensal MPLS = soma dos valores mensais das capacidades de 1 Gbps, 500 Mbps e 100 Mbps;

- Total anual MPLS = total mensal MPLS x 12;

- Valor mensal do link dedicado Sede-Foro 25 Gbps = ponto médio da faixa preliminar de mercado, isto é, (R$ 30.000,00 + R$ 60.000,00) / 2 = R$ 45.000,00;

- Valor anual do link dedicado Sede-Foro 25 Gbps = R$ 45.000,00 x 12 = R$ 540.000,00.

| Capacidade | Referências usadas na média | Fórmula do preço médio mensal | Quantidade TRT10 | Valor mensal preliminar | Valor anual preliminar |
|---|---|---|---|---|---|
| 1 Gbps | MPRS R$ 4.740,75; Santa Maria/RS R$ 1.429,68; Xanxerê/SC R$ 1.000,00 | (4.740,75 + 1.429,68 + 1.000,00) / 3 = R$ 2.390,14 | 2 | R$ 4.780,28 | R$ 57.363,36 |
| 500 Mbps | MPRS R$ 3.687,25; Glorinha/RS R$ 1.550,00; Xanxerê/SC R$ 119,00 | (3.687,25 + 1.550,00 + 119,00) / 3 = R$ 1.785,42 | 3 | R$ 5.356,25 | R$ 64.275,00 |
| 100 Mbps | MPRS R$ 1.580,25; Transitar/Cascavel R$ 761,56; TJPB R$ 2.425,00 | (1.580,25 + 761,56 + 2.425,00) / 3 = R$ 1.588,94 | 5 | R$ 7.944,68 | R$ 95.336,16 |
| Total preliminar MPLS | - | Soma dos valores mensais por capacidade | 10 | R$ 18.081,21 | R$ 216.974,52 |
| Link dedicado Sede-Foro 25 Gbps | Faixa paramétrica baseada em precedentes PNCP compatíveis de 4, 5 e 10 Gbps | (30.000,00 + 60.000,00) / 2 = R$ 45.000,00 | 1 | R$ 45.000,00 | R$ 540.000,00 |
| Total preliminar geral | MPLS + link dedicado 25 Gbps | 18.081,21 + 45.000,00 | 11 | R$ 63.081,21 | R$ 756.974,52 |

Para o grupo de link dedicado Sede-Foro de 25 Gbps, não foram localizados nesta pesquisa preliminar três itens PNCP exatamente com 25 Gbps e o mesmo escopo ponto-a-ponto. Foram localizadas, contudo, contratações PNCP/públicas compatíveis por similaridade técnica, envolvendo LAN-to-LAN, Metro Ethernet, fibra dedicada, links de 4 Gbps, 5 Gbps e 10 Gbps, além de especificações públicas que aceitam interfaces 10/25Gbps SFP28. Como estimativa conservadora inicial, recomenda-se tratar o enlace de 25 Gbps como item de alta capacidade sujeito a cotação formal. Para planejamento preliminar, adota-se faixa indicativa de R$ 30.000,00 a R$ 60.000,00 mensais, com ponto de partida de R$ 45.000,00 mensais, equivalente a R$ 540.000,00 anuais, até que a pesquisa formal confirme valores para Brasília/DF, dupla abordagem, SLA, baixa latência, interfaces 25GbE e roteamento/segurança exigidos.

O valor acima deve ser tratado como indicativo de ordem de grandeza e deverá ser recalculado pela pesquisa de preços formal, preferencialmente com itens PNCP atuais, cotações diretas com fornecedores aptos a atender DF/TO, análise crítica de outliers e demonstrativo de memória de cálculo. As referências que não possuam número de controle PNCP integralmente confirmado devem ser usadas apenas como apoio metodológico ou substituídas por referências PNCP atuais na pesquisa formal.

### 5.2 Como se chegou ao valor preliminar?

Para fins de memória inicial, os documentos anteriores registram valores históricos de contratos de comunicação de dados e Internet, mas tais valores não devem ser usados diretamente como orçamento atual sem atualização metodológica, comparação de escopo, pesquisa de mercado e tratamento das diferenças entre Internet dedicada, SD-WAN e MPLS.

A pesquisa deverá observar, no mínimo:

- preços públicos de serviços MPLS ou redes privadas corporativas similares;

- capacidades por localidade;

- custos de instalação, equipamentos e ativação;

- prazo contratual pretendido;

- SLA exigido;

- eventual necessidade de rotas físicas distintas, QoS, VRF, BGP/OSPF ou monitoramento.

Enquanto não houver pesquisa formal, a estimativa de valor deve permanecer como pendência de planejamento, sem prejuízo da continuidade da estruturação técnica do DFD, ETP e TR.

### 5.3 Referências preliminares de preços por capacidade

Pesquisa realizada em 02/06/2026. A API oficial de consulta do PNCP apresentou instabilidade/erro de conexão nesta sessão; por isso, foram utilizadas páginas públicas, publicações oficiais, portais de transparência e editais indexados que indicam publicação ou origem PNCP quando disponível. O PNCP, conforme página oficial de dados abertos, disponibiliza APIs públicas para consultar contratações, contratos, atas e itens sem cadastro, e o número de controle PNCP deve ser confirmado na pesquisa formal final.

| Capacidade | Órgão / contrato de referência | Número do pregão/licitação e identificador | Item utilizado | Valor mensal unitário usado | Fonte / observação |
|---|---|---|---|---|---|
| 100 Mbps | Ministério Público do Estado do Rio Grande do Sul - Contrato 68/2024 | Pregão Eletrônico nº 007/2024; Procedimento nº 02405.000.098/2024; contrato com Brasil Serviços de Telecomunicações Ltda.; fonte MPRS | Circuito MPLS óptico duplo com roteador - 100 Mbps, item 6 da planilha reajustada | R$ 1.580,25 | Fonte: Portal de Transparência MPRS / 1ª Apostila ao Contrato 68/2024, com valores reajustados. Número PNCP não localizado na minuta. |
| 100 Mbps | Município de Cascavel/PR / Autarquia Transitar | Edital 90129/2025; Pregão eletrônico; PNCP-76208867000107-1-000429/2025; abertura em 03/11/2025 | Link de dados MPLS 100 Mbps - mensalidade | R$ 761,56 | Fonte: PNCP/Alerta Licitação e documento público de Cascavel/Transitar; objeto de comunicação de dados por Rede IP com tecnologia MPLS. |
| 100 Mbps | Tribunal de Justiça da Paraíba | Pregão Eletrônico nº 010/2019; Processo Administrativo Eletrônico 2019094162 | Lote 01, item 03 - Link de Transporte de Dados, tecnologia MPLS, 100 Mbps | R$ 2.425,00 | Fonte: edital institucional TJPB. Referência anterior ao PNCP e à Lei nº 14.133/2021; usada apenas como referência auxiliar/histórica. |
| 500 Mbps | Ministério Público do Estado do Rio Grande do Sul - Contrato 68/2024 | Pregão Eletrônico nº 007/2024; Procedimento nº 02405.000.098/2024; contrato com Brasil Serviços de Telecomunicações Ltda.; fonte MPRS | Circuito MPLS óptico duplo com roteador - 500 Mbps, item 9 da planilha reajustada | R$ 3.687,25 | Fonte: Portal de Transparência MPRS / 1ª Apostila ao Contrato 68/2024, com valores reajustados. Número PNCP não localizado na minuta. |
| 500 Mbps | Município de Glorinha/RS | Processo Administrativo nº 25.714/2025; documento técnico assinado em 10/09/2025; pregão/sessão pública indicada em 02/03/2026 em agregador público; PNCP a confirmar | Serviço de conexão ponto a ponto em Camada 2 (L2L), transporte Ethernet/MPLS, 500 Mbps, 12 meses | R$ 1.550,00 | Fonte: documento público do Município de Glorinha/RS; a própria minuta informa consulta de preços via PNCP e Portal de Compras Públicas. Número do pregão/PNCP não foi localizado integralmente. |
| 500 Mbps | Município de Xanxerê/SC | Pregão Eletrônico nº 0032/2024; UASG 988383; edital público | Link MPLS 500 MB | R$ 119,00 | Fonte: edital público de Xanxerê/SC. Valor muito baixo, tratado como possível outlier por escopo municipal/volume de pontos. |
| 1 Gbps | Ministério Público do Estado do Rio Grande do Sul - Contrato 68/2024 | Pregão Eletrônico nº 007/2024; Procedimento nº 02405.000.098/2024; contrato com Brasil Serviços de Telecomunicações Ltda.; fonte MPRS | Circuito MPLS óptico duplo com roteador - 1.000 Mbps, item 10 da planilha reajustada | R$ 4.740,75 | Fonte: Portal de Transparência MPRS / 1ª Apostila ao Contrato 68/2024, com valores reajustados. Número PNCP não localizado na minuta. |
| 1 Gbps | Município de Santa Maria/RS | Pregão Eletrônico nº 90055/2025; UASG 988841; registro de preços; ata/resultado público | Lote/item 6 - Serviços de comunicação de dados tecnologia MPLS 1 Gbps, locação de 1 ponto equivalente a 12 serviço/mês, total de 4 pontos | R$ 1.429,68 | Fonte: documento público da Prefeitura de Santa Maria/RS; fornecedor Brasil Tecpar Serviços de Telecomunicações S.A.; valor unitário do item. |
| 1 Gbps | Município de Xanxerê/SC | Pregão Eletrônico nº 0032/2024; UASG 988383; edital público | Link MPLS 01 GB | R$ 1.000,00 | Fonte: edital público de Xanxerê/SC; possível influência de grande volume de pontos e escopo municipal. |

Fontes preliminares consultadas: Portal PNCP em Dados Abertos; Manual da API de Consultas PNCP; Portal de Transparência do MPRS; Edital PE 0032/2024 de Xanxerê/SC; publicação de Glorinha/RS; documentos públicos de Santa Maria/RS, Cascavel/PR e TJPB.

### 5.3.2 Rastreabilidade das fontes consultadas

Rastreabilidade das fontes consultadas:

| Referência | Consulta pública / identificador | Observação de uso |
| --- | --- | --- |
| MPRS - Contrato 68/2024 | Portal de Transparência MPRS; Procedimento nº 02405.000.098/2024; Pregão Eletrônico nº 007/2024; Súmula do Contrato de Prestação de Serviços Contínuos nº 0068/2024 | Fonte dos itens MPLS 100 Mbps, 500 Mbps e 1 Gbps, com valores da 1ª Apostila/reajuste. |
| Cascavel/PR - Transitar | PNCP-76208867000107-1-000429/2025; Edital 90129/2025; Pregão eletrônico; consulta PNCP: https://pncp.gov.br/app/editais/76208867000107/2025/429 | Fonte do item MPLS 100 Mbps, com objeto de comunicação de dados por Rede IP/MPLS. |
| TJPB | Pregão Eletrônico nº 010/2019; Processo Administrativo Eletrônico nº 2019094162 | Fonte auxiliar/histórica para item MPLS 100 Mbps, anterior ao PNCP. |
| Glorinha/RS | Processo Administrativo nº 25.714/2025; documento técnico municipal assinado em 10/09/2025; pregão/sessão pública indicada para 02/03/2026 | Fonte do item L2L Ethernet/MPLS 500 Mbps. Número PNCP/pregão não localizado integralmente na pesquisa preliminar. |
| Xanxerê/SC | Pregão Eletrônico nº 0032/2024; UASG 988383 | Fonte dos itens MPLS 500 Mbps e 1 Gbps; valor tratado com cautela por possível outlier. |
| Santa Maria/RS | Pregão Eletrônico nº 90055/2025; UASG 988841; resultado/ata pública municipal | Fonte do item MPLS 1 Gbps, fornecedor Brasil Tecpar Serviços de Telecomunicações S.A., valor unitário R$ 1.429,68. |
| Candeias/BA | PNCP-13830336000123-1-000051/2026; Edital 023/2026; consulta PNCP: https://pncp.gov.br/app/editais/13830336000123/2026/51 | Referência de alta capacidade para LAN-to-LAN, fibra dedicada, concentradores de 10 Gbps e link dedicado 4 Gbps. |
| Jaguariúna/SP | PNCP-46410866000171-1-000610/2024; Edital PL-674/2024; PE 90081/2024; consulta PNCP: https://pncp.gov.br/editais/46410866000171/2024/610 | Referência de alta capacidade para link dedicado simétrico de 10 Gbps, embora com escopo de acesso à Internet. |
| Ubarana/SP | PNCP-65708786000141-1-000038/2026; Edital 19/2026; consulta PNCP: https://pncp.gov.br/app/editais/65708786000141/2026/38 | Referência de alta capacidade para rede LAN-to-LAN por fibra dedicada, capacidade agregada até 10 Gbps. |
| TJPR | PNCP 77821841000194-1-000049/2025; Edital PE 15/2025 | Referência de alta capacidade para dois links dedicados de 10 Gbps, BGP, Anti-DDoS e operadoras distintas. |
| JFRS/TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços nº 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Referência técnica de Metro Ethernet/LAN-to-LAN/ponto-a-ponto; valor do item específico não confirmado. |

### 5.3.1 Referências preliminares para o grupo de link dedicado Sede-Foro 25 Gbps

Pesquisa realizada em 02/06/2026. Não foram encontrados três itens exatamente equivalentes a link dedicado ponto-a-ponto de 25 Gbps. As referências abaixo são compatíveis por similaridade técnica e devem ser usadas como indícios, não como estimativa final.

| Referência | Número do pregão/licitação e identificador | Objeto compatível | Valor informado | Uso na estimativa |
|---|---|---|---|---|
| Município de Candeias/BA | Edital 023/2026; Pregão eletrônico; PNCP-13830336000123-1-000051/2026; abertura em 13/03/2026 | Comunicação de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra óptica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos | R$ 950.560,00 | Similaridade por LAN-to-LAN, fibra dedicada, alta capacidade, rotas redundantes e equipamentos. |
| Município de Jaguariúna/SP | Edital PL-674/2024; PE 90081/2024; Pregão eletrônico; PNCP-46410866000171-1-000610/2024; abertura em 16/10/2024 | Link dedicado de acesso à Internet bidirecional e simétrico de 10 Gbps e link compartilhado de internet banda larga | R$ 4.705.844,00 | Similaridade por link dedicado 10 Gbps; escopo de Internet, não ponto-a-ponto. |
| Município de Ubarana/SP | Edital 19/2026; Pregão eletrônico; PNCP-65708786000141-1-000038/2026; abertura em 15/04/2026 | Rede LAN-to-LAN por fibra óptica dedicada, capacidade agregada de até 10 Gbps, ponto concentrador e link dedicado de acesso à Internet | R$ 184.400,00 | Similaridade por LAN-to-LAN, fibra dedicada e limite agregado de 10 Gbps. |
| TJPR | Edital PE 15/2025; PNCP 77821841000194-1-000049/2025; Pregão eletrônico | Dois links dedicados de 10 Gbps cada, BGP, Anti-DDoS e operadoras distintas para Sistema Autônomo de Internet do TJPR | R$ 187.560,00 | Similaridade por 10 Gbps, redundância e operadoras distintas; escopo de Internet/AS, não replicação ponto-a-ponto. |
| JFRS/TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Serviços de comunicação de dados dedicados e exclusivos para acesso à Internet e comunicação ponto a ponto entre sites via Metro Ethernet / LAN-to-LAN, camada 2 | Valor de item específico a confirmar na pesquisa formal | Similaridade funcional por Metro Ethernet/LAN-to-LAN e comunicação ponto a ponto entre sites; usado como referência técnica, não como preço direto. |

As referências acima não foram usadas para cálculo de média direta do item de 25 Gbps, porque os valores informados correspondem a objetos, prazos e escopos distintos. Elas foram usadas para demonstrar compatibilidade técnica de mercado e para balizar a faixa paramétrica preliminar de R$ 30.000,00 a R$ 60.000,00 mensais. Também foi localizada especificação federal de modernização de rede que admite interfaces de 10/25Gbps SFP28, indicando aderência de mercado para portas 25GbE em equipamentos de rede corporativa. Essa referência apoia a viabilidade técnica do enlace, mas não serve como preço mensal de serviço de telecomunicações.

### 5.4 Contratações similares a detalhar na pesquisa

Para subsidiar o ETP, o TR, a pesquisa de preços, a definição de SLA e a validação das especificações técnicas, deverão ser priorizadas contratações que possuam maior similaridade com a arquitetura pretendida pelo TRT10. A similaridade deverá considerar: uso de MPLS, L3VPN, L2L ou rede privada corporativa; interligação de múltiplas unidades a ponto concentrador; fibra óptica; CPE ou roteador incluso; monitoramento; suporte; disponibilidade; e capacidades próximas a 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps e 1 Gbps.

Como referências principais, recomenda-se detalhar:

| Prioridade | Contratação/produto similar | Motivo da similaridade | Informações a buscar |
|---|---|---|---|
| 1 | Solução de Rede Privada Virtual MPLS sobre fibra óptica para interligação de 45 pontos | Rede privada, múltiplos pontos, fibra óptica e interligação institucional | TR, ETP, SLA, matriz de riscos, preços por ponto, CPE, concentrador e monitoramento |
| 2 | Redes Privadas LAN-to-LAN ou MPLS entre Data Center Municipal e unidades remotas | Topologia semelhante a hub-and-spoke, com concentrador e unidades remotas | Arquitetura, aceite, disponibilidade, roteamento, suporte e valores mensais |
| 3 | Serviço de Link de Comunicação Multimídia Concentrador L3VPN/MPLS, 3 Gbps | Comparável ao papel da Sede como concentrador | Requisitos do concentrador, SLA, QoS, roteamento, suporte e preço do link central |
| 4 | Serviços de Link de Comunicação Multimídia L3VPN/MPLS de 100 Mbps, 200 Mbps e 400 Mbps | Comparável aos circuitos das unidades | Preço mensal por capacidade, instalação, CPE, SLA e prazo de reparo |
| 5 | Circuitos MPLS ópticos com roteador, simples e duplos, em 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps e 1 Gbps | Aderente a capacidades propostas e à exigência de equipamento gerenciado | Diferença de preço entre circuito simples e duplo, instalação, roteador e disponibilidade |
| 6 | Serviço de acesso link de dados com tecnologia MPLS Capital/Interior, 50 Mbps a 1 Gbps, por 60 meses | Permite comparar capital/interior, prazo e velocidades próximas | Planilha de itens, valores unitários, vigência, reajuste, SLA e suporte |
| 7 | Rede MPLS ou superior / SD-WAN Interior | Alta aderência por envolver MPLS e SD-WAN | Justificativa da arquitetura híbrida, failover, roteamento, SLA e preços |

Como referências secundárias, poderão ser analisadas contratações de transporte IP com fibra óptica, suporte a tunelamento, VLANs, roteamento TCP/IP e MPLS; redes IP multisservicos com operação, manutenção e monitoramento; serviços MPLS/L2L; e links dedicados com MPLS ou EAPS e dupla abordagem. Essas referências são úteis para requisitos técnicos e disponibilidade, mas devem ser avaliadas com cautela quando não houver rede privada corporativa completa ou quando o objeto principal for apenas Internet.

Para a comparação das alternativas do ETP, deverão ser buscadas referências de links satelitais e de links comuns de Internet com VPN ponto a ponto. Essas referências servirão para justificar a rejeição ou classificação secundária das Soluções 2 e 3, especialmente quanto a latência, previsibilidade, SLA, superfície de exposição, custo operacional e aderência a tráfego crítico.

Não devem ser usados como referência principal de preços da presente contratação itens de aquisição de switches, roteadores avulsos, telefonia IP, web server, integração de sistemas, instalação de rede local, fusão de fibra ou manutenção de equipamentos, pois tais objetos não representam serviço continuado de rede privada corporativa interligando unidades à Sede.

## 6. Data Pretendida para Conclusão da Contratação

### 6.1 Data de início de vigência

Sugere-se que a nova contratação esteja vigente antes de qualquer marco de encerramento ou degradação de contratos correlatos que sustentem a conectividade das unidades, observada a antecedência mínima para tramitação dos artefatos de planejamento.

### 6.2 Trata-se de serviço continuado?

Sim. Trata-se de serviço continuado de comunicação de dados, essencial para o funcionamento permanente das unidades do TRT10.

## 7. Grau de Prioridade da Contratação

### 7.1 Tabela de identificação do grau de prioridade

| Criterio | Marcacao sugerida | Justificativa |
|---|---|---|
| Impacto se não atendida | Grave | Pode afetar disponibilidade, desempenho, contingência e segurança da comunicação institucional. |
| Urgência | Não é urgente, mas precisa ser realizada o mais rápido possível | Há necessidade de planejamento, pesquisa de preços, implantação e operação assistida, evitando solução de continuidade. |
| Tendência do problema | Ira piorar | A demanda por tráfego corporativo, segurança centralizada e continuidade tende a crescer. |

## 8. Vinculação ou Dependencia com Outra Demanda

A demanda possui vinculação técnica com:

- contrato SD-WAN vigente, objeto do processo SEI 0000030-87.2023.5.10.8000;

- contratos de Internet e Anti-DDoS da Sede e demais unidades;

- redes JT, Infovia e arquitetura de segurança perimetral;

- projeto de centralização de saída de Internet na Sede, considerando 3 saídas redundantes.

## 9. Objetivo Estratégico

A contratação se alinha ao objetivo estratégico de aprimorar a Governança de TIC e a proteção de dados, contribuindo para disponibilidade, continuidade, segurança, monitoramento e desempenho dos serviços digitais do TRT10.

## 10. Informacoes SIGEO

### 10.1 Processo administrativo da contratação em vigor

**Processos de referência histórica: SEI 0000030-87.2023.5.10.8000, SEI 0007608-72.2021.5.10.8000 e SEI 0002027-76.2021.5.10.8000.**

### 10.2 Contrato ou ARP em vigor

Contrato 131/2023 relacionado a link IP dedicado com SD-WAN. Contratos anteriores de Internet/Anti-DDoS e links das unidades devem ser conferidos pela área de contratos para atualização de vigência e número no SIGEO.

### 10.3 Item SIGEO

A informar pela área competente.

### 10.4 Estimativa para 12 meses no SIGEO

A informar após pesquisa de preços.

## 11. Servidor Responsável pela Demanda

Nome: Edson Mateus de Sousa - Coordenador da CDTEC

E-mail funcional: cdtec@trt10.jus.br

Telefone: (61) 3348-1249 / 1288 / 1280 / 1188

## 12. Figura 1 - Arquitetura Proposta SD-WAN + MPLS + Link Dedicado Sede-Foro

![Figura 1 - Arquitetura proposta SD-WAN + MPLS + link dedicado Sede-Foro 25 Gbps](../diagrama_topologia_revisada.png)
