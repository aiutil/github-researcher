#!/usr/bin/env python3
'''Correct the stars_delta of projects/zero-breach.md.

Verified 2026-11-08: `interplains/zero-breach` (id 1424399708) and
`interplains/Zero-Breach-Toolkit` (id 1433297111) are two independently
created repositories, NOT a rename.  The archive body describes the UPSTREAM
repo correctly (its README quotes match `zero-breach`), so only the
stars_delta / metadata claims need correcting.

Upstream now: 1,218 stars / 97 forks / 13 subs / 9 releases (v0.1.0..v0.1.8) /
499 KB / 57 commits / Apache-2.0 / pushed 2026-10-20T14:26:41Z (unchanged since
2026-10-20, i.e. 19 days without a push).
'''

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "projects" / "zero-breach.md"
c = p.read_text(encoding="utf-8")

NEW_DELTA = (
    'stars_delta: "⭐ 2026-10-20 建档时 402⭐ → 2026-11-08 快照 **1,218⭐**'
    "（19 天 +203%，fork 97 / subs 13 / oi 0 · Apache-2.0 · Python · 499 KB · 57 commits · "
    "`pushed_at` 仍停在 **2026-10-20T14:26:41Z**，即已 19 天无新提交）；"
    "**⭐⭐⭐ 2026-11-08 更正：此前本档案的 `stars_delta` 记录了「2026-11-06 快照 4,475⭐ · "
    "12,477 KB · fork 473 / subs 42 · oi 7」并称本仓库「已由 `interplains/Zero-Breach-Toolkit` "
    "改名为 `interplains/zero-breach`」，这一认定是错的 —— 经 `id` / `fork` / `parent` / "
    "`created_at` / release 列表四字段交叉确认，两个路径是**各自独立创建的���同仓库**"
    "（`interplains/zero-breach` = `id 1424399708`，创建 2026-10-18T13:22:34Z；"
    "`interplains/Zero-Breach-Toolkit` = `id 1433297111`，创建 2026-10-25T14:41:34Z；"
    "两者 `fork=False` 且 `parent=None`），**不是改名关系**；**⭐⭐⭐⭐⭐ 4,475⭐ / 12,477 KB / "
    "fork 473 / subs 42 / oi 7 这组数字全部属于下游的 `Zero-Breach-Toolkit`"
    "（2026-11-08 实测 4,553⭐ / 12,477 KB / fork 480 / subs 44 / oi 8 / 23 个 release，"
    "最新 v2.0.6）**，而本档案的正文自始至终描述的是**上游** `zero-breach`"
    "（其 README 原文「no admin, no dependencies」「Tested on Windows, macOS and Linux "
    "(Python 3.8–3.12) in CI」「A clean result is not a clean bill of health」等均与上游吻合，"
    "且 `PRIVACY.md` / `docs/VERIFYING.md` 这两份文件**只存在于下游 Toolkit**，上游两者皆无）；"
    "**⭐⭐ 另有一处记录错误：2026-10-30 日报称上游「`releases` 0 个」，实测上游有 **9 个 release**"
    "（v0.1.0 → v0.1.8，每个 19 个 asset，含 `release-signatures/v0.1.x/` 下的 "
    "`SHA256SUMS.txt` + `.asc` + `archivegenocide-signing-key.asc` + `zero-breach.py.asc`），"
    "且上游 `pushed_at` 自 2026-10-20 起未动，因此这些 release 在 2026-10-30 当天就已存在**；"
    "**⭐⭐⭐⭐ 教训与本日报记录的「`created_at` 会说谎」「改名时间戳」同族：**"
    "GitHub 的旧路径在改名后仍可解析，因此「旧路径能打开」不能证明「两者是同一个仓库」；"
    "**判定改名必须比对 `id` 与 `parent`，而不是比对路径或描述**；"
    "**⭐⭐⭐⭐⭐ 本档案现已更正为上游 `interplains/zero-breach` 的真实数据，"
    "下游 `Zero-Breach-Toolkit` 已另建独立档案 `projects/zero-breach-toolkit.md`**"
)

lines = c.split("\n")
for i, ln in enumerate(lines):
    if ln.startswith("stars_delta:"):
        lines[i] = NEW_DELTA
        print(f"projects/zero-breach.md: stars_delta replaced (line {i + 1})")
        break
else:
    raise SystemExit("stars_delta line not found")

c = "\n".join(lines)

# Also fix the "为什么值得关注" paragraph's stale claim about the rename.
old_frag = "仓��已由 `interplains/Zero-Breach-Toolkit` 改名为 `interplains/zero-breach`"
if old_frag in c:
    c = c.replace(old_frag, "本仓库与下游 `interplains/Zero-Breach-Toolkit` 是两个各自独立创建的仓库")
    print("projects/zero-breach.md: body rename claim corrected")

p.write_text(c, encoding="utf-8")

import yaml

meta = yaml.safe_load(c.split("---", 2)[1])
print("  stars field:", meta.get("stars"))
print("  url field:", meta.get("url"))
