# 中文原稿语法与逻辑审查：第2–3章（2026-09-14）

本轮为独立重新阅读，不以既往语言建议作为发现依据。只提出建议，不修改 source-zh、chapters、tables 或 figures。范文只能支持表达方法，不能代替本文技术实现与实验依据。

## 范围与结论

完整读取 source-zh/chapters/chapter02.tex（165行）、chapter03.tex（386行）及对应现英文；读取表 table_2_1–table_2_6、table_2_hi_screening_steps 的中英文件，图 figure_2_1–figure_2_4、figure_3_1–figure_3_3 的中英 TeX 图注。关联读取第4章 L41、L73、L79 的输入与配置协议。图内栅格文字不是本报告完整覆盖范围，不宣称已重审所有图像。

覆盖：框架四步骤；四组数据；15项HI定义；PCC/SCC与三阶段MS-CCCT；准入/排序/去冗余；模型三步骤；标准DSConv成本；DSConv-S/L结构；一般/Softmax/线性注意力；RAA归一化、聚合、广播、残差、复杂度；SLFA融合。

发现不是“中文到处有错”：大部分衔接顺畅。以下包括1项明确对应关系语言问题、1项中文问题但英文已修好、7项需确认的逻辑/技术表述、1项可选澄清。不得将全部建议一次写入论文。

## M01：五个指标与三个属性使用“分别”却未分组（明确语言问题）

位置：[中文第2章L74](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:74)，[现英文同位置](D:/MS-AgentNet-English/chapters/chapter02.tex:74)。

中文改前：
> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围\cite{ref64}。

中文最小改后：
> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9）。其中，HI5和HI7描述热响应的幅值，HI6和HI8描述特征位置，HI9描述波动范围\cite{ref64}。

现英文：
> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted to describe the amplitude, characteristic positions, and range of variation of the thermal response\cite{ref64}.

英文建议：
> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted. HI5 and HI7 describe the amplitude of the thermal response, HI6 and HI8 describe its characteristic positions, and HI9 describes its range of variation\cite{ref64}.

原因/效果：不是简单嫌句长；5→3的对应在中文“分别”后缺失。英文已没有机械翻成 respectively，不属误译，但仍可将分组显式化。分组由既有指标定义直接确定，不新增电化学机制。两句仍在同一自然段。

范文：[JESSOHRUL TXT L1803–1811](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1803)逐项列出“the peak of the DTV curve (HI5)”以及对应峰位、谷值、谷位。助手释义：用指标实体与编号直接对应。它支持明确对应的写法，不含本文HI9，不能用它证明HI9机制；本项分组依据本文定义。

## M02：残差句中省略主语导致“特征与自己相加”（中文问题，现英文保留）

位置：[中文第3章L33](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:33)。

中文改前：
> 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN），并与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：

中文建议：
> 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN）；FFN的输出与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：

现英文（保留，无再次改动）：
> The features $\mathbf X_l''$ are processed by $\operatorname{LN}_0$ and then a feedforward neural network (FFN). The result is added to $\mathbf X_l''$ through a residual connection to produce the Block output $\mathbf Y_l$:

原因/效果：中文后一分句的隐含主语容易继续承接“特征X''”；公式明确相加的是FFN输出和X''。现英文The result已经依据公式消解，不需为了凑改动再次改。中文修正不改变计算。

范文：[Engineering-AI TXT L822–826](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:822)明确说明残差连接使用哪个阶段输出（“the output of the first stage”）。只借“点明相加对象”的表达；范文残差取X'、本文取X''，不得照搬对象。此短段可独立读取，不依据TXT跨栏顺序推断算法。

## M03：最小值得分≠无条件保证两个电池均强相关（逻辑边界，需确认）

位置：[中文第2章L137](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:137)。

中文改前：
> 该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，使入选窗口在两节电池上均保持较强的相关性。

建议（将末项准确表达为选择目标）：
> 该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，并以提高两节电池中的最低相关水平为窗口选择目标。

现英文：
> This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and allowing the selected window to maintain strong correlations on both cells.

建议英文：
> This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and favoring windows with a higher minimum correlation across the two cells.

原因：式S_i=min(...)及选择最大S只能提高所考察候选中的最差项。如果所有候选S均为0.2–0.3，最大者仍不是“强”。后文Oxford实测0.994447以及筛选阈值可以支持该结果，但不能倒推得分函数自身保证强相关。本项收窄“必然效果”为准则目标，涉及力度，需作者确认，不按纯语法自动处理。

范文：[BMSFormer TXT L447–457](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:447)先取跨电池最小PCC作baseline，再选择“the segment with the highest baseline value”。助手释义：选择最小相关水平最高的候选段。支持描述实际选择规则，不证明所有数据都强相关。该范文窗口步长与列举区间存在不一致，不继承其数值。

## M04：‘其他电池’相对于开发集还是训练池？（协议指代待确认）

汇总说明：本项与主审跨章 X01 重叠，最终以主审 X01 的整段版本为准，不重复计为两项发现；以下保留独立核对依据。

位置：[中文第2章L160](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:160)；表2_4、第4章L41/L73。

中文改前：
> 用于后续评价的其他电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发与后续评价之间的数据隔离。

现英文：
> The other cells used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between feature development and subsequent evaluation.

若这里“其他”明确指开发集合之外，中文建议：
> 特征开发集合之外、用于后续评价的电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持这些电池与特征开发之间的数据隔离。

对应英文：
> Cells outside the feature-development set that are used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between these cells and feature development.

原因：开发集含Cell1/Cell2，第4章报告范围又含Cell2。前文亦用“训练后的模型用于其他电池”，彼处“其他”相对训练池。不能把不同“其他”合并理解为所有报告池均未参与开发。不是认定泄漏，更不是要求新增第三类协议角色；只是明确集合。若实际意图声称所有报告池未参与开发，则与现稿表/协议冲突，应先核对而非采用上述句子。

范文：[Engineering-AI TXT L396–400](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:396)明确相关计算用“only the calibration/training data”；L377–379说区间在后续测试前固定。借明确数据集合和冻结时点的表达；不能借其training partition替换本文两电池开发集。

## M05：DSConv低成本结论缺少比值<1的条件（数学逻辑，需确认）

位置：[中文第3章L100](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:100)，公式L81–98。

中文改前：
> 由式\eqref{eq:dsconv_cost_ratio}可知，在输入、输出通道配置一致的情况下，DSConv的计算成本低于标准卷积，为后续小核与大核卷积模块的构建提供了基础。

现英文：
> Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and output channel configurations, DSConv has a lower computational cost than standard convolution, providing the basis for the small- and large-kernel modules described below.

保留现式的条件建议：
> 由式\eqref{eq:dsconv_cost_ratio}可知，在输入、输出通道配置一致且$1/C_{\mathrm{out}}+1/k^2<1$时，DSConv的计算成本低于标准卷积，为后续小核与大核卷积模块的构建提供了基础。

对应英文：
> Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and output channel configurations and $1/C_{\mathrm{out}}+1/k^2<1$, DSConv has a lower computational cost than standard convolution, providing the basis for the small- and large-kernel modules described below.

原因：直接由现式代入k=1得1+1/Cout>1；仅通道一致不充分。这是本文公式自身可验证的反例，不依赖外部结论。实际小核5/大核31可能满足相应一维条件，不等于无条件通式结论成立。增加技术限定，需作者确认；先处理M06以免保留错误维度的限定。

范文：[BMSFormer TXT L784–825](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:784)有同类二维成本记号，L814–817说明分离空间/通道运算。范文能说明公式来源风格，不能豁免本文比值小于1的条件，更不能据此证明本文带扩展的模块在任意配置都低成本。

## M06：二维通式与一维序列尺寸没有接上（技术定义待确认）

位置：[中文第3章L57–100](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:57)、L110–170、L176–185；现英文同位置。

中文原句：
> 其中，$2C_{\mathrm{out}}$和$D_F\times D_F$分别表示扩展后的通道数和特征图尺寸。

现英文：
> where $2C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of channels and the feature map size, respectively.

冲突：前面输入B×N×d，转置B×2d×N、深度核1×5/1×31，均只有N个序列位置；成本却一直乘D_F×D_F，基础核面积k×k。没有说明这是二维示例再适配一维，或D_F²被特殊定义为位置数。无法单纯换“size”修好。

分支A（确实希望先介绍二维背景）：先明确中文“上述通式以二维方形特征图为例；以下模块沿序列维度进行一维卷积。”英文“ The preceding formulas use a square two-dimensional feature map as an example; the following modules apply one-dimensional convolution along the sequence dimension.” 随后必须由实现核实并统一后续实际成本式，不能只加此句了事。

分支B（全文只应给实际一维成本）：在确认计算计数口径、单样本、忽略偏置/激活、Cin=Cout=d后，将位置因子写N；基础核写k而非k²。例如现有结构的乘加级项可写DSConv-S：N(4d²+10d)，DSConv-L：N(6d²+93d)。这是根据两逐点+一深度的代数推导示意，不是可直接替换的FLOPs数值或已核实代码，不提供正式批准式。

原因/效果：消除“套范文公式但维度未适配”。涉及公式、定义及计量，必须核实后改；当前不选分支、不写论文。

范文：[BMSFormer TXT L784–789](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:784)确有k×k与NF×NF，[Engineering-AI TXT L845–849](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:845)明确N×d↔d×N转置。它们提示需要区分空间模板与序列实现，不证明两者可无说明混用。

## M07：非负相似度不足以保证归一化分母有效（条件缺失）

位置：[中文第3章L207](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:207)，L209–223公式。

中文改前：
> 在采用非负相似度函数构造归一化注意力权重时，第$i$个注意力头在第$p$个位置的输出可表示为：

现英文：
> When a nonnegative similarity function is used to construct normalized attention weights, the output at the $p$th position of the $i$th attention head can be expressed as:

最小中文建议：
> 在采用非负相似度函数构造归一化注意力权重且该查询对应的相似度之和为正时，第$i$个注意力头在第$p$个位置的输出可表示为：

对应英文：
> When a nonnegative similarity function is used to construct normalized attention weights and the sum of similarities for the query is positive, the output at the $p$th position of the $i$th attention head can be expressed as:

原因：全行0满足非负，但现式为0/0；本文自己的RAA L294–311特意规定零正值行返回均匀分布，说明确有这一分支。建议只补一般商式成立条件，不改变RAA已写的分支，也不擅自新增epsilon。属于数学适用条件，需确认。范文未找到能直接支持该补充条件的对应完整表达；依据是现式与本文章节内定义，不硬凑范文。

## M08：去冗余表each/otherwise的量词与加入时点不明（原稿已英文，算法待确认）

位置：[冻结表L13–16](D:/MS-AgentNet-English/source-zh/tables/table_2_hi_screening_steps.tex:13)与[现表同位置](D:/MS-AgentNet-English/tables/table_2_hi_screening_steps.tex:13)。这不是中文翻错，冻结稿该表原本就用英文。

原文：
> For each retained candidate HI $f_i$: compare $f_i$ with each HI already contained in $\mathcal{S}$; if their group-average absolute PCC and SCC both reach $\theta_{\mathrm{co}}=0.95$, remove $f_i$; otherwise, add $f_i$ to $\mathcal{S}$.

问题：先每一项比较，再otherwise加入，可能读成“某一对未超过阈值就加入”，即使下一对高度冗余；S为空时比较不执行，何时加入亦不明。需明确“存在一项/不存在任何项”及加入发生在全部检查后。

若实现是通常的任一高冗余即拒绝，中文建议（助手表达，非冻结原文）：
> 对每个保留候选$f_i$，若$\mathcal S$中存在至少一个指标，使其与$f_i$的组平均绝对PCC和SCC均达到$\theta_{\mathrm{co}}=0.95$，则剔除$f_i$；否则将$f_i$加入$\mathcal S$。

对应英文建议：
> For each retained candidate HI $f_i$, remove it if there is any HI in $\mathcal{S}$ for which the group-average absolute PCC and SCC with $f_i$ both reach $\theta_{\mathrm{co}}=0.95$; otherwise, add $f_i$ to $\mathcal{S}$.

该版本空集自然进入otherwise。仍需代码/作者确认，不能用“通常”推定实现。

范文：[JESSOHRUL TXT L1829–1834](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1829)确实先排序再剔除高特征间相关指标；它支持步骤顺序，不直接规定本文跨两电池聚合、PCC/SCC同时、存在量词。无直接证据处不得称范文标准算法。

## M09：Oxford充电协议表—文不一致（事实待核，不强制择一）

位置：[中文第2章L29](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:29)、[冻结表2_1L19](D:/MS-AgentNet-English/source-zh/tables/table_2_1.tex:19)、对应现英文。

中文原句：
> 电池采用恒流–恒压方式充电至4.2 V……

现英文：
> The cells were charged to 4.2 V using a constant-current--constant-voltage protocol ...

表中原/现：Oxford Charge protocol (rate) = CC (2C)。

若实际全程CC-CV，表需写CC-CV（2C恒流阶段），是否保留2C亦核实；英文可为“CC-CV (2C during the CC phase)”。
若原数据所指是仅CC老化循环，正文对应中文应为“电池以2C恒流充电至4.2 V”，英文“The cells were charged at a constant current of 2C to 4.2 V.”
若表与正文分别描述老化与定期表征，二者可都正确但须标明各自阶段，不能强行同一。

没有选择上述分支。范文不能证明本文采用的数据阶段；本轮未查数据发布方协议，结论仅是现稿内部不一致。此前variance→Dynamic current profile的现表已改好，不重复列入实施建议。

## M10：‘PCC仅对线性变化敏感’容易被理解成完全无法反映非线性（可选精确化）

位置：[中文第2章L108](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:108)。

中文原句：
> PCC是衡量CCCT与SOH线性关联强度的常用统计指标，但该指标仅对线性变化敏感，单独使用难以反映单调非线性关系。

现英文：
> PCC is a common statistical measure of the strength of the linear association between CCCT and SOH. However, it is sensitive only to linear changes and is insufficient on its own to characterize monotonic nonlinear relationships.

建议中文：
> PCC是衡量CCCT与SOH线性关联强度的常用统计指标，但单独使用难以充分刻画单调非线性关系。

对应英文：
> PCC is a common statistical measure of the strength of the linear association between CCCT and SOH. However, it is insufficient on its own to fully characterize monotonic nonlinear relationships.

原因：保留“衡量线性、需要SCC补充”的真正论点，避免将only解释成非线性关联一定没有PCC响应。此项不是否认PCC线性指标身份，也不改变筛选公式。若作者“仅对线性变化敏感”只是指标定义的简称，原句并非不可理解；精确化优先级低于上述逻辑问题。

范文：[JESSOHRUL TXT L1674–1680](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1674)：“PCC measures the linear correlation, while SCC assesses the monotonic relationship”。助手释义：分别说明两统计量测量的关系，不说PCC完全不响应非线性。此处支持删去过度限定only，不把范文“nonlinear dependencies”泛化为全部非线性。

## 重点保留与不应强改

- 第2章L60“除……外”、L76“与DTV……不同”、L106“然而”、L149“相比之下”均有实际对象关系，不因连接词出现就认定错误。
- 第2章L139的R3优于R2取R3、否则保留R2，包含等分时的处理，保留；未凭搜索层级推断全电压连续域全局最优。
- 第2章L158四项相关系数确实接近1，不能因M03否定该具体样本结果；“跨电池一致性”在其两池语境可读，不擅自增成跨数据集。
- 第2章L90 HI13/14命名已被英文分清；L98充放电变量定义现英文已分组；不重复修改。
- 第3章L18与公式DSConv-L残差一致；L174明确残差在Block级，不将DSConv-S内部残差机械复制给L。
- 第3章L265明确映射维度等于dh、dh固定，线性复杂度条件已给，不再加冗余声明。
- 第3章L294、311共同正比例缩放、正值行归一化及全非正回退在公式层面一致；不把ReLU²称为Softmax的等价替换，不声称权重区分本身保证更高精度。
- 第3章L349低秩仅指等效序列交互映射Phi_q Phi_k，不说整个含残差RAA映射秩≤na，保留。
- 第3章L363固定h和na且上下文固定维度的复杂度表述可保留；理论复杂度不改写实际推理速度。
- 图2_4现图注已明确四子图Cell/PCC/SCC对应，保留；未把历史图注问题当成现稿未修。
- 表2_3各S=min(mPCC,mSCC)、表2_4所列HIs均满足给定准入阈值，未见须靠语言修复的数值冲突。去冗余是否导致全部所列最终集合仍需原始矩阵/代码，不能仅凭最终表保证。
- 其余表2_2、2_5、2_6已读，未发现新的中文语法错误；英文表头HI可更明确为HI1属可选表意，不计入本次可靠发现。

## 本轮范文重读及证据边界

重读三篇TXT完整相应局部上下文：JESSOHRUL 1658–1686、1786–1849；BMSFormer435–459、735–825；Engineering-AI332–425、818–853。跨栏穿插已识别，本报告仅引用可独立定位的完整短语/小段，不根据穿插片段推断范文论证顺序、式号先后或跨页句法；未声称本轮重渲染PDF，亦未以旧词表代替原文。所有中文释义为助手译释。无直接参考依据项明确标示，不能因范文也这么写就沿用逻辑缺口。
