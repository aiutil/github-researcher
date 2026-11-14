#!/usr/bin/env python3
"""Repair a daily frontmatter whose scalars contain ': ' and were left unquoted.

YAML rejects a plain scalar that contains ': '.  The 2026-10-25 report was
written that way.  This script re-parses the frontmatter with a line-oriented
parser that knows the layout used by this repository:

    stats:
      key: value                 <- indent 2 scalars
    trends:
    - rank: 1                   <- list items at indent 0
      name: value               <- item scalars at indent 2
      projects:
      - item                    <- nested list at indent 2
    key_projects:
    - name: value
      tags:
      - item

Scalar values are re-read with yaml.safe_load so quoting and escapes stay
correct, then the whole frontmatter is re-emitted through yaml.safe_dump.
"""

import sys
from pathlib import Path

import yaml

NESTED_LIST_KEYS = {"projects", "tags"}


def split_kv(line):
    """Split 'key: value' on the FIRST ': ' occurrence.

    A bare 'key:' (a key that opens a nested block) yields (key, "").
    """
    if line.endswith(":"):
        return line[:-1].strip(), ""
    if ": " not in line:
        return None, None
    key, _, value = line.partition(": ")
    return key.strip(), value.strip()


def read_scalar(value):
    """Read one scalar.

    Only quoted values are handed to PyYAML, so escapes are processed while
    plain values stay plain strings (a bare 2026-10-25 must remain a string,
    not become a datetime.date).
    """
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        try:
            parsed = yaml.safe_load(value)
        except yaml.YAMLError:
            return value[1:-1]
        if isinstance(parsed, str):
            return parsed
    return value


def parse(raw):
    data = {}
    stats = {}
    trends = []
    key_projects = []
    section = None
    item = None
    nested_owner = None  # the item dict that owns a pending nested list

    for raw_line in raw.split("\n"):
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip())
        line = raw_line.strip()

        # A "- " line starts either a new mapping item (indent 0) or an
        # element of the nested list named by `nested_owner` (indent 2).
        if line.startswith("- "):
            payload = line[2:].strip()
            if indent == 0:
                nested_owner = None
                if section == "trends":
                    item = {}
                    trends.append(item)
                elif section == "key_projects":
                    item = {}
                    key_projects.append(item)
                else:
                    item = None
                    continue
                key, value = split_kv(payload)
                if key is not None:
                    item[key] = read_scalar(value)
                continue

            if indent == 2 and nested_owner is not None:
                key, value = split_kv(payload)
                if key is None:
                    target = nested_owner.get(nested_owner["__list__"])
                    if target is None:
                        target = []
                        nested_owner[nested_owner["__list__"]] = target
                    target.append(payload)
                else:
                    target = nested_owner.get(nested_owner["__list__"])
                    if target is None:
                        target = []
                        nested_owner[nested_owner["__list__"]] = target
                    target.append(read_scalar(value))
                continue
            continue

        key, value = split_kv(line)
        if key is None:
            continue

        if indent == 0:
            nested_owner = None
            item = None
            if key == "stats":
                section = "stats"
                continue
            if key in ("trends", "key_projects"):
                section = key
                continue
            section = None
            data[key] = read_scalar(value) if value else ""
            continue

        if indent == 2 and section == "stats":
            stats[key] = read_scalar(value)
            continue

        if indent == 2 and item is not None:
            if key in NESTED_LIST_KEYS:
                item["__list__"] = key
                nested_owner = item
                item[key] = []
                continue
            nested_owner = None
            item[key] = read_scalar(value)
            continue

    for group in (trends, key_projects):
        for entry in group:
            entry.pop("__list__", None)

    data["stats"] = stats
    data["trends"] = trends
    data["key_projects"] = key_projects
    return data


def normalise(data):
    for key in ("project_count", "daily_updates", "core_directions"):
        if key in data["stats"]:
            try:
                data["stats"][key] = int(data["stats"][key])
            except (TypeError, ValueError):
                pass

    for trend in data["trends"]:
        for key in ("rank", "score"):
            if key in trend:
                try:
                    trend[key] = int(trend[key])
                except (TypeError, ValueError):
                    pass

    for proj in data["key_projects"]:
        if "score" in proj:
            try:
                proj["score"] = int(proj["score"])
            except (TypeError, ValueError):
                pass
    return data


def main():
    path = Path(sys.argv[1])
    content = path.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise SystemExit("no frontmatter found")

    data = normalise(parse(parts[1]))

    ordered = {
        "title": data.get("title", ""),
        "date": data.get("date", ""),
        "version": data.get("version", "v1"),
        "summary": data.get("summary", ""),
        "hero_badge": data.get("hero_badge", data.get("date", "")),
        "stats": data.get("stats", {}),
        "trends": data.get("trends", []),
        "key_projects": data.get("key_projects", []),
    }

    dumped = yaml.safe_dump(
        ordered, allow_unicode=True, sort_keys=False, default_flow_style=False, width=100000
    )
    path.write_text("---" + dumped + "---" + parts[2], encoding="utf-8")

    check = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
    print("OK title:", check["title"])
    print("date:", check["date"], "| summary len:", len(check["summary"]))
    print("stats:", check["stats"])
    for t in check["trends"]:
        print("  trend rank", t.get("rank"), "score", t.get("score"), t.get("projects"))
    for k in check["key_projects"]:
        print("  KP:", k.get("name"), "|", k.get("href"), "|", k.get("stars"),
              "| tags", len(k.get("tags", [])), "| score", k.get("score"))


if __name__ == "__main__":
    main()
