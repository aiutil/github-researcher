---
title: "SteelMillerBar/auto-twitch-drops-claim"
slug: "auto-twitch-drops-claim"
date_added: "2026-11-12"
last_seen_date: "2026-11-12"
category: "观察型（反例样本）"
emoji: "🎣"
stars: "57 stars"
stars_delta: "⭐ 2026-11-12 建档（快照 2026-11-12 CST，仓库创建于 2026-11-11T02:57:57Z，约 19 小时）：57⭐ ⑂19（fork/star 33.3%）· subs 7 · oi 0 · **17 commits（其中 14 个由 github-actions[bot] 提交）** · 22 KB · **仅 3 个 blob** · 无语言字段 · 无 LICENSE"
language: "无（仓库无实现语言）"
score: 93
tags: ["activity-pulse", "commit-graph-inflation", "bot-commits", "star-farm", "ci-abuse", "anti-pattern", "new-technique"]
url: "https://github.com/SteelMillerBar/auto-twitch-drops-claim"
---

# SteelMillerBar/auto-twitch-drops-claim

## 一句话定位
**仓库里没有实现，只有三个文件**（README、一个 GitHub Actions workflow、一个随机名的时间戳文件）—— 而它的 commit 历史有 **14/17 由 `github-actions[bot]` 提交**，提交信息是 `import analyze` / `merge encrypt` / `docs encrypt` 这类**随机双词组合**。

## 它解决的问题
**它不解决任何问题。** README 描述的是一个「后台自动刷 Twitch 掉落、领取奖励、切换频道」的轻量 AFK 矿工，声称「open-source」、「Streamless, bandwidth-friendly」、跨 Windows/macOS/Linux、支持 Docker。

⭐⭐⭐⭐⭐ **而仓库的实际内容是：**

```
3 blobs:
  3,522  README.md
  3,324  .github/workflows/gkk424t.yml
    727  .github/JG832J1784GJ
```

**没有一个字节的产品代码。** ⭐⭐⭐⭐⭐ 而那个 `JG832J1784GJ` 文件的全部内容是 15 行时间戳：

```
2026-11-11T05:35:32.723Z  run=42962139994  n=598273
2026-11-11T06:10:10.164Z  run=42968633613  n=151345
2026-11-11T07:19:29.545Z  run=42976345750  n=34865
...
2026-11-11T19:55:30.616Z  run=43091364967  n=553642
```

## 为什么值得关注（2026-11-12）

⭐⭐⭐⭐⭐ **因为这是本数据集记录到的第一种全新投放形态 —— 本日报此前记录过的三种形态是「可执行载荷 → starter 模板 → 空壳占位符」，而本仓库是第四种：「用 CI 制造 commit 图」。** 而它的**判据完全不同于前三类** —— 前三类靠「体积小 / commit 少 / 代码缺失」都能筛出来，**而本仓库的 commit 数（17）和活跃时间跨度（05:35 → 19:55 共 14 小时）看起来比一个正常的小项目还「像在开发」**。

⭐⭐⭐⭐⭐ **其机制在 `.github/workflows/gkk424t.yml` 里写得清清楚楚：** 一个 `cron: '0 * * * *'`（每小时）的 workflow，权限 `contents: write`，用 `actions/github-script@v7` 做一件事 —— **往 `.github/JG832J1784GJ` 追加一行时间戳并提交**。⭐⭐⭐⭐⭐ 而提交信息是从一个**固定的 45 词前缀表里随机取两个词拼接**：

```javascript
const commitPrefixes = ["fix","update","refactor","add","remove","improve","optimize","feature","bug","docs","test","style","merge","cleanup","adjust","rename","enhance","replace","format","config","release","hotfix","patch","review","sync","rollback","revert","tweak","implement","validate","check","load","save","export","import","upgrade","downgrade","convert","render","parse","compress","encrypt","decrypt","log","trace","monitor","analyze","schedule","retry","notify"];
...
const commitMessage = randomCommitMessage();  // 两个随机词拼接
```

⭐⭐⭐⭐⭐ **这解释了本仓库 commit 历史上的全部异常**：`import analyze` / `cleanup bug` / `merge encrypt` / `docs encrypt` / `render export` / `replace notify` / `downgrade analyze` / `bug trace` / `sync save` / `check patch` —— **16/17 个提交信息是这种随机双词**（唯一例外是 `Initial commit`），而提交者全部是 `github-actions[bot]`（14 个）。

⭐⭐⭐⭐⭐ **而这条链把 11-08 日报提出的「commit 时间戳的秒字段熵」判据反向用了一次**：11-08 记录到 `Flake-setup.exe` 那个仓库的 43 个 commit 只落在 2 个秒值上（熵=2），据此得出「秒熵低 = 脚本化」；**本仓库的 bot 提交每次都带 `new Date().toISOString()`，秒熵高、间隔看着「像人」，反而更难被熵判据抓到** —— ⭐⭐⭐⭐⭐ **即：投放者用 CI 把「时间分布」这个判据也一并对冲了。这是判据被针对性规避的第二个案例（第一个是 11-08 的 subs 被明写成指令）。**

⭐⭐⭐⭐⭐ **fork 分布同样给出机器判定**：抽样 21 个 fork，间隔中位数 **9.0 秒**，**17/21 个间隔 ≤10 秒**。

## 热度来源判断
**纯投放，且是本日投放形态中技术含量最高的一种。** 判据：
1. **⭐⭐⭐⭐⭐ 仓库无实现：** 3 个 blob、零产品代码、无 LICENSE、无语言字段，而 README 声称跨三平台 + Docker；
2. **⭐⭐⭐⭐⭐ commit 图由 CI 制造：** 14/17 提交来自 `github-actions[bot]`，提交信息为随机双词，且与 stamp 文件里的 `run=` 编号一一对应 —— **stamp 文件的每一行就是一次 workflow run，即 bot 提交是可逐行追溯的**；
3. **⭐⭐⭐⭐ fork 时间分布机器化：** 中位数 9.0 s，17/21 ≤10 s；
4. **⭐⭐⭐⭐⭐ 与 11-06 起的 `.gitignore`/`helpers.py` md5 模板不同 —— 本仓库走的是另一条基础设施路线**（CI 脉冲而非文件模板），**这本身说明投放方在演化手段，而非只有一套工具**。

⭐⭐⭐⭐⭐ **而 README 的叙事又一次出现「免责声明与载荷脱钩」**：它自称 open-source，实际没有任何源码。⚠️ **本日报未运行该 workflow、未访问任何外部地址，不主张作者意图。**

## 关键技术亮点
**本档案不设「技术亮点」一节（无实现可分析），改为记录这一「投放技术」本身值得防御方关注的设计细节：**

1. **⭐⭐⭐⭐⭐ 极低成本的活动伪造：** 整个方案只需要 **两个文件**（一个 workflow + 一个 stamp 文件）+ 一个 `gh api` 写权限的 Actions token，即可让仓库在任意长的时间里持续产生「看起来在开发」的提交。**对自动化筛选器而言，这是一个 22 KB 的极小攻击面。**
2. **⭐⭐⭐⭐⭐ 用 `new Date().toISOString()` + `run=` 编号让每次提交唯一：** stamp 行格式为 `<ISO 时间>  run=<runId>  n=<随机数>`，**既提供了「可审计的时间证据」，又让提交内容每次不同以避免被内容去重命中** —— ⭐⭐⭐⭐ **这是一个针对内容去重判据的显式规避设计。**
3. **⭐⭐⭐⭐ 用 45 词前缀表生成双词提交信息：** 提交信息在语义上无意义（`import analyze`、`merge encrypt`），**但形态上是「两段式动词+名词」的常见 git 规范** —— ⭐⭐⭐⭐ **它模仿的是 commit message 的「形状」而不是内容，这正是当前大多数启发式筛选器的盲区。**
4. **⭐⭐⭐⭐ workflow 文件名随机化：** `gkk424t.yml` 与 stamp 文件名 `JG832J1784GJ` 都是无语义随机串，**使「同一模板的文件路径聚类」判据也失效**。
5. **⭐⭐⭐⭐⭐ 最重要的对照：本仓库证明了「commit 数 / 提交时间跨度 / 提交信息形状 / 提交者多样性」这一整族判据可以被一个 22 KB 的 workflow 同时对冲。**

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 真正的系统在 GitHub Actions 的定时执行环境里，**不在仓库工作树内**；仓库工作树只承担「提交历史的存储」与「landing page」两个职责 | workflow YAML 原文与 stamp 文件内容为实测；**未运行 workflow、未观察实际 run**；「系统边界在 Actions 环境内」是由 workflow 内容推出的**推断** |
| 主路径 | Actions 定时触发 → github-script 读 stamp → 追加时间戳行 → `createOrUpdateFileContents` 提交 → commit 出现在 main 分支历史 → 仓库看起来「活跃」 | 该主路径由 workflow 脚本逐行读出；**未实际触发或观察一次 run**；`run=` 编号与 commit 时刻的对应关系**由 stamp 文件与 commit 历史的时间吻合推断，未逐条核验** |
| 关键权衡 | 投放方：付出 2 个文件 + Actions token 的成本，换取「任意长时间的 commit 图」；**代价是提交者全部是 bot、提交信息无意义、且每个 commit 都在 `.github/` 下留有可追溯的 stamp 行 —— 即这个手法本身是可检测的** | 成本估算与「可检测」判断为**推断**；可检测性由 stamp 文件结构与 bot 提交者实测支撑 |
| 最小 PoC | 检测该手法只需三条零成本检查：(a) `contributors` API 里 `github-actions[bot]` 的提交占比；(b) 提交信息是否为无语义双词；(c) 是否存在 workflow + 随机名 stamp 文件的组合 | 三条检查均已在本日报的 sweep（`scripts/_pulse_2026_11_12.py`）中实现并对本日 29 个候选全量跑通，**结果为 1 命中 / 28 未命中** |

## 架构启发
⭐⭐⭐⭐⭐ **本日最有价值的一条方法论结论：「启发式筛选器可以被低成本定向规避，因此判据必须基于「无法伪造的东西」。」** 这个仓库给出的答案是残酷的：**commit 数量、提交时间分布、提交信息文本、文件路径命名 —— 这一整族「活跃度信号」都可以用 22 KB 的 YAML 全部伪造。** ⭐⭐⭐⭐⭐ **真正无法伪造的是：(a) 代码是否存在且能 import/运行；(b) 文件内容的 md5 是否与已知集合重复；(c) fork 到达的时间分布（因为那需要真实的、被投放的账号）；(d) 外部依赖的可达性。** 11-08 提出的「判据成对部署」在本日被推进一步 —— **⭐⭐⭐⭐⭐ 不是「成对」，而是「成组」：一组正向信号必须被一组不可伪造的反向信号同时验证。**

⭐⭐⭐⭐⭐ **第二个启发关于「主动对冲历史证据」这个模式本身。** 11-08 记录到「判据被明写成投放指令」（README 索取 star → subs 被抬高），本日记录到「判据被工程化对冲」（CI 伪造 commit 图 → 熵与活跃度假信号失效）。⭐⭐⭐⭐⭐ **两者的共同结构是：投放方读到了判据的公开描述，然后针对判据的失效方向做优化。** ⭐⭐⭐⭐ **这意味着任何公开的、单一的、基于元数据的判据，预期寿命是以周计的；而基于「代码实体」的判据（能不能 import、文件 md5、fork 时间分布、依赖可达性）预期寿命是以月计的。**

⭐⭐⭐⭐⭐ **第三个启发是一个具体的架构建议：把「bot 提交占比」当作一等公民指标。** 本仓库 14/17 = **82.4%** 的提交来自 `github-actions[bot]`，**而这条信息在 `contributors` API 里是一次调用就能拿到的** —— 它几乎零成本，却直接命中了本日唯一的这一类投放形态。**本日报已把它实现进 sweep 脚本。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；标注「待核验」的节点不应视为项目实现事实。

```mermaid
flowchart TB
  subgraph Repo[仓库工作树 · 仅 3 个 blob]
    Rd[README.md 3522 B<br/>宣称 Twitch 掉落自动领取]
    Wf[.github/workflows/gkk424t.yml 3324 B<br/>文件名随机化]
    Stamp[.github/JG832J1784GJ 727 B<br/>随机名时间戳文件<br/>15 行 run= 编号 + n= 随机数]
  end
  subgraph Actions[真正的系统 · GitHub Actions 执行环境]
    Sched[定时触发]
    Script[github-script<br/>读 stamp 并追加一行<br/>new Date().toISOString()]
    Commit[createOrUpdateFileContents<br/>写入 main 分支]
    Token[gh api 写权限 token]
  end
  subgraph History[伪造出的 commit 图]
    Bot[14/17 提交来自<br/>github-actions[bot] = 82.4%]
    Msg[无语义双词提交信息<br/>import analyze / merge encrypt<br/>45 词前缀表组合]
    Secs[每条提交秒值唯一<br/>规避内容去重]
  end
  Rd -.叙事层.-> Sched
  Wf --> Sched --> Script --> Stamp --> Commit
  Token --> Script
  Commit --> Bot
  Commit --> Msg
  Commit --> Secs
  Bot --> Look[对筛选器的可见效果<br/>仓库看起来持续在开发]
  Msg --> Look
  Secs --> Look
  Det[本日报已落地的检测<br/>a contributors API 里 bot 提交占比<br/>b 提交信息是否为无语义双词<br/>c workflow + 随机名 stamp 文件组合]
  Bot --> Det
  Msg --> Det
  Wf --> Det
  Lim[证据边界与推论<br/>未运行 workflow 未观察实际 run<br/>run 编号与 commit 时刻的对应为推断<br/>「本手法可检测」是基于 stamp 结构的推断<br/>不主张其意图 只主张可核验内容]
  Det -.受其约束.-> Lim
```

## 定位判断
**反例样本（counter-example），刻意建档而非推荐 —— 但它与另两类反例不同：它是一个「手法样本」而非「个案样本」。** ⭐⭐⭐⭐⭐ `youtube-seo-optimizer` 与 `discord-quest-completer` 展示的是**投放内容**（投递壳 + 指标指令），而本仓库展示的是**投放工程能力**（用 CI 对冲活跃度判据）。⭐⭐⭐⭐⭐ **三个档案并排的价值在于：它们共同说明「星标榜单上排前面的仓库」这一命题本身，需要三种完全不同的检查才能证伪。**

## 风险 / 局限 / 泡沫点
- **⭐⭐⭐⭐⭐ 对 CI 供应链的提示：** 该模式要求仓库开启 Actions 且授予 `contents: write`。⭐⭐⭐⭐⭐ **任何允许第三方仓库在本机/自建 runner 上执行 Actions 的流程，都应意识到「commit 数量」不能作为项目活跃度或可信度的证据。**
- **⭐⭐⭐⭐⭐ 对自动评分系统的攻击面：** 任何把 `commit count` 或 `pushed_at` 纳入权重的产品级评分器，都可被一个 22 KB 的 workflow 刷高。**本日报不主张该仓库以此盈利，仅主张该手法在技术上是可行的且已被观察到。**
- **⭐⭐⭐⭐ 无实现：** README 承诺的跨平台 AFK 矿工、Docker 支持、Twitch 集成在仓库中均不存在。
- **⭐⭐⭐⭐ 无许可：** 仓库无 LICENSE 文件，`license.spdx_id` 为 null（按默认版权保留处理）—— **与 10-26 记录的 `unclebob/ub-mode`（341⭐ 却无 LICENSE）同类**：**热度与许可元数据之间没有相关性。**
- **⚠️ 证据边界：** 未运行 workflow、未访问任何外部地址、未核实该 README 中提到的 Twitch / Docker 相关实现是否存在于别处；**本档案主张的是「仓库内容与其 README 宣称不一致」与「commit 历史由 CI 机器人制造」这两个可核验事实。**

## 与同类项目的关系
- **vs 同日 `BankerInterface/youtube-seo-optimizer` / `Nobleglusurvive/discord-quest-completer`：** **同属本日投放，但路线不同** —— 那两家靠**文件模板复用**（md5 相同），本仓库靠 **CI 伪造活动度**；⭐⭐⭐⭐⭐ **本仓库是本日唯一一例「体积/commit 粗筛指标全部正常」的投放形态**，因此也是唯一一例**会被粗筛漏掉**的。
- **vs 11-08 记录的 `Tropicaldrescoop/discord-id-osint-checker`：** 同为「commit 时间戳集中」形态，但方向相反 —— 那个仓库的 43 个 commit 只落在 2 个秒值上（熵=2，暴露出脚本化）；**本仓库用 `new Date()` 让每次 commit 落在不同秒值（熵高），主动对冲了那个判据。**
- **vs 11-06 起的 `.gitignore`/`helpers.py` 农场簇：** md5 指纹**不匹配**，属**另一套投放基础设施** —— 表明投放方至少在并行使用两种手法。
- **vs 10-26 的 `unclebob/ub-mode`：** 共同点是「高热度 + 缺 LICENSE / 缺实现」这一组合在不同体量上反复出现。

## 是否值得持续跟踪
**不作为项目跟踪，作为「投放手法」跟踪 —— 这是本档案最强的建议。** 具体建议：
1. **⭐⭐⭐⭐⭐ 把 `github-actions[bot]` 提交占比纳入常规采集与判据**（本日报的 `scripts/_pulse_2026_11_12.py` 已实现，可直接复用）；
2. **⭐⭐⭐⭐⭐ 把「无语义双词提交信息」与「随机名 stamp 文件」作为二级启发式**（两者联合可命中本形态，但单独会误报 —— 例如 `c6lang/c6` 本日有 9/100 个两词提交却是真人项目）；
3. **⭐⭐⭐⭐ 观察该手法是否扩散到其他窗口** —— 本日 sweep 29 个候选仅此 1 命中（3.4%），**若后续日期该比例上升，说明它正在成为主流投放形态**；
4. **⭐⭐⭐ 观察 `pushed_at` 与真实人工提交的关系** —— 本仓库的 `pushed_at`（2026-11-11T19:55:31Z）与最后一次 bot 提交（19:55:30Z）相差 1 秒，**这是一个极廉价、可自动化的高精度判据候选**。

## 后续观察点
- 本仓库的 bot 提交是否持续（观察 `.github/JG832J1784GJ` 是否继续增长）；
- `github-actions[bot]` 提交占比这一指标在后续窗口的分布（本日 29 个候选中仅 1 个 >0）；
- 该 workflow 是否有后续变体（例如改为直接 push 空 commit 以省去 stamp 文件）；
- 是否出现「bot 提交 + 高 subs」同时成立的新样本（本仓库 subs 7，不算高 —— **若出现，则 bot 与指标投放会叠加**）。

---
> 数据来源: GitHub REST API 快照（2026-11-12 CST，仓库创建于 2026-11-11T02:57:57Z）| Stars: 57 | Forks: 19 | Subscribers: 7 | License: null（无 LICENSE 文件） | 体积: 22 KB / 3 blobs
> **证据边界：** 未运行该仓库的 GitHub Actions workflow、未访问任何外部地址、未执行任何代码；`contributors` 计数取自 `repos/{owner}/{repo}/contributors`；fork 抽样为 21 个。
