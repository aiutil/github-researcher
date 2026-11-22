#!/usr/bin/env python3
"""Fork-owner account age, fetched per-owner via users/{login} (the fork
payload does not carry owner.created_at, which is why the first pass
reported meta?=100 for every repo).

Suspect: ZhuLinsen/daily_stock_analysis (57,884 forks / 73,327 stars = 78.9%,
all 100 newest forks on 2026-11-18).
Controls: 9 ordinary repos, same n=100 newest forks, same method.

Also: the single-day fork-wave check -- how many of each repo's newest 100
forks fall on exactly one calendar day?
"""

import json
import os
import subprocess
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")

SUSPECT = "ZhuLinsen/daily_stock_analysis"
CONTROLS = [
    "torvalds/linux", "sveltejs/svelte", "astral-sh/uv",
    "vercel-labs/agent-browser", "openai/codex-security",
    "google-research/paper-orchestra", "NVIDIA/SkillEvaluator",
    "affaan-m/ECC", "appwrite/appwrite", "google-labs-code/stitch-skills",
    "elementalsouls/Claude-BugHunter", "HKUDS/CLI-Anything",
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


_OWNER = {}


def owner(login):
    if login not in _OWNER:
        u = api(f"users/{login}") or {}
        _OWNER[login] = {
            "created_at": u.get("created_at"),
            "followers": u.get("followers"),
            "public_repos": u.get("public_repos"),
            "type": u.get("type"),
        }
    return _OWNER[login]


def measure(full, n=100):
    m = api(f"repos/{full}") or {}
    forks = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n}) or []
    forks = forks if isinstance(forks, list) else []
    rec = {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks_total": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "n_sampled": len(forks),
        "fork_dates": dict(Counter(f.get("created_at", "")[:10] for f in forks)),
        "max_day_share": 0,
        "fresh_7d": 0, "fresh_30d": 0, "fresh_90d": 0, "fresh_365d": 0,
        "owner_meta_missing": 0,
        "owner_followers_sum": 0,
        "owner_repos_sum": 0,
        "owner_single_repo": 0,
        "owner_bot": 0,
    }
    dates = Counter(f.get("created_at", "")[:10] for f in forks)
    if dates:
        rec["max_day_share"] = round(max(dates.values()) / len(forks) * 100, 1)
    for f in forks:
        o = f.get("owner") or {}
        login = o.get("login")
        om = owner(login) if login else {}
        oc = om.get("created_at")
        fc = f.get("created_at")
        if not oc or not fc:
            rec["owner_meta_missing"] += 1
            continue
        import datetime as dt
        f_dt = dt.datetime.fromisoformat(fc.replace("Z", "+00:00"))
        o_dt = dt.datetime.fromisoformat(oc.replace("Z", "+00:00"))
        age = (f_dt - o_dt).days
        if age <= 7:
            rec["fresh_7d"] += 1
        if age <= 30:
            rec["fresh_30d"] += 1
        if age <= 90:
            rec["fresh_90d"] += 1
        if age <= 365:
            rec["fresh_365d"] += 1
        rec["owner_followers_sum"] += om.get("followers") or 0
        rec["owner_repos_sum"] += om.get("public_repos") or 0
        if (om.get("public_repos") or 0) <= 1:
            rec["owner_single_repo"] += 1
        if om.get("type") == "Bot":
            rec["owner_bot"] += 1
    return rec


def main():
    out = []
    print("=" * 122)
    print("FORK-OWNER ACCOUNT AGE (per-owner users/{login} lookup) + single-day fork-wave share")
    print("=" * 122)
    print(f"{'repo':44s} {'stars':>9s} {'forks':>8s} {'f/s%':>7s} {'1day%':>7s} "
          f"{'<=7d':>5s} {'<=30d':>6s} {'<=90d':>6s} {'<=365d':>7s} {'1repo%':>7s} {'bot':>4s}")
    print("=" * 122)
    for full in [SUSPECT] + CONTROLS:
        r = measure(full)
        out.append(r)
        fs = (r["forks_total"] / r["stars"] * 100) if r["stars"] else 0
        n = r["n_sampled"]
        print(f"{full:44s} {r['stars']:>9,} {r['forks_total']:>8,} {fs:>6.1f}% "
              f"{r['max_day_share']:>6.1f}% {r['fresh_7d']:>5} {r['fresh_30d']:>6} "
              f"{r['fresh_90d']:>6} {r['fresh_365d']:>7} "
              f"{(r['owner_single_repo']/n*100 if n else 0):>6.1f}% {r['owner_bot']:>4}", flush=True)

    json.dump(out, open("/tmp/forktest_1119b.json", "w"), ensure_ascii=False, indent=1)

    print()
    print("=" * 122)
    print("AGGREGATE: suspect vs 11 controls (n=100 newest forks each)")
    print("=" * 122)
    sus, ctl = out[0], out[1:]

    def agg(recs, key):
        tot = sum(r["n_sampled"] for r in recs)
        hit = sum(r[key] for r in recs)
        return hit, tot, (hit / tot * 100 if tot else 0)

    for key, label in (("fresh_7d", "owner account <=7d old at fork time"),
                       ("fresh_30d", "owner account <=30d old"),
                       ("fresh_90d", "owner account <=90d old"),
                       ("fresh_365d", "owner account <=365d old"),
                       ("owner_single_repo", "owner has <=1 public repo")):
        h1, t1, p1 = agg([sus], key)
        h2, t2, p2 = agg(ctl, key)
        print(f"  {label:38s} suspect {h1:>4}/{t1:<4} = {p1:5.1f}%   "
              f"control {h2:>4}/{t2:<4} = {p2:5.1f}%   delta = {p1 - p2:+6.1f}pp")

    print()
    print("  single-day fork-wave share (max day / 100 newest forks):")
    for r in out:
        tag = "  <-- SUSPECT" if r["repo"] == SUSPECT else ""
        print(f"    {r['repo']:44s} {r['max_day_share']:>6.1f}%  {r['fork_dates']}{tag}")


if __name__ == "__main__":
    main()
