---
category: 平台候选
date_added: '2026-04-07'
emoji: 👥
github_url: https://github.com/tycrek/oh-my-claudecode
mcp: false
poc_recommend: false
score: 56
stars_per_day: 7832
summary: 以团队为原子的 Multi-Agent 编排平台，多 Provider 路由 + 流水线自愈。
tech_stack: TypeScript
title: oh-my-claudecode
total_stars: 17.6k
---

# oh-my-claudecode

> Teams-first Multi-agent orchestration for Claude Code

## 基本信息

- **仓库：** [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
- **Star：** 25,133
- **本周新增：** 7,832
- **语言：** TypeScript
- **许可：** MIT
- **归档状态：** 活跃

## 核心定位

在 Claude Code 上构建**团队化多 Agent 编排**。用户定义角色（executor、reviewer、architect），系统执行 `team-plan → team-prd → team-exec → team-verify → team-fix` 流水线。底层支持 Claude / Codex / Gemini 三路并发，通过 tmux 分屏真实启动子进程。

## 技术亮点

1. **团队即编排单元**：以"团队"而非"Agent"为原子，更符合工程直觉
2. **多 Provider 路由**：Claude + Codex + Gemini 并行，结果由 Claude 合成
3. **流水线自愈**：`team-fix` 循环确保任务不静默失败
4. **Marketplace 插件机制**：Claude Code 原生插件安装，工程化程度高
5. **多种执行模式**：Team（推荐）、Autopilot、Ultrawork、Ralph

## 关键争议

- **与 Claude Code 官方能力的关系**：Claude Code 官方正在引入原生 Teams 功能（`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`），一旦官方能力追平，oh-my-claudecode 的差异化价值会快速稀释
- **平台绑定风险**：严重依赖 Claude Code 的内部 API 和插件机制

## 架构启发

以"团队"为原子的设计模式值得在企业内部 Copilot 平台中借鉴。这种设计让复杂任务可以自然地拆解为多个角色的协作，而非在一个 Prompt 里堆叠复杂指令。

## 评分

| 维度 | 得分 | 理由 |
|------|------|------|
| 热度质量 | 9 | 7832/week，极速增长 |
| 技术创新度 | 7 | 编排模式有创新，具体技术基于现有组件 |
| 工程成熟度 | 8 | Marketplace、文档、Discord 社区完备 |
| 架构启发价值 | 8 | 团队化抽象对内部门平台有直接参考价值 |
| 企业落地潜力 | 6 | 依赖 Claude Code，企业内部定制化成本高 |
| 中期趋势概率 | 8 | Multi-Agent 是真实方向 |
| 平台化潜力 | 7 | 平台依赖是双刃剑 |
| 基础设施潜力 | 5 | 偏工具而非基础设施 |
| **总分** | **58/80** | |

## 归类

**平台候选 | 持续跟踪**

## 关联项目

- `oh-my-codex` — 同作者的 Codex 版本
- `hermes-agent` — 不同路径的 Agent 编排

---

*首次记录：2026-04-07*
