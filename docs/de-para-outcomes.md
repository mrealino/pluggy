# De/para dos outcomes: numeração antiga → v1.0

A v1.0 do Estudo renumerou os outcomes e foi de 16 para 30. As abas Main, Mapa do widget, Banco de outcomes e Gates × jobs foram escritas contra a numeração antiga. Esta tabela é o que torna as quatro legíveis juntas.

**Regra:** a numeração da v1.0 é a válida. Onde uma aba citar um número antigo sem correspondência marcada aqui, tratar como referência a revisar.

| Antigo | v1.0 | Outcome | Etapa |
|---|---|---|---|
| O1 | **O1** | tempo para determinar quais dados e operações o sistema terá acesso | 1 |
| O2 | **O2** | probabilidade de delegar mais capacidade do que pretendia | 1 |
| O3 | **O3** | probabilidade de interpretar errado a finalidade do acesso | 1 |
| O4 | **O6** | probabilidade de iniciar sem ter em mãos o que será exigido | 2 |
| O5 | **O7** | probabilidade de iniciar sem poderes para autorizar em nome da empresa | 2 |
| O6 | **O10** | probabilidade de selecionar a instituição errada | 3 |
| O7 | **O13** | probabilidade de desistir por desconfiar da legitimidade | 4 |
| O8 | **O16** | tempo para determinar o próximo passo em cada tela do banco | 5 |
| O9 | **O17** | probabilidade de se perder na ida e na volta | 5 |
| O10 | **O18** | tempo para concluir a autorização | 5 |
| O11 | **O20** | tempo para determinar se a conexão foi concluída | 6 |
| O12 | **O21** | probabilidade de a conexão ficar pendente sem saber o que falta | 6 |
| O13 | **O24** | tempo para determinar como corrigir quando algo falha | 7 |
| O14 | **O26** | tempo para determinar como revogar ou alterar a delegação | 7 |
| O15 | **O27** | probabilidade de ser surpreendido com o que o sistema faz com o acesso | 8 |
| O16 | **O22** | tempo para determinar que a conclusão depende de outra pessoa, e de quem | 6 |

## Os catorze que não existiam

Nenhuma das outras abas os cobre. Vários vieram de medição, não de dedução.

| v1.0 | Outcome | Etapa | Evidência |
|---|---|---|---|
| O4 | tempo para determinar quem, além do sistema de gestão, verá os dados | 1 | doc |
| O5 | probabilidade de conceder acesso que não cobre o que a contabilidade exige | 1 | doc |
| O8 | tempo para determinar que o acesso precisa ser provisionado no banco antes | 2 | **dado** |
| O9 | número de idas ao banco antes de conseguir iniciar | 2 | hipótese |
| O11 | probabilidade de selecionar o trilho errado para os poderes que tem | 3 | doc |
| O12 | tempo para determinar qual entrada da mesma marca corresponde à sua conta | 3 | doc |
| **O14** | **probabilidade de submeter o documento errado — CPF onde se exige CNPJ** | 4 | **dado** |
| O15 | tempo para determinar o que vai acontecer na tela do banco | 4 | doc |
| O19 | probabilidade de estar num canal em que a autorização não pode ser concluída | 5 | **dado** |
| O23 | número de tentativas repetidas antes de saber o resultado | 6 | doc |
| O25 | probabilidade de repetir a mesma falha na tentativa seguinte | 7 | **dado** |
| O28 | tempo para determinar onde o consentimento vive depois e quando expira | 8 | doc |
| O29 | probabilidade de a conexão quebrar depois sem aviso | 8 | **dado** |
| O30 | tempo para determinar que falta dado de um período que precisa ser apurado | 8 | **dado** |

## Jobs emocionais

E1 a E5 seguem iguais. A v1.0 acrescenta dois, com o teste discriminante de que só são distintos se o abandono tiver causa e tratamento diferentes:

- **E6** — sentir que a decisão é reversível. Não é E4: controle é sobre o estado depois de concedido, reversibilidade é sobre o custo do "sim" antes de clicar.
- **E7** — evitar a sensação de estar sem saída quando algo falha. Não é E5: E5 se resolve com status, E7 se resolve com saída. O caso concreto é o `oauthRedirectUri` ausente, em que o status existe e a pessoa continua presa.

## Gates

A v1.0 renumerou em setembro de 2026 e acrescentou gates fora da série G, com prefixo. **Não se cria G0** — colidiria com a árvore de decisão de outro time.

| Gate | Etapa | Fluxo |
|---|---|---|
| `entry.welcome` | 1 | ambos |
| G1 perfil de acesso | 2 | ambos |
| G2 credenciais técnicas | 2 | só direto |
| G3 autorização de dispositivo | 2 | só direto |
| `entry.rail` *(proposto)* | 3 | ambos |
| `entry.credentials` | 4 | ambos |
| G4 QR no app para obter token | 4 | ambos |
| G5 expiração rápida do token | 4–5 | ambos |
| G6 consentimento no app | 5 | só OF |
| G7 tela de consentimento | 5 | só OF |
| G8 múltiplos titulares | 5–6 | só OF |
| `bridge.waiting` *(proposto)* | 6 | ambos |
