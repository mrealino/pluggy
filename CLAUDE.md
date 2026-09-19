# Estudo JTBD — conversão no widget de conexão da Pluggy

Contexto migrado de uma conversa no claude.ai (18–19 set 2026). Este arquivo resume o que já foi alinhado.

- Documento vivo: `docs/estudo-jtbd-widget.html` (versão 0.4)
- Mapa do widget: `docs/mapa-widget.md` (versão 1.0)
- Refino dos outcomes: `docs/modelo-valor-outcomes.md` (versão 1.0)

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

#### Próxima tarefa C: fechar o modelo de valor

`docs/modelo-valor-outcomes.md` v1.0 confronta o modelo com a Figura 2.4 e conclui que os outcomes estão subespecificados em cerca de seis vezes (2 por etapa contra a dúzia que Ulwick estabelece). Já desenvolveu a dúzia completa em três etapas — 36 outcomes:

- `G1–G12` etapa transversal "Garantir que não está sendo golpeado" (substitui E1 e O7)
- `R1–R12` etapa 2 "Reunir acesso e poderes" (substitui O4, O5)
- `P1–P12` etapa 3 "Escolher por onde conectar" (substitui O6)

Pendente:

1. Desenvolver ~44 outcomes nas cinco etapas restantes. Depende de evidência nova — não inventar.
2. Validar com produto e design a promoção de E1 a etapa transversal e a dissolução da etapa 4 antes de reescrever a seção 5 do documento vivo.
3. Decidir o destino de E2 a E5. Suspeita: E5 não é emoção, é a etapa "Acompanhar a conclusão" mal especificada.
4. Confirmar os proxies comportamentais no Amplitude antes de usá-los como satisfação.
5. Montar o questionário de importância sobre os 36 outcomes refinados.

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
