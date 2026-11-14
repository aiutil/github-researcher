#!/usr/bin/env python3
'''Repair malformed YAML frontmatter in daily/*.md by widening long or
quote-unsafe double-quoted scalars into folded block scalars (`>-`).

A folded block scalar carries the payload literally, so embedded double
quotes, backslashes and `#` need no escaping.  Only scalars that are long
(>=120 chars) or that contain an unescaped inner double quote are rewritten,
so the diff stays limited to the broken entries.
'''

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

SCALAR_RE = re.compile(r'^(\s*)([A-Za-z_][A-Za-z0-9_.-]*): "(.*)$')


def unescape_dq(body: str) -> str:
    '''Resolve the escape sequences valid inside a YAML double-quoted scalar.'''
    out = []
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == "\\" and i + 1 < len(body):
            nxt = body[i + 1]
            if nxt == '"':
                out.append('"')
            elif nxt == "\\":
                out.append("\\")
            elif nxt == "n":
                out.append("\n")
            elif nxt == "t":
                out.append("\t")
            else:
                out.append(ch)
                out.append(nxt)
            i += 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def has_raw_quote(body: str) -> bool:
    '''True if body holds a double quote that is not backslash-escaped.'''
    i = 0
    while i < len(body):
        if body[i] == "\\":
            i += 2
            continue
        if body[i] == '"':
            return True
        i += 1
    return False


def widen(lines):
    changed = 0
    out = []
    for ln in lines:
        m = SCALAR_RE.match(ln)
        if m:
            indent, key, body = m.group(1), m.group(2), m.group(3)
            trailing_closed = body.endswith('"')
            inner = body[:-1] if trailing_closed else body
            raw_q = has_raw_quote(inner)
            if len(ln) >= 120 or raw_q or not trailing_closed:
                payload = unescape_dq(inner).rstrip()
                if payload:
                    out.append(f"{indent}{key}: >-")
                    out.append(f"{indent}  {payload}")
                    changed += 1
                    continue
        out.append(ln)
    return out, changed


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
    newlines, changed = widen(lines)
    try:
        yaml.safe_load("\n".join(newlines))
    except Exception as e:
        return f"unresolved: {str(e)[:160]}"
    path.write_text("---" + "\n".join(newlines) + "---" + parts[2], encoding="utf-8")
    return f"fixed ({changed} scalars)"


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
