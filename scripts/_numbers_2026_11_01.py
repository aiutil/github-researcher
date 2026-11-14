#!/usr/bin/env python3
"""Final numbers for 2026-11-01 key_projects candidates."""
import json, os, subprocess, re

ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}

def api(p, raw=False):
    a = ["gh","api",p] + (["-H","Accept:application/vnd.github.raw"] if raw else [])
    r = subprocess.run(a, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None

def j(p):
    try: return json.loads(api(p) or "null")
    except Exception: return None

REPOS = [
 "deepseek-ai/dsh-superagent-prototype",
 "valentderah/totk-pc-recomp",
 "haydenschmitty/floorplan",
 "Shagg88/COGBox",
 "kuraeow/ultratears",
 "interplains/zero-breach",
 "Yugiri-AO/battery-peek",
 "QuantumBladesmith/FPS-Optimizer-Universal-Game-Performance-Booster-2026",
 "TinsmithConsole60/Roblox-Account-Manager-Multi-Account-Tool-2026",
 "redjellyfishrampart/Bunny-Hop-Script-Auto-Bhop-Movement-Tool-2026",
]

print("="*100)
for r in REPOS:
    m = j(f"repos/{r}")
    if not m:
        print(f"{r}: API FAIL"); continue
    t = j(f"repos/{r}/git/trees/HEAD?recursive=1") or {}
    blobs = [e for e in t.get("tree",[]) if e.get("type")=="blob"]
    langs = j(f"repos/{r}/languages") or {}
    commits = j(f"repos/{r}/commits?per_page=1")
    ncomm = len(j(f"repos/{r}/commits?per_page=100") or [])
    branches = j(f"repos/{r}/branches?per_page=100") or []
    print(f"\n### {r}")
    print(f"  stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} watchers={m.get('watchers_count')}")
    print(f"  size={m.get('size')}KB lang={m.get('language')} created={m.get('created_at')} pushed={m.get('pushed_at')} updated={m.get('updated_at')}")
    print(f"  openissues={m.get('open_issues_count')} license={(m.get('license') or {}).get('spdx_id')} topics={m.get('topics')}")
    print(f"  files={len(blobs)} langs={ {k:v for k,v in list(langs.items())[:6]} }")
    print(f"  branches={[b['name'] for b in branches][:8]} commits_on_default_page={ncomm}")
    print(f"  desc={m.get('description')}")
    print(f"  homepage={m.get('homepage')}")
    # README payload scan
    rd = api(f"repos/{r}/readme", raw=True) or ""
    urls = sorted(set(re.findall(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+", rd)))
    hosts = sorted(set(u.split("/")[2] for u in urls))
    print(f"  readme_bytes={len(rd)} hosts={hosts[:12]}")
    for kw in ["irm ","iex ","Invoke-WebRequest","download","Download","telegraph","mediafire","discord.gg","bit.ly","tinyurl"]:
        if kw in rd:
            print(f"    !! keyword {kw!r} x{rd.count(kw)}")
print("="*100)
