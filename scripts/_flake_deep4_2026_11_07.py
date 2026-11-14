#!/usr/bin/env python3
import json, subprocess, os, collections, base64

ENV = {**os.environ, "HOME": "/home/lohasle", "GH_PAGER": "cat"}
def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, env=ENV, timeout=90)
    return r.stdout if r.returncode == 0 else None

def content(repo, path):
    out = gh("api", f"repos/{repo}/contents/{path}")
    if not out: return None
    try:
        d = json.loads(out)
        return base64.b64decode(d["content"]).decode("utf-8", "replace")
    except Exception:
        return None

print("=== SECOND-VALUE DIVERSITY ACROSS CANDIDATES (commit authenticity cross-check) ===")
for repo in ["voyager-so/vork", "JosssphZhou/poki", "majorminorlabs/hermes-voice",
             "devvmhq/devvm", "JenkinWoo/sheeridVerify",
             "HerdBuilderEstimate/roblox-studio-mcp",
             "Tropicaldrescoop/discord-id-osint-checker"]:
    out = gh("api", f"repos/{repo}/commits?per_page=100")
    if not out:
        print(f"  {repo:45s} (fetch failed)"); continue
    cs = json.loads(out)
    if not cs:
        print(f"  {repo:45s} (0 commits)"); continue
    secs = collections.Counter(c["commit"]["author"]["date"][17:19] for c in cs)
    same = sum(1 for c in cs if c["commit"]["author"]["date"] == c["commit"]["committer"]["date"])
    dates = sorted(c["commit"]["author"]["date"] for c in cs)
    print(f"  {repo:45s} n={len(cs):4d} distinct_secs={len(secs):3d} "
          f"author==committer:{same}/{len(cs)} "
          f"range={dates[0][:10]}..{dates[-1][:10]} "
          f"top_secs={secs.most_common(3)}")

print("\n=== FLAKE: CHANGELOG.md ===")
print((content("Tropicaldrescoop/discord-id-osint-checker", "CHANGELOG.md") or "(none)")[:2000])
print("\n=== FLAKE: CREDITS.md ===")
print((content("Tropicaldrescoop/discord-id-osint-checker", "CREDITS.md") or "(none)")[:1500])
print("\n=== FLAKE: design/README.md ===")
print((content("Tropicaldrescoop/discord-id-osint-checker", "design/README.md") or "(none)")[:1500])
print("\n=== FLAKE: .github/settings.yml ===")
print(content("Tropicaldrescoop/discord-id-osint-checker", ".github/settings.yml") or "(none)")
print("\n=== FLAKE: CONTRIBUTING.md (head) ===")
print((content("Tropicaldrescoop/discord-id-osint-checker", "CONTRIBUTING.md") or "(none)")[:1200])
