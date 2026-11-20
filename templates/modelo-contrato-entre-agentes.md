---
tipo: contrato-entre-agentes
id: CONTRATO-001
versao: 0.1.0
status: proposta
produtor: AGENTE_ORIGEM
consumidor: AGENTE_DESTINO
---

# Contrato — [Origem] → [Destino]

## Finalidade e acionamento
Quando a passagem ocorre e qual resultado atende.

## Autoridades
O que o produtor pode decidir; o que o consumidor pode decidir; quais atos exigem aprovação superior.

## Entrada do produtor
| Campo | Obrigatório | Origem confiável | Critério |
|---|---|---|---|
| identificador_da_tarefa | sim | [sistema] | [validação] |

## Saída para o consumidor
| Campo | Obrigatório | Formato | Evidência | Critério de aceite |
|---|---|---|---|---|
| recomendacao | sim | texto | [fonte] | justificativa verificável |

## Porta 1 — Conferência do produtor
- [ ] Método especializado aplicado.
- [ ] Dados rastreáveis e versão registrada.
- [ ] Limites da SOUL respeitados.
- [ ] Campos obrigatórios presentes.

## Porta 2 — Conferência do consumidor
- [ ] Objetivo do pedido atendido.
- [ ] Entrega tecnicamente suficiente para a próxima decisão.
- [ ] Dependências e ressalvas explícitas.
- [ ] Resultado registrado como aceito, devolvido ou bloqueado.

## Porta 3 — Autorizações reservadas
Quais ações requerem aprovação humana e como essa aprovação será comprovada.

## Devolução, bloqueio e escalonamento
Motivos possíveis, campos de retorno, responsável pela correção e regras contra aprovação tácita.

## Compatibilidade, versão e testes
Casos positivo, negativo, ausência de fonte, incompatibilidade de versão, mudança de SOUL e regressão. Registrar execução real separadamente.
