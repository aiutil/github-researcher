#!/usr/bin/env python3
'''Set the corrected stars value for projects/zero-breach.md (upstream repo).'''

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "projects" / "zero-breach.md"
lines = p.read_text(encoding="utf-8").split("\n")
for i, ln in enumerate(lines):
    if ln.startswith('stars: "4,475 stars"'):
        lines[i] = 'stars: "1,218 stars"'
        print(f"stars field updated at line {i + 1}")
        break
else:
    raise SystemExit("stars field not found")
p.write_text("\n".join(lines), encoding="utf-8")

import yaml

m = yaml.safe_load("\n".join(lines).join(["---", "---"]).split("---", 2)[1]) if False else yaml.safe_load(
    p.read_text(encoding="utf-8").split("---", 2)[1]
)
print("YAML OK:", m["title"], "|", m["stars"], "|", m["url"])
