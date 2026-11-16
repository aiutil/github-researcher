#!/usr/bin/env python3
"""Prepend the 2026-11-17 block to indexes/trend-index.md and daily-report.md.

Uses direct file I/O (not `patch`) because index files contain many date
strings as plain text, which makes `patch`'s uniqueness matching unreliable.
"""

TREND_BLOCK = """## 2026-11-17

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | oi | 语言 | 体积 | blobs | commits | 类别 |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| `OceanChandlerSewer/rob-run-cheat-private` | 236 | 65 | 27.5% | **91** | 1 | Markdown | 8 KB | **2** | 3 | 观察型（反例样本） |
| `hubchrysalisspanner/Call-of-Duty--Modern-Warfare-4-cheat-client` | 53 | 0 | 0% | 24 | 0 | Markdown | 7 KB | **2** | 3 | 观察型（反例样本） |
| `kajisho5/ffmpeg-skill` | 6,630 | 598 | 9.0% | 12 | 33 | Python | 40,342 KB | 425 | 100+ | 生产可用 |
| `google/elephant-goldfish-model` | 20,347 | 1,505 | 7.4% | 81 | 122 | Python | 15,271 KB | 283 | 100+ | 工具型 |
| `NVIDIA/SkillEvaluator` | 2,623 | 356 | 13.6% | 3 | 20 | Python | 23,230 KB | 1,180 | 100+ | 平台候选 |
| `mvanhorn/last30days-skill` | 68,087 | 6,035 | 8.9% | 219 | 34 | Python | 56,718 KB | 736 | 100+ | 生产可用 |
| `vercel-labs/agent-browser` | 51,996 | 3,628 | 7.0% | 114 | **589** | Rust | 35,243 KB | 680 | 100+ | 生产可用 |
| `ag-ui-protocol/ag-ui` | 18,912 | 1,961 | 10.4% | 102 | 591 | TypeScript | 89,211 KB | 6,069 | 100+ | 平台候选 |
| `boringmarketer/boring-marketing-skills` | 117 | 52 | **44.4%** | 0 | 0 | Python | 1,143 KB | 235 | **6** | 观察型 |

### ⭐⭐⭐⭐⭐ 判据修正一：「账号注册聚集度」被「占位仓库指纹」取代（本日最强判据）

10 个投放账号 **10/10** 各持有一个结构占位仓库；同一天候选池里 16 个普通账号只有 **1 个**（`staryone/sanckut`，6.25%）命中同一签名。

| 组别 | 账号数 | 命中占位签名 | 全部仓库都是占位 |
|---|---:|---:|---:|
| **投放账号** | 10 | **10（100%）** | 0 |
| **对照账号** | 16 | **1（6.25%）** | 0 |

占位签名：整棵树只有 1 个 blob（`README.md`），内容**恰好等于** `# <仓库名>`（8 字符随机名 ⇒ 10 字节），0⭐ / 0 forks / 0 issues / 1 个 commit（`Initial commit`），创建于账号注册后 1–3 分钟。

| owner | 占位仓库 | README | 创建 | 账号创建 | 延迟 |
|---|---|---|---|---|---:|
| `OceanChandlerSewer` | `trckulpa` | `# trckulpa` | 08-10T10:13:55Z | 08-10T10:12:04Z | 1m51s |
| `SandstoneShoutMoon` | `szoyxrqs` | `# szoyxrqs` | 08-10T22:38:53Z | 08-10T22:36:43Z | 2m10s |
| `VergeEnvoyAdze` | `fzohpjud` | `# fzohpjud` | 08-10T22:38:52Z | 08-10T22:36:56Z | 1m56s |
| `ashtherapistpillar` | `cwjhmbpo` | `# cwjhmbpo` | 08-10T22:39:08Z | 08-10T22:37:15Z | 1m53s |
| `LairFreighter85` | `ugqbrkec` | `# ugqbrkec` | 08-10T22:38:28Z | 08-10T22:36:14Z | 2m14s |
| `DiamondCockatooFlow` | `hrolzfoa` | `# hrolzfoa` | 08-10T22:38:25Z | 08-10T22:36:23Z | 2m02s |
| `Brandtrocontrol` | `upzuukrt` | `# upzuukrt` | 09-21T17:27:42Z | 09-21T17:24:55Z | 2m47s |
| `hubchrysalisspanner` | `nuxtdjnj` | `# nuxtdjnj` | 09-21T17:28:06Z | 09-21T17:25:39Z | 2m27s |
| `DestroyerStrait` | `rqpylldg` | `# rqpylldg` | 06-15T19:52:00Z | 06-15T19:48:39Z | 3m21s |
| `delugesovereignphase` | `khcmkgzv` | `# khcmkgzv` | 06-15T19:52:03Z | 06-15T19:49:37Z | 2m26s |

**判据升级：**

> ❌ 旧：「这些账号是否在同一时间窗口注册？」—— 受账号闲置时间影响（11-12 已证伪「当天新建」），**且投放方只需养号数月即可规避**
> ✅ 新：**「该 owner 的仓库列表里是否存在一个 README 恰好等于 `# <仓库名>` 的单 blob 随机名仓库？」** —— 一次 `users/{owner}/repos` 请求即可判定

**⭐⭐⭐⭐⭐ 跨日闭环**：11-15 记录的「零代码但高 subs」批次，其 owner `Hairzenexalt`（2026-08-10T10:11:27Z）与 `prismarmorergirder`（2026-09-21T17:24:16Z）同样各持有一个 10 字节占位仓库（`fbvylkfq` / `mopeftmn`）。

### ⭐⭐⭐⭐⭐ 判据修正二：投放方的账号是「长期在编的产能」，不是当天现注册的

9 个 `cheat client` 族仓库（ROB RUN ×3 / PUBG / GTA V / Apex Legends / Warzone / CoD MW4 / Marvel Rivals）共享同一套 README 模板：`capsule-render.vercel.app` 横幅生成器（9/9）+ `readme-typing-svg.demolab.com` 打字动效（9/9）+ `img.shields.io` 徽章阵列（9/9），⭐⭐⭐⭐⭐ 其中 6 个统一指向同一条载荷域名 `modbay.live`（路径按游戏分）。9/9 只有 2 个 blob、0 个源码文件、8/9 是 0 个 open issue（唯二的两个 issue 内容是 `NOT WORK` 与 `无法运行`）。

账号注册时间分三批：

| 批次 | 账号 | 注册窗口 | 跨度 |
|---|---|---|---:|
| A | `LairFreighter85` / `DiamondCockatooFlow` / `SandstoneShoutMoon` / `VergeEnvoyAdze` / `ashtherapistpillar` | `2026-08-10T22:36:14Z – 22:37:15Z` | **61 秒** |
| B | `Brandtrocontrol` / `hubchrysalisspanner` | `2026-09-21T17:24:55Z – 17:25:39Z` | 44 秒 |
| C | `DestroyerStrait` / `delugesovereignphase` | `2026-06-15T19:48:39Z – 19:49:37Z` | 58 秒 |

**批次 A 落在 11-15 记录的 `2026-08-10T10:11:27Z` 账号队列同一注册日内；批次 B 直接落在 11-15 记录的「`2026-09-21T17:23:39Z–17:25:16Z` 的 97 秒窗口」之内。**

⭐⭐⭐⭐⭐ **推论：投放方把账号提前 1–5 个月养好、等到需要时才启用 —— 因此任何依赖「注册时间接近当前」的判据都在被针对性规避。**

### ⭐⭐⭐⭐⭐ 判据修正三：「release 数量」应降级为「tag → commit → 代码 diff」链路闭合性

11-16 刚用 `atlas7283/steam-library-bridge`（1 个 commit → 7 秒内 4 个语义无关版本号）证伪「release 多 = 有发布史」；本日 `kajisho5/ffmpeg-skill` 从正面给出同一条判据的真样本。

| | 11-16 `steam-library-bridge`（伪造） | 本日 `ffmpeg-skill`（真实） |
|---|---|---|
| 版本号语义 | 4 个 release 互不相关（v1.2.8 → v4.4.2） | 100 个 tag 语义连续（v2.9.0 → v3.10.1） |
| commit sha 是否唯一 | 仅 1 个 commit | **100 / 100 互不相同** |
| 是否有代码 diff 支撑该版本 | **无** | **有**（父 commit 12/12 触及源码） |

实测 `ffmpeg-skill` 的 release commit 本身只改元数据（8 个文件 +16/-9：`package.json` / `.claude-plugin/plugin.json` / `.cursor-plugin/plugin.json` / `gemini-extension.json` / `server.json` / `CHANGELOG.md` / `docs/contract.md` / `docs/roadmap.md`），⭐⭐⭐⭐⭐ 而**它的父 commit 100% 触及源码**（12 个 tag 抽样，触及源码文件数 2–17 个）；⭐⭐⭐⭐⭐ 最近 100 个 commit 中 47 个 `chore(release)` 里有 35 个紧接着一个 `fix:` / `feat:`。

**⭐⭐⭐⭐⭐ 结论：判据不是「release 数量」，而是「tag → commit → 代码 diff」这条链是否闭合。**

### ⭐⭐⭐⭐⭐ 趋势修正四：「Agent Skills」已收敛成「跨 harness 可移植包格式」，但安装协议未收敛

实测 17 个相关仓库：**15 个带 `SKILL.md`**；⭐⭐⭐⭐⭐ 带 ≥3 套 harness 专属清单的有 4 个 —— `google/elephant-goldfish-model`（**6 套**：`.claude-plugin/` / `.codex-plugin/` / `.cursor-plugin/` / `.plugin/` / `.gemini/config.yaml` / Windsurf 适配器）、`mvanhorn/last30days-skill`（4 套，含 `.grok-plugin/`）、`kajisho5/ffmpeg-skill`（4 套）、`addyosmani/agent-skills`（3 套）。

⭐⭐⭐⭐⭐ **但 17 个仓库里只有 3 个同时公开 `npx skills add` 与 `/plugin marketplace add` 两条安装命令**（`addyosmani/agent-skills` / `mvanhorn/last30days-skill` / `boringmarketer/boring-marketing-skills`）。⭐⭐⭐⭐⭐ **两条分发路线并存：EGM 自己逐 harness 适配（6 套清单 + 6 份文档 + 3 个分叉 CI 工作流）；last30days 靠 `npx skills` 聚合层覆盖「50+ hosts」。**

**⭐⭐⭐⭐⭐ 结论：Skills 的竞争战场已从「技能内容」转移到「分发适配层」。**

### ⭐⭐⭐⭐⭐ 趋势修正五：「内容质量」与「分发适配」被拆成两个可分别测量的维度

`NVIDIA/SkillEvaluator` 把评估做成三个独立 tier：Tier 1 校验（安全 / 格式 / harness 兼容，依赖固定版本的 SkillSpector + Gitleaks）、Tier 2 去重（embeddings + chat）、Tier 3 实况评测（provider + agent + Docker 沙箱）。⭐⭐⭐⭐⭐ **门禁策略是成本阶梯：Tier 1 默认门禁 → Tier 2 默认门禁可关 → Tier 3 默认不门禁需显式开启；且实测原文「a scanner that cannot run is `INCOMPLETE` and exits nonzero」（fail-closed）。**

⭐⭐⭐⭐⭐ 而它的 20 个 open issue 全是「我用自己的工具时发现的 BUG」，⭐⭐⭐⭐⭐ 其中 `[FEA]: Tier 1 security on a plugin scans only its bundled skills; hooks and bin/ are never scanned` 暴露了**评估工具自身的已知扫描盲区**（由用户报告），⭐⭐⭐⭐⭐ `[BUG]: docs CI recipe (ci-integration.mdx) is less hardened than the repo's own workflows` 暴露了**文档弱于实现**。

### ⭐⭐⭐⭐⭐ 本日跨项目共性：自检（doctor）正在成为 agent 工具的标准配置

| 项目 | 自检实现 | 证据 |
|---|---|---|
| `boringmarketer/boring-marketing-skills` | `_system/scripts/doctor.sh`（CI 第一步） | 实测 `ci.yml` |
| `vercel-labs/agent-browser` | `cli/src/doctor/` 8 模块（chrome / config / daemon / environment / ffmpeg / launch / helpers / **fix**） | 实测目录树 |
| `mvanhorn/last30days-skill` | `doctor` 命令（但实测 issue 显示它会误报） | 实测 issue 标题 |

⭐⭐⭐⭐⭐ **而 `boring-marketing-skills` 的 CI 同时给出了「知识腐化」的解法：`refresh_check.py` + `tests/ttl_files.txt`（给文件设 TTL 并在 CI 里检查过期）。**

### ⭐⭐⭐⭐⭐ 自我纠偏：模板相似性不构成判据

⭐⭐⭐⭐⭐ **本日报实测一个真实学生账号 `francyellenn`（2023-05-28 创建、16 个公开仓库），其 14 个仓库中有 11 个使用同一套 `capsule-render.vercel.app` 横幅（`HAVARD-SQL` / `HAVARD-CS50-R` / `HAVARD-CS50-PYTHON` / `SANDBOX` / `comment-overdose` / `code-dumpster-fire` …），内容是葡萄牙语的 CS50 课程笔记。** ⭐⭐⭐⭐⭐ **因此「用了 capsule-render」本身不是判据 —— 本日报不据此主张任何结论；真正的判据是「owner + 占位仓库」的结构组合。**

### ⭐⭐⭐⭐⭐ 本日工具链的第二个正例：机器可读契约

| 项目 | 契约形态 | 特点 |
|---|---|---|
| `ag-ui-protocol/ag-ui` | **JSON Schema → 代码生成 SDK**（TS / Python / .NET） | 契约即代码源头；1.0 冻结并承诺 0.x 双向兼容 |
| `kajisho5/ffmpeg-skill` | `docs/contract.md`（每次 release 同步更新） | 契约随版本化 |
| `boringmarketer/boring-marketing-skills` | 7 个 JSON Schema（品牌 / 活动 / 内容 / 邮件 / 关键词 / VOC / 广告矩阵） | 契约用于 agent 间交接 |
| `NVIDIA/SkillEvaluator` | `.gitleaks.toml` + `THIRD_PARTY_NOTICES.md` + 固定版本 scanner | 契约用于供应链 |

"""


REPORT_BLOCK = """## 2026-11-17
**核心主题：** 本日最硬的发现是**投放体的「账号队列」从一次性突击升级成了长期在编的产能** —— ⭐⭐⭐⭐⭐ `cheat client` 族的 **9 个仓库（ROB RUN ×3 / PUBG / GTA V / Apex Legends / Warzone / CoD MW4 / Marvel Rivals）共享同一套 README 模板**（`capsule-render.vercel.app` 横幅生成器 + `readme-typing-svg.demolab.com` 打字动效 + `img.shields.io` 徽章阵列 + 一张功能表），⭐⭐⭐⭐⭐ **其中 6 个统一指向同一条载荷域名 `modbay.live`（路径按游戏分：`/library/rob-run`、`/library/pubg`、`/library/gta-v-enhanced`）**，⭐⭐⭐⭐⭐ **每棵只有 2 个 blob（`LICENSE` + `README.md`）、0 个代码文件、8/9 是 0 个 open issue**（唯二的两个 issue 内容是 `NOT WORK` 与 `无法运行`）。⭐⭐⭐⭐⭐ **而本日最有方法论价值的一步是「占位仓库指纹」首次被做成对照实验**：⭐⭐⭐⭐⭐ **10/10 个投放账号各持有一个「README 恰好等于 `# <仓库名>`、10 字节、1 个 blob、0⭐、1 个 commit（`Initial commit`）、创建于账号注册后 1–3 分钟」的随机名占位仓库**（`trckulpa` / `szoyxrqs` / `fzohpjud` / `cwjhmbpo` / `ugqbrkec` / `hrolzfoa` / `nuxtdjnj` / `upzuukrt` / `rqpylldg` / `khcmkgzv`），⭐⭐⭐⭐⭐ **对照组的 16 个普通账号里只有 1 个（`staryone/sanckut`）命中同一签名 —— 6.25% vs 100%**，⭐⭐⭐⭐⭐ **这使「占位仓库」成为比「账号注册时间聚集」更硬、更便宜（一次 `users/{owner}/repos` 请求即可判定）的判据。**⭐⭐⭐⭐⭐ 与之并列的第二个发现是**投放方的账号是跨月常备的，不是当天现注册的**：⭐⭐⭐⭐⭐ 实测账号分三批创建 —— **2026-08-10 一批 5 个（`22:36:14Z–22:37:15Z`，跨度 61 秒）**、**2026-09-21 一批 2 个（`17:24:55Z–17:25:39Z`）**、**2026-06-15 一批 2 个**，⭐⭐⭐⭐⭐ **且 2026-08-10 那一批落在 11-15 日报记录的 `2026-08-10T10:11:27Z` 账号队列的同一注册日内、2026-09-21 那一批直接落在 11-15 记录的「97 秒账号窗口」内** —— ⭐⭐⭐⭐⭐ **即「账号注册聚集度」这条判据在 11-16 已被证明会被时间稀释，而本日的证据表明：投放方干脆把账号提前 1–5 个月养好，等 payload 需要时才启用；⭐⭐⭐⭐⭐ 顺带闭合了一条跨日线索 —— 11-15 记录的 7 个「零代码但高 subs」仓库，其 owner `Hairzenexalt` / `prismarmorergirder` 同样各持有一个 10 字节占位仓库，即本日族与 11-15 族是同一套「养号 + 占位 + 启用」流程的两次投放。**⭐⭐⭐⭐⭐ 第三个发现是**「release 数量」这条 11-16 刚被证伪的判据，在本日被一个真项目正面推翻**：`kajisho5/ffmpeg-skill`（6,630⭐ · 598 forks · MIT）**有 100 个 release、100 个 tag、100 个互不相同的 commit sha，且 release 与 tag 一一对应** —— ⭐⭐⭐⭐⭐ **但本日报逐个查了这 100 个 tag 的 commit：release commit 本身只改元数据（8 个文件 +16/-9），而它的父 commit 才是真正的代码变更（12 个 tag 抽样中 12/12 的父 commit 触及源码，触及文件数 2–17 个）** —— ⭐⭐⭐⭐⭐ **即「release 多」既可能是伪造的（11-16 的 `steam-library-bridge`：1 个 commit → 4 个语义无关的版本号），也可能是真实的（本日：每个版本号背后都有一个真实的功能 commit）；两者的区别不在 release 数量，而在「tag → commit → 代码 diff」这条链是否闭合。**⭐⭐⭐⭐⭐ 第四个发现是**「Agent Skills」已经从「一个技能格式」收敛成「一个跨 harness 的可移植包格式」**：⭐⭐⭐⭐⭐ 本日报实测 17 个相关仓库中 **15 个带 `SKILL.md`**，⭐⭐⭐⭐⭐ **`google/elephant-goldfish-model` 同时发布 6 套 harness 专属清单（`.claude-plugin/` / `.codex-plugin/` / `.cursor-plugin/` / `.plugin/` / `.gemini/config.yaml` / Windsurf 适配器，另有 3 个按 harness 分叉的 CI 工作流与 6 份分 harness 文档）、`mvanhorn/last30days-skill` 与 `kajisho5/ffmpeg-skill` 各 4 套、`addyosmani/agent-skills` 3 套** —— ⭐⭐⭐⭐⭐ **但 17 个仓库里只有 3 个同时公开 `npx skills add` 与 `/plugin marketplace add` 两条安装命令，且并存两条分发路线（EGM 自己逐 harness 适配 vs last30days 靠 `npx skills` 聚合层覆盖「50+ hosts」），说明「包内多 harness 清单」已经收敛而「安装协议」尚未收敛 —— Skills 的竞争战场已经从「技能内容」转移到「分发适配层」。**⭐⭐⭐⭐⭐ 第五个发现是**「内容质量」第一次与「分发适配」被拆成两个可分别测量的维度**：`NVIDIA/SkillEvaluator`（2,623⭐ · 356 forks · Apache-2.0 · 1,180 blobs · 8 个 CI 工作流）把评估做成三个独立 tier（校验 / 去重 / 实况），⭐⭐⭐⭐⭐ **其 fail-closed 语义尤其值得抄：「一个跑不起来的 scanner 判为 `INCOMPLETE` 并以非零码退出」**，⭐⭐⭐⭐⭐ **而它的 open issue 全是「我用自己的工具时发现的 BUG」，其中 `[FEA]: Tier 1 security on a plugin scans only its bundled skills; hooks and bin/ are never scanned` 暴露了**评估工具自身的已知扫描盲区**。

**证据边界：** 本日全部元数据取自 **2026-11-17 CST**（2026-11-16T22:00Z–2026-11-16T23:30Z 窗口）经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `search/repositories`（`created:2026-11-16 stars:>=30`，`total_count` = **27**；以及 `created:2026-11-14..2026-11-16` 的 cheat/crack/trainer 三组查询共 **70** 个去重候选）、`repos/{owner}/{repo}`、`git/trees/{branch}?recursive=1`、`commits`（含 `files` diff）、`tags`、`releases`、`readme`、`contents/{path}`（`Accept: application/vnd.github.raw`）、`users/{owner}`、`users/{owner}/repos`、`contributors`、`search/repositories`（GitHub Trending HTML 的 `github.com/trending?since=daily` 与 `?since=weekly`）。⭐⭐⭐ **⚠️ 本日报未下载、未执行、未运行任何被投放的载荷。** 对 `modbay.live/library/rob-run` 只做了一次 HTTP **HEAD**（返回 405 / `Allow: GET` / `server: nginx/1.18.0 (Ubuntu)`），**未发起 GET**。⭐⭐⭐ **⚠️ `stargazers` 与 `subscribers` 端点在本窗口对所有被测仓库返回 404**（含对照仓库 `anthropics/skills`、`kajisho5/ffmpeg-skill`），故 **91 / 77 / 24 个订阅者的身份未取证**，**本日报不主张「91 个订阅是假的」**。⭐⭐⭐ **⚠️ 本日报实测到一个必须记录的自我纠偏：`capsule-render.vercel.app` 与 `readme-typing-svg.demolab.com` 是公开的第三方横幅生成器，不是投放方的私产 —— 实测真实学生账号 `francyellenn` 的 14 个仓库里有 11 个使用同一套横幅，因此「模板相似性」本身不构成判据，本日报不据此主张任何结论。** ⭐⭐⭐ **⚠️ `ffmpeg-skill` 的 100 个 tag 只抽样了 12 个逐个查了父 commit，「12/12 触及源码」是抽样结论，未外推到 100 个；且其 100 个 release 全部 0 asset，故 11-16 判据的第二段「release 资产是否随版本变化」在本仓库不适用。** ⭐⭐⭐ **⚠️ 「跨日连接」基于账号注册窗口重叠（`2026-08-10T22:36Z` 与 `2026-09-21T17:24Z`）而非同一批账号 ID 的直接对照，属强推断而非同一性证明。** ⭐⭐⭐ **⚠️ 对照组只有 16 个账号且取自单日候选池（有选择偏差），6.25% 不能当作总体基线。** ⭐⭐⭐ **⚠️ `ag-ui-protocol/ag-ui` 的 23 个 `SKILL.md` 中只有 1 个（`skills/ag-ui-a2ui-integration`）是对外分发技能，13 个位于 `.github/skills/`（贡献者路径）、9 个位于 `sdks/dotnet/plugins/*/skills/`（SDK 附属），本日报不将其记为「23 技能的 Skill 市场」。** ⭐⭐⭐ **⚠️ `boringmarketer/boring-marketing-skills` 建档时仅约 3 小时历史（6 个 commit / 1 位贡献者 / 0 条 issue），117⭐ 与 44.4% 的 fork/star 比全部落在最初几小时，本日报不主张任何关于长期热度的结论。** ⭐⭐⭐ **⚠️ star 增速未做统计**，所有 ⭐ 数均为快照绝对值。⭐⭐⭐ **⚠️ 本日的 `git pull --ff-only origin main` 在默认代理配置下持续失败**（`gnutls_handshake() failed`，重试 3 次并尝试 `http.sslCAInfo` / `http.version=HTTP/1.1` 均失败），**最终以 `git -c http.proxy= -c https.proxy=` 绕过本机 127.0.0.1:7890 代理成功**；本次任务中所有 `git push` 也使用同一绕过方式。⭐⭐⭐ **⚠️ 未核验项**：`ffmpeg-skill` 的 npm 包内容与仓库是否一致、42 个工具的实现质量、`clusterfuzzlite` 的实际覆盖范围、eval 的可复现性、`SkillEvaluator` 三个 tier 的内部实现与基准样本量、`elephant-goldfish-model` 的 Windsurf 适配器落地形态与 `docs/designs/architecture.md` 内容、`agent-browser` 的 589 个 issue 正文与 `doctor` 检查项、`ag-ui` 的规范全文与生态实际采用度（未做依赖分析）、`last30days-skill` 的「50+ hosts」宣称（项目自述，未逐一验证）与各平台抓取实现、`boring-marketing-skills` 的 32 个 `SKILL.md` 正文与 7 个 JSON Schema 的实际约束力、`modbay.live` 是否托管其他品类。

**关键项目：**
- 🪞 [OceanChandlerSewer/rob-run-cheat-private](projects/rob-run-cheat-private.html) — **反例样本**：2 个 blob / 0 代码 / 236⭐ · 91 subs；owner 账号 2026-08-10 注册、0 followers、恰 2 个仓库，另一个是 10 字节占位仓库 `trckulpa`
- 🪞 [hubchrysalisspanner/Call-of-Duty--Modern-Warfare-4-cheat-client](projects/call-of-duty-modern-warfare-4-cheat-client.html) — **反例样本**：owner 账号 `2026-09-21T17:25:39Z` 落在 11-15 记录的 97 秒窗口内，同样持 10 字节占位仓库 `nuxtdjnj`
- 🎬 [kajisho5/ffmpeg-skill](projects/ffmpeg-skill.html) — 42 个 FFmpeg 工具的 Agent Skill；**100 个 release / 100 个 tag / 100 个互不相同的 commit，父 commit 12/12 触及源码**；「默认 12 个 / 全量 42 个工具」的分层暴露
- 🐘 [google/elephant-goldfish-model](projects/elephant-goldfish-model.html) — **6 套 harness 专属清单**（本数据集首次）+ 3 个分叉 CI 工作流；「金鱼明确不带前情」的复核角色分离
- 🔬 [NVIDIA/SkillEvaluator](projects/skillevaluator.html) — **三 tier 评估流水线**（校验 / 去重 / 实况）+ fail-closed 的 scanner 语义；已知盲区：`hooks/` 与 `bin/` 不被扫描
- 🔎 [mvanhorn/last30days-skill](projects/last30days-skill.html) — 41,943⭐ → **68,087⭐**；4 套 harness 清单 + 「50+ hosts」聚合分发；34 条机制级 issue 与自带 `doctor`
- 🌐 [vercel-labs/agent-browser](projects/agent-browser.html) — Rust 浏览器自动化 CLI；**紧凑快照 + 稳定 ref**；`doctor` 8 模块含自动修复 `fix.rs`
- 🔌 [ag-ui-protocol/ag-ui](projects/ag-ui.html) — Agent-User Interaction Protocol；**1.0 冻结 + JSON Schema → 代码生成三语言 SDK + 0.x 双向兼容**
- 📣 [boringmarketer/boring-marketing-skills](projects/boring-marketing-skills.html) — **6 个 commit 交付 32 个技能 + 7 步 CI**（doctor / 安装路径测试 / 违禁词 / TTL 时效性 / 官方 `claude plugin validate`）+ 7 个 JSON Schema

---

"""


def prepend(path, block, marker):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if marker in content[:200]:
        print(f"{path}: already has {marker}, skipping")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(block + content)
    print(f"{path}: prepended {len(block)} bytes")


if __name__ == "__main__":
    prepend("indexes/trend-index.md", TREND_BLOCK, "## 2026-11-17")
    prepend("daily-report.md", REPORT_BLOCK, "## 2026-11-17")
