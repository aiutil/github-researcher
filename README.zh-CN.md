# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-11-16.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-11-16

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 9 | 825 | 5 | 126k+ |

**今日核心判断：** 本日最硬的发现是**投放体第一次被证明会「认领」一个真实上游** —— ⭐⭐⭐⭐⭐ `Gemini-Config-Checker-` 族的 21 个仓库（每个 473⭐、同一个 README md5 `9dca10b4fa20…`、同一条 Dropbox 链接 `GeminiConfigChecker.rar`）**逐字节复制了真实存在的上游 `MatinSenPai/Gemini-Config-Checker`（144⭐ · MIT · 2026-10-03 创建 · 72 blobs）的目录结构与代码**，⭐⭐⭐⭐⭐ 实测 `internal/scan/scan_test.go` / `internal/scan/region.go` / `internal/ui/ui.go` / `dns_android.go` / `Makefile` / `go.mod` / `VERSION` **七个文件在 21 个仓库中各自只有 1 个 md5（blob sha 也完全相同：`585365ee…` / `88c61e0e…` / `0985644d…`）** —— ⭐⭐⭐⭐⭐ **但改掉了许可（MIT → Apache-2.0）、改掉了载荷（上游无 Dropbox 链接，镜像统一指向 `GeminiConfigChecker.rar`）、并把 53 个 commit 的消息序列**逐条复制**（`Create main.go` / `Create internal/ui/ui.go` / `Create internal/scan/scan_test.go` …，仅时间戳不同）**。⭐⭐⭐⭐⭐ 即「镜像」在本日不再是「上游清空后的产物」（11-13 记录的 `AIRzZ90/study-materials-fork`），而是「**上游健在、镜像方主动改许可换载荷并批量复制 star**」** —— 这让 11-13 的判据「`parent=null` 只能证明不是 GitHub 的 fork 关系」升级为可操作的检测法：把同族仓库的 blob sha 逐个比对上游，即可判定是否镜像。⭐⭐⭐⭐⭐ 而与该族同框的 21 个 owner 账号**恰恰是 11-14 记录的 `2026-10-14T00:43Z–03:03Z` 那 468 个账号队列的一部分**（本族实测窗口 `2026-10-14T01:07:31Z–03:02:24Z`，跨度 6,893 秒，21 个账号**全部 0 followers、全部恰好 12 个公开仓库**），⭐⭐⭐⭐⭐ **且其中 10 个账号同时持有 `GitHub-Copilot-app` 族的 9–10 个副本、另 4 个持有 `ai--manus2.0` 族的 9–10 个副本** —— **即同一个账号队列在 11-14 投放 `GitHub-Copilot-app` / `ai--manus2.0`，在 11-15 同一时刻投放第三个家族 `Gemini-Config-Checker-`**，⭐⭐⭐⭐⭐ **本日报据此给出本日最重要的判据修正：「账号注册聚集度」应升级为「账号 × 家族矩阵」—— 判据不再是「这些账号是否同批注册」，而是「同一个账号是否在多个家族里各持 N–10 个副本」**。⭐⭐⭐⭐⭐ 与之并列的第二个发现是**「release 数量」与「版本语义」可以同时被凭空制造**：`atlas7283/steam-library-bridge`（176⭐ · 19 subs · 572 blobs · 1 个 commit）**在 21:11:41Z 一次提交后 7 秒内连发 4 个 release（v1.2.8 → v2.3.2 → v3.1.6 → v4.4.2，发布间隔各 4–7 秒），每个 release 带 2 个 asset**，⭐⭐⭐⭐⭐ 而**四个版本号的次版本号互不相同且与代码无关**（4.4.2 / 3.1.6 / 2.3.2 / 1.2.8），⭐⭐⭐⭐⭐ **owner 账号 `atlas7283` 创建于 2026-11-03（仅 12 天）、0 followers、仅 1 个公开仓库、仓库 `size` 字段实测 0 KB 但树内有 1,050,048 B 的 `Steam-Library-Bridge.exe`** —— ⭐⭐⭐⭐⭐ **即「release 多 / 版本号多」不是发布历史的证据，除非同时核对 release 资产与代码是否随版本演进。**⭐⭐⭐⭐⭐ 第三个发现是**一批真项目用同一套语言给出了三种不同的诚实边界**：`tsukumijima/pydtcpip`（44⭐ · **9 open issues 全是来自 6 位不同用户的真机兼容性报告** · 57 blobs · MIT · owner 2018 年创建、140 repos、462 followers）**把「我们从未实现过」写进 `AGENTS.md`**（`The project does not implement recorder scheduling, proprietary preparation for mobile downloads, remote access, Enhanced Full Authentication, PCP2, or a DTCP Source for playback distribution`）；`petekp/coordinator`（34⭐ · 26 commits · MIT · 82 repos）**把「token 预算」做成一个可被 pre-commit hook 读取的文件**（`.token-ceilings`：`herdr/RECIPE.md 6500` / `herdr/mods/coordinator-agents/main.js 9000`）；`cnrad/interspace`（131⭐ · Swift · **LICENSE 文件写着 MIT 但 `license.spdx_id` 是 `NOASSERTION`**）**把「自更新只能装签名相同且版本更新的包，否则什么也不做」写进 README**。⭐⭐⭐⭐⭐ **本日报据此修正 11-15 的一条判据：「许可」不是 `license.spdx_id` 字段，而是 LICENSE 文件的实际内容 + 仓库内第三方声明文件 —— `lishuangqiang/mixbar` 的 `THIRD_PARTY_NOTICES.md` 精确到**引用了 `burghr/MacMixer` 的具体 commit `3b2c69015949786b02462281420bb6eb75488434` 与引用范围**，⭐⭐⭐⭐⭐ 这是本数据集里第一次见到**把「借了谁的哪一段代码」的 commit hash 写进产物**。

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [WindGatorRise37/Gemini-Config-Checker-](projects/gemini-config-checker.md) | 473 stars | 观察型（反例样本） |
| [atlas7283/steam-library-bridge](projects/steam-library-bridge.md) | 176 stars | 观察型（反例样本） |
| [tsukumijima/pydtcpip](projects/pydtcpip.md) | 44 stars | 生产可用 |
| [petekp/coordinator](projects/coordinator.md) | 34 stars | 工具型 |
| [cnrad/interspace](projects/interspace.md) | 131 stars | 工具型 |
| [lishuangqiang/mixbar](projects/mixbar.md) | 79 stars | 工具型 |
| [rauchg/winamp-ui-sdk](projects/winamp-ui-sdk.md) | 42 stars | 观察型 |
| [huangserva/h3-fight](projects/h3-fight.md) | 30 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **⭐⭐⭐⭐⭐ 投放体第一次被证明会「认领」一个真实上游：Gemini-Config-Checker- 族的 21 个仓库逐字节复制了真实存在的上游 MatinSenPai/Gemini-Config-Checker（144⭐ · MIT · 2026-10-03）的目录结构与代码。⭐⭐⭐⭐⭐ 实测 internal/scan/scan_test.go、internal/scan/region.go、internal/ui/ui.go、dns_android.go、Makefile、go.mod、VERSION 七个文件在 21 个仓库中各自只有 1 个 md5，blob sha 也完全相同（585365ee… / 88c61e0e… / 0985644d…）；⭐⭐⭐⭐⭐ 但许可被改掉（上游 LICENSE 首行 MIT License，镜像首行 Apache License / license.spdx_id=Apache-2.0）、载荷被改掉（上游 README 无 Dropbox 链接，21 个镜像统一指向 …/GeminiConfigChecker.rar?rlkey=dv7oxsttd2j8kvr5zu7uyx1tm）、53 个 commit 的消息序列逐条复制（Create main.go / Create internal/ui/ui.go / Create internal/scan/scan_test.go …，仅时间戳不同）。⭐⭐⭐⭐⭐ 即「镜像」在本日不再是「上游清空后的产物」（11-13 的 AIRzZ90/study-materials-fork），而是「上游健在、镜像方主动改许可换载荷并批量复制 star」—— 这让 11-13 的判据「parent=null 只能证明不是 GitHub 的 fork 关系」升级为可操作检测法：把同族仓库的 blob sha 逐个比对上游** · 相关项目：WindGatorRise37/Gemini-Config-Checker-, MatinSenPai/Gemini-Config-Checker, TypeTyrantScheme/Gemini-Config-Checker- · 强度：97
2. **⭐⭐⭐⭐⭐ 「账号注册聚集度」升级为「账号 × 家族矩阵」：21 个 Gemini-Config-Checker- owner 账号实测注册于 2026-10-14T01:07:31Z–03:02:24Z 的 6,893 秒窗口内，全部 0 followers、全部恰好 12 个公开仓库，⭐⭐⭐⭐⭐ 且其中 10 个账号同时持有 GitHub-Copilot-app 族的 9–10 个副本、另 4 个持有 ai--manus2.0 族的 9–10 个副本 —— 即同一个账号队列在 11-14 投放 GitHub-Copilot-app / ai--manus2.0，在 11-15 同一时刻投放第三个家族 Gemini-Config-Checker-。⭐⭐⭐⭐⭐ 判据因此从「这些账号是否同批注册」改为「同一个账号是否在多个家族里各持 N–10 个副本」—— 后者不受账号闲置时间影响，也不受家族命名词根相似性影响** · 相关项目：WindGatorRise37/Gemini-Config-Checker-, Visionbeyondtrack/Gemini-Config-Checker-, Violetnyudress/Gemini-Config-Checker- · 强度：95
3. **⭐⭐⭐⭐⭐ 「release 数量 / 版本号」可以同时被凭空制造：atlas7283/steam-library-bridge（176⭐ · 19 subs · 572 blobs · 1 个 commit）在 2026-11-15T21:11:41Z 一次提交后 7 秒内连发 4 个 release（v1.2.8 → v2.3.2 → v3.1.6 → v4.4.2，发布间隔各 4–7 秒，各带 2 个 asset），⭐⭐⭐⭐⭐ 而四个版本号的次版本号互不相同且与代码无关；owner 账号创建于 2026-11-03（仅 12 天）、0 followers、仅 1 个公开仓库；仓库 size 字段实测 0 KB 但树内含 1,050,048 B 的 Steam-Library-Bridge.exe 与 312 个 third_party blob。⭐⭐⭐⭐⭐ 结论：「release 多 / 版本号多」不是发布历史的证据，除非同时核对 release 资产与代码是否随版本演进** · 相关项目：atlas7283/steam-library-bridge, HideKazekage/rob-run-cheat-tool · 强度：93
4. **⭐⭐⭐⭐⭐ 三个真项目用同一套语言给出三种不同的诚实边界：pydtcpip（44⭐ · 9 open issues 全是 6 位不同用户的真机兼容性报告 · 57 blobs · MIT · owner 2018 年创建 / 140 repos / 462 followers）把「我们从未实现过」写进 AGENTS.md（不实现 recorder scheduling / 手机端专有下载准备 / remote access / Enhanced Full Authentication / PCP2 / playback distribution 的 DTCP Source）；coordinator（34⭐ · 26 commits · MIT）把「token 预算」做成 pre-commit hook 可读的文件（.token-ceilings：herdr/RECIPE.md 6500 / herdr/mods/coordinator-agents/main.js 9000）；interspace（131⭐ · Swift）把「自更新只装签名相同且版本更新的包，否则什么也不做」写进 README。⭐⭐⭐⭐⭐ 三者共性：边界被写在了会被机器读到的地方** · 相关项目：tsukumijima/pydtcpip, petekp/coordinator, cnrad/interspace · 强度：92

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-11-16](daily/2026-11-16.md) | 9 | 5 |
| [2026-11-15](daily/2026-11-15.md) | 7 | 5 |
| [2026-11-14](daily/2026-11-14.md) | 6 | 5 |
| [2026-11-13](daily/2026-11-13.md) | 6 | 4 |
| [2026-11-12](daily/2026-11-12.md) | 6 | 4 |
| [2026-11-11](daily/2026-11-11.md) | 2 | 2 |
| [2026-11-10](daily/2026-11-10.md) | 5 | 3 |

## 为什么做这个项目

GitHub Trending 展示注意力，不等于长期价值。本项目记录带日期的仓库事实，阅读代码、文档和 Release，对比跨日变化，区分事实与推断，并保留 Benchmark 未复现、许可证变化或异常 Star 等风险。

## 研究工作流

```mermaid
flowchart LR
  A["采集公开仓库信号"] --> B["阅读代码、文档、Release 与元数据"]
  B --> C["对比跨日变化"]
  C --> D["判断价值与风险"]
  D --> E["发布日报"]
  E --> F["更新项目档案与趋势账本"]
```

- `daily/`：带来源快照的每日研究报告。
- `projects/`：可持续修订的项目档案。
- `indexes/`：跨项目、跨日期的趋势记录。
- `docs/`：生成后的公开站点。
- `scripts/generate_readme.py`：从已提交数据生成双语 README 和活动图表。

## 证据边界

Star、Fork、Release、许可证、语言与时间戳属于采集时可观察的 GitHub 事实；产品质量、架构意义、市场方向和疑似刷星属于研究判断。作者自述在独立复现前会明确标注，后续修正保留在带日期的记录里。

## 生成与验证

```bash
python3 -m pip install pyyaml
python3 scripts/generate_readme.py
git diff --exit-code -- README.md README.zh-CN.md docs/images/research-activity.svg
```

定时研究任务运行在 AIUtil 私有自动化环境中，Token、私有运行记忆和运营状态不进入仓库。

## 安全

请勿提交访问令牌、私有仓库内容、用户级活动数据或未经脱敏的运营记忆。安全问题请通过 [GitHub Security Advisories](https://github.com/aiutil/github-researcher/security/advisories/new) 私下报告。

## 开源协议

Apache License 2.0，详见 [NOTICE](NOTICE)。
