# Modelo de valor do cliente: refino dos outcomes

Versão 1.0 — 19 de setembro de 2026. Deriva da Figura 2.4 de Ulwick (*What Customers Want*, exemplo da serra circular Bosch) aplicada ao estudo em `docs/estudo-jtbd-widget.html` e ao mapa em `docs/mapa-widget.md`.

## 1. O que a Figura 2.4 cobra do nosso modelo

Quatro exigências, e falhamos em três.

| O que a figura estabelece | Onde estamos |
|---|---|
| "In most cases **a dozen or so outcomes define success at each step**" | **2 por etapa.** 16 outcomes em 8 etapas. Uma etapa tem 3, três etapas têm 1. |
| Os três exemplos são todos de **uma única etapa** (Plan the cut), e todos no formato *Minimize the time it takes to [ação observável]* | Nossos outcomes misturam tempo, probabilidade e, em três casos, o próprio sucesso do job |
| As etapas têm **nomes do job**, não rótulos genéricos: Plan the cut, Adjust the saw, Start the cut, Operate the saw, Complete the cut, Maintain the saw | Usamos os rótulos genéricos do job map universal: Definir, Localizar, Preparar… |
| **"Ensure Safety" é uma etapa transversal**, desenhada fora da cadeia com uma seta apontando para o job inteiro | Tratamos segurança como job emocional (E1) pendurado em duas etapas |

O ponto crítico é o primeiro. Com dois outcomes por etapa, **não temos um modelo de valor — temos uma lista de temas.** "O6 minimizar a probabilidade de selecionar a instituição ou a conta errada" não é algo contra o que se projeta uma tela; é um assunto. A priorização por oportunidade aplicada a temas produz um ranking de assuntos, não uma fila de trabalho.

Ulwick trabalha com 50 a 150 outcomes para um job completo. Oito etapas a uma dúzia dá 96. Nosso alvo deve ficar nessa ordem de grandeza.

---

## 2. Auditoria de formato dos 16 outcomes atuais

Formato canônico: **[direção] + [unidade de medida] + [objeto de controle] + [clarificador contextual]**. Um outcome precisa ser algo que o próprio executor consegue medir.

| Outcome | Problema | Veredito |
|---|---|---|
| O7 "minimizar a probabilidade de **desconfiar** da legitimidade do pedido **e desistir**" | Composto (dois eventos), e "desistir" é a métrica de conversão. Repete o erro que a v0.1 já corrigiu em "maximizar a probabilidade de conectar com sucesso" — só que na escala da etapa. Além disso, o executor não mede a própria desconfiança. | **Reescrever** |
| O10 "minimizar o tempo para concluir a autorização" | É a duração da etapa inteira. Mede o resultado, não um passo do resultado. Não indica onde intervir. | **Reescrever como roll-up, não como outcome** |
| O1 "quais **dados ou operações** o sistema terá acesso" | Composto. Dados e operações são coisas distintas e com ansiedades distintas. | Dividir |
| O16 "saber que a conclusão depende de outra pessoa, **e de quem**" | Composto. | Dividir |
| O2, O4, O5, O6, O11, O12, O13, O14 | Formato válido, granularidade insuficiente | Decompor |

Nenhum outcome cita solução — isso a v0.1 já tinha acertado.

---

## 3. Refino conceitual: "Garantir a legitimidade" é etapa transversal, não emoção

Este é o ganho estrutural que a figura entrega.

Na Bosch, segurança não é atributo nem sentimento: é **uma etapa do job map com outcomes próprios**, que atravessa todas as outras. O desenho é literal — a caixa fica fora da cadeia, com uma seta apontando para o job inteiro.

O estudo hoje trata a legitimidade como job emocional E1, pendurado na etapa 4 (alta) e na etapa 5 (pico). **Que o mesmo item apareça em duas etapas com intensidades diferentes já é o sintoma: não é uma etapa, é algo que atravessa.** O empresário pergunta "isso é golpe?" na tela de boas-vindas, na lista de bancos, no formulário de credenciais, no aviso de pop-up e no redirecionamento. Cinco momentos, um único job.

### Proposta

| Antes | Depois |
|---|---|
| Etapa 4 "Confirmar" (verificar legitimidade e poderes) | **Dissolvida.** A verificação de poderes vai para a etapa 2; a de legitimidade vira transversal |
| Job emocional E1 | **Promovido a etapa transversal: "Garantir que não está sendo golpeado"**, com outcomes funcionais próprios |
| Job map de 8 etapas lineares | **7 etapas lineares + 1 transversal** |

Isso **não** contradiz o insight de "intervir nos picos, não em todas as telas". Bosch não põe proteção redundante em cada etapa da serra. Etapa transversal significa que a *necessidade* atravessa o job, não que a *solução* deva aparecer em toda tela. A distinção fica mais clara assim do que estava antes.

### O mapa renomeado na língua do executor

| # | Antes (genérico) | Depois (na língua do empresário) |
|---|---|---|
| 1 | Definir | Decidir o que liberar |
| 2 | Localizar | Reunir acesso e poderes |
| 3 | Preparar | Escolher por onde conectar |
| 4 | Confirmar | *(dissolvida)* |
| 5 | Executar | Autorizar no banco |
| 6 | Monitorar | Acompanhar a conclusão |
| 7 | Modificar | Corrigir e ajustar |
| 8 | Concluir | Voltar e usar |
| — | *(era E1)* | **Garantir que não está sendo golpeado** *(transversal)* |

---

## 4. Outcomes refinados: três conjuntos completos

Desenvolvi a dúzia completa nas três etapas onde o mapa do widget produziu evidência. As demais seguem pendentes — fazê-las sem evidência seria inventar.

**Legenda de procedência:** ▲ deriva de achado documentado no mapa do widget · ○ decomposição dos outcomes atuais · ◇ novo, hipótese a validar

### 4.1 Transversal — Garantir que não está sendo golpeado (`G`)

Substitui E1 e O7.

| # | Outcome | Proc. |
|---|---|---|
| G1 | Minimizar o tempo para confirmar que o pedido de acesso partiu do sistema de gestão que a empresa contratou | ○ |
| G2 | Minimizar o tempo para confirmar que o nome exibido na tela é o da empresa que enviou o convite | ▲ |
| G3 | Minimizar o tempo para verificar que o intermediário é autorizado a fazer o que está pedindo | ◇ |
| G4 | Minimizar a probabilidade de informar credenciais fora do ambiente do banco sem perceber que saiu dele | ▲ |
| G5 | **Minimizar o tempo para distinguir um aviso legítimo do sistema de um alerta de golpe** | ▲ |
| G6 | Minimizar o tempo para confirmar que a janela que se abriu pertence ao banco | ▲ |
| G7 | Minimizar a probabilidade de interpretar o redirecionamento legítimo como sequestro de sessão | ○ |
| G8 | Minimizar o tempo para confirmar que o acesso concedido pode ser retirado depois | ○ |
| G9 | Minimizar a probabilidade de precisar confiar num passo sem ter como verificá-lo | ◇ |
| G10 | Minimizar o tempo para saber a quem recorrer ao suspeitar de fraude durante o processo | ◇ |
| G11 | Minimizar o tempo para confirmar que nenhuma senha foi exposta a terceiros | ◇ |
| G12 | Minimizar a probabilidade de abandonar um pedido legítimo por não conseguir distingui-lo de um golpe | ○ |

G5 e G6 são a tradução exata do achado do aviso de pop-up bloqueado: uma mensagem que, em forma, é indistinguível de um alerta de fraude, entregue no pico. G12 é o que O7 tentava dizer sem a contaminação da métrica de conversão.

### 4.2 Etapa 2 — Reunir acesso e poderes (`R`)

Substitui O4 e O5.

| # | Outcome | Proc. |
|---|---|---|
| R1 | Minimizar o tempo para saber tudo o que será exigido antes de começar | ○ |
| R2 | Minimizar o tempo para descobrir se quem está diante da tela pode autorizar em nome da empresa | ○ |
| R3 | Minimizar a probabilidade de começar sem ter em mãos a credencial que será pedida | ○ |
| R4 | **Minimizar a probabilidade de começar sem o dispositivo previamente autorizado no banco** | ▲ |
| R5 | **Minimizar a probabilidade de começar sem o certificado digital que a instituição exige** | ▲ |
| R6 | Minimizar o tempo para providenciar, no banco, o acesso que falta | ▲ |
| R7 | Minimizar o tempo para saber a quem pedir, dentro da empresa, quando falta poder para autorizar | ◇ |
| R8 | **Minimizar a probabilidade de descobrir um pré-requisito depois de já ter começado** | ▲ |
| R9 | Minimizar o tempo para retomar de onde parou depois de providenciar o que faltava | ◇ |
| R10 | Minimizar a probabilidade de precisar de uma segunda pessoa sem saber disso de antemão | ▲ |
| R11 | Minimizar o tempo para estimar quanto o processo inteiro vai tomar | ◇ |
| R12 | Minimizar a probabilidade de começar num dispositivo que não permite concluir | ▲ |

R4, R5 e R8 vêm dos seis tutoriais PJ que ensinam a provisionar acesso antes de conectar. R12 vem dos problemas de webview e pop-up no celular.

### 4.3 Etapa 3 — Escolher por onde conectar (`P`)

Substitui O6.

| # | Outcome | Proc. |
|---|---|---|
| P1 | Minimizar o tempo para localizar a instituição da empresa na lista | ○ |
| P2 | **Minimizar o tempo para decidir entre duas entradas da mesma instituição** | ▲ |
| P3 | **Minimizar a probabilidade de escolher uma entrada que exige mais aprovadores do que a empresa consegue reunir** | ▲ |
| P4 | **Minimizar a probabilidade de escolher uma entrada que exige credencial que a empresa não possui** | ▲ |
| P5 | Minimizar a probabilidade de conectar uma empresa do grupo que não era a pretendida | ▲ |
| P6 | Minimizar o tempo para saber quais contas da empresa serão alcançadas pela escolha | ○ |
| P7 | Minimizar o tempo para saber se a instituição está operando normalmente agora | ▲ |
| P8 | Minimizar o tempo para saber o que muda nos dados conforme a entrada escolhida | ▲ |
| P9 | Minimizar a probabilidade de precisar refazer a escolha depois de iniciar | ○ |
| P10 | Minimizar o tempo para trocar de instituição sem recomeçar o processo | ◇ |
| P11 | Minimizar o tempo para confirmar que a escolha feita é a adequada ao caso da empresa | ◇ |
| P12 | Minimizar a probabilidade de escolher pela familiaridade da marca em vez da adequação ao caso | ◇ |

P2, P3 e P4 são o achado das quatro entradas do Itaú traduzido em medida. P12 é a armadilha específica: quatro entradas "Itaú" e o empresário escolhe a primeira.

**Cobertura após o refino:** 36 outcomes em 3 etapas (12, 12, 12) + 44 ainda por desenvolver nas 5 etapas restantes ≈ 80 no total. Ordem de grandeza compatível com ODI.

---

## 5. O desbloqueio prático: outcomes de tempo já têm proxy no funil

Os três exemplos da Bosch são todos de tempo, e não por acaso — tempo é observável. **Vários dos outcomes refinados já têm medida comportamental disponível hoje**, sem pesquisa com o empresário. Isso ataca de frente a restrição do B2B2B registrada no estudo ("o acesso ao empresário em escala é difícil").

| Outcome | Proxy comportamental | Disponível |
|---|---|---|
| P1 tempo para localizar a instituição | intervalo `SUBMITTED_CONSENT` → `SELECTED_INSTITUTION` | após inserir `SUBMITTED_CONSENT` no funil |
| P2 tempo para decidir entre entradas da mesma marca | mesmo intervalo, segmentado por marcas com entrada duplicada | idem |
| P9 / P10 refazer a escolha | `SELECTED_INSTITUTION` emitido mais de uma vez na sessão, com `connector` diferente | **hoje** — o evento carrega o objeto `connector` |
| P4 credencial que não se possui | `SELECTED_INSTITUTION` sem `SUBMITTED_LOGIN` subsequente, por conector | **hoje** |
| P3 aprovadores demais | itens de Open Finance PJ com warning 002 | após re-autenticar o dashboard |
| R8 pré-requisito descoberto tarde | abandono no formulário de credenciais concentrado em conectores de certificado (Inter Empresas, Efí) | **hoje** |
| G5 aviso confundido com golpe | tempo entre exibir o aviso de pop-up e o clique seguinte, e taxa de abandono nesse ponto | requer instrumentar o aviso |
| G12 abandono do pedido legítimo | abandono antes de `SUBMITTED_CONSENT` | após inserir o evento |

Ou seja: **a insatisfação de boa parte dos outcomes pode ser estimada por comportamento, e a importância é o que realmente exige pesquisa.** Isso inverte a ordem prática — mede-se satisfação primeiro, de graça, e gasta-se o acesso escasso ao empresário só com importância.

---

## 6. Refino dos experimentos

Cada hipótese passa a mirar outcomes nomeados, com métrica primária derivada do outcome — não da conversão global.

| Hip. | Outcomes-alvo | Métrica primária | Antes |
|---|---|---|---|
| **H7** desambiguar entradas duplicadas | P2, P3, P4, P8, P12 | tempo `SUBMITTED_CONSENT` → `SELECTED_INSTITUTION` em marcas duplicadas, e taxa de re-seleção | "O6" |
| **H3** checklist do que ter em mãos | R1, R3, R4, R5, R8, R10 | taxa de `SELECTED_INSTITUTION` sem `SUBMITTED_LOGIN`, por conector | "O4, O5" |
| **H9** aviso de pop-up | G5, G6 | tempo até o clique seguinte ao aviso; abandono nesse ponto | "O8, O9" |
| **H8** roteamento por poderes | R2, R7, R10, P3 | incidência de warning 002; taxa de conclusão em PJ multi-aprovador | "O5, O6" |
| **H1** preparar antes do redirect | G4, G6, G7, R12 | retorno do banco por dispositivo | "O7, O8, O9" |
| **H2** confirmação no retorno | O11, O12 *(pendente de refino)* | retentativas por CPF/CNPJ + instituição no mês | "O11, O12" |

Duas consequências de desenho:

1. **A métrica primária deixa de ser conversão.** Conversão vira métrica de resultado do conjunto; cada experimento responde pelo seu outcome. Isso torna possível declarar um experimento bem-sucedido no outcome e mal-sucedido na conversão — o que é informação, não fracasso.
2. **H7 ganha uma variante barata que não estava no radar.** Se P12 (escolher pela familiaridade da marca) for real, ordenar ou agrupar as entradas duplicadas já move o outcome, sem mudar texto nenhum — não passa pelo jurídico e não depende de customização por cliente.

---

## 7. O que muda nos objetivos do estudo

| Antes | Depois |
|---|---|
| "Rodar experimentos de UX no widget para aumentar a conversão" | Aumentar a conversão **atacando outcomes nomeados e medidos**, com a conversão como resultado, não como alvo de cada teste |
| Priorizar por oportunidade sobre 16 temas | Priorizar sobre ~80 outcomes, começando pelos 36 refinados |
| Importância e satisfação por pesquisa com o empresário | **Satisfação por proxy comportamental primeiro; pesquisa reservada à importância** |
| Segurança como job emocional E1 | Etapa transversal com 12 outcomes funcionais próprios |
| 8 etapas genéricas | 7 etapas na língua do executor + 1 transversal |

---

## 8. Pendências

1. Desenvolver a dúzia de outcomes nas cinco etapas restantes (Decidir o que liberar, Autorizar no banco, Acompanhar a conclusão, Corrigir e ajustar, Voltar e usar) — ~44 outcomes. Depende de evidência: entrevistas, tickets e a leitura tela a tela ainda pendente.
2. Validar a promoção de E1 a etapa transversal com produto e design antes de reescrever o documento vivo inteiro.
3. Decidir o destino de E2 a E5. A mesma pergunta se aplica: E5 (ansiedade de não saber se deu certo) é emoção ou é a etapa "Acompanhar a conclusão" mal especificada? Minha suspeita é a segunda, mas não desenvolvi.
4. Montar o questionário de importância sobre os 36 outcomes refinados — é o tamanho que cabe num instrumento único.
5. Confirmar os proxies da seção 5 no Amplitude antes de usá-los como satisfação.
