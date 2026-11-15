#!/usr/bin/env python3
"""Deep forensics on selected 2026-11-15 candidates.

Adds: owner account age + repo count + followers, workflow names (random-string
detector), release/tag presence, README full text, tree top-level layout,
fork arrival timing for high fork/star ratios, and code-vs-doc byte split.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
C = {r["full_name"]: r for r in json.load(open("/tmp/cand_1115.json"))}


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
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


def owner_info(login):
    d = api(f"users/{login}")
    if not d:
        return None
    repos = api(f"users/{login}/repos", {"per_page": 100, "sort": "created"}) or []
    return {
        "login": login,
        "type": d.get("type"),
        "created_at": d.get("created_at"),
        "followers": d.get("followers"),
        "public_repos": d.get("public_repos"),
        "repos_listed": len(repos) if isinstance(repos, list) else 0,
        "repo_names": [r.get("name") for r in repos] if isinstance(repos, list) else [],
    }


def repo_deep(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path", "") for b in blobs]
    top = Counter(p.split("/")[0] for p in paths)
    wf = [p for p in paths if p.startswith(".github/workflows/")]
    rel = api(f"repos/{full}/releases", {"per_page": 5}) or []
    tags = api(f"repos/{full}/tags", {"per_page": 10}) or []
    commits = api(f"repos/{full}/commits", {"per_page": 30}) or []
    cmt = []
    for c in commits if isinstance(commits, list) else []:
        au = ((c.get("commit") or {}).get("author") or {})
        cmt.append((au.get("date"), (c.get("commit") or {}).get("message", "").split("\n")[0][:70]))
    forks = api(f"repos/{full}/forks", {"sort": "newest", "per_page": 100}) or []
    ftimes = []
    for f in forks if isinstance(forks, list) else []:
        ftimes.append(f.get("created_at"))
    ftimes = sorted([t for t in ftimes if t])
    gaps = []
    import datetime
    for i in range(1, len(ftimes)):
        a = datetime.datetime.fromisoformat(ftimes[i - 1].replace("Z", "+00:00"))
        b = datetime.datetime.fromisoformat(ftimes[i].replace("Z", "+00:00"))
        gaps.append((b - a).total_seconds())
    gaps_sorted = sorted(gaps)
    return {
        "full": full,
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "watchers": m.get("watchers_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "topics": m.get("topics", []),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "default_branch": branch,
        "n_blobs": len(blobs),
        "truncated": tree.get("truncated"),
        "top_dirs": dict(top.most_common(14)),
        "workflows": wf,
        "n_releases": len(rel) if isinstance(rel, list) else 0,
        "releases": [(r.get("tag_name"), r.get("published_at"), r.get("name")) for r in rel] if isinstance(rel, list) else [],
        "tags": [t.get("name") for t in tags] if isinstance(tags, list) else [],
        "recent_commits": cmt,
        "fork_times": ftimes,
        "fork_gap_median": gaps_sorted[len(gaps_sorted) // 2] if gaps_sorted else None,
        "fork_le10": sum(1 for g in gaps if g <= 10),
        "fork_n": len(ftimes),
        "fork_span_min": round((datetime.datetime.fromisoformat(ftimes[-1].replace("Z", "+00:00")) -
                                datetime.datetime.fromisoformat(ftimes[0].replace("Z", "+00:00"))).total_seconds() / 60, 1) if len(ftimes) > 1 else 0,
    }


def readme(full):
    return api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"]) or ""


def tree_files(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    return [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]


TARGETS = sys.argv[1:] or [
    "ineedfoundmyway/planrelay",
    "atlas7283/steam-library-bridge",
    "tsukumijima/pydtcpip",
    "Dart-veider01/TradingAgents-crypto",
    "rauchg/winamp-ui-sdk",
    "cnrad/interspace",
    "huangserva/h3-fight",
    "petekp/coordinator",
    "bymodify-ux/Dying-Light-VR",
    "Pixelgamer4k/WZM-4.5.2-offline-source",
    "WindGatorRise37/Gemini-Config-Checker-",
    "HideKazekage/rob-run-cheat-tool",
    "lishuangqiang/mixbar",
]

out = {}
for full in TARGETS:
    print(f"=== {full} ===", flush=True)
    d = repo_deep(full)
    d["owner"] = owner_info(full.split("/")[0])
    blobs = tree_files(full)
    d["blob_paths"] = [b.get("path") for b in blobs]
    d["blob_sizes"] = {b.get("path"): b.get("size") for b in blobs}
    rm = readme(full)
    d["readme_len"] = len(rm)
    d["readme_md5"] = hashlib.md5(rm.encode()).hexdigest()
    d["readme_head"] = rm[:2500]
    d["readme_tail"] = rm[-1200:]
    out[full] = d
    o = d["owner"] or {}
    print(f"  ⭐{d['stars']} ⑂{d['forks']} subs{d['subs']} oi{d['oi']} "
          f"blobs={d['n_blobs']} trunc={d['truncated']} {d['size_kb']}KB {d['language']} {d['license']}")
    print(f"  owner: type={o.get('type')} created={o.get('created_at')} followers={o.get('followers')} "
          f"public_repos={o.get('public_repos')} listed={o.get('repos_listed')}")
    print(f"  repos: {o.get('repo_names')}")
    print(f"  top_dirs: {d['top_dirs']}")
    print(f"  workflows: {d['workflows']}")
    print(f"  releases({d['n_releases']}): {d['releases'][:3]}  tags: {d['tags'][:5]}")
    print(f"  commits: {d['recent_commits'][:6]}")
    print(f"  forks: n={d['fork_n']} median_gap={d['fork_gap_median']}s <=10s={d['fork_le10']} span={d['fork_span_min']}min")
    print(f"  readme_len={d['readme_len']} md5={d['readme_md5'][:12]} topics={d['topics'][:8]}", flush=True)

json.dump(out, open("/tmp/deep_1115.json", "w"), ensure_ascii=False)
print("\nwrote /tmp/deep_1115.json")
