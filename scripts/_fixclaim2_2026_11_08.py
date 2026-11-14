#!/usr/bin/env python3
'''Regex-based correction of the AFK-Bot import claim.'''

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAT = re.compile(
    r"而它的 `main\.py`（164 B）写的是 `from utils import build`"
    r"（单数）而仓库里的文件叫 `utils\.py`（复数）"
    r"—— 这是一个会直接抛 `ModuleNotFoundError` 的 import\*\*，"
    r"与 11-06 的 `PulverizeLink/roblox-performance-tool`"
    r"（`from utils import build` 而 `utils\.py` 根本不存在、API 返回 404）"
    r"属于同一类构造错误，⭐+ \*\*即：本仓库的代码在当前状态下无法运行\*\*"
)

REPL = (
    "而它的 `main.py`（164 B）写的是 `from utils import build`"
    "—— 该 import 在本仓库里能解析（`utils.py` 存在且确实定义了 `build`），"
    "但运行结果是 `Project: [0, 2, 4, ..., 18]` 即模板占位数据**；"
    "⭐⭐⭐⭐ **这与 11-06 的 `PulverizeLink/roblox-performance-tool` "
    "属于同一类构造错误的两个级别 —— 那一个的 `utils.py` 根本不存在（API 返回 404），"
    "代码连 import 都无法解析**；⭐⭐⭐⭐ **即：本仓库的代码能跑，但跑出来的不是 AFK 机器人**"
)

for rel in ["daily/2026-11-08.md", "projects/minecraft-afk-bot.md"]:
    p = ROOT / rel
    c = p.read_text(encoding="utf-8")
    new, n = PAT.subn(REPL, c)
    if n:
        p.write_text(new, encoding="utf-8")
    print(f"{rel}: {n} replacement(s)")

# Verify no stale claims remain
for rel in ["daily/2026-11-08.md", "projects/minecraft-afk-bot.md"]:
    c = (ROOT / rel).read_text(encoding="utf-8")
    for probe in ["ModuleNotFoundError", "无法运行", "无法解析的同类重演"]:
        if probe in c:
            i = c.find(probe)
            print(f"  !! {rel} still contains {probe!r}: ...{c[max(0,i-160):i+120]}...")
