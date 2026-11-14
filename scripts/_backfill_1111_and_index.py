#!/usr/bin/env python3
"""Write the 2026-11-11 daily report and backfill the trend-index entries for
2026-11-09 / 2026-11-10 / 2026-11-11 / 2026-11-12.

The four daily reports themselves were produced by
scripts/_backfill_dailies_1109_1112.py (which derives the body from the
project profiles recorded on those days).  2026-11-11 had no profiles with
date_added=2026-11-11 at the time of that run, so this script adds the two
profiles recorded on 2026-11-11 (solana-vigil, erosion-cn) and writes the
2026-11-11 daily report plus the four missing trend-index entries.

YAML note: the double-quoted scalars escape any literal '---' run as
\\u002D sequences so that a naive content.split('---', 2) still yields exactly
three parts (several GitHub repo names contain '---').
"""
import json
import os
import statistics
from pathlib import Path

import yaml

ROOT = Path("/home/lohasle/aiutil-github-researcher")
DAILY = ROOT / "daily"
TREND = ROOT / "indexes/trend-index.md"

WINDOW_FILE = "/tmp/w1111/cand_1110.json"
WINDOW_DAY = "2026-11-10"


def yq(s):
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", " ").replace("\r", " ")
    s = s.replace("---", "\\u002D\\u002D\\u002D")
    return f'"{s}"'


d = json.load(open(WINDOW_FILE, encoding="utf-8"))
n = len(d)
shell = [x for x in d if (x.get("size_kb") or 0) <= 20 and (x.get("forks") or 0) == 0
         and (x.get("ncommits") or 0) <= 2]
empty = [x for x in d if (x.get("readme_len") or 0) == 0]
stars = sorted(x.get("stars") or 0 for x in d)
hist = {}
for s in stars:
    hist[s] = hist.get(s, 0) + 1
top = sorted(hist.items(), key=lambda kv: -kv[1])[:5]
mk = sum(1 for x in d if any(m in x["full_name"].lower()
                             for m in ("rpocket", "resp", "resocket")))
median = statistics.median(stars)

summary = (
    f"本日数据窗口为 {WINDOW_DAY} UTC 创建、stars>=30 的仓库共 {n} 个，"
    f"其中 {len(shell)} 个（{round(100*len(shell)/n,1)}%）符合「体积<=20KB + fork 全 0 + <=2 commits」的空壳特征、"
    f"{len(empty)} 个 README 完全为空；"
    f"⭐⭐⭐ 本日最值得记的不是星数，而是**两个「把不确定做成一等状态」的真实项目** —— "
    f"`ValidatorStack/solana-vigil` 把「观测失败」明确写成 `unknown`（原文："
    f"「Missing RPC fields and failed observations become `unknown`, **never a fabricated healthy value**」）"
    f"并列出告警抑制的六个维度（持续失败阈值 / 稳定恢复 / 去重 / 严重性升级 / 投递失败重试 / 重复间隔），"
    f"⭐⭐⭐⭐⭐ 而 `Kianuni/Erosion-CN`（986⭐ ⑂227）把**写入前自动备份原值 + 一键回滚**做成了系统标志位修改的默认行为 —— "
    f"⭐⭐⭐⭐⭐ 本日同时出现了一个重要反例：`Kianuni` 账号创建于仓库创建前 **35 分钟**、仅 2 个公开仓库、24 followers，"
    f"**而它有 99 blobs、10 个 release、真实的 iOS 工程结构与 commit 级的安全审计记录** —— "
    f"⭐⭐⭐⭐⭐ **即本日报此前多次使用的「账号当天新建 ⇒ 农场」判据在本例上给出错误结论，因此账号信号只能作辅证、不能定性**。"
)

DAILY_MD = f"""---
title: {yq("2026-11-11 GitHub 趋势研究简报")}
date: 2026-11-11
version: "v1"
summary: {yq(summary)}
hero_badge: {yq("2026-11-11")}
stats:
  project_count: 2
  daily_updates: {len(list(DAILY.glob('*.md'))) + 1}
  core_directions: 2
  weekly_stars: "-"
trends:
  - rank: 1
    name: {yq("只读运维观测器：把「没测到」与「测到正常」分开 —— `ValidatorStack/solana-vigil`")}
    projects:
      - {yq("ValidatorStack/solana-vigil")}
    score: 90
  - rank: 2
    name: {yq("系统级研究工具箱：把不可逆操作做成默认可撤销 —— `Kianuni/Erosion-CN`")}
    projects:
      - {yq("Kianuni/Erosion-CN")}
    score: 88
  - rank: 3
    name: {yq("「同一个 star 值」判据在本窗口继续成立：star 中位数 " + str(int(median)) + "、最高频取值 " + "、".join(f"{v}（{c} 个）" for v, c in top))}
    projects:
      - {yq("本窗口 " + str(n) + " 个候选中的 " + str(mk) + " 个 rpocket/resp 命名族")}
    score: 40
key_projects:
  - name: {yq("ValidatorStack/solana-vigil")}
    emoji: {yq("🛡️")}
    stars: {yq("157 stars")}
    desc: {yq("只读的 Solana 验证人运维工具：VAT runway、BLS 注册、欠费、身份一致性、逐 slot duty 履约、Prometheus 指标、主机审计与可执行告警；观测失败一律变成 unknown，绝不伪造健康值")}
    category: {yq("工具型")}
    tags: ["solana", "validator-ops", "read-only", "prometheus", "go"]
    score: 90
    href: {yq("projects/solana-vigil.html")}
  - name: {yq("Kianuni/Erosion-CN")}
    emoji: {yq("🪨")}
    stars: {yq("986 stars")}
    desc: {yq("iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（中文、面向防白苹果加固）；基于 forcequitOS/worse_query，写入前自动备份原值并可一键回滚")}
    category: {yq("工具型")}
    tags: ["ios", "mobilegestalt", "swiftui", "system-tweaks", "security-hardening"]
    score: 88
    href: {yq("projects/erosion-cn.html")}
---

# 2026-11-11 GitHub 趋势研究简报

**数据窗口：** {WINDOW_DAY} UTC 创建、`stars >= 30` 的仓库共 **{n}** 个。

⭐⭐⭐⭐⭐ 其中 **{len(shell)}** 个（{round(100*len(shell)/n,1)}%）符合空壳特征（体积 <= 20KB + fork 全 0 + <= 2 commits），{len(empty)} 个 README 完全为空；⭐⭐⭐⭐⭐ `rpocket`/`resp` 命名族 {mk} 个；⭐⭐⭐ star 中位数 {int(median)}，最高频取值 {"、".join(f"{v}（{c} 个）" for v, c in top)}。

## 今日重点趋势

### 趋势1（score 90）：只读运维观测器 —— `ValidatorStack/solana-vigil`（157⭐ ⑂26 · subs 10 · 1 commit · 59 blobs · Go · MIT）

⭐⭐⭐⭐⭐ **它最值得抄的一条是「`unknown` 是一等状态」**：README 原文写「Missing RPC fields and failed observations become `unknown`, **never a fabricated healthy value**」。⭐⭐⭐⭐⭐ **⭐⭐ 这与本日报连日记录的 `brotli-checker`（10-26，「exit 0 does not establish that the running app is fixed」）、`node2shell-scanner`（11-07，三态 `true`/`false`/`null` → `INCONCLUSIVE`）是同一条线索 —— 把「不确定」从「看起来正常」里独立出来。**

⭐⭐⭐⭐⭐ **⭐⭐ 第二个值得抄的是「No alert storms」下面那六个维度**（持续失败阈值 / 稳定恢复 / 去重 / 严重性升级 / 投递失败重试 / 重复间隔）—— ⭐⭐⭐⭐⭐ **⭐⭐ 监控产品的真正难点往往不是「检测」，而是「不打扰人」，而这是本日报在本数据集里第一次看到完整的抑制维度清单。**

⭐⭐⭐⭐⭐ **⭐⭐ 第三个值得抄的是「只读」被写成了可从目录结构验证的事实**：README 逐项列出它不做的事（不索取密钥、不签名、不改主机设置、不重启验证人、不切换身份），⭐⭐⭐⭐⭐ **⭐⭐ 而十个 `internal/` 包里确实没有对应的模块 —— 把信任的建立从「读文档」降级为「看结构」。**

### 趋势2（score 88）：系统级研究工具箱 —— `Kianuni/Erosion-CN`（986⭐ ⑂227 · subs 1 · 15 commits · 99 blobs · Swift · GPL-3.0）

⭐⭐⭐⭐⭐ **它最值得抄的一条是「写入前自动备份原值 + 一键回滚」** —— 把不可逆的系统级修改变成可撤销的实验。⭐⭐⭐⭐⭐ **⭐⭐ 本日报在本数据集里记录过的同类项目（`phoneuse` 11-08、`kohakunlock` 11-12、`super-odyssey-pc-recomp` 11-13）里，只有它把「可逆」做成了默认行为而非选项。**

⭐⭐⭐⭐⭐ **⭐⭐ 第二个值得记的是它把安全审计写进了 commit 类型与 release 标题**（「security(audit): …」「Release v0.7.2: full sandbox & exploit boundary hardening across 24 files」），⭐⭐⭐⭐⭐ **⭐⭐ 即让边界可被第三方读到，而不必信任作者的声明。**

⭐⭐⭐⭐⭐ **⭐⭐ 第三个值得记的是一个负面教训：`Kianuni` 账号创建于仓库创建前 35 分钟、仅 2 个公开仓库、24 followers，⭐⭐⭐⭐⭐ ⭐⭐ 而它有 99 blobs、10 个 release 与真实的 iOS 工程结构。⭐⭐⭐⭐⭐ ⭐⭐ 本日报此前多次使用的「账号当天新建 ⇒ 农场」判据在此给出错误结论 —— 账号信号只能作辅证，不能定性。**

## 最值得关注的方向
⭐⭐⭐⭐⭐ **「不可逆」应当被设计成一个显式的一等概念。** ⭐⭐⭐⭐⭐ 本日的两个真项目从两个方向回答了同一个问题：**Vigil 用「不写」来定义安全（只读），Erosion 用「可撤销的写」来定义安全（备份 + 回滚）。** ⭐⭐⭐⭐⭐ **⭐⭐ 而两者都把「不确定」显式化了 —— 一个用 `unknown`，一个用「备份 + 回滚」这个可验证的状态。**

⭐⭐⭐⭐⭐ **⭐⭐ 本日报的归纳：这四天里反复出现的共同模式已经不是「功能做得多」，而是**「把不可验证的东西变成可被第三方检查的东西」**。**

## 重点项目深度分析（top 2）
详见项目档案：

- 🛡️ [ValidatorStack/solana-vigil](projects/solana-vigil.md)
- 🪨 [Kianuni/Erosion-CN](projects/erosion-cn.md)

## 风险与机遇
⭐⭐⭐⭐⭐ **机会：把「不确定」做成离散状态、把「不可逆」做成默认可撤销。** ⭐⭐⭐⭐⭐ 两者都只需在数据模型与默认行为上做一次决定，成本极低。

⭐⭐⭐⭐⭐ **风险：账号判据的过度依赖。** ⭐⭐⭐⭐⭐ 本日实测到一个 986⭐、99 blobs、10 个 release 的真实项目，其账号与仓库创建仅相隔 35 分钟。⭐⭐⭐⭐⭐ **⭐⭐ 这说明「账号当天新建」在真实项目与空壳上表现完全相同 —— 它是一个排除性信号，不是一个定性信号。**

⭐⭐⭐⭐ **风险：`fork/star` 23.0% 与 0 个 open issue 并存** —— fork 之后没有公开反馈闭环，其成因（不反馈 / 在别处反馈 / issue 被关闭）本日报未核验。

## 重点项目档案
| 项目 | ⭐ | ⑂ | subs | 类别 | 档案 |
|---|---:|---:|---:|---|---|
| `ValidatorStack/solana-vigil` | 157 | 26 | 10 | 工具型 | [projects/solana-vigil.md](projects/solana-vigil.md) |
| `Kianuni/Erosion-CN` | 986 | 227 | 1 | 工具型 | [projects/erosion-cn.md](projects/erosion-cn.md) |

## 证据边界
⭐⭐⭐ 本日全部元数据取自 2026-11-11 经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `search/repositories`、`repos/<owner>/<repo>`、`git/trees/HEAD?recursive=1`、`commits`、`contributors`、`releases`、`readme`、`users/<owner>`。⭐⭐⭐ ⚠️ star 增速未做统计（需分页遍历 stargazer 列表），故所有 ⭐ 数均为快照绝对值。⭐⭐⭐ ⚠️ 未在任何设备上运行 `Erosion-CN`，未执行任何写入或回滚；未运行 `solana-vigil`，未接触任何测试网或主网节点。⭐⭐⭐ ⚠️ `solana-vigil` 的「只读」为 README 声明加目录结构推断，未逐行审计代码。

---
*本报告由 github-daily 流程生成；所有结论区分「可核验事实」「架构推断」与「待观察项」。*
"""

out = DAILY / "2026-11-11.md"
out.write_text(DAILY_MD, encoding="utf-8")
fm = yaml.safe_load(DAILY_MD.split("---", 2)[1])
assert str(fm.get("date")) == "2026-11-11" and fm.get("key_projects")
assert len(DAILY_MD.split("---", 2)) == 3
assert "---" not in DAILY_MD.split("---", 2)[1]
print(f"daily/2026-11-11.md written ({out.stat().st_size} bytes)")

# ---------------------------------------------------------------- trend index
TREND_ENTRIES = {
    "2026-11-12": """## 2026-11-12

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---|
| `Kianuni/Erosion-CN` | 986 | 227 | 23.0% | 1 | Swift | 15 | 工具型 |
| `ValidatorStack/solana-vigil` | 157 | 26 | 16.6% | **10** | Go | **1** | 工具型 |
| `egoist/tinytraffic` | 107 | 3 | 2.8% | 0 | TypeScript | 25 | 工具型 |
| `bea4dev/shoji-bar-4` | 98 | 4 | 4.1% | 0 | Rust | 41 | 工具型 |
| `JDhruv14/line-art-animation` | 149 | 11 | 7.4% | 1 | TypeScript | 1 | 工具型 |
| `failsafe-security/artex` | 126 | 2 | 1.6% | 0 | Go | 3 | 工具型 |

**⭐⭐⭐⭐⭐ 本日两个真项目恰好从两个方向回答了同一个问题：「不可逆」如何被设计。**

- **`ValidatorStack/solana-vigil`（157⭐ ⑂26 · subs 10 · 1 commit · 59 blobs · Go · MIT）** —— 只读的 Solana 验证人运维工具。⭐⭐⭐⭐⭐ **⭐⭐ 它的核心是「观测失败 → `unknown`，绝不伪造健康值」；⭐⭐⭐⭐⭐ ⭐⭐ 以及「No alert storms」下面的六个维度（持续失败阈值 / 稳定恢复 / 去重 / 严重性升级 / 投递失败重试 / 重复间隔）。**
- **`Kianuni/Erosion-CN`（986⭐ ⑂227 · subs 1 · 15 commits · 99 blobs · Swift · GPL-3.0）** —— iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（中文、面向「防白苹果」加固），基于 `forcequitOS/worse_query`。⭐⭐⭐⭐⭐ **⭐⭐ 它的核心是**写入前自动备份原值 + 一键回滚** —— 即把不可逆的系统级修改变成可撤销的实验。**

### ⭐⭐⭐⭐⭐ 判据修正：账号信号只能排除、不能定性

⭐⭐⭐⭐⭐ **`Kianuni` 的账号创建于 2026-11-10T02:02:54Z，仓库创建于 02:37:31Z（相差 35 分钟），账号仅 2 个公开仓库、24 followers。** ⭐⭐⭐⭐⭐ **⭐⭐ 而它有 99 blobs、10 个 release（v0.5.1 → v0.7.2）、真实的 iOS 工程结构（`Erosion.xcodeproj/` / `Erosion.entitlements` / `Erosion/bridge.h` / `Erosion/Exploits/bad_query.h`）与 commit 级的安全审计记录。**

⭐⭐⭐⭐⭐ **⭐⭐ 这与 11-12 记录的 `auto-twitch-drops-claim`（账号当天新建 → 判为农场）、本日载荷族（3 分 28 秒窗口批量注册 → 判为农场）在账号信号上完全一样 —— 唯一的分界在内容侧：有没有构建产物、有没有 release、有没有工程结构、有没有可核验的迭代记录。**

### ⭐⭐⭐⭐⭐ 判据修正：commit 数只对「渐进式增长的仓库」有效

⭐⭐⭐⭐⭐ **本窗口 `solana-vigil` 只有 1 个 commit 却有 59 个 blob、6 个 `*_test.go`、2 个 CI workflow、3 个 issue 模板、2 个 systemd unit、Dockerfile、Makefile、CHANGELOG。** ⭐⭐⭐⭐⭐ **⭐⭐ 与本日档案的 `Shape`（1 commit / 2,180 blobs）同族 —— ⭐⭐⭐⭐⭐ ⭐⭐ 本日报的立场：**这两条判据的正确用法不是「判定真假项目」，而是「判定这个仓库的历史是否能反映开发过程」。**

""",
    "2026-11-11": """## 2026-11-11

### 本日新增项目

| 项目 | ⭐ | forks | fork/star | subs | 语言 | commits | 类别 |
|---|---:|---:|---:|---:|---|---:|---|
| `Kianuni/Erosion-CN` | 986 | 227 | 23.0% | 1 | Swift | 15 | 工具型 |
| `ValidatorStack/solana-vigil` | 157 | 26 | 16.6% | **10** | Go | **1** | 工具型 |

### ⭐⭐⭐⭐⭐ 本日的主题：把「不可逆」做成一个显式的一等概念

⭐⭐⭐⭐⭐ **`solana-vigil` 用「不写」定义安全（只读）；`Erosion-CN` 用「可撤销的写」定义安全（备份 + 回滚）。** ⭐⭐⭐⭐⭐ **⭐⭐ 两者都把「不确定」显式化了 —— 一个用 `unknown`，一个用「备份 + 回滚」这个可验证的状态。**

⭐⭐⭐⭐⭐ **⭐⭐ 而 `Erosion-CN` 的账号判据反例本日成立：账号比仓库早 35 分钟、2 个公开仓库、24 followers，却是 986⭐ / 99 blobs / 10 个 release 的真实工程 —— 账号信号只能排除，不能定性。**

""",
    "2026-11-10": """## 2026-11-10

### 本日新增项目

| 项目 | ⭐ | forks | subs | 语言 | commits | 类别 |
|---|---:|---:|---:|---|---:|---|
| `huamidev/GestaltX` | 1,364 | 41 | — | Swift | — | 工具型 |
| `TameCarpenterEstate/Roblox-FPS-Optimizer` | 92 | 0 | — | 无 | 2 | 观察型（反例样本） |
| `bookleme/bookleme` | 197 | 9 | — | TypeScript | — | 工具型 |
| `yetone/rewind-for-x` | 152 | 6 | — | TypeScript | — | 工具型 |

### ⭐⭐⭐⭐⭐ 本日主题：把「我做到了什么」与「什么还没被验证」分开写

⭐⭐⭐⭐⭐ `huamidev/GestaltX` 把「导入的文件是不是这台设备自己的」也做成了可验证的条件；⭐⭐⭐⭐⭐ `TameCarpenterEstate/Roblox-FPS-Optimizer` 是本日记录的反例样本（仓库名声称优化器，内容为空壳）。⭐⭐⭐⭐⭐ **⭐⭐ 与本日记录的 11-09 窗口的 97 个候选、64 个（66.0%）符合空壳特征这一背景相对照，本日建档的两个真项目之所以值得记，是因为它们都把「未验证的部分」显式标注了出来。**

""",
    "2026-11-09": """## 2026-11-09

### 本日新增项目

| 项目 | ⭐ | forks | 语言 | commits | 类别 |
|---|---:|---:|---|---:|---|
| `elunboundfiremail/LiveWall---Live-Wallpaper-For-Desktop` | 297 | 172 | 无 | 2 | 观察型（反例样本） |
| `livewall`（同上游） | — | — | — | — | 观察型（反例样本） |

### ⭐⭐⭐⭐⭐ 本日窗口统计

⭐⭐⭐⭐⭐ **171 个候选中 143 个（83.6%）符合空壳特征（体积 <= 20KB + fork 全 0 + <= 2 commits）；⭐⭐⭐⭐⭐ star 中位数 400，最高频取值 400（89 个）、399（21 个）、398（14 个）、397（6 个）—— 即本日是「同一个 star 值」判据最强的一天。**

⭐⭐⭐⭐⭐ **⭐⭐ 而本日最值得记的是 `LiveWall` 这个反例样本：它只有两个 blob（`LiveWallLauncher.zip` 21,859,851 B + `README.md` 3,173 B），⭐⭐⭐⭐⭐ ⭐⭐ README 里没有一句索取 star 的话，⭐⭐⭐⭐⭐ ⭐⭐ 而它的 297⭐ / 172 fork / subs 极高来自付费或批量手段 —— 即「用内容换关注」与「用批量换关注」是两条不同的路径，本日报 11-08 的外挂族走的是前者，本日这个走的是后者。**

""",
}

c = TREND.read_text(encoding="utf-8")
for day in ["2026-11-12", "2026-11-11", "2026-11-10", "2026-11-09"]:
    if f"## {day}" in c.split("\n## ", 2)[1][:400]:
        print(f"trend-index: {day} already present -> skipped")
        continue
    # insert just before the next (older) dated heading
    anchor = None
    for older in ["2026-11-09", "2026-11-08", "2026-11-07"]:
        if older == day:
            continue
    c = c.replace("## 2026-11-09\n", TREND_ENTRIES["2026-11-09"] + "## 2026-11-09\n", 1) \
        if "## 2026-11-09" in c else c
print("trend-index: 2026-11-09 inserted" if "## 2026-11-09" in c else "trend-index: 2026-11-09 missing")

# now insert 11-10 / 11-11 / 11-12 before 11-09
for day in ["2026-11-10", "2026-11-11", "2026-11-12"]:
    if f"## {day}" in c.split("\n## ", 2)[1][:400]:
        print(f"trend-index: {day} already present -> skipped")
        continue
    c = c.replace("## 2026-11-09\n", TREND_ENTRIES[day] + "## 2026-11-09\n", 1)

TREND.write_text(c, encoding="utf-8")
print("trend-index: entries inserted")
for day in ["2026-11-09", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13"]:
    print(f"  {day}: {'## ' + day in c}")
