# 图表文字与全篇术语一致性：英文语言审校

日期：2026-09-13。按作者最新阶段要求，仅审校现有英文，不重新翻译，不修改论文。本轮主审重新通读英文摘要及第1–5章，读取22个表格、11个图题、共享宏及主文件的现有文字；重点语言问题所在的fig1.png、01.png和fig3_3_attention_comparison.png再次目视核对。其余图片沿用同日已完成的图片记录，不声称本轮再次逐图复查。

## 本批重新阅读的范文依据

- BMSFormer：full.txt 441–459、500–524，HI提取/选择及PCC比较；1344–1376、1385–1398，资源指标、训练设置和层配置。1344段后的公式定义及1370标题存在双栏穿插，本报告只取明确连贯句/短语，不据TXT次序模仿段落推进。
- JESSOHRUL：full.txt 1576–1588、1640–1696、1797–1834、1946–1959，HI曲线、筛选操作、输入方案比较。1797与1822跨栏恢复仅作为算法背景，以下引用的1829–1834连续表达可辨识；不照搬范文阈值或电池角色。
- Engineering-AI：full.txt 878–926、2806–2850，局部/全局模块与资源总结。仅用于功能/术语边界；有跨栏片段，未把TXT行顺序当完整结论段落顺序。本文不引入其硬件验证结果。
- 术语以本目录terminology.md为统一表，不新建另一套词汇。范文短引的中文解释均为助手释义。

## 建议项

### LT01：输入本身不会产生估计误差，明确输入与模型结果的关系

位置：tables/table_4_hi_input.tex，表题。

现有英文：

> SOH estimation errors of different health-indicator inputs on the Oxford dataset.

建议英文：

> SOH estimation errors with different health-indicator inputs on the Oxford dataset.

范文依据：JESSOHRUL full.txt 1946–1959完整输入方案比较，1956–1957的短语“all four HIs are fed into the model together”（四个HI一起送入模型）明确输入→模型→结果关系。本句是语义适配，不冒充范文原句。

简短中文原因：不是词难，而是of把errors归属于inputs；改为with直接说明使用不同输入时的误差。保留SOH、不同输入、Oxford及比较功能，不更名HI或增加结果。六层复核：仅修搭配关系；短表题无需模拟句间推进，其余信息和力度不变。

### LT02：表头用具体指标编号，减少来回查正文

位置：tables/table_2_6.tex，第二列表头。

现有英文：

> HI

建议英文：

> HI1

范文依据：BMSFormer full.txt 503–507在PCC比较中明确所选HI的具体恒流时间指标；523–524表题“PCC comparison of different HIs”说明比较功能。本文第2章最后小节已明确该列为HI1，编号取自本文，不从范文迁移。

简短中文原因：可选清晰度，不是误译。单独的HI需读者回看正文才能确定所指，HI1直接定位该列，数值和比较对象不变。六层复核：术语缩写一致；只显化现有指代，不改变主干/颗粒度/力度。

### LG01：流程图的名词修饰与动作顺序

位置：figures/fig1.png。以下均为图中短标签，不合并为新正文段落。

|现有英文|建议英文|性质及简短中文原因|
|---|---|---|
|Health indicators extraction|Health indicator extraction|建议修正名词修饰搭配；不改变提取对象或整个算法的正式名称|
|others Cells|Other cells|明确语法错误；other修饰cells，others不能直接修饰名词|
|Four datasets dividing|Data partitioning for the four datasets|建议修正搭配，让划分的对象/操作可读；four保留；具体角色仍按正文，不新增独立测试集|
|Health indicators splitting|Windowing of HI sequences|条件性建议：图中确为HI序列的滑窗切分，与第2、3章一致；若绘图作者另有所指则先核实|
|Five models training, validating and testing|Training, validation, and testing of five models|仅修名词短语，五个模型保留；validation与本文configuration-selection的关系仍需按实际图示角色核实，不能把这条语言建议当作数据划分已通过|

范文依据：BMSFormer full.txt 441–459的HI extraction和window size，以及JESSOHRUL full.txt 1576–1584的数据→曲线→HIs的提取过程，支持具体操作+明确对象。BMS标题本身使用复数修饰的“Health indicators extraction”，此处不机械照抄其语法。数据划分的精确角色为本文特有协议，三篇范文不提供代换依据。

六层复核：修的是名词修饰和动作—对象顺序；窗口术语显化图中已有操作。没有改变阶段次序、模型数量、训练条件或结果力度。需核实的协议项不作为可直接写入的定稿。

### LG02：图内模块名称与正文统一

位置：figures/01.png及figures/fig3_3_attention_comparison.png。

|现有英文|建议英文|性质及简短中文原因|
|---|---|---|
|L-DSConv|DSConv-L|01.png内名称与本文第3章定义不一致；统一为本文已用名称，不能因EAI用L-DSConv改正文|
|Skim Local-Global Fusion Attention|Slim Local-Global Fusion Attention|注意力对比图(d)的Skim与SLFA正式定义不符，应修拼写|
|Embed layer|Embedding layer|与正文和配置表统一层名称；不新增层|

范文依据：BMSFormer full.txt 508–514明确使用DSConv-L、DSConv-S及Local-Global Fusion Attention；Engineering-AI full.txt 898–901使用L-DSConv，但它是另一篇模型的命名，不能作为本稿轮换词。Slim全称是本文专名，以本稿定义为准，不虚构范文同名。

六层复核：仅术语/拼写一致性，不动图的运算路径或模型边界。特别是图(d)DSConv-L放在K/V支路与正文DSConv-S→局部表示→双分支不一致，必须核实际实现，不能只把图上L改成S便宣称已解决。

## 待核实，不提交确定改稿

|位置|现有英文/问题|为何不能仅凭语言偏好修复|
|---|---|---|
|table_2_1，Oxford放电协议|variance|这是“方差”而不是清晰协议名称；正文为动态ARTEMIS工况，但需确认表格原始意图后才替换，不能凭近义猜成variable|
|table_2_hi_screening_steps，第5步|compare ... each；if ... both ...；otherwise ...|需要明确是否“任意一个已选HI同时满足两个组平均阈值便排除”，以及otherwise发生在每次比较还是全部比较后。JES full.txt 1829–1834支持排序和冗余剔除功能，不能证明本文量词逻辑|
|table_4_10，Average/Reduction|缺少显式比较基准和聚合口径|数字精度与Reduction分母应由实际计算确认；不能为了表题简洁猜公式|
|fig1，Battery role assignment|下面是Prismatic/Cylindrical/Pouch类型|若表示封装类型，Cell types更贴切；若设计者要表达实验角色，需调整图示含义，不是单纯换词|
|01.png，Turn/Back/Gate|非标准操作名或与可学习缩放混淆|确认转置与逆转置的实际位置后再命名；Gate不得擅解读为额外门控|

这些问题在前一轮回译附件也有记录；本轮将其保留为歧义/图文核实项，不用语言建议掩盖技术未决事项。

## 全覆盖保留记录

以下“保留”指本轮未发现需新提语言修改的明确问题，不代表实验或数据经重新验证。所有数据、引用键、公式、图片路径、命令均不建议修改。

|文件|本轮结论|
|---|---|
|table_1_comparison|保留；Estimation model在SOH语境成立，既有HI算法全称不得简化|
|table_2_1|除上述variance待核，其他表头/材料/协议名称保留；排版大小写不作必改|
|table_2_2|15项定义保留，FWHM、DTV/DTC、discharge capacity等不因词长简化|
|table_2_3、table_2_4、table_2_5|保留；当前主稿未调用，仅目录附属文件|
|table_2_6|LT02可选，其余保留；绝对PCC与一般相关性不混称|
|table_2_hi_screening_steps|第5步量词待核，其余保留；retain/sort/output已经直接|
|table_4_1、table_4_2、table_4_3、table_4_3_initialization|保留；table_4_2未调用；标题/阈值与聚合名称可读，不能只为短改去必要限定|
|table_4_4|保留；Layer configurations有BMS对应原词依据|
|table_4_5、table_4_6|保留；误差比较表题与配置电池脚注对象清晰，不能把配置电池改称独立测试电池|
|table_4_7、table_4_8、table_4_9|保留；直接迁移与目标域适应在上下文可区分，不强行给每个短题加全套协议|
|table_4_10、table_4_11|Average/Reduction的定义待核；其他模块/指标名保留|
|table_4_12|保留；FLOPs、training time、parameters、storage是四种不同资源量，不能宣称全部速度最优|
|table_4_hi_input|LT01，其余保留|
|figure_2_1、figure_2_2、figure_2_3、figure_2_4|图题保留；面板映射具体，charge-side已明确侧别，不只为偏好换词|
|figure_3_1、figure_3_2、figure_3_3|图题保留；图内LG02及技术路径另列，不通过改图题隐藏|
|figure_4_1|保留；未调用的附属文件，不把validation RMSE嫁接为当前实验|
|figure_4_2、figure_4_3、figure_4_4|保留；数据集、模型比较、测过的宽度范围明确|
|comparison_panel_layout.tex|共享排版宏，无待审学术行文|
|main.tex|章节名称保留；Methodological framework在章内容语境可接受，不为逐字回译改名|

## 统一边界

保留health indicator extraction与selection的区别；完整算法始终使用作者确认的multi-source health indicator extraction and optimization algorithm。保留lightweight/efficient、cross-cell/cross-dataset、source-only/few-shot、weight storage/memory、parameter count/training time的概念边界。already clear的句子不为了“更像范文”换近义词。图内错误可修，但当前只交付建议，无任何图/表/正文写入。

