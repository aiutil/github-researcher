#!/usr/bin/env python3
"""Compact prep: formats, existence, branch counts, totals."""
import json, os, re, subprocess, glob, yaml

R = "/home/lohasle/aiutil-github-researcher"
os.chdir(R)
ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}
def j(p):
    r = subprocess.run(["gh","api",p],capture_output=True,text=True,env=ENV)
    try: return json.loads(r.stdout) if r.returncode==0 else None
    except Exception: return None

print("### profile existence")
for f in ["dsh-superagent-prototype","battery-peek","floorplan","totk-pc-recomp","ultratears",
          "cogbox","zero-breach","zero-breach-toolkit","fps-optimizer-universal-game-performance-booster-2026",
          "fps-optimizer-2026","dsh-superagent"]:
    p=f"projects/{f}.md"
    print(f"  {'EXIST' if os.path.exists(p) else 'new  '} {p}")

print("\n### fuzzy-match check (validate.py rule)")
def slugify(n):
    clean = re.sub(r'\s*\([^)]*\)','',n).strip()
    return re.sub(r'[^a-z0-9]+','-',clean.lower()).strip('-')
def keyify(s): return s.lower().replace('-','').replace(' ','').replace('_','').replace('.','')
pf_keys = {os.path.basename(p)[:-3]: keyify(os.path.basename(p)[:-3]) for p in glob.glob("projects/*.md")}
for n in ["deepseek-ai/dsh-superagent-prototype","valentderah/totk-pc-recomp","haydenschmitty/floorplan",
          "kuraeow/ultratears","Shagg88/COGBox","interplains/Zero-Breach-Toolkit","Yugiri-AO/battery-peek",
          "QuantumBladesmith/FPS-Optimizer-Universal-Game-Performance-Booster-2026"]:
    ck = keyify(n); hit = None
    for k,v in pf_keys.items():
        if ck in v or v in ck: hit=k; break
    print(f"  {n[:60]:62s} -> {hit}")

print("\n### generate_readme load_projects")
src = open("scripts/generate_readme.py").read()
m = re.search(r'def load_projects.*?(?=\ndef )', src, re.S)
print(m.group(0)[:1400] if m else "NOT FOUND")
m2 = re.search(r'def load_dailies.*?(?=\ndef )', src, re.S)
print("\n### load_dailies\n", (m2.group(0)[:900] if m2 else "NF"))

print("\n### generate_pages: project page filename logic")
gs = open("docs/generate_pages.py").read()
for pat in [r'def make_slug.*?(?=\ndef )', r'def project_page.*?(?=\ndef )']:
    mm = re.search(pat, gs, re.S)
    print("---", pat[:30], "\n", (mm.group(0)[:900] if mm else "NOT FOUND"))

print("\n### branch commit counts")
for r,b in [("kuraeow/ultratears","dev"),("kuraeow/ultratears","main"),
            ("valentderah/totk-pc-recomp","dev"),("valentderah/totk-pc-recomp","main"),
            ("Shagg88/COGBox","main"),("interplains/Zero-Breach-Toolkit","main")]:
    c = j(f"repos/{r}/commits?sha={b}&per_page=100") or []
    if isinstance(c, dict): c=[]
    print(f"  {r}@{b}: commits_page={len(c)} first={c[0]['commit']['author']['date'] if c else '-'} last={c[-1]['commit']['author']['date'] if c else '-'}")

print("\n### archive star total (all profiles)")
tot=0; n=0
for p in glob.glob("projects/*.md"):
    txt=open(p,encoding="utf-8").read()
    if not txt.startswith('---'): continue
    fm=yaml.safe_load(txt.split('---',2)[1]) or {}
    s=fm.get('stars')
    if s:
        mm=re.search(r'([\d,]+)',str(s))
        if mm: tot+=int(mm.group(1).replace(',','')); n+=1
print(f"  profiles_with_stars={n} sum={tot} -> {tot/1000:.1f}k")

print("\n### daily-report.md head")
print("".join(open("daily-report.md",encoding="utf-8").readlines()[:14]))
print("\n### trend-index.md head")
print("".join(open("indexes/trend-index.md",encoding="utf-8").readlines()[:26])[:2200])
print("\n### 10-30 body headings")
print("".join(l for l in open("daily/2026-10-30.md",encoding="utf-8").readlines() if re.match(r'^#{1,3} ',l)))
