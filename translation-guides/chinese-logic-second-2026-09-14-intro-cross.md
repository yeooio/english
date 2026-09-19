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
