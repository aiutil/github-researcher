#!/usr/bin/env python3
"""Update the 2026-11-23 project profiles.

For each project: update frontmatter (stars / stars_delta / score /
last_seen_date / tags) and prepend a "## 最近动态（2026-11-23）" section
carrying today's measured facts.

The daily-report body is NOT regenerated — only frontmatter and the new
最近动态 block are touched, so hand-written architecture prose is preserved.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJ = ROOT / "projects"

UPDATES = {
    "plannotator": {
        "stars": "14,399 stars",
        "stars_delta": (
            "⭐ 2026-11-23 更新（快照 2026-11-23 CST，仓库创建于 2025-12-28T02:09:40Z）："
            "13,035⭐（11-18 快照）→ **14,399⭐**（+1,364，6 日序列 13,030 → 13,421 → 13,644 → "
            "13,870 → 14,139 → 14,399）；forks 1,428 · subs 37 · oi 205 · **8,051 blobs**"
            "（11-18 为 7,261）· 379,909 KB · TypeScript · Apache-2.0 · **100 个 release / 100 个 tag，"
            "每个 release 36 个 asset**（CycloneDX SBOM + 13 个 sha256）· 14 个 CI 工作流 · "
            "**SKILL.md 23 个 / 名口径 11 身份（2.09×）/ 内容口径 23 身份（1.00×）** · "
            "**asset 下载真实区间 3–1,735（11-18 记的「1–12」是取 36 个 asset 中最小 12 个的截断伪影）** · "
            "harness 目录 4 套（11-18 为 2 套）"
        ),
        "score": 93,
        "last_seen_date": "2026-11-23",
        "tags": '["agent-workspace", "sbom", "signed-releases", "caliber-audit", "multi-harness", "variant-vs-copy"]',
        "recent": """
⭐⭐⭐⭐⭐ **本日对本项目做的是口径审计复测，结论是：11-18 日报对它下的两条判断都需要修正，而它本身作为供应链纪律标杆的地位不变。**

**可核验事实一（修正一）：asset 下载次数。**

| 口径 | 11-18 日报发布值 | **11-23 实测** |
|---|---|---|
| `v0.29.1` 下载区间 | — | **9 – 1,691**（11-18 视角显示 9–13，**低估 130.1×**） |
| `v0.29.0` 下载区间 | — | **4 – 1,735**（11-18 视角 4–8，**216.9×**） |
| `v0.29.2` 下载区间 | — | **3 – 453**（11-18 视角 3–5，**90.6×**） |
| 全量 release 单 asset 最大下载 | — | **2,304** |
| 全量 release 平均下载（最近 100 个） | — | **2,729** |
| 最新 3 个 release 平均下载 | — | **6,857**（比全量均值高 2.5×） |

⭐⭐⭐⭐⭐ **根因已定位到 11-18 的取数脚本第 60 / 163 行：先 `sorted(download_count)` 再取 `[:12]` 打印，而 36 个 asset 被截断成最小的 12 个，⭐⭐⭐⭐⭐ 日报把「1」与「12」读成了区间端点。⭐⭐⭐⭐⭐ 本日报据此**撤回**「plannotator 下载仅 1–12 次、是本组最低」的结论；⭐⭐⭐⭐⭐ **但也同时撤回「它下载很多」的相反主张 —— 实测其全量均值 2,729 低于 `open-code-review` 的 3,480，⭐⭐⭐⭐⭐ 准确表述是「两者在同一量级，11-18 的对比不成立」。**

**可核验事实二（修正二）：SKILL.md 身份数。**

| 口径 | 11-18 发布值 | **11-23 实测** |
|---|---|---|
| SKILL.md 文件数 | 23 | **23**（未变） |
| **名口径**（身份 = 父目录名，11-18 用的口径） | 11 | **11**（复现 ✓） |
| **内容口径**（身份 = 不同 blob sha 集合） | — | **23** |
| `plannotator-review` | 5 份 | **5 份 / 5 个不同 blob sha** |
| `plannotator-last` | 4 份 | **4 份 / 4 个不同 blob sha** |
| `plannotator-inbox` | 2 份 | **2 份 / 2 个不同 blob sha** |

⭐⭐⭐⭐⭐ **即 4 个被复制的技能身份，其每一份副本的内容都不同 —— 它们是「针对不同 app 定制过的同名技能变体」，⭐⭐⭐⭐⭐ 而不是「同一份内容存了 N 遍」。⭐⭐⭐⭐⭐ 这与它 41 个 generator/sync 脚本路径的存在一致（变体是被生成出来的，但生成器会针对目标 app 调整内容）。**

**可核验事实三（未变，且加强）：供应链纪律仍是本队列最完整的一档。**

| 指标 | 11-18 | **11-23** |
|---|---:|---:|
| release / tag | 100 / 100 | **100 / 100** |
| 每 release 的 asset | 36 | **36** |
| 最新 release | `v0.28.67` | **`v0.29.2`** |
| SBOM 文件名 | `plannotator-0.28.67-release-sbom.cdx.json` | **`plannotator-0.29.2-release-sbom.cdx.json`**（文件名仍内嵌版本号，即每版独立生成） |
| harness 目录 | 2 套 | **4 套**（`claude` / `codex` / `copilot` / `gemini`） |
| blobs | 7,261 | **8,051**（+790） |
| 6 日 star | 13,030 | **14,399**（+10.5%，逐日 +391/+223/+226/+269/+260） |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 值得单独指出的一条：实测 `v0.28.63` 的 asset 数是 26 而不是 36 —— 即 asset 构成本身在演进（新增了 10 个资产），⭐⭐⭐⭐⭐ 这符合 11-18 建立的「资产是否随版本演进」这条判据，是一个正向证据。**

⭐⭐⭐⭐⭐ **⭐⭐⭐ 而「harness 目录从 2 套增到 4 套」是一个新观测 —— 本日报 11-23 的第 4 条趋势指出，⭐⭐⭐⭐⭐ harness 目录数会随项目演进上下浮动（`obra/superpowers` 同期从 5 套降到 4 套），⭐⭐⭐⭐⭐ 因此不宜把目录数当作稳定的能力刻度。**
""",
    },
    "alibaba-open-code-review": {
        "stars": "55,384 stars",
        "stars_delta": (
            "⭐ 2026-11-23 更新（快照 2026-11-23 CST，仓库创建于 2026-05-18T02:16:36Z）："
            "53,682⭐（11-18 快照）→ **55,384⭐**（+1,702，6 日序列 53,669 → 54,166 → 54,369 → "
            "54,746 → 55,070 → 55,384）；forks 4,600 · subs 158 · oi 345 · **1,320 blobs**"
            "（11-18 为 1,227）· Go · Apache-2.0 · **100 个 release / 100 个 tag，每个 release 7 个 asset**"
            "（含 sha256sum.txt）· **全量 release 单 asset 下载最大值 16,263，是「最新 6 个 release」"
            "窗口（14,019）的 23.8×** · **SKILL.md 4 个 / 名口径 2 身份（2.00×）/ 内容口径 4 身份（1.00×）** · "
            "harness 目录 2 套"
        ),
        "score": 91,
        "last_seen_date": "2026-11-23",
        "tags": '["code-review", "hybrid-architecture", "alibaba", "contract-as-ci", "release-discipline", "caliber-audit"]',
        "recent": """
⭐⭐⭐⭐⭐ **本日对本项目做的是同口径复测，结论是：它作为「确定性 + LLM 混合架构」与「契约做成 CI 门禁」这两条的样本地位完全不变，⭐⭐⭐⭐⭐ 但 11-18 用来支撑对比的那组下载数字需要修正 —— 而修正的方向对它有利。**

**可核验事实一：11-18 的下载区间之所以看起来高，是因为它的 asset 数少到不会被截断。**

| release | asset 数 | 11-18 视角（`[:12]`，实际未截断） | **真实区间** |
|---|---:|---|---|
| `v1.13.12` | 7 | 493 – 1,886 | **493 – 1,886**（无截断） |
| `v1.13.13` | 7 | 476 – 991 | **476 – 991**（无截断） |
| `v1.14.1` | 7 | — | **119（max）/ 441（total）** |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 关键的不对称就在这里：`plannotator` 每个 release 36 个 asset，被截断的正是 12 个（33%）；⭐⭐⭐⭐⭐ 而本项目每个 release 只有 7 个 asset，11-18 脚本的 `[:12]` **根本没有触发截断**。⭐⭐⭐⭐⭐ 也就是说，11-18 那次对比的误差**只作用在对照组一侧**，⭐⭐⭐⭐⭐ 这是一个典型的「非对称测量误差」案例 —— 也是本日第 1 条趋势的方法论核心。**

**可核验事实二：全量 release 的下载分布。**

| 指标 | 实测值 |
|---|---:|
| release 数（API 前 100 条） | **100** |
| **全量 release 平均下载** | **3,480** |
| 最新 3 个 release 平均下载 | **1,726**（比全量均值**低** 2.0×） |
| **全量 release 单 asset 最大下载** | **16,263** |
| 最新 6 个 release 下载总量 | **14,019** |
| 较老 release（9.8–159.1 天）下载总量 | **333,966**（**23.8×**） |
| Spearman(发布年龄, 下载量) | **−0.549**（n=100） |
| 30–34 天区间中位数 | **28,400** |

⭐⭐⭐⭐⭐ **即本项目的下载量是「越老越高」的（ρ = −0.549），⭐⭐⭐⭐⭐ 而 `nginx/nginx` 是「越老越低」（ρ = +0.370），⭐⭐⭐⭐⭐ `Ghost-Downloader-3` 越老越高（−0.636），`autoclip` 越老越低（−0.321）。⭐⭐⭐⭐⭐ **四个项目两种符号 —— 这就是本日报主张「取最新 N 个 release 不能跨项目比较」的实证。**

**可核验事实三：SKILL.md 身份口径（本日新发现的一处 11-18 口径不一致）。**

| 口径 | 11-18 发布值 | **11-23 实测** |
|---|---|---|
| SKILL.md 文件数 | 4 | **4** |
| **名口径**（身份 = 父目录名） | — | **2**（`open-code-review` / `open-code-review-delegate`，各 2 份） |
| **内容口径**（身份 = 不同 blob sha 集合） | **4** | **4**（复现 ✓） |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 即 11-18 那张表里这一行用的是内容口径（或两者在此巧合相同），⭐⭐⭐⭐⭐ 而其余各行用的是名口径 —— 11-18 的表格内部口径并不统一，⭐⭐⭐⭐⭐ 这本身比任何一个单行的偏差更危险，因为它使整张表无法被复现。⭐⭐⭐⭐⭐ 且 4 份副本两两内容不同（`plugins/open-code-review/skills/` vs `skills/`），⭐⭐⭐⭐⭐ 同样是「变体」而非「复制」。**

**可核验事实四：6 日 star 序列与契约工作流。**

| 指标 | 实测值 |
|---|---|
| 6 日 star 序列 | 53,669 → 54,166 → 54,369 → 54,746 → 55,070 → **55,384** |
| 逐日增 | +497 / +203 / +377 / +324 / +314 |
| 5 日总增 | **+1,715（+3.2%）** |
| blobs | 1,227 → **1,320**（+93） |
| harness 目录 | 2 套（`claude-code` / `opencode`） |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 而本项目特有的价值 —— 「把契约做成 CI 门禁」—— 本日出现了第二个独立样本：`HKUDS/CLI-Anything` 的 `check-codex-skill.yml` / `check-cursor-plugin.yml` / `check-root-skills.yml`。⭐⭐⭐⭐⭐ 两个不同机构、两个不同领域（代码评审 vs agent CLI 生成）、同一模式，⭐⭐⭐⭐⭐ **本日报据此把「契约检查成为多 harness 项目的标准做法」列为本日的一条正面发现。**
""",
    },
    "claude-bughunter": {
        "stars": "17,618 stars",
        "stars_delta": (
            "⭐ 2026-11-23 更新（快照 2026-11-23 CST，仓库创建于 2026-05-05T11:22:32Z）："
            "9,120⭐（11-18 快照）→ **17,618⭐**（+8,498，**6 日序列 9,095 → 11,251 → 12,391 → "
            "14,061 → 15,885 → 17,618，累计 +93.8%**）；forks 1,955 · subs 79 · oi **15** · "
            "**348 blobs**（11-18 为 335）· 3,704 KB · Python · MIT · **2 个 release / 2 个 tag** · "
            "**83 个 SKILL.md = 名口径 83 身份 = 内容口径 83 身份（两口径均 1.00×，零复制且零变体）** · "
            "8 个 CI 工作流 · 贡献者 `elementalsouls`（账号 2019-04-03 创建）"
        ),
        "score": 92,
        "last_seen_date": "2026-11-23",
        "tags": '["agent-skills", "security", "red-team", "zero-replication", "star-time-series", "caliber-audit"]',
        "recent": """
⭐⭐⭐⭐⭐ **本日对本项目做的是「口径审计 + 首次时间序列」双重复测，结论是：它是本数据集里唯一同时满足「两套身份口径都零复制」与「5 天 star 增长 +93.8%」的项目，⭐⭐⭐⭐⭐ 而这两条在本日之前都无法被确认。**

**可核验事实一：口径审计反而让「零复制」这个结论更硬了。**

| 仓库 | 名口径 | 内容口径 | 说明 |
|---|---:|---:|---|
| **`elementalsouls/Claude-BugHunter`** | **83（1.00×）** | **83（1.00×）** | **同名身份中出现 ≥2 份的：0 个** |
| `backnotprop/plannotator` | 11（2.09×） | 23（1.00×） | 4 个同名身份的副本内容全不同 |
| `affaan-m/ECC` | 331（3.29×） | 944（1.15×） | 273 个同名身份中 240 个内容不同 |
| `cursor/plugins` | 113（1.53×） | 136（1.27×） | 60 个同名身份中 23 个内容不同 |
| `tradermonty/claude-trading-skills` | 74（1.27×） | 84（1.12×） | 10 个同名身份中 10 个内容不同 |
| `alibaba/open-code-review` | 2（2.00×） | 4（1.00×） | 2 个同名身份的副本内容不同 |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 关键点：本项目在**两套口径下都是 83/83**，⭐⭐⭐⭐⭐ 即它既没有复制，也没有为任何 harness 定制变体 —— 83 个技能就是 83 份互不相同的内容。⭐⭐⭐⭐⭐ 这与 ECC 的「1.15× 内容冗余 + 0.73 变体率」形成清晰对照，⭐⭐⭐⭐⭐ **说明「零复制」与「零变体」是两个独立的质量维度，而本项目在两个维度上都取到了最优值。**

**可核验事实二：本数据集首条真实的 star 时间序列。**

| 日期 | 快照 star | 相对前一日 |
|---|---:|---:|
| 2026-11-18 | 9,095 | — |
| 2026-11-19 | 11,251 | **+2,156** |
| 2026-11-20 | 12,391 | +1,140 |
| 2026-11-21 | 14,061 | +1,670 |
| 2026-11-22 | 15,885 | +1,824 |
| 2026-11-23 | **17,618** | +1,733 |

⭐⭐⭐⭐⭐ **⭐⭐⭐⭐⭐ 形态判读：「首日冲高 + 回落 + 平台」。⭐⭐⭐⭐⭐ 首日 2,156（最高）、次日回落 47% 至 1,140、此后三天稳定在 1,670–1,824。⭐⭐⭐⭐⭐ 五日极差 1,016、均值 1,704、变异系数约 0.21，⭐⭐⭐⭐⭐ **没有任何一天归零 —— 这与 11-17 记录的投放体形态（「push 频率与 commit 数量可被 30 行定时脚本凭空制造」，通常表现为一夜暴涨后长期不动）明显不同。⭐⭐⭐⭐⭐ 本数据集此前 6 份日报都在证据边界里写「star 增速未做统计」，⭐⭐⭐⭐⭐ 本日第一次有了可与「被制造的增长」区分的基线。**

**可核验事实三：规模与社区指标。**

| 指标 | 11-18 | **11-23** |
|---|---:|---:|
| stars | 9,120 | **17,618** |
| forks | 1,349 | **1,955** |
| subs | 49 | **79** |
| open issues | **11** | **15** |
| blobs | 335 | **348** |
| subs/star | 0.54% | **0.45%**（本队列中位数 0.38%） |
| fork/star | 14.8% | 11.1% |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 值得单独指出：** 本队列 27 个仓库中 `open issue` 最少的是 `Tracer-Cloud/opensre`（20），第二少的就是本项目（15），⭐⭐⭐⭐⭐ 而它的 star 增速是本队列第一 —— ⭐⭐⭐⭐⭐ **「高增长 + 低 issue」这一组合在本数据集里目前只出现在两个项目上，⭐⭐⭐⭐⭐ 本日报认为它值得作为一个长期观察项（可能是「被广泛使用但问题不外溢」，⭐⭐⭐ ⚠️ 也可能是「问题被隐藏在 Discussions 里」—— 本日报未核验其 Discussions）。**
""",
    },
    "ecc": {
        "stars": "306,433 stars",
        "stars_delta": (
            "⭐ 2026-11-23 更新（快照 2026-11-23 CST，仓库创建于 2026-01-18T00:51:51Z）："
            "305,425⭐（11-18 快照）→ **306,433⭐**（+1,008；本日已**离开 Trending 榜单**，"
            "最后可见快照为 2026-11-19 的 306,433⭐，之后未再进入日榜/周榜）；forks 44,975 · "
            "subs 1,495 · oi 153 · **4,951 blobs**（11-18 为 4,878）· 64,399 KB · JavaScript · MIT · "
            "**19 个 release / 20 个 tag** · **SKILL.md 1,089 个 / 名口径 331 身份（3.29×）/ "
            "内容口径 944 身份（1.15×）**（11-18 记 1,087 / 330）· 9 套 harness 目录 · 15 个 CI 工作流"
        ),
        "score": 92,
        "last_seen_date": "2026-11-23",
        "tags": '["agent-harness", "multi-harness", "skills", "caliber-audit", "variant-vs-copy", "release-discipline"]',
        "recent": """
⭐⭐⭐⭐⭐ **本日对本项目做的是口径审计复测，结论是：11-18 日报的头条发现「1,087 文件 / 330 身份 = 3.30×，最大单一技能被复制 10 份」需要按三层重新解读，⭐⭐⭐⭐⭐ 而其中「被复制 10 份」这一条经实测是**不准确**的。**

**可核验事实一：两套口径在同一棵树上并置（2026-11-23 CST）。**

| 口径 | 定义 | **11-23 实测** | 11-18 发布值 |
|---|---|---:|---:|
| SKILL.md 文件数 | — | **1,089** | 1,087 |
| **名口径** | 身份 = `SKILL.md` 的**父目录名** | **331（3.29×）** | 330（3.30×）✓ 复现 |
| **内容口径** | 身份 = **不同 blob sha 集合** | **944（1.15×）** | 未测 |
| 不同 blob sha 总数 | — | **944** | 942（11-18 记录） |
| 同名身份中出现 ≥2 份的 | — | **273** | 273 ✓ |
| **其中逐字节相同的** | — | **33** | 11-18 记「最大单一技能被复制 10 份」 |
| **其中内容不同的** | — | **240** | 未测 |

⭐⭐⭐⭐⭐ **⭐⭐⭐⭐⭐ 决定性事实：11-18 说「`verification-loop` / `tdd-workflow` / `security-review` / `frontend-patterns` / `coding-standards` / `backend-patterns` 各被复制 10 份」—— 本日实测 `backend-patterns` 是 **10 份副本 / 9 个不同 blob sha**、`coding-standards` 是 **10 份副本 / 9 个不同 blob sha**，⭐⭐⭐⭐⭐ 即「10 份」是**同名身份出现在 10 个目录**，⭐⭐⭐⭐⭐ 而这 10 份里有 9 份是**各自不同内容的 harness 变体**，只有 1 份是原始件。⭐⭐⭐⭐⭐ 因此「被复制 10 份」这个说法在内容层面不成立。**

⭐⭐⭐⭐⭐ **⭐⭐⭐⭐⭐ 而这个修正不是贬低 ECC，反而解释了它为什么好：⭐⭐⭐⭐⭐ 9 个 harness 目录（`.agents` / `.claude-plugin` / `.codebuddy` / `.codex-plugin` / `.cursor` / `.gemini` / `.grok-plugin` / `.kiro` / `.opencode`）⭐⭐⭐⭐⭐ 意味着每个技能都要针对 9 个 harness 各写一份 —— ⭐⭐⭐⭐⭐ **「变体」正是适配层的必要产物，⭐⭐⭐⭐⭐ 而 11-18 把这种必要产物误读成了「复制放大」，⭐⭐⭐⭐⭐ 由此得出的「ECC 的内容层与适配层投入比（3.30×）值得被持续观测」这一条推论也随之失效 —— 因为它的**内容冗余倍数只有 1.15×**，是本队列中第二低的。⭐⭐⭐⭐⭐ 修正后的正确表述是：ECC 的内容层（944 个不同技能内容）与适配层（1,089 个文件）之比是 1.15，⭐⭐⭐⭐⭐ 而「273 个技能有 9 套变体」才是它支持多 harness 的真实代价。**

⭐⭐⭐⭐⭐ **⭐⭐⭐ 修正后的三层判据（本日报建议固化为常规体检项）：**

| 层 | 定义 | **ECC** | `plannotator` | `cursor/plugins` | `claude-trading-skills` | `CLI-Anything` |
|---|---|---:|---:|---:|---:|---:|
| **① 内容冗余倍数** | 文件数 ÷ 不同 blob sha | **1.15×** | 1.00× | 1.27× | 1.12× | 1.15× |
| **② 变体率** | 同名不同内容的身份 ÷ 身份数 | **0.73** | 0.17 | 0.20 | 0.14 | 0.05 |
| **③ 身份跨度** | 同一身份名出现在几个目录 | 273 个身份 ≥2 份 | 4 个 | 60 个 | 10 个 | 4 个 |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 第三点（本日的新事实）：它已离开 Trending 榜单。** ⭐⭐⭐⭐⭐ 实测 11-18 的 25 个仓库中只有 15 个留在 11-23 榜单上，⭐⭐⭐⭐⭐ ECC 是离榜者之一（11-19 快照 306,433⭐ 后未再出现）。⭐⭐⭐⭐⭐ **本日报不主张它的热度下降 —— 305,425 → 306,433 的 6 日净增仅 +1,008（约 +0.3%），⭐⭐⭐⭐⭐ 远低于它此前 11-17 记录的 +66,998，⭐⭐⭐⭐⭐ 但「此前 11-17 的 +66,998 是两个快照点之差而非时间序列增速」这一保留仍然成立，⭐⭐⭐⭐⭐ 本日无法用现有数据判断这个落差是趋势还是快照噪声。**

⭐⭐⭐⭐⭐ **⭐⭐⭐ 第四点：它的分发纪律部分未受影响。** ⭐⭐⭐⭐⭐ 实测 15 个 CI 工作流仍在（含 `generator-generic-ossf-slsa3-publish.yml` / `pr-burst-guard.yml`），⭐⭐⭐⭐⭐ 9 套 harness 目录不变，⭐⭐⭐⭐⭐ 19 release / 20 tag 不变，⭐⭐⭐⭐⭐ 且实测到 `scripts/sync-ecc-to-codex.sh` / `scripts/dev/generate-skill-triggers.js` / `scripts/lib/codex-legacy-sync.js` 等 23 个生成/同步脚本路径 —— ⭐⭐⭐⭐⭐ **即「变体是被脚本生成的」这一点有文件名层面的证据，⭐⭐⭐⭐⭐ 但本日报未读取这些脚本，⭐⭐⭐⭐⭐ 因此不主张它们生成的是「变体」还是「副本」以外的任何东西。**
""",
    },
    "superpowers": {
        "stars": "324,102 stars",
        "stars_delta": (
            "⭐ 2026-11-23 更新（快照 2026-11-23 CST，仓库创建于 2024-10-14T18:20:44Z）："
            "319,255⭐（11-18 快照）→ **324,102⭐**（+4,847，6 日序列 319,255 → 321,277 → 322,015 → "
            "322,789 → 323,655 → 324,102，+1.5%）；forks 28,757 · subs 1,177 · oi 363 · 236 blobs · "
            "Shell / Markdown · **15 个 SKILL.md = 15 个身份（名口径与内容口径均 1.00×）** · "
            "**harness 目录 4 套**（`antigravity` / `claude-code` / `codex` / `opencode`；11-18 为 5 套）· "
            "39 tag / 17 release（0 asset）"
        ),
        "score": 90,
        "last_seen_date": "2026-11-23",
        "tags": '["agent-skills", "zero-replication", "multi-harness", "star-time-series", "methodology", "caliber-audit"]',
        "recent": """
⭐⭐⭐⭐⭐ **本日对本项目做的是口径审计 + 时间序列复测，结论是：它的「零复制」完全复现，但 11-18 日报里「5 套 harness」这一半在 5 天后已变成 4 套 —— 该结论需要降级。**

**可核验事实一：身份口径（两套口径完全一致）。**

| 口径 | **11-23 实测** |
|---|---:|
| SKILL.md 文件数 | **15** |
| 名口径身份 | **15（1.00×）** |
| 内容口径身份 | **15（1.00×）** |
| 不同 blob sha | **15** |
| 同名身份中出现 ≥2 份的 | **0 个** |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 即 15 份技能文件就是 15 份互不相同的内容 —— 没有复制，也没有变体。⭐⭐⭐⭐⭐ 这与 `Claude-BugHunter`（83/83）、`stitch-skills`（16/16）、`ffmpeg-skill`（19/19）、`ag-ui`（23/23）、`chrome-devtools-mcp`（8/8）同属本数据集最健康的一档。**

⭐⭐⭐⭐⭐ **⭐⭐⭐⭐⭐ 但另一处必须诚实记录：harness 目录从 11-18 实测的 5 套变成了 4 套。** ⭐⭐⭐⭐⭐ 11-18 日报把「15 身份 / 5 套 harness 清单 / 复制 1.00×」作为「零复制 + 多 harness 是最健康形态」的证据，⭐⭐⭐⭐⭐ **本日实测该 5 套已降为 4 套（`antigravity` / `claude-code` / `codex` / `opencode`）。⭐⭐⭐⭐⭐ 本日报据此把该结论降级为「多 harness 适配的形态曾出现」，⭐⭐⭐⭐⭐ 并把本日第 4 条趋势的核心判断改为：⭐⭐⭐⭐⭐ **跨 harness 项目中唯一稳定的结构事实不是「harness 目录数」而是「有没有一条别人能直接粘贴运行的安装命令」。⭐⭐⭐⭐⭐ 本项目实测有 2 条 `marketplace add` 命令且 0 条 `npx skills add`。**

⭐⭐⭐⭐⭐ **⭐⭐⭐ 同时，本日第 4 条趋势中的第三个样本 `HKUDS/CLI-Anything` 是反向的：0 套 harness 目录却有 3 条安装命令。⭐⭐⭐⭐⭐ 即 harness 目录与安装命令之间没有稳定的相关性。**

**可核验事实二：首条完整的 star 时间序列。**

| 日期 | 快照 star | 相对前一日 |
|---|---:|---:|
| 2026-11-18 | 319,255 | — |
| 2026-11-19 | 321,277 | **+2,022** |
| 2026-11-20 | 322,015 | +738 |
| 2026-11-21 | 322,789 | +774 |
| 2026-11-22 | 323,655 | +866 |
| 2026-11-23 | **324,102** | +447 |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 形态：「首日冲高 + 回落 + 缓降平台」。⭐⭐⭐⭐⭐ 首日 2,022 是后续均值的 2.9 倍，⭐⭐⭐⭐⭐ 而末日仅 447 —— **即 Trending 榜单本身会制造一个「进入即冲高」的效应，⭐⭐⭐⭐⭐ 这意味着「某项目今天涨得快」几乎不携带信息量（14 个全程在榜仓库中 11 个首日增量高于其后 4 日均值）。⭐⭐⭐⭐⭐ 5 日总增 +4,847（+1.5%），⭐⭐⭐⭐⭐ 而首日一天就占了其中的 42%。**

⭐⭐⭐⭐⭐ **⭐⭐⭐ 另一项值得记录的形态对比：`we-promise/sure` 的逐日增是 +230 / +210 / +204 / +225 / +200（极差 30，占均值 14%），⭐⭐⭐⭐⭐ 而本项目是 +2,022 / +738 / +774 / +866 / +447（极差 1,575，占均值 53%）。⭐⭐⭐⭐⭐ 即「首日冲高型」与「稳定型」在时间序列上是可区分的，⭐⭐⭐⭐⭐ 而后者更难由一次性投放造成。**

**可核验事实三：规模与发布面。**

| 指标 | 实测值 |
|---|---:|
| stars / forks / subs / open issues | 324,102 / 28,757 / **1,177** / 363 |
| blobs | 236（`.md` 112 · `.sh` 53 · `.json` 17 · `.js` 11） |
| tag / release | **39 / 17**（release 全部 0 asset） |
| subs/star | 0.36%（本队列中位数 0.38%） |
| fork/star | 8.9% |
| 安装命令 | `marketplace add https://github.com/obra/superpowers` · `marketplace add obra/superpowers-marketplace` |
| owner | `obra`（账号 **2009-01-09** 创建，本队列最老的账号） |
""",
    },
    "cli-anything": {
        "stars": "62,725 stars",
        "stars_delta": (
            "⭐ 2026-11-23 更新（快照 2026-11-23 CST，仓库创建于 2026-03-08T13:52:57Z）："
            "46,882⭐（08-11 快照）→ **62,725⭐**；**本日首次进入 Trending 日榜**（+687）· "
            "forks 5,689 · subs 232 · oi 285 · **1,872 blobs** · 42,161 KB · Python · Apache-2.0 · "
            "**151 个 SKILL.md / 名口径 82 身份（1.84×）/ 内容口径 131 身份（1.15×）** · "
            "**7 个 CI 工作流**（含 `check-codex-skill.yml` / `check-cursor-plugin.yml` / `check-root-skills.yml` 三个契约检查）· "
            "**0 套 harness 目录但有 3 条安装命令** · 贡献者 `yuh-yang` 290 + `AiMiDi` 43 + `omerarslan0` 33"
        ),
        "score": 89,
        "last_seen_date": "2026-11-23",
        "tags": '["agent-native", "cli-generation", "contract-as-ci", "caliber-audit", "community-hub", "multi-harness"]',
        "recent": """
⭐⭐⭐⭐⭐ **本日为本项目首次建立完整档案（此前仅有一条 2026-08-11 的简略记录），⭐⭐⭐⭐⭐ 并把它确立为本日第 4 条趋势中「契约检查成为标准做法」这条判断的第二个独立样本。**

**可核验事实一（2026-11-23 CST 快照）：**

| 指标 | 实测值 |
|---|---|
| stars / forks / subs / open issues | **62,725** / 5,689 / 232 / 285 |
| 体积 / blobs | 42,161 KB / **1,872** |
| 语言 / 许可 / 创建 / 最后 push | Python / Apache-2.0 / **2026-03-08T13:52:57Z** / 2026-11-20T10:05:15Z |
| homepage | `https://clianything.cc/` |
| **CI 工作流（7 个）** | `check-codex-skill.yml` · `check-cursor-plugin.yml` · `check-root-skills.yml` · `deploy-pages.yml` · `pr-labeler.yml` · `pr-labeler-tests.yml` · `publish-cli-hub.yml` |
| 贡献者 | `yuh-yang` 290 · `AiMiDi` 43 · `omerarslan0` 33 · `furkankoykiran` 31 · `hito0512` 31 · `apireno` 22 · `haorui-harry` 19 · `OGRLEAF` 18 |
| 顶层目录 | `skills/` 71 · `mailchimp/` 49 · `unimol_tools/` 47 · `docs/` 42 · `macrocli/` 40 · `iterm2/` 39 · `freecad/` 36 · `audacity/` 34 · `slay_the_spire_ii/` 34 · `firefly-iii/` 33 · `zotero/` 32 · `live2d/` 31 |
| 扩展名分布 | `.py` **1,267** · `.md` 441 · `.json` 24 · `.sh` 18 · `.yml` 14 |
| README 长度 | **80,335 B**（含 18 个 app 的 demo 章节与 arXiv 技术报告链接 `arxiv.org/abs/2606.03854`） |
| **SKILL.md** | **151 个文件 / 名口径 82 身份（1.84×）/ 内容口径 131 身份（1.15×）** |
| **同名身份中出现 ≥2 份的** | **4 个**（`skills` 67 份 / 67 个不同 sha · `cli-hub-meta-skill` 2 份 · `cli-anything-firefly-iii` 2 份 · `cli-anything-openrefine` 2 份），**逐字节相同的 0 个** |
| **harness 目录** | **0 套** |
| **安装命令** | `pip install cli-anything-hub` · `npx skills add HKUDS/CLI-Anything --list` · `npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y` |
| release / tag | 3 / 3 |

⭐⭐⭐⭐⭐ **⭐⭐⭐⭐⭐ 三个本日报首次测到的事实：**

**事实一：它是「有命令、无 harness 目录」的反向样本。** ⭐⭐⭐⭐⭐ 实测 **0 套 harness 目录**（`.claude` / `.codex` / `.cursor` / `.gemini` 等一个都没有），⭐⭐⭐⭐⭐ **却有 3 条别人能直接粘贴运行的安装命令**，⭐⭐⭐⭐⭐ 且其中两条是 `npx skills add` 协议 —— **即「包内多 harness 清单」与「安装协议」在本项目上是解耦的，⭐⭐⭐⭐⭐ 本日报第 4 条趋势据此判断：唯一稳定的结构事实是安装命令，而不是 harness 目录数。**

**事实二：它是「契约检查」的第二个独立样本。** ⭐⭐⭐⭐⭐ 实测 7 个工作流里有 **3 个是契约检查**：`check-codex-skill.yml` / `check-cursor-plugin.yml` / `check-root-skills.yml` —— ⭐⭐⭐⭐⭐ **即「每个 harness 的产物形态是否符合契约」被做成了每次 CI 必跑的检查。⭐⭐⭐⭐⭐ 这与 11-18 记录的 `alibaba/open-code-review` 的 `plugin-contract.yml` / `action-contract.yml` 是同一模式，⭐⭐⭐⭐⭐ 两个不同机构、两个不同领域（代码评审 vs agent CLI 生成）、同一做法，⭐⭐⭐⭐⭐ **本日报把「契约检查正在成为多 harness 项目的标准做法」列为本日的一条正面发现。**

**事实三：它的「复制」本质上是「为 67 个不同软件各生成一份适配」。** ⭐⭐⭐⭐⭐ 实测 `skills` 这个身份名下有 **67 份 SKILL.md、67 个不同的 blob sha**，⭐⭐⭐⭐⭐ 路径形如 `3MF/agent-harness/cli_anything/threemf/skills/SKILL.md` / `QGIS/agent-harness/cli_anything/qgis/skills/SKILL.md` / `adguardhome/agent-harness/cli_anything/adguardhome/skills/SKILL.md`；⭐⭐⭐⭐⭐ 且实测存在 `.github/scripts/generate_meta_skill.py` 与 `.github/scripts/sync_root_skills.py` 两个生成脚本、⭐⭐⭐⭐⭐ 各 app 目录下还有 `skill_generator.py` / `preview_bundle.py` / `core/generate.py` 等生成器。⭐⭐⭐⭐⭐ **即它的名口径 1.84× 几乎全部来自「按 app 生成的 per-CLI 适配」，而不是内容冗余（内容口径仅 1.15×）。**

⭐⭐⭐⭐⭐ **⭐⭐⭐ 修正后的三层判据定位：`CLI-Anything` = ① 内容冗余 1.15×（低）· ② 变体率 0.05（**最低**）· ③ 身份跨度 4 个。⭐⭐⭐⭐⭐ 即它是本队列里「变体率最低」的项目 —— 它的 151 个文件几乎都是不同 app 的不同技能，⭐⭐⭐⭐⭐ 而不是同一个技能的多个版本。**

**可核验事实四：6 条抽样 issue 全是「具体 app + 具体现象」。**

| issue | 提交者 | 标题 |
|---|---|---|
| `#691` | `ajack13` | fix(libreoffice): declare xmlns:of so Calc formulas evaluate |
| `#690` | `dung997tb` | docs: update Japanese README to current version |
| `#689` | `dung997tb` | docs: add Vietnamese README translation |
| `#688` | `mhmd2520` | fix(blender): resolve the EEVEE engine id across Blender 4.2–5.x |
| `#687` | `mhmd2520` | fix(blender,freecad,shotcut): stop live preview pid checks from killing processes |
| `#686` | `mhmd2520` | [Bug]: [blender/freecad/shotcut] live preview pid check kills the poller on Windows |

⭐⭐⭐⭐⭐ **⭐⭐⭐ 注意 `#690` 与 `#689` 是「文档翻译待补」类 issue —— 这与本数据集 11-16 记录的「issue 的技术含量与定位精度是免费信号」是同一条判断：**多语言文档的翻译进度被公开追踪，本身就是项目活跃度的一个侧面。**

**证据边界：**
- ⭐⭐⭐ ⚠️ **本日报未 clone、未运行任何生成的 CLI、未安装 `cli-anything-hub`、未验证任何一条安装命令可执行。**
- ⭐⭐⭐ ⚠️ **151 个 SKILL.md 的「67 份不同 sha」只证明「不是逐字节相同」**，⭐⭐⭐ ⚠️ 未逐份 diff，⭐⭐⭐ ⚠️ **不主张它们在功能语义上不同。**
- ⭐⭐⭐ ⚠️ **「2,461 个测试通过」「18 个 app 的 demo」「arXiv 技术报告」均为 README 自述**，⭐⭐⭐ ⚠️ **本日报未核验任何一项。**
- ⭐⭐⭐ ⚠️ **8 月 11 日快照到本日的 star 跨度（46,882 → 62,725）跨越了三个多月**，⭐⭐⭐ ⚠️ **不是时间序列增速；⭐⭐⭐ ⚠️ 且本项目本日才首次进入 Trending 榜单，⭐⭐⭐ ⚠️ 故本日报不对其增长做任何速率主张。**
- ⭐⭐⭐ ⚠️ **未核验项**：`check-*.yml` 三个契约检查的具体规则、CLI-Hub 的实际内容与审核流程、67 个 per-CLI 生成物的功能质量、285 个 issue 的正文、`publish-cli-hub.yml` 的发布策略。
""",
    },
}


def update(slug: str, spec: dict) -> None:
    path = PROJ / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise SystemExit(f"{slug}: no frontmatter")
    fm, body = parts[1], parts[2]

    # --- frontmatter field replacement ---
    for field in ("stars", "stars_delta", "score", "last_seen_date", "tags"):
        if field not in spec:
            continue
        value = spec[field]
        if field == "tags":
            new_line = f"tags: {value}"
        elif field == "score":
            new_line = f"score: {value}"
        else:
            new_line = f'{field}: "{value}"'
        pattern = re.compile(rf"^{field}:.*$", re.M)
        if pattern.search(fm):
            fm = pattern.sub(new_line, fm, count=1)
        else:
            fm = fm.rstrip("\n") + "\n" + new_line + "\n"

    # --- insert the new 最近动态 section right before the first '## ' heading ---
    recent = spec["recent"].strip("\n")
    m = re.search(r"^## ", body, re.M)
    if not m:
        raise SystemExit(f"{slug}: no '## ' heading found")
    block = f"\n## 最近动态（2026-11-23）\n\n{recent}\n\n---\n\n"
    body = body[:m.start()] + block.lstrip("\n") + body[m.start():]

    path.write_text(f"---{fm}---{body}", encoding="utf-8")
    print(f"updated projects/{slug}.md  ({len(path.read_text(encoding='utf-8'))} bytes)")


if __name__ == "__main__":
    for slug, spec in UPDATES.items():
        update(slug, spec)
