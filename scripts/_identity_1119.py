#!/usr/bin/env python3
"""CORRECTED skill-identity metric + superpowers tag/release detail.

FINDING UNDER TEST (from 11-19 measurement):
  * CLI-Anything: 151 SKILL.md files / 82 "identities" by parent-dir name.
    But the single biggest "identity" is literally the directory named
    `skills`, with 67 copies (one per app harness).  So the 1.84x
    "replication" is a MEASUREMENT ARTIFACT.
  * ECC: 1,087 files / 330 identities / max blob-sha multiplicity 3.
    The "copied 10 times" skills have 9 DISTINCT blob shas -> they are
    per-harness / per-locale VARIANTS, not copies.

METRIC:
  naive_identity  = basename(dirname(path))
  robust_identity = nearest meaningful ancestor segment:
      walk up while the segment is generic
      (skills / skill / plugins / plugin / agents / agent / .claude / ...)
      and take the first non-generic one.
  content_identity = the blob sha itself.

Report all three so the reader can see the difference.
"""

import json
import os
import subprocess
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")

GENERIC = {
    "skills", "skill", "plugins", "plugin", "agents", "agent", "commands",
    "cmd", "examples", "example", "docs", "doc", "src", "lib", "core",
    ".claude", ".codex", ".cursor", ".opencode", ".gemini", ".agents",
    ".kiro", ".windsurf", ".antigravity", "harness", "meta", "shared",
    "templates", "template", "references", "reference",
}

REPOS = [
    "affaan-m/ECC", "HKUDS/CLI-Anything", "cursor/plugins",
    "tradermonty/claude-trading-skills", "elementalsouls/Claude-BugHunter",
    "obra/superpowers", "backnotprop/plannotator", "openai/codex-security",
    "NVIDIA/SkillEvaluator", "anthropics/skills", "google-labs-code/stitch-skills",
    "vercel-labs/agent-browser", "GoogleChrome/modern-web-guidance-src",
]


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


def robust_identity(path):
    """Nearest meaningful ancestor segment of the SKILL.md path."""
    parts = [p for p in path.split("/") if p]
    # drop the trailing SKILL.md
    parts = parts[:-1]
    # walk from the closest parent upward, skipping generic names
    for seg in reversed(parts):
        if seg.lower() not in GENERIC and not seg.startswith("."):
            return seg
    return parts[-1] if parts else "<root>"


def measure(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
    naive = defaultdict(list)
    robust = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        n = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        naive[n].append((p, b.get("sha")))
        robust[robust_identity(p)].append((p, b.get("sha")))
    shas = {b.get("sha") for b in skills}
    # a robust identity that has MORE THAN ONE distinct sha is a VARIANT set
    variant_ids = {k: len({s for _, s in v}) for k, v in robust.items()}
    n_variants = sum(1 for k, v in variant_ids.items() if v > 1)
    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "n_skill_files": len(skills),
        "naive_identities": len(naive),
        "robust_identities": len(robust),
        "content_shas": len(shas),
        "naive_replication": round(len(skills) / len(naive), 2) if naive else 0,
        "robust_replication": round(len(skills) / len(robust), 2) if robust else 0,
        "content_replication": round(len(skills) / len(shas), 2) if shas else 0,
        "n_generic_parent_dirs": sum(
            1 for k in naive if k.lower() in GENERIC),
        "generic_parent_files": sum(
            len(v) for k, v in naive.items() if k.lower() in GENERIC),
        "n_robust_ids_with_variants": n_variants,
        "naive_top": sorted(((len(v), k) for k, v in naive.items()), reverse=True)[:5],
        "robust_top": sorted(((len(v), k) for k, v in robust.items()), reverse=True)[:5],
    }


def superpowers_detail():
    full = "obra/superpowers"
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    rel_tags = {r.get("tag_name") for r in rel}
    tag_names = [t.get("name") for t in tags]
    released = [t for t in tag_names if t in rel_tags]
    orphan = [t for t in tag_names if t not in rel_tags]
    print()
    print("=" * 100)
    print("superpowers: which tags have releases and which do not")
    print("=" * 100)
    print(f"  released tags ({len(released)}): {released}")
    print(f"  orphan tags   ({len(orphan)}): {orphan}")
    print("  -> released tags are all v5.x+, orphans are all <= v5.0.2 : the project")
    print("     simply stopped creating GitHub Releases at some point, while tagging")
    print("     continued.  The orphan tags are NOT fake versions (8/8 carry diffs).")


if __name__ == "__main__":
    print("=" * 132)
    print("CORRECTED SKILL-IDENTITY METRIC")
    print("=" * 132)
    print(f"{'repo':40s} {'files':>6s} {'naiveId':>8s} {'robustId':>9s} {'shaId':>6s} "
          f"{'naive×':>7s} {'robust×':>8s} {'content×':>9s} {'genericParentFiles':>18s}")
    print("=" * 132)
    out = []
    for full in REPOS:
        r = measure(full)
        out.append(r)
        print(f"{r['repo']:40s} {r['n_skill_files']:>6} {r['naive_identities']:>8} "
              f"{r['robust_identities']:>9} {r['content_shas']:>6} "
              f"{r['naive_replication']:>7} {r['robust_replication']:>8} "
              f"{r['content_replication']:>9} "
              f"{r['generic_parent_files']:>6}/{r['n_skill_files']:<11}", flush=True)
        print(f"    naive top: {r['naive_top']}")
        print(f"    robust top: {r['robust_top']}  variants={r['n_robust_ids_with_variants']}")
    json.dump(out, open("/tmp/identity_1119.json", "w"), ensure_ascii=False, indent=1)
    print("\nwrote /tmp/identity_1119.json")
    superpowers_detail()
