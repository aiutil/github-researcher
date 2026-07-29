---
title: "Paperclip"
slug: "paperclip"
date_added: "2026-04-26"
category: "平台候选"
emoji: "📎"
stars: "58.8k stars"
stars_delta: "高增速"
language: "TypeScript"
score: 80
tags: ["zero-human", "orchestration", "automation", "agent-workflow"]
url: "https://github.com/paperclipai/paperclip"
---

# Paperclip

## 一句话定位
零人类公司开源编排框架，端到端自动化商业流程。

## 它解决的问题
企业内部大量重复性流程仍需人工介入。Paperclip 提供多 Agent 协作编排框架，实现从任务分拆到执行到审批的全链路自动化。

## 为什么值得关注（2026-04-26）
58.8K Stars + 10.2K Forks，不只是在传播，有真实工程采纳。"零人类公司"概念击中市场想象。

## 热度来源判断
概念驱动 + 工程实现。Star 中有一部分是概念追捧，但 Fork 数和 TypeScript 工程质量说明有严肃使用者。

## 关键技术亮点
1. 多 Agent 协作编排，支持任务分拆和依赖管理
2. 审批流建模为 Agent 间消息传递，而非人类 UI 操作
3. TypeScript 全栈，部署门槛低

## 架构启发
把"审批"建模为 Agent 间的消息传递是重要设计思想。企业内部流程自动化可以直接借鉴这个模式：不是模拟人类操作，而是重新建模流程。

## 定位判断
平台候选。如果审计链和合规问题得到解决，可能成为企业自动化基础设施。

## 风险 / 局限 / 泡沫点
1. "零人类"在大多数监管环境不合规，金融/医疗场景无法直接使用
2. 真实商业场景的边界条件极其复杂，长尾问题多
3. 高度依赖 LLM 可靠性，关键决策环节仍需人工兜底

## 与同类项目的关系
- vs **n8n**：n8n 偏通用工作流，Paperclip 专注 Agent 协作编排
- vs **Langflow**：Langflow 偏 AI Agent 构建，Paperclip 偏业务流程编排
- vs **Mercury Agent**：Mercury 偏单 Agent 运行时，Paperclip 偏多 Agent 编排

## 是否值得持续跟踪
是。建议企业内部做 PoC，验证在合规框架下的半自动化流程。

## 后续观察点
- 是否出现合规/审计插件
- 真实企业案例
- 是否被大厂收购或集成
