#!/usr/bin/env python3
'''Detail on interplains/zero-breach -- the OTHER interplains repository.'''

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


FULL = "interplains/zero-breach"
m, _ = api(f"repos/{FULL}")
print(f"id={m.get('id')} stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
      f"subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} size={m.get('size')}KB "
      f"lang={m.get('language')} lic={(m.get('license') or {}).get('spdx_id')} "
      f"created={m.get('created_at')} pushed={m.get('pushed_at')} topics={m.get('topics')}")
print(f"desc={m.get('description')}")

tree, _ = api(f"repos/{FULL}/git/trees/HEAD?recursive=1")
files = [t["path"] for t in (tree or {}).get("tree", []) if t["type"] == "blob"]
print(f"\nfiles({len(files)}):")
for f in files:
    print("   ", f)

ct, _ = api(f"repos/{FULL}/contributors")
print(f"\ncontributors={len(ct) if isinstance(ct, list) else ct}")

rm, _ = api(f"repos/{FULL}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
print(f"\nREADME ({len(rm or '')} bytes):")
print((rm or "")[:4200])
