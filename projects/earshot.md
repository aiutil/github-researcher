---
title: "Leonxlnx/earshot"
slug: earshot
date_added: 2026-10-17
category: "工具型"
emoji: "🎧"
stars: "302 stars"
stars_delta: "2 天 302⭐（粗略下限估计）"
language: "Python"
score: 84
tags: ["earshot","leonxlnx","ears-for-coding-agents","cpu-only","audio-understanding","sound-critique","sound-design","code-synthesized","evolutionary-search","recipe","modal-resonators","mcp","claude-code","gemini-audio-llm","launch-film-critique","lufs","true-peak","lra","spectrogram","python","cli","python-api","mit"]
url: "https://github.com/Leonxlnx/earshot"
---

# Leonxlnx/earshot

## 一句话定位
Coding agent 的耳朵——把声音变成 agent 能 reasoning 的 evidence：what a file sounds like in words、how well it fits a description、best moment inside a long recording、real recording vs code-synthesized、second-by-second listening transcript、annotated picture、scorecard against professional launch films。CPU-only run，开源 MIT。

## 它解决的问题
2026 年 coding agent 写代码渲染电影 / 制作产品 demo / 写游戏，但他们"听不见"自己写的——premium key press 还是 cheap key press、hit 是不是晚了 80ms、music swell 在错地方——这是真痛点。Leonxlnx/earshot 把声音变成可量化、可 critique、可 self-iterate 的工程化闭环：CLI + Python API + MCP server + 16 commands + earshot forge 物理合成 + critic 量化打分 + evolutionary search 自我迭代。

## 为什么值得关注（2026-10-17）
- **Stars:** 302（截至 2026-10-17），2 天破 300
- **Forks:** 19，fork/star 6.3% 适度二次开发
- **Language:** Python
- **License:** MIT
- **Size:** 3429 KB
- **热度来源：** AI coding agent 多模态感官严肃工程化 + recipe 物理合成 + critic 量化打分 + evolutionary search 自我迭代
- **独特性：** 是「coding agent 听觉 + 自我迭代闭环」严肃工程化范本，与 generative audio GAN/TTS 路线不同
- **架构独特性：** 16 命令宽能力 + CPU-only 无 GPU 依赖 + earshot forge 物理合成（无录音依赖）+ MCP for Claude Code

## 热度来源判断
**真实需求 + 工程化范式独特 + 开源 + CPU-only** 四组合：
- **需求侧：** coding agent 已经在 rendering / 状态机 / 数据处理 / 多媒体创造 上强，但听不见自己写的；游戏 audio / 播客 / UX audio / indie film 的 agent 化是真痛点
- **技术侧：** 「声音 → 描述 + 匹配 + 时间线 + 量化 + 物理合成 + 进化搜索」是与 GAN/TTS 完全不同的严肃工程化路径——recipe 物理合成（无录音依赖）+ critic 量化打分（无主观偏差）+ evolutionary search 自我迭代
- **生态侧：** MCP server for Claude Code + Python API + CLI + CPU-only 让它可以塞进 Claude Code / Cursor / Codex / OpenCode workflow
- **风险：** 「local model 推理延迟 + 进化搜索 budget」是 production-scale 测试需要严肃 benchmark；「7 部专业 launch films」的电影 baseline 是否真代表"professional"需要开放评估

## 关键技术亮点
1. **声音 → evidence → agent reasoning：** calibrated tags (z) + closest alternative readings + AudioSet labels + measurements → agent 可 reasoning 的 evidence
2. **16 命令宽能力：** describe / match（cosine + z among vocabulary + verdict strong/plausible/weak/no match + held-out evidence）/ rank（多候选排序）/ find（best moments as sample trims）/ compare / ab（A/B two sounds，差异用 words）/ realness（real recording vs code-synthesized，evidence + per-window scores）/ timeline（events + sections + loudness + beat grid + sync to picture cuts + cue frames）/ sheet（annotated PNG video frames + sections + labelled events + spectrogram + waveform + loudness + sync markers）/ critique（launch-video scorecard vs 7 professional launch films + timestamped fixes）/ profile（build your own reference profile）/ measure（LUFS + true peak + LRA + envelope + spectrum + tempo/key）/ forge（make a sound in code + improve by listening）/ llm（optional Gemini audio critique + own key + consent）/ mcp（same tools as MCP server for Claude Code）/ doctor（check install + models + data + CPU）
3. **earshot forge 物理合成引擎：** recipe of physical synthesis (modal resonators + contact excitations + filtered noise + computed room + microphone; no recorded audio inside) → 渲染候选 → critic scoring → evolutionary search (keeps best + mutates) → self-iteration loop (agent 读 critic words + 看谱图 next to refs + 改 recipe + 重跑)
4. **Critic scoring 模块：** description match against named confusions + realness + closeness to real reference recordings + measured shape + model-free tonal-balance + tail check against references
5. **Evolutionary search 引擎：** 保持最优 + 变异 + 迭代 + agent read critic words + 谱图对照 + rewrite recipe + rerun
6. **CPU-only runtime：** 不依赖 GPU；适合 CI / 边缘 / 服务器部署
7. **MCP server for Claude Code and other agents：** same tools as CLI 暴露给 Claude Code 等 coding agent
8. **Gemini audio-LLM critique（optional）：** 仅 with own key + explicit consent
9. **7 部专业 launch films baseline：** critique 命令与 launch-video scorecard 对照；用户可 build own reference profile

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 一个 earshot CLI（16 commands: describe / match / rank / find / compare / ab / realness / timeline / sheet / critique / profile / measure / forge / llm / mcp / doctor）+ 一个 Python API（`from earshot import api`）+ 一个 MCP server（same tools as CLI for Claude Code and other agents）+ 一个 local CPU 模型集合（描述 / 匹配 / 真实 vs 合成分类 / 时间线 / 频谱）+ 一个 Gemini 可选 audio-LLM critique（用户自己的 key + 明确 consent）+ 一个 CPU-only runtime（不需 GPU） + 一个 earshot forge 物理合成引擎（recipe: modal resonators + contact excitations + filtered noise + computed room + microphone；no recorded audio）+ 一个 critic scoring 模块（description match against named confusions + realness + closeness to real reference recordings + measured shape + model-free tonal-balance + tail check against references）+ 一个 evolutionary search 引擎（保持最优、变异、迭代）+ 一个 Launch film critique profile（7 部专业 launch films）+ 一个 local-first 安装（Python + `pip install` 隐含）+ 一个 self-iteration loop（critic 反馈 + 谱图对照 + 改 recipe + 重跑）+ Python + MIT + 5 topics ai-agents/audio/claude-code/mcp/sound-design | 仅基于 README「Ears for coding agents + AI coding agents can now write the code that renders a film + a product demo or a game. They still cannot hear what they made + earshot turns sound into evidence an agent can reason about: what a file sounds like in words + how well it fits a description + the best moment inside a long recording + whether it is a real recording or code-synthesized + a second-by-second listening transcript of a whole film + an annotated picture of it + a scorecard against professional launch films + runs locally on CPU + CLI + Python API + MCP server + 16 commands + earshot forge recipe of physical synthesis + evolutionary search + critic scoring + self-iteration + 5 topics」+ license badge + size 推断；具体本地模型集合的来源（CLAP / AudioCLIP / PANNs / Wav2CLIP 等的 fine-tune 版本）、Gemini integration 的 cost 模型、evolutionary search 的 population size + mutation 策略、forge recipe DSL 的语法（python-based vs 自定义）、7 部专业 launch films 的具体名单未在档案明示 |
| 主路径 | 用户 `pip install earshot`（假设）→ 装本地 CPU 模型集合 → 用 `earshot describe` 给一段声音 → 拿 calibrated tags (z) + closest alternative readings + AudioSet labels + measurements（attack + decays + peak + brightness）；用 `earshot match file.wav "description" --alts ...` 拿 cosine + z among vocabulary + verdict (strong/plausible/weak/no match) + held-out evidence；用 `earshot find longfile.ogg "a single mechanical key press" --top 4` → 0:03.94-0:04.19 ... best moments；用 `earshot compare file --refs DIR` → nearest reference recordings；用 `earshot realness file.wav ...` → real recording vs code-synthesized with evidence；用 `earshot timeline film.ogg [--video V] [--cues C]` → events (time + level + tag) + sections + loudness + beat grid + sync to picture cuts + cue frames；用 `earshot sheet film.ogg -o out.png` → annotated PNG with video frames + sections + labelled events + spectrogram + waveform + loudness + sync markers（给读图 agent 看）；用 `earshot critique film.mp4 [--video V]` → launch-video scorecard vs profile of 7 professional launch films + timestamped fixes；用 `earshot profile refs... -o p.json` → build your own reference profile；用 `earshot measure file` → objective only（LUFS + true peak + LRA + envelope + spectrum + tempo/key）；用 `earshot forge` 写 sound recipe → forge 渲染候选 → critic 打分 → evolutionary search 最优 + 变异 → agent 看 critic words + 谱图 next to refs → 改 recipe → 重跑；可选 `earshot llm --yes-upload` → Gemini audio critique（own key + consent）；`earshot mcp` 启 MCP server for Claude Code / other agents；`earshot doctor [--load]` check install + models + data + CPU | 主路径为 README「What it does (16 commands table) + Make sounds earshot forge + How it works」段落整理；具体模型加载延迟（20-40s 每次 CLI call vs 进程内复用）、Gemini integration 的 cost 本地测算、evolutionary search 在 budget=144 + reps=2 下的实际 budget 时间、forge recipe DSL 在不同材质（金属 / 木头 / 玻璃）的差异未在档案明示 |
| 关键权衡 | CPU-only vs GPU/audio-LLM 为主 vs CLAP/AudioCLIP/PANNs/Wav2CLIP 等预训练 vs 自训 collector vs recipe 物理合成 vs GAN/TTS/VALL-E/Tortoise 等录制型 TTS vs code-synthesized vs 录音依赖 vs quantitative critique (z score) vs subjective critique vs evolutionary search vs gradient descent optimization vs 16 命令宽能力 vs 单一 describe/match vs MCP for Claude Code vs Gemini 集成（optional + key）vs local-first vs cloud API vs standalone CLI vs forge + critic self-iteration loop vs 7 部专业 launch films baseline vs 自建 profile | 权衡来自 README「Ears for coding agents + AI coding agents can write the code that renders a film ... cannot hear what they made + earshot turns sound into evidence an agent can reason about + 16 commands + earshot forge recipe of physical synthesis + evolutionary search + critic scoring + self-iteration + MCP server for Claude Code and other agents + CPU-only + 5 topics」 |
| 最小 PoC | a) `pip install earshot` → `earshot doctor` 检装 + 模型 + data + CPU；b) `earshot describe keypress.ogg` → 拿 calibrated tags (z) + closest alternatives + measurements（attack/decays/peak/brightness）；c) `earshot match key.ogg "a deep thocky mechanical keyboard press" --alts "a clicky blue switch keyboard" "a mouse click"` → 强 verdict；d) `earshot forge keypress --refs path/to/real/keypresses/ --budget 144 --reps 2 --tone 1.5 --keep 4 --robust 8 --dir made/keypress` → 物理合成 + critic scoring + evolutionary search → 看 made/keypress 目录；e) `earshot mcp` 启 MCP server → Claude Code 装 MCP → call describe / match / forge | PoC 由 README「Quick start (隐含) + 16 commands + earshot forge + mcp」段落整理；具体 forge 在不同 recipe 复杂度下的总时长、MCP server 在 Claude Code 上的 multi-tool 协同、local 模型在 8GB+ RAM CPU 上的 latency、与 Stable Audio / ElevenLabs / Udio 的实际音质对比未在档案明示 |
| 证据边界 | 仅核验：仓库存在、stars/forks/description/license/size/language 来自 GitHub API；README 节录自 raw 接口；Ears for coding agents + CPU-only + 16 commands (describe / match / rank / find / compare / ab / realness / timeline / sheet / critique / profile / measure / forge / llm / mcp / doctor) + earshot forge recipe 物理合成 (modal resonators + contact excitations + filtered noise + computed room + microphone; no recorded audio) + critic scoring (description match + realness + closeness + measured shape + tonal-balance + tail check) + evolutionary search (keep best + mutate) + self-iteration loop (agent 改 recipe + 重跑) + MCP server for Claude Code and other agents + Python + CLI + Python API + 5 topics ai-agents/audio/claude-code/mcp/sound-design + MIT 由 README 直接叙述 | 待核验：本地模型集合的具体来源（CLAP / AudioCLIP / PANNs / Wav2CLIP fine-tune 等）+ 训练数据 + 模型规模、模型加载延迟（20-40s 每次 CLI call）、evolutionary search population + mutation 策略、7 部专业 launch films 的具体名单、Gemini 集成的 cost 模型、recipe DSL 语法（python-based 或 DSL）、launch-video scorecard 23 scored metrics 的具体定义、与 Stable Audio / ElevenLabs / Udio / MusicGen 等音频生成模型的对比、噪音素材 license、与 Anthropic / OpenAI / Google 官方 audio-LLM 的互补/竞争关系 |

## 架构启发
Leonxlnx/earshot 的核心启发是 **「Coding agent 不能只 rendering + state machine + 数据处理，必须有耳朵；耳朵应该是 evidence + critique + self-iterate 的工程闭环」**。三层意义：
1. **声音 → agent reasoning evidence：** 把"声音感觉"翻译成 calibrated tags (z) + AudioSet labels + measurements，让 agent 在 reasoning 时可以客观对照，而非"主观好听"
2. **earshot forge 物理合成 vs GAN/TTS：** recipe 物理合成（modal resonators + contact excitations + filtered noise + computed room + microphone，无录音）+ critic 量化打分 + evolutionary search 自我迭代，是与 GAN/TTS/VALL-E/Tortoise 等录制型 TTS 完全不同的严肃工程化路径——优势是无录音 license / 隐私 / 数据依赖，劣势是音色自然度 vs generative model
3. **CPU-only + MCP for Claude Code：** 让 16 命令宽能力可以塞进 Claude Code / Cursor / Codex / OpenCode workflow；这对 indie coder / 边缘部署 / CI pipeline 友好

更深层的启发：**Self-iteration loop = critic 量化打分 + evolutionary search + agent read critic words + 谱图对照 + rewrite recipe + rerun**——这是一个非常具体的"agent-evolution 闭环"。从 recipe 写出，到 critic 打分，到 evolutionary search 优化，到 agent 重写 recipe——这是 AI agent 自我进化的严肃工程化范式，可推广到图像 / 视频 / 文档生成等领域。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[开发者 / Claude Code / Cursor / Coding Agent] --> CLI[earshot CLI<br/>16 commands]
  User --> API[from earshot import api<br/>Python API]
  User --> MCP[earshot mcp<br/>MCP server for Claude Code]
  CLI --> Models[local CPU 模型集合<br/>描述 / 匹配 / 真实 vs 合成分类 / 时间线 / 频谱]
  MCP --> Models
  API --> Models
  Models --> Output[earshot evidence<br/>calibrated tags (z) + AudioSet labels + measurements<br/>+ best moments + realness score]
  Output --> Describe[describe + match + rank + find + compare + ab + realness<br/>+ timeline + sheet + critique + profile + measure + llm + doctor]
  Output --> Forge[earshot forge<br/>recipe of physical synthesis<br/>modal resonators + contact excitations + filtered noise + computed room + microphone<br/>no recorded audio]
  Forge --> Critics[critic scoring<br/>description match + realness + closeness + measured shape + tonal-balance + tail check]
  Critics --> Search[evolutionary search<br/>keep best + mutate + iterate]
  Search --> AgentLoop[agent self-iteration loop<br/>read critic words + 谱图 next to refs + rewrite recipe + rerun]
  User -.optional.-> Gemini[Gemini audio-LLM critique<br/>own key + explicit consent]
  Output -.scorecard against.-> LaunchFilms[7 部专业 launch films baseline<br/>or user-built profile]
```

## 定位判断
**工具型候选（coding agent 时代多模态感官 + 自我迭代闭环）。** Leonxlnx/earshot 试图成为「coding agent 时代多模态感官 + 自我迭代闭环」的事实标准——声音 → agent reasoning evidence + 16 命令宽能力 + CPU-only + earshot forge 物理合成 + critic 量化打分 + evolutionary search 自我迭代 + MCP for Claude Code。**定位判断：**
- **现在：** CPU-only + 16 commands + recipe 物理合成 + critic 量化打分 + evolutionary search 自我迭代 的第一个公共发布
- **如果 recipe DSL 简洁 + forge 自我迭代能在 1-2 分钟收敛：** 它会变成「indie coder / game audio / 播客 / UX audio」的事实工具
- **如果 earshot forge 出品的音色与 real recording 接近：** 它会打开 AI 声音创造的新范式（无录音 license / 隐私 / 数据依赖）
- **如果 MCP server + Claude Code / Cursor / Codex / OpenCode 工作流紧密集成：** 它会变成 "coding agent 多模态感官" 标准件
- **风险：** CPU-only 推理延迟（20-40s 每次 CLI call）+ recipe DSL 学习曲线 + evolutionary search population/mutation 策略 + 7 部 launch films baseline 的代表性 + Gemini integration 的 cost
- **潜力：** 自我迭代闭环 + 物理合成 + MCP for Claude Code + CPU-only + 5 个 coding agent 集成 = 「coding agent 多模态感官」严肃工程化范本

## 风险 / 局限 / 泡沫点
- **CPU-only 推理延迟（20-40s 每次 CLI call）：** 在 production-scale（每秒多次调用）下 latency 是瓶颈；进程内复用（MCP server）才稳
- **Recipe DSL 学习曲线：** forge 命令需要用户写物理合成 recipe（modal resonators + contact excitations + filtered noise + computed room + microphone）；新手不友好
- **Evolutionary search population/mutation 策略：** 在 budget=144 + reps=2 下的实际 search quality 未公开 benchmark；高维 recipe space 是否能 reach global optimum 未明
- **7 部专业 launch films 代表性：** 是哪 7 部？Apple iPhone launch 还是 Tesla Cybertruck 还是其他？是否真代表"professional"？
- **Gemini integration cost：** user-own-key + explicit-consent 模式，但 cost 不可忽视
- **本地模型集合来源 + 规模：** CLAP / AudioCLIP / PANNs / Wav2CLIP 等 fine-tune 版本的来源 + 训练数据 + 模型规模未公开，license 风险需检查
- **与 generative audio GAN/TTS 比较：** Stable Audio / ElevenLabs / Udio / MusicGen 的音质仍可能更自然；earshot forge 的优势在 recipe control + self-iteration 而非音色
- **与 Anthropic / OpenAI / Google 官方 audio-LLM 关系：** 是互补还是竞争？Claude / GPT / Gemini 都没有 native audio-LLM 公开 API（除 Gemini）
- **噪音素材 license：** forge recipe 中的 reference recordings 来自哪里？license 是否允许二次使用？
- **CLI 一次性进程：** 每次调用都要重新 load 模型（20-40s），效率低；MCP server 模式才能稳定
- **个人项目：** Leonxlnx 个人维护，长期可持续性
- **依赖 local CPU：** 在 ARM（如 Apple Silicon）vs x86 上的 performance 差异

## 与同类项目的关系
- **vs Stable Audio / ElevenLabs / Udio / MusicGen 等 generative audio：** 那些是 generative audio 模型（录制 + neural codec）；earshot 是 procedural + analytical（recipe + critic + evolutionary search）；不同路线可互补
- **vs CLAP / AudioCLIP / PANNs / Wav2CLIP 等 audio-LLM：** 那些是 audio-text embedding；earshot 用这些做底层模型 + 自加 earshot-specific tools（describe + match + realness 等）；是基础模型 vs 产品 vs 工具的层级关系
- **vs Wave-U-Net / Demucs / Spleeter 等 source separation：** 那些是 separate sources；earshot 是 analyze + synthesize + iterate；不同目标
- **vs librosa / PyAudio / soundfile 等 audio library：** 那些是基础 audio 处理；earshot 是 "AI agent → audio" 工具
- **vs Sonix / Descript 等 transcription：**：那些是 speech → text；earshot 是 "any sound → evidence + synthesize"
- **vs Anthropic / OpenAI native audio-LLM（待观察）：** 那些是 LLM-native audio；earshot 是 CPU-only local + recipe + self-iterate
- **vs audio production DAW（Logic Pro / Ableton / Reaper）：** 那些是 human-facing DAW；earshot 是 agent-facing + procedural + analytical

## 是否值得持续跟踪
**值得跟踪（Coding agent 时代多模态感官 + 自我迭代闭环）。** Leonxlnx/earshot 是「coding agent 听觉」+「recipe 物理合成」+「critic 量化打分」+「evolutionary search 自我迭代」+「MCP for Claude Code」严肃工程化范本。对游戏 audio / 播客 / UX audio / indie film / indie coder / 严肃 AI agent engineer，建议：
1. `pip install earshot` → 跑 `earshot doctor` 检装
2. `earshot describe keypress.ogg` + `earshot match ...` 试描述与匹配
3. `earshot forge keypress --refs path/to/real/keypresses/ --budget 144 --reps 2 --tone 1.5 --keep 4 --robust 8 --dir made/keypress` 试物理合成 + critic + evolutionary search
4. `earshot mcp` 启 MCP server，让 Claude Code / Cursor 等 call describe / match / forge

对 AI 生态观察者，它是「coding agent 多模态感官」+「自我迭代闭环」+「procedural + analytical 路线」严肃工程化范本，与 generative audio GAN/TTS 形成对比，值得持续关注：
- recipe DSL 的成熟度与可表达性
- earshot forge 出品音色的 naturalness vs real recording
- MCP server + Claude Code / Cursor / Codex / OpenCode 集成稳定性
- 与 Stable Audio / ElevenLabs / Udio / MusicGen 的实测音质对比
- evolutionary search 在高维 recipe space 的收敛性
- 7 部专业 launch films baseline 的代表性演化
- CPU-only 推理延迟改善
- Leonxlnx 后续工程

## 后续观察点
- **Recipe DSL 扩展性：** 能否处理更复杂的复合音色（金属 + 木头 + 玻璃）
- **Earshot forge 自然度：** 与 real recording 在双盲测试中的感知相似度
- **Evolutionary search 收敛性：** 在不同 budget / reps 下的 quality vs time
- **MCP for coding agents 集成深度：** Claude Code / Cursor / Codex / OpenCode 工作流集成案例
- **Gemini integration adoption：** user own key + consent 的实际 cost 与 utility
- **CPU-only 性能：** 在不同 CPU（Intel i7 vs AMD Ryzen vs Apple M3 Max）上的 latency benchmark
- **本地模型集合开源：** 是否完全开源 + Apache-2.0 / MIT
- **噪音素材 license：** forge recipe 中的 reference recordings license 来源
- **企业 / 商业采用：** 是否被 indie game studio / 播客制作公司 / UX audio 设计公司采用
- **与 generative audio GAN/TTS 的对比 benchmark：** 音质 / 速度 / cost / control 4 维度
- **与 Anthropic / OpenAI / Google 官方 audio-LLM 的关系：** 互补还是竞争
- **Leonxlnx 后续工程：** 是否出 multimodal 视觉 / 视频 / 触觉感官

---
> 数据来源: GitHub API (2026-10-17) | Stars: 302 | Forks: 19 | License: MIT | 语言: Python | 创建: 2026-10-15 | Size: 3429 KB
