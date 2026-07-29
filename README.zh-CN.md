# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-07-30）

**Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1M 上下文/原生多模态）并带火全栈基础设施 · MoonEP 用动态冗余专家实现 EP 完美负载均衡，对标 DeepEP v2 · deltafin 把 2.8T MoE 通过专家按需流式加载塞进单台 Apple Silicon Mac**

今日热榜新信号：
- **MoonshotAI/Kimi-K3**（5,511 stars）：首个开源 3T 级模型，2.8T 参数 MoE / 104B 激活，KDA + Attention Residuals 新架构，Stable LatentMoE（896 专家选 16），1M 上下文，原生多模态，对标 Claude Fable 5 / GPT-5.6
- **MoonshotAI/MoonEP**（858 stars）：专家并行通信库，通过动态冗余专家实现每 rank 完美负载均衡（恒定 S×K tokens），零拷贝 + 静态形状，通信延迟低于 DeepEP v2 且对路由不均衡免疫
- **gavamedia/deltafin**（308 stars）：在单台 Apple Silicon Mac 上运行 2.8T 参数 Kimi K3，MXFP4 专家按需 HTTP 流式加载到本地磁盘缓存，融合 NEON 内核 + Metal 计算，M1 Max 64GB 实测 0.0687 token/s

**→ [查看 2026-07-30 完整简报](daily/2026-07-30.md)**
**→ [查看 2026-07-29 完整简报](daily/2026-07-29.md)**
**→ [查看 2026-07-28 完整简报](daily/2026-07-28.md)**
**→ [查看 2026-07-27 完整简报](daily/2026-07-27.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |
| [2026-07-29](daily/2026-07-29.md) | OpenWorker 重定义「本地优先 AI Coworker」交付物范式 ·  | 4 个深度分析 |
| [2026-07-28](daily/2026-07-28.md) | openclaw（384,378 stars） · hermes-agent（2 | 8 个深度分析 |
| [2026-07-27](daily/2026-07-27.md) | freeCodeCamp（453,008 stars） · openclaw（3 | 8 个深度分析 |
| [2026-07-26](daily/2026-07-26.md) | freeCodeCamp（453,008 stars） · react（246, | 8 个深度分析 |
| [2026-07-25](daily/2026-07-25.md) | caveman（93,628 stars） · awesome-mcp-serv | 8 个深度分析 |
| [2026-07-24](daily/2026-07-24.md) | Human-Agent 协作通信基础设施——Block/Buzz 8.1K⭐（N | 5 个深度分析 |

---

## 当前最值得关注的趋势

1. **Kimi K3 发布：3T 级开源模型 + 全栈基础设施同日涌现**：相关项目 kimi-k3, moonep, deltafin。
2. **MoE 训练通信库赛道：MoonEP 动态冗余专家对标 DeepEP**：相关项目 moonep。
3. **超参数模型本地推理边界探索：2.8T MoE 按需流式加载进单机**：相关项目 deltafin。
4. **Agent 后训练框架成熟化：多轮 Agent RL 走向工程化**：相关项目 axrl。

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

- 📊 项目档案：285 个
- 📅 日报总数：115 期
- 🔄 最近更新：2026-07-30

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
