#!/usr/bin/env python3
"""Verify three hypotheses for the 2026-11-15 window.

H1: The 21 `Gemini-Config-Checker-` repos are one deployment batch:
    identical README md5, identical payload link, identical code bytes,
    identical commit message multiset, identical commit timestamps,
    and owners drawn from a single registration cohort.

H2: `atlas7283/steam-library-bridge` publishes 4 releases within seconds with
    non-sequential version numbers off a single commit.

H3: `ineedfoundmyway/planrelay` vendors an upstream repo (badge points at a
    different owner) while presenting itself as an independent derivative.
"""
import hashlib
import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")


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


C = {r["full_name"]: r for r in json.load(open("/tmp/cand_1115.json"))}
gem = sorted(k for k in C if "Gemini-Config-Checker" in k)
print(f"=== H1: Gemini family n={len(gem)} ===")

print("\n-- owner registration cohort --")
owners = {}
for full in gem:
    o = full.split("/")[0]
    if o not in owners:
        u = api(f"users/{o}") or {}
        repos = api(f"users/{o}/repos", {"per_page": 100}) or []
        owners[o] = {
            "created": u.get("created_at"),
            "followers": u.get("followers"),
            "public_repos": u.get("public_repos"),
            "repos": [(r.get("name"), r.get("stargazers_count"), r.get("created_at"))
                      for r in repos] if isinstance(repos, list) else [],
        }
for o, d in sorted(owners.items(), key=lambda kv: kv[1]["created"] or ""):
    print(f"  {d['created']}  {o:32s} followers={d['followers']} repos={d['public_repos']}")
    for r in d["repos"]:
        print(f"        - {r[0]:34s} ⭐{r[1]} created={r[2]}")

print("\n-- commit message multiset + timestamps (first repo) --")
sample = gem[0]
cm = api(f"repos/{sample}/commits", {"per_page": 100}) or []
msgs = Counter()
times = []
for c in cm if isinstance(cm, list) else []:
    m = ((c.get("commit") or {}).get("message") or "").split("\n")[0]
    msgs[m] += 1
    au = ((c.get("commit") or {}).get("author") or {})
    times.append(au.get("date"))
print(f"  {sample}: {len(cm)} commits")
for m, n in msgs.most_common(12):
    print(f"    {n:3d}x {m}")
print(f"  first={times[0] if times else None} last={times[-1] if times else None}")
secs = Counter(t[-2:] for t in times if t)
print(f"  distinct commit second-fields: {len(secs)} -> {dict(secs.most_common(6))}")

print("\n-- byte-identity of code across repos --")
probe_paths = ["internal/scan/scan_test.go", "internal/scan/region.go",
               "dns_android.go", "Makefile", "go.mod", "VERSION"]
hashes = defaultdict(dict)
for full in gem[:8]:
    for pp in probe_paths:
        d = api(f"repos/{full}/contents/{pp}", raw=True,
                headers=["Accept: application/vnd.github.raw"])
        if d:
            hashes[pp][full] = hashlib.md5(d.encode()).hexdigest()[:12]
for pp, h in hashes.items():
    uniq = set(h.values())
    print(f"  {pp:32s} -> {len(h)} repos, {len(uniq)} distinct md5 {list(uniq)[:3]}")

print("\n-- per-repo star/fork/subs/blob/commit counts --")
for full in gem:
    r = C[full]
    print(f"  {full:44s} ⭐{r['stars']} ⑂{r['forks']} subs{r['subs']} oi{r['oi']} "
          f"blobs={r['n_blobs']} cmt={r['n_commits']} created={r['created_at']} lang={r['language']}")

print("\n-- payload link identity --")
links = set()
for full in gem:
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    for line in rm.splitlines():
        if "dropbox" in line.lower():
            import re
            for u in re.findall(r"https?://[^\s)\"'<>]+", line):
                links.add(u)
print(f"  distinct dropbox URLs across {len(gem)} READMEs: {len(links)}")
for u in links:
    print(f"    {u}")

print("\n=== H2: steam-library-bridge release timeline ===")
sl = "atlas7283/steam-library-bridge"
rel = api(f"repos/{sl}/releases", {"per_page": 20}) or []
for r in rel if isinstance(rel, list) else []:
    print(f"  tag={r.get('tag_name'):10s} published={r.get('published_at')} "
          f"created={r.get('created_at')} assets={len(r.get('assets') or [])} "
          f"name={r.get('name')}")
m = api(f"repos/{sl}") or {}
print(f"  repo size field = {m.get('size')} KB")
tree = api(f"repos/{sl}/git/trees/HEAD?recursive=1") or {}
blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
big = sorted(blobs, key=lambda b: -(b.get("size") or 0))[:8]
print("  largest blobs:")
for b in big:
    print(f"    {b.get('size'):>12} B  {b.get('path')}")
exe = [b for b in blobs if b.get("path", "").endswith(".exe")]
for b in exe:
    print(f"  exe blob: {b.get('path')} size={b.get('size')} sha={b.get('sha')}")
print(f"  total blobs={len(blobs)}  top dirs={Counter(b.get('path','').split('/')[0] for b in blobs).most_common(8)}")

print("\n=== H3: planrelay upstream relationship ===")
pl = "ineedfoundmyway/planrelay"
pm = api(f"repos/{pl}") or {}
print(f"  fork={pm.get('fork')} parent={(pm.get('parent') or {}).get('full_name')} source={(pm.get('source') or {}).get('full_name')}")
up = api("repos/brunnojob/planrelay")
if up:
    print(f"  upstream brunnojob/planrelay: ⭐{up.get('stargazers_count')} ⑂{up.get('forks_count')} "
          f"created={up.get('created_at')} pushed={up.get('pushed_at')} size={up.get('size')}KB")
    um = api("users/brunnojob") or {}
    print(f"  upstream owner: created={um.get('created_at')} repos={um.get('public_repos')} followers={um.get('followers')}")
    print(f"  SAME owner as local? {up.get('owner',{}).get('login') == pm.get('owner',{}).get('login')}")
tags = api(f"repos/{pl}/tags", {"per_page": 100}) or []
print(f"  local tags: {len(tags)} -> {[t.get('name') for t in tags[:8]]}")
utags = api("repos/brunnojob/planrelay/tags", {"per_page": 100}) or []
print(f"  upstream tags: {len(utags)} -> {[t.get('name') for t in utags[:8]]}")
print("  -- local .product / .agents / adr entries --")
ptree = api(f"repos/{pl}/git/trees/HEAD?recursive=1") or {}
for b in (ptree.get("tree") or []):
    if b.get("type") == "blob" and b.get("path", "").startswith((".product/", ".adr/", "adr/")):
        print(f"    {b.get('path')}")
print("  -- does local README reference upstream owner? --")
lrm = api(f"repos/{pl}/readme", raw=True, headers=["Accept: application/vnd.github.raw"]) or ""
for line in lrm.splitlines():
    if "brunnojob" in line or "upstream" in line.lower():
        print(f"    {line.strip()[:190]}")
