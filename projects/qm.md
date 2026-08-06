---
title: "yc-software/qm"
slug: "qm"
date_added: "2026-08-01"
last_seen_date: "2026-08-07"
category: "平台候选"
emoji: "👥"
stars: "12,022 stars"
stars_delta: "7/29创建→8/07 12,022⭐（第六日 +369，+3%，接近停滞），fork 1,290→1,349，六日累计 +10,655"
language: "TypeScript"
license: "MIT"
score: 88
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

## 最近动态（2026-08-03）

- **第二日续涨回答"脉冲 vs 趋势"之问**：4,782 → 7,015（+2,233，+47%），fork 469 → 736（+267）。增速百分比从 +250% 正常化到 +47% 是健康的衰减曲线，但**绝对量级仍远超同期一切项目**（K3 今日仅 +75）。**这不是脉冲崩塌，而是趋势的第二天确认。**
- **全站第一**：在 created>2026-07-27, stars>300 的搜索里，qm（7,015⭐）已是全站第一名，超过 decimen-optical-transfer（3,620⭐，疑似刷星，昨日 3,031→今日 3,620 几乎停滞，印证刷星判断）和所有 K3 衍生项目。
- **两日累计**：从 08-01 的 1,367 到 08-03 的 7,015，两日 +5,648 stars / +611 forks。fork 持续同步增长进一步确认真实部署意愿。
- **判断修正**：score 89 → 90。"应用层产品化"从"市场既成事实"确认为**持续性趋势**（两日数据支撑）。第三日（08-04）若仍维持 +1000/天量级则完全确认。
- **待观察**：open issues 85（昨日数据），pushed_at 停在 08-01（代码未更新，热度由已有版本驱动）。

## 最近动态（2026-08-04）

- **第三日续涨 +2,443，应用层产品化趋势完全确认**：7,015 → 9,458（+2,443，+35%），fork 736 → 998（+262）。连续三日正增量：+3,415（08-02）/ +2,233（08-03）/ +2,443（08-04），**三日无一日回落，且第三日增量反而高于第二日**——这彻底排除了"脉冲"假设。增速百分比 +250% → +47% → +35% 是健康衰减，但绝对量级稳定在 +2000/天以上。
- **三日累计**：从 08-01 的 1,367 到 08-04 的 9,458，三日 +8,091 stars / +873 forks（fork 125→998）。fork 持续高比例同步增长，是真实部署意愿的强信号。
- **判断修正**：score 维持 90（已处于高位）。"应用层产品化"从"持续性趋势（两日支撑）"升级为**完全确立的趋势（三日支撑，无衰减崩塌）**。待观察从"是否趋势"转为"趋势天花板在哪"——突破 10K⭐ 后的增速是下一观察点。
- **待观察**：open_issues 113（较 08-03 的 85 上升），subscribers 仅 47（相对于 9.4K⭐ 偏低），pushed_at 停在 08-03。

## 最近动态（2026-08-05）

- **第四日突破 10K 关口**：9,458 → 11,092（+1,634，+17%），fork 998 → 1,200（+202）。增速继续健康衰减（+250%→+47%→+35%→+17%），绝对量级从 +2,443 降到 +1,634——这是趋势确立后的正常降温，非崩塌。四日累计 +9,725 stars / +1,075 forks（fork 125→1,200）。
- **关键转折：增速被 crm 反超**：qm 第四日 +17%，而 crm +46%、genoffice +125%。**应用层从"齐涨"进入"分化"**——qm 仍是量级龙头（11K⭐），但不再是增速最快的应用层项目。这说明市场开始在多路线间区分 PMF 强度。
- **数据细节**：open_issues 105（较 08-04 的 113 下降，健康的 issue 处理），subscribers 51（相对 11K⭐ 偏低），pushed_at 停在 08-04（热度由已有版本驱动）。
- **判断**：score 维持 90。qm 的量级护城河确立，但增速衰减 + 被反超意味着下一阶段的关键问题是"能否守住通用平台位置"而非"是否趋势"。

---
*首次记录：2026-08-01* · *最近更新：2026-08-06（第五日增速骤降 +561/+5%，11,653⭐，仍守万星量级，score 90→89）*

## 最近动态（2026-08-06）

- **第五日增速骤降 +561（+5%），衰减斜率显著加大**：11,092 → 11,653，fork 1,200 → 1,290。增速序列 +250%→+47%→+35%→+17%→+5%，第五日从 +17% 骤降到 +5%，衰减斜率在第五日显著加大。五日累计 +10,286 stars / +1,165 forks。
- **关键转折：crm 连续两日增速领先，"crm 领跑、qm 守量"格局确立**：qm +5% vs crm +34%，差距从昨日（+17% vs +46%）进一步扩大。qm 仍是量级龙头（11.7K⭐），但增速接近停滞，可能触及自然热度上限。crm（6.1K⭐）持续放量追赶。
- **数据细节**：open_issues 101（健康），subscribers 52（相对 11.7K⭐ 偏低），pushed_at 仍停在 08-04（热度由已有版本驱动，无新代码刺激）。
- **判断修正**：score 90 → 89。增速骤降 + 被反超差距扩大。下一观察点：+5% 是否进一步降到 +1-2%（则 qm 热度基本结束），还是企稳（则进入万星稳态）。

## 最近动态（2026-08-07）

- **第六日接近停滞 +369（+3%），万星量级为最终稳态**：11,653 → 12,022，fork 1,290 → 1,349（+59）。增速序列 +250%→+47%→+35%→+17%→+5%→+3%，已明确进入停滞通道。08-06 判断的"接近自然热度上限"被今日 +3% 数据证实。
- **格局固化**：qm +3% vs crm +16%，差距仍在但两者都在减速。qm 守住 12K 量级（绝对增量 +369 仍为正），但增长动能基本消失。
- **判断修正**：score 89 → 88。增速接近停滞，万星量级为最终稳态。pushed_at 仍停在 08-04（无新代码刺激）。open_issues 112（略升，健康的社区反馈）。
- **下一观察点**：+3% 是否进一步降到 +1-2%（则 qm 热度基本结束），还是企稳在 +2-3%（则进入万星稳态）。
