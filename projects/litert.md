---
title: "LiteRT"
slug: "litert"
date_added: "2026-04-08"
category: "基础设施"
emoji: "⚡"
stars: "2k+"
stars_delta: "+500/day"
language: "C++"
score: 62
tags: ["Edge AI", "端侧推理", "Google", "TensorFlow Lite", "GenAI"]
url: "https://github.com/google-ai-edge/litert"
---

# LiteRT

## 一句话定位

TensorFlow Lite 的官方继任者——Google 面向端侧 ML 和 GenAI 推理的高性能运行时框架。

## 它解决的问题

将机器学习模型部署到边缘设备（手机、手表、IoT）是 AI 工业化的关键瓶颈。TensorFlow Lite 虽然曾是事实标准，但在 LLM 时代面临：

1. **大模型支持不足**：TFLite 设计面向小模型，无法高效运行数十亿参数的 LLM
2. **生成式 AI 缺失**：缺少对 Transformer decoder、KV Cache 等生成式推理的优化
3. **多硬件适配碎片化**：不同芯片（ARM、GPU、NPU）的适配逻辑分散

LiteRT 作为 TFLite 的继任者，从底层重新设计以解决这些问题。

## 为什么值得关注（2026-04-08）

LiteRT 已从实验项目进入**生产环境**：Chrome 浏览器、Pixel Watch、Android 系统均已集成。配合 Gemma-4 端侧部署和 google-ai-edge/gallery 示例应用，Google 正在构建完整的端侧 AI 推理栈。

+500/day 的增速虽然绝对值不大，但对于一个 C++ 基础设施项目来说非常罕见。

## 热度来源判断

- **Google 官方背书**：作为 TFLite 继任者，自带 Google 生态的推广资源
- **端侧 LLM 浪潮**：Gemma-4 等小模型使端侧 LLM 推理成为现实，催生对运行时的需求
- **生产验证**：Chrome + Pixel Watch 的生产部署证明了框架的可靠性

## 关键技术亮点

1. **Model Conversion Pipeline**：支持从 TensorFlow、PyTorch、JAX 等框架高效转换为 LiteRT 格式
2. **多后端运行时**：自动选择最优执行后端（CPU、GPU、NPU），开发者无需手动配置
3. **GenAI 优化**：针对 Transformer 架构优化，支持 KV Cache、Speculative Decoding 等生成式推理加速
4. **AOT 编译**：Ahead-of-Time 编译消除运行时开销，适合资源受限设备
5. **HuggingFace 集成**：通过 google-ai-edge/gallery 提供开箱即用的模型库

## 架构启发

LiteRT 的架构设计体现了 Google 在端侧 AI 上的长期思考：

- **统一运行时**：用单个运行时覆盖传统 ML 和 GenAI，避免碎片化
- **编译器 + 运行时分离**：Conversion Pipeline 负责优化，Runtime 负责执行，关注点清晰分离
- **Trade-off**：通用性 vs 性能——LiteRT 选择了通用性，通过多后端支持覆盖所有硬件，但单个后端的优化深度可能不如专用方案（如 ONNX Runtime 对特定硬件的优化）

## 定位判断

**基础设施层**。LiteRT 是端侧 AI 推理的底层运行时，类似于操作系统中的"虚拟机"角色。所有端侧 AI 应用都需要通过它来执行模型。

## 风险 / 局限 / 泡沫点

- **Google 控制风险**：作为 Google 内部项目，开源策略可能随时调整（TFLite 的教训）
- **与 ONNX Runtime 竞争**：微软的 ONNX Runtime 在企业端侧部署中已有较大份额
- **C++ 门槛**：对 Web/移动开发者来说，C++ 的贡献和学习门槛较高
- **Stars 数偏低**：2K stars 对于一个"基础设施"定位的项目来说偏低，社区生态尚未建立

## 与同类项目的关系

- **TensorFlow Lite**：LiteRT 的前身，正在被逐步替代
- **ONNX Runtime（微软）**：最大竞争对手，在企业端有更广泛的硬件支持
- **MLC-LLM**：Apache TVM 生态的端侧 LLM 推理方案，更偏学术
- **llama.cpp**：纯 CPU 端侧推理，更轻量但功能更少

## 是否值得持续跟踪

**关注端侧推理框架赛道。** LiteRT 本身的价值取决于 Google 的投入力度，但端侧 AI 推理是确定性趋势，值得跟踪整个赛道的演进。

## 后续观察点

1. **Chrome 集成深度**：Chrome 中 LiteRT 的使用场景是否从 ML 扩展到 GenAI
2. **HuggingFace 模型库**：gallery 中可用的模型数量和类型
3. **与 ONNX Runtime 的性能对比**：第三方基准测试结果
4. **社区增长**：Stars 增速是否能维持 +500/day

---

*首次记录：2026-04-08*
