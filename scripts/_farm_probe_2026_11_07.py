#!/usr/bin/env python3
"""Probe 2026-11-06 farm-wave READMEs for payload markers and template reuse.

Reads only public README content via the GitHub API. Nothing is executed.
"""
import json, subprocess, os, re, sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}
OUT = "/tmp/collect_1107"

URL_RE = re.compile(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+")
HINTS = ["Invoke-Expression", "irm ", "Invoke-RestMethod", "ExecutionPolicy Bypass",
         "Real-time protection", "Setup.ps1", "git-software.cc", "iwr ",
         "powershell", "cmd /c", "{{", "}}", "deploy", "environment",
         "configuration folder", "pre-configured"]

# Rebuild the cohort straight from search so we do not depend on the earlier
# background run having produced its JSON sidecar.
res = subprocess.run(["gh", "api", "-X", "GET", "search/repositories",
                      "-f", "q=created:2026-11-06 stars:>=30",
                      "-f", "sort=stars", "-f", "per_page=100"],
                     capture_output=True, text=True, env=ENV).stdout
items = json.loads(res)["items"]
small = [i for i in items if i["size"] <= 20]
json.dump([{"full_name": i["full_name"], "stars": i["stargazers_count"],
            "forks": i["forks_count"], "size": i["size"],
            "created_at": i["created_at"], "desc": i.get("description")}
           for i in items],
          open(f"{OUT}/cohort_2026-11-06.json", "w"), indent=2)
print(f"cohort total={len(items)} small(<=20KB)={len(small)}")


def readme(full):
    r = subprocess.run(["gh", "api", f"repos/{full}/readme",
                        "-H", "Accept:application/vnd.github.raw"],
                       capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def one(it):
    rd = readme(it["full_name"])
    if rd is None:
        return it, None
    hits = [h for h in HINTS if h.lower() in rd.lower()]
    urls = sorted(set(URL_RE.findall(rd)))
    import hashlib
    return it, {"len": len(rd), "hits": hits, "urls": urls[:15],
                "md5": hashlib.md5(rd.encode()).hexdigest(),
                "body": rd}


flagged, doms, bodies = [], Counter(), {}  # bodies: md5 -> count
with ThreadPoolExecutor(max_workers=8) as ex:
    for it, s in ex.map(one, small):
        if s is None:
            print(f"  DEAD {it['full_name']}")
            continue
        bodies[s["md5"]] = bodies.get(s["md5"], 0) + 1
        if s["hits"]:
            flagged.append((it["full_name"], s["hits"], s["urls"], s["len"]))
        for u in s["urls"]:
            doms[u] += 1
        print(f"  {it['full_name']:<48} stars={it['stargazers_count']:<4} "
              f"forks={it['forks_count']:<4} len={s['len']:<6} hits={s['hits']}")

print("=" * 100)
print(f"probed {len(small)} small repos; flagged={len(flagged)}")
print("--- unique README bodies (md5 -> count) ---")
for md5, c in sorted(bodies.items(), key=lambda kv: -kv[1])[:12]:
    print(f"  {md5}  x{c}")
print("--- top urls ---")
for u, c in doms.most_common(20):
    print(f"  {c:>4}  {u}")
print("--- flagged sample ---")
for n, h, u, L in flagged[:8]:
    print(f"  {n}  len={L}\n     hits={h}\n     urls={u}")

# Dump the distinct README bodies for offline inspection.
seen = set()
for it, s in [(it, None) for it in small]:
    pass
print("\n--- writing distinct bodies ---")
md5s = {}
with ThreadPoolExecutor(max_workers=8) as ex:
    for it, s in ex.map(one, small):
        if s is None:
            continue
        if s["md5"] not in md5s:
            md5s[s["md5"]] = (it["full_name"], s["body"])
for i, (md5, (name, body)) in enumerate(md5s.items()):
    p = f"{OUT}/farm_body_{i}_{md5[:8]}.md"
    open(p, "w").write(body)
    print(f"  {p}  <- {name}")
