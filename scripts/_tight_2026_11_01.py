#!/usr/bin/env python3
"""Tight, unambiguous payload census + battery-peek payload-introduction diff."""
import json, os, re, subprocess, urllib.request, urllib.error

ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}

def api(path, raw=False):
    a = ["gh","api",path]
    if raw: a += ["-H","Accept:application/vnd.github.raw"]
    r = subprocess.run(a, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode==0 else None

def j(path):
    try: return json.loads(api(path) or "null")
    except Exception: return None

# Only unambiguous delivery markers: no "bypass"/"Windows Security" false positives.
DELIV = ["git-software", "activation-gateway", "Setup.ps1", "ps-activator",
         "Invoke-Expression", "DownloadString", "scriptblock", "irm http"]

def readme(full): return api(f"repos/{full}/readme", raw=True) or ""
def hits(t): return [p for p in DELIV if p.lower() in t.lower()]

print("=== [1] TIGHT payload census (unambiguous delivery markers only) ===")
for day in ["2026-10-28","2026-10-29","2026-10-30","2026-10-31"]:
    items = (j(f"search/repositories?q=created:{day}+stars:>=40&per_page=60&sort=stars") or {}).get("items",[])
    n=0; hit=0; ex=[]
    for it in items:
        rd=readme(it["full_name"])
        if not rd: continue
        n+=1
        h=hits(rd)
        if h:
            hit+=1
            if len(ex)<2: ex.append((it["full_name"], h, it.get("size")))
    print(f"  {day}: sampled={n} payload_hit={hit} ({hit*100//max(n,1)}%)")
    for e in ex: print(f"      eg {e[0]} size={e[2]}KB markers={e[1]}")

print("\n=== [2] 10-31 farm: split-construction exact text (2 samples) ===")
for full in ["darkareaminaret/MetaTrader-5-Bot","Astralbyretake/Microsoft-Office"]:
    rd = readme(full)
    print(f"  --- {full}  (readme {len(rd)}B)")
    for ln in rd.splitlines():
        if "git-software" in ln or "activation-gateway" in ln:
            print(f"      {ln.strip()[:230]}")
            break

print("\n=== [3] battery-peek: when did the payload appear? (per-commit README) ===")
cs = j("repos/Yugiri-AO/battery-peek/commits?per_page=100") or []
prev=None
for cm in reversed(cs):
    sha=cm["sha"]; msg=cm["commit"]["message"]; date=cm["commit"]["author"]["date"]
    rd = api(f"repos/Yugiri-AO/battery-peek/contents/README.md?ref={sha}", raw=True)
    if rd is None:
        rd = ""
    h = hits(rd)
    state = ("PAYLOAD:"+",".join(h)) if h else ("README %dB"%len(rd) if rd else "NO README")
    if state != prev:
        print(f"  {date} {sha[:8]} {msg[:40]!r:<45} -> {state}")
        prev = state
print(f"  total commits={len(cs)}")

print("\n=== [4] battery-peek: diff of 'Update installation command' commit ===")
d = j("repos/Yugiri-AO/battery-peek/commits/6f64211764") or {}
for f in d.get("files",[]):
    print(f"  file {f['filename']} status={f['status']} +{f['additions']}/-{f['deletions']}")
    patch = f.get("patch","")
    for ln in patch.splitlines():
        if ln.startswith(("+","-")) and ("irm" in ln or "iex" in ln or "http" in ln or "software" in ln or "gateway" in ln):
            print(f"      {ln[:210]}")

print("\n=== [5] courier-dota2 'bypass' context (false-positive check) ===")
rd = readme("FencerEngage/courier-dota2")
for ln in rd.splitlines():
    if "bypass" in ln.lower():
        print(f"   {ln.strip()[:190]}")

print("\n=== [6] legit project spot-checks: contributors/releases/subs ===")
for full in ["rddmwmddr/android-ad-cleaner","interplains/Zero-Breach-Toolkit","valentderah/totk-pc-recomp",
             "deepseek-ai/dsh-superagent-prototype","NyxFoundation/nyxis","haydenschmitty/floorplan"]:
    contrib = j(f"repos/{full}/contributors?per_page=100") or []
    rel = j(f"repos/{full}/releases?per_page=100") or []
    m = j(f"repos/{full}") or {}
    print(f"  {full}: contributors={len(contrib)} releases={len(rel)} subs={m.get('subscribers_count')} "
          f"oi={m.get('open_issues_count')} topics={len(m.get('topics') or [])}")
    if rel:
        print(f"      latest release: {rel[0].get('tag_name')} assets={len(rel[0].get('assets') or [])} published={rel[0].get('published_at')}")
