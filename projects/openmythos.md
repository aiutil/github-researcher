---
title: "OpenMythos"
slug: "openmythos"
date_added: "2026-04-30"
category: "学习型"
emoji: "🧬"
stars: "11.2k stars"
stars_delta: "12天11K，极高增速"
language: "Python"
score: 85
tags: ["transformer", "recurrent-depth", "moe", "claude", "architecture", "mla", "gqa"]
url: "https://github.com/kyegomez/OpenMythos"
---

# OpenMythos

## 一句话定位
基于公开论文理论重建 Claude Mythos 架构的开源实现 — Recurrent-Depth Transformer + Sparse MoE。

## 它解决的问题
大模型架构不透明。Anthropic 的 Claude 系列被广泛认为采用了创新的推理架构，但从未公开细节。OpenMythos 为研究者和工程师提供了一个可运行、可调试的理论参考实现。

目标用户：ML 研究者、架构师、对推理优化感兴趣的工程师。

## 为什么值得关注（2026-04-30）
- 12 天 11.2K stars，是本月增长最快的研究型项目
- 首次将 Recurrent-Depth Transformer 的概念推向社区实践
- 直接影响对推理基础设施未来设计的认知

## 热度来源判断
**真实需求 + 社区好奇心驱动**。Anthropic 的 Claude 在推理质量上与竞品明显不同，社区对"它到底怎么做到的"有强烈求知欲。OpenMythos 满足了这个需求。但需注意：star 增长中相当部分来自"围观"而非"使用"。

## 关键技术亮点亮点

1. **Recurrent-Depth Transformer (RDT)**：三层架构（Prelude → Recurrent Block × N → Coda），推理时计算深度可变。核心洞察：不是所有 token 都需要相同深度的计算。

2. **MLA / GQA 双注意力切换**：支持 Multi-Head Latent Attention（DeepSeek 风格 KV 压缩）和 Grouped Query Attention，可在配置中切换。

3. **Sparse MoE with Shared Experts**：路由专家 + 共享专家的混合 FFN，21B 活跃参数承载大模型能力。

4. **pip install 即可运行**：`pip install open-mythos` 即可实验，门槛极低。

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | OpenMythos 是 Python 项目，边界由 `pip install open-mythos` 入口、RDT 三层（Prelude→Recurrent Block×N→Coda）、可切换的 MLA/GQA 注意力、Routing+Shared Sparse MoE FFN 组成；宿主运行时为 Python ML 栈，扩展通过配置文件切换注意力变体 | 组件名/层级关系来自档案；具体模块文件、依赖清单与外部接口签名未在档案中给出，须源码核验 |
| 主路径 | 开发者或 CI 调用 CLI/Python API → 进入 RDT Core Loop（Prelude→循环 N 次的 Recurrent Block→Coda）→ 经稀疏 MoE FFN 与 MLA/GQA 注意力输出 → 回到调用方 | 流程基于档案"架构启发"图与 pip 入口描述；CLI 子命令、API 协议、序列化格式待核验 |
| 关键权衡 | 推理时变深度循环带来的尾延迟不确定性（循环上限）与准确率/算力成正比设计哲学之间的平衡，叠加"理论重建 vs 实际 Claude 架构"的认知风险 | 权衡描述直接取自档案；定量延迟、显存、训练成本基准未提供 |
| 最小 PoC | 在沙箱/CI 中 `pip install open-mythos`，用最小配置构造短序列，验证 RDT 循环次数上限切换与 MLA/GQA 路由，再以单元测试覆盖 Recurrent Block 的自适应计算分支 | 仅基于档案"pip install 即可运行"与架构师速览建议；具体测试样例、benchmark 套件、参考权重均待核验 |

## 架构启发

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
graph TB
    DEV["开发者 / CI 触发器"]
    CLI["CLI 或 Python API 入口<br/>(pip install open-mythos)"]
    CFG["配置开关<br/>MLA / GQA"]
    RDT["RDT Core Loop<br/>Prelude → Recurrent Block × N → Coda"]
    MOE["Sparse MoE FFN<br/>路由专家 + 共享专家"]
    ATT["注意力变体<br/>MLA(DeepSeek 风格 KV 压缩) 或 GQA"]
    ADAPT["自适应计算<br/>循环次数随问题复杂度变化(待核验上限策略)"]
    OUT["Output / 调用方返回"]
    EXT["外部边界<br/>Anthropic Claude Mythos 实际架构(未公开, 仅论文推测)"]
    RISK["风险边界<br/>无预训练权重 / 理论重建 vs 真实架构"]

    DEV --> CLI
    CLI --> CFG
    CFG --> ATT
    CLI --> RDT
    RDT --> MOE
    RDT --> ATT
    RDT --- ADAPT
    RDT --> OUT
    RDT -.对照.-> EXT
    RDT -.暴露.-> RISK
```

**设计哲学**：推理成本应该与问题复杂度成正比。这打破了"每个 token 固定计算量"的传统范式。

**Trade-off**：循环次数的上限需要平衡延迟和准确率。过高的循环次数会导致尾延迟不可控。

## 定位判断
**学习型 + 研究探索型**。目前不适合生产使用，但作为理解下一代 Transformer 架构的教学工具和实验平台，价值极高。

## 风险 / 局限 / 泡沫点

1. **理论重建 vs 实际架构**：完全基于公开论文推测，Anthropic 从未确认 Mythos 架构细节。实际实现可能截然不同。
2. **无预训练权重**：仅提供架构代码，无可用预训练模型。真正的验证需要完整训练流程。
3. **过度追捧风险**：社区可能将理论模型等同于 Anthropic 的实际做法，产生误导。

## 与同类项目的关系

| 项目 | 定位 | 差异 |
|------|------|------|
| DeepSeek-V3/R1 | 生产级 MoE 模型 | 有完整训练和权重，生产可用 |
| Mistral | 开源 MoE 模型 | 成熟产品，OpenMythos 是纯架构 |
| llama.cpp | 推理框架 | 聚焦推理优化，OpenMythos 聚焦架构设计 |

## 是否值得持续跟踪
**是，高优先级**。RDT 概念如果被验证，将改变推理基础设施设计。

## 后续观察点

1. 是否出现基于 OpenMythos 架构的实际预训练尝试
2. Anthropic 是否对 Mythos 架构做出任何公开回应
3. RDT 的推理效率 benchmark（与标准 Transformer 对比）

---
*首次记录：2026-04-30*
