#!/usr/bin/env python3
"""11-22 — final: harness/plugin-manifest census (same caliber as the 11-18
report's "harness 清单数"), plus planted-repo edge cases and the two new
release-asset shapes (.sig and .hdiff).
"""
import json
import os
import subprocess
import urllib.parse
from collections import Counter

ENV = dict(os.environ, HOME="/home/lohasle")


def api(path, params=None, raw=False, headers=None, timeout=120):
    url = path
    if params:
        url = path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    cmd = ["gh", "api"]
    for h in (headers or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, timeout=120)
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


MANIFEST = (
    ".claude-plugin/plugin.json", ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json", ".gemini/config.yaml", ".grok-plugin/plugin.json",
    ".kiro-plugin/plugin.json", ".opencode/plugin.json", ".windsurf-plugin/plugin.json",
    ".devin-plugin/plugin.json", ".kimi-plugin/plugin.json", ".muse-plugin/plugin.json",
    ".antigravity-plugin/plugin.json", ".hermes-plugin/plugin.yaml",
    ".agents/plugins/marketplace.json", "gemini-extension.json",
)

print("=" * 100)
print("HARNESS / PLUGIN-MANIFEST CENSUS (same caliber as 11-18's 'harness 清单数')")
print("=" * 100)
REPOS = ["affaan-m/ECC", "obra/superpowers", "cursor/plugins", "backnotprop/plannotator",
         "mvanhorn/last30days-skill", "google-labs-code/stitch-skills",
         "alibaba/open-code-review", "tradermonty/claude-trading-skills",
         "HKUDS/CLI-Anything", "Tracer-Cloud/opensre", "elementalsouls/Claude-BugHunter",
         "kajisho5/ffmpeg-skill", "GoogleChrome/modern-web-guidance-src",
         "ChromeDevTools/chrome-devtools-mcp", "ag-ui-protocol/ag-ui"]
for full in REPOS:
    m = api(f"repos/{full}") or {}
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    paths = [b.get("path") for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    hits = sorted({p for p in paths if p in MANIFEST})
    # per-harness skill roots
    roots = sorted({p.split("/")[0] for p in paths
                    if p.lower().endswith("skill.md") and "/" in p})
    rm = api(f"repos/{full}/readme", raw=True,
             headers=["Accept: application/vnd.github.raw"]) or ""
    cmds = sorted({c for c in __import__("re").findall(
        r"(npx\s+skills\s+add[^\n`\"]{0,45}|marketplace\s+add[^\n`\"]{0,45})", rm)})
    print(f"{full:42s} manifests={len(hits):2d} {hits if hits else ''}")
    print(f"{'':42s} skill_roots={len(roots):2d} {roots[:9]}")
    print(f"{'':42s} install_cmds={cmds}")

print()
print("=" * 100)
print("PLANTED-REPO EDGE CASES: minimind (49 blobs) + smallest trees")
print("=" * 100)
for full in ["jingyaogong/minimind", "google-labs-code/stitch-skills",
              "mjmirza/app-store-compliance", "pookjw/HermesEnabler"]:
    m = api(f"repos/{full}") or {}
    tree = api(f"repos/{full}/git/trees/{m.get('default_branch','main')}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    exts = Counter(os.path.splitext(b.get("path", ""))[1].lower() or "<none>" for b in blobs)
    code = sum(v for k, v in exts.items() if k in (".py", ".go", ".rs", ".ts", ".js", ".tsx",
                                                   ".jsx", ".java", ".c", ".cpp", ".rb", ".swift",
                                                   ".m", ".mm", ".dart", ".sh", ".php", ".scala"))
    print(f"  {full:40s} blobs={len(blobs):5d} code_files={code:5d} "
          f"exts={dict(exts.most_common(7))}")

print()
print("=" * 100)
print("NEW RELEASE-ASSET SHAPES: .sig (autoclip) and .hdiff (Ghost-Downloader-3)")
print("=" * 100)
for full in ["zhouxiaoka/autoclip", "XiaoYouChR/Ghost-Downloader-3"]:
    rels = api(f"repos/{full}/releases", {"per_page": 3}) or []
    rels = rels if isinstance(rels, list) else []
    for r in rels[:2]:
        names = [a.get("name") for a in (r.get("assets") or [])]
        print(f"  {full} :: {r.get('tag_name')}")
        for n in names:
            print(f"      {n}")
        print()
