# Estudo JTBD — conversão no widget de conexão da Pluggy

Contexto migrado de uma conversa no claude.ai (18–19 set 2026). Este arquivo resume o que já foi alinhado. O documento completo está em `docs/estudo-jtbd-widget.html` (versão 0.2).

## Quem sou e o objetivo

Sou Product Manager na Pluggy (Open Finance, conecta ERPs, plataformas contábeis e BPOs a instituições financeiras). Objetivo desta fase: rodar experimentos de UX no widget de conexão (Pluggy Connect) para aumentar a conversão do empresário da PME, de modo que ele chegue ao fim do fluxo informado e sem dúvidas. Os experimentos devem atacar primeiro os outcomes com maior oportunidade (importância alta e satisfação baixa).

Trabalho com Jobs to be Done na abordagem Outcome-Driven Innovation (ODI). O trabalho sobre consentimento (definido como contrato para delegar agência) vem depois; agora o foco é a UI do widget.

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
| 3 Preparar | Escolher a instituição e a conta certas | E2 | O6 minimizar a probabilidade de selecionar a instituição ou a conta errada |
| 4 Confirmar | Verificar que o pedido é legítimo e que tem poderes | E1 | O7 minimizar a probabilidade de desconfiar da legitimidade do pedido e desistir |
| 5 Executar | Autorizar o acesso junto à instituição | E1 (pico) | O8 minimizar a probabilidade de não saber o que fazer na etapa seguinte; O9 minimizar a probabilidade de se perder na ida e volta entre o sistema e o app do banco; O10 minimizar o tempo para concluir a autorização |
| 6 Monitorar | Acompanhar se a conexão foi concluída | E5 | O11 minimizar o tempo para saber se a conexão foi concluída; O12 minimizar a probabilidade de a conexão ficar pendente sem saber o que falta |
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

- Customização pelos ERPs: apenas nome da empresa na primeira página, logo e cor dos botões. Estratificar experimentos por cliente.
- Regulação: pelas regras do Open Finance, só o handoff para o banco é regulado. A LGPD (consentimento livre, informado e inequívoco) continua valendo dentro do widget; variantes da tela de termos devem passar pelo jurídico.

## Perguntas ainda abertas

1. Divisão entre Open Finance e conectores diretos; lista de conectores e credenciais pedidas por cada um.
2. O que Login Step Success significa em cada trilho (no Open Finance, dispara antes ou depois do handoff?).
3. Entre os 15.570 da zona B, quanto é erro técnico, erro do usuário e abandono.
4. Com que frequência quem está no widget não é o titular ou não tem poderes na conta.
5. Com que frequência o consentimento PJ fica parado em múltiplas alçadas.

## Próxima tarefa: mapear o widget atual (requer Chrome)

Use a integração com o Chrome (`claude --chrome` ou `/chrome`).

1. Abrir https://demo-connect.pluggy.dev/ (aba React Pluggy Connect).
2. Em Connect Demo Settings, usar a URL https://connect.pluggy.ai e o cliente com label "marco". Eu preencho as credenciais; não peça nem grave o client secret em arquivos.
3. Gerar o connectToken e abrir o widget.
4. Percorrer o fluxo tela a tela, registrando: texto e elementos de cada tela, conectores disponíveis, trilho de cada um (Open Finance ou direto) e credenciais pedidas.
5. Não concluir conexões reais nem submeter credenciais.
6. Salvar o resultado em `docs/mapa-widget.md` e cruzar cada tela com as etapas do job, os outcomes e os eventos do funil.
7. Atualizar `docs/estudo-jtbd-widget.html` para a versão 0.3.

## Hipóteses candidatas de experimento

- H1: preparar o empresário antes do redirecionamento (O7, O8, O9; E1)
- H2: confirmação imediata e explícita no retorno (O11, O12; E5)
- H3 (proposta): checklist do que ter em mãos, incluindo poderes na conta (O4, O5; E2)
- H4 (proposta): resumo de permissões em linguagem simples (O1–O3; E3)
- H5 (proposta): recuperação específica por tipo de erro (O13; E2)
- H6 (proposta): mostrar como revogar na conclusão (O14, O15; E4)

Priorização: Oportunidade = Importância + máx(Importância − Satisfação, 0). Fontes: funil por etapa, micropesquisa no ponto de abandono, tickets e entrevistas. Segmentar por trilho, instituição, titular ou operador, dispositivo e cliente.
