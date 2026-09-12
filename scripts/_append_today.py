#!/usr/bin/env python3
"""Append 2026-09-13 section to trend-index.md at the top of content (after frontmatter)."""
from pathlib import Path

p = Path("indexes/trend-index.md")
text = p.read_text(encoding="utf-8")

# Idempotency: if today's section is already present, do nothing.
if f"\n## {__import__('datetime').date.today().isoformat()}" in ("\n" + text):
    print("OK (idempotent: today's section already present, skipping)")
    raise SystemExit(0)

# Find end of frontmatter (--- ... ---)
lines = text.split("\n")
fm_end = 0
for i, l in enumerate(lines):
    if i > 0 and l.strip() == "---":
        fm_end = i + 1
        break

new_section = """

## 2026-09-13

### Chuloo/mural（114 stars）· Xu123-Bob/Baize（67 stars）· Qiuner/birdview（68 stars）· ccompactor/ccompactor（16 stars · fork 11）· wannabeyourfriend/awesome-harness-evolution（22 stars）· JoaoFranco03/DuoHinge（40 stars）

> 证据边界：项目名称、星标、tags、description 来自 2026-09-13 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license）+ 各项目 README 公开摘录（API readme 字段 base64 解码）。"X 天 Y⭐"基于 created_at→2026-09-13 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**09-13 当日新创仓库 API 暂返回 0 条（亚洲时区多数仓库刚过 12 小时曝光窗口）；本简报以 09-12 创建且截至 09-13 仍在快速增长的 6 个项目为分析对象**。**今日最大事件是 `ccompactor/ccompactor` 1 天 16⭐ / fork 11 / fork/star 68.8% 极端高企业 fork 信号 — Coding Agent Session Handoff CLI**——把任意 coding agent session（Claude Code / Codex / Pi）提取为压缩 + 验证 + 跨 Agent 可继续的 handoff 制品，TypeScript + commander/ink/react + standalone 二进制 + .deb + npm，SPEC.md 全阶段实现 + 「No Anthropic-derived code is present」避免 license 风险。**`Chuloo/mural` 1 天 114⭐ / fork 33 / fork/star 28.9% 是本批企业 fork 信号次高 — 原生 iPhone 对话式语言学习伴侣**——SwiftUI + Liquid Glass（iOS 26 新界面框架）+ SwiftData 本地存储 + 自带 OpenAI API key（不绑账号、不绑 Mac）+ GPT-Live-1 + GPT-5.6 Luna；与昨日 `FankChen/tracecrate` 同构「客户端原生 + 自带 API key」反 SaaS 范式。**iPhone Duo 二创集群在 09-13 第二天新增 `JoaoFranco03/DuoHinge` 40⭐**——Swift 6.4 + Metal 3 + AppleSPUHIDDriver 底层 IOKit 盖角度读数 + 120Hz 渲染 + prebuilt DMG Apple Silicon only + Ko-fi 赞助；与 09-12 集群（sumimakito/Mac-Duo 512⭐ / DhananjayBhosale/MacDuo 132⭐ / jh3y/lid-plane 131⭐ / Atomicx7/Duo-animation 128⭐ / elijah-semyonov/DuoLikeAnimation 125⭐ / chuspeeism/iphone-duo 98⭐ / IuCC123/BendMac 88⭐ / eperez28/sonar.cool 89⭐ / opensourcevillain/Bendable 76⭐ / MakrSas/Inferno-iOS 73⭐ / jlxc2001/MacBook-Duo 62⭐）形成单点灵感 → 多 repo 并发持续事件。**AI Coding 工具链六件套 09-13 集中成形**：maskit（出网层隐私）+ routeVSCODE（模型层路由）+ Baize（agent loop 层）+ tracecrate（时序层只读）+ birdview（架构层可视化）+ ccompactor（session 层互操作）。11 个游戏外挂 / 私服 / Mod 工具（solara-executor-free / universal-aimbot-esp / wardogs-tactical-overlay / Fortnite-ESP / Roblox-Executor 等）元数据信号异常，本简报不列入核心趋势；`flybook-git/Main`（237⭐ / 1 天 / fly-connectome 驱动加密货币自动交易 / README 自述"Profitable learning has not been demonstrated"）虽有真材实料但定位极窄（神经科学 × 加密交易），亦不列入。

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|---:|---|---|---:|
| 1 | native-iphone-language-companion / 原生 iPhone 对话式语言学习伴侣——Chuloo/mural 1 天 114⭐ ⑂33 fork/star 28.9%（SwiftUI + Liquid Glass + SwiftData · 自带 OpenAI API key · GPT-Live-1 + GPT-5.6 Luna · Xcode 26 + iOS 26.1+ · 6MB repo · Swift 6 · iPhone 17 截图四张 · 现场 Code Agent 一键构建安装的 install prompt 公开 · MIT） | Chuloo/mural | 90 |
| 2 | agent-session-handoff-cli / Coding Agent Session 压缩 + 验证 + 跨 Agent Handoff——ccompactor/ccompactor 1 天 16⭐ ⑂11 fork/star 68.8%（TypeScript · commander + ink + react · Claude Code/Codex/Pi 三适配器 · schema + quote-verify 验证 · list/find/extract/expand/verify/handoff/--tui 七命令 · standalone 二进制 + .deb + npm · CI + npm 自动 publish · MIT） | ccompactor/ccompactor | 86 |
| 3 | chinese-vibe-coding-cli / 中文 Vibe Coding CLI「白泽」——Xu123-Bob/Baize 1 天 67⭐ fork 0（Python 3.10+ · DeepSeek / OpenAI 兼容 / Ollama 三后端 · Skills + Subagents + Hooks + MCP + 上下文压缩 + 安全沙箱 · 黑金 CLI 主题 · 中文宽度自适应 · MIT） | Xu123-Bob/Baize | 84 |
| 4 | architecture-as-code-skill / 「Stop letting AI code blind」架构可视化 Skill——Qiuner/birdview 1 天 68⭐ ⑂3（Node.js 18+ · Evidence-linked 架构图带 stable module IDs + 文件归属 · Architecture / Changes / Side-by-side 三视图 · JSON Schema + semantic 验证 · standalone HTML 输出无服务器依赖 · 英文 + 中文双语 · 0.1.0 · MIT） | Qiuner/birdview | 82 |
| 5 | agent-harness-research-list / AI Agent Harness 演化论文精选——wannabeyourfriend/awesome-harness-evolution 1 天 22⭐ ⑂1 fork/star 4.5%（Python awesome-list · Foundation / Benchmark / Recipe / Position 四类 · 104 选中论文 · 99 校徽 · research-timeline.svg 2022→2026-09 跨度图 · assets/institutions.json + timeline-affiliations.json · CC0） | wannabeyourfriend/awesome-harness-evolution | 78 |
| 6 | duo-macos-hinge-app / iPhone Duo 折叠动效 macOS 移植——JoaoFranco03/DuoHinge 1 天 40⭐ ⑂1 fork/star 2.5%（Swift 6.4 + Metal 3 · AppleSPUHIDDriver 盖角度读数 · damped response · 120Hz 渲染 · prebuilt DMG Apple Silicon only · Ko-fi 赞助 · MIT · 09-12 Mac-Duo 集群延伸） | JoaoFranco03/DuoHinge | 76 |

#### 当日重点项目

- 🗣️ Chuloo/mural (1 天 114⭐) — 原生 iPhone 对话式语言学习伴侣，SwiftUI + Liquid Glass + SwiftData + 自带 OpenAI API key + GPT-Live-1 + GPT-5.6 Luna，MIT，fork/star 28.9%，Score 90
- 🧳 ccompactor/ccompactor (1 天 16⭐ ⑂11) — Coding Agent Session Handoff CLI，Claude Code/Codex/Pi 三适配器，schema + quote-verify，TypeScript，standalone 二进制 + .deb + npm，MIT，fork/star 68.8%，Score 86
- 🦌 Xu123-Bob/Baize (1 天 67⭐) — 中文 Vibe Coding CLI「白泽」，多后端 + Skills + Subagents + Hooks + MCP + 安全沙箱 + 黑金 CLI 主题，MIT，Score 84
- 🗺️ Qiuner/birdview (1 天 68⭐) — 「Stop letting AI code blind」架构可视化 Skill，evidence-linked 模块图 + standalone HTML 输出，Node.js 18+，MIT，Score 82
- 📚 wannabeyourfriend/awesome-harness-evolution (1 天 22⭐) — AI Agent Harness 演化论文精选清单，Foundation/Benchmark/Recipe/Position 四类 104 篇，CC0，Score 78
- 📐 JoaoFranco03/DuoHinge (1 天 40⭐) — iPhone Duo 折叠动效移植 macOS，Swift 6.4 + Metal 3 + AppleSPUHIDDriver + 120Hz，prebuilt DMG Apple Silicon only，MIT，Score 76


"""

# Insert new_section after frontmatter (line fm_end)
new_lines = lines[:fm_end] + [new_section] + lines[fm_end:]
# Update last_updated in frontmatter
for i in range(fm_end):
    if new_lines[i].startswith("last_updated:"):
        new_lines[i] = "last_updated: '2026-09-13'"

new_text = "\n".join(new_lines)
p.write_text(new_text, encoding="utf-8")
print("OK")
