#!/usr/bin/env python3
"""Append 2026-09-25 section to trend-index.md"""
from pathlib import Path
import re

p = Path("indexes/trend-index.md")
text = p.read_text(encoding="utf-8")

# Update last_updated in frontmatter
text = re.sub(
    r"(last_updated: ')\d{4}-\d{2}-\d{2}(')",
    r"\g<1>2026-09-25\g<2>",
    text,
    count=1,
)

if "## 2026-09-25" in text:
    print("OK (idempotent: 2026-09-25 already present)")
    raise SystemExit(0)

lines = text.split("\n")
fm_end = 0
for i, l in enumerate(lines):
    if i > 0 and l.strip() == "---":
        fm_end = i + 1
        break

new_section = """

## 2026-09-25

### Contrastive-LM/CLM（769 stars · fork 61）· mikehasa/golive-skill（845 stars · fork 60）· yetone/magpie（595 stars · fork 29）· anishfn/shapeshift（566 stars · fork 53 · update）· samyost1/3dicon（379 stars · fork 36）

> 证据边界：项目名称、星标、tags、description、license、size、forks 来自 2026-09-25 GitHub Search API 公开元数据（created_at / pushed_at / stargazers_count / forks_count / language / description / topics / license / size）+ 各项目 README 公开摘录（API readme 字段 base64 解码）。"X 天 Y⭐"基于 created_at→2026-09-25 总星数除以经过天数（粗略下限估计），stargazers REST endpoint 需要认证故未做精确单日增量统计。**今日观察窗为 2026-09-23 ~ 2026-09-24 创建且截至 2026-09-25 仍在快速增长的 5 个非游戏类高质量工程型项目**；09-25 当日新创仓库在 GitHub API 暴露窗口 < 12 小时，本批重点放在 09-23 ~ 09-24 创建且仍持续增长的项目。**今日最大事件是 `Contrastive-LM/CLM` 2 天 769⭐ / fork 61 / fork/star 7.9% — 把 Jev / TypeSafe AI System One 决策模型从昨日 deepopen-com/deepopen「非自回归 System 1 决策引擎」+ anishfn/shapeshift「Jev 应用层 UI 端 18 类卡片」推到「对比学习 states↔actions + 缓存独立 + Apache-2.0 + pip install + vLLM serve + Terminal-Bench 87.6% + DeepSWE 81.6% SOTA verifier」严肃工程化形态**——CLM-8B 60M Nemotron Q&A + 30M synthetic hard negatives + 1M agentic trajectories 三段训练，states 和 actions 解耦，embeddings 独立缓存训练和服务都又快又便宜；computer-use / gaming / tool-calling 9× Jev 速度；CLMClient.system_one(state, questions={urgency:Noul, department:Choice}) 一次判断多 typed questions，TypeSafe 兼容 API（client 用 TYPESAFE_API_KEY 接入既有 Jev 应用层如 shapeshift / Astra-Ares / deepopen 即可无缝切换 CLM 后端）。**与昨日「Jev 应用层深化 + Codex effort 切换 + macOS / Windows 严肃隐私工程化 + Agent Skill 三平台 3D 严肃工程化」四主线不同**，今日主线转向「**Jev 决策模型挑战者 Apache-2.0 严肃工程化**（Contrastive-LM/CLM 对比学习 + SOTA verifier + pip install）」+「**Agent Skill 严肃工程化跨工作流**（golive-skill 上线 + 3dicon 视觉 + shapeshift UI）」+「**跨 Agent 模型统一网关 / 工具严肃工程化**（yetone/magpie 菜单栏 + 跨 CLI 模型切换）」三个严肃工程化的演化形态。**今日 5 个项目分三条主线**：**A. Jev 决策模型挑战者 Apache-2.0 严肃工程化**（Contrastive-LM/CLM）——把昨日 09-23 deepopen-com/deepopen「非自回归 System 1 决策引擎」+ 09-24 anishfn/shapeshift「Jev 应用层 UI 端 18 类卡片」同构「Jev 决策模型挑战者」推到「对比学习 states↔actions + 缓存独立 + Apache-2.0 + pip install + vLLM serve + Terminal-Bench 87.6% + DeepSWE 81.6% SOTA verifier + Discord + Hugging Face + blog + Contrastive-LM org」严肃工程化形态；**B. Agent Skill 严肃工程化跨工作流**（mikehasa/golive-skill 上线 + samyost1/3dicon 视觉生成）——把昨日 09-19 ~ 09-24 各 Agent Skill / harness 同构「Agent Skill 严肃工程化」推到「上线六路 provider detect → plan → approve → apply → verify + teardown + drift check + Zero telemetry + ownership document + Codex / Claude Code 已测」+「一个 prompt → 透明循环 3D 图标 + same still 双端 + 选色 matting + WebP alpha + Claude Code plugin + OpenRouter 双模型」两个跨工作流严肃工程化形态；**C. 跨 Agent 模型统一网关 / 工具严肃工程化**（yetone/magpie 菜单栏 App）——把昨日 09-23 unreallabsai/unreal-agent「async-first Go harness」+ 09-24 SewCabinSpout/cleanupper「macOS 终端 CLI + Trash-first + 保护路径黑名单 + Zero telemetry」同构「严肃工程化个人开发者工具 + 隐私 / 安全边界」推到「跨 Agent 菜单栏 App + 统一网关 127.0.0.1:3425/v1 + surgical 配置 + 模型列表拉取 + 共享订阅 + macOS / Linux / Windows 三平台 + 系统 webview < 15 MB」统一网关严肃工程化形态。**疑似操纵信号**——延续昨日 09-23 ~ 09-24 观测，09-25 继续出现一批 09-23 创建的 4KB Rust / 4KB None 仓库「BridgeDruidCompress/TauriKit」「BufferHerald/WarpLite」「AutocratGirder/ClashDesk」「BinaryDeliverer/CodexDesk」「BricklayerSurmount/DockForge」「centralcashierboost/ZedLite」等星标 222 ~ 224 / fork 47 ~ 48 / fork/star 21.2% 巧合相同，是典型的 bot-driven star fraud 信号，本批不入今日重点。

| 排名 | 趋势方向 | 代表项目 | 趋势分 |
|---:|---|---|---:|
| 1 | CLM-contrastive-system-one / Jev 决策模型挑战者进入 Apache-2.0 + 对比学习路线——Contrastive-LM/CLM 2 天 769⭐ ⑂61 fork/star 7.9%（Python · Apache-2.0 · 892 KB · CLM-8B 60M Nemotron Q&A + 30M synthetic hard negatives + 1M agentic trajectories 三段训练 · states 和 actions 解耦 embeddings 独立缓存 · TypeSafe 兼容 API · `pip install contrastive-lm` · `vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --port 8090` encoder + `clm-serve` 8700 API · CLMClient.system_one(state, questions={urgency:Noul, department:Choice}) 一次判断多 typed questions · computer-use / gaming / tool-calling 9× Jev 速度 · Terminal-Bench 2.1 87.6% SOTA verifier · DeepSWE 81.6% SOTA verifier · Discord + Hugging Face + blog · 与昨日 09-23 deepopen-com/deepopen「非自回归 System 1 决策引擎」+ 09-24 anishfn/shapeshift「Jev 应用层 UI 端 18 类卡片」同构「Jev 决策模型挑战者」但推到「对比学习 states↔actions + 缓存独立 + Apache-2.0 + pip install + vLLM serve + Terminal-Bench / DeepSWE SOTA verifier」严肃工程化形态） | Contrastive-LM/CLM | 90 |
| 2 | golive-skill / Agent Skill 把 agent 产物上线——mikehasa/golive-skill 2 天 845⭐ ⑂60 fork/star 7.1%（TypeScript · MIT · 1716 KB · Node.js 20+ · `npx skills add https://github.com/mikehasa/golive-skill --skill golive --global` 一行装 · `--agent codex --yes` / `--agent claude-code --yes` · detect → plan → approve → apply → verify 五步 · 0.1.0-alpha.3 · 六路 disposable live test 覆盖 hosting Vercel / Netlify + database Supabase / Neon + DNS Porkbun / GoDaddy + transactional email Resend + test-mode payments Stripe + Supabase auth + teardown 卸载 · ownership document + golive status on-demand drift check · Zero telemetry 无 GoLive account / hosted backend / product telemetry · 与昨日 09-23 unreallabsai/unreal-agent「async-first Go harness」+ 09-22 fstandhartinger/chat-seek-vscode「跨 CLI 聊天本地检索」同构「Agent Skill / harness 严肃工程化」但推到「Agent Skill 上线工程化 + 六路 provider + detect → plan → approve → apply → verify + teardown + drift check + Zero telemetry + ownership document」上线严肃工程化形态） | mikehasa/golive-skill | 88 |
| 3 | magpie-cross-agent-gateway / 跨 Agent 模型统一网关菜单栏 App——yetone/magpie 2 天 595⭐ ⑂29 fork/star 4.9%（Go · MIT · 6737 KB · Wails 系统 webview < 15 MB · 7 MB 终端 build · macOS / Linux / Windows · magpie tui / magpie cli / magpie panel · 本地网关 127.0.0.1:3425/v1 同时讲 OpenAI chat completions + OpenAI Responses + Anthropic Messages · 把 Codex / Claude Code / OpenCode / Cursor / Copilot / Goose / Gemini CLI / Pi 都指向一个 catalog · 配置 surgical edit settings.json / config.toml / opencode.jsonc / config.yaml 只动改的 key comments / ordering / indentation 完整保留 · atomic writes · 模型列表拉取 models.dev 不编译进 · 共享订阅 Claude Code / Codex / Copilot 登录让其他 Agent 用 · 厂商 OpenAI / Anthropic / Gemini / DeepSeek / Kimi / GLM / MiniMax / Qwen / Mistral / Groq / xAI / OpenRouter / Together / Fireworks / SiliconFlow / AiHubMix / 302.AI / Ollama / LM Studio · 与昨日 09-23 unreallabsai/unreal-agent + 09-24 SewCabinSpout/cleanupper 同构「严肃工程化个人开发者工具 + 隐私 / 安全边界」但推到「跨 Agent 菜单栏 App + 统一网关 + surgical 配置 + 模型列表拉取 + 共享订阅 + 三平台 + 系统 webview < 15 MB」统一网关严肃工程化形态） | yetone/magpie | 85 |
| 4 | shapeshift-update / Jev 应用层 UI 端具身形态更新——anishfn/shapeshift 3 天 566⭐ ⑂53 fork/star 9.4%（TypeScript · MIT · 12116 KB · 与昨日 09-24 同 · Jev 14 typed questions + 18 类卡片 + 滞回状态机 challenger + Next.js + Three.js + Excalidraw · shapeshiftui.vercel.app 在线 demo · 387⭐ → 566⭐ 持续增长） | anishfn/shapeshift | 82 |
| 5 | 3dicon-prompt-3d-icon / 一个 prompt 生成透明背景循环动画 3D 图标 Claude Code skill——samyost1/3dicon 2 天 379⭐ ⑂36 fork/star 9.5%（Python · MIT · 7741 KB · `/plugin marketplace add samyost1/3dicon` + `/plugin install 3dicon` · OPENROUTER_API_KEY GPT Image + Seedance · ffmpeg + 180 MB matting model · 同 still 作 first + last frame 无缝 loop · 选色 matting 解线性方程保 soft edge · WebP 真实 alpha · MIT 商用无限制 · 与昨日 09-19 ~ 09-24 各 Agent Skill / harness 同构「Agent Skill 严肃工程化」但推到「一个 prompt → 透明循环 3D 图标 + same still 双端 + 选色 matting + WebP alpha + Claude Code plugin + OpenRouter 双模型」视觉生成 Agent Skill 形态） | samyost1/3dicon | 78 |

#### 当日重点项目

- 🧠 Contrastive-LM/CLM (2 天 769⭐ ⑂61) — Jev 决策模型挑战者进入 Apache-2.0 + 对比学习路线；CLM-8B 60M Nemotron Q&A + 30M synthetic hard negatives + 1M agentic trajectories 三段训练；states 和 actions 解耦 embeddings 独立缓存；TypeSafe 兼容 API；`pip install contrastive-lm`；`vllm serve Qwen/Qwen3-8B --runner pooling --port 8090` encoder + `clm-serve` 8700 API；CLMClient.system_one(state, questions={urgency:Noul, department:Choice}) 一次判断多 typed questions；computer-use / gaming / tool-calling 9× Jev 速度；Terminal-Bench 2.1 87.6% SOTA verifier + DeepSWE 81.6% SOTA verifier；Discord + Hugging Face + blog Contrastive-LM org；Python Apache-2.0 892 KB，fork/star 7.9%，Score 90
- 🚀 mikehasa/golive-skill (2 天 845⭐ ⑂60) — Agent Skill 把 agent 产物上线；Vercel / Netlify / Supabase / Neon / Porkbun / GoDaddy / Resend / Stripe 六路 provider；detect → plan → approve → apply → verify 五步；teardown 卸载；ownership document + golive status on-demand drift check；Zero telemetry 无 GoLive account / hosted backend / product telemetry；0.1.0-alpha.3；Codex / Claude Code 已测；TypeScript MIT 1716 KB，fork/star 7.1%，Score 88
- 🐦 yetone/magpie (2 天 595⭐ ⑂29) — 跨 Agent 模型统一网关菜单栏 App；Wails 系统 webview < 15 MB desktop + 7 MB 终端 build；macOS / Linux / Windows；本地网关 127.0.0.1:3425/v1 同时讲 OpenAI chat completions / OpenAI Responses / Anthropic Messages；Codex / Claude Code / OpenCode / Cursor / Copilot / Goose / Gemini CLI / Pi 都指向一个 catalog；surgical edit + atomic writes；模型列表拉取 models.dev 不编译进；共享订阅 Claude Code / Codex / Copilot 登录让其他 Agent 用；厂商 OpenAI / Anthropic / Gemini / DeepSeek / Kimi / GLM / MiniMax / Qwen / Mistral / Groq / xAI / OpenRouter / Together / Fireworks / SiliconFlow / AiHubMix / 302.AI / Ollama / LM Studio；Go MIT 6737 KB，fork/star 4.9%，Score 85
- 🎭 anishfn/shapeshift (3 天 566⭐ ⑂53) — Jev 应用层 UI 端具身形态更新；Jev 14 typed questions + 18 类卡片 + 滞回状态机 challenger + Next.js + Three.js + Excalidraw；内置离线关键词分类器兜底；URL 参数 ?debug=1 ?demo=1&loop=1；shapeshiftui.vercel.app 在线 demo；TypeScript MIT 12116 KB，fork/star 9.4%，Score 82
- 🎲 samyost1/3dicon (2 天 379⭐ ⑂36) — 一个 prompt 生成透明背景循环动画 3D 图标 Claude Code skill；`/plugin marketplace add samyost1/3dicon` + `/plugin install 3dicon`；OPENROUTER_API_KEY 走 GPT Image + Seedance；ffmpeg + 180 MB matting model；同 still 作 first + last frame 无缝 loop；选色 matting 解线性方程保 soft edge；WebP 真实 alpha；MIT 商用无限制；Python MIT 7741 KB，fork/star 9.5%，Score 78
"""

new_lines = lines[:fm_end] + new_section.split("\n") + lines[fm_end:]
new_text = "\n".join(new_lines)
p.write_text(new_text, encoding="utf-8")
print("OK: 2026-09-25 section appended to trend-index.md")