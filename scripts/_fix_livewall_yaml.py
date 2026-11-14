#!/usr/bin/env python3
"""Fix projects/livewall.md frontmatter.

The repo full name is 'elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop'.
The literal three-hyphen sequence inside the YAML frontmatter terminates the
frontmatter block for every consumer that does content.split('---', 2)
(validate.py, generate_readme.py, generate_pages.py) -- the quoted title is
left unterminated and YAML parsing fails.

Fix: in the double-quoted YAML scalars, encode the hyphen run as
\\u002D\\u002D\\u002D.  YAML double-quoted style decodes \\uXXXX escapes, so the
parsed value is byte-identical to the real repo path while the raw file no
longer contains a literal '---' inside the frontmatter block.
"""
from pathlib import Path
import re
import yaml

p = Path("/home/lohasle/aiutil-github-researcher/projects/livewall.md")
c = p.read_text(encoding="utf-8")

REAL = "elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop"
ESC = "elunboundfiremail/LiveWall\\u002D\\u002D\\u002DLive-Wallpaper-For-Desktop"

lines = c.split("\n")
assert lines[0].strip() == "---", "file does not start with ---"
end = None
for i in range(1, len(lines)):
    if lines[i].strip() == "---":
        end = i
        break
assert end is not None, "no closing --- found"

fm_lines = []
for l in lines[1:end]:
    stripped = l.lstrip()
    if stripped.startswith("title:"):
        l = f'title: "{ESC}"'
    elif stripped.startswith("url:"):
        l = f'url: "https://github.com/{ESC}"'
    elif "---" in l:
        l = l.replace("---", "\\u002D\\u002D\\u002D")
    fm_lines.append(l)

out = "\n".join(lines[:1] + fm_lines + lines[end:])
p.write_text(out, encoding="utf-8")

parts = out.split("---", 2)
assert len(parts) == 3, "frontmatter split failed"
fm = yaml.safe_load(parts[1])
print("YAML OK")
print("  title =", fm.get("title"))
print("  url   =", fm.get("url"))
assert fm.get("title") == REAL, f"title mismatch: {fm.get('title')!r}"
assert fm.get("url") == "https://github.com/" + REAL, f"url mismatch: {fm.get('url')!r}"
assert "---" not in "\n".join(fm_lines), "literal --- still inside frontmatter"
print("ASSERTIONS PASSED: parsed values byte-identical to the real repo path")
