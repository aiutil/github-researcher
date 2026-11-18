#!/usr/bin/env python3
"""Focused forensics for 2026-11-18.

Q1. Release ASSET anatomy — 36 assets/release (plannotator), 41 (arcane), 7
    (open-code-review): real build artifacts or bulk filler?
Q2. tag -> release asymmetry: modern-web-guidance-src has 100 tags but 1
    release (tag 'audit-data', prerelease).
Q3. Skill DENSITY: SKILL.md count vs total blobs — is the "skills" number a
    substance metric or a vanity counter?
Q4. paper-orchestra: 8 commits, 56 blobs, 0 releases, 2.8k stars.
"""

import json
import os
import subprocess
import sys
import urllib.parse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=90):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=timeout)
    if p.returncode != 0:
        return None
    if raw:
        return p.stdout
    try:
        return json.loads(p.stdout)
    except Exception:  # noqa: BLE001
        return None


def asset_anatomy(full, n=3):
    rel = api(f"repos/{full}/releases", {"per_page": 5}) or []
    if not isinstance(rel, list):
        return {"repo": full, "error": "no releases"}
    out = []
    for r in rel[:n]:
        assets = r.get("assets") or []
        exts = Counter(os.path.splitext(a.get("name", ""))[1].lower() for a in assets)
        sizes = sorted((a.get("size") or 0) for a in assets)
        out.append({
            "tag": r.get("tag_name"),
            "n_assets": len(assets),
            "exts": dict(exts),
            "total_bytes": sum(sizes),
            "min_size": sizes[0] if sizes else 0,
            "max_size": sizes[-1] if sizes else 0,
            "names": [a.get("name") for a in assets[:8]],
            "download_counts": sorted((a.get("download_count") or 0) for a in assets),
            "asset_created": sorted({a.get("created_at") for a in assets})[:2],
        })
    return {"repo": full, "releases": out}


def skill_density(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") for b in blobs if b.get("path")]
    skills = [p for p in paths if os.path.basename(p) == "SKILL.md"]
    skill_bytes = [b.get("size") or 0 for b in blobs
                   if os.path.basename(b.get("path") or "") == "SKILL.md"]
    # where do skills live?
    top = Counter()
    for p in skills:
        parts = p.split("/")
        top[parts[0] if len(parts) > 1 else "<root>"] += 1
    # harness manifests
    harness = Counter()
    for p in paths:
        for h in (".claude-plugin", ".codex-plugin", ".cursor-plugin", ".plugin",
                  ".grok-plugin", ".gemini", ".windsurf", ".opencode"):
            if p.startswith(h + "/"):
                harness[h] += 1
    # install commands
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    install = {
        "npx_skills_add": "npx skills add" in rm,
        "plugin_marketplace_add": "marketplace add" in rm,
        "claude_plugin_install": "claude plugin" in rm,
        "codex": "codex" in rm.lower(),
        "cursor": "cursor" in rm.lower(),
        "opencode": "opencode" in rm.lower(),
    }
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
        "n_blobs": len(blobs),
        "truncated_tree": tree.get("truncated"),
        "n_skills": len(skills),
        "skill_density_pct": round(100 * len(skills) / len(blobs), 2) if blobs else 0,
        "skill_bytes_total": sum(skill_bytes),
        "skill_bytes_avg": (sum(skill_bytes) // len(skill_bytes)) if skill_bytes else 0,
        "skill_topdirs": dict(top.most_common(10)),
        "harness_files": dict(harness),
        "install": install,
        "skill_sample": skills[:12],
    }


def tag_release_gap(full):
    m = api(f"repos/{full}") or {}
    rel = api(f"repos/{full}/releases", {"per_page": 100}) or []
    if not isinstance(rel, list):
        rel = []
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    if not isinstance(tags, list):
        tags = []
    rel_tags = {r.get("tag_name") for r in rel}
    tag_names = [t.get("name") for t in tags]
    return {
        "repo": full,
        "n_tags": len(tag_names),
        "n_releases": len(rel),
        "tags_without_release": [t for t in tag_names if t not in rel_tags][:20],
        "n_tags_without_release": len([t for t in tag_names if t not in rel_tags]),
        "releases_without_tag": [t for t in rel_tags if t not in set(tag_names)],
        "tag_sample": tag_names[:15],
    }


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    if which in ("all", "assets"):
        print("========== Q1: release ASSET anatomy ==========")
        targets = ["backnotprop/plannotator", "getarcaneapp/arcane",
                   "alibaba/open-code-review", "we-promise/sure",
                   "GoogleChrome/modern-web-guidance-src"]
        with ThreadPoolExecutor(max_workers=5) as ex:
            for r in ex.map(lambda t: asset_anatomy(t), targets):
                print(f"\n--- {r['repo']} ---")
                if "error" in r:
                    print("  ", r["error"])
                    continue
                for rel in r["releases"]:
                    print(f"  tag={rel['tag']:<24} assets={rel['n_assets']:<4} "
                          f"total={rel['total_bytes']/1e6:.2f}MB "
                          f"min={rel['min_size']} max={rel['max_size']}")
                    print(f"    exts={rel['exts']}")
                    print(f"    names={rel['names']}")
                    print(f"    downloads={rel['download_counts'][:12]}")

    if which in ("all", "density"):
        print("\n========== Q3: skill density ==========")
        targets = ["affaan-m/ECC", "cursor/plugins", "tradermonty/claude-trading-skills",
                   "elementalsouls/Claude-BugHunter", "backnotprop/plannotator",
                   "Tencent/LoopForge", "anthropics/skills", "obra/superpowers",
                   "addyosmani/agent-skills", "GoogleChrome/modern-web-guidance-src",
                   "google-labs-code/stitch-skills", "mvanhorn/last30days-skill"]
        with ThreadPoolExecutor(max_workers=5) as ex:
            rows = list(ex.map(skill_density, targets))
        print(f"{'repo':<44}{'skills':>7}{'blobs':>7}{'dens%':>7}{'avgB':>7}"
              f"{'npx':>5}{'mkt':>5}{'cc':>5}  harness")
        for r in rows:
            i = r["install"]
            print(f"{r['repo']:<44}{r['n_skills']:>7}{r['n_blobs']:>7}"
                  f"{r['skill_density_pct']:>7.1f}{r['skill_bytes_avg']:>7}"
                  f"{str(i['npx_skills_add'])[0]:>5}{str(i['plugin_marketplace_add'])[0]:>5}"
                  f"{str(i['claude_plugin_install'])[0]:>5}  {r['harness_files']}")
        for r in rows:
            print(f"\n--- {r['repo']} --- stars={r['stars']} subs={r['subs']} "
                  f"oi={r['oi']} lang={r['language']} lic={r['license']} "
                  f"created={r['created_at']} pushed={r['pushed_at']} "
                  f"skill_bytes_total={r['skill_bytes_total']}")
            print(f"    topdirs={r['skill_topdirs']}")
            print(f"    install={r['install']}")
            print(f"    sample={r['skill_sample'][:8]}")

    if which in ("all", "gap"):
        print("\n========== Q2: tag -> release gap ==========")
        for t in ["GoogleChrome/modern-web-guidance-src", "we-promise/sure",
                  "obra/superpowers", "Tencent/LoopForge",
                  "affaan-m/ECC", "addyosmani/agent-skills"]:
            r = tag_release_gap(t)
            print(f"  {r['repo']:<42} tags={r['n_tags']:<5} rel={r['n_releases']:<5} "
                  f"tags_without_release={r['n_tags_without_release']:<5} "
                  f"sample={r['tags_without_release'][:6]}")
