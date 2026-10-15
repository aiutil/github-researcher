---
title: "devswha/herdr-web-ui"
slug: herdr-web-ui
date_added: "2026-10-16"
last_seen_date: "2026-10-16"
category: "工具型"
emoji: "📱"
stars: "1022 stars"
stars_delta: "29 天 1022⭐ ⑂138 fork/star 13.5%（持续高增长，跨设备协同需求强）"
language: "TypeScript"
score: 89
tags: ["herdr-web-ui","devswha","herdr","claude-code","codex","omp","omo","gjc","pi","hermes","opencode","devin-cli","coding-agents","browser-client","phone-client","pwa","tailscale","qr-code","xterm","bun","vite","react","voice-dictation","screen-mirror","worktree","mit","coding-agent-remote"]
url: "https://github.com/devswha/herdr-web-ui"
---

# devswha/herdr-web-ui

## 一句话定位
herdr-web-ui 是一个 Browser and phone client for herdr——Claude Code and Codex, from your phone，把同一 herdr pane 在 desktop browser / phone（PWA） / 远程 PC over SSH 上以 Chat（agent 自己的 native transcript：Claude Code / Codex / omp / omo / gjc / pi / Hermes / OpenCode 2 / Devin CLI） 与 Live Terminal 一键切换的形式呈现，附 push alerts when an agent needs input or finishes、Tailscale serve + QR code 给 phone、voice dictation (Korean + English mixed)、Windows screen mirror、⋯ New worktree 从 phone branch off 第二个 agent。

## 它解决的问题
2026 年 coding agent（Claude Code / Codex / Hermes / OpenCode 2 / Devin CLI 等）日常长跑 → 开发者离开桌面时如何继续推进？现有方案要么是 tmux/zellij + SSH + 手动端口转发 + Tailscale（仅桌面 / 不读 native transcript），要么是 collie / roamgate / herdr-remote（不发 tunnel，要 tmux/zellij/diffs/Telegram），要么是 Happy / Paseo / CloudCLI UI（自启/管 session，不读 agent 自己的 transcript）。herdr-web-ui 直击痛点：（1）**native transcript reader**——读 agent 自己的 session store，把 Claude Code / Codex / omp / omo / gjc / pi / Hermes / Devin CLI 的 transcript 折成 chat（per turn 而不是 terminal output）；（2）**Browser and phone client**——同一 pane 在 desktop browser / phone（PWA，installable，key bar above the keyboard: Esc / Tab / Ctrl / Alt / Shift / Enter / arrows）+ 远程 PC over SSH from the sidebar；（3）**Chat ↔ Terminal 一键切换**——native transcript 时是 chat，要 terminal 一键转；（4）**Approve with a tap**——approvals / questions / plan menus become cards, checked to be current before send；（5）**Push alerts**——live status for every pane + an alert that drops in while the app is open + push alerts when an agent needs input or finishes, even with the app closed；（6）**Voice dictation**——speak instead of typing, Korean and English mixed, browser's speech recognition 或 own OpenAI key；（7）**Worktree branch from phone**——⋯ New worktree on phone: branch filled in, pick an agent, it starts beside the first；（8）**Screen mirror (Windows)**——herdr 不支持 terminal attach there 时，screen mirror with typing and fixed grid。解决的是 **「coding agent 远程控制 + 跨设备协同 + 不读 native transcript + 仅桌面 + 镜像端无 push alert」** 的工程化问题。

## 为什么值得关注（2026-10-16）
- **Stars:** 1022（截至 2026-10-16），29 天 1022⭐ ⑂138 fork/star 13.5%，**增长率** 13.5%（fork/star 反映社区参与度，跨设备协同类项目 fork 多因二次开发成本低）
- **Forks:** 138，社区贡献活跃
- **Size:** 73130 KB（Bun + Vite + React + xterm.js + Lucide 全栈 + 7 语言 docs）
- **License:** MIT
- **语言:** TypeScript + Bun 1.4+ + Node 18+ (Linux/macOS) + Git for Windows (Windows) + xterm.js + React + Lucide + Vite
- **活跃度:** created 2026-09-17，pushed_at 2026-10-15，持续高活跃
- **平台:** Linux (x64 + arm64) + macOS + Windows (x64)

## 热度来源判断
herdr-web-ui 的热度是 **「coding agent 真实生活场景刚需 × 严肃工程化 native transcript reader × Chat↔Terminal 一键切换 × PWA + key bar + Tailscale serve + QR × push alerts + voice dictation × Windows screen mirror × worktree branch from phone × herdr plugin 模式 × MIT** 的组合。`fork/star 13.5%` 极高说明大量用户在 fork 用于二次开发——herdr plugin 模式让 fork = 自托管定制 = 跨设备协同定制都可行。这与昨日 trending `outcrawlai/scout` + 今日 trending `lexmount/moli` + 之前 `eliasstravik/herdr-projects` + `HelixDB/helix-foundry` + `Gentleman-Programming/gentle-dot` 等一同指向「coding agent 真实生活场景严肃工程化栈」的成型。

## 关键技术亮点
1. **native transcripts：** Claude Code / Codex / omp / omo / gjc / pi / Hermes and explicitly identified Devin CLI transcripts, plus OpenCode 2 sessions herdr identifies；OpenCode 1.x 走 live terminal；plain `devin` 走 live terminal；其他走 live terminal + status
2. **Chat ↔ Terminal 一键切换：** 同一 pane 可在 native transcript (chat) 与 live terminal 之间切换；next message 走 next turn，Send now 立即发
3. **Approve with a tap：** approvals / questions / plan menus become cards, checked to be current before send
4. **Push alerts：** live status for every pane + an alert that drops in while the app is open + push alerts when an agent needs input or finishes, even with the app closed
5. **PWA + key bar：** installable PWA with a key bar above the keyboard (Esc / Tab / Ctrl / Alt / Shift / Enter / arrows), rearrange and extend with your own combinations in Settings
6. **Tailscale serve + QR code：** `tailscale serve` 自动发 HTTPS，给 tailnet address + QR code → phone scan QR + add to home screen；`HERDR_WEB_TAILSCALE_SERVE_ONLY=1` 仅 tailnet 访问
7. **Voice dictation (Korean + English mixed)：** dictate into chat or terminal line, browser's speech recognition 或 own OpenAI key；review words before send
8. **Windows screen mirror：** herdr 不支持 terminal attach there 时，screen mirror with typing and fixed grid（`docs/remote-pcs.md#windows-pcs`）
9. **Worktree branch from phone：** ⋯ New worktree：branch filled in, pick an agent, and it starts beside the first
10. **Open what the agent made：** click a path in terminal → file viewer；tap in chat → full screen
11. **Send a screenshot from your phone：** the + button uploads it into the pane's folder and adds its path；agent reads the image
12. **Remote PCs over SSH from the sidebar：** 其他 PC 通过 SSH 加入
13. **Keep your workflow：** herdr owns the agents; this app connects to them; update from Settings without stopping them, with patch notes for what each update brings
14. **Multi-platform install：** Linux x64/arm64 + macOS：`curl -fsSL https://herdrweb.dev/install.sh | sh`；Windows x64 PowerShell：`irm https://herdrweb.dev/install.ps1 | iex`；已有 prerequisites 装 plugin：`herdr plugin install devswha/herdr-web-ui`
15. **Anonymous usage counts：** version + OS + install method + random ID；no IP；可关（Settings → About → Anonymous usage counts）
16. **7 语言 README：** English / 简体中文 / 日本語 / 한국어 + 5 种欧洲语言 docs
17. **与同类比较（README 明示）：** vs collie / roamgate / herdr-remote（其他 herdr 手机/浏览器客户端，但那些不发 tunnel，要 tmux/zellij/diffs/Telegram）；vs Happy / Paseo / CloudCLI UI（那些自启/管 session，不读 agent 自己的 transcript）
18. **Built on：** herdr + chatmux + xterm.js + React + Bun + Lucide

## 架构师速览

（详见各趋势的架构师速览表 + Mermaid 架构图。系统边界、主路径、关键权衡、最小 PoC、证据边界、待核验均见下表与图。）

## 架构启发
herdr-web-ui 的核心启发是 **「coding agent 的远程控制应该是『读 agent 自己的 transcript』而不是『镜像 terminal 输出』」**。当前所有主流 coding agent 远程控制工具（tmux/zellij + Tailscale + 桌面 only）都把「远程控制 = 镜像 terminal output」，这导致：对话要自己看输出、看 prompt、看 diff 才理解 agent 在干啥。herdr-web-ui 走另一条路：读 agent 自己的 session store，把 transcript 折成 chat，next message 走 next turn，approvals/plan menus 变 cards，all in 上 desktop browser / phone（PWA）/ remote PC over SSH。这与 `outcrawlai/scout`（昨日 trending 636⭐，LLM-driven browser agent on Outcrawl cloud）形成完美互补——scout 偏「agent 调度 / 模型分工」，herdr-web-ui 偏「agent 远程控制 / native transcript reader」。更深层的启发是：**herdr plugin 模式让 fork = 自托管定制 = 跨设备协同定制**——`fork/star 13.5%` 极高说明这是社区强需求的 stand。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  User[Developer<br/>desktop browser / phone PWA / remote PC over SSH] --> Tailscale[Tailscale serve<br/>HTTPS + tailnet]
  Tailscale --> Server[Bun server :7317<br/>API + WebSocket<br/>Vite :5173 dev]
  HerdrPane[herdr pane<br/>on user PC] --> Server
  Server --> Read[Native transcript reader<br/>Claude Code / Codex / omp / omo<br/>gjc / pi / Hermes / Devin CLI<br/>+ OpenCode 2 (via herdr)]
  Server --> Term[Live terminal bridge<br/>xterm.js<br/>其他 programs / OpenCode 1.x<br/>plain devin]
  Read --> Chat[Chat view<br/>next message → next turn<br/>Send now immediate]
  Term --> TermView[Terminal view<br/>click path → file viewer]
  Chat <-->|一键切换| TermView
  Chat --> Approve[Approve with a tap<br/>cards: approvals / questions<br/>plan menus<br/>checked to be current]
  HerdrPane -.live status.-> Server
  Server -.push alerts.-> User
  User -.voice dictation.-> Voice[Voice input<br/>browser's speech recognition<br/>OR own OpenAI key<br/>Korean + English mixed]
  Voice --> Chat
  Voice --> TermView
  User -.⋯ New worktree.-> WT[Branch off second agent<br/>phone ↔ desktop]
  Win[Windows x64<br/>Git for Windows] -.不支持 terminal attach.-> Mirror[Screen mirror<br/>typing + fixed grid]
  Server -.herdr plugin.-> Plugin[herdr plugin install devswha/herdr-web-ui]
  Server -.update.-> Update[Update from Settings<br/>without stopping agents<br/>patch notes]
```

## 定位判断
**工具型（coding agent 远程控制 + 跨设备协同 native transcript reader）。** herdr-web-ui 不只是 web UI，更是 coding agent 「人在外面也能继续推进」的 **「native transcript 路径」**——在 tmux/zellij + Tailscale + 仅桌面 + 镜像端不读 native transcript 的常态，提供「native transcripts + Chat↔Terminal + PWA + key bar + Tailscale serve + QR + voice dictation + screen mirror + worktree branch from phone + herdr plugin + MIT」的严肃工程化路径。1022⭐ ⑂138 + 11 topics（bun / claude-code / codex / coding-agents / herdr / herdr-plugin / mobile / pwa / react / terminal / xterm）+ MIT + 7 语言 README 已显示这是 coding agent 跨设备协同的关键 stand。能否成为「coding agent 远程控制默认 client」取决于：push alerts provider + voice dictation OpenAI key 模型 + Bun server 并发模型 + port 7317 安全边界 + anonymous usage counts 隐私细节 + herdr-projects 多 agent 协同在该 web-ui 上的可观察性。

## 风险 / 局限 / 泡沫点
- **push alerts provider + Web Push vs native push 差异：** push alerts 用何种 provider、Web Push 与 native push 的差异、跨 OS 的兼容性
- **voice dictation OpenAI key 模型：** voice input 的 OpenAI key 模型、enabled usage meters contact provider APIs、计费公式
- **Bun server 并发模型 + port 7317 安全边界：** Bun server 的并发模型、port 7317 在 Tailscale + LAN 上的安全边界、与 HTTPS / SSH / VPN 的对比
- **herdr-projects 多 agent 协同：** herdr-projects 多 agent 协同在该 web-ui 上的可观察性、approve/answer 状态在断网时的回放、worktree branch 时的冲突解决
- **与其他同类项目比较：** vs collie / roamgate / herdr-remote（不发 tunnel，要 tmux/zellij/diffs/Telegram）；vs Happy / Paseo / CloudCLI UI（自启/管 session，不读 agent 自己的 transcript）——README 明示但不构成竞争壁垒
- **Windows screen mirror 局限：** herdr 不支持 terminal attach there 时用 screen mirror，但 typing + fixed grid 不是真 terminal，体验不及 macOS/Linux
- **数据治理：** Session files stay on the PC running each agent；optional voice input sends audio to configured provider；anonymous usage counts 可关——但 push alerts / remote-PC setup / app updates 仍可用 external services

## 与同类项目的关系
- **vs tmux/zellij + SSH + Tailscale（传统远程控制）：** 传统方案仅桌面 + 镜像端不读 native transcript；herdr-web-ui 是 Browser and phone client + native transcripts + Chat↔Terminal + PWA + Tailscale serve + QR + push alerts + voice dictation + screen mirror + worktree branch from phone + MIT
- **vs collie / roamgate / herdr-remote：** 那些是其他 herdr 手机/浏览器客户端，但不发 tunnel，要 tmux/zellij/diffs/Telegram；herdr-web-ui 读 agent 自己的 transcript，把 work 折成 chat，other PCs join over SSH from the sidebar
- **vs Happy / Paseo / CloudCLI UI：** 那些自启/管 session，不读 agent 自己的 transcript；herdr-web-ui 用 herdr panes already run，keeps the same terminals available in the TUI and browser
- **vs anthropics/skills：** Anthropic 官方 Skills 仓库仅服务 Claude；herdr-web-ui 跨 Claude Code / Codex / omp / omo / gjc / pi / Hermes / OpenCode 2 / Devin CLI，更通用
- **vs outcrawlai/scout（昨日 trending）：** scout 偏 LLM-driven browser agent；herdr-web-ui 偏 coding agent 远程控制 client——两者在「agent 调度 / 模型分工」与「agent 远程控制 / native transcript reader」分工不同但互补

## 是否值得持续跟踪
**值得跟踪（coding agent 远程控制 + 跨设备协同 native transcript reader）。** herdr-web-ui 代表了 coding agent 时代的「native transcript + 跨设备协同」严肃工程化路径——在 tmux/zellij + Tailscale + 仅桌面的常态，提供「native transcripts + Chat↔Terminal + PWA + Tailscale serve + QR + push alerts + voice dictation + screen mirror + worktree branch from phone + MIT」的严肃工程化方案。建议关注：push alerts provider + voice dictation OpenAI key 模型 + Bun server 并发模型 + port 7317 安全边界 + anonymous usage counts 隐私细节 + herdr-projects 多 agent 协同在该 web-ui 上的可观察性。对 Claude Code / Codex / Hermes / OpenCode 2 / Devin CLI 用户，这是「人在外面也能继续推进」的实用方案，值得直接采用。

## 后续观察点
- push alerts 用何种 provider（Web Push / FCM / APNs / 自建）与跨 OS 兼容性
- voice dictation OpenAI key 模型 + 计费公式 + 准确率（Korean + English mixed）
- Bun server 并发模型 + port 7317 安全边界 + Tailscale serve 与自建 HTTPS 代理的对比
- herdr-projects 多 agent 协同在该 web-ui 上的可观察性
- Windows screen mirror 体验进展（herdr 是否会支持 terminal attach on Windows）
- 与 collie / roamgate / herdr-remote / Happy / Paseo / CloudCLI UI 的实测差异

---
*首次记录：2026-10-16*