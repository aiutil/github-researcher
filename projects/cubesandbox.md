---
title: "CubeSandbox"
slug: "cubesandbox"
date_added: "2026-04-25"
last_seen_date: "2026-07-13"
category: "基础设施候选"
emoji: "📦"
stars: "9,795 stars"
stars_delta: "从 7.1K→9.8K（周增 2.4K），v0.5 发布：AutoPause+Terraform+ARM64。CNCF Landscape 收录"
language: "Rust"
score: 88
tags: ["Sandbox", "AI-Agent", "Tencent", "Rust", "KVM", "E2B", "Runtime", "Security"]
url: "https://github.com/TencentCloud/CubeSandbox"
---

# CubeSandbox

## 一句话定位
腾讯云出品的即时、并发、安全的轻量级沙箱，专为 AI Agent 设计，Rust 实现。

## 它解决的问题
AI Agent 需要执行代码、访问文件系统、调用外部工具，但直接在宿主机上执行有安全风险。Docker 等传统沙箱启动慢、资源消耗大。Agent 需要一个轻量、即时、并发的隔离执行环境。

## 为什么值得关注（2026-07-04 更新）
Agent 沙箱是 Agent 从开发走向生产的关键基础设施。70 天内从 4.5K 增长到 7.1K，持续保持 Trending。新增 Snapshot/Clone/Rollback 功能、凭据保险库、Egress 控制。与 NVIDIA OpenShell 形成"腾讯 vs NVIDIA"的 Agent 安全沙箱双雄格局，两大巨头同时押注验证了赛道确定性。

## 热度来源判断
热度真实。腾讯背书 + Rust 实现 + Agent 安全刚需，三重驱动。Fork 数（250）与 Star 比例健康。

## 关键技术亮点亮点
1. **KVM+RustVMM microVM**：亚 60ms 冷启动（bare metal benchmark），<5MB 内存开销
2. **E2B SDK 兼容**：零代码改动迁移，swap 一个 URL 环境变量即可
3. **凭据保险库**：API keys 不进入沙箱/model context/logs，通过安全代理注入
4. **Snapshot/Clone/Rollback**：百毫秒级检查点，支持 fork 和回滚
5. **Web Console**：浏览器管理沙箱、模板、节点（:12088）
6. **模板系统**：OCI 镜像一键转模板，支持 Template Store

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 介于 Agent 调用入口与外部工具/凭据/网络之间的执行隔离层，自带 Web Console (:12088) 与 Template Store，前提是宿主提供 KVM | 基于档案 "KVM+RustVMM microVM" 与 "Web Console" 等标签与描述，未审计源码 |
| 主路径 | Agent 触发沙箱创建 → RustVMM/KVM microVM 冷启动（亚 60ms）→ 凭据保险库注入密钥 → 工具/代码在沙箱内执行 → Snapshot/Clone/Rollback 状态回写 | 性能数字仅来自 "bare metal benchmark"，E2B 兼容通过 "swap URL 环境变量" 实现，具体协议待核验 |
| 关键权衡 | 冷启动速度与 <5MB 内存开销 vs 必须依赖 KVM（x86_64 Linux）、与 NVIDIA OpenShell 的赛道竞争、腾讯维护投入波动风险 | 风险点来自档案 "风险/局限" 章节，非生产数据 |
| 最小 PoC | 单节点 x86_64 Linux 启用 KVM → 用 E2B SDK 替换 URL 环境变量接入 → 启用 AutoPause 与 ARM64（v0.5）→ 在 Web Console 验证 Snapshot/Rollback 与凭据保险库注入 | 凭据保险库与 Egress 控制机制细节、ARM64 实际可用性均需源码验证 |

## 架构启发
CubeSandbox 代表了 Agent Runtime 的隔离层。与 Docker（重隔离）、WebAssembly（语言限制）形成差异化定位：

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    Agent["Agent 调用入口"] --> Orch["CubeSandbox 编排层 (Rust)"]
    Orch --> MicroVM["KVM + RustVMM microVM<br/>亚 60ms 冷启动 / 待核验: 资源配额"]
    Orch --> Cred["凭据保险库<br/>API keys 不入沙箱 / 待核验: 注入协议"]
    Orch --> Snap["Snapshot / Clone / Rollback<br/>百毫秒级检查点 / 待核验: 持久化后端"]
    MicroVM --> Egress["Egress 控制 (v0.5)"]
    MicroVM --> Template["OCI 模板 → Template Store"]
    Orch --> Console["Web Console :12088<br/>沙箱/模板/节点管理"]
    subgraph External["外部边界"]
        E2B["E2B SDK 兼容<br/>通过 URL 环境变量切换"]
        NVD["NVIDIA OpenShell<br/>竞争项目"]
    end
    Orch --- E2B
    Orch -.竞争压力.-> NVD
    subgraph Risk["风险/控制边界"]
        KVMDep["宿主依赖: x86_64 Linux + KVM"]
        Tencent["腾讯维护投入波动"]
    end
    MicroVM --- KVMDep
    Orch --- Tencent
```

## 定位判断
基础设施候选。Agent 沙箱是 Agent Runtime 的核心组件，如果质量过关可能成为事实标准。

## 风险 / 局限 / 泡沫点
1. **腾讯开源维护风险**：腾讯开源项目历史上维护投入波动较大
2. **生产环境验证不足**：虽然有 SWE-Bench RL demo，但缺乏大规模生产案例
3. **需要 KVM 支持**：要求 x86_64 Linux + KVM，限制了部署场景（云 VM 需要 PVM 或嵌套虚拟化）
4. **与 OpenShell 的竞争**：NVIDIA 入局可能分流开发者注意力

## 与同类项目的关系
- **E2B Sandbox**：商业化的 AI Agent 沙箱，云服务模式
- **Modal**：Serverless 执行平台，可做 Agent 沙箱但更通用
- **gVisor**：Google 的容器沙箱，更重但更成熟

## 是否值得持续跟踪
是。Agent 沙箱是确定性基础设施需求，腾讯的投入增加了可信度。需要观察隔离性 benchmark 和社区活跃度。

## 后续观察点
1. 与 Docker/gVisor 的隔离性和性能对比 benchmark
2. 是否有非腾讯用户的生产环境使用案例
3. 是否支持 MCP 工具调用的沙箱化

---
*首次记录：2026-04-25*
