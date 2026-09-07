---
title: "VII-Cae/hyalite--liquid-glass"
slug: "hyalite-liquid-glass"
date_added: 2026-09-08
last_seen_date: 2026-09-08
category: "工具型"
emoji: "💧"
stars: "102 stars"
stars_delta: "1 天 0→102⭐，单日均速 ~102⭐/day；纯 CSS 真折射液态玻璃"
language: "JavaScript"
score: 70
tags: ["backdrop-filter", "css", "hyalite", "javascript", "liquid-glass", "refraction", "sdf", "svg", "vii-cae"]
url: "https://github.com/VII-Cae/hyalite--liquid-glass"
---

# VII-Cae/hyalite--liquid-glass

## 一句话定位
Real refraction "liquid glass" for the web——**SDF 镜头映射 + SVG displacement + backdrop-filter**，单文件无 WebGL 无构建步骤；中心清晰 + 边缘内收（弯曲而非涂抹），是 Apple Vision Pro "Liquid Glass" 设计语言的开源纯 CSS 实现；1 天 102⭐，fork 7，JavaScript。

## 它解决的问题
2026 年 Apple Vision Pro 推出 "Liquid Glass" 设计语言——真实折射、弯曲边缘、深度感。社区尝试在 Web 复现该设计语言时面临三大痛点：(a) **WebGL / Canvas 太重**——大多数实现依赖 WebGL 自定义 shader，启动慢 / 兼容性差；(b) **纯 backdrop-filter blur 是模糊而非折射**——`backdrop-filter: blur(10px)` 是高斯模糊，不弯曲；(c) **构建步骤繁琐**——大多数实现需要 npm install / Vite / React 集成。`hyalite` 直击这三点：(a) **SDF 镜头映射 + SVG displacement filter**——纯 CSS / SVG 路径；(b) **真实折射**——边缘弯曲而非涂抹；(c) **单文件无构建**——直接 `<script>` / `<link>` 引入即可。

## 为什么值得关注
- **Stars:** 102（截至 2026-09-08），1 天净增，单日均速 ~102⭐/day
- **Forks:** 7（fork/star 6.9%，接近 magnitude 7.2%）
- **语言:** JavaScript 主导（CSS / SVG）
- **项目年龄:** 1 天（创建 2026-09-07）
- **核心差异:** SDF + SVG displacement + backdrop-filter + 单文件 + 真实折射（弯曲而非涂抹）

## 热度来源判断
`hyalite` 的热度来自三个因素：(1) **Apple Liquid Glass 设计语言普及**——Apple 在 2025-2026 年推 Liquid Glass 设计语言，社区对 Web 实现需求大；(2) **纯 CSS 实现的稀缺**——大多数 Liquid Glass 实现依赖 WebGL / React，纯 CSS 实现稀缺；(3) **可验证性**——README 提供 regression cases 页（`cases.html`）+ 命令行测试脚本（`demo/run-cases.mjs`）——可验证性极高。

1 天 102⭐ / fork 7（fork/star 6.9%）的组合反映 **"纯 CSS 真实折射 + 可验证 + 零依赖"** 三者叠加。

## 关键技术亮点
1. **SDF 镜头映射:** "computes a lens map for the element's exact size and corner radii"——为每个元素尺寸 + 圆角计算镜头映射
2. **SVG displacement filter:** "feeds it to an SVG filter"——把镜头映射送到 SVG 滤镜
3. **backdrop-filter:** "lets the browser bend whatever is behind the element through backdrop-filter: url(#…)"——把 SVG 滤镜挂到 backdrop-filter
4. **真实折射（弯曲而非涂抹）:** "Straight lines curve, not smear"——边缘内收，中心清晰
5. **零依赖:** "One file, no WebGL, no build step"——单文件直接引入
6. **可验证性:** regression cases 页（`demo/cases.html`）+ 命令行测试脚本（`demo/run-cases.mjs`）——自动验证渲染正确性

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 纯 CSS / SVG 渲染层——SDF + SVG displacement filter + backdrop-filter；关键是"无 WebGL / 无构建"vs"WebGL 自定义 shader" | 边界由 README 明示；具体 SDF 镜头映射的实现（解析 vs 查表）需 README 核验 |
| 主路径 | 元素尺寸 + 圆角 → SDF 镜头映射 → SVG displacement filter → backdrop-filter url() → 浏览器渲染弯曲折射 | 主路径为 README 语义抽象；具体 SVG displacement filter 的参数（bevel / thickness / blur / dispersion / rim）需 README 核验 |
| 关键权衡 | 纯 CSS 实现的零依赖（vs WebGL 通用性）；SDF 近似（vs 物理光路追踪精度）；单文件零构建（vs 可维护性） | README 列出演示参数（bevel / thickness / blur / dispersion / rim）；具体浏览器兼容性需 benchmark |
| 最小 PoC | 在 Chromium 浏览器打开 `demo/index.html` → 拖拽 / 切换 / 调参（bevel / thickness / blur / dispersion / rim） → 对比"plain blur vs hyalite" → 运行 `node demo/run-cases.mjs`（Node 22+）验证 | PoC 范围由 README "Live" + "cases.html" 推导；具体渲染精度与浏览器兼容性需 benchmark |

## 架构启发
`hyalite` 的核心启发是 **"真实折射不一定要 WebGL，SDF + SVG displacement filter 即可"**。传统 Liquid Glass 实现依赖 WebGL 自定义 shader，启动慢 / 兼容性差；hyalite 走 **"SDF + SVG filter"** 路线——纯 CSS / SVG 实现，零依赖 / 跨浏览器。

更深层的启发是 **"设计语言的开源化"**——Apple Liquid Glass 是 Apple 私有设计语言；hyalite 是 **"逆向工程 + 开源实现"**——任何 Web 页面都能用 Liquid Glass 效果，不依赖 Apple 生态。

风险提示：**浏览器兼容性**——`backdrop-filter` + SVG displacement filter 在 Safari / Chrome / Firefox 的实现差异需要测试；**真实折射 vs 模拟折射**——SDF 是近似计算，与物理折射（光路追踪）的差距需要视觉对比。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Element[HTML 元素<br/>尺寸 + 圆角] --> SDF[SDF 镜头映射<br/>有符号距离场]
  SDF --> Filter[SVG displacement filter<br/>feDisplacementMap]
  Filter --> CSS[CSS backdrop-filter<br/>url(#…)]
  CSS --> Browser[浏览器渲染<br/>弯曲折射]
  Browser --> Visual[真实折射效果<br/>中心清晰 + 边缘内收]
  Filter -.参数.-> Params[bevel / thickness / blur<br/>dispersion / rim]
  SDF -.零依赖.-> Zero[无 WebGL<br/>无构建步骤<br/>单文件]
  Browser -.兼容性.-> Compat[Safari / Chrome / Firefox<br/>实现差异需测试]
  SDF -.近似.-> Accuracy[SDF vs 物理光路追踪<br/>精度差距]
  Repo[hyalite 仓库] --> Demo[demo/index.html<br/>playground]
  Repo --> Cases[demo/cases.html<br/>regression cases]
  Repo --> Run[demo/run-cases.mjs<br/>命令行测试]
  Run -.Node 22+.-> Verify[npm test 验证<br/>red/green exit code]
```

## 定位判断
**工具型项目（纯 CSS Liquid Glass 实现），向"Web 设计语言开源化"演进。** `hyalite` 不仅是一个 CSS 库，更是 Apple Liquid Glass 设计语言在 Web 端开源实现的样本。1 天 102⭐ / fork/star 6.9% 已显示初步关注。当前定位是"Web Liquid Glass 头部开源实现"，向"Web 设计语言开源化生态"演进是合理路径。

## 风险/局限/泡沫点
- **浏览器兼容性:** `backdrop-filter` + SVG displacement filter 在 Safari / Chrome / Firefox 的实现差异需要测试；移动端兼容性需要 benchmark
- **真实折射 vs 模拟折射:** SDF 是近似计算，与物理折射（光路追踪）的差距需要视觉对比
- **单文件 / 零构建的可维护性:** 102⭐ 项目的代码组织是否经得起规模化使用需要 benchmark
- **性能:** 复杂场景（多层 Liquid Glass / 大尺寸元素）的渲染性能需要测试
- **1 天新项目风险:** VII-Cae 是新 GitHub 账号，项目可持续性未验证
- **Apple 设计语言的法律边界:** "Liquid Glass" 是 Apple 私有设计语言，开源实现是否触及 Apple 商标需要核验（README 中 hyalite 命名来自 hyalite opal，未直接使用 Apple Liquid Glass 商标——降低了风险）

## 与同类项目的关系
- **vs Apple Liquid Glass (visionOS / iOS):** Apple 私有设计语言（visionOS / iOS）；hyalite 是 Web 端开源实现
- **vs WebGL Liquid Glass 实现:** WebGL 自定义 shader（启动慢 / 兼容性差）；hyalite 是纯 CSS / SVG
- **vs backdrop-filter blur:** `backdrop-filter: blur(10px)` 是高斯模糊（涂抹）；hyalite 是 SDF 折射（弯曲）——模糊 vs 折射
- **vs M3 Expressive (Google):** Google Material 3 Expressive 是设计语言；hyalite 是 Web 实现——设计语言 vs Web 实现
- **vs CSS Houdini:** CSS Houdini 是浏览器 API（Paint API / Layout API）；hyalite 是 SVG filter 封装——浏览器 API vs 库

## 是否值得持续跟踪
**值得跟踪（Web Liquid Glass 开源实现头部样本）。** `hyalite` 代表了 Apple Liquid Glass 设计语言在 Web 端开源实现的方向，与 SDF + SVG displacement + 单文件零依赖 + 1 天 102⭐ 共同构成新方向。建议关注：(a) 浏览器兼容性的演化；(b) 真实折射 vs 模拟折射的精度差异；(c) Web 设计语言开源化生态；(d) 与 Apple 私有设计语言的法律边界。对 Web 设计师 / 前端开发者，hyalite 是 Liquid Glass 效果的零依赖开源方案。

## 后续观察点
- 浏览器兼容性的演化（Safari / Chrome / Firefox / 移动端）
- 真实折射 vs 模拟折射的精度差异
- 性能 benchmark（复杂场景渲染性能）
- Web 设计语言开源化生态的演进
- Apple 私有设计语言的法律边界演化
- 多语言 / 多框架集成（React / Vue / Svelte）

---
> 数据来源: GitHub API (2026-09-08) | Stars: 102 | Forks: 7 | License: 待核验 | 语言: JavaScript | 创建: 2026-09-07
