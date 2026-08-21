#!/usr/bin/env python3
"""Add an evidence-bounded architect brief and Mermaid diagram to every profile."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
TICK = chr(96) * 3


def frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    try:
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError:
        return {}


def classify(meta: dict, body: str) -> str:
    text = " ".join([str(meta.get("category", "")), " ".join(meta.get("tags", [])), body]).lower()
    if any(word in text for word in ("agent", "llm", "assistant", "mcp", "workflow")):
        return "agent"
    if any(word in text for word in ("rag", "retrieval", "database", "data", "crawler", "search")):
        return "data"
    if any(word in text for word in ("kubernetes", "container", "sandbox", "runtime", "cloud", "microvm", "infra")):
        return "platform"
    if any(word in text for word in ("security", "cve", "exploit", "auth", "policy", "compliance")):
        return "security"
    if any(word in text for word in ("react", "frontend", "ui", "design", "web", "mobile")):
        return "application"
    return "tool"


MODELS = {
    "agent": (
        "入口渠道、模型供应商、工具/数据源之间的编排层",
        "请求 → 编排/运行时 → 模型与工具调用 → 会话或状态回写",
        "扩展速度与权限、可观测性、供应商耦合之间的平衡",
        "先在单一渠道、最小工具权限和可审计日志下验证，再扩大接入面",
        """flowchart LR
    U[使用者或上游系统] --> I[入口与身份边界]
    I --> C[项目编排与运行时]
    C --> M[模型或推理服务]
    C --> T[工具与外部系统]
    C --> S[会话 状态 审计]
    M --> C
    T --> C""",
    ),
    "data": (
        "数据源、处理/检索核心与消费应用之间的数据产品边界",
        "数据源 → 采集/规范化 → 项目核心能力 → 索引或存储 → 消费接口",
        "新鲜度、召回/准确性、成本与数据治理之间的平衡",
        "选一个可审计数据集，先测质量、延迟和失败可恢复性，再扩展来源",
        """flowchart LR
    D[公开或私有数据源] --> I[采集 解析 规范化]
    I --> C[项目核心处理]
    C --> S[索引 存储 缓存]
    S --> A[应用或 API 消费者]
    C --> O[质量 观测 治理]""",
    ),
    "platform": (
        "调用方、控制面、执行数据面和基础设施资源之间的分层边界",
        "请求 → 控制面策略/调度 → 执行单元 → 资源或持久化状态",
        "隔离、弹性、运维复杂度和资源效率之间的平衡",
        "以一个隔离执行单元或工作负载压测启动、恢复、失败隔离和观测能力",
        """flowchart TB
    U[调用方或 CI] --> API[项目 API 与控制面]
    API --> P[策略 调度 生命周期]
    P --> W[执行单元或数据面]
    W --> R[计算 网络 存储资源]
    P --> O[审计 指标 日志]
    R --> S[持久化或外部服务]""",
    ),
    "security": (
        "不可信输入、策略决策、受保护资源和审计证据之间的信任边界",
        "输入/事件 → 检测或策略 → 处置/隔离 → 审计与修复闭环",
        "检测覆盖率、误报成本、可操作性与安全边界强度之间的平衡",
        "在隔离环境验证检测与阻断路径；不把研究或 PoC 代码当作生产安全控制",
        """flowchart LR
    I[不可信输入或安全事件] --> D[项目检测 分析]
    D --> P[策略与风险判定]
    P --> R[隔离 修复 或告警]
    P --> A[审计证据]
    R --> S[受保护系统]
    A --> O[安全运营闭环]""",
    ),
    "application": (
        "用户体验层、领域状态、服务接口与扩展/数据依赖之间的应用边界",
        "用户交互 → UI/状态管理 → 项目核心逻辑 → 服务或数据依赖",
        "交互速度、状态一致性、可扩展性和后端耦合之间的平衡",
        "用一个真实用户路径验证状态边界、错误恢复与外部依赖降级，而非只看界面",
        """flowchart LR
    U[用户或客户端] --> UI[项目 UI 与交互层]
    UI --> C[状态与领域核心]
    C --> API[服务 API 或运行时]
    API --> D[数据与外部能力]
    C --> O[错误 监测 反馈]""",
    ),
    "tool": (
        "开发者/自动化入口、公共接口、核心能力、宿主运行时和扩展点之间的边界",
        "开发者或 CI → CLI/API → 项目核心 → 宿主运行时或外部集成",
        "易用性、可移植性、扩展能力与运行时/供应链风险之间的平衡",
        "先在可重复的 CI 或沙箱任务中验证接口、失败语义和依赖锁定，再用于关键路径",
        """flowchart LR
    U[开发者 CI 或上游应用] --> API[项目 CLI 或 API]
    API --> C[核心库 规则 或引擎]
    C --> H[宿主运行时 操作系统]
    C --> X[插件 适配器 外部服务]
    API --> O[配置 日志 诊断]""",
    ),
}


def brief(meta: dict, kind: str) -> str:
    boundary, flow, tradeoff, poc, _ = MODELS[kind]
    tags = ", ".join(map(str, meta.get("tags", [])[:6])) or "暂无标签"
    language = meta.get("language") or "公开资料未标注"
    return f"""## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | {boundary} | 基于项目分类、语言（{language}）、标签（{tags}）及本档案引用的公开资料做的架构抽象，不替代源码审计。 |
| 主路径 | {flow} | 图中组件表达职责与边界；具体协议、部署形态和持久化实现须以项目源码/文档核验。 |
| 核心权衡 | {tradeoff} | 这是技术决策观察，不将 GitHub 热度或评分当成生产可用性证据。 |
| 采用建议 | {poc} | 先做最小 PoC，并把安全、成本、SLO 与退出路径作为验收项。 |

"""


def enrich(path: Path, check_only: bool) -> tuple[bool, bool]:
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    kind = classify(meta, text)
    changed = False
    if "## 架构师速览" not in text:
        anchor = re.search(r"^## 架构启发.*$", text, re.MULTILINE)
        if not anchor:
            raise ValueError(f"{path.name}: missing 架构启发")
        text = text[:anchor.start()] + brief(meta, kind) + text[anchor.start():]
        changed = True
    if TICK + "mermaid" not in text:
        anchor = re.search(r"^## 定位判断.*$", text, re.MULTILINE)
        section = f"""## 架构图（MMD）

> 研究抽象：展示职责、控制/数据边界与主路径；不是未经验证的源码实现图。

{TICK}mermaid
{MODELS[kind][4]}
{TICK}

"""
        text = text[:anchor.start()] + section + text[anchor.start():] if anchor else text.rstrip() + "\n\n" + section
        changed = True
    if changed and not check_only:
        path.write_text(text, encoding="utf-8")
    return changed, TICK + "mermaid" in text and "## 架构师速览" in text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = valid = 0
    files = sorted(PROJECTS.glob("*.md"))
    for path in files:
        did_change, ok = enrich(path, args.check)
        changed += did_change
        valid += ok
    print(f"architect briefs: {valid}/{len(files)}; updated: {changed}")
    if args.check and (changed or valid != len(files)):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
