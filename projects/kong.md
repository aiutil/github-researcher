---
title: "Kong/kong"
slug: kong
date_added: 2026-06-04
last_seen_date: 2026-06-04
category: "平台候选"
emoji: "📦"
stars: "43,937 stars"
score: 56
tags: ["Lua", "api-gateway", "ai-gateway", "kubernetes", "microservices"]
url: "https://github.com/Kong/kong"
---

# Kong/kong

## 一句话定位
云原生 API 和 AI 网关，统一管理 API 流量、LLM 调用和 MCP 工具连接，支持插件扩展。

## 它解决的问题
微服务架构下，API 流量管理（路由、认证、限流、监控）需要一个统一的入口网关。随着 AI 应用普及，LLM API 调用管理（多模型路由、成本控制、缓存）成为新的网关需求。Kong 面向企业架构团队，提供了一个高性能、可扩展的 API/ AI 网关，通过插件架构覆盖了从传统 API 管理到 AI 推理代理的全场景。

## 为什么值得关注
- **Stars:** 43,937 stars，在 API 网关领域属于顶级开源项目
- **双轨战略:** 从传统 API 网关扩展到 AI 网关，覆盖了 AI 时代的新需求
- **企业级成熟度:** 创建于 2014 年，经过十余年生产验证，被大量企业采用
- **Lua/Nginx 高性能:** 基于 OpenResty（Nginx + LuaJIT），处理性能业界领先
- **云原生原生支持:** 深度集成 Kubernetes（Kong Ingress Controller）

## 热度来源判断
热度来自 API 网关作为微服务基础设施的刚性需求——几乎每个中大型企业都需要 API 网关。Kong 作为该领域的顶级开源方案，43K stars 是十年积累的稳定结果。新增的 AI 网关功能带来了新一轮关注——LLM API 管理、MCP 网关等能力踩中了 AI 基础设施建设的浪潮。

## 关键技术亮点亮点
1. **OpenResty/Nginx 高性能核心:** 基于 Nginx 事件驱动架构，单实例可处理数十万 QPS 的 API 请求
2. **Lua 插件系统:** 使用 Lua 编写插件，在请求处理管道的各个阶段（access、header filter、body filter）插入自定义逻辑
3. **AI 网关能力:** 支持 LLM API 代理（OpenAI、Anthropic、Azure 等）、请求缓存、Token 限流、多模型路由负载均衡
4. **MCP 网关:** 支持 Model Context Protocol 的网关代理，统一管理 Agent 工具调用
5. **多数据库后端:** 支持 PostgreSQL、Cassandra、Redis 等多种数据存储，适应不同部署规模

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Kong 是位于上游调用方、模型供应商、工具与数据源之间的流量编排与策略层，自身不提供模型或工具实现 | 基于 tags（api-gateway / ai-gateway / kubernetes）与档案"API/AI 网关"定位推断；其协议面与权威/未授权子集未在档案中给出 |
| 主路径 | 入站请求经 Nginx+OpenResty 核心与 Lua 插件管道处理，再被代理到上游 API、LLM 端点或 MCP 工具，状态与会话由所配置后端承担 | 路径上"数十万 QPS""插件阶段 access/header filter/body filter"来自档案亮点；QPS 数字未独立验证 |
| 关键权衡 | 在 OpenResty/Lua 的高性能与扩展速度 vs. 插件开发人才稀缺、集群运维复杂度上升之间取舍；同时承担传统 API 与 AI 流量会使插件与配置面迅速变大 | 权衡基于档案"Lua 门槛""部署复杂度""企业/社区版本差异"；版本功能差异未提供具体清单 |
| 最小 PoC | 用单一路由 + 一项鉴权/限流插件覆盖一条传统 API 链路，并复用同一网关开一条只读、低配额的 LLM 代理，日志与可观测性先于横向扩展上线 | PoC 所需 PostgreSQL/Redis 等依赖清单与 Kubernetes 控制器细节未在档案中核验 |

## 架构启发
Kong 的核心设计是「Nginx + Lua 插件」——利用 Nginx 的高性能事件循环作为核心，通过 Lua 插件系统实现灵活的功能扩展。这种架构的权衡是：获得了极致性能，但 Lua 语言相对小众，增加了开发门槛。近年 Kong 也在探索基于 Go 的数据平面（Kong 模式），以降低插件开发门槛。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    C[上游调用方或 Agent] --> I[入口与身份边界]
    I --> K[Nginx + OpenResty 内核与 Lua 插件管道]
    K --> A[传统上游 API]
    K --> L[LLM 端点 OpenAI Anthropic Azure 等 具体清单待核验]
    K --> P[MCP 工具与外部系统]
    K --> D[数据后端 PostgreSQL 或 Cassandra 或 Redis 选其一待核验]
    D --> K
    K --> O[日志 指标 审计]
    K --> R[企业版与社区版功能差异 待核验]
</mmid>
```

## 定位判断
属于 API 网关生态的第一梯队。与 APISIX（Apache，同为 OpenResty）、Tyk（Go）、Envoy（C++/代理）形成竞争格局。Kong 的差异化在于企业级成熟度和 AI 网关先发优势。

## 风险 / 局限 / 泡沫点
1. **Lua 语言门槛:** 插件开发需要掌握 Lua，对很多团队来说是小众语言，人才稀缺
2. **部署复杂度:** 完整的 Kong 集群部署需要数据库、DNS、证书管理等多个组件，运维门槛不低
3. **AI 网关竞争加剧:** 专精 AI 网关的新方案（如 Portkey、LiteLLM）在 AI 场景可能更轻量灵活
4. **商业化压力:** Kong 有商业版本，社区版和企业版的功能差异可能影响开源社区的信任

## 与同类项目的关系
- **Apache APISIX:** 同为 OpenResty 方案，直接竞品，在中国市场更强
- **Envoy + Istio:** 服务网格方案，功能覆盖更广但复杂度更高
- **Tyk:** Go 实现的 API 网关，更轻量但生态不如 Kong
- **LiteLLM:** 专注 LLM API 管理的开源代理，在 AI 场景更轻量

## 是否值得持续跟踪
**值得跟踪。** API 网关是基础设施的核心组件，Kong 向 AI 网关的扩展代表了基础设施适应 AI 时代的重要趋势。尤其需要关注其 AI 网关功能在实际企业中的采用情况。

## 后续观察点
- 关注 Kong AI 网关功能的企业采用案例和真实价值验证
- 观察与 APISIX 在全球市场和中国市场的竞争态势
- 跟踪 MCP 网关功能是否成为 AI Agent 基础设施的标准组件

---
> 数据来源: GitHub API (gh cli) | 更新: 2026-08-07 | Stars: 43,937 | Language: Lua | License: Apache-2.0 | Forks: 5,197
