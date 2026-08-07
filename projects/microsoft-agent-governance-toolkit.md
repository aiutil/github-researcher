---
title: "microsoft/agent-governance-toolkit"
slug: microsoft-agent-governance-toolkit
date_added: 2026-06-02
last_seen_date: 2026-06-02
category: "Agent Infra"
emoji: "🛡️"
stars: "5,703 stars"
score: 87
tags: ["agent-governance", "security", "policy-enforcement", "owasp"]
url: "https://github.com/microsoft/agent-governance-toolkit"
---

# microsoft/agent-governance-toolkit

## 一句话定位
微软出品的 AI Agent 治理工具包，提供策略执行、零信任身份、执行沙盒和可靠性工程能力，覆盖 OWASP Agentic Top 10 全部 10 项安全风险。

## 它解决的问题
AI Agent 正获得越来越大的自主权——可以调用 API、执行代码、访问数据、发送消息。但"自主"也意味着"风险"：Agent 可能被 Prompt 注入攻击劫持、执行未授权操作、泄露敏感数据、产生不可控的连锁行为。Agent Governance Toolkit 解决的是"如何让 Agent 在安全边界内自主行动"——在不牺牲自主性的前提下，提供策略执行、身份验证、操作审计和安全沙盒。

## 为什么值得关注
- **Stars:** 5,703 stars，2026 年 3 月创建后快速增长
- **微软官方出品:** 在 AI 安全领域的权威性背书
- **OWASP Agentic Top 10 全覆盖:** 对标 OWASP Web Top 10，为 Agent 安全提供标准化的风险分类和防护
- **零信任架构:** 不默认信任任何 Agent 操作，每次操作都需验证和授权
- **执行沙盒:** Agent 的代码执行在隔离环境中运行，防止宿主被破坏
- **多语言支持:** 提供英文、日文、中文、韩文文档

## 热度来源判断
Agent Governance Toolkit 的热度来自"Agent 安全"从理论讨论转向工程实践的关键节点。2026 年随着 Agent 在生产环境中部署增加，安全事件（Agent 被劫持、数据泄露、未授权操作）开始出现，企业急需治理工具。微软在这一时机推出覆盖 OWASP Agentic Top 10 的工具包，切中了市场需求。Star 数从 0 到 5.7K 的增长反映了"Agent 安全"赛道的升温。

## 关键技术亮点
- **策略引擎（Policy Engine）:** 以声明式策略定义 Agent 的行为边界（可以做什么、不可以做什么），运行时强制执行
- **零信任身份:** 每个 Agent 操作都经过身份验证和权限检查，不依赖隐式信任
- **执行沙盒（Execution Sandboxing）:** Agent 的代码执行在隔离容器中运行，限制文件系统、网络和系统调用访问
- **可靠性工程（Reliability Engineering）:** 监控 Agent 行为模式，检测异常和偏离预期的情况
- **OWASP Agentic Top 10 映射:** 每项防护措施明确对应 OWASP Agentic Top 10 中的具体风险

## 架构启发
Agent Governance Toolkit 的核心架构启发是"治理优先于能力"——在赋予 Agent 自主权之前，先定义安全边界。其策略引擎将"安全策略"从代码中分离为声明式配置（类似 Kubernetes 的 RBAC / NetworkPolicy），使得安全策略可以被审计、版本管理和集中管理。零信任架构在 Agent 领域的应用也值得借鉴——不信任 Agent 的"善意"，而是通过技术手段强制每次操作都经过验证。

## 定位判断
**基础设施型项目（早期成长期）。** Agent Governance Toolkit 定位为 Agent 生态的"安全基础设施"。如果 Agent 成为软件的主流形态，治理工具将成为必需品。它不是"又一个 Agent 框架"，而是"让 Agent 框架安全运行的底层依赖"。类似于 Kubernetes 之于容器编排的治理层。

## 风险 / 局限 / 泡沫点
- **采用门槛:** 需要企业理解并接受"Agent 治理"的概念，目前市场教育不足
- **性能开销:** 策略执行和沙盒隔离会带来性能开销
- **标准竞争:** OWASP Agentic Top 10 虽有影响力，但是否成为行业标准尚不确定
- **与 Agent 框架的集成:** 需要与 LangGraph、CrewAI、AutoGPT 等框架深度集成才能发挥作用，目前集成度待验证
- **概念早期:** "Agent 治理"作为独立领域是否成立，还是会被吸收进通用安全工具

## 与同类项目的关系
- **vs OWASP Top 10 for LLMs:** OWASP Top 10 for LLMs 关注模型安全，Agent Governance 关注 Agent 行为安全
- **vs LangGraph Guardrails:** LangGraph 有内置的 guardrails，但不如 Agent Governance Toolkit 系统
- **vs NVIDIA NeMo Guardrails:** NeMo Guardrails 关注对话安全，Agent Governance 关注行为安全
- **vs Kubernetes RBAC / OPA:** 传统云原生安全工具关注基础设施，Agent Governance 关注 AI Agent
- **vs imran-siddique/agent-os (deprecated):** 该项目已迁移到 microsoft/agent-governance-toolkit

## 是否值得持续跟踪
**是。** Agent 安全是 Agent 大规模部署的前提条件。如果 Agent 治理成为标配（类似 HTTPS 之于 Web），Agent Governance Toolkit 有潜力成为标准工具。值得关注的是：与主流 Agent 框架的集成、OWASP Agentic Top 10 的行业接受度、以及真实部署案例。

## 后续观察点
- 与主流 Agent 框架（LangGraph、CrewAI、AutoGPT、Dify）的原生集成
- OWASP Agentic Top 10 的行业接受度和标准化进展
- 企业采用案例（尤其是金融、医疗等高合规行业）
- 策略引擎的表达能力和性能优化
- 是否从工具包升级为平台 / 服务

---
> 数据来源: GitHub API (2026-08-07) | 首次发现: 2026-06-02
