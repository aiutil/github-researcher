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

## 关键技术亮点亮点
1. **9 类并行子 Agent 审计**：correctness / security / performance / test coverage / tech debt / dependencies / DX / docs / direction，每个发现携带 `file:line` 证据
2. **Advisor 重读验证**：子 Agent 会过度报告，Advisor 模型重读每个引用位置，过滤误报
3. **计划即产品**：不直接实现，而是生成 `plans/001-*.md` 格式的自包含计划，可由任何 Agent 执行
4. **隔离 worktree 执行**：`/improve execute 001` 在独立 worktree 中委派便宜模型执行，review diff vs plan
5. **上下文感知**：读取 ADR/PRD/CONTEXT.md/DESIGN.md 等设计文档，避免对已决定 tradeoff 重复报告
6. **丰富子命令**：`/improve quick|deep|security|perf|branch|next|plan|review-plan|execute|reconcile`

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | shadcn/improve 是一个 Agent Skill，由 9 类并行子 Agent（correctness/security/performance/test coverage/tech debt/dependencies/DX/docs/direction）做审计，再由 Advisor 模型重读过滤误报，输出 `plans/001-*.md` 自包含计划文档；执行通过 `/improve execute 001` 在隔离 worktree 中委派便宜模型。 | 边界来自档案"关键技术亮点"列举的子 Agent 与子命令；不同模型间切换的接口协议、模型供应商、Skill 安装/分发机制未在档案中描述，待核验。 |
| 主路径 | 使用者→Skill 入口（`/improve quick\|deep\|security\|perf\|branch\|next\|plan\|review-plan\|execute\|reconcile`）→并行子 Agent 审计（含 `file:line` 证据）→Advisor 重读验证→产出计划文档→worktree 委派执行→diff vs plan 回写。 | 路径由档案明确描述；具体的编排运行时、状态持久化、上下文注入方式（除 ADR/PRD/CONTEXT.md/DESIGN.md 外）未披露，待核验。 |
| 关键权衡 | "贵模型规划 + 便宜模型执行"的成本梯度利用是核心权衡：规划质量依赖顶级模型的判断力，但执行可下沉到便宜模型；中间的计划文档必须自包含、可审查、可由任意 Agent 重放。审计覆盖广度（9 类别）vs 子 Agent 过度报告的过滤成本，是另一层权衡。 | 权衡描述来自档案"技术亮点"与"架构启发"段；具体的 token 用量、计划长度上限、各子 Agent 的边界规则未量化，待核验。 |
| 最小 PoC | 选定一个非关键中型仓库，启用 `/improve deep` 子命令，不接 CI，跑一遍审计-计划闭环，人工 review 计划质量与误报率；先验证 9 类审计覆盖完整性与 Advisor 过滤可信度两项验收指标，再决定是否接 CI 与 execute 子命令。 | 仓库大小、模型选择与验收阈值未在档案中给出，需在 PoC 中自行确定；`/improve execute` 在复杂场景下的可靠性档案明确标注"待验证"。 |

## 架构启发
**LLM 成本梯度利用的关键不在"用什么模型"，而在"如何分解任务"。** improve 的设计揭示了：
- 审计/规划需要全局视野+判断力 → 贵模型
- 实现/测试只需要局部上下文+执行力 → 便宜模型
- 中间的"计划文档"是两者之间的接口，必须自包含、可审查

这个模式与企业架构中的"架构师设计→工程师执行"完全同构，只是执行者变成了便宜模型。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
  U[使用者] --> CMD[Skill 子命令入口<br/>quick deep security perf branch next plan review-plan execute reconcile]
  CMD --> ORCH[项目编排与运行时<br/>上下文读取: ADR PRD CONTEXT.md DESIGN.md]
  ORCH --> A1[子 Agent: correctness]
  ORCH --> A2[子 Agent: security]
  ORCH --> A3[子 Agent: performance]
  ORCH --> A4[子 Agent: 其余审计类别<br/>待核验]
  A1 --> ADV[Advisor 模型: 重读 file:line 过滤误报]
  A2 --> ADV
  A3 --> ADV
  A4 --> ADV
  ADV --> PLAN[plans/001-*.md<br/>自包含可审查计划]
  PLAN --> EXE[/improve execute/<br/>隔离 worktree + 便宜模型]
  EXE --> DIFF[diff vs plan]
  DIFF -.回写风险待核验.-> ORCH
```

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
