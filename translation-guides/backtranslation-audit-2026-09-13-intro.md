# 反向回译审查：摘要与第一章（2026-09-13）

这是本轮新建的审查记录，不是获准写入正文的修改稿。审查依据为当前 source-zh/chapters 与 chapters 文件，未把此前聊天所述检查当作证据。负责范围：摘要自然段、关键词；第一章全部21个自然段及2个小节标题，共25个可见文本块。第一章引用的表1和主文件里的章标题由总报告的附属文本审查覆盖。

方法：阅读英文，按英文实际可表达的意思生成回译，再对照中文逐义核验。已知原中文及全文上下文，因此这不是独立盲回译；回译文字不作为英文唯一解释的证明。原文代码完整保留，回译为了阅读不重复LaTeX引文标记，但保护内容另对照原文。五项依次为①漏增译/原义，②术语数字限定，③地道简洁，④夸大绝对化复杂词，⑤三篇范文对应语境。每块附处置意见，建议均未写入正文。

已读准备：START_TRANSLATION.md、工作流、风格、术语、科学边界、house-style、expression-detail-rules、参考使用与颗粒度指南；通读五章中文正文以理解输入/模型/实验边界；核对摘要与P01/P02单独批准、全文授权及language-fixes-batch-01记录。范文核对包括三篇abstract.txt、introduction.txt及下列full.txt相关完整段。复用已保存的摘要和引言P01/P02/P03句级计量记录，回看原始TXT以核对本轮词义；本轮未重新声明独立测得这些历史统计或重新完成全PDF视觉审查。

## 本轮直接回看的范文证据索引

定位均为 style-references/论文目录/full.txt 的1基行号；中文为助手释义。短引仅用来核对措辞，其余说明为适用边界。

- B1：BMSFormer 30–40，摘要模块、资源与比较语境。短引“resource-consuming structures”（消耗资源的结构）与“Local-Global Fusion Attention”（局部—全局融合注意力）。本文的resource-consuming因此有原文依据，不能仅凭个人偏好认定不地道。
- B2：BMSFormer 49–92，引言应用—安全风险—BMS约束完整段。本文保留更具体的老化机制；范文不证明这些机制是本文模型已保障的结果。
- B3：BMSFormer 94–218，方法分类、模型驱动、数据驱动、CNN/RNN/Transformer及挑战段。短引“model-based approaches”（基于模型的方法）。TXT双栏顺序有交错，本轮只取可恢复的完整段义，不按TXT先后推断论文论证顺序。
- E1：Engineering-AI 34–47，摘要HI→轻量网络→实验。短引“long-range degradation dependencies”（长程退化依赖）。此处的框架硬件验证不适用于本稿。
- E2：Engineering-AI 65–96，引言直接容量测量和在线约束完整段。短引“full charge–discharge cycles”（完整充放电循环）。本稿near full为源中文必要补充。
- E3：Engineering-AI 271–276，§3.1容量定义段。短引“capacity retention”（容量保持率）。max available在该段出现，但本稿额定容量等口径从本稿定义核对。
- E4：Engineering-AI 116–141、164–187，电化学/ECM及特征工程相关段：解释性、参数、温度倍率和导数噪声语境；引用条目不作为本文外部实验事实认证。
- E5：Engineering-AI 197–225，§2.2.2，RNN顺序运算、CNN感受野、Transformer时间/内存二次复杂度完整项目。
- J1：JESSOHRUL 33–50，摘要HI提取—双相关筛选—多数据集评估。其SOH-RUL任务与本文SOH任务不同。
- J2：JESSOHRUL 105–140，引言HI来源、阻抗/温度限制、IC及时间指标完整段。其筛选窗口的具体操作不能替代本文CCCT定义。
- J3：JESSOHRUL 1671–1680、1822–1840，§3.5.2，相关类型及筛选完整段。短引“linear correlation”（线性相关）、“monotonic relationship”（单调关系）、“highly redundant information”（高度冗余信息）。只借对应概念，范文阈值和全电池范围不导入本文。

## 逐块对照

### ABS-P01｜abstract.tex:1

源位置：source-zh/chapters/abstract.tex:1；英文位置：chapters/abstract.tex:1。

中文原文：

```tex
高效准确的锂离子电池健康状态估计，对保障电池安全运行和支持资源受限电池管理系统的在线应用至关重要。然而，现有估计方法往往依赖跨电池稳定性有限的健康指标和资源开销较大的模型结构。为此，本文提出一种轻量化的SOH估计框架。首先，提出多源健康指标提取与优化算法，以筛选跨电池稳健的健康指标并减少特征冗余。随后，构建轻量化预测网络MS-AgentNet。该网络主要集成局部—全局融合注意力模块，通过小核深度可分离卷积与ReLU²智能体注意力协同捕获局部退化特征与长程退化依赖，同时将传统Transformer的二次注意力复杂度降至线性。此外，大核深度可分离卷积用于提取长尺度退化特征，并与小核卷积共同以较低参数开销融合多尺度和多通道特征，增强特征多样性。我们在四个涵盖不同化学体系和运行条件的公开电池数据集上，将所提模型与多种主流深度学习模型进行了比较。实验结果表明，MS-AgentNet总体上取得了更优的综合性能，同时保持了较低的计算与存储开销，进一步体现了其面向资源受限电池管理系统的轻量化优势。
```

当前英文：

```tex
Efficient and accurate estimation of lithium-ion battery state of health (SOH) is crucial for ensuring safe battery operation and supporting online applications in resource-limited battery management systems (BMS). However, many existing SOH estimation approaches often rely on health indicators (HIs) with limited stability across cells and resource-consuming model structures. Therefore, this paper proposes a lightweight SOH estimation framework. First, a multi-source health indicator extraction and optimization algorithm is proposed to select HIs that are robust across cells and reduce feature redundancy. Subsequently, a lightweight prediction network, MS-AgentNet, is constructed. The network mainly integrates a local-global fusion attention module that combines small-kernel depthwise separable convolutions with ReLU² agent attention to capture local degradation features and long-range degradation dependencies, while reducing the quadratic attention complexity of traditional Transformers to linear complexity. Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity. We compared the proposed model with various mainstream deep learning models on four public battery datasets with different chemistries and operating conditions. The experimental results show that MS-AgentNet achieves better overall performance while maintaining low computational and storage overhead, further highlighting the advantages of its lightweight design for resource-limited BMS.
```

中文回译：

高效、准确地估计锂离子电池的健康状态（SOH），对于保障电池安全运行以及支持资源受限电池管理系统（BMS）中的在线应用至关重要。然而，许多现有SOH估计方法往往依赖跨电池稳定性有限的健康指标（HI）以及资源消耗较大的模型结构。因此，本文提出一种轻量化SOH估计框架。首先，提出一种多源健康指标提取与优化算法，以筛选在不同电池间稳健的HI并减少特征冗余。随后，构建轻量化预测网络MS-AgentNet。该网络主要集成一个局部—全局融合注意力模块，将小核深度可分离卷积与ReLU²智能体注意力结合，以捕获局部退化特征和长程退化依赖，同时将传统Transformer的二次注意力复杂度降为线性复杂度。此外，大核深度可分离卷积用于提取更长时间尺度上的退化特征，并与小核卷积共同以低参数开销融合多尺度和多通道特征，增强特征多样性。我们在四个具有不同化学体系和运行条件的公开电池数据集上，将所提模型与多种主流深度学习模型进行了比较。实验结果表明，MS-AgentNet取得了更好的总体性能，同时保持低计算与存储开销，进一步体现其轻量化设计面向资源受限BMS的优势。

五项审查：

1. 基本对应；many为已明确批准的新增限定。句末“总体上取得了更优的综合性能”压成better overall performance，overall直接修饰performance，可理解为综合性能，却未单独表达结果在总体层面的限定。属于已批准文本中的轻度范围弱化风险，非确定的普遍优越宣称。
2. 四个数据集、HI、两种卷积、ReLU²、注意力二次转线性对应；longer time scales与第三章较长时间尺度一致。
3. 整体可读；mainly integrates及resource-consuming model structures接近BMS原句，前者略模板化但无语法硬伤；many…often稍重复，因已批准不要求重决。
4. ensuring对应保障且描述需求，不是模型已保证安全。两处low比“较低”更直接，属可选程度贴合；未出现prove或部署完成。
5. B1、E1、J1支持模块/资源、长程依赖、HI提取筛选各自语境；不继承三篇实验结果。

处置：可选最小修改：末句MS-AgentNet generally achieves better overall performance…；只有作者选择严格恢复双重限定时采用。low可保留，不列强制修订。

### ABS-K01｜abstract.tex:3

源位置：source-zh/chapters/abstract.tex:3；英文位置：chapters/abstract.tex:3。

中文原文：

```tex
\textbf{关键词：} 锂离子电池；健康状态估计；线性复杂度；深度特征融合；轻量化深度学习
```

当前英文：

```tex
\textbf{Keywords:} lithium-ion batteries; state-of-health estimation; linear complexity; deep feature fusion; lightweight deep learning
```

中文回译：

关键词：锂离子电池；健康状态估计；线性复杂度；深度特征融合；轻量化深度学习。

五项审查：

1. 五个关键词逐一对应。
2. deep feature fusion保留深度特征融合，不误写BMS的depthwise feature fusion。
3. 自然、简洁。
4. 无夸大或无必要复杂词。
5. B1/E1/J1均有相关关键词，但本文深度特征融合为已批准技术适配。

处置：无须修改。

### C01-B01｜chapter01.tex:1

源位置：source-zh/chapters/chapter01.tex:1；英文位置：chapters/chapter01.tex:1。

中文原文：

```tex
锂离子电池凭借高能量密度、长循环寿命和低自放电率等优势，已广泛应用于电动汽车、便携式电子设备和规模化储能等领域\cite{ref1,ref2,ref3,ref4}，是支撑新能源交通、智能终端和能源存储行业发展的重要储能技术。尽管如此，电池在长期运行中仍存在不可忽视的安全风险。充放电循环与复杂工况会引发固体电解质界面（solid electrolyte interphase, SEI）膜增厚、活性锂损失和电极结构衰退等老化现象\cite{ref5,ref6}，进而导致容量衰减和性能下降，严重时将诱发短路、热失控等故障\cite{ref7,ref8}。因此，精确估计锂离子电池的健康状态对于保障电池的安全性、可靠性和运行性能至关重要。
```

当前英文：

```tex
With their high energy density, long cycle life, and low self-discharge rate, lithium-ion batteries have found widespread use in electric vehicles, portable electronic devices, and large-scale energy storage\cite{ref1,ref2,ref3,ref4}. As an important energy storage technology, they support the development of transportation powered by new energy sources, smart devices, and the energy storage industry. However, batteries still pose safety risks that cannot be ignored during long-term operation. Charge-discharge cycling and complex operating conditions lead to aging processes such as thickening of the solid electrolyte interphase (SEI) layer, loss of active lithium, and structural degradation of the electrodes\cite{ref5,ref6}. These processes cause capacity fade and reduced performance and, in severe cases, lead to failures such as short circuits and thermal runaway\cite{ref7,ref8}. Therefore, accurate estimation of the state of health of lithium-ion batteries is crucial for ensuring battery safety, reliability, and operating performance.
```

中文回译：

凭借高能量密度、长循环寿命和低自放电率，锂离子电池已广泛用于电动汽车、便携式电子设备和大规模储能。作为一种重要的储能技术，它们支持由新能源驱动的交通、智能设备和储能产业的发展。然而，电池在长期运行中仍带来不可忽视的安全风险。充放电循环及复杂运行条件导致固体电解质相间层（SEI）增厚、活性锂损失和电极结构退化等老化过程。这些过程造成容量衰减和性能降低，严重时会引发短路、热失控等故障。因此，准确估计锂离子电池健康状态对于保障电池安全性、可靠性和运行性能至关重要。

五项审查：

1. 信息顺序、三种老化现象与两种严重故障均对应。新能源交通按已批准描述译出，其行业边界在中文中仍待界定。
2. SEI的interphase保留源稿括号英文；thickening对应增厚；智能终端译smart devices较宽，为已批准译法，需精确区分终端与一般设备时另行确认。
3. 读来通顺，risk that cannot be ignored偏直译但忠实不可忽视，非硬错。
4. in severe cases保留严重时；ensuring为需求陈述。
5. B2背景—风险—必要性的语境匹配；EAI的SEI growth不替代厚度专指，机制词为源文技术适配。

处置：不作强制修改；“新能源交通”的边界属于已记录的原中文待确认项。

### C01-B02｜chapter01.tex:3

源位置：source-zh/chapters/chapter01.tex:3；英文位置：chapters/chapter01.tex:3。

中文原文：

```tex
容量衰减是电池老化最直观的特征，健康状态（state of health, SOH）通常采用容量保持率定义\cite{ref13,ref14}。但电池最大可用容量的精确测算需要完整或近似完整的充放电循环，难以满足在线监测需求\cite{ref10,ref11}。因此，从可观测运行信号中间接估计SOH已成为在线健康监测的关键途径。然而，复杂工况增加了退化信息稳定提取的难度，而电池管理系统（battery management system, BMS）严格的计算与存储限制又制约了模型复杂度，使在线SOH估计面临退化信息提取与模型计算效率的双重挑战\cite{ref31}。
```

当前英文：

```tex
Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurate measurement of a battery's maximum available capacity requires full or nearly full charge-discharge cycles, a requirement that is difficult to meet in online monitoring\cite{ref10,ref11}. Consequently, indirect estimation of SOH from observable operating signals has become a key approach to online health monitoring. However, complex operating conditions make the stable extraction of degradation information more difficult, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity. These limitations pose a dual challenge for online SOH estimation: extracting degradation information and maintaining model computational efficiency\cite{ref31}.
```

中文回译：

容量衰减是电池老化最直接的迹象，健康状态（SOH）通常用容量保持率定义。然而，准确测量电池最大可用容量需要完整或近乎完整的充放电循环，这一要求在在线监测中难以满足。因此，根据可观测运行信号间接估计SOH已成为在线健康监测的关键方法。然而，复杂运行条件使退化信息的稳定提取更加困难，而电池管理系统（BMS）严格的计算和存储约束限制了模型复杂度。这些限制给在线SOH估计带来双重挑战：提取退化信息和保持模型计算效率。

五项审查：

1. 定义、近似完整、间接估计及双重挑战均对应。
2. maximum available capacity/ capacity retention一致；未把容量定义分母加进本段。
3. 两个However各接不同转折，略密但并非不自然到必须重写。
4. commonly与full or nearly full保留限制；未称SOH绝对不可测。
5. E2与E3精确对应周期要求及容量词；B2支持资源约束。

处置：无须修改。

### C01-B03｜chapter01.tex:5

源位置：source-zh/chapters/chapter01.tex:5；英文位置：chapters/chapter01.tex:5。

中文原文：

```tex
\subsection{文献综述}
```

当前英文：

```tex
\subsection{Literature review}
```

中文回译：

文献综述

五项审查：

1. 标题对应。
2. 无数字或条件。
3. 惯用标题。
4. 无强词。
5. 三篇综述功能一致，标题为常规适配，不冒充唯一原题。

处置：无须修改。

### C01-B04｜chapter01.tex:7

源位置：source-zh/chapters/chapter01.tex:7；英文位置：chapters/chapter01.tex:7。

中文原文：

```tex
近期的健康状态估计方法主要分为模型驱动和数据驱动两类\cite{ref10,ref11,ref12}。前者包括电化学模型和等效电路模型，后者包括传统机器学习和深度学习方法。
```

当前英文：

```tex
Recent SOH estimation approaches can be classified into two main categories: model-based and data-driven approaches\cite{ref10,ref11,ref12}. The former include electrochemical models and equivalent circuit models, while the latter include traditional machine learning and deep learning methods.
```

中文回译：

近期SOH估计方法可分为两大类：基于模型的方法和数据驱动方法。前者包括电化学模型和等效电路模型，后者包括传统机器学习和深度学习方法。

五项审查：

1. 两类及各自子类完整。
2. model-based遵循术语表；equivalent circuit未被范文empirical替代。
3. 分类结构自然。
4. can be classified不改变主要分类强度。
5. B3及EAI §2分类段、JES引言分类段已读；选择BMS/EAI的model-based，未混用model-driven。

处置：无须修改。

### C01-B05｜chapter01.tex:9

源位置：source-zh/chapters/chapter01.tex:9；英文位置：chapters/chapter01.tex:9。

中文原文：

```tex
模型驱动方法通过数学方程或等效电路模拟电池内部的电化学机制\cite{ref19}。其中，电化学模型以微分方程表示电池的反应与退化过程。例如，Li等人\cite{ref21}基于单粒子模型（SPM），构建了同时考虑化学退化与机械损伤的SOH估计框架。虽然这类模型具有较好的物理可解释性和估计精度，但求解复杂方程需要较多计算资源，颗粒半径、扩散系数等参数也难以获取，限制了其在资源受限BMS中的在线应用\cite{ref20,ref22,ref23}。相比之下，等效电路模型（ECM）将复杂的电化学过程简化为由电阻、电容等元件组成的电路，以模拟电池充放电动态特性\cite{ref19}。例如，Chen等人\cite{ref24}采用递推最小二乘法辨识Thevenin模型参数，并根据欧姆内阻与容量衰减的关系估计SOH。这种简化降低了模型的计算开销，但也使其难以全面刻画电池内部状态的变化。与电化学模型相比，ECM的估计精度可能较低，且依赖于所选电路结构与模型参数。此外，ECM参数对温度和充放电倍率等工况高度敏感，使其难以在整个老化周期内保持良好的估计鲁棒性\cite{ref19}。
```

当前英文：

```tex
Model-based approaches simulate the electrochemical mechanisms inside batteries using mathematical equations or equivalent circuits\cite{ref19}. Electrochemical models use differential equations to describe battery reactions and degradation processes. For example, Li et al.\cite{ref21} developed an SOH estimation framework based on a single-particle model (SPM) that accounts for both chemical degradation and mechanical damage. Although these models offer good physical interpretability and estimation accuracy, solving complex equations requires substantial computational resources, and parameters such as particle radius and diffusion coefficients are difficult to obtain. These limitations hinder their online application in resource-limited BMS\cite{ref20,ref22,ref23}. In contrast, equivalent circuit models (ECMs) simplify complex electrochemical processes into circuits composed of resistors, capacitors, and other components to simulate battery charge-discharge dynamics\cite{ref19}. For example, Chen et al.\cite{ref24} used recursive least squares to identify the parameters of a Thevenin model and estimated SOH from the relationship between ohmic resistance and capacity fade. This simplification reduces computational overhead but makes it difficult to fully capture changes in the internal battery state. Compared with electrochemical models, ECMs may provide lower estimation accuracy and depend on the selected circuit structure and model parameters. In addition, ECM parameters are highly sensitive to operating conditions such as temperature and charge-discharge rate, making it difficult to maintain robust estimation throughout the aging process\cite{ref19}.
```

中文回译：

基于模型的方法采用数学方程或等效电路模拟电池内部的电化学机制。电化学模型使用微分方程描述电池反应和退化过程。例如，Li等人基于单粒子模型（SPM）开发了一种兼顾化学退化和机械损伤的SOH估计框架。尽管这些模型具有良好的物理可解释性和估计精度，求解复杂方程仍需要大量计算资源，而且颗粒半径、扩散系数等参数难以获得。这些限制阻碍了其在资源受限BMS中的在线应用。相比之下，等效电路模型（ECM）将复杂电化学过程简化为由电阻、电容等元件组成的电路，以模拟电池充放电动态。例如，Chen等人使用递推最小二乘法辨识Thevenin模型参数，并根据欧姆电阻和容量衰减之间的关系估计SOH。这种简化减少了计算开销，却使完整捕获电池内部状态变化变得困难。与电化学模型相比，ECM可能提供更低的估计精度，并依赖所选电路结构和模型参数。此外，ECM参数对温度、充放电倍率等运行条件高度敏感，使整个老化过程中保持稳健估计变得困难。

五项审查：

1. 主要信息对应；末部ECMs may provide lower estimation accuracy and depend on…在语法上may可同时管辖provide和depend，而中文只有“估计精度可能较低”，依赖关系是直接陈述。轻微情态范围歧义。
2. SPM、ECM、Thevenin、递推最小二乘、颗粒半径和扩散系数准确。
3. 表达清楚；“ECMs…depend on”把精度依赖简化成模型依赖，结合上下文可读懂，宜随情态范围一并明确。
4. substantial对应较多资源，无统计增强；highly对应高度。
5. B3与E4对电化学/电路模型及工况敏感性的对象匹配。

处置：建议最小修正为：Compared with electrochemical models, ECMs may provide lower estimation accuracy, and their accuracy depends on the selected circuit structure and model parameters. 保留可能较低，同时明确依赖对象。

### C01-B06｜chapter01.tex:11

源位置：source-zh/chapters/chapter01.tex:11；英文位置：chapters/chapter01.tex:11。

中文原文：

```tex
相较于模型驱动方法，数据驱动方法无需建立详细的电化学模型或深入分析电池内部的反应及老化机制\cite{ref11,ref14}。这类方法利用历史运行数据训练模型，将提取的健康指标映射为SOH估计值。早期研究主要采用传统机器学习模型进行电池状态估计与寿命预测\cite{ref25}。例如，Fei等人\cite{ref26}从前100个循环的充放电数据中构造42个特征，经筛选后输入弹性网络、高斯过程回归（GPR）、支持向量机（SVM）、随机森林（RF）、梯度提升回归树（GBRT）和神经网络（NN）六种模型，比较其早期寿命预测表现。Li等人\cite{ref27}则利用局部充电过程中的电压和容量数据，通过随机森林实现在线容量估计。然而，当面对来自在线监测和历史循环的非线性、波动性数据时，传统机器学习模型因其结构限制而难以提供高性能。
```

当前英文：

```tex
Compared with model-based approaches, data-driven approaches do not require detailed electrochemical models or an in-depth analysis of internal battery reactions and aging mechanisms\cite{ref11,ref14}. These approaches train models on historical operating data to map extracted health indicators to SOH estimates. Early studies mainly used traditional machine learning models for battery state estimation and lifetime prediction\cite{ref25}. For example, Fei et al.\cite{ref26} constructed 42 features from charge-discharge data for the first 100 cycles. After feature selection, they fed the retained features into six models, namely elastic net, Gaussian process regression (GPR), support vector machine (SVM), random forest (RF), gradient boosting regression tree (GBRT), and neural network (NN), to compare their performance in early prediction of battery lifetime. Li et al.\cite{ref27} used voltage and capacity data from partial charging processes to estimate capacity online with a random forest. However, when handling nonlinear and fluctuating data from online monitoring and historical cycles, traditional machine learning models struggle to achieve high performance because of their structural constraints.
```

中文回译：

与基于模型的方法相比，数据驱动方法不需要详细的电化学模型，也不需要深入分析电池内部反应和老化机制。这些方法利用历史运行数据训练模型，将提取的健康指标映射为SOH估计值。早期研究主要使用传统机器学习模型进行电池状态估计和寿命预测。例如，Fei等人从前100个循环的充放电数据中构造了42个特征。特征筛选后，他们将保留特征输入弹性网络、高斯过程回归（GPR）、支持向量机（SVM）、随机森林（RF）、梯度提升回归树（GBRT）和神经网络（NN）这六种模型，以比较其电池寿命早期预测性能。Li等人利用部分充电过程中的电压和容量数据，通过随机森林在线估计容量。然而，在处理在线监测和历史循环中的非线性、波动数据时，传统机器学习模型因结构约束难以实现高性能。

五项审查：

1. 历史数据、前100循环、42特征、筛选后六模型、局部充电和结构限制完整。
2. 42、100、six及六个模型名称一致；未按BMS的五模型叙述篡改本稿。
3. 常用动词train/map/feed/estimate，平行结构清楚。
4. 无不必要绝对化；do not require对应无需。
5. B3及JES引言数据驱动段支持输入到SOH映射；具体研究人数/实验细节以中文为准。

处置：无须修改。

### C01-B07｜chapter01.tex:13

源位置：source-zh/chapters/chapter01.tex:13；英文位置：chapters/chapter01.tex:13。

中文原文：

```tex
随着深度学习的快速发展，研究者进一步采用多层神经网络，利用其较强的非线性表征能力捕捉复杂的电池退化模式，以提高估计精度\cite{ref14}。卷积神经网络（CNN）、循环神经网络（RNN）和Transformer是其中常用的模型。CNN利用卷积核提取局部特征，并通过池化操作降低特征维度。例如，Qian等人\cite{ref29}将随机选取的充电曲线片段输入一维CNN，用于电池容量估计。结果表明，该方法在随机片段输入条件下取得了较低的容量估计误差。Lee等人\cite{ref30}则将跨循环的容量衰减序列转换为二维图像，并采用二维CNN估计SOH。
```

当前英文：

```tex
With the rapid development of deep learning, researchers have increasingly used multilayer neural networks to capture complex battery degradation patterns through their strong nonlinear representational capability and thereby improve estimation accuracy\cite{ref14}. Convolutional neural networks (CNNs), recurrent neural networks (RNNs), and Transformers are commonly used models. CNNs extract local features using convolutional kernels and reduce feature dimensions through pooling operations. For example, Qian et al.\cite{ref29} fed randomly selected charging-curve segments into a one-dimensional CNN for battery capacity estimation. Their results showed low capacity estimation errors with randomly selected input segments. Lee et al.\cite{ref30} converted capacity fade sequences across cycles into two-dimensional images and used a two-dimensional CNN to estimate SOH.
```

中文回译：

随着深度学习快速发展，研究者日益使用多层神经网络，借助其强大的非线性表征能力捕获复杂电池退化模式，从而提高估计精度。卷积神经网络（CNN）、循环神经网络（RNN）和Transformer是常用模型。CNN通过卷积核提取局部特征，并通过池化操作降低特征维度。例如，Qian等人将随机选取的充电曲线片段输入一维CNN以估计电池容量。其结果显示，在随机选择的输入片段下，容量估计误差较低。Lee等人把跨循环容量衰减序列转换为二维图像，并用二维CNN估计SOH。

五项审查：

1. 全部研究例子对应。increasingly较“进一步”更显趋势，但深度学习发展的上下文容许，不列实质增译。
2. 随机片段、一维/二维、跨循环及模型名称对应。
3. 句法自然。
4. strong/low对应较强/较低，属于非定量程度的常见译法，不据此指认夸大。
5. JES full.txt 79–103支持CNN局部核/池化；其中Qian结果措辞与本中文不同，没有照搬范文。

处置：无须修改。

### C01-B08｜chapter01.tex:15

源位置：source-zh/chapters/chapter01.tex:15；英文位置：chapters/chapter01.tex:15。

中文原文：

```tex
然而，传统CNN的单层卷积受局部感受野限制，相距较远的特征通常需要经过多层卷积才能融合\cite{ref31}。为建立这些远距离联系，RNN通过隐藏状态将历史信息传递到后续时间步；其变体长短期记忆网络（LSTM）和门控循环单元（GRU）进一步利用门控机制选择性地保留和更新历史信息，以捕捉长期依赖\cite{ref14}。为同时利用局部特征与历史信息，研究者将CNN与循环网络相结合。例如，Xu等人\cite{ref41}将CNN提取的特征输入LSTM，利用LSTM的时序记忆能力估计SOH。Tian等人\cite{ref42}在CNN与BiLSTM的组合中进一步引入注意力机制，构建了CNN-BiLSTM-AM预测模型。Zheng等人\cite{ref33}则采用CNN-GRU，根据随机充电过程中的电压、电流和温度曲线片段估计SOH。尽管如此，这类模型中的隐藏状态仍需按时间步串行更新，限制了训练和推理过程中的并行计算\cite{ref31}。
```

当前英文：

```tex
However, a single convolutional layer in a traditional CNN is limited by its local receptive field, and multiple convolutional layers are generally needed to fuse features that are far apart\cite{ref31}. To establish these long-range connections, RNNs pass historical information to subsequent time steps through hidden states. Their variants, long short-term memory (LSTM) and gated recurrent unit (GRU) networks, further use gating mechanisms to selectively retain and update historical information to capture long-term dependencies\cite{ref14}. Researchers have combined CNNs with recurrent networks to use both local features and historical information. For example, Xu et al.\cite{ref41} fed CNN-extracted features into an LSTM and used its temporal memory to estimate SOH. Tian et al.\cite{ref42} further introduced an attention mechanism into a CNN-BiLSTM combination to develop a CNN-BiLSTM-AM prediction model. Zheng et al.\cite{ref33} used a CNN-GRU to estimate SOH from voltage, current, and temperature curve segments during random charging processes. Nevertheless, the hidden states in these models still need to be updated sequentially over time, limiting parallel computation during training and inference\cite{ref31}.
```

中文回译：

然而，传统CNN中的单个卷积层受局部感受野限制，相距较远的特征通常需要多个卷积层才能融合。为建立这些长距离联系，RNN通过隐藏状态把历史信息传递至后续时间步。其变体长短期记忆（LSTM）和门控循环单元（GRU）网络进一步利用门控机制有选择地保留和更新历史信息，以捕获长期依赖。研究者将CNN与循环网络结合以同时利用局部特征和历史信息。例如，Xu等人将CNN提取的特征输入LSTM，并利用其时间记忆估计SOH。Tian等人进一步把注意力机制引入CNN-BiLSTM组合，开发了CNN-BiLSTM-AM预测模型。Zheng等人使用CNN-GRU，根据随机充电过程中的电压、电流和温度曲线片段估计SOH。尽管如此，这些模型的隐藏状态仍须随时间按顺序更新，限制了训练和推理时的并行计算。

五项审查：

1. 单层、通常、多层融合、RNN门控、三研究及训练/推理串行限制齐全。
2. single、generally、hidden states及LSTM/GRU角色准确。
3. multiple convolutional layers are generally needed to fuse features that are far apart句法自然。最终文件校验时此句已与初读版本不同；本报告对齐校验时现稿，该变化非本审查agent实施。
4. 限制未扩大到CNN完全不能处理长序列。
5. B3及E5给局部感受野、RNN串行处理对应语境。

处置：无须修改。

### C01-B09｜chapter01.tex:17

源位置：source-zh/chapters/chapter01.tex:17；英文位置：chapters/chapter01.tex:17。

中文原文：

```tex
为解决这一问题，Vaswani等人\cite{ref34}提出了Transformer。该模型避免循环递推，利用自注意力直接建立不同序列位置之间的联系，在捕捉长程依赖的同时支持并行计算。例如，Park和Kim\cite{ref38}采用物理先验引导的Transformer估计电池长期SOH；Chen等人\cite{ref37}则在视觉Transformer中加入维度变换层等结构，使其适用于电池SOH估计。研究者还将Transformer与卷积或循环网络相结合，以提高预测精度。Gu等人\cite{ref35}采用CNN提取局部特征，并结合Transformer捕捉长程依赖。Jia等人\cite{ref32}将BiGRU与Transformer结合，实验表明该模型在所用电池数据上具有较好的预测精度、鲁棒性和泛化表现。Bai和Wang\cite{ref36}则提出卷积Transformer框架，从电压和电流信号中提取局部细节，并通过自注意力建立局部特征之间的全局联系。然而，现有方法多通过集成其他模块或模型提高Transformer的预测精度，这种性能提升往往以增加参数量和计算开销为代价\cite{ref31}。与此同时，标准自注意力的计算瓶颈依然存在：它需要计算所有序列位置之间的两两关系，时间和存储复杂度随序列长度$N$呈二次增长，即$O(N^2)$\cite{ref39,ref40}。这些计算与存储需求增加了模型在资源受限BMS中的在线应用难度\cite{ref31}。
```

当前英文：

```tex
To address this issue, Vaswani et al.\cite{ref34} proposed the Transformer. This model avoids recurrence and uses self-attention to directly connect different sequence positions, capturing long-range dependencies while supporting parallel computation. For example, Park and Kim\cite{ref38} used a Transformer guided by physical priors to estimate long-term battery SOH, while Chen et al.\cite{ref37} added structures such as dimension-transformation layers to a vision Transformer to adapt it to battery SOH estimation. Researchers have also combined Transformers with convolutional or recurrent networks to improve prediction accuracy. Gu et al.\cite{ref35} used a CNN to extract local features and a Transformer to capture long-range dependencies. Jia et al.\cite{ref32} combined a BiGRU with a Transformer, and their experiments showed good prediction accuracy, robustness, and generalization on the battery data used. Bai and Wang\cite{ref36} proposed a convolutional Transformer framework that extracts local details from voltage and current signals and uses self-attention to establish global connections among local features. However, existing methods often improve Transformer prediction accuracy by integrating other modules or models, and these gains usually come at the cost of more parameters and higher computational overhead\cite{ref31}. Meanwhile, the computational bottleneck of standard self-attention remains: it computes pairwise relationships among all sequence positions, with time and memory complexity growing quadratically with sequence length $N$, namely $O(N^2)$\cite{ref39,ref40}. These computational and storage requirements make online application in resource-limited BMS more difficult\cite{ref31}.
```

中文回译：

为解决这一问题，Vaswani等人提出了Transformer。该模型避免递归，利用自注意力直接连接不同序列位置，在捕获长程依赖的同时支持并行计算。例如，Park和Kim使用由物理先验引导的Transformer估计电池长期SOH，而Chen等人向视觉Transformer加入维度变换层等结构，使其适用于电池SOH估计。研究者还将Transformer与卷积或循环网络结合以改善预测精度。Gu等人使用CNN提取局部特征，并使用Transformer捕获长程依赖。Jia等人将BiGRU与Transformer结合，其实验显示模型在所用电池数据上具有良好的预测精度、鲁棒性和泛化能力。Bai和Wang提出一种卷积Transformer框架，从电压和电流信号中提取局部细节，并用自注意力建立局部特征之间的全局联系。然而，现有方法往往通过集成其他模块或模型提高Transformer预测精度，这些收益通常以更多参数和更高计算开销为代价。同时，标准自注意力的计算瓶颈依然存在：它计算所有序列位置之间的两两关系，其时间和内存复杂度随序列长度N呈二次增长，即O(N²)。这些计算和存储需求使模型在资源受限BMS中的在线应用更加困难。

五项审查：

1. 模型发展、例子、所用电池数据限定及二次瓶颈完整。
2. N和O(N²)保留；time and memory complexity对应理论存储，非权重文件大小。
3. 并列综述较长但顺序清晰；dimension-transformation为具体结构适配。
4. on the battery data used、often、usually均保留；未加所有数据最优。
5. B3与E5对长程依赖、混合模型和二次开销对应；不继承rank collapse这一中文未提机制。

处置：无须修改。

### C01-B10｜chapter01.tex:19

源位置：source-zh/chapters/chapter01.tex:19；英文位置：chapters/chapter01.tex:19。

中文原文：

```tex
除了预测模型，健康指标的提取与选择对SOH估计的准确性同样至关重要。这些指标主要从电池循环过程中的电压、电流、温度、时间和内阻等运行数据及其衍生曲线中提取\cite{ref47,ref48,ref49,ref50}。其中，部分内阻指标需要通过阻抗谱测试获得，测试过程耗时且依赖专用仪器\cite{ref64}。温度指标虽然包含电池退化信息，但也会受到环境温度和充放电倍率的影响，其在不同工况下的稳定性受到限制\cite{ref64}。增量容量曲线能够反映电池老化引起的电压平台变化，但计算该曲线需要进行微分运算，容易放大采样噪声。为获得可靠的曲线特征，通常需要进行平滑处理\cite{ref28,ref50}。例如，Wen等人\cite{ref50}从平滑后的增量容量曲线中提取峰值、峰位和峰形斜率等候选特征，并根据相关性分析选择峰值作为BP神经网络输入。
```

当前英文：

```tex
In addition to the prediction model, health indicator extraction and selection are crucial for accurate SOH estimation. These indicators are mainly extracted from operating data, including voltage, current, temperature, time, and internal resistance during battery cycling, and their derived curves\cite{ref47,ref48,ref49,ref50}. Some internal-resistance indicators require impedance spectroscopy, which is time-consuming and depends on specialized instruments\cite{ref64}. Although temperature indicators contain battery degradation information, they are also affected by ambient temperature and charge-discharge rate, limiting their stability across operating conditions\cite{ref64}. Incremental capacity curves reflect changes in voltage plateaus caused by battery aging, but their calculation requires differentiation, which can amplify sampling noise. Smoothing is therefore usually needed to obtain reliable curve features\cite{ref28,ref50}. For example, Wen et al.\cite{ref50} extracted candidate features such as peak values, peak positions, and peak-shape slopes from smoothed incremental capacity curves and selected the peak value as the input to a BP neural network based on correlation analysis.
```

中文回译：

除预测模型外，健康指标的提取和筛选对准确估计SOH也至关重要。这些指标主要从运行数据及其衍生曲线中提取，包括电池循环过程中的电压、电流、温度、时间和内阻。一些内阻指标需要阻抗谱测试，而该测试耗时且依赖专用仪器。温度指标虽然包含电池退化信息，也会受到环境温度和充放电倍率的影响，从而限制其跨运行条件的稳定性。增量容量曲线反映电池老化所引起的电压平台变化，但计算这些曲线需要微分，这可能放大采样噪声。因此，通常需要平滑处理才能获得可靠的曲线特征。例如，Wen等人从平滑后的增量容量曲线提取峰值、峰位和峰形斜率等候选特征，并依据相关性分析选择峰值作为BP神经网络的输入。

五项审查：

1. 来源信号、部分内阻、温度干扰、微分噪声、平滑及峰筛选完整。
2. 峰值与峰位分清；温度/倍率限制保留；BP未擅自更名其他网络。
3. 第二句插入including稍长，仍可明确their指operating data；不必调整。
4. some、can、usually保留，can amplify略弱于容易放大但未改变机理方向。
5. J2完整HI段匹配；E4微分分析段支持噪声和平滑语境，范文更重的预处理负担未引入。

处置：无须修改。

### C01-B11｜chapter01.tex:21

源位置：source-zh/chapters/chapter01.tex:21；英文位置：chapters/chapter01.tex:21。

中文原文：

```tex
相比之下，时间类健康指标无需微分处理，提取过程更为简单。其中，恒流充电时间（CCCT）可由所选电压区间两端对应时刻的差值获得。Richardson等人\cite{ref28}利用恒流充电曲线中不同电压区间的时间特征估计电池容量，Lin等人\cite{ref63}则将CCCT作为随机森林的输入，估计电池SOH。由于时间特征与容量之间的相关性会受到所选电压区间影响，相关研究通常需要进一步确定合适的特征提取区间。Tian等人\cite{ref51}通过优化充电电压区间，提高所提取健康指标与容量之间的相关性。在充电时间特征的区间选择中，Li等人\cite{ref31}逐步缩小电压窗口，并利用组内多节电池的皮尔逊相关系数（PCC）评价候选区间，以从更短的充电片段中提取与SOH高度相关的时间特征。
```

当前英文：

```tex
In contrast, time-based health indicators do not require differentiation and are simpler to extract. Constant current charge time (CCCT) is obtained as the difference between the times corresponding to the two endpoints of a selected voltage interval. Richardson et al.\cite{ref28} used time features from different voltage intervals of constant-current charging curves to estimate battery capacity, while Lin et al.\cite{ref63} used CCCT as the input to a random forest to estimate battery SOH. Because the correlation between time features and capacity depends on the selected voltage interval, these studies generally need to further identify a suitable feature extraction interval. Tian et al.\cite{ref51} optimized the charging voltage interval to improve the correlation between the extracted health indicator and capacity. For charging-time feature extraction, Li et al.\cite{ref31} progressively narrowed the voltage window and used the Pearson correlation coefficient (PCC) across multiple cells within a group to evaluate candidate intervals, allowing highly SOH-correlated time features to be extracted from shorter charging segments.
```

中文回译：

相比之下，时间类健康指标无需微分，提取更简单。恒流充电时间（CCCT）由选定电压区间两个端点所对应时刻的差得到。Richardson等人使用恒流充电曲线中不同电压区间的时间特征估计电池容量，而Lin等人将CCCT输入随机森林以估计电池SOH。由于时间特征和容量之间的相关性依赖选定的电压区间，这些研究通常需要进一步识别合适的特征提取区间。Tian等人优化充电电压区间，以提高提取的健康指标与容量的相关性。在充电时间特征提取方面，Li等人逐步缩小电压窗口，并利用组内多节电池上的皮尔逊相关系数（PCC）评价候选区间，从而可从更短的充电片段提取与SOH高度相关的时间特征。

五项审查：

1. 区间端点差、三项研究和逐步缩窗均对应；“区间选择中”被概括成feature extraction，但后句完整说明窗口选择，无实质丢失。
2. CCCT、PCC及组内多电池保留。
3. highly SOH-correlated不如strongly correlated with SOH常见，能清楚理解；非必改。
4. generally保留通常，highly对应高度。
5. J2时间HI段与BMS HI窗口语境一致；本稿CCCT为时长，未混同EAI面积。

处置：无须修改。

### C01-B12｜chapter01.tex:23

源位置：source-zh/chapters/chapter01.tex:23；英文位置：chapters/chapter01.tex:23。

中文原文：

```tex
不同运行数据及其衍生曲线能够从不同方面反映电池退化。为更充分地利用这些信息，一些研究从多种运行信号中构建候选健康指标，并进一步优化模型输入。例如，Dai等人\cite{ref48}从电压、电流、温度以及增量容量、差分热伏安曲线中提取健康指标，并计算这些指标在各循环下的均值、中位数等统计特征，随后通过比较不同统计特征组合的估计误差确定用于SOH估计的输入。Lin等人\cite{ref55}从电学、热学和电化学等角度构建多类特征，采用主成分分析进行降维，并利用模拟退火算法优化保留的特征维数，从而减少冗余并改善SOH估计表现。
```

当前英文：

```tex
Different operating data and their derived curves reflect different aspects of battery degradation. To make fuller use of this information, some studies construct candidate health indicators from multiple operating signals and further optimize model inputs. For example, Dai et al.\cite{ref48} extracted health indicators from voltage, current, temperature, incremental capacity, and differential thermal voltammetry curves and calculated statistical features such as their means and medians in each cycle. They then compared estimation errors for different combinations of statistical features to determine the inputs for SOH estimation. Lin et al.\cite{ref55} constructed multiple types of electrical, thermal, and electrochemical features, applied principal component analysis for dimensionality reduction, and used simulated annealing to optimize the retained feature dimension, thereby reducing redundancy and improving SOH estimation performance.
```

中文回译：

不同运行数据及其衍生曲线反映电池退化的不同方面。为更充分地使用这些信息，一些研究从多种运行信号构建候选健康指标，并进一步优化模型输入。例如，Dai等人从电压、电流、温度、增量容量和差分热伏安曲线中提取健康指标，并计算每个循环中这些指标的均值、中位数等统计特征。随后，他们比较不同统计特征组合的估计误差，以确定SOH估计输入。Lin等人构建多类电学、热学和电化学特征，使用主成分分析降维，并用模拟退火优化保留的特征维度，从而减少冗余并改善SOH估计性能。

五项审查：

1. 多源信息、均值中位数、按循环、组合比较、PCA及模拟退火均对应。
2. differential thermal voltammetry对应此处差分热伏安；不机械替代为第二章不同中文称谓。
3. means/medians的their指HIs，清楚；dimension表示保留维数可接受。
4. 未增添统计显著性或最优保证。
5. J2/J3支持多源HI和去冗余关系；Dai/Lin具体研究细节属本文所引文献语境适配，三篇范文不替代事实证据。

处置：无须修改。

### C01-B13｜chapter01.tex:25

源位置：source-zh/chapters/chapter01.tex:25；英文位置：chapters/chapter01.tex:25。

中文原文：

```tex
单一健康指标所反映的退化信息相对有限，多源特征能够从不同方面补充电池退化的描述。然而，增加候选指标并不必然提高估计精度，表征能力较弱、跨电池表现不稳定或相互重复的指标，可能限制多源信息的有效利用，并增加模型的学习负担。因此，有必要设计相应的健康指标筛选算法，将SOH相关性、跨电池表现与冗余关系纳入统一的评价与筛选过程，保留具有稳定表征能力的指标，减少弱相关和重复信息的输入，以帮助模型更有效地学习电池退化规律。
```

当前英文：

```tex
A single health indicator contains relatively limited degradation information, whereas multi-source features can describe complementary aspects of battery degradation. However, increasing the number of candidate indicators does not necessarily improve estimation accuracy. Indicators with weak representational capability, unstable cross-cell performance, or redundant information may limit the effective use of multi-source information and increase the learning burden on the model. It is therefore necessary to develop a health indicator selection algorithm that incorporates SOH correlation, cross-cell performance, and redundancy into a unified evaluation and selection process. Retaining indicators with stable representational capability and reducing inputs that are weakly correlated with SOH or redundant can help the model learn battery degradation patterns more effectively.
```

中文回译：

单一健康指标包含的退化信息相对有限，而多源特征可以描述电池退化中互补的方面。然而，增加候选指标的数量并不一定提高估计精度。表征能力较弱、跨电池表现不稳定或信息冗余的指标，可能限制多源信息的有效使用并增加模型的学习负担。因此，有必要开发健康指标筛选算法，将SOH相关性、跨电池表现及冗余纳入统一的评价筛选过程。保留具有稳定表征能力的指标并减少与SOH弱相关或冗余的输入，可以帮助模型更有效地学习电池退化模式。

五项审查：

1. 单一有限、多源互补、非必然、可能不利和统一筛选均保留。
2. with SOH为弱相关补足对象，与本段SOH相关性语境吻合。
3. learning burden、learn…patterns自然可接受。
4. does not necessarily、may、can均保留，没有将互补性写成无条件性能增益。
5. J3相关性和冗余语境匹配；BMS weakly correlated HIs未直接照搬成对象不明。

处置：无须修改。

### C01-B14｜chapter01.tex:27

源位置：source-zh/chapters/chapter01.tex:27；英文位置：chapters/chapter01.tex:27。

中文原文：

```tex
现有SOH估计方法之间的比较总结于\Cref{tab:soh-method-comparison}。具体而言，重点考察各方法是否充分利用电池运行数据中的退化信息，是否采用有效的健康指标提取与选择策略，是否通过针对性的模型设计兼顾估计性能与计算效率，以及是否开展模型复杂度评价。在健康指标方面，不同电池在材料体系和运行条件上存在差异，所选指标能否在不同电池间保持稳定的退化表征能力仍需进一步关注。在模型方面，除估计性能外，模型复杂度同样直接关系到实际部署。近年来，深度模型架构发展的一个显著趋势是通过增加网络深度、扩大模型规模或引入更复杂的特征交互结构来增强表征能力。这些设计有助于提升模型对复杂退化规律的建模能力，但通常也伴随着更高的参数量、计算开销和存储需求。因此，面向计算能力、存储空间和实时性受到限制的BMS，SOH估计模型需要在保持有效表征能力的同时控制模型规模与资源开销，进一步向紧凑化和高效化方向发展。
```

当前英文：

```tex
A comparison of existing SOH estimation methods is summarized in \Cref{tab:soh-method-comparison}. Specifically, the comparison examines whether each method fully uses degradation information in battery operating data, employs effective health indicator extraction and selection strategies, balances estimation performance and computational efficiency through targeted model design, and evaluates model complexity. For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention. For models, complexity is directly related to practical deployment, in addition to estimation performance. In recent years, a notable trend in deep model design has been to improve representational capability by increasing network depth, enlarging model size, or introducing more complex feature interactions. These designs help models capture complex degradation patterns but usually require more parameters, computation, and storage. Therefore, for BMS with limited computing power and storage space and strict real-time requirements, SOH estimation models need to control model size and resource overhead while retaining effective representational capability, moving toward more compact and efficient designs.
```

中文回译：

现有SOH估计方法的比较汇总于相应表中。具体而言，比较考察各方法是否充分利用电池运行数据中的退化信息，是否采用有效的健康指标提取和筛选策略，是否通过有针对性的模型设计兼顾估计性能与计算效率，以及是否评价模型复杂度。对于健康指标，电池材料和运行条件的差异意味着其退化表征在不同电池间的稳定性需要进一步关注。对于模型，除估计性能外，复杂度也直接关系到实际部署。近年来，深度模型设计的一个明显趋势是通过加深网络、扩大模型规模或引入更复杂的特征交互来提高表征能力。这些设计有助于模型捕获复杂退化模式，但通常需要更多参数、计算和存储。因此，对于计算能力和存储空间有限、实时要求严格的BMS，SOH估计模型需要在保留有效表征能力的同时控制模型规模和资源开销，朝更紧凑、更高效的设计发展。

五项审查：

1. 四项比较维度、材料工况差异、复杂化趋势和BMS需求完整。
2. 计算、存储、模型规模未互换；实时性受到限制译strict real-time requirements符合语境。
3. their degradation representations名词串略密，但指HIs表示退化的能力可由上下文恢复，属可选清晰化。
4. notable译显著趋势不引入统计检验；usually保留通常。
5. JES full.txt 314–322比较段及B2、E4模型开销段功能对应；以本文四维比较为准。

处置：无强制修改；可选把the stability of their degradation representations across cells改为whether they can consistently represent degradation across cells。

### C01-B15｜chapter01.tex:32

源位置：source-zh/chapters/chapter01.tex:32；英文位置：chapters/chapter01.tex:32。

中文原文：

```tex
\subsection{挑战分析与贡献}
```

当前英文：

```tex
\subsection{Challenges and contributions}
```

中文回译：

挑战与贡献

五项审查：

1. Challenges and contributions未显式译“分析”，但作为挑战分析小节惯用缩写不改变正文内容。
2. 无数字条件。
3. 自然标题。
4. 无夸大。
5. 标题常规适配。

处置：可保留；严格逐词时用Analysis of challenges and contributions，但不作为实质错误。

### C01-B16｜chapter01.tex:34

源位置：source-zh/chapters/chapter01.tex:34；英文位置：chapters/chapter01.tex:34。

中文原文：

```tex
现有方法面临的主要挑战可归纳为以下三点。
```

当前英文：

```tex
The main challenges faced by existing methods can be summarized as follows.
```

中文回译：

现有方法面临的主要挑战可概括如下。

五项审查：

1. 漏掉显式数量“三点”；下列(1)–(3)可恢复信息，因此影响低，但不满足严格逐义保留。
2. three缺失。
3. 句法自然。
4. 无夸大。
5. BMS引出挑战有Three main problems；无需照其problem措辞。

处置：建议：The main challenges faced by existing methods can be summarized in the following three points.

### C01-B17｜chapter01.tex:36

源位置：source-zh/chapters/chapter01.tex:36；英文位置：chapters/chapter01.tex:36。

中文原文：

```tex
（1）\textbf{健康指标的跨电池稳定性问题。} 从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。PCC和斯皮尔曼相关系数（SCC）分别用于评价线性关联与单调关联，仅采用其中一种，难以同时考察这两方面的表现。此外，即使多个指标均与SOH具有较强关联，它们之间仍可能包含重复信息。因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。
```

当前英文：

```tex
(1) \textbf{Cross-cell stability of health indicators.} Raw data collected from multiple sensors contain diverse features related to degradation. The relationship between a candidate health indicator and SOH may vary across cells, and an indicator that performs well on one cell may not retain the same representational capability on others. PCC and the Spearman correlation coefficient (SCC) evaluate linear and monotonic relationships, respectively; using only one makes it difficult to assess both aspects. Moreover, even indicators strongly associated with SOH may contain redundant information. Model input selection therefore needs to consider both correlations across cells and redundancy among indicators to reduce its dependence on the performance of a single cell.
```

中文回译：

（1）健康指标的跨电池稳定性。从多个传感器收集的原始数据包含多样的退化相关特征。候选健康指标与SOH的关系可能随电池而变化，在一个电池上表现良好的指标，在其他电池上未必保有同样的表征能力。PCC与斯皮尔曼相关系数（SCC）分别评价线性关系和单调关系；仅使用其中一种很难同时评估这两个方面。此外，即使与SOH强关联的指标也可能包含冗余信息。因此，模型输入筛选需要同时考虑不同电池上的相关性以及指标之间的冗余，以降低其对单个电池表现的依赖。

五项审查：

1. 跨电池不确定性、双相关分工及冗余完整；其末its可回指model input selection，基本清楚但未明确“选择结果”。
2. PCC线性、SCC单调对应；未把指标间关系混作HI–SOH关系。
3. its dependence有轻微指代模糊，可明确为the selection results。
4. may vary、may not均保留；strongly对应较强，程度常规适配。
5. J3提供相关类型/冗余词；评估对象限定在本文电池。

处置：可选将to reduce its dependence on…改为so that the selection results depend less on…。非确定误译。

### C01-B18｜chapter01.tex:38

源位置：source-zh/chapters/chapter01.tex:38；英文位置：chapters/chapter01.tex:38。

中文原文：

```tex
（2）\textbf{局部与长期退化信息的融合问题。} 随着循环推进，电池容量整体呈下降趋势，并伴随相邻循环的波动和局部容量恢复。局部特征能够反映短期变化，但对长期衰减趋势的把握还需要建立跨循环联系；在聚合跨循环信息时，也需要保留局部退化细节，避免短期变化被弱化。因此，模型不仅需要提取不同时间尺度的退化特征，还需要使局部变化与长期趋势相互补充，以提高SOH估计的准确性。
```

当前英文：

```tex
(2) \textbf{Fusion of local and long-term degradation information.} As cycling progresses, battery capacity generally declines, with fluctuations between neighboring cycles and local capacity recovery. Local features reflect short-term changes, but capturing long-term capacity fade trends also requires connections across cycles. When aggregating information across cycles, local degradation details must be retained so that short-term changes are not weakened. Therefore, the model needs not only to extract degradation features at different time scales but also to make local variations and long-term trends complement each other to improve SOH estimation accuracy.
```

中文回译：

（2）局部与长期退化信息的融合。随着循环推进，电池容量一般下降，同时出现相邻循环间的波动和局部容量恢复。局部特征反映短期变化，但捕获长期容量衰减趋势还需要建立跨循环联系。聚合跨循环信息时，必须保留局部退化细节，使短期变化不被削弱。因此，模型不仅需要提取不同时间尺度的退化特征，还需要让局部变化和长期趋势互为补充，以提高SOH估计精度。

五项审查：

1. 跨循环、短期/长期、信息保留和互补均对应。
2. generally declines能表达一般下降，但“整体呈下降趋势”更准确为an overall downward trend；当前有轻微从趋势层级变成频率的一义差。
3. 整体自然；must be retained比也需要更强一些，属于必要性叙述，非硬错。
4. 未增无条件精度保证。
5. JES full.txt 283–286与B3/E5支持长期与局部信息；本文与范文恢复现象位置不同，已作适配。

处置：可选将battery capacity generally declines改为battery capacity follows an overall downward trend；其余保留。

### C01-B19｜chapter01.tex:40

源位置：source-zh/chapters/chapter01.tex:40；英文位置：chapters/chapter01.tex:40。

中文原文：

```tex
（3）\textbf{计算复杂度限制。} 许多现有深度学习模型通过增加网络深度或组合不同网络结构提高SOH估计精度。这些方法增加了模型参数和计算操作。循环结构需要按时间步依次计算，标准自注意力需要计算所有序列位置之间的两两关系，其时间和存储开销随序列长度呈二次增长。这些开销加重了资源受限BMS的运行负担，限制了在线SOH估计模型的部署。
```

当前英文：

```tex
(3) \textbf{Computational complexity limitations.} Many existing deep learning models improve SOH estimation accuracy by increasing network depth or combining different network structures. These approaches increase the number of model parameters and computational operations. Recurrent structures require sequential computation over time steps, while standard self-attention computes pairwise relationships among all sequence positions, with time and memory overhead growing quadratically with sequence length. These costs increase the operating burden on resource-limited BMS and limit the deployment of online SOH estimation models.
```

中文回译：

（3）计算复杂度限制。许多现有深度学习模型通过加深网络或组合不同网络结构提高SOH估计精度。这些方法增加模型参数和计算操作的数量。循环结构需要沿时间步顺序计算，而标准自注意力计算所有序列位置间的两两关系，时间与内存开销随序列长度呈二次增长。这些成本增加资源受限BMS的运行负担，并限制在线SOH估计模型的部署。

五项审查：

1. 完整对应。
2. number of model parameters为本日已批准修订；理论内存开销不是文件存储。
3. 参数与计算操作数量表达准确。
4. many保留许多；limit deployment对应限制而非完全不可部署。
5. BMS挑战与E5串行/二次复杂度功能对应。

处置：无须修改。

### C01-B20｜chapter01.tex:42

源位置：source-zh/chapters/chapter01.tex:42；英文位置：chapters/chapter01.tex:42。

中文原文：

```tex
为应对上述挑战，本文提出一种以MS-AgentNet为核心的锂离子电池SOH估计框架。该框架从健康指标构建和轻量模型设计两个层面展开，分别通过组级标定与筛选提高模型输入的跨电池稳定性，并以较低计算开销提取局部变化和长期趋势，主要贡献如下。
```

当前英文：

```tex
To address these challenges, this paper proposes a lithium-ion battery SOH estimation framework built around MS-AgentNet. The framework addresses health indicator construction and lightweight model design: group-level calibration and selection improve the cross-cell stability of model inputs, while local variations and long-term trends are extracted with low computational overhead. The main contributions are as follows.
```

中文回译：

为应对这些挑战，本文提出一种以MS-AgentNet为核心的锂离子电池SOH估计框架。框架涉及健康指标构建和轻量化模型设计：组级标定与筛选提高模型输入的跨电池稳定性，同时以低计算开销提取局部变化和长期趋势。主要贡献如下。

五项审查：

1. 两层设计、对应作用、主要贡献均保留。
2. group-level calibration/selection为本文算法层级适配。
3. 框架主语与操作关联清楚。
4. low对应较低，可选relatively low，不判实质增强。
5. E1/E4轻量设计和J3指标筛选语境吻合。

处置：无须修改。

### C01-B21｜chapter01.tex:44

源位置：source-zh/chapters/chapter01.tex:44；英文位置：chapters/chapter01.tex:44。

中文原文：

```tex
（1）\textbf{提出多源健康指标提取与优化算法。} 该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，再以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余。利用MS-CCCT标定其中充电时间特征的电压窗口，再通过PCC/SCC双阈值与冗余约束筛选候选指标。统一的筛选规则为各数据集确定相应的健康指标组合，入选指标在同一数据集的其他电池上仍保持较强的线性和单调相关性。
```

当前英文：

```tex
(1) \textbf{A multi-source health indicator extraction and optimization algorithm is proposed.} The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators using correlations on the feature-development cells. MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators. The unified selection rules determine a corresponding health indicator combination for each dataset, and the selected indicators retain strong linear and monotonic correlations on other cells within the same dataset.
```

中文回译：

（1）提出一种多源健康指标提取与优化算法。该算法首先从充放电数据及其衍生曲线提取多类候选健康指标。然后，利用特征开发电池上的相关性，联合评价候选指标与SOH的关系以及指标之间的冗余。MS-CCCT标定充电时间特征的电压窗口，此后用PCC/SCC双阈值及冗余约束筛选候选指标。统一筛选规则为每个数据集确定相应的健康指标组合，选中指标在同一数据集的其他电池上仍保持强线性和单调相关性。

五项审查：

1. 提取→相关性评价→窗标定→筛选→同数据集其余电池结果均保留。
2. feature-development cells省略集合一词，但复数及方法节明确集合，未改变数据角色；与SOH的相关对象可由段内承接。
3. jointly evaluates A and B自然；correlations on…为本文角色适配。
4. strong对应较强可接受；只称same dataset other cells，无跨域偷换。
5. J3支持PCC/SCC与冗余；其全电池筛选协议未导入本文开发集合。

处置：无须修改。

### C01-B22｜chapter01.tex:46

源位置：source-zh/chapters/chapter01.tex:46；英文位置：chapters/chapter01.tex:46。

中文原文：

```tex
（2）\textbf{构建轻量级局部—全局网络MS-AgentNet。} 设计轻量级局部—全局融合注意力模块（SLFA），将小核深度可分离卷积与ReLU$^2$智能体注意力相结合，以较低的参数开销融合局部退化特征与长期依赖。所构建的注意力机制将计算复杂度由$O(N^2)$降低至$O(N)$。模型进一步引入大核深度可分离卷积，与小核卷积共同提取不同时间尺度的退化特征。上述设计将局部特征提取与全局信息交互整合于紧凑的网络结构中，在提高SOH估计精度的同时降低了计算与存储开销。
```

当前英文：

```tex
(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} A Slim Local-Global Fusion Attention (SLFA) module combines small-kernel depthwise separable convolutions with ReLU$^2$ agent attention to fuse local degradation features and long-term dependencies with low parameter overhead. The attention mechanism reduces computational complexity from $O(N^2)$ to $O(N)$. Large-kernel depthwise separable convolutions are further introduced to extract degradation features at different time scales together with small-kernel convolutions. These designs integrate local feature extraction and global information interaction into a compact network structure, improving SOH estimation accuracy while reducing computational and storage overhead.
```

中文回译：

（2）构建轻量化局部—全局网络MS-AgentNet。轻量级局部—全局融合注意力（SLFA）模块结合小核深度可分离卷积和ReLU²智能体注意力，以低参数开销融合局部退化特征和长期依赖。该注意力机制将计算复杂度从O(N²)降至O(N)。进一步引入大核深度可分离卷积，与小核卷积共同提取不同时间尺度的退化特征。这些设计把局部特征提取与全局信息交互整合到紧凑的网络结构中，在提高SOH估计精度的同时减少计算和存储开销。

五项审查：

1. 结构、模块融合、多尺度和复杂度变化完整。
2. SLFA全称来自中文第三章明确英文名，为跨章一致；long-term dependencies保留本段长期，不强换摘要长程。
3. 常用combines/fuse/extract/integrate，无明显直译硬伤。
4. 改善/降低本来是源稿断言，未升级证明；低参数开销属既有表达。
5. B1对卷积/融合词适合；E1线性复杂度适合，RAA机制和Slim专名为本文特有。

处置：无须修改。

### C01-B23｜chapter01.tex:48

源位置：source-zh/chapters/chapter01.tex:48；英文位置：chapters/chapter01.tex:48。

中文原文：

```tex
（3）\textbf{开展多数据集综合验证。} 在具有不同材料、容量和充放电协议的多个公开数据集上开展实验，并结合模块消融与复杂度分析，综合评估所提方法的估计精度、计算效率及跨电池泛化能力。进一步通过跨数据集迁移实验考察模型的跨域适应能力。结果表明，所提模型在保持较高SOH估计精度的同时，具有较低的计算量和存储开销。
```

当前英文：

```tex
(3) \textbf{Comprehensive validation is conducted on multiple datasets.} Experiments on multiple public datasets with different battery materials, capacities, and charge-discharge protocols, together with module ablation and complexity analysis, jointly evaluate the estimation accuracy, computational efficiency, and cross-cell generalization of the proposed method. Cross-dataset transfer experiments further examine the model's cross-domain adaptation capability. The results show that the proposed model maintains high SOH estimation accuracy with low computational and storage overhead.
```

中文回译：

（3）在多个数据集上开展综合验证。在具有不同电池材料、容量和充放电协议的多个公开数据集上的实验，结合模块消融与复杂度分析，共同评价所提方法的估计精度、计算效率和跨电池泛化能力。跨数据集迁移实验进一步考察模型的跨域适应能力。结果表明，所提模型以低计算和存储开销保持高SOH估计精度。

五项审查：

1. 验证范围、消融、复杂度、跨电池与跨域适应及资源结论完整。
2. 不同材料/容量/协议、cross-cell generalization与cross-domain adaptation区分准确。
3. Experiments…together with…jointly evaluate有轻微堆叠但语法成立；可保留。
4. high/low表达较高/较低的绝对形容，语境对比可理解；不列硬错。
5. JES full.txt 307–313验证范围匹配，轻量资源结论借E1对应词；没有借入RUL/MCU证据。

处置：无须修改。

## 发现汇总与优先级

- 低影响明确漏译：C01-B16（原文件34行）引出句遗漏“三点”。下方三条仍完整，建议补three。
- 轻微情态范围歧义：C01-B05（9行）may可能同时限定估计精度与依赖关系，建议明确their accuracy depends on…。
- 已批准译文中的可选限定恢复：ABS-P01末句overall目前只直接修饰performance，中文“总体上”和“综合”两层意思可用generally…overall显式保留。不得将此直接判为普遍优越误译。
- 可选精确化：C01-B18（38行）generally declines与“整体下降趋势”存在频率/整体走势侧重差异；C01-B17（36行）its可明确为selection results；C01-B14（27行）退化表征名词串可更清楚。以上均未达到确定技术误译。
- 不列新错误：many为已批准新增；resource-consuming有BMS同语境原文；low/strong/high对应较低/较强/较高的多数实例有清楚上下文，不机械升级为夸大；章内标题省略“分析”属常见简写。
- 已知原中文边界：新能源交通的行业范围仍未冻结；现有描述译法已批准，不能未经判断改成更窄的电动交通。

范围结论：本部分未发现数字、模型名单、核心技术操作或跨数据集/跨电池概念的确定误译。上述结论只限本报告25块，不意味着全篇及图表已无问题。所有修改均为提议，正文与source-zh未改。
