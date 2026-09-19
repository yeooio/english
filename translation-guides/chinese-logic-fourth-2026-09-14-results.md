# 第四轮复核：第4章中文逻辑、英文承接与旧建议保义

日期：2026-09-14。仅新建审查报告，论文中英文、表格、图像及公式均未修改。

## 结论

本范围本轮 **0项新增确定错误，0项新增待核技术问题**。这不表示前三轮待核问题已经解决，也不保证零遗漏。重新审查的价值在于排除重复报错和防止旧建议改过头，不应每轮为了数量制造新问题。

复核覆盖中英文第4章全文、当前调用的结果与配置表，并查看未调用的table_4_2以区分当前正文和辅助材料；对照9月13日whole-manuscript-review、前三轮主报告及结果附录中的已知问题。未查看实际训练代码、预测数组或本轮图像像素，故不能独立认证图形描述或实验实现。本报告不声称重新复现全部数值。

## 一、因果、转折和比较：审后保留

### 1．“不能保证”不能被改成“不能”

位置：[中文第4章L45](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:45)、[现英文L45](D:/MS-AgentNet-English/chapters/chapter04.tex:45)。

中文原句：

> 上述结果表明，单节电池上的高相关性不能保证健康指标在组内其他电池上保持相同的表征能力，而组级筛选得到的 HI1 在该组 Oxford 电池上提供了更稳定的 SOH 估计输入。

现英文：

> These results show that a high correlation on one cell does not guarantee the same representational capability on other cells in the group. The group-selected HI1 provides a more stable input for SOH estimation on this group of Oxford cells.

改后：中英文均保留。不能改成“单节高相关HI不具备跨电池表征能力”，也不能将当前输入对比写成已经隔离了组级筛选算法本身的因果贡献。现文以does not guarantee保留了“非充分条件”的意思，且最后限定该组Oxford，未声称所有数据集必然如此。表4_hi_input中的HI9/HI11相对次序在Cell7/8反转，与该谨慎叙述一致。

本轮重读[JESSOHRUL full.txt L1946–1988](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1946)：其比较段明确四项输入、Fusion及所用模型。借鉴的是具体方案与对象对应，不能照搬其Fusion排名或把范文研究结果当作本文因果证据。TXT结果段跨栏，未据此拼接段落推进。

### 2．“尽管LSTM训练更快”是权衡，不是“训练快导致精度低”

位置：[中文L170](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:170)、[英文L170](D:/MS-AgentNet-English/chapters/chapter04.tex:170)。

中文原句：

> 尽管 LSTM 在统一复杂度测试中以 44.568 s 取得最短训练时间，但其对复杂退化模式的刻画仍有局限，整体 SOH 估计精度相对较低。

现英文：

> Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low.

改后：连接关系保留。although和“尽管……但……”在此表达两项性能之间的对照，没有因为/因此式机制归因；不应作为新中文因果错误。精度与资源配置不同的旧R04仍需限定归属，但不能据此删去LSTM训练最短这一不利于本方法的事实。

本轮重读[BMSFormer full.txt L1331–1395](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:1331)的复杂度定义与设置说明，其分别讨论accuracy、training time、parameters和storage，支持分项陈述。不能把范文的fair comparison措辞搬来证明本文配置等价。数值依据是本文table_4_12，不是范文。

### 3．“与设计目标一致”并非已证明唯一机制

位置：[中文L158](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:158)、[英文L158](D:/MS-AgentNet-English/chapters/chapter04.tex:158)。

中文原句：

> 这一结果与 DSConv-L 进行长尺度特征细化的设计目标一致。

现英文：

> This result is consistent with the design goal of DSConv-L to refine features over longer time scales.

改后：保留“consistent with”。第二轮S-IC01关于实际输入范围与长尺度表述的待核项仍在，不能在未确认N的情况下宣布解决；也不能将本句进一步改为“证明长核捕获长期退化，因而造成误差下降”。当前措辞是在报告结果与设计意图的相容关系，不是唯一机制证明。

本轮重读[Engineering-AI full.txt L1376–1451](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:1376)，可见其局部曲线讨论和机制解释。本文不机械继承其中“driven by”等更强归因；已有consistent with比强机制归因审慎。该范文段不是本文长核作用的实验证明。

## 二、旧建议的保义复核，不计新增

|旧编号|本轮再次确认的边界|
|---|---|
|R02，整体MAPE与尾段结论|若采用“overall prediction errors on this cell”，只能替换L107数值之后的结论，不删除L105已有局部图观察。若作者要保留尾段数值结论，则先核实局部证据。|
|R04，精度与资源归属|原两句建议保留“高精度”及“低于四种基线”两项结果，分别注明主比较/复杂度测试；不能简化成只有“模型较轻”。学习率不同本身不会改变参数数量，不能宣布资源表无效。|
|R06，Fusion比较对象|“直接组合这四项HI，相比HI1单独输入无进一步收益”只明确原段最自然的基准，不改成“所有特征融合无用”；Fusion优于DTV的结果保留。|
|R07，适配比例范围|四个已测试比例下单调下降的观察保留；补测试范围是防外推，不应删掉逐档改善这一原有事实。旧句“improves ... across the tested adaptation ratios”仍可读，不另造必要语言修改。|
|SR02，初始化均值|加mean由现表头mean±SD直接支持；不改成统计等效，不把普通正态默认选择改成精度最优。|
|SR01/SR03/TR01|评价电池集合、重复运行及指标聚合仍需原始记录；本轮没有新证据，不把推测写成确定实现，也不重复计数。|

旧R03的Average与Reduction定义、R05表标题范围亦仍保留。未调用table_4_2中出现全连接维度，并不能自动把这些数值写入当前主实验，需确认版本；这是既有辅助材料/配置边界的提醒，不另外统计新问题。

## 三、为什么此轮不再新增“改前改后”

经过三轮发现与本轮针对性复核，本范围尚未找到具有新证据、且未被历史报告覆盖的语言或逻辑缺陷。上列中英原句的改后是“保留”，而非故意改成另一种同义表述。需要实验记录才能闭环的问题继续保留待核；增加阅读次数本身不能替代那些记录。

参考段落均在本轮重读；没有宣称范文全文逐句计数或PDF双栏重排，也没有将范文语气当成本文科学结论的授权。
