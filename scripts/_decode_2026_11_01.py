#!/usr/bin/env python3
"""Static decode of the battery-peek install payload. No execution."""
import base64, re, subprocess, urllib.request, urllib.error

def fetch(u, t=30):
    req = urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=t) as r: return r.status, r.read(500000)
    except urllib.error.HTTPError as e: return e.code, e.read(200000)
    except Exception as e: return "ERR", str(e).encode()

s, b = fetch("https://activation-gateway.cc/update/ps-activator")
print("== battery-peek loader: status", s, "bytes", len(b))
txt = b.decode("utf-8", "replace")
m = re.search(r"FromBase64String\('([^']+)'\)", txt)
if m:
    dec = base64.b64decode(m.group(1)).decode("utf-8", "replace")
    print("\n== DECODED STAGE-2 (static) ==\n")
    print(dec)
    print("\n== embedded stage-3 URLs (base64-decoded) ==")
    for mm in re.finditer(r"\$([A-Za-z]+)=@\('([^']+)'\)|\[Convert\]::FromBase64String\('([^']+)'\)", dec):
        pass
    for mm in re.finditer(r"'([A-Za-z0-9+/=]{16,})'", dec):
        try:
            d = base64.b64decode(mm.group(1)).decode("utf-8", "replace")
            if "http" in d: print("   ", d[:120])
        except Exception: pass
    for mm in re.finditer(r"'(https?://[^']+)'", dec):
        print("    PLAIN:", mm.group(1))

print("\n== git-software.cc/ps/Setup.ps1 (10-30 farm) ==")
s2, b2 = fetch("https://git-software.cc/ps/Setup.ps1")
print("status", s2, "bytes", len(b2))
t2 = b2.decode("utf-8", "replace")
print(t2[:3000])
