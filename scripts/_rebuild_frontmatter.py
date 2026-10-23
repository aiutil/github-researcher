#!/usr/bin/env python3
"""Rebuild a daily report frontmatter into guaranteed-valid YAML.

Reads the loosely-structured frontmatter produced by hand editing, recovers the
field values, and re-emits them with yaml.safe_dump so quoting is always
correct.  Usage: python3 scripts/_rebuild_frontmatter.py daily/YYYY-MM-DD.md
"""

import sys
import yaml

LIST_KEYS = {"trends", "key_projects", "tags"}
SCALAR_KEYS = {"title", "date", "version", "summary", "hero_badge"}
STATS_KEYS = {"project_count", "daily_updates", "core_directions", "weekly_stars"}


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1]
    if len(value) >= 2 and value[0] == '"':
        return value[1:]
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1]
    return value


def parse_flow_list(value: str) -> list:
    value = value.strip()
    if not value.startswith("["):
        return []
    inner = value[1:-1]
    items = []
    for chunk in inner.split(","):
        chunk = chunk.strip()
        if chunk:
            items.append(unquote(chunk))
    return items


def recover(fm_text: str) -> dict:
    """Recover the frontmatter structure from hand-written lines."""
    data = {}
    stats = {}
    trends = []
    key_projects = []
    current_list = None
    current_item = None

    for raw in fm_text.split("\n"):
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()

        if indent == 0:
            if ":" not in line:
                continue
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if key == "stats":
                current_list = "stats"
                current_item = stats
                continue
            if key in LIST_KEYS:
                current_list = key
                current_item = None
                if key == "trends":
                    trends = []
                elif key == "key_projects":
                    key_projects = []
                continue
            current_list = None
            current_item = None
            if value:
                data[key] = unquote(value)
            else:
                data[key] = ""
            continue

        if indent == 2 and line.startswith("- "):
            current_item = {}
            if current_list == "trends":
                trends.append(current_item)
            elif current_list == "key_projects":
                key_projects.append(current_item)
            line = line[2:].strip()
            if ":" not in line:
                continue
            key, _, value = line.partition(":")
            current_item[key.strip()] = unquote(value)
            continue

        if indent == 2 and ":" in line and current_list == "stats":
            key, _, value = line.partition(":")
            stats[key.strip()] = unquote(value)
            continue

        if indent == 4 and ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if current_list == "stats":
                stats[key] = unquote(value)
            elif current_item is not None:
                current_item[key] = unquote(value)
            continue

    data["stats"] = stats
    data["trends"] = trends
    data["key_projects"] = key_projects
    return data


def main() -> None:
    path = sys.argv[1]
    content = open(path, encoding="utf-8").read()
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise SystemExit("no frontmatter found")

    data = recover(parts[1])

    # Normalise: stats numeric fields stay ints, weekly_stars stays a string.
    for key in ("project_count", "daily_updates", "core_directions"):
        if key in data["stats"]:
            try:
                data["stats"][key] = int(data["stats"][key])
            except (TypeError, ValueError):
                pass

    # trends: rank/score ints, projects list
    for trend in data["trends"]:
        for key in ("rank", "score"):
            if key in trend:
                try:
                    trend[key] = int(trend[key])
                except (TypeError, ValueError):
                    pass
        if "projects" in trend:
            trend["projects"] = parse_flow_list(str(trend["projects"]))

    # key_projects: score int, tags list
    for proj in data["key_projects"]:
        if "score" in proj:
            try:
                proj["score"] = int(proj["score"])
            except (TypeError, ValueError):
                pass
        if "tags" in proj:
            proj["tags"] = parse_flow_list(str(proj["tags"]))

    ordered = {
        "title": data.get("title", ""),
        "date": data.get("date", ""),
        "version": data.get("version", "v1"),
        "summary": data.get("summary", ""),
        "hero_badge": data.get("hero_badge", data.get("date", "")),
        "stats": data["stats"],
        "trends": data["trends"],
        "key_projects": data["key_projects"],
    }

    dumped = yaml.safe_dump(
        ordered, allow_unicode=True, sort_keys=False, default_flow_style=False, width=100000
    )
    open(path, "w", encoding="utf-8").write("---" + dumped + "---" + parts[2])

    # Verify
    check = yaml.safe_load(open(path, encoding="utf-8").read().split("---", 2)[1])
    print("OK title:", check["title"])
    print("trends:", len(check["trends"]))
    for t in check["trends"]:
        print("   rank", t.get("rank"), "score", t.get("score"), t.get("projects"))
    for k in check["key_projects"]:
        print("   KP:", k.get("name"), "|", k.get("href"), "|", k.get("stars"), "| tags", len(k.get("tags", [])))
    print("stats:", check["stats"])
    print("summary len:", len(check["summary"]))


if __name__ == "__main__":
    main()
