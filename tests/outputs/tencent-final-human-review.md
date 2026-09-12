# 腾讯 AI 产品经理｜Slice 1 双工作流审阅稿

**建议：保留一个腾讯 targeted 方向，先核验，再决定是否进入材料准备。** 工作流证据值得继续看；当前输入不足以确认今天的岗位状态，也不能证明 Agent/RAG 工程能力或商业产品数据经验。

本次结果：`Explore → PREPARATION_HOLD → HUMAN_REVIEW_REQUIRED`。

这是以既有脱敏 fixture 为输入的一次 `/analyse-job → /prepare-application` 执行。后一步已实际检查前一步结果，返回 HOLD；没有伪造 OPEN 条件来演示成功路径。下面仍提供本次明确要求的条件式 CV／项目方向，供判断是否值得继续，不生成可采用的简历主张。

## 1. 输入与来源

运行日期：2026-09-12。模式：`HISTORICAL_SNAPSHOT`；输入截至 2026-09-11。分析编号 `TENCENT-SLICE1-REVIEW-01`，本文件同时承载分析及其后续 preparation 结果。

| 引用 | 实际读取内容 | 可以支持什么 |
|---|---|---|
| [A：腾讯 fixture](../fixtures/A-tencent.json) | 岗位身份、历史资格结论、两条规范化需求、场景假设 | 已有记录及本次分析范围；不能替代当前官网 |
| [E：脱敏证据片段](../fixtures/evidence-excerpts.json) | `dneg-workflow`、`dneg-testing`、`dneg-ownership` | 工作流原型、测试迭代汇总、人／AI／团队边界 |
| [来源索引](../../SOURCES.md) | TENCENT、SCAN、BATCH、OUTPUT 的位置和版本信息 | 追溯历史来源；本次没有重新读取招聘网页或 Master Evidence 原件 |
| [CV 路由规则](../../rules/cv-claims.md) | 既有 CN-P/Product 路由及使用边界 | 可以推荐 Base 名称；不能确认具体源文件及版本 |

阅读约定：**FACT** 指 fixture 留存的历史记录事实；**EXTERNAL_REPORT** 指对职位或项目的来源转述；**INFERENCE** 是本次判断；**UNKNOWN** 是未取得的事实。原报告曾引用官方来源，不等于本次直接核验了权威页面。具体原始 JD 与项目事实的当前权威等级仍未核定。

## 2. /analyse-job：岗位事实与资格

| 字段 | 本次可读结论 | 来源等级与时间边界 |
|---|---|---|
| 公司／职位 | 腾讯｜2027 AI Product Manager | A，EXTERNAL_REPORT |
| 岗位身份 | `Tencent:1283126456553382912:2027` | A，历史记录身份；不是标题相似匹配 |
| 招聘类型 | 2027 campus 招聘入口的历史记录 | A 与其来源索引；未作当前校招资格复核 |
| 官方／发现来源 | A 引用 TENCENT routing 与 SCAN；当前原始权威快照未载入 | 报告级溯源已知，当前 AUTHORITY SOURCE 核验缺失 |
| 地点、发布日期、截止日 | UNKNOWN；本 fixture 未给出这些字段 | 不从别的岗位或旧印象补齐 |
| 当前开放状态、当前核验日期 | UNKNOWN；截至日为 2026-09-11，不冒充 last verified | 当前状态判定为 VERIFY |
| 精确 BG／产品团队 HC | UNKNOWN | 产品／场景存在不能证明该入口有对应 HC |

**资格结论分两层保留。** A 明确留存了用户确认的历史 `ELIGIBLE` 及既有 Full Evidence Match PASS，因此本次不推翻该历史结论。当前逐项资格是 `VERIFY`：fixture 未带当前原始资格条款、候选人各项资格依据或毕业窗口检查表，不能重新推出今天的 ELIGIBLE。

能力匹配不替代资格；反过来，历史资格通过也不证明技术、数据或业务能力通过。本次没有把学历当作职业边界，也没有假设某专业为硬门槛。

## 3. 需求层级与证据匹配

两条 `MUST` 来自 A 已有的规范化需求，不声称是本次逐字摘录的官方硬资格。精确 JD 措辞及层级仍待核验。fixture 没有提供 STRONG PREFERENCE 或 NICE TO HAVE 条目，因此不补造。

| 需求 ID／层级 | 证据 → 匹配 | 支撑范围与不能推导的部分 |
|---|---|---|
| `workflow`／MUST | E `dneg-workflow` → **SUPPORTED** | Human-AI 原型工作流；有 Anchor、Compare、Feedback、Human Decision、History。仅限原型层，不证明商业上线、产品规模或独立工程实现 |
| `product-data`／MUST | E `dneg-testing` → **PARTIAL** | 定性原型测试和迭代；不能推导 SQL、A/B、留存／漏斗分析或商业产品指标 ownership |

E 的数据边界：**3 轮正式测试、9+ 修改是报告中的汇总口径**，不是参与者人数或商业收益；逐条测试→问题→修改的原始事件记录未包含在 fixture 中。个人、团队及 AI 的分工以 `dneg-ownership` 为边界：AI 辅助实现，个人原型／测试／迭代贡献与共享研究分开。

**实际工作解释 — INFERENCE，依据 A 的两条需求和场景条目：**值得讨论的是把 Human-AI 工作过程变成可理解的流程、人工决策点和验证方案。Agent／知识工作／生产力应用层是合理的场景假设。岗位是否实际负责这些产出、归哪个团队，仍需该岗位的权威信息绑定。不能由“AI 产品经理”推导候选人具有 Agent 架构、RAG 实现、模型工程或平台开发专长。

## 4. 多维判断

以下为本次基于 A／E 的分析判断，不是分数或自动 Apply 决定。

| 维度 | 判断 | 对决策的意义 |
|---|---|---|
| Capability Fit | MIXED | 工作流与原型判断有支撑；数据和技术深度未建立 |
| Evidence Fit | MIXED | 两条需求有可定位的报告级片段，原始事实链尚未补齐 |
| Experience Fit | MIXED | 有项目原型／测试，不等于商业 PM 生命周期或指标责任 |
| Eligibility Fit | 历史 ELIGIBLE；当前 VERIFY | 保留旧结论，当前准备前需复核适用条件 |
| Practical Fit | UNKNOWN | 缺地点及实际分配信息；不靠城市猜团队 |
| Career Value | 值得 Explore | 场景可能验证 Human-AI 产品路线；是推断，取决于实际职责 |
| Interest / Preference Fit | UNKNOWN | fixture 未给出足够的个人兴趣／具体团队偏好 |
| Work-style Preference Fit | UNKNOWN | 日常销售／收入责任未明；正常协作不自动扣分 |
| Interview Process Risk | UNKNOWN | 不编造群面、Case 或即兴展示安排；如后续确认，也单独评估 |
| Stretch Level | MODERATE（暂定） | 从原型判断走向真实产品仍有数据、经验和技术表达缺口；完整 JD 可能改变判断 |

**主要缺口。** Evidence：原始事实卡、具体决策／测试记录及材料使用权限。Capability／Experience：现有片段不支持商业分析、Agent/RAG 技术专长或生产交付责任。Timing／Eligibility：当前状态、截止及资格条款待核。Wording：表达需保留人／AI／团队分工，不能把“AI 辅助原型”写成工程师经历。没有证据证明的 Domain／Preference 信息继续留空，不为了凑齐类别制造负面结论。

**建议：Explore。** 保留此前的一份 Tencent-targeted 方向，但当前不进入实质 tailoring。足以继续的理由是工作流与测试判断有直接项目支撑；阻止进一步投入的是当前岗位及原始主张链缺失。若权威信息确认实际工作是应用层 Human-AI 产品，且资格可用，再决定是否推进；若主要是模型／基础设施／数据平台工程，或核心销售收入责任，则需重新评估。产品场景存在本身不改变 HC 结论。

## 5. /prepare-application：门槛结果与条件式 brief

前一步的同一岗位身份、两条匹配结果和未决信息已传入准备检查。**结果为 `PREPARATION_HOLD`**：缺少当前同岗位权威观察，当前资格及公司申请约束未完成核验，原始证据／CV Base 引用未齐。检查没有把未知的公司约束假定为“无限制”。

下面是供本轮 Human Review 的准备方向；它不表示门槛通过，也不授权采用材料。

| 项目 | 最小建议 |
|---|---|
| Why this role | 若实际职责符合场景假设，DNEG 的工作流、人工决策和测试迭代可以支撑讨论；理由来自工作内容，不是“腾讯＋AI”标签 |
| 推荐 CV Base | **既有 CN-P / Product Base**；精确文件／版本 UNKNOWN。核对后再使用，不新建 Base |
| 项目路由 | **DNEG 作为这一 fixture 范围内的主证据**：workflow → testing → ownership。其他项目未在此输入中形成足够的腾讯证据链，不自动前置 PAW 或增添第二、第三项目 |
| 材料数量 | **一份 Tencent-targeted 策略**。以后可调整面试中的场景表达，不派生多个猜测 BG 的 CV |
| Portfolio | 仅在已有可用且获准分享的引用确认后考虑；当前没有可批准的链接。不要求新 demo、新项目或改作品集 |
| 本次主张／Packet | 不生成可采用的 CV claim；不生成额外 Vibe-Coded Packet、求职信或完整面试包 |

**可能的 recruiter concerns — INFERENCE，不是已发生的面试反馈：**

| 可能追问 | 诚实准备边界 |
|---|---|
| 原型里你、团队和 AI 各做了什么？ | 以 E `dneg-ownership` 回到具体决策与实现边界；不要用“独立实现”掩盖 AI 或团队贡献 |
| 测试如何改变产品，效果有多大？ | 可沿工作流→测试→修改准备一个故事；具体事件需回原件。3 轮／9+ 仅作待核汇总，不讲商业效率或增长效果 |
| 你是否真正做过 Agent/RAG 或产品数据分析？ | 当前片段不足以证明。工作流能力可以说明；技术专长与 SQL/A-B/漏斗经历不能从它外推 |

这些是面试准备方向，本轮没有向用户追加问题。缺少的官网和原件应先从既有来源核对，不启动泛化职业访谈。

## 6. 下一步核验清单与 Human decision

| 顺序 | VERIFY 项 | 完成后改变什么 |
|---|---|---|
| 1 | 同一 Post ID／batch 的当前原始 JD、开放状态、资格与截止 | 判断是否仍值得投入；资格不能由能力替代 |
| 2 | 实际职责、地点分配、BG／团队／HC 关系及公司申请约束 | 决定场景、地点和申请可行性；不能用产品存在填 HC |
| 3 | DNEG 原始事实／测试记录、ownership 和 resume/public-use 权限 | 决定哪些事实可进入主张链，哪些只能保留缺口 |
| 4 | 既有 CN-P Base 的精确源文件及版本 | 决定未来针对性编辑应基于哪份材料 |

**当前足够支持的 Human decision：是否保留这一个方向，并允许下一次先完成上述核验。** 本稿不支持直接确认申请材料或提交。没有修改 Career records、CV source 或任何外部账号。

## 执行溯源

两份输入未修改，SHA-256：

- A-tencent.json：`d901664b9dbe3caec8812a75fc94ae2c6c2f967484a9c9d837e26427bd27bbd4`
- evidence-excerpts.json：`5fd26e0999dbe5a7152d6ad3865d84791cbcdafe7d8352bcd23c6b4b6b8d1af4`

本 agent 按两个 Markdown workflows 完成语义分析和本审阅稿；[acceptance_check.py](../acceptance_check.py) 实际执行现有 guard：两条 evidence match 均无结构错误，当前 qualification 为 VERIFY，source status 为 VERIFY，preparation 为 HOLD。脚本不以 fixture 的 `expected` 字段作决策输入，也没有把机器检查包装成独立模型验证。

`HUMAN_REVIEW_REQUIRED`
