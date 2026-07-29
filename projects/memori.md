---
title: "Memori"
slug: "memori"
date_added: "2026-05-19"
category: "基础设施候选"
emoji: "💾"
stars: "14,595 stars"
stars_delta: "周增 2K+"
language: "Python"
score: 84
tags: ["Agent记忆", "持久化", "生产系统", "LLM无关", "结构化状态"]
url: "https://github.com/MemoriLabs/Memori"
last_seen_date: "2026-05-19"
---

# Memori

## 一句话定位
Agent 原生记忆基础设施，LLM 无关的结构化持久状态层，将 Agent 执行和对话转化为可检索的结构化状态。

## 它解决的问题
生产环境中的 Agent 需要跨会话、跨用户、跨 LLM 的持久状态管理。当前方案要么依赖 LLM 自身的上下文窗口（有上限），要么自己拼凑向量数据库 + KV 存储（工程复杂度高）。Memori 提供统一的记忆抽象层。

目标用户：生产级 Agent 系统架构师、Multi-Agent 平台开发者、企业 AI 应用团队。

## 为什么值得关注（2026-05-19）

14.6K⭐，2.2K forks。「Agent 原生记忆基础设施」定位精准，与 agentmemory（Coding Agent 专注）形成互补。LLM 无关的设计使其适合 Multi-Agent 和 Multi-LLM 场景。

## 热度来源判断
热度 75% 真实需求。生产级 Agent 部署确实面临状态管理难题。Fork 数（2.2K）表明有实际采用意向。但「记忆基础设施」概念仍处于教育市场阶段。

## 关键技术亮点
1. **LLM 无关设计**：不绑定特定 LLM 提供商，支持 GPT/Claude/Gemini/Llama 等任意后端
2. **结构化状态**：不是简单的文本存储，将对话和执行转化为结构化、可查询的状态
3. **Agent 原生 API**：接口设计围绕 Agent 执行模式（而非 CRUD），符合 Agent 开发心智模型

## 架构启发
- **记忆即基础设施**：类似数据库在 Web 应用中的地位，记忆层将成为 Agent 应用的标配基础设施
- **结构化 > 非结构化**：纯向量检索的幻觉问题通过结构化状态可以缓解
- **LLM 无关是正确方向**：Multi-LLM 策略正在成为企业标配，记忆层不应绑定 LLM

## 定位判断
在 Agent 基础设施栈中定位为「通用记忆基础设施」，类似于数据库领域的 PostgreSQL（通用存储 vs Redis 专用缓存）。与 agentmemory 形成互补而非竞争。

## 风险 / 局限 / 泡沫点
1. **抽象层过重**：在简单场景下可能过度设计，直接用向量数据库更轻量
2. **性能开销**：结构化记忆的读写延迟需要与原始 LLM 调用延迟做权衡
3. **标准化风险**：如果 OpenAI/Anthropic 在平台层内置记忆，第三方方案空间被压缩

## 与同类项目的关系
- **vs agentmemory**：agentmemory 专注 Coding Agent，Memori 更通用；类似 Redis vs PostgreSQL 的关系
- **vs 向量数据库（Pinecone/Weaviate）**：Memori 是更高层的抽象，底层可能使用向量数据库
- **vs LangChain Memory**：Memori 更底层、更生产级，LangChain Memory 更偏向原型

## 是否值得持续跟踪
**是。** Agent 记忆基础设施是中期确定性趋势。

## 后续观察点
1. 是否出现大型生产部署案例
2. 记忆检索质量在真实 Agent 场景中的表现
3. 是否形成事实标准的记忆 API 规范

---
*首次记录：2026-05-19*
