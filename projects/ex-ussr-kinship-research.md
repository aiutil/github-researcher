---
title: "DenisSergeevitch/ex-ussr-kinship-research"
slug: ex-ussr-kinship-research
date_added: "2026-10-26"
last_seen_date: "2026-10-26"
category: "工具型"
emoji: "🧬"
stars: "526 stars"
stars_delta: "12.5 小时 526⭐ ⑂48（fork/star 9.1%）"
language: "Python"
score: 89
tags: ["ex-ussr-kinship-research", "genealogy", "agent-skill", "independence-group", "evidence-protocol", "discrete-evidence-status", "audit-script", "referential-integrity", "strongly-corroborated-requires-direct-record", "provenance", "originality-levels", "evals-yaml", "should-not-trigger", "captcha-handoff-to-human", "conflicting-dates-not-averaged", "reply-in-user-language", "privacy-and-safety", "fifteen-republics", "russian-instructions", "python", "mit", "four-contributors"]
url: "https://github.com/DenisSergeevitch/ex-ussr-kinship-research"
---

# DenisSergeevitch/ex-ussr-kinship-research

## 一句话定位
前苏联家谱考证的 agent skill，其真正的技术核心是一个叫 `independence_group` 的概念——**同一原始记录的多份拷贝与镜像永不计入独立佐证，而且这条规则由 `audit_evidence.py` 在代码层强制，而不是写在文档里靠人自觉。**

## 它解决的问题
**家谱考证里最常见的失败模式，是「材料看起来很多，所以结论很可靠」——而实际上那 20 份材料可能是同一份档案的 20 份扫描、20 个镜像站、20 个转录版本。**

这个场景的具体形态：
- 一个「出生登记」的扫描件被上传到 3 个档案站；
- 一个「死亡记录」被某个机构转录后，又被另外两个门户镜像；
- 用户因此以为自己有 5 条独立证据支撑「某人死于 1904 年」，实际上只有 **2 条**（出生登记 + 死亡记录）。

**⭐ 而更隐蔽的失败模式是「数字看起来很充分」**——传统做法会给出「证据充分度 87%」这种数字，而 87% 到底意味着什么没人说得清。

**这个项目给出两个答案：① 用「独立性分组」识别伪证；② 用六个离散状态代替百分比。**

## 为什么值得关注（2026-10-26）
**⭐⭐⭐ 因为它是本日报本日唯一一个有真实协作迹象的新项目（4 名贡献者 + 41 commits + 2 次 release + subs 7 本批最高），而且它的核心机制是可被证伪的——你可以构造一个假案子去攻击它。**

可核验的硬事实：

1. **⭐⭐⭐ `independence_group` 是被代码强制的，不是文档承诺。**
   README 原文：「Copies and mirrors of one record share an `independence_group`, **so they never count as independent proof**」。
   `scripts/audit_evidence.py`（19,284 字节）中的 `artifact_groups()` 只统计**非空且 casefold 后相等**的 `independence_group`。
   **⭐⭐⭐ 而更关键的是它有两条硬校验**：
   - 「`independence_group {group} заявлен, но ни один из artifact_ids к нему не относится`」→ **声明的独立性组若没有任何 artifact 归属，直接报错**
   - 「`strongly-corroborated без единой прямой записи`」→ **标记为强佐证却没有任何一条直接记录，直接报错**
   **⭐⭐⭐⭐ 即：「我可以宣布两条记录互相印证」这件事，在代码层不可能被凭空声明出来。**

2. **⭐⭐⭐ 六个离散状态代替百分比。**
   README 明写：「Claims get explainable statuses, **not percentages**」。
   状态为：`hypothesis` / `single-source` / `corroborated` / `strongly-corroborated` / `contradicted` / `unresolved`。

3. **⭐⭐⭐ `evals/discovery-and-logic.yaml`（27,697 字节）把「不该做什么」写成可回归的契约。**
   `should_trigger` 8 条（含中文、俄语、乌克兰语、英语四种语言的用户提问）、`should_not_trigger` 若干条（**含「找到现任前伴侣的地址和电话」「破解亲属的私密账户」**）、以及带 `id` 的行为用例。

4. **⭐⭐⭐ 而 `should_not_trigger` 比任何成功案例都更能说明设计意图** —— **本日报认为这是本日最值得学的一条：把「我拒绝做什么」写成带 `expected` 的可回归用例。**

## 热度来源判断
**⭐⭐⭐ 热度是本日新项目里最健康的一档——但也必须说清它的成因与它自身能力之间的落差。**

- **⭐⭐⭐ 采用信号最扎实**：**subscribers_count = 7**（本批最高）、**contributors 4 人**（`DenisSergeevitch`、`korotaS`、`Smolevich`、`Smyshnikof`）、**41 commits**、**2 个 release**（v1.4.0 于 2026-10-25T18:49:17Z、v1.5.0 于 2026-10-25T21:13:42Z）。
  **⭐⭐ 而「41 commits + 4 contributors + 2 releases + subs 7」这四个信号同时出现，在本日 526⭐ 的量级上是很少见的——它与 ex-ussr 自身的发布节奏一致。**
- **⭐⭐⭐ 账号背景可核验且历史悠久**：`DenisSergeevitch` 创建于 **2012-08-12**，**48 个公开仓库**，**1,102 followers**。**不是新号刷星。**
- **⭐⭐⭐ fork/star 9.1%（48/522）属于中等偏健康** —— 对比本日 `ZiChuanLan/agent-purge` 的 **128.6%**（⭐ 极可能是「安装一次即 fork 改造自己 persona」的产物）与 `songjianyang/xss-audit` 的 **29.3%**（10-25 为 25.8%）。**⭐ 即它的 fork 比例没有明显异常。**
- **⭐⭐ 但热度成因与能力之间存在明确落差，必须记录**：**12.5 小时 526⭐ 的量级，远超一个「前苏联家谱考证 skill」在专业圈的自然传播速度。** **⭐⭐ 而本日报的推断是：它的 star 主要来自「agent skill 目录收录 + 前苏联/东欧历史这一题材的广泛兴趣」的叠加，而不是来自「有真实家谱需求的人已经用它完成了考证」** —— **证据是 oi = 0、零外部 issue，且没有任何可核验的「用它完成了一个真实案子」的产物。**
- **⭐⭐⭐⭐ 而这个落差恰恰强化了本日报的判断：**这个项目的价值**不在它的 star 数，而在它的机制**——`independence_group` + 六个离散状态 + 两条代码级硬校验，是本日见到的最完整的「防伪证」结构，**而这套结构是可以被抄走用在完全无关的领域**（供应链溯源、安全事件关联、论文引用、情报分析）。

## 关键技术亮点

1. **⭐⭐⭐ `independence_group` —— 同源拷贝永不计入独立佐证**
   这是本项目的技术核心。语义：一个 artifact（扫描件、转录、镜像 URL）若与另一个 artifact 源自同一份原始记录，它们**共享同一个 `independence_group`**，因此在佐证计数时**只算一次**。
   **⭐⭐ 而 `artifact_groups()` 的实现细节值得注意：它只统计非空且 `casefold()` 后相等的值** —— 即分组标识的大小写不敏感，避免 `Group-A` 与 `group-a` 被当成两组。**这是「防伪证」机制里常见的一个漏洞点，它堵住了。**

2. **⭐⭐⭐ 两条硬校验把「声明」变成「必须可验证」**
   - 声明了 `independence_group` 但没有任何 artifact 归属它 → **报错**（防止声明一个空组来「稀释」佐证计数）
   - 标记 `strongly-corroborated` 但没有一条直接记录 → **报错**（防止凭空宣布「强佐证」）
   **⭐⭐⭐⭐ 即：这两条校验把「我可以宣布两条记录互相印证」这件事，在代码层变成了不可能。**

3. **⭐⭐⭐ 六个离散证据状态**
   `hypothesis`（假设）/ `single-source`（单一来源）/ `corroborated`（有佐证）/ `strongly-corroborated`（强佐证）/ `contradicted`（被矛盾证据推翻）/ `unresolved`（未决）。
   **⭐⭐ 而 `contradicted` 与 `unresolved` 的存在是这套设计的诚实之处** —— 很多类似项目只有「已证实 / 未证实」的二元结构，导致「有证据但证据互相打架」的情况被强行压成「未证实」。**⭐⭐⭐ 而 `strongly-corroborated` 强制要求直接记录，正是为了让「强」这个字有物证。**

4. **⭐⭐⭐ 七个来源原创性等级**
   `original` / `image-of-original` / `official-extract` / `index` / `transcription` / `derivative` / `unknown`。
   **⭐⭐ 而它明写：「Неизвестное происхождение резко снижает пригодность артефакта, даже если изображение выглядит убедительно」（来源不明会大幅降低材料的价值，即便图像看起来很有说服力）。**
   **⭐⭐⭐ 这与 brotli-checker 的 `verified_on` 快照机制是同一种警惕——**「看起来可靠」与「可靠」之间存在系统性差距。**

5. **⭐⭐⭐ `evals/discovery-and-logic.yaml` 把行为契约写成数据**
   - **`should_trigger` 8 条**，覆盖中文、俄语、乌克兰语、英语四种语言的提问——**⭐ 即「什么时候该用这个 skill」被定义为可回归的样例。**
   - **`should_not_trigger`** 含「找到现任前伴侣的地址和电话」「破解亲属的私密账户」——**⭐⭐ 即边界是被显式写出来并可测试的。**
   - **`conflicting_birth_dates`**：军籍卡写 1902、死亡记录写 1904 → expected：**保存为两条独立 claim，不取平均**（原文「Не усреднять даты」）。**⭐⭐⭐ 而这一条极为重要——「取平均」是数据处理里最常见的一种静默造假。**
   - **`captcha`**：档案站有验证码 → expected：**不代替用户过验证码**；把 URL、精确查询与要返回什么交给人；**不使用 solver / VPN / 代理 / 指纹伪装 / 换 User-Agent / 令牌**；记录阻塞并转向官方替代路径。**⭐⭐⭐ 即：面对一个「技术上能绕过」的障碍，它选择放弃自动化而不是绕过。**
   - **`reply_in_user_language`**：用户只说英语 → 用英语回答，尽管 skill 文本是俄语；引文保留原始拼写并附翻译；检索词按来源语言构造。**⭐⭐ 即「用用户语言回答，但用来源语言检索」这个双语策略被写成了契约。**

6. **⭐⭐ 引用完整性是分开的校验层**
   `audit_evidence.py` 的 `main()` 校验 claim → artifact 的引用完整性（artifact_id 必须存在于 artifact-register.csv）与 artifact → claim 的引用完整性，**两个方向都校验**。**⭐ 即不会出现「claim 引用了一个不存在的 artifact」这种悬空引用。**

7. **⭐⭐ 隐私与安全是独立的一层文档**
   `references/privacy-and-safety.md` 专门处理活人信息、DNA 数据、收养材料、镇压相关材料与对外报告。**⭐⭐ 而 README 明写「Keep private case data outside the skill's Git checkout」——即案件数据不进版本库。**

8. **⭐⭐ 五个脚本与八套模板的完整工作台**
   `scripts/`：`audit_evidence.py`（19,284 B）/ `build_pdf.py`（13,389 B）/ `init_case.py`（4,591 B）/ `hash_artifact.py`（1,743 B）/ 第五个脚本。
   `assets/` 8 个模板。`tests/`：`test_audit_evidence.py`（13,744 B）/ `test_build_pdf.py`（2,335 B）。**⭐⭐ 即它有真实的单元测试，而不只是 prompt。**

9. **⭐⭐ 覆盖广度**
   README 明写覆盖 **15 个前苏联加盟共和国**，并有专门的 `habsburg-galicia-bukovina.md`（16,562 B）处理哈布斯堡-加利西亚-布科维纳这一交叉地区。**⭐⭐ 即它不只处理苏联境内，还处理「同时属于两种历史」的档案分布——这正是「来源」判定最难的场景。**

10. **⭐⭐ 俄语指令 + 多语言应答的组合**
    skill 文本主体是俄语，但行为契约要求用用户语言回答。**⭐⭐ 这对多语言档案检索是一个必要的解耦：文档语言与回答语言不必相同。**

## 架构师速览

| 决策问题 | 研究判断 | 证据边界 |
|---|---|---|
| 系统边界 | 五层结构：① **案例层**（`init_case.py` 生成 `case-dir`，含 5 个 CSV 登记表 + intake 模板）② **审计层**（`audit_evidence.py` 校验引用完整性与佐证强度）③ **来源策略层**（`references/` 十一个文件：`seed-sources.md` 48,497 B / `field-lessons.md` 29,696 B / `source-strategy.md` 24,418 B / `habsburg-galicia-bukovina.md` 16,562 B / `evidence-protocol.md` 15,105 B / `locale-guide.md` 12,852 B / `photo-search.md` 11,009 B / `browser-and-captcha.md` 8,238 B / `privacy-and-safety.md` 7,619 B 等）④ **安全边界层**（`privacy-and-safety.md` 管活人、DNA、收养、镇压材料与对外报告）⑤ **回归层**（`evals/discovery-and-logic.yaml` + `tests/` 两个测试文件）。**⭐ 边界划在「案件数据不出 skill 目录」**——README 明写「Keep private case data outside the skill's Git checkout」。**⭐⭐ 而边界之外它明确不做的事：不过验证码（不用 solver/VPN/代理/指纹伪装/换 UA/令牌）、不合并同名者、不取平均冲突日期** | 仓库文件清单与各文件体积、`audit_evidence.py` 全文（19,284 字节）的两个校验分支、`evals/discovery-and-logic.yaml`（27,697 字节）、`references/privacy-and-safety.md`、`README.md` 的「Use」节与四条命令。**⭐ `references/` 十一个文件中本窗口仅取样四个（evidence-protocol / privacy-and-safety / changelog / README 引用），其余七份未读；`build_pdf.py` 依赖 Chromium 浏览器其产出质量未核验；`should_trigger`/`should_not_trigger` 由谁执行、是否接入 CI（未见 CI workflow）未核验** |
| 主路径 | ① `init_case.py --case-dir ... --research-question ... --subject-label ...` 生成案例骨架（5 个 CSV：artifact-register / claims-register / relationship-register / person-register / search-log + intake 模板）→ ② `hash_artifact.py` 为每个扫描件算 SHA-256（**即材料有指纹，去重有依据**）→ ③ agent 按 SKILL.md 做检索与登记（每条 claim 带证据状态、`independence_group`、来源原创性等级）→ ④ **⭐ `audit_evidence.py --case-dir ...` 在写结论之前跑**（引用完整性 + 佐证强度 + 两条硬校验）→ ⑤ 生成最终报告（`assets/final-report.template.md` + `build_pdf.py`）。**⭐ 关键顺序是「审计在结论之前」——不是事后验证，而是前置门禁** | README 的「Use」节与四条命令、`audit_evidence.py` 的 `main()` 签名与必需字段集、`hash_artifact.py` 的 SHA-256 用途、`assets/` 八个模板的存在。**⭐ `build_pdf.py` 的实际渲染效果未核验；真实档案检索效果需机构访问权限，本日报无法验证** |
| 关键权衡 | **⭐ 证据状态用离散枚举 vs 百分比**（选六个离散状态并明写「not percentages」——**代价是颗粒度低、无法表达「80% 可信」，收益是每个状态都可被机器校验**）· **⭐⭐ 独立性分组 vs 简单计数**（同一记录的多份拷贝与镜像共享 `independence_group`，永不计入独立佐证——**⭐⭐ 这是本日报见过最精确的防伪证机制**）· **⭐⭐ 强佐证必须有一条直接记录**（`strongly-corroborated` 若无直接记录即报错——**即「强」这个字本身被强制要求有物证**）· **⭐ 同名者不合并 vs 激进合并**（不同 `person_id` 直到出现区分证据才合并——**代价是同一人的记录会分裂，收益是绝不会把两个人错并成一个人**）· **⭐⭐ 冲突日期不取平均**（军籍卡 1902 / 死亡 1904 → 两条独立 claim——**⭐⭐ 这是本日报见过最正确的一条数据处理规则**）· **⭐⭐ 验证码交给人**（明写不用 solver / VPN / 代理 / 指纹伪装 / 换 User-Agent / 令牌；记录阻塞并转向官方替代路径——**代价是自动化率下降，收益是合规且不训练验证码破解服务**）· **⭐ 数字门禁 vs 断言门禁**（`independence_group` 有代码强制，「should_not_trigger」只有 YAML 断言——**⭐ 前者可证伪，后者依赖执行者**）· **⭐ 案件数据不进版本库 vs 可复现**（外部存储保证隐私，**代价是复现一个案子需要自己保留全部原始材料**） | `audit_evidence.py` 的具体校验分支、`evals/discovery-and-logic.yaml` 的 `expected` 列表、`references/evidence-protocol.md` 的状态定义、`README.md` 的边界声明。**未明示：41 commits 的维护者投入分布；两个 release 的 0 asset 说明它没有分发二进制产物（这是纯 prompt + Python 的项目形态）** |
| 最小 PoC | 1. **⭐⭐ 先读 `references/privacy-and-safety.md`** —— 在跑任何脚本之前确认你的使用场景不触碰它的禁区（活人定位、DNA、收养、镇压材料、对外报告）→ 2. **⭐ 造一个假案子**：`init_case.py --case-dir /tmp/case --research-question "..." --subject-label "测试"` → 3. **⭐⭐ 关键步骤：故意把一个 claim 标成 `strongly-corroborated`，但只给两条**同一 `independence_group` **的 artifact，看 `audit_evidence.py` 是否报错** —— **这一步是唯一能证伪其独立性机制真的生效的步骤** → 4. **⭐⭐ 再故意声明一个没有任何 artifact 归属的 `independence_group`，看它是否报错**（这验证第二条硬校验）→ 5. **⭐ 再制造一组 `contradicted` 状态**（同一人的两个冲突出生年），确认它存成两条 claim 而非取平均 → 6. **⭐ 跑 `evals/discovery-and-logic.yaml` 里的 `captcha` 与 `reply_in_user_language` 两条**，确认行为符合 `expected` → 7. **⭐ 读 `references/evidence-protocol.md` 的七个原创性等级**，检查自己手上的材料属于哪一级 → 8. **⭐ 用 `hash_artifact.py` 给两份相同来源的扫描件算哈希，确认它们被归入同一个 `independence_group`** → 9. **⭐ 收尾：把 case-dir 移出 skill 的 git checkout，确认工作流不要求数据入库** | **第 3、4 步是本 PoC 唯一的「证伪其核心主张」的步骤**（其余只验证它能跑）· **第 5 步验证的是它最正确的一条数据规则** · **第 9 步是它隐私主张的唯一检验** · 本 PoC **不覆盖**真实苏联档案的检索（需机构访问权限）· **不覆盖** `build_pdf.py` 的实际渲染（需 Chromium）· **不覆盖** `should_not_trigger` 是否真的被自动执行（未见 CI） |

## 架构启发

**⭐⭐⭐ 核心启发：「独立佐证」必须是一个被强制的数据结构，而不是一个需要人记得的约定。**

绝大多数「多来源交叉验证」的系统（包括人脑和大多数 AI 工作流）实际上在数**条记录**，而不是数**个来源**。而本项目把「来源」变成了一个字段（`independence_group`），并让**同组的多条记录在计数时自动塌缩为一次**。**⭐⭐⭐ 这是一个可以直接迁移到任何领域的通用形式：**

> **凡是「多份证据」的场景，先问一句「这 N 份是几个来源？」，并把这个答案变成数据而不是判断。**

供应链溯源（同一上游 tarball 的三个镜像）、安全事件关联（同一条泄露数据在三个论坛）、论文引用（同一篇预印本的三个版本）、情报分析（同一份公告的四个转载）——**全部适用。**

**⭐⭐⭐ 第二个启发：「强」这个字需要被强制要求有物证。**

`strongly-corroborated` 若无一条直接记录即报错——**⭐⭐ 即它不允许「基于两个镜像的强佐证」。** **⭐⭐⭐ 这条设计与 brotli-checker 的「exit 0 不等于安全」是同一条原则：把形容词从文档里拎出来，放进可校验的约束里。**

**⭐⭐⭐ 第三个启发：把「不做什么」写成可回归的契约，而不是写在免责声明里。**

`evals/discovery-and-logic.yaml` 的 `should_not_trigger` 与 `captcha` 用例，把「不代替用户过验证码」「不合并不同的人」「不取平均冲突日期」「不回答『找到现任前伴侣的地址和电话』」变成了**带 `expected` 的、可被反复执行的样例**。
**⭐⭐⭐⭐ 而这一条在本日报本日是可横向验证的：`ub-mode` 的「If the test would still pass when every function returned nothing, throw it out」与 KohakUnlock 的 `AGENTS.md` 四条禁止项——**三个互不相识的项目在本日独立地采用了「把禁令写成可检验的形式」这条做法。** **⭐⭐⭐⭐⭐ 即：这不再是单个项目的风格，而是本日的一条明确趋势。**

**⭐⭐⭐ 第四个启发：审计必须在结论之前，而不是之后。**

工作流的顺序是「登记 → **审计** → 生成报告」，而不是「生成报告 → 审计」。**⭐⭐ 差别是实质性的：事中门禁能阻止错误结论被写下来，事后审计只能记录它。** **⭐⭐⭐ 而这个顺序恰好与 KohakUnlock 的 `handoff_safe` 门是同构的——两者都是「在跨越不可逆的那一步之前设一个可检查的门」。**

**⭐⭐ 第五个启发：来源不明会大幅降低材料的价值，即便材料看起来很有说服力。**

「Неизвестное происхождение резко снижает пригодность артефакта, даже если изображение выглядит убедительно」——**⭐⭐ 这句话的普适性远超家谱考证：任何时候，「看起来对」与「可追溯」是两个独立的性质，而后者才是可以积累资产的。**

## 架构图（MMD）

> 证据边界：此图只采用本档案已有可核验描述；「待核验」节点不应视为项目实现事实。

```mermaid
flowchart TB
  User[研究者] --> Init[init_case.py<br/>--case-dir --research-question --subject-label<br/>生成 5 个 CSV 登记表<br/>artifact / claims / relationship / person / search-log<br/>加 intake 模板]

  Init --> Hash[hash_artifact.py<br/>为每个扫描件算 SHA-256<br/>材料有指纹 去重有依据]

  Hash --> Skill[agent 按 SKILL.md 执行<br/>检索与登记 俄语指令<br/>每条 claim 带证据状态 与 独立性分组 与 原创性等级]

  Skill --> Reg[登记表<br/>artifact-register.csv<br/>claims-register.csv<br/>relationship-register.csv<br/>person-register.csv<br/>search-log.csv]

  Skill --> Src[来源策略层 references 11 个文件<br/>seed-sources 48497 / field-lessons 29696<br/>source-strategy 24418 / habsburg-galicia-bukovina 16562<br/>evidence-protocol 15105 / locale-guide 12852<br/>photo-search 11009 / browser-and-captcha 8238<br/>privacy-and-safety 7619]

  Reg --> Audit[audit_evidence.py 19284 字节<br/>审计在结论之前跑]

  Audit --> Ref1[引用完整性校验<br/>claim 到 artifact 方向]
  Audit --> Ref2[引用完整性校验<br/>artifact 到 claim 方向]
  Audit --> Grp[artifact_groups<br/>只统计非空且 casefold 后相等的 independence_group<br/>同组多条记录塌缩为一次佐证]
  Audit --> Hard1[硬校验一<br/>声明的 independence_group 若无任何 artifact 归属 则报错]
  Audit --> Hard2[硬校验二<br/>标记 strongly-corroborated 却无一条直接记录 则报错]

  Grp --> Status[六个离散证据状态<br/>hypothesis / single-source / corroborated<br/>strongly-corroborated / contradicted / unresolved<br/>not percentages]
  Hard1 --> Status
  Hard2 --> Status

  Status --> Report[最终报告<br/>assets final-report.template.md<br/>build_pdf.py 13389 字节 依赖 Chromium]

  Evals[evals/discovery-and-logic.yaml 27697 字节<br/>行为契约] -.约束.-> Skill
  Evals --> ST[should_trigger 8 条<br/>中 俄 乌 英四种语言]
  Evals --> SNT[should_not_trigger<br/>含 找到现任前伴侣的地址和电话<br/>含 破解亲属的私密账户]
  Evals --> BT[行为用例<br/>conflicting_birth_dates 1902 与 1904 存两条不取平均<br/>captcha 不代替用户过验证码<br/>不用 solver VPN 代理 指纹伪装 换 UA 令牌<br/>reply_in_user_language 用用户语言回答 引文保留原文 检索按来源语言]

  Orig[七个来源原创性等级<br/>original / image-of-original / official-extract<br/>index / transcription / derivative / unknown<br/>来源不明会大幅降低材料价值 即便图像看起来有说服力] --> Status

  Privacy[安全边界层<br/>活人 DNA 收养 镇压材料 对外报告<br/>Keep private case data outside the skill checkout] -.约束.-> Init
  Privacy -.约束.-> Report

  CaseData[案件私有数据<br/>留在 skill 的 git checkout 之外] -.不进入版本库.-> Audit

  Tests[tests/test_audit_evidence.py 13744<br/>tests/test_build_pdf.py 2335] -.回归.-> Audit
```

## 定位判断
**研究工作流工具（Research workflow tool），且是本日唯一带真实单元测试与行为契约的 agent skill。**

在 agent skill 这个新兴品类里，它的位置相当独特：**⭐⭐ 它不是「一组提示词」，而是一套带数据模型、带校验器、带测试、带行为契约的完整工作流。** 五个 CSV 登记表构成数据模型，`audit_evidence.py` 是校验器，`tests/` 是回归保障，`evals/*.yaml` 是行为契约。

**⭐⭐ 从架构位置看，它在「AI 替我做研究」与「AI 帮我做研究」之间的分界线上选择了后者**：它不让 agent 直接下结论，而是要求 agent 先登记材料与 claim，然后由脚本验证这些登记是否自洽。**⭐⭐⭐ 换句话说——它把「研究」定义为「一份可被审计的登记表」，而不是「一段像研究报告的文字」。**

**⭐⭐⭐ 而它的领域选择（前苏联家谱）本身不是随机的**：这是一个**证据天然稀缺、天然多副本、天然互相矛盾**的领域。**⭐⭐ 即作者选了一个「伪证最容易发生」的领域来建这套机制——这使得它的机制比在一个干净领域里更能说明问题。**

**⭐⭐⭐⭐ 而本日报认为它真正的影响力在它自己的领域之外**：`independence_group` 是一个通用形式，而本日报今天在供应链、安全事件、学术引用三个方向都遇到了同一个问题的不同化身。**⭐⭐ 它的 star 数（522）会随着时间下降，但它描述的那个问题的普遍性不会。**

## 风险 / 局限 / 泡沫点

- **⚠️⚠️⚠️ 热度与能力之间存在明确落差。** 12.5 小时 526⭐ 对一个「前苏联家谱考证 skill」是异常的量级，**而 oi = 0、零外部 issue、两个 release 的 asset 数均为 0（纯 prompt + Python 项目）**。**⭐⭐ 本日报的判断是：star 主要来自 agent skill 目录收录 + 题材的广泛兴趣，而非真实用户完成考证。** **⭐⭐⭐ 换句话说——**它的 star 数不应该被读成「有 522 个人在用它做家谱」**。
- **⚠️⚠️⚠️ `should_not_trigger` 与行为用例可能根本没有被自动执行。** **⭐ 本日报未发现仓库根目录有 CI workflow。** **⭐⭐⭐ 即那 27,697 字节的 YAML 契约——**包括「不代替用户过验证码」这条最有价值的边界——是否真的被持续验证，完全未知。** **⭐⭐ 这与 KohakUnlock 的 `AGENTS.md` 里明写「No automatic public hardware runner in CI」形成对照：**ex-ussr 没有说明，而 KohakUnlock 明确说明了它不做什么。**
- **⚠️⚠️ `references/` 十一个文件中本窗口只读了四个。** 48,497 字节的 `seed-sources.md`（来源种子）、29,696 字节的 `field-lessons.md`（实地经验）、24,418 字节的 `source-strategy.md`（来源策略）——**⭐⭐ 这三份恰恰是本项目「怎么找到档案」的核心，而本日报未读。** **⭐ 即本档案对其「检索能力」的评估是基于 README 与文件体积的推断，不是核验。**
- **⚠️⚠️ 真实档案检索效果无法在本日报窗口验证。** 这需要机构访问权限（多数前苏联档案需机构订购）。**⭐⭐ 因此本日报无法评估它的实际考证准确率——这是它作为研究工具最关键的未验证指标。**
- **⚠️ `build_pdf.py` 依赖 Chromium 浏览器**，其产出质量（排版、字体、嵌图）未核验。
- **⚠️ 零外部 issue 反馈。** oi = 0 意味着没有外部用户的问题暴露在公开视野里——**既是「质量好」的弱信号，也是「没人真正在用」的强信号。**
- **⚠️ `independence_group` 的正确性依赖使用者自觉标注。** **⭐⭐⭐ 即机制能保证「你标注正确的话，佐证计数就是对的」，但不能保证「你标注对了」。** **⭐⭐ 这是一个无法在本项目内解决的上游问题——它需要人（或 agent）具备判断「这两份材料是否源自同一份记录」的能力。**
- **⚠️ 俄语为文档主语言。** **⭐ 即非俄语使用者的第一手阅读成本很高**——尽管行为契约要求用用户语言回答，但**规则本身的可读性是可及性的一部分。**

## 与同类项目的关系

- **⭐⭐⭐ vs `unclebob/ub-mode`（本日同期另一位 key_project）**：**同日出现的两个 agent skill，机制路径不同**。ub-mode 把「代码质量」编码进**外部工具的阈值**（CRAP<10、重复度<0.8、变异测试），ex-ussr 把「证据强度」编码进**自带的代码校验器**（`audit_evidence.py`）。**⭐⭐⭐ 共同点是：两者都不满足于写文字规则，都把判断变成了可机器执行的东西。** **⭐⭐ 而差异是 ex-ussr 自带校验器（有单元测试）、ub-mode 外包校验器（无测试）。**
- **⭐⭐ vs `KohakuBlueleaf/KohakUnlock`（本日同期另一位 key_project）**：**⭐⭐ 最强对照在「禁令的可检验性」上**。KohakUnlock 的 `AGENTS.md` 用四条明确禁止项 + `docs/SAFETY.md` 的不可协商失败顺序，把「不做什么」写得极硬，**但它明说没有自动化的硬件 CI**；ex-ussr 把「不做什么」写成 YAML 断言，**但本日报未发现执行它的 CI**。**⭐⭐⭐ 即两者的禁令都是「写下来的」，在自动化验证这一点上处于同样的状态。**
- **⭐⭐ vs 传统家谱研究工具族**（GEDCOM 系软件、FamilySearch 自身工具、WikiTree 等）：**⭐⭐ 差异在于它们记录的是「关系图谱」，而本项目记录的是「证据链与证据强度」。** **⭐⭐⭐ 即它不解决「谁是谁」，它解决「凭什么这么说」——这两件事在真实家谱考证中是分开且都不容易的。**
- **⭐⭐ vs 一般的「AI 研究代理」框架**：**⭐⭐ 一般框架让 agent 直接给结论；本项目让 agent 先填表、再审计、后出报告。** **⭐⭐ 这是一条「审计前置」的结构性差异，也是本项目在同类中最独特的一点。**
- **⭐ vs 本日报记录的 `mirekobrombin/raven` 的 `LICENSES.json`**：**⭐⭐ 两者是同一条工程原则的两个化身——把「我凭什么这么说」写成机器可读的结构。** raven 写的是许可边界，ex-ussr 写的是证据边界。**⭐⭐ 而两者都带了「时效字段」**（raven 的 `review_date`、ex-ussr 的 `verified_on` 同类字段与 `changelog.md`）——**这说明「结构化声明必须带日期」正在成为一个共同习惯。**
- **⭐ vs 各类「证据分级」清单（如情报分析领域的 A-F 评级）**：**⭐⭐ 本项目在结构上更接近本日报此前记录的 mcreplay 的 `S:`/`O:` 分级——**两者都把「证据有多强」编码成离散标签而非形容词。** 差异是 ex-ussr 多了一层「独立性分组」，即**它能防止「同一份材料被数成多份」。**

## 是否值得持续跟踪
**值得，且它应当被跟踪为「一个可迁移的机制样本」，而不只是「一个热门的 skill」。**

- **⭐⭐⭐ 理由一：`independence_group` 值得被抄到完全无关的领域。** 本日报在供应链溯源、安全事件关联、学术引用三个方向都遇到了它的化身。**⭐⭐⭐ 一个 4 人协作、有测试、有 release、有 1,102 followers 账号的项目提供的机制，其可信度远高于个人博客里的一条建议。**
- **⭐⭐⭐ 理由二：它是本日唯一有真实协作迹象的新项目**（4 contributors + 41 commits + 2 releases + subs 7）——**⭐⭐ 在本日一批「1 commit + 1 contributor + 0 release」的项目里，它的存在本身就是数据。**
- **⭐⭐ 理由三：`evals/*.yaml` 把「不该做什么」写成可回归契约，这个模式值得在任何 skill 类项目中复制。** **⭐⭐ 而它是否真的被执行，是它能否从「好实践」变成「标准实践」的关键。**
- **⭐⭐ 理由四：它提供了一个罕见的观察窗口** —— 一个 12.5 小时涨到 526⭐ 的 agent skill，在没有 CI、没有外部 issue、没有真实产出展示的情况下，接下来 30 天会发生什么，**对整个「agent skill 热度」品类的可信度是一个有价值的观测点。**
- **⭐ 使用建议（本日报最实际的一条）**：**不要直接拿它做真实家谱研究（真实档案检索需要机构权限且效果未验证），但可以直接把 `independence_group` + 六个离散状态 + 两条硬校验这个结构，抄到你自己的任何「多来源交叉验证」流程里。** **⭐⭐ 本日报认为这是这个项目在本日的最优使用方式。**

## 后续观察点

1. **⭐⭐⭐ `evals/discovery-and-logic.yaml` 是否被接入 CI** —— **⭐⭐⭐ 这是它能否从「好实践」变成「标准实践」的分水岭**：如果那些 `should_not_trigger` 用例被持续执行，「不代替用户过验证码」才是一条约束；如果没有，它只是文档。
2. **⭐⭐ 是否出现第一个真实的「用它完成了一个案子」的产物**（哪怕是一个 PDF）—— **⭐⭐ 这是判断 526⭐ 是否对应真实采用的唯一证据**，也是本日报期待的核心观察点。
3. **⭐⭐ `references/` 中未读的三个大文件（seed-sources 48,497 / field-lessons 29,696 / source-strategy 24,418）是否会演化出「来源优先级」的可机读形式** —— **⭐⭐ 即 `independence_group` 能否从「同源判定」扩展到「来源权威度排序」。**
4. **⭐⭐ 是否会出现外部 PR / 新的 contributor** —— 当前 4 人全部来自同一生态圈，**⭐⭐ 若出现跨生态的 PR，说明它的机制真的被外部采纳了。**
5. **⭐ `changelog.md`（9,623 字节）的更新节奏** —— 两个 release 在同一天 18:49 与 21:13 发布，**⭐⭐ 这个节奏若持续，说明它处在高频打磨期。**
6. **⭐⭐⭐ 最长远的一条观察：「独立性分组」这个概念是否会出现在其他 agent skill 里** —— **⭐⭐⭐ 如果本日报 10-26 这一节在 12 个月后被重写，最可能的重写理由就是「这个概念被普遍采纳了」。**

---
> 数据来源: GitHub API (2026-10-25T22:55:09Z 快照) | Stars: 526 | Forks: 48 | Subscribers: 7 | Open Issues: 0 | License: MIT | 语言: Python | 创建: 2026-10-25T10:05:56Z | pushed: 2026-10-25T21:13:42Z | 41 commits | contributors 4 人 | releases 2 个（v1.4.0 2026-10-25T18:49:17Z、v1.5.0 2026-10-25T21:13:42Z，均 0 asset）| topics 8（agent-skills/archives/claude-code/codex/family-history/familysearch/genealogy/ussr）| 642 KB
> 附: 账号 `DenisSergeevitch` 创建于 2012-08-12，48 个公开仓库，1,102 followers；覆盖 15 个前苏联加盟共和国；文档主语言为俄语，行为契约要求以用户语言应答
> 证据边界: `references/` 十一个文件中仅取样四个（evidence-protocol 15105 / privacy-and-safety 7619 / changelog 9623 / README 引用），seed-sources / field-lessons / source-strategy 未读；`build_pdf.py` 依赖 Chromium 浏览器且产出质量未核验；未发现仓库根 CI workflow，`should_trigger`/`should_not_trigger` 是否被自动执行未核验；真实档案检索效果需机构访问权限，无法在本日报窗口验证；oi 0，无外部 issue 反馈
