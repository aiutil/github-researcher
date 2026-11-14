#!/usr/bin/env python3
"""Focused forensics on the 2026-11-10 window's 1 KB single-blob shell cluster.

Tests three automatable fingerprints that survive a cluster with 0 forks and 0 subs:
  (1) owner account creation-date clustering
  (2) templated SEO topic names derived from the product slug
  (3) commit-timestamp clustering + star-value banding
Also checks whether three previously profiled repos still resolve.
"""
import json
import os
import subprocess
import time
from collections import Counter
from datetime import datetime

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path_):
    p = subprocess.run(["gh", "api", path_], capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None, p.stderr.strip()[:160]
    try:
        return json.loads(p.stdout), None
    except Exception:
        return None, "parse"


rows = json.load(open("/tmp/w1111/cand_1110.json"))
shells = [r for r in rows if (r["size_kb"] or 0) <= 5 and (r["ncommits"] or 0) <= 2]
print(f"### shell cluster size = {len(shells)} / {len(rows)}\n")

print("=== 1. OWNER ACCOUNT CREATION DATES (batch) ===")
owners = {}
for r in shells:
    owner = r["full_name"].split("/")[0]
    if owner in owners:
        continue
    u, err = api(f"users/{owner}")
    if isinstance(u, dict):
        owners[owner] = (u.get("created_at"), u.get("public_repos"), u.get("followers"), u.get("type"))
    else:
        owners[owner] = (None, None, None, err)
    time.sleep(0.15)
days = Counter((v[0] or "?")[:10] for v in owners.values())
print("  owner created_at date distribution:")
for d, c in sorted(days.items(), key=lambda x: (-x[1], x[0])):
    print(f"    {d}: {c}")
print(f"  distinct owners = {len(owners)}")
print("  owners created 2026-06-10/11 (prior farm cohort window):")
for o, v in sorted(owners.items(), key=lambda x: (x[1][0] or "")):
    if v[0] and v[0][:10] in ("2026-06-10", "2026-06-11"):
        print(f"    {o:44s} created={v[0]} repos={v[1]} followers={v[2]}")
print("  public_repos distribution:", dict(Counter(v[1] for v in owners.values())))
print("  followers distribution:", dict(Counter(v[2] for v in owners.values())))

print("\n=== 2. TEMPLATED SEO TOPIC NAMES ===")
tmpl_hits = 0
tmpl_examples = []
for r in shells:
    topics = r.get("topics") or []
    slug = r["full_name"].split("/")[1]
    normalized = slug.lower().replace("-", "")
    hits = [t for t in topics if t.startswith(("guide-setup-", "how-to-install-", "how-to-setup-", "setup-", "install-"))
            and normalized and normalized in t.replace("-", "").replace("_", "")]
    if hits:
        tmpl_hits += 1
        if len(tmpl_examples) < 6:
            tmpl_examples.append((r["full_name"], len(topics), hits))
print(f"  repos whose topics contain a slug-derived setup/install template: {tmpl_hits}/{len(shells)}")
for full, n, hits in tmpl_examples:
    print(f"    {full:50s} topics={n} -> {hits}")
topic_counts = Counter(len(r.get("topics") or []) for r in shells)
print("  topic-count distribution:", dict(sorted(topic_counts.items())))

print("\n=== 3. COMMIT TIMESTAMP CLUSTERING + STAR BANDS ===")
times = []
for r in shells:
    cm, _ = api(f"repos/{r['full_name']}/commits?per_page=5")
    if isinstance(cm, list) and cm:
        au = (cm[0].get("commit") or {}).get("author") or {}
        if au.get("date"):
            times.append((au["date"], r["full_name"], r["stars"]))
    time.sleep(0.12)
times.sort()
print(f"  first-commit times: earliest={times[0][0] if times else '-'}  latest={times[-1][0] if times else '-'}")
if times:
    t0 = datetime.fromisoformat(times[0][0].replace("Z", "+00:00"))
    t1 = datetime.fromisoformat(times[-1][0].replace("Z", "+00:00"))
    print(f"  span = {(t1 - t0).total_seconds()/60:.1f} minutes across {len(times)} repos")
    print("  first 8:")
    for t, f, s in times[:8]:
        print(f"    {t}  {f:50s} stars={s}")
    print("  last 4:")
    for t, f, s in times[-4:]:
        print(f"    {t}  {f:50s} stars={s}")
starbands = Counter()
for r in shells:
    s = r["stars"] or 0
    band = f"{s//50*50}-{s//50*50+49}"
    starbands[band] += 1
print("  star bands (50-wide):", dict(sorted(starbands.items(), key=lambda x: int(x[0].split("-")[0]), reverse=True)))

print("\n=== 4. PREVIOUSLY PROFILED REPOS STILL RESOLVE? ===")
for full in ["elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop",
             "TameCarpenterEstate/Roblox-FPS-Optimizer",
             "Nanoutrolley/roblox-studio-mcp",
             "Sectionsereclaim/discord-auto-quest",
             "ridgecobblerslide/windows-animated-wallpapers",
             "Platoonritomb/Fortnite-FPS-Booster-Performance-Optimizer"]:
    m, err = api(f"repos/{full}")
    if isinstance(m, dict):
        print(f"  {full:58s} OK stars={m.get('stargazers_count')} forks={m.get('forks_count')} "
              f"subs={m.get('subscribers_count')} size={m.get('size')} created={m.get('created_at')}")
    else:
        print(f"  {full:58s} GONE/ERROR: {err}")
    time.sleep(0.15)

print("\n=== 5. windows-defender.cc DOMAIN REACHABILITY (HEAD, no execution) ===")
for url in ["https://windows-defender.cc/updater/Fix.ps1", "https://git-software.cc/ps/Setup.ps1"]:
    try:
        p = subprocess.run(["curl", "-sS", "-m", "25", "-o", "/tmp/w1111/probe.bin", "-w", "%{http_code} %{size_download}",
                            "-A", "Mozilla/5.0", url], capture_output=True, text=True, timeout=40)
        print(f"  {url} -> {p.stdout.strip()}  (stderr {p.stderr.strip()[:80]})")
    except Exception as e:
        print(f"  {url} -> ERROR {e}")
