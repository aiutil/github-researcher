#!/usr/bin/env python3
"""Map today's 27 trending repos to existing project profiles, and list which
need a NEW profile.  Uses validate.py's own slug rule: name.lower() with
non-alnum -> '-'.
"""
import glob
import json
import os
import re

trend = json.load(open("/tmp/trend_1122.json"))
existing = {os.path.basename(p)[:-3] for p in glob.glob("projects/*.md")}
print(f"{'repo':45s} {'slug(name rule)':32s} {'profile?':>9s}  match-by-fuzzy")
missing = []
for t in trend:
    name = t["full_name"]
    clean = re.sub(r"\s*\([^)]*\)", "", name).strip()
    slug = re.sub(r"[^a-z0-9]+", "-", clean.lower()).strip("-")
    hit = slug if slug in existing else None
    if not hit:
        # fuzzy: strip separators
        key = slug.replace("-", "")
        for e in existing:
            ek = e.replace("-", "").replace("_", "")
            if key in ek or ek in key:
                hit = e
                break
    status = hit or "MISSING"
    if not hit:
        missing.append((name, slug))
    print(f"{name:45s} {slug:32s} {status:>9s}")

print(f"\nMISSING ({len(missing)}):")
for n, s in missing:
    print(f"   {n}  -> projects/{s}.md")
