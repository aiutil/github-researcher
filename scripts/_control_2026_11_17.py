#!/usr/bin/env python3
"""Control test: how common is the '10-byte placeholder README' signature?

The cheat-farm owners each hold exactly 2 public repos: the payload repo plus
a repo whose README.md is exactly '# <repo-name>' (10 bytes for an 8-char
name), created 1-2 minutes after the account.  This samples owners of
ordinary, non-farm repositories (selected from the daily candidate pool) and
measures how often the same signature appears.  If it is rare among normal
accounts, it is a usable structural fingerprint.
"""
import json
import os
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
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


def owner_signature(login):
    u = api(f"users/{login}") or {}
    rs = api(f"users/{login}/repos", {"per_page": 100, "sort": "created"}) or []
    if not isinstance(rs, list):
        rs = []
    ph = []
    for r in rs:
        name = r.get("name") or ""
        full = r.get("full_name")
        m = api(f"repos/{full}") or {}
        tree = api(f"repos/{full}/git/trees/{m.get('default_branch') or 'main'}?recursive=1") or {}
        blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
        rm = api(f"repos/{full}/readme", raw=True,
                 headers=["Accept: application/vnd.github.raw"])
        rm = rm if isinstance(rm, str) else ""
        # signature: exactly one blob, README.md, content == "# <name>"
        is_ph = (len(blobs) == 1 and blobs[0].get("path") == "README.md"
                 and rm.strip() == f"# {name}")
        ph.append({"name": name, "stars": r.get("stargazers_count"),
                   "created": r.get("created_at"), "n_blobs": len(blobs),
                   "is_placeholder": is_ph, "readme_len": len(rm)})
    return {"login": login, "created_at": u.get("created_at"),
            "followers": u.get("followers"),
            "public_repos": u.get("public_repos"), "repos": ph,
            "n_placeholder": sum(1 for x in ph if x["is_placeholder"])}


# Control owners: taken from the 2026-11-16 candidate pool, excluding the
# known farm accounts.
CONTROL = [
    "andyhuo520", "stvlynn", "chuanqisun", "staryone", "scottsturrock",
    "Aabyss-Team", "louis49", "adamsardo", "siliconjungle", "ampdot-io",
    "squallsama", "jackson-cmd", "asimawdah", "CoderL98", "liangdabiao",
    "nagavineerpasam", "oujingzhou", "Mecsocse", "boringmarketer",
]

FARM = [
    "OceanChandlerSewer", "SandstoneShoutMoon", "VergeEnvoyAdze",
    "ashtherapistpillar", "LairFreighter85", "DiamondCockatooFlow",
    "hubchrysalisspanner", "Brandtrocontrol", "DestroyerStrait",
    "delugesovereignphase",
]

if __name__ == "__main__":
    for label, owners in (("CONTROL (normal owners)", CONTROL),
                          ("FARM (cheat-deployment owners)", FARM)):
        print("=" * 92)
        print(label)
        print("=" * 92)
        rows = []
        with ThreadPoolExecutor(max_workers=4) as ex:
            for r in ex.map(owner_signature, owners):
                rows.append(r)
        n_any = 0
        n_all_ph = 0
        for r in rows:
            ph = [x for x in r["repos"] if x["is_placeholder"]]
            has_ph = len(ph) > 0
            all_ph = len(r["repos"]) > 0 and len(ph) == len(r["repos"])
            n_any += 1 if has_ph else 0
            n_all_ph += 1 if all_ph else 0
            names = [(x["name"], x["stars"], x["readme_len"]) for x in r["repos"]]
            print(f"  {r['login']:<28} created={str(r['created_at'])[:10]} "
                  f"repos={r['public_repos']:<3} followers={r['followers']:<5} "
                  f"placeholders={len(ph)}/{len(r['repos'])}")
            for x in r["repos"]:
                flag = "PH" if x["is_placeholder"] else "  "
                print(f"      [{flag}] {x['name']:<30} ⭐{str(x['stars']):<6} "
                      f"blobs={x['n_blobs']:<4} readme={x['readme_len']}B "
                      f"created={x['created']}")
        print(f"\n  owners with >=1 placeholder repo: {n_any}/{len(rows)}")
        print(f"  owners where ALL repos are placeholders: {n_all_ph}/{len(rows)}\n")
        json.dump(rows, open(f"/tmp/ctrl_{'farm' if 'FARM' in label else 'ctrl'}_1117.json",
                             "w"), ensure_ascii=False, indent=1)
