#!/usr/bin/env python3
"""Dump READMEs + key docs for the 5 missing project profiles."""
import json, subprocess, os, sys

TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout.strip()
ENV = {**os.environ, "GH_TOKEN": TOKEN, "HOME": "/home/lohasle"}


def api(path, raw=False):
    args = ["gh", "api", path]
    if raw:
        args += ["-H", "Accept:application/vnd.github.raw"]
    r = subprocess.run(args, capture_output=True, text=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


TARGETS = {
    "Shagg88/COGBox": ["README.md"],
    "valentderah/totk-pc-recomp": ["README.md", "docs/architecture.md"],
    "haydenschmitty/floorplan": ["README.md", "docs/how-it-works.md"],
    "kuraeow/ultratears": ["README.md"],
    "NotRexed/SkyboundTotk": ["README.md"],
}

for full, paths in TARGETS.items():
    print("=" * 110)
    print("REPO:", full)
    print("=" * 110)
    for p in paths:
        print(f"\n----- {p} -----")
        print(api(f"repos/{full}/contents/{p}", raw=True)[:9000])
    # releases + issue titles
    rel = api(f"repos/{full}/releases?per_page=20")
    try:
        rl = json.loads(rel) if rel else []
        print(f"\n----- RELEASES ({len(rl)}) -----")
        for x in rl:
            print(f"  {x['tag_name']} published={x['published_at']} assets={len(x['assets'])} "
                  f"name={x['name']}")
    except Exception:
        pass
    iss = api(f"repos/{full}/issues?state=all&per_page=30")
    try:
        il = json.loads(iss) if iss else []
        print(f"\n----- ISSUES/PRs (first 30 of {len(il)}) -----")
        for x in il:
            kind = "PR" if "pull_request" in x else "issue"
            print(f"  #{x['number']} [{kind}] {x['state']} {x['created_at']} :: {x['title'][:100]}")
    except Exception:
        pass
