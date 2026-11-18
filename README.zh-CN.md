# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-11-18.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-11-18

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 9 | 839 | 5 | 55k+ |

**今日核心判断：** 本日最硬的方法论发现是**给判据加上对照组之后，11-12~11-15 建立的「账号注册聚集度」判据被证伪了** —— ⭐⭐⭐⭐⭐ 实测 15 个 Trending 仓库各 100 个 fork（1,500 个 fork owner 账号）中「7 天内新建账号」占 **38.0%**，⭐⭐⭐⭐⭐ **而对照组 11 个仓库的 1,100 个 fork owner 中该比例是 40.5% —— 更高**；⭐⭐⭐⭐⭐ **逐仓库看更反直觉：`golang/go` 是 80/100、`rust-lang/rust` 是 72/100、`torvalds/linux` 是 71/100、`sveltejs/svelte` 是 88/100，⭐⭐⭐⭐⭐ 即「短期账号集中 fork 热门仓库」是 GitHub 的常态行为而非攻击特征**；⭐⭐⭐⭐⭐ 与之并列的第二个发现是**「版本发布」这条判据必须从一维拆成四维（tag 数 / release 数 / tag→commit→源码 diff 是否闭合 / 资产是否随版本演进），⭐⭐⭐⭐⭐ 本日实测四个真项目给出四种形态** —— ⭐⭐⭐⭐⭐ `alibaba/open-code-review` 100 release × 7 asset（366 MB，含 sha256sum.txt，**下载 57–951 次**）· `getarcaneapp/arcane` 100 release × 41 asset（1.78 GB，**无 SBOM**）· `backnotprop/plannotator` 100 release × 36 asset（**含 CycloneDX SBOM**，但下载仅 1–12 次）· ⭐⭐⭐⭐⭐ `GoogleChrome/modern-web-guidance-src` **100 个 tag 但只有 1 个 release**（且是 prerelease 的审计数据 JSON），⭐⭐⭐⭐⭐ **而这 100 个 tag 的 commit 全部真实改动了 RAG 索引产物（`guide-chunk-cache.i8/.json/.scale.f32`），其父 commit 10/10 触及源码** —— ⭐⭐⭐⭐⭐ 即 11-16 记录的「假版本号」（`steam-library-bridge`）、11-17 记录的「多而实」（`ffmpeg-skill`）与本日新增的「有 tag 无 release」是**三种不同状态**，⭐⭐⭐⭐⭐ 而判据恰恰在于「链上有没有真实 diff」而非「功能 commit 在前还是在后」⭐⭐⭐⭐⭐ （本日 `open-code-review` 与 `plannotator` 各自实测到功能 commit 在 tag 与在父上交替出现）；⭐⭐⭐⭐⭐ 第三个发现是**「SKILL.md 数量」是一个被复制放大的计数，必须拆成三个独立指标**：⭐⭐⭐⭐⭐ 实测 12 个 skill 类 Trending 项目，`affaan-m/ECC` 的 **1,087 个 SKILL.md 只对应 330 个独立技能身份（3.30×）**、最大单一技能被复制 **10 份**（`verification-loop` / `tdd-workflow` / `security-review` 等各 10 份）· `Tencent/LoopForge` 21 文件 / 9 身份（2.33×）· `backnotprop/plannotator` 23 / 11（2.09×）· `cursor/plugins` 173 / 113（1.53×），⭐⭐⭐⭐⭐ **而 `Claude-BugHunter`（83/83）、`superpowers`（15/15）、`addyosmani/agent-skills`（25/25）、`anthropics/skills`（20/20）、`stitch-skills`（16/16）是零复制**；⭐⭐⭐⭐⭐ **关键的反例是 `superpowers` 15 身份 / 5 套 harness 清单 / 复制 1.00×，⭐⭐⭐⭐⭐ 证明「零复制」与「多 harness」可以兼得 —— 因而 ECC 的 3.30× 是实现选择而非能力上限**；⭐⭐⭐⭐⭐ 第四个发现是**分发协议仍在缓慢收敛，且本日首次出现「零复制 + 多清单」的组合**：⭐⭐⭐⭐⭐ 对 11-17 同一批 17 个仓库同口径复测，**同时公开 `npx skills add` 与 `marketplace add` 两条命令的从 3/17 变为 4/17**（新增 `google-labs-code/stitch-skills`），⭐⭐⭐⭐⭐ **而 `Tencent/LoopForge` 有 21 个技能文件却是 0 套 harness 目录、0 条安装命令**，⭐⭐⭐⭐⭐ **同批 12 个 skill 项目里 0 条安装命令的有 4 个、只有 1 条的有 4 个、两条全有的 4 个 —— 适配层这条赛道的分化比 11-17 更明显，而不是更收敛**；⭐⭐⭐⭐⭐ 第五个发现是**「确定性 + LLM」的混合架构在两个不同领域各自独立出现**：⭐⭐⭐⭐⭐ `alibaba/open-code-review` 是「确定性规则流水线（NPE/线程安全/XSS/SQL 注入）+ LLM Agent」，⭐⭐⭐⭐⭐ `google-research/paper-orchestra` 是 `autoraters/citation_f1.py`（确定性 F1）+ `agent_review.py`（LLM 评审），⭐⭐⭐⭐⭐ **两家机构、两个领域、同一分工 —— 这是本日最值得推广的架构范式**

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [GoogleChrome/modern-web-guidance-src](projects/modern-web-guidance-src.md) | 8,414 stars | 平台候选 |
| [affaan-m/ECC](projects/ecc.md) | 305,425 stars | 平台候选 |
| [backnotprop/plannotator](projects/plannotator.md) | 13,035 stars | 工具型 |
| [alibaba/open-code-review](projects/alibaba-open-code-review.md) | 53,682 stars | 生产可用 |
| [google-research/paper-orchestra](projects/paper-orchestra.md) | 2,884 stars | 观察型 |
| [getarcaneapp/arcane](projects/arcane.md) | 9,275 stars | 生产可用 |
| [Tencent/LoopForge](projects/loopforge.md) | 3,071 stars | 平台候选 |
| [elementalsouls/Claude-BugHunter](projects/claude-bughunter.md) | 9,120 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **⭐⭐⭐⭐⭐ 「账号注册聚集度」这条判据在加上对照组之后被证伪 —— 15 个 Trending 仓库的 1,500 个 fork owner 中「7 天内新建账号」占 38.0%，⭐⭐⭐⭐⭐ 而对照组 11 个仓库的 1,100 个 fork owner 中该比例是 40.5%（更高）；⭐⭐⭐⭐⭐ 逐仓库看：`golang/go` 80/100 · `rust-lang/rust` 72/100 · `torvalds/linux` 71/100 · `sveltejs/svelte` 88/100；⭐⭐⭐⭐⭐ 即「短期账号集中 fork 热门仓库」是 GitHub 的常态行为而非攻击信号 —— 本日报据此撤回对 `google-research/paper-orchestra` 的 100 个同日 fork 的任何「协调刷量」解读** · 相关项目：google-research/paper-orchestra, backnotprop/plannotator, getarcaneapp/arcane · 强度：95
2. **⭐⭐⭐⭐⭐ 「版本发布」判据从一维拆成四维（tag 数 / release 数 / tag→commit→源码 diff 闭合 / 资产随版本演进），本日实测四个真项目给出四种形态：⭐⭐⭐⭐⭐ `alibaba/open-code-review` 100 release × 7 asset（366 MB，含 sha256sum.txt，asset 下载 57–951 次）· `getarcaneapp/arcane` 100 release × 41 asset（1.78 GB，deb/rpm/apk/zst + 14 个裸二进制，**无 SBOM**）· `backnotprop/plannotator` 100 release × 36 asset（2.57 GB，**含 CycloneDX SBOM JSON 与 13 个 sha256**，但下载仅 1–12 次）· ⭐⭐⭐⭐⭐ `GoogleChrome/modern-web-guidance-src` **100 个 tag / 1 个 release**（prerelease 的审计数据 JSON），且其 10/10 抽样 tag 的 commit 真实改动 RAG 索引产物、其父 commit 10/10 触及源码；⭐⭐⭐⭐⭐ 关键结论：判据是「链上有没有真实 diff」而非「功能 commit 在前还是在后」（`open-code-review` 与 `plannotator` 实测到两种形态在同一仓库内交替出现）** · 相关项目：GoogleChrome/modern-web-guidance-src, alibaba/open-code-review, getarcaneapp/arcane · 强度：93
3. **⭐⭐⭐⭐⭐ 「SKILL.md 数量」是复制放大的计数，必须拆成「独立技能身份数 / harness 清单数 / 复制倍数」三个指标：⭐⭐⭐⭐⭐ 实测 12 个 skill 类 Trending 项目 —— `affaan-m/ECC` **1,087 文件 / 330 身份（3.30×）**，最大单一技能被复制 10 份；⭐⭐⭐⭐⭐ `Tencent/LoopForge` 21/9（2.33×）· `backnotprop/plannotator` 23/11（2.09×）· `cursor/plugins` 173/113（1.53×）· `tradermonty/claude-trading-skills` 94/74（1.27×）；⭐⭐⭐⭐⭐ 而 `Claude-BugHunter` 83/83 · `superpowers` 15/15 · `addyosmani/agent-skills` 25/25 · `anthropics/skills` 20/20 · `stitch-skills` 16/16 · `mvanhorn/last30days-skill` 1/1 **全部是零复制**；⭐⭐⭐⭐⭐ 决定性的反例是 `obra/superpowers` **15 身份 / 5 套 harness 清单 / 复制 1.00×** —— 证明「零复制」与「多 harness」可兼得，⭐⭐⭐⭐⭐ 因而 ECC 的 3.30× 是实现选择而非能力上限** · 相关项目：affaan-m/ECC, elementalsouls/Claude-BugHunter, Tencent/LoopForge · 强度：92
4. **⭐⭐⭐⭐⭐ 分发协议仍在缓慢收敛，但赛道的**分化**比收敛更明显：对 11-17 同一批 17 个仓库同口径复测，⭐⭐⭐⭐⭐ **同时公开 `npx skills add` 与 `marketplace add` 两条命令的从 3/17 变为 4/17**（新增 `google-labs-code/stitch-skills`）；⭐⭐⭐⭐⭐ 但在 12 个 skill 类 Trending 项目里，**0 条安装命令的有 4 个、只有 1 条的有 4 个、两条全有的 4 个**；⭐⭐⭐⭐⭐ 而 `Tencent/LoopForge` 有 21 个技能文件却是 **0 套 harness 目录、0 条安装命令**（技能以 `local/.claude/skills/` 项目内目录形式交付）；⭐⭐⭐⭐⭐ 同日 `alibaba/open-code-review` 出现 `plugin-contract.yml` 与 `action-contract.yml` 两个把「契约」做成 CI 门禁的工作流 —— 即「把契约从文档变成可执行检查」本日首次出现，而「让外部用户能装上」仍是最薄弱的一环** · 相关项目：alibaba/open-code-review, Tencent/LoopForge, google-labs-code/stitch-skills · 强度：89

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-11-18](daily/2026-11-18.md) | 9 | 5 |
| [2026-11-17](daily/2026-11-17.md) | 9 | 5 |
| [2026-11-16](daily/2026-11-16.md) | 9 | 5 |
| [2026-11-15](daily/2026-11-15.md) | 7 | 5 |
| [2026-11-14](daily/2026-11-14.md) | 6 | 5 |
| [2026-11-13](daily/2026-11-13.md) | 6 | 4 |
| [2026-11-12](daily/2026-11-12.md) | 6 | 4 |

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
