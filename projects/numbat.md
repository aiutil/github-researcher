---
title: "perplexityai/numbat"
slug: "numbat"
date_added: "2026-08-05"
last_seen_date: "2026-08-05"
category: "工具型"
emoji: "🦝"
stars: "684 stars"
stars_delta: "7/24创建→8/05观测 684⭐ / 68 fork / 5 subscribers，v0.1.2"
language: "Go"
license: "Apache-2.0"
score: 84
tags: ["agent-observability", "endpoint-security", "cel-rules", "forensics", "pre-action-blocking", "go", "perplexity", "audit"]
url: "https://github.com/perplexityai/numbat"
---

# perplexityai/numbat — 端点 AI agent 活动可观测性与取证

## 一句话定位
Perplexity 官方的单二进制端点 agent 可见性工具：通过本地 hooks/plugins、OTLP/HTTP 日志、磁盘会话产物三类输入，把十余个主流 agent 的活动归一到统一事件模型，用 CEL 规则引擎实时检测，支持可选 pre-action 阻断和事后取证重建。

## 它解决的问题
目标用户是需要在企业端点（macOS/Linux/Windows）上部署和审计多个 AI agent 的安全/平台团队。痛点：每个 agent（Claude Code、Codex、Gemini CLI、Copilot 等）都有自己的日志格式、会话存储位置、活动语义，企业无法统一回答"agent 在端点上做了什么、何时做的、是否触发了策略"。numbat 把这些异构来源归一到同一事件模型，提供统一检测、审计和（可选）阻断。

## 为什么值得关注（2026-08-05）

在 08-04 ratchet（执行约束）与 skill-recorder（技能提取）构成"agent 质量基础设施"两极之后，numbat 填补了第三个维度——**事后可追溯 + 事中可观测 + 可选阻断**。Perplexity 官方入场（非个人项目）提升了这个品类的公信力。它的覆盖矩阵列出 Claude、Codex、Gemini CLI、Copilot、OpenCode、Grok、Hermes、OpenClaw、Pi、Kimi Code、Qwen、Cline、Kiro、Crush 等**十余个 agent**——这是目前观察到的覆盖最广的 agent 可观测性工具。68 fork 说明已有部署尝试。

## 热度来源判断
- **真实需求信号**：684⭐ / 68 fork，fork/star ≈ 10%（健康，说明有人真在部署测试）。Perplexity 官方背书（非个人 hobby 项目）。Go 单二进制、Apache-2.0、无 cgo——部署门槛低。
- **品类时机信号**：agent 在企业端点的使用量正在增长（qm 11K⭐、Claude Code/Codex 等大规模采用），"agent 做了什么"的审计需求自然浮现。numbat 出现在这个需求上升期。
- **话题性成分**：subscribers 仅 5（相对 684⭐ 偏低），说明目前更多是"收藏/试用"而非"深度使用"——热度部分来自品类话题性。

## 关键技术亮点

1. **三类输入归一到统一事件模型**：本地 hooks/plugins（同步生命周期钩子或生成的 agent 插件/扩展）、OTLP/HTTP 日志导出器、磁盘会话产物（on-disk artifacts）。所有输入产生相同的归一化事件，使用相同的 CEL 规则引擎。这意味着 numbat 既能实时捕获（hooks/logs），也能对**未被 numbat 预先埋点的 agent 会话做事后取证重建**（读 on-disk artifacts）。
2. **CEL 规则引擎 + 多步序列规则**：内置 CEL（Common Expression Language）规则，支持多步序列规则（检测跨多步的可疑行为模式），以及自定义 YAML 规则。规则分 monitor-only（所有 shipped 规则）和 enforce（可选，需显式标记 `enforce: true`）。
3. **可选 pre-action 阻断（默认关闭）**：通过支持的同步 pre-action hooks 实现阻断。**关键设计决策：enforce 模式默认禁用，所有 shipped 规则为 monitor-only**——这是安全工具的谨慎姿态（先观测，不贸然阻断生产流）。
4. **版本化 NDJSON 记录 + JSON Schema**：事件、发现、执行决策、指标、扫描摘要均有版本化 NDJSON wire format，事件和发现保留 source references。密钥脱敏（redaction）——记录输出永远不含完整原始 transcript，原始证据文件加入 case bundle 是 opt-in。
5. **单二进制 + 跨平台**：macOS/Linux/Windows amd64/arm64，CGO_ENABLED=0 构建。`go install` 可装。

## 架构启发
numbat 的核心架构选择是 **"输入归一化 + 规则统一"**——不试图重新发明 agent 监控，而是把 agent 已有的可观测表面（hooks、日志、磁盘产物）统一到一个事件模型。这与传统 EDR（端点检测响应）对进程/文件/网络的做法同构，但针对的是 agent 活动。对架构师的启发：**当 agent 生态多极化（十余个 agent 并存），可观测性层必须格式无关**——针对单一 agent 的监控工具无法成为基础设施。

三层 agent 质量栈的成型：

| 层 | 项目 | 作用 | 时机 |
|----|------|------|------|
| 技能提取 | skill-recorder | 录屏→Skill | 事前 |
| 执行约束 | ratchet | 编辑后测复杂度、回灌 | 事中 |
| 可观测/取证/阻断 | numbat | 端点活动可见 + 可选阻断 + 事后追溯 | 事中+事后 |

## 定位判断
属于 **L2 开发范式/工具层**，是 agent 安全与可观测性品类。与 ratchet（执行时质量约束）、skill-recorder（技能提取）正交互补，共同构成 agent 工作流的质量基础设施。numbat 独特之处是**覆盖广度**（十余个 agent）和**事后取证能力**（从磁盘 artifacts 重建未被实时监控的会话）。

## 风险 / 局限 / 泡沫点

1. **生产成熟度早期**：v0.1.2，pre-action 阻断为设计声明（默认关闭，shipped 规则全为 monitor-only）。enforce 模式在真实生产流的误阻断风险未公开评测。
2. **覆盖矩阵为 docs 自述**：README/docs 列出十余个 agent，但每个 agent 的 hook/plugin 实现深度未逐一验证。"deferred"表示上游已知但未解析，"none"表示无可用上游表面——实际覆盖质量需逐项核实。
3. **subscribers 偏低**：5 subscribers（相对 684⭐），说明深度使用者尚少。热度部分来自品类话题性而非规模部署。
4. **依赖 agent 暴露的表面**：numbat 能观测的前提是 agent 暴露了 hooks/logs/on-disk artifacts。如果 agent 不暴露这些（如某些闭源/托管 agent），numbat 无法覆盖。
5. **forks 68 vs 5 subscribers 的解读**：高 fork 低 subscriber 可能意味着"很多人 clone 来试，但少有人深度跟踪"——需观察 fork 是否转化为 issue/PR 贡献。

## 与同类项目的关系
- **vs ratchet（423⭐）**：正交互补。ratchet 是 agent 编辑的**事中质量约束**（PostToolUse hook 测复杂度），numbat 是 agent 活动的**事中+事后可观测与可选阻断**。ratchet 强绑 Claude Code，numbat 覆盖十余个 agent——广度不同。
- **vs skill-recorder（1,751⭐）**：正交互补。skill-recorder 解决"技能从哪来"（人→Skill 提取），numbat 解决"agent 做了什么、能否追溯"。生命周期阶段不同。
- **vs 传统 EDR（CrowdStrike/SentinelOne）**：传统 EDR 观测进程/文件/网络，numbat 观测 agent 语义活动（工具调用、会话、决策）。是 agent 时代的 EDR 范式，但非替代传统 EDR。

## 是否值得持续跟踪
**是，作为"agent 可观测性/治理"品类的代表项目跟踪。** Perplexity 官方背书 + 覆盖十余个 agent 的广度是当前最强信号。重点验证覆盖矩阵的实际实现深度和 enforce 模式的生产可用性。

## 后续观察点
1. **覆盖矩阵的实现深度**：逐一核实 README/docs 列出的十余个 agent 的 hook/plugin 实际覆盖质量（哪些是完整 hook、哪些是 artifact 解析、哪些是 deferred）。
2. **enforce 模式的生产采用**：是否有企业报告 pre-action 阻断在生产流的误阻断率和可用性。
3. **是否会成为 agent 安全事实标准**：观察其他 agent（如 OpenClaw、Kimi Code）是否主动暴露 numbat 友好的 hooks/artifacts，形成正反馈。

---
*首次记录：2026-08-05* · *数据来源: GitHub API + 仓库 README/docs*
