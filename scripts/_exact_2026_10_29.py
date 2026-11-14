#!/usr/bin/env python3
"""精确 commit 总数（Link 头 rel=last）+ 农场簇指纹核验。"""
import subprocess, json, sys, re

def api(args, headers=False):
    cmd = ["gh", "api", "-i"] if headers else ["gh", "api"]
    r = subprocess.run(cmd + args, capture_output=True, text=True)
    return r.stdout if headers else r.stdout

def exact_commits(full):
    out = api([f"repos/{full}/commits?per_page=1"], headers=True)
    m = re.search(r'<https://api\.github\.com/[^>]*[?&]page=(\d+)>;\s*rel="last"', out)
    if m:
        return int(m.group(1))
    # no link header -> single page
    body = out.split("\r\n\r\n", 1)[-1]
    try:
        return len(json.loads(body))
    except Exception:
        return None

def blob_sha(full, path):
    r = subprocess.run(["gh", "api", f"repos/{full}/contents/{path}"],
                       capture_output=True, text=True)
    try:
        return json.loads(r.stdout).get("sha")
    except Exception:
        return None

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "commits":
        for full in sys.argv[2:]:
            print(f"{full}\t{exact_commits(full)}")
    elif mode == "blob":
        full, path = sys.argv[2], sys.argv[3]
        print(f"{full}\t{path}\t{blob_sha(full, path)}")
