---
title: "FreeLLMAPI"
slug: "freellmapi"
date_added: "2026-05-01"
category: "工具型"
emoji: "🌊"
stars: "13,142 stars"
stars_delta: "2 个月 17 倍（783→13K），日增 586"
language: "TypeScript"
score: 85
tags: ["llm-proxy", "free-tier", "openai-compatible", "anthropic-compatible", "multi-provider", "claude-code"]
url: "https://github.com/tashfeenahmed/freellmapi"
last_seen_date: "2026-06-27"
---

# FreeLLMAPI

## 一句话定位
聚合 16 家免费 LLM Provider 的 OpenAI/Anthropic 双兼容代理——~1.7B tokens/月免费推理能力，2 个月 17 倍增长。

## 它解决的问题
开发者需要在多个 LLM Provider 之间切换以利用各自的免费额度，但每个 Provider 的 SDK、rate limit、key 管理都不同。FreeLLMAPI 将这些聚合为一个 OpenAI 兼容端点 + Anthropic 兼容端点。

## 为什么值得关注（2026-06-27 更新）
从 5 月 1 日的 783⭐ 暴涨至 13,142⭐（2 个月 17 倍），日增 586。代表了一个加速的新兴模式——**免费推理聚合**。16 家 Provider 聚合后 ~1.7B tokens/月，已形成可用的推理能力。

### 最近动态（2026-06-27）
- Provider 从 14 扩展至 16（新增 OVH AI Endpoints、OpenCode Zen）
- 新增 Anthropic Messages API 兼容（`/v1/messages`）——Claude Code 可直接对接免费 pool
- 新增 Responses API（`/v1/responses`）——Codex CLI 兼容
- 新增图片生成（`/v1/images/generations`）和 TTS（`/v1/audio/speech`）
- 新增 Embeddings（`/v1/embeddings`，family-based 路由）
- Sticky sessions（30 分钟同模型，避免中途切换幻觉）
- Context handoff（model switch 时注入 compact system message）
- 桌面 App + Docker 部署支持

## 热度来源判断
- **实用性驱动**：~1.7B tokens/月免费额度对个人开发者有巨大吸引力
- **Claude Code / Codex 兼容**：直接对接主流 Agent 工具是增长加速器
- **合规讨论引发关注**：ToS 灰色地带本身也是话题传播点
- **17 倍增长验证需求**：不是一日热点，持续 2 个月高增长

## 关键技术亮点亮点
1. **三协议兼容**——OpenAI `/v1/chat/completions` + Anthropic `/v1/messages` + Responses API（`/v1/responses`）
2. **智能路由 + 自动 failover**——429/5xx 自动跳到下一个 Provider，每 key RPM/RPD/TPM/TPD 计数，最多 20 次重试
3. **Sticky sessions**——多轮对话 30 分钟内保持同一模型，避免中途切换的幻觉
4. **AES-256-GCM 加密 key 存储**——16 个 Provider 的 API key 加密存储在 SQLite
5. **Embeddings family-based 路由**——failover 只在同模型 Provider 间发生（不同模型向量不兼容）
6. **16 Provider 覆盖**——Google/Groq/Cerebras/NVIDIA/Mistral/OpenRouter/GitHub Models/Cloudflare/Z.ai/Cohere/HuggingFace/Ollama Cloud/Kilo/Pollinations/LLM7/OVH

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 客户端（Claude Code / Codex CLI 等 Agent 工具）↔ FreeLLMAPI 代理层 ↔ 16 家外部免费 Provider 的三层编排层 | 边界由三协议端点（`/v1/chat/completions`、`/v1/messages`、`/v1/responses`）与 Provider 列表（Google/Groq/Cerebras/NVIDIA/Mistral/OpenRouter/GitHub Models/Cloudflare/Z.ai/Cohere/HuggingFace/Ollama Cloud/Kilo/Pollinations/LLM7/OVH）描述；具体鉴权流、容器化形态与企业级 Gateway 差异需源码核验 |
| 主路径 | 客户端请求 → Smart Router（按 key 计 RPM/RPD/TPM/TPD）→ 单 Provider 尝试 → 遇 429/5xx 触发 Fallback Chain（≤20 次重试）→ 命中后维持 30 分钟 Sticky Session；模型切换时注入 compact system message；Embeddings 仅在同模型 family 内 failover | 路径由档案「关键技术亮点」描述；compact system message 内容、fallover 调度算法、KV/上下文压缩实现均未在档案披露 |
| 关键权衡 | 16 Provider 覆盖面与 ToS 灰区耦合度的权衡：聚合得越广，攻击面（加密 key 库）、政策依赖（单 Provider 改 ToS 即影响全局）、商用合规风险越高；Sticky Session 与模型切换 Context Handoff 体现"稳定性 vs 路由灵活性"取舍 | 权衡基于「风险/局限」段与 sticky sessions、context handoff 描述；各 Provider ToS 细节、实测可用额度未在档案给出量化 |
| 最小 PoC | 在 `/v1/chat/completions` 与 `/v1/messages` 两端点分别跑 1 个 Provider（如 Google），验证 sticky session、fallback、加密 key 落盘；优先核对 NVIDIA 等带 eval-only 限制的 Provider ToS，再决定是否扩到多 Provider 与 images/audio/embeddings 端点 | PoC 范围由端点清单、加密存储声明与风险段推导；实际可用 token 配额、QPS、延迟 P99 须实测，档案未提供 |

## 架构启发

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    A[客户端: Claude Code / Codex CLI / 其他 OpenAI 兼容工具]
    B[FreeLLMAPI 入口: /v1/chat/completions<br/>/v1/messages<br/>/v1/responses<br/>/v1/images/generations<br/>/v1/audio/speech<br/>/v1/embeddings]
    C[Smart Router + Sticky Session 30min<br/>RPM/RPD/TPM/TPD 计数<br/>Context Handoff on model switch]
    D[Fallback Chain: 最多 20 次重试<br/>遇 429/5xx 跳下一 Provider<br/>Embeddings 仅同 family 内 failover]
    E[加密 Key 存储: AES-256-GCM over SQLite]
    F[外部边界: 16 家免费 Provider<br/>Google / Groq / Cerebras / NVIDIA / Mistral / OpenRouter / GitHub Models / Cloudflare / Z.ai / Cohere / HuggingFace / Ollama Cloud / Kilo / Pollinations / LLM7 / OVH]
    G[风险/合规边界: Provider ToS 灰区<br/>无 SLA / 政策可单方变更 / 聚合触发审查]
    A --> B --> C --> D --> F
    E --> C
    F -.触发策略变更.-> G
    D -.失败耗尽.-> G
    F -->|响应| D -->|响应| A
    H[桌面 App + Docker 部署形态 - 待核验]
    B -.打包方式.-> H
```

FreeLLMAPI 的架构本质上是一个 **LLM Gateway 的免费版**。企业级 LLM Gateway（如 Portkey、LiteLLM）做的是多 Provider 路由 + 可观测性 + 成本控制，FreeLLMAPI 聚焦在免费 tier 的最大化利用。

启示：
1. LLM Gateway 层标准化加速——OpenAI 兼容已成为事实标准，Anthropic 兼容正在成为第二标准
2. 免费 tier 聚合是一种新型 Cloud Arbitrage——不同 Provider 的免费额度等价于"云资源碎片"
3. Agent 工具（Claude Code/Codex）兼容是增长杠杆

## 定位判断
- **个人实验工具 → 开发者基础设施过渡**
- 适合 PoC 和个人开发者降低成本
- Anthropic/OpenAI 双兼容是关键差异化
- 对 SLA 有要求的场景不可用

## 评分
| 维度 | 分数 | 理由 |
|------|------|------|
| 热度质量 | 8 | 17 倍增长真实，但增速可能见顶 |
| 技术创新度 | 6 | 路由+failover 非新概念，免费聚合角度有新意 |
| 工程成熟度 | 7 | 功能完整，三协议支持，但依赖外部 Provider 稳定性 |
| 架构启发价值 | 7 | LLM Gateway 标准化+Cloud Arbitrage 模式 |
| 企业落地潜力 | 4 | ToS 灰色地带是硬伤 |
| 中期趋势概率 | 7 | 免费 tier 聚合需求持续，但政策风险大 |
| 平台化潜力 | 5 | 可演化为个人 AI infra 入口 |
| 基础设施潜力 | 4 | 合规限制使其难以成为企业基础设施 |
| **总分** | **48/80** | **工具型→平台候选过渡** |

## 风险 / 局限 / 泡沫点
1. ⚠️ **合规灰色地带（高）**：部分 Provider 免费 tier 限个人非商用（如 NVIDIA eval-only ToS）
2. ⚠️ **无 SLA 保障**：免费 tier 随时可能被限流或取消
3. ⚠️ **Provider 政策变更**：任何一家 Provider 修改免费 tier 政策都会影响整体可用性
4. ⚠️ **安全攻击面**：16 个 Provider 的 key 集中存储，即使加密也增加攻击面
5. ⚠️ **ToS 审查风险**：随着规模增长，可能引发 Provider 的合规审查

## 与同类项目的关系
- **LiteLLM**：企业级 LLM Gateway，100+ Provider，更成熟但非免费导向
- **Portkey AI**：LLM Gateway + 可观测性，企业级方案
- **OneAPI / New API**：国内 API 聚合方案
- **Cloudflare AI Gateway**：云厂商提供的 Gateway 方案

差异化：免费 tier 最大化 + Anthropic 兼容 + Claude Code 可直接对接

## 是否值得持续跟踪
✅ **持续跟踪**。17 倍增长验证需求。关键观察点：
1. Provider 是否会限制此类聚合使用
2. 是否有 Provider 推出官方聚合方案
3. Claude Code / Codex 兼容是否带动更多 Agent 工具集成
4. 是否出现企业级合规版本

## 后续观察点
1. Provider 政策变更影响
2. 社区合规性讨论
3. 是否出现 SaaS 化版本
4. 免费 tier 总额度是否随 AI 竞争加剧而增长

---
*首次记录：2026-05-01*
*重大更新：2026-06-27 — stars 783→13K（17 倍），Provider 14→16，新增 Anthropic/Responses API 兼容，评分 76→85*
