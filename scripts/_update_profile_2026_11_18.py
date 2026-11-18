#!/usr/bin/env python3
"""Update an existing project profile in place for 2026-11-18.

Rewrites the frontmatter (stars / stars_delta / last_seen_date) and appends a
'最近动态（2026-11-18）' section before the final separator, keeping all the
existing body intact.
"""
import re
import sys

PATH = sys.argv[1]
STARS = sys.argv[2]
DELTA = sys.argv[3]
TODAY = sys.argv[4]
SECTION = sys.argv[5]

src = open(PATH, encoding="utf-8").read()

# --- frontmatter ---
parts = src.split("---", 2)
fm = parts[1]
body = parts[2]

fm = re.sub(r'^last_seen_date:.*$', f'last_seen_date: "{TODAY}"', fm, flags=re.M)
fm = re.sub(r'^stars:.*$', f'stars: "{STARS}"', fm, flags=re.M)
fm = re.sub(r'^stars_delta:.*$', f'stars_delta: "{DELTA}"', fm, flags=re.M)

out = "---" + fm + "---" + body

# --- append the new section before the trailing separator / footer ---
marker = "\n---\n*首次记录"
if marker in out:
    head, tail = out.split(marker, 1)
    out = head + "\n" + SECTION + marker + tail
else:
    out = out.rstrip() + "\n\n" + SECTION + "\n"

open(PATH, "w", encoding="utf-8").write(out)
print(f"updated {PATH}: stars={STARS}, section {len(SECTION)} chars")
