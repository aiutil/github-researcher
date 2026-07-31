---
title: "slvDev/esp32-ai"
slug: "esp32-ai"
date_added: "2026-08-01"
last_seen_date: "2026-08-01"
category: "观察型"
emoji: "🔧"
stars: "2,627 stars"
stars_delta: "7/23创建→8/01 2,627⭐"
language: "Python"
license: "MIT"
score: 83
tags: ["llm", "esp32", "edge-ai", "per-layer-embeddings", "microcontroller", "offline", "quantization"]
url: "https://github.com/slvDev/esp32-ai"
---

# esp32-ai — 28.9M 参数 LLM 跑在 8 美元 ESP32-S3 微控制器上

## 一句话定位
用 Google Per-Layer Embeddings 思路，把 28.9M 参数语言模型塞进 512KB SRAM 的 ESP32-S3（约 8 美元），靠把 25M 参数表留在 flash 实现 9.5 tok/s，完全离线运行。

## 它解决的问题
微控制器（如 ESP32-S3）只有 512KB SRAM，传统方法只能跑极小模型（此前同类芯片上最大的 LLM 仅 260K 参数）。本项目验证了：用 Per-Layer Embeddings 把不计算的参数留在慢速 flash，可以在几乎不增加 SRAM 占用的前提下把模型参数量提升 100 倍（260K → 28.9M）。

## 为什么值得关注（2026-08-01）

本周"边缘推理"趋势的核心洞察是"模型推理瓶颈是内存放置策略，而非算力"——colibri（744B MoE / VRAM-RAM-NVMe 三级）、deltafin（2.8T MoE / HTTP 流式）都在不同尺度验证这一点。esp32-ai 把这个范式推到了**物理极限**（512KB SRAM），用"把不计算的 embedding 表留在 flash、每 token 只读 ~450B"的方式证明：即使在最受限的硬件上，参数放置策略仍是关键变量。

## 热度来源判断
- **话题性成分显著**：2.6K⭐ 在很大程度上来自"把 LLM 跑上 8 美元芯片"的视觉冲击力（README 顶部有实物 GIF demo）。
- **技术诚实性是加分项**：作者在 README 明确声明模型仅能写 TinyStories 级别短故事，不能问答/指令/编码，且保留了参数计数 bug 的修正历史——这种诚实降低了"夸大宣传"的嫌疑，反而增强了技术可信度。
- **真实需求有限**：28.9M 模型的实际输出价值极低，热度主要来自架构启发性而非实用性。

## 关键技术亮点

1. **Per-Layer Embeddings 下沉到微控制器**：Google Gemma 3n/4 的 Per-Layer Embeddings 设计原用于手机/GPU，本项目建设性地把它适配到微控制器的内存布局（SRAM/PSRAM/Flash 三级）。25M 参数的 embedding 表留在 flash，每 token 只读约 6 行（~450B），"大部分参数从不被加载"。
2. **三级内存布局**：SRAM（512KB，快/小）放"思考核心"（每 token 实际计算的参数）→ PSRAM（8MB，中速）放输出头和工作内存 → FLASH（16MB，大/慢）放 25M 参数表。这和 colibri 的 VRAM/RAM/NVMe 三级是同一原理的不同尺度实现。
3. **端到端实测**：ESP32-S3，28.9M 参数，4-bit 量化后 14.9MB，端到端 ~9.5 tok/s（纯计算 9.7 tok/s），零网络连接。
4. **可复现的实验记录**：训练、消融、量化代码在 `src/` 和 `experiments/`，`RESULTS.md` 记录完整方法和芯片实测。作者特意保留了 commit 历史（含参数计数 bug 修正过程）。

## 架构启发
esp32-ai 与 MoE 专家按需加载是同一原理的两种表现：MoE 是"只加载激活的专家"，Per-Layer Embeddings 是"只读取被查询的 embedding 行"。两者的共同点是——**模型中大部分参数是"被查表"而非"被计算"的，因此可以放在慢速大容量存储，按需少量读取**。这个洞察对嵌入式 AI、离线设备、隐私敏感场景有结构性价值。

## 定位判断
在边缘推理范式家族中，esp32-ai 是**最极端的验证案例**：colibri（消费 GPU 级）、deltafin（单台 Mac 级）、quill（端侧 ASR 级）、esp32-ai（微控制器级）。它不代表可用的产品，而是验证了范式在物理极限下仍成立。归类为"观察型"——价值在架构启发而非工程复用。

## 风险 / 局限 / 泡沫点

1. **模型能力极有限**：训练于 TinyStories，只能写简单短故事，不能问答/指令/编码/掌握事实。作者明确声明这是能力边界而非推理速度的夸大。热度（2.6K⭐）不等于实用性。
2. **单人项目**：作者在 README 标注"Open to Work"，0 releases，firmware/training/ablation 全由一人完成（bus factor=1）。
3. **Per-Layer Embeddings 的普适性待验证**：该方法在 TinyStories 级模型上有效，但能否扩展到指令跟随模型尚不清楚——embedding 表的比例随模型规模和任务复杂度的变化关系未在本项目中探索。
4. **非生产代码库**：研究性 repo，不应作为嵌入式 AI 部署方案。

## 与同类项目的关系

- **vs colibri（21.2K⭐）**：colibri 是 744B MoE 在多 GPU 上跑（VRAM/RAM/NVMe 三级），esp32-ai 是 28.9M 在微控制器上跑（SRAM/PSRAM/Flash 三级）。同一"按需读参数"范式，尺度差 25,000 倍。
- **vs deltafin（553⭐）**：deltafin 把 2.8T MoE 的专家按需 HTTP 流式加载到单台 Mac；esp32-ai 把 embedding 表留在本地 flash。前者是"网络流式"，后者是"本地慢存储"。
- **vs llama2.c（Karpathy）**：作者明确致谢 llama2.c 是"让人相信可以用纯 C 跑 tiny 模型"的灵感来源。esp32-ai 在此基础上引入了 Per-Layer Embeddings 来突破 SRAM 限制。

## 是否值得持续跟踪
**有限跟踪。** 作为边缘推理范式家族的极端案例记录，但不预期它演变为生产项目。真正值得跟踪的是 Per-Layer Embeddings 思路是否被更大规模的端侧项目采纳。

## 后续观察点
1. **Per-Layer Embeddings 在指令模型上的可行性**：是否有人把这个思路用于能执行指令的模型（即使很小），而非仅 TinyStories 级。
2. **社区 fork 方向**：是否有人基于此 repo 扩展到其他微控制器或更大的模型规模。

---
*首次记录：2026-08-01*
