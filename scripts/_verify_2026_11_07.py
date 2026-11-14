#!/usr/bin/env python3
"""Fork-cadence analysis + stub-cluster verification for the 2026-11-07 daily."""
import json, subprocess, os, datetime, statistics

ENV = {**os.environ, "HOME": "/home/lohasle",
       "GH_TOKEN": subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                                  env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()}


def api(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def forks(full, pages=5):
    out = []
    for p in range(1, pages + 1):
        d = api(f"repos/{full}/forks?per_page=100&page={p}")
        if not d:
            break
        items = json.loads(d)
        if not items:
            break
        out += items
        if len(items) < 100:
            break
    return out


print("=== FORK CADENCE (machine-verified inter-arrival) ===")
for full in ["PulverizeLink/roblox-performance-tool",
             "HerdBuilderEstimate/roblox-studio-mcp",
             "JenkinWoo/sheeridVerify"]:
    fs = forks(full)
    ts = sorted(datetime.datetime.fromisoformat(f["created_at"].replace("Z", "")) for f in fs)
    deltas = [(ts[i + 1] - ts[i]).total_seconds() for i in range(len(ts) - 1)]
    if not deltas:
        continue
    d = sorted(deltas)
    print(f"\n{full}: n_forks={len(fs)} span={ts[0].isoformat()} .. {ts[-1].isoformat()}")
    print(f"  median_delta={statistics.median(d):.1f}s  min={min(d):.1f}s  max={max(d):.1f}s  "
          f"p10={d[len(d)//10]:.1f}s  p90={d[len(d)*9//10]:.1f}s")
    print(f"  deltas<=10s: {sum(1 for x in deltas if x <= 10)}/{len(deltas)} = "
          f"{100*sum(1 for x in deltas if x<=10)/len(deltas):.1f}%")

print("\n=== STUB CLUSTER: does main.py import a module that does not exist? ===")
for full, files in [
    ("PulverizeLink/roblox-performance-tool", ["main.py", "utils.py", "helpers.py", "config.py"]),
    ("Lowbetweentrim/crypto-portfolio-tracker", ["main.py", "utils.py", "helpers.py", "config.py"]),
    ("phaseboulderfetter/discord-quest-completer", ["main.py", "utils.py", "helpers.py", "config.py"]),
    ("HerdBuilderEstimate/roblox-studio-mcp", ["utils.py", "config.py"]),
]:
    print(f"\n{full}")
    for f in files:
        d = api(f"repos/{full}/contents/{f}")
        if not d:
            print(f"  {f:<12} ABSENT (404)")
            continue
        j = json.loads(d)
        body = api(f"repos/{full}/contents/{f}")
        r2 = subprocess.run(["gh", "api", f"repos/{full}/contents/{f}",
                             "-H", "Accept:application/vnd.github.raw"],
                            capture_output=True, text=True, env=ENV).stdout
        imp = [ln.strip() for ln in r2.splitlines() if ln.strip().startswith(("from ", "import "))]
        print(f"  {f:<12} size={j.get('size')} imports={imp}")

print("\n=== interplains repo existence check (broken card target) ===")
for r in ["interplains/Zero-Breach-Toolkit", "interplains/zero-breach"]:
    d = api(f"repos/{r}")
    if not d:
        print(f"  {r}: NOT FOUND")
        continue
    j = json.loads(d)
    print(f"  {r}: stars={j['stargazers_count']} forks={j['forks_count']} subs={j['subscribers_count']} "
          f"oi={j['open_issues_count']} lang={j['language']} lic={(j.get('license') or {}).get('spdx_id')} "
          f"size={j['size']}KB created={j['created_at']} pushed={j['pushed_at']} "
          f"topics={j.get('topics')}")
