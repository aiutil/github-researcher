#!/usr/bin/env python3
"""Prepend today's (and the backfilled 2026-11-14) sections to indexes/trend-index.md
and daily-report.md. Uses python string ops to avoid patch ambiguity."""
import io
import os

BASE = "/home/lohasle/aiutil-github-researcher"
TI = os.path.join(BASE, "indexes/trend-index.md")
DR = os.path.join(BASE, "daily-report.md")

TI_NEW = """## 2026-11-15

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | 体积 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| `hikaku-io/hikaku-extension` | 283 | 1 | 0.4% | 0 | JavaScript | 12,307 KB | 10 | 工具型 |
| `opencoredev/islandcn` | 658 | 56 | 8.5% | 0 | TypeScript | 1,795 KB | 4 | 基础设施候选 |
| `faizfahmi77/ScanDot` | 532 | 5 | 0.9% | 0 | Kotlin | 151 KB | 5 | 工具型 |
| `quer3q/kraken-mount` | 321 | 27 | 8.4% | 8 | Rust | 1,602 KB | 5 | 工具型 |
| `duwqijlk/muse-protocol` | 513 | **253** | **49.3%** | 0 | Python | 32 KB | 5 | 观察型（反例样本） |
| `WarriorRemember/IPTV_Player_2.0` | 672 | 12 | 1.8% | 10 | Rust | 609 KB | 26 | 观察型（反例样本） |
| `brisk-thrush-husky/malware-defender-desktop` | 300 | 0 | 0% | 0 | C++ | 269 KB | 16 | 观察型（反例样本） |

### ⭐⭐⭐⭐⭐ 判据修正一：活跃度可以被脚本单独制造 —— 「push 频率」与「commit 数」不再是判据

`brisk-thrush-husky/malware-defender-desktop` 实测携带一个随机名 GitHub Actions 工作流：

| 项 | 实测值 |
|---|---|
| 工作流路径 | `.github/workflows/SP7LDgUHone.yml` |
| 工作流名 | `YAqWuDoGTdQ`（随机串） |
| 实现 | `actions/github-script@v7` + 43 词数组取 3 词 + 0–9999 随机数 |
| 目标文件 | `.github/f4fMKgTN95`（随机名） |
| 实测提交消息 | `optimize revert sync (5102)` / `monitor docs enhance (3709)` / `improve validate retry (4810)` |

**即「近期 push 频繁」「commit 数多」可由一个 30 行定时脚本凭空制造。**

> 新增零成本检测项：**「工作流文件名 / 工作流名是否呈随机串形态」** —— 正常项目为 `ci.yml` / `release.yml` / `pages.yml` 等有语义命名。

### ⭐⭐⭐⭐⭐ 判据修正二：体积可以被加密载荷单独撑起

`WarriorRemember/IPTV_Player_2.0` 的 26 个 blob 中，可读文本仅 4 份文档 + 5 个 954–998 B 的小 JSON，
其余为 4 个 `.enc` 加密载荷、4 个 `.dll` 二进制与 8 个 64 KB–797 KB 的不可读文件 —— **体积 5.8 MB，可读代码量为 0**。

> 新增零成本检测项：**「可读文本 blob 字节数 / 总体积」比值**（本样本 < 0.3%）。

### ⭐⭐⭐⭐⭐ 判据修正三：「subs 高」可以是纯手动订阅农场

| 仓库 | subs | star | 整棵树文件数 |
|---|---:|---:|---:|
| `DimensionRobin/rob-run-private-cheat` | **68** | 202 | **2** |
| `prismarmorergirder/wallet-security-checker` | **50** | 115 | **2** |
| `summittypeplay/sims4-updater` | 24 | 226 | **2** |
| `Crateryeexpiate/TradePilot` | 24 | 184 | **2** |
| `Beachfromgate/Wallet-Hunter` | 24 | 179 | **2** |
| `Logosheshow47/crypto-panic` | 24 | 177 | **2** |
| `Hairzenexalt/Fragment-Sniper` | 24 | 170 | **2** |

7 个 owner 账号中 **6 个创建于 2026-09-21T17:23:39Z–17:25:16Z 的 97 秒窗口内**，每个带一个随机名 + 0⭐ + 0–1 KB 的占位仓库。

> **「养号 → 占位 → 静默 54 天 → 一次性投放」四段式**。⭐⭐⭐⭐⭐ 即：**subs 必须先与「该仓库是否存在任何代码」一起看**，否则 24–68 个订阅可完全由人工点击产生。

### ⭐⭐⭐⭐⭐ 判据修正四：fork/star 高比率必须与 fork 到达分布一起读

| 仓库 | fork/star | fork 间隔中位 | ≤10 秒占比 | 抽样跨度 |
|---|---:|---:|---:|---:|
| `duwqijlk/muse-protocol` | **49.3%** | **266 秒** | **2/99（2.0%）** | 13 小时 15 分 |
| `WarriorRemember/IPTV_Player_2.0` | 1.8% | 20 秒 | 3/11（27%） | 65 分钟 |
| `AIRzZ90/study-materials-fork`（11-13 记录） | 146.2% | 139 秒 | 2/59（3.4%） | 241.7 分钟 |

**同一族比率下分布形态完全不同 —— 没有分布配套，比值不可解释。**

### ⭐⭐⭐⭐⭐ 方法论总纲：任何单点信号必须先问「能否被脚本或人工单独制造？」

| 信号 | 本日证伪情况 | 替代检测项 |
|---|---|---|
| README 全文 md5 | 跨天全变（`dd748177…` → `265eb99c…`） | **README 内外部下载链接的跨窗口聚类** |
| push 频率 / commit 数 | 可由随机词工作流制造 | 工作流文件名随机串检测 |
| 仓库体积 / blob 数 | 可由加密载荷撑起 | 可读文本字节数占比 |
| subs 数 | 可由人工点击产生 | 与「是否存在代码」一起看 |
| star 值 | 67 个不同取值，已完全失效 | 与 fork 到达分布一起看 |
| README 长度 | 与工程量完全脱钩（13 KB vs 823 B 代码） | 可执行代码字节数 |
| topic 字段 | 投放体自称 `open-source` / `developer-tools` | 不作分类依据 |

---

## 2026-11-14

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | 体积 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| `opencoredev/islandcn` | 656 | 56 | 8.5% | 0 | TypeScript | 1,795 KB | 4 | 基础设施候选 |
| `faizfahmi77/ScanDot` | 532 | 5 | 0.9% | 0 | Kotlin | 151 KB | 5 | 工具型 |
| `quer3q/kraken-mount` | 321 | 27 | 8.4% | 8 | Rust | 1,602 KB | 5 | 工具型 |
| `duwqijlk/muse-protocol` | 512 | **253** | **49.3%** | 0 | Python | 32 KB | 5 | 观察型（反例样本） |
| `ariamitchell54/cubase-studio-desktop` | 300 | 0 | 0% | 0 | C++ | 220 KB | 28 | 观察型（反例样本） |
| `Lowbydemodulator/IPTV_Player2.0` | 297 | 0 | 0% | 2 | Rust | 629 KB | 26 | 观察型（反例样本） |

### ⭐⭐⭐⭐⭐ 判据修正一：「md5 相同」首次被跨天证伪 —— 改盯载荷链接

| 族群 | 2026-11-13 窗口 md5 | 2026-11-14 窗口 md5 | README 长度变化 | 载荷链接 |
|---|---|---|---|---|
| `IPTV_Player` 族 | `dd748177e4739fee…`（92 个） | **`265eb99cc4a7d4c6…`（111 个）** | 8,771 B → 8,763 B | **完全相同** |
| `ai--manus` 族 | `26d4565b…`(139) / `a7f542a8…`(41) / `a21a6ad0…`(11) | `a21a6ad0…`（114 个） | 7,244/7,246/7,236 → 7,236 B | **完全相同** |
| `GitHub-Copilot-app` 族 | —— | `093f7cbc…`（61 个） | —— | 新增 |

**即：README 是「人读的东西、会被改写」，载荷链接是「投放者必须真花成本复制的东西」—— 跨天追踪应盯后者。**

### ⭐⭐⭐⭐⭐ 判据修正二：「软件本体」外置到 Pages 落地页，仓库退化为纯空壳

`ariamitchell54/cubase-studio-desktop` 整棵树 12 个 blob：**README 13,709 B + docs/index.html 20,755 B + banner.png 179,586 B + 3 个 C++ 桩合计 823 B**。

**实测 `https://ariamitchell54.github.io/` 返回 HTTP 404（`Site not found · GitHub Pages`）。**

**即：仓库是空壳、落地页不存在、README 承诺无对应物 —— 三者同时成立。**

### ⭐⭐⭐⭐⭐ 判据修正三：投放账号的「四段式」被完整量化

| 创建窗口 | 账号数 | 每个账号的公开仓库数 |
|---|---:|---:|
| 2026-10-02T23:48Z–23:50Z | 24 | 13 |
| **2026-10-14T00:43Z–03:03Z** | **468** | **12–17** |
| 2026-09-21T17:23Z–17:25Z（次日高订阅账号） | 6 | 2–3 + 1 个随机名占位 |

**养号 → 占位 → 静默 54 天 → 一次性投放。**

### ⭐⭐⭐⭐⭐ 判据修正四：跨仓库复用源码时，字符串常量最先被忘记

`files/main.cpp` 中硬编码 `usage: iobit-util [--version|--help]` —— **「iobit」是兄弟仓库 `iobit-driver-booster-desktop` 的产品名**；
且 `files/platform.cpp` 的 md5 `10356665038832f19a2cb56a7d1d922b` **在全部 17 个 `-desktop` 仓库中完全一致**。

**即：字节级比对非 README 文件，比 md5 比 README 更能穿透「文案逐个改写」的防线。**

---

"""

DR_NEW = """## 2026-11-15
**核心主题：** 本日最值得记的判据修正，是把「投放体」从一个**静态形态**升级成一个**可运行的自动化流水线** —— ⭐⭐⭐⭐⭐ 在 `created:2026-11-14` 的 300 个候选里，**286 个（95.3%）共享同一批 README 全文 md5**，被拆成三个族群（`ai--manus2.0` 114 个 / `IPTV_Player_2.0` 111 个 / `GitHub-Copilot-app` 61 个），且**每个族群内部的所有仓库都指向同一条 Dropbox 链接**（`ManusStudio2.0.rar`、`IPTVPlayer2.0.rar`、`GitHub_Copilot_app.rar`）—— ⭐⭐⭐⭐⭐ **即「md5 相同」这一判据在本日被证伪了一半：真正稳定的指纹不是 README 的字节，而是 README 里那一条下载链接**。⭐⭐⭐⭐⭐ 而与这三族同框的 `-desktop` 族（本日 5 个）**暴露了更硬的一层：它们的「活跃度」是自动生成的** —— 每个仓库都有一个随机名的 GitHub Actions 工作流（`SP7LDgUHone.yml` / `mmZDs9dJzawUKR.yml` / `hi6b2Xefut.yml` / `F1fAks7Y8Hdu0.yml` / `J5zzALI4By.yml`），工作流名是随机串（`YAqWuDoGTdQ` / `P015SrpLujreU` …），内容是 `actions/github-script@v7` 里一段**随机词组合 + 随机数**的提交消息生成器，往 `.github/<随机名>` 文件里追加一行时间戳；⭐⭐⭐⭐⭐ **实测该仓库的提交历史是 `optimize revert sync (5102)` / `monitor docs enhance (3709)` / `improve validate retry (4810)`，时间戳每次都变** —— ⭐⭐⭐⭐⭐ **即「push 频率」与「commit 数量」这两个最常用的活跃度判据，在本日被证实可以由一个 30 行的定时脚本凭空制造**。⭐⭐⭐⭐⭐ 与之并列的第三个发现是**一批「零代码但高订阅」的仓库**：本日 7 个仓库（`rob-run-private-cheat` 68 subs / `wallet-security-checker` 50 subs / `sims4-updater` 24 / `TradePilot` 24 / `Wallet-Hunter` 24 / `crypto-panic` 24 / `Fragment-Sniper` 24）**整棵树只有 `LICENSE` + `README.md` 两个文件、0 个代码文件**，⭐⭐⭐⭐⭐ 而它们的 **7 个 owner 账号中有 6 个创建于 2026-09-21T17:23:39Z–17:25:16Z 的 97 秒窗口内**、每个账号各有一个随机名 + 0⭐ + ~1KB 的占位仓库 —— **即「subs 高」在本日第一次被证明可以是纯订阅农场的手动产物，且它与「star 高」完全正交**。⭐⭐⭐⭐⭐ 而与这三批同框的四个真项目，恰好给出四种**互不重叠**的诚实形态：`hikaku-io/hikaku-extension`（283⭐ · 87 files · Apache-2.0 · v0.1.0）**把模型的真实失败率直接写进文档**（Reddit 弱标签基准：AI 图捕获 65%、真图误报 6%、AI 视频仅捕获 22%），并用 `docs/ARCHITECTURE.md` + `docs/MODELS.md` 把「声明（declaration）」与「模型估计（estimate）」在数据结构上分开；`opencoredev/islandcn`（658⭐ · 310 blobs · 组织账号 · MIT）**把 `AGENTS.md` 写成给 coding agent 的合同**，并用 `/r/island-core.json` 这个 shadcn registry 端点分发引擎；`faizfahmi77/ScanDot`（532⭐ · 55 files · v0.3.0-preview.1）**在 README 第二段就用加粗声明「The Android app does not reconstruct ordinary video with photogrammetry on the phone」**，并同时给出「手机端 ARCore 深度」与「工作站端 COLMAP」两条互不混淆的路径；`quer3q/kraken-mount`（321⭐ · 19 open issues · GPL-3.0）**用 `DESIGN.md` 明确写出「支持的来源只有三种」并逐条列出「不支持什么」**。⭐⭐⭐⭐⭐ **本日报据此给出本日最重要的判据修正：11-13 记录的「仓库名可被伪装」和 11-08 记录的「账号注册聚集度」都只描述了投放体的「静态指纹」，而本日证实投放体已经具备「运行时」—— 即任何基于 README 文本、commit 数量、push 频率、subs 数量的单点判据，都必须先问「这个信号能否被一个自动化脚本单独制造？」**

**证据边界：** 本日全部元数据取自 **2026-11-15 CST**（2026-11-14T22:00Z–22:20Z 窗口）经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `search/repositories`（`created:2026-11-14 stars:>=30`，`total_count` = **300**）、`repos/{owner}/{repo}`、`git/trees/{branch}?recursive=1`、`commits`、`forks?sort=newest&per_page=100`、`releases`、`tags`、`readme`、`contents/{path}`（`Accept: application/vnd.github.raw`）、`users/{owner}`、`users/{owner}/repos`、`actions/workflows`、`license`。⭐⭐⭐ **⚠️ 本日报未下载、未执行、未运行任何被投放的载荷。** 对三条 Dropbox 链接**只提取了 URL 字符串，未发起任何请求**；对 GitHub Pages 落地页只做了一次 HTTP GET，记录状态码 **404** 与响应体首行 `Site not found · GitHub Pages`。⭐⭐⭐ **⚠️ `stargazers` 与 `subscribers` 端点在本窗口对本 token 返回 404**（对 `torvalds/linux` 等公共仓库亦然），故**未对 star / subscriber 的账号做逐个取证**。⭐⭐⭐ **⚠️ star 增速未做统计**，所有 ⭐ 数均为快照绝对值。⭐⭐⭐ **⚠️ `git pull --ff-only origin main` 在本次任务中持续失败**（`gnutls_handshake() failed`，重试 3 次并尝试 `http.sslCAInfo` 与 `http.version=HTTP/1.1` 均失败），本仓库 git smart-HTTP 通道在本次任务期间不可达；所有 API 取证均通过 `api.github.com` 完成，未受影响。⭐⭐⭐ **⚠️ 未核验项**：`hikaku-extension` 的任何实际检测结果与其基准数据的可复现性、`islandcn` 的构建与动画保真度、`ScanDot` 在真机上的点云质量、`kraken-mount` 在 PS5 上的实际挂载行为、`muse-protocol` 协议细节在 muse.ai 当前的可用性、三个 Dropbox 载荷的实际内容、加密 `.enc`/`.dll` 文件的用途。

**关键项目：**
- 🔍 [hikaku-io/hikaku-extension](projects/hikaku-extension.html) — 浏览器本地标记 AI 生成图像/视频的 Manifest V3 扩展，**把模型真实失败率写进 `docs/MODELS.md`**（Reddit 弱标签：AI 图捕获 65%、真图误报 6%、AI 视频仅 22%），并把「声明」与「估计」做成两条独立路径
- 🏝️ [opencoredev/islandcn](projects/islandcn.html) — React 的 Dynamic Island 引擎，**`AGENTS.md` 写成给 coding agent 的路径归属合同**，用 shadcn registry 端点分发
- 📐 [faizfahmi77/ScanDot](projects/scandot.html) — Android ARCore 点云采集器，**README 第二段即声明手机端不做摄影测量重建**
- 🗄️ [quer3q/kraken-mount](projects/kraken-mount.html) — PS5 ELF payload，**`DESIGN.md` 节标题「Supported sources (nothing else)」**，供应链写「拉官方 release + SHA256SUMS + build.sh 校验」
- 🧪 [duwqijlk/muse-protocol](projects/muse-protocol.html) — **反例样本**：fork/star 49.3% 但 fork 间隔中位 266 秒（正常分布）；README 首行即给出「用 JP 节点、不绑卡」的规避用法
- ⏱️ [brisk-thrush-husky/malware-defender-desktop](projects/malware-defender-desktop.html) — **反例样本**：活跃度全部由随机名 GitHub Actions 工作流制造；16/17 个兄弟仓库共享逐字节相同的 C++ 文件
- 📺 [WarriorRemember/IPTV_Player_2.0](projects/iptv-player-2-0.html) — **反例样本**：111 个 README 逐字节相同的仓库共用同一条 Dropbox 链接；体积由加密载荷撑起而可读代码为 0

---

## 2026-11-14
**核心主题：** ⭐⭐⭐⭐⭐ 本日的核心发现在于**投放体的「可复制性」第一次被证明是可以跨天复用的基础设施，而不是当天现造的仓库名** —— ⭐⭐⭐⭐⭐ 在 `created:2026-11-13` 的 300 个候选里，**283 个（94.3%）共享四个 README 全文 md5**，分属 `ai--manus`（139 + 41 + 11 = 191 个）与 `IPTV_Player2.0`（92 个）两个族群；⭐⭐⭐⭐⭐ **而这四个 md5 在 2026-11-14 窗口全部换成了新值（`a21a6ad0…` / `265eb99c…` / `093f7cbc…`）** —— ⭐⭐⭐⭐⭐ **即「md5 相同」这个判据在本日第一次被跨天证伪，而三条 Dropbox 载荷链接（`ManusStudio2.0.rar` / `IPTVPlayer2.0.rar` / `GitHub_Copilot_app.rar`）一字未变**。⭐⭐⭐⭐⭐ 与这两族同框的第三个发现是**「-desktop」族把「软件本体」彻底搬到了 GitHub Pages 落地页上**：`ariamitchell54/cubase-studio-desktop` 的整棵树只有 12 个文件（README 13,709 B + LICENSE + 3 个 9 行的 C++ 桩 + 179,586 B 的 `banner.png` + 2 个 SVG + 20,755 B 的 `docs/index.html` + 1 个随机名工作流 + 1 个 155 B 的随机名 stamp 文件），⭐⭐⭐⭐⭐ **其 `docs/index.html` 落地页实测在快照时刻返回 HTTP 404（`Site not found · GitHub Pages`）** —— ⭐⭐⭐⭐⭐ **即仓库是空壳，落地页不存在，而 README 却写着一整套「离线自包含部署包」的承诺。** ⭐⭐⭐⭐⭐ 与这三批同框的四个真项目给出四种**互不重叠**的诚实形态：`opencoredev/islandcn`（656⭐ · 组织账号 · 310 blobs · MIT）**把 `AGENTS.md` 写成一份给 coding agent 的路径归属与许可归属合同**；`faizfahmi77/ScanDot`（532⭐ · 55 files）**在 README 第二段就用加粗声明「The Android app does not reconstruct ordinary video with photogrammetry on the phone」**；`quer3q/kraken-mount`（321⭐ · **oi 19** · GPL-3.0）**用 `DESIGN.md` 的节标题「Supported sources (nothing else)」把非目标写死**，并把「不自行构建 ampr-emu-ng，而是拉官方 release 并校验 `SHA256SUMS`」写进供应链边界；`duwqijlk/muse-protocol`（512⭐ · ⑂253 = **fork/star 49.3%**）⭐⭐⭐⭐⭐ **其 fork 到达间隔中位 266 秒、仅 2/99 个 ≤10 秒 —— 远慢于同日投放体的 20–24 秒，是本日报记录的第一个「fork/star 高但 fork 分布正常」的反例样本**。⭐⭐⭐⭐⭐ **本日报据此给出本日最重要的判据修正：投放体的 README 是「给人看的、会被改写的」，而载荷链接是「投放者必须真花成本才能复制的」—— 因此跨天追踪应当盯载荷链接，而不是 README 文本。**

**证据边界：** 本日全部元数据取自 **2026-11-15 CST**（2026-11-14T22:00Z–22:30Z 窗口）经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `search/repositories`（`created:2026-11-13 stars:>=30`，`total_count` = **300**）、`repos/{owner}/{repo}`、`git/trees/{branch}?recursive=1`、`commits`、`forks?sort=newest&per_page=100`、`releases`、`tags`、`readme`、`contents/{path}`、`users/{owner}`、`users/{owner}/repos`、`actions/workflows`、`license`。⭐⭐⭐ **⚠️ 本日报为补齐缺失日期而回溯生成**（`daily/2026-11-14.md` 在本次任务开始时不存在），因此其快照时刻是 **2026-11-15 CST** 而非 2026-11-14 当日；⭐⭐⭐ **所有 ⭐ 数为快照绝对值，不反映 2026-11-14 当日的数值。** ⭐⭐⭐ **⚠️ 本日报未下载、未执行、未运行任何被投放的载荷**；⭐⭐⭐ 对 GitHub Pages 落地页只做了一次 HTTP GET（404）。⭐⭐⭐ **⚠️ `stargazers` 与 `subscribers` 端点返回 404**，未对 star / subscriber 账号逐个取证。⭐⭐⭐ **⚠️ star 增速未做统计。** ⭐⭐⭐ **⚠️ 未核验项**：`islandcn` 的构建与动画保真度、`ScanDot` 在真机上的点云质量、`kraken-mount` 在 PS5 上的实际挂载行为与其 `vendor/ampr-emu-ng/` 目录、`muse-protocol` 协议细节在 muse.ai 当前的可用性、三个 Dropbox 载荷的实际内容、`cubase-studio-desktop` 等 12 个 `-desktop` 仓库的落地页是否全部 404。

**关键项目：**
- 🏝️ [opencoredev/islandcn](projects/islandcn.html) — React 的 Dynamic Island 引擎，**`AGENTS.md` 写成给 coding agent 的路径归属与许可归属合同**
- 📐 [faizfahmi77/ScanDot](projects/scandot.html) — Android ARCore 点云采集器，**README 第二段即声明手机端不做摄影测量重建**
- 🗄️ [quer3q/kraken-mount](projects/kraken-mount.html) — PS5 ELF payload，**`DESIGN.md` 节标题「Supported sources (nothing else)」**
- 🧪 [duwqijlk/muse-protocol](projects/muse-protocol.html) — **反例样本**：fork/star 49.3% 但 fork 分布正常
- 📦 [ariamitchell54/cubase-studio-desktop](projects/cubase-studio-desktop.html) — **反例样本**：3 个 9 行 C++ 桩 + 实测 404 的落地页
- 📺 [Lowbydemodulator/IPTV_Player2.0](projects/iptv-player2-0.html) — **反例样本**：92 个同 md5 副本，与次日 111 个共用同一 Dropbox 载荷链接

---

"""


def prepend(path, block):
    with io.open(path, encoding="utf-8") as f:
        cur = f.read()
    if block.split("## ", 1)[1].split("\n", 1)[0] in cur[:4000]:
        print(f"SKIP (already present): {path}")
        return
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(block + cur)
    print(f"prepended -> {path}")


prepend(TI, TI_NEW)
prepend(DR, DR_NEW)
