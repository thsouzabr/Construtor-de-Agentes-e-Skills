# Auditoria diagnóstica de contratos entre agentes

## Princípio
**O contrato é somente um dos entregáveis.** Nunca encerrar o trabalho informando apenas que o Markdown foi criado. É obrigatório apresentar na resposta ao usuário um parecer crítico, com evidências, lacunas e melhorias; anexar o diagnóstico em arquivo separado.

## 1. Conferir o material real
Ler SOUL de cada participante, skills produtoras e consumidoras, competências, métodos, referências, contratos anteriores, fluxos, critérios de aceite e objetivo do time. Identificar versão, estado e o que não foi acessado. Se não existe evidência, classificar HIPÓTESE ou NÃO VERIFICADO, sem inventar avaliação factual.

## 2. Auditar cada agente
- **Produtor:** domínio especializado, responsabilidade, método, critérios de pronto, entradas, saídas, riscos e evidência de qualidade.
- **Consumidor/coordenador:** resultado que deve validar, conhecimento mínimo para entender e questionar a especialidade, critérios de aceitação, skill ou referência de revisão, risco de aceitar algo sem avaliação.
- **Autoridades:** separar executar, coordenar, revisar, decidir e aprovar; não estender permissões.
- **Lacunas e conflitos:** conhecimentos ausentes, responsabilidades órfãs, skills duplicadas, método não comprovado, documentos incompatíveis.

**Conhecimento necessário para validar não é o mesmo que conhecimento necessário para executar.** O coordenador deve reconhecer problemas, exigir evidências, verificar estratégia e encaminhar revisão técnica; não se tornar autor da especialidade.

## 3. Auditar o contrato
Examinar o encaixe entre saída e entrada: evento, campos, fonte, versão, formato, prazo apenas quando real, aceite, devolução, bloqueio, aprovação externa, dependências e evidência. Aplicar a conferência técnica do produtor e a conferência de suficiência do consumidor, separadamente.

## 4. Entregar diagnóstico bilateral, antes do contrato ou junto dele
Sempre incluir no corpo da resposta, e em arquivo:
1. **O que está bom:** observação, fonte, por que preservar.
2. **O que está ruim/insuficiente:** problema, impacto e gravidade.
3. **O que não foi comprovado:** fontes, integrações e testes indisponíveis.
4. **Lacunas por agente:** conhecimento, competência, skill ou contrato faltante; evidência; risco; hipótese quando aplicável.
5. **Melhorias recomendadas:** mudança específica, justificativa, prioridade, local de implementação (SOUL, skill existente, referência, procedimento, contrato), responsável e teste de aceitação.
6. **Decisão:** pronto para revisão, não pronto ou homologado com evidência; próximos passos, dependências e aprovações.

Não basta dizer "salvei diagnóstico". Mostrar conclusões úteis na conversa. Se não houver lacuna, justificar com verificações realizadas; não inventar problemas.

## 5. Priorização
- **P0:** conflito grave de alçada, segurança, autorização ou incompatibilidade que impede aceite confiável.
- **P1:** falta de conhecimento/revisão ou competência que prejudica qualidade operacional.
- **P2:** refinamento, clareza, manutenção e eficiência sem bloqueio imediato.

Cada recomendação deve responder **o que, por quê, onde, quem aprova e como testar**. Verificar se skill existente pode ser aprimorada antes de recomendar criação de outra.

## 6. Exemplo orientador: Dara ↔ Dex (hipótese, não auditoria real)
Dara produz copy de marketing, vendas e institucional. Dex coordena e precisa julgar adequação ao objetivo, ao posicionamento, ao público e ao processo comercial, sem redigir em seu lugar.

Investigar se a SOUL/skills do Dex já cobrem conhecimentos de: posicionamento e proposta de valor; objetivo e estágio do funil; público e nível de consciência; clareza, CTA e objeções; evidências/prova social; afirmações e promessas permitidas; critérios distintos para copy de anúncio, página e institucional. Consultar primeiro a skill `revisar-entrega` do Dex. Se insuficiente, recomendar complemento metodológico e checklist por tipo de peça, não criar duplicação automaticamente.

Investigar se a Dara entrega briefing, peça, objetivo, fontes, versão, justificativa do ângulo, ressalvas e evidências suficientes ao Dex. Se faltarem, propor ajuste da skill de Dara e do contrato.

## 7. Matriz mínima
| Passagem | Requisito do consumidor | Evidência produzida | Conhecimento do revisor | Estado | Risco | Correção |
|---|---|---|---|---|---|---|
| Dara → Dex | Copy coerente com objetivo e oferta vigente | Texto, briefing, fontes, versão | Avaliação de copy e negócio | A verificar | Aceite superficial | Auditar revisão do Dex |

## Gate final
**Contrato pronto para revisão:** há diagnóstico bilateral (resposta e arquivo), matriz de competências, análise de compatibilidade, recomendações, status, fontes e testes preparados. **Não pronto:** falha essencial ou revisor sem capacidade suficiente. **Homologado:** somente após evidência de testes integrados e aprovações. Arquivo MD criado sozinho nunca satisfaz o gate.
