# 全篇中文逻辑与中英对应：第二轮查漏报告

日期：2026-09-14。此轮由主审与3个并行agent交叉复核，分别覆盖第2–3章、第4–5章及结果表、摘要/引言与跨章关系。主审复核新发现、相关正文与表格，并重新查看所引用的三篇范文对应片段。本文是上一轮的增补与纠偏，不替代上一轮尚待确认的技术问题。

## 结论先看

**确实有遗漏，但不应把所有审查点都算作中文语法错误。** 本轮新增9个不重复的审查点：6个优先核实的逻辑/证据/实验说明问题，3个较低优先级的措辞或步骤澄清。同时，将上一轮M02“特征与自己相加”的过重定性降为可选澄清。

|优先级|编号|此次新发现|处理边界|
|---|---|---|---|
|优先核实|N-M01|CVT时间轴偏移不必然使固定电压窗时长改变|纯平移在差值中抵消；先核图/提取记录，再决定是否改为并列观察|
|优先核实|N-M02|15项统一候选与MIT电压覆盖范围之间缺适用规则|不猜排除或部分积分，不改HI13上下限|
|优先核实|S-IC01|主实验输入时间范围未明确，“长期/全局”缺实际范围对应|补真实N、步长、记录间隔；不能套用复杂度测试的N=5|
|优先核实|S-IC02|高绝对相关不直接量化敏感性或全部意义的一致性|定义所指维度；不声称实际方向反转，原文若仅指相关强度则可读|
|优先核实|SR01|消融表未定义评价电池集合|单池数值吻合只是线索，不能代替记录确认|
|优先核实|SR03|初始化/收敛统计缺重复次数及统计单元|不能从其他表或范文套入“五次”|
|最小精确化|SR02|初始化正文所列是方案均值的范围|补“平均/mean”，数字不动，不误称全部运行范围|
|可选澄清|N-M03|线性注意力矩阵商可说明逐行除法|原式惯用记号可理解，不判矩阵运算错误|
|可选且待核|N-M04|R3继承哪个搜索区域未明确|按真实实现补范围，不擅自假定嵌套R2窗口|

## 三个最直观的改前改后

### 1．已有表头就能支持的最小修改：统计对象

改前：“各方案对应的R²为0.98527～0.98645……”

建议：“三种方案的平均R²为0.98527～0.98645……”

英文对应由“Their R² values range…”改为“Their mean R² values range…”。RMSE、MAE同步明确均值，数字全部保留。原因是初始化表头明确写着mean ± SD。本轮重读的JESSOHRUL也把重复运行与结果平均写明；只借其说明统计对象的方式，不继承次数或强结论。完整对照见SR02。

### 2．不能按普通润色直接实施：曲线位置与时长

改前：“该偏移表现为固定电压区间内的充电时长随老化持续变化。”

条件建议：“……CVT曲线沿时间轴的位置发生变化……；固定电压区间内的充电时长也随老化变化。”

原因：CCCT=t(V₂)−t(V₁)，若两个时刻同时增加相同数值，差不变。建议把等同关系改成并列观察，**但必须先确认确有时长变化，而且需确认原文‘持续’的意图**，不能借修改连接词掩盖未核实观察。范文支持直接描述电压窗内时长，不证明本文图形。完整中英对照见N-M01。

### 3．不是换一个连接词就能解决：消融统计范围

改前：仅写“在CX2和Oxford数据集上的综合平均误差……”。

建议效果：保留结果和数字，在协议段说明各数据集实际评价电池；如有多节，再交代如何聚合。

原因：表4-10部分M4结果与主比较中的单节测试电池吻合，不能默认等同两节平均；Oxford范围也不能从表中猜出。Engineering-AI宏观消融表题直接写NASA B0005，可参考其明确对象的做法，不能照搬电池。完整条件模板见SR01。

## 对上一轮判断的纠偏

1. **M02降级**：中文“经……后输入……并与……”可自然承接处理结果，不必然意味着X''与自身相加。原来的标题过强。若需要可以补“FFN输出”以降低省略歧义；现英文“The result”已清楚，应保留。
2. **M01不判当前英文错误**：中文5项与3类性质的对应可以更明确，但英文没有respectively，已经避免一一对应暗示，分组扩写不是必改。
3. **S-IC02补充证据边界**：原文没有明说映射方向、斜率、截距相同。反例只能说明绝对相关无法证明这些，不代表实际数据发生反转；若“跨电池一致性”只是相关强度的简称，原句可以理解。
4. **X02继续可选**：若数据介绍句概括全文包括跨域实验，可以结合后文理解，不强制改成仅谈域内。
5. **已有的谨慎表述保留**：总体较优不等于每项均最优；局部图观察不因整体指标不足而全部撤销；潜在部署不等于声称已完成部署；四头/四层原文已明确只是数值对应。不增加这些假警报。

## 范文依据怎么用

所有具体条目均区分“范文表达参照”和“本文自身证据”。范文帮助判断对象如何写明、条件如何交代，不能代替本文实验记录，也不能证明本文技术结论。没有直接对应范文时明确说明，尤其是矩阵维度与纯平移反例，不硬找一句范文当背书。未将双栏TXT跨段错序拼成连续论证；本轮未声称重新渲染范文PDF或读取训练代码、原始曲线数据。

## 下一步处理顺序与未完成核验

- SR02可在作者批准后作最小文字精确化；N-M03是否补写由清晰度需求决定。
- 其余条件项先核实际含义、图/数据或实验设置，再给最终定稿，不将方括号模板写进论文。
- 上一轮DSConv维度与成本、筛选量词、数据隔离、协议表文一致性等未确认项仍有效，本轮没有将它们视为已解决。
- 多轮交叉审查降低遗漏风险，但不能保证零遗漏。未核训练实现、原始数据、所有外部引用及实际图中观察，属于本轮明确边界。

## 文件保护

本轮只创建审查报告，未修改论文。对source-zh、chapters、tables、figures、backmatter在本轮前后进行逐文件哈希比较，完全一致。没有重新编译或改动PDF。上一轮报告保留：
[第一轮完整报告](D:/MS-AgentNet-English/translation-guides/chinese-logic-audit-2026-09-14.md)。

以下完整收录三个独立复核附录，含原句、条件性中英文建议、修改原因、可定位范文依据及保留项，方便在一个新文档内阅读全文。

---

## 附录1

# 中文逻辑二次查漏：第2–3章（2026-09-14）

本轮只读复核中文及对应英文第2–3章、表2_1–2_6及筛选步骤表，然后对照上一轮methods报告。没有修改论文，没有检查训练代码或原始数据，不把复现细节缺失全部归为语法错误。新增4项：2项需作者核实的逻辑/适用范围，2项低优先级表意补充；同时收窄旧M02的定性。

## N-M01：曲线沿时间轴“偏移”不必然等于窗口时长改变

位置：[中文第2章L52](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:52)，[英文同段](D:/MS-AgentNet-English/chapters/chapter02.tex:52)。

中文改前：
> 随循环推进，CVT 曲线沿时间轴逐渐偏移，如\cref{fig:2-3}(a)所示。该偏移表现为固定电压区间内的充电时长随老化持续变化。

现英文：
> As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). This shift appears as a continuous change in charge duration within a fixed voltage interval as the battery ages.

问题：按紧接着的CCCT=t(V2)−t(V1)，若曲线仅作时间轴平移，即两端时刻都增加c，时长差不变。因此“偏移→时长改变”的指代连接不够精确。但“偏移”在中文中也可能泛指曲线形态改变，不能据此认定数据或HI定义错误。

条件建议（若图/提取记录确实显示窗口时长变化，保留两个观察而不把第二个说成纯平移结果）：
> 随循环推进，CVT曲线沿时间轴的位置发生变化，如\cref{fig:2-3}(a)所示；固定电压区间内的充电时长也随老化变化。

对应英文：
> As cycling progresses, the position of the CVT curve along the time axis changes, as shown in \cref{fig:2-3}(a); the charge duration within a fixed voltage interval also changes with aging.

效果：将未充分成立的等同关系改为并列观察。技术含义边界：不是单纯语法修复；需要作者确认两项观察及“持续”的实际含义，不擅自新增拉伸、斜率改变等机制。若原图只显示平移而无时长变化，不能采用此建议，需要回看提取数据。

范文依据：[JESSOHRUL表4，TXT L1637–1638](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1637)将特征直接定义为指定电压范围内的charge time。[BMSFormer TXT L440–459](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:440)也明确从电压片段提取时间序列。二者支持围绕“窗口内时长”描述，不证明本文图中变化；本问题的核心依据为本文自身差值公式。

## N-M02：统一15项候选与不同数据电压范围之间缺少适用规则

位置：[中文第2章L48](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:48)、[L90](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:90)、[MIT协议L37](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:37)；表2_2 HI13。

原句：
> ……形成包含15项候选健康指标的指标池……
> 本文进一步构造两个窗口放电容量候选指标，分别计算端电压由3.80 V降至3.40 V以及由3.20 V降至3.00 V过程中释放的电荷量，并记为HI13和HI14……

现英文对应：
> ...forming a pool of 15 candidate HIs...
> Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V.

内部疑点：MIT协议充电截止为3.6 V，不能按当前协议叙述完整经历3.8→3.4 V放电段。但集合积分公式仍可对实际记录落入[3.4,3.8]的部分积分，因此不能直接声称HI13在MIT上必为0、无法计算或已造成错误结果。真正缺口是：15项是否为统一定义清单；逐数据集是否排除不可完整提取的指标；还是允许按实际覆盖部分积分。现有最终MIT只选HI14/HI15不能反推前期如何处理HI13。

分支A（若确实先按完整可提取性排除）中文建议：
> 上述15项指标构成统一的候选定义清单；在每个数据集上，仅对能够按其完整定义提取的指标进行相关性筛选。

英文：
> The 15 indicators form a common list of candidate definitions. For each dataset, correlation-based selection is applied only to indicators that can be extracted according to their complete definitions.

分支B（若实际使用交集积分）中文建议：
> 窗口放电容量按实际放电记录中电压位于指定区间内的时间片段积分；当记录未覆盖完整区间时，其覆盖范围需单独说明。

英文：
> Discharge capacity within a voltage window is integrated over the recorded discharge segments whose voltages lie within the specified interval. The actual voltage coverage is reported separately when the record does not cover the full interval.

以上为条件方案，不能选择后直接写入。A补充了筛选准入，B澄清并要求报告实际定义范围，均涉及技术方法；不可静默把HI13改成3.6→3.4 V，也不可将异常项补0等处理当成既有事实。

范文对应：[Engineering-AI TXT L377–390](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:377)分数据集明确最终特征区间，L411–413说明预配置观察窗口依赖电池特征。支持明确适用范围，但范文没有规定本文对未覆盖窗口的处理。依据仍为本文MIT截止电压与HI13定义的交叉检查。

## N-M03：线性注意力矩阵商的逐行含义未显式说明（低优先级）

位置：[中文第3章L263](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:263)，前式linear_attention；现英文同位置。

中文改前：
> 其中，$\phi(\cdot)$表示非负特征映射，例如$\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$；$\mathbf 1$表示全1向量，用于计算对应的归一化项\cite{ref40}。

现英文：
> where $\phi(\cdot)$ is a nonnegative feature mapping, such as $\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$, and $\mathbf 1$ is an all-ones vector used to calculate the corresponding normalization term\cite{ref40}.

可选句末补充：
> 此处的除法表示分子各行分别除以分母中对应的标量。
> Here, division means dividing each row of the numerator by the corresponding scalar in the denominator.

理由：按本节维度，分子N×dh、分母N×1，不是一般矩阵除法。逐行缩放是可理解的惯用写法，不能把原式判为运算错误。此项只澄清记号，不改变算法。分母为0的处理仍与旧M07合并，不能借此添加epsilon。

范文：本轮查看的三个对应片段没有直接支持该补充句的原文，不硬引。依据是本文维度。一般注意力先前逐位置定义已为读者提供理解线索，所以不是必须修改项。

## N-M04：R3在哪个区域搜索可更明确（低优先级，需核实）

位置：[中文第2章L139](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:139)。

中文改前：
> R2阶段在该区域内采用0.20 V窗宽和0.05 V步长继续搜索；R3阶段进一步采用0.10 V窗宽和0.05 V步长细化搜索。

现英文：
> Stage R2 searches this region using a window width of 0.20 V and a step size of 0.05 V. Stage R3 further refines the search using a window width of 0.10 V and a step size of 0.05 V.

若R3确实限于R2得分最高窗口，建议：
> R2阶段在该区域内采用0.20 V窗宽和0.05 V步长继续搜索；R3阶段在R2得分最高的窗口内采用0.10 V窗宽和0.05 V步长细化搜索。
> Stage R2 searches this region using a window width of 0.20 V and a step size of 0.05 V. Stage R3 refines the search within the highest-scoring R2 window using a window width of 0.10 V and a step size of 0.05 V.

原因：当前R1明确把获胜窗口传给下一阶段；R2→R3仅“进一步”可由粗到细上下文推知，但没有同样明确。若R3仍搜索R1优胜区域，则上述改法错误，应写实际范围。不得仅凭“多尺度”推定嵌套规则。

范文：[BMSFormer TXT L450–457](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:450)明确将优胜段作为下一步搜索区间，再重复搜索。只支持把继承关系写清；该范文0.2步长与枚举0.1起点并不一致，不继承数值。这不是已发现实现错误，也不另报“全局最优”问题。

## 旧项再次核定

- M01保留为中文对应关系不够明确；现英文不用respectively已经避免一一对应暗示。不得把英文原句判为错译，分组版属于更明确而非必须扩写。
- M02降级：旧报告“导致特征与自己相加”的标题过强。中文“经……后输入……并与……”通常可理解为处理结果继续作主语，不必然说X''+X''。保留“可补FFN输出以减轻省略歧义”的建议；英文The result与公式一致，继续不改。
- M03成立：候选最高不保证绝对强相关；须保留Oxford实际高分作为具体结果，不能否定结果。
- M04与主报告X01合并，不双计。
- M05、M06仍需共同核定。二维成本、序列维度、比值条件不是单一换词能修复；不新增推理更快的主张。
- M07成立于一般非负相似度商；ELU+1例子理论上严格正，不能说该例子也必然有零分母。
- M08保留量词/加入时点待核。仍未从结果表推断实际程序。
- M09保留为表—文协议待核，不断言Oxford真实协议究竟是哪一个。
- M10保持可选精确化；“PCC衡量线性”本身正确。

## 本轮排除的假警报

1. R3与R2相等时已被“否则保留R2”覆盖，不报漏掉等值分支。
2. R1上界与步长可能造成尾部未覆盖，不足以认定搜索错误；本稿没有承诺覆盖连续域全部窗口，不列新增问题。
3. na=2的等效交互矩阵秩≤2，不推出整个残差RAA低秩；现稿限定正确，不重报。
4. 小核卷积保长需要相应边界配置，但未查实现，不把省略padding细节当作中文逻辑错误。
5. 不因3.6<3.8就说MIT的HI13积分必然空集。范围交集、完整窗口过程与最终入选是三个不同问题，已在N-M02区分。

## 本轮重读参考范围

Engineering-AI TXT332–426、838–853；JESSOHRUL1576–1686、1786–1849；BMSFormer426–460、671–735。只引用局部可定位语句或表项，不从双栏错序抽取跨段逻辑；没有声称本轮渲染PDF或确认曲线图形。以上参考中文解释均为助手释义。正文与方法事实的最终确认仍以作者及实际记录为准。

---

## 附录2

# 中文逻辑二次查漏：第4—5章及结果表

日期：2026-09-14。仅审查，不修改论文、源稿、表图或代码。本报告重新读取中英文第4—5章、全部 table_4*.tex 与 figure_4*.tex，再对照上轮 results、intro-conclusion 和 cross-chapter 报告，避免将旧问题重新计数。参考材料取重新读取的对应连续段落；没有重新核验原始训练数据、随机种子或绘图数据。

## 结论

本范围新增三项：一项统计对象措辞精确化、两项需要作者核实的报告信息缺失。它们不是三个已经证明的实验错误。上轮八项结果问题与结论边界不重复列为新增。

|编号|新增遗漏|性质|
|---|---|---|
|SR01|消融结果没有说明评价电池集合，且部分数值对应主比较单节电池而非数据集两节平均|需核实实验范围|
|SR02|初始化正文把三种方案的均值范围写成未限定的指标值范围|可作最小精确化|
|SR03|初始化与收敛统计没有明确重复次数、统计单元及其对应关系|需补实际统计定义|

## SR01｜消融表中的“数据集结果”究竟来自哪些电池？

位置：[中文第4章152行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:152)、[英文同段](D:/MS-AgentNet-English/chapters/chapter04.tex:152)、[表4-10](D:/MS-AgentNet-English/tables/table_4_10.tex:7)、[表4-11](D:/MS-AgentNet-English/tables/table_4_11.tex:7)。

中文原句：

> 如\cref{tab:4-10}所示，与基础模型 M1 相比，加入多尺度 DSConv 后，M2 在 CX2 和 Oxford 数据集上的综合平均误差分别降低约 1.20\% 和 8.45\%；加入 RAA 后，M3 在 CS2、CX2 和 Oxford 数据集上的综合平均误差分别降低约 3.18\%、11.60\% 和 15.49\%。

现有英文起句：

> As shown in \cref{tab:4-10}, compared with the basic model M1, adding multi-scale DSConv in M2 reduces the combined average error by approximately 1.20\% on CX2 and 8.45\% on Oxford.

问题不是这些百分比已经被证明算错，而是消融小节只列数据集名称，没有明确各行是哪个电池、哪些电池的平均、是否跨重复运行。前面主比较按两节或七节电池给出结果，读者可能自然沿用那个集合，但数值并不支持无条件沿用：

|数据集|表4-10 M4：MAE / RMSE / MAPE|表4-6对应单节主比较|主比较两节平均 MAE|
|---|---|---|---|
|CS2|0.0120 / 0.0174 / 0.0160|CS2_38：0.01201 / 0.01741 / 0.015984|0.00967|
|CX2|0.0106 / 0.0193 / 0.0377|CX2_38：0.01059 / 0.01928 / 0.037673|0.009875|
|MIT|0.0018 / 0.0022 / 0.0020|b3c29：0.00183 / 0.00215 / 0.001960|0.001655|

这些对应关系提示前三组消融可能采用单节测试电池，但相近数值不能代替训练记录确认。Oxford 的 M4 为 0.0053 / 0.0062 / 0.0062，亦不能直接称为表4-5七节平均 0.00524 / 0.00638 / 0.00615 的正常四位舍入。

条件式改后方案：保留现有所有结果句，在消融协议段补一句经确认的范围定义；如实际为单节评价，可写：

> 消融实验在各数据集指定的评价电池上进行；CS2、CX2 和 MIT 分别采用〔确认后的电池编号〕，Oxford 采用〔确认后的电池或电池集合〕。〔如含多节电池，再明确先逐电池计算指标还是合并样本计算。〕

对应英文模板（方括号必须核实后填，不得直接入稿）：

> The ablation experiments are evaluated on [confirmed cells] for CS2, CX2, MIT, and Oxford, respectively. [If multiple cells are included, specify how their results are aggregated.]

表4-11使用相同集合时可以引用该定义；若不同，则另写清楚。确认前不把 Dataset 全改成 Cell，不猜 Oxford 集合，不调整数值。

修改原因与效果：读者能确定结果支持的是指定电池还是整个报告集合；避免把单电池结果读成跨电池平均。这是补充真实实验范围，不能用语言润色代替作者确认。

范文对应语境：[Engineering-AI 第2097—2098行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:2097)的宏观消融表标题明确标出 NASA B0005；其第2077—2090行则讨论数据集上的模块消融。可借鉴的是有需要时点明实际评价对象；其微观消融只写数据集的表达不能反过来证明本文不需要说明。范文不提供本文电池名单。

与旧问题的区别：旧 R03 问的是 MAE、RMSE、MAPE 如何合成 Average 及 Reduction 的比较分母；本项问的是每个 MAE、RMSE、MAPE 本身来自哪些电池。两个聚合层级不同。

## SR02｜初始化比较报告的是均值范围，不是全部运行值范围

位置：[中文第4章64行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:64)、[英文同段](D:/MS-AgentNet-English/chapters/chapter04.tex:64)、[初始化表](D:/MS-AgentNet-English/tables/table_4_3_initialization.tex:8)。

中文改前：

> 各方案对应的 $R^2$ 为 0.98527～0.98645，RMSE 为 0.00774～0.00805，MAE 为 0.00485～0.00499，表明其预测性能较为接近。

中文建议：

> 三种方案的平均 $R^2$ 为 0.98527～0.98645，平均 RMSE 为 0.00774～0.00805，平均 MAE 为 0.00485～0.00499，表明其平均预测性能较为接近。

英文改前：

> Their $R^2$ values range from 0.98527 to 0.98645, RMSE from 0.00774 to 0.00805, and MAE from 0.00485 to 0.00499, indicating similar prediction performance.

英文建议：

> Their mean $R^2$ values range from 0.98527 to 0.98645, mean RMSE from 0.00774 to 0.00805, and mean MAE from 0.00485 to 0.00499, indicating similar mean prediction performance.

原因：表头明确为 mean ± SD，正文列的是三种方案均值的最小值和最大值，不是每次训练的取值范围，也不是置信区间。加“平均”即可对应已有表头，不新增科学结论。原文没有声称统计等效，不应要求补显著性检验才能保留“较为接近”；也不把后面的默认初始化选择改成其精度最优。

范文：[JESSOHRUL 第1306—1313行](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1306)明确说明重复训练及结果平均。这里只参考将均值身份说明白，不继承其五次设置；该段“guarantee statistical significance”等强措辞不适合机械继承。本项直接依据是本文表头。

## SR03｜均值、标准差、中位数的重复次数与统计单元未交代

位置：[中文第4章64—66行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:64)、[初始化表](D:/MS-AgentNet-English/tables/table_4_3_initialization.tex:8)、[收敛表](D:/MS-AgentNet-English/tables/table_4_3.tex:7)。

中文改前相关句：

> 模型收敛特性通过收敛速度和训练后期损失波动共同评价。将训练损失首次降至首轮损失 10\% 以下的训练轮次定义为收敛阈值轮次，并采用最后 20 轮损失的均值和标准差描述训练后期的收敛状态。如\cref{tab:4-3}所示，各次训练均达到预设收敛阈值。

英文现句：

> As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

缺失的不是“最后20轮”——这一层已明写；缺的是跨运行汇总层：初始化表的 mean±SD 来自多少次运行、每次改变什么，收敛表的 median [range] 又跨多少次、什么电池、什么初始化设置。表4-5只对主比较 Cell2 写了五次独立运行，不能据此替初始化表、MIT 或收敛表自动补五次。

经作者确认后，可保留原统计句，补如下定义；这不是要求新增实验：

> 初始化比较在 Oxford Cell2 上汇总〔实际次数〕次〔实际重复方式〕运行，报告各评价指标的均值和标准差。收敛分析在 Oxford 的〔实际训练电池〕与 MIT 的〔实际训练电池〕上分别汇总〔实际次数及初始化设置〕次训练；先在每次训练内计算收敛阈值轮次以及最后20轮损失的均值和标准差，再跨〔实际统计单元〕报告中位数及表中范围。

对应英文模板：

> For the initialization comparison on Oxford Cell2, the reported values are the means and standard deviations over [confirmed number and type of runs]. For convergence analysis, [confirmed cells, initialization settings, and run counts] are used. The convergence threshold epoch and the mean and standard deviation of the loss over the final 20 epochs are calculated for each run, and the reported medians and ranges are taken across [confirmed aggregation units].

若中位数实际跨方案或跨电池而非重复运行，必须改写模板，不把推测写成事实。若各方案样本数不同，也应如实说明。

范文依据：[JESSOHRUL 第1306—1313行](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1306)把 five independent training and validation runs、different random seeds 和结果平均连在同一说明段中；这是与本项最直接的可复现性参照。本文次数不能从范文照搬。[Engineering-AI 第1300—1305、1317—1330行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:1300)分别把收敛阈值与特定电池、末20轮波动绑定，可参考对象明确性，不继承其机制因果解释。

## 对上轮结论的再次审慎确认

- R02“整体MAPE不能单独证明尾段误差”仍成立；但第105行已明确局部放大图支持尾段轨迹观察，因此不能把所有尾段描述全部撤销。只处理第107行数值证据与结论的跳转。
- R03保留为待定义，不从四位舍入数字判 Reduction 算错。本轮 SR01 是另一个聚合维度。
- R04不同配置的精度/资源归属仍值得明确；不把学习率不同本身判为参数量结果无效。
- R05四头与四层数值相同不等于结构等价；正文已明说“数值上”，不能再说作者没有承认区别。
- R06 Fusion 的隐含基准最自然是 HI1；原句可理解，不升级为已经证明的逻辑错误。
- R07四档适配比例下降真实存在；限定测试范围是防外推，不表示观察到的趋势不成立。
- 初始化普通正态默认选择没有声称精度最高；本轮只精确均值与统计协议，不把这一选择理由撤回。
- 第5章52.69%明确指CX2两节平均MAPE；与表值对应，不替换成CX2_38的59.75%。结论已有同数据集、一定程度、应用潜力和未来硬件验证，保留。
- 组级HI1与Cell1筛选的不同类别HI对比可以说明当前输入方案的实测表现，但不单独隔离组级筛选算法的因果贡献。现稿末句限定在该组Oxford输入表现，尚不足以判为新错误；不要求为了本轮语言审查自动加算法对照实验。

## 范文与覆盖边界

本轮读取 Engineering-AI L1251—1333、1451—1505、2077—2098；BMSFormer L1331—1394；JESSOHRUL L1271—1325。TXT中跨栏/跨页错序没有拼成新句；只引用可直接确认的完整内部段或表题。未宣称重新做范文PDF重排或全文句长测量。论文表图文件均只读，未调用的 table_4_2 和 figure_4_1 不算已展示内容。三个新增条目应先由主审核对再交作者，技术空白不能自动填写。

---

## 附录3

# 中文逻辑二次查漏：摘要、引言与跨章定义

日期：2026-09-14。独立交叉复核，只新增本文档；未修改论文。首轮报告不是错误清单的永久定论，本轮也复核其“保留”判断。

## 范围及结论

完整重读中英摘要、第1章及首轮 intro-conclusion、cross-chapter、methods、results 报告。交叉读取第2章HI定义、筛选与结论，第3章窗口输入、卷积尺度和RAA运算，第4章主实验、配置、迁移、消融及复杂度设置，第5章英文结论；核对表2_5、2_6、4_1、4_4。检索中英文正文及表格的序列长度、滑动窗口、步长和填充说明。本文是查漏附录，不重复声称完成代码或原始数据审计。

新增两项需要核实/界定的证据问题，不是两处确定语法错误。第二项修正首轮M03之外的一项“保留”判断：高相关的实测数字可以保留，但不能直接推出未经定义的敏感性和跨电池一致性。

## S-IC01｜“长期/全局”对应的实际输入时间范围未交代完整

位置：[中文摘要](D:/MS-AgentNet-English/source-zh/chapters/abstract.tex:1)、[引言第38行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:38)、[模型输入第5行](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:5)、[复杂度实验第168行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:168)、[主实验超参数表](D:/MS-AgentNet-English/tables/table_4_1.tex:1)。

中文改前：

> ……协同捕获局部退化特征与长程退化依赖……

方法原句：

> 健康指标（Health Indicators，HIs）序列经滑动窗口划分为样本片段……训练时以每个输入窗口后紧邻循环的真实SOH值作为监督标签。

现有英文摘要片段：

> to capture local degradation features and long-range degradation dependencies

问题不是global这个技术名词错误，而是其观察范围未落到实际实验。RAA的全局交互只跨当前输入的N个位置；网络未描述跨窗口保留状态。主性能设置给出L、d和学习率，但没有明确主实验的N、窗口移动步长，以及序列相邻记录对应的实际循环间隔。N=5只在另设的统一复杂度测试中明确，不能据此断言所有主实验都采用5。更不能由大核31直接断言模型看到了31个真实历史循环；其实际有效范围还取决于输入N、填充与采样间隔。

建议处理顺序：

1. 先向作者/实现核实主实验与迁移实验的N、步长、记录间隔及卷积填充方式；若各数据集设置不同，应分别交代。不得把范文或复杂度测试的值填进去。
2. 在模型说明中明确global的定义域，而非在每段反复添加免责声明。
3. 若实际历史跨度支持“长期”，可保留；若只支持窗口内跨位置关系，应收窄相应摘要/贡献表述，而不是把模型判作无效。

条件性中文改后（仅定义范围、不填未核实数值）：

> 本文的全局信息交互是指各输入窗口内不同序列位置之间的信息交互。

条件性英文：

> Here, global information interaction refers to interactions among sequence positions within each input window.

若作者确认摘要应只表达当前架构能直接确定的作用，摘要局部候选为：

> ……协同捕获局部退化特征与输入窗口内的跨循环依赖……

> to capture local degradation features and cross-cycle dependencies within the input window

以上后一个候选收窄“长程”的主张范围，不能作为不改原意的普通润色自动应用。补主实验N/步长是增加可复现信息，也须核实；本轮不提供虚构的正式设置句。

范文依据：本轮重新读取[BMSFormer第270—299行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:270)，其中写“moving forward one step at a time”，并明确下一步SOH是标签。可借鉴的是交代窗口如何移动以及标签与窗口的关系，不可照搬其数据协议。另重读[Engineering-AI第818—853行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:818)，其N定义及k=5/31只说明记号和核尺度，不能替本文证明31个真实循环的信息范围。TXT跨栏段落不拼接为连续论证。

## S-IC02｜相关强度接近不等于未定义的“退化敏感性/跨电池一致性”

分类：证据边界/可选定义澄清，不是已证实的逻辑错误。原文并未明说两池映射方向、斜率和截距相同；如果“敏感性/一致性”在本文只作关联强度的简称，原句在上下文可以理解。以下反例用于说明不能扩大解读，不用于证明原稿已经作出该扩大断言。

位置：[中文第2章158行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:158)，交叉[引言42行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:42)、[其他电池相关表](D:/MS-AgentNet-English/tables/table_2_5.tex:7)。

中文改前（数字之前的句子不动）：

> 四项相关系数均接近1，且在两节电池之间差异较小，表明HI1对SOH变化具有较高的退化敏感性和良好的跨电池一致性。

现有英文：

> All four coefficients are close to 1 and differ only slightly between the two cells, indicating that HI1 is highly sensitive to SOH changes during degradation and has good cross-cell consistency.

首轮认为在两池语境下可读并保留；二次复核认为需区分指标量纲和证据范围。这里列的是绝对PCC/SCC：它们支持关联强度高且接近，但不直接量化HI随SOH变化的幅度、噪声分辨能力，也不证明两电池具有相同的映射方向、斜率或截距。

这一点可以由本文公式自身检验，无须假定实际数据有问题：若一池f=y，另一池f=-y，两者绝对PCC和SCC都为1；若f=a y+b，正比例a极小时相关系数仍可为1。因此相关强度相近不是对全部意义的“敏感性/一致性”的充分证明。这里仅举数学反例，不声称本文实际出现符号反转、小幅变化或泛化失败。

若作者意图就是“相关性表现一致”，最小中文改后：

> 四项绝对相关系数均接近1，且在两节电池之间差异较小，表明HI1在两节电池上均与SOH具有较强的线性和单调关联，且关联强度相近。

对应英文：

> All four absolute correlation coefficients are close to 1 and differ only slightly between the two cells, indicating that HI1 has strong linear and monotonic relationships with SOH on both cells, with similar correlation strengths.

原因与效果：将结论约束到实际测量的对象，不改四个数字或筛选规则。若“退化敏感性”是作者另有定义的技术指标，需先给定义和对应证据，不应直接删去。上述候选是论断范围精确化，需作者确认。

跨章影响：引言/摘要里的“跨电池稳健”不需要全部删除，但建议在方法中明确本筛选约束的是开发电池上的绝对关联强度；实际模型跨电池性能另由第4章结果支持。组级绝对相关得分本身不保证映射方向/尺度一致。不要未经确认增加符号约束、重设计筛选算法，也不要求因这一理论反例重做实验。第2章162行“其余六节电池仍保持较高线性相关性”和引言44行“较强线性和单调相关性”没有扩大到映射一致，仍可保留。

范文依据：本轮重新读取[JESSOHRUL第1659—1686行](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1659)，其中“PCC measures the linear correlation, while SCC assesses the monotonic relationship”明确测量对象。另读[BMSFormer第503—524行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:503)，其将PCC定义为线性关联强度。范文支持按相关关系命名结论；上面的充分条件反例来自本文统计量定义，不伪称范文曾验证本文的方向/斜率。范文没有直接支持必须使用候选整句。

## 首轮六项复核

| 首轮编号 | 二次判断 |
|---|---|
| ZIC-01 实时性受到限制 | 保留发现；现英文已拆成资源有限/实时要求严格，不再改英文。 |
| ZIC-02 线性复杂度限定 | 保留为可自足化的限定说明，不升级为公式错误。摘要候选较长，可在作者确认后作最小补充，不能把所有句子都塞入推导细节。 |
| ZIC-03 ECM机制总括 | 保留待核；Engineering-AI114—134本轮重读支持区分electrochemical/electrical dynamics，但本文ref19本轮仍未核验。 |
| ZIC-04 传统机器学习宽泛局限 | 保留证据范围问题；some/may不等于取得证据。BMSFormer64—93本轮重读确认其类别范围比本文更广，不构成本文全类别因果断言的证明。 |
| X01 其他电池 | 保留范围澄清；表中已经区分配置电池，不能把报告它的性能认定为数据泄漏。 |
| X02 多体系泛化 | 保留可选澄清；如果数据介绍句同时总括迁移实验，宽泛原句可结合后文理解，不必强制改成只谈域内。 |

## 未新增为错误的内容

- 引言第15—17行“为解决这一问题”紧接串行限制，合理；不强行解释成Vaswani专为电池任务提出Transformer。
- 摘要“随后”是方法介绍推进，不是严格的代码执行时刻；不以开发先后猜测实验顺序错误。
- “总体更优”与某些单池指标未最优并不矛盾，结论已使用总体及一定程度等限定。
- 在线应用作为目标不等于已部署，当前结论明确嵌入式验证为未来工作；不重复撤销这个研究目标。
- 外部文献对比是否同样本清洗、真实协议是否正确需原始资料核验。本轮没有读这些外部原始文献，不把未核验信息当成确定错误。

## 写入边界

只创建此审查文件。新增项先由作者确认含义/实现，再形成批准稿；不改冻结中文，不以猜测填实验参数，不新增科学机制。

---


