#!/usr/bin/env python3
"""Prepend the 2026-11-18 block to indexes/trend-index.md and daily-report.md.

Using python (not patch) to avoid the multi-match problem, per the runbook.
"""
from pathlib import Path

ROOT = Path("/home/lohasle/aiutil-github-researcher")

TREND_BLOCK = Path("/tmp/trend_index_1118.md").read_text(encoding="utf-8")

REPORT_BLOCK = """## 2026-11-18
**核心主题：** 本日最硬的发现是**我们自己的判据库第一次被加上对照组，结果被证伪了一条** —— ⭐⭐⭐⭐⭐ 本日报对 15 个 Trending 仓库各取最新 100 个 fork（**1,500 个 fork owner 账号**）实测「账号创建于 7 天内」的比例是 **38.0%**，⭐⭐⭐⭐⭐ 而对 11 个对照仓库（含 `torvalds/linux` / `rust-lang/rust` / `golang/go` / `sveltejs/svelte`）各取 100 个（**1,100 个**）的同口径比例是 **40.5%** —— **Trending 组反而更低**；⭐⭐⭐⭐⭐ **逐仓库看更反直觉：`golang/go` 80/100 · `rust-lang/rust` 72/100 · `torvalds/linux` 71/100 · `sveltejs/svelte` 88/100，⭐⭐⭐⭐⭐ 即「短期新建账号集中 fork 热门仓库」是 GitHub 的常态行为而非攻击信号**，⭐⭐⭐⭐⭐ **因此本日报据此**撤回**对 `google-research/paper-orchestra`（2,884⭐ · 403 forks · 仅 56 blobs / 8 个 commit / 0 CI / 0 release）的 100 个同日 fork 的任何「协调刷量」解读** —— ⭐⭐⭐⭐⭐ **判据必须从「绝对阈值」改为「相对对照」；⭐⭐⭐⭐⭐ 与之并列的第二个发现是**「版本发布」判据必须从一维拆成四维（tag 数 / release 数 / tag→commit→源码 diff 是否闭合 / 资产是否随版本演进）**，⭐⭐⭐⭐⭐ **本日实测四个真项目给出四种形态**：`alibaba/open-code-review` 100 release × 7 asset（366 MB，含 `sha256sum.txt`，**asset 下载 57–951 次**）· `getarcaneapp/arcane` 100 release × 41 asset（1.78 GB，deb/rpm/apk/zst + 14 个裸二进制，**无 SBOM**）· `backnotprop/plannotator` 100 release × 36 asset（2.57 GB，**含 CycloneDX SBOM JSON + 13 个 sha256**，下载仅 1–12 次）· ⭐⭐⭐⭐⭐ **`GoogleChrome/modern-web-guidance-src` 100 个 tag 但只有 1 个 release（prerelease 的审计数据 JSON），而其 10/10 抽样 tag 的 commit 全部真实改动 RAG 索引产物（`guide-chunk-cache.i8/.json/.scale.f32`）、其父 commit 10/10 触及源码** —— ⭐⭐⭐⭐⭐ **即 11-16 的「假版本号」（`steam-library-bridge`）、11-17 的「多而实」（`ffmpeg-skill`）与本日新增的「有 tag 无 release」是三种不同状态，⭐⭐⭐⭐⭐ 而判据恰恰在于「链上有没有真实 diff」而非「功能 commit 在前还是在后」**（本日 `open-code-review` 与 `plannotator` 各自实测到功能 commit 在 tag 与在父上交替出现）；⭐⭐⭐⭐⭐ **第三个发现是「SKILL.md 数量」是一个被复制放大的计数，必须拆成三个指标**：⭐⭐⭐⭐⭐ 实测 12 个 skill 类 Trending 项目，`affaan-m/ECC` 的 **1,087 个 SKILL.md 只对应 330 个独立技能身份（3.30×）**、最大单一技能被复制 **10 份**（1,029 个文件即 94.7% 是副本）· `Tencent/LoopForge` 21/9（2.33×）· `backnotprop/plannotator` 23/11（2.09×）· `cursor/plugins` 173/113（1.53×），⭐⭐⭐⭐⭐ **而 `Claude-BugHunter`（83/83）、`superpowers`（15/15）、`addyosmani/agent-skills`（25/25）、`anthropics/skills`（20/20）、`stitch-skills`（16/16）、`last30days-skill`（1/1）全部零复制**；⭐⭐⭐⭐⭐ **关键反例是 `obra/superpowers` 15 身份 / 5 套 harness 清单 / 复制 1.00×，⭐⭐⭐⭐⭐ 证明「零复制」与「多 harness」可以兼得 —— 因而 ECC 的 3.30× 是实现选择而非能力上限**；⭐⭐⭐⭐⭐ **第四个发现是安装协议仍在缓慢收敛且赛道在分化**：⭐⭐⭐⭐⭐ 对 11-17 同一批 17 个仓库同口径复测，**同时公开 `npx skills add` 与 `marketplace add` 的从 3/17 变为 4/17**（新增 `google-labs-code/stitch-skills`），⭐⭐⭐⭐⭐ **而 12 个 skill 类项目中 0 条安装命令的有 4 个、只有 1 条的有 4 个、两条全有的 4 个 —— 三足鼎立**，⭐⭐⭐⭐⭐ **最刺眼的是 `Tencent/LoopForge` 有 21 个技能文件却是 0 套 harness 目录、0 条安装命令**；⭐⭐⭐⭐⭐ **同日 `alibaba/open-code-review` 出现 `plugin-contract.yml` 与 `action-contract.yml` 两个把契约做成 CI 门禁的工作流 —— 即「让外部用户能装上」仍是最薄弱的一环，而「把契约变成可执行检查」本日首次出现**；⭐⭐⭐⭐⭐ **第五个发现是「确定性 + LLM」的混合架构在两个不同领域各自独立出现**：`alibaba/open-code-review` 是「确定性规则流水线（NPE/线程安全/XSS/SQL 注入）+ LLM Agent」，`google-research/paper-orchestra` 是 `autoraters/citation_f1.py`（确定性 F1）+ `agent_review.py`（LLM 评审），⭐⭐⭐⭐⭐ **两家机构、两个领域、同一分工 —— 共同点是把确定性的部分承担「可复现可回归」，LLM 的部分承担「无法规则化的判断」，而分工边界写在哪里决定了系统是否可测试**。

**证据边界：** 本日全部元数据取自 **2026-11-18 CST** 经 `gh` CLI 认证的 GitHub REST / Search API 快照，覆盖 `repos/*`、`git/trees/*?recursive=1`、`commits/{sha}`（含 files diff）、`tags`、`releases`（含 asset 元数据）、`readme`、`contributors`、`users/*`、`forks?sort=newest&per_page=100`、`issues?state=all&per_page=30`，以及 `github.com/trending?since=daily` 与 `?since=weekly` 的 HTML 快照（日榜 15 + 周榜 14，去重 25 个仓库）。⭐⭐⭐ **⚠️ 本日报未 clone、未安装、未运行任何被观测项目，未调用任何 LLM API，未下载任何 release asset，未访问任何被投放的载荷域名。** ⭐⭐⭐ **⚠️ fork 对照实验为「最新 100 个 fork」的有偏样本（老 fork 不可见），2,600 个样本的「账号 ≤7 天」基线会随时间波动，单日单次快照不能当作长期基线。** ⭐⭐⭐ **⚠️ tag→commit 链的检查为抽样**（`modern-web-guidance-src` 10 个 / `open-code-review` 3 个 / `plannotator` 3 个 / `ECC` 4 个），**「N/N 触及源码」是抽样结论，未外推**。 ⭐⭐⭐ **⚠️ skill 身份去重口径为「`SKILL.md` 父目录名 + blob sha 同一性」，若两个技能同名但内容不同会被计为两个身份。** ⭐⭐⭐ **⚠️ issue 仅读了标题、作者与正文长度**（`paper-orchestra` 30 条 / `LoopForge` 14 条 / `open-code-review` 14 条），未逐条读正文。 ⭐⭐⭐ **⚠️ star 增速未做统计**，所有 ⭐ 数为快照绝对值；出现的增量（如 ECC +66,998、last30days +877）都是两个快照点之差。 ⭐⭐⭐ **⚠️ `Tencent/LoopForge` 的 `license.spdx_id` = NOASSERTION**，未读取其 LICENSE 文件，**不主张其实际许可条款**。 ⭐⭐⭐ **⚠️ 本日的 `git pull --ff-only origin main` 在默认代理配置下持续失败**（`gnutls_handshake() failed`，重试并尝试 `http.sslCAInfo` 与 `http.version=HTTP/1.1` 均失败，绕过代理的直连亦超时），**经 `api.github.com` 核验 remote HEAD 与 local HEAD 均为 `e1141ff`（无待拉取更新）**，**最终提交通过 GitHub Git Data API 推送**。 ⭐⭐⭐ **⚠️ 未核验项**：ECC 的 npm 包与 GitHub App 分发物、`modern-web-guidance-src` 的 RAG 构建实现与 `.i8` 索引格式、paper-orchestra 的全部 Python 实现与数据集发布计划、plannotator 的应用技术栈与 SBOM 内容、arcane 的 server↔agent 通信协议与权限模型、LoopForge 的部署前置条件与 32 个 API 路由清单、`open-code-review` 的规则集实现与命中情况。

**关键项目：**
- 🌐 [GoogleChrome/modern-web-guidance-src](projects/modern-web-guidance-src.html) — **版本判据的第三类形态**：100 tag / 1 release（prerelease 审计数据）；10/10 抽样 tag 的 commit 改动 RAG int8 索引产物、父 commit 触及源码；Chrome/Edge/Firefox/MDN 联合治理
- ⚡ [affaan-m/ECC](projects/ecc.html) — **1,087 个 SKILL.md = 330 个独立身份（3.30×）**，最大单一技能复制 10 份；9 套 harness 目录 + 15 个 CI 工作流 + SLSA3 provenance；README 首段即「Official sources only」防御声明
- 🗂️ [backnotprop/plannotator](projects/plannotator.html) — **100 release × 36 asset，含 CycloneDX SBOM + 13 个 sha256**；`snapshots-sign-check.yml` 做签名校验；23 SKILL.md 去重后仅 11 身份；asset 下载仅 1–12 次
- 🔍 [alibaba/open-code-review](projects/alibaba-open-code-review.html) — **确定性规则 + LLM Agent 混合架构**；`plugin-contract.yml` / `action-contract.yml` 把契约做成 CI 门禁；100 release × 7 asset（含 sha256sum.txt），**下载 57–951 次为本组最高**
- 🎼 [google-research/paper-orchestra](projects/paper-orchestra.html) — **「账号判据必须有对照组」的首个实证样本**；56 blobs / 8 commit / 0 CI / 0 release；30 条 issue 全是具体失效报告；`autoraters/` = 确定性 F1 + LLM 评审
- 🐉 [getarcaneapp/arcane](projects/arcane.html) — **100 release × 41 asset（deb/rpm/apk/zst + 14 裸二进制）1.78 GB 但无 SBOM**；仅 9 个 open issue 且被显式限定为 Bug；Go / BSD-3-Clause
- 🔁 [Tencent/LoopForge](projects/loopforge.html) — **21 个 SKILL.md = 9 身份、0 套 harness 目录、0 条安装命令**（适配层最末端）；`license.spdx_id` = NOASSERTION；issue 全是带定位信息的开发者自测记录
- 🐛 [elementalsouls/Claude-BugHunter](projects/claude-bughunter.html) — **83 SKILL.md = 83 独立身份，复制 1.00×（零复制）**；技能平均 20,191 B；`evidence-hygiene` 被单列为一个技能
- 🔎 [mvanhorn/last30days-skill](projects/last30days-skill.html) — **1 个技能 = 1 个身份（复制 1.00）+ 4 套 harness 清单 + 50+ host**，单文件 31,980 B 为本日最高；同时公开两条安装命令

---

"""

for path, block, first_marker in (
    (ROOT / "indexes/trend-index.md", TREND_BLOCK, "## 2026-11-17"),
    (ROOT / "daily-report.md", REPORT_BLOCK, "## 2026-11-17"),
):
    src = path.read_text(encoding="utf-8")
    assert first_marker in src, f"{path} missing marker {first_marker}"
    assert "## 2026-11-18" not in src, f"{path} already has 11-18"
    path.write_text(block + src, encoding="utf-8")
    print(f"prepended 2026-11-18 -> {path} ({len(block)} chars)")
