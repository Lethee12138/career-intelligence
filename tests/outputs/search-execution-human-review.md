# 从角色假设到求职执行｜v0.2 Human Review

**本稿演示可移交、可接回、可解释路由的执行链。没有进行真实岗位搜索。** 所有公司、岗位、URL、薪资／资格／sponsor 条件和候选人证据均为 SYNTHETIC。`example.invalid` 是刻意不可用的演示地址；不能用于真实申请。日期为模拟的 2026-09-13。

[原始批次及证据](../fixtures/search-execution.json) 保留全部 12 条输入；[完整执行 trace](search-execution-trace.json) 包含 discovery、生成的 handoff、去重结果、Application Pool proposal、两条完整 JobAnalysis／ApplicationBrief。

## 搜索策略：先找工作内容

合成输入证明的是一个 review-checkpoint prototype，不是 Agent/RAG 工程经验。由此提出三个 potential hypothesis：产品／工作流产品，产品运营／系统改进，以及 AI Evaluation／HITL Experience Ops。B 路径有明确合成产出；未提供 seed 和足够重复行为，A/C/D 的缺失被记录，没有凑出隐藏能力。

| 搜索轴 | 例子 | 为什么存在 |
|---|---|---|
| Title | Workflow Product / Product Operations / AI Evaluation | 发现职位词汇，不认定这些角色等价 |
| Responsibility | prototype review flow / improve internal workflow / design human review checkpoints | 找真实 ownership 和工作对象 |
| Problem | unclear human decision boundaries | 找需要这类能力的团队 |
| Output | reviewable prototype and test findings | 对照可交付成果而非头衔 |
| Trap | quota-carrying presales | 提醒检查实际职责，不单靠负关键词删除岗位 |

生成 handoff 对 China、UK、Other 都保留查询集合。China 高活跃、UK active；其他市场机会驱动。正式搜索可按当前职责补中文或当地词汇；本例词汇用于结构验证，不声称搜索效果。可支持全部七个 core families，Creative Tech／Game Systems 按证据选择，本例只覆盖三个。

建议返回约 30 个 useful raw candidates，可按质量减少；不是凑数任务。优先官方 careers/ATS，再公共就业渠道、平台、社区；每条都需区分 discovery 和 authority。重复过多、职责不再扩展、官方来源不可得或已有足够候选时停止。缺少 UK 非标题查询会触发 EXPAND_ACTIVE_MARKET_QUERIES。

外部 executor 收到的是最小查询上下文与现有 pool 身份摘要，不含完整候选人证据。可使用 CHATGPT_WORK、WEB_RESEARCH、MANUAL_IMPORT 或其他 executor；Core 不包含平台 API。

## 原始批次 → 去重 → 路由

| 原始结果／岗位 | 核验与去重 | 路由 | 一个下一步 |
|---|---|---|---|
| 深圳 Workflow Steward：官方 + 平台两条 | 同一 scoped ATS ID，合并为一身份；两份 provenance 保留 | TARGETED_PREPARE / ACTIVE | RUN_ANALYSE_JOB |
| 杭州 Product Operations | 合成当前 authority 与 qualification 通过，value 合理、成本低 | FAST_APPLY / REVIEW | FAST_APPLICATION_REVIEW |
| 英国 London role | 官方岗位模拟开放，sponsor UNKNOWN，工作权仍 VERIFY | WATCH_VERIFY | VERIFY_SPONSORSHIP |
| 新加坡 HITL role | 模拟岗位支持 sponsorship 且候选人 route 条件通过；不是签证签发 | TARGETED_PREPARE / ACTIVE | RUN_ANALYSE_JOB |
| 平台仍显示开放的 closed role | 合成官方 CLOSED 优先 | SKIP / CLOSED | SKIP |
| Strong fit，长期加班 | 职责 fit 保留；真实岗位式合成质量观察导致 LOW Job Quality | WATCH_VERIFY | VERIFY_JOB_QUALITY |
| AI Product title，实际 presales quota | 支持 mismatch 的 duties 来源保留 | SKIP | SKIP |
| 已在 pool 中 Applied | exact identity 对上旧条目，不新建 active 工作 | WATCH_VERIFY / EXISTING_POOL | HOLD |
| 同公司 Workflow Steward，上海另一 BG | 不同官方 ID、城市／BG，保留为独立候选 | TARGETED_PREPARE / ACTIVE | RUN_ANALYSE_JOB |
| 南京岗位，PARTIAL dated salary 偏低 | calibration 只是 context；不能单独 Skip | FAST_APPLY / REVIEW | FAST_APPLICATION_REVIEW |
| 社区弱结果 | 身份、JD 和 authority 信息不足 | DISCOVERED / WATCH_VERIFY | REVIEW_ROLE |

12 条输入得到 11 个候选；3 个 Targeted、2 个 Fast、4 个 Watch（包括 existing pool）、2 个 Skip。Company/application status 没有被 routing 改成 Applied。Application Pool 是供审阅的 artifact，不是新 tracker。

这个故意偏重中国案例的测试批次用于覆盖 city/BG、工资和平台冲突分支，**不是合理全球搜索配额或真实结果分布**。正式 handoff 要求报告市场覆盖；不能因为中国更易搜而跳过英国。新加坡按机会价值正常进入 Targeted，没有 overseas penalty。深圳高价值角色进入 Targeted，杭州较普通角色走 Fast，城市不覆盖 Career Value。

WIP 正常例为可调整的 4；已有 Targeted 活跃数达到 4 的反事实测试中，新高价值岗位保持 TARGETED_CANDIDATE / QUEUED，下一步 HOLD。不会为了新结果自动清空或替换原 pool。公司 slot FULL／VERIFY 同样阻止新 active work。

## 完整 Targeted 链：深圳 Workflow Steward

链条：SYN-E1 → C1 → H1 → SYN-SEARCH-01 → raw-sz／raw-sz-linkedin → 去重 Candidate → TARGETED → JobAnalysis → ApplicationBrief。每一层在 trace 中有 id/reference；分析和 brief 的 role_key 完全一致。

岗位事实来自合成官方 snapshot：职责是制作可审阅流程、检查用户工作流；qualification 为模拟通过。标题陌生，但职责更贴近已给出的 prototype 证据。十个 assessment dimensions 分开保留，Job Quality 常规细节 UNKNOWN，没有假装全部优秀。

| Requirement | Evidence match | 保留边界 |
|---|---|---|
| MUST：reviewable workflow prototypes | SUPPORTED → SYN-E1 | 只支持合成 review-checkpoint prototype |
| Preferred：production model evaluation | PARTIAL / DEFENSIBLE_STRETCH → SYN-E1、C1 | 评估思路可迁移；production AI、Agent/RAG、商业效果未证明 |

推荐 High Priority Apply 是**合成控制分支**；理由是具体职责支持和高价值，不是标题或城市。准备包含完整 requirement/evidence review、小项目路由、招聘方疑虑“能否迁移到 production evaluation？”及诚实回答边界。只提供一条有 fact-chain 的合成 claim，无商业数字或部署扩张。

模拟 gate 为 READY_FOR_REVIEW，**不授权真实材料采用**。现有真实 CV Base／版本仍 UNKNOWN，本例未创建 CV；公开 portfolio 权限也未授予。去掉模拟 current-source 标记后，原 Core gate 正确返回 PREPARATION_HOLD。

## 完整 Fast 链：杭州 Product Operations

相同 source、qualification、evidence 和 Human Review 标准，但不为普通、低申请成本角色增加深度公司研究。SYN-E1 → H2 → Search → Candidate → FAST → JobAnalysis → ApplicationBrief 的 lineage 保留。

角色工作内容与 review/workflow 原型有合理交集；Career Value 为 reasonable，不因杭州偏好变为最高优先级。仍逐项匹配上述两条要求，preferred 生产评估 gap 保持 PARTIAL；未省略 qualification 或 claim 检查。

Brief 只要求复核资格和两条匹配、在确认已有 base 与权限后使用一份现有模板。不自动生成 cover letter、整套 interview pack 或完整材料包。READY_FOR_REVIEW 同样仅为合成控制结果；FAST_APPLY 标签不提交、不联系 recruiter。

## Human UX 与真实执行边界

只对 11 个候选中的 2 个进行完整分析，其他停在足够路由的 screen。英国下一步只核 sponsor；坏工况下一步核质量；未知常规福利不制造一长串阻塞问题。没有 match percentage、总分或自动 salary 筛选。

可把 handoff 模板交给真实 Work/search executor，再将返回批次导入；本次尚未验证真实 executor 的搜索质量、字段完整性或 authority 判断。`reviewed`、`LIVE` 等标记要求 agent 实际查验，不能从返回字符串自动相信。真实 CV／source access 限制与已接受的四个历史缺失路径继续保留。

`CAREER_INTELLIGENCE_V02_JOB_SEARCH_EXECUTION_HUMAN_REVIEW_READY`
