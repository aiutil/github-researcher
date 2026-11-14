#!/usr/bin/env python3
'''Cross-day farm lineage + stargazer-account forensics + remaining project reads.'''

import json
import os
import subprocess
import urllib.parse
from collections import Counter
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")
D = json.load(open("/tmp/cand_1107.json", encoding="utf-8"))


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


def content(full, path):
    r, _ = api(f"repos/{full}/contents/{urllib.parse.quote(path)}", raw=True,
               headers=["Accept: application/vnd.github.raw"])
    return r or ""


print("=" * 72)
print("A. FARM LINEAGE: identical template files across 2026-11-06 and 2026-11-07")
day6 = ["HerdBuilderEstimate/roblox-studio-mcp", "PulverizeLink/roblox-performance-tool",
        "Lowbetweentrim/crypto-portfolio-tracker", "phaseboulderfetter/discord-quest-completer"]
day7 = ["Poltergeistlunagrid/Steam-Idler", "sentinelsoldierprize/Minecraft-AFK-Bot"]
import hashlib

for f in [".gitignore", "helpers.py", "config.py", "utils.py"]:
    print(f"\n  --- {f} ---")
    for full in day6 + day7:
        c = content(full, f)
        if c:
            print(f"    {full:48} len={len(c):6} md5={hashlib.md5(c.encode()).hexdigest()}")
        else:
            print(f"    {full:48} (absent)")

print()
print("  helpers.py full content (Steam-Idler):")
print("   ", repr(content("Poltergeistlunagrid/Steam-Idler", "helpers.py")))
print("  helpers.py full content (roblox-studio-mcp):")
print("   ", repr(content("HerdBuilderEstimate/roblox-studio-mcp", "helpers.py")))
print("  config.py (Steam-Idler):")
print("   ", repr(content("Poltergeistlunagrid/Steam-Idler", "config.py")))
print("  config.py (roblox-studio-mcp):")
print("   ", repr(content("HerdBuilderEstimate/roblox-studio-mcp", "config.py")))
print("  main.py (Minecraft-AFK-Bot):")
print("   ", repr(content("sentinelsoldierprize/Minecraft-AFK-Bot", "main.py")))
print("  utils.py (Minecraft-AFK-Bot):")
print("   ", repr(content("sentinelsoldierprize/Minecraft-AFK-Bot", "utils.py")))

print()
print("=" * 72)
print("B. STARGAZER ACCOUNT FORENSICS on the two 425-star repos (subs 25 / 35)")
for full in ["Poltergeistlunagrid/Steam-Idler", "sentinelsoldierprize/Minecraft-AFK-Bot", "lxe/phoneuse"]:
    st, err = api(f"repos/{full}/stargazers", {"per_page": 100})
    if not isinstance(st, list):
        print(f"  {full}: stargazers -> {err}")
        continue
    years = Counter()
    nullbio = 0
    norepos = 0
    fetched = 0
    for s in st[:25]:
        u, _ = api(f"users/{s['login']}")
        if u:
            fetched += 1
            years[u.get("created_at", "")[:4]] += 1
            if u.get("bio") in (None, ""):
                nullbio += 1
            if u.get("public_repos") == 0:
                norepos += 1
    print(f"  {full}: stargazers_sampled={len(st)} fetched={fetched}")
    print(f"     account-creation years: {sorted(years.items())}")
    print(f"     empty bio: {nullbio}/{fetched}   zero public repos: {norepos}/{fetched}")
