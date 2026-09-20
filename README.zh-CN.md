# GitHub 趋势研究

<h3 align="center">每日追踪快速增长的开源项目，用可核验事实解释变化、趋势、价值与风险。</h3>

<p align="center">
  不只搬运 Star 排名：记录发生了什么、为什么可能重要、信号有多强，以及哪些结论仍未验证。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://github-research.aiutil.com">在线研究站</a> ·
  <a href="daily/2026-09-21.md">最新日报</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="研究数据检查" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日更新" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub 趋势研究真实站点](docs/images/readme-overview.png)

## 最新研究 · 2026-09-21

| 今日深度分析 | 项目档案 | 核心趋势方向 | 本周 Star 变化 |
| ---: | ---: | ---: | ---: |
| 4 | 618 | 3 | 10k+ |

**今日核心判断：** Haleclipse/CometixCode 1 天 325⭐ ⑂17 Anthropic Claude Code TUI 的 Rust 1:1 重实现（Rust 2024 edition · AGPL-3.0 · iocraft retained-mode TUI + 自带 CometixTUI fork row-level diffing + SIGCONT 自愈 + IME cursor + bracketed paste · 5919 KB · AGPL-3.0 是「服务端网络使用 copyleft」具体路径 · README 明示「Unofficial project, not affiliated with Anthropic」 · 与昨日 09-19 ~ 09-20 各 agent SDK / harness fork 范式同构但推到「terminal UI 1:1 重实现」领域）· rmalde/minecraft-agent 1 天 259⭐ ⑂17 GPT-6 Astra + JEV Minecraft Java 1.16.5 端到端通关 agent（JavaScript · 无 license · Mineflayer + vanilla server + 隐藏 Java sensor 报告龙首精确位置 · nether-final-08 用时 8 分 43.3 秒比上一次 14 分 31.8 秒缩短 40% · 131 次 JEV 决策 + 35 次 Astra 调用 · 6 次床爆炸击杀末影龙 · 全部 17 项 run 检查 + 8 项 route/camera/screen 检查 + 29 项本地测试通过 · 摄像头连续转向 240 度/秒 + 加速度 960 度/秒² · README 诚实表态「Dragon flight and landing times can vary」 · 698 KB）· wuyoscar/jev-skill 1 天 142⭐ ⑂3 Awesome Jev Skills 90 场景 + 9 技能 + 浏览器 / inbox / 文档 / 创意项目工作流合集（Python · MIT · 9 个 skills + 90 个 scenarios · Action tests 工作流 · Demos 链接到原作者 · 双语 README 英文 + 简体中文 · 1011 KB · 与昨日 09-20 v-modal/awesome-jev-tools「Jev 资源聚合 + 严格纳入标准」同构「Jev 资源聚合」但推到「90 场景可运行 + Action tests 工作流 + 9 技能可安装」具体可执行化领域）· ghuntley/underclass 1 天 107⭐ ⑂5 OpenAI 兼容多订阅池化代理（Rust · MIT · /v1/responses + /v1/chat/completions + /v1/models 三端点 · sticky sessions 钉单订阅保持 prompt cache warm · quota exhausted 自动冷却到窗口重置 · 池全枯竭 fail-fast 返回最早 Retry-After · chatgpt.com Codex N 订阅 OAuth device flow · api.githubcopilot.com GitHub device flow · web UI accounts / catalog / live request feed · ghuntley 个人开发者背书（GitHub Principal Engineer 出身） · 170 KB · 与昨日 clawback/claude-code-cost-ledger「session 层成本治理」+ NiazMorshed2007/jev-review「本地优先」同构「AI Coding 多账户 / 多订阅治理」但推到「OpenAI 兼容代理 + sticky session + 冷却 + fail-fast」领域）

| 项目 | 当日快照 | 分类 |
| --- | --- | --- |
| [Haleclipse/CometixCode](projects/cometixcode.md) | 325 stars | 工具型 |
| [rmalde/minecraft-agent](projects/minecraft-agent.md) | 259 stars | 观察型 |
| [wuyoscar/jev-skill](projects/jev-skill.md) | 142 stars | 观察型 |
| [ghuntley/underclass](projects/underclass.md) | 107 stars | 工具型 |

![最近三十期 GitHub 研究活动](docs/images/research-activity.svg)

## 当前趋势信号

1. **Claude Code TUI 的 Rust 1:1 重实现——Haleclipse/CometixCode 1 天 325⭐ ⑂17（Rust 2024 edition · AGPL-3.0 · iocraft retained-mode TUI framework · 自带 CometixTUI fork row-level diffing + SIGCONT 自愈 + IME cursor + bracketed paste + grid layout · TypeScript 组件映射到 Rust 组件 · hook 映射到 hook · 偏差记录在源码里 · interactive loop + tool execution + permissions + MCP + slash commands 已实现 · 其余部分进度中 · 5919 KB · fork/star 5.2% · README 明示「Unofficial project, not affiliated with Anthropic」+ 「Claude/Claude Code are trademarks of Anthropic」+ 「Nothing here is endorsed」· Rust 1.88+ edition 2024 是「最低依赖无系统库无 pkg-config」具体路径 · AGPL-3.0 是「网络使用 copyleft + 修改需公开」具体路径 · 与昨日 09-19 ~ 09-20 各 agent SDK / harness fork 范式同构「Claude Code 替代 / 复用 / 重实现」但推到「terminal UI 1:1 重实现」领域 · 与前日 09-18 kitze/skillbox「自托管 Skills + 知名独立开发者背书」同构「独立开发者 + Claude Code 周边」领域 · 与昨日 09-18 dsh-lab/cordis-bundle-publisher「manifest + minisign + PyPI/OCI publish」同构「Claude Code 生态工具链补齐」但推到「TUI 层重写 + 严肃许可」领域）** · 相关项目：Haleclipse/CometixCode · 强度：88
2. **GPT-6 Astra + JEV Minecraft 端到端通关 agent——rmalde/minecraft-agent 1 天 259⭐ ⑂17（JavaScript · 无 license · Mineflayer + Minecraft Java 1.16.5 vanilla server + 隐藏 Java sensor 报告龙首精确位置 · nether-final-08 用时 8 分 43.300 秒比上一次 14 分 31.800 秒缩短 40% · End combat 152 秒代替 332 秒 · 131 次 JEV 决策 + 35 次 Astra 调用 · 6 次床爆炸击杀末影龙 · 全部 17 项 run 检查 + 8 项 route/camera/screen 检查 + 29 项本地测试通过 · 不改游戏规则或实体状态 · 摄像头连续转向 240 度/秒 + 加速度 960 度/秒² · 隐藏原生 Minecraft 客户端渲染游戏无桌面输入 · 698 KB · fork/star 6.6% · README 诚实表态「Dragon flight and landing times can vary between runs」 · 与昨日 09-20 sutro-sh/jev-align「GEPA 对齐 Jev」+ Heman10x-NGU/openJev-verdict-2.0「Non-Autoregressive Decision Engine 击败 TypeSafe Jev & Laya」同构「Jev 决策模型应用层」但推到「Astra 规划 + JEV 选动作 + Minecraft 端到端通关」具身智能领域 · 与 09-17 rmalde/minecraft-agent 同构领域但推到「nether-final-08 验证 + 全部测试通过」严肃工程化 · 意味着 JEV 决策模型从「决策 API」推到「具身智能 agent 动作选择」具体路径 · 无 license 是企业 / 商业复用风险点）** · 相关项目：rmalde/minecraft-agent · 强度：86
3. **Awesome Jev Skills 90 场景 + 9 技能合集——wuyoscar/jev-skill 1 天 142⭐ ⑂3（Python · MIT · 9 个 skills + 90 个 scenarios · Action tests 工作流 · Demos 链接到原作者（browser-use/jev-ultrafast 等）· 双语 README 英文 + 简体中文 · topics 含 skills badge · 1011 KB · fork/star 2.1% · 与昨日 09-20 v-modal/awesome-jev-tools「README 是分类文件首页聚合 + 5 类应用 + 严格纳入标准 + Curation is not endorsement」同构「Jev 资源聚合」但推到「90 场景可运行 + 9 技能可安装 + Action tests 工作流 + 双语 README」具体可执行化领域 · 与 09-19 mizorewww/laya-mlx「Native MLX runtime for Laya typed decision models 7-14 ms on M3 Max」+ mizorewww/laya-coreml「Core ML + Neural Engine」同构「Laya 决策模型本地推理」但推到「Jev 技能生态 + 应用场景 + 浏览器 / inbox / 文档 / 创意」领域 · 意味着 Jev 决策模型从「awesome 列表资源聚合」推到「可运行场景 + 可安装技能 + 工作流测试」可执行化 · 决定这条主线长期价值的是「Action tests 工作流是否稳定 + 90 场景覆盖广度 + 9 技能的可复用性 + Demos 链接的活跃度 + 双语 README 在中文 Jev 用户的接受度」—— Action tests CI / 90 场景广度 / 技能可复用性 / Demos 活跃度是关键）** · 相关项目：wuyoscar/jev-skill · 强度：82
4. **OpenAI 兼容多订阅池化代理——ghuntley/underclass 1 天 107⭐ ⑂5（Rust · MIT · /v1/responses + /v1/chat/completions + /v1/models 三端点 · sticky sessions 钉单订阅保持上游 prompt cache warm · quota exhausted 自动冷却到窗口重置 · 池全枯竭 fail-fast 返回最早 Retry-After · chatgpt.com Codex N 订阅 OAuth device flow · api.githubcopilot.com GitHub device flow · web UI accounts / catalog / live request feed · ghuntley 个人开发者背书（GitHub Principal Engineer 出身 + 转独立）· 170 KB · fork/star 4.7% · 与昨日 09-17 clawback/claude-code-cost-ledger「session 层成本治理 + canonical JSON + content_hash + buckets.yaml」同构「AI Coding 多账户 / 多订阅治理」但推到「OpenAI 兼容代理 + sticky session + 冷却 + fail-fast」运行时领域 · 与 09-19 NiazMorshed2007/jev-review「本地优先 + 无 backend/database/telemetry/proxy」同构「本地优先」但推到「本地代理 + 多订阅池化」资源治理领域 · 决定这条主线长期价值的是「sticky session 在 chatgpt.com 订阅配额变化的兼容性 + 池全枯竭 fail-fast 在多用户场景的公平性 + web UI 的可用度 + GitHub device flow 在企业 GitHub 账号的可用度 + sticky session vs round-robin 在上游 cache 命中率的差异」—— chatgpt.com 配额机制 + fail-fast 公平性 + web UI 可用度 + device flow 可用度是关键）** · 相关项目：ghuntley/underclass · 强度：78

## 最近 7 期更新量

| 日期 | 深度分析项目 | 核心趋势方向 |
| --- | ---: | ---: |
| [2026-09-21](daily/2026-09-21.md) | 4 | 3 |
| [2026-09-20](daily/2026-09-20.md) | 4 | 3 |
| [2026-09-19](daily/2026-09-19.md) | 4 | 3 |
| [2026-09-18](daily/2026-09-18.md) | 5 | 3 |
| [2026-09-17](daily/2026-09-17.md) | 5 | 5 |
| [2026-09-16](daily/2026-09-16.md) | 5 | 4 |
| [2026-09-15](daily/2026-09-15.md) | 5 | 4 |

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
