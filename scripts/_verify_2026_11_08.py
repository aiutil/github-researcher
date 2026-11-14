#!/usr/bin/env python3
'''Verify (a) whether the farm repos actually contain runnable code,
(b) whether their "subscribers" are real depth-interest accounts,
(c) what the plausible-looking repos really ship.
'''

import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter

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


def show_file(full, path, limit=600):
    r, err = api(f"repos/{full}/contents/{urllib.parse.quote(path)}", raw=True,
                 headers=["Accept: application/vnd.github.raw"])
    if r is None:
        return f"  [ERR {err}] {path}"
    return f"  --- {path} ({len(r)} bytes) ---\n" + "\n".join("    " + ln for ln in r[:limit].split("\n"))


print("=" * 72)
print("A. STEAM-IDLER / MINECRAFT-AFK-BOT: is there any implementation?")
for full in ["Poltergeistlunagrid/Steam-Idler", "sentinelsoldierprize/Minecraft-AFK-Bot"]:
    print(f"\n### {full}")
    for f in ["config.py", "helpers.py", "main.py", "utils.py"]:
        tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
        names = [t["path"] for t in (tree or {}).get("tree", []) if t["type"] == "blob"]
        if f in names:
            print(show_file(full, f, limit=40))
    # .gitignore md5 vs the other repo
    for other in ["sentinelsoldierprize/Minecraft-AFK-Bot", "Poltergeistlunagrid/Steam-Idler"]:
        if other == full:
            continue
        a, _ = api(f"repos/{full}/contents/.gitignore", raw=True, headers=["Accept: application/vnd.github.raw"])
        b, _ = api(f"repos/{other}/contents/.gitignore", raw=True, headers=["Accept: application/vnd.github.raw"])
        if a and b:
            import hashlib
            print(f"  .gitignore md5 {full.split('/')[1][:16]}={hashlib.md5(a.encode()).hexdigest()}  "
                  f"{other.split('/')[1][:16]}={hashlib.md5(b.encode()).hexdigest()}  identical={a==b}")

print()
print("=" * 72)
print("B. SUBSCRIBERS of the two 425-star repos: account age distribution")
for full in ["Poltergeistlunagrid/Steam-Idler", "sentinelsoldierprize/Minecraft-AFK-Bot"]:
    subs, err = api(f"repos/{full}/subscribers", {"per_page": 100})
    if not isinstance(subs, list):
        print(f"  {full}: subscribers API -> {err}")
        continue
    print(f"\n  {full}: {len(subs)} subscribers (sampled)")
    years = Counter()
    logins = []
    for s in subs[:40]:
        u, _ = api(f"users/{s['login']}")
        if u:
            c = u.get("created_at", "")
            years[c[:4]] += 1
            logins.append((s["login"], c[:10], u.get("public_repos")))
    print(f"    account creation years: {sorted(years.items())}")
    print(f"    sample: {logins[:8]}")
    print(f"    repos with 0 public repos: {sum(1 for x in logins if x[2] == 0)}/{len(logins)}")

print()
print("=" * 72)
print("C. REAL-LOOKING CANDIDATES: content check")
for full in ["lxe/phoneuse", "Th0rgal/satmux", "SamG-Coder/solstice", "dabingfy-dot/solo-to-team-skills", "MajestyPoemFold/ghostclick-mouse-double-click-fix"]:
    m, _ = api(f"repos/{full}")
    if not m:
        print(f"\n### {full}: not found")
        continue
    tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    files = [(t["path"], t.get("size")) for t in (tree or {}).get("tree", []) if t["type"] == "blob"] if tree else []
    print(f"\n### {full}")
    print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} oi={m.get('open_issues_count')}")
    print(f"  size={m.get('size')}KB lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')} topics={m.get('topics')}")
    print(f"  created={m.get('created_at')} pushed={m.get('pushed_at')} owner={m.get('owner',{}).get('login')}({m.get('owner',{}).get('type')}, created {m.get('owner',{}).get('created_at')})")
    print(f"  desc={m.get('description')}")
    print(f"  files({len(files)}): {[f[0] for f in files][:22]}")
    print(f"  releases={api('repos/'+full+'/releases')[0] and len(api('repos/'+full+'/releases')[0]) or 0}")
