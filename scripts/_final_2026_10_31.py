#!/usr/bin/env python3
"""Final verification: 10-29 farm cohort content, ultratears dev history, tracked-project deltas."""
import json, subprocess, os, re, sys

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


print("### 1) 10-29 cohort: how many are size<=20 vs real content? (sample 40, all stars>=40)")
res = japi("search/repositories?q=created:2026-10-29+stars:>=40&per_page=40")
items = res["items"]
sizes = [i["size"] for i in items]
print(f"  sampled {len(items)}; size<=20KB: {sum(1 for s in sizes if s<=20)}; size>20KB: {sum(1 for s in sizes if s>20)}")
print(f"  size distribution: min={min(sizes)} median={sorted(sizes)[len(sizes)//2]} max={max(sizes)}")
payload = 0
checked = 0
for i in items[:40]:
    rd = api(f"repos/{i['full_name']}/readme", raw=True) or ""
    if not rd:
        continue
    checked += 1
    if "git-software.cc" in rd or "Invoke-Expression" in rd:
        payload += 1
print(f"  READMEs checked={checked}; containing git-software.cc payload = {payload}")

print("\n### 2) ultratears dev-branch earliest commits")
dev = japi("repos/kuraeow/ultratears/commits?sha=dev&per_page=100")
if dev:
    dates = [c["commit"]["author"]["date"] for c in dev]
    print(f"  dev page1 newest={dates[0]} oldest_on_page={dates[-1]} total_pages=87")
    print(f"  dev commits on 10-29: {sum(1 for d in dates if d.startswith('2026-10-29'))} on 10-30: {sum(1 for d in dates if d.startswith('2026-10-30'))}")

print("\n### 3) tracked-project day-over-day deltas")
TRACKED = [
    "unclebob/ub-mode", "rddmwmddr/android-ad-cleaner",
    "DenisSergeevitch/ex-ussr-kinship-research", "trailofbits/brotli-checker",
    "YoyoLin008/mcreplay", "songjianyang/xss-audit", "NyxFoundation/nyxis",
    "deepseek-ai/DeepInfer", "colinhacks/reylo", "Snapintosh/Snapintosh",
    "AxiomMath/CFSG", "patch-gg/anymove", "ngxson/esp32-usb-to-airprint",
    "interplains/zero-breach",
]
for full in TRACKED:
    r = japi(f"repos/{full}")
    if not r:
        print(f"  {full}: 404")
        continue
    rel = japi(f"repos/{full}/releases?per_page=100")
    nrel = len(rel) if isinstance(rel, list) else 0
    cm = japi(f"repos/{full}/commits?per_page=1")
    hdr = api(f"repos/{full}/commits?per_page=1")
    # count via link
    import subprocess as sp
    h = sp.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"], capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    ncomm = int(m.group(1)) if m else 1
    print(f"  {full:<42} ⭐{r['stargazers_count']:>6} subs={r['subscribers_count']:>3} oi={r['open_issues_count']:>3} "
          f"commits={ncomm:<5} rel={nrel:<3} pushed={r['pushed_at']} lic={(r.get('license') or {}).get('spdx_id')}")
