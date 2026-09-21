# Síntese: o que as quatro análises dizem juntas

Versão 1.0 — 19 de setembro de 2026. Análise cruzada de `estudo-jtbd-widget` (job map e funil), `mapa-widget` (fluxo e conectores), `modelo-valor-outcomes` (banco de outcomes) e `gates-jobs` (modelo de gates). Este documento não repete as quatro fontes — ele diz o que só aparece quando as quatro são lidas juntas.

## 1. A conclusão que muda a ordem do trabalho

**O 37,9% ainda não é um baseline.**

O funil perde 49.600 pessoas. Lidas juntas, as quatro análises identificam **quatro causas de natureza diferente** dentro desse número, e apenas uma delas é problema de UX no sentido que o estudo assumia:

| Causa | Natureza | Onde bate | Dimensionada? |
|---|---|---|---|
| **Instrumentação** — sessões com `selectedConnectorId` ou `updateItem` pulam a seleção de instituição e nunca podem emitir `List Item Clicked` | artefato de medição | os 23.402 | **não** |
| **Configuração do cliente** — `oauthRedirectUri` ausente deixa o usuário sem caminho de volta do banco | defeito de integração do ERP | os 15.570 | **não** |
| **Mecânico** — pop-up bloqueado, limite de taxa do Open Finance por retentativa, múltipla alçada pendente, espera de autorização de dispositivo | estrutural, não persuasivo | 15.570 + parte dos 7.976 | **não** |
| **Outcome desatendido** — O4, O5, O6 | UX, o alvo original | 23.402 + 7.976 | parcialmente |

Três das quatro não têm tamanho. Enquanto não tiverem, **não se sabe quanto dos 49.600 é sequer endereçável por experimento de UX** — e qualquer teste A/B roda sobre um denominador contaminado.

Isso não paralisa o trabalho: dimensionar as três primeiras é barato, usa dados que já existem e não depende de pesquisa com o empresário. É a fase 0 da seção 8.

## 2. A convergência: três análises independentes apontam para a mesma etapa

O sinal mais forte de todo o material, e o mais fácil de perder porque está espalhado.

| Fonte | O que encontrou | Aponta para |
|---|---|---|
| **Estudo** | O4 e O5 são os únicos outcomes da etapa 2, e H3 estava marcada apenas como proposta | etapa 2 Localizar |
| **Mapa do widget** | 6 dos 14 tutoriais PJ da Pluggy não ensinam a conectar — ensinam a provisionar acesso no banco antes | etapa 2 Localizar |
| **Gates** | 5 dos 8 gates atendem à etapa 2 | etapa 2 Localizar |
| **Banco de outcomes** | o conjunto R é o mais lastreado: 5 das 12 formulações vêm de achado documentado | etapa 2 Localizar |

Nenhuma das três olhou para as outras. O mapa saiu da documentação, os gates saíram das telas de referência dos conectores, o estudo saiu do funil.

**A etapa 2 "Localizar" — reunir dispositivo, credenciais, app do banco e poderes na conta — é onde começar.** O estudo original a tratava como intensidade média, com dois outcomes e uma hipótese não priorizada. A evidência acumulada diz o contrário.

E há um detalhe que reforça: a etapa 2 é a única em que **a Pluggy pode agir antes de o banco entrar em cena**. Tudo que acontece depois é atrito do banco, que só se consegue tornar esperado.

## 3. A maior oportunidade isolada não pertence a nenhum dos modelos

Num widget só de PJ, a lista chega a 77 entradas, e nove marcas aparecem nos dois trilhos — Itaú com quatro entradas, Caixa e Santander com três. A escolha entre elas muda **quem pode autorizar**: o trilho direto aceita usuário operador, que muitas empresas já têm; o Open Finance exige a aprovação de todos os aprovadores da conta.

Cruzando as quatro fontes, essa escolha cai num vão:

- O **estudo** classificava O6 como intensidade baixa.
- O **mapa** identificou o problema e o chamou de maior oportunidade aparente da zona A.
- O **modelo de gates** começa explicitamente *depois* da escolha — o nó raiz é "o usuário escolhe banco + tipo de conexão".
- O **banco de outcomes** tem P2, P3, P4 e P12 escritos, mas eles não são cobertos por nenhum gate.

**Ninguém está olhando para o momento mais barato de resolver o problema mais caro.** O G1 pergunta "você tem acesso admin?" depois de a pessoa já ter escolhido um trilho que talvez fosse evitável: se ela é operador e o banco é o Santander, o Direct funciona e o Open Finance não — mas a escolha já foi feita.

**H7 e H8 são o mesmo problema atacado em dois momentos.** A proposta que sai deste cruzamento é um gate zero: usar a resposta de poderes para ordenar ou rotular as entradas duplicadas na própria lista, convertendo a pergunta de triagem em roteamento.

## 4. Três classes de outcome, e uma regra de triagem

O modelo de gates classifica o atrito por propriedade — alavanca da Pluggy, do banco, compartilhado. Aplicada aos outcomes do estudo, essa taxonomia produz uma distinção que nenhuma das fontes enuncia sozinha:

| Classe | O que a Pluggy pode fazer | Exemplos |
|---|---|---|
| **Satisfazível** | mover o número | O4, O5, O6, O13 — verificar, perguntar, ordenar antes do banco |
| **Apenas esperável** | fazer com que não pareça erro | O10, O12 — a Caixa leva 30 min, e isso não muda |
| **Inegociável** | apenas divulgar | **O2** no Open Finance: todas as contas da empresa naquele banco são compartilhadas de uma vez, e o usuário não escolhe |

A regra prática: **para outcome apenas esperável, reescreva o outcome sobre o saber, não sobre o fato.** "Minimizar o tempo para concluir a autorização" (O10) é um outcome que a Pluggy não pode atender; "minimizar o tempo para saber quanto a autorização vai levar" é. A diferença decide qual métrica o experimento persegue e impede prometer o que não se entrega.

O caso de O2 merece atenção própria: é um outcome que o desenho do Open Finance torna impossível de satisfazer. Se a importância dele for alta nas entrevistas, isso vira **argumento de produto para o trilho direto em certos casos** — não um problema de copy.

## 5. A teoria implícita dos gates sobre os jobs emocionais

Vale explicitar, porque é uma divergência silenciosa entre as fontes e é testável.

O **modelo de gates é inteiramente funcional**. Não há gate de segurança, de confiança ou de tranquilidade. E, no entanto, o próprio artefato de gates diz: *"uma etapa normal do banco que chega sem aviso é lida como erro; antecipada, é lida como progresso"*.

Isso é uma tese sobre E1. A teoria implícita é que **a ansiedade de legitimidade não é uma necessidade independente — é subproduto de expectativa não atendida.** Se for verdade, E1 não precisa de tratamento próprio: some quando os gates fazem o trabalho.

O estudo assume o contrário: E1 é job emocional com peso próprio, e "o fluxo legítimo parece golpe" porque os bancos treinaram o cliente a desconfiar de redirecionamentos — um reflexo que existiria mesmo com expectativa perfeitamente calibrada.

**As duas teses levam a produtos diferentes.** Pela primeira, basta prever bem e nenhuma reassurance é necessária. Pela segunda, há um trabalho de legitimidade que nenhum aviso de preparação resolve.

É uma das perguntas mais valiosas para a entrevista com PME, e é barata de fazer: perguntar sobre uma conexão que deu certo e entender se o desconforto sumiu por saber o que ia acontecer, ou se permaneceu apesar disso.

## 6. O que a instrumentação dos gates desbloqueia

Três peças de fontes diferentes que só funcionam juntas:

1. O **banco de outcomes** mostra que outcomes escritos como tempo têm proxy comportamental — satisfação pode sair do funil, sem pesquisa.
2. O **mapa do widget** mostra que o funil não tem nenhum evento entre `SELECTED_INSTITUTION` e `SUBMITTED_LOGIN`.
3. Os **gates** vivem exatamente nesse vão, e cada um é tela mais ação — portanto, instrumentável, e já com esquema de ID estável.

Juntando: **os IDs de gate são a instrumentação que faz os proxies comportamentais funcionarem.** Nenhum dos três documentos diz isso sozinho.

Consequências diretas:

- A perda passa a ser atribuível ao gate, não à transição inteira de 7.976.
- A resposta do G1 vira dimensão de segmentação do funil inteiro — o que **responde a pergunta aberta nº 4 do estudo sem pesquisa nenhuma**.
- O custo de cada gate fica isolável, o que permite remover os que não pagam.

Por isso a recomendação é instrumentar **antes** de desenhar as telas. O esquema de IDs foi pensado para design, conteúdo e engenharia; estendê-lo a analytics é barato agora e caro depois.

## 7. A tensão que precisa de métrica de guarda

O estudo é explícito: o job é instrumental, ninguém quer conectar conta, "a tolerância a esforço, dúvida e risco percebido é baixa", e **"reassurance espalhada por todas as telas vira ruído"**.

O modelo de gates propõe oito unidades de orientação antes do banco.

A contradição é real, e o modelo de gates já a mitiga ao ser uma espinha dorsal que acumula num pacote único em vez de 64 caminhos. Mas o cruzamento permite quantificar o limite:

| Janela | Perda hoje | Papel |
|---|---|---|
| Clique na instituição → formulário enviado | **7.976** (85,9%) | onde vivem os gates de preparação |
| Login bem-sucedido → polling com sucesso | **15.570** (66,0%) | onde a preparação precisa pagar |

**Os gates de preparação precisam custar menos na primeira janela do que economizam na segunda.** A transição de 85,9% é a métrica de guarda do modelo inteiro, desde o primeiro teste.

Com um corolário de desenho: **se um gate custa mais do que economiza, ele não vira tela — vira texto dentro de uma tela que já existe.**

## 8. Plano sequenciado

### Fase 0 · Saneamento (nenhum experimento antes disto)

Tudo aqui usa dados existentes e não depende do empresário.

1. Segmentar o funil por presença de `selectedConnectorId` e `updateItem`.
2. Levantar clientes que criam connect tokens sem `oauthRedirectUri` e cruzar com a conversão da zona B.
3. Inserir `SUBMITTED_CONSENT` no funil para separar abandono nas boas-vindas do abandono na lista.
4. Resolver o significado de `Login Step Success` segmentando a transição anterior por trilho.
5. Medir `SUCCESS` contra `PARTIAL_SUCCESS` nos 30.230, e a distribuição de warnings.
6. Contar `USER_NOT_SUPPORTED` por conector e itens PJ de Open Finance com warning 002.

**Saída:** um baseline confiável, e o tamanho real da oportunidade de UX.

### Fase 1 · Instrumentação

7. Emitir um evento por variante de gate, com o ID estável, antes de desenhar qualquer tela.
8. Fixar a transição clique → formulário enviado (85,9%) como métrica de guarda.

### Fase 2 · Entrevistas com PME

9. Roteiro sobre importância, usando as 36 formulações do banco de outcomes como material de apoio — descartar as que não ressoam, capturar as que faltam.
10. Testar a tese de E1 da seção 5: a ansiedade some com expectativa calibrada, ou persiste?
11. Testar a formulação comportamental do G1 contra a de nomenclatura.
12. Medir a importância de O2 — o compartilhamento em bloco — que é inegociável e pode virar argumento de trilho.

### Fase 3 · Experimentos, nesta ordem

13. **Gate zero** — ordenar ou rotular as entradas duplicadas usando poderes (H7 + H8). Maior oportunidade, e a montante de tudo.
14. **Pacote de preparação** — os gates da etapa 2 (H1 + H3), onde as três análises convergem.
15. **Aviso de pop-up** (H9) — menor custo de implementação de todas, e no pico de E1.
16. **Recuperação por tipo de erro** (H5) — 17 estados em 8 famílias, com `providerMessage` como fonte de texto.

## 9. Tensões não resolvidas entre as fontes

Registradas em vez de conciliadas por suposição.

| Tensão | Entre | Como resolver |
|---|---|---|
| "G1 é o maior fator de perda" é conclusão de análise de fluxo; o estudo tem a mesma pergunta em aberto desde a v0.2 | Gates × Estudo | `USER_NOT_SUPPORTED` por conector (fase 0) |
| E1 é necessidade própria ou subproduto de expectativa não atendida | Estudo × Gates | entrevista (fase 2) |
| Reassurance espalhada vira ruído × oito gates de orientação | Estudo × Gates | métrica de guarda (seção 7) |
| O6 como intensidade baixa × maior oportunidade da zona A | Estudo × Mapa | resolvido: O6 foi elevado a alta na v0.3 |
| Cobertura: 16 conectores revisados × 11 diretos PJ e 66 instituições OF no universo documentado | Gates × Mapa | a generalização do modelo de gates vale para 16, não para 66 |
| Granularidade: 2 outcomes por etapa × uma dúzia em Ulwick | Estudo × Banco | resolvido: fica em 2; a granularidade vem das entrevistas |

## 10. O que continua desconhecido

Consolidado das quatro fontes, ordenado pelo que cada resposta destrava.

| Pergunta | Destrava | Custo |
|---|---|---|
| Quanto da perda da zona A é instrumentação e não abandono | o baseline inteiro | consulta |
| Quantos clientes não configuram `oauthRedirectUri` | dimensionar a zona B | consulta |
| O que `Login Step Success` significa em cada trilho | a leitura da zona B | consulta |
| Com que frequência quem está no widget não tem poderes | prioridade de G1 e do gate zero | consulta |
| Qual lista de conectores cada cliente de fato exibe | validade dos experimentos por cliente | dashboard |
| A importância de cada outcome | a priorização por oportunidade | entrevista |
| Se E1 sobrevive à expectativa calibrada | o escopo do trabalho de legitimidade | entrevista |
| O texto real de cada tela do widget | H9 e toda revisão de copy | Chrome, pendente |

As seis primeiras não dependem do empresário e podem ser respondidas nesta semana. As duas últimas são as que exigem campo.
