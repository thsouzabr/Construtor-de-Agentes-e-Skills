#!/usr/bin/env python3
"""Validação estrutural simples do pacote mestre; não é teste integrado."""
from pathlib import Path
import re
import sys
import json

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
required = [
    "SKILL.md",
    "README.md",
    "INSTALACAO.md",
    "references/engenharia-de-agentes.md",
    "references/contratos-entre-agentes.md",
    "references/time-inteligente-caso-piloto.md",
    "templates/modelo-soul.md",
    "templates/modelo-mapa-competencias.md",
    "templates/modelo-contrato-entre-agentes.md",
    "chatgpt/INSTRUCOES-AGENTE-CHATGPT.md",
]
errors = []
for f in required:
    if not (root / f).is_file():
        errors.append(f"Ausente: {f}")
for p in root.rglob("*.md"):
    t = p.read_text(encoding="utf8")
    for ref in re.findall(r"\[[^\]]+\]\(([^)]+)\)", t):
        if re.match(r"^(?:https?://|mailto:|#)", ref):
            continue
        if p.relative_to(root).parts[0] == "templates":
            continue
        target = (p.parent / ref.split("#")[0]).resolve()
        if not target.is_relative_to(root) or not target.exists():
            errors.append(f"{p.relative_to(root)}: link inválido {ref}")
r = {"ok": not errors, "files": len(list(root.rglob("*"))), "errors": errors}
print(json.dumps(r, ensure_ascii=False, indent=2))
sys.exit(0 if not errors else 1)
