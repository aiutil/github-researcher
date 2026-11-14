#!/usr/bin/env python3
'''Align the remaining zero-breach references in daily/2026-11-08.md with the
verified upstream/downstream facts.'''

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "daily" / "2026-11-08.md"
c = p.read_text(encoding="utf-8")

OLD = (
    "- ⭐⭐⭐⭐ **`interplains/zero-breach` 与 `interplains/Zero-Breach-Toolkit` 的双仓库事实，"
    "是本窗口通过 `id` / `fork` / `parent` / `created_at` / release 列表 / 文件存在性六个字段交叉确认的**；"
    "本报告已据此指出 `projects/zero-breach.md` 的指向错误，但**该档案的正文与 URL 修正属于独立的一处档案维护工作，"
    "已在本日报同步记录，未擅自改写历史日报正文**。"
)
NEW = (
    "- ⭐⭐⭐⭐ **`interplains/zero-breach` 与 `interplains/Zero-Breach-Toolkit` 的上下游事实，"
    "是本窗口通过 `id` / `fork` / `parent` / `created_at` / release 列表 / 文件存在性六个字段交叉确认的**；"
    "本报告已据此**更正 `projects/zero-breach.md` 的 `stars`（4,475 → 1,218）与 `stars_delta`**"
    "（该档案正文描述的始终是上游，故只更正元数据），并**为下游另建独立档案 "
    "`projects/zero-breach-toolkit.md`**；⭐⭐⭐ **2026-10-30 日报正文未被改写** —— "
    "历史日报记录保留原样，纠错以本档案与本日报的更正说明为准。"
)

if OLD in c:
    c = c.replace(OLD, NEW)
    p.write_text(c, encoding="utf-8")
    print("daily/2026-11-08.md: evidence-boundary bullet rewritten")
else:
    print("daily/2026-11-08.md: bullet NOT found")

import yaml

meta = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
print("YAML OK:", meta["title"], "|", meta["stats"]["project_count"], "projects")
