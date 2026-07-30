# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-07-31）

**Coding agent harness 多极化——SpaceXAI 官方 grok-build（Rust TUI/23.5K⭐）入场，omnigent meta-harness（7.9K⭐）与 vercel/eve filesystem-first（4.2K⭐）三线并进 · 前沿 MoE 本地推理范式确立——colibri 从 3.85K 飙升至 21K⭐，纯 C/零依赖跑 GLM-5.2 744B，VRAM/RAM/存储三级内存层级 · Kimi K3 全栈生态持续深化（K3 5.5K→7.5K/MoonEP→923/deltafin→466/axrl→641/AgentENV→2.6K）**

今日热榜新信号：
- **xai-org/grok-build**（23,556 stars）：SpaceXAI 官方开源 coding agent harness 与 TUI（Rust），全屏鼠标交互/可 headless 跑 CI/经 Agent Client Protocol 嵌入编辑器，预编译二进制覆盖 macOS/Linux/Windows
- **JustVugg/colibri**（21,218 stars）：纯 C/零依赖的 GLM-5.2 744B MoE 推理引擎，把 VRAM/RAM/NVMe 当作统一内存层级；6×RTX 5090 全专家驻留实测 4 tok/s、TTFT 1.6s；19 天从 3.85K 飙至 21K⭐
- **omnigent-ai/omnigent**（7,924 stars）：开源 Agent meta-harness，统一编排 Claude Code/Codex/Cursor/Pi/Hermes + 自定义 agent，跨设备实时协作、策略治理、云沙箱（Modal/Daytona/E2B 等），alpha 阶段

**→ [查看 2026-07-31 完整简报](daily/2026-07-31.md)**
**→ [查看 2026-07-30 完整简报](daily/2026-07-30.md)**
**→ [查看 2026-07-29 完整简报](daily/2026-07-29.md)**
**→ [查看 2026-07-28 完整简报](daily/2026-07-28.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |
| [2026-07-29](daily/2026-07-29.md) | OpenWorker 重定义「本地优先 AI Coworker」交付物范式 ·  | 4 个深度分析 |
| [2026-07-28](daily/2026-07-28.md) | openclaw（384,378 stars） · hermes-agent（2 | 8 个深度分析 |
| [2026-07-27](daily/2026-07-27.md) | freeCodeCamp（453,008 stars） · openclaw（3 | 8 个深度分析 |
| [2026-07-26](daily/2026-07-26.md) | freeCodeCamp（453,008 stars） · react（246, | 8 个深度分析 |
| [2026-07-25](daily/2026-07-25.md) | caveman（93,628 stars） · awesome-mcp-serv | 8 个深度分析 |

---

## 当前最值得关注的趋势

1. **Coding agent harness 多极化：官方入场 + meta-harness + filesystem-first 三线并进**：相关项目 grok-build, omnigent, eve。
2. **前沿 MoE 本地推理范式确立：colibri 纯 C 引擎把 744B MoE 跑上消费硬件**：相关项目 colibri。
3. **Kimi K3 全栈生态持续深化：模型/训练/推理/后训练/环境五层齐增长**：相关项目 kimi-k3, moonep, deltafin。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [MoonshotAI/Kimi-K3](projects/kimi-k3.md) | 基础设施候选 | 首个开源 3T 级模型——2.8T 参数 MoE / 104B 激活，KDA + | 持续跟踪 |
| [DietrichGebert/ponytail](projects/ponytail.md) | 工具型 | 让 AI Agent 像最懒的资深工程师一样思考——YAGNI 极简主义 Ski | 持续跟踪 |
| [12-Factor Agents](projects/12-factor-agents.md) | 基础设施候选 | 构建足够好到可以交给专业用户使用的 LLM 驱动软件的 12 条工程原则，Age | 持续跟踪 |
| [codebase-memory-mcp](projects/codebase-memory-mcp.md) | 基础设施候选 | 高性能代码智能 MCP Server——用 tree-sitter 将代码库索引 | 持续跟踪 |
| [gstack](projects/garrytan-gstack.md) | 平台候选 | YC CEO Garry Tan 的 Claude Code 工具栈——23 个 | 持续跟踪 |
| [Graphify](projects/graphify.md) | 平台候选 | 跨 Agent 平台的 GraphRAG 编排 Skill，一次编写，7+ Ag | 持续跟踪 |
| [andrewyng/openworker](projects/openworker.md) | 平台候选 | Andrew Ng 出品的开源本地 AI Coworker——运行在你的桌面上， | 持续跟踪 |
| [Understand-Anything](projects/understand-anything.md) | 平台候选 | 将任意代码转换为交互式知识图谱，支持探索、搜索和问答，兼容 Claude Cod | 持续跟踪 |
| [NVIDIA OpenShell](projects/openshell.md) | 基础设施候选 | NVIDIA 出品的 Agent 安全运行时沙箱——Rust 实现，四层策略防御 | 持续跟踪 |
| [Agent-Reach](projects/agent-reach.md) | 基础设施候选 | AI Agent 的互联网感知层——一个 CLI 聚合 Twitter/Redd | 持续跟踪 |

---

## 数据统计

- 📊 项目档案：287 个
- 📅 日报总数：116 期
- 🔄 最近更新：2026-07-31

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
