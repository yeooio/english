# 第2章与HI结论术语一致性复查（2026-09-16，只读建议）

已读：当前中英文第2章；英文第5章；第2章实际引用的4张表及4个图题；当前术语表及approved-translations相关批准条目。视觉检查fig1.png、fig3.png。本批重读BMSFormer full.txt:415–507（数据集、窗口HI提取完整段落），Engineering-AI:300–429（数据采集、窗口标定完整语境），JESSOHRUL:1620–1697、1773–1850（HI定义与筛选上下文）。范文双栏错序处只用明确连续的句子和表内词组，不从错序推断句间习惯。未改论文。

## 建议统一（并非每项均为技术错误）

1. **充电时间特征名称**：chapter02.tex:58 `charge duration feature`、:60 `charge timing features`，对照chapter01.tex:21、:44已批准的`charging-time feature(s)`。建议在指称特征类别处统一后者；:58也可直接`the resulting CCCT feature`。范文：BMS §2.3 full:457–459 `constant current charge time (CCCT) series`；JES表4 full:1637–1638 `The charge time within the voltage range...`；EAI full:327谈`CC phase duration`，但其特征为积分面积CCCA，不可照搬。同条件：前两篇都把时差作为HI，支持time；EAI仅物理时长同条件。chapter02:52描述持续时间的`charge duration`保留，不要求所有duration消失。批准记录:102明确引言charging-time features，但并未单独批准chapter02的timing版本。

2. **材料体系**：chapter02.tex:13、:23 `material systems` → `battery chemistries`，与chapter01:27及chapter05:5一致。中文两处均“材料体系”，紧接数据集明确NCO/LCO/LFP。JES §3.5.2 full:1786–1796确用`different battery chemistries`；EAI数据采集full:317–318及图2:369–371用`battery chemistries`；BMS full:426–439用`battery materials`。范文本身有材料/化学体系两种表达，因此不是现译错误；按本项目已选首选统一，依据terminology:92及approved-translations:20/56。不要把同段`battery systems`（连同封装、规格在内的较宽概念）和表中`Cathode material`机械换掉。

3. **筛选步骤名称**：tables/table_2_hi_screening_steps.tex:3/7 `Group-level health indicator screening` → `Group-level health indicator selection`；对应chapter02:143节题和:155 `group-level HI selection method`。JES §3.5.2 full:1797命名`HI selection algorithm`，1833–1834则把流程描述为`screening procedure`；BMS §2.3是窗口搜索，EAI §3.3.2是`Multi-scale sliding window screening strategy`，均非本文HI集合筛选名。建议仅统一本步骤标题和正式称谓，不禁止普通流程叙述使用screening。整体算法仍为作者已定`multi-source health indicator extraction and optimization algorithm`，不得缩成HI selection algorithm。

4. **最终筛选输出**：tables/table_2_hi_screening_steps.tex:17 `final selected HI set`与chapter01:44 `health indicator combination`，若严格统一可用`final HI subset`（terminology:44/85，JES full:1829–1834）。表:12中间态`selected HI set`可保留，因为集合仍在构造；不要给中间状态加final。JES同样从候选集筛选，条件相同；BMS/EAI主要选一个时间或积分窗口，不强加它们的单HI叫法。当前组合/集合含义清楚，本项为规范性统一而非技术错误。

5. **PCC对应关系**：chapter02:108两处`linear association`可统一`linear correlation`，与本章:162及terminology:46一致。JES full:1671–1680明确`PCC measures the linear correlation`；BMS full:451–454用PCC选窗；EAI full:396–422以PCC评估特征与SOH。三者计算对象同类。只是统计术语首选统一，不意味着association本来错误，也不应把所有association（尤其泛指HI与SOH关联）全文替换。

## 图内旧名（视觉确认，优先级高于上列普通词统一）

figures/fig1.png（由figures/figure_2_1.tex:4引用）：模型小图仍写SLFA、SLFA features、L-DSConv；正文当前正式名LLGFA、DSConv-L。approved-translations:29明确LLGFA为正式英文名，中文冻结稿SLFA是历史名，不是保留图中旧名的理由。图底部还有Cross-battery、Source-only testing、Model size，对应正文cross-cell、source-only evaluation、weight storage size（最后一个需按图中具体测量对象统一）。这些是同一图对同一模型/实验的不同名称，不是范文不同条件。图中Health indicators extraction宜随正文正式步骤改Health indicator extraction；Health indicators splitting实际表示HI序列滑窗分段，可用HI sequence segmentation，避免看成筛选指标。

## 核实后保留

- CCCT、CVT、IC、DTV、DTC在本章正文与表2-2定义一致。DTV=`differential temperature--voltage`、DTC=`differential temperature--capacity`与JES表4 full:1639–1647对应。
- chapter01引用Dai文献的`differential thermal voltammetry`已在approved-translations:90批准，terminology:195要求与本文DTV按语境区分；不要统一成一个长名而篡改所引文献的称谓。
- CCCT的全称/缩写、health indicator(s)/HI(s)、PCC/SCC全称/缩写属于正常缩写变化。
- voltage interval / voltage window无需无条件二选一。EAI同一完整方法段既用candidate window（396–397），也用optimal interval（377–380、417）；BMS也在窗口搜索与具体segments间切换。本文区间端点、窗口搜索、序列滑窗、平滑窗口的对象不同，强行统一会降低清晰性。
- window width、step size与BMS的window size、moving step size语义对应；当前分别表达电压宽度、步长，范文自身引言使用step size，本轮不判为专名多版本。
- 结论HI部分整体算法名称、MS-CCCT、PCC/SCC、dual-threshold admission、redundancy removal与第2章一致，未发现另外命名一套算法。
- charge/discharge energy efficiency指电池能量比，不能与模型computational efficiency归一。rated capacity与nominal capacity由冻结中文不同用词决定，不作为同义词机械互换。

## 第二轮：按作者最新要求排除图旧名，重审专业概念（2026-09-16）

此轮仅看专业词本身，上列图旧名不纳入本轮结论。以下新结论覆盖上文相应优先级，不删除历史判断。

- **撤回linear association作为未对齐候选**：扩大核对发现BMSFormer full:520–522原文正是“The PCC is a widely utilized statistical metric for evaluating the strength of linear association between HIs and true SOH”。本文chapter02:108在相同PCC定义语境采用linear association，已复用范文。JES用linear correlation是另一范文变体；即使术语表偏好correlation，也只属可选内部统一，不能称为没有复用专业术语。
- **主要建议保留1项**：chapter02:60 `charge timing features` → `charging-time features`。本段承接CCCT时差特征，time确对应特征物理量；timing更容易理解为事件发生时机。BMS:457–459、503–504和JES:122–138、1637–1638均以charge/charging time为此物理量。chapter02:58的duration feature语义准确，只为名称一致时一并调整，不能把duration说成误译。
- **selection/screening降为可选**：JES同一筛选完整上下文同时用HI selection algorithm（1797）和screening procedure（1833–1834）；EAI更把screening写进正式策略标题（332）。本文已有health indicator selection作为节题，并未把提取和筛选混淆。若用户只要真正专业术语缺口，则不把screening独立列为问题。
- **曲线名称已对齐**：JES §3.5.1 full:1575–1590列IC、CVT、DTV、DTC，表4 full:1634–1647列峰、峰位、谷、谷位；本文对应名称准确，charge→charging、连字符和大小写只是正常语法/排版。本文CVT曲线与其提取的CCCT时差已有明确区分，不应因JES公式也把CVT写成时差就继承这种模糊写法。
- **不将本文新增特征改名为范文已有但不同的特征**：full width at half maximum、peak-to-valley difference、窗口放电容量和energy efficiency各对应不同定义；范文只列峰值/峰位并不意味着本文应改成它们。EAI full:720–722有CCCQ/CCDQ（charge/discharge quantity），但这是其文献比较表标记，不能据标签就把本文窗口容量改作CCDQ，更不能以其CCCA/CCDA面积指标替代CCCT时间。
- **表4的类别缩写已消歧**：tables/table_4_hi_input.tex:54说明CCCT/IC/DTV/DTC对应HI1/HI4/HI9/HI11，表头不需要展开到每个特征的长名称；其表示输入类别，不与第2章曲线名称冲突。
- **最终等级**：HI方向没有大面积专业名称未复用。最值得改的是timing→time；material systems→battery chemistries是跨章规范统一；其余多为已使用范文词、正常缩写或本文独有定义，应保留或降为可选。
