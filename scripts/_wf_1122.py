#!/usr/bin/env python3
"""11-22 — workflows + contributors for the key projects (profile material)."""
import json
import os
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


for full in ["affaan-m/ECC", "backnotprop/plannotator", "alibaba/open-code-review",
             "mvanhorn/last30days-skill", "GoogleChrome/modern-web-guidance-src",
             "cursor/plugins", "HKUDS/CLI-Anything", "Tracer-Cloud/opensre",
             "mjmirza/app-store-compliance", "obra/superpowers"]:
    wf = api(f"repos/{full}/contents/.github/workflows") or []
    wf_names = [w.get("name") for w in wf] if isinstance(wf, list) else []
    ct = api(f"repos/{full}/contributors", {"per_page": 8}) or []
    ct = [(c.get("login"), c.get("contributions")) for c in ct] if isinstance(ct, list) else []
    iss = api(f"repos/{full}/issues", {"state": "open", "per_page": 3}) or []
    iss = [f"#{i.get('number')} {str(i.get('title'))[:70]}" for i in iss] if isinstance(iss, list) else []
    print(f"{full}")
    print(f"   workflows({len(wf_names)}): {wf_names}")
    print(f"   contributors: {ct}")
    print(f"   sample issues: {iss}")
    print()
