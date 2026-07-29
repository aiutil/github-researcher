---
title: "Memory OS"
slug: "memory-os"
date_added: "2026-06-06"
category: "平台候选"
emoji: "🧠"
stars: "869 stars"
stars_delta: "新建项目，首日记录 869"
language: "Python"
score: 84
tags: ["agent-memory", "persistent-memory", "qdrant", "rag", "hermes-agent", "vector-db", "sqlite-fts5"]
url: "https://github.com/ClaudioDrews/memory-os"
---

# Memory OS

## 一句话定位
Hermes Agent 的 7 层记忆操作系统，从 workspace 文件到向量数据库到自动知识库，实现跨会话持久化记忆。

## 它解决的问题
AI Agent 的「失忆症」：每次对话重新开始，无法积累用户偏好、项目决策、技术上下文。现有记忆方案要么云锁定（云端 RAG），要么太浅（单层 KV）。

## 为什么值得关注（2026-06-06）
7 层分层架构是当前最系统的 Agent 记忆设计方案。不是简单的向量检索，而是按时间尺度和信息类型分层的完整操作系统。v0.2.0 一键安装说明项目认真对待可用性。

## 热度来源判断
- Agent Memory 是 2026 年刚需赛道
- 7 层架构设计引发技术讨论
- Hermes Agent 生态的扩展
- Hacker News / Reddit 技术社区传播
- 869 stars 对基础设施项目来说是严肃信号

## 关键技术亮点
1. **7 层分层架构**：Workspace（系统提示注入）→ Sessions（FTS5 全文搜索）→ Structured Facts（信任评分 + 实体消解）→ Fabric（跨会话提取）→ Vector DB（Qdrant 混合检索）→ LLM Wiki（自动策展）→ Context Injection（token 预算控制）
2. **4 级检索回退**：hybrid（向量+词频）→ dense（纯向量）→ lexical（BM25）→ SQLite（精确匹配），确保任何情况都能检索到
3. **信任评分系统**：结构化事实带有信任分数，通过用户反馈自动校准
4. **语义去重**：cosine > 0.92 自动合并相似记忆，防止记忆膨胀
5. **每周衰减扫描**：过期信息自动降权，保持记忆库新鲜
6. **Provider 无关**：OpenRouter / OpenAI / Anthropic / Ollama / 本地模型全兼容

## 架构启发
Memory OS 的分层设计是 Agent OS 记忆子系统的参考架构：
- **短期记忆**（Layer 1-2）：毫秒级，注入 + 全文搜索
- **中期记忆**（Layer 3-4）：结构化事实 + 跨会话关联
- **长期记忆**（Layer 5-6）：语义检索 + 自动知识图谱
- **调度层**（Layer 7）：根据上下文窗口预算智能注入

这个分层思路可以迁移到任何 Agent 系统（不限于 Hermes）。

## 定位判断
**平台候选。** Agent 记忆基础设施的早期参考实现。如果 7 层架构被验证有效，可能成为 Agent OS 记忆层的标准设计。

## 风险 / 局限 / 泡沫点
1. **Hermes Agent 绑定**：当前只为 Hermes 设计，迁移到其他 Agent 框架需要适配
2. **运维复杂度**：Docker + Qdrant + Redis + ARQ Worker = 最小 4 个服务
3. **token 消耗**：多层注入会占用大量 context window
4. **信任评分冷启动**：新用户缺乏反馈数据，初期评分不准
5. **竞品压力**：MemPalace 53.8K stars 是更热门的竞品

## 与同类项目的关系
| 项目 | 定位 | 差异 |
|------|------|------|
| MemPalace (53.8K⭐) | 通用 Agent 记忆 | 更热门，但架构可能不如 Memory OS 分层清晰 |
| mem0 | Agent 记忆层 | 更轻量，功能较少 |
| Letta (原 MemGPT) | 有状态 Agent | 核心注意力机制，不是纯记忆层 |

## 是否值得持续跟踪
**是。** 7 层架构是最系统的 Agent 记忆设计，值得作为参考架构长期跟踪。

## 后续观察点
1. 是否从 Hermes 专属走向框架无关（SDK / API 抽象）
2. 信任评分的效果在大规模使用中是否成立
3. 与 MemPalace 的架构对比和社区选择
4. Qdrant 到其他向量数据库的抽象层是否出现

---
*首次记录：2026-06-06*
