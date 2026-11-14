#!/usr/bin/env python3
import json, subprocess, os, collections, statistics, datetime, re

ENV = {**os.environ, "HOME": "/home/lohasle", "GH_PAGER": "cat"}
def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, env=ENV, timeout=90)
    return r.stdout if r.returncode == 0 else None

REPO = "Tropicaldrescoop/discord-id-osint-checker"

print("=== COMMIT AUTHORS (name/email) ===")
out = gh("api", f"repos/{REPO}/commits?per_page=100")
commits = json.loads(out)
au = collections.Counter((c["commit"]["author"]["name"], c["commit"]["author"]["email"]) for c in commits)
for (n,e),v in au.most_common():
    print(f"    {v:3d}  name={n!r} email={e!r}")
# committer too
cu = collections.Counter((c["commit"]["committer"]["name"], c["commit"]["committer"]["email"]) for c in commits)
print("  committers:", dict(cu))

print("\n=== SECOND-OFFSET: minute field too ===")
mins = collections.Counter(c["commit"]["author"]["date"][14:16] for c in commits)
print("  distinct minutes:", len(mins), dict(list(mins.items())[:20]))

print("\n=== FORK OWNER PROVENANCE (all 73) ===")
out = gh("api", f"repos/{REPO}/forks?per_page=100")
forks = json.loads(out) if out else []
created = []
for f in forks:
    o = f["owner"]["login"]
    u = gh("api", f"users/{o}")
    if u:
        d = json.loads(u)
        created.append((d.get("created_at"), o, d.get("public_repos"), d.get("followers")))
    else:
        created.append((None, o, None, None))
created = [c for c in created if c[0]]
created.sort()
ok = created
print(f"  resolved={len(ok)}/{len(forks)}")
if ok:
    yrs = collections.Counter(c[0][:4] for c in ok)
    print("  account creation year histogram:", dict(sorted(yrs.items())))
    ds = sorted(datetime.datetime.strptime(c[0], "%Y-%m-%dT%H:%M:%SZ") for c in ok)
    print(f"  oldest={ds[0].date()}  newest={ds[-1].date()}")
    after_repo = sum(1 for d in ds if d > datetime.datetime(2026,11,6,8,59,5))
    print(f"  created AFTER repo creation (2026-11-06T08:59:05Z): {after_repo}/{len(ds)}")
    print(f"  public_repos: median={statistics.median([c[2] for c in ok if c[2] is not None]):.0f} max={max(c[2] for c in ok if c[2] is not None)}")
    print(f"  followers: total={sum(c[3] for c in ok if c[3] is not None)} max={max(c[3] for c in ok if c[3] is not None)}")
    print(f"  accounts with 0 followers: {sum(1 for c in ok if c[3]==0)}/{len(ok)}")
    # name pattern
    names = [c[1] for c in ok]
    pat = re.compile(r"^[A-Za-z][A-Za-z0-9]*\d+[a-z0-9]*(-[a-z0-9]+)+$")
    print(f"  names matching 'base<digits>-<word>': {sum(1 for n in names if pat.match(n))}/{len(names)}")

print("\n=== FORK BATCHING: forks per 10-minute bucket ===")
times = sorted(datetime.datetime.strptime(f["created_at"], "%Y-%m-%dT%H:%M:%SZ") for f in forks)
buckets = collections.Counter(t.replace(minute=(t.minute//10)*10, second=0) for t in times)
for b, v in sorted(buckets.items()):
    print(f"    {b.strftime('%H:%M')} -> {v}")
