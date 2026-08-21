---
title: "no-mistakes"
slug: "no-mistakes"
date_added: "2026-06-28"
last_seen_date: "2026-06-28"
category: "工具型"
emoji: "🛡️"
stars: "3,790 stars"
stars_delta: "周增 1,744（日均 ~249）"
language: "Go"
score: 82
tags: ["git-safety", "ai-validation", "code-quality", "agent-workflow", "pre-push", "ci"]
url: "https://github.com/kunchenguid/no-mistakes"
---

# no-mistakes

## 一句话定位
git push 和远程仓库之间的 AI 验证防护门——在 disposable worktree 中跑完验证流水线，全绿才放行。

## 它解决的问题
AI Coding Agent 产出代码速度快但质量不可控。直接 push 到 origin 会引入未验证的代码——测试没跑、lint 没过、文档没更新。传统 CI 在 push 之后才检查，已经太晚了。no-mistakes 在 push 之前做验证，类似"本地前置 CI"。

## 为什么值得关注（2026-06-28）
- 周增 1,744 stars，在 Agent 安全治理赛道中增速最快
- 用 Go 编写，单二进制部署，工程品质高
- 核心设计精妙：disposable worktree 不阻塞开发者工作
- 与 Claude Code/Codex/Copilot 等 Agent 深度集成（/no-mistakes skill）
- 填补了 Agent 工作流中"验证环节"的空白

## 热度来源判断
真实需求驱动。AI Coding Agent 产出量暴增，代码质量把控成为瓶颈。开发者需要一种不降低速度的质量保障机制。no-mistakes 的"非阻塞 + AI 验证"模式精准命中这个需求。

## 关键技术亮点亮点
1. **Disposable worktree 隔离：** 在独立的 git worktree 中做验证，开发者可以继续在原分支工作。验证完成后 worktree 被丢弃。这是非常精妙的架构选择。
2. **分级处理策略：** 安全的机械修复（formatting/import/lint）自动修复；涉及意图的问题升级给人类。这比全自动化或全人工都更合理。
3. **Agent-native 设计：** `/no-mistakes` skill 让 Coding Agent 自己触发验证流程，无需人类切换工具。
4. **多入口：** git push（命令行）、TUI（交互界面）、/no-mistakes（Agent skill）三种触发方式。
5. **Fork 友好：** 支持 `--fork-url` 让贡献者验证后再推到上游。

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 本地 git push 与远程仓库之间、由 disposable worktree 隔离驱动的一次性验证层，触发入口含 git push 命令行、TUI、`/no-mistakes` Agent skill 三种 | 入口清单见档案；后端 LLM 供应商、验证流水线具体步骤、远程触发协议未在档案中给出 |
| 主路径 | 开发者主分支保持工作 → 触发入口拉起 disposable worktree → 在 worktree 中编排验证流水线（机械修复 vs 人工升级 两级）→ 全绿才放行 push，结果回写主流程 | disposable worktree 与分级策略来自档案；具体编排器、状态存储、消息协议未给出 |
| 关键权衡 | 验证深度 vs 开发者等待时间：选 disposable worktree 保证非阻塞，但深度审查（并发/性能/安全）超出其能力 | 验证深度有限、Agent 验证者可靠性、Go 二进制本地安装门槛均在档案风险段列出 |
| 最小 PoC | 单仓库单分支安装 Go 二进制，启用 git push 钩子触发，TUI 复核默认验证流水线，确认分级策略（自动 fix vs 人工升级）行为符合预期，再扩展到 `--fork-url` 贡献流程 | PoC 步骤仅为架构师速览建议，真实流水线条目与默认规则集尚需源码核验 |

## 架构启发
no-mistakes 的核心启发是"验证左移 + 非阻塞"：
- 传统 CI 是 push 后验证（post-push）→ 错误已经在远程
- no-mistakes 是 push 前验证（pre-push）→ 错误在本地拦截
- 用 disposable worktree 做到非阻塞 → 开发者不等待

这种模式可以推广到更多场景：pre-merge 验证、pre-deploy 验证、pre-release 验证。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    Dev[开发者主分支工作区] --> Trigger{触发入口}
    Trigger -->|git push| Hook[git push 钩子]
    Trigger -->|TUI| UI[TUI 交互入口]
    Trigger -->|/no-mistakes skill| AgentSkill[Agent Skill 入口]
    Hook --> Orch[验证编排器]
    UI --> Orch
    AgentSkill --> Orch
    Orch --> WT[Disposable Worktree 隔离层]
    WT --> Pipe[验证流水线<br/>含机械自动修复 / 意图升级两级]
    Pipe -->|全绿| Allow[放行 push]
    Pipe -->|未通过| Block[拦截并升级给人类]
    Allow --> Remote[远程 origin 仓库]
    Block --> Dev
    Pipe -.->|调用| Agent[AI Coding Agent 验证者<br/>待核验]
    Agent -.->|供应商| LLM[外部 LLM 供应商<br/>待核验]
    Orch -.->|日志| Audit[审计/状态日志<br/>待核验]</mermaid>
```

## 定位判断
在 Agent 工具链中处于 L3 编排/治理层。不是 CI 的替代品，而是 CI 的补充——更前置、更轻量、更 Agent 友好。

## 风险 / 局限 / 泡沫点
1. **验证深度有限：** 真正复杂的问题（并发 bug、性能回归、安全漏洞）不是 pre-push 阶段能发现的。
2. **Agent 依赖：** 需要 AI Agent 做验证，Agent 本身可能犯错。验证者的可靠性是被验证者的前提。
3. **采用门槛：** 团队需要统一工作流才能发挥价值。个人开发者可能觉得"多此一举"。
4. **Go 二进制 + 本地 git：** 需要本地安装，不如云端方案易部署。

## 与同类项目的关系
- **vs 传统 CI（GitHub Actions/GitLab CI）：** 传统 CI 是 post-push，no-mistakes 是 pre-push。互补关系。
- **vs Husky/pre-commit hooks：** pre-commit hooks 做格式/lint 检查，no-mistakes 做 AI 驱动的深度验证。不同层级。
- **vs OpenSpec：** OpenSpec 从规格出发约束 Agent（上游），no-mistakes 从验证把关 Agent 产出（下游）。可以组合。

## 是否值得持续跟踪
**是。** Agent 安全治理是新兴赛道，no-mistakes 的 disposable worktree 模式有架构创新性。建议每两周跟踪一次。

## 后续观察点
1. 企业团队采纳案例——是否有人在中大型团队全面推广
2. 验证流水线的可扩展性——是否支持自定义验证步骤
3. 与 CI 系统的集成深度——是否能在 GitHub Actions 中复用验证逻辑
4. Agent 自动修复的成功率——多少比例的问题被自动修复 vs 升级给人类

---
*首次记录：2026-06-28*
