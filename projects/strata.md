---
title: "Niko1221/Strata"
slug: strata
date_added: "2026-10-07"
category: "基础设施候选"
emoji: "🖥️"
stars: "15616 stars"
stars_delta: "13 天 15616⭐ ⑂1331 fork/star 8.5%"
language: "C++"
license: "MIT"
score: 92
tags: ["strata", "niko1221", "qwen3-8-flash-next", "local-llm", "consumer-gpu", "rtx-5070", "rx-9070-xt", "12gb-vram", "24576-experts", "moe-offloading", "gpu-cpu-ram-ssd-tiering", "guess-and-check", "1-6x-speedup", "8192-token-chunks", "openai-compatible", "anthropic-compatible", "mcp-server", "claude-code", "llama-cpp", "ggml", "q2_0", "iq2_xs", "iq3_xxs", "iq3_s", "coder-91pct-swe-bench", "swift-1-5", "unsloth", "ud-iq4-xs", "ud-q4-k-xl", "orcarouter-uncensored", "thinking-effort", "images", "parallel-batching", "multi-gpu", "intel-arc", "strix-halo", "mit", "7-languages-readme", "19115kb", "13-days", "buy-me-a-coffee"]
url: "https://github.com/Niko1221/Strata"
---

# Niko1221/Strata

## 一句话定位
消费级显卡跑 Qwen3.8-Flash-Next 125B 模型的严肃工程化平台——把「本地 LLM 推理」从「24GB H100 / 双卡 A100 集群 + 闭源 SaaS」推到「Strata 引擎跨 GPU/CPU/RAM/SSD 分层调度 24576 experts（每 token 仅用 10 个）+ VRAM 持热点 + RAM 持全集 + SSD 持 lookup table + 处理器 兼用 + Coder 91% SWE-bench Verified + guess-and-check 1.6-1.8x + 8192 token 块读 1000+ tok/s + OpenAI/Anthropic/OpenAI Responses/MCP /v1 全兼容 + Claude Code ANTHROPIC_BASE_URL 直连 + 一键启动 START-HERE.bat / setup.sh + 7 语言 README + 多 GPU 协调 + docs/{INSTALL,MODELS,DETAILS,HOW_IT_WORKS,TROUBLESHOOTING,MCP_SERVER,AI_SETUP,BATCHING,COMMUNITY_BENCHMARKS,OLDER_GPUS,INTEL_ARC,STRIX_HALO,MULTI_GPU,paper/Strata-Paper.pdf}.md + buymeacoffee + MIT + C++ 19115 KB」（Niko1221 个人）。

## 它解决的问题
2026 年本地 LLM 推理赛道的痛点是 **「绝大多数本地 LLM 推理都是 24GB+ H100 / 双卡 A100 集群 + 闭源 SaaS + 单 OS + 单 API + 单语言 + 无文档严谨度承诺」**。Strata 直击这一痛点：把「本地 LLM 推理」从「24GB H100 / 双卡 A100 集群 + 闭源 SaaS」推到「RTX 5070 / RX 9070 XT 12GB+ 消费级 + Strata 引擎跨 GPU/CPU/RAM/SSD 分层调度 24576 experts + VRAM 持热点 + RAM 持全集 + SSD 持 lookup table + 处理器 兼用 + Coder 91% SWE-bench Verified + guess-and-check 1.6-1.8x + 8192 token 块读 1000+ tok/s + OpenAI/Anthropic/OpenAI Responses/MCP /v1 全兼容 + Claude Code ANTHROPIC_BASE_URL 直连 + 一键启动 + 7 语言 README + 多 GPU 协调 + docs 全 13 个 + buymeacoffee + MIT」严肃工程化形态。解决的是 **「消费级硬件本地 LLM 推理 + 跨 GPU/CPU/RAM/SSD 分层调度严肃工程化 + 跨 API 兼容 + 一键启动 + 多语言 README + 多 OS」** 的本地 LLM 推理严肃工程化问题。

## 为什么值得关注（2026-10-07）
- **Stars:** 15616（截至 2026-10-07），13 天 15616⭐，fork 1331，fork/star 8.5%
- **Forks:** 1331（典型高 fork 严肃工程化持续关注信号）
- **License:** MIT（明确许可，商用清晰）
- **语言:** C++
- **活跃度:** created 2026-09-24，pushed_at 2026-10-06，持续高活跃
- **规模:** 19115 KB
- **Topics:** 0 个覆盖（README 未明示）

## 热度来源判断
Niko1221/Strata 的热度是 **「消费级 12GB+ GPU 跑 125B 模型刚需 × Strata 引擎分层调度严肃工程化 × 多 README 语言 × 一键启动 × 三 API 兼容」** 的强劲组合。本地 LLM 推理是 2026 年最热赛道，但消费级硬件跑大模型是真痛点——大多数用户的 RTX 5070 / RX 9070 XT 12GB+ 无法承载 125B 模型的完整权重（80GB+）。一个把「24GB H100 / 双卡 A100 集群 + 闭源 SaaS」推到「消费级 12GB+ GPU + Strata 引擎分层调度 + guess-and-check + 三 API 兼容 + 一键启动」的严肃工程化平台自然爆火。1331 个 forks 反映社区高度参与——这正是「本地 LLM 推理严肃工程化」类项目的网络效应（贡献者越多，价值越大，吸引更多用户）。13 天 15616⭐ + fork/star 8.5% 说明这是真实严肃工程化信号（不是泡沫）。

## 关键技术亮点
1. **跨 GPU/CPU/RAM/SSD 分层调度 24576 experts（每 token 仅用 10 个）**——Qwen3.8-Flash-Next 是 MoE 125B，24576 个 experts；Strata 把热点 experts 放在 GPU VRAM，全集 experts 放在 RAM，lookup table 放在 SSD，处理器补齐余下
2. **guess-and-check 1.6-1.8x 加速**——小 helper 猜下一段词，大模型一次性检查，1.6-1.8x 加速语义保持
3. **三 API 兼容 + Claude Code ANTHROPIC_BASE_URL 直连**——OpenAI /v1 + Anthropic /v1/messages + OpenAI Responses /v1/responses + MCP /mcp 全部兼容；Claude Code `ANTHROPIC_BASE_URL=http://127.0.0.1:8080` 直连
4. **一键启动 + 7 语言 README + 13 个文档**——START-HERE.bat（Windows）/ setup.sh（Linux）+ docs/{INSTALL,MODELS,DETAILS,HOW_IT_WORKS,TROUBLESHOOTING,MCP_SERVER,AI_SETUP,BATCHING,COMMUNITY_BENCHMARKS,OLDER_GPUS,INTEL_ARC,STRIX_HALO,MULTI_GPU,paper/Strata-Paper.pdf}.md + 7 语言 README（English/简体中文/日本語/Deutsch/Français/Español/Português）
5. **多 GPU + 多模型 + 多硬件严肃工程化**——RTX 5070 / RX 9070 XT / RTX 3090 / 多 GPU 协调 + Coder / Swift 1.5 / Unsloth UD-IQ4_XS / UD-Q4_K_XL / OrcaRouter Uncensored IQ3_XXS 多模型 + Intel Arc / Strix Halo / older CPUs 实验性

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 消费级显卡（NVIDIA RTX 20/30/40/50 + AMD RX 7900/7800/7700/9060/9070/Radeon AI PRO R9700/RX 6800/6900 12 GB+ VRAM）跑 Qwen3.8-Flash-Next 125B 模型；Strata 引擎跨 GPU/CPU/RAM/SSD 分层调度 24576 experts | 仅基于 README 描述的 Strata 引擎分层调度 + 24576 experts + VRAM 持热点 + RAM 持全集 + SSD 持 lookup table + 处理器 兼用 + Qwen3.8-Flash-Next 125B + Coder 91% SWE-bench Verified + guess-and-check 1.6-1.8x + 8192 token 块读 1000+ tok/s + OpenAI/Anthropic/OpenAI Responses/MCP /v1 兼容 + Claude Code ANTHROPIC_BASE_URL 直连 + 一键启动 + 7 语言 README + 多 GPU + MIT；具体 Strata 引擎在多 125B 模型稀疏激活正确性、guess-and-check 语义保持、三 API 兼容完整度、MCP server 多 tool 的覆盖广度、Intel Arc / Strix Halo / older CPUs 实验性覆盖广度未在档案中明示 |
| 主路径 | 12GB+ VRAM GPU → Strata 引擎加载 Qwen3.8-Flash-Next 125B → 24576 experts 跨 GPU/CPU/RAM/SSD 分层调度（每 token 用 10 个）→ guess-and-check 1.6-1.8x 加速 → OpenAI /v1 + Anthropic /v1/messages + OpenAI Responses /v1/responses + MCP /mcp → Claude Code ANTHROPIC_BASE_URL 直连 → http://127.0.0.1:8080 | 主路径为档案语义抽象；具体 Strata 引擎分层调度算法、guess-and-check 加速语义保持、Claude Code ANTHROPIC_BASE_URL 直连可用性未在档案中讨论 |
| 关键权衡 | 消费级 12GB+ GPU vs 24GB H100 / 双卡 A100 集群 + 24576 experts 跨 GPU/CPU/RAM/SSD 分层调度 vs 单 GPU 持全集 + Coder 91% SWE-bench Verified vs full model + Swift 1.5 thinking 短时间 vs 长推理 + Unsloth UD-IQ4_XS/UD-Q4_K_XL vs IQ3_S 质量 + 8192 token 块读 1000+ tok/s vs 256 token 块 + 多 GPU 协调 vs 单 GPU 优化 + OpenAI/Anthropic 三 API 兼容 vs 单 API 优化 + 7 语言 README 国际化 vs 多语言输出 + buymeacoffee 商业化 vs 单 GitHub 严肃工程化 | 档案明示 Qwen3.8-Flash-Next 125B + ISTA-DASLab / UkisAI / Unsloth 压缩 + llama.cpp / ggml + Q2_0 / IQ2_XS / IQ3_XXS / IQ3_S / Coder / Swift 1.5 / Unsloth UD-IQ4_XS / UD-Q4_K_XL / OrcaRouter Uncensored IQ3_XXS + buymeacoffee + 7 语言 README；具体 Strata 引擎跨 GPU/CPU/RAM/SSD 分层调度在多 vendor 硬件的严谨度、guess-and-check 加速在多模型的语义保持、三 API 兼容在多 SDK 的兼容性未在档案中讨论 |
| 最小 PoC | 在 RTX 5070 (12 GB) 或 RX 9070 XT (16 GB) 上 git clone Niko1221/Strata + 双击 START-HERE.bat（Windows）/ ./setup.sh（Linux）+ 默认 Coder 模型 IQ3_S → http://127.0.0.1:8080 → Chat → 加载更长 32K prompt 验证 2650 tok/s reads → 设置 ANTHROPIC_BASE_URL=http://127.0.0.1:8080 在 Claude Code 上验证 OpenAI/Anthropic 兼容 → 试 MCP server → 验证 buymeacoffee | PoC 范围由档案「RTX 5070 / RX 9070 XT 12GB+ + Qwen3.8-Flash-Next + 24576 experts + guess-and-check + OpenAI/Anthropic/MCP 兼容 + Claude Code ANTHROPIC_BASE_URL 直连 + 一键启动」建议推导；具体分层调度算法严谨度、OpenAI/Anthropic/OpenAI Responses 三 API 兼容完整度、Intel Arc / Strix Halo 严肃工程化承诺未在档案中讨论 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[用户] --> Installer[一键启动<br/>START-HERE.bat / setup.sh]
  Installer --> GPU[GPU: RTX 5070 12GB+<br/>RX 9070 XT 16GB+<br/>RTX 3090 24GB]
  Installer --> CPU[CPU: Ryzen / 任何 GPU 卡]
  Installer --> RAM[RAM: 32-64 GB+]
  Installer --> SSD[SSD: ~80 GB NVMe]
  GPU -.加载热点.-> Strata[Strata 引擎<br/>Qwen3.8-Flash-Next 125B]
  RAM -.加载全集.-> Strata
  CPU -.补齐余下.-> Strata
  SSD -.加载 lookup.-> Strata
  Strata --> Expert24576[24576 experts<br/>每 token 用 10 个]
  Expert24576 -.VRAM 持热点.-> VCache[VRAM 热点 experts]
  Expert24576 -.RAM 持全集.-> RCache[RAM 全集 experts]
  Expert24576 -.SSD 持 lookup.-> SCache[SSD lookup table]
  Expert24576 --> Guess[猜&检查 1.6-1.8x<br/>8192 token 块读 1000+ tok/s]
  Guess --> Chat[http://127.0.0.1:8080<br/>Chat + Monitor + About]
  Guess --> API1[OpenAI /v1<br/>base URL 兼容]
  Guess --> API2[Anthropic /v1/messages<br/>Claude Code ANTHROPIC_BASE_URL]
  Guess --> API3[OpenAI Responses /v1/responses<br/>Codex CLI]
  Guess --> MCP[MCP server<br/>AI tools install/start/stop]
  Chat -.Browser.-> User
  API1 -.Apps.-> Apps[Apps<br/>任何 OpenAI 兼容应用]
  API2 -.Apps.-> CC[Claude Code<br/>ANTHROPIC_BASE_URL=http://127.0.0.1:8080]
  API3 -.Apps.-> CX[Codex CLI<br/>OpenAI Responses]
  MCP -.Apps.-> AITools[AI Coding Tools]
  GPU -.NVIDIA.-> Sidecar[NVIDIA + AMD 双 vendor]
  GPU -.AMD.-> Sidecar
  Strata -.Coder.-> Coder[Coder 91% SWE-bench<br/>fits 32 GB]
  Strata -.Swift.-> Swift[Swift 1.5<br/>thinks shorter]
  Strata -.Unsloth.-> UD[Unsloth UD-IQ4_XS<br/>between IQ3_S & UD-Q4_K_XL]
  Strata -.UD-Q4_K_XL.-> Full[Unsloth UD-Q4_K_XL experimental<br/>7-8.5 tok/s on 64 GB]
  Strata -.OrcaRouter.-> Orca[OrcaRouter Uncensored IQ3_XXS<br/>setup by hand]
  Strata -.Multi GPU.-> Multi[2-3 GPUs 共享模型]
  Strata -.Older GPU.-> Exp[实验性老 GPU<br/>Tesla P40/V100/GTX 10/Radeon VII/MI50/RX 6700 XT/RX 5500 XT]
  Strata -.Intel Arc.-> Arc[Intel Arc 实验性<br/>built from source on Linux]
  Strata -.Strix Halo.-> Strix[AMD Ryzen AI Max Strix Halo<br/>built from source on Linux]
  Strata -.Multi Lang.-> Docs[7 语言 README<br/>English/简体中文/日本語/Deutsch/Français/Español/Português]
  Strata -.Docs.-> DocList[docs/{INSTALL,MODELS,DETAILS<br/>HOW_IT_WORKS,TROUBLESHOOTING<br/>MCP_SERVER,AI_SETUP,BATCHING<br/>COMMUNITY_BENCHMARKS,OLDER_GPUS<br/>INTEL_ARC,STRIX_HALO,MULTI_GPU}.md<br/>+ paper/Strata-Paper.pdf]
  Strata -.License.-> MIT[MIT 商用清晰<br/>Niko1221 个人 + Buy Me a Coffee]
```

## 架构启发
Niko1221/Strata 的核心启发是 **「125B 大模型推理的硬件门槛必须被打破——分层调度 + guess-and-check 是消费级硬件跑大模型的核心严肃工程化」**。当前 125B 模型推理通常需要 80GB+ 显存（H100 / 双卡 A100），这违背绝大多数消费级用户的硬件现实（RTX 5070 / RX 9070 XT 12GB+）。Strata 尝试把 125B 模型推理的硬件门槛从「24GB H100 / 双卡 A100 集群」打到「消费级 12GB+ GPU + Strata 引擎分层调度 + guess-and-check + 三 API 兼容 + 一键启动」严肃工程化，类似 llama.cpp 之于移动端 LLM。更深层的启发是：**MoE 模型的稀疏激活（每 token 仅用 10/24576 = 0.04%）使得「分层调度（GPU 持热点 + RAM 持全集 + SSD 持 lookup）」成为可能**——这是 MoE 模型的杀手特性，但被绝大多数推理框架忽视（llama.cpp / vLLM 都默认全权重加载）。Strata 把这个特性工程化了，是 2026 年 MoE 推理严肃工程化方向的范式。

## 定位判断
**平台候选型项目（消费级硬件跑大模型严肃工程化平台）。** Niko1221/Strata 不仅是本地 LLM 推理工具，更试图成为「消费级硬件跑大模型」的严肃工程化平台——类似 Ollama / LM Studio 但专攻 MoE 大模型（Qwen3.8-Flash-Next 125B）。13 天 15616⭐ + 1331 forks 已显示其严肃工程化影响力。但「消费级硬件跑大模型」取决于一个关键问题：MoE 模型的「热点 experts」是否在多 prompt 类型上稳定——若 prompt 类型变化导致热点 experts 抖动，VRAM 频繁换入换出会严重拖慢推理（hardware thrashing）。目前定位是「最有影响力的消费级硬件跑 MoE 大模型严肃工程化平台」，向更通用本地推理平台演进是合理路径。

## 风险/局限/泡沫点
- **MoE 稀疏激活正确性边界:** 24576 experts 中每 token 用 10 个是否在所有 prompt 类型上都正确——若 prompt 类型变化导致热点 experts 抖动，硬件换入换出会严重拖慢推理（hardware thrashing）
- **guess-and-check 语义保持边界:** 1.6-1.8x 加速的语义保持度——小 helper 猜的下一段词若与大模型不一致，是否会导致质量下降
- **三 API 兼容完整度:** OpenAI /v1 + Anthropic /v1/messages + OpenAI Responses /v1/responses + MCP /mcp 兼容在多 SDK（Claude Code / Codex CLI / Cursor / Grok Build / OpenCode / Google Antigravity）的边界
- **Coder 91% SWE-bench Verified 边界:** Coder 模型只在 SWE-bench 上 91% full model，但其他 benchmark 上是否同样 91% 未明示
- **多硬件严肃工程化承诺边界:** Intel Arc / Strix Halo / older CPUs 标记为「experimental, written and tested by community members」——非官方严肃工程化承诺，社区维护可持续性存疑
- **个人项目属性:** Niko1221 个人维护，1331 forks 但核心治理仍集中，长期可持续性需要观察

## 与同类项目的关系
- **vs llama.cpp:** llama.cpp 是通用 GGML 推理引擎；Strata 是 llama.cpp 之上的「MoE 分层调度 + 125B 模型严肃工程化 + 三 API 兼容 + 一键启动」包装
- **vs Ollama / LM Studio:** Ollama / LM Studio 是通用本地 LLM 推理桌面应用；Strata 是「消费级硬件跑 MoE 125B 大模型」严肃工程化平台
- **vs vLLM / SGLang:** vLLM / SGLang 是数据中心级 LLM 推理服务框架（80GB+ H100）；Strata 是消费级硬件跑大模型严肃工程化平台
- **vs unsloth:** Unsloth 提供模型压缩（Qwen3.8-Flash-Next GGUF）；Strata 在 Unsloth 之上做推理分层调度
- **vs Qwen 官方:** Qwen 提供 Qwen3.8-Flash-Next 模型；Strata 是其严肃工程化本地推理平台

## 是否值得持续跟踪
**值得跟踪（消费级硬件跑大模型严肃工程化平台）。** Niko1221/Strata 代表了「MoE 大模型消费级硬件推理」严肃工程化诉求，无论其本身成败，这一方向是行业趋势（MoE 模型的稀疏激活使得「分层调度」成为可能）。建议关注：MoE 模型热点 experts 在多 prompt 类型的稳定性（决定硬件 thrashing 风险）、三 API 兼容在多 Claude Code / Codex / Cursor harness 的完整性、Intel Arc / Strix Halo 社区维护可持续性。对本地 LLM 推理用户，Strata 是「消费级硬件跑 125B 大模型」的实用严肃工程化方案，值得直接采用。

## 后续观察点
- MoE 模型热点 experts 在多 prompt 类型的稳定性（hardware thrashing 风险）
- guess-and-check 加速在多 benchmark 的语义保持度
- 三 API 兼容在多 Claude Code / Codex / Cursor / Grok Build / OpenCode / Google Antigravity harness 的完整性
- Coder 91% SWE-bench Verified 在多 benchmark 的严肃工程化承诺
- 多硬件严肃工程化（Intel Arc / Strix Halo / older CPUs）社区维护可持续性
- 个人项目治理结构（1331 forks 但核心治理仍集中于 Niko1221 个人）

---
> 数据来源: GitHub API (2026-10-07) | Stars: 15616 | Forks: 1331 | License: MIT | 语言: C++ | 创建: 2026-09-24 | 大小: 19115 KB