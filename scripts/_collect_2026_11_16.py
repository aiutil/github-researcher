#!/usr/bin/env python3
"""Collect candidate repos for the 2026-11-15 UTC creation window.

Discriminates real projects from star/payload farms by pulling metadata that
encodes engineering effort: tree blob count, file extension mix, commit
author-date distribution, license, owner account age, README text and its
md5 (identical READMEs across repos is a farm fingerprint), plus subscribers
and open issues (a farm rarely accrues real discussion).
"""

import hashlib
import json
import os
import subprocess
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

DAY = "2026-11-15"
MIN_STARS = int(sys.argv[1]) if len(sys.argv) > 1 else 30
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/cand_1115.json"

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=90, raw=False, headers=None):
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
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:200]}"


def search(q, page=1, per_page=100):
    d, _ = api("search/repositories", {"q": q, "sort": "stars", "order": "desc",
                                       "per_page": per_page, "page": page})
    return d.get("items", []) if d else []


def work(it):
    full = it["full_name"]
    m, _ = api(f"repos/{full}")
    m = m or {}
    branch = m.get("default_branch") or "main"
    commits, _ = api(f"repos/{full}/commits", {"per_page": 100})
    commits = commits if isinstance(commits, list) else []
    secs = set()
    for c in commits:
        au = (c.get("commit", {}) or {}).get("author", {}) or {}
        if au.get("date"):
            secs.add(au["date"][-2:])
    tree, _ = api(f"repos/{full}/git/trees/{branch}?recursive=1")
    tree = tree or {}
    blobs = tree.get("tree") or []
    blobs = [b for b in blobs if b.get("type") == "blob"]
    exts = {}
    for b in blobs:
        e = os.path.splitext(b.get("path", ""))[1].lower() or "<none>"
        exts[e] = exts.get(e, 0) + 1
    rm, _ = api(f"repos/{full}/readme", raw=True,
                headers=["Accept: application/vnd.github.raw"])
    rm = rm or ""
    lic = m.get("license") or {}
    owner = m.get("owner") or {}
    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "watchers": m.get("watchers_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": lic.get("spdx_id"),
        "license_name": lic.get("name"),
        "topics": m.get("topics", []),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "updated_at": m.get("updated_at"),
        "default_branch": branch,
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "archived": m.get("archived"),
        "is_fork": m.get("fork"),
        "has_issues": m.get("has_issues"),
        "has_wiki": m.get("has_wiki"),
        "has_discussions": m.get("has_discussions"),
        "owner_login": owner.get("login"),
        "owner_type": owner.get("type"),
        "n_commits": len(commits),
        "commit_secs": sorted(secs),
        "n_blobs": len(blobs),
        "exts": dict(sorted(exts.items(), key=lambda kv: -kv[1])[:12]),
        "truncated_tree": tree.get("truncated"),
        "readme_len": len(rm),
        "readme_md5": hashlib.md5(rm.encode("utf-8", "replace")).hexdigest(),
        "readme_head": rm[:1200],
    }


def main():
    q = f"created:{DAY} stars:>={MIN_STARS}"
    items = search(q)
    total, _ = api("search/repositories", {"q": q, "per_page": 1})
    print(f"query={q} total_count={total.get('total_count') if total else '?'} "
          f"fetched={len(items)}", flush=True)

    # fill up to 300 candidates
    for page in (2, 3, 4):
        if len(items) >= 300:
            break
        extra = search(q, page=page)
        if not extra:
            break
        items.extend(extra)

    seen = set()
    uniq = []
    for it in items:
        if it["full_name"] in seen:
            continue
        seen.add(it["full_name"])
        uniq.append(it)
    print(f"unique candidates: {len(uniq)}", flush=True)

    out = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        for i, r in enumerate(ex.map(work, uniq), 1):
            out.append(r)
            if i % 25 == 0 or i == len(uniq):
                print(f"  [{i}/{len(uniq)}] {r['full_name']} "
                      f"*{r['stars']} blobs={r['n_blobs']}", flush=True)

    with open(OUT, "w") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"wrote {len(out)} -> {OUT}", flush=True)


if __name__ == "__main__":
    main()
