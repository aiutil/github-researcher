#!/usr/bin/env python3
import json
import os
import subprocess
import urllib.parse

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    p = subprocess.run(["gh", "api", url], capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None, p.stderr.strip()[:300]
    try:
        return json.loads(p.stdout), None
    except Exception as e:  # noqa: BLE001
        return None, f"{e}: {p.stdout[:200]}"


for day in ["2026-11-06", "2026-11-07", "2026-11-08"]:
    d, err = api("search/repositories", {"q": f"created:{day} stars:>=30", "sort": "stars", "order": "desc", "per_page": 5})
    if d is None:
        print(day, "ERR", err)
        continue
    print(f"created:{day} stars:>=30  total={d.get('total_count')}")
    for i in d.get("items", [])[:5]:
        print(f"      {i['full_name']:55} stars={i['stargazers_count']}")
    print()
