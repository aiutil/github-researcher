---
title: "9router"
slug: "9router"
date_added: "2026-08-14"
last_seen_date: "2026-08-14"
category: "工具型"
emoji: "🛠️"
stars: "25,938 stars"
stars_delta: "创建于 2026-01-05，8 个月内获得 25,938 stars，增速明显（forks 4,667）"
language: "JavaScript"
license: "MIT"
score: 72
tags: ["ai-agents", "ai-gateway", "anthropic", "claude-code", "free-ai", "llm-gateway", "openai-proxy"]
url: "https://github.com/decolua/9router"
homepage: "https://9router.com"
---

# 9router

## 一句话定位
自托管 AI 网关——把 Claude Code / Codex / Cursor / Cline / Copilot / Antigravity 等 Coding Agent 的 LLM 请求路由到 40+ 免费/付费 provider，自带 RTK（Round-Trip Killer，号称省 40% token）与自动 failover。

## 它解决的问题
Coding Agent 用户普遍痛点：官方 LLM API 价格高昂、区域受限、限速严重；同时手动切换 provider 费时。9router 把多 provider 路由、token 压缩、失败自动重试打包成一个 HTTP/SSE 代理，Agent 本地指向 9router 端口即可无缝跨 provider。

## 为什么值得关注（2026-08-14）
被 daily/2026-08-14.md 选为今日 AI 周边工具重点。代表了 "Agent 工具链中间层" 方向——既不是 Agent 本身，也不是单纯模型 API，而是把多 provider 解构成 Agent 可调用的统一接口。在 Coding Agent 内卷的 2026 年，这类中间层服务有真实付费/自助场景。

## 热度来源判断
热度来源为 **"Coding Agent 成本痛点 × 多 provider 路由刚需"**。25,938 stars 在 8 个月（2026-01 至 2026-08）的实测数据下成立——属于冷启动增长期，是真实的早期采用者效应。open_issues 高达 1,718（远超大多数项目）显示用户基数大、问题反馈密集。但需注意：网关类项目容易被官方或上游替代方案"消化"——一旦 Cursor/Claude Code 官方推出同等功能，价值会被压缩。

## 关键技术亮点
1. **统一 HTTP/SSE 网关:** 透明代理 Coding Agent 的所有 LLM 请求，零侵入
2. **40+ provider 支持:** 涵盖 Claude / GPT / Gemini / DeepSeek / Qwen 等
3. **RTK token 压缩:** 自研压缩算法（声称减 40% token，**待独立验证效果**）
4. **自动 failover + 重试:** provider 失败时无缝切换，自带限速/重试策略
5. **CLI 安装:** 一行命令启动，支持 docker/裸进程

## 架构启发
"把分裂的 LLM API 在网关层屏蔽"是经典反向代理模式，但 9router 把它做成了 Coding Agent 友好版本。其架构启发是：**当生态碎片化时，中间层是真实商业机会**——但同时中间层也最易被标准化（如 OpenRouter 也瞄准同一赛道）。

## 定位判断
**工具型 / 中间件候选项目。** 是自托管 LLM 网关的代表性新项目，处于"被 AI Agent 基础设施生态消化"的风险与机会并存区间。25k stars 反映早期采用热度，但能否长期留存取决于：(a) RTK 实际收益是否被独立验证，(b) 上游 Coding Agent 是否原生集成类似能力。

## 风险 / 局限 / 泡沫点
- **RTK 效果待验证:** 自称 -40% token 需要独立基准测试，可能存在营销夸大
- **OpenRouter 等成熟竞品:** 同一赛道，OpenRouter 体量、品牌、云托管能力更强
- **provider 协议变化:** 上游 LLM 协议变更需快速适配，长期维护成本高
- **合规/审计盲区:** 自托管网关绕过部分 provider 的 ToS，存在封号风险
- **单维护者风险:** 1,718 issues 但核心团队规模未知，社区治理压力大

## 与同类项目的关系
- **vs OpenRouter:** OpenRouter 是云端路由龙头；9router 强调自托管 + Coding Agent 友好
- **vs LiteLLM:** LiteLLM 是 Python 库，9router 是 CLI/网关服务，更易部署
- **vs Portkey:** Portkey 偏向网关 + 可观测性；9router 偏 Coding Agent + 成本优化
- **vs 各 Coding Agent 自带 provider switch:** 9router 跨 Agent 复用，Agent 内置则单家

## 是否值得持续跟踪
**值得跟踪（成本敏感型 Coding Agent 用户的实用工具）。** 对需要多 provider 切换 + 成本控制的自托管用户，9router 是当下少数可选项。建议关注：(a) RTK 独立基准测试，(b) 对 Anthropic / OpenAI / Google 官方 ToS 的合规声明演化，(c) 与 OpenRouter 等的市场份额变化。

## 后续观察点
- RTK 压缩效果是否有第三方对比测试
- 是否进入 Coding Agent 官方推荐中间件列表
- 自托管 vs 云端模式的产品定位演化
- 与 LiteLLM/OpenAI 兼容层的关系（合作或竞争）
- 1,718 issues 的关闭率（衡量维护能力）

---
> 数据来源: GitHub API (2026-08-21) | Stars: 25,938 | Forks: 4,667 | License: MIT | 语言: JavaScript | 创建: 2026-01-05
