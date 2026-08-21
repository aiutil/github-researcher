---
title: "iii"
slug: "iii"
date_added: "2026-06-03"
category: "平台候选"
emoji: "🏗️"
stars: "17.5K stars"
stars_delta: "+1.5K/week, Rust 引擎 + 多语言 SDK"
language: "Rust"
score: 83
tags: ["service-composition", "observability", "rust", "agent-runtime", "worker-pattern"]
url: "https://github.com/iii-hq/iii"
last_seen_date: "2026-06-03"
---

# iii

## 一句话定位
服务组合/扩展/实时观测平台——Worker/Function/Trigger 三原语统一开发面，零集成，Agent 可在运行时动态扩展系统能力。

## 它解决的问题
后端开发中，每个新能力（队列、定时任务、HTTP 端点、可观测性、Agent）都需要独立集成。iii 将所有能力统一为 Worker/Function/Trigger 三个原语，新能力通过 `iii worker add` 接入。

## 为什么值得关注（2026-06-03）
- **17.5K stars**，Rust 引擎 + 多语言 SDK（Node/Python/Rust）
- **三原语抽象**简洁有力：Worker（进程）→ Function（工作单元）→ Trigger（触发条件）
- **Agent 可动态扩展**：Agent 在运行时发现缺少某个能力时，可以自己 `iii worker add` 添加
- **零集成实时可观测**：所有 Worker/Function 自动可追踪
- 预构建 Worker 生态：[workers.iii.dev](https://workers.iii.dev/)

## 热度来源判断
- 「零集成」承诺击中后端开发痛点
- Agent 运行时扩展能力的概念新颖
- Rust 性能保障 + 多语言 SDK 覆盖面广

## 关键技术亮点亮点
1. **Worker/Function/Trigger 三原语**：统一所有后端能力的抽象模型
2. **Agent 可编排**：Agent 用同一套接口发现和调用 Function
3. **实时可观测**：所有调用自动 trace，无需额外集成
4. **SDK 多语言**：Node.js/Python/Rust 三端支持
5. **iii-console**：开发运维控制台，Worker/Function/Trigger 全可视

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | iii 定位为后端能力组合/扩展/可观测平台，通过 Worker/Function/Trigger 三原语统一 HTTP、队列、定时、Agent 等入口，将调度与可观测内置在引擎中（Rust 引擎 + Node/Python/Rust SDK + iii-console 控制台 + workers.iii.dev 预构建生态） | 边界与原语仅来自档案引用的公开资料；具体持久化、部署形态与多语言 SDK 范围须源码核验 |
| 主路径 | 外部请求或 Agent 命中 Trigger → 调度到所属 Worker 内的 Function 执行 → 自动埋点进入 iii-console/Live Catalog → Agent 通过 Catalog 发现并在运行时 `iii worker add` 扩展新 Worker | 协议、传输、状态写回机制未在档案中证实，路径细节待核验 |
| 关键权衡 | (1) Agent 自主 `iii worker add` 带来的能力膨胀与权限失控风险；(2) Elastic License 2.0 对引擎商业使用的限制；(3) 三原语抽象对 Kubernetes/Dapr/Temporal 已覆盖场景的差异化收益尚需生产验证；(4)「零集成可观测」对已有埋点体系的侵入程度 | 权衡判断基于项目定位描述与风险段落，未引用任何基准或生产案例数据 |
| 最小 PoC | 用单一 HTTP Worker + 一个 Function 暴露内部接口，接入 iii-console 验证自动 trace，再让 Agent 通过 Catalog 调用该 Function，最后尝试 `iii worker add` 一个新 Worker 验证动态扩展；验收项应包含 License 边界、退出路径、调用链完整性与最小权限 | 许可证条款原文、SDK 实际可用语言与 console 自托管方式均待核验 |

## 架构启发

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
graph LR
    Client["外部请求 / 调度方"] --> T1["Trigger: HTTP/Queue/State 等<br/>(待核验: 协议与队列实现)"]
    Agent["AI Agent"] -->|"发现/调用"| Cat["Live Catalog<br/>workers.iii.dev 生态"]
    Agent -->|"iii worker add"| Risk["风险边界: 运行时动态扩展<br/>(待核验: 权限与审计)"]
    T1 --> W1["Worker A: HTTP API<br/>(Rust 引擎)"]
    W1 --> F1["Function: handler"]
    W2["Worker B: Queue/Schedule"] --> F2["Function: process"]
    W3["Worker C: Agent 接入"] --> F3["Function: decide"]
    Cat --> F1
    Cat --> F2
    F1 --> Console["iii-console<br/>自动 trace / 可观测"]
    F2 --> Console
    F3 --> Console
    Engine["Rust 引擎 + 多语言 SDK<br/>(Node/Python/Rust, 其余待核验)"] -.托管.-> W1
    Engine -.托管.-> W2
    Engine -.托管.-> W3
    License["外部边界: Elastic License 2.0<br/>商业使用受限"] -.约束.-> Engine
```

**架构师启发：**
1. 三原语模型可以简化微服务架构的服务注册/发现
2. Agent 运行时扩展能力是一个有趣的方向——Agent 不只是调用工具，还能扩展平台本身
3. 零集成可观测的承诺如果兑现，可以大幅降低 DevOps 复杂度

## 定位判断
**平台候选。** 如果三原语模型被验证有效，可以成为后端开发的新范式。但目前仍需验证大规模场景下的可行性。

## 风险/局限/泡沫点
1. **Elastic License 2.0（引擎部分）**——商业使用受限
2. 17.5K stars 增速快，但真实生产案例较少
3. 「零集成」承诺需要验证——现实中的集成往往比预期复杂
4. 与 Kubernetes/Docker Compose 等编排工具的定位重叠
5. 「Agent 可扩展平台」概念新颖但可能导致不可控的系统膨胀

## 与同类项目的关系
- **Kubernetes**：编排层，iii 更偏应用层的组合抽象
- **Temporal/Inngest**：工作流引擎，iii 用更轻量的 Trigger 模型
- **Dapr**：类似的多语言运行时，iii 更简洁

## 是否值得持续跟踪
**是。** 三原语模型和 Agent 运行时扩展是有意思的架构创新，值得观察。

## 后续观察点
1. 生产环境案例和规模验证
2. Worker 生态的丰富度（workers.iii.dev 增长情况）
3. Agent 动态扩展能力的实际使用场景
4. 引擎 License 是否会调整

---

*档案创建于 2026-06-03 · 数据截止 2026-06-03 06:00 CST*
