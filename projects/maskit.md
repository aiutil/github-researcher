---
title: "xiaYuTian11/maskit"
slug: maskit
date_added: "2026-09-12"
category: "工具型"
emoji: "🛡️"
stars: "143 stars"
stars_delta: "3 天 143⭐ / fork 24 / fork/star 16.8%"
language: "Python + TypeScript (Tauri shell)"
score: 90
tags: ["llm", "privacy", "pii", "mitmproxy", "tauri", "data-masking", "anthropic", "claude-code", "cursor", "codex", "pi", "opencode", "security", "local-gateway", "agpl-3.0"]
url: "https://github.com/xiaYuTian11/maskit"
---

# xiaYuTian11/maskit

## 一句话定位
LLM 终端侧本地隐私脱敏与还原网关——出网前自动打码、入网时 SSE 流式无感还原，100% 本地零遥测，支持 Cursor / Claude Code / Codex / Pi / OpenCode / ChatGPT 等任意可配 Base URL 的 LLM 工具。

## 它解决的问题
2025-2026 年 LLM Coding Agent 大爆发，但每次调用都把代码原文发送到远端模型服务——其中可能含数据库连接串（`mysql://root:***@192.168.1.50:3306/db`）、私有 IP（10.x / 172.16.x / 192.168.x）、API Key（`sk-proj-...` / `ghp_...` / 云厂商 AccessKey / JWT / PEM 私钥）、手机号、身份证、企业内部代号等高危信息。企业开发者用 Cursor / Claude Code 写代码时几乎不可能逐条人工过滤。**maskit 把「出网打码 + 入网还原 + 工具通用 + 本地部署」打包成透明网关**，让 LLM 工具在保留能力的同时不泄露敏感数据。

## 为什么值得关注（2026-09-12）
- 3 天 143⭐ / fork 24 / fork/star **16.8%**——16.8% 是企业级 fork 信号区间（与昨日 `mizzlelover/gongwen-gbt9704-skill` 18.6% 同区间）
- AGPL-3.0 license——企业内部可自由用，但任何修改 + 分发必须开源
- 跨 LLM 工具通用——不绑定单家 Cursor / Claude Code / Codex / Pi
- 技术栈成熟——mitmproxy MITM + Tauri 桌面壳 + SSE 流式还原
- 100% 本地零遥测——满足企业内网合规要求

## 热度来源判断
LLM Coding Agent 在 2026 年渗透企业研发全流程，但"代码含凭据"是真痛点——尤其政企 / 金融 / 医疗场景不可能接受原始代码外发。maskit 直击这一痛点，且技术形态成熟（mitmproxy 是 HTTPS MITM 业界标准；Tauri 桌面壳跨平台完整；SSE 流式还原是合理工程实现）。**热度来源是「LLM Coding Agent 渗透率 × 企业合规刚需 × 跨工具通用 × 零遥测」四因素叠加**。fork/star 16.8% 偏高企服信号，但 AGPL-3.0 也会劝退一部分商业闭源集成方——这是双向筛选。**热度真实且具长期价值**，但能否进入"基础设施"取决于是否被 IDE / Coding Agent 工具官方接入或内置。

## 关键技术亮点
1. **mitmproxy MITM 改写**：HTTPS 中间人拦截请求体，按规则把数据库连接串 / 内网 IP / API Key / 手机号 / 身份证 / 业务词替换为结构化占位符（如 `[DB_CONN_1]` / `[PRIVATE_IP_2]` / `[API_KEY_3]`）
2. **SSE 流式还原**：模型回答流式到达（SSE 协议）时按占位符表毫秒级还原成原文；用户感知不到脱敏存在
3. **跨 LLM 工具通用**：任意可配 Base URL 的工具都可用——Cursor / Claude Code / Codex / Pi / OpenCode / ChatGPT 等
4. **桌面 + Docker 双形态**：Tauri 桌面壳（Windows / macOS）+ Docker 镜像（amd64 / arm64）；CI 完整（GitHub Actions badge 亮）
5. **结构化占位符**：占位符是结构化 token 而非随机字符串——方便模型在脱敏后仍能理解代码语义
6. **100% 本地零遥测**：README 明示无任何外发统计；符合 GDPR / 个人信息保护法对"最小化外发"的要求

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | LLM 客户端 ↔ 远端模型服务之间的透明 MITM 网关；Tauri 桌面壳或 Docker 部署；中间件形态，不替代 LLM 工具本身 | 仅基于 README 与 GitHub 元数据；mitmproxy 证书安装、Tauri 进程隔离、Docker 端口映射未在档案中给出实现细节 |
| 主路径 | LLM 工具 → 出站请求 → mitmproxy 拦截 → 占位符替换 → 远端 LLM 服务 → 流式 SSE 响应 → 占位符还原 → LLM 工具 | 主路径为 README 描述语义；占位符映射表持久化、并发会话隔离、还原顺序保证均待核验 |
| 关键权衡 | 隐私脱敏完整度 vs 模型对脱敏后代码的理解精度 vs 流式还原延迟 vs AGPL-3.0 与商业 fork 兼容性 | 档案明示 AGPL-3.0 与跨工具通用两点权衡；脱敏准确率 benchmark、流式还原延迟基准均未公开 |
| 最小 PoC | 在单 LLM 工具（建议 Claude Code）配 Base URL 指 maskit 网关；上传一段含真实凭据的代码让 Agent 重构；检查 (a) 出网请求体是否打码 (b) 回答流是否还原 (c) 代码重构质量是否显著下降 | PoC 范围与退出路径由档案"先单渠道、最小化外发、可审计"原则推导；具体脱敏规则可调、模型影响 A/B 指标待核验 |
| 依赖与红线 | 依赖 mitmproxy（TLS 中间人证书需用户在 LLM 客户端信任）；AGPL-3.0 禁止修改后闭源分发；任何中间人网关对企业 IT 都是审计对象 | 依赖与红线均来自 README + GitHub 元数据；mitmproxy 证书风险、AGPL-3.0 企业内集成影响需 IT 法务独立确认 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
  LLMClient[LLM 工具<br/>Cursor / Claude Code / Codex / Pi / OpenCode / ChatGPT]
  LLMClient -->|HTTPS 出站请求| MITM[mitmproxy 网关<br/>Tauri 桌面壳或 Docker]
  MITM -->|规则匹配占位符替换| MaskTable[占位符映射表<br/>本地持久化]
  MITM -->|脱敏后请求体| Remote[远端 LLM 服务<br/>OpenAI / Anthropic / DeepSeek / 自托管]
  Remote -->|SSE 流式响应| MITM
  MITM -->|占位符还原| LLMClient
  MITM -.本地零遥测.-> NoExternal[无外部统计上报]
  LLMClient -.用户感知不到脱敏.-> User[开发者]
  MITM -.审计风险边界.-> Audit[企业 IT 中间人网关审计]
```

## 架构启发
maskit 的核心启发是 **「隐私保护不应是 LLM 工具的责任，而应是中间件的责任」**——把脱敏 / 还原做成透明网关，让 LLM 工具和远端服务都不知道中间存在。这样 LLM 工具保持原有 UX、企业保留原有合规边界、用户无需关心凭据过滤。**更深层的启发是「结构化占位符 vs 随机字符串」的设计选择**——结构化 token 让模型在脱敏后仍能理解代码语义，是关键的工程 trick。**最值得借鉴的是「跨工具通用」的产品哲学**——不绑定单家 LLM 工具，让用户保留选择权。

## 定位判断
**平台候选型项目（LLM 隐私基础设施）。** maskit 不是单纯的 PII 替换工具，而是把「出网打码 / 入网还原 / 工具通用 / 本地部署」四件事打包成产品。**它是 LLM 工具链里"隐私侧"的标准件**，类比 SaaS 服务的 zero-trust 网关、API 调用的 API Gateway。能否进入"基础设施"取决于：(a) 是否被 IDE / Coding Agent 工具官方接入或内置（最高优先级）；(b) AGPL-3.0 是否被企业接受（决定商业 fork 空间）；(c) 脱敏准确率与模型影响是否公开 benchmark（决定技术信任度）。当前定位是"最有影响力的本地隐私 LLM 网关"，向基础设施演进是合理路径。

## 风险 / 局限 / 泡沫点
- **AGPL-3.0 与商业 fork 兼容性**：企业内部可自由用，但任何修改 + 分发必须开源——这会劝退一部分商业闭源集成方
- **结构化占位符对模型理解的影响**：README 未提供脱敏后代码准确率 benchmark；下游用户需要自己做 A/B 测试
- **mitmproxy TLS 证书信任**：用户需在 LLM 客户端信任 maskit 自签证书——首次启动有 IT 合规摩擦
- **流式还原顺序保证**：双向加密 / 非标 SSE 协议 / 多路并发会话下占位符还原的顺序与并发安全未公开
- **占位符映射表持久化安全**：映射表本身是敏感资产（包含真实凭据 ↔ 占位符对应关系）——一旦泄露等于完全脱敏失败
- **平台竞争**：未来如果 OpenAI / Anthropic / DeepSeek 官方推出"客户端 PII 脱敏"功能，第三方网关价值会被压缩

## 与同类项目的关系
- **vs Langfuse / Helicone / Phoenix AI observability 平台**：那些是 SaaS 端 observability，需要企业信任服务端；maskit 是中间件端隐私网关，零信任服务端
- **vs Burp Suite / OWASP ZAP**：那些是 Web 应用安全测试工具；maskit 是 LLM 工具的中间人网关，定位完全不同
- **vs 企业 DLP（数据防泄漏）系统**：DLP 在企业网络出口拦截；maskit 是 LLM 工具专用中间件，颗粒度更细
- **vs 各 LLM 工具官方 PII 处理**：目前 OpenAI / Anthropic / DeepSeek 的官方 PII 处理多为服务端日志过滤；maskit 是客户端打码，更彻底
- **vs Prompt 加密 / 同态加密方案**：那些是密码学路线，性能开销大；maskit 是规则匹配 + 占位符替换，工程实用

## 是否值得持续跟踪
**值得跟踪（LLM 隐私基础设施候选）。** maskit 解决了 LLM Coding Agent 时代最关键的合规痛点，且技术形态成熟、产品形态完整（桌面 + Docker）。**对企业 / 政企 / 金融 / 医疗场景的 LLM 工具集成方，这是必看项目**。建议关注：(a) 是否被 IDE / Coding Agent 工具官方接入（决定基础设施地位）；(b) 脱敏准确率与模型影响是否公开 benchmark（决定技术信任度）；(c) 占位符映射表持久化与备份机制（决定企业采用门槛）；(d) AGPL-3.0 是否会调整为更友好的 dual license（决定商业生态）。

## 后续观察点
- 是否被 Cursor / Claude Code / Codex 官方文档或集成指南引用
- 是否出现 dual license 调整（AGPL-3.0 → AGPL + 商业 license）
- 脱敏准确率与模型影响 benchmark 是否公开
- 占位符映射表加密存储与备份机制是否完善
- 是否出现企业级 multi-tenant / SSO / 审计日志版本
- 是否出现竞品（Lit-Gateway、LLM-Proxy、PII-Mitigator 等）

---

*首次记录：2026-09-12*
