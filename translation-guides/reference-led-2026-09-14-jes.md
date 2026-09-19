# JESSOHRUL 全文学习与第四章语言复核

日期：2026-09-14。仅审校记录，不修改论文。此分报告负责 JESSOHRUL 完整阅读、结果表达、英文第四章的直接性；三篇交叉校准由主审汇总，不将单篇结论冒充三篇一致意见。

## 1. 实际阅读覆盖

- 本轮从头至 EOF 分五段完整读取 `style-references/JESSOHRUL/full.txt`，共 4371 行，覆盖 PDF 第 1-26 页，包括方法、实验、结果、结论和参考文献；并非复用旧词表代替阅读。
- 完整通读当前 `chapters/abstract.tex` 和 `chapter01.tex` 至 `chapter05.tex`；完整阅读 `terminology.md`、`usage-guide.md`、`house-style.md`、`expression-detail-rules.md`。截断输出已补读。
- 第四章候选逐项核对冻结中文完整段落；不把旧统计或实验口径待核项重新归类成语言错误。
- 按 PDF 技能渲染并查看 JESSOHRUL **第 15 页完整页面**，确认 §4 开段、§4.1 HI 比较段、§4.2 与 §4.2.1 的双栏阅读顺序。尤其 TXT 将右栏 HI 比较续段排到 §4 标题前；下面逐句记录按 PDF 实际段落，不按 TXT 相邻行拼接。

原文：[JESSOHRUL PDF](D:/MS-AgentNet-English/style-references/JESSOHRUL/source.pdf)；[全文 TXT](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt)。

## 2. 一段完整、可复现的逐句分析

范围：PDF 第 15 页右栏顶部，§4.1 最后一段；起于 “Furthermore, Table 7 also reveals”，止于 “generalization and robustness.”。TXT 第 1885-1893 行附近。上一段以 Fusion 排名说明总体相关性影响估计精度，本段从同一 HI 的跨电池差异推进到组级筛选。

计词规则：恢复行内断词，空白分词，带连字符的 correlation-based 计 1 词，Table 7 计 2 词，缩写与电池标识各计 1 词；逗号不分句。本段 4 句、87 词。

| ID | 原句 | 词数 | 主句主语 / 时态语态 | 功能与推进 |
| --- | --- | ---: | --- | --- |
| J1 | Furthermore, Table 7 also reveals that the representational ability of the same HI varies significantly across different batteries. | 18 | Table 7 / 一般现在时、主动 | 结果；由总体精度转向跨电池变化 |
| J2 | For example, the DTC feature performs significantly better than the IC feature on Cell5, whereas the opposite is observed for Cell3. | 21 | the DTC feature / 现在时、主动；whereas 从句被动 | 结果；用电池间相反排序举例，语态切换服务于焦点 |
| J3 | However, the CVT feature, extracted using the proposed strong correlation-based HI selection method for battery groups, consistently achieves the best performance across all batteries. | 24 | the CVT feature / 现在时、主动；extracted 为过去分词修饰，非过去时主句 | 混合：结果 + 筛选方法限定；对比组级特征 |
| J4 | Therefore, considering the correlation of health indicators across all battery data is essential, as it greatly contributes to enhancing the model's generalization and robustness. | 24 | considering ... / 现在时、系表；as 从句主动 | 解释；由结果归纳组级相关性价值 |

句长为 18、21、24、24，均值 21.75，中位数 22.5，范围 18-24。方法纯句 0/4、0/87；结果纯句 2/4、39/87（44.83%）；方法 + 结果混合句单列 1/4、24/87（27.59%）；解释句 1/4、24/87（27.59%）。不把混合句同时算进两个互斥比例，也不将本段比例称作整篇论文比例。

可学的是“同一 HI 的跨电池差异 → 一对具体反例 → 组级特征的对比结果 → 含义”。不是四句配额，也不是全抄 Furthermore/However/Therefore；本文目前已用 Moreover、For example、In contrast 和具体结果自然推进。

## 3. 可适配的句式，不是整句套用

| 功能 | 改编句式 | 本轮定位的原文语境 | 本文适配与边界 |
| --- | --- | --- | --- |
| HI 提取 | `[HIs] are extracted from [curves/data].` | §3.5.1，第 11-13 页，从四类曲线到十个 HIs；TXT 1570 行以后 | 只替换本文实际 15 个候选及其来源；提取与筛选不能互换 |
| HI 筛选 | `The retained HIs are ranked by [criterion], and [redundant HIs] are removed.` | §3.5.2，第 14 页，准入后排序与去冗余完整说明 | 保留本文自己的双阈值、排序得分和冗余逻辑；不得复制范文阈值或表 5 条件符号 |
| 跨电池差异 | `[HI A] yields lower errors than [HI B] on [cell], whereas the opposite is observed on [other cell].` | §4.1，第 15 页完整代表段 J2 | 本文第四章 HI9/HI11 在 Cell7/Cell8 的现有句已采用该结构；保留，不再换词 |
| 结果与范围 | `[Model/HI] achieves [metric/result] across [defined cells].` | §4.1，第 15 页 J3；§4.2.1，第 15-16 页比较段 | 对象直接作主语；保留具体指标、范围，不将本文部分最好改成全部最优 |
| 结果与解释分开 | `[Concrete comparison]. These results show [bounded interpretation].` | §4.2.1，第 15 页图示分析段及第 16 页量化结果 | 本文用 show，不继承范文的 superior、exceptional 或额外部署主张；结论必须以本文结果为准 |

这些句式足以支持日常动词 extract、retain、rank、remove、yield、achieve、show。术语仍以既有术语表为准，例如本文固定 representational capability，不因范文有 representational ability 就轮换译名。

## 4. 本文候选：同句重复的最小删减

### J-C1 初始化解释：可选删冗余，非语法错误

位置：[chapter04.tex:61](D:/MS-AgentNet-English/chapters/chapter04.tex:61)。完整所在英文段：

> where $A_{ij}$ is the parameter of the $i$th agent in the $j$th feature dimension. This initialization gives different agents small, nonidentical initial parameters, avoiding identical initial states.

建议英文（保留同一段）：

> where $A_{ij}$ is the parameter of the $i$th agent in the $j$th feature dimension. This initialization gives different agents small, nonidentical initial parameters.

对应冻结中文完整段：

> 式中，$A_{ij}$ 表示第 $i$ 个智能体在第 $j$ 维特征上的参数。该初始化能够为不同智能体提供幅值较小且非一致的初始参数，避免其处于完全相同的初始状态。

中文可删除的仅为“避免其处于完全相同的初始状态”：该句语境中已由“非一致的初始参数”表达；不删除小幅、不删除不同智能体，也不删上一段的均值 0、标准差 0.02、静态可学习矩阵、输入无关或智能体数 2。此处是“词汇简单但表达重复”，不是长术语不规范。

范文尺度：JESSOHRUL 并非本句初始化依据，未找到与本文静态智能体初始化同条件的说明，不能虚称“范文同样如此”。范文 §2.2.2 甚至有两次复述 depthwise/pointwise 分解的同句重复，故“发表过”不等于值得照搬；该处 TXT 尚未经本轮 PDF 核实，不据此认定范文错误。主审应结合 Engineering-AI 对应代理参数语境，才能把候选纳入三篇校准后的建议清单。此分报告判定为低优先级可选删减，不是已批准修改。

## 5. 明确保留的候选

### J-R1 第四章开段末句不作为必删冗余

现有句：`Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.`

建议：保留。中文对应“综合上述多维度实验结果，可全面验证……有效性与适用性”。本段首句总体评价，接着分述 HI、比较、消融复杂度及迁移任务，末句把这些任务归拢到 effectiveness/applicability。PDF 第 15 页 §4 完整开段采用完全相同的组织功能：总体评价 → 三类实验 → 分别说明用途 → Collectively 收束准确性和实际适用性。本文首尾略有信息重合，但语境功能成立；用户不要求过度细节，不能把还能压短当作错误。也不照搬范文更强的 rigorous、thorough validation。

### J-R2 不将术语重复误判为中文冗余

第四章反复使用 MAE、MAPE、RMSE、combined average error、HI1、RAA、DSConv-S、DSConv-L，均需保持对象稳定。范文 §4.1-4.4 同样反复使用相同指标/模型名称。删除其中任何指标或把 combined average error 改成笼统 error 都可能丢失比较对象。保留 necessary model/cell names；只在上下文唯一时使用 its、the model 等自然指代。

### J-R3 时态语态按功能一致，不全篇统一

当前第四章方法设置、表图结果以一般现在时为主；selected、initialized、measured 等为被动结构，和结果主动句自然衔接；未发现本次需确认为错误的时态跳变。第二章原始老化试验用过去时，第三章模块操作用现在时，摘要的 We compared 为已完成验证，结果 show 为当前呈现，功能不同可并存。

范文第 15 页 §4.1 用现在时选择 HIs，§4.2.1 用过去时交代所做实验，随后图表结果用现在时；同页 J2 主动和被动并存。因此不能以范文局部过去时为由要求本文所有实验现在时改过去时，更不能把过去分词 extracted 当作时态冲突。

### J-R4 专有名词与美式拼写

本轮通读未发现正文中需新增纠正的 modeling/generalization/behavior 英美拼写混用。范文对 health indicator/feature、SOH estimation/prediction、representational ability/capacity 的变化不构成本文随意轮换的理由；本文保持既定术语。静态可学习矩阵不是固定不可训练矩阵，source-only evaluation 不是 few-shot adaptation，计算效率不是 energy efficiency；不以简单词替换这些必要概念。

## 6. 结论

本分区没有新增明确语法、时态语态或专名错误；1 项同句冗余可选删减待主审跨参考校准。主要结果表达已能用具体对象和日常动词直接推进。完整范文阅读亦显示其有长句、重复总述和不同语态，不应机械套入其全部文字。正文及冻结中文均未改动。
