# 全文文字语法、术语与直接性审查

日期：2026-09-14。按作者最新要求，**本报告只讨论文字，暂不处理图内英文和图文技术疑点**。主审与两名agent通读当前英文，分工复查三篇范文。以下是建议，论文未修改。

## 结论与处理次序

本轮未确认正文存在需要全篇纠正的时态、语态或主谓一致问题。值得优先优化的是重复解释、抽象名词链和较远的代词回指。下面保留7处完整替换建议，均属于语言直接性优化，不把它们包装成7个确定的语法错误。

其中第3、5项与历史可选建议重合，经本轮原文复核后保留；其他项也不以“首次发现”为价值标准。没有采用补充更多统计细节、改写技术解释或删减实验事实的建议。

## 1. 摘要：直接写大核卷积做什么

位置：[abstract.tex](D:/MS-AgentNet-English/chapters/abstract.tex:1)。

**现有英文**

> Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity.

**建议英文**

> Additionally, large-kernel depthwise separable convolutions extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity.

**中文原因**：删去`are used to`，让`extract`与`work`成为清楚的并列谓语。长时间尺度、大小核协同、多尺度/多通道、低参数开销和特征多样性均保留。原句被动结构本身合法，不是要求所有被动句改主动。

**范文依据与尺度**：三篇完整摘要本轮已重读并核PDF p.1。BMSFormer摘要第4句用模型主语直接接`integrates`，第5句也使用`are embedded to`；Engineering-AI第2、4句直接以过程/模型陈述功能；JESSOHRUL第5句主动、第6句被动。三篇都允许两种语态；本项仅在本文已有并列动作时使主干更直接，属于**可选**，不是范文强制要求。

## 2. 引言：明确是谁具有表征能力

位置：[chapter01.tex](D:/MS-AgentNet-English/chapters/chapter01.tex:13)。

**现有英文**

> With the rapid development of deep learning, researchers have increasingly used multilayer neural networks to capture complex battery degradation patterns through their strong nonlinear representational capability and thereby improve estimation accuracy\cite{ref14}.

**建议英文**

> With the rapid development of deep learning, researchers have increasingly used multilayer neural networks with strong nonlinear representational capability to capture complex battery degradation patterns and thereby improve estimation accuracy\cite{ref14}.

**中文原因**：把能力紧贴`neural networks`，不再让读者回找`their`的先行词；保留现在完成时、研究趋势、网络能力和提高精度的目的。这是指代和修饰位置优化；技术语境原本已能判断能力属于网络，不能称原文必然把能力归给研究者。

**范文依据与尺度**：Engineering-AI引言p.2“深度学习—CNN/RNN—Transformer”完整段；BMSFormer引言p.2数据驱动及CNN/RNN段；JESSOHRUL引言p.2以CNN、RNN、Transformer为主语的能力说明。三篇也使用可恢复的代词和`capability/ability`类名词，不支持禁止`their`。本文同句有两个复数名词，贴近修饰对象是**可选**的局部改善；不据此替换已确认术语`representational capability`。

## 3. 引言：把名词链改成“指标能否稳定表征退化”

位置：[chapter01.tex](D:/MS-AgentNet-English/chapters/chapter01.tex:27)。

**现有英文**

> For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention.

**建议英文**

> Given differences in battery materials and operating conditions, further attention is needed to how consistently the selected HIs represent degradation across cells.

**中文原因**：**词汇简单但表达绕**。`differences → mean that → stability of representations → requires attention`层层推进；改为“需要关注所选HI能否稳定表征退化”。`selected`对应冻结中文的“所选指标”，不新增实验条件；保留“仍需关注”的力度，不改成已经证实不稳定。

**范文依据与尺度**：JESSOHRUL §3.5.2，PDF pp.13–14，完整跨电池HI比较与筛选语境直接讨论指标能否表征群体退化；其引言p.3也有较长抽象表述。BMSFormer引言p.2“Estimation Accuracy Challenges / Performance Stability Issues”本身使用抽象名词；Engineering-AI引言及§2.2.1也讨论特征稳定性、噪声与预处理。三篇不是都采用短主干，更不能证明抽象名词错误；本项以**相同信息下减少嵌套**为理由，定为可选并建议优先。

## 4. DTC定义：直接说明相对哪个量的变化率

位置：[chapter02.tex](D:/MS-AgentNet-English/chapters/chapter02.tex:76)。前一句关于DTV电压域与DTC充电容量域的区别保持原样。

**现有英文**

> With charge capacity as the independent variable, DTC describes how the rate of temperature change evolves with capacity and is defined as follows\cite{ref64}:

**建议英文**

> DTC describes the rate of temperature change with respect to charge capacity and is defined as follows\cite{ref64}:

**中文原因**：**词汇简单但表达绕**。用`with respect to charge capacity`直接表达自变量和微分关系，减少两次交代capacity。与紧接的dT/dQ定义一致，不删公式、平滑参数或前句领域区别。

**范文依据与尺度**：JESSOHRUL §3.5.1 PDF p.13 DTC定义段，`methodology.txt`1254–1269及1313–1316行，在完整定义和后续平滑语境中采用相同“温度相对容量变化率”的直接结构。BMSFormer §2.3是充电时间HI，Engineering-AI §3.3是积分HI，均不是同一微分对象，不能拿它们的简短定义要求本文删信息。本文原句配合公式可理解，本项为**可选**直接化。

## 5. 模型命名：减少组成与作用的修饰链

位置：[chapter03.tex](D:/MS-AgentNet-English/chapters/chapter03.tex:1)。

**现有英文**

> The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales.

**建议英文**

> MS refers to the multi-scale convolutional design: small-kernel DSConv-S and large-kernel DSConv-L efficiently extract degradation features over different time scales.

**中文原因**：**词汇简单但表达绕**。冒号后直接说明两个模块的作用，保留MS含义、大小核组成、高效提取和不同时间尺度。`extracts`变为`extract`是建议句主语变成两个模块后的正常调整；原句`which`回指单数`design`时，`extracts`原本正确。

**范文依据与尺度**：Engineering-AI摘要p.1将模型名称、大小核组成和设计作用连接，§4.2 PDF p.7直接说明尺度与提取功能；BMSFormer §3.2 pp.6–7和JESSOHRUL §2.2.2均使用包含关系和关系从句说明模块。三篇也有修饰链，因此只作**可选**局部简化，不能判原句主谓错误。主审保留历史较直接的冒号方案，不新增另一套同义改写。

## 6. 卷积段：合并“计算开销/计算负担”的重复

位置：[chapter03.tex](D:/MS-AgentNet-English/chapters/chapter03.tex:57)。

**现有英文**

> As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time.

**建议英文**

> As the numbers of input and output channels and the kernel size increase, the parameter count and computational load grow rapidly, substantially increasing training time.

**中文原因**：同一句中`computational overhead grow`与`increasing the computational load`重复说明计算负担增加。合并同义信息，保留通道数、核大小、参数量、计算负担以及训练时间的变化；参数量没有与训练时间合并为同一概念。

**范文依据与尺度**：BMSFormer §3.2.1 PDF p.6，`methodology.txt`544–566行，标准卷积段直接联系计算资源和训练时间；Engineering-AI §4.2 p.7，646–649行，直接从参数冗余进入模块设计；JESSOHRUL §2.2 p.7及§2.2.2也有计算成本解释，且存在重复说明。范文也重复不等于本文必须保留重复，但不足以把此句判为语法错误；定为**可选去冗余，建议优先**。

## 7. 初始化句：避免同一句说两次“初始状态不同”

位置：[chapter04.tex](D:/MS-AgentNet-English/chapters/chapter04.tex:61)。

**现有英文**

> This initialization gives different agents small, nonidentical initial parameters, avoiding identical initial states.

**建议英文**

> This initialization gives different agents small, nonidentical initial parameters.

**中文原因**：`nonidentical initial parameters`已表达参数初态不同，末尾没有新增另一种状态变量或操作。仅删除同一句的重复解释，保留不同智能体、小幅值和非一致性。

**范文依据与尺度**：Engineering-AI §5.2.1，`results.txt`108–169行完整初始化讨论，也解释初始化分布的作用；其单智能体条件不同，不搬入本文。BMSFormer实验设置`results.txt`171–198行和JESSOHRUL §4.4.2 PDF p.24直接说明设置与用途，但不是与本文相同的双智能体初始化。不能说三篇完全没有重复；本项根据本文同句含义重叠，定为**可选去冗余，建议优先**。

## 术语、时态和语态：哪些保持，哪些只作轻量统一

| 项目 | 本轮判断 |
|---|---|
| SOH、HIs、MS-AgentNet、SLFA、RAA、DSConv-S/L | 连续正文名称总体一致。保留正式名称与定义，不用范文自己的模块名替换。 |
| 总算法与内部步骤 | `multi-source health indicator extraction and optimization algorithm`是整体；extraction与selection是内部步骤，不强行缩成同一名称。 |
| long-range / long-term dependencies | 注意力贡献句用long-term，摘要用long-range，语境接近，可选统一同一机制用语。但冻结中文贡献句是“长期依赖”，本轮不将其确认为错译；LSTM长期记忆语境不批量换词。 |
| source domains / source-domain training cells | 第4章132行具体电池可写后者以对应119行角色定义。前文已足以消歧，属于可选明确化，不当成技术错误。 |
| state of health / state-of-health estimation | 普通名词与前置修饰语的语法形式不同，保留。 |
| DTV与被引文献的differential thermal voltammetry | 本文指标名称与引文对象按各自语境保留，不机械统一不同来源名称。 |
| cross-cell generalization / cross-dataset transfer / few-shot adaptation | 分别对应不同评价任务，不能当同义词轮换。 |
| parameter count / FLOPs / training time / weight storage size | 对象不同，保留；不把weight storage换成运行时memory。 |
| modeling / generalization / behavior / normalization | 连续正文采用美式拼写；本轮未检出相应英式变体混入。引用题名不是正文改拼写的对象。 |
| cutoff / Cut-off | 正文与表头可统一为cutoff，属于拼写格式偏好；三篇也存在连字符差别，不定为语法错。 |
| 摘要We compared与results show | 保留。前者报告已完成实验，后者说明当前结果；JESSOHRUL摘要有同样分工。 |
| 数据集were charged与contains / are included | 保留。历史操作、现有数据性质和本文使用范围的时间功能不同。 |
| 第4章is used / is trained / are measured | 协议作为程序说明时一般现在时被动自然；BMSFormer、JESSOHRUL也这样写，不全改过去时。 |
| 结论proposes / show与未来will focus / will cover | 保留，贡献、结果与未来计划分工清楚。 |

范文逐项完整语境与同条件判断见两份独立记录，以上不是凭词表匹配就判定一致。

## 一个低优先级标点规范项

第3章有多处“公式以句号结束，下一段接小写where释义”。建议在最后统一校稿时将接续释义的公式末句号改为逗号，保留小写where。第66、159、170、185、205、223、263、286、311、329、347、361、382行对应同一类情况，不计为13个独立错误。三篇原PDF有公式后不加标点或逗号接where的写法；本项只理顺明确句号与从句的衔接，不改数学内容。详见方法agent记录O9。

## 校准后没有优先采用的改法

- 不把`Compared with [models], its average MAE ...`升级为硬性比较对象错误：BMSFormer和JESSOHRUL同类结果段也省略“对应指标值”，本文上下文清楚。补`the corresponding values for`会增加字数，本轮不优先。
- 不删除第4章开头、结论或其他段落的整句总结来追求短：其中包含评价范围和有效性/适用性等信息，不能把所有概括句都当冗余。
- 不禁用which、with、however、被动语态或长句；只在具体句子的指代、主干或重复确有改善时调整。
- 不把范文中较强的自我评价、未验证的部署结论和个别语法错误套到本文。

## 阅读与交付记录

- 主审通读当前摘要、第1—5章；两名agent各通读全文并交叉检查正文术语、表题、表头、表注及可编辑图题。用户最新排除的图内事项不进入本报告建议。
- 本轮重新读取三篇摘要、引言、方法、结果和结论的原文语境；双栏关系不确定时回查PDF。逐文件实际阅读范围及回查页码保留在分报告中，不以旧词库代替本轮阅读。
- 三篇完整摘要的21个句子已重新按功能、主语、时态、语态、句长和衔接测量；另有方法段抽样。统计只描述选定语境，不是全文字数统计或本文的句长配额。
- 主审对建议涉及的中文原意作定点复核；中文源稿未改，英文正文、表格、公式与图像均未改。本轮不涉及正文变更，因此没有运行论文编译。

配套记录：

- [三篇范文句式提炼与本文映射](D:/MS-AgentNet-English/translation-guides/grammar-reference-patterns-2026-09-14.md)
- [语法、时态与语态独立复核](D:/MS-AgentNet-English/translation-guides/grammar-tense-review-2026-09-14-agent.md)
- [方法语法与全文术语独立复核](D:/MS-AgentNet-English/translation-guides/grammar-terms-review-2026-09-14-agent.md)
