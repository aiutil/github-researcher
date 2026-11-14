#!/usr/bin/env python3
"""Strip a trailing bold run from daily trend names.

generate_readme.py wraps trend names as ``**{name}**``; a name that already
ends with ``**`` produces ``****`` which renders as literal asterisks.

Usage: python3 scripts/_fix_trend_trailing_bold.py daily/YYYY-MM-DD.md
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rebuild_frontmatter import dump_frontmatter, load_frontmatter  # noqa: E402


def main() -> None:
    path = Path(sys.argv[1])
    fm, body = load_frontmatter(path)

    changed = 0
    for trend in fm.get("trends", []) or []:
        name = trend.get("name", "")
        if name.endswith("**"):
            trend["name"] = name[:-2].rstrip()
            changed += 1

    if not changed:
        print("nothing to fix")
        return

    dump_frontmatter(path, fm, body)
    print(f"fixed {changed} trend names")


if __name__ == "__main__":
    main()
