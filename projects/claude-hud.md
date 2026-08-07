---
title: "jarrodwatts/claude-hud"
slug: claude-hud
date_added: 2026-07-20
last_seen_date: 2026-08-07
category: "工具型"
emoji: "⌨️"
stars: "27,208 stars"
score: 78
tags: ["anthropic", "claude", "claude-code", "cli", "plugin", "statusline", "typescript"]
url: "https://github.com/jarrodwatts/claude-hud"
---

# jarrodwatts/claude-hud

## 一句话定位
Claude Code 的状态显示插件——在终端状态栏（statusline/HUD）实时展示 Agent 正在做什么：上下文用量、活跃工具、运行中的子 Agent、todo 进度，让 Claude Code 这一强大的终端 Agent 的执行过程从"黑盒"变为"透明可见"，解决 Agent 运行时缺乏可视化的体验痛点。

## 它解决的问题
Claude Code 是 2026 年最火的终端编程 Agent，但它有一个体验短板：执行过程高度黑盒化。当 Agent 在工作（调用工具、运行子任务、消耗上下文），用户只能盯着终端等待，不清楚它进展到哪、还剩多少上下文预算、是否卡住。这种"黑盒等待"引发焦虑，也降低了对 Agent 的信任与掌控感。claude-hud 直击这一痛点：它作为 Claude Code 插件，在终端底部状态栏实时渲染关键信息——上下文 token 用量条、当前激活的工具、并行运行的子 Agent 数量、todo 列表完成度。解决的是 **"Agent 执行过程不可见导致的焦虑与失控感"**，是 Agent 可观测性在终端 UI 层的实用化。

## 为什么值得关注
- **Stars:** 27,208（截至 2026-08-07），7 个月突破 2.7 万，增速很快
- **Forks:** 1,264，社区参与高
- **Watchers/Subscribers:** 36
- **Open Issues:** 20，维护良好
- **License:** MIT
- **语言:** JavaScript/TypeScript
- **活跃度:** created 2026-01-02，pushed_at 2026-08-04，持续迭代
- **规模:** 2.9MB，轻量插件
- **生态:** Claude Code 插件生态的代表性项目

## 热度来源判断
claude-hud 的热度是 **"Claude Code 生态红利 × 真实体验痛点 × 可视化刚需"** 驱动。Claude Code 2026 年用户基数庞大（最火 Coding Agent），任何提升其体验的插件都有巨大潜在受众。"执行黑盒"是 Claude Code 用户公认痛点——长任务时不知进度、不知上下文是否快耗尽。claude-hud 用直观状态栏解决此事，切中刚需。热度**真实**——2.7 万 stars 对应的是大量 Claude Code 用户的实际采用。需注意的是，作为生态附属插件，其生命周期高度依赖 Claude Code：若 Claude Code 官方内置类似 HUD 功能，这个插件的独立价值将受冲击。

## 关键技术亮点
1. **状态栏（Statusline）渲染:** 在终端底部常驻渲染 HUD 信息，不干扰主交互区
2. **上下文用量可视化:** 实时显示已用/剩余 token，带进度条，让用户预判"上下文快满了"
3. **活跃工具追踪:** 显示 Agent 当前正在调用的工具（读文件/运行命令/搜索），消除"它在干嘛"的疑惑
4. **子 Agent 监控:** 若 Claude Code 启用子 Agent（并行任务），HUD 显示其数量与状态
5. **Todo 进度:** 将 Agent 的 todo 列表渲染为可视化进度，让长任务的阶段清晰可见
6. **TypeScript 实现:** 轻量、类型安全，与 Claude Code 插件机制契合

## 架构启发
claude-hud 的核心启发是 **"Agent 越强大，可观测性 UI 越重要"**。传统 CLI 工具是"用户主动操作"，过程天然可见；而 Agent 是"用户委派、Agent 自主执行"，过程变成黑盒。Agent 的自主性越强，用户对"它在做什么"的焦虑越高。claude-hud 证明：**Agent 时代，状态可视化（HUD/statusline）从"锦上添花"变为"必需品"**。这与自动驾驶汽车需要仪表盘、AI 训练需要 TensorBoard 同理——任何自主系统都需要让人类监督者看见状态。更深层的启发是：Agent 的可观测性 UI 会成为一个独立的细分品类（Agent Observability UI），claude-hud 是终端场景的早期代表。

## 定位判断
**工具型插件（Claude Code 生态增强）。** claude-hud 是 Claude Code 生态的优秀增强插件，定位清晰：让 Agent 执行过程可见。它本身不创造"智能"，而是提升"使用体验与掌控感"。作为插件，其价值高度依赖 Claude Code 生态存续——Claude Code 兴则它兴。2.7 万 stars 显示它已是 Claude Code 插件生态的头部项目之一。不会独立成为平台，但在 Claude Code 生态内有稳固位置。最大风险是官方化（Claude Code 内置 HUD）。

## 风险/局限/泡沫点
- **官方化风险:** Claude Code 官方若内置状态栏/HUD 功能，插件的差异化急剧缩小
- **强依赖 Claude Code:** Claude Code 的 API/插件接口变化会直接影响插件可用性
- **功能单一:** 专注状态显示，扩展空间有限（但这也是其聚焦优势）
- **终端渲染限制:** 终端 UI 能力有限，复杂可视化不如 Web 仪表盘
- **竞争:** 其他 Claude Code 状态类插件可能分流
- **Agent 演进风险:** 若未来 Agent 交互范式变化（如语音/全屏 GUI），终端 statusline 价值下降

## 与同类项目的关系
- **vs Claude Code 内置功能:** 若官方增加 statusline，本插件可能被吸收；目前是补充
- **vs 其他 Claude Code 插件:** 专注"可观测性"细分，与功能类插件（代码审查、部署）互补
- **vs LangSmith/Langfuse（Agent 追踪）:** 那些是 Web 端深度追踪平台；claude-hud 是终端轻量实时 HUD
- **vs tmux/screen statusline:** 通用终端状态栏；claude-hud 专精 Claude Code 语义
- **vs Hermes TUI dock（widget）:** 类似理念——为 Agent 运行时提供可视化 widget，不同平台

## 是否值得持续跟踪
**值得跟踪（Claude Code 用户必备，Agent 可观测性样本）。** 对 Claude Code 重度用户，claude-hud 几乎是推荐安装——它显著降低长任务的等待焦虑。建议关注：Claude Code 官方是否内置类似功能（决定插件存亡）、是否扩展到其他 Agent（Codex/Gemini CLI 的 HUD 版）、以及 Agent 可观测性 UI 这一品类的整体演进。对 Agent 工具链设计者，claude-hud 是"终端场景 Agent HUD"的优秀参考实现。

## 后续观察点
- Claude Code 官方是否推出原生 statusline（官方化威胁兑现与否）
- 是否扩展支持其他 Coding Agent（Codex CLI/Gemini CLI 的 HUD）
- 可视化信息维度的扩展（成本/美元追踪、错误率、工具调用历史）
- Agent 可观测性 UI 是否成为独立品类（Web 版 HUD 出现）
- 企业团队采用（多人协作中共享 Agent 状态的需求）

---
> 数据来源: GitHub API (2026-08-07) | Stars: 27,208 | Forks: 1,264 | License: MIT | 语言: JavaScript/TypeScript | 创建: 2026-01-02
