# Gates × jobs e outcomes

> **Reconciliado em 22 set 2026 contra a v1.0 do Estudo.** Três correções materiais: **são três gates na etapa 2, não cinco** (G1, G2, G3 — e G2 e G3 só existem no trilho direto); o **"gate zero" é proibido** e se chama `entry.rail`; e as janelas de guarda abaixo usam o funil antigo, substituído pelo mapa L1–L5. A cobertura parcial, registrada aqui como ressalva, é tratada pela v1.0 como **risco número um**. Numeração de outcomes: ver `docs/de-para-outcomes.md`.

Versão 1.1 — 22 de setembro de 2026. Cruza o modelo de gates (*A lógica dos gates · Guided Connect*, 8 gates sobre 16 conectores) com o job map e os outcomes do estudo.

## 1. Onde cada modelo vive

A primeira coisa a fixar, porque confundir isso desmonta os dois modelos:

| | Job map e outcomes | Modelo de gates |
|---|---|---|
| Responde | o que o empresário está tentando conseguir, e como ele julga se conseguiu | o que o produto diz e pergunta, e quando |
| Natureza | critério, estável | solução, substituível |
| Vem de | o executor | os fluxos dos conectores |
| Muda quando | o job muda (quase nunca) | um banco muda a tela, ou se acha um jeito melhor |

**Gates são solução; outcomes são o critério contra o qual a solução é julgada.** A v0.1 do estudo já tinha estabelecido que outcome não cita solução — é a mesma disciplina aqui, na direção inversa. Se o time passar a tratar os gates como o modelo, perde a pergunta "existe forma melhor de atender este outcome do que um gate?".

O acoplamento correto: **todo gate responde por pelo menos um outcome, e todo outcome que importa tem gate ou tem lacuna conhecida.**

## 2. A convergência: duas análises independentes, mesma etapa

O mapa do widget saiu da documentação. Os gates saíram das telas de referência dos conectores. Nenhum dos dois olhou para o outro. Mesmo assim:

**Corrigido na reconciliação.** O mapeamento abaixo é o da v1.0, com a numeração de outcomes nova e os gates fora da série G que este cruzamento não conhecia.

| Gate | O que faz | Etapa | Fluxo | Outcomes v1.0 |
|---|---|---|---|---|
| `entry.welcome` | termos, política e o que será acessado | 1 Definir | ambos | O1–O5 |
| **G1** perfil admin × operador | pergunta se a pessoa tem poderes | **2 Localizar** | ambos | **O7**, O6 |
| **G2** credenciais técnicas | avisa que é tarefa de TI | **2 Localizar** | **só direto** | **O6**, O8 |
| **G3** autorização de dispositivo | avisa que leva de 30 min a 24h | **2 Localizar** | **só direto** | O6, O8, O9 |
| `entry.rail` *(proposto)* | desambigua a mesma marca nos dois trilhos | 3 Preparar | ambos | **O10, O11, O12** |
| `entry.credentials` | CPF/CNPJ em OF; usuário e senha no direto | 4 Confirmar | ambos | **O14** |
| **G4** QR no app para obter token | pede o celular por perto | 4 Confirmar | ambos | O15, O16 |
| **G5** expiração rápida do token | manda abrir o app antes | 4–5 | ambos | O18, **O23** |
| **G6** consentimento no app | explica que termina no celular | 5 Executar | só OF | **O16, O17, O19** |
| **G7** tela de consentimento | o resumo de compartilhamento, no banco | 5 Executar | só OF | O2, O3 |
| **G8** múltiplos titulares | o segundo aprovador assina no app dele | 5–6 | só OF | **O7, O21, O22** |
| `bridge.waiting` *(proposto)* | a espera pelo retorno, hoje sem identidade | 6 Monitorar | ambos | O20, O21 |

**São três gates na etapa 2, não cinco** — e dois deles só existem no trilho direto, então em Open Finance apenas G1 atende a etapa. G4 foi para a etapa 4 e G8 para a 5–6. A afirmação original vinha de um mapeamento meu, não da especificação.

A convergência qualitativa continua real: o mapa do widget chegou à etapa 2 por outro caminho, com os seis tutoriais de provisionamento — hoje o outcome **O8**, marcado como *dado*. **Mas ela não sobrevive como prioridade.** Os gates da etapa 2 vivem em L3 = 9,6%, a terceira maior perda; as duas maiores são L5 (~23,5%) e L2 (19,2%). E a v1.0 levanta uma objeção de fundo: amarrar as oito etapas às telas reimporta a suposição de que a pessoa descobre o pré-requisito na etapa 2, quando a evidência dos tutoriais diz que ela descobre na 5 e volta. Ver aba Main, seção 2.

## 3. Os gates são a decomposição empírica de O6 e O7 *(antigos O4 e O5)*

Vale registrar, porque fecha uma discussão anterior. A v0.4 do estudo tentou decompor os outcomes deduzindo uma dúzia por etapa a partir de Ulwick, e a decisão foi não seguir por ali — a granularidade viria das entrevistas, não de dedução em cima de documentação.

**Os gates fazem exatamente essa decomposição, e por um caminho melhor.** "Minimizar a probabilidade de iniciar sem ter em mãos o que será exigido" (**O6** na v1.0) se decompõe, na prática dos fluxos, em: sem o celular por perto (G4), sem o dispositivo autorizado (G3), sem as credenciais técnicas (G2), sem tempo antes do código expirar (G5). Isso não é dedução — é observação de dezesseis conectores.

O banco de hipóteses da aba Modelo de valor continua útil como roteiro de entrevista. Mas **o que já pode virar backlog é o que os gates sustentam**, porque tem lastro em fluxo real.

## 4. A taxonomia de propriedade resolve um problema do estudo

O estudo registra, entre as premissas, que "o pico de ansiedade acontece em boa parte dentro do app do banco; as janelas de intervenção da Pluggy ficam antes e depois". Verdade, mas vago demais para orientar desenho. O modelo de gates operacionaliza isso em três classes:

| Classe | Significado | O que a Pluggy pode fazer |
|---|---|---|
| **Alavanca da Pluggy** | atrito que o widget consegue antecipar | verificar ou perguntar antes da tela do banco |
| **Do banco** | atrito que a instituição controla | só criar expectativa, para não parecer erro |
| **Compartilhado** | responsabilidade dividida | explicar antes, para a tela do banco não surpreender |

Isso tem uma consequência forte para o modelo de outcomes, e é o melhor ganho conceitual deste cruzamento:

> **Há outcomes que a Pluggy pode satisfazer e outcomes que ela só pode tornar esperados.**

Para atrito do banco, escrever "minimizar o tempo da autorização de dispositivo" é escrever um outcome que a Pluggy não pode mover — a Caixa leva o que leva. O outcome atendível é outro: **minimizar o tempo para saber que a espera é normal e quanto ela dura**. Não é firula de redação: muda qual métrica o experimento persegue e evita prometer o que não se entrega.

Proposta de reescrita, para os casos afetados:

| Outcome atual | Classe | Reescrita proposta |
|---|---|---|
| **O18** *(antigo O10)* tempo para concluir a autorização | do banco | a v1.0 já traz o par: **O15**, tempo para determinar o que vai acontecer na tela do banco |
| **O21** *(antigo O12)* conexão pendente sem saber o que falta | do banco | mantido — já está escrito sobre o saber |
| **O24** *(antigo O13)* tempo para determinar como corrigir | compartilhado | mantido |

## 5. Onde os gates cobrem hipóteses que já existiam

| Hipótese | O que os gates trazem |
|---|---|
| **H1** preparar antes do redirecionamento | **Deixa de ser hipótese e vira especificação.** O modelo de gates é H1 inteira, com oito unidades, ordem fixa e texto por banco. |
| **H3** checklist do que ter em mãos | É o "pacote de preparação montado" — só os gates que dispararam para aquele banco × tipo × perfil × canal. |
| **H5** recuperação por tipo de erro | A seção "Depois — se não concluiu" cobre G3, G6 e G8 com orientação pós-falha. Combina com as oito famílias de erro do mapa do widget. |
| **H2** confirmação imediata no retorno | A mensagem universal dos **5 minutos** para o banco começar a enviar dados é a peça que faltava: a tela de sucesso deve oferecer seguir trabalhando, em vez de parecer travada. |
| **H8** roteamento por poderes | É o G1, já especificado, com o comportamento por banco levantado. |

## 6. Três lacunas do modelo de gates

Nenhuma invalida o modelo. Todas são trabalho que não está coberto e que alguém vai supor que está.

### 6.1 A escolha do trilho está a montante dos gates

O nó raiz é "o usuário escolhe banco + tipo de conexão". O modelo **começa depois da escolha**, tratando-a como entrada dada.

Mas o mapa do widget identificou justamente aí a maior oportunidade aparente da zona A: num widget só de PJ a lista chega a 77 entradas, e nove marcas aparecem nos dois trilhos — Itaú com quatro entradas, Caixa e Santander com três. E a escolha muda quem pode autorizar: o trilho direto aceita operador, o Open Finance exige todos os aprovadores.

**O gate G1 pergunta "você tem acesso admin?" depois de a pessoa já ter escolhido um trilho que talvez fosse evitável.** Se a resposta for "só operador" e o banco for o Santander, o Direct funciona e o Open Finance não — mas a escolha já foi feita. H7 e H8 são, na verdade, o mesmo problema atacado em dois momentos, e o momento mais barato é antes.

**Proposta — corrigida.** O gate existe na v1.0 e se chama **`entry.rail`**, na etapa 3. **"Gate zero" é nome proibido:** G0 colidiria com a árvore de decisão de outro time, e gate fora da série G leva prefixo (`entry.*`, `bridge.*`).

O dado confirma a leitura: **L2 é 19,2%, a segunda maior perda, e é a única faixa do fluxo sem gate nenhum hoje.** E **32% das seleções vêm da busca**, o que sugere que a lista não é navegável por leitura.

Ressalva que não estava aqui: mover G1 para antes da lista **adiciona atrito exatamente em L2**. É uma pergunta aberta para o time, não uma decisão tomada.

### 6.2 Não há gate para pop-up bloqueado

O G6 cobre a passagem para o app do banco. Não cobre o caso em que **o navegador bloqueia o pop-up do handoff** — que a base de suporte registra como recorrente, a ponto de a Pluggy recusar pedidos de clientes para remover o aviso.

É um atrito de classe diferente das três: não é da Pluggy nem do banco, é do navegador. E o aviso atual chega no pico de E1 com forma indistinguível de um alerta de golpe. Era a H9 e continua sem dono no modelo.

### 6.3 A etapa 8 Concluir não tem gate

O modelo termina em "início do fluxo do banco", mais a mensagem dos 5 minutos. O que acontece depois da conexão bem-sucedida — O15 (ser surpreendido com o que o sistema faz com o acesso) e O14 (saber como revogar) — fica de fora. É coerente com o escopo declarado, que é preparação; vale só não confundir cobertura de preparação com cobertura do job.

## 7. O risco que precisa de métrica de guarda desde o primeiro teste

O estudo é explícito: o job é instrumental, ninguém quer conectar conta, e "a tolerância a esforço, dúvida e risco percebido é baixa". **Oito gates são oito oportunidades de desistir antes de chegar ao banco.**

O modelo já mitiga isso ao ser uma espinha dorsal que acumula num único pacote, em vez de 64 caminhos. Mas o risco é real e é quantificável com o funil que já existe:

**Números substituídos pelo mapa L1–L5.**

| Perda | % dos loads | Gates |
|---|---|---|
| **L2** age na tela inicial e não escolhe banco | **19,2%** | nenhum hoje; `entry.rail` é a proposta |
| **L3** escolhe banco e não submete | 9,6% | `entry.credentials`, G1, G2, G3 |
| **L5** cria item e não chega a sucesso | **~23,5%** | G6, G7, G8, espera |

**O orçamento continua válido, com os números certos:** os gates de preparação precisam custar, em L2 e L3, menos do que economizam em L5. A guarda deixa de ser uma transição de funil e passa a ser o conjunto do desenho experimental da v1.0 — abandono antes da seleção, tempo até a primeira ação e, sobretudo, **cobertura de contas da empresa**, a única guarda capaz de transformar ganho aparente em perda real.

É um teste honesto e barato de montar. E tem um desdobramento útil: se um gate custa mais do que economiza, ele não deve virar tela — vira texto dentro de uma tela que já existe.

## 8. Uma crítica ao G1, que é o gate mais importante

O G1 pergunta: *"Você tem acesso de administrador ou master neste banco?"*

Duas objeções.

**A pessoa pode não saber responder.** "Admin", "master", "operador" são nomes de perfil do internet banking, não vocabulário do empresário. Quem usa o banco todo dia para pagar fornecedor não necessariamente sabe sob qual perfil está logado. Uma pergunta que o executor não consegue responder com confiança não atende O5 — só transfere o erro para mais cedo, com aparência de rigor.

**Uma pergunta de comportamento seria mais confiável que uma de nomenclatura.** Algo como *"no site do banco, você consegue cadastrar um novo pagamento sozinho, sem que outra pessoa precise aprovar?"* — o empresário sabe responder isso. E a resposta cobre de uma vez o perfil (G1) e a dupla aprovação (G8), que hoje são dois gates perguntando facetas do mesmo fato.

**Melhor ainda seria não perguntar.** Verificar vale mais que perguntar, e o estudo deveria registrar essa preferência: `USER_NOT_SUPPORTED` e o warning 002 são sinais que a Pluggy já recebe. Não servem para a primeira tentativa, mas servem para a segunda — e para dizer ao cliente, antes de o usuário abrir o widget, que aquele CNPJ já falhou por perfil.

## 9. Duas afirmações do artefato que precisam de dado antes de virar prioridade

Adversarial, no espírito do resto do estudo:

1. **"G1 é a maior fonte isolada de perda silenciosa de conversão."** É uma conclusão de análise de fluxo, não de medição. O estudo tem essa mesma pergunta em aberto desde a v0.2 — "com que frequência quem está no widget não é o titular ou não tem poderes na conta?" — e ela segue sem resposta. Verificável: contagem de `USER_NOT_SUPPORTED` por conector, mais a decomposição da zona B. **Enquanto não medido, G1 é a hipótese mais promissora, não o fato estabelecido.**

2. **A cobertura parcial é o risco número um, não uma ressalva de amostra.** Era assim que esta seção tratava o assunto; a v1.0 corrige a ênfase. São 16 conectores revisados, **só cinco bancos com variantes de gate finalizadas**, e o widget principal exibe **mais de 170 instituições**. A consequência não é margem de erro, é desenho: o conteúdo de gate precisa funcionar de forma genérica na lista inteira, e mais genérico pode ser menos eficaz do que a evidência dos cinco bancos sugere. **O experimento pode acabar medindo cinco bancos em vez do sistema.**

## 10. Outcomes que os gates sugerem e o job map não tem

Três candidatos, para o banco de hipóteses das entrevistas:

- **Compartilhamento em bloco.** "Todas as contas da empresa naquele banco são compartilhadas de uma vez — o usuário não escolhe." Isto é um golpe direto em **O2** (autorizar mais acesso do que pretendia), e é **inegociável**: vem do desenho do Open Finance. É o exemplo mais puro de outcome que a Pluggy só pode tornar esperado, nunca satisfazer. Vale medir a importância na entrevista justamente por isso — se for alto, é argumento para o trilho direto em certos casos.
- **Assinatura eletrônica.** A Unicred pede uma antes do consentimento, e nenhum outro fluxo revisado pede. Se aparecer em mais cooperativas, é gate novo.
- **Saber que a espera acabou.** Os 5 minutos do Open Finance não pertencem a nenhum gate e são o que separa "conectado" de "conectado e funcionando". Reforça O11.

## 11. Instrumentação: os gates são eventos

Cada gate é tela mais ação, ou seja, **cada gate é instrumentável**. E é isso que resolve um problema que o funil tem hoje: **não há nenhuma visibilidade entre `SELECTED_INSTITUTION` e `SUBMITTED_LOGIN`** — exatamente onde os gates de preparação vão viver, e onde se perdem 7.976 pessoas.

Recomendação: cada variante de gate emite um evento com o próprio ID estável (o esquema de 5 caracteres do artefato, `G1001` e afins). Com isso:

- a perda passa a ser atribuível ao gate, não à transição inteira;
- a resposta do G1 vira dimensão de segmentação de todo o funil, o que responde a pergunta aberta nº 4 sem pesquisa;
- o custo de cada gate fica mensurável isoladamente, o que permite remover os que não pagam.

O esquema de IDs do artefato foi pensado para design, conteúdo e engenharia. **Vale estendê-lo a analytics desde o início** — é barato agora e caro depois.

## 12. Próximos passos

1. Instrumentar os gates como eventos, usando os IDs estáveis, antes de desenhar as telas.
2. Fixar a transição clique → formulário enviado (85,9%) como métrica de guarda do modelo inteiro.
3. Medir o G1 antes de construí-lo: `USER_NOT_SUPPORTED` por conector e decomposição da zona B.
4. Testar a formulação comportamental do G1 contra a de nomenclatura, e avaliar a fusão de G1 e G8 numa pergunta só.
5. Decidir o **`entry.rail`** — usar a resposta de poderes para ordenar ou rotular a lista, unindo H7 e H8. Pesar contra o atrito que isso adiciona em L2, que é a segunda maior perda.
6. Escrever o gate que falta para pop-up bloqueado, ou registrar que fica fora do modelo.
7. Levar as três afirmações da seção 10 para o roteiro das entrevistas com PME.
