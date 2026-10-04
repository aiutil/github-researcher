---
title: "pbakaus/impeccable"
slug: "pbakaus-impeccable"
date_added: "2026-10-05"
last_seen_date: "2026-10-05"
category: "工具型"
emoji: "🎨"
stars: "76,227 stars"
stars_delta: "11 个月 76,227⭐，fork 4,546，fork/star 5.9%；持续 GitHub Trending"
language: "JavaScript"
license: "Apache-2.0"
score: 88
tags: ["impeccable", "pbakaus", "design-language", "ai-design", "frontend-design", "anthropic-skills", "claude-skills", "impeccable-style", "npx-install", "impeccable-init", "product-md", "24-commands", "polish", "audit", "critique", "distill", "animate", "bolder", "quieter", "61-detector-rules", "deterministic-rules", "llm-critique-checks", "cli", "browser-extension", "no-llm", "no-api-key"]
url: "https://github.com/pbakaus/impeccable"
---

# pbakaus/impeccable

## 一句话定位
Impeccable——AI 编程 Agent 的设计语言 skill 集，1 skill + 24 commands（polish / audit / critique / distill / animate / bolder / quieter 等）+ 61 个确定性 detector rules + LLM-only critique checks，CLI 与浏览器扩展无需 LLM 即可离线运行，Apache-2.0 开源。

## 它解决的问题
2026 年 AI 编程 Agent 生成的 UI 严重「SaaS 模板化」——每个项目都用同样的 telltale：Inter for everything / purple-to-blue gradients / cards nested in cards / gray text on colored backgrounds / rounded-square icon tile above every heading。Anthropic 官方的 frontend-design skill 是第一个广泛使用的设计 skill，但只解决了一半——它提供方向，没有提供「确定性验证」。Impeccable 直击这一痛点：它在 Anthropic frontend-design 基础上，提供 **24 个共享词汇命令（polish / audit / critique / distill / animate / bolder / quieter）+ 61 个无需 LLM 的确定性 detector rules** + LLM-only critique checks + 浏览器扩展，让 AI 编程 Agent 不仅能生成设计，还能 **离线 check + 可执行 polish**。解决的是 **「AI 设计语言碎片化、SaaS 模板化 telltale 堆叠、设计质量无法自动验证」** 的痛点。

## 为什么值得关注（2026-10-05）
- **Stars:** 76,227（截至 2026-10-05），11 个月突破 7.6 万
- **Forks:** 4,546
- **License:** Apache-2.0，商用清晰
- **语言:** JavaScript（含 npx CLI + 浏览器扩展 + detector rules 引擎）
- **规模:** 387,030 KB（巨大工程量，反映 24 commands + 61 detector rules 的实现深度）
- **活跃度:** created 2025-11-16，pushed_at 2026-10-04，持续高活跃
- **覆盖:** Claude Code / Codex / Cursor / Windsurf / 任何支持 Agent Skills spec 的 AI coding tool
- **背书:** pbakaus 个人 + impeccable.style 主页
- **Topics:** 0 个覆盖（README 未明示）

## 热度来源判断
impeccable 的热度是 **「AI 设计 SaaS 模板化 telltale 痛点 × 24 commands 共享设计词汇 × 61 确定性 detector rules × npx install 一行装 × Apache-2.0 商用清晰」** 的强劲组合。AI 编程 Agent 生成的 UI 缺乏差异化是行业公认问题——开发者苦「千篇一律 purple-to-blue gradients」久矣。Impeccable 提供「无 LLM 离线 deterministic check」是关键创新——之前的设计 skill 都依赖 LLM 评审（成本高、不稳定），Impeccable 用 61 个 deterministic rules 在 CLI/浏览器扩展里直接检查，不消耗 LLM API 调用。`/impeccable init` 自动扫描写 `PRODUCT.md`（audience / purpose / operating context / constraints / voice / evidence）也是创新——把「durable product truth」与「surface-level visual direction」分离。热度 **真实且具设计标准潜力**——但需警惕：24 commands 在多 AI coding tool 的兼容性、61 detector rules 在多 frontend stack 的覆盖广度决定其能否成为设计标准。

## 关键技术亮点
1. **24 commands 共享设计词汇:** polish / audit / critique / distill / animate / bolder / quieter 等 24 个共享命令，让 AI 与开发者用同一词汇对话
2. **61 deterministic detector rules:** 无 LLM、无 API key 即可离线运行的确定性检查规则，CLI 与浏览器扩展支持
3. **LLM-only critique checks:** 仅在 deterministic rules 通过后调用 LLM 做 critique，避免 LLM 浪费在「明显 SaaS telltale」上
4. **`/impeccable init` 写 PRODUCT.md:** 一次性扫描项目 + 询问 material gaps + 写 durable product truth（audience / purpose / operating context / constraints / voice / evidence），把产品真相与视觉方向分离
5. **Anthropic frontend-design 兼容 + 超越:** README 明示「started from there」+ 在 frontend-design 基础上加 One setup flow + 24 commands + 61 rules + LLM critique
6. **npx 一行装:** `npx impeccable install` + `/impeccable init` 启动完整工作流，零摩擦

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | AI 编程 Agent 的设计语言 skill 集；1 个 skill + 24 commands + 61 deterministic detector rules + LLM-only critique checks + CLI 与浏览器扩展 | 仅基于 README 描述的 1 skill + 24 commands（polish / audit / critique / distill / animate / bolder / quieter）+ `npx impeccable install` + `/impeccable init` 写 PRODUCT.md + 61 deterministic detector rules + LLM-only critique checks + CLI 与浏览器扩展无 LLM 无 API key 跑；具体 24 commands 在多 AI coding tool 的兼容性、61 detector rules 的实现细节、CLI 与浏览器扩展的底层架构未在档案中给出 |
| 主路径 | 开发者 → 装 `npx impeccable install` → 跑 `/impeccable init` → 扫描项目 → 写 PRODUCT.md → 用 24 commands 中任一个（polish / audit / critique / distill / animate / bolder / quieter）→ 61 deterministic detector rules 离线 check → 可选 LLM critique | 主路径为档案语义抽象；具体 PRODUCT.md 的 schema、24 commands 在多 AI coding tool（Claude Code / Codex / Cursor / Windsurf）的兼容性、CLI/浏览器扩展 ↔ 61 detector rules 的接口未在档案中明示 |
| 关键权衡 | 1 skill + 24 commands 覆盖面 vs 单一命令优化 + 61 deterministic detector rules 离线检查 vs LLM critique 准确性 + Anthropic frontend-design 兼容性 vs 独立产品 + Apache-2.0 商用清晰 vs SaaS 模板化压制；具体 387030 KB 巨大工程量在多 file 的可靠性、impeccable.style 主页的活跃度未在档案中讨论 | 档案明示「Every model trained on the same SaaS templates + Skip the guidance and you get the same handful of tells on every project」+ 11 个月 76227⭐ + Apache-2.0 + impeccable.style |
| 最小 PoC | 在一个新项目上跑 `npx impeccable install`，再跑 `/impeccable init` 验证扫描 + 写 PRODUCT.md；用 `/impeccable polish` 验证 1 个 polish command + 61 detector rules 离线 check；再尝试 Claude Code / Codex / Cursor 多 AI tool 兼容性 | PoC 范围由档案「24 commands + 61 detector rules + 多 AI tool 兼容性」建议推导；具体 detector rules 在多 frontend stack 的覆盖广度、LLM critique 在多 LLM provider 的可移植性未在档案中讨论 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Dev[开发者] --> Install[npx impeccable install]
  Install --> Init[/impeccable init]
  Init --> Scan[扫描项目]
  Scan --> Ask[询问 material gaps<br/>在 durable product truth]
  Ask --> Product[写 PRODUCT.md<br/>audience + purpose + operating context<br/>constraints + voice + evidence]
  Product --> Cmds[24 commands<br/>polish / audit / critique<br/>distill / animate / bolder / quieter]
  Cmds --> Rule[61 deterministic<br/>detector rules]
  Rule --> CLI[CLI<br/>无 LLM 无 API key]
  Rule --> Ext[浏览器扩展<br/>无 LLM 无 API key]
  Cmds -.可选.-> LLM[LLM-only<br/>critique checks]
  CLI --> Result[detector rule 输出<br/>offline 离线运行]
  Ext --> Result
  Rule -.修复 SaaS telltale.-> Fix[Inter for everything<br/>purple-to-blue gradients<br/>cards nested in cards<br/>gray text on colored backgrounds<br/>rounded-square icon tile]
  Fix -.Visitor mode.-> Visitor[visitor mode
and visual direction<br/>incumbent or newly built]
  Init -.兼容.-> ACS[Anthropic frontend-design<br/>首 widely-used]
  Cmds -.兼容.-> Multi[Claude Code / Cursor<br/>Windsurf / Codex 等]
  Install -.工程量.-> Big[387030 KB<br/>巨大工程量]
  Result -.商用.-> Biz[Apache-2.0 商用清晰<br/>impeccable.style]
```

## 架构启发
impeccable 的核心启发是 **"AI 设计语言应该 deterministic + LLM critique 双轨，正如 Linter + Type-checker 双轨"**。之前的设计 skill 全部依赖 LLM 评审（成本高、不稳定、不可复现），impeccable 把「确定性 check」与「LLM critique」分离**——61 个 deterministic rules 先离线 check，明确告诉开发者「这里有 SaaS telltale」「这里没有 durable product truth」，LLM critique 只在 deterministic 通过后做语义级 critique。这是把软件工程「lint first, type-check second, then human review」的成熟模式推到 AI 设计领域。387030 KB 巨大工程量 + 24 commands + 61 detector rules + PRODUCT.md schema 反映这是严肃工程化尝试，不是「再加一个 skill」的 quick hack。

## 定位判断
**AI 设计语言候选标准项目。** impeccable 不仅是一个 skill 集合，更试图成为 AI 编程 Agent 的「设计语言标准」——类似 ESLint 之于 JavaScript / Prettier 之于代码格式化。若成功，它会成为每个 AI 编程 Agent 默认装载的设计 skill，具有生态级价值。11 个月 76227⭐ 已显示真实严肃工程化信号。但"标准"取决于一个关键问题：24 commands + 61 detector rules 在多 AI coding tool 的兼容性能否持续——若任一 AI tool 格式大幅变更，impeccable 适配成本陡增。目前定位是"AI 设计语言领域的下一代"，向 standard 演进是合理路径。

## 风险 / 局限 / 泡沫点
- **24 commands 多 AI tool 兼容性:** 24 commands 在 Claude Code / Codex / Cursor / Windsurf 等多 AI coding tool 的兼容性是开放问题
- **61 detector rules 覆盖广度:** detector rules 在多 frontend stack（React / Vue / Svelte / Solid 等）的覆盖广度未明示
- **巨大工程量维护成本:** 387030 KB 巨大工程量反映 24 commands + 61 rules 的实现深度，但维护成本极高
- **Anthropic 官方 frontend-design 威胁:** Anthropic 可能在 frontend-design 中加入 deterministic check + 24 commands，挤压第三方空间
- **SaaS 模板化压制 vs 设计创新:** 「SaaS telltale 修复」可能反过来压制设计创新（设计师可能故意用 Inter / purple-to-blue gradients）
- **topics 0 个覆盖:** README 未明示 topics，发现性可能受限

## 与同类项目的关系
- **vs Anthropic frontend-design:** Anthropic 官方设计 skill，仅 LLM critique，无 deterministic check；impeccable 在 frontend-design 基础上加 24 commands + 61 rules + PRODUCT.md
- **vs ESLint / Prettier:** 通用 lint/format 工具，需手动配置；impeccable 是 AI 设计专用 deterministic check
- **vs Tailwind CSS:** 实用工具型 CSS 框架，不解决设计方向问题；impeccable 解决设计方向问题
- **vs shadcn/ui:** UI 组件集合，提供默认设计；impeccable 反对「默认设计」，鼓励 durable product truth
- **vs design tokens / style dictionary:** 设计 token 系统，需手动配置；impeccable 自动扫描 + 写 PRODUCT.md

## 是否值得持续跟踪
**值得跟踪（AI 设计语言候选标准）。** impeccable 代表了 AI 编程 Agent「设计语言确定性化」的诉求，无论其本身成败，这一方向是行业趋势。建议关注：24 commands 在多 AI tool 的兼容性（决定其标准地位）、61 detector rules 在多 frontend stack 的覆盖广度（决定其实用价值）、Anthropic frontend-design 是否会加入 deterministic check（决定其"差异化"命运）。对 AI 编程 Agent 用户，impeccable 是获取「设计方向 + 离线 check」的实用工具，值得直接试用。对 AI 编程生态观察者，它是"AI 设计语言"赛道的头部样本。

## 后续观察点
- 24 commands 是否在 Claude Code / Codex / Cursor / Windsurf 等多 AI tool 全部兼容
- 61 detector rules 覆盖广度（React / Vue / Svelte / Solid / Astro 等多 framework）
- 是否演化为独立 CLI 工具（脱离 AI coding tool 独立运行）
- 与 Anthropic frontend-design 的关系（互补 vs 替代）
- 浏览器扩展是否扩展到 Chrome / Firefox / Safari 多浏览器
- 企业采用（设计团队是否将此作为标准 design linter）

---
> 数据来源: GitHub API (2026-10-05) | Stars: 76,227 | Forks: 4,546 | License: Apache-2.0 | 语言: JavaScript | 创建: 2025-11-16 | fork/star 5.9%