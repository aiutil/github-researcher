#!/usr/bin/env python3
"""Prepend today's (2026-11-16) sections to indexes/trend-index.md and
daily-report.md. Uses python string ops to avoid patch ambiguity."""
import io
import os

BASE = "/home/lohasle/aiutil-github-researcher"
TI = os.path.join(BASE, "indexes/trend-index.md")
DR = os.path.join(BASE, "daily-report.md")

TI_NEW = """## 2026-11-16

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | 体积 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| `WindGatorRise37/Gemini-Config-Checker-` | 473 | 0 | 0% | 3 | Go | 181 KB | 53 | 观察型（反例样本） |
| `atlas7283/steam-library-bridge` | 176 | 0 | 0% | **19** | JavaScript | 0 KB | **1** | 观察型（反例样本） |
| `tsukumijima/pydtcpip` | 44 | 5 | 11.6% | 1 | Python | 258 KB | 6 | 生产可用 |
| `petekp/coordinator` | 34 | 3 | 8.8% | 0 | Python | 894 KB | 26 | 工具型 |
| `cnrad/interspace` | 131 | 7 | 5.3% | 0 | Swift | 17,768 KB | 5 | 工具型 |
| `lishuangqiang/mixbar` | 79 | 1 | 1.3% | 0 | Swift | 2,178 KB | 4 | 工具型 |
| `rauchg/winamp-ui-sdk` | 42 | 2 | 4.8% | 0 | TypeScript | 15,385 KB | 2 | 观察型 |
| `huangserva/h3-fight` | 30 | **14** | **46.7%** | 0 | Python | 8,902 KB | 2 | 工具型 |
| `Dart-veider01/TradingAgents-crypto` | 140 | **64** | **45.7%** | 0 | Python | 6,984 KB | 4 | 观察型 |

### ⭐⭐⭐⭐⭐ 判据修正一：镜像检测从「上游是否清空」转向「blob sha 是否相同」

`Gemini-Config-Checker-` 族的 21 个仓库（各 473⭐）逐字节复制了**健在**的上游 `MatinSenPai/Gemini-Config-Checker`（144⭐ · MIT · 2026-10-03 创建 · 72 blobs）。

| 探针文件 | 覆盖仓库 | 不同 md5 数 | GitHub blob sha |
|---|---:|---:|---|
| `internal/scan/scan_test.go` | 21 | **1** | `585365eec6394fc0d3e5f85815add761051ad664` |
| `internal/scan/region.go` | 21 | **1** | — |
| `internal/ui/ui.go` | 21 | **1** | — |
| `dns_android.go` | 21 | **1** | — |
| `Makefile` | 21 | **1** | `88c61e0e666782968392de1f5c96a5c2cf43f0d6` |
| `go.mod` | 21 | **1** | `0985644d9817804ca6331193ff7a002ab859aeaf` |
| `VERSION` | 21 | **1** | — |

**但许可被改掉（上游 `MIT License` → 镜像 `Apache License`）、载荷被改掉（上游无 Dropbox 链接 → 21 个镜像统一指向 `…/GeminiConfigChecker.rar?rlkey=dv7oxsttd2j8kvr5zu7uyx1tm`）、53 个 commit 的消息序列逐条复制（`identical message sequence = True`，仅时间戳不同）。**

> 新增零成本检测项：**「同族仓库的 blob sha 是否与上游逐一相同」** —— 无需下载任何内容。

> **与 11-13 的 `AIRzZ90/study-materials-fork` 的区别**：那次是「上游被作者清空后的镜像」（镜像方没有选择）；**本次是「上游健在时的镜像」（镜像方主动选择复制 21 份、改许可、换载荷）。**

### ⭐⭐⭐⭐⭐ 判据修正二：「账号注册聚集度」升级为「账号 × 家族矩阵」

21 个 Gemini 镜像的 owner 账号实测注册窗口 `2026-10-14T01:07:31Z–03:02:24Z`（跨度 **6,893 秒**），**全部 0 followers、全部恰好 12 个公开仓库**。

| 账号 | 注册时间 | GitHub-Copilot-app | ai--manus2.0 | Gemini-Config-Checker- |
|---|---|---:|---:|---:|
| `TypeTyrantScheme` | 01:07:31Z | 10 | 0 | 1 |
| `VortexHostFeel` | 01:15:10Z | 9 | 1 | 1 |
| `Visionbeyondtrack` | 01:41:16Z | 0 | **10** | 1 |
| `WindGatorRise37` | 02:04:33Z | 10 | 0 | 1 |
| `Violetnyudress` | 03:02:13Z | 10 | 0 | 1 |
| `wisemeadowlarkspike` | 03:02:24Z | 10 | 0 | 1 |
| **（其余 15 个账号同构）** | 01:15Z–03:02Z | 9–10 | 0–10 | 1 |

**注册窗口完全落在 11-14 记录的 `2026-10-14T00:43Z–03:03Z` 账号队列内部 —— 即同一批账号在 11-14 投放两个家族，在 11-15 投放第三个家族，且每个账号每个家族各持 9–10 个副本 + 1 个主仓库 + 1 个随机名占位 = 恰好 12 个。**

> 新增零成本检测项：**「同一个账号是否在多个毫无词法关系的家族里各持 9–10 个副本」** —— `users/{owner}/repos` 一次请求即可取全，**不受账号闲置时间影响，也不受命名词根相似性影响**。

### ⭐⭐⭐⭐⭐ 判据修正三：「release 数量 / 版本号」不能当发布历史的证据

`atlas7283/steam-library-bridge`（176⭐ · 19 subs · 572 blobs · **1 个 commit**）：

| tag | `created_at` | `published_at` | assets |
|---|---|---|---:|
| `v1.2.8` | 2026-11-15T21:11:41Z | 21:11:48Z | 2 |
| `v2.3.2` | 2026-11-15T21:11:41Z | 21:11:54Z | 2 |
| `v3.1.6` | 2026-11-15T21:11:41Z | 21:11:59Z | 2 |
| `v4.4.2` | 2026-11-15T21:11:41Z | 21:12:02Z | 2 |

**四个 release 的 `created_at` 完全相同（= 唯一那次 commit 的时间），`published_at` 依次 +7s / +13s / +18s / +21s；四个版本号的次版本号互不相同且与代码无关。**

> 新增零成本检测项：**「仓库 `size` 字段为 0 但 `git/trees` 非空」** —— 本样本 `size = 0 KB` 而树内含 `Steam-Library-Bridge.exe` **1,050,048 B** 与 312 个 `third_party/` blob。

> **发布史真伪的三项配套核验**：① release 资产的 sha256 是否随版本变化；② tag 是否指向不同 commit；③ 代码在版本之间是否实质改动。

### ⭐⭐⭐⭐⭐ 判据修正四：许可判据从 `license.spdx_id` 字段转向 LICENSE 文件内容 + 第三方声明文件

| 仓库 | `license.spdx_id` | LICENSE 实际内容 |
|---|---|---|
| `cnrad/interspace` | **NOASSERTION** | `MIT License` / `Copyright (c) 2026 cnrad` |
| `lishuangqiang/mixbar` | MIT | MIT + **`THIRD_PARTY_NOTICES.md`** |

**`mixbar` 的 `THIRD_PARTY_NOTICES.md` 精确到借用代码的 commit hash：**

> - 项目：https://github.com/burghr/MacMixer
> - 参考提交：**`3b2c69015949786b02462281420bb6eb75488434`**
> - 引用范围：**`CoreAudioSupport.swift` 中的 Core Audio 属性读取、设备枚举和应用进程识别辅助逻辑**
> - 原始作者：burghr

> 新增零成本检测项：**「仓库是否有第三方声明文件，且是否精确到 commit hash」** —— 本数据集里第一次见到这种写法。

### ⭐⭐⭐⭐⭐ 判据修正五：仓库体积必须先做构成分析

`rauchg/winamp-ui-sdk` 共 15,385 KB，其中 **5 个 mp3 音轨占 15,373,046 B（98%）**，实际 TypeScript 代码只有 5 个文件共 158,566 B。⭐⭐⭐⭐⭐ **「体积大」不等于「工程量大」** —— 这与 11-10 的 `Shape`（2,180 blobs 但 1 个 commit）是「体积」判据的两种不同失效方式。

---

"""

DR_NEW = """## 2026-11-16
**核心主题：** 本日最值得记的判据修正，是**投放体第一次被证明会「认领」一个真实上游** —— ⭐⭐⭐⭐⭐ `Gemini-Config-Checker-` 族的 **21 个仓库（每个 473⭐、同一个 README md5 `9dca10b4fa20…`、同一条 Dropbox 链接 `GeminiConfigChecker.rar`）逐字节复制了真实存在的上游 `MatinSenPai/Gemini-Config-Checker`（144⭐ · MIT · 2026-10-03 创建 · 72 blobs · owner 1,845 followers）的目录结构与代码**：⭐⭐⭐⭐⭐ 实测 `internal/scan/scan_test.go` / `internal/scan/region.go` / `internal/ui/ui.go` / `dns_android.go` / `Makefile` / `go.mod` / `VERSION` **七个文件在 21 个仓库中各自只有 1 个 md5，GitHub 的 blob sha 也完全相同（`585365ee…` / `88c61e0e…` / `0985644d…`）** —— ⭐⭐⭐⭐⭐ **但改掉了许可（上游 LICENSE 首行 `MIT License`，镜像首行 `Apache License` / `license.spdx_id` = Apache-2.0）、改掉了载荷（上游 README 实测无 Dropbox 链接，21 个镜像统一指向 `…/GeminiConfigChecker.rar?rlkey=dv7oxsttd2j8kvr5zu7uyx1tm`）、并把 53 个 commit 的消息序列逐条复制**（`Create main.go` / `Create internal/ui/ui.go` / `Create internal/scan/scan_test.go` …，**`identical message sequence = True`**，仅时间戳不同）。⭐⭐⭐⭐⭐ **即「镜像」在本日不再是「上游清空后的产物」（11-13 的 `AIRzZ90/study-materials-fork`），而是「上游健在、镜像方主动改许可换载荷并批量复制 star」** —— ⭐⭐⭐⭐⭐ **这让 11-13 的判据「`parent=null` 只能证明不是 GitHub 的 fork 关系」升级为可操作的检测法：把同族仓库的 blob sha 逐个比对上游，无需下载任何内容。**⭐⭐⭐⭐⭐ 与之并列的第二个发现是**「账号注册聚集度」应升级为「账号 × 家族矩阵」**：⭐⭐⭐⭐⭐ 本族 21 个 owner 账号实测注册于 `2026-10-14T01:07:31Z–03:02:24Z` 的 **6,893 秒**窗口内，**全部 0 followers、全部恰好 12 个公开仓库**，⭐⭐⭐⭐⭐ **且其中 10 个账号同时持有 `GitHub-Copilot-app` 族的 9–10 个副本、另 4 个持有 `ai--manus2.0` 族的 9–10 个副本** —— ⭐⭐⭐⭐⭐ **即同一个账号队列在 11-14 投放两个家族、在 11-15 投放第三个家族**；⭐⭐⭐⭐⭐ **判据因此从「这些账号是否同批注册」改为「同一个账号是否在多个毫无词法关系的家族里各持 9–10 个副本」—— 后者不受账号闲置时间影响，也不受命名词根相似性影响。**⭐⭐⭐⭐⭐ 第三个发现是**「release 数量」与「版本语义」可以同时被凭空制造**：`atlas7283/steam-library-bridge`（176⭐ · 19 subs · 572 blobs · **1 个 commit**）**在 21:11:41Z 一次提交后 7 秒内连发 4 个 release（v1.2.8 → v2.3.2 → v3.1.6 → v4.4.2，发布间隔各 4–7 秒、每个带 2 个 asset），四个版本号的次版本号互不相同且与代码无关；owner 账号创建于 2026-11-03（仅 12 天）、0 followers、仅 1 个公开仓库；仓库 `size` 字段实测 0 KB 而树内含 1,050,048 B 的 `.exe`** —— ⭐⭐⭐⭐⭐ **即「release 多 / 版本号多」不是发布历史的证据，除非同时核对 release 资产与代码是否随版本演进。**⭐⭐⭐⭐⭐ 第四个发现是**一批真项目用同一套语言给出了三种不同的诚实边界**：`tsukumijima/pydtcpip`（44⭐ · **9 个 open issue 全部是来自 6 位不同用户的真机兼容性报告** · 57 blobs · MIT · owner 2018 年创建、140 repos、462 followers）**把「我们从未实现过」写进 `AGENTS.md`**（不实现 recorder scheduling / 手机端专有下载准备 / remote access / Enhanced Full Authentication / PCP2 / playback distribution 的 DTCP Source），并用 `Verified` / `Unverified (profile implemented)` / `Not applicable` 三档标注每台设备；`petekp/coordinator`（34⭐ · 26 commits · MIT）**把「token 预算」做成 pre-commit hook 可读的文件**（`.token-ceilings`：`herdr/RECIPE.md 6500` / `herdr/mods/coordinator-agents/main.js 9000`，规则 `tokens = bytes / 4`，默认上限 5,000）；`cnrad/interspace`（131⭐ · Swift）**把「自更新只装签名相同且版本更新的包，否则什么也不做」写进 README**。⭐⭐⭐⭐⭐ **本日报据此修正 11-15 的一条判据：「许可」不是 `license.spdx_id` 字段，而是 LICENSE 文件的实际内容 + 仓库内第三方声明文件 —— `lishuangqiang/mixbar` 的 `THIRD_PARTY_NOTICES.md` 精确到引用了 `burghr/MacMixer` 的具体 commit `3b2c69015949786b02462281420bb6eb75488434` 与引用范围**，⭐⭐⭐⭐⭐ **这是本数据集里第一次见到把「借了谁的哪一段代码」的 commit hash 写进产物。**

**证据边界：** 本日全部元数据取自 **2026-11-16 CST**（2026-11-15T22:00Z–22:40Z 窗口）经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `search/repositories`（`created:2026-11-15 stars:>=30`，`total_count` = **105**）、`repos/{owner}/{repo}`、`git/trees/{branch}?recursive=1`、`commits`、`forks?sort=newest&per_page=100`、`releases`、`tags`、`readme`、`contents/{path}`（`Accept: application/vnd.github.raw`）、`users/{owner}`、`users/{owner}/repos`、`actions/workflows`、`license`。⭐⭐⭐ **⚠️ 本日报未下载、未执行、未运行任何被投放的载荷。** 对 `GeminiConfigChecker.rar` 的 Dropbox 链接**只提取 URL 字符串，未发起任何请求**；对 `Steam-Library-Bridge.exe`（1,050,048 B）**只读取 tree 中的 blob 元数据（路径与大小），未下载、未反汇编、未运行**。⭐⭐⭐ **⚠️ `stargazers` 与 `subscribers` 端点在本窗口未用于逐个取证**，⭐⭐⭐ 因此**「21 个镜像的 473⭐ 是刷的」这一结论本日报不作主张** —— 只记录「21 个副本的 star 取值完全相同（distinct = 1），且真实上游只有 144⭐」这一可核验事实。⭐⭐⭐ **⚠️ 「镜像方未经授权」是推断，不是取证结论** —— 未取得上游作者的授权状态证明，未核验是否存在私下协议，**未做上游 ↔ 镜像的完整文件级 diff**（上游 72 blobs vs 镜像 53 blobs，目录不完全一致）。⭐⭐⭐ **⚠️ star 增速未做统计**，所有 ⭐ 数均为快照绝对值。⭐⭐⭐ **⚠️ 本日的 `git pull --ff-only origin main` 在默认代理配置下持续失败**（`gnutls_handshake() failed`，重试 3 次并尝试 `http.sslCAInfo` 均失败），**最终以 `git -c http.proxy= -c https.proxy= pull` 绕过本机 127.0.0.1:7890 代理成功**；本次任务中所有 `git push` 也使用同一绕过方式。⭐⭐⭐ **⚠️ 未核验项**：`pydtcpip` 在真实设备上的任何行为、其 PyPI 包内容、9 个 issue 的正文、`coordinator` 的 pre-commit hook 本体、`interspace` 的实际动画与签名逻辑、`mixbar` 的 Core Audio Process Tap 实现、`winamp-ui-sdk` 的 WebMCP agent 控制与音频实现、`h3-fight` 的出片效果与素材原始授权、`TradingAgents-crypto` 的 bytx 下单链路、`steam-library-bridge` 的 4 个 release 的 8 个 asset 是否内容相同。

**关键项目：**
- 🪞 [WindGatorRise37/Gemini-Config-Checker-](projects/gemini-config-checker.html) — **反例样本**：21 个副本各 473⭐，逐字节复制**健在**的上游（blob sha 完全相同），但改许可 MIT→Apache-2.0、改载荷为同一条 Dropbox 链接、复刻 53 条 commit 消息
- 🎮 [atlas7283/steam-library-bridge](projects/steam-library-bridge.html) — **反例样本**：1 个 commit 后 7 秒内连发 4 个语义无关版本号；账号 12 天大、0 followers、仅 1 个仓库；`size` 字段 0 KB 但树内含 1.05 MB 的 `.exe`
- 📺 [tsukumijima/pydtcpip](projects/pydtcpip.html) — DTCP-IP + DLNA/UPnP 的非官方 asyncio 实现，**9 个 open issue 全是 6 位用户的真机兼容性报告**，把「我们从未实现过」写进 `AGENTS.md`
- 🧭 [petekp/coordinator](projects/coordinator.html) — 多 agent 舰队调度器，**`.token-ceilings` 把 token 预算做成 pre-commit 可读清单**（`tokens = bytes / 4`），四条件才升级提问
- 🪟 [cnrad/interspace](projects/interspace.html) — macOS 空间切换器，**自更新只装签名相同且版本更新的包，否则什么也不做**；`license.spdx_id` 是 NOASSERTION 但 LICENSE 实为 MIT
- 🎚️ [lishuangqiang/mixbar](projects/mixbar.html) — Core Audio Process Tap 分应用音量器，**`THIRD_PARTY_NOTICES.md` 精确到借用代码的 commit hash**，随 App 分发
- 🎵 [rauchg/winamp-ui-sdk](projects/winamp-ui-sdk.html) — UI SDK 的 Web Components showcase，**98% 的体积是 5 首 mp3 而非代码**
- 🥋 [huangserva/h3-fight](projects/h3-fight.html) — H3 打戏提示词库 + 检查器，**188 个镜头块 + 去重/自检脚本 + 三层来源溯源**，代码 MIT / 库 CC BY-NC
- 📈 [Dart-veider01/TradingAgents-crypto](projects/tradingagents-crypto.html) — **fork 披露的正面范本**：恢复上游许可与 README、8 语言说明差异、**执行器默认关闭且默认走 demo**

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
