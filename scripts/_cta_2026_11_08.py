#!/usr/bin/env python3
'''Last data gathering round: farm README CTAs + remaining project text.'''

import json
import os
import re
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=90, raw=False, headers=None):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in headers or []:
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception:
        return None, "parse"


print("=" * 72)
print("A. Do the two 425-star farms ask for stars/subscriptions?")
for full in ["Poltergeistlunagrid/Steam-Idler", "sentinelsoldierprize/Minecraft-AFK-Bot"]:
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    t = rm or ""
    print(f"\n  {full} README ({len(t)} bytes):")
    for ln in t.split("\n"):
        if re.search(r"star|watch|subscribe|⭐|Star this|fork", ln, re.I):
            print(f"    | {ln.strip()[:170]}")
    print("  --- tail ---")
    print("   ", t[-900:].replace("\n", "\n    "))

print()
print("=" * 72)
print("B. satmux README: limitations / safety")
rm, _ = api("repos/Th0rgal/satmux/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
t = rm or ""
print(f"  length={len(t)}")
for key in ["## Limit", "## Security", "## Note", "## Caveat", "## Risk", "## Legal", "## What this is not"]:
    i = t.find(key)
    if i >= 0:
        print(f"\n  --- {key} ---")
        print("   ", t[i:i + 1800])
        break

print()
print("=" * 72)
print("C. axiom-launch-replay: what it does NOT do")
rm, _ = api("repos/raygullcrease/axiom-launch-replay/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
t = rm or ""
print(f"  length={len(t)}")
for key in ["not connected", "What this is not", "## Limit", "paper", "Risk"]:
    i = t.lower().find(key.lower())
    if i >= 0:
        print(f"\n  --- around {key!r} ---")
        print("   ", t[max(0, i - 500):i + 1500])
        break
