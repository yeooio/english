# 全篇反向回译审查：第二、三章分册

日期：2026-09-13。审查者：并行方法审查 agent。对象为当前磁盘文件，精确原文和译文均直接装配自文件。本册覆盖第二章50个可见文字块、第三章70个可见文字块（包括标题、步骤、正文和公式说明），另逐项比较34个独立公式块。一个源正文自然段对应一个回译自然段。图表的外部input文件及栅格文字由主审图表分册覆盖，本册不将其计算为已核查图像。

回译按英文实际表达给出，审查者同时接触中英文，因此不称盲回译。为阅读方便，回译中公式符号使用可读转写，图表引用用中文名称；精确LaTeX、引用键及所有数学内容以并列原文和公式保护核验为准。回译不是替换中文原稿。

五项检查逐块记录：①漏译、增译、改义；②术语、数字、限定；③自然与简洁；④夸大、绝对化、复杂词；⑤三范文对应语境。正常英汉语序和必要分句不作为误译。新审查报告获得授权；本次未修改正文或source-zh。现有 approved-translations.md 及 language-fixes-batch-01.md 中的后续批准已考虑。

## 范文核对依据与边界

本轮实际读取三篇对应原始TXT相关段落，以下均为full.txt行号，不冒充新查PDF页码。既有逐句计数和主语/时态/功能记录见 [method-reference-analysis.md](D:/MS-AgentNet-English/translation-guides/method-reference-analysis.md)，本册复用该记录，未重做全文句子计数。

| 证据 | 短原词 | 助手中文释义与使用边界 |
|---|---|---|
| BMSFormer L275–283、L735–744 | a sliding window; true SOH; embedded in a high-dimensional space | 滑动窗口；真实SOH；嵌入高维空间。用于输入及标签，不继承其训练划分。 |
| BMSFormer L766–789 | computational cost; output channel | 计算成本；输出通道。适用于卷积说明，不为本文全部核尺寸提供无条件低成本保证。 |
| Engineering-AI L855–860、L875–884、L898–901、L923–927 | Dual-role local enhancement; locality bias; feature fusion stage; Global Aggregation | 双作用局部增强；局部性偏置；特征融合阶段；全局聚合。保留本文RAA、双智能体和残差位置，不继承范文机制主张。 |
| JESSOHRUL L1576–1590、L1634–1647、L1671–1680、L1822–1849 | peak value; monotonic relationship; retained HIs; feature diversity | 峰值；单调关系；保留的HI；特征多样性。本文HI编号、阈值、双电池及使用范围独立。 |

源稿事实优先于范文写法。第五项“适配”表示没有准确的范文完整对应，不等于英文错误；未从三范文继承RUL、硬件验证、单智能体或不同筛选阈值。

## 第2章逐块核对

### M02-001 — 标题含义

位置：[中文 L1](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:1)；[英文 L1](D:/MS-AgentNet-English/chapters/chapter02.tex:1)。

中文原文：

```latex
\subsection{健康状态估计框架概述}
```

当前英文：

```latex
\subsection{Overview of the SOH estimation framework}
```

中文回译：

SOH估计框架概述

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-002 — 容量保持率、当前/额定容量

位置：[中文 L3](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:3)；[英文 L3](D:/MS-AgentNet-English/chapters/chapter02.tex:3)。

中文原文：

```latex
为统一后续实验中的计算口径，SOH 按容量保持率进行计算，即电池当前可用容量与额定容量之比\cite{ref13,ref14}：
```

当前英文：

```latex
To use a consistent definition in the following experiments, SOH is calculated as capacity retention, namely the ratio of the current available capacity to the rated capacity\cite{ref13,ref14}:
```

中文回译：

为在后续实验中使用一致的定义，SOH按容量保持率计算，即当前可用容量与额定容量之比：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 容量保持率、当前/额定容量对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-003 — 两个容量符号定义

位置：[中文 L9](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:9)；[英文 L9](D:/MS-AgentNet-English/chapters/chapter02.tex:9)。

中文原文：

```latex
其中，$C_{\mathrm{current}}$ 和 $C_{\mathrm{rated}}$ 分别表示电池当前可用容量和额定容量。
```

当前英文：

```latex
where $C_{\mathrm{current}}$ and $C_{\mathrm{rated}}$ denote the current available capacity and rated capacity of the battery, respectively.
```

中文回译：

其中，C_current和C_rated分别表示电池的当前可用容量与额定容量。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 两个容量符号定义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-004 — 框架图引用

位置：[中文 L11](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:11)；[英文 L11](D:/MS-AgentNet-English/chapters/chapter02.tex:11)。

中文原文：

```latex
所提出的健康状态估计框架如\cref{fig:2-1}所示。
```

当前英文：

```latex
The proposed SOH estimation framework is shown in \cref{fig:2-1}.
```

中文回译：

所提出的SOH估计框架见图2-1。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 框架图引用对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-005 — 五类循环记录、充放电条件

位置：[中文 L13](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:13)；[英文 L13](D:/MS-AgentNet-English/chapters/chapter02.tex:13)。

中文原文：

```latex
（1）\textbf{数据获取。} 选取不同材料体系和运行工况下的公开电池老化数据，获取充放电过程中的电压、电流、温度、时间和容量等循环记录。
```

当前英文：

```latex
(1) \textbf{Data acquisition.} Public battery aging data covering different material systems and operating conditions are selected to obtain cycle records of voltage, current, temperature, time, and capacity during charging and discharging.
```

中文回译：

（1）数据获取。选择涵盖不同材料体系和运行条件的公开电池老化数据，以获取充放电过程中的电压、电流、温度、时间和容量循环记录。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 五类循环记录、充放电条件对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-006 — 提取→组级筛选→窗口→下一循环标签

位置：[中文 L15](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:15)；[英文 L15](D:/MS-AgentNet-English/chapters/chapter02.tex:15)。

中文原文：

```latex
（2）\textbf{系统化特征工程。} 采用所提出的多源健康指标提取与优化算法，从上述数据中构建多源候选健康指标池，并通过组级标定与筛选确定模型输入。随后，采用滑动窗口划分健康指标时间序列，将各窗口与其下一循环的 SOH 配对，形成输入样本及对应标签。
```

当前英文：

```latex
(2) \textbf{Systematic feature engineering.} The proposed multi-source health indicator extraction and optimization algorithm constructs a pool of multi-source candidate HIs from these data and determines the model inputs through group-level calibration and selection. A sliding window is then used to segment the HI time series. Each window is paired with the SOH of the next cycle to form an input sample and its label.
```

中文回译：

（2）系统化特征工程。所提出的多源健康指标提取与优化算法从这些数据中构建多源候选HI池，并通过组级标定与筛选确定模型输入。随后用滑动窗口划分HI时间序列。每个窗口与下一循环的SOH配对，构成输入样本及其标签。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 提取→组级筛选→窗口→下一循环标签对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-007 — 训练与配置电池角色

位置：[中文 L17](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:17)；[英文 L17](D:/MS-AgentNet-English/chapters/chapter02.tex:17)。

中文原文：

```latex
（3）\textbf{模型训练。} 将筛选后的健康指标样本输入 MS-AgentNet，在训练电池上完成模型参数学习，并根据配置电池上的估计表现确定模型配置。
```

当前英文：

```latex
(3) \textbf{Model training.} Samples of the selected HIs are fed into MS-AgentNet. Model parameters are learned on the training cell, and the model configuration is determined based on estimation performance on the configuration-selection cell.
```

中文回译：

（3）模型训练。将所选HI样本输入MS-AgentNet。在训练电池上学习模型参数，根据配置选择电池上的估计表现确定模型配置。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 训练与配置电池角色对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-008 — 直接应用、跨电池与跨域区分

位置：[中文 L19](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:19)；[英文 L19](D:/MS-AgentNet-English/chapters/chapter02.tex:19)。

中文原文：

```latex
（4）\textbf{性能评价。} 将训练后的模型直接用于相应数据集的其他电池，比较不同模型的 SOH 估计精度、跨电池泛化性能及计算与存储开销。进一步通过消融实验分析关键模块的作用，并通过跨数据集迁移实验考察模型的跨域适应能力。
```

当前英文：

```latex
(4) \textbf{Performance evaluation.} The trained model is directly applied to other cells in the corresponding dataset to compare the SOH estimation accuracy, cross-cell generalization performance, and computational and storage overhead of different models. Ablation studies are further conducted to analyze the roles of key modules, and cross-dataset transfer experiments are used to examine cross-domain adaptation.
```

中文回译：

（4）性能评价。将训练后的模型直接应用于相应数据集的其他电池，比较不同模型的SOH估计精度、跨电池泛化性能以及计算与存储开销。进一步开展消融研究分析关键模块的作用，并通过跨数据集迁移实验考察跨域适应。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 直接应用、跨电池与跨域区分对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §2.1 full.txt L275–283（窗口与下一步标签）及§3.1 L735–744（输入数据流）相应语境可用；容量定义、四步对象和训练/配置角色为本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-009 — 标题含义

位置：[中文 L21](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:21)；[英文 L21](D:/MS-AgentNet-English/chapters/chapter02.tex:21)。

中文原文：

```latex
\subsection{典型电池数据集}
```

当前英文：

```latex
\subsection{Typical battery datasets}
```

中文回译：

典型电池数据集

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-010 — 四数据集、三类外形、图面板

位置：[中文 L23](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:23)；[英文 L23](D:/MS-AgentNet-English/chapters/chapter02.tex:23)。

中文原文：

```latex
为考察所提方法在不同电池体系和运行条件下的泛化能力，选取 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四组公开电池老化数据开展实验。这些数据集涵盖软包、方形和圆柱形电池，在材料体系、标称容量及运行条件等方面存在明显差异，可为模型在不同电池退化场景下的评估提供具有多样性的实验数据。各数据集的主要特性汇总于\cref{tab:2-1}。\cref{fig:2-2}(a)--(d)展示了所选电池的容量衰减曲线，\cref{fig:2-2}(e)--(h)给出了各数据集中代表性电池在不同 SOH 水平下的充电电压曲线。各数据集的具体情况如下。
```

当前英文：

```latex
Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, are selected to examine the generalization capability of the proposed method across different battery systems and operating conditions. These datasets include pouch, prismatic, and cylindrical cells and differ considerably in material systems, nominal capacities, and operating conditions, providing diverse experimental data for model evaluation under different battery degradation scenarios. Their main characteristics are summarized in \cref{tab:2-1}. \cref{fig:2-2}(a)--(d) shows the capacity fade curves of the selected cells, and \cref{fig:2-2}(e)--(h) presents the charging voltage curves of a representative cell from each dataset at different SOH levels. Details of each dataset are given below.
```

中文回译：

选取Oxford、CALCE CS2、CALCE CX2和MIT/Severson四个公开电池老化数据集，以考察所提方法在不同电池体系和运行条件下的泛化能力。这些数据集包括软包、方形和圆柱电池，在材料体系、标称容量和运行条件方面存在较大差异，为模型在不同电池退化场景下的评价提供多样化实验数据。主要特性汇总于表2-1。图2-2(a)—(d)展示所选电池的容量衰减曲线，(e)—(h)展示每个数据集中一节代表性电池在不同SOH水平下的充电电压曲线。以下给出各数据集的详细情况。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 四数据集、三类外形、图面板对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 具体机构、型号、化学体系和实验协议是本文事实；三范文不作为这些事实的替代证据，本文所需适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-011 — 标题及数据集名称

位置：[中文 L27](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:27)；[英文 L27](D:/MS-AgentNet-English/chapters/chapter02.tex:27)。

中文原文：

```latex
\subsubsection*{（1）Oxford数据集}
```

当前英文：

```latex
\subsubsection*{(1) Oxford dataset}
```

中文回译：

（1）Oxford数据集

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题及数据集名称对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-012 — 8节、型号、材料、0.74 Ah/40 ℃/4.2 V/2.7 V

位置：[中文 L29](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:29)；[英文 L29](D:/MS-AgentNet-English/chapters/chapter02.tex:29)。

中文原文：

```latex
Oxford 数据集由牛津大学电池智能实验室提供，包含 8 节 Kokam SLPB533459H4 锂离子软包电池的老化数据，每节电池的标称容量为 0.74 Ah\cite{ref28}。该类电池的正极材料为镍钴酸锂（NCO）和钴酸锂（LCO）的混合物，负极材料为石墨\cite{ref60}。老化实验在 40 ℃ 的恒温环境下进行。电池采用恒流–恒压方式充电至 4.2 V，随后按照源自城市 ARTEMIS 工况的动态电流曲线进行放电，直至电压降至 2.7 V\cite{ref28,ref61}。实验纳入 Cell1–Cell8 共 8 节电池的循环老化记录。
```

当前英文：

```latex
The Oxford dataset is provided by the Battery Intelligence Laboratory at the University of Oxford and contains aging data from 8 Kokam SLPB533459H4 lithium-ion pouch cells, each with a nominal capacity of 0.74 Ah\cite{ref28}. The cathode is a blend of lithium nickel cobalt oxide (NCO) and lithium cobalt oxide (LCO), and the anode is graphite\cite{ref60}. The aging tests were conducted at a constant temperature of 40 ℃. The cells were charged to 4.2 V using a constant-current--constant-voltage protocol and then discharged following a dynamic current profile derived from the urban ARTEMIS drive cycle until the voltage reached 2.7 V\cite{ref28,ref61}. Aging records from cycling tests on all 8 cells, Cell1–Cell8, are included in the experiments.
```

中文回译：

Oxford数据集由牛津大学电池智能实验室提供，包含8节Kokam SLPB533459H4锂离子软包电池的老化数据，每节标称容量为0.74 Ah。正极为镍钴酸锂（NCO）与钴酸锂（LCO）的混合物，负极为石墨。老化试验在40 ℃恒温下进行。电池按恒流—恒压协议充至4.2 V，随后按源自城市ARTEMIS行驶工况的动态电流曲线放电，直到电压达到2.7 V。实验包含全部8节电池Cell1—Cell8循环试验的老化记录。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 正文数字与源稿一致；Oxford充电协议是否与数据集表一致由主报告另核，不依据范文静默改协议。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 具体机构、型号、化学体系和实验协议是本文事实；三范文不作为这些事实的替代证据，本文所需适配。 |

具体处理：已批准语言：Aging records from cycling tests on 已在 language-fixes-batch-01.md 确认；不再以旧 cycling aging records 报错。

### M02-013 — 标题及数据集名称

位置：[中文 L31](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:31)；[英文 L31](D:/MS-AgentNet-English/chapters/chapter02.tex:31)。

中文原文：

```latex
\subsubsection*{（2）CALCE数据集}
```

当前英文：

```latex
\subsubsection*{(2) CALCE dataset}
```

中文回译：

（2）CALCE数据集

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题及数据集名称对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-014 — 6节、1.1/1.35 Ah、1C、4.2/2.7 V

位置：[中文 L33](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:33)；[英文 L33](D:/MS-AgentNet-English/chapters/chapter02.tex:33)。

中文原文：

```latex
CALCE 数据集由马里兰大学先进生命周期工程中心提供，包括 CS2 和 CX2 两组方形锂离子电池的老化数据\cite{ref18,ref61}。两组电池均采用钴酸锂（LCO）作为正极材料，其中 CS2 电池的标称容量为 1.1 Ah，CX2 电池的标称容量为 1.35 Ah。老化实验均在室温条件下开展，电池采用恒流–恒压方式充电至 4.2 V。CS2 和 CX2 均以 1C 恒流放电至 2.7 V。实验覆盖 CS2\_36–CS2\_38 和 CX2\_36–CX2\_38 共 6 节电池的循环老化记录。
```

当前英文：

```latex
The CALCE dataset is provided by the Center for Advanced Life Cycle Engineering at the University of Maryland and contains aging data from two groups of prismatic lithium-ion cells, CS2 and CX2\cite{ref18,ref61}. Both groups use lithium cobalt oxide (LCO) as the cathode material, with nominal capacities of 1.1 Ah for CS2 and 1.35 Ah for CX2. All aging tests were conducted at room temperature, and the cells were charged to 4.2 V using a constant-current--constant-voltage protocol. Both CS2 and CX2 were discharged at a constant current of 1C to 2.7 V. Aging records from cycling tests on 6 cells, CS2\_36–CS2\_38 and CX2\_36–CX2\_38, are included in the experiments.
```

中文回译：

CALCE数据集由马里兰大学先进生命周期工程中心提供，包含CS2和CX2两组方形锂离子电池的老化数据。两组均以钴酸锂（LCO）为正极，CS2和CX2的标称容量分别为1.1 Ah与1.35 Ah。所有老化试验均在室温下进行，电池采用恒流—恒压协议充至4.2 V。CS2和CX2均以1C恒流放电至2.7 V。实验包含CS2_36—CS2_38和CX2_36—CX2_38共6节电池循环试验的老化记录。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 6节、1.1/1.35 Ah、1C、4.2/2.7 V对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 具体机构、型号、化学体系和实验协议是本文事实；三范文不作为这些事实的替代证据，本文所需适配。 |

具体处理：已批准语言：Aging records from cycling tests on 是当前生效修订，不报旧表达。

### M02-015 — 标题及数据集名称

位置：[中文 L35](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:35)；[英文 L35](D:/MS-AgentNet-English/chapters/chapter02.tex:35)。

中文原文：

```latex
\subsubsection*{（3）MIT/Severson数据集}
```

当前英文：

```latex
\subsubsection*{(3) MIT/Severson dataset}
```

中文回译：

（3）MIT/Severson数据集

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题及数据集名称对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-016 — 三电池及每段倍率、SOC、温度和截止电压

位置：[中文 L37](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:37)；[英文 L37](D:/MS-AgentNet-English/chapters/chapter02.tex:37)。

中文原文：

```latex
MIT/Severson 数据集由麻省理工学院、斯坦福大学和丰田研究院联合发布\cite{ref62}。该数据集采用 A123 APR18650M1A 型 18650 圆柱形锂离子电池，每节电池的标称容量约为 1.1 Ah，正极材料为磷酸铁锂（LFP），负极材料为石墨。老化实验在 30 ℃ 的恒温环境下开展。实验纳入 b3c8、b3c13 和 b3c29 三节电池。三节电池均采用两步快速充电策略，其中 b3c8 采用 5.3C（54\% SOC）–4C 策略，b3c13 和 b3c29 采用 5.6C（36\% SOC）–4.3C 策略。达到 80\% SOC 后，电池以 1C 恒流充电至 3.6 V，随后转入恒压充电。放电过程采用 4C 恒流方式，截止电压为 2.0 V。
```

当前英文：

```latex
The MIT/Severson dataset was jointly released by the Massachusetts Institute of Technology, Stanford University, and Toyota Research Institute\cite{ref62}. It uses A123 APR18650M1A 18650 cylindrical lithium-ion cells, each with a nominal capacity of approximately 1.1 Ah, a lithium iron phosphate (LFP) cathode, and a graphite anode. The aging tests were conducted at a constant temperature of 30 ℃. Three cells, b3c8, b3c13, and b3c29, are included in the experiments. All three cells followed two-step fast-charging protocols: 5.3C (54\% SOC)–4C for b3c8 and 5.6C (36\% SOC)–4.3C for b3c13 and b3c29. After reaching 80\% SOC, the cells were charged at a constant current of 1C to 3.6 V, followed by constant-voltage charging. Discharging was performed at a constant current of 4C with a cutoff voltage of 2.0 V.
```

中文回译：

MIT/Severson数据集由麻省理工学院、斯坦福大学和丰田研究院联合发布。该数据集使用A123 APR18650M1A型18650圆柱锂离子电池，每节标称容量约1.1 Ah，正极为磷酸铁锂（LFP），负极为石墨。老化试验在30 ℃恒温下进行。实验包含b3c8、b3c13和b3c29三节电池。三节电池均遵循两步快速充电协议：b3c8为5.3C（54% SOC）—4C，b3c13和b3c29为5.6C（36% SOC）—4.3C。达到80% SOC后，以1C恒流充至3.6 V，再恒压充电。放电采用4C恒流，截止电压为2.0 V。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 三电池及每段倍率、SOC、温度和截止电压对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 具体机构、型号、化学体系和实验协议是本文事实；三范文不作为这些事实的替代证据，本文所需适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-017 — 标题含义

位置：[中文 L42](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:42)；[英文 L42](D:/MS-AgentNet-English/chapters/chapter02.tex:42)。

中文原文：

```latex
\subsection{特征工程}
```

当前英文：

```latex
\subsection{Feature engineering}
```

中文回译：

特征工程

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-018 — 候选池、标定、双阈值与冗余

位置：[中文 L44](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:44)；[英文 L44](D:/MS-AgentNet-English/chapters/chapter02.tex:44)。

中文原文：

```latex
本节围绕 SOH 估计模型的输入构建展开，提出多源健康指标提取与优化算法。该算法首先基于充放电数据建立多源候选健康指标池，随后通过组级标定与筛选优化模型输入：利用 MS-CCCT 标定 CCCT 电压窗口，并结合特征开发电池集合上的 PCC/SCC 评价结果实现双阈值准入与冗余剔除，确定各数据集对应的模型输入。
```

当前英文：

```latex
This section presents the multi-source health indicator extraction and optimization algorithm for constructing the inputs to the SOH estimation model. The algorithm first builds a pool of multi-source candidate HIs from charging and discharging data, then optimizes the model inputs through group-level calibration and selection. Specifically, MS-CCCT calibrates the CCCT voltage window, and PCC/SCC results on the feature-development cell set are used for dual-threshold admission and redundancy removal to determine the inputs for each dataset.
```

中文回译：

本节介绍用于构建SOH估计模型输入的多源健康指标提取与优化算法。算法先用充放电数据构建多源候选HI池，再通过组级标定与筛选优化模型输入。具体而言，MS-CCCT标定CCCT电压窗口，并利用特征开发电池集合上的PCC/SCC结果进行双阈值准入和冗余剔除，以确定各数据集的输入。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 候选池、标定、双阈值与冗余对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 具体机构、型号、化学体系和实验协议是本文事实；三范文不作为这些事实的替代证据，本文所需适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-019 — 标题含义

位置：[中文 L46](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:46)；[英文 L46](D:/MS-AgentNet-English/chapters/chapter02.tex:46)。

中文原文：

```latex
\subsubsection{健康指标提取}
```

当前英文：

```latex
\subsubsection{Health indicator extraction}
```

中文回译：

健康指标提取

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-020 — 四类曲线、15指标及充放电量

位置：[中文 L48](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:48)；[英文 L48](D:/MS-AgentNet-English/chapters/chapter02.tex:48)。

中文原文：

```latex
基于电池循环采集的电压、电流、温度、时间与容量数据，构建充电电压–时间（CVT）、增量容量（IC）、微分温度–电压（DTV）和微分温度–容量（DTC）特征曲线，如\cref{fig:2-3}(a)--(d)所示。根据曲线随老化的变化特性，提取时长、幅值、特征位置和分布宽度等特征；同时计算窗口放电容量与充放电能量效率，形成包含 15 项候选健康指标的指标池\cite{ref52,ref63,ref64,ref65}。各指标的定义与分类见\cref{tab:2-2}。
```

当前英文：

```latex
Charging voltage--time (CVT), incremental capacity (IC), differential temperature--voltage (DTV), and differential temperature--capacity (DTC) curves are constructed from voltage, current, temperature, time, and capacity data collected during battery cycling, as shown in \cref{fig:2-3}(a)--(d). Features describing duration, amplitude, characteristic position, and distribution width are extracted based on how these curves change with aging. Discharge capacity within a voltage window and charge-discharge energy efficiency are also calculated, forming a pool of 15 candidate HIs\cite{ref52,ref63,ref64,ref65}. Their definitions and categories are listed in \cref{tab:2-2}.
```

中文回译：

根据电池循环过程中采集的电压、电流、温度、时间和容量数据构建充电电压—时间（CVT）、增量容量（IC）、温度—电压微分（DTV）和温度—容量微分（DTC）曲线，见图2-3(a)—(d)。根据这些曲线随老化的变化，提取描述时长、幅值、特征位置和分布宽度的特征。同时计算电压窗口内放电容量及充放电能量效率，构成含15项候选HI的指标池。其定义和类别见表2-2。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 四类曲线、15指标及充放电量对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-021 — CVT/CCCT与固定电压区间

位置：[中文 L52](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:52)；[英文 L52](D:/MS-AgentNet-English/chapters/chapter02.tex:52)。

中文原文：

```latex
充电电压–时间（CVT）曲线记录恒流充电阶段端电压随时间的变化，可由电压与时间采样直接获取。随循环推进，CVT 曲线沿时间轴逐渐偏移，如\cref{fig:2-3}(a)所示。该偏移表现为固定电压区间内的充电时长随老化持续变化。电池老化引起的极化增大和容量衰减会共同改变这一充电过程\cite{ref63,ref64}，据此定义 CCCT：
```

当前英文：

```latex
The charging voltage--time (CVT) curve records changes in terminal voltage over time during constant-current charging and can be obtained directly from voltage and time samples. As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). This shift appears as a continuous change in charge duration within a fixed voltage interval as the battery ages. Increased polarization and capacity fade caused by battery aging jointly change this charging process\cite{ref63,ref64}. Accordingly, CCCT is defined as:
```

中文回译：

充电电压—时间（CVT）曲线记录恒流充电时端电压随时间的变化，可直接根据电压与时间采样得到。随着循环推进，CVT曲线逐渐沿时间轴偏移，见图2-3(a)。这种偏移体现为电池老化时固定电压区间内充电时长的连续变化。电池老化引起的极化增大和容量衰减共同改变这一充电过程。据此，CCCT定义如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | CVT/CCCT与固定电压区间对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 可选措辞：continuous change 容易让读者联想到数学连续变化，中文“持续变化”重在老化过程中的持续性；可用 ongoing change，非确定的科学误译。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

具体处理：最小建议：a continuous change → an ongoing change。其余保留。

### M02-022 — 时刻定义与HI1

位置：[中文 L58](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:58)；[英文 L58](D:/MS-AgentNet-English/chapters/chapter02.tex:58)。

中文原文：

```latex
式中，$t(V_1)$、$t(V_2)$ 分别为充电电压达到 $V_1$、$V_2$ 的时刻。CCCT 的电压区间由 MS-CCCT 标定，具体方法见第~\ref{sec:ms-ccct}~节，标定所得充电时长特征记为 HI1。
```

当前英文：

```latex
where $t(V_1)$ and $t(V_2)$ are the times when the charging voltage reaches $V_1$ and $V_2$, respectively. The CCCT voltage interval is calibrated by MS-CCCT, as described in Section~\ref{sec:ms-ccct}, and the resulting charge duration feature is denoted as HI1.
```

中文回译：

其中，t(V1)和t(V2)分别是充电电压达到V1和V2的时刻。CCCT电压区间由MS-CCCT标定，方法见所引小节，所得充电时长特征记为HI1。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 时刻定义与HI1对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-023 — 容量对电压求导、峰位置/形状

位置：[中文 L60](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:60)；[英文 L60](D:/MS-AgentNet-English/chapters/chapter02.tex:60)。

中文原文：

```latex
除充电时序特征外，容量随电压的变化同样包含电池退化信息。增量容量（IC）曲线是解析电池电化学退化的经典分析手段。该方法对容量关于电压求导，将平缓的充电电压平台转化为辨识度更高的特征峰，其位置与形状会随电池老化发生变化\cite{ref50,ref64}。IC 的具体表达式为：
```

当前英文：

```latex
In addition to charge timing features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:
```

中文回译：

除了充电计时特征，容量随电压的变化也包含电池退化信息。增量容量（IC）曲线是分析电池电化学退化的成熟工具。通过对容量关于电压求导，它将较平缓的充电电压平台转化为更清晰的峰，其位置和形状随电池老化变化。IC表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 容量对电压求导、峰位置/形状对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 可选措辞：charge timing features 容易让人先想到充电时机/调度；上下文能消歧，但 charging time features 更直接指时长类特征。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

具体处理：最小建议：charge timing features → charging time features。

### M02-024 — N、HI2—HI4与FWHM

位置：[中文 L66](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:66)；[英文 L66](D:/MS-AgentNet-English/chapters/chapter02.tex:66)。

中文原文：

```latex
式中，$V_k$ 和 $Q_k$ 分别为第 $k$ 个采样点的端电压和充电容量，$N$ 为两个采样点之间的间隔。不同循环下，IC 曲线的峰值、特征位置和分布宽度随老化发生变化，如\cref{fig:2-3}(b)所示。由此提取 IC 曲线的峰值、峰值对应电压和半峰宽，并分别定义为 HI2、HI3 和 HI4。
```

当前英文：

```latex
where $V_k$ and $Q_k$ are the terminal voltage and charge capacity at the $k$th sampling point, respectively, and $N$ is the interval between the two sampling points. Across cycles, the peak value, characteristic position, and distribution width of the IC curve change with aging, as shown in \cref{fig:2-3}(b). The peak value, voltage corresponding to the peak, and full width at half maximum of the IC curve are therefore extracted and defined as HI2, HI3, and HI4, respectively.
```

中文回译：

其中，Vk和Qk分别是第k个采样点的端电压和充电容量，N是两个采样点的间隔。在不同循环间，IC曲线的峰值、特征位置和分布宽度随老化变化，见图2-3(b)。因此提取IC曲线峰值、峰值对应电压与半峰全宽，分别定义为HI2、HI3和HI4。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | N、HI2—HI4与FWHM对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-025 — 通常缓慢、表面温度、对电压的导数

位置：[中文 L68](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:68)；[英文 L68](D:/MS-AgentNet-English/chapters/chapter02.tex:68)。

中文原文：

```latex
温度是反映电池内部状态的另一重要维度。恒流充电过程中，电池表面温度变化通常较为缓慢，老化带来的微小热响应差异难以通过原始温度曲线直接识别。为识别这类差异，Wu 等人\cite{ref65}提出微分温度–电压（DTV）分析方法。该方法通过计算充电过程中电池表面温度相对电压的变化率，将热响应映射至电压域，形成随老化变化的峰谷特征曲线\cite{ref64,ref65}。其定义如下：
```

当前英文：

```latex
Temperature is another important measure of the internal state of a battery. During constant-current charging, the battery surface temperature usually changes slowly, making small aging-related differences in thermal response difficult to identify directly from the raw temperature curve. To identify these differences, Wu et al.\cite{ref65} proposed differential temperature--voltage (DTV) analysis. By calculating the rate of change in battery surface temperature with respect to voltage during charging, this method maps the thermal response to the voltage domain, producing a curve with peaks and valleys that change with aging\cite{ref64,ref65}. DTV is defined as:
```

中文回译：

温度是衡量电池内部状态的另一项重要量。恒流充电时电池表面温度通常变化缓慢，因此与老化有关的微小热响应差异难以从原始温度曲线直接识别。为识别这些差异，Wu等人提出温度—电压微分（DTV）分析。通过计算充电时电池表面温度相对于电压的变化率，该方法将热响应映射至电压域，形成峰谷随老化变化的曲线。DTV定义如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 通常缓慢、表面温度、对电压的导数对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-026 — 200点、HI5—HI9、峰值与峰位

位置：[中文 L74](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:74)；[英文 L74](D:/MS-AgentNet-English/chapters/chapter02.tex:74)。

中文原文：

```latex
其中，$V_k$ 和 $T_k$ 分别为第 $k$ 个采样点的端电压和电池表面温度，$N$ 为两个采样点之间的间隔。为减小差分噪声的影响，对所得 DTV 曲线采用窗口大小为 200 个采样点的移动平均进行平滑处理\cite{ref64}。不同循环下，DTV 曲线的峰谷幅值与特征位置随老化发生变化，如\cref{fig:2-3}(c)所示。据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围\cite{ref64}。
```

当前英文：

```latex
where $V_k$ and $T_k$ are the terminal voltage and battery surface temperature at the $k$th sampling point, respectively, and $N$ is the interval between the two sampling points. To reduce the effect of noise introduced by differencing, the DTV curve is smoothed using a moving average with a window size of 200 sampling points\cite{ref64}. Across cycles, the peak and valley values and characteristic positions of the DTV curve change with aging, as shown in \cref{fig:2-3}(c). The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted to describe the amplitude, characteristic positions, and range of variation of the thermal response\cite{ref64}.
```

中文回译：

其中，Vk和Tk分别是第k个采样点的端电压和电池表面温度，N是两采样点的间隔。为减小差分引入的噪声影响，使用窗口大小为200个采样点的移动平均平滑DTV曲线。在不同循环间，DTV曲线的峰谷值和特征位置随老化变化，见图2-3(c)。提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）及峰谷差（HI9），以描述热响应的幅值、特征位置和变化范围。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 200点、HI5—HI9、峰值与峰位对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-027 — DTV与DTC自变量区分

位置：[中文 L76](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:76)；[英文 L76](D:/MS-AgentNet-English/chapters/chapter02.tex:76)。

中文原文：

```latex
与 DTV 在电压域刻画热响应不同，DTC 在充电容量域刻画热响应。DTC 以充电容量为自变量，描述温度变化率随容量的演化，其定义如下\cite{ref64}：
```

当前英文：

```latex
While DTV characterizes the thermal response in the voltage domain, DTC characterizes it in the charge capacity domain. With charge capacity as the independent variable, DTC describes how the rate of temperature change evolves with capacity and is defined as follows\cite{ref64}:
```

中文回译：

DTV在电压域表征热响应，而DTC在充电容量域表征热响应。DTC以充电容量为自变量，描述温度变化率如何随容量演变，定义如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | DTV与DTC自变量区分对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-028 — 200点、HI10—HI12

位置：[中文 L82](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:82)；[英文 L82](D:/MS-AgentNet-English/chapters/chapter02.tex:82)。

中文原文：

```latex
其中，$T_k$、$Q_k$ 为第 $k$ 个采样点的电池表面温度和充电容量，$N$ 为两个采样点之间的间隔。对所得 DTC 曲线同样采用窗口大小为 200 个采样点的移动平均进行平滑处理\cite{ref64}。\cref{fig:2-3}(d)所示 DTC 曲线同样表现出随循环变化的峰值、特征位置和分布宽度，本文据此提取峰值、峰值对应容量和半峰宽，并将其定义为 HI10、HI11 和 HI12。
```

当前英文：

```latex
where $T_k$ and $Q_k$ are the battery surface temperature and charge capacity at the $k$th sampling point, and $N$ is the interval between the two sampling points. The DTC curve is also smoothed using a moving average with a window size of 200 sampling points\cite{ref64}. The DTC curves in \cref{fig:2-3}(d) likewise show changes in peak value, characteristic position, and distribution width across cycles. Accordingly, the peak value, capacity corresponding to the peak, and full width at half maximum are extracted and defined as HI10, HI11, and HI12.
```

中文回译：

其中，Tk和Qk是第k个采样点的电池表面温度和充电容量，N为两采样点的间隔。同样使用窗口大小为200个采样点的移动平均平滑DTC曲线。图2-3(d)中的DTC曲线也呈现峰值、特征位置和分布宽度随循环变化。据此提取峰值、峰值对应容量与半峰全宽，并定义为HI10、HI11和HI12。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 200点、HI10—HI12对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.1 full.txt L1576–1590、L1609–1614及Table 4 L1634–1647提供曲线、peak value/峰位语境；本文15项编号、FWHM及差分定义保持本文适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-029 — 电流积分与电压筛选区间

位置：[中文 L84](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:84)；[英文 L84](D:/MS-AgentNet-English/chapters/chapter02.tex:84)。

中文原文：

```latex
窗口放电容量由指定电压区间内的放电电流累计积分得到，其定义如下：
```

当前英文：

```latex
Discharge capacity within a voltage window is obtained by integrating the discharge current over a specified voltage interval and is defined as:
```

中文回译：

电压窗口内放电容量通过在指定电压区间上对放电电流积分获得，定义如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 电流积分与电压筛选区间对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 可选措辞：integrating ... over a specified voltage interval 单独读易被理解为对电压积分；紧接dt公式和下一段时间片段定义已消歧。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 放电窗口、完整能量积分及HI13–HI15为本文所需适配；未将Engineering-AI的电压面积CCCA/CCDA换成本段容量或能量指标。 |

具体处理：可选最小建议：by integrating the discharge current over time while the voltage lies within a specified interval。保留电压窗口限定。

### M02-030 — s/Ah、两个电压窗口与HI13/14

位置：[中文 L90](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:90)；[英文 L90](D:/MS-AgentNet-English/chapters/chapter02.tex:90)。

中文原文：

```latex
其中，$V_{\mathrm{dch}}(t)$ 和 $I_{\mathrm{dch}}(t)$ 分别为放电电压和电流，积分范围为电压位于 $[V_l,V_h]$ 内的放电时间片段。时间以 s 为单位，$Q_{\mathrm{dch}}$ 的单位为 Ah。本文进一步构造两个窗口放电容量候选指标，分别计算端电压由 3.80 V 降至 3.40 V 以及由 3.20 V 降至 3.00 V 过程中释放的电荷量，并记为 HI13 和 HI14\cite{ref31,ref52}。
```

当前英文：

```latex
where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge voltage and current, respectively, and integration is performed over the discharge time segments in which the voltage lies within $[V_l,V_h]$. Time is measured in s, and $Q_{\mathrm{dch}}$ is measured in Ah. Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

中文回译：

其中，Vdch(t)和Idch(t)分别是放电电压和电流，积分在电压位于[Vl,Vh]内的放电时间片段上进行。时间以s计，Qdch以Ah计。进一步计算端电压由3.80 V下降到3.40 V和由3.20 V下降到3.00 V时释放的电荷量，构造两个电压窗口内放电容量候选指标，分别记为HI13和HI14。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | s/Ah、两个电压窗口与HI13/14对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 放电窗口、完整能量积分及HI13–HI15为本文所需适配；未将Engineering-AI的电压面积CCCA/CCDA换成本段容量或能量指标。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-031 — 单循环放电能量/充电能量

位置：[中文 L92](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:92)；[英文 L92](D:/MS-AgentNet-English/chapters/chapter02.tex:92)。

中文原文：

```latex
能量效率反映电池在充放电过程中的能量转换特性，定义为单次循环放电能量与充电能量之比\cite{ref66}：
```

当前英文：

```latex
Energy efficiency reflects the energy conversion characteristics of a battery during charging and discharging and is defined as the ratio of discharge energy to charge energy in a single cycle\cite{ref66}:
```

中文回译：

能量效率反映电池充放电时的能量转换特性，定义为单次循环中放电能量与充电能量之比：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 单循环放电能量/充电能量对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 放电窗口、完整能量积分及HI13–HI15为本文所需适配；未将Engineering-AI的电压面积CCCA/CCDA换成本段容量或能量指标。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-032 — 电压/电流幅值/时长及完整阶段

位置：[中文 L98](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:98)；[英文 L98](D:/MS-AgentNet-English/chapters/chapter02.tex:98)。

中文原文：

```latex
其中，$V_{\mathrm{ch}}(t)$、$|I_{\mathrm{ch}}(t)|$、$t_{\mathrm{ch}}$ 与 $V_{\mathrm{dch}}(t)$、$|I_{\mathrm{dch}}(t)|$、$t_{\mathrm{dch}}$ 分别表示充电与放电阶段的端电压、电流幅值和持续时间，充电与放电均取完整循环过程。该能量效率记为 HI15（$\eta$）。
```

当前英文：

```latex
where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$, and $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote the terminal voltage, current magnitude, and duration of the charging and discharging phases, respectively. Both phases cover their full duration within the cycle. This energy efficiency is denoted as HI15 ($\eta$).
```

中文回译：

其中，Vch(t)、|Ich(t)|及tch，以及Vdch(t)、|Idch(t)|及tdch，分别表示充电和放电阶段的端电压、电流幅值及持续时间。两个阶段均涵盖该循环中各自的完整时段。这一能量效率记为HI15（η）。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 电压/电流幅值/时长及完整阶段对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 可选语法：两组三项由 and 串联，再用 respectively，读者需回溯配对。数值/物理含义未丢失。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 放电窗口、完整能量积分及HI13–HI15为本文所需适配；未将Engineering-AI的电压面积CCCA/CCDA换成本段容量或能量指标。 |

具体处理：可选把第二个 and 前改为分号，或分充/放电两个短句；仍保留一个自然段。不属必改。

### M02-033 — 标题含义

位置：[中文 L103](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:103)；[英文 L103](D:/MS-AgentNet-English/chapters/chapter02.tex:103)。

中文原文：

```latex
\subsubsection{组级双相关 MS-CCCT}
```

当前英文：

```latex
\subsubsection{Group-level dual-correlation MS-CCCT}
```

中文回译：

组级双相关MS-CCCT

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-034 — 同数据集两电池、组级得分

位置：[中文 L106](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:106)；[英文 L106](D:/MS-AgentNet-English/chapters/chapter02.tex:106)。

中文原文：

```latex
恒流充电时间能够反映电池容量随循环产生的变化，但其与 SOH 之间的相关性受到提取电压区间的影响。部分研究直接从预设的局部电压区间提取时间特征\cite{ref28,ref63}。然而，不同数据集对应的退化敏感区间并不相同，一个数据集上采用的固定窗口难以直接适用于其他数据集。为提高 CCCT 与 SOH 的相关性及其在同一数据集不同电池上的稳定性，本文提出组级双相关多尺度搜索方法（MS-CCCT）。该方法选取同一数据集内两节电池组成特征开发集合 $\mathcal{B}$，根据集合内的相关性结果构建组级稳健得分，并据此确定 HI1 的提取窗口。
```

当前英文：

```latex
Constant current charge time can reflect changes in battery capacity with cycling, but its correlation with SOH depends on the voltage interval used for extraction. Some studies directly extract time features from predefined local voltage intervals\cite{ref28,ref63}. However, degradation-sensitive intervals differ across datasets, and a fixed window used for one dataset is difficult to apply directly to others. To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT). Two cells from the same dataset form the feature-development set $\mathcal{B}$. Correlation results within this set are used to construct a group-level robust score, which determines the extraction window for HI1.
```

中文回译：

恒流充电时间可以反映电池容量随循环的变化，但其与SOH的相关性取决于提取时采用的电压区间。一些研究直接从预定义的局部电压区间提取时间特征。然而，各数据集的退化敏感区间不同，一个数据集所用的固定窗口难以直接应用于其他数据集。为提高CCCT与SOH的相关性及其在同一数据集各电池间的稳定性，本文提出组级双相关多尺度搜索方法（MS-CCCT）。同一数据集的两节电池组成特征开发集合B。利用集合内的相关性结果构建组级稳健得分，以此确定HI1的提取窗口。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 同数据集两电池、组级得分对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-035 — PCC线性、SCC单调

位置：[中文 L108](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:108)；[英文 L108](D:/MS-AgentNet-English/chapters/chapter02.tex:108)。

中文原文：

```latex
现有 CCCT 窗口优化方法多采用 PCC 评价候选区间\cite{ref31,ref51}。PCC 是衡量 CCCT 与 SOH 线性关联强度的常用统计指标，但该指标仅对线性变化敏感，单独使用难以反映单调非线性关系。SCC 专门评估变量间的单调变化关系，适合刻画这类单调非线性特征。候选窗口评价同时采用 PCC 和 SCC，以兼顾 CCCT 与 SOH 之间的线性关联和单调变化关系\cite{ref25,ref53,ref55}。第 $i$ 个候选窗口在集合 $\mathcal{B}$ 中第 $j$ 节电池上的 PCC $\gamma_{i,j}$ 和 SCC $\rho_{i,j}$ 分别定义为
```

当前英文：

```latex
Most existing CCCT window optimization methods use PCC to evaluate candidate intervals\cite{ref31,ref51}. PCC is a common statistical measure of the strength of the linear association between CCCT and SOH. However, it is sensitive only to linear changes and is insufficient on its own to characterize monotonic nonlinear relationships. SCC specifically measures monotonic relationships between variables and is suitable for characterizing such nonlinear features. Both PCC and SCC are used to evaluate candidate windows, accounting for the linear association and monotonic relationship between CCCT and SOH\cite{ref25,ref53,ref55}. The PCC $\gamma_{i,j}$ and SCC $\rho_{i,j}$ of the $i$th candidate window on the $j$th cell in $\mathcal{B}$ are defined as
```

中文回译：

多数现有CCCT窗口优化方法采用PCC评价候选区间。PCC是衡量CCCT与SOH之间线性关联强度的常用统计量。然而，它仅对线性变化敏感，单独使用不足以描述单调非线性关系。SCC专门衡量变量间的单调关系，适合描述这类非线性特征。采用PCC和SCC共同评价候选窗口，兼顾CCCT与SOH之间的线性关联和单调关系。B中第j节电池上第i个候选窗口的PCC γi,j与SCC ρi,j定义如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | PCC线性、SCC单调对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | “sensitive only to linear changes”原中文已有“仅对线性变化敏感”，不是英译新增；这里PCC度量线性关联，不能由此理解成遇非线性数据必为零。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

具体处理：源表述核实项：若作者意在描述PCC不能充分刻画一般单调非线性，当前中文前句“仅”表述可讨论；不得静默变更科学含义。

### M02-036 — 三个下标、均值、秩及−1至1

位置：[中文 L122](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:122)；[英文 L122](D:/MS-AgentNet-English/chapters/chapter02.tex:122)。

中文原文：

```latex
式中，$f_{i,j,k}$ 表示第 $j$ 节电池在第 $k$ 个循环由第 $i$ 个候选窗口提取的 CCCT，$y_{j,k}$ 为对应循环的 SOH，$n_j$ 为该电池的有效循环数；$\bar{f}_{i,j}$ 和 $\bar{y}_j$ 分别为 CCCT 与 SOH 的均值，$R(\cdot)$ 表示取秩操作。PCC 和 SCC 的取值范围均为 $-1$ 至 $1$，其绝对值越接近 $1$，表示相关性越强。
```

当前英文：

```latex
where $f_{i,j,k}$ is the CCCT extracted from the $i$th candidate window at the $k$th cycle of the $j$th cell, $y_{j,k}$ is the SOH of the corresponding cycle, and $n_j$ is the number of valid cycles for that cell. $\bar{f}_{i,j}$ and $\bar{y}_j$ are the mean CCCT and SOH, respectively, and $R(\cdot)$ denotes the ranking operation. Both PCC and SCC range from $-1$ to $1$, with absolute values closer to $1$ indicating stronger correlations.
```

中文回译：

其中，fi,j,k为第j节电池第k循环中从第i个候选窗口提取的CCCT，yj,k是对应循环的SOH，nj是该电池的有效循环数。相应带横线的f和y分别是CCCT与SOH的均值，R(·)表示取秩操作。PCC和SCC均在−1至1之间，绝对值越接近1表示相关性越强。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 三个下标、均值、秩及−1至1对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-037 — 最小绝对PCC与SCC

位置：[中文 L124](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:124)；[英文 L124](D:/MS-AgentNet-English/chapters/chapter02.tex:124)。

中文原文：

```latex
为综合候选窗口在两节电池上的相关性表现，分别取其在集合 $\mathcal{B}$ 中的最小绝对 PCC 和最小绝对 SCC：
```

当前英文：

```latex
To account for the correlation performance of each candidate window on both cells, its minimum absolute PCC and minimum absolute SCC within $\mathcal{B}$ are calculated:
```

中文回译：

为考虑每个候选窗口在两节电池上的相关性表现，计算它在B中的最小绝对PCC和最小绝对SCC：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 最小绝对PCC与SCC对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-038 — 再次取两者最小值

位置：[中文 L131](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:131)；[英文 L131](D:/MS-AgentNet-English/chapters/chapter02.tex:131)。

中文原文：

```latex
进一步取二者中的较小值作为第 $i$ 个候选窗口的组级稳健得分：
```

当前英文：

```latex
The smaller of these two values is then used as the group-level robust score of the $i$th candidate window:
```

中文回译：

随后使用这两个值中的较小值作为第i个候选窗口的组级稳健得分：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 再次取两者最小值对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-039 — 最低相关性与两电池约束

位置：[中文 L137](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:137)；[英文 L137](D:/MS-AgentNet-English/chapters/chapter02.tex:137)。

中文原文：

```latex
该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，使入选窗口在两节电池上均保持较强的相关性。
```

当前英文：

```latex
This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and allowing the selected window to maintain strong correlations on both cells.
```

中文回译：

该得分由两节电池中的最低相关性决定，阻止单节电池上的局部高相关性主导窗口选择，并使所选窗口在两节电池上都能保持较强相关性。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 交叉复核：中文“可避免”在此可表设计能力，preventing在方法功能描述中有合理对应，不列确定情态加强。can只作可选的能力显化。 |
| ② 术语/数字/条件 | 最低相关性与两电池约束对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现确定的新增夸大；是否显式写can属可选表达，不能把能力用法一律判成不确定性丢失。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

具体处理：最小建议：This score is determined by the lowest correlation across the two cells and can prevent a locally high correlation on a single cell from dominating window selection, allowing the selected window to maintain strong correlations on both cells.

### M02-040 — R1—R3范围、窗宽、步长及严格优于

位置：[中文 L139](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:139)；[英文 L139](D:/MS-AgentNet-English/chapters/chapter02.tex:139)。

中文原文：

```latex
MS-CCCT 采用由粗到细的三阶段搜索。Oxford 数据集的初始搜索范围设为 3.50--4.20 V。R1 阶段采用 0.40 V 窗宽和 0.20 V 步长进行粗定位，并将稳健得分最高的窗口作为下一阶段的搜索区域；R2 阶段在该区域内采用 0.20 V 窗宽和 0.05 V 步长继续搜索；R3 阶段进一步采用 0.10 V 窗宽和 0.05 V 步长细化搜索。若 R3 阶段所得窗口的稳健得分高于 R2 阶段，则采用 R3 窗口，否则保留 R2 阶段的结果。
```

当前英文：

```latex
MS-CCCT uses a three-stage coarse-to-fine search. For the Oxford dataset, the initial search range is 3.50--4.20 V. Stage R1 uses a window width of 0.40 V and a step size of 0.20 V for coarse localization, and the window with the highest robust score becomes the search region for the next stage. Stage R2 searches this region using a window width of 0.20 V and a step size of 0.05 V. Stage R3 further refines the search using a window width of 0.10 V and a step size of 0.05 V. If the robust score obtained in R3 exceeds that in R2, the R3 window is selected; otherwise, the R2 result is retained.
```

中文回译：

MS-CCCT采用三个阶段的由粗到细搜索。对于Oxford数据集，初始搜索范围为3.50—4.20 V。R1阶段采用0.40 V窗宽和0.20 V步长进行粗定位，得分最高的窗口成为下一阶段的搜索区域。R2阶段在该区域中以0.20 V窗宽和0.05 V步长搜索。R3阶段以0.10 V窗宽和0.05 V步长进一步细化搜索。如果R3得分超过R2，就选R3窗口；否则保留R2结果。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | R1—R3范围、窗宽、步长及严格优于对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-041 — 3.55—3.75 V、0.994447

位置：[中文 L141](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:141)；[英文 L141](D:/MS-AgentNet-English/chapters/chapter02.tex:141)。

中文原文：

```latex
最终，Oxford 数据集的 3.55--3.75 V 窗口以 0.994447 的最高稳健得分入选，其对应的恒流充电时间序列作为 HI1。
```

当前英文：

```latex
For the Oxford dataset, the 3.55--3.75 V window is finally selected with the highest robust score of 0.994447, and its constant current charge time series is used as HI1.
```

中文回译：

对于Oxford数据集，最终选取3.55—3.75 V窗口，其最高稳健得分为0.994447，对应的恒流充电时间序列用作HI1。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 3.55—3.75 V、0.994447对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680提供linear correlation/monotonic relationship；BMSFormer L275–283提供逐级窗口词汇，Engineering-AI L332–342提供标定语境。本文双电池最小绝对得分及三阶段参数为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-042 — 标题含义

位置：[中文 L143](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:143)；[英文 L143](D:/MS-AgentNet-English/chapters/chapter02.tex:143)。

中文原文：

```latex
\subsubsection{健康指标筛选}
```

当前英文：

```latex
\subsubsection{Health indicator selection}
```

中文回译：

健康指标筛选

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-043 — 15项候选、HI–SOH及HI–HI

位置：[中文 L145](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:145)；[英文 L145](D:/MS-AgentNet-English/chapters/chapter02.tex:145)。

中文原文：

```latex
健康指标筛选是锂离子电池 SOH 估计中的关键步骤\cite{ref60,ref61,ref62}，所选指标的质量直接影响最终估计精度。在前述 HI1 窗口标定的基础上，将恒流充电时间、IC、DTV、DTC、窗口放电容量和能量效率等 15 项特征共同作为候选健康指标。沿用前述组级相关性评价方式，分别计算各候选指标与 SOH 之间以及不同候选指标之间的 PCC 和 SCC。
```

当前英文：

```latex
HI selection is a key step in lithium-ion battery SOH estimation\cite{ref60,ref61,ref62}, as the quality of the selected indicators directly affects the final estimation accuracy. Following HI1 window calibration, 15 features based on constant current charge time, IC, DTV, DTC, discharge capacity within a voltage window, and energy efficiency are considered as candidate HIs. Using the same group-level correlation evaluation, PCC and SCC are calculated both between each candidate HI and SOH and between different candidate HIs.
```

中文回译：

HI筛选是锂离子电池SOH估计中的关键步骤，因为所选指标质量直接影响最终估计精度。在HI1窗口标定之后，将基于恒流充电时间、IC、DTV、DTC、电压窗口内放电容量和能量效率的15项特征作为候选HI。沿用同一组级相关性评价，分别计算各候选HI与SOH之间及不同候选HI之间的PCC和SCC。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 15项候选、HI–SOH及HI–HI对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-044 — 矩阵上下三角及大小/颜色映射

位置：[中文 L147](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:147)；[英文 L147](D:/MS-AgentNet-English/chapters/chapter02.tex:147)。

中文原文：

```latex
Oxford Cell1 和 Cell2 的相关性结果如\cref{fig:2-4}所示。图中同时展示了候选指标与 SOH 以及候选指标相互之间的 PCC 和 SCC。矩阵下三角列出相关系数，上三角通过圆圈大小和颜色深浅表示相关强度。圆圈越大、颜色越深，表示相应变量之间的相关性越强。
```

当前英文：

```latex
The correlation results for Oxford Cell1 and Cell2 are shown in \cref{fig:2-4}, including both PCC and SCC between candidate HIs and SOH and among the candidate HIs. The lower triangular part of each matrix lists the correlation coefficients, while the upper triangular part represents correlation strength through circle size and color intensity. Larger, darker circles indicate stronger correlations between the corresponding variables.
```

中文回译：

Oxford Cell1与Cell2的相关性结果见图2-4，包括候选HI与SOH之间及候选HI相互间的PCC和SCC。各矩阵下三角列出相关系数，上三角通过圆圈大小与颜色深浅表示相关强度。更大、更深的圆圈表示对应变量之间更强的相关性。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 矩阵上下三角及大小/颜色映射对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-045 — HI5四个数值、Cell1限定

位置：[中文 L149](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:149)；[英文 L149](D:/MS-AgentNet-English/chapters/chapter02.tex:149)。

中文原文：

```latex
同一候选指标在两节电池上的相关性表现并不完全相同。HI5（DTV 峰值）在 Cell1 上的绝对 PCC 和绝对 SCC 分别为 0.949 和 0.966，在 Cell2 上则降至 0.898 和 0.902；相比之下，HI1 在两节电池上均保持较高的相关性。若仅依据 Cell1 的相关性结果，HI5 会表现为强相关指标，但这一结果无法反映其在 Cell2 上的相关水平。单节电池上的相关性排序由此难以完整代表候选指标在其他电池上的表现。
```

当前英文：

```latex
The same candidate HI does not show identical correlation performance on the two cells. For HI5 (DTV peak value), the absolute PCC and SCC are 0.949 and 0.966 on Cell1 but decrease to 0.898 and 0.902 on Cell2. In contrast, HI1 maintains high correlations on both cells. Based on the results for Cell1 alone, HI5 would appear to be strongly correlated, but this result does not reflect its correlation level on Cell2. Thus, a correlation ranking based on a single cell cannot fully represent the performance of candidate HIs on other cells.
```

中文回译：

同一候选HI在两节电池上的相关性表现并不完全相同。HI5（DTV峰值）在Cell1上的绝对PCC与SCC为0.949和0.966，而在Cell2上下降为0.898和0.902。相比之下，HI1在两节电池上均保持高相关性。单看Cell1结果，HI5会显得高度相关，但该结果不能反映它在Cell2上的相关水平。因此，基于单节电池的相关性排名不能完全代表候选HI在其他电池上的表现。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | HI5四个数值、Cell1限定对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-046 — 通常、可能、条件变化

位置：[中文 L151](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:151)；[英文 L151](D:/MS-AgentNet-English/chapters/chapter02.tex:151)。

中文原文：

```latex
现有研究通常依据相关系数的大小选择健康指标。当候选指标的相关性分布随电池化学体系、运行温度等条件发生变化时，这类筛选结果容易受到数据条件的影响。在单一条件下表现较好的指标，在其他电池或工况下的适用性可能下降。为提高筛选结果对电池个体和运行条件变化的鲁棒性，有必要引入综合相关性分布特征的健康指标筛选策略。
```

当前英文：

```latex
Existing studies usually select HIs based on the magnitude of their correlation coefficients. When the correlation distributions of candidate HIs change with battery chemistry, operating temperature, or other conditions, the selection results can be sensitive to the data conditions. An indicator that performs well under one condition may become less applicable to other cells or operating conditions. To improve the robustness of HI selection to differences between individual cells and operating conditions, a selection strategy that accounts for the characteristics of correlation distributions is needed.
```

中文回译：

现有研究通常根据相关系数的大小选择HI。当候选HI的相关性分布随电池化学体系、运行温度或其他条件而变化时，选择结果可能对数据条件敏感。在一种条件下表现良好的指标，在其他电池或工况下可能变得不太适用。为提高HI筛选对电池个体差异和工况差异的稳健性，需要考虑相关性分布特征的筛选策略。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 通常、可能、条件变化对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-047 — 双电池均达标、排序、去冗余

位置：[中文 L155](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:155)；[英文 L155](D:/MS-AgentNet-English/chapters/chapter02.tex:155)。

中文原文：

```latex
据此，本文构建组级健康指标筛选方法。该方法首先综合特征开发集合内两节电池的 PCC 和 SCC，仅保留均满足相关性要求的候选指标。相关性矩阵还显示，部分候选指标之间具有较高的相关系数，表明候选池中存在重复信息。保留的指标按照相关性强度进行排序，并进一步移除与已入选指标高度相关的特征，以降低指标间冗余并保持特征多样性。具体筛选条件、阈值和完整步骤见\cref{tab:2-hi-screening-steps}。
```

当前英文：

```latex
Accordingly, this study develops a group-level HI selection method. It first considers PCC and SCC on both cells in the feature-development set and retains only candidate HIs that meet all correlation requirements. The correlation matrices also show high correlations between some candidate HIs, indicating repeated information in the candidate pool. The retained HIs are ranked by correlation strength, and features highly correlated with already selected HIs are further removed to reduce redundancy while preserving feature diversity. The specific selection criteria, thresholds, and complete procedure are given in \cref{tab:2-hi-screening-steps}.
```

中文回译：

据此，本文建立组级HI筛选方法。它首先考虑特征开发集合中两节电池上的PCC和SCC，仅保留满足全部相关性要求的候选HI。相关性矩阵还显示某些候选HI间相关性较高，提示候选池包含重复信息。按相关强度对保留的HI排序，进一步去除与已选HI高度相关的特征，以降低冗余并保持特征多样性。具体准则、阈值和完整流程见所引筛选步骤表。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 双电池均达标、排序、去冗余对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-048 — HI1与四个六位小数

位置：[中文 L158](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:158)；[英文 L158](D:/MS-AgentNet-English/chapters/chapter02.tex:158)。

中文原文：

```latex
经过相关性准入与冗余剔除，Oxford 数据集最终保留 HI1。该指标在 Cell1 和 Cell2 上的绝对 PCC 分别为 0.998759 和 0.997322，绝对 SCC 分别为 0.998710 和 0.994447。四项相关系数均接近 1，且在两节电池之间差异较小，表明 HI1 对 SOH 变化具有较高的退化敏感性和良好的跨电池一致性。
```

当前英文：

```latex
After correlation-based admission and redundancy removal, HI1 is retained for the Oxford dataset. Its absolute PCC values on Cell1 and Cell2 are 0.998759 and 0.997322, and its absolute SCC values are 0.998710 and 0.994447, respectively. All four coefficients are close to 1 and differ only slightly between the two cells, indicating that HI1 is highly sensitive to SOH changes during degradation and has good cross-cell consistency.
```

中文回译：

经过相关性准入和冗余剔除，Oxford数据集保留HI1。其在Cell1与Cell2上的绝对PCC分别为0.998759、0.997322，绝对SCC分别为0.998710、0.994447。四个系数均接近1，且两节电池间差异很小，表明HI1在退化过程中对SOH变化高度敏感，并具有良好跨电池一致性。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | HI1与四个六位小数对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-049 — 仅开发阶段、固定参数、后续电池排除

位置：[中文 L160](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:160)；[英文 L160](D:/MS-AgentNet-English/chapters/chapter02.tex:160)。

中文原文：

```latex
健康指标筛选仅在特征开发阶段执行。指标确定后，其定义和计算参数保持不变，并直接用于同一数据集其他电池的特征提取。用于后续评价的其他电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发与后续评价之间的数据隔离。
```

当前英文：

```latex
HI selection is performed only during feature development. Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for other cells within the same dataset. The other cells used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between feature development and subsequent evaluation.
```

中文回译：

HI筛选仅在特征开发时执行。指标一经确定，其定义和计算参数即保持固定，并直接用于同一数据集中其他电池的特征提取。用于后续评价的其他电池不参与基于相关性的筛选、阈值确定或HI重选，从而保持特征开发与后续评价之间的数据隔离。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 仅开发阶段、固定参数、后续电池排除对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

### M02-050 — 其余六电池、绝对PCC范围及所列比较对象

位置：[中文 L162](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:162)；[英文 L162](D:/MS-AgentNet-English/chapters/chapter02.tex:162)。

中文原文：

```latex
固定后的 HI1 在 Cell3--Cell8 上的绝对 PCC 为 0.997874--0.999337。与已有健康指标的比较结果见\cref{tab:2-hi-literature}，其相关水平均高于所列样本熵、DTV/IC 特征及充电电压曲线斜率在相应电池上的已报道值，说明 HI1 在其余六节电池上仍保持较高的线性相关性。
```

当前英文：

```latex
With its definition fixed, HI1 achieves absolute PCC values of 0.997874--0.999337 on Cell3--Cell8. Comparisons with existing HIs are presented in \cref{tab:2-hi-literature}. Its correlations exceed the reported values for the listed sample entropy, DTV/IC features, and charging voltage curve slopes on the corresponding cells, showing that HI1 maintains high linear correlations on the remaining six cells.
```

中文回译：

在定义固定后，HI1在Cell3—Cell8上的绝对PCC为0.997874—0.999337。与已有HI的比较见所引文献对比表。它的相关性超过所列样本熵、DTV/IC特征及充电电压曲线斜率在相应电池上的已报告值，表明HI1在其余六节电池上保持较高的线性相关性。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 其余六电池、绝对PCC范围及所列比较对象对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | JESSOHRUL §3.5.2 L1671–1680、L1822–1849对应相关性、retained HIs、排序与去冗余语境；本文双电池、绝对值、阈值及固定应用范围不继承范文实验协议。 |

处理：语义一致，无须因回译措辞不同而修改。

## 第3章逐块核对

### M03-001 — 名称来源、多尺度与轻量化

位置：[中文 L1](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:1)；[英文 L1](D:/MS-AgentNet-English/chapters/chapter03.tex:1)。

中文原文：

```latex
为同时应对电池SOH估计中精度与计算效率两方面的挑战，本文提出一种轻量级多尺度智能体网络（Multi-Scale Agent Network，MS-AgentNet）。其命名中的“MS”源于由小核DSConv-S与大核DSConv-L构成的多尺度卷积设计，用于高效提取不同时间尺度的退化特征。下文介绍MS-AgentNet的总体架构与工作流程，阐述所设计的多尺度深度可分离卷积模块，并详细说明轻量级局部—全局融合注意力（Slim Local-Global Fusion Attention，SLFA）模块。
```

当前英文：

```latex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Slim Local-Global Fusion Attention (SLFA) module.
```

中文回译：

为应对电池SOH估计在精度与计算效率两方面的挑战，本文提出轻量化多尺度智能体网络（MS-AgentNet）。名称中的MS指由小核DSConv-S与大核DSConv-L组成的多尺度卷积设计，它高效提取不同时间尺度上的退化特征。以下各小节介绍MS-AgentNet的整体架构与工作流程，说明设计的多尺度深度可分离卷积模块，并详述轻量级局部—全局融合注意力（SLFA）模块。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 名称来源、多尺度与轻量化对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-002 — 标题含义

位置：[中文 L3](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:3)；[英文 L3](D:/MS-AgentNet-English/chapters/chapter03.tex:3)。

中文原文：

```latex
\subsection{MS-AgentNet架构概述}
```

当前英文：

```latex
\subsection{Architecture overview of MS-AgentNet}
```

中文回译：

MS-AgentNet架构概述

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-003 — 窗口、d维、读出与紧邻循环标签

位置：[中文 L5](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:5)；[英文 L5](D:/MS-AgentNet-English/chapters/chapter03.tex:5)。

中文原文：

```latex
MS-AgentNet的总体架构如\cref{fig:3-1}所示：健康指标（Health Indicators，HIs）序列经滑动窗口划分为样本片段，通过线性嵌入层映射至$d$维特征空间后输入MS-AgentNet Block；Block输出经层归一化、展平和线性读出后得到SOH估计值，训练时以每个输入窗口后紧邻循环的真实SOH值作为监督标签。
```

当前英文：

```latex
The overall architecture of MS-AgentNet is shown in \cref{fig:3-1}. Health indicator (HI) sequences are divided into sample segments using a sliding window, mapped to a $d$-dimensional feature space through a linear embedding layer, and fed into an MS-AgentNet Block. The Block output passes through layer normalization, flattening, and a linear readout to produce the SOH estimate. During training, the true SOH of the cycle immediately following each input window is used as the supervision label.
```

中文回译：

MS-AgentNet的整体架构见图3-1。通过滑动窗口将健康指标（HI）序列划分成样本片段，经线性嵌入层映射至d维特征空间，输入MS-AgentNet Block。Block输出依次经过层归一化、展平和线性读出，产生SOH估计值。训练时以每个输入窗口紧随其后循环的真实SOH作为监督标签。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 窗口、d维、读出与紧邻循环标签对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-004 — B/N/d和三步

位置：[中文 L7](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:7)；[英文 L7](D:/MS-AgentNet-English/chapters/chapter03.tex:7)。

中文原文：

```latex
从数学角度看，设第$l$个MS-AgentNet Block的输入为$\mathbf X_l\in\mathbb R^{B\times N\times d}$，其中$B$为批量大小，$N$为输入序列长度，$d$为特征嵌入维度。Block通过以下三个步骤完成特征变换：
```

当前英文：

```latex
Mathematically, let the input to the $l$th MS-AgentNet Block be $\mathbf X_l\in\mathbb R^{B\times N\times d}$, where $B$ is the batch size, $N$ is the input sequence length, and $d$ is the feature embedding dimension. The Block transforms the features in three steps:
```

中文回译：

数学上，令第l个MS-AgentNet Block的输入为Xl∈R^(B×N×d)，其中B是批量大小，N是输入序列长度，d是特征嵌入维度。Block通过三个步骤变换特征：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | B/N/d和三步对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-005 — SLFA中DSConv-S与RAA分工

位置：[中文 L9](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:9)；[英文 L9](D:/MS-AgentNet-English/chapters/chapter03.tex:9)。

中文原文：

```latex
\textbf{步骤1：局部—全局特征融合。} 输入$\mathbf X_l$经SLFA模块处理。SLFA利用DSConv-S提取局部特征，并通过ReLU$^2$智能体注意力（ReLU$^2$ Agent Attention，RAA）建立跨位置全局信息交互：
```

当前英文：

```latex
\textbf{Step 1: Local-global feature fusion.} The input $\mathbf X_l$ is processed by SLFA, which uses DSConv-S to extract local features and ReLU$^2$ Agent Attention (RAA) to establish global information interactions across positions:
```

中文回译：

步骤1：局部—全局特征融合。输入Xl由SLFA处理，SLFA使用DSConv-S提取局部特征，并使用ReLU²智能体注意力（RAA）建立跨位置的全局信息交互：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | SLFA中DSConv-S与RAA分工对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-006 — LN→DSConv-L→缩放→残差

位置：[中文 L18](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:18)；[英文 L18](D:/MS-AgentNet-English/chapters/chapter03.tex:18)。

中文原文：

```latex
\textbf{步骤2：长尺度特征细化。} SLFA的输出$\mathbf X_l'$经层归一化后输入DSConv-L，以提取较长时间尺度的退化特征。DSConv-L的输出经$W_l$缩放，并与$\mathbf X_l'$进行残差相加：
```

当前英文：

```latex
\textbf{Step 2: Feature refinement over longer time scales.} The SLFA output $\mathbf X_l'$ passes through layer normalization and then DSConv-L to extract degradation features over longer time scales. The DSConv-L output is scaled by $W_l$ and added to $\mathbf X_l'$ through a residual connection:
```

中文回译：

步骤2：较长时间尺度上的特征细化。SLFA输出Xl′依次经过层归一化和DSConv-L，以提取较长时间尺度上的退化特征。DSConv-L的输出经Wl缩放后，通过残差连接与Xl′相加：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | LN→DSConv-L→缩放→残差对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-007 — LN0→FFN→残差

位置：[中文 L33](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:33)；[英文 L33](D:/MS-AgentNet-English/chapters/chapter03.tex:33)。

中文原文：

```latex
\textbf{步骤3：非线性映射。} 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN），并与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：
```

当前英文：

```latex
\textbf{Step 3: Nonlinear mapping.} The features $\mathbf X_l''$ are processed by $\operatorname{LN}_0$ and then a feedforward neural network (FFN). The result is added to $\mathbf X_l''$ through a residual connection to produce the Block output $\mathbf Y_l$:
```

中文回译：

步骤3：非线性映射。特征Xl″经LN0处理后再经过前馈神经网络（FFN）。所得结果通过残差连接与Xl″相加，产生Block输出Yl：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | LN0→FFN→残差对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-008 — 下一Block、Wl及LN0无仿射参数

位置：[中文 L46](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:46)；[英文 L46](D:/MS-AgentNet-English/chapters/chapter03.tex:46)。

中文原文：

```latex
令$\mathbf Y_l$作为下一Block的输入，即$\mathbf X_{l+1}=\mathbf Y_l$。其中，$W_l$为可学习缩放系数；$\operatorname{LN}$和$\operatorname{LN}_0$均表示层归一化，$\operatorname{LN}_0$不使用额外的缩放和偏置参数。
```

当前英文：

```latex
The output $\mathbf Y_l$ is used as the input to the next Block, i.e., $\mathbf X_{l+1}=\mathbf Y_l$. Here, $W_l$ is a learnable scaling factor. Both $\operatorname{LN}$ and $\operatorname{LN}_0$ denote layer normalization, but $\operatorname{LN}_0$ uses no additional scale or bias parameters.
```

中文回译：

将输出Yl作为下一Block的输入，即Xl+1=Yl。其中，Wl为可学习缩放系数。LN和LN0都表示层归一化，但LN0不使用额外的缩放或偏置参数。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 下一Block、Wl及LN0无仿射参数对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-009 — 标题含义

位置：[中文 L50](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:50)；[英文 L50](D:/MS-AgentNet-English/chapters/chapter03.tex:50)。

中文原文：

```latex
\subsection{所设计的多尺度深度可分离卷积模块}
```

当前英文：

```latex
\subsection{The designed multi-scale depthwise separable convolution modules}
```

中文回译：

所设计的多尺度深度可分离卷积模块

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-010 — 先基本结构再成本及分工

位置：[中文 L52](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:52)；[英文 L52](D:/MS-AgentNet-English/chapters/chapter03.tex:52)。

中文原文：

```latex
为兼顾多尺度局部特征提取与计算效率，本节首先介绍DSConv的基本结构，并将其与标准卷积进行计算量比较；随后说明DSConv-S和DSConv-L的结构配置及其功能分工。
```

当前英文：

```latex
To combine multi-scale local feature extraction with computational efficiency, this section first introduces the basic structure of DSConv and compares its computational cost with that of standard convolution. The configurations and respective roles of DSConv-S and DSConv-L are then described.
```

中文回译：

为兼顾多尺度局部特征提取与计算效率，本节先介绍DSConv基本结构，并比较它与标准卷积的计算成本，随后说明DSConv-S与DSConv-L的配置及各自作用。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 先基本结构再成本及分工对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746对应HI→窗口→嵌入→Block→输出/标签的数据流；本文SLFA/RAA和LN0配置为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-011 — 标题含义

位置：[中文 L55](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:55)；[英文 L55](D:/MS-AgentNet-English/chapters/chapter03.tex:55)。

中文原文：

```latex
\subsubsection{DSConv基本结构与计算量比较}
```

当前英文：

```latex
\subsubsection{Basic DSConv structure and computational cost comparison}
```

中文回译：

DSConv基本结构与计算成本比较

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-012 — 通道/核与成本、可能过拟合

位置：[中文 L57](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:57)；[英文 L57](D:/MS-AgentNet-English/chapters/chapter03.tex:57)。

中文原文：

```latex
卷积运算通过滑动卷积核提取时间序列中的局部信息\cite{ref71}。标准卷积在所有输入通道上进行运算，每个卷积核生成一个输出特征图，对应一个输出通道。随着输入通道数、输出通道数和卷积核尺寸增加，其参数量与计算开销迅速累积，显著推高计算负载并延长训练时间。在小样本电池数据集上，较大的参数量还可能增加模型的过拟合风险。其计算成本可表示为：
```

当前英文：

```latex
Convolution extracts local information from time series through sliding kernels\cite{ref71}. Standard convolution operates across all input channels, with each kernel producing one output feature map corresponding to one output channel. As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time. A larger parameter count may also increase the risk of overfitting on small-sample battery datasets. Its computational cost can be expressed as:
```

中文回译：

卷积通过滑动核从时间序列中提取局部信息。标准卷积跨全部输入通道运算，每个核产生一个输出特征图，对应一个输出通道。随着输入、输出通道数量与核尺寸增大，参数量和计算开销迅速增长，大幅增加计算负载和训练时间。较大的参数量也可能提高模型在小样本电池数据集上的过拟合风险。其计算成本可表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 通道/核与成本、可能过拟合对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.2.1 L766–789对应卷积输入通道、输出特征图、计算成本与符号；本文数学条件仍须独立核对。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-013 — k/Cin/Cout/DF定义

位置：[中文 L66](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:66)；[英文 L66](D:/MS-AgentNet-English/chapters/chapter03.tex:66)。

中文原文：

```latex
其中，$k$、$C_{\mathrm{in}}$、$C_{\mathrm{out}}$和$D_F$分别表示卷积核大小、输入通道数、输出通道数和特征图尺寸。
```

当前英文：

```latex
where $k$, $C_{\mathrm{in}}$, $C_{\mathrm{out}}$, and $D_F$ denote the kernel size, number of input channels, number of output channels, and feature map size, respectively.
```

中文回译：

其中，k、Cin、Cout和DF分别表示核尺寸、输入通道数量、输出通道数量和特征图尺寸。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | k/Cin/Cout/DF定义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.2.1 L766–789对应卷积输入通道、输出特征图、计算成本与符号；本文数学条件仍须独立核对。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-014 — depthwise→pointwise及通道数

位置：[中文 L68](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:68)；[英文 L68](D:/MS-AgentNet-English/chapters/chapter03.tex:68)。

中文原文：

```latex
与标准卷积不同，深度可分离卷积（DSConv）将卷积运算分解为深度卷积和逐点卷积两个阶段\cite{ref71}。其中，深度卷积为每个输入通道单独配置卷积核，在通道内完成局部特征提取；随后，$1\times1$逐点卷积融合不同通道的特征，并将通道数调整为$C_{\mathrm{out}}$。通过分离通道内特征提取与通道间特征融合，DSConv减少了标准卷积中的密集跨通道运算。其计算成本可表示为：
```

当前英文：

```latex
Unlike standard convolution, depthwise separable convolution (DSConv) divides convolution into two stages: depthwise convolution and pointwise convolution\cite{ref71}. Depthwise convolution applies a separate kernel to each input channel to extract local features within that channel. A $1\times1$ pointwise convolution then fuses features across channels and adjusts the number of channels to $C_{\mathrm{out}}$. By separating within-channel feature extraction from cross-channel feature fusion, DSConv reduces the dense cross-channel operations required by standard convolution. Its computational cost can be expressed as:
```

中文回译：

与标准卷积不同，深度可分离卷积（DSConv）把卷积分为深度卷积和逐点卷积两个阶段。深度卷积对每个输入通道使用独立的核，在该通道内提取局部特征。随后1×1逐点卷积融合通道间特征，并把通道数调整至Cout。通过分离通道内特征提取与跨通道特征融合，DSConv减少标准卷积所需的密集跨通道运算。其计算成本表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | depthwise→pointwise及通道数对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.2.1 L766–789对应卷积输入通道、输出特征图、计算成本与符号；本文数学条件仍须独立核对。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-015 — 比值引导

位置：[中文 L79](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:79)；[英文 L79](D:/MS-AgentNet-English/chapters/chapter03.tex:79)。

中文原文：

```latex
进一步比较两类卷积的计算量，可得二者之比为：
```

当前英文：

```latex
The ratio of the computational costs of the two types of convolution is:
```

中文回译：

这两类卷积计算成本的比值如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 比值引导对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.2.1 L766–789对应卷积输入通道、输出特征图、计算成本与符号；本文数学条件仍须独立核对。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-016 — 成本比较的适用条件

位置：[中文 L100](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:100)；[英文 L100](D:/MS-AgentNet-English/chapters/chapter03.tex:100)。

中文原文：

```latex
由式\eqref{eq:dsconv_cost_ratio}可知，在输入、输出通道配置一致的情况下，DSConv的计算成本低于标准卷积，为后续小核与大核卷积模块的构建提供了基础。
```

当前英文：

```latex
Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and output channel configurations, DSConv has a lower computational cost than standard convolution, providing the basis for the small- and large-kernel modules described below.
```

中文回译：

所引计算成本比公式表明，在输入和输出通道配置相同时，DSConv的计算成本低于标准卷积，为下文的小核和大核模块提供基础。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 成本比较的适用条件对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 中文和英文均把低成本写为同通道配置下的结论，但式1/Cout+1/k²还需要核/通道条件才能小于1；例如k=1时不成立。属于中文源条件问题，不是翻译扩大。 |
| ⑤ 范文语境 | BMSFormer §3.2.1 L766–789对应卷积输入通道、输出特征图、计算成本与符号；本文数学条件仍须独立核对。 |

具体处理：源待确认：明确比较针对的核尺寸及通道范围后再修改。当前不擅自补条件或改变公式。

### M03-017 — 标题含义

位置：[中文 L102](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:102)；[英文 L102](D:/MS-AgentNet-English/chapters/chapter03.tex:102)。

中文原文：

```latex
\subsubsection{DSConv-S：双重作用的局部增强}
```

当前英文：

```latex
\subsubsection{DSConv-S: Dual-role local enhancement}
```

中文回译：

DSConv-S：双重作用的局部增强

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-018 — 1×5、RAA之前、双作用

位置：[中文 L104](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:104)；[英文 L104](D:/MS-AgentNet-English/chapters/chapter03.tex:104)。

中文原文：

```latex
小核DSConv-S采用紧凑的$1\times5$深度卷积，并嵌入SLFA模块、位于RAA全局交互之前，以实现输入增强与局部分支保留两项作用：
```

当前英文：

```latex
Small-kernel DSConv-S uses a compact $1\times5$ depthwise convolution and is embedded in SLFA before the global interactions in RAA. It serves two roles: input enhancement and local branch preservation:
```

中文回译：

小核DSConv-S使用紧凑的1×5深度卷积，嵌入SLFA中并位于RAA的全局交互之前。它有输入增强和局部分支保留两项作用：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 1×5、RAA之前、双作用对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-019 — XS先于QKV、聚合广播

位置：[中文 L106](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:106)；[英文 L106](D:/MS-AgentNet-English/chapters/chapter03.tex:106)。

中文原文：

```latex
1. \textbf{输入增强。} DSConv-S提取输入特征中的局部邻域信息，形成局部增强表示$\mathbf X_S$。RAA随后基于$\mathbf X_S$构造查询、键和值，并通过智能体聚合与广播完成跨位置交互。这一前置卷积为RAA引入局部性偏置，增强其在跨位置上下文聚合过程中对局部变化的表征。
```

当前英文：

```latex
1. \textbf{Input enhancement.} DSConv-S extracts local neighborhood information from the input features to form a locally enhanced representation $\mathbf X_S$. RAA then constructs queries, keys, and values from $\mathbf X_S$ and performs cross-position interactions through agent aggregation and broadcasting. This preceding convolution introduces a locality bias into RAA, improving its representation of local variations during cross-position context aggregation.
```

中文回译：

1. 输入增强。DSConv-S从输入特征中提取局部邻域信息，形成局部增强表示XS。RAA随后从XS构建查询、键和值，通过智能体聚合与广播进行跨位置交互。这一前置卷积为RAA引入局部性偏置，改善其在跨位置上下文聚合中对局部变化的表示。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | XS先于QKV、聚合广播对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-020 — 双分支、局部分支LN

位置：[中文 L108](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:108)；[英文 L108](D:/MS-AgentNet-English/chapters/chapter03.tex:108)。

中文原文：

```latex
2. \textbf{局部分支保留。} 在SLFA中，$\mathbf X_S$同时传递至RAA分支和局部分支。局部分支对$\mathbf X_S$进行层归一化后传递至融合端，并与RAA分支建立的跨位置上下文进行融合，形成局部特征与全局信息的互补表示。
```

当前英文：

```latex
2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

中文回译：

2. 局部分支保留。在SLFA中，XS同时传给RAA分支和局部分支。局部分支对XS进行层归一化后传至融合阶段，与RAA分支建立的跨位置上下文结合，形成局部特征与全局信息的互补表示。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 双分支、局部分支LN对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-021 — B×N×d、转置、2d

位置：[中文 L110](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:110)；[英文 L110](D:/MS-AgentNet-English/chapters/chapter03.tex:110)。

中文原文：

```latex
DSConv-S采用两倍通道扩展。给定输入特征$\mathbf X\in\mathbb R^{B\times N\times d}$，其中$B$、$N$和$d$分别表示批量大小、序列长度和嵌入维度，输入首先经转置使嵌入维度对应卷积通道维度，随后通过第一层$1\times1$逐点卷积将通道维度扩展至$2d$：
```

当前英文：

```latex
DSConv-S uses a channel expansion factor of two. Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:
```

中文回译：

DSConv-S采用两倍通道扩展。给定输入特征X∈R^(B×N×d)，其中B、N和d分别是批量大小、序列长度与嵌入维度，先转置输入，使嵌入维度成为卷积通道维度。随后第一层1×1逐点卷积将通道维度扩展到2d：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | B×N×d、转置、2d对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-022 — 1×5、通道独立

位置：[中文 L122](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:122)；[英文 L122](D:/MS-AgentNet-English/chapters/chapter03.tex:122)。

中文原文：

```latex
扩展后的特征通过$1\times5$深度卷积，该卷积在各通道内独立处理序列特征，以提取短邻域信息：
```

当前英文：

```latex
The expanded features pass through a $1\times5$ depthwise convolution, which processes the sequence features independently within each channel to extract information from a short local neighborhood:
```

中文回译：

扩展特征经过1×5深度卷积，该卷积在各通道内独立处理序列特征，以从短局部邻域中提取信息：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 1×5、通道独立对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-023 — ReLU及非线性

位置：[中文 L131](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:131)；[英文 L131](D:/MS-AgentNet-English/chapters/chapter03.tex:131)。

中文原文：

```latex
随后，应用ReLU激活函数引入非线性：
```

当前英文：

```latex
A ReLU activation is then applied to introduce nonlinearity:
```

中文回译：

随后应用ReLU激活以引入非线性：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | ReLU及非线性对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-024 — 第二PW、恢复d

位置：[中文 L139](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:139)；[英文 L139](D:/MS-AgentNet-English/chapters/chapter03.tex:139)。

中文原文：

```latex
之后，第二层$1\times1$逐点卷积融合不同通道的信息，并将通道维度恢复为$d$：
```

当前英文：

```latex
Next, the second $1\times1$ pointwise convolution fuses information across channels and restores the channel dimension to $d$:
```

中文回译：

接着，第二层1×1逐点卷积融合跨通道信息，并把通道维度恢复到d：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 第二PW、恢复d对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-025 — 逆转置及输入残差

位置：[中文 L148](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:148)；[英文 L148](D:/MS-AgentNet-English/chapters/chapter03.tex:148)。

中文原文：

```latex
最后，输出经逆转置恢复至原始排列，并与输入通过残差连接融合：
```

当前英文：

```latex
Finally, the output is transposed back to its original arrangement and combined with the input through a residual connection:
```

中文回译：

最后，将输出转置回原始排列，通过残差连接与输入结合：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 逆转置及输入残差对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-026 — PW↑/↓、DW5、T/逆T

位置：[中文 L159](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:159)；[英文 L159](D:/MS-AgentNet-English/chapters/chapter03.tex:159)。

中文原文：

```latex
其中，$\operatorname{PW}_{\uparrow}$和$\operatorname{PW}_{\downarrow}$分别表示通道扩展和通道恢复的逐点卷积，$\operatorname{DW}_{5}$表示尺寸为$1\times5$的深度卷积，$\mathcal T(\cdot)$与$\mathcal T^{-1}(\cdot)$分别表示转置和逆转置操作。
```

当前英文：

```latex
where $\operatorname{PW}_{\uparrow}$ and $\operatorname{PW}_{\downarrow}$ denote the pointwise convolutions for channel expansion and restoration, respectively, $\operatorname{DW}_{5}$ denotes the $1\times5$ depthwise convolution, and $\mathcal T(\cdot)$ and $\mathcal T^{-1}(\cdot)$ denote the transpose and inverse transpose operations, respectively.
```

中文回译：

其中，PW↑和PW↓分别表示用于通道扩展和恢复的逐点卷积，DW5表示1×5深度卷积，T(·)及T⁻¹(·)分别表示转置与逆转置操作。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | PW↑/↓、DW5、T/逆T对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-027 — 2倍、两PW与一DW

位置：[中文 L161](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:161)；[英文 L161](D:/MS-AgentNet-English/chapters/chapter03.tex:161)。

中文原文：

```latex
\textbf{计算分析。} 在两倍通道扩展条件下，DSConv-S的计算成本主要来自两层$1\times1$逐点卷积和一层$1\times5$深度卷积，可表示为：
```

当前英文：

```latex
\textbf{Computational analysis.} With a channel expansion factor of two, the computational cost of DSConv-S mainly comes from two $1\times1$ pointwise convolutions and one $1\times5$ depthwise convolution and can be expressed as:
```

中文回译：

计算分析。在通道扩展倍数为二时，DSConv-S的计算成本主要来自两层1×1逐点卷积及一层1×5深度卷积，可表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 2倍、两PW与一DW对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-028 — 2Cout、DF×DF

位置：[中文 L170](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:170)；[英文 L170](D:/MS-AgentNet-English/chapters/chapter03.tex:170)。

中文原文：

```latex
其中，$2C_{\mathrm{out}}$和$D_F\times D_F$分别表示扩展后的通道数和特征图尺寸。
```

当前英文：

```latex
where $2C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of channels and the feature map size, respectively.
```

中文回译：

其中，2Cout和DF×DF分别表示扩展后通道数量和特征图尺寸。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 2Cout及DF×DF忠实保留；本章输入为B×N×d、卷积1×5，但成本仍采用二维面积DF×DF记号，与前面序列长度N的对应未说明。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.1 L855–860、L875–884对应小核、locality bias及局部分支语境；本文Q/K/V全由XS生成，不照搬范文只增强K/V或rank restoration的更强机制结论。 |

具体处理：源待确认：这里是通用二维记号还是实际一维序列成本，英文没有引入该问题；与M03-032联合核实。

### M03-029 — 标题含义

位置：[中文 L172](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:172)；[英文 L172](D:/MS-AgentNet-English/chapters/chapter03.tex:172)。

中文原文：

```latex
\subsubsection{DSConv-L：长尺度特征细化}
```

当前英文：

```latex
\subsubsection{DSConv-L: Feature refinement over longer time scales}
```

中文回译：

DSConv-L：较长时间尺度上的特征细化

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-030 — 三倍、1×31、残差在Block

位置：[中文 L174](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:174)；[英文 L174](D:/MS-AgentNet-English/chapters/chapter03.tex:174)。

中文原文：

```latex
DSConv-L置于SLFA之后，采用三倍通道扩展和$1\times31$深度卷积，从融合表示中提取较长时间尺度的退化特征。两层$1\times1$逐点卷积分别完成通道扩展与恢复，整体变换顺序与DSConv-S一致；其残差连接在MS-AgentNet Block层完成，如式\eqref{eq:block_dsconv_l}所示。
```

当前英文：

```latex
DSConv-L follows SLFA and uses a channel expansion factor of three and a $1\times31$ depthwise convolution to extract degradation features over longer time scales from the fused representation. Two $1\times1$ pointwise convolutions expand and restore the channel dimension, respectively, following the same transformation order as DSConv-S. Its residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}.
```

中文回译：

DSConv-L位于SLFA之后，采用三倍通道扩展和1×31深度卷积，从融合表示中提取较长时间尺度上的退化特征。两层1×1逐点卷积分别扩展和恢复通道维度，变换顺序与DSConv-S相同。其残差连接施加在MS-AgentNet Block层，如所引公式所示。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 三倍、1×31、残差在Block对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.2 L898–901、L914–921对应融合后大核细化；本文只保留长时间尺度作用，不继承噪声过滤/aging inertia解释。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-031 — 三倍成本

位置：[中文 L176](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:176)；[英文 L176](D:/MS-AgentNet-English/chapters/chapter03.tex:176)。

中文原文：

```latex
\textbf{计算分析。} 在三倍通道扩展条件下，DSConv-L的计算成本可表示为：
```

当前英文：

```latex
\textbf{Computational analysis.} With a channel expansion factor of three, the computational cost of DSConv-L can be expressed as:
```

中文回译：

计算分析。在通道扩展倍数为三时，DSConv-L的计算成本可表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 三倍成本对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.2 L898–901、L914–921对应融合后大核细化；本文只保留长时间尺度作用，不继承噪声过滤/aging inertia解释。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-032 — 3Cout、DF×DF

位置：[中文 L185](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:185)；[英文 L185](D:/MS-AgentNet-English/chapters/chapter03.tex:185)。

中文原文：

```latex
其中，$3C_{\mathrm{out}}$和$D_F\times D_F$分别表示扩展后的通道数和特征图尺寸。
```

当前英文：

```latex
where $3C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of channels and the feature map size, respectively.
```

中文回译：

其中，3Cout和DF×DF分别表示扩展后通道数量和特征图尺寸。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 3Cout及DF×DF与中文一致；同M03-028，序列张量与面积记号对应待源稿澄清。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.2.2 L898–901、L914–921对应融合后大核细化；本文只保留长时间尺度作用，不继承噪声过滤/aging inertia解释。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-033 — 专名Slim/SLFA

位置：[中文 L189](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:189)；[英文 L189](D:/MS-AgentNet-English/chapters/chapter03.tex:189)。

中文原文：

```latex
\subsection{所提出的轻量级局部—全局融合注意力模块}
```

当前英文：

```latex
\subsection{The proposed Slim Local-Global Fusion Attention module}
```

中文回译：

所提出的轻量级局部—全局融合注意力模块

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 专名Slim/SLFA对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-034 — 一般形式→比较→SLFA

位置：[中文 L191](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:191)；[英文 L191](D:/MS-AgentNet-English/chapters/chapter03.tex:191)。

中文原文：

```latex
本节给出多头自注意力的一般形式，简要比较Softmax注意力与线性注意力，并在此基础上介绍所提出的SLFA模块。该模块兼顾局部—全局特征建模与计算效率。
```

当前英文：

```latex
This section presents the general form of multi-head self-attention, briefly compares Softmax attention and linear attention, and then introduces the proposed SLFA module, which combines local-global feature modeling with computational efficiency.
```

中文回译：

本节给出多头自注意力的一般形式，简要比较Softmax注意力与线性注意力，再介绍所提出的SLFA模块，该模块结合局部—全局特征建模与计算效率。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 一般形式→比较→SLFA对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-035 — 标题含义

位置：[中文 L194](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:194)；[英文 L194](D:/MS-AgentNet-English/chapters/chapter03.tex:194)。

中文原文：

```latex
\subsubsection{多头自注意力的一般形式}
```

当前英文：

```latex
\subsubsection{General form of multi-head self-attention}
```

中文回译：

多头自注意力的一般形式

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-036 — 多头并行、子空间、QKV

位置：[中文 L196](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:196)；[英文 L196](D:/MS-AgentNet-English/chapters/chapter03.tex:196)。

中文原文：

```latex
多头自注意力通过多个并行注意力头在不同表示子空间内计算特征之间的相关性\cite{ref34}。设输入特征为$\mathbf X\in\mathbb R^{N\times d}$，第$i$个注意力头的查询、键和值表示为：
```

当前英文：

```latex
Multi-head self-attention uses multiple parallel attention heads to calculate correlations between features in different representation subspaces\cite{ref34}. Given input features $\mathbf X\in\mathbb R^{N\times d}$, the query, key, and value representations of the $i$th attention head are:
```

中文回译：

多头自注意力使用多个并行注意力头，在不同表示子空间中计算特征之间的相关性。给定输入特征X∈R^(N×d)，第i个注意力头的查询、键和值表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 多头并行、子空间、QKV对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-037 — 投影维度与h、dh

位置：[中文 L205](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:205)；[英文 L205](D:/MS-AgentNet-English/chapters/chapter03.tex:205)。

中文原文：

```latex
其中，$N$为序列长度，$d$为输入特征维度，$\mathbf W_i^Q,\mathbf W_i^K,\mathbf W_i^V\in\mathbb R^{d\times d_h}$为可学习投影矩阵，$i=1,2,\ldots,h$，$h$为注意力头数，$d_h=d/h$为单个注意力头的特征维度。
```

当前英文：

```latex
where $N$ is the sequence length, $d$ is the input feature dimension, and $\mathbf W_i^Q,\mathbf W_i^K,\mathbf W_i^V\in\mathbb R^{d\times d_h}$ are learnable projection matrices. Here, $i=1,2,\ldots,h$, $h$ is the number of attention heads, and $d_h=d/h$ is the feature dimension of each head.
```

中文回译：

其中，N是序列长度，d是输入特征维度，WiQ、WiK及WiV∈R^(d×dh)为可学习投影矩阵。i=1,2,…,h，h是注意力头数，dh=d/h为每个头的特征维度。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 投影维度与h、dh对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-038 — 非负相似度条件

位置：[中文 L207](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:207)；[英文 L207](D:/MS-AgentNet-English/chapters/chapter03.tex:207)。

中文原文：

```latex
在采用非负相似度函数构造归一化注意力权重时，第$i$个注意力头在第$p$个位置的输出可表示为：
```

当前英文：

```latex
When a nonnegative similarity function is used to construct normalized attention weights, the output at the $p$th position of the $i$th attention head can be expressed as:
```

中文回译：

当使用非负相似度函数构建归一化注意力权重时，第i个注意力头在第p个位置的输出可以表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 非负相似度条件对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-039 — 位置及头下标、非负函数

位置：[中文 L223](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:223)；[英文 L223](D:/MS-AgentNet-English/chapters/chapter03.tex:223)。

中文原文：

```latex
其中，$\mathbf Q_{i,p}$表示第$i$个注意力头中第$p$个位置的查询，$\mathbf K_{i,j}$和$\mathbf V_{i,j}$分别表示第$j$个位置的键和值，$\operatorname{Sim}(\cdot,\cdot)$表示非负相似度函数\cite{ref40}。
```

当前英文：

```latex
where $\mathbf Q_{i,p}$ is the query at the $p$th position in the $i$th attention head, $\mathbf K_{i,j}$ and $\mathbf V_{i,j}$ are the key and value at the $j$th position, respectively, and $\operatorname{Sim}(\cdot,\cdot)$ is a nonnegative similarity function\cite{ref40}.
```

中文回译：

其中，Qi,p是第i个头中第p个位置的查询，Ki,j与Vi,j分别是第j个位置的键和值，Sim(·,·)是非负相似度函数。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 位置及头下标、非负函数对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-040 — Oi维度、拼接与计算顺序

位置：[中文 L225](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:225)；[英文 L225](D:/MS-AgentNet-English/chapters/chapter03.tex:225)。

中文原文：

```latex
所有位置的输出共同构成第$i$个注意力头的输出矩阵$\mathbf O_i\in\mathbb R^{N\times d_h}$，各注意力头的输出随后沿特征维度拼接。不同注意力机制的主要区别在于相似度函数及其计算顺序。
```

当前英文：

```latex
The outputs at all positions form the output matrix $\mathbf O_i\in\mathbb R^{N\times d_h}$ of the $i$th attention head. The outputs of all heads are then concatenated along the feature dimension. Attention mechanisms mainly differ in their similarity functions and computation order.
```

中文回译：

所有位置的输出构成第i个注意力头的输出矩阵Oi∈R^(N×dh)。随后沿特征维度拼接所有头的输出。注意力机制的主要区别是相似度函数与计算顺序。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | Oi维度、拼接与计算顺序对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-041 — 标题含义

位置：[中文 L227](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:227)；[英文 L227](D:/MS-AgentNet-English/chapters/chapter03.tex:227)。

中文原文：

```latex
\subsubsection{Softmax注意力与线性注意力}
```

当前英文：

```latex
\subsubsection{Softmax attention and linear attention}
```

中文回译：

Softmax注意力与线性注意力

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-042 — 点积与Softmax

位置：[中文 L229](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:229)；[英文 L229](D:/MS-AgentNet-English/chapters/chapter03.tex:229)。

中文原文：

```latex
标准Softmax注意力通过查询与键的点积计算序列位置之间的相关性，并利用Softmax函数对相关性得分进行归一化\cite{ref34}。第$i$个注意力头的输出可表示为：
```

当前英文：

```latex
Standard Softmax attention calculates correlations between sequence positions through query-key dot products and normalizes the correlation scores using the Softmax function\cite{ref34}. The output of the $i$th attention head can be expressed as:
```

中文回译：

标准Softmax注意力通过查询—键点积计算序列位置之间的相关性，用Softmax函数归一化相关性得分。第i个注意力头的输出可表示如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 点积与Softmax对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-043 — N×N、单头计算及内存复杂度

位置：[中文 L242](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:242)；[英文 L242](D:/MS-AgentNet-English/chapters/chapter03.tex:242)。

中文原文：

```latex
Softmax中的指数映射与归一化使相关性较高的查询—键对获得更大的注意力权重\cite{ref34}。然而，$\mathbf Q_i\mathbf K_i^{\mathrm T}$需要计算所有查询与键之间的两两关系，并形成尺寸为$N\times N$的注意力矩阵。因此，单个注意力头的计算复杂度为$O(N^2d_h)$，相关性矩阵的存储复杂度为$O(N^2)$；随着序列长度增加，其计算与存储开销会显著增大\cite{ref34,ref39}。
```

当前英文：

```latex
The exponential mapping and normalization in Softmax assign larger attention weights to more highly correlated query-key pairs\cite{ref34}. However, $\mathbf Q_i\mathbf K_i^{\mathrm T}$ requires pairwise calculations between all queries and keys, forming an $N\times N$ attention matrix. Thus, the computational complexity of one attention head is $O(N^2d_h)$, and the memory complexity of the correlation matrix is $O(N^2)$. As the sequence length increases, the computational and storage overhead grows substantially\cite{ref34,ref39}.
```

中文回译：

Softmax中的指数映射和归一化为相关性更高的查询—键对分配更大注意力权重。然而，QiKiᵀ需要对全部查询与键进行两两计算，形成N×N注意力矩阵。因此单头计算复杂度为O(N²dh)，相关性矩阵内存复杂度为O(N²)。序列长度增大时，计算与存储开销大幅增加。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | N×N、单头计算及内存复杂度对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-044 — 核映射与乘法结合律

位置：[中文 L244](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:244)；[英文 L244](D:/MS-AgentNet-English/chapters/chapter03.tex:244)。

中文原文：

```latex
针对Softmax注意力的二次计算开销，线性注意力利用核函数$\phi(\cdot)$映射查询和键，并借助矩阵乘法结合律重新组织计算顺序\cite{ref40}。第$i$个注意力头的输出可写为：
```

当前英文：

```latex
To address the quadratic computational cost of Softmax attention, linear attention maps queries and keys through a kernel function $\phi(\cdot)$ and rearranges the computation order using the associative property of matrix multiplication\cite{ref40}. The output of the $i$th attention head can be written as:
```

中文回译：

为应对Softmax注意力的二次计算成本，线性注意力通过核函数φ(·)映射查询和键，并利用矩阵乘法的结合律重新安排计算顺序。第i个头的输出可以写成：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 核映射与乘法结合律对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-045 — 非负映射、ELU+1、全1向量

位置：[中文 L263](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:263)；[英文 L263](D:/MS-AgentNet-English/chapters/chapter03.tex:263)。

中文原文：

```latex
其中，$\phi(\cdot)$表示非负特征映射，例如$\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$；$\mathbf 1$表示全1向量，用于计算对应的归一化项\cite{ref40}。
```

当前英文：

```latex
where $\phi(\cdot)$ is a nonnegative feature mapping, such as $\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$, and $\mathbf 1$ is an all-ones vector used to calculate the corresponding normalization term\cite{ref40}.
```

中文回译：

其中，φ(·)是非负特征映射，例如φ(x)=ELU(x)+1；1是全1向量，用于计算相应归一化项。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 非负映射、ELU+1、全1向量对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-046 — 先KᵀV、映射维度、固定dh

位置：[中文 L265](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:265)；[英文 L265](D:/MS-AgentNet-English/chapters/chapter03.tex:265)。

中文原文：

```latex
通过优先计算$\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$，线性注意力避免了完整$N\times N$注意力矩阵的构造。当特征映射维度与$d_h$一致时，其计算复杂度为$O(Nd_h^2)$；当$d_h$固定时，该复杂度关于序列长度$N$为线性\cite{ref40}。
```

当前英文：

```latex
By first calculating $\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$, linear attention avoids constructing the full $N\times N$ attention matrix. When the feature mapping dimension equals $d_h$, its computational complexity is $O(Nd_h^2)$. For a fixed $d_h$, this complexity is linear in the sequence length $N$\cite{ref40}.
```

中文回译：

通过先计算φ(Ki)ᵀVi，线性注意力避免构建完整N×N注意力矩阵。当特征映射维度等于dh时，计算复杂度为O(Ndh²)。对于固定dh，该复杂度相对于序列长度N为线性。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 先KᵀV、映射维度、固定dh对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-047 — 较低复杂度与缺少显式局部

位置：[中文 L267](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:267)；[英文 L267](D:/MS-AgentNet-English/chapters/chapter03.tex:267)。

中文原文：

```latex
线性注意力以较低计算复杂度完成全局信息交互，但其计算过程未显式引入局部邻域特征\cite{ref31,ref39,ref40,ref64}。因此，需要进一步协同建模跨位置交互与局部特征。
```

当前英文：

```latex
Linear attention enables global information interactions at a lower computational complexity, but its computation does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref40,ref64}. Joint modeling of cross-position interactions and local features is therefore needed.
```

中文回译：

线性注意力以较低计算复杂度实现全局信息交互，但其计算没有显式纳入局部邻域特征。因此需要联合建模跨位置交互和局部特征。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 较低复杂度与缺少显式局部对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.3.2 L974–987与Engineering-AI §4.3.1 L903–912对应Softmax/线性注意力与复杂度；本文逐头维度、归一化及操作次序为适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-048 — 标题含义

位置：[中文 L269](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:269)；[英文 L269](D:/MS-AgentNet-English/chapters/chapter03.tex:269)。

中文原文：

```latex
\subsubsection{所提出的SLFA模块}
```

当前英文：

```latex
\subsubsection{The proposed SLFA module}
```

中文回译：

所提出的SLFA模块

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-049 — DSConv-S先于RAA、两分支加法

位置：[中文 L271](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:271)；[英文 L271](D:/MS-AgentNet-English/chapters/chapter03.tex:271)。

中文原文：

```latex
为同时捕获局部邻域特征与跨位置交互，本文将DSConv-S与所构建的ReLU²智能体注意力（ReLU² Agent Attention，RAA）相结合，提出SLFA模块，其结构如\cref{fig:3-3}(d)所示。该模块采用局部分支与RAA分支的融合形式：DSConv-S首先提取局部表示，RAA随后以该表示为输入完成跨位置特征交互，两个分支的输出经加法融合。
```

当前英文：

```latex
To capture both local neighborhood features and cross-position interactions, this study combines DSConv-S with the developed ReLU² Agent Attention (RAA) to form the SLFA module, as shown in \cref{fig:3-3}(d). The module fuses a local branch with an RAA branch: DSConv-S first extracts a local representation, and RAA then uses this representation to establish cross-position feature interactions. The outputs of the two branches are fused by addition.
```

中文回译：

为同时捕获局部邻域特征与跨位置交互，本文将DSConv-S与所构建的ReLU²智能体注意力（RAA）结合，形成SLFA模块，见图3-3(d)。该模块融合局部分支和RAA分支：DSConv-S先提取局部表示，随后RAA用该表示建立跨位置特征交互。两分支输出通过加法融合。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | DSConv-S先于RAA、两分支加法对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-050 — 专名RAA

位置：[中文 L273](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:273)；[英文 L273](D:/MS-AgentNet-English/chapters/chapter03.tex:273)。

中文原文：

```latex
\textbf{（1）ReLU²智能体注意力。}
```

当前英文：

```latex
\textbf{(1) ReLU² Agent Attention.}
```

中文回译：

（1）ReLU²智能体注意力。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 专名RAA对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-051 — 两阶段及信息流向

位置：[中文 L275](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:275)；[英文 L275](D:/MS-AgentNet-English/chapters/chapter03.tex:275)。

中文原文：

```latex
Agent Attention以少量智能体作为信息中介，将序列位置之间的全局交互分解为上下文聚合与信息广播两个阶段\cite{ref46}：智能体首先从键和值中聚合序列上下文，各查询位置随后从智能体上下文中读取信息。
```

当前英文：

```latex
Agent Attention uses a small number of agents as information intermediaries to divide global interactions between sequence positions into context aggregation and information broadcasting\cite{ref46}. The agents first aggregate sequence context from the keys and values, and each query position then reads information from the agent context.
```

中文回译：

智能体注意力用少量智能体作为信息中介，将序列位置间的全局交互分解为上下文聚合与信息广播。智能体先从键和值聚合序列上下文，每个查询位置再从智能体上下文读取信息。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 两阶段及信息流向对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-052 — 缩放与划分头

位置：[中文 L277](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:277)；[英文 L277](D:/MS-AgentNet-English/chapters/chapter03.tex:277)。

中文原文：

```latex
为降低查询、键和值生成过程中的参数开销，RAA采用可学习通道缩放调节不同特征通道的相对贡献，并将缩放后的特征划分至各注意力头：
```

当前英文：

```latex
To reduce the parameter overhead of query, key, and value generation, RAA uses learnable channel scaling to adjust the relative contributions of different feature channels and splits the scaled features across attention heads:
```

中文回译：

为减少生成查询、键和值的参数开销，RAA用可学习通道缩放调整不同特征通道的相对贡献，并把缩放后的特征划分到各注意力头：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 缩放与划分头对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-053 — 三向量、逐元素及分割

位置：[中文 L286](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:286)；[英文 L286](D:/MS-AgentNet-English/chapters/chapter03.tex:286)。

中文原文：

```latex
其中，$\mathbf s_q,\mathbf s_k,\mathbf s_v\in\mathbb R^d$为可学习通道缩放向量，$\odot$表示逐元素相乘，$\operatorname{Split}_i(\cdot)$表示沿特征维度划分为$h$个$d_h$维子空间并取第$i$个子空间。
```

当前英文：

```latex
where $\mathbf s_q,\mathbf s_k,\mathbf s_v\in\mathbb R^d$ are learnable channel scaling vectors, $\odot$ denotes element-wise multiplication, and $\operatorname{Split}_i(\cdot)$ divides the feature dimension into $h$ subspaces of dimension $d_h$ and selects the $i$th subspace.
```

中文回译：

其中，sq、sk、sv∈R^d是可学习通道缩放向量，⊙表示逐元素相乘，Spliti(·)将特征维度划分为h个维度为dh的子空间并选择第i个子空间。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 三向量、逐元素及分割对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-054 — 约3d²对3d

位置：[中文 L288](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:288)；[英文 L288](D:/MS-AgentNet-English/chapters/chapter03.tex:288)。

中文原文：

```latex
相较于标准查询、键和值线性投影约$3d^2$的参数量，三组通道缩放向量仅包含$3d$个参数，从而降低了查询、键和值生成过程中的参数开销。
```

当前英文：

```latex
Compared with standard linear projections for queries, keys, and values, which require approximately $3d^2$ parameters, the three channel scaling vectors contain only $3d$ parameters, reducing the parameter overhead of query, key, and value generation.
```

中文回译：

与需要约3d²个参数的标准查询、键和值线性投影相比，三组通道缩放向量仅含3d个参数，减少查询、键、值生成过程的参数开销。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 约3d²对3d对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-055 — na=2、训练学习及样本共享

位置：[中文 L290](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:290)；[英文 L290](D:/MS-AgentNet-English/chapters/chapter03.tex:290)。

中文原文：

```latex
RAA设置$n_a=2$个可学习智能体，以矩阵$\mathbf A\in\mathbb R^{n_a\times d}$表示，其参数通过训练学习，并在不同输入样本间共享。
```

当前英文：

```latex
RAA uses $n_a=2$ learnable agents, represented by a matrix $\mathbf A\in\mathbb R^{n_a\times d}$. Their parameters are learned during training and shared across input samples.
```

中文回译：

RAA使用na=2个可学习智能体，以矩阵A∈R^(na×d)表示。其参数在训练中学习，并在输入样本间共享。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | na=2、训练学习及样本共享对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-056 — 沿特征维分头、Ai尺寸

位置：[中文 L292](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:292)；[英文 L292](D:/MS-AgentNet-English/chapters/chapter03.tex:292)。

中文原文：

```latex
沿特征维度将全局智能体矩阵$\mathbf A$划分为$h$个子空间，第$i$个注意力头对应的智能体表示为$\mathbf A_i=\operatorname{Split}_i(\mathbf A)\in\mathbb R^{n_a\times d_h}$。
```

当前英文：

```latex
The global agent matrix $\mathbf A$ is divided into $h$ subspaces along the feature dimension. The agent representation for the $i$th attention head is $\mathbf A_i=\operatorname{Split}_i(\mathbf A)\in\mathbb R^{n_a\times d_h}$.
```

中文回译：

沿特征维度将全局智能体矩阵A划分成h个子空间。第i个注意力头的智能体表示为Ai=Spliti(A)∈R^(na×dh)。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 沿特征维分头、Ai尺寸对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-057 — 共同正缩小、Softmax均匀趋势

位置：[中文 L294](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:294)；[英文 L294](D:/MS-AgentNet-English/chapters/chapter03.tex:294)。

中文原文：

```latex
在信息广播阶段，查询需要根据自身与两个智能体的匹配关系分配上下文权重。标准Agent Attention在聚合与广播阶段均采用Softmax归一化。当一行得分按共同正比例缩小时，正得分之间的相对比例虽然保持不变，权重却趋于均匀，使对应查询对两个智能体上下文的读取趋向等权混合。为在这种尺度变化下保留正相关匹配的区分，RAA在两个阶段采用ReLU²行归一化：
```

当前英文：

```latex
During information broadcasting, each query assigns context weights according to how it matches the two agents. Standard Agent Attention uses Softmax normalization in both aggregation and broadcasting. When all scores in a row are reduced by a common positive scaling factor, the relative ratios between positive scores remain unchanged, but the weights approach a uniform distribution. The corresponding query therefore reads an increasingly equal mixture of the two agent contexts. To preserve the distinction between positive matches under such scale changes, RAA uses ReLU² row normalization in both stages:
```

中文回译：

信息广播时，各查询根据自身与两个智能体的匹配关系分配上下文权重。标准智能体注意力在聚合和广播时都使用Softmax归一化。当一行所有得分按共同正缩放因子减小时，正得分间的相对比例不变，但权重趋于均匀分布。因此，对应查询读取的两个智能体上下文越来越接近等权混合。为了在这种尺度变化下保留正匹配之间的区别，RAA在两个阶段都使用ReLU²行归一化：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 共同正缩小、Softmax均匀趋势对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 可选精确化：reduced by a common positive scaling factor 可被读成除以大于1的因子；结论仍是缩小，未改变主要推理。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

具体处理：可选最小建议：multiplied by the same positive factor smaller than one。明确乘法及(0,1)条件，需作者确认再落正文。

### M03-058 — 两种M、非正截断、正缩放不变、无正则均匀

位置：[中文 L311](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:311)；[英文 L311](D:/MS-AgentNet-English/chapters/chapter03.tex:311)。

中文原文：

```latex
其中，$M$表示每一行参与归一化的元素数量：在智能体聚合阶段，$M=N$；在信息广播阶段，$M=n_a$。ReLU截断非正相关性得分。对于含有正得分的行，共同正尺度的平方在分子与分母中相互抵消，因此整体得分按共同正比例变化时，权重分配保持不变。平方操作进一步增大较大与较小正得分的权重比，使归一化权重更加突出较高的正相关性得分。当某一行不存在正相关性得分时，$\mathcal R_2(\cdot)$返回均匀分布，以保持归一化结果的有效性。
```

当前英文：

```latex
where $M$ is the number of elements normalized in each row: $M=N$ during agent aggregation and $M=n_a$ during information broadcasting. ReLU sets nonpositive correlation scores to zero. For a row containing positive scores, the squared common positive scaling factor cancels between the numerator and denominator. Thus, the weight distribution remains unchanged when all scores are scaled by the same positive factor. Squaring further increases the weight ratio between larger and smaller positive scores, giving greater emphasis to higher positive correlation scores. When a row contains no positive correlation scores, $\mathcal R_2(\cdot)$ returns a uniform distribution to keep the normalization valid.
```

中文回译：

其中，M是每行归一化的元素数：智能体聚合时M=N，信息广播时M=na。ReLU将非正相关性得分设为零。对于含正得分的行，共同正缩放因子的平方在分子与分母间抵消。因此，所有得分按同一正因子缩放时权重分布不变。平方进一步提高较大和较小正得分的权重比，更突出较高正相关性得分。如果一行没有正相关性得分，R2(·)返回均匀分布以保持归一化有效。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 两种M、非正截断、正缩放不变、无正则均匀对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-059 — Ai作查询、键值上下文

位置：[中文 L313](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:313)；[英文 L313](D:/MS-AgentNet-English/chapters/chapter03.tex:313)。

中文原文：

```latex
在智能体聚合阶段，$\mathbf A_i$作为查询，从序列的键和值中汇集上下文：
```

当前英文：

```latex
During agent aggregation, $\mathbf A_i$ acts as the query to gather context from the sequence keys and values:
```

中文回译：

智能体聚合时，Ai作为查询，从序列键和值中收集上下文：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | Ai作查询、键值上下文对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-060 — Φk/VA矩阵尺寸

位置：[中文 L329](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:329)；[英文 L329](D:/MS-AgentNet-English/chapters/chapter03.tex:329)。

中文原文：

```latex
其中，$\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$表示智能体对各序列位置的聚合权重，$\mathbf V_{A,i}\in\mathbb R^{n_a\times d_h}$表示聚合得到的智能体上下文。
```

当前英文：

```latex
where $\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$ contains the weights used by the agents to aggregate information from each sequence position, and $\mathbf V_{A,i}\in\mathbb R^{n_a\times d_h}$ is the resulting agent context.
```

中文回译：

其中，Φk,i∈R^(na×N)含有智能体从各序列位置聚合信息的权重，VA,i∈R^(na×dh)是所得智能体上下文。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | Φk/VA矩阵尺寸对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-061 — 查询读取上下文

位置：[中文 L331](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:331)；[英文 L331](D:/MS-AgentNet-English/chapters/chapter03.tex:331)。

中文原文：

```latex
在信息广播阶段，各查询位置根据自身特征从智能体上下文中读取信息：
```

当前英文：

```latex
During information broadcasting, each query position reads information from the agent context according to its own features:
```

中文回译：

信息广播时，各查询位置根据自身特征从智能体上下文中读取信息：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 查询读取上下文对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-062 — Φq/Oi尺寸与两上下文组合

位置：[中文 L347](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:347)；[英文 L347](D:/MS-AgentNet-English/chapters/chapter03.tex:347)。

中文原文：

```latex
其中，$\boldsymbol{\Phi}_{q,i}\in\mathbb R^{N\times n_a}$表示各查询位置对智能体的广播权重，$\mathbf O_i\in\mathbb R^{N\times d_h}$为第$i$个注意力头的输出。各查询与智能体的匹配得分经ReLU²行归一化得到广播权重，用于对两个智能体上下文进行加权组合，形成相应的全局交互表示。
```

当前英文：

```latex
where $\boldsymbol{\Phi}_{q,i}\in\mathbb R^{N\times n_a}$ contains the broadcasting weights assigned to the agents by each query position, and $\mathbf O_i\in\mathbb R^{N\times d_h}$ is the output of the $i$th attention head. ReLU² row normalization converts query-agent matching scores into broadcasting weights, which combine the two agent contexts to form the corresponding global interaction representation.
```

中文回译：

其中，Φq,i∈R^(N×na)含有每个查询位置向智能体分配的广播权重，Oi∈R^(N×dh)为第i个注意力头的输出。ReLU²行归一化将查询—智能体匹配得分转为广播权重，这些权重组合两个智能体上下文，形成对应的全局交互表示。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | Φq/Oi尺寸与两上下文组合对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-063 — 等效映射、秩≤na

位置：[中文 L349](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:349)；[英文 L349](D:/MS-AgentNet-English/chapters/chapter03.tex:349)。

中文原文：

```latex
由式\eqref{eq:agent_aggregation}和式\eqref{eq:agent_broadcast}可知，从等效映射角度看，第$i$个注意力头中智能体介导的序列交互可表示为$\boldsymbol{\Phi}_{q,i}\boldsymbol{\Phi}_{k,i}\in\mathbb R^{N\times N}$，其秩不超过智能体数量$n_a$。
```

当前英文：

```latex
Equations \eqref{eq:agent_aggregation} and \eqref{eq:agent_broadcast} show that the agent-mediated sequence interaction in the $i$th attention head can be represented by the equivalent mapping $\boldsymbol{\Phi}_{q,i}\boldsymbol{\Phi}_{k,i}\in\mathbb R^{N\times N}$, whose rank is at most the number of agents $n_a$.
```

中文回译：

所引聚合与广播公式表明，第i个注意力头中智能体介导的序列交互可表示为等效映射Φq,iΦk,i∈R^(N×N)，其秩至多为智能体数量na。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 等效映射、秩≤na对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-064 — 拼接→缩放→残差

位置：[中文 L351](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:351)；[英文 L351](D:/MS-AgentNet-English/chapters/chapter03.tex:351)。

中文原文：

```latex
各注意力头的输出沿特征维度拼接，并通过可学习输出缩放向量$\mathbf s_o$调节通道响应，随后与输入特征进行残差相加：
```

当前英文：

```latex
The outputs of all attention heads are concatenated along the feature dimension. A learnable output scaling vector $\mathbf s_o$ then adjusts the channel responses, and the result is added to the input features through a residual connection:
```

中文回译：

沿特征维度拼接所有注意力头的输出。随后可学习输出缩放向量so调整通道响应，通过残差连接将所得结果与输入特征相加：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 拼接→缩放→残差对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-065 — Concat与so

位置：[中文 L361](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:361)；[英文 L361](D:/MS-AgentNet-English/chapters/chapter03.tex:361)。

中文原文：

```latex
其中，$\operatorname{Concat}(\cdot)$表示沿特征维度拼接各注意力头的输出，$\mathbf s_o\in\mathbb R^d$为可学习输出缩放向量。
```

当前英文：

```latex
where $\operatorname{Concat}(\cdot)$ concatenates the outputs of all attention heads along the feature dimension, and $\mathbf s_o\in\mathbb R^d$ is a learnable output scaling vector.
```

中文回译：

其中，Concat(·)沿特征维度拼接所有注意力头的输出，so∈R^d是可学习输出缩放向量。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | Concat与so对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-066 — 单/多头计算量及固定h、na

位置：[中文 L363](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:363)；[英文 L363](D:/MS-AgentNet-English/chapters/chapter03.tex:363)。

中文原文：

```latex
RAA在聚合与广播阶段分别生成$n_a\times N$和$N\times n_a$相关性矩阵。由此，单个注意力头的计算复杂度为$O(Nn_ad_h)$，$h$个注意力头的总计算复杂度为$O(Nn_ad)$，相关性权重的存储规模为$O(hNn_a)$。当$h$和$n_a$固定时，计算量与存储量均随序列长度$N$线性增长。
```

当前英文：

```latex
RAA generates correlation matrices of size $n_a\times N$ and $N\times n_a$ during aggregation and broadcasting, respectively. The computational complexity is therefore $O(Nn_ad_h)$ for one attention head and $O(Nn_ad)$ for all $h$ heads, while the memory required for the correlation weights is $O(hNn_a)$. With fixed $h$ and $n_a$, both computation and memory grow linearly with the sequence length $N$.
```

中文回译：

RAA在聚合和广播中分别产生na×N与N×na相关性矩阵。因此，一个头的计算复杂度为O(Nna dh)，全部h个头为O(Nna d)，相关性权重所需内存为O(hNna)。当h和na固定时，计算量和内存均随序列长度N线性增长。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 单/多头复杂度、矩阵维度及固定h和na均一致；关于N的复杂度比较沿用本节固定特征维度的常规语境，未推导实际运行速度最小。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | Engineering-AI §4.3.1 L903–927提供agent、aggregation与复杂度语境；RAA的双智能体、通道缩放、ReLU²规则和秩界为本文特有，未标为三范文原机制。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-067 — 标题含义

位置：[中文 L365](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:365)；[英文 L365](D:/MS-AgentNet-English/chapters/chapter03.tex:365)。

中文原文：

```latex
\textbf{（2）局部—全局特征融合。}
```

当前英文：

```latex
\textbf{(2) Local-global feature fusion.}
```

中文回译：

（2）局部—全局特征融合。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 标题含义对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | 标题/专名按本文定义核对；一般标题无需硬配范文。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-068 — XS先生成、局部分支LN、RAA交互

位置：[中文 L367](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:367)；[英文 L367](D:/MS-AgentNet-English/chapters/chapter03.tex:367)。

中文原文：

```latex
输入特征$\mathbf X$首先经DSConv-S得到局部表示$\mathbf X_S=\operatorname{DSConv\text{-}S}(\mathbf X)$，随后分别进入局部分支和RAA分支。局部分支对$\mathbf X_S$进行层归一化，RAA分支通过智能体聚合与信息广播建立跨位置特征交互。SLFA的融合输出$\mathbf X_F$计算如下：
```

当前英文：

```latex
The input features $\mathbf X$ first pass through DSConv-S to obtain the local representation $\mathbf X_S=\operatorname{DSConv\text{-}S}(\mathbf X)$, which is then fed into the local and RAA branches. The local branch applies layer normalization to $\mathbf X_S$, while the RAA branch establishes cross-position feature interactions through agent aggregation and information broadcasting. The fused output $\mathbf X_F$ of SLFA is calculated as:
```

中文回译：

输入特征X先经过DSConv-S得到局部表示XS=DSConv-S(X)，再输入局部分支与RAA分支。局部分支对XS施加层归一化，RAA分支通过智能体聚合与信息广播建立跨位置特征交互。SLFA的融合输出XF计算如下：

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | XS先生成、局部分支LN、RAA交互对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746提供融合模块数据流语境；Engineering-AI §4.2.1 L875–884提供局部分支与全局上下文词汇。本文加性融合、Wa和Dropout为所需适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-069 — XF、两个分支、训练Dropout、Wa

位置：[中文 L382](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:382)；[英文 L382](D:/MS-AgentNet-English/chapters/chapter03.tex:382)。

中文原文：

```latex
其中，$\mathbf X_F$表示SLFA的融合输出，$\operatorname{LN}(\mathbf X_S)$为局部分支的归一化表示，$\operatorname{RAA}(\mathbf X_S)$为RAA分支输出；$\operatorname{Dropout}(\cdot)$用于训练阶段的正则化\cite{ref75}，$W_a$为调节RAA分支贡献的可学习缩放系数。
```

当前英文：

```latex
where $\mathbf X_F$ is the fused SLFA output, $\operatorname{LN}(\mathbf X_S)$ is the normalized local branch representation, and $\operatorname{RAA}(\mathbf X_S)$ is the RAA branch output. $\operatorname{Dropout}(\cdot)$ provides regularization during training\cite{ref75}, and $W_a$ is a learnable scaling factor that adjusts the contribution of the RAA branch.
```

中文回译：

其中，XF是SLFA融合输出，LN(XS)是归一化局部分支表示，RAA(XS)是RAA分支输出。Dropout(·)在训练时提供正则化，Wa是调整RAA分支贡献的可学习缩放系数。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | XF、两个分支、训练Dropout、Wa对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746提供融合模块数据流语境；Engineering-AI §4.2.1 L875–884提供局部分支与全局上下文词汇。本文加性融合、Wa和Dropout为所需适配。 |

处理：语义一致，无须因回译措辞不同而修改。

### M03-070 — 加性融合与关于N线性

位置：[中文 L384](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:384)；[英文 L384](D:/MS-AgentNet-English/chapters/chapter03.tex:384)。

中文原文：

```latex
这种加性连接保留了DSConv-S提取的局部退化特征，并融合RAA建立的跨位置上下文，在形成局部—全局联合表示的同时，保持关于序列长度$N$的线性计算复杂度。
```

当前英文：

```latex
This additive connection preserves the local degradation features extracted by DSConv-S and combines them with the cross-position context established by RAA, forming a joint local-global representation while maintaining linear computational complexity with respect to the sequence length $N$.
```

中文回译：

这种加性连接保留DSConv-S提取的局部退化特征，并将其与RAA建立的跨位置上下文结合，形成局部—全局联合表示，同时保持关于序列长度N的线性计算复杂度。

| 检查 | 结论 |
|---|---|
| ① 漏/增/改义 | 本块语义对应；未发现实质漏译或无依据增译。 |
| ② 术语/数字/条件 | 加性融合与关于N线性对应；符号与具体值以本块精确中英及下文公式核验为准，未见译中改变。 |
| ③ 自然/简洁 | 表达可读，语法与动作衔接成立；未发现需修正的明显中文直译痕迹。 |
| ④ 强度/复杂词 | 未发现英译新增夸大、绝对化或无必要复杂词；专业名称不因长度判错。 |
| ⑤ 范文语境 | BMSFormer §3.1 L735–746提供融合模块数据流语境；Engineering-AI §4.2.1 L875–884提供局部分支与全局上下文词汇。本文加性融合、Wa和Dropout为所需适配。 |

处理：语义一致，无须因回译措辞不同而修改。

## 公式与受保护内容

下列公式块经逐字符比较，中英一致（包括内部标签、大小写、下标、括号、标点及LaTeX命令）。文字说明的科学含义已在逐块记录中检查，公式一致本身不证明科学命题在所有条件下成立。

### M02-E01 — 中文与英文公式相同

源及目标章文件 L5 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathrm{SOH}=\frac{C_{\mathrm{current}}}{C_{\mathrm{rated}}}\times100\%,
\end{equation}
```

### M02-E02 — 中文与英文公式相同

源及目标章文件 L54 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
CCCT(V_1,V_2)=t(V_2)-t(V_1),
\end{equation}
```

### M02-E03 — 中文与英文公式相同

源及目标章文件 L62 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
IC=\frac{dQ}{dV}\approx\frac{Q_{k+N}-Q_k}{V_{k+N}-V_k},
\end{equation}
```

### M02-E04 — 中文与英文公式相同

源及目标章文件 L70 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
DTV=\frac{dT}{dV}\approx\frac{T_{k+N}-T_k}{V_{k+N}-V_k},
\end{equation}
```

### M02-E05 — 中文与英文公式相同

源及目标章文件 L78 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
DTC=\frac{dT}{dQ}\approx\frac{T_{k+N}-T_k}{Q_{k+N}-Q_k},
\end{equation}
```

### M02-E06 — 中文与英文公式相同

源及目标章文件 L86 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
Q_{\mathrm{dch}}(V_h,V_l)=\frac{1}{3600}\int_{\{t:\,V_l\leq V_{\mathrm{dch}}(t)\leq V_h\}}\left|I_{\mathrm{dch}}(t)\right|\,dt,
\end{equation}
```

### M02-E07 — 中文与英文公式相同

源及目标章文件 L94 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\eta=\frac{E_{\mathrm{dch}}}{E_{\mathrm{ch}}}=\frac{\int_0^{t_{\mathrm{dch}}}V_{\mathrm{dch}}(t)\left|I_{\mathrm{dch}}(t)\right|\,dt}{\int_0^{t_{\mathrm{ch}}}V_{\mathrm{ch}}(t)\left|I_{\mathrm{ch}}(t)\right|\,dt},
\end{equation}
```

### M02-E08 — 中文与英文公式相同

源及目标章文件 L110 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\gamma_{i,j}=
\frac{\displaystyle\sum_{k=1}^{n_j}(f_{i,j,k}-\bar{f}_{i,j})(y_{j,k}-\bar{y}_j)}
     {\displaystyle\sqrt{\sum_{k=1}^{n_j}(f_{i,j,k}-\bar{f}_{i,j})^2\sum_{k=1}^{n_j}(y_{j,k}-\bar{y}_j)^2}},
\end{equation}
```

### M02-E09 — 中文与英文公式相同

源及目标章文件 L116 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\rho_{i,j}=
\frac{\displaystyle\sum_{k=1}^{n_j}\bigl(R(f_{i,j,k})-\bar{R}(f_{i,j})\bigr)\bigl(R(y_{j,k})-\bar{R}(y_j)\bigr)}
{\displaystyle\sqrt{\sum_{k=1}^{n_j}\bigl(R(f_{i,j,k})-\bar{R}(f_{i,j})\bigr)^2\sum_{k=1}^{n_j}\bigl(R(y_{j,k})-\bar{R}(y_j)\bigr)^2}},
\end{equation}
```

### M02-E10 — 中文与英文公式相同

源及目标章文件 L126 起；回译不适用，数学内容原样保护。

```latex
\begin{equation*}
mPCC_i=\min_{j\in\mathcal{B}}|\gamma_{i,j}|,\qquad
mSCC_i=\min_{j\in\mathcal{B}}|\rho_{i,j}|.
\end{equation*}
```

### M02-E11 — 中文与英文公式相同

源及目标章文件 L133 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
S_i=\min(mPCC_i,mSCC_i).
\end{equation}
```

### M03-E01 — 中文与英文公式相同

源及目标章文件 L11 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf X_l'
=
\operatorname{SLFA}(\mathbf X_l).
\label{eq:block_slfa}
\end{equation}
```

### M03-E02 — 中文与英文公式相同

源及目标章文件 L20 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf X_l''
=
\mathbf X_l'
+
W_l
\operatorname{DSConv\text{-}L}
\left(
\operatorname{LN}(\mathbf X_l')
\right).
\label{eq:block_dsconv_l}
\end{equation}
```

### M03-E03 — 中文与英文公式相同

源及目标章文件 L35 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Y_l
=
\mathbf X_l''+
\operatorname{FFN}
\left(
\operatorname{LN}_0(\mathbf X_l'')
\right).
\label{eq:block_ffn}
\end{equation}
```

### M03-E04 — 中文与英文公式相同

源及目标章文件 L59 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
C_{\mathrm{Conv}}
=
k\times k\times C_{\mathrm{in}}\times C_{\mathrm{out}}\times D_F\times D_F.
\label{eq:conv_cost}
\end{equation}
```

### M03-E05 — 中文与英文公式相同

源及目标章文件 L70 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
C_{\mathrm{DSConv}}
=
k\times k\times C_{\mathrm{in}}\times D_F\times D_F
+
C_{\mathrm{in}}\times C_{\mathrm{out}}\times D_F\times D_F.
\label{eq:dsconv_cost}
\end{equation}
```

### M03-E06 — 中文与英文公式相同

源及目标章文件 L81 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\begin{aligned}
\frac{C_{\mathrm{DSConv}}}{C_{\mathrm{Conv}}}
&=
\frac{
k\times k\times C_{\mathrm{in}}\times D_F\times D_F
+
C_{\mathrm{in}}\times C_{\mathrm{out}}\times D_F\times D_F
}{
k\times k\times C_{\mathrm{in}}\times C_{\mathrm{out}}\times D_F\times D_F
} \\
&=
\frac{1}{C_{\mathrm{out}}}
+
\frac{1}{k^2}.
\end{aligned}
\label{eq:dsconv_cost_ratio}
\end{equation}
```

### M03-E07 — 中文与英文公式相同

源及目标章文件 L112 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Y_1
=
\operatorname{PW}_{\uparrow}
\left(
\mathcal T(\mathbf X)
\right)
\in\mathbb R^{B\times 2d\times N}.
\end{equation}
```

### M03-E08 — 中文与英文公式相同

源及目标章文件 L124 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Y_2
=
\operatorname{DW}_{5}(\mathbf Y_1)
\in\mathbb R^{B\times 2d\times N}.
\end{equation}
```

### M03-E09 — 中文与英文公式相同

源及目标章文件 L133 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Y_3
=
\operatorname{ReLU}(\mathbf Y_2).
\end{equation}
```

### M03-E10 — 中文与英文公式相同

源及目标章文件 L141 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Y_4
=
\operatorname{PW}_{\downarrow}(\mathbf Y_3)
\in\mathbb R^{B\times d\times N}.
\end{equation}
```

### M03-E11 — 中文与英文公式相同

源及目标章文件 L150 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf X_S
=
\operatorname{DSConv\text{-}S}(\mathbf X)
=
\mathbf X+\mathcal T^{-1}(\mathbf Y_4).
\label{eq:dsconv_s}
\end{equation}
```

### M03-E12 — 中文与英文公式相同

源及目标章文件 L163 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
C_{\mathrm{in}}\times2C_{\mathrm{out}}\times D_F\times D_F
+1\times5\times2C_{\mathrm{out}}\times D_F\times D_F
+2C_{\mathrm{out}}\times C_{\mathrm{out}}\times D_F\times D_F.
\label{eq:dsconv_s_expanded_cost}
\end{equation}
```

### M03-E13 — 中文与英文公式相同

源及目标章文件 L178 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
C_{\mathrm{in}}\times3C_{\mathrm{out}}\times D_F\times D_F
+1\times31\times3C_{\mathrm{out}}\times D_F\times D_F
+3C_{\mathrm{out}}\times C_{\mathrm{out}}\times D_F\times D_F.
\label{eq:dsconv_l_expanded_cost}
\end{equation}
```

### M03-E14 — 中文与英文公式相同

源及目标章文件 L198 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Q_i=\mathbf X\mathbf W_i^Q,\qquad
\mathbf K_i=\mathbf X\mathbf W_i^K,\qquad
\mathbf V_i=\mathbf X\mathbf W_i^V.
\label{eq:qkv_projection}
\end{equation}
```

### M03-E15 — 中文与英文公式相同

源及目标章文件 L209 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf O_{i,p}
=
\frac{
\displaystyle\sum_{j=1}^{N}
\operatorname{Sim}\left(\mathbf Q_{i,p},\mathbf K_{i,j}\right)\mathbf V_{i,j}
}{
\displaystyle\sum_{j=1}^{N}
\operatorname{Sim}\left(\mathbf Q_{i,p},\mathbf K_{i,j}\right)
},
\qquad p=1,2,\ldots,N.
\label{eq:general_attention}
\end{equation}
```

### M03-E16 — 中文与英文公式相同

源及目标章文件 L231 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf O_i
=
\operatorname{Softmax}
\left(
\frac{\mathbf Q_i\mathbf K_i^{\mathrm T}}{\sqrt{d_h}}
\right)
\mathbf V_i.
\label{eq:softmax_attention}
\end{equation}
```

### M03-E17 — 中文与英文公式相同

源及目标章文件 L246 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf O_i
=
\frac{
\phi(\mathbf Q_i)
\left[
\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i
\right]
}{
\phi(\mathbf Q_i)
\left[
\phi(\mathbf K_i)^{\mathrm T}\mathbf 1
\right]
}.
\label{eq:linear_attention}
\end{equation}
```

### M03-E18 — 中文与英文公式相同

源及目标章文件 L279 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf Q_i=\operatorname{Split}_i(\mathbf X\odot\mathbf s_q),\quad
\mathbf K_i=\operatorname{Split}_i(\mathbf X\odot\mathbf s_k),\quad
\mathbf V_i=\operatorname{Split}_i(\mathbf X\odot\mathbf s_v).
\label{eq:raa_qkv_scaling}
\end{equation}
```

### M03-E19 — 中文与英文公式相同

源及目标章文件 L296 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\left[\mathcal R_2(\mathbf Z)\right]_{r,c}
=
\begin{cases}
\dfrac{\operatorname{ReLU}(\mathbf Z_{r,c})^2}
{\sum_{j=1}^{M}\operatorname{ReLU}(\mathbf Z_{r,j})^2},
&
\sum_{j=1}^{M}\operatorname{ReLU}(\mathbf Z_{r,j})^2>0,\\[10pt]
\dfrac{1}{M},
&
\sum_{j=1}^{M}\operatorname{ReLU}(\mathbf Z_{r,j})^2=0.
\end{cases}
\label{eq:relu2_normalization}
\end{equation}
```

### M03-E20 — 中文与英文公式相同

源及目标章文件 L315 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\boldsymbol{\Phi}_{k,i}
=
\mathcal R_2
\left(
\frac{\mathbf A_i\mathbf K_i^{\mathrm T}}{\sqrt{d_h}}
\right),
\qquad
\mathbf V_{A,i}
=
\boldsymbol{\Phi}_{k,i}\mathbf V_i.
\label{eq:agent_aggregation}
\end{equation}
```

### M03-E21 — 中文与英文公式相同

源及目标章文件 L333 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\boldsymbol{\Phi}_{q,i}
=
\mathcal R_2
\left(
\frac{\mathbf Q_i\mathbf A_i^{\mathrm T}}{\sqrt{d_h}}
\right),
\qquad
\mathbf O_i
=
\boldsymbol{\Phi}_{q,i}\mathbf V_{A,i}.
\label{eq:agent_broadcast}
\end{equation}
```

### M03-E22 — 中文与英文公式相同

源及目标章文件 L353 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\operatorname{RAA}(\mathbf X)
=
\mathbf X+
\operatorname{Concat}(\mathbf O_1,\ldots,\mathbf O_h)\odot\mathbf s_o.
\label{eq:raa_output}
\end{equation}
```

### M03-E23 — 中文与英文公式相同

源及目标章文件 L369 起；回译不适用，数学内容原样保护。

```latex
\begin{equation}
\mathbf X_F
=
\operatorname{LN}(\mathbf X_S)
+
W_a
\operatorname{Dropout}
\left(
\operatorname{RAA}(\mathbf X_S)
\right).
\label{eq:slfa_fusion}
\end{equation}
```

## 问题汇总与待作者决定项

| 编号 | 分类 | 发现及最小处理 |
|---|---|---|
| M02-039 | 交叉复核后降为可选表达 | 可避免→preventing在设计功能语境合理；can可显式表达能力，不是必须修正的错译。 |
| M02-021 | 可选消歧 | continuous change→ongoing change，减少数学连续性联想。 |
| M02-023 | 可选自然度 | charge timing features→charging time features，避免充电时机联想。 |
| M02-029 | 可选消歧 | 明确对时间积分且以电压区间限制；现有dt公式与后文已消歧。 |
| M02-032 | 可选语法 | 两组三符号的and链可更清楚，含义没有丢失。 |
| M03-057 | 可选数学措辞 | 可明确乘以同一(0,1)正因子；当前总体缩小含义成立。 |
| M02-035 | 中文源表述待核 | “PCC仅对线性变化敏感”不宜误读为非线性数据必零相关；英文忠实，非新增误译。 |
| M03-016 | 中文源适用条件待核 | 1/Cout+1/k²<1并非所有同通道配置都成立；例如k=1不成立。 |
| M03-028、M03-032 | 中文源记号待核 | 一维序列N与DF×DF二维面积成本记号关系未说明。 |
| M02-012、M02-014 | 已批准并生效 | Aging records from cycling tests on已修正，不再报告旧 cycling aging records。 |

除这些项目外，未识别出需要改写第二、三章正文的明确语义错误。完整保留两章各段技术信息、15项HI对应、阈值逻辑文字、窗口数值、各张量维度与复杂度范围；图表外部文件和原始数据真实性由主报告分别列范围，不在本册宣称重新核实。

本册建议尚未写入正文。标题/纯说明块计入覆盖分母，独立公式另计；第二章50/50文字块、11/11公式，第三章70/70文字块、23/23公式。

末次核验记录：本审查过程中chapter03.tex L288发生并发更新；M03-054已重新读取并同步末次磁盘英文与回译。旧句以approximately 3d² parameters作为比较项，新句明确比较standard linear projections与channel scaling vectors；当前句比较对象更清楚。该正文变化不是本审查agent实施，批准归属由主审统一核对。
