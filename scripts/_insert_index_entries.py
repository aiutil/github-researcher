#!/usr/bin/env python3
"""Insert the missing 2026-11-09..2026-11-12 trend-index entries.

The trend index currently jumps straight from 2026-11-13 to 2026-11-08, so the
four dated sections have to be inserted before the `## 2026-11-08` heading.
The daily-report.md needs the same four sections.
"""
from pathlib import Path

ROOT = Path("/home/lohasle/aiutil-github-researcher")

TREND = {
    "2026-11-12": """## 2026-11-12

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---|
| `Kianuni/Erosion-CN` | 986 | 227 | 23.0% | 1 | Swift | 15 | 工具型 |
| `ValidatorStack/solana-vigil` | 157 | 26 | 16.6% | **10** | Go | **1** | 工具型 |
| `egoist/tinytraffic` | 107 | 3 | 2.8% | 0 | TypeScript | 25 | 工具型 |
| `bea4dev/shoji-bar-4` | 98 | 4 | 4.1% | 0 | Rust | 41 | 工具型 |
| `JDhruv14/line-art-animation` | 149 | 11 | 7.4% | 1 | TypeScript | 1 | 工具型 |
| `failsafe-security/artex` | 126 | 2 | 1.6% | 0 | Go | 3 | 工具型 |

### ⭐⭐⭐⭐⭐ 本日两个真项目从两个方向回答了同一个问题：「不可逆」如何被设计

- **`ValidatorStack/solana-vigil`（157⭐ ⑂26 · subs 10 · 1 commit · 59 blobs · Go · MIT）** —— 只读的 Solana 验证人运维工具。⭐⭐⭐⭐⭐ **⭐⭐ 核心是「观测失败 → `unknown`，绝不伪造健康值」（README 原文：Missing RPC fields and failed observations become `unknown`, never a fabricated healthy value）**；⭐⭐⭐⭐⭐ ⭐⭐ 以及「No alert storms」下面的六个维度（持续失败阈值 / 稳定恢复 / 去重 / 严重性升级 / 投递失败重试 / 重复间隔）。
- **`Kianuni/Erosion-CN`（986⭐ ⑂227 · subs 1 · 15 commits · 99 blobs · Swift · GPL-3.0）** —— iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（中文、面向「防白苹果」加固），基于 `forcequitOS/worse_query`。⭐⭐⭐⭐⭐ **⭐⭐ 核心是**写入前自动备份原值 + 一键回滚** —— 把不可逆的系统级修改变成可撤销的实验。**

### ⭐⭐⭐⭐⭐ 判据修正：账号信号只能排除、不能定性

⭐⭐⭐⭐⭐ **`Kianuni` 的账号创建于 2026-11-10T02:02:54Z，仓库创建于 02:37:31Z（相差 35 分钟），账号仅 2 个公开仓库、24 followers。** ⭐⭐⭐⭐⭐ **⭐⭐ 而它有 99 blobs、10 个 release（v0.5.1 → v0.7.2）、真实的 iOS 工程结构（`Erosion.xcodeproj/` / `Erosion.entitlements` / `Erosion/bridge.h` / `Erosion/Exploits/bad_query.h`）与 commit 级的安全审计记录。**

⭐⭐⭐⭐⭐ **⭐⭐ 这与 11-12 记录的 `auto-twitch-drops-claim`（账号当天新建 → 判为农场）、本日载荷族（3 分 28 秒窗口批量注册 → 判为农场）在账号信号上完全一样 —— 唯一的分界在内容侧：有没有构建产物、有没有 release、有没有工程结构、有没有可核验的迭代记录。**

### ⭐⭐⭐⭐⭐ 判据修正：commit 数只对「渐进式增长的仓库」有效

⭐⭐⭐⭐⭐ **本窗口 `solana-vigil` 只有 1 个 commit，却有 59 个 blob、6 个 `*_test.go`、2 个 CI workflow、3 个 issue 模板、2 个 systemd unit、Dockerfile、Makefile、CHANGELOG。** ⭐⭐⭐⭐⭐ **⭐⭐ 与本日档案的 `Shape`（1 commit / 2,180 blobs）同族 —— ⭐⭐⭐⭐⭐ ⭐⭐ 本日报的立场：**这两条判据的正确用法不是「判定真假项目」，而是「判定这个仓库的历史是否能反映开发过程」。**

""",
    "2026-11-11": """## 2026-11-11

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---|
| `Kianuni/Erosion-CN` | 986 | 227 | 23.0% | 1 | Swift | 15 | 工具型 |
| `ValidatorStack/solana-vigil` | 157 | 26 | 16.6% | **10** | Go | **1** | 工具型 |

### ⭐⭐⭐⭐⭐ 本日的主题：把「不可逆」做成一个显式的一等概念

⭐⭐⭐⭐⭐ **`solana-vigil` 用「不写」定义安全（只读）；`Erosion-CN` 用「可撤销的写」定义安全（备份 + 回滚）。** ⭐⭐⭐⭐⭐ **⭐⭐ 两者都把「不确定」显式化了 —— 一个用 `unknown`，一个用「备份 + 回滚」这个可验证的状态。**

⭐⭐⭐⭐⭐ **⭐⭐ 而 `Erosion-CN` 的账号判据反例本日成立：账号比仓库早 35 分钟、2 个公开仓库、24 followers，却是 986⭐ / 99 blobs / 10 个 release 的真实工程 —— 账号信号只能排除，不能定性。**

""",
    "2026-11-10": """## 2026-11-10

### 本日新增项目

| 项目 | ⭐ | forks | subs | 语言 | 类别 |
|---|---:|---:|---:|---|---|
| `huamidev/GestaltX` | 1,364 | 41 | — | Swift | 工具型 |
| `TameCarpenterEstate/Roblox-FPS-Optimizer` | 92 | 0 | — | 无 | 观察型（反例样本） |
| `bookleme/bookleme` | 197 | 9 | — | TypeScript | 工具型 |
| `yetone/rewind-for-x` | 152 | 6 | — | TypeScript | 工具型 |

### ⭐⭐⭐⭐⭐ 本日主题：把「我做到了什么」与「什么还没被验证」分开写

⭐⭐⭐⭐⭐ `huamidev/GestaltX` 把「导入的文件是不是这台设备自己的」也做成了可验证的条件；⭐⭐⭐⭐⭐ `TameCarpenterEstate/Roblox-FPS-Optimizer` 是本日记录的反例样本（仓库名声称优化器，内容为空壳）。⭐⭐⭐⭐⭐ **⭐⭐ 与本日窗口 97 个候选、64 个（66.0%）符合空壳特征这一背景相对照，本日建档的两个真项目之所以值得记，是因为它们都把「未验证的部分」显式标注了出来。**

""",
    "2026-11-09": """## 2026-11-09

### 本日新增项目

| 项目 | ⭐ | forks | 语言 | commits | 类别 |
|---|---:|---:|---|---:|---|
| `elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop` | 297 | 172 | 无 | 2 | 观察型（反例样本） |

### ⭐⭐⭐⭐⭐ 本日窗口统计

⭐⭐⭐⭐⭐ **171 个候选中 143 个（83.6%）符合空壳特征（体积 <= 20KB + fork 全 0 + <= 2 commits）；⭐⭐⭐⭐⭐ star 中位数 400，最高频取值 400（89 个）、399（21 个）、398（14 个）、397（6 个）—— 即本日是「同一个 star 值」判据最强的一天。**

⭐⭐⭐⭐⭐ **⭐⭐ 而本日最值得记的是 `LiveWall` 这个反例样本：它只有两个 blob（`LiveWallLauncher.zip` 21,859,851 B + `README.md` 3,173 B），⭐⭐⭐⭐⭐ ⭐⭐ README 里没有一句索取 star 的话，⭐⭐⭐⭐⭐ ⭐⭐ 而它的 297⭐ / 172 fork / 极高 subs 来自付费或批量手段 —— 即「用内容换关注」与「用批量换关注」是两条不同的路径，本日报 11-08 的外挂族走的是前者，本日这个走的是后者。**

""",
}

REPORT = {
    "2026-11-12": """## 2026-11-12
**核心主题：** 本日的关键词是**「边界」**—— 两个真项目都把「我做了什么 / 我没做什么 / 什么还没被验证」写进了产物本身。⭐⭐⭐⭐⭐ `egoist/tinytraffic`（107⭐ ⑂3 · 25 commits · 100 blobs · TypeScript · AGPL-3.0）把隐私承诺做成了一条可检验的算法：**访客标识 = `hash(daily salt, site, IP, user agent)`，salt 在该站点时区的午夜轮换，IP 从不落库，referrer 保留域名与路径但丢弃 query string**；⭐⭐⭐⭐⭐ `Kianuni/Erosion-CN`（986⭐ ⑂227 · 15 commits · 99 blobs · Swift · GPL-3.0）把系统标志位的修改做成**写入前自动备份原值 + 一键回滚**。⭐⭐⭐⭐⭐ **⭐⭐ 本日最值得记的判据修正是一个反例：`Kianuni` 的账号创建于仓库创建前 35 分钟、仅 2 个公开仓库、24 followers，⭐⭐⭐⭐⭐ ⭐⭐ 而它有 99 blobs、10 个 release、真实的 iOS 工程结构与 commit 级安全审计记录 —— 即「账号当天新建 ⇒ 农场」这条本日报多次使用的判据在此给出错误结论，账号信号只能作辅证、不能定性。** ⭐⭐⭐⭐ 证据边界：本日全部元数据取自 2026-11-12 经 `gh` CLI 认证的 GitHub REST / Search API 快照；⭐⭐⭐ ⚠️ star 增速未做统计；⭐⭐⭐ ⚠️ 未在任何设备上运行 `Erosion-CN`，未执行任何写入或回滚。

**关键项目：**
- 🪨 [Kianuni/Erosion-CN](projects/erosion-cn.html) — iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（986⭐ ⑂227 · 15 commits · 99 blobs · Swift · GPL-3.0）—— **写入前自动备份原值 + 一键回滚**
- 🛡️ [ValidatorStack/solana-vigil](projects/solana-vigil.html) — 只读的 Solana 验证人运维工具（157⭐ ⑂26 · subs 10 · 1 commit · 59 blobs · Go · MIT）—— **观测失败 → `unknown`，绝不伪造健康值**
- 📊 [egoist/tinytraffic](projects/tinytraffic.html) — 单二进制自托管 web 分析（107⭐ ⑂3 · 25 commits · 100 blobs · TypeScript · AGPL-3.0）—— **隐私承诺写成可检验的算法**

---

""",
    "2026-11-11": """## 2026-11-11
**核心主题：** 本日的关键词是**「不可逆」**—— 两个真项目从两个方向回答了同一个问题：如何让会改变系统状态的操作变得可控。⭐⭐⭐⭐⭐ `ValidatorStack/solana-vigil`（157⭐ ⑂26 · subs 10 · 1 commit · 59 blobs · Go · MIT）用**「不写」**定义安全：README 逐项列出它不做的事（不索取密钥、不签名、不改主机设置、不重启验证人、不切换身份），⭐⭐⭐⭐⭐ **而工具的十个 `internal/` 包里确实没有对应的模块 —— 即信任的建立从「读文档」降级为「看结构」**；⭐⭐⭐⭐⭐ `Kianuni/Erosion-CN`（986⭐ ⑂227 · 15 commits · 99 blobs · Swift · GPL-3.0）用**「可撤销的写」**定义安全：**写入前自动备份原值 + 一键回滚**。⭐⭐⭐⭐⭐ **⭐⭐ 两者都把「不确定」显式化了 —— 一个用 `unknown`（README 原文：Missing RPC fields and failed observations become `unknown`, never a fabricated healthy value），一个用「备份 + 回滚」这个可验证的状态。** ⭐⭐⭐⭐⭐ **⭐⭐ 而本日最值得记的是那个判据反例：`Kianuni` 的账号创建于仓库创建前 35 分钟、仅 2 个公开仓库、24 followers，却是 986⭐ / 99 blobs / 10 个 release 的真实工程 —— 本日报此前多次使用的「账号当天新建 ⇒ 农场」在此给出错误结论，因此账号信号只能作辅证、不能定性。** ⭐⭐⭐⭐ 证据边界：本日全部元数据取自 2026-11-11 经 `gh` CLI 认证的 GitHub REST / Search API 快照；⭐⭐⭐ ⚠️ star 增速未做统计；⭐⭐⭐ ⚠️ 未在任何设备上运行 `Erosion-CN`，未运行 `solana-vigil`，未接触任何测试网或主网节点。

**关键项目：**
- 🛡️ [ValidatorStack/solana-vigil](projects/solana-vigil.html) — 只读的 Solana 验证人运维工具（157⭐ ⑂26 · subs 10 · 1 commit · 59 blobs · Go · MIT）—— **「unknown」是一等状态；告警抑制的六个维度**
- 🪨 [Kianuni/Erosion-CN](projects/erosion-cn.html) — iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（986⭐ ⑂227 · 15 commits · 99 blobs · Swift · GPL-3.0）—— **备份 + 回滚把不可逆变成可撤销**

---

""",
    "2026-11-10": """## 2026-11-10
**核心主题：** 本日的关键词是**「验证」**—— 建档的真项目都把「我做到了什么」与「什么还没被验证」分开写。⭐⭐⭐⭐⭐ `huamidev/GestaltX`（1,364⭐ ⑂41 · SwiftUI + 共享扩展）把「导入的文件是不是这台设备自己的」也做成了可验证的条件；⭐⭐⭐⭐⭐ `bookleme/bookleme`（197⭐ ⑂9）与 `yetone/rewind-for-x`（152⭐ ⑂6）同属工具型。⭐⭐⭐⭐⭐ **⭐⭐ 与本日窗口 97 个候选中 64 个（66.0%）符合空壳特征（体积 <= 20KB + fork 全 0 + <= 2 commits）这一背景相对照，本日建档的真项目之所以值得记，是因为它们都把「未验证的部分」显式标注了出来 —— 而同日的 `TameCarpenterEstate/Roblox-FPS-Optimizer`（92⭐ ⑂0 · 2 commits · 8KB）则是本日记录的反例样本：仓库名声称是优化器，内容却是空壳。** ⭐⭐⭐⭐ 证据边界：本日全部元数据取自 2026-11-10 经 `gh` CLI 认证的 GitHub REST / Search API 快照；⭐⭐⭐ ⚠️ star 增速未做统计；⭐⭐⭐ ⚠️ 各项目的功能与性能结论均为作者自述，本日报未复现。

**关键项目：**
- 🧩 [huamidev/GestaltX](projects/gestaltx.html) — iOS 27.x 的 MobileGestalt 编辑器（1,364⭐ ⑂41 · Swift）
- 📖 [bookleme/bookleme](projects/bookleme.html) — 阅读器工具（197⭐ ⑂9 · TypeScript）
- 🔁 [yetone/rewind-for-x](projects/rewind-for-x.html) — X 平台回溯工具（152⭐ ⑂6 · TypeScript）
- ⚠️ [TameCarpenterEstate/Roblox-FPS-Optimizer](projects/roblox-fps-optimizer.html) — 反例样本（92⭐ · 空壳）

---

""",
    "2026-11-09": """## 2026-11-09
**核心主题：** 本日的关键词是**「注意力的价格」**—— 同样是获取关注，两条路径的成本结构完全不同。⭐⭐⭐⭐⭐ 本日窗口 171 个候选中 **143 个（83.6%）**符合空壳特征（体积 <= 20KB + fork 全 0 + <= 2 commits），⭐⭐⭐⭐⭐ **star 中位数 400，最高频取值 400（89 个）、399（21 个）、398（14 个）—— 即本日是「同一个 star 值」判据最强的一天**：⭐⭐⭐⭐⭐ **⭐⭐ 一批仓库把 star 值精确地钉在同一个数字上，而本日建档的反例样本 `elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop`（297⭐ ⑂172 · 2 commits · 仅 2 个 blob：`LiveWallLauncher.zip` 21,859,851 B + `README.md` 3,173 B）走的是另一条路 —— 它的 README 里没有一句索取 star 的话，⭐⭐⭐⭐⭐ ⭐⭐ 它的关注来自付费或批量手段。⭐⭐⭐⭐⭐ ⭐⭐ 即「用内容换关注」（11-08 的外挂族）与「用批量换关注」（本日这个）是两种不同成本结构的路径。** ⭐⭐⭐⭐ 证据边界：本日全部元数据取自 2026-11-09 经 `gh` CLI 认证的 GitHub REST / Search API 快照；⭐⭐⭐ ⚠️ star 增速未做统计；⭐⭐⭐ ⚠️ `elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop` 的账号与仓库在 2026-11-13 快照时刻均返回 404，无法复核其当前状态。

**关键项目：**
- 🖥️ [elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop](projects/livewall.html) — 反例样本（297⭐ ⑂172 · 仅 2 个 blob · README 无索取 star 的语句）

---

""",
}


def insert_before(path, anchor, entries):
    p = ROOT / path
    c = p.read_text(encoding="utf-8")
    added = []
    for day in sorted(entries, reverse=True):
        if f"## {day}\n" in c:
            print(f"{path}: {day} already present -> skipped")
            continue
        if anchor not in c:
            print(f"{path}: anchor {anchor!r} not found")
            continue
        c = c.replace(anchor, entries[day] + anchor, 1)
        added.append(day)
    p.write_text(c, encoding="utf-8")
    print(f"{path}: inserted {added} before {anchor!r}")
    return c


insert_before("indexes/trend-index.md", "## 2026-11-08\n", TREND)
insert_before("daily-report.md", "## 2026-11-08\n", REPORT)

for f in ["indexes/trend-index.md", "daily-report.md"]:
    c = (ROOT / f).read_text(encoding="utf-8")
    heads = [ln for ln in c.splitlines() if ln.startswith("## ")]
    print(f"\n{f}: first 8 headings -> {heads[:8]}")
