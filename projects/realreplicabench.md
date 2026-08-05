---
title: "Accio-Lab/RealReplicaBench"
slug: "realreplicabench"
date_added: "2026-08-06"
last_seen_date: "2026-08-06"
category: "观察型"
emoji: "📊"
stars: "1,017 stars"
stars_delta: "8/02创建→8/06观测 1,017⭐ / 69 fork / 0 subscribers（API 未返回），v1.3.1"
language: "HTML"
license: "Apache-2.0"
score: 84
tags: ["agent-benchmark", "long-horizon", "stateful-eval", "commerce-workflow", "openclaw", "alibaba"]
url: "https://github.com/Accio-Lab/RealReplicaBench"
---

# Accio-Lab/RealReplicaBench — 长程 agent 状态化 benchmark

## 一句话定位
阿里国际 Accio 团队的长程 agent benchmark，用本地 mock 服务模拟真实 SaaS（电商/物流/消息/文档），评测 agent 能否完成 107 个多步骤、有状态、需改变系统状态的真实业务流任务。

## 它解决的问题
目标用户是 agent 开发者和企业。痛点：现有 agent benchmark 多为单轮/短程问答（SWE-bench 偏代码修复单轮，GAIA 偏知识问答），无法评测"agent 能否完成真实业务流"——多步骤、有状态、需改变系统状态的长程任务。RealReplicaBench 填补这个空白：用本地 mock 服务（阿里发布表单、Freightos 运费预订、Shopify 店面、消息系统、文档系统）让 agent 在新鲜容器中操作并改变状态。

## 为什么值得关注（2026-08-06）

这标志着**长程 agent benchmark 品类的出现**——从"agent 能答什么"（SWE-bench/GAIA）到"agent 能做什么业务流"。1,017⭐ / 69 fork 说明 agent 评测基础设施有真实需求。阿里 Accio 团队背书（非个人项目）+ 107 任务规模 + OpenClaw/Accio 双 harness 参考结果提升了公信力。关键差异化：(a) **状态化评测**（本地 SaaS 副本，非静态测试集）；(b) **长程业务流**（107 任务覆盖浏览器/CLI/API-MCP/文档/电商运营）；(c) **双 harness 参考结果**（OpenClaw 12 模型族 + Accio 13 模型族）。

## 热度来源判断
- **真实需求信号**：69 fork（相对 1,017⭐）说明有团队在尝试运行/适配。阿里国际 Accio 团队背书（非学生/个人项目），有 live leaderboard 和 mock showcase。任务覆盖面（107 任务、8 类业务流）说明是认真构建的 benchmark。
- **话题性成分**：agent benchmark 是当前热点（SWE-bench 衍生项目多），RealReplicaBench 受益于品类热度。subscribers 数据 API 未返回（可能为 0 或私有），深度关注度待验证。

## 关键技术亮点

1. **107 任务三层切片**：65 纯文本 + 20 browser-text-capable + 22 vision-required，覆盖 CLI（53）/browser（28）/file（16）/API-MCP（10）。任务覆盖浏览器操作、native-style CLI 工具、API/MCP 工作流、文档/表格生成、公开网络研究、供应商分析、产品发布、物流、电商运营。
2. **状态化本地 mock 服务**：用本地容器模拟 SaaS（阿里发布表单、Freightos、Shopify、消息、文档系统），agent 必须操作界面并改变状态——不是回答"关于业务的问题"，而是"完成业务操作"。不要求生产账号，降低评测门槛。
3. **新鲜容器 + 完整审计**：每个任务在 fresh container 中运行，保存 resolved config、trajectory、verifier result、artifacts、logs、container metadata。结果可审计。
4. **双 harness 参考结果**：OpenClaw（12 模型族）和 Accio（13 模型族），12 个共有模型可直接比较。judge 为 `gemini-3.1-pro-preview`，公开路径用 bring-your-own credentials。
5. **live leaderboard 为 source of record**：实时更新，README 中的表格为快照。

## 架构启发
RealReplicaBench 的设计哲学是 **"用状态化副本评测真实业务流"**——不问"agent 知道什么"（知识问答），问"agent 能改变什么系统状态"（业务操作）。这对架构师的启发：**agent 的生产价值在于改变系统状态**（下单、发布、配置），而非回答问题。评测 agent 时应优先关注状态改变能力。本地 mock 服务的保真度是关键 trade-off——保真度越高越接近真实但成本越高。

## 定位判断
属于 **L0 评测基础设施层**，是 agent 生态的基础设施（没有可信评测就无法比较 agent 能力）。与 SWE-bench（代码单轮）、GAIA（知识问答）互补，填补"长程状态化业务流"维度。

## 风险 / 局限 / 泡沫点

1. **验证器质量未独立审视**：107 任务的"确定性 vs LLM 辅助"验证器混合比例未明确披露。LLM 辅助验证器（judge 为 gemini-3.1-pro-preview）可能引入 judge 偏差。确定性验证器的覆盖面（多少任务能用纯规则验证）未知。
2. **mock 服务保真度未验证**：本地 mock 对真实 SaaS（Freightos/Shopify/阿里）的界面/行为保真度未独立评估。mock 与真实系统的差异可能导致 benchmark 成绩与生产表现脱节。
3. **强绑定 OpenClaw harness**：README 反复提到 OpenClaw harness（08-04 趋势报告提及的 agent），但 OpenClaw 本身的成熟度和采用度待验证。benchmark 的可用性部分取决于 harness 生态。
4. **subscribers 数据缺失**：API 返回 subscribers 为 0 或未返回，相对 1,017⭐ 偏低，深度关注度待验证。

## 与同类项目的关系
- **vs SWE-bench**：SWE-bench 评测代码修复（单轮、静态测试集），RealReplicaBench 评测业务流（长程、状态化）。维度互补。
- **vs GAIA**：GAIA 评测通用助手问答（知识/推理），RealReplicaBench 评测业务操作（状态改变）。层次不同。
- **vs OpenClaw（harness）**：OpenClaw 是被评测的 harness 之一，RealReplicaBench 是评测工具。两者是"被测物 vs 测量仪"关系。

## 是否值得持续跟踪
**是，作为"长程 agent benchmark 品类"的代表项目跟踪。** 阿里 Accio 背书 + 107 任务规模 + 双 harness 参考结果使其成为可信的 agent 能力评测基准。重点验证验证器质量和 mock 保真度。

## 后续观察点
1. **验证器质量审视**：确定性验证器 vs LLM 辅助验证器的比例，以及 LLM judge 的偏差程度。
2. **mock 保真度**：本地 mock 与真实 SaaS 的差异是否导致 benchmark 成绩与生产脱节。
3. **模型覆盖面扩展**：是否有更多模型族加入 leaderboard，以及 pre-release/internal 模型的评测透明度。

---
*首次记录：2026-08-06* · *数据来源: GitHub API + 仓库 README*
