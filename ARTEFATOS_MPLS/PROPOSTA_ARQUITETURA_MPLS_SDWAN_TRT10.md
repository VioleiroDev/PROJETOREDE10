# PROPOSTA TECNICA DE ARQUITETURA DE REDE

**Objeto:** arquitetura hibrida de comunicacao de dados do TRT10 com preservacao da SD-WAN atual e implantacao complementar de MPLS.  
**Orgao:** Tribunal Regional do Trabalho da 10a Regiao - TRT10  
**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC  
**Processo de referencia:** SEI 0009785-67.2025.5.10.8000  
**Versao:** proposta de arquitetura melhorada  
**Data:** 23/05/2026

## 1. Sintese Executiva

A arquitetura proposta organiza a conectividade do TRT10 em camadas complementares, preservando a SD-WAN ja implantada e acrescentando uma camada privada MPLS para trafego institucional critico. A Sede passa a ser tratada como hub preferencial de seguranca, saida de Internet, integracao com redes institucionais, observabilidade e contingencia controlada.

O desenho recomendado nao substitui a SD-WAN existente. Ao contrario, aproveita os enlaces e a capacidade ja contratados, reduzindo retrabalho, preservando investimento e permitindo evolucao gradual. O MPLS entra como camada complementar, de menor capacidade relativa, orientada a previsibilidade, isolamento logico, QoS e continuidade dos fluxos mais sensiveis.

A melhoria principal esta na separacao explicita de funcoes:

- SD-WAN como transporte preferencial para Internet, servicos externos e continuidade operacional;
- MPLS como transporte preferencial para sistemas criticos, servicos internos, autenticacao, redes institucionais e trafego sensivel;
- Sede como ponto de concentracao de politicas, seguranca, saida de Internet, monitoramento e integracao;
- contingencia cruzada entre MPLS e SD-WAN, com criterios objetivos de acionamento, registro e retorno ao caminho preferencial.

![Figura 1 - Arquitetura-alvo em camadas](../IMAGENS_PROPOSTA_ARQUITETURA/01_arquitetura_alvo_camadas.png)

## 2. Principios de Arquitetura

A arquitetura deve ser orientada por principios de segmentacao, redundancia, governanca e mensurabilidade. Esses principios reduzem a dependencia de uma unica tecnologia e tornam a fiscalizacao contratual mais objetiva.

### 2.1 Separacao de camadas

A SD-WAN e o MPLS devem ser tratados como camadas logicas distintas, cada uma com papel preferencial definido. Essa separacao evita que todos os fluxos concorram pelo mesmo caminho e permite aplicar politicas diferentes para Internet, sistemas criticos, voz, video, administracao, monitoramento e replicacao.

### 2.2 Hub controlado na Sede

A Sede deve operar como concentrador preferencial, pois reune as saidas redundantes de Internet, os controles de seguranca, as integracoes com redes institucionais e os mecanismos de observabilidade. Esse papel de hub deve ser acompanhado de capacidade adequada, redundancia de borda, firewall em alta disponibilidade, politicas de roteamento e monitoramento permanente.

### 2.3 Contingencia cruzada com retorno controlado

O failover entre SD-WAN e MPLS deve ser tratado como politica de arquitetura, nao como comportamento improvisado. Para cada classe de trafego, o projeto executivo deve definir caminho preferencial, caminho alternativo, gatilho de mudanca, tempo esperado de convergencia, forma de registro e criterio de retorno.

### 2.4 Evidencias tecnicas para fiscalizacao

Disponibilidade, latencia, jitter, perda, eventos de failover, chamados, causa raiz e relatorios mensais devem formar a base de fiscalizacao do contrato. A arquitetura deve produzir evidencias verificaveis, permitindo correlacionar degradacao, indisponibilidade, glosas e medidas corretivas.

## 3. Desenho Logico Recomendado

O desenho logico recomendado organiza as unidades em torno da Sede, mantendo os enlaces SD-WAN atuais como base operacional e implantando MPLS complementar para todas as localidades. A Sede devera concentrar a egressao preferencial de Internet, com 3 saidas redundantes, preferencialmente contratadas com operadoras e rotas fisicas distintas.

Em operacao normal, o trafego de Internet e servicos externos deve seguir preferencialmente pela SD-WAN, com saida centralizada pela Sede sempre que tecnicamente aplicavel. O trafego critico e institucional deve seguir preferencialmente pelo MPLS, aproveitando isolamento logico, QoS, roteamento controlado e SLA.

Em cenarios de falha, degradacao ou manutencao, a arquitetura deve permitir que a SD-WAN transporte trafego critico e que o MPLS transporte trafego de Internet por egressao centralizada, observada a politica de degradacao controlada. Essa flexibilidade aumenta a continuidade sem eliminar a disciplina de rotas preferenciais.

## 4. Fluxos de Trafego e Contingencia

A arquitetura deve classificar o trafego em grupos operacionais, pois cada grupo possui sensibilidade diferente a disponibilidade, latencia, jitter, perda e seguranca. A classificacao inicial recomendada e:

| Classe | Exemplos | Caminho preferencial | Caminho alternativo | Observacao |
|---|---|---|---|---|
| Critico institucional | PJe, autenticacao, sistemas internos, redes JT, Infovia | MPLS | SD-WAN | Deve ter prioridade e monitoramento reforcado |
| Internet e SaaS | Web, colaboracao, servicos externos e nuvem | SD-WAN com egressao pela Sede | MPLS pela Sede | Saida local apenas por excecao documentada |
| Voz e video | Reunioes, telefonia, colaboracao sensivel a tempo | Caminho com melhor SLA medido | Caminho secundario por politica | Deve observar jitter, perda e latencia |
| Gerencia e monitoramento | CPE, roteadores, logs, NOC, SIEM, backup | Caminho dedicado ou priorizado | Caminho de contingencia | Deve permanecer acessivel em incidentes |

![Figura 2 - Fluxos de operacao, contingencia e retorno](../IMAGENS_PROPOSTA_ARQUITETURA/02_fluxos_operacao_contingencia.png)

O projeto executivo deve estabelecer gatilhos objetivos para acionamento de contingencia, tais como indisponibilidade do circuito, perda de rota, perda de pacotes acima do limite, latencia anormal, jitter elevado, falha de CPE, falha de firewall, degradacao de saida central ou indisponibilidade de servico institucional.

O retorno ao caminho preferencial deve ser controlado, com periodo minimo de estabilidade para evitar oscilacao. Recomenda-se que todo evento de mudanca de rota gere registro tecnico, correlacao com chamado, tempo de convergencia, causa raiz e indicacao de impacto percebido.

## 5. Segmentacao, Seguranca e Governanca

A solucao deve adotar segmentacao logica por VRF, classes de servico ou mecanismo equivalente. A segmentacao permite separar fluxos de usuarios, administracao, voz/video, servicos criticos, monitoramento, backup, replicacao e gerencia, reduzindo superficie de exposicao e melhorando a aplicacao de QoS.

As unidades devem operar com Internet local bloqueada ou restrita por padrao, salvo excecoes formalmente justificadas, controladas e auditaveis. A politica preferencial e encaminhar o trafego de Internet para a Sede, onde estarao os controles de seguranca, filtragem, logs e inspeção.

Na Sede, recomenda-se prever borda redundante, firewall em alta disponibilidade, roteamento controlado por BGP, OSPF ou desenho equivalente, QoS fim a fim, telemetria, logs centralizados e integracao com SIEM ou plataforma institucional equivalente.

![Figura 3 - Segmentacao, seguranca e governanca](../IMAGENS_PROPOSTA_ARQUITETURA/03_segmentacao_seguranca_governanca.png)

## 6. Requisitos Tecnicos a Consolidar no Projeto Executivo

O projeto executivo devera detalhar os elementos que transformam a arquitetura conceitual em solucao operavel:

- mapa de enderecamento, VRFs, rotas, prefixos anunciados e politicas de redistribuicao;
- definicao de BGP, OSPF ou roteamento estatico justificado, com metricas, prioridades e prevencao de loops;
- classes de QoS, marcacoes, filas, reservas, limites e politicas de descarte;
- criterios de failover e retorno por classe de trafego;
- arquitetura de borda da Sede, incluindo redundancia fisica e logica;
- integracao com firewalls, controladores SD-WAN, redes JT, Infovia, monitoramento e seguranca;
- padrao de documentacao as built e atualizacao apos mudancas;
- plano de testes de ativacao, contingencia, desempenho, seguranca e aceite;
- matriz de responsabilidades entre contratada, CDTEC, fiscalizacao e fornecedores correlatos.

## 7. Capacidade e Alta Disponibilidade

A capacidade combinada inicial de 4 Gbps para as 3 saidas de Internet da Sede deve ser tratada como premissa de planejamento, derivada da soma aproximada dos enlaces SD-WAN atuais. Essa premissa deve ser validada por medicoes reais, historico de uso, picos, simultaneidade, criticidade dos servicos, crescimento esperado e politica de degradacao em contingencia.

As 3 saidas de Internet da Sede devem, sempre que viavel, usar operadoras e rotas fisicas distintas. A diversidade de operadora sem diversidade de caminho fisico pode reduzir o beneficio de redundancia, especialmente em falhas de infraestrutura compartilhada.

Para a camada MPLS, as capacidades preliminares devem ser mantidas como referencia tecnica inicial e ajustadas conforme medicao de trafego critico por localidade:

| Localidade | SD-WAN atual | MPLS complementar proposto | Papel recomendado |
|---|---:|---:|---|
| Edificio Sede | 1 Gbps | 1 Gbps | Hub, seguranca, Internet, redes JT/Infovia e observabilidade |
| Foro de Brasilia | 1 Gbps | 1 Gbps | Unidade de alta demanda e contingencia reforcada |
| Predio de Apoio | 500 Mbps | 200 Mbps | Unidade metropolitana |
| Foro de Taguatinga | 500 Mbps | 200 Mbps | Unidade regional DF |
| Foro de Palmas | 500 Mbps | 200 Mbps | Polo regional TO |
| Vara do Gama | 100 Mbps | 50 Mbps | Unidade remota |
| Foro de Araguaina | 100 Mbps | 50 Mbps | Unidade remota |
| Vara de Gurupi | 100 Mbps | 50 Mbps | Unidade remota |
| Vara de Dianopolis | 100 Mbps | 50 Mbps | Unidade remota |
| Vara de Guarai | 100 Mbps | 50 Mbps | Unidade remota |

## 8. Operacao, Monitoramento e Aceite

A operacao deve ser acompanhada por indicadores mensuraveis e por relatorios periodicos. No minimo, a contratada deve fornecer dados de disponibilidade, indisponibilidade, chamados, tempos de atendimento e reparo, causa raiz, manutencoes programadas, latencia, perda, jitter, throughput, eventos de failover e retorno.

O aceite por localidade deve verificar conectividade com a Sede, banda contratada, roteamento conforme projeto, registro no monitoramento, abertura de chamado teste, medicao inicial de desempenho, teste de contingencia entre MPLS e SD-WAN e entrega de documentacao as built.

Recomenda-se periodo de operacao assistida apos ativacao de todas as localidades, com acompanhamento de estabilidade, ajustes de QoS, saneamento de pendencias, validacao de relatorios e simulacao de indisponibilidade controlada.

## 9. Evolucao Recomendada

A evolucao deve ocorrer em fases para reduzir risco operacional:

| Fase | Escopo | Resultado esperado |
|---:|---|---|
| 1 | Sede | Hub preparado com saidas centrais, borda, seguranca, roteamento e monitoramento |
| 2 | Gama e Taguatinga | Validacao inicial em unidades DF com sensibilidade operacional |
| 3 | Predio de Apoio, Foro de Brasilia e Palmas | Integracao das unidades de maior demanda |
| 4 | Araguaina, Gurupi, Dianopolis e Guarai | Conclusao da capilaridade MPLS nas unidades remotas |
| 5 | Operacao assistida | Validacao de failover, QoS, desempenho, relatorios e documentacao |

## 10. Conclusao Tecnica

A arquitetura melhorada preserva a SD-WAN existente, acrescenta MPLS como camada privada complementar e consolida a Sede como ponto preferencial de seguranca, Internet, redes institucionais e observabilidade. Esse desenho reduz dependencia de uma unica tecnologia, melhora previsibilidade para trafego critico, permite contingencia cruzada e cria base objetiva para fiscalizacao contratual.

A proposta deve ser confirmada por pesquisa de mercado, medicao real de trafego, validacao de capacidade por localidade, definicao de metas de desempenho, consolidacao do projeto executivo e alinhamento com contratos correlatos de SD-WAN, Internet, Anti-DDoS, Infovia, redes JT, firewalls e monitoramento.
