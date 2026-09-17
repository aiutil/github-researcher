# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-18.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-18

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 5 | 606 | 3 | 10k+ |

**今日核心判断：** thruwire/foreman 1 天 172⭐ ⑂11 TypeSafe Jev Software Factory Foreman（Python · MIT · Jev 决策模型置于 Codex coding agent 之上双 loop 并行 · `codex exec --cd <repo> --sandbox workspace-write --json` 作为 worker · Jev 并行评估 7 维度 implementation_complete / tests_sufficient / requirements_satisfied / worker_stuck / needs_verification / work_off_track / meaningful_progress 返回概率决策 · Python policy 层决定 continue/stop/retry/verify/finish · 默认 20K diff + 12K tail + 30 events + 10 workers 边界 · FactoryConfig 可调 · Worker implementation replaceable 取决于 small worker protocol · verifier 复用 Codex 不同 verification mission · 不替换 Codex 内部 reason/tool/observe loop · doc 4 篇含 theory.md + why-jev.md + what-foreman-proves.md + runtime.md）· NiazMorshed2007/jev-review 1 天 72⭐ ⑂6 本地优先 MCP 软件质量评估插件（TypeScript · MIT · Node.js 20+ MCP stdio · 单一 `jev_review` 工具 · 支持 Claude Code / Codex / Cursor / OpenCode 四大 Coding Agent · 评估 correctness/complexity/changeability/modularity/tests/security 多维度 · 用户 API key 留在本地 · 无 hosted backend · 无 database · 无 telemetry · 无 author proxy · 唯一 remote 请求直接到 Jev API · 编码由主 agent 完成 Jev 只供应 scalar signal · README 重点强调「Your API key stays on your machine」 · 2.9 MB · TypeSafe AI 官方 console 配 Jev API key）· Worldbuilder013/HEXIS 1 天 69⭐ SKILL.md → 扩展有限状态机编译器（Python · MIT · 3.11/3.12 · 论文「Compiling Agent Skills into Extended Finite State Machines」配套代码 · `efsm-v1` JSON schema 含 typed variables + tool/model/judge/user/end 5 类 actions + 有序 guarded transitions + bounded loops + fallback state · LLM 在 state 内推理 · 顺序由 program 强制 · 4 个 shipped machines data analysis/mathematics/QA over corpus/spreadsheet editing · GUIDE.md + PROMPT.md 自描述产物 · 350+ tests 不需网络/endpoint/key · OpenAI-compatible `--model --base-url --api-key-env` · OpenCode native tools + 本地 `bash` backend + 工具 registry · fallback state 重试 + 解释执行兜底）· kitze/skillbox 1 天 69⭐ ⑂7 自托管版本化 AI agent 技能库（TypeScript · MIT · MCP + scoped clients + 可选 Jev recommendations · 自托管 · 版本化 · 主流 Coding Agent 通用接入 · Kitze 知名独立开发者多项目矩阵营销 · Zero To Shipped + Sotto + Tinkerer Club + Sizzy + Supermac）· pengchujin/MacTV 1 天 61⭐ ⑂2 macOS 电视遥控菜单栏 App（Swift · MIT · Apple Silicon arm64 + macOS 14+ · HDMI-CEC 双向遥控 · Mac 音量键控制电视音量 · 电视遥控器控制 Mac 媒体/鼠标 · 菜单栏遥控器 · 输入源切换 · VoiceOver + 浅色/深色外观 + 简繁英三语 · Homebrew cask `pengchujin/tap/mactv` 安装 · 5.1 MB · 与今日 Jev 生态无关联独立工程类项目）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [thruwire/foreman](projects/foreman.md) | 172 stars | 基础设施候选 |
| [NiazMorshed2007/jev-review](projects/jev-review.md) | 72 stars | 工具型 |
| [Worldbuilder013/HEXIS](projects/hexis.md) | 69 stars | 观察型 |
| [kitze/skillbox](projects/skillbox.md) | 69 stars | 工具型 |
| [pengchujin/MacTV](projects/mactv.md) | 61 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **TypeSafe Jev 软件工厂 Foreman——thruwire/foreman 1 天 172⭐ ⑂11（Python · MIT · Jev 决策模型置于 Codex coding agent 之上双 loop 并行 · `codex exec --cd <repo> --sandbox workspace-write --color never --json <mission>` worker · Jev 并行评估 7 维度 implementation_complete / tests_sufficient / requirements_satisfied / worker_stuck / needs_verification / work_off_track / meaningful_progress · Python policy 层决定 continue / stop / retry / verify / finish · 默认 20K diff + 12K tail + 30 events + 10 workers 边界 · FactoryConfig 可调 · worker implementation replaceable 取决于 small worker protocol · verifier 复用 Codex 不同 verification mission · 不替换 Codex 内部 reason/tool/observe loop · 4 篇 docs theory.md / why-jev.md / what-foreman-proves.md / runtime.md · 46 KB · 明确表态「an architectural experiment, not a claim that this design is already better than a conventional coding-agent harness」 · 与 NiazMorshed2007/jev-review + kitze/skillbox + ekzhang/openjev-sglang 等同构 TypeSafe Jev 决策模型生态爆发 但推到「软件工厂监管层」最高抽象）** · 相关项目：thruwire/foreman · 强度：88
2. **本地优先 MCP 软件质量评估插件——NiazMorshed2007/jev-review 1 天 72⭐ ⑂6（TypeScript · MIT · Node.js 20+ · MCP stdio · 单一 `jev_review` 工具 · 支持 Claude Code / Codex / Cursor / OpenCode 四大 Coding Agent · 评估 correctness / complexity / changeability / modularity / tests / security 多维度 · 用户 API key 留在本地 · 无 hosted backend · 无 database · 无 telemetry · 无 author-operated proxy · 唯一 remote 请求直接到 Jev API · 编码由主 agent 完成 Jev 只供应 scalar signal · README 重点强调「Your API key stays on your machine」 · 2.9 MB · TypeSafe AI 官方 console 配 Jev API key · 与昨日 karanb192/awesome-claude-code-mods / agent-sec/mod-provenance-graph「plugin/mod 供应链可见性」同构但推到「plugin/mod 质量评估」领域 · 与 kitze/skillbox 同构 Jev 决策模型生态但推到「软件质量评估」领域）** · 相关项目：NiazMorshed2007/jev-review · 强度：84
3. **SKILL.md → 扩展有限状态机编译器——Worldbuilder013/HEXIS 1 天 69⭐（Python · MIT · 3.11/3.12 · 论文「Compiling Agent Skills into Extended Finite State Machines」配套代码 · `efsm-v1` JSON schema 含 typed variables + tool/model/judge/user/end 5 类 actions + ordered guarded transitions + bounded loops + fallback state · LLM 在 state 内推理 · 顺序由 program 强制 · 4 个 shipped machines data analysis/mathematics/QA over corpus/spreadsheet editing · GUIDE.md + PROMPT.md 自描述产物 · 350+ tests 不需网络/endpoint/key · OpenAI-compatible `--model --base-url --api-key-env` · OpenCode native tools + 本地 `bash` backend + 工具 registry · fallback state 重试 + 解释执行兜底 · 6.1 MB · 与昨日 TopVitamin/agent-skills「中文 Codex Skills 实例」同构但推到「SKILL.md → 状态机编译」学术严肃度）** · 相关项目：Worldbuilder013/HEXIS · 强度：82
4. **自托管版本化 AI agent 技能库——kitze/skillbox 1 天 69⭐ ⑂7（TypeScript · MIT · MCP + scoped clients + 可选 Jev recommendations · 自托管 · 版本化 · 主流 Coding Agent 通用接入 · Kitze 知名独立开发者多项目矩阵营销 · Zero To Shipped + Sotto + Tinkerer Club + Sizzy + Supermac · 191 KB · 与昨日 wshobson/agents「多 Harness Agent Skills 市场」同构但推到「自托管 + 个人开发者背书」领域 · 与 TopVitamin/agent-skills「中文 Codex Skills」同构但推到「英文 + 知名独立开发者 + 自托管」领域）** · 相关项目：kitze/skillbox · 强度：80

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-18](daily/2026-09-18.md) | 5 | 3 |
| [2026-09-17](daily/2026-09-17.md) | 5 | 5 |
| [2026-09-16](daily/2026-09-16.md) | 5 | 4 |
| [2026-09-15](daily/2026-09-15.md) | 5 | 4 |
| [2026-09-14](daily/2026-09-14.md) | 4 | 4 |
| [2026-09-13](daily/2026-09-13.md) | 6 | 4 |
| [2026-09-12](daily/2026-09-12.md) | 8 | 6 |

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
