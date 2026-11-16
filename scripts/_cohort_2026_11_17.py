#!/usr/bin/env python3
"""Probe the 'cheat client' farm's owner cohorts and their placeholder repos.

Hypothesis: each owner account holds exactly 2 public repos — the payload repo
plus one random-name placeholder created ~2 minutes after the account.  If true,
the placeholder is a structural signature of the deployment, and it appears in
cohorts separated by months (which would mean the operation is long-running,
not a one-day burst).
"""
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


def repo_row(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [(b.get("path"), b.get("size")) for b in (tree.get("tree") or [])
             if b.get("type") == "blob"]
    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    if not isinstance(commits, list):
        commits = []
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "desc": m.get("description"),
        "n_blobs": len(blobs),
        "blob_paths": blobs[:10],
        "n_commits": len(commits),
        "commit_msgs": [((c.get("commit") or {}).get("message") or "").split("\n")[0][:60]
                        for c in commits][:6],
        "readme_len": len(rm),
        "readme_head": rm[:600],
        "license": (m.get("license") or {}).get("spdx_id"),
    }


def owner_block(login):
    u = api(f"users/{login}") or {}
    rs = api(f"users/{login}/repos", {"per_page": 100, "sort": "created"}) or []
    if not isinstance(rs, list):
        rs = []
    rows = []
    for r in rs:
        full = r.get("full_name")
        if not full:
            continue
        d = repo_row(full)
        d["owner_created"] = u.get("created_at")
        rows.append(d)
    return {
        "login": login,
        "created_at": u.get("created_at"),
        "followers": u.get("followers"),
        "public_repos": u.get("public_repos"),
        "repos": rows,
    }


OWNERS = [
    "OceanChandlerSewer", "SandstoneShoutMoon", "VergeEnvoyAdze",
    "ashtherapistpillar", "DestroyerStrait", "delugesovereignphase",
    "betovallefilho", "crackallergicaleinstein", "underwhiles",
]

if __name__ == "__main__":
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for b in ex.map(owner_block, OWNERS):
            out.append(b)
            print("=" * 92)
            print(f"OWNER {b['login']}  account_created={b['created_at']} "
                  f"followers={b['followers']} public_repos={b['public_repos']}")
            for r in b["repos"]:
                print(f"   -> {r['full_name']:<48} ⭐{r['stars']:<5} "
                      f"f={r['forks']:<4} s={r['subs']:<4} oi={r['oi']:<3} "
                      f"cmt={r['n_commits']:<3} blobs={r['n_blobs']:<3} "
                      f"size={r['size_kb']}KB")
                print(f"      created={r['created_at']} pushed={r['pushed_at']} "
                      f"lic={r['license']} readme={r['readme_len']}B")
                print(f"      paths={r['blob_paths'][:6]}")
                print(f"      msgs={r['commit_msgs'][:4]}")
                print(f"      desc={(r['desc'] or '')[:90]}")
    json.dump(out, open("/tmp/cohort_1117.json", "w"), ensure_ascii=False, indent=1)
    print("\nwrote /tmp/cohort_1117.json")
