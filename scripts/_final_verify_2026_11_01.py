#!/usr/bin/env python3
"""Final verification batch for the 2026-11-01 daily."""
import json, subprocess, os, re

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


def lastpage(full, sha=None):
    p = f"repos/{full}/commits?per_page=1" + (f"&sha={sha}" if sha else "")
    h = subprocess.run(["gh", "api", "-i", p], capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    return int(m.group(1)) if m else 1


print("### 1) ultratears: dev branch commit count + date range")
print(f"  main = {lastpage('kuraeow/ultratears')} commits")
print(f"  dev  = {lastpage('kuraeow/ultratears', 'dev')} commits")
cm = japi("repos/kuraeow/ultratears/commits?sha=dev&per_page=100") or []
if cm:
    ds = sorted(c["commit"]["author"]["date"] for c in cm)
    print(f"  dev page1 (newest 100): {ds[0]} .. {ds[-1]}")
    print(f"  dev commits on 10-29: {sum(1 for d in ds if d.startswith('2026-10-29'))}"
          f"  10-30: {sum(1 for d in ds if d.startswith('2026-10-30'))}"
          f"  10-31: {sum(1 for d in ds if d.startswith('2026-10-31'))}")
print("  newest dev commits:")
for c in cm[:6]:
    print(f"    {c['commit']['author']['date']} | {c['commit']['message'].splitlines()[0][:75]}")

print("\n### 2) battery-peek: in-place mutation smoking gun")
r = japi("repos/Yugiri-AO/battery-peek")
if r:
    print(f"  created={r['created_at']} pushed={r['pushed_at']} size={r['size']}KB stars={r['stargazers_count']}")
    cm = japi("repos/Yugiri-AO/battery-peek/commits?per_page=20") or []
    print(f"  commits={len(cm)}")
    for c in cm:
        print(f"    {c['commit']['author']['date']} | {c['commit']['message'].splitlines()[0][:80]}")

print("\n### 3) dsh-superagent issues/PRs")
il = japi("repos/deepseek-ai/dsh-superagent-prototype/issues?state=all&per_page=20") or []
print(f"  issues+PRs = {len(il)}")
for x in il:
    k = "PR" if "pull_request" in x else "issue"
    print(f"    #{x['number']} [{k}] {x['state']} {x['created_at'][:10]} {x['title'][:80]}")

print("\n### 4) 10-31 farm: README shape uniformity (payload repos)")
res = japi("search/repositories?q=created:2026-10-31+stars:>=40&per_page=100&sort=stars")
shapes = {}
for i in res["items"][:40]:
    t = japi(f"repos/{i['full_name']}/git/trees/HEAD?recursive=1") or {}
    blobs = [(e.get("size", 0), e["path"]) for e in t.get("tree", []) if e["type"] == "blob"]
    key = (len(blobs), tuple(sorted(p for _, p in blobs)))
    shapes.setdefault(key, []).append(i["full_name"])
for k, v in sorted(shapes.items(), key=lambda x: -len(x[1]))[:6]:
    print(f"  {len(v):>3} repos | {k[0]} files {k[1]}")
    if len(v) >= 3:
        print(f"        e.g. {v[0]}, {v[1]}")

print("\n### 5) floorplan Health feature (new in 0.6.0)")
rd = api("repos/haydenschmitty/floorplan/contents/README.md", raw=True) or ""
for ln in rd.splitlines():
    if "Health" in ln or "Supabase" in ln or "Stripe" in ln:
        print("   ", ln[:170])
