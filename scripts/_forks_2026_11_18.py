#!/usr/bin/env python3
"""Targeted paper-orchestra forensics: fork timeline, issue quality,
stargazer timeline, and comparison against a control group of thin repos
that trended today.

The comparison target: does the fork/star ratio and fork-creation-time
clustering of paper-orchestra look organic or coordinated?
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


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
        return None, p.stderr.strip()[:300]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:300]}"


def fork_forensics(full, n=100):
    forks, _ = api(f"repos/{full}/forks", {"sort": "newest", "per_page": n})
    forks = forks if isinstance(forks, list) else []
    dates = sorted(f.get("created_at") for f in forks if f.get("created_at"))
    owners = [((f.get("owner") or {}).get("login"),
               (f.get("owner") or {}).get("type")) for f in forks]
    # per-day histogram
    days = Counter(d[:10] for d in dates)
    # hour-of-day concentration
    hours = Counter(d[11:13] for d in dates)
    return {
        "repo": full,
        "n_forks_listed": len(forks),
        "earliest": dates[0] if dates else None,
        "latest": dates[-1] if dates else None,
        "days": dict(sorted(days.items(), reverse=True)[:10]),
        "hours": dict(sorted(hours.items())),
        "owner_types": dict(Counter(t for _, t in owners)),
        "owners": [o for o, _ in owners[:20]],
    }


def issue_quality(full, n=30):
    issues, _ = api(f"repos/{full}/issues", {"state": "all", "per_page": n})
    issues = issues if isinstance(issues, list) else []
    rows = []
    for i in issues:
        body = (i.get("body") or "")
        rows.append({
            "n": i.get("number"),
            "title": (i.get("title") or "")[:100],
            "state": i.get("state"),
            "created": i.get("created_at"),
            "comments": i.get("comments"),
            "user": (i.get("user") or {}).get("login"),
            "body_len": len(body),
            "has_traceback": "Traceback" in body,
            "has_code": "```" in body,
        })
    return {"repo": full, "n_issues": len(issues), "rows": rows}


def star_timeline(full, n=100):
    stars, err = api(f"repos/{full}/stargazers", {"per_page": n},
                     headers=["Accept: application/vnd.github.star+json"])
    if not isinstance(stars, list):
        return {"repo": full, "error": err}
    days = Counter(s.get("starred_at", "")[:10] for s in stars if s.get("starred_at"))
    return {
        "repo": full,
        "n_listed": len(stars),
        "days": dict(sorted(days.items(), reverse=True)[:12]),
        "users": [(s.get("starred_at", "")[:10], (s.get("user") or {}).get("login"))
                  for s in stars[:25]],
    }


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "forks"):
        print("========== FORK forensics (paper-orchestra vs controls) ==========")
        targets = ["google-research/paper-orchestra", "Tencent/LoopForge",
                   "backnotprop/plannotator", "getarcaneapp/arcane",
                   "google-labs-code/stitch-skills", "elementalsouls/Claude-BugHunter"]
        with ThreadPoolExecutor(max_workers=4) as ex:
            for r in ex.map(fork_forensics, targets):
                print(f"\n--- {r['repo']} --- forks_listed={r['n_forks_listed']} "
                      f"window={r['earliest']} .. {r['latest']}")
                print(f"    owner_types={r['owner_types']}")
                print(f"    by_day={r['days']}")
                print(f"    by_hour={r['hours']}")
                print(f"    owners={r['owners'][:12]}")

    if which in ("all", "issues"):
        print("\n\n========== ISSUE quality ==========")
        for t in ["google-research/paper-orchestra", "Tencent/LoopForge"]:
            r = issue_quality(t)
            print(f"\n--- {r['repo']} --- n_issues={r['n_issues']}")
            for x in r["rows"][:14]:
                print(f"    #{x['n']:<4} {x['state']:<6} c={x['comments']:<3} "
                      f"len={x['body_len']:<6} tb={int(x['has_traceback'])} "
                      f"code={int(x['has_code'])} {x['user']:<22} {x['title']}")

    if which in ("all", "stars"):
        print("\n\n========== STARGAZER timeline (star+json) ==========")
        for t in ["google-research/paper-orchestra", "Tencent/LoopForge",
                  "getarcaneapp/arcane"]:
            r = star_timeline(t)
            print(f"\n--- {r['repo']} ---")
            if r.get("error"):
                print(f"    ERROR: {r['error']}")
            else:
                print(f"    n_listed={r['n_listed']} by_day={r['days']}")
                print(f"    sample={r['users'][:15]}")
