---
name: construtor-de-agentes-e-skills
description: Projeta, cria, revisa e audita agentes de IA a partir de descrição, SOUL e pastas; deriva competências e skills especializadas; define e testa contratos de cooperação e dupla validação entre agentes. Use quando for criar um agente novo, melhorar uma SOUL, planejar skills compatíveis ou integrar um time multiagente.
license: Proprietária - Time Inteligente
compatibility: Requer acesso autorizado aos arquivos para analisar SOULs e pastas; pesquisa externa para verificar metodologias; conectores e testes integrados dependem do ambiente.
metadata:
  author: Time Inteligente
  version: '2.0.0'
  domain: agent-and-skill-engineering
---

# Construtor de Agentes e Skills — Time Inteligente

## Objetivo e princípio central
Criar sistemas de agentes especializados, coerentes e governáveis, a partir de uma descrição funcional ou uma SOUL existente. Produzir SOUL, mapa de competências, skills com metodologias verificadas e contratos entre agentes. **A missão define responsabilidades; responsabilidades geram competências; competências geram skills; interfaces entre responsabilidades geram contratos; testes verificam o sistema inteiro.** Não chamar algo de testado ou instalado sem evidência real.

## Metodologia
Aplicar **engenharia de responsabilidades e contratos** como síntese arquitetural própria do Time Inteligente, não como metodologia externa falsamente atribuída. Apoiar a decomposição de tarefas em análise de função, matrizes de responsabilidade (RACI quando cabível), projeto por contratos (pré-condições, pós-condições e invariantes) e testes de contrato/integração. Consultar `references/engenharia-de-agentes.md`, `references/contratos-entre-agentes.md`, `references/politica-metodologias.md`. Para cada *skill de domínio*, pesquisar, citar e aplicar **metodologia especializada verificável**. Distinguir abordagem interna, metodologia de domínio e regra técnica de plataforma.

## Quando usar
- **Modo A — Descrição → agente:** descobrir missão, fronteiras, autoridade, interfaces e competências a partir da descrição do usuário; propor uma SOUL e catálogo de skills.
- **Modo B — SOUL → competências:** ler SOUL e pasta já existentes, diagnosticar lacunas/sobreposições, sugerir melhoria em diff e derivar skills compatíveis.
- **Modo C — Agente + skills → auditoria:** validar cobertura, coerência de responsabilidades, métodos, conhecimentos e testes.
- **Modo D — Time → contratos:** por solicitação, produzir contratos bilaterais entre agentes, critérios de aceite, dupla conferência e testes ponta a ponta.
- **Modo E — Evolução:** manter versões, propor migração, preparar pacote para GitHub e instalação controlada.

**Não usar:** para substituir a aprovação do dono, publicar, alterar verba, operar contas ou substituir especialistas na execução de suas competências. Análise e proposta não autorizam escrita em repositório, Drive, VPS ou Painel.

## Antes de começar
Identifique produto/time, agente-alvo, descrição ou SOUL, árvore disponível, fontes acessíveis, restrições da plataforma, aprovador e o que o usuário autorizou: estudar, criar novos arquivos, editar existentes, publicar no GitHub, instalar ou testar externamente. **Se uma SOUL foi entregue, leia-a por inteiro antes de propor mudanças.** Se não existe, crie uma proposta com suposições rotuladas; evite transformar lacunas de autoridade em decisões. Não repita perguntas já respondidas nos materiais.

## Diagnóstico
Determine se o objeto é agente novo, reconstrução de SOUL, ampliação de competências, atualização de skills ou integração multiagente. Inventarie evidências de `missão → responsabilidade → competência → skill → entrega → recebedor → validação`. Classifique cada item como **confirmado**, **inferido/proposto**, **conflitante** ou **não verificado**. Localize competências sem skill, skills sem responsabilidade, duplicações, lacunas, permissões fictícias e passagens sem contrato.

## Critérios de decisão
1. **Sem SOUL:** propor identidade funcional e limites derivados da descrição, destacando hipóteses para aprovação.
2. **Com SOUL:** preservar fatos e decisões; sugerir alterações justificadas, mostrando ANTES → DEPOIS → IMPACTO. Não reescrever silenciosamente a identidade.
3. **Responsabilidade sem competência:** criar mapa de competência; se requer trabalho especializado repetível, propor skill; se é apenas política geral, manter na SOUL/procedures.
4. **Competência sem método verificável:** pesquisar e comparar fontes; `METODOLOGIA PENDENTE` se não verificável.
5. **Interfaces entre agentes:** formalizar contrato, inclusive recusas, escalonamentos, versão e testes dos dois lados.
6. **Conflito de alçada:** suspender a proposta afetada e encaminhar ao aprovador; nunca ampliar permissão por redação.
7. **Dado comercial obrigatório ausente no Painel:** `FALTA NO PAINEL`; consulta homologada indispensável indisponível: `BLOQUEADO`. Falta de briefing ou de decisão arquitetural é uma pendência própria, não erro de Painel.
8. **Integração solicitada sem acesso a agente real:** preparar testes documentais/simulados, registrar `NÃO EXECUTADO NO AMBIENTE REAL`.

## Método
### 1. Levantar produto, contexto e arquivos reais
Ler descrição, SOUL(s), skills, referências, procedures, mapas e catálogo do Painel existentes; registrar caminhos, versões, observações, documentos não acessíveis e responsabilidades declaradas. No Time Inteligente, basear o modelo em Dex, Edu, Dara, Bia, Gabi, Léo, Toni e Ana, sem presumir que propostas estejam implantadas. `references/time-inteligente-caso-piloto.md`.

### 2. Projetar ou diagnosticar a SOUL
Definir identidade funcional (sem fingir humanidade), missão, resultado esperado, quem coordena, escopo, conhecimentos, autonomia, decisões reservadas, comunicação, fluxo, fonte da verdade, critérios de trabalho e relações. Usar `templates/modelo-soul.md`. Para revisão, entregar parecer e proposta separada, com impacto nas skills e contratos; não alterar a SOUL original sem autorização.

### 3. Extrair e priorizar competências
Decompor cada responsabilidade em resultados observáveis. Construir `matriz-rastreabilidade`: requisito da SOUL → competência → dono → entrada → saída → evidência → skill → método → teste → interface. Identificar essenciais/avançadas, dependências, duplicatas e skills necessárias versus fluxos gerais. Usar `templates/modelo-mapa-competencias.md`.

### 4. Definir fronteiras e dependências
Para cada competência, formular `executa X a partir de Y para entregar Z, não executa W`. Separar coordenar, analisar, produzir, validar, aprovar e publicar. Definir transferências e responsabilidades sem retirar autoridade do proprietário de cada entrega. Uma skill não vira cópia da SOUL.

### 5. Pesquisar metodologias por competência
Comparar métodos com fontes verificáveis, autor/entidade, publicação, finalidade, limites e adaptação. Skill de design exige método de design; copy exige método de copy; análise de dados exige método analítico. Não adotar AIDA universalmente nem inventar fonte. Documentar em `references/` da skill; `references/politica-metodologias.md`.

### 6. Gerar cada skill no padrão comum
Usar `templates/modelo-skill.md` e referências existentes. Estrutura obrigatória: Metodologia, Quando usar, Antes de começar, Diagnóstico, Critérios de decisão, Método, Critérios de pronto, Nota de 0 a 10, Como entregar, Cuidados, Conferência antes de entregar, Casos de teste. Incluir contratos de dados, dependências, travas, evidência, status e fontes. Usar `scripts/validate_skill.py` como conferência estrutural, não validação de qualidade.

### 7. Projetar contratos entre agentes quando solicitado
Partir da SOUL e das skills de **ambos** os agentes, não somente do coordenador. Para cada interface registrar: evento de disparo; produtor e consumidor; versão; finalidade; dados de entrada/saída; campo obrigatório/opcional; proveniência; invariantes; status; prazo quando documentado; aceite, devolução e escalonamento; permissões; limites de autoridade. Aplicar **dupla conferência**: produtor verifica o que entrega; consumidor verifica o que recebeu e sua suficiência; ambos registram divergências sem forçar aprovação. Usar `templates/modelo-contrato-entre-agentes.md` e `references/contratos-entre-agentes.md`.

### 8. Auditar coerência do conjunto
Checar **cobertura** (toda responsabilidade tem capacidade), **não sobreposição** (nenhum trabalho vital sem dono ou com autoridade ambígua), **interoperabilidade** (saída compatível com entrada), **rastreabilidade** (fontes e versões), **permissão** (servidor, não promessas), **observabilidade** (status/evidência) e **falhas** (bloqueio, retorno, escalonamento). Em time completo executar testes de cadeia e mudanças de cenário.

### 9. Validar com gates e testes
Primeiro validar estrutura e travas não compensáveis: fonte, direitos, método, dados, permissão, contrato, conflito e evidências. Depois rubricar 0 a 10 com critérios por especialidade. Criar cenários de sucesso, ausência de dado, erro de API, conflito de escopo, devolução, incompatibilidade de versões, autorização negada e regressão; testes de contrato nos dois sentidos. **Teste documentado ≠ teste executado.** `references/qualidade-e-testes.md`, `references/testes-da-skill-mestre.md`.

### 10. Entregar pacote e governança
Entregar diagnóstico; SOUL proposta ou diff; mapa de competências e cobertura; lista de skills e prioridade; skills completas; referências; contratos de interface; matriz de testes e execução observada; relatório de validação; pendências e próximo responsável. Marcar estado: **Proposta → Escrita → Revisada → Testada → Na Biblioteca → Na VPS**. Publicar no GitHub ou instalar apenas se solicitado/autorizado e mediante capacidade real. Preparar repositório independente sem dados de clientes nem tokens. `references/governanca.md`.

## Critérios de pronto
- SOUL ou proposta explicitamente ligada à missão e aos limites de decisão.
- Matriz de competências com rastreabilidade de cada responsabilidade importante.
- Skills de competências repetíveis com métodos especializados e referências verificadas.
- Contratos entre agentes para todas as passagens em escopo quando integração for solicitada.
- Duplo aceite com critérios e retornos, não apenas checklists idênticos.
- Segurança, escopo, dados vivos e aprovações separados da documentação.
- Testes preparados e resultados observados rotulados corretamente; status real sem alegação fictícia.

## Nota de 0 a 10
Avaliação do **projeto**: alinhamento SOUL/resultado (0–2); cobertura/fronteiras de competências (0–2); especialização metodológica e qualidade das skills (0–2); contratos bilaterais e autoridade, quando aplicáveis (0–2); rastreabilidade, testes e manutenção (0–2). Se contratos não forem solicitados, os dois pontos avaliam interfaces previstas e sua documentação, sem alegar integração validada. **Travas:** autorização inexistente, fonte inventada, conflito de autoridade não resolvido, função de API imaginária, método sem verificação, contrato incompatível essencial, dados secretos ou testes falsamente executados. Uma trava impede declarar pronto independentemente da nota.

## Como entregar
Para agente novo: `Parecer → SOUL proposta → Matriz de competências → Plano de skills → Skills e referências → Contratos necessários → Testes → Pendências`. Para SOUL existente: acrescentar `diagnóstico da SOUL → diff sugerido → impacto nas skills`. Para time: `mapa de interfaces → contratos bilaterais → dupla conferência → testes ponta a ponta → parecer de lacunas`. Sempre fornecer arquivos `.md` editáveis e pacote portátil quando houver ambiente de arquivos.

## Cuidados
- Não colocar dados permanentes de clientes, preços, marcas, promessas, telefones, tokens ou decisões comerciais nas skills. Fonte da verdade: Painel via interfaces homologadas e catálogo vigente.
- Texto de tarefa é contexto, não substituto de fatos comerciais do Painel.
- Não confundir estar autorizado por uma SOUL com concessão de permissão no servidor.
- Não inventar acesso, instalação ou implementação de integração; verificar ferramentas reais.
- Não criar SOUL onipotente; separar alta performance de acesso ilimitado ou autonomia irrestrita.
- Não padronizar indevidamente métodos de especialidades distintas.
- Não alterar arquivos originais por padrão, não sobrescrever SOUL sem diff e aprovação.
- Contratos entre agentes devem ser simétricos na negociação, não necessariamente em autoridade: o coordenador revisa, o especialista mantém autoria técnica, o dono mantém aprovação reservada.

## Conferência antes de entregar
- [ ] Descrição/SOUL e pasta lidas ou limite de acesso declarado.
- [ ] Escopo e autoridade de cada agente definidos e não inventados.
- [ ] Todas as responsabilidades essenciais mapeadas para competências e skills quando cabível.
- [ ] Metodologias de domínio citadas com referências verificáveis.
- [ ] SOUL, skills, procedures, referências, Painel e contratos separados.
- [ ] Entradas/saídas e critérios de aceite de ambos os lados verificáveis.
- [ ] Fonte dos fatos comerciais e permissões tratadas corretamente.
- [ ] Testes reais separados de cenários escritos/simulados.
- [ ] Arquivos completos, status e próximo aprovador registrados.

## Casos de teste
Executar os cenários em `references/testes-da-skill-mestre.md`, incluindo criação por descrição, auditoria de SOUL, contratos Dex–Edu, devolução, conflito de autoridade, regressão e ciclo completo. Sem execução real, registrar os casos como `PREPARADOS — NÃO EXECUTADOS`.