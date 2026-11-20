# Contratos entre agentes e dupla conferência

Um contrato é uma interface operacional bilateral. Deve ser derivado das SOULs e das skills reais de **produtor e consumidor**, não apenas de um dos lados.

## Campos obrigatórios
- Identificador, versão e agentes envolvidos.
- Evento de acionamento e finalidade.
- Responsabilidade e autoridade de cada agente.
- Entradas obrigatórias, opcionais, formato, fonte e versão dos dados.
- Saída esperada: campos, critérios de pronto, evidência e restrições.
- Condições de aceite, devolução, correção, bloqueio e escalonamento.
- Limites da ferramenta, permissões e aprovações reservadas.
- Cenários de compatibilidade, exceção, regressão e documentação dos resultados.

## Portas de controle
**Porta 1 — Produtor:** especialista verifica método, dados, escopo, segurança, conclusão e rastreabilidade da entrega.

**Porta 2 — Consumidor:** coordenador ou recebedor verifica adequação ao objetivo, completude, coerência, formato e evidência; pode aceitar, devolver com motivo ou bloquear.

**Porta 3 — Autoridade externa:** quando o ato implica publicar, alterar oferta, gastar, ativar anúncio ou alterar regra permanente, a aprovação do responsável continua obrigatória. Duas conferências não substituem esse consentimento.

## Invariantes
Não alterar dados da entrega após aceite sem versionamento. Não declarar execução sem evidência. Não tratar ausência de dados como aprovação. Não presumir que o consumidor substitui o parecer técnico do especialista.

## Exemplo Dex ↔ Edu
Dex fornece objetivo e contexto confirmado. Edu devolve diagnóstico, evidências, alternativas, diretriz, riscos e critérios de verificação. Edu revisa qualidade estratégica; Dex revisa pertinência gerencial. Se faltarem evidências ou objetivo verificável, há devolução fundamentada.
