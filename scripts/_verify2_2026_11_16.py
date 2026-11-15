#!/usr/bin/env python3
"""Part 2 of verification: Gemini cohort cross-day linkage, code byte-identity,
commit fingerprint, payload links, steam-library-bridge release timeline."""
import hashlib
import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    if headers:
        for h in headers:
            cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


C = {r["full_name"]: r for r in json.load(open("/tmp/cand_1115.json"))}
gem = sorted(k for k in C if "Gemini-Config-Checker" in k)

print("=== owner cohort: registration window + family composition ===")
cohort = []
for full in gem:
    o = full.split("/")[0]
    u = api(f"users/{o}") or {}
    repos = api(f"users/{o}/repos", {"per_page": 100}) or []
    names = [r.get("name") for r in repos] if isinstance(repos, list) else []
    fam = Counter()
    for n in names:
        for key in ("GitHub-Copilot-app", "ai--manus", "Gemini-Config-Checker", "IPTV_Player"):
            if n.startswith(key):
                fam[key] += 1
                break
        else:
            fam["<other>"] += 1
    cohort.append((u.get("created_at"), o, u.get("public_repos"), u.get("followers"), dict(fam)))
cohort.sort()
for t, o, n, f, fam in cohort:
    print(f"  {t}  {o:30s} repos={n} followers={f} {fam}")
ts = [c[0] for c in cohort]
print(f"\n  -> owner registration window: {min(ts)} .. {max(ts)}")
print(f"  -> span seconds: {int((__import__('datetime').datetime.fromisoformat(max(ts).replace('Z','+00:00')) - __import__('datetime').datetime.fromisoformat(min(ts).replace('Z','+00:00'))).total_seconds())}")
print(f"  -> all owners 0 followers: {all(c[3]==0 for c in cohort)}")
print(f"  -> all owners exactly 12 repos: {all(c[2]==12 for c in cohort)}")

print("\n=== code byte-identity across the family ===")
probes = ["internal/scan/scan_test.go", "internal/scan/region.go",
          "internal/ui/ui.go", "dns_android.go", "Makefile", "go.mod", "VERSION"]
agg = {}
for pp in probes:
    hs = {}
    for full in gem:
        d = api(f"repos/{full}/contents/{pp}", raw=True,
                headers=["Accept: application/vnd.github.raw"])
        if d:
            hs[full.split("/")[0]] = hashlib.md5(d.encode()).hexdigest()
    if hs:
        agg[pp] = hs
        print(f"  {pp:28s} repos={len(hs):3d} distinct_md5={len(set(hs.values()))} "
              f"-> {list(set(hs.values()))[:2]}")
print("  -> same blob sha across all repos? (GitHub dedups identical blobs)")
for full in gem[:3]:
    t = api(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
    shas = [(b.get('path'), b.get('sha')) for b in (t.get('tree') or [])
            if b.get('type') == 'blob' and b.get('path') in
            ('internal/scan/scan_test.go', 'go.mod', 'Makefile')]
    print(f"    {full}: {shas}")

print("\n=== commit fingerprint (all 53 messages) ===")
sample = gem[0]
cm = api(f"repos/{sample}/commits", {"per_page": 100}) or []
times = []
for c in cm if isinstance(cm, list) else []:
    times.append((((c.get("commit") or {}).get("author") or {}).get("date"),
                  ((c.get("commit") or {}).get("message") or "").split("\n")[0]))
print(f"  {sample}: {len(cm)} commits, first={times[0]}, last={times[-1]}")
# compare 2nd repo
sample2 = gem[5]
cm2 = api(f"repos/{sample2}/commits", {"per_page": 100}) or []
t2 = []
for c in cm2:
    cc = c.get("commit") or {}
    au = cc.get("author") or {}
    t2.append((au.get("date"), (cc.get("message") or "").splitlines()[0] if cc.get("message") else ""))
same_msg = [t[1] for t in times] == [t[1] for t in t2]
same_time = [t[0] for t in times] == [t[0] for t in t2]
print(f"  {sample2}: {len(cm2)} commits; identical message sequence={same_msg}; "
      f"identical timestamp sequence={same_time}")
print(f"  first 6 msgs repo1: {[t[1][:40] for t in times[:6]]}")
print(f"  first 6 msgs repo2: {[t[1][:40] for t in t2[:6]]}")

print("\n=== payload links ===")
links = Counter()
for full in gem:
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    for u in re.findall(r"https?://[^\s)\"'<>]+", rm):
        if "dropbox" in u:
            links[u] += 1
for u, n in links.most_common():
    print(f"  {n:3d} repos -> {u}")

print("\n=== README structural fingerprint (headings) ===")
rm = api(f"repos/{sample}/readme", raw=True,
         headers=["Accept: application/vnd.github.raw"]) or ""
heads = [l for l in rm.splitlines() if l.startswith("#")]
print(f"  {len(heads)} headings, {len(rm)} bytes")
for h in heads[:28]:
    print(f"    {h[:90]}")

print("\n=== steam-library-bridge release timeline ===")
sl = "atlas7283/steam-library-bridge"
rel = api(f"repos/{sl}/releases", {"per_page": 20}) or []
for r in rel if isinstance(rel, list) else []:
    print(f"  tag={r.get('tag_name'):10s} published={r.get('published_at')} "
          f"created={r.get('created_at')} assets={len(r.get('assets') or [])}")
t = api(f"repos/{sl}/git/trees/HEAD?recursive=1") or {}
blobs = [b for b in (t.get("tree") or []) if b.get("type") == "blob"]
print(f"  total blobs={len(blobs)}")
for b in sorted(blobs, key=lambda b: -(b.get('size') or 0))[:6]:
    print(f"    {b.get('size'):>11} B  {b.get('path')}")
for b in blobs:
    if b.get("path", "").endswith(".exe"):
        print(f"  EXE blob: {b.get('path')} size={b.get('size')} sha={b.get('sha')}")
print("  commits:")
for c in (api(f"repos/{sl}/commits", {"per_page": 10}) or []):
    cc = c.get("commit") or {}
    au = cc.get("author") or {}
    print(f"    {au.get('date')} {(cc.get('message') or '').splitlines()[0][:70] if cc.get('message') else ''}")
print(f"  owner repos:")
for r in (api("users/atlas7283/repos", {"per_page": 100}) or []):
    print(f"    {r.get('name')} ⭐{r.get('stargazers_count')} created={r.get('created_at')} "
          f"size={r.get('size')}KB desc={str(r.get('description'))[:80]}")
