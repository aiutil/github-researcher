---
title: "Vibe-Trading"
slug: "vibe-trading"
date_added: "2026-07-14"
category: "工具型"
emoji: "📈"
stars: "21,656 stars"
stars_delta: "日增 1,148"
language: "Python"
score: 80
tags: ["trading-agent", "multi-agent", "finance", "llm", "multi-market", "a-share"]
url: "https://github.com/HKUDS/Vibe-Trading"
---

# Vibe-Trading

## 一句话定位
个人交易 Agent——多 LLM Provider 支持，覆盖美股/港股/A股/印度 NSE/BSE，460 个 Alpha 因子，多 Agent Swarm 辩论决策，从研究到执行的完整交易流水线。

## 它解决的问题
个人投资者面临信息过载、多市场数据分散、情绪化决策等问题。Vibe-Trading 将多 Agent 辩论 + 多市场数据 + 多 LLM 推理整合为一个可运行的交易 Agent 系统，让普通投资者也能获得机构级的投研能力。

## 为什么值得关注（2026-07-14）
21.6K⭐ 日增 1.1K，GitHub Trending 日榜排名第二（仅次于 OpenCut）。继 ai-hedge-fund 和 TradingAgents 之后，Vibe-Trading 是交易 Agent 赛道的最新整合者——它不只是单市场策略，而是覆盖美股、港股、A股、印度市场的多市场交易 Agent，且支持 GLM/Kimi/Claude/OpenAI 等多个 LLM Provider。

## 热度来源判断
- 交易 Agent 是"AI 变现"最直接的叙事——热度持续高
- 多市场覆盖（特别是 A 股和印度市场）触达了全球增长最快的两个零售投资市场
- HKUDS（香港大学数据科学实验室）学术背景带来信任
- 社区贡献活跃：近期 PR 涵盖印度市场引擎、A 股因子、Docker 修复等

## 关键技术亮点
1. **多市场引擎**：美股 + 港股 + A股 + 印度 NSE/BSE，每个市场有独立的交易规则引擎（T+1、涨跌停、费用结构）
2. **460 个 Alpha 因子**：包含 Alpha101、Qlib158、SEC 基本面因子，PIT-safe（Point-in-Time 安全）
3. **Swarm 多 Agent 辩论**：多角色 Agent 各自分析后辩论决策，降低单一模型偏见
4. **多 LLM Provider**：OpenAI/Claude/Kimi/GLM/Codex，用户可自选模型
5. **Docker 一键部署**：FastAPI 服务化，支持本地/云端部署
6. **API Server 模块化**：从 1,103 行重构为 371 行，工程质量持续提升

## 架构启发
Vibe-Trading 的多市场引擎设计揭示了一个重要架构模式：**市场规则作为可插拔模块**。每个市场的交易规则（T+1/T+0、涨跌停板、费用结构、数据源）封装为独立引擎，Agent 核心逻辑保持不变。这种模式可推广到其他"规则驱动的多场景 Agent"领域。

## 定位判断
在交易 Agent 生态中，Vibe-Trading 占据"多市场个人交易 Agent"的位置。它比 ai-hedge-fund 更完整（覆盖更多市场），比 TradingAgents 更产品化（有 API Server 和 Docker 部署）。

## 风险 / 局限 / 泡沫点
1. **回测 ≠ 实盘**：历史因子表现不代表未来收益，市场 regime 切换会导致因子失效
2. **交易是后果不可逆场景**：Agent 决策错误会直接导致资金损失，可解释性和风控比收益更重要
3. **多市场覆盖的深度存疑**：覆盖 4 个市场意味着每个市场的深度可能不够
4. **LLM 推理成本**：Swarm 多 Agent 辩论每次决策都消耗大量 token
5. **监管风险**：AI 驱动交易在多国面临日益严格的监管审查

## 与同类项目的关系
- **virattt/ai-hedge-fund**：AI 对冲基金团队，偏研究型，Vibe-Trading 更产品化
- **TauricResearch/TradingAgents**：多 Agent LLM 金融交易框架，Vibe-Trading 在其基础上扩展了多市场覆盖
- **simonlin1212/TradingAgents-astock（2.1K⭐）**：A 股多 Agent 投研框架，深度适配 A 股规则，Vibe-Trading 更广但 A 股深度可能不如

## 是否值得持续跟踪
**谨慎跟踪。** 作为技术研究对象（多 Agent 辩论架构、多市场引擎设计）值得跟踪，但不建议用于实盘交易。

## 后续观察点
1. 是否有实盘交易记录和业绩追踪
2. Swarm 辩论的可解释性——Agent 决策逻辑是否可审计
3. 风控机制是否有真实拦截能力（止损/仓位控制/异常检测）
4. 多市场因子是否在不同市场 regime 下都有 alpha

---
*首次记录：2026-07-14*
