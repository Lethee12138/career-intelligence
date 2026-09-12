# 腾讯 AI 产品经理｜Core Integration 职业策略审阅稿

**这条路线值得保留：以“把模糊问题转成可验证的 Human-AI 工作流与产品原型”为主张，争取应用层 AI／数字产品机会。** 不需要先拥有 PM 职称才能讨论产品潜力。DNEG 可作主项目，Circular Flow 用于证明这不是一次偶然的工具使用；若具体职责偏人机控制，再选 C the Signs 或 AI Survival 中最相关的一项。

本次职业定位不是“熟练使用 Codex”，而是**研究与问题重构 → 产品规则／流程 → 可运行原型 → 测试解释与迭代判断**。这比工具清单更能说明可迁移价值。商业数据分析、Agent/RAG 实现及生产工程责任仍是明确缺口，不能靠包装补齐。

执行模式为 historical / frozen role fixture。四阶段顺序：`C-CORE-01 /position → D-CORE-01 /discover → A-TENCENT-CORE-01 /analyse-job → P-TENCENT-CORE-01 /prepare-application`，统一版本为本次 `2026-09-12` integration review。**结果为 Explore + PREPARATION_HOLD；本稿中的措辞属于 NOT_FOR_ADOPTION 内部审阅，不是 canonical CV 或可直接提交的材料。** 这个门槛针对当前岗位与材料核验，不是否定候选人的产品潜力。

## 输入、身份和来源

优先检查了快手用户产品经理 fixture：其 `role_key=UNKNOWN`，缺精确 requisition URL/ID，因此选择有固定身份的腾讯 fallback。腾讯身份始终为 `Tencent:1283126456553382912:2027`；冻结岗位输入截至 `2026-09-11`，本次没有联网更新岗位。

| 引用 | 本次输入或读取位置 | 来源性质与本次范围 |
|---|---|---|
| A | [腾讯 accepted fixture](../fixtures/A-tencent.json)，role_key、历史资格、requirements | 历史记录；两条规范化需求，不冒充完整原始 JD |
| B | [快手 accepted fixture](../fixtures/B-kuaishou-user.json)，identity_boundary | 用于选择 fallback，不拼接进腾讯资格或申请约束 |
| E | [accepted evidence excerpts](../fixtures/evidence-excerpts.json)，dneg-workflow / testing / ownership / runtime | 保留原 evidence ID；报告级项目证据，不升级为亲验个人成果 |
| X | [Slice 2 completed cases](../fixtures/slice2-cases.json)，五个项目的逐项定位 | OUTPUT 报告的脱敏衍生，用于重复行为与角色发现；不修改旧 fixture |
| OUTPUT | `/Users/luna/Downloads/Prototype_Output_First_Role_Discovery_2026-09-09.md`，§2 DNEG ownership／AI／实际产出 | 本次重读该段，明确个人原型、测试、迭代与共享研究边界；仍是报告来源 |
| BATCH | `/Users/luna/Downloads/Kuaishou_Baidu_2027_Qualification_Evidence_Ranking_2026-09-11.md`，User Product／Usability 行 | 本次重读定位行；3 轮正式测试、9+ 修改是报告汇总，不是效果或人数 |
| DNEG_IMPLEMENTATION | `/Users/luna/dmi/workflow/CREATIVE_DRIFT_CHECKPOINT_PROJECT_NOTE.md`，AI Integration Boundary | 本次直接读取该文档：写明 simulated default、有限 optional AI support；没有运行程序或核验实时 provider |

完整源文件路径、版本哈希沿用 [source manifest](../fixtures/source-manifest.json)；本次输入文件 SHA-256、逐阶段 ID、结构检查和五条反向链见 [trace record](core-integration-trace.json)。报告源的作者归属按 ASSISTANT_REPORT／EXTERNAL_REPORT 保留，项目个人事实的原始 Master Evidence 深度仍有限。来源摘录的 observed_at 是本次读取日，不是岗位或个人能力的 last_verified_at。

阅读约定：项目内容为 EXTERNAL_REPORT／source_level=UNKNOWN；本次能力与迁移判断为 INFERENCE／REASONABLE INFERENCE。唯一列为 VERIFIED_FACT 的 F-documentary 是“所读文档明确写了什么”，验证范围不包括当前运行行为、个人作者或真实 AI 产品部署。这里不制造 DEMONSTRATED 能力以满足表格。

## Stage 1 — /position：把价值从工具提升到产品判断

输入 C-CORE-01：E、X 中已完成项目。排除 active PAW、Portfolio Studio；AR 只用历史已完成研究及低／中保真贡献，不取团队高保真为个人能力。已有正式 profile 和 frozen CV 精确版本未取得，因此任务内候选不宣称新增事实或完成正式去重。

| Profile 项／状态 | 行为依据与可用的专业语言 | 独立 use boundary 与未证明部分 |
|---|---|---|
| C-pattern：流程／产品规则思考，INFERRED，MODERATE | dneg-ownership、dneg-workflow；X Circular Flow 的规则与服务决策，AI Survival 的状态／反馈。重复的是解释问题并作系统和体验选择，不是重复使用同一工具 | 向 workflow product／AI product 迁移为 DEFENSIBLE_STRETCH（S-AI）；未证明商业 PM 全生命周期、后台架构或独立拥有整个项目 |
| C-stretch：定性测试到迭代判断，INFERRED，MODERATE | dneg-testing；X Circular Flow 测试驱动改动、AI Survival 试玩迭代。候选人解释观察并选改动，AI 实现支持另列 | 产品评估／验证潜力为 DEFENSIBLE_STRETCH（S-evaluation）；不包含 SQL、实验统计或量化商业效果 |
| P-AI：应用层 AI 产品／Human-AI 工作流潜力，POTENTIAL，TENTATIVE | 源能力 C-pattern 加 DNEG 的 Human Decision 边界，迁移目标是人的任务、控制与反馈设计 | DEFENSIBLE_STRETCH；不是 VERIFIED_FACT，也不是 Agent/RAG 工程能力 |
| P-evaluation：产品验证及评估潜力，POTENTIAL，TENTATIVE | C-stretch → 定义要观察的问题、组织验证、解释反馈 | DEFENSIBLE_STRETCH；没有模型 benchmark 或量化实验所有权 |
| C-gap：商业分析／SQL／A-B 的证据覆盖缺口 | dneg-testing 仅覆盖定性测试。当前检索范围没有该技术／商业经历的支持 | 对这类经历的事实包装为 SPECULATIVE_UNSUPPORTED；不等于候选人永远学不会或做不到 |
| C-unknown：CV 来源版本及材料使用权限 | dneg-workflow resume/public-use=UNKNOWN；exact frozen CV 未载入 | VERIFY，不是能力负面结论；不授予任何使用许可 |
| C-record：实现说明的技术边界 | dneg-runtime → 直接读取 DNEG_IMPLEMENTATION | F-documentary / VERIFIED_FACT 仅验证“文档说明 simulated default”；这属于 profile 的来源边界，不是候选人能力评级 |

DEMONSTRATED 能力列表为空：本次没有强行把二手项目记录提升成直接核验。SELF_IDENTIFIED 也未凭报告语言生成。已有 INFERRED 模式仍足以正向提出 adjacent potential，不需要先补任职头衔。

Seed Product Manager 的支持是问题重构、工作流、原型和测试迭代；反证／缺口是商业指标、真实上线经营、资源优先级及算法团队协作 ownership 未建立。候选人选择 PM 的明确动机仍 UNKNOWN，不推定其喜欢管理或商业经营。可能误区是把“能做原型”与“已经拥有商业 PM 全责”混同。没有把 PM 设为唯一或自动第一结论。

## Stage 2 — /discover：从产出扩宽责任方向

D-CORE-01 只消费 C-CORE-01 的已标记能力／潜力，不重新发明证据。Route A 对 PM 做双向检查；Route C 从 INFERRED 源模式生成潜力目标，未将 POTENTIAL 改标来进入 C；Route D 从重复的流程、控制、理解与反馈问题找 owning teams。Route B 缺直接自述／直接核验能力输入，保持不适用。

以下同级假设按职责组织，不是排序推荐。入池依据是明确 transfer bridge；查到符合标题的岗位也不等于职责已验证。

| Hypothesis／route | 实际产出、桥梁与行业团队 | 搜索策略：核心／邻近；职责／问题／产出；负词 | 反证及市场验证需求 |
|---|---|---|---|
| H-discovery：Research-led Product Discovery，A/C/D | C-pattern → 问题定义、服务规则、原型验证；消费服务、企业 SaaS、公共服务数字化 | 产品发现、体验产品／服务设计；研究综合、需求定义／采用摩擦／旅程、PoC；注意纯研究专家或视觉 craft 门槛 | 若 JD 核心为独立大型研究或商业路线图，需要额外证据；UNVALIDATED |
| H-workflow：Workflow Product / Product Operations，C/D | C-pattern → 流程状态、信息可见性、内部工具；制造业数字化、企业协作、循环服务 | 工作流产品、产品运营／内部工具产品；流程规则／信息断点／workflow prototype；注意获客、营收、销售 KPI | 同标题可能重增长收入，保留 capability adjacency 但偏好降级；UNVALIDATED |
| H-AI：Applied AI Product / Human-AI Experience，A/C/D | C-pattern 与 S-AI → 人机任务、人工复核与反馈；创意工具、企业知识工作、健康信息服务 | AI 产品、Human-AI Experience／AI 产品质量；人工介入、验证／失控、误用／复核流程、评估样例；注意 RAG 平台工程、售前、视觉重 AI Experience | 进入假设池不要求 PM title；但真实技术硬门槛与团队职责必须核验。腾讯 frozen fixture 提供 MARKET_SIGNAL_FOUND，未成为 VALIDATED_BY_CURRENT_JD |
| H-game：Game Systems / Interactive Prototyping，C/D | X AI Survival 的规则、状态、反馈与试玩，辅以 C-stretch 的迭代模式；游戏、互动学习、模拟体验 | 系统策划、交互原型／玩法原型；状态与反馈／引导摩擦／playable demo；注意引擎工程、商业数值运营 | 单一游戏上下文不建立成熟系统策划专长；若 JD 要求上线游戏／引擎实现则削弱。UNVALIDATED |

每项的原始假设均保留在本稿，随后只给 H-AI 追加腾讯历史观察。没有搜索、抓取或用 ESCO/O*NET 当市场证据。学历不划定行业；正常访谈、跨职能沟通和内部 presentation 不视作销售。MT 没有明确职能、低销售／轮岗风险和高 Career Value 的证据，暂不进入优先池。

## Stage 3 — /analyse-job：潜力能加分，不能代替资格与事实

A-TENCENT-CORE-01 输入 D-CORE-01 的 H-AI、A 的精确身份及 E 的原证据 ID。公司／角色为腾讯 2027 AI Product Manager 的历史记录；当前地点、发布日期、截止、开放状态、BG／团队 HC、公司申请约束及 current verification date 都为 UNKNOWN。官方发现路径保留在 TENCENT／SCAN 源索引，本次未读取官网。

历史资格保留 A 中直接用户确认的 ELIGIBLE 记录；当前 qualification=VERIFY。没有从 title、潜力或历史 Full Evidence Match PASS 推导今天的资格。BG／产品场景存在依旧不等于实际 HC。

两条 MUST 是 accepted fixture 中的规范化需求，不是本次重新认定的官方硬资格。没有添造 STRONG PREFERENCE／NICE TO HAVE。原始 JD 措辞及完整需求覆盖仍待核验。

| 需求／来源 | Match 与 claim/use 判断 | 对假设的影响与真实 gap |
|---|---|---|
| workflow / A.requirements.workflow | dneg-workflow：SUPPORTED **仅限既有 Human-AI 原型工作流**。S-AI 则是从这部分行为向目标 AI 产品职责的 DEFENSIBLE_STRETCH，仍为推断，不让更广的潜力继承 SUPPORTED | 能正向支撑 H-AI 的应用层工作假设；不能证明商业上线、真实 Agent 系统或全栈工程 |
| product-data / A.requirements.product-data | dneg-testing：PARTIAL + DEFENSIBLE_STRETCH（S-evaluation）。从观察→问题→改动的机制，合理迁移到产品评估问题和验证规划 | H-AI 中“可做评估规划”的部分得到支持；“已经能独立承担商业数据分析”的版本被削弱。SQL、A/B、留存／漏斗与商业指标 ownership 仍是未获支持的子项 |

完整市场观察：job_key 与 A 一致，source_kind=EXTERNAL_REPORT，fixture_as_of=2026-09-11，inspected_current_original=false。title variant 为 AI Product Manager／AI 产品经理的责任候选表达；两条实际职责只在这个规范化快照范围比较。没有证据宣告腾讯某条真实 MUST 与候选人硬冲突，故不制造 CONTRADICTED。已有的产品数据 gap 足以削弱“全范围已准备就绪”的版本；若后续 JD 核心转为 RAG／模型／生产工程，H-AI 的该岗位版本应降级或被否定，能力来源历史保留。

| 维度 | 判断 | 理由／来源与未决项 |
|---|---|---|
| Capability Fit | MIXED，含正向 transferable fit | C-pattern、C-stretch、S-AI/S-evaluation 可支撑应用层产品探索；商业数据及工程深度未建立 |
| Evidence Fit | MIXED | E/OUTPUT/BATCH 有定位与 ownership 边界；Master Evidence、事件链与权限仍不完整 |
| Experience Fit | MIXED | 项目原型及测试是有效经验，不能改称正式 PM 任职或商业全周期 |
| Eligibility Fit | UNKNOWN（当前 VERIFY） | A 保留历史 ELIGIBLE；当前适用资格原文缺失 |
| Practical Fit | UNKNOWN | A 未给当前地点与实际分配，不能借快手城市数据填入 |
| Career Value | HIGH，条件性判断 | 若 A 的应用层职责成立，可检验 C-pattern 的产品迁移；完整 JD 仍可能改变此判断 |
| Interest / Preference Fit | MIXED | X 的偏好不排斥这类产品判断；具体腾讯团队兴趣未明 |
| Work-style Preference Fit | UNKNOWN | 未提供当前核心日常职责；若收入／销售主责则负向，普通协作中性 |
| Interview Process Risk | UNKNOWN | 未提供流程，不推测群面／算法题等既成安排 |
| Stretch Level | MODERATE | 相邻的产品判断桥梁清楚；目标的商业／技术部分仍需分开验证 |

建议：**Explore，保留一个腾讯 targeted 策略。** 比纯“缺少 PM title／缺少直接证据”判断更积极，因为可迁移的流程和验证能力已有解释；仍不进入 Apply，因为当前岗位、资格、约束和可用材料链未齐。保留 H-discovery/H-workflow 作为并列方向，不用腾讯 title 反向改写全部定位。

## Stage 4 — /prepare-application：强表达，窄事实

P-TENCENT-CORE-01 读取 A-TENCENT-CORE-01 同一身份及 revision；实际调用既有 preparation guard 得到 PREPARATION_HOLD。阻塞是 current authority、当前 qualification、公司约束和材料链，不能由 stretch 绕过。`claim_candidates=[]`，`packet=null`。

本轮明确授权的内部 framing_review 可以继续完成竞争力检查。以下是 **NOT_FOR_ADOPTION 的候选措辞**，只有核验底层个人事实、准确版本与使用权限后才可进入真实材料；这个共同边界不重复附在每句 bullet 后。

| 目的 | 过弱／不准确示例 | 更强且可解释的候选表达 | 内部 claim boundary |
|---|---|---|---|
| 原型 ownership | “Used Codex to help build a prototype.” | “Independently developed and iterated a working web prototype using Codex-assisted implementation.” | OUTPUT §2 的个人原型落地、测试和迭代支持该报告级候选；independently 只修饰 prototype，不修饰团队研究／整个项目。原个人事实尚未直接核验，不标 VERIFIED_FACT |
| 岗位定位 | “Interested in AI product management.” | “Research-led product prototyping, with a focus on Human-AI workflows and iterative validation.” | S-AI / DEFENSIBLE_STRETCH。专业定位语言，不声称正式职称、生产 AI 系统或工程资格 |
| 面试迁移 | “I have no commercial product data experience.” | “My strongest evidence is turning qualitative testing into product changes. I can bring that approach to framing evaluation questions and validation plans; commercial analytics is the next area I need to demonstrate.” | S-evaluation / DEFENSIBLE_STRETCH。承认可带来的价值，再回答真实 gap；没有把计划写成历史结果 |
| 修改成果 | “Improved usability significantly.”（无效果证据，不采用） | 若需数字，保留“3 formal test rounds and 9+ documented changes”这一待原件核对的汇总；若数字无助于叙事，改为“Iterated the prototype through structured testing and feedback.” | 单位仍为轮／修改，不是人数或改善比例。没有生成 30% usability 或 50% efficiency |

措辞选择体现潜力，不要求每句简历都带全部 limitations。关键区别在于：产品判断和原型迭代是可讨论的真实行为；Agent/RAG／ML／backend 技术实现是另一类需要额外事实支撑的主张。

**最小 preparation strategy：** 既有 CN-P / Product Base 路由，精确文件／版本 UNKNOWN；DNEG 主项目，Circular Flow 作为跨场景复用能力的后备。若实际职责重人机控制，再从 C the Signs／AI Survival 中挑一项替换后备，不堆满所有项目。不派生虚构 BG CV，不新增项目或完整求职礼包。Portfolio 分享权限和可用版本未确认，本稿不输出可批准的分享链接。

| Recruiter concern（INFERENCE） | L1 — What | L2 — Transfer | L3 — Boundary |
|---|---|---|---|
| “你做的是工具操作还是产品判断？” | OUTPUT/BATCH 报告中的流程设计、原型落地、测试解释与迭代；研究 partly team-shared，Codex 支持实现 | 用规则和可运行交互使假设可测，与应用层 AI 产品发现相邻 | 不声称独立领导整项目或独立承担生产代码架构 |
| “你没有 PM 职称，为什么适合？” | DNEG、Circular Flow、AI Survival 中可定位的规则／反馈／原型选择 | 迁移的是反复出现的行为机制，不依赖旧 title；目标是能贡献的产品发现与验证工作 | 商业路线图、资源协调、正式算法团队合作和规模化经营尚未证明 |
| “评估做出了多大效果？” | dneg-testing 的 3 轮／9+ 是报告汇总，逐事件原件不完整 | 可以解释测试问题如何转成产品改动，并提出未来评估方案 | 不虚构具体九个事件、参与者或统计／商业改善；提出方案用未来式 |
| “是真 AI／RAG 产品吗？” | F-documentary：实现说明写明 simulated default，optional 支持范围有限 | 该原型可以讨论 Human decision、复核和反馈的体验设计 | 没有核验实时 provider 或候选人的 RAG／模型开发，不能说已部署商业 AI 系统 |

以上 L1–L3 通过内部审阅，但个人事实原件／权限未解决，因此只支持本稿的条件式 framing_review，不授予材料采用许可。

下一步只需四项：同一岗位当前原始 JD 与资格；实际团队／HC／地点／申请约束；DNEG ownership／测试与材料权限；现有 CN-P frozen source/version。当前不向用户发起补故事问答，不要求新作品或测试。Human 可先判断这套“产品判断＋原型验证”的表达是否值得进入下一次真实岗位核验。

## 五条反向追溯

每行的短 ID 与 trace JSON 对应；scope 沿链收窄，未补造原事实。

| 最终策略／主张 → 分析 → 假设 → profile → 原证据 | 类型与链路状况 |
|---|---|
| P-record 不宣称实时 AI → A-record 技术边界 → H-record 应用层而非生产 AI 工程 → C-record 文档边界 → dneg-runtime → DNEG_IMPLEMENTATION AI Integration Boundary | VERIFIED_FACT 仅限文档所写 simulated default。来源可达；当前运行／作者验证不在范围内 |
| P-pattern DNEG-first 产品判断定位 → A-pattern workflow 的原型层 SUPPORTED → H-pattern / H-AI → C-pattern INFERRED → dneg-ownership → OUTPUT §2，附 X 跨场景 refs | INFERRED 沿链保留，未转换为直接核验能力。到报告可达；更深 Master Evidence 链缺失已标记 |
| P-stretch 评估问题／验证规划的 bridge answer → A-stretch product-data PARTIAL → H-stretch / H-AI 的评估部分 → C-stretch 定性测试迭代模式 → dneg-testing → BATCH Usability row | DEFENSIBLE_STRETCH，L1–L3 可解释；未来商业责任仍未证明，不升级 SUPPORTED |
| P-gap 排除 SQL／A-B／商业成果声明 → A-gap product-data 未支持子项 → H-gap / H-AI 商业分析版本被削弱 → C-gap 覆盖缺口 → dneg-testing 的定性测试范围 | Genuine Evidence/Experience gap；源记录未提供所需成果。链完整不等于已经证明不存在能力 |
| P-unknown NOT_FOR_ADOPTION／Base version VERIFY → A-unknown Evidence Fit 与准备 gate → H-unknown 所有角色不授予材料许可 → C-unknown 权限与既有来源上下文 → dneg-workflow resume_use=UNKNOWN | UNKNOWN 保持。精确 CV Base 外部链接明确断裂／不可定位，未用文件名相似补齐；先核验再采用 |

这些 JSON 节点是报告决策的索引，不是新的证据库。结构测试验证 ID／edge／job identity；语义对应由本 agent 执行与审阅，不能宣称 Python 自动证明迁移或文字真实性。

`HUMAN_REVIEW_REQUIRED`
