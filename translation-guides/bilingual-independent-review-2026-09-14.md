# 当前中英文独立复审：关系、对象和术语

本轮由主审与3个agent并行检查当前中英文摘要及第1—5章，分工覆盖引言/结论、方法、结果。以下判断先来自当前正文及其上下文；旧记录只用于发现后的去重，没有按旧清单逐项套用。只生成审查材料，未修改中文源稿、英文正文、表图或公式。

本报告集中交付5处值得处理的表达问题，另列1处需要区分含义的可选澄清。它们不等于5处研究结论错误，也不表示全文已经无误。前3处可以明确修清关系或术语；第4、5处涉及叙述层级与观察关系，需作者确认意图。完整检查后，已自然、含义明确的表达保留。

## 1. 英文后置补充语使并列关系不清

位置：[中文第1章27行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:27)，[英文第1章27行](D:/MS-AgentNet-English/chapters/chapter01.tex:27)。

**现有中文**

> 在模型方面，除估计性能外，模型复杂度同样直接关系到实际部署。

**建议中文**：保留。中文明确说性能、复杂度两项都与部署有关。

**现有英文**

> For models, complexity is directly related to practical deployment, in addition to estimation performance.

**建议英文**

> Both estimation performance and model complexity are directly relevant to practical deployment.

**原因及效果**：词汇简单但表达绕。原句尾部的补充语可能挂到“related to”后面，被读成复杂度与部署、估计性能这两者相关。把真正并列的两个因素放到主语中，读者立即知道谁与谁并列。未新增性能与复杂度之间的因果关系。

**范文依据**：[Engineering-AI引言108—112行](D:/MS-AgentNet-English/style-references/Engineering-AI/introduction.txt:108)的“balance engineering feasibility with accuracy”（助手释义：兼顾工程可行性与精度），以及[BMSFormer引言184—189行](D:/MS-AgentNet-English/style-references/BMSFormer/introduction.txt:184)的“balancing accuracy and efficiency”（兼顾精度与效率），均明确列出需要共同考虑的对象。本建议的具体并列关系由本文中文确定，不是从范文借用实验结论。

## 2. 英文未明确“相关性”和“表现”的对象

位置：[中文第1章36行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:36)，[英文第1章36行](D:/MS-AgentNet-English/chapters/chapter01.tex:36)。

**现有中文**

> 因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。

**建议中文**

> 因此，模型输入的确定需要结合健康指标在不同电池上与SOH的相关性表现，以及指标间的冗余关系，减少选择结果对指标在单节电池上表现的依赖。

中文结合前句可以理解，此处补对象是可选自足化，不认定原中文是病句。

**现有英文**

> Model input selection therefore needs to consider both correlations across cells and redundancy among indicators to reduce its dependence on the performance of a single cell.

**建议英文**

> Model input selection therefore needs to consider both HI–SOH correlations on different cells and redundancy among indicators to reduce its dependence on HI performance on any single cell.

**原因及效果**：“correlations across cells”容易让人理解成电池之间的相关性，而本文是在不同电池上分别计算HI与SOH的相关性；“performance of a single cell”也可能指电池自身的运行性能。补清两个对象，保留相关性、冗余与降低单池依赖这三层信息。并非字数越少越直接。

**范文依据**：[JESSOHRUL方法1317—1326行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1317)明确写“the correlation between HIs and SOH”（助手释义：HI与SOH之间的相关性）；[1419—1431行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1419)再讨论同一HI在不同电池上的相关性差异。参考的是“变量对＋评价所在电池”的对象层次，不借其阈值或数据角色。

## 3. 同一个φ先称“核函数”、后称“特征映射”

位置：[中文第3章244行](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:244)，[英文第3章244行](D:/MS-AgentNet-English/chapters/chapter03.tex:244)，与两份文件第263行的定义对照。

**现有中文**

> 针对Softmax注意力的二次计算开销，线性注意力利用核函数$\phi(\cdot)$映射查询和键，并借助矩阵乘法结合律重新组织计算顺序\cite{ref40}。第$i$个注意力头的输出可写为：

**建议中文**

> 针对Softmax注意力的二次计算开销，线性注意力利用非负特征映射$\phi(\cdot)$变换查询和键，并借助矩阵乘法结合律重新组织计算顺序\cite{ref40}。第$i$个注意力头的输出可写为：

**现有英文**

> To address the quadratic computational cost of Softmax attention, linear attention maps queries and keys through a kernel function $\phi(\cdot)$ and rearranges the computation order using the associative property of matrix multiplication\cite{ref40}. The output of the $i$th attention head can be written as:

**建议英文**

> To address the quadratic computational cost of Softmax attention, linear attention maps queries and keys through a nonnegative feature mapping $\phi(\cdot)$ and rearranges the computation order using the associative property of matrix multiplication\cite{ref40}. The output of the $i$th attention head can be written as:

**原因及效果**：这是中英共同的术语不精确，不是普通句法错误。本文公式中的φ分别接收查询、键并输出特征表示；核相似度则由两个映射后表示的内积构成。第263行已把φ定义为非负特征映射，统一第244行即可，不改公式、计算顺序、复杂度或算法。

**本轮核验的原始依据**：本文ref40即Katharopoulos等的[原论文§3.2，PDF第3页，式(4)—(6)](https://proceedings.mlr.press/v119/katharopoulos20a/katharopoulos20a.pdf)。原文区分核k(x,y)和特征表示φ(x)，并明确称φ为feature map。此技术定义优先于范文的松散简称。

**三篇范文比对**：[Engineering-AI方法711—717行](D:/MS-AgentNet-English/style-references/Engineering-AI/methodology.txt:711)用“kernel feature map”；[JESSOHRUL方法291—299行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:291)用“feature mapping operation”。[BMSFormer方法804—814行](D:/MS-AgentNet-English/style-references/BMSFormer/methodology.txt:804)确实也把φ称为kernel functions，因此不能宣称三篇一致支持原稿或一致使用精确名称。这正是范文用词不能机械继承的实例。

## 4. 总述与分述被写成连续的步骤链

位置：[中文第1章44行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:44)，[英文第1章44行](D:/MS-AgentNet-English/chapters/chapter01.tex:44)。下列仅展示贡献段中受影响的连续句，标题和末句保持原样。

**现有中文**

> 该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，再以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余。利用MS-CCCT标定其中充电时间特征的电压窗口，再通过PCC/SCC双阈值与冗余约束筛选候选指标。

**建议中文**

> 该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，并以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余。具体而言，利用MS-CCCT标定其中充电时间特征的电压窗口，再通过PCC/SCC双阈值与冗余约束筛选候选指标。

**现有英文**

> The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It then uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators. MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators.

**建议英文**

> The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators. Specifically, MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators.

**原因及效果**：词汇简单但表达绕。前面的“再/then”使读者期待严格顺序，后句却才展开标定和筛选，容易误读为先完成最终相关性/冗余评价，再回到标定。若作者本意是总述后展开，第一个“再”改为“并”，后一层加“具体而言”即可。这里不是断言实现顺序有错误，也不改变段落或新增一轮评价。

**依据**：本文[第2章特征工程完整总述及后续小节](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:43)给出了标定、准入、冗余剔除的关系。三篇范文可参考操作层次清楚的写法，但不决定本文步骤；具体原文定位见[引言分报告I-03](D:/MS-AgentNet-English/translation-guides/source-language-review-intro-2026-09-14.md)。本项英文是本文所需适配。

## 5. “局部偏离导致跟踪偏差”没有先区分真实轨迹与预测误差

位置：[中文第4章94行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:94)，[英文第4章94行](D:/MS-AgentNet-English/chapters/chapter04.tex:94)。

**现有中文**

> 值得注意的是，Cell4 的局部偏离和 Cell6 后段的快速下降使各模型表现出不同程度的跟踪偏差。

**现有英文**

> In particular, the local deviations in Cell4 and the rapid decline in the later stage of Cell6 lead to different degrees of tracking error.

**问题**：“Cell4的局部偏离”没有说明偏离的是哪条曲线、相对什么对象。若指预测偏离真实值，就成了“偏差导致偏差”；若指真实SOH局部偏离平滑趋势，则应先说清真实轨迹。英文保留了同样的对象省略。问题在对象与关系，不在deviation是否难。

主审本轮实际查看了[Cell4图](D:/MS-AgentNet-English/figures/Oxford/cell4.png)和[Cell6图](D:/MS-AgentNet-English/figures/Oxford/cell6.png)：Reference曲线分别可见局部变化及后段较快下降，支持将此处理解为真实轨迹的变化区间；图形观察不能单独证明因果机制。

**建议中文（按真实轨迹变化区间的含义）**

> 值得注意的是，在Cell4真实SOH的局部变化区间和Cell6后段快速下降区间，各模型表现出不同程度的跟踪偏差。

**建议英文**

> In particular, the models show different degrees of tracking error in regions with local changes in the true SOH of Cell4 and a rapid late-stage decline in the true SOH of Cell6.

**原因及效果**：词汇简单但表达绕。明确“真实变化区间—模型跟踪表现”这两个对象，将含糊因果改成图能直接支持的区间观察。电池、阶段和比较对象保留。由“使/lead to”改成“在/in”属于关系修订，需要确认；不能标成完全不改力度的普通换词。

**范文依据**：[BMSFormer结果1003—1008行](D:/MS-AgentNet-English/style-references/BMSFormer/results.txt:1003)分别说estimated SOH与true SOH，再联系localized magnifications；[Engineering-AI结果260—263行](D:/MS-AgentNet-English/style-references/Engineering-AI/results.txt:260)把局部现象明确叫SOH drops或knee-points；[JESSOHRUL结果112—120行](D:/MS-AgentNet-English/style-references/JESSOHRUL/results.txt:112)将短期容量波动与细节子图对应。这里只借对象和证据范围的写法，不把范文的膝点、滞后或机制解释移植进本文。

## 6. 可选澄清：“固定RAA”是固定结构，还是冻结参数？

位置：[中文第4章156行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:156)，[英文第4章156行](D:/MS-AgentNet-English/chapters/chapter04.tex:156)。

**现有中文**

> 为进一步区分多尺度 DSConv 中两个卷积尺度的作用，固定 RAA 模块并仅调整卷积尺度，设置 S0（仅保留 RAA）、S5（RAA 与核长度为 5 的 DSConv-S）、S31（RAA 与核长度为 31 的 DSConv-L）和 SFull（RAA、DSConv-S 与 DSConv-L）四种尺度变体。

**现有英文（受影响的句子）**

> To further distinguish the roles of the two convolutional scales, RAA is held fixed while only the convolutional scale is changed.

**若意指结构配置保持一致，建议局部替换**

中文：将“固定 RAA 模块并仅调整卷积尺度”改为“保持 RAA 模块的结构配置不变，仅调整卷积尺度”。

英文：

> To further distinguish the roles of the two convolutional scales, the RAA configuration is kept unchanged while only the convolutional scale is changed.

**原因及限度**：前文迁移实验明确冻结特征提取模块，此处held fixed可能被读成冻结已训练参数。当前四个变体的命名能确定RAA都保留，不能凭此证明它们的参数是否参与训练。故本项只作条件澄清，不宣告误译，也不把“每个变体从头训练”写入正文。若真实操作是冻结权重，应明确写参数冻结，而不是采用上面的结构版本。三篇范文不能代替本文训练记录作决定。

本项过去已作为可选表达提及，本轮再次独立识别后不计为全新错误。

## 本轮主动保留及检查边界

- 第3章FFN残差句的当前英文用“The result”明确进入残差相加的对象，不能再照中文省略主语的问题去改已经清楚的英文。
- DTV与DTC相邻段的对比说明自变量不同，随后“同样平滑”说明处理相同，关系成立；不机械把while、also判为冲突。
- RAA对无正得分行返回均匀分布的分支已经写明，不把一般注意力商式的分母问题重复说成RAA缺少回退分支。
- 摘要总体结果、结论域内泛化与跨域局限的主线成立；没有因个别电池不最优而否定“总体”限定。
- 没有根据范文替本文补原始实验、推定训练实现或改数值。相关系数、计算量与实测耗时的区别仍需遵守，但旧问题不在本轮反复展开。
- 三篇TXT只引用内部连续可确认的短句；不按双栏提取错序推断整篇论证顺序。φ的专业定义另核验了原始论文。未声称新做了三篇全文句长计数、重新运行实验或完成所有引文的事实核查。

本轮未修改论文，故未运行LaTeX编译。分工细节可见[引言审查](D:/MS-AgentNet-English/translation-guides/source-language-review-intro-2026-09-14.md)、[方法复核备忘](D:/MS-AgentNet-English/translation-guides/source-language-review-methods-2026-09-14.md)及[结果审查](D:/MS-AgentNet-English/translation-guides/source-language-review-results-2026-09-14.md)；最终优先级与保留/待核实判断以本汇总为准。

## 续审：中文句法与范文对应表达

作者要求继续核对中文语法后，主审与原3个agent重新从当前原段检查。以下按中文问题的性质交付，不把已出现过的发现重新计作新增数量。英文范文帮助检查主语、宾语、分组和句间推进是否清楚，不能充当中文语法规范，也不能证明本文实验正确。全程未修改论文。

### C1：实验条件占据了真正主语的位置——应修正

位置：[中文第4章137行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:137)。

中文改前（原段第一句）：

> 进一步比较相邻适配比例，CS2 和 CX2 源域从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。

中文建议：

> 进一步比较相邻适配比例，在分别以 CS2 和 CX2 为源域的设置下，适配比例从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。

现有英文，建议保留：

> A comparison of adjacent adaptation ratios shows that increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively. Increasing it from 50\% to 70\% gives smaller reductions of 0.0114 and 0.0055.

原因与效果：增加的是适配比例，“以CS2/CX2为源域”是实验条件。补回真正的变化对象后，条件、变化、结果三层关系明确。数字及原段其余内容保留。英文已经使用increasing the ratio，没有照搬这个主语错位。

范文参照：[BMSFormer结果1019—1022行](D:/MS-AgentNet-English/style-references/BMSFormer/results.txt:1019)明确写“30 % of the data from the first cell”（助手释义：第一节电池的30%数据），百分比明确修饰数据。它并非本文的适配实验；本项修正的决定性依据是本文第132行对适配比例的定义。

### C2：处理模块与被传递的表示没有区分——建议补清对象

位置：[中文第3章108行](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:108)。属于“词汇简单但表达绕”：动作主体与宾语需要读者自行补全，并非算法错误。

中文原段：

> 2. **局部分支保留。** 在SLFA中，$\mathbf X_S$同时传递至RAA分支和局部分支。局部分支对$\mathbf X_S$进行层归一化后传递至融合端，并与RAA分支建立的跨位置上下文进行融合，形成局部特征与全局信息的互补表示。

中文建议（仍为一个段落）：

> 2. **局部分支保留。** 在SLFA中，$\mathbf X_S$同时传递至RAA分支和局部分支。局部分支对$\mathbf X_S$进行层归一化，并将归一化后的表示传递至融合端；该表示与RAA分支建立的跨位置上下文进行融合，形成局部特征与全局信息的互补表示。

现有英文，建议保留：

> 2. **Local branch preservation.** In SLFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

原因与效果：原中文显式主语为“局部分支”，但传递到融合端、参与融合的是归一化后的表示。补“将归一化后的表示”“该表示”即可；无需拆段、加解释或改变网络。英文已经明确passes的宾语是the normalized representation，因此保留。

范文参照：[Engineering-AI方法836—839行](D:/MS-AgentNet-English/style-references/Engineering-AI/methodology.txt:836)明确以“the S-DSConv output”为被讨论的对象，后句说明其保留局部细节的作用；[BMSFormer方法512—521行](D:/MS-AgentNet-English/style-references/BMSFormer/methodology.txt:512)明确写“The output from LGFA module”，再描述转置和后续模块处理。助手释义分别为“S-DSConv的输出”“LGFA模块的输出”。借鉴的是明确中间结果，不借范文的满秩、梯度或模块实现结论。

同类补充：[中文第3章33行](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:33)“输入FFN，并与原特征残差相加”也可补为“FFN的输出再与原特征残差相加”。当前英文已用The result is added指明结果，建议保留；不另计一类问题。

### C3：五个指标“分别”对应三类属性，分组未写清——建议明确对应

位置：[中文第2章74行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:74)。同段变量定义、平滑窗口和曲线观察前三句均保留。

中文改前：

> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围\cite{ref64}。

中文建议：

> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9）。其中，HI5和HI7描述热响应的幅值，HI6和HI8描述特征位置，HI9描述波动范围\cite{ref64}。

现有英文：

> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted to describe the amplitude, characteristic positions, and range of variation of the thermal response\cite{ref64}.

建议英文（若同步采用分组澄清）：

> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted. HI5 and HI7 describe the amplitude of the thermal response, HI6 and HI8 describe its characteristic positions, and HI9 describes its range of variation\cite{ref64}.

原因与效果：前面按五项列举，后面按三类概括，“分别”却未说明配对规则。明确为2＋2＋1的对应，读者无需重新从五个名称中推理分组。现英文没有使用respectively，不能说它有同样的逐项对应错误；若只作最小中文修复，也可删除中文“分别”而保留英文。

范文参照：[JESSOHRUL方法1449—1457行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1449)明确逐项列峰、峰位、谷、谷位，例如“the voltage corresponding to the peak (HI6)”（助手释义：峰对应的电压HI6），随后整体说明作用。范文没有本文HI9，不能说它给出了本文的五指标分组；具体2＋2＋1关系来自本文定义。

### C4：“两个层面……分别……”能理解，不判为语病——可选直接性改善

位置：[中文第1章42行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:42)。

中文原段：

> 为应对上述挑战，本文提出一种以MS-AgentNet为核心的锂离子电池SOH估计框架。该框架从健康指标构建和轻量模型设计两个层面展开，分别通过组级标定与筛选提高模型输入的跨电池稳定性，并以较低计算开销提取局部变化和长期趋势，主要贡献如下。

中文可选建议：

> 为应对上述挑战，本文提出一种以MS-AgentNet为核心的锂离子电池SOH估计框架。该框架从健康指标构建和轻量模型设计两个层面展开，通过组级标定与筛选提高模型输入的跨电池稳定性，并通过MS-AgentNet以较低计算开销提取局部变化和长期趋势。主要贡献如下。

现有英文：

> To address these challenges, this paper proposes a lithium-ion battery SOH estimation framework built around MS-AgentNet. The framework addresses health indicator construction and lightweight model design: group-level calibration and selection improve the cross-cell stability of model inputs, while local variations and long-term trends are extracted with low computational overhead. The main contributions are as follows.

英文可选建议：只将第二项改为“while MS-AgentNet extracts local variations and long-term trends with low computational overhead”，其余保留。

原因与效果：原句的“分别”可以统摄两项动作，主体也可由上下文理解，不应认定语法错误。可选修改让“组级标定筛选做什么”和“MS-AgentNet做什么”更直接对应两个层面；不是因为被动句一律不好，也不是强迫所有句子句式平行。

范文参照：本批重新读取[JESSOHRUL引言169—187行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:169)，其“First, in terms of joint modeling”与“Second, for accuracy enhancement”（助手释义：首先在联合建模方面；其次在精度提升方面）明确提示各方面讨论什么。另重读Engineering-AI引言108—112行、BMSFormer引言184—189行的模型目标段。只借鉴方面与动作对应清楚，不继承联合SOH–RUL任务或额外机制。

### 这次比对后保留的句间关系

- 第1章15—17行从循环网络串行计算限制转到Transformer，最近的指代对象明确；“为解决这一问题”在该上下文成立。
- 第2章先对比DTV与DTC的自变量域，再说明二者都作平滑，分别属于方法差异和处理共同点；转折与“同样”没有逻辑冲突。
- 第4章开头先总列实验，再说明各实验用途，最后概括总体评价，段落功能成立。抽象名词略多是直接性问题，不能单凭范文句数更少就删句或认定语法错误。
- 英文已补清主语或对象的地方保留。中文存在省略，不等于英文一定有错；英文流畅，也不等于原中文的关系一定严密。

本批所有中文修改均是建议，未写入冻结源稿。范文证据来自本批重新读取的对应TXT完整短段；只引用可确认连续的短句，不以双栏错序作为句间推进证据，也未声称完成新的全文句长计数。
