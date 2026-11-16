#!/usr/bin/env python3
"""Lean control test for the '10-byte placeholder README' fingerprint.

Only one API call per repo (contents/README.md) plus one per owner, instead of
the full tree walk.  Determines how common the signature is among ordinary
repository owners versus the cheat-deployment owners.
"""
import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, raw=False, headers=None, timeout=60):
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(path)
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
    rs = api(f"users/{login}/repos?per_page=100&sort=created") or []
    if not isinstance(rs, list):
        rs = []
    ph = []
    for r in rs:
        name = r.get("name") or ""
        full = r.get("full_name")
        rm = api(f"repos/{full}/readme", raw=True,
                 headers=["Accept: application/vnd.github.raw"])
        rm = rm if isinstance(rm, str) else ""
        is_ph = rm.strip() == f"# {name}" and len(rm) <= 12
        ph.append({"name": name, "stars": r.get("stargazers_count"),
                   "created": r.get("created_at"),
                   "readme_len": len(rm), "is_placeholder": is_ph})
    return {"login": login, "created_at": u.get("created_at"),
            "followers": u.get("followers"),
            "public_repos": u.get("public_repos"), "repos": ph,
            "n_placeholder": sum(1 for x in ph if x["is_placeholder"])}


CONTROL = ["andyhuo520", "stvlynn", "chuanqisun", "staryone", "scottsturrock",
           "Aabyss-Team", "louis49", "adamsardo", "siliconjungle",
           "squallsama", "jackson-cmd", "asimawdah", "CoderL98",
           "nagavineerpasam", "oujingzhou", "boringmarketer"]
FARM = ["OceanChandlerSewer", "SandstoneShoutMoon", "VergeEnvoyAdze",
        "ashtherapistpillar", "LairFreighter85", "DiamondCockatooFlow",
        "hubchrysalisspanner", "Brandtrocontrol", "DestroyerStrait",
        "delugesovereignphase"]

if __name__ == "__main__":
    summary = {}
    for label, owners, key in (("CONTROL", CONTROL, "ctrl"), ("FARM", FARM, "farm")):
        print("=" * 88)
        print(f"{label} ({len(owners)} owners)")
        print("=" * 88)
        with ThreadPoolExecutor(max_workers=6) as ex:
            rows = list(ex.map(owner_signature, owners))
        n_any = sum(1 for r in rows if r["n_placeholder"] > 0)
        n_all = sum(1 for r in rows
                    if r["repos"] and r["n_placeholder"] == len(r["repos"]))
        for r in rows:
            ph = [x["name"] for x in r["repos"] if x["is_placeholder"]]
            print(f"  {r['login']:<26} created={str(r['created_at'])[:10]} "
                  f"repos={str(r['public_repos']):<4} foll={str(r['followers']):<5} "
                  f"placeholders={len(ph)}/{len(r['repos'])} {ph}")
        print(f"\n  owners with >=1 placeholder: {n_any}/{len(rows)}")
        print(f"  owners where ALL repos are placeholders: {n_all}/{len(rows)}\n")
        summary[key] = {"n": len(rows), "any": n_any, "all": n_all}
    json.dump(summary, open("/tmp/control_summary_1117.json", "w"), indent=1)
    print("SUMMARY:", json.dumps(summary))
