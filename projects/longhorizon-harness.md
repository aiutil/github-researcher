---
title: "AMAP-ML/LongHorizon-Harness"
slug: longhorizon-harness
date_added: 2026-08-08
last_seen_date: 2026-08-08
category: "观察型"
emoji: "🧭"
stars: "384 stars"
score: 83
tags: ["long-horizon-agents", "computer-use", "claude-code", "codex", "state-management", "verification", "harness", "loop-engineering"]
url: "https://github.com/AMAP-ML/LongHorizon-Harness"
---

# AMAP-ML/LongHorizon-Harness

## 一句话定位
长程（long-horizon）计算机操作 agent 的执行/状态管理/结果验证 harness——通过"管理-执行-审计"三角色分离 + 持久化可信状态，让 agent 在真实桌面和 CLI 环境中连续工作数十小时且进度可验证、可恢复，兼容 Claude Code 和 Codex。

## 它解决的问题
当前 agent 的核心瓶颈已不是"单轮能做什么"，而是**"能否在数十小时的长程任务中保持状态一致性、验证进度、故障恢复"**。具体痛点：单一不断增长的 context 负责一切（规划+执行+验证）→ 状态漂移、无法验证完成度、"done"只意味着"agent 停止说话"、重试是冷启动丢失学到的上下文、唯一 trace 是要像小说一样读的 transcript、跑两次得到两个不同系统。LongHorizon-Harness 直击这些长程 agent 的工程化痛点。

## 为什么值得关注
- **Stars:** 384（截至 2026-08-08），创建 2026-08-04，4 天破 384
- **Forks:** 40
- **Watchers/Subscribers:** 2（偏低）
- **Open Issues:** 5
- **License:** MIT
- **语言:** Python
- **活跃度:** created 2026-08-04，pushed_at 2026-08-07，v0.1.3 已发布（快速迭代）
- **学术背书:** arXiv 2608.01964，HuggingFace Daily Papers 周榜 #1（2026-W32，可核验）
- **机构:** AMAP-ML（高德地图 AI 团队，可从 org 名推断）
- **兼容:** Claude Code + Codex + OpenClaw 原生集成
- **Benchmark:** WeaveBench / OSWorld 2.0 / Terminal-Bench 2.1

## 热度来源判断
LongHorizon-Harness 的热度来自**"长程 agent 是公认瓶颈 × 学术论文背书 × HuggingFace Daily Papers 周榜 #1 的曝光"**。HuggingFace Daily Papers 周榜 #1（可核验）是最强信号——这带来了学术和工程社区的双重关注。384⭐ / 40 fork 说明关注者中有实际部署意愿。但 **2 watchers 偏低**——与 star 数不匹配，说明热度更多来自论文曝光的"一次性关注"，深度跟踪意愿有限。这与 super-simple-software-factory（14 watchers / 459⭐）的模式类似：关注 > 深度跟踪。热度**真实但有论文驱动的脉冲成分**——需观察论文曝光红利消退后的留存。

## 关键技术亮点
1. **三角色分离（Manager / Executor / Auditor）:** Manager 维护原始目标+已验证进度+下一步；Executor 每轮 fresh context 只做一个明确任务；Auditor 独立检查文件/接口/日志/测试。只有通过独立验证的结果才进入持久化状态。
2. **持久化可信状态（durable verified state）:** 即使 context 刷新、action 失败、deliverable 未通过检查，系统仍保留已验证的进度并从剩余部分继续
3. **Fresh-context 执行:** 每轮执行从全新 context 开始，避免长程 context 膨胀
4. **独立审计（independent auditing）:** Auditor 角色只读检查，与 Executor 隔离
5. **可恢复进度（recoverable progress）:** 故障后从验证状态恢复，非冷启动
6. **v0.1.3 快速迭代:** 每轮以自然语言回复（基于验证状态），按启动目录操作，实时报告

## 架构启发
LongHorizon-Harness 的核心启发是**"长程 agent 的可靠性不是模型问题，而是架构问题"**——README 明确声明"模型决定 agent 单轮能做什么，harness 决定这些工作能否被验证、保留和持续直到任务真正完成"。这与 super-simple-software-factory（"Python 拥有控制平面"）和 RealReplicaBench（"状态化评测"）共同构成一个主题：**"agent 工程化"从 prompt 工程转向架构工程**。三角色分离（规划/执行/验证）是经典的分离关注点原则在 agent 领域的应用——人类组织中这三个角色也总是分离的（项目经理/执行者/QA）。更深层的启发：**"fresh context"可能是长程 agent 的必然选择**——与其维护一个不断膨胀的 context，不如每轮重置并从持久化状态恢复，这与"无状态服务"的云原生理念同构。

## 定位判断
**架构参考型项目（长程 agent harness）。** LongHorizon-Harness 的价值在于提出了一个**可复现的长程 agent 架构范式**（三角色分离 + 持久化可信状态 + fresh-context 执行），而非具体工具。HuggingFace Daily Papers 周榜 #1 + arXiv 论文提供了学术可信度。它不替代任何 agent（明确声明 runs on top of Claude Code/Codex），而是为长程任务提供可靠性层。定位类似 super-simple-software-factory 但更学术化——后者是"实用工程范式"，前者是"学术验证的架构模式"。若论文的 benchmark 结果（WeaveBench/OSWorld 2.0/Terminal-Bench 2.1）经独立复现，会成为长程 agent 的参考架构。

## 风险/局限/泡沫点
- **watchers 仅 2:** 深度关注度极低，热度有论文曝光脉冲成分
- **benchmark 结果未独立复现:** WeaveBench/OSWorld 2.0/Terminal-Bench 2.1 的"measured gains"为论文自报，需独立验证
- **机构属性:** AMAP-ML 为高德地图团队（推断），长程 agent harness 与其核心业务（地图/导航）的关系不明，可能是研究探索而非产品投入
- **"数十小时"为设计目标:** README 声明"work for dozens of hours"，实际长程稳定性未独立验证
- **依赖底层 agent:** 完全依赖 Claude Code/Codex/OpenClaw，底层 agent 的限制会传导
- **OpenClaw 兼容性:** README 提及 OpenClaw 集成，但 OpenClaw 本身成熟度待确认

## 与同类项目的关系
- **vs super-simple-software-factory:** 两者都主张"确定性代码拥有控制平面、agent 为有界节点"；sss-factory 聚焦 SDLC 编排，LongHorizon-Harness 聚焦长程计算机操作——同主题不同场景
- **vs RealReplicaBench:** RRB 评测长程 agent（benchmark），LongHorizon-Harness 提供长程 agent 运行时（harness）——评测 vs 运行时
- **vs Claude Code / Codex 原生:** 它们是 agent，LongHorizon-Harness 是运行在它们之上的可靠性层——增强而非替代
- **vs OpenAI CUA / Anthropic computer use:** 那些是模型能力，LongHorizon-Harness 是工程化框架——不同层次

## 是否值得持续跟踪
**值得跟踪（长程 agent 架构参考）。** LongHorizon-Harness 提出了长程 agent 的核心架构问题（状态管理/验证/恢复）和一个具体的解决方案（三角色分离）。HuggingFace Daily Papers 周榜 #1 提供了学术背书。建议关注：benchmark 结果的独立复现、watchers 是否随论文红利消退而增长（判断真实留存）、三角色分离在实际生产中的效果反馈、AMAP-ML 是否持续投入（vs 学术一次性发表）。

## 后续观察点
- 论文 benchmark（WeaveBench/OSWorld 2.0/Terminal-Bench 2.1）的独立复现结果
- watchers 增长趋势（论文红利消退后是否有人持续跟踪）
- 是否有生产环境使用案例
- AMAP-ML 的持续投入程度（研究 vs 产品）
- 三角色分离范式是否被其他 harness 采纳（架构影响力指标）

---
> 数据来源: GitHub API (2026-08-08) | Stars: 384 | Forks: 40 | Watchers: 2 | License: MIT | 语言: Python | 创建: 2026-08-04 | 论文: arXiv 2608.01964 | HF Daily Papers 周榜 #1 (2026-W32，可核验)
