#!/usr/bin/env python3
"""Prepend 2026-09-13 section to daily-report.md (newest first)."""
from pathlib import Path

p = Path("daily-report.md")
text = p.read_text(encoding="utf-8")

# Find the first H2 line (## YYYY-MM-DD) to insert before it
lines = text.split("\n")
insert_at = None
for i, l in enumerate(lines):
    if l.startswith("## 2026-"):
        insert_at = i
        break

if insert_at is None:
    # Fall back: append after the horizontal rule
    insert_at = 4

new_section = """## 2026-09-13
**核心主题：** Chuloo/mural 1 天 114⭐ 原生 iPhone 对话式语言学习伴侣（SwiftUI · Liquid Glass · SwiftData · 自带 OpenAI API key · GPT-Live-1 + GPT-5.6 Luna · MIT · fork/star 28.9%）· ccompactor/ccompactor 1 天 16⭐ ⑂11 Coding Agent Session Handoff CLI（TypeScript · Claude Code/Codex/Pi 三适配器 · schema + quote-verify · standalone 二进制 + .deb + npm · MIT · fork/star 68.8% 极端高）· Xu123-Bob/Baize 1 天 67⭐ 中文 Vibe Coding CLI「白泽」（多后端 DeepSeek/OpenAI 兼容/Ollama · Skills + Subagents + Hooks + MCP · 安全沙箱 · MIT）· Qiuner/birdview 1 天 68⭐ 「Stop letting AI code blind」架构可视化 Skill（architecture-as-code · evidence-linked · standalone HTML 输出 · MIT）· wannabeyourfriend/awesome-harness-evolution 1 天 22⭐ AI Agent Harness 演化论文精选清单（104 篇 · Foundation/Benchmark/Recipe/Position · CC0）· JoaoFranco03/DuoHinge 1 天 40⭐ iPhone Duo 折叠动效移植 macOS（Metal 3 · AppleSPUHIDDriver · 120Hz · prebuilt DMG · MIT）

**证据边界：** 星标、总星数与增速取自 2026-09-13 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license）+ 各项目 README 公开摘录（API readme 字段 base64 解码）；"X 天 Y⭐"基于 created_at→2026-09-13 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**09-13 当日新创仓库 API 暂返回 0 条（亚洲时区多数仓库刚过 12 小时曝光窗口）；本简报以 09-12 创建且截至 09-13 仍在快速增长的 6 个项目为分析对象**。**今日最大事件是 `ccompactor/ccompactor` 1 天 16⭐ / fork 11 / fork/star 68.8% 极端高企业 fork 信号 — Coding Agent Session Handoff CLI**——把任意 coding agent session（Claude Code / Codex / Pi）提取为压缩 + 验证 + 跨 Agent 可继续的 handoff 制品，TypeScript + commander/ink/react + standalone 二进制 + .deb + npm，SPEC.md 全阶段实现 + 「No Anthropic-derived code is present」避免 license 风险。**`Chuloo/mural` 1 天 114⭐ / fork 33 / fork/star 28.9% 是本批企业 fork 信号次高 — 原生 iPhone 对话式语言学习伴侣**——SwiftUI + Liquid Glass（iOS 26 新界面框架）+ SwiftData 本地存储 + 自带 OpenAI API key（不绑账号、不绑 Mac）+ GPT-Live-1 + GPT-5.6 Luna；与昨日 `FankChen/tracecrate` 同构「客户端原生 + 自带 API key」反 SaaS 范式。**iPhone Duo 二创集群在 09-13 第二天新增 `JoaoFranco03/DuoHinge` 40⭐**——Swift 6.4 + Metal 3 + AppleSPUHIDDriver 底层 IOKit 盖角度读数 + 120Hz 渲染 + prebuilt DMG Apple Silicon only + Ko-fi 赞助；与 09-12 集群形成单点灵感 → 多 repo 并发持续事件。**AI Coding 工具链六件套 09-13 集中成形**：maskit（出网层隐私）+ routeVSCODE（模型层路由）+ Baize（agent loop 层）+ tracecrate（时序层只读）+ birdview（架构层可视化）+ ccompactor（session 层互操作）——覆盖出网 / 模型 / loop / 时序 / 架构 / 互操作六个角度。11 个游戏外挂 / 私服 / Mod 工具元数据信号异常，本简报不列入核心趋势；`flybook-git/Main`（237⭐ / 1 天 / fly-connectome 驱动加密货币自动交易 / README 自述"Profitable learning has not been demonstrated"）虽有真材实料但定位极窄，亦不列入。

**关键项目：**
- 🗣️ Chuloo/mural (1 天 114⭐) — 原生 iPhone 对话式语言学习伴侣（SwiftUI + Liquid Glass + SwiftData · 自带 OpenAI API key · GPT-Live-1 + GPT-5.6 Luna · 语音驱动 + 三档回忆强度词汇 · Xcode 26 + iOS 26.1+ · install prompt 公开 · 6MB · fork/star 28.9%），Score 90
- 🧳 ccompactor/ccompactor (1 天 16⭐ ⑂11) — Coding Agent Session Handoff CLI（TypeScript · commander + ink + react · Claude Code/Codex/Pi 三适配器 · schema + quote-verify 双重验证 · doctor/list/find/extract/expand/verify/handoff/--tui 七命令 · session refs 四种寻址 · standalone 二进制 macOS arm64/x64 + Linux x64/arm64 + Windows x64/arm64 + .deb + npm · CI + npm Automation token · SPEC.md 全阶段实现 · fork/star 68.8%），Score 86
- 🦌 Xu123-Bob/Baize (1 天 67⭐) — 中文 Vibe Coding CLI「白泽」（Python 3.10+ · DeepSeek/OpenAI 兼容/Ollama 三后端 · Skills + Subagents + Hooks + MCP · 两级上下文压缩 · 命令白名单 + 路径逃逸检测 + 脚本注入拦截安全沙箱 · 黑金 CLI 主题中文宽度自适应 · fork 0 反映产品成熟度早期信号），Score 84
- 🗺️ Qiuner/birdview (1 天 68⭐) — 「Stop letting AI code blind」架构可视化 Skill（Node.js 18+ · evidence-linked 架构图带 stable module IDs + 文件归属 · Architecture/Changes/Side-by-side 三视图 · JSON Schema + semantic 验证 · standalone HTML 输出无服务器依赖 · 双击离线浏览 · 中英双语 · 0.1.0），Score 82
- 📚 wannabeyourfriend/awesome-harness-evolution (1 天 22⭐) — AI Agent Harness 演化论文精选清单（明确 harness vs weights 概念边界 · Foundation/Benchmark/Recipe/Position 四类 · 104 篇选中论文 · 99 篇机构 logo · research-timeline.svg 2022→2026-09 跨度图 · assets/institutions.json + timeline-affiliations.json · CC0），Score 78
- 📐 JoaoFranco03/DuoHinge (1 天 40⭐) — iPhone Duo 折叠动效移植 macOS 菜单栏 App（Swift 6.4 + Metal 3 · AppleSPUHIDDriver 底层 IOKit 盖角度读数 · damped response 平滑到渲染节奏 · 120Hz 渲染 · 桌面处理不外发屏幕数据 · prebuilt DMG Apple Silicon only · Ko-fi 赞助 · 44 MB），Score 76

**关键判断：**
- **「自带 API key」反 SaaS 范式在 iOS 端确立**：Chuloo/mural 的 SwiftUI + Liquid Glass + 自带 OpenAI API key + 不绑账号，与昨日 tracecrate / maskit 同构但推到 iOS 端最难做的语音实时对话场景；iOS 26 + GPT-5.6 Luna 双前沿定位
- **Coding Agent 互操作层出现第一个标杆**：ccompactor 的 fork/star 68.8% 是极端高企业 fork 信号（11 个 fork 几乎都是企业内 fork 准备二次开发 / 私有部署）；schema + quote-verify + 跨 agent 启动三件套是 Agent 互操作的最小可用形态
- **AI Coding 工具链六件套集中成形**：maskit（出网层）+ routeVSCODE（模型层）+ Baize（agent loop 层）+ tracecrate（时序层）+ birdview（架构层）+ ccompactor（session 层）六件套覆盖六个角度，与昨日 Baize 形成对照
- **Agent Harness 赛道被 awesome-list 形式化**：wannabeyourfriend/awesome-harness-evolution 把 harness 定义清楚并索引 104 篇论文；意味着 Harness 作为独立学术 / 工程领域已得到广泛认可；研究型 awesome-list 模板（Timeline + 机构 logo + 阅读笔记）成熟
- **iPhone Duo 二创集群在 09-13 第二天**：JoaoFranco03/DuoHinge 是该集群第二天新增成员，差异点是 AppleSPUHIDDriver 底层 IOKit 接口 + Metal 3 120Hz；累计 7+ 个变体；真正决定集群长期可持续性的是 Apple 官方是否在 macOS 下个版本内置类似 API
- **本土 Coding Agent 工具链 2026 Q3 集中爆发**：Baize（本土 Claude Code 替代 + 中文宽度）+ mural（iOS 自带 API key）+ tracecrate（local-first）说明中文 Coding Agent 工具链补完进入加速期；与 09-11 DeepSelect + recipe 形成「官方底层 + 社区工具层」双线推进
- **AI Coding 黑盒透明化形成「架构 + 时序」双视角**：birdview（架构层）+ tracecrate（时序层）覆盖 AI Coding 黑盒的两个维度；与 ccompactor（session 互操作）三件套构成 AI Coding 工具链完整可观测栈

---
"""

# Insert at the position of the first ## date header (push it down)
new_lines = lines[:insert_at] + [new_section] + lines[insert_at:]
new_text = "\n".join(new_lines)
p.write_text(new_text, encoding="utf-8")
print("OK")
