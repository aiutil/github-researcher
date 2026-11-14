#!/usr/bin/env python3
"""Check whether the crypto-cluster repos share the same subscriber accounts."""
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
        return None, p.stderr.strip()[:300]
    if raw:
        return p.stdout, None
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:300]}"


REPOS = [
    "summittypeplay/sims4-updater",
    "Crateryeexpiate/TradePilot",
    "Beachfromgate/Wallet-Hunter",
    "Logosheshow47/crypto-panic",
    "Hairzenexalt/Fragment-Sniper",
    "prismarmorergirder/wallet-security-checker",
    "DimensionRobin/rob-run-private-cheat",
]


def subs_of(full):
    s, _ = api(f"repos/{full}/subscribers", {"per_page": 100})
    return full, [x.get("login") for x in s] if isinstance(s, list) else []


def main():
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(subs_of, REPOS))
    sets = {f: set(s) for f, s in res}
    for f, s in res:
        print(f"{f:<45} n={len(s):<4}")
    all_logins = {}
    for f, s in sets.items():
        for l in s:
            all_logins.setdefault(l, []).append(f)
    print("\n--- accounts subscribed to >1 repo ---")
    shared = {l: fs for l, fs in all_logins.items() if len(fs) > 1}
    print(f"unique subscriber accounts across cluster: {len(all_logins)}")
    print(f"accounts subscribed to 2+ of these repos: {len(shared)}")
    for l, fs in sorted(shared.items(), key=lambda kv: -len(kv[1]))[:30]:
        print(f"  {l:<40} -> {len(fs)} repos")

    # inspect a couple of the shared accounts
    for l in list(shared)[:4]:
        u, _ = api(f"users/{l}")
        u = u or {}
        print(f"\n>> {l}: type={u.get('type')} created={u.get('created_at')} repos={u.get('public_repos')} followers={u.get('followers')} name={u.get('name')!r} bio={u.get('bio')!r}")

    json.dump({"subs": {f: s for f, s in res}, "shared": shared}, open("/tmp/subs_1114.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
