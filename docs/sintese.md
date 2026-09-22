# Síntese: o que as quatro análises dizem juntas

Versão 2.0 — 22 de setembro de 2026. **Reconciliada contra a v1.0 do Estudo**, que trouxe medição de produção e derrubou parte do que a v1.0 desta síntese afirmava. Onde a v1.0 do Estudo mede e as outras abas deduzem, a medição vence.

As outras três abas — Mapa do widget, Banco de outcomes, Gates × jobs — foram escritas contra o funil antigo e a numeração antiga de outcomes. Continuam válidas no que é qualitativo: telas, credenciais por conector, famílias de erro, taxonomia de propriedade. **Todo número de funil que vier delas está superado.** O de/para da numeração está em `docs/de-para-outcomes.md`.

## 1. O baseline mudou, e a conclusão anterior sobrevive por razões melhores

A v1.0 desta síntese abria com "o 37,9% ainda não é um baseline". Estava certa na direção e errada no número: **o 37,9% não existe**. Foi construído com dois eventos que não medem o que parecem medir.

| O que o funil antigo usava | O que é |
|---|---|
| `Login Step Success` como passo de login | **Não mede login.** Dispara 22–25 vezes por item, de um `useEffect` que depende do item sob polling, sem trava. Mede frequência de polling. |
| `Item Polling Finished` como fechamento | **Viés de sobrevivência.** Falta em ~41% dos itens. Reportava 47,7% de conversão onde o Redshift dá 59,5% para a mesma população. |

O funil defensável é outro, e é menor em escopo: **dentro do widget, 58,0% em 7 dias**, com eventos que existem de verdade.

| Passo | Evento real | Usuários | Conversão |
|---|---|---|---|
| 1 | `Connect Widget Loaded` | 20.685 | — |
| 2 | `Button Clicked · location=welcomePage` | 18.418 | 89,0% |
| 3 | `List Item Clicked · location=connectorsList` | 14.440 | 78,4% |
| 4 | `Form Submitted · form=login` | 12.453 | 86,2% |
| 5 | `Item Created` | 11.989 | 96,3% |

O passo 2 é o ganho: **separa a tela de boas-vindas da lista de bancos**, que a síntese anterior pedia via `SUBMITTED_CONSENT` e que agora existe.

### O mapa de perdas substitui as zonas A e B

| | Perda | Etapas | Gates |
|---|---|---|---|
| **L1** carrega e não age na tela inicial | 11,0% | 1 | `entry.welcome` |
| **L2** age e não escolhe banco | **19,2%** | 1–3 | **sem gate hoje** |
| **L3** escolhe banco e não submete | 9,6% | 3–4 | `entry.credentials`, G1, G2, G3 |
| **L4** submete e não cria item | 2,2% | 4 | — |
| **L5** cria item e não chega a sucesso | **~23,5%** | 5–6 | G6, G7, G8, espera |

L5 é estimativa — mistura funil de usuários do Amplitude com taxa de item do Redshift. É a melhor aproximação disponível, não um número para publicar.

## 2. A convergência na etapa 2 não sobrevive ao dado

**Esta é a correção mais importante, e é contra uma conclusão minha.**

A síntese anterior tinha como achado central que três análises independentes convergiam na etapa 2 Localizar, e que era por ali que se deveria começar. A convergência era real, mas era entre análises **qualitativas** — documentação, tutoriais e telas de referência. Nenhuma das três tinha medição de onde a perda acontece.

O dado diz outra coisa:

| Onde as análises apontavam | Onde a perda está |
|---|---|
| Etapa 2 Localizar, por três caminhos independentes | Os gates da etapa 2 (G1, G2, G3) vivem em **L3 = 9,6%** — a terceira maior perda |
| — | As duas maiores são **L5 (~23,5%)**, depois do banco autorizar, e **L2 (19,2%)**, antes de um banco ser escolhido |

Duas correções de fato, além do tamanho:

- **Não são cinco gates na etapa 2, são três.** A aba Gates afirma "cinco dos oito gates atendem à etapa 2". Na numeração da v1.0, apenas G1, G2 e G3 estão ali — e **G2 e G3 são exclusivos do trilho direto**, então em Open Finance só G1 atende a etapa. G4 foi para a etapa 4 e G8 para a 5–6.
- **A premissa de que o pré-requisito é descoberto na etapa 2 é do software, não do usuário.** A própria v1.0 levanta isso como uma das cinco maneiras de o mapa estar errado: a evidência dos tutoriais sugere que a pessoa descobre o pré-requisito na etapa 5 e **volta**. O job map do ODI é sequência de necessidades, não de telas.

**O que sobrevive:** a etapa 2 continua subatendida, e a evidência dos seis tutoriais de provisionamento continua de pé — virou O8, com evidência marcada como *dado*. O que cai é a conclusão de que é por ali que se começa. Por tamanho de perda, não é.

## 3. A maior oportunidade isolada foi confirmada, quantificada — e tem nome proibido

A síntese anterior dizia que a escolha do trilho caía num vão entre modelos e era a maior oportunidade aparente. **O dado confirma e dá o número:** L2 é 19,2%, a segunda maior perda, e é a única faixa do fluxo **sem gate nenhum hoje**.

Mas a proposta de "gate zero" está morta como nome: **não se cria G0**, porque colidiria com a árvore de decisão de outro time. O gate existe, é proposto na v1.0 e se chama **`entry.rail`** — desambiguar a mesma marca nos dois trilhos pela consequência para o usuário, na etapa 3.

Um dado novo reforça: **32% das seleções vêm da busca**, o que sugere que a lista não é navegável por leitura.

E há um alerta que a síntese anterior não tinha: mover G1 para antes da lista, como H3 e H8 pedem, **adiciona atrito exatamente em L2**. É uma das cinco perguntas que a v1.0 devolve ao time.

## 4. Três classes de outcome — mantido

Nada no dado contradiz. A taxonomia de propriedade do modelo de gates continua a melhor ferramenta de triagem que o material produziu.

| Classe | O que a Pluggy pode fazer | Exemplos, já na numeração v1.0 |
|---|---|---|
| **Satisfazível** | mover o número | O6, O7, O10, O14, O24 |
| **Apenas esperável** | fazer com que não pareça erro | O18, O21 — a Caixa leva 30 min, e isso não muda |
| **Inegociável** | apenas divulgar | O2 — em Open Finance todas as contas da empresa naquele banco vão de uma vez |

A regra segue: para outcome apenas esperável, escreva sobre o *saber*, não sobre o *fato*. A v1.0 já nasce assim — O18 é "tempo para concluir", mas o par dela, O15, é "tempo para determinar o que vai acontecer na tela do banco".

E a v1.0 estende o caso de O2 de um jeito que faltava: **O5** — conceder acesso que não cobre o que a contabilidade exige. Dentro de um banco o escopo é tudo ou nada; entre bancos, a completude fica por conta do empresário, e nada no fluxo diz isso.

## 5. A divergência sobre E1 se resolveu por absorção

A síntese anterior levantava duas teses incompatíveis: a dos gates, em que a ansiedade de legitimidade é subproduto de expectativa não atendida, e a do estudo, em que E1 é job com peso próprio.

**A v1.0 mantém E1 como job e adota os gates** — e enuncia a tensão melhor do que eu: excesso de "confie, é seguro" espalhado por todas as telas é, em forma, indistinguível de golpe, e **isso é o maior risco do sistema de gates, que por definição adiciona telas explicativas**.

Ou seja: não são duas teses concorrentes, é uma restrição de desenho sobre a solução. A pergunta de entrevista continua valendo, mas deixa de ser bifurcação.

A v1.0 acrescenta **E6** (reversibilidade) e **E7** (não ficar sem saída), com um teste discriminante que o modelo anterior não tinha: dois jobs emocionais só são distintos se o abandono que provocam tiver **causa diferente e tratamento diferente**. E7 é o melhor exemplo — o `oauthRedirectUri` ausente produz um caso em que o status existe, a autorização funcionou, e a pessoa continua presa. Status não trata E7.

## 6. A instrumentação não é recomendação, é pré-requisito bloqueante

A síntese anterior recomendava instrumentar os gates antes de desenhar telas. A v1.0 mostra que é mais duro que isso: **o experimento não é legível com a instrumentação de hoje**, porque não existe denominador por tentativa nem taxa de passagem por gate.

Quatro fases são pré-requisito, e a primeira não é sobre analytics:

1. **Allowlist de propriedades.** O objeto de props do host é repassado sem filtro, e isso já colocou **CPF e CNPJ em ~138 mil eventos em 90 dias**. Acrescentar telemetria de gate antes de fechar isso amplia um problema de LGPD. Entrega sozinha, primeiro.
2. **Wrapper de telemetria**, sem nenhum call site falando direto com o SDK do fornecedor — é o que impede o erro já cometido duas vezes, de evento que nasce numa superfície e nunca chega às outras.
3. **`connection_id` no item e `Connection Reconciled` emitido pelo backend no webhook** — o único evento que sobrevive ao widget fechar, e portanto a única forma de medir L5, que é a maior perda. Critério de aceite: resolução da tentativa ÷ conectores selecionados ≥ 0,98.
4. **Gates e handoff instrumentados**, com `gate_surface`, os dois índices de gate e `help_id` como slug estável.

## 7. O experimento tem desenho, e não é "com gate × sem gate"

A síntese anterior propunha como métrica de guarda a transição de 85,9% do funil antigo. Substituída por um desenho inteiro:

| Elemento | Definição |
|---|---|
| Unidade de análise | `connect_attempt_id` — a tentativa, criada na escolha do conector. Não o usuário, não a sessão |
| Variantes | `gate_surface = page` × `accordion_item`, mesmo `gate_id` e mesmo texto |
| Métrica primária | o outcome que o gate mira, não a conversão |
| Métrica de sistema | resolução da tentativa — sucesso exige **todas** as conexões da tentativa concluídas |
| Guarda | tempo até a primeira ação · abandono antes da seleção · share de `PARTIAL_SUCCESS` · revogações precoces · tickets · conexões na conta errada · **cobertura de contas da empresa** |
| Tamanho | ~**9.700 tentativas por braço** para detectar 2 pontos — cerca de dez dias, antes de descontar perda de telemetria |

Comparar com e sem gate confundiria conteúdo com proeminência. Variando só a superfície, a única coisa que muda é quanta atenção a orientação exige.

**A guarda que a síntese anterior não tinha:** cobertura de contas. Um gate que acelera a conexão única e reduz o número de contas conectadas por empresa é vitória falsa — mais rápido até a primeira conexão, menos banco conectado no fim, e a apuração fica pior. A tentativa é a unidade do experimento, mas não é a unidade do job.

## 8. Plano sequenciado, revisado

### Fase 0 · Correções que entregam sozinhas

1. **Allowlist de propriedades** — LGPD, bloqueante, não depende de mais nada.
2. **Clientes sem `oauthRedirectUri`** — medir e corrigir com CS, documentação e aviso no Dashboard. Não é experimento.
3. **Documento pré-preenchido (CPF × CNPJ)** — ver seção 9. Maior razão evidência/esforço do material.

### Fase 1 · Tornar o experimento legível

4. Wrapper de telemetria; `Connection Reconciled`; gates instrumentados com `gate_surface`.
5. Segmentar o funil por configuração do SDK — `selectedConnectorId` e `updateItem` — **antes** de interpretar L1 e L2 como comportamento.
6. Declarar a cobertura de telemetria por cliente ao lado de todo número: **~36% dos usuários de alguns clientes emitem zero evento**, e o bloqueio é mais comum em desktop.

### Fase 2 · Medir quem é o executor

7. É a premissa mais cara de estar errada. Se a maioria das sessões PJ for de funcionário ou contador, E1 e E2 mudam de sentido e os jobs emocionais **sociais** — hoje fora do escopo — podem ser os dominantes.
8. Entrevistas para importância, com o banco de outcomes como material de apoio.

### Fase 3 · Experimentos

9. **H10** documento pré-preenchido — maior evidência.
10. **H9** aviso de pop-up — menor custo.
11. **H7** `entry.rail`, desambiguar marcas duplicadas — maior perda sem gate.
12. **H1** preparação antes do redirecionamento, como experimento de superfície.

## 9. O achado que nenhuma aba anterior tinha

**O documento pré-preenchido.** Num cliente medido, **~46% de todos os itens terminam em `USER_INPUT_TIMEOUT`** — e o padrão **inverte por segmento dentro do mesmo banco**: Santander PF 8% contra Santander Empresas 83%; Nubank PF 75% contra Nubank Empresas 17%.

Copy não inverteria dentro de um banco. A suspeita é mecânica: o widget escolhe CPF ou CNPJ pelo que o conector suporta, e prefixando o errado o usuário cai num formulário que não tem como preencher.

É o **O14**, marcado como *dado*, e a v1.0 o chama de maior razão evidência/esforço do mapa. Nenhuma das três abas anteriores o menciona, porque nenhuma tinha acesso a medição por conector e segmento.

## 10. O risco número um, que a aba Gates subestimou

A aba Gates registra a cobertura parcial como uma ressalva de amostra: 16 conectores revisados contra 66 instituições de Open Finance empresariais. A v1.0 trata o mesmo fato como **premissa central e risco número um**, e com razão:

> O modelo de gates foi desenhado contra 16 conectores revisados, **só cinco bancos têm variantes finalizadas**, e o widget principal exibe **mais de 170 instituições**.

A consequência não é margem de erro, é desenho: o conteúdo de gate precisa funcionar de forma genérica na lista inteira. Se não escalar, o sistema de gates no widget principal é necessariamente mais genérico — **e mais genérico pode ser menos eficaz do que a evidência dos cinco bancos sugere**. O experimento pode acabar medindo cinco bancos em vez do sistema.

É a primeira das cinco perguntas que a v1.0 devolve ao time: qual é o comportamento padrão para um banco não revisado — gate genérico, ou o gate simplesmente não dispara?

## 11. O que continua desconhecido

| Pergunta | Destrava | Custo |
|---|---|---|
| Quem está no widget em sessões PJ | **a camada emocional inteira** | consulta + entrevista |
| Comportamento de gate para banco não revisado | se o experimento mede o sistema ou cinco bancos | decisão de produto |
| Quanto de L1 e L2 é configuração e não comportamento | interpretabilidade das duas primeiras perdas | consulta |
| Confirmar a hipótese do documento pré-preenchido | H10, a correção de maior retorno | consulta |
| Fonte da verdade do readout — Redshift × Amplitude | quando o experimento pode ser lido | decisão de produto |
| `PARTIAL_SUCCESS` conta como sucesso? | se o experimento pode subir o número sem melhorar o resultado | decisão de produto |
| Importância por outcome | a priorização por oportunidade | entrevista |

## 12. O que cada aba ainda vale

| Aba | Vale | Não vale mais |
|---|---|---|
| **Mapa do widget** | telas por trilho, credenciais por conector direto PJ, 17 estados de erro em 8 famílias, três camadas de variação, múltipla alçada | seção 5 inteira, sobre eventos do funil; todo número das zonas A e B |
| **Banco de outcomes** | o formato de redação, a tabela de proxies comportamentais, as 36 formulações como roteiro de entrevista | a numeração antiga nas colunas "substitui"; o alvo de ~80 outcomes, hoje 30 |
| **Gates × jobs** | gates são solução e outcomes são critério; taxonomia de propriedade; crítica ao G1 | "cinco dos oito gates na etapa 2" — são três; o gate zero; as janelas de guarda do funil antigo |
