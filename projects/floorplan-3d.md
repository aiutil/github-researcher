---
title: "wy51ai/floorplan-3d"
slug: floorplan-3d
date_added: "2026-09-30"
last_seen_date: "2026-09-30"
category: "工具型"
emoji: "🏠"
stars: "457 stars"
stars_delta: "1 天 457⭐ (2026-09-29 → 2026-09-30)"
language: "HTML"
license: "待核验（README 未明示 license）"
score: 78
tags: ["floorplan-3d", "html", "javascript", "three-js", "3d", "2d-floorplan", "interior-design", "furniture", "rounded-box-geometry", "orbit-controls", "pointer-lock-controls", "room-environment", "css2d-renderer", "svg", "localstorage", "json-export", "no-build", "single-file", "i18n", "zh-en", "117-forks", "1-day"]
url: "https://github.com/wy51ai/floorplan-3d"
---

# wy51ai/floorplan-3d

## 一句话定位
纯前端 2D / 3D 户型装修设计工具——一个 index.html 无构建 + Three.js r160 + 60 余种家具 + 鸟瞰 / 漫游 + 中文 / English 界面 + localStorage 自动保存 + PNG / JSON 导出 + 自定义户型数据（ROOMS / WALLS / WINS / MATS / LIB）。

## 它解决的问题
户型装修设计工具赛道的痛点是 **「绝大多数工具都是 SaaS + 多端构建 + 不能离线 + 双语覆盖不足 + 不能自定义户型 + 不能 2D / 3D 实时同步 + 不能 localStorage 自动保存 + 不能 PNG / JSON 导出 + 不能一个 index.html 打开即用」**。floorplan-3d 用「一个 index.html 无构建 + 2D SVG 平面图 1:60 / 1:100 + mm 单位 + 60 余种家具（卧室 / 客厅 / 餐厨 / 卫浴 / 家电 / 书房休闲）+ 拖动旋转贴墙吸附 + 测量工具 + 拆改非承重墙 + 承重墙单独标示 + 图层开关 + 3D Three.js r160 + 鸟瞰 / 漫游 + 中英双语 + localStorage 自动保存 + PNG / JSON 导出 + 自定义户型数据」是「纯前端 + 单文件 + 零构建 + 2D / 3D + 双语 + localStorage + 自定义户型 + 严肃工程化」的具体路径。

## 为什么值得关注（2026-09-30）
- **Stars:** 457（截至 2026-09-30），1 天 457⭐，fork 117，fork/star 25.6%
- **Forks:** 117（典型高 fork 纯前端严肃工程化持续关注信号）
- **License:** 待核验（README 未明示 license）
- **语言:** HTML
- **活跃度:** created 2026-09-29，持续高活跃
- **规模:** 69 KB（极小项目——仅 README + 1 个 index.html）
- **Topics:** 0 个（README 未明示 topics 数组）

## 热度来源判断
floorplan-3d 的热度是 **「纯前端户型装修刚需 × 单文件零构建 × 2D / 3D 实时同步 × 双语 × 60 余种家具 × Three.js r160 × localStorage 自动保存 × 严肃工程化 × 自定义户型」** 的强劲组合。中文户型装修 / 室内设计 2026 年高热，但绝大多数是 SaaS + 不能离线 + 不能 2D / 3D 实时同步 + 不能自定义户型 + 不能单文件零构建——一个「单文件 + 零构建 + 2D / 3D 实时同步 + 双语 + 60 余种家具 + Three.js r160 + localStorage 自动保存 + 严肃工程化 + 自定义户型」的工具直击痛点。457 stars + 117 forks + fork/star 25.6% 反映社区高度参与——这正是「纯前端 + 单文件 + 严肃工程化」类项目的典型特征（用户 fork 部署 + 自定义户型 + 自定义家具库）。1 天 457⭐ 反映 GitHub Trending 纯前端单文件零构建严肃工程化持续关注信号。热度**真实且具纯前端严肃工程化潜力**——但需警惕：单文件零构建的「Three.js 性能 + 60 余种家具覆盖广度 + 鸟瞰/漫游体验 + 双语覆盖广度 + localStorage 稳定性 + PNG / JSON 兼容性 + 自定义户型数据可访问性 + Three.js 通过 jsDelivr CDN 加载（首次打开 3D 场景需要联网）+ license 未明示的商用边界」。

## 关键技术亮点
1. **一个 index.html 无构建：** 整个应用就是一个 `index.html`，无需构建，打开即用
2. **2D SVG 平面图 1:60 / 1:100 + mm 单位：** 2D 平面布置精确
3. **60 余种家具：** 卧室 / 客厅 / 餐厨 / 卫浴 / 家电 / 书房休闲——家具库覆盖广度
4. **拖动旋转贴墙吸附：** 拖动移动、旋转（Shift 自由角度）、调整尺寸，贴墙自动吸附
5. **测量工具：** 测量工具（靠近墙面自动吸附，Shift 锁定水平 / 垂直）
6. **拆改非承重墙 + 承重墙单独标示：** 拆改墙体支持
7. **图层开关：** 尺寸标注、房间名、家具、网格、承重墙——图层管理
8. **3D Three.js r160：** OrbitControls / PointerLockControls / RoundedBoxGeometry / RoomEnvironment / CSS2DRenderer
9. **鸟瞰 / 漫游模式：** 桌面端 WASD + 鼠标 + 触屏虚拟摇杆 + 点门开关
10. **精细家具模型：** 柜门分缝与拉手、软包床头、带环境反射的金属与陶瓷材质
11. **2D / 3D 实时同步：** 在 3D 中也能选中、拖动家具，与 2D 方案实时同步
12. **房间面积 + 套内使用面积 + 地面材料更换 + 5% 损耗估算造价：** 方案与统计
13. **撤销 / 重做 + localStorage 自动保存方案：** 严肃工程化
14. **中文 / English 界面切换：** 默认中文（顶栏右侧按钮，选择会记住）
15. **PNG 图片导出 + 方案 JSON 导入导出：** 数据可携带
16. **自定义户型数据：** ROOMS / WALLS / WINS / MATS / LIB / buildFurniture() 数据在 index.html
17. **快捷键：** T/V/M/X/R/Delete/Ctrl+D/Ctrl+Z/Esc 等

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 纯前端 2D / 3D 户型装修设计工具——单个 index.html（无构建）+ 浏览器原生 JS + SVG + Three.js r160（jsDelivr CDN） + localStorage | 仅基于 README 公开描述的 60 余种家具 + 鸟瞰 / 漫游 + 双语 + localStorage + PNG/JSON + 自定义户型；具体文件结构、buildFurniture() 函数实现、Three.js 模块加载策略未在档案中给出 |
| 主路径 | 自定义户型数据 (ROOMS/WALLS/WINS/MATS/LIB) → 2D SVG 平面布置 → 60 余种家具拖拽旋转贴墙吸附 → 测量工具 / 拆改墙体 / 图层开关 → 3D Three.js r160 渲染（鸟瞰 / 漫游 / 精细家具模型）→ 房间面积统计 + 地面材料更换 + 5% 损耗估算造价 → 撤销/重做 + localStorage 自动保存 → PNG 图片导出 + 方案 JSON 导入导出 | 主路径为 README 语义抽象；具体数据结构、贴墙吸附算法、漫游控制器未在档案中给出 |
| 关键权衡 | 单文件零构建 + 离线优先 + 双语 + localStorage + 自定义户型 + 严肃工程化 vs Three.js 通过 jsDelivr CDN 加载（首次联网）+ 60 余种家具覆盖广度 + 鸟瞰/漫游体验 + license 未明示商用边界 | 档案明示单文件零构建 + 双语 + localStorage vs jsDelivr CDN 联网依赖 + license 未明示 |
| 最小 PoC | `git clone <仓库地址>` + `python3 -m http.server 8000` + 浏览器打开 index.html（默认中文）+ 拖入 1 个家具到 2D + 切换到 3D 鸟瞰 + 漫游 WASD + 切换到 English + 保存方案（localStorage） + 导出 PNG | PoC 范围由 README 「快速开始」+ `python3 -m http.server` 推导；具体 jsDelivr CDN 首次联网、贴墙吸附精度、漫游控制器体验待核验 |
| 证据边界 | stars / forks / language / size / created_at 来自 GitHub API 公开元数据；架构细节 / 文件结构 / buildFurniture() 函数 / Three.js 模块加载策略 / license 均待核验 | GitHub API 元数据可信；架构细节未在 README 中给出 |

## 架构启发
floorplan-3d 的核心启发是 **「户型装修设计工具应该纯前端、单文件、零构建、2D / 3D 实时同步、双语、自定义户型，正如严肃工程化工具的标准」**。当前中文户型装修 / 室内设计工具多以 SaaS + 多端构建 + 不能离线 + 不能自定义户型为主——这违背严肃工程化用户利益——没人想要「SaaS + 不能离线 + 不能自定义户型」的户型装修设计工具。floorplan-3d 尝试做「户型装修设计工具的纯前端严肃工程化标准层」，类似 SingleFile 之于严肃工程化工具。更深层的启发是：**纯前端类项目的价值在于「单文件 + 零构建 + 离线优先 + 双语 + localStorage + 自定义户型 + 严肃工程化」而非 SaaS 体验**。457 stars + 117 forks 的结构，说明它已初步形成纯前端严肃工程化飞轮。能否持续，取决于「Three.js 性能 + 60 余种家具覆盖广度 + 鸟瞰/漫游体验 + 双语覆盖广度 + localStorage 稳定性 + PNG / JSON 兼容性 + 自定义户型数据可访问性 + Three.js 通过 jsDelivr CDN 加载的离线体验 + license 商用清晰」。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；"待核验"节点不应视为项目实现事实。

```mermaid
flowchart LR
  Data[自定义户型数据<br/>ROOMS WALLS WINS MATS LIB buildFurniture] --> Single[单 index.html]
  Single --> SVG2D[2D SVG 平面布置<br/>1:60 1:100 + mm]
  SVG2D --> Furniture[60 余种家具<br/>卧室 客厅 餐厨 卫浴 家电 书房休闲]
  Furniture --> DragRotate[拖动旋转贴墙吸附]
  DragRotate --> Measure[测量工具]
  Measure --> Wall[拆改非承重墙<br/>承重墙单独标示]
  Wall --> Layer[图层开关<br/>尺寸 房间名 家具 网格 承重墙]
  Layer --> Three3D[3D Three.js r160<br/>OrbitControls PointerLockControls RoundedBoxGeometry RoomEnvironment CSS2DRenderer]
  Three3D --> BirdView[鸟瞰 / 漫游<br/>WASD 鼠标 触屏虚拟摇杆]
  BirdView --> Detail[精细家具模型<br/>柜门分缝 软包床头 环境反射]
  Detail --> Sync[2D / 3D 实时同步]
  Sync --> Stats[房间面积 + 套内使用面积 + 地面材料 + 5% 损耗估算造价]
  Stats --> UndoRedo[撤销 / 重做 + localStorage 自动保存]
  UndoRedo --> I18N[中文 / English 界面切换]
  I18N --> Export[PNG 图片导出 + 方案 JSON 导入导出]
  CDN[Three.js jsDelivr CDN<br/>首次打开 3D 场景需要联网] -.联网加载.-> Three3D
```

## 定位判断
**工具型项目（纯前端 2D / 3D 户型装修设计工具）。** floorplan-3d 不仅是户型装修工具，更试图成为「纯前端 2D / 3D 户型装修设计工具的严肃工程化参考」——类似 SingleFile 之于严肃工程化工具。若成功，它会成为中文户型装修 / 室内设计严肃工程化用户的默认入口，具有严肃工程化级价值。457 stars + 117 forks + fork/star 25.6% 已显示纯前端严肃工程化飞轮雏形。但「工具化」取决于一个关键问题：Three.js 通过 jsDelivr CDN 加载（首次打开 3D 场景需要联网）——若纯前端严肃工程化用户希望完全离线，需用户自行验证。目前定位是「最有影响力的纯前端 2D / 3D 户型装修设计工具严肃工程化参考」，向严肃工程化级演进是合理路径。

## 风险 / 局限 / 泡沫点
- **Three.js jsDelivr CDN 联网依赖：** README 明示「Three.js 通过 jsDelivr CDN 加载，首次打开 3D 场景需要联网」——纯前端严肃工程化用户的「完全离线」体验受限
- **60 余种家具覆盖广度：** README 明示「卧室、客厅、餐厨、卫浴、家电、书房休闲」——覆盖广度需用户自行验证
- **自定义户型数据可访问性：** README 明示「户型数据写在 index.html 里：ROOMS、WALLS / WINS、MATS、LIB、buildFurniture()」——自定义户型门槛需用户自行验证
- **license 未明示：** README 未明示 license——商用边界需用户自行核验
- **topics 0 个（README 未明示 topics 数组）：** 描述密度低于 projects 标准
- **size 极小（69 KB）：** 单文件极小项目——扩展性需用户自行验证
- **个人项目属性：** wy51ai 个人维护——长期维护深度需核验

## 与同类项目的关系
- **vs 各 SaaS 户型装修设计工具：** SaaS + 不能离线 + 不能自定义户型；floorplan-3d 是纯前端 + 单文件 + 双语 + localStorage + 自定义户型
- **vs 各类 Three.js 户型装修 demo：** demo + 功能不全 + 不支持自定义户型；floorplan-3d 是完整工具 + 60 余种家具 + 自定义户型
- **vs 各室内设计 SaaS：** SaaS + 收费 + 不能 2D / 3D 实时同步；floorplan-3d 是纯前端 + 单文件 + 2D / 3D 实时同步 + localStorage
- **vs Planner 5D / RoomSketcher：** SaaS；floorplan-3d 是纯前端 + 离线优先 + 双语 + 自定义户型
- **vs 各类 Blender 插件：** Blender 依赖 + 学习曲线高；floorplan-3d 是浏览器打开即用 + 单文件 + 双语

## 是否值得持续跟踪
**值得跟踪（纯前端 2D / 3D 户型装修设计工具严肃工程化）。** floorplan-3d 代表了纯前端 2D / 3D 户型装修设计工具严肃工程化的诉求，无论其本身成败，这一方向是行业趋势。建议关注：Three.js 性能演进、60 余种家具覆盖广度、鸟瞰/漫游体验、双语覆盖广度、localStorage 稳定性、PNG / JSON 兼容性、自定义户型数据可访问性、Three.js jsDelivr CDN 离线体验、license 商用清晰。对中文户型装修 / 室内设计严肃工程化用户，这个工具是获取纯前端 + 单文件 + 零构建 + 2D / 3D 实时同步 + 双语 + localStorage + 自定义户型 + 严肃工程化的实用来源，值得直接采用。对纯前端严肃工程化观察者，它是「纯前端 + 单文件 + 零构建」赛道的头部样本。

## 后续观察点
- 是否演化为多户型装修设计工具（从单户型扩展为多户型模板）
- Three.js 通过 jsDelivr CDN 加载的离线演进（README 明示「首次打开 3D 场景需要联网」）
- 60 余种家具覆盖广度的扩展（README 明示「卧室、客厅、餐厨、卫浴、家电、书房休闲」）
- 鸟瞰/漫游体验的演进
- 双语覆盖广度的扩展（README 明示「中文 / English」）
- localStorage 稳定性的演进
- PNG / JSON 兼容性的演进
- 自定义户型数据可访问性的演进（README 明示「ROOMS、WALLS / WINS、MATS、LIB、buildFurniture()」）
- license 商用清晰的边界（README 未明示 license）
- topics 覆盖的清晰度（README 未明示 topics 数组）

---
> 数据来源: GitHub API (2026-09-30) | Stars: 457 | Forks: 117 | License: 待核验（README 未明示） | 语言: HTML | 创建: 2026-09-29 | 观察窗: 2026-09-29
