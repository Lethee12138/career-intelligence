# v0.1.3 Market Calibration Reference Integration — Accepted checkpoint

Current status: CAREER_INTELLIGENCE_V013_MARKET_CALIBRATION_ACCEPTED

Human Review: ACCEPT WITH RECORDED VERIFICATION LIMITATION (direct Human instruction, 2026-09-13).

Recorded limitation: `PROTECTED_SOURCE_VERIFICATION_PARTIAL_DUE_TO_MISSING_HISTORICAL_PATHS`. Historical snapshot: 14 available files SHA-256 matched; 4 historical Downloads paths missing and unverifiable; no reconstruction or replacement. Required calibration imports are independently 4/4 byte-identical; Personal Preference hash unchanged. This accepted limitation is not a blocker and is not 18/18 PASS.

Local checkpoint commit message: `Accept Career Intelligence v0.1.3 Market Calibration`. Annotated tag: `career-intelligence-v0.1.3-market-calibration-accepted-20260913`. Exact commit identity is resolved by that tag and reported after creation. No push or next-stage work.

The following original delivery snapshot retains pre-acceptance state descriptions as historical provenance.

## Original delivery snapshot

Status: CAREER_INTELLIGENCE_V013_MARKET_CALIBRATION_HUMAN_REVIEW_READY

本轮接受的是外部研究的使用授权，不把来源升级为独立验证事实。四份原件已找到并逐字节导入；它们内部的历史待审阅标签保留，manifest 记录当前 Human 接受为 GLOBAL_JOB_QUALITY_MARKET_CALIBRATION_V01_ACCEPTED。基线仍为 main / `1c1a2e910903f24b926917d9aadc2468e21ee969`，既有 annotated tag 不变；未 commit / tag / push。

## Exact source import

来源均为 `/Users/luna/Downloads/` 下同名文件；目标为 `references/market-calibration-v01/`，SHA-256 在 [manifest](references/market-calibration-v01/manifest.json)。

- `Global_Job_Quality_Market_Calibration_v0.1.md`
- `Salary_Calibration_Matrix_v0.1.csv`
- `Benefits_Employment_Conditions_Matrix_v0.1.csv`
- `UK_Sponsorship_Work_Right_Verification_Guide_v0.1.md`

未省略任何原件内容。60 行薪资原始列完整保留；FULL 2、PARTIAL 58。原始 source ledger 包含不完整 URL／样本说明，未补造或修复。19 行福利原件保留，helper 提供 38 个独立市场 context；缺少逐行 confidence 和 trace audit 的地方标为 UNKNOWN_NOT_SUPPLIED / NOT_ASSESSED。

## Representation and use

三层为 durable method、dated reference data、volatile VERIFY-only facts。[校准规则](rules/market-calibration.md) 和 shared contract 承载方法；CSV 承载区间，工作流正文不复制 60 行。原件哈希 + 文件 + row locator 定位来源；last_verified 为空，不以 captured_date 冒充核验日期。

Freshness 没有统一 TTL。Salary/rent/recruiting context 需显式 cycle/age review（capture date、as-of、decision、reason）；无 review 为 RECHECK_REQUIRED，旧数据为 HISTORICAL_ONLY。结构方法按政策变化重审；volatile visa、sponsor、岗位和公司政策始终要求 ROLE_LEVEL_FRESH_VERIFY。法律原文数值只作为历史参考留存，未进入 helper 条件或阈值。

比较先保留当前岗位 actual fixed base 和 source，再匹配 market × city × route × responsibility-grounded family × currency basis。只比较 common interval，输出四种 directional label，绝不输出百分位或自动 Apply/Skip。FULL 只加强溯源，不赋予自动选择权；PARTIAL 明示方向性限制。Product Prototyping 的相邻数字原样保存但不用于精确 band 比较。AI title 不自动触发溢价。

UK 六个 gate 复用已有 work-right / qualification 框架，作为规则指导未来 fresh verification；未另造法律判定引擎。市场薪资可 normal 而某签证路线失败／VERIFY，候选人其他路径独立判断。Licence 不证明岗位 sponsor。

`/discover` 使用 contextual compensation，保留能力与假设；`/analyse-job` 当前岗位证据优先并显示日期／confidence／traceability；`/prepare-application` 携带必要质量疑问，不改事实简历、不绕过 HOLD、不自动谈薪。Personal Preference 文件完全未变；中国 10–15 天休假保留 ABOVE STATUTORY BASELINE / MARKET PREVALENCE VERIFY 的 dated 解读。

## Exact file changes

Modified — 5:

- `SKILL.md`
- `schemas/contracts.md`
- `workflows/discover.md`
- `workflows/analyse-job.md`
- `workflows/prepare-application.md`

Added — 11:

- 上述四份 `references/market-calibration-v01/` 原件
- `references/market-calibration-v01/manifest.json`
- `rules/market-calibration.md`
- `scripts/market_calibration_guard.py`
- `tests/test_market_calibration.py`
- `tests/outputs/market-calibration-trace.json`
- `tests/outputs/market-calibration-human-review.md`
- `MARKET_CALIBRATION_DELIVERY.md`

复用且未修改：既有 source/evidence、Job Quality、global-market、eligibility、stretch、CV claim 规则；原四个 guard 与 validator；全部原 tests、fixtures、已接受的 Human outputs 和 `references/job-quality-profile.md`。既有 `/position` 保持 market-agnostic，不需要增量。

## Validation and Human Review

[可读示例](tests/outputs/market-calibration-human-review.md) 与 [运行 trace](tests/outputs/market-calibration-trace.json) 包含七例：PARTIAL China、FULL London Product、FULL London Research、UK visa separation、高薪坏工况、稀疏 Product Prototyping、旧招聘周期。实际岗位均为 synthetic，外部研究为真实导入的 dated reference；没有暗示真实 Offer 或当前法定金额已核验。

| Check | Result |
|---|---|
| `python3 -I -S -B scripts/validate.py` | PASS — standard library only |
| Slice 1 | 33/33 PASS |
| Slice 2 | 19/19 PASS |
| Existing acceptance | 7/7 PASS |
| Core / Stretch | 13/13 PASS |
| Job Quality | 15/15 PASS |
| Global Market | 15/15 PASS |
| Market Calibration | 12/12 PASS |
| Original source manifest | 3/7 hash MATCH；4 个原始路径 MISSING，无法复核 |
| Protected source/CV snapshot | 14/18 hash MATCH；同上 4 个路径 MISSING |
| Personal Preference + four external inputs | 5/5 unchanged |
| Raw imports | 4/4 byte-identical |

测试命令：`python3 -B -m unittest discover -s tests -p test_<suite>.py`，suite 为 core、discovery、stretch、job_quality、global_market、market_calibration；acceptance 为 `python3 -B tests/acceptance_check.py`。新 A–H 分别覆盖 PARTIAL、FULL、签证隔离、高薪不抹风险、stale、实际待遇优先、年假、稀疏角色；额外验证导入哈希、freshness、scope/source/basis 错配、福利元数据未补造。

新增说明及代码通过 whitespace/conflict/temporary 检查；原件保留原始 Markdown 的双空格换行，不为格式清理改变其哈希。未发现 evidence inflation 或自动 selection。数据读取只验证结构化输入的约定和分支，不是独立法律／样本／模型验证。

## Intentionally inactive data and limitations

没有遗漏原件，但 captured visa money、going rates、Graduate rules、补贴、公司奖金和 hybrid 内容未转成执行常量。Product Prototyping 的相邻数字不用于 exact benchmark。原件的租金／法律／福利细节可按需阅读，未制成新的金融计算器或事实数据库。

58 个 PARTIAL 行、缺失样本集合、未知 sample n、稀疏 title、福利未审计 confidence 都继续可见。原始 source_refs 不保证 URL 完整或今天有效。Current official role evidence 的真实性与适用性需要未来 Human/agent 核验；helper 的 reviewed/as-of 是输入断言，不是认证。年龄／周期 review 依赖明确判断，不自动保证市场时效；没有 independent model benchmark。

未研究、抓取、刷新网页、安装依赖、创建监控或开始 Adapter、PAW、投递、谈薪。保持待 Human Review 的未提交增量。

`CAREER_INTELLIGENCE_V013_MARKET_CALIBRATION_HUMAN_REVIEW_READY`

Protected verification limitation: the following legacy paths are currently missing (no same-name match under Downloads, Luna or Documents):

- `/Users/luna/Downloads/职业规划_Canonical_Career_Plan_v1 (2).md`
- `/Users/luna/Downloads/Kuaishou_Baidu_2027_Qualification_Evidence_Ranking_2026-09-11.md`
- `/Users/luna/Downloads/职业定位与求职工具.txt`
- `/Users/luna/Downloads/China_September_Opportunity_Pool_Incremental_Scan_2026-09-10.md`

No external source write was performed. Missing legacy files were not recreated or assigned new hashes; full protected-source equality cannot be certified this run. All four required calibration input artifacts are accessible and byte-identical to imports.
