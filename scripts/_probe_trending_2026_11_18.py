#!/usr/bin/env python3
"""Probe every repo on today's GitHub Trending (daily + weekly) with the
discriminators this project has established over 11-12 .. 11-17:

  * stars vs subscribers vs open issues vs forks  (star-farms have high subs
    relative to stars, zero issues, zero forks)
  * tree blob count / extension mix  (payload farms ship 2 blobs, 0 code)
  * README md5  (identical READMEs across repos = templated deployment)
  * commit author-date seconds distribution  (burst commits)
  * owner account age / followers / public repo count
  * release / tag chain closure

Output: /tmp/probe_1118.json
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/probe_1118.json"

URL = re.compile(r"https?://[^\s)\"'<>`]+")
PAY = ("dropbox", "mediafire", "mega.nz", "drive.google", "wetransfer",
       "pixeldrain", "linkbox", "discord.gg", "quark", "pan.baidu", "bit.ly",
       "modbay.live", "capsule-render", "readme-typing-svg")


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


_OWNER = {}


def owner_meta(login):
    if login not in _OWNER:
        _OWNER[login] = api(f"users/{login}") or {}
    return _OWNER[login]


def trending_repos():
    repos = []
    for period in ("daily", "weekly"):
        path = f"/tmp/trend_{period}.html"
        if not os.path.exists(path):
            continue
        src = open(path, encoding="utf-8", errors="replace").read()
        for blk in re.findall(r'<article class="Box-row">.*?</article>', src, re.S):
            m = re.search(r'<h2 class="h3 lh-condensed">.*?href="/([^"?]+)"', blk, re.S)
            if m:
                repos.append((m.group(1), period))
    seen, out = set(), []
    for r, p in repos:
        if r in seen:
            continue
        seen.add(r)
        out.append((r, p))
    return out


def probe(item):
    full, period = item
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    exts = Counter()
    for b in blobs:
        exts[os.path.splitext(b.get("path", ""))[1].lower() or "<none>"] += 1
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    commits = api(f"repos/{full}/commits", {"per_page": 100}) or []
    if not isinstance(commits, list):
        commits = []
    secs, authors = set(), set()
    for c in commits:
        au = (c.get("commit", {}) or {}).get("author", {}) or {}
        if au.get("date"):
            secs.add(au["date"][-2:])
        if au.get("name"):
            authors.add(au["name"])
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    if not isinstance(rel, list):
        rel = []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    if not isinstance(tags, list):
        tags = []
    owner = m.get("owner") or {}
    om = owner_meta(owner.get("login")) if owner.get("login") else {}
    lic = m.get("license") or {}
    stars = m.get("stargazers_count") or 0
    subs = m.get("subscribers_count") or 0
    forks = m.get("forks_count") or 0
    oi = m.get("open_issues_count") or 0
    urls = URL.findall(rm[:4000])
    return {
        "full_name": full,
        "period": period,
        "stars": stars,
        "forks": forks,
        "subs": subs,
        "watchers": m.get("watchers_count"),
        "oi": oi,
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": lic.get("spdx_id"),
        "topics": m.get("topics", []),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "archived": m.get("archived"),
        "is_fork": m.get("fork"),
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "default_branch": branch,
        "owner_login": owner.get("login"),
        "owner_type": owner.get("type"),
        "owner_created": om.get("created_at"),
        "owner_followers": om.get("followers"),
        "owner_public_repos": om.get("public_repos"),
        "n_blobs": len(blobs),
        "exts": dict(exts.most_common(10)),
        "truncated_tree": tree.get("truncated"),
        "n_commits": len(commits),
        "n_authors": len(authors),
        "commit_secs": sorted(secs),
        "n_releases": len(rel),
        "n_tags": len(tags),
        "release_assets": sum(len(r.get("assets") or []) for r in rel),
        "readme_len": len(rm),
        "readme_md5": hashlib.md5(rm.encode("utf-8", "replace")).hexdigest(),
        "readme_head": rm[:2500],
        "ext_links": sorted({u for u in urls if any(k in u.lower() for k in PAY)}),
    }


def main():
    items = trending_repos()
    print(f"trending repos to probe: {len(items)}", flush=True)
    out = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for i, r in enumerate(ex.map(probe, items), 1):
            out.append(r)
            print(f"  [{i}/{len(items)}] {r['full_name']:<45} ⭐{r['stars']:<7} "
                  f"subs={r['subs']:<6} oi={r['oi']:<5} blobs={r['n_blobs']:<5} "
                  f"rel={r['n_releases']}", flush=True)

    with open(OUT, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print("\n=== stars / subs ratio (star-farm indicator) ===")
    print(f"{'repo':<46}{'stars':>8}{'subs':>8}{'sub/star':>10}{'forks':>7}{'oi':>6}"
          f"{'blobs':>7}{'rel':>5}  owner/created")
    for r in sorted(out, key=lambda r: -(r["stars"] or 0)):
        ratio = (r["subs"] / r["stars"]) if r["stars"] else 0
        print(f"{r['full_name']:<46}{r['stars']:>8}{r['subs']:>8}{ratio:>10.3f}"
              f"{r['forks']:>7}{r['oi']:>6}{r['n_blobs']:>7}{r['n_releases']:>5}  "
              f"{r['owner_login']}/{(r['owner_created'] or '-')[:10]}")

    print("\n=== README md5 clusters (>=2) ===")
    by = defaultdict(list)
    for r in out:
        by[r["readme_md5"]].append(r)
    for md5, g in sorted(by.items(), key=lambda kv: -len(kv[1])):
        if len(g) < 2:
            continue
        print(f"  md5={md5[:16]} n={len(g)} len={g[0]['readme_len']}")
        for x in g:
            print(f"    - {x['full_name']} ⭐{x['stars']} subs{x['subs']}")

    print("\n=== payload-ish / templating links ===")
    for r in out:
        if r["ext_links"]:
            print(f"  {r['full_name']:<46} -> {r['ext_links'][:4]}")

    print("\n=== owners ===")
    for r in sorted(out, key=lambda r: (r["owner_created"] or "")):
        print(f"  {r['owner_login']:<28} created={r['owner_created']} "
              f"type={r['owner_type']} foll={r['owner_followers']} "
              f"repos={r['owner_public_repos']}  -> {r['full_name']}")

    print(f"\nwrote {len(out)} -> {OUT}")


if __name__ == "__main__":
    main()
