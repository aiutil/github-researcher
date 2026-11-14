#!/usr/bin/env python3
import sys
import yaml
from pathlib import Path

p = Path(sys.argv[1])
c = p.read_text(encoding="utf-8")
parts = c.split("---", 2)
try:
    m = yaml.safe_load(parts[1])
    print("OK keys:", list(m.keys()) if m else m)
except Exception as e:
    print("ERR:")
    print(e)
    # show offending region
    lines = parts[1].split("\n")
    for i, ln in enumerate(lines[:60], 1):
        print(i, repr(ln[:120]))
