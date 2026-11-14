#!/usr/bin/env python3
"""Deep-fetch details for selected 2026-11-08 candidates."""

import json
import os
import subprocess
import sys
import time
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")
TARGETS = sys.argv[1].split(",") if len(sys.argv) > 1 else []


def api(path, params=None, raw=False, headers=None):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=90)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


for full in TARGETS:
    print("=" * 100)
    print(f"### {full}")
    m = api(f"repos/{full}") or {}
    print(f"stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} "
          f"oi={m.get('open_issues_count')} size={m.get('size')}KB lang={m.get('language')} "
          f"lic={(m.get('license') or {}).get('spdx_id')} created={m.get('created_at')} pushed={m.get('pushed_at')}")
    print(f"desc={m.get('description')}")
    print(f"topics={m.get('topics')} homepage={m.get('homepage')} owner_type={(m.get('owner') or {}).get('type')}")
    ou = api(f"users/{full.split('/')[0]}") or {}
    print(f"OWNER created={ou.get('created_at')} repos={ou.get('public_repos')} followers={ou.get('followers')} "
          f"type={ou.get('type')} name={ou.get('name')}")
    rel = api(f"repos/{full}/releases") or []
    print(f"releases={len(rel) if isinstance(rel,list) else 0}")
    con = api(f"repos/{full}/contributors?per_page=10") or []
    print(f"contributors={len(con) if isinstance(con,list) else 0}")
    tree = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    tl = tree.get("tree", [])
    blobs = [t for t in tl if t.get("type") == "blob"]
    print(f"tree files={len(blobs)} (truncated={tree.get('truncated')})")
    for t in sorted(blobs, key=lambda x: -(x.get("size") or 0))[:22]:
        print(f"    {t.get('size'):>9} {t.get('path')}")
    commits = api(f"repos/{full}/commits?per_page=100") or []
    if isinstance(commits, list):
        print(f"commits(first page)={len(commits)} secs={len(set(c['commit']['author']['date'][-2:] for c in commits))}")
        for c in commits[:12]:
            print(f"    {c['commit']['author']['date']}  {c['commit']['message'].splitlines()[0][:80]}")
    forks = api(f"repos/{full}/forks?per_page=100&sort=newest") or []
    if isinstance(forks, list) and forks:
        ts = sorted(f["created_at"] for f in forks)
        print(f"forks page={len(forks)} first={ts[0]} last={ts[-1]}")
    print("--- README ---")
    rm = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"]) or ""
    print(rm[:6000])
    time.sleep(0.6)
