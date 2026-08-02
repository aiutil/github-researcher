---
title: "sqliteai/waste"
slug: waste
date_added: "2026-08-02"
last_seen_date: "2026-08-03"
category: "观察型"
emoji: "💽"
stars: "1,010 stars"
stars_delta: "7/28创建→8/02 652⭐→8/03 1,010⭐（+358），fork 53→89，v0.6.2 cgroup-aware budget"
language: "C"
license: "Apache-2.0"
score: 83
tags: ["kimi-k3", "moe", "local-inference", "nvme-streaming", "c", "dependency-free", "trillion-parameter", "streaming-tensor-engine"]
url: "https://github.com/sqliteai/waste"
---

# waste (WASTE) — 纯 C 零依赖跑全量 Kimi K3 2.78T 的推理引擎

## 一句话定位
WASTE（Weight-Aware Streaming Tensor Engine）——纯 C、零运行时依赖、可嵌入的推理引擎，在 64GB MacBook Pro 上跑**全量** Kimi K3（2.78 万亿参数，非蒸馏/非剪枝），把 trunk 驻内存、selected experts 直接从 NVMe 流式读取、剩余 RAM 做有界 expert cache。

## 它解决的问题
目标用户是在消费级硬件上运行超大 MoE 模型的研究者/极客。痛点：Kimi K3 完整权重 1.42 TB（转后 982 GiB），远超主流消费机内存，无法直接加载。waste 要解决的是"让一个 2.78T 模型在一台 64GB 消费机上跑起来"——不是蒸馏/剪枝，而是利用 MoE 每 token 仅激活约 4% 的特性，让 idle weight 不需要在内存、只需要"reachable in time"。

## 为什么值得关注（2026-08-02）
这是本周"超大模型本地推理"命题的**第三个独立实现**。deltafin（Python，589⭐）和此前追踪的 colibri（纯 C，744B，21K⭐）已分别给出 Python 与纯 C 路线；waste 是纯 C 路线里**首个瞄准万亿级 K3 单机消费硬件**的实现。三个独立团队、三种实现，使"推理瓶颈是内存放置策略而非算力"这一命题的验证不再依赖单一项目。

## 热度来源判断
- **真实需求信号**：Apache-2.0、fork 53、README 极其坦诚（明确自述"slow, 0.5 tok/s"、声明"未发现其他万亿级消费机磁盘流式公开演示"为"我们的搜索结果而非调研，无对比表，欢迎反例"）——这是研究性项目的诚实姿态，非营销。
- **话题性成分**："在 Macbook 上跑 2.78 万亿参数"的叙事有极强传播性；652⭐ 来自"把不可能变可能"的话题性。
- **价值定位**：作者明确把价值定位为"**可行性证明**"（万亿级可达单台消费机），而非"实用速度"（0.62 tok/s 是可用性下限）。

## 关键技术亮点

1. **Trunk 驻内存 + expert 磁盘流式 + RAM 有界 cache**：模型 trunk 保持在内存；每 token 需要的 selected experts 从 NVMe 直接读取（一个 expert = 一次读取）；剩余 RAM 全部用作 expert cache（有界）。实测命令显示 "expert cache 17.56 GB"，"experts 9038 hit / 14514 miss = 38%"。
2. **纯 C、零运行时依赖**：可嵌入。对比 deltafin（Python + 依赖），waste 追求极致的依赖控制与可移植性。
3. **作者自验对齐**：每层与 PyTorch 参考对齐，最终 logits 一致到 3.6e-06，vision tower 与自身 oracle 一致到 2.3e-06。**注意这是作者自验，非第三方独立复现。**
4. **多模型支持**：除 K3 2.78T，还跑 Kimi-Linear 48B（19 GiB 容器，1.87 GiB 最小 RAM，10.7 tok/s）。

## 架构启发
核心启发是 **"idle weight 不需要在内存，只需要 reachable in time"**。这与 colibri（VRAM/RAM/NVMe 三级）、esp32-ai（SRAM/PSRAM/FLASH 三级 + Per-Layer Embeddings）是同一原理家族的不同表现——**"推理瓶颈是内存放置策略而非算力"**。waste 的取舍是：trunk（高频访问）驻内存换速度，expert（低频/按需）放磁盘换容量，RAM 做 cache 桥接两者。作者诚实指出"两个看起来最大的杠杆（每 token 读更少字节、RAM 里放更多）都被榨干了，接下来是工程优化而非新原理"。

```
[模型权重 982 GiB]
   ├── trunk → 驻内存（高频）
   └── experts → NVMe 磁盘（按需，一个 expert = 一次读取）
                    ↑
              RAM 有界 expert cache（剩余空间，17.56GB）
              hit 9038 / miss 14514 = 38%
```

## 定位判断
在"超大模型本地推理"品类里，waste 与 deltafin（Python）、colibri（C）并立。waste 的差异化是**纯 C 零依赖 + 万亿级单机消费硬件**。定位为观察型——价值在可行性与工程启发，0.62 tok/s 尚不实用。与 colibri（744B 多 GPU、21K⭐）相比，waste 瞄准更大模型（2.78T）但单机，是规模/便携的不同权衡。

## 风险 / 局限 / 泡沫点

1. **0.62 tok/s 是可用性下限**：26 秒答一句话，价值在可行性证明而非日常使用。作者诚实承认，但**容易被读者误读为"K3 可日常本地跑"**——不能。
2. **自验非第三方复现**：logits 一致到 3.6e-06 是作者自报，未经独立团队复现；"未发现其他万亿级消费机磁盘流式公开演示"是作者的搜索结果，**非系统性调研，作者声明无对比表、欢迎反例**。
3. **需要 982 GiB 磁盘 + 64GB RAM**：模型容器 982 GiB，最低 RAM 29.05 GiB——仍是高门槛，非普通消费机。
4. **单点实现早期**：创建于 2026-07-28，5 天 652⭐，生产/长期维护承诺待验证。

## 与同类项目的关系
- **vs deltafin（589⭐，Python）**：同跑全量 K3，deltafin 用 Python + OpenAI 兼容 API server（易用/API 优先），waste 用纯 C 零依赖（极致依赖控制/可嵌入）。语言与策略分化。
- **vs colibri（21K⭐，C）**：同为纯 C 零依赖，但 colibri 跑 GLM-5.2 744B 多 GPU（VRAM/RAM/NVMe 三级），waste 跑 K3 2.78T 单机（trunk/expert 分离）。规模与便携性的不同权衡。
- **vs esp32-ai（2.7K⭐）**：esp32-ai 把 28.9M 跑上 8 美元微控制器（512KB SRAM），waste 把 2.78T 跑上 64GB Mac——同一原理（内存放置策略）的两个极端规模。

## 是否值得持续跟踪
**是，作为"超大模型本地推理三极"之一跟踪。** 关注其 expert cache 命中率优化、是否出现第三方对齐复现、以及能否从 0.62 tok/s 工程优化到"日常可用"速度（如 5+ tok/s）。

## 最近动态（2026-08-03）

- **持续放量**：652 → 1,010（+358），fork 53 → 89（+36）。纯 C 万亿级推理话题持续获得关注。
- **v0.6.2 发布**：cgroup-aware budget——按 cgroup limit 而非 host RAM 自动预算内存（"Size the automatic budget against the cgroup limit, not the host's RAM"）。这是容器化部署的工程改进。
- **K3 本地推理第四极出现**：FareedKhan-dev/kimi-k3-in-c（218⭐）用便携 C99 把 peak RSS 压到 8.24GB（waste 要求 ~64GB）。waste 不再是纯 C K3 推理的唯一实现，但两者在 Pareto 前沿占据不同点——waste 求接近可用速度（0.62 tok/s），kimi-k3-in-c 求内存下限（8.24GB / 32s·token⁻¹）。
- **判断**：score 82 → 83。品类成熟（四极并立）提升整体关注度，waste 作为"接近可用速度"的代表持续受益。

## 后续观察点
1. **expert cache 命中率优化**：当前 38%（9038/14514），命中率提升直接提速；关注作者的工程优化进展。
2. **第三方对齐复现**：logits 3.6e-06 一致性是否被独立团队复现，是验证可行性的关键。
3. **与 kimi-k3-in-c/deltafin/colibri 的 Pareto 前沿竞赛**：四极并立后，速度-内存-易用性前沿被多个实现探索。关注 waste 能否工程优化到 5+ tok/s（跨入实用性）。

---
*首次记录：2026-08-02* · *最近更新：2026-08-03（652→1,010，v0.6.2，score 83）*
