---
title: "langchain-ai/langchain"
slug: langchain
date_added: 2026-07-25
last_seen_date: 2026-08-07
category: "头部项目"
emoji: "🦜"
stars: "143,611 stars"
score: 95
tags: ["agents", "ai", "ai-agents", "langchain", "langgraph", "llm", "rag", "framework"]
url: "https://github.com/langchain-ai/langchain"
---

# langchain-ai/langchain

## 一句话定位
LLM 应用开发的全栈框架，从最初的"LLM + 工具链胶水层"演进为"Agent 工程平台"，涵盖 LangChain（基础库）、LangGraph（Agent 编排）、LangSmith（可观测性）、LangServe（部署）的完整生态。

## 它解决的问题
ChatGPT 出现后，开发者发现"调用 LLM API"远不等于"构建有用的 AI 应用"。真实场景需要：Prompt 管理、记忆、工具调用、检索增强（RAG）、多 Agent 协作、流式输出、可观测性、评估体系。LangChain 在 2022 年底率先以"框架"形式封装这些能力，让开发者用几十行代码搭建一个"能上网搜索 + 读文档 + 记忆对话"的 Agent。它是 LLM 应用工程化的拓荒者。

## 为什么值得关注
- **Stars:** 143,611（截至 2026-08-07），LLM 应用框架绝对第一
- **Forks:** 23,930，生态极其庞大
- **Watchers:** 907，行业关注度顶级
- **License:** MIT
- **活跃度:** pushed_at 2026-08-07（当日更新），极速迭代
- **商业化:** LangSmith（SaaS 观测平台）、LangGraph Cloud，估值数十亿美元
- **Topics 命中:** agents / ai-agents / deepagents / multiagent / rag / enterprise

## 热度来源判断
LangChain 的热度是**真实先发优势 + LLM 应用爆发**双重驱动。它是 LLM 应用框架的"事实标准"，2023 年几乎每个 AI demo 都基于它。虽然 2024 年后出现"反 LangChain"声音（批评其抽象过度、不够 Pythonic），但通过 LangGraph 转型 Agent 编排，成功延续了热度。当前热度真实但分化：初学者爱其开箱即用，资深工程师转向更轻量方案（LlamaIndex、直接用 OpenAI SDK）。

## 关键技术亮点
1. **LangGraph:** 基于图的有状态 Agent 编排引擎，支持循环、分支、人机协同（Human-in-the-loop）
2. **LCEL（LangChain Expression Language）:** 用管道符 `|` 组合 Prompt | Model | Parser，声明式构建 Chain
3. **工具调用标准化:** 统一封装 OpenAI/Anthropic/Google 的 function calling，跨模型兼容
4. **RAG 全栈:** 文档加载、分块、向量化、检索、重排序（reranker）一站式支持
5. **LangSmith:** Agent 执行追踪、Token 成本分析、回归评估，生产可观测性
6. **Multi-Agent:** 通过 LangGraph 支持多 Agent 协作（Supervisor、Hierarchical 等模式）

## 架构启发
LangChain 的最大架构启发是 **"LLM 应用需要框架，但框架要克制"**。早期 LangChain 因过度抽象（层层 Runnable 包装）被批评；LangGraph 的推出是一次"减法"——它将核心抽象收敛为"状态机 + 图"，更接近传统工作流引擎。这反映了一个趋势：**LLM 框架正在从"魔法胶水"回归"工程化编排"**，开发者要的是可控、可调、可观测，而非"一行代码搞定一切"。

## 定位判断
**平台型头部项目。** LangChain 已从"框架"升级为"Agent 工程平台"——LangChain（库）+ LangGraph（编排）+ LangSmith（观测）+ LangServe（部署）构成完整闭环。它是 LLM 应用层基础设施的竞争者，与 OpenAI 自家 Agents SDK、Anthropic Claude Stack 形成三方博弈。

## 风险/局限/泡沫点
- **抽象债务:** 早期版本的过度抽象导致升级痛苦，部分用户已流失
- **"反 LangChain"情绪:** 资深工程师倾向直接用 SDK，认为框架增加复杂度而非减少
- **大模型厂商自建栈:** OpenAI Agents SDK、Anthropic Skills 都在抢占"官方框架"心智
- **性能开销:** 多层封装带来额外开销，超低延迟场景需绕过
- **版本碎片:** Python 与 JS 版本功能不同步，文档时常滞后
- **商业模式争议:** LangSmith 闭源 SaaS 与开源框架的关系引发社区讨论

## 与同类项目的关系
- **vs LlamaIndex:** LlamaIndex 专注 RAG/数据连接，更聚焦；LangChain 是全栈框架
- **vs CrewAI:** CrewAI 专注多 Agent 协作，API 更简洁；LangChain 通过 LangGraph 覆盖此场景
- **vs OpenAI Agents SDK:** OpenAI 官方栈，与模型深度绑定；LangChain 框架中立
- **vs AutoGen (Microsoft):** AutoGen 强调多 Agent 对话；LangGraph 更强调"图"式编排
- **vs Haystack:** Haystack 偏企业搜索 + NLP，传统 NLP 基因重

## 是否值得持续跟踪
**必须跟踪。** LangChain 是 LLM 应用工程化的风向标。它的走向直接影响行业对"Agent 框架该是什么样"的认知。建议重点关注 LangGraph 的采用率、LangSmith 的商业化数据、以及与大模型厂商官方 SDK 的竞合。

## 后续观察点
- LangGraph 是否成为多 Agent 编排事实标准
- LangSmith 的 ARR 增长（反映企业 LLM 应用规模）
- 是否被 OpenAI/Anthropic 官方 SDK 架空
- TypeScript 版本与 Python 版本的功能对齐进度
- "反框架"趋势（直接用 SDK + 轻量库）是否实质性侵蚀其份额

---
> 数据来源: GitHub API (2026-08-07) | Stars: 143,611 | Forks: 23,930 | License: MIT
