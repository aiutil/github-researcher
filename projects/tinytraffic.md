---
title: "egoist/tinytraffic"
slug: "tinytraffic"
date_added: "2026-11-12"
last_seen_date: "2026-11-12"
category: "生产可用候选"
emoji: "📊"
stars: "179 stars"
stars_delta: "⭐ 2026-11-12 建档（快照 2026-11-12 CST，仓库创建于 2026-11-10T09:39:00Z，约 36 小时）：179⭐ ⑂10 · subs 0 · oi 0 · 25 commits · 482 KB · 100 blobs · TypeScript · **AGPL-3.0** · User `egoist`（账号 **2014-09-15** 创建，**843 个公开仓库**，**13,985 followers**）"
language: "TypeScript"
score: 91
tags: ["web-analytics", "privacy", "duckdb", "go", "single-binary", "plausible-compatible", "self-hosted", "clickhouse"]
url: "https://github.com/egoist/tinytraffic"
---

# egoist/tinytraffic

## 一句话定位
**自托管的隐私友好网页分析：Go + DuckDB 后端 + 嵌入二进制的 Solid/TanStack 仪表盘，零 cookie、无 IP 存储、约 1 KB 的追踪脚本**，并且**明确接受 Plausible 的事件格式**（所以已有的 Plausible 集成可直接复用）。

## 它解决的问题
⭐⭐⭐⭐⭐ **主流网页分析的困境是「要拿到有用的数据，就必须先拿到可识别的人」。** Google Analytics 用 cookie 做标识符；Plausible/Matomo 之类的隐私派工具仍在做 IP 哈希与跨站追踪；Cloudflare/Umami 这类则把「自托管」当成卖点但仍要你接受它们的标识方案。

⭐⭐⭐⭐⭐ **tinytraffic 的选择是把自己的边界画得很硬：** README 的 Privacy 一段原文是「**no cookies or storage. Visitors are identified by `hash(daily salt, site, IP, user agent)`. The salt rotates at midnight in the site's timezone, and the IP is never stored.**」⭐⭐⭐⭐⭐ **即：它不是「不给第三方 cookie」，而是「自己也不留标识」—— 用一个每天轮换的盐做哈希，跨天不可关联，IP 本身从不落盘。**

⭐⭐⭐⭐⭐ **而这个选择带来一个真实的产品难题并被正面处理了：轮换的盐意味着「同一天内同一访客可识别，跨天不可识别」，这直接影响 bounce rate 与 visit duration 的计算。** README 明写 salt 是「rotates at midnight in the site's timezone」—— **注意是站点时区而非 UTC，这是一条把「统计口径」写进实现的决定。**

⭐⭐⭐⭐ **第二个它解决的问题是「部署形态」：** 一个 binary + 一个 DuckDB 文件，无外部服务依赖，Docker 一行起，也支持 Dokploy/Traefik/Caddy/nginx 反代。

## 为什么值得关注（2026-11-12）

⭐⭐⭐⭐⭐ **因为它是本日最不像「农场」的一个项目，而它的作者本身就是本日最强的可信度信号：账号 `egoist` 创建于 2014-09-15，有 843 个公开仓库、13,985 followers。** ⭐⭐⭐⭐⭐ **对照本日报连续多日记录的观察 —— 新账号、无 followers、单 commit、md5 模板复用 —— 这是一个 12 年历史的账号在 2026-11-10 发布的新项目。**

⭐⭐⭐⭐⭐ **而它的 commit 历史是「工程师式的连续工作」形态，与本日的 `auto-twitch-drops-claim` 形成教科书级对照：**

```
2026-11-11T15:56:19Z  Add AGPL-3.0 license
2026-11-11T15:15:59Z  Add public dashboards that anyone can view without signing in
2026-11-11T14:56:52Z  Rotate visitor salt at midnight in each site's timezone
2026-11-11T14:33:12Z  Add ClickHouse as a storage backend (#1)
2026-11-11T13:20:52Z  Redirect signed-out visitors to sign-in on the server
2026-11-11T13:10:37Z  Document stop-first update order for Dokploy deployments
2026-11-11T13:06:34Z  Document TT_TRUST_PROXY for deployments behind a reverse proxy
...
```

⭐⭐⭐⭐⭐ **这 10 条 commit 每一件都是一个具体的功能或决定，而不是「import analyze」这类无语义双词。** ⭐⭐⭐⭐⭐ **而且它有一个真实外部贡献的痕迹：`Add ClickHouse as a storage backend (#1)` —— 带 PR 编号 #1，即这是别人提的 PR。**

⭐⭐⭐⭐⭐ **而 11-11 当天它还在连续推进（`pushed_at` = 2026-11-11T21:25:06Z，距仓库创建约 36 小时），星数已从创建时的 107 涨到 179。**

⭐⭐⭐⭐⭐ **第三个值得记的点：它的「反代信任」设计被写成了 README 里的一整段警告，而不是一句「支持反代」。** README 原文：「Behind a reverse proxy (Traefik, Caddy, nginx or Dokploy), add `-e TT_TRUST_PROXY=true` and drop `-p 8080:8080`, so the proxy is the only way in. Visitors are then located by their real IP. **Without the flag, every visitor appears to come from the proxy and shows as "Unknown", and viewers of public dashboards share one rate limit.**」⭐⭐⭐⭐⭐ **「不开这个 flag，所有访客都显示为 Unknown，且公开仪表盘的观众共享同一个限流配额」—— 这是把「配置错误的后果」明确写出来的写法。**

## 热度来源判断
**真实需求驱动的自发关注，且传播路径与农场不同。** 判据：
1. **⭐⭐⭐⭐⭐ 作者资历：** 12 年账号、843 个公开仓库、13,985 followers。⭐⭐⭐⭐⭐ **对照本日报记录的农场账号画像（`BankerInterface`、`Nobleglusurvive`、`SteelMillerBar` 等均为当天新建、0 followers、仅 1–2 个公开仓库），这是两个完全不同的分布。**
2. **⭐⭐⭐⭐ commit 形态：** 25 个语义明确的提交，覆盖具体功能（public dashboards / salt 轮换 / ClickHouse 后端 / 反代信任 / 文档），其中一条带外部 PR 号。⭐⭐⭐⭐ **没有随机双词提交，没有 bot 提交。**
3. **⭐⭐⭐⭐ 代码量与结构：** 100 blobs，包含 `internal/ingest/bot.go`（bot 过滤）、`internal/store/events.go`、`internal/audit/`、`packages/tracker/`（追踪脚本）、`apps/dashboard/`（Solid + shadcn 风格组件）、`web/embed.go`（把前端嵌进 Go binary）。
4. **⭐⭐⭐ fork 分布正常。** ⭐⭐⭐ **⚠️ 精确的 fork 间隔中位数本窗口未单独取样（10 个 fork），仅记录量级正常。**
5. **⭐⭐⭐⭐⭐ 许可选择：AGPL-3.0 —— 这是网络软件里最「认真」的许可选择之一**（对比本日 `c6lang/c6` 的无 LICENSE 与 `auto-twitch-drops-claim` 的无 LICENSE）。

⭐⭐⭐⭐ **但必须同时给出反面：** ⭐⭐⭐ **subscribers 0、open issues 0、releases 0 —— 它没有任何深度关注者、没有 issue、没有版本发布。** ⭐⭐⭐⭐ **即：179⭐ 里几乎没有「采用了之后又回来反馈」的那部分人。** ⭐⭐⭐ **这是「热度 ≠ 价值」主线的另一面 —— 本日报不主张 179⭐ 说明了什么被验证过的价值，只主张它是一个由资深作者构建、结构完整、但尚无外部验证的早期项目。**

## 关键技术亮点

1. **⭐⭐⭐⭐⭐ 单二进制 + 嵌入前端：** 「**Stack**: Go + DuckDB backend. The dashboard is TanStack Start (SPA mode) with Solid and shadcn-style components, **embedded in the binary**」。⭐⭐⭐⭐ `web/embed.go`（403 B）即嵌入点；部署物是「一个 binary、一个 DuckDB 文件」，**无 Node 运行时、无数据库服务、无 CDN**。

2. **⭐⭐⭐⭐⭐ 追踪脚本 ≈1 KB gzipped，并兼容 Plausible 事件格式：** 「**Tracker**: ~1 KB gzipped. Pageviews (including SPA navigation), outbound link clicks and custom events. **Accepts Plausible's event format, so existing Plausible integrations work.**」⭐⭐⭐⭐⭐ **「兼容别人的事件格式」是一个极聪明的迁移策略 —— 用户不用改埋点代码，只换接收端。**

3. **⭐⭐⭐⭐⭐ 访客标识 = `hash(daily salt, site, IP, user agent)`，IP 不落盘：** salt 每站点时区午夜轮换。⭐⭐⭐⭐⭐ **这是一个把「隐私」从口号变成具体算法、且把算法边界（当天内可关联、跨天不可）写进 README 的实现。**

4. **⭐⭐⭐⭐ 存储后端可切换（Go 内建 DuckDB + 可选 ClickHouse）：** commit「Add ClickHouse as a storage backend (#1)」是带 PR 号的外部贡献。⭐⭐⭐⭐ **「小规模用嵌入式、大规模用 ClickHouse」的分层存储是自托管分析工具的常见正确做法。**

5. **⭐⭐⭐⭐⭐ 公开仪表盘 + 限流模型被明确写出：** 「Make a site's stats public to share its dashboard with anyone, no sign-in needed (**rate limited to 300 requests a minute per IP**)」，且**「viewers of public dashboards share one rate limit」** —— 即限流是按 IP 而非按站点，与反代场景下的访客限流是两套独立的预算，**这个区别被写在了文档里。**

6. **⭐⭐⭐⭐ 反代信任是显式开关且有明确后果说明：** `TT_TRUST_PROXY=true` + 去掉端口映射（让代理成为唯一入口），README 同时写明**不开会怎样**（所有访客显示 Unknown、公开仪表盘观众共享限流）。

7. **⭐⭐⭐ 引导流程细节：** 「On first visit you choose a dashboard password, unless `TT_PASSWORD` set one. Then add a site and paste its snippet into the site's `<head>`」；且 commit「Keep setup form up after creating the password」—— **修的是一个具体的首次使用摩擦点。**

8. **⭐⭐⭐ 语言栈细节：** 「**Tracker**: ~1 KB gzipped」（TypeScript，`packages/tracker/`）、后端 Go、DuckDB 为 C++ 库因此需要 cgo、构建需 Go 1.26+ / Bun 1.4+ / C 编译器。

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | **单一进程**：Go 进程内含 HTTP 服务 + 事件摄取 + 审计 + 指标渲染 + 嵌入的 SPA 仪表盘；外部依赖只有「一个 DuckDB 文件」（可选 ClickHouse）与「地理定位数据库」（构建期由 `bun install` 抓取）。**边界之外没有任何常驻服务。** | README 的 Stack / Quick start / Tracking 段 + 树清单（`internal/ingest`、`internal/store`、`internal/audit`、`packages/tracker`、`apps/dashboard`、`web/embed.go`）为实测；**GeoIP 数据库的抓取方式仅见 README 一句，未核验** |
| 主路径 | 浏览器 → `<script defer data-domain=... src=.../js/script.js>` → 摄取端（`internal/ingest`，含 bot 过滤）→ `hash(daily salt, site, IP, UA)` → 事件存储（DuckDB / ClickHouse）→ 仪表盘查询（`internal/store` + 嵌入 SPA）。⭐ **公开仪表盘的读路径与埋点写路径共用同一服务，但限流预算是分开的。** | 主路径由目录结构 + README 各段拼出；**`internal/store/events.go`（1,103 B）与 `internal/ingest/bot.go`（869 B）的内部实现未逐行核验**；⭐ **「读路径与写路径共用服务」为由文件布局推断** |
| 关键权衡 | **① 隐私 vs 统计精度** —— 放弃跨天访客关联，换取「不存 IP」；② **嵌入前端 vs 独立前端服务** —— 换来零额外依赖，代价是仪表盘改动要重新编译 Go；③ **DuckDB 嵌入式 vs ClickHouse 服务端** —— 默认零运维，代价是单机写入上限；④ **AGPL vs 更宽松许可** —— 选了网络传染性最强的那个 | 四项权衡均直接对应 README 明文（Privacy 段、Stack 段、commit「Add ClickHouse as a storage backend (#1)」、commit「Add AGPL-3.0 license」）；**「单机写入上限」为基于 DuckDB 特性的推断，未做压测** |
| 最小 PoC | **单站点 + 单容器**：Docker 起一个实例、设 `TT_PASSWORD`、加一个站点、贴一段 `<script>`、观察 24 小时内 pageview 与访客数；⭐ **退出路径 = 删掉容器与数据卷**（唯一持久状态是 DuckDB 文件）；⭐ **关键验收点不是「图表好看」，而是「次日 salt 轮换后，同一访客是否变为两个访客」—— 这是隐私承诺的直接检验** | PoC 范围由 README 的 Quick start 与 Data/DuckDB 描述推导；**「salt 轮换后访客被拆分」为基于 README 描述的预期，未实测**；**数据删除的彻底性（DuckDB 文件内的残留）未核验** |

## 架构启发
⭐⭐⭐⭐⭐ **最值得抄的一条：「把隐私承诺写成一条可检验的算法，而不是一句形容词」。** `hash(daily salt, site, IP, user agent)` + salt 按站点时区午夜轮换 —— ⭐⭐⭐⭐⭐ **这句话可以被第三方独立验证**（抓一天的访客数、跨天比对、确认 IP 未落盘），而「隐私友好」这四个字不能。** ⭐⭐⭐⭐⭐ **这与本日报连日记录的「把边界写进输出」是同一条线索** —— 11-08 记录的 `satmux` 把物理 RTT 下界写进 `## Limits`，`phoneuse` 用实测环境表标注「Tested with」，10-26 记录的 `brotli-checker` 明写「exit 0 does not establish that the running app is fixed」。**它们共同指向一条原则：可被证伪的承诺才是承诺。**

⭐⭐⭐⭐⭐ **第二条关于「兼容别人的事件格式」。** 「Accepts Plausible's event format, so existing Plausible integrations work」—— ⭐⭐⭐⭐⭐ **这是一个把迁移成本降到零的设计决策**：用户不需要改一行埋点代码。⭐⭐⭐⭐ **对于一个要与既有工具竞争的独立项目，**「我的格式和你的兼容」比「我的格式更好」有效一个数量级** —— 因为它把用户的决策从「评估」降级为「切换」。

⭐⭐⭐⭐⭐ **第三条是关于「配置错误的后果」应该被文档化。** README 不是写「支持反代」，而是写「**不开这个 flag 会发生什么**」（所有访客显示 Unknown、公开仪表盘观众共享限流）。⭐⭐⭐⭐⭐ **大多数项目只写正确用法的 happy path，而错误配置的后果恰恰是运维事故的主要来源。**

⭐⭐⭐⭐⭐ **第四条关于「用一条 commit 记录一个决定」。** 25 条 commit 覆盖 36 小时，每条对应一件具体的事（加许可、加公开仪表盘、加 salt 轮换、加 ClickHouse、改反代行为）。⭐⭐⭐⭐⭐ **这种提交粒度使得「这个项目的历史就是它的设计决策日志」** —— 对比本日报记录的 `impacket-rs` 的 `ci(security): pin immutable commit SHAs for actions` 一类同样有信息量的条目。⭐⭐⭐⭐ **而这与本日报记录的 `raven` 用 `DECISIONS.md`（11-07 的 `hermes-voice`）是同一条思路：把「为什么这么选」留下。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；标注「待核验」的节点不应视为项目实现事实。

```mermaid
flowchart LR
  subgraph Browser[浏览器]
    Page[站点页面<br/>head 标签插入 script defer]
  end
  subgraph Single[单一 Go 进程 · 无外部常驻服务]
    Tracker[packages/tracker<br/>约 1 KB gzip 脚本<br/>含 SPA 导航与自定义事件]
    Ingest[internal/ingest<br/>事件摄取 + bot 过滤]
    Hash[访客标识<br/>hash(daily salt, site, IP, UA)]
    Salt[盐轮换<br/>按站点时区午夜<br/>跨天不可关联]
    Store[internal/store<br/>DuckDB 嵌入式<br/>可选 ClickHouse 服务端]
    Audit[internal/audit<br/>审计与指标]
    Dash[嵌入 SPA 仪表盘<br/>TanStack Start + Solid]
    Embed[web/embed.go<br/>前端打进二进制]
    Public[公开仪表盘<br/>每 IP 300 req/min<br/>观众共享同一限流预算]
    Proxy[TT_TRUST_PROXY=true<br/>反代信任开关]
  end
  subgraph Outside[边界外]
    Geo[地理定位数据库<br/>构建期由 bun install 抓取]
  end
  Page --> Tracker --> Ingest --> Hash --> Store
  Salt --> Hash
  Store --> Audit --> Dash
  Embed --> Dash
  Dash --> Public
  Proxy -.决定 IP 解析方式.-> Ingest
  Tracker -.格式兼容 Plausible 事件格式.-> Plausible[Plausible 既有集成<br/>无需改动埋点代码]
  Geo -.仅地理维度用.-> Audit
  Lim[未核验与边界<br/>「不存 IP」未在容器内实测<br/>DuckDB 文件内残留未核验<br/>单机写入上限为推断 未压测<br/>配置错误后果已文档化 访客显示 Unknown]
  Hash -.受其约束.-> Lim
  Store -.受其约束.-> Lim
```

## 定位判断
**生产可用候选（production-ready candidate），但必须附三个限定条件。** ⭐⭐⭐⭐⭐ **理由**：它有完整的可运行产品形态（单 binary + 单文件存储 + 嵌入仪表盘 + Docker 一行起）、有真实外部 PR、有清晰的隐私语义、有具体的错误配置说明、有活跃的提交节奏。

⭐⭐⭐⭐⭐ **三个限定条件必须一起写：**
1. **⭐⭐⭐⭐ 无版本发布（releases 0）、无 issue、subs 0** —— **即没有任何外部使用者的反馈闭环**。「生产可用候选」是**基于代码与文档质量的判断，不是基于使用证据的判断。**
2. **⭐⭐⭐⭐ 项目仅约 36 小时大（快照时）**，README 自己也标了 `v0.1.0-dev` 之外的状态吗？—— **⚠️ 更正：本仓库 README 未标注版本状态，`releases` 为 0 个。**
3. **⭐⭐⭐⭐ AGPL-3.0 的传染性** —— 若要嵌入进闭源商业产品，需要先走法律评估；**对纯自托管使用场景则无影响。**

⭐⭐⭐⭐ **与同类项目的关系：**
- **vs Plausible（官方自托管版）：** **协议兼容而非产品对等** —— tinytraffic 接受 Plausible 事件格式（迁移成本低），但**不提供 Plausible 的完整功能面**（无 A/B 测试、无 dashboard 分享链接、无数仓级扩展）。⭐⭐⭐⭐ **而它的差异化是「连 IP 都不存」+ 单二进制。**
- **vs Umami / Counter / GoAccess 等自托管分析：** 都是同类；tinytraffic 的差异是**零 cookie + 跨天不可关联 + 单文件 + DuckDB 嵌入式**，而 Umami 走 Postgres、GoAccess 走日志文件解析。
- **vs Matomo：** Matomo 功能更全但重得多；tinytraffic 是「一个人用的最小实现」。
- **vs Cloudflare Web Analytics：** 那个是托管的免费服务、无自托管；tinytraffic 是完全自托管。

## 风险 / 局限 / 泡沫点
- **⭐⭐⭐⭐ 隐私承诺的验证缺口：** 「IP 从不存储」与「salt 按站点时区午夜轮换」都是 **README 陈述**。⭐⭐⭐⭐ **本日报未部署、未抓包、未检查 DuckDB 文件内容，也未验证跨天访客拆分是否真的发生。** **一个声称不做标识的隐私工具，其隐私承诺必须由第三方审计而非作者自述确认。**
- **⭐⭐⭐⭐ 单作者单仓库（contributors 1 人 = egoist）：** 843 个仓库的作者做一件新事，**深度贡献的门槛全在一个人身上**。
- **⭐⭐⭐⭐ 无 release、无 issue：** 没有版本化发布节奏，**下游无法锁定版本**（Docker 镜像用的是 `:main` 标签 —— README 的 Quick start 写 `ghcr.io/egoist/tinytraffic:main`）。
- **⭐⭐⭐⭐ 构建链较重：** 需要 Go 1.26+ **且** Bun 1.4+ **且** C 编译器（cgo），**且**构建时会抓取 GeoIP 数据库 —— **对「一个二进制」的承诺来说，源码构建路径并不轻。**
- **⭐⭐⭐ DuckDB 的并发写入上限未知：** 单文件嵌入式数据库在高频写入下的表现**本日报未压测**。
- **⭐⭐⭐ ClickHouse 后端刚由外部 PR 加入（#1），未经充分验证。**
- **⭐⭐⭐ subs 0 / oi 0：** 179⭐ 无深度关注者 —— **热度与采用之间存在明显缺口。**
- **⚠️ 证据边界：** 未部署、未运行、未压测、未验证隐私承诺；star 数为快照绝对值，**单日 star 增量未做统计**（需分页遍历 stargazer 列表）；fork 间隔中位数未单独取样。

## 与同类项目的关系
- **vs Plausible：** **事件格式兼容关系**（这是本项目最值得注意的竞合方式）；tinytraffic 是「更小、更私密、更自托管」的替代，不是功能替代。
- **vs Umami：** 同为自托管分析，Umami 是 Postgres + React 全栈方案（更重、功能更多），tinytraffic 是 Go + DuckDB + 嵌入 SPA（更轻、部署更简单）。⭐⭐⭐⭐ **两者最本质的差别在隐私模型：Umami 默认做 IP 哈希（salt 可配，但存在），tinytraffic 明写不存 IP。**
- **vs GoAccess：** GoAccess 是**日志文件**分析器（读 nginx/caddy 日志），tinytraffic 是**主动埋点**分析器。⭐⭐⭐⭐ **两者可互补：不想埋点就用 GoAccess。**
- **vs Fathom / Simple Analytics（托管）：** 它们用「不 cookie、不存 PII」做差异化，tinytraffic 的差异是**你可以自己托管它**。
- **vs `c6lang/c6`（本日另一建档项目）：** ⭐⭐⭐⭐ **两者恰好构成一组关于「许可证与成熟度」的对照** —— c6（37⭐，761 blobs，无 LICENSE）与 tinytraffic（179⭐，100 blobs，AGPL-3.0，外部 PR）。⭐⭐⭐⭐ **两者的星数差 5 倍、体量差 7 倍，而更小的那一个的许可与外部参与状况明显更健康。**

## 是否值得持续跟踪
**值得跟踪，且建议在小规模自托管场景做一次真实验证。** 具体建议：
1. **⭐⭐⭐⭐⭐ 独立验证它的隐私承诺**（抓 48 小时的访客数据、确认 IP 未落盘、确认跨天访客被拆分）—— **这是本档案认为唯一值得投入的验证动作**；
2. **⭐⭐⭐⭐ 观察 releases 是否开始出现** —— `:main` 标签对生产使用是硬伤，**发布节奏是它从「候选」变成「可用」的分界线**；
3. **⭐⭐⭐⭐ 观察 issue 出现后的响应速度** —— 对一个单人项目，这比 star 数更能说明它值不值得依赖；
4. **⭐⭐⭐⭐ 关注 ClickHouse 后端的成熟度**（#1 是外部 PR）；
5. **⭐⭐⭐⭐⭐ 把它的两个设计当作可迁移范式**：**「把隐私承诺写成可检验的算法」与「兼容竞品的事件格式以降低迁移成本」** —— 这两条与语言无关，任何团队都能用。

## 后续观察点
- `pushed_at` 节奏（快照时 2026-11-11T21:25:06Z）；
- star 增速（107 → 179 在约 36 小时内）与 subs 何时从 0 变为非 0（**subs 是「从看热闹到在用」的转换指标**）；
- releases 是否出现、是否改用语义化版本标签；
- 是否出现第一个非作者的 issue；
- GeoIP 数据库的获取方式与许可（**README 未说明其来源与许可 —— 这是一个待核验的合规点**）。

---
> 数据来源: GitHub REST API 快照（2026-11-12 CST，仓库创建于 2026-11-10T09:39:00Z）| Stars: 179 | Forks: 10 | Subscribers: 0 | License: AGPL-3.0 | 语言: TypeScript | 体积: 482 KB / 100 blobs | 作者 `egoist`（2014-09-15 创建，843 repos，13,985 followers）
> **证据边界：** 未部署、未运行、未压测、未验证隐私承诺；star 增量为两次快照之间的差值推算，**单日 star 增量未做统计**。
