# Engenharia de agentes

## Objetivo
Transformar uma necessidade de negócio em agente com missão delimitada, competências observáveis e interfaces testáveis. Esta arquitetura é uma síntese operacional do Time Inteligente, não uma metodologia externa atribuída indevidamente.

## Sequência de raciocínio
1. **Produto e resultado:** qual problema o produto resolve e como se reconhece o resultado.
2. **Responsabilidade:** qual resultado específico pertence a cada agente.
3. **Autoridade:** o que decide, recomenda, executa, valida e escala.
4. **Competência:** o conhecimento e a capacidade necessários para cumprir a responsabilidade.
5. **Skill:** procedimento especializado e repetível para produzir uma entrega observável.
6. **Contrato:** quando e como outro agente recebe, verifica, aceita ou devolve a entrega.
7. **Teste:** evidência de que as regras funcionaram no ambiente realmente utilizado.

## Matriz de rastreabilidade
Para cada responsabilidade, registrar ID, origem da SOUL, competência, agente responsável, skill, entrada, saída, dependências, método especializado, evidência de qualidade, consumidor e cenário de teste.

### Limites
Uma SOUL não substitui uma skill; uma skill não concede acesso; uma documentação de contrato não instala integração. Nenhuma competência técnica deve ser atribuída por conveniência sem evidência, metodologia ou aprovação da ampliação de papel.

## Checklist de auditoria
- Existem responsabilidades sem competência?
- Existem skills sem responsabilidade explícita?
- Existem dois agentes com o mesmo poder de aprovação?
- O especialista consegue apresentar a evidência que o coordenador exige?
- As entradas do consumidor correspondem à saída do produtor?
- Uma alteração de SOUL exige atualizar skills e contratos?
