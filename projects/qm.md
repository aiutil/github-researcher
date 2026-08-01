---
title: "yc-software/qm"
slug: "qm"
date_added: "2026-08-01"
last_seen_date: "2026-08-02"
category: "平台候选"
emoji: "👥"
stars: "4,782 stars"
stars_delta: "7/29创建→8/01 1,367⭐→8/02 4,782⭐（24h +250%/+3,415），fork 125→469（+344）"
language: "TypeScript"
license: "MIT"
score: 89
tags: ["agent-harness", "multiplayer", "slack", "collaboration", "sandbox", "typescript", "multi-agent"]
url: "https://github.com/yc-software/qm"
---

# qm — 多人协作 agent harness for work

## 一句话定位
面向初创团队的多 player agent harness，Slack + Web 双入口，每人独立沙箱/记忆/权限/技能，统一编排 Pi/OpenCode/Claude Code/Codex。

## 它解决的问题
现有 coding agent（Claude Code、Codex 等）都是为单用户设计的个人助手。当整个团队要用 agent 时，缺一个"每人有自己的 agent 空间、又能协同"的平台。qm 面向的就是这个 gap：让初创团队的每个员工都有独立的 agent 工作区，同时在 Slack 频道和项目里协作。

## 为什么值得关注（2026-08-01）

在昨日（07-31）grok-build/omnigent/eve 把 harness 层多极化之后，今天 harness 的竞争前沿明显扩散到**应用层产品形态**。qm 是其中最清晰的一个——它不造新 harness，而是把现有 harness（Pi/OpenCode/Claude Code/Codex）做成**多人协作平台**。3 天 1.4K⭐ 说明"团队级 agent 协同"是真实需求。

## 热度来源判断
- **真实需求信号**：fork 125（高于同期 star 量级项目），说明有团队在尝试部署；README 详细的安全策略（Strict/Auto/Dangerous 三档）和部署目录架构说明这是认真做的产品而非 demo。
- **话题性成分**：harness 应用化是本周热点，qm 受益于品类热度；但"multiplayer"和"Slack 集成"是独立差异化，非纯蹭热度。

## 关键技术亮点

1. **Per-scope durable sandbox**：每人/每房间有独立的文件、工具、已登录服务——这是隔离的核心。README 架构图显示 agent 通过 `execute` 工具在 scope 自己的沙箱里运行命令，"installed tools stay installed"。
2. **Harness 无关的 core**：中央 core 用 TypeScript + Fastify，agent loop 支持多种 harness（Pi/OpenCode/Claude Code），所有 substrate（harness/session store/sandbox/memory）都在接口后面，生产实现通过一个 wiring 文件替换。
3. **Slack + Web 统一身份**：同一身份和配置在 Slack 和 Web 间无缝切换；Slack 是可选的 in-process plugin，由 core 启动和监督。
4. **Org 级安全策略**：Strict（每次工具调用需人工审批）/ Auto（默认，分类器筛外部数据）/ Dangerous（无筛选无暂停）三档，且 scope 只能收紧不能放松 org 策略。预声明命令策略（审批规则 + 硬拒绝递归删除/破坏性 SQL）在所有 posture 下生效。

## 架构启发
qm 的分层很清晰：headless core（API/identity/policy/scheduler + agent loop）→ per-scope sandbox → 可选插件（web UI/admin panel/Slack）。这种"core 无关 harness、一切通过接口"的设计让它在 harness 快速迭代时有一定韧性。但也意味着它对上游 harness 的依赖是结构性的——如果 Claude Code/Codex 的 API 发生 breaking change，qm 的适配成本会很高。

## 定位判断
在 agent 生态分层中，qm 占据 **L5 应用产品层**——在 harness 本体（L1）、编排层（L3）、开发范式（L2）之上的产品化。它与 cindy（开箱即用单机客户端）的差异在于：qm 面向**团队协同**（多人 scope + Slack），cindy 面向**个人异构组合**（多 harness 混合驱动）。

## 风险 / 局限 / 泡沫点

1. **极早期项目**：创建于 2026-07-29（3 天），1.4K⭐，生产部署案例未见。README 虽详细但"deploy it for your org"的承诺未经大规模验证。
2. **上游 harness 依赖**：Pi/OpenCode/Claude Code/Codex 都在快速迭代，qm 的 multi-harness 抽象层维护成本可能随上游 breaking change 线性增长。
3. **Slack 集成深度待验证**：Slack 作为 in-process plugin 的稳定性、并发会话处理、消息一致性在实际团队场景下未经检验。
4. **安全模型依赖人工策略**：Strict 模式下"每次工具调用暂停审批"在真实团队场景可能不可持续；Auto 模式的分类器筛外部数据的效果未经安全审计。

## 与同类项目的关系

- **vs omnigent（7.9K⭐）**：omnigent 是 meta-harness 编排层（L3），qm 是应用平台（L5）。omnigent 更偏"管理多个 agent"，qm 更偏"让团队用 agent 协同"。抽象层次不同，但 qm 的 harness 无关 core 与 omnigent 的 transport 抽象层有概念重叠。
- **vs cindy（1.3K⭐）**：cindy 是单机客户端（桌面+移动），qm 是团队平台（Slack+Web）。cindy 强调"多 harness 混合驱动 + 中途切换"，qm 强调"多人 scope + 协同"。
- **vs openworker（11.3K⭐）**：openworker（Andrew Ng）是"本地优先 AI Coworker 交付成品"，更偏个人/审批门控；qm 更偏团队协作。

## 是否值得持续跟踪
**是，作为"harness 应用层产品化"趋势的代表项目跟踪。** 关注其 per-scope sandbox 的实际隔离强度和 Slack 集成的生产稳定性。

## 后续观察点
1. **fork 增速 vs star 增速**：如果 fork 持续高于同期项目，说明真实部署在增加；如果只有 star 涨，则可能只是品类热度。
2. **上游 harness breaking change 的影响**：观察 Claude Code/Codex 下一次大版本更新后 qm 的适配速度和 issue 数变化。
3. **Slack 集成的并发瓶颈**：当多个用户同时在 Slack 触发 agent 时，in-process plugin 模式是否扛得住。

## 最近动态（2026-08-02）

- **24h 爆发**：1,367 → 4,782（+3,415，+250%），fork 同步 125 → 469（+344）。**fork 与 star 同步暴涨**是真实部署意愿的强信号（对比 decimen-optical-transfer 3K⭐ 仅 19 watcher / stargazers 接口异常的刷星特征）。
- **全站排名**：在 created>2026-07-20, stars>300 的搜索里，qm 已是仅次于 Kimi-K3 本体（7,817⭐）的第二名，且日增速（+3,415）远超 K3（+108）。
- **判断修正**：昨日"应用层产品化"从趋势判断升级为**市场既成事实**。score 86 → 89（热度质量、中期趋势概率两维提升）。
- **脉冲性待验**：+250% 可能部分来自登上 trending 后的注意力脉冲。明后日若回落到 +几百/天属脉冲；若维持 +1000/天量级则确认进入主流。

---
*首次记录：2026-08-01* · *最近更新：2026-08-02（24h +250%，score 89）*
