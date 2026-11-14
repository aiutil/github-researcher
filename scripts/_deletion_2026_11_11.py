#!/usr/bin/env python3
"""Quantify the account-deletion pattern across the farm cohorts.

The 11-10 window's 52 shells had 0 forks and 0 subs, so fork-arrival timing and
subscriber counts are unusable for them.  Owner-account age and account existence
are the signals that survive.  This script measures:
  (1) owner-account survival for the farm cohorts profiled on 11-06..11-10
  (2) whether the surviving accounts' own repos are also farm-shaped
  (3) the topic-template fingerprint rate, which needs no account history at all
"""
import json
import os
import subprocess
import time
from collections import Counter
from datetime import datetime, timezone

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path_):
    p = subprocess.run(["gh", "api", path_], capture_output=True, text=True, env=ENV, timeout=120)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


def alive(login):
    u = api(f"users/{login}")
    if not isinstance(u, dict):
        return None
    return (u.get("created_at"), u.get("public_repos"), u.get("followers"), u.get("type"))


# Cohort owners already observed in this repo's dailies (profiled as counterexamples
# or as farm samples) plus the full 52-owner shell cluster from the 11-10 window.
COHORTS = {
    "11-06 farm (profile .gitignore/helpers.py cohort)": [
        "HerdBuilderEstimate", "PulverizeLink", "Lowbetweentrim", "phaseboulderfetter",
    ],
    "11-07 farm (425* pair)": [
        "Poltergeistlunagrid", "sentinelsoldierprize",
    ],
    "11-08 farm (robiox template cohort)": [
        "ServantSieve", "Manaclenodisconnect", "finriderradial",
        "MuseumCassowaryCarve", "RapidSailorFreeze", "Nanoutrolley",
        "Sectionsereclaim", "ridgecobblerslide",
        "TameCarpenterEstate", "Platoonritomb",
    ],
    "11-08 Rust utility cohort (2026-08-15 batch)": [
        "PlateParrotTerminal", "ToneProtectorSolve48", "AmbassadorTassel",
        "majestydamseldecoder", "Avalanchevonproxy69",
    ],
    "11-08 keyword cluster (Manus)": [
        "LumiVikinggard89137", "Adil-Ijaz7", "thecoderrrer", "abhinay-h",
    ],
    "11-08 LiveWall (subs>stars)": ["elunboundfiremail"],
}

print("=" * 100)
print("=== 1. ACCOUNT SURVIVAL BY COHORT (snapshot: now) ===")
tot = Counter()
for label, owners in COHORTS.items():
    alive_n = 0
    gone = []
    details = []
    for o in owners:
        info = alive(o)
        if info:
            alive_n += 1
            details.append(f"{o}(created={info[0][:10]},repos={info[1]},f={info[2]})")
        else:
            gone.append(o)
    tot["total"] += len(owners)
    tot["alive"] += alive_n
    tot["gone"] += len(gone)
    print(f"\n  {label}  ({len(owners)} owners)")
    print(f"    alive: {alive_n}   deleted: {len(gone)}  {gone if gone else ''}")
    for d in details:
        print(f"      alive {d}")
    time.sleep(0.2)
print(f"\n  TOTAL: alive={tot['alive']}  deleted={tot['gone']}  of {tot['total']}")

print("\n" + "=" * 100)
print("=== 2. 11-10 WINDOW: 52 SHELL OWNERS -- ACCOUNT SURVIVAL ===")
rows = json.load(open("/tmp/w1111/cand_1110.json"))
shells = [r for r in rows if (r["size_kb"] or 0) <= 5 and (r["ncommits"] or 0) <= 2]
owners = []
for r in shells:
    o = r["full_name"].split("/")[0]
    if o not in owners:
        owners.append(o)
alive_n = 0
for o in owners:
    info = alive(o)
    if info:
        alive_n += 1
    time.sleep(0.12)
print(f"  {alive_n}/{len(owners)} owner accounts still exist")
print("  (i.e. the 11-10 cohort is NOT yet deleted -- these are the forward cohort)")

print("\n" + "=" * 100)
print("=== 3. TOPIC-TEMPLATE FINGERPRINT (no account history needed) ===")
for label, path in [("11-09 window (created 11-08)", "/tmp/cand_2026_11_09.json"),
                    ("11-10 window (created 11-09)", "/tmp/cand_2026_11_10.json"),
                    ("11-11 window (created 11-10)", "/tmp/w1111/cand_1110.json")]:
    rs = json.load(open(path))
    hit = 0
    withtopics = 0
    for r in rs:
        topics = r.get("topics") or []
        if not topics:
            continue
        withtopics += 1
        slug = r["full_name"].split("/")[1].lower().replace("-", "").replace("_", "")
        if any(tp.startswith(("guide-setup-", "how-to-install-", "how-to-setup-"))
               and slug and slug in tp.replace("-", "").replace("_", "") for tp in topics):
            hit += 1
    print(f"  {label}: repos_with_topics={withtopics}/{len(rs)}  "
          f"slug-derived setup/install topics={hit}")

print("\n" + "=" * 100)
print("=== 4. README PAYLOAD LINE PERSISTENCE ACROSS THE 3 WINDOWS ===")
for label, path in [("11-09 window (created 11-08)", "/tmp/cand_2026_11_09.json"),
                    ("11-10 window (created 11-09)", "/tmp/cand_2026_11_10.json"),
                    ("11-11 window (created 11-10)", "/tmp/w1111/cand_1110.json")]:
    rs = json.load(open(path))
    hits = [r for r in rs if r.get("hit_irm") or r.get("hit_invoke_expression")]
    print(f"  {label}: {len(hits)}/{len(rs)} README carry an irm/Invoke-Expression payload line")
