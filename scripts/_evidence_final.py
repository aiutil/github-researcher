#!/usr/bin/env python3
"""Final evidence: farm channel quantification + default-branch vs all-branch commit counts."""
import json, subprocess, os, re

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def japi(path):
    r = api(path)
    try:
        return json.loads(r) if r else None
    except Exception:
        return None


def ncommits(full, sha=None):
    p = f"repos/{full}/commits?per_page=1" + (f"&sha={sha}" if sha else "")
    h = subprocess.run(["gh", "api", "-i", p], capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    return int(m.group(1)) if m else 1


print("### A) 10-30 farm: delivery channels over the 100-repo size<=20 cohort")
names = [l.strip() for l in open("/tmp/farm30.txt") if l.strip()]
ps_chan = tel_chan = both = neither = 0
for full in names[:60]:
    rd = api(f"repos/{full}/readme", raw=True) or ""
    p = ("git-software.cc" in rd) or ("Invoke-Expression" in rd)
    t = "telegra" in rd.lower()
    if p and t:
        both += 1
    elif p:
        ps_chan += 1
    elif t:
        tel_chan += 1
    else:
        neither += 1
print(f"  sampled 60 of {len(names)}: powershell-payload={ps_chan} telegraph-only={tel_chan} both={both} neither={neither}")

print("\n### B) default branch vs all branches (commit-count methodology)")
for full in ["kuraeow/ultratears", "valentderah/totk-pc-recomp", "NotRexed/SkyboundTotk",
             "haydenschmitty/floorplan", "Shagg88/COGBox", "interplains/Zero-Breach-Toolkit",
             "dbreunig/nesformer", "wangzan101/Mika", "tapoooooty/hypergrad",
             "soimy/c3rb3r-rescue", "heydamir/unslop", "Djihads80/Eglantine"]:
    r = japi(f"repos/{full}") or {}
    br = japi(f"repos/{full}/branches") or []
    defb = r.get("default_branch")
    per = {b["name"]: ncommits(full, b["name"]) for b in br}
    tot = sum(per.values())
    print(f"  {full:<34} default={defb:<8} default_commits={ncommits(full):<6} branches={per} sum={tot}")

print("\n### C) licenses: spdx vs LICENSE file first line")
for full in ["kuraeow/ultratears", "valentderah/totk-pc-recomp", "NotRexed/SkyboundTotk",
             "haydenschmitty/floorplan", "Shagg88/COGBox", "dbreunig/nesformer",
             "wangzan101/Mika", "tapoooooty/hypergrad", "soimy/c3rb3r-rescue",
             "heydamir/unslop", "Djihads80/Eglantine"]:
    r = japi(f"repos/{full}") or {}
    spdx = (r.get("license") or {}).get("spdx_id")
    lic = api(f"repos/{full}/contents/LICENSE", raw=True) or api(f"repos/{full}/contents/LICENSE.md", raw=True) or ""
    first = " ".join(lic.split()[:6]) if lic else "(no LICENSE file)"
    flag = ""
    ls = lic.lower()
    if spdx == "MIT" and "general public license" in ls:
        flag = "  <<< MISMATCH"
    if spdx in (None, "NOASSERTION") and "mit license" in ls:
        flag = "  <<< MISMATCH"
    print(f"  {full:<34} spdx={str(spdx):<14} file='{first[:60]}'{flag}")
