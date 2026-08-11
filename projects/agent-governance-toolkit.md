---
title: "agent-governance-toolkit"
slug: "agent-governance-toolkit"
date_added: "2026-05-29"
last_seen_date: "2026-08-11"
category: "基础设施候选"
emoji: "🛡️"
stars: "5,867 stars"
stars_delta: "从 3.6K→5.9K（约 10 周），周增 ~230，覆盖 OWASP Agentic Top 10，Public Preview"
language: "Python"
license: "MIT"
score: 86
tags: ["Agent治理", "安全", "OWASP", "Microsoft", "合规", "零信任", "policy-engine"]
url: "https://github.com/microsoft/agent-governance-toolkit"
---

# Microsoft Agent Governance Toolkit (AGT)

## 一句话定位
Microsoft 出品的 AI Agent 安全治理工具包，在**工具调用执行前用确定性代码拦截**（非 prompt 规则），提供策略执行、零信任身份、执行沙箱和可靠性工程，是业界唯一声称覆盖 OWASP Agentic Top 10 全部 10 项的开源工具包。

## 它解决的问题
Agent 部署到生产环境后，面临三个核心安全问题：

1. **动作授权**：Agent 有 `send_email` 和 `query_database` 权限，不应该能 `drop_table`。OAuth scopes 和 IAM 角色控制的是 Agent 能连接哪些服务，**而非连上后做什么**。
2. **身份追溯**：5 个 Agent 共享一个 API key 时，出问题无法定位"哪个 Agent 干的"。
3. **审计追踪**：审计需要防篡改的决策记录——当时什么策略生效、Agent 请求了什么、为什么被允许或拒绝。

Prompt 级安全（"请遵守规则"）不是控制面，是对随机系统的礼貌请求。OWASP LLM01:2025 明确指出"无法保证 Prompt Injection 有万无一失的防护"。Andriushchenko 等人（ICLR 2025）报告 GPT-4o/Claude 3/Llama-3 的自适应攻击成功率达 **100%**。AGT 不在 prompt 层打这场仗——每次工具调用、消息发送、委托操作都在确定性应用代码中被拦截。**被拒绝的操作不是"不太可能执行"，而是结构上不可能执行。**

## 为什么值得关注（2026-08-11）
- **Stars:** 5,867（从 5 月底的 3.6K 增长约 63%），Forks 1,017，社区参与度高
- **Microsoft 出品**：工程质量、文档质量和长期维护有保障
- **OWASP Agentic Top 10 全覆盖**：业界唯一声称覆盖 10/10 的工具包，且获 AARM Extended (R1–R9) 和 ATF 全 5 要素认证
- **三平台 SDK**：Python（PyPI `agent-governance-toolkit`）/ npm（`@microsoft/agent-governance-sdk`）/ NuGet（`Microsoft.AgentGovernance`）
- **Claude Code Plugin 集成**：一行命令安装为 Claude Code 治理插件
- **OpenSSF 双认证**：Scorecard + Best Practices，供应链安全达标
- **持续活跃**：pushed_at 2026-08-10，几乎每日更新

## 热度来源判断
AGT 的热度来自 **"企业 Agent 安全合规的刚性需求 × Microsoft 品牌背书 × 确定性拦截的技术差异化"** 三重驱动。企业 Agent 部署的最大阻碍不是模型能力，而是安全合规审计——SOC 2、ISO 27001 等要求可追溯的操作日志。AGT 是目前唯一系统性解决这一问题的开源方案。5.8K stars 中有相当比例来自企业安全团队的评估采纳，而非纯社区围观。热度**真实且具有基础设施级粘性**——一旦集成进 Agent 架构，迁移成本极高。

## 关键技术亮点亮点
1. **确定性拦截（核心差异化）**：在工具调用前用代码拦截，被拒绝操作"结构上不可能执行"，而非"不太可能"。这是概率性 prompt 防御与确定性安全控制的根本分野
2. **`govern()` 两行代码接入**：`safe_tool = govern(my_tool, policy="policy.yaml")`，每次调用自动检查策略、记录审计日志、违反时抛出 `GovernanceDenied`
3. **YAML 策略引擎**：声明式策略定义（`apiVersion: governance.toolkit/v1`），支持 allow/deny/conditional 等丰富规则
4. **OWASP Agentic Top 10 全覆盖**：10/10 项均有对应架构控制，文档化映射关系
5. **多框架兼容**：Claude Code Plugin + 通用 Python SDK + npm/NuGet SDK，不绑定特定 Agent 框架
6. **审计日志**：防篡改的决策记录，记录策略版本、请求内容、决策原因，满足合规审计
7. **零信任身份**：每个 Agent 有独立身份，解决多 Agent 共享 API key 的追溯问题

## 架构启发
- **安全不是功能，是架构**：Agent 安全需要在架构层面设计（工具调用拦截层），而非事后加 prompt 规则。这与零信任网络的设计哲学一脉相承
- **确定性 > 概率性**：对于安全场景，模型层的概率性防御（prompt guardrails）永远不够，需要代码层的确定性控制。AGT 的设计基于一个清醒认知：**模型会犯错，但 Runtime 不应该**
- **治理即基础设施**：Agent 治理应该像 IAM 一样成为基础设施层——每次 API 调用经过认证授权，每次 Agent 操作经过策略检查和审计记录
- **声明式策略优于硬编码**：YAML 策略文件让安全规则可版本化、可审计、可 diff，符合 GitOps 理念

## 定位判断
**基础设施候选——企业 Agent 落地的必经之路。** AGT 不是工具库，而是 Agent 安全治理的**控制面**。它的定位类比：IAM 之于云服务、OPA 之于 Kubernetes 策略、WAF 之于 Web 应用。如果 Agent 成为企业的标准计算单元，那么 Agent 操作的认证/授权/审计将成为合规基础设施。AGT 有潜力成为这个层面的事实标准——Microsoft 出品 + OWASP 全覆盖 + 多语言 SDK 构成了标准制定者的初始条件。5,867 stars 和 1,017 forks 显示企业社区已经开始采用。

## 风险 / 局限 / 泡沫点
1. **Public Preview 阶段**：明确标注可能有 breaking changes，`agent_os` 模块已废弃（迁移到 `agentmesh`），v4→v5 策略迁移需要手动执行。不适合未经评估直接进生产
2. **策略编写复杂度**：YAML 策略虽声明式，但复杂场景（条件授权、委托链、多 Agent 协作）的策略编写需要专业知识
3. **性能开销**：每次工具调用都经过拦截和审计，在高频调用场景下可能成为瓶颈
4. **与现有 IAM/SIEM 的集成**：企业已有安全基础设施（Okta、Azure AD、Splunk），AGT 需要与这些系统深度集成而非替代
5. **Microsoft 锁定风险**：虽 MIT 开源，但深度依赖 Microsoft 生态（Azure Monitor、Application Insights）可能引入隐性锁定
6. **社区生态规模**：1K forks 中有多少转化为实际生产部署尚不清楚

## 与同类项目的关系
- **vs Prompt 级安全（Claude Guardrails / NeMo Guardrails）**：AGT 是确定性代码拦截，在工具调用层而非文本生成层。两者互补——prompt 级过滤输入，AGT 拦截执行
- **vs Agent 沙箱（E2B / Daytona）**：E2B 是运行时隔离（Agent 在沙箱内执行代码），AGT 是策略治理（决定 Agent 能否执行某操作）。正交互补
- **vs google/ax（Agent Runtime）**：ax 管"Agent 怎么跑"（分布式运行时），AGT 管"Agent 不能做什么"（安全治理）。天然搭档
- **vs OPA（Open Policy Agent）**：OPA 是通用策略引擎，AGT 是 Agent 专用。OPA 更通用但缺乏 Agent 领域的原语（工具调用、委托链等）
- **vs OWASP LLM Top 10 指南**：OWASP 是指南文档，AGT 是工程实现。AGT 把指南变成了可运行的代码

## 是否值得持续跟踪
**强烈建议持续跟踪。** 企业 Agent 安全是刚需——没有可审计的安全控制，Agent 永远无法进入生产环境。AGT 是目前最系统性的开源解决方案，Microsoft 出品增加了标准化可能性。对安全工程师和平台架构师，AGT 是直接可用的工具；对 Agent 生态观察者，它是"Agent 安全治理"赛道的标杆项目。建议同时关注 google/ax（Agent Runtime）——两者组合可能构成企业 Agent 基础设施的核心栈。

## 后续观察点
1. **GA 时间线和稳定性承诺**：何时从 Public Preview 到 GA，breaking changes 何时收敛
2. **主流 Agent 框架的官方集成**：是否被 LangChain、CrewAI、Claude Code、Codex 等默认集成
3. **企业生产部署案例**： Fortune 500 企业是否公开采用 AGT 作为 Agent 安全标准
4. **与 OPA / SPIFFE / cloud-native 安全生态的集成**：是否成为 CNCF 生态的一部分
5. **策略市场**：是否出现社区共享的 Agent 安全策略库（类比 OPA 的策略库）
6. **竞品响应**：AWS / Google Cloud 是否推出类似的 Agent 治理工具

---
> 数据来源: GitHub API (2026-08-11) | Stars: 5,867 | Forks: 1,017 | License: MIT | 语言: Python | 创建: 2026-03-02 | pushed: 2026-08-10
