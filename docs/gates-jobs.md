# Gates × jobs e outcomes

Versão 1.0 — 19 de setembro de 2026. Cruza o modelo de gates (*A lógica dos gates · Guided Connect*, 8 gates sobre 16 conectores) com o job map e os outcomes do estudo.

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

| Gate | O que faz | Etapa do job | Outcomes |
|---|---|---|---|
| Raiz · banco + tipo | define o kit de credenciais antes de qualquer redirecionamento | 3 Preparar | **O6** |
| **G1** perfil admin × operador | pergunta se a pessoa tem poderes | **2 Localizar** | **O5**, O4 |
| **G2** credenciais técnicas do Inter | avisa que é tarefa de TI | **2 Localizar** | **O4** |
| **G3** autorização de dispositivo | avisa que leva de 30 min a 24h | 2 Localizar, 6 Monitorar | O4, **O12**, O13 |
| **G4** QR no app para gerar token | pede o celular por perto | **2 Localizar** | **O4**, O8 |
| **G5** expiração rápida do código | manda abrir o app antes | 5 Executar | O8, O10 |
| **G6** consentimento no app | explica que termina no celular | 5 Executar (pico) | **O8, O9** |
| **G7** tela de consentimento | antecipa o resumo de compartilhamento | 1 Definir | **O1, O2, O3** |
| **G8** múltiplos titulares | pergunta se precisa de dupla aprovação | 2 Localizar, 6 Monitorar | **O5, O12, O16** |

**Cinco dos oito gates atendem a etapa 2 Localizar.** Os outcomes dessa etapa são exatamente dois no estudo — O4 e O5. O mapa do widget já tinha chegado lá por outro caminho: seis dos catorze tutoriais PJ da Pluggy são sobre provisionar acesso no banco antes de conectar.

Três análises independentes apontando para a mesma etapa é a evidência mais forte que este estudo tem de onde está a oportunidade.

## 3. Os gates são a decomposição empírica de O4 e O5

Vale registrar, porque fecha uma discussão anterior. A v0.4 do estudo tentou decompor os outcomes deduzindo uma dúzia por etapa a partir de Ulwick, e a decisão foi não seguir por ali — a granularidade viria das entrevistas, não de dedução em cima de documentação.

**Os gates fazem exatamente essa decomposição, e por um caminho melhor.** "Minimizar a probabilidade de iniciar sem ter em mãos o que será exigido" (O4) se decompõe, na prática dos fluxos, em: sem o celular por perto (G4), sem o dispositivo autorizado (G3), sem as credenciais técnicas (G2), sem tempo antes do código expirar (G5). Isso não é dedução — é observação de dezesseis conectores.

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
| O10 minimizar o tempo para concluir a autorização | do banco | minimizar o tempo para saber quanto a autorização vai levar |
| O12 minimizar a probabilidade de a conexão ficar pendente sem saber o que falta | do banco | mantido — já está escrito sobre o saber, não sobre o pendente |
| O13 minimizar o tempo para saber como corrigir quando algo falha | compartilhado | mantido |

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

**Proposta:** um gate zero, antes da lista ou embutido nela, que use a resposta de poderes para ordenar ou rotular as entradas duplicadas. Converte a pergunta do G1 de triagem em roteamento.

### 6.2 Não há gate para pop-up bloqueado

O G6 cobre a passagem para o app do banco. Não cobre o caso em que **o navegador bloqueia o pop-up do handoff** — que a base de suporte registra como recorrente, a ponto de a Pluggy recusar pedidos de clientes para remover o aviso.

É um atrito de classe diferente das três: não é da Pluggy nem do banco, é do navegador. E o aviso atual chega no pico de E1 com forma indistinguível de um alerta de golpe. Era a H9 e continua sem dono no modelo.

### 6.3 A etapa 8 Concluir não tem gate

O modelo termina em "início do fluxo do banco", mais a mensagem dos 5 minutos. O que acontece depois da conexão bem-sucedida — O15 (ser surpreendido com o que o sistema faz com o acesso) e O14 (saber como revogar) — fica de fora. É coerente com o escopo declarado, que é preparação; vale só não confundir cobertura de preparação com cobertura do job.

## 7. O risco que precisa de métrica de guarda desde o primeiro teste

O estudo é explícito: o job é instrumental, ninguém quer conectar conta, e "a tolerância a esforço, dúvida e risco percebido é baixa". **Oito gates são oito oportunidades de desistir antes de chegar ao banco.**

O modelo já mitiga isso ao ser uma espinha dorsal que acumula num único pacote, em vez de 64 caminhos. Mas o risco é real e é quantificável com o funil que já existe:

| Janela do funil | Perda hoje | Relação com os gates |
|---|---|---|
| Clique na instituição → formulário enviado | **7.976** | onde vivem os gates de preparação (G1, G2, G4, G8) |
| Login bem-sucedido → polling com sucesso | **15.570** | onde vivem os gates de fluxo (G3, G5, G6, G7) e onde a preparação deveria pagar |

**O orçamento do modelo é este: os gates de preparação precisam custar, na primeira janela, menos do que economizam na segunda.** Como métrica de guarda, a transição clique → formulário enviado, hoje em 85,9%, não deve cair.

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

2. **A cobertura é parcial, e a amostra não é aleatória.** São 16 conectores revisados, contra 11 diretos PJ e 66 instituições de Open Finance com contexto empresarial no universo documentado. Os revisados são os grandes, o que é a escolha certa — mas a afirmação "o Open Finance tem o mesmo formato em toda instituição revisada" tem alcance de 16, não de 66. O próprio artefato reconhece isso ao listar Banrisul como nunca analisado e o Banco do Nordeste como sem documentação.

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
5. Decidir o gate zero — usar a resposta de poderes para ordenar ou rotular a lista, unindo H7 e H8.
6. Escrever o gate que falta para pop-up bloqueado, ou registrar que fica fora do modelo.
7. Levar as três afirmações da seção 10 para o roteiro das entrevistas com PME.
