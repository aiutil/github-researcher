#!/usr/bin/env python3
import json, subprocess, os, collections, datetime

ENV = {**os.environ, "HOME": "/home/lohasle", "GH_PAGER": "cat"}
def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, env=ENV, timeout=90)
    return r.stdout if r.returncode == 0 else None

REPO = "Tropicaldrescoop/discord-id-osint-checker"

def content(path):
    out = gh("api", f"repos/{REPO}/contents/{path}")
    if not out: return None
    import base64
    try:
        d = json.loads(out)
        return base64.b64decode(d["content"]).decode("utf-8", "replace")
    except Exception:
        return None

print("=== .github/workflows/build.yml ===")
c = content(".github/workflows/build.yml")
print(c if c else "(none)")

print("\n=== design/ file list with sizes ===")
out = gh("api", f"repos/{REPO}/contents/design")
if out:
    for f in sorted(json.loads(out), key=lambda x: x["name"]):
        print(f"    {f['name']:24s} {f['size']:7d} B  type={f['type']}")

print("\n=== design/src/hero.html (first 40 lines) ===")
c = content("design/src/hero.html")
print("\n".join(c.split("\n")[:40]) if c else "(none)")

print("\n=== design/package.json ===")
print(content("design/package.json") or "(none)")

print("\n=== RELEASE ===")
out = gh("api", f"repos/{REPO}/releases")
if out:
    for r in json.loads(out):
        print(f"    tag={r['tag_name']} name={r['name']} published={r['published_at']} prerelease={r['prerelease']}")
        for a in r.get("assets", []):
            print(f"      asset: {a['name']} {a['size']} B  downloads={a['download_count']}")
        print("      body:", (r.get("body") or "")[:600])

print("\n=== COMMIT DATE INTERVAL ANALYSIS (sorted) ===")
out = gh("api", f"repos/{REPO}/commits?per_page=100")
commits = json.loads(out)
ts = sorted(datetime.datetime.strptime(c["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ") for c in commits)
gaps = [(ts[i+1]-ts[i]).total_seconds()/86400 for i in range(len(ts)-1)]
gs = sorted(gaps)
print(f"  n={len(ts)} span_days={(ts[-1]-ts[0]).days}")
print(f"  day-gap: median={sorted(gaps)[len(gaps)//2]:.2f}d  min={min(gaps):.3f}d max={max(gaps):.2f}d")
# check for regular spacing
import statistics
print(f"  mean={statistics.mean(gaps):.3f}d stdev={statistics.pstdev(gaps):.3f}d  cv={statistics.pstdev(gaps)/statistics.mean(gaps):.3f}")
print("  --- consecutive gaps (days) ---")
for i,g in enumerate(gaps):
    print(f"    {ts[i].date()} -> {ts[i+1].date()}  {g:.3f}d")

print("\n=== AUTHORS ===")
au = collections.Counter(c["commit"]["author"]["name"] for c in commits)
print("  ", dict(au))
ae = collections.Counter(c["commit"]["author"]["email"] for c in commits)
print("  emails:", dict(list(ae.items())[:5]))

print("\n=== CHANGELOG.md ===")
c = content("CHANGELOG.md")
print(c[:2500] if c else "(none)")
