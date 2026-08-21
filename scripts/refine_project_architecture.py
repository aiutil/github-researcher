#!/usr/bin/env python3
"""Refine profile architecture briefs from the evidence already in each profile."""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
TICK = chr(96) * 3
API = "https://api.minimaxi.com/anthropic/v1/messages"


def message(profile: str) -> str:
    return f"""你是服务于架构师和技术决策者的开源研究编辑。只能使用下面的项目档案中已有的事实；不能补写 README 未证实的组件、性能、协议或部署方式。

请输出且只输出下面格式：
<brief>
一张 4 行的 Markdown 表格，列为“决策问题 | 研究判断 | 证据边界”。四行依次是系统边界、主路径、关键权衡、最小 PoC。判断必须针对项目，不得泛泛而谈。
</brief>
<mmd>
一段可由 Mermaid 11 解析的 flowchart（LR 或 TB）。4 到 8 个节点，包含项目核心、至少一个外部边界和一个状态/控制/风险边界。只画档案中明确描述的组件；信息不充分的节点必须写“待核验”。不要加 Markdown 代码围栏。
</mmd>

项目档案：
{profile[:18000]}"""


def call(profile: str) -> tuple[str, str]:
    key = os.environ["MINIMAX_CN_API_KEY"]
    payload = json.dumps({
        "model": "MiniMax-M3",
        "max_tokens": 1100,
        "messages": [{"role": "user", "content": message(profile)}],
    }).encode()
    request = urllib.request.Request(API, data=payload, headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(request, timeout=120) as response:
        data = json.loads(response.read().decode())
    content = "".join(part.get("text", "") for part in data.get("content", []) if part.get("type") == "text")
    brief = re.search(r"<brief>\s*(.*?)\s*</brief>", content, re.S | re.I)
    mmd = re.search(r"<mmd>\s*(.*?)\s*</mmd>", content, re.S | re.I)
    if not brief:
        brief = re.search(r"((?:\|[^\n]+\|\n){5,})", content)
    if not mmd:
        mmd = re.search(r"((?:flowchart|graph)\s+(?:LR|RL|TB|BT)[\s\S]*)", content, re.I)
    if not brief or not mmd or not any(token in mmd.group(1).lower() for token in ("flowchart", "graph")):
        raise ValueError("model response did not contain a valid brief and flowchart")
    return brief.group(1).strip(), mmd.group(1).strip().strip(chr(96)).replace("mermaid\n", "", 1)


def replace_section(text: str, heading: str, next_heading: str, value: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        raise ValueError(f"missing section: {heading}")
    return text[:start] + value.rstrip() + "\n\n" + text[end:]


def refine(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    brief, mmd = call(text)
    updated_brief = "## 架构师速览\n\n" + brief
    updated_mmd = f"""## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

{TICK}mermaid
{mmd}
{TICK}"""
    text = replace_section(text, "## 架构师速览", "## 架构启发", updated_brief)
    if "## 架构图（MMD）" in text:
        text = replace_section(text, "## 架构图（MMD）", "## 定位判断", updated_mmd)
    else:
        start = text.find(TICK + "mermaid")
        end = text.find(TICK, start + len(TICK + "mermaid"))
        if start < 0 or end < 0:
            raise ValueError("missing Mermaid block")
        text = text[:start] + updated_mmd + text[end + len(TICK):]
    path.write_text(text, encoding="utf-8")
    return path.name, "ok"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--names-file")
    args = parser.parse_args()
    if "MINIMAX_CN_API_KEY" not in os.environ:
        raise SystemExit("MINIMAX_CN_API_KEY is required")
    if args.names_file:
        files = [PROJECTS / name for name in Path(args.names_file).read_text(encoding="utf-8").splitlines() if name]
    else:
        files = sorted(PROJECTS.glob("*.md"))[args.start:args.start + args.limit]
    if not files:
        return
    failed = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(refine, path): path for path in files}
        for future in as_completed(futures):
            path = futures[future]
            try:
                print(*future.result())
            except Exception as exc:
                failed.append(path.name)
                print(path.name, "failed", str(exc)[:160])
    print(json.dumps({"requested": len(files), "failed": failed}, ensure_ascii=False))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
