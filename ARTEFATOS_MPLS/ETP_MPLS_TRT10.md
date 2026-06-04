# ESTUDO TÉCNICO PRELIMINAR (ETP)

**Objeto:** Contratação de serviços continuados de comunicação de dados por MPLS, com capacidades equivalentes às capacidades dos enlaces SD-WAN vigentes em cada localidade, e contratação de grupo específico de link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, para replicação, redundância da Sede e arquitetura híbrida integrada com a SD-WAN vigente.

**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC

**Órgão:** Tribunal Regional do Trabalho da 10ª Região - TRT10

**Processo de referência:** SEI 0009785-67.2025.5.10.8000

**Versão:** Minuta técnica - arquitetura de redundância total MPLS/SD-WAN

**Data:** 02/06/2026

## Registro de Evidências e Premissas

### Fatos recuperados dos documentos anexados

- O modelo de ETP anexo estrutura o estudo em descrição da necessidade, alinhamento estratégico, requisitos, levantamento de mercado, descrição da solução, estimativas, justificativa de parcelamento, resultados esperados, providências prévias, contratações correlatas, impactos ambientais e posicionamento conclusivo.

- O processo SEI 0000030-87.2023.5.10.8000 registra contratação de link IP dedicado com SD-WAN para 10 localidades, com bandas de 1 Gbps na Sede e Foro de Brasília, 500 Mbps em Taguatinga, Palmas e Prédio de Apoio, e 100 Mbps nas demais localidades.

- O mesmo processo registra disponibilidade mínima de 99,90% para a Sede e 99,70% para as demais localidades, e vigência inicial de 5 anos.

- Contratações anteriores de Internet com Anti-DDoS registram a relevância de redundância, operadoras distintas, monitoramento, portal de chamados, glosas por indisponibilidade e teste de aceite.

- Documentos anteriores indicam que Foro de Brasília e Prédio de Apoio já se conectavam à Sede via MPLS e Infovia, evidenciando aderência histórica da arquitetura de concentração na Sede.

- O DFD do processo SEI 0009785-67.2025.5.10.8000 consolida a manutenção da topologia SD-WAN vigente e a contratação de MPLS, com capacidades equivalentes às capacidades SD-WAN por localidade, interconexão das unidades à Sede e saída de Internet preferencialmente centralizada na Sede.

- O DFD registra que a topologia SD-WAN vigente se baseia em enlaces dedicados, túneis IPSec, roteamento dinâmico OSPF e concentração em pontos centrais, devendo coexistir com os links MPLS durante e após a implantação.

- O DFD indica, como premissa a validar, que a Sede deverá dispor de 3 links de Internet redundantes, preferencialmente com operadoras e rotas físicas distintas, com capacidade combinada suficiente para suportar a agregação do tráfego das unidades.

- A demanda contempla grupo próprio de link dedicado ponto-a-ponto de 25 Gbps entre o Edifício Sede e o Foro de Brasília, distinto da rede MPLS, para replicação, redundância da Sede e uso do Foro como ponto contingencial de acesso das unidades.

- A base local da skill etp-nagem-v2 não retornou precedentes PNCP úteis para a busca "links MPLS / comunicação de dados / rede corporativa", razão pela qual esta minuta se apoia nos documentos anexos, em referências públicas externas e em inferências técnicas marcadas.

- Em 02/06/2026, foram levantadas referências públicas de contratações similares para capacidades de 100 Mbps, 500 Mbps e 1 Gbps, incluindo itens de MPLS óptico com roteador, L2L com transporte Ethernet/MPLS e links MPLS municipais. A API oficial de consulta do PNCP apresentou instabilidade/erro nesta sessão, o que exige confirmação posterior dos números de controle PNCP e documentos de suporte na pesquisa formal.

- Para o novo grupo Sede-Foro, não foram localizados três itens idênticos de 25 Gbps no PNCP nesta pesquisa preliminar; foram localizadas referências compatíveis de LAN-to-LAN, Metro Ethernet, fibra dedicada, datacenter, 4 Gbps, 5 Gbps e 10 Gbps, além de especificação pública com interfaces 10/25Gbps SFP28.

### Inferências analíticas

- A contratação de MPLS não substitui a SD-WAN vigente; ela compõe, desde o desenho inicial, uma arquitetura híbrida com camada privada para tráfego crítico, enquanto a SD-WAN permanece como camada preferencial para Internet.

- As capacidades MPLS requeridas correspondem às capacidades SD-WAN vigentes por localidade, como premissa de redundância total. A escolha deve ser confirmada por medição real de tráfego, pesquisa de mercado e validação da capacidade dos CPEs, mas evita contingência parcial e subdimensionamento em incidente.

- A existência de 3 saídas de Internet redundantes na Sede permite centralizar a egressão de Internet e aplicar políticas uniformes de segurança.

- A capacidade mínima combinada de 4 Gbps para as 3 saídas de Internet da Sede constitui premissa técnica conservadora, derivada da soma aproximada dos enlaces SD-WAN atuais, e deve ser validada por medição de uso, picos, simultaneidade, política de degradação controlada e pesquisa de mercado.

- A arquitetura mais resiliente é a que permite contingência cruzada: MPLS pode transportar tráfego de Internet em caso de falha da SD-WAN, e SD-WAN pode transportar tráfego crítico em caso de falha do MPLS.

- A equivalência de capacidade entre MPLS e SD-WAN é premissa técnica do modelo de disponibilidade adotado. Para sistemas judiciais, autenticação, colaboração, administração remota, suporte técnico e continuidade operacional, a capacidade equivalente é aderente ao objetivo de alta disponibilidade.

- A interligação Sede-Foro deve ser tratada como link dedicado ponto-a-ponto, e não MPLS, porque sua finalidade é criar um barramento de alta capacidade entre dois pontos centrais para replicação, backup, sincronização, baixa latência e continuidade operacional.

## I - Descrição da Necessidade de Contratação

### 1.1 Necessidade da Administração

O TRT10 necessita contratar serviços de comunicação de dados MPLS para interconectar suas unidades à Sede, de modo a prover uma camada privada, previsível, monitorável e resiliente para tráfego institucional crítico.

A necessidade decorre da dependência dos serviços digitais, da centralização de segurança e saída de Internet na Sede, da necessidade de redundância total entre camadas de conectividade e da conveniência de manter tráfego sensível em rede privada, com QoS, segregação lógica e controle de rotas. A arquitetura pretendida separa os fluxos por finalidade: MPLS para sistemas críticos e comunicação corporativa interna; SD-WAN para Internet; e uso recíproco dos meios em contingência.

A demanda considera os enlaces SD-WAN vigentes, com suas capacidades atuais e tunelamento IPSec, e define camada MPLS com a mesma capacidade nominal dos links SD-WAN em cada localidade. Com isso, assegura-se redundância total entre as camadas, de modo que a indisponibilidade de uma delas não obrigue a Administração a operar com banda nominal reduzida.

A Sede deverá operar como concentrador preferencial de saída de Internet, segurança, observabilidade e integração com redes institucionais, considerando a existência de 3 saídas de Internet redundantes. A saída local de Internet pelas unidades deverá ser tratada como exceção técnica, contingência ou fluxo formalmente autorizado, conforme política definida no projeto executivo.

A equivalência de banda entre as camadas é adotada como requisito inicial porque a separação entre tráfego crítico e não crítico tende a se tornar insuficiente durante incidentes reais: acesso ao PJe, colaboração, autenticação, suporte remoto, monitoramento, integrações, voz/vídeo e rotinas administrativas podem ocorrer simultaneamente e disputar capacidade. A equivalência de banda reduz esse risco e simplifica a operação de failover.

A necessidade também contempla interligação dedicada de 25 Gbps entre o Edifício Sede e o Foro de Brasília. O Foro deverá ser preparado como ponto de replicação e redundância da Sede, apto a receber tráfego de sincronização, backup, replicação de dados, serviços de continuidade e, conforme projeto executivo, acesso contingencial das demais unidades quando a Sede estiver indisponível ou degradada. Esse enlace deve ser contratado como link dedicado ponto-a-ponto, LAN-to-LAN, Metro Ethernet, clear channel, E-Line, E-LAN ou tecnologia equivalente, e não como MPLS.

### 1.1.1 Quais as especificações mínimas do objeto da contratação para que a necessidade da Administração possa ser satisfatoriamente atendida?

Para que a necessidade da Administração seja atendida de forma satisfatória, o objeto deverá contemplar uma solução continuada de comunicação de dados corporativa, em rede privada MPLS L3 VPN ou tecnologia funcionalmente equivalente, capaz de interconectar todas as unidades do TRT10 à Sede, coexistir com a SD-WAN vigente e permitir operação com preferência de tráfego e contingência cruzada.

As especificações mínimas abaixo constituem hipótese técnica de trabalho para o ETP e deverão ser refinadas no Termo de Referência, no projeto executivo e na pesquisa de mercado.

#### a) Escopo mínimo do serviço

A contratação deverá incluir, no mínimo:

- prestação de serviço continuado de comunicação de dados por rede privada corporativa MPLS L3 VPN ou tecnologia equivalente;

- interconexão da Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga, Foro de Palmas, Vara do Gama, Foro de Araguaína, Vara de Gurupi, Vara de Dianópolis e Vara de Guaraí;

- interligação dedicada ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, em grupo próprio, por fibra óptica, LAN-to-LAN/Metro Ethernet ou tecnologia equivalente;

- fornecimento, instalação, configuração, ativação, operação, manutenção e suporte dos circuitos;

- fornecimento dos CPEs, roteadores, modems, transceptores, fontes, cabos, licenças e demais elementos necessários a prestação do serviço, quando não forem expressamente indicados como responsabilidade do TRT10;

- monitoramento 24x7 dos circuitos e equipamentos sob responsabilidade da contratada;

- central de atendimento, registro de chamados, escalonamento técnico e relatórios mensais;

- documentação técnica inicial, documentação as built e atualização após mudanças relevantes.

#### b) Arquitetura mínima

A solução deverá adotar topologia lógica com à Sede como concentrador preferencial, mantendo todas às demais localidades interconectadas à Sede por MPLS. A Sede deverá permanecer como ponto preferencial de saída de Internet e de aplicação das políticas de segurança, considerando a existência de 3 saídas de Internet redundantes.

A arquitetura deverá permitir:

- uso preferencial do MPLS para tráfego crítico, sistemas institucionais, autenticação, serviços corporativos internos, administração, monitoramento e integrações;

- uso preferencial da SD-WAN para tráfego de Internet e serviços externos;

- uso do MPLS para tráfego de Internet em contingência da SD-WAN, com egressão preferencial pela Sede;

- uso da SD-WAN para tráfego crítico em contingência do MPLS;

- retorno controlado ao caminho preferencial após normalizacao;

- capacidade agregada na Sede para suportar, em condições normais e em regime de contingência controlada, a egressão de Internet das unidades;

- uso do Foro de Brasília como ponto de replicação e redundância da Sede, com enlace dedicado de 25 Gbps entre os dois prédios;

- redirecionamento contingencial do acesso das unidades ao Foro de Brasília, conforme rotas, segurança, serviços disponíveis e critério de acionamento definidos no projeto executivo;

- convivência com firewalls, roteadores, controladores SD-WAN, redes JT, Infovia e demais componentes indicados pela CDTEC.

#### c) Capacidades mínimas preliminares

As capacidades mínimas preliminares deverão observar o dimensionamento abaixo, sujeito a validação por medição de tráfego, criticidade, simultaneidade, crescimento esperado e pesquisa de mercado:

| Item | Localidade | Capacidade SD-WAN vigente | Capacidade MPLS requerida | Papel técnico |
|---|---|---|---|---|
| 1 | Edifício Sede | 1 Gbps | 1 Gbps | Concentrador preferencial |
| 2 | Foro de Brasília | 1 Gbps | 1 Gbps | Unidade de alta demanda |
| 3 | Prédio de Apoio | 500 Mbps | 500 Mbps | Unidade metropolitana |
| 4 | Foro de Taguatinga | 500 Mbps | 500 Mbps | Unidade regional DF |
| 5 | Foro de Palmas | 500 Mbps | 500 Mbps | Polo regional TO |
| 6 | Vara do Gama | 100 Mbps | 100 Mbps | Unidade remota |
| 7 | Foro de Araguaína | 100 Mbps | 100 Mbps | Unidade remota |
| 8 | Vara de Gurupi | 100 Mbps | 100 Mbps | Unidade remota |
| 9 | Vara de Dianópolis | 100 Mbps | 100 Mbps | Unidade remota |
| 10 | Vara de Guaraí | 100 Mbps | 100 Mbps | Unidade remota |

Grupo específico de interligação dedicada entre pontos centrais:

| Item | Enlace | Tecnologia mínima | Capacidade | Papel técnico |
|---|---|---|---|---|
| 11 | Edifício Sede ↔ Foro de Brasília | link dedicado ponto-a-ponto por fibra óptica, LAN-to-LAN/Metro Ethernet, clear channel, E-Line, E-LAN ou equivalente | 25 Gbps | Replicação, backup, sincronização, baixa latência, redundância da Sede e acesso contingencial das unidades |

Os circuitos deverão ser simétricos, full duplex, com banda útil compatível com a capacidade contratada, ressalvados apenas os overheads inerentes aos protocolos de comunicação.

Como premissa para pesquisa de preços e validação técnica, as 3 saídas de Internet da Sede deverão ser dimensionadas para capacidade mínima combinada de 4 Gbps em operação normal, preferencialmente com operadoras e rotas físicas distintas. Essa premissa não substitui a medição real de tráfego, devendo ser ajustada conforme uso médio, picos, simultaneidade, criticidade dos serviços e política de degradação controlada.

A equivalência entre MPLS e SD-WAN não significa duplicidade indevida de objeto, pois as camadas possuem papeis técnicos complementares: à SD-WAN utiliza transporte por Internet dedicada, túneis, orquestracao e políticas de acesso; o MPLS fornece rede privada corporativa, isolamento lógico, QoS e caminho controlado para interconexão. A duplicacao de capacidade nominal decorre da finalidade de redundância integral, e não da repeticao desnecessaria de uma mesma solução.

O link dedicado de 25 Gbps Sede-Foro possui natureza distinta da rede MPLS das localidades. Ele não é enlace MPLS de filial, mas circuito de alta capacidade entre dois pontos centrais, voltado a replicação, continuidade, contingência e baixa latência. Por isso, deverá compor grupo próprio na modelagem da contratação e na pesquisa de preços.

#### c.1) Itens complementares a prever no TR

O Termo de Referência deverá avaliar a inclusão ou explicitacao dos seguintes itens complementares:

- 3 links de Internet centralizados e redundantes na Sede, preferencialmente com operadoras e rotas físicas distintas;

- equipamentos de borda, roteadores, CPEs ou integração com firewalls existentes, sem vinculação a marca específica;

- serviços de implantação, configuração, testes de aceite, documentação e transferência de conhecimento;

- monitoramento 24x7 dos links, alertas de indisponibilidade e relatórios mensais de SLA;

- suporte técnico com prazos definidos para falha crítica, degradação e indisponibilidade;

- endereçamento, roteamento, QoS, segmentação e políticas de segurança documentadas no projeto executivo.

#### d) Roteamento, segregação e QoS

A solução deverá suportar roteamento controlado e integração com a infraestrutura existente do TRT10, preferencialmente por BGP ou OSPF, ou por roteamento estático quando tecnicamente justificado. O projeto executivo deverá definir rotas anunciadas, métricas, prioridades, contingência, retorno ao caminho preferencial e prevenção de loops.

A solução deverá prover isolamento lógico do tráfego do TRT10, por VRF ou mecanismo equivalente, e suportar QoS com classes de serviço configuraveis. Como referência inicial, deverão ser previstas classes para:

- tráfego crítico de sistemas judiciais, autenticação, serviços internos e administração;

- tráfego sensível a tempo, como voz, video e colaboração, quando aplicável;

- tráfego corporativo administrativo;

- tráfego de melhor esforço.

As marcações, filas, percentuais de reserva e políticas de descarte deverão ser definidos no projeto executivo, sem exigência de marca, fabricante ou tecnologia proprietária específica.

#### e) Disponibilidade, desempenho e suporte

Como requisito mínimo preliminar, a solução deverá observar disponibilidade mensal de referência de 99,90% para a Sede e 99,70% para as demais localidades, em coerência com o histórico da contratação SD-WAN. As metas finais deverão ser confirmadas no Termo de Referência.

O TR deverá definir, de forma mensuravel:

- disponibilidade por circuito;

- prazo para início de atendimento;

- prazo de reparo por severidade;

- regras de manutenção programada;

- formula de cálculo de disponibilidade;

- hipoteses de glosa;

- forma de afericao por relatórios da contratada e validação da fiscalização;

- parametros de latência, perda de pacotes e jitter, após validação de mercado.

#### f) Implantação, testes e aceite

A contratada deverá apresentar plano de implantação antes da ativação dos circuitos, contendo cronograma, pré-requisitos, responsáveis, janelas de mudança, testes, riscos e plano de rollback. A implantação deverá ocorrer preferencialmente por fases, iniciando pela Sede e pelas unidades de maior criticidade.

O aceite mínimo por localidade deverá verificar:

- identificação do circuito;

- banda contratada;

- conectividade com à Sede;

- roteamento conforme projeto;

- acesso a serviços institucionais;

- registro no monitoramento;

- abertura de chamado teste;

- medição inicial de latência e perda;

- teste de contingência entre MPLS e SD-WAN, quando tecnicamente aplicável;

- entrega de documentação as built.

#### g) Segurança e confidencialidade

A contratada deverá preservar o sigilo das informações de rede, endereçamento, rotas, configurações, chamados e incidentes. Deverá manter controle de acesso administrativo aos equipamentos sob sua responsabilidade, registrar mudanças relevantes e comunicar incidentes que possam afetar disponibilidade, integridade, confidencialidade ou continuidade do serviço.

#### h) Vedação a direcionamento

As especificações deverão ser descritas por requisitos funcionais e de desempenho, sem indicação de marca, fabricante, modelo ou solução proprietária específica, salvo quando indispensável e devidamente justificado. Deverá ser admitida tecnologia equivalente ao MPLS quando demonstrada aderência funcional aos requisitos de rede privada, isolamento, QoS, roteamento controlado, monitoramento e SLA.

### 1.1.2 Será necessário exigir garantia contratual do objeto, complementar a legal?

Sim. Recomenda-se exigir garantia contratual do objeto durante toda a vigência da contratação, complementar as garantias legais aplicáveis, abrangendo o funcionamento dos circuitos, CPEs, roteadores, modems, fontes, transceptores, licenças, configurações, monitoramento, suporte técnico e demais componentes fornecidos ou operados pela contratada.

A garantia do objeto deverá assegurar que falhas, defeitos, indisponibilidades ou degradações imputáveis a contratada sejam corrigidos sem ônus adicional para o TRT10, observados os prazos de atendimento, reparo, disponibilidade e demais níveis mínimos de serviço previstos no Termo de Referência e no contrato.

Essa garantia do objeto não substitui a garantia de execução contratual eventualmente exigida, nem afasta a aplicação de glosas, sanções, obrigacoes de reparo, substituicao de equipamentos, manutenção corretiva ou demais medidas previstas no instrumento contratual.

### 1.1.3 A garantia contratual do objeto e compatível com às práticas de mercado?

Sim. A exigência e compatível com às práticas de mercado para serviços continuados de telecomunicações e comunicação de dados, nos quais e usual que a contratada se responsabilize pela disponibilidade do circuito, funcionamento dos equipamentos sob sua gestão, manutenção corretiva, substituicao de componentes defeituosos, suporte técnico, monitoramento e cumprimento de SLA durante toda a vigência contratual.

Também é prática usual que equipamentos fornecidos em comodato, locação, cessão de uso ou como parte indissociável do serviço sejam mantidos pela contratada, sem transferência de responsabilidade técnica ao contratante, salvo quando houver dano causado por uso indevido, caso fortuito, força maior ou responsabilidade expressamente atribuída ao contratante no contrato.

### 1.2 Quais as características mínimas do modelo de execução da contratação para que a necessidade da Administração possa ser satisfatoriamente atendida?

O modelo de execução deverá permitir implantação controlada, operação continuada, fiscalização objetiva e preservacao da conectividade vigente durante a transição. Para tanto, deverá contemplar, no mínimo:

- emissão de ordem de serviço para início da execução;

- apresentacao de plano de implantação pela contratada em prazo definido no Termo de Referência;

- levantamento inicial de pré-requisitos por localidade, incluindo acesso físico, energia, espaço, passagem de cabos, infraestrutura de fibra, CPEs e pontos de conexão;

- implantação por fases, iniciando pela Sede e pelas unidades de maior criticidade ou maior capacidade;

- convivência com a SD-WAN vigente durante a implantação do MPLS, evitando interrupcao dos serviços institucionais;

- entrega de projeto executivo antes da ativação, contendo desenho lógico, rotas, endereçamento, políticas de preferência, QoS, contingência, responsabilidades e rollback;

- ativação e teste de aceite por localidade;

- operação assistida após a ativação dos circuitos, com acompanhamento de estabilidade, roteamento, desempenho, chamados e relatórios;

- monitoramento 24x7 dos circuitos e equipamentos sob responsabilidade da contratada;

- disponibilização de central de atendimento, portal ou canal equivalente de abertura de chamados, telefone e e-mail;

- relatório mensal com disponibilidade, indisponibilidades, chamados, causa raiz, tempos de atendimento, reparos, manutenções, desempenho e eventos de contingência;

- reuniões técnicas de acompanhamento, quando solicitadas pela fiscalização;

- documentação as built e atualização documental sempre que houver mudança relevante;

- execução de manutenções programadas apenas mediante comunicação e autorização prévia, quando houver risco de impacto;

- aplicação de glosas e sanções em caso de descumprimento dos níveis de serviço, conforme regras do TR e do contrato.

O modelo deverá prever recebimento provisorio por localidade após ativação e teste, e recebimento definitivo após periodo de observacao, saneamento de pendencias e validação pela fiscalização técnica.

Sugere-se que a implantação seja faseada, permitindo preservar a continuidade da SD-WAN vigente e reduzir risco operacional:

| Fase | Escopo | Objetivo |
|---|---|---|
| 1 | Sede | Implantar concentrador principal, validar saídas centrais de Internet, roteamento, segurança e saída preferencial |
| 2 | Gama e Taguatinga | Atender unidades com maior sensibilidade contratual histórica |
| 3 | Prédio de Apoio e Palmas | Integrar unidades de demanda intermediária |
| 4 | Araguaína, Gurupi, Dianópolis e Guaraí | Concluir capilaridade MPLS e contingência das unidades remotas |
| 5 | Operação assistida | Validar failover, QoS, desempenho, monitoramento e documentação final |

### 1.2.1 Será admitida a subcontratação? Se sim, apresente as justificativas, bem como indique seus limites e partes do objeto.

Sim. Sugere-se admitir subcontratação apenas para atividades acessórias de infraestrutura local, lançamento de fibra, obras civis leves, passagem de cabos, adequações físicas, vistorias, instalação de último trecho e atendimento de campo, mantendo a contratada principal integralmente responsável pela prestação do serviço, pelo SLA, pela segurança, pela documentação, pelo suporte, pela operação e pela manutenção da solução.

A justificativa para admitir subcontratação limitada decorre da natureza distribuída da solução, que envolve localidades no Distrito Federal e no Tocantins, podendo exigir equipes locais, acesso à infraestrutura regional, serviços de campo e atividades acessórias que não representam a gestão técnica central do serviço de comunicação de dados.

Não deverá ser admitida subcontratação que transfira a responsabilidade principal pela rede privada corporativa, pela gerência dos circuitos, pelo cumprimento do SLA, pelo atendimento ao TRT10, pela segurança das informações ou pela integração técnica com a arquitetura MPLS/SD-WAN. A contratada principal deverá responder integralmente por atos, omissões, falhas e atrasos de suas subcontratadas.

### 1.2.2 Os riscos ou características da contratação tornam recomendavel a exigência de garantia de execução contratual?

Sim, recomenda-se avaliar a exigência de garantia de execução contratual na versão final do Termo de Referência, considerando o valor estimado, à criticidade do serviço, a quantidade de localidades, a necessidade de implantação coordenada, o fornecimento de equipamentos, a dependência de SLA e o impacto operacional de eventual inadimplemento.

A garantia de execução contratual e recomendavel porque a contratação envolve serviço continuado essencial, com risco de atraso de implantação, indisponibilidade de circuitos, falha de integração MPLS/SD-WAN, descumprimento de níveis de serviço e necessidade de manutenção da continuidade da comunicação institucional. O percentual, modalidade e condições da garantia deverão ser definidos no TR final, após estimativa de valor, análise de riscos e manifestação da área jurídica/administrativa competente.

### 1.3 A necessidade decorre de determinacao legal?

Não há obrigação legal de adotar MPLS como tecnologia. A contratação se fundamenta na necessidade administrativa de assegurar continuidade, disponibilidade e segurança da comunicação de dados. A Lei nº 14.133/2021 orienta o planejamento e a estruturação dos artefatos; a ENTIC-JUD 2021-2026 orienta a governança de TIC no Poder Judiciário.

### 1.4 Natureza continuada

A necessidade possui natureza continuada, pois a comunicação entre unidades e Sede e indispensável ao funcionamento permanente dos serviços judiciais e administrativos.

## II - Previsão no Planejamento Institucional, PLS e PCA

### 2.1 Alinhamento ao Planejamento Estratégico

A demanda se alinha ao objetivo estratégico "Aprimorar a Governança de TIC e a proteção de dados", pois aumenta a disponibilidade, a segurança e a governabilidade da infraestrutura de comunicação.

### 2.2 Alinhamento ao PLS

Há alinhamento indireto com o uso eficiente de recursos de TIC, redução de deslocamentos por indisponibilidade técnica, melhor uso de serviços digitais e racionalização de infraestrutura.

### 2.3 PCA/SIGPLAC

A confirmação de inclusão no PCA/SIGPLAC deverá ser realizada pela unidade competente. Caso ainda não conste, recomenda-se providenciar a inclusão ou justificar a demanda superveniente.

## III - Requisitos da Contratação e Criterios de Sustentabilidade

### 3.1 Requisitos do objeto

Requisitos mínimos sugeridos:

- rede MPLS L3 VPN ou tecnologia equivalente de rede privada corporativa, desde que preserve isolamento lógico, QoS e roteamento controlado;

- interconexão das demais localidades à Sede;

- fornecimento de CPEs, modems, transceptores, cabos, licenças e demais itens necessários;

- compatibilidade com roteamento dinâmico, preferencialmente OSPF ou BGP, conforme projeto executivo;

- suporte a QoS para classes de tráfego crítico, administrativo, voz/vídeo, monitoramento e melhor esforço;

- suporte a VRF ou segregação lógica equivalente;

- capacidade simétrica mínima conforme tabela de dimensionamento;

- monitoramento 24x7, portal de chamados e relatórios mensais;

- SLA de disponibilidade mínima sugerido de 99,90% para a Sede e 99,70% para demais localidades, em coerência com o histórico da SD-WAN, sujeito a validação no TR.

- políticas de roteamento que priorizem MPLS para tráfego crítico e SD-WAN para Internet;

- contingência automatizada ou operacionalmente documentada entre MPLS e SD-WAN, com critérios objetivos de acionamento, retorno e registro.

### 3.2 Requisitos de execução

- implantação por fases, iniciando pela Sede;

- ativação e teste de aceite por localidade;

- entrega de documentação "as built";

- operação assistida mínima de 30 dias após ativação de todas as localidades;

- suporte técnico com chamados por portal, telefone e e-mail;

- relatório mensal de disponibilidade, indisponibilidade, chamados, tempo de reparo, perdas e incidentes.

### 3.3 Subcontratação

Sugere-se admitir subcontratação apenas para atividades acessórias de infraestrutura local, lançamento de fibra, obras civis leves e atendimento de campo, mantendo a contratada principal integralmente responsável pela prestação do serviço e pelo SLA.

### 3.4 Sustentabilidade e acessibilidade

Exigir equipamentos com eficiência energética compatível com o mercado, descarte ambientalmente adequado de equipamentos substituídos, redução de deslocamentos por meio de monitoramento remoto e atendimento as normas trabalhistas, ambientais e de segurança aplicáveis.

### 3.4.1 Quais os critérios e práticas de sustentabilidade e acessibilidade cabíveis ou exigiveis, no caso?

Considerando a natureza da contratação, os critérios de sustentabilidade e acessibilidade cabíveis devem ser compatibilizados com serviços continuados de telecomunicações, comunicação de dados, infraestrutura de rede e atendimento técnico. São critérios e práticas recomendáveis:

- priorizacao de equipamentos com eficiência energética compatível com às práticas de mercado;

- uso de equipamentos, fontes e acessorios em conformidade com normas técnicas e regulamentos aplicáveis;

- descarte ambientalmente adequado de equipamentos, cabos, fontes, baterias, embalagens e demais resíduos sob responsabilidade da contratada;

- redução de deslocamentos mediante monitoramento remoto, abertura remota de chamados, diagnóstico remoto e atendimento presencial apenas quando necessário;

- consolidação de relatórios em meio digital;

- reaproveitamento de infraestrutura existente sempre que tecnicamente possível e autorizado;

- adoção de janelas de manutenção planejadas para reduzir retrabalho e deslocamentos;

- observância de normas de segurança do trabalho nas atividades de instalação, lançamento de cabos, acesso a salas técnicas, racks, forros, shafts e demais ambientes;

- garantia de que instalacoes físicas, passagem de cabos e acomodacao de equipamentos não prejudiquem rotas de circulacao, acessibilidade física, segurança predial ou sinalizacao;

- atendimento a requisitos de sigilo, proteção de informações e minimização de acesso a dados de rede;

- preferência por documentação digital, as built eletrônico e relatórios mensais em formato pesquisavel.

### 3.4.2 Caso não aplicáveis critérios de sustentabilidade e acessibilidades, apresentar as justificativas.

Os critérios de sustentabilidade e acessibilidade são aplicáveis de forma proporcional ao objeto. Não se trata de contratação de obra, aquisição massiva de bens permanentes ou solução diretamente voltada ao atendimento ao público, razão pela qual alguns critérios típicos de obras, mobiliário, edificações, materiais de consumo ou acessibilidade de interfaces digitais podem não ser pertinentes.

Assim, os critérios devem se concentrar na eficiência energética dos equipamentos, descarte ambientalmente adequado, redução de deslocamentos, segurança em instalacoes, documentação digital, reaproveitamento de infraestrutura e preservacao da acessibilidade física dos ambientes onde houver instalação de equipamentos ou cabos.

### 3.4.3 Foi consultado o Guia de Contratações Sustentáveis da Justiça do Trabalho (CSJT), ou, subsidiariamente, o Guia Nacional de Contratações Sustentáveis (AGU)?

Recomenda-se registrar, na versão final do ETP, a consulta ao Guia de Contratações Sustentáveis da Justiça do Trabalho (CSJT) e, subsidiariamente, ao Guia Nacional de Contratações Sustentáveis da AGU, para confirmar a aderência dos critérios aplicáveis ao objeto.

Nesta minuta, a consulta deverá ser confirmada pela equipe de planejamento antes da finalização do processo. Caso a consulta ainda não tenha sido formalizada, deve permanecer como pendência de instrução, sem prejuízo da inclusão preliminar dos critérios de sustentabilidade proporcionais ao objeto.

### 3.5 Esclareca se a solução escolhida demandara a contratação de serviços de manutenção e/ou assistência técnica.

Sim. A solução escolhida demandara manutenção e assistência técnica durante toda a vigência contratual, mas tais atividades deverão compor o próprio objeto da contratação, sem necessidade de contratação apartada, salvo se à Administração optar por escopo excepcional não previsto neste ETP.

A manutenção e assistência técnica deverão abranger, no mínimo:

- manutenção corretiva dos circuitos, acessos, CPEs, roteadores, modems, fontes, transceptores, cabos e demais componentes sob responsabilidade da contratada;

- substituicao de equipamentos defeituosos ou degradados sob responsabilidade da contratada;

- suporte técnico para indisponibilidade, degradação, perda de pacotes, latência anormal, falha de roteamento, falha de QoS e falha de monitoramento;

- atendimento remoto e presencial quando necessário;

- monitoramento 24x7;

- abertura, acompanhamento, escalonamento e encerramento de chamados;

- manutenções programadas previamente comunicadas e autorizadas quando houver risco de impacto;

- atualização da documentação técnica após mudanças relevantes.

Assim, os custos de manutenção, suporte e assistência técnica deverão estar incorporados aos valores mensais dos circuitos ou aos itens específicos previstos no Termo de Referência, evitando lacunas de responsabilidade durante a execução contratual.

### 3.6 No caso de compras, será necessário analisar amostras?

Não se aplica como regra principal, pois o objeto pretendido e serviço continuado de comunicação de dados, e não compra isolada de bens. Não se recomenda exigir amostras físicas como critério ordinário de aceitação da proposta, pois os equipamentos, CPEs, licenças e acessorios integram a prestação do serviço e deverão ser avaliados por requisitos funcionais, documentação técnica, projeto executivo, testes de ativação e aceite por localidade.

Caso o Termo de Referência venha a prever fornecimento relevante de equipamentos como parte destacada do objeto, à Administração poderá exigir catálogos, datasheets, declarações técnicas, comprovação de compatibilidade, homologações aplicáveis e demonstração de atendimento aos requisitos, sem direcionamento por marca ou modelo.

### 3.7 No caso de serviços, será necessário vistoria prévia do local da execução dos serviços?

Recomenda-se que a vistoria prévia seja facultativa, e não obrigatória, podendo ser substituída por declaracao da licitante de que conhece as condições locais e assume responsabilidade pela formulação de sua proposta. Essa abordagem reduz risco de restrição indevida a competitividade e preserva a possibilidade de participação de fornecedores que consigam estimar custos por documentação, mapas, endereços, inventário técnico e informações disponibilizadas no edital.

A vistoria facultativa poderá ser disponibilizada para as localidades do TRT10, mediante agendamento, especialmente quando houver necessidade de verificar entrada de fibra, sala técnica, rack, energia, infraestrutura de passagem, espaço para CPE, restrições prediais ou condições de acesso. A não realização de vistoria não deverá justificar pedidos posteriores de acréscimo de custos, desde que o edital disponibilize informações mínimas suficientes sobre as localidades e condições de execução.

### 3.8 É necessária autorização do poder público para o exercício da atividade a ser contratada (habilitação jurídica)?

Sim. Por se tratar de serviço de telecomunicações/comunicação de dados, deverá ser exigida, quando aplicável, comprovação de autorização, outorga, licenca ou instrumento regulatório pertinente para prestação dos serviços, nos termos da regulamentacao setorial vigente.

Em princípio, a contratada deverá demonstrar regularidade para prestação de Serviço de Comunicação Multimídia (SCM) ou outro enquadramento regulatório aplicável ao serviço efetivamente ofertado, junto a Anatel, diretamente ou por meio de arranjo juridicamente admitido. Caso a licitante utilize infraestrutura, autorização ou serviços de terceiros, deverá demonstrar que tal arranjo não transfere ao TRT10 riscos de irregularidade regulatoria, descontinuidade ou ausência de responsabilidade contratual.

A exigência deverá ser redigida de forma funcional e proporcional, evitando restringir indevidamente a competição, mas assegurando que a futura contratada esteja apta a prestar os serviços de telecomunicações objeto da contratação.

### 3.9 Será necessário exigir qualificações econômico-financeiras adicionais?

Em princípio, não se recomenda exigir qualificações econômico-financeiras adicionais além daquelas ordinariamente previstas na legislação e no edital, enquanto não houver estimativa final de valor, matriz de riscos completa e definição final de vigência. A contratação envolve serviço continuado essencial, mas os riscos economico-financeiros podem ser mitigados por garantia de execução contratual, pagamentos mensais condicionados ao aceite, glosas por descumprimento de SLA e fiscalização contratual.

Na versão final do Termo de Referência, a equipe de planejamento deverá avaliar, com base no valor estimado, criticidade, prazo contratual e análise de riscos, se há justificativa para exigir índices contábeis, patrimônio líquido mínimo, capital social mínimo ou garantia de proposta/execução, observados os limites legais e a proporcionalidade. Exigências excessivas devem ser evitadas para não restringir indevidamente a competitividade.

### 3.10 Será necessário exigir qualificações técnicas técnico-operacional e técnico-profissional especiais?

Sim. Recomenda-se exigir qualificação técnico-operacional compatível com a complexidade do objeto, especialmente porque a solução envolve rede privada corporativa, múltiplas localidades, SLA, monitoramento, suporte, roteamento, QoS, integração com SD-WAN e continuidade de serviços críticos.

A qualificação técnico-operacional deverá comprovar experiência anterior da licitante em prestação de serviço semelhante, contemplando, preferencialmente:

- comunicação de dados corporativa por MPLS, L3VPN, L2L, rede privada gerenciada ou tecnologia equivalente;

- atendimento a múltiplas localidades;

- operação, monitoramento e suporte de circuitos;

- cumprimento de níveis de serviço e atendimento a chamados;

- fornecimento ou gestão de CPEs/roteadores;

- implantação, configuração, manutenção e documentação de rede.

A exigência deve ser proporcional ao objeto, sem exigir identidade absoluta com a solução do TRT10 e sem impor marca, fabricante ou modelo. Os quantitativos mínimos, quando adotados, deverão ser definidos após pesquisa de mercado, de modo a comprovar capacidade técnica sem restringir indevidamente a competitividade.

Quanto à qualificação técnico-profissional, recomenda-se avaliar a exigência de indicação de responsável técnico ou equipe técnica com experiência em redes corporativas, telecomunicações, roteamento, segurança de rede ou operação de serviços de comunicação de dados. A exigência deverá ser justificada no Termo de Referência final e compatibilizada com a natureza comum do serviço, evitando requisitos excessivos ou desnecessários.

## IV - Levantamento de Mercado

### 4.1 Soluções identificadas

Foram avaliadas as seguintes alternativas aderentes ao problema arquitetural:

| Alternativa | Descrição | Pros | Contras / Riscos |
|---|---|---|---|
| Solução 1 - MPLS integrado à SD-WAN com capacidade equivalente | Contratação de MPLS com a mesma capacidade nominal da SD-WAN por localidade. Ambos os meios podem transportar qualquer tráfego em contingência. | Combina rede privada, QoS, isolamento lógico, previsibilidade, centralização na Sede, convivência com a SD-WAN vigente e redundância total por caminhos distintos. Permite tratar tráfego crítico e Internet com políticas distintas, sem reduzir banda durante falha de uma camada. | Exige projeto executivo de roteamento, definição de QoS, monitoramento integrado e gestão coordenada entre contrato MPLS e contrato SD-WAN. A vantajosidade deverá ser demonstrada pela relação entre custo, disponibilidade, continuidade, segurança e redução de risco operacional. |
| Solução 2 - Links satelitais | Contratação de enlaces satelitais para atuar como meio de interconexão das unidades à Sede, substituindo ou complementando a função pretendida para o MPLS. | Pode ser útil em locais sem boa cobertura terrestre, em contingência de desastres regionais ou como caminho fisicamente diverso. Independe parcialmente de infraestrutura terrestre local. | Tende a apresentar maior latência, maior variabilidade de desempenho, possíveis franquias ou restrições técnicas, sensibilidade a condições ambientais e menor aderência para sistemas críticos sensíveis a atraso. Pode elevar custo por Mbps e exigir arquitetura adicional de roteamento/segurança. |
| Solução 3 - Links de Internet comuns com VPN ponto a ponto | Contratação de links convencionais de Internet nas unidades, estabelecendo túneis VPN ponto a ponto ou malha VPN até a Sede. | Pode ter maior disponibilidade de fornecedores locais, menor custo unitário aparente e implantação simples em algumas localidades. | Não garante a mesma previsibilidade de rede privada, dificulta QoS fim a fim, amplia superfície exposta à Internet, aumenta complexidade de operação de túneis, depende da qualidade da Internet local e pode gerar maior esforço de suporte, troubleshooting e segurança. |

### 4.2 Análise comparativa das soluções

A Solução 1 é a que melhor equilibra disponibilidade, segurança, governança e convivência com a infraestrutura vigente. A SD-WAN contratada continua exercendo papel relevante para saída de Internet, balanceamento e contingência; o MPLS acrescenta uma camada privada para tráfego crítico e institucional, reduzindo dependência exclusiva dos enlaces de Internet para comunicação entre unidades e Sede. A Solução 1 preve capacidade MPLS equivalente a capacidade SD-WAN em cada localidade porque o objetivo arquitetural e assegurar redundância integral para à continuidade dos serviços.

Do ponto de vista arquitetural, à Sede possui papel natural de concentrador porque abriga as 3 saídas redundantes de Internet, políticas de segurança perimetral, integrações institucionais e concentração de serviços corporativos. Ao interconectar as unidades à Sede por MPLS, à Administração passa a dispor de um caminho controlado para sistemas críticos e, ao mesmo tempo, mantém a SD-WAN para tráfego de Internet e contingência. Essa separação reduz competição entre fluxos de natureza distinta e permite aplicar QoS, priorizacao, monitoramento e glosas por circuito.

A Solução 2, baseada em links satelitais, é tecnicamente possível, mas deve ser tratada como alternativa complementar ou de contingência específica, não como desenho preferencial para todo o ambiente. A latência e a variabilidade de desempenho podem afetar autenticação, sessoes de sistemas, voz, video, replicacoes e outros fluxos sensíveis. Sua melhor aplicação seria para localidades sem viabilidade terrestre ou para plano de continuidade de negócios em cenários extremos.

A Solução 3, baseada em Internet comum com VPN ponto a ponto, reduz barreiras iniciais, mas transfere para a Administração maior complexidade operacional e maior dependência de redes públicas. Embora VPNs possam prover confidencialidade, elas não equivalem a QoS fim a fim, previsibilidade de backbone, isolamento operacional e SLA privado. A multiplicação de túneis também pode dificultar mudanças, troubleshooting, gestão de chaves, auditoria e evolução da topologia.

### 4.3 Solução escolhida

A solução escolhida é a Solução 1: utilização integrada de MPLS e SD-WAN, com MPLS contratado na mesma capacidade nominal dos links SD-WAN vigentes por localidade. O MPLS será contratado para interconectar as unidades à Sede e transportar preferencialmente tráfego crítico de sistemas institucionais, serviços internos, autenticação, administração e integrações. A SD-WAN vigente permanecerá como camada preferencial para Internet. Em caso de falha, degradação relevante ou manutenção de uma das camadas, a arquitetura deverá permitir contingência cruzada, de modo que MPLS e SD-WAN possam transportar os fluxos necessários à continuidade dos serviços sem redução planejada de capacidade nominal.

A escolha da Solução 1 fica condicionada a validação por pesquisa de preços, confirmação de capacidade por localidade, definição de políticas de QoS e confirmação de viabilidade de roteamento com a infraestrutura existente.

## V - Descrição da Solução como um Todo

A solução consiste em contratar conectividade privada para as 10 localidades, tendo à Sede como concentrador preferencial. Todas nas demais unidades deverão possuir circuito MPLS até a Sede. A SD-WAN vigente permanecerá ativa como camada preferencial para Internet, enquanto o MPLS será a camada preferencial para tráfego crítico. A saída de Internet será preferencialmente centralizada na Sede, onde existem 3 saídas redundantes de Internet.

A solução deverá coexistir com a SD-WAN como transporte vigente, considerando seus enlaces, túneis IPSec, roteamento dinâmico e capacidade contratada. O MPLS atuara como camada privada, voltada a tráfego corporativo crítico, contingência controlada, isolamento lógico, previsibilidade de desempenho e rotas de recuperacao.

A solução também deverá contratar link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, separado da malha MPLS, para criar um eixo de alta capacidade entre os dois principais pontos institucionais. O Foro de Brasília deverá ser considerado ambiente de replicação e redundância, com possibilidade de assumir, em contingência, funções de acesso das unidades, desde que o projeto executivo preveja rotas, segurança, disponibilidade de serviços, DNS, autenticação, firewalls e procedimentos operacionais.

### Logica arquitetural da Solução 1

1. A Sede concentra as 3 saídas redundantes de Internet e deve permanecer como ponto preferencial de egressão, segurança, filtragem e observabilidade.

1. O MPLS fornece caminho privado e controlado para tráfego crítico entre unidades e Sede, permitindo QoS, segregação lógica e metas objetivas de disponibilidade.

1. A SD-WAN mantém a capacidade já contratada para acesso à Internet e pode operar como caminho alternativo para tráfego crítico quando o MPLS estiver indisponível ou degradado.

1. O MPLS pode transportar tráfego de Internet em contingência, direcionando as unidades para a Sede quando à SD-WAN local estiver indisponível ou degradada.

1. O desenho evita dependência exclusiva de uma tecnologia e reduz o risco de indisponibilidade total por falha de um único meio de comunicação.

1. O link dedicado Sede-Foro de 25 Gbps viabiliza replicação, sincronização e uso do Foro como redundância da Sede.

1. A convivência entre MPLS, SD-WAN e link dedicado Sede-Foro deve ser definida em projeto executivo, com rotas preferenciais, métricas, failover, retorno controlado, QoS, segurança e monitoramento.

### Topologia proposta

![Figura 1 - Arquitetura proposta SD-WAN + MPLS](../diagrama_topologia_revisada.png)

### Dimensionamento preliminar

| Item | Localidade | SD-WAN vigente | MPLS requerido | Papel |
|---|---|---|---|---|
| 1 | Edifício Sede | 1 Gbps | 1 Gbps | Concentrador preferencial |
| 2 | Foro de Brasília | 1 Gbps | 1 Gbps | Unidade de maior demanda interconectada à Sede |
| 3 | Prédio de Apoio | 500 Mbps | 500 Mbps | Unidade metropolitana |
| 4 | Foro de Taguatinga | 500 Mbps | 500 Mbps | Unidade regional DF |
| 5 | Foro de Palmas | 500 Mbps | 500 Mbps | Polo TO |
| 6 | Vara do Gama | 100 Mbps | 100 Mbps | Unidade remota |
| 7 | Foro de Araguaína | 100 Mbps | 100 Mbps | Unidade remota |
| 8 | Vara de Gurupi | 100 Mbps | 100 Mbps | Unidade remota |
| 9 | Vara de Dianópolis | 100 Mbps | 100 Mbps | Unidade remota |
| 10 | Vara de Guaraí | 100 Mbps | 100 Mbps | Unidade remota |
| 11 | Sede ↔ Foro de Brasília | Não se aplica | link dedicado 25 Gbps | Replicação, redundância da Sede e acesso contingencial das unidades |

### Premissas de capacidade da Sede

Considerando a soma aproximada de 4 Gbps dos enlaces SD-WAN atuais das localidades, a Sede deverá ter capacidade agregada suficiente para atuar como ponto preferencial de egressão de Internet e concentração de políticas. A capacidade mínima combinada de 4 Gbps nas 3 saídas centrais é premissa técnica inicial, devendo ser validada e eventualmente ajustada pela pesquisa de preços, medição de tráfego, fator de simultaneidade, crescimento esperado e política de degradação em contingência. A equivalência de capacidade entre MPLS e SD-WAN por localidade não elimina a necessidade de QoS; ela assegura que o failover não dependa de uma redução prévia da banda disponível.

O enlace dedicado Sede-Foro de 25 Gbps deve ser dimensionado para cargas de replicação e contingência, não apenas para tráfego ordinário de usuários. A banda elevada se justifica pela necessidade de transferências volumosas entre ambientes, sincronização de dados, restauração, espelhamento, backup, testes de continuidade e eventual redirecionamento de acesso das unidades ao Foro. A especificação final deverá prever, no mínimo, banda simétrica full duplex, baixa latência, medição de perda, jitter, disponibilidade, rotas físicas preferencialmente distintas quando aplicável, interfaces 25GbE/SFP28 ou equivalentes e aceite com teste de throughput.

### Diretrizes de operação e governança

- Definir política clara de roteamento, com Internet preferencialmente vià Sede e tráfego local apenas quando formalmente autorizado e controlado.

- Implementar QoS fim a fim para priorizar processo judicial, sistemas administrativos, autenticação, voz/vídeo institucional, monitoramento e tráfego de replicação.

- Medir latência, jitter, perda de pacotes e throughput por unidade antes e depois da implantação.

- Configurar failover entre SD-WAN e MPLS para fluxos críticos, com critérios de acionamento, retorno e registro.

- Centralizar inspeção de tráfego, filtragem, logs e políticas de acesso na Sede, quando tecnicamente aplicável.

- Segmentar tráfego por classes ou VRFs, tais como usuários, administração, voz/vídeo, serviços críticos, monitoramento, backup/replicação e gerência.

- Integrar logs de borda a solução institucional de SIEM ou plataforma equivalente de monitoramento e auditoria, quando existente.

- Exigir documentação as built da rede, incluindo endereçamento, rotas, políticas, QoS, equipamentos, circuitos e contatos de suporte.

- Implantar paineis de monitoramento com disponibilidade, capacidade, erros, latência, perda, jitter e eventos de failover.

- Estabelecer rotina de revisão semestral de capacidade e relatório mensal de desempenho por localidade.

- Documentar procedimentos de crise, escalonamento técnico e comunicação institucional em caso de indisponibilidade ampla.

## VI - Estimativa das Quantidades e do Valor

### 6.1 Quantidades

Serão contratados 10 circuitos MPLS mensais, incluindo um circuito concentrador na Sede e circuitos nas demais localidades.

Também será contratado 1 link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, em grupo próprio, para replicação e redundância.

Também deverá ser avaliada, no Termo de Referência e na pesquisa de preços, a contratação ou manutenção de 3 saídas de Internet centralizadas na Sede, com capacidade combinada inicialmente estimada em 4 Gbps, preferencialmente com operadoras e rotas físicas distintas, para sustentar a arquitetura de egressão preferencial centralizada.

### 6.2 Estimativa de valor

Não se fixa estimativa final nesta minuta. Os valores históricos identificados são de objetos distintos ou parcialmente correlatos, incluindo SD-WAN, Internet dedicada, L2L e MPLS. Eles servem apenas como indícios de ordem de grandeza e não substituem pesquisa de preços atual.

A pesquisa de preços deverá comparar, quando possível, propostas ou referências para as três alternativas avaliadas: MPLS integrado à SD-WAN, links satelitais e links de Internet com VPN ponto a ponto. A comparação deverá considerar custo mensal, instalação, equipamentos, SLA, latência, prazo de reparo, suporte, disponibilidade por localidade, expansibilidade e custo operacional de gestão.

Para memória preliminar, foram levantadas 3 referências públicas para cada capacidade atualmente desejada no TRT10: 100 Mbps, 500 Mbps e 1 Gbps. A API oficial de consulta PNCP apresentou instabilidade nesta sessão, com erro de conexão, e os resultados abaixo deverão ser confirmados pela pesquisa formal quanto ao número de controle PNCP, vigência, situação do item, valor homologado/contratado e documentos de suporte.

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

Com base apenas nesses valores preliminares, a memória de cálculo inicial adota média simples dos valores mensais unitários por capacidade, conforme fórmulas abaixo:

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

### 10.3.2 Rastreabilidade das fontes consultadas

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

### 10.3.3 Referências preliminares para o grupo de link dedicado Sede-Foro 25 Gbps

Para o grupo de link dedicado Sede-Foro de 25 Gbps, a pesquisa preliminar não localizou três itens PNCP idênticos em 25 Gbps. Foram localizados precedentes compatíveis de alta capacidade, listados abaixo:

| Referência | Número do pregão/licitação e identificador | Objeto compatível | Valor informado | Uso na estimativa |
|---|---|---|---|---|
| Município de Candeias/BA | Edital 023/2026; Pregão eletrônico; PNCP-13830336000123-1-000051/2026; abertura em 13/03/2026 | Comunicação de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra óptica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos | R$ 950.560,00 | Similaridade por LAN-to-LAN, fibra dedicada, alta capacidade, rotas redundantes e equipamentos. |
| Município de Jaguariúna/SP | Edital PL-674/2024; PE 90081/2024; Pregão eletrônico; PNCP-46410866000171-1-000610/2024; abertura em 16/10/2024 | Link dedicado de acesso à Internet bidirecional e simétrico de 10 Gbps e link compartilhado de internet banda larga | R$ 4.705.844,00 | Similaridade por link dedicado 10 Gbps; escopo de Internet, não ponto-a-ponto. |
| Município de Ubarana/SP | Edital 19/2026; Pregão eletrônico; PNCP-65708786000141-1-000038/2026; abertura em 15/04/2026 | Rede LAN-to-LAN por fibra óptica dedicada, capacidade agregada de até 10 Gbps, ponto concentrador e link dedicado de acesso à Internet | R$ 184.400,00 | Similaridade por LAN-to-LAN, fibra dedicada e limite agregado de 10 Gbps. |
| TJPR | Edital PE 15/2025; PNCP 77821841000194-1-000049/2025; Pregão eletrônico | Dois links dedicados de 10 Gbps cada, BGP, Anti-DDoS e operadoras distintas para Sistema Autônomo de Internet do TJPR | R$ 187.560,00 | Similaridade por 10 Gbps, redundância e operadoras distintas; escopo de Internet/AS, não replicação ponto-a-ponto. |
| JFRS/TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Serviços de comunicação de dados dedicados e exclusivos para acesso à Internet e comunicação ponto a ponto entre sites via Metro Ethernet / LAN-to-LAN, camada 2 | Valor de item específico a confirmar na pesquisa formal | Similaridade funcional por Metro Ethernet/LAN-to-LAN e comunicação ponto a ponto entre sites; usado como referência técnica, não como preço direto. |

As referências acima não foram usadas para cálculo de média direta do item de 25 Gbps, porque os valores informados correspondem a objetos, prazos e escopos distintos. Elas foram usadas para demonstrar compatibilidade técnica de mercado e para balizar a faixa paramétrica preliminar de R$ 30.000,00 a R$ 60.000,00 mensais.

Como memória preliminar, recomenda-se reservar faixa de R$ 30.000,00 a R$ 60.000,00 mensais para o enlace dedicado Sede-Foro de 25 Gbps, adotando como ponto de partida R$ 45.000,00 mensais e R$ 540.000,00 anuais até a pesquisa formal confirmar valores para Brasília/DF. A pesquisa final deverá obter cotações específicas para 25 Gbps, baixa latência, fibra dedicada, interfaces 25GbE/SFP28, SLA, eventual dupla abordagem, equipamentos, instalação e monitoramento.

Essa memória deve ser revisada com análise crítica de outliers. Em especial, os valores de Xanxerê/SC aparentam depender de grande volume de pontos e escopo municipal próprio, podendo reduzir artificialmente a média. Recomenda-se que a pesquisa formal calcule média saneada ou mediana, compare capital/interior, considere DF/TO e preserve pelo menos 3 preços válidos por capacidade, quando disponíveis.

## VII - Justificativa para Parcelamento ou Não Parcelamento

Sugere-se adjudicação por grupo único, pois a solução depende de interoperabilidade ponta a ponta, gestão centralizada de SLA, roteamento integrado, suporte unificado e responsabilização única por indisponibilidade. O parcelamento por localidade pode gerar risco de fragmentação operacional, disputas de responsabilidade e maior complexidade de gerenciamento.

A justificativa de grupo único deverá ser confirmada pela pesquisa de mercado, demonstrando que há fornecedores capazes de atender o conjunto sem restrição indevida de competitividade. Caso a pesquisa revele baixa competitividade para todas as localidades, o parcelamento por lotes tecnicamente coerentes deverá ser reavaliado.

## VIII - Contratação Correlata ou Interdependente

A contratação é correlata ao contrato SD-WAN vigente e às contratações de Internet da Sede. A execução deverá preservar a operação atual e ser coordenada com a área de redes, segurança, operadoras atuais e fiscalização contratual.

## IX - Resultados Esperados

- maior disponibilidade da comunicação institucional;

- redução de risco de indisponibilidade total das unidades;

- centralização de segurança e saída de Internet na Sede;

- tráfego crítico com maior previsibilidade;

- separação operacional entre tráfego crítico e tráfego de Internet, com contingência cruzada entre MPLS e SD-WAN;

- simplificação de políticas de roteamento e QoS;

- fortalecimento da governança e do monitoramento da infraestrutura de rede;

- melhor padronização de políticas de segurança, inspeção de tráfego, registros e controle de acesso;

- maior previsibilidade para acesso a redes JT, Infovia, serviços institucionais e rotinas de continuidade;

- possibilidade de revisão periódica de capacidade com base em indicadores reais de consumo e desempenho;

- continuidade dos serviços judiciais e administrativos.

## X - Providências Prévias a Contratação

- Validar inventário de circuitos e endereços;

- medir uso real da SD-WAN por localidade;

- validar capacidade das 3 saídas de Internet da Sede;

- confirmar se a capacidade mínima combinada de 4 Gbps para as saídas centrais e adequada ao uso médio, picos, simultaneidade e política de contingência;

- avaliar operadoras e rotas físicas distintas para as saídas de Internet da Sede;

- definir plano de endereçamento, VRFs, roteamento e QoS;

- definir políticas de failover e retorno entre MPLS e SD-WAN;

- definir regras de tráfego local de Internet nas unidades, quando houver exceção técnica formalmente autorizada;

- definir RTO e RPO de serviços de rede relacionados à Internet, redes JT, Infovia e sistemas institucionais;

- conferir vigências contratuais e dependências;

- preparar mapa de riscos;

- elaborar pesquisa de preços;

- definir fiscais técnico, administrativo e gestor.

## XI - Contratações Correlatas e/ou Interdependentes

Contrato 131/2023 de SD-WAN, contratos de Internet/Anti-DDoS e eventuais contratos relativos a Infovia, redes JT, firewalls, monitoramento e segurança perimetral.

## XII - Impactos Ambientais

Impactos ambientais são baixos e restritos a equipamentos de rede, energia e eventuais adequações físicas. Mitigacoes: equipamentos eficientes, descarte adequado, reaproveitamento de infraestrutura existente, documentação digital e monitoramento remoto.

## XIII - Posicionamento Conclusivo

A contratação é tecnicamente viável, razoável e adequada, desde que precedida de pesquisa de preços, validação de capacidade, definição detalhada de SLA e projeto executivo. Entre as alternativas avaliadas, a Solução 1, com MPLS integrado à SD-WAN, é a mais aderente à necessidade do TRT10, pois usa o MPLS como camada privada para tráfego crítico, mantém a SD-WAN como camada preferencial de Internet, permite contingência cruzada, considera a existência de 3 saídas redundantes na Sede e fortalece disponibilidade, segurança, governança e observabilidade da rede institucional. O grupo de link dedicado Sede-Foro de 25 Gbps é tecnicamente justificável por possuir finalidade distinta da malha MPLS: replicação, backup, sincronização, baixa latência e uso do Foro como redundância da Sede.

A recomendação final é contratar MPLS para todas as localidades, em convivência com a topologia SD-WAN vigente, centralizar preferencialmente a saída de Internet na Sede, dimensionar as saídas centrais a partir de dados reais de tráfego e contratar, em grupo próprio, link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília. A conclusão permanece condicionada à pesquisa formal de mercado, validação de viabilidade por localidade, confirmação orçamentária, confirmação de preços para 25 Gbps em Brasília/DF e consolidação do Termo de Referência.

## XIV - Responsável

**Unidade: CDTEC**

Servidor responsável: Edson Mateus de Sousa

E-mail: cdtec@trt10.jus.br

Telefone: (61) 3348-1249 / 1288 / 1280 / 1188
