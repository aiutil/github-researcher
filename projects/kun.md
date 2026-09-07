---
title: "kunchenguid/kun"
slug: kun
date_added: 2026-09-08
last_seen_date: 2026-09-08
category: "工具型"
emoji: "👷"
stars: "234 stars"
stars_delta: "2 天 0→234⭐，单日均速 ~117⭐/day；Meta/Microsoft/Atlassian L8 首席工程师 /kun Skill + living docs 日更"
language: "Markdown"
score: 82
tags: ["agentskills-io", "agent-skill", "codex", "distilled-experience", "kunchenguid", "kun", "living-docs", "principal-engineer"]
url: "https://github.com/kunchenguid/kun"
---

# kunchenguid/kun

## 一句话定位
"Think and build like a principal engineer"——Meta / Microsoft / Atlassian **L8 首席工程师 kunchenguid** 的 `/kun` Skill（**living docs 日更**），通过 agentskills.io `npx skills add kunchenguid/kun -g` 分发；2 天 234⭐，fork 13，Markdown。

## 它解决的问题
2026 年 Agent Skill 内容市场已经成型（mattpocock / anthropics / humanlayer / sepia 等），但绝大多数 Skill 是 **"静态文档 + 一次性发布"**——作者写完即固定。`/kun` 的核心差异是 **"living docs / daily update"**："This /kun skill here is a near-realtime distillation of my experience, knowledge, tools, workflows and skills. The instructions and knowledge base here is **updated daily** based on what I said and did."——Skill 内容随作者经验动态演化，用户调用的不是"v1 知识"，而是"今日经验"。

直击痛点：(a) **静态 Skill 的过时问题**——Skill 写完 6 个月后可能与最新最佳实践脱节；(b) **作者投入的可量化**——living docs 模式下，用户的每次调用都反映了作者当日的认知；(c) **Skill 时代的"个人订阅"**——`/kun` 是"知识订阅"的雏形。

## 为什么值得关注
- **Stars:** 234（截至 2026-09-08），2 天净增，单日均速 ~117⭐/day
- **Forks:** 13（fork/star **5.6%**，略低于 magnitude 7.2%）
- **语言:** Markdown 主导（Skill 内容是结构化文档）
- **项目年龄:** 2 天（创建 2026-09-06）
- **核心差异:** 作者品牌背书（L8 PE @ Meta / Microsoft / Atlassian）+ living docs 日更 + agentskills.io 分发

## 热度来源判断
`/kun` 的热度来自三个因素：(1) **作者品牌背书极强**——L8 首席工程师（Meta / Microsoft / Atlassian），verified identity + 真实 X 账号（@kunchenguid）+ Discord 链接；(2) **living docs 模式刷新 Skill 模式预设**——从静态文档升级为"作者 live 经验流"；(3) **agentskills.io 协议分发**——`npx skills add kunchenguid/kun -g` 标准化安装，降低采用门槛。

2 天 234⭐ / fork 13（fork/star 5.6%）的组合反映 **"作者品牌 + 模式创新 + 分发协议"** 三者叠加。

## 关键技术亮点
1. **作者品牌背书:** L8 首席工程师（Meta / Microsoft / Atlassian），verified identity + 真实 X + Discord——Skill 内容的可信度天花板
2. **Living docs / Daily update:** "updated daily based on what I said and did"——Skill 是动态文档，不是静态快照
3. **agentskills.io 协议分发:** `npx skills add kunchenguid/kun -g` 标准化安装
4. **多 Runtime 兼容:** README 注明"in your agent: /kun how should I improve my AGENTS.md?"——支持 Claude Code / Codex / Cursor 等能读 SKILL.md 的 Runtime
5. **README 工作流图明示:** daily automation → refresh living docs；/kun question → fetch ENTRY → 应用方法论

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 个人 Skill 层 + Living docs 日更机制；Skill 内容是作者经验的蒸馏，不是 LLM 通用知识 | 边界由 README 明示；具体 living docs 的更新机制（自动化 / 手动）需 commit log 核验 |
| 主路径 | daily automation → refresh living docs → 用户调用 → fetch ENTRY → 应用方法论 | 主路径为 README 语义抽象；具体 ENTRY 格式与 fetch 机制需 README 核验 |
| 关键权衡 | 作者投入的可持续性（vs 静态 Skill 的稳定性）；living docs 的质量稳定性（vs 静态 Skill 的多次 review）；个人品牌的单一性（vs 团队 Skill 的多样性） | README 标注"updated daily based on what I said and did"；具体更新频率需 commit log 验证 |
| 最小 PoC | 在 Codex / Claude Code 安装 Skill → 调用 `/kun how should I improve my AGENTS.md?` → 检查输出是否包含作者当日更新的方法论 | PoC 范围由 README "Quick Start" 推导；living docs 的"今日 vs 昨日"差异需要 benchmark |

## 架构启发
`/kun` 的核心启发是 **"Skill 模式从'静态文档'升级到'作者 live 经验流'"**。传统 Skill 是"快照"——写完即固定；living docs 是"流"——随作者持续演化。更深层的启发是 **"Skill 时代的个人订阅"**——用户调用的不是"v1 知识"，而是"作者今日认知"；这与 Newsletter / Substack 等知识订阅模式有相似性，但 Skill 模式更结构化、更可编程。

风险提示：**作者依赖是 living docs 的最大风险**——一旦作者停更 / 转岗 / 倦怠，Skill 即"过时"；**质量稳定性**——daily update 可能包含未深思熟虑的内容（vs 静态 Skill 经多次 PR review）。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Author[kunchenguid<br/>L8 首席工程师] --> Daily[Daily Automation]
  Daily --> Living[Living Docs<br/>每日更新]
  Living --> Repo[kun 仓库<br/>Markdown]
  User[用户] --> Trigger[/kun 命令<br/>"how should I improve AGENTS.md?"]
  Trigger --> Fetch[fetch ENTRY<br/>从仓库拉取]
  Fetch --> Apply[应用方法论]
  Apply --> Out[创作建议]
  Repo -.agentskills.io.-> Install[npx skills add kunchenguid/kun -g]
  Install --> Runtime[Claude Code / Codex / Cursor Runtime]
  Runtime --> Trigger
  Living -.作者依赖.-> Risk[停更 / 转岗 / 倦怠<br/>Skill 过时风险]
  Living -.质量稳定性.-> Quality[未深思熟虑内容<br/>vs 静态 Skill PR review]
```

## 定位判断
**工具型项目（个人 Skill + living docs 日更），向"Expert Skill as a Service"演进。** `/kun` 不仅是一个 Skill 仓库，更是 Skill 模式从"静态文档"升级到"作者 live 经验流"的样本。2 天 234⭐ 已显示初步关注，但 fork/star 5.6% 略低于同类项目。当前定位是"作者品牌 + living docs 模式的头部样本"，向"Expert Skill as a Service"（专家本人订阅）演进是合理路径。

## 风险/局限/泡沫点
- **作者依赖:** living docs 完全依赖 kunchenguid 本人持续活跃；作者一旦停更 / 转岗 / 倦怠，Skill 即"过时"
- **质量稳定性:** daily update 可能包含未深思熟虑的内容（vs 静态 Skill 经多次 PR review）
- **个人品牌的单一性:** 单作者 Skill 缺乏团队多样性（vs Anthropic Skills 团队 / mattpocock 社区）
- **Living docs 的安全性:** 动态内容可能被恶意 commit 注入，需要审计机制
- **fork/star 5.6% 偏低:** 略低于 magnitude 7.2%，反映"围观但不动手"特征
- **2 天新项目风险:** 项目可持续性 / 治理结构未验证

## 与同类项目的关系
- **vs mattpocock/skills (9-06, 252K⭐):** mattpocock 是通用 Skills 集合（多作者 / 多领域）；/kun 是单作者 / 单领域——通用 vs 个人品牌
- **vs anthropics/skills (9-06, 472⭐/day):** anthropics 是 Claude 官方 Skills（团队 / 官方）；/kun 是社区单作者——官方 vs 社区
- **vs jtydhr88/screenwriting-skills (9-08, 301⭐):** screenwriting-skills 是垂直领域深度蒸馏（19 本书 + 契诃夫 + 小津安二郎）；/kun 是单作者 living docs——垂直深度 vs 个人广度
- **vs DietrichGebert/ponytail (9-06, 2813⭐/day):** ponytail 是单 Skill 静态；/kun 是单 Skill + living docs——静态 vs 动态
- **vs Newsletter / Substack:** 知识订阅模式相似，但 Skill 模式更结构化、可编程

## 是否值得持续跟踪
**值得跟踪（个人 Skill + living docs 日更头部样本）。** `/kun` 代表了 Skill 模式从"静态文档"升级到"作者 live 经验流"的方向，与 L8 PE 个人品牌 + agentskills.io 协议 + 2 天 234⭐ 共同构成新方向。建议关注：(a) 作者投入的可持续性（commit log 验证 living docs）；(b) living docs 的质量稳定性（vs 静态 Skill）；(c) "Expert Skill as a Service"模式是否成型；(d) 下一波"作者 living docs Skill"是否跟进（律师 / 医生 / 设计师）。对 Agent Skill 生态观察者，/kun 是 Skill 模式演进的标杆样本。

## 后续观察点
- 作者投入的可持续性（commit log 频率）
- living docs 的质量稳定性（每日更新的内容质量）
- "Expert Skill as a Service"模式是否成型（其他专家是否跟进）
- 作者个人品牌的传播（X / Discord / 行业影响力）
- Skill 时代的"个人订阅"商业模式是否成立
- agentskills.io 协议的演进（是否成为跨 Runtime 标准）

---
> 数据来源: GitHub API (2026-09-08) | Stars: 234 | Forks: 13 | License: 待核验 | 语言: Markdown | 创建: 2026-09-06
