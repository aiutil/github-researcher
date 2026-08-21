---
title: "superloglabs/superlog"
slug: "superlog"
date_added: "2026-06-11"
category: "平台候选"
emoji: "🔧"
stars: "875 stars"
stars_delta: "周+83"
last_seen_date: "2026-06-19"
language: "TypeScript"
score: 78
tags: ["observability", "opentelemetry", "clickhouse", "ai-agent", "self-healing", "incidents"]
url: "https://github.com/superloglabs/superlog"
---

# superloglabs/superlog

## 一句话定位
AI 原生可观测性平台：OpenTelemetry + ClickHouse + AI Agent 自愈，从信号聚合到根因分析到修复建议的闭环。

## 它解决的问题
传统可观测性工具的三大痛点：(1) 告警风暴让人疲劳；(2) 找到根因需要人工排查；(3) 发现问题后修复建议缺失。superlog 用 AI Agent 贯穿「发现问题→定位根因→修复建议」全链路。

## 为什么值得关注（2026-06-11）

1. **YC P26 背书** — 商业验证 + 资源支持
2. **AI-native 架构** — 不是在监控上加 AI 壳，而是从底层设计
3. **OpenTelemetry 原生** — 基于事实标准，可集成性强
4. **开源核心** — 社区版包含完整可观测性功能

## 热度来源判断
- YC 品牌效应 + 可观测性 + AI 自愈是真需求 + 技术栈现代
- 持续增长，非爆发式

## 关键技术亮点亮点
- **OTLP 原生** — 支持 traces/logs/metrics 统一接入
- **ClickHouse 查询引擎** — 海量遥测数据高性能查询
- **AI 事件聚合** — 将噪声信号自动聚合为事件
- **Agent Runner** — 可插拔的 AI 调查运行时
- **社区 Agent** — 默认 agent 自动记录事件摘要
- **Postgres 元数据** — 事件、配置等元数据存储

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | OTLP 入口 + ClickHouse 遥测存储 + Postgres 元数据 + AI Agent Runner 编排的 AI-native 可观测性平台；处于数据接入、聚合、推理三层之间的边界 | 组件基于档案明列（OTLP、ClickHouse、Postgres、AI 事件聚合、Agent Runner、社区 Agent）；Agent Runner 的协议与部署形态未在档案中描述 |
| 主路径 | OTLP 接入 → ClickHouse/Postgres 落库 → AI 事件聚合降噪 → Agent Runner 根因分析 → 修复建议/事件摘要输出 | 路径由档案「关键技术亮点」与「架构启发」图直接给出；具体查询语言、Agent 调用协议、对外 API 未证实 |
| 关键权衡 | AI 自愈差异化能力 vs 修复可靠性与权限风险；ClickHouse 高性能查询 vs 自托管运维门槛；开源核心获客 vs 与 Grafana/Datadog/SigNoz 的同质化竞争 | 权衡源自档案「风险/局限/泡沫点」与「与同类项目的关系」；市场份额与商业转化数据档案未提供 |
| 最小 PoC | 用 OTLP 单一 trace 信号源接入社区版，启用默认社区 Agent，在最小工具权限与可审计日志下验证事件聚合→根因→建议闭环 | PoC 范围仅基于档案已确认的「社区版含完整可观测性功能」「社区 Agent 自动记录事件摘要」；生产级权限模型、SLO 验收项未在档案中描述 |

## 架构启发

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    A[OTLP 接入<br/>Traces/Logs/Metrics] --> B[ClickHouse<br/>遥测存储]
    A --> C[Postgres<br/>元数据存储]
    B --> D[AI 事件聚合<br/>降噪]
    C --> D
    D --> E[Agent Runner<br/>可插拔 AI 调查运行时]
    E --> F[社区 Agent<br/>事件摘要]
    E --> G[修复建议<br/>待核验: 自动化程度与权限边界]
    subgraph 外部边界["外部依赖/边界"]
        A
        B
    end
    subgraph 风险边界["风险/控制边界"]
        G
    end
```

**启发 1：** AI-native 可观测性的核心不是展示更多数据，而是减少需要人看的数据。
**启发 2：** OpenTelemetry 是可观测性的 TCP/IP，基于 OTel 构建意味着天然的可集成性。
**启发 3：** Agent Runner 可插拔设计意味着 AI 调查能力可以持续进化。

## 定位判断
**平台候选。** 可观测性天然是平台生意，AI 自愈能力是差异化壁垒。

## 风险/局限/泡沫点
1. **AI 修复的可靠性** — 目前更偏辅助建议，离真正自动修复还有距离
2. **竞品密集** — Grafana/Datadog/New Relic 都在加 AI 能力
3. **ClickHouse 运维门槛** — 自托管需要 ClickHouse 运维能力
4. **商业模型待验证** — 开源核心 + 云版的模式在可观测性领域竞争激烈

## 与同类项目的关系
- **Grafana** — 竞品，Grafana 也在加 AI，但 superlog 是 AI-native
- **Datadog** — 竞品，Datadog 更成熟但更贵
- **SigNoz** — 同赛道，SigNoz 也是 OTel-native，但缺少 AI 自愈

## 是否值得持续跟踪
✅ 是。AI 原生可观测性是确定性趋势。

## 后续观察点
1. AI 修复建议的准确率和采纳率
2. 社区版功能与企业版差异化
3. 大规模部署案例
4. Agent Runner 生态（第三方 Agent 插件）
5. 与 Grafana 生态的竞合关系
