# Qualidade, validação e testes

## Duas avaliações independentes

**Gates obrigatórios:** a skill não está pronta se falta fonte verificável, método, autorização, dado obrigatório, contrato essencial, delimitação de competência ou se contém segredo. Nenhuma nota alta compensa uma trava.

**Nota de qualidade (0 a 10):** utilizar rubrica própria da especialidade com critérios verificáveis e escala descrita. Evitar pesos universais quando não representam o risco da tarefa.

## Testes mínimos
1. Caso completo com dados e autorização.
2. Caso sem informação indispensável.
3. Pedido fora do escopo.
4. Fonte ou permissão indisponível.
5. Inconsistência do dado ou da evidência.
6. Integração: entrega aceita, devolvida e bloqueada.
7. Regressão: alteração de SOUL ou contrato que repercute nas skills.

## Estados
- **PREPARADO:** existe roteiro.
- **SIMULADO:** cenário executado sem sistemas reais.
- **EXECUTADO:** há evidência de execução no ambiente alvo.
- **HOMOLOGADO:** houve revisão e aprovação definidas na governança.

Nunca confundir testes preparados com testes executados. Guardar entrada, saída, versão, resultado esperado, resultado observado, evidência e responsável pela aprovação.
