---
title: "QwenAudio/qwen-audio-agent"
slug: qwen-audio-agent
date_added: "2026-08-02"
last_seen_date: "2026-08-02"
category: "平台候选"
emoji: "🎙️"
stars: "1,181 stars"
stars_delta: "7/27创建→8/02 1,181⭐，6天破千"
language: "JavaScript"
license: "Apache-2.0"
score: 84
tags: ["voice-agent", "realtime", "full-duplex", "acp", "multi-harness", "typescript", "javascript", "voice-ai"]
url: "https://github.com/QwenAudio/qwen-audio-agent"
---

# qwen-audio-agent — Agent 实时语音运行时

## 一句话定位
让 agent 持续在场、持续工作的实时语音运行时——全双工语音交互 + 自然打断 + 前台对话与后台任务并行，后台 Agent 经 ACP（Agent Communication Protocol）接入 OpenCode/Claude Code/Codex/Hermes/Kimi Code 等多 harness。

## 它解决的问题
目标用户是想给 agent 加"持续在场的实时语音"能力的开发者/团队。痛点：传统语音 agent 在 agent 查资料/调用工具/处理任务时整场对话暂停（用户陷入漫长等待）；现有 coding agent 主要是文本/IDE 交互，缺语音优先的交互形态。qwen-audio-agent 要解决的是"对话不该因后台任务而停"，让 agent 像真人助理一样边做边说。

## 为什么值得关注（2026-08-02）
在 qm 24h +250% 验证 harness 应用层进入主流的同时，qwen-audio-agent 代表应用层的**另一个产品形态——语音优先**。它与 qm（团队协同）、cindy（个人客户端）互补，共同构成应用层多形态矩阵。v1.0.0 已于 2026-07-30 发布（含内置 Gateway 的 macOS 桌面版），有正式 release 信号。

## 热度来源判断
- **真实需求信号**：Apache-2.0、有 CI（ci.yml badge）、有 npm 包、v1.0.0 正式版、9 个后台 Agent 接入矩阵——工程化程度高于一般 demo。fork 79 说明有集成尝试。
- **话题性成分**：语音 agent + ACP（新兴协议）是热点组合；"全双工 + 自然打断"对标 OpenAI Advanced Voice 等话题，传播性强。
- **待验**：语音质量（延迟、打断准确率、嘈杂环境）与后台任务可靠性需独立验证；依赖 DashScope API Key（百炼），非完全本地。

## 关键技术亮点

1. **全双工实时语音 + 自然打断**：用户可随时打断 agent 的播报，对话连续不暂停——这是语音 agent 的核心难点（VAD、回声消除、打断检测）。
2. **前台对话与后台任务并行**：能立即回答的直接答；需要工具/持续处理的交给后台 Agent，用户可随时追问进度或取消；任务完成后结果自然回到当前对话。这是把"语音交互"与"长任务执行"解耦的设计。
3. **ACP 多 harness 编排**：后台 Agent 经 Agent Communication Protocol 接入 OpenCode（原生 ACP/五星）、OpenClaw（内置 ACP 桥接）、Qoder/Kimi Code（原生 ACP）、Hermes/CodeBuddy/Codex/Claude Code（部分外部 ACP 适配/四星）。同一语音助理可调度多种 coding agent。
4. **多端形态**：WebUI、终端 TUI、macOS 桌面悬浮球；本地用户档案与跨会话个人记忆。

## 架构启发
核心启发是**"语音层与任务执行层解耦，经 ACP 桥接"**。qwen-audio-agent 不自建 coding 能力，而是把"语音在场"做成前台，把"任务执行"委托给后台已有的 harness——前台是 voice runtime，后台是多 harness 编排。这与 qm（把团队协同做前台、harness 做后台）是同一个"应用层编排底层 harness"模式的语音变体。ACP 作为协议层让前后台解耦，使语音层可独立演进。

```
[用户语音] → 全双工语音运行时（前台）
                ├── 能直接答 → 立即语音回答
                └── 需工具/长任务 → 后台 Agent（经 ACP）
                                      ├── OpenCode（原生 ACP）
                                      ├── Claude Code（外部适配）
                                      └── ...任务结果回到前台对话
```

## 定位判断
在 agent 生态分层中占据 **L5 应用产品层（语音形态）**。与 qm（团队协同）、cindy（个人客户端）并列，是应用层多形态矩阵的一极。定位为平台候选——若语音 + ACP 编排模式被验证，有成为语音 agent 运行时基础设施的潜力。

## 风险 / 局限 / 泡沫点

1. **依赖 DashScope API Key（百炼）**：非完全本地，语音能力依赖阿里云 DashScope；本地优先/隐私场景受限（对比 quill 的全本地）。
2. **v1.0.0 仅 3 天**：2026-07-30 发布正式版，语音质量、后台任务可靠性、长对话稳定性均需独立验证。
3. **9 个接入成熟度不一**：4 星（Codex/Claude Code 外部 ACP 适配）成熟度低于 5 星（OpenCode 原生 ACP）；多 harness 编排的稳定性依赖各 harness 的 ACP 实现质量。
4. **语音 agent 竞争激烈**：OpenAI Advanced Voice、各类语音 SDK 已多；qwen-audio-agent 的差异化（多 harness 编排 + 后台任务并行）是否构成护城河待观察。

## 与同类项目的关系
- **vs qm（4.8K⭐）**：qm 是文本团队协同（Slack/Web），qwen-audio-agent 是语音个人/在场助理；都属应用层但形态不同，经 ACP 都接入底层 harness。
- **vs quill（3.5K⭐）**：quill 是全本地 macOS 会议转录（单向录音→文本），qwen-audio-agent 是双向实时语音交互——方向相反。
- **vs OpenAI Advanced Voice**：Advanced Voice 是闭源模型能力；qwen-audio-agent 是开源运行时，可接入自选 harness，强调可编排性。

## 是否值得持续跟踪
**是，作为"应用层语音形态"代表跟踪。** 关注 ACP 多 harness 编排的稳定性、语音延迟/打断准确率的独立评测、以及是否脱离 DashScope 支持全本地。

## 后续观察点
1. **脱离 DashScope**：是否支持本地语音模型（ASR/TTS），降低对百炼的依赖。
2. **ACP 接入矩阵的稳定性**：9 个后台 Agent 接入里，4 星适配项（Codex/Claude Code）是否升到 5 星。
3. **语音质量评测**：是否有独立的全双工延迟、打断准确率、嘈杂环境鲁棒性评测。

---
*首次记录：2026-08-02* · *数据来源: GitHub API (gh CLI) + README 深度阅读*
