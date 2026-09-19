# 英文语言与三篇范文风格审校：第二、三章

日期：2026-09-13。按作者最新AGENTS审校现有英文，不重新翻译，不以反向回译为主。仅写建议，未修改论文正文。

本轮重新通读chapters/abstract.tex及chapter01.tex至chapter05.tex。第二、三章50+70=120个文字块（含标题、步骤、公式说明）按术语、动词搭配、句子主干、句间推进、信息颗粒度、表达力度六层审查。7个段落给出有效建议，113块保留；LS-M03因外部更新已修复而撤销，保留编号用于版本追踪。34个独立数学公式不作风格改写，外部图表input文件和栅格文字不纳入本册覆盖分母。

## 本批重新阅读的范文上下文

以下均为本轮重新查看的full.txt对应完整段落，不以旧词表替代。另直接从原PDF按页保留布局回读Engineering-AI第7–8页、JESSOHRUL第13–14页、BMSFormer第6页，以辨明双栏顺序。这是PDF文字布局核对，不声称新做全PDF视觉审查。

- JESSOHRUL：L1576–1590（HI构建、IC定义引段）；L1634–1647（Table 4）；L1671–1680（PCC/SCC完整段）；L1751–1760、L1773–1797、L1799–1811、L1822–1849（DTV及筛选完整相关段）。L1797的This method first接L1822的calculates，中间另一栏温度公式说明不可连入。
- BMSFormer：L731–746（模型引入和架构数据流完整段）；L766–789（标准卷积、计算量引导及符号）；L806–817、L837–841（深度/逐点卷积和符号上下文）。第6页左栏数据流与右栏卷积说明不能按TXT穿插顺序串读。
- Engineering-AI：L332–342（窗口标定引段）；L838–841（完整DSConv引段）；L845–849、L853及L828–829（置换和归一化说明）；L855–860接L875–884（小核双作用段）；L898–901及L914–921（大核细化）；L903–912、L923–927（智能体注意力上下文）。PDF第7–8页确认跨栏/跨页衔接，不能把AFF/AAT段混入DSConv段。

范文只提供匹配语境的短搭配及结构观察；本文建议不是范文原句。不照搬范文的长引导、生硬语法、ensure、aging inertia或rank restoration。没有把“范文也这么写”当作忽略直接性的理由。

## 完整段落建议

### LS-M01 — 可选搭配修复：charge timing容易联想到充电时机

位置：[chapter02.tex L60](D:/MS-AgentNet-English/chapters/chapter02.tex:60)；覆盖ID M02-023。

现有英文：

```latex
In addition to charge timing features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:
```

建议英文（完整段落，未写入）：

```latex
In addition to charging time features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:
```

范文依据：JESSOHRUL full.txt L1585–1590（完整IC定义引段）及Table 4 L1634–1647（时间与峰特征对应）；BMSFormer full.txt L275–283（窗口/标签完整步骤）。本批核实短引：“The charge time within the voltage range”。完整建议句属于本文适配，不是范文原句。

简短中文原因：这里对应前文CCCT时长特征，timing容易让读者先想到充电时机。charging time与本章charge duration的物理对象更明确。其余原句已经直接，保留。

六层复查：仅调整时间特征的搭配；IC、容量对电压求导、平台转峰、峰位和形状、引文与力度全保留。句子主干、段内推进及信息颗粒度不变。不是为简洁任意换术语。

### LS-M02 — 词汇简单但表达绕：长被动名词链与末尾编号回指

位置：[chapter02.tex L90](D:/MS-AgentNet-English/chapters/chapter02.tex:90)；覆盖ID M02-030。

现有英文：

```latex
where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge voltage and current, respectively, and integration is performed over the discharge time segments in which the voltage lies within $[V_l,V_h]$. Time is measured in s, and $Q_{\mathrm{dch}}$ is measured in Ah. Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

建议英文（完整段落，未写入）：

```latex
where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge voltage and current, respectively, and integration is performed over the discharge time segments in which the voltage lies within $[V_l,V_h]$. Time is measured in s, and $Q_{\mathrm{dch}}$ is measured in Ah. We further construct two candidate indicators of discharge capacity within a voltage window by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V. These indicators are denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

范文依据：JESSOHRUL full.txt L1799–1811（完整DTV处理/提取上下文），特别L1803–1811按特征逐一对应HI编号。本批核实短引：“four HIs are extracted”。完整建议句属于本文适配，不是范文原句。

简短中文原因：现句用Two candidate indicators of discharge capacity within a voltage window作长主语，等读完两个电压区间后才出现denoted as，编号需向前回找。建议以We construct明确动作，并把编号对齐单独成句；仍为同一自然段。

六层复查：术语与搭配：discharge capacity、voltage window、charge released保留；主干：We construct前置；推进：积分范围→单位→两个窗口→编号不变；颗粒度：四电压值、s/Ah、两个HI以及绝对电流公式指代保留；力度：未新增测量/因果结论。范文仅支持对象和编号贴近的功能，不是此完整句的原文来源。

### LS-M03 — 已撤销：外部更新已修复，保留当前段落

位置：[chapter02.tex L98](D:/MS-AgentNet-English/chapters/chapter02.tex:98)；覆盖ID M02-032。

末次重新读取的当前英文：

```latex
where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$ denote the terminal voltage, current magnitude, and duration of charging, respectively; $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote those of discharging. The full charging and discharging phases of each cycle are used. This energy efficiency is denoted as HI15 ($\eta$).
```

版本说明：审查期间该段由外部操作更新，现以分号分开充电和放电两组符号；respectively仅完成充电三符号的局部配对，放电组用those of discharging明确回指相同三个物理量。原“六符号and链”的问题已不存在。该正文更新不是本审校agent实施。

处置：撤销原LS-M03建议并保留现稿，不再为拆句或改写完整充放电阶段的表达而提出新修订。术语、六符号、完整循环条件、HI15及表达力度均保留。本编号仅作撤销记录，不计入7项有效建议。

### LS-M04 — 词汇简单但表达绕：结果被用于构造、再由which指定窗口

位置：[chapter02.tex L106](D:/MS-AgentNet-English/chapters/chapter02.tex:106)；覆盖ID M02-034。

现有英文：

```latex
Constant current charge time can reflect changes in battery capacity with cycling, but its correlation with SOH depends on the voltage interval used for extraction. Some studies directly extract time features from predefined local voltage intervals\cite{ref28,ref63}. However, degradation-sensitive intervals differ across datasets, and a fixed window used for one dataset is difficult to apply directly to others. To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT). Two cells from the same dataset form the feature-development set $\mathcal{B}$. Correlation results within this set are used to construct a group-level robust score, which determines the extraction window for HI1.
```

建议英文（完整段落，未写入）：

```latex
Constant current charge time can reflect changes in battery capacity with cycling, but its correlation with SOH depends on the voltage interval used for extraction. Some studies directly extract time features from predefined local voltage intervals\cite{ref28,ref63}. However, degradation-sensitive intervals differ across datasets, and a fixed window used for one dataset is difficult to apply directly to others. To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT). Two cells from the same dataset form the feature-development set $\mathcal{B}$. The method constructs a group-level robust score from correlations within this set and uses this score to determine the extraction window for HI1.
```

范文依据：JESSOHRUL full.txt L1671–1680（PCC/SCC段）及L1843–1849（完整跨电池选择解释段）；Engineering-AI full.txt L332–342（完整窗口/离线标定引段）。本批核实短引：“By evaluating candidates across several cells”。完整建议句属于本文适配，不是范文原句。

简短中文原因：最后一句把Correlation results作被动主语，再靠which转到窗口选择。以The method作主语并列constructs/uses，明确两步及得分的中介作用；不改变前面先说明动机、再定义方法和集合的顺序。

六层复查：术语：group-level robust score及HI1固定；搭配：constructs a score/uses this score；主干：The method执行两动作；推进和颗粒度：两电池、同数据集及集合B、评分后选窗全保留；力度：不从稳健得分推断额外泛化结果。本文最小绝对相关评分不同于三范文，仍标适配。

### LS-M05 — 词汇简单但表达绕：长设计名词串后which指向不够就近

位置：[chapter03.tex L1](D:/MS-AgentNet-English/chapters/chapter03.tex:1)；覆盖ID M03-001。

现有英文：

```latex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Slim Local-Global Fusion Attention (SLFA) module.
```

建议英文（完整段落，未写入）：

```latex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design of small-kernel DSConv-S and large-kernel DSConv-L. This design efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Slim Local-Global Fusion Attention (SLFA) module.
```

范文依据：Engineering-AI full.txt L838–841（完整DSConv小节引段）；BMSFormer full.txt L731–746（完整模型引入与架构段）。本批核实短引：“The kernel scales”。完整建议句属于本文适配，不是范文原句。

简短中文原因：第二句which前隔着DSConv-S与DSConv-L，读者需回溯它指的是整个多尺度设计。明确写This design作下一句主语，且不用comprising叠加名词串；名称→组成→作用顺序不变。

六层复查：术语/专名MS、DSConv-S/L、SLFA全保留；搭配extracts features不变；主干指向整个设计；推进保持名称→两尺度→作用→后文安排；不同时间尺度/高效和全部信息保留；不新增硬件或精度结果。

### LS-M06 — 指代回绕：Its computational cost越过parameter count回指

位置：[chapter03.tex L57](D:/MS-AgentNet-English/chapters/chapter03.tex:57)；覆盖ID M03-012。

现有英文：

```latex
Convolution extracts local information from time series through sliding kernels\cite{ref71}. Standard convolution operates across all input channels, with each kernel producing one output feature map corresponding to one output channel. As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time. A larger parameter count may also increase the risk of overfitting on small-sample battery datasets. Its computational cost can be expressed as:
```

建议英文（完整段落，未写入）：

```latex
Convolution extracts local information from time series through sliding kernels\cite{ref71}. Standard convolution operates across all input channels, with each kernel producing one output feature map corresponding to one output channel. As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time. A larger parameter count may also increase the risk of overfitting on small-sample battery datasets. The computational cost of standard convolution can be expressed as:
```

范文依据：BMSFormer full.txt L766–789（完整标准卷积成本引段，公式穿插处只用明确语句）；Engineering-AI full.txt L838–841（完整过拟合/DSConv设计段）。本批核实短引：“The standard convolutions have”。完整建议句属于本文适配，不是范文原句。

简短中文原因：最后一句Its最近的名词是parameter count或overfitting risk，实际要指standard convolution。直接点名对象比强求少词更清楚；这是独立于词难度的指代问题。其余段落保留。

六层复查：术语、所有成本/训练/过拟合判断不变；只明确公式主语的对象，后接同一公式。may保留，未升级因果或参数-实际耗时结论。句间推进与信息颗粒度保持。

### LS-M07 — 词汇简单但表达绕：融合句嵌套where及it回指

位置：[chapter03.tex L108](D:/MS-AgentNet-English/chapters/chapter03.tex:108)；覆盖ID M03-020。

现有英文：

```latex
2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

建议英文（完整段落，未写入）：

```latex
2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes the result to the fusion stage. There, the normalized local representation is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

范文依据：BMSFormer full.txt L735–744（完整数据流段）；Engineering-AI full.txt L855–860及L875–884（小核双作用段，跨页延续，顺序另见本册阅读说明）。本批核实短引：“output from LGFA module”。完整建议句属于本文适配，不是范文原句。

简短中文原因：第二句从归一化一路串到passes、where、it、to form，局部表示的对象在后半句只剩it。将融合动作单独成句并明确the normalized local representation；数据仍按分支→归一化→融合→互补表示推进，段落不拆。

六层复查：术语与模块位置不变；搭配passes the result/is combined与数据流匹配；主干按真实操作分开；局部/RAA两分支、LN、融合端和互补作用都保留；无额外rank restoration或噪声机制。

### LS-M08 — 词汇简单但表达绕：Given+where推迟真正的转置操作

位置：[chapter03.tex L110](D:/MS-AgentNet-English/chapters/chapter03.tex:110)；覆盖ID M03-021。

现有英文：

```latex
DSConv-S uses a channel expansion factor of two. Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:
```

建议英文（完整段落，未写入）：

```latex
DSConv-S uses a channel expansion factor of two. The input features are $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively. The input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:
```

范文依据：BMSFormer full.txt L735–746（输入/嵌入完整上下文）；Engineering-AI full.txt L845–849与L853、L828–829（置换段跨栏，见阅读说明）。本批核实短引：“The refined feature”。完整建议句属于本文适配，不是范文原句。

简短中文原因：原第二句在the input is first transposed之前放入给定输入、张量维度和三个符号定义。把张量及符号定义独立成句，再说明转置；不是删掉维度来求短。范文仅支持按输入→转置→后续运算说明，具体B×N×d保持本文。

六层复查：2倍扩展、B/N/d含义、转置目的、第一层1×1及2d都保留；语法主干更早完成；定义→转置→扩展顺序不变；没有段落拆并或新增张量操作。

## 全部文字块覆盖

编号沿用方法回译分册仅方便定位；审校标准为本轮六层语言审校。“保留”不是只检查简单词，也不是宣称母语无误。专业名称、维度、必要条件和有功能的重复不机械删除。

| 覆盖ID | 行号 | 当前段落开头 | 处置 |
|---|---|---|---|
| M02-001 | 1 | \subsection{Overview of the SOH estimation framework} | 保留；标题/专名及层级准确。 |
| M02-002 | 3 | To use a consistent definition in the following experiments, SOH is calcula… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-003 | 9 | where $C_{\mathrm{current}}$ and $C_{\mathrm{rated}}$ denote the current av… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-004 | 11 | The proposed SOH estimation framework is shown in \cref{fig:2-1}. | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-005 | 13 | (1) \textbf{Data acquisition.} Public battery aging data covering different… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-006 | 15 | (2) \textbf{Systematic feature engineering.} The proposed multi-source heal… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-007 | 17 | (3) \textbf{Model training.} Samples of the selected HIs are fed into MS-Ag… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-008 | 19 | (4) \textbf{Performance evaluation.} The trained model is directly applied … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-009 | 21 | \subsection{Typical battery datasets} | 保留；标题/专名及层级准确。 |
| M02-010 | 23 | Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/S… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-011 | 27 | \subsubsection*{(1) Oxford dataset} | 保留；标题/专名及层级准确。 |
| M02-012 | 29 | The Oxford dataset is provided by the Battery Intelligence Laboratory at th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-013 | 31 | \subsubsection*{(2) CALCE dataset} | 保留；标题/专名及层级准确。 |
| M02-014 | 33 | The CALCE dataset is provided by the Center for Advanced Life Cycle Enginee… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-015 | 35 | \subsubsection*{(3) MIT/Severson dataset} | 保留；标题/专名及层级准确。 |
| M02-016 | 37 | The MIT/Severson dataset was jointly released by the Massachusetts Institut… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-017 | 42 | \subsection{Feature engineering} | 保留；标题/专名及层级准确。 |
| M02-018 | 44 | This section presents the multi-source health indicator extraction and opti… | 保留；全称及筛选步骤有功能，仅主动化未见确定收益，不凑改动。 |
| M02-019 | 46 | \subsubsection{Health indicator extraction} | 保留；标题/专名及层级准确。 |
| M02-020 | 48 | Charging voltage--time (CVT), incremental capacity (IC), differential tempe… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-021 | 52 | The charging voltage--time (CVT) curve records changes in terminal voltage … | 保留；偏移→时长→原因→定义清楚，continuous/ongoing仅可选，不升级为必改。 |
| M02-022 | 58 | where $t(V_1)$ and $t(V_2)$ are the times when the charging voltage reaches… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-023 | 60 | In addition to charge timing features, changes in capacity with voltage als… | 建议LS-M01。 |
| M02-024 | 66 | where $V_k$ and $Q_k$ are the terminal voltage and charge capacity at the $… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-025 | 68 | Temperature is another important measure of the internal state of a battery… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-026 | 74 | where $V_k$ and $T_k$ are the terminal voltage and battery surface temperat… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-027 | 76 | While DTV characterizes the thermal response in the voltage domain, DTC cha… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-028 | 82 | where $T_k$ and $Q_k$ are the battery surface temperature and charge capaci… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-029 | 84 | Discharge capacity within a voltage window is obtained by integrating the d… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-030 | 90 | where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge vol… | 建议LS-M02。 |
| M02-031 | 92 | Energy efficiency reflects the energy conversion characteristics of a batte… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-032 | 98 | where $V_{\mathrm{ch}}(t)$, $\|I_{\mathrm{ch}}(t)\|$, and $t_{\mathrm{ch}}$ d… | 保留；L98外部新版本已用分号和those of discharging完成配对。LS-M03已撤销。 |
| M02-033 | 103 | \subsubsection{Group-level dual-correlation MS-CCCT} | 保留；标题/专名及层级准确。 |
| M02-034 | 106 | Constant current charge time can reflect changes in battery capacity with c… | 建议LS-M04。 |
| M02-035 | 108 | Most existing CCCT window optimization methods use PCC to evaluate candidat… | 保留语言；PCC/SCC对比直接，only对应中文已有技术表述，不能风格名义改科学含义。 |
| M02-036 | 122 | where $f_{i,j,k}$ is the CCCT extracted from the $i$th candidate window at … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-037 | 124 | To account for the correlation performance of each candidate window on both… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-038 | 131 | The smaller of these two values is then used as the group-level robust scor… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-039 | 137 | This score is determined by the lowest correlation across the two cells, pr… | 保留；preventing在方法语境表达作用，can仅可选，不当误译。 |
| M02-040 | 139 | MS-CCCT uses a three-stage coarse-to-fine search. For the Oxford dataset, t… | 保留；R1/R2/R3及判定条件各句承载信息，数值不能为缩短删除。 |
| M02-041 | 141 | For the Oxford dataset, the 3.55--3.75 V window is finally selected with th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-042 | 143 | \subsubsection{Health indicator selection} | 保留；标题/专名及层级准确。 |
| M02-043 | 145 | HI selection is a key step in lithium-ion battery SOH estimation\cite{ref60… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-044 | 147 | The correlation results for Oxford Cell1 and Cell2 are shown in \cref{fig:2… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-045 | 149 | The same candidate HI does not show identical correlation performance on th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-046 | 151 | Existing studies usually select HIs based on the magnitude of their correla… | 保留；长目的状语有衔接功能，仅移后不足以确立明显改善。 |
| M02-047 | 155 | Accordingly, this study develops a group-level HI selection method. It firs… | 保留；准入→排序→去冗余直接，重复操作词承担步骤对应。 |
| M02-048 | 158 | After correlation-based admission and redundancy removal, HI1 is retained f… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-049 | 160 | HI selection is performed only during feature development. Once the indicat… | 保留；only、固定定义/参数和三项排除均是必要协议范围。 |
| M02-050 | 162 | With its definition fixed, HI1 achieves absolute PCC values of 0.997874--0.… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-001 | 1 | To address the challenges of both accuracy and computational efficiency in … | 建议LS-M05。 |
| M03-002 | 3 | \subsection{Architecture overview of MS-AgentNet} | 保留；标题/专名及层级准确。 |
| M03-003 | 5 | The overall architecture of MS-AgentNet is shown in \cref{fig:3-1}. Health … | 保留；HI→窗口→嵌入→Block→读出→标签清楚，被动句适合处理对象。 |
| M03-004 | 7 | Mathematically, let the input to the $l$th MS-AgentNet Block be $\mathbf X_… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-005 | 9 | \textbf{Step 1: Local-global feature fusion.} The input $\mathbf X_l$ is pr… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-006 | 18 | \textbf{Step 2: Feature refinement over longer time scales.} The SLFA outpu… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-007 | 33 | \textbf{Step 3: Nonlinear mapping.} The features $\mathbf X_l''$ are proces… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-008 | 46 | The output $\mathbf Y_l$ is used as the input to the next Block, i.e., $\ma… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-009 | 50 | \subsection{The designed multi-scale depthwise separable convolution module… | 保留；标题/专名及层级准确。 |
| M03-010 | 52 | To combine multi-scale local feature extraction with computational efficien… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-011 | 55 | \subsubsection{Basic DSConv structure and computational cost comparison} | 保留；标题/专名及层级准确。 |
| M03-012 | 57 | Convolution extracts local information from time series through sliding ker… | 建议LS-M06。 |
| M03-013 | 66 | where $k$, $C_{\mathrm{in}}$, $C_{\mathrm{out}}$, and $D_F$ denote the kern… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-014 | 68 | Unlike standard convolution, depthwise separable convolution (DSConv) divid… | 保留；通道内与跨通道分工清楚，术语重复承担对比。 |
| M03-015 | 79 | The ratio of the computational costs of the two types of convolution is: | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-016 | 100 | Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and o… | 保留语言；成本比适用条件是源技术事项，不在风格稿中擅补。 |
| M03-017 | 102 | \subsubsection{DSConv-S: Dual-role local enhancement} | 保留；标题/专名及层级准确。 |
| M03-018 | 104 | Small-kernel DSConv-S uses a compact $1\times5$ depthwise convolution and i… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-019 | 106 | 1. \textbf{Input enhancement.} DSConv-S extracts local neighborhood informa… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-020 | 108 | 2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to … | 建议LS-M07。 |
| M03-021 | 110 | DSConv-S uses a channel expansion factor of two. Given input features $\mat… | 建议LS-M08。 |
| M03-022 | 122 | The expanded features pass through a $1\times5$ depthwise convolution, whic… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-023 | 131 | A ReLU activation is then applied to introduce nonlinearity: | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-024 | 139 | Next, the second $1\times1$ pointwise convolution fuses information across … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-025 | 148 | Finally, the output is transposed back to its original arrangement and comb… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-026 | 159 | where $\operatorname{PW}_{\uparrow}$ and $\operatorname{PW}_{\downarrow}$ d… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-027 | 161 | \textbf{Computational analysis.} With a channel expansion factor of two, th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-028 | 170 | where $2C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-029 | 172 | \subsubsection{DSConv-L: Feature refinement over longer time scales} | 保留；标题/专名及层级准确。 |
| M03-030 | 174 | DSConv-L follows SLFA and uses a channel expansion factor of three and a $1… | 保留；位置、3倍、1×31、Block层残差清楚，必要细节不是冗词。 |
| M03-031 | 176 | \textbf{Computational analysis.} With a channel expansion factor of three, … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-032 | 185 | where $3C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-033 | 189 | \subsection{The proposed Slim Local-Global Fusion Attention module} | 保留；标题/专名及层级准确。 |
| M03-034 | 191 | This section presents the general form of multi-head self-attention, briefl… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-035 | 194 | \subsubsection{General form of multi-head self-attention} | 保留；标题/专名及层级准确。 |
| M03-036 | 196 | Multi-head self-attention uses multiple parallel attention heads to calcula… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-037 | 205 | where $N$ is the sequence length, $d$ is the input feature dimension, and $… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-038 | 207 | When a nonnegative similarity function is used to construct normalized atte… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-039 | 223 | where $\mathbf Q_{i,p}$ is the query at the $p$th position in the $i$th att… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-040 | 225 | The outputs at all positions form the output matrix $\mathbf O_i\in\mathbb … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-041 | 227 | \subsubsection{Softmax attention and linear attention} | 保留；标题/专名及层级准确。 |
| M03-042 | 229 | Standard Softmax attention calculates correlations between sequence positio… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-043 | 242 | The exponential mapping and normalization in Softmax assign larger attentio… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-044 | 244 | To address the quadratic computational cost of Softmax attention, linear at… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-045 | 263 | where $\phi(\cdot)$ is a nonnegative feature mapping, such as $\phi(\mathbf… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-046 | 265 | By first calculating $\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$, linear att… | 保留；先KᵀV、避免N×N、映射维度及固定dh各有必要，顺序直接。 |
| M03-047 | 267 | Linear attention enables global information interactions at a lower computa… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-048 | 269 | \subsubsection{The proposed SLFA module} | 保留；标题/专名及层级准确。 |
| M03-049 | 271 | To capture both local neighborhood features and cross-position interactions… | 保留；局部表示、RAA和加法融合清楚，不为仿范文增加修饰。 |
| M03-050 | 273 | \textbf{(1) ReLU² Agent Attention.} | 保留；标题/专名及层级准确。 |
| M03-051 | 275 | Agent Attention uses a small number of agents as information intermediaries… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-052 | 277 | To reduce the parameter overhead of query, key, and value generation, RAA u… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-053 | 286 | where $\mathbf s_q,\mathbf s_k,\mathbf s_v\in\mathbb R^d$ are learnable cha… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-054 | 288 | Compared with standard linear projections for queries, keys, and values, wh… | 保留当前已修订句；线性投影与通道缩放向量比较对象清楚，不报旧版问题。 |
| M03-055 | 290 | RAA uses $n_a=2$ learnable agents, represented by a matrix $\mathbf A\in\ma… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-056 | 292 | The global agent matrix $\mathbf A$ is divided into $h$ subspaces along the… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-057 | 294 | During information broadcasting, each query assigns context weights accordi… | 保留；共同缩小→权重均匀→等权读取→RAA动机清楚，非每个长解释都绕。 |
| M03-058 | 311 | where $M$ is the number of elements normalized in each row: $M=N$ during ag… | 保留；M条件、截断、抵消、平方、无正得分回退各为独立必要信息。 |
| M03-059 | 313 | During agent aggregation, $\mathbf A_i$ acts as the query to gather context… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-060 | 329 | where $\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$ contains the weig… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-061 | 331 | During information broadcasting, each query position reads information from… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-062 | 347 | where $\boldsymbol{\Phi}_{q,i}\in\mathbb R^{N\times n_a}$ contains the broa… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-063 | 349 | Equations \eqref{eq:agent_aggregation} and \eqref{eq:agent_broadcast} show … | 保留；等效映射与秩上界明确，数学对象长度不是改写理由。 |
| M03-064 | 351 | The outputs of all attention heads are concatenated along the feature dimen… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-065 | 361 | where $\operatorname{Concat}(\cdot)$ concatenates the outputs of all attent… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-066 | 363 | RAA generates correlation matrices of size $n_a\times N$ and $N\times n_a$ … | 保留；单/多头计算、内存及固定h/na均明确，未推断实测速度。 |
| M03-067 | 365 | \textbf{(2) Local-global feature fusion.} | 保留；标题/专名及层级准确。 |
| M03-068 | 367 | The input features $\mathbf X$ first pass through DSConv-S to obtain the lo… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-069 | 382 | where $\mathbf X_F$ is the fused SLFA output, $\operatorname{LN}(\mathbf X_… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-070 | 384 | This additive connection preserves the local degradation features extracted… | 保留；局部保留、全局融合、线性复杂度各有功能。 |

## 交付复查

7项有效建议保持原段落边界及信息次序；数学表达、全部引用键和数字保持。LS-M03已撤销，不纳入有效建议。LS-M08仍按“2倍扩展→输入张量→B/N/d定义→转置目的→1×1扩展2d”推进，只在符号定义后完成一句，再开始转置，不把操作先移到定义前。LS-M02改成We construct不是收益的唯一理由，主要修复是将末尾HI编号配对从长句中独立，避免远距离回指。

7项有效建议不是7项误译。LS-M01为可选术语搭配消歧，其余针对名词被动链、主干或指代。对于2章L44和L151，已拒绝仅主动化或更换目的状语位置的候选；L98的外部新版本配对已清楚，保留。先前回译报告里的源数学/协议问题不自动成为本阶段语言修改。

仅新增本审校文档。作者确认前不写入论文。
