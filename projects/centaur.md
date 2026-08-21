---
title: "Paradigm Centaur"
slug: "centaur"
date_added: "2026-06-06"
category: "平台候选"
emoji: "🐎"
stars: "718 stars"
stars_delta: "新建项目，首日记录 718"
language: "Python"
score: 82
tags: ["self-hosted", "agent-platform", "kubernetes", "slack", "team-agents", "sandbox", "workflows"]
url: "https://github.com/paradigmxyz/centaur"
---

# Paradigm Centaur

## 一句话定位
自托管团队共享 Agent 平台，Slack 原生交互 + K8s 隔离沙箱 + 持久工作流 + 凭据安全边界。

## 它解决的问题
团队使用 AI Agent 的三大痛点：每人本地跑一套浪费资源、Agent 拿到 API Key 有安全风险、对话状态不持久无法协作。

## 为什么值得关注（2026-06-06）
Paradigm（以太坊生态知名开发公司）出品的自托管 Agent 平台。核心创新是凭据边界（Credential Boundaries）：Agent 永远拿不到原始密钥，通过 iron-proxy 代理替换。这是企业级 Agent 安全的正确设计。

## 热度来源判断
- Paradigm 品牌（以太坊/Rust 生态）
- Slack 原生交互降低使用门槛
- 安全设计（沙箱 + 凭据隔离）直击企业痛点
- 718 stars + 116 forks = 活跃的早期社区

## 关键技术亮点亮点
1. **Slack 原生对话**：@mention 发起对话，线程级进度更新和结果回复
2. **K8s 隔离沙箱**：每个对话独立沙箱，default-deny NetworkPolicy，k3s 即可部署
3. **iron-proxy 凭据隔离**：Agent 只看到占位符字符串，真实凭据由 iron-proxy 在出站请求时替换到指定 host + header
4. **可插拔 Agent 引擎**：支持 Claude Code / Codex / Amp / 自定义 harness
5. **Python 工具插件**：工具是 Python 包，公共方法自动变为 API 端点
6. **持久工作流**：Python 函数 + durable steps，支持 sleep/resume/子 Agent/定时触发
7. **可重放状态**：Postgres 存储消息、执行、事件，客户端断线重连不丢结果

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Centaur 是自托管团队 Agent 编排层：入口为 Slack（@mention 发起线程式对话），Agent 引擎可插拔（Claude Code / Codex / Amp / 自定义），工具以 Python 包形式注册，状态由 Postgres 持久化；外部边界仅描述到 GitHub/Jira 一类出站服务。 | 仅档案明列的 Slack 入口、Python 工具插件、可插拔 harness 列表；未提及其他 IM、Web UI、API-first 入口——视为规划中而非已交付。 |
| 主路径 | Slack 线程 → Centaur API → 沙箱分配器 → K8s 沙箱内 Agent → Python 工具调用 → iron-proxy 凭据替换 → 外部服务；消息/执行/事件回写 Postgres，客户端断线重连可恢复。 | 主路径基于档案"关键技术亮点"1–7 条串联；具体消息协议、工具注册协议、Postgres schema 未在档案中描述。 |
| 关键权衡 | 核心权衡在 Agent 能力与凭据安全之间：iron-proxy 用 host+header 粒度做占位符替换以防密钥泄露，但代价是引入 K8s 运维负担（即使 k3s）与出站代理的额外一跳，同时 Agent 引擎可插拔带来版本/能力分散风险。 | 权衡仅为档案描述的设计选择；性能损耗、可观测性指标、具体 NetworkPolicy 规则未给出。 |
| 最小 PoC | 单 Slack 工作区 + k3s 单节点 + Postgres + iron-proxy，仅注册 1 个 Python 工具、1 个 Agent harness（Claude Code），验收项：占位符不出沙箱、线程级结果回写、对话中断后可重放。 | k3s 部署、Postgres 持久化、iron-proxy 替换逻辑可由档案支持；具体 helm chart、镜像、版本号——待核验。 |

## 架构启发

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    U["Slack 用户<br/>@mention 触发线程"] --> API["Centaur API<br/>编排入口"]
    API --> PG["Postgres<br/>消息/执行/事件<br/>可重放状态"]
    API --> SB["沙箱分配器"]
    SB --> K8S["Kubernetes 沙箱<br/>default-deny NetworkPolicy<br/>k3s 可部署 — 待核验"]
    K8S --> AGENT["可插拔 Agent 引擎<br/>Claude Code / Codex / Amp / 自定义"]
    K8S --> IP["iron-proxy<br/>凭据边界<br/>按 host+header 替换占位符"]
    AGENT --> TOOLS["Python 工具插件<br/>公共方法→API 端点"]
    TOOLS --> IP
    IP --> EXT["外部服务<br/>GitHub / Jira / …"]
    EXT -.占位符出站仅经 IP.-> K8S
    PG -.断线重连回放.-> U
```

**核心设计模式：凭据边界**
传统方式：把 API Key 放到 Agent 环境变量 → Agent 可以泄露密钥。
Centaur 方式：Agent 环境只有占位符（如 `OP_SERVICE_ACCOUNT_TOKEN`），iron-proxy 拦截出站请求，按 host + header 精确替换。Agent 用服务但不接触密钥。

## 定位判断
**平台候选。** 自托管团队 Agent 平台的早期参考实现。安全设计领先，但运维门槛较高。

## 风险 / 局限 / 泡沫点
1. **K8s 依赖**：虽然 k3s 降低了门槛，但仍然是运维复杂的选择
2. **Paradigm 维护优先级**：Paradigm 核心业务是 Web3，此项目可能非战略优先
3. **Slack 绑定**：当前只有 Slack 入口，缺少 Discord/飞书/企业微信支持
4. **早期阶段**：83 个 open issues 说明功能完善度有限
5. **中国落地的本地化障碍**：需要适配钉钉/飞书等国内 IM

## 与同类项目的关系
| 项目 | 定位 | 差异 |
|------|------|------|
| Odysseus (55.4K⭐) | 自托管 AI 工作空间 | 个人使用，非团队 Agent 平台 |
| n8n (191K⭐) | 工作流自动化 | 偏流程编排，非 Agent 沙箱 |
| Butterbase (1.3K⭐) | AI 原生 BaaS | 后端服务，非 Agent 平台 |

## 是否值得持续跟踪
**是。** 团队级 Agent 平台是企业 Agent 化的关键基础设施。凭据边界设计值得长期跟踪。

## 后续观察点
1. 是否出现非 Slack 的对话入口（Discord / Web UI / API-first）
2. 沙箱方案是否从 K8s 扩展到 microVM（如 forkd）
3. 工作流引擎的可靠性验证
4. 企业部署案例

---
*首次记录：2026-06-06*
