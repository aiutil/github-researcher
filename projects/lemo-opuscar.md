---
title: "lemomo-ai/lemo-opuscar"
slug: lemo-opuscar
date_added: 2026-09-29
last_seen_date: 2026-09-29
category: "工具型"
emoji: "🎬"
stars: "512 stars"
stars_delta: "3 天 512⭐（粗略下限估计，created_at 2026-09-26 → 2026-09-29 总星数除以 3 天）"
language: "TypeScript / 视频生成"
score: 84
tags: ["lemo-opuscar", "opus-5-5", "claude", "claude-code", "ai-video", "ai-agents", "animation", "canvas", "webgl", "creative-coding", "filmmaking", "ffmpeg", "prompt-library", "text-to-speech", "threejs", "video-production", "motion-graphics", "agent-skill", "plugin-marketplace", "39-styles", "98-best-picture"]
url: "https://github.com/lemomo-ai/lemo-opuscar"
---

# lemomo-ai/lemo-opuscar

## 一句话定位
**39 种影片风格 × Opus 5.5 写代码导演** —— `claude plugin marketplace add lemomo-ai/lemo-opuscar` + `claude plugin install lemo-opuscar@lemolab` 一行装；选一个风格 + 自己的故事 + 让 coding agent 当导演；Canvas + WebGL 页面逐帧渲染 + 原创配乐 + 本地 TTS 配音；不用视频生成，也不用素材库画面。

## 它解决的问题
2026 年 AI 视频生成赛道火热的同构问题：**Opus 5.5 / Claude 等 coding agent 能用代码写出惊艳影片，但每个作品都要从 0 拼装 canvas / WebGL / 音轨 / TTS / 字幕 + 反复试错 + 风格散乱** —— 没有风格库 / 没有可复用 pipeline / 没有"装一次就能用"的 agent skill / 没有导演 + 配乐 + 混音的工作流自动化 / 没有从"用户说一句话"到"成片 + 1080p 下载"的全链路。
lemo-opuscar 直击这一痛点：它给 Claude 一个**完整的影片工厂 skill** —— `claude plugin install` 装一次 → 任何目录 → 说一句"用油画厚涂风格做 30 秒讲我家那只橘猫" → 自动出成片（Canvas / WebGL 渲染 + 原创音乐 + 本地 TTS + 1080p MP4 下载）。39 种风格 + 导演 + 技术指南 + 风格提示词（约 60 MB），全部本地缓存 `~/lemo-opuscar`。

## 为什么值得关注（2026-09-29）
- **Stars:** 512（截至 2026-09-29），3 天突破 500，**09-26 ~ 09-29 Jev/Opus 视频严肃工程化多线铺开中的典型样本**
- **Forks:** 67，**fork/star 13.1%** 较健康 + AI 视频 skill 严肃工程化持续关注信号
- **License:** NOASSERTION（含 docs 图像与可商用样式表的实际状态需要核验）
- **语言:** TypeScript / JavaScript + Canvas / WebGL / Three.js（按风格混用）
- **规模:** 107227 KB（约 105 MB —— 含 39 部样片 + 39 个样式文件 + 工具脚本）
- **活跃度:** created 2026-09-26，pushed_at 2026-09-28，持续高活跃
- **Topics:** 15 个（ai-agents / ai-video / animation / canvas / claude / claude-code / creative-coding / ffmpeg / filmmaking / motion-graphics / prompt-library / text-to-speech / threejs / video-production / webgl）覆盖清晰
- **核心作品:** OPUSCAR 98 —— 98 Years of Best Picture · 1927 – 2025 · 6:25；一个 Clawd 走过 98 部最佳影片，每部换贴合那部电影的画风
- **首页:** https://lemomo-ai.github.io/lemo-opuscar/ 在线 gallery
- **安装:** `claude plugin marketplace add lemomo-ai/lemo-opuscar` + `claude plugin install lemo-opuscar@lemolab`

## 热度来源判断
lemo-opuscar 的热度是 **"AI 视频严肃工程化 + Opus 5.5 写代码 + 39 种风格 + agent skill plugin marketplace + 60 MB 本地缓存"** 的强劲组合。Opus 5.5 09-26 ~ 09-27 推出后，**"Opus 5.5 写代码做视频"成为新趋势**：yihui-dev/awesome-opus5-5-videos 09-27（692⭐ / 80f）聚合了 389 个 X 视频 + 提示词；lemo-opuscar 09-26（512⭐ / 67f）给出一个**结构化、可复用的严肃工程化 skill**；feitangyuan/onetake 09-26（814⭐ / 53f）给出一个**一镜到底连贯动效的 agent skill**；Rieranthony/product-film-skill 09-26（356⭐ / 25f）给出一个**Remotion + 你的设计系统的产品片 skill**。**lemo-opuscar 的关键差异**：它不是单点作品，而是 **39 种风格的完整工具链 + plugin marketplace 二次分发 + 60 MB 本地缓存**——把"Opus 5.5 写代码做视频"从单点作品推到**风格化 + 严肃工程化 + agent skill 二次分发**。512⭐ / 67f / fork/star 13.1% 与 yihui-dev/awesome-opus5-5-videos 692⭐ / 80f / 11.6% 同步，反映**"Opus 5.5 视频严肃工程化"的典型严肃工程化 fork 率特征**。热度**真实且具严肃工程化生态价值**——这是 "Opus 5.5 视频严肃工程化从单点作品 → 风格化 + plugin marketplace + 本地缓存" 演化关键信号。

## 关键技术亮点
1. **39 种影片风格** —— watercolor / 油画厚涂 / 多 Clawd 历险等 39 种可复用 style prompt + 短片样片 + 导演与技术指南
2. **OPUSCAR 98 范例作品** —— 98 Years of Best Picture · 1927 – 2025 · 6:25；每一帧 + 每一音符 + 每一刀剪辑都是 Opus 5.5 写代码
3. **两层安装路径** —— plugin marketplace 安装（推荐）/ clone 仓库
4. **60 MB 本地缓存** —— `~/lemo-opuscar` 共享所有片子的指南 + 工具 + 风格提示词；每片子放在发起时所在文件夹
5. **Canvas + WebGL 逐帧渲染** —— 不用视频生成，不用素材库画面
6. **原创配乐** —— 免费采样库写原创音乐
7. **本地 TTS 配音** —— text-to-speech 配音（不是 cloud TTS）
8. **成片 + 1080p 下载** —— `git clone` 仓库下载 1080p MP4（如 opuscar98.mp4）
9. **Onboarding 询问** —— 一上来问：风格 + 故事 + 是否有 voice / music / material + 是否先看 storyboard
10. **双语 README** —— 中英双语完整文档（英文 + 简体中文）
11. **plugin/skills/lemo-opuscar/** —— 可复制到其他 agent 的 skills 目录（不仅 Claude Code / Codex / OpenCode / Cursor 等）
12. **topics 15 个** —— ai-agents / ai-video / animation / canvas / claude / claude-code / creative-coding / ffmpeg / filmmaking / motion-graphics / prompt-library / text-to-speech / threejs / video-production / webgl

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 视频生成领域的 agent skill + style library + 导演工作流，仓库是 skill manifest + 39 风格产物 | 描述层准确；具体 skill runtime（plugin 解析、style prompt 注入、tools 调度）均待核验 |
| 主路径 | 用户说"风格 + 故事" → plugin marketplace 安装 → skill 拉取 60 MB 本地缓存 → agent 按 style prompt + 导演指南写代码 → canvas / WebGL 逐帧渲染 → ffmpeg 合成 → 1080p MP4 输出 | 主路径为 README 表述；plugin 安装是 marketplace 二次分发；具体 skill 内部 action list、style 缓存策略、ffmpeg 模板均待核验 |
| 关键权衡 | 风格广度（39 种） vs 风格深度（每种需导演 + 配乐 + 调色 vs Opus 5.5 适配深度） vs plugin marketplace 兼容性 vs 60 MB 本地缓存的用户接受度 vs 不用云端视频模型的算力门槛 | README 明示"风格是按 Opus 5.5 调出来的，换成其他模型不保证能做出同样的效果"——单一模型依赖是核心权衡；39 风格的实际质量分级、跨模型迁移能力未证实 |
| 最小 PoC | 在单 Claude Code 上 `claude plugin install lemo-opuscar@lemolab`，选 1 个简短风格（建议 watercolor）做 15 秒样片，验证：(1) 60 MB 缓存下载完整 (3) canvas / WebGL 渲染无 ffmpeg 错误 (4) 1080p MP4 成功导出 (5) style prompt 是否对其他模型有效 | PoC 范围、退出路径由 README"先单风格、最短时长、可下载验证"建议推导；具体 style 质量、ffmpeg 失败率、其他模型兼容性待核验 |

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[用户说"风格 + 故事"] --> PluginInstall[plugin marketplace add<br/>plugin install lemo-opuscar@lemolab]
  PluginInstall --> Skill[Claude Code Skill<br/>plugin/skills/lemo-opuscar]
  Skill --> Cache[本地缓存 ~/lemo-opuscar<br/>指南 + 工具 + 风格提示词 约 60 MB 待核验]
  Cache --> StylePrompt[Style Prompt<br/>39 种风格选一]
  StylePrompt --> Opus55[Claude Opus 5.5<br/>写代码导演]
  Opus55 --> Canvas[Canvas 逐帧渲染]
  Opus55 --> WebGL[WebGL / Three.js 逐帧渲染 待核验]
  Opus55 --> Music[原创配乐<br/>免费采样库]
  Opus55 --> TTS[本地 TTS 配音]
  Opus55 --> FFmpeg[ffmpeg 合成<br/>1080p MP4]
  Canvas --> FFmpeg
  WebGL --> FFmpeg
  Music --> FFmpeg
  TTS --> FFmpeg
  FFmpeg --> Output[成片 1080p MP4<br/>可下载]
  Output --> Gallery[在线 gallery<br/>lemomo-ai.github.io/lemo-opuscar]
  Skill -.可选其他 agent 复制.-> OtherAgent[Codex / OpenCode / Cursor<br/>复制到 skills 目录]
  Skill -.Onboarding.-> Check[询问 voice / music / material<br/>storyboard 选择]
  Check --> Opus55
  Opus55 -.单一模型依赖.-> Risk[Opus 5.5 升级<br/>风格可能失效 待核验]
```

## 架构启发
lemo-opuscar 的核心启发是 **"agent skill 不只是单点工具，而是完整的风格化工作流 + plugin marketplace 二次分发 + 本地缓存"**。当前 Agent Skill 生态多以单点工具为主（onelake 一镜到底 / company-brain 商用副驾 / logo-design-skill logo 设计 / 3dicon 一个 prompt 3D 图标），但 lemo-opuscar 把"风格库 + 导演指南 + 本地缓存 + plugin marketplace 安装"四件事同时推到严肃工程化形态——这意味着 **agent skill 已从"单点工具" → "完整工作流 + plugin 二次分发"演化**。更深层的启发：**Opus 5.5 单一模型依赖** ——"风格是按 Opus 5.5 调出来的，换成其他模型不保证能做出同样的效果"——这是严肃工程化 agent skill 的关键权衡：模型升级可能让风格失效。

## 定位判断
**风格化 AI 视频 Agent Skill 的具体路径（工具型 + 严肃工程化）。** lemo-opuscar 不仅是 39 部样片的合集，更是 **"Opus 5.5 写代码做视频" 的严肃工程化模板**——把风格库 + 导演指南 + 本地缓存 + plugin marketplace 同时落地。512⭐ + 67f 已显示严肃工程化持续关注。但"单一 Opus 5.5 依赖"是核心风险——模型升级时风格需要重调。目前定位是"Opus 5.5 视频严肃工程化最具代表性的完整工作流"，向 plugin marketplace 二次分发 + 多模型适配是合理演化。

## 风险 / 局限 / 泡沫点
- **单一 Opus 5.5 模型依赖** ——"风格是按 Opus 5.5 调出来的，换成其他模型不保证能做出同样的效果"；Opus 5.5 升级时风格可能失效
- **39 风格的质量不均** —— 39 部样片不是每一部都完美，质量分级可能压低整体口碑
- **60 MB 本地缓存用户接受度** —— 首次使用下载 60 MB；不接受者可能放弃
- **plugin marketplace 兼容性** —— 仅明示 Claude Code；Codex / OpenCode / Cursor / Copilot 兼容性需自复制 skills 目录
- **本地 TTS 配音质量** —— 非云端 TTS（ElevenLabs / Azure），配音质量可能不如云端
- **NOASSERTION 许可** —— 仓库无明示许可；商用复用边界需用户自行核验
- **个人开发者属性** —— Lemomo 个人维护；持续维护承诺 + 多模型适配 = 长期风险
- **算力门槛** —— ffmpeg + canvas / WebGL 渲染需要 CPU / GPU 算力；端到端时间可能较长

## 与同类项目的关系
- **vs yihui-dev/awesome-opus5-5-videos（09-27 692⭐）:** awesome list 聚合 389 个 X 视频 + 提示词；lemo-opuscar 是 39 种风格的严肃工程化 skill
- **vs feitangyuan/onetake（09-26 814⭐）:** 一镜到底连贯动效 + probe.py oracle carry score；lemo-opuscar 是多风格 + 完整影片
- **vs Rieranthony/product-film-skill（09-26 356⭐）:** Remotion + 你的设计系统的产品片 skill；lemo-opuscar 是 39 种风格库
- **vs anishfn/shapeshift（09-26 ~ 09-29 持续）:** Jev 应用层 UI 端具身；lemo-opuscar 是 Opus 5.5 应用层视频
- **vs lhlGitHub/threejs-architecture-effects（09-24）:** Three.js 古建程序化动态组装；lemo-opuscar 是多风格视频工具链

## 是否值得持续跟踪
**值得跟踪（Opus 5.5 视频严肃工程化风格化代表样本）。** lemo-opuscar 代表了 **"Opus 5.5 写代码做视频" 从单点作品 → 风格化 + plugin marketplace + 本地缓存 + 双语 README** 的演化方向。建议关注：(1) 39 种风格在 Opus 5.5 升级时的稳定性；(2) plugin marketplace 兼容性是否扩展到 Codex / OpenCode / Cursor；(3) 60 MB 本地缓存用户接受度与首次使用完成率；(4) NOASSERTION 许可是否补成明示 Apache-2.0 / MIT；(6) 多模型适配是否支持（GPT-Image / Gemini / Seedance）。对 Agent Skill 用户，这个 skill 是"Opus 5.5 多风格视频"的实用模板，值得直接采用。

## 后续观察点
- 39 种风格的样本质量分级（哪些风格最被引用、哪些被 fork 最多）
- plugin marketplace 在 Codex / OpenCode / Cursor / Copilot 的兼容性扩展
- 60 MB 本地缓存下载完成率与用户放弃率
- NOASSERTION 许可是否补成明示 Apache-2.0 / MIT
- 是否支持其他视频生成模型（GPT-Image / Gemini / Seedance / Luma）
- 是否新增更多风格 + 多 Clawd 历险 + 用户自定义风格
- OPUSCAR 98 之外是否推出 100 / 198 / 短视频 + 长视频混合系列
- 双语 README 在中文用户与英文用户的覆盖广度
- docs 与 plugin 同步更新频率

---
> 数据来源: GitHub API (2026-09-29) | Stars: 512 | Forks: 67 | License: NOASSERTION | 语言: TypeScript | 创建: 2026-09-26 | 规模: 107227 KB