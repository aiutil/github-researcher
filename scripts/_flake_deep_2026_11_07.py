#!/usr/bin/env python3
import json, subprocess, os, statistics, datetime, collections

ENV = {**os.environ, "HOME": "/home/lohasle", "GH_PAGER": "cat"}
def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, env=ENV, timeout=90)
    if r.returncode != 0:
        return None
    return r.stdout

REPO = "Tropicaldrescoop/discord-id-osint-checker"

print("=== COMMIT TIMESTAMP SECOND-OFFSET ANALYSIS ===")
out = gh("api", f"repos/{REPO}/commits?per_page=100")
commits = json.loads(out)
sec = collections.Counter()
pairs = []
for c in commits:
    a = c["commit"]["author"]["date"]
    cm = c["commit"]["committer"]["date"]
    sec[a[17:19]] += 1
    pairs.append((a, cm, c["sha"][:8], c["commit"]["message"].split("\n")[0][:70],
                  c["commit"]["author"]["name"], c["commit"]["author"]["email"][:30]))
print("  author-date SECOND field distribution:", dict(sec))
print(f"  distinct second values: {len(sec)} across {len(commits)} commits")
same = sum(1 for a,cm,_,_,_,_ in pairs if a == cm)
print(f"  author_date == committer_date: {same}/{len(pairs)}")
diff = [(a,cm) for a,cm,_,_,_,_ in pairs if a != cm]
if diff:
    print("  DIFFERS (backdating evidence):")
    for a, cm in diff[:8]:
        print(f"    author={a}  committer={cm}")
print("  --- message pattern groups ---")
msgs = collections.Counter()
for a,cm,sha,m,an,ae in pairs:
    key = m.split(":")[0] if ":" in m else m.split("—")[0].strip()
    msgs[key]+=1
for k,v in msgs.most_common():
    print(f"    {k!r:40s} x{v}")
print("  --- duplicate message texts ---")
mc = collections.Counter(m for a,cm,sha,m,an,ae in pairs)
for k,v in mc.most_common(6):
    print(f"    x{v}  {k!r}")

print("\n=== FULL TREE (recursive) ===")
out = gh("api", f"repos/{REPO}/git/trees/HEAD?recursive=1")
t = json.loads(out)
paths = [x["path"] for x in t.get("tree", [])]
print(f"  total entries={len(paths)} truncated={t.get('truncated')}")
ext = collections.Counter()
for p in paths:
    base = p.rsplit("/",1)[-1]
    if "." in base and not base.startswith("."):
        ext[base.rsplit(".",1)[-1].lower()] += 1
    else:
        ext["(no-ext)"] += 1
print("  extension histogram:", dict(ext.most_common(15)))
print("  --- any application source? ---")
for pat in ["package.json","pyproject.toml","requirements.txt","Cargo.toml","src/","main.py","app.py","*.py","*.js","*.ts","*.rs","*.cs","electron","tauri"]:
    hits = [p for p in paths if pat.strip("*") in p]
    if hits:
        print(f"    {pat}: {len(hits)} -> {hits[:6]}")
print("  --- top-level dirs ---")
print("   ", sorted(set(p.split('/')[0] for p in paths)))
print("  --- all non-asset/non-design files ---")
for p in sorted(paths):
    if not p.startswith(("assets/","design/")):
        print("    ", p)

print("\n=== OWNER ACCOUNT ===")
out = gh("api", "users/Tropicaldrescoop")
if out:
    u = json.loads(out)
    for k in ["login","created_at","updated_at","public_repos","followers","following","bio","name","blog","company","location"]:
        print(f"    {k} = {u.get(k)}")
out = gh("api", "users/Tropicaldrescoop/repos?per_page=100")
if out:
    for r in json.loads(out):
        print(f"    repo: {r['full_name']:50s} created={r['created_at']} stars={r['stargazers_count']} forks={r['forks_count']} size={r['size']} lang={r.get('language')}")

print("\n=== FORK OWNER NAME PATTERN (all 73) ===")
out = gh("api", f"repos/{REPO}/forks?per_page=100")
forks = json.loads(out) if out else []
names = [f["owner"]["login"] for f in forks]
hyphenated = [n for n in names if "-" in n]
print(f"  total={len(names)}  with-hyphen-suffix={len(hyphenated)}")
print("  samples:", names[:20])
# check for numeric-random suffix pattern
import re
pat = re.compile(r".*[a-z]?\d{2,}[a-z0-9]*-[a-z]+$")
print(f"  match 'name<digits>-<word>': {sum(1 for n in names if pat.match(n))}/{len(names)}")
