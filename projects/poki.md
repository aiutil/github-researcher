---
title: "JosssphZhou/poki"
slug: poki
date_added: "2026-11-07"
last_seen_date: "2026-11-07"
category: "生产可用"
emoji: "📱"
stars: "406 stars"
stars_delta: "1.3 天 406⭐ ⑂83（fork/star 20.4%）· subs 1 · oi 10 · 快照 2026-11-06T22:00Z 区间；星数为两次快照之间的总量差，非当日新增"
language: "JavaScript"
score: 90
tags: ["poki", "ios-device-automation", "mcp-server", "no-jailbreak", "rust-native-bridge", "nodejs-stdio-mcp", "agent-with-memory", "verification-document", "sent-true-not-acknowledged", "screen-changed-signal", "touch-drop-measurements", "single-device-log-not-guarantee", "simulator-vs-physical-separated", "protocol-suite-excludes-device", "live-fixture-scripts-excluded-from-npm-test", "chinese-interface-only-verified", "portrait-only", "agpl-3-0-only", "prebuilt-macos-arm64-tarball", "third-party-dependency-manifest", "send-messages-or-payments-warning", "gpt-6-1-terra-default", "23-commits", "2-contributors", "2-releases"]
url: "https://github.com/JosssphZhou/poki"
---

# JosssphZhou/poki

## 一句话定位

让 AI agent 操作真实 iPhone 的本地 MCP server + 独立 agent（免越狱、免额外硬件），**而它本日最硬的一份资产不是能力而是 `docs/verification.md` —— 那份文件把「我测过了」拆成「在什么设备上、什么姿态、哪些结论不能外推」，并逐条记录没赢的地方**。

## 它解决的问题

让 agent 操作手机（发消息、查资料、填表）需要一条从「模型」到「设备」的链路。常见方案有三条，各有代价：

1. **越狱 + 私有 API** —— 能力最强，但要越狱、要重建签名、系统升级即失效；
2. **Apple 官方 Shortcuts / XCUITest** —— 安全但在后台执行，交互能力受限，且难以做「读屏 → 判断 → 操作」的闭环；
3. **WebDriverAgent / 第三方桥接** —— 需要额外硬件或复杂环境。

poki 走的是第三条里最省事的一支：**用 `pymobiledevice3` 风格的 USB 配对 + 一个自研 native bridge，把触摸、滑动、截图、OCR、粘贴板做成本地服务**，然后用 MCP 暴露给 agent。**免越狱、免额外硬件**。

## 为什么值得关注（2026-11-07）

**⭐⭐⭐⭐⭐ 本日最值得抄的一段（`docs/verification.md` 原文）**：

> **`sent: true` only means the touch was written to the connection. The device does not acknowledge it, so check `screen_changed` and the returned screen.**

**⭐⭐⭐⭐⭐⭐ 这句话把一个被普遍混淆的事实拆开了**：「触摸指令写进去了」和「设备执行了这次触摸」是两件事。前者可以由写入端确认，后者只能由屏幕变化推断。**⭐⭐⭐⭐⭐ 把前者单独取名 `sent`、把后者单独取名 `screen_changed`，并要求调用方同时检查，是本日报见过最干净的一次「接口语义设计」** —— 它不靠文档提醒，靠返回值结构强制调用方注意。

**⭐⭐⭐⭐⭐⭐⭐ 配套的实测数字全部带适用边界（原文逐条）**：

| 场景 | 结果 | 原文边界 |
|---|---|---|
| 旧连接处理，点聊天应用搜索框 | **丢 2 / 70** 次触摸 | 「**Every dropped touch still returned `sent: true`.**」 |
| 保持连接直到 post-touch wait 结束 | **丢 0 / 70** | 「These numbers only apply to **that single search field**.」 |
| 最终构建 | **丢 0 / 24** | 同上 |
| 启动后 1.5 秒点击 | **0 / 3 生效** | 「Touches sent too soon after app launch may have no effect.」 |
| 启动后 ≥ 2.8 秒点击 | **12 / 12 生效** | 同上 |
| 点底部浮动栏旁的控件（Settings） | **4 / 4 无效** | 「**This is not fixed.** Those taps now return `screen_changed: false`.」 |
| 横屏游戏点按钮坐标 | 无效（同一 session 竖屏有效） | 「**The cause is unknown.**」 |

**⭐⭐⭐⭐⭐⭐⭐⭐⭐ 它连「没测的部分」都点名**：

> We only measured taps. `drag` and `pinch` use the same connection path and **were not measured.** The latest update to how `screen_changed` compares screens **has not been tested with touches on a physical phone.**

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 它把「模拟器数据」与「真机数据」在文件结构上就分开了**（「Measured on simulators only」独立成节），并写明：

> These numbers were measured **before** the later physical-tap changes. **They have not been re-run.** To run the measurement yourself, see `bin/eval-first-call.mjs`.

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 全文件的定调句极为克制**：

> The earlier measurements below come from a **single iPhone running iOS 27.3 over Wi-Fi. Treat them as a test log from that setup, not a guarantee for other apps or devices.**

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 「测过什么」与「没测什么」的边界写在测试脚本的分类里**：

| 套件 | 内容 | 是否接触真机 |
|---|---|---|
| `npm test`（协议套件） | stdio↔HTTP 桥、鉴权、工具发现、无设备错误处理、wait-only 批处理 | **否** —— 「without injecting input into a phone or simulator」 |
| `bin/verify-fixture.mjs` | 真实 UI 与应用变更 | 是 —— 需专用一次性模拟器 `Poki MCP QA` + `PokiMCPFixture` app |
| `bin/verify-platform.mjs` | 同上（含 pasteboard 限制探测） | 是 —— 「**intentionally excluded from `npm test`**」 |

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 它的边界声明把「外部进程 fixture 能证明什么」也划清了**：

> These coordination checks use external-process fixtures. **They do not establish real-device cancellation, gesture effects, first-time system permissions, or an independent new-user installation.** Those checks still require separately authorized device acceptance.

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 风险披露写在 README 最显眼处**：

> Poki controls your real iPhone. **If you ask it to send messages or make payments, it will.** Screen contents are sent to your configured model service.

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 它的许可选择与分发方式匹配**：AGPL-3.0-only，**并且提供预编译包**（`poki-v0.1.1-macos-arm64.tar.gz`）+ **每日匿名 GitHub release 检查**（可用 `POKI_NO_UPDATE_CHECK=1` 关闭）。**⭐⭐⭐ AGPL + 预编译分发 + 自动更新这三者的组合，说明作者清楚「网络服务场景的许可义务」并做了工程应对。**

**⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 依赖也做成了可审阅清单**：`docs/third-party-dependencies.md`、`docs/licenses/BlueBubbles-LICENSE`、`native/LICENSE.idb`、`native/LICENSE.idevice`、`native/LICENSE.idevice`、`THIRD_PARTY_NOTICES.md`。

## 热度来源判断

**⭐⭐⭐⭐ 真实需求，且热度结构本身是可信的。**

支持「真实」的证据：

- **⭐⭐⭐⭐⭐ fork 间隔分布是真人形态**：`forks` 全量 83 个，跨 `2026-11-05T15:41:43Z .. 2026-11-06T18:34:17Z`（约 27 小时），按小时分桶为 `15:41`×7、`16:01`×15、`17:02`×7、`18:25`×2、`19:15`×2、`21:37`×1 —— **⭐⭐⭐⭐⭐ 这是本日第二批农场（5–6 秒中位数、96.9% 的间隔 ≤10 秒）截然不同的形态**。
- **⭐⭐⭐⭐ 六个语言的 README**（`README.md` / `README.zh-CN.md` / `README.zh-TW.md` / `README.ja.md` / `README.ko.md` / `README.es.md`）+ 独立的 `docs/` 文档站（`install.md` / `tools.md` / `configuration.md` / `physical-iphone.md` / `verification.md` / `imessage-gateway.md` / `third-party-dependencies.md` / `verification/cellular-test-plan.md` / `verification/tailscale-pr-validation.md`）。
- **⭐⭐⭐⭐ 2 个 release、23 个 commit、2 个 contributor**；有 `AGENTS.md` / `CODE_OF_CONDUCT.md` / `CONTRIBUTING.md` / `SECURITY.md`。
- **⭐⭐⭐⭐⭐ `docs/verification.md` 里那 5 条「没修好」的记录**（bottom bar 点击 4/4 无效、两次未复现的 touch 丢失、horizon 未知原因）—— **⭐⭐⭐⭐⭐ 真实的项目不会把这些写进 README**，因为这会显得产品不好用。

**⭐⭐⚠️ 但必须点名一个反向信号**：**`subscribers_count` = 1，而 forks = 83**。**⭐⭐ 这个「大量 fork + 极少深度订阅」的组合，本日在农场簇里也出现过**（`roblox-studio-mcp` 是 subs 8 / forks 260）。**⭐⭐⭐⭐ 因此本日再次确认：单看 fork 数会误判，必须看 fork 的时间分布。**

## 关键技术亮点

1. **⭐⭐⭐⭐⭐ 双层架构：设备执行与 agent 决策分离**。`native/bridge/`（Rust + Cargo，`apps.rs` / `gesture.rs` / `installation.rs` / `stream.rs` / `pasteboard.rs` / `remote.rs` / `ax.rs`）负责设备侧；`src/*.mjs`（Node）负责 MCP 协议与批处理。
2. **⭐⭐⭐⭐⭐ 双信号返回**：`sent`（写入了）与 `screen_changed`（屏幕变了）分离，让调用方能区分「动作已投递」与「动作已生效」。
3. **⭐⭐⭐⭐⭐ 触摸可靠性被实测并公开**：2/70 → 0/70 → 0/24 的修复路径，以及「启动后 ≥2.8 秒」的窗口结论。
4. **⭐⭐⭐⭐ 三套测试分层**：协议套件（无设备）、fixture 脚本（一次性模拟器 + fixture app）、真机 e2e（授权设备验收）。
5. **⭐⭐⭐⭐ 三种接入方式并存**：MCP server（Claude Code / Codex / 任意 `mServers` JSON）、独立终端 agent（`poki login` / `poki status`）、消息渠道（`poki imessage` / `poki telegram`）。
6. **⭐⭐⭐⭐ 远程接入与多设备**：`native/bridge/src/remote.rs` + `docs/remote-iphone.md` + `docs/verification/tailscale-pr-validation.md`；`bin/prepare-remote.mjs`；多设备时用 `--device '<device UUID>'` 显式选择。
7. **⭐⭐⭐ OCR 与粘贴板**：`native/ocr.swift` + `native/bridge/src/pasteboard.rs`；`bin/verify-platform.mjs` 专门报告 pasteboard 限制（并说明该脚本「so it does not verify clipboard writes on this runtime」）。
8. **⭐⭐⭐ fixture app 自带**：`bin/fixture-app/` 是一个 Xcode 工程（`PokiMCPFixture`），使端到端验证不依赖第三方应用。
9. **⭐⭐⭐ `eval-first-call.mjs`**：把「首次调用延迟」做成可复算的评测脚本，`docs/verification.md` 的中位数表（Claude Code / Codex CLI × Counter / Form × batch / single-step）由它产生。
10. **⭐⭐ agent 技能**：`skills/poki-mcp/SKILL.md`，README 直接给出「让 agent 装它」的一句话指令。

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 本地 iOS 设备执行层（Rust native bridge）+ MCP 协议层（Node stdio→HTTP）+ agent 层（独立 CLI / 消息渠道）+ 文档与 fixture app；**不含云端服务** | 依据根树 25 项与 `native/bridge/src/` 的文件清单；`ax.rs` 与 `roles.json` / `traits.json` 的实现**未读** |
| 主路径 | agent（或 MCP 客户端）→ stdio → 本地 HTTP → agent 编排层 → native bridge → USB/Wi-Fi 连接的 iPhone → **读回截图** → 判断 → 下一步 | 主路径为 README 描述 + 目录结构的语义抽象；`stream.rs` 的连接生命周期与 `roles.json` 的角色模型**未核验** |
| 关键权衡 | **① 免越狱 vs 能力上限**（换来实现稳定性与可分发的许可友好性）；**② 真实设备 vs 可复现性**（作者用「真机日志 + 明确标注不可外推」而非「只报模拟器漂亮数字」）；**③ 模拟器验证 vs 真机验收**（两套脚本分开，明确后者不在 `npm test` 内）；**④ AGPL + 预编译分发 + 自动更新 vs 许可义务**（作者对 AGPL 的网络服务义务做了工程应对） | ①②③ 有原文直接支撑（README 与 `docs/verification.md`）；④ 是本日报基于「AGPL-3.0-only + 提供 tar.gz + 每日 release 检查」三项事实的**推断**，项目未如此陈述 |
| 最小 PoC | **不要先接真机**：先在 iOS 模拟器上跑 `bin/setup` → `npm start` → `bin/verify-fixture.mjs`，用自带 `PokiMCPFixture` app 验证 `tap_text` 与 `screen_changed` 的双信号行为；模拟器通过后再用 `bin/verify-platform.mjs`；**真机环节必须由用户在授权设备上完成** | PoC 顺序依据 `docs/verification.md` 的测试分层与「They do not establish real-device cancellation… Those checks still require separately authorized device acceptance」推导 |
| 证据边界 | **可核验**：`docs/verification.md` 全文、README 的平台/许可/风险声明、目录树、测试脚本清单、GitHub 元数据。**未核验**：所有触摸数字均为**作者自测结果的转述**，本日报**未运行该工具、未连接任何 iPhone、未复现任何测量** | `agent/` 目录（Poki Agent，含 `gpt-6.1-terra` 默认模型）**未审**；Linux 社区移植 `carrotciallo/poki-for-linux` 在仓库外，**未核验** |

## 架构启发

**⭐⭐⭐⭐⭐ 启发一：接口语义要强制调用方注意，而不只是文档提醒。**

`sent: true` + `screen_changed: false` 这对返回值，把「投递」与「生效」拆成两个可断言的信号。**⭐⭐⭐⭐⭐ 很多项目只给一个 `success: true`，把判断责任推给调用方 —— 结果调用方不看屏幕，于是把失败的触摸当成成功。** poki 的做法让「慢一步」（写入到生效之间）成为可观测状态，而不是隐藏的失败。

**⭐⭐⭐⭐⭐ 启发二：把「我测过的」和「我测过的适用范围」放在同一张表里。**

poki 的表格里每个数字都带一句边界（「These numbers only apply to that single search field.」）。**⭐⭐⭐⭐⭐ 这比「测试覆盖率 87%」这类指标有用得多 —— 前者告诉你这个结论能不能搬到你的场景，后者只告诉你代码跑过多少。**

**⭐⭐⭐⭐⭐⭐ 启发三：把「已知失败」写进产品文档，而不是等 issue。**

「Tapping a target next to a bottom floating bar had no effect 4 of 4 times… **This is not fixed.**」—— 这类句子在 README 里非常罕见。**⭐⭐⭐⭐⭐ 它的价值不在于诚实本身，而在于它把「已知坏掉的路径」变成了可被 agent 规划时避开的显式约束**（agent 读文档时会避开那个交互位置）。

**⭐⭐⭐⭐⭐⭐⭐ 启发四：把「测量脚本」和「测量结果」一起交付。**

`bin/eval-first-call.mjs` 与 `docs/verification.md` 的中位数表是一对。**⭐⭐⭐⭐⭐⭐ 这意味着任何人都可以重跑那张表 —— 而文档里那句「These numbers … have not been re-run」反而承认了这一点。** 交付测量工具比交付数字更值钱。

**⭐⭐⭐⭐⭐ 启发五：把「需要的外部条件」写进警告，而不是埋进文档。**

「If you ask it to send messages or make payments, it will.」—— 一句提醒，放在读者必然经过的位置。

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart LR
  Client[MCP 客户端<br/>Claude Code / Codex / 任意 mcpServers] --> Stdio[src/stdio.mjs<br/>stdio 到 HTTP 桥]
  Stdio --> Orch[src/batch.mjs 等<br/>批处理与编排层]
  Agent[独立 Poki Agent<br/>poki CLI / imessage / telegram] --> Orch
  Orch --> Bridge[native/bridge (Rust)<br/>apps / gesture / stream / pasteboard / remote]
  Bridge --> Device[真实 iPhone 或 模拟器<br/>USB 配对 或 Wi-Fi]
  Device --> Screen[屏幕截图回读]
  Screen --> Orch
  Orch --> Dual[双信号返回<br/>sent 写入确认 + screen_changed 生效确认]
  Bridge --> Native[设备侧原生能力<br/>ocr.swift / pasteboard / simulator.m]
  Bridge -.测试夹具.-> Fixture[bin/fixture-app<br/>PokiMCPFixture 一次性 app]
  Bridge --> Eval[bin/eval-first-call.mjs<br/>可复算的首次调用延迟评测]
  Eval --> Doc[docs/verification.md<br/>真机日志与模拟器数据分节]
  Dual --> Doc
  Stdio --> Auth[鉴权 / 租约 / 会话<br/>协议套件覆盖 不触碰设备]
  Auth -.仅协议层证明.-> Doc
```

## 定位判断

**⭐⭐⭐⭐⭐ 基础设施候选型项目（agent 触达真实设备的一条务实路线），目前是本日报证据充分度最高的项目之一。**

它的位置很清楚：**在「云端大模型」与「物理世界」之间做一层本地、可审计的设备适配**。同类项目多数要么依赖云端服务（数据出境、隐私、延迟），要么依赖越狱（不稳定、不可分发）。poki 走的是「本地 + 免越狱 + 协议标准化（MCP）」这条组合。

**⭐⭐⭐⭐⭐ 而它与本日其余项目最大的不同是：它的产出可以被第三方逐条核对。** `docs/verification.md` 的数字可以重跑（`bin/eval-first-call.mjs`），测试套件可以看，fixture app 可以自己编译，第三方许可清单可以逐条查。

**⭐⭐ 定位的限定**：**平台仅 macOS**（需要完整 Xcode 与 iOS 工具链），Linux 走仓库外维护的社区移植（`carrotciallo/poki-for-linux`，issue #16），**真机验证仅覆盖中文界面与竖屏**。这些不是小问题 —— 它们直接限制了可用场景。

## 风险 / 局限 / 泡沫点

- **⭐⭐⭐⭐⭐ 真机验证面极窄**：README 明写「Physical iPhone support has been verified **only on iPhones using the Chinese interface**」「Physical devices support **portrait orientation only**」「App container export and direct links to Settings subpages are unavailable.」**⭐⭐⭐⭐⭐ 即：非中文界面、横屏、以及部分系统导航路径都属于未验证区。**
- **⭐⭐⭐⭐⭐ 已知未修的交互失败**：`docs/verification.md` 明确记录「Tapping a target next to a bottom floating bar had no effect 4 of 4 times in the Settings app. **This is not fixed.**」以及「Two earlier `tap_text` calls … returned `sent: true` but had no effect. **We have not reproduced this failure**」。**⭐⭐⭐⭐ 这些是产品层面的真缺陷，不是文档瑕疵。**
- **⭐⭐⭐⭐ 未测的手势**：`drag` 与 `pinch` 「were not measured」。
- **⭐⭐⭐⭐ 平台门槛**：macOS 15+、完整 Xcode、Rust、Node.js 24+、ffmpeg；**无 Linux/Windows 一等支持**。
- **⭐⭐⭐⭐⭐ 隐私与金钱风险**：屏幕内容会发送到用户配置的模型服务；agent 可以真的发消息、真的付款。**⭐⭐⭐⭐ 这不是漏洞而是设计，但使用者必须知道。**
- **⭐⭐⭐ 模型绑定**：Poki Agent 默认模型写死为 `gpt-6.1-terra`（low reasoning），可用 `POKI_AGENT_MODEL` 覆盖。**⭐⭐⭐ 依赖一个特定前沿模型名，意味着上游改名即需跟改。**
- **⭐⭐⭐ 供应链面**：提供 `curl | sh` 式的预编译包与每日自动 release 检查 —— 便利，但**自动更新本身是攻击面**（可用 `POKI_NO_UPDATE_CHECK=1` 关闭）。
- **⭐⭐⚠️ subs 仅 1**：406⭐ 而深度订阅者 1 个。**⭐⭐ 结合 forks=83 看，这不是「无人使用」也不是「广泛使用」的真实项目，而是「被大量 fork 尝试过」的形态 —— 原因待观察。**

## 与同类项目的关系

- **⭐⭐⭐⭐⭐ vs 越狱方案（如基于 frida / Substrate 的自动化）**：越狱路线能力上限更高（可注入进程、可读更多数据），但系统升级即失效、且难以合法分发。**poki 用「免越狱 + 有限但稳定」换取了可分发性。**
- **⭐⭐⭐⭐⭐ vs 官方 XCUITest / Shortcuts**：官方路径合规性最好，但只能在有限场景下操作，且难以支撑「读屏 → 推理 → 自由交互」的闭环。**poki 提供了更自由的交互面。**
- **⭐⭐⭐⭐ vs 云端手机农场（如各类 device cloud）**：云端方案无需本地设备，但数据必须出境、成本随调用计费、无法处理个人敏感内容。**poki 的本地化是其核心差异。**
- **⭐⭐⭐⭐ vs 其他 MCP server 项目**：MCP 生态中大量 server 是「包一个 API」；poki 是少见的**「包一个物理设备」**的 server，**因此它的失败模式是物理的（触摸没生效），而不是 API 的（HTTP 500）** —— 这也是它必须发明 `screen_changed` 的原因。
- **⭐⭐⭐ 与本日报的 `hermes-voice` 对比**：两者都做「把既有设备接入 agent」，但 poki 面向触屏设备的**精细操作**，hermes-voice 面向语音设备的**会话维持**。**后者的会话问题（`X-Hermes-Session-Id`）与前者的问题（触摸是否生效）在结构上同类** —— 都是「客户端以为成功、实际没生效」。

## 是否值得持续跟踪

**⭐⭐⭐⭐⭐ 值得跟踪，且是本日报证据质量最高的项目之一。**

理由不是星数，而是：**它提供了一份「如何在设备自动化这种高失败率场景里做可信验证」的完整可复制样例**。`docs/verification.md` 的写法可以直接搬用到任何「动作可能失败」的系统 —— 机器人控制、UI 自动化、支付流程。

**⭐⭐⭐⭐ 具体跟踪方式**：
1. 跟踪 **`docs/verification.md` 的修订**：新条目是「新增已知失败」还是「修复已知失败」，这是它成熟度的直接读数；
2. 跟踪 **`docs/verification/` 子目录的扩充**（目前有 `cellular-test-plan.md` / `tailscale-pr-validation.md`）—— 说明验证面在扩大；
3. 跟踪 **真机验证的支持范围**（中文界面 → 多语言？竖屏 → 横屏？），这是它从「个人工具」走向「可用产品」的关键；
4. 跟踪 **`subscribers_count` 是否离开 1**；
5. 跟踪 **`poki-for-linux` 社区移植是否被上游合并**。

## 后续观察点

- **⭐⭐⭐⭐⭐ `docs/verification.md` 中「This is not fixed」的条目数是否下降** —— 这是产品成熟度的单一最佳指标。
- **⭐⭐⭐⭐ 真机支持语言是否从「仅中文」扩大**；
- **⭐⭐⭐⭐ `drag` / `pinch` 是否获得实测数据**；
- **⭐⭐⭐⭐ 社区移植 `carrotciallo/poki-for-linux` 是否被纳入上游仓库或成为官方支持的后端；
- **⭐⭐⭐⭐ `subscribers_count` 与 `forks` 的比值是否收敛**（83 fork / 1 sub 是本日最刺眼的不对称之一）；
- **⭐⭐⭐⭐⭐ 默认模型从 `gpt-6.1-terra` 迁移后的兼容性处理**；
- **⭐⭐⭐ `bin/eval-first-call.mjs` 产出的中位数表是否随版本更新** —— 若长期不更新，说明「可复算」承诺在退化。

---
> 数据来源: GitHub REST API (2026-11-06T22:00Z 快照区间) | Stars: 406 | Forks: 83 | Subscribers: 1 | Open Issues: 10 | License: AGPL-3.0-only | 语言: JavaScript | 体积: 4,097 KB | Commits: 23 | Contributors: 2 | Releases: 2 (2 assets) | 创建: 2026-11-05T15:04:31Z | 最后推送: 2026-11-06T16:22:45Z
> 本档案未核验项：所有触摸与延迟数字均为作者自测结果的转述（本日报未运行该工具、未连接任何 iPhone）；`native/bridge/src/ax.rs`、`roles.json`、`traits.json` 的实现；`agent/` 目录；`carrotciallo/poki-for-linux` 社区移植。
