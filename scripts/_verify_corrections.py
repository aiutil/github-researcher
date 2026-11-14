#!/usr/bin/env python3
"""Decisive: (1) ultratears dev-branch timeline vs yesterday's snapshot, (2) farm payload prevalence exhaustive on 10-29 <=20KB subset."""
import json, subprocess, os, re, collections

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


SNAP = "2026-10-29T22:30:00Z"  # yesterday's snapshot window
print("### 1) ultratears dev branch: full timeline")
dev = japi("repos/kuraeow/ultratears/commits?sha=dev&per_page=100") or []
dates = [c["commit"]["author"]["date"] for c in dev]
print(f"  dev commits (page1 of 87): newest={dates[0]} oldest_on_page={dates[-1]}")
byday = collections.Counter(d[:10] for d in dates)
print(f"  dev commits per day: {dict(sorted(byday.items()))}")
before = sum(1 for d in dates if d < SNAP)
print(f"  dev commits BEFORE yesterday's snapshot ({SNAP}): {before} (of 87 total)")
print(f"  -> yesterday's '仅 3 个 commit（10-25 一天内全部完成）' counted ONLY the default branch 'main' (3)")
print(f"  -> at yesterday's snapshot the repo already had {3+before} commits across 2 branches")

print("\n### 2) ultratears main-branch commits vs dev")
mn = japi("repos/kuraeow/ultratears/commits?sha=main&per_page=10") or []
print(f"  main: {len(mn)} commits, dates={[c['commit']['author']['date'] for c in mn]}")

print("\n### 3) 10-29 cohort: exhaustive payload check on the <=20KB subset")
c29 = japi("search/repositories?q=created:2026-10-29+stars:>=40+size:<=20&per_page=100")
items = c29["items"]
print(f"  total_count={c29['total_count']} fetched={len(items)}")
hits = []
for i in items:
    rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
    if "git-software.cc" in rd or "Invoke-Expression" in rd:
        hits.append(i["full_name"])
print(f"  payload hits among the {len(items)} remaining <=20KB shells: {len(hits)}")
for h in hits:
    print(f"    {h}")

print("\n### 4) structural fingerprint of the 10-29 cohort (all 45 sampled earlier) — count by file-set signature")
c29b = japi("search/repositories?q=created:2026-10-29+stars:>=40&per_page=45")
sig = collections.Counter()
for i in c29b["items"]:
    tree = japi(f"repos/{i['full_name']}/git/trees/HEAD?recursive=1") or {}
    blobs = [e["path"] for e in tree.get("tree", []) if e["type"] == "blob"]
    has_rand_gh = any(p.startswith(".github/") and not p.endswith(".yml") and not p.endswith(".yaml") for p in blobs)
    has_svg = any(p.endswith(".svg") for p in blobs)
    has_index = any(p.endswith("index.html") for p in blobs)
    key = (has_rand_gh, has_svg, has_index)
    sig[key] += 1
print("  (random .github file, .svg filler, index.html) -> count")
for k, v in sig.most_common():
    print(f"    {k} -> {v}")
