#!/usr/bin/env python3
'''Trending-cluster metadata + stargazer API check + resp-token count.'''

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


print("=" * 72)
print("A. stargazers with the correct Accept header")
for full in ["lxe/phoneuse", "sentinelsoldierprize/Minecraft-AFK-Bot"]:
    st, err = api(f"repos/{full}/stargazers", {"per_page": 5},
                  headers=["Accept: application/vnd.github.star+json"])
    print(f"  {full}: {'OK n=' + str(len(st)) if isinstance(st, list) else err}")
    if isinstance(st, list) and st:
        print(f"     first entry keys: {list(st[0].keys())}")

print()
print("=" * 72)
print("B. resp/rpocket token count in the empty-README cluster")
empty = [d for d in D if d["readme_len"] == 0]
tok = sum(1 for d in empty if re.search(r"resp|rpocket|resocket", d["full_name"].lower()))
print(f"  empty-readme total={len(empty)}  containing resp/rpocket/resocket={tok}")
rest = [d["full_name"] for d in empty if not re.search(r"resp|rpocket|resocket", d["full_name"].lower())]
print(f"  without the token ({len(rest)}): {rest}")

print()
print("=" * 72)
print("C. trending-page repos: metadata")
TREND = ["vercel-labs/agent-browser", "cloudflare/security-audit-skill", "google/skills",
         "mattpocock/skills", "anthropics/skills", "meta/astryx", "ranxianglei/billion-context",
         "dsx-ai-factory/nvke", "sherlock-project/sherlock", "prometheus/prometheus"]
for full in TREND:
    m, err = api(f"repos/{full}")
    if not m:
        print(f"  {full}: {err}")
        continue
    print(f"  {full:42} stars={m.get('stargazers_count'):7} forks={m.get('forks_count'):5} "
          f"subs={m.get('subscribers_count'):4} oi={m.get('open_issues_count'):4} "
          f"created={str(m.get('created_at'))[:10]} pushed={str(m.get('pushed_at'))[:10]} "
          f"lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')}")
    print(f"      desc={str(m.get('description'))[:120]}")
