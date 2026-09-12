# 全球机会开放，具体岗位逐项核验｜v0.1.2 Human Review

**同一个 workflow／AI product 能力假设，可以同时探索中国、英国及其他市场。** 中国仍是高活跃执行市场；英国仍是 active，不因当前中国申请较多、人在别处或工作权未确认而自动降为次要市场。其他市场在出现具体有价值机会时再校准，不预先研究或永久关闭整个国家。

本稿只演示框架。下列公司、岗位、候选人工作权、雇主 sponsorship 和资格证据均为 **SYNTHETIC**，不是本人真实签证状态或真实招聘信息。输入为 [合成 fixture](../fixtures/global-market-synthetic.json)，每个 `SYN:<role_key>` 引用定位到其中对应 case，版本截至 2026-09-13；真实市场 benchmark 未填入。个人市场意图来自 [Human-confirmed context](../../references/global-market-context.md)，不是对就业市场可行性的调查结论。本次没有实时研究、法律核验、登录或投递。

## 从一个能力假设开始

假设：“把复杂任务转成工作流、原型和验证机制”的产品潜力。它的 evidence／INFERRED／POTENTIAL 状态由 accepted Core 决定，本稿不重评个人能力。可考虑 Product Discovery、Workflow Product、Applied AI Product／Human-AI Experience 等责任方向；PM 不是唯一答案。

| 搜索表达（词汇建议，未搜索） | 市场验证发生在哪一步 |
|---|---|
| 中国：产品发现、工作流产品、AI 产品、内部工具、原型验证 | 实际 JD 的职责、批次、资格、城市分配与本地 Job Quality |
| 英国：Product Discovery、Associate Product Manager、Workflow Product、Human-AI Experience | 先保持责任假设，再核对具体岗位工作权、是否 sponsor、programme 条件与地点要求 |
| 其他市场：Product Prototyping、Product Operations、AI Product Experience、Internal Tools | 针对具体国家／城市与岗位补充 authorization、sponsorship、收入／福利／成本；不凭术语推断需求或在招 |

能力 → 责任假设 → 市场可能性是默认顺序。候选人可主动排除市场或改变临时执行优先级，但这些选择不改写能力身份。

## 六个合成岗位

以下均假设 Capability Fit、Job Quality 和 Career Value 较强，以隔离 eligibility 的影响。“其他资格通过”也仅是合成记录中的输入断言，不是对真实候选人的判断。source_scope 为各 `SYN` case；结论是基于该输入的 INFERENCE／REASONABLE INFERENCE。

| Case | Employment market / work location | Company type | 独立 work-right / sponsorship | 具体岗位资格与下一步 |
|---|---|---|---|---|
| CN-domestic | China / Hangzhou | Chinese domestic | 合成记录确认已有适用工作权；sponsorship 未确认但无需依赖 | ALREADY_AUTHORISED；其余模拟资格通过 → ELIGIBLE。正常进入 Core 的岗位状态、质量和材料检查 |
| CN-mnc | China / Shanghai | foreign multinational | 合成记录确认已有适用工作权；不因外企身份推定 sponsor | ALREADY_AUTHORISED → ELIGIBLE。仍是中国就业市场，不自动享有“海外工资／国际福利／西式文化” |
| UK-verify | UK / London | Chinese multinational | candidate need=SPONSORSHIP_REQUIRED；雇主是否提供未知 | resolution=SPONSORSHIP_VERIFY，qualification=VERIFY。保留 UK／该责任假设，允许 STRATEGY_ONLY，工作权核验保持开放 |
| SG-available | Singapore / Singapore | startup | 合成岗位权威记录确认 OFFERS；候选人适用 route conditions 也在模拟输入中确认 | SPONSORSHIP_AVAILABLE；其他模拟资格通过 → ELIGIBLE。正常 opportunity assessment，可讨论高优先级；不自动降低，也不声称 visa 已签发 |
| UK-unavailable | UK / London | multinational | 合成岗位权威来源明确 DOES_NOT；候选人无现有适用权利，其他路径也在输入中确认不可用 | SPONSORSHIP_UNAVAILABLE → NOT ELIGIBLE，仅限这个 Job Record；停止 full materials，保留 capability 和 UK active 状态 |
| AU-verify | Australia / Melbourne | mid-size | candidate need=SPONSORSHIP_REQUIRED；雇主政策未知 | SPONSORSHIP_VERIFY → VERIFY，不 PASS、不 FAIL。价值值得时可做有限策略，先验证该岗位的路径 |

这里 company nationality 和 employment market 没有互相替代：外企上海岗是 China；中国公司的伦敦岗是 UK。实体、办公地点和跨境雇佣安排若不清楚，应保持 jurisdiction VERIFY，不能仅凭城市或总部猜法律适用。

## 英国 VERIFY 时如何继续，而不是提前关门

UK-verify 可以保留如下 bounded preparation strategy：围绕产品判断与原型验证选择最小项目组合，列出最重要的职责匹配及 gap，并把“是否对本岗位／programme 提供 sponsorship、候选人 route 是否符合、时间与地点限制”列为下一步核验。

`Qualification / Work-right verification remains open`；现有准备 gate 仍为 PREPARATION_HOLD，strategy_scope=STRATEGY_ONLY。没有批准 CV claim、完整申请材料、已有 visa 或雇主支持的断言。它不是一张泛化求职大礼包，也不是把缺签证误写成能力不足。

如果来源只是“公司以前 sponsor 过”或“公司在 sponsor 名单”，仍不能把这个岗位变成 SPONSORSHIP_AVAILABLE。如果明确不 sponsor，但有可能的其他合法路径尚未验证，则为 OTHER_ROUTE_VERIFY；只有工作权需要、雇主限制和无替代路径都确定时，才得到上表的岗位特定 NOT ELIGIBLE。已有适用工作权时，则不应被“该雇主不 sponsor”误拒。

## 海外的摩擦真实存在，但不是地理惩罚

SG-available 的优先级按 fit、job quality、career value 和 practical costs 正常判断。还需关注 relocation、开始时间、雇主条件、材料投入和签证费用／时间的不确定性。强价值和可信路径可以值得投入；普通价值却要承担大量不确定成本的机会，也可能不值得深做。必须解释具体成本／回报，不能只写“海外所以 Low Priority”。

UK-unavailable 的负面结论不传播：未删除工作流能力、未降低 Capability Profile、未封锁 AI 产品家族，也未把 UK 状态改为 inactive。仍可看同市场其他 sponsor 岗位或其他市场可行路径。

## 钱和福利：不能只换汇

合成金额 `RMB 15,000/month` 与 `GBP 35,000/year` 都不是本次市场 benchmark。不能比原始数字，也不能仅将年／月和汇率换算后宣布哪份 offer 更好。

| 需要的比较 context | 当前状态 |
|---|---|
| gross/net、保证／浮动、发薪周期 | 周期已给出；gross/net 和完整薪酬结构 UNKNOWN |
| 适用税费、本地生活与房租 | UNKNOWN／MARKET_VERIFY，不计算虚假的税后生活余量 |
| 工时、实际可休假期、福利可用性 | UNKNOWN，不能由市场或品牌推定 |
| China housing fund vs UK pension | 分别属于各自市场制度背景；缴纳、金额、资格、可取得性和当地待遇含义 UNKNOWN，不能按福利名称视为等值 |
| relocation、visa 成本／时间／雇主约束 | 具体岗位条件尚需证据，不隐去这些 friction |

可选 Market Benchmark contract 已能记录 market/country、region/city、role family、career stage／graduate status、招聘年、币种、薪资口径／区间、总待遇、成本、福利、work-right／sponsor context、sourceRefs、captured/verified date、evidence level 和 limitations。本次值为空，`MARKET_VERIFY`；没有建立国家数据库。

稳定个人偏好仍包括正常休息、避免长期高压、清晰支持与成长自主、钱重要但不无限弥补生活损害、interesting work、ownership、career mobility 和 hybrid 正向。中国的薪资直觉／公积金优先级不能机械搬到英国；英国 pension 或其他国家福利需要当地 context。市场“常见”也不等于本人必须接受。

中国城市偏好只在 China scope 内应用，未把杭州与伦敦、新加坡放进同一个默认城市排名。可以以后由 Human 明确新增跨市场偏好，但本轮未替本人做这个选择。

## Human Review 结论范围

全球机会保持开放，中国执行没有被削弱，英国保持明确 active 的框架位置；岗位可行性由真实适用的资格和工作权证据判断。五项重点分离保持：Capability Fit ≠ Eligibility ≠ Job Quality；company type ≠ employment market；Personal Preference ≠ Market Benchmark。

本 agent 实际运行六个 `authorization_review`／`strategy_scope` 检查并完成本稿语义审阅；测试覆盖错误 job/market/date 引用、未知 sponsor、候选人 route 条件、货币陷阱和 capability 隔离。程序只验证明确输入与结构边界，不独立验证签证法律、来源真实性或 sponsor 意愿。所有真实市场数字、候选人工作权、雇主 sponsor 和新市场待遇仍待具体机会出现后校准。

`HUMAN_REVIEW_REQUIRED`
