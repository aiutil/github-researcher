#!/usr/bin/env python3
"""Re-measure the tracked cohort for 2026-11-07 and diff against the 11-06 snapshot."""
import json, subprocess, os, re, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}
PREV = "/tmp/collect_1106/tracked_1106.json"
OUT = "/tmp/collect_1107/tracked_1107.json"

TRACKED = json.load(open(PREV))


def api(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    try:
        return json.loads(api(path) or "null")
    except Exception:
        return None


def ncommits(full):
    h = subprocess.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"],
                       capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    return int(m.group(1)) if m else 1


cur = {}
for full, p in TRACKED.items():
    r = japi(f"repos/{full}")
    if not r:
        print(f"  DEAD {full}")
        continue
    d = {
        "stars": r["stargazers_count"], "forks": r["forks_count"],
        "subs": r["subscribers_count"], "oi": r["open_issues_count"],
        "size": r["size"], "lic": (r.get("license") or {}).get("spdx_id"),
        "created": r["created_at"], "pushed": r["pushed_at"],
        "commits": ncommits(full),
    }
    rel = japi(f"repos/{full}/releases?per_page=100")
    d["rel"] = len(rel) if isinstance(rel, list) else None
    contrib = japi(f"repos/{full}/contributors?per_page=100")
    d["contrib"] = len(contrib) if isinstance(contrib, list) else None
    cur[full] = d

    ds = d["stars"] - p["stars"]
    dc = d["commits"] - p.get("commits", 0)
    dr = (d["rel"] or 0) - (p.get("rel") or 0)
    moved = "PUSHED" if d["pushed"] != p.get("pushed") else "no-push"
    print(f"  {full:<45} stars {p['stars']:>6}->{d['stars']:>6} ({ds:+5d})  "
          f"forks {p['forks']:>4}->{d['forks']:>4}  subs {p['subs']:>3}->{d['subs']:>3}  "
          f"oi {p['oi']:>4}->{d['oi']:>4}  commits {p.get('commits',0):>4}->{d['commits']:>4} ({dc:+d})  "
          f"rel {p.get('rel',0):>3}->{d['rel']} ({dr:+d})  {moved}")

json.dump(cur, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"\nwrote {OUT}")
