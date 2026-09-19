# 第2、3章：中文句法与句间逻辑复核（建议稿）

**状态说明：本文件是独立复核备忘，不作为用户最新要求下的“新增问题”清单。** 用户随后要求不再用已查项目填充新一轮报告。此处第2、4、5项与早前报告重合，第1、3项也由主审交叉复核；不得把这五项包装为新发现。再次逐句审阅第3章后，尚未确认其他新的明确语病。第3章244行的φ“核函数/特征映射”名称问题交主审查原始论文后单列，不在此未核实地定论。

本报告只提建议，未修改论文。重点逐段重读第2、3章中英文，并结合全篇任务与术语边界检查。重新查看三篇 methodology.txt 的对应原文段落：BMSFormer §2.3；Engineering-AI §4.1–4.2 的模块流程；JESSOHRUL §3.5.1–3.5.2 的指标定义与筛选。TXT含双栏错序，以下只引用可独立定位的连续短句，不把跨栏相邻文本当作论证衔接。范文支持表达方法，不证明本文技术结论。以下五项部分与旧报告重合，均已重新核验，不计为五个“新发现”。

## 1. CVT“偏移”与区间时长变化不宜写成同义关系

位置：source-zh/chapters/chapter02.tex:52；chapters/chapter02.tex:52。

中文改前：
> 随循环推进，CVT曲线沿时间轴逐渐偏移，如图所示。该偏移表现为固定电压区间内的充电时长随老化持续变化。

中文建议（其余原句、图引用及段落不动）：
> 随循环推进，CVT曲线沿时间轴逐渐偏移，如图所示。固定电压区间内的充电时长也随老化持续变化。

现有英文：
> As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). This shift appears as a continuous change in charge duration within a fixed voltage interval as the battery ages.

建议英文：
> As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). The charge duration within a fixed voltage interval also changes continuously as the battery ages.

原因与效果：**词汇简单但表达绕，且指代建立了不充分的关系。**“该偏移表现为”把两个不同量连成同一现象。若两个电压端点的到达时刻都平移同一时间量，CCCT差值不变。因此，偏移本身不能推出时长变化。最小修复是直接以“区间内的充电时长”为主语，把原稿两个观察写为并列观察，不删除任何观察。**待核实：本批没有重测图中曲线，‘持续变化’及偏移的实际形态仍须由图/数据支持；建议不能充当该事实的验证。**

范文依据：JESSOHRUL methodology.txt:1335–1343，§3.5.1，先介绍电压随时间的变化，再直接定义电压区间内的时间指标；短引文“the time intervals during which the charging voltage ranges”。助手释义：充电电压处于指定范围内的时间区间。参考的是直接定义观察量，不照搬该范文CVT公式的符号顺序。

## 2. 五个指标与三个属性之间的“分别”缺少分组

位置：source-zh/chapters/chapter02.tex:74；chapters/chapter02.tex:74。

中文改前：
> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围\cite{ref64}。

中文建议：
> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9）。其中，HI5和HI7描述热响应的幅值，HI6和HI8描述特征位置，HI9描述波动范围\cite{ref64}。

现有英文：
> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted to describe the amplitude, characteristic positions, and range of variation of the thermal response\cite{ref64}.

建议英文：
> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted. HI5 and HI7 describe the amplitude of the thermal response, HI6 and HI8 describe its characteristic positions, and HI9 describes its range of variation\cite{ref64}.

原因与效果：中文“分别”通常提示按顺序对应，但这里是五项对三类。英语已经避免了 respectively 的机械误译，却仍未显式说明分组。建议按现有定义补明对应，保持同一段落、全部指标与原顺序，不新增机制。这是明确的对应关系语言问题。

范文依据：JESSOHRUL methodology.txt:1449–1457，§3.5.1，连续段明确列出DTV峰、峰位、谷、谷位。短引文“the voltage corresponding to the peak”。助手释义：峰值对应的电压。范文没有本文HI9，HI9归属由本文“峰谷差”定义支持。

## 3. DTC的“温度变化率”最好直接补明相对于容量

位置：source-zh/chapters/chapter02.tex:76；chapters/chapter02.tex:76。

中文改前：
> 与DTV在电压域刻画热响应不同，DTC在充电容量域刻画热响应。DTC以充电容量为自变量，描述温度变化率随容量的演化，其定义如下\cite{ref64}：

中文建议：
> 与DTV在电压域刻画热响应不同，DTC在充电容量域刻画热响应。DTC以充电容量为自变量，描述温度相对于容量的变化率，其定义如下\cite{ref64}：

现有英文：
> While DTV characterizes the thermal response in the voltage domain, DTC characterizes it in the charge capacity domain. With charge capacity as the independent variable, DTC describes how the rate of temperature change evolves with capacity and is defined as follows\cite{ref64}:

建议英文：
> While DTV characterizes the thermal response in the voltage domain, DTC characterizes it in the charge capacity domain. With charge capacity as the independent variable, DTC describes the rate of temperature change with respect to capacity and is defined as follows\cite{ref64}:

原因与效果：**词汇简单但表达绕。**现句先提出一个分母不明确的“温度变化率”，再说该变化率随容量演化；读者需回看公式才能排除dT/dt随Q变化的读法。最小修改直接说清dT/dQ。前句和“容量为自变量”已限定曲线所在域，因此没有删去容量域信息。这是低优先级定义澄清，不能称原公式有错。

范文依据：JESSOHRUL methodology.txt:1257–1260，§3.5.1，短引文“the rate of temperature change with respect to capacity”。助手释义：温度相对于容量的变化率。此句连续完整，不使用该页开头与上一页断句拼接的部分作为风格证据。

## 4. 最小相关得分支持选择方向，不能单独保证强相关

位置：source-zh/chapters/chapter02.tex:137；chapters/chapter02.tex:137。

中文改前：
> 该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，使入选窗口在两节电池上均保持较强的相关性。

中文建议：
> 该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，使筛选优先保留两节电池中最低相关水平较高的窗口。

现有英文：
> This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and allowing the selected window to maintain strong correlations on both cells.

建议英文：
> This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and favoring windows with a higher minimum correlation across the two cells.

原因与效果：原句前半讲评分规则，后半直接变为必然效果。即使所有候选最低相关仅0.2–0.3，仍可选出最高得分窗口，故得分定义本身不足以保证“均较强”。建议把结尾准确落到选择规则；Oxford已得到的0.994447仍在下文保留。**属于推论力度调整，需作者确认；若作者本意指通过后续准入阈值的最终窗口，应明确该条件，不能把该条件归因给得分本身。**

范文依据：BMSFormer methodology.txt:224–237，§2.3，最小PCC作为baseline，再选择“the segment with the highest baseline value”。助手释义：基准值最高的片段。该连续句支持“明确实际选择规则”的表达，不能证明本文规则必然强相关，亦不照搬其数值和步长。

## 5. FFN残差句的相加对象：中文修复，英文保留

位置：source-zh/chapters/chapter03.tex:33；chapters/chapter03.tex:33。

中文改前：
> 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN），并与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：

中文建议：
> 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN）；FFN的输出与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：

现有英文（建议保留）：
> The features $\mathbf X_l''$ are processed by $\operatorname{LN}_0$ and then a feedforward neural network (FFN). The result is added to $\mathbf X_l''$ through a residual connection to produce the Block output $\mathbf Y_l$:

原因与效果：中文“并与……”继续沿用的主语可能被读成输入特征本身。公式明确相加的是FFN输出与输入。补出“FFN的输出”即可；英语The result已完成这一步，没有理由再次改写。此例恰好说明现英文不全是照搬中文错误。

范文依据：Engineering-AI methodology.txt:630–634，§4.1，短引文“the residual connection aggregates the output of the first stage”。助手释义：残差连接聚合第一阶段的输出。参考其明确相加对象的写法；范文使用X'，本文使用X''，不得借表达参考改变本文残差路径。

## 保留与范围边界

第3章“DSConv-S局部表示→RAA构造Q/K/V→聚合与广播→两分支相加”的顺序，与公式总体相符，保留。“DSConv-L置于SLFA之后”与块级公式相符，保留。第2章PCC/SCC计算、分别取最小值、再取二者较小值的顺序清楚，保留。旧报告中的一维/二维成本、零分母及数据角色问题属于技术核验，不在本次语言报告中重复扩充为新问题。
