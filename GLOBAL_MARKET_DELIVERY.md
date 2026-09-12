# v0.1.2 Global Market & Eligibility — accepted checkpoint

Current status: CAREER_INTELLIGENCE_V012_GLOBAL_MARKET_ACCEPTED

Human Review: ACCEPT（2026-09-13，当前用户直接确认）。接受现有框架与已记录 limitations；本次仅将已审阅增量完成本地 commit / annotated tag checkpoint，不 push、不启动下一阶段。Market Benchmark 不能作为 Candidate Evidence；real current JD / authority source 高于 taxonomy、一般职业描述及历史市场资料。China 与 UK 均 active；其他市场按具体机会校准；个人偏好不因市场切换而重写。

Commit message: `Accept Career Intelligence v0.1.2 Global Market`。Annotated tag: `career-intelligence-v0.1.2-global-market-accepted-20260913`。精确 commit 身份由该 tag 的目标确定并在提交后报告。

以下保留原 Human Review 交付快照；其中未提交／待审阅状态描述属于接受前的历史时点。

## Original Human Review delivery snapshot

Status: CAREER_INTELLIGENCE_V012_GLOBAL_MARKET_HUMAN_REVIEW_READY

2026-09-13。仅实现规则、共享 contract 增量、reviewed-input guards 与合成案例。Human 尚未接受本增量。基线保持 main / `02fcae7497c4012ec2cc0d7748463054e0dcfd6f`，accepted tag `career-intelligence-v0.1.1-job-quality-accepted-20260913` 未修改；本轮不 commit、不 tag、不 push。

## 可阅读结果与语义

[Global Market Human Review](tests/outputs/global-market-human-review.md) 展示六个合成岗位：中国本土、外企上海、中国公司伦敦 sponsorship VERIFY、新加坡 sponsorship AVAILABLE、英国 strong-fit 但 sponsorship UNAVAILABLE、澳大利亚 sponsorship VERIFY。每例都有独立市场／公司／地点、工作权、sponsorship、qualification 和下一步；包含 role hypothesis 的市场词汇变体、有限准备策略、跨币种与福利比较边界。

默认顺序为 Capability / Problem / Output → Role Hypothesis → Market / Location validation。China = ACTIVE / HIGH-ACTIVITY EXECUTION MARKET；UK = ACTIVE；其他市场 = OPEN / OPPORTUNITY-DRIVEN。物理位置、当前中国申请活动或未知签证不自动关闭英国；其他市场只在具体机会出现时校准。市场偏好／排除／临时执行优先级有独立来源和作用域，不改写能力。

Employment market、company type/nationality、work location、candidate authorization、employer sponsorship、qualification 分开。六个要求的工作权状态都有明确规则；need=SPONSORSHIP_REQUIRED 可与 resolution=SPONSORSHIP_AVAILABLE 并存。最终仍是 ELIGIBLE / VERIFY / NOT ELIGIBLE；具体 no-sponsor 岗位只有在候选人无适用工作权且无其他路线时失败，不传播为国家／角色家族排除或能力降级。

schema extension 有必要：原资格总状态不能表达上述独立事实，也不足以表达外部市场口径。本轮在既有 [contracts](schemas/contracts.md) 增加 market_context、work_right、可选 market_benchmark 和 comparison context；没有建立平行 schema 文件或全球数据库。Benchmark 保留 sourceRefs、日期、证据层级与限制，当前为空。Personal Preference 保持原值，与外部市场事实分开。

## Exact modified files — 10

- `SKILL.md` — 加入全局市场入口。
- `rules/eligibility.md` — 链接独立工作权／市场 gate。
- `rules/opportunity-assessment.md` — 中国城市顺序限定 China scope，海外不自动降级。
- `rules/job-quality.md` — 明确中国薪资／福利参考的市场作用域。
- `schemas/contracts.md` — 上述共享 contract 增量。
- `scripts/job_quality_guard.py` — RMB-only 限制改为三字母大写币种格式检查。
- `workflows/position.md` — 市场约束不删除能力。
- `workflows/discover.md` — responsibility-first、市场词汇变体与验证。
- `workflows/analyse-job.md` — 市场、公司、工作权、qualification 与质量独立。
- `workflows/prepare-application.md` — VERIFY 的 STRATEGY_ONLY 与岗位不可行时停止完整材料。

## Exact added files — 7

- `references/global-market-context.md` — 本次 DIRECT_USER / HUMAN_CONFIRMED 市场意图及来源哈希。
- `rules/global-market.md` — 全局机会、市场校准及四个 workflow 规则。
- `scripts/global_market_guard.py` — 纯输入校验与岗位限定决策 helper。
- `tests/fixtures/global-market-synthetic.json` — 六例合成输入，金额不是市场 benchmark。
- `tests/test_global_market.py` — 15 项 focused regression。
- `tests/outputs/global-market-human-review.md` — 独立中文 Human Review artifact。
- `GLOBAL_MARKET_DELIVERY.md` — 本交付报告。

## Exact unchanged files reused

规则／参考：`rules/source-and-inference.md`, `rules/evidence.md`, `rules/cv-claims.md`, `rules/stretch.md`, `rules/discovery.md`, `rules/user-questioning.md`, `references/job-quality-profile.md`, `SOURCES.md`, `reuse-matrix.md`。

执行边界：`scripts/guard.py`, `scripts/discovery_guard.py`, `scripts/stretch_guard.py`, `scripts/validate.py`。新增 helper 使用既有 `qualification` 和日期解析；没有替换 READY、source 或 claim-use gate。

原测试入口：`tests/test_core.py`, `tests/test_discovery.py`, `tests/acceptance_check.py`, `tests/test_stretch.py`, `tests/test_job_quality.py`。

原 fixtures：`tests/fixtures/A-tencent.json`, `tests/fixtures/B-kuaishou-user.json`, `tests/fixtures/C-baidu.json`, `tests/fixtures/D-kuaishou-commerce.json`, `tests/fixtures/E-stale-source.json`, `tests/fixtures/F-dneg-packet.json`, `tests/fixtures/evidence-excerpts.json`, `tests/fixtures/slice2-cases.json`, `tests/fixtures/job-quality-synthetic.json`, `tests/fixtures/source-manifest.json`。原 Human Review outputs 与历史交付文档保留。

## Final validation

| Check | Command / method | Result |
|---|---|---|
| Dependency-free validator | `python3 -I -S -B scripts/validate.py` | PASS；禁用 site packages，standard library only |
| Slice 1 | `python3 -B -m unittest discover -s tests -p test_core.py` | 33/33 PASS |
| Slice 2 | `python3 -B -m unittest discover -s tests -p test_discovery.py` | 19/19 PASS |
| Existing acceptance | `python3 -B tests/acceptance_check.py` | 7/7 PASS；Tencent 历史例仍保持 HOLD |
| Core / Stretch | `python3 -B -m unittest discover -s tests -p test_stretch.py` | 13/13 PASS |
| Job Quality | `python3 -B -m unittest discover -s tests -p test_job_quality.py` | 15/15 PASS |
| Global Market | `python3 -B -m unittest discover -s tests -p test_global_market.py` | 15/15 PASS |
| Protected sources | SHA-256：manifest 原始来源 7；本轮前后 source/CV/root documents 共 18 | 全部一致 |
| Whitespace / temporary files | tracked + untracked 文本检查；工作区及 ignored inventory | PASS；无临时／缓存文件 |
| Git boundary | HEAD/tag、cached diff、旧 fixtures/tests 比较 | accepted baseline 不变；index 空；仅上述 17 文件为本轮工作区增量 |

新测试 A–J 分别覆盖外企中国市场、UK VERIFY、UK 单岗失败、其他市场可 sponsor、其他市场未知、币种陷阱、福利制度差异、中国城市 scope、中国公司伦敦、能力不受签证失败影响。其余五项覆盖角色／市场／日期／来源错配、sponsor 与候选人路线条件分离、替代路线及已有权利、国际币种格式、候选人／其他路线 UNKNOWN 不被当成否定证据。

## Compatibility / review findings

发现并处理三处需要澄清的接缝：原 pay-basis helper 只接受 RMB，现只放宽币种格式，不声称 ISO 代码真实性或汇率／税后价值；原中国城市和待遇参考明确限定市场，保留已确认偏好；sponsorship VERIFY 的有限策略通过显式 STRATEGY_ONLY 承载，同时保持 PREPARATION_HOLD、空 approved claims 和无完整材料。没有把策略变成 READY，也没有改写既有 Core guard。

Artifact 采用六例对照和少量解释；UNKNOWN 集中到会影响决策的工作权与比较口径，没有自动生成大量询问。可 sponsor 不声称签证签发，强 fit 是合成前提而非新个人事实。未发现 evidence inflation。程序测试证明输入边界与分支行为；人工可读稿是本 agent 整理和语义复核，不是独立模型 benchmark。

## Remaining UNKNOWN / limitations

真实候选人的各市场工作权、期限和路线条件，具体雇主当前岗位 sponsor、真实 JD 资格与 freshness，以及 salary/tax/cost/benefit/leave/probation/relocation 数据均未在本轮验证。现有 Master Evidence／frozen CV 访问限制和事件级 trace 限制继续保留。

Guards 接受经人工审阅的结构化断言和来源引用，只核对绑定、显式状态及上下文完整性；不独立抓取或认证来源，不作法律裁定，不解析自然语言材料，也不计算金融结果。地域代码与币种格式不构成真实市场核验。完整自然语言 workflow 的独立模型表现仍未 benchmark。

未开展 live market research、扫描、Adapter、PAW integration 或投递；没有修改外部 Career records 或 CV source。停在 Human Review，下一步不自动开始。

`CAREER_INTELLIGENCE_V012_GLOBAL_MARKET_HUMAN_REVIEW_READY`
