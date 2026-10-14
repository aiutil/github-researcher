---
title: "outcrawlai/scout"
slug: scout
date_added: "2026-10-15"
last_seen_date: "2026-10-15"
category: "工具型"
emoji: "🤖"
stars: "636 stars"
stars_delta: "2 天 636⭐ ⑂22 fork/star 3.5%（持续增长）"
language: "TypeScript"
score: 92
tags: ["scout","outcrawlai","browser-agent","ai-agent","browser-automation","playwright","cdp","devtools-protocol","mcp","lm-provider","structured-output","json-schema","bun","monorepo","typescript","apache-2","outcrawl","aeonmind","2-days"]
url: "https://github.com/outcrawlai/scout"
---

# outcrawlai/scout

## 一句话定位
Scout 是一个 open-source browser agent——用户用自然语言告诉它任务，它在真实浏览器里 read / click / type / scroll 直到任务完成并返回结构化答案，最佳运行于 Outcrawl 的云浏览器服务（residential + captcha solving + 自然输入 + 录像回放），同时可在本地 launch / 已有的 CDP 上跑。

## 它解决的问题
2026 年 AI agent 进入真实浏览器完成任务的诉求极强，但现有方案要么是「playwright + stealth + 自己接 LLM 写 loop」的离散组合，要么是 Browser Use / Skyvern 等单一 SaaS 端到端方案的 vendor-lock。Scout 直击痛点：（1）**`new Scout({ browser, models }).run(task)`**——一行调用把 browser 与 4 角色模型串起来；（2）**BYO 任意 chat completions API**——hands / brain / eyes / extract 四角色各自可独立选 model / baseURL / API key，不必锁单一 provider；（3）**JSON Schema → 结构化答案**——不用 post-processing 直接拿到 shape 一致的 data；（4）**三种 browser 入口**——Outcrawl cloud（residential + captcha + 自然输入 + 录像回放推荐）/ 本机 `browser: { launch: {} }` / 已有 CDP `browser: { cdpUrl: 'http://127.0.0.1:9222' }`；（5）**monorepo 6 packages**——把 runtime agent loop、model prompts、CDP browser driver、agenthands pointer/keyboard 拆为清晰边界。

## 为什么值得关注（2026-10-15）
- **Stars:** 636（截至 2026-10-15），2 天 636⭐ ⑂22 fork/star 3.5%，**增长率** 3.5%（fork/star 反映社区参与度，浏览器 agent 类项目 fork 多因二次开发成本低）
- **Forks:** 22，社区参与度中（agenthands MIT 自带 licence 鼓励 fork）
- **Size:** 14434 KB（monorepo 6 packages + demo assets + docs）
- **License:** Apache-2.0（仓库整体）；`packages/agenthands` 自带 MIT（鼓励 pointer/keyboard 跨项目引用）
- **语言:** TypeScript + bun + Bun（runtime + test）
- **活跃度:** created 2026-10-13，pushed_at 2026-10-14，持续高活跃
- **平台:** Node 22+ + Outcrawl cloud / 本地 Chromium / CDP-attachable browser

## 热度来源判断
Scout 的热度是 **「AI agent 真实基础设施刚需 × 严肃工程化 monorepo 6 packages × 4 角色模型分工 × Outcrawl cloud 旁路商业浏览器接入 × BYO 任意 chat completions API × JSON Schema → 结构化答案 × 92.5% on Browser Use 80-site benchmark × Apache-2.0 (agenthands MIT)」** 的组合。AI agent 在真实浏览器工作 99% 失败的原因不是模型，是浏览器层——数据中心 IP 被反爬 / 验证码卡住 / 登录态丢失 / 点击没点上。Scout 把「住宅 IP + 自家 captcha solver + 自然输入 + 录像回放」做成 Scout runs best on Outcrawl's cloud 的旁路选项，同时不锁定 model provider。92.5% 在 Browser Use 80-site benchmark（next best 81.4%）的实测数据是这个项目最硬的证据。

## 关键技术亮点
1. **Tell it the task 一行 API：** `new Scout({ browser: 'outcrawl' | { launch } | { cdpUrl }, models: { hands, brain?, eyes?, extract? } }).run(task)`，完整任务起点
2. **BYO 4 角色模型：** hands（每步 click/type/scroll/read，快模型收益高）+ brain（规划长任务可选）+ eyes（需多模态截图可选）+ extract（读 page → schema 答案可选，缺则 hands 兼任）
3. **JSON Schema → 结构化答案：** 传 JSON Schema 与 task，answer 直接是 schema-shape；service 拒绝时设 `structuredOutput: 'json_object' | 'strict'` 提示
4. **Outcrawl cloud 旁路：** residential connections + captcha solving + natural input（browser 自计划 pointer / scroll / keystroke）+ recordings + nothing to install；1000 free credits / month no card needed
5. **monorepo 6 packages 严肃工程化：** packages/scout / packages/runtime（agent loop: look at the page, pick an action, act, check, repeat）/ packages/model（prompts, the job split, structured replies, provider-neutral clients）/ packages/scout-core（shared types）/ packages/scout-cdp（drives a real browser over the DevTools protocol: navigation, clicks, typing, scrolling, tabs, snapshots）/ packages/agenthands（pointer/keyboard input planning，MIT 自带）
6. **每 run 返回完整元数据：** status（completed / partial / capped / failed）+ data（schema-shape 答案）+ error + steps（each action + timing + success/fail）+ costUsd + replayUrl（云端录像回放）
7. **caps：steps / duration / budget：** limit reached 是 normal ending，agent 不会试图无限做
8. **CDP 旁路：** 已有 CDP browser 可通过 `cdpUrl: 'http://127.0.0.1:9222'` 直接挂，scout-cdp 完成驱动（navigation / clicks / typing / scrolling / tabs / snapshots）
9. **AGENTS.md + DCO：** Pull requests welcome + sign-off each commit（`git commit -s`，Developer Certificate of Origin）
10. **automatic mirror to public repo：** 改动先在 Outcrawl 内部生产仓库落地 + tests 后同步到公开 GitHub
11. **bun install + bun test：** 开发体验一致
12. **92.5% on Browser Use 80-site benchmark：** 3 full runs 2026-10-07 用 Browser Use 自家代码打分（next best 81.4%）
13. **Outcrawl 旁路 SaaS 商业模式：** 1k free credits/month + 扩展按 Outcrawl browser session 计费 + 用户的 model calls 仍走用户自己的服务

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 一个 Scout 前门（npm @outcrawl/scout）+ 一个 runtime agent loop（look at the page, pick an action, act, check, repeat）+ 一个 model 包（prompts, the job split, structured replies, provider-neutral clients）+ 一个 scout-core（shared types）+ 一个 scout-cdp（drives a real browser over DevTools: navigation, clicks, typing, scrolling, tabs, snapshots）+ 一个 agenthands 包（pointer / keyboard input planning，MIT 自带 licence）+ 一个 Outcrawl 云浏览器服务（residential + captcha + natural input + replays + 1000 free credits/month）+ 一个用户自选 chat completions provider（hosted/gateway/local）+ 一个 Benchmark pipeline（Browser Use 80-site + 自家 code） | 仅基于 README「Tell it the task + Start in three steps + Bring your own models + Browser Use 80-site 92.5% + monorepo 6 packages + Scout runs best on Outcrawl's cloud + 1000 free credits + MIT/Apache-2.0」+ license badge + size 推断；具体 Outcrawl 内部基础设施（browser fleet size / captcha solver 选型 / replay 录制后端 / cost 上限）未在档案明示 |
| 主路径 | 用户 `npm i @outcrawl/scout` + 配 OUTCRAWL_API_KEY / SCOUT_BASE_URL / SCOUT_API_KEY / SCOUT_HANDS_MODEL + 写 `new Scout({ browser: 'outcrawl', models: { hands } }).run('找 HN top 3 stories')` → Scout 在云端打开 residential browser → hands 模型 read / click / type / scroll → brain 规划 step → eyes 看 screenshot（如需）→ extract 给 schema-shape 答案 → 返回 { status, data, steps, costUsd, replayUrl } | 主路径为 README「Start in three steps + Examples（research / form-fill / compare / login）+ What you get back + Caps」段落整理；具体 model provider 容错、step-level retry 策略、brain 与 eyes 在长跨页任务的实际调度权重未在档案明示 |
| 关键权衡 | LLM-driven browser agent vs 静态重编译（ps2-web-recomp）vs 反检测浏览器底层（dots）vs Scout CLI bridge vs Outcrawl cloud 仅一家支持 vs monorepo 6 包 vs BYO 4 role models vs JSON Schema schema-shape vs 92.5% on 80-site vs 1k free credits/month vs AGENTS.md/DCO 协议 vs Apache-2.0（agenthands 自带 MIT）vs automatic mirror to public repo | 权衡来自 README「Scout runs best on Outcrawl's cloud + It also runs on your own machine + 4 roles + monorepo + 92.5% benchmark + 1000 free credits + Apache-2.0 + DCO + automatic mirror」 |
| 最小 PoC | 装 `@outcrawl/scout` + 拿 OUTCRAWL_API_KEY（1000 free credits）+ 配 OPENAI_API_KEY 作 hands + 配 OPENAI_BASE_URL → 跑 `new Scout({ browser: 'outcrawl', models: { hands: { model: 'gpt-4o-mini', baseURL, apiKey } } }).run('Go to books.toscrape.com, open the first book in the Poetry category and report its title and price')` → 验证 5 步完成 + replay 可看 | PoC 由 README「Start in three steps + Examples + demo-light.gif」段落整理；具体 captcha 命中率、replay 录像大小、costUsd 在不同 task 上的分布未在档案明示 |
| 证据边界 | 仅核验：仓库存在、stars/forks/description/license/size/language 来自 GitHub API；README 节录自 raw 接口；npm @outcrawl/scout + Aeonmind LLC + monorepo 6 packages + 92.5% on 80-site + 1000 free credits + MIT/Apache-2.0 由 README 直接叙述 | 待核验：Outcrawl 内部 browser fleet size / captcha solver / replay 录制后端 / cost 计费公式 / 自动 mirror 仓库间的差异 / 数据治理 / multi-task 在同一 browser 上的并发隔离 |

## 架构启发
Scout 的核心启发是 **「AI agent 的浏览器应该是可旁路的 SaaS + 可换模型的 4 角色 + 结构化答案 + 一次调用即可」**。当前 AI browser agent 的两个极端要么 vendor-lock（Browser Use / Skyvern 等 SaaS 端到端），要么 DIY（playwright + stealth + 自建 LLM loop + captcha 自己接）。Scout 把商业浏览器服务（residential + captcha + natural input + replay）做成「`browser: 'outcrawl'`」旁路选项，把模型选型做成「`models: { hands, brain, eyes, extract }`」4 角色 BYO，把答案做成「JSON Schema → 结构化」，这是浏览器 agent 的现实路径。这指向 **「LLM-driven agent 的栈应该每一层都可旁路：browser 可 SaaS 也可本地 + model 可每角色独立选 provider + answer 可 schema-shaped」**。Scout 还展示了 **「vendor-lock 反例 = 把每一层做成可独立选的可选项」**——这是 2026 年 AI 基础设施的关键哲学。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart TB
  User[调用方<br/>npx tsx task.ts] -->|run task| Front[packages/scout<br/>new Scout().run 入口]
  Front --> Runtime[packages/runtime<br/>agent loop look→act→check→repeat]
  Runtime --> Model[packages/model<br/>prompts + job split + provider-neutral clients]
  Model --> Hands[hands 模型<br/>click/type/scroll/read]
  Model -.可选.-> Brain[brain 模型<br/>规划 step]
  Model -.可选.-> Eyes[eyes 模型<br/>看 screenshot 多模态]
  Model -.可选.-> Extract[extract 模型<br/>page → schema 答案]
  Runtime --> Browser3{browser 三选一}
  Browser3 -->|outcrawl| Cloud[Outcrawl cloud<br/>residential + captcha + natural input + replays<br/>1000 free credits/month]
  Browser3 -->|launch| Local[本机 Chromium<br/>playwright-core + headless 可关]
  Browser3 -->|cdpUrl| CDP[已有的 CDP browser<br/>127.0.0.1:9222]
  Cloud --> Replay[replayUrl 录像回放<br/>costUsd 计费]
  Runtime --> ScoutCdp[packages/scout-cdp<br/>DevTools protocol<br/>navigation/click/type/scroll/tabs/snapshots]
  Local --> AgentHands[packages/agenthands<br/>pointer + keyboard input planning MIT]
  Runtime --> Out[返回 result<br/>status data error steps costUsd replayUrl]
  Schema[JSON Schema] -.-> Runtime
```

## 定位判断
**平台候选型项目（open-source browser agent + 商业 Outcrawl cloud 旁路）。** Scout 不仅是工具，更是 AI browser agent 的开放栈——运行时（runtime agent loop）+ 模型适配（provider-neutral clients）+ 浏览器驱动（CDP）+ 旁路商业服务（Outcrawl cloud）+ 旁路 MIT 输入控件（agenthands）。它把「AI 在浏览器工作的整套真实基础设施」做成可重用的 6 packages，同时通过 Outcrawl cloud 维持可持续商业模式（不是 vendor-lock SaaS，是 1000 free credits/month 旁路 + 商用 pay-as-you-go）。92.5% on Browser Use 80-site 的硬数据 + 4 角色模型分工 + JSON Schema 答案使其具备「未来 browser agent 工业栈候选」地位。能否持续，取决于（a）Outcrawl cloud 的稳定 + 规模；（b）4 角色模型的 prompt 是否在新模型上不需重写；（c）自动 mirror 公开仓库同步的纪律。

## 风险/局限/泡沫点
- **Outcrawl cloud 单点依赖：** 推荐的 browser 是 Outcrawl cloud，独立性依赖一家公司；具体 fleet size / captcha solver 选型 / replay 录制后端 / cost 计费公式均不透明
- **automatic mirror 公开 repo 的同步延迟：** 内部生产仓库与公开 GitHub 仓库同步延迟 + 内容差异未明示
- **parallel task 共享同一 browser 的并发隔离：** 多任务在同一 outcrawl browser 上的并发行为、隔离度未明
- **replay 录像内容安全 / 隐私合规：** 云端录像默认启用，敏感场景隐私边界 + 合规（GDPR / CCPA）需用户自审
- **captcha solver 法律与伦理：** 部分 captcha 服务商对自动解题服务的 TOS 边界存在灰区
- **4 角色模型责任边界：** 如果 task 失败，是 hands / brain / eyes / extract 哪个角色导致未明示；debug 体验不一定清晰
- **vs 静态重编译（ps2-web-recomp）+ 反检测浏览器底层（feder-cr/dots）方向不同：** scout 走 LLM-driven，ps2-web-recomp 走静态重编译，feder-cr/dots 走 patched Firefox 内核反检测；三者面向不同任务边界，不应混淆
- **Apache-2.0 + agenthands MIT 双 license：** 用户在二次开发时需同时考虑两套；OUTCRAWL_API_KEY 与 model provider key 双重管理

## 与同类项目的关系
- **vs Browser Use / Skyvern：** 那些是 vendor-lock SaaS 端到端 agent；Scout 是 monorepo + BYO model + 旁路 Outcrawl cloud + MIT/Apache-2.0，更开放
- **vs playwright + stealth + 自建 LLM loop：** 那是离散组合；Scout 是「`new Scout().run()`」一次性封装 + 4 角色 + monorepo 严肃工程化
- **vs feder-cr/dots（patched Firefox C++ 内核）：** dots 是反检测浏览器底层；Scout 是 LLM-driven agent 抽象 + 用 Outcrawl cloud 旁路反检测；dots 是更底层反浏览器指纹，Scout 是更上层 agent loop
- **vs anthropics/skills / wshobson/agents：** 那些是 skills/插件市场；Scout 是 open-source browser agent runtime，互补关系
- **vs PS2 静态重编译（snuri00/ps2-web-recomp）：** 完全不同的任务（游戏 vs 网页）；方法（LLM-driven agent vs static recompilation）也不同
- **vs models.dev / Browser Use native models：** models.dev 列模型目录；Scout 用模型清单 + structured answer

## 是否值得持续跟踪
**值得跟踪（AI browser agent 开放栈候选）。** Scout 代表了 2026 年 AI agent 在真实浏览器工作的开放栈范式：monorepo 6 packages + 4 角色 BYO model + Outcrawl cloud 旁路商业服务 + JSON Schema 结构化答案 + 92.5% on 80-site + Apache-2.0 (agenthands MIT)。建议关注：（a）Outcrawl cloud 的 fleet 透明度 + cost 计费公式是否公开；（b）自动 mirror 公开仓库的同步纪律；（c）4 角色模型对新发布的 LLM 适配是否及时；（d）parallel task 并发隔离；（e）replay 隐私合规工具链。对需要在真实浏览器自动化任何任务（research / form-fill / compare / login）的团队 / SaaS / 个人 agent，Scout 是 `npm i @outcrawl/scout` 即可用的严肃工程化路径。对 AI 基础设施观察者，它是「AI browser agent 开放栈」的样本。

## 后续观察点
- Outcrawl cloud browser fleet size / captcha solver 选型 / replay 录制后端 / 计费公式是否公开
- monorepo 6 packages 之间是否有 SDK 边界被外部进一步使用（如只引用 scout-cdp）
- 4 角色模型在新 LLM（如 GPT-5 / Claude 5 / Gemini 3）发布后 prompt 是否继续 work
- automatic mirror 公开仓库的 sync commit 与内部生产仓库的差异、频率
- parallel task 在同一 outcrawl browser 上的并发隔离、状态隔离
- replay 录像的隐私合规工具链（如选择性录像 / 字段脱敏）
- 1k free credits / month no card 的商业上限与升级路径
- 与其它商业浏览器服务（如 Browserbase / Steel.dev 等）的互通 / 替代

---
> 数据来源: GitHub API (2026-10-15) | Stars: 636 | Forks: 22 | License: Apache-2.0 (agenthands MIT) | 语言: TypeScript | 创建: 2026-10-13
