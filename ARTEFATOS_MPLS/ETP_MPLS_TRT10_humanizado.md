# ESTUDO TÉCNICO PRELIMINAR (ETP)

**Objeto:** Contratação de serviços continuados de comunicação de dados por MPLS, com capacidades equivalentes às capacidades dos enlaces SD-WAN vigentes em cada localidade; contratação de link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília; e contratação de links dedicados de Internet centralizados na Sede e no Foro, com Anti-DDoS e 32 IPs fixos por link.

**Unidade demandante:** Coordenadoria de Infraestrutura de Tecnologia - CDTEC

**Órgão:** Tribunal Regional do Trabalho da 10ª Região - TRT10

**Processo de referência:** SEI 0009785-67.2025.5.10.8000

**Versão:** Estudo Técnico Preliminar - arquitetura de redundância total MPLS/SD-WAN, link dedicado Sede-Foro e Internet centralizada - versão humanizada

**Data:** 12/06/2026

## Registro de Evidências e Premissas

### Fatos recuperados dos documentos anexados

- O modelo de ETP anexo estrutura o estudo em descrição da necessidade, alinhamento estratégico, requisitos, levantamento de mercado, descrição da solução, estimativas, justificativa de parcelamento, resultados esperados, providências prévias, contratações correlatas, impactos ambientais e posicionamento conclusivo.
- O processo SEI 0000030-87.2023.5.10.8000 registra contratação de link IP dedicado com SD-WAN para 10 localidades, com bandas de 1 Gbps na Sede e Foro de Brasília, 500 Mbps em Taguatinga, Palmas e Prédio de Apoio, e 100 Mbps nas demais localidades.
- Contratações públicas similares de Internet com Anti-DDoS registram a relevância de redundância, operadoras distintas, monitoramento, portal de chamados, glosas por indisponibilidade e teste de aceite.
- Documentos técnicos indicam que Foro de Brasília e Prédio de Apoio já se conectavam à Sede via MPLS e Infovia, evidenciando aderência da arquitetura de concentração em pontos centrais.
- A demanda contempla grupo próprio de link dedicado ponto-a-ponto de 25 Gbps entre o Edifício Sede e o Foro de Brasília, distinto da rede MPLS, para replicação, redundância da Sede e uso do Foro como ponto contingencial de acesso das unidades.
- O escopo definido da contratação contempla 3 links dedicados de Internet de 4 Gbps na Sede e 2 links dedicados de Internet de 2 Gbps no Foro de Brasília, todos com Anti-DDoS e 32 IPs fixos por link.
- Os links de Internet serão os únicos links de Internet do Tribunal no desenho pretendido, estruturando a centralização do acesso em Sede e Foro.
- Cada link de Internet será item próprio. Na mesma localidade, a adjudicação deverá assegurar provedores distintos, impedindo que a mesma empresa vença dois links da Sede ou dois links do Foro.
- A pesquisa PNCP foi realizada com consulta online à API pública do PNCP e download de artefatos para contratações semelhantes de MPLS, rede privada, comunicação de dados, SD-WAN/MPLS, links dedicados de Internet, Anti-DDoS, IPs fixos e interconexão por fibra.

### Inferências analíticas

- A contratação de MPLS não substitui a SD-WAN vigente; ela compõe uma arquitetura híbrida com camada privada para tráfego crítico, enquanto a SD-WAN permanece como camada de transporte e contingência.
- Os links de Internet centralizados constituem componente essencial da solução definida para esta contratação.
- A Sede será o ponto principal de egressão à Internet; o Foro será ponto redundante e poderá assumir acesso das unidades em contingência, apoiado pelo link dedicado de 25 Gbps entre os dois prédios.
- A exigência de provedores distintos por localidade reduz risco de falha comum e é coerente com precedentes PNCP que exigem links principal e redundante por empresas diferentes.
- A exigência de Anti-DDoS é proporcional à centralização dos acessos de Internet, pois a concentração aumenta a criticidade dos enlaces e exige mitigação volumétrica e lógica.
- A exigência de 32 IPs fixos por link corresponde a bloco IPv4 público /27 ou arranjo funcional equivalente, necessário para publicação controlada de serviços, NAT, segmentação de borda, contingência e políticas de segurança.
- A interligação Sede-Foro deve ser tratada como link dedicado ponto-a-ponto, e não MPLS, porque sua finalidade é criar um barramento de alta capacidade entre dois pontos centrais para replicação, backup, sincronização, baixa latência e continuidade operacional.

## I - DESCRIÇÃO DA NECESSIDADE DE CONTRATAÇÃO

### 1 - Qual a necessidade da Administração (problema a ser resolvido sob a perspectiva do interesse público)?

O TRT10 necessita contratar uma solução continuada de conectividade institucional que una rede privada MPLS, redundância com a SD-WAN vigente, interligação dedicada Sede-Foro e Internet centralizada com proteção Anti-DDoS. A finalidade é garantir disponibilidade, segurança, desempenho, previsibilidade e continuidade dos serviços digitais que sustentam a atividade jurisdicional e administrativa.

A necessidade decorre da dependência permanente de sistemas judiciais eletrônicos, autenticação, serviços internos de TIC, videoconferência, colaboração institucional, suporte remoto, monitoramento, integração com redes externas, acesso à Internet, replicação de dados, backup e continuidade de serviços. O desenho técnico definido separa os fluxos por finalidade: MPLS para comunicação privada e tráfego crítico; SD-WAN para convivência e contingência; link dedicado Sede-Foro para replicação e redundância; e Internet centralizada para egressão controlada, protegida e monitorada.

O objeto contempla 3 links de Internet dedicada de 4 Gbps na Sede e 2 links de Internet dedicada de 2 Gbps no Foro de Brasília, todos com Anti-DDoS e 32 IPs fixos por link. Esses serão os únicos links de Internet do Tribunal na arquitetura pretendida, estruturando o acesso externo em pontos centrais redundantes. A Sede será o ponto principal de saída para a Internet; o Foro será ponto redundante para continuidade de acesso em caso de indisponibilidade ou degradação da Sede.

Cada link de Internet será licitado como item separado para assegurar provedores distintos por localidade. A mesma empresa não poderá vencer dois links de Internet na Sede, nem dois links de Internet no Foro. A mesma empresa poderá vencer um item da Sede e um item do Foro, desde que atendidos os requisitos técnicos de capacidade, Anti-DDoS, 32 IPs fixos, independência operacional e disponibilidade.

A necessidade também contempla interligação dedicada de 25 Gbps entre o Edifício Sede e o Foro de Brasília. O Foro deve ser preparado como ponto de replicação e redundância da Sede, apto a receber tráfego de sincronização, backup, replicação de dados, serviços de continuidade e acesso contingencial das demais unidades quando a Sede estiver indisponível ou degradada. Esse enlace deve ser contratado como link dedicado ponto-a-ponto, LAN-to-LAN, Metro Ethernet, clear channel, E-Line, E-LAN ou tecnologia equivalente, e não como MPLS.

### 2 - A necessidade decorre de determinação legal?

Não há obrigação legal de adotar MPLS como tecnologia. A contratação se fundamenta na necessidade de garantir continuidade, disponibilidade e segurança da comunicação de dados. A Lei nº 14.133/2021 orienta o planejamento e a estruturação dos artefatos; a ENTIC-JUD 2021-2026 orienta a governança de TIC no Poder Judiciário.

### 3 - A necessidade é contínua (resulta em demanda permanente, habitual ou, ao menos, intermitente ao longo de vários anos)? Explique.

A necessidade é continuada: sem comunicação entre unidades e Sede, os serviços judiciais e administrativos perdem sustentação operacional.

A necessidade resulta em demanda permanente e habitual ao longo de vários anos, pois a conectividade entre Sede, Foro de Brasília, Prédio de Apoio, fóruns e varas é condição operacional para prestação jurisdicional, comunicação administrativa, acesso a sistemas, autenticação, segurança, monitoramento, suporte técnico, videoconferência, replicação de dados e continuidade de serviços. A contratação deve ser estruturada como serviço continuado de telecomunicações/TIC, com vigência inicial de 60 meses, prestação ininterrupta, monitoramento 24x7, manutenção, suporte, níveis mínimos de serviço e mecanismos de glosa durante toda a execução.

## II - PREVISÃO NO PLANO ESTRATÉGICO INSTITUCIONAL, PLANO DE LOGÍSTICA SUSTENTÁVEL (PLS) E PLANO DE CONTRATAÇÕES ANUAL (PCA)

### 1 - A demanda alinha-se aos objetivos do Plano Estratégico Institucional (RA 35/2021-TRT10)?

A demanda está alinhada diretamente ao Objetivo Estratégico 10 - Aprimorar a governança de TIC e a proteção de dados, pois amplia a disponibilidade, a segurança, a rastreabilidade, a governabilidade e a continuidade da infraestrutura de comunicação de dados. A contratação também contribui para a razoável duração do processo e para o aperfeiçoamento da gestão administrativa, ao reduzir riscos de indisponibilidade de sistemas judiciais, autenticação, videoconferência, suporte remoto, monitoramento e serviços corporativos.

| Nº | Objetivo estratégico | Alinhamento |
|---|---|---|
| 3 | Garantir a razoável duração do processo | Contribuição indireta pela continuidade dos sistemas judiciais e serviços digitais. |
| 7 | Aperfeiçoar a Governança, a Gestão Estratégica e a Gestão Administrativa | Contribuição indireta pela padronização de operação, monitoramento, SLA e gestão de rede. |
| 10 | Aprimorar a governança de TIC e a proteção de dados | Alinhamento direto, por fortalecer disponibilidade, segurança, redundância e governança de TIC. |

### 2 - A demanda observa o Plano de Logística Sustentável (PLS)?

Sim. Há alinhamento com o uso eficiente de recursos de TIC, redução de deslocamentos por indisponibilidade técnica, melhor uso de serviços digitais, monitoramento remoto, documentação digital, reaproveitamento de infraestrutura existente e racionalização da infraestrutura de comunicação.

### 3 - A demanda está prevista no Plano de Contratações Anual (PCA)?

Providência administrativa: a contratação deve constar do PCA/SIGPLAC antes da publicação do edital. Caso a demanda ainda não esteja cadastrada, deve ser incluída como demanda superveniente, com justificativa vinculada à continuidade dos serviços de comunicação institucional, à redundância total da arquitetura SD-WAN/MPLS e à interligação dedicada Sede-Foro para replicação e contingência.

## III - REQUISITOS DA CONTRATAÇÃO E CRITÉRIOS DE SUSTENTABILIDADE E ACESSIBILIDADE

### 1 - Quais são os requisitos necessários e suficientes para a escolha da solução?

Os requisitos necessários e suficientes são os requisitos funcionais, técnicos, operacionais, de segurança, desempenho, disponibilidade, suporte, sustentabilidade e fiscalização descritos neste item. Eles são definidos por desempenho e resultado, sem indicação de marca, fabricante ou modelo específico.

#### 1.1 - Quais são as especificações mínimas do objeto da contratação para que a necessidade da Administração possa ser satisfatoriamente atendida?

Para que a necessidade da Administração seja atendida satisfatoriamente, o objeto deverá contemplar uma solução continuada de comunicação de dados corporativa, em rede privada MPLS L3 VPN ou tecnologia funcionalmente equivalente, capaz de interconectar todas as unidades do TRT10 à Sede, coexistir com a SD-WAN vigente e permitir operação com preferência de tráfego e contingência cruzada.

As especificações mínimas abaixo constituem a definição técnica do ETP e devem ser reproduzidas no Termo de Referência e no instrumento contratual, sem redução de capacidade, disponibilidade, segurança, suporte ou critérios de aceite.

#### a) Escopo mínimo do serviço

A contratação deve incluir, no mínimo:

- prestação de serviço continuado de comunicação de dados por rede privada corporativa MPLS L3 VPN ou tecnologia equivalente;

- interconexão da Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga, Foro de Palmas, Vara do Gama, Foro de Araguaína, Vara de Gurupi, Vara de Dianópolis e Vara de Guaraí;

- interligação dedicada ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, em grupo próprio, por fibra óptica, LAN-to-LAN/Metro Ethernet ou tecnologia equivalente;

- fornecimento, instalação, configuração, ativação, operação, manutenção e suporte dos circuitos;

- fornecimento dos CPEs, roteadores, modems, transceptores, fontes, cabos, licenças e demais elementos necessários à prestação do serviço, quando não forem expressamente indicados como responsabilidade do TRT10;

- monitoramento 24x7 dos circuitos e equipamentos sob responsabilidade da contratada;

- central de atendimento, registro de chamados, escalonamento técnico e relatórios mensais;

- documentação técnica inicial, documentação as built e atualização após mudanças relevantes.

#### b) Arquitetura mínima

A solução deve adotar topologia lógica com a Sede como concentrador preferencial, mantendo todas as demais localidades interconectadas à Sede por MPLS. A Sede deve permanecer como ponto preferencial de aplicação das políticas de segurança e observabilidade. A saída de Internet institucional será provida pelos links dedicados de Internet definidos neste objeto, com a Sede como ponto principal e o Foro de Brasília como ponto redundante.

A arquitetura deve permitir:

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

Grupo específico de Internet dedicada centralizada:

| Item | Localidade | Tecnologia mínima | Capacidade | Requisito de diversidade | Papel técnico |
|---|---|---|---|---|---|
| 12 | Edifício Sede | Internet dedicada simétrica por fibra óptica, com Anti-DDoS e 32 IPs fixos | 4 Gbps | Provedor distinto dos itens 13 e 14 | Egressão principal de Internet |
| 13 | Edifício Sede | Internet dedicada simétrica por fibra óptica, com Anti-DDoS e 32 IPs fixos | 4 Gbps | Provedor distinto dos itens 12 e 14 | Egressão principal de Internet |
| 14 | Edifício Sede | Internet dedicada simétrica por fibra óptica, com Anti-DDoS e 32 IPs fixos | 4 Gbps | Provedor distinto dos itens 12 e 13 | Egressão principal de Internet |
| 15 | Foro de Brasília | Internet dedicada simétrica por fibra óptica, com Anti-DDoS e 32 IPs fixos | 2 Gbps | Provedor distinto do item 16 | Egressão redundante de Internet |
| 16 | Foro de Brasília | Internet dedicada simétrica por fibra óptica, com Anti-DDoS e 32 IPs fixos | 2 Gbps | Provedor distinto do item 15 | Egressão redundante de Internet |

Os circuitos devem ser simétricos, full duplex, com banda útil compatível com a capacidade contratada, ressalvados apenas os overheads inerentes aos protocolos de comunicação.

Os links de Internet da Sede e do Foro compõem o objeto desta contratação, em itens próprios, com capacidade, Anti-DDoS, endereçamento fixo e regra de diversidade de provedores definidos neste ETP. A solução MPLS, o link dedicado Sede-Foro e os links de Internet deverão interoperar com firewalls, roteadores, DNS, monitoramento, autenticação, redes internas, redes da Justiça do Trabalho, Infovia e demais componentes de borda e segurança do TRT10, preservando as responsabilidades de cada contrato ou componente técnico.

A equivalência entre MPLS e SD-WAN não significa duplicidade indevida de objeto, pois as camadas possuem papéis técnicos complementares: a SD-WAN utiliza transporte por Internet dedicada, túneis, orquestração e políticas de acesso; o MPLS fornece rede privada corporativa, isolamento lógico, QoS e caminho controlado para interconexão. A duplicação de capacidade nominal decorre da finalidade de redundância integral, e não da repetição desnecessária de uma mesma solução.

O link dedicado de 25 Gbps Sede-Foro possui natureza distinta da rede MPLS das localidades. Ele não é enlace MPLS de filial, mas circuito de alta capacidade entre dois pontos centrais, voltado a replicação, continuidade, contingência e baixa latência. Por isso, deverá compor grupo próprio na modelagem da contratação e na pesquisa de preços.

#### c.1) Itens complementares definidos para a contratação

A contratação contempla os seguintes itens complementares, que integram o escopo mínimo da solução:

- equipamentos de borda, roteadores, CPEs ou integração com firewalls existentes, sem vinculação a marca específica;

- serviços de implantação, configuração, testes de aceite, documentação e transferência de conhecimento;

- monitoramento 24x7 dos links, alertas de indisponibilidade e relatórios mensais de SLA;

- suporte técnico 24x7, com início de atendimento em até 30 minutos para falha crítica, até 1 hora para degradação relevante e até 4 horas úteis para chamados ordinários;

- endereçamento, roteamento, QoS, segmentação e políticas de segurança documentadas no projeto executivo e na documentação as built.

#### d) Roteamento, segregação e QoS

A solução deve suportar roteamento controlado e integração com a infraestrutura existente do TRT10 por OSPF como protocolo preferencial para integração interna e por BGP quando houver necessidade de troca de rotas com bordas de operadoras, datacenter, Internet ou ambiente autônomo. O roteamento estático somente será aceito para enlaces simples, rotas de contingência, rotas de gerenciamento ou situações em que a área técnica do TRT10 aprove formalmente sua simplicidade e menor risco. Estabelecem-se como requisitos mínimos: anúncio apenas das redes autorizadas pelo TRT10; métricas que priorizem MPLS para tráfego crítico e SD-WAN para Internet em operação normal; failover automático ou semiautomático documentado; retorno controlado ao caminho preferencial após estabilização mínima de 15 minutos; filtros contra rotas indevidas; e mecanismos para prevenção de loops.

A solução deve prover isolamento lógico do tráfego do TRT10, por VRF ou mecanismo equivalente, e suportar QoS com classes de serviço configuráveis. Ficam definidas, no mínimo, as seguintes classes de tráfego:

- tráfego crítico de sistemas judiciais, autenticação, serviços internos e administração;

- tráfego sensível a tempo, como voz, vídeo e colaboração, quando aplicável;

- tráfego corporativo administrativo;

- tráfego de melhor esforço.

As marcações e reservas mínimas de QoS ficam definidas assim: classe crítica, com DSCP AF31/CS3 ou marcação equivalente e reserva mínima de 35% da banda; voz/vídeo institucional, com DSCP EF/AF41 ou marcação equivalente e reserva mínima de 20%; tráfego corporativo administrativo, com DSCP AF21 ou equivalente e reserva mínima de 25%; monitoramento, gerenciamento e backup operacional, com reserva mínima de 5%; e melhor esforço, com uso da banda remanescente. As filas poderão aproveitar banda ociosa entre classes, mas, em congestionamento, a classe crítica e voz/vídeo terão prioridade de encaminhamento e menor descarte.

#### e) Disponibilidade, desempenho e suporte

A solução deve observar disponibilidade mensal mínima de 99,90% para a Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga e Foro de Palmas, e de 99,70% para Gama, Araguaína, Gurupi, Dianópolis e Guaraí. O link dedicado Sede-Foro de 25 Gbps deve observar disponibilidade mensal mínima de 99,95%.

Estabelecem-se os níveis mínimos de serviço:

- início de atendimento: até 30 minutos para indisponibilidade total, até 1 hora para degradação severa e até 4 horas úteis para chamados ordinários;

- prazo de reparo: até 4 horas para Sede, Foro de Brasília e link dedicado Sede-Foro; até 6 horas para demais localidades do DF; até 8 horas para localidades do Tocantins;

- manutenção programada: janela preferencial das 22h às 6h, com aviso prévio mínimo de 5 dias úteis, plano de rollback e autorização do TRT10 quando houver risco de impacto;

- fórmula de disponibilidade: disponibilidade mensal = ((tempo total mensal - tempo indisponível imputável à contratada) / tempo total mensal) x 100;

- hipóteses de glosa: 5% da mensalidade do circuito quando a disponibilidade ficar abaixo da meta e até 0,5 ponto percentual abaixo dela; 10% quando a queda exceder 0,5 ponto e for até 1 ponto percentual; 20% quando a queda exceder 1 ponto percentual; e 30% quando houver indisponibilidade superior a 24 horas acumuladas no mês, sem afastar sanções;

- aferição: relatórios mensais da contratada, registros de monitoramento, chamados, evidências da fiscalização técnica e testes sob demanda;

- desempenho mínimo: perda média de pacotes inferior a 1%; jitter médio inferior a 30 ms para tráfego sensível; latência média mensal até a Sede inferior a 30 ms para localidades no DF e inferior a 80 ms para localidades no Tocantins, ressalvadas medições afetadas por falha comprovada em infraestrutura do contratante ou evento de força maior.

#### f) Implantação, testes e aceite

A contratada deve apresentar plano de implantação antes da ativação dos circuitos, contendo cronograma, pré-requisitos, responsáveis, janelas de mudança, testes, riscos e plano de rollback. A implantação deve ocorrer preferencialmente por fases, iniciando pela Sede e pelas unidades de maior criticidade.

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

- para o link dedicado Sede-Foro de 25 Gbps: throughput compatível com a capacidade contratada, latência, perda, redundância física declarada quando ofertada, identificação de portas/interfaces, caminho lógico, testes de replicação/sincronização e acionamento do Foro como ponto contingencial;

- para os links de Internet: banda contratada, roteamento, BGP quando aplicável, entrega dos 32 IPs fixos, teste de Anti-DDoS por simulação controlada ou evidência técnica aceita pela fiscalização, independência de provedor na mesma localidade, DNS reverso quando aplicável, latência, perda, jitter e relatório de ativação;

- entrega de documentação as built.

#### g) Segurança e confidencialidade

A contratada deve preservar o sigilo das informações de rede, endereçamento, rotas, configurações, chamados e incidentes. Deverá manter controle de acesso administrativo aos equipamentos sob sua responsabilidade, registrar mudanças relevantes e comunicar incidentes que possam afetar disponibilidade, integridade, confidencialidade ou continuidade do serviço.

#### h) Vedação a direcionamento

As especificações devem ser descritas por requisitos funcionais e de desempenho, sem indicação de marca, fabricante, modelo ou solução proprietária específica, salvo quando indispensável e devidamente justificado. Deverá ser admitida tecnologia equivalente ao MPLS quando demonstrada aderência funcional aos requisitos de rede privada, isolamento, QoS, roteamento controlado, monitoramento e SLA.

### 1.1.2 Será necessário exigir garantia contratual do objeto, complementar a legal?

Sim. Exige-se garantia contratual do objeto durante toda a vigência da contratação, complementar às garantias legais aplicáveis, abrangendo o funcionamento dos circuitos, CPEs, roteadores, modems, fontes, transceptores, licenças, configurações, monitoramento, suporte técnico e demais componentes fornecidos ou operados pela contratada.

A garantia do objeto deverá assegurar que falhas, defeitos, indisponibilidades ou degradações imputáveis à contratada sejam corrigidos sem ônus adicional para o TRT10, observados os prazos de atendimento, reparo, disponibilidade e demais níveis mínimos de serviço definidos neste ETP e reproduzidos no instrumento contratual.

Essa garantia do objeto não substitui a garantia de execução contratual eventualmente exigida, nem afasta a glosas, sanções, obrigações de reparo, substituição de equipamentos, manutenção corretiva ou demais medidas previstas no instrumento contratual.

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

Assim, para esta contratação, a garantia contratual do objeto fica definida como obrigação de manter os circuitos MPLS, o link dedicado Sede-Foro de 25 Gbps, os equipamentos fornecidos, as configurações, o monitoramento e o suporte em condições regulares de funcionamento durante toda a vigência contratual. Falhas, defeitos, degradações, indisponibilidades ou incompatibilidades imputáveis à contratada devem ser corrigidos sem custo adicional ao TRT10, observados os prazos de atendimento, reparo, disponibilidade, desempenho e glosas previstos neste ETP.

#### 1.2 - Quais são as características mínimas do modelo de execução da contratação para que a necessidade da Administração possa ser satisfatoriamente atendida?

O modelo de execução deve permitir implantação controlada, operação continuada, fiscalização objetiva e preservação da conectividade institucional durante a entrada em produção. Para tanto, deverá contemplar, no mínimo:

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

- glosas e sanções em caso de descumprimento dos níveis de serviço definidos neste ETP e no contrato.

O modelo deverá prever recebimento provisório por localidade após ativação e teste, e recebimento definitivo após período de observação, saneamento de pendências e validação pela fiscalização técnica.

A implantação será faseada para preservar a continuidade da SD-WAN vigente e reduzir risco operacional:

| Fase | Escopo | Objetivo |
|---|---|---|
| 1 | Sede | Implantar concentrador principal, roteamento, segurança e integração com infraestrutura existente de Internet/borda |
| 2 | Gama e Taguatinga | Atender unidades com maior sensibilidade contratual histórica |
| 3 | Prédio de Apoio e Palmas | Integrar unidades de demanda intermediária |
| 4 | Araguaína, Gurupi, Dianópolis e Guaraí | Concluir capilaridade MPLS e contingência das unidades remotas |
| 5 | Operação assistida | Validar failover, QoS, desempenho, monitoramento e documentação final |

### 1.2.1 Será admitida a subcontratação? Se sim, apresente as justificativas, bem como indique seus limites e partes do objeto.

Sim. Fica admitida subcontratação apenas para atividades acessórias de infraestrutura local, lançamento de fibra, obras civis leves, passagem de cabos, adequações físicas, vistorias, instalação de último trecho e atendimento de campo, mantendo a contratada principal integralmente responsável pela prestação do serviço, pelo SLA, pela segurança, pela documentação, pelo suporte, pela operação e pela manutenção da solução.

A justificativa para admitir subcontratação limitada decorre da natureza distribuída da solução, que envolve localidades no Distrito Federal e no Tocantins, podendo exigir equipes locais, acesso à infraestrutura regional, serviços de campo e atividades acessórias que não representam a gestão técnica central do serviço de comunicação de dados.

Não deve ser admitida subcontratação que transfira a responsabilidade principal pela rede privada corporativa, pela gerência dos circuitos, pelo cumprimento do SLA, pelo atendimento ao TRT10, pela segurança das informações ou pela integração técnica com a arquitetura MPLS/SD-WAN. A contratada principal deve responder integralmente por atos, omissões, falhas e atrasos de suas subcontratadas.

### 1.2.2 Os riscos ou características da contratação tornam recomendável a exigência de garantia de execução contratual?

Sim. Fica definida a exigência de garantia de execução contratual, considerando o valor estimado, a criticidade do serviço, a quantidade de localidades, a necessidade de implantação coordenada, o fornecimento de equipamentos, a dependência de SLA e o impacto operacional de eventual inadimplemento.

A garantia de execução contratual fica definida em 5% do valor anual estimado da contratação, admitidas as modalidades previstas na Lei nº 14.133/2021, com manutenção durante toda a vigência contratual e 90 dias após seu encerramento. A garantia deverá cobrir atraso de implantação, indisponibilidade de circuitos, falha de integração MPLS/SD-WAN, descumprimento de níveis de serviço, danos causados à Administração, obrigações trabalhistas/previdenciárias quando aplicáveis e multas não pagas. A contratada deve recompor a garantia em até 10 dias úteis quando houver utilização parcial ou acréscimo contratual.

### 3.1 Requisitos do objeto

Requisitos mínimos definidos:

- rede MPLS L3 VPN ou tecnologia equivalente de rede privada corporativa, desde que preserve isolamento lógico, QoS e roteamento controlado;

- interconexão das demais localidades à Sede;

- fornecimento de CPEs, modems, transceptores, cabos, licenças e demais itens necessários;

- compatibilidade com roteamento dinâmico, adotando OSPF como protocolo preferencial de integração interna e BGP para bordas de Internet, ASN próprio, troca de rotas com operadoras ou cenários em que a CDTEC defina essa necessidade operacional;

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

Exigir equipamentos com eficiência energética compatível com o mercado, descarte ambientalmente adequado de equipamentos substituídos, redução de deslocamentos por monitoramento remoto e atendimento as normas trabalhistas, ambientais e de segurança aplicáveis.

### 3.4.1 Quais os critérios e práticas de sustentabilidade e acessibilidade cabíveis ou exigíveis, no caso?

Considerando a natureza da contratação, os critérios de sustentabilidade e acessibilidade cabíveis devem ser compatibilizados com serviços continuados de telecomunicações, comunicação de dados, infraestrutura de rede e atendimento técnico. São critérios e práticas recomendáveis:

- priorização de equipamentos com eficiência energética compatível com as práticas de mercado;

- uso de equipamentos, fontes e acessórios em conformidade com normas técnicas e regulamentos aplicáveis;

- descarte ambientalmente adequado de equipamentos, cabos, fontes, baterias, embalagens e demais resíduos sob responsabilidade da contratada;

- redução de deslocamentos mediante monitoramento remoto, abertura remota de chamados, diagnóstico remoto e atendimento presencial apenas quando necessário;

- consolidação de relatórios em meio digital;

- reaproveitamento de infraestrutura existente sempre que tecnicamente possível e autorizado;

- uso de janelas de manutenção planejadas para reduzir retrabalho e deslocamentos;

- observância de normas de segurança do trabalho nas atividades de instalação, lançamento de cabos, acesso a salas técnicas, racks, forros, shafts e demais ambientes;

- garantia de que instalações físicas, passagem de cabos e acomodação de equipamentos não prejudiquem rotas de circulação, acessibilidade física, segurança predial ou sinalização;

- atendimento a requisitos de sigilo, proteção de informações e minimização de acesso a dados de rede;

- preferência por documentação digital, as built eletrônico e relatórios mensais em formato pesquisável.

### 3.4.2 Caso não aplicáveis critérios de sustentabilidade e acessibilidades, apresentar as justificativas.

Os critérios de sustentabilidade e acessibilidade são aplicáveis proporcionalmente ao objeto. Não se trata de contratação de obra, aquisição massiva de bens permanentes ou solução diretamente voltada ao atendimento ao público, razão pela qual alguns critérios típicos de obras, mobiliário, edificações, materiais de consumo ou acessibilidade de interfaces digitais podem não ser pertinentes.

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

### 3.6 No caso de compras, é necessário analisar amostras?

Não se aplica como regra principal, pois o objeto pretendido é serviço continuado de comunicação de dados, e não compra isolada de bens. Não serão exigidas amostras físicas como critério ordinário de aceitação da proposta. Equipamentos, CPEs, licenças e acessórios integram a prestação do serviço e serão avaliados por requisitos funcionais, documentação técnica, projeto executivo, testes de ativação e aceite por localidade.

Para os equipamentos fornecidos como parte do serviço, a licitante deve apresentar catálogos, datasheets ou declarações técnicas suficientes para comprovar compatibilidade com as capacidades contratadas, interfaces, roteamento, QoS, monitoramento, energia e instalação, sem direcionamento por marca ou modelo.

### 3.7 No caso de serviços, é necessário vistoria prévia do local da execução dos serviços?

A vistoria prévia será facultativa, e não obrigatória, podendo ser substituída por declaração da licitante de que conhece as condições locais e assume responsabilidade pela formulação de sua proposta. Essa definição reduz risco de restrição indevida à competitividade e preserva a possibilidade de participação de fornecedores que consigam estimar custos por documentação, mapas, endereços, inventário técnico e informações disponibilizadas no edital.

A vistoria facultativa poderá ser disponibilizada para as localidades do TRT10, mediante agendamento, especialmente quando houver necessidade de verificar entrada de fibra, sala técnica, rack, energia, infraestrutura de passagem, espaço para CPE, restrições prediais ou condições de acesso. A ausência de vistoria não deve justificar pedidos posteriores de acréscimo de custos, desde que o edital disponibilize informações mínimas suficientes sobre as localidades e condições de execução.

### 3.8 É necessária autorização do poder público para o exercício da atividade a ser contratada (habilitação jurídica)?

Sim. Por se tratar de serviço de telecomunicações/comunicação de dados, deve ser exigida, quando aplicável, comprovação de autorização, outorga, licença ou instrumento regulatório pertinente para prestação dos serviços, nos termos da regulamentação setorial vigente.

Em princípio, a contratada deverá demonstrar regularidade para prestação de Serviço de Comunicação Multimídia (SCM) ou outro enquadramento regulatório aplicável ao serviço efetivamente ofertado, junto a Anatel, diretamente ou por arranjo juridicamente admitido. Caso a licitante utilize infraestrutura, autorização ou serviços de terceiros, deverá demonstrar que tal arranjo não transfere ao TRT10 riscos de irregularidade regulatória, descontinuidade ou ausência de responsabilidade contratual.

A exigência deve ser redigida de forma funcional e proporcional, evitando restringir indevidamente a competição, mas assegurando que a futura contratada esteja apta a prestar os serviços de telecomunicações objeto da contratação.

### 3.9 Será necessário exigir qualificações econômico-financeiras adicionais?

Sim. Exigem-se as qualificações econômico-financeiras ordinárias previstas na legislação e no edital, incluindo balanço patrimonial e demonstrações contábeis do último exercício social, quando aplicáveis, e comprovação de índices contábeis compatíveis com contratação continuada essencial. Quando algum índice mínimo não for atendido, admitir-se-á comprovação alternativa de patrimônio líquido mínimo de 10% do valor estimado anual da contratação, observado o limite legal e a proporcionalidade. Não se exige capital social mínimo cumulativo com patrimônio líquido mínimo. Os riscos econômico-financeiros serão complementados por garantia de execução contratual de 5%, pagamentos mensais condicionados ao aceite, glosas por descumprimento de SLA e fiscalização contratual.

### 3.10 Será necessário exigir qualificações técnicas técnico-operacional e técnico-profissional especiais?

Sim. Exige-se qualificação técnico-operacional compatível com a complexidade do objeto, especialmente porque a solução envolve rede privada corporativa, múltiplas localidades, SLA, monitoramento, suporte, roteamento, QoS, integração com SD-WAN e continuidade de serviços críticos.

A qualificação técnico-operacional deve comprovar experiência anterior da licitante em prestação de serviço semelhante, contemplando, no mínimo:

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

### 1 - Qual é a estimativa da quantidade a ser contratada?

A contratação compreende de 10 circuitos MPLS mensais, correspondentes às 10 localidades do TRT10 abrangidas pela arquitetura de comunicação de dados: Edifício Sede, Foro de Brasília, Prédio de Apoio, Foro de Taguatinga, Foro de Palmas, Vara do Gama, Foro de Araguaína, Vara de Gurupi, Vara de Dianópolis e Vara de Guaraí.

Também fica definida a contratação de 1 link dedicado ponto-a-ponto de 25 Gbps entre a Sede e o Foro de Brasília, em grupo próprio, para replicação, sincronização, backup, redundância da Sede e acesso contingencial das unidades ao Foro em cenários de indisponibilidade ou degradação da Sede.

Além disso, ficam definidos 5 links dedicados de Internet centralizados: 3 links de 4 Gbps na Sede e 2 links de 2 Gbps no Foro de Brasília. Cada link deve incluir Anti-DDoS e 32 IPs fixos. Esses enlaces serão os únicos links de Internet do Tribunal na arquitetura pretendida.

| Item | Localidade / enlace | Quantidade | Capacidade definida | Tecnologia / finalidade |
|---|---:|---:|---:|---|
| 1 | Edifício Sede | 1 circuito | 1 Gbps | MPLS; concentrador preferencial |
| 2 | Foro de Brasília | 1 circuito | 1 Gbps | MPLS; unidade de alta demanda e ponto de redundância |
| 3 | Prédio de Apoio | 1 circuito | 500 Mbps | MPLS; unidade metropolitana |
| 4 | Foro de Taguatinga | 1 circuito | 500 Mbps | MPLS; unidade regional do DF |
| 5 | Foro de Palmas | 1 circuito | 500 Mbps | MPLS; polo regional do Tocantins |
| 6 | Vara do Gama | 1 circuito | 100 Mbps | MPLS; unidade remota |
| 7 | Foro de Araguaína | 1 circuito | 100 Mbps | MPLS; unidade remota |
| 8 | Vara de Gurupi | 1 circuito | 100 Mbps | MPLS; unidade remota |
| 9 | Vara de Dianópolis | 1 circuito | 100 Mbps | MPLS; unidade remota |
| 10 | Vara de Guaraí | 1 circuito | 100 Mbps | MPLS; unidade remota |
| 11 | Sede ↔ Foro de Brasília | 1 link | 25 Gbps | Link dedicado ponto-a-ponto, não MPLS, para replicação e redundância |
| 12 | Sede | 1 link | 4 Gbps | Internet dedicada; provedor distinto; Anti-DDoS; 32 IPs fixos |
| 13 | Sede | 1 link | 4 Gbps | Internet dedicada; provedor distinto; Anti-DDoS; 32 IPs fixos |
| 14 | Sede | 1 link | 4 Gbps | Internet dedicada; provedor distinto; Anti-DDoS; 32 IPs fixos |
| 15 | Foro de Brasília | 1 link | 2 Gbps | Internet dedicada; provedor distinto; Anti-DDoS; 32 IPs fixos |
| 16 | Foro de Brasília | 1 link | 2 Gbps | Internet dedicada; provedor distinto; Anti-DDoS; 32 IPs fixos |

### 1.1 - Apresente a memória de cálculo e os documentos que dão suporte à quantidade indicada.

A memória de quantidades decorre do mapa de localidades do TRT10, da topologia SD-WAN vigente, da premissa técnica de redundância total, da interligação dedicada Sede-Foro e da Internet centralizada em dois pontos institucionais. A regra de cálculo adotada é objetiva: cada localidade institucional abrangida pela solução corresponde a 1 circuito MPLS; cada circuito MPLS recebe capacidade equivalente à capacidade SD-WAN vigente naquela localidade; a interligação Sede-Foro recebe 1 link dedicado próprio de 25 Gbps; a Sede recebe 3 links de Internet de 4 Gbps; e o Foro recebe 2 links de Internet de 2 Gbps.

Os documentos que dão suporte à quantidade indicada são:

| Documento / evidência | Contribuição para a estimativa de quantidade |
|---|---|
| Processo SEI 0000030-87.2023.5.10.8000 | Indica a topologia SD-WAN vigente e as capacidades por localidade: 1 Gbps na Sede e Foro, 500 Mbps em Taguatinga, Palmas e Prédio de Apoio, e 100 Mbps nas demais localidades. |
| DFD do processo SEI 0009785-67.2025.5.10.8000 | Consolida a necessidade de manter a topologia SD-WAN vigente e contratar MPLS com capacidades equivalentes. |
| Requisito inicial de Internet centralizada | Define 3 links de 4 Gbps na Sede e 2 links de 2 Gbps no Foro, todos com Anti-DDoS e 32 IPs fixos. |
| Contratações públicas similares de Internet/Anti-DDoS e comunicação de dados | Demonstram a relevância de redundância, monitoramento, SLA, portal de chamados, glosas por indisponibilidade e operação com provedores distintos. |
| Pesquisa PNCP em `PNCP_REFERENCIAS_MPLS` e `PNCP_REFERENCIAS_INTERNET` | Confirma práticas de contratação por circuito, capacidade, localidade, link dedicado, Anti-DDoS, IPs fixos, SLA, equipamentos e suporte. |

### 1.2 - Há expectativa de aumento ou diminuição da demanda no futuro?

Há expectativa de crescimento gradual da demanda por capacidade, especialmente nos pontos centrais. A comunicação entre unidades e Sede é permanente e tende a se intensificar em razão do aumento do uso de sistemas eletrônicos, videoconferência, autenticação centralizada, serviços em nuvem, tráfego de segurança, monitoramento, administração remota, backup, replicação e continuidade.

Não se projeta redução da demanda como premissa. Eventual redução futura dependerá de desativação, mudança de endereço, consolidação de unidade, alteração de arquitetura, migração tecnológica ou decisão administrativa. A contratação deve permitir ajustes de capacidade dentro dos limites legais, mediante medição de tráfego, justificativa técnica e preservação da vantajosidade.

### 1.3 - Foram analisadas as eventuais interdependências com outras contratações, para possibilitar economia de escala?

Sim. Foram analisadas interdependências com SD-WAN vigente, Infovia, redes da Justiça do Trabalho, firewalls, segurança perimetral, monitoramento, energia, climatização, cabeamento, datacenter, DNS e autenticação. A economia de escala foi internalizada no próprio objeto, reunindo MPLS, link dedicado Sede-Foro e links de Internet centralizados, mas com parcelamento específico dos links de Internet para garantir provedores distintos por localidade.

Não se agrupam firewalls, SD-WAN, Infovia ou monitoramento corporativo como novos objetos principais, pois possuem escopos especializados e ciclos próprios. A integração será tratada no projeto executivo.

### 1.4 - No caso de indicativo para uso do Sistema de Registro de Preços, a expectativa é de a necessidade anual se repetir no ano seguinte (prorrogação da ARP com renovação de quantitativos), ou a eventual prorrogação visaria apenas concluir os pedidos remanescentes do ano anterior (prorrogação da ARP sem renovação de quantitativos)?

Não há indicativo principal para adoção do Sistema de Registro de Preços. O objeto corresponde a serviço continuado, essencial, com quantitativo conhecido, localidades definidas e necessidade permanente. A modelagem mais aderente é contratação ordinária de serviço continuado, com medição mensal, SLA, glosas e possibilidade de ajustes dentro dos limites legais.

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

Do ponto de vista arquitetural, a Sede possui papel natural de concentrador porque abriga políticas de segurança perimetral, integrações institucionais, concentração de serviços corporativos e os 3 links dedicados de Internet de 4 Gbps que compõem a egressão principal do Tribunal. A interconexão das unidades à Sede por MPLS fornece caminho controlado para sistemas críticos e, ao mesmo tempo, preserva a borda central de Internet protegida por Anti-DDoS, com contingência pelo Foro de Brasília. Essa separação reduz competição entre fluxos de natureza distinta e permite aplicar QoS, priorização, monitoramento e glosas por circuito.

A Solução 2, baseada em links satelitais, é tecnicamente possível, mas deve ser tratada como alternativa complementar ou de contingência específica, não como desenho preferencial para todo o ambiente. A latência e a variabilidade de desempenho podem afetar autenticação, sessões de sistemas, voz, vídeo, replicações e outros fluxos sensíveis. Sua melhor aplicação seria para localidades sem viabilidade terrestre ou para plano de continuidade de negócios em cenários extremos.

A Solução 3, baseada em Internet comum com VPN ponto a ponto, reduz barreiras iniciais, mas transfere para a Administração maior complexidade operacional e maior dependência de redes públicas. Embora VPNs possam prover confidencialidade, elas não equivalem a QoS fim a fim, previsibilidade de backbone, isolamento operacional e SLA privado. A multiplicação de túneis também pode dificultar mudanças, troubleshooting, gestão de chaves, auditoria e evolução da topologia.

### 4.3 Solução escolhida

A solução escolhida é a Solução 1: uso integrado de MPLS e SD-WAN, com MPLS contratado na mesma capacidade nominal dos links SD-WAN vigentes por localidade. O MPLS será contratado para interconectar as unidades à Sede e transportar preferencialmente tráfego crítico de sistemas institucionais, serviços internos, autenticação, administração e integrações. A SD-WAN vigente permanecerá como camada preferencial para Internet. Em caso de falha, degradação relevante ou manutenção de uma das camadas, a arquitetura deve permitir contingência cruzada, de modo que MPLS e SD-WAN possam transportar os fluxos necessários à continuidade dos serviços sem redução planejada de capacidade nominal.

A escolha da Solução 1 fica definida neste ETP. A pesquisa de preços já realizada sustenta a estimativa de planejamento, as capacidades por localidade estão fixadas na tabela de quantitativos, as políticas mínimas de QoS estão definidas neste documento e a integração de roteamento será executada conforme os requisitos técnicos de OSPF/BGP, métricas, filtros e failover aqui estabelecidos.

### 2 - Foram analisadas contratações similares realizadas por outros órgãos e entidades, para identificar a existência de novas metodologias, tecnologias ou inovações que melhor atendam às necessidades da Administração? Relacione-as.

Sim. Foram analisadas contratações similares realizadas por outros órgãos e entidades, especialmente processos publicados no PNCP envolvendo MPLS, rede privada corporativa, comunicação de dados, SD-WAN/MPLS, LAN-to-LAN, Metro Ethernet, fibra dedicada, links dedicados de alta capacidade, suporte técnico, monitoramento, SLA, disponibilidade e equipamentos sob responsabilidade da contratada. Os artefatos disponíveis foram baixados para a pasta `PNCP_REFERENCIAS_MPLS` e utilizados como referência para identificar metodologias de contratação, práticas técnicas e elementos de inovação aplicáveis ao TRT10.

Em 12/06/2026, foram realizadas consultas online adicionais à API pública do PNCP, pelo método textual `https://pncp.gov.br/api/search/`, com posterior consulta aos endpoints públicos de itens e resultados. As buscas usaram os termos "internet dedicada 4 Gbps anti-ddos IP fixo", "internet 2 Gbps anti-ddos", "MPLS 1 Gbps rede privada", "serviço lan-to-lan fibra óptica 10 Gbps", "metro ethernet ponto a ponto fibra 10 Gbps" e "link dedicado ponto a ponto datacenter fibra". As consultas reforçaram Ipojuca/PE para 4 Gbps, identificaram CLDF e IPEA como referências diretas para 2 Gbps com Anti-DDoS, reforçaram Chapecó/SC para MPLS e localizaram Ubarana/SP e Água Clara/MS como referências técnicas de LAN-to-LAN/interligação de dados. As referências sem aderência plena foram tratadas como auxiliares, sem extrapolação automática de preço unitário.

| Órgão / entidade | Pregão, processo e PNCP | Objeto similar identificado | Metodologia, tecnologia ou inovação observada | Aproveitamento no ETP do TRT10 |
|---|---|---|---|---|
| CODEVASF - Companhia de Desenvolvimento dos Vales do São Francisco e do Parnaíba | Pregão Eletrônico nº 90003/2025; Processo nº 59500002693202462; PNCP nº 00399857000126-1-000049/2025 | Rede corporativa WAN com tecnologia MPLS, instalação e configuração de equipamentos, enlaces de comunicação, gerenciamento proativo contra falhas e interligação da Administração Central com 16 Superintendências Regionais. | Contratação estruturada por localidades/enlaces; rede VPN/MPLS isolada; disponibilidade medida por enlace incluindo CPE; solução de gerenciamento; relatórios mensais; possibilidade limitada de subcontratação de última milha com responsabilidade integral da contratada; equipamentos de propriedade e responsabilidade da contratada. | Reforça a adoção de MPLS como camada privada corporativa, a modelagem por circuitos/localidades, a exigência de monitoramento, SLA por enlace, gestão de CPEs pela contratada e responsabilização única mesmo quando houver última milha subcontratada. |
| ANCINE - Agência Nacional do Cinema | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025 | Solução de acesso à Internet e rede de dados privada MPLS com SD-WAN. | Integração de MPLS com SD-WAN; suporte técnico 24x7x365; assistência técnica abrangendo instalação, desinstalação e substituição de equipamentos; SLA para recuperação de indisponibilidade; preocupação com alta disponibilidade, suporte técnico especializado, garantias contratuais e custo total de propriedade. | Reforça a arquitetura híbrida MPLS/SD-WAN adotada no TRT10, a contingência cruzada entre camadas, a necessidade de suporte 24x7, substituição de componentes e definição de SLA objetivo para indisponibilidade e degradação. |
| Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026 | Serviço de telecomunicação com transporte de dados em tecnologia MPLS via fibra óptica, links de Internet dedicada e links temporários móveis. | Uso de fibra óptica, rede privada MPLS, links dedicados de Internet, hardware em comodato, substituição obrigatória de hardware em caso de falha, disponibilidade mínima, MTTR definido para backbone/circuitos MPLS, monitoramento gráfico e segmentação lógica. | Reforça a exigência de fibra óptica como meio preferencial, equipamentos fornecidos como parte do serviço, substituição de hardware, monitoramento, disponibilidade mínima, prazo de reparo e segmentação lógica da rede. |
| Município de Cascavel/PR | Edital nº 90129/2025; Processo nº 115968; Pregão eletrônico; PNCP nº 76208867000107-1-000429/2025 | Rede IP/MPLS e serviços correlatos de comunicação de dados, com itens de capacidade próximos aos do TRT10. | Contratação por faixas de capacidade, com rede IP/MPLS e estruturação por itens de enlace, permitindo comparação de mercado para capacidades intermediárias. | Foi usada como referência parcial de faixa para 100 Mbps e 500 Mbps, sem tratar os valores como equivalência perfeita quando a capacidade não coincidia exatamente. Contribui para a metodologia de normalização e análise crítica de preços. |
| SENAR/MS - Serviço Nacional de Aprendizagem Rural de Mato Grosso do Sul | Pregão Eletrônico nº 009/2026; Processo nº 018/2026; PNCP nº 04253881000103-1-000025/2026 | Item de link dedicado MPLS de 1 Gbps. | Contratação com item específico de capacidade de 1 Gbps para MPLS, com valor unitário mensal identificável. | Foi usada como referência exata de preço para a capacidade de 1 Gbps, compondo a mediana da estimativa financeira do ETP. |
| Município de Brusque/SC | Pregão Eletrônico nº 11/2026; Processo nº 33/2026; PNCP nº 83102343000194-1-000064/2026 | Serviço de acesso privado entre Prefeitura e datacenter por link MPLS de ao menos 1 Gbps, além de contratação TIC crítica em IaaS nos artefatos correlatos baixados. | Link MPLS de alta capacidade para acesso privado; em artefatos TIC correlatos, adoção de SLA, suporte, garantia, manutenção preventiva/corretiva, disponibilidade e responsabilização integrada da contratada. | Foi usada como referência exata de preço para 1 Gbps no componente de estimativa e como referência auxiliar para demonstrar práticas de SLA, suporte, garantia e manutenção em serviços TIC críticos. |
| Município de Candeias/BA | Edital nº 023/2026; PNCP nº 13830336000123-1-000051/2026 | Comunicação de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra óptica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos. | Uso de LAN-to-LAN, fibra dedicada, concentração de alta capacidade, redundância de rotas e equipamentos incluídos como parte da solução. | Referência técnica para o grupo de link dedicado Sede-Foro, demonstrando que interligações privativas de alta capacidade por fibra são prática de mercado para comunicação entre pontos centrais. |
| Município de Ubarana/SP | Edital nº 19/2026; PNCP nº 65708786000141-1-000038/2026 | Prestação de serviço continuado de interligação de dados entre setores da Administração Pública Municipal; rede LAN-to-LAN por fibra óptica dedicada, capacidade agregada de até 10 Gbps, ponto concentrador e link dedicado. | Serviço de interligação de dados por item, com valor homologado no PNCP, fibra dedicada, rede LAN-to-LAN, capacidade agregada elevada e ponto concentrador. | Referência técnica auxiliar para o grupo de link dedicado Sede-Foro e para a lógica de concentração em pontos centrais, sem equivalência de capacidade com 25 Gbps. |
| Município de Água Clara/MS | Pregão Eletrônico; PNCP nº 03184066000177-1-000029/2025 | Serviços LAN-to-LAN de 1 Gbps para múltiplas unidades. | Contratação por pontos de LAN-to-LAN, com mensalidade por localidade e itens individualizados. | Referência técnica auxiliar para interligação privada por fibra entre unidades, sem equivalência de capacidade com 25 Gbps. |
| Município de Jaguariúna/SP | Edital PL-674/2024; PE nº 90081/2024; PNCP nº 46410866000171-1-000610/2024 | Link dedicado simétrico de 10 Gbps e link compartilhado de Internet. | Contratação de link dedicado de alta capacidade, simétrico, com requisitos de desempenho e disponibilidade. | Referência auxiliar para balizar tecnicamente a contratação de enlace dedicado de alta capacidade, sem confundir escopo de Internet com o link ponto-a-ponto Sede-Foro de 25 Gbps. |
| Tribunal de Justiça do Estado do Paraná - TJPR | Edital PE nº 15/2025; PNCP nº 77821841000194-1-000049/2025 | Dois links dedicados de 10 Gbps, BGP, Anti-DDoS e operadoras distintas. | Redundância por operadoras distintas, alta capacidade, roteamento BGP e proteção Anti-DDoS. | Referência auxiliar técnica para interoperabilidade com borda, roteamento controlado, alta disponibilidade, Anti-DDoS e diversidade de operadoras nos links de Internet centrais. |
| Justiça Federal do Rio Grande do Sul / TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços nº 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Serviços de comunicação de dados dedicados e exclusivos para acesso à Internet e comunicação ponto-a-ponto entre sites via Metro Ethernet/LAN-to-LAN, camada 2. | Uso de Metro Ethernet/LAN-to-LAN e comunicação ponto-a-ponto entre sites, com camada dedicada. | Referência técnica, sem valor unitário usado no cálculo, para a possibilidade de contratar o enlace Sede-Foro como link dedicado ponto-a-ponto, e não como MPLS. |

A análise dos processos similares não identificou inovação que torne inadequada a solução escolhida. Ao contrário, os precedentes confirmam a maturidade de mercado de redes MPLS, redes privadas gerenciadas, SD-WAN/MPLS, LAN-to-LAN, Metro Ethernet, links dedicados de alta capacidade, QoS, SLA, monitoramento, suporte 24x7, equipamentos fornecidos como parte do serviço e responsabilização da contratada pela disponibilidade da solução.

As principais metodologias e inovações absorvidas neste ETP são: contratação por circuitos/localidades e capacidade; equivalência de capacidade MPLS/SD-WAN para redundância total; integração MPLS com SD-WAN em contingência cruzada; tratamento do link Sede-Foro como enlace dedicado ponto-a-ponto de alta capacidade, e não como MPLS; exigência de monitoramento e relatórios mensais; SLA por circuito; definição de prazos de reparo; QoS por classe de tráfego; responsabilização da contratada por CPEs, roteadores, modems, transceptores e demais componentes fornecidos; e possibilidade de subcontratação apenas acessória, sem transferência de responsabilidade principal.

Com base nesse levantamento, a Solução 1 é a mais aderente à necessidade do TRT10: MPLS integrado à SD-WAN, capacidades MPLS equivalentes às capacidades SD-WAN por localidade, link dedicado ponto-a-ponto de 25 Gbps entre Sede e Foro de Brasília para replicação e redundância, e links dedicados de Internet centralizados na Sede e no Foro com Anti-DDoS, 32 IPs fixos e provedores distintos por localidade.

### 3 - Quais são os prós e contras das alternativas identificadas?

A comparação técnica entre as alternativas consta da tabela e da análise acima. Em síntese, a Solução 1 - MPLS integrado à SD-WAN com capacidade equivalente - apresenta melhor equilíbrio entre segurança, disponibilidade, QoS, isolamento lógico, roteamento controlado, integração com a infraestrutura vigente e redundância total. Links satelitais são úteis como contingência específica, mas possuem maior latência e variabilidade. Links comuns de Internet com VPN possuem menor custo aparente, mas ampliam dependência de rede pública e dificultam QoS fim a fim.

## VI - ESTIMATIVA DO VALOR DA CONTRATAÇÃO

### 1 - Foi feita pesquisa de preços e definição do valor estimado da contratação conforme planilha padronizada neste Regional?

Sim. Foi feita estimativa de planejamento com base em preços públicos e referências PNCP documentadas, organizada por grupo de serviço, capacidade, quantidade, valor mensal e valor anual. A memória abaixo contém os elementos necessários para alimentação da planilha padronizada do Regional, mantendo rastreabilidade de órgãos, pregões, processos, números de controle PNCP, artefatos baixados e fórmulas.

### 1.1 - A estimativa do valor da contratação está acompanhada dos preços unitários referenciais, das memórias de cálculo e dos documentos que lhe dão suporte?

Sim. A estimativa está acompanhada dos preços unitários referenciais, memória de cálculo e documentos de suporte baixados para `PNCP_REFERENCIAS_MPLS` e `PNCP_REFERENCIAS_INTERNET`.

| Grupo / item | Referências e fórmula | Quantidade | Valor mensal unitário | Valor mensal | Valor anual |
|---|---|---:|---:|---:|---:|
| MPLS 1 Gbps | Mediana PNCP: SENAR/MS R$ 6.950,00; Brusque/SC R$ 7.295,00; Chapecó/SC R$ 574,00; ANCINE R$ 8.211,77 | 2 | R$ 7.122,50 | R$ 14.245,00 | R$ 170.940,00 |
| MPLS 500 Mbps | Mediana PNCP: Chapecó/SC R$ 410,00; ANCINE R$ 5.875,42; Cascavel/PR R$ 1.900,00 | 3 | R$ 1.900,00 | R$ 5.700,00 | R$ 68.400,00 |
| MPLS 100 Mbps | Mediana PNCP: CODEVASF R$ 2.161,00; Cascavel/PR R$ 1.900,00; Chapecó/SC R$ 202,97 | 5 | R$ 1.900,00 | R$ 9.500,00 | R$ 114.000,00 |
| Link dedicado Sede-Foro 25 Gbps | Ponto médio da faixa paramétrica: (R$ 30.000,00 + R$ 60.000,00) / 2 | 1 | R$ 45.000,00 | R$ 45.000,00 | R$ 540.000,00 |
| Internet Sede 4 Gbps com Anti-DDoS e 32 IPs fixos | Ipojuca/PE 4 Gbps com Anti-DDoS R$ 15.687,33 + Chapecó/SC IP /27 R$ 1.920,00 | 3 | R$ 17.607,33 | R$ 52.821,99 | R$ 633.863,88 |
| Internet Foro 2 Gbps com Anti-DDoS e 32 IPs fixos | Mediana conservadora de referências normalizadas: IPEA R$ 5.520,00; composição Ministério da Defesa + /27 R$ 13.693,78; CLDF R$ 23.520,00 | 2 | R$ 13.693,78 | R$ 27.387,56 | R$ 328.650,72 |
| **Total estimado** | Soma de todos os grupos | 16 itens | - | **R$ 154.654,55** | **R$ 1.855.854,60** |

#### Fórmulas de cálculo adotadas

| Grupo | Fórmula |
|---|---|
| MPLS 1 Gbps | mediana das referências aderentes de 1 Gbps = mediana de R$ 6.950,00, R$ 7.295,00, R$ 574,00 e R$ 8.211,77 = R$ 7.122,50; quantidade 2; mensal = 2 x R$ 7.122,50 |
| MPLS 500 Mbps | mediana das referências aderentes/parciais de 500 Mbps = mediana de R$ 410,00, R$ 5.875,42 e R$ 1.900,00 = R$ 1.900,00; quantidade 3; mensal = 3 x R$ 1.900,00 |
| MPLS 100 Mbps | mediana das referências aderentes/parciais de 100 Mbps = mediana de R$ 2.161,00, R$ 1.900,00 e R$ 202,97 = R$ 1.900,00; quantidade 5; mensal = 5 x R$ 1.900,00 |
| Link dedicado Sede-Foro 25 Gbps | ponto médio da faixa técnica paramétrica = (R$ 30.000,00 + R$ 60.000,00) / 2 = R$ 45.000,00; quantidade 1; mensal = R$ 45.000,00 |
| Internet Sede 4 Gbps | referência direta de Ipojuca/PE para 4 Gbps com Anti-DDoS, R$ 15.687,33, acrescida do custo de bloco /27 identificado em Chapecó/SC, R$ 1.920,00; unitário = R$ 17.607,33; quantidade 3; mensal = 3 x R$ 17.607,33 |
| Internet Foro 2 Gbps | mediana conservadora de três referências normalizadas: IPEA R$ 5.520,00; composição Ministério da Defesa + /27 R$ 13.693,78; CLDF R$ 23.520,00; unitário = R$ 13.693,78; quantidade 2; mensal = 2 x R$ 13.693,78 |

#### Referências específicas para MPLS

| Órgão | Pregão/licitação, processo e PNCP | Objeto / item localizado | Valor de referência | Uso |
|---|---|---|---:|---|
| SENAR/MS - Serviço Nacional de Aprendizagem Rural de Mato Grosso do Sul | Pregão Eletrônico nº 009/2026; Processo nº 018/2026; PNCP nº 04253881000103-1-000025/2026 | Link dedicado MPLS de 1 Gbps | R$ 6.950,00/mês | Referência direta para MPLS 1 Gbps. |
| Município de Brusque/SC | Pregão Eletrônico nº 11/2026; Processo nº 33/2026; PNCP nº 83102343000194-1-000064/2026 | Link MPLS de, no mínimo, 1 Gbps para acesso privado entre Prefeitura e datacenter | R$ 7.295,00/mês | Referência direta para MPLS 1 Gbps. |
| Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026 | Serviço de transporte de dados em tecnologia MPLS por fibra óptica, com itens de 1 Gbps, 500 Mbps e 100 Mbps | R$ 574,00/mês para 1 Gbps; R$ 410,00/mês para 500 Mbps; R$ 202,97/mês para 100 Mbps, conforme itens coletados | Referência de mercado para faixas MPLS, tratada com cautela por diferença de escala e composição do certame. |
| ANCINE - Agência Nacional do Cinema | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025 | Solução com acesso à Internet e rede privada MPLS/SD-WAN | R$ 8.211,77/mês para item de referência de 1 Gbps; R$ 5.875,42/mês para item de referência de 500 Mbps | Referência parcial para estimativa e validação da arquitetura híbrida MPLS/SD-WAN. |
| Município de Cascavel/PR | Edital nº 90129/2025; Processo nº 115968; PNCP nº 76208867000107-1-000429/2025 | Rede IP/MPLS e serviços de comunicação de dados por faixas de capacidade | R$ 1.900,00/mês em item usado como referência de faixa | Referência parcial para 100 Mbps e 500 Mbps, usada na mediana. |
| CODEVASF - Companhia de Desenvolvimento dos Vales do São Francisco e do Parnaíba | Pregão Eletrônico nº 90003/2025; Processo nº 59500002693202462; PNCP nº 00399857000126-1-000049/2025 | Rede corporativa WAN IP/MPLS, com Administração Central e Superintendências Regionais | R$ 2.161,00/mês em item de referência de circuito | Referência parcial para 100 Mbps e validação de SLA, gerenciamento, suporte e CPE sob responsabilidade da contratada. |

#### Referências específicas para o link dedicado Sede-Foro de 25 Gbps

| Órgão | Pregão/licitação, processo e PNCP | Objeto / item localizado | Valor de referência | Uso |
|---|---|---|---:|---|
| Município de Candeias/BA | Edital nº 023/2026; PNCP nº 13830336000123-1-000051/2026 | Comunicação de dados privativa LAN-to-LAN, concentradores de 10 Gbps, fibra óptica, link dedicado de 4 Gbps full duplex, rotas redundantes e equipamentos inclusos | Referência técnica sem uso direto como preço unitário de 25 Gbps | Demonstra aderência de mercado para interligação privativa por fibra e concentração de alta capacidade. |
| Município de Ubarana/SP | Edital nº 19/2026; PNCP nº 65708786000141-1-000038/2026 | Rede LAN-to-LAN por fibra óptica dedicada, capacidade agregada de até 10 Gbps, ponto concentrador e link dedicado | Valor homologado identificado no PNCP: R$ 138.000,00 para item de interligação, conforme cache de pesquisa | Referência técnica auxiliar, sem equivalência direta com 25 Gbps. |
| Município de Água Clara/MS | Pregão Eletrônico; PNCP nº 03184066000177-1-000029/2025 | Serviços LAN-to-LAN de 1 Gbps para múltiplas unidades | Valores mensais inferiores, usados apenas como evidência de mercado para LAN-to-LAN | Referência técnica de contratação por ponto de interligação privada. |
| Município de Jaguariúna/SP | Edital PL-674/2024; Pregão Eletrônico nº 90081/2024; PNCP nº 46410866000171-1-000610/2024 | Link dedicado simétrico de 10 Gbps e link compartilhado de Internet | Referência auxiliar sem uso direto como preço unitário de 25 Gbps | Evidencia contratação pública de enlace dedicado simétrico de alta capacidade. |
| Justiça Federal do Rio Grande do Sul / TRF4 | Pregão Eletrônico nº 90012/2025; Ata de Registro de Preços nº 10/2025; PNCP relacionado a 00508903000188-1-002018/2025 | Comunicação de dados dedicada e exclusiva para Internet e ponto-a-ponto via Metro Ethernet/LAN-to-LAN, camada 2 | Referência técnica sem uso direto no cálculo | Valida a opção técnica de contratar o enlace Sede-Foro como link dedicado ponto-a-ponto, e não como MPLS. |

Não foram localizadas, nas consultas PNCP realizadas, três referências públicas plenamente equivalentes ao enlace ponto-a-ponto de 25 Gbps entre dois prédios centrais com a mesma finalidade de replicação e redundância. Por isso, o preço de planejamento desse item foi definido por faixa paramétrica conservadora, com registro explícito da limitação metodológica e separação das referências técnicas que demonstram viabilidade de mercado.

#### Referências específicas para links de Internet

| Órgão | Pregão/licitação, processo e PNCP | Objeto / item localizado | Valor de referência | Uso |
|---|---|---|---:|---|
| Município de Ipojuca/PE | Pregão Eletrônico nº 035/PMI-SMAD/2024; Processo nº 188/PMI-SMAD/2024; PNCP nº 11294386000108-1-000244/2024; https://pncp.gov.br/app/editais/11294386000108/2024/244 | Internet dedicada 4 Gbps, Anti-DDoS e faixa de IP fixo CIDR/29; links principal e redundante por empresas diferentes | R$ 15.687,33/mês por link | Base direta dos itens de 4 Gbps da Sede. |
| Município de Chapecó/SC | Pregão Eletrônico nº 153/2026; Processo nº 153/2026; PNCP nº 83021808000182-1-000200/2026; https://pncp.gov.br/app/editais/83021808000182/2026/200 | Memória de cálculo com IP /27 e links dedicados de Internet 5 Gbps | R$ 1.920,00/mês para IP /27; R$ 8.500,00 e R$ 7.500,00/mês para 5 Gbps | Ajuste de endereçamento e referência de alta capacidade. |
| Câmara Legislativa do Distrito Federal | Aviso de Contratação Direta nº 90021/2025; PNCP nº 26963645000113-1-000038/2025; https://pncp.gov.br/app/compras/26963645000113/2025/38 | Link de dados de 2 Gbps para acesso dedicado à Internet com Anti-DDoS | R$ 21.600,00 homologado; R$ 23.520,00 quando acrescido o ajuste /27 de Chapecó/SC | Referência direta homologada para 2 Gbps com Anti-DDoS. |
| Instituto de Pesquisa Econômica Aplicada - IPEA | Pregão Eletrônico nº 90047/2026; PNCP nº 33892175000100-1-000033/2026; https://pncp.gov.br/app/compras/33892175000100/2026/33 | Dois links dedicados de Internet, cada um com velocidade mínima de 2 Gbps simétrica e Anti-DDoS | R$ 3.600,00/mês por item estimado; R$ 5.520,00 quando acrescido o ajuste /27 de Chapecó/SC | Referência direta estimada para 2 Gbps com Anti-DDoS. |
| Ministério da Defesa | Dispensa com Disputa nº 292/2025; Processo nº 60591.000013/2025-64; PNCP nº 03277610000125-1-000586/2025; https://pncp.gov.br/app/editais/03277610000125/2025/586 | Link dedicado 1 Gbps e Anti-DDoS | R$ 5.161,89/mês para acesso; R$ 1.450,00/mês para Anti-DDoS | Composição dos itens de 2 Gbps do Foro. |
| Município de Itaipulândia/PR | Pregão Eletrônico nº 52/2025; Processo nº 98/2025; PNCP nº 95725057000164-1-000097/2025; https://pncp.gov.br/app/editais/95725057000164/2025/97 | Links dedicados simétricos de 2 Gbps por fibra óptica | R$ 450.000,00 valor global estimado | Referência técnica de disponibilidade de serviço 2 Gbps. |
| CAU/BA | Dispensa nº 5/2025; Processo nº 00152.000202/2025-84; PNCP nº 15158665000103-1-000011/2025; https://pncp.gov.br/app/editais/15158665000103/2025/11 | Relatório de cotação com referência de Internet dedicada 2 Gbps com Anti-DDoS | Referência auxiliar de cotação | Apoio de mercado, sem uso direto na fórmula. |
| ANCINE | Pregão Eletrônico nº 90007/2025; Processo nº 01416.005548/2024-11; PNCP nº 04884574000120-1-000056/2025; https://pncp.gov.br/app/editais/04884574000120/2025/56 | Link de Internet 1 Gbps com proteção Anti-DDoS | R$ 7.296,87/mês por link | Validação técnica de Anti-DDoS e SLA. |

### 1.2 - Apresente, também, a listagem dos fornecedores consultados, as justificativas de sua escolha e as empresas que, consultadas, não apresentaram resposta.

Não foi adotada pesquisa direta com fornecedores privados como fonte principal de preço. A pesquisa priorizou preços públicos e documentos oficiais obtidos no PNCP, por serem mais rastreáveis e aderentes ao art. 23, §1º, da Lei nº 14.133/2021 e à IN SEGES/ME nº 65/2021. Não há empresas privadas consultadas diretamente e sem resposta a registrar nesta fase.

### 1.3 - Foi feita uma análise crítica dos preços coletados?

Sim. Os preços foram avaliados quanto à aderência do objeto, capacidade, unidade de medida, prazo, localidade, inclusão de equipamentos, Anti-DDoS, bloco de IPs, suporte, SLA, ganho de escala e existência de valor unitário identificável. Para 4 Gbps, Ipojuca/PE foi tratado como referência direta e recebeu ajuste de endereçamento /27. Para 2 Gbps, a estimativa adotou mediana conservadora entre referência direta estimada do IPEA, referência direta homologada da Câmara Legislativa do Distrito Federal e composição paramétrica do Ministério da Defesa, todas ajustadas ou comparadas com o custo de IP /27 identificado em Chapecó/SC quando necessário.

### 2 - No caso de aquisição de bens e contratação de serviços em geral, a estimativa observa o art. 23, §1º, da Lei nº 14.133/2021 e a IN SEGES/ME nº 65/2021?

Sim. A estimativa adota preços públicos, normalização mensal, identificação do órgão, pregão, processo, número PNCP, item, valor unitário, memória de cálculo e análise crítica. Referências sem aderência plena foram classificadas como auxiliares ou técnicas, sem uso direto como se fossem equivalentes perfeitas.

### 2.1 - A pesquisa priorizou os preços públicos?

Sim. A pesquisa priorizou preços públicos do PNCP e documentos oficiais anexos aos processos.

### 2.2 - Foi explicitada qual a metodologia utilizada?

Sim. A metodologia consistiu em: coletar contratações públicas similares no PNCP; baixar artefatos; identificar item, capacidade, valor e prazo; normalizar valores para mensalidade unitária; classificar referências como diretas, parciais, auxiliares ou técnicas; aplicar mediana nas faixas MPLS; aplicar mediana ou composição paramétrica justificada nos itens sem três referências plenamente idênticas; e calcular o valor mensal e anual por multiplicação da quantidade.

### 2.3 - Cada item contém ao menos 3 preços/propostas?

Parcialmente. As capacidades MPLS possuem pelo menos três referências por faixa. Os links de Internet de 4 Gbps possuem uma referência direta altamente aderente e referências complementares para IP /27, Anti-DDoS e alta capacidade. Os links de Internet de 2 Gbps possuem referências públicas diretas e auxiliares suficientes para mediana conservadora, embora nem todas contenham simultaneamente 32 IPs fixos no mesmo item. O link dedicado Sede-Foro de 25 Gbps usa faixa paramétrica, pois não foram localizados três itens públicos idênticos com a mesma capacidade e finalidade.

### 3 - No caso de obras e serviços de engenharia, a estimativa observa o art. 23, §2º, da Lei nº 14.133/2021, a IN SEGES/ME nº 91/2022 e o Decreto nº 7.983/2013?

Não se aplica. O objeto é serviço continuado de telecomunicações e comunicação de dados.

### 3.1 - Foi utilizada a tabela SINAPI?

Não. A tabela SINAPI não foi utilizada porque o objeto não é obra nem serviço de engenharia.

### 3.2 - Foi justificada a escolha entre a tabela Onerada ou Desonerada?

Não se aplica.

### 3.3 - Foi elaborado o Cronograma Físico-Financeiro?

Não se aplica cronograma físico-financeiro típico de obra. A contratação terá cronograma de implantação operacional por fases, com medição mensal por circuito ou enlace ativado e aceito.

## VII - DESCRIÇÃO DA SOLUÇÃO COMO UM TODO

### 1 - Qual é a solução apta a atender à necessidade, considerando todo o ciclo de vida do objeto?

A solução contrata conectividade privada MPLS para as 10 localidades, link dedicado Sede-Foro de 25 Gbps e links dedicados de Internet centralizados na Sede e no Foro, mantendo integração operacional com a SD-WAN vigente. A Sede será o concentrador principal; o Foro de Brasília será ponto de replicação, redundância e egressão de Internet em contingência.

A solução deve contratar 3 links de Internet dedicada de 4 Gbps na Sede e 2 links de Internet dedicada de 2 Gbps no Foro de Brasília. Cada link deve possuir Anti-DDoS, 32 IPs fixos e provedor distinto dos demais links da mesma localidade. Esses enlaces compõem a borda central de Internet do Tribunal.

### Lógica arquitetural da Solução 1

1. O MPLS fornece caminho privado e controlado para tráfego crítico entre unidades e Sede.
1. A SD-WAN vigente permanece integrada como camada de transporte, contingência e convivência operacional.
1. A Sede é o ponto principal de segurança, filtragem, observabilidade, integração institucional e egressão à Internet.
1. O Foro de Brasília é ponto redundante de egressão à Internet e pode assumir acesso das unidades em contingência.
1. O link dedicado Sede-Foro de 25 Gbps viabiliza replicação, sincronização, backup e redirecionamento de tráfego entre os pontos centrais.
1. A Internet centralizada reduz dispersão de saídas, melhora padronização de segurança e concentra Anti-DDoS em enlaces críticos.
1. A vedação de dois links de Internet do mesmo provedor na mesma localidade reduz risco de falha comum.

### Topologia proposta

![Figura 1 - Arquitetura proposta MPLS, SD-WAN, link dedicado Sede-Foro e Internet centralizada](../diagrama_topologia_revisada.png)

### Dimensionamento definido

| Item | Localidade / enlace | Tecnologia | Capacidade | Papel |
|---|---|---|---:|---|
| 1 | Edifício Sede | MPLS | 1 Gbps | Concentrador preferencial |
| 2 | Foro de Brasília | MPLS | 1 Gbps | Unidade de maior demanda e ponto redundante |
| 3 | Prédio de Apoio | MPLS | 500 Mbps | Unidade metropolitana |
| 4 | Foro de Taguatinga | MPLS | 500 Mbps | Unidade regional DF |
| 5 | Foro de Palmas | MPLS | 500 Mbps | Polo TO |
| 6 a 10 | Gama, Araguaína, Gurupi, Dianópolis e Guaraí | MPLS | 100 Mbps cada | Unidades remotas |
| 11 | Sede ↔ Foro de Brasília | Link dedicado ponto-a-ponto | 25 Gbps | Replicação, redundância da Sede e acesso contingencial |
| 12 a 14 | Sede | Internet dedicada | 3 x 4 Gbps | Egressão principal; Anti-DDoS; 32 IPs fixos por link; provedores distintos |
| 15 a 16 | Foro de Brasília | Internet dedicada | 2 x 2 Gbps | Egressão redundante; Anti-DDoS; 32 IPs fixos por link; provedores distintos |

### Premissas de capacidade dos pontos centrais

A Sede possuirá capacidade agregada de Internet de 12 Gbps, distribuída em 3 links de 4 Gbps, com provedores distintos, Anti-DDoS e 32 IPs fixos por link. O Foro possuirá capacidade agregada de Internet de 4 Gbps, distribuída em 2 links de 2 Gbps, com provedores distintos, Anti-DDoS e 32 IPs fixos por link.

O enlace dedicado Sede-Foro de 25 Gbps fica dimensionado para cargas de replicação e contingência, não apenas para tráfego ordinário de usuários. A banda elevada se justifica pela necessidade de transferências volumosas entre ambientes, sincronização de dados, restauração, espelhamento, backup, testes de continuidade e redirecionamento de acesso das unidades ao Foro.

### Diretrizes de operação e governança

- Centralizar políticas de Internet na Sede e no Foro, com tráfego local de Internet nas unidades apenas como exceção formalmente autorizada.
- Implementar Anti-DDoS por link, com detecção, mitigação, relatórios, acionamento 24x7 e reinjeção do tráfego limpo quando aplicável.
- Manter provedores distintos por localidade e documentar rotas físicas, ASN, contatos de NOC e processos de escalonamento.
- Implementar QoS fim a fim para sistemas críticos, voz/vídeo, autenticação, monitoramento e replicação.
- Configurar failover entre Sede e Foro, entre links de Internet e entre MPLS/SD-WAN para fluxos definidos.
- Exigir documentação as built, incluindo endereçamento /27, rotas, NAT, políticas, equipamentos, circuitos e contatos de suporte.
- Implantar painéis de monitoramento com disponibilidade, capacidade, erros, latência, perda, jitter, eventos de Anti-DDoS e eventos de failover.

### 2 - Quais são as justificativas técnicas e econômicas para a escolha?

A solução é tecnicamente justificável porque combina rede privada MPLS, SD-WAN vigente, link dedicado de 25 Gbps entre os pontos centrais e Internet centralizada com Anti-DDoS, provedores distintos e endereçamento fixo suficiente. Economicamente, a escolha reduz dispersão de contratos de Internet, concentra proteção e fiscalização, permite competição por itens de Internet e utiliza preços públicos PNCP como base de planejamento.

### 3 - A solução demandará manutenção e/ou assistência técnica?

Sim. Manutenção, assistência técnica, operação, monitoramento, suporte, substituição de equipamentos sob responsabilidade da contratada, relatórios mensais, Anti-DDoS, atendimento a chamados e cumprimento de SLA integram o objeto e deverão estar incluídos nos preços mensais.

### 4 - No caso de compras, é necessário analisar amostras?

Não. O objeto é serviço continuado de telecomunicações e comunicação de dados.

### 5 - No caso de serviços, é necessária vistoria prévia?

A vistoria prévia será facultativa. A licitante poderá substituí-la por declaração de conhecimento das condições locais e responsabilidade pela proposta.

### 6 - É necessária autorização do poder público para exercício da atividade a ser contratada?

Sim. A contratada deve comprovar autorização, outorga, licença ou regularidade regulatória aplicável à prestação de serviços de telecomunicações/comunicação de dados, em especial SCM ou enquadramento equivalente perante a Anatel.

### 7 - Será necessário exigir qualificações econômico-financeiras adicionais?

Sim. Exigem-se qualificações econômico-financeiras ordinárias previstas na legislação e no edital, compatíveis com serviço continuado essencial.

### 8 - Será necessário exigir qualificações técnicas técnico-operacionais e técnico-profissionais específicas?

Sim. Exige-se qualificação técnico-operacional compatível com rede corporativa, MPLS/L3VPN/LAN-to-LAN/rede privada gerenciada, link dedicado de alta capacidade, Internet dedicada, Anti-DDoS, múltiplas localidades, operação, monitoramento, suporte, SLA, CPEs/roteadores, implantação, configuração, manutenção e documentação.

## VIII - JUSTIFICATIVAS PARA O PARCELAMENTO OU NÃO PARCELAMENTO

### 1 - No caso de parcelamento do objeto por item, justifique.

Haverá parcelamento por item para os links de Internet. Os itens 12, 13 e 14 correspondem aos 3 links de 4 Gbps da Sede; os itens 15 e 16 correspondem aos 2 links de 2 Gbps do Foro de Brasília. Esse parcelamento é obrigatório para preservar a redundância real, pois permite impedir que a mesma empresa vença mais de um link de Internet na mesma localidade.

Fica definida a seguinte regra: uma mesma empresa, CNPJ, grupo econômico ou provedor operacionalmente dependente não poderá ser adjudicatário de mais de um link de Internet na mesma localidade. Caso a mesma licitante apresente a melhor proposta em mais de um item de Internet da mesma localidade, será adjudicado apenas um desses itens à licitante, observada a ordem de vantajosidade definida no edital, convocando-se a próxima classificada aceitável para os demais itens da mesma localidade. A mesma empresa poderá vencer um link da Sede e um link do Foro, pois a restrição se aplica por localidade.

### 2 - No caso de parcial parcelamento do objeto por grupo de itens, justifique.

A contratação terá parcelamento parcial. Os circuitos MPLS poderão ser estruturados em grupo de solução por dependerem de roteamento integrado, QoS, monitoramento centralizado, SLA de ponta a ponta e responsabilização técnica única. O link dedicado Sede-Foro de 25 Gbps deverá compor item ou grupo próprio por possuir tecnologia, finalidade, escala e preço distintos da malha MPLS. Os links de Internet devem ser itens separados para assegurar competição e independência de provedores.

### 3 - No caso de não parcelamento global, justifique.

Não se adota adjudicação global única para todo o objeto. A adjudicação global única contrariaria o requisito de provedores distintos nos links de Internet da mesma localidade e poderia concentrar risco operacional em um único fornecedor. O desenho adequado é híbrido: grupo técnico para a malha MPLS quando necessário, item ou grupo próprio para o link dedicado Sede-Foro, e itens individualizados para os links de Internet.

## IX - DEMONSTRATIVO DOS RESULTADOS PRETENDIDOS

### 1 - O que se almeja alcançar com a contratação?

- mais disponibilidade da comunicação institucional;

- redução de risco de indisponibilidade total das unidades;

- centralização de segurança e saída de Internet na Sede;

- tráfego crítico com mais previsibilidade;

- separação operacional entre tráfego crítico e tráfego de Internet, com contingência cruzada entre MPLS e SD-WAN;

- simplificação de políticas de roteamento e QoS;

- fortalecimento da governança e do monitoramento da infraestrutura de rede;

- padronização mais consistente de políticas de segurança, inspeção de tráfego, registros e controle de acesso;

- mais previsibilidade para acesso a redes JT, Infovia, serviços institucionais e rotinas de continuidade;

- possibilidade de revisão periódica de capacidade com base em indicadores reais de consumo e desempenho;

- continuidade dos serviços judiciais e administrativos.

### 2 - No caso de contratação de serviços, quais são os níveis esperados de qualidade da prestação e as respectivas adequações de pagamento para o Instrumento de Medição de Resultados (IMR)?

Os níveis esperados de qualidade ficam definidos pelos SLA de disponibilidade, atendimento, reparo, manutenção programada, desempenho mínimo, documentação, relatórios e aceite descritos neste ETP. O IMR deverá aplicar glosas por circuito, conforme faixas já definidas: 5% da mensalidade quando a disponibilidade ficar abaixo da meta e até 0,5 ponto percentual abaixo dela; 10% quando a queda exceder 0,5 ponto e for até 1 ponto percentual; 20% quando a queda exceder 1 ponto percentual; e 30% quando houver indisponibilidade superior a 24 horas acumuladas no mês, sem afastar sanções. Também serão aferidos início de atendimento, prazo de reparo, perda, jitter, latência, throughput do link dedicado de 25 Gbps, entrega de relatórios e documentação as built.

## X - PROVIDÊNCIAS A SEREM ADOTADAS PELA ADMINISTRAÇÃO

### 1 - Quais providências devem ser adotadas pela Administração previamente à celebração do contrato?

- Validar inventário de circuitos, endereços, salas técnicas, racks, energia, climatização e entradas de fibra.
- Medir uso real da SD-WAN por localidade e dos acessos de Internet atuais.
- Consolidar plano de implantação para que os links de Internet da Sede e do Foro operem como pontos centrais de egressão do Tribunal.
- Definir endereçamento público dos blocos de 32 IPs fixos por link, NAT, publicação de serviços, regras de firewall, DNS, BGP quando aplicável e políticas de roteamento.
- Consolidar políticas de Anti-DDoS, acionamento, mitigação, relatórios, limiares, contatos de NOC e testes de aceite.
- Consolidar políticas de failover entre links de Internet da mesma localidade, entre Sede e Foro, e entre MPLS/SD-WAN.
- Definir ordem de implantação: Sede, Foro, link dedicado Sede-Foro, links de Internet centrais, unidades de maior criticidade, demais unidades, testes integrados e operação assistida.
- Conferir interdependências contratuais e técnicas para preservar continuidade operacional durante a implantação.
- Preparar mapa de riscos, matriz de responsabilidades, fiscais técnico e administrativo, gestor do contrato e rotina de medição mensal.

### 1.1 - Será necessária a adequação prévia do ambiente da organização para que a contratação surta efeito?

Sim, pontualmente e com controle. A Administração deverá validar espaço em rack, energia, climatização, passagem de cabos, entrada de fibra, endereçamento, políticas de firewall, rotas, VLANs/VRFs, acesso físico às salas técnicas e integração com monitoramento.

### 1.2 - Será necessária capacitação específica ou diferenciada para servidores responsáveis pela fiscalização e gestão?

Sim. A contratada deve realizar transferência de conhecimento para gestores e fiscais técnicos, abrangendo topologia, circuitos, rotas, QoS, Anti-DDoS, abertura e acompanhamento de chamados, interpretação de relatórios de SLA, testes de contingência, documentação as built, critérios de aceite, glosas e procedimentos de escalonamento.

## XI - CONTRATAÇÕES CORRELATAS E/OU INTERDEPENDENTES

### 1 - Há correlação ou interdependência com outras contratações?

Sim. Há interdependência com contrato SD-WAN vigente, Infovia, redes da Justiça do Trabalho, firewalls, segurança perimetral, DNS, autenticação, monitoramento, datacenter, energia, climatização e cabeamento. Essas interdependências dizem respeito à integração técnica da solução e à continuidade operacional durante a implantação.

Os links de Internet da Sede e do Foro compõem o objeto definido neste ETP. As interdependências técnicas concentram-se na infraestrutura de segurança, roteamento, monitoramento e serviços internos que utilizarão esses links.

### 1.1 - Há risco de sobreposição de contratações similares ou com o mesmo objeto?

O risco de sobreposição será controlado pela definição de que os links de Internet centralizados serão os únicos links de Internet do Tribunal na arquitetura pretendida. A Administração deverá mapear instrumentos vigentes que possam interagir com o objeto para evitar duplicidade de escopo durante a implantação e a operação assistida.

### 1.2 - É possível agrupar contratações correlatas em um só certame para ampliar economia de escala?

O agrupamento nesta contratação fica limitado aos componentes tecnicamente interdependentes da solução de comunicação de dados: MPLS, link dedicado Sede-Foro e links de Internet centralizados. Firewalls, SIEM, Infovia, SD-WAN vigente e monitoramento corporativo permanecem correlatos, mas não precisam ser incorporados ao mesmo certame por possuírem escopos e ciclos próprios.

### 1.3 - Se houver interdependência cronológica, qual cronograma ou ordem deve ser observado?

A ordem mínima será: validação de infraestrutura e inventário; emissão da ordem de serviço; entrega do plano de implantação; implantação da Sede e do Foro; ativação do link dedicado Sede-Foro; ativação dos links de Internet centrais; ativação dos circuitos MPLS; testes de aceite por localidade; testes de Anti-DDoS e failover; entrada em produção controlada; operação assistida; recebimento definitivo; e início da rotina mensal de medição e IMR.

## XII - DESCRIÇÃO DE POSSÍVEIS IMPACTOS AMBIENTAIS

### 1 - Descreva os possíveis impactos ambientais da contratação.

Impactos ambientais são baixos e restritos a equipamentos de rede, energia e eventuais adequações físicas. Mitigações: equipamentos eficientes, descarte adequado, reaproveitamento de infraestrutura existente, documentação digital e monitoramento remoto.

### 1.1 - Quais medidas mitigadoras serão usadas?

Serão adotadas eficiência energética dos equipamentos, reaproveitamento de infraestrutura existente, documentação digital, monitoramento remoto, redução de deslocamentos, descarte ambientalmente adequado de cabos, fontes, embalagens e componentes substituídos, além de logística reversa quando aplicável.

### 1.2 - As medidas incluem baixo consumo de energia e logística reversa?

Sim. Os equipamentos fornecidos como parte do serviço devem observar padrões compatíveis de eficiência energética e a contratada deverá destinar adequadamente resíduos, embalagens, cabos, fontes, CPEs e demais componentes substituídos, inclusive por logística reversa quando aplicável.

## XIII - POSICIONAMENTO CONCLUSIVO SOBRE A ADEQUAÇÃO DA CONTRATAÇÃO

### 1 - Explique se a contratação escolhida é adequada, viável e razoável para o atendimento da necessidade.

A contratação é tecnicamente viável, razoável e adequada. A solução integra MPLS para as 10 localidades, link dedicado Sede-Foro de 25 Gbps e links dedicados de Internet centralizados na Sede e no Foro, com Anti-DDoS, 32 IPs fixos por link e provedores distintos por localidade. A arquitetura fortalece continuidade, segurança, disponibilidade, governança, observabilidade e capacidade de resposta a incidentes.

A decisão final deste ETP é contratar: 10 circuitos MPLS com capacidades equivalentes à SD-WAN vigente; 1 link dedicado ponto-a-ponto de 25 Gbps entre Sede e Foro; 3 links de Internet dedicada de 4 Gbps na Sede; e 2 links de Internet dedicada de 2 Gbps no Foro. Os links de Internet serão itens separados para assegurar diversidade de provedores na mesma localidade. A estimativa de planejamento fica definida em **R$ 154.654,55 mensais** e **R$ 1.855.854,60 anuais**, sem prejuízo de atualização ordinária no momento da publicação caso haja decurso temporal relevante ou alteração formal de escopo.

## XIV - RESPONSÁVEL

**Unidade: CDTEC**

Servidor responsável: Edson Mateus de Sousa

E-mail: cdtec@trt10.jus.br

Telefone: (61) 3348-1249 / 1288 / 1280 / 1188
