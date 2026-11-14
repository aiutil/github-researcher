#!/usr/bin/env python3
'''Repair malformed YAML frontmatter in daily/*.md.

Several long double-quoted scalars were emitted without a closing quote or
with raw inner quotes.  We locate the failing line from the PyYAML error and
convert that one scalar into a folded block scalar (`>-`), which tolerates any
quote character in the payload.  The loop repeats until the document parses.
'''

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

KEY_RE = re.compile(r'^(\s*)([A-Za-z_][A-Za-z0-9_.-]*): "(.*)$')


def error_line(exc):
    m = re.search(r'line (\d+), column (\d+)', str(exc))
    if not m:
        return None
    return int(m.group(1))


def convert_to_block(lines, idx):
    '''Convert lines[idx] (0-based) `key: "....` into a folded block scalar.'''
    ln = lines[idx]
    m = KEY_RE.match(ln)
    if not m:
        return False
    indent, key, body = m.group(1), m.group(2), m.group(3)
    # Strip a trailing quote if present (well-formed scalar we are widening).
    body = body.rstrip()
    if body.endswith('"'):
        body = body[:-1]
    body = body.replace("\t", " ").rstrip()
    if not body:
        return False
    new = [f"{indent}{key}: >-", f"{indent}  {body}"]
    lines[idx:idx + 1] = new
    return True


def repair(path):
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
    for _ in range(60):
        try:
            yaml.safe_load("\n".join(lines))
            path.write_text("---" + "\n".join(lines) + "---" + parts[2], encoding="utf-8")
            return "fixed"
        except Exception as e:
            n = error_line(e)
            if n is None:
                return f"unresolved: {str(e)[:120]}"
            idx = n - 1
            if idx < 0 or idx >= len(lines):
                return f"bad-line-ref: {n}"
            if not convert_to_block(lines, idx):
                # Not a quoted scalar -> cannot repair mechanically.
                return f"manual: line {n}: {lines[idx][:100]}"
    return "too-many-iterations"


def main():
    targets = sys.argv[1:]
    paths = [Path(t) for t in targets] if targets else sorted((ROOT / "daily").glob("*.md"))
    for p in paths:
        r = repair(p)
        if r != "ok":
            print(f"{p.name}: {r}")
    print("repair pass done")


if __name__ == "__main__":
    main()
