---
title: "juspay/streamgres"
slug: streamgres
date_added: 2026-10-10
last_seen_date: 2026-10-10
category: "基础设施候选"
emoji: "🌊"
stars: "365 stars"
score: 82
tags: ["subscription-native","sync-engine","postgresql","websocket","delta-stream","incremental-view","logical-replication","wal","order-by-limit-window","planner","rust","apache-2"]
url: "https://github.com/juspay/streamgres"
---

# juspay/streamgres

## 一句话定位
subscription-native PostgreSQL 同步引擎——客户端订阅 SQL 查询，通过 WebSocket 接收 rows added/removed/changed 增量 delta，写入成本 O(匹配条件数) 不 O(订阅数)，为开源生态提供「Hasura/Supabase realtime 开源替代 + 不收费 + 数据不出库」严肃工程化承诺。

## 它解决的问题
实时数据订阅是 SaaS / agent / finance / dashboard 等场景的核心需求。当前方案要么闭源收费（Hasura GraphQL、Supabase realtime），要么依赖 LISTEN/NOTIFY + 轮询（高延迟高开销），要么 materialized view（重建开销大）。Streamgres 直击中间地带：**subscription-native sync engine**，让 client 通过 WebSocket subscribe(SQL)，engine 维护 incrementally maintained view，每次 commit 把变更路由到 affected views，成本取决于 write 匹配的条件数而非订阅数。解决的是 **「实时数据订阅的写扩展性 + 跨订阅复用 + 数据不出库」的严肃工程化承诺问题**，是 Hasura/Supabase realtime 的开源严肃工程化替代尝试。

## 为什么值得关注
- **Stars:** 365（截至 2026-10-10），3 天 365⭐ ⑂11 fork/star 3.0%
- **Forks:** 11，社区参与度中等
- **Size:** 3235 KB
- **License:** Apache-2.0（商用清晰）
- **语言:** Rust
- **活跃度:** created 2026-10-07，pushed_at 2026-10-09，**3 天 365⭐ ⑂11 fork/star 3.0%**
- **治理:** juspay 团队（Juspay/Hyperotaian/HyperUDF/HyperSDK 同源 Indi 支付栈）

## 热度来源判断
Streamgres 的热度是 **「subscription-native sync engine 严肃工程化承诺 × WebSocket subscribe(SQL) × 写入成本 O(匹配条件数) 不 O(订阅数) × 相同查询共享视图 × ORDER BY/LIMIT 窗口 × LEFT/RIGHT/INNER/EXISTS planner × logical replication 订阅 × 写不到你的数据库 × live schema changes × Apache-2.0」** 的组合。Hasura/Supabase realtime 都是闭源 SaaS，开源方案稀缺；streamgres 提供「开源版 + Apache-2.0 + 写不到你的数据库」严肃工程化承诺组合。3 days 365⭐ ⑂11 fork/star 3.0% 反映「Hasura 替代」刚需。热度真实且具备严肃工程化承诺潜力——但与成熟闭源 SaaS 形成竞合，能否走长线需观察。

## 关键技术亮点
1. **Subscription-native:** 每个订阅是一个 incrementally maintained view，commit 变化路由到 affected views
2. **Write cost independent of subscriber count:** filter normalize + index per column，从 100→10000 订阅，写仍触 3-4 个条件
3. **Identical queries share work:** 相同查询共享一个视图一个行副本，新订阅者从内存服务
4. **ORDER BY / LIMIT 窗口:** client 收到确切页面 + 变化，离开页的行由 buffer 维护
5. **JOIN planner:** LEFT/RIGHT/INNER/EXISTS 子查询（含 OR 内）+ per-parent limits + planner picks driving side from row counts
6. **Consistent by construction:** 引擎停在 WAL 一个位置，初始读用不领先 snapshot，读中写入先 apply 再送达，client 永不看到 row 倒退

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | PostgreSQL 之上的订阅原生 sync engine；输入 WebSocket subscribe(SQL)，输出 rows added/removed 增量 delta；logical replication 订阅 primary/replica/standby；引擎本身写不到你的数据库 | 基于 README + Apache-2.0 + juspay 团队；SLO 指标、生产部署案例、压力测试结果未在档案中给出 |
| 主路径 | WebSocket subscribe(SQL) → 初始 snapshot 读 → 创建 incrementally maintained view → 订阅 logical replication → commit 触发 → filter normalize+route to affected views → 输出 delta 给 client | 主路径为 README 语义抽象；具体 LSN 位置算法、filter normalize 实现、planner 决策路径待核验 |
| 关键权衡 | 写入成本独立于订阅数 vs filter normalize 实现复杂度 vs JOIN planner 拒绝会读太多的查询 vs live schema changes 仅支持新表+带 default 的新列 vs Apache-2.0 vs 与 Hasura/Supabase realtime 闭源 SaaS 竞合 | 档案明示 write cost independent of subscriber count、Consistent by construction、Writes nothing to your database；治理可持续性、生产部署规模待核验 |
| 最小 PoC | 用 docker-compose 起 PostgreSQL + streamgres，写 2 个 client 订阅相同 SQL（一个 SELECT * FROM events WHERE status='open'），观察从 100→10000 订阅时单 INSERT 延迟不变；尝试带 JOIN 的 SQL 看 planner 行为 | PoC 范围、退出路径由档案"单 SQL、多订阅、可观测"建议推导；具体 stress test 场景、SLO 指标待核验 |

## 架构启发
Streamgres 的核心启发是 **「subscription-native vs query-on-demand 是两种本质不同的范式」**。传统 query-on-demand（每次 query 跑一次 SELECT）简单但浪费；subscription-native 让订阅关系 = view，写时增量路由到 affected views，写入成本与订阅数解耦。这一思路早在 Database CRDT、Materialized View、Trigger-based replication 都有痕迹，但 streamgres 把它做成 WebSocket-first + subscription-first + Apache-2.0 + 写不到你的数据库的严肃工程化承诺产品，对 realtime SaaS 是结构性选择。更深层的启发是：**「JOIN planner 拒绝会读太多的查询」是其设计纪律——不让一个 client 拖累所有 client**，这种纪律是 mature realtime system 应有的。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Clients[Client A<br/>subscribe(SELECT * FROM events WHERE status='open')<br/>Client B<br/>subscribe(SELECT * FROM events WHERE status='open')] --> Engine[Streamgres Sync Engine]
  Engine --> Views[Incrementally maintained view<br/>相同查询共享视图]
  Engine --> Planner[JOIN planner<br/>LEFT/RIGHT/INNER/EXISTS<br/>refuses too-large queries]
  Engine --> Filter[Filter normalize<br/>per-column index]
  Postgres[PostgreSQL Primary/Replica/Standby] -->|logical replication + WAL| Engine
  Engine --> Snapshot[Initial reads snapshot<br/>never ahead of LSN]
  Engine --> Delta[Delta rows added/removed<br/>pushed to affected subscriptions]
  Engine -->|每 commit| Commit[composed, write-only-then-read input]
  Snapshot --> Clients
  Views --> Clients
  Delta --> Clients
  Planner -.边界.-> Risk[Governance 可持续性<br/>未上线 SLO 生产案例<br/>Filter normalize 实现细节待核验<br/>与 Hasura/Supabase realtime 竞合]
  Filter -.边界.-> Risk
```

## 定位判断
**基础设施候选项目（PostgreSQL realtime 订阅引擎）。** streamgres 有潜力成为 PostgreSQL 生态的 realtime 严肃工程化层——类似 Hasura 但 Apache-2.0 + 写不到你的数据库。决定其后续价值的是生产部署案例、SLA/SLO、与 PostgreSQL 主版本的兼容性。

## 风险 / 局限 / 泡沫点
- **JOIN planner 拒绝会读太多的查询:** 部分 SQL 模式不支持，可能限制 SaaS 应用
- **live schema changes 仅限新表+带 default 的新列:** 其他改动停机报错特定类型，运维复杂度
- **与闭源 SaaS 竞争:** Hasura/Supabase realtime 有完整生态，streamgres 商业化难度大
- **PostgreSQL 版本绑定:** WAL 位置快照机制依赖具体 PG 版本
- **生产部署案例缺:** 3 days 365⭐ ⑂11 fork/star 3.0% 主要来自 README 内容，未见规模化生产采用
- **过滤性能边界:** filter normalize 在高 cardinality 列（多不同值）的极限性能待验证

## 与同类项目的关系
- **vs Hasura GraphQL:** Hasura 闭源 SaaS + GraphQL；streamgres 开源 + Apache-2.0 + SQL-first
- **vs Supabase realtime:** Supabase 闭源 + integrated；streamgres 纯 engine + Apache-2.0
- **vs Materialized view:** 那是查询时刷新；streamgres 是 commit 时增量
- **vs LISTEN/NOTIFY + 轮询:** 简单但高延迟；streamgres 是 commit 触发 + delta
- **vs Electric SQL:** Electric 是 active-active sync；streamgres 是 subscription-native
- **vs PowerSync:** PowerSync 是 mobile-first sync engine；streamgres 是 server-first

## 是否值得持续跟踪
**值得持续跟踪（PostgreSQL realtime 严肃工程化层）。** Streamgres 代表了 **「subscription-native 同步引擎 + Apache-2.0 + 数据不出库」** 的严肃工程化承诺，无论其本身成败，这一方向是行业趋势。建议关注：生产部署案例、SLA/SLO、与 PostgreSQL 主版本兼容、与 Hasura/Supabase realtime 闭源 SaaS 竞争。对 PostgreSQL 实时数据需求，这是严肃工程化参考实现。

## 后续观察点
- 生产部署案例（哪家 SaaS / agent / dashboard 在用）
- SLA / SLO / 性能 benchmark 发布
- 与 PostgreSQL 主版本兼容性矩阵
- 与 Hasura/Supabase realtime 闭源 SaaS 的市场博弈
- 商业化路径（Juspay 内部用？开源 SaaS？企业版？）
- GOVERNANCE：juspay 团队是否引入更多 maintainer
- 是否推出 multi-region / cross-DC replication 能力
- 是否支持其他 database（MySQL、MongoDB 等）

---
> 数据来源: GitHub API (2026-10-10) | Stars: 365 | Forks: 11 | License: Apache-2.0 | 语言: Rust | 创建: 2026-10-07 | 治理: juspay 团队
