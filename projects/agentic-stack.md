---
title: "Agentic Stack"
slug: "agentic-stack"
date_added: "2026-04-30"
last_seen_date: "2026-08-11"
category: "基础设施候选"
emoji: "🧳"
stars: "2,218 stars"
stars_delta: "4个月2.2K，稳步增长"
language: "Python"
license: "Apache-2.0"
score: 79
tags: ["agent-portability", "memory", "skills", "interoperability", "coding-agent", "harness", "data-layer"]
url: "https://github.com/codejunkie99/agentic-stack"
---

# codejunkie99/agentic-stack — 跨 Agent 的便携记忆与技能层

## 一句话定位
一个可移植的 `.agent/` 文件夹（记忆 + 技能 + 协议），插入 Claude Code、Cursor、Windsurf、OpenCode、OpenClaw、Hermes、Codex、Gemini CLI 等 12+ 种 Coding Agent 后保持知识不丢失——切换工具不重置 Agent 的工作方式。

## 它解决的问题
2026 年 Coding Agent 生态高度碎片化：Claude Code、Cursor、Windsurf、Codex、Gemini CLI 等各有独立的记忆/技能/配置体系，互不兼容。开发者切换 Agent（或同时使用多个）时，之前的记忆（学到的项目约定、错误教训、偏好设置）和技能（自定义指令、工作流）全部丢失，需要从零重建。这是 **"Agent 数据可移植性"** 的核心痛点——类似于换手机时通讯录不同步的痛苦，但在 Agent 场景下更严重（知识积累是 Agent 价值的核心）。agentic-stack 提供一个**跨 Harness 的标准数据层**：一个 `.agent/` 文件夹承载所有 Agent 的记忆、技能和协议，任何兼容的 Agent 都能读写，实现"一个大脑，多个身体"。此外还提供本地数据看板（监控多个 Agent 的活动、token 成本、KPI）和飞轮机制（将运行记录转化为可复用的 trace/eval/training 数据）。

## 为什么值得关注（2026-08-11）
- **Stars:** 2,218，4 个月稳步增长
- **Forks:** 273，社区参与度高
- **Watchers:** 15
- **License:** Apache-2.0，商用友好
- **活跃度:** created 2026-04-15，pushed 2026-08-06，持续高活跃
- **版本迭代快:** 已到 v0.19.1，功能持续扩展（bounded loops、brain memory、mission control 等）
- **规模:** 7,939 KB，含大量文档和示例
- **兼容性广:** 支持 12+ 种主流 Agent Harness

## 热度来源判断
热度来自 **"Agent 碎片化痛点 × 跨平台解决方案 × 迭代速度快"** 的组合。Coding Agent 是 2026 年最热赛道，但每个 Agent 自建封闭生态——开发者苦"切换成本高"久矣。agentic-stack 是第一个系统化解决"Agent 数据可移植性"的项目，切中真痛点。273 forks 说明不少用户在二次定制。迭代速度（4 个月到 v0.19，含 bounded agentic loops、data layer、flywheel 等高级功能）显示投入力度大。热度**真实且方向正确**——但能否成为事实标准取决于生态采用率，若各 Agent 平台不主动支持 `.agent/` 格式，项目可能停留在"适配层"而非"标准层"。

## 关键技术亮点
1. **便携 `.agent/` 文件夹:** 记忆（lessons/preferences）+ 技能（skills/protocols）+ 配置统一存储，Agent 无关
2. **12+ Harness 兼容:** Claude Code、Cursor、Windsurf、OpenCode、OpenClaw、Copilot CLI、Gemini CLI、Hermes、Codex、Antigravity 等全覆盖
3. **Bounded Agentic Loops (v0.19):** 便携 loop 契约，maker → 确定性 verifier → 独立 checker 生命周期，支持 Git worktree 隔离、有限预算、deny-path 门控、可恢复检查点
4. **本地数据层:** 监控多 Agent 活动面板——harness 活动、cron 运行、token/成本估算、KPI 汇总、截图级日报
5. **飞轮机制:** 将已批准、脱敏的运行记录转化为本地制品——trace 记录、context cards、eval cases、training-ready JSONL、readiness metrics
6. **Memory 桥接 (v0.18):** Brain memory bridge，跨 Harness 共享学到的"经验教训"
7. **Mission Control (v0.17):** 任务管理和 lesson retraction 机制
8. **安全升级:** `agentic-stack upgrade` 支持项目安全升级，处理路径变更

## 架构启发
agentic-stack 的核心启发是 **"Agent 的价值在于积累的知识，而非执行的环境"**——正如开发者的价值在于技能而非用哪个 IDE。当前 Agent 生态正在重蹈移动应用的覆辙：每个平台建封闭生态，数据不互通。agentic-stack 试图建立 **Agent 数据的"通用文件系统"**，类似 POSIX 之于操作系统——让上层应用（Agent）和底层数据（记忆/技能）解耦。更深层的启发是其**飞轮设计**：将 Agent 运行数据自动转化为 eval cases 和 training JSONL，形成"用得越多→数据越好→Agent 越强"的正循环，这是从"工具"向"平台"演进的关键路径。

## 定位判断
**基础设施候选。** 若 `.agent/` 格式被广泛采用，它将成为 Agent 生态的"数据标准层"——类似 `.git` 之于版本控制。但与 git 不同的是，它需要各 Agent 平台主动配合（读写 `.agent/` 文件夹），这对平台厂商缺乏激励（封闭生态是护城河）。因此更可能的定位是"跨平台适配工具"而非"标准协议"——除非有强大的社区共识推动标准化。数据层和飞轮机制增加了平台化可能性。

## 风险 / 局限 / 泡沫点
- **标准采用不确定:** 各 Agent 平台缺乏动机支持第三方标准，可能推出自己的跨设备同步
- **兼容性维护成本高:** 12+ Harness 各自迭代，持续适配是巨大工程负担
- **性能开销:** 代理层可能引入额外延迟或资源消耗
- **安全风险:** 跨 Agent 共享记忆可能泄露敏感信息（如 API key 习惯）
- **单人维护:** codejunkie99 个人项目，可持续性取决于作者投入和社区贡献
- **竞争加剧:** wshobson/agents 等项目也在做跨平台 Agent 能力，可能分流

## 与同类项目的关系
- **vs wshobson/agents:** 跨平台插件集合（能力分发）；agentic-stack 跨平台数据层（记忆/技能持久化），互补但部分重叠
- **vs Anthropic Skills:** 官方标准但仅服务 Claude；agentic-stack 是跨平台的超集适配
- **vs MCP (Model Context Protocol):** MCP 是工具调用协议；agentic-stack 是数据/记忆层，正交关系
- **vs OpenAI Codex CLI 配置:** 单平台配置；agentic-stack 做跨平台抽象
- **vs skills.sh 生态:** skills.sh 是技能分发平台；agentic-stack 包含技能管理但更偏记忆层

## 是否值得持续跟踪
**值得跟踪（高优先级）。** Agent 数据可移植性是被忽视的关键问题，agentic-stack 是该方向的先行者。无论其本身成败，"Agent 记忆跨平台同步"是确定性需求。建议关注其是否被任何主流 Agent 平台官方采纳（决定性信号），以及飞轮机制的实际效果。

## 后续观察点
1. 是否有任何主流 Agent 平台（Claude Code/Cursor/Codex）官方支持 `.agent/` 格式
2. Bounded loops 功能的安全性和实际使用效果
3. 飞轮数据（eval cases、training JSONL）是否被用于实际模型训练或微调
4. 是否推出独立的数据看板 Web 产品（从 CLI 向 SaaS 演进）
5. 社区贡献的技能/记忆模板生态是否形成

---
> 数据来源: GitHub API (2026-08-11) | Stars: 2,218 | Forks: 273 | License: Apache-2.0 | 语言: Python | 创建: 2026-04-15
