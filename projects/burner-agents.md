---
title: "NotPBShaw/burner-agents"
slug: "burner-agents"
date_added: "2026-06-19"
category: "观察型"
emoji: "🔥"
stars: "554 stars"
stars_delta: "17天+554"
language: "Python"
score: 72
tags: ["privacy", "disposable-agents", "anti-tracking", "web-automation", "ethics"]
url: "https://github.com/NotPBShaw/burner-agents"
---

# Burner Agents

## 一句话定位
一次性身份 Agent swarm——每次 web 交互使用独立浏览器上下文和指纹，任务完成后销毁一切，实现不可归因、不可关联的 web 操作。

## 它解决的问题
现代 web 通过指纹、cookie、行为关联来识别和追踪用户。VPN 隐藏 IP，隐私模式清除本地状态，但都无法解决"你以同一个身份出现"这个根本问题。

## 为什么值得关注（2026-06-19）
- 概念创新：不是"更好地隐藏身份"，而是"不维护身份"
- 架构清晰：isolation / reasoning / orchestration / identity 四层
- Agent swarm 模式在隐私场景的首次系统化实现

## 热度来源判断
隐私议题热度 + Agent swarm 概念热度。但使用场景和用户群体不够明确。

## 关键技术亮点
1. **Fresh identity per task** — 每个任务独立的浏览器上下文 + 指纹 + 设备特征 + 网络出口
2. **Orchestration in trust boundary** — 协调逻辑只在本地，对外不可见
3. **Reasoning agent** — 不是脚本，是 LLM 驱动的动态页面理解
4. **Complete erasure** — 任务完成 = 身份销毁，零残留

## 架构启发
Burner Agents 定义了 **Disposability as Privacy** 范式——隐私不是隐藏，而是不可关联。这与零知识证明的哲学异曲同工。

## 定位判断
观察型。概念前沿但伦理边界模糊，使用场景（记者、研究人员、隐私需求用户）有限。不适合企业部署。

## 风险 / 局限 / 泡沫点
1. **伦理风险** — 不可归因 web 交互可被滥用于攻击、欺诈
2. **法律灰区** — 不同司法管辖区对匿名访问的法律态度不同
3. **资源密集** — 每个 agent 需要独立浏览器 + 网络
4. **对手进化** — 反欺诈系统也在进化

## 与同类项目的关系
- **vs VPN + 隐私浏览器** — VPN/隐私浏览器隐藏身份，burner 不维护身份
- **vs browser-use** — browser-use 是通用 web 自动化，burner 是隐私优先的 web 自动化
- **vs Tor** — Tor 做网络层匿名，burner 做应用层不可关联

## 是否值得持续跟踪
**观察型跟踪。** 概念值得关注，但伦理和法律风险使其不适合推荐为生产工具。

## 后续观察点
1. 是否出现合规使用场景（记者保护、学术研究）
2. 社区是否增加治理机制（使用许可等）
3. 反欺诈行业对 disposable agent 的检测能力

---
*首次记录：2026-06-19*
