# GitHub 趋势研究仓库

[English](README.md) · [在线站点](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-08-04）

**应用层产品化第三日完全确认——qm 三日连涨无一日回落（1,367→9,458，三日 +8,091，第三日增量反超第二日彻底排除脉冲假设）+ 多路线并行扩张（通用平台 qm/垂直重写 crm/AI-native 桌面 genoffice 同步放量） · K3 本地推理品类级爆发——kimi-k3-in-c 单日 +955（218→1,173，近 5.4 倍）引爆极端低内存卖点，waste +510 续涨，品类从个别项目变为系统性关注 · AI 推理边界外延——OpenAI 官方发布 ten-proofs，用 Lean 4 形式化十项数学成果，标志'AI + 形式化验证'交叉品类出现 · agent 质量基础设施成型——ratchet 把极简规则从开环注入变闭环检查（285 watchers 高质量关注）**

今日热榜新信号：
- **yc-software/qm**（9,458 stars）：多人协作 agent harness，第三日 +2,443（7,015→9,458），三日累计 +8,091，第三日增量反超第二日彻底排除脉冲假设，应用层产品化趋势完全确立
- **FareedKhan-dev/kimi-k3-in-c**（1,173 stars）：便携 C99 跑全量 K3，peak RSS 仅 8.24GB，今日爆发性增长 +955（218→1,173，近 5.4 倍），'最低 RAM'卖点引爆关注
- **openai/ten-proofs**（432 stars）：OpenAI 官方，Lean 4 形式化《十项数学/理论计算机科学进展》的十个结果（球填充/二进码/非 sofic 群/Connes 刚性反例等），AI 推理↔形式化验证交叉信号

**→ [查看 2026-08-04 完整简报](daily/2026-08-04.md)**
**→ [查看 2026-08-03 完整简报](daily/2026-08-03.md)**
**→ [查看 2026-08-02 完整简报](daily/2026-08-02.md)**
**→ [查看 2026-08-01 完整简报](daily/2026-08-01.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-08-04](daily/2026-08-04.md) | 应用层产品化第三日完全确认——qm 三日连涨无一日回落（1,367→9,458， | 8 个深度分析 |
| [2026-08-03](daily/2026-08-03.md) | qm 第二日续涨 +2,233（4,782→7,015⭐，fork 469→73 | 5 个深度分析 |
| [2026-08-02](daily/2026-08-02.md) | qm 单日爆发 +250%（1,367→4,782⭐，验证 harness 应用 | 5 个深度分析 |
| [2026-08-01](daily/2026-08-01.md) | Coding agent 应用层从 harness 扩散为完整产品形态——qm  | 4 个深度分析 |
| [2026-07-31](daily/2026-07-31.md) | Coding agent harness 多极化——SpaceXAI 官方 gr | 4 个深度分析 |
| [2026-07-30](daily/2026-07-30.md) | Kimi K3 发布首个开源 3T 级模型（2.8T MoE/KDA 新架构/1 | 4 个深度分析 |
| [2026-07-29](daily/2026-07-29.md) | OpenWorker 重定义「本地优先 AI Coworker」交付物范式 ·  | 4 个深度分析 |

---

## 当前最值得关注的趋势

1. **应用层产品化第三日完全确认——qm 三日连涨 +8,091（1,367→9,458），第三日 +2,443 反超第二日 +2,233，彻底排除脉冲假设；crm/genoffice 多路线同步放量**：相关项目 qm, crm, genoffice。
2. **K3 本地推理品类级爆发——kimi-k3-in-c 单日 +955（218→1,173，近 5.4 倍）引爆极端低内存（8.24GB）卖点，waste +510 续涨，品类从个别项目变为系统性关注**：相关项目 kimi-k3-in-c, waste。
3. **AI 推理边界外延——OpenAI 官方 ten-proofs 用 Lean 4 形式化十项数学/理论计算机成果（球填充/非 sofic 群/Connes 刚性反例等），标志 AI + 形式化验证交叉品类出现**：相关项目 ten-proofs。
4. **agent 质量基础设施成型——ratchet 把 coding agent 极简规则从开环注入变闭环检查（PostToolUse hook 实时测量复杂度），与 skill-recorder 正交互补**：相关项目 ratchet, skill-recorder。

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

- 📊 项目档案：300 个
- 📅 日报总数：120 期
- 🔄 最近更新：2026-08-04

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*

## 开源协议

本项目采用 Apache License 2.0，详见 [NOTICE](NOTICE)。
