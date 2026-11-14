#!/usr/bin/env python3
"""Batch evidence for 2026-11-03 key projects. Read-only GitHub API."""
import importlib.util, json, sys

spec = importlib.util.spec_from_file_location("c", "scripts/_collect_2026_11_03.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

FULLS = ["Gezine/CivSwitch", "SAOS-3624/dsh-see-now", "caru-ini/stack-diagram",
         "justrach/nanolight", "interplains/Zero-Breach-Toolkit",
         "valentderah/totk-pc-recomp", "kuraeow/ultratears",
         "haydenschmitty/floorplan", "NyxFoundation/nyxis", "interplains/zero-breach"]

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "releases":
        for f in FULLS:
            rel = m.japi(f"repos/{f}/releases?per_page=30")
            print("=" * 90)
            print("RELEASES:", f, "count=", len(rel or []))
            for r in (rel or [])[:12]:
                body = (r.get("body") or "")[:320].replace("\r", "").replace("\n", " ")
                print(f"  {r['tag_name']:<16} {r['published_at'][:19]} assets={len(r.get('assets', []))} "
                      f"dl={sum(a['download_count'] for a in r.get('assets', []))}")
                if body.strip():
                    print(f"      {body}")
    elif mode == "issues":
        for f in FULLS:
            iss = m.japi(f"repos/{f}/issues?state=all&per_page=30")
            print("=" * 90)
            print("ISSUES:", f, "count=", len(iss) if isinstance(iss, list) else "FAIL")
            if not isinstance(iss, list):
                continue
            for i in iss:
                tag = "PR " if "pull_request" in i else "ISS "
                print(f"  {tag}#{i['number']:<4} {i['state']:<6} {i['title'][:88]} "
                      f"[{i['user']['login']}] {i['created_at'][:10]}")
    elif mode == "tree":
        for f in FULLS:
            t = m.japi(f"repos/{f}/git/trees/HEAD?recursive=1") or {}
            paths = [e["path"] for e in t.get("tree", [])]
            print("=" * 90)
            print(f"TREE {f}  entries={len(paths)} truncated={t.get('truncated')}")
            for p in paths[:120]:
                print("   ", p)
    elif mode == "contents":
        f, path = sys.argv[2], sys.argv[3]
        print((m.api(f"repos/{f}/contents/{path}", raw=True) or "FAILED")[:12000])
