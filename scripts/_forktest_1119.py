#!/usr/bin/env python3
"""The decisive 11-19 forensic test.

Hypothesis: ZhuLinsen/daily_stock_analysis shows a FORK WAVE (57,884 forks
vs 73,327 stars = 78.9% -- far above every other repo in today's cohort),
and its 100 newest forks were all created on 2026-11-18.

The 11-18 report established that an absolute threshold is worthless and a
CONTROL GROUP is required.  So: measure "fraction of fork owners whose
account was created within N days of the fork" for the suspect repo AND for
a control group of ordinary repos, at the SAME sample size and SAME date
window.

Also test the alternative hypothesis that this is genuine deploy-and-use
behaviour (the repo is a GitHub-Actions-deployed personal stock dashboard, so
forking to deploy is the documented intent).

Output: /tmp/forktest_1119.json
"""

import json
import os
import subprocess
import urllib.parse
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")

SUSPECT = "ZhuLinsen/daily_stock_analysis"
CONTROLS = [
    "torvalds/linux",
    "sveltejs/svelte",
    "astral-sh/uv",
    "vercel-labs/agent-browser",
    "openai/codex-security",
    "google-research/paper-orchestra",
    "NVIDIA/SkillEvaluator",
    "affaan-m/ECC",
    "appwrite/appwrite",
    "google-labs-code/stitch-skills",
]


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def owners_created_since(fork_created, owner_created, days):
    if not (fork_created and owner_created):
        return None
    # ISO-8601 lexicographic compare works for same-format UTC strings
    import datetime as dt
    try:
        f = dt.datetime.fromisoformat(fork_created.replace("Z", "+00:00"))
        o = dt.datetime.fromisoformat(owner_created.replace("Z", "+00:00"))
    except Exception:  # noqa: BLE001
        return None
    return (f - o).days <= days


def measure(full, n=100):
    m = api(f"repos/{full}") or {}
    forks = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n}) or []
    if not isinstance(forks, list):
        forks = []
    rec = {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks_total": m.get("forks_count"),
        "n_sampled": len(forks),
        "fork_dates": dict(Counter(f.get("created_at", "")[:10] for f in forks)),
        "fresh_7d": 0,
        "fresh_30d": 0,
        "fresh_365d": 0,
        "owner_meta_missing": 0,
        "owner_repos_total": 0,
        "owner_zero_repo_accounts": 0,
        "account_ages": [],
    }
    for f in forks:
        o = f.get("owner") or {}
        oc = o.get("created_at")
        fc = f.get("created_at")
        if not oc:
            rec["owner_meta_missing"] += 1
            continue
        if owners_created_since(fc, oc, 7):
            rec["fresh_7d"] += 1
        if owners_created_since(fc, oc, 30):
            rec["fresh_30d"] += 1
        if owners_created_since(fc, oc, 365):
            rec["fresh_365d"] += 1
        rec["account_ages"].append(oc[:10])
    # public repo counts of the fork owners (from the fork payload)
    pr = [f.get("owner", {}).get("public_repos") for f in forks
          if isinstance(f.get("owner", {}).get("public_repos"), int)]
    rec["owner_repos_total"] = sum(pr)
    rec["n_owners_with_repo_count"] = len(pr)
    return rec


def main():
    out = []
    print("=" * 118)
    print("FORK-OWNER ACCOUNT AGE: suspect vs control group (same n=100 newest forks, same method)")
    print("=" * 118)
    print(f"{'repo':44s} {'stars':>9s} {'forks':>8s} {'f/s%':>7s} {'n':>4s} "
          f"{'<=7d':>6s} {'<=30d':>6s} {'<=365d':>7s} {'meta?':>5s}")
    print("=" * 118)
    for full in [SUSPECT] + CONTROLS:
        r = measure(full)
        out.append(r)
        fs = (r["forks_total"] / r["stars"] * 100) if r["stars"] else 0
        n = r["n_sampled"]
        print(f"{full:44s} {r['stars']:>9,} {r['forks_total']:>8,} {fs:>6.1f}% {n:>4} "
              f"{r['fresh_7d']:>6} {r['fresh_30d']:>6} {r['fresh_365d']:>7} "
              f"{r['owner_meta_missing']:>5}", flush=True)
        print(f"    fork dates: {dict(list(r['fork_dates'].items())[:6])}")

    json.dump(out, open("/tmp/forktest_1119.json", "w"), ensure_ascii=False, indent=1)
    print("\nwrote /tmp/forktest_1119.json")

    # aggregate
    print()
    print("=" * 118)
    print("AGGREGATE")
    print("=" * 118)
    sus = out[0]
    ctl = out[1:]
    def pct(recs, key):
        tot = sum(r["n_sampled"] for r in recs)
        hit = sum(r[key] for r in recs)
        return hit, tot, (hit / tot * 100 if tot else 0)
    for key, label in (("fresh_7d", "owner created <=7d before fork"),
                       ("fresh_30d", "owner created <=30d before fork"),
                       ("fresh_365d", "owner created <=365d before fork")):
        h1, t1, p1 = pct([sus], key)
        h2, t2, p2 = pct(ctl, key)
        print(f"  {label:34s} suspect {h1:>4}/{t1:<4} = {p1:5.1f}%   "
              f"control {h2:>4}/{t2:<4} = {p2:5.1f}%   delta = {p1 - p2:+.1f}pp")


if __name__ == "__main__":
    main()
