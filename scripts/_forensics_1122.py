#!/usr/bin/env python3
"""11-22 forensics, part 2:

A. CONTENT DIFF of divergent skill copies — is the per-harness divergence a
   trivial path substitution (188 B delta) or real adaptation (>=1 KB delta)?
B. Continuity: last30days-skill went 0 tag/0 release (11-18) -> 91/85 (11-22)?
C. Release-asset download continuity: plannotator 1-12 (11-18) -> max 1734?
D. Tag->commit->source diff closure for today's new tag/release samples.
"""
import json
import os
import subprocess
import urllib.parse
from collections import defaultdict

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


def blob(path):
    return api(f"repos/{full}/contents/{urllib.parse.quote(path)}", raw=True,
               headers=["Accept: application/vnd.github.raw"])


def diff_group(full, name):
    """Fetch every copy of one skill name and report line-level differences."""
    m = api(f"repos/{full}") or {}
    branch = m.get("default_branch") or "main"
    tree = api(f"repos/{full}/git/trees/{branch}?recursive=1") or {}
    blobs = [b for b in (tree.get("tree") or []) if b.get("type") == "blob"]
    paths = [b.get("path") for b in blobs
             if os.path.basename(b.get("path") or "").lower() == "skill.md"
             and os.path.basename(os.path.dirname(b.get("path") or "")) == name]
    out = []
    for p in sorted(paths):
        txt = api(f"repos/{full}/contents/{urllib.parse.quote(p)}", raw=True,
                  headers=["Accept: application/vnd.github.raw"]) or ""
        out.append({"path": p, "bytes": len(txt.encode()), "text": txt})
    # pairwise-ish: compare each to the first
    base = out[0] if out else None
    for o in out:
        if base is None or o is base:
            o["diff_lines_vs_base"] = 0
            continue
        a = base["text"].splitlines()
        b = o["text"].splitlines()
        import difflib
        sm = difflib.SequenceMatcher(None, a, b)
        ndiff = sum(max(i2 - i1, j2 - j1)
                    for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal")
        o["diff_lines_vs_base"] = ndiff
        o["ratio_vs_base"] = round(sm.quick_ratio(), 3)
        # which lines differ (sample)
        d = list(difflib.unified_diff(a, b, lineterm="", n=0))
        o["diff_sample"] = d[:14]
    return out


print("=" * 100)
print("A. CONTENT DIFF — divergent skill copies")
print("=" * 100)
for full, name in [("backnotprop/plannotator", "plannotator-annotate"),
                   ("backnotprop/plannotator", "plannotator-review"),
                   ("cursor/plugins", "pr-review-canvas"),
                   ("cursor/plugins", "architect"),
                   ("tradermonty/claude-trading-skills", "market-news-analyst")]:
    print(f"\n--- {full} :: {name}")
    rows = diff_group(full, name)
    for r in rows:
        print(f"    {r['bytes']:7d} B  difflines_vs_base={r.get('diff_lines_vs_base')}  "
              f"ratio={r.get('ratio_vs_base')}  {r['path']}")
    if len(rows) >= 2:
        print("    sample diff (vs base):")
        for l in rows[1].get("diff_sample", [])[:12]:
            print("      " + l[:150])

print()
print("=" * 100)
print("B. last30days-skill TAG/RELEASE CONTINUITY")
print("=" * 100)
for full in ["mvanhorn/last30days-skill", "kajisho5/ffmpeg-skill", "GoogleChrome/modern-web-guidance-src"]:
    tags = api(f"repos/{full}/tags", {"per_page": 100}) or []
    rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
    tags = tags if isinstance(tags, list) else []
    rels = rels if isinstance(rels, list) else []
    print(f"\n{full}: tags={len(tags)} releases={len(rels)}")
    print("   first 8 tag names:", [t.get("name") for t in tags[:8]])
    if rels:
        r0 = rels[0]
        print(f"   newest release: {r0.get('tag_name')} prerelease={r0.get('prerelease')} "
              f"published={r0.get('published_at')} assets={len(r0.get('assets') or [])} "
              f"dl_total={sum(a.get('download_count') or 0 for a in (r0.get('assets') or []))}")
        print(f"   oldest fetched release: {rels[-1].get('tag_name')} "
              f"published={rels[-1].get('published_at')}")
    # how many distinct tag commit shas (a repo that fakes tags reuses shas)
    shas = {t.get("commit", {}).get("sha") for t in tags}
    print(f"   distinct tag commit shas: {len(shas)} / {len(tags)} tags")

print()
print("=" * 100)
print("C. RELEASE ASSET DOWNLOAD CONTINUITY (11-18 recorded vs 11-22 live)")
print("=" * 100)
for full in ["backnotprop/plannotator", "alibaba/open-code-review", "getarcaneapp/arcane"]:
    rels = api(f"repos/{full}/releases", {"per_page": 100}) or []
    rels = rels if isinstance(rels, list) else []
    if not rels:
        print(f"{full}: no releases")
        continue
    rows = []
    for r in rels[:8]:
        assets = r.get("assets") or []
        dl = [a.get("download_count") or 0 for a in assets]
        rows.append((r.get("tag_name"), r.get("published_at"), len(assets),
                     sum(dl), max(dl) if dl else 0))
    print(f"\n{full} (newest 8 releases):")
    for t, p, na, tot, mx in rows:
        print(f"   {str(t):18s} {str(p)[:10]} assets={na:3d} dl_total={tot:7d} dl_max={mx:7d}")
