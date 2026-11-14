#!/usr/bin/env python3
"""Final verification for the 2026-11-01 daily report.

Vets candidate key_projects for payload strings, and re-census the
2026-10-29 / 10-30 / 10-31 cohorts for current payload hits.
Static inspection only -- nothing fetched from the delivery endpoints is executed.
"""
import json, os, re, subprocess, urllib.request, urllib.error
from datetime import datetime, timezone

ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}
SNAP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"SNAPSHOT {SNAP}")

PAY = ["git-software", "activation-gateway", "Setup.ps1", "ps-activator",
       "Invoke-Expression", "irm http", "iex(", "WebClient", "DownloadString",
       "scriptblock", "pause real-time", "Windows Security", "暂停", "bypass"]

def api(path, raw=False):
    a = ["gh","api",path]
    if raw: a += ["-H","Accept:application/vnd.github.raw"]
    r = subprocess.run(a, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode==0 else None

def j(path):
    try: return json.loads(api(path) or "null")
    except Exception: return None

def readme(full):
    return api(f"repos/{full}/readme", raw=True) or ""

def payload_hits(text):
    return sorted({p for p in PAY if p.lower() in text.lower()})

def files_of(full):
    t = j(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    return t.get("tree", []), t.get("truncated")

# ------------------------------------------------------------------
print("\n=== [A] VET CANDIDATE key_projects (payload strings? file count? commits?) ===")
CANDS = ["deepseek-ai/dsh-superagent-prototype","rddmwmddr/android-ad-cleaner",
         "interplains/Zero-Breach-Toolkit","valentderah/totk-pc-recomp",
         "haydenschmitty/floorplan","kuraeow/ultratears","NotRexed/SkyboundTotk",
         "Shagg88/COGBox","NyxFoundation/nyxis","patch-gg/pixelfx",
         "kevinraymond/florilegium","Arjun-Ingole/hop","joeblau/subvox",
         "FencerEngage/courier-dota2","dbreunig/nesformer"]
for full in CANDS:
    m = j(f"repos/{full}") or {}
    rd = readme(full)
    hits = payload_hits(rd)
    tree, trunc = files_of(full)
    blobs = [e for e in tree if e.get("type")=="blob"]
    commits = j(f"repos/{full}/commits?per_page=1") or []
    ncommits = 1
    r = subprocess.run(["gh","api",f"repos/{full}/commits?per_page=1","-i"],capture_output=True,text=True,env=ENV)
    mm = re.search(r'page=(\d+)>; rel="last"', r.stdout)
    if mm: ncommits = int(mm.group(1))
    print(f"  {full}")
    print(f"     ⭐{m.get('stargazers_count')} ⑂{m.get('forks_count')} subs{m.get('subscribers_count')} oi{m.get('open_issues_count')} "
          f"{m.get('language') or '-'} {(m.get('license') or {}).get('spdx_id')} {m.get('size')}KB commits={ncommits}")
    print(f"     files={len(blobs)} truncated={trunc} readme={len(rd)}B PAYLOAD_HITS={hits if hits else 'NONE'}")

# ------------------------------------------------------------------
print("\n=== [B] COHORT CENSUS: current payload-hit rate (sorted by stars, top 60/day) ===")
for day in ["2026-10-29","2026-10-30","2026-10-31"]:
    q = f"search/repositories?q=created:{day}+stars:>=40&per_page=60&sort=stars"
    items = (j(q) or {}).get("items", [])
    hit = 0; checked = 0; small = 0; hit_small = 0
    for it in items:
        full = it["full_name"]
        rd = readme(full)
        if not rd: continue
        checked += 1
        h = payload_hits(rd)
        issmall = it.get("size",0) <= 20
        if issmall: small += 1
        if h:
            hit += 1
            if issmall: hit_small += 1
    print(f"  {day}: sampled={len(items)} readme_ok={checked} payload_hit={hit}/{checked} "
          f"({hit*100//max(checked,1)}%) | size<=20KB={small} of which payload_hit={hit_small}")

# ------------------------------------------------------------------
print("\n=== [C] 2026-10-31 farm: structural fingerprint sample ===")
q = "search/repositories?q=created:2026-10-31+stars:>=200+size:<=5&per_page=40&sort=created"
items = (j(q) or {}).get("items", [])
print(f"  sampled={len(items)}")
sizes=set(); stars=set(); forks=set(); subs=set(); fcount=set(); hit=0
for it in items:
    full=it["full_name"]
    rd=readme(full)
    if payload_hits(rd): hit+=1
    tree,_=files_of(full)
    fcount.add(len([e for e in tree if e.get("type")=="blob"]))
    sizes.add(it.get("size")); stars.add(it.get("stargazers_count"))
    forks.add(it.get("forks_count")); subs.add(it.get("subscribers_count"))
print(f"  distinct repo sizes(KB): {sorted(sizes)}")
print(f"  distinct star values: {sorted(stars)}")
print(f"  distinct fork values: {sorted(forks)}")
print(f"  distinct subscriber values: {sorted(subs)}")
print(f"  distinct file counts: {sorted(fcount)}")
print(f"  payload hits: {hit}/{len(items)}")
times=sorted(it['created_at'] for it in items)
print(f"  creation window: {times[0]} .. {times[-1]}")

# ------------------------------------------------------------------
print("\n=== [D] endpoint final state ===")
for u in ["https://git-software.cc/","https://git-software.cc/ps/Setup.ps1",
          "https://activation-gateway.cc/update/ps-activator"]:
    req = urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0 research"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(1200)
            print(f"  {u} -> {r.status} ct={r.headers.get('Content-Type')} srv={r.headers.get('Server')} first120={body[:120]!r}")
    except urllib.error.HTTPError as e:
        print(f"  {u} -> HTTP {e.code}")
    except Exception as e:
        print(f"  {u} -> {type(e).__name__}: {e}")

print("\n=== [E] battery-peek: payload install commit ===")
c = j("repos/Yugiri-AO/battery-peek/commits?per_page=100") or []
for cm in c:
    msg = cm["commit"]["message"]
    if "install" in msg.lower() or "update" in msg.lower():
        print(f"  {cm['commit']['author']['date']} {cm['sha'][:10]} {msg!r}")
print(f"  total commits={len(c)}")
print("\nDONE")
