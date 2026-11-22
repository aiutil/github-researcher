#!/usr/bin/env python3
"""Classify CI gates by their *blocking semantics*, not by their filename.

Finding
-------
Several repositories in today's cohort ship workflows whose names contain
"contract".  Reading the workflow bodies shows that the same word covers
three materially different enforcement levels, and the projects usually say
so in the file's own comment header:

  BLOCKING   the gate is a required status check; a red result blocks the
             merge or the release.
  ADVISORY   the gate is deliberately NOT required ("never a required
             check", "not a required check", "does not block").
  CANARY     the gate runs *after* publication and verifies the artifact
             that was actually shipped (live installers, released package).

A fourth pattern shows up as a scheduling detail rather than a comment:
the gate fires on a cron/schedule rather than on pull_request.

This script extracts the evidence for the classification -- the comment
lines that state the blocking semantics -- so the claim in the report is
traceable to specific lines in specific files rather than to a filename
heuristic.

Output: /tmp/gates_1121.json
"""
import json
import os
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/gates_1121.json"

REPOS = [
    "alibaba/open-code-review", "backnotprop/plannotator", "meta/astryx",
    "tradermonty/claude-trading-skills", "zhouxiaoka/autoclip",
    "Tracer-Cloud/opensre", "ag-ui-protocol/ag-ui", "mvanhorn/last30days-skill",
    "HKUDS/CLI-Anything", "cursor/plugins", "google-labs-code/stitch-skills",
    "elementalsouls/Claude-BugHunter", "openvinotoolkit/openvino",
]

GATE_WORDS = ("contract", "canary", "gate", "policy")

# Phrases that state, in the project's own words, whether the gate blocks.
BLOCKING = re.compile(r"\bblocking\b|\brequired (?:status )?check\b|\bmust pass\b|"
                       r"\bfails? the (?:build|pipeline|pr|pull request)\b|"
                       r"\bblocks? (?:the )?(?:merge|release)\b", re.I)
ADVISORY = re.compile(r"never a required check|not a required check|"
                       r"non-blocking|never blocks|does not block|"
                       r"doesn'?t block|without blocking|advisory|"
                       r"holds back only|never delay", re.I)

CANARY = re.compile(r"after publication|after release|post-release|"
                    r"exercises the real|actual artifact|published artifact|"
                    r"live install", re.I)


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


def comments(body):
    out = []
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("#"):
            out.append(s.lstrip("# ").rstrip())
    return out


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
        c = comments(body)
        trig = re.findall(r"^\s{2}(push|pull_request|pull_request_target|schedule|"
                          r"workflow_dispatch|repository_dispatch|workflow_call|"
                          r"release|create):", body, re.M)
        joined = "\n".join(c)
        # Evidence lines: the comment lines that actually carry the semantics.
        ev_block = [x for x in c if BLOCKING.search(x)]
        ev_adv = [x for x in c if ADVISORY.search(x)]
        ev_can = [x for x in c if CANARY.search(x)]
        if ev_can:
            kind = "CANARY"
        elif ev_adv:
            kind = "ADVISORY"
        elif ev_block:
            kind = "BLOCKING"
        else:
            kind = "UNDECLARED"
        rows.append({
            "workflow": n,
            "kind": kind,
            "triggers": sorted(set(trig)),
            "scheduled": "schedule" in trig,
            "evidence_blocking": ev_block[:3],
            "evidence_advisory": ev_adv[:3],
            "evidence_canary": ev_can[:3],
            "n_comment_lines": len(c),
        })
    return {"repo": full, "n_workflows": len(wf), "gates": rows}


def main():
    out = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(scan, REPOS):
            out.append(r)
            for g in r["gates"]:
                print(f"  {r['repo']:44s} {g['workflow']:30s} {g['kind']:11s} "
                      f"sched={g['scheduled']} trig={g['triggers']}", flush=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(g["kind"] for r in out for g in r["gates"])
    print("\nclassification:", dict(c))
    print("repos with >=1 declared gate:",
          sum(1 for r in out if any(g["kind"] != "UNDECLARED" for g in r["gates"])),
          "/", len(out))


if __name__ == "__main__":
    main()
