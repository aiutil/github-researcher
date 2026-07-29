---
title: "improve"
slug: "improve"
date_added: "2026-07-07"
category: "工具型"
emoji: "🔍"
stars: "7,049 stars"
stars_delta: "27 天创建，日均 ~261⭐"
language: "Markdown/Agent Skill"
score: 76
tags: ["agent-skill", "code-audit", "cost-optimization", "planning", "shadcn"]
url: "https://github.com/shadcn/improve"
---

# improve

## 一句话定位
shadcn 出品的 Agent Skill——用最强模型审计代码库并生成实现计划，交给便宜模型执行，将 LLM 成本梯度利用范式固化成可安装工具。

## 它解决的问题
AI 编码 Agent 普遍存在"用贵模型做所有事"的问题——审计代码用 Opus，写样板代码也用 Opus。企业使用 Agent 时成本高昂但很多步骤并不需要最强模型。如何系统化地利用不同模型的能力梯度？

## 为什么值得关注（2026-07-07）
- shadcn（shadcn/ui 作者）个人项目，27 天 7K⭐
- 固化了 2026 年最重要的 LLM 成本利用范式："贵模型规划 + 便宜模型执行"
- 9 类并行子 Agent 审计设计，工程化程度高
- 计划即产品（Plans as Product）的理念清晰——不直接实现，而是产出可审查的自包含计划
- 已在 shadcn/ui 自身仓库验证

## 热度来源判断
shadcn 个人品牌是主要加速器（shadcn/ui 80K+⭐），但项目本身的设计理念——成本梯度利用——击中了企业 Agent 应用的核心痛点。不是纯品牌泡沫，有真实工程价值。

## 关键技术亮点
1. **9 类并行子 Agent 审计**：correctness / security / performance / test coverage / tech debt / dependencies / DX / docs / direction，每个发现携带 `file:line` 证据
2. **Advisor 重读验证**：子 Agent 会过度报告，Advisor 模型重读每个引用位置，过滤误报
3. **计划即产品**：不直接实现，而是生成 `plans/001-*.md` 格式的自包含计划，可由任何 Agent 执行
4. **隔离 worktree 执行**：`/improve execute 001` 在独立 worktree 中委派便宜模型执行，review diff vs plan
5. **上下文感知**：读取 ADR/PRD/CONTEXT.md/DESIGN.md 等设计文档，避免对已决定 tradeoff 重复报告
6. **丰富子命令**：`/improve quick|deep|security|perf|branch|next|plan|review-plan|execute|reconcile`

## 架构启发
**LLM 成本梯度利用的关键不在"用什么模型"，而在"如何分解任务"。** improve 的设计揭示了：
- 审计/规划需要全局视野+判断力 → 贵模型
- 实现/测试只需要局部上下文+执行力 → 便宜模型
- 中间的"计划文档"是两者之间的接口，必须自包含、可审查

这个模式与企业架构中的"架构师设计→工程师执行"完全同构，只是执行者变成了便宜模型。

## 定位判断
在 Agent Skill 生态中定位为 "成本优化型审计工具"。不是通用 Agent Skill（不增强代码生成能力），而是约束型 Skill（约束成本+提升审计质量）。与 Ponytail（约束代码量）和 loop-engineering（约束流程）形成互补。

## 风险 / 局限 / 泡沫点
1. **shadcn 依赖度高**：目前由 shadcn 一人维护，bus factor 低
2. **审计质量依赖模型能力**：如果贵模型本身审计能力不足，计划质量无法保证
3. **计划执行闭环尚未成熟**：`/improve execute` 是新功能，在复杂场景下的可靠性待验证
4. **与 CI/CD 集成深度不足**：当前偏交互式使用，与企业 CI pipeline 集成需要额外工程

## 与同类项目的关系
- **vs Ponytail**：Ponytail 约束代码输出量，improve 约束成本和审计流程，互补关系
- **vs loop-engineering**：loop-engineering 是 Agent 编排方法论（5 件套），improve 是审计+规划工具，可被 loop-engineering 编排
- **vs GitHub Copilot Autofix**：Copilot Autofix 是闭源 SaaS 功能，improve 是开源可安装 Skill

## 是否值得持续跟踪
**是。** LLM 成本优化是中期刚需，shadcn 有产品化能力，9 类并行审计的设计理念会影响后续 Agent Skill 设计。

## 后续观察点
1. **企业采用案例**：是否有中大型团队在生产中使用 improve 的审计→执行闭环
2. **CI/CD 集成**：是否会发展出 GitHub Actions / GitLab CI 自动化审计模式
3. **社区贡献扩展**：是否会有人贡献更多审计类别或特定语言/框架的审计规则
4. **与 ECC 的关系**：ECC（226K⭐）也在做 Agent Harness 优化，两者是否会产生整合

---
*首次记录：2026-07-07*
