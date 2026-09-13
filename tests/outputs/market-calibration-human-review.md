# 市场校准读取示例｜Human Review v0.1.3

真实 dated research + 合成岗位输入。研究捕获日期为 2026-09-13；以下岗位、工资、资格、团队情况及 cycle review 均为 SYNTHETIC，不是真实 Offer。没有联网刷新。薪资数据 FULL 2/60、PARTIAL 58/60；FULL 也不代表统计分位数。

[执行 trace](market-calibration-trace.json) 保留输入、原始 CSV 行定位、review 与实际 helper 输出；[规则及来源入口](../../rules/market-calibration.md) 可追到原件及 source ledger。

| 示例 | 合成实际 fixed base | Dated common band | 结果与限制 |
|---|---|---|---|
| PARTIAL China：杭州产品 | RMB 12k/月，税前 | 9k–15k | WITHIN_DIRECTIONAL_BAND；PARTIAL / MEDIUM-LOW |
| FULL London Product | GBP 35k/年，税前 | £32k–£40k | WITHIN_DIRECTIONAL_BAND；FULL / MEDIUM |
| FULL London Research | GBP 35k/年，税前 | £32k–£40k | WITHIN_DIRECTIONAL_BAND；FULL / MEDIUM |
| UK salary-path 问题 | GBP 35k/年，税前 | £32k–£40k | 市场区间内；eligibility 独立 VERIFY |
| 高薪但工作条件差 | RMB 30k/月，税前 | 9k–15k | ABOVE_DIRECTIONAL_BAND；加班、管理风险及资格失败仍保留 |
| London Product Prototyping | GBP 38k/年，税前 | INSUFFICIENT DATA | INSUFFICIENT_REFERENCE_DATA；不借用相邻角色数字 |
| 旧招聘周期记录 | RMB 12k/月，税前 | 历史 9k–15k | STALE_RECHECK_REQUIRED；不作当前 band 判断 |

## 如何据此做决定

China 的 12k 只是在杭州、对应 campus/master route 的 dated common interval 内。PARTIAL 的精确岗位集没有保留，不能称为市场中位数或据此自动 Apply。可继续看职责价值、实际生活成本、休息和团队证据。

London Product 与 Research 的 FULL 来源可追溯性更强，但仍包含职业指南和混合样本。“Within”不是统计排名，也不能推广到 Bristol 或不匹配的职责／route。所有比较都保留 2026-09-13 capture date；cycle review 只允许 dated context 使用，不认证市场仍然新鲜。

UK salary-path 示例只假设未来某条 sponsorship 路线的适用门槛核验发现 shortfall；未读取旧指南金额计算，也不声称今天的法律门槛。Market salary 可以正常，eligibility 仍 VERIFY。六个 gate（现有权利、licence、具体岗位支持、occupation/duties、salary、timing）需要 fresh authority evidence。确认某路线失败也不等于所有合法路线均失败。

高薪案例仍保留长期加班、管理风险和合成资格失败，不生成 Apply 指令。正式当前 Offer 的 actual base 作为事实输入保留，dated estimate 不覆盖它。可观薪资不能抹掉 genuine gap 或坏工作条件。

Product Prototyping 返回 INSUFFICIENT_REFERENCE_DATA；中国原表保留的相邻数字也不得冒充该角色的精确工资基准。先看真实 duties 和公布待遇，不因数据弱而丢弃能力假设。

Stale 案例在合成的 2027 招聘周期查看旧记录，要求重新校准，不静默输出 current band。没有任何统一 TTL；其他示例使用显式 cycle usability review，也只得到 DATED_CONTEXT_ONLY。

## 福利与准备边界

福利分 China / UK 读取，共 19 个维度、38 个市场 context。原表未提供逐行 confidence / trace audit，因此明确 UNKNOWN_NOT_SUPPLIED / NOT_ASSESSED。不按“五险一金”和“pension”等标签数量比较；实际基数、可取得性、工时、可休假、合同与生活成本才影响价值。

中国年假保留已接受的 dated 解释：符合条件的 early-career 法定起点可能约 5 天；10–15 天高于该起点，市场普及度 VERIFY。个人强偏好不变，不能称为 above-market demanding；本轮不验证当前法律适用性。

准备阶段只携带决策问题：固定工资口径、真实工作条件、必要工作权条件。没有新 CV claims、完整材料包或自动谈薪。Market Benchmark 从不作为 Candidate Evidence。

这些例子验证 reference integration 与边界；未执行独立模型 benchmark，也未验证真实 JD、签证、工资或法律。

`CAREER_INTELLIGENCE_V013_MARKET_CALIBRATION_HUMAN_REVIEW_READY`
