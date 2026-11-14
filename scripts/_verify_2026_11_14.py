#!/usr/bin/env python3
"""Final verification: dropbox payload link identity, gh.io targets, -desktop workflow spread."""
import json
import re
import subprocess
import os
import sys
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=90, raw=False, headers=None):
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
        return None, p.stderr.strip()[:200]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:200]}"


DATA = json.load(open("/tmp/fingerprint_1114.json", encoding="utf-8"))
rows = [r for r in DATA if r["day"] == "2026-11-14"]

GROUPS = {
    "ai--manus2.0": "aimanus20",
    "IPTV_Player_2.0": "iptvplayer20",
    "GitHub-Copilot-app": "githubcopilotapp",
}


def sample(names, n=4):
    return [r["full_name"] for r in rows if r["full_name"].split("/")[1] == names][:n]


def dl_links(full):
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    rm = rm or ""
    links = sorted(set(re.findall(r"https://(?:www\.)?dropbox\.com/scl/fi/[^\s\"'<>)]+", rm)))
    other = sorted(set(re.findall(r"https://gh\.io/[^\s\"'<>)]+", rm)))
    return full, links, other


def wf(full):
    w, _ = api(f"repos/{full}/actions/workflows", {"per_page": 10})
    if not isinstance(w, dict):
        return full, []
    return full, [(x.get("name"), x.get("state"), x.get("path")) for x in (w.get("workflows") or [])]


print("=== dropbox link identity within each family ===")
for repo_name in GROUPS.values():
    names = sample(repo_name)
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(dl_links, names))
    print(f"\n-- family {repo_name} --")
    for full, links, other in res:
        print(f"  {full}")
        for l in links:
            print(f"      {l}")
        if other:
            print(f"      gh.io: {other}")

print("\n\n=== '-desktop' family: workflow inventory + README template identity ===")
DESK = [r["full_name"] for r in rows if r["full_name"].split("/")[1].endswith("-desktop")]
print("repos:", DESK)
with ThreadPoolExecutor(max_workers=4) as ex:
    wres = list(ex.map(wf, DESK))
for full, ws in wres:
    print(f"  {full}: {ws}")

print("\n=== README template identity across -desktop family (normalized) ===")
norm = Counter()
for r in DATA:
    if r["day"] == "2026-11-14" and r["full_name"].split("/")[1].endswith("-desktop"):
        rm, _ = api(f"repos/{r['full_name']}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
        rm = rm or ""
        # strip the product name and the owner slug to see the template
        t = re.sub(r"[A-Za-z0-9 .:+-]{3,40}? 2026", "PRODUCT 2026", rm)
        t = re.sub(r"https://[a-z0-9-]+\.github\.io", "https://OWNER.github.io", t)
        t = re.sub(r"updated-\d{4}--\d{2}--\d{2}", "updated-DATE", t)
        t = re.sub(r"release-v[\d.]+", "release-vX", t)
        norm[__import__("hashlib").md5(t.encode()).hexdigest()] += 1
print("  distinct normalized README templates:", len(norm))
for k, v in norm.most_common():
    print(f"    md5={k[:14]} x{v}")
