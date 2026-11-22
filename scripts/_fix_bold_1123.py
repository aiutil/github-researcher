#!/usr/bin/env python3
"""Normalise bold markers in the 2026-11-23 frontmatter (line-level, lossless).

generate_readme.py renders a trend as ``**{name}**`` and the summary as
``**{summary}**``.  When `name`/`summary` itself ends with ``**`` the two
markers collapse into a literal ``****`` in the generated README.

The fix must remove BOTH halves of the offending pair: dropping only the
trailing ``**`` would leave the opening ``**`` unmatched, which the
generator then renders as a stray single ``*``.

Rules applied to the `summary:` line and every `name:` line under `trends:`:
  1. if the value ends with a ``**`` pair, delete that pair together with
     its matching opening marker
  2. the remaining ``**`` markers must be balanced (even count)
"""
import re
from pathlib import Path

import yaml

DAILY = Path(__file__).resolve().parents[1] / "daily" / "2026-11-23.md"


def marker_positions(text: str):
    """Return the indices of every '**' marker, left to right."""
    out = []
    i = 0
    while True:
        j = text.find("**", i)
        if j < 0:
            return out
        out.append(j)
        i = j + 2


def fix_value(value: str) -> str:
    out = value.rstrip()
    # find the last marker pair
    while True:
        positions = marker_positions(out)
        if len(positions) < 2:
            break
        last = positions[-1]
        # is the final marker the last thing in the string?
        if out[last + 2:].strip() != "":
            break
        # markers pair up as (0,1), (2,3), ... so the partner of `last`
        # is positions[-2] when the count is even
        if len(positions) % 2 == 0:
            partner = positions[-2]
            out = out[:partner] + out[partner + 2:last] + out[last + 2:]
            out = out.rstrip()
            continue
        # odd count: the final marker is unmatched -> demote it to '*'
        out = out[:last] + "*" + out[last + 2:]
        break
    return out


def main() -> None:
    raw = DAILY.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    fm_text, body = parts[1], parts[2]
    lines = fm_text.split("\n")

    in_trends = False
    changed = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        if re.match(r"^trends:\s*$", stripped):
            in_trends = True
            continue

        target = None
        if stripped.startswith("summary:"):
            target = "summary"
        elif in_trends and stripped.startswith("name:"):
            target = "trend-name"

        # A top-level key (indent 0) ends the trends block.
        if in_trends and indent == 0 and re.match(r"^[a-z_]+:", stripped):
            in_trends = False
            target = None

        if not target:
            continue

        prefix, _, value = line.partition(":")
        raw_value = value.strip()
        if len(raw_value) >= 2 and raw_value[0] == raw_value[-1] and raw_value[0] in "\"'":
            quote = raw_value[0]
            inner = raw_value[1:-1]
            new_inner = fix_value(inner)
        else:
            quote = ""
            inner = raw_value
            new_inner = fix_value(inner)

        if new_inner == inner:
            continue

        new_line = f"{prefix}: {quote}{new_inner}{quote}" if quote else f"{prefix}: {new_inner}"
        lines[i] = new_line
        changed += 1
        print(f"line {i + 1} ({target}) fixed")

    new_fm = "\n".join(lines)
    DAILY.write_text(f"---{new_fm}---{body}", encoding="utf-8")

    check = yaml.safe_load(DAILY.read_text(encoding="utf-8").split("---", 2)[1])
    s = check["summary"]
    print(f"\nsummary: ** count={s.count('**')}  ends**={s.rstrip().endswith('**')}  "
          f"stray*={s.count('*') - 2 * s.count('**')}")
    for t in check["trends"]:
        n = t["name"]
        print(f"  trend {t['rank']}: ** count={n.count('**')}  ends**={n.rstrip().endswith('**')}  "
              f"stray*={n.count('*') - 2 * n.count('**')}")
    print(f"key_projects={len(check['key_projects'])}  changed={changed}")


if __name__ == "__main__":
    main()
