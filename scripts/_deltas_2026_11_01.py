#!/usr/bin/env python3
"""2026-11-01: day-over-day deltas for tracked projects + candidate discovery."""
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


def ncommits(full):
    h = subprocess.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"],
                       capture_output=True, text=True, env=ENV).stdout
    m = re.search(r'page=(\d+)>; rel="last"', h)
    return int(m.group(1)) if m else 1


TRACKED = [
    "unclebob/ub-mode", "rddmwmddr/android-ad-cleaner",
    "DenisSergeevitch/ex-ussr-kinship-research", "trailofbits/brotli-checker",
    "YoyoLin008/mcreplay", "songjianyang/xss-audit",
    "deepseek-ai/DeepInfer", "colinhacks/reylo", "Snapintosh/Snapintosh",
    "AxiomMath/CFSG", "patch-gg/anymove", "ngxson/esp32-usb-to-airprint",
    "interplains/zero-breach", "KohakuBlueleaf/KohakUnlock", "mirkobrombin/raven",
    "shinglyu/Prompt-Orchestrator", "karpathy/autoresearch",
]
print("### TRACKED DELTAS")
for full in TRACKED:
    r = japi(f"repos/{full}")
    if not r:
        print(f"  {full}: 404/FAILED")
        continue
    rel = japi(f"repos/{full}/releases?per_page=100")
    assets = sum(len(x.get("assets", [])) for x in rel) if isinstance(rel, list) else 0
    c = ncommits(full)
    print(f"  {full:<40} stars={r['stargazers_count']:<7} subs={r['subscribers_count']:<4} "
          f"oi={r['open_issues_count']:<5} commits={c:<5} rel={len(rel) if isinstance(rel,list) else 0:<3} "
          f"assets={assets:<4} pushed={r['pushed_at']} size={r['size']}KB lang={r['language']} "
          f"lic={(r.get('license') or {}).get('spdx_id')}")

print("\n### 10-31 NON-FARM CANDIDATES (from cohort top-list, size>20KB or subs>20)")
res = japi("search/repositories?q=created:2026-10-31+stars:>=40&per_page=100&sort=stars")
for i in res["items"][:40]:
    if i["size"] <= 30:
        continue
    print(f"  {i['stargazers_count']:>6} {i['size']:>8}KB {i['full_name']}  | {str(i['description'])[:90]}")

print("\n### 10-30 top non-farm (size>100KB)")
res30 = japi("search/repositories?q=created:2026-10-30+stars:>=60+size:>100&per_page=60&sort=stars")
for i in res30["items"][:35]:
    print(f"  {i['stargazers_count']:>6} {i['size']:>8}KB {i['full_name']}  | {str(i['description'])[:90]}")
