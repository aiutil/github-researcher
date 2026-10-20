---
title: "vercel-labs/fx0"
slug: "fx0"
date_added: "2026-10-21"
category: "基础设施候选"
emoji: "🎨"
stars: "296 stars"
stars_delta: "创建 2 天（2026-10-19 起）"
language: "TypeScript"
score: 90
tags: ["fx0", "vercel-labs", "libfx", "design-agent", "durable-agent", "vercel-workflow", "vercel-queues", "ai-gateway", "botid", "createfxagent", "createfxengine", "durable-sessions", "single-html-file", "design-md", "streaming", "retries", "steering", "claude-opus", "vercel", "typescript", "apache-2"]
url: "https://github.com/vercel-labs/fx0"
---

# vercel-labs/fx0

## 一句话定位
Vercel 官方 labs 发布的开源轻量 design agent：你描述一个页面，agent 把它写成一个 HTML 文件；核心价值不在 UI，而在于它是 `libfx` 的公开参考实现——一次 `createFxAgent()` 调用即获得 agent loop、streaming、tool calls、retries 和 durable sessions。

## 它解决的问题
"durable agent" 这个词在各家 SDK 文档里通常是抽象名词：崩溃后怎么续跑？后台跑完的账单挂到谁头上？agent 陷入死循环怎么刹车？fx0 把这三件事的答案写在了 README 首页，并给出可读的 TypeScript 分层——**这让它同时成为产品和一个可被逐条抄走的设计清单**。

第二类用户是产品团队：想要一个"描述页面→单文件 HTML"的极简设计工具，不想自己搭 agent 循环、队列、重试。fx0 挂在 fx0.vercel.dev 可直接试。

## 为什么值得关注（2026-10-21）
- **由做这套基础设施的公司自己公开参考实现**，比第三方教程可信度高一档
- **两条把成本和计费归属写进首页的工程约束**：`每轮 funding 必须在 Redis 里封存`（因为队列投递没有浏览器 cookie）、`每轮 64 model steps 上限`（因为 agent 会死循环烧钱）。这两条几乎必然出现在任何自建 agent 生产系统里，但极少见有项目写出来
- **fork-star 18.6%（296⭐ ⑂55），是本批四项目唯一显著高于平均的**，指向开发者读架构而非收藏
- 在线可试（fx0.vercel.dev），文档含深浅两色分层图

## 热度来源判断
**偏真实，但需要区分两类热度。** 支撑真实的一面：fork-star 18.6% 在"设计 agent 网页应用"这类通常"用完就走"的品类里属于异常高，说明存在一批**在读它架构**的开发者；README 把职责分层（fx0 / libfx / World / Queues / AI Gateway）画成了图，恰好是这类读者需要的形态。泡沫的一面：项目创建仅 2 天、`subscribers_count = 0`、`open_issues_count = 1`，7 天后 fork 是否继续增长才是判断依据。本档判断：**热度本身不足以支撑采用决策，但内容值得读。**

## 关键技术亮点
1. **一行调用换四件套**：`One createFxAgent() call gives it the agent loop, streaming, tool calls, retries and durable sessions`，外加 `createFxEngine()` 跑每个 subagent
2. **五层职责边界写死在 README**：fx0（UI / 鉴权 / agent 调用的设计工具 / Redis+Neon 里的 chat 历史）· libfx（每轮内的模型循环、tool calls、retries、steering）· Workflow World（每轮每步落盘）· Vercel Queues（prompt 备份 + 崩溃唤醒）· AI Gateway（收每一次模型调用，管计费归属）
3. **先存后 ack**：`POST /api/prompt` 在**一个 Redis 脚本**里把消息加进 transcript 再交给 libfx；libfx 先存后确认——保证"显示为已发送的消息不会丢"，且重试请求落到同一轮
4. **funding 封存**：队列投递没有浏览器 cookie，prompt 路由把 funding 封进 Redis；每条消息记录它所启动那一轮的 funding 归属（被准入的赞助 / 付费发送者的 OAuth grant + team）
5. **64 model steps 上限（含 subagent）**：README 直言 `keeps an agent stuck in a loop from running up a bill`
6. **800 秒 + 队列兜底**：`app/api/libfx` 声明 `maxDuration = 800`，`vercel.json` 用 `queue/v2beta` 订阅 libfx 队列主题、`retryAfterSeconds: 5`，崩溃后由队列唤醒新函数从最后保存步骤继续
7. **steer 语义**：空闲时发消息 = 新一轮；运行中发消息 = 插话（经 Queues 送达正在跑的那轮）。试用轮刻意让每条输入各成一轮，以隔离免费与付费资金
8. **成本闸门**：不登录每 IP 五次免费 Opus 5.5 Fast，BotID 防滥用，服务器专用 Gateway key 出资；十个 `design.md` 风格起步（源自 VoltAgent 的 awesome-design-md，可自上传）

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 四层：fx0（用户可见的一切：chat/实时预览/登录/设计工具/Redis+Neon 历史）· libfx（每个 turn 内的全部工作）· Vercel Workflow 的 World + Vercel Queues（落盘与崩溃唤醒）· AI Gateway（每次模型调用的路由与计费） | README「How fx0 uses libfx」五点分述 + `docs/diagrams/pieces-*.svg`；fx0 侧文件边界（`app/api/*`、`lib/agent.ts`）由 README 代码块路径推得 |
| 主路径 | 用户发消息 → `POST /api/prompt` 在一个 Redis 脚本里写入 transcript 并交给 libfx（libfx 先存后 ack）→ prompt 路由把 funding 封进 Redis → libfx 跑 turn、每步存进 World → 边跑边流式回用户 → 若函数崩溃或触 800 秒上限，Queues 在 `app/api/libfx` 唤醒新函数（`agent().wakeHandler()`）从最后保存步骤继续 | 全部由 README「Durability」段第 1–5 步 + 两个 TS 代码块 + vercel.json 片段直读 |
| 关键权衡 | 每步落盘 World（更贵但可续）vs 只存终态（更便宜但崩了全丢）/ 队列兜底（多一跳延迟）vs 纯同步（崩了就没）/ **64 步上限（防烧钱）vs 不设限（agent 可能真需要更久）** / 试用与付费资金严格隔离 vs 统一计费 / AI Gateway 统一收口 vs 直连模型厂商 | README 明示了 64 步与资金隔离的原因，但未给 World/Queues 的实际成本量级，也未论证 800 秒是否够长 |
| 最小 PoC | 1. `npm i libfx` + 任意 Next.js route 建 `createFxAgent()`（不传 durability 选项 → Vercel 上自动用 World+Queues，别处用本地文件）→ 2. `agent.newSessionId()` + `agent.session(id, {model, instructions, context})` → 3. `session.prompt(text, {messageId})` → 4. **故意在 turn 中途 kill 进程** → 5. 确认新函数从最后步骤继续、转录未丢 → 6. 故意让 agent 死循环，确认 64 步后停止 | 前 3 步由 README 内联 TS 代码给出（已注明 simplified）；4–6 步是对 README 明示行为的**可证伪测试设计**，本地复现所需账号/免费额度、libfx 版本待核验 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart TB
  subgraph 控制面与用户可见
    UI[fx0 Chat 与实时预览<br/>登录 · 设计工具]
    HIST[(Redis 转录与设置<br/>Neon 账号与历史)]
  end

  subgraph Agent 执行面
    AGT[libfx agent<br/>createFxAgent()<br/>模型循环 · 工具 · 重试 · steer]
    WF[(Workflow World<br/>每轮每步落盘)]
    Q[Vercel Queues<br/>prompt 备份 · 崩溃唤醒]
  end

  subgraph 计费面
    FW[Redis funding 封存<br/>每条消息记录所属轮的计费归属]
    GW[AI Gateway<br/>每一次模型调用]
    OAUTH[付费发送者<br/>OAuth token + team]
    TRIAL[服务器 trial key<br/>每 IP 5 次免费额度]
  end

  REQ[POST /api/prompt<br/>一个 Redis 脚本先存消息] --> HIST
  REQ --> AGT
  REQ -.封存计费归属.-> FW
  AGT <--> WF
  AGT <--> Q
  Q --> RT[app/api/libfx<br/>maxDuration=800<br/>wakeHandler 从最后步骤续跑]
  RT --> AGT
  AGT --> GW
  GW --> OAUTH
  GW --> TRIAL
  AGT --> UI
  BOT[BotID 防滥用] --> GW
  GAP1[非 Vercel 环境<br/>durable 降级为本地文件<br/>实现细节待核验]
  AGT -.降级.-> GAP1
  GAP2[agent 可搜索并抓取网页<br/>prompt injection 入口<br/>README 未讨论防护] -.-> AGT
```

## 架构启发
fx0 最重要的启发不在它的 UI，而在于它把「agent 的失败模式」显式地变成了架构约束。多数 agent 框架把 durable 当作一句宣传语，fx0 把它拆成三个可定位的故障点，并给每个故障点配了一条明确的恢复路径：**函数崩溃 → 队列唤醒新函数**、**队列投递丢 cookie → funding 在 Redis 里提前封存**、**agent 死循环 → 64 步硬上限**。

更深一层的启发是关于**钱的归属**：一旦 agent 在后台运行，任何"谁付的"的问题都会变成运维事故（账单挂错用户、被滥用者刷爆）。fx0 的做法——**每条消息记录它所启动那一轮的 funding**——把计费归属从"请求上下文"提升为"持久化状态"。这个模式可以直接搬到任何有异步 agent 的系统，与 agent 框架无关。

第三层启发关于**降级要写在明面上**：README 明确说 Vercel 上用 World + Queues，别处用本地文件。一个诚实的架构会承认自己在不同环境下的能力差异，而不是假装能力一致。这对读者的价值高于任何性能数字。

反面启发同样重要：**不要为了展示架构而在 README 里截断关键代码**。fx0 的 `apiKey: 'sessi...ed'` 这类 `elided` 占位符让读者能理解架构却不能直接复制——文档的可复制性和可读性之间需要一个明确的取舍，而 fx0 明显没有做这个取舍。

## 定位判断
**基础设施候选（参考实现型）。** fx0 双身：作为产品是一个"描述页面→单文件 HTML"的轻量设计工具，作为代码是 `libfx` 的分层样例。它最可能的位置不是被完整采用，而是被**抄走架构**——尤其是 funding 封存与 64 步上限这两条，会出现在任何自建 agent 生产系统里。相比 LangChain / CrewAI / OpenAI Agents SDK 这类通用框架，fx0 的独特性在于它是**云厂商自己开的、默认开启计费隔离与队列兜底的窄实现**。

## 风险 / 局限 / 泡沫点
- **README 大量使用 `elided` 截断**：如 `apiKey: 'sessi...ed'`，关键接入代码在公开 README 中并不完整——读者能理解架构但不能直接复制
- **强绑定 Vercel 生态**：World、Queues、AI Gateway、BotID 全为 Vercel 服务。README 称"on Vercel 用 World + Queues，别处用本地文件"——**非 Vercel 环境下 durable 语义是降级的**，这对想借鉴架构的团队是重要边界
- **默认模型绑定 Opus 5.5 Fast**：模型涨价或下架会直接改变成本模型
- **agent 可搜索并抓取网页**（README 明示 `The agent can search the web and fetch pages for reference`）——这是典型的 prompt injection 入口，README 未讨论防护
- **早期信号**：创建 2 天、`subscribers_count = 0`、`open_issues_count = 1`，社区尚未形成
- **免费额度机制可被针对**：每 IP 五次 + BotID 是常见形态，实际防护强度待观察

## 与同类项目的关系
- **vs LangChain / CrewAI / LlamaIndex**：那些是框架级通用抽象；fx0 是窄的、绑定 Vercel 的参考实现，胜在把计费与崩溃这两件"脏活"写清楚了
- **vs OpenAI Agents SDK / Anthropic SDK**：厂商官方 agent 库；fx0 不自己造模型循环，而是把这些细节在云上落地
- **vs Vercel Workflow 文档示例**：文档示例通常碎片化；fx0 是一个可运行的完整应用，可直接读
- **vs 各类"一键生成网页"的 AI 前端**：那些多是封装模型 API；fx0 的差异化在 durable + 计费隔离，不在生成质量

## 是否值得持续跟踪
**值得，且在本批四个项目中优先级最高——但理由与热度无关。** 哪怕 fx0 本身失败，"每轮 funding 封存"和"64 步上限"这两条约束会留在使用者的系统里。对任何要自建 agent 生产系统的团队，这份 README 值得当设计清单逐条读。**但今天不该基于它的 star 数做技术选型**：2 天、0 订阅者、代码在 README 中被截断。

## 后续观察点
- 7 天 / 30 天后 fork 是否继续增长（当前 fork-star 18.6%，是真实采用的先行指标）
- libfx 是否独立开源并发布许可与版本号（README 未提 libfx 本身的仓库与许可）
- 非 Vercel 环境（本地文件 durable）的实际语义到底降级到什么程度
- 是否补上网页抓取的 prompt injection 防护说明
- fx0 是否有付费/自托管形态，或始终是 demo 性质

---
*首次记录：2026-10-21*

> 数据来源: GitHub REST API + README 原文（2026-10-21 CST 06:00） | Stars: 296 | Forks: 55 | License: Apache-2.0 | 语言: TypeScript | 创建: 2026-10-19 | 推送: 2026-10-20 | Subscribers: 0 | Open Issues: 1