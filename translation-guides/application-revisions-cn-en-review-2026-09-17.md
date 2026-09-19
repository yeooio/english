# 注意力与卷积应用解释：中文成果及当前英文对应核对

> 状态更新：本文件保留提案时的历史状态。其中补充建议及两处精简现已落实，见[最新落实记录](D:/MS-AgentNet-English/translation-guides/application-supplement-applied-2026-09-17.md)。下文“待审/未执行”是历史记录，不再代表当前状态。

日期：2026-09-17。审查对象：当前 chapters/ 英文工作稿。本文件为整理与建议，不是新一轮正文修改记录。

## 1. 本次结论与版本更正

**前面的工作没有丢失：8 处确认内容都能在当前英文中逐字找到。原位置可继续使用，不需要重新插入。** 以下“历史改前”取自当时修改前快照，“当前英文”取自已落实记录并逐字校验现稿；不能把历史改前误认成当前仍待修改的正文。

中文内容来自作者已确认的修改记录，用于核对本轮意图；不以冻结中文旧稿替代当前英文。后续判断以现英文上下文和实际结构为准。

当前英文各章没有“序列长度为 5”“窗口长度为 5”或 N=5 的设置。DSConv-S 的 1×5 及 S5 是卷积核大小，five models 是五种模型。冻结中文中那项已被作者删除的设置，不再用于要求当前英文联动修改。

撤回以旧长度设置为依据提出的摘要、架构、标题、贡献、方法、结论六处必须联动修改的要求。这不等于用删除文字证明某项模块效果；本轮不据此新增时间尺度结论，也不对原有表述作无依据的整体删改。

## 2. 八处成果与位置总表

|编号|位置|现状|处理|
|---|---|---|---|
|1|[引言贡献第（2）点](D:/MS-AgentNet-English/chapters/chapter01.tex:46)|已落实|保留，不重复插入|
|2|[§3.2 卷积模块引入](D:/MS-AgentNet-English/chapters/chapter03.tex:52)|已落实|保留，不重复插入|
|3|[§3.2.2 DSConv-S：输入增强](D:/MS-AgentNet-English/chapters/chapter03.tex:106)|已落实|保留，不重复插入|
|4|[§3.2.2 DSConv-S：局部分支保留](D:/MS-AgentNet-English/chapters/chapter03.tex:108)|已落实|保留；另有可选精简|
|5|[§3.2.3 DSConv-L：融合后特征处理](D:/MS-AgentNet-English/chapters/chapter03.tex:174)|已落实|保留；另有可选精简|
|6|[§3.3.2 末段：线性注意力转入应用需求](D:/MS-AgentNet-English/chapters/chapter03.tex:267)|已落实|保留，不重复插入|
|7|[§3.3.3 LGFA 引入](D:/MS-AgentNet-English/chapters/chapter03.tex:271)|已落实|保留，不重复插入|
|8|[结论：网络设计概括句](D:/MS-AgentNet-English/chapters/chapter05.tex:1)|已落实|保留，不重复插入|

## 3. 完整中文—历史英文—当前英文对照

以下英文保留 LaTeX 标记，方便定位和逐字复核。结论条目只覆盖已批准的网络概括句，不改同段的健康指标与复杂度说明。

### 1. 引言贡献第（2）点

位置：[chapters/chapter01.tex:46](D:/MS-AgentNet-English/chapters/chapter01.tex:46)。

**位置与句子作用：** 保留加粗贡献小标题；正文说明设计与电池退化表征的关系，不在此展开全部内部机制。

**前接现稿：**

(1) \textbf{A multi-source health indicator extraction and optimization algorithm is proposed.} The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. MS-CCCT then calibrates the voltage window for the charging-time feature. The algorithm uses correlation results from the feature-development cells to evaluate each candidate's association with SOH and its redundancy with other indicators. It then applies PCC and SCC thresholds and redundancy constraints to select the indicators. The same selection rules determine a final HI subset for each dataset, and the selected indicators retain strong linear and monotonic correlations with SOH on other cells in that dataset.

**已确认中文：**

构建轻量级局部—全局网络 MS-AgentNet。局部—全局融合注意力（LGFA）模块结合小核深度可分离卷积与 ReLU² 智能体注意力，以较低参数开销将局部特征提取与全局上下文建模相结合。相较于标准自注意力，其注意力计算复杂度关于序列长度由 O(N²) 降低至 O(N)。模型进一步引入大核深度可分离卷积，与小核卷积共同提取不同时间尺度的退化特征。这些设计旨在增强模型对长期退化趋势和短期容量波动的表征能力，在控制计算与存储开销的同时提高 SOH 估计精度。

**历史改前英文（已被替换）：**

```tex
(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} A Local-Global Fusion Attention (LGFA) module combines small-kernel depthwise separable convolutions with ReLU$^2$ agent attention. It extracts local degradation features, captures long-term dependencies, and fuses the resulting representations with low parameter overhead. The attention mechanism reduces computational complexity from $O(N^2)$ to $O(N)$. The model further introduces large-kernel depthwise separable convolutions, which, together with small-kernel convolutions, extract degradation features at different time scales. These designs integrate local feature extraction and global information interaction into a compact network structure, improving SOH estimation accuracy while reducing computational and storage overhead.
```

**当前英文（修改已落实）：**

```tex
(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} A Local-Global Fusion Attention (LGFA) module combines small-kernel depthwise separable convolutions with ReLU$^2$ agent attention to integrate local feature extraction and global context modeling with low parameter overhead. Compared with standard self-attention, its attention computation reduces the complexity with respect to sequence length from $O(N^2)$ to $O(N)$. The model further introduces large-kernel depthwise separable convolutions, which, together with small-kernel convolutions, extract degradation features at different time scales. These designs aim to enhance the model's representation of long-term degradation trends and short-term capacity fluctuations and improve SOH estimation accuracy while limiting computational and storage overhead.
```

**后接现稿：**

(3) \textbf{Comprehensive validation is conducted across multiple datasets.} Experiments on multiple public battery datasets with different chemistries, capacities, and charge-discharge protocols, together with module ablation and complexity analysis, provide a comprehensive evaluation of the proposed method in terms of estimation accuracy, computational efficiency, and cross-cell generalization capability. Cross-dataset transfer experiments further examine the model's cross-domain adaptation capability. The results show that the proposed model maintains high SOH estimation accuracy with low computational and storage overhead.

**范文对应与复用边界：** JESSOHRUL introduction.txt:269–286；conclusion.txt:62–78。借用设计→应用能力的收束，不迁入秩补偿或 RUL 任务。

### 2. §3.2 卷积模块引入

位置：[chapters/chapter03.tex:52](D:/MS-AgentNet-English/chapters/chapter03.tex:52)。

**位置与句子作用：** 保留作者亲自选定的两句；先说能力与效率，再预告计算分析和两个模块。

**前接现稿：**

\subsection{The designed multi-scale depthwise separable convolution modules}

**已确认中文：**

为平衡特征提取能力与计算效率，采用大小核深度可分离卷积捕获多尺度局部依赖，在增强特征多样性的同时控制参数开销。本节首先介绍标准卷积与深度可分离卷积的计算特性，随后说明 DSConv-S 和 DSConv-L 的结构配置及作用。

**历史改前英文（已被替换）：**

```tex
To combine multi-scale local feature extraction with computational efficiency, this section first introduces the basic structure of DSConv and compares its computational cost with that of standard convolution. The configurations and respective roles of DSConv-S and DSConv-L are then described.
```

**当前英文（修改已落实）：**

```tex
To balance feature extraction capability and computational efficiency, small- and large-kernel depthwise separable convolutions are used to capture multi-scale local dependencies, enhancing feature diversity while limiting parameter overhead. This section first introduces the computational characteristics of standard and depthwise separable convolutions, followed by the configurations and roles of DSConv-S and DSConv-L.
```

**后接现稿：**

\subsubsection{Basic DSConv structure and computational cost comparison}

**范文对应与复用边界：** JESSOHRUL methodology.txt:519–586。借用能力/效率并列、multi-scale local dependencies 与 rich representations；本稿大小核配置来自自身结构。

### 3. §3.2.2 DSConv-S：输入增强

位置：[chapters/chapter03.tex:106](D:/MS-AgentNet-English/chapters/chapter03.tex:106)。

**位置与句子作用：** 保留：健康指标相邻循环表示→通道内局部提取与跨通道整合→RAA 使用所得表示。

**前接现稿：**

Small-kernel DSConv-S uses a compact $1\times5$ depthwise convolution and is embedded in LGFA before the global interactions in RAA. It serves two roles: input enhancement and local branch preservation:

**已确认中文：**

输入增强。为提取健康指标序列中的细粒度退化信息，DSConv-S 对相邻循环的特征表示进行局部建模，形成局部增强表示 X_S。其中，深度卷积提取各通道内的局部依赖，逐点卷积整合不同通道的特征。RAA 随后基于 X_S 构造查询、键和值，并通过智能体聚合与广播建立循环间关联，使上下文聚合能够利用卷积提取的局部变化信息。

**历史改前英文（已被替换）：**

```tex
1. \textbf{Input enhancement.} DSConv-S extracts local neighborhood information from the input features to form a locally enhanced representation $\mathbf X_S$. RAA then constructs queries, keys, and values from $\mathbf X_S$ and performs cross-position interactions through agent aggregation and broadcasting. This preceding convolution introduces a locality bias into RAA, improving its representation of local variations during cross-position context aggregation.
```

**当前英文（修改已落实）：**

```tex
1. \textbf{Input enhancement.} To extract fine-grained degradation information from health indicator sequences, DSConv-S models local relationships between the feature representations of neighboring cycles to form a locally enhanced representation $\mathbf X_S$. Depthwise convolution extracts local dependencies within each channel, while pointwise convolution integrates features across channels. RAA then constructs queries, keys, and values from $\mathbf X_S$ and establishes relationships across cycles through agent aggregation and broadcasting, allowing context aggregation to use the local variation information extracted by convolution.
```

**后接现稿：**

2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is carried by the local branch to the fusion stage, where it is added to the RAA branch output. This path passes the locally enhanced health indicator representation directly to the fusion stage, combining it with the global context established by RAA to form a joint local-global representation for SOH estimation.

**范文对应与复用边界：** JESSOHRUL methodology.txt:315–346；BMSFormer methodology.txt:645–657。卷积提取→跨通道整合→卷积增强后注意力；RAA 的 Q/K/V 关系来自本文。

### 4. §3.2.2 DSConv-S：局部分支保留

位置：[chapters/chapter03.tex:108](D:/MS-AgentNet-English/chapters/chapter03.tex:108)。

**位置与句子作用：** 已落实，可选精简：路径说明与融合用途分开，避免两次说送至融合端。

**前接现稿：**

1. \textbf{Input enhancement.} To extract fine-grained degradation information from health indicator sequences, DSConv-S models local relationships between the feature representations of neighboring cycles to form a locally enhanced representation $\mathbf X_S$. Depthwise convolution extracts local dependencies within each channel, while pointwise convolution integrates features across channels. RAA then constructs queries, keys, and values from $\mathbf X_S$ and establishes relationships across cycles through agent aggregation and broadcasting, allowing context aggregation to use the local variation information extracted by convolution.

**已确认中文：**

局部分支保留。在进行循环间信息交互的同时，X_S 还经层归一化后由局部分支传递至融合端，并与 RAA 分支输出相加。这一路径将局部增强后的健康指标表示直接送入融合端，与 RAA 建立的全局上下文共同形成 SOH 估计所需的局部—全局联合表征。

**历史改前英文（已被替换）：**

```tex
2. \textbf{Local branch preservation.} In LGFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

**当前英文（修改已落实）：**

```tex
2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is carried by the local branch to the fusion stage, where it is added to the RAA branch output. This path passes the locally enhanced health indicator representation directly to the fusion stage, combining it with the global context established by RAA to form a joint local-global representation for SOH estimation.
```

**后接现稿：**

DSConv-S uses a channel expansion factor of two. The input features are $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively. The input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:

**范文对应与复用边界：** Engineering-AI methodology.txt:808–840；JESSOHRUL methodology.txt:338–346。范文也分别说明局部增强与融合，不能因重复概念就删除；不借用 rank restoration。

### 5. §3.2.3 DSConv-L：融合后特征处理

位置：[chapters/chapter03.tex:174](D:/MS-AgentNet-English/chapters/chapter03.tex:174)。

**位置与句子作用：** 已落实；通道扩展、深度卷积、通道恢复、缩放残差及 SOH 用途都应保留。残差说明可选合并。

**前接现稿：**

\subsubsection{DSConv-L: Feature refinement over longer time scales}

**已确认中文：**

DSConv-L 位于 LGFA 之后，用于进一步细化已融合局部信息与全局上下文的特征表示。该模块通过 1×1 逐点卷积将通道维度扩展至三倍，以提取丰富的表征，随后采用 1×31 深度卷积在各通道内捕获较长时间尺度的局部序列模式。第二个 1×1 逐点卷积跨通道整合这些特征，并恢复原始通道维度。整体变换顺序与 DSConv-S 一致，残差连接在 MS-AgentNet Block 层面实现，如相应公式所示。卷积输出经可学习系数缩放后，与原有 LGFA 输出相加，将进一步提取的序列特征融入已有表示。通过注意力前的局部增强与融合后的特征细化，大小核卷积共同丰富用于 SOH 估计的多尺度退化表征。

**历史改前英文（已被替换）：**

```tex
DSConv-L follows LGFA and uses a channel expansion factor of three and a $1\times31$ depthwise convolution to extract degradation features over longer time scales from the fused representation. Two $1\times1$ pointwise convolutions expand and restore the channel dimension, respectively, following the same transformation order as DSConv-S. Its residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}.
```

**当前英文（修改已落实）：**

```tex
DSConv-L follows LGFA to further refine the feature representation that combines local information and global context. A $1\times1$ pointwise convolution first expands the channel dimension by a factor of three to extract rich representations, followed by a $1\times31$ depthwise convolution that captures local sequence patterns over longer time scales within each channel. A second $1\times1$ pointwise convolution integrates these features across channels and restores the original channel dimension. The transformation order is the same as in DSConv-S, and the residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}. The convolution output is scaled by a learnable factor and added to the original LGFA output, incorporating the further extracted sequence features into the existing representation. Through local enhancement before attention and feature refinement after fusion, the small- and large-kernel convolutions jointly enrich multi-scale degradation representations for SOH estimation.
```

**后接现稿：**

\textbf{Computational analysis.} With a channel expansion factor of three, the computational cost of DSConv-L can be expressed as:

**范文对应与复用边界：** JESSOHRUL methodology.txt:519–586；BMSFormer methodology.txt:594–603；Engineering-AI methodology.txt 的 Lconv 后融合处理。沿用操作→所得表征，不将范文的时间范围作为本文验证证据。

### 6. §3.3.2 末段：线性注意力转入应用需求

位置：[chapters/chapter03.tex:267](D:/MS-AgentNet-English/chapters/chapter03.tex:267)。

**位置与句子作用：** 保留：前段解释线性复杂度，本段补应用需求，下段自然引出 LGFA。

**前接现稿：**

By first calculating $\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$, linear attention avoids constructing the full $N\times N$ attention matrix. When the feature mapping dimension equals $d_h$, its computational complexity is $O(Nd_h^2)$. For a fixed $d_h$, this complexity is linear in the sequence length $N$.

**已确认中文：**

上述线性注意力通过重组计算顺序降低了全局信息交互的开销，但其计算过程未显式引入局部邻域特征。在电池 SOH 估计中，健康指标序列不仅包含退化趋势，也包含相邻循环的局部变化。模型在建立循环间依赖关系时，仍需充分利用其中的细粒度退化信息。因此，有必要将局部特征提取与高效注意力机制相结合，在控制计算开销的同时增强对电池退化过程的表征。

**历史改前英文（已被替换）：**

```tex
Linear attention enables global information interactions at a lower computational complexity, but its computation does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref64}. Joint modeling of cross-position interactions and local features is therefore needed.
```

**当前英文（修改已落实）：**

```tex
The linear attention described above reduces the cost of global information interactions by rearranging the computation order, but it does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref64}. In battery SOH estimation, health indicator sequences contain both degradation trends and local variations between neighboring cycles. When modeling dependencies across cycles, the model still needs to make full use of the fine-grained degradation information in these sequences. Local feature extraction therefore needs to be combined with an efficient attention mechanism to enhance the representation of battery degradation while limiting computational overhead.
```

**后接现稿：**

\subsubsection{The proposed LGFA module}

**范文对应与复用边界：** JESSOHRUL methodology.txt 的 DSCA 引入与卷积增强；BMSFormer methodology.txt:630–645。按全局处理→局部需求→模块引入衔接。

### 7. §3.3.3 LGFA 引入

位置：[chapters/chapter03.tex:271](D:/MS-AgentNet-English/chapters/chapter03.tex:271)。

**位置与句子作用：** 保留：说明两个分支的输入来源、各自处理与融合用途；不能只留模块清单。

**前接现稿：**

\subsubsection{The proposed LGFA module}

**已确认中文：**

为兼顾退化特征提取与计算效率，本文将小核深度可分离卷积 DSConv-S 与 ReLU² 智能体注意力（RAA）相结合，构建局部—全局融合注意力（LGFA）模块，如图 3-3(d) 所示。DSConv-S 增强健康指标序列的输入表征，在保留序列结构的同时丰富局部信息，所得表示分别进入局部分支与 RAA 分支。局部分支将局部增强表示直接传递至融合端，RAA 分支则基于这一表示进行全局上下文建模。两个分支的输出经加法融合，为 SOH 估计提供兼顾局部退化细节与全局上下文的特征表示。

**历史改前英文（已被替换）：**

```tex
To capture both local neighborhood features and cross-position interactions, this study combines DSConv-S with the developed ReLU² Agent Attention (RAA) to form the LGFA module, as shown in \cref{fig:3-3}(d). The module fuses a local branch with an RAA branch: DSConv-S first extracts a local representation, and RAA then uses this representation to establish cross-position feature interactions. The outputs of the two branches are fused by addition.
```

**当前英文（修改已落实）：**

```tex
To balance degradation feature extraction and computational efficiency, this study combines small-kernel depthwise separable convolution (DSConv-S) with ReLU² Agent Attention (RAA) to form the Local-Global Fusion Attention (LGFA) module, as shown in \cref{fig:3-3}(d). DSConv-S enhances the input representation of health indicator sequences by enriching local information while preserving the sequence structure. The resulting representation is fed into both the local and RAA branches. The local branch passes the locally enhanced representation directly to the fusion stage, while the RAA branch uses it to model global context. The outputs of the two branches are fused by addition to provide SOH estimation with a feature representation that incorporates both local degradation details and global context.
```

**后接现稿：**

\textbf{(1) ReLU² Agent Attention.}

**范文对应与复用边界：** JESSOHRUL methodology.txt:315–346；Engineering-AI methodology.txt:808–840。先解释卷积增强所得表示，再解释注意力及融合，不照搬其独有秩结论。

### 8. 结论：网络设计概括句

位置：[chapters/chapter05.tex:1](D:/MS-AgentNet-English/chapters/chapter05.tex:1)。

**位置与句子作用：** 已落实，原位置可复用；不误标为尚未修改，不重复新增一条结论。

**前接现稿：**

This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-constrained battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset.

**已确认中文：**

在序列建模方面，MS-AgentNet 将 ReLU² 智能体注意力与大小核深度可分离卷积相结合，通过局部特征提取与全局上下文建模，增强对局部退化变化和较长时间尺度退化趋势的表征能力。

**历史改前英文（已被替换）：**

```tex
For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales.
```

**当前英文（修改已落实）：**

```tex
For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to enhance the representation of local degradation variations and degradation trends over longer time scales through local feature extraction and global context modeling.
```

**后接现稿：**

With a fixed number of agents, RAA uses a small number of static learnable agents for information aggregation and broadcasting, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.

**范文对应与复用边界：** JESSOHRUL conclusion.txt:62–78。设计组合→退化表征能力；本文保留 SOH 范围，不增添联合 RUL 任务。

## 4. 直接从范文英文提取的表达依据

下列短语本轮重新对照本地英文原文。它们是词语及句子功能依据，不代表范文实验替本文验证了效果。TXT 存在双栏交错，行号供定位；本文件不据相邻提取行另造连续原句，也未重新作完整句数统计。

|英文原词/搭配|范文位置|在本稿中承接什么|
|---|---|---|
|fine-grained local dependencies|[JESSOHRUL 方法](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:338)|通道内局部依赖；映射到健康指标序列时可说明细粒度退化信息|
|integrates these features across channels|[JESSOHRUL 方法](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:339)|逐点卷积整合前一步得到的特征|
|retains the sequential structure / enriching local information|[JESSOHRUL 方法](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:340)|交代所得表示保留结构并丰富局部信息|
|Following the convolutional enhancement|[JESSOHRUL 方法](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:342)|卷积所得表示接入后续注意力|
|capture local sequential patterns|[JESSOHRUL 方法](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:560)|DSConv-L 深度卷积处理融合表示中的序列模式|
|extract rich representations / multi-scale local dependencies|[JESSOHRUL 方法](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:581)|通道扩展与卷积处理的表征用途|
|long-term degradation patterns / short-term local capacity recovery|[JESSOHRUL 引言](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:285)|学习应用层面的收束；不据此指定本文某个核专门识别容量恢复|

**逐句作用对应：** JESS 卷积增强说明依次给出通道内提取、跨通道整合、所得表示、后续注意力；本文“输入增强”按同样的动作关系组织，并将对象明确为健康指标的相邻循环表示。JESS MBConv1 依次说明扩展、深度卷积、恢复及残差，再归纳表征用途；本文 DSConv-L 保留自己的配置和 Block 级残差，借用这一表达层次。

**颗粒度校准：** BMSFormer 同时在卷积与注意力小节说明局部输入增强；Engineering-AI 分开说明局部增强与加法融合。故本稿各小节重复提到“局部/全局”本身不是错误。只将同一段两次交代同一路径视为可选精简，不把还能更细或更短当作必须修改。

## 5. 当前英文仅有的两处可选精简（尚未执行）

这两项延续已有建议，不增加功能；作者可直接选择保留现稿。时间尺度用语不在这两项中暗改。

### A. 局部分支：压缩同一路径的重复说明

**现有英文：**

```tex
2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is carried by the local branch to the fusion stage, where it is added to the RAA branch output. This path passes the locally enhanced health indicator representation directly to the fusion stage, combining it with the global context established by RAA to form a joint local-global representation for SOH estimation.
```

**建议英文：**

```tex
2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is sent directly through the local branch to the fusion stage, where it is added to the RAA branch output. This path combines the locally enhanced health indicator representation with the global context established by RAA within the input window to form a joint local-global representation for SOH estimation.
```

**中文对应：** 在进行循环间信息交互的同时，X_S 经层归一化后由局部分支直接传递至融合端，并与 RAA 分支输出相加。这一路径将局部增强后的健康指标表示与 RAA 在输入窗口内建立的全局上下文相结合，形成用于 SOH 估计的局部—全局联合表征。

**原因：** 不是术语错误，而是同段重复说明送到融合端。第一句说路径，第二句说表示如何结合；输入窗口限定只出现一次。原位置与前后文均可复用。范文依据为上表及 Engineering-AI 双分支/融合语境，不迁入其秩恢复作用。

### B. DSConv-L：合并残差说明，其他内容保留

**只替换以下两句，整段其余句子不动：**

```tex
The transformation order is the same as in DSConv-S, and the residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}. The convolution output is scaled by a learnable factor and added to the original LGFA output, incorporating the further extracted sequence features into the existing representation.
```

**建议英文：**

```tex
The transformation order is the same as in DSConv-S. At the MS-AgentNet Block level, the convolution output is scaled by a learnable factor and added to the original LGFA output through a residual connection, incorporating the further extracted sequence features into the existing representation, as shown in Eq.~\eqref{eq:block_dsconv_l}.
```

**中文对应：** 整体变换顺序与 DSConv-S 一致。在 MS-AgentNet Block 层，卷积输出经可学习系数缩放后，通过残差连接与原有 LGFA 输出相加，将进一步提取的序列特征融入已有表示，如相应公式所示。

**原因：** 残差所在位置与具体运算集中交代。配置、可学习缩放、相加对象、表征补充与公式引用均保留。范文也会分别说明操作及用途，因此这只是可选组织调整，现稿可以保留。该建议不修改“较长时间尺度”，也不删去通道扩展的表征用途。

## 6. 不再加入或尚未落实的内容

- 引言新增轻量化研究段及缩短后的 Li 等一句：作者已撤回，不补回。原有模型综述后继续接健康指标综述。
- RAA 开头长篇解释、ReLU² 的额外应用理由：此前未批准落实，本次不作为完成项，不凭范文添加噪声抑制。
- 新增消融、实验设计、实验结果改写：仍暂缓。
- 摘要、整体架构与 DSConv-L 标题：当前保留，不因旧中文长度设置联动改写。
- 全文中英对照旧文件未同步：本文件保存的是本轮8处可核验成果，不宣称其他历史对照都已更新。
- LGFA 名称沿用当前英文；历史 SLFA 不重新引入。

## 7. 执行建议与核验

八处已落实内容全部保留；两个可选精简待作者审核。若批准，后续只在现有位置替换相应英文，保留公式、引用、参数及段落结构，再编译。当前任务只生成本核对文档，没有再次修改论文。

核验：8处已落实英文均在当前对应章节中唯一匹配；历史改前来自当日快照与 changes.json；生成文档前后 chapters/*.tex 的 SHA-256 一致。冻结中文未读作当前设置、未修改。
