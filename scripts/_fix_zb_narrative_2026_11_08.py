#!/usr/bin/env python3
'''Correct the zero-breach narrative in daily/2026-11-08.md, indexes/trend-index.md
and daily-report.md now that the upstream/downstream relationship is verified.

Verified 2026-11-08:
  interplains/zero-breach        id=1424399708  created 2026-10-18  1,218*  9 rel
  interplains/Zero-Breach-Toolkit id=1433297111  created 2026-10-25  4,553*  23 rel
  (* stars at 2026-11-08 snapshot)
Both fork=False, parent=None -> two independently created repositories.
'''

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_DAILY = (
    "⭐⭐⭐⭐⭐ **对研究者而言，这意味着「GitHub 上新仓库的 star 分布」这个数据源本身已被污染到不能单独用于趋势判断**；"
    "对使用者而言，空仓库里不会有任何东西可下载，但描述会引导到别处。"
)

NEW_DAILY = OLD_DAILY  # unchanged, kept for clarity

# ---- 1. daily/2026-11-08.md : replace the Risk-4 paragraph ----------------
daily = ROOT / "daily" / "2026-11-08.md"
c = daily.read_text(encoding="utf-8")

old_risk = re.search(
    r"⭐⭐⭐⭐ \*\*风险四：一个已归档项目的档案指向了错误的仓库。\*\*.*?(?=\n\n⭐⭐⭐⭐⭐ \*\*机遇一)",
    c,
    re.S,
)
new_risk = """⭐⭐⭐⭐⭐ **风险四：一个已归档项目的档案混入了另一个仓库的数据 —— 而它的成因不是「改名」，是「上下游」。**
本日报核查持续跟踪项时发现：2026-10-30 日报把 `interplains/Zero-Breach-Toolkit` 的数据（4,475⭐ / 12,477 KB / fork 473 / subs 42 / oi 7 / v0.1.13）写进了上游 `interplains/zero-breach` 的档案，并把两者描述为「仓库已由 `interplains/Zero-Breach-Toolkit` **改名为** `interplains/zero-breach`（GitHub 会重定向旧路径）」。⭐⭐⭐⭐⭐ **经 `id` / `fork` / `parent` / `created_at` / release 列表五字段交叉确认，两者是各自独立创建的不同仓库** —— `interplains/zero-breach` = `id 1424399708`（创建 2026-10-18T13:22:34Z，1,218⭐，9 个 release v0.1.0–v0.1.8，499 KB，57 commits），`interplains/Zero-Breach-Toolkit` = `id 1433297111`（创建 2026-10-25T14:41:34Z，**4,553⭐**，23 个 release v0.1.0–v2.0.6，12,477 KB，70 commits），**两者 `fork=False` 且 `parent=None`**。⭐⭐⭐⭐⭐ **判定依据是文件存在性**：`PRIVACY.md` 与 `docs/VERIFYING.md` **只存在于下游 Toolkit**，上游两者皆无；⭐⭐⭐⭐⭐ **而 `projects/zero-breach.md` 的正文自始至终描述的是上游**（其 README 引文「no admin, no dependencies」「Tested on Windows, macOS and Linux (Python 3.8–3.12) in CI」「A clean result is not a clean bill of health」均与上游吻合）—— **即：档案的正文是对的，元数据是错的。** ⭐⭐⭐⭐⭐ **本日报已据此更正 `projects/zero-breach.md` 的 `stars` 与 `stars_delta`，并为下游另建独立档案 `projects/zero-breach-toolkit.md`。** ⭐⭐⭐⭐⭐ **而这次纠错反而证实了 2026-10-30 日报自己记下的那句观察**：「上游负责研究，下游负责可用，而 star 记在下游」—— 上游 9 个 release 停在 10-20（19 天无 push），下游 10 天内从 v0.1.0 迭代到 v2.0.6 并新增 27 种语言与 Android / iPhone 备份支持；⭐⭐⭐⭐⭐ **教训与本日报记录的「`created_at` 会说谎」「改名时间戳」同族：GitHub 的旧路径在改名后仍可解析，因此「旧路径能打开」不能证明「两者是同一个仓库」；判定改名必须比对 `id` 与 `parent`，而不是比对路径或描述。**

"""

if old_risk:
    c = c[: old_risk.start()] + new_risk + c[old_risk.end() :]
    daily.write_text(c, encoding="utf-8")
    print("daily/2026-11-08.md: risk-4 paragraph rewritten")
else:
    print("daily/2026-11-08.md: risk-4 paragraph NOT found")

# ---- 2. trend-index.md : replace the zero-breach row ----------------------
ti = ROOT / "indexes" / "trend-index.md"
t = ti.read_text(encoding="utf-8")
old_row_re = re.compile(r"\| `interplains/zero-breach` \|.*?\n")
new_row = (
    "| `interplains/zero-breach` | **档案更正（上游）** | "
    "⭐⭐⭐⭐⭐ 本档案此前的 `stars_delta` 记的是**下游** `Zero-Breach-Toolkit` 的数据（4,475⭐ / 12,477 KB / "
    "fork 473 / subs 42 / v0.1.13）并称两者是改名关系 —— **经 `id` / `fork` / `parent` / `created_at` / "
    "release 列表五字段交叉确认，两者各自独立创建（`id 1424399708` vs `id 1433297111`，均 `fork=False` / "
    "`parent=None`）**。本档案正文描述的始终是**上游**，故只更正元数据：**1,218⭐** ⑂97 · subs 13 · oi 0 · "
    "499 KB · 57 commits · **9 个 release（v0.1.0–v0.1.8，每个 19 个 asset）** · "
    "`pushed_at` 仍停在 **2026-10-20T14:26:41Z（19 天无 push）**。⭐⭐ 另更正 2026-10-30 日报「上游 releases 0 个」"
    "的记录 —— 实测为 9 个。下游已另建 `projects/zero-breach-toolkit.md` |\n"
)
t2, n = old_row_re.subn(new_row, t, count=1)
if n:
    ti.write_text(t2, encoding="utf-8")
    print("indexes/trend-index.md: zero-breach row replaced")
else:
    print("indexes/trend-index.md: zero-breach row NOT found")

# ---- 3. daily-report.md : fix the summary sentence ------------------------
dr = ROOT / "daily-report.md"
d = dr.read_text(encoding="utf-8")
old_sum = (
    "⭐⭐⭐⭐⭐ **同日另有一项对档案本身的修正**：`interplains/zero-breach` 与 `interplains/Zero-Breach-Toolkit` "
    "经 `id`/`fork`/`parent`/`created_at`/release 列表/文件存在性六字段交叉确认是**两个不同仓库**"
    "（1,218⭐ vs 4,550⭐），而 `projects/zero-breach.md` 的正文与 URL 指向的是前者、内容却描述后者"
    "（`PRIVACY.md` 与 `docs/VERIFYING.md` 只存在于后者）—— "
    "**这是「`created_at` 会说谎」「改名时间戳」那一族问题的第 N 例，且更严重：归档档案本身指向了错误的仓库。**"
)
new_sum = (
    "⭐⭐⭐⭐⭐ **同日另有一项对档案本身的修正**：2026-10-30 日报把下游 `interplains/Zero-Breach-Toolkit` 的数据"
    "（4,475⭐ / 12,477 KB / fork 473 / subs 42 / v0.1.13）写进了上游 `interplains/zero-breach` 的档案，"
    "并称两者是「改名」关系 —— **经 `id`/`fork`/`parent`/`created_at`/release 列表五字段交叉确认，"
    "两者是各自独立创建的上下游（`id 1424399708` vs `id 1433297111`，均 `fork=False` / `parent=None`）**，"
    "而 `PRIVACY.md` 与 `docs/VERIFYING.md` 只存在于下游；**本档案的正文自始至终描述的是上游（正文是对的、元数据是错的）**，"
    "已更正 `stars`/`stars_delta` 并为下游另建独立档案 —— "
    "⭐⭐⭐⭐ **这次纠错反而证实了 10-30 日报自己记下的那句观察：「上游负责研究，下游负责可用，而 star 记在下游」**"
    "（上游 9 个 release 停在 10-20、19 天无 push；下游 10 天内 v0.1.0→v2.0.6、23 个 release、4,553⭐）；"
    "⭐⭐⭐⭐⭐ **教训与本日报记录的「`created_at` 会说谎」「改名时间戳」同族：GitHub 的旧路径在改名后仍可解析，"
    "因此「旧路径能打开」不能证明「两者是同一个仓库」；判定改名必须比对 `id` 与 `parent`，而不是比对路径或描述。**"
)
if old_sum in d:
    d = d.replace(old_sum, new_sum)
    dr.write_text(d, encoding="utf-8")
    print("daily-report.md: summary sentence rewritten")
else:
    print("daily-report.md: summary sentence NOT found (may already be updated)")
