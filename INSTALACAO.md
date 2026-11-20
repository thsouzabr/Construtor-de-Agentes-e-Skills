# Instalação, atualização e versionamento

## GitHub — repositório fonte
1. Crie repositório privado inicialmente, por exemplo `thsouzabr/construtor-de-agentes-e-skills` (repositório exclusivo, a ser criado).
2. Envie todo o conteúdo desta pasta, preservando `SKILL.md`, `references/`, `templates/`, `scripts/` e `chatgpt/`.
3. Revise `git diff` antes do commit; não inclua dados de clientes, segredos, credenciais, snapshots do Painel ou material confidencial sem licença.
4. Marque versões por tag (ex.: `v2.0.0`) somente após revisão. A cada mudança na SOUL ou skill do time, rodar análise de impacto nos contratos.

```bash
git init
git add .
git commit -m "feat: construtor de agentes e skills v2"
# git remote add origin URL-REAL-DO-SEU-REPOSITORIO
# git push -u origin main
```

## Claude Code
Coloque a pasta do pacote em `.claude/skills/construtor-de-agentes-e-skills/` do projeto ou outro diretório de skills suportado pela sua instalação. Reinicie/recarregue o contexto conforme necessário; solicite: `Use a skill construtor-de-agentes-e-skills para revisar a SOUL do Edu e criar contrato com Dex`. Confirmar reconhecimento na instalação real.

## Claude.ai
Caso sua conta exponha importação de skills personalizadas, importe o ZIP sem remover a pasta raiz. Verifique a ativação em um teste simples. Recursos e localização da opção podem variar.

## ChatGPT
O ZIP não instala automaticamente um GPT. Crie uma área/projeto/agente personalizado disponível na sua conta; copie `chatgpt/INSTRUCOES-AGENTE-CHATGPT.md` para as instruções e anexe como conhecimento `SKILL.md`, `references/` e `templates/` quando o recurso permitir. Conecte Drive ou GitHub somente mediante autorização, verificando escopo. Quando a configuração não aceitar pastas, envie os arquivos separadamente ou o ZIP quando o produto oferecer leitura dele. O agente deve sempre reler fontes atualizadas.

## Validação local
```bash
python scripts/validate_package.py .
python scripts/validate_skill.py CAMINHO-DE-UMA-SKILL-GERADA
```
O sucesso técnico significa somente presença e ligações locais válidas, não execução real ou qualidade do método. Testar no Hermes/ChatGPT/Claude antes de declarar homologado.

## Governança Time Inteligente
A oficina prepara e revisa; a Biblioteca oficial distribui após aprovação; a VPS recebe apenas versão autorizada. Não mudar SOULs ou skills instaladas apenas por haver uma versão nova no GitHub. Executar teste de compatibilidade dos contratos e garantir rollback.

Consulte também `PUBLICACAO-GITHUB.md` para instruções específicas da conta e envio.