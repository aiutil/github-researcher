#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import yaml

p = Path(sys.argv[1])
c = p.read_text(encoding="utf-8")
parts = c.split("---", 2)
fm = parts[1]
lines = fm.split("\n")

print("=== raw line endings (last 60 chars) for long scalar lines ===")
for i, ln in enumerate(lines, 1):
    if len(ln) > 200:
        print(i, "len", len(ln), "| start:", repr(ln[:60]), "| end:", repr(ln[-60:]))

print()
print("=== bisect: find minimal prefix that fails ===")
lo, hi = 1, len(lines)
bad = None
for n in range(1, len(lines) + 1):
    chunk = "\n".join(lines[:n])
    try:
        yaml.safe_load(chunk)
    except Exception:
        # ignore 'expected block end' style truncation errors at the tail
        msg = str(yaml.safe_load(chunk)) if False else ""
        try:
            yaml.safe_load(chunk)
        except Exception as e:
            msg = str(e)
        if "expected <block end>" in msg or "expected the node content" in msg:
            continue
        bad = n
        print("FAIL at line", n, "->", msg[:200])
        break
if bad:
    ln = lines[bad - 1]
    print("OFFENDING LINE", bad, "len", len(ln))
    print("  start:", repr(ln[:150]))
    print("  end  :", repr(ln[-150:]))
    print("  raw double quotes count:", ln.count('"'))
    print("  raw backslash count:", ln.count("\\"))
