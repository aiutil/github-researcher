#!/usr/bin/env python3
'''Final verification pass for the 2026-11-08 report.'''

import hashlib
import json
import os
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


print("=" * 72)
print("A. The 85 empty-README repos: how many share the SAME 2-file template?")
empty = [d for d in D if (d.get("readme_len") or 0) == 0]
print(f"empty-README count: {len(empty)}")
ih_md5 = Counter()
con_md5 = Counter()
with_tree = 0
for d in empty[:30]:
    full = d["full_name"]
    tree, _ = api(f"repos/{full}/git/trees/HEAD?recursive=1")
    if not tree:
        continue
    with_tree += 1
    for t in tree.get("tree", []):
        if t["type"] != "blob":
            continue
        if t["path"] == "initial.html":
            c, _ = api(f"repos/{full}/contents/initial.html", raw=True,
                       headers=["Accept: application/vnd.github.raw"])
            if c:
                ih_md5[hashlib.md5(c.encode()).hexdigest()] += 1
        if t["path"] == "CONTRIBUTING.md":
            c, _ = api(f"repos/{full}/contents/CONTRIBUTING.md", raw=True,
                       headers=["Accept: application/vnd.github.raw"])
            if c:
                con_md5[hashlib.md5(c.encode()).hexdigest()] += 1
print(f"  sampled {with_tree} trees")
print(f"  initial.html md5 groups: {ih_md5.most_common(5)}")
print(f"  CONTRIBUTING.md md5 groups: {con_md5.most_common(5)}")
print(f"  names without rpocket/respocket: "
      f"{[d['full_name'] for d in empty if 'rpocket' not in d['full_name'].lower() and 'respocket' not in d['full_name'].lower()][:12]}")

print()
print("=" * 72)
print("B. The 57 manus-family repos: README md5 + the Dropbox link")
fam = [d for d in D if "manus" in d["full_name"].lower()]
print(f"count={len(fam)}")
print(f"  all readme_len equal: {len(set(d['readme_len'] for d in fam))} distinct lengths -> {set(d['readme_len'] for d in fam)}")
print(f"  stars set: {sorted(set(d['stars'] for d in fam))}")
print(f"  licenses: {Counter(d['license'] for d in fam)}")
rm, _ = api("repos/LumiVikinggard89137/ai--manus/readme", raw=True,
            headers=["Accept: application/vnd.github.raw"])
print(f"  README length={len(rm or '')}")
for pat in ["dropbox.com", "PROMO2026", "manuscdn.com", "Manus_Studio.rar"]:
    print(f"    contains {pat!r}: {pat in (rm or '')}")
print("  README tail:")
print("   ", (rm or "")[-1200:])

print()
print("=" * 72)
print("C. Tracked projects status (from the 2026-11-07 tracked list)")
TRACK = [
    "rddmwmddr/android-ad-cleaner", "SAOS-3624/dsh-see-now", "valentderah/totk-pc-recomp",
    "unclebob/ub-mode", "trailofbits/brotli-checker", "DenisSergeevitch/ex-ussr-kinship-research",
    "YoyoLin008/mcreplay", "voyager-so/vork", "JosssphZhou/poki", "majorminorlabs/hermes-voice",
    "devvmhq/devvm", "JenkinWoo/sheeridVerify", "HerdBuilderEstimate/roblox-studio-mcp",
    "Tropicaldrescoop/discord-id-osint-checker", "interplains/zero-breach", "deepseek-ai/DeepInfer",
]
for full in TRACK:
    m, err = api(f"repos/{full}")
    if not m:
        print(f"  {full:44} -> NOT FOUND ({err})")
        continue
    print(f"  {full:44} stars={m.get('stargazers_count'):6} forks={m.get('forks_count'):5} "
          f"subs={m.get('subscribers_count'):3} oi={m.get('open_issues_count'):4} "
          f"pushed={m.get('pushed_at')} commits_pushed_age_days=?", end="")
    c, _ = api(f"repos/{full}/commits", {"per_page": 1})
    if isinstance(c, list) and c:
        print(f" last_commit={c[0]['commit']['author']['date']}", end="")
    print()
