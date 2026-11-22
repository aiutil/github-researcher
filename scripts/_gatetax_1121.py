#!/usr/bin/env python3
"""Objective taxonomy of CI gates by TRIGGER, plus declared semantics.

The prose-comment classification proved fragile (a single line can be wrapped
across several comment lines, so a phrase-level regex misses it).  The
*trigger* is objective and comes straight out of the YAML, so this script
leads with it and keeps the prose only as supporting evidence.

Taxonomy
--------
PR_GATE        the workflow fires on pull_request / pull_request_target.
               Such a workflow can gate a merge, and its check can be
               configured as a required status check.
SCHEDULE_ONLY  the workflow fires ONLY on schedule / workflow_dispatch /
               repository_dispatch / workflow_call and never on
               pull_request.  Such a workflow *cannot* gate a merge; it is
               a periodic or post-publication verifier.

The interesting question is whether projects that use the word "contract"
disagree about which of the two they mean.

Output: /tmp/gatetax_1121.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/gatetax_1121.json"

REPOS = [
    "alibaba/open-code-review", "backnotprop/plannotator", "meta/astryx",
    "tradermonty/claude-trading-skills", "zhouxiaoka/autoclip",
    "Tracer-Cloud/opensre", "ag-ui-protocol/ag-ui", "mvanhorn/last30days-skill",
    "HKUDS/CLI-Anything", "cursor/plugins", "google-labs-code/stitch-skills",
    "elementalsouls/Claude-BugHunter", "openvinotoolkit/openvino",
    "firecrawl/firecrawl", "dream-num/univer", "we-promise/sure",
]

GATE_WORDS = ("contract", "canary", "gate", "policy", "provenance", "sign-check")

PR_TRIGGERS = ("pull_request", "pull_request_target")
SCHED_TRIGGERS = ("schedule", "workflow_dispatch", "repository_dispatch",
                  "workflow_call", "release", "create")


def api(path, raw=False, headers=None, timeout=120):
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(path)
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
    rows = []
    for w in wf:
        n = w.get("name") or ""
        if not any(k in n.lower() for k in GATE_WORDS):
            continue
        body = api(f"repos/{full}/contents/{urllib.parse.quote(w.get('path'))}",
                   raw=True, headers=["Accept: application/vnd.github.raw"]) or ""
        trig = set(re.findall(r"^\s{2}(push|pull_request|pull_request_target|schedule|"
                               r"workflow_dispatch|repository_dispatch|workflow_call|"
                               r"release|create):", body, re.M))
        if trig & set(PR_TRIGGERS):
            kind = "PR_GATE"
        elif trig & set(SCHED_TRIGGERS):
            kind = "SCHEDULE_ONLY"
        else:
            kind = "NO_TRIGGER_FOUND"
        # prose evidence, joined across wrapped comment lines
        prose = " ".join(
            l.strip().lstrip("# ").rstrip() for l in body.splitlines() if l.strip().startswith("#")
        )
        prose = re.sub(r"\s+", " ", prose)
        adv = re.search(r"(never a required check|not a required check|"
                        r"never blocks|does not block|doesn'?t block|"
                        r"non-blocking|advisory)", prose, re.I)
        blk = re.search(r"(blocking:|required status check|must pass)", prose, re.I)
        can = re.search(r"(after publication|after release|post-release|"
                        r"exercises the real|live install)", prose, re.I)
        rows.append({
            "workflow": n,
            "kind": kind,
            "triggers": sorted(trig),
            "declared_advisory": bool(adv),
            "declared_blocking": bool(blk),
            "declared_canary": bool(can),
            "evidence": (adv.group(0) if adv else "") or (can.group(0) if can else "") or (blk.group(0) if blk else ""),
            "prose_excerpt": prose[:340],
        })
    return {"repo": full, "n_workflows": len(wf), "gates": rows}


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(scan, REPOS):
            out.append(r)
            for g in r["gates"]:
                print(f"  {r['repo']:42s} {g['workflow']:32s} {g['kind']:17s} "
                      f"adv={int(g['declared_advisory'])} blk={int(g['declared_blocking'])} "
                      f"can={int(g['declared_canary'])}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    c = Counter(g["kind"] for r in out for g in r["gates"])
    print("\ntrigger taxonomy:", dict(c))
    named = [g for r in out for g in r["gates"] if "contract" in g["workflow"].lower()]
    cn = Counter(g["kind"] for g in named)
    print('workflows whose NAME contains "contract":', dict(cn), f"(n={len(named)})")
    both = sum(1 for g in named if g["kind"] == "PR_GATE")
    print(f'"contract" gates that fire on a pull request: {both}/{len(named)}')


if __name__ == "__main__":
    main()
