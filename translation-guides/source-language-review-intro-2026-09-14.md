# 中英文独立复查：摘要、引言、结论

日期：2026-09-14。仅提供建议，未修改中文源稿或英文论文。本文根据当前中英文重新检查句间关系、修饰范围、相关对象和步骤层次；旧报告只用于事后去重。本轮不重复计入“实时性受到限制”“线性复杂度限定”“传统机器学习整体局限”等旧项。

通读了中英摘要及第1—5章，重点逐段检查摘要、第1章、第5章。重读三篇范文的摘要、引言、结论对应正文；TXT含跨栏错序时，不把相邻提取行直接当作连续论证。下列证据来自本轮重读的完整相关段落；只引用没有跨栏拼接疑义的短语。未声称完成外部引文事实审计，也未重新统计三篇全文句长。

本轮新增3项：1项英文并列关系表达不清，1项英文省略相关对象，1项中英总述—分述层次不清。后两项是可消除的误读风险，不认定算法实现或实验结果错误。

## I-01：英文把“两个因素都与部署相关”写成了可能错挂的补充语

位置：[中文第1章27行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:27)；[英文第1章27行](D:/MS-AgentNet-English/chapters/chapter01.tex:27)。

分类：英文独有的并列关系不清；词汇简单但表达绕。中文关系成立，保留。

现有中文：

> 在模型方面，除估计性能外，模型复杂度同样直接关系到实际部署。

建议中文：保留原句。两个需要考虑的对象是“估计性能”和“模型复杂度”。

现有英文：

> For models, complexity is directly related to practical deployment, in addition to estimation performance.

建议英文：

> Both estimation performance and model complexity are directly relevant to practical deployment.

原因与改后效果：原英文的 `in addition to estimation performance` 放在 `related to practical deployment` 之后，读者容易把它理解为“复杂度除了与估计性能相关，也与实际部署相关”，从而改变中文的并列对象。把两项直接置于 `Both ... and ...` 的主语中，立即交代什么共同关系到部署。不增加“性能提高由复杂度增加导致”等因果，也不把部署目标改成已完成部署。此处不是单纯把词换简单。

范文依据：[Engineering-AI引言108—112行](D:/MS-AgentNet-English/style-references/Engineering-AI/introduction.txt:108)中使用 `balance engineering feasibility with accuracy`（兼顾工程可行性与精度），明确列出要兼顾的两个对象；[BMSFormer引言184—189行](D:/MS-AgentNet-English/style-references/BMSFormer/introduction.txt:184)同样直接写 `balancing accuracy and efficiency`（兼顾精度与效率）。两处只支持清楚列出并列因素，不是本文指标或部署结论的证据。建议英文是针对本文句义的改写，不是范文整句。

## I-02：英文的“correlations across cells”没有说清谁与谁相关

位置：[中文第1章36行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:36)；[英文第1章36行](D:/MS-AgentNet-English/chapters/chapter01.tex:36)。

分类：英文相关对象省略造成的歧义；中文可保留。不是判定本文计算了错误的相关系数。

现有中文：

> 因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。

建议中文：保留。这里的“不同电池上的”结合前文“候选健康指标与SOH之间的关联”能够回指正确对象；如需自足化，可仅补为“不同电池上健康指标与SOH的相关性表现”。

现有英文：

> Model input selection therefore needs to consider both correlations across cells and redundancy among indicators to reduce its dependence on the performance of a single cell.

建议英文：

> Model input selection therefore needs to consider both HI–SOH correlations on different cells and redundancy among indicators to reduce its dependence on HI performance on any single cell.

原因与改后效果：`correlations across cells` 可以被理解为不同电池之间的相关性，实际需要表达的是在不同电池上分别评价HI与SOH的相关性。后面的 `performance of a single cell` 也省略了表现的对象，容易理解成电池自身性能；补回HI后，两处关系均明确。保留了跨电池考察、指标冗余与减少单池依赖三项信息；这项修改略增加字数，但更直接且更准确。

范文依据：[JESSOHRUL方法1317—1326行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1317)直接写 `the correlation between HIs and SOH`（HI与SOH之间的相关性）；[1419—1431行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1419)逐一讨论同一HI在不同电池上的相关性差异。借鉴的是“先明确相关变量，再明确在哪些电池上评价”的表达方式。本文两池开发集合和具体筛选规则仍来自本文，不继承范文的电池数量或阈值。

## I-03：“先提取—再评价—标定—再筛选”没有标明后句是在展开前句

位置：[中文第1章44行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:44)；[英文第1章44行](D:/MS-AgentNet-English/chapters/chapter01.tex:44)。

分类：中英共同的总述—分述层次不清；词汇简单但表达绕。最小修复是标出展开关系，不调整段落或实际算法。

现有中文（贡献标题之后、末句之前的两句）：

> 该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，再以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余。利用MS-CCCT标定其中充电时间特征的电压窗口，再通过PCC/SCC双阈值与冗余约束筛选候选指标。

建议中文：

> 该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，并以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余。具体而言，利用MS-CCCT标定其中充电时间特征的电压窗口，再通过PCC/SCC双阈值与冗余约束筛选候选指标。

现有英文：

> The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It then uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators. MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators.

建议英文：

> The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators. Specifically, MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators.

原因与改后效果：原中文“首先—再”及英文 `first—then` 形成了顺序期待，但下一句才开始交代标定和筛选，读者可能误以为标定前已经完成了一轮最终HI相关性与冗余评价，之后又重做一轮。第2章实际是将标定、准入、冗余剔除作为输入优化流程的内部步骤。删去总括句的强顺序标记、加“具体而言/Specifically”，读者就知道后面是在展开总括操作，而非无说明地回到前一步。原文在充分上下文下可以理解，因此本项不称为确定的算法顺序错误，也不主张添加额外评价步骤。

范文依据：[JESSOHRUL摘要41—43行](D:/MS-AgentNet-English/style-references/JESSOHRUL/abstract.txt:41)在“提取多类HI”后用 `and then` 引出筛选，时间连接词对应实际操作顺序；[Engineering-AI摘要36—38行](D:/MS-AgentNet-English/style-references/Engineering-AI/abstract.txt:36)也以 `First` 和 `Subsequently` 区分特征处理与网络介绍。参考价值是让顺序词有清楚的操作层级；`Specifically` 并非从这些原句照抄，本文标定—筛选的关系以[中文第2章44行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:44)及其完整对应小节为依据。

## 已检查并保留

- 摘要主线“问题—HI方法—网络—比较—总体结果”成立。没有为凑数将所有长句、被动句或连接词列为错误。摘要中 `many existing ... often` 有轻微量词重复，但优先级较低，本轮不另列一项；该句的证据范围问题也不能靠删一个词解决。
- 第1章15—17行的CNN—RNN—Transformer过渡，最近先行项是串行计算限制，不能强行读成Transformer专为电池SOH提出。
- 第1章25行明确“增加候选指标并不必然提高精度”，后续列举弱表征、跨池不稳定与冗余，并用“可能、帮助”限定，逻辑本身可保留。
- 第5章三段中方法总结、总体结果、局限与未来工作关系合理。本轮没有新的确定结论段语言问题。跨数据集限制未被写成所有方向已解决，嵌入式平台仍属于未来验证。

三项建议均需作者确认后才进入英文工作稿；冻结中文只展示建议，不写入源文件。

