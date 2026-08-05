# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-08-06）

**anydoc 爆发式跃迁（1,086→4,688，单日 +3,602/+331%，5 天连发 6 个版本），agent 文档摄入层从'新品类'变为'最热赛道'，doc7（本地 VLM 解析）与之构成'云 vs 本地'路线分化 · 应用层第五日结构性降温——qm 增速骤降（+1,634→+561，+17%→+5%），crm 反超为增速第一（+1,569/+34%），genoffice 稳健（+482/+38%），'分化'进入'crm 领跑、qm 守量'格局 · 中文 agent skill 品类出现——human-writing（1,006⭐，'活人感'写作）+ open-kimi-ppt-skill（530⭐，逆向 Kimi Slides→PPT），中文社区从'用 agent'进入'造 skill' · 长程 agent benchmark 品类出现——阿里 Accio RealReplicaBench（1,017⭐，107 任务，状态化评测）**

今日热榜新信号：
- **firecrawl/anydoc**（4,688 stars）：Firecrawl 官方 Rust 文档解析库，第五日爆发 +3,602（1,086→4,688，+331%），单日连发 v0.1.4/v0.1.5/v0.1.6 三个版本，fork 40→205，5 天 6 版高频迭代
- **trycompai/crm**（6,138 stars）：Agentic-first 开源 CRM，第五日反超为应用层增速第一 +1,569（4,569→6,138，+34%），fork 485→627（+142），垂直 agent 路线持续放量
- **yc-software/qm**（11,653 stars）：多人协作 agent harness，第五日增速骤降 +561（11,092→11,653，+5%），仍守万星量级，fork 1,200→1,290，从'增速被反超'进入'量级守成'阶段

**→ [查看 2026-08-06 完整简报](daily/2026-08-06.md)**
**→ [查看 2026-08-05 完整简报](daily/2026-08-05.md)**
**→ [查看 2026-08-04 完整简报](daily/2026-08-04.md)**
**→ [查看 2026-08-03 完整简报](daily/2026-08-03.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-08-06](daily/2026-08-06.md) | anydoc 爆发式跃迁（1,086→4,688，单日 +3,602/+331% | 11 个深度分析 |
| [2026-08-05](daily/2026-08-05.md) | 应用层第四日——qm 突破 10K 关口（9,458→11,092，+1,634 | 10 个深度分析 |
| [2026-08-04](daily/2026-08-04.md) | 应用层产品化第三日完全确认——qm 三日连涨无一日回落（1,367→9,458， | 8 个深度分析 |
| [2026-08-03](daily/2026-08-03.md) | qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→73 | 5 个深度分析 |
| [2026-08-02](daily/2026-08-02.md) | qm 单日爆发 +250%（1,367→4,782⭐，验证 harness 应用 | 5 个深度分析 |
| [2026-08-01](daily/2026-08-01.md) | Coding agent 应用层从 harness 扩散为完整产品形态——qm  | 4 个深度分析 |
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |

---

## 当前最值得关注的趋势

1. **anydoc 爆发式跃迁 + agent 文档摄入层成最热赛道——1,086→4,688（单日 +3,602/+331%，5 天 6 版），doc7（本地 VLM 解析）与之构成'云/服务化 vs 本地/私有化'路线分化**：相关项目 anydoc, doc7。
2. **应用层第五日结构性降温——qm 增速骤降（+1,634→+561，+17%→+5%）但仍守万星量级，crm 反超为增速第一（+1,569/+34%），genoffice 稳健（+482/+38%），'分化'进入'crm 领跑、qm 守量'阶段**：相关项目 qm, crm, genoffice。
3. **中文 agent skill 品类出现——human-writing（1,006⭐，'活人感'中文写作 Skill）+ open-kimi-ppt-skill（530⭐，逆向 Kimi Slides→可编辑 PPTX），中文社区从'使用 agent'进入'制造 skill'**：相关项目 human-writing, open-kimi-ppt-skill。
4. **长程 agent benchmark 品类出现——阿里 Accio RealReplicaBench（1,017⭐，107 任务，状态化 SaaS 副本评测，OpenClaw harness），填补'agent 能否完成真实业务流'的评测空白**：相关项目 realreplicabench。

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

- 📊 项目档案：307 个
- 📅 日报总数：122 期
- 🔄 最近更新：2026-08-06

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
