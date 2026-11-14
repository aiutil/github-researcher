#!/usr/bin/env python3
"""Full static decode of the battery-peek loader chain. No execution of any payload."""
import base64, json, re, struct, urllib.request, urllib.error

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch(u, t=40):
    req = urllib.request.Request(u, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=t) as r:
            return r.status, r.read(4_000_000)
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:
        return "ERR:" + str(e)[:60], b""

def png_chunks(data):
    """Yield (type, payload) for PNG chunks."""
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    i = 8
    while i < len(data):
        ln = struct.unpack(">I", data[i:i+4])[0]
        typ = data[i+4:i+8].decode("latin1")
        payload = data[i+8:i+8+ln]
        yield typ, payload
        i += 12 + ln
        if typ == "IEND":
            break

def xor_decrypt(b64, hexkey):
    d = base64.b64decode(b64)
    ky = bytes.fromhex(hexkey)
    out = bytearray(len(d))
    for i in range(len(d)):
        out[i] = d[i] ^ ky[i % len(ky)]
    return bytes(out)

st, png = fetch("https://activation-gateway.cc/i/main.png")
print("== stage2 PNG fetch: status", st, "bytes", len(png))
if st != 200:
    raise SystemExit("cannot fetch png")

meta = None; X = {}; Y = {}
for typ, payload in png_chunks(png):
    if typ != "tEXt":
        continue
    k, _, v = payload.partition(b"\x00")
    k = k.decode("latin1"); v = v.decode("latin1")
    if k == "meta":
        meta = v
    elif re.fullmatch(r"X\d+", k):
        X[k] = v
    elif re.fullmatch(r"Y\d+", k):
        Y[k] = v

print("   tEXt keys:", len(X), "X-chunks,", len(Y), "Y-chunks; meta present:", meta is not None)
if meta is None:
    raise SystemExit("no meta chunk")
m = json.loads(meta)
print("   meta keys:", list(m.keys()), "| n =", m.get("n"), "| m =", m.get("m"), "| fn =", m.get("fn"))

# X chunks -> XOR-encrypted payload data ; Y chunks -> base64 C# source
Xcat = "".join(X[f"X{i:05d}"] for i in range(m["n"]))
Ycat = "".join(Y[f"Y{i:05d}"] for i in range(m["m"]))
print("   X concat b64 len:", len(Xcat), "| Y concat b64 len:", len(Ycat))

try:
    blob = xor_decrypt(Xcat, m["key"])
    print("   XOR-decrypted blob bytes:", len(blob), "| printable head:", blob[:120])
    pe = blob[:2]
    print("   PE signature check:", pe == b"MZ", pe)
except Exception as e:
    print("   XOR decrypt failed:", e)

print("\n== C# source (from Y chunks) ==")
try:
    cs = base64.b64decode(Ycat).decode("utf-8", "replace")
    print(cs[:12000])
except Exception as e:
    print("   decode failed:", e)
