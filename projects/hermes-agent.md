---
category: 基础设施候选
date_added: '2026-04-07'
emoji: 🧙
github_url: https://github.com/insinbusy/hermes-agent
mcp: true
poc_recommend: false
score: 58
stars_per_day: ~1700 (日增量)
summary: Agent 自进化 + 跨会话记忆系统，Skill 自进化机制触及 Agent 学习核心。
tech_stack: Python
title: hermes-agent
total_stars: ~149k (推算)
---

# hermes-agent

> The agent that grows with you

## 基本信息

- **仓库：** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Star：** 146,768
- **本周新增：** ~8,000
- **语言：** Python
- **许可：** 需确认
- **归档状态：** 活跃

## 核心定位

NousResearch 出品的**自进化 AI Agent**。核心理念："The agent that grows with you"——不是静态的工具，而是一个会从经验中学习、生成新技能、在使用中自我改进的动态 Agent 系统。

## 技术亮点

1. **自进化 Skill 系统**：任务完成后自动提取可复用 Skill，Skill 在后续使用中自动优化。不同于 RAG 的"检索已有知识"，这是"从经验中生成新能力"
2. **跨会话连续性**：FTS5 全文检索 + LLM Summarization，实现真正的长期记忆
3. **Honcho 用户画像**：跨会话建立用户偏好模型，每次交互都在加深对用户的理解
4. **多平台 Messaging Gateway**：Telegram、Discord、Slack、WhatsApp、Signal、Email，一个 Gateway 对接所有平台
5. **Cron 调度 + 自然语言**：用自然语言描述定时任务，Agent 自动编排执行
6. **多终端部署**：$5 VPS / Docker / SSH / Daytona / Singularity / Modal，Modal 可实现 Serverless 持久化
7. **多 Provider 路由**：OpenRouter 200+ 模型、OpenAI、Kimi、GLM、MiniMax，灵活切换无 Lock-in
8. **OpenClaw 迁移路径**：明确提供从 OpenClaw 一键迁移，降低迁移门槛

## 解决的问题

**AI Agent 的记忆与学习问题是核心工程挑战。** 大多数 Agent 方案只是：
- 把历史对话放进 Context（有限）
- 加个向量数据库做 RAG（只是检索，不是学习）

hermes-agent 走的是"从经验中生成技能并自动优化"这条路，这是更接近"真正学习"的方向。

## 泡沫点

- Skill 自进化的质量边界不明确，"自我优化"在实践中能走多远有待验证
- OpenClaw 迁移功能说明它正在蚕食 OpenClaw 生态，但迁移本身可能带来用户对供应商锁定风险的担忧

## 架构启发

**Skill 自进化机制是最值得深度研究的工程问题。** 如果能在企业内部落地，会是真正的差异化竞争力。核心思路：从"让 Agent 检索知识"升级到"让 Agent 从经验中创造知识"。

## 评分

| 维度 | 得分 | 理由 |
|------|------|------|
| 热度质量 | 8 | 稳健增长，28k 总数，9.6k/week |
| 技术创新度 | 8 | Skill 自进化 + Honcho 用户建模，开源中少见 |
| 工程成熟度 | 7 | 文档完备，Gateway 支持多平台，但 Skill 进化质量待验证 |
| 架构启发价值 | 9 | 触及 Agent 核心问题，记忆+学习对企业平台有直接参考价值 |
| 企业落地潜力 | 7 | 部署灵活，迁移成本低，但需评估 Skill 进化质量 |
| 中期趋势概率 | 8 | 自进化是真实方向 |
| 平台化潜力 | 7 | Messaging Gateway 已有平台特征 |
| 基础设施潜力 | 8 | Skill 系统、Memory 系统是多 Agent 平台必需的底层能力 |
| **总分** | **62/80** | |

## 归类

**基础设施候选 | 深度跟踪 + 值得做 PoC**

## 关联项目

- `oh-my-claudecode` — 不同路径的 Agent 编排（Claude Code 绑定 vs 独立）
- `onyx` — 开源 AI Chat 平台

---

*首次记录：2026-04-07*

## 最近动态 (2026-05-15)

- **2026-05-15:** 网络受限日，趋势延续分析。基于 05-14 实测数据推算，持续跟踪中。
- Stars 数据为推算值，网络恢复后验证。

---
