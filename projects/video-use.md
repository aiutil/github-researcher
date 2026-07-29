---
title: "video-use"
slug: "video-use"
date_added: "2026-04-18"
category: "工具型"
emoji: "🎬"
stars: "903 stars"
stars_delta: "5天900星"
language: "Python"
score: 75
tags: ["Video Editing", "Claude Code", "Agent Skill", "ffmpeg", "browser-use"]
url: "https://github.com/browser-use/video-use"
---

# video-use

## 一句话定位
browser-use 团队出品的 Claude Code Skill，用自然语言指令让 Agent 完成视频编辑——自动剪辑、调色、字幕、动画，输出 final.mp4。

## 它解决的问题
视频编辑门槛高、工具复杂（Premiere/FCP/DaVinci）。非专业用户想做的只是：去填充词、调色、加字幕、生成动画。video-use 让这些通过对话完成。

目标用户：内容创作者、教程制作者、自媒体运营。

## 为什么值得关注（2026-04-18）
browser-use 团队出品（browser-use 本身是知名的 Browser Automation 项目），5天 903 星。代表了 Claude Code Skill 从"开发工具"延伸到"内容生产"的趋势。

## 热度来源判断
- browser-use 团队的品牌效应
- "用 Claude Code 剪视频"的噱头吸引力强
- 功能完整度高，不是 demo
- 视频编辑是真实需求场景

## 关键技术亮点
1. **Agent 自评估**：在每个切点边界自评估渲染结果，质量门控
2. **会话记忆持久化**：project.md 记录编辑历史，下次会话可续接
3. **并行子 Agent 调度**：Manim/Remotion/PIL 动画通过并行子 Agent 生成
4. **30ms 音频淡入淡出**：每个切点自动处理，避免爆音

## 架构启发
多步骤 Skill 的质量管控流程设计值得借鉴：自评估 + 会话记忆 + 并行子 Agent 调度。这不是简单的"调用 ffmpeg"，而是给 Agent 赋予了完整的视频编辑工作流。

## 定位判断
垂直内容工具。不具备平台化或基础设施潜力，但作为 Skill 生态的标杆案例值得关注。

## 风险 / 局限 / 泡沫点
1. **依赖链重**：需要 ffmpeg、yt-dlp、ElevenLabs API、Manim/Remotion
2. **视频质量上限**：AI 驱动的自动编辑无法替代专业剪辑师
3. **Claude Code 绑定**：强依赖 Claude Code 生态

## 与同类项目的关系
- **Remotion**：React 视频框架，底层技术
- **MoviePy**：Python 视频编辑库
- **CapCut/剪映**：消费级视频编辑器，AI 辅助但非 Agent 驱动

## 是否值得持续跟踪
短期跟踪。作为 Skill 生态标杆观察。

## 后续观察点
1. browser-use 团队是否会持续投入
2. 用户实际编辑效果的质量
3. 是否出现类似的音频/图片编辑 Skill

---
*首次记录：2026-04-18*
