#!/usr/bin/env python3
"""Push an already-created local commit to origin via the GitHub Git Data API.

Used when github.com (git smart HTTP) TLS is unreachable but api.github.com
works.  This variant does NOT rebuild blobs: it uploads the tree of the local
HEAD commit by recreating only the blobs that differ from the parent tree, then
creates a commit with the SAME message and updates the branch ref.

Blob payloads are sent as JSON on stdin (--input -) so that large files do not
overflow the argument list.

Safety: refuses to run unless remote HEAD == local HEAD^.
"""
import base64
import json
import os
import subprocess
import sys

REPO = "aiutil/github-researcher"
BRANCH = "main"
ROOT = "/home/lohasle/aiutil-github-researcher"
ENV = {**os.environ, "HOME": "/home/lohasle"}


def gh(args, stdin=None):
    r = subprocess.run(["gh", "api"] + args, capture_output=True, text=True,
                       env=ENV, input=stdin)
    if r.returncode != 0:
        raise SystemExit(f"gh api failed: {args[:4]}\n{r.stderr[:2000]}")
    return r.stdout


def gh_json(args, stdin=None):
    return json.loads(gh(args, stdin=stdin))


def git(*args):
    return subprocess.run(["git"] + list(args), capture_output=True, text=True,
                          env=ENV, cwd=ROOT).stdout.strip()


def post_blob(data: bytes) -> str:
    try:
        text = data.decode("utf-8")
        payload = json.dumps({"content": text, "encoding": "utf-8"})
    except UnicodeDecodeError:
        payload = json.dumps({"content": base64.b64encode(data).decode(),
                              "encoding": "base64"})
    out = gh_json(["--method", "POST", f"repos/{REPO}/git/blobs", "--input", "-"],
                  stdin=payload)
    return out["sha"]


def main():
    head = git("rev-parse", "HEAD")
    parent = git("rev-parse", "HEAD^")
    tree_sha = git("rev-parse", "HEAD^{tree}")
    msg = git("log", "-1", "--pretty=%B").strip()

    remote = gh_json([f"repos/{REPO}/git/ref/heads/{BRANCH}"])["object"]["sha"]
    if remote != parent:
        raise SystemExit(f"remote {remote} != local HEAD^ {parent}; refusing to push")

    diff = git("diff", "--name-only", "HEAD^", "HEAD").split()
    print(f"base_commit(parent)={parent}")
    print(f"new_commit={head}")
    print(f"new_tree(local)={tree_sha}")
    print(f"changed files: {len(diff)}", flush=True)

    entries = []
    for i, path in enumerate(diff, 1):
        full = os.path.join(ROOT, path)
        if not os.path.isfile(full):
            continue
        sha = post_blob(open(full, "rb").read())
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": sha})
        if i % 25 == 0 or i == len(diff):
            print(f"  [{i}/{len(diff)}] blob {sha[:8]}  {path}", flush=True)

    parent_tree = git("rev-parse", "HEAD^^{tree}")
    payload = json.dumps({"base_tree": parent_tree, "tree": entries})
    tree = gh_json(["--method", "POST", f"repos/{REPO}/git/trees", "--input", "-"],
                   stdin=payload)
    print(f"remote tree {tree['sha']}  (local {tree_sha})")

    if tree["sha"] != tree_sha:
        raise SystemExit(f"tree mismatch: remote {tree['sha']} != local {tree_sha}")

    payload = json.dumps({"message": msg, "tree": tree["sha"], "parents": [parent]})
    commit = gh_json(["--method", "POST", f"repos/{REPO}/git/commits", "--input", "-"],
                     stdin=payload)
    print(f"created commit {commit['sha']}")

    payload = json.dumps({"sha": commit["sha"], "force": False})
    ref = gh_json(["--method", "PATCH", f"repos/{REPO}/git/refs/heads/{BRANCH}",
                   "--input", "-"], stdin=payload)
    print(f"ref updated -> {ref['object']['sha']}")
    print(f"PUSH_OK {commit['sha']}")


if __name__ == "__main__":
    main()
