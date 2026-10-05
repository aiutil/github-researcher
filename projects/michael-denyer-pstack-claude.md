---
title: "michael-denyer/pstack-claude"
slug: "michael-denyer-pstack-claude"
date_added: "2026-10-06"
category: "工具型"
emoji: "🔌"
stars: "1405 stars"
stars_delta: "4 个月 1405⭐，fork 152，fork/star 10.8%；持续 GitHub Trending daily 列表 222⭐ today"
language: "JavaScript"
score: 82
tags: ["pstack-claude", "michael-denyer", "pstack", "lauren-tan", "cursor", "plugin-marketplace", "claude-code", "codex", "pi", "opencode", "gemini-cli", "prime-agent", "poteto-mode", "tla-plus", "agent-formal-verify", "setup-pstack", "reasoning-effort", "arena-runners", "mit", "3771kb", "4-months"]
url: "https://github.com/michael-denyer/pstack-claude"
---

# michael-denyer/pstack-claude

## 一句话定位
Lauren Tan Cursor 官方 pstack 跨 6 Harness（Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent）的严肃工程化移植——poteto-mode 统一入口 + how/why/architect/fix/rerun 工作流 + agent-formal-verify TLA+ 配套。

## 它解决的问题
2026 年 Cursor 官方 pstack（Lauren Tan 的 opinionated Cursor skill stack）改进了 agent outcomes，但仅服务 Cursor 单 Harness。开发者需要 **跨 6 Harness（Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent）严肃工程化移植**：michael-denyer/pstack-claude 提供 **Tell `poteto-mode` your goal and it will invoke the correct workflow for the task + It keeps your code concise, simple and verified + agent-formal-verify 配套 TLA+ model checking + Lean + setup-pstack 模型默认 / reasoning effort / arena runners + how/why/architect/fix/rerun 工作流** —— 解决 **「Cursor 官方 pstack 仅服务 Cursor + 缺跨 Harness 严肃工程化移植 + 缺 TLA+ formal verify 配套」** 的工程链缺口。目标是成为 Cursor 官方 pstack 跨 Harness 严肃工程化移植候选。

## 为什么值得关注
- **Stars:** 1,405（截至 2026-10-06），4 个月突破 1.4K，增速极快
- **Forks:** 152，社区贡献活跃（跨 Harness 严肃工程化移植方向天然适合贡献）
- **Watchers:** 未明示
- **Open Issues:** 未明示
- **License:** MIT
- **语言:** JavaScript
- **活跃度:** created 2026-05-26，pushed_at 2026-10-05，持续高活跃
- **规模:** 3.8MB
- **Topics:** 20 个覆盖（agent-plugin / agent-skills / agentic-ai / anthropic / chatgpt / claude / claude-code / claude-code-skills / claude-plugin / claude-skills / code-review / codex / codex-cli / codex-plugin / codex-skills / coding-agent / developer-tools / gemini-cli / opencode / pstack）
- **Trending:** GitHub Trending daily 列表 222⭐ today

## 热度来源判断
pstack-claude 的热度是 **「Cursor 官方 pstack 严肃工程化 Agent workflow 刚需 × 6 Harness 严肃工程化移植 × poteto-mode 统一入口 × agent-formal-verify TLA+ 配套 × MIT」** 的强劲组合。Cursor 官方 pstack（Lauren Tan）是 2026 年严肃工程化 Agent workflow 的头部样本，但仅服务 Cursor 单 Harness。`michael-denyer/pstack-claude` 把 pstack 移植到 Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent 6 Harness 直击"单 Harness 锁定"痛点。`poteto-mode` + `how/why/architect/fix/rerun` 工作流 + `agent-formal-verify TLA+` + `setup-pstack` 模型默认 + `arena runners opus @xhigh fable @max` 体现严肃工程化深度。`4 个月 1405⭐` + `222⭐ today` 反映社区对跨 Harness 严肃工程化移植方向的强烈兴趣。热度**真实且具跨 Harness 严肃工程化潜力**——但需警惕：6 Harness 适配层兼容性、poteto-mode 在多任务的调派准确性、TLA+ 在多并发不变量验证的严谨度、setup-pstack 在多用户的可定制性均未在档案中明示。

## 关键技术亮点
1. **跨 6 Harness 严肃工程化移植:** Claude Code + Codex + Pi + OpenCode + Gemini CLI + Prime Agent（plugin marketplace + plugin install）
2. **poteto-mode 统一入口:** Tell `poteto-mode` your goal and it will invoke the correct workflow for the task
3. **代码质量保证:** It keeps your code concise, simple and verified
4. **how/why/architect/fix/rerun 工作流:** for bug reproduces the failure, uses how and why to investigate, delegates the fix, then reruns the failing case + if the fix crosses a function boundary, it brings in architect before implementing
5. **agent-formal-verify TLA+:** concurrency bugs and invariants that tests cannot reach → TLA+ model checking + Lean
6. **setup-pstack:** 模型默认 + reasoning effort per role + arena runners opus @xhigh fable @max
7. **`/loop` + 路由指令:** Pi extension: subagent / question / wake-up 工具
8. **`/skill:<name>`:** 跨 Harness skill 调用
9. **shared installation:** docs/reference.md#shared-skills-installation Prime Agent / OpenCode / Gemini CLI / skills-only
10. **20 个 topics 全覆盖:** 跨 Harness 兼容性清晰度极高

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Lauren Tan Cursor 官方 pstack 跨 6 Harness（Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent）的严肃工程化移植；poteto-mode 统一入口 + how/why/architect/fix/rerun 工作流 + agent-formal-verify TLA+ 配套 | 仅基于 README 描述的 Lauren Tan's pstack (Cursor 官方 plugins/tree/main/pstack) is an opinionated Cursor skill stack that improves agent outcomes + This is a port for Claude Code, Codex, Pi and other agent harnesses + Tell poteto-mode your goal + It keeps your code concise, simple and verified + agent-formal-verify TLA+ + Lean + Claude Code /plugin marketplace add + Codex codex plugin marketplace add + Pi pi install git:github + setup-pstack 模型默认 + reasoning effort per role + arena runners opus @xhigh fable @max；具体 6 Harness 适配层实现深度、poteto-mode 在多任务的调派准确性、TLA+ model checking 在多并发不变量验证的严谨度未在档案中明示 |
| 主路径 | 开发者 → Tell poteto-mode your goal → invokes the correct workflow for the task → 保持代码 concise, simple, verified → for concurrency bugs see agent-formal-verify TLA+ Lean → For Prime Agent / OpenCode / Gemini CLI see shared installation docs/reference.md | 主路径为档案语义抽象；具体 poteto-mode 在多 bug 类型的覆盖广度、TLA+ 在多并发不变量验证的严谨度、Lean 在多形式化验证的深度未在档案中讨论 |
| 关键权衡 | 6 Harness 适配层兼容性 vs 单 Harness 优化 + poteto-mode 统一入口 vs 单 skill 优化 + how/why/architect/fix/rerun 覆盖广度 vs 单步骤优化 + agent-formal-verify TLA+ 严谨度 vs 简单测试 + setup-pstack 模型默认可定制性 vs 默认值合理度 + arena runners opus @xhigh fable @max 优化 vs 单一模型 + MIT 商用清晰 | 档案明示 poteto-mode + It keeps your code concise, simple and verified + agent-formal-verify TLA+ Lean + 6 Harness 适配 + setup-pstack reasoning effort per role + arena runners；具体 6 Harness 适配层在多版本的兼容性、TLA+ 在多实际 bug 的验证严谨度未在档案中讨论 |
| 最小 PoC | Claude Code 装 `/plugin marketplace add michael-denyer/pstack-claude` + `/plugin install pstack@pstack-claude` → 用 poteto-mode 修 1 个 bug 验证 how/why/architect/fix/rerun 工作流；切换到 Codex 装 `codex plugin marketplace add` + `codex plugin add pstack@pstack-claude` 验证多 Harness 兼容性；最后装 agent-formal-verify 验证 TLA+ model checking；可运行 setup-pstack arena runners opus @xhigh fable @max 验证多模型优化 | PoC 范围由档案「6 Harness + poteto-mode + how/why/architect/fix/rerun + agent-formal-verify + setup-pstack + arena runners」建议推导；具体 TLA+ 在多并发不变量的严谨度、setup-pstack 在多用户的可定制性未在档案中讨论 |

## 架构启发
pstack-claude 的核心启发是 **「Cursor 官方 pstack 严肃工程化 Agent workflow 应该跨 6 Harness 严肃工程化移植 + 配套 agent-formal-verify TLA+」**。Cursor 官方 pstack（Lauren Tan）仅服务 Cursor 单 Harness，开发者苦于跨 Harness 兼容性问题（Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent 各自格式不同）。`michael-denyer/pstack-claude` 把 pstack 移植到 6 Harness + poteto-mode 统一入口 + how/why/architect/fix/rerun 工作流 + agent-formal-verify TLA+ 配套 + setup-pstack 模型默认 —— 这是跨 Harness 严肃工程化移植的方向。更深层的启发是：**TLA+ model checking + Lean 形式化验证是严肃工程化 Agent workflow 的关键组件** —— 对并发不变量验证 test 无法 reach。4 个月 1405⭐ + 222⭐ today 显示这是真实严肃工程化信号——但能否持续，取决于 6 Harness 适配层兼容性、poteto-mode 在多任务的调派准确性、TLA+ 在多并发不变量验证的严谨度、setup-pstack 在多用户的可定制性。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Dev[开发者] --> Goal[Tell poteto-mode your goal]
  Goal --> Wf[invokes the correct workflow<br/>for the task]
  Wf --> How[how]
  Wf --> Why[why]
  Wf --> Arch[architect<br/>如果 fix crosses function boundary]
  Wf --> Fix[fix<br/>delegates the fix]
  Wf --> Rerun[reruns the failing case]
  How --> Verify[keeps your code<br/>concise, simple and verified]
  Why --> Verify
  Arch --> Verify
  Fix --> Verify
  Rerun --> Verify
  Verify -.并发 bug.-> Formal[agent-formal-verify<br/>TLA+ model checking + Lean]
  Goal --> Install[6 Harness 适配<br/>Claude Code / Codex / Pi<br/>OpenCode / Gemini CLI / Prime Agent]
  Install --> CC[Claude Code<br/>/plugin marketplace add<br/>/plugin install pstack@pstack-claude]
  Install --> CX[Codex<br/>codex plugin marketplace add<br/>codex plugin add pstack@pstack-claude]
  Install --> PI[Pi<br/>pi install git:github.com<br/>+ subagent/question/wake-up 工具<br/>/loop + 路由指令]
  Install --> OA[OpenCode]
  Install --> GC[Gemini CLI]
  Install --> PA[Prime Agent]
  CC --> Skill[/skill:<name>]
  CX --> Skill
  PI --> Skill
  OA --> Skill
  GC --> Skill
  PA --> Skill
  CC --> Setup[setup-pstack<br/>模型默认 / reasoning effort per role]
  Setup --> Arena[arena runners<br/>opus @xhigh fable @max<br/>pstack:effort-<level> subskill]
  CX --> Setup
  PI --> Setup
  OA --> Setup
  GC --> Setup
  PA --> Setup
  CC -.兼容.-> Shared[shared installation<br/>docs/reference.md]
  CX -.兼容.-> Shared
  PI -.兼容.-> Shared
  OA -.兼容.-> Shared
  GC -.兼容.-> Shared
  PA -.兼容.-> Shared
  Install -.上游.-> Cursor[Cursor 官方<br/>plugins/tree/main/pstack<br/>Lauren Tan]
  Install -.许可证.-> MIT[MIT 商用清晰<br/>michael-denyer 个人]
```

## 定位判断
**工具型项目（Cursor 官方 pstack 跨 Harness 严肃工程化移植候选）。** pstack-claude 不仅是一个 porting 工具，更试图成为 Cursor 官方 pstack 严肃工程化 Agent workflow 的跨 Harness 移植方案——填补 Cursor 单 Harness 严肃工程化锁定。若成功，它会成为 Cursor pstack 严肃工程化生态的跨 Harness 入口。4 个月 1405⭐ + 222⭐ today 已显示社区对跨 Harness 严肃工程化移植方向的强烈兴趣。但"移植化"取决于关键问题：6 Harness 适配层在多版本的兼容性、poteto-mode 在多任务的调派准确性、TLA+ 在多并发不变量验证的严谨度、Lean 在多形式化验证的深度、setup-pstack 在多用户的可定制性均未在档案中明示。目前定位是"Cursor 官方 pstack 跨 Harness 严肃工程化移植先驱"，向跨 Harness 严肃工程化平台演进是合理路径。

## 风险/局限/泡沫点
- **6 Harness 适配层兼容性:** 6 Harness（Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent）适配层在多 Harness 版本的兼容性未在档案中明示
- **poteto-mode 调派准确性:** poteto-mode 在多任务（bug fix / feature / refactor / test）的调派准确性未在档案中明示
- **TLA+ 严谨度:** agent-formal-verify TLA+ model checking 在多并发不变量验证的严谨度未在档案中明示
- **Lean 深度:** Lean 形式化验证的深度未在档案中明示
- **how/why/architect/fix/rerun 覆盖广度:** 工作流在多 bug 类型的覆盖广度未在档案中明示
- **setup-pstack 可定制性:** setup-pstack 模型默认 / reasoning effort per role 在多用户的可定制性未在档案中明示
- **arena runners 优化:** arena runners opus @xhigh fable @max 在多 benchmark 的优化效果未在档案中明示
- **shared installation 扩展性:** docs/reference.md#shared-skills-installation 在多 Harness 的扩展性未在档案中明示

## 与同类项目的关系
- **vs Cursor 官方 pstack:** Cursor 官方 pstack 仅服务 Cursor；michael-denyer/pstack-claude 跨 6 Harness
- **vs wshobson/agents:** wshobson/agents 是跨平台 Agent 插件市场；michael-denyer/pstack-claude 是单 skill stack 跨 Harness 严肃工程化移植
- **vs Anthropic Skills:** Anthropic Skills 仅服务 Claude；michael-denyer/pstack-claude 跨 6 Harness
- **vs OpenAI Codex Skills:** Codex Skills 仅服务 Codex；michael-denyer/pstack-claude 跨 6 Harness
- **vs addyosmani/agent-skills:** addyosmani/agent-skills 是 production-grade engineering skills for AI coding agents；michael-denyer/pstack-claude 是 Lauren Tan pstack 严肃工程化移植

## 是否值得持续跟踪
**值得跟踪（Cursor 官方 pstack 跨 Harness 严肃工程化移植方向）。** pstack-claude 代表了 Cursor 官方 pstack 严肃工程化 Agent workflow 的跨 Harness 移植诉求，无论其本身成败，这一方向是行业趋势。建议关注：6 Harness 适配层在多版本的兼容性、poteto-mode 在多任务的调派准确性、TLA+ 在多并发不变量验证的严谨度、Lean 在多形式化验证的深度、setup-pstack 在多用户的可定制性。对 Cursor pstack 用户 / 跨 Harness Coding Agent 用户，这是 Cursor pstack 严肃工程化移植方案的实用选择，值得评估采用。对跨 Harness 严肃工程化观察者，它是"Cursor pstack 跨 Harness 移植"赛道的头部样本。

## 后续观察点
- 6 Harness（Claude Code / Codex / Pi / OpenCode / Gemini CLI / Prime Agent）适配层在多 Harness 版本的兼容性
- poteto-mode 在多任务（bug fix / feature / refactor / test）的调派准确性
- agent-formal-verify TLA+ model checking 在多并发不变量验证的严谨度
- Lean 形式化验证在多实际 bug 的深度
- how/why/architect/fix/rerun 工作流在多 bug 类型的覆盖广度
- setup-pstack 模型默认 / reasoning effort per role 在多用户的可定制性
- arena runners opus @xhigh fable @max 在多 benchmark 的优化效果
- shared installation docs/reference.md 在多 Harness 的扩展性

---
> 数据来源: GitHub API (2026-10-06) | Stars: 1,405 | Forks: 152 | License: MIT | 语言: JavaScript | 创建: 2026-05-26