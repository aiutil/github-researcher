# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-11-23.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-11-23

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 9 | 842 | 5 | 45k+ |

**今日核心判断：** 本日最硬的发现是**我们自己的两条判据在同一批数据上被证伪，而根因是同一个：测量口径** —— ⭐⭐⭐⭐⭐ 第一条是**「asset 下载次数」这条判据**：11-18 日报用它断言 `plannotator`「下载仅 1–12 次」、`open-code-review`「57–951 次」，⭐⭐⭐⭐⭐ **但那次的脚本取的是 `sorted(download_count)[:12]`（36 个 asset 里最小的 12 个）当成全量区间**，⭐⭐⭐⭐⭐ **本日在**同一时刻、同一批 release** 上复测：同一 tag `v0.29.1` 的真实区间是 9–1,691（11-18 视角显示 9–13，**被低估 130.1×**）、`v0.29.0` 是 4–1,735（**216.9×**）、`v0.29.2` 是 3–453（**90.6×**），⭐⭐⭐⭐⭐ **即 11-18 那条「采用度差一到两个数量级」的结论是测量伪影而非事实**；⭐⭐⭐⭐⭐ 第二条是**「SKILL.md 复制倍数」这条判据**：11-18 日报的核心发现是 ECC「1,087 文件 / 330 身份 = 3.30×」，⭐⭐⭐⭐⭐ **但 330 这个数用的是「父目录名」作身份，本日在同一棵树上并置两种口径后发现 —— 按名口径 331（3.29×，与 11-18 一致）、按内容 sha 口径 944（1.15×），⭐⭐⭐⭐⭐ 而 273 个「被复制」的技能名里有 240 个其副本**内容并不相同**，⭐⭐⭐⭐⭐ **即「复制倍数 3.30×」衡量的是「同名目录的分布」而非「同一份内容的冗余」，⭐⭐⭐⭐⭐ `plannotator` 更极端：名口径 23/11（2.09×）→ 内容口径 23/23（1.00×），4 个被复制的技能身份其 5/4/2 份副本逐份内容都不同**；⭐⭐⭐⭐⭐ **这两个修正合起来指向同一条方法论：凡是用「截断的样本」或「代理身份」去支撑一个关于「量级」的结论，都必须先做口径审计** —— ⭐⭐⭐⭐⭐ **而本日第三次给出正面证据的是「star 增速」这条本数据集连续 6 份日报都标注「未做统计」的指标**：⭐⭐⭐⭐⭐ **本数据集首次攒齐 6 个连续日快照（11-18 → 11-23，日更），⭐⭐⭐⭐⭐ 实测 14 个在 6 个快照中全程在榜的仓库、120 个相邻日区间，⭐⭐⭐⭐⭐ 结果是 **0 个负区间、0 个平区间**，min +49 / p25 +226 / median +415 / p75 +668 / max +2,156**，⭐⭐⭐⭐⭐ 且 `elementalsouls/Claude-BugHunter` 的日增序列是 **+2,156 / +1,140 / +1,670 / +1,824 / +1,733**，⭐⭐⭐⭐⭐ **即 6 天里没有一天是「异常值日」，⭐⭐⭐⭐⭐ 增长是连续的、有噪声但无断裂 —— 这与 11-17 记录的「投放体可用 30 行定时脚本凭空制造 push 频率」形成直接对照：⭐⭐⭐⭐⭐ 本数据集首次有了一条能真正区分「真实增长」与「被制造的增长」的基线**；⭐⭐⭐⭐⭐ 第四个发现是**「分发适配层」这条线在本日出现了一个反向样本**：`obra/superpowers` 仍是 **15 身份 / 15 文件 / 1.00× 零复制**，⭐⭐⭐⭐⭐ **但它的 harness 目录数从 11-18 的 5 套降到了 4 套，而 `backnotprop/plannotator` 从 2 套升到 4 套、`HKUDS/CLI-Anything` 是 0 套目录却有 3 条安装命令** —— ⭐⭐⭐⭐⭐ 即「harness 目录数」与「独立技能身份数」都不是稳定的能力指标，⭐⭐⭐⭐⭐ 而真正稳定的结构事实是「有没有一条别人能跑的安装命令」

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [backnotprop/plannotator](projects/plannotator.md) | 14,399 stars | 工具型 |
| [alibaba/open-code-review](projects/alibaba-open-code-review.md) | 55,384 stars | 生产可用 |
| [elementalsouls/Claude-BugHunter](projects/claude-bughunter.md) | 17,618 stars | 工具型 |
| [affaan-m/ECC](projects/ecc.md) | 306,433 stars | 平台候选 |
| [obra/superpowers](projects/superpowers.md) | 324,102 stars | 平台候选 |
| [jingyaogong/minimind](projects/minimind.md) | 68,602 stars | 观察型 |
| [nginx/nginx](projects/nginx.md) | 32,874 stars | 基础设施候选 |
| [HKUDS/CLI-Anything](projects/cli-anything.md) | 62,725 stars | 平台候选 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **⭐⭐⭐⭐⭐ 「asset 下载次数」这条判据在同口径复测下被证伪 —— 根因是 11-18 的脚本取 `sorted(download_count)[:12]`（36 个 asset 里**最小的** 12 个）当作全量区间；⭐⭐⭐⭐⭐ 本日在同一时刻、同一批 release 上复测：plannotator 同一 tag `v0.29.1` 真实区间 9–1,691（11-18 视角显示 9–13，**低估 130.1×**）、`v0.29.0` 4–1,735（**216.9×**）、`v0.29.2` 3–453（**90.6×**）；⭐⭐⭐⭐⭐ 因此 11-18 那条「plannotator 下载仅 1–12 次 vs open-code-review 57–951 次，差一到两个数量级」的结论**是测量伪影，不是事实** —— 本日按「最新 3 个 release 均值 vs 全量 release 均值」复测，`open-code-review` 是 2.0×（旧 release 更热）、`nginx/nginx` 4.1×、`we-promise/sure` 4.1×，而 `plannotator` 0.4×、`autoclip` 0.2×（新 release 更热），⭐⭐⭐⭐⭐ 即下载量与 release 年龄的相关性在不同项目上符号相反，「取最新 release」根本不是一个可跨项目比较的采样策略** · 相关项目：backnotprop/plannotator, alibaba/open-code-review, zhouxiaoka/autoclip · 强度：96
2. **⭐⭐⭐⭐⭐ 「SKILL.md 复制倍数」这条判据同样是口径问题 —— 11-18 头条「ECC 1,087 文件 / 330 身份 = 3.30×」用的是**父目录名**作身份；⭐⭐⭐⭐⭐ 本日在同一棵树上并置两种口径：**名口径 331（3.29×，与 11-18 复现一致）/ 内容 sha 口径 944（1.15×）**，⭐⭐⭐⭐⭐ 而 273 个「被复制」的技能名中 **240 个其副本内容并不相同**（仅 33 个是逐字节相同）；⭐⭐⭐⭐⭐ `plannotator` 更极端：名口径 23/11（2.09×）→ 内容口径 **23/23（1.00×）**，4 个被复制身份（`plannotator-review` 5 份 / `plannotator-last` 4 份 / `plannotator-inbox` 2 份 / `open-code-review` 2 份）的每一份副本内容都不同；⭐⭐⭐⭐⭐ **结论：3.30× 衡量的是「同名技能在多少个目录出现」，而非「同一份内容被冗余存储了几次」；⭐⭐⭐⭐⭐ ECC 真正的冗余是「944 个不同 blob sha / 1,089 个文件」这一层，即 1.15×，⭐⭐⭐⭐⭐ 而它 273 个同名技能里 240 个是「按 harness 改写过的变体」而非复制品** —— 修正后的判据应分三层：内容冗余倍数（sha 级）/ 变体倍数（同名不同内容）/ 身份跨度（同名跨目录）** · 相关项目：affaan-m/ECC, backnotprop/plannotator, cursor/plugins · 强度：95
3. **⭐⭐⭐⭐⭐ 「star 增速」这条本数据集连续 6 份日报都标注「未做统计」的指标，本日首次有真实时间序列 —— 本数据集攒齐了 **6 个连续日快照（11-18 → 11-23，日更）**；⭐⭐⭐⭐⭐ 实测 14 个全程在榜仓库、**120 个相邻日区间：0 个负区间、0 个平区间**，min +49 / p25 +226 / median +415 / p75 +668 / max +2,156；⭐⭐⭐⭐⭐ `elementalsouls/Claude-BugHunter`（9,095 → 17,618，**+93.8% / 5 天**）日增序列为 **+2,156 / +1,140 / +1,670 / +1,824 / +1,733**，⭐⭐⭐⭐⭐ `obra/superpowers`（319,255 → 324,102，+1.5%）为 +2,022 / +738 / +774 / +866 / +447，⭐⭐⭐⭐⭐ **即 6 天里没有任何一天是「异常值日」，增长连续、有噪声但无断裂**；⭐⭐⭐⭐⭐ **这直接补上了 11-17 记录的那条判据缺口 —— 「push 频率与 commit 数量可被 30 行定时脚本凭空制造」，⭐⭐⭐⭐⭐ 而 star 增量的**连续性（0 个负区间 / 0 个平区间）是一条本数据集此前没有的、可与「被制造的增长」区分的基线** · 相关项目：elementalsouls/Claude-BugHunter, obra/superpowers, mvanhorn/last30days-skill · 强度：93
4. **⭐⭐⭐⭐⭐ 「分发适配层」的三个度量在本日全部出现反向样本，说明它们都不是稳定的能力指标 —— ⭐⭐⭐⭐⭐ `obra/superpowers` 仍是 **15 身份 / 15 文件 / 1.00× 零复制**（11-18 的「零复制 + 多 harness」结论复现），⭐⭐⭐⭐⭐ **但它的 harness 目录数从 11-18 实测的 5 套降到了 4 套**（`antigravity` / `claude-code` / `codex` / `opencode`）；⭐⭐⭐⭐⭐ **而 `backnotprop/plannotator` 从 2 套升到 4 套（`claude` / `codex` / `copilot` / `gemini`）、`HKUDS/CLI-Anything` 是 0 套 harness 目录却有 3 条安装命令**（`pip install cli-anything-hub` / `npx skills add HKUDS/CLI-Anything --list` / `npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y`）；⭐⭐⭐⭐⭐ 同口径复测 11-17 的 17 仓库队列，**双安装命令（`npx skills add` + `marketplace add`）的仓库数从 11-18 记录的 4/17 降为 2/9（在榜子集）**，⭐⭐⭐⭐⭐ 即结论是：唯一跨项目稳定的结构事实不是「harness 目录数」也不是「技能身份数」，而是「有没有一条别人能直接粘贴运行的安装命令」** · 相关项目：obra/superpowers, HKUDS/CLI-Anything, backnotprop/plannotator · 强度：89

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-11-23](daily/2026-11-23.md) | 9 | 5 |
| [2026-11-18](daily/2026-11-18.md) | 9 | 5 |
| [2026-11-17](daily/2026-11-17.md) | 9 | 5 |
| [2026-11-16](daily/2026-11-16.md) | 9 | 5 |
| [2026-11-15](daily/2026-11-15.md) | 7 | 5 |
| [2026-11-14](daily/2026-11-14.md) | 6 | 5 |
| [2026-11-13](daily/2026-11-13.md) | 6 | 4 |

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
