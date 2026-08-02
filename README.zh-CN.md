# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-08-03）

**qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→736 同步增），昨日'脉冲 vs 趋势'之问得到回应——应用层产品化确认非一日脉冲 · K3 本地推理第四极：kimi-k3-in-c 便携 C99 把 RAM 下限打到 8.24GB（176KB 引擎/0 GPU/8GB 与 224GB 字节一致输出），waste 652→1,010 续涨 · 垂直应用层成型：trycompai/crm 1.7K⭐ 以 eve 为底座把 agent 做成 CRM 产品本体（'agent 是产品，数据库只是它记笔记的地方'/证据账本/无置信度/deny-all egress 沙箱） · Microsoft skill-recorder 726⭐ 官方入场（录屏→Copilot 重建意图+步骤→生成可复用 Skill）**

今日热榜新信号：
- **yc-software/qm**（7,015 stars）：多人协作 agent harness，第二日续涨 4,782→7,015（+2,233/+47%），fork 469→736（+267），应用层产品化确认非一日脉冲
- **trycompai/crm**（1,731 stars）：Agentic-first 开源 CRM，以 Vercel eve 为底座——agent 是产品本体、数据库只是它记笔记的地方；证据账本（工具报告观察而非置信度）、deny-all egress 沙箱、单租户内部设计
- **FareedKhan-dev/kimi-k3-in-c**（218 stars）：便携 C99 跑全量 Kimi K3 2.78T，peak RSS 仅 8.24GB（176KB 引擎/0 GPU/1.56TB 检查点），'同一模型在 8GB 与 224GB 字节一致输出'，本地推理第四种独立实现

**→ [查看 2026-08-03 完整简报](daily/2026-08-03.md)**
**→ [查看 2026-08-02 完整简报](daily/2026-08-02.md)**
**→ [查看 2026-08-01 完整简报](daily/2026-08-01.md)**
**→ [查看 2026-07-31 完整简报](daily/2026-07-31.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-08-03](daily/2026-08-03.md) | qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→73 | 5 个深度分析 |
| [2026-08-02](daily/2026-08-02.md) | qm 单日爆发 +250%（1,367→4,782⭐，验证 harness 应用 | 5 个深度分析 |
| [2026-08-01](daily/2026-08-01.md) | Coding agent 应用层从 harness 扩散为完整产品形态——qm  | 4 个深度分析 |
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |
| [2026-07-29](daily/2026-07-29.md) | OpenWorker 重定义「本地优先 AI Coworker」交付物范式 ·  | 4 个深度分析 |
| [2026-07-28](daily/2026-07-28.md) | openclaw（384,378 stars） · hermes-agent（2 | 8 个深度分析 |

---

## 当前最值得关注的趋势

1. **qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→736），增速从 +250% 正常化至 +47% 但量级仍远超 K3（+75），应用层产品化确认非一日脉冲**：相关项目 qm, cindy。
2. **K3 本地推理第四极——kimi-k3-in-c 便携 C99（8.24GB peak RSS/176KB 引擎/0 GPU/'8GB 与 224GB 字节一致输出'）加入战局，waste 652→1,010 续涨，命题从'能否跑'深化为'RAM 下限能压到多低'**：相关项目 kimi-k3-in-c, waste, deltafin。
3. **垂直应用层成型——trycompai/crm 1.7K⭐ 以 Vercel eve 为底座把 agent 做成 CRM 产品本体（agent 是产品/数据库只是笔记/证据账本/无置信度/deny-all egress），eve 首个可观察的生产级应用**：相关项目 crm, skill-recorder。

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

- 📊 项目档案：297 个
- 📅 日报总数：119 期
- 🔄 最近更新：2026-08-03

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
