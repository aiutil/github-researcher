#!/usr/bin/env python3
"""Same-discriminator re-measurement for the 2026-11-19 cohort, using the
EXACT method from scripts/_forensics_2026_11_18.py and
scripts/_identity_2026_11_18.py so that today's numbers are directly
comparable with the 11-18 report.

  * skill identity = parent directory name; replication = files / identities
  * harness manifest dirs = PREFIX match (.claude-plugin/, .codex-plugin/,
    .cursor-plugin/, .plugin/, .grok-plugin/, .gemini/, .windsurf/, .opencode/)
  * install flags = substring presence in README
  * tag/release gap = tag names not present in release tag_name set
  * blob-sha duplication groups

Output: /tmp/forensics_1119.json
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")

COHORT = [
    "elementalsouls/Claude-BugHunter",
    "cursor/plugins",
    "HKUDS/CLI-Anything",
    "mvanhorn/last30days-skill",
    "getarcaneapp/arcane",
    "NVIDIA/SkillEvaluator",
    "nvm-sh/nvm",
    "astral-sh/uv",
    "google-research/paper-orchestra",
    "google-labs-code/stitch-skills",
    "sveltejs/svelte",
    "jquery/jquery",
    "appwrite/appwrite",
    "openvinotoolkit/openvino",
    "obra/superpowers",
    "affaan-m/ECC",
    "DeanChensj/jiangshan-map",
    "n8n-io/n8n",
    "solidjs/solid",
    "punkpeye/awesome-mcp-servers",
    "GoogleChrome/modern-web-guidance-src",
    "backnotprop/plannotator",
    "meta/astryx",
    "we-promise/sure",
    "alibaba/open-code-review",
    "tradermonty/claude-trading-skills",
    "ChromeDevTools/chrome-devtools-mcp",
    "anthropics/skills",
    "ZhuLinsen/daily_stock_analysis",
    "ag-ui-protocol/ag-ui",
    "vercel-labs/agent-browser",
    "openai/codex-security",
    "dream-num/univer",
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


HARNESS_PREFIXES = (".claude-plugin", ".codex-plugin", ".cursor-plugin", ".plugin",
                     ".grok-plugin", ".gemini", ".windsurf", ".opencode")


def measure(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") or "" for b in blobs]

    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
    ident = defaultdict(list)
    for b in skills:
        p = b.get("path") or ""
        parent = os.path.basename(os.path.dirname(p)) if "/" in p else "<root>"
        ident[parent].append((p, b.get("sha"), b.get("size")))
    sha_counter = Counter(b.get("sha") for b in skills)
    dup_sha = {s: c for s, c in sha_counter.items() if c > 1}
    replicated = {k: v for k, v in ident.items() if len(v) > 1}
    skill_bytes = [b.get("size") or 0 for b in skills]

    harness = Counter()
    for p in paths:
        for h in HARNESS_PREFIXES:
            if p.startswith(h + "/"):
                harness[h] += 1

    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""

    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    rel = rel if isinstance(rel, list) else []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    tags = tags if isinstance(tags, list) else []
    rel_tags = {r.get("tag_name") for r in rel}
    tag_names = [t.get("name") for t in tags]

    contribs = api(f"repos/{full}/contributors", {"per_page": 20}) or []
    contribs = contribs if isinstance(contribs, list) else []

    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "size_kb": m.get("size"),
        "language": m.get("language"),
        "license": (m.get("license") or {}).get("spdx_id"),
        "created_at": m.get("created_at"),
        "pushed_at": m.get("pushed_at"),
        "description": m.get("description"),
        "homepage": m.get("homepage"),
        "topics": m.get("topics", []),
        "n_blobs": len(blobs),
        "truncated_tree": tree.get("truncated"),
        "n_skills": len(skills),
        "n_identities": len(ident),
        "n_identities_replicated": len(replicated),
        "n_files_in_replicated": sum(len(v) for v in replicated.values()),
        "n_distinct_blob_shas": len(sha_counter),
        "n_dup_blobsha_groups": len(dup_sha),
        "top_dup_blobsha": sorted(dup_sha.values(), reverse=True)[:8],
        "biggest_replicated": sorted(((len(v), k) for k, v in ident.items()), reverse=True)[:8],
        "skill_bytes_total": sum(skill_bytes),
        "skill_bytes_avg": (sum(skill_bytes) // len(skill_bytes)) if skill_bytes else 0,
        "skill_topdirs": dict(Counter(
            (p.split("/")[0] if "/" in p else "<root>")
            for p in [b.get("path") or "" for b in skills]).most_common(10)),
        "harness_files": dict(harness),
        "n_harness_manifests": len(harness),
        "install": {
            "npx_skills_add": "npx skills add" in rm,
            "plugin_marketplace_add": "marketplace add" in rm,
            "claude_plugin_install": "claude plugin" in rm,
            "codex": "codex" in rm.lower(),
            "cursor": "cursor" in rm.lower(),
            "opencode": "opencode" in rm.lower(),
        },
        "n_tags": len(tag_names),
        "n_releases": len(rel),
        "tags_without_release": [t for t in tag_names if t not in rel_tags][:25],
        "contributors": [(c.get("login"), c.get("contributions")) for c in contribs][:12],
    }


def main():
    out = []
    for full in COHORT:
        r = measure(full)
        out.append(r)
        print(f"{r['repo']:44s} *{r['stars']:>7,} sk={r['n_skills']:>4}/{r['n_identities']:>4} "
              f"dupgroups={r['n_dup_blobsha_groups']:>3} harness={r['n_harness_manifests']} "
              f"tag/rel={r['n_tags']}/{r['n_releases']} "
              f"npx={'Y' if r['install']['npx_skills_add'] else 'n'}"
              f" mkt={'Y' if r['install']['plugin_marketplace_add'] else 'n'}", flush=True)
    json.dump(out, open("/tmp/forensics_1119.json", "w"), ensure_ascii=False, indent=1)
    print("wrote /tmp/forensics_1119.json")


if __name__ == "__main__":
    main()
