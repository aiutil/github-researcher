---
title: "hunk"
slug: "modem-dev-hunk"
date_added: "2026-06-23"
category: "工具型"
emoji: "🔍"
stars: "5,431 stars"
stars_delta: "日增 126，持续 Trending"
language: "TypeScript"
score: 80
tags: ["code-review", "diff", "terminal", "agentic", "cli", "git", "tui"]
url: "https://github.com/modem-dev/hunk"
---

# hunk

## 一句话定位
Review-first terminal diff viewer——为 Agentic Coders 重新设计的代码审查界面。

## 它解决的问题
当 Agent 写代码成为常态，代码审查的工作量和模式发生了变化。传统 git diff 只告诉你"什么变了"，不帮你判断"这个变化对不对"。Agent 一晚上可能改 50 个文件，人类需要高效地审查这些变更。

## 为什么值得关注（2026-06-23）
- **5.4K⭐** 日增 126，在 Trending TypeScript 持续出现
- "Review-first" 定位独特——不是 diff viewer 加 review 功能，而是 review 工具天然以 diff 为核心
- Terminal-native，与 Claude Code / Codex CLI 等 Agent 工作流无缝集成
- Ben Vinegar（Sentry 工程师）参与构建

## 热度来源判断
**真实需求驱动。** Agentic coding 的直接后果是 code review 需求暴增。当你用 Claude Code 写了 200 行代码，你需要一个高效的工具来审查 Agent 的输出。hunk 正好填补了这个空白。

## 关键技术亮点
1. **Review-first 设计** — 界面从"展示 diff"转变为"辅助审查"：变更分类、风险标注、上下文扩展
2. **Terminal-native** — 不离开终端的代码审查，与 CLI Agent 工作流无缝衔接
3. **Agentic coder 定位** — 明确针对"AI Agent 辅助编程"场景设计，而非传统 git diff 工具
4. **137 forks** — 说明开发者不仅在看，还在改造适配自己的工作流

## 架构启发
**核心设计哲学：** 当代码是 Agent 写的，review 的重心从"这段代码对不对"变成"这个 Agent 的决策链路合不合理"。diff viewer 需要从"展示变更"进化到"解释变更意图 + 标注风险"。

**Trade-off：** Terminal 界面限制了可交互性——复杂的多文件 review 可能还是需要 IDE 界面。

## 定位判断
**工具型。** 填补了 Agentic Code Review 工具链中的空白，但不太可能演化为平台或基础设施。更可能被更大的工具栈（如 gstack）集成或内建。

## 风险 / 局限 / 泡沫点
1. **Terminal 限制** — 复杂 review 场景（跨文件追踪、大重构）在 terminal 中体验有限
2. **59 open issues** — 相对项目规模偏高
3. **竞品风险** — gstack /review、GitHub Copilot review、IDE 内建 review 可能覆盖同一需求
4. **不是 daily driver** — 对不需要 terminal-native review 的开发者吸引力有限

## 与同类项目的关系
- **vs gstack /review**：gstack /review 是 Claude Code slash command（角色化审查），hunk 是独立 terminal 工具（diff 展示）。互补
- **vs GitHub PR review**：GitHub 是 web-based + team workflow，hunk 是 terminal + 个人快速 review
- **vs lazygit/tig**：传统 TUI git 客户端没有"review-first"设计，hunk 专注审查体验

## 是否值得持续跟踪
**建议观察。** 工具型项目的关键是用户留存——需要观察是否从"尝鲜"变成"daily driver"。

## 后续观察点
1. 是否被 gstack 或其他 Agent 工具栈集成
2. DAU/MAU 比率——terminal 工具的关键是日活
3. 是否增加"Agent 决策解释"功能——展示 Agent 为什么做这个变更
4. 是否支持多 Agent 输出对比（如 Claude vs Codex 的方案 diff）

## 评分
| 维度 | 分数 | 理由 |
|------|------|------|
| 热度质量 | 7 | 5.4K⭐ 日增 126，稳定增长 |
| 技术创新度 | 7 | Review-first 定位有新意 |
| 工程成熟度 | 7 | Terminal TUI 工程质量好 |
| 架构启发价值 | 7 | Agentic Code Review 是新需求 |
| 企业落地潜力 | 5 | 个人工具，企业场景有限 |
| 中期趋势概率 | 7 | Agentic Review 是确定性需求 |
| 平台化潜力 | 4 | 工具型，平台化空间小 |
| 基础设施潜力 | 3 | 纯工具层 |

**总分：47/80**
**项目归类：工具型**
**是否建议持续跟踪：是（观察型）**

---
*首次记录：2026-06-23*
