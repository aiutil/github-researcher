---
title: "citrolabs/ego-lite"
slug: "ego-lite"
date_added: "2026-07-24"
last_seen_date: "2026-08-11"
category: "工具型"
emoji: "🧭"
stars: "9,566 stars"
stars_delta: "从 2K→9.6K（约 2.5 周），日增 ~400+，爆发式增长"
language: "JavaScript"
license: "MIT"
score: 86
tags: ["browser-automation", "agent-browser", "parallel-work", "chrome-migration", "code-driven", "claude-code", "codex"]
url: "https://github.com/citrolabs/ego-lite"
---

# ego (lite) — 人机并行浏览器

## 一句话定位
专为 AI Agent 设计的浏览器——Agent 在独立 Space（并行工作区）中运行浏览器自动化任务，共享你的 Chrome 登录态但不干扰你的标签页，代码驱动而非 CLI 驱动，复杂任务快 2.5 倍且消耗更少 Token。

## 它解决的问题
现有 Agent 浏览器工具（browser-use、agent-browser）存在三大痛点：

1. **登录态无法继承**：需要单独启动浏览器实例，Agent 不得不重新登录每个网站，Cookie/Session/扩展全部丢失
2. **标签冲突**：Agent 和人争抢同一个浏览器窗口，Agent 操作时用户无法继续浏览
3. **CLI 循环效率低**：Agent 在"调用命令 → 看结果 → 调用下一条"的串行循环中浪费时间。复杂多步任务（如填表+截图+提交）需要多轮往返

ego lite 的解法：**一个浏览器，从一开始就为人机共享而设计**。Agent 有自己的 Space（隔离工作区），继承你的真实登录状态，通过 JavaScript 函数直接调用浏览器 API，多步任务一次执行。

## 为什么值得关注（2026-08-11）
- **Stars:** 9,566（7 月底 2K，2.5 周爆发到 9.6K），Forks 470，Watchers 25
- **范式转变**：从"驱动浏览器"到"共享浏览器"，从 CLI 到 Code
- **实测快 2.5 倍**：复杂工作流比传统 CLI 方式快 2.5 倍，工具调用次数更少，任务成功率更高
- **内核级 Snapshot**：号称市场上最强的页面快照，可靠处理深层嵌套 iframe（其他方案的通用断点）
- **跨 Agent 兼容**：`ego-browser` Skill 兼容 Claude Code、Codex、Cursor 等所有主流 Agent CLI
- **Chrome 一键迁移**：首次启动迁移登录态/Cookie/扩展/书签，零配置试用
- **持续活跃**：pushed_at 2026-08-11（今日），几乎每日更新

## 热度来源判断
ego lite 的热度是 **"Agent 浏览器自动化的真实痛点 × 范式创新 × Chrome 迁移降低门槛"** 的组合。Agent 操控浏览器是 2026 年 Agent 应用最大场景之一（数据抓取、表单填写、端到端测试、Lead Enrichment），但现有方案的登录态和标签冲突是开发者每天面对的麻烦。ego lite 的"共享浏览器 + 独立 Space"设计直击痛点。日增 400+ 的增速说明口碑传播正在加速。470 forks 显示社区在积极尝试集成。**热度真实，痛点验证充分**——但闭源核心浏览器是长期信任的变量。

## 关键技术亮点
1. **Code-based 非 CLI-based（核心差异）**：Agent 写 JavaScript 函数直接调用浏览器 API（snapshot/fill/click/wait/navigate/capture），多步任务一次输出而非多轮 CLI 循环。复杂工作流快 2.5 倍，Token 消耗更少
2. **Space 隔离架构**：每个 Agent / 任务有独立 Space（并行工作区），10 个 Space 同时运行互不干扰。用户可随时查看哪个 Space 在运行、接管或停止
3. **最强 Page Snapshot**：内核级定制产出高质量页面快照（文本模型"看"页面的依据），可靠处理深层嵌套 iframe——这是 browser-use 等方案的通用断点
4. **Chrome 数据迁移**：首次启动可选择迁移 Chrome 登录态/Cookie/扩展/书签，Agent 直接继承用户的真实身份
5. **`ego-browser` Skill 协议**：标准 Skill 安装（`npx skills add citrolabs/ego-lite`），将浏览器暴露为一组页内 JavaScript 工具
6. **本地优先**：浏览数据留在设备上，仅记录是否选择 Chrome 迁移

## 架构启发
ego lite 代表了 Agent 浏览器自动化的**范式迭代**：

| 维度 | 1.0 范式（browser-use） | 2.0 范式（ego-lite） |
|------|------------------------|---------------------|
| 浏览器 | 独立实例，需重登 | 共享浏览器，继承登录态 |
| 驱动 | CLI 串行循环 | JavaScript 函数，一次执行 |
| 并行 | ❌ 单线程 | ✅ 多 Space 并行 |
| 页面理解 | DOM 抓取（脆弱） | 内核级 Snapshot（精确） |

更深层启发：**Agent 工具的效率瓶颈不在模型能力，而在交互范式**。CLI 循环每轮消耗一次 LLM 推理，而 Code 驱动让 Agent 把多步操作编译为一段代码一次执行——这本质上是"把推理成本从 N 次降到 1 次"。

## 定位判断
**工具型，有平台化潜力。** 当前是 Agent 浏览器自动化工具的有力竞争者。长期价值取决于能否从"工具"升级为"平台"——开放 Space API 供第三方编排、构建经验积累系统。如果成功，可能成为"Agent 的浏览器层"。Trendshift 已收录（#42334），表明已进入趋势雷达。

## 风险 / 局限 / 泡沫点
1. **仅 macOS**：Windows 和 Linux 仍在 roadmap，限制了采用范围。macOS 优先策略降低了初期工程负担但收窄了用户基数
2. **闭源核心**：浏览器本身闭源，仅 Skill 层（`ego-browser`）开源。社区对闭源核心的信任度有限，也无法审计安全关键路径
3. **安全考量**：Agent 可访问用户登录态（银行、邮箱、企业 SaaS），企业场景需要额外的权限 Scope 和数据隔离控制。目前缺乏细粒度权限模型
4. **竞争激烈**：browser-use、ChatGPT Atlas、Perplexity Comet 都在同一赛道。大厂产品的分发优势可能挤压独立项目空间
5. **"体验积累"功能未落地**：声称可加速 5 倍的 Experience Accumulation 仍是 coming soon
6. **Chrome 迁移风险**：迁移完整的登录态意味着安全敏感凭据暴露给 Agent，需要谨慎评估

## 与同类项目的关系

| 维度 | ego-lite | browser-use | ChatGPT Atlas | Perplexity Comet | agent-browser (Vercel) |
|------|----------|-------------|---------------|------------------|----------------------|
| 范式 | 共享浏览器 | 驱动浏览器 | 独立浏览器 | 独立浏览器 | 驱动浏览器 |
| 并行 Space | ✅ | ❌ | ✅ | ✅ | ❌ |
| 继承 Chrome 数据 | ✅ | ❌ | ✅ | ✅ | ❌ |
| 可复用 Skill | ✅ | ❌ | ❌ | ❌ | ❌ |
| 代码驱动 | ✅ JS | ❌ CLI | 内置 Agent | 内置 Agent | ✅ |
| 外部 Agent 可控 | ✅ | ✅ | ❌ | ❌ | ✅ |
| 数据本地 | ✅ | ✅ | ❌ | ❌ | ✅ |
| 开源程度 | Skill 层开源 | ✅ 完全开源 | ❌ 闭源 | ❌ 闭源 | ✅ |

## 是否值得持续跟踪
**建议持续跟踪。** "共享浏览器"范式如果能被验证，将成为 Agent 浏览器自动化的主流方式。对 Agent 应用开发者，ego lite 是当前最高效的浏览器自动化方案。对生态观察者，它代表了 Agent 工具从"CLI 循环"向"Code 编译"的范式跃迁。重点关注跨平台支持进度、安全控制成熟度和企业采用情况。

## 后续观察点
1. **Windows/Linux 版本发布时间表**——跨平台是规模化的前提
2. **浏览器内核是否开源**——当前仅 Skill 层开源，闭源核心限制社区信任
3. **企业级安全控制**——Agent 权限 Scope、数据隔离、操作审计
4. **"体验积累"功能落地效果**——声称可加速 5 倍
5. **与 Claude Code / Codex 的深度集成质量**——是否成为默认浏览器 Skill
6. **Space API 开放**——是否从工具升级为编排平台

---
> 数据来源: GitHub API (2026-08-11) | Stars: 9,566 | Forks: 470 | License: MIT | 语言: JavaScript | 创建: 2026-04-16 | pushed: 2026-08-11
