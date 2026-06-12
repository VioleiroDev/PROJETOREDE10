# CADERNO DE ANEXOS DO TERMO DE REFERENCIA

**Objeto:** Contratacao de servicos continuados de comunicacao de dados por MPLS para interconexao das unidades do TRT10 a Sede, em arquitetura integrada com a SD-WAN atual.  
**Orgao:** Tribunal Regional do Trabalho da 10a Regiao - TRT10  
**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC  
**Versao:** Minuta tecnica preliminar  
**Data:** 21/05/2026

## Registro de Evidencias e Premissas

A base local da skill etp-nagem-v2 retornou apenas precedente generico de Termo de Referencia, com numeroControlePNCP 83102335000148-1-000005/2023, sem orgao, ano, dominio tecnologico, subdominio ou cluster de solucao preenchidos. Por essa razao, os anexos abaixo devem ser tratados como minuta tecnica e hipotese de trabalho, a ser validada pela pesquisa de mercado, area tecnica, area de contratos e assessoria juridica.

As premissas tecnicas adotadas sao:

- a infraestrutura de Internet/borda da Sede e mantida por contratos existentes/correlatos e nao integra o objeto desta contratacao;
- a SD-WAN atual sera preservada e utilizada preferencialmente para trafego de Internet;
- o MPLS sera utilizado preferencialmente para trafego critico, institucional e corporativo interno;
- MPLS e SD-WAN deverao permitir contingencia cruzada, transportando qualquer classe de trafego em caso de indisponibilidade ou degradacao relevante de uma das camadas;
- todas as demais localidades deverao ser interconectadas a Sede por MPLS;
- as capacidades indicadas sao preliminares e dependem de validacao por medicao de trafego e pesquisa de precos.

## Anexo I - Arquitetura Tecnica da Solucao

### 1. Objetivo

Este anexo descreve a arquitetura tecnica pretendida para a solucao de rede privada corporativa integrada a SD-WAN, com foco em disponibilidade, continuidade operacional, seguranca, governanca de trafego, monitoramento e previsibilidade para sistemas criticos.

### 2. Visao de arquitetura

A arquitetura devera operar em modelo hub-and-spoke, com a Sede como concentrador preferencial da rede privada MPLS e da saida de Internet. As unidades remotas deverao possuir circuito MPLS para a Sede e manter a conectividade SD-WAN vigente. O roteamento devera priorizar o MPLS para trafego critico e a SD-WAN para trafego de Internet, preservando a possibilidade de contingencia cruzada.

![Figura 1 - Arquitetura proposta SD-WAN + MPLS](../diagrama_topologia_revisada.png)

### 3. Papeis das camadas de conectividade

| Camada | Uso preferencial | Uso em contingencia | Observacoes |
|---|---|---|---|
| MPLS | Sistemas criticos, autenticacao, servicos internos, integracoes institucionais, administracao e monitoramento | Trafego de Internet quando a SD-WAN estiver indisponivel ou degradada | Deve suportar QoS, isolamento logico, roteamento controlado e SLA mensuravel |
| SD-WAN | Trafego de Internet e acesso a servicos externos | Trafego critico quando o MPLS estiver indisponivel ou degradado | Permanece como contrato correlato e deve ser integrada ao projeto executivo |
| Infraestrutura de Internet da Sede | Egressao, seguranca, filtragem e observabilidade por contratos existentes/correlatos | Interoperabilidade com MPLS e SD-WAN | Fora do escopo desta contratacao |

### 4. Fluxos de trafego

| Fluxo | Caminho preferencial | Caminho alternativo | Responsabilidade de politica |
|---|---|---|---|
| Unidade para sistemas internos na Sede | MPLS | SD-WAN | CDTEC, com apoio da contratada |
| Unidade para redes institucionais externas integradas a Sede | MPLS | SD-WAN | CDTEC, com apoio da contratada |
| Unidade para Internet | SD-WAN | MPLS via Sede | CDTEC |
| Sede para unidades | MPLS | SD-WAN | CDTEC, com apoio da contratada |
| Monitoramento e administracao | MPLS | SD-WAN | CDTEC |

### 5. Principios de desenho

- Evitar dependencia exclusiva de uma unica tecnologia de transporte.
- Separar fluxos criticos e fluxos de Internet por politica de roteamento.
- Centralizar seguranca e observabilidade na Sede sempre que tecnicamente adequado.
- Garantir retorno controlado ao caminho preferencial apos evento de contingencia.
- Manter compatibilidade com os ativos, firewalls, roteadores e controladores SD-WAN existentes.
- Evitar especificacao por marca, modelo ou fabricante.

## Anexo II - Localidades, Capacidades e Escopo dos Circuitos

### 1. Localidades abrangidas

| Item | Localidade | UF | Capacidade minima MPLS proposta | Papel na topologia |
|---:|---|---|---:|---|
| 1 | Edificio Sede | DF | 1 Gbps | Concentrador preferencial |
| 2 | Foro de Brasilia | DF | 1 Gbps | Unidade de alta demanda |
| 3 | Predio de Apoio | DF | 200 Mbps | Unidade metropolitana |
| 4 | Foro de Taguatinga | DF | 200 Mbps | Unidade regional DF |
| 5 | Foro de Palmas | TO | 200 Mbps | Polo regional TO |
| 6 | Vara do Gama | DF | 50 Mbps | Unidade remota |
| 7 | Foro de Araguaina | TO | 50 Mbps | Unidade remota |
| 8 | Vara de Gurupi | TO | 50 Mbps | Unidade remota |
| 9 | Vara de Dianopolis | TO | 50 Mbps | Unidade remota |
| 10 | Vara de Guarai | TO | 50 Mbps | Unidade remota |

### 2. Escopo minimo por circuito

Cada circuito devera contemplar:

- acesso fisico ou logico necessario a prestacao do servico;
- CPE ou equipamento equivalente, quando necessario;
- instalacao, configuracao, ativacao e testes;
- enderecamento e roteamento conforme projeto executivo;
- monitoramento 24x7;
- suporte tecnico e manutencao;
- relatorio mensal de desempenho e disponibilidade;
- documentacao as built.

### 3. Capacidades

As capacidades indicadas sao hipoteses de trabalho. A versao final devera ser confirmada por:

- medicao de trafego atual da SD-WAN por localidade;
- avaliacao de simultaneidade de usuarios e sistemas;
- volume de trafego critico;
- crescimento esperado;
- criticidade operacional da localidade;
- pesquisa de mercado e disponibilidade de atendimento.

## Anexo III - Requisitos Tecnicos Detalhados

### 1. Rede privada e isolamento

A solucao devera prover rede privada corporativa por MPLS L3 VPN ou tecnologia equivalente, desde que atenda aos requisitos de isolamento logico, roteamento controlado, suporte a QoS, monitoramento e SLA. Quando utilizada tecnologia equivalente, a licitante devera demonstrar que a solucao entrega resultado funcional equivalente ao MPLS pretendido.

### 2. Roteamento

O projeto executivo devera definir, no minimo:

- protocolos de roteamento utilizados, preferencialmente BGP ou OSPF, ou justificativa para uso de roteamento estatico;
- redes anunciadas por localidade;
- metricas, prioridades e preferencias de caminho;
- politica de failover entre MPLS e SD-WAN;
- politica de retorno ao caminho preferencial;
- tratamento de rotas default;
- prevencao de loops;
- matriz de responsabilidades por configuracao.

### 3. QoS

A solucao devera suportar, no minimo, quatro classes logicas de servico, ajustaveis no projeto executivo:

| Classe | Uso previsto | Prioridade sugerida | Observacao |
|---|---|---|---|
| Critica | Sistemas judiciais, autenticacao, servicos internos essenciais e administracao | Alta | Deve ter tratamento preferencial no MPLS |
| Tempo real | Voz, video e colaboracao, quando aplicavel | Alta ou media | Depende de validacao da CDTEC |
| Corporativa | Sistemas administrativos e integracoes institucionais | Media | Trafego institucional regular |
| Melhor esforco | Atualizacoes, navegacao e trafego nao critico | Baixa | Pode usar preferencialmente SD-WAN/Internet |

As marcacoes DSCP, percentuais de reserva, filas e politicas de descarte deverao ser definidos no projeto executivo, sem impor marca ou fabricante especifico.

### 4. Seguranca

A contratada devera:

- manter sigilo sobre informacoes de topologia, enderecamento, rotas e configuracoes;
- restringir acessos administrativos aos equipamentos sob sua responsabilidade;
- registrar alteracoes relevantes;
- comunicar incidentes de seguranca que afetem a prestacao do servico;
- preservar isolamento logico do trafego do TRT10;
- nao compartilhar configuracoes sensiveis com terceiros nao autorizados;
- apoiar a CDTEC na analise de eventos de indisponibilidade ou degradacao.

### 5. Equipamentos e licencas

Todos os equipamentos, modulos, licencas, fontes, cabos, transceptores, suportes e demais elementos necessarios a prestacao do servico deverao ser fornecidos pela contratada, salvo itens expressamente indicados como responsabilidade do TRT10 no projeto executivo.

## Anexo IV - Implantacao, Migracao e Rollback

### 1. Plano de implantacao

A contratada devera apresentar plano de implantacao em ate 10 dias uteis apos a assinatura do contrato ou emissao da ordem de servico, contendo:

- cronograma por localidade;
- responsaveis tecnicos;
- prerequisitos de infraestrutura;
- janelas de intervencao;
- atividades de instalacao;
- testes previstos;
- riscos da implantacao;
- plano de comunicacao;
- plano de rollback.

### 2. Fases sugeridas

| Fase | Escopo | Resultado esperado |
|---:|---|---|
| 1 | Sede | Concentrador MPLS ativado, rotas base validadas e monitoramento habilitado |
| 2 | Foro de Brasilia, Predio de Apoio, Taguatinga e Palmas | Unidades de maior capacidade ativadas e integradas |
| 3 | Gama, Araguaina, Gurupi, Dianopolis e Guarai | Unidades remotas ativadas |
| 4 | Operacao assistida | Testes de estabilidade, QoS, failover, relatorios e saneamento de pendencias |

### 3. Criterios de janela de mudanca

Intervencoes com risco de indisponibilidade deverao ser previamente aprovadas pela CDTEC. A solicitacao de janela devera informar:

- localidade afetada;
- data e horario pretendidos;
- atividades previstas;
- impacto esperado;
- tempo maximo de indisponibilidade;
- responsaveis;
- criterio de sucesso;
- criterio de rollback.

### 4. Rollback

O rollback devera ser acionado quando houver falha de conectividade, perda de acesso a sistemas criticos, degradacao severa, falha de roteamento ou qualquer condicao definida pela CDTEC como impeditiva de continuidade da mudanca. O plano devera indicar os passos para retorno ao estado anterior e os registros que deverao ser preservados.

## Anexo V - Plano de Testes e Aceite

### 1. Testes minimos por localidade

| Teste | Evidencia esperada | Resultado |
|---|---|---|
| Identificacao do circuito | Designacao do circuito e localidade | Obrigatorio |
| Banda contratada | Teste ou evidencia tecnica compativel com a capacidade contratada | Obrigatorio |
| Conectividade com a Sede | Ping, traceroute ou teste equivalente | Obrigatorio |
| Roteamento | Rotas e caminhos conforme projeto executivo | Obrigatorio |
| Acesso a servicos institucionais | Validacao pela CDTEC | Obrigatorio |
| Monitoramento | Circuito visivel em ferramenta ou portal | Obrigatorio |
| Chamado teste | Protocolo aberto e encerrado | Obrigatorio |
| Medicao de latencia e perda | Relatorio inicial de desempenho | Obrigatorio |
| Failover MPLS para SD-WAN | Evidencia de continuidade, quando tecnicamente aplicavel | Obrigatorio para aceite final da arquitetura |
| Failover SD-WAN para MPLS | Evidencia de continuidade, quando tecnicamente aplicavel | Obrigatorio para aceite final da arquitetura |
| Retorno ao caminho preferencial | Evidencia de reconvergencia controlada | Obrigatorio |
| Documentacao as built | Documento entregue e validado | Obrigatorio |

### 2. Aceite provisorio

O aceite provisorio por localidade podera ocorrer apos a ativacao do circuito, validacao de conectividade, registro no monitoramento, teste de chamado e entrega da documentacao minima da localidade.

### 3. Aceite definitivo

O aceite definitivo devera ocorrer apos periodo de observacao e saneamento das pendencias identificadas. A duracao do periodo de observacao devera ser definida no TR final ou na ordem de servico, conforme criticidade e cronograma.

### 4. Pendencias de aceite

As pendencias deverao ser classificadas como:

| Classe | Descricao | Efeito no aceite |
|---|---|---|
| Bloqueante | Impede uso do circuito ou causa indisponibilidade relevante | Impede aceite |
| Critica | Afeta funcao essencial, SLA, roteamento ou seguranca | Pode impedir aceite definitivo |
| Menor | Nao impede uso, mas exige correcao documentada | Pode permitir aceite com ressalva |

## Anexo VI - Niveis de Servico, Medicao e Glosas

### 1. Indicadores minimos

| Indicador | Meta sugerida | Forma de afericao |
|---|---:|---|
| Disponibilidade Sede | 99,90% mensal | Relatorio da contratada e validacao da fiscalizacao |
| Disponibilidade demais localidades | 99,70% mensal | Relatorio da contratada e validacao da fiscalizacao |
| Inicio de atendimento para incidente critico | ate 2 horas | Registro de chamado |
| Prazo de reparo critico | ate 8 horas, salvo justificativa aceita pela fiscalizacao | Registro de chamado |
| Entrega do relatorio mensal | ate o 5o dia util do mes subsequente | Entrega documental |
| Latencia, perda e jitter | A definir no TR final por localidade/regiao | Medicoes automatizadas |

As metas de latencia, perda de pacotes e jitter devem ser definidas apos pesquisa de mercado e validacao tecnica, para evitar exigencia inexequivel ou insuficiente.

### 2. Formula de disponibilidade

`D = [(To - Ti) / To] x 100`

Onde:

- `D` representa a disponibilidade mensal;
- `To` representa o total de minutos do periodo de apuracao;
- `Ti` representa o tempo de indisponibilidade imputavel a contratada.

### 3. Eventos desconsideraveis

Somente poderao ser desconsiderados do calculo:

- manutencoes programadas previamente aprovadas pela CDTEC;
- falhas comprovadamente causadas por infraestrutura interna do TRT10 fora da responsabilidade da contratada;
- eventos de forca maior devidamente comprovados;
- periodos em que a indisponibilidade decorra de ordem expressa do TRT10.

### 4. Glosa por indisponibilidade

Como hipotese de trabalho, a glosa podera ser proporcional ao valor mensal do circuito afetado:

`Vd = V x [1 - (D / 100)]`

Onde:

- `Vd` representa o valor de desconto;
- `V` representa o valor mensal do circuito afetado;
- `D` representa a disponibilidade mensal apurada.

O TR final podera estabelecer glosas adicionais por atraso de implantacao, ausencia de relatorio, descumprimento de prazo de atendimento ou reincidencia.

## Anexo VII - Matriz de Riscos

| Risco | Causa provavel | Probabilidade | Impacto | Mitigacao | Responsavel sugerido |
|---|---|---|---|---|---|
| Pesquisa de precos insuficiente | Baixa disponibilidade de referencias comparaveis | Media | Alto | Coletar propostas, contratações similares e memoria de calculo | Equipe de planejamento |
| Restricao indevida de competitividade | Exigencia excessivamente fechada para MPLS ou qualificacao tecnica | Media | Alto | Usar requisitos funcionais e aceitar tecnologia privada equivalente | Equipe de planejamento |
| Atraso na implantacao | Dependencia de infraestrutura local ou operadora | Media | Alto | Cronograma por fases, plano de implantacao e glosa por atraso | Contratada |
| Capacidade insuficiente | Dimensionamento sem medicao real de trafego | Media | Medio | Medir uso atual, prever upgrade e acompanhar percentil de utilizacao | CDTEC |
| Capacidade superdimensionada | Ausencia de estudo de demanda | Media | Medio | Validar demanda por localidade e comparar alternativas | CDTEC |
| Falha de integracao MPLS/SD-WAN | Rotas, metricas ou politicas inconsistentes | Media | Alto | Projeto executivo, matriz de responsabilidade e testes de failover | Contratada e CDTEC |
| Indisponibilidade de circuito | Falha de backbone, acesso local ou CPE | Media | Alto | SLA, monitoramento, glosas e contingencia pela SD-WAN | Contratada |
| Falha comum em infraestrutura fisica | Mesma rota fisica ou dependencia local | Media | Alto | Rotas distintas quando viavel e planejamento de contingencia | Contratada |
| SLA sem afericao adequada | Relatorios insuficientes ou falta de validacao | Media | Medio | Relatorio padronizado e validacao pela fiscalizacao | Fiscalizacao tecnica |
| Dificuldade de troubleshooting | Multiplicidade de fornecedores | Media | Medio | Matriz RACI e canais de escalonamento | CDTEC |
| Incidente de seguranca | Exposicao de configuracoes ou acesso indevido | Baixa | Alto | Sigilo, controle de acesso, logs e comunicacao de incidentes | Contratada |
| Falta de dotacao ou PCA/SIGEO | Pendencia administrativa | Media | Alto | Confirmar item, estimativa e disponibilidade orcamentaria | Area administrativa |

## Anexo VIII - Modelo de Relatorio Mensal

### 1. Identificacao

| Campo | Conteudo esperado |
|---|---|
| Contrato | Numero do contrato |
| Competencia | Mes/ano |
| Contratada | Razao social |
| Gestor/fiscal | Nome do responsavel |
| Data de entrega | Data do relatorio |

### 2. Indicadores por circuito

| Localidade | Designacao do circuito | Capacidade | Disponibilidade | Indisponibilidade | Chamados | MTTR | Utilizacao pico | Observacoes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Sede | A informar | 1 Gbps | A informar | A informar | A informar | A informar | A informar | A informar |
| Foro de Brasilia | A informar | 1 Gbps | A informar | A informar | A informar | A informar | A informar | A informar |
| Demais localidades | A informar | Conforme contrato | A informar | A informar | A informar | A informar | A informar | A informar |

### 3. Incidentes

Cada incidente devera conter:

- protocolo;
- localidade;
- data e hora de abertura;
- data e hora de inicio de atendimento;
- data e hora de normalizacao;
- severidade;
- causa raiz;
- acao corretiva;
- impacto percebido;
- indicacao de glosa, quando aplicavel.

### 4. Manutencoes programadas

Informar todas as manutencoes programadas, aprovadas ou rejeitadas, com data, janela, localidade, impacto, responsavel e resultado.

### 5. Eventos de contingencia

O relatorio devera indicar eventos de failover, uso de caminho alternativo, retorno ao caminho preferencial e qualquer degradacao relevante entre MPLS e SD-WAN, quando identificavel pela contratada.

## Anexo IX - Modelo de Pesquisa de Precos e Comparacao de Alternativas

### 1. Objetivo

Este anexo orienta a coleta de informacoes para comparar a Solucao 1, Solucao 2 e Solucao 3 avaliadas no ETP, sem substituir a pesquisa formal conduzida pela area competente.

### 2. Alternativas a comparar

| Alternativa | Descricao | Dados minimos a coletar |
|---|---|---|
| Solucao 1 - MPLS integrado a SD-WAN | MPLS para trafego critico e SD-WAN para Internet, com contingencia cruzada | Preco por circuito, instalacao, CPE, SLA, latencia, suporte, prazo de implantacao, upgrade |
| Solucao 2 - Links satelitais | Enlaces satelitais para funcao equivalente ou contingencia | Preco por Mbps, latencia, franquia, disponibilidade, restricoes tecnicas, antena/equipamentos |
| Solucao 3 - Internet com VPN ponto a ponto | Links comuns de Internet com tuneis VPN | Preco por link, IP fixo, banda garantida, suporte, disponibilidade, custo operacional de VPN |

### 3. Criterios qualitativos

| Criterio | Peso sugerido | Observacao |
|---|---:|---|
| Disponibilidade e SLA | Alto | Essencial para atividade jurisdicional e administrativa |
| Previsibilidade de desempenho | Alto | Relevante para sistemas criticos |
| Seguranca e isolamento | Alto | Importante para trafego institucional |
| Custo total | Alto | Deve considerar mensalidade, instalacao, equipamentos e operacao |
| Complexidade operacional | Medio | Considerar troubleshooting, monitoramento e suporte |
| Prazo de implantacao | Medio | Relevante para continuidade contratual |
| Expansibilidade | Medio | Considerar aumento de banda e novas unidades |

### 4. Pendencias para pesquisa final

- Definir periodo de vigencia considerado na comparacao.
- Confirmar se instalacao e equipamentos serao cobrados separadamente.
- Coletar evidencias de mercado suficientes para cada alternativa.
- Registrar premissas de atualizacao de valores.
- Justificar eventual nao comparacao de alternativa por inviabilidade tecnica ou ausencia de fornecedores.
