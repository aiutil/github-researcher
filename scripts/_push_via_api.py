#!/usr/bin/env python3
"""Push a commit to origin via the GitHub Git Data API.

Used when github.com (git smart HTTP) TLS is unreachable but api.github.com works.
Builds blobs -> tree -> commit -> updates refs/heads/main.
Only files that differ from HEAD are uploaded; the rest come from the base tree.
"""
import base64, json, os, subprocess, sys

REPO = "aiutil/github-researcher"
BRANCH = "main"
ENV = {**os.environ, "HOME": "/home/lohasle"}


def gh(args, stdin=None):
    r = subprocess.run(["gh", "api"] + args, capture_output=True, text=True,
                       env=ENV, input=stdin)
    if r.returncode != 0:
        raise SystemExit(f"gh api failed: {args[:3]}\n{r.stderr[:2000]}")
    return r.stdout


def gh_json(args):
    return json.loads(gh(args))


def changed_files():
    """Paths that differ from HEAD (staged, unstaged, or untracked)."""
    tracked = subprocess.run(["git", "diff", "--name-only", "HEAD"],
                             capture_output=True, text=True, env=ENV).stdout.split()
    untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"],
                               capture_output=True, text=True, env=ENV).stdout.split()
    seen, out = set(), []
    for p in tracked + untracked:
        if p and p not in seen and not p.startswith("scripts/__pycache__"):
            seen.add(p)
            out.append(p)
    return out


def main():
    base_commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                 text=True, env=ENV).stdout.strip()
    base_tree = subprocess.run(["git", "rev-parse", "HEAD^{tree}"], capture_output=True,
                               text=True, env=ENV).stdout.strip()
    remote = gh_json([f"repos/{REPO}/git/ref/heads/{BRANCH}"])["object"]["sha"]
    if remote != base_commit:
        raise SystemExit(f"remote {remote} != local HEAD {base_commit}; refusing to push")

    files = changed_files()
    print(f"base_commit={base_commit}")
    print(f"base_tree={base_tree}")
    print(f"changed files: {len(files)}")

    entries = []
    for path in files:
        if not os.path.isfile(path):
            continue
        data = open(path, "rb").read()
        is_text = True
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            is_text = False
            text = None
        if is_text:
            blob = gh_json(["--method", "POST", f"repos/{REPO}/git/blobs",
                            "-f", f"content={text}", "-f", "encoding=utf-8"])
        else:
            blob = gh_json(["--method", "POST", f"repos/{REPO}/git/blobs",
                            "-f", f"content={base64.b64encode(data).decode()}",
                            "-f", "encoding=base64"])
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
        print(f"  blob {blob['sha'][:8]}  {path}")

    tree = gh_json(["--method", "POST", f"repos/{REPO}/git/trees",
                    "-f", f"base_tree={base_tree}", "-f", f"tree={json.dumps(entries)}"])
    print(f"new tree {tree['sha']}")

    msg = sys.argv[1] if len(sys.argv) > 1 else "daily: automated commit"
    commit = gh_json(["--method", "POST", f"repos/{REPO}/git/commits",
                      "-f", f"message={msg}", "-f", f"tree={tree['sha']}",
                      "-f", f"parents[]={base_commit}"])
    print(f"new commit {commit['sha']}")

    ref = gh_json(["--method", "PATCH", f"repos/{REPO}/git/refs/heads/{BRANCH}",
                   "-f", f"sha={commit['sha']}", "-f", "force=false"])
    print(f"ref updated -> {ref['object']['sha']}")
    print(f"PUSH_OK {commit['sha']}")


if __name__ == "__main__":
    main()
