---
title: "rohitg00/ai-engineering-from-scratch"
slug: ai-engineering-from-scratch
date_added: "2026-05-26"
last_seen_date: "2026-08-07"
category: "工具型"
emoji: "📚"
stars: "46,168"
language: "Python"
score: 78
tags: ["AI工程", "教育", "Python", "教程", "从零开始", "TypeScript", "Rust"]
url: "https://github.com/rohitg00/ai-engineering-from-scratch"
---

# rohitg00/ai-engineering-from-scratch

## 一句话定位
从零学习 AI 工程的系统化课程——503 节课、20 个阶段、约 320 小时，覆盖 Python/TypeScript/Rust/Julia 四种语言，每节课产出一个可复用的 Artifact（prompt、skill、agent 或 MCP server）。

## 它解决的问题
AI 工程师需求爆发但教育供给碎片化——学习者需要在论文、博客、视频、教程之间跳转，知识碎片化严重。学完一个 chatbot demo 却不理解 loss curve，接上一个 function call 却说不清 attention 机制。ai-engineering-from-scratch 提供了一条系统化的学习路径：从数学基础到深度学习，从 Transformer 到 Agent，从 MCP 到强化学习，20 个阶段层层递进，每节课都有概念讲解、数学推导、代码实现和测验。

## 为什么值得关注（2026-05-26）
- 46,168 stars，7,986 forks——创建于 2026-03-18，不到 5 个月达到 46K stars，极为罕见
- MIT 许可证，已有 11 种语言的 README 翻译（中文、日语、韩语、西语、法语等）
- 503 节课，20 个阶段，~320 小时，四语言并行（Python、TypeScript、Rust、Julia）
- 通过 `npx skills add` 一键安装，Coding Agent（Claude Code、Cursor、Codex、OpenClaw、Hermes）成为私人教师
- 官方网站 aiengineeringfromscratch.com，近 30 天 24 万页面浏览

## 热度来源判断
**AI 工程师培训需求爆发 + 创新分发模式**。ai-engineering-from-scratch 的爆发式增长（5 个月 46K stars）由多重因素驱动：(1) AI 工程师是全球最热门的职业方向，系统化学习资源严重短缺；(2) "Agent 作为教师"的创新模式——通过 `npx skills add` 安装后，Coding Agent 成为交互式私人教师，这比传统视频教程更高效；(3) 四语言并行（Python/TS/Rust/Julia）和 11 语言 README 翻译覆盖了全球开发者；(4) 作者此前的 agentmemory 项目（#1 持久记忆 Skill）带来了初始粉丝。这是 2026 年教育赛道的现象级项目。

## 关键技术亮点
1. **Agent-as-Tutor 模式**：通过 `npx skills add rohitg00/ai-engineering-from-scratch` 安装后，在 Agent 中执行 `/start-learning` 会先进行 10 题分班测验，映射已有知识到起始阶段，生成个性化学习计划保存到 `LEARNING.md`。然后 `/learn` 每次教授一节课（概念 → 数学 → 代码 → 测验），`/course-guide <topic>` 跳转到特定知识点。兼容任何读取 SKILL.md 目录的 Agent。
2. **系统化课程结构**：20 个阶段从基础到高级层层递进——从 Python/数学基础，到深度学习、Transformer、LLM，再到 Agent、MCP、强化学习、群体智能。每节课都产出可复用的 Artifact。503 节课的规模覆盖了 AI 工程的完整知识图谱。
3. **四语言并行教学**：同一概念在 Python、TypeScript、Rust、Julia 四种语言中实现，学习者可以选择主力语言，同时对比不同语言的实现差异。这在 AI 教育项目中极为罕见。
4. **数据驱动的读者统计**：README 中嵌入了实时统计数据（150,639 读者、近 30 天 24 万页面浏览），通过 build.js 自动生成。这为课程改进提供了量化反馈。

## 架构启发
ai-engineering-from-scratch 的核心创新是"用 AI Agent 重新定义编程教育"。传统的编程教育（MOOC、书籍、视频）是单向的——内容固定、节奏固定、无法个性化。而 Agent-as-Tutor 模式实现了：(1) 个性化分班（10 题测验映射起始点）；(2) 交互式教学（每节课都有测验和即时反馈）；(3) 知识检索（`/course-guide` 随时跳转到需要的知识点）。这种模式可能是 AI 时代编程教育的范式转变。另一个启发是"Skills 作为教育内容的载体"——课程内容存储在 SKILL.md 文件中，Agent 按需加载，这比传统 LMS 系统更轻量。

## 定位判断
ai-engineering-from-scratch 定位为**AI 时代系统化编程教育的新标杆**。在 GitHub 教育项目中，46K stars 使其成为 2026 年最热门的学习资源之一。与传统教程仓库（如 ml-algorithms、handson-ml）不同，它的核心竞争力不是内容本身（503 节课可以持续更新），而是"Agent 作为私人教师"的交互模式。这预示着编程教育从"看教程"到"和 AI 学"的转变。

## 风险 / 局限 / 泡沫点
1. **内容质量的方差**：503 节课的规模意味着内容质量可能有较大方差——前 100 节可能精心编写，后面的课程是否保持同等质量需要验证。课程"广而全"可能导致某些主题深度不足。
2. **依赖 Agent 能力的天花板**：Agent-as-Tutor 的效果完全取决于底层 LLM 的能力。如果 Agent 无法准确回答学生的追问或无法理解学生的错误模式，教学体验会大打折扣。
3. **完成率的挑战**：320 小时的课程对于绝大多数学习者来说太长。传统 MOOC 的完成率不到 10%，这个项目可能面临类似的挑战。Agent 交互是否能显著提升完成率有待验证。
4. **商业化路径不明确**：MIT 开源 + 免费网站的模型如何可持续？如果靠赞助或 Pro 版本，可能影响内容的开放性。

## 与同类项目的关系
- **mlabonne/llm-course**：约 40K stars 的 LLM 课程，结构化路径学习 LLM。更聚焦 LLM 领域，ai-engineering-from-scratch 范围更广（覆盖整个 AI 工程）。
- **e2b-dev/awesome-ai-agents**：Agent 项目列表/资源汇总。不是课程，而是索引。
- **karpathy/nn-zero-to-hero**：Karpathy 的神经网络从零到英雄系列。教学风格更个人化、更深入，但课程数量远少于 503 节。

## 是否值得持续跟踪
**值得跟踪，作为 AI 教育范式转变的标志性项目**。ai-engineering-from-scratch 的 Agent-as-Tutor 模式可能是编程教育的未来方向。46K stars 的爆发性增长验证了市场需求。建议关注其完成率数据、课程质量反馈和商业化路径。

## 后续观察点
1. **学习者完成率数据**：503 节课中有多少学习者真正完成，Agent 交互模式是否比传统 MOOC 显著提升了完成率
2. **课程质量的持续维护**：随着 AI 领域快速演进（新模型、新框架），503 节课是否持续更新以保持时效性
3. **商业化路径**：是否会推出 Pro 版（认证、项目评审、社区）或企业版（团队培训），验证"开源教育 + 增值服务"的商业可行性

---
*首次记录：2026-05-26*
