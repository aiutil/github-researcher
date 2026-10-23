#!/usr/bin/env python3
"""Update tracked project profiles with fresh stars / last_seen / url facts.

Only touches frontmatter fields plus appends a dated "最近动态" entry.
Usage: python3 scripts/_update_tracked.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# slug -> {stars, stars_delta, last_seen_date, title?, url?, note}
UPDATES = {
    "unixnu": {
        "stars": "856 stars",
        "stars_delta": "4.6 天 856⭐ ⑂148（fork/star 17.3%）",
        "last_seen_date": "2026-10-24",
        "note": (
            "**2026-10-24：** ⭐ 750 → **856**（+106），⑂ 118 → **148**（fork/star 15.7% → **17.3%**），"
            "subs 3 → **4**，oi 6 不变，`pushed_at` 2026-10-23T15:29:35Z。"
            "`license.spdx_id` 仍为 `NOASSERTION`（LICENSE 首行仍写 `SPDX-License-Identifier: BSD-2-Clause-Patent`），"
            "**这是 10-23 记录的两处元数据不一致之一，一周内未修复**。"
            "本日新增第三个同领域项目 oosexgang/hackios-xnu-kernel（1,064⭐），**而它选择了与 UniXNU 相反的技术路线"
            "（直接编译 Apple 开源 XNU 并打补丁）**——见 [2026-10-24 日报](../daily/2026-10-24.md)。"
            "**跟踪方式仍是「设备覆盖表」而非 star 数**：观察 `docs/devices/` 是否从 35 增长到 40+。"
        ),
    },
    "snapintosh": {
        "stars": "745 stars",
        "stars_delta": "2.4 天 745⭐ ⑂43（fork/star 5.8%）",
        "last_seen_date": "2026-10-24",
        "title": "Macintosh/Snapintosh",
        "url": "https://github.com/Macintosh/Snapintosh",
        "note": (
            "**2026-10-24：** ⚠️ **仓库已改组——`Acelogic/Snapintosh` → `Macintosh/Snapintosh`**"
            "（新组织 `Snapintosh` 创建于 2026-10-23T05:28:04Z）。"
            "⭐ 530 → **745**（+215），⑂ 29 → **43**（fork/star 5.5% → **5.8%**），subs 4 → **7**，oi 4 不变。"
            "⚠️ **`license.spdx_id` 仍为 `NOASSERTION`**（LICENSE 首行仍写 `MIT License`），"
            "**而 `LICENSE` 文件本身确认仍在**（`Copyright (c) 2026 The Snapintosh contributors`）。"
            "**⭐ 结构性变化：主仓库已拆分为 8 个仓库**——`Macintosh/Snapintosh`（745⭐）、"
            "`Macintosh/q1n1`（35⭐，2026-09-16 创建，从 Asahi Linux m1n1 fork 的 UEFI EL2 proxy）、"
            "`Macintosh/air2ir3`（AIR→Mesa ir3 shader 编译器，2026-10-23 新建，0⭐）、"
            "`Macintosh/SnapAdreno`（Adreno X2-90 IOGPU 与显示驱动，0⭐）、"
            "`Macintosh/SnapI2CHID`（I2C-HID 键盘/触控板/精密触控板驱动，0⭐）、"
            "`Macintosh/SnapMetal`（AdrenoMetal.bundle，0⭐）、"
            "`Macintosh/SnapQCC2072`（QCC2072 Wi-Fi 驱动，work in progress，0⭐）、"
            "`Macintosh/.github`（组织档案）。"
            "**这与 UniXNU 的 16 个驱动 submodule 属同一种「驱动独立仓库」的责任边界划分，但本日才显现。**"
            "**新的跟踪方式：主仓库 star 数已不是好指标（拆到 8 个仓库里），应改为跟踪 7 个子仓库中"
            "哪一个先获得外部 star**——这是「从单仓库走向多仓库平台」的第一个可观测信号。"
            "另注：10-23 记录的 Status 表中「60 Hz 目标」与「Wi-Fi 从 macOS 菜单发起连接尚不可用」"
            "**本窗口未重新核验**（README 未重取）。"
        ),
    },
    "deepinfer": {
        "stars": "21,056 stars",
        "stars_delta": "8.5 天 21,056⭐ ⑂2,322（fork/star 11.0%）",
        "last_seen_date": "2026-10-24",
        "note": (
            "**2026-10-24：** ⭐ 19,806 → **21,056**（+1,250），⑂ 2,106 → **2,322**（fork/star 10.6% → **11.0%**），"
            "**subs 43 → 50（本项目订阅数持续上升，仍为本批最高）**，oi 193 → **200**。"
            "⚠️ **`pushed_at` 为 2026-10-21T04:55:44Z——距本快照（2026-10-23T22:13Z）已约 2.7 天，即最近三天窗口内无新 push**。"
            "**这是本日最值得注意的一条延续跟踪观察：一个 21k⭐ 的项目连续三天无提交，"
            "说明热度与开发活动在本项目上已经脱钩**——star 仍在涨，但代码未动。"
            "**三项缺失（KV cache 系统 / VE-Prefill-Decode 分离 / prefill 与 decode 两侧的跨 DP 副本负载均衡）"
            "本窗口未重新核验是否已开源——这仍是本项目未来的分水岭。**"
            "另：oi 200 对 21k⭐ 属正常早期信号，需观察关闭率。"
        ),
    },
    "reylo": {
        "stars": "1,028 stars",
        "stars_delta": "3.9 天 1,028⭐ ⑂8（fork/star 0.8%）",
        "last_seen_date": "2026-10-24",
        "note": (
            "**2026-10-24：** ⭐ 616 → **1,028**（+412，约 +67%），⑂ 3 → **8**（fork/star 0.5% → **0.8%**，仍为本批最低区间），"
            "**subs 0 → 2**（首次出现深度关注者），oi 13 → **12**。"
            "**`pushed_at` 更新至 2026-10-23T22:12:38Z（10-23 当日仍在提交）**，"
            "**且仓库体积从 66,704 KB 增至 78,474 KB**——说明项目在持续开发而非停滞。"
            "**⭐ 关键观察：10-23 记录的「单一决定性风险」——完全依赖 TypeScript 7.1 beta 的 content mappers——"
            "本窗口未核验 TS 7.1 是否已进入 stable**（本日报未取 microsoft/typescript-go 的最新状态）。"
            "**subs 从 0 到 2 是本项目首次出现采用信号**，比 star 数更能说明问题："
            "前 1.9 天 616⭐ 而 subs 0（纯曝光），现在 1,028⭐ 且 subs 2，"
            "**fork-star 仍仅 0.8%——再次印证本日报连续四天观察到的分界线："
            "「需要等上游 beta 特性而非 fork 它」的项目，fork 比例天然低。**"
            "**观察重点不变：TypeScript 7.1 是否进入 stable、content mapper API 是否变更。**"
        ),
    },
}


def update_frontmatter(text: str, changes: dict) -> str:
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise SystemExit("no frontmatter")
    fm = parts[1]
    for key, value in changes.items():
        if key in ("note",):
            continue
        pattern = re.compile(rf"^({re.escape(key)}:\s*).*$", re.M)
        if pattern.search(fm):
            fm = pattern.sub(lambda m: m.group(1) + f'"{value}"', fm, count=1)
        else:
            fm = fm.rstrip("\n") + f'\n{key}: "{value}"\n'
    return "---" + fm + "---" + parts[2]


def append_dynamic(text: str, note: str, date: str) -> str:
    """Append a dated 最近动态 block before the trailing source line."""
    # A bold run must never end adjacent to another bold run: "**a****b" renders
    # as literal asterisks.  Separate the two runs with a single space.
    note = note.replace("****", "** **")
    block = f"\n## 最近动态（{date}）\n\n{note}\n"
    marker = "\n---\n> 数据来源:"
    if marker in text:
        head, _, tail = text.partition(marker)
        return head + block + marker + tail
    return text + block


for slug, changes in UPDATES.items():
    path = ROOT / "projects" / f"{slug}.md"
    if not path.exists():
        print(f"SKIP {slug}: not found")
        continue
    text = path.read_text(encoding="utf-8")
    note = changes["note"]
    date = changes["last_seen_date"]
    new_text = update_frontmatter(text, changes)
    new_text = append_dynamic(new_text, note, date)
    path.write_text(new_text, encoding="utf-8")
    print(f"updated {path.name} ({len(text)} -> {len(new_text)} bytes)")
