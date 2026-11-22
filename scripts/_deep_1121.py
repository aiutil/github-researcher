#!/usr/bin/env python3
"""Deep second-pass for the 2026-11-20 daily.

A) Same-caliber re-test of the 11-18 skill cohort (install protocol,
   skill replication, harness manifests) so today's numbers are comparable
   with the 11-18 table rather than a different sample.

B) Tag -> commit -> source-diff closure sampling for every repo whose
   tag count exceeds its release count, to separate "tag-heavy repo that
   never cut releases" from "tag/release counts are simply capped".

C) README heads for the candidate key projects.

Output: /tmp/deep_1121.json
"""
import hashlib
import json
import os
import re
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

ENV = dict(os.environ, HOME="/home/lohasle")
OUT = "/tmp/deep_1121.json"

# The exact 12-project skill cohort measured on 11-18 (daily/2026-11-18.md).
COHORT = [
    "affaan-m/ECC",
    "elementalsouls/Claude-BugHunter",
    "Tencent/LoopForge",
    "backnotprop/plannotator",
    "cursor/plugins",
    "tradermonty/claude-trading-skills",
    "alibaba/open-code-review",
    "obra/superpowers",
    "addyosmani/agent-skills",
    "anthropics/skills",
    "google-labs-code/stitch-skills",
    "mvanhorn/last30days-skill",
]

# Repos sampled for tag -> commit -> diff closure.
DIFF_SAMPLE = [
    "obra/superpowers",
    "firecrawl/firecrawl",
    "mvanhorn/last30days-skill",
    "nginx/nginx",
    "meta/astryx",
    "ag-ui-protocol/ag-ui",
    "we-promise/sure",
    "XiaoYouChR/Ghost-Downloader-3",
    "openvinotoolkit/openvino",
    "zhouxiaoka/autoclip",
    "GoogleChrome/modern-web-guidance-src",
    "alibaba/open-code-review",
    "backnotprop/plannotator",
    "kajisho5/ffmpeg-skill",
]

SRC_EXT = {".py", ".go", ".ts", ".tsx", ".js", ".jsx", ".rs", ".java", ".c", ".cc",
           ".cpp", ".h", ".hpp", ".cs", ".rb", ".sh", ".swift", ".kt", ".scala",
           ".php", ".m", ".mm", ".vue", ".svelte", ".lua", ".ex", ".exs"}


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


SKILL_RE = re.compile(r"(^|/)SKILL\.md$", re.I)
HARNESS_DIRS = ("claude", "codex", "cursor", "gemini", "copilot", "windsurf",
                "amp", "zed", "opencode", "aider", "droid", "qwen", "codex-cli",
                "claude-code", "antigravity", "kiro", "trae", "augment")


def skill_and_harness(full):
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path", "") for b in blobs]
    skill_blobs = [b for b in blobs if SKILL_RE.search(b.get("path", ""))]
    skill_by_dir = {}
    for b in skill_blobs:
        p = b.get("path", "")
        parent = p.rsplit("/", 1)[0] if "/" in p else "<root>"
        skill_by_dir.setdefault(parent, set()).add(b.get("sha"))
    n_ident = len({frozenset(v) for v in skill_by_dir.values()})
    harness = sorted({hp for p in paths for hp in HARNESS_DIRS if hp in p.split("/")})
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    cmds = sorted({c for c in re.findall(
        r"(npx\s+skills\s+add[^\n`\"]{0,70}|marketplace\s+add[^\n`\"]{0,70}|"
        r"pip\s+install\s+[a-zA-Z0-9_.\-]+|npm\s+i(?:nstall)?\s+-g\s+[a-zA-Z0-9_.\-@]+|"
        r"cargo\s+install\s+[a-zA-Z0-9_.\-]+|brew\s+install\s+[a-zA-Z0-9_.\-]+)", rm)})
    # also count distinct harness manifest files by name
    manifests = sorted({os.path.basename(p) for p in paths
                        if os.path.basename(p) in
                        ("plugin.json", "marketplace.json", "gemini-extension.json",
                         "server.json", "manifest.json", "agent.json", "config.yaml")})
    return {
        "full_name": full,
        "stars": m.get("stargazers_count"),
        "n_blobs": len(blobs),
        "n_skill_files": len(skill_blobs),
        "n_skill_identities": n_ident,
        "skill_replication": round(len(skill_blobs) / n_ident, 2) if n_ident else 0,
        "harness_dirs": harness,
        "n_harness": len(harness),
        "install_cmds": cmds,
        "has_npx_skills": any("skills add" in c for c in cmds),
        "has_marketplace": any("marketplace" in c for c in cmds),
        "manifest_files": manifests,
        "readme_len": len(rm),
        "readme_md5": hashlib.md5(rm.encode("utf-8", "replace")).hexdigest(),
        "readme_head": rm[:3000],
    }


def diff_closure(full, n=6):
    """Sample up to n git tags, resolve to commit, inspect that commit's
    changed files and its parent's changed files."""
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    if not isinstance(tags, list) or not tags:
        return {"full_name": full, "n_tags_sampled": 0}
    step = max(1, len(tags) // n)
    picked = tags[::step][:n]
    rows = []
    for t in picked:
        sha = t.get("commit", {}).get("sha")
        name = t.get("name")
        c = api(f"repos/{full}/commits/{sha}") or {}
        files = c.get("files") or []
        src = [f for f in files if os.path.splitext(f.get("filename", ""))[1].lower() in SRC_EXT]
        parents = c.get("parents") or []
        pfiles = []
        if parents:
            pc = api(f"repos/{full}/commits/{parents[0].get('sha')}") or {}
            pfiles = pc.get("files") or []
        psrc = [f for f in pfiles if os.path.splitext(f.get("filename", ""))[1].lower() in SRC_EXT]
        rows.append({
            "tag": name,
            "n_files": len(files),
            "n_src": len(src),
            "src_examples": [f.get("filename") for f in src][:4],
            "parent_files": len(pfiles),
            "parent_src": len(psrc),
            "parent_src_examples": [f.get("filename") for f in psrc][:4],
            "msg": ((c.get("commit") or {}).get("message") or "").split("\n")[0][:110],
        })
    return {"full_name": full, "n_tags_sampled": len(rows), "samples": rows}


def main():
    res = {"cohort": [], "diff": []}
    with ThreadPoolExecutor(max_workers=5) as ex:
        for r in ex.map(skill_and_harness, COHORT):
            res["cohort"].append(r)
            print(f"cohort {r['full_name']:42s} sk={r['n_skill_files']}/{r['n_skill_identities']} "
                  f"repl={r['skill_replication']} harn={r['n_harness']} "
                  f"npx={r['has_npx_skills']} mkt={r['has_marketplace']}", flush=True)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(diff_closure, DIFF_SAMPLE):
            res["diff"].append(r)
            print(f"diff {r['full_name']:42s} sampled={r.get('n_tags_sampled')}", flush=True)
    json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote -> {OUT}")


if __name__ == "__main__":
    main()
