# BMSFormer 全文阅读与本文方法语言复核

日期：2026-09-14。本报告仅提出建议，不修改论文。主审负责把三篇论文的同功能语境交叉校准后决定正式收录。

## 阅读覆盖与结论

- 本轮重新分段读取 `style-references/BMSFormer/full.txt` 第1–2567行，直到末尾参考文献及EOF；不是复用旧摘录。通读摘要、引言、数据和HI、模型、实验、结论及表注。TXT 的双栏阅读顺序不能直接当段落推进依据。
- 完整读取当前 `chapters/abstract.tex` 和第1–5章，以及 `translation-guides/terminology.md`、`style-references/usage-guide.md`、`house-style.md`、`expression-detail-rules.md`。候选另核冻结中文完整段落。
- 按 PDF 技能渲染并目视检查 BMSFormer 原 PDF 第6、7页完整页面。第6页核实 §3.1 数据流与 §3.2.1 标准卷积段；第7页核实 §3.2.2 模块描述和 §3.3.1 完整代表段。并未目视认证所有16页的每个字符。
- 本文第2、3章大多数方法句已经采用“对象—动作—输出”，本轮没有发现新的明确时态、语态或术语硬错误。保留前轮模型命名句的同一可选方案；另提供1处中文同义重复的可选最小压缩，交主审按其他两篇校准。不是为了凑问题数。

来源：[BMSFormer 原文](../style-references/BMSFormer/source.pdf)；[完整 TXT](../style-references/BMSFormer/full.txt)。

## 1. 完整代表段的可复现逐句分析

选段：BMSFormer PDF p.7，§3.3.1 第一完整段；TXT L883–891。从 `To improve the model’s representational capacity` 起，到 `especially long-range dependencies.` 止，不含后面的公式引导句。PDF 确认5个句号对应5句，`selfattention` 按原PDF换行恢复为 `self-attention`；不把左右栏公式插入本段。

计词：恢复断行后按空白分词；带连字符的词、所有格各计1词；引号和括号不另计；无公式/引文计数歧义。本段80词，5句，均值16词，中位数15词，范围13–21词。计数仅描述本段，不作为本文句长配额。

|句ID及原句起止定位|词数|主语、时态和语态|功能|推进方式|
|---|---:|---|---|---|
|S1 `To improve…` → `independent self-attention mechanism.`|21|multi-head self-attention；一般现在时主动 processes|目的+方法混合|先述目的，再说明并行heads；each补充head含义|
|S2 `Each head calculates…` → `attention representation.`|13|Each head；一般现在时主动 calculates/generates|方法|从多个head转向单个head的两项操作|
|S3 `The self-attention mechanism computes…` → `all other elements.`|18|The self-attention mechanism；一般现在时主动 computes|方法|说明权重所对应的关系范围|
|S4 `It then produces…` → `new representations.`|13|It指上句机制；一般现在时主动 produces|方法|then明确运算下一步，these relationships承接上句|
|S5 `This allows…` → `long-range dependencies.`|15|This指前述机制；一般现在时主动 allows|机制解释/作用|从运算转向注意重要信息与长程依赖的作用|

功能分母明确为上述5句/80词：纯方法3句（60%），44词（55%）；目的+方法混合1句（20%），21词（26.25%），不强行拆成互斥的目的/方法词数；机制解释1句（20%），15词（18.75%）。实验结果0句/0词：S5不是实验结果，不能为凑方法/结果比例把机制解释算成结果。方法相关句包含混合句共4句，但不与纯方法百分比相加。

可学之处是稳定对象、具体动词、按步骤推进；不是要求所有句子都主动、都短于21词。该段对基础注意力的解释比本文当前 §3.3.1 还细，因此不能要求本文再加同样的教材式说明。

## 2. 可适配句式：不是原文整句复制

|功能|本轮定位的原文短片段|适配结构（模板，不是引文）|本文采用边界|
|---|---|---|---|
|输入数据流|§3.1 p.6，L735–744：`HIs are taken as input`、`then fed into`|`[Input] is [operation], [operation], and then fed into [module].`|本文架构首段已有这类自然被动链，保留；不能套入范文MLP或转置路径|
|模块具体操作|§3.3.1 p.7，L883–891：`Each head calculates`|`[Module/head] calculates [quantity] and generates [output].`|用于操作主体明确的句子；RAA具体归一化仍按本文实现|
|卷积层与功能|§3.2.2 p.7，L874–880：`This module further incorporates`|`[Module] uses [layers] to [function].`|可借主干，不照抄其1×3核；本文为1×5|
|操作先后|§3.2.1 p.7，式(8)前完整引导句：`depthwise filtering followed by pointwise combination`|`[Operation A] is followed by [operation B].`|只适用于串行操作，不把本文两并行分支改成先后关系|
|资源代价|§3.2.1 p.6，L767–773：`computational resources and training time`|`As [configuration] increases, [resource cost] increases.`|保留具体条件、量和力度；不从参数量推出推理延迟|

注意：范文也有较长引导、重复副词与不规范语法，例如 p.6 的 `Convolutions operations`、p.7 的 `aiming to addresses`。不继承这些错误；也不以范文有长句为由禁用本文所有简化。

## 3. 可选最小修复：同一计算代价重复叙述

位置：`chapters/chapter03.tex:57`，标准卷积的完整段落。分类：**可选，词汇不难但重复表达计算代价；不是术语错译或时态错误。**

中文完整段：

> 卷积运算通过滑动卷积核提取时间序列中的局部信息。标准卷积在所有输入通道上进行运算，每个卷积核生成一个输出特征图，对应一个输出通道。随着输入通道数、输出通道数和卷积核尺寸增加，其参数量与计算开销迅速累积，显著推高计算负载并延长训练时间。在小样本电池数据集上，较大的参数量还可能增加模型的过拟合风险。其计算成本可表示为：

以上仅为显示省略引用命令，正文引用不得删。

现有英文（目标整句）：

> As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time.

建议英文：

> As the numbers of input and output channels and the kernel size increase, the parameter count and computational load grow rapidly, substantially increasing training time.

改动原因：保留输入通道数、输出通道数、核尺寸、参数量、计算负载和训练时间，以及迅速/显著增加的力度。只把同一句中的“计算开销迅速累积→推高计算负载”合并成一次计算负载增加，不再用近义抽象名词重复中间一步。没有将训练时间偷换成推理时间，也没有删后句的小样本条件或过拟合可能性。现在时、主动语态不变；`computational load` 原句已有，不引入新术语。

对应中文措辞效果（只为说明删冗余，不修改冻结中文）：

> 随着输入通道数、输出通道数和卷积核尺寸增加，其参数量与计算负载迅速增加，显著延长训练时间。

范文是否也这样：BMSFormer p.6 §3.2.1 同样把计算资源和训练时间放在一句中，未把二者分成多句；因此不要求本文多拆句。其本段未把 computational overhead 与 computational load 串联重复一次。范文条件是大型时序数据，本文条件是通道数/核尺寸增加，**不是相同实验条件**；只借组织资源代价的句法，不把它作为本文计算关系的证据。范文其他位置仍有 further 等重复修饰，故该候选仅是作者本轮偏好的可选压缩，待主审比对另外两篇，不升级为必须修改。

## 4. 前轮模型命名方案继续有效，不循环换词

位置：`chapters/chapter03.tex:1`。已重新读冻结中文开篇完整段，含模型命名、组成、提取对象及后续章节引导。

中文目标：其命名中的“MS”源于由小核DSConv-S与大核DSConv-L构成的多尺度卷积设计，用于高效提取不同时间尺度的退化特征。

现有英文：

> The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales.

继续保留前轮建议，不另生竞争版本：

> MS refers to the multi-scale convolutional design: small-kernel DSConv-S and large-kernel DSConv-L efficiently extract degradation features over different time scales.

说明：去掉“命名中的”表层引导和组成关系的修饰链，直接呈现两个模块做什么；组成、MS含义、高效与不同时间尺度全保留。BMS p.6 §3.1也用包含关系和从句，原句不构成规范错误；p.7 §3.2.2直接以DSConv模块为主语描述核与作用，可借其主干。仍为可选，不按新增问题累计。

## 5. 一致性保留判断

- 第2章历史老化过程 `were charged/were conducted` 与数据内容 `contains`、本稿采用 `are included` 功能不同，不是同一动作时态漂移。
- 第3章模块操作现在时与文献研究过去时各有职能；当前方法主体/处理对象变化导致主动与被动交替自然。BMS p.6架构段采用被动，p.7注意力段采用主动，也不是要求全篇统一语态。
- 第3章 `LN` 与 `LN_0` 都是layer normalization，后者无缩放/偏置参数有明示；不改成同一个符号。RAA中的row normalization也不能改成layer normalization。
- DSConv-S/L、SLFA、RAA、MS-AgentNet 专名保持本文，不能模仿范文而套成LGFA。ReLU²与ReLU作用位置不同，不混同。
- 术语全文允许语法需要的单复数和定义后的缩写；`charge timing features` 一般类别与固定CCCT术语不能机械视为两个同义译名。
- 第2章HI提取、MS-CCCT标定、HI筛选与总体算法名的层级清楚；为减少重复省掉完整算法中的extraction或optimization会改变已确认名称，不建议。
- 本报告没有重判旧技术疑点，没有重新认证原始实验记录或栅格图全部标签。只读论文、图表源文件；无正文修改，无需编译。
