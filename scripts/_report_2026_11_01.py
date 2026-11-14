#!/usr/bin/env python3
"""Final evidence collection for the 2026-11-01 daily report."""
import json, os, subprocess, urllib.request, urllib.error, re, sys
from datetime import datetime, timezone

ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}
SNAP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"SNAPSHOT {SNAP}")

def api(path, raw=False):
    a = ["gh","api",path]
    if raw: a += ["-H","Accept:application/vnd.github.raw"]
    r = subprocess.run(a, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode==0 else None

def j(path):
    try: return json.loads(api(path) or "null")
    except Exception: return None

def http_status(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent":"Mozilla/5.0 research"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:
        return type(e).__name__, 0

# ---------- 1. daily cohort counts ----------
print("\n=== [1] DAILY COHORTS (created: date, stars>=40) ===")
cohorts = {}
for day in ["2026-10-27","2026-10-28","2026-10-29","2026-10-30","2026-10-31","2026-11-01"]:
    q = f"search/repositories?q=created:{day}+stars:>=40&per_page=100&sort=stars"
    d = j(q) or {}
    items = d.get("items",[])
    tot = d.get("total_count",0)
    # count shell-like: readme short AND size small AND topic-less-ish
    shells = 0; small = 0; checked = 0
    for it in items:
        s = it.get("size",0)
        if s<=20: small+=1
    cohorts[day] = (tot, len(items), small)
    print(f"  {day}: total(stars>=40)={tot:<6} sampled={len(items):<4} of which size<=20KB={small}")

# ---------- 2. 10-31 farm detail ----------
print("\n=== [2] 2026-10-31 FARM DETAIL ===")
q = "search/repositories?q=created:2026-10-31+stars:>=100&per_page=100&sort=created"
d = j(q) or {}
items = d.get("items",[])
print(f"  total(stars>=100)={d.get('total_count')}")
star_vals = sorted({it['stargazers_count'] for it in items})
print(f"  distinct star values (first 100): {star_vals}")
times = sorted(it['created_at'] for it in items)
print(f"  creation window: {times[0]} .. {times[-1]}")
for it in items[:8]:
    print(f"    {it['created_at']} {it['stargazers_count']}⭐ {it['forks_count']}f size={it['size']}KB {it['full_name']}")

# ---------- 3. battery-peek smoking gun ----------
print("\n=== [3] SMOKING GUN: Yugiri-AO/battery-peek first-commit README vs current ===")
full="Yugiri-AO/battery-peek"
meta=j(f"repos/{full}") or {}
print(f"  created_at={meta.get('created_at')} pushed_at={meta.get('pushed_at')} size={meta.get('size')}KB stars={meta.get('stargazers_count')}")
commits=j(f"repos/{full}/commits?per_page=100") or []
if commits:
    first=commits[-1]; last=commits[0]
    print(f"  oldest commit: {first['commit']['author']['date']} {first['sha'][:10]} {first['commit']['message'][:70]!r}")
    print(f"  newest commit: {last['commit']['author']['date']} {last['sha'][:10]} {last['commit']['message'][:70]!r}")
    for label, sha in (("FIRST", first["sha"]), ("CURRENT", last["sha"])):
        t=j(f"repos/{full}/contents/README.md?ref={sha}") or {}
        raw=api(f"repos/{full}/contents/README.md?ref={sha}", raw=True) or ""
        urls=sorted(set(re.findall(r"https?://[a-zA-Z0-9._:/-]+", raw)))
        pay=[u for u in urls if not any(k in u for k in ("github.com","shields.io","img.shields"))]
        print(f"  {label} README bytes={len(raw)} payload-urls={pay}")
        # look for split-string construction
        for pat in ["git-software","activation-gateway","Setup.ps1","ps-activator"]:
            if pat in raw:
                idx=raw.find(pat)
                print(f"    [{pat}] context: ...{raw[max(0,idx-160):idx+120]}...".replace("\n","\\n"))

# ---------- 4. .gitignore fingerprint ----------
print("\n=== [4] .gitignore BLOB SHA FINGERPRINT across clusters ===")
def tree_blob(full, path, ref=None):
    ref = ref or "HEAD"
    t=j(f"repos/{full}/git/trees/{ref}?recursive=1") or {}
    for e in t.get("tree",[]):
        if e["path"]==path: return e.get("sha"), e.get("size")
    return None, None
for full in ["Yugiri-AO/battery-peek","darkareaminaret/MetaTrader-5-Bot","mythicassemblyladle/RX-11-Audio-Editor",
             "Pointoocupola/Hwid-Spoofer","Astralbyretake/Microsoft-Office","KnotSteersmanAtrium/Cellebrite-UFED",
             "lookoutcoxswainwhirl/Acronis","Breakunsever/Adobe-Audition"]:
    sha,size=tree_blob(full,".gitignore")
    if sha: print(f"  {full:<44} .gitignore sha={sha} size={size}")
    else:  print(f"  {full:<44} .gitignore ABSENT")

# ---------- 5. delivery endpoints ----------
print("\n=== [5] DELIVERY ENDPOINTS (status only, NO execution) ===")
for u in ["https://git-software.cc/ps/Setup.ps1","https://activation-gateway.cc/update/ps-activator",
          "https://git-software.cc/","https://activation-gateway.cc/"]:
    st,ln=http_status(u)
    print(f"  {u:<52} -> {st} ({ln} bytes fetched)")

# ---------- 6. key project metadata ----------
print("\n=== [6] KEY PROJECT METADATA ===")
KEY = ["deepseek-ai/dsh-superagent-prototype","valentderah/totk-pc-recomp","kuraeow/ultratears",
       "NotRexed/SkyboundTotk","Shagg88/COGBox","haydenschmitty/floorplan",
       "interplains/Zero-Breach-Toolkit","NyxFoundation/nyxis","joeblau/subvox",
       "FencerEngage/courier-dota2","patch-gg/pixelfx","kevinraymond/florilegium",
       "Arjun-Ingole/hop","dbreunig/nesformer"]
for full in KEY:
    m=j(f"repos/{full}")
    if not m: print(f"  {full}: 404/NOT FOUND"); continue
    lic=(m.get("license") or {}).get("spdx_id")
    print(f"  {full:<44} ⭐{m.get('stargazers_count'):<6} fork{m.get('forks_count'):<4} sub{m.get('subscribers_count'):<3} oi{m.get('open_issues_count'):<4} {m.get('language') or '-':<12} {lic} {m.get('size')}KB created={m.get('created_at')} pushed={m.get('pushed_at')}")

# ---------- 7. tracked project deltas ----------
print("\n=== [7] TRACKED PROJECT DELTAS vs 2026-10-30 report ===")
TRACK = [("deepseek-ai/DeepInfer",21823),("colinhacks/reylo",1206),("UniXNU/UniXNU",896),
         ("oosexgang/hackios-xnu-kernel",1278),("theorem-labs/oss-verify-proofs",131),
         ("xevrion/hatchzip",1678),("Snapintosh/Snapintosh",875),
         ("rddmwmddr/android-ad-cleaner",728),("songjianyang/xss-audit",393),("YoyoLin008/mcreplay",200),
         ("M-China/mcd-developer-innovation-challenge",237),("M-China/mcd-mcp-server",246)]
for full, prev in TRACK:
    m=j(f"repos/{full}")
    if not m: print(f"  {full:<44} GONE"); continue
    now=m.get("stargazers_count",0); d=now-prev
    pct = (d/prev*100) if prev else 0
    print(f"  {full:<44} {prev} -> {now} ({d:+d}, {pct:+.1f}%) pushed={m.get('pushed_at')}")

# ---------- 8. 10-30 sample repo liveness ----------
print("\n=== [8] 2026-10-30 SAMPLE REPO LIVENESS (7 paths) ===")
SAMPLE = ["quantumbladesmith/SecureBoot-DriverUnlock","RudraClinic/Windows11-Activator",
          "valentderah/totk-pc-recomp","kuraeow/ultratears","NotRexed/SkyboundTotk",
          "Shagg88/COGBox","haydenschmitty/floorplan"]
for full in SAMPLE:
    st,ln = http_status(f"https://github.com/{full}")
    print(f"  https://github.com/{full:<44} -> {st}")

# ---------- 9. name recreation ----------
print("\n=== [9] NAME RECREATION (same repo name, different owner) ===")
for name in ["SecureBoot-DriverUnlock","Windows11-Activator","Hwid-Spoofer","MetaTrader-5-Bot"]:
    q=f"search/repositories?q={name}+in:name+created:2026-10-31&per_page=5"
    d=j(q) or {}
    print(f"  '{name}' created:2026-10-31 -> total={d.get('total_count')}")
    for it in (d.get("items") or [])[:3]:
        print(f"      {it['full_name']} {it['stargazers_count']}⭐ {it['created_at']}")
print("\nDONE")
