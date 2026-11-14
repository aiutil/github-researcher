#!/usr/bin/env python3
'''Convert the over-long stars_delta in projects/zero-breach.md into a folded
block scalar so the YAML parses (the value contains ": " sequences).'''

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "projects" / "zero-breach.md"
lines = p.read_text(encoding="utf-8").split("\n")

for i, ln in enumerate(lines):
    if ln.startswith("stars_delta:"):
        value = ln[len("stars_delta:"):].strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        # Unescape the doubled backslashes that came from the Python literal.
        value = value.replace("\\\\", "\\")
        lines[i:i + 1] = ["stars_delta: >-", "  " + value]
        print(f"converted stars_delta to folded block scalar at line {i + 1}")
        break
else:
    raise SystemExit("stars_delta not found")

p.write_text("\n".join(lines), encoding="utf-8")

import yaml

meta = yaml.safe_load("\n".join(lines).join(["---", "---"]).split("---", 2)[1])
print("YAML OK:", meta["title"], "|", meta["stars"], "|", meta["url"])
print("stars_delta head:", meta["stars_delta"][:120])
