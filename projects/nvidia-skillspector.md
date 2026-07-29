---
title: "NVIDIA SkillSpector"
slug: "nvidia-skillspector"
date_added: "2026-06-12"
last_seen_date: "2026-06-26"
category: "工具型"
emoji: "🛡️"
stars: "10,661 stars"
stars_delta: "周增 ~2,410，持续高增长"
language: "Python"
score: 86
tags: ["agent-security", "nvidia", "vulnerability-scanning", "supply-chain", "skills"]
url: "https://github.com/NVIDIA/SkillSpector"
## 2026-06-20 更新

stars 从 4,360 翻倍到 8,251（周增 5,505）。重要新增信息：
- **64 类漏洞检测覆盖 16 分类**（此前记录不详）—— 包括 prompt injection (P1-P8)、数据泄露 (E1-E4)、权限越界 (PE1-PE3)、供应链 (SC1-SC6)、过度自主 (EA1-EA4)、输出处理 (OH1-OH3)、系统提示泄露 (P6-P8)、内存投毒 (MP1-MP3)、工具滥用 (TM1-TM3)、Rogue Agent (RA1-RA2)、触发器滥用 (TR1-TR3)、危险代码 AST (AST1-AST8)、Taint Tracking (TT1-TT5)、YARA 签名 (YR1-YR4)、MCP 最小权限 (LP1-LP4)、MCP 工具投毒 (TP1-TP4)
- **SARIF 输出**：支持 CI/CD 集成
- **多 LLM 语义评估**：OpenAI / Anthropic / NVIDIA Build / 本地 Ollama
- **研究数据**：26.1% Skills 含漏洞，5.2% 疑似恶意

**判断升级：** 这不是通用代码扫描器，而是 Agent Skill 的 SAST。NVIDIA 出品 + Apache 2.0 + SARIF = 企业可在 CI/CD 中直接集成。

---

# NVIDIA SkillSpector

## 一句话定位
AI Agent 技能的安全扫描器，检测技能中的漏洞、恶意模式和安全风险。

## 它解决的问题
随着 Agent Skills 生态爆发，Skills 成为 Agent 的核心能力来源。但 Skills 可能包含恶意代码、数据泄露路径、权限越界等安全风险。目前没有任何工具对 Agent Skills 做安全审计。SkillSpector 填补了这个空白。

## 为什么值得关注（2026-06-12）
日增 308 stars，NVIDIA 官方出品。出现在 Agent Skills 爆发的同一周，是"技能供应链安全"这个新赛道的首个重要工具。时机和定位都非常精准。

## 热度来源判断
**NVIDIA 品牌 + 市场空白。** Agent Skills 安全是全新领域，NVIDIA 第一时间切入。2.6K stars 说明开发者已经开始意识到这个问题。增长不是泡沫，是安全意识的觉醒。

## 关键技术亮点
1. **Skills 专项扫描：** 不是通用代码扫描，而是专门针对 Agent Skills 的安全模式检测
2. **恶意模式识别：** 能识别 Skills 中的数据泄露、权限越界、后门等恶意模式
3. **漏洞检测：** 静态分析 Skills 代码中的安全漏洞
4. **Python 实现：** 低门槛集成到 CI/CD 流水线

## 架构启发
Agent 供应链安全是一个被严重忽视的领域。类比：
- npm 生态的 security audit → Agent Skills 的 SkillSpector
- Docker 镜像扫描（Trivy）→ Agent Skills 扫描
- SAST/DAST → Agent Skills SAST

未来 Agent 的安全架构需要：Skills 来源认证 + Skills 安全扫描 + 运行时权限控制 + 行为审计。

## 定位判断
Agent 安全工具链中的"静态扫描"组件。是 Agent 安全防御体系的第一道防线。

## 风险 / 局限 / 泡沫点
1. **标准缺失：** 还没有公认的 Skills 安全标准，扫描规则可能不够全面
2. ** Skills 格式不统一：** 不同 Agent 平台的 Skills 格式不同，难以通用扫描
3. **NVIDIA 战略绑定风险：** 可能和 NVIDIA 的 Agent 平台深度绑定
4. **误报率：** 新工具的误报率需要时间验证

## 与同类项目的关系
- **vs. trivy（ Aqua Security）：** trivy 扫描容器/镜像，SkillSpector 扫描 Agent Skills，领域不同
- **vs. Snyk：** Snyk 做通用代码安全，SkillSpector 聚焦 Agent Skills 特有风险
- **vs. Socket.dev：** Socket 做 npm 供应链安全，SkillSpector 做 Skills 供应链安全

## 是否值得持续跟踪
**是。** Agent 安全是确定性增长赛道，SkillSpector 是目前唯一的 Skills 安全扫描工具。

## 后续观察点
1. 是否被主流 Agent 平台（Claude Code、Cursor）集成
2. Skills 安全标准是否开始形成
3. 是否扩展到运行时安全监控（不只是静态扫描）

---
*首次记录：2026-06-12*
