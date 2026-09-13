# Global Job Quality Market Calibration v0.1

**Status:** Traceability patch complete — final Human Review ready  
**Market capture date:** 2026-09-13  
**Scope:** China baseline + UK baseline  
**China salary cohort:** 海内外硕士应届生为主；本科/全体毕业生只作背景  
**UK work-right state:** `VERIFY`

---

## 0. Executive calibration

### China

- 对本次目标岗位，不能用一个“全国毕业生平均工资”判断 Offer。硕士应届、城市、职能、公司类型及 AI 溢价共同决定市场区间。
- 公开数据可较稳健地支持的结论是：一般硕士应届市场的背景中心约在 **8k–14k RMB/月**，而杭州、上海、深圳、北京的产品/AI 产品通常高于这个背景区间；南京、苏州、广州仍需按岗位和公司拆分。
- **AI 公司或 AI title 不自动等于高薪。** 有意义的溢价通常来自真正的 AI 产品责任、模型/Agent/评估工作、稀缺能力和高质量公司，而不是名称。
- 五险一金是合规基础，不是“竞争力福利”；补充医疗、住房/搬迁、餐补交通补贴及更高公积金才是增量价值。
- 标准工时是 8 小时/日、40 小时/周；但“招聘页写双休”仍不足以证明实际团队没有结构性晚间或周末加班。
- 符合条件的 early-career worker 法定年休假起点通常为 5 天。**10–15 天高于法定起点，但当前研究不足以判断其市场普及度。** Market 状态保持 `ABOVE STATUTORY BASELINE / MARKET PREVALENCE VERIFY`；个人对 10–15 天年假的强偏好不变。
- 试用期 6 个月在 3 年以上或无固定期限劳动合同下可能合法，但对 early-career Offer 仍应结合工资、转正标准和淘汰风险判断；试用期工资约 80% 可能合法且符合已确认个人容忍线，但不是“优质”信号。

### UK

- 2026 年英国头部 100 家 graduate employers 的起薪中位数为 **£35,000/年**；这是“大型正规 graduate employer”基准，不能代表所有 direct-entry 岗位。更广泛 early-career 市场常见区间约为 **£25,000–£35,000**。
- London 对同类岗位通常有名义薪资溢价，但 2026 年平均私人租金约 **£2,317/月**；Bristol 约 **£1,880/月**、Manchester 约 **£1,350/月**。这些是整套私人租赁平均数，不等于合租房间价格，但足以说明不能只用汇率或 London headline salary 比较 Offer。
- 法定最低带薪假为 5.6 周；五天工作制通常对应 **28 天，且可包含 bank holidays**。所以“25 天 + bank holidays”通常是较好基准，“28 天 including bank holidays”只是法律地板附近。
- 雇主养老金自动加入的法定最低总缴费通常为 8% 的 qualifying earnings，其中雇主至少 3%。更高雇主缴费才是竞争力福利。
- 2026 Skilled Worker 一般工资门槛是 **£41,700 或 occupation going rate 中较高者**。符合 new entrant 条件时，可能使用 70% going rate，但通常仍需至少 **£33,400**。因此一个岗位可以在薪资市场上“正常”，却仍无法支持 sponsorship。
- Graduate visa 的长度取决于申请日期：2026-12-31 前申请通常为 2 年；2027-01-01 起申请通常为 18 个月；博士为 3 年。候选人是否能用该路径取决于课程完成、学校报送、当时 Student visa 状态和实际申请时间，当前保持 `VERIFY`。

---

# A. Global Job Quality Market Calibration v0.1

## 1. Research boundary and method

### 1.1 Strict separation

| Layer | 本报告如何处理 |
|---|---|
| Market Benchmark | 描述市场中的低 / 常见 / 较好 / 很有竞争力条件 |
| Personal Preference | 只与已 Human-confirmed Profile 对照；不由市场数据改写 |
| Role-level reality | 没有岗位级证据时保持 `VERIFY` |
| Eligibility / Sponsorship | 与能力、职业价值和薪资质量分开判断 |

### 1.2 Salary basis

- China：**税前固定月薪**，不含未书面保证的年终奖、股票、人才补贴和一次性签字费。
- UK：**税前年固定 base salary**，不含 discretionary bonus、equity 和一次性 relocation/sign-on。
- 固定薪资、保证现金、浮动奖金和股权必须分别记录。
- 标有 `×13 / ×14 / ×16` 时，只在劳动合同或正式 Offer 明确保证发放时，才进入 guaranteed cash。

示例：

| Offer wording | Fixed base | Guaranteed cash | Variable |
|---|---:|---:|---:|
| China 15k/月 × 14 薪，14 薪书面保证 | 15k/月 | 210k/年 | 另列 |
| China 15k/月 × 12 + 年终奖最高 2 个月 | 15k/月 | 180k/年 | 0–30k，且可能为 0 |
| UK £38k + target bonus 10% | £38k/年 | £38k/年 | target £3.8k，不保证 |

### 1.3 Evidence grading

| Grade | Meaning |
|---|---|
| HIGH | 政府/监管/官方规则，或稳定的多源市场数据 |
| MEDIUM | 多来源方向一致，但样本不是完全对应“硕士应届 × 城市 × 角色” |
| LOW | title 稀疏、样本混合、城市样本少；只能作方向性校准 |
| INSUFFICIENT DATA | 不给数字区间，等待岗位级或更强市场样本 |

所有矩阵区间都是 **calibration bands**，不是统计意义上的精确分位数，也不是自动 Apply/Reject 阈值。

CSV 现已增加 `traceability_status`、`source_refs`、`source_types`、`source_capture_dates`、`sample_count`、`sample_scope`、`salary_transparent_postings`、`derivation_type`、`derivation_note`、`visa_salary_gate` 和 `visa_source_refs`。旧 `evidence_bundle` 仅保留为摘要，不再承担行级溯源功能。

本轮 60 行中，2 行为 `FULL`，58 行为 `PARTIAL`。`PARTIAL` 表示来源方向仍可解释区间，但原研究没有保留完整的岗位样本清单、精确数量或完整 URL。它不等于数据无效，也不能被当成统计分位数。

---

## 2. China baseline

### 2.1 Compensation baseline

#### Market anchors

- 2025 年全国城镇非私营单位平均工资为 129,441 元；信息传输/软件/IT 服务为 248,752 元，科研和技术服务为 182,064 元，外商投资单位为 164,956 元。这些是**全体从业人员**数据，不是应届起薪，但能说明行业和公司类型差异很大。[国家统计局](https://www.stats.gov.cn/sj/zxfb/202605/t20260515_1963707.html)
- 聚合型毕业生资料给出的硕士起薪背景约为 10.1k/月、常见 8k–14k；该数据不是政府统计，且混合行业，只用于建立全国背景，不直接决定具体 Offer。[赛氪就业数据汇总](https://m.saikr.com/employment-rank)
- 2025 城市“新质人才”招聘薪酬中，北京 17,095、上海 16,910、深圳 15,975、杭州 14,596 元/月；样本混合年资和高级人才，**只用于城市/新质岗位方向比较**。[潮新闻转述北大城市软实力研究院×智联招聘报告](https://tidenews.com.cn/news.html?id=3498420)
- 2026 年 1–5 月新发校招 AI 岗位同比增长 47.3%；北京、上海、深圳、杭州、广州为校招岗位量前五，产品经理进入校招热门岗位前十。这支持 AI 需求和城市热度，不提供可靠起薪分位数。[证券时报·e公司](https://m.ahanganji.com/news/detail/2310288.html)
- AI Product Manager 的公开招聘均值和平台薪资通常混合 1–10 年经验，不得直接当作应届生薪资；本报告只把它们作为“AI 应用产品可能有溢价”的辅助信号。

#### China salary calibration summary

完整 42 行 China 矩阵见 `Salary_Calibration_Matrix_v0.1.csv`。以下为读法摘要，单位均为 **RMB/月，税前固定 base**：

| City group | Product / Digital 常见 | Research / Insights 常见 | Product Ops / Workflow 常见 | Strategy / Innovation 常见 | Applied AI / Agent Product 常见 |
|---|---:|---:|---:|---:|---:|
| Hangzhou | 9k–15k | 8k–13k | 8k–14k | 10k–16k | 12k–20k |
| Nanjing / Suzhou | 8k–13k | 7k–12k | 7k–12k | 9k–14k | 10k–17k |
| Guangzhou | 8k–14k | 8k–13k | 8k–13k | 9k–15k | 11k–19k |
| Shanghai | 10k–16k | 9k–15k | 9k–15k | 11k–18k | 14k–23k |
| Shenzhen | 10k–16k | 9k–15k | 9k–15k | 11k–18k | 14k–24k |
| Beijing（比较市场） | 11k–18k | 10k–16k | 10k–16k | 12k–20k | 15k–25k |

解释：

- 这些区间针对 **硕士应届 / early-career、非纯研发、与本项目 Role Families 相邻的岗位**。
- `Competitive` 通常位于 common band 上方约 4k–8k/月；`High` 对公司质量、责任范围、保证薪数和工作强度要求更高，详见 CSV。
- Product Prototyping / 0→1 Product Builder 不是稳定 title，China 城市级公开薪资样本不足。CSV 给的是相邻职位参照并标记 `LOW`，不能直接当成该 title 的市场价。
- 对 China 0–2 年社招，若明确要求已有商业 ownership，薪资可能高于 campus band，但同时 experience gate 更强；不可把社招价反推应届 Offer 应有水平。

#### What counts as concerning

- 目标城市的硕士应届产品/研究/系统类岗位，**4k–6k/月仍属于强警戒**。
- 8k–9k 不是全国统一结论：在南京/苏州/广州部分 research/ops 岗可能落入常见低端；在上海/深圳/北京或实质性 AI Product 岗通常偏低。
- 低于 common band 不自动 Reject，但必须能明确交换到稀缺 Career Capital、正常生活质量、强 mentorship 或非常低生活成本；否则性价比弱。

### 2.2 Annual package and bonus

| Component | Benchmark treatment |
|---|---|
| 12 个月固定月薪 | guaranteed fixed cash 基线 |
| 明确保证的 13/14 薪 | 可计入 guaranteed cash；需核合同措辞 |
| “年终奖 1–3 个月 / up to” | discretionary；不得按上限计入 |
| 绩效奖金 | 记录 target、历史兑现与个人/公司触发条件 |
| 股权 / 期权 | 单列；未上市公司按高不确定性资产处理 |
| 人才补贴 | 只有官方政策仍有效且本人满足条件时才计入 effective compensation |

“13薪”没有跨公司的统一法律含义。公司政策也会变化；因此不要把“互联网通常 13/14/16 薪”编码成稳定规则。

### 2.3 Benefits benchmark

| Benefit | Market baseline | Better | Role-level verification |
|---|---|---|---|
| 五险 | 正式劳动关系的合规基础 | 补充医疗、商业险、年度体检 | 缴费基数、起缴月份、补充保险覆盖 |
| 公积金 | 合规缴存是基础 | 较高单位比例、按实际工资基数缴 | 城市比例/基数、试用期是否缴纳 |
| 餐补/交通/通讯 | 非法定，常见但差异大 | 现金价值稳定、适用日广 | 是否并入工资、出勤限制 |
| 住房/人才补贴 | 非公司通用福利 | 宿舍、租房补贴、搬迁费可显著改善首年现金流 | 政策有效期、户籍/学历/首次就业条件、本人资格 |
| 补充医疗 | 非法定 | 门诊/住院/牙科/家属覆盖更完整 | 免赔额、报销比例、试用期等待期 |
| Relocation | 非普遍 | 一次性搬迁、临时住宿、差旅报销 | 返还条款、服务期 |

### 2.4 Time and lifestyle

- 国家标准工时为 **8 小时/日、40 小时/周**。[国务院关于职工工作时间的规定](https://xzfg.moj.gov.cn/law/download?LawID=629&type=pdf)
- 一般延长工时规则为每日通常不超过 1 小时；特殊情况下每日不超过 3 小时、每月不超过 36 小时。加班报酬通常对应工作日 150%、休息日不能补休时 200%、法定节假日 300%。[中华人民共和国劳动法](https://www.gov.cn/banshi/2005-05/25/content_905.htm)
- 企业可以根据实际情况安排周休息日，所以“不是周六日休”不必然违法；但对本人的双休偏好仍可能 Practical/Lifestyle Fit 较差。
- 招聘页的“双休、弹性、朝九晚六”是初步信号，不是团队事实。需在 Offer 前验证：实际到离时间、版本/上线周期、周末频率、调休/加班费、跨时区会议。
- 关于 996、管理压力和“很难请假”的信息，除非来自公司正式政策，只能标为 `ANECDOTAL / COMMUNITY SIGNAL`，并记录团队、地点和时间。

### 2.5 Annual leave

中国带薪年休假法定基线按累计工作年限计算：连续工作满 12 个月后，累计 1–10 年通常 5 天、10–20 年 10 天、20 年以上 15 天；休息日和法定节假日不计入年休假。[职工带薪年休假条例](https://www.gov.cn/zwgk/2008-02/21/content_895662.htm)

对 early-career：

| Employer offer | Market interpretation |
|---|---|
| 只有法定年假 | 法定基线；市场普及度判断不适用 |
| 7–9 天 | 高于法定起点；`MARKET PREVALENCE VERIFY` |
| 10–15 天 | `ABOVE STATUTORY BASELINE / MARKET PREVALENCE VERIFY`；个人强偏好保持不变 |
| >15 天 | 明显高于法定起点；市场普及度和实际可用性仍需核实 |

### 2.6 Probation

法定上限通常取决于劳动合同期限：3 个月以上不满 1 年可约定不超过 1 个月；1 年以上不满 3 年不超过 2 个月；3 年以上或无固定期限不超过 6 个月。同一单位与同一劳动者只能约定一次试用期。试用期工资不得低于同岗位最低档或劳动合同工资的 80%，且不得低于当地最低工资。[劳动合同法](https://www.gov.cn/flfg/2007-06/29/content_669394.htm)

| Condition | Market / quality interpretation |
|---|---|
| 1–3 个月、100%工资、标准明确 | 较好 |
| 3 个月、80%–100% | 常见可接受，仍核转正标准 |
| 6 个月、80% | 可能合法但质量风险明显上升 |
| 竞业/培训费/高淘汰/模糊转正 | 强风险，必须读合同并人工确认 |

### 2.7 Employment quality and company type

| Signal | Established company | Startup / smaller company |
|---|---|---|
| Payroll / stability | 查主体、合同主体、发薪日、社保公积金基数 | 额外查融资 runway、现金流、欠薪/社保历史 |
| Development | 正式 graduate training、mentor、明确 job ladder 加分 | founder/manager 能否提供反馈、是否只有“自己摸索” |
| Ownership | 可能流程成熟但 scope 较窄 | 可能 ownership 大，但也可能是人手不足 |
| Equity | 大公司 RSU 可有市场价格 | 私企期权高不确定；不替代合理 fixed pay |
| Workload | 品牌不能证明团队强度 | “创业”也不能自动推定 996；逐团队验证 |

---

## 3. UK baseline

### 3.1 Compensation baseline

#### Graduate Scheme vs direct-entry

| Route | Typical structure | Salary interpretation |
|---|---|---|
| Graduate Scheme | 1–3 年，可能轮岗、培训、mentor、cohort | £35k 是 2026 头部 100 家雇主中位数，偏大型正规雇主样本 |
| Direct-entry graduate / junior | 具体岗位、团队招聘，培训差异大 | 更广泛常见约 £25k–£35k；London/tech/product/research 可更高 |
| Junior PM title | 市场常要求相关经验，不一定真正 entry-level | UK guide 给出约 £33k–£34k 平均，但 role-level gate 必须核实 |

来源：[High Fliers 2026](https://highfliers.co.uk/publication-the-graduate-market-report)、[University of Sheffield employer guide](https://sheffield.ac.uk/careers/employers/support/setting-appropriate-graduate-salary)、[ISE graduate salary analysis](https://ise.org.uk/knowledge/insights/259/what_are_the_average_salaries_for_graduates_school_leavers_and_interns/)、[Prospects Product Manager](https://www.prospects.ac.uk/job-profiles/product-manager/)。

#### UK salary calibration summary

完整 18 行矩阵见 CSV。单位均为 **GBP/年，税前固定 base**：

| City | Product / Digital 常见 | Research / Insights 常见 | Product Ops / Workflow 常见 | Strategy / Innovation 常见 | Applied AI / Agent Product 常见 |
|---|---:|---:|---:|---:|---:|
| London | £32k–£40k | £32k–£40k | £30k–£38k | £32k–£42k | £35k–£47k |
| Bristol | £28k–£35k | £29k–£36k | £27k–£34k | £28k–£36k | £32k–£42k |
| Manchester | £28k–£35k | £28k–£36k | £27k–£34k | £28k–£36k | £32k–£42k |

Notes:

- User Research 有较清晰职业资料：National Careers Service 给出的 starter 约 £34k；Prospects 指 UK UXR 起薪通常 >£30k，部分接近 £40k。[National Careers Service](https://nationalcareers.service.gov.uk/job-profiles/user-researcher) [Prospects UXR](https://www.prospects.ac.uk/job-profiles/ux-researcher/)
- Applied AI / Agent Product 样本稀疏且常混合技术/经验溢价，置信度低于一般 Product。三座城市的 `low_concerning` 现统一为 `INSUFFICIENT DATA`。£33,400 只出现在独立的 `visa_salary_gate`，不再充当市场低薪界线。
- Product Prototyping / 0→1 Product Builder 缺乏稳定 title 与城市样本，v0.1 标为 `INSUFFICIENT DATA`；未来只用具体职位职责和公布薪资判断。
- Cambridge / Edinburgh / Birmingham 暂不输出角色级数字矩阵：现有可靠、同口径数据不足，避免用 UK 平均值硬填。

### 3.2 Benefits

| Benefit | Legal / common baseline | Competitive signal | VERIFY |
|---|---|---|---|
| Pension | qualifying earnings 上总最低 8%，雇主至少 3% | 雇主 6%–10%+、salary sacrifice、match 更高 | eligibility、waiting/postponement、贡献基数 |
| Annual leave | 5.6 周；五天制 28 天，可含 bank holidays | 25 天 + bank holidays；30 天 + bank holidays 很强 | bank holidays 是否另计、buy/sell、carry-over |
| Sick pay | statutory SSP 是地板 | full-pay occupational sick leave | probation 时是否适用、等待期 |
| Private medical | 非法定；大雇主较常见 | dental/vision/family/low excess | taxable benefit、覆盖开始时间 |
| Hybrid | 常见但不是默认权利 | 明确 2–3 天 office 且团队执行一致 | team days、试用期、未来 policy change |
| Relocation | 非普遍 | 现金、临时住宿、签证费支持 | repayment / clawback、税务处理 |
| Bonus / equity | 职位和行业差异大 | 明确 target、历史 payout、可交易 equity | discretionary、vesting、leaver rules |

权威基线：[GOV.UK holiday entitlement](https://www.gov.uk/holiday-entitlement-rights/holiday-pay)、[GOV.UK workplace pension](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay)、[GOV.UK SSP](https://www.gov.uk/statutory-sick-pay)。

### 3.3 Cost context

| City | 2026 observed average private rent | Interpretation |
|---|---:|---|
| London | 约 £2,317/月 | 名义薪资最高，但住房成本显著吞噬 premium |
| Bristol | 约 £1,880/月 | 不是“低成本城市”；相对 Manchester 仍高 |
| Manchester | 约 £1,350/月 | 住房压力通常低于 London/Bristol，但区域/通勤差异大 |

限制：这是全体私人租赁住房平均值，不是 room-share，也未纳入 council tax、交通、能源和个人生活方式。Offer 比较应使用候选人的真实住房方案，而非简单用平均租金相减。[ONS private rent statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/privaterentandhousepricesuk/latest)

### 3.4 Working time and probation

- 大多数劳动者平均每周不得超过 48 小时（通常按 17 周平均），但个人可以 opt out。[GOV.UK](https://www.gov.uk/maximum-weekly-working-hours)
- 工作超过 6 小时通常有 20 分钟休息；两工作日间通常 11 小时休息；每周 24 小时或每两周 48 小时不间断休息。[GOV.UK](https://www.gov.uk/rest-breaks-work)
- UK 没有法定必须设置 probation，也没有统一法定长度。市场上 3–6 个月常见，但必须看合同；probation 期间仍有最低工资、带薪假、反歧视等 day-one rights。[Acas，更新 2026-07-24](https://www.acas.org.uk/probation-periods)
- 2027-01-01 起，普通 unfair dismissal protection 将在连续受雇 6 个月后适用；这是时间敏感规则，未来必须重新验证，不能静态硬编码。

### 3.5 Job quality signals

| Stronger signal | Neutral / role-level | Risk signal |
|---|---|---|
| 明确 25–30 天假期 + bank holidays | “competitive benefits”但无细节 | 法定最低附近且措辞模糊 |
| 雇主 pension >3% | statutory pension | 无法确认 pension basis |
| 明确 mentor / accredited learning / cohort | “learning opportunities” | 无经理反馈、无 role ladder |
| 明确 hybrid days 和 team location | “hybrid”标签 | 实际全周到岗或政策可随时变 |
| 正常合同、固定 base、清晰 probation | bonus/equity 另列 | 低 base 被不确定 bonus 包装 |
| role/program 明确 sponsor policy | 公司在 sponsor register | “must have unrestricted right to work”或不 sponsor |

---

# B. Salary Calibration Matrix

交付文件：`Salary_Calibration_Matrix_v0.1.csv`

### How to use

1. 先识别 Market、City、实际职责和 recruitment route。
2. 对固定 base 定位 `LOW / COMMON / COMPETITIVE / HIGH`。
3. 再单列 guaranteed extra months、bonus、equity、housing/relocation。
4. 查看行级 `source_refs`、样本范围、推导方式和 `traceability_status`。
5. China 检查社保公积金和实际工时；UK 另查 `visa_salary_gate`。签证门槛不参与 market salary band。
6. 任何低置信度或 `PARTIAL` 行不能决定申请；只触发 role-level evidence collection。

---

# C. Benefits & Employment Conditions Matrix

交付文件：`Benefits_Employment_Conditions_Matrix_v0.1.csv`

最重要的跨市场不可比点：

- China “5 天法定年假起点”与 UK “5.6 周法定最低”完全不是同一休假制度。
- China 五险一金与 UK NHS + workplace pension 的结构不同，不能简单比较“福利项数量”。
- China 月薪常需乘保证薪数；UK 通常直接报年 base。
- UK sponsorship 是额外 eligibility 层，不代表岗位本身薪资质量。

---

# D. UK Sponsorship / Work-right Verification Guide

单独交付：`UK_Sponsorship_Work_Right_Verification_Guide_v0.1.md`

核心状态模型：

| Status | Meaning |
|---|---|
| `WORK_RIGHT CONFIRMED` | 候选人已有覆盖 start date 与工作安排的权利 |
| `GRADUATE_ROUTE POSSIBLE — VERIFY` | 可能符合，但课程完成/学校报送/Student visa/申请日期未全部确认 |
| `SPONSOR LICENCE EXISTS` | 公司在官方 register；不代表岗位 sponsor |
| `ROLE SPONSORSHIP CONFIRMED` | 官方岗位/项目页面明确支持，且 occupation/salary 条件可满足 |
| `SPONSORSHIP UNKNOWN` | 公司或岗位未明确；保持 `VERIFY` |
| `SPONSORSHIP UNAVAILABLE` | 该岗位/项目明确不支持；若无其他 work right，则 role eligibility 不通过 |

---

## 4. Personal Preference comparison — not a preference rewrite

| Human-confirmed preference | China market relation | UK market relation |
|---|---|---|
| 薪资相对市场/城市合理 | 正常且可执行；需逐岗拆 fixed/bonus/薪数 | 正常；需同时做 city cost 与 visa floor 两条判断 |
| 双休、正常休息 | 合法工时目标合理，但“实际稳定双休”需团队证据 | 五天制通常正常；仍核 48h opt-out、launch/client peaks |
| 反对结构性 996 / 长期 21–22 点 | 高于“只看合同”的要求，但不是不合理；主要是 role-level verification 难 | 通常更容易满足，但 consultancy/startup/launch roles 仍不保证 |
| 10–15 天年假有明显价值 | 高于 China 法定起点；市场普及度未知，不能判断为“高于市场要求” | 容易满足；UK 法定最低本身通常已高于此数字 |
| 高压管理是风险 | 市场数据不能证明具体团队；始终 `VERIFY` | 同样必须逐团队验证 |
| Hybrid 加分但不决定 | China 角色/公司差异大，不能设默认 | UK 较常见，但 role-level policy 仍可能变 |
| Startup 可接受，风险回报要好 | 合理；需增强 payroll/runway/社保/ownership 检查 | 合理；需增强 funding/runway/pension/leave/sponsorship 检查 |
| Growth + ownership 重要 | 不能从“大厂/小厂”推断 | Graduate Scheme 结构化成长强；direct-entry ownership 可能更直接 |
| AI/frontier + future mobility 重要 | 市场需求高，但高薪与好生活不自动成立 | Career value 高，但岗位少、竞争强、sponsorship 可能成为独立门槛 |
| 高薪不能无限补偿不可持续生活 | 属于个人选择，市场不改写 | 同样保留；London 高薪还需扣除真实住房/通勤情境 |

结论：

- **Easy / normal to satisfy:** UK 10–15 天休假；两国要求固定薪资清晰、法定基础福利合规。
- **Normal but requires verification:** 双休/五天制、正常管理、真实 hybrid、奖金稳定性、mentor。
- **Market prevalence remains VERIFY:** China 10–15 天年假。这里只确认它高于法定起点和符合个人强偏好，不判断其是否属于市场常见条件。
- **More demanding combination:** 在高增长 AI/互联网团队同时要求顶薪且长期绝少加班。
- **Unclear until role-level evidence:** 实际下班时间、管理风格、淘汰率、bonus payout、startup runway、团队 hybrid、UK role sponsorship。

---

# E. Calibration implications for Career Intelligence

## 5. Proposed data and rules

### 5.1 Suitable as reference data

- `market_capture_date`
- `market / country / city`
- `role_family` 与 `title_variants`
- `recruitment_route`: campus / 0–2 social / graduate scheme / direct entry
- `salary_currency`、`salary_basis`、`base_min/max`
- `guaranteed_salary_months`、`guaranteed_cash`
- `target_bonus`、`bonus_certainty`、`equity_type`
- `benchmark_band` + `confidence` + `source_bundle`
- statutory leave / work time / pension/social insurance baseline, with jurisdiction and effective date

### 5.2 Suitable as market benchmark logic

- 按 `Market × City × Role Family × Level/Route` 选择区间。
- 先判断 fixed base，再判断 guaranteed cash、variable、equity 和 cost context。
- AI title 不自动使用 AI premium；职责必须包含实质 AI product/workflow/evaluation ownership。
- 稳定 title 不存在时，用 responsibility keywords + output pattern，并降低 confidence。
- 个人城市偏好不得写入市场薪资 band。

### 5.3 Role-level VERIFY rules

China：

- 实际工作时段、周末频率、加班费/调休；
- 13/14/16 薪是否保证；
- 试用期工资、长度、转正标准和淘汰机制；
- 五险一金基数、比例、起缴时间；
- 人才补贴本人是否满足、何时到账；
- startup 合同主体、发薪/社保、runway。

UK：

- 当前 work right 覆盖 start date 否；
- company sponsor licence、specific role sponsorship、occupation code、going rate 四项分别核；
- new entrant 是否适用及总时长；
- Graduate route 申请资格和实际申请日期；
- annual leave 是否含 bank holidays；
- pension employer rate、hybrid team days、probation、relocation clawback。

### 5.4 Do NOT encode as durable rules

- 具体城市薪资区间本身；至少季度/招聘季复核。
- Skilled Worker 金额门槛、occupation going rates、Sponsor Register。
- Graduate visa 时长与资格规则。
- 城市人才补贴、公积金缴存比例/基数。
- 公司 13/14/16 薪、bonus payout、hybrid policy。
- 公司 culture、996、裁员和 startup runway。
- “某公司有 licence = 某岗位 sponsor”。
- “London salary = UK salary”。
- “AI title = AI premium”。

## 6. Proposed handoff: Market Calibration → Career Intelligence

仅作为 `CANDIDATE HANDOFF`，等待 Human Review，不执行 Skill 修改：

1. 导入薪资矩阵为带 `captured_date / confidence / source_bundle` 的 reference dataset。
2. 新增 compensation normalization：fixed base、guaranteed cash、variable、equity、benefits 分栏。
3. 新增 `market_quality_band`，但禁止其自动输出 Apply/Skip。
4. UK 新增独立 sponsorship verifier：licence → role policy → occupation code → salary → candidate route。
5. 所有 volatile facts 增加 `last_verified` 与 expiry/recheck trigger。
6. 将 work-life、management、bonus certainty 保持 role-level evidence，不从 brand 自动推断。

---

## 7. Evidence quality, freshest dates and gaps

### Freshest material used

- UK official sponsor register snapshot: **2026-09-11**.
- China/UK pages captured: **2026-09-13**.
- Acas probation guidance updated: **2026-07-24**.
- China 2026 campus report coverage: **2026-07-02**.
- China 2025 wage release: **2026-05-15**.
- High Fliers Graduate Market 2026 publication: **2026**.

### Confidence

| Area | Confidence | Why |
|---|---|---|
| China statutory work/probation/leave | HIGH | 法规/政府来源 |
| China master early-career national background | MEDIUM-LOW | 聚合资料多，官方统计不按该 cohort 发布 |
| China city × role salary bands | MEDIUM-LOW / LOW | 42 行均为 `PARTIAL`；透明岗位样本清单没有完整保留 |
| China AI Product premium | MEDIUM-LOW | 多源方向一致，但样本混合年资且行级样本不完整 |
| UK statutory conditions | HIGH | GOV.UK / Acas |
| UK graduate overall salary | HIGH for top-employer cohort; MEDIUM for broad market | High Fliers/ISE 样本清晰但有大型雇主偏差 |
| UK London Product / UXR | MEDIUM | 2 行可完整回溯至明确调查/职业资料；仍不是统计分位数 |
| UK regional Product / UXR; UK Ops / Strategy | LOW | 城市岗位样本集未完整保留，均为 `PARTIAL` directional bands |
| UK AI Agent Product / Product Prototyping | LOW / INSUFFICIENT | title 稀少、岗位常混合技术年资 |
| UK sponsorship law | HIGH as of capture date | GOV.UK；但金额和清单高度时效性 |
| Role-specific sponsorship | UNKNOWN until each opening is checked | licence 不等于岗位 sponsor |

### Remaining `VERIFY`

- 候选人实际 UK Student/Graduate/其他 work-right 路径；
- 2026-12–2027-01 完成学位与学校向 Home Office 报送的实际日期；
- 每个 UK role 的 occupation code、going rate、new entrant 与 program sponsorship；
- China 目标公司给硕士应届的保证薪数、奖金兑现、五险一金基数；
- 实际团队工作时长、年假可用性、管理压力；
- city/role salary bands 在具体 2027 秋招岗位发布后的再校准。

### Row-level traceability patch

| Scope | FULL | PARTIAL | Main treatment |
|---|---:|---:|---|
| China, 7 cities × 6 role families | 0 | 42 | 保留 directional bands；全部显示样本限制 |
| UK London | 2 | 4 | Product 与 Research 为 FULL；其余依赖相邻职责或未保留的岗位样本 |
| UK Bristol / Manchester | 0 | 12 | 统一为 PARTIAL；Product/Research 降为 LOW |
| **Total** | **2** | **58** | 不新增虚假样本，不把区间称为 percentile |

本轮置信度下调集中在：China 上海/深圳/北京 Product 与 Applied AI、China 上海/深圳/北京 Strategy、UK 两个区域市场的 Product/Research，以及 UK Ops/Strategy 的部分行。UK Applied AI 保持 LOW，但删除了市场列中的签证金额。

---

## 8. Source ledger

### China salary source refs used by the matrix

| Ref | Source type and retained scope | Sample / trace limit |
|---|---|---|
| `CN-NBS-2025` | [国家统计局：2025年城镇单位就业人员年平均工资](https://www.stats.gov.cn/sj/zxfb/202605/t20260515_1963707.html) | Official all-worker data; not graduate starting pay |
| `CN-MASTER-AGG-2026` | [赛氪就业薪资汇总](https://m.saikr.com/employment-rank) | Secondary aggregate: master background around 10.1k, common 8k–14k; sample n not published |
| `CN-CITY-NEW-TALENT-2025` | [潮新闻转述北大城市软实力研究院×智联报告](https://tidenews.com.cn/news.html?id=3498420) | Beijing/Shanghai/Shenzhen/Hangzhou city averages; mixed experience, n not published |
| `CN-CITY-SALARY-2024` | 智联城市薪资报道的 2024 背景资料 | Used only for Nanjing/Suzhou/Guangzhou direction; older data and exact source set incomplete |
| `CN-CIIC-GRAD-2025` | [中智咨询毕业生招聘与薪酬调查](https://www.ciicmc.com.cn/) | Employer survey across 10+ sectors; accessible summary did not expose row-level n |
| `CN-CAMPUS-AI-2026` | [证券时报·e公司：2026校招AI岗位趋势](https://m.ahanganji.com/news/detail/2310288.html) | Demand signal only; no salary range |
| `CN-AIPM-REPORT-2025` | 21世纪经济报道 AI Product Manager 薪资报道 | Mixed experience; article-specific URL was not retained, so matrix rows remain PARTIAL |
| `CN-AIPM-JOBUI-2026` | 职友集 AI Product Manager salary snapshot | Entry-level signal plus mixed-experience distribution; exact sample basis incomplete |
| `CN-JOBS-PRODUCT-2026` | BOSS直聘 campus Product/AI Product snapshots | At least 2 salary-transparent examples noted; complete listing set/URLs not retained |
| `CN-JOBS-RESEARCH-2026` | BOSS直聘 2027 User Research snapshots | At least 1 transparent example retained at 12k–15k ×14; other ads undisclosed |
| `CN-JOBS-OPS-2026` | 猎聘 Product Operations salary snapshot | Platform aggregate mixes education and experience; no row-level sample retained |
| `CN-JOBS-STRATEGY-2026` | Current strategy/innovation/consulting-adjacent snapshots | Direct city-role set not retained |
| `CN-JOBS-PROTOTYPE-2026` | Product/innovation/prototyping-adjacent postings | No stable title; exact set not retained |

### China statutory refs preserved

- [国务院关于职工工作时间的规定](https://xzfg.moj.gov.cn/law/download?LawID=629&type=pdf)
- [中华人民共和国劳动合同法](https://www.gov.cn/flfg/2007-06/29/content_669394.htm)
- [职工带薪年休假条例](https://www.gov.cn/zwgk/2008-02/21/content_895662.htm)
- [中华人民共和国劳动法](https://www.gov.cn/banshi/2005-05/25/content_905.htm)

### UK salary source refs used by the matrix

| Ref | Source type and retained scope | Sample / trace limit |
|---|---|---|
| `UK-HF-GRAD-2026` | [High Fliers: The Graduate Market in 2026](https://highfliers.co.uk/publication-the-graduate-market-report) | 100 leading graduate employers; £35k median; large-employer bias |
| `UK-ISE-GRAD-2024` | [ISE graduate salary analysis](https://ise.org.uk/knowledge/insights/259/what_are_the_average_salaries_for_graduates_school_leavers_and_interns/) | 145 mainly large/formal employers; £32k overall and £34k London; older survey year |
| `UK-PM-PROSPECTS-2026` | [Prospects: Product Manager](https://www.prospects.ac.uk/job-profiles/product-manager/) | Junior PM guide around £33k–£34k; sample n not published and role often requires experience |
| `UK-UXR-NCS-2026` | [National Careers Service: User Researcher](https://nationalcareers.service.gov.uk/job-profiles/user-researcher) | Starter guide £34k; sample n not published |
| `UK-UXR-PROSPECTS-2026` | [Prospects: UX Researcher](https://www.prospects.ac.uk/job-profiles/ux-researcher/) | Starter usually above £30k, some near £40k; sample n not published |
| `UK-REGIONAL-JOBS-2026` | Targetjobs/Indeed current Bristol and Manchester examples | Salary-transparent examples were used, but exact count and listing set were not retained |
| `UK-OPS-SALARY-2026` | Indeed/Milkround Operations Analyst salary snapshots | Platform estimates mix experience; exact sample set incomplete |
| `UK-BA-SALARY-2026` | [Live Digital: UK junior Business Analyst salary guide](https://live-digital.co.uk/blog/business-analyst-salary-uk/) | £24k–£33k adjacent role guide; not direct Product Ops evidence |
| `UK-CONSULTING-PROSPECTS-2026` | Prospects graduate consulting salary guide | £28k–£35k adjacency; exact page reference was not retained |
| `UK-AI-GRAD-POSTINGS-2026` | Targetjobs current Data & AI graduate examples | 2 transparent examples around £27.5k and £48.5k; neither is direct Agent Product |
| `UK-CREATIVETECH-2026` | Indeed/Glassdoor Creative Technologist snapshots | 1 transparent role and 1 aggregate; exact listing set incomplete |
| `UK-VISA-SW-2026` | [GOV.UK Skilled Worker job and salary rules](https://www.gov.uk/skilled-worker-visa/your-job), [lower salary routes](https://www.gov.uk/skilled-worker-visa/when-you-can-be-paid-less) | Eligibility only; never used to set market salary bands |

### UK statutory, cost and employer-policy refs preserved

- [GOV.UK: Graduate visa](https://www.gov.uk/graduate-visa)
- [GOV.UK: Register of licensed sponsors](https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers)
- [GOV.UK: Holiday entitlement](https://www.gov.uk/holiday-entitlement-rights/holiday-pay)
- [GOV.UK: Maximum weekly working hours](https://www.gov.uk/maximum-weekly-working-hours)
- [GOV.UK: Rest breaks](https://www.gov.uk/rest-breaks-work)
- [GOV.UK: Workplace pensions](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay)
- [GOV.UK: Statutory Sick Pay](https://www.gov.uk/statutory-sick-pay)
- [Acas: Probation periods](https://www.acas.org.uk/probation-periods)
- [ONS: Private rent and house prices](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/privaterentandhousepricesuk/latest)
- [NatWest Early Talent support](https://jobs.natwestgroup.com/pages/early-talent-application-support), [Deloitte sponsorship](https://www.deloitte.com/uk/en/careers/early-careers/work-permits-and-sponsorship.html), [KPMG international students](https://www.kpmgcareers.co.uk/graduates/how-to-apply/international-students)

---

`GLOBAL_JOB_QUALITY_MARKET_CALIBRATION_FINAL_REVIEW_READY`
