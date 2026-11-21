# Contrato arquitetural

## Fronteiras

| Componente | Contém | Não contém |
|---|---|---|
| SOUL | identidade, missão, alçada, responsabilidades, postura e limites | método completo de execução de cada tarefa |
| Skill | competência operacional, decisão, passos, entradas e critérios de qualidade | dados fixos de clientes ou concessão de privilégios |
| Referências | metodologia verificável, exemplos, normas, especificações e modelos | segredos ou regras de cliente não vigentes |
| Procedimentos | fluxos transversais e rotinas operacionais | cópia de todas as skills |
| Painel | dados vivos, autorizações e regras vigentes de clientes | conhecimento geral reutilizável |
| Contrato | interface, aceite, rejeição e rastreabilidade entre agentes | poder de aprovação inexistente |

## Estrutura obrigatória de SKILL.md
Metodologia; Quando usar; Antes de começar; Diagnóstico; Critérios de decisão; Método; Critérios de pronto; Nota de 0 a 10; Como entregar; Cuidados; Conferência antes de entregar; Casos de teste.

## Decisão de criar skill
Criar quando houver competência repetível com entradas, decisão, método e entrega própria. Não criar uma skill apenas para repetir uma orientação de identidade ou uma política de acesso.

## Versionamento
Qualquer revisão de SOUL deve registrar impacto nas skills e contratos. Mudanças de campos obrigatórios nos contratos exigem teste de compatibilidade e controle de versão.

## Regra de separação SOUL × skill — atualização 2.3

A SOUL contém identidade funcional, missão, responsabilidades, alçada, postura, limites e interfaces. Uma referência breve à área de atuação pode delimitar o papel, mas **não deve conter fundamentos ou instruções técnicas detalhadas**.

HTML, CSS, JavaScript, UX/UI, SEO técnico, acessibilidade, microdados, linguagens e frameworks são conhecimentos e habilidades operacionais: documentar em **skills** e suas **referências**. Fluxos compartilhados ficam nos procedimentos; dados vivos dos clientes, no Painel.

**Exemplo válido na SOUL da Bia:** “Sou responsável por entregar páginas acessíveis e tecnicamente conformes, utilizando skills de implementação, auditoria e otimização.”

**Exemplo inválido na SOUL:** “Fundamentos de HTML: tags semânticas e atributos; fundamentos de CSS: seletores e flexbox; fundamentos de JavaScript: DOM e eventos”. Mover para skills e referências, apresentando o impacto e pedindo aprovação antes de alterar a SOUL original.

