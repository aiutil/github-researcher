# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-08-05）

**应用层第四日——qm 突破 10K 关口（9,458→11,092，+1,634，增速继续健康衰减至 +17%），多路线出现分化：crm 加速 +1,446（3,123→4,569，+46% 反超 qm 增速）、genoffice 翻倍 +709（564→1,273，+125%），应用层从'齐涨'进入'分化'阶段 · K3 本地推理品类分化——kimi-k3-in-c 持续 +779（1,173→1,952）逼近 2K，waste 增量骤降（+510→+145），'极限低内存'叙事热度持续压过'可用速度' · Agent 可观测性/治理品类出现——Perplexity 官方 numbat（684⭐，端点 agent 活动可见性 + 取证重建 + 可选阻断），与 ratchet/skill-recorder 构成三层 agent 质量基础设施栈（技能提取→执行约束→事后取证） · Agent 摄入层扩张——Firecrawl 官方 anydoc（2 天 1.1K⭐，Rust，office 文档→LLM-ready Markdown，单数毫秒）**

今日热榜新信号：
- **yc-software/qm**（11,092 stars）：多人协作 agent harness，第四日 +1,634（9,458→11,092），突破 10K 关口，增速继续健康衰减（+47%→+35%→+17%），fork 998→1,200
- **trycompai/crm**（4,569 stars）：Agentic-first 开源 CRM，第四日加速 +1,446（3,123→4,569，+46%），增速反超 qm，fork 205→485（+280），垂直 agent 路线持续放量
- **genspark-ai/genoffice**（1,273 stars）：AI-native 办公套件，第四日翻倍 +709（564→1,273，+125%），fork 197，增速最快，AI-native 桌面生产力路线获得强验证

**→ [查看 2026-08-05 完整简报](daily/2026-08-05.md)**
**→ [查看 2026-08-04 完整简报](daily/2026-08-04.md)**
**→ [查看 2026-08-03 完整简报](daily/2026-08-03.md)**
**→ [查看 2026-08-02 完整简报](daily/2026-08-02.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-08-05](daily/2026-08-05.md) | 应用层第四日——qm 突破 10K 关口（9,458→11,092，+1,634 | 10 个深度分析 |
| [2026-08-04](daily/2026-08-04.md) | 应用层产品化第三日完全确认——qm 三日连涨无一日回落（1,367→9,458， | 8 个深度分析 |
| [2026-08-03](daily/2026-08-03.md) | qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→73 | 5 个深度分析 |
| [2026-08-02](daily/2026-08-02.md) | qm 单日爆发 +250%（1,367→4,782⭐，验证 harness 应用 | 5 个深度分析 |
| [2026-08-01](daily/2026-08-01.md) | Coding agent 应用层从 harness 扩散为完整产品形态——qm  | 4 个深度分析 |
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |

---

## 当前最值得关注的趋势

1. **应用层第四日分化——qm 突破 10K 关口（+1,634，增速衰减至 +17%）但 crm 反超增速（+1,446/+46%）、genoffice 翻倍（+709/+125%）；'齐涨'结束、'分化'开始，多路线各自验证 PMF**：相关项目 qm, crm, genoffice。
2. **K3 本地推理品类分化——kimi-k3-in-c 持续 +779 逼近 2K（极限低内存叙事延续），waste 增量骤降 +510→+145（可用速度叙事退潮），'最低 RAM'卖点持续压过'接近可用速度'**：相关项目 kimi-k3-in-c, waste。
3. **Agent 可观测性/治理品类出现——Perplexity 官方 numbat（端点 agent 活动可见性 + 取证重建 + 可选 pre-action 阻断 + 单二进制）把 agent 安全从'事后审计'推向'实时可观测 + 事中阻断'，与 ratchet（执行约束）、skill-recorder（技能提取）构成三层栈**：相关项目 numbat, ratchet, skill-recorder。
4. **Agent 摄入层扩张——Firecrawl 官方 anydoc（2 天 1.1K⭐，Rust，office 文档→LLM-ready Markdown，单数毫秒，Node/Python 绑定 + Agent Skill 分发），文档解析成为 agent 基础设施标配**：相关项目 anydoc。

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

- 📊 项目档案：302 个
- 📅 日报总数：121 期
- 🔄 最近更新：2026-08-05

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
