---
title: "NyxFoundation/nyxis"
slug: nyxis
date_added: "2026-10-28"
last_seen_date: "2026-10-28"
category: "基础设施候选"
emoji: "🛡️"
stars: "297 stars"
stars_delta: "41.8 小时 297⭐ ⑂11（fork/star 3.7%）· 快照 2026-10-27T22:16:31Z"
language: "Lean"
score: 93
tags: ["nyxis", "lean4", "formal-verification", "cedar-policy", "authorization", "supabase", "postgres", "assumptions-boundary", "four-colour-boundary-diagram", "axiom-audit-macro", "three-axioms-only", "no-sorry-allowed", "proof-catalog", "connection-code-split", "unproven-in-red", "integration-test-not-a-proof", "mit", "single-author", "two-commits", "nix-foundation"]
url: "https://github.com/NyxFoundation/nyxis"
---

# NyxFoundation/nyxis

## 一句话定位

开发者只需写 Cedar schema 与 policies，**永远不必写 Lean**；而每一个建在 Nyxis 上的后端，都自带一份关于授权安全的**形式证明**——主定理断言「任何 HTTP 请求序列都不能让已认证主体读写或授予超出其正当权限的数据」，且这个结论由 Lean 内核在**每次 `lake build`** 时裁决。

## 它解决的问题

**它要解决的是「授权逻辑的正确性无法被证明」这个问题。**

绝大多数后端框架的权限检查是运行时的一段代码：你写 `if (user.isAdmin) { ... }`，然后靠测试、靠 code review、靠「后来没出过事」来保证它是对的。**⭐ 而这三种保证都有同一个共同弱点——它们只能发现「有人想到过的错误路径」。**

Nyxis 的做法是把权限检查从「运行时的一段手写代码」变成「**从 Cedar policy 编译出来的、被 Lean 证明过的授权层**」：授权决策在纯模型层里被完全定义与证明，连接代码只负责「把 HTTP 请求翻译成授权层的调用」，而**翻译过程中可能出错的地方被显式标红并写进假设**。

**⭐⭐ 而它最独特的贡献是：它把「我证明到哪里为止」当成产品的一部分来做。**

## 为什么值得关注（2026-10-28）

**⭐⭐⭐ 因为它是本日唯一一个「技术严谨度」与「边界声明完整度」同时达到本日报所见最高水平的项目——而它只有 2 个 commit、1 个贡献者。**

四个可核验的硬事实：

1. **⭐⭐⭐⭐⭐ `ASSUMPTIONS.md` 把证明边界画成了一张四色图**

   | 颜色 | 含义 | 本日报核对到的实例 |
   |---|---|---|
   | 🟢 绿 | **纯模型内已证** | 从路由到授权层对每个 action 的判定（`exactly cedar-spec's Cedar.Spec.isAuthorized`）、effect 签发、状态转移、列表、级联、外部效果记录，直到传给 handler 的值 |
   | 🔵 蓝 | **连接代码，已证** | 由成功认证构造主体的接线（`HttpAuth`）；把生成值固定、组装请求、在**一个事务内**分阶段执行、构建响应；签发出的 SQL 全部来自已授权操作；外部效果只对已记录内容发送；响应可由请求与阶段结果序列重放（`ReadSafety.replay_runHandler`） |
   | 🔴 红 | **连接代码，未证 → 作为 Assumption 1 被信任** | 原始 HTTP 解码、body task 与发送；JWKS 获取 / 签名验证 / 时钟 / 随机数的内部实现；**加载判定材料**（点查与 `SELECT ... WHERE` 的结果就是数据库当前行，且已取全判定所需行）；PostgreSQL 实际执行 SQL 的语义 / 隔离 / 持久化；JSON 解析器；启动 curl 并解析其响应；outbox 写入与内部循环重试；CORS 装饰后的响应 |
   | 🟡 黄 | **外部世界与人 → Assumption 1–3** | Lean 工具链与固定版本的依赖、FFI 与原生库、密码学实现正确性（Assumption 1）；Supabase Auth JWKS / TLS / PostgreSQL / Storage / SMTP / 外部 API 的行为（Assumption 2）；**被人类批准的那两份文件**（schema 与 policies）、应用 handler 代码、secrets 与云端设置、运维者的正确使用（Assumption 3） |

2. **⭐⭐⭐⭐⭐ 三条假设各按四段写 —— 这四段本身就是本日报今日最值得单独记的一条文档规范**

   > Each of the three items is written in four parts: **the assumption (what is trusted), what happens if it is broken, how developers uphold it, and checks** (the supporting condition IDs and checks). **These do not prove that the assumption holds, and a passing integration test is never a substitute for a formal proof.**

3. **⭐⭐⭐⭐⭐⭐ `Test/Axioms.lean` 用一个宏遍历命名空间下的每一个定理，而不是手工维护名单**

   它定义 `#assert_axioms_under ns`：遍历环境里命名空间 `ns` 下的**每一个**定理（包含 private 定理），逐个 `collectAxioms`，凡不在允许名单 `["propext", "Classical.choice", "Quot.sound"]` 里就 `throwError`。宏的说明原文：

   > 列挙を手で保守しないため、補助定理の追加・削除で検査が漏れない。

   **⭐⭐⭐⭐⭐⭐⭐ 「不手工维护名单，所以辅助定理的增删不会漏检」—— 这是本日报见过最正确的自检写法之一：它把「检查的覆盖面」本身做成了可增长的，而不是靠人记得补。** 且说明里明确写着：**未证明的洞或自定义公理一旦混入，构建就会失败（并报告不被允许的公理名）。**

4. **⭐⭐⭐⭐⭐ `docs/proofs.md` 的定理目录每一行都有第四列「述べないこと」**

   即「我没证明什么」与「我证明了什么」在同一张表里。**⭐⭐⭐⭐⭐⭐⭐⭐ 这是本日报连续多日记录的「边界要写进可核验位置」的最高完成度形态：主定理、假设、连接代码的责任划分、定理目录、集成检查脚本，全部在同一套命名下对齐。**

**⭐⭐⭐⭐⭐⭐⭐ 而它同时留下了一条本日最值得记的治理缺口：**

> **This document is maintained by humans, and any change to it, including adding, removing, or restructuring assumptions, is made at human discretion.**

**⭐⭐ 假设是可以被人改的 —— 于是「谁改、什么时候改、基于什么」就成了这个体系里真正的治理问题。** 而本日唯一一条外部 issue（#33，日文供应链尽调问卷）问的恰恰是这件事。**一个把证明边界写得极其严谨的系统，在治理层面留下的空白恰恰是最容易被攻击的地方。**

## 热度来源判断

**热度主要来自「形式化验证」这个话题本身的可见度，而非可核验的采用。**

- **⭐⭐⭐ 本日报可核验的采用信号几乎为零**：`subscribers_count` = **3**、`contributors` = **1 人**、`releases` 2 个且**均 0 asset**（无二进制分发）、topics 为空数组、**仅 2 个 commit**。
- **⭐⭐⭐ 而 33 个 open issue 的构成更说明问题**：已核验的 issue 里，#32–#26 是一批**作者自建 issue 式的工程待办**（`feat(theorem): state the record kind behind a signed URL`、`docs: align the theorem readings and docstrings with the definitions`、`fix(mail): keep message lines within the RFC limits`、`fix(outbox): decide async deliveries by status, discarding the body`、`fix(calls): allow spaces inside auth: header secret values`、`fix(cors): allow the handler request headers and expose ETag/Location`、`fix(postgres): store only canonical sets and records`、`fix(schema): make action group ancestors transitive`）；#17–#21 是一批 Linux/Windows 构建与运行故障；#16 是一条**真实缺陷报告**（`Schema parser accepts /* */ block comments, which Cedar's schema syntax does not have`）；而**唯一的外部 issue 是 #33 —— 一份日文的企业供应链尽调问卷**（提问者 `umayado17`，主题为「研究助成与 Nyxis 开发/发布治理」，明确提到 Nyx Foundation 曾获 Fenbushi Capital 研究助成，并列出 4 个待答问题：助成的合同/受领主体与期间、助成附带权利、成果与源码的发布权、以及维护承诺）。
  **⭐⭐⭐⭐⭐⭐⭐ 而这批 issue 本身就是本日报今日关于 nyxis 最有价值的一条观察：33 个 issue 里绝大多数是作者自己开的工程待办与平台兼容性故障，而唯一的「外部用户」是一份尽调问卷 —— 它说明这个项目当前的关注者主要是评估者而不是使用者。**
- **⭐⭐⭐⭐⭐⭐⭐ 账号背景可核验**：`NyxFoundation` 是 Organization，创建于 2025-07-15，57 个公开仓库、43 followers。
- **⭐⭐ 而 297⭐ 在 41.8 小时里的分布无法核验** —— `stargazers` 端点对本 token 持续返回 **404**，因此本日报**不能**声称这 297⭐ 来自真实使用者。**⭐⭐ 397⭐ 而 subs 3 的巨大落差，本身就是「star ≠ 关注」的又一个样本。**

## 关键技术亮点

1. **⭐⭐⭐⭐⭐ 主定理说的是一件具体的事，而不是一句「安全」**

   > No sequence of HTTP requests can cause an authenticated principal to read, modify, delete, or grant access to data beyond its legitimate permissions.

   **⭐⭐⭐⭐⭐ 注意它的量词：「任何请求**序列**」而不是「任何请求」—— 即它证明的是「多步操作组合起来也不会越权」，这正是单步检查最容易漏掉的一类 bug。**

2. **⭐⭐⭐⭐⭐ 授权层的定义精确到「与官方规范完全一致」**

   授权判定被定义为 `exactly cedar-spec's Cedar.Spec.isAuthorized` —— 即证明对象不只是「某个授权函数」，而是**官方 Cedar 规范里的那个函数**。**⭐⭐⭐ 这意味着 Cedar 本身的语义变更会直接反映到证明上。**

3. **⭐⭐⭐⭐⭐ 「What the theorem does not state」逐条列出保证之外的东西**

   已核验条目包括：HTTP/JWT/SQL 的对应关系；生成值的唯一性与时钟正确性；签名 URL 的内容与 Storage 的行为；邮件与异步外部 API 的投递；**「COMMIT 失败之后已发出的同步调用在目标端产生的副作用」**；服务主体的 ID 与配置；**「unconditional noninterference, including observation of permit and deny」**（即**它不保证「拒绝」本身不可被观察** —— 一个 permit 与一个 deny 的可区分性 leaking 明确落在保证之外）；**以及「附件内容直接在客户端与 Storage 之间传递，不经过 Nyxis，因此内容检查、病毒扫描与大小限制是 Storage 与应用的责任，并在保证之外」**。

   **⭐⭐⭐⭐⭐⭐⭐⭐ 一个安全证明最有价值的部分，往往是它明确不覆盖的那几行。**

4. **⭐⭐⭐⭐ 34 个集成检查脚本与证明目录一一对应**

   `scripts/` 下 34 个检查脚本（`check-approved-binding.py` / `check-approved-declaration.py` / `check-core-isolation.py` / `check-cors.py` / `check-external-calls.py` / `check-handler-effects.sh` / `check-http-headers.py` / `check-http.sh` / `check-installed-jwt.sh` / `check-jwt-dependency.sh` / `check-local-postgres-http.py` / `check-local-supabase.py` / `check-materials-scale.py` / `check-outbox.py` / `check-postgres-http.py` / `check-postgres-lifetime.py` / `check-postgres-values.py` / `check-pq-patch.py` / `check-sample-init.py` / `check-sample-jwks.py` / `check-sample-jwt-db.py` / `check-sample-startup.py` / `check-schema-rejection.sh` / `check-team-docs.py` + `prepare-dependencies.py` + `local-supabase.py` + `nyxis_local.py` + `run-sample-frontend-backend.py`）。

   **⭐⭐⭐⭐⭐⭐ 而其中三个最值得抄走：`check-approved-declaration.py`（校验「声明了什么」）、`check-core-isolation.py`（校验「核心是否被绕过」）、`check-handler-effects.sh`（校验「效果是不是被记录」）—— 三者对应的都是「绕过路径」，而不是「正常路径」。**

5. **⭐⭐⭐ 工程规模可核验**

   全树 **261 个条目（`truncated: false`）**，其中 `Nyxis/` 43 项、`Test/` 33 项、`.lean` 文件 **102** 个。依赖 Lean 4（`lean-toolchain` 固定 `leanprover/lean4:v4.34.1`）、cedar-lean、batteries、lean-pq、lean-jose 等，经 `scripts/dependencies.py`（`prepare-dependencies.py`）按 SHA256 固定拉取。运行时需 PostgreSQL（Supabase）+ Supabase Auth。

6. **⭐⭐ 两个官方样例，且形态不同**

   `examples/bulletin-board/`（含 `BulletinBoard.lean` / `Approved.lean` / `Handlers.lean` / `Server.lean` + `Test/` 4 个测试文件 + **Next.js frontend**）与 `examples/team-docs/`（**仅后端**）。**⭐⭐ 一个带前端的完整应用 + 一个纯后端，说明它想同时覆盖「有 UI 的后端」与「作为服务的后端」两种形态。**

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | **四层边界**：① **纯模型层**（`Nyxis/` 43 项：路由 / Cedar 解析 / 授权层 / 运行时 / 连接代码 / 证明）② **连接代码层**（`Nyxis.Internal.*`：HTTP / JWT / JWKS / Postgres / CORS / StorageSign / MailSend / CallSend / Outbox / Jobs）③ **信任边界层**（`ASSUMPTIONS.md` 的 Assumption 1–3 + `docs/proofs.md` 的「述べないこと」列）④ **工具边界层**（`scripts/` 34 个检查脚本 + `Test/Axioms.lean` 的公理审计 + `examples/` 两个官方样例）。**边界划在「连接代码中未被证明的部分」**，且被显式标红。**⭐ 关键的架构判断：边界不是画在「模块之间」，而是画在「哪些代码被 Lean 检查过」这条线上 —— 这条线会穿过模块内部。** | `ASSUMPTIONS.md` 四色 Mermaid 图与三条假设的四段结构、`docs/proofs.md` 的四列表格、`Test/Axioms.lean` 的 `allowed` 名单与 `#assert_axioms_under` 宏、34 个 `scripts/check-*.py` 文件名清单、261 条树（`truncated: false`）。**⭐ 未核验：nyxis 的 `docs/proofs.md` 中每条定理的具体 Lean 原文（仅读表头与部分行）、`Nyxis/` 43 个条目的具体职责划分、`scripts/` 34 个检查脚本的实现** |
| 主路径 | 写 Cedar schema（`entity User = {...}`）+ policies（`@id("manage-post") permit (...) when { resource.author == principal \|\| principal.admin }`）→ 写 handler（类型 `Nyxis.Handler`，**其唯一效果是调用授权层的 action，不能做 IO、不能直接碰数据库**）→ `lake build`（**同时绑定应用源码、审计应用代码、检查证明**）→ 客户端用 Supabase Auth 的 JWT 走 HTTP 调用；前端在 Nyxis 之外，作为普通 HTTP 客户端。**⭐⭐ 注意「lake build 同时做三件事」这一点 —— 它把证明、应用绑定、应用审计合并成一次构建，而不是三套独立流程。** | README 的 "How it works" 四步与官方样例节、`policies.cedar` / `schema.cedarschema` 的文件存在性、`examples/bulletin-board/` 的文件清单。**⭐ 未核验：nyxis 的 `lake build` 实际耗时与样例是否能跑通（需 Lean 4.34.1 + 本地 Supabase）** |
| 关键权衡 | **⭐ 证明 vs 文档**（两者都做，因此体量与门槛都高）· **⭐ 边界写进文档 vs 写进可执行检查**（两者都做：文档给四色图，检查给 34 个脚本 + 公理审计宏）· **⭐⭐⭐ 公理白名单 vs 手工核查**（用 `#assert_axioms_under` 遍历命名空间，**覆盖率不靠人记得补**）· **⭐ 定理目录 vs 单个定理**（`docs/proofs.md` 给出逐条的「述べる / 述べない」两列，**代价是需要人工同步 Lean 源码与文档表**）· **⭐⭐⭐ 治理 vs 技术**（明写假设「由人裁量修改」—— **⭐ 技术上严谨的系统，治理上留了空白**，而 issue #33 恰好在问这件事）· **⭐ 红灯区 vs 缩小红灯区**（把「连接代码未证」全部标红而非声称已证，**代价是保证强度低于宣称全面验证的系统**） | 三份 README 原文、`ASSUMPTIONS.md` 的假设段落与图例、`docs/proofs.md` 的表头与连接代码段落、issue 列表（33 条已核验全部标题与 #33 正文前 700 字符）。**未明示：三个项目都没有说明「谁负责长期维护、谁付钱、出问题找谁」—— nyxis 的 #33 恰好在问这件事且本日报未取得回复** |
| 最小 PoC | 1. **⭐⭐ nyxis：先读 `ASSUMPTIONS.md` 的四色图与三条假设（四段结构），再读 `docs/proofs.md` 的「述べないこと」列** —— **这一步是唯一能判断「它证明了什么」的动作，且不需要装任何东西** → 2. ⭐ `grep -rn "sorry" <clone>/Test/` 与 `lake build`（**观察 `Test/Axioms.lean` 是否真的在编译期拒绝越界公理**）→ 3. ⭐⭐ 跑 `examples/bulletin-board/`，**在 UI 里用一个非管理员账号试着编辑别人的帖子，确认被 Cedar 策略拒绝**（**这一步才是证明的价值所在：它对应一个你能亲眼看到的拒绝**）→ 4. ⭐ 读 `scripts/check-*.py` 的文件名清单，对照自己项目的安全检查，**挑 3 个抄走**（推荐 `check-approved-declaration.py` / `check-core-isolation.py` / `check-handler-effects.sh`）→ 5. **⭐⭐⭐ 读 `ASSUMPTIONS.md` 末尾那句「This document is maintained by humans … at human discretion」，然后问自己：「如果这个项目明天被收购，假设会怎么变？」** | **第 3 步是 nyxis 唯一能证伪其价值的步骤**（证明好 ≠ 策略对）· **第 1 步是唯一能在不装任何东西的情况下判断其可信度的步骤** · **第 5 步是本 PoC 真正的产出** · **本 PoC 不覆盖**：真实 PostgreSQL/Supabase 部署（需本地 Supabase）、`lake build` 的实际耗时（需 Lean 4.34.1 + 24 GB 依赖下载） |

## 架构启发

**⭐⭐⭐⭐⭐ 核心启发：「证明到哪里为止」必须和「证明了什么」用同一套文档结构表达，而不是分两个地方写。**

`ASSUMPTIONS.md` 的四色图把「已被 Lean 检查的代码」与「未被检查的代码」在同一张图上区分；`docs/proofs.md` 把每条定理的「述べる」与「述べない」放在同一行。**⭐⭐⭐ 这两处的共同点是：读者不需要在两个文档之间来回切换才能知道自己站在哪里。**

**⭐⭐⭐⭐⭐⭐ 第二个启发（本日最可迁移的一条）：用宏遍历命名空间来保证「检查的覆盖面」不靠人记得补。**

`#assert_axioms_under` 的价值不在于它检查了什么，而在于**它检查的是「命名空间里的全部定理」这个集合本身** —— 新增一个辅助定理，它自动进入检查范围；删除一个，也自动退出。**⭐⭐⭐⭐⭐⭐ 这与「维护一份白名单」的常见做法相比，把「覆盖面」从人的记忆负担变成了代码的不变量。** 这个模式可以直接套用到任何做静态检查的项目：lint 规则集、审计脚本清单、测试用例清单、证明辅助定理清单。

**⭐⭐⭐⭐⭐ 第三个启发：「集成测试通过永远不是形式证明的替代品」这句话应该写进代码库本身，而不是只写在文档里。**

它写在 `ASSUMPTIONS.md` 里，而**真正把它变成不变量的是那条构建期的公理审计** —— 即文档承诺与构建行为是对齐的。**⭐⭐⭐⭐⭐ 文档与实现对齐，本质上是「写下来就意味着要兑现」。**

**⭐⭐⭐⭐ 第四个启发：把「保证不覆盖的东西」写得比「保证覆盖的东西」更细。**

「What the theorem does not state」这一节里有「permit 与 deny 的可区分性 leaking 明确在保证之外」「附件内容不经 Nyxis 故病毒扫描在保证之外」这样的具体条目。**⭐⭐⭐⭐ 抽象地说「本框架不保证绝对安全」是没有价值的，而具体地说出「哪一类攻击仍然可行」才是可用的。**

**⭐⭐⭐ 第五个启发（本档案最想记的一条）：技术上最严谨的系统，往往在治理上留有最大的空白。**

假设文档由人裁量修改 —— 这意味着**证明的强度最终由「谁能改假设」决定，而不是由证明本身决定**。**⭐⭐⭐ 而 issue #33 恰好在问这件事（谁有权批准、合同主体是谁、维护承诺是什么），且在本日快照时未取得作者回复。** 这是一条本日可核验的、具体的治理缺口。

**⭐⭐ 架构对比：** 与 `AxiomMath/CFSG`（本日同期另一位 key_project）构成**同一语言、同一领域、完成度差异极大**的一对。**⭐⭐⭐ 一个把边界写全了（红/黄两层 + 四段式假设 + 定理目录 + 34 个检查脚本），另一个只写了证明与对照机制（无 `docs/`、无 CI）。** **⭐⭐⭐⭐⭐ 这组对比的价值在于：它证明「形式化实践」的差异点**不在「有没有做形式化」**，而在「有没有写清楚自己没做什么」。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart TB
  Client[客户端<br/>Supabase Auth JWT 或普通 HTTP 客户端] --> HTTP[连接代码层 Nyxis.Internal<br/>HTTP 解码 body task 与发送 待核验实现<br/>JWKS 获取 签名验证 时钟 随机数<br/>JSON 解析器 curl 启动与响应解析<br/>CORS 装饰 全部标红 未被证明]

  HTTP --> Auth[主体构造 HttpAuth<br/>已证 蓝色]
  HTTP --> Model[纯模型层 Nyxis<br/>路由 Cedar 解析 授权层 运行时<br/>绿色 已被 Lean 检查]

  Model --> Cedar[Cedar 授权判定<br/>exactly cedar-spec Cedar.Spec.isAuthorized<br/>Effect 签发 状态转移 列表 级联<br/>外部效果记录 直到传给 handler 的值]
  Model --> Handler[Nyxis.Handler<br/>唯一效果是调用授权层的 action<br/>不能做 IO 不能直接碰数据库<br/>check-core-isolation.py 校验]

  Cedar --> Main[主定理 Nyxis.Runtime.authorization_safety<br/>No sequence of HTTP requests can cause<br/>an authenticated principal to read modify delete<br/>or grant access beyond its legitimate permissions<br/>量词是请求序列 而非单个请求]
  Cedar --> SQL[签发出的 SQL 全部来自已授权操作<br/>一个事务内分阶段执行<br/>读取判定材料 点查与 SELECT WHERE<br/>取全判定所需行]

  SQL --> PG[(PostgreSQL Supabase<br/>实际执行语义 隔离 持久化<br/>标红 未被证明]
  SQL --> External[外部效果<br/>只对已记录内容发送<br/>Outbox 写入与内部循环重试<br/>StorageSign MailSend CallSend]

  Axioms[Test/Axioms.lean<br/>assert_axioms_under 宏<br/>遍历命名空间下每一个定理 含 private<br/>逐个 collectAxioms<br/>名单 propext Classical.choice Quot.sound<br/>不手工维护名单 因此新增辅助定理不漏检<br/>越界即构建失败并报告公理名] --> Main
  Checks[scripts 34 个检查脚本<br/>check-approved-declaration<br/>check-core-isolation<br/>check-handler-effects<br/>check-cors check-outbox check-postgres-values 等] --> Model

  Boundary[信任边界层 ASSUMPTIONS.md<br/>绿 纯模型内已证<br/>蓝 连接代码已证<br/>红 连接代码未证 作为 Assumption 1 被信任<br/>黄 外部世界与人 Assumption 1-3<br/>三条假设各四段<br/>信什么 破了会怎样 如何维持 支撑检查<br/>These do not prove that the assumption holds<br/>and a passing integration test is never a substitute<br/>for a formal proof] --> Main

  NotStated[What the theorem does not state<br/>HTTP JWT SQL 的对应关系<br/>生成值唯一性与时钟正确性<br/>签名 URL 内容与 Storage 行为<br/>邮件与异步外部 API 投递<br/>COMMIT 失败后已发出的同步调用的副作用<br/>服务主体 ID 与配置<br/>unconditional noninterference<br/>including observation of permit and deny<br/>附件内容不经 Nyxis<br/>故病毒扫描与大小限制在保证之外] --> Main

  Governance[治理层<br/>This document is maintained by humans<br/>and any change to it including adding removing<br/>or restructuring assumptions<br/>is made at human discretion<br/>issue 33 供应链尽调问卷 在快照时未取得回复] -.边界.-> Boundary

  Proofs[docs/proofs.md<br/>逐条定理的目录<br/>四列 定理 文件 述べる 述べない<br/>保证与不保证在同一张表里] --> Main
  Build[lake build<br/>同时做三件事<br/>绑定应用源码 审计应用代码 检查证明<br/>耗时未核验] --> Axioms
```

## 定位判断

**形式化验证驱动的后端框架 —— 准确地说，是「授权层可证明」这一特定主张的框架，而不是通用形式化框架。**

⭐⭐⭐⭐ 它在生态中的位置非常独特：**它不试图证明整个系统正确，只证明一件最容易出安全事故的事（授权），并把其余部分诚实地划出去。** 这比「全系统形式化」务实得多，也比「纯运行时检查」强得多。

**⭐⭐⭐⭐⭐ 而它的形态判断是「基础设施候选」而非「生产可用」**，依据是可核验的：README 首屏徽章写 `status: under development`；v0.1.1（快照时最新 release，2026-10-26T08:56:02Z，0 个 asset）；仅 2 个 commit；contributors 1 人；releases 无二进制分发。

**⭐⭐⭐⭐⭐⭐ 文档形态也是一项值得记录的事实**：README 明写「Apart from the README and ASSUMPTIONS, documentation is currently written in Japanese」；`ASSUMPTIONS.md` 是英译，且**日文版为权威版本，项目检查跑的是日文版**。**⭐⭐ 这对日语社区是优势，对英语社区是门槛 —— 而本日报不认为这属于缺陷，它更像是「项目由谁维护」的诚实反映。**

## 风险 / 局限 / 泡沫点

- **⚠️⚠️⚠️ 治理空白是本项目最实质的风险。** 「假设由人裁量修改」+ issue #33（尽调问卷）在快照时未取得回复 —— **一个授权安全框架的信任根，落在「谁能改假设」这个未公开的治理安排上。**
- **⚠️⚠️⚠️ 采用信号几乎为零。** `subs 3`、`contributors 1 人`、`releases` 无 asset、**33 个 open issue 里唯一的外部 issue 是一份尽调问卷** —— **这说明它当前被评估，而不是被使用。**
- **⚠️⚠️ 门槛极高。** 需要 Lean 4.34.1（需下载按 SHA256 固定的依赖）、本地 Supabase、PostgreSQL、Cedar schema/policies 编写能力。**⭐⭐ 而对多数团队来说，「用 Cedar 直接写策略」本身就是一门新学问。**
- **⚠️⚠️ 依赖版本被钉死在 2025 年的 Lean 4.34.1，而同日的 `AxiomMath/CFSG` 用的是 Lean 4.35.0-rc3** —— **⭐⭐ 即 nyxis 用的是较旧的稳定版，而更新的版本仍在 rc。** 这本身是合理选择（稳定优先），但**它意味着证明要在工具链升级后重新验证**。
- **⚠️⚠️ 保证不覆盖的项里有几条是实践中最常出事的**：permit/deny 的可区分性 leaking、附件内容的病毒扫描与大小限制、COMMIT 失败后的外部副作用。**⭐⭐ 换句话说，「用了 Nyxis 就安全了」是错误的读法。**
- **⚠️⚠️ Linux/Windows 构建摩擦已被自己的 issue 记录**：#17–#21 覆盖了 `lake build` 在 Linux 上 `-L<system libdir>` 覆盖 Lean sysroot、Linux 上找不到 `libcrypto_shim.so`、`prepare-dependencies.py` 在 Windows 上的 locale 解码与 CRLF checkout 失败、Linux/WSL2 下跑本地 Supabase 检查、Windows checkout 准备依赖。**⭐⭐ 即跨平台可用性尚未打通。**
- **⚠️ 仅 2 个 commit、1 个作者 —— bus factor 为 1。**
- **⚠️ 本日报无法核验 297⭐ 的来源**（`stargazers` 端点 404），**因此不能排除其中相当部分来自非真实使用者**。
- **⚠️ 本日报未运行 `lake build`，未核验证明是否真的编译通过。**

## 与同类项目的关系

- **⭐⭐⭐ vs `AxiomMath/CFSG`（本日同期另一位 key_project）**：**同语言（Lean 4）、同领域（形式化验证）、完成度差异极大。** CFSG 有真证明（5.8 GB、24 小时构建）但**没有 `docs/`、没有 CI、没有任何「我没证明什么」的说明**；nyxis 的证明规模小得多（1274 KB），**但有四色图、四段式假设、定理目录与 34 个检查脚本**。**⭐⭐⭐⭐⭐ 这组对比是本日最可迁移的一条：「形式化实践」的成熟度差异不在证明难度，而在边界声明。**
- **⭐⭐⭐ vs Cedar 生态本身（`cedar-policy/cedar`）**：**不是竞品，是被证明的对象。** Cedar 是策略语言与授权库，nyxis 是**把 Cedar 语义编译进 Lean 并证明其判定正确性**的那一层。**⭐⭐ 而 Cedar 生态的其余部分（各类 policy engine）都停在「运行时判定」。**
- **⭐⭐ vs 传统 Zanzibar / OPA / Permify 类方案**：**⭐⭐⭐ 三者都在「运行时判定」，nyxis 在「编译期 + 证明期」判定。** 它的代价是构建门槛与策略语言的学习成本；收益是「越权」这一类 bug 在构建期就被排除，而不是上线后被发现。
- **⭐⭐ vs 各家云厂商的「权限保证」承诺**：**⭐⭐ 云厂商的 IAM 通常提供的是「策略可审计」与「策略变更可追溯」，而不是「策略语义被形式证明」。** **nyxis 走的是另一条路：把策略语义交给一个数学对象。**
- **⭐ vs 自建形式化安全项目的组织（如 Trail of Bits 的 Trailmark 系工作）**：**⭐⭐ Trailmark 是「帮 agent 找到调用点」的分析工具，nyxis 是「把授权层做进类型系统」；两者都是「把安全判断从运行时挪到更早」这个方向的不同实例。**

## 是否值得持续跟踪

**值得 —— 但它的价值主要在于「可借鉴的方法」而不是「可立即采用的产品」。**

- **⭐⭐⭐ 理由一：它是本日报见过最完整的「证明边界声明」实践，可直接抄。** 四色图、四段式假设、「述べないこと」列、`#assert_axioms_under` 宏 —— **⭐⭐⭐⭐⭐ 这四件东西可以直接用在任何「我做了什么保证」的项目上，而与 Lean 无关。**
- **⭐⭐⭐ 理由二：它证明了「形式化验证」在 2026 年可以以「一个可安装的框架」而非「一篇论文」的形态存在** —— 且它选择证明最容易出安全事故的那一件事（授权）而非最难证明的那一件事（全部正确性）。**⭐⭐ 这个取舍比它证明的内容更值得学。**
- **⭐⭐⭐ 理由三：它的 33 个 issue 是一份极有价值的需求清单** —— #32–#26 那批自建待办（`state the record kind behind a signed URL`、`make action group ancestors transitive`、`keep message lines within the RFC limits`）**直接暴露了一个「可证明的系统」在工程上会遇到什么**，对任何想走这条路的人都有参考价值。
- **⭐⭐ 使用建议**：**在它成熟之前，把它的 `ASSUMPTIONS.md` 模板与 `Test/Axioms.lean` 的宏当作模板抄走，而不是把它当作依赖引入。**

## 后续观察点

1. **⭐⭐⭐ issue #33 的四个问题（助成的合同/受领主体与期间、助成附带权利、源码发布权、维护承诺）是否得到作者回复** —— **⭐⭐ 这是本项目治理缺口的唯一公开检验点。**
2. **⭐⭐⭐ `lake build` 的实际耗时是否可接受**（本日报未核验）—— **⭐⭐ 这决定它是「可日常运行的构建产物」还是「一年跑一次的证明」。**
3. **⭐⭐⭐ 第一个真实的、非尽调性质的外部 issue 何时出现** —— **⭐⭐ 这决定它从「被评估的项目」变成「被使用的项目」的时间点。**
4. **⭐⭐ `releases` 是否开始附带二进制或依赖缓存**（当前 2 个 release 均 0 asset）—— **⭐ 这决定安装门槛能否下降。**
5. **⭐⭐ 文档主体是否从日文转向双语**（`ASSUMPTIONS.md` 的英译版与日文版权威的分工是否长期维持）—— **⭐ 这决定英语社区能否成为用户群。**
6. **⭐⭐ `docs/proofs.md` 的「述べないこと」列是否会随代码演进持续更新** —— **⭐⭐ 这是本项目最容易腐化的一处：如果它不更新，读者会误以为保证范围比实际更大。**
7. **⭐⭐ 34 个 `scripts/check-*.py` 中是否会出现第一个被外部贡献者新增的** —— **⭐ 这是它从「单作者作品」转向「有社区」的第一个可核验信号。**
8. **⭐ Cedar 上游语义变更时，本项目的证明是否需要重做** —— **⭐⭐ 这决定它能否跟上上游。**

---
> 数据来源: GitHub REST/Search API（gh CLI 认证），UTC **2026-10-27T22:16:31Z** 单一快照 | Stars: 297 | Forks: 11 | Subscribers: 3 | Open Issues: 33 | License: MIT | 语言: Lean | 创建: 2026-10-26T04:26:18Z | pushed: 2026-10-26T08:55:57Z | 2 commits | contributors 1 人 | releases 2 个（均 0 asset）| topics 0 | 1,274 KB
> 组织背景: `NyxFoundation` 为 Organization，创建于 2025-07-15，57 个公开仓库，43 followers
> 附: `lean-toolchain` = `leanprover/lean4:v4.34.1`；全树 261 条目（`truncated: false`），`.lean` 102 个，`Nyxis/` 43，`Test/` 33，`scripts/` 34 个检查脚本
> 证据边界: `docs/proofs.md` 中每条定理的具体 Lean 原文未逐条核验（仅读表头与部分行）；`Nyxis/` 43 个条目的职责划分未逐目录核验；`scripts/` 34 个检查脚本仅核验了文件名，未读实现；`lake build` 实际耗时与两个官方样例能否跑通未验证（需 Lean 4.34.1 + 本地 Supabase）；297⭐ 的来源无法核验（`stargazers` 端点对本 token 返回 404）；issue #33 在快照时未见作者回复
