---
title: "EverettFish/holo-card-studio"
slug: holo-card-studio
date_added: 2026-09-08
last_seen_date: 2026-09-08
category: "工具型"
emoji: "🃏"
stars: "779 stars"
stars_delta: "1 天 0→779⭐，单日均速 ~779⭐/day；Codex Skill 把'一句话描述'变成可拖拽 3D 全息闪卡"
language: "Python"
score: 92
tags: ["3d-pipeline", "agent-skill", "blender", "codex", "everettfish", "holographic", "python", "three-js"]
url: "https://github.com/EverettFish/holo-card-studio"
---

# EverettFish/holo-card-studio

## 一句话定位
Codex Skill 把"一句话描述"或参考图变成可拖拽、可翻面、含镭射全息效果的 3D 闪卡——四层图（主体 / 背景 / 线稿 / 文字）+ Blender 工程 + Three.js 网页，Python 项目，1 天 779⭐，是 2026-09-08 GitHub Trending 新项目榜首。

## 它解决的问题
2026 年 Codex / Claude Code / Cursor 等 Coding Agent 已经能写代码、改文件，但绝大多数仍无法直接产出"影视级 / 可交互的内容"。朋友圈晒图、PPT 介绍页、独立游戏角色卡、团队纪念卡等场景需要：(a) 视觉冲击力（镭射 / 闪光 / 3D 视差）；(b) 可交互（拖拽 / 翻面 / 滑块）；(c) 可编辑（拿到 Blender 工程而不是渲染图）。`holo-card-studio` 直击这一痛点：用 Codex Skill 把"一句话"变成可拖拽的 3D 全息闪卡 + 可编辑 Blender 工程，零美术基础也能做"传说稀有度"闪卡。

## 为什么值得关注
- **Stars:** 779（截至 2026-09-08），1 天净增，单日均速 ~779⭐/day
- **Forks:** 123（fork/star **15.8%**，远高于 magnitude 7.2% / fastpotify 4.4%——反映真实开发者使用，不是营销放大）
- **语言:** Python 主导（README + 流水线脚本）
- **项目年龄:** 1 天（创建 2026-09-07），是 9-08 trending 新项目榜首
- **核心差异:** Codex Skill 协议（agentskills.io）+ Blender 自动下载（SHA-256 校验）+ Three.js 网页实时渲染

## 热度来源判断
`holo-card-studio` 的热度来自三个趋势的交汇：(1) **Codex Skill 内容市场成型**——继 9-07 `Nanako0129/sepia`（"Skill CLI"）之后，holo-card-studio 把 Skill 模式推到"具体场景 Skill"（闪卡 / 游戏卡 / 纪念卡）；(2) **3D 内容 / Blender + Three.js 栈成熟**——M3 Expressive / Apple Liquid Glass 等设计语言推 3D UI 普及；(3) **小红书教程 + Twitter 视觉冲击**——README 顶部明示"实现教程来源：@乌托邦的香蕉🍌"（小红书），短视频教程 + 实测截图驱动传播。

1 天 779⭐ / fork 123（fork/star 15.8%）的组合反映 **"真实开发者采用 + 视觉冲击力 + 可直接运行"** 三者叠加——不是营销放大，是真实需求。

## 关键技术亮点
1. **四层图流水线:** 主体 / 背景 / 线稿 / 文字 独立生成 + UV 对齐；每层独立可控（视差 / 镭射 / 星光）
2. **Blender 自动下载 + SHA-256 校验:** 不依赖用户预装 Blender，项目自带便携版 Blender + 校验 SHA-256；项目自带、互不干扰
3. **Three.js 网页实时渲染:** 按同一套 UV 公式重建四层合成，与 Blender 离线渲染像素级一致；浏览器端纯 Three.js，无 WebGL 自定义
4. **可编辑 Blender 工程:** `card.blend` 是真实可编辑 Blender 工程，节点组用中文命名（缩放 / 深度 / 视差效果 / 镭射条纹 / 星光 / 线稿发光）
5. **Codex Skill 协议触发:** 安装到 `~/.codex/skills/holo-card-studio/`，SKILL.md 触发；自然语言输入即可
6. **三种交付物:** 本地网页链接（拖/转/翻/拉滑块）+ `card.blend`（Blender 工程）+ 渲染图（PNG）

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | Codex Skill 层 + 4 层图流水线 + Blender 离线渲染 + Three.js 网页实时渲染；Skill 协议层负责触发，流水线层负责生成，渲染层负责呈现 | 边界由 README 明示；具体图像生成模型（Imagen / DALL-E / Stable Diffusion）需 README 核验 |
| 主路径 | 用户描述 → Codex Skill 触发 → 4 层图像生成（ImageGen）→ Blender 场景构建 → 视差/镭射/星光材质 → 离线渲染 + Three.js 重建 → 输出 `card.blend` + 网页链接 | 主路径为 README 语义抽象；具体 ImageGen 调用方式与 Blender MCP 集成方式需代码审阅 |
| 关键权衡 | Blender 自动下载的供应链安全（SHA-256 校验需用户主动触发）vs 一键部署 UX；4 层图独立生成 vs 主体一致性；Three.js 实时重建 vs 离线渲染质量 | README 标注"项目自带 Blender + 校验 SHA-256"；4 层图一致性的工程实现未在 README 可见 |
| 最小 PoC | 安装 Codex Skill → 输入"水墨风锦鲤闪卡 No.001" → 等待流水线完成 → 浏览器打开本地链接 → 拖拽测试视差 + 翻面测试 → 检查 `card.blend` 可编辑 | PoC 范围由 README "Quick start" 推导；具体资源消耗（API 成本 + Blender 渲染时间）需 benchmark |

## 架构启发
`holo-card-studio` 的核心启发是 **"Agent Skill 不只是文档，也可以是 3D 内容流水线"**。传统 Skill 模式（humanizer / sepia / screenwriting-skills）输出"文字建议"或"指令转换"；holo-card-studio 输出"3D 内容"。更深层的启发是 **"Skill 触发 + 流水线生成 + 多端呈现" 三段式架构**——Skill 是接口（自然语言触发），流水线是后端（Blender + ImageGen + Three.js），呈现是多端的（Blender 工程 + 网页链接 + 渲染图）。

风险提示：**"preserve the requested subject, style, typography" 是营销话术**，主体一致性（保留猫的神态）需要 benchmark；**Blender 自动下载是供应链攻击面**——SHA-256 校验仅当用户主动触发。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[用户] --> NL[自然语言描述<br/>或上传参考图]
  NL --> Skill[Codex Skill<br/>SKILL.md 触发]
  Skill --> Pipeline[4 层图流水线<br/>主体/背景/线稿/文字]
  Pipeline --> ImageGen[图像生成<br/>ImageGen 待核验]
  ImageGen --> Layers[四层 PNG<br/>subject/background/lineart/text]
  Layers --> Blender[Blender 场景构建<br/>视差/镭射/星光]
  Blender --> Render[离线渲染<br/>PNG 输出]
  Blender --> Blend[card.blend<br/>可编辑工程]
  Layers --> ThreeJS[Three.js 重建<br/>实时渲染]
  ThreeJS --> Web[本地网页<br/>拖/转/翻/滑块]
  Render --> Web
  Skill -.agentskills.io.-> Codex[Codex Runtime]
  Blender -.自动下载 + SHA-256.-> BlenderBin[便携 Blender<br/>项目自带]
```

## 定位判断
**工具型项目（Codex Skill → 3D 内容流水线），向"内容 Skill 市场"演进。** `holo-card-studio` 不仅是一个 Skill，更是 Skill 模式从"指令"扩展到"内容"的开端。1 天 779⭐ / fork/star 15.8% 已显示真实需求。但 Skill 内容的扩展取决于：(a) 图像生成模型的成本 / 质量；(b) Blender 自动下载的供应链安全；(c) 与 Anthropic Skills / Codex plugins 协议的竞争。当前定位是"Codex Skill 3D 内容头部样本"，向 Skill Marketplace 演进是合理路径。

## 风险/局限/泡沫点
- **Blender 自动下载的供应链攻击面:** 项目自带便携 Blender + 校验 SHA-256，但哈希校验仅当用户主动触发；恶意 commit 可能注入恶意 Blender 二进制
- **4 层图一致性的工程实现:** "preserve the requested subject" 是营销话术，主体一致性（保留猫的神态）需要 benchmark
- **Codex Skill 协议的封闭性:** 与 Anthropic Skills / OpenAI Codex plugins / Cursor Skill 协议的竞争需要观察；agentskills.io 是否成为跨 Runtime 标准需要观察
- **图像生成模型成本:** 单次闪卡生成需要 4 次 ImageGen 调用（主体 / 背景 / 线稿 / 文字），API 成本不可忽视
- **1 天新项目风险:** EverettFish 是新 GitHub 账号（holo-card-studio 是其首个 100+⭐ 项目），项目可持续性 / 治理结构 / 安全漏洞响应都未验证
- **"3D 全息闪卡"概念营销化:** 实际效果可能不及短视频宣传的"传说稀有度"视觉冲击；Blender 离屏渲染 + Three.js 重建的实际像素差异需要测试

## 与同类项目的关系
- **vs kacperkapusciak/goldie (9-06, 1856⭐):** goldie 是 AI 直接产出 App Store 预览图；holo-card-studio 是 AI 产出可交互 3D 闪卡——输出形态不同（图片 vs 网页）
- **vs achimala/dream-loop (1 天 121⭐):** dream-loop 是图像生成 + 子 Agent 批评闭环；holo-card-studio 是固定 4 层流水线——自动化程度不同（dream-loop 是开放循环，holo-card-studio 是封闭流水线）
- **vs Tejashmakwana/astra-chatgpt-hyperframes (2 天 130⭐):** hyperframes 保留原视频 180 帧 + 替换文字层；holo-card-studio 是从零生成 3D 内容——输入模式不同（参考 vs 零起点）
- **vs anthropics/skills (9-06, 252K⭐):** anthropics 是 Anthropic 官方 Skills；holo-card-studio 是社区 Codex Skill——协议 / 平台不同
- **vs Nanako0129/sepia (9-07, 2324⭐):** sepia 是 77+ Agent 兼容的 deAI Skill；holo-card-studio 是单一场景（闪卡）的 Codex Skill——宽度 vs 深度

## 是否值得持续跟踪
**值得跟踪（Codex Skill → 3D 内容流水线头部样本）。** `holo-card-studio` 代表了 Skill 模式从"指令 / 文字"升级到"3D 互动内容"的方向，与 Codex Skill 协议 + Blender + Three.js 栈 + 1 天 779⭐ 共同构成新方向。无论其本身成败，这一方向是行业趋势。建议关注：(a) 图像生成模型的成本 / 质量；(b) Blender 自动下载的供应链安全治理；(c) 与 Anthropic Skills / Codex plugins 协议的兼容性；(d) Skill 内容市场的演进。对 Content Creator / Indie Game Developer，holo-card-studio 是零美术基础做 3D 闪卡的开源方案。

## 后续观察点
- 图像生成模型的具体选择（Imagen / DALL-E / Stable Diffusion）
- 4 层图一致性的工程实现（diffusion seed / ControlNet / 其他）
- Blender 自动下载的供应链安全治理（是否引入签名验证）
- 与 Anthropic Skills / Codex plugins 协议的兼容性测试
- Skill 内容市场是否成型（Codex Skill Marketplace）
- 多语言 / 多风格扩展（除闪卡外的卡牌类型）
- 性能 benchmark（单次闪卡的 API 成本 + 渲染时间）

---
> 数据来源: GitHub API (2026-09-08) | Stars: 779 | Forks: 123 | License: 待核验 | 语言: Python | 创建: 2026-09-07
