# Mapa do widget de conexão (Pluggy Connect)

Versão 1.0 — 19 de setembro de 2026. Insumo para o estudo JTBD (`docs/estudo-jtbd-widget.html`).

## 0. Método, e por que este mapa não saiu do Chrome

A tarefa original previa percorrer https://demo-connect.pluggy.dev/ com a integração do Chrome. **Não foi possível nesta sessão**: o ambiente remoto bloqueia a saída de rede para `connect.pluggy.ai`, `demo-connect.pluggy.dev` e `api.pluggy.ai` (o proxy responde 403 no CONNECT, por política da organização). Não é falta de credencial — é egresso bloqueado. O passo de observação direta continua pendente e está listado na seção 10.

No lugar dele, este mapa foi reconstruído a partir de duas fontes que o MCP de documentação da Pluggy expõe sem autenticação:

- **[DOC]** — guias oficiais da documentação viva (`connect-widget/*`, `open-finance/*`, `connections/*`, `guides/sandbox`, `developer-tools/tutorials/*`).
- **[QA]** — base curada de perguntas e respostas reais do suporte da Pluggy.
- **[INFERÊNCIA]** — leitura minha a partir das duas anteriores. Precisa de validação.

As ferramentas de dashboard (`list_connectors`, `get_stats`, `get_reports`) exigem re-autenticação do conector e não puderam ser usadas. Tudo que dependeria delas está marcado como pendente.

**Consequência metodológica:** este documento descreve o widget como a documentação o especifica, não como ele se apresenta na tela. Toda contagem de conectores abaixo é o universo da Pluggy, não a lista que um cliente específico exibe — a diferença importa e é o assunto da seção 1.

---

## 1. O widget não é um artefato só: três camadas de variação antes de qualquer experimento

Este é o achado que mais muda o desenho dos experimentos, e ele **contradiz em parte o que está registrado como "confirmado v0.2"** no CLAUDE.md ("customização: apenas nome da empresa na primeira página, logo e cor dos botões").

### Camada 1 — Personalização via Dashboard [DOC: `connect-widget/customization`]

| Item | Escopo | Impacto no estudo |
|---|---|---|
| Nome da empresa | 20 caracteres, tela de boas-vindas | já mapeado |
| Logo | telas principais | já mapeado |
| Cor primária | telas, botões, componentes interativos | já mapeado |
| **Raio de borda dos botões** | todos os botões | novo |
| **Texto dos botões** | **primeira tela e tela de credenciais** | **novo — o CTA não é centralizado** |
| **Seleção de conectores** | liga/desliga por tipo (Pessoal, Empresarial, Investimento) | **novo — a lista de bancos varia por cliente** |
| **Textos de consentimento** | Termos e Políticas de Privacidade na 1ª tela; não self-service, passa por Vendas e validação jurídica | **novo — a tela candidata nº 1 a experimento já é variável** |

Recurso disponível na assinatura Pro e no Free Trial — ou seja, nem todo cliente customiza, o que cria uma variação a mais, não a menos.

### Camada 2 — Parâmetros do SDK, escolhidos pelo ERP no código [DOC: `connect-widget/environments`]

Esta camada não aparece no Dashboard e é invisível para quem olha só o funil:

| Parâmetro | O que faz | Por que importa |
|---|---|---|
| `selectedConnectorId` | **pula a etapa de seleção de conector** e vai direto ao login, após os termos | **sessões assim podem nunca emitir `SELECTED_INSTITUTION`** |
| `updateItem` | abre direto no formulário de credenciais do item | pula boas-vindas e lista |
| `connectorTypes` / `connectorIds` / `countries` | filtram a lista exibida | muda o tamanho e a composição da lista |
| `products` | restringe os produtos coletados | muda o que é consentido (O1–O3) |
| `openFinanceParameters` | pré-preenche CPF/CNPJ no formulário de Open Finance | remove uma etapa de digitação |
| `language` (padrão `pt`) / `theme` (`light` \| `dark`) | idioma e tema | variação visual não controlada |
| `allowFullscreen` (padrão `true`) / `allowConnectInBackground` | modal vs. tela cheia; permite minimizar | muda a experiência no celular |
| `forceOauthInBrowser` | força OAuth no navegador do sistema em vez de webview | **mitigação direta de perda no handoff** |
| `includeSandbox` | exibe conectores sandbox | contaminação de dados se ligado em produção |

### Camada 3 — Estado dos conectores no momento da sessão

O widget **exibe aviso de instabilidade** quando um conector está com `health` degradado [QA: "Cliente teve popup de erro ao conectar com C6"]. Ou seja, a tela de lista não é estável nem para o mesmo cliente ao longo do tempo.

### O que isso implica

1. **A premissa "quase todo o widget é testável de forma centralizada" precisa ser revista.** O CTA da primeira tela, o CTA da tela de credenciais, os textos de consentimento e a própria lista de bancos são todos variáveis por cliente. O que sobra de fato centralizado é a estrutura do fluxo, as telas de MFA, as telas de espera e as telas de erro.
2. **Estratificar por cliente não basta.** É preciso estratificar por *configuração*: dois clientes com o mesmo logo podem ter widgets funcionalmente diferentes se um usa `selectedConnectorId` e o outro não.
3. **[INFERÊNCIA — alta prioridade de verificação]** Se sessões com `selectedConnectorId` ou `updateItem` pulam a seleção de instituição, elas entram no funil em `Connect Widget Loaded` e **nunca podem** chegar a `List Item Clicked`. Parte dos **23.402** da zona A pode ser artefato de instrumentação, não abandono. Antes de tratar a zona A como oportunidade de UX, é preciso segmentar o funil por presença desses parâmetros.

---

## 2. As telas do fluxo

Reconstrução a partir da documentação. Cada tela está cruzada com a etapa do job map, os outcomes e o evento correspondente.

### Trilho comum

| # | Tela | Etapa do job | Outcomes | Evento do widget |
|---|---|---|---|---|
| 1 | **Boas-vindas / Termos** — nome da empresa do ERP, logo, Termos e Condições, Política de Privacidade, CTA customizável | 1 Definir, 2 Localizar, 4 Confirmar (antecipado) | O1–O5, O7 | `SUBMITTED_CONSENT` |
| 2 | **Lista de instituições** — agrupada por tipo; exibe aviso de instabilidade quando aplicável; pulável via `selectedConnectorId` | 3 Preparar | O6 | `SELECTED_INSTITUTION` (traz `connector`) |

### Trilho A — Conector direto (credenciais na UI da Pluggy)

| # | Tela | Etapa | Outcomes | Evento |
|---|---|---|---|---|
| 3A | **Formulário de credenciais** — campos variam por conector (seção 4); CTA customizável | 4 Confirmar, 5 Executar | O4, O5, O7, O10 | `SUBMITTED_LOGIN` |
| 3A' | **Seleção conta única / conta conjunta** — só em conectores como Bradesco Conta Conjunta; conta conjunta abre depois uma seleção de qual conta conectar | 3 Preparar | **O6** | — |
| 4A | **MFA** — 1 etapa (junto com as credenciais) ou 2 etapas (tela separada). Variantes documentadas no sandbox: token simples, **imagem QR**, **lista de opções para escolher**, **seleção de telefone antes do MFA**, **seleção de empresa depois do MFA** | 5 Executar | O8, O10 | `SUBMITTED_MFA` → `LOGIN_MFA_SUCCESS` |
| 4A' | **Login por QR** — sem credenciais; QR que muda rapidamente; item fica em `WAITING_USER_ACTION` (padrão Inter) | 5 Executar | O8, O9 | — |
| 5A | **Espera / polling** — `LOGIN_IN_PROGRESS` **pode levar até 5 minutos** [DOC: `connections/item-lifecycle`] | 6 Monitorar | **O11, O12** | `LOGIN_STEP_COMPLETED`, `ITEM_RESPONSE` (repetido) |

A **seleção de empresa depois do MFA** (`user-ok-multi-company` no sandbox) é uma tela de O6 que não estava no mapa: o operador de um escritório contábil ou de um grupo com várias CNPJs escolhe ali qual empresa conectar. Errar essa escolha produz uma conexão bem-sucedida na empresa errada — perda invisível para o funil, que a conta como sucesso.

### Trilho B — Open Finance (autorização no ambiente do banco)

| # | Tela | Etapa | Outcomes | Evento |
|---|---|---|---|---|
| 3B | **Formulário de CPF ou CNPJ** — só isso; pré-preenchível via `openFinanceParameters` | 4 Confirmar | O7 | `SUBMITTED_LOGIN` |
| 4B | **Handoff — pop-up para a instituição** — o widget avisa quando o pop-up está bloqueado [QA] | 5 Executar (pico) | **O8, O9** | — |
| 5B | **Fora do widget** — login na instituição (QR, deep link para o app, credenciais — depende do banco) e **seleção do que compartilhar** | 5 Executar (pico) | O1–O3, O10 | — |
| 6B | **Retorno** — desktop: a janela tenta se fechar sozinha; mobile: redireciona para o `oauthRedirectUri`. Sem `oauthRedirectUri` configurado, **o usuário fica numa página de autorização concluída sem caminho de volta** [DOC + QA] | 6 Monitorar | **O9, O11** | — |
| 7B | **Espera / polling** | 6 Monitorar | O11, O12 | `LOGIN_STEP_COMPLETED`, `ITEM_RESPONSE` |

### Telas terminais (ambos os trilhos)

| Tela | Etapa | Outcomes |
|---|---|---|
| **Sucesso** — `SUCCESS` ou `PARTIAL_SUCCESS` | 8 Concluir | O15 |
| **Erro** — 17 `executionStatus` de erro distintos (seção 6) | 7 Modificar | **O13** |
| **Pendente** — `USER_AUTHORIZATION_PENDING`: Caixa exige autorização de dispositivo com **~30 minutos** de espera; `onSuccess` **não é chamado** e o cliente recebe `onError` | 6 Monitorar, 7 Modificar | **O12, O13** |

---

## 3. Conectores e trilhos: os números

[DOC: `connections/connectors-coverage` e `open-finance/institutions-coverage`, ambos sincronizados com `GET /connectors`]

### Conectores diretos — 27 no total

| Tipo | Quantidade | Conectores |
|---|---|---|
| Pessoal | 8 | BB Previdência, Caixa, Redes Ethereum, Inter, Itaú Cartões, Mercado Pago, MeuPluggy, Wise |
| **Empresarial** | **11** | BB Empresas, BNB Empresas, Banrisul Empresas, Bradesco Empresas, Caixa Empresas, Cora, Efí Bank, Inter Empresas, Itaú Empresas, Santander Empresas, Sicredi Empresas |
| Investimento | 7 | Avenue, BTG, Caixa Previdência, EQI, Mercado Bitcoin, Necton, XP |
| Outros | 1 | Splitwise |

### Open Finance — 143 instituições

| Contexto | Quantidade |
|---|---|
| Com contexto **Empresarial** | **66** |
| Só Pessoal | 70 |
| Só Investimentos | 7 |

### A lista que o empresário da PME vê

Um widget configurado só para PJ (`connectorTypes: ['BUSINESS_BANK']`) apresenta, no limite, **até 77 entradas** (66 OF + 11 diretas) numa única lista. E 9 das 11 marcas do trilho direto têm gêmeas no Open Finance:

| Marca | Entradas OF-PJ | Entradas diretas PJ | **Entradas na lista** |
|---|---|---|---|
| **Itaú** | 3 (Itaú, Itaú BBA, Itaú Emps) | 1 (Itaú Empresas) | **4** |
| **Caixa** | 2 (Caixa Econômica Federal, CAIXA – clientes sem conta) | 1 (Caixa Empresas) | **3** |
| **Santander** | 2 (Santander, Santander Cartões) | 1 (Santander Empresas) | **3** |
| Banco do Brasil | 1 | 1 | 2 |
| Bradesco | 1 | 1 | 2 |
| Inter | 1 | 1 | 2 |
| Sicredi | 1 | 1 | 2 |
| Banrisul | 1 | 1 | 2 |
| Banco do Nordeste | 1 | 1 | 2 |
| Cora, Efí Bank | 0 | 1 | 1 |

**Este é o achado mais acionável do mapa.** Um empresário do Itaú que procura "Itaú" na lista encontra quatro opções, sem nenhuma informação que permita escolher entre elas — a diferença entre elas é o trilho regulatório, que não é vocabulário dele. **O6 ("minimizar a probabilidade de selecionar a instituição ou a conta errada") deixa de ser um outcome de baixa intensidade** (está marcado como "Intensidade baixa" na etapa 3 Preparar do estudo) **e passa a ser candidato a maior oportunidade da zona A.**

E a escolha tem consequência real, não cosmética [QA: "OF vs Direto — qual conector recomendar para PJ?"]:

| Critério | Melhor trilho |
|---|---|
| Qualidade de datas, descrições de transação, detalhe de boleto | **Direto** |
| CPF/CNPJ da contraparte, alcance de produtos | **Open Finance** |
| Login em Caixa e BB | **Open Finance** |
| Login nos demais, se bem configurado | **Direto** |
| **Quem pode autorizar** | **Direto** — aceita usuário OPERADOR, que muitas empresas já têm. **OF exige aprovação de todos os aprovadores (múltipla alçada)** |

A última linha é decisiva para o executor deste estudo. Para uma PME com dois sócios que assinam em conjunto, **o trilho Open Finance pode ser simplesmente inviável** e o trilho direto, viável — e nada na lista comunica isso.

---

## 4. Credenciais pedidas por conector (trilho direto, PJ)

[DOC: `developer-tools/tutorials/*`]

| Conector | O que é pedido no formulário |
|---|---|
| Caixa Empresas | usuário e senha do Internet Banking |
| Sicredi Empresas | CNPJ, usuário, senha |
| Sicoob PJ | número da cooperativa, chave de acesso, senha do Internet Banking |
| Santander Empresas | agência, conta, usuário, senha |
| Itaú Empresas | agência, conta, senha, CPF |
| Banco do Brasil Empresas | chave J, senha J, senha de 8 dígitos |
| Bradesco Empresas | usuário, senha, **chave de segurança gerada no app Bradesco** |
| Inter MEI | login no app Inter com o número da conta MEI + **leitura de QR code** |
| **Inter Empresas** | **Client ID, Client Secret, chave e certificado** de uma integração de API criada no Inter Empresas |
| **Efí Bank** | **Client ID, Client Secret e certificado** de uma aplicação de API criada no Efí |

### O que a lista de tutoriais revela sobre O4 e O5

A Pluggy mantém **14 tutoriais para conectores PJ**. Seis deles **não ensinam a conectar** — ensinam a provisionar acesso no banco *antes* de o widget servir para alguma coisa:

- Banco do Brasil PJ — autorizar o dispositivo no Internet Banking
- Bradesco PJ — habilitar acesso ao aplicativo móvel pela administração do IB
- Santander PJ — criar um usuário secundário
- Itaú PJ — criar um perfil de acesso e um operador sem token, e validá-lo pela web
- Inter Empresas — criar uma integração de API e emitir certificado
- Efí Bank — criar uma aplicação de API e emitir certificado

**Quase metade do esforço de documentação PJ da Pluggy está na etapa 2 Localizar, não na 5 Executar.** É a evidência mais forte que este mapa produziu de que **O4 ("iniciar sem ter em mãos o que será exigido") e O5 ("iniciar sem ter permissão para autorizar em nome da empresa") estão subatendidos** — e o estudo hoje trata ambos como outcomes secundários, com H3 marcada apenas como proposta.

Nenhum desses pré-requisitos é comunicado pelo widget antes da seleção da instituição. O empresário descobre que precisa de um certificado digital depois de já ter aceitado os termos e escolhido o banco.

---

## 5. Eventos do widget × funil do Amplitude

[DOC: `connect-widget/environments`, callback `onEvent`]

| Evento do widget | Significado documentado | Evento do funil (provável) |
|---|---|---|
| `SUBMITTED_CONSENT` | usuário confirmou termos e consentimento de privacidade **na primeira tela** | — **não está no funil** |
| `SELECTED_INSTITUTION` | selecionou uma instituição (traz o objeto `connector`) | `List Item Clicked` |
| `SUBMITTED_LOGIN` | enviou credenciais para criar o item | `Form Submitted` |
| `SUBMITTED_MFA` | enviou parâmetro extra pedido pela instituição | — |
| `LOGIN_SUCCESS` | enviou credenciais **com sucesso** | candidato a `Login Step Success` |
| `LOGIN_MFA_SUCCESS` | enviou o parâmetro extra **com sucesso** | — |
| `LOGIN_STEP_COMPLETED` | "conclusão bem-sucedida do login. O usuário **efetivamente fez login na instituição**" | candidato a `Login Step Success` |
| `ITEM_RESPONSE` | disparado a cada leitura do item na API — é o batimento do polling | base do `Item Polling Finished` |

### Duas correções ao que está registrado no estudo

**1. A zona A já pode ser dividida hoje, e melhor do que por page view.** O estudo propõe adicionar as visualizações `welcomePage` e `connectorsList` ao funil. Existe algo mais forte: `SUBMITTED_CONSENT` é uma **ação**, não uma visualização. Inserido entre `Connect Widget Loaded` e `List Item Clicked`, ele separa com precisão:

- *carregou → aceitou os termos* = abandono na tela de boas-vindas (O1–O5, O7; E1, E3)
- *aceitou os termos → clicou numa instituição* = abandono na lista (O6; E2)

São dois problemas de produto diferentes, com hipóteses diferentes. Hoje estão somados em 23.402.

**2. `Login Step Success` provavelmente significa coisas diferentes em cada trilho.** Esta é a pergunta aberta nº 2 do estudo, e a documentação dá uma resposta com ressalva:

- No **trilho direto**, as credenciais vão no formulário do widget. `LOGIN_STEP_COMPLETED` ("efetivamente fez login na instituição") é um login de verdade no banco.
- No **trilho Open Finance**, o que o usuário submete no widget é **apenas o CPF ou CNPJ**. O login acontece depois, no pop-up da instituição.

**[INFERÊNCIA]** Se o evento do funil for `LOGIN_SUCCESS` (submissão bem-sucedida de credenciais), então, no Open Finance, ele dispara **antes do handoff** — e a zona B (66%, 15.570 perdidos) **contém o redirecionamento regulado inteiro**, não apenas a espera. Isso reinterpreta a zona B de ponta a ponta: ela não é majoritariamente ansiedade de espera (E5), é majoritariamente a viagem de ida e volta ao banco (O9, E1).

Se for `LOGIN_STEP_COMPLETED`, o handoff já aconteceu e a leitura atual se sustenta.

**Como resolver em uma consulta:** segmentar a transição `Form Submitted → Login Step Success` por trilho. Se a conversão de 94,5% se mantiver parecida nos dois trilhos, o evento dispara antes do handoff no OF (é improvável que 94,5% das pessoas completem a autorização no banco). Se cair muito no trilho OF, dispara depois.

---

## 6. Modos de falha documentados, e o que cada um pede de UI

[DOC: `connections/item-lifecycle`]

O estudo trata a zona B como "erro técnico, erro do usuário e abandono". A documentação é mais granular — são **17 estados finais de erro**, e eles pedem recuperações diferentes. Isso dá corpo a H5 (recuperação específica por tipo de erro), hoje só uma proposta:

| Grupo | `executionStatus` | O que a UI precisa dizer |
|---|---|---|
| **Credencial errada** | `INVALID_CREDENTIALS`, `INVALID_CREDENTIALS_MFA` | qual campo, e que o item não é atualizável — precisa recomeçar |
| **Conta bloqueada ou exigindo ação no banco** | `ACCOUNT_LOCKED`, `ACCOUNT_NEEDS_ACTION`, `ACCOUNT_CREDENTIALS_RESET` | **a ação é no banco, não aqui** — e o campo `providerMessage` traz a instrução da própria instituição |
| **Pessoa errada / conta errada** | `USER_NOT_SUPPORTED` (ex.: conta "Operador" na Caixa Empresas) | **O5 puro** — quem está no widget não pode fazer isto |
| **Autorização de dispositivo pendente** | `USER_AUTHORIZATION_PENDING`, `USER_AUTHORIZATION_NOT_GRANTED` | **esperar**, e quanto — a Caixa leva ~30 min |
| **Consentimento revogado** | `USER_AUTHORIZATION_REVOKED` | foi revogado no app do banco |
| **Instituição fora do ar** | `SITE_NOT_AVAILABLE`, `CONNECTION_ERROR`, `ALREADY_LOGGED_IN` | não é culpa do usuário — tentar depois |
| **Timeout de MFA** | `USER_INPUT_TIMEOUT` | o código expirou |
| **Falha da Pluggy** | `ERROR`, `MERGE_ERROR` | não é culpa do usuário |

Vale notar que `ACCOUNT_NEEDS_ACTION` já carrega `providerMessage` com instruções da instituição — existe matéria-prima para mensagens específicas sem inventar copy.

---

## 7. Três mecanismos estruturais de perda que o estudo ainda não contempla

Estes não são problemas de persuasão nem de reassurance. São mecânicos, e provavelmente respondem por uma fração relevante da zona B.

### 7.1 `oauthRedirectUri` não configurado pelo cliente

[DOC: `connect-widget/oauth-support` + QA: "Redirect no app mobile após fluxo OF não volta para widget"]

Alguns navegadores móveis não permitem que a janela de autorização se feche sozinha. Sem `oauthRedirectUri`, **o usuário fica olhando uma página de autorização concluída sem caminho de volta para o app**. A autorização funcionou; a conexão consta como não concluída.

É um item recorrente no suporte. E o parâmetro é responsabilidade do ERP, não da Pluggy — ou seja, **parte da conversão de cada cliente é função de uma linha na integração dele**, não da UI. Existe ainda `forceOauthInBrowser`, que evita problemas de webview e tem precedência sobre a configuração da API.

**Ação imediata, sem experimento:** levantar quais clientes criam connect tokens sem `oauthRedirectUri` e cruzar com a conversão da zona B por cliente. Se a correlação existir, isso é trabalho de CS e documentação — mais barato e mais rápido que qualquer teste A/B, e explicaria a suspeita de que "clientes grandes podem dominar o número".

### 7.2 Pop-up bloqueado

[QA: "Mensagem do widget sobre popup bloqueado pode ser removida?"]

O handoff do Open Finance abre um pop-up. Bloqueadores de pop-up o impedem. O widget já mostra uma mensagem sobre isso — e a Pluggy se recusa a removê-la a pedido de clientes, o que confirma que o problema é frequente. Essa mensagem chega ao usuário **no pico exato de ansiedade (E1)** e é, em forma, indistinguível de um alerta de golpe.

**É a melhor candidata a experimento de copy de todo o fluxo**: intervém no pico, é centralizada, não é regulada e não passa pelo jurídico.

### 7.3 O ciclo vicioso: ansiedade → nova tentativa → limite de taxa → falha

[DOC: `open-finance/rate-limits` + QA: "Códigos de warning/erro no Open Finance"]

Os limites operacionais do Open Finance são **por mês, por CPF/CNPJ + instituição + produto**, e contam **entre itens diferentes**. O mais apertado:

| Produto | Requisições/mês |
|---|---|
| **Lista e detalhes da conta** | **4** |
| Transações não recentes (7–365 dias) | 4 |
| Identidade, empréstimos | 4 |

Criar um item consome essas cotas. Um empresário que, sem saber se deu certo (E5, O11), **tenta conectar o mesmo banco cinco vezes no mesmo mês, esgota a cota de listagem de contas** — e a quinta tentativa retorna `PARTIAL_SUCCESS` com warning 423.

Duas consequências:

- A ansiedade de não saber se deu certo **não custa só abandono: degrada o produto de quem persiste**. Isso eleva a importância de O11 e O12 acima do que o estudo assume, e fortalece H2.
- **`PARTIAL_SUCCESS` conta como sucesso na definição atual do funil.** Parte dos 30.230 "sucessos" pode ser conexão degradada por retentativa. O baseline de 37,9% é, nesse ponto, otimista. Vale medir a proporção `SUCCESS` vs `PARTIAL_SUCCESS` e a distribuição de warnings antes de fixá-lo.

---

## 8. Múltipla alçada: resposta à pergunta aberta nº 5

[QA: "Como funciona múltipla alçada (multi-signature) para contas PJ no Open Finance?" e "Códigos de warning/erro no Open Finance"]

- É observável: o `statusDetail` traz o **warning código 002 — "Conta pendente de autorização"**. A frequência pode ser medida contando itens PJ de Open Finance com esse warning. **Isto responde o "como medir" da pergunta 5; falta rodar a consulta** (bloqueada pela re-autenticação do dashboard).
- **O outro aprovador não recebe notificação pela Pluggy.** Depende do banco. Do ponto de vista do widget, o fluxo simplesmente para, e a UI não tem como saber de quem está esperando.
- Há uma proposta oficial no conselho do Open Finance para mudar isso: aprovadores notificados pelo app do banco, **basta um aprovador consentir**, e qualquer operador pode fazer o login inicial. Se aprovada, remove boa parte do problema — o que é argumento para **não** investir pesado em UI para múltipla alçada agora, e sim em detectá-la e explicá-la.
- O sandbox já simula os três casos (aprovado, rejeitado, autenticação lenta), então dá para prototipar sem conta real.

**Consequência para o job map:** existe um estado, hoje ausente, em que o job **não pode ser concluído pelo executor sozinho**. A etapa 6 Monitorar precisa de um outcome próprio — proposta: **O16, minimizar o tempo para saber que a conclusão depende de outra pessoa e de quem**.

---

## 9. Efeito sobre as hipóteses do estudo

| Hipótese | Situação após o mapa |
|---|---|
| H1 preparar antes do redirecionamento | **Reforçada e mais concreta.** Agora se sabe o que preparar: pop-up, o que o banco vai pedir (QR, app, credenciais), e a tela de seleção de compartilhamento. |
| H2 confirmação imediata no retorno | **Reforçada, com novo argumento.** Não é só conforto: reduz retentativa, que consome cota de Open Finance e degrada o resultado. |
| H3 checklist do que ter em mãos | **Promover de proposta a prioridade alta.** Seis dos catorze tutoriais PJ são sobre provisionar acesso antes de começar. É o outcome com mais evidência de subatendimento. |
| H4 resumo de permissões | Mantida. No Open Finance a seleção de compartilhamento acontece **no banco**, fora do widget — o resumo teria de ser antecipatório, não substituto. |
| H5 recuperação por tipo de erro | **Mais concreta.** 17 estados de erro agrupáveis em 8 famílias, e `providerMessage` como fonte de texto. |
| H6 mostrar como revogar | Mantida, com precisão nova: consentimentos de Open Finance **não expiram por padrão** e se revogam **no app do banco**, não no ERP. Inter PJ é exceção, expira em um ano. |

### Hipóteses novas propostas

- **H7 — desambiguar instituições duplicadas na lista.** Quando a mesma marca aparece nos dois trilhos (Itaú: 4 entradas), rotular por consequência para o usuário, não por trilho regulatório. Outcome: O6. Emocional: E2. *Maior oportunidade aparente da zona A.*
- **H8 — roteamento por poderes antes da lista.** Perguntar se a pessoa pode autorizar sozinha em nome da empresa e, quando não, sugerir o trilho direto com usuário operador. Outcomes: O5, O6. Emocional: E2. *Depende de confirmar a frequência do problema.*
- **H9 — tratar o aviso de pop-up bloqueado como tela de pico.** Reescrever a mensagem para que não pareça alerta de golpe e diga o próximo passo concreto. Outcomes: O8, O9. Emocional: E1. *Menor custo de implementação de todas as hipóteses.*

### Não-hipótese: correção de configuração

O `oauthRedirectUri` ausente (7.1) **não deve virar experimento**. É defeito de integração. Vira trabalho de CS, documentação e talvez um aviso no Dashboard. Convém medir antes de experimentar em cima de um ruído que se resolve sem UI.

---

## 10. O que continua pendente

**Depende de desbloqueio de rede (ou de rodar o Chrome na máquina local):**

1. Percorrer o widget tela a tela e registrar o texto real de cada uma. Todo este mapa descreve a especificação, não a interface.
2. Verificar a ordem e a redação da tela de boas-vindas, e como os termos são apresentados.
3. Conferir se a lista de instituições tem busca, como agrupa e como exibe marcas duplicadas.
4. Ler a redação exata do aviso de pop-up bloqueado (insumo de H9).
5. Percorrer os fluxos do sandbox sem credenciais reais: `user-ok-multi-company`, `user-ok-phone`, `user-ok-select`, QR, conta conjunta, e o fluxo Open Finance (CPF `761.092.776-73`, banco simulado). Tudo isso é sintético — não envolve credencial real nem conexão real.

**Depende de re-autenticar o conector do dashboard da Pluggy:**

6. `list_connectors` para a lista real da aplicação "marco", em vez do universo documentado.
7. `get_stats` com `kind: items-by-connector` para distribuir a zona B por conector e por `executionStatus` — responde a pergunta aberta nº 3 diretamente.
8. Contagem de itens PJ de Open Finance com warning 002 — responde a pergunta nº 5.

**Depende de consulta no Amplitude:**

9. Segmentar o funil por presença de `selectedConnectorId` e `updateItem` (seção 1).
10. Inserir `SUBMITTED_CONSENT` no funil para dividir a zona A (seção 5).
11. Segmentar `Form Submitted → Login Step Success` por trilho para resolver o significado do evento (seção 5).
12. Proporção `SUCCESS` vs `PARTIAL_SUCCESS` nos 30.230 e distribuição de warnings (seção 7.3).
