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
