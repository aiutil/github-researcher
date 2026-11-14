#!/usr/bin/env python3
"""Full-README fingerprinting across the whole 2026-11-14 window (+11-13 for continuity).

For each repo: full README md5, presence of "Standalone Offline Build", all
external download URLs (dropbox/drive/gumroad etc.), capsule-render usage,
and the owner's account creation timestamp.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
DAYS = ["2026-11-14", "2026-11-13"]
CAND = "/tmp/cand_1114.json"
OUT = "/tmp/fingerprint_1114.json"

URL_RE = re.compile(r"https?://[^\s\"'<>)\]}]+")


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


def work(r):
    full = r["full_name"]
    owner = full.split("/")[0]
    rm, _ = api(f"repos/{full}/readme", raw=True, headers=["Accept: application/vnd.github.raw"])
    rm = rm or ""
    u, _ = api(f"users/{owner}")
    u = u or {}
    urls = [u_ for u_ in URL_RE.findall(rm) if not re.search(r"shields\.io|img\.githubusercontent|github\.com/user-attachments|capsule-render|badge", u_)]
    hosts = Counter()
    for u_ in urls:
        h = re.sub(r"^https?://", "", u_).split("/")[0]
        hosts[h] += 1
    return {
        "full_name": full,
        "day": (r.get("created_at") or "")[:10],
        "stars": r["stars"],
        "forks": r["forks"],
        "subs": r["subs"],
        "size_kb": r["size_kb"],
        "ncommits": r["ncommits"],
        "readme_md5": hashlib.md5(rm.encode()).hexdigest(),
        "readme_len": len(rm),
        "offline_build": "Standalone Offline Build" in rm,
        "has_download_link": bool(re.search(r"dropbox\.com|drive\.google|gumroad|wetransfer|mediafire|discord\.gg|t\.me/", rm)),
        "capsule": "capsule-render" in rm,
        "hosts": dict(hosts.most_common(6)),
        "owner_created": u.get("created_at"),
        "owner_repos": u.get("public_repos"),
        "owner_followers": u.get("followers"),
        "owner_type": u.get("type"),
        "license": r["license"],
        "topics": r["topics"],
    }


def main():
    data = json.load(open(CAND, encoding="utf-8"))
    rows = [r for r in data if (r.get("created_at") or "")[:10] in DAYS]
    rows.sort(key=lambda r: -r["stars"])
    print(f"fingerprinting {len(rows)} repos", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = list(ex.map(work, rows))
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"wrote {len(res)} -> {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
