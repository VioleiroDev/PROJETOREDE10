# TERMO DE REFERENCIA

**Objeto:** Contratacao de servicos continuados de comunicacao de dados por MPLS para interconexao das unidades do TRT10 a Sede, em arquitetura integrada com a SD-WAN atual.  
**Natureza:** Servico comum continuado sem dedicacao exclusiva de mao de obra.  
**Regime sugerido:** Empreitada por preco unitario por circuito/localidade, com adjudicacao por grupo unico.  
**Criterio de julgamento sugerido:** Menor preco global do grupo, observadas as especificacoes tecnicas.  
**Versao:** Minuta tecnica preliminar  
**Data:** 21/05/2026

## Secao I - Do Objeto e Suas Especificacoes

### 1. Do objeto

Contratacao de empresa especializada para prestacao de servicos continuados de comunicacao de dados por rede MPLS, ou rede privada corporativa equivalente, incluindo fornecimento, instalacao, configuracao, ativacao, equipamentos, monitoramento, suporte tecnico e manutencao, para interconexao das unidades do TRT10 a Sede e integracao operacional com a SD-WAN vigente.

### 1.1 Itens, localidades e capacidades

| Item | Localidade | Endereco resumido | Capacidade minima MPLS | Disponibilidade minima sugerida |
|---:|---|---|---:|---:|
| 1 | Edificio Sede | SAS Qd. 1, Bloco D, Brasilia/DF | 1 Gbps | 99,90% |
| 2 | Foro de Brasilia | SEPN 513, Bloco B, Brasilia/DF | 1 Gbps | 99,70% |
| 3 | Predio de Apoio | SGAN 916 Norte, Brasilia/DF | 200 Mbps | 99,70% |
| 4 | Foro de Taguatinga | Quadra C12, Taguatinga/DF | 200 Mbps | 99,70% |
| 5 | Foro de Palmas | Quadra 302 Norte, Palmas/TO | 200 Mbps | 99,70% |
| 6 | Vara do Gama | Area Especial 01, Gama/DF | 50 Mbps | 99,70% |
| 7 | Foro de Araguaina | Av. Neief Murad, Araguaina/TO | 50 Mbps | 99,70% |
| 8 | Vara de Gurupi | Rua Antonio Lisboa da Cruz, Gurupi/TO | 50 Mbps | 99,70% |
| 9 | Vara de Dianopolis | Av. Wolney Filho, Dianopolis/TO | 50 Mbps | 99,70% |
| 10 | Vara de Guarai | Av. Araguaia, Guarai/TO | 50 Mbps | 99,70% |

### 2. Da natureza do objeto

Trata-se de servico comum continuado, pois os padroes de desempenho e qualidade podem ser objetivamente definidos por especificacoes usuais de mercado, inclusive capacidade, disponibilidade, latencia, perda de pacotes, prazo de reparo, monitoramento e suporte.

### 3. Da fundamentacao da contratacao

A fundamentacao consta do ETP, especialmente quanto a necessidade de interconexao privada das unidades a Sede, manutencao da SD-WAN atual como camada preferencial para Internet e contingencia, e utilizacao da infraestrutura de Internet/borda da Sede apenas como componente existente e correlato, fora do objeto desta contratacao.

### 4. Da descricao da solucao

A solucao contempla uma rede privada corporativa em topologia hub-and-spoke, com Sede como concentrador preferencial. Todas as demais localidades deverao se conectar a Sede por MPLS. O MPLS sera utilizado preferencialmente para trafego critico e institucional; a SD-WAN vigente sera utilizada preferencialmente para trafego de Internet. Em caso de indisponibilidade, degradacao relevante ou manutencao de qualquer uma das camadas, MPLS e SD-WAN deverao poder transportar os fluxos necessarios a continuidade dos servicos, conforme politicas de roteamento aprovadas pela CDTEC. A saida de Internet pela Sede, quando aplicavel, utilizara infraestrutura existente e fora do escopo desta contratacao.

![Figura 1 - Arquitetura proposta SD-WAN + MPLS](../diagrama_topologia_revisada.png)

## Secao II - Dos Requisitos da Contratacao

### 5. Requisitos tecnicos

5.1 A contratada devera prover rede MPLS L3 VPN ou tecnologia privada equivalente, desde que atenda, no minimo, aos requisitos de isolamento logico, QoS, roteamento controlado, SLA e monitoramento.

5.2 A rede devera interconectar todas as localidades a Sede, preservando a possibilidade de convivencia com a SD-WAN atual.

5.2.1 A contratada devera apoiar, no limite de sua responsabilidade tecnica sobre o servico contratado, a integracao do MPLS com a arquitetura SD-WAN vigente, firewalls, roteadores e demais componentes indicados pelo TRT10.

5.2.2 A arquitetura devera permitir politicas de preferencia de trafego, contemplando:

- MPLS como caminho preferencial para sistemas criticos, autenticacao, servicos corporativos internos, integracoes institucionais, administracao de rede e demais fluxos definidos pela CDTEC;
- SD-WAN como caminho preferencial para trafego de Internet;
- uso do MPLS para trafego de Internet em contingencia da SD-WAN, com egressao preferencial pela Sede;
- uso da SD-WAN para trafego critico em contingencia do MPLS;
- retorno controlado ao caminho preferencial apos normalizacao.

5.3 A contratada devera fornecer todos os equipamentos necessarios a prestacao do servico, incluindo CPE, modem, transceptores, cabos, fontes, acessorios e licencas.

5.4 Os circuitos deverao ser simetricos, full duplex, com banda livre para trafego util, ressalvados apenas overheads tecnicos inerentes ao protocolo.

5.5 A solucao devera suportar:

- roteamento estatico e dinamico, preferencialmente OSPF ou BGP;
- VRF ou segregacao logica equivalente;
- QoS com no minimo 4 classes de servico;
- priorizacao de trafego critico definido pelo TRT10;
- monitoramento de disponibilidade, latencia, perda de pacotes e utilizacao;
- relatorios mensais por localidade.

5.6 A contratada devera possibilitar integracao tecnica com firewalls, roteadores e controladores SD-WAN existentes, sem exigir troca de fabricante ou solucao proprietaria do TRT10.

### 6. Garantia do objeto

Durante toda a vigencia contratual, a contratada devera garantir funcionamento dos circuitos, equipamentos fornecidos, configuracoes sob sua responsabilidade e suporte tecnico.

### 7. Criterios de sustentabilidade e acessibilidade

Os equipamentos deverao observar eficiencia energetica compativel com o mercado, descarte ambientalmente adequado, documentacao digital e reducao de deslocamentos por meio de suporte remoto sempre que tecnicamente possivel.

## Secao III - Do Modelo de Execucao do Objeto

### 8. Modelo de execucao

8.1 O inicio da execucao ocorrera apos assinatura do contrato e emissao da ordem de servico.

8.2 A implantacao devera ocorrer por fases:

| Fase | Escopo | Resultado |
|---:|---|---|
| 1 | Sede | Ativacao do concentrador MPLS, roteamento e testes de conectividade |
| 2 | Foro de Brasilia, Predio de Apoio, Taguatinga e Palmas | Ativacao das unidades de maior capacidade |
| 3 | Gama, Araguaina, Gurupi, Dianopolis e Guarai | Ativacao das unidades remotas |
| 4 | Operacao assistida | Validacao de SLA, QoS, rotas, documentacao e aceite |

8.3 O prazo de instalacao sugerido e de ate 90 dias corridos para todas as localidades, podendo ser ajustado no TR final conforme pesquisa de mercado e criticidade.

8.4 A contratada devera apresentar plano de implantacao em ate 10 dias uteis apos a assinatura.

8.5 A ativacao de cada localidade dependera de teste de aceite, contemplando conectividade, banda, roteamento, disponibilidade do CPE, monitoramento e registro em documentacao.

8.6 A contratada devera entregar projeto executivo antes da ativacao, contendo, no minimo:

- desenho logico da rede MPLS;
- identificacao de circuitos e CPEs;
- enderecamento e interfaces sob sua responsabilidade;
- rotas, protocolos e vizinhancas previstas;
- classes de QoS, marcacoes e criterios de priorizacao;
- plano de testes;
- matriz de responsabilidade entre contratada, TRT10 e fornecedores correlatos;
- plano de rollback para mudancas com risco de indisponibilidade.

### 9. Locais e horarios de execucao

Os servicos serao executados nas localidades listadas no item 1.1, preferencialmente em horario comercial. Intervencoes com risco de indisponibilidade deverao ser agendadas com a CDTEC.

### 10. Obrigações da contratada

- prestar o servico conforme SLA;
- manter central de atendimento;
- disponibilizar portal de chamados em dominio publico ou canal equivalente;
- informar designacao de circuitos;
- manter monitoramento 24x7;
- comunicar incidentes criticos;
- apresentar relatorio mensal;
- manter sigilo sobre informacoes de rede;
- reparar falhas nos prazos definidos;
- manter documentacao atualizada;
- nao transferir responsabilidade tecnica pelo objeto.

### 11. Obrigações do contratante

- disponibilizar acesso as dependencias;
- indicar pontos de contato;
- aprovar janelas de manutencao;
- fornecer informacoes de enderecamento e roteamento necessarias;
- fiscalizar a execucao;
- efetuar pagamentos devidos apos aceite e verificacao.

## Secao IV - Modelo de Gestao Contratual

### 12. Fiscalizacao

A gestao e fiscalizacao serao exercidas por servidores designados formalmente. A fiscalizacao tecnica devera validar disponibilidade, relatorios, chamados, mudancas, testes e aceite.

### 13. Recebimento do objeto

13.1 O recebimento provisorio por localidade ocorrera apos comunicacao de ativacao e teste tecnico.

13.2 O recebimento definitivo ocorrera apos periodo de observacao e saneamento de pendencias.

### 14. Niveis minimos de servico

| Indicador | Meta sugerida | Forma de afericao |
|---|---:|---|
| Disponibilidade Sede | 99,90% mensal | Relatorio da contratada e validacao do TRT10 |
| Disponibilidade demais localidades | 99,70% mensal | Relatorio da contratada e validacao do TRT10 |
| Latencia mensal media entre unidade e Sede | A definir no projeto final por localidade/regiao | Medicoes automatizadas e relatorio mensal |
| Perda de pacotes mensal media | A definir no projeto final | Medicoes automatizadas e relatorio mensal |
| Jitter para classes sensiveis | A definir no projeto final, quando houver voz/video ou aplicacao sensivel | Medicoes automatizadas e relatorio mensal |
| Prazo para inicio de atendimento critico | ate 2 horas | Registro de chamado |
| Prazo de reparo critico | ate 8 horas, salvo justificativa aceita | Registro de chamado |
| Relatorio mensal | ate o 5o dia util do mes subsequente | Entrega documental |

14.1 A disponibilidade mensal sera calculada pela formula:

`D = [(To - Ti) / To] x 100`

onde `D` e disponibilidade, `To` e o periodo mensal em minutos e `Ti` e o tempo de indisponibilidade imputavel a contratada.

14.2 Falhas causadas por equipamentos, backbone, enlaces, CPEs ou configuracoes sob responsabilidade da contratada serao consideradas indisponibilidade.

14.3 Interrupcoes programadas somente poderao ser desconsideradas mediante autorizacao previa do TRT10.

### 15. Glosas

Em caso de descumprimento de disponibilidade, sugere-se glosa proporcional:

`Vd = V x [1 - (D / 100)]`

onde `Vd` e o desconto, `V` e o valor mensal do circuito afetado e `D` e a disponibilidade mensal apurada.

O TR final podera prever glosas adicionais por atraso de instalacao, atraso no atendimento e ausencia de relatorio.

### 15.1 Relatorio mensal minimo

O relatorio mensal devera conter, no minimo:

- disponibilidade por circuito;
- indisponibilidades programadas e nao programadas;
- chamados abertos, causa raiz, severidade, horario de abertura, inicio de atendimento e normalizacao;
- latencia, perda de pacotes, jitter quando aplicavel e utilizacao media e de pico;
- eventos de failover ou uso de contingencia entre MPLS e SD-WAN, quando identificaveis;
- manutencoes programadas;
- calculo de glosas ou justificativa de inexistencia de glosa.

## Secao V - Criterios de Selecao

### 16. Habilitacao juridica, fiscal, social e trabalhista

Aplicam-se os requisitos ordinarios da Lei no 14.133/2021 e do edital.

### 17. Qualificacao tecnica

17.1 A licitante devera comprovar aptidao para prestacao de servicos de comunicacao de dados corporativa, MPLS, rede privada gerenciada ou objeto equivalente.

17.2 Sugere-se exigir atestado que comprove prestacao de servico semelhante, com caracteristicas compativeis de rede privada, multiplas localidades, suporte tecnico e SLA.

17.2.1 O edital devera definir quantitativo minimo proporcional e justificavel para a qualificacao tecnica, evitando exigencias que restrinjam indevidamente a competitividade. Como hipotese de trabalho, recomenda-se exigir experiencia em rede corporativa gerenciada com multiplas localidades, monitoramento, suporte e SLA, em percentual ou numero de localidades a ser definido apos pesquisa de mercado.

17.3 A contratada devera possuir autorizacao, outorga ou instrumento regulatorio aplicavel para prestacao dos servicos de telecomunicacoes, quando exigivel pela regulamentacao setorial.

### 18. Vistoria previa

A vistoria previa podera ser facultativa, substituivel por declaracao de conhecimento das condicoes locais. A nao realizacao da vistoria nao devera embasar pedidos posteriores de acrescimo de custo.

## Secao VI - Vigencia, Pagamento e Reajuste

### 19. Vigencia

Sugere-se vigencia inicial de 5 anos, em coerencia com o historico do contrato SD-WAN e com a natureza continuada do servico, observada a legislacao vigente e justificativa de vantajosidade.

### 20. Pagamento

O pagamento sera mensal por circuito efetivamente ativado e aceito, condicionado a apresentacao de nota fiscal, relatorio de disponibilidade e ateste da fiscalizacao.

### 21. Reajuste

O reajuste devera observar indice setorial ou indice geral definido pela area competente no TR final, com periodicidade minima legal.

### 22. Garantia de execucao

A exigencia de garantia contratual devera ser avaliada na versao final com base no valor estimado, risco e orientacao juridica. Caso exigida, sugere-se percentual compativel com a Lei no 14.133/2021.

## Secao VII - Sancoes, Alteracao e Extincao

Aplicam-se as sancoes, hipoteses de alteracao e extincao previstas na Lei no 14.133/2021, edital e contrato, sem prejuizo das glosas especificas de nivel de servico.

## Secao VIII - Subcontratacao

A subcontratacao podera ser admitida apenas para atividades acessorias, tais como infraestrutura local, lancamento de fibra, adequacoes fisicas leves e atendimento de campo, desde que previamente autorizada quando exigido no contrato. A contratada principal permanecera integralmente responsavel pela execucao, suporte, seguranca, sigilo, SLA, documentacao e demais obrigacoes contratuais.

## Secao IX - Anexos do Termo de Referencia

Integram este Termo de Referencia, para fins de detalhamento tecnico, operacional, fiscalizatorio e de planejamento, os anexos constantes do Caderno de Anexos do TR:

| Anexo | Titulo | Finalidade |
|---|---|---|
| I | Arquitetura Tecnica da Solucao | Descrever a arquitetura MPLS integrada a SD-WAN, papeis das camadas, fluxos e principios de desenho |
| II | Localidades, Capacidades e Escopo dos Circuitos | Consolidar localidades, capacidades preliminares e escopo minimo por circuito |
| III | Requisitos Tecnicos Detalhados | Detalhar rede privada, isolamento, roteamento, QoS, seguranca e equipamentos |
| IV | Implantacao, Migracao e Rollback | Definir plano de implantacao, fases, janelas de mudanca e retorno |
| V | Plano de Testes e Aceite | Estabelecer testes minimos, aceite provisorio, aceite definitivo e classificacao de pendencias |
| VI | Niveis de Servico, Medicao e Glosas | Detalhar indicadores, formulas de disponibilidade e hipoteses de desconto |
| VII | Matriz de Riscos | Consolidar riscos, causas, probabilidade, impacto, mitigacao e responsaveis sugeridos |
| VIII | Modelo de Relatorio Mensal | Padronizar informacoes de desempenho, disponibilidade, incidentes e contingencia |
| IX | Modelo de Pesquisa de Precos e Comparacao de Alternativas | Apoiar a comparacao entre MPLS + SD-WAN, links satelitais e VPN sobre Internet |

As metas, parametros e responsabilidades descritos nos anexos que ainda dependam de pesquisa de mercado, validacao tecnica ou decisao administrativa deverao ser confirmados na versao final do edital e do contrato.
