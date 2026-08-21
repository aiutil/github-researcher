---
title: "Block/Buzz"
slug: "block-buzz"
date_added: "2026-07-24"
category: "基础设施候选"
emoji: "🐝"
stars: "8,122 stars"
stars_delta: "日增 2,162 / 周数据待观察"
language: "Rust"
score: 90
tags: ["nostr", "human-agent", "collaboration", "self-hosted", "rust", "agent-protocol"]
url: "https://github.com/block/buzz"
---

# Block/Buzz

## 一句话定位
基于 Nostr relay 的 Human-Agent 协作通信平台——人类和 AI Agent 在同一频道工作，所有操作签名上链。

## 它解决的问题
当团队中有多个 AI Agent 时，现有协作工具（Slack、Discord、GitHub）的 Agent 集成都是外挂式 bot。Agent 没有一等公民身份，没有独立审计链，没有统一的身份和权限模型。团队不得不在 7 个 tab 之间切换：聊天、代码托管、CI 面板、发布工具、搜索索引……它们之间互不知情。

## 为什么值得关注（2026-07-24）
Block（原 Square）官方开源项目，首日 2,162 stars。这不是社区玩具——是有大公司工程团队背书的 Agent 协作底层协议。采用 Nostr（已被验证的去中心化协议）作为事件模型，把所有协作行为统一为签名事件。这是目前最认真尝试解决"Agent 时代协作工具应该怎么设计"的项目。

## 热度来源判断
- **真实需求驱动**：Agent 从单点工具走向团队协作场景是 2026 下半年的确定性趋势
- **Block 背书**：大型 fintech 公司的工程团队出品，不是个人项目
- **协议创新**：Nostr + Git Events (NIP-34) 的组合在协作领域是全新思路
- **非炒作型**：README 诚实标注功能成熟度（✅ Works today / 🚧 Being wired / 💭 Pending），没有过度承诺

## 关键技术亮点亮点
1. **统一事件模型**：消息、反应、代码审查、CI 结果、工作流审批、git 事件——全部是同一种 Nostr 签名事件。一种数据结构、一种身份模型、一条审计链
2. **Agent 身份 = 密钥对**：Agent 的权限由密钥对定义，和人类同事一样 scoped by identity。不是 permission flags，不是 API token
3. **buzz-cli（JSON in/JSON out）**：专为 LLM 工具调用设计的 CLI，支持 Goose / Codex / Claude Code 等 Agent harness
4. **Branch as Room**：Feature branch 自动创建协作频道，patch (NIP-34) / CI 结果 / review / merge decision 在同一房间
5. **YAML 工作流引擎**：消息/反应/调度/webhook 四种触发器，Agent 可执行编排
6. **搜索 = 事件查询**：对话、补丁、工作流运行、审批记录搜索合一，因为它们是同一种事件

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Block/Buzz 是一个自托管的 Nostr relay 协作层，把人类与 AI Agent 统一为签名事件的发布者；外部边界是 buzz-cli（对接 Agent harness）与 NIP-34 Git 事件源 | 档案明确列为基础设施候选、Rust、Nostr、self-hosted、agent-protocol；具体 relay 协议字段、加密方案、存储后端未在档案中证实 |
| 主路径 | 人类/Agent 用密钥对身份 → 在 relay 上签名发布事件（消息、patch、review、CI、审批）→ YAML 工作流引擎订阅并驱动 Agent 编排 | 仅档案中列出的六类事件、YAML 四类触发器、buzz-cli JSON-in/JSON-out 可证；review/merge 协议细节、调度实现未细化 |
| 关键权衡 | 用 Nostr + 统一签名事件换取跨工具审计与 Agent 一等公民身份，代价是自托管门槛高（Rust 1.88+/Node 24+/Docker/Hermit）、依赖单一公司维护、移动端缺失 | "Branch as Room"、Agent=密钥对、单核贡献者风险均有档案原文；具体性能、吞吐量、可扩展性指标档案未提供 |
| 最小 PoC | 单 relay + 单 Agent 密钥对 + buzz-cli 跑 NIP-34 patch/review 流，验证事件可签名可检索；关闭外部模型与多渠道，仅留 JSON 日志做审计回归 | 档案只承诺 "✅ Works today" 类功能可用；🚧/💭 项及生产部署形态须源码核验 |

## 架构启发
## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    Human["👤 人类<br/>密钥对 A<br/>(权限由密钥定义)"] -->|签名事件| Relay["📋 Nostr Relay<br/>Block/Buzz 自托管<br/>统一事件日志"]
    Agent["🤖 Agent<br/>密钥对 B<br/>一等公民身份"] -->|签名事件| Relay
    CLI["🖥️ buzz-cli<br/>JSON in / JSON out<br/>对接 Goose/Codex/Claude Code<br/>(状态/控制边界)"] -->|编排调用| Agent
    Git["🔧 Git 源<br/>NIP-34 patch / branch<br/>Branch as Room"] -->|git 事件| Relay
    WF["⚙️ YAML 工作流引擎<br/>触发器:消息/反应/调度/webhook"] -->|订阅事件| Relay
    Mobile["📱 iOS/Android 客户端<br/>Flutter — 待核验<br/>(风险边界)"] -.->|尚未发布| Human

    Relay --> Audit["🧾 审计链<br/>消息/反应/patch/CI/审批/工作流<br/>(风险边界: 单公司维护)"]
```

核心设计哲学：**一种协议、一种身份模型、一条事件日志**。不是集成了 7 个工具，是替代了 7 个工具的数据层。

## 定位判断
处于 **Agent 基础设施协议层**。如果 Human-Agent 协作成为主流工作模式（2026-2027 大概率事件），Buzz 定义的就是这个领域的"HTTP"——最基本的交互协议。

## 风险 / 局限 / 泡沫点
1. **开源阉割风险**：Block 内部版本预连接 Block relay 和 Agent provider，开源版需要自行搭建。存在"社区版 = 二等公民"风险
2. **自托管门槛高**：需要 Docker + Hermit + Rust 1.88+ + Node 24+，非一键部署
3. **Nostr 采用风险**：Nostr 在团队协作场景的采用仍属极早期，社区可能选择更传统的协议
4. **移动端缺失**：iOS/Android 客户端仍在开发中（Flutter）
5. **单公司依赖**：核心维护者几乎都来自 Block，bus factor 风险

## 与同类项目的关系
| 维度 | Buzz | Slack + Bot | Zed Collaboration |
|------|------|-------------|-------------------|
| Agent 身份 | 一等公民（密钥对） | 外挂 bot（token） | 编辑器内协作 |
| 事件模型 | Nostr 签名事件 | 私有 API | CRDT |
| 自托管 | ✅ 完全控制 | ❌ SaaS | ❌ 编辑器绑定 |
| Git 集成 | NIP-34 原生 | Webhook | 内置 |
| 审计链 | ✅ 事件日志 | 部分 | ❌ |

## 是否值得持续跟踪
**强烈建议持续跟踪。** 这是目前最认真的 Agent 协作底层协议项目。即使最终 Nostr 路线未被广泛采用，其设计思路（统一事件模型、Agent 一等公民身份、签名审计链）将深刻影响后续所有协作工具设计。

## 后续观察点
1. 移动端发布时间表及体验质量
2. 社区是否出现第三方 relay 托管服务（降低自托管门槛）
3. 非 Block 员工的核心贡献者数量变化
4. Agent harness 生态（Goose / Codex / Claude Code）的集成深度
5. 是否有企业 PoC 案例公开

---
*首次记录：2026-07-24*
