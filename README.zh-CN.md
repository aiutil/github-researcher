# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-08-02）

**qm 单日爆发 +250%（1,367→4,782⭐，验证 harness 应用层产品化进入主流），qwen-audio-agent 1.2K⭐ 加入应用层（全双工实时语音 + 后台任务并行编排多 harness via ACP） · Agent 记忆独立成品类——OptMem 1.05K⭐（426-token prompt + 单 Python 脚本 / append-only log + 重建式树摘要 / position-is-identity，1M 记忆 wake 0.03s） · Kimi K3 本地推理三极分化——waste 纯 C 零依赖跑全量 2.78T（0.62 tok/s / 64GB Mac / expert 磁盘流式），与 deltafin(Python)/colibri 并立，'推理瓶颈是内存放置策略'出现三种独立实现 · K3 生态斜率继续趋平（K3 +108 / AgentENV +41） · decimen-optical-transfer 3K⭐ 疑似刷星（star/watcher 159:1）标记不推荐**

今日热榜新信号：
- **yc-software/qm**（4,782 stars）：多人协作 agent harness for work，24h 内 1,367→4,782（+250%），Slack+Web 双入口/per-scope 沙箱/统一编排 Pi/OpenCode/Claude Code/Codex
- **VictorTaelin/OptMem**（1,058 stars）：Agent 永久记忆：426-token prompt + 单个无依赖 Python 脚本，append-only log + 重建式树摘要，position-is-identity 每次 lookup 一次 seek，1M 记忆(608MB)wake 0.03s
- **QwenAudio/qwen-audio-agent**（1,181 stars）：Agent 实时语音运行时，全双工语音 + 自然打断，前台对话与后台任务并行，后台 Agent 经 ACP 接入 OpenCode/Claude Code/Codex/Hermes/Kimi Code，v1.0.0 已发布 macOS 桌面版

**→ [查看 2026-08-02 完整简报](daily/2026-08-02.md)**
**→ [查看 2026-08-01 完整简报](daily/2026-08-01.md)**
**→ [查看 2026-07-31 完整简报](daily/2026-07-31.md)**
**→ [查看 2026-07-30 完整简报](daily/2026-07-30.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-08-02](daily/2026-08-02.md) | qm 单日爆发 +250%（1,367→4,782⭐，验证 harness 应用 | 5 个深度分析 |
| [2026-08-01](daily/2026-08-01.md) | Coding agent 应用层从 harness 扩散为完整产品形态——qm  | 4 个深度分析 |
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |
| [2026-07-29](daily/2026-07-29.md) | OpenWorker 重定义「本地优先 AI Coworker」交付物范式 ·  | 4 个深度分析 |
| [2026-07-28](daily/2026-07-28.md) | openclaw（384,378 stars） · hermes-agent（2 | 8 个深度分析 |
| [2026-07-27](daily/2026-07-27.md) | freeCodeCamp（453,008 stars） · openclaw（3 | 8 个深度分析 |

---

## 当前最值得关注的趋势

1. **qm 单日爆发 +250%（1,367→4,782⭐），harness 应用层产品化进入主流；qwen-audio-agent 1.2K⭐ 以全双工实时语音加入应用层**：相关项目 qm, qwen-audio-agent, cindy。
2. **Agent 记忆/持久化独立成品类——OptMem 1.05K⭐（426-token prompt + 单 Python 脚本 / append-only log + 重建式树摘要 / position-is-identity / 1M 记忆 wake 0.03s）**：相关项目 optmem。
3. **Kimi K3 本地推理三极分化——waste 纯 C 零依赖跑全量 2.78T（0.62 tok/s / 64GB Mac / expert 磁盘流式），与 deltafin(Python)、colibri 并立，'推理瓶颈是内存放置策略'出现三种独立实现**：相关项目 waste, deltafin, colibri。

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

- 📊 项目档案：294 个
- 📅 日报总数：118 期
- 🔄 最近更新：2026-08-02

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
