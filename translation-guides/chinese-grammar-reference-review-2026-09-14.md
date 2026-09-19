# 中文语法与范文对照审查记录

状态：待作者确认，仅保存审查建议，未修改中英文论文。

本文件单独保存上一批C1—C4及其范文依据；后续继续核对的结果追加在文末。原综合报告保留，后续中文语法建议以本文件更新为准。保存建议不表示作者已批准写入论文。

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

## 保存后继续核对：方法、曲线和指标的对象层次

以下从当前第2章及其英文对应段出发重新检查，不沿旧发现清单逐项套用。重点是同一段内“分析方法”“曲线”“具体指标”能否清楚衔接。范文只提供表达参照。

### C5：先说“曲线”，后用“该方法”承接——可选对象一致性修复

位置：[中文第2章60行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:60)，[现有英文](D:/MS-AgentNet-English/chapters/chapter02.tex:60)。

完整中文原段：

> 除充电时序特征外，容量随电压的变化同样包含电池退化信息。增量容量（IC）曲线是解析电池电化学退化的经典分析手段。该方法对容量关于电压求导，将平缓的充电电压平台转化为辨识度更高的特征峰，其位置与形状会随电池老化发生变化\cite{ref50,ref64}。IC 的具体表达式为：

建议中文：

> 除充电时序特征外，容量随电压的变化同样包含电池退化信息。增量容量（IC）分析是解析电池电化学退化的经典手段。该方法对容量关于电压求导，将平缓的充电电压平台转化为辨识度更高的特征峰，其位置与形状会随电池老化发生变化\cite{ref50,ref64}。IC 的具体表达式为：

现有英文：

> In addition to charge timing features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:

建议英文：

> In addition to charge timing features, changes in capacity with voltage also contain battery degradation information. Incremental capacity (IC) analysis is a well-established method for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, this method converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:

原因及效果：原中文用“曲线”代指“曲线分析方法”，属于可以理解的转喻，不能直接宣告科学错误。但紧接着“该方法求导”时，讨论对象从曲线跳到了生成曲线的分析方法；英文it的最近先行项同样是curve。用“IC分析”引出、用“该方法/this method”承接，读者无需转换对象。公式、特征峰及老化变化等内容全部保留。此项属可选直接性改善，不是必须增加解释或重写整段的理由。

本批范文依据：重新读取[JESSOHRUL方法1221—1236行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1221)的特征工程总述及IC完整定义段，原文先说“Incremental Capacity (IC) analysis is a diagnostic technique”，再说“The IC curve is obtained by computing the derivative”。助手释义：IC分析是一种诊断技术；IC曲线由求导获得。这明确区分方法与其产物，直接支持本项对象澄清。

另重新读取[Engineering-AI引言161—181行](D:/MS-AgentNet-English/style-references/Engineering-AI/introduction.txt:161)，其使用Incremental Capacity Analysis称呼分析方法；[BMSFormer方法218—236行](D:/MS-AgentNet-English/style-references/BMSFormer/methodology.txt:218)主要讨论充放电窗口和时间指标，未提供同功能的IC定义原句，不能硬凑其为第三份直接证据。后者跨栏未连续处不拼接引用。

### C6：曲线类别与15项具体特征没有明确分层——可选澄清，英文保留

位置：[中文第2章145行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:145)，[现有英文](D:/MS-AgentNet-English/chapters/chapter02.tex:145)。

完整中文原段：

> 健康指标筛选是锂离子电池 SOH 估计中的关键步骤\cite{ref60,ref61,ref62}，所选指标的质量直接影响最终估计精度。在前述 HI1 窗口标定的基础上，将恒流充电时间、IC、DTV、DTC、窗口放电容量和能量效率等 15 项特征共同作为候选健康指标。沿用前述组级相关性评价方式，分别计算各候选指标与 SOH 之间以及不同候选指标之间的 PCC 和 SCC。

建议中文（只修第二句，仍为原段）：

> 健康指标筛选是锂离子电池 SOH 估计中的关键步骤\cite{ref60,ref61,ref62}，所选指标的质量直接影响最终估计精度。在前述 HI1 窗口标定的基础上，将基于恒流充电时间、IC、DTV、DTC、窗口放电容量和能量效率构建的 15 项特征共同作为候选健康指标。沿用前述组级相关性评价方式，分别计算各候选指标与 SOH 之间以及不同候选指标之间的 PCC 和 SCC。

现有英文，建议保留：

> HI selection is a key step in lithium-ion battery SOH estimation\cite{ref60,ref61,ref62}, as the quality of the selected indicators directly affects the final estimation accuracy. Following HI1 window calibration, 15 features based on constant current charge time, IC, DTV, DTC, discharge capacity within a voltage window, and energy efficiency are considered as candidate HIs. Using the same group-level correlation evaluation, PCC and SCC are calculated both between each candidate HI and SOH and between different candidate HIs.

原因与效果：IC、DTV、DTC各自对应多个具体指标，原中文容易把“从什么构建”与“构建了多少项”放在同一列举层级。补“基于……构建的”即可。中文“等”本来允许不完整列举，因此不能仅凭列出六个名称就认定15项数量错误。表2-2实际为1＋3＋5＋3＋2＋1＝15项，与正文数量一致。英文已有15 features based on，层级清楚，无需重写。

范文依据：本批重新读取[JESSOHRUL方法1222—1230行](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1222)的完整首段：先列四类characteristic curves，再写“From these curves, ten representative HIs are extracted”（助手释义：从这些曲线中提取十项代表性健康指标）。可借鉴曲线→具体指标的层级，不借十项这一数量。本文各类数量由[表2-2](D:/MS-AgentNet-English/tables/table_2_2.tex:9)核实。

### 继续核对后的保留结论

- 第2章48行已清楚区分构建曲线、提取特征、另行计算容量与效率、形成15项指标池；不再重复改写。
- 第2章82行峰值、峰值对应容量、半峰宽分别对应HI10、HI11、HI12，三项对应顺序明确，中英文均保留。
- 本次进一步核对补充C5、C6两处可选澄清，没有把它们包装成新的确定语病或研究错误。未修改论文，也未运行编译。

## 再读PDF后的补充：C7与C8

本次逐句学习记录见[三篇范文逐句分析](D:/MS-AgentNet-English/translation-guides/reference-sentence-study-2026-09-14.md)。主审核验PDF并分析10句；方法审查agent独立复核下面两处当前中英文。C7为可选精简，C8为重复表达及程度范围待确认；不称作两处确定语法错误。

### C7：先说本节提出什么，再说用途（可选；现英文保留）

位置：[中文第2章44行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:44)，[英文第2章44行](D:/MS-AgentNet-English/chapters/chapter02.tex:44)。已重读完整段落及后续健康指标提取上下文；只建议替换首句，后续流程不变。

改前中文：

> 本节围绕 SOH 估计模型的输入构建展开，提出多源健康指标提取与优化算法。

建议中文：

> 本节提出多源健康指标提取与优化算法，用于构建 SOH 估计模型的输入。

现有英文，建议保留：

> This section presents the multi-source health indicator extraction and optimization algorithm for constructing the inputs to the SOH estimation model.

原因与效果：“围绕……展开”不是语法错误，但先交代讨论范围、再说“提出”，使实际动作延后。建议完整保留算法名称和用途，直接让“本节—提出—算法”形成主干。属于“词汇简单但表达绕”的最小修复；英文已经直接表达，无需为了双语对称再改。

范文依据：[JESSOHRUL PDF第11页§3.5.1](D:/MS-AgentNet-English/style-references/JESSOHRUL/source.pdf)完整首段，学习记录J1—J3。J1虽以In this section开头，随即明确数据被处理以生成曲线；J2承接曲线说指标提取。依据支持尽早出现实际动作，不支持机械禁止“本节”或要求中文模仿英文被动句。

### C8：计算开销与计算负载重复，且中英文程度范围需要核实

位置：[中文第3章57行](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:57)，[英文第3章57行](D:/MS-AgentNet-English/chapters/chapter03.tex:57)。已重读卷积介绍完整段落、计算量公式及后续DSConv对比。以下只处理该段第三句，不变更段落结构、公式和训练时间结论。

改前中文：

> 随着输入通道数、输出通道数和卷积核尺寸增加，其参数量与计算开销迅速累积，显著推高计算负载并延长训练时间。

现有英文：

> As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time.

判断：本段没有定义“计算开销”和“计算负载”为两个不同计量对象，因此“开销增加，导致负载增加”重复说明同一负担。训练时间是另一项信息，必须保留。另有中英文力度风险：英文substantially increasing同时作用于computational load和training time；中文“显著”的范围不能仅凭此句确定。

保留现英文力度的候选（仅在作者原意为训练时间也显著延长时采用）：

> 随着输入通道数、输出通道数和卷积核尺寸增加，其参数量迅速增加，计算负载也迅速、大幅上升，训练时间随之显著延长。

> As the numbers of input and output channels and the kernel size increase, the parameter count grows rapidly. The computational load also rises rapidly and substantially, leading to substantially longer training time.

若中文原意只是训练时间延长、没有“显著延长”的程度判断，则上述中文删除训练时间前的“显著”，英文末尾用leading to longer training time。两个版本都保持原段，英文允许在段内分句。不能未经确认就在两种力度之间选择；也不应自行改成may、删除训练时间或增加硬件条件。

修改效果与局限：去掉计算开销和计算负载之间的循环因果，使参数量、计算负担、训练时长各有明确陈述。保留所有程度判断时，英文仍有两处substantially；这是保真候选，不宣称已得到最简终稿。作者确认程度范围后才能进一步收紧表达。

范文依据及边界：[Engineering-AI PDF第7页§4.2](D:/MS-AgentNet-English/style-references/Engineering-AI/source.pdf)完整首段E1—E3，将参数冗余／过拟合风险、应对模块设计和核尺度选择分别交代，后句推进到新内容；这支持避免用同义负担反复解释同一结论，但该段不提供本文训练时长判断的证据。另核验[BMSFormer PDF第6页§3.2.1](D:/MS-AgentNet-English/style-references/BMSFormer/source.pdf)卷积段，其computational resources and training time也是两个并列对象。范文关于时间的陈述不能证明本文实测过该关系，亦不能决定本文“显著”的范围。

本轮新增结论：C7可选、C8待确认。第2章48行现有数据→曲线→指标与容量／效率的层级继续保留；此前C2的数据对象澄清获得PDF依据，不重复计为新发现。所有建议仅存入审查文档，论文正文未改。

