# Instalação, atualização e versionamento

Este manual explica como instalar ou consultar o **Construtor de Agentes e Skills** a partir do repositório público oficial:

**https://github.com/thsouzabr/Construtor-de-Agentes-e-Skills**

A publicação dos arquivos não instala automaticamente o agente em nenhum serviço.

## 1. Baixar os arquivos

No GitHub, abra o repositório, clique em **Code** e selecione **Download ZIP**. Extraia o conteúdo no computador. Para quem utiliza Git:

```bash
git clone https://github.com/thsouzabr/Construtor-de-Agentes-e-Skills.git
cd Construtor-de-Agentes-e-Skills
```

Todos os arquivos de orientação foram escritos em português. Nomes de campos padronizados, caminhos técnicos e sintaxe de programação foram preservados para garantir compatibilidade.

## 2. Usar no ChatGPT

Crie um espaço de trabalho ou agente configurável, conforme os recursos disponíveis na conta. Utilize o conteúdo de `chatgpt/INSTRUCOES-AGENTE-CHATGPT.md` como instrução persistente. Acrescente `SKILL.md`, a pasta `references/` e a pasta `templates/` ao material de conhecimento quando a plataforma permitir.

Quando usar arquivos do GitHub como referência, peça que o agente consulte a versão atual antes de revisar ou criar novas skills. O acesso a pastas privadas, Drive e Painel exige conexões e permissões próprias. Não presuma que a conexão esteja habilitada.

## 3. Usar no Claude Code

Copie a pasta para um diretório de skills suportado pelo seu ambiente, por exemplo:

```text
.claude/skills/construtor-de-agentes-e-skills/
  SKILL.md
  references/
  templates/
  scripts/
```

Peça: «Use a skill construtor-de-agentes-e-skills para analisar a SOUL do Edu e propor um contrato com Dex». Verifique que a instalação reconheceu a skill antes de considerar a configuração concluída.

## 4. Usar no Claude.ai

Caso a conta ofereça importação de skills personalizadas, compacte a pasta que contém `SKILL.md` e os arquivos de apoio e importe o ZIP. A disponibilidade e a localização dessa opção podem variar.

## 5. Executar uma solicitação

Exemplo:

> Leia a SOUL do agente informado, identifique responsabilidades e competências, proponha melhorias, crie as skills necessárias com metodologias especializadas e prepare contratos de integração. Não altere os originais sem autorização. Identifique cada evidência e o que ainda não foi verificado.

## 6. Validar localmente

Requer Python 3.11 ou superior.

```bash
python scripts/validate_package.py .
python scripts/validate_skill.py CAMINHO-DA-SKILL-GERADA
```

A validação confirma estrutura e referências locais. **Não confirma qualidade especializada, conexão com APIs, integração entre agentes ou homologação.** O workflow do GitHub Actions repete a validação estrutural a cada envio de alterações.

## 7. Atualizar em colaboração com o sócio

Abra uma branch, explique as alterações, avalie o impacto sobre SOULs, skills e contratos, execute os testes e envie um Pull Request para revisão. Consulte `COMO-COLABORAR.md`.

## 8. Segurança e publicação pública

Este repositório é **público**. Não envie segredos, tokens, credenciais, dados de clientes, capturas do Painel ou documentação operacional sensível. Os exemplos devem utilizar informações fictícias rotuladas.

O projeto identifica sua licença como **proprietária**: disponibilizar o código publicamente não autoriza automaticamente redistribuição ou uso comercial por terceiros. Antes de ampliar a colaboração pública, escolha com o sócio a licença apropriada.

## 9. Governança do Time Inteligente

A oficina prepara e revisa. A Biblioteca oficial distribui versões aprovadas. A VPS recebe apenas a versão autorizada. Uma atualização no GitHub não altera por si só as SOULs ou skills instaladas. Toda mudança de contrato exige análise de impacto e teste de regressão.


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
