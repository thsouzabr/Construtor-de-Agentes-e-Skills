#!/usr/bin/env python3
"""Validador estrutural conservador de Agent Skills (sem dependências externas)."""
import re
import sys
import pathlib
import json

REQUIRED = [
    "Metodologia", "Quando usar", "Antes de começar", "Diagnóstico",
    "Critérios de decisão", "Método", "Critérios de pronto",
    "Nota de 0 a 10", "Como entregar", "Cuidados",
    "Conferência antes de entregar", "Casos de teste",
]


def run(root):
    root = pathlib.Path(root)
    path = root / "SKILL.md"
    issues, warnings = [], []
    if not path.is_file():
        return {"ok": False, "errors": ["SKILL.md ausente"], "warnings": []}
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        issues.append("Frontmatter YAML ausente ou mal delimitado")
    else:
        meta = m.group(1)
        for k in ["name", "description"]:
            if not re.search(rf"(?m)^{k}:\s*\S+", meta):
                issues.append(f"Metadado obrigatório ausente: {k}")
        n = re.search(r"(?m)^name:\s*(.+?)\s*$", meta)
        if n and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", n.group(1).strip()):
            issues.append("name deve ser slug minúsculo")
    heads = {
        re.sub(r"\s+", " ", x).strip().casefold()
        for x in re.findall(r"^##\s+(.+)$", text, re.M)
    }
    for sec in REQUIRED:
        if sec.casefold() not in heads:
            issues.append(f"Seção ausente: {sec}")
    for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"(?i)https?://|mailto:", ref) or ref.startswith("#"):
            continue
        target = (root / ref.split("#")[0]).resolve()
        if not target.is_relative_to(root.resolve()):
            issues.append(f"Link fora da raiz: {ref}")
        elif not target.exists():
            issues.append(f"Link local inexistente: {ref}")
    if not (root / "references").exists():
        warnings.append("Sem diretório references; justificar se skill simples")
    if "NÃO EXECUTADO" not in text and "casos-de-teste.md" not in text:
        warnings.append("Verificar se a existência de testes não foi confundida com execução")
    return {"ok": not issues, "errors": issues, "warnings": warnings, "path": str(root)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_skill.py /caminho/da/skill")
        sys.exit(2)
    r = run(sys.argv[1])
    print(json.dumps(r, ensure_ascii=False, indent=2))
    sys.exit(0 if r["ok"] else 1)
