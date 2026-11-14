#!/usr/bin/env python3
'''Repair daily/2026-11-07.md frontmatter (summary used a YAML double-quoted
scalar whose content contains triple-quote sequences) and the stale
projects/zero-breach-toolkit.html href in daily/2026-10-30.md.'''

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --- 1. daily/2026-11-07.md : summary -> folded block scalar -----------------
p = ROOT / "daily" / "2026-11-07.md"
text = p.read_text(encoding="utf-8")
parts = text.split("---", 2)
fm = parts[1]

new_fm = fm
m = re.search(r'^summary: "(.*)"\s*$', fm, re.M)
if m:
    body = m.group(1)
    # Block scalar cannot contain a line that is more-indented than the first
    # non-empty line; the summary is a single logical line, so indent by 2.
    folded = "summary: >-\n  " + body.replace("\n", " ") + "\n"
    new_fm = fm[: m.start()] + folded + fm[m.end() :]
    p.write_text("---" + new_fm + "---" + parts[2], encoding="utf-8")
    print("2026-11-07.md: summary converted to folded block scalar")
else:
    print("2026-11-07.md: summary line not matched (already fixed?)")

# --- 2. daily/2026-10-30.md : stale href ----------------------------------
q = ROOT / "daily" / "2026-10-30.md"
t2 = q.read_text(encoding="utf-8")
before = t2.count("projects/zero-breach-toolkit.html")
t2 = t2.replace("projects/zero-breach-toolkit.html", "projects/zero-breach.html")
q.write_text(t2, encoding="utf-8")
print(f"2026-10-30.md: href occurrences replaced {before}")

# --- 3. verify -------------------------------------------------------------
import yaml

for f in sorted((ROOT / "daily").glob("*.md")):
    c = f.read_text(encoding="utf-8")
    if not c.startswith("---"):
        print("!! no frontmatter:", f.name)
        continue
    pp = c.split("---", 2)
    try:
        meta = yaml.safe_load(pp[1]) or {}
    except Exception as e:  # noqa: BLE001
        print("!! YAML FAIL:", f.name, str(e)[:120])
        continue
    if not meta.get("summary"):
        print("!! no summary:", f.name)
print("frontmatter scan done")
