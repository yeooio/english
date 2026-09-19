# 全文术语与第2/3章语法审查（独立 agent，2026-09-14）

本记录仅提供建议，未修改论文、图片或术语表。历史审查记录未用作本轮判定依据。

## 实际阅读范围及尺度

- 通读了 `main.tex`、`chapters/abstract.tex`、第1—5章、全部 `tables/*.tex` 和 `figures/*.tex`；第2/3章为语法、指代、时态语态重点，其余章节检查全篇术语与专名一致性。
- 重新完整读取三篇 `methodology.txt`（BMSFormer：PDF第3—8页；Engineering-AI：第3—11页；JESSOHRUL：第4—15页，文件均带相邻章节）。JESSOHRUL工具输出中段被截断后已补读，不把未显示的内容当作已读。
- 为辨认双栏顺序，视觉回查 BMSFormer PDF第6、7页，Engineering-AI第7页，JESSOHRUL第13、14页。以下证据提供论文、节、页和段落边界，不声称完成三篇全文逐句语法审查。
- 视觉检查本文四张结构图：`fig1.png`、`01.png`、`02.png`、`fig3_3_attention_comparison.png`。其他栅格结果图的细小文字未逐幅穷尽，本报告不宣称所有图片内部已完整校对。
- 已读 `usage-guide.md`、`terminology.md`、`scientific-boundaries.md`。必要项以明确拼写/语法错误或同一模块异名为主；合理时态变化和可理解的省略不算错误。

## 结论

第2/3章的连续英文整体语法稳定，没有发现需要统一改成过去时或统一主动语态的系统性错误。按用户最新要求，本轮仅报告连续正文的语言问题。未确认第2/3章存在需要强制修改的时态、语态或主谓一致错误；有少量可选术语统一、指代明确化和重复表达压缩。此前发现的图内问题仅存附记，不属本轮候选。范文本身也存在名词修饰、主谓一致和重复表达问题，不能原样套用。

## 一、连续正文的可选修改，不列为硬错误

### O9 公式后where的标点衔接：合并为一个低优先级规范项

- **现有英文形式：** 公式以句号结束，下一段以小写`where ...`给出同句中的符号解释。例如`C_{Conv}=...D_F.`后接`where k, ... denote ...`。
- **建议形式：** 若where继续解释当前公式，将公式最终句号改为逗号，保留小写`where`。不要只把它改成`Where`而仍留下关系从句式的独立段。
- **位置：** 第3章where位于66、159、170、185、205、223、263、286、311、329、347、361、382行。此为同一种标点处理，不能计为13个独立语法问题。223行之前分式后虽有逗号，最终`p=1,2,...,N.`仍有句号；311行之前句号在cases最后一行的`=0.`后。
- **尺度：** 已直接查看BMSFormer PDF第6—7页公式(6)、(7)、(9)、(10)与where，常在公式末不加标点；Engineering-AI PDF第7页公式(7)与where也未以句号断开；JESSOHRUL PDF第13页公式(52)、(53)用逗号后接where。因此范文允许省略数学标点，不能宣称它们全部严格遵循同一排版规范。本项只建议把本文明确句号与后续释义的衔接理顺，不改变公式或要求新增释义，不把TXT空行本身视为句子断开。按用户“不用过度细节”要求，适合统一校稿时一次处理，不作为主要发现。

### O6 方法目的句中的its：可明确，原文不判错

- **位置：** `chapters/chapter02.tex:106`。
- **现有英文：** `To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT).`
- **建议英文：** `To improve the strength and cross-cell stability of the correlation between CCCT and SOH within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT).`
- **中文原因：** 原句`its`可以正常回指`correlation`，也与冻结中文“相关性及其…稳定性”一致，并非悬空指代或必须修改的语法错误。建议只把“相关强度”和“相关关系的跨电池稳定性”并列，减轻读者寻找指代的负担。不能改成声称任何工况下通用稳定。
- **三篇尺度：** BMSFormer §2.3从窗口搜索到PCC解释，直接指定最小相关值和下一搜索区间；Engineering-AI §3.3.2从异质退化到离线标定步骤，重复交代calibration对象；JESSOHRUL §3.5.2、PDF第13—14页从单电池相关差异到跨电池HI筛选的完整论述同样使用`its`、`this`和重复对象。三篇都允许可恢复的代词回指，本文并未超出其通常阅读难度，故只列可选。相关对象上以JES最接近，三篇的具体评分公式与本文不同。

### O7 SOH定义句目的引导：可缩短，非悬垂修饰语错误

- **位置：** `chapters/chapter02.tex:3`。
- **现有英文：** `To use a consistent definition in the following experiments, SOH is calculated as capacity retention, namely the ratio of the current available capacity to the rated capacity`。
- **建议英文：** `For consistency across the following experiments, SOH is calculated as capacity retention, namely the ratio of the current available capacity to the rated capacity`。
- **中文原因：** 保留统一实验定义、容量保持率以及全部分子分母信息，只把目的引导缩成介词短语。科研被动句的目的状语可以表达隐含执行者的目的，不应仅因主语为SOH就把原句判为悬垂错误。
- **三篇尺度：** BMSFormer §2.1 SOH定义段从“The SOH is a critical metric...”到where行；Engineering-AI §3.1从“SOH is a key indicator...”到公式及后文capacity fade说明；JESSOHRUL §3.3.1从“SOH is a metric...”到随循环下降的说明，都含目的/定义背景和被动表达。本文信息颗粒度没有比范文更冗长；保留定义引导，只做可选直接化。

### O8 which从句与单数design一致：保留为默认

- **位置：** `chapters/chapter03.tex:1`第二句。
- **现有英文：** `The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales.`
- **建议英文（可选）：** `The name MS refers to the multi-scale convolutional design, which combines small-kernel DSConv-S and large-kernel DSConv-L to efficiently extract degradation features over different time scales.`
- **中文原因：** `which`可以指单数`design`，所以`extracts`单数正确。原句不是主谓不一致。若要进一步明确设计与两个模块的关系，可将`comprising`改为`which combines`，保留MS命名含义、两种核尺度、高效性和多时间尺度信息。此处不建议为了“简单句”拆段或删除限定。
- **三篇尺度：** BMSFormer §3.1第6页整体架构段使用`block, which includes...`；Engineering-AI §4.1跨第6—7页的命名解释把Small-kernel/Large-kernel作为design philosophy组成部分；JESSOHRUL §2.1.2第6页整体架构段使用模块列举后的`which function...`。三篇均允许列举+关系从句结构，本文无需因出现which就改。名词design和modules的单复数条件不同，不能从范文复数动词机械套用。

### O1 同一注意力作用的依赖术语

- **现有英文：** 第1章贡献(2)，`to fuse local degradation features and long-term dependencies with low parameter overhead`。
- **建议英文：** `to fuse local degradation features and long-range dependencies with low parameter overhead`。
- **中文原因：** 这里与摘要的`long-range degradation dependencies`和第3章的跨位置交互指同一类依赖，统一到术语表`long-range dependencies`更稳妥。原表达可理解，不是语法错误。第1章介绍LSTM的`long-term dependencies`则是长期记忆语境，可保留，不应机械全文替换。
- **三篇尺度：** BMSFormer §3.3.1，第7页从“To improve…”到“…long-range dependencies.”的完整段；Engineering-AI §4.1，第7页Step 1从“The input…”到“gradient flow”用长程依赖说明全局聚合；JESSOHRUL §2.1.1—2.1.2用长程依赖说明注意力跨序列建模。该贡献句与这些语境同功能；与RNN记忆语境不完全同条件。因此仅建议统一同一注意力功能，不把long-term一律判错。

### O2 简单词但表达重复：计算开销又被解释成计算负担

- **位置：** `chapters/chapter03.tex:57`。
- **现有英文：** `As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time.`
- **建议英文：** `As the numbers of input and output channels and the kernel size increase, the parameter count and computational load grow rapidly, substantially increasing training time.`
- **中文原因：** `computational overhead grow`与紧接的`increasing the computational load`重复。只合并同一信息，保留通道数、核大小、参数量、计算量和训练时间，不重排段落。
- **三篇尺度：** BMSFormer §3.2.1，第6页从“Convolutions operations…”到标准卷积公式前，同时提计算资源和训练时间；Engineering-AI §4.2，第7页三句直接介绍参数冗余、过拟合和DSConv设计；JESSOHRUL §2.2、第7页从“Convolutional operations…”到方法介绍也同时提cost和memory，§2.2.2首句甚至重复两次“两步分解”。这些说明范文也有重复，不能因范文某句更短便要求本文必须改。本句修改仅是可选的同义重复消除，不删除独立事实。

### O3 DTC定义句可更直接

- **位置：** `chapters/chapter02.tex:76`。
- **现有英文：** `With charge capacity as the independent variable, DTC describes how the rate of temperature change evolves with capacity and is defined as follows`。
- **建议英文：** `DTC describes the rate of temperature change with respect to charge capacity and is defined as follows`。
- **中文原因：** 【词汇简单但表达绕】把“以容量为自变量”与“随容量变化”合为准确的`with respect to charge capacity`。原句有上下文和公式可消歧，不升级为导数定义错误。
- **三篇尺度：** JESSOHRUL §3.5.1，PDF第13页右栏从“To leverage these characteristics…”到DTC公式与平滑说明，直接使用`rate of temperature change with respect to capacity`，属于相同DTC定义。BMSFormer §2.3只讨论时间型HI和PCC；Engineering-AI §3.3讨论电压积分面积，两者不是同一计算对象，因此不拿它们短而直接的定义强迫本文改变技术信息。本文不照搬JES的峰指标编号及CVT含义。

### O4 美式拼写/图表格式可统一，但不是硬错

- **现有英文：** 第2章MIT段`cutoff voltage`；表`table_2_1.tex:23,25`的`Cut-off voltage / Cut-off current`。
- **建议英文：** 表中统一为`Cutoff voltage / Cutoff current`。
- **原因与尺度：** 是同一修饰词的拼写格式统一，不是专业概念冲突。BMSFormer第4页表1和JESSOHRUL第11页表3也用`Cut-off`；JES §3.4 NASA叙述则用`cutoff voltages`。因此范文自身也有这种差别，不把连字符变体列为语法错误；选择`cutoff`是遵循本文已经采用的美式形式。Engineering-AI方法段没有可比的cutoff逐项说明，不能补称三篇一致。

## 四、明确保留及防止误改

| 检查项 | 当前英文及决定 | 范文尺度及理由 |
| --- | --- | --- |
| 数据集介绍时态 | `is provided / contains`与`were conducted / were charged`并存：保留。MIT的`was jointly released`是一次历史发布：保留。 | BMSFormer §2.2叙述现存数据性质时多用现在时；JES §3.4 Oxford历史测试用过去时，CALCE描述有现在时。EAI §3.2也是过去时评价动作与现在时数据性质并存。本文是按时间功能变化，不是无原因跳时态。 |
| 方法描述主动/被动交替 | `MS-CCCT uses...`、`features are extracted...`、`The local branch applies...`：保留。 | 三篇方法均交替用“模块做什么”和“数据经何操作”；主语焦点不同，语态不必统一。 |
| SOH / HI / CCCT / PCC / SCC | 正文存在全称和正常缩写，核心概念未见需要重新翻译之处。 | CCCT/PCC在第1章定义；SCC在Challenges定义。BMS与JES也在后续方法中复述全称/缩写。不把正常复述算术语漂移。 |
| DTV命名 | 本文指标`differential temperature--voltage`与第1章被引文献`differential thermal voltammetry`：保留区别。 | JES §3.5.1/Table4对应本文DTV曲线；第1章是引文对象，不应强迫改为本文命名。 |
| SOH形式 | 普通名词`state of health`与修饰`state-of-health estimation`：保留。 | 连字符由语法位置决定，不是两种术语。 |
| 小核/大核/长程 | `local features`、`long-range dependencies`、`features over longer time scales`：保留概念区别。 | 三篇区分卷积局部/尺度特征与注意力长程关联。不能都改成`long-term degradation trends`。 |
| extraction / selection / optimization | 总算法全名和内部步骤名称：保留。 | 三篇也区分提取与筛选；本文总算法名称有作者确认，不为压缩改成HI selection algorithm。 |
| source-only evaluation / few-shot adaptation | 明确不同协议：保留。 | 三篇方法没有与本文完全同条件的跨数据集少样本协议，不能借范文泛称generalization统一掉。 |
| BMS、MS-AgentNet、SLFA、RAA、FFN、DSConv | 连续正文和表题整体一致；ReLU²大小写/LaTeX写法正常。 | 范文各有正式模块名，本文章节大小写与普通叙述差别不等于改名。 |
| 英美拼写 | 连续英文中的`modeling/generalization/behavior/normalization`符合美式；未发现对应英式拼写混用。 | 不为追求“美式”修改标准技术词、数据集品牌名。 |
| 方法省略颗粒度 | 不要求每次再定义参数、每句重复“同一数据集”，不把第3章通用卷积表达中的未采用极端参数自动判错。 | BMS §3.2先讲通用卷积再给模块；EAI也在宏观叙述中省略固定条件；JES公式后按必要程度说明。本文已有上下文时不提高到明显超出范文的标准。 |

文本搜索未检出`pancrea`或“胰腺癌”相关字样；本论文全文主题是锂离子电池SOH，未发现混入该医学主题的英文。

## 五、本轮提炼的句式及逐句尺度记录

只借“主语—操作—对象”的组织方式，不照抄论证、材料编号和技术机制。下列抽样都来自本批已回看PDF的完整段落。计词规则：按空白分隔token，连字符词算一个，数学符号按空白token计，去掉引文编号，不计节标题与公式独立行；不据此规定本文句长。方法占比中含设计目的的混合句单列，不重叠相加。

### BMSFormer，PDF第7页§3.3.1第一段

边界：从“To improve the model’s representational capacity...”到“...especially long-range dependencies.”，5句，80词；全部现在时主动。

| 句ID | 词数 | 功能 | 主语/主句 | 衔接 |
| --- | --- | --- | --- | --- |
| B1 | 21 | 方法+设计目的 | multi-head self-attention / processes | 目的开头，引出多头 |
| B2 | 13 | 方法 | Each head / calculates and generates | 每个head承接多头 |
| B3 | 18 | 方法 | The self-attention mechanism / computes | 解释内部计算 |
| B4 | 13 | 方法 | It / produces | then连接下一操作 |
| B5 | 15 | 解释/作用 | This / allows | 指代前述操作的功能 |

纯方法3/5句、44/80词；方法+目的1/5句、21/80词；解释1/5句、15/80词；实验结果0。范围13—21词，中位15词。可借模式：`The [module] [verb] [object]. The [output] then [verb]...`。本文§3.2的`The expanded features pass through...`和`Next, the second... fuses...`已符合，可保留。

### Engineering-AI，PDF第7页§4.2完整首段

边界：从“Standard convolutions often suffer...”到“...as visualized in Fig. 5.”，3句，51词。

| 句ID | 词数 | 功能 | 主语/时态语态 | 衔接 |
| --- | --- | --- | --- | --- |
| E1 | 17 | 背景/问题 | Standard convolutions；现在时主动+情态 | 点出冗余和过拟合 |
| E2 | 12 | 方法 | two specialized ... modules；现在时被动 | To mitigate this回指问题 |
| E3 | 22 | 方法+目的 | The kernel scales；过去时被动 | 给出已选择尺度及目的 |

纯方法1/3句、12/51词；混合方法+目的1/3句、22/51词；问题1/3句、17/51词；实验结果0。范围12—22词，中位17词。该段本身现在时与过去时并存，因为“模块被设计为”和“尺度当时被确定”不同。模式：`To [address the named problem], [module] is designed.`；本文可用，但已有自然句不必重复套同一模板。

### JESSOHRUL，PDF第13页§3.5.2首段

边界：从“The extraction of HIs is a crucial step...”到“The formulas for PCC and SCC are given as follows:”；4句，85词。原文第一句`the precise`是不规范名词用法，不用于本文模板。

| 句ID | 词数 | 功能 | 主语/时态语态 | 衔接 |
| --- | --- | --- | --- | --- |
| J1 | 31 | 背景/理由 | The extraction of HIs；现在时系表 | 提出提取质量的重要性 |
| J2 | 23 | 方法+目的 | PCC and SCC；现在时被动 | 指定两种分析量 |
| J3 | 21 | 定义/解释 | PCC / measures；SCC / assesses；现在时主动 | while并列区别量的作用 |
| J4 | 10 | 公式过渡 | The formulas；现在时被动 | 引出数学定义 |

方法+目的1/4句、23/85词；背景1/4句、31/85词；定义解释1/4句、21/85词；公式过渡1/4句、10/85词；实验结果0。范围10—31词，中位22词。可借模式：`[Metric A] measures..., while [metric B] assesses...`；本文已用明确对象区分PCC线性与SCC单调关系，不必为了像范文再扩大成所有非线性依赖。

以上检查不产生正文修改授权。若合并到主审查报告，图文技术待核项应与纯语言修复分开，不能用它们凑“语法错误”数量。


## 附记：用户缩小范围前的图像检查（本轮不处理、不计问题数量）

## 一、建议修复的明确问题

### N1 图内拼写与正式模块名错误

| 位置 | 现有英文 | 建议英文 | 简短中文原因 |
| --- | --- | --- | --- |
| `figures/fig1.png`，橙色第4步标题 | MS-CCCT & PCC/SCC sereening | MS-CCCT & PCC/SCC screening | `sereening` 是拼写错误。 |
| `figures/fig3_3_attention_comparison.png`，(d)下方标题 | Skim Local-Global Fusion Attention | Slim Local-Global Fusion Attention | 本文第1章贡献、第3章定义均为 `Slim`；`Skim` 是另一个词。 |
| `figures/01.png`，紫色模块和(c)标题；`figures/fig1.png` 内嵌同一结构图 | L-DSConv | DSConv-L | 对应同一大核模块；正文、图题和`02.png`采用`DSConv-L`。 |

**范文是否也如此—定位—同条件判断：** BMSFormer §3.1—3.2.2、PDF第6—7页正文和Fig.4/5采用`DSConv-L/DSConv-S`；Engineering-AI §4.2、PDF第7页以及methodology中§4.2.2用`S-DSConv/L-DSConv`。两篇的命名顺序不同，均可以成为各自论文的体系，但不应把两套命名混用来称本文同一模块。JESSOHRUL §2.2.2用`DSConv/MBConv1`，是不同模块，不能套入本文。三篇均无本文`SLFA`这个专名的定义，因此`Slim`的正确性来自本文自己的正式定义，不冒称范文证明。Engineering-AI §3.3及JESSOHRUL §3.5.2使用`screening`；此处同为筛选操作，拼写修复不涉及粒度提高。

### N2 流程图动名词标题与复数修饰语

| 位置（均为`figures/fig1.png`） | 现有英文 | 建议英文 | 简短中文原因 |
| --- | --- | --- | --- |
| 绿色左上标题 | Four datasets dividing | Division of the four datasets | 现有名词顺序生硬且缺少关系标记；只调整句法，保留四个数据集。 |
| 绿色右上标题 | Five models training, validating and testing | Training, validation, and testing of five models | 把操作名词并列，使`five models`的宾语关系明确。是否应保留`validation`另见待核项T2。 |
| 左侧电池列表 | others Cells | Other cells | `other`作限定词修饰复数名词，不用代词`others`。 |

**范文是否也如此—定位—同条件判断：** BMSFormer §2.1四步标题采用`Data acquisition / Feature engineering / Model training / Model evaluation`，正文明确训练、验证和其他电池测试；Engineering-AI §3.1也采用操作名词标题；JESSOHRUL §3.1.3和§3.2使用`model training`、`training and testing subsets`及训练/验证叙述。均是相同“操作—对象”功能，支持直接的操作名词结构。三篇协议与本文不同，不能借标题调整引入新的验证角色。`Other cells`属于语法修复，与范文是否存在类似错误无关。

### O5 图内冠词/名词修饰可以自然化

- **现有英文：** `Health indicators extraction`；`Health indicators splitting`。
- **建议英文：** `Health indicator extraction`；`HI sequence segmentation`。
- **原因：** 第一项与正文`Health indicator extraction`一致；第二项明确被分窗的是HI序列。若仅做最小语法调整，第二项也可用`Health indicator splitting`，但不如序列分段明确。
- **三篇尺度：** BMSFormer §2.3及JESSOHRUL §3.5.1标题本身使用`Health indicators extraction`，JES §3.5.2也有`Health indicators selection`。因此不能以“范文都不用复数修饰语”为依据声称必须改。Engineering-AI §3.3使用`extraction and screening of health indicators`，语法关系直接。本文正文已采用单数修饰，图内统一是可选润色，不是增加新筛选步骤。

## 三、需核实的图文对象问题，不按纯语言错误自动修复

### T1 SLFA图中的DSConv-L与正文DSConv-S

- **现有英文/对象：** `figures/fig3_3_attention_comparison.png`，(d)中卷积框为`DSConv-L`；第3章§3.3.3写`DSConv-S first extracts a local representation`，并且局部分支与RAA均来自X_S。
- **建议英文：** 如果图表示当前正文的SLFA，卷积应标`DSConv-S`，同时需要核对连接关系后再修图。不能仅换一个字母便宣称整图已经一致。
- **原因：** S/L是不同核尺度和不同位置的模块，不能把此处当作L-DSConv/DSConv-L同义顺序调整。图中Q/K/V、局部分支和末端Linear也应依据实现与正文核对。
- **三篇尺度：** BMSFormer §3.2.2—3.3.3区分DSConv-S在注意力内与DSConv-L在融合后；Engineering-AI §4.2.1—4.3.2也区分小核增强与大核融合后处理；JESSOHRUL DSCA/MBConv1结构不同，不能直接替换。本项是实际模块对象冲突，即使范文示意图会省略细节也应核实；不凭极端参数反例扩大问题。

### T2 流程图中的协议角色与用语

- **现有英文：** `Five models training, validating and testing`；`Train / Config. / Eval.`三排；`Battery role assignment`上方实际显示Prismatic/Cylindrical/Pouch；概览用`Cross-battery and cross-dataset evaluation`，下方用`Source-only testing`。
- **建议英文：** 先核对图示意图意图。若只是泛指流程，`training, configuration selection, and evaluation of five models`更接近正文既有协议；`Battery types`比`Battery role assignment`更符合图中三个外形分类。`cross-cell`和`source-only evaluation`可与正文统一。
- **原因与尺度：** 本文仅明确training cell与configuration-selection cell两种角色，“其余报告电池”不是自动出现的新第三类角色。BMSFormer §2.1和JES §3.2、§4.2.1确有各自训练/验证/测试设定，EAI §3.3也使用calibration/training及testing，但均不与本文同协议。因此不照抄范文的validation；也不把图中的简称机械判为新增独立测试集，先核清实际意图。本项不属于已证实语法错误。


