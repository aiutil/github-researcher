---
title: "gstack"
slug: "garrytan-gstack"
date_added: "2026-06-23"
category: "平台候选"
emoji: "🏗️"
stars: "113,069 stars"
stars_delta: "Trending #2 全站，日增持续高位"
language: "TypeScript"
score: 92
tags: ["agent-skills", "claude-code", "tooling", "yc", "code-review", "qa", "security", "release-engineering"]
url: "https://github.com/garrytan/gstack"
---

# gstack

## 一句话定位
YC CEO Garry Tan 的 Claude Code 工具栈——23 个角色化 slash commands 把一个人变成一支工程团队。

## 它解决的问题
当 AI Agent（特别是 Claude Code）能力足够强时，瓶颈不再是"能不能写代码"，而是"怎么系统性地管理 Agent 的工作流"——产品思考、架构审查、代码 Review、QA 测试、安全审计、发布部署。传统软件工程的角色分工在 Agent 时代被压缩到一个人 + Agent 工具栈。

## 为什么值得关注（2026-06-23）
- **113K⭐** 在 Trending 持续高位，这不是技术 demo——是 YC CEO 每天使用的生产工具
- Garry Tan 声称 2026 年 ship 速度是 2013 年的 810×，60 天内交付 3 个生产服务 + 40+ 功能
- Karpathy 背书："I don't think I've typed like a line of code probably since December"
- 定义了"Agent Skills"品类：不是代码库，不是插件，是角色化认知注入

## 热度来源判断
**真实需求驱动。** 三重信任信号：
1. YC CEO 个人品牌——他管理着数千家初创公司，工具选择极有话语权
2. 实际使用证明——不是 demo，是自己每天用的工具开源
3. 完整流程覆盖——23 工具覆盖从产品思考到部署的全链路

## 关键技术亮点
1. **角色化认知注入** — /cso 不是运行安全扫描脚本，是让 Claude 以 CISO 视角审查代码。/plan-ceo-review 让 Claude 以产品 CEO 视角重新思考功能设计
2. **团队模式 auto-update** — git hook 自动同步，零版本漂移。`./setup --team` + `gstack-team-init required` 让整个团队自动获得最新工具
3. **gstack-detach** — 长时间 eval/benchmark（30-60 min）在独立 session 运行，通过 setsid + caffeinate 保护不受 SIGTERM 和 idle-sleep 影响
4. **Hermetic E2E** — 本地测试与 CI 一致的密封环境：allowlist scrub env + seeded config + --strict-mcp-config
5. **GBrowser 反检测** — Layer C stealth：chrome.* shape 恢复 + Function.toString Proxy + per-install hardware spoof + UA 去标识 + Selenium/Playwright 痕迹清理

## 架构启发
**核心设计哲学：** Agent 工具不是"给 Agent 用的工具"，而是"让 Agent 扮演特定角色的认知框架"。

**Trade-off：** 高度 Claude Code 绑定。23 个工具都是 slash commands + Markdown，依赖 Claude Code 的 slash command 解析能力。如果 Agent runtime 变化（如切换到 Codex/Gemini），工具需要重新适配。

**架构启发：** Skills 不应该是"做什么"的指令（"扫描这段代码的安全漏洞"），而应该是"以谁的视角思考什么"的角色注入（"你是一个 CISO，用 OWASP + STRIDE 框架审查这个 PR"）。

## 定位判断
**平台候选。** gstack 正在定义"Agent 工具栈应该长什么样"。如果 Claude Code 是 Agent 时代的操作系统，gstack 就是预装的 iWork 套件。关键问题是：它会成为行业标准，还是仍然是 Garry Tan 的个人工具？

## 风险 / 局限 / 泡沫点
1. **个人品牌依赖** — Garry Tan 是 YC CEO，如果精力转移（YC 工作、投资、其他），项目维护可能放缓
2. **Claude Code 绑定** — 工具设计深度依赖 Claude Code 的 slash command 体系，跨 Agent 兼容性存疑
3. **MIT 开源但无商业化** — 113K⭐ 的项目完全免费，长期可持续性存疑
4. **722 open issues** — 社区活跃但也意味着维护压力大

## 与同类项目的关系
- **vs mattpocock/skills（141K⭐）**：更通用、更轻量，是个人 .claude 目录开源。gstack 更系统化，是完整工具栈
- **vs Anthropic-Cybersecurity-Skills（18.6K⭐）**：安全领域垂直深度 vs gstack 的全流程宽度
- **vs Claude Code 原生**：gstack 是 Claude Code 之上的"能力增强包"，不替代而是增强

## 是否值得持续跟踪
**强烈建议持续跟踪。** gstack 是 Agent Skills 经济的风向标项目，它的增长曲线直接反映"Agent 工具栈品类"的成熟度。

## 后续观察点
1. 是否出现非 Garry Tan 的核心贡献者（标志：从个人项目 → 社区项目）
2. 是否被其他 Agent runtime（Codex/Gemini CLI）兼容或适配
3. 是否出现企业版或商业化路径
4. 23 工具是否会标准化为 agentskills.io 格式

## 评分
| 维度 | 分数 | 理由 |
|------|------|------|
| 热度质量 | 9 | 113K⭐，YC CEO 背书，Trending 持续高位 |
| 技术创新度 | 8 | 角色化认知注入是 Agent 时代独创 |
| 工程成熟度 | 9 | 生产环境每天使用，hermetic E2E，248+ 测试 |
| 架构启发价值 | 9 | 定义了 Agent Skills 品类的设计模式 |
| 企业落地潜力 | 7 | MIT 开源可自部署，但个人品牌依赖 |
| 中期趋势概率 | 9 | Agent 工具栈是必然趋势 |
| 平台化潜力 | 8 | 有 auto-update/team-mode 基础 |
| 基础设施潜力 | 6 | 更偏工具层而非基础设施层 |

**总分：65/80**
**项目归类：平台候选**
**是否建议持续跟踪：是**

---
*首次记录：2026-06-23*
