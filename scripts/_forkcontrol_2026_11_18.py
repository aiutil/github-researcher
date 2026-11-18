#!/usr/bin/env python3
"""Control-group comparison for 2026-11-18.

The claim under test: "a large share of trending-repo forks come from
accounts created the same day (coordinated fork campaigns)".

We compare:
  A. trending repos (the ones that trended today)
  B. CONTROL repos: same orgs/owners but NOT on the trending list, plus
     long-established repos not related to AI at all.

For each we sample 100 newest forks and compute:
  - fraction of fork owners whose account was created within 7 / 30 / 365
    days of the fork
  - fraction of fork owners whose account has <=2 public repos (fresh
    account signature from the 11-12..11-17 corpus)
  - fraction of fork owners with 0 followers

Baseline expectation: for a mature repo, fresh-account forks should be a
small minority. If the trending set shows a much higher rate, that is
evidence of a coordinated campaign rather than organic interest.
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")

TRENDING = [
    "google-research/paper-orchestra", "Tencent/LoopForge",
    "backnotprop/plannotator", "getarcaneapp/arcane",
    "google-labs-code/stitch-skills", "elementalsouls/Claude-BugHunter",
    "obra/superpowers", "affaan-m/ECC", "cursor/plugins",
    "tradermonty/claude-trading-skills", "alibaba/open-code-review",
    "we-promise/sure", "anthropics/skills", "addyosmani/agent-skills",
    "GoogleChrome/modern-web-guidance-src",
]

CONTROL = [
    # same ecosystem, but not trending today
    "sveltejs/svelte", "jingyaogong/minimind", "mvanhorn/last30days-skill",
    "vercel-labs/agent-browser", "ChromeDevTools/chrome-devtools-mcp",
    "dream-num/univer", "ZhuLinsen/daily_stock_analysis",
    "openai/codex-security",
    # unrelated mature repos
    "torvalds/linux", "rust-lang/rust", "golang/go",
]


def api(path, params=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    p = subprocess.run(["gh", "api", url], capture_output=True, text=True,
                       env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def days_between(a, b):
    from datetime import datetime
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    try:
        da = datetime.strptime(a, fmt)
        db = datetime.strptime(b, fmt)
        return (db - da).total_seconds() / 86400.0
    except Exception:  # noqa: BLE001
        return None


def analyse(full, n=100):
    forks = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n})
    forks = forks if isinstance(forks, list) else []
    rows = []
    for f in forks:
        o = f.get("owner") or {}
        u = api(f"users/{o.get('login')}") or {}
        created = u.get("created_at")
        forked = f.get("created_at")
        age = days_between(created, forked) if created and forked else None
        rows.append({
            "login": o.get("login"),
            "type": o.get("type"),
            "owner_created": created,
            "forked_at": forked,
            "age_days": age,
            "public_repos": u.get("public_repos"),
            "followers": u.get("followers"),
            "total_public_repos": u.get("public_repos"),
        })
    n_s = len(rows)
    if not n_s:
        return {"repo": full, "n": 0}
    le7 = sum(1 for r in rows if r["age_days"] is not None and r["age_days"] <= 7)
    le30 = sum(1 for r in rows if r["age_days"] is not None and r["age_days"] <= 30)
    le365 = sum(1 for r in rows if r["age_days"] is not None and r["age_days"] <= 365)
    le2repos = sum(1 for r in rows if (r["public_repos"] or 99) <= 2)
    zerofoll = sum(1 for r in rows if (r["followers"] or 0) == 0)
    both = sum(1 for r in rows
               if (r["public_repos"] or 99) <= 2 and (r["followers"] or 0) == 0)
    return {
        "repo": full,
        "n": n_s,
        "acct_le7d": le7, "acct_le30d": le30, "acct_le365d": le365,
        "le2repos": le2repos, "zero_followers": zerofoll,
        "le2repos_and_0foll": both,
        "rows": rows,
    }


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "trending"
    targets = TRENDING if which == "trending" else CONTROL
    out = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        for r in ex.map(analyse, targets):
            out.append(r)
            if not r["n"]:
                print(f"  {r['repo']:<44} NO DATA")
                continue
            print(f"  {r['repo']:<44} n={r['n']:<4} "
                  f"acct<=7d={r['acct_le7d']:<4} acct<=30d={r['acct_le30d']:<4} "
                  f"acct<=365d={r['acct_le365d']:<4} repos<=2={r['le2repos']:<4} "
                  f"0foll={r['zero_followers']:<4} both={r['le2repos_and_0foll']:<4}",
                  flush=True)
    with open(f"/tmp/forkctrl_{which}.json", "w") as f:
        json.dump(out, f, ensure_ascii=False)

    print(f"\n=== SUMMARY ({which}) ===")
    tot = sum(r["n"] for r in out)
    for key in ("acct_le7d", "acct_le30d", "acct_le365d", "le2repos",
                "zero_followers", "le2repos_and_0foll"):
        s = sum(r[key] for r in out)
        print(f"  {key:<22} {s}/{tot} = {100*s/tot:.1f}%" if tot else "")
    print(f"  repos sampled: {len([r for r in out if r['n']])}")
