#!/usr/bin/env python3
"""Insert the 2026-11-23 section into indexes/trend-index.md and the
2026-11-23 block into daily-report.md.

Both files are append-at-the-top style: the newest date goes first.  Using a
python script instead of patch avoids the "Found N matches" problem the daily
dates cause in patch old_string matching.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------- trend-index
TREND_BLOCK = """## 2026-11-23

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | oi | 语言 | 体积 | blobs | tag/release | 类别 |
|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| `backnotprop/plannotator` | 14,399 | 1,428 | 9.9% | 37 | 205 | TypeScript | 379,909 KB | 8,051 | 100 tag / 100 rel | 工具型 |
| `alibaba/open-code-review` | 55,384 | 4,600 | 8.3% | 158 | 345 | Go | — | 1,320 | 100 tag / 100 rel | 生产可用 |
| `elementalsouls/Claude-BugHunter` | 17,618 | 1,955 | 11.1% | 79 | 15 | Python | 3,704 KB | 348 | 2 tag / 2 rel | 工具型 |
| `affaan-m/ECC` | 306,433 | 44,975 | 14.7% | 1,495 | 153 | JavaScript | 64,399 KB | 4,951 | 20 tag / 19 rel | 平台候选 |
| `obra/superpowers` | 324,102 | 28,757 | 8.9% | 1,177 | 363 | Shell / Markdown | — | 236 | 39 tag / 17 rel | 平台候选 |
| `jingyaogong/minimind` | 68,602 | 8,972 | 13.1% | 304 | 61 | Python | 39,623 KB | **49** | 2 tag / 2 rel | 观察型 |
| `nginx/nginx` | 32,874 | 8,381 | 25.5% | **945** | 493 | C | 76,752 KB | 544 | **100 tag / 36 rel** | 基础设施候选 |
| `HKUDS/CLI-Anything` | 62,725 | 5,689 | 9.1% | 232 | 285 | Python | 42,161 KB | 1,872 | 3 tag / 3 rel | 平台候选 |
| `pookjw/HermesEnabler` | 2,399 | 200 | 8.3% | 17 | 84 | Objective-C / Swift | 4,494 KB | 82 | 15 tag / 15 rel | 观察型 |

### ⭐⭐⭐⭐⭐ 判据修正一（本日的核心）：两条头条判据的根因是同一个 —— 测量口径

**修正 A：「asset 下载次数」这条判据是截断样本造成的伪影。**

11-18 日报用「asset 下载次数」给项目排座次（`plannotator` 1–12 次 / `arcane` 10–16 / `open-code-review` 57–951），
并断言「同样认真的供应链纪律，采用度差了一到两个数量级」。**根因已定位到取数脚本
`scripts/_forensics_2026_11_18.py`：先 `sorted(download_count)` 再取 `[:12]` 打印** ——
36 个 asset 被截断成**最小的 12 个**，而日报把「1」与「12」读成了区间端点。

| 仓库 | release | asset 数 | 11-18 报告区间 | **真实区间** | 低估倍数 |
|---|---|---:|---|---|---:|
| `backnotprop/plannotator` | `v0.29.1` | 36 | 9 – 13 | **9 – 1,691** | **130.1×** |
| `backnotprop/plannotator` | `v0.29.0` | 36 | 4 – 8 | **4 – 1,735** | **216.9×** |
| `backnotprop/plannotator` | `v0.29.2` | 36 | 3 – 5 | **3 – 453** | **90.6×** |
| `alibaba/open-code-review` | `v1.13.12` | 7 | 493 – 1,886 | **493 – 1,886** | 1.0×（未截断） |

**关键的非对称误差**：多 asset 的项目（`plannotator` 36 个）被截断 33%，
少 asset 的项目（`open-code-review` 7 个）**根本没触发截断** —— 误差只作用在对照组一侧。

**第二层：「取最新 N 个 release」本身跨项目不可比。** 全量 release 的年龄-下载秩相关：

| 仓库 | release 数 | Spearman(年龄, 下载量) | 最新 3 均值 | 全量均值 | 比值 |
|---|---:|---:|---:|---:|---:|
| `alibaba/open-code-review` | 100 | **−0.549** | 1,726 | 3,480 | 2.0× |
| `XiaoYouChR/Ghost-Downloader-3` | 94 | **−0.636** | 15,908 | 6,670 | 0.4× |
| `zhouxiaoka/autoclip` | 17 | −0.321 | 14,810 | 3,279 | 0.2× |
| `nginx/nginx` | 36 | **+0.370** | 2,271 | 9,255 | **4.1×** |
| `we-promise/sure` | 17 | **+0.169** | 272 | 1,122 | **4.1×** |
| `backnotprop/plannotator` | 100 | −0.181 | 6,857 | 2,729 | 0.4× |
| `pookjw/HermesEnabler` | 15 | −0.182 | 2,160 | 1,983 | 0.9× |

**第三层（正面结论）：「零下载 release」几乎都是「被跳过的版本」而非「刚发布没人要」。**
`we-promise/sure` 27 个 release 中 10 个零下载，年龄 10.3–485.3 天，**无一在 7 天内**；
`autoclip` 19 个中 2 个零下载，年龄 172.6 天与 433.4 天。

### ⭐⭐⭐⭐⭐ 判据修正二：「SKILL.md 复制倍数」这条判据用的是代理身份

11-18 日报的核心发现是 ECC「1,087 文件 / 330 身份 = 3.30×，最大单一技能被复制 10 份」。
**根因：330 用的是「父目录名」作身份，而它与「同一份内容被存了几份」不是一回事。**

| 仓库 | SKILL.md | **名口径身份** | 名口径倍数 | **内容口径身份** | 内容口径倍数 | 11-18 发布值 |
|---|---:|---:|---:|---:|---:|---|
| `affaan-m/ECC` | **1,089** | **331** | 3.29× | **944** | **1.15×** | 1087/330 |
| `backnotprop/plannotator` | 23 | 11 | 2.09× | **23** | **1.00×** | 23/11 |
| `cursor/plugins` | 173 | 113 | 1.53× | 136 | 1.27× | 173/113 |
| `tradermonty/claude-trading-skills` | 94 | 74 | 1.27× | 84 | 1.12× | 94/74 |
| `HKUDS/CLI-Anything` | 151 | 82 | 1.84× | 131 | 1.15× | — |
| `alibaba/open-code-review` | 4 | **2** | 2.00× | **4** | **1.00×** | **4/4**（内容口径） |
| `elementalsouls/Claude-BugHunter` | 83 | 83 | 1.00× | 83 | 1.00× | 83/83 |
| `obra/superpowers` | 15 | 15 | 1.00× | 15 | 1.00× | 15/15 |
| `google-labs-code/stitch-skills` | 16 | 16 | 1.00× | 16 | 1.00× | 16/16 |
| `mvanhorn/last30days-skill` | 1 | 1 | 1.00× | 1 | 1.00× | 1/1 |
| `GoogleChrome/modern-web-guidance-src` | 15 | 15 | 1.00× | 15 | 1.00× | — |
| `kajisho5/ffmpeg-skill` | 19 | 19 | 1.00× | 19 | 1.00× | — |
| `ag-ui-protocol/ag-ui` | 23 | 23 | 1.00× | 23 | 1.00× | — |
| `ChromeDevTools/chrome-devtools-mcp` | 8 | 8 | 1.00× | 8 | 1.00× | — |

**决定性事实**：ECC 的 273 个「被复制」技能名中，**只有 33 个逐字节相同，240 个内容不同** ——
`backend-patterns` 是 **10 份副本 / 9 个不同 blob sha**，`coding-standards` 同。
**即「被复制 10 份」在内容层面不成立**；「10 份」是同名身份出现在 10 个目录，且 9 份是 harness 专属变体。
`plannotator` 更极端：4 个同名身份（5/4/2 份）**每一份副本内容都不同**。

**修正后的三层判据**（取代单一「复制倍数」）：

| 层 | 定义 | ECC | plannotator | cursor/plugins | CLI-Anything | Claude-BugHunter |
|---|---|---:|---:|---:|---:|---:|
| **① 内容冗余倍数** | 文件数 ÷ 不同 blob sha | **1.15×** | 1.00× | 1.27× | 1.15× | **1.00×** |
| **② 变体率** | 同名不同内容的身份 ÷ 身份数 | **0.73** | 0.17 | 0.20 | **0.05** | **0.00** |
| **③ 身份跨度** | 同一身份名出现在几个目录 | 273 个身份 ≥2 份 | 4 | 60 | 4 | **0** |

**推论修正**：11-18 由「3.30×」推出的「ECC 的内容层与适配层投入比值得被持续观测」随之失效 ——
其**内容冗余倍数只有 1.15×**，是本队列第二低；「273 个技能有 9 套变体」才是它支持多 harness 的真实代价。

### ⭐⭐⭐⭐⭐ 正面发现：「star 增速」这条连续 6 份日报标注「未做统计」的指标，今日首次有真实时间序列

本数据集首次攒齐 **6 个连续日快照**（11-18 → 11-23，日更）。

| 统计量 | 值 |
|---|---:|
| 参与统计的仓库 | 34 |
| **相邻日区间总数** | **120** |
| **负增长区间** | **0（0.0%）** |
| **零增长区间** | **0（0.0%）** |
| min / p25 / median / p75 / max | +49 / +226 / **+415** / +668 / +2,156 |

14 个全程在榜仓库的逐日序列：

| 仓库 | 11-18 | 11-19 | 11-20 | 11-21 | 11-22 | 11-23 | 5 日增 | 逐日增 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `elementalsouls/Claude-BugHunter` | 9,095 | 11,251 | 12,391 | 14,061 | 15,885 | 17,618 | **+8,523（+93.8%）** | +2,156 / +1,140 / +1,670 / +1,824 / +1,733 |
| `obra/superpowers` | 319,255 | 321,277 | 322,015 | 322,789 | 323,655 | 324,102 | +4,847（+1.5%） | +2,022 / +738 / +774 / +866 / +447 |
| `mvanhorn/last30days-skill` | 68,952 | 69,928 | 70,737 | 71,390 | 71,941 | 72,641 | +3,689（+5.3%） | +976 / +809 / +653 / +551 / +700 |
| `dream-num/univer` | 28,859 | 29,872 | 30,426 | 30,927 | 31,083 | 31,246 | +2,387（+8.3%） | +1,013 / +554 / +501 / +156 / +163 |
| `meta/astryx` | 30,104 | 30,542 | 30,921 | 31,318 | 31,765 | 32,183 | +2,079（+6.9%） | +438 / +379 / +397 / +447 / +418 |
| `google-labs-code/stitch-skills` | 10,062 | 10,377 | 10,680 | 10,993 | 11,380 | 11,875 | +1,813（+18.0%） | +315 / +303 / +313 / +387 / +495 |
| `GoogleChrome/modern-web-guidance-src` | 8,409 | 8,807 | 9,090 | 9,505 | 9,866 | 10,176 | +1,767（+21.0%） | +398 / +283 / +415 / +361 / +310 |
| `alibaba/open-code-review` | 53,669 | 54,166 | 54,369 | 54,746 | 55,070 | 55,384 | +1,715（+3.2%） | +497 / +203 / +377 / +324 / +314 |
| `cursor/plugins` | 16,864 | 17,168 | 17,528 | 17,814 | 18,074 | 18,406 | +1,542（+9.1%） | +304 / +360 / +286 / +260 / +332 |
| `backnotprop/plannotator` | 13,030 | 13,421 | 13,644 | 13,870 | 14,139 | 14,399 | +1,369（+10.5%） | +391 / +223 / +226 / +269 / +260 |
| `ag-ui-protocol/ag-ui` | 19,951 | 20,404 | 20,614 | 20,797 | 20,997 | 21,174 | +1,223（+6.1%） | +453 / +210 / +183 / +200 / +177 |
| `we-promise/sure` | 16,250 | 16,480 | 16,690 | 16,894 | 17,119 | 17,319 | +1,069（+6.6%） | +230 / +210 / +204 / +225 / +200 |
| `tradermonty/claude-trading-skills` | 6,840 | 7,068 | 7,229 | 7,414 | 7,599 | 7,773 | +933（+13.6%） | +228 / +161 / +185 / +185 / +174 |
| `ChromeDevTools/chrome-devtools-mcp` | 58,019 | 58,203 | 58,348 | 58,520 | 58,681 | 58,828 | +809（+1.4%） | +184 / +145 / +172 / +161 / +147 |

**三条结论**：
① **6 天里没有一天是「异常值日」** —— 真实增长的形态是「首日冲高 + 回落 + 平台」，
这与 11-17 记录的投放体形态（「push 频率与 commit 数量可被 30 行定时脚本凭空制造」）明显不同；
② **「首日冲高」是普遍形态**（14 个中 11 个首日增量高于其后 4 日均值），
**即「某项目今天涨得快」几乎不携带信息量**；
③ `we-promise/sure` 的逐日增极差仅 30（占均值 14%），
与 `superpowers` 的极差 1,575（占均值 53%）形成「稳定型 vs 冲高型」的清晰对照。

### ⭐⭐⭐⭐⭐ 判据修正三：harness 目录数与技能身份数都不是稳定的能力指标

| 仓库 | 身份（名/内容） | **harness 目录 11-18 → 11-23** | 安装命令 |
|---|---|---|---|
| `obra/superpowers` | 15 / 15（1.00×） | **5 → 4 套** | 2 条 `marketplace add` |
| `backnotprop/plannotator` | 11 / 23（2.09× / 1.00×） | **2 → 4 套** | `brew install` + 2 条 `marketplace add` |
| `cursor/plugins` | 113 / 136（1.53× / 1.27×） | 1 → 1 套 | **0 条** |
| `HKUDS/CLI-Anything` | 82 / 131（1.84× / 1.15×） | **0 套** | **3 条**（`pip install cli-anything-hub` / `npx skills add … --list` / `npx skills add … --skill cli-hub-meta-skill -g -y`） |
| `ag-ui-protocol/ag-ui` | 23 / 23（1.00×） | 1 套（`antigravity`） | 1 条（`pip install ag-ui-protocol`） |

**结论**：唯一跨项目稳定的结构事实不是「harness 目录数」也不是「技能身份数」，
**而是「有没有一条别人能直接粘贴运行的安装命令」**。
11-18 的「零复制 + 多 harness 是最健康形态」结论据此**降级**为「多 harness 适配的形态曾出现」。

### ⭐⭐⭐⭐⭐ 正面发现二：契约检查正在成为多 harness 项目的标准做法

`HKUDS/CLI-Anything` 的 7 个工作流里有 **3 个是契约检查**：
`check-codex-skill.yml` / `check-cursor-plugin.yml` / `check-root-skills.yml`。
这与 11-18 记录的 `alibaba/open-code-review` 的 `plugin-contract.yml` / `action-contract.yml`
是同一模式的**第二个独立样本** —— 两个不同机构、两个不同领域、同一做法。

### ⭐⭐⭐⭐⭐ 正面发现三：成熟项目进入判据库，给出了第一组同域基线

本日 27 个仓库中有 12 个是 2015 年前的成熟项目。

| 判据 | 本日 27 个仓库的结果 |
|---|---|
| README md5 聚类 | **0 组**（两两互不相同） |
| 载荷域名（dropbox / mediafire / mega.nz / modbay.live 等） | **0 个** |
| `discord.gg` 链接 | 8 个 —— **全部是项目自己的社群邀请**（11-17 曾把它列为载荷域名，**本日修正**） |
| 2-blob 零代码仓库 | **0 个**（最小 `minimind` 49 blobs，含 22 个 `.py`） |
| owner 账号年龄 | 全部多年历史（最短 `pookjw` 2015-04-11，最长 `obra` 2009-01-09） |
| **subs/star** | **0.16% – 2.87%，中位数 0.38%**（`nginx` 2.87% 最高） |

**⭐⭐⭐⭐⭐ 关键对照**：11-15 记录的投放体样本（`rob-run-cheat-private`：236⭐ / 91 subs）
是 **38.6%** —— **高出成熟基线 13 倍**。这是「订阅农场」这条判据第一次有了同域基线。

### ⭐⭐⭐⭐⭐ 榜单换血：队列类结论不可跨日比较

11-18 的 25 个仓库中**只有 15 个**留在 11-23 榜单上。离榜 10 个：
`affaan-m/ECC`（305,414⭐）、`anthropics/skills`（196,675⭐）、`addyosmani/agent-skills`（118,640⭐）、
`sveltejs/svelte`（89,552⭐）、`ZhuLinsen/daily_stock_analysis`（73,066⭐）、
`vercel-labs/agent-browser`、`openai/codex-security`、`getarcaneapp/arcane`、
`Tencent/LoopForge`、`google-research/paper-orchestra`。

新进榜 12 个：`HKUDS/CLI-Anything`、`Tracer-Cloud/opensre`、`XiaoYouChR/Ghost-Downloader-3`、
`cathrynlavery/diagram-design`、`firecrawl/firecrawl`、`kajisho5/ffmpeg-skill`、
`mjmirza/app-store-compliance`、`nginx/nginx`、`openvinotoolkit/openvino`、
`pookjw/HermesEnabler`、`toeverything/AFFiNE`、`zhouxiaoka/autoclip`。

**因此 11-17 的 17 仓库队列上的任何比例，其分母每天都在变** ——
本日报把「双安装命令 4/17 → 2/9」明确降级为不可比。

### 本日排名变化

| 项目 | 11-18 | 11-23 | 变化 |
|---|---|---|---|
| `obra/superpowers` | 在榜 | 在榜 | 0 |
| `mvanhorn/last30days-skill` | 在榜 | 在榜 | 0 |
| `elementalsouls/Claude-BugHunter` | 在榜 | 在榜 | 0 |
| `backnotprop/plannotator` | 在榜 | 在榜 | 0 |
| `alibaba/open-code-review` | 在榜 | 在榜 | 0 |
| `GoogleChrome/modern-web-guidance-src` | 在榜 | 在榜 | 0 |
| `cursor/plugins` | 在榜 | 在榜 | 0 |
| `tradermonty/claude-trading-skills` | 在榜 | 在榜 | 0 |
| `ChromeDevTools/chrome-devtools-mcp` | 在榜 | 在榜 | 0 |
| `ag-ui-protocol/ag-ui` | 在榜 | 在榜 | 0 |
| `affaan-m/ECC` | 在榜 | **离榜** | ↓ |
| `anthropics/skills` | 在榜 | **离榜** | ↓ |
| `addyosmani/agent-skills` | 在榜 | **离榜** | ↓ |
| `Tencent/LoopForge` | 在榜 | **离榜** | ↓ |
| `getarcaneapp/arcane` | 在榜 | **离榜** | ↓ |
| `google-research/paper-orchestra` | 在榜 | **离榜** | ↓ |
| `jingyaogong/minimind` | 对照组 | 在榜 | ↑ |
| `dream-num/univer` | 对照组 | 在榜 | ↑ |
| `nginx/nginx` | 未观测 | 在榜 | **新进榜** |
| `HKUDS/CLI-Anything` | 未观测 | 在榜 | **新进榜** |
| `Tracer-Cloud/opensre` | 未观测 | 在榜 | **新进榜** |
| `pookjw/HermesEnabler` | 未观测 | 在榜 | **新进榜** |
| `XiaoYouChR/Ghost-Downloader-3` | 未观测 | 在榜 | **新进榜** |
| `zhouxiaoka/autoclip` | 未观测 | 在榜 | **新进榜** |
| `kajisho5/ffmpeg-skill` | 在榜（11-17 观测） | 在榜 | ↑ |

"""

# --------------------------------------------------------------- daily-report
REPORT_BLOCK = """## 2026-11-23
**核心主题：** 本日最硬的发现是**我们自己的两条判据在同一批数据上被证伪，而根因是同一个：测量口径** —— ⭐⭐⭐⭐⭐ 第一条是**「asset 下载次数」这条判据**：11-18 日报用它断言 `plannotator`「下载仅 1–12 次」、`open-code-review`「57–951 次」，⭐⭐⭐⭐⭐ **但那次的脚本取的是 `sorted(download_count)[:12]`（36 个 asset 里**最小的** 12 个）当成全量区间**，⭐⭐⭐⭐⭐ **本日在同一时刻、同一批 release 上复测：同一 tag `v0.29.1` 的真实区间是 9–1,691（11-18 视角显示 9–13，**被低估 130.1×**）、`v0.29.0` 是 4–1,735（**216.9×**）、`v0.29.2` 是 3–453（**90.6×**），⭐⭐⭐⭐⭐ **即 11-18 那条「采用度差一到两个数量级」的结论是测量伪影而非事实**；⭐⭐⭐⭐⭐ 且**误差是非对称的** —— 多 asset 的 `plannotator`（36 个）被截断 33%，少 asset 的 `open-code-review`（7 个）**根本没触发截断**，⭐⭐⭐⭐⭐ **第二层：即使口径修正，「取最新 N 个 release」也跨项目不可比 —— 实测 7 个仓库的「年龄-下载」Spearman 秩相关有 3 个为正、4 个为负（`nginx` +0.370、`open-code-review` −0.549、`Ghost-Downloader-3` −0.636），⭐⭐⭐⭐⭐ `nginx` 的「最新 6 个 release」只占全量下载的 4.3%，⭐⭐⭐⭐⭐ 而正确做法是「全量 release + 年龄分层 + 同域对照」；⭐⭐⭐⭐⭐ 第二条是**「SKILL.md 复制倍数」这条判据**：11-18 日报的核心发现是 ECC「1,087 文件 / 330 身份 = 3.30×」，⭐⭐⭐⭐⭐ **但 330 这个数用的是「父目录名」作身份，本日在同一棵树上并置两种口径后发现 —— 名口径 331（3.29×，与 11-18 一致）、内容 sha 口径 944（1.15×），⭐⭐⭐⭐⭐ 而 273 个「被复制」的技能名里有 **240 个其副本内容并不相同**（`backend-patterns` 10 份副本 / 9 个不同 sha），⭐⭐⭐⭐⭐ **即「3.30×」衡量的是「同名技能出现在多少个目录」而非「同一份内容被冗余存储了几次」；⭐⭐⭐⭐⭐ `plannotator` 更极端：名口径 23/11（2.09×）→ 内容口径 **23/23（1.00×）**，4 个被复制的技能身份其 5/4/2 份副本逐份内容都不同**；⭐⭐⭐⭐⭐ **这两个修正合起来指向同一条方法论：凡是用「截断的样本」或「代理身份」去支撑一个关于「量级」的结论，都必须先做口径审计** —— ⭐⭐⭐⭐⭐ **而本日第三次给出正面证据的是「star 增速」这条本数据集连续 6 份日报都标注「未做统计」的指标**：⭐⭐⭐⭐⭐ **本数据集首次攒齐 6 个连续日快照（11-18 → 11-23，日更），实测 14 个在 6 个快照中全程在榜的仓库、120 个相邻日区间，结果是 **0 个负区间、0 个平区间**，min +49 / p25 +226 / median +415 / p75 +668 / max +2,156**，⭐⭐⭐⭐⭐ 且 `elementalsouls/Claude-BugHunter` 的日增序列是 **+2,156 / +1,140 / +1,670 / +1,824 / +1,733**，⭐⭐⭐⭐⭐ **即 6 天里没有一天是「异常值日」，增长是连续的、有噪声但无断裂 —— 这与 11-17 记录的「投放体可用 30 行定时脚本凭空制造 push 频率」形成直接对照：⭐⭐⭐⭐⭐ 本数据集首次有了一条能真正区分「真实增长」与「被制造的增长」的基线**；⭐⭐⭐⭐⭐ 第四个发现是**「分发适配层」这条线在本日出现了一个反向样本**：`obra/superpowers` 仍是 **15 身份 / 15 文件 / 双口径均 1.00× 零复制**，⭐⭐⭐⭐⭐ **但它的 harness 目录数从 11-18 的 5 套降到了 4 套，而 `backnotprop/plannotator` 从 2 套升到 4 套、`HKUDS/CLI-Anything` 是 0 套目录却有 3 条安装命令** —— ⭐⭐⭐⭐⭐ **即「harness 目录数」与「独立技能身份数」都不是稳定的能力指标，⭐⭐⭐⭐⭐ 而真正稳定的结构事实是「有没有一条别人能跑的安装命令」**；⭐⭐⭐⭐⭐ 第五个发现是**本日榜单的结构特征是「成熟基础设施与 AI 原生项目同框」，⭐⭐⭐⭐⭐ 这恰好给出了 11-18 建立的判据库一个难得的同域大样本对照**：⭐⭐⭐⭐⭐ 本日 27 个仓库中 `nginx/nginx`（32,874⭐ · 2012 年创建 · 544 blobs）、`openvinotoolkit/openvino`（12,080⭐ · **19,247 blobs**）、`toeverything/AFFiNE`、`meta/astryx`、`dream-num/univer` 都是多年度维护的成熟项目，⭐⭐⭐⭐⭐ 实测**全部 27 个仓库 README md5 两两互不相同（0 个聚类）、无载荷域名、owner 账号全部有多年历史**，⭐⭐⭐⭐⭐ 且**首次给出成熟项目的 subs/star 基线 0.23%–2.87%（中位数 0.38%）—— 对照 11-15 记录的投放体样本 38.6%，高出 13 倍**。

**证据边界：** 本日全部元数据取自 **2026-11-23 CST**（2026-11-22T22:00Z–23:00Z 窗口）经 `gh` CLI 认证的 GitHub REST API 快照，覆盖日榜 16 个 + 周榜 13 个、去重 **27 个仓库**，以及本机保留的 **6 个历史日快照**（11-18 ~ 11-22）用于时间序列统计。⭐⭐⭐ **⚠️ 本日报未 clone、未安装、未运行任何被观测项目**，未调用任何 LLM API，未下载任何 release asset，未访问任何第三方载荷域名，未做 GPG 验签。⭐⭐⭐ **⚠️ 6 个历史快照取自本机 /tmp，采集时刻与当前不同（11-18 约 06:00 CST、其余 06:03–06:04 CST），因此 star 序列的「日」精度约 ±1 小时；且每个点是一次独立抓取，两次抓取之间可能存在未观测到的增长或回落（含 unstar），本日报只主张「区间净增为正」。** ⭐⭐⭐ **⚠️「全量 release」实测只覆盖 API 返回的前 100 条** —— `plannotator` / `open-code-review` / `opensre` / `Ghost-Downloader-3` 的 release 总数均可能 ≥100，**更早的 release 不在样本内，「全量均值」实为「最近 100 个 release 的均值」。** ⭐⭐⭐ **⚠️ 下载量是 GitHub `download_count` 计数器，不是独立用户数** —— 重复下载与 CI/镜像拉取均会计入，未核验是否存在批量拉取。⭐⭐⭐ **⚠️ Spearman 相关系数在 n=15~100 上对离群值敏感** —— `nginx` 的 +0.370 主要由单个 244,802 下载的 release 拉高，本日报只主张「按最新 N 个采样在不同项目上产生方向相反的偏差」，不主张任何因果解释。⭐⭐⭐ **⚠️ 技能身份的两套口径都只证明「是否逐字节相同」** —— 未逐份 diff 240 个 ECC 变体、4 个 plannotator 身份、4 个 CLI-Anything 身份，因此「变体」一词在本日报中仅指「blob sha 不同」，**不主张它们在功能语义上不同**。⭐⭐⭐ **⚠️ issue 抽样**：`nginx` 6 条、`CLI-Anything` 6 条、`minimind` 6 条、`HermesEnabler` 6 条、`opensre` 7 条、`autoclip` 6 条、`Ghost-Downloader-3` 6 条，**仅读标题、作者与评论数，未逐条读正文**。⭐⭐⭐ **⚠️ 11-17 的载荷词表把 `discord.gg` 列为载荷域名，本日实测 8 个含该域名的仓库全是正当项目**，据此将其移出载荷词表；该词表的其余条目未逐条复测。⭐⭐⭐ **⚠️ 本日样本中成熟项目比例异常高（12/27），不能推广** —— 11-16 ~ 11-18 的样本以「当日新建仓库」为主，而**一个新建仓库的 subs/star 天生更高**（订阅早于 star 出现），这个混淆本日报尚未处理。⭐⭐⭐ **⚠️ 未核验项**：`nginx` 的 `.asc` 签名有效性与 stable/mainline 用户构成、493 个 issue 正文；`plannotator` 的应用技术栈与 SBOM 内容、205 个 issue 正文；`Claude-BugHunter` 的 83 份技能内容质量与上游对照；`ECC` 的 npm 包与 GitHub App 分发物、23 个生成/同步脚本的实际行为；`CLI-Anything` 的 67 份 per-CLI 生成物内容与三个契约检查的具体规则；`minimind` 的「2 小时 / 3 元」宣称、训练数据来源与许可；`HermesEnabler` 在真机上的行为与 `.ipa` 签名有效期；`superpowers` 的 15 份技能内容。

**关键项目：**
- 🗂️ [backnotprop/plannotator](projects/plannotator.html) — **两条判据的共同反例**：asset 下载真实区间 3–1,735（11-18 的「1–12」是截断伪影，低估 130–217×）；23 SKILL.md 名口径 11 身份 / 内容口径 23 身份；36 asset + CycloneDX SBOM + 13 sha256 的供应链纪律未变；harness 目录 2→4 套
- 🔍 [alibaba/open-code-review](projects/alibaba-open-code-review.html) — **非对称测量误差的对照侧**：每 release 仅 7 个 asset，11-18 的 `[:12]` 根本没触发截断；全量 release 单 asset 下载最大值 16,263；4 个 SKILL.md 内容口径 1.00×（名口径 2.00×）
- 🐛 [elementalsouls/Claude-BugHunter](projects/claude-bughunter.html) — **两套口径均零复制零变体（83/83）**；本数据集首条完整 star 时间序列：9,095 → 17,618（**+93.8%**，逐日 +2,156/+1,140/+1,670/+1,824/+1,733）
- ⚡ [affaan-m/ECC](projects/ecc.html) — **口径修正的最刺眼样本**：1,089 SKILL.md = 名口径 331（3.29×）/ 内容口径 944（1.15×）；273 个同名技能中 240 个副本内容不同 —— 「被复制 10 份」不成立；已离开 Trending 榜单
- 🧠 [obra/superpowers](projects/superpowers.html) — **15 身份 / 双口径 1.00× 零复制**；但 harness 目录 5→4 套（11-18 的结论需降级）；6 日 star 319,255 → 324,102（首日占 5 日增量的 42%）
- 🧠 [jingyaogong/minimind](projects/minimind.html) — **68,602⭐ 却只有 49 blobs，但不是投放体**：22 个 `.py`、0 CI、61 条真问题 issue（含 SDPA/KV cache、SFT assistant span 技术补丁）、账号 2020 年注册
- 🌐 [nginx/nginx](projects/nginx.html) — **采样窗口偏差最极端的样本**：双发布线使「最新 6 个 release」只占全量下载 4.3%，单 asset 最高 244,802；本日唯一带 `.asc` 分离签名的项目；**成熟项目 subs/star 基线 2.87%**
- 🔧 [HKUDS/CLI-Anything](projects/cli-anything.html) — **契约检查的第二个独立样本**（`check-codex-skill.yml` / `check-cursor-plugin.yml` / `check-root-skills.yml`）；151 SKILL.md 名口径 82（1.84×）/ 内容口径 131（1.15×），变体率 0.05 为本队列最低；**0 套 harness 目录却有 3 条安装命令**
- ⌚ [pookjw/HermesEnabler](projects/hermesenabler.html) — **1 个 release 只发 1 个 `.ipa`**（下载 346–6,650，是本日少数未被截断污染的样本）；0 CI 却有 84 条「机型+系统版本+症状」三要素齐全的 issue；10 种语言 README 占 22% blobs

---

"""


def insert_top(path: Path, block: str, anchor: str) -> None:
    text = path.read_text(encoding="utf-8")
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit(f"{path}: anchor {anchor!r} not found")
    path.write_text(text[:idx] + block + text[idx:], encoding="utf-8")
    print(f"inserted into {path}")


def update_trend_frontmatter(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    fm = parts[1]
    import re
    fm = re.sub(r'^title:.*$', 'title: "2026-11-23 GitHub 趋势研究简报"', fm, count=1, flags=re.M)
    fm = re.sub(r'^slug:.*$', 'slug: "2026-11-23"', fm, count=1, flags=re.M)
    fm = re.sub(r'^date_added:.*$', 'date_added: "2026-11-23"', fm, count=1, flags=re.M)
    fm = re.sub(r'^last_seen_date:.*$', 'last_seen_date: "2026-11-23"', fm, count=1, flags=re.M)
    fm = re.sub(r'^stars:.*$', 'stars: "9 projects"', fm, count=1, flags=re.M)
    fm = re.sub(
        r'^stars_delta:.*$',
        'stars_delta: "2026-11-23: 新增 3 个项目档案（nginx / minimind / hermesenabler），'
        '更新 6 个（plannotator / alibaba-open-code-review / claude-bughunter / ECC / superpowers / cli-anything）"',
        fm, count=1, flags=re.M)
    fm = re.sub(
        r'^tags:.*$',
        'tags: ["trend-index", "daily", "methodology", "caliber-audit", "star-time-series", "metric-correction"]',
        fm, count=1, flags=re.M)
    path.write_text(f"---{fm}---{parts[2]}", encoding="utf-8")
    print(f"updated frontmatter of {path}")


if __name__ == "__main__":
    ti = ROOT / "indexes" / "trend-index.md"
    insert_top(ti, TREND_BLOCK, "\n## 2026-11-18\n")
    update_trend_frontmatter(ti)

    dr = ROOT / "daily-report.md"
    insert_top(dr, REPORT_BLOCK, "## 2026-11-18\n")
