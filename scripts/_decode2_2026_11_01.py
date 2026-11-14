#!/usr/bin/env python3
"""Static decode of the already-fetched battery-peek loader (/tmp/bp.ps1). No execution."""
import base64, re, sys

raw = open("/tmp/bp.ps1", "rb").read()
txt = raw.decode("utf-8", "replace")
m = re.search(r"FromBase64String\('([^']+)'\)", txt)
if not m:
    print("no base64 blob found"); sys.exit(1)
stage2 = base64.b64decode(m.group(1)).decode("utf-8", "replace")
print("== STAGE 2 (decoded, static) — first 60 lines ==\n")
lines = stage2.splitlines()
for i, l in enumerate(lines[:60]):
    print(f"{i:3d}| {l[:400]}")

print("\n== PLAIN URLs in stage2 ==")
for mm in re.finditer(r"'(https?://[^']+)'", stage2):
    print("   ", mm.group(1))

print("\n== BASE64 blobs in stage2 that decode to URLs/hostnames ==")
seen = set()
for mm in re.finditer(r"'([A-Za-z0-9+/=]{20,})'", stage2):
    s = mm.group(1)
    if s in seen: continue
    seen.add(s)
    try:
        d = base64.b64decode(s).decode("utf-8", "replace")
    except Exception:
        continue
    if any(k in d for k in ("http", ".com", ".net", ".org", ".cc", ".top", "api.", "/")):
        print("   ", d[:140])
