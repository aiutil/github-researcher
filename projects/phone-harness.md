---
title: "ShawnPana/phone-harness"
slug: phone-harness
date_added: "2026-08-10"
last_seen_date: "2026-08-12"
category: "观察型"
emoji: "📱"
stars: "1,488 stars"
stars_delta: "8/07创建→8/12观测 1,488⭐ / 129 fork / 7 subscribers，第五日 +206（+16.1%），fork 100→129，'phone-as-tool'赛道持续"
language: "Python"
license: "MIT"
score: 85
tags: ["phone-control", "iphone-mirroring", "vision-ocr", "agent-harness", "cgenevents", "skill", "hid", "macos"]
url: "https://github.com/ShawnPana/phone-harness"
---

# ShawnPana/phone-harness — agent 控制真实 iPhone 的薄 harness

## 一句话定位
一个用 Python 写的薄 harness，让 LLM/agent 通过 macOS 的 iPhone Mirroring 窗口直接控制真实 iPhone——`screencapture` + Apple Vision 框架 OCR 做"眼睛"，HID 级 CGEvents 做"手"，无需越狱、无需 Xcode、无需 WebDriverAgent。

## 它解决的问题
目标用户是想让 agent 自动化操作 iPhone 的开发者和高级用户。痛点：iOS 设备的自动化要么需要越狱（破坏保修/安全），要么需要 Xcode + WebDriverAgent（重、开发者门槛高），要么需要专用 MDM 方案（企业级、复杂）。phone-harness 利用 macOS Sequoia+ 原生的 iPhone Mirroring 功能——它把 iPhone 渲染为一个 Mac 窗口并转发鼠标/键盘输入为触摸——给 agent 提供了"看（截图+OCR）+ 操作（CGEvents 点击/输入）+ 验证（再截图）"的完整闭环，无需任何 iOS 侧的 agent/守护进程。

## 为什么值得关注（2026-08-10）

这代表了一个新概念赛道：**"phone-as-tool"——把物理 iPhone 当作 agent 的工具**。继 browser-harness（agent 控制浏览器）、computer-use（agent 控制桌面）之后，这是"agent 控制物理设备"赛道的延伸。789⭐ / 60 fork（fork/star=7.6%，正常）说明有开发者愿意尝试部署。关键差异化：(a) **零 iOS 侧依赖**——不需要越狱、不需要 Xcode、不需要 WDA、不需要在 iPhone 上装任何东西，只靠 macOS 的 iPhone Mirroring；(b) **OS 级 GUI 自动化**——用 `screencapture` + Vision OCR + CGEvents 这个最原始的"截图+OCR+点击"循环，而非专用移动端自动化框架；(c) **作为 Agent Skill 分发**——`phone-harness skill` 打印 skill body，可注册为 Claude Code/Codex 的 agent skill。

## 热度来源判断
- **真实需求信号**：60 fork（fork/star=7.6%，正常范围）说明有开发者愿意部署。README 是认真的工程文档（含架构图、踩坑经验、权限引导），非营销页面。
- **概念新颖性**：用 iPhone Mirroring 做 agent 控制通道是新角度——iPhone Mirroring 是 macOS Sequoia+ 的新功能，把"手机自动化"从"需要 iOS 侧工具"变成"只需要 macOS"。
- **话题性成分**：subscribers 仅 1（极低），说明目前是"收藏/好奇"为主，深度使用尚少。789⭐ 在 3 天内积累，可能含"agent 控制手机"的话题性成分。
- **作者**：ShawnPana（需观察持续投入）。

## 关键技术亮点亮点

1. **iPhone Mirroring 作为传输层（README 可核验）：** macOS Sequoia+ 的 iPhone Mirroring 把 iPhone 渲染为 Mac 窗口，转发真实鼠标/键盘输入为触摸。phone-harness 把这个窗口作为唯一传输通道——不需要在 iPhone 上装任何东西。
2. **眼睛：`screencapture` + Vision 框架 OCR：** 只截取 Mirroring 窗口，用 Apple Vision 框架 OCR 识别所有可见文本及其 tap-ready 坐标。README 称之为"the poor man's DOM"——因为 iOS 窗口是视频流，没有 accessibility tree，OCR 文本坐标是唯一的"可点击目标"来源。
3. **手：HID 级 CGEvents：** 在 HID tap 层投递事件，覆盖 tap、长按、拖拽/滑动（flick）、滚动手势（wheel scroll）、unicode 输入、app 快捷键（Cmd+1 Home、Cmd+2 App Switcher、Cmd+3 Spotlight）。
4. **验证：再截图（capture is ground truth）：** "No DOM means the capture is the ground truth"——因为没有 DOM/accessibility tree，每次操作后再截图是唯一验证方式。
5. **真实踩坑经验（README 明确列出）：** AppleScript `click at` 被静默忽略（窗口是视频流，无 accessibility tree）、unicode key payload 无效（Mirroring 转发 raw HID keycodes，必须用 keycodes）、慢速 touch-drag 几乎不动 iOS 列表（要用 wheel scroll for lists, fast flick for pages）、输入时窗口必须 frontmost（否则被吞）。这些是真实的工程经验，非理论。
6. **作为 Agent Skill 分发：** `phone-harness skill` 打印 skill body，可注册为 Claude Code/Codex 的 agent skill，让 agent 自动 reach for it。
7. **架构分层（README 可核验）：** `SKILL.md`（agent 面向的产品面）+ `install.md`（权限引导）+ `src/phone_harness/`（约 500 行保护核心：mirror.py 窗口发现/聚焦/截图/CGEvent 输入、ocr.py Vision 文本识别、helpers.py 预导入原语、admin.py `--doctor`、run.py CLI）+ `agent-workspace/agent_helpers.py`（agent 编辑的 helper，自动加载到每个脚本 namespace）。传输无状态（无 daemon），每次调用自包含。

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 编排与运行时仅在 macOS 侧，iPhone 侧零 agent；传输通道完全依赖 macOS Sequoia+ 的 iPhone Mirroring 窗口 | 档案明确 macOS 绑定，iPhone 侧不安装任何组件；其他 OS 支持待核验 |
| 主路径 | agent/CLI → mirror.py（窗口发现/聚焦/截图/CGEvent）↔ iPhone Mirroring 窗口；ocr.py Vision OCR 出 tap-ready 坐标 → 再截图校验 | 来自档案对 src/phone_harness/（mirror.py、ocr.py、run.py、admin.py）的描述，具体协议与接口以源码为准 |
| 关键权衡 | 零 iOS 依赖 vs 无 accessibility tree/DOM：观察通道只能靠 screencapture+OCR，DRM 黑屏、纯图标按钮、多点触控均受限；单机会话不可并发 | 档案自述局限：OCR 看文本不看语义、无多点触控/相机/Face ID、解锁即暂停、单设备单会话 |
| 最小 PoC | 在 macOS Sequoia+ 上 `phone-harness --doctor` 校验权限，通过 `phone-harness skill` 注册为 Claude Code/Codex skill，跑通“截图→OCR→tap→再截图”单一闭环 | 命令与 skill 注册名来自档案描述；权限清单、稳定性、退出路径须实机验证 |

## 架构启发
phone-harness 的核心启发是 **"用 OS 级的镜像/无障碍能力替代专用自动化框架"**。传统移动端自动化（Appium、WebDriverAgent、XCUITest）都需要在 iOS 侧安装 agent 或用 Xcode 签名，门槛高且易被系统更新破坏。phone-harness 完全绕过 iOS 侧——只靠 macOS 的 iPhone Mirroring（官方功能）+ macOS 的截图/Vision/CGEvent API，实现了对 iPhone 的 GUI 自动化。这与 browser-harness（用浏览器 DevTools/CDP）是不同层次的思路：browser-harness 用浏览器原生协议，phone-harness 用 OS 级 GUI 原语。更深层的启发：**当 OS 提供"镜像/无障碍"能力时，专用自动化框架的壁垒会被降低**——agent 不需要"懂 iOS"，只需要"看屏幕+点坐标"。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；“待核验”节点不应视为项目实现事实。

```mermaid
flowchart LR
    A[Agent 或 CLI 调用 run.py] --> B[mirror.py 窗口发现 聚焦 截图]
    B <--> M[iPhone Mirroring 窗口 macOS Sequoia+]
    M -- 视频流 --> B
    M -- HID 触摸 反馈 --> B
    B --> C[ocr.py Apple Vision OCR tap-ready 坐标]
    C --> D[CGEvent tap drag flick wheel scroll unicode]
    D --> M
    B --> E[再截图 校验 ground truth]
    E --> A
    A --> S[agent_helpers.py 自动加载 namespace 待核验]
    A --> K[phone-harness skill 注册 Claude Code Codex 待核验]
    M -. 受限 .-> R[DRM 黑屏 无多点触控 解锁暂停 多点触控不可用 待核验]
</mermaid>
```

## 定位判断
属于 **agent 终端/harness 层**，是"agent 控制物理设备"赛道在 iOS 的代表。与 browser-harness（浏览器）、computer-use（桌面）、qm（协作 harness）不在同一层——它是"如何让 agent 操作手机"的范式参考。定位是概念验证型项目：验证了"用 iPhone Mirroring 做 agent 控制通道"的可行性。

## 风险 / 局限 / 泡沫点

1. **强绑定 macOS（iPhone Mirroring 是 macOS Sequoia+ 功能）：** 无法在 Windows/Linux 上使用，限制了可及性。iPhone Mirroring 本身是较新的 macOS 功能，用户基数有限。
2. **无多点触控、无相机/Face ID、DRM 视频黑屏（README 自述）：** 无法处理需要生物识别的流程，DRM 内容（如 Netflix）渲染为黑色导致 OCR 失败。
3. **OCR 看文本不看语义（README 自述）：** 无标签的纯图标按钮需要截图 + vision-capable 模型才能识别，增加了延迟和成本。
4. **单机单会话：** 一个手机一个会话，解锁物理手机会暂停 Mirroring。不适合大规模并发。
5. **subscribers 仅 1：** 极早期，深度跟踪意愿低。789⭐ 可能含话题性成分。
6. **iPhone Mirroring 依赖：** 若 Apple 调整 iPhone Mirroring 的行为（如增加反自动化），整个方案可能失效。

## 与同类项目的关系
- **vs browser-harness / computer-use（Anthropic）：** browser-harness 控制浏览器，computer-use 控制桌面，phone-harness 控制物理 iPhone。三者是"agent 控制不同界面"的赛道延伸。
- **vs Appium / WebDriverAgent / XCUITest：** 传统移动自动化需要在 iOS 侧安装 agent 或 Xcode 签名；phone-harness 完全在 macOS 侧，零 iOS 依赖。但传统方案有 accessibility tree（精确），phone-harness 只有 OCR（近似）。
- **vs qm（yc-software，12,757⭐）：** qm 是多人协作 agent harness（Slack 集成、sandbox），phone-harness 是单设备控制 harness。不同层。
- **vs MCP 设备控制类工具：** MCP 是工具协议（结构化调用），phone-harness 是 GUI 自动化（截图+点击）。不同抽象层。

## 是否值得持续跟踪
**是，作为"agent 控制物理设备"赛道在 iOS 的代表跟踪。** phone-harness 验证了"用 OS 镜像能力替代专用自动化框架"的可行性，无论其本身成败，这一方向值得关注。重点验证：(a) 是否被实际用于真实自动化场景（不只是 demo）；(b) iPhone Mirroring 的稳定性是否会随 macOS 更新变化；(c) 是否出现同类项目（如 Android 版、用 scrcpy 的方案）。

## 后续观察点
1. **真实采用案例：** 是否有开发者公开用 phone-harness 完成真实自动化任务（而非 demo），以及稳定性反馈。
2. **iPhone Mirroring 稳定性：** macOS 更新是否会破坏方案（Apple 是否会限制自动化）。
3. **同类项目出现：** 是否出现 Android 版（用 scrcpy + ADB）、或其他 iOS 方案，形成"phone-as-tool"赛道。
4. **subscribers 增长：** 从 1 增长说明深度使用意愿上升。
5. **作者持续投入：** ShawnPana 是否持续维护。

---
*首次记录：2026-08-10* · *数据来源: GitHub API (2026-08-10) + 仓库 README | Stars: 789 | Forks: 60 | License: MIT | 语言: Python | 创建: 2026-08-07*
