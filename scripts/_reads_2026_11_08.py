#!/usr/bin/env python3
'''Read the remaining candidates' own documents.'''

import json
import os
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


def content(full, path, limit=3200):
    r, _ = api(f"repos/{full}/contents/{urllib.parse.quote(path)}", raw=True,
               headers=["Accept: application/vnd.github.raw"])
    if r is None:
        return f"[MISSING {path}]"
    return r[:limit]


JOBS = [
    ("Th0rgal/satmux", ["README.md"]),
    ("dabingfy-dot/solo-to-team-skills", ["README.md", "skills/evidence-before-done/SKILL.md"]),
    ("MajestyPoemFold/ghostclick-mouse-double-click-fix", ["README.md"]),
    ("raygullcrease/axiom-launch-replay", ["README.md", "CREDITS.md"]),
    ("qnguyen3/zalo-swift-re", ["README.md"]),
    ("SamG-Coder/solstice", ["README.md"]),
]

for full, paths in JOBS:
    m, _ = api(f"repos/{full}")
    if not m:
        print(f"### {full}: NOT FOUND")
        continue
    print("=" * 72)
    print(f"### {full}  stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
          f"subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} size={m.get('size')}KB "
          f"lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')}")
    print(f"    created={m.get('created_at')} pushed={m.get('pushed_at')} "
          f"owner={m.get('owner',{}).get('login')} type={m.get('owner',{}).get('type')}")
    print(f"    topics={m.get('topics')}")
    print(f"    desc={m.get('description')}")
    for p in paths:
        print(f"\n--- {p} ---")
        print(content(full, p))
