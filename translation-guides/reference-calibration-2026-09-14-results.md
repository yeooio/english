# 结果类旧问题的范文反向校准（2026-09-14）

本报告只重新分级旧 R02–R08、SR01–SR03、TR01，不增加问题，不修改论文。检查目标不是找一句“更理想”的范文，而是检查范文是否也省略相同细节、是否采用相同概括方式，以及本文是否存在额外的实质歧义。以下“保留”指保留现有表述；“待核”是核实真实口径，不等于确认论文错误。

## 主要校准结论

以前把“没有写得最完整”当作“需要补充”的倾向应纠正。最明显的是：JESSOHRUL 也直接使用 Average/Reduction；BMSFormer 的纯资源表也称 comprehensive performance，并使用 same configuration；Engineering-AI 的微观消融也只列 Dataset 和 average results。不能再只引用范文其他地方的详细定义来要求本文一律写得更细。

|旧编号|范文实际相似做法、可定位依据|语境差异与此次裁定|
|---|---|---|
|R02 整体误差与寿命后期讨论|Engineering-AI/full.txt L1433–1451 在 accelerated aging trends 段直接用 CS2_38 整体 RMSE 0.0249 与两基线数值说明加速衰减轨迹的拟合；L1393–1409 也用局部放大图作定性观察。不是所有局部描述都另设区间指标。BMSFormer/full.txt L1307–1326 同段讨论突降跟踪与跨电池平均排名。|本文 L105 已明确 enlarged views 支持尾段轨迹观察，因此旧建议要求“只能改成整体或新增尾段指标”过于二选一。**降为可选衔接澄清**：如图确实支持，可保留尾段定性结论，把结论明确归于图表共同观察；无需为语言审查新增尾段实验。仍不能把 0.037673 称作尾段 MAPE。|
|R03 Average/Reduction 定义|JESSOHRUL/full.txt L3476–3534 完整消融说明及 L3536–3788 Table 13，直接列 MAE/RMSE/MAPE/Average/Reduction；本次所读消融段及表附近未另给 Average 运算公式或 Reduction 公式。L3518–3526 通过 Proposed 与 M1/M2/M3 的比较说明降幅对象。|**拆分分级**：表头没有公式本身降为可选表注，不是确定错误。本文正文 M2 vs M1 与表列 M4 vs 各行不必采用同一基准，分工不同可成立，不能称其本身逻辑冲突。实际 Average 如何计算、未舍入降幅是否一致仍可内部核实，但不自动要求写三句长表注。范文自身的数值未被本轮逐项重算，不能据范文格式证明本文算式或数值正确。|
|R04 精度和复杂度来自不同配置|BMSFormer/full.txt L1344–1394 明确先谈准确率，再单独规定效率测试配置；L1670–1697 将资源结果与精度权衡综合讨论，并不在资源表给出每一配置的准确率。Engineering-AI/full.txt L2440–2456 也综合精度和开销讨论权衡。|分别做精度与标准化开销实验是范文实际做法，不能要求所有实验必须同配置。本文已在 L79/L168 分开规定配置，**降为可选来源澄清**，不把原总结判为已证实的虚假同配置主张；如作者意在声称“资源表的精确配置取得前述全部精度”，才保留针对该解释的核实。学习率不同不使参数量/FLOPs结果无效。|
|R05 comprehensive performance / same configuration 表题|BMSFormer/full.txt L1764–1803 Table 6 标题就是 The comprehensive performance of models under the same and optimal configurations，指标只列 FLOPs/training time/parameters/storage；L1670 又写 almost same configuration。JESSOHRUL/full.txt L3799–3824 使用 identical training and architectural hyperparameters 后分别列 Transformer 4 heads 与 LSTM 4 layers。|**默认保留**。这属于范文功能对应的标题/比较约定，不是因为“没有准确率列”就必须改标题。本文正文已解释同输入、训练设置及数值对应，不声称异构结构数学等价。换成 resource costs 可以更精确，但只能作为个人偏好的可选命名，退出必要问题清单。|
|R06 Fusion 隐含比较基准|JESSOHRUL/full.txt L1946–1968 定义单输入及 Fusion，L1961–1969 将 Fusion 平均排名与单指标结果连接，未每一句重列比较基准；完整 HI 结果开头还跨栏延续至 L1874–1891。|本文前句明确 HI1 最好，后句进一步增益最自然承接 HI1，表中也给排名。**默认保留**；加 over HI1 alone 只是可选精确化。不能说论文已经断言所有融合方法无效。|
|R07 continuously improves 只试四档|本轮未定位三范文中与本文同协议的适配比例试验，不能声称范文对该实验也这么写。Engineering-AI/full.txt L1330–1378 的超参数敏感性讨论在列出搜索范围后用 consistent trends 概括观察，并非每句复述 tested 范围。|本文同一小节已经列10/30/50/70%，后续对这些比例作总结，**默认保留、可选加 tested**。不能只因未逐句复述范围就认定无限外推。该裁定依据本文上下文为主，范文只提供功能相近的概括粒度。|
|R08 comprehensive evaluation|JESSOHRUL/full.txt L1895–1914 实验章开头使用 comprehensively evaluate / thorough validation；Engineering-AI/full.txt L1141–1153 的结果章开头更有 holistic assessment 和 validates practical viability。|本文已用 evaluation 而不是保证所有情形成立，**保留现英文**。不机械继承范文更强的机制或实用性保证，也不要求再加 from the aspects considered here 使句子防御性变长。|
|SR01 消融评价电池集合|Engineering-AI/full.txt L2077–2090、L2153–2269 的微观消融按 Dataset 报 average results；L2356–2357 起 Table 12 也为 Avg. results。该局部没有每表列电池或细讲聚合。相反，其宏观表 L2097–2098 明写 NASA B0005；JESSOHRUL/full.txt L3536 起 Table13 用 Battery 和具体编号，L3518–3526 正文也逐电池说明。|“范文全部要求每表列电池”不成立。**缩小保留为待核**：本文若消融沿用既有评价集合，可不重复长协议；但旧检查发现 CS2/CX2/MIT 全模型值近于单节结果而非主比较两节平均，这构成具体识别疑问。只问实际对象是否变化，确认后必要时加一句/表头标电池，不强制展开先后聚合公式。|
|SR02 初始化指标值其实均值|JESSOHRUL/full.txt L1306–1313 全局说明五次运行后报告平均，后续结果段并不在每个指标前都重写 mean。BMSFormer/full.txt L1707–1709 以表注说明 Cell1 的十次平均，结果段直接讨论其指标。范文也依赖协议/表头提供均值身份。|本文表头 mean±SD 已清楚，当前范围自然可理解为三方案表中中心值。**降为可选**，不判确定语法错误；如采用，只在首次概括加 mean，不必三个指标及 performance 重复四次 mean。|
|SR03 初始化/收敛重复次数和统计单元|JESSOHRUL/full.txt L1306–1313 确实给 independent runs/random seeds/averaging；Engineering-AI/full.txt L1251–1330 的收敛段则给两个代表电池、单曲线阈值和末20轮SD，没有在这段报告重复次数。BMSFormer/full.txt L1707–1709 的十次只在 Cell1 表注，而非全稿每节重申。|范文并非每种收敛图都交代重复数，旧要求若泛化为所有段必须重复则过细。但本文明确报 mean±SD、median[range]、every training run，涉及跨运行层，和范文单轨迹描述不同。**保留最小待核**：这些统计跨什么、多少个单位；已写的最后20轮不要再次要求补。无需新增实验、显著性检验或复制范文五次。|
|TR01 R²/RMSE 隐含方差关系|BMSFormer/full.txt L1232–1305 把 ARMSE 表述为跨子集/划分平均，又把 m 解释为电池数，说明范文也可能存在统计层表述不完全精确，不能视作无歧义标准。JESSOHRUL/full.txt L1306–1313 的独立运行平均则说明汇总指标本就可能不服从单次恒等式。|**保留待核，不判错数**。本文问题基于同一测试电池、本文公式和两组具体显示数值的条件性冲突，不是要求比范文写得细。若确认为分别跨运行平均，则不能用单次恒等式指控错误；只需最小说明其均值身份。本轮未重算三范文全部 R²/RMSE，因此绝不声称范文数值完全满足该恒等式。|

## 相似省略不等于相同错误

本次确实找到相同写法和相同省略，但未把范文当作正确性豁免。应区分：

1. **可由相邻上下文消解的省略**：R05/R06/R07/R08/SR02 不应继续列为需要作者逐项确认的错误。
2. **建议可更清楚、但并不必需**：R02/R03 的表注部分/R04，默认保留原意和正常篇幅，不要求增加实验或冗长限制语。
3. **有本文具体证据触发的事实核实**：SR01 的评价集合可能变化、SR03 的跨运行统计、TR01 的指标层级。问最少必要信息，确认后再决定是否改文。

R03 过去引用 JESSOHRUL 的 FLOPs 定义只能说明某种指标定义方式，不能证明它对 Average/Reduction 也要求逐项定义。本报告用真正对应的消融表校正该不足。R02 过去只选范文局部图论证，也漏看了同篇直接把整体 RMSE 用在晚期轨迹讨论的实际做法，此次一并纠正。

## 读取边界

本次读取了当前英文第4章结果/消融/复杂度上下文、两张消融表、三轮结果报告；范文重点重新读取 Engineering-AI 结果的初始化、局部轨迹、完整微观消融及资源权衡上下文，JESSOHRUL 运行协议、HI比较、完整消融和复杂度小节，BMSFormer 评价指标、Oxford结果及效率配置/表格上下文。TXT双栏提取错序没有拼接作“完整连续原句”；以上引用采用可识别的内部连续段或表题/表头。未渲染PDF或重排跨栏逻辑，未声称完成三篇数值审计。报告只做旧问题分级，不新增范文问题清单。
