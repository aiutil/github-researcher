#!/usr/bin/env python3
"""Batch meta + evidence for 2026-11-04 daily candidates."""
import importlib.util, json, sys, subprocess, os

spec = importlib.util.spec_from_file_location("c", "scripts/_collect_2026_11_03.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

TRACK = [
    "interplains/Zero-Breach-Toolkit", "interplains/zero-breach",
    "haydenschmitty/floorplan", "NyxFoundation/nyxis",
    "kuraeow/ultratears", "valentderah/totk-pc-recomp",
    "NotRexed/SkyboundTotk", "Shagg88/COGBox",
    "Gezine/CivSwitch", "SAOS-3624/dsh-see-now",
    "unclebob/ub-mode", "rddmwmddr/android-ad-cleaner",
    "DenisSergeevitch/ex-ussr-kinship-research", "trailofbits/brotli-checker",
    "YoyoLin008/mcreplay", "songjianyang/xss-audit",
    "deepseek-ai/DeepInfer", "colinhacks/reylo",
    "UniXNU/UniXNU", "theorem-labs/oss-verify-proofs",
    "xevrion/hatchzip", "Snapintosh/Snapintosh",
]

CAND = [
    "chadandyou/jrames", "Renly1994/xiaotang-daozai", "govijr/terminal-mac",
    "justrach/nanolight", "caru-ini/stack-diagram", "mromidev/claude-animated-shorts",
    "AssassinCreator/steam-stash-value-report-card",
    "wideeyededi/uncensored-nsfw-ai-video-api",
    "SplendorHornbill/windows-animated-wallpapers",
]


def ncommits(full):
    h = subprocess.run(["gh", "api", "-i", f"repos/{full}/commits?per_page=1"],
                       capture_output=True, text=True,
                       env={**os.environ, "HOME": "/home/lohasle"}).stdout
    import re
    mm = re.search(r'page=(\d+)>; rel="last"', h)
    return int(mm.group(1)) if mm else 1


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "meta":
        for full in (TRACK if len(sys.argv) < 3 else sys.argv[2:]):
            r = m.japi(f"repos/{full}")
            if not r:
                print(f"FAILED {full}")
                continue
            contrib = m.japi(f"repos/{full}/contributors?per_page=100&anon=false")
            rel = m.japi(f"repos/{full}/releases?per_page=100")
            tree = m.japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
            blobs = [e for e in tree.get("tree", []) if e["type"] == "blob"]
            print(f"{full}")
            print(f"  stars={r['stargazers_count']} forks={r['forks_count']} subs={r['subscribers_count']} "
                  f"oi={r['open_issues_count']} size={r['size']}KB lang={r['language']} "
                  f"lic={(r.get('license') or {}).get('spdx_id')}")
            print(f"  created={r['created_at']} pushed={r['pushed_at']} owner={r['owner']['login']}({r['owner']['type']}) "
                  f"archived={r['archived']}")
            print(f"  contributors={len(contrib) if isinstance(contrib,list) else 'FAIL'} "
                  f"releases={len(rel) if isinstance(rel,list) else 'FAIL'} "
                  f"commits={ncommits(full)} blobs={len(blobs)} truncated={tree.get('truncated')}")
            print(f"  topics={r.get('topics')}")
            print(f"  desc={r.get('description')}")
            print(f"  homepage={r.get('homepage')}")
    elif mode == "releases":
        for full in sys.argv[2:]:
            rel = m.japi(f"repos/{full}/releases?per_page=30") or []
            print("=" * 90)
            print(f"RELEASES {full} count={len(rel)}")
            for r in rel[:12]:
                body = (r.get("body") or "")[:300].replace("\r", "").replace("\n", " ")
                print(f"  {r['tag_name']:<16} {r['published_at'][:19]} assets={len(r.get('assets',[]))} "
                      f"dl={sum(a['download_count'] for a in r.get('assets',[]))}")
                if body.strip():
                    print(f"      {body}")
    elif mode == "issues":
        for full in sys.argv[2:]:
            iss = m.japi(f"repos/{full}/issues?state=all&per_page=30")
            print("=" * 90)
            print(f"ISSUES {full} count={len(iss) if isinstance(iss,list) else 'FAIL'}")
            for i in (iss or [])[:30]:
                tag = "PR " if "pull_request" in i else "ISS "
                print(f"  {tag}#{i['number']:<4} {i['state']:<6} {i['title'][:85]} "
                      f"[{i['user']['login']}] {i['created_at'][:10]}")
    elif mode == "tree":
        for full in sys.argv[2:]:
            t = m.japi(f"repos/{full}/git/trees/HEAD?recursive=1") or {}
            paths = [e["path"] for e in t.get("tree", [])]
            print("=" * 90)
            print(f"TREE {full} entries={len(paths)} truncated={t.get('truncated')}")
            for p in paths[:100]:
                print("   ", p)
    elif mode == "readme":
        for full in sys.argv[2:]:
            rd = m.api(f"repos/{full}/readme", raw=True)
            print("=" * 100)
            print("README:", full, "len=", len(rd) if rd else 0)
            print("=" * 100)
            print((rd or "FAILED")[:14000])
    elif mode == "contents":
        full, path = sys.argv[2], sys.argv[3]
        print((m.api(f"repos/{full}/contents/{path}", raw=True) or "FAILED")[:12000])
