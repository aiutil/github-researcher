#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def scan_and_fix(path):
    c = path.read_text(encoding="utf-8")
    if not c.startswith("---"):
        return "no-frontmatter"
    parts = c.split("---", 2)
    try:
        yaml.safe_load(parts[1])
        return "ok"
    except Exception:
        pass

    lines = parts[1].split("\n")
    out = []
    changed = 0
    for ln in lines:
        m = re.match(r'^(\s*)([A-Za-z_][A-Za-z0-9_-]*): "(.*)"\s*$', ln)
        if m:
            indent, key, inner = m.group(1), m.group(2), m.group(3)
            # Detect raw (unescaped) double quotes inside the scalar body.
            if re.search(r'(?<!\\)"', inner):
                # Convert to single-quoted YAML scalar: '' escapes a quote.
                body = inner.replace("''", "\x00").replace("'", "''").replace("\x00", "''")
                out.append(f"{indent}{key}: '{body}'")
                changed += 1
                continue
        out.append(ln)

    newfm = "\n".join(out)
    try:
        yaml.safe_load(newfm)
    except Exception as e:
        return f"still-broken: {str(e)[:100]}"
    path.write_text("---" + newfm + "---" + parts[2], encoding="utf-8")
    return f"fixed ({changed} scalars)"


def main():
    targets = sys.argv[1:]
    if targets:
        paths = [Path(t) for t in targets]
    else:
        paths = sorted((ROOT / "daily").glob("*.md"))
    for p in paths:
        print(p.name, "->", scan_and_fix(p))


if __name__ == "__main__":
    main()
