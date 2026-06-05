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

- O DFD indica, como premissa adotada neste ETP, que a Sede deverá dispor de 3 links de Internet redundantes, preferencialmente com operadoras e rotas físicas distintas, com capacidade combinada mínima de 4 Gbps para suportar a agregação do tráfego das unidades.

- A demanda contempla grupo próprio de link dedicado ponto-a-ponto de 25 Gbps entre o Edifício Sede e o Foro de Brasília, distinto da rede MPLS, para replicação, redundância da Sede e uso do Foro como ponto contingencial de acesso das unidades.

- A pesquisa PNCP foi atualizada em 03/06/2026, com consulta online à API pública do PNCP e download dos artefatos disponíveis para contratações semelhantes de MPLS, rede privada, comunicação de dados, SD-WAN/MPLS e interconexão por fibra.

- Em 03/06/2026, foram levantadas e documentadas referências PNCP para capacidades iguais ou tecnicamente próximas às capacidades de 100 Mbps, 500 Mbps e 1 Gbps. Os artefatos baixados foram salvos em `PNCP_REFERENCIAS_MPLS`, incluindo detalhes da contratação, itens, editais, termos de referência, estudos técnicos, mapas de preços e memórias de cálculo quando disponibilizados pelo órgão no PNCP.

- Para o novo grupo Sede-Foro, a pesquisa PNCP não localizou três itens idênticos de 25 Gbps; foram localizadas referências compatíveis de LAN-to-LAN, Metro Ethernet, fibra dedicada, datacenter, 4 Gbps, 5 Gbps e 10 Gbps, além de especificação pública com interfaces 10/25Gbps SFP28.

### Inferências analíticas

- A contratação de MPLS não substitui a SD-WAN vigente; ela compõe, desde o desenho inicial, uma arquitetura híbrida com camada privada para tráfego crítico, enquanto a SD-WAN permanece como camada preferencial para Internet.

- As capacidades MPLS requeridas correspondem às capacidades SD-WAN vigentes por localidade, como premissa de redundância total. Essa definição evita contingência parcial e subdimensionamento em incidente, sem impedir revisões futuras de capacidade baseadas em medições formais durante a execução contratual.

- A existência de 3 saídas de Internet redundantes na Sede permite centralizar a egressão de Internet e aplicar políticas uniformes de segurança.

- A capacidade mínima combinada de 4 Gbps para as 3 saídas de Internet da Sede fica definida como requisito técnico conservador, derivado da soma aproximada dos enlaces SD-WAN atuais, dos picos esperados, da simultaneidade, da política de degradação controlada e das referências de mercado analisadas.

- A arquitetura mais resiliente é a que permite contingência cruzada: MPLS pode transportar tráfego de Internet em caso de falha da SD-WAN, e SD-WAN pode transportar tráfego crítico em caso de falha do MPLS.

- A equivalência de capacidade entre MPLS e SD-WAN é premissa técnica do modelo de disponibilidade adotado. Para sistemas judiciais, autenticação, colaboração, administração remota, suporte técnico e continuidade operacional, a capacidade equivalente é aderente ao objetivo de alta disponibilidade.

- A interligação Sede-Foro deve ser tratada como link dedicado ponto-a-ponto, e não MPLS, porque sua finalidade é criar um barramento de alta capacidade entre dois pontos centrais para replicação, backup, sincronização, baixa latência e continuidade operacional.

## I - DESCRIÇÃO DA NECESSIDADE DE CONTRATAÇÃO

### 1 - Qual a necessidade da Administração (problema a ser resolvido sob a perspectiva do interesse público)?

O TRT10 necessita contratar serviços de comunicação de dados MPLS para interconectar suas unidades à Sede, de modo a prover uma camada privada, previsível, monitorável e resiliente para tráfego institucional crítico.

A necessidade decorre da dependência dos serviços digitais, da centralização de segurança e saída de Internet na Sede, da necessidade de redundância total entre camadas de conectividade e da conveniência de manter tráfego sensível em rede privada, com QoS, segregação lógica e controle de rotas. A arquitetura pretendida separa os fluxos por finalidade: MPLS para sistemas críticos e comunicação corporativa interna; SD-WAN para Internet; e uso recíproco dos meios em contingência.

A demanda considera os enlaces SD-WAN vigentes, com suas capacidades atuais e tunelamento IPSec, e define camada MPLS com a mesma capacidade nominal dos links SD-WAN em cada localidade. Com isso, assegura-se redundância total entre as camadas, de modo que a indisponibilidade de uma delas não obrigue a Administração a operar com banda nominal reduzida.

A Sede deverá operar como concentrador preferencial de saída de Internet, segurança, observabilidade e integração com redes institucionais, considerando a existência de 3 saídas de Internet redundantes. A saída local de Internet pelas unidades deverá ser tratada como exceção técnica, contingência ou fluxo formalmente autorizado, conforme política definida no projeto executivo.

A equivalência de banda entre as camadas é adotada como requisito inicial porque a separação entre tráfego crítico e não crítico tende a se tornar insuficiente durante incidentes reais: acesso ao PJe, colaboração, autenticação, suporte remoto, monitoramento, integrações, voz/vídeo e rotinas administrativas podem ocorrer simultaneamente e disputar capacidade. A equivalência de banda reduz esse risco e simplifica a operação de failover.

A necessidade também contempla interligação dedicada de 25 Gbps entre o Edifício Sede e o Foro de Brasília. O Foro deverá ser preparado como ponto de replicação e redundância da Sede, apto a receber tráfego de sincronização, backup, replicação de dados, serviços de continuidade e, conforme projeto executivo, acesso contingencial das demais unidades quando a Sede estiver indisponível ou degradada. Esse enlace deve ser contratado como link dedicado ponto-a-ponto, LAN-to-LAN, Metro Ethernet, clear channel, E-Line, E-LAN ou tecnologia equivalente, e não como MPLS.

### 2 - A necessidade decorre de determinação legal?

Não há obrigação legal de adotar MPLS como tecnologia. A contratação se fundamenta na necessidade administrativa de assegurar continuidade, disponibilidade e segurança da comunicação de dados. A Lei nº 14.133/2021 orienta o planejamento e a estruturação dos artefatos; a ENTIC-JUD 2021-2026 orienta a governança de TIC no Poder Judiciário.

### 3 - A necessidade é contínua (resulta em demanda permanente, habitual ou, ao menos, intermitente ao longo de vários anos)? Explique.

A necessidade possui natureza continuada, pois a comunicação entre unidades e Sede é indispensável ao funcionamento permanente dos serviços judiciais e administrativos.

A necessidade resulta em demanda permanente e habitual ao longo de vários anos, pois a conectividade entre Sede, Foro de Brasília, Prédio de Apoio, fóruns e varas é condição operacional para prestação jurisdicional, comunicação administrativa, acesso a sistemas, autenticação, segurança, monitoramento, suporte técnico, videoconferência, replicação de dados e continuidade de serviços. A contratação deverá ser estruturada como serviço continuado de telecomunicações/TIC, com vigência inicial de 60 meses, prestação ininterrupta, monitoramento 24x7, manutenção, suporte, níveis mínimos de serviço e mecanismos de glosa durante toda a execução.

## II - PREVISÃO NO PLANO ESTRATÉGICO INSTITUCIONAL, PLANO DE LOGÍSTICA SUSTENTÁVEL (PLS) E PLANO DE CONTRATAÇÕES ANUAL (PCA)

### 1 - A demanda alinha-se aos objetivos do Plano Estratégico Institucional (RA 35/2021-TRT10)?

A demanda se alinha diretamente ao Objetivo Estratégico 10 - Aprimorar a governança de TIC e a proteção de dados, pois amplia a disponibilidade, a segurança, a rastreabilidade, a governabilidade e a continuidade da infraestrutura de comunicação de dados. A contratação também contribui para a razoável duração do processo e para o aperfeiçoamento da gestão administrativa, ao reduzir riscos de indisponibilidade de sistemas judiciais, autenticação, videoconferência, suporte remoto, monitoramento e serviços corporativos.

| Nº | Objetivo estratégico | Alinhamento |
|---|---|---|
| 3 | Garantir a razoável duração do processo | Contribuição indireta pela continuidade dos sistemas judiciais e serviços digitais. |
| 7 | Aperfeiçoar a Governança, a Gestão Estratégica e a Gestão Administrativa | Contribuição indireta pela padronização de operação, monitoramento, SLA e gestão de rede. |
| 10 | Aprimorar a governança de TIC e a proteção de dados | Alinhamento direto, por fortalecer disponibilidade, segurança, redundância e governança de TIC. |

### 2 - A demanda observa o Plano de Logística Sustentável (PLS)?

Sim. Há alinhamento com o uso eficiente de recursos de TIC, redução de deslocamentos por indisponibilidade técnica, melhor uso de serviços digitais, monitoramento remoto, documentação digital, reaproveitamento de infraestrutura existente e racionalização da infraestrutura de comunicação.

### 3 - A demanda está prevista no Plano de Contratações Anual (PCA)?

A providência administrativa fica definida: a contratação deverá constar do PCA/SIGPLAC antes da publicação do edital. Caso a demanda ainda não esteja cadastrada, deverá ser incluída como demanda superveniente, com justificativa vinculada à continuidade dos serviços de comunicação institucional, à redundância total da arquitetura SD-WAN/MPLS e à interligação dedicada Sede-Foro para replicação e contingência.

## III - REQUISITOS DA CONTRATAÇÃO E CRITÉRIOS DE SUSTENTABILIDADE E ACESSIBILIDADE

### 1 - Quais são os requisitos necessários e suficientes para a escolha da solução?

Os requisitos necessários e suficientes são os requisitos funcionais, técnicos, operacionais, de segurança, desempenho, disponibilidade, suporte, sustentabilidade e fiscalização descritos neste item. Eles são definidos por desempenho e resultado, sem indicação de marca, fabricante ou modelo específico.

#### 1.1 - Quais são as especificações mínimas do objeto da contratação para que a necessidade da Administração possa ser satisfatoriamente atendida?

Para que a necessidade da Administração seja atendida de forma satisfatória, o objeto deverá contemplar uma solução continuada de comunicação de dados corporativa, em rede privada MPLS L3 VPN ou tecnologia funcionalmente equivalente, capaz de interconectar todas as unidades do TRT10 à Sede, coexistir com a SD-WAN vigente e permitir operação com preferência de tráfego e contingência cruzada.

As especificações mínimas abaixo constituem a definição técnica do ETP e deverão ser reproduzidas no Termo de Referência e no instrumento contratual, sem redução de capacidade, disponibilidade, segurança, suporte ou critérios de aceite.

#### a) Escopo mínimo do serviço

A contratação deverá incluir, no mínimo:

- prestação de serviço continuado de comunicação de dados por rede privada corporativa MPLS L3 VPN ou tecnologia equivalente;

- interconexão da Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga, Foro de Palmas, Vara do Gama, Foro de Araguaína, Vara de Gurupi, Vara de Dianópolis e Vara de Guaraí;

- interligação dedicada ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, em grupo próprio, por fibra óptica, LAN-to-LAN/Metro Ethernet ou tecnologia equivalente;

- fornecimento, instalação, configuração, ativação, operação, manutenção e suporte dos circuitos;

- fornecimento dos CPEs, roteadores, modems, transceptores, fontes, cabos, licenças e demais elementos necessários à prestação do serviço, quando não forem expressamente indicados como responsabilidade do TRT10;

- monitoramento 24x7 dos circuitos e equipamentos sob responsabilidade da contratada;

- central de atendimento, registro de chamados, escalonamento técnico e relatórios mensais;

- documentação técnica inicial, documentação as built e atualização após mudanças relevantes.

#### b) Arquitetura mínima

A solução deverá adotar topologia lógica com a Sede como concentrador preferencial, mantendo todas as demais localidades interconectadas à Sede por MPLS. A Sede deverá permanecer como ponto preferencial de saída de Internet e de aplicação das políticas de segurança, considerando a existência de 3 saídas de Internet redundantes.

A arquitetura deverá permitir:

- uso preferencial do MPLS para tráfego crítico, sistemas institucionais, autenticação, serviços corporativos internos, administração, monitoramento e integrações;

- uso preferencial da SD-WAN para tráfego de Internet e serviços externos;

- uso do MPLS para tráfego de Internet em contingência da SD-WAN, com egressão preferencial pela Sede;

- uso da SD-WAN para tráfego crítico em contingência do MPLS;

- retorno controlado ao caminho preferencial após normalização;

- capacidade agregada na Sede para suportar, em condições normais e em regime de contingência controlada, a egressão de Internet das unidades;

- uso do Foro de Brasília como ponto de replicação e redundância da Sede, com enlace dedicado de 25 Gbps entre os dois prédios;

- redirecionamento contingencial do acesso das unidades ao Foro de Brasília, conforme rotas, segurança, serviços disponíveis e critério de acionamento definidos no projeto executivo;

- convivência com firewalls, roteadores, controladores SD-WAN, redes JT, Infovia e demais componentes indicados pela CDTEC.

#### c) Capacidades mínimas definidas

As capacidades mínimas da contratação ficam definidas conforme o dimensionamento abaixo, considerando criticidade, simultaneidade, crescimento esperado, redundância total e equivalência com as capacidades SD-WAN vigentes:

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

As 3 saídas de Internet da Sede ficam definidas com capacidade mínima combinada de 4 Gbps em operação normal, distribuídas preferencialmente entre operadoras distintas e com rotas físicas diversas quando tecnicamente viável. A contratação deverá preservar essa capacidade mínima combinada para egressão centralizada, segurança, contingência e absorção temporária de tráfego das unidades em caso de falha da SD-WAN local.

A equivalência entre MPLS e SD-WAN não significa duplicidade indevida de objeto, pois as camadas possuem papéis técnicos complementares: a SD-WAN utiliza transporte por Internet dedicada, túneis, orquestração e políticas de acesso; o MPLS fornece rede privada corporativa, isolamento lógico, QoS e caminho controlado para interconexão. A duplicação de capacidade nominal decorre da finalidade de redundância integral, e não da repetição desnecessária de uma mesma solução.

O link dedicado de 25 Gbps Sede-Foro possui natureza distinta da rede MPLS das localidades. Ele não é enlace MPLS de filial, mas circuito de alta capacidade entre dois pontos centrais, voltado a replicação, continuidade, contingência e baixa latência. Por isso, deverá compor grupo próprio na modelagem da contratação e na pesquisa de preços.

#### c.1) Itens complementares definidos para a contratação

A contratação contempla os seguintes itens complementares, que integram o escopo mínimo da solução:

- 3 links de Internet centralizados e redundantes na Sede, com capacidade mínima combinada de 4 Gbps, preferencialmente com operadoras e rotas físicas distintas;

- equipamentos de borda, roteadores, CPEs ou integração com firewalls existentes, sem vinculação a marca específica;

- serviços de implantação, configuração, testes de aceite, documentação e transferência de conhecimento;

- monitoramento 24x7 dos links, alertas de indisponibilidade e relatórios mensais de SLA;

- suporte técnico 24x7, com início de atendimento em até 30 minutos para falha crítica, até 1 hora para degradação relevante e até 4 horas úteis para chamados ordinários;

- endereçamento, roteamento, QoS, segmentação e políticas de segurança documentadas no projeto executivo e na documentação as built.

#### d) Roteamento, segregação e QoS

A solução deverá suportar roteamento controlado e integração com a infraestrutura existente do TRT10 por OSPF como protocolo preferencial para integração interna e por BGP quando houver necessidade de troca de rotas com bordas de operadoras, datacenter, Internet ou ambiente autônomo. O roteamento estático somente será aceito para enlaces simples, rotas de contingência, rotas de gerenciamento ou situações em que a área técnica do TRT10 aprove formalmente sua simplicidade e menor risco. Ficam definidos como requisitos mínimos: anúncio apenas das redes autorizadas pelo TRT10; métricas que priorizem MPLS para tráfego crítico e SD-WAN para Internet em operação normal; failover automático ou semiautomático documentado; retorno controlado ao caminho preferencial após estabilização mínima de 15 minutos; filtros contra rotas indevidas; e mecanismos para prevenção de loops.

A solução deverá prover isolamento lógico do tráfego do TRT10, por VRF ou mecanismo equivalente, e suportar QoS com classes de serviço configuráveis. Ficam definidas, no mínimo, as seguintes classes de tráfego:

- tráfego crítico de sistemas judiciais, autenticação, serviços internos e administração;

- tráfego sensível a tempo, como voz, vídeo e colaboração, quando aplicável;

- tráfego corporativo administrativo;

- tráfego de melhor esforço.

As marcações e reservas mínimas de QoS ficam definidas assim: classe crítica, com DSCP AF31/CS3 ou marcação equivalente e reserva mínima de 35% da banda; voz/vídeo institucional, com DSCP EF/AF41 ou marcação equivalente e reserva mínima de 20%; tráfego corporativo administrativo, com DSCP AF21 ou equivalente e reserva mínima de 25%; monitoramento, gerenciamento e backup operacional, com reserva mínima de 5%; e melhor esforço, com uso da banda remanescente. As filas poderão aproveitar banda ociosa entre classes, mas, em congestionamento, a classe crítica e voz/vídeo terão prioridade de encaminhamento e menor descarte.

#### e) Disponibilidade, desempenho e suporte

A solução deverá observar disponibilidade mensal mínima de 99,90% para a Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga e Foro de Palmas, e de 99,70% para Gama, Araguaína, Gurupi, Dianópolis e Guaraí. O link dedicado Sede-Foro de 25 Gbps deverá observar disponibilidade mensal mínima de 99,95%.

Ficam definidos os níveis mínimos de serviço:

- início de atendimento: até 30 minutos para indisponibilidade total, até 1 hora para degradação severa e até 4 horas úteis para chamados ordinários;

- prazo de reparo: até 4 horas para Sede, Foro de Brasília e link dedicado Sede-Foro; até 6 horas para demais localidades do DF; até 8 horas para localidades do Tocantins;

- manutenção programada: janela preferencial das 22h às 6h, com aviso prévio mínimo de 5 dias úteis, plano de rollback e autorização do TRT10 quando houver risco de impacto;

- fórmula de disponibilidade: disponibilidade mensal = ((tempo total mensal - tempo indisponível imputável à contratada) / tempo total mensal) x 100;

- hipóteses de glosa: 5% da mensalidade do circuito quando a disponibilidade ficar abaixo da meta e até 0,5 ponto percentual abaixo dela; 10% quando a queda exceder 0,5 ponto e for até 1 ponto percentual; 20% quando a queda exceder 1 ponto percentual; e 30% quando houver indisponibilidade superior a 24 horas acumuladas no mês, sem prejuízo de sanções;

- aferição: relatórios mensais da contratada, registros de monitoramento, chamados, evidências da fiscalização técnica e testes sob demanda;

- desempenho mínimo: perda média de pacotes inferior a 1%; jitter médio inferior a 30 ms para tráfego sensível; latência média mensal até a Sede inferior a 30 ms para localidades no DF e inferior a 80 ms para localidades no Tocantins, ressalvadas medições afetadas por falha comprovada em infraestrutura do contratante ou evento de força maior.

#### f) Implantação, testes e aceite

A contratada deverá apresentar plano de implantação antes da ativação dos circuitos, contendo cronograma, pré-requisitos, responsáveis, janelas de mudança, testes, riscos e plano de rollback. A implantação deverá ocorrer preferencialmente por fases, iniciando pela Sede e pelas unidades de maior criticidade.

O aceite mínimo por localidade deverá verificar:

- identificação do circuito;

- banda contratada;

- conectividade com a Sede;

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

Sim. Fica exigida garantia contratual do objeto durante toda a vigência da contratação, complementar às garantias legais aplicáveis, abrangendo o funcionamento dos circuitos, CPEs, roteadores, modems, fontes, transceptores, licenças, configurações, monitoramento, suporte técnico e demais componentes fornecidos ou operados pela contratada.

A garantia do objeto deverá assegurar que falhas, defeitos, indisponibilidades ou degradações imputáveis à contratada sejam corrigidos sem ônus adicional para o TRT10, observados os prazos de atendimento, reparo, disponibilidade e demais níveis mínimos de serviço definidos neste ETP e reproduzidos no instrumento contratual.

Essa garantia do objeto não substitui a garantia de execução contratual eventualmente exigida, nem afasta a aplicação de glosas, sanções, obrigações de reparo, substituição de equipamentos, manutenção corretiva ou demais medidas previstas no instrumento contratual.

### 1.1.3 A garantia contratual do objeto é compatível com as práticas de mercado?

Sim. A exigência é compatível com as práticas de mercado para serviços continuados de telecomunicações e comunicação de dados, nos quais é usual que a contratada se responsabilize pela disponibilidade do circuito, funcionamento dos equipamentos sob sua gestão, manutenção corretiva, substituição de componentes defeituosos, suporte técnico, monitoramento e cumprimento de SLA durante toda a vigência contratual.

Também é prática usual que equipamentos fornecidos em comodato, locação, cessão de uso ou como parte indissociável do serviço sejam mantidos pela contratada, sem transferência de responsabilidade técnica ao contratante, salvo quando houver dano causado por uso indevido, caso fortuito, força maior ou responsabilidade expressamente atribuída ao contratante no contrato.

A compatibilidade com o mercado foi verificada em processos públicos recentes consultados no PNCP e nos artefatos baixados para a pasta `PNCP_REFERENCIAS_MPLS`. Em 05/06/2026, foram realizadas consultas online adicionais à API pública do PNCP pelos termos "MPLS garantia suporte manutenção equipamentos SLA" e "comunicação de dados comodato substituição equipamentos disponibilidade"; essas buscas específicas não retornaram novos resultados, razão pela qual a análise abaixo utiliza como evidência os processos similares já localizados e documentados por consulta PNCP anterior, com arquivos oficiais baixados.

| Processo semelhante | Objeto aderente | Requisitos identificados no edital/TR/ETP | Aderência ao requisito deste ETP |
|---|---|---|---|
| CODEVASF - Companhia de Desenvolvimento dos Vales do São Francisco e do Parnaíba; Pregão Eletrônico nº 90003/2025; Processo nº 59500002693202462; PNCP nº 00399857000126-1-000049/2025 | Rede corporativa WAN com tecnologia MPLS, interligando Administração Central e Superintendências Regionais, incluindo instalação e configuração de equipamentos, enlaces de comunicação e gerenciamento proativo contra falhas. | O Termo de Referência prevê que a contratada forneça, dimensione, instale, configure, monitore, opere, gerencie e mantenha roteadores, modems, estações de gerenciamento, meios de transmissão e demais recursos necessários. Os equipamentos são de propriedade da contratada, que responde pelo suporte técnico. O mesmo processo admite subcontratação da última milha, mas mantém a responsabilidade integral da contratada pelo funcionamento e disponibilidade, inclusive para instalação, manutenção, substituição, teste e configuração dos equipamentos da rede WAN IP/MPLS. | Confirma a prática de transferir à contratada a responsabilidade pela disponibilidade da solução, manutenção dos enlaces, suporte dos equipamentos, substituição de componentes e monitoramento, sem repassar ao órgão a gestão técnica dos CPEs/roteadores. |
| CODEVASF - Pregão Eletrônico nº 90003/2025; PNCP nº 00399857000126-1-000049/2025 | Mesma rede WAN IP/MPLS. | O Anexo de Indicadores de Níveis de Serviço trata a disponibilidade do enlace incluindo o CPE, calcula o Índice de Disponibilidade Mensal, exige aferição mensal, relatórios de níveis de serviço e disponibilidade mínima de 99,7% para a Administração Central e 99,5% para as demais unidades. | Demonstra que a garantia do objeto, em serviços MPLS, normalmente abrange o circuito e o equipamento de borda, com SLA mensal e consequência operacional para indisponibilidade. |
| ANCINE - Agência Nacional do Cinema; Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025 | Solução de acesso à Internet e rede de dados privada MPLS com SD-WAN. | O Anexo de Especificações Técnicas define assistência técnica com identificação e solução de incidentes, instalação/desinstalação de equipamentos, substituição de componentes fornecidos que apresentem falhas, abertura de chamados por 0800/portal e atendimento 24x7x365. O suporte técnico deve prevenir e solucionar problemas, alterar configurações, atualizar componentes de software/hardware e recuperar indisponibilidade total em até 4 horas. | Confirma que, em serviços MPLS/SD-WAN, é prática exigir garantia operacional durante a vigência, com suporte permanente, manutenção lógica e física, substituição de componentes e SLA de recuperação. |
| Município de Chapecó/SC; Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026 | Serviço de telecomunicação com transporte de dados em tecnologia MPLS por fibra óptica, links dedicados de Internet e links temporários móveis. | O Termo de Referência prevê hardware em comodato, substituição obrigatória em caso de falha física, disponibilidade mínima, MTTR de 4 horas para backbone principal e circuitos MPLS, monitoramento por interface gráfica e garantia contratual dos serviços. | Confirma a prática de equipamentos sob responsabilidade da contratada, fornecidos como parte do serviço, com substituição, manutenção, monitoramento e prazo de restabelecimento definidos. |
| Município de Brusque/SC; Pregão Eletrônico nº 11/2026; Processo nº 33/2026; PNCP nº 83102343000194-1-000064/2026 | Serviço continuado crítico de TIC em IaaS, com hospedagem, suporte, disponibilidade e continuidade operacional. | Embora não seja MPLS, o Termo de Referência estabelece garantia da contratação, SLA de disponibilidade mínima, suporte técnico, manutenção preventiva e corretiva durante toda a vigência, tratamento prioritário de falhas/indisponibilidades e descontos por descumprimento de SLA. Em resposta a impugnação, o processo registra a importância de SLA único, suporte, instalação, manutenção e substituição de componentes em cenários críticos. | Referência auxiliar de mercado de TIC: reforça que serviços continuados críticos usualmente concentram na contratada a garantia de disponibilidade, manutenção, suporte e continuidade durante a vigência. |

Esses precedentes demonstram que a exigência de garantia contratual do objeto não cria ônus atípico nem requisito estranho ao mercado. Ao contrário, ela reflete a forma ordinária de contratação de serviços corporativos de comunicação de dados: a Administração contrata disponibilidade, desempenho, suporte e continuidade da solução, e a contratada assume a responsabilidade técnica pelos meios necessários à prestação do serviço, incluindo enlaces, CPEs, roteadores, modems, transceptores, licenças, configurações, monitoramento, manutenção e substituição de componentes sob sua gestão.

Assim, para esta contratação, a garantia contratual do objeto fica definida como obrigação de manter os circuitos MPLS, o link dedicado Sede-Foro de 25 Gbps, os equipamentos fornecidos, as configurações, o monitoramento e o suporte em condições regulares de funcionamento durante toda a vigência contratual. Falhas, defeitos, degradações, indisponibilidades ou incompatibilidades imputáveis à contratada deverão ser corrigidos sem custo adicional ao TRT10, observados os prazos de atendimento, reparo, disponibilidade, desempenho e glosas previstos neste ETP.

#### 1.2 - Quais são as características mínimas do modelo de execução da contratação para que a necessidade da Administração possa ser satisfatoriamente atendida?

O modelo de execução deverá permitir implantação controlada, operação continuada, fiscalização objetiva e preservação da conectividade vigente durante a transição. Para tanto, deverá contemplar, no mínimo:

- emissão de ordem de serviço para início da execução;

- apresentação de plano de implantação pela contratada em até 10 dias corridos após a emissão da ordem de serviço;

- levantamento inicial de pré-requisitos por localidade, incluindo acesso físico, energia, espaço, passagem de cabos, infraestrutura de fibra, CPEs e pontos de conexão;

- implantação por fases, iniciando pela Sede e pelas unidades de maior criticidade ou maior capacidade;

- convivência com a SD-WAN vigente durante a implantação do MPLS, evitando interrupção dos serviços institucionais;

- entrega de projeto executivo antes da ativação, contendo desenho lógico, rotas, endereçamento, políticas de preferência, QoS, contingência, responsabilidades e rollback;

- ativação e teste de aceite por localidade;

- operação assistida após a ativação dos circuitos, com acompanhamento de estabilidade, roteamento, desempenho, chamados e relatórios;

- monitoramento 24x7 dos circuitos e equipamentos sob responsabilidade da contratada;

- disponibilização de central de atendimento, portal ou canal equivalente de abertura de chamados, telefone e e-mail;

- relatório mensal com disponibilidade, indisponibilidades, chamados, causa raiz, tempos de atendimento, reparos, manutenções, desempenho e eventos de contingência;

- reuniões técnicas de acompanhamento, quando solicitadas pela fiscalização;

- documentação as built e atualização documental sempre que houver mudança relevante;

- execução de manutenções programadas apenas mediante comunicação e autorização prévia, quando houver risco de impacto;

- aplicação de glosas e sanções em caso de descumprimento dos níveis de serviço definidos neste ETP e no contrato.

O modelo deverá prever recebimento provisório por localidade após ativação e teste, e recebimento definitivo após período de observação, saneamento de pendências e validação pela fiscalização técnica.

A implantação será faseada para preservar a continuidade da SD-WAN vigente e reduzir risco operacional:

| Fase | Escopo | Objetivo |
|---|---|---|
| 1 | Sede | Implantar concentrador principal, validar saídas centrais de Internet, roteamento, segurança e saída preferencial |
| 2 | Gama e Taguatinga | Atender unidades com maior sensibilidade contratual histórica |
| 3 | Prédio de Apoio e Palmas | Integrar unidades de demanda intermediária |
| 4 | Araguaína, Gurupi, Dianópolis e Guaraí | Concluir capilaridade MPLS e contingência das unidades remotas |
| 5 | Operação assistida | Validar failover, QoS, desempenho, monitoramento e documentação final |

### 1.2.1 Será admitida a subcontratação? Se sim, apresente as justificativas, bem como indique seus limites e partes do objeto.

Sim. Fica admitida subcontratação apenas para atividades acessórias de infraestrutura local, lançamento de fibra, obras civis leves, passagem de cabos, adequações físicas, vistorias, instalação de último trecho e atendimento de campo, mantendo a contratada principal integralmente responsável pela prestação do serviço, pelo SLA, pela segurança, pela documentação, pelo suporte, pela operação e pela manutenção da solução.

A justificativa para admitir subcontratação limitada decorre da natureza distribuída da solução, que envolve localidades no Distrito Federal e no Tocantins, podendo exigir equipes locais, acesso à infraestrutura regional, serviços de campo e atividades acessórias que não representam a gestão técnica central do serviço de comunicação de dados.

Não deverá ser admitida subcontratação que transfira a responsabilidade principal pela rede privada corporativa, pela gerência dos circuitos, pelo cumprimento do SLA, pelo atendimento ao TRT10, pela segurança das informações ou pela integração técnica com a arquitetura MPLS/SD-WAN. A contratada principal deverá responder integralmente por atos, omissões, falhas e atrasos de suas subcontratadas.

### 1.2.2 Os riscos ou características da contratação tornam recomendável a exigência de garantia de execução contratual?

Sim. Fica definida a exigência de garantia de execução contratual, considerando o valor estimado, a criticidade do serviço, a quantidade de localidades, a necessidade de implantação coordenada, o fornecimento de equipamentos, a dependência de SLA e o impacto operacional de eventual inadimplemento.

A garantia de execução contratual fica definida em 5% do valor anual estimado da contratação, admitidas as modalidades previstas na Lei nº 14.133/2021, com manutenção durante toda a vigência contratual e 90 dias após seu encerramento. A garantia deverá cobrir atraso de implantação, indisponibilidade de circuitos, falha de integração MPLS/SD-WAN, descumprimento de níveis de serviço, danos causados à Administração, obrigações trabalhistas/previdenciárias quando aplicáveis e multas não pagas. A contratada deverá recompor a garantia em até 10 dias úteis quando houver utilização parcial ou acréscimo contratual.

### 3.1 Requisitos do objeto

Requisitos mínimos definidos:

- rede MPLS L3 VPN ou tecnologia equivalente de rede privada corporativa, desde que preserve isolamento lógico, QoS e roteamento controlado;

- interconexão das demais localidades à Sede;

- fornecimento de CPEs, modems, transceptores, cabos, licenças e demais itens necessários;

- compatibilidade com roteamento dinâmico, preferencialmente OSPF ou BGP, conforme projeto executivo;

- suporte a QoS para classes de tráfego crítico, administrativo, voz/vídeo, monitoramento e melhor esforço;

- suporte a VRF ou segregação lógica equivalente;

- capacidade simétrica mínima conforme tabela de dimensionamento;

- monitoramento 24x7, portal de chamados e relatórios mensais;

- SLA de disponibilidade mínima de 99,90% para Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga e Foro de Palmas; 99,70% para Gama, Araguaína, Gurupi, Dianópolis e Guaraí; e 99,95% para o link dedicado Sede-Foro de 25 Gbps.

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

Fica admitida subcontratação apenas para atividades acessórias de infraestrutura local, lançamento de fibra, obras civis leves e atendimento de campo, mantendo a contratada principal integralmente responsável pela prestação do serviço e pelo SLA.

### 3.4 Sustentabilidade e acessibilidade

Exigir equipamentos com eficiência energética compatível com o mercado, descarte ambientalmente adequado de equipamentos substituídos, redução de deslocamentos por meio de monitoramento remoto e atendimento as normas trabalhistas, ambientais e de segurança aplicáveis.

### 3.4.1 Quais os critérios e práticas de sustentabilidade e acessibilidade cabíveis ou exigíveis, no caso?

Considerando a natureza da contratação, os critérios de sustentabilidade e acessibilidade cabíveis devem ser compatibilizados com serviços continuados de telecomunicações, comunicação de dados, infraestrutura de rede e atendimento técnico. São critérios e práticas recomendáveis:

- priorização de equipamentos com eficiência energética compatível com as práticas de mercado;

- uso de equipamentos, fontes e acessórios em conformidade com normas técnicas e regulamentos aplicáveis;

- descarte ambientalmente adequado de equipamentos, cabos, fontes, baterias, embalagens e demais resíduos sob responsabilidade da contratada;

- redução de deslocamentos mediante monitoramento remoto, abertura remota de chamados, diagnóstico remoto e atendimento presencial apenas quando necessário;

- consolidação de relatórios em meio digital;

- reaproveitamento de infraestrutura existente sempre que tecnicamente possível e autorizado;

- adoção de janelas de manutenção planejadas para reduzir retrabalho e deslocamentos;

- observância de normas de segurança do trabalho nas atividades de instalação, lançamento de cabos, acesso a salas técnicas, racks, forros, shafts e demais ambientes;

- garantia de que instalações físicas, passagem de cabos e acomodação de equipamentos não prejudiquem rotas de circulação, acessibilidade física, segurança predial ou sinalização;

- atendimento a requisitos de sigilo, proteção de informações e minimização de acesso a dados de rede;

- preferência por documentação digital, as built eletrônico e relatórios mensais em formato pesquisável.

### 3.4.2 Caso não aplicáveis critérios de sustentabilidade e acessibilidades, apresentar as justificativas.

Os critérios de sustentabilidade e acessibilidade são aplicáveis de forma proporcional ao objeto. Não se trata de contratação de obra, aquisição massiva de bens permanentes ou solução diretamente voltada ao atendimento ao público, razão pela qual alguns critérios típicos de obras, mobiliário, edificações, materiais de consumo ou acessibilidade de interfaces digitais podem não ser pertinentes.

Assim, os critérios devem se concentrar na eficiência energética dos equipamentos, descarte ambientalmente adequado, redução de deslocamentos, segurança em instalações, documentação digital, reaproveitamento de infraestrutura e preservação da acessibilidade física dos ambientes onde houver instalação de equipamentos ou cabos.

### 3.4.3 Foi consultado o Guia de Contratações Sustentáveis da Justiça do Trabalho (CSJT), ou, subsidiariamente, o Guia Nacional de Contratações Sustentáveis (AGU)?

Fica registrada, para fins de instrução, a utilização dos critérios de sustentabilidade compatíveis com o Guia de Contratações Sustentáveis da Justiça do Trabalho (CSJT) e, subsidiariamente, com o Guia Nacional de Contratações Sustentáveis da AGU. Aplicam-se ao objeto os critérios proporcionais de eficiência energética dos equipamentos, descarte ambientalmente adequado, documentação digital, redução de deslocamentos por monitoramento remoto, reaproveitamento de infraestrutura existente e preservação da acessibilidade física nas áreas de instalação.

### 3.5 Esclareça se a solução escolhida demandará a contratação de serviços de manutenção e/ou assistência técnica.

Sim. A solução escolhida demandará manutenção e assistência técnica durante toda a vigência contratual, mas tais atividades deverão compor o próprio objeto da contratação, sem necessidade de contratação apartada, salvo se a Administração optar por escopo excepcional não previsto neste ETP.

A manutenção e assistência técnica deverão abranger, no mínimo:

- manutenção corretiva dos circuitos, acessos, CPEs, roteadores, modems, fontes, transceptores, cabos e demais componentes sob responsabilidade da contratada;

- substituição de equipamentos defeituosos ou degradados sob responsabilidade da contratada;

- suporte técnico para indisponibilidade, degradação, perda de pacotes, latência anormal, falha de roteamento, falha de QoS e falha de monitoramento;

- atendimento remoto e presencial quando necessário;

- monitoramento 24x7;

- abertura, acompanhamento, escalonamento e encerramento de chamados;

- manutenções programadas previamente comunicadas e autorizadas quando houver risco de impacto;

- atualização da documentação técnica após mudanças relevantes.

Assim, os custos de manutenção, suporte e assistência técnica deverão estar incorporados aos valores mensais dos circuitos e do link dedicado Sede-Foro, evitando lacunas de responsabilidade durante a execução contratual.

### 3.6 No caso de compras, será necessário analisar amostras?

Não se aplica como regra principal, pois o objeto pretendido é serviço continuado de comunicação de dados, e não compra isolada de bens. Não serão exigidas amostras físicas como critério ordinário de aceitação da proposta. Equipamentos, CPEs, licenças e acessórios integram a prestação do serviço e serão avaliados por requisitos funcionais, documentação técnica, projeto executivo, testes de ativação e aceite por localidade.

Para os equipamentos fornecidos como parte do serviço, a licitante deverá apresentar catálogos, datasheets ou declarações técnicas suficientes para comprovar compatibilidade com as capacidades contratadas, interfaces, roteamento, QoS, monitoramento, energia e instalação, sem direcionamento por marca ou modelo.

### 3.7 No caso de serviços, será necessário vistoria prévia do local da execução dos serviços?

A vistoria prévia será facultativa, e não obrigatória, podendo ser substituída por declaração da licitante de que conhece as condições locais e assume responsabilidade pela formulação de sua proposta. Essa definição reduz risco de restrição indevida à competitividade e preserva a possibilidade de participação de fornecedores que consigam estimar custos por documentação, mapas, endereços, inventário técnico e informações disponibilizadas no edital.

A vistoria facultativa poderá ser disponibilizada para as localidades do TRT10, mediante agendamento, especialmente quando houver necessidade de verificar entrada de fibra, sala técnica, rack, energia, infraestrutura de passagem, espaço para CPE, restrições prediais ou condições de acesso. A não realização de vistoria não deverá justificar pedidos posteriores de acréscimo de custos, desde que o edital disponibilize informações mínimas suficientes sobre as localidades e condições de execução.

### 3.8 É necessária autorização do poder público para o exercício da atividade a ser contratada (habilitação jurídica)?

Sim. Por se tratar de serviço de telecomunicações/comunicação de dados, deverá ser exigida, quando aplicável, comprovação de autorização, outorga, licença ou instrumento regulatório pertinente para prestação dos serviços, nos termos da regulamentação setorial vigente.

Em princípio, a contratada deverá demonstrar regularidade para prestação de Serviço de Comunicação Multimídia (SCM) ou outro enquadramento regulatório aplicável ao serviço efetivamente ofertado, junto a Anatel, diretamente ou por meio de arranjo juridicamente admitido. Caso a licitante utilize infraestrutura, autorização ou serviços de terceiros, deverá demonstrar que tal arranjo não transfere ao TRT10 riscos de irregularidade regulatória, descontinuidade ou ausência de responsabilidade contratual.

A exigência deverá ser redigida de forma funcional e proporcional, evitando restringir indevidamente a competição, mas assegurando que a futura contratada esteja apta a prestar os serviços de telecomunicações objeto da contratação.

### 3.9 Será necessário exigir qualificações econômico-financeiras adicionais?

Sim. Ficam exigidas as qualificações econômico-financeiras ordinárias previstas na legislação e no edital, incluindo balanço patrimonial e demonstrações contábeis do último exercício social, quando aplicáveis, e comprovação de índices contábeis compatíveis com contratação continuada essencial. Quando algum índice mínimo não for atendido, admitir-se-á comprovação alternativa de patrimônio líquido mínimo de 10% do valor estimado anual da contratação, observado o limite legal e a proporcionalidade. Não se exige capital social mínimo cumulativo com patrimônio líquido mínimo. Os riscos econômico-financeiros serão complementados por garantia de execução contratual de 5%, pagamentos mensais condicionados ao aceite, glosas por descumprimento de SLA e fiscalização contratual.

### 3.10 Será necessário exigir qualificações técnicas técnico-operacional e técnico-profissional especiais?

Sim. Fica exigida qualificação técnico-operacional compatível com a complexidade do objeto, especialmente porque a solução envolve rede privada corporativa, múltiplas localidades, SLA, monitoramento, suporte, roteamento, QoS, integração com SD-WAN e continuidade de serviços críticos.

A qualificação técnico-operacional deverá comprovar experiência anterior da licitante em prestação de serviço semelhante, contemplando, no mínimo:

- comunicação de dados corporativa por MPLS, L3VPN, L2L, rede privada gerenciada ou tecnologia equivalente;

- atendimento a, no mínimo, 5 localidades ou 50% do quantitativo de localidades do TRT10, admitido somatório de atestados quando tecnicamente compatíveis;

- operação, monitoramento e suporte de circuitos;

- cumprimento de níveis de serviço e atendimento a chamados;

- fornecimento ou gestão de CPEs/roteadores;

- implantação, configuração, manutenção e documentação de rede.

A exigência é proporcional ao objeto, não exige identidade absoluta com a solução do TRT10 e não impõe marca, fabricante ou modelo. Os quantitativos mínimos ficam definidos em experiência anterior com rede corporativa, telecomunicações ou comunicação de dados em pelo menos 5 localidades ou 50% do quantitativo do TRT10, e com pelo menos 1 enlace de 1 Gbps ou superior, admitida comprovação por somatório de atestados quando houver compatibilidade técnica e temporal.

Quanto à qualificação técnico-profissional, fica exigida indicação de responsável técnico ou equipe técnica com experiência em redes corporativas, telecomunicações, roteamento, segurança de rede ou operação de serviços de comunicação de dados. A comprovação poderá ocorrer por currículo, certificação técnica, vínculo profissional, registro profissional quando aplicável ou declaração da licitante, sem exigência de certificação de fabricante específico.

### 2 - Quais são os critérios e práticas de sustentabilidade e acessibilidade cabíveis ou exigíveis?

Os critérios de sustentabilidade e acessibilidade aplicáveis estão definidos no item 3.4 e seus subitens: eficiência energética, descarte ambientalmente adequado, documentação digital, monitoramento remoto, reaproveitamento de infraestrutura existente, segurança do trabalho, preservação da acessibilidade física em salas técnicas, racks, shafts e áreas de circulação, bem como observância aos guias de contratações sustentáveis da Justiça do Trabalho e da AGU naquilo que for compatível com serviços de telecomunicações e comunicação de dados.

## IV - ESTIMATIVAS DAS QUANTIDADES

### 1 - Qual é a estimativa das quantidades a serem contratadas, acompanhada das memórias de cálculo e dos documentos que lhes dão suporte?

Serão contratados 10 circuitos MPLS mensais, incluindo um circuito concentrador na Sede e circuitos nas demais localidades.

Também será contratado 1 link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, em grupo próprio, para replicação e redundância.

Fica definida a contratação ou manutenção de 3 saídas de Internet centralizadas na Sede, com capacidade combinada mínima de 4 Gbps, preferencialmente com operadoras e rotas físicas distintas, para sustentar a arquitetura de egressão preferencial centralizada.

A memória de quantidades decorre do mapa de localidades do TRT10 e da premissa técnica de redundância total: cada localidade receberá capacidade MPLS equivalente à capacidade SD-WAN vigente, além do grupo específico de link dedicado ponto-a-ponto de 25 Gbps entre Sede e Foro de Brasília. Assim, a estimativa quantitativa fica definida em 10 circuitos MPLS, 1 link dedicado Sede-Foro de 25 Gbps e manutenção de 3 saídas centralizadas de Internet na Sede com capacidade combinada mínima de 4 Gbps.

## V - LEVANTAMENTO DE MERCADO

### 1 - Quais soluções disponíveis no mercado foram avaliadas?

### 4.1 Soluções identificadas

Foram avaliadas as seguintes alternativas aderentes ao problema arquitetural:

| Alternativa | Descrição | Pros | Contras / Riscos |
|---|---|---|---|
| Solução 1 - MPLS integrado à SD-WAN com capacidade equivalente | Contratação de MPLS com a mesma capacidade nominal da SD-WAN por localidade. Ambos os meios podem transportar qualquer tráfego em contingência. | Combina rede privada, QoS, isolamento lógico, previsibilidade, centralização na Sede, convivência com a SD-WAN vigente e redundância total por caminhos distintos. Permite tratar tráfego crítico e Internet com políticas distintas, sem reduzir banda durante falha de uma camada. | Exige projeto executivo de roteamento, definição de QoS, monitoramento integrado e gestão coordenada entre contrato MPLS e contrato SD-WAN. A vantajosidade deverá ser demonstrada pela relação entre custo, disponibilidade, continuidade, segurança e redução de risco operacional. |
| Solução 2 - Links satelitais | Contratação de enlaces satelitais para atuar como meio de interconexão das unidades à Sede, substituindo ou complementando a função pretendida para o MPLS. | Pode ser útil em locais sem boa cobertura terrestre, em contingência de desastres regionais ou como caminho fisicamente diverso. Independe parcialmente de infraestrutura terrestre local. | Tende a apresentar maior latência, maior variabilidade de desempenho, possíveis franquias ou restrições técnicas, sensibilidade a condições ambientais e menor aderência para sistemas críticos sensíveis a atraso. Pode elevar custo por Mbps e exigir arquitetura adicional de roteamento/segurança. |
| Solução 3 - Links de Internet comuns com VPN ponto a ponto | Contratação de links convencionais de Internet nas unidades, estabelecendo túneis VPN ponto a ponto ou malha VPN até a Sede. | Pode ter maior disponibilidade de fornecedores locais, menor custo unitário aparente e implantação simples em algumas localidades. | Não garante a mesma previsibilidade de rede privada, dificulta QoS fim a fim, amplia superfície exposta à Internet, aumenta complexidade de operação de túneis, depende da qualidade da Internet local e pode gerar maior esforço de suporte, troubleshooting e segurança. |

### 4.2 Análise comparativa das soluções

A Solução 1 é a que melhor equilibra disponibilidade, segurança, governança e convivência com a infraestrutura vigente. A SD-WAN contratada continua exercendo papel relevante para saída de Internet, balanceamento e contingência; o MPLS acrescenta uma camada privada para tráfego crítico e institucional, reduzindo dependência exclusiva dos enlaces de Internet para comunicação entre unidades e Sede. A Solução 1 prevê capacidade MPLS equivalente à capacidade SD-WAN em cada localidade porque o objetivo arquitetural é assegurar redundância integral para a continuidade dos serviços.

Do ponto de vista arquitetural, a Sede possui papel natural de concentrador porque abriga as 3 saídas redundantes de Internet, políticas de segurança perimetral, integrações institucionais e concentração de serviços corporativos. Ao interconectar as unidades à Sede por MPLS, a Administração passa a dispor de um caminho controlado para sistemas críticos e, ao mesmo tempo, mantém a SD-WAN para tráfego de Internet e contingência. Essa separação reduz competição entre fluxos de natureza distinta e permite aplicar QoS, priorização, monitoramento e glosas por circuito.

A Solução 2, baseada em links satelitais, é tecnicamente possível, mas deve ser tratada como alternativa complementar ou de contingência específica, não como desenho preferencial para todo o ambiente. A latência e a variabilidade de desempenho podem afetar autenticação, sessões de sistemas, voz, vídeo, replicações e outros fluxos sensíveis. Sua melhor aplicação seria para localidades sem viabilidade terrestre ou para plano de continuidade de negócios em cenários extremos.

A Solução 3, baseada em Internet comum com VPN ponto a ponto, reduz barreiras iniciais, mas transfere para a Administração maior complexidade operacional e maior dependência de redes públicas. Embora VPNs possam prover confidencialidade, elas não equivalem a QoS fim a fim, previsibilidade de backbone, isolamento operacional e SLA privado. A multiplicação de túneis também pode dificultar mudanças, troubleshooting, gestão de chaves, auditoria e evolução da topologia.

### 4.3 Solução escolhida

A solução escolhida é a Solução 1: utilização integrada de MPLS e SD-WAN, com MPLS contratado na mesma capacidade nominal dos links SD-WAN vigentes por localidade. O MPLS será contratado para interconectar as unidades à Sede e transportar preferencialmente tráfego crítico de sistemas institucionais, serviços internos, autenticação, administração e integrações. A SD-WAN vigente permanecerá como camada preferencial para Internet. Em caso de falha, degradação relevante ou manutenção de uma das camadas, a arquitetura deverá permitir contingência cruzada, de modo que MPLS e SD-WAN possam transportar os fluxos necessários à continuidade dos serviços sem redução planejada de capacidade nominal.

A escolha da Solução 1 fica definida neste ETP. A pesquisa de preços já realizada sustenta a estimativa de planejamento, as capacidades por localidade estão fixadas na tabela de quantitativos, as políticas mínimas de QoS estão definidas neste documento e a integração de roteamento será executada conforme os requisitos técnicos de OSPF/BGP, métricas, filtros e failover aqui estabelecidos.

### 2 - Foram identificadas contratações similares ou inovações relevantes?

Sim. Foram identificadas contratações similares no PNCP envolvendo MPLS, rede privada, comunicação de dados, SD-WAN/MPLS, LAN-to-LAN, Metro Ethernet, fibra dedicada e links de alta capacidade, com artefatos baixados para a pasta `PNCP_REFERENCIAS_MPLS`. As referências utilizadas para preços e compatibilidade técnica estão detalhadas no item VI deste ETP, com indicação de órgão, pregão/licitação, processo, identificador PNCP, item, valor e fórmula de cálculo.

### 3 - Quais são os prós e contras das alternativas identificadas?

A comparação técnica entre as alternativas consta da tabela e da análise acima. Em síntese, a Solução 1 - MPLS integrado à SD-WAN com capacidade equivalente - apresenta melhor equilíbrio entre segurança, disponibilidade, QoS, isolamento lógico, roteamento controlado, integração com a infraestrutura vigente e redundância total. Links satelitais são úteis como contingência específica, mas possuem maior latência e variabilidade. Links comuns de Internet com VPN possuem menor custo aparente, mas ampliam dependência de rede pública e dificultam QoS fim a fim.

## VI - ESTIMATIVA DO VALOR DA CONTRATAÇÃO

### 1 - Foi elaborada pesquisa de preços conforme planilha padronizada da Administração? Apresente a memória de cálculo.

Fixa-se estimativa de planejamento com base em referências PNCP documentadas, no valor mensal de R$ 74.445,00 e valor anual de R$ 893.340,00 para MPLS e link dedicado Sede-Foro de 25 Gbps. Os valores identificados possuem escopos distintos e foram tratados por mediana, normalização mensal e análise crítica de similaridade técnica.

A estimativa de preços adota as referências PNCP de MPLS, rede privada, comunicação de dados, SD-WAN/MPLS e interconexão por fibra como base para a Solução 1, por ser a alternativa escolhida. A comparação entre alternativas foi considerada qualitativamente na análise de soluções, e a estimativa financeira da solução escolhida considera custo mensal, instalação quando embutida, equipamentos sob responsabilidade da contratada, SLA, latência, prazo de reparo, suporte, disponibilidade por localidade, expansibilidade e custo operacional de gestão.

Para memória de cálculo, foram consultadas contratações PNCP publicadas ou atualizadas nos últimos 2 anos, por meio da API pública do PNCP e dos endpoints públicos de itens e arquivos. A consulta utilizou os termos "MPLS", "comunicação de dados", "rede privada", "SD-WAN", "fibra óptica", "100 Mbps", "500 Mbps" e "1 Gbps". Os documentos disponíveis foram baixados para a pasta local `PNCP_REFERENCIAS_MPLS`, preservando `detalhe_contratacao.json`, `itens.json`, `arquivos.json`, editais, termos de referência, ETPs, mapas de preços e memórias de cálculo.

| Capacidade | Órgão / contrato de referência PNCP | Número do pregão/licitação e identificador | Item utilizado | Valor mensal unitário usado | Fonte / observação |
|---|---|---|---|---|---|
| 100 Mbps | Companhia de Desenvolvimento dos Vales do São Francisco e do Parnaíba - CODEVASF | Pregão Eletrônico nº 90003/2025; Processo nº 59500002693202462; PNCP-00399857000126-1-000049/2025 | Rede VPN IP/MPLS - links de 100 Mbps para Superintendências Regionais; tabela do edital republicado | R$ 2.161,00 | Valor mensal direto do edital: 100 Mbps por 30 meses a R$ 2.161,00 mensais por localidade. Artefato baixado: edital completo republicado e relação de itens. |
| 100 Mbps | Município de Cascavel/PR | Edital 90129/2025; Processo nº 115968; Pregão eletrônico; PNCP-76208867000107-1-000429/2025 | Rede IP/MPLS; itens de 70 Mbps e 200 Mbps usados como faixa inferior/superior para capacidade próxima | R$ 1.900,00 | Referência parcial: item de 200 Mbps possui valor unitário anual de R$ 22.800,00, normalizado para R$ 1.900,00/mês. Usado como teto próximo para 100 Mbps, não como preço exato de 100 Mbps. |
| 100 Mbps | Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; PNCP-83021808000182-1-000200/2026 | Levantamento de mercado anexo ao edital, com referência PNCP de interconexão por fibra óptica de 100 Mbps | R$ 202,97 | Referência auxiliar de interconexão por fibra, obtida de levantamento de mercado baixado do PNCP: R$ 316.628,05 / 1.560 meses = R$ 202,97/mês. Não é referência MPLS pura; usada apenas para demonstrar faixa inferior de mercado. |
| 500 Mbps | Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; PNCP-83021808000182-1-000200/2026 | Rede privada MPLS para 205 pontos de 500 Mbps, full duplex, por fibra óptica, segmentados por VLAN | R$ 410,00 | Valor unitário por ponto informado no Termo de Referência: R$ 410,00/mês por ponto de 500 Mbps. Valor global mensal do item: R$ 84.050,00. |
| 500 Mbps | Agência Nacional do Cinema - ANCINE | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP-04884574000120-1-000056/2025 | Link MPLS com SD-WAN - Brasília e Rio de Janeiro (Augusto Severo), 2 links de 500 Mbps | R$ 5.875,42 | Valor total do item: R$ 141.010,08 para 2 links por 12 meses; fórmula: R$ 141.010,08 / 2 / 12 = R$ 5.875,42 por link/mês. |
| 500 Mbps | Município de Cascavel/PR | Edital 90129/2025; Processo nº 115968; Pregão eletrônico; PNCP-76208867000107-1-000429/2025 | Rede IP/MPLS; item de 200 Mbps como referência parcial de menor capacidade | R$ 1.900,00 | Referência parcial, pois a contratação PNCP não possui item de 500 Mbps. O item de 200 Mbps foi normalizado de R$ 22.800,00 anuais para R$ 1.900,00 mensais e usado apenas como apoio de faixa. |
| 1 Gbps | Serviço Nacional de Aprendizagem Rural - SENAR/MS | Pregão Eletrônico nº 009/2026; Processo nº 018/2026; PNCP-04253881000103-1-000025/2026 | Link dedicado - MPLS (1 Gbps), item 10006 | R$ 6.950,00 | Valor unitário estimado no PNCP: R$ 6.950,00, quantidade 12, total R$ 83.400,00. |
| 1 Gbps | Município de Brusque/SC | Pregão Eletrônico nº 11/2026; Processo nº 33/2026; PNCP-83102343000194-1-000064/2026 | Serviço de acesso privado entre Prefeitura e datacenter por link MPLS de ao menos 1 Gbps, item 7 | R$ 7.295,00 | Valor unitário estimado no PNCP e no mapa de preços: R$ 7.295,00 por serviço/mês, quantidade 72, total R$ 525.240,00. |
| 1 Gbps | Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; PNCP-83021808000182-1-000200/2026 | Rede privada MPLS para 20 pontos de 1 Gbps, full duplex, por fibra óptica, segmentados por VLAN | R$ 574,00 | Valor unitário por ponto informado no Termo de Referência: R$ 574,00/mês por ponto de 1 Gbps. Valor global mensal do item: R$ 11.480,00. Tratado como referência de grande volume, com forte ganho de escala. |
| 1 Gbps | Agência Nacional do Cinema - ANCINE | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP-04884574000120-1-000056/2025 | Link MPLS com SD-WAN - Rio de Janeiro (Graça Aranha), 1 link de 1 Gbps | R$ 8.211,77 | Valor total do item: R$ 98.541,28 para 1 link por 12 meses; fórmula: R$ 98.541,28 / 12 = R$ 8.211,77 por link/mês. |

Com base nesses valores PNCP, a memória de cálculo inicial adota mediana por capacidade quando há pelo menos três referências utilizáveis, por ser menos sensível a outliers e a ganhos de escala. Quando houver menos de três referências exatas, registra-se a limitação e usa-se referência parcial apenas como apoio de faixa, sem afirmar equivalência plena.

- Preço mensal de referência por capacidade = mediana dos valores mensais unitários utilizáveis; quando houver apenas uma referência exata, usa-se o valor exato localizado e classifica-se a referência como parcial, auxiliar ou técnica conforme aderência ao objeto;

- Valor mensal por capacidade = preço mensal de referência por capacidade x quantidade de links TRT10 naquela capacidade;

- Valor anual por capacidade = valor mensal por capacidade x 12;

- Total mensal MPLS = soma dos valores mensais das capacidades de 1 Gbps, 500 Mbps e 100 Mbps;

- Total anual MPLS = total mensal MPLS x 12;

- Valor mensal do link dedicado Sede-Foro 25 Gbps = ponto médio da faixa de mercado, isto é, (R$ 30.000,00 + R$ 60.000,00) / 2 = R$ 45.000,00;

- Valor anual do link dedicado Sede-Foro 25 Gbps = R$ 45.000,00 x 12 = R$ 540.000,00.

| Capacidade | Referências usadas no cálculo | Fórmula do preço mensal de referência | Quantidade TRT10 | Valor mensal | Valor anual |
|---|---|---|---|---|---|
| 1 Gbps | SENAR/MS R$ 6.950,00; Brusque/SC R$ 7.295,00; Chapecó/SC R$ 574,00; ANCINE R$ 8.211,77 | Mediana de 574,00; 6.950,00; 7.295,00; 8.211,77 = (6.950,00 + 7.295,00) / 2 = R$ 7.122,50 | 2 | R$ 14.245,00 | R$ 170.940,00 |
| 500 Mbps | Chapecó/SC R$ 410,00; ANCINE R$ 5.875,42; Cascavel/PR 200 Mbps R$ 1.900,00 como referência parcial | Mediana de 410,00; 1.900,00; 5.875,42 = R$ 1.900,00 | 3 | R$ 5.700,00 | R$ 68.400,00 |
| 100 Mbps | CODEVASF R$ 2.161,00; Cascavel/PR 200 Mbps R$ 1.900,00 como referência parcial; Chapecó/SC interconexão 100 Mbps R$ 202,97 como referência auxiliar | Mediana de 202,97; 1.900,00; 2.161,00 = R$ 1.900,00 | 5 | R$ 9.500,00 | R$ 114.000,00 |
| Total MPLS | - | Soma dos valores mensais por capacidade | 10 | R$ 29.445,00 | R$ 353.340,00 |
| Link dedicado Sede-Foro 25 Gbps | Faixa paramétrica baseada em precedentes PNCP compatíveis de 4, 5 e 10 Gbps | (30.000,00 + 60.000,00) / 2 = R$ 45.000,00 | 1 | R$ 45.000,00 | R$ 540.000,00 |
| Total geral | MPLS + link dedicado 25 Gbps | 29.445,00 + 45.000,00 | 11 | R$ 74.445,00 | R$ 893.340,00 |

### 10.3.2 Rastreabilidade das fontes consultadas

Rastreabilidade das fontes consultadas e artefatos baixados:

| Referência | Consulta pública / identificador | Observação de uso |
| --- | --- | --- |
| CODEVASF | PNCP-00399857000126-1-000049/2025; Pregão Eletrônico nº 90003/2025; Processo nº 59500002693202462; consulta PNCP: https://pncp.gov.br/app/editais/00399857000126/2025/49 | Fonte principal para 100 Mbps. Artefatos baixados em `PNCP_REFERENCIAS_MPLS/00399857000126-1-000049-2025`, incluindo edital completo republicado e relação de itens. |
| Cascavel/PR | PNCP-76208867000107-1-000429/2025; Edital 90129/2025; Processo nº 115968; Pregão eletrônico; consulta PNCP: https://pncp.gov.br/app/editais/76208867000107/2025/429 | Referência de rede IP/MPLS. Artefatos baixados em `PNCP_REFERENCIAS_MPLS/76208867000107-1-000429-2025`. Usada como referência parcial por conter 70 Mbps e 200 Mbps, mas não 100/500 Mbps exatos. |
| Chapecó/SC | PNCP-83021808000182-1-000200/2026; Pregão Eletrônico nº 153/2026; consulta PNCP: https://pncp.gov.br/app/editais/83021808000182/2026/200 | Fonte exata para 500 Mbps e 1 Gbps em rede privada MPLS por fibra óptica. Artefatos baixados em `PNCP_REFERENCIAS_MPLS/83021808000182-1-000200-2026`, incluindo DFD, ETP, levantamento de mercado, memória de cálculo, TR e edital. |
| ANCINE | PNCP-04884574000120-1-000056/2025; Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; consulta PNCP: https://pncp.gov.br/app/editais/04884574000120/2025/56 | Fonte para MPLS com SD-WAN em 500 Mbps e 1 Gbps. Artefatos baixados em `PNCP_REFERENCIAS_MPLS/04884574000120-1-000056-2025`, incluindo edital e relação de itens. |
| SENAR/MS | PNCP-04253881000103-1-000025/2026; Pregão Eletrônico nº 009/2026; Processo nº 018/2026; consulta PNCP: https://pncp.gov.br/app/editais/04253881000103/2026/25 | Fonte exata para item MPLS 1 Gbps. Artefato baixado em `PNCP_REFERENCIAS_MPLS/04253881000103-1-000025-2026`. |
| Brusque/SC | PNCP-83102343000194-1-000064/2026; Pregão Eletrônico nº 11/2026; Processo nº 33/2026; consulta PNCP: https://pncp.gov.br/app/editais/83102343000194/2026/64 | Fonte exata para link MPLS de ao menos 1 Gbps entre Prefeitura e datacenter. Artefatos baixados em `PNCP_REFERENCIAS_MPLS/83102343000194-1-000064-2026`, incluindo edital, ETP, TR, mapa de preços e republicações. |
| Candeias/BA | PNCP-13830336000123-1-000051/2026; Edital 023/2026; consulta PNCP: https://pncp.gov.br/app/editais/13830336000123/2026/51 | Referência de alta capacidade para LAN-to-LAN, fibra dedicada, concentradores de 10 Gbps e link dedicado 4 Gbps. |
| Jaguariúna/SP | PNCP-46410866000171-1-000610/2024; Edital PL-674/2024; PE 90081/2024; consulta PNCP: https://pncp.gov.br/editais/46410866000171/2024/610 | Referência de alta capacidade para link dedicado simétrico de 10 Gbps, embora com escopo de acesso à Internet. |
| Ubarana/SP | PNCP-65708786000141-1-000038/2026; Edital 19/2026; consulta PNCP: https://pncp.gov.br/app/editais/65708786000141/2026/38 | Referência de alta capacidade para rede LAN-to-LAN por fibra dedicada, capacidade agregada até 10 Gbps. |
| TJPR | PNCP 77821841000194-1-000049/2025; Edital PE 15/2025 | Referência de alta capacidade para dois links dedicados de 10 Gbps, BGP, Anti-DDoS e operadoras distintas. |
| JFRS/TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços nº 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Referência técnica de Metro Ethernet/LAN-to-LAN/ponto-a-ponto; valor do item específico não confirmado. |

### 10.3.3 Referências para o grupo de link dedicado Sede-Foro 25 Gbps

Para o grupo de link dedicado Sede-Foro de 25 Gbps, a pesquisa não localizou três itens PNCP idênticos em 25 Gbps. Foram localizados precedentes compatíveis de alta capacidade, listados abaixo:

| Referência | Número do pregão/licitação e identificador | Objeto compatível | Valor informado | Uso na estimativa |
|---|---|---|---|---|
| Município de Candeias/BA | Edital 023/2026; Pregão eletrônico; PNCP-13830336000123-1-000051/2026; abertura em 13/03/2026 | Comunicação de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra óptica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos | R$ 950.560,00 | Similaridade por LAN-to-LAN, fibra dedicada, alta capacidade, rotas redundantes e equipamentos. |
| Município de Jaguariúna/SP | Edital PL-674/2024; PE 90081/2024; Pregão eletrônico; PNCP-46410866000171-1-000610/2024; abertura em 16/10/2024 | Link dedicado de acesso à Internet bidirecional e simétrico de 10 Gbps e link compartilhado de internet banda larga | R$ 4.705.844,00 | Similaridade por link dedicado 10 Gbps; escopo de Internet, não ponto-a-ponto. |
| Município de Ubarana/SP | Edital 19/2026; Pregão eletrônico; PNCP-65708786000141-1-000038/2026; abertura em 15/04/2026 | Rede LAN-to-LAN por fibra óptica dedicada, capacidade agregada de até 10 Gbps, ponto concentrador e link dedicado de acesso à Internet | R$ 184.400,00 | Similaridade por LAN-to-LAN, fibra dedicada e limite agregado de 10 Gbps. |
| TJPR | Edital PE 15/2025; PNCP 77821841000194-1-000049/2025; Pregão eletrônico | Dois links dedicados de 10 Gbps cada, BGP, Anti-DDoS e operadoras distintas para Sistema Autônomo de Internet do TJPR | R$ 187.560,00 | Similaridade por 10 Gbps, redundância e operadoras distintas; escopo de Internet/AS, não replicação ponto-a-ponto. |
| JFRS/TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Serviços de comunicação de dados dedicados e exclusivos para acesso à Internet e comunicação ponto a ponto entre sites via Metro Ethernet / LAN-to-LAN, camada 2 | Não utilizado no cálculo | Similaridade funcional por Metro Ethernet/LAN-to-LAN e comunicação ponto a ponto entre sites; usado como referência técnica, sem impacto na estimativa por ausência de valor unitário confirmado. |

As referências acima não foram usadas para cálculo de média direta do item de 25 Gbps, porque os valores informados correspondem a objetos, prazos e escopos distintos. Elas foram usadas para demonstrar compatibilidade técnica de mercado e para balizar a faixa paramétrica de R$ 30.000,00 a R$ 60.000,00 mensais.

Para o enlace dedicado Sede-Foro de 25 Gbps, fica adotado o valor de planejamento de R$ 45.000,00 mensais e R$ 540.000,00 anuais, correspondente ao ponto médio da faixa de R$ 30.000,00 a R$ 60.000,00 mensais observada para referências públicas de alta capacidade e ajustada à criticidade do circuito. Esse valor contempla baixa latência, fibra dedicada, interfaces 25GbE/SFP28 ou equivalentes, SLA de 99,95%, monitoramento, instalação, equipamentos necessários à entrega do serviço e suporte 24x7.

A memória de cálculo já utiliza mediana e análise crítica de outliers. Referências com valor unitário não confirmado, escopo não equivalente ou ganho de escala muito acentuado foram tratadas como referência parcial ou técnica, e não como preço direto sem ressalva.

### 2 - No caso de aquisição de bens e contratação de serviços em geral, a estimativa observa o art. 23, §1º, da Lei nº 14.133/2021 e a IN SEGES/ME nº 65/2021?

Sim. A estimativa adota pesquisa em contratações públicas similares obtidas no PNCP, normalização mensal dos valores, identificação de escopo, capacidade, órgão, pregão/licitação, processo e número de controle PNCP, com tratamento crítico de referências exatas, parciais e auxiliares. A metodologia utiliza mediana por capacidade quando há referências suficientes, por ser menos sensível a valores extremos, e registra limitação quando a referência não corresponde integralmente ao objeto.

### 3 - No caso de obras e serviços de engenharia, a estimativa observa o art. 23, §2º, da Lei nº 14.133/2021, a IN SEGES/ME nº 91/2022 e o Decreto nº 7.983/2013?

Não se aplica. O objeto é serviço continuado de telecomunicações e comunicação de dados, com fornecimento de meios, equipamentos de borda e operação gerenciada como parte do serviço. Eventuais obras civis leves, passagem de cabos, adequações físicas ou lançamento de último trecho possuem caráter acessório e deverão estar incorporados ao preço do serviço, sem caracterizar contratação principal de obra ou serviço de engenharia.

## VII - DESCRIÇÃO DA SOLUÇÃO COMO UM TODO

### 1 - Qual é a solução apta a atender à necessidade, considerando todo o ciclo de vida do objeto?

A solução consiste em contratar conectividade privada para as 10 localidades, tendo a Sede como concentrador preferencial. Todas nas demais unidades deverão possuir circuito MPLS até a Sede. A SD-WAN vigente permanecerá ativa como camada preferencial para Internet, enquanto o MPLS será a camada preferencial para tráfego crítico. A saída de Internet será preferencialmente centralizada na Sede, onde existem 3 saídas redundantes de Internet.

A solução deverá coexistir com a SD-WAN como transporte vigente, considerando seus enlaces, túneis IPSec, roteamento dinâmico e capacidade contratada. O MPLS atuará como camada privada, voltada a tráfego corporativo crítico, contingência controlada, isolamento lógico, previsibilidade de desempenho e rotas de recuperação.

A solução também deverá contratar link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, separado da malha MPLS, para criar um eixo de alta capacidade entre os dois principais pontos institucionais. O Foro de Brasília fica definido como ambiente de replicação e redundância da Sede, apto a assumir, em contingência, funções de acesso das unidades. Para isso, a solução deverá contemplar rotas de contingência para o Foro, regras de segurança equivalentes às aplicadas na Sede, disponibilidade dos serviços de DNS, autenticação e firewall, monitoramento do enlace e procedimentos operacionais de ativação e retorno.

### Lógica arquitetural da Solução 1

1. A Sede concentra as 3 saídas redundantes de Internet e deve permanecer como ponto preferencial de egressão, segurança, filtragem e observabilidade.

1. O MPLS fornece caminho privado e controlado para tráfego crítico entre unidades e Sede, permitindo QoS, segregação lógica e metas objetivas de disponibilidade.

1. A SD-WAN mantém a capacidade já contratada para acesso à Internet e pode operar como caminho alternativo para tráfego crítico quando o MPLS estiver indisponível ou degradado.

1. O MPLS pode transportar tráfego de Internet em contingência, direcionando as unidades para a Sede quando a SD-WAN local estiver indisponível ou degradada.

1. O desenho evita dependência exclusiva de uma tecnologia e reduz o risco de indisponibilidade total por falha de um único meio de comunicação.

1. O link dedicado Sede-Foro de 25 Gbps viabiliza replicação, sincronização e uso do Foro como redundância da Sede.

1. A convivência entre MPLS, SD-WAN e link dedicado Sede-Foro fica definida com MPLS preferencial para tráfego crítico, SD-WAN preferencial para Internet, link dedicado Sede-Foro dedicado a replicação e contingência, métricas de failover documentadas, retorno controlado após estabilização mínima de 15 minutos, QoS fim a fim, segurança equivalente entre Sede e Foro e monitoramento 24x7.

### Topologia proposta

![Figura 1 - Arquitetura proposta SD-WAN + MPLS](../diagrama_topologia_revisada.png)

### Dimensionamento definido

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

Considerando a soma aproximada de 4 Gbps dos enlaces SD-WAN atuais das localidades, a Sede deverá manter capacidade agregada mínima de 4 Gbps nas 3 saídas centrais para atuar como ponto preferencial de egressão de Internet e concentração de políticas. Essa capacidade mínima será distribuída entre os enlaces centrais e preservada por operadoras e rotas físicas distintas sempre que tecnicamente viável. A equivalência de capacidade entre MPLS e SD-WAN por localidade não elimina a necessidade de QoS; ela assegura que o failover não dependa de redução prévia da banda disponível.

O enlace dedicado Sede-Foro de 25 Gbps fica dimensionado para cargas de replicação e contingência, não apenas para tráfego ordinário de usuários. A banda elevada se justifica pela necessidade de transferências volumosas entre ambientes, sincronização de dados, restauração, espelhamento, backup, testes de continuidade e redirecionamento de acesso das unidades ao Foro. O enlace deverá possuir banda simétrica full duplex, latência média mensal máxima de 5 ms entre as pontas, perda média inferior a 0,1%, jitter médio inferior a 5 ms, disponibilidade mensal mínima de 99,95%, interface 25GbE/SFP28 ou equivalente em cada ponta, monitoramento 24x7 e aceite com teste de throughput mínimo de 95% da banda contratada em janela de teste acordada com o TRT10.

### Diretrizes de operação e governança

- Definir política clara de roteamento, com Internet preferencialmente via Sede e tráfego local apenas quando formalmente autorizado e controlado.

- Implementar QoS fim a fim para priorizar processo judicial, sistemas administrativos, autenticação, voz/vídeo institucional, monitoramento e tráfego de replicação.

- Medir latência, jitter, perda de pacotes e throughput por unidade antes e depois da implantação.

- Configurar failover entre SD-WAN e MPLS para fluxos críticos, com critérios de acionamento, retorno e registro.

- Centralizar inspeção de tráfego, filtragem, logs e políticas de acesso na Sede, quando tecnicamente aplicável.

- Segmentar tráfego por classes ou VRFs, tais como usuários, administração, voz/vídeo, serviços críticos, monitoramento, backup/replicação e gerência.

- Integrar logs de borda a solução institucional de SIEM ou plataforma equivalente de monitoramento e auditoria, quando existente.

- Exigir documentação as built da rede, incluindo endereçamento, rotas, políticas, QoS, equipamentos, circuitos e contatos de suporte.

- Implantar painéis de monitoramento com disponibilidade, capacidade, erros, latência, perda, jitter e eventos de failover.

- Estabelecer rotina de revisão semestral de capacidade e relatório mensal de desempenho por localidade.

- Documentar procedimentos de crise, escalonamento técnico e comunicação institucional em caso de indisponibilidade ampla.

### 2 - Quais são as justificativas técnicas e econômicas para a escolha?

A solução escolhida é tecnicamente justificável porque combina rede privada MPLS, SD-WAN vigente, saídas centralizadas de Internet e link dedicado Sede-Foro de 25 Gbps em uma arquitetura de redundância total. A equivalência de capacidade entre MPLS e SD-WAN reduz o risco de contingência parcial e evita que uma falha em uma camada force operação com banda inferior à capacidade ordinária. Economicamente, a escolha preserva infraestrutura vigente, permite competição por requisitos funcionais, utiliza preços de mercado documentados no PNCP e reduz custos indiretos associados a indisponibilidade, suporte emergencial, degradação de desempenho e interrupção de serviços.

### 3 - A solução demandará manutenção e/ou assistência técnica?

Sim. A manutenção, assistência técnica, operação, monitoramento, suporte, substituição de equipamentos sob responsabilidade da contratada, relatórios mensais e atendimento a chamados integram o objeto da contratação e deverão estar incluídos nos preços mensais.

### 4 - No caso de compras, será necessário analisar amostras?

Não. O objeto é serviço continuado de comunicação de dados. Não serão exigidas amostras físicas como critério ordinário de aceitação. Equipamentos fornecidos como parte do serviço serão avaliados por documentação técnica, projeto executivo, testes de ativação, aceite por localidade, desempenho e aderência aos requisitos funcionais.

### 5 - No caso de serviços, será necessária vistoria prévia?

A vistoria prévia será facultativa. A licitante poderá substituí-la por declaração de conhecimento das condições locais e responsabilidade pela proposta. O edital deverá disponibilizar informações mínimas sobre localidades, endereços, infraestrutura, condições de acesso e pontos de instalação, sem transformar a vistoria em barreira de competitividade.

### 6 - É necessária autorização do poder público para exercício da atividade a ser contratada?

Sim. A contratada deverá comprovar autorização, outorga, licença ou regularidade regulatória aplicável à prestação de serviços de telecomunicações/comunicação de dados, em especial SCM ou enquadramento equivalente perante a Anatel, diretamente ou por arranjo juridicamente admitido, mantendo responsabilidade integral pela execução e pelo SLA.

### 7 - Será necessário exigir qualificações econômico-financeiras adicionais?

Sim. Ficam exigidas qualificações econômico-financeiras ordinárias previstas na legislação e no edital, com balanço e demonstrações contábeis quando aplicáveis, índices compatíveis com serviço continuado essencial e possibilidade de comprovação alternativa de patrimônio líquido mínimo de 10% do valor estimado anual quando algum índice mínimo não for atendido. A exigência não será cumulada com capital social mínimo.

### 8 - Será necessário exigir qualificações técnicas técnico-operacionais e técnico-profissionais específicas?

Sim. Fica exigida qualificação técnico-operacional compatível com rede corporativa, MPLS/L3VPN/LAN-to-LAN/rede privada gerenciada ou tecnologia equivalente, múltiplas localidades, operação, monitoramento, suporte, SLA, CPEs/roteadores, implantação, configuração, manutenção e documentação. A experiência mínima fica definida em atendimento a pelo menos 5 localidades ou 50% do quantitativo do TRT10, com pelo menos 1 enlace de 1 Gbps ou superior, admitido somatório de atestados tecnicamente compatíveis. Também fica exigida indicação de responsável técnico ou equipe técnica com experiência em redes corporativas, telecomunicações, roteamento, segurança de rede ou operação de serviços de comunicação de dados, sem exigência de certificação de fabricante específico.

## VIII - JUSTIFICATIVAS PARA O PARCELAMENTO OU NÃO PARCELAMENTO

### 1 - No caso de parcelamento do objeto por item, justifique.

Não será adotado parcelamento por item/localidade. O parcelamento por circuito isolado não é adequado ao desenho pretendido, porque a solução depende de roteamento integrado, QoS, monitoramento centralizado, SLA de ponta a ponta, contingência cruzada MPLS/SD-WAN e responsabilização única por indisponibilidade.

### 2 - No caso de parcial parcelamento do objeto por grupo de itens, justifique.

A contratação será estruturada em grupo único de solução, com composição interna dos itens MPLS e do link dedicado Sede-Foro para fins de orçamento, execução, fiscalização, medição e glosa. A modelagem em grupo único preserva a responsabilidade integral da contratada e evita disputas de responsabilidade técnica entre fornecedores distintos.

### 3 - No caso de não parcelamento global, justifique.

Fica definida adjudicação por grupo único, pois a solução depende de interoperabilidade ponta a ponta, gestão centralizada de SLA, roteamento integrado, suporte unificado e responsabilização única por indisponibilidade. O parcelamento por localidade geraria risco de fragmentação operacional, disputas de responsabilidade e maior complexidade de gerenciamento.

A justificativa de grupo único fica mantida porque há referências PNCP de contratações de rede privada, MPLS, SD-WAN/MPLS e comunicação de dados com múltiplos pontos e gestão centralizada. A disputa deverá admitir consórcios quando juridicamente cabível e subcontratação acessória nos limites definidos neste ETP, reduzindo risco de restrição indevida à competitividade sem fragmentar a responsabilidade técnica principal.

## IX - DEMONSTRATIVO DOS RESULTADOS PRETENDIDOS

### 1 - O que se almeja alcançar com a contratação?

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

### 2 - No caso de contratação de serviços, quais são os níveis esperados de qualidade da prestação e as respectivas adequações de pagamento para o Instrumento de Medição de Resultados (IMR)?

Os níveis esperados de qualidade ficam definidos pelos SLA de disponibilidade, atendimento, reparo, manutenção programada, desempenho mínimo, documentação, relatórios e aceite descritos neste ETP. O IMR deverá aplicar glosas por circuito, conforme faixas já definidas: 5% da mensalidade quando a disponibilidade ficar abaixo da meta e até 0,5 ponto percentual abaixo dela; 10% quando a queda exceder 0,5 ponto e for até 1 ponto percentual; 20% quando a queda exceder 1 ponto percentual; e 30% quando houver indisponibilidade superior a 24 horas acumuladas no mês, sem prejuízo de sanções. Também serão aferidos início de atendimento, prazo de reparo, perda, jitter, latência, throughput do link dedicado de 25 Gbps, entrega de relatórios e documentação as built.

## X - PROVIDÊNCIAS A SEREM ADOTADAS PELA ADMINISTRAÇÃO

### 1 - Quais providências deverão ser adotadas pela Administração previamente à celebração do contrato?

- Validar inventário de circuitos e endereços;

- medir uso real da SD-WAN por localidade;

- validar capacidade das 3 saídas de Internet da Sede;

- registrar a capacidade mínima combinada de 4 Gbps para as saídas centrais como requisito de egressão, picos, simultaneidade e contingência;

- exigir operadoras e rotas físicas distintas para as saídas de Internet da Sede quando houver viabilidade técnica e competição suficiente;

- consolidar plano de endereçamento, VRFs, roteamento e QoS conforme requisitos definidos neste ETP;

- consolidar políticas de failover e retorno entre MPLS e SD-WAN conforme requisitos definidos neste ETP;

- registrar que tráfego local de Internet nas unidades somente será admitido como exceção técnica formalmente autorizada;

- adotar RTO de rede de até 4 horas para Sede, Foro de Brasília e link Sede-Foro, até 6 horas para demais localidades do DF e até 8 horas para localidades do Tocantins, e RPO de configuração de rede de até 24 horas para restauração de parâmetros documentados;

- conferir vigências contratuais e dependências;

- preparar mapa de riscos;

- elaborar pesquisa de preços;

- definir fiscais técnico, administrativo e gestor.

### 1.1 - Será necessária a adequação prévia do ambiente da organização para que a contratação surta efeito?

Sim, de forma pontual e controlada. A Administração deverá validar espaço em rack, energia, climatização, passagem de cabos, entrada de fibra, pontos de conexão, endereçamento, políticas de firewall, rotas, VLANs/VRFs, acesso físico às salas técnicas e integração com monitoramento. Não se identifica necessidade de obra estrutural ampla como requisito prévio ordinário.

### 1.2 - Será necessária capacitação específica ou diferenciada para servidores responsáveis pela fiscalização e gestão?

Sim. A contratada deverá realizar transferência de conhecimento para gestores e fiscais técnicos, abrangendo topologia, circuitos, rotas, QoS, abertura e acompanhamento de chamados, interpretação de relatórios de SLA, testes de contingência, documentação as built, critérios de aceite, glosas e procedimentos de escalonamento.

## XI - CONTRATAÇÕES CORRELATAS E/OU INTERDEPENDENTES

### 1 - Há correlação ou interdependência com outras contratações?

Contrato 131/2023 de SD-WAN, contratos de Internet/Anti-DDoS e eventuais contratos relativos a Infovia, redes JT, firewalls, monitoramento e segurança perimetral.

A contratação é correlata ao contrato SD-WAN vigente e às contratações de Internet da Sede. A execução deverá preservar a operação atual e ser coordenada com a área de redes, segurança, operadoras atuais e fiscalização contratual.

### 1.1 - Há risco de sobreposição de contratações similares ou com o mesmo objeto?

O risco de sobreposição é baixo quando o escopo for delimitado como rede privada MPLS para interconexão institucional, link dedicado ponto-a-ponto Sede-Foro de 25 Gbps e integração com SD-WAN vigente sem substituir integralmente o objeto desta. A SD-WAN vigente permanece como camada preferencial de Internet e contingência; o MPLS atua como camada privada para tráfego crítico; e o link Sede-Foro possui finalidade específica de replicação e redundância.

### 1.2 - É possível agrupar contratações correlatas em um só certame para ampliar economia de escala?

O agrupamento nesta contratação fica limitado aos componentes tecnicamente interdependentes da solução de comunicação de dados definida neste ETP. Contratações de firewalls, segurança perimetral, monitoramento corporativo, Infovia ou SD-WAN vigente permanecem correlatas, mas não precisam ser incorporadas ao mesmo certame porque possuem escopos, vigências e modelos operacionais próprios.

### 1.3 - Se houver interdependência cronológica, qual cronograma ou ordem deverá ser observado?

A ordem mínima será: validação de infraestrutura e inventário; emissão da ordem de serviço; entrega do plano de implantação em até 10 dias corridos; implantação da Sede e do link Sede-Foro; ativação das unidades de maior criticidade; ativação das demais unidades; testes de aceite por localidade; teste de contingência MPLS/SD-WAN e Sede/Foro; operação assistida; recebimento definitivo; e início da rotina mensal de medição e IMR.

## XII - DESCRIÇÃO DE POSSÍVEIS IMPACTOS AMBIENTAIS

### 1 - Descreva os possíveis impactos ambientais da contratação.

Impactos ambientais são baixos e restritos a equipamentos de rede, energia e eventuais adequações físicas. Mitigações: equipamentos eficientes, descarte adequado, reaproveitamento de infraestrutura existente, documentação digital e monitoramento remoto.

### 1.1 - Quais medidas mitigadoras serão adotadas?

Serão adotadas eficiência energética dos equipamentos, reaproveitamento de infraestrutura existente, documentação digital, monitoramento remoto, redução de deslocamentos, descarte ambientalmente adequado de cabos, fontes, embalagens e componentes substituídos, além de logística reversa quando aplicável.

### 1.2 - As medidas incluem baixo consumo de energia e logística reversa?

Sim. Os equipamentos fornecidos como parte do serviço deverão observar padrões compatíveis de eficiência energética e a contratada deverá destinar adequadamente resíduos, embalagens, cabos, fontes, CPEs e demais componentes substituídos, inclusive por logística reversa quando aplicável.

## XIII - POSICIONAMENTO CONCLUSIVO SOBRE A ADEQUAÇÃO DA CONTRATAÇÃO

### 1 - Explique se a contratação escolhida é adequada, viável e razoável para o atendimento da necessidade.

A contratação é tecnicamente viável, razoável e adequada. A pesquisa de preços PNCP foi incorporada ao ETP, as capacidades por localidade foram fixadas, os níveis mínimos de serviço foram definidos e a solução técnica foi estruturada com MPLS integrado à SD-WAN e link dedicado Sede-Foro de 25 Gbps. Entre as alternativas avaliadas, a Solução 1 é a mais aderente à necessidade do TRT10, pois usa o MPLS como camada privada para tráfego crítico, mantém a SD-WAN como camada preferencial de Internet, permite contingência cruzada, considera a existência de 3 saídas redundantes na Sede e fortalece disponibilidade, segurança, governança e observabilidade da rede institucional. O grupo de link dedicado Sede-Foro de 25 Gbps é tecnicamente justificável por possuir finalidade distinta da malha MPLS: replicação, backup, sincronização, baixa latência e uso do Foro como redundância da Sede.

A decisão final deste ETP é contratar MPLS para todas as localidades, em convivência com a topologia SD-WAN vigente, centralizar preferencialmente a saída de Internet na Sede, manter 3 saídas centrais com capacidade mínima combinada de 4 Gbps e contratar, em grupo próprio, link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília. A estimativa de planejamento fica definida em R$ 74.445,00 mensais e R$ 893.340,00 anuais, sem prejuízo da atualização ordinária de preços no momento da publicação caso haja decurso temporal relevante ou alteração de escopo formalmente justificada.

## XIV - RESPONSÁVEL

**Unidade: CDTEC**

Servidor responsável: Edson Mateus de Sousa

E-mail: cdtec@trt10.jus.br

Telefone: (61) 3348-1249 / 1288 / 1280 / 1188
