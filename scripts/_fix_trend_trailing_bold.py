#!/usr/bin/env python3
"""Strip a trailing bold run from daily trend names.

generate_readme.py wraps trend names as ``**{name}**``; a name that already
ends with ``**`` produces ``****`` which renders as literal asterisks.
Usage: python3 scripts/_fix_trend_trailing_bold.py daily/YYYY-MM-DD.md
"""

import sys
import yaml

path = sys.argv[1]
content = open(path, encoding="utf-8").read()
parts = content.split("---", 2)
fm = yaml.safe_load(parts[1])

changed = 0
for trend in fm.get("trends", []) or []:
    name = trend.get("name", "")
    if name.endswith("**"):
        trend["name"] = name[:-2].rstrip()
        changed += 1

if not changed:
    print("nothing to fix")
    raise SystemExit(0)

ordered = {
    "title": fm.get("title", ""),
    "date": fm.get("date", ""),
    "version": fm.get("version", "v1"),
    "summary": fm.get("summary", ""),
    "hero_badge": fm.get("hero_badge", ""),
    "stats": fm.get("stats", {}),
    "trends": fm.get("trends", []),
    "key_projects": fm.get("key_projects", []),
}

dumped = yaml.safe_dump(
    ordered, allow_unicode=True, sort_keys=False, default_flow_style=False, width=100000
)
open(path, "w", encoding="utf-8").write("---" + dumped + "---" + parts[2])
print(f"fixed {changed} trend names")
