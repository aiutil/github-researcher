#!/usr/bin/env python3
'''Correct the AFK-Bot import claim in daily/2026-11-08.md and the matching
one-liner in the project frontmatter.'''

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_TAIL = (
    "⭐⭐⭐⭐ **它的 `utils.py`（101 B）是 11-06 那条「代码连 import 都无法解析」的同类重演**："
    "`\"\"\"Utility helpers for engine.\"\"\"` + `def build(limit): return [item * 2 for item in range(limit)]` "
    "—— **一个与 Minecraft 毫无关系的列表推导**；"
    "⭐⭐⭐⭐⭐ **而它的 `main.py`（164 B）写的是 `from utils import build`（单数）而仓库里的文件叫 `utils.py`（复数）"
    "—— 这是一个会直接抛 `ModuleNotFoundError` 的 import**，"
    "与 11-06 的 `PulverizeLink/roblox-performance-tool`（`from utils import build` 而 `utils.py` 根本不存在、API 返回 404）"
    "属于同一类构造错误，⭐⭐⭐⭐ **即：本仓库的代码在当前状态下无法运行**"
)

NEW_TAIL = (
    "⭐⭐⭐⭐ **它的 `utils.py`（101 B）是 11-06 那条「占位符代码」的同类重演**："
    "`\"\"\"Utility helpers for engine.\"\"\"` + `def build(limit): return [item * 2 for item in range(limit)]` "
    "—— **一个与 Minecraft 毫无关系的列表推导**；"
    "⭐⭐⭐⭐ **而它的 `main.py`（164 B）写的是 `from utils import build` —— 这个 import 在本仓库里恰好能解析"
    "（`utils.py` 存在且确实定义了 `build`），但运行结果是 `Project: [0, 2, 4, ..., 18]` 即模板占位数据**；"
    "⭐⭐⭐⭐ **这与 11-06 的 `PulverizeLink/roblox-performance-tool` 属于同一类构造错误的两个级别 "
    "—— 那一个的 `utils.py` 根本不存在（API 返回 404），代码连 import 都无法解析**；"
    "⭐⭐⭐⭐ **即：本仓库的代码能跑，但跑出来的不是 AFK 机器人**"
)

p = ROOT / "daily" / "2026-11-08.md"
c = p.read_text(encoding="utf-8")
if OLD_TAIL in c:
    c = c.replace(OLD_TAIL, NEW_TAIL)
    p.write_text(c, encoding="utf-8")
    print("daily/2026-11-08.md: import claim corrected")
else:
    print("daily/2026-11-08.md: OLD_TAIL not found -- checking partial")
    i = c.find("代码连 import 都无法解析")
    print("  context:", repr(c[i - 200:i + 400]) if i >= 0 else "n/a")

# Project frontmatter one-liner
q = ROOT / "projects" / "minecraft-afk-bot.md"
t = q.read_text(encoding="utf-8")
old_fl = "⭐⭐⭐⭐⭐ **而它的 `main.py`（164 B）写的是 `from utils import build` 而仓库里的文件叫 `utils.py`（复数）"
if old_fl in t:
    t = t.replace(
        old_fl,
        "⭐⭐⭐⭐⭐ **而它的 `main.py`（164 B）写的是 `from utils import build` —— 该 import 在本仓库里能解析，"
        "但运行结果是模板占位数据",
    )
    q.write_text(t, encoding="utf-8")
    print("projects/minecraft-afk-bot.md: frontmatter corrected")
else:
    print("projects/minecraft-afk-bot.md: frontmatter pattern not found (may already be ok)")
