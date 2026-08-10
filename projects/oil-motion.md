---
title: "oil-oil/oil-motion"
slug: "oil-motion"
date_added: "2026-08-11"
last_seen_date: "2026-08-11"
category: "工具型"
emoji: "🌊"
stars: "1,142 stars"
stars_delta: "+1,142 (新建项目首日观测)"
language: "Python"
license: "MIT"
score: 83
tags: ["agent-skill", "interactive-animation", "video-frames", "scroll-driven", "web-animation", "ai-video"]
url: "https://github.com/oil-oil/oil-motion"
---

# oil-oil/oil-motion

## 一句话定位
Agent 交互动画 Skill——让 AI 生成连续视频帧序列，再把用户的滚动/鼠标/拖动/触摸/设备方向操作映射到视频帧进度，把"线性播放的视频"变成"用户可控的交互动画"。

## 它解决的问题
AI 视频生成（如 H3、Sora 类工具）能产出高质量连续画面，但生成的视频只能从头播放到尾，无法与网页交互（滚动、鼠标、触摸）联动。开发者想让产品页面有"滚动展示产品拆解""鼠标控制角色朝向"等效果时，需要手动拆帧、编排、写前端交互代码——流程冗长且技术门槛高。Oil Motion 解决的是：**让 Agent 理解"交互动画"需求，自动完成 AI 视频生成→逐帧检查→资源压缩→前端交互绑定的全流程。**

## 为什么值得关注（2026-08-11）
- **新 Skill 品类——"AI 视频帧→交互"：** 此前 Skill 生态集中在"生成"（PPT、写作、代码），Oil Motion 首次将 AI 视频生成与前端交互绑定自动化，开创"AI 视频驱动的交互设计"品类。
- **快速增长：** 创建于 08-07，四天内达 1,142⭐ / 98 fork（API 可核验），增速在中文 Skill 生态中位居前列。
- **安装方式符合 Skill 生态范式：** README 明确"告诉 Agent：帮我安装这个 Skill"——与 Claude Skills / Hermes Agent 的自然语言安装范式一致。

## 热度来源判断
**判断：真实需求 + 中文 Skill 生态红利。** Oil Motion 的热度来自两个因素叠加：(1) AI 视频生成在 2026 年已成为基础设施（H3 生态爆发验证），但"把视频变成可交互内容"的工具链缺失是真实痛点；(2) 中文 Skill 生态正在快速扩张（human-writing、open-kimi-ppt-skill 验证），Oil Motion 填补了"设计/动画"垂直。fork 98 说明有实际集成尝试。需注意：subscribers 仅 1，深度关注者少，可能是早期热度驱动而非深度采用。

## 关键技术亮点
1. **进度映射引擎：** 核心思想是把 AI 生成的 N 帧视频映射到交互输入的 0-100% 进度。滚动到 30% 显示第 30 帧，反向滚动自然返回——同一映射机制适用于鼠标、拖动、触摸、设备方向。
2. **三段式工作流：** (a) 确认关键画面（开始/中间/结束应该是什么样）→ (b) AI 视频生成填充中间帧 → (c) 逐帧检查+删除异常+压缩+前端绑定。
3. **帧质量控制：** README 描述"逐帧检查，删除停顿、重复和异常画面"——说明不是简单截取，而是有质量过滤层。
4. **按显示尺寸压缩：** 资源整理环节按页面实际显示大小压缩，解决移动端加载体积问题。
5. **Agent 原生安装：** 符合 Skill 生态的"自然语言安装"范式（"帮我安装这个 Skill"），降低使用门槛。

## 架构启发
Oil Motion 的核心启发是**"AI 生成的连续内容不应止于播放，应成为交互的素材"**。当前 AI 视频生成的产物是 .mp4 文件——线性、不可逆、不可交互。Oil Motion 把视频"解构"为帧序列，再"重构"为可交互的动画对象。这与 sprite animation / scroll-driven video 的传统前端技术一脉相承，但用 AI 生成替代了手工制作帧序列。更深层的启发：**Skill 的价值不只在"生成"，更在"把生成物接入工程链路"**——Oil Motion 覆盖了从设计意图到前端实现的完整链路。

## 定位判断
**工具型 Skill（品类开创者）。** Oil Motion 在 Skill 生态中定位为"AI 视频驱动的交互动画"品类的开创者。与 human-writing（写作 Skill）、open-kimi-ppt-skill（PPT Skill）并列，它填补了"设计/动画"垂直。fork 98 显示有实际集成，但能否成为该品类的标准工具取决于迭代深度和社区采用。

## 风险 / 局限 / 泡沫点
- **帧序列的体积：** AI 生成的视频帧序列体积大（即使压缩），移动端加载性能是真实瓶颈。README 提到按显示尺寸压缩，但未给出具体体积基准。
- **交互平滑度依赖帧数：** 滚动映射需要足够多的帧才能平滑（100 帧 vs 30 帧体验差异大），帧数与生成成本/体积正相关。
- **深度关注不足：** subscribers 仅 1，说明当前热度可能由发现驱动而非深度使用验证。
- **AI 视频质量瓶颈：** 最终效果受限于 AI 视频生成的质量——若帧间不连贯，交互体验会很差。
- **竞品风险：** 若 Framer/Framer Motion 等成熟工具直接集成 AI 视频帧，Skill 的独立性可能被削弱。

## 与同类项目的关系
- **vs human-writing / open-kimi-ppt-skill：** 那些是文本/演示 Skill；Oil Motion 是视觉交互 Skill，品类不同但共享中文 Skill 生态红利。
- **vs Framer Motion / GSAP：** 成熟前端动画库需要手动编写动画逻辑；Oil Motion 用 AI 生成帧+自动映射，降低门槛但灵活度更低。
- **vs Apple Vision Pro 原生 scroll-driven media：** 平台级方案；Oil Motion 是跨平台的 Skill 方案。
- **vs 视频生成 Skill（MiniMax-H3 Skills）：** H3 Skills 生成视频；Oil Motion 消费视频（将生成结果转为交互素材），是上下游关系。

## 是否值得持续跟踪
**值得跟踪（AI 视频交互品类开创者）。** Oil Motion 代表了"AI 生成物→工程接入"的方向，这是 Skill 生态从"生成"走向"集成"的趋势信号。建议关注：帧序列在实际页面的加载性能、是否被前端社区（而不仅是 Skill 社区）采用、是否扩展到非视频的连续内容（如 3D 序列帧）。

## 后续观察点
- star 增速是否维持（当前四天 1,142⭐，需看是否进入稳态）
- 是否有实际部署案例（网站/产品使用 Oil Motion 产出的交互动画）
- 帧序列移动端加载性能的实际基准数据
- 是否被 Agent 平台（Claude Code / Hermes）官方推荐或集成
- 是否出现竞品或同类 Skill（品类扩散信号）

---
> 数据来源: GitHub API (2026-08-11) | Stars: 1,142 | Forks: 98 | Subscribers: 1 | License: MIT | 语言: Python | 创建: 2026-08-07
