#!/usr/bin/env python3
"""Deep evidence collection for the 2026-11-19 selected cohort.

Q1. RELEASE-ASSET AS A DISCIMINATOR: does the release asset *set* evolve
    across versions (i.e. is the release channel actually maintained), and
    is there an SBOM/checksum?  Sample 6 releases per repo.

Q2. SKILL DISTRIBUTION SURFACE re-measured with the 11-18 exact method:
    harness manifest prefixes at REPO ROOT, install-command flags.

Q3. CONTINUITY: for the 9 projects archived on 11-18, what changed in
    24h (stars, blobs, releases, workflows, skills)?

Q4. TIER-STRUCTURE (NVIDIA/SkillEvaluator): read the CI workflows that
    implement the "tiers" and the multi-tier CI template claim.

Output: /tmp/deep_1119.json
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

ENV = dict(os.environ, HOME="/home/lohasle")

SKILL_REPOS = [
    "NVIDIA/SkillEvaluator", "HKUDS/CLI-Anything", "cursor/plugins",
    "elementalsouls/Claude-BugHunter", "openai/codex-security",
    "vercel-labs/agent-browser", "ag-ui-protocol/ag-ui",
    "appwrite/appwrite", "ChromeDevTools/chrome-devtools-mcp",
    "google-labs-code/stitch-skills", "obra/superpowers",
    "tradermonty/claude-trading-skills",
]

ASSET_REPOS = [
    "NVIDIA/SkillEvaluator", "HKUDS/CLI-Anything", "openai/codex-security",
    "vercel-labs/agent-browser", "n8n-io/n8n", "astral-sh/uv",
    "ZhuLinsen/daily_stock_analysis", "mvanhorn/last30days-skill",
    "we-promise/sure", "meta/astryx", "appwrite/appwrite",
    "backnotprop/plannotator", "getarcaneapp/arcane",
    "alibaba/open-code-review", "GoogleChrome/modern-web-guidance-src",
]

CONTINUITY = {
    "GoogleChrome/modern-web-guidance-src": 8414,
    "affaan-m/ECC": 305425,
    "backnotprop/plannotator": 13035,
    "alibaba/open-code-review": 53682,
    "google-research/paper-orchestra": 2884,
    "getarcaneapp/arcane": 9275,
    "Tencent/LoopForge": 3071,
    "elementalsouls/Claude-BugHunter": 9120,
    "mvanhorn/last30days-skill": 68964,
}

HARNESS_PREFIXES = (".claude-plugin", ".codex-plugin", ".cursor-plugin", ".plugin",
                     ".grok-plugin", ".gemini", ".windsurf", ".opencode")


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


def asset_evolution(full):
    rel = api(f"repos/{full}/releases", {"per_page": 30}) or []
    rel = rel if isinstance(rel, list) else []
    rows = []
    for r in rel[:8]:
        assets = r.get("assets") or []
        names = sorted(a.get("name") or "" for a in assets)
        # strip the version string so we can compare asset NAMES across versions
        import re as _re
        def norm(n):
            n = _re.sub(r"v?\d+\.\d+[\.\d]*", "VER", n)
            n = _re.sub(r"\d{6,}", "NUM", n)
            return n
        rows.append({
            "tag": r.get("tag_name"),
            "published": r.get("published_at"),
            "prerelease": r.get("prerelease"),
            "n_assets": len(assets),
            "total_bytes": sum(a.get("size") or 0 for a in assets),
            "total_downloads": sum(a.get("download_count") or 0 for a in assets),
            "max_downloads": max([a.get("download_count") or 0 for a in assets] or [0]),
            "normalized_names": sorted({norm(n) for n in names}),
            "has_sbom": any("sbom" in (n or "").lower() or "cyclonedx" in (n or "").lower()
                            or "spdx" in (n or "").lower() for n in names),
            "has_checksum": any(_re.search(r"sha256|checksum|\.sha", n or "", _re.I)
                                for n in names),
            "sample_names": names[:8],
        })
    # does the normalized asset set evolve across versions?
    sets = [frozenset(r["normalized_names"]) for r in rows]
    evolving = len(set(sets)) > 1
    return {
        "repo": full,
        "n_releases_sampled": len(rows),
        "asset_set_evolves": evolving,
        "distinct_asset_sets": len(set(sets)),
        "rows": rows,
    }


def skill_surface(full):
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
        ident[parent].append((p, b.get("sha")))
    sha_counter = Counter(b.get("sha") for b in skills)
    dup = {s: c for s, c in sha_counter.items() if c > 1}
    harness = Counter()
    for p in paths:
        for h in HARNESS_PREFIXES:
            if p.startswith(h + "/"):
                harness[h] += 1
    # root-level harness manifest markers (e.g. .claude-plugin/plugin.json)
    root_markers = sorted({p for p in paths if p.endswith("plugin.json")
                           or p.endswith("marketplace.json")})
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    wf = api(f"repos/{full}/contents/.github/workflows") or []
    return {
        "repo": full,
        "stars": m.get("stargazers_count"),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "blobs": len(blobs),
        "truncated": tree.get("truncated"),
        "n_skills": len(skills),
        "n_identities": len(ident),
        "replication": round(len(skills) / len(ident), 2) if ident else 0,
        "n_dup_blobsha_groups": len(dup),
        "top_dup": sorted(dup.values(), reverse=True)[:8],
        "biggest_replicated": sorted(((len(v), k) for k, v in ident.items()), reverse=True)[:8],
        "harness_files": dict(harness),
        "n_harness_manifests": len(harness),
        "root_markers": root_markers[:10],
        "install": {
            "npx_skills_add": "npx skills add" in rm,
            "marketplace_add": "marketplace add" in rm,
            "claude_plugin": "claude plugin" in rm,
        },
        "workflows": [w.get("name") for w in wf] if isinstance(wf, list) else [],
        "skill_topdirs": dict(Counter(
            (p.split("/")[0] if "/" in p else "<root>")
            for p in [b.get("path") or "" for b in skills]).most_common(8)),
    }


def continuity(full, prev_stars):
    m = api(f"repos/{full}") or {}
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    rel = rel if isinstance(rel, list) else []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    tags = tags if isinstance(tags, list) else []
    wf = api(f"repos/{full}/contents/.github/workflows") or []
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch') or 'main'}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    skills = [b for b in blobs if os.path.basename(b.get("path") or "") == "SKILL.md"]
    ident = {os.path.basename(os.path.dirname(b.get("path") or "")) for b in skills}
    st = m.get("stargazers_count") or 0
    return {
        "repo": full,
        "prev_stars_1118": prev_stars,
        "stars_now": st,
        "delta": st - prev_stars,
        "delta_pct": round((st - prev_stars) / prev_stars * 100, 2),
        "forks": m.get("forks_count"),
        "subs": m.get("subscribers_count"),
        "oi": m.get("open_issues_count"),
        "blobs": len(blobs),
        "n_tags": len(tags),
        "n_releases": len(rel),
        "n_workflows": len(wf) if isinstance(wf, list) else 0,
        "n_skills": len(skills),
        "n_identities": len(ident),
        "pushed_at": m.get("pushed_at"),
        "license": (m.get("license") or {}).get("spdx_id"),
    }


def main():
    out = {"assets": [], "skills": [], "continuity": []}
    print("### ASSET EVOLUTION", flush=True)
    for full in ASSET_REPOS:
        r = asset_evolution(full)
        out["assets"].append(r)
        head = r["rows"][0] if r["rows"] else {}
        print(f"{full:44s} rel={r['n_releases_sampled']:>2} evolves={r['asset_set_evolves']} "
              f"distinct_sets={r['distinct_asset_sets']} "
              f"latest_assets={head.get('n_assets')} dl={head.get('total_downloads')} "
              f"sbom={head.get('has_sbom')} chk={head.get('has_checksum')}", flush=True)

    print("\n### SKILL SURFACE (11-18 method)", flush=True)
    for full in SKILL_REPOS:
        r = skill_surface(full)
        out["skills"].append(r)
        print(f"{full:44s} sk={r['n_skills']:>4}/{r['n_identities']:>4} repl={r['replication']:>5} "
              f"harness={r['n_harness_manifests']} {list(r['harness_files'])} "
              f"npx={'Y' if r['install']['npx_skills_add'] else 'n'} "
              f"mkt={'Y' if r['install']['marketplace_add'] else 'n'} "
              f"root={r['root_markers'][:3]}", flush=True)

    print("\n### CONTINUITY vs 11-18", flush=True)
    for full, prev in CONTINUITY.items():
        r = continuity(full, prev)
        out["continuity"].append(r)
        print(f"{full:44s} {prev:>8,} -> {r['stars_now']:>8,} ({r['delta_pct']:+.1f}%) "
              f"rel={r['n_releases']:>3} tag={r['n_tags']:>3} wf={r['n_workflows']:>2} "
              f"sk={r['n_skills']:>4}/{r['n_identities']:>4} blobs={r['blobs']:>6,} "
              f"oi={r['oi']}", flush=True)

    json.dump(out, open("/tmp/deep_1119.json", "w"), ensure_ascii=False, indent=1)
    print("\nwrote /tmp/deep_1119.json")


if __name__ == "__main__":
    main()
