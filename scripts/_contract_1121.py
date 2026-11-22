#!/usr/bin/env python3
"""Count "machine-readable contract enforced in CI" across the cohort.

Observation
-----------
On 2026-11-18 the report noted, for the first time, that
``alibaba/open-code-review`` ships ``plugin-contract.yml`` and
``action-contract.yml`` — i.e. it turns a "contract" from documentation into
an executable CI gate.  That was recorded as a single-project observation.

Today the same pattern shows up in several *unrelated* projects.  The claim
that matters is not "one project does this" but "how many independent
projects do this, and what exactly does the gate check".  To test that, this
script:

  1. lists every workflow filename in the cohort,
  2. classifies each name against a fixed vocabulary of contract-like gates,
  3. for every matching workflow, downloads the raw YAML and records which
     job/step names it contains and whether it fails closed (a non-zero
     exit / a `fail` condition) — a "contract" that only warns is a
     different thing from a gate.

The vocabulary is stated explicitly so the classification can be audited and
disputed rather than hidden in a heuristic.

Output: /tmp/contract_1121.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/contract_1121.json"

REPOS = [
    "alibaba/open-code-review",
    "backnotprop/plannotator",
    "meta/astryx",
    "tradermonty/claude-trading-skills",
    "zhouxiaoka/autoclip",
    "HKUDS/CLI-Anything",
    "cursor/plugins",
    "google-labs-code/stitch-skills",
    "elementalsouls/Claude-BugHunter",
    "mvanhorn/last30days-skill",
    "openvinotoolkit/openvino",
    "ag-ui-protocol/ag-ui",
    "nginx/nginx",
    "dream-num/univer",
    "toeverything/AFFiNE",
    "XiaoYouChR/Ghost-Downloader-3",
    "Tracer-Cloud/opensre",
    "mjmirza/app-store-compliance",
]

# A workflow name counts as a contract gate if it matches one of these.
CONTRACT_WORDS = ("contract", "schema", "gate", "policy", "canary", "provenance",
                  "sign-check", "attest", "sbom")

# A gate "fails closed" if the YAML contains an explicit failing condition.
FAIL_CLOSED = re.compile(
    r"(exit\s+1|::error|fail-fast|if:\s*failure\(\)|continue-on-error:\s*false|"
    r"required:|strict:)", re.I)


def api(path, params=None, raw=False, headers=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def scan(full):
    wf = api(f"repos/{full}/contents/.github/workflows") or []
    if not isinstance(wf, list):
        wf = []
    names = [w.get("name") for w in wf if w.get("name")]
    matches = []
    for w in wf:
        n = w.get("name") or ""
        if not any(k in n.lower() for k in CONTRACT_WORDS):
            continue
        path = w.get("path")
        body = api(f"repos/{full}/contents/{urllib.parse.quote(path)}", raw=True,
                   headers=["Accept: application/vnd.github.raw"]) or ""
        jobs = re.findall(r"^  ([A-Za-z0-9_.-]+):\s*$", body, re.M)
        steps = re.findall(r"^\s*-\s*(?:name:\s*(.+)|run:\s*(.+))", body, re.M)
        matches.append({
            "workflow": n,
            "path": path,
            "bytes": len(body),
            "jobs": jobs[:8],
            "fails_closed": bool(FAIL_CLOSED.search(body)),
            "step_names": [s[0] or (s[1] or "")[:40] for s in steps][:10],
            "head": body[:400],
        })
    return {
        "repo": full,
        "n_workflows": len(names),
        "workflow_names": names,
        "contract_workflows": matches,
        "n_contract_workflows": len(matches),
    }


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(scan, REPOS):
            out.append(r)
            print(f"  {r['repo']:44s} wf={r['n_workflows']:>3} contract={r['n_contract_workflows']:>2} "
                  f"{[m['workflow'] for m in r['contract_workflows']]}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    n_with = sum(1 for r in out if r["n_contract_workflows"])
    n_fail = sum(1 for r in out if any(m["fails_closed"] for m in r["contract_workflows"]))
    print(f"repos with >=1 contract-like gate: {n_with}/{len(out)}")
    print(f"repos with >=1 fail-closed contract gate: {n_fail}/{len(out)}")


if __name__ == "__main__":
    main()
