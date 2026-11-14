#!/usr/bin/env python3
"""Quantify the 2026-11-08 payload cluster: domains, commands, README templates."""

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")
PATH = "/tmp/cand_2026_11_09.json"


def api_raw(full, path="README.md"):
    p = subprocess.run(
        ["gh", "api", "-H", "Accept: application/vnd.github.raw",
         f"repos/{full}/contents/{path}"],
        capture_output=True, text=True, env=ENV, timeout=90)
    return p.stdout if p.returncode == 0 else None


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    farm = [d for d in data if "pre-configured environment" in (d["desc"] or "").lower()
            or "automated deployment pipeline" in (d["desc"] or "").lower()
            or "pre-configured production build" in (d["desc"] or "").lower()
            or "deployment package" in (d["desc"] or "").lower()
            or "Optimized package deployment" in (d["desc"] or "").lower()
            or "configuration folder" in (d["desc"] or "").lower()]
    print(f"farm cluster size: {len(farm)} / {len(data)} = {len(farm)/len(data)*100:.1f}%\n")

    dom = Counter()
    cmds = Counter()
    tmpl = Counter()
    per_repo = {}

    for d in farm:
        rm = api_raw(d["full_name"])
        if rm is None:
            continue
        per_repo[d["full_name"]] = rm
        for m in set(re.findall(r"https?://([a-z0-9.\-]+\.(?:cc|com|net|org|io|ru|xyz|top|shop|site|icu|buzz|click))", rm, re.I)):
            dom[m] += 1
        for m in re.findall(r"(?:irm|iwr|curl|wget)\s+([^\s|`]+)", rm, re.I):
            cmds[m] += 1
        # template signature: strip the product name
        t = re.sub(r"[A-Za-z0-9 ._\-]{3,40}", "X", rm)
        tmpl[hashlib.md5(t.encode()).hexdigest()[:10]] += 1
        time.sleep(0.18)

    print("=== DOMAINS in READMEs ===")
    for d_, c in dom.most_common(20):
        print(f"  {c:>4}  {d_}")

    print("\n=== DOWNLOAD COMMANDS ===")
    for c_, c in cmds.most_common(20):
        print(f"  {c:>4}  {c_}")

    print("\n=== README TEMPLATE HASHES (product name masked) ===")
    for h, c in tmpl.most_common(10):
        print(f"  {c:>4}  {h}")

    json.dump(per_repo, open("/tmp/farm_readmes_1109.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    print("\n=== keywords across farm READMEs ===")
    for kw in ["Real-time protection", "Execution Policy", "Antivirus", "SmartScreen",
               "Administrator", "Organic Discovery", "powershell -File", "irm https",
               "curl -sL", "gcm i*x", "windows-defender.cc", "git-software.cc"]:
        n = sum(1 for rm in per_repo.values() if kw.lower() in rm.lower())
        if n:
            print(f"  {kw:28s} {n:>4} / {len(per_repo)}")

    print("\n=== per-repo payload command (first found) ===")
    hits = 0
    for full, rm in per_repo.items():
        m = re.search(r"(?:irm|iwr)\s+(https?://[^\s|`]+)", rm, re.I)
        if m:
            hits += 1
            if hits <= 5:
                print(f"  {full:46s} {m.group(1)}")
    print(f"  -> {hits} of {len(per_repo)} farm repos carry an irm/iwr payload URL")


if __name__ == "__main__":
    main()
