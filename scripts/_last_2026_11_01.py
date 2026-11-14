#!/usr/bin/env python3
import json, os, subprocess, datetime
ENV = {**os.environ, "GH_TOKEN": subprocess.run(["gh","auth","token"],capture_output=True,text=True).stdout.strip(), "HOME":"/home/lohasle"}
def j(p):
    r = subprocess.run(["gh","api",p],capture_output=True,text=True,env=ENV)
    try: return json.loads(r.stdout) if r.returncode==0 else None
    except Exception: return None
def api(p, raw=False):
    a=["gh","api",p]+(["-H","Accept:application/vnd.github.raw"] if raw else [])
    r=subprocess.run(a,capture_output=True,text=True,env=ENV); return r.stdout if r.returncode==0 else None

print("TODAY_LOCAL:", datetime.datetime.now().isoformat(), "| UTC:", datetime.datetime.utcnow().isoformat())
for r in ["deepseek-ai/dsh-superagent-prototype","haydenschmitty/floorplan","valentderah/totk-pc-recomp","Shagg88/COGBox","kuraeow/ultratears","interplains/zero-breach","Yugiri-AO/battery-peek"]:
    m=j(f"repos/{r}") or {}
    c=j(f"repos/{r}/commits?per_page=100") or []
    b=j(f"repos/{r}/branches?per_page=100") or []
    t=j(f"repos/{r}/git/trees/HEAD?recursive=1") or {}
    blobs=[e for e in t.get("tree",[]) if e.get("type")=="blob"]
    print(f"{r}\n   stars={m.get('stargazers_count')} forks={m.get('forks_count')} subs={m.get('subscribers_count')} oi={m.get('open_issues_count')} size={m.get('size')}KB lang={m.get('language')} created={m.get('created_at')} pushed={m.get('pushed_at')} license={(m.get('license') or {}).get('spdx_id')}")
    print(f"   commits_default_branch={len(c)} branches={[x['name'] for x in b]} blobs={len(blobs)} desc={m.get('description')}")
    print(f"   topics={m.get('topics')}")
print("\n== dsh README ==")
print((api("repos/deepseek-ai/dsh-superagent-prototype/readme", raw=True) or "")[:2600])
