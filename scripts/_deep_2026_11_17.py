#!/usr/bin/env python3
"""Deep metadata probe for a list of repos: tree, commits, releases, issues,
subscribers, license file head, README head.  Used to build evidence tables."""
import hashlib
import json
import os
import re
import subprocess
import sys
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
    exts = {}
    for b in blobs:
        e = os.path.splitext(b.get("path", ""))[1].lower() or "<none>"
        exts[e] = exts.get(e, 0) + 1
    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    if not isinstance(commits, list):
        commits = []
    msgs = []
    dates = []
    authors = set()
    for c in commits:
        cm = (c.get("commit") or {})
        msgs.append((cm.get("message") or "").split("\n")[0][:120])
        d = ((cm.get("author") or {}).get("date"))
        if d:
            dates.append(d)
        n = ((cm.get("author") or {}).get("name"))
        if n:
            authors.add(n)
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    lic_txt = api(f"repos/{full}/license", raw=True,
                  headers=["Accept: application/vnd.github.raw"]) or ""
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    subs = api(f"repos/{full}/subscribers") or []
    issues = api(f"repos/{full}/issues", {"state": "open", "per_page": 50}) or []
    issues = [i for i in issues if "pull_request" not in i] if isinstance(issues, list) else []
    contribs = api(f"repos/{full}/contributors", {"per_page": 100}) or []
    owner = m.get("owner") or {}
    u = api(f"users/{owner.get('login')}") or {}
    lic = m.get("license") or {}
    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "lang": m.get("language"),
        "license": lic.get("spdx_id"),
        "license_name": lic.get("name"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "updated_at": m.get("updated_at"),
        "homepage": m.get("homepage"),
        "desc": m.get("description"),
        "topics": m.get("topics", []),
        "is_fork": m.get("fork"),
        "archived": m.get("archived"),
        "default_branch": branch,
        "n_blobs": len(blobs),
        "truncated": tree.get("truncated"),
        "exts": dict(sorted(exts.items(), key=lambda kv: -kv[1])[:14]),
        "n_commits": len(commits),
        "n_authors": len(authors),
        "commit_msgs_head": msgs[:12],
        "commit_dates_head": dates[:6],
        "readme_len": len(rm),
        "readme_md5": hashlib.md5(rm.encode("utf-8", "replace")).hexdigest(),
        "readme_head": rm[:2500],
        "license_head": lic_txt[:300],
        "n_releases": len(rel) if isinstance(rel, list) else 0,
        "releases": [(r.get("tag_name"), r.get("created_at"), r.get("published_at"),
                      len(r.get("assets") or [])) for r in (rel or [])][:8]
        if isinstance(rel, list) else [],
        "n_tags": len(tags) if isinstance(tags, list) else 0,
        "subs_list": [s.get("login") for s in (subs or [])] if isinstance(subs, list) else [],
        "n_open_issues": len(issues),
        "issue_titles": [i.get("title", "")[:110] for i in issues][:14],
        "issue_authors": sorted({(i.get("user") or {}).get("login") for i in issues
                                 if (i.get("user") or {}).get("login")}),
        "contributors": [(c.get("login"), c.get("contributions"))
                         for c in (contribs or [])][:12] if isinstance(contribs, list) else [],
        "owner_login": owner.get("login"),
        "owner_created": u.get("created_at"),
        "owner_followers": u.get("followers"),
        "owner_public_repos": u.get("public_repos"),
        "owner_type": u.get("type"),
        "top_paths": [b.get("path") for b in blobs[:40]],
    }


if __name__ == "__main__":
    repos = sys.argv[1:]
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(probe, repos):
            out.append(r)
            print(f"{r['full_name']:<45} *{r['stars']:<7} f={r['forks']:<5} "
                  f"s={r['subs']:<4} oi={r['oi']:<4} cmt={r['n_commits']:<4} "
                  f"blobs={r['n_blobs']:<5} rel={r['n_releases']:<3} "
                  f"lic={(r['license'] or '-'):<14} {r['lang']}", flush=True)
    json.dump(out, open("/tmp/deep_1117.json", "w"), ensure_ascii=False, indent=1)
    print("wrote /tmp/deep_1117.json")
