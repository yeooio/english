# 全文英文语言与范文风格审查

日期：2026-09-13。性质：只读审查与替换建议，未获准写入正文。当前状态：分章审查与独立最终复核完成，结论：通过（指建议稿边界检查通过，不代表论文无需修改）。

最新实施状态（覆盖下文历史待确认说明）：作者在看到4处完整改前/改后后回复“可以改动”。已且仅已应用A2、C1、F3、D1，涉及chapter01.tex、chapter04.tex、table_2_1.tex；其他建议未应用。目标文件修改前快照与修改后内容逐字比对确认仅这4处差异，独立只读复核通过。XeLaTeX/latexmk编译成功，输出37页；PDF第8页表格渲染检查通过。检查器chapter04及表2通过，chapter01提示42/100为中文相邻字符导致的数字识别差异，冻结中文第11行已有两数，本轮未改该段。现有ICC及字体重定义警告保留，无未定义引用、缺字或溢出警告。下文改前文本作为审查历史保留，不是当前正文。

首轮：13项审查记录，其中10项建议修改、2项可选优化（A5、C4）、1项已被其他操作修复并保留（B1）。第二轮在F节补充7处：3项建议修改、4项可选改善。累计20项记录，19项待作者选择、1项已解决；这是本轮发现清单，不是“未列出的句子全部无误”的保证。建议先看A2（精度依赖对象）、C1（FLOPs计数对象）、C2（资源数值搭配）、D1（表格variance）及F3（比较动作主语）。

## 范围与总判断

已通读摘要及第1—5章英文正文；核对相关冻结中文和三篇范文对应原文，并检查主文调用的图题、表题及表头文字。不是重新翻译、反向回译、实验有效性审计或排版验收。本轮未逐图读取栅格图内部文字，未核验参考文献题名/元数据，未重新编译，不能据此宣称图内英文或投稿格式全部通过。

全文主线清楚：先通过多源HI构建、组级窗口标定和双相关筛选改善输入的跨电池稳定性，再以MS-AgentNet融合局部与长期信息，兼顾估计表现与资源开销，并通过迁移实验交代适应边界。

语言整体可用，不需要整篇重译。需要处理的主要是：动作堆叠、长插入语、并列对象不清、抽象搭配以及个别表格残留词。不能笼统判定整篇比三篇范文更绕；本文许多步骤句反而更规整。建议只修改下列可定位问题，不按字数或修改数量衡量质量。

判定标准：每处保持原信息、条件、数值、术语、引文和主张力度；同段分句不等于拆段。不改章节组织，不删实验，不增加硬件、机理或统计主张。建议英文是针对本文的适配，不冒充范文原句。

## 三篇范文的实际对齐依据

| 范文 | 本轮重查的对应功能 | 保留的颗粒度与语言习惯 | 不继承 |
| --- | --- | --- | --- |
| BMSFormer | 摘要、模型综述、模型数据流、复杂度、结论 | 摘要写模块及直接功能；方法按输入与中间表示推进；复杂度写测量对象、工具、配置和比较量 | 个别不自然搭配、泛化过强的部署推断；不因其摘要较短而删本文信息 |
| Engineering-AI | 摘要、ECM综述、HI标定、模块分工、效率结果、结论 | 明确accuracy等依赖对象；交代局部模块与全局模块的作用；按具体资源指标表达轻量化 | 大量预防性说明、无本文证据支持的硬件/安全结论、噪声与物理机制归因 |
| JESSOHRUL | 摘要、HI来源及筛选、符号解释、消融、复杂度、结论 | 写清曲线来源、相关对象、保留/排序/剔除动作；明确指标与数值的对应关系 | 重复总结优越性、部分语法错误和过强解释；不移植RUL任务 |

协议、结果、解释颗粒度均以本文现有内容为边界。范文摘要是否含数值，不决定本轮给本文摘要新增数值；方法所需参数与公式完整保留；结果不删现有百分比，仅理顺句法。范文在本报告中支持表达方式，不是本文数据或结论的证据。

## A. 摘要与引言

### A1 摘要第7句：四个动作挤在同一句

位置：[abstract.tex:1](D:/MS-AgentNet-English/chapters/abstract.tex:1)。任务：交代大核作用及大小核共同融合。类型：微调，建议替换；仍在同一摘要段落。

原文：
> Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity.

建议稿：
> Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales. Together with small-kernel convolutions, they fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity.

原因与效果：先读到大核的提取作用，再读到联合融合，不再连续跨越extract/work with/fuse/enhancing。长尺度、参数开销和多样性均保留。

范文依据：[BMS摘要L35](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:35)以卷积为对象交代融合；EAI摘要L38—41写模块组合及功能；JES摘要L38—43分开交代模型功能与HI处理。本文比BMS多一项长尺度提取任务，不能为模仿句数强塞进一句。

### A2 引言ECM段：依赖对象不清

位置：[chapter01.tex:9](D:/MS-AgentNet-English/chapters/chapter01.tex:9)。任务：说明ECM估计精度的限制。类型：微调，建议替换。

原文：
> Compared with electrochemical models, ECMs may provide lower estimation accuracy and depend on the selected circuit structure and model parameters.

建议稿：
> Compared with electrochemical models, ECMs may provide lower estimation accuracy. Their accuracy depends on the selected circuit structure and model parameters.

原因与效果：and depend的主语原来是ECMs；中文要说明的是精度依赖结构与参数。明确accuracy为主语，保留may，不加强比较。

范文依据：[EAI L129](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:129)直接写“their accuracy depends on the fidelity of the circuit structure”；BMS L134—136单独说明精度可能较低。

### A3 引言HI来源段：并列来源被长列表隔开

位置：[chapter01.tex:19](D:/MS-AgentNet-English/chapters/chapter01.tex:19)。任务：列明指标来源。类型：微调，建议替换。

原文：
> These indicators are mainly extracted from operating data, including voltage, current, temperature, time, and internal resistance during battery cycling, and their derived curves\cite{ref47,ref48,ref49,ref50}.

建议稿：
> These indicators are mainly extracted from battery cycling data (including voltage, current, temperature, time, and internal resistance) and curves derived from these data\cite{ref47,ref48,ref49,ref50}.

原因与效果：明确“数据”和“衍生曲线”两项来源，避免读到their时回找指代。全部数据类型与引文保留。

范文依据：[JES L105](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:105)将HI提取直接连接到循环曲线；BMS L145—146把数据类型列举置于data之后。括号是本文适配，不称范文原句。

### A4 引言综合比较：句尾限定可能挂错对象

位置：[chapter01.tex:27](D:/MS-AgentNet-English/chapters/chapter01.tex:27)。任务：连接性能、复杂度与部署。类型：微调，建议替换。

原文：
> For models, complexity is directly related to practical deployment, in addition to estimation performance.

建议稿：
> Both estimation performance and model complexity are directly related to practical deployment.

原因与效果：原句容易被读成复杂度还与估计性能相关；并列主语直接对应中文“除估计性能外，模型复杂度同样直接关系到实际部署”。

范文依据：[JES L259](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:259)将model complexity and accuracy并列，再关联计算资源；EAI L108—111直接连接工程可行性与精度。

### A5 引言贡献3：主语过长

位置：[chapter01.tex:48](D:/MS-AgentNet-English/chapters/chapter01.tex:48)。任务：说明验证范围与评价维度。类型：微调，可选调整；原句语法可成立。

原文：
> Experiments on multiple public datasets with different battery materials, capacities, and charge-discharge protocols, together with module ablation and complexity analysis, jointly evaluate the estimation accuracy, computational efficiency, and cross-cell generalization of the proposed method.

建议稿：
> Experiments are conducted on multiple public datasets with different battery materials, capacities, and charge-discharge protocols. These experiments, together with module ablation and complexity analysis, evaluate the estimation accuracy, computational efficiency, and cross-cell generalization of the proposed method.

原因与效果：先说明实验范围，再说明综合评价内容，主干不再等到长列表结束才出现。不拆贡献段，也不改变贡献数量。

范文依据：[JES L303](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:303)以实验为主语交代多数据集验证；EAI L154—159分句交代验证与进一步分析。删除jointly仅去掉与together with重复的联合含义；后者仍承载该信息。

## B. 第二、三章

### B1 第二章能量效率符号释义：已由并行修改解决，当前保留

位置：[chapter02.tex:98](D:/MS-AgentNet-English/chapters/chapter02.tex:98)。任务：准确对应符号和物理量。类型：已解决、保留。交付前哈希复查发现该文件由本任务以外的操作更新；已重新通读第二章，当前已分别说明两组符号，不再重复提出替换。

当前正文（保留）：
> where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$ denote the terminal voltage, current magnitude, and duration of charging, respectively; $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote those of discharging. The full charging and discharging phases of each cycle are used. This energy efficiency is denoted as HI15 ($\eta$).

以下为审查历史，不再作为待应用建议：

原文：
> where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$, and $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote the terminal voltage, current magnitude, and duration of the charging and discharging phases, respectively.

建议稿：
> where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$ denote the terminal voltage, current magnitude, and duration of the charging phase, respectively. The corresponding quantities for the discharging phase are $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$.

原因与效果：连续两个and将两组三元列表连在一起，respectively需要回读。按充电、放电分别解释，保留全部符号与含义，不拆段。

范文依据：[BMS L788](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:788)采用单组符号对应释义；JES L1771—1772先解释秩符号，再解释样本量。借清晰对应方式，不复制个别语法错误。

### B2 第二章HI相关性差异：非相同不如直接说不同

位置：[chapter02.tex:149](D:/MS-AgentNet-English/chapters/chapter02.tex:149)。任务：引出HI5的跨电池数值差异。类型：微调，建议替换。

原文：
> The same candidate HI does not show identical correlation performance on the two cells.

建议稿：
> The same candidate HI shows different correlations on the two cells.

原因与效果：does not show identical ... performance将简单事实绕成抽象否定。直接说相关性不同，不增加差异程度；后续所有例子与数值保持。

范文依据：[JES L1778](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1778)直接描述同一HI在两个电池中的相关性差异，随后用PCC/SCC数值举例。

### B3 第三章局部分支：归一化后的对象需明确

位置：[chapter03.tex:108](D:/MS-AgentNet-English/chapters/chapter03.tex:108)。任务：说明局部表示进入融合阶段的路径。类型：微调，建议替换。

原文：
> The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

建议稿：
> The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage. There, it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

原因与效果：先交代归一化及传递，再交代融合；明确it指向归一化后的表示。保留互补关系、全部动作与顺序，仍在原段。

范文依据：[BMS L736](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:736)分别以输入及模块输出推进数据流；EAI L845—848先交代中间特征进入模块，再解释变换。只借数据流写法，不借其机制主张。

复核后保留：第三章L288的$3d^2$与$3d$比较虽然前置较长，但语法成立、条件明确。本轮不采用“为了让本方法数字先出现而重排”的备选；L265的计算顺序与复杂度说明、聚合与广播起句也保留。

## C. 第四、五章

### C1 第四章FLOPs统计：被补计、换算的对象不清

位置：[chapter04.tex:166](D:/MS-AgentNet-English/chapters/chapter04.tex:166)。任务：说明测量口径。类型：微调，建议替换。

原文：
> FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass.

建议稿：
> Operation counts obtained using the \texttt{profile} function in the THOP library are supplemented with counts for attention operations and then converted to the number of floating-point operations required for a single forward pass.

原因与效果：原句像把FLOPs换算为FLOPs，又把数量和attention operations本身相加。明确“统计值→补充注意力计数→换算到单次前向口径”，保留工具和流程，不新增倍数或测量设定。

范文依据：[BMS L1360](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:1360)和[JES L3800](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:3800)均直接说明工具与single forward pass范围。补计步骤为本文特有，不冒充范文步骤。本建议澄清语言，不验证实现计数是否正确。

### C2 第四章资源数值：has FLOPs搭配生硬

位置：[chapter04.tex:170](D:/MS-AgentNet-English/chapters/chapter04.tex:170)。任务：报告三项资源指标。类型：微调，建议替换。

原文：
> In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models.

建议稿：
> In contrast, MS-AgentNet requires 0.045760 M FLOPs and has a parameter count of 4,643 and a storage size of 27.44 KB; all three values are the lowest among the five models.

原因与效果：requires对应计算需求，has对应参数量与存储属性；加上自然的冠词结构，使每个数值直接对应指标。所有数字、比较范围和排名保持。

范文依据：[JES L3826](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:3826)用requiring连接运算量与存储需求；EAI L2820—2822用a parameter count of连接参数量。本文继续使用已定storage size，不引入footprint轮换。

### C3 第五章相关结果来源：on的搭配不直接

位置：[chapter05.tex:1](D:/MS-AgentNet-English/chapters/chapter05.tex:1)。任务：回顾MS-CCCT标定依据。类型：微调，建议替换。

原文：
> Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs.

建议稿：
> Based on correlation results from the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs.

原因与效果：correlation results from明确指相关性结果的来源，对应中文“相关性结果”；不改电池角色、步骤或范围。

范文依据：[JES L1822](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1822)先写相关系数，再写筛选；L1843—1848交代同组多电池数据来源；结论L3867—3870保留相关筛选核心信息。完整搭配是本文语境适配。

### C4 第四章消融：两层前置引导

位置：[chapter04.tex:152](D:/MS-AgentNet-English/chapters/chapter04.tex:152)。任务：说明M2相对M1的变化及收益。类型：微调，可选调整；不是语法硬错。

原文：
> As shown in \cref{tab:4-10}, compared with the basic model M1, adding multi-scale DSConv in M2 reduces the combined average error by approximately 1.20\% on CX2 and 8.45\% on Oxford.

建议稿：
> As shown in \cref{tab:4-10}, M2 adds multi-scale DSConv to the basic model M1 and reduces the combined average error by approximately 1.20\% on CX2 and 8.45\% on Oxford.

原因与效果：不必经过表格引导、比较引导两层铺垫才读到主语；直接以M2为主语交代相对M1的模块变化。比较对象、约数和百分比不变，保留combined average error。

范文依据：[EAI L2290](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:2290)直接连接添加模块与误差变化；JES L3521—3525以模型为主语报告比较值。仅学主干，不继承因果强化措辞。

## D. 图表文字

### D1 Oxford放电协议栏的variance：不能照搬范文残留词

位置：[table_2_1.tex:21](D:/MS-AgentNet-English/tables/table_2_1.tex:21)。任务：说明放电协议。类型：术语修正建议，需作者确认；不是新翻译造成的问题。

原文完整行：
```tex
Discharge protocol\newline (rate) & variance & CC (1C) & CC (1C) & CC (4C) \\
```

建议行：
```tex
Discharge protocol\newline (rate) & Dynamic current profile & CC (1C) & CC (1C) & CC (4C) \\
```

原因与效果：variance表示方差，不是“变化电流”的协议名称。冻结中文表也已经含有此词，不能归责本轮翻译。建议依据本文第二章已有“源自城市ARTEMIS工况的动态电流曲线”，让表格描述与正文一致，不改变其他电池设置。

范文依据：[EAI L243](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:243)说明Urban Artemis drive cycle，并在L246—247使用dynamic discharging profile；本文dynamic current profile为根据自身正文的适配，不标为范文逐字原词。JES表格也出现variance，正说明原词不可无条件继承。

## E. 保留项与统一边界

- resource-limited已由作者确认，全文正文保持该写法；不因EAI使用resource-constrained而整体替换。
- long-range dependencies、long-term degradation trends、degradation features over longer time scales指向不同对象，不能合并成一个词。引言中的long-term dependencies有中文“长期依赖”依据，不仅凭字面不同判为术语错误。
- 第三章逐步数据流、大核差异说明与RAA计算说明总体清楚；保留公式、模块名、符号和必要说明，不因长而压缩技术定义。
- 第四章对非最优结果、负R²和适应局限的表达总体直接；不加防御性解释，不删除不利结果。
- 正文未检出absolutely、definitely、demonstrate及其词形。否定句does not guarantee不是保证性夸大，不能按禁词机械删除。背景中的ensuring需按整句与中文判断，不强行改成弱主张。
- 主文调用的图题和多数表题已简洁；只保留真实词义问题，不为变化轮换results/performance等表达。
- 新能源交通的已批准译法transportation powered by new energy sources仍有范围待明确，本轮不擅自缩窄为electric mobility。

## F. 第二轮补查：首轮遗漏与可选清晰度改善

第二轮重新核对现有章节和中文，重点查首轮未覆盖的搭配、指代、修饰与跨章同类问题。分组意见经主审核对；图表两项另经独立复核。下面区分真实修复与可选改善，后者不应作为强制改稿理由。

### F1 引言贡献1：C3同类问题未在引言同步识别

位置：[chapter01.tex:44](D:/MS-AgentNet-English/chapters/chapter01.tex:44)。任务：说明筛选依据。类型：微调，建议替换；是新增位置，不是新增问题类型。

原文：
> It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators using correlations on the feature-development cells.

建议稿：
> It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators based on correlation results from the feature-development cells.

原因与效果：明确“相关性结果来自特征开发电池”，并与C3的结论段修复一致。对应中文“以……相关性结果为依据”，不改变关联/冗余两项评价。

范文依据：[JES L1822](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1822)及L1843—1848，先交代相关性计算和数据来源，再说明筛选。完整建议为本文适配。

### F2 引言综合比较：抽象名词串联

位置：[chapter01.tex:27](D:/MS-AgentNet-English/chapters/chapter01.tex:27)。任务：提出指标跨电池稳定性问题。类型：可选语言优化，非语法硬错。

原文：
> For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention.

建议稿：
> Battery materials and operating conditions differ across cells. Further attention is therefore needed to assess whether the selected health indicators can consistently represent battery degradation across these cells.

原因与效果：原句用differences—mean that—stability—representations多层名词组织一个问题。建议先交代差异，再写“指标能否稳定表征退化”；保持中文的信息顺序、退化对象和待关注语气，不拆段。并非字数越少越好。

范文依据：[JES L1778](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1778)至L1796直接讨论HI在不同电池/条件下的表现；EAI L177—181联系化学体系与窗口适用性。不移植其具体特征或结论。

### F3 第四章适配比例：比较动作的主语不匹配

位置：[chapter04.tex:137](D:/MS-AgentNet-English/chapters/chapter04.tex:137)。任务：比较相邻适配比例的收益。类型：语言修复，建议替换。

原文：
> Comparing adjacent adaptation ratios, increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively.

建议稿：
> A comparison of adjacent adaptation ratios shows that increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively.

原因与效果：Comparing的隐含执行者不是主句的increasing the ratio。改为比较结果作主语，明确观察与结果的关系。数字、域、相邻比例和力度均不变；这是更自然，不是更短。

范文依据：[EAI L1469](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:1469)使用“the comparison reveals two key insights”。本文保留show偏好，不借其后文较冗长的研究动机。

### F4 第三章标准卷积：较远的代词指代

位置：[chapter03.tex:57](D:/MS-AgentNet-English/chapters/chapter03.tex:57)，段末。任务：引出标准卷积成本公式。类型：可选明确化；原句成立。

原文：
> Its computational cost can be expressed as:

建议稿：
> The computational cost of standard convolution can be expressed as:

原因与效果：standard convolution之后已经谈到参数、通道和过拟合；直接点明公式对象，免去回找its。不改变公式，不推广到其他同样含its的自然句。

范文依据：[BMS L767](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:767)至L773，在解释卷积后明确点名standard convolutions的成本。

### F5 结论轻量化优势：搭配可更自然

位置：[chapter05.tex:3](D:/MS-AgentNet-English/chapters/chapter05.tex:3)。任务：解释参数和存储结果的意义。类型：可选搭配优化。

原文：
> It also has a low parameter count and storage overhead, showing its lightweight advantages.

建议稿：
> It also has a low parameter count and storage overhead, showing the advantages of its lightweight design.

原因与效果：原句可以理解，但lightweight直接修饰advantages较生硬；明确优势属于轻量化设计，指标和结论不变，不升级为已部署。反查后保留原动词showing，不再建议改为reflecting：二者在此没有必须换用的理由，优化对象仅是后面的搭配，整项仍为可选。

范文依据：[EAI L2807](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:2807)至L2822以lightweight network architecture为对象再写资源指标；JES L3826—3837联系资源需求与compact architecture。这是本文语境适配，不是原句照搬。

### F6 HI输入表题：误差对应估计结果，不是输入本身

位置：[table_4_hi_input.tex:6](D:/MS-AgentNet-English/tables/table_4_hi_input.tex:6)。任务：说明不同输入条件下的误差。类型：搭配修复，建议替换。

原文：
> SOH estimation errors of different health-indicator inputs on the Oxford dataset.

建议稿：
> SOH estimation errors with different health-indicator inputs on the Oxford dataset.

原因与效果：with明确输入是估计条件；of容易将误差归给输入本身。中文冻结版本的表题也已是此英文，属于遗留搭配，不归责新翻译。

范文依据：[JES L2084](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:2084)图题使用“results and error with different HIs”。其全文图题不复制，只借关系介词。

### F7 收敛表头：Late loss不如明确统计区间

位置：[table_4_3.tex:7](D:/MS-AgentNet-English/tables/table_4_3.tex:7)。任务：读者独立读表时识别两个统计层级。类型：可选明确化，非统计口径变更。

原文完整行：
```tex
Dataset & \makecell[c]{10\% threshold epoch\\median [range]} & \makecell[c]{Late loss mean\\median} & \makecell[c]{Late loss SD\\median} \\
```

建议完整行：
```tex
Dataset & \makecell[c]{10\% threshold epoch\\median [range]} & \makecell[c]{Mean loss over\\final 20 epochs\\median} & \makecell[c]{Loss SD over\\final 20 epochs\\median} \\
```

原因与效果：明确loss mean/SD计算于最后20轮，而表中汇总的是其median；不将中位数误改为平均数。第四章L65已提供该区间，因此不新增设定；正式写入时检查新增表头换行后的排版。

范文依据：[EAI L1323](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:1323)直接界定“the final 20 epochs”并讨论loss standard deviation。本文median汇总来自自身表格，不从范文移植。

## G. 第三轮：细读后的可选改善

本轮重新通读当前英文摘要及第1—5章，分组复查并回看三篇对应原文。没有新增明确语法错误；以下3处仅属可选改善，不意味着需要继续扩大改稿范围。累计23项记录，其中22项待选择、1项已解决；页首20项是前两轮小计。A—F的问题不重复计入本轮。三项建议经独立最终只读复核，结论：通过；原意、数据、段落与术语边界保持。

### G1 引言充电时间HI综述：将相关对象从复合修饰语中展开

位置：[chapter01.tex:21](D:/MS-AgentNet-English/chapters/chapter01.tex:21)。任务：介绍通过窗口搜索提取高相关时间特征的已有工作。类型：微调，可选调整。

原文：
> For charging-time feature extraction, Li et al.\cite{ref31} progressively narrowed the voltage window and used the Pearson correlation coefficient (PCC) across multiple cells within a group to evaluate candidate intervals, allowing highly SOH-correlated time features to be extracted from shorter charging segments.

建议稿：
> For charging-time feature extraction, Li et al.\cite{ref31} progressively narrowed the voltage window and used the Pearson correlation coefficient (PCC) across multiple cells within a group to evaluate candidate intervals, allowing time features strongly correlated with SOH to be extracted from shorter charging segments.

原因与改后效果：原句可理解，但highly SOH-correlated将程度、缩写与相关关系都压在time features前。展开为“特征—与SOH高度相关”，搭配更自然；不改变组内多电池、PCC、窗口缩小或较短片段的信息。中文对应“从更短的充电片段中提取与SOH高度相关的时间特征”。

范文依据：[JES L1777](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1777)明确HI与SOH的相关对象，L1784使用strongly correlated HIs；[BMS L447](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:447)—L459按窗口缩小、组内PCC、选定片段推进；[EAI L396](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:396)—L400明确feature sequence与SOH之间的相关性。只学习关系表达，不移植范文区间或协议。建议句为本文适配，不是范文整句。

### G2 第二章HI5对比：明确高相关的另一端

位置：[chapter02.tex:149](D:/MS-AgentNet-English/chapters/chapter02.tex:149)。任务：说明仅看Cell1不能代表Cell2上的HI–SOH相关性。类型：微调，可选调整；与B2修改的是同段不同句。

原文：
> Based on the results for Cell1 alone, HI5 would appear to be strongly correlated, but this result does not reflect its correlation level on Cell2.

建议稿：
> Based on the results for Cell1 alone, HI5 would appear to be strongly correlated with SOH, but this result does not reflect its correlation level on Cell2.

原因与改后效果：前段同时讨论HI–SOH和HI–HI相关性，补with SOH明确此处对象。上下文原本可以推知，因此不是严重歧义。保留would appear的条件判断，不将其改为无条件结论；不改变单电池与跨电池比较。中文的“HI5会表现为强相关指标”在本段指HI与SOH相关。

范文依据：本轮重看[JES L1773](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1773)—L1796及L1822—L1834：先明确between the HI and SOH，再另行讨论inter-feature correlation coefficients。BMS的组内窗口相关性和EAI的feature sequence–SOH相关性也明确评价对象；本文不借用范文的阈值或电池角色。

### G3 第四章收敛结果：拆开两个统计量的长并列句

位置：[chapter04.tex:65](D:/MS-AgentNet-English/chapters/chapter04.tex:65)。任务：报告收敛速度与训练后期损失波动。类型：句内微调，可选调整，仍在原段落中；F7处理表头，本项处理正文。

原文：
> The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

建议稿：
> The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively. The corresponding median standard deviations of late-stage loss are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

原因与改后效果：原句把两种统计量挤在同一句中，后半句还有median late-stage loss standard deviations名词串。分句并使用standard deviations of late-stage loss，使读者依次理解“何时到阈值—后期波动多大”。corresponding承接相同数据集顺序。中位数、标准差、数据集顺序及四个数字全部保留，未将中位数误改为均值。

范文依据：[EAI L1300](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:1300)—L1306定义相对损失阈值，L1317—L1326分别陈述达阈值速度与最后20轮损失标准差，并使用standard deviation of the loss。仅借搭配和两个指标的区分，不照搬其数据、统计协议或机制归因。BMS L1669—L1699和JES L3794—L3845的对应资源结果按具体指标组织比较，但没有本句的双中位数模板，不能声称该统计句直接来自三篇范文。

### 本轮明确保留与复核分歧

- 第四章L172的the closest model：主审曾建议补为the model with the closest storage size；独立复核认为本段一直讨论storage size，补词收益有限、反而更绕。采纳复核意见，保留原句，不列入修改数。
- 第二章charge timing features对应中文“充电时序特征”，不擅自缩窄为charge duration features。
- 第三章ReLU²归一化条件及缩放关系虽然较长，但承载必要条件；不为短句而删技术信息。
- 摘要resource-consuming属于已核实范文表达，不为反复换词另造译名。

## H. 反查结论：不能把三篇范文视为同一种简洁程度

本轮不新增修改编号，重点检查“改后是否真的更直接”，并重新核对第四章首段及三篇实验章节开头。

- 本文第四章首段英文7句，采用“总述—列实验类别—逐项解释用途—总体总结”。冻结中文已有这些信息层，因此较长不完全是翻译造成的。独立只读复核确认：大幅缩短将涉及内容压缩，当前没有该授权。
- [JES results.txt L25—L42](D:/MS-AgentNet-English/style-references/JESSOHRUL/results.txt:25)本身也采用实验分类、逐项解释、Collectively总结的组织。因此，不能将本文这一段笼统判为“不像三篇范文”。
- [BMS results.txt L171](D:/MS-AgentNet-English/style-references/BMSFormer/results.txt:171)从模型、数据集进入训练设置；[EAI results.txt L18—L31](D:/MS-AgentNet-English/style-references/Engineering-AI/results.txt:18)也有协议说明、评价任务和总体意义，并非全部短而直接。三篇信息选择不同，不存在可机械套用的统一句长标准。
- F5反查后撤去showing到reflecting的非必要换词，只保留可选的名词搭配调整。更换报告动词本身不等于改善英语。

处理结论：保留当前正文，不因“范文对齐”擅自压缩原意；明确区分翻译新增的绕法、中文已有的信息重复，以及范文本身的写法。现有建议也须服从最小改动原则，而不是默认全部应用。此判断不表示全文已无语言问题。

## 确认与后续

独立最终复核已确认：B3的归一化后表示与SLFA公式一致；C4的M1比较基线在上下文明确；D1有本文动态电流曲线描述依据。B1已根据交付前检测到的外部更新改为保留，避免覆盖另一任务的修正。其余建议未扩大科学内容或段落结构。本任务只新建并更新本审查报告，未修改正文与排版文件。

本报告仅提供建议。作者可按编号确认后分批写入；写入前重新核对当前文件，避免覆盖另一个任务的回译修正。语言审查不代表科学结论、图内文字和编译已经完成最终验收。
