# Estudo JTBD — conversão no widget de conexão da Pluggy

Contexto migrado de uma conversa no claude.ai (18–19 set 2026). Este arquivo resume o que já foi alinhado.

Publicado em `docs/estudo-jtbd-widget.html`, em cinco abas. **A aba Main é a síntese e o ponto de entrada**; as outras quatro guardam os dados de cada linha de investigação.

| Aba | Fonte | Conteúdo |
|---|---|---|
| **Main** | `docs/sintese.md` (v2.0) | análise cruzada, **reconciliada contra a v1.0 do Estudo** |
| Estudo | `docs/fonte-connect-outcome-map.html` (v1.0) | Mapa de outcomes do Connect — bilíngue PT/EN, E1–E7, camada de gates, funil com eventos reais |
| Mapa do widget | `docs/mapa-widget.md` (v1.1) | telas, conectores, famílias de erro — números de funil superados |
| Banco de outcomes | `docs/modelo-valor-outcomes.md` (v1.1) | 36 formulações para testar em entrevista |
| Gates × jobs | `docs/gates-jobs.md` (v1.1) | 8 gates cruzados com job map e outcomes |
| — | `docs/de-para-outcomes.md` (v1.0) | numeração antiga → v1.0, gates e jobs emocionais |

Ao acrescentar uma análise nova: ela vira aba própria **e** a Main é atualizada com o que o cruzamento revela.

Documento externo vira aba com `scripts/integrar-aba.py`, que prefixa as classes com `om-` e escopa o CSS sob o painel — sem isso ele reestiliza as outras abas, porque usa os mesmos nomes de token e de classe.

> **A numeração de outcomes da v1.0 é a válida** — 30 outcomes, não 16. De/para em `docs/de-para-outcomes.md`. Todo número de funil anterior ao mapa L1–L5 está superado.

## Quem sou e o objetivo

Sou Product Manager na Pluggy (Open Finance, conecta ERPs, plataformas contábeis e BPOs a instituições financeiras). Objetivo desta fase: rodar experimentos de UX no widget de conexão (Pluggy Connect) para aumentar a conversão do empresário da PME, de modo que ele chegue ao fim do fluxo informado e sem dúvidas. Os experimentos devem atacar primeiro os outcomes com maior oportunidade (importância alta e satisfação baixa).

Trabalho com Jobs to be Done na abordagem Outcome-Driven Innovation (ODI). Referência de método: Ulwick, *What Customers Want* — em particular a Figura 2.4 (customer value model da serra circular Bosch), que fixa o padrão de granularidade e formato dos outcomes. O trabalho sobre consentimento (definido como contrato para delegar agência) vem depois; agora o foco é a UI do widget.

## Como quero que você trabalhe

- Seja sistêmico, sistemático e adversarial: questione premissas, aponte inconsistências nos dados e separe fato de hipótese.
- Marque formulações novas como proposta, para eu validar antes de levar ao time.
- Responda em português.

## Executor e hierarquia de jobs

Executor: o empresário da PME, quem conecta de fato ou quem detém a conta sobre a qual o acesso é concedido. Fora do escopo por enquanto: jobs de ERPs, contadores, bancos, jobs de consumo do produto Pluggy e jobs emocionais sociais.

- Jobs centrais: saber quanto dinheiro a empresa tem e terá; receber o que é devido sem erro; pagar o que deve sem erro.
- Job instrumental atendido pelo widget: conceder ao sistema de gestão acesso à conta bancária da empresa. Ninguém quer conectar conta; a tolerância a esforço e risco percebido é baixa.

## Jobs emocionais pessoais

"Segurança" e "transparência" são atributos da solução, não jobs. Decomposição:

- E1: sentir-se protegido contra golpes ao autorizar acesso à conta da empresa
- E2: sentir-se confiante de que está fazendo certo
- E3: evitar sentir-se enganado sobre o que está autorizando
- E4: sentir-se no controle do acesso concedido
- E5: evitar a ansiedade de não saber se deu certo

Insight central: o fluxo legítimo parece golpe (bancos ensinaram a nunca informar senha fora do app e a desconfiar de redirecionamentos). Reassurance espalhada em todas as telas vira ruído; intervir nos picos. O pico de ansiedade acontece em parte no app do banco, fora do controle da Pluggy: as janelas de intervenção são antes (preparar) e depois (reentrada).

## Mapa do job (8 etapas do ODI) e outcomes

| Etapa | Job funcional (proposta) | Emocional | Outcomes |
|---|---|---|---|
| 1 Definir | Definir quais acessos conceder e para quê | E3, E4 | O1 minimizar o tempo para saber quais dados ou operações o sistema terá acesso; O2 minimizar a probabilidade de autorizar mais acesso do que pretendia; O3 minimizar a probabilidade de não saber para que o acesso será usado |
| 2 Localizar | Reunir o necessário: dispositivo, app do banco, token, credenciais, poderes na conta | E2 | O4 minimizar a probabilidade de iniciar sem ter em mãos o que será exigido; O5 minimizar a probabilidade de iniciar sem permissão para autorizar em nome da empresa |
| 3 Preparar | Escolher a instituição e a conta certas | E2 (**alta**, reavaliado v0.3) | O6 minimizar a probabilidade de selecionar a instituição ou a conta errada |
| 4 Confirmar | Verificar que o pedido é legítimo e que tem poderes | E1 | O7 minimizar a probabilidade de desconfiar da legitimidade do pedido e desistir |
| 5 Executar | Autorizar o acesso junto à instituição | E1 (pico) | O8 minimizar a probabilidade de não saber o que fazer na etapa seguinte; O9 minimizar a probabilidade de se perder na ida e volta entre o sistema e o app do banco; O10 minimizar o tempo para concluir a autorização |
| 6 Monitorar | Acompanhar se a conexão foi concluída | E5 | O11 minimizar o tempo para saber se a conexão foi concluída; O12 minimizar a probabilidade de a conexão ficar pendente sem saber o que falta; **O16 (proposta v0.3)** minimizar o tempo para saber que a conclusão depende de outra pessoa, e de quem |
| 7 Modificar | Corrigir falhas e ajustar ou revogar | E4, E2 | O13 minimizar o tempo para saber como corrigir quando algo falha; O14 minimizar o tempo para saber como revogar ou alterar a autorização |
| 8 Concluir | Voltar ao sistema com a conta conectada | E4, E3 | O15 minimizar a probabilidade de ser surpreendido com o que o sistema faz com o acesso |

Os outcomes originais ("maximizar a probabilidade de conectar com sucesso" e "maximizar a probabilidade de entender cada passo") foram decompostos: o primeiro é a própria métrica de conversão; o segundo cita a solução e enviesa para mais texto.

## Dados do funil (Amplitude, Connect – Prod, 30 dias desde 20 ago, base inteira)

| Transição | Conversão | Perda |
|---|---|---|
| Connect Widget Loaded (79.830) → List Item Clicked (56.428) | 70,7% | 23.402 |
| → Form Submitted (48.452) | 85,9% | 7.976 |
| → Login Step Success (45.800) | 94,5% | 2.652 |
| → Item Polling Finished, SUCCESS ou PARTIAL_SUCCESS (30.230) | 66,0% | 15.570 |
| Ponta a ponta | 37,9% | 49.600 |

Um print com dados de um único cliente foi descartado; usar só a base inteira.

- Zona A (carregamento → clique em instituição): maior perda absoluta, inteira no widget, não regulada. O funil não separa boas-vindas/termos da lista de bancos; os eventos de visualização existem (`location: welcomePage`, `location: connectorsList`).
- Zona B (login bem-sucedido → sucesso): maior perda relativa. Mistura erro técnico, abandono no handoff para o banco e abandono na espera. Decompor antes de experimentar.
- Cuidados: 37,9% é média da base (agrupar por cliente); parte da perda inicial pode ser widget carregado sem intenção ou falha de carregamento; excluir sandbox e sessões internas.

## Respostas já confirmadas

- Customização pelos ERPs: **revisado na v0.3.** Além de nome da empresa, logo e cor, são customizáveis o raio de borda, o texto dos botões da primeira tela e da tela de credenciais, a seleção de conectores exibidos e os textos de consentimento. Há ainda uma camada de parâmetros do SDK escolhidos no código do ERP (`selectedConnectorId` pula a seleção de instituição; `updateItem` abre direto nas credenciais). Estratificar por configuração, não só por cliente.
- Regulação: pelas regras do Open Finance, só o handoff para o banco é regulado. A LGPD (consentimento livre, informado e inequívoco) continua valendo dentro do widget; variantes da tela de termos devem passar pelo jurídico.

## Perguntas ainda abertas

1. O que Login Step Success significa em cada trilho. O mapa propõe um teste barato (segmentar `Form Submitted → Login Step Success` por trilho); falta rodar.
2. Entre os 15.570 da zona B, quanto é erro técnico, erro do usuário e abandono.
3. Quanto da perda da zona A é abandono e quanto é sessão que nunca teve a etapa de seleção de instituição.
4. Com que frequência quem está no widget não é o titular ou não tem poderes na conta.
5. Quantos clientes não configuram `oauthRedirectUri`, e quanto isso explica da zona B.
6. Qual lista de conectores cada cliente de fato exibe (o universo documentado não é o que o empresário vê).

Respondidas na v0.3: divisão entre trilhos (27 diretos, sendo 11 PJ; 143 instituições de Open Finance, sendo 66 com contexto empresarial) e credenciais por conector direto PJ; e como medir a múltipla alçada (warning 002 no `statusDetail`).

## Estado do mapeamento do widget

`docs/mapa-widget.md` v1.0 existe, derivado da documentação viva da Pluggy (MCP Pluggy Docs) e da base de Q&A do suporte — **não da observação da tela**. No ambiente remoto do Claude Code a saída de rede para `connect.pluggy.ai`, `demo-connect.pluggy.dev` e `api.pluggy.ai` é bloqueada pelo proxy (403 no CONNECT). As ferramentas de dashboard do MCP (`list_connectors`, `get_stats`) pedem re-autenticação do conector.

### Próxima tarefa A: percorrer o widget (requer Chrome, rodar localmente)

Use `claude --chrome` ou `/chrome` numa sessão local, não nesta.

1. Abrir https://demo-connect.pluggy.dev/ (aba React Pluggy Connect).
2. Em Connect Demo Settings, usar https://connect.pluggy.ai e o cliente com label "marco". Eu preencho as credenciais; não peça nem grave o client secret em arquivos.
3. Gerar o connectToken e abrir o widget.
4. Registrar o texto e os elementos reais de cada tela, confirmando ou corrigindo a seção 2 do mapa.
5. Conferir: se a lista de instituições tem busca, como agrupa, como exibe marcas duplicadas (Itaú tem 4 entradas), e a redação exata do aviso de pop-up bloqueado (insumo de H9).
6. Percorrer os fluxos sintéticos do sandbox (`includeSandbox: true`): `user-ok-multi-company`, `user-ok-phone`, `user-ok-select`, QR, conta conjunta e o fluxo Open Finance com CPF `761.092.776-73`. São dados sintéticos — não envolvem credencial real nem conexão real.
7. Não concluir conexões reais nem submeter credenciais reais.
8. Atualizar `docs/mapa-widget.md` para a v1.1 e o estudo para a v0.4.

### Conclusões da síntese (aba Main)

1. **O 37,9% ainda não é um baseline.** Das 49.600 perdas, quatro causas distintas: instrumentação, configuração do cliente, mecânica e outcome desatendido. Três não têm tamanho. Dimensioná-las é a fase 0 e não depende do empresário.
2. **Três análises independentes convergem na etapa 2 Localizar** — é onde começar, e é a única etapa em que a Pluggy age antes de o banco entrar.
3. **A maior oportunidade isolada está num vão entre modelos:** a escolha do trilho (Itaú com 4 entradas) fica a montante dos gates e era intensidade baixa no estudo. Proposta: gate zero unindo H7 e H8.
4. **Três classes de outcome:** satisfazível, apenas esperável, inegociável. Para o apenas esperável, reescrever sobre o *saber*, não sobre o *fato*.
5. **Divergência testável sobre E1:** os gates supõem que a ansiedade de legitimidade é subproduto de expectativa não atendida; o estudo supõe necessidade própria. Levar à entrevista.
6. **Os IDs de gate são a instrumentação que faz os proxies comportamentais funcionarem** — instrumentar antes de desenhar telas.

### Decisão sobre granularidade de outcomes

**O job map segue com cerca de dois outcomes por etapa.** A Figura 2.4 de Ulwick sugere uma dúzia, e a v0.4 chegou a tratar isso como déficit — a decisão foi não seguir por ali. A granularidade fina virá das **entrevistas com empresários de PME**, não de dedução em cima de documentação. Não reintroduzir a cota de 12 no documento central.

Os 36 outcomes de `docs/modelo-valor-outcomes.md` ficam como **banco de hipóteses para o roteiro das entrevistas**. O que vale guardar da Figura 2.4 é o formato (*minimizar o tempo para [ação observável]*), não a quantidade.

Os gates são a exceção útil: eles decompõem O4 e O5 empiricamente, a partir de dezesseis fluxos reais, e por isso já podem virar backlog.

### Próxima tarefa C: gates

`docs/gates-jobs.md` cruza o modelo de gates (8 gates, 16 conectores) com o job map. Achados:

- **Cinco dos oito gates atendem a etapa 2 Localizar.** Somado aos seis tutoriais PJ de provisionamento, são três análises independentes apontando para a mesma etapa.
- **Gates são solução, outcomes são critério.** Não deixar o time tratar os gates como o modelo.
- **Há outcomes que a Pluggy só pode tornar esperados, não satisfazer** (atrito do banco). Isso muda a redação de O10.
- **Lacunas:** a escolha do trilho está a montante dos gates (H7); não há gate para pop-up bloqueado (H9); a etapa 8 Concluir não tem gate.
- **Métrica de guarda:** os gates de preparação vivem na transição clique → formulário enviado (85,9%, perde 7.976) e precisam pagar na zona B (perde 15.570). Se um gate custa mais do que economiza, vira texto numa tela existente, não tela nova.

Pendente:

1. Instrumentar os gates como eventos, com os IDs estáveis, **antes** de desenhar telas.
2. Medir o G1 antes de construí-lo: `USER_NOT_SUPPORTED` por conector.
3. Testar a formulação comportamental do G1 ("você consegue cadastrar um pagamento sozinho?") contra a de nomenclatura ("você tem acesso admin?"), e avaliar fundir G1 e G8.
4. Decidir o gate zero, que une H7 e H8 na própria lista de instituições.
5. Confirmar os proxies comportamentais no Amplitude antes de usá-los como satisfação.
6. Montar o roteiro das entrevistas com PME, usando os 36 como banco de hipóteses.

## Próxima tarefa B: saneamento de dados, antes de qualquer experimento

Ver a lista reordenada na seção 11 do estudo. Os quatro primeiros itens (segmentar por configuração, levantar `oauthRedirectUri` ausente, inserir `SUBMITTED_CONSENT` no funil, resolver o significado de Login Step Success) precedem qualquer teste A/B: hoje não se sabe quanto da perda é comportamento e quanto é instrumentação ou configuração.

## Hipóteses candidatas de experimento

- H1: preparar o empresário antes do redirecionamento (O7, O8, O9; E1)
- H2: confirmação imediata e explícita no retorno (O11, O12; E5)
- H3 (prioridade alta v0.3): checklist do que ter em mãos, incluindo poderes na conta (O4, O5; E2). Seis dos catorze tutoriais PJ da Pluggy são sobre provisionar acesso no banco antes de começar.
- H4 (proposta): resumo de permissões em linguagem simples (O1–O3; E3)
- H5 (detalhada v0.3): recuperação específica por tipo de erro — 17 estados em 8 famílias, `providerMessage` como fonte de texto (O13; E2)
- H6 (proposta): mostrar como revogar na conclusão. Consentimentos de OF não expiram por padrão e se revogam no app do banco (O14, O15; E4)
- H7 (novo v0.3): desambiguar instituições duplicadas na lista (O6; E2) — maior oportunidade aparente da zona A
- H8 (novo v0.3): roteamento por poderes antes da lista, sugerindo o trilho direto com usuário operador (O5, O6; E2)
- H9 (novo v0.3): tratar o aviso de pop-up bloqueado como tela de pico (O8, O9; E1) — menor custo de todas

Não é hipótese: `oauthRedirectUri` ausente na integração do ERP é defeito de configuração, trabalho de CS, não experimento.

Priorização: Oportunidade = Importância + máx(Importância − Satisfação, 0). Segmentar por trilho, instituição, titular ou operador, dispositivo e cliente.

**Inversão da v0.4:** satisfação sai de proxy comportamental no funil (de graça); o acesso escasso ao empresário fica reservado para medir importância. Tabela de proxies em `docs/modelo-valor-outcomes.md`, seção 5.

**Métrica primária de cada experimento é o outcome que ele mira, não a conversão.**

## Exportar uma aba

`scripts/export-aba.py` gera um HTML autocontido de uma aba (o documento publicado é um fragmento; o export carrega o próprio esqueleto, abre com duplo clique e imprime).

```
python3 scripts/export-aba.py estudo          # -> docs/export/estudo.html
python3 scripts/export-aba.py gates caminho.html
```

Abas: `main`, `estudo`, `mapa`, `modelo`, `gates`. Reexportar depois de mudar o documento — os arquivos em `docs/export/` são derivados e não devem ser editados à mão.

## Estado da reconciliação (22 set 2026)

As três abas foram reconciliadas contra a v1.0. **Correções materiais, todas contra afirmações minhas anteriores:**

1. **O 37,9% não existe.** Era construído com `Login Step Success` (dispara 22–25× por item, mede polling) e `Item Polling Finished` (falta em ~41% dos itens). O funil defensável é 58,0% dentro do widget, 7 dias.
2. **A convergência na etapa 2 não sobrevive como prioridade.** Era convergência entre análises qualitativas; nenhuma media perda. Os gates da etapa 2 vivem em L3 = 9,6%. As duas maiores perdas são L5 (~23,5%) e L2 (19,2%).
3. **São três gates na etapa 2, não cinco** — G1, G2, G3, e dois só no trilho direto.
4. **"Gate zero" é nome proibido.** G0 colidiria com a árvore de decisão de outro time. O gate é `entry.rail`, etapa 3 — e o dado o confirma: L2 é a única faixa sem gate.
5. **A cobertura parcial é risco número um, não ressalva.** 16 conectores revisados, cinco com variantes finalizadas, 170+ instituições no widget. O experimento pode medir cinco bancos em vez do sistema.
6. **A divergência sobre E1 se resolveu por absorção** — a v1.0 mantém E1 como job e adota os gates, tratando o excesso de reassurance como restrição de desenho.

**Achado novo, sem equivalente nas abas anteriores:** o documento pré-preenchido (CPF × CNPJ). ~46% dos itens em `USER_INPUT_TIMEOUT` num cliente, invertendo por segmento dentro do mesmo banco (Santander PF 8% × Empresas 83%). É o O14, maior razão evidência/esforço do material.

**Bloqueante antes de qualquer telemetria nova:** allowlist de propriedades — CPF e CNPJ em ~138 mil eventos em 90 dias.

### Ordem de trabalho vigente

Fase 0, correções que entregam sozinhas: allowlist; clientes sem `oauthRedirectUri`; documento pré-preenchido.
Fase 1, tornar o experimento legível: wrapper de telemetria, `Connection Reconciled`, gates instrumentados, segmentação por configuração do SDK.
Fase 2, medir quem é o executor — premissa mais cara de estar errada.
Fase 3, experimentos: H10, H9, H7, H1.

### Pendência conhecida

A aba **Banco de outcomes** não foi reconciliada em profundidade: as colunas "substitui O4 e O5" e afins usam a numeração antiga, e o alvo de ~80 outcomes ficou obsoleto (a v1.0 tem 30). O de/para cobre a leitura; a reescrita não foi feita.
