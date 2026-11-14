#!/usr/bin/env python3
"""Dump full README + selected source files for the real projects of interest."""
import json
import os
import subprocess
import sys
import urllib.parse
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


def one(spec):
    full, files = spec
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    out = {"full_name": full, "readme": rm or "", "files": {}}
    for f in files:
        c, _ = api(f"repos/{full}/contents/{f}", raw=True, headers=["Accept: application/vnd.github.raw"])
        out["files"][f] = (c or "")[:4000]
    return out


SPECS = [
    ("hikaku-io/hikaku-extension", ["docs/ARCHITECTURE.md", "docs/MODELS.md", "package.json", "manifest.json"]),
    ("duwqijlk/muse-protocol", ["musepy/client.py", "example_register.py", "requirements.txt", "config.example.json"]),
    ("opencoredev/islandcn", ["AGENTS.md", "package.json", "app/.well-known/agent-skills/index.json/route.ts"]),
    ("faizfahmi77/ScanDot", ["README.md", "android-app/app/build.gradle.kts"]),
    ("quer3q/kraken-mount", ["README.md", "DESIGN.md", "Cargo.toml"]),
    ("brisk-thrush-husky/malware-defender-desktop", [".github/workflows/SP7LDgUHone.yml", "files/main.cpp", "docs/index.html"]),
]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as ex:
        res = list(ex.map(one, SPECS))
    json.dump(res, open("/tmp/rd.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in res:
        print("=" * 70)
        print(r["full_name"], f"(readme {len(r['readme'])}B)")
        print(r["readme"][:3000])
        for f, c in r["files"].items():
            print(f"\n----- {f} ({len(c)}B) -----")
            print(c[:1800])
