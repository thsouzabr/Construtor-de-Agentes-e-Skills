# Construtor de Agentes e Skills

**Ferramenta de engenharia de agentes de IA, SOULs, competências, skills e contratos entre agentes.**

Este projeto foi desenvolvido para o **Time Inteligente** e pode servir como base para outros produtos e equipes especializadas. Ele organiza a criação de agentes de forma rastreável, modular e testável.

## O que ele faz

1. **Cria um agente a partir de uma descrição:** identifica missão, responsabilidades, limites, autonomia e entregas e propõe uma SOUL.
2. **Analisa uma SOUL existente:** encontra lacunas, conflitos, competências sem skill e oportunidades de melhoria, sem alterar o original automaticamente.
3. **Constrói skills especializadas:** pesquisa metodologias verificáveis, define quando usar, pré-condições, diagnóstico, critérios de decisão, execução e qualidade.
4. **Integra agentes:** estabelece contratos de passagem, campos de entrada e saída, responsabilidades, aceite, devolução e dupla conferência.
5. **Audita equipes:** verifica cobertura das competências, riscos de sobreposição, dependências, qualidade das fontes e testes.

## Por onde começar

Leia primeiro [a skill-mestre](SKILL.md) e depois [o manual de instalação](INSTALACAO.md). Para usar no ChatGPT, consulte [as instruções do agente](chatgpt/INSTRUCOES-AGENTE-CHATGPT.md). Os arquivos de `templates/` são modelos editáveis. As regras de arquitetura e governança estão em `references/`.

### Exemplo prático

> Analise as SOULs do Dex e do Edu, liste as competências necessárias de cada um, compare as skills existentes e proponha um contrato de entrega entre eles. Faça a conferência do produtor e a conferência do coordenador, com critérios e casos de devolução. Não altere os arquivos originais.

### Resultado esperado

- Diagnóstico fundamentado nas fontes realmente acessadas.
- SOUL proposta ou revisão documentada com justificativa.
- Matriz de competências e rastreabilidade.
- Skills com metodologia própria e referências verificáveis.
- Contratos bilaterais entre agentes e testes preparados.
- Relatório claro do que foi validado e do que ainda precisa de homologação.

## Organização

```text
SKILL.md
README.md
INSTALACAO.md
chatgpt/
references/
templates/
scripts/
.github/workflows/
```

## Segurança e fonte da verdade

**Não coloque neste repositório tokens, credenciais, dados de clientes, preços, informações pessoais ou configurações privadas.** No Time Inteligente, o Painel é a fonte de fatos empresariais vivos. O repositório contém apenas modelos e princípios de engenharia.

Uma metodologia escrita não comprova sua execução. Um contrato documentado não comprova integração real. **Publicação no GitHub não equivale à instalação ou homologação nos agentes.**

## Como colaborar

Leia [COMO-COLABORAR.md](COMO-COLABORAR.md). Mudanças devem preservar a separação entre identidade (SOUL), competência (skill), conhecimento (referências), procedimentos e dados vivos (Painel).

## Situação

**Versão 2.0.0 — biblioteca inicial para revisão.** A estrutura foi validada documentalmente; a integração com agentes reais ainda requer testes e aprovação. O conteúdo é disponibilizado publicamente para leitura e colaboração autorizada. A publicação não concede automaticamente licença de reutilização comercial ou redistribuição.


## Instalação rápida no Claude Code

O repositório também é um **plugin do Claude Code**: ele contém a skill, o agente especializado e um catálogo de instalação. Com o Claude Code instalado, execute no **terminal**:

```bash
claude plugin marketplace add thsouzabr/Construtor-de-Agentes-e-Skills
claude plugin install construtor-de-agentes-e-skills@time-inteligente
```

Na interface interativa do Claude Code, a alternativa é:

```text
/plugin marketplace add thsouzabr/Construtor-de-Agentes-e-Skills
/plugin install construtor-de-agentes-e-skills@time-inteligente
```

Depois, abra uma sessão e invoque a skill:

```text
/construtor-de-agentes-e-skills:construir-agentes-e-skills
```

Também pode pedir: **«Use o agente arquiteto-de-agentes-e-skills para analisar a SOUL do Dex, a do Edu e revisar o contrato entre eles».**

Para verificar:

```bash
claude plugin list
claude plugin details construtor-de-agentes-e-skills
```

A instalação depende de uma versão compatível do Claude Code e de acesso ao GitHub. **A publicação do plugin foi preparada, mas a instalação efetiva ainda precisa ser testada no seu computador.**

## Uso no ChatGPT

Um GPT ou agente personalizado no ChatGPT **não é instalado por esses comandos do Claude Code**. O arquivo [INSTRUCOES-AGENTE-CHATGPT.md](chatgpt/INSTRUCOES-AGENTE-CHATGPT.md) permanece como configuração reutilizável: copie-o para as instruções do agente e anexe os arquivos de conhecimento conforme os recursos da sua conta. Para automatizar a criação programática de agentes, seria necessário um fluxo suportado pela plataforma/API, separado da interface de criação manual do ChatGPT.
