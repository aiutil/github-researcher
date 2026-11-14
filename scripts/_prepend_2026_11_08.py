#!/usr/bin/env python3
'''Phase 5.1 / 5.2: prepend the 2026-11-08 entry to indexes/trend-index.md and
daily-report.md, keeping both files in reverse-chronological order.'''

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TREND_BLOCK = """## 2026-11-08

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | 体积 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| `Poltergeistlunagrid/Steam-Idler` | 425 | 313 | 73.6% | **25** | Python | 6 KB | 4 | 观察型（反例样本） |
| `sentinelsoldierprize/Minecraft-AFK-Bot` | 425 | 260 | 61.2% | **35** | Python | 7 KB | 5 | 观察型（反例样本） |
| `Th0rgal/satmux` | 316 | 17 | 5.4% | 1 | Python | 22 KB | 3 | 工具型 |
| `MajestyPoemFold/ghostclick-mouse-double-click-fix` | 136 | 21 | 15.4% | 0 | Rust | 12,029 KB | 1 | 工具型 |
| `dabingfy-dot/solo-to-team-skills` | 130 | 14 | 10.8% | 4 | 无（Markdown） | 13,997 KB | 1 | 工具型 |
| `lxe/phoneuse` | 118 | 10 | 8.5% | 2 | Python | 594 KB | 85 | 工具型 |

**⭐⭐⭐⭐⭐ 本表最重要的一列是 `subs`，而它恰好在本日被证伪。** 11-07 日报把 `subscribers_count` 列为「噪声极低但样本极小的指标」；本日实测：**两个 425⭐ 的空壳仓库的 subs（25 / 35）高于全部四个真项目（4 / 2 / 1 / 0）**。原因写在它们的 README 里 —— Quick Start 之后与文末各一次 `**⭐ Star the repo if it helped you.**`。

### ⭐⭐⭐⭐⭐ 判据修正：subs 只能同作者族内比较

| 仓库 | ⭐ | forks | subs | README 索取 star？ | 代码状态 |
|---|---:|---:|---:|---|---|
| `sentinelsoldierprize/Minecraft-AFK-Bot` | 425 | 260 | **35** | **是（两处）** | 模板骨架，输出占位数据 |
| `Poltergeistlunagrid/Steam-Idler` | 425 | 313 | **25** | **是（两处）** | 模板骨架，无 Steam 实现 |
| `dabingfy-dot/solo-to-team-skills` | 130 | 14 | 4 | 否 | 4 支技能 + 模板 + 案例 |
| `lxe/phoneuse` | 118 | 10 | 2 | 否 | 完整实现，85 commits |
| `Th0rgal/satmux` | 316 | 17 | 1 | 否 | 7 文件完整实现 |
| `MajestyPoemFold/ghostclick-mouse-double-click-fix` | 136 | 21 | 0 | 否（导流 Discord） | Rust + Tauri，77 文件 |

> ~~「subs 是一个噪声极低但样本极小的指标」~~
> **「subs 只在同作者族内可比；跨作者比较前必须先确认该仓库的 README 是否含索取 star/watch 的语句。」**

**⭐⭐⭐⭐⭐ 本日报由此得出本日最重要的方法论结论：判据必须成对部署 —— 一个正面信号 + 一个反向信号同时检查。** 本日可用的四元组：**(a) README 是否索取 star/watch；(b) fork 到达的时间分布；(c) 文件 md5 是否与已知农场集合重复；(d) 代码能否 import / 运行。**

### ⭐⭐⭐⭐⭐ 跨日模板血缘（本日报第一次拿到跨日期的文件级证据）

| 文件 | md5 | 出现日期与仓库 |
|---|---|---|
| `.gitignore`（4,664 B） | `e18f025c87b71b9fe481f53ac6e8235d` | **2026-11-06**：`roblox-studio-mcp` / `roblox-performance-tool` / `crypto-portfolio-tracker` / `discord-quest-completer`；**2026-11-07**：`Steam-Idler` / `Minecraft-AFK-Bot` |
| `helpers.py`（97 B） | `8470fd5b911eacd63327be59d2562f16` | **2026-11-06**：`crypto-portfolio-tracker` / `discord-quest-completer`；**2026-11-07**：`Steam-Idler` / `Minecraft-AFK-Bot` |
| `initial.html`（485 B） | `258a0f5edf5d42288cfc1866497dc7dd` | **2026-11-07**：85 个空壳簇中抽样 30 个里有 28 个命中（内容是把 `README.md`/`CONTRIBUTING.md`/`SECURITY.md` 推入 `std::vector` 的 C++ 玩具） |

### ⭐⭐⭐⭐⭐ fork 时间分布（第四日采集，判据仍然有效）

| 仓库 | forks | 间隔中位数 | ≤10s 占比 | 判定 |
|---|---:|---:|---:|---|
| `sentinelsoldierprize/Minecraft-AFK-Bot` | 260 | **4.0 s** | 98/99 | 机器 |
| `Poltergeistlunagrid/Steam-Idler` | 313 | **5.0 s** | 98/99 | 机器 |
| `LumiVikinggard89137/ai--manus`（关键词簇样本） | 50 | 56.0 s | 6/49 | 分发网络，待观察 |
| `JenkinWoo/sheeridVerify`（11-06 真人样本复测） | 889 | **74.0 s** | 19/99 | 真人 |
| `MajestyPoemFold/ghostclick-mouse-double-click-fix` | 21 | **1555.0 s** | 0/20 | 真人 |

**⭐⭐⭐⭐⭐ 对照 11-06 的 `roblox-studio-mcp`（5.0 s / 96.9%）与 `roblox-performance-tool`（6.0 s / 94.5%），本日两个 425⭐ 仓库是同一套投放基础设施的第三、第四次出现。**

### ⭐⭐⭐⭐⭐ 本日 162 个候选的形态分布

| 形态 | 数量 | 判据 |
|---|---:|---|
| README 为空 | **85 / 162（52.5%）** | `readme` 端点返回 0 字节；**其中 84 个仓库名带 `resp`/`rpocket`/`resocket` 标记**；star 全为 42、forks 全为 0、无 LICENSE、体积 3–10 KB；`CONTRIBUTING.md` 顶部是伪造的 `Downloads-40K+` 徽章；描述**直接售卖外挂**（Warframe Hack 2026 / ROBLOX Universal ESP Module / aimbot / Monero Miner / Claude jailbreak prompt） |
| SEO 关键词投毒 | 57 / 162 | README 长度只有 7,256 与 7,234 两种、star 只有 91 与 92 两个取值、许可全 Apache-2.0、创建窗口 6 小时 54 分；顶部是 Dropbox 直链 `Manus_Studio.rar` + `PROMO2026`，末尾是 24 个 `Related Search Terms` |
| 模板骨架 + 索取 star | 2 / 162 | 见上表；**subs 25 与 35** |
| 真实工程项目 | 18 / 162 | 其余，含 phoneuse / satmux / ghostclick / solo-to-team-skills |

**⭐⭐⭐⭐⭐ 谱系已完整**：可执行 PowerShell 载荷（11-06 前）→ starter 模板（11-06）→ 索取 star 的同模板变体（11-07）→ 空壳占位符 + 关键词投毒（11-07）—— **四天四种形态，同一套基础设施。**

### 持续跟踪项目状态

| 项目 | 变化 | 说明 |
|---|---|---|
| `interplains/zero-breach` | **档案指向错误（已发现）** | ⭐⭐⭐⭐⭐ `interplains/zero-breach`（`id=1424399708`，创建 2026-10-18，1,218⭐，9 release，最新 v0.1.8 / 2026-10-20）与 `interplains/Zero-Breach-Toolkit`（`id=1433297111`，创建 2026-10-25，**4,550⭐**，23 release，最新 v2.0.6 / 2026-11-05）是**两个不同仓库**（`fork=False`、`parent=None`），**不是改名关系**。11-06 记录的 4,475⭐ / 12,477 KB / v0.1.13 全属 `Zero-Breach-Toolkit`，而 `projects/zero-breach.md` 的 frontmatter 与 URL 写的是 `zero-breach`；且该档案正文引用的 `PRIVACY.md` 与 `docs/VERIFYING.md` **只存在于 `Zero-Breach-Toolkit`**（`zero-breach` 两者皆无）—— 即档案内容与档案标题指向了不同的仓库 |
| `voyager-so/vork` | 增长 | 197 → **850⭐**，forks 13 → 55，subs 4 → 7，commits 1 → **5**，`pushed_at` 2026-11-07T20:54:07Z |
| `JosssphZhou/poki` | 增长 | 406 → **493⭐**，forks 83 → 105，subs 仍为 **1**，commits 23 → **121**，oi 0 → 14，`pushed_at` 2026-11-07T18:27:05Z |
| `majorminorlabs/hermes-voice` | 增长 | 424 → **499⭐**，forks 20 → 28，subs 3 → 5，commits 仍 35，`pushed_at` 2026-11-06T21:59:50Z |
| `devvmhq/devvm` | 增长 | 116 → **353⭐**，forks 2 → 12，subs 1，commits 600 → **611**，`pushed_at` 2026-11-07T22:17:57Z |
| `Tropicaldrescoop/discord-id-osint-checker` | 增长但 commits 停滞 | 329 → **381⭐**，forks 73 → 87，subs 仍 0，commits 仍 43，**`pushed_at` 2026-11-07T03:26:48Z 而最后 commit 为 2026-10-30T12:13:22Z** |
| `rddmwmddr/android-ad-cleaner` | 增长 | **6,924⭐** ⑂620 · subs 15 · oi 208 · `pushed_at` 2026-11-07T16:13:18Z（持续活跃） |
| `valentderah/totk-pc-recomp` | 增长 | **5,670⭐** ⑂467 · subs 68 · oi 360 · `pushed_at` 2026-11-07T17:41:26Z |
| `unclebob/ub-mode` | **⭐⭐⭐⭐ 增长但无新提交** | **7,252⭐** ⑂407 · subs 56 · oi 10 · **`pushed_at` 停在 2026-11-02T15:08:31Z** —— **⭐⭐⭐⭐⭐ 本日记录的第二个「star 与开发解耦」样本**：它 11-02 之后 star 从 341 涨到 7,252（+2,027%），而 commit 与 `pushed_at` 都没动，**且这是它首次出现两位数的 subs（56）** —— ⭐⭐⭐⭐ **但本日已证明 subs 可被 README 索取 star 抬高，故此处的 56 需在下一日复测中观察其构成** |
| `DenisSergeevitch/ex-ussr-kinship-research` | 增长 | **2,137⭐** ⑂216 · subs 14 · oi 0 · `pushed_at` 2026-11-07T21:16:24Z（活跃） |
| `SAOS-3624/dsh-see-now` | 增长 | **462⭐** ⑂43 · subs 1 · oi 14 · `pushed_at` 2026-11-07T09:19:58Z |
| `trailofbits/brotli-checker` | 停滞 | 68⭐ ⑂4 · subs 0 · oi 3 → 9 · `pushed_at` 2026-11-06T08:25:52Z，**最后 commit 仍为 2026-10-27T20:20:25Z** |
| `YoyoLin008/mcreplay` | **停滞** | 199⭐ ⑂12 · subs 0 · oi 0 · **`pushed_at` 仍为 2026-10-24T18:56:03Z**（连续第 14 天无新 push） |
| `HerdBuilderEstimate/roblox-studio-mcp` | 无变化 | 427⭐ ⑂260 · subs 8 · `pushed_at` 仍为 2026-11-06T06:16:56Z |
| `JenkinWoo/sheeridVerify` | **⭐⭐⭐⭐⭐ 增长但无新提交** | **1,637⭐** ⑂889（fork/star 54%）· subs 0 · oi 0 · `pushed_at` 2026-11-06T09:54:37Z —— ⭐⭐⭐⭐⭐ **fork 间隔中位数复测为 74.0 秒（19/99 个间隔 ≤10 秒，跨度 404.8 分钟），与 11-06 的 73 秒一致，仍属真人节奏；但它是本日全部候选中 fork 数增长最快的一个（360 → 889）且 subs 仍为 0** —— ⭐⭐⭐⭐ **「fork 涨、commit 不动、subs 为 0」三者同时成立，是本日最需要下一日复测的组合** |
| `deepseek-ai/DeepInfer` | 增长 | **25,602⭐** ⑂3,137 · subs 65 · oi 247 · `pushed_at` 2026-11-03T07:31:59Z（**star 继续涨而 push 停在 11-03**） |

### 排名变化

- **新增**：`lxe/phoneuse` / `Th0rgal/satmux` / `MajestyPoemFold/ghostclick-mouse-double-click-fix` / `dabingfy-dot/solo-to-team-skills`（真项目）＋ `Poltergeistlunagrid/Steam-Idler` / `sentinelsoldierprize/Minecraft-AFK-Bot`（反例样本）
- **⭐⭐⭐⭐⭐ 方法论变更**：11-07 记录的「看 fork 的时间分布与账号年龄分布」本日继续有效（机器 4–6 秒 vs 真人 74 秒 / 1555 秒），**但新增一条更前置的规则** —— **先查 README 是否索取 star，再看 subs**。
- **⭐⭐⭐⭐⭐ 档案修正**：`projects/zero-breach.md` 的仓库指向需改为 `interplains/Zero-Breach-Toolkit`（内容与 URL 同步），或档案内容需整体重写以匹配 `interplains/zero-breach`。**本日报已记录该发现，未擅自改写历史日报正文。**

"""

REPORT_BLOCK = """## 2026-11-08
**核心主题：** 本日最值得记的不是任何单一项目的星数，而是**「注意力」这一指标第一次出现了一个可以当众证伪的对照实验**：同一份 162 个仓库的榜单里，两个 425⭐ 的仓库比当天所有真项目的订阅数都高（subs 25 / 35 vs 4 / 2 / 1 / 0），而它们的代码是一个 4 commit、5 文件、6 KB 的模板骨架 —— 其 `helpers.py` 的内容逐字节等于 11-06 那批农场的同一个文件（md5 `8470fd5b911eacd63327be59d2562f16`），`.gitignore` 的 md5 `e18f025c87b71b9fe481f53ac6e8235d` 更是在 11-06 与 11-07 之间、在这两个仓库之间**跨日复用**。⭐⭐⭐⭐⭐ 而拆穿它的不是星数、不是 fork 数，**恰恰是本日报连日推荐的「订阅数」判据自己失灵了**：11-07 的日报把 subs 列为「噪声极低但样本极小」的深度信号，而这两个仓库的 README 末尾正写着 `**⭐ Star the repo if it helped you.**` —— **即「关注」本身被明写成一条投放指令，而它同时抬高了 subs 与 stars 两个指标**。⭐⭐⭐⭐⭐ **这是本日报记录到的第一个「判据被针对」案例：判据本身成了攻击面。** 第二个同日发现是**投递脚本从「载荷」退化成「占位符」**：本日 162 个候选里 **85 个（52.5%）README 为空、体积 3–10 KB、forks 全为 0、star 全为 42、无 LICENSE**，其中 **84 个的仓库名含 `resp`/`rpocket`/`resocket` 标记**，抽样 30 个树里有 **28 个的 `initial.html` 逐字节相同**（md5 `258a0f5edf5d42288cfc1866497dc7dd`，内容是一个把 `README.md`/`CONTRIBUTING.md`/`SECURITY.md` 推入 `std::vector` 的 C++ 玩具），`CONTRIBUTING.md` 顶部是伪造的 `Downloads-40K+` 徽章 —— **即：过去五天记录的三种形态（可执行 PowerShell 载荷 → starter 模板 → 空壳占位符）在本日形成了一条完整的降级曲线**，而这一批的描述文本是**真的在卖外挂**（`Warframe Hack 2026`、`ROBLOX Universal ESP Module`、`Monero Miner`），**⭐⭐⭐ 这意味着它已经不是「投放」而是「货源」：模板农场变成了外挂分销的货架，而 GitHub 的 star 机制对「一个伪装成作弊器的空目录」零感知**。第三个同日发现是 **57 个仓库共用同一份「Manus AI Agent」README（长度 7,256 / 7,234 两种）、star 只有 91 与 92 两个取值、Apache-2.0 全同、创建窗口横跨 6 小时 54 分**，README 顶部是 `[![Download Manus](...)](https://www.dropbox.com/scl/fi/7otex5g3in9c38g1ney7u/Manus_Studio.rar?...&dl=1)` 加一行 `PROMO2026`，末尾是一段 24 个关键词的 `## Related Search Terms` —— **⭐⭐⭐⭐⭐ 这是本日报记录到的第一例「SEO 关键词投毒」**：README 不再是给人读的文档，而是给搜索引擎读的关键词堆；而此前五天的农场形态都是「给人看的」。⭐⭐⭐⭐ 与这批同框的四个真项目，恰好给出四种**互相不重叠**的诚实形态：`lxe/phoneuse`（118⭐ · 85 commits · MIT）在 README 最前面用 `> [!WARNING]` 写明「**Under heavy construction… built quickly for my own setup: one iPhone 17 Pro, Arch Linux, Hyprland and an NVIDIA GPU. Other setups will probably need fixes**」，并用一张**实测环境表**（iPhone 17 Pro / iOS 26、Arch Linux + BlueZ 5.87、Hyprland 0.56、UxPlay 1.73.7、GStreamer 1.28、Python 3.14）逐项标注「Tested with」；`Th0rgal/satmux`（316⭐ · 7 文件 · 零依赖纯标准库）把**物理下界**写进 `## Limits`（「**Latency floor (~580–650 ms)**: Speed-of-light propagation to geostationary orbit (35,786 km) does not change; satmux removes extra round-trips, **not the physical RTT of one hop.**」）；`MajestyPoemFold/ghostclick-mouse-double-click-fix`（136⭐ · Rust + Tauri 2 · 77 文件）**从用户的真实故障出发**而不是从技术出发，并且**把检测结果导出为可提交给厂商的 RMA 证据**（而不是只给结论）；`dabingfy-dot/solo-to-team-skills`（130⭐ · 中英双语 · 5 topics）把「证据先于完成声明」写成一条**可执行的铁规**并附带「该停一下的信号」与「常见借口 → 实际上」两张清单，同时在 README 顶部**主动降级自己的支持声明**（`v0.9-draft`、`Claude Code 结构已备、走通待补`、`部分宿主未保留技能加载的原始轨迹；不表示每家四个技能都逐一被调用，也不证明效果`）。⭐⭐⭐⭐⭐ **而这四个真项目的订阅数是 2 / 1 / 0 / 4 —— 全部低于两个空壳仓库的 25 与 35。本日报据此修正昨日的判据：不是「subs 少说明质量高」，而是「在 subs 被明写成投放指令的年代，subs 只能用于同一作者族内比较，不能跨作者比较」。** ⭐⭐⭐⭐⭐ **同日另有一项对档案本身的修正**：`interplains/zero-breach` 与 `interplains/Zero-Breach-Toolkit` 经 `id`/`fork`/`parent`/`created_at`/release 列表/文件存在性六字段交叉确认是**两个不同仓库**（1,218⭐ vs 4,550⭐），而 `projects/zero-breach.md` 的正文与 URL 指向的是前者、内容却描述后者（`PRIVACY.md` 与 `docs/VERIFYING.md` 只存在于后者）—— **这是「`created_at` 会说谎」「改名时间戳」那一族问题的第 N 例，且更严重：归档档案本身指向了错误的仓库。**

**证据边界：** 本日全部元数据取自 **2026-11-08 CST 的 GitHub REST / Search API 快照**（经 `gh` CLI 认证），覆盖 `search/repositories`（`created:2026-11-07 stars:>=30`，`total_count` = 162）、`repos/{owner}/{repo}`、`git/trees/HEAD` 与 `?recursive=1`、`commits`（含 Link 头分页）、`forks`（时间戳）、`releases`、`contributors`、`contents/{path}`（`Accept: application/vnd.github.raw`）、`users/{owner}`。⭐⭐⭐ **`stargazers` 与 `subscribers` 端点在本窗口对本 token 返回 404，因此本日报未能对 star / subscriber 的账号年龄做逐个取证**，请以 fork 时间分布、commit 时间戳与文件 md5 证据为准。⭐⭐⭐ **star 增速未做统计**（需分页遍历 stargazer 列表），故所有 ⭐ 数均为快照绝对值。⭐⭐⭐ **两个农场仓库的代码均未被执行**；本日报对其「无实现」的判断依据是树清单、文件原文、`language` 字段与 README 宣称的依赖缺失，**不主张其意图**。⭐⭐⭐ **`ghostclick` 的系统级过滤机制、`phoneuse` 的 `unlock.py` 与 `screen_points`、`satmux` 的 `satmux.py` 内部实现、`solo-to-team-skills` 在任一宿主上的调用结果，本窗口未核验**；`docs/solo-to-team-value.pdf`（17 页）未打开核验。

**关键项目：**
- 📱 [lxe/phoneuse](projects/phoneuse.html) — 让 Linux PC 看见并操作**未越狱的 iPhone**（AirPlay 镜像进、Bluetooth HID 出，手机侧零安装）（118⭐ ⑂10 · **subs 2** · oi 0 · 85 commits · 594 KB · Python · MIT · 34 文件 · User `lxe`（账号 2012-02-29 创建，271 个公开仓库））—— **⭐⭐⭐⭐⭐ 本日最值得抄的是它对「未验证」的写法**：README **第一个块**即 `> [!WARNING]` + `**Under heavy construction.** This is a technology demo, built quickly for my own setup: one iPhone 17 Pro, Arch Linux, Hyprland and an NVIDIA GPU. Other setups will probably need fixes…`，⭐⭐⭐⭐ 紧接着的 `## What you need` 表**逐项钉版本**（iPhone 17 Pro / iOS 26、Arch Linux + BlueZ 5.87、Hyprland 0.56、UxPlay 1.73.7、GStreamer 1.28、GTK 4 + `gtk4paintablesink` 4.24、Python 3.11+ 实测 3.14、`grim`），⭐⭐⭐⭐⭐ **而第三列里那些像抱怨的句子其实是「我的结论在什么条件下成立」**：「other models: set `screen_points`」「the Bluetooth adapter must be in range of the phone」「window geometry and the cursor come from Hyprland's IPC」「NVIDIA decoding used when available, software otherwise」；⭐⭐⭐⭐⭐ **架构上它把两个通道刻意拆开**：`ARCHITECTURE.md` 首段写「The screen comes in over AirPlay… input goes out over Bluetooth… **Nothing runs on the phone.**」；⭐⭐⭐⭐ **HID daemon 以 root 跑在 systemd 下，report descriptor 同时声明键盘、相对鼠标与绝对指针**，且 `phoneuse install` 明写它会「disable bluetoothd's own input and hostname plugins, **so this PC stops accepting Bluetooth keyboards and mice of its own**」并给出卸载命令；⭐⭐⭐⭐ **输入映射走 Hyprland IPC 取窗口几何与光标，而不是盲发像素**；⭐⭐⭐ 网络边界精确枚举（TCP 7000/7001/7100、UDP 6000/6001/7011）；⭐⭐⭐ **必须开 AssistiveTouch 并关掉 Dwell Control**（否则光标静止时自己点）；⭐⭐⭐⭐⭐ **对 agent 的入口是 CLI + MCP 双份**（`bin/phoneuse` / `bin/phoneuse-mcp`），视觉侧走 OCR + grounding；⚠️ **subs 仅 2、contributors 1 人、releases 0、topics 空数组**；⚠️ **全部结论基于单一机型与单一桌面，本日报未在任何硬件上复现**
- 🛰️ [Th0rgal/satmux](projects/satmux.html) — 静止轨道（GEO）客机 Wi-Fi 的 TCP 多路复用器 + 1-RTT HTTP/TLS 中继（纯 Python 3 标准库、零依赖）（316⭐ ⑂17 · **subs 1** · oi 0 · 3 commits · 22 KB · 7 文件 · Python · MIT · User `Th0rgal`（账号 2018-07-28 创建，253 个公开仓库））—— **⭐⭐⭐⭐⭐ 本日最值得抄的是它把物理下界写进 `## Limits`**：「**Latency floor (`~580–650 ms`):** Speed-of-light propagation to geostationary orbit (`35,786 km`) does not change; `satmux` removes extra round-trips, **not the physical RTT of one hop.**」⭐⭐⭐⭐ 并逐条给出另外两条边界（per-seat shaper ~4–5 Mbps「already-compressed binaries stay bounded by the seat cap」；「**Single paid session:** … **it does not bypass captive portals.**」）；⭐⭐⭐⭐⭐ **它的测速表把「没赢的格子」也标了出来**：GitHub Repo（raw **TIMEOUT** → 4.66s，**FIXED ✓**）、GitHub API（raw **TCP RESET** → 2.66s **FIXED ✓**）、Hacker News（raw **TIMEOUT** → 2.28s **FIXED ✓**）、MDN Docs（12.01s → 2.30s，**5.2×**）、Cloudflare（2.97s → 1.40s，**2.1×**）、PyPI（7.09s → 2.64s，**2.7×**），汇总「**6-Origin Burst: 19.13s (3/6 failed) → 5.35s (0/6 failed) [3.6× faster · -76% TTFB]**」—— ⭐⭐⭐⭐⭐ **前三行的 FIXED 与后三行的倍数含义完全不同：前者是「让失败变成成功」，后者才是提速**；⭐⭐⭐⭐ **问题诊断是三段可核验结构**（客舱 `:443` PEP 代理在负载下丢连接且非 443 端口透传 / 每个 origin 付多次卫星往返 / 丢包使 `cwnd` 反复腰斩而令牌桶用不满），**对策与成因一一对应**（12 条常驻 `:8444` 载波池按最近字节负载调度避免 keepalive 造成队头阻塞 / 0-RTT 在 `<1 ms` 内返回 `OK` 并把 `FT_OPEN` + TLS ClientHello 放进同一 TCP 突发同时保留端到端 TLS / 1-RTT 地面取回用 `BLAKE2b-512` + `HMAC-SHA256` 加密流，地面 VM 在光纤上做 DNS、已验证的 TLS 1.3 与 zlib 压缩）；⭐⭐⭐⭐⭐ **它连 `gh` 的代理绕过都写进了设计**（「Go binaries such as `gh` ignore macOS `scutil` proxies」→ 暴露 `0600` 的 `/tmp/satmux-gh-tls.sock`）；⭐⭐⭐ **部署路径可交给 coding agent**，地面站选址写成出口 ASN → 机房列表的查表；⭐⭐ **并要求在机上暂停 UDP VPN**（「blocked UDP retry traffic competes with cabin airtime」）；⚠️ **subs 1、contributors 1 人、releases 0、topics 空数组**；⚠️ **全部性能数字为作者自述的一次性测量（Inmarsat GX、~620 ms RTT、SITA `AS206433` 阿姆斯特丹地面站），本日报未复现，README 也未给方差或重复次数**；⚠️ **需在地面站自备付费 VM（$0.01–0.03/h），不是一个「装上就能用」的工具**
- 🖱️ [MajestyPoemFold/ghostclick-mouse-double-click-fix](projects/ghostclick-mouse-double-click-fix.html) — Windows 10/11 的**鼠标「幽灵点击」（mouse chatter / switch bounce）检测与修复**（Rust + Tauri 2）（136⭐ ⑂21 · **subs 0** · oi 0 · 1 commit · 12,029 KB · 77 文件 · Rust · MIT · 1 release · User `MajestyPoemFold`（账号 2026-08-15 创建，仅 2 个公开仓库））—— **⭐⭐⭐⭐⭐ 它把问题的定义放在用户可观察的现象上而不是技术名词上**：首屏 hero 图 alt 文本即「a strip of chart recorder paper with a 6 ms ghost click circled in red ink」，⭐⭐⭐⭐⭐ **而最见功力的一步是「learns a debounce threshold from your real double-clicks」** —— 不内置固定去抖阈值，而是**先让用户自己双击、从真实输入里学出这台设备这只手在这个灵敏度下的阈值**；⭐⭐⭐⭐ **输出是条带图而非布尔值**（每键一支笔，6 ms 与 11 ms 的幽灵点击被红笔圈出并标注），⭐⭐⭐⭐⭐ **而「exports RMA evidence」是本日所有项目中最值得架构师记的一句**：它不只输出结论，而是**产出可提交给厂商退货/换货的证据材料**（与本日报连日记录的「把边界写进输出」方向相反 —— 前者说清不能保证什么，后者把证据造出来）；⭐⭐⭐⭐⭐ **它的分发选择构成本日最重要的对照**：把用户导流到 Discord（`discord.gg/INVITE`），**README 全文没有一句索取 star 的话**，因此 **subs = 0** —— 与两个 425⭐ 空壳把 `⭐ Star the repo if it helped you.` 写两遍形成教科书级对照；⭐⭐⭐⭐ 另两项独立能力是「catches drag and drop drops」（拖放丢帧是另一类故障）与 `releases/latest/download/app.zip` 直分发；⭐⭐⭐⭐ **工程面完整**：CI workflow、三份 issue 模板、CHANGELOG / ROADMAP / FAQ / CONTRIBUTING、`.github/media/` 下 11 张品牌资产 —— 对照 85 个空壳的 2 个文件；⚠️ **subs 0、oi 0、contributors 1 人、owner 账号仅两个月大**；⚠️ **全部硬件结论为作者自述，本日报未在真实鼠标上复现**；⚠️ **「学习阈值可能误吞合法双击」是本档案识别出的最关键未解风险，README 未见相关说明**
- 🤝 [dabingfy-dot/solo-to-team-skills](projects/solo-to-team-skills.html) — 「一个人统筹一支 AI 团队」的协作技能包（中英双语，4 支技能 + 模板 + 脱敏案例）（130⭐ ⑂14 · **subs 4** · **oi 9（本批真项目最高）** · 1 commit · 13,997 KB · 23 文件 · 无语言字段 · MIT · User `dabingfy-dot`（账号 2026-10-18 创建，仅 2 个公开仓库））—— **⭐⭐⭐⭐⭐ 本日最值得抄的是它把「证据先于完成声明」写成一条带反例清单的铁规**：`skills/evidence-before-done/SKILL.md` 开篇即「**没有对得上当前版本的有效证据，就不说「做好了」**」，⭐⭐⭐⭐⭐ 并给出**可执行的复用/补核判定**（「可以复用：上一回已经核过、之后没改过、没出过失败、环境没换的那部分」/「要补核：之后有改动、有过失败、换了环境的部分，只补核受影响的部分」/「不算证据：别人说好了的」），⭐⭐⭐⭐⭐ **并把「执行人自己的报告不算独立核验」写成规则本体**（「分清两种东西：执行人报告……和独立核验……前者是线索，不能当后者用」）—— **这一句直接堵住了 agent 生态里最常见的自证漏洞**；⭐⭐⭐⭐⭐ **它的「想说什么 → 要什么证据」对照表**逐行给出「够」与「不够」（「文档做好了」要「用对应软件打开，或转成图片逐页看过」而**不够**「生成成功的提示」；「电脑问题修好了」要「按原来出问题的步骤再走一遍」并**写明下一次自动改写的时间**；「已放行的发送成功了」要「在收件或目标那一端看得到」而**不够**「工具返回「成功」」；「别的助手或子任务说做完了」要「自己去看改动和成品」），⭐⭐⭐⭐⭐ **并配了两张刹车清单**（「该停一下的信号」与「常见借口 → 实际上」，后者含「我**有把握** → **有把握不等于有证据**」「就这一次 → **没有例外**」「检查工具没报错 → **没报错不等于结果对**」）；⭐⭐⭐⭐ **它对「谁该做什么」的三栏切分是本包最可复用的架构**（本包技能负责 / 宿主能力负责 / 须人做），**并明确把定时与叫醒划给宿主**（`hooks: {}`）；⭐⭐⭐⭐⭐ **它对「验证到什么程度」的诚实度是本批最高的**：README 顶部即写「**v0.9-draft，非最终发布稿**」并逐个宿主标注真实状态（Codex / WorkBuddy / DeepSeek Harness / Cursor / CodeBuddy / Kimi Work / 千问办公写「支持」，**Grok Bot 写「支持，需手动配置」**，**Claude Code 写「结构已备、走通待补，不在首发支持之列」**），且明写「**部分宿主经受阻重跑或退回修订后才通过；不代表稳定性或所有任务都能做成**……**部分宿主未保留技能加载的原始轨迹；不表示每家四个技能都逐一被调用，也不证明效果**」，⭐⭐⭐⭐⭐ **而 SKILL.md 里对应的一栏更克制**：「公开包保证的是**核对步骤可照做**。**能否降低返工率……本技能正文不下效果结论。**」；⭐⭐⭐⭐ **它还有 9 个 open issue**（本批真项目最高），说明这套技能正在被真实使用与质疑；⭐⭐⭐ **同时提供 `.claude-plugin/`、`.codex-plugin/`、`.agents/plugins/` 三套插件清单**，`NOTICE` 声明借鉴来源；⚠️ **contributors 1 人、releases 0 个、单 commit、owner 账号仅两个月大**；⚠️ **「能否降低返工率」被它自己列为「仍未证明」，本日报也未验证任何一次宿主调用**；⚠️ **13,997 KB 中含一份 17 页 PDF，本日报未打开核验其内容**
- 🎣 [Poltergeistlunagrid/Steam-Idler](projects/steam-idler.html) — **反例样本**：自称的 Steam 挂机/集卡工具，**而其仓库是一个 4 commit、5 文件、6 KB 的模板骨架**（425⭐ ⑂313（**fork/star 73.6%**）· **subs 25** · oi 0 · Python · MIT · User 账号当天新建）—— ⭐⭐⭐⭐⭐ **它的 `.gitignore` md5 `e18f025c87b71b9fe481f53ac6e8235d` 与 11-06 农场四家完全相同，`helpers.py`（97 B）md5 `8470fd5b911eacd63327be59d2562f16` 与 11-06 的 `crypto-portfolio-tracker` / `discord-quest-completer` 逐字节相同** —— ⭐⭐⭐⭐⭐ **即本日报第一次拿到跨日期的文件级模板血缘**；⭐⭐⭐⭐⭐ **它 README 末尾两处 `**⭐ Star the repo if it helped you.**` 是「subs 被投放抬高」的直接证据**；⭐⭐⭐⭐⭐ **README 的 Tech Stack 写「Node.js / C# / TypeScript / SteamKit2 / Web Dashboard」而 `language` 字段是 Python、树里没有任何 JS/TS 文件与 Steam 实现** —— **本日报记录到的第二例「宣称技术栈与实现不符」**；⭐⭐⭐⭐ **fork 间隔中位数 5.0 秒、98/99 个间隔 ≤10 秒、全部落在 10.0 分钟内**，4 个 commit 在 19 秒内完成（`Add config.py` / `Add helpers.py` / `Add README.md`）—— ⭐⭐⭐⭐⭐ **同一套投放基础设施的第三次出现**；⭐⭐⭐⭐ **`config.py` 与 11-06 `roblox-studio-mcp` 的 `config.py` 仅 docstring 一个词（`core` vs `starter`）与两个常量不同，证明模板是可参数化批量生成的**；⭐⭐⭐⭐ **它同时是一份写得很详尽的免责声明**（退款资格、2FA、Aternos、多账号）—— **合规话术与虚假实现的脱钩，是本日最值得记录的「话术包装」形态**；⚠️ **本日报未执行其代码，不主张其意图，只主张其可核验内容与 README 宣称不一致**
- 🤖 [sentinelsoldierprize/Minecraft-AFK-Bot](projects/minecraft-afk-bot.html) — **反例样本**：自称的 Minecraft 防 AFK 机器人，**而它是本日订阅数最高（35）的仓库**（425⭐ ⑂260（fork/star 61.2%）· **subs 35** · oi 0 · 5 commits · 7 KB · Python · MIT · User 账号当天新建）—— ⭐⭐⭐⭐⭐ **它与 `Steam-Idler` 共享同一份 `.gitignore`（md5 `e18f025c...`）与同一份 `helpers.py`（md5 `8470fd5b...`），构成跨日期 + 同日期的双重模板复用证据**；⭐⭐⭐⭐⭐ **它的 README 同样两处索取 star，这是本日报修正 11-07「subs 是低噪声深度信号」判据的直接触发点**；⭐⭐⭐⭐⭐ **README 的 Tech Stack 写「Node.js / Mineflayer / Express / Socket.io / Microsoft / Mojang」而仓库是 Python、无 JS/TS 文件**；⭐⭐⭐⭐ **`utils.py` 的内容是 `def build(limit): return [item * 2 for item in range(limit)]` —— 与 Minecraft 毫无关系**，`main.py` 的 `from utils import build` 在本仓库能解析但输出的是 `[0, 2, 4, ..., 18]` 即模板占位数据（11-06 的 `roblox-performance-tool` 是同一类错误的更严重级别：其 `utils.py` 根本不存在、API 返回 404）；⭐⭐⭐⭐⭐ **fork 间隔中位数 4.0 秒（本批最低）、98/99 个间隔 ≤10 秒、全部落在 9.9 分钟内**，5 个 commit 在 26 秒内完成 —— ⭐⭐⭐⭐ **它与 11-06 的 `roblox-studio-mcp` 近乎同构（fork 数 260 vs 260、fork/star 61.2% vs 61%）**；⭐⭐⭐⭐⭐ **而它的免责声明段落（服务器禁止自动化客户端、Aternos、多账号切换）详尽而专业，却与仓库内容完全脱钩**；⚠️ **本日报未执行其代码，不主张其意图**

---

"""

for rel, block in [("indexes/trend-index.md", TREND_BLOCK), ("daily-report.md", REPORT_BLOCK)]:
    p = ROOT / rel
    c = p.read_text(encoding="utf-8")
    if c.startswith("## 2026-11-08"):
        print(f"{rel}: already has a 2026-11-08 entry -- skipped")
        continue
    p.write_text(block + c, encoding="utf-8")
    print(f"{rel}: 2026-11-08 entry prepended")
