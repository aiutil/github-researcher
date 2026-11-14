---
title: "HerdBuilderEstimate/roblox-studio-mcp"
slug: roblox-studio-mcp
date_added: "2026-11-07"
last_seen_date: "2026-11-07"
category: "观察型"
emoji: "🧩"
stars: "427 stars"
stars_delta: "1 天 427⭐ ⑂260（fork/star 61%）；subs 8 · oi 0 · 快照 2026-11-06T22:00Z 区间；星数为两次快照之间的总量差，非当日新增"
language: "Python"
score: 86
tags: ["roblox-studio-mcp", "counter-example", "documentation-purpose", "readme-claims-nodejs", "language-field-python", "no-package-json", "no-typescript-source", "5-files-7kb", "starter-template", "utils-py-process-doubles-list", "config-py-docstring-starter", "4-commits-in-20-seconds", "10-mcp-tools-promised-none-implemented", "fork-interarrival-median-5s", "96-9-percent-gaps-under-10s", "260-forks-in-27m35s", "shared-gitignore-md5-e18f025c", "sibling-repos-404-utils-py", "main-py-imports-nonexistent-module", "star-band-425-427", "readme-diff-only-product-name", "no-payload-url-in-this-cluster", "telegra-ph-link-unreachable-unverified", "fork-account-age-distribution", "subscribers-as-low-noise-signal", "mit", "4-commits"]
url: "https://github.com/HerdBuilderEstimate/roblox-studio-mcp"
---

# HerdBuilderEstimate/roblox-studio-mcp

## 一句话定位

一个声称是「Roblox Studio 的 MCP server」的仓库 —— **而本日报建立这个档案的目的不是推荐它，而是为了把它作为一份可复现的「宣称与实现不一致」的反例样本保存下来。**

## 它解决的问题

（自述）让 Claude / Cursor 等 AI 助手连接 Roblox Studio：读取对象树、编辑 Lua 脚本、运行 playtest。

**这个需求本身是真实的** —— agent 操作 Roblox Studio 确实是一个有人做的方向。**本档案要记的不是需求，而是这个仓库与其宣称之间的距离。**

## 为什么值得关注（2026-11-07）

**本日它的价值在于作为反例样本：它与三个真项目、91 个载荷仓库出现在同一份 star 榜单上，而它的元数据与文件内容可以逐条证伪其宣称。**

**可核验事实（GitHub REST，2026-11-06T22:00Z 快照区间）**：

| 字段 | 值 |
|---|---|
| stars / forks / subs / oi | 427 / 260 / 8 / 0 |
| fork/star | **61%** |
| `language` 字段 | **Python** |
| `license.spdx_id` | MIT |
| 体积 | **7 KB** |
| 根树文件数 | **5** |
| commits | **4**（全部在 20 秒内） |
| contributors | 1 |
| `releases` | **0** |
| topics | 12 个 |
| owner | Account `HerdBuilderEstimate`（User） |

**⭐⭐⭐⭐⭐ 三处可直接证伪的冲突**：

**① README 自述的技术栈与仓库内容不符。** README 写：

> **Roblox Studio MCP** is a lightweight **Node.js/TypeScript** server that implements the Model Context Protocol (MCP) to bridge Roblox Studio and AI agents.
>
> | ⚡ **Fast & Lightweight** | Built with **Node.js + WebSocket**, low memory footprint |
> | 🔌 **Auto-Discovery** | Finds open Studio sessions automatically |

而根树的 5 个文件是：`.gitignore`（4,664 B）/ `LICENSE`（1,076 B）/ `README.md`（4,908 B）/ `config.py`（80 B）/ `utils.py`（104 B）—— **没有 `package.json`、没有任何 `.ts` / `.js` 文件、没有 `src/`**。GitHub 的 `language` 字段诚实地报 **Python**。

**② 代码是 starter 模板。** `utils.py` 的全部内容：

```python
"""Utility helpers for starter."""


def process(limit):
    return [item * 2 for item in range(limit)]
```

`config.py` 的全部内容：

```python
"""Configuration for starter."""

VERSION = "0.1.5"
DEBUG = True
MAX_ITEMS = 50
```

**③ README 承诺的 10 个 MCP 工具在代码里一个都不存在**：`get_object_tree` / `get_instance` / `create_script` / `update_script` / `delete_instance` / `get_properties` / `set_property` / `run_playtest` / `stop_playtest`（README 表格列了 9 个，正文提到 10 个工具名），加上「Auto-Discovery」与「Node.js + WebSocket」实现 —— **仓库里没有任何对应实现**。

**⭐⭐⭐⭐⭐ 四个 commit 全部在 20 秒内完成**：

```
2026-11-06T06:16:36Z  Initial commit
2026-11-06T06:16:53Z  Add README.md
2026-11-06T06:16:54Z  Add utils.py
2026-11-06T06:16:56Z  Add config.py
```

**⭐⭐⭐⭐⭐⭐ 最有说服力的判据是 fork 的时间分布**（`repos/{owner}/{repo}/forks` 全量 260 个）：

| 指标 | 值 |
|---|---|
| fork 总数 | 260 |
| 时间跨度 | 2026-11-06T06:54:32Z → 07:22:07Z（**27 分 35 秒**） |
| 相邻间隔中位数 | **5.0 s** |
| 最小 / 最大 | 3.0 s / 216.0 s |
| p10 / p90 | 3.0 s / 6.0 s |
| ≤10 秒的间隔占比 | **251/259 = 96.9%** |

**一个真实用户群不会让 96.9% 的相邻 fork 间隔落在 10 秒以内。**

**⭐⭐⭐⭐⭐⭐⭐⭐ 姊妹仓库的对照更能说明问题**（本日报逐个抓取核实）：

| 仓库 | stars | forks | fork/star | 体积 | commits | README 自述栈 | `language` | `main.py` 的 import | `utils.py` |
|---|---:|---:|---:|---:|---:|---|---|---|---|
| `HerdBuilderEstimate/roblox-studio-mcp` | 427 | 260 | 61% | 7 KB | 4 | Node.js/TypeScript | Python | 无 main.py | 104 B（starter） |
| `PulverizeLink/roblox-performance-tool` | 426 | **386** | **91%** | 6 KB | 4 | 原生 Windows 工具 | Python | `from utils import build` | **404 不存在** |
| `Lowbetweentrim/crypto-portfolio-tracker` | 425 | 358 | 84% | 6 KB | 4 | TypeScript（topics） | Python | `from utils import optimize` | **404 不存在** |
| `phaseboulderfetter/discord-quest-completer` | 425 | 332 | 78% | 6 KB | 4 | Python（topics） | Python | `from utils import optimize` | **404 不存在** |

**四家共用同一个 `.gitignore`** —— md5 全部为 `e18f025c87b71b9fe481f53ac6e8235d`。**docstring 也取自同一组 starter 文本**：`"""Configuration for starter."""` / `"""Small helper utilities."""` / `"""Utility helpers for starter."""` / `"""Entry point for starter."""` / `"""Entry point for toolkit."""` / `"""Entry point for service."""`。

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 而它们的 star 数落在同一条窄带上**（425 / 426 / 427），**四个仓库的 README 只是把同一段模板里的产品名换掉** —— 本日报已逐行 diff 验证：`roblox-studio-mcp` 与 `roblox-performance-tool` 的 README 差异只有标题、描述与工具表格，`telegra.ph/TRANSITION-06-17-3` 这个跳转链接在两家都存在。

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 与 91 个载荷仓库的关系也已核验**：本簇的 README **不含** `git-software.cc`（`roblox-studio-mcp` 的 URL 集合是 `img.shields.io` 徽章与 `telegra.ph`），其余三家同样不含。**即这是两个不同手法、可能不同来源的簇，而不是同一个脚本的两批输出**：一个用「投放载荷」制造注意力，一个用「宣称功能但交付空壳」制造注意力。

## 热度来源判断

**⭐⭐⭐⭐⭐ 热度来源是机器行为，且本日报可以给出可复现的判据。**

证据链：

1. **fork 间隔中位数 5.0 秒、96.9% 的间隔 ≤10 秒、260 个 fork 集中在 27 分钟内** —— 这是脚本的节奏，不是人的节奏。
2. **四个仓库 star 值相邻（425/426/427）** —— 自然增长不会产生这种聚集。
3. **四个仓库共用同一个 `.gitignore` 字节流**（md5 一致）与同一组 starter docstring。
4. **两个仓库的 `main.py` import 一个不存在的模块** —— 同一个模板的不同变体。
5. **README 逐行 diff 后只差产品名**。

**⭐⭐⭐⭐⭐ 但必须同时说明本档案不做什么**：**本日报核验的是元数据与文件内容的自洽性，不判断作者意图、不判断账号归属、不判断这些仓库是否已被 GitHub 处置。** 「机器行为」是对**时间分布**的判断，不是对**人的动机**的指控。

## 关键技术亮点

**本档案不列技术亮点，因为仓库内没有可分析的实现。**

**⭐⭐⭐⭐⭐ 但它有四条可复用的判据 —— 这才是本档案真正的产出**：

**判据一：`forks/{owner}/{repo}` 的相邻 `created_at` 间隔分布。**
- 真人形态（本日报的 `sheeridVerify`）：中位数 73 秒、跨 12.5 小时、≤10 秒占比 8.9%
- 机器形态（本例）：中位数 5 秒、跨 27 分钟、≤10 秒占比 96.9%
- **中位数与 ≤10 秒占比是最灵敏的两个数**

**判据二：`subscribers_count`。**
- 本例 8；载荷簇 7–9；`sheeridVerify` 0；`poki` 1；`vork` 4
- **噪声低但样本小，只能做方向性判断**

**判据三：README 承诺的能力 vs 代码里是否真的存在。**
- 本例 README 承诺 10 个 MCP 工具 + Auto-Discovery + Node.js/WebSocket 实现，交付 0 个

**判据四：`language` 字段 vs README 自述技术栈。**
- 本例自述 Node.js/TypeScript，字段为 Python

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | **无可识别的系统边界** —— 根树 5 个文件（.gitignore / LICENSE / README.md / config.py / utils.py），无 package.json、无 src/、无运行时入口 | 依据 `git/trees/HEAD` 全量根树（5 项）与 `contents/{path}` 逐个抓取 |
| 主路径 | **无主路径** —— README 描述的路径（Agent → MCP server → WebSocket → Roblox Studio）在仓库内没有实现文件 | 依据 README 工具表与根树比对；**本日报未运行该仓库** |
| 关键权衡 | **本档案不推测其权衡** —— 仓库内没有可供分析的取舍记录。可核验的只有「宣称 vs 实现」的距离 | 唯一的取舍记录 `README.md` 自身就是宣称文本 |
| 最小 PoC | **不适用** —— 没有可运行的实现可供 PoC。若要验证「它能否工作」，最小检查是 `contents/utils.py` 与 `contents/main.py` 的存在性与 README 工具表比对 | 本日报已执行该比对 |
| 证据边界 | **可核验**：GitHub 元数据、根树、四个源文件全文、四个 commit 的时间戳与标题、README 全文、fork 时间分布、四家 `.gitignore` 的 md5、姊妹仓库的 `main.py` import 与 `utils.py` 的 404。**未核验**：作者意图、账号归属、平台处置状态、`telegra.ph` 链接的落地内容 | **`telegra.ph/TRANSITION-06-17-3` 在本日报快照时刻从本机不可达（curl 返回 http=000），因此本日报对其性质不作任何判断** |

## 架构启发

**⭐⭐⭐⭐⭐ 启发一（本档案最重要的一条）：判据必须与被判定对象无关。**

「这个项目是不是农场」不能靠「看它像不像农场」来回答 —— 必须靠**与内容无关的元数据**回答。**本档案的四条判据没有一条需要读 README 内容之外的实现判断**：fork 间隔分布、subscribers、承诺与实现的差距、language 字段与自述的差距。**⭐⭐⭐⭐⭐ 而这四条都可以用 API 在几分钟内对任意仓库跑一遍。**

**⭐⭐⭐⭐⭐ 启发二：⭐⭐⭐⭐⭐ 「文档承诺」与「代码交付」之间的距离，是最容易被忽略的真实性指标。**

绝大多数项目的 README 都会**高估**自己的能力 —— 写「支持 A/B/C」时常常只有 A 实现了。**⭐⭐⭐⭐⭐ 但这里的差距是「承诺 10 个工具、交付 0 个，且连运行时入口都没有」—— 这是量级上的差异，不是措辞上的差异。** 这个区分很重要：日常项目的高估是噪声，而这个是信号。

**⭐⭐⭐⭐⭐ 启发三：⭐⭐⭐⭐⭐ 同一批仓库里「fork 间隔」比「fork 数」信息量高一个数量级。**

`sheeridVerify` 有 358 个 fork —— **数量上比本例的 260 还多**，按数量排序它会排在农场前面。**但它的间隔中位数是 73 秒、账号年龄跨越 11 年。** **⭐⭐⭐⭐⭐ 这直接证明了：任何按 fork 数排序的榜单都是错的。**

**⭐⭐⭐⭐⭐ 启发四：⭐⭐⭐⭐⭐ 「共用同一个 `.gitignore` 的 md5」是一条比读 README 更快的同源检测。**

四个仓库的 `.gitignore` 字节流完全一致（md5 `e18f025c87b71b9fe481f53ac6e8235d`），而每个仓库 4,664 字节的 `.gitignore` 本身在普通项目里是**不会被人注意的文件**。**⭐⭐⭐⭐⭐ 一次 md5 就把四个仓库绑成了一个簇 —— 成本远低于逐行 diff。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  subgraph Actual[仓库实际内容 全部可核验]
    Gi[.gitignore<br/>4664 B md5 e18f025c]
    Li[LICENSE<br/>MIT 1076 B]
    Rd[README.md<br/>4908 B 承诺 10 个 MCP 工具]
    Cp[config.py<br/>80 B<br/>docstring: Configuration for starter]
    Up[utils.py<br/>104 B<br/>docstring: Utility helpers for starter]
  end
  subgraph Claimed[README 声称但仓库中不存在]
    Ts[package.json 不存在]
    Ts2[TypeScript 或 JavaScript 源码 不存在]
    Src[src 目录 不存在]
    Tools[get_object_tree 等 10 个 MCP 工具<br/>无实现]
    Ws[Node.js + WebSocket 传输层<br/>无实现]
    Auto[Auto-Discovery<br/>无实现]
  end
  Rd -.承诺.-> Tools
  Rd -.承诺.-> Ws
  Rd -.承诺.-> Auto
  Ts2 -.被 language 字段否定.-> Lang[language 字段 = Python]
  subgraph Siblings[同模板的三家姊妹仓库]
    S1[PulverizeLink/roblox-performance-tool<br/>426⭐ 386 fork 91%<br/>main.py: from utils import build]
    S2[Lowbetweentrim/crypto-portfolio-tracker<br/>425⭐ 358 fork 84%<br/>main.py: from utils import optimize]
    S3[phaseboulderfetter/discord-quest-completer<br/>425⭐ 332 fork 78%<br/>main.py: from utils import optimize]
  end
  Gi --- S1
  Gi --- S2
  Gi --- S3
  S1 -.utils.py 404.-> Missing[被 import 的模块不存在]
  S2 -.utils.py 404.-> Missing
  S3 -.utils.py 404.-> Missing
  subgraph Machine[机器行为证据]
    F[forks 相邻间隔<br/>中位数 5.0s 96.9% 小于等于 10s<br/>260 fork 集中在 27 分 35 秒]
  end
  Rd -.遥测侧信号.-> F
```

## 定位判断

**⭐⭐⭐⭐⭐ 观察型项目 —— 本日报明确不推荐、不使用、不建为产品依赖的「反例样本」。**

它的生态位置是：**它占据了一个 star 榜单的位置，但没有占据一个工程的位置。** 在「Roblox Studio 的 MCP server」这个方向上，真正值得看的应该是那些真的实现了协议、真的能连上 Studio 的仓库；**而本仓库的存在会污染任何按 star 排序的该方向榜单。**

**⭐⭐⭐⭐⭐ 因此本档案的定位是「研究基础设施」而不是「项目评估」**：它的价值在于把一个可复现的判据固化下来，供本日报后续每天使用。

## 风险 / 局限 / 泡沫点

- **⭐⭐⭐⭐⭐ README 承诺的能力全部不存在**：10 个 MCP 工具、Auto-Discovery、Node.js/WebSocket 传输层，在 5 个文件里一个都没有。
- **⭐⭐⭐⭐⭐ 自述技术栈与 `language` 字段矛盾**：README 说 Node.js/TypeScript，GitHub 报 Python。
- **⭐⭐⭐⭐⭐ 没有运行时**：无 `package.json`、无入口文件，**无法运行**。
- **⭐⭐⭐⭐ fork 间隔呈机器节奏**：中位数 5.0 秒，96.9% 的间隔 ≤10 秒。
- **⭐⭐⭐⭐ 四家共享同一 `.gitignore` 与同一组 starter docstring**，star 值落在 425–427 的窄带上。
- **⭐⭐⭐⭐ 与 91 个载荷仓库同框，但手法不同**（本簇不含 `git-software.cc`）—— **说明这不是一次脚本的两种输出，而是两类不同的注意力制造方式。**
- **⭐⭐ `telegra.ph/TRANSITION-06-17-3` 链接的落地内容未核验**（本机不可达）。**本日报不对其性质作任何判断。**
- **⭐⭐ `subs` 8 / `oi` 0 / `contributors` 1 / `releases` 0** —— 没有任何社区活动的痕迹。

## 与同类项目的关系

- **⭐⭐⭐⭐⭐ vs 本日报的 `sheeridVerify`（同日对照样本）**：两者在榜单上并列，形态完全相反 —— **它 5 个文件、4 个 commit、无 CI、承诺 10 个工具交付 0 个；对方 64 个 blob、19 个源文件、CI 矩阵、模拟接口测试、显式代码级人机边界。** **⭐⭐⭐⭐⭐ 这组对照是本日最有说服力的一份：star 数相近、体量相近（甚至本仓库更小），而真实性相差一个数量级。**
- **⭐⭐⭐⭐⭐ vs 本日的载荷仓库簇（91 个带 `git-software.cc` 的仓库）**：**手法不同** —— 那批教用户暂停杀毒并执行混淆脚本；这一批交付的是「看起来像 README 的空壳」。**⭐⭐⭐⭐ 两者的共同点是都不交付实现，差别是载荷簇至少给了攻击面，本簇只给了预期。**
- **⭐⭐⭐⭐ vs 真正的 Roblox Studio MCP 实现**：**本日报未在本窗口调查该方向的其他仓库**，因此**不对该方向的生态质量下任何结论**。**⭐⭐ 只指出：本仓库不是其中一个可用的实现。**
- **⭐⭐⭐⭐ vs `poki`（同为 MCP 项目）**：poki 的 MCP server 有 23 commits、2 contributors、2 releases、六个语言 README、AGPL-3.0、完整的 `docs/verification.md`。**⭐⭐⭐⭐⭐ 同为 MCP，两者的差距不在「MCP 这个协议」，而在协议之外有没有东西。**

## 是否值得持续跟踪

**⭐⭐⭐ 不作为项目跟踪；作为判据跟踪。**

**理由**：本档案的目的是保留一份可复现的样本与一套可执行的区分判据。**一个农场仓库本身没有跟踪价值 —— 有价值的是「下次再遇到同类形态时，本日报能立刻认出它」。**

**⭐⭐⭐⭐ 具体用法**：
1. 每次分析新仓库批次时，对头部候选**默认跑 fork 间隔分布**（4 个 API 调用即可）；
2. 遇到 `language` 字段与 README 自述不一致时，标记并降权；
3. 遇到 README 有工具表而无实现目录时，标记并降权；
4. 遇到 star 值聚集在窄带（如 425–427）时，直接检查 `.gitignore` 与 `.gitattributes` 的 md5。

## 后续观察点

- **⭐⭐⭐⭐⭐ 本仓库是否被平台处置**（本日报不追踪平台行为，只记录状态变化）；
- **⭐⭐⭐⭐⭐ 同簇的另外三家（`roblox-performance-tool` / `crypto-portfolio-tracker` / `discord-quest-completer`）是否被处置或补齐实现**；
- **⭐⭐⭐⭐ 是否出现「同一模板」的新变体**（例如不同的 docstring 组合或新的 README 段落）—— **这直接衡量该手法是否在演化**；
- **⭐⭐⭐ `telegra.ph` 跳转链接是否在本机可达**（本日报快照时刻不可达）；
- **⭐⭐⭐ `subscribers_count` 是否变化**（现为 8，是本簇四个仓库中最高的）。

---
> 数据来源: GitHub REST API (2026-11-06T22:00Z 快照区间) | Stars: 427 | Forks: 260 | Subscribers: 8 | Open Issues: 0 | License: MIT | 语言字段: Python（README 自述 Node.js/TypeScript）| 体积: 7 KB | 根文件数: 5 | Commits: 4 | Contributors: 1 | Releases: 0 | 创建: 2026-11-06T06:16:35Z | 最后推送: 2026-11-06T06:16:56Z | Owner: User HerdBuilderEstimate
> 本档案用途：反例样本与判据固化。**本日报不判断作者意图、不判断账号归属、不判断平台处置状态。**
> `telegra.ph/TRANSITION-06-17-3` 的落地内容未核验（快照时刻本机不可达），本日报对其性质不作任何判断。
