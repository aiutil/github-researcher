---
title: "paradigmxyz/centaur"
slug: paradigm-centaur
date_added: 2026-06-06
last_seen_date: 2026-08-07
category: "Platform"
emoji: "🐎"
stars: "967 stars"
score: 80
tags: ["self-hosted", "agent-platform", "multiplayer", "secure-agents", "python", "team-agents"]
url: "https://github.com/paradigmxyz/centaur"
---

# paradigmxyz/centaur

## 一句话定位
Paradigm（顶级加密投资/研究机构）开源的**多人协作、自托管、安全的 Agent 平台**——让团队能够共享、安全地运行 AI Agent，强调"多人（multiplayer）"协作与凭据安全边界，官网 centaur.run，是加密原生机构对"团队级 Agent 基础设施"的探索。

## 它解决的问题
AI Agent 在个人使用场景已较成熟（Claude Code、各类 CLI Agent），但在**团队/组织**场景面临独特挑战：多个成员如何共享同一个 Agent（及其记忆/配置）？Agent 持有的敏感凭据（API key、数据库密码）如何在不暴露给每个成员的情况下被安全使用？Agent 执行的长任务如何在团队间可见、可协作？centaur 直击这些"团队 Agent"痛点：它提供自托管的多用户 Agent 平台，内置凭据隔离（Agent 能用凭据但不向所有成员暴露）、持久工作流、团队协作可见性。解决的是 **"个人 Agent 易做，团队 Agent 难行"** 的组织级 Agent 部署难题，尤其适合对数据主权敏感的团队（自托管而非用 SaaS）。

## 为什么值得关注
- **Stars:** 967（截至 2026-08-07），3 个月稳步增长，早期高潜项目
- **Forks:** 183，早期社区形成
- **Watchers/Subscribers:** 6
- **Open Issues:** 90，活跃讨论（多为功能设想，反映早期阶段）
- **License:** NOASSERTION（需注意，非标准开源许可）
- **语言:** Python
- **活跃度:** created 2026-05-18，pushed_at 2026-08-07（**当日更新**），极度活跃
- **官网:** centaur.run，有独立品牌与产品定位
- **规模:** 42.8MB，有实质工程量
- **背书:** Paradigm（paradigmxyz）官方组织，加密领域顶级机构

## 热度来源判断
centaur 的热度（近 1k stars）主要由 **"Paradigm 品牌背书 + 团队 Agent 痛点真实 + 自托管趋势"** 驱动，但规模仍小，处于早期孕育期。Paradigm 在加密/Web3 圈影响力巨大（投资/研究双顶尖），其开源的 Agent 平台天然吸引关注。团队级 Agent 确是真实痛点——个人 Agent 工具遍地，但"团队共享 Agent + 凭据安全"的方案稀缺。自托管趋势（数据主权需求）让 centaur 这类非 SaaS 方案有明确受众。热度真实但量级小，说明尚未破圈。需注意：License 为 NOASSERTION（非标准开源），可能限制采用与社区贡献——这是需要厘清的关键点。整体是**有潜力但极早期**的项目。

## 关键技术亮点
1. **多人（Multiplayer）协作:** 多用户共享同一 Agent 实例及其记忆/工作流，团队可见 Agent 状态与历史
2. **凭据安全边界:** Agent 能使用敏感凭据（API key/密码）执行任务，但凭据对普通成员隔离——"用而不见"
3. **自托管（Self-hosted）:** 团队完全掌控数据与 Agent，不依赖第三方 SaaS，满足合规与主权需求
4. **持久工作流:** Agent 任务可长期运行、中断恢复、跨会话延续，适合团队级长周期任务
5. **Python 实现:** 便于集成丰富 AI 生态（LangChain、MCP 等），降低扩展门槛
6. **centaur.run 产品化:** 独立官网暗示有产品化意图，非纯开源副业

## 架构启发
centaur 的核心启发是 **"Agent 从个人工具走向团队基础设施时，'凭据安全'是核心设计约束"**。个人 Agent 的凭据由用户自己管理，风险可控；但团队 Agent 的凭据若处理不当，可能被任何团队成员借 Agent 之手提取——这是全新的威胁模型。centaur 把"凭据隔离"作为一等公民，Agent 能调用凭据但成员不可见，这是一种巧妙的"能力受托"架构。更深层的启发是 **"自托管 + 多人"是 Agent 平台的重要细分**——并非所有团队都愿把 Agent 与凭据交给 SaaS（如 OpenAI/Anthropic 的托管方案），自托管方案满足数据主权需求，centaur 是这一细分的有力探索。

## 定位判断
**平台型早期项目（团队自托管 Agent 基础设施）。** centaur 定位于"团队级自托管 Agent 平台"，是一个有明确产品形态（centaur.run）的平台型项目。它瞄准的细分（自托管+多人+凭据安全）在当前 Agent 生态中相对空白，有先发优势。但处于极早期（<1k stars），能否成长为真正的平台取决于：①Paradigm 的持续投入；②凭据安全模型的工程成熟度；③社区与企业采用。License 问题（NOASSERTION）是当前需解决的基础障碍。若这些问题理顺，centaur 有潜力成为"注重数据主权的团队的 Agent 平台"首选之一。

## 风险/局限/泡沫点
- **极早期:** 967 stars、6 subscribers，产品成熟度与采用率均低，风险高
- **License 不明（NOASSERTION）:** 非标准开源许可，法律上限制复用与商业采用，是重大障碍
- **Paradigma 主业偏离:** Paradigm 核心是加密投资/研究，Agent 平台是否长期战略重点存疑
- **凭据安全实现难度:** "用而不见"的凭据隔离工程上极具挑战，实现缺陷会成安全漏洞
- **竞争:** 自托管 Agent 平台赛道会吸引更多玩家（尤其企业级需求明确后）
- **Open Issues 高:** 90 个 issues 多为设想，反映功能尚未稳定

## 与同类项目的关系
- **vs OpenClaw/Hermes Agent（自托管 Agent 平台）:** 同为自托管方向；centaur 强调"团队多人+凭据"，差异化在协作与安全
- **vs OpenAI/Anthropic 托管 Agent:** 那些是 SaaS 托管；centaur 是自托管，满足数据主权
- **vs Dify/Coze（Agent 平台）:** 那些偏"无代码搭建 Agent"；centaur 偏"运行托管团队 Agent"
- **vs HashiCorp Vault（凭据管理类比）:** Vault 管凭据；centaur 把凭据安全融入 Agent 运行时，理念延伸
- **vs n8n（自托管工作流）:** n8n 是工作流自动化；centaur 是 Agent 平台，自主性层级更高

## 是否值得持续跟踪
**值得跟踪（团队 Agent 细分 + 凭据安全视角）。** centaur 探索的"自托管团队 Agent + 凭据安全"是一个真实且有壁垒的细分方向，无论项目本身成败，这一方向值得重视。建议关注：License 是否明确为标准开源（决定社区可行性）、凭据安全模型的工程细节、Paradigm 的投入持续性、以及首批企业采用案例。对关注"组织级 Agent 部署"的团队，centaur 的设计思路（尤其凭据隔离）值得借鉴。对加密/Web3 团队，Paradigm 背书增加了其作为自托管方案的可信度。

## 后续观察点
- License 明确化（是否转为 MIT/Apache，决定开源可行性）
- 凭据安全模型的技术细节公开（验证"用而不见"实现）
- centaur.run 的产品化进展（是否开放注册/公测）
- 首批企业/团队采用案例披露
- Paradigm 是否将此作为战略产品（而非实验）
- 与 MCP/Agent 标准的集成（是否成为标准的多用户 Agent 运行时）

---
> 数据来源: GitHub API (2026-08-07) | Stars: 967 | Forks: 183 | License: NOASSERTION（待明确）| 语言: Python | 官网: centaur.run
