#!/usr/bin/env python3
"""Probe the 'cheat/crack' family repos surfaced by search on 2026-11-15..16.

Hypothesis under test (carried over from 11-16's RobRun finding): these repos
share a *description template* and a README template, sit in near-empty trees,
have 0 open issues, and accumulate stars far faster than forks/issues would
suggest for real usage.  This probe records only verifiable metadata.
"""
import hashlib
import json
import os
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def probe(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    if not isinstance(commits, list):
        commits = []
    msgs = [((c.get("commit") or {}).get("message") or "").split("\n")[0][:90]
            for c in commits]
    dates = [(((c.get("commit") or {}).get("author") or {}).get("date"))
             for c in commits]
    dates = [d for d in dates if d]
    issues = api(f"repos/{full}/issues", {"state": "all", "per_page": 50}) or []
    if not isinstance(issues, list):
        issues = []
    issues = [i for i in issues if "pull_request" not in i]
    owner = m.get("owner") or {}
    u = api(f"users/{owner.get('login')}") or {}
    repos_of_owner = api(f"users/{owner.get('login')}/repos",
                         {"per_page": 100, "sort": "created"}) or []
    if not isinstance(repos_of_owner, list):
        repos_of_owner = []
    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "watchers": m.get("watchers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "lang": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "desc": m.get("description"),
        "n_blobs": len(blobs),
        "blob_paths": [(b.get("path"), b.get("size")) for b in blobs][:30],
        "readme_len": len(rm),
        "readme_md5": hashlib.md5(rm.encode("utf-8", "replace")).hexdigest(),
        "readme_head": rm[:1400],
        "n_commits": len(commits),
        "commit_msgs": msgs[:15],
        "commit_dates": sorted(dates)[:8],
        "n_issues_all": len(issues),
        "issue_titles": [i.get("title", "")[:100] for i in issues][:8],
        "issue_users": sorted({(i.get("user") or {}).get("login") for i in issues
                              if (i.get("user") or {}).get("login")}),
        "owner_login": owner.get("login"),
        "owner_created": u.get("created_at"),
        "owner_followers": u.get("followers"),
        "owner_public_repos": u.get("public_repos"),
        "owner_repos": [(r.get("full_name"), r.get("stargazers_count"),
                         r.get("created_at")) for r in repos_of_owner][:40],
    }


REPOS = [
    "OceanChandlerSewer/rob-run-cheat-private",
    "SandstoneShoutMoon/ROB-RUN-cheat-client",
    "DestroyerStrait/RobRun-Cheat-Ares-Crack",
    "ashtherapistpillar/PUBG-private-cheat-midnight",
    "VergeEnvoyAdze/GTA5-cheat-client",
    "delugesovereignphase/phantom-blade-zero-cheat-engine",
    "betovallefilho/RobRun-Cheat-Menu-2026",
    "crackallergicaleinstein/HVHGOD-paid-cheat-free-forever-",
    "serena0322/pro-wardogs-bilberry",
    "underwhiles/Red-Dead-Redemption-2-Cheat-RDR-2-Hack-GodMode-ESP-More",
]

if __name__ == "__main__":
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(probe, REPOS):
            out.append(r)
            print(f"{r['full_name']:<55} *{r['stars']:<6} f={r['forks']:<4} "
                  f"s={r['subs']} oi={r['oi']:<4} cmt={r['n_commits']:<4} "
                  f"blob={r['n_blobs']:<4} size={r['size_kb']}KB "
                  f"lic={r['license']} md5={(r['readme_md5'] or '')[:8]}", flush=True)
    json.dump(out, open("/tmp/cheat_family_1117.json", "w"),
              ensure_ascii=False, indent=1)
    print("wrote /tmp/cheat_family_1117.json")
