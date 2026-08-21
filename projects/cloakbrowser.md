---
title: "CloakHQ/CloakBrowser"
slug: "cloakbrowser"
date_added: "2026-05-19"
last_seen_date: "2026-05-22"
category: "工具型"
emoji: "🎭"
stars: "29,872 stars"
stars_delta: "API 实时数据"
language: "Python"
license: "MIT"
score: 82
tags: ["ai-agents", "anti-detect", "antidetect-browser", "bot-detection", "browser-automation", "captcha-bypass", "chromium", "cloudflare"]
url: "https://github.com/CloakHQ/CloakBrowser"
---

# CloakHQ/CloakBrowser — Stealth Chromium that passes every bot detection test. Drop-in Playwright replac

## 一句话定位

Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.。主要使用 Python 编写，当前 29,872 stars / 2,457 forks / 140 subscribers。

## 它解决的问题

**目标用户**：使用 python 生态的开发者、AI Agent 构建者。

**痛点**：该项目解决的核心问题是 Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.。从 README 来看，项目提供了 <p align="center"> <img src="https://i.imgur.com/cqkp6fG.png" width="500" alt="CloakBrowser"> </p> <p align="center"> <a href="https://pypi.org/project/cloakbrowser/"><img src="https://img.shields.io/。

**场景**：适用于需要 ai-agents, anti-detect, antidetect-browser 的开发场景。

## 为什么值得关注（2026-05-19）

1. **Stars 增长**：29,872 stars，2,457 forks——fork/star 比为 8.2% （正常范围）
2. **活跃度**：创建于 2026-02-22，最后更新 2026-08-11，190 open issues
3. **技术栈**：Python，License: MIT
4. **生态定位**：Topics: ai-agents, anti-detect, antidetect-browser, bot-detection, browser-automation

## 热度来源判断

**真实需求信号**：forks 2457（高部署意愿），subscribers 140（深度关注）。

**品类时机**：从 topics 来看，ai-agents, anti-detect, antidetect-browser 是当前社区关注的方向。



## 关键技术亮点

1. **<p align="center">**
2. **<img src="https://i.imgur.com/cqkp6fG.png" width="500" alt="CloakBrowser">**
4. **<p align="center">**
5. **<a href="https://pypi.org/project/cloakbrowser/"><img src="https://img.shields.io/pypi/v/cloakbrowse**
6. **<a href="https://www.npmjs.com/package/cloakbrowser"><img src="https://img.shields.io/npm/v/cloakbro**

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 仅明确入口为 Python PyPI 与 npm 双分发，构建于 Chromium 之上的隐身浏览器自动化客户端，无服务端组件记录。 | 证据仅来自简介、tags（chromium / browser-automation / anti-detect）、PyPI/npm 徽章；具体补丁范围、依赖未在档案披露。 |
| 主路径 | 调用方（如 Playwright 代码）→ CloakBrowser 客户端（Python/Node）→ 经源码级指纹补丁的 Chromium → 目标站点/反检测测试。30/30 测试通过为档案中唯一量化结果。 | 路径节点均依简介"sourse-level fingerprint patches""Playwright replacement"推导；无会话管理、无外部模型编排节点，档案未证实的不得写入。 |
| 关键权衡 | 作为开源隐身浏览器客户端，在反 bot 检测能力（30/30）与法务/合规风险（绕过 captcha、云防护）之间的取舍；MIT 许可降低采用门槛但无力兜底合规。 | 档案仅给出 MIT、tags（captcha-bypass / cloudflare / bot-detection）；性能、对抗强度、维护频率无量化指标。 |
| 最小 PoC | 在隔离环境以最小脚本替换 Playwright 启动入口，跑同一组 30 项 bot 检测用例复现"30/30 通过"，并对照原 Playwright 基线差异——以验证补丁实际生效而非依赖默认行为。 | PoC 步骤基于"drop-in Playwright replacement""30/30 tests passed"文字；具体测试集来源与脚本结构在档案中未见，需待核验。 |

## 架构启发

从 CloakHQ/CloakBrowser 的设计来看，核心思路是 **"Stealth Chromium that passes every bot detection test. Drop-"**。这反映了 Python 生态中 Agent / AI 工具链 的演进方向——降低集成复杂度、提供开箱即用的能力。开源 License (MIT) 降低了采用门槛。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
  Caller[Playwright 调用方 Python 或 Node] --> Client[CloakBrowser 客户端 MIT Python npm 双分发]
  Client --> Patched[源码级指纹补丁的 Chromium 30 30 bot 测试通过 待核验 具体补丁面]
  Patched --> Targets[目标站点与反检测 CF Captcha 等标签外边界]
  Client -. 状态回写 .-> Client
  Targets --> Adversary[对抗强度演进 检测方持续升级 风险边界 档案无时间序列]
```

## 定位判断

**工具型**。在生态中定位为Stealth Chromium that passes every bot d方向的工具。Stars 29872 说明已有一定社区基础。

## 风险 / 局限 / 泡沫点

1. **规模风险**：29,872 stars，但 fork 2457 说明有实际部署
2. **维护风险**：最后 push 时间 2026-08-11，活跃维护中
3. **Open Issues**：190 个 open issues，活跃社区反馈
4. **License**：MIT（宽松许可，适合商用）

## 与同类项目的关系

- 与同 Python 生态的同类工具形成竞争/互补关系。具体竞品对比需参考社区讨论。
- 从 topics (ai-agents, anti-detect, antidetect-browser) 来看，与关注 ai-agents 的其他项目有交叉。

## 是否值得持续跟踪

**是。** 29872 stars + 活跃更新说明项目有持续价值。建议关注后续版本迭代和社区增长。

## 后续观察点

1. Star 增速是否可持续（当前 29,872）
2. Fork 增长趋势（当前 2,457）
3. 功能迭代频率（最后更新 2026-08-11）
4. 社区活跃度（subscribers 140, open issues 190）

---
> 数据来源: GitHub API (2026-08-11) | Stars: 29,872 | Forks: 2,457 | License: MIT | 语言: Python | 创建: 2026-02-22
