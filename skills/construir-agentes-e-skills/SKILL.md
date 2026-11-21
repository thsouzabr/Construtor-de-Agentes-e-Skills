---
name: construir-agentes-e-skills
description: Analise uma descrição, pasta ou SOUL para construir ou melhorar um agente, derivar skills especializadas e preparar contratos bilaterais com dupla conferência.
---

# Construir agentes e skills

Este comando aciona o **Construtor de Agentes e Skills**. A especificação-mestre completa está no arquivo `SKILL.md` da raiz do mesmo plugin. Leia-o antes de iniciar, juntamente com as referências pertinentes em `references/`.

## Quando usar

Use para criar agentes a partir de uma descrição; auditar ou reescrever uma SOUL como proposta; decompor responsabilidades em skills; avaliar a biblioteca de competências; criar contratos entre agentes e seus testes.

## Instruções
1. Leia a SOUL ou o contexto fornecido, sem assumir acesso àquilo que não foi consultado.
2. Identifique responsabilidades, autonomia, limites, interfaces e competências.
3. Gere proposta de SOUL, matriz de competências e skills especializadas seguindo os modelos em `templates/`.
4. Cada skill deve usar metodologia relevante e verificável, não modelos genéricos aplicados a todas as áreas.
5. Quando solicitado, gere contratos de produtor-consumidor com critérios de aceite, devolução, validação dupla e aprovação superior separada.
6. Se o usuário pedir uma auditoria, faça relatório de lacunas, duplicidade, riscos, integração e testes.
7. Use português e informe claramente o que foi revisado, o que foi criado e o que ainda precisa ser testado.

## Verificações
- Nunca inventar fatos de clientes, fontes, dados de API, permissões nem resultados.
- Não alterar SOULs e skills vigentes ou outros projetos sem autorização.
- Manter conhecimento reutilizável separado dos dados vivos do Painel.
- Não confundir conformidade documental com homologação real.

## Materiais de referência
- `SKILL.md`
- `references/engenharia-de-agentes.md`
- `references/contratos-entre-agentes.md`
- `references/politica-metodologias.md`
- `references/qualidade-e-testes.md`
- `references/time-inteligente-caso-piloto.md`
