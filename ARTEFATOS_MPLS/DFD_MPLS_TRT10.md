# DOCUMENTO DE FORMALIZACAO DE DEMANDA (DFD)

**Orgao:** Tribunal Regional do Trabalho da 10a Regiao - TRT10  
**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC  
**Objeto:** Contratacao de servicos continuados de comunicacao de dados por MPLS para interconexao das unidades do TRT10 a Sede, em arquitetura integrada com a SD-WAN atual, adotando capacidades MPLS equivalentes as capacidades dos links SD-WAN por localidade, e contratacao de grupo especifico de link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasilia, para replicacao, redundancia da Sede e continuidade de acesso das unidades.  
**Versao:** Minuta tecnica revisada - redundancia total MPLS/SD-WAN  
**Data:** 02/06/2026

## 1. Unidade Demandante

### 1.1 Nome da Unidade

Coordenadoria de Infraestrutura de Tecnologia.

### 1.2 Sigla da Unidade

CDTEC.

## 2. Justificativa da Necessidade da Contratacao

### 2.1 Justificativa da necessidade

O TRT10 depende de conectividade permanente, segura e resiliente entre suas unidades para sustentar o Processo Judicial Eletronico, sistemas administrativos, servicos internos de TIC, autenticacao, colaboracao institucional, acesso a redes externas, contingencia, suporte tecnico e atividades de atendimento ao publico.

Os documentos de contratacoes anteriores demonstram historico recorrente de contratacao de links de comunicacao de dados, links de Internet, redundancia de acesso e servicos de suporte associados. Em especial:

- o processo SEI 0000030-87.2023.5.10.8000 registra a contratacao de Link IP dedicado com SD-WAN para 10 localidades, com bandas de 1 Gbps na Sede e no Foro de Brasilia, 500 Mbps no Foro de Taguatinga, Foro de Palmas e Predio de Apoio, e 100 Mbps nas demais unidades;
- o mesmo processo registra disponibilidade minima de 99,90% para a Sede e 99,70% para as demais localidades;
- os processos anteriores de Internet e links das unidades indicam a necessidade de redundancia, monitoramento, disponibilidade, abertura de chamados, glosas por indisponibilidade e manutencao da continuidade dos servicos;
- documentos de 2021/2022 ja registravam que Foro de Brasilia e Predio de Apoio se conectavam a Sede por MPLS e Infovia, demonstrando que a concentracao de trafego na Sede e a interconexao privada das unidades fazem parte do historico arquitetural do Tribunal.

A nova demanda consiste em contratar servicos MPLS para interconectar todas as demais localidades a Sede, preservando a SD-WAN atual e estabelecendo uma camada corporativa privada, previsivel e controlada para trafego critico. A Sede devera operar como concentrador preferencial de saida de Internet e das redes institucionais, considerando a existencia de 3 saidas de Internet redundantes na Sede.

A contratacao nao tem por finalidade substituir a SD-WAN atual, mas complementar a arquitetura com uma camada MPLS de capacidade equivalente a dos enlaces SD-WAN existentes em cada localidade. A opcao por capacidades equivalentes decorre da necessidade de redundancia total: em caso de indisponibilidade, manutencao, degradacao severa ou falha operacional de uma das camadas, a outra devera ter capacidade nominal suficiente para absorver integralmente o perfil de trafego esperado da unidade, sem reducao planejada da banda contratada. Na operacao normal, o MPLS podera ser priorizado para sistemas criticos, servicos corporativos internos, autenticacao, integracoes institucionais, administracao de rede e demais fluxos definidos pela CDTEC; a SD-WAN podera ser priorizada para acesso a Internet e servicos publicos externos. Em contingencia, ambas as camadas deverao estar aptas a transportar qualquer classe de trafego, conforme politicas de roteamento, QoS e failover definidas no projeto executivo.

A adocao de MPLS com a mesma capacidade dos links SD-WAN tambem reduz o risco de subdimensionamento em cenarios de crise, elimina a necessidade de escolher previamente quais sistemas seriam degradados durante falha da camada principal e preserva a experiencia operacional das unidades. Embora a alternativa de MPLS com banda inferior pudesse reduzir custo mensal, ela criaria contingencia parcial e exigiria politica de degradacao de servicos em momento de incidente, o que e menos aderente a criticidade da prestacao jurisdicional, a continuidade do PJe, a autenticacao, a colaboracao institucional, aos servicos de TIC e as rotinas de suporte remoto.

Adicionalmente, a presente revisao inclui um novo grupo de contratacao para interligacao direta entre o Edificio Sede e o Foro de Brasilia por link dedicado ponto-a-ponto de 25 Gbps, distinto da rede MPLS. Esse enlace dedicado devera funcionar como infraestrutura de alta capacidade para replicacao de dados, sincronizacao de ambientes, trafego de backup, continuidade operacional, redundancia da Sede e eventual redirecionamento do acesso das unidades ao Foro de Brasilia em cenarios de indisponibilidade ou degradacao relevante da Sede. Por se tratar de comunicacao de alto desempenho entre dois pontos institucionais especificos, a tecnologia adequada e link dedicado/LAN-to-LAN/Metro Ethernet ou equivalente funcional, e nao MPLS de acesso das localidades.

### 2.1.1 Solucoes possiveis consideradas

Foram consideradas tres alternativas arquiteturais para atendimento da necessidade:

| Alternativa | Sintese | Avaliacao preliminar |
|---|---|---|
| Solucao 1 - MPLS integrado a SD-WAN | Contratar MPLS para trafego critico e manter SD-WAN para Internet, com contingencia cruzada entre as camadas. | Alternativa preferencial, por combinar rede privada, QoS, centralizacao na Sede, aproveitamento da SD-WAN existente e resiliencia operacional. |
| Solucao 2 - Links satelitais | Contratar enlaces satelitais para cumprir papel equivalente ao MPLS na interconexao das unidades. | Alternativa util para contingencia extrema ou localidades sem cobertura terrestre, mas com maior latencia, possivel variabilidade e menor aderencia ao trafego critico sensivel. |
| Solucao 3 - Links de Internet comuns com VPN ponto a ponto | Usar acessos convencionais de Internet com tuneis VPN entre unidades e Sede. | Alternativa de menor complexidade inicial, porem com menor previsibilidade, maior esforco de operacao, maior exposicao e maior dependencia da qualidade da Internet local. |

A Solucao 1 e indicada como preferencial para desenvolvimento no ETP por preservar os investimentos ja realizados em SD-WAN, acrescentar camada privada para trafego critico e permitir que a Sede, dotada de 3 saidas redundantes de Internet, concentre politicas de seguranca, controle e observabilidade.

### 2.2 A necessidade de contratacao decorre de exigencia legal?

Nao ha exigencia legal especifica para contratar MPLS como tecnologia. A necessidade decorre da obrigacao administrativa de assegurar continuidade, disponibilidade, seguranca e desempenho dos servicos de TIC que suportam a atividade jurisdicional e administrativa.

A demanda se relaciona com a Lei no 14.133/2021, especialmente quanto ao planejamento da contratacao, ETP e Termo de Referencia, e com a ENTIC-JUD 2021-2026, instituida pela Resolucao CNJ no 370/2021, que orienta a governanca de TIC do Poder Judiciario e a disponibilidade dos servicos digitais. Os documentos anteriores tambem citam diretriz de prover links suficientes entre unidades e orgao, bem como links de comunicacao com a Internet preferencialmente com operadoras distintas.

### 2.3 Quais unidades serao beneficiadas?

Serao beneficiadas todas as unidades do TRT10 atendidas pela rede institucional:

| Item | Unidade / Localidade | Endereco | Municipio | UF | CEP |
|---:|---|---|---|---|---|
| 1 | Edificio Sede | SAS Quadra 1, Bloco D, Praca dos Tribunais Superiores | Brasilia | DF | 70.097-900 |
| 2 | Foro de Brasilia | SEPN 513, Bloco B, Lotes 2/3 | Brasilia | DF | 70.760-522 |
| 3 | Foro de Taguatinga | Quadra C12, Bloco O, Lotes 1 a 5 e 8 a 12 | Taguatinga | DF | 72.010-120 |
| 4 | Vara do Gama | Area Especial 01, Praca 02, Lote 06 | Gama | DF | 72.405-610 |
| 5 | Foro de Araguaina | Av. Neief Murad, 1131, Jardim Goias | Araguaina | TO | 77.824-022 |
| 6 | Foro de Palmas | Quadra 302 Norte, Conjunto QI 12, Alameda 2, Lote IA | Palmas | TO | 77.066-338 |
| 7 | Vara de Gurupi | Rua Antonio Lisboa da Cruz, 2031, Centro, Setor Central | Gurupi | TO | 77.405-100 |
| 8 | Vara de Dianopolis | Avenida Wolney Filho, Qd. 69 A, Setor Novo Horizonte | Dianopolis | TO | 77.300-000 |
| 9 | Vara de Guarai | Avenida Araguaia, esquina com Av. Bernardo Sayao, 1360 | Guarai | TO | 77.700-000 |
| 10 | Predio de Apoio | SGAN 916 Norte, Lote AI, Asa Norte | Brasilia | DF | 70.790-160 |

O Foro de Brasilia, alem de unidade beneficiada como localidade de atendimento, passa a ter papel tecnico adicional como ponto de redundancia da Sede, ambiente de replicacao e concentrador contingencial para acesso das unidades, condicionado ao projeto executivo de roteamento, seguranca, capacidade e continuidade.

### 2.4 Consequencias do nao atendimento da demanda

- Permanencia de maior dependencia da SD-WAN como unica camada estruturada de interconexao corporativa.
- Menor previsibilidade para trafego critico em cenarios de degradacao dos enlaces de Internet.
- Dificuldade de concentrar politicas de seguranca, monitoramento, filtragem e controle de trafego na Sede.
- Risco de indisponibilidade ou degradacao de acesso a sistemas judiciais e administrativos.
- Menor resiliencia para rotas de contingencia, suporte, replicacao, autenticacao e servicos institucionais.
- Dificuldade de evoluir para arquitetura com saida de Internet preferencial centralizada na Sede, uso de 3 saidas redundantes e separacao logica entre trafego critico e trafego de Internet.
- Risco de descumprimento de diretrizes de governanca de TIC relativas a disponibilidade, capacidade, seguranca e continuidade.

## 3. Descricao Sucinta do Objeto

### 3.1 Objeto da contratacao

Contratacao de empresa especializada para prestacao de servicos continuados de comunicacao de dados por meio de rede MPLS, incluindo fornecimento, instalacao, configuracao, equipamentos necessarios, monitoramento, suporte tecnico, manutencao e garantia de niveis de servico, para interconexao das unidades do TRT10 a Sede e integracao operacional com a SD-WAN vigente.

A contratacao devera:

- interconectar todas as demais localidades a Sede por MPLS;
- manter compatibilidade com a topologia SD-WAN existente;
- permitir uso preferencial do MPLS para trafego critico e da SD-WAN para trafego de Internet;
- permitir contingencia cruzada, de modo que MPLS e SD-WAN possam transportar trafegos criticos ou de Internet em caso de indisponibilidade ou degradacao de uma das camadas;
- permitir roteamento controlado para saida de Internet preferencial pela Sede;
- integrar-se as redes JT, Infovia e demais redes institucionais conforme definicao tecnica do TRT10;
- possibilitar QoS, segregacao logica e priorizacao de trafego critico;
- contemplar suporte, monitoramento e relatorios mensais de disponibilidade;
- evitar especificacao por marca, fabricante ou modelo, salvo quando indispensavel e tecnicamente justificado em etapa posterior.

O objeto tambem contempla, em grupo especifico e tecnicamente segregado, link dedicado ponto-a-ponto de 25 Gbps entre o Edificio Sede e o Foro de Brasilia, por fibra optica, LAN-to-LAN, Metro Ethernet, clear channel, E-Line, E-LAN ou tecnologia equivalente, com banda simetrica, full duplex, baixa latencia, SLA, monitoramento e equipamentos em comodato ou fornecidos como parte do servico, destinado a replicacao, redundancia, continuidade e acesso contingencial das unidades.

## 4. Quantidade a Ser Contratada

### 4.1 Quantidade estimada por ano

| Item | Localidade | Capacidade SD-WAN atual recuperada dos documentos | Capacidade MPLS proposta para redundancia total | Quantidade | Unidade |
|---:|---|---:|---:|---:|---|
| 1 | Edificio Sede | 1 Gbps | 1 Gbps | 1 | mes |
| 2 | Foro de Brasilia | 1 Gbps | 1 Gbps | 1 | mes |
| 3 | Predio de Apoio | 500 Mbps | 500 Mbps | 1 | mes |
| 4 | Foro de Taguatinga | 500 Mbps | 500 Mbps | 1 | mes |
| 5 | Foro de Palmas | 500 Mbps | 500 Mbps | 1 | mes |
| 6 | Vara do Gama | 100 Mbps | 100 Mbps | 1 | mes |
| 7 | Foro de Araguaina | 100 Mbps | 100 Mbps | 1 | mes |
| 8 | Vara de Gurupi | 100 Mbps | 100 Mbps | 1 | mes |
| 9 | Vara de Dianopolis | 100 Mbps | 100 Mbps | 1 | mes |
| 10 | Vara de Guarai | 100 Mbps | 100 Mbps | 1 | mes |

Grupo especifico de interligacao dedicada Sede-Foro:

| Item | Enlace dedicado | Tecnologia / funcao | Capacidade | Quantidade | Unidade |
|---:|---|---|---:|---:|---|
| 11 | Edificio Sede ↔ Foro de Brasilia | Link dedicado ponto-a-ponto por fibra optica, LAN-to-LAN/Metro Ethernet ou equivalente; replicacao e redundancia da Sede | 25 Gbps | 1 | mes |

As capacidades MPLS propostas reproduzem as capacidades SD-WAN atualmente registradas para cada localidade, com a finalidade de assegurar redundancia total e eliminar contingencia apenas parcial. O dimensionamento devera ser validado por meio de analise de trafego, criticidade dos sistemas, simultaneidade, QoS, crescimento esperado, desempenho da SD-WAN atual, capacidade de processamento dos CPEs e pesquisa de mercado.

O enlace dedicado de 25 Gbps nao integra a malha MPLS das localidades. Ele constitui grupo proprio por possuir finalidade, escala, tecnologia, precificacao e requisitos de desempenho distintos: interligacao de alta capacidade entre dois pontos centrais, suporte a replicacao e possibilidade de o Foro assumir papel contingencial de concentrador.

### 4.2 A estimativa e baseada no historico demandado?

Sim. A estimativa considera o historico de contratacoes de comunicacao de dados do TRT10, notadamente:

- Contrato 131/2023, referente a Link IP dedicado com SD-WAN para 10 localidades, com vigencia inicial de 5 anos e possibilidade de prorrogacao;
- contratacoes anteriores de Internet com Anti-DDoS para Sede, Foro de Brasilia e Predio de Apoio;
- contratacao anterior de links de Internet para unidades do Tocantins;
- mencoes documentais a conectividade MPLS e Infovia como meios de redundancia e interconexao com a Sede.

## 5. Estimativa Preliminar do Valor da Contratacao

### 5.1 Valor estimado da contratacao

O valor oficial devera ser apurado pela area competente em pesquisa de precos formal. Para memoria preliminar, foram levantadas referencias publicas de contratacoes similares de MPLS, L2L ou rede privada corporativa, com capacidades de 100 Mbps, 500 Mbps e 1 Gbps. A amostra abaixo nao substitui a pesquisa formal do processo, pois os precos variam conforme localidade, interiorizacao, rota fisica, dupla abordagem, SLA, CPE/roteador, prazo contratual, volume de pontos e escopo de monitoramento.

Com base nas referencias localizadas, adota-se apenas como estimativa inicial:

| Capacidade | Quantidade TRT10 | Media mensal preliminar por link | Valor mensal preliminar | Valor anual preliminar |
|---:|---:|---:|---:|---:|
| 1 Gbps | 2 | R$ 2.390,14 | R$ 4.780,28 | R$ 57.363,36 |
| 500 Mbps | 3 | R$ 1.785,75 | R$ 5.357,25 | R$ 64.287,00 |
| 100 Mbps | 5 | R$ 1.588,60 | R$ 7.943,00 | R$ 95.316,00 |
| Total preliminar | 10 | - | R$ 18.080,53 | R$ 216.966,36 |

Para o grupo de link dedicado Sede-Foro de 25 Gbps, nao foram localizados nesta pesquisa preliminar tres itens PNCP exatamente com 25 Gbps e o mesmo escopo ponto-a-ponto. Foram localizadas, contudo, contratacoes PNCP/publicas compativeis por similaridade tecnica, envolvendo LAN-to-LAN, Metro Ethernet, fibra dedicada, links de 4 Gbps, 5 Gbps e 10 Gbps, alem de especificacoes publicas que aceitam interfaces 10/25Gbps SFP28. Como estimativa conservadora inicial, recomenda-se tratar o enlace de 25 Gbps como item de alta capacidade sujeito a cotacao formal. Para planejamento preliminar, adota-se faixa indicativa de R$ 30.000,00 a R$ 60.000,00 mensais, com ponto de partida de R$ 45.000,00 mensais, equivalente a R$ 540.000,00 anuais, ate que a pesquisa formal confirme valores para Brasilia/DF, dupla abordagem, SLA, baixa latencia, interfaces 25GbE e roteamento/seguranca exigidos.

O valor acima deve ser tratado como indicativo de ordem de grandeza e devera ser recalculado pela pesquisa de precos formal, preferencialmente com itens PNCP atuais, cotacoes diretas com fornecedores aptos a atender DF/TO, analise critica de outliers e demonstrativo de memoria de calculo.

### 5.2 Como se chegou ao valor preliminar?

Para fins de memoria inicial, os documentos anteriores registram valores historicos de contratos de comunicacao de dados e Internet, mas tais valores nao devem ser usados diretamente como orcamento atual sem atualizacao metodologica, comparacao de escopo, pesquisa de mercado e tratamento das diferencas entre Internet dedicada, SD-WAN e MPLS.

A pesquisa devera observar, no minimo:

- precos publicos de servicos MPLS ou redes privadas corporativas similares;
- capacidades por localidade;
- custos de instalacao, equipamentos e ativacao;
- prazo contratual pretendido;
- SLA exigido;
- eventual necessidade de rotas fisicas distintas, QoS, VRF, BGP/OSPF ou monitoramento.

Enquanto nao houver pesquisa formal, a estimativa de valor deve permanecer como pendencia de planejamento, sem prejuizo da continuidade da estruturacao tecnica do DFD, ETP e TR.

### 5.3 Referencias preliminares de precos por capacidade

Pesquisa realizada em 02/06/2026. A API oficial de consulta do PNCP apresentou instabilidade/erro de conexao nesta sessao; por isso, foram utilizadas paginas publicas, publicacoes oficiais, portais de transparencia e editais indexados que indicam publicacao ou origem PNCP quando disponivel. O PNCP, conforme pagina oficial de dados abertos, disponibiliza APIs publicas para consultar contratacoes, contratos, atas e itens sem cadastro, e o numero de controle PNCP deve ser confirmado na pesquisa formal final.

| Capacidade | Orgao / contratacao similar | Referencia localizada | Valor mensal unitario usado | Observacao de qualidade |
|---:|---|---|---:|---|
| 100 Mbps | Ministerio Publico do Estado do Rio Grande do Sul - Contrato 68/2024 | Circuito MPLS otico duplo com roteador - 100 Mbps | R$ 1.580,25 | Alta aderencia: MPLS otico com roteador, item mensal. Fonte de transparencia institucional. |
| 100 Mbps | Autarquia Municipal Transitar - Cascavel/PR | Link de dados MPLS 100 Mbps - mensalidade | R$ 761,56 | Aderente por tecnologia e mensalidade; contratacao anterior e localidade distinta. |
| 100 Mbps | Tribunal de Justica da Paraiba - PE 010/2019 | Link de transporte de dados MPLS 100 Mbps | R$ 2.425,00 | Aderente por objeto, mas anterior a Lei 14.133/2021; usar com cautela. |
| 500 Mbps | Ministerio Publico do Estado do Rio Grande do Sul - Contrato 68/2024 | Circuito MPLS otico duplo com roteador - 500 Mbps | R$ 3.687,25 | Alta aderencia: MPLS otico com roteador, item mensal. |
| 500 Mbps | Municipio de Glorinha/RS - processo administrativo 25.714/2025 | Conexao ponto a ponto L2L com transporte Ethernet/MPLS, 500 Mbps | R$ 1.550,00 | Aderente por transporte Ethernet/MPLS e banda garantida; escopo L2L municipal. |
| 500 Mbps | Municipio de Xanxere/SC - PE 0032/2024 | Link MPLS 500 MB | R$ 119,00 | Referencia publica de edital; valor e baixo e deve ser tratado como possivel outlier/escopo local. |
| 1 Gbps | Ministerio Publico do Estado do Rio Grande do Sul - Contrato 68/2024 | Circuito MPLS otico duplo com roteador - 1.000 Mbps | R$ 4.740,75 | Alta aderencia: MPLS otico com roteador, item mensal. |
| 1 Gbps | Municipio de Santa Maria/RS | Servicos de comunicacao de dados tecnologia MPLS 1 Gbps | R$ 1.429,68 | Aderente por capacidade e tecnologia; confirmar detalhamento do item na pesquisa formal. |
| 1 Gbps | Municipio de Xanxere/SC - PE 0032/2024 | Link MPLS 01 GB | R$ 1.000,00 | Referencia publica de edital; escopo municipal com grande volume de pontos. |

Fontes preliminares consultadas: Portal PNCP em Dados Abertos; Manual da API de Consultas PNCP; Portal de Transparencia do MPRS; Edital PE 0032/2024 de Xanxere/SC; publicacao de Glorinha/RS; documentos publicos de Santa Maria/RS, Cascavel/PR e TJPB.

### 5.3.1 Referencias preliminares para o grupo de link dedicado Sede-Foro 25 Gbps

Pesquisa realizada em 02/06/2026. Nao foram encontrados tres itens exatamente equivalentes a link dedicado ponto-a-ponto de 25 Gbps. As referencias abaixo sao compativeis por similaridade tecnica e devem ser usadas como indicios, nao como estimativa final.

| Referencia | Numero/identificador PNCP ou fonte | Objeto compativel | Valor informado | Uso na estimativa |
|---|---|---|---:|---|
| Municipio de Candeias/BA | PNCP-13830336000123-1-000051/2026 | Comunicacao de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra optica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos | R$ 950.560,00 | Similaridade por LAN-to-LAN, fibra dedicada, alta capacidade, rotas redundantes e equipamentos. |
| Municipio de Jaguariuna/SP | PNCP-46410866000171-1-000610/2024 | Link dedicado de acesso a Internet bidirecional e simetrico de 10 Gbps | R$ 4.705.844,00 | Similaridade por link dedicado 10 Gbps; escopo de Internet, nao ponto-a-ponto. |
| Municipio de Ubarana/SP | PNCP-65708786000141-1-000038/2026 | Rede LAN-to-LAN por fibra optica dedicada, capacidade agregada de ate 10 Gbps, ponto concentrador | R$ 184.400,00 | Similaridade por LAN-to-LAN, fibra dedicada e limite agregado de 10 Gbps. |
| TJPR | 77821841000194-1-000049/2025 | Dois links dedicados de 10 Gbps cada, BGP e Anti-DDoS, operadoras distintas | R$ 187.560,00 | Similaridade por 10 Gbps e redundancia; escopo de Internet/AS, nao replicacao ponto-a-ponto. |
| JFRS | 00508903000188-1-001162/2024 | Conexao LAN-to-LAN para interligar datacenter com datacenter externo, taxa de 5 Gbps | R$ 72.000,00 | Alta similaridade funcional por interligacao de datacenters e LAN-to-LAN; capacidade inferior. |

Tambem foi localizada especificacao federal de modernizacao de rede que admite interfaces de 10/25Gbps SFP28, indicando aderencia de mercado para portas 25GbE em equipamentos de rede corporativa. Essa referencia apoia a viabilidade tecnica do enlace, mas nao serve como preco mensal de servico de telecomunicacoes.

### 5.4 Contratacoes similares a detalhar na pesquisa

Para subsidiar o ETP, o TR, a pesquisa de precos, a definicao de SLA e a validacao das especificacoes tecnicas, deverao ser priorizadas contratacoes que possuam maior similaridade com a arquitetura pretendida pelo TRT10. A similaridade devera considerar: uso de MPLS, L3VPN, L2L ou rede privada corporativa; interligacao de multiplas unidades a ponto concentrador; fibra optica; CPE ou roteador incluso; monitoramento; suporte; disponibilidade; e capacidades proximas a 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps e 1 Gbps.

Como referencias principais, recomenda-se detalhar:

| Prioridade | Contratacao/produto similar | Motivo da similaridade | Informacoes a buscar |
|---:|---|---|---|
| 1 | Solucao de Rede Privada Virtual MPLS sobre Fibra Optica para interligacao de 45 pontos | Rede privada, multiplos pontos, fibra optica e interligacao institucional | TR, ETP, SLA, matriz de riscos, precos por ponto, CPE, concentrador e monitoramento |
| 2 | Redes Privadas LAN-to-LAN ou MPLS entre Data Center Municipal e unidades remotas | Topologia semelhante a hub-and-spoke, com concentrador e unidades remotas | Arquitetura, aceite, disponibilidade, roteamento, suporte e valores mensais |
| 3 | Servico de Link de Comunicacao Multimidia Concentrador L3VPN/MPLS, 3 Gbps | Comparavel ao papel da Sede como concentrador | Requisitos do concentrador, SLA, QoS, roteamento, suporte e preco do link central |
| 4 | Servicos de Link de Comunicacao Multimidia L3VPN/MPLS de 100 Mbps, 200 Mbps e 400 Mbps | Comparavel aos circuitos das unidades | Preco mensal por capacidade, instalacao, CPE, SLA e prazo de reparo |
| 5 | Circuitos MPLS oticos com roteador, simples e duplos, em 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps e 1 Gbps | Aderente a capacidades propostas e a exigencia de equipamento gerenciado | Diferenca de preco entre circuito simples e duplo, instalacao, roteador e disponibilidade |
| 6 | Servico de acesso link de dados com tecnologia MPLS Capital/Interior, 50 Mbps a 1 Gbps, por 60 meses | Permite comparar capital/interior, prazo e velocidades proximas | Planilha de itens, valores unitarios, vigencia, reajuste, SLA e suporte |
| 7 | Rede MPLS ou superior / SD-WAN Interior | Alta aderencia por envolver MPLS e SD-WAN | Justificativa da arquitetura hibrida, failover, roteamento, SLA e precos |

Como referencias secundarias, poderao ser analisadas contratacoes de transporte IP com fibra optica, suporte a tunelamento, VLANs, roteamento TCP/IP e MPLS; redes IP multisservicos com operacao, manutencao e monitoramento; servicos MPLS/L2L; e links dedicados com MPLS ou EAPS e dupla abordagem. Essas referencias sao uteis para requisitos tecnicos e disponibilidade, mas devem ser avaliadas com cautela quando nao houver rede privada corporativa completa ou quando o objeto principal for apenas Internet.

Para a comparacao das alternativas do ETP, deverao ser buscadas referencias de links satelitais e de links comuns de Internet com VPN ponto a ponto. Essas referencias servirao para justificar a rejeicao ou classificacao secundaria das Solucoes 2 e 3, especialmente quanto a latencia, previsibilidade, SLA, superficie de exposicao, custo operacional e aderencia a trafego critico.

Nao devem ser usados como referencia principal de precos da presente contratacao itens de aquisicao de switches, roteadores avulsos, telefonia IP, web server, integracao de sistemas, instalacao de rede local, fusao de fibra ou manutencao de equipamentos, pois tais objetos nao representam servico continuado de rede privada corporativa interligando unidades a Sede.

## 6. Data Pretendida para Conclusao da Contratacao

### 6.1 Data de inicio de vigencia

Sugere-se que a nova contratacao esteja vigente antes de qualquer marco de encerramento ou degradacao de contratos correlatos que sustentem a conectividade das unidades, observada a antecedencia minima para tramitacao dos artefatos de planejamento.

### 6.2 Trata-se de servico continuado?

Sim. Trata-se de servico continuado de comunicacao de dados, essencial para o funcionamento permanente das unidades do TRT10.

## 7. Grau de Prioridade da Contratacao

### 7.1 Tabela de identificacao do grau de prioridade

| Criterio | Marcacao sugerida | Justificativa |
|---|---|---|
| Impacto se nao atendida | Grave | Pode afetar disponibilidade, desempenho, contingencia e seguranca da comunicacao institucional. |
| Urgencia | Nao e urgente, mas precisa ser realizada o mais rapido possivel | Ha necessidade de planejamento, pesquisa de precos, implantacao e operacao assistida, evitando solucao de continuidade. |
| Tendencia do problema | Ira piorar | A demanda por trafego corporativo, seguranca centralizada e continuidade tende a crescer. |

## 8. Vinculacao ou Dependencia com Outra Demanda

A demanda possui vinculacao tecnica com:

- contrato SD-WAN vigente, objeto do processo SEI 0000030-87.2023.5.10.8000;
- contratos de Internet e Anti-DDoS da Sede e demais unidades;
- redes JT, Infovia e arquitetura de seguranca perimetral;
- projeto de centralizacao de saida de Internet na Sede, considerando 3 saidas redundantes.

## 9. Objetivo Estrategico

A contratacao se alinha ao objetivo estrategico de aprimorar a Governanca de TIC e a protecao de dados, contribuindo para disponibilidade, continuidade, seguranca, monitoramento e desempenho dos servicos digitais do TRT10.

## 10. Informacoes SIGEO

### 10.1 Processo administrativo da contratacao em vigor

Processos de referencia historica: SEI 0000030-87.2023.5.10.8000, SEI 0007608-72.2021.5.10.8000 e SEI 0002027-76.2021.5.10.8000.

### 10.2 Contrato ou ARP em vigor

Contrato 131/2023 relacionado a Link IP dedicado com SD-WAN. Contratos anteriores de Internet/Anti-DDoS e links das unidades devem ser conferidos pela area de contratos para atualizacao de vigencia e numero no SIGEO.

### 10.3 Item SIGEO

A informar pela area competente.

### 10.4 Estimativa para 12 meses no SIGEO

A informar apos pesquisa de precos.

## 11. Servidor Responsavel pela Demanda

**Nome:** Edson Mateus de Sousa - Coordenador da CDTEC  
**E-mail funcional:** cdtec@trt10.jus.br  
**Telefone:** (61) 3348-1249 / 1288 / 1280 / 1188

## 12. Figura 1 - Arquitetura Proposta SD-WAN + MPLS + Link Dedicado Sede-Foro

![Figura 1 - Arquitetura proposta SD-WAN + MPLS + link dedicado Sede-Foro 25 Gbps](../diagrama_topologia_revisada.png)
