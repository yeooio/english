# 全文中英对照记录

2026-09-13。依据作者“全自动，直到这篇论文全部翻译完毕”的授权完成。摘要及引言前两段为此前逐段批准版本；其余为本次整体授权下的译文，并非逐段另行批准。中文直接取自冻结 source-zh，英文取自当前 chapters；不改写中文。按空行划分的源文件块逐一匹配，含中文的块完整展示；公式或输入命令等两侧共用块不重复展示。某些源文件块包含连续的标题和正文，保留原有结构。

## 范文依据

以下中文均为助手释义，不是官方译文。三篇按段落功能使用，不为每段强行凑齐三篇，不照搬其结论。

- BMSFormer，p.4 §2.1：`A sliding window is then used`——“随后使用滑动窗口”；借鉴操作对象作主语和 then 的顺序连接。
- JESSOHRUL，p.13 §3.5.2：`the correlation between HIs and SOH`——“HI与SOH之间的相关性”；明确相关对象，不将健康指标写成SOH本身。
- Engineering-AI，p.7 §4.2：`parameter redundancy`——“参数冗余”；用于轻量化问题的直接表述，不扩大为已完成嵌入式部署。

原文位于 style-references 下对应论文文件夹。详细句级依据见 method-reference-analysis.md；全篇终检见 final-translation-review.md。

## abstract.tex

### 源文件块 1

中文原文：

```latex
高效准确的锂离子电池健康状态估计，对保障电池安全运行和支持资源受限电池管理系统的在线应用至关重要。然而，现有估计方法往往依赖跨电池稳定性有限的健康指标和资源开销较大的模型结构。为此，本文提出一种轻量化的SOH估计框架。首先，提出多源健康指标提取与优化算法，以筛选跨电池稳健的健康指标并减少特征冗余。随后，构建轻量化预测网络MS-AgentNet。该网络主要集成局部—全局融合注意力模块，通过小核深度可分离卷积与ReLU²智能体注意力协同捕获局部退化特征与长程退化依赖，同时将传统Transformer的二次注意力复杂度降至线性。此外，大核深度可分离卷积用于提取长尺度退化特征，并与小核卷积共同以较低参数开销融合多尺度和多通道特征，增强特征多样性。我们在四个涵盖不同化学体系和运行条件的公开电池数据集上，将所提模型与多种主流深度学习模型进行了比较。实验结果表明，MS-AgentNet总体上取得了更优的综合性能，同时保持了较低的计算与存储开销，进一步体现了其面向资源受限电池管理系统的轻量化优势。
```

英文译文：

```latex
Efficient and accurate estimation of lithium-ion battery state of health (SOH) is crucial for ensuring safe battery operation and supporting online applications in resource-constrained battery management systems (BMS). However, many existing SOH estimation approaches often rely on health indicators (HIs) with limited stability across cells and resource-consuming model structures. Therefore, this paper proposes a lightweight SOH estimation framework. First, a multi-source health indicator extraction and optimization algorithm is proposed to select HIs that are robust across cells and reduce feature redundancy. Subsequently, a lightweight prediction network, MS-AgentNet, is constructed. The network mainly integrates a Local-Global Fusion Attention (LGFA) module that combines small-kernel depthwise separable convolutions with ReLU² agent attention to capture local degradation features and long-term dependencies, while reducing the quadratic attention complexity of traditional Transformers to linear complexity. Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity. We compared the proposed model with various mainstream deep learning models on four public battery datasets with different chemistries and operating conditions. The experimental results show that MS-AgentNet achieves better overall performance while maintaining low computational and storage overhead, further highlighting the advantages of its lightweight design for resource-constrained BMS.
```

### 源文件块 2

中文原文：

```latex
\textbf{关键词：} 锂离子电池；健康状态估计；线性复杂度；深度特征融合；轻量化深度学习
```

英文译文：

```latex
\textbf{Keywords:} lithium-ion batteries; state-of-health estimation; linear complexity; deep feature fusion; lightweight deep learning
```

## chapter01.tex

### 源文件块 1

中文原文：

```latex
锂离子电池凭借高能量密度、长循环寿命和低自放电率等优势，已广泛应用于电动汽车、便携式电子设备和规模化储能等领域\cite{ref1,ref2,ref3,ref4}，是支撑新能源交通、智能终端和能源存储行业发展的重要储能技术。尽管如此，电池在长期运行中仍存在不可忽视的安全风险。充放电循环与复杂工况会引发固体电解质界面（solid electrolyte interphase, SEI）膜增厚、活性锂损失和电极结构衰退等老化现象\cite{ref5,ref6}，进而导致容量衰减和性能下降，严重时将诱发短路、热失控等故障\cite{ref7,ref8}。因此，精确估计锂离子电池的健康状态对于保障电池的安全性、可靠性和运行性能至关重要。
```

英文译文：

```latex
With high energy density, a long cycle life, and a low self-discharge rate, lithium-ion batteries have become one of the most important electrochemical energy storage technologies, widely used across consumer electronics, electric vehicles, stationary energy storage, and other domains\cite{ref1,ref2,ref3,ref4}. Nevertheless, lithium-ion batteries cannot always remain stable during long-term operation and continue to pose safety risks that cannot be overlooked. Charge-discharge cycling and complex operating conditions induce aging processes such as thickening of the solid electrolyte interphase (SEI) layer, loss of active lithium, and structural degradation of the electrodes\cite{ref5,ref6}. These processes, in turn, lead to capacity fade and performance degradation and, in severe cases, trigger failures such as short circuits and thermal runaway\cite{ref7,ref8}. Therefore, precise estimation of lithium-ion battery state of health (SOH) is essential for ensuring battery safety, reliability, and operational performance.
```

### 源文件块 2

中文原文：

```latex
容量衰减是电池老化最直观的特征，健康状态（state of health, SOH）通常采用容量保持率定义\cite{ref13,ref14}。但电池最大可用容量的精确测算需要完整或近似完整的充放电循环，难以满足在线监测需求\cite{ref10,ref11}。因此，从可观测运行信号中间接估计SOH已成为在线健康监测的关键途径。然而，复杂工况增加了退化信息稳定提取的难度，而电池管理系统（battery management system, BMS）严格的计算与存储限制又制约了模型复杂度，使在线SOH估计面临退化信息提取与模型计算效率的双重挑战\cite{ref31}。
```

英文译文：

```latex
Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurately measuring a battery's maximum available capacity requires full or nearly full charge-discharge cycles, which are impractical for online monitoring\cite{ref10,ref11}. Consequently, indirectly inferring SOH from observable operating signals has become a key approach to online battery health monitoring. Nevertheless, complex operating conditions make it harder to consistently extract degradation information, while the limited computing power and storage space of battery management systems (BMS) constrain model complexity. Together, these factors pose a dual challenge for online SOH estimation: degradation information extraction and the computational efficiency of estimation models\cite{ref31}.
```

### 源文件块 3

中文原文：

```latex
\subsection{文献综述}
```

英文译文：

```latex
\subsection{Literature review}
```

### 源文件块 4

中文原文：

```latex
近期的健康状态估计方法主要分为模型驱动和数据驱动两类\cite{ref10,ref11,ref12}。前者包括电化学模型和等效电路模型，后者包括传统机器学习和深度学习方法。
```

英文译文：

```latex
Recent approaches to SOH estimation can generally be classified as model-based or data-driven\cite{ref10,ref11,ref12}. The former include electrochemical models and equivalent circuit models, while the latter include traditional machine learning and deep learning methods.
```

### 源文件块 5

中文原文：

```latex
模型驱动方法通过数学方程或等效电路模拟电池内部的电化学机制\cite{ref19}。其中，电化学模型以微分方程表示电池的反应与退化过程。例如，Li等人\cite{ref21}基于单粒子模型（SPM），构建了同时考虑化学退化与机械损伤的SOH估计框架。虽然这类模型具有较好的物理可解释性和估计精度，但求解复杂方程需要较多计算资源，颗粒半径、扩散系数等参数也难以获取，限制了其在资源受限BMS中的在线应用\cite{ref20,ref22,ref23}。相比之下，等效电路模型（ECM）将复杂的电化学过程简化为由电阻、电容等元件组成的电路，以模拟电池充放电动态特性\cite{ref19}。例如，Chen等人\cite{ref24}采用递推最小二乘法辨识Thevenin模型参数，并根据欧姆内阻与容量衰减的关系估计SOH。这种简化降低了模型的计算开销，但也使其难以全面刻画电池内部状态的变化。与电化学模型相比，ECM的估计精度可能较低，且依赖于所选电路结构与模型参数。此外，ECM参数对温度和充放电倍率等工况高度敏感，使其难以在整个老化周期内保持良好的估计鲁棒性\cite{ref19}。
```

英文译文：

```latex
Model-based approaches simulate the internal electrochemical mechanisms of batteries using mathematical equations or equivalent circuits\cite{ref19}. Electrochemical models use differential equations to represent electrochemical reactions and degradation processes in batteries. For instance, Li et al.\cite{ref21} developed an SOH estimation framework based on a single-particle model (SPM), incorporating both chemical degradation and mechanical damage. Although these models are physically interpretable and can achieve high estimation accuracy, solving their complex equations requires extensive computational resources. In addition, parameters such as particle radius and diffusion coefficients are difficult to obtain. These limitations hinder the online application of electrochemical models in resource-constrained BMS\cite{ref20,ref22,ref23}. In contrast, equivalent circuit models (ECMs) simplify complex electrochemical processes into circuits composed of resistors, capacitors, and other components to simulate battery charge-discharge dynamics\cite{ref19}. For example, Chen et al.\cite{ref24} used recursive least squares to identify the parameters of a Thevenin model and estimated SOH based on the relationship between ohmic internal resistance and capacity fade. This simplification reduces computational cost, but it also limits the ability of ECMs to fully capture changes in the internal state of the battery. Compared with electrochemical models, ECMs may achieve lower estimation accuracy. Their accuracy depends on the selected circuit structure and model parameters. Furthermore, ECM parameters are highly sensitive to operating conditions, including temperature and charge-discharge rate, making it difficult for ECMs to maintain robust estimation performance throughout the battery aging process\cite{ref19}.
```

### 源文件块 6

中文原文：

```latex
相较于模型驱动方法，数据驱动方法无需建立详细的电化学模型或深入分析电池内部的反应及老化机制\cite{ref11,ref14}。这类方法利用历史运行数据训练模型，将提取的健康指标映射为SOH估计值。早期研究主要采用传统机器学习模型进行电池状态估计与寿命预测\cite{ref25}。例如，Fei等人\cite{ref26}从前100个循环的充放电数据中构造42个特征，经筛选后输入弹性网络、高斯过程回归（GPR）、支持向量机（SVM）、随机森林（RF）、梯度提升回归树（GBRT）和神经网络（NN）六种模型，比较其早期寿命预测表现。Li等人\cite{ref27}则利用局部充电过程中的电压和容量数据，通过随机森林实现在线容量估计。然而，当面对来自在线监测和历史循环的非线性、波动性数据时，传统机器学习模型因其结构限制而难以提供高性能。
```

英文译文：

```latex
In contrast, data-driven approaches avoid the need to develop detailed electrochemical models or extensively analyze electrochemical reactions and battery aging mechanisms\cite{ref11,ref14}. Instead, they train models on historical operating data to map extracted health indicators (HIs) to SOH estimates. Earlier studies primarily employed traditional machine learning models to estimate battery states and predict battery lifetime\cite{ref25}. For instance, Fei et al.\cite{ref26} crafted 42 features from charge--discharge data collected over the first 100 cycles. After feature selection, the retained features were fed into six models: elastic net, Gaussian process regression (GPR), support vector machine (SVM), random forest (RF), gradient boosting regression tree (GBRT), and neural network (NN). Their performance in the early prediction of battery lifetime was then compared. Li et al.\cite{ref27} used a random forest to estimate battery capacity online from partial charging voltage--capacity data. However, when faced with nonlinear and fluctuating data from online monitoring and historical cycling, traditional machine learning models struggle to achieve high predictive performance because of their structural limitations.
```

### 源文件块 7

中文原文：

```latex
随着深度学习的快速发展，研究者进一步采用多层神经网络，利用其较强的非线性表征能力捕捉复杂的电池退化模式，以提高估计精度\cite{ref14}。卷积神经网络（CNN）、循环神经网络（RNN）和Transformer是其中常用的模型。CNN利用卷积核提取局部特征，并通过池化操作降低特征维度。例如，Qian等人\cite{ref29}将随机选取的充电曲线片段输入一维CNN，用于电池容量估计。结果表明，该方法在随机片段输入条件下取得了较低的容量估计误差。Lee等人\cite{ref30}则将跨循环的容量衰减序列转换为二维图像，并采用二维CNN估计SOH。
```

英文译文：

```latex
With the rapid development of deep learning, researchers have increasingly adopted multilayer neural networks. These networks have strong nonlinear representational capacity and can therefore capture complex battery degradation patterns and improve estimation accuracy\cite{ref14}. Common deep learning models include convolutional neural networks (CNNs), recurrent neural networks (RNNs), and Transformers. CNNs extract local features using convolutional kernels and reduce feature dimensionality through pooling operations. For example, Qian et al.\cite{ref29} fed randomly selected charging-curve segments into a one-dimensional CNN for battery capacity estimation. The results showed that the method achieved low capacity estimation errors with randomly selected segments as inputs. Lee et al.\cite{ref30} transformed capacity fade sequences across cycles into two-dimensional images and employed a two-dimensional CNN for SOH estimation.
```

### 源文件块 8

中文原文：

```latex
然而，传统CNN的单层卷积受局部感受野限制，相距较远的特征通常需要经过多层卷积才能融合\cite{ref31}。为建立这些远距离联系，RNN通过隐藏状态将历史信息传递到后续时间步；其变体长短期记忆网络（LSTM）和门控循环单元（GRU）进一步利用门控机制选择性地保留和更新历史信息，以捕捉长期依赖\cite{ref14}。为同时利用局部特征与历史信息，研究者将CNN与循环网络相结合。例如，Xu等人\cite{ref41}将CNN提取的特征输入LSTM，利用LSTM的时序记忆能力估计SOH。Tian等人\cite{ref42}在CNN与BiLSTM的组合中进一步引入注意力机制，构建了CNN-BiLSTM-AM预测模型。Zheng等人\cite{ref33}则采用CNN-GRU，根据随机充电过程中的电压、电流和温度曲线片段估计SOH。尽管如此，这类模型中的隐藏状态仍需按时间步串行更新，限制了训练和推理过程中的并行计算\cite{ref31}。
```

英文译文：

```latex
However, a single convolutional layer in a traditional CNN has a limited local receptive field, and fusing distant features generally requires multiple convolutional layers\cite{ref31}. RNNs establish these long-range connections by passing historical information to subsequent time steps through hidden states. RNN variants, including long short-term memory (LSTM) and gated recurrent unit (GRU) networks, further employ gating mechanisms to selectively retain and update historical information to capture long-term dependencies\cite{ref14}. Researchers have also combined CNNs with recurrent networks to capture local features while retaining historical information. For example, Xu et al.\cite{ref41} fed CNN-extracted features into an LSTM and used its temporal memory to estimate SOH. Tian et al.\cite{ref42} further incorporated an attention mechanism into a CNN-BiLSTM architecture to develop the CNN-BiLSTM-AM prediction model. Zheng et al.\cite{ref33} employed a CNN-GRU to estimate SOH using segments of voltage, current, and temperature curves obtained during random charging. Nevertheless, the hidden states in these models still require sequential updates across time steps, limiting parallel computation during training and inference\cite{ref31}.
```

### 源文件块 9

中文原文：

```latex
为解决这一问题，Vaswani等人\cite{ref34}提出了Transformer。该模型避免循环递推，利用自注意力直接建立不同序列位置之间的联系，在捕捉长程依赖的同时支持并行计算。例如，Park和Kim\cite{ref38}采用物理先验引导的Transformer估计电池长期SOH；Chen等人\cite{ref37}则在视觉Transformer中加入维度变换层等结构，使其适用于电池SOH估计。研究者还将Transformer与卷积或循环网络相结合，以提高预测精度。Gu等人\cite{ref35}采用CNN提取局部特征，并结合Transformer捕捉长程依赖。Jia等人\cite{ref32}将BiGRU与Transformer结合，实验表明该模型在所用电池数据上具有较好的预测精度、鲁棒性和泛化表现。Bai和Wang\cite{ref36}则提出卷积Transformer框架，从电压和电流信号中提取局部细节，并通过自注意力建立局部特征之间的全局联系。然而，现有方法多通过集成其他模块或模型提高Transformer的预测精度，这种性能提升往往以增加参数量和计算开销为代价\cite{ref31}。与此同时，标准自注意力的计算瓶颈依然存在：它需要计算所有序列位置之间的两两关系，时间和存储复杂度随序列长度$N$呈二次增长，即$O(N^2)$\cite{ref39,ref40}。这些计算与存储需求增加了模型在资源受限BMS中的在线应用难度\cite{ref31}。
```

英文译文：

```latex
To address this limitation, Vaswani et al.\cite{ref34} proposed the Transformer, which avoids recurrence and uses self-attention to directly connect different sequence positions, capturing long-range dependencies while supporting parallel computation. For example, Park and Kim\cite{ref38} used a Transformer guided by physical priors to estimate long-term battery SOH, while Chen et al.\cite{ref37} added structures such as dimension-transformation layers to a vision Transformer to adapt it to battery SOH estimation. Researchers have also combined Transformers with convolutional or recurrent networks to enhance prediction accuracy. Gu et al.\cite{ref35} used a CNN to extract local features and a Transformer to capture long-range dependencies. Jia et al.\cite{ref32} combined a BiGRU with a Transformer, and their experiments showed good prediction accuracy, robustness, and generalization on the battery data used. Bai and Wang\cite{ref36} proposed a convolutional Transformer framework that extracts local details from voltage and current signals and uses self-attention to establish global connections among local features. However, many existing methods improve Transformer prediction accuracy by integrating other modules or models, often at the cost of more parameters and higher computational overhead\cite{ref31}. Meanwhile, the computational bottleneck of standard self-attention remains: it computes pairwise relationships among all sequence positions, with time and memory complexity growing quadratically with sequence length $N$, namely $O(N^2)$\cite{ref39,ref40}. These computational and storage demands make it challenging to use such models online in resource-constrained BMS\cite{ref31}.
```

### 源文件块 10

中文原文：

```latex
除了预测模型，健康指标的提取与选择对SOH估计的准确性同样至关重要。这些指标主要从电池循环过程中的电压、电流、温度、时间和内阻等运行数据及其衍生曲线中提取\cite{ref47,ref48,ref49,ref50}。其中，部分内阻指标需要通过阻抗谱测试获得，测试过程耗时且依赖专用仪器\cite{ref64}。温度指标虽然包含电池退化信息，但也会受到环境温度和充放电倍率的影响，其在不同工况下的稳定性受到限制\cite{ref64}。增量容量曲线能够反映电池老化引起的电压平台变化，但计算该曲线需要进行微分运算，容易放大采样噪声。为获得可靠的曲线特征，通常需要进行平滑处理\cite{ref28,ref50}。例如，Wen等人\cite{ref50}从平滑后的增量容量曲线中提取峰值、峰位和峰形斜率等候选特征，并根据相关性分析选择峰值作为BP神经网络输入。
```

英文译文：

```latex
In addition to the prediction model, health indicator extraction and selection are crucial for accurate SOH estimation. These indicators are mainly extracted from voltage, current, temperature, time, and internal resistance data recorded during battery cycling, as well as curves derived from these data\cite{ref47,ref48,ref49,ref50}. Some internal-resistance indicators require impedance spectrum measurements, which are time-consuming and require specialized instruments\cite{ref64}. Although temperature indicators contain battery degradation information, they are also affected by ambient temperature and charge-discharge rate, limiting their stability across operating conditions\cite{ref64}. Incremental capacity curves reflect changes in voltage plateaus caused by battery aging, but their calculation requires differentiation, which can amplify sampling noise. Smoothing is therefore usually needed to obtain reliable curve features\cite{ref28,ref50}. For example, Wen et al.\cite{ref50} extracted candidate features such as peak values, peak positions, and peak-shape slopes from smoothed incremental capacity curves and used correlation analysis to select the peak value as the input to a backpropagation (BP) neural network.
```

### 源文件块 11

中文原文：

```latex
相比之下，时间类健康指标无需微分处理，提取过程更为简单。其中，恒流充电时间（CCCT）可由所选电压区间两端对应时刻的差值获得。Richardson等人\cite{ref28}利用恒流充电曲线中不同电压区间的时间特征估计电池容量，Lin等人\cite{ref63}则将CCCT作为随机森林的输入，估计电池SOH。由于时间特征与容量之间的相关性会受到所选电压区间影响，相关研究通常需要进一步确定合适的特征提取区间。Tian等人\cite{ref51}通过优化充电电压区间，提高所提取健康指标与容量之间的相关性。在充电时间特征的区间选择中，Li等人\cite{ref31}逐步缩小电压窗口，并利用组内多节电池的皮尔逊相关系数（PCC）评价候选区间，以从更短的充电片段中提取与SOH高度相关的时间特征。
```

英文译文：

```latex
In contrast, time-based health indicators do not require differentiation and are simpler to extract. Constant current charge time (CCCT) can be obtained from the difference between the times corresponding to the two endpoints of a selected voltage interval. Richardson et al.\cite{ref28} used charging-time features from different voltage intervals of constant-current charging curves to estimate battery capacity, while Lin et al.\cite{ref63} used CCCT as the input to a random forest to estimate battery SOH. Because the correlation between charging-time features and capacity depends on the selected voltage interval, researchers generally need to identify a suitable interval for feature extraction. Tian et al.\cite{ref51} optimized the charging voltage interval, strengthening the correlation between the extracted health indicator and capacity. In selecting intervals for charging-time features, Li et al.\cite{ref31} progressively narrowed the voltage window and evaluated candidates using Pearson correlation coefficient (PCC) values from multiple cells in the same group, aiming to extract charging-time features highly correlated with SOH from shorter charging segments.
```

### 源文件块 12

中文原文：

```latex
不同运行数据及其衍生曲线能够从不同方面反映电池退化。为更充分地利用这些信息，一些研究从多种运行信号中构建候选健康指标，并进一步优化模型输入。例如，Dai等人\cite{ref48}从电压、电流、温度以及增量容量、差分热伏安曲线中提取健康指标，并计算这些指标在各循环下的均值、中位数等统计特征，随后通过比较不同统计特征组合的估计误差确定用于SOH估计的输入。Lin等人\cite{ref55}从电学、热学和电化学等角度构建多类特征，采用主成分分析进行降维，并利用模拟退火算法优化保留的特征维数，从而减少冗余并改善SOH估计表现。
```

英文译文：

```latex
Different types of operating data and the curves derived from them reflect different aspects of battery degradation. To use this information more fully, some studies construct candidate health indicators from multiple operating signals and further optimize model inputs. For example, Dai et al.\cite{ref48} extracted health indicators from voltage, current, temperature, incremental capacity, and differential thermal voltammetry curves and calculated statistical features such as the per-cycle means and medians of these indicators. They then compared estimation errors for different combinations of statistical features to determine the inputs for SOH estimation. Lin et al.\cite{ref55} constructed multiple features from electrical, thermodynamic, and electrochemical perspectives, used principal component analysis to reduce dimensionality, and optimized the number of retained dimensions with simulated annealing, thereby reducing redundancy and improving SOH estimation performance.
```

### 源文件块 13

中文原文：

```latex
单一健康指标所反映的退化信息相对有限，多源特征能够从不同方面补充电池退化的描述。然而，增加候选指标并不必然提高估计精度，表征能力较弱、跨电池表现不稳定或相互重复的指标，可能限制多源信息的有效利用，并增加模型的学习负担。因此，有必要设计相应的健康指标筛选算法，将SOH相关性、跨电池表现与冗余关系纳入统一的评价与筛选过程，保留具有稳定表征能力的指标，减少弱相关和重复信息的输入，以帮助模型更有效地学习电池退化规律。
```

英文译文：

```latex
A single health indicator contains relatively limited degradation information, whereas multi-source features can describe complementary aspects of battery degradation. However, adding more candidate indicators does not necessarily improve estimation accuracy. Indicators with weak representational ability, inconsistent performance across cells, or redundant information may limit the effective use of multi-source information and increase the model's learning burden. Therefore, a health indicator selection algorithm should be developed to jointly evaluate candidates' correlations with SOH, performance across cells, and redundancy among indicators. It should retain indicators with stable representational ability and reduce inputs weakly correlated with SOH or containing redundant information, helping the model learn battery degradation patterns more effectively.
```

### 源文件块 14

中文原文：

```latex
现有SOH估计方法之间的比较总结于\Cref{tab:soh-method-comparison}。具体而言，重点考察各方法是否充分利用电池运行数据中的退化信息，是否采用有效的健康指标提取与选择策略，是否通过针对性的模型设计兼顾估计性能与计算效率，以及是否开展模型复杂度评价。在健康指标方面，不同电池在材料体系和运行条件上存在差异，所选指标能否在不同电池间保持稳定的退化表征能力仍需进一步关注。在模型方面，除估计性能外，模型复杂度同样直接关系到实际部署。近年来，深度模型架构发展的一个显著趋势是通过增加网络深度、扩大模型规模或引入更复杂的特征交互结构来增强表征能力。这些设计有助于提升模型对复杂退化规律的建模能力，但通常也伴随着更高的参数量、计算开销和存储需求。因此，面向计算能力、存储空间和实时性受到限制的BMS，SOH估计模型需要在保持有效表征能力的同时控制模型规模与资源开销，进一步向紧凑化和高效化方向发展。
```

英文译文：

```latex
A comparison of existing SOH estimation methods is summarized in \Cref{tab:soh-method-comparison}. Specifically, we examine whether these methods make full use of degradation information in battery operating data, adopt effective health indicator extraction and selection strategies, balance estimation performance and computational efficiency through targeted model design, and evaluate model complexity. Given differences in battery chemistries and operating conditions, the ability of selected indicators to represent degradation consistently across cells warrants further attention. In addition to estimation performance, model complexity is directly related to practical deployment. In recent years, a notable trend in deep model design has been to increase network depth, expand model size, or introduce more complex structures for feature interaction to enhance representational capacity. These designs help models better capture complex degradation patterns but usually come with higher parameter counts, computational costs, and storage requirements. Therefore, SOH estimation models need to become more compact and efficient while retaining effective representational capacity to meet the real-time estimation requirements of resource-constrained BMS.
```

### 源文件块 16

中文原文：

```latex
\subsection{挑战分析与贡献}
```

英文译文：

```latex
\subsection{Challenges and contributions}
```

### 源文件块 17

中文原文：

```latex
现有方法面临的主要挑战可归纳为以下三点。
```

英文译文：

```latex
Three main challenges facing existing methods are summarized as follows.
```

### 源文件块 18

中文原文：

```latex
（1）\textbf{健康指标的跨电池稳定性问题。} 从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。PCC和斯皮尔曼相关系数（SCC）分别用于评价线性关联与单调关联，仅采用其中一种，难以同时考察这两方面的表现。此外，即使多个指标均与SOH具有较强关联，它们之间仍可能包含重复信息。因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。
```

英文译文：

```latex
(1) \textbf{Cross-cell stability of health indicators.} Raw data collected from multiple sensors contain diverse features related to degradation. The relationship between a candidate health indicator and SOH may vary across cells, and an indicator that performs well on one cell may not retain the same representational ability on others. PCC and the Spearman correlation coefficient (SCC) evaluate linear and monotonic relationships, respectively; using only one makes it difficult to assess both aspects. Moreover, even indicators strongly associated with SOH may contain redundant information. Model input selection therefore needs to consider both correlations across cells and redundancy among indicators to reduce its dependence on the performance of a single cell.
```

### 源文件块 19

中文原文：

```latex
（2）\textbf{局部与长期退化信息的融合问题。} 随着循环推进，电池容量整体呈下降趋势，并伴随相邻循环的波动和局部容量恢复。局部特征能够反映短期变化，但对长期衰减趋势的把握还需要建立跨循环联系；在聚合跨循环信息时，也需要保留局部退化细节，避免短期变化被弱化。因此，模型不仅需要提取不同时间尺度的退化特征，还需要使局部变化与长期趋势相互补充，以提高SOH估计的准确性。
```

英文译文：

```latex
(2) \textbf{Fusion of local and long-term degradation information.} As cycling progresses, battery capacity generally declines, with fluctuations between neighboring cycles and local capacity recovery. Local features reflect short-term changes, but capturing long-term capacity fade trends also requires connections across cycles. When aggregating information across cycles, local degradation details must be retained so that short-term changes are not weakened. Therefore, the model needs not only to extract degradation features at different time scales but also to make local variations and long-term trends complement each other to improve SOH estimation accuracy.
```

### 源文件块 20

中文原文：

```latex
（3）\textbf{计算复杂度限制。} 许多现有深度学习模型通过增加网络深度或组合不同网络结构提高SOH估计精度。这些方法增加了模型参数和计算操作。循环结构需要按时间步依次计算，标准自注意力需要计算所有序列位置之间的两两关系，其时间和存储开销随序列长度呈二次增长。这些开销加重了资源受限BMS的运行负担，限制了在线SOH估计模型的部署。
```

英文译文：

```latex
(3) \textbf{Computational complexity limitations.} Many existing deep learning models improve SOH estimation accuracy by increasing network depth or combining different network structures. These approaches increase the number of model parameters and computational operations. Recurrent structures require sequential computation over time steps, while standard self-attention computes pairwise relationships among all sequence positions, with time and memory complexity growing quadratically with sequence length. These costs increase the operating burden on resource-constrained BMS and limit the deployment of online SOH estimation models.
```

### 源文件块 21

中文原文：

```latex
为应对上述挑战，本文提出一种以MS-AgentNet为核心的锂离子电池SOH估计框架。该框架从健康指标构建和轻量模型设计两个层面展开，分别通过组级标定与筛选提高模型输入的跨电池稳定性，并以较低计算开销提取局部变化和长期趋势，主要贡献如下。
```

英文译文：

```latex
To address these challenges, this paper proposes a lithium-ion battery SOH estimation framework built around MS-AgentNet. The framework addresses health indicator construction and lightweight model design: group-level calibration and selection improve the cross-cell stability of model inputs, while local variations and long-term trends are extracted with low computational overhead. The main contributions are as follows.
```

### 源文件块 22

中文原文：

```latex
（1）\textbf{提出多源健康指标提取与优化算法。} 该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，再以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余。利用MS-CCCT标定其中充电时间特征的电压窗口，再通过PCC/SCC双阈值与冗余约束筛选候选指标。统一的筛选规则为各数据集确定相应的健康指标组合，入选指标在同一数据集的其他电池上仍保持较强的线性和单调相关性。
```

英文译文：

```latex
(1) \textbf{A multi-source health indicator extraction and optimization algorithm is proposed.} The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. MS-CCCT then calibrates the voltage window for the charging-time feature. The algorithm uses correlation results from the feature-development cells to evaluate each candidate's association with SOH and its redundancy with other indicators. It then applies PCC and SCC thresholds and redundancy constraints to select the indicators. The same selection rules determine a final HI subset for each dataset, and the selected indicators retain strong linear and monotonic correlations with SOH on other cells in that dataset.
```

### 源文件块 23

中文原文：

```latex
（2）\textbf{构建轻量级局部—全局网络MS-AgentNet。} 设计轻量级局部—全局融合注意力模块（SLFA），将小核深度可分离卷积与ReLU$^2$智能体注意力相结合，以较低的参数开销融合局部退化特征与长期依赖。所构建的注意力机制将计算复杂度由$O(N^2)$降低至$O(N)$。模型进一步引入大核深度可分离卷积，与小核卷积共同提取不同时间尺度的退化特征。上述设计将局部特征提取与全局信息交互整合于紧凑的网络结构中，在提高SOH估计精度的同时降低了计算与存储开销。
```

英文译文：

```latex
(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} A Local-Global Fusion Attention (LGFA) module combines small-kernel depthwise separable convolutions with ReLU$^2$ agent attention. It extracts local degradation features, captures long-term dependencies, and fuses the resulting representations with low parameter overhead. The attention mechanism reduces computational complexity from $O(N^2)$ to $O(N)$. The model further introduces large-kernel depthwise separable convolutions, which, together with small-kernel convolutions, extract degradation features at different time scales. These designs integrate local feature extraction and global information interaction into a compact network structure, improving SOH estimation accuracy while reducing computational and storage overhead.
```

### 源文件块 24

中文原文：

```latex
（3）\textbf{开展多数据集综合验证。} 在具有不同材料、容量和充放电协议的多个公开数据集上开展实验，并结合模块消融与复杂度分析，综合评估所提方法的估计精度、计算效率及跨电池泛化能力。进一步通过跨数据集迁移实验考察模型的跨域适应能力。结果表明，所提模型在保持较高SOH估计精度的同时，具有较低的计算量和存储开销。
```

英文译文：

```latex
(3) \textbf{Comprehensive validation is conducted across multiple datasets.} Experiments on multiple public battery datasets with different chemistries, capacities, and charge-discharge protocols, together with module ablation and complexity analysis, provide a comprehensive evaluation of the proposed method in terms of estimation accuracy, computational efficiency, and cross-cell generalization capability. Cross-dataset transfer experiments further examine the model's cross-domain adaptation capability. The results show that the proposed model maintains high SOH estimation accuracy with low computational and storage overhead.
```

## chapter02.tex

### 源文件块 1

中文原文：

```latex
\subsection{健康状态估计框架概述}
```

英文译文：

```latex
\subsection{Overview of the SOH estimation framework}
```

### 源文件块 2

中文原文：

```latex
为统一后续实验中的计算口径，SOH 按容量保持率进行计算，即电池当前可用容量与额定容量之比\cite{ref13,ref14}：
```

英文译文：

```latex
To use a consistent definition in the following experiments, SOH is calculated as capacity retention, namely the ratio of the current available capacity to the rated capacity\cite{ref13,ref14}:
```

### 源文件块 4

中文原文：

```latex
其中，$C_{\mathrm{current}}$ 和 $C_{\mathrm{rated}}$ 分别表示电池当前可用容量和额定容量。
```

英文译文：

```latex
where $C_{\mathrm{current}}$ and $C_{\mathrm{rated}}$ denote the current available capacity and rated capacity of the battery, respectively.
```

### 源文件块 5

中文原文：

```latex
所提出的健康状态估计框架如\cref{fig:2-1}所示。
```

英文译文：

```latex
The proposed SOH estimation framework is shown in \cref{fig:2-1}.
```

### 源文件块 6

中文原文：

```latex
（1）\textbf{数据获取。} 选取不同材料体系和运行工况下的公开电池老化数据，获取充放电过程中的电压、电流、温度、时间和容量等循环记录。
```

英文译文：

```latex
(1) \textbf{Data acquisition.} Public battery aging data covering different battery chemistries and operating conditions are selected to obtain cycle records of voltage, current, temperature, time, and capacity during charging and discharging.
```

### 源文件块 7

中文原文：

```latex
（2）\textbf{系统化特征工程。} 采用所提出的多源健康指标提取与优化算法，从上述数据中构建多源候选健康指标池，并通过组级标定与筛选确定模型输入。随后，采用滑动窗口划分健康指标时间序列，将各窗口与其下一循环的 SOH 配对，形成输入样本及对应标签。
```

英文译文：

```latex
(2) \textbf{Systematic feature engineering.} The proposed multi-source health indicator extraction and optimization algorithm constructs a pool of multi-source candidate HIs from these data and determines the model inputs through group-level calibration and selection. A sliding window is then used to segment the HI time series. Each window is paired with the SOH of the next cycle to form an input sample and its label.
```

### 源文件块 8

中文原文：

```latex
（3）\textbf{模型训练。} 将筛选后的健康指标样本输入 MS-AgentNet，在训练电池上完成模型参数学习，并根据配置电池上的估计表现确定模型配置。
```

英文译文：

```latex
(3) \textbf{Model training.} Samples of the selected HIs are fed into MS-AgentNet. Model parameters are learned on the training cell, while the validation cell is used for validation and comparison to select the best-performing hyperparameter configuration. The selected model is then directly tested on the remaining cells in the corresponding dataset.
```

### 源文件块 9

中文原文：

```latex
（4）\textbf{性能评价。} 将训练后的模型直接用于相应数据集的其他电池，比较不同模型的 SOH 估计精度、跨电池泛化性能及计算与存储开销。进一步通过消融实验分析关键模块的作用，并通过跨数据集迁移实验考察模型的跨域适应能力。
```

英文译文：

```latex
(4) \textbf{Model evaluation.} The SOH estimation accuracy, cross-cell generalization, and computational and storage overhead of the different models are evaluated. Ablation studies are further conducted to analyze the roles of key modules, and cross-dataset transfer experiments are used to examine cross-domain adaptation.
```

### 源文件块 10

中文原文：

```latex
\subsection{典型电池数据集}
```

英文译文：

```latex
\subsection{Typical battery datasets}
```

### 源文件块 11

中文原文：

```latex
为考察所提方法在不同电池体系和运行条件下的泛化能力，选取 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四组公开电池老化数据开展实验。这些数据集涵盖软包、方形和圆柱形电池，在材料体系、标称容量及运行条件等方面存在明显差异，可为模型在不同电池退化场景下的评估提供具有多样性的实验数据。各数据集的主要特性汇总于\cref{tab:2-1}。\cref{fig:2-2}(a)--(d)展示了所选电池的容量衰减曲线，\cref{fig:2-2}(e)--(h)给出了各数据集中代表性电池在不同 SOH 水平下的充电电压曲线。各数据集的具体情况如下。
```

英文译文：

```latex
Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, are selected to examine the generalization capability of the proposed method across different battery systems and operating conditions. These datasets include pouch, prismatic, and cylindrical cells and differ considerably in battery chemistries, nominal capacities, and operating conditions, providing diverse experimental data for model evaluation under different battery degradation scenarios. Their main characteristics are summarized in \cref{tab:2-1}. \cref{fig:2-2}(a)--(d) shows the capacity degradation curves of the selected cells, and \cref{fig:2-2}(e)--(h) presents the charging voltage curves of a representative cell from each dataset at different SOH levels. Details of each dataset are given below.
```

### 源文件块 12

中文原文：

```latex
\subsubsection*{（1）Oxford数据集}
```

英文译文：

```latex
\subsubsection*{(1) Oxford dataset}
```

### 源文件块 13

中文原文：

```latex
Oxford 数据集由牛津大学电池智能实验室提供，包含 8 节 Kokam SLPB533459H4 锂离子软包电池的老化数据，每节电池的标称容量为 0.74 Ah\cite{ref28}。该类电池的正极材料为镍钴酸锂（NCO）和钴酸锂（LCO）的混合物，负极材料为石墨\cite{ref60}。老化实验在 40 ℃ 的恒温环境下进行。电池采用恒流–恒压方式充电至 4.2 V，随后按照源自城市 ARTEMIS 工况的动态电流曲线进行放电，直至电压降至 2.7 V\cite{ref28,ref61}。实验纳入 Cell1–Cell8 共 8 节电池的循环老化记录。
```

英文译文：

```latex
The Oxford dataset is provided by the Battery Intelligence Laboratory at the University of Oxford and contains aging data from 8 Kokam SLPB533459H4 lithium-ion pouch cells, each with a nominal capacity of 0.74 Ah\cite{ref28}. The cathode is a blend of lithium nickel cobalt oxide (NCO) and lithium cobalt oxide (LCO), and the anode is graphite\cite{ref60}. The aging tests were conducted at a constant temperature of 40 ℃. The cells were charged to 4.2 V using a constant-current--constant-voltage protocol and then discharged following a dynamic current profile derived from the urban ARTEMIS drive cycle until the voltage reached 2.7 V\cite{ref28,ref61}. Aging records from cycling tests on all 8 cells, Cell1–Cell8, are included in the experiments.
```

### 源文件块 14

中文原文：

```latex
\subsubsection*{（2）CALCE数据集}
```

英文译文：

```latex
\subsubsection*{(2) CALCE dataset}
```

### 源文件块 15

中文原文：

```latex
CALCE 数据集由马里兰大学先进生命周期工程中心提供，包括 CS2 和 CX2 两组方形锂离子电池的老化数据\cite{ref18,ref61}。两组电池均采用钴酸锂（LCO）作为正极材料，其中 CS2 电池的标称容量为 1.1 Ah，CX2 电池的标称容量为 1.35 Ah。老化实验均在室温条件下开展，电池采用恒流–恒压方式充电至 4.2 V。CS2 和 CX2 均以 1C 恒流放电至 2.7 V。实验覆盖 CS2\_36–CS2\_38 和 CX2\_36–CX2\_38 共 6 节电池的循环老化记录。
```

英文译文：

```latex
The CALCE dataset is provided by the Center for Advanced Life Cycle Engineering at the University of Maryland and contains aging data from two groups of prismatic lithium-ion cells, CS2 and CX2\cite{ref18,ref61}. Both groups use lithium cobalt oxide (LCO) as the cathode material, with nominal capacities of 1.1 Ah for CS2 and 1.35 Ah for CX2. All aging tests were conducted at room temperature, and the cells were charged to 4.2 V using a constant-current--constant-voltage protocol. Both CS2 and CX2 were discharged at a constant current of 1C to 2.7 V. Aging records from cycling tests on 6 cells, CS2\_36–CS2\_38 and CX2\_36–CX2\_38, are included in the experiments.
```

### 源文件块 16

中文原文：

```latex
\subsubsection*{（3）MIT/Severson数据集}
```

英文译文：

```latex
\subsubsection*{(3) MIT/Severson dataset}
```

### 源文件块 17

中文原文：

```latex
MIT/Severson 数据集由麻省理工学院、斯坦福大学和丰田研究院联合发布\cite{ref62}。该数据集采用 A123 APR18650M1A 型 18650 圆柱形锂离子电池，每节电池的标称容量约为 1.1 Ah，正极材料为磷酸铁锂（LFP），负极材料为石墨。老化实验在 30 ℃ 的恒温环境下开展。实验纳入 b3c8、b3c13 和 b3c29 三节电池。三节电池均采用两步快速充电策略，其中 b3c8 采用 5.3C（54\% SOC）–4C 策略，b3c13 和 b3c29 采用 5.6C（36\% SOC）–4.3C 策略。达到 80\% SOC 后，电池以 1C 恒流充电至 3.6 V，随后转入恒压充电。放电过程采用 4C 恒流方式，截止电压为 2.0 V。
```

英文译文：

```latex
The MIT/Severson dataset was jointly released by the Massachusetts Institute of Technology, Stanford University, and Toyota Research Institute\cite{ref62}. It uses A123 APR18650M1A 18650 cylindrical lithium-ion cells, each with a nominal capacity of approximately 1.1 Ah, a lithium iron phosphate (LFP) cathode, and a graphite anode. The aging tests were conducted at a constant temperature of 30 ℃. Three cells, b3c8, b3c13, and b3c29, are included in the experiments. All three cells followed two-step fast-charging protocols: 5.3C (54\% SOC)–4C for b3c8 and 5.6C (36\% SOC)–4.3C for b3c13 and b3c29. After reaching 80\% SOC, the cells were charged at a constant current of 1C to 3.6 V, followed by constant-voltage charging. Discharging was performed at a constant current of 4C with a cutoff voltage of 2.0 V.
```

### 源文件块 19

中文原文：

```latex
\subsection{特征工程}
```

英文译文：

```latex
\subsection{Feature engineering}
```

### 源文件块 20

中文原文：

```latex
本节围绕 SOH 估计模型的输入构建展开，提出多源健康指标提取与优化算法。该算法首先基于充放电数据建立多源候选健康指标池，随后通过组级标定与筛选优化模型输入：利用 MS-CCCT 标定 CCCT 电压窗口，并结合特征开发电池集合上的 PCC/SCC 评价结果实现双阈值准入与冗余剔除，确定各数据集对应的模型输入。
```

英文译文：

```latex
This section presents the multi-source health indicator extraction and optimization algorithm for constructing the inputs to the SOH estimation model. The algorithm first builds a pool of multi-source candidate HIs from charging and discharging data, then optimizes the model inputs through group-level calibration and selection. Specifically, MS-CCCT calibrates the CCCT voltage window, and PCC/SCC results on the feature-development cell set are used for dual-threshold admission and redundancy removal to determine the inputs for each dataset.
```

### 源文件块 21

中文原文：

```latex
\subsubsection{健康指标提取}
```

英文译文：

```latex
\subsubsection{Health indicator extraction}
```

### 源文件块 22

中文原文：

```latex
基于电池循环采集的电压、电流、温度、时间与容量数据，构建充电电压–时间（CVT）、增量容量（IC）、微分温度–电压（DTV）和微分温度–容量（DTC）特征曲线，如\cref{fig:2-3}(a)--(d)所示。根据曲线随老化的变化特性，提取时长、幅值、特征位置和分布宽度等特征；同时计算窗口放电容量与充放电能量效率，形成包含 15 项候选健康指标的指标池\cite{ref52,ref63,ref64,ref65}。各指标的定义与分类见\cref{tab:2-2}。
```

英文译文：

```latex
Charging voltage--time (CVT), incremental capacity (IC), differential temperature--voltage (DTV), and differential temperature--capacity (DTC) curves are constructed from voltage, current, temperature, time, and capacity data collected during battery cycling, as shown in \cref{fig:2-3}(a)--(d). Features describing duration, amplitude, characteristic position, and distribution width are extracted based on how these curves change with aging. Discharge capacity within a voltage window and charge-discharge energy efficiency are also calculated, forming a pool of 15 candidate HIs\cite{ref52,ref63,ref64,ref65}. Their definitions and categories are listed in \cref{tab:2-2}.
```

### 源文件块 23

中文原文：

```latex
充电电压–时间（CVT）曲线记录恒流充电阶段端电压随时间的变化，可由电压与时间采样直接获取。随循环推进，CVT 曲线沿时间轴逐渐偏移，如\cref{fig:2-3}(a)所示。该偏移表现为固定电压区间内的充电时长随老化持续变化。电池老化引起的极化增大和容量衰减会共同改变这一充电过程\cite{ref63,ref64}，据此定义 CCCT：
```

英文译文：

```latex
The charging voltage--time (CVT) curve records changes in terminal voltage over time during constant-current charging and can be obtained directly from voltage and time samples. As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). This shift appears as a continuous change in charge duration within a fixed voltage interval as the battery ages. Increased polarization and capacity fade caused by battery aging jointly change this charging process\cite{ref63,ref64}. Accordingly, CCCT is defined as:
```

### 源文件块 25

中文原文：

```latex
式中，$t(V_1)$、$t(V_2)$ 分别为充电电压达到 $V_1$、$V_2$ 的时刻。CCCT 的电压区间由 MS-CCCT 标定，具体方法见第~\ref{sec:ms-ccct}~节，标定所得充电时长特征记为 HI1。
```

英文译文：

```latex
where $t(V_1)$ and $t(V_2)$ are the times when the charging voltage reaches $V_1$ and $V_2$, respectively. The CCCT voltage interval is calibrated by MS-CCCT, as described in Section~\ref{sec:ms-ccct}, and the resulting charging-time feature is denoted as HI1.
```

### 源文件块 26

中文原文：

```latex
除充电时序特征外，容量随电压的变化同样包含电池退化信息。增量容量（IC）曲线是解析电池电化学退化的经典分析手段。该方法对容量关于电压求导，将平缓的充电电压平台转化为辨识度更高的特征峰，其位置与形状会随电池老化发生变化\cite{ref50,ref64}。IC 的具体表达式为：
```

英文译文：

```latex
In addition to charging-time features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. Differentiating capacity with respect to voltage converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:
```

### 源文件块 28

中文原文：

```latex
式中，$V_k$ 和 $Q_k$ 分别为第 $k$ 个采样点的端电压和充电容量，$N$ 为两个采样点之间的间隔。不同循环下，IC 曲线的峰值、特征位置和分布宽度随老化发生变化，如\cref{fig:2-3}(b)所示。由此提取 IC 曲线的峰值、峰值对应电压和半峰宽，并分别定义为 HI2、HI3 和 HI4。
```

英文译文：

```latex
where $V_k$ and $Q_k$ are the terminal voltage and charge capacity at the $k$th sampling point, respectively, and $N$ is the interval between the two sampling points. Across cycles, the peak value, characteristic position, and distribution width of the IC curve change with aging, as shown in \cref{fig:2-3}(b). The peak value, voltage corresponding to the peak, and full width at half maximum of the IC curve are therefore extracted and defined as HI2, HI3, and HI4, respectively.
```

### 源文件块 29

中文原文：

```latex
温度是反映电池内部状态的另一重要维度。恒流充电过程中，电池表面温度变化通常较为缓慢，老化带来的微小热响应差异难以通过原始温度曲线直接识别。为识别这类差异，Wu 等人\cite{ref65}提出微分温度–电压（DTV）分析方法。该方法通过计算充电过程中电池表面温度相对电压的变化率，将热响应映射至电压域，形成随老化变化的峰谷特征曲线\cite{ref64,ref65}。其定义如下：
```

英文译文：

```latex
Temperature is another important measure of the internal state of a battery. During constant-current charging, the battery surface temperature usually changes slowly, making small aging-related differences in thermal response difficult to identify directly from the raw temperature curve. To identify these differences, Wu et al.\cite{ref65} proposed differential temperature--voltage (DTV) analysis. By calculating the rate of change in battery surface temperature with respect to voltage during charging, this method maps the thermal response to the voltage domain, producing a curve with peaks and valleys that change with aging\cite{ref64,ref65}. DTV is defined as:
```

### 源文件块 31

中文原文：

```latex
其中，$V_k$ 和 $T_k$ 分别为第 $k$ 个采样点的端电压和电池表面温度，$N$ 为两个采样点之间的间隔。为减小差分噪声的影响，对所得 DTV 曲线采用窗口大小为 200 个采样点的移动平均进行平滑处理\cite{ref64}。不同循环下，DTV 曲线的峰谷幅值与特征位置随老化发生变化，如\cref{fig:2-3}(c)所示。据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围\cite{ref64}。
```

英文译文：

```latex
where $V_k$ and $T_k$ are the terminal voltage and battery surface temperature at the $k$th sampling point, respectively, and $N$ is the interval between the two sampling points. To reduce the effect of noise introduced by differencing, the DTV curve is smoothed using a moving average with a window size of 200 sampling points\cite{ref64}. Across cycles, the peak and valley values and characteristic positions of the DTV curve change with aging, as shown in \cref{fig:2-3}(c). The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted to describe the amplitude, characteristic positions, and range of variation of the thermal response\cite{ref64}.
```

### 源文件块 32

中文原文：

```latex
与 DTV 在电压域刻画热响应不同，DTC 在充电容量域刻画热响应。DTC 以充电容量为自变量，描述温度变化率随容量的演化，其定义如下\cite{ref64}：
```

英文译文：

```latex
While DTV characterizes the thermal response in the voltage domain, DTC characterizes it in the charge capacity domain. With charge capacity as the independent variable, DTC describes how the rate of temperature change evolves with capacity and is defined as follows\cite{ref64}:
```

### 源文件块 34

中文原文：

```latex
其中，$T_k$、$Q_k$ 为第 $k$ 个采样点的电池表面温度和充电容量，$N$ 为两个采样点之间的间隔。对所得 DTC 曲线同样采用窗口大小为 200 个采样点的移动平均进行平滑处理\cite{ref64}。\cref{fig:2-3}(d)所示 DTC 曲线同样表现出随循环变化的峰值、特征位置和分布宽度，本文据此提取峰值、峰值对应容量和半峰宽，并将其定义为 HI10、HI11 和 HI12。
```

英文译文：

```latex
where $T_k$ and $Q_k$ are the battery surface temperature and charge capacity at the $k$th sampling point, and $N$ is the interval between the two sampling points. The DTC curve is also smoothed using a moving average with a window size of 200 sampling points\cite{ref64}. The DTC curves in \cref{fig:2-3}(d) likewise show changes in peak value, characteristic position, and distribution width across cycles. Accordingly, the peak value, capacity corresponding to the peak, and full width at half maximum are extracted and defined as HI10, HI11, and HI12.
```

### 源文件块 35

中文原文：

```latex
窗口放电容量由指定电压区间内的放电电流累计积分得到，其定义如下：
```

英文译文：

```latex
Discharge capacity within a voltage window is obtained by integrating the discharge current over a specified voltage interval and is defined as:
```

### 源文件块 37

中文原文：

```latex
其中，$V_{\mathrm{dch}}(t)$ 和 $I_{\mathrm{dch}}(t)$ 分别为放电电压和电流，积分范围为电压位于 $[V_l,V_h]$ 内的放电时间片段。时间以 s 为单位，$Q_{\mathrm{dch}}$ 的单位为 Ah。本文进一步构造两个窗口放电容量候选指标，分别计算端电压由 3.80 V 降至 3.40 V 以及由 3.20 V 降至 3.00 V 过程中释放的电荷量，并记为 HI13 和 HI14\cite{ref31,ref52}。
```

英文译文：

```latex
where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge voltage and current, respectively, and integration is performed over the discharge time segments in which the voltage lies within $[V_l,V_h]$. Time is measured in s, and $Q_{\mathrm{dch}}$ is measured in Ah. Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

### 源文件块 38

中文原文：

```latex
能量效率反映电池在充放电过程中的能量转换特性，定义为单次循环放电能量与充电能量之比\cite{ref66}：
```

英文译文：

```latex
Energy efficiency reflects the energy conversion characteristics of a battery during charging and discharging and is defined as the ratio of discharge energy to charge energy in a single cycle\cite{ref66}:
```

### 源文件块 40

中文原文：

```latex
其中，$V_{\mathrm{ch}}(t)$、$|I_{\mathrm{ch}}(t)|$、$t_{\mathrm{ch}}$ 与 $V_{\mathrm{dch}}(t)$、$|I_{\mathrm{dch}}(t)|$、$t_{\mathrm{dch}}$ 分别表示充电与放电阶段的端电压、电流幅值和持续时间，充电与放电均取完整循环过程。该能量效率记为 HI15（$\eta$）。
```

英文译文：

```latex
where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$ denote the terminal voltage, current magnitude, and duration of charging, respectively; $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote those of discharging. The full charging and discharging phases of each cycle are used. This energy efficiency is denoted as HI15 ($\eta$).
```

### 源文件块 42

中文原文：

```latex
\subsubsection{组级双相关 MS-CCCT}
\label{sec:ms-ccct}
```

英文译文：

```latex
\subsubsection{Group-level dual-correlation MS-CCCT}
\label{sec:ms-ccct}
```

### 源文件块 43

中文原文：

```latex
恒流充电时间能够反映电池容量随循环产生的变化，但其与 SOH 之间的相关性受到提取电压区间的影响。部分研究直接从预设的局部电压区间提取时间特征\cite{ref28,ref63}。然而，不同数据集对应的退化敏感区间并不相同，一个数据集上采用的固定窗口难以直接适用于其他数据集。为提高 CCCT 与 SOH 的相关性及其在同一数据集不同电池上的稳定性，本文提出组级双相关多尺度搜索方法（MS-CCCT）。该方法选取同一数据集内两节电池组成特征开发集合 $\mathcal{B}$，根据集合内的相关性结果构建组级稳健得分，并据此确定 HI1 的提取窗口。
```

英文译文：

```latex
Constant current charge time can reflect changes in battery capacity with cycling, but its correlation with SOH depends on the voltage interval used for extraction. Some studies directly extract charging-time features from predefined local voltage intervals\cite{ref28,ref63}. However, degradation-sensitive intervals differ across datasets, and a fixed window used for one dataset is difficult to apply directly to others. To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT). Two cells from the same dataset form the feature-development set $\mathcal{B}$. Correlation results within this set are used to construct a group-level robust score, which determines the extraction window for HI1.
```

### 源文件块 44

中文原文：

```latex
现有 CCCT 窗口优化方法多采用 PCC 评价候选区间\cite{ref31,ref51}。PCC 是衡量 CCCT 与 SOH 线性关联强度的常用统计指标，但该指标仅对线性变化敏感，单独使用难以反映单调非线性关系。SCC 专门评估变量间的单调变化关系，适合刻画这类单调非线性特征。候选窗口评价同时采用 PCC 和 SCC，以兼顾 CCCT 与 SOH 之间的线性关联和单调变化关系\cite{ref25,ref53,ref55}。第 $i$ 个候选窗口在集合 $\mathcal{B}$ 中第 $j$ 节电池上的 PCC $\gamma_{i,j}$ 和 SCC $\rho_{i,j}$ 分别定义为
```

英文译文：

```latex
Most existing CCCT window optimization methods use PCC to evaluate candidate intervals\cite{ref31,ref51}. PCC is a common statistical measure of the strength of the linear correlation between CCCT and SOH. However, it is sensitive only to linear changes and is insufficient on its own to characterize monotonic nonlinear relationships. SCC specifically measures monotonic relationships between variables and is suitable for characterizing such nonlinear features. Both PCC and SCC are used to evaluate candidate windows, accounting for the linear correlation and monotonic relationship between CCCT and SOH\cite{ref25,ref53,ref55}. The PCC $\gamma_{i,j}$ and SCC $\rho_{i,j}$ of the $i$th candidate window on the $j$th cell in $\mathcal{B}$ are defined as
```

### 源文件块 47

中文原文：

```latex
式中，$f_{i,j,k}$ 表示第 $j$ 节电池在第 $k$ 个循环由第 $i$ 个候选窗口提取的 CCCT，$y_{j,k}$ 为对应循环的 SOH，$n_j$ 为该电池的有效循环数；$\bar{f}_{i,j}$ 和 $\bar{y}_j$ 分别为 CCCT 与 SOH 的均值，$R(\cdot)$ 表示取秩操作。PCC 和 SCC 的取值范围均为 $-1$ 至 $1$，其绝对值越接近 $1$，表示相关性越强。
```

英文译文：

```latex
where $f_{i,j,k}$ is the CCCT extracted from the $i$th candidate window at the $k$th cycle of the $j$th cell, $y_{j,k}$ is the SOH of the corresponding cycle, and $n_j$ is the number of valid cycles for that cell. $\bar{f}_{i,j}$ and $\bar{y}_j$ are the mean CCCT and SOH, respectively, and $R(\cdot)$ denotes the ranking operation. Both PCC and SCC range from $-1$ to $1$, with absolute values closer to $1$ indicating stronger correlations.
```

### 源文件块 48

中文原文：

```latex
为综合候选窗口在两节电池上的相关性表现，分别取其在集合 $\mathcal{B}$ 中的最小绝对 PCC 和最小绝对 SCC：
```

英文译文：

```latex
To account for the correlation performance of each candidate window on both cells, its minimum absolute PCC and minimum absolute SCC within $\mathcal{B}$ are calculated:
```

### 源文件块 50

中文原文：

```latex
进一步取二者中的较小值作为第 $i$ 个候选窗口的组级稳健得分：
```

英文译文：

```latex
The smaller of these two values is then used as the group-level robust score of the $i$th candidate window:
```

### 源文件块 52

中文原文：

```latex
该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，使入选窗口在两节电池上均保持较强的相关性。
```

英文译文：

```latex
This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and allowing the selected window to maintain strong correlations on both cells.
```

### 源文件块 53

中文原文：

```latex
MS-CCCT 采用由粗到细的三阶段搜索。Oxford 数据集的初始搜索范围设为 3.50--4.20 V。R1 阶段采用 0.40 V 窗宽和 0.20 V 步长进行粗定位，并将稳健得分最高的窗口作为下一阶段的搜索区域；R2 阶段在该区域内采用 0.20 V 窗宽和 0.05 V 步长继续搜索；R3 阶段进一步采用 0.10 V 窗宽和 0.05 V 步长细化搜索。若 R3 阶段所得窗口的稳健得分高于 R2 阶段，则采用 R3 窗口，否则保留 R2 阶段的结果。
```

英文译文：

```latex
MS-CCCT uses a three-stage coarse-to-fine search. For the Oxford dataset, the initial search range is 3.50--4.20 V. Stage R1 uses a window width of 0.40 V and a step size of 0.20 V for coarse localization, and the window with the highest robust score becomes the search region for the next stage. Stage R2 searches this region using a window width of 0.20 V and a step size of 0.05 V. Stage R3 further refines the search using a window width of 0.10 V and a step size of 0.05 V. If the robust score obtained in R3 exceeds that in R2, the R3 window is selected; otherwise, the R2 result is retained.
```

### 源文件块 54

中文原文：

```latex
最终，Oxford 数据集的 3.55--3.75 V 窗口以 0.994447 的最高稳健得分入选，其对应的恒流充电时间序列作为 HI1。
```

英文译文：

```latex
For the Oxford dataset, the 3.55--3.75 V window is finally selected with the highest robust score of 0.994447, and its constant current charge time series is used as HI1.
```

### 源文件块 55

中文原文：

```latex
\subsubsection{健康指标筛选}
```

英文译文：

```latex
\subsubsection{Health indicator selection}
```

### 源文件块 56

中文原文：

```latex
健康指标筛选是锂离子电池 SOH 估计中的关键步骤\cite{ref60,ref61,ref62}，所选指标的质量直接影响最终估计精度。在前述 HI1 窗口标定的基础上，将恒流充电时间、IC、DTV、DTC、窗口放电容量和能量效率等 15 项特征共同作为候选健康指标。沿用前述组级相关性评价方式，分别计算各候选指标与 SOH 之间以及不同候选指标之间的 PCC 和 SCC。
```

英文译文：

```latex
HI selection is a key step in lithium-ion battery SOH estimation\cite{ref60,ref61,ref62}, as the quality of the selected indicators directly affects the final estimation accuracy. Following HI1 window calibration, 15 features based on constant current charge time, IC, DTV, DTC, discharge capacity within a voltage window, and energy efficiency are considered as candidate HIs. Using the same group-level correlation evaluation, PCC and SCC are calculated both between each candidate HI and SOH and between different candidate HIs.
```

### 源文件块 57

中文原文：

```latex
Oxford Cell1 和 Cell2 的相关性结果如\cref{fig:2-4}所示。图中同时展示了候选指标与 SOH 以及候选指标相互之间的 PCC 和 SCC。矩阵下三角列出相关系数，上三角通过圆圈大小和颜色深浅表示相关强度。圆圈越大、颜色越深，表示相应变量之间的相关性越强。
```

英文译文：

```latex
The correlation results for Oxford Cell1 and Cell2 are shown in \cref{fig:2-4}, including both PCC and SCC between candidate HIs and SOH and among the candidate HIs. The lower triangular part of each matrix lists the correlation coefficients, while the upper triangular part represents correlation strength through circle size and color intensity. Larger, darker circles indicate stronger correlations between the corresponding variables.
```

### 源文件块 58

中文原文：

```latex
同一候选指标在两节电池上的相关性表现并不完全相同。HI5（DTV 峰值）在 Cell1 上的绝对 PCC 和绝对 SCC 分别为 0.949 和 0.966，在 Cell2 上则降至 0.898 和 0.902；相比之下，HI1 在两节电池上均保持较高的相关性。若仅依据 Cell1 的相关性结果，HI5 会表现为强相关指标，但这一结果无法反映其在 Cell2 上的相关水平。单节电池上的相关性排序由此难以完整代表候选指标在其他电池上的表现。
```

英文译文：

```latex
The same candidate HI does not show identical correlation performance on the two cells. For HI5 (DTV peak value), the absolute PCC and SCC are 0.949 and 0.966 on Cell1 but decrease to 0.898 and 0.902 on Cell2. In contrast, HI1 maintains high correlations on both cells. Based on the results for Cell1 alone, HI5 would appear to be strongly correlated, but this result does not reflect its correlation level on Cell2. Thus, a correlation ranking based on a single cell cannot fully represent the performance of candidate HIs on other cells.
```

### 源文件块 59

中文原文：

```latex
现有研究通常依据相关系数的大小选择健康指标。当候选指标的相关性分布随电池化学体系、运行温度等条件发生变化时，这类筛选结果容易受到数据条件的影响。在单一条件下表现较好的指标，在其他电池或工况下的适用性可能下降。为提高筛选结果对电池个体和运行条件变化的鲁棒性，有必要引入综合相关性分布特征的健康指标筛选策略。
```

英文译文：

```latex
Existing studies usually select HIs based on the magnitude of their correlation coefficients. When the correlation distributions of candidate HIs change with battery chemistry, operating temperature, or other conditions, the selection results can be sensitive to the data conditions. An indicator that performs well under one condition may become less applicable to other cells or operating conditions. To improve the robustness of HI selection to differences between individual cells and operating conditions, a selection strategy that accounts for the characteristics of correlation distributions is needed.
```

### 源文件块 61

中文原文：

```latex
据此，本文构建组级健康指标筛选方法。该方法首先综合特征开发集合内两节电池的 PCC 和 SCC，仅保留均满足相关性要求的候选指标。相关性矩阵还显示，部分候选指标之间具有较高的相关系数，表明候选池中存在重复信息。保留的指标按照相关性强度进行排序，并进一步移除与已入选指标高度相关的特征，以降低指标间冗余并保持特征多样性。具体筛选条件、阈值和完整步骤见\cref{tab:2-hi-screening-steps}。
```

英文译文：

```latex
Accordingly, this study develops a group-level HI selection method. It first considers PCC and SCC on both cells in the feature-development set and retains only candidate HIs that meet all correlation requirements. The correlation matrices also show high correlations between some candidate HIs, indicating redundant information in the candidate pool. The retained HIs are ranked by correlation strength, and features highly correlated with already selected HIs are further removed to reduce redundancy while preserving feature diversity. The specific selection criteria, thresholds, and complete procedure are given in \cref{tab:2-hi-screening-steps}.
```

### 源文件块 62

中文原文：

```latex
经过相关性准入与冗余剔除，Oxford 数据集最终保留 HI1。该指标在 Cell1 和 Cell2 上的绝对 PCC 分别为 0.998759 和 0.997322，绝对 SCC 分别为 0.998710 和 0.994447。四项相关系数均接近 1，且在两节电池之间差异较小，表明 HI1 对 SOH 变化具有较高的退化敏感性和良好的跨电池一致性。
```

英文译文：

```latex
After correlation-based admission and redundancy removal, HI1 is retained for the Oxford dataset. Its absolute PCC values on Cell1 and Cell2 are 0.998759 and 0.997322, and its absolute SCC values are 0.998710 and 0.994447, respectively. All four coefficients are close to 1 and differ only slightly between the two cells, indicating that HI1 is highly sensitive to SOH changes during degradation and has good cross-cell consistency.
```

### 源文件块 63

中文原文：

```latex
健康指标筛选仅在特征开发阶段执行。指标确定后，其定义和计算参数保持不变，并直接用于同一数据集其他电池的特征提取。用于后续评价的其他电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发与后续评价之间的数据隔离。
```

英文译文：

```latex
HI selection is performed only during feature development. Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for the other cells in the corresponding dataset without correlation-based selection, threshold determination, or HI reselection.
```

### 源文件块 64

中文原文：

```latex
固定后的 HI1 在 Cell3--Cell8 上的绝对 PCC 为 0.997874--0.999337。与已有健康指标的比较结果见\cref{tab:2-hi-literature}，其相关水平均高于所列样本熵、DTV/IC 特征及充电电压曲线斜率在相应电池上的已报道值，说明 HI1 在其余六节电池上仍保持较高的线性相关性。
```

英文译文：

```latex
With its definition fixed, HI1 achieves absolute PCC values of 0.997874--0.999337 on Cell3--Cell8. Comparisons with existing HIs are presented in \cref{tab:2-hi-literature}. Its correlations exceed the reported values for the listed sample entropy, DTV/IC features, and charging voltage curve slopes on the corresponding cells, showing that HI1 maintains high linear correlations on the remaining six cells.
```

## chapter03.tex

### 源文件块 1

中文原文：

```latex
为同时应对电池SOH估计中精度与计算效率两方面的挑战，本文提出一种轻量级多尺度智能体网络（Multi-Scale Agent Network，MS-AgentNet）。其命名中的“MS”源于由小核DSConv-S与大核DSConv-L构成的多尺度卷积设计，用于高效提取不同时间尺度的退化特征。下文介绍MS-AgentNet的总体架构与工作流程，阐述所设计的多尺度深度可分离卷积模块，并详细说明轻量级局部—全局融合注意力（Slim Local-Global Fusion Attention，SLFA）模块。
```

英文译文：

```latex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Local-Global Fusion Attention (LGFA) module.
```

### 源文件块 2

中文原文：

```latex
\subsection{MS-AgentNet架构概述}
```

英文译文：

```latex
\subsection{Architecture overview of MS-AgentNet}
```

### 源文件块 3

中文原文：

```latex
MS-AgentNet的总体架构如\cref{fig:3-1}所示：健康指标（Health Indicators，HIs）序列经滑动窗口划分为样本片段，通过线性嵌入层映射至$d$维特征空间后输入MS-AgentNet Block；Block输出经层归一化、展平和线性读出后得到SOH估计值，训练时以每个输入窗口后紧邻循环的真实SOH值作为监督标签。
```

英文译文：

```latex
The overall architecture of MS-AgentNet is shown in \cref{fig:3-1}. Health indicator (HI) sequences are divided into sample segments using a sliding window, mapped to a $d$-dimensional feature space through a linear embedding layer, and fed into an MS-AgentNet Block. The Block output passes through layer normalization, flattening, and a linear readout layer to produce the SOH estimate. During training, the true SOH of the cycle immediately following each input window is used as the supervision label.
```

### 源文件块 4

中文原文：

```latex
从数学角度看，设第$l$个MS-AgentNet Block的输入为$\mathbf X_l\in\mathbb R^{B\times N\times d}$，其中$B$为批量大小，$N$为输入序列长度，$d$为特征嵌入维度。Block通过以下三个步骤完成特征变换：
```

英文译文：

```latex
Mathematically, let the input to the $l$th MS-AgentNet Block be $\mathbf X_l\in\mathbb R^{B\times N\times d}$, where $B$ is the batch size, $N$ is the input sequence length, and $d$ is the feature embedding dimension. The Block transforms the features in three steps:
```

### 源文件块 5

中文原文：

```latex
\textbf{步骤1：局部—全局特征融合。} 输入$\mathbf X_l$经SLFA模块处理。SLFA利用DSConv-S提取局部特征，并通过ReLU$^2$智能体注意力（ReLU$^2$ Agent Attention，RAA）建立跨位置全局信息交互：
```

英文译文：

```latex
\textbf{Step 1: Local-global feature fusion.} The input $\mathbf X_l$ is processed by LGFA, which uses DSConv-S to extract local features and ReLU$^2$ Agent Attention (RAA) to establish global information interactions across positions:
```

### 源文件块 7

中文原文：

```latex
\textbf{步骤2：长尺度特征细化。} SLFA的输出$\mathbf X_l'$经层归一化后输入DSConv-L，以提取较长时间尺度的退化特征。DSConv-L的输出经$W_l$缩放，并与$\mathbf X_l'$进行残差相加：
```

英文译文：

```latex
\textbf{Step 2: Feature refinement over longer time scales.} The LGFA output $\mathbf X_l'$ passes through layer normalization and then DSConv-L to extract degradation features over longer time scales. The DSConv-L output is scaled by $W_l$ and added to $\mathbf X_l'$ through a residual connection:
```

### 源文件块 9

中文原文：

```latex
\textbf{步骤3：非线性映射。} 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN），并与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：
```

英文译文：

```latex
\textbf{Step 3: Nonlinear mapping.} The features $\mathbf X_l''$ are processed by $\operatorname{LN}_0$ and then a feedforward neural network (FFN). The result is added to $\mathbf X_l''$ through a residual connection to produce the Block output $\mathbf Y_l$:
```

### 源文件块 11

中文原文：

```latex
令$\mathbf Y_l$作为下一Block的输入，即$\mathbf X_{l+1}=\mathbf Y_l$。其中，$W_l$为可学习缩放系数；$\operatorname{LN}$和$\operatorname{LN}_0$均表示层归一化，$\operatorname{LN}_0$不使用额外的缩放和偏置参数。
```

英文译文：

```latex
The output $\mathbf Y_l$ is used as the input to the next Block, i.e., $\mathbf X_{l+1}=\mathbf Y_l$. Here, $W_l$ is a learnable scaling factor. Both $\operatorname{LN}$ and $\operatorname{LN}_0$ denote layer normalization, but $\operatorname{LN}_0$ uses no additional scale or bias parameters.
```

### 源文件块 13

中文原文：

```latex
\subsection{所设计的多尺度深度可分离卷积模块}
```

英文译文：

```latex
\subsection{The designed multi-scale depthwise separable convolution modules}
```

### 源文件块 14

中文原文：

```latex
为兼顾多尺度局部特征提取与计算效率，本节首先介绍DSConv的基本结构，并将其与标准卷积进行计算量比较；随后说明DSConv-S和DSConv-L的结构配置及其功能分工。
```

英文译文：

```latex
To combine multi-scale local feature extraction with computational efficiency, this section first introduces the basic structure of DSConv and compares its computational cost with that of standard convolution. The configurations and respective roles of DSConv-S and DSConv-L are then described.
```

### 源文件块 15

中文原文：

```latex
\subsubsection{DSConv基本结构与计算量比较}
```

英文译文：

```latex
\subsubsection{Basic DSConv structure and computational cost comparison}
```

### 源文件块 16

中文原文：

```latex
卷积运算通过滑动卷积核提取时间序列中的局部信息\cite{ref71}。标准卷积在所有输入通道上进行运算，每个卷积核生成一个输出特征图，对应一个输出通道。随着输入通道数、输出通道数和卷积核尺寸增加，其参数量与计算开销迅速累积，显著推高计算负载并延长训练时间。在小样本电池数据集上，较大的参数量还可能增加模型的过拟合风险。其计算成本可表示为：
```

英文译文：

```latex
Convolution extracts local information from time series through sliding kernels\cite{ref71}. Standard convolution operates across all input channels, with each kernel producing one output feature map corresponding to one output channel. As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time. A larger parameter count may also increase the risk of overfitting on small-sample battery datasets. Its computational cost can be expressed as:
```

### 源文件块 18

中文原文：

```latex
其中，$k$、$C_{\mathrm{in}}$、$C_{\mathrm{out}}$和$D_F$分别表示卷积核大小、输入通道数、输出通道数和特征图尺寸。
```

英文译文：

```latex
where $k$, $C_{\mathrm{in}}$, $C_{\mathrm{out}}$, and $D_F$ denote the kernel size, number of input channels, number of output channels, and feature map size, respectively.
```

### 源文件块 19

中文原文：

```latex
与标准卷积不同，深度可分离卷积（DSConv）将卷积运算分解为深度卷积和逐点卷积两个阶段\cite{ref71}。其中，深度卷积为每个输入通道单独配置卷积核，在通道内完成局部特征提取；随后，$1\times1$逐点卷积融合不同通道的特征，并将通道数调整为$C_{\mathrm{out}}$。通过分离通道内特征提取与通道间特征融合，DSConv减少了标准卷积中的密集跨通道运算。其计算成本可表示为：
```

英文译文：

```latex
Unlike standard convolution, depthwise separable convolution (DSConv) decomposes convolution into two stages: depthwise convolution and pointwise convolution\cite{ref71}. Depthwise convolution applies a separate kernel to each input channel to extract local features within that channel. A $1\times1$ pointwise convolution then fuses features across channels and adjusts the number of channels to $C_{\mathrm{out}}$. By separating within-channel feature extraction from cross-channel feature fusion, DSConv reduces the dense cross-channel operations required by standard convolution. Its computational cost can be expressed as:
```

### 源文件块 21

中文原文：

```latex
进一步比较两类卷积的计算量，可得二者之比为：
```

英文译文：

```latex
The ratio of the computational costs of the two types of convolution is:
```

### 源文件块 23

中文原文：

```latex
由式\eqref{eq:dsconv_cost_ratio}可知，在输入、输出通道配置一致的情况下，DSConv的计算成本低于标准卷积，为后续小核与大核卷积模块的构建提供了基础。
```

英文译文：

```latex
Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and output channel configurations, DSConv has a lower computational cost than standard convolution, providing the basis for the small- and large-kernel modules described below.
```

### 源文件块 24

中文原文：

```latex
\subsubsection{DSConv-S：双重作用的局部增强}
```

英文译文：

```latex
\subsubsection{DSConv-S: Dual-role local enhancement}
```

### 源文件块 25

中文原文：

```latex
小核DSConv-S采用紧凑的$1\times5$深度卷积，并嵌入SLFA模块、位于RAA全局交互之前，以实现输入增强与局部分支保留两项作用：
```

英文译文：

```latex
Small-kernel DSConv-S uses a compact $1\times5$ depthwise convolution and is embedded in LGFA before the global interactions in RAA. It serves two roles: input enhancement and local branch preservation:
```

### 源文件块 26

中文原文：

```latex
1. \textbf{输入增强。} DSConv-S提取输入特征中的局部邻域信息，形成局部增强表示$\mathbf X_S$。RAA随后基于$\mathbf X_S$构造查询、键和值，并通过智能体聚合与广播完成跨位置交互。这一前置卷积为RAA引入局部性偏置，增强其在跨位置上下文聚合过程中对局部变化的表征。
```

英文译文：

```latex
1. \textbf{Input enhancement.} DSConv-S extracts local neighborhood information from the input features to form a locally enhanced representation $\mathbf X_S$. RAA then constructs queries, keys, and values from $\mathbf X_S$ and performs cross-position interactions through agent aggregation and broadcasting. This preceding convolution introduces a locality bias into RAA, improving its representation of local variations during cross-position context aggregation.
```

### 源文件块 27

中文原文：

```latex
2. \textbf{局部分支保留。} 在SLFA中，$\mathbf X_S$同时传递至RAA分支和局部分支。局部分支对$\mathbf X_S$进行层归一化后传递至融合端，并与RAA分支建立的跨位置上下文进行融合，形成局部特征与全局信息的互补表示。
```

英文译文：

```latex
2. \textbf{Local branch preservation.} In LGFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

### 源文件块 28

中文原文：

```latex
DSConv-S采用两倍通道扩展。给定输入特征$\mathbf X\in\mathbb R^{B\times N\times d}$，其中$B$、$N$和$d$分别表示批量大小、序列长度和嵌入维度，输入首先经转置使嵌入维度对应卷积通道维度，随后通过第一层$1\times1$逐点卷积将通道维度扩展至$2d$：
```

英文译文：

```latex
DSConv-S uses a channel expansion factor of two. Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:
```

### 源文件块 30

中文原文：

```latex
扩展后的特征通过$1\times5$深度卷积，该卷积在各通道内独立处理序列特征，以提取短邻域信息：
```

英文译文：

```latex
The expanded features pass through a $1\times5$ depthwise convolution, which processes the sequence features independently within each channel to extract information from a short local neighborhood:
```

### 源文件块 32

中文原文：

```latex
随后，应用ReLU激活函数引入非线性：
```

英文译文：

```latex
A ReLU activation is then applied to introduce nonlinearity:
```

### 源文件块 34

中文原文：

```latex
之后，第二层$1\times1$逐点卷积融合不同通道的信息，并将通道维度恢复为$d$：
```

英文译文：

```latex
Next, the second $1\times1$ pointwise convolution fuses features across channels and restores the channel dimension to $d$:
```

### 源文件块 36

中文原文：

```latex
最后，输出经逆转置恢复至原始排列，并与输入通过残差连接融合：
```

英文译文：

```latex
Finally, the output is transposed back to its original arrangement and combined with the input through a residual connection:
```

### 源文件块 38

中文原文：

```latex
其中，$\operatorname{PW}_{\uparrow}$和$\operatorname{PW}_{\downarrow}$分别表示通道扩展和通道恢复的逐点卷积，$\operatorname{DW}_{5}$表示尺寸为$1\times5$的深度卷积，$\mathcal T(\cdot)$与$\mathcal T^{-1}(\cdot)$分别表示转置和逆转置操作。
```

英文译文：

```latex
where $\operatorname{PW}_{\uparrow}$ and $\operatorname{PW}_{\downarrow}$ denote the pointwise convolutions for channel expansion and restoration, respectively, $\operatorname{DW}_{5}$ denotes the $1\times5$ depthwise convolution, and $\mathcal T(\cdot)$ and $\mathcal T^{-1}(\cdot)$ denote the transpose and inverse transpose operations, respectively.
```

### 源文件块 39

中文原文：

```latex
\textbf{计算分析。} 在两倍通道扩展条件下，DSConv-S的计算成本主要来自两层$1\times1$逐点卷积和一层$1\times5$深度卷积，可表示为：
```

英文译文：

```latex
\textbf{Computational analysis.} With a channel expansion factor of two, the computational cost of DSConv-S mainly comes from two $1\times1$ pointwise convolutions and one $1\times5$ depthwise convolution and can be expressed as:
```

### 源文件块 41

中文原文：

```latex
其中，$2C_{\mathrm{out}}$和$D_F\times D_F$分别表示扩展后的通道数和特征图尺寸。
```

英文译文：

```latex
where $2C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of channels and the feature map size, respectively.
```

### 源文件块 42

中文原文：

```latex
\subsubsection{DSConv-L：长尺度特征细化}
```

英文译文：

```latex
\subsubsection{DSConv-L: Feature refinement over longer time scales}
```

### 源文件块 43

中文原文：

```latex
DSConv-L置于SLFA之后，采用三倍通道扩展和$1\times31$深度卷积，从融合表示中提取较长时间尺度的退化特征。两层$1\times1$逐点卷积分别完成通道扩展与恢复，整体变换顺序与DSConv-S一致；其残差连接在MS-AgentNet Block层完成，如式\eqref{eq:block_dsconv_l}所示。
```

英文译文：

```latex
DSConv-L follows LGFA and uses a channel expansion factor of three and a $1\times31$ depthwise convolution to extract degradation features over longer time scales from the fused representation. Two $1\times1$ pointwise convolutions expand and restore the channel dimension, respectively, following the same transformation order as DSConv-S. Its residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}.
```

### 源文件块 44

中文原文：

```latex
\textbf{计算分析。} 在三倍通道扩展条件下，DSConv-L的计算成本可表示为：
```

英文译文：

```latex
\textbf{Computational analysis.} With a channel expansion factor of three, the computational cost of DSConv-L can be expressed as:
```

### 源文件块 46

中文原文：

```latex
其中，$3C_{\mathrm{out}}$和$D_F\times D_F$分别表示扩展后的通道数和特征图尺寸。
```

英文译文：

```latex
where $3C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of channels and the feature map size, respectively.
```

### 源文件块 48

中文原文：

```latex
\subsection{所提出的轻量级局部—全局融合注意力模块}
```

英文译文：

```latex
\subsection{The proposed Local-Global Fusion Attention module}
```

### 源文件块 49

中文原文：

```latex
本节给出多头自注意力的一般形式，简要比较Softmax注意力与线性注意力，并在此基础上介绍所提出的SLFA模块。该模块兼顾局部—全局特征建模与计算效率。
```

英文译文：

```latex
This section presents the general form of multi-head self-attention, briefly compares Softmax attention and linear attention, and then introduces the proposed LGFA module, which combines local-global feature modeling with computational efficiency.
```

### 源文件块 50

中文原文：

```latex
\subsubsection{多头自注意力的一般形式}
```

英文译文：

```latex
\subsubsection{General form of multi-head self-attention}
```

### 源文件块 51

中文原文：

```latex
多头自注意力通过多个并行注意力头在不同表示子空间内计算特征之间的相关性\cite{ref34}。设输入特征为$\mathbf X\in\mathbb R^{N\times d}$，第$i$个注意力头的查询、键和值表示为：
```

英文译文：

```latex
Multi-head self-attention uses multiple parallel attention heads, each calculating correlations between features within a different representation subspace\cite{ref34}. Given input features $\mathbf X\in\mathbb R^{N\times d}$, the query, key, and value representations of the $i$th attention head are:
```

### 源文件块 53

中文原文：

```latex
其中，$N$为序列长度，$d$为输入特征维度，$\mathbf W_i^Q,\mathbf W_i^K,\mathbf W_i^V\in\mathbb R^{d\times d_h}$为可学习投影矩阵，$i=1,2,\ldots,h$，$h$为注意力头数，$d_h=d/h$为单个注意力头的特征维度。
```

英文译文：

```latex
where $N$ is the sequence length, $d$ is the input feature dimension, and $\mathbf W_i^Q,\mathbf W_i^K,\mathbf W_i^V\in\mathbb R^{d\times d_h}$ are learnable linear projection matrices. Here, $i=1,2,\ldots,h$, $h$ is the number of attention heads, and $d_h=d/h$ is the feature dimension of each head.
```

### 源文件块 54

中文原文：

```latex
在采用非负相似度函数构造归一化注意力权重时，第$i$个注意力头在第$p$个位置的输出可表示为：
```

英文译文：

```latex
When a nonnegative similarity function is used to construct normalized attention weights, the output at the $p$th position of the $i$th attention head can be expressed as:
```

### 源文件块 56

中文原文：

```latex
其中，$\mathbf Q_{i,p}$表示第$i$个注意力头中第$p$个位置的查询，$\mathbf K_{i,j}$和$\mathbf V_{i,j}$分别表示第$j$个位置的键和值，$\operatorname{Sim}(\cdot,\cdot)$表示非负相似度函数\cite{ref40}。
```

英文译文：

```latex
where $\mathbf Q_{i,p}$ is the query at the $p$th position in the $i$th attention head, $\mathbf K_{i,j}$ and $\mathbf V_{i,j}$ are the key and value at the $j$th position, respectively, and $\operatorname{Sim}(\cdot,\cdot)$ is a nonnegative similarity function\cite{ref40}.
```

### 源文件块 57

中文原文：

```latex
所有位置的输出共同构成第$i$个注意力头的输出矩阵$\mathbf O_i\in\mathbb R^{N\times d_h}$，各注意力头的输出随后沿特征维度拼接。不同注意力机制的主要区别在于相似度函数及其计算顺序。
```

英文译文：

```latex
The outputs at all positions form the output matrix $\mathbf O_i\in\mathbb R^{N\times d_h}$ of the $i$th attention head. The outputs of all heads are then concatenated along the feature dimension. Attention mechanisms mainly differ in their similarity functions and computation order.
```

### 源文件块 58

中文原文：

```latex
\subsubsection{Softmax注意力与线性注意力}
```

英文译文：

```latex
\subsubsection{Softmax attention and linear attention}
```

### 源文件块 59

中文原文：

```latex
标准Softmax注意力通过查询与键的点积计算序列位置之间的相关性，并利用Softmax函数对相关性得分进行归一化\cite{ref34}。第$i$个注意力头的输出可表示为：
```

英文译文：

```latex
Standard Softmax attention calculates correlations between sequence positions through query-key dot products and normalizes the similarity scores using the Softmax function\cite{ref34}. The output of the $i$th attention head can be expressed as:
```

### 源文件块 61

中文原文：

```latex
Softmax中的指数映射与归一化使相关性较高的查询—键对获得更大的注意力权重\cite{ref34}。然而，$\mathbf Q_i\mathbf K_i^{\mathrm T}$需要计算所有查询与键之间的两两关系，并形成尺寸为$N\times N$的注意力矩阵。因此，单个注意力头的计算复杂度为$O(N^2d_h)$，相关性矩阵的存储复杂度为$O(N^2)$；随着序列长度增加，其计算与存储开销会显著增大\cite{ref34,ref39}。
```

英文译文：

```latex
The exponential mapping and normalization in Softmax assign larger attention weights to more highly correlated query-key pairs\cite{ref34}. However, computing $\mathbf Q_i\mathbf K_i^{\mathrm T}$ requires pairwise similarity calculations between all queries and keys, forming an $N\times N$ attention score matrix. Thus, the computational complexity of one attention head is $O(N^2d_h)$, and the memory complexity of the attention score matrix is $O(N^2)$. As the sequence length increases, the computational and storage overhead grows substantially\cite{ref34,ref39}.
```

### 源文件块 62

中文原文：

```latex
针对Softmax注意力的二次计算开销，线性注意力利用核函数$\phi(\cdot)$映射查询和键，并借助矩阵乘法结合律重新组织计算顺序\cite{ref40}。第$i$个注意力头的输出可写为：
```

英文译文：

```latex
To address the quadratic computational cost of Softmax attention, linear attention maps queries and keys through a kernel function $\phi(\cdot)$ and rearranges the computation order using the associative property of matrix multiplication\cite{ref40}. The output of the $i$th attention head can be written as:
```

### 源文件块 64

中文原文：

```latex
其中，$\phi(\cdot)$表示非负特征映射，例如$\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$；$\mathbf 1$表示全1向量，用于计算对应的归一化项\cite{ref40}。
```

英文译文：

```latex
where $\phi(\cdot)$ is a nonnegative feature mapping, such as $\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$, and $\mathbf 1$ is an all-ones vector used to calculate the corresponding normalization term\cite{ref40}.
```

### 源文件块 65

中文原文：

```latex
通过优先计算$\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$，线性注意力避免了完整$N\times N$注意力矩阵的构造。当特征映射维度与$d_h$一致时，其计算复杂度为$O(Nd_h^2)$；当$d_h$固定时，该复杂度关于序列长度$N$为线性\cite{ref40}。
```

英文译文：

```latex
By first calculating $\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$, linear attention avoids constructing the full $N\times N$ attention matrix. When the feature mapping dimension equals $d_h$, its computational complexity is $O(Nd_h^2)$. For a fixed $d_h$, this complexity is linear in the sequence length $N$\cite{ref40}.
```

### 源文件块 66

中文原文：

```latex
线性注意力以较低计算复杂度完成全局信息交互，但其计算过程未显式引入局部邻域特征\cite{ref31,ref39,ref40,ref64}。因此，需要进一步协同建模跨位置交互与局部特征。
```

英文译文：

```latex
Linear attention enables global information interactions at a lower computational complexity, but its computation does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref40,ref64}. Joint modeling of cross-position interactions and local features is therefore needed.
```

### 源文件块 67

中文原文：

```latex
\subsubsection{所提出的SLFA模块}
```

英文译文：

```latex
\subsubsection{The proposed LGFA module}
```

### 源文件块 68

中文原文：

```latex
为同时捕获局部邻域特征与跨位置交互，本文将DSConv-S与所构建的ReLU²智能体注意力（ReLU² Agent Attention，RAA）相结合，提出SLFA模块，其结构如\cref{fig:3-3}(d)所示。该模块采用局部分支与RAA分支的融合形式：DSConv-S首先提取局部表示，RAA随后以该表示为输入完成跨位置特征交互，两个分支的输出经加法融合。
```

英文译文：

```latex
To capture both local neighborhood features and cross-position interactions, this study combines DSConv-S with the developed ReLU² Agent Attention (RAA) to form the LGFA module, as shown in \cref{fig:3-3}(d). The module fuses a local branch with an RAA branch: DSConv-S first extracts a local representation, and RAA then uses this representation to establish cross-position feature interactions. The outputs of the two branches are fused by addition.
```

### 源文件块 69

中文原文：

```latex
\textbf{（1）ReLU²智能体注意力。}
```

英文译文：

```latex
\textbf{(1) ReLU² Agent Attention.}
```

### 源文件块 70

中文原文：

```latex
Agent Attention以少量智能体作为信息中介，将序列位置之间的全局交互分解为上下文聚合与信息广播两个阶段\cite{ref46}：智能体首先从键和值中聚合序列上下文，各查询位置随后从智能体上下文中读取信息。
```

英文译文：

```latex
Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into two stages: context aggregation and information broadcasting\cite{ref46}. The agents first aggregate sequence context from the keys and values, and each query position then reads information from the agent context.
```

### 源文件块 71

中文原文：

```latex
为降低查询、键和值生成过程中的参数开销，RAA采用可学习通道缩放调节不同特征通道的相对贡献，并将缩放后的特征划分至各注意力头：
```

英文译文：

```latex
To reduce the parameter overhead of query, key, and value generation, RAA uses learnable channel scaling to adjust the relative contributions of different feature channels and splits the scaled features across attention heads:
```

### 源文件块 73

中文原文：

```latex
其中，$\mathbf s_q,\mathbf s_k,\mathbf s_v\in\mathbb R^d$为可学习通道缩放向量，$\odot$表示逐元素相乘，$\operatorname{Split}_i(\cdot)$表示沿特征维度划分为$h$个$d_h$维子空间并取第$i$个子空间。
```

英文译文：

```latex
where $\mathbf s_q,\mathbf s_k,\mathbf s_v\in\mathbb R^d$ are learnable channel scaling vectors, $\odot$ denotes element-wise multiplication, and $\operatorname{Split}_i(\cdot)$ divides the feature dimension into $h$ subspaces of dimension $d_h$ and selects the $i$th subspace.
```

### 源文件块 74

中文原文：

```latex
相较于标准查询、键和值线性投影约$3d^2$的参数量，三组通道缩放向量仅包含$3d$个参数，从而降低了查询、键和值生成过程中的参数开销。
```

英文译文：

```latex
Compared with standard linear projections for queries, keys, and values, which require approximately $3d^2$ parameters, the three channel scaling vectors contain only $3d$ parameters, reducing the parameter overhead of query, key, and value generation.
```

### 源文件块 75

中文原文：

```latex
RAA设置$n_a=2$个可学习智能体，以矩阵$\mathbf A\in\mathbb R^{n_a\times d}$表示，其参数通过训练学习，并在不同输入样本间共享。
```

英文译文：

```latex
RAA uses $n_a=2$ learnable agents, represented by a matrix $\mathbf A\in\mathbb R^{n_a\times d}$. Their parameters are learned during training and shared across input samples.
```

### 源文件块 76

中文原文：

```latex
沿特征维度将全局智能体矩阵$\mathbf A$划分为$h$个子空间，第$i$个注意力头对应的智能体表示为$\mathbf A_i=\operatorname{Split}_i(\mathbf A)\in\mathbb R^{n_a\times d_h}$。
```

英文译文：

```latex
The global agent matrix $\mathbf A$ is divided into $h$ subspaces along the feature dimension. The agent representation for the $i$th attention head is $\mathbf A_i=\operatorname{Split}_i(\mathbf A)\in\mathbb R^{n_a\times d_h}$.
```

### 源文件块 77

中文原文：

```latex
在信息广播阶段，查询需要根据自身与两个智能体的匹配关系分配上下文权重。标准Agent Attention在聚合与广播阶段均采用Softmax归一化。当一行得分按共同正比例缩小时，正得分之间的相对比例虽然保持不变，权重却趋于均匀，使对应查询对两个智能体上下文的读取趋向等权混合。为在这种尺度变化下保留正相关匹配的区分，RAA在两个阶段采用ReLU²行归一化：
```

英文译文：

```latex
During information broadcasting, each query assigns broadcasting weights according to how it matches the two agents. Standard Agent Attention uses Softmax normalization in both aggregation and broadcasting. When all scores in a row are reduced by a common positive scaling factor, the relative ratios between positive scores remain unchanged, but the weights approach a uniform distribution. The corresponding query therefore reads an increasingly equal mixture of the two agent contexts. To preserve the distinction between positive matches under such scale changes, RAA uses ReLU² row normalization in both stages:
```

### 源文件块 79

中文原文：

```latex
其中，$M$表示每一行参与归一化的元素数量：在智能体聚合阶段，$M=N$；在信息广播阶段，$M=n_a$。ReLU截断非正相关性得分。对于含有正得分的行，共同正尺度的平方在分子与分母中相互抵消，因此整体得分按共同正比例变化时，权重分配保持不变。平方操作进一步增大较大与较小正得分的权重比，使归一化权重更加突出较高的正相关性得分。当某一行不存在正相关性得分时，$\mathcal R_2(\cdot)$返回均匀分布，以保持归一化结果的有效性。
```

英文译文：

```latex
where $M$ is the number of elements normalized in each row: $M=N$ during agent aggregation and $M=n_a$ during information broadcasting. ReLU sets nonpositive similarity scores to zero. For a row containing positive scores, the squared common positive scaling factor cancels between the numerator and denominator. Thus, the weight distribution remains unchanged when all scores are scaled by the same positive factor. Squaring further increases the weight ratio between larger and smaller positive scores, giving greater emphasis to higher positive similarity scores. When a row contains no positive similarity scores, $\mathcal R_2(\cdot)$ returns a uniform distribution to keep the normalization valid.
```

### 源文件块 80

中文原文：

```latex
在智能体聚合阶段，$\mathbf A_i$作为查询，从序列的键和值中汇集上下文：
```

英文译文：

```latex
During agent aggregation, $\mathbf A_i$ acts as the query to gather context from the sequence keys and values:
```

### 源文件块 82

中文原文：

```latex
其中，$\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$表示智能体对各序列位置的聚合权重，$\mathbf V_{A,i}\in\mathbb R^{n_a\times d_h}$表示聚合得到的智能体上下文。
```

英文译文：

```latex
where $\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$ contains the agents' aggregation weights for each sequence position, and $\mathbf V_{A,i}\in\mathbb R^{n_a\times d_h}$ is the resulting agent context.
```

### 源文件块 83

中文原文：

```latex
在信息广播阶段，各查询位置根据自身特征从智能体上下文中读取信息：
```

英文译文：

```latex
During information broadcasting, each query position reads information from the agent context according to its own features:
```

### 源文件块 85

中文原文：

```latex
其中，$\boldsymbol{\Phi}_{q,i}\in\mathbb R^{N\times n_a}$表示各查询位置对智能体的广播权重，$\mathbf O_i\in\mathbb R^{N\times d_h}$为第$i$个注意力头的输出。各查询与智能体的匹配得分经ReLU²行归一化得到广播权重，用于对两个智能体上下文进行加权组合，形成相应的全局交互表示。
```

英文译文：

```latex
where $\boldsymbol{\Phi}_{q,i}\in\mathbb R^{N\times n_a}$ contains the broadcasting weights assigned to the agents by each query position, and $\mathbf O_i\in\mathbb R^{N\times d_h}$ is the output of the $i$th attention head. ReLU² row normalization converts query-agent similarity scores into broadcasting weights, which combine the two agent contexts to form the corresponding global interaction representation.
```

### 源文件块 86

中文原文：

```latex
由式\eqref{eq:agent_aggregation}和式\eqref{eq:agent_broadcast}可知，从等效映射角度看，第$i$个注意力头中智能体介导的序列交互可表示为$\boldsymbol{\Phi}_{q,i}\boldsymbol{\Phi}_{k,i}\in\mathbb R^{N\times N}$，其秩不超过智能体数量$n_a$。
```

英文译文：

```latex
Equations \eqref{eq:agent_aggregation} and \eqref{eq:agent_broadcast} show that the agent-mediated sequence interaction in the $i$th attention head can be represented by the equivalent mapping $\boldsymbol{\Phi}_{q,i}\boldsymbol{\Phi}_{k,i}\in\mathbb R^{N\times N}$, whose rank is at most the number of agents $n_a$.
```

### 源文件块 87

中文原文：

```latex
各注意力头的输出沿特征维度拼接，并通过可学习输出缩放向量$\mathbf s_o$调节通道响应，随后与输入特征进行残差相加：
```

英文译文：

```latex
The outputs of all attention heads are concatenated along the feature dimension. A learnable output scaling vector $\mathbf s_o$ then adjusts the channel responses, and the result is added to the input features through a residual connection:
```

### 源文件块 89

中文原文：

```latex
其中，$\operatorname{Concat}(\cdot)$表示沿特征维度拼接各注意力头的输出，$\mathbf s_o\in\mathbb R^d$为可学习输出缩放向量。
```

英文译文：

```latex
where $\operatorname{Concat}(\cdot)$ concatenates the outputs of all attention heads along the feature dimension, and $\mathbf s_o\in\mathbb R^d$ is a learnable output scaling vector.
```

### 源文件块 90

中文原文：

```latex
RAA在聚合与广播阶段分别生成$n_a\times N$和$N\times n_a$相关性矩阵。由此，单个注意力头的计算复杂度为$O(Nn_ad_h)$，$h$个注意力头的总计算复杂度为$O(Nn_ad)$，相关性权重的存储规模为$O(hNn_a)$。当$h$和$n_a$固定时，计算量与存储量均随序列长度$N$线性增长。
```

英文译文：

```latex
RAA generates attention weight matrices of size $n_a\times N$ and $N\times n_a$ during aggregation and broadcasting, respectively. The computational complexity is therefore $O(Nn_ad_h)$ for one attention head and $O(Nn_ad)$ for all $h$ heads, while the memory required for the attention weights is $O(hNn_a)$. With fixed $h$ and $n_a$, both computation and memory grow linearly with the sequence length $N$.
```

### 源文件块 91

中文原文：

```latex
\textbf{（2）局部—全局特征融合。}
```

英文译文：

```latex
\textbf{(2) Local-global feature fusion.}
```

### 源文件块 92

中文原文：

```latex
输入特征$\mathbf X$首先经DSConv-S得到局部表示$\mathbf X_S=\operatorname{DSConv\text{-}S}(\mathbf X)$，随后分别进入局部分支和RAA分支。局部分支对$\mathbf X_S$进行层归一化，RAA分支通过智能体聚合与信息广播建立跨位置特征交互。SLFA的融合输出$\mathbf X_F$计算如下：
```

英文译文：

```latex
The input features $\mathbf X$ first pass through DSConv-S to obtain the local representation $\mathbf X_S=\operatorname{DSConv\text{-}S}(\mathbf X)$, which is then fed into the local and RAA branches. The local branch applies layer normalization to $\mathbf X_S$, while the RAA branch establishes cross-position feature interactions through agent aggregation and information broadcasting. The fused output $\mathbf X_F$ of LGFA is calculated as:
```

### 源文件块 94

中文原文：

```latex
其中，$\mathbf X_F$表示SLFA的融合输出，$\operatorname{LN}(\mathbf X_S)$为局部分支的归一化表示，$\operatorname{RAA}(\mathbf X_S)$为RAA分支输出；$\operatorname{Dropout}(\cdot)$用于训练阶段的正则化\cite{ref75}，$W_a$为调节RAA分支贡献的可学习缩放系数。
```

英文译文：

```latex
where $\mathbf X_F$ is the fused LGFA output, $\operatorname{LN}(\mathbf X_S)$ is the normalized local branch representation, and $\operatorname{RAA}(\mathbf X_S)$ is the RAA branch output. $\operatorname{Dropout}(\cdot)$ provides regularization during training\cite{ref75}, and $W_a$ is a learnable scaling factor that adjusts the contribution of the RAA branch.
```

### 源文件块 95

中文原文：

```latex
这种加性连接保留了DSConv-S提取的局部退化特征，并融合RAA建立的跨位置上下文，在形成局部—全局联合表示的同时，保持关于序列长度$N$的线性计算复杂度。
```

英文译文：

```latex
This additive fusion preserves the local degradation features extracted by DSConv-S and combines them with the cross-position context established by RAA, forming a joint local-global representation while maintaining linear computational complexity with respect to the sequence length $N$.
```

## chapter04.tex

### 源文件块 1

中文原文：

```latex
本节基于四个公开电池数据集对所提 MS-AgentNet 模型进行系统性评估。研究设置多组验证实验，主要包含健康指标有效性验证、模型性能对比分析、模块消融与复杂度评估以及跨域适应性测试。其中，健康指标有效性实验用于验证所选特征对电池退化模式的表征能力，可有效评价模型输入的合理性；模型对比实验用于检验所提方法在跨电池场景下的估计精度与稳定性；通过消融实验与复杂度分析可量化核心模块的贡献程度，并评估模型的计算效率；最终通过跨数据集迁移实验进一步考察模型对数据域差异的适应能力。综合上述多维度实验结果，可全面验证所提 MS-AgentNet 模型在电池 SOH 估计任务中的有效性与适用性。
```

英文译文：

```latex
This section systematically evaluates MS-AgentNet on four public battery datasets. The experiments cover HI effectiveness, model performance comparisons, module ablation and complexity analysis, and cross-domain adaptation. The HI experiments examine whether the selected features can represent battery degradation patterns and thus provide suitable model inputs. The model comparisons assess estimation accuracy and stability across cells. Ablation studies and complexity analysis quantify the contributions of core modules and evaluate computational efficiency. Finally, cross-dataset transfer experiments further examine the model's ability to adapt to differences between data domains. Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.
```

### 源文件块 2

中文原文：

```latex
\subsection{评价指标}
```

英文译文：

```latex
\subsection{Evaluation metrics}
```

### 源文件块 3

中文原文：

```latex
为评价模型的 SOH 估计性能，选取平均绝对误差（MAE）、平均绝对百分比误差（MAPE）、均方根误差（RMSE）和决定系数（R²）四项常用指标\cite{ref76}。
```

英文译文：

```latex
Four commonly used metrics are selected to evaluate SOH estimation performance: mean absolute error (MAE), mean absolute percentage error (MAPE), root mean square error (RMSE), and the coefficient of determination (R²)\cite{ref76}.
```

### 源文件块 4

中文原文：

```latex
MAE 表示全部评价样本中预测 SOH 与真实 SOH 之间绝对误差的平均值，用于反映模型的整体误差水平。该指标不会进一步放大单个较大偏差，能够较为直观地衡量总体估计精度。
```

英文译文：

```latex
MAE is the mean absolute difference between predicted and true SOH over all evaluation samples and reflects the overall error level. It does not assign extra weight to individual large errors and provides a direct measure of overall estimation accuracy.
```

### 源文件块 5

中文原文：

```latex
MAPE 通过真实 SOH 对绝对误差进行归一化，便于比较不同数据集上的估计性能。当真实 SOH 接近零时，MAPE 可能被显著放大，需结合 MAE 和 RMSE 进行综合评价。
```

英文译文：

```latex
MAPE normalizes absolute errors by the true SOH, allowing estimation performance to be compared across datasets. When the true SOH approaches zero, MAPE may become much larger and should be considered together with MAE and RMSE.
```

### 源文件块 6

中文原文：

```latex
RMSE 表示预测 SOH 与真实 SOH 之间均方误差的平方根。与 MAE 相比，RMSE 对较大的预测偏差赋予更高权重，可以进一步反映模型对较大误差的控制能力。
```

英文译文：

```latex
RMSE is the square root of the mean squared difference between predicted and true SOH. Compared with MAE, it assigns greater weight to large prediction deviations and thus further reflects the model's ability to limit large errors.
```

### 源文件块 7

中文原文：

```latex
R² 衡量模型对真实 SOH 变化的拟合程度，其值越接近 1，表明模型对整体退化趋势的拟合效果越好。
```

英文译文：

```latex
R² measures how well the model fits variations in the true SOH. A value closer to 1 indicates a better fit to the overall degradation trend.
```

### 源文件块 8

中文原文：

```latex
上述四项指标的数学定义如下：
```

英文译文：

```latex
The four metrics are defined as follows:
```

### 源文件块 13

中文原文：

```latex
其中，$y_i$ 和 $\hat{y}_i$ 分别表示第 $i$ 个样本的真实 SOH 和预测 SOH，$\bar{y}$ 表示评价样本中真实 SOH 的平均值，$n$ 表示评价样本总数。
```

英文译文：

```latex
where $y_i$ and $\hat{y}_i$ are the true and predicted SOH of the $i$th sample, respectively, $\bar{y}$ is the mean true SOH of the evaluation samples, and $n$ is the total number of evaluation samples.
```

### 源文件块 14

中文原文：

```latex
\subsection{健康指标筛选结果与有效性分析}
```

英文译文：

```latex
\subsection{HI selection results and effectiveness analysis}
```

### 源文件块 15

中文原文：

```latex
为验证组级健康指标筛选方法在识别跨电池稳定输入方面的有效性，本节以 Oxford 数据集为例比较不同健康指标输入下的 SOH 估计性能。根据 Cell1 上候选指标的 PCC 和 SCC，从 IC、DTV 和 DTC 三类特征中各选取一项综合相关性最高的指标，分别为 HI4、HI9 和 HI11，三者的综合相关性得分均高于 0.94。将上述指标与组级筛选得到的 CCCT 指标 HI1 分别输入 MS-AgentNet，并将 HI1、HI4、HI9 和 HI11 共同输入的方案记为 Fusion。不同输入下 Cell2--Cell8 的 SOH 估计结果见\cref{tab:4-hi-input}。
```

英文译文：

```latex
To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset. Based on the PCC and SCC of candidate HIs on Cell1, the indicator with the highest combined correlation score is selected from each of the IC, DTV, and DTC categories, giving HI4, HI9, and HI11, respectively. All three combined correlation scores exceed 0.94. These HIs and the CCCT indicator HI1, which is obtained through group-level selection, are separately fed into MS-AgentNet. The input combining HI1, HI4, HI9, and HI11 is denoted as Fusion. The validation result on Cell2 and the test results on Cell3--Cell8 with different inputs are given in \cref{tab:4-hi-input}.
```

### 源文件块 16

中文原文：

```latex
结果表明，HI1 在 Cell2--Cell8 上始终保持较高的估计精度，其平均 MAE、RMSE 和 MAPE 均为五种输入方案中的最低值，平均 MAPE 为 0.00615，即 0.615\%。当四项健康指标共同作为输入时，Fusion 的三项平均误差均排名第四，说明多类健康指标的直接组合没有形成进一步的性能增益。
```

英文译文：

```latex
The results show that using HI1 consistently yields high estimation accuracy across Cell2--Cell8, with the lowest average MAE, RMSE, and MAPE among the five input schemes. Its average MAPE is 0.00615, or 0.615\%. When all four HIs are used together, Fusion ranks fourth for all three average errors, showing that directly combining multiple types of HIs does not provide further performance gains.
```

### 源文件块 17

中文原文：

```latex
此外，同一健康指标的表征能力在不同电池间存在差异。例如，HI9 在 Cell7 上的估计误差低于 HI11，而在 Cell8 上则观察到相反结果。相比之下，组级筛选得到的 HI1 在七节电池上均取得最低的 MAE、RMSE 和 MAPE。上述结果表明，单节电池上的高相关性不能保证健康指标在组内其他电池上保持相同的表征能力，而组级筛选得到的 HI1 在该组 Oxford 电池上提供了更稳定的 SOH 估计输入。
\input{tables/table_4_hi_input}
```

英文译文：

```latex
Moreover, the representational ability of the same HI differs across cells. For example, HI9 yields lower estimation errors than HI11 on Cell7, whereas the opposite is observed on Cell8. In contrast, HI1 obtained through group-level selection achieves the lowest MAE, RMSE, and MAPE on all seven cells. These results show that a high correlation on one cell does not guarantee the same representational ability on other cells in the group. The group-selected HI1 provides a more stable input for SOH estimation on this group of Oxford cells.
\input{tables/table_4_hi_input}
```

### 源文件块 18

中文原文：

```latex
\subsection{模型训练鲁棒性与超参数分析}
```

英文译文：

```latex
\subsection{Training robustness and hyperparameter analysis}
```

### 源文件块 19

中文原文：

```latex
为进一步考察 MS-AgentNet 的训练稳定性及轻量化模型的参数设置，本文对智能体矩阵的初始化策略、模型收敛表现和超参数配置进行分析。
```

英文译文：

```latex
To further examine the training stability and parameter settings of the lightweight MS-AgentNet model, this study analyzes agent matrix initialization, model convergence, and hyperparameter configuration.
```

### 源文件块 20

中文原文：

```latex
\subsubsection{智能体矩阵初始化与收敛性分析}
```

英文译文：

```latex
\subsubsection{Agent matrix initialization and convergence analysis}
```

### 源文件块 21

中文原文：

```latex
RAA 将智能体表示为与输入无关的静态可学习矩阵 $\mathbf A\in\mathbb R^{n_a\times d}$，用于全局特征聚合，智能体数量固定为 $n_a=2$。矩阵参数采用均值为 0、标准差为 0.02 的正态分布初始化：
```

英文译文：

```latex
RAA represents the agents as a static learnable matrix $\mathbf A\in\mathbb R^{n_a\times d}$ that is independent of the input and used for global feature aggregation. The number of agents is fixed at $n_a=2$. The matrix parameters are initialized from a normal distribution with a mean of 0 and a standard deviation of 0.02:
```

### 源文件块 23

中文原文：

```latex
式中，$A_{ij}$ 表示第 $i$ 个智能体在第 $j$ 维特征上的参数。该初始化能够为不同智能体提供幅值较小且非一致的初始参数，避免其处于完全相同的初始状态。
```

英文译文：

```latex
where $A_{ij}$ is the parameter of the $i$th agent in the $j$th feature dimension. This initialization gives different agents small, nonidentical initial parameters, avoiding identical initial states.
```

### 源文件块 24

中文原文：

```latex
三种初始化方案的对比结果如\cref{tab:4-3-initialization}所示。各方案对应的 $R^2$ 为 0.98527～0.98645，RMSE 为 0.00774～0.00805，MAE 为 0.00485～0.00499，表明其预测性能较为接近。截断正态通过限定采样范围控制参数幅值，Xavier 均匀初始化则根据网络层的输入和输出维度调整参数方差。相比之下，普通正态初始化能够直接为静态智能体矩阵提供以零为中心的小幅随机参数，且不依赖额外的范围限制或维度缩放。因此，本文采用普通正态初始化作为默认设置。
```

英文译文：

```latex
\Cref{tab:4-3-initialization} compares the three initialization schemes. Their $R^2$ values range from 0.98527 to 0.98645, RMSE from 0.00774 to 0.00805, and MAE from 0.00485 to 0.00499, indicating similar prediction performance. Truncated normal initialization controls parameter magnitudes by restricting the sampling range, while Xavier uniform initialization adjusts parameter variance according to the input and output dimensions of a layer. In comparison, ordinary normal initialization directly provides small, zero-centered random parameters for the static agent matrix without additional range restrictions or dimension-based scaling. It is therefore used as the default setting.
```

### 源文件块 25

中文原文：

```latex
模型收敛特性通过收敛速度和训练后期损失波动共同评价。将训练损失首次降至首轮损失 10\% 以下的训练轮次定义为收敛阈值轮次，并采用最后 20 轮损失的均值和标准差描述训练后期的收敛状态。如\cref{tab:4-3}所示，各次训练均达到预设收敛阈值。Oxford 和 MIT 数据集上的收敛阈值轮次中位数分别为 26 和 7，训练后期损失标准差中位数分别为 $2.38\times10^{-4}$ 和 $4.84\times10^{-6}$。上述结果表明，MS-AgentNet 在当前实验设置下能够稳定收敛，且训练后期的损失波动较小。
```

英文译文：

```latex
Model convergence is evaluated through both convergence speed and loss fluctuations in the late training stage. The convergence threshold epoch is defined as the first epoch at which the training loss falls below 10\% of the first-epoch loss. The mean and standard deviation of the loss over the final 20 epochs describe the late-stage convergence state. As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median standard deviations of the late-stage loss are $2.38\times10^{-4}$ and $4.84\times10^{-6}$. These results show that MS-AgentNet converges stably under the current experimental settings, with small loss fluctuations in the late training stage.
```

### 源文件块 27

中文原文：

```latex
\subsubsection{超参数配置}
```

英文译文：

```latex
\subsubsection{Hyperparameter configuration}
```

### 源文件块 28

中文原文：

```latex
MS-AgentNet 的主要超参数包括学习率、网络深度 $L$ 和嵌入维度 $d$，各参数的配置范围见\cref{tab:4-1}。在上述范围内，各数据集利用特征开发集合中的两节电池完成模型训练和配置，其中一节用于模型参数学习，另一节用于超参数配置。Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 数据集对应的训练电池与配置电池分别为 Cell1 与 Cell2、CS2\_36 与 CS2\_37、CX2\_36 与 CX2\_37 以及 b3c8 与 b3c13。
```

英文译文：

```latex
The main hyperparameters of MS-AgentNet are the learning rate, network depth $L$, and embedding dimension $d$. The hyperparameter search space is listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, while a second cell is used for validation and comparison to select the best-performing hyperparameter configuration. The training and validation cells are Cell1 and Cell2 for Oxford, CS2\_36 and CS2\_37 for CALCE CS2, CX2\_36 and CX2\_37 for CALCE CX2, and b3c8 and b3c13 for MIT/Severson, respectively.
```

### 源文件块 29

中文原文：

```latex
五种模型的层配置见\cref{tab:4-4}。
```

英文译文：

```latex
The layer configurations of the five models are given in \cref{tab:4-4}.
```

### 源文件块 31

中文原文：

```latex
确定后的模型配置保持不变。在后续 SOH 估计性能比较中，MS-AgentNet 采用学习率 0.001、网络深度 $L=1$ 和嵌入维度 $d=16$。
```

英文译文：

```latex
Once selected, the model configurations remain fixed. In the subsequent SOH estimation comparisons, MS-AgentNet uses a learning rate of 0.001, network depth $L=1$, and embedding dimension $d=16$.
```

### 源文件块 33

中文原文：

```latex
\subsection{SOH估计精度与跨电池泛化性能比较}
```

英文译文：

```latex
\subsection{Comparison of SOH estimation accuracy and cross-cell generalization}
```

### 源文件块 34

中文原文：

```latex
根据第~2.3~节的筛选结果，Oxford 数据集采用 HI1，CALCE CS2 数据集采用 HI1 和 HI2，CALCE CX2 数据集采用 HI13，MIT/Severson 数据集采用 HI14 和 HI15。在上述健康指标输入下，进一步比较 MS-AgentNet 与四种基线模型的 SOH 估计性能。
```

英文译文：

```latex
Based on the selection results in Section~2.3, the inputs are HI1 for Oxford, HI1 and HI2 for CALCE CS2, HI13 for CALCE CX2, and HI14 and HI15 for MIT/Severson. With these HI inputs, the SOH estimation performance of MS-AgentNet is further compared with that of four baseline models.
```

### 源文件块 35

中文原文：

```latex
\subsubsection{Oxford数据集上的估计精度分析}
```

英文译文：

```latex
\subsubsection{Estimation accuracy on the Oxford dataset}
```

### 源文件块 36

中文原文：

```latex
\Cref{fig:4-2}和\cref{tab:4-5}展示了 MS-AgentNet、CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 在 Oxford Cell2--Cell8 上的 SOH 估计结果和误差。
```

英文译文：

```latex
\Cref{fig:4-2} and \cref{tab:4-5} present the validation results on Oxford Cell2 and the test results on Cell3--Cell8 for MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM.
```

### 源文件块 38

中文原文：

```latex
总体而言，各模型均能够跟踪电池的容量衰减趋势，但在局部变化区间的预测结果上存在差异。值得注意的是，Cell4 的局部偏离和 Cell6 后段的快速下降使各模型表现出不同程度的跟踪偏差。局部放大结果显示，MS-AgentNet 在上述变化区间仍能较好地跟踪真实 SOH。对于退化轨迹相对平滑的 Cell3 和 Cell5，其预测结果也与真实 SOH 保持较好的贴合。
```

英文译文：

```latex
Overall, all models track the capacity fade trends, but their predictions differ in regions with local variations. In particular, the local deviations in Cell4 and the rapid decline in the later stage of Cell6 lead to different degrees of tracking error. The enlarged views show that MS-AgentNet still tracks the true SOH well in these regions. Its predictions also closely follow the true SOH of Cell3 and Cell5, whose degradation trajectories are relatively smooth.
```

### 源文件块 39

中文原文：

```latex
定量结果表明，MS-AgentNet 在 Cell2、Cell3、Cell5 和 Cell6 上的 $R^2$、MAE、MAPE 和 RMSE 均为最优，并在 Cell4 上取得最高的 $R^2$ 和最低的 RMSE。从 Cell2--Cell8 的平均结果来看，MS-AgentNet 的平均 $R^2$ 为 0.98379，平均 MAE、MAPE 和 RMSE 分别为 0.00524、0.00615 和 0.00638，均在五种模型中排名第一。与 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 相比，其平均 MAE 分别降低了 2.42\%、8.87\%、4.20\% 和 12.52\%，平均 MAPE 分别降低了 2.38\%、8.48\%、3.76\% 和 12.52\%，平均 RMSE 分别降低了 5.06\%、11.39\%、5.62\% 和 15.83\%。上述结果表明，MS-AgentNet 在 Oxford 数据集上具有较高的 SOH 估计精度和良好的预测鲁棒性。
```

英文译文：

```latex
The quantitative results show that MS-AgentNet achieves the best $R^2$, MAE, MAPE, and RMSE on Cell2, Cell3, Cell5, and Cell6, as well as the highest $R^2$ and lowest RMSE on Cell4. Averaged over Cell2--Cell8, its $R^2$ is 0.98379, and its MAE, MAPE, and RMSE are 0.00524, 0.00615, and 0.00638, respectively, ranking first among the five models for all four metrics. Compared with CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by 2.42\%, 8.87\%, 4.20\%, and 12.52\%, its average MAPE by 2.38\%, 8.48\%, 3.76\%, and 12.52\%, and its average RMSE by 5.06\%, 11.39\%, 5.62\%, and 15.83\%, respectively. These results show that MS-AgentNet achieves high SOH estimation accuracy and good prediction robustness on the Oxford dataset.
```

### 源文件块 41

中文原文：

```latex
\subsubsection{CALCE和MIT数据集上的跨电池泛化分析}
```

英文译文：

```latex
\subsubsection{Cross-cell generalization on the CALCE and MIT datasets}
```

### 源文件块 42

中文原文：

```latex
本节进一步比较了 MS-AgentNet 与四种基线模型在 CALCE CS2、CALCE CX2 和 MIT/Severson 数据集上的 SOH 估计性能。上述数据集在电池材料和充放电协议方面与 Oxford 数据集存在差异，并呈现出平滑衰减、阶段性转折和寿命后期加速衰减等多样化退化动态。各模型的 SOH 估计结果如\cref{fig:4-3}所示。
```

英文译文：

```latex
This section further compares MS-AgentNet with the four baseline models on the CALCE CS2, CALCE CX2, and MIT/Severson datasets. CS2\_37, CX2\_37, and b3c13 are the validation cells, while CS2\_38, CX2\_38, and b3c29 are the test cells. These datasets differ from Oxford in battery chemistries and charge-discharge protocols and show diverse degradation dynamics, including smooth capacity fade, transitions between stages, and accelerated late-life degradation. The SOH estimation results are shown in \cref{fig:4-3}.
```

### 源文件块 43

中文原文：

```latex
从整体结果来看，各模型均能够跟踪不同电池的容量衰减趋势，但在局部非线性转折和寿命后期加速衰减阶段的预测表现上存在差异。其中，CX2\_38 经历了多次阶段性转折，并呈现出明显的非线性衰减尾部。局部放大结果显示，进入加速衰减阶段后，各模型的预测偏差逐渐扩大，MS-AgentNet 仍能较好地跟踪其加速衰减轨迹。对于退化轨迹较为连续的 CS2\_38 和 b3c29，MS-AgentNet 也能够保持与真实 SOH 的较好贴合。
```

英文译文：

```latex
Overall, all models track the capacity fade trends of different cells, but their prediction performance differs at local nonlinear transitions and during accelerated late-life degradation. In particular, CX2\_38 undergoes several transitions between stages and shows a clear nonlinear degradation tail. The enlarged views show that prediction deviations gradually increase during accelerated degradation, while MS-AgentNet still tracks the accelerated degradation trajectory well. For CS2\_38 and b3c29, whose degradation trajectories are more continuous, MS-AgentNet also maintains close agreement with the true SOH.
```

### 源文件块 44

中文原文：

```latex
\Cref{tab:4-6}列出了各模型在六节电池上的 SOH 估计误差。MS-AgentNet 在其中五节电池上的 $R^2$、MAE、MAPE 和 RMSE 均为最优。值得注意的是，在具有阶段性转折和非线性衰减尾部的 CX2\_38 上，MS-AgentNet 的 MAPE 仅为 0.037673，较 CNN-Transformer 和 Transformer 分别降低了 59.75\% 和 51.80\%，表明模型在寿命后期加速衰减阶段仍能保持较低的预测误差。
```

英文译文：

```latex
\Cref{tab:4-6} lists the SOH estimation errors of all models on the three validation cells and three test cells. MS-AgentNet achieves the best $R^2$, MAE, MAPE, and RMSE on five of them. Notably, on the test cell CX2\_38, which shows transitions between stages and a nonlinear degradation tail, its MAPE is only 0.037673, a reduction of 59.75\% and 51.80\% compared with CNN-Transformer and Transformer, respectively. This shows that the model maintains low prediction errors during accelerated late-life degradation.
```

### 源文件块 45

中文原文：

```latex
从六节电池的平均结果来看，MS-AgentNet 的平均 $R^2$ 为 0.9896，平均 MAE、MAPE 和 RMSE 分别为 0.00707、0.013335 和 0.01188，均在五种模型中排名第一。与 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 相比，其平均 MAE 分别降低了 13.50\%、26.02\%、9.11\% 和 22.94\%，平均 MAPE 分别降低了 42.19\%、60.08\%、34.49\% 和 58.17\%，平均 RMSE 分别降低了 12.04\%、26.52\%、7.97\% 和 23.09\%。综合不同退化场景，MS-AgentNet 在平滑衰减、阶段性转折和寿命后期加速衰减过程中均保持了较低的估计误差，体现出较好的预测鲁棒性和跨电池泛化能力。
```

英文译文：

```latex
Across the six cells, MS-AgentNet achieves an average $R^2$ of 0.9896 and average MAE, MAPE, and RMSE of 0.00707, 0.013335, and 0.01188, respectively, ranking first among the five models for all four metrics. Compared with CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by 13.50\%, 26.02\%, 9.11\%, and 22.94\%, its average MAPE by 42.19\%, 60.08\%, 34.49\%, and 58.17\%, and its average RMSE by 12.04\%, 26.52\%, 7.97\%, and 23.09\%, respectively. On the three test cells, MS-AgentNet maintains low estimation errors during smooth capacity fade, transitions between stages, and accelerated late-life degradation, showing good prediction robustness and cross-cell generalization capability.
```

### 源文件块 47

中文原文：

```latex
\subsection{跨数据集迁移实验}
```

英文译文：

```latex
\subsection{Cross-dataset transfer experiments}
```

### 源文件块 48

中文原文：

```latex
当源域与目标域来自不同数据集时，化学体系、运行协议和退化轨迹差异可能引起域偏移\cite{ref52,ref59}。为评价 MS-AgentNet 的跨数据集迁移能力，本文设置源域直接测试和少样本适应两类实验。源域直接测试（source-only）仅利用源域参考电池训练模型，并在不使用目标域数据更新参数的情况下直接测试目标域电池；少样本适应则固定特征提取模块，利用目标域参考电池前 30\% 的循环数据更新读出层，再在目标域测试电池上进行评价\cite{ref52,ref58}。
```

英文译文：

```latex
When the source and target domains come from different datasets, differences in chemistry, operating protocols, and degradation trajectories may cause domain shift\cite{ref52,ref59}. To evaluate the cross-dataset transfer capability of MS-AgentNet, this study conducts source-only evaluation and few-shot adaptation experiments. In source-only evaluation, the model is trained only on the source-domain reference cell and directly tested on the target-domain cell without updating its parameters using target-domain data. In few-shot adaptation, the feature extraction modules are frozen, and the first 30\% of cycle data from the target-domain reference cell are used to update the readout layer before evaluation on the target-domain test cell\cite{ref52,ref58}.
```

### 源文件块 49

中文原文：

```latex
CALCE CS2、CALCE CX2 和 Oxford 分别视为三个数据域，其中 CS2\_36、CX2\_36 和 Oxford Cell1 用于源域训练或目标域适应，CS2\_38、CX2\_38 和 Oxford Cell3 仅用于目标域测试。CALCE CS2 与 CALCE CX2 均属于 LCO 化学体系，Oxford 采用 NCO-LCO 混合化学体系，因此实验同时覆盖同化学体系和跨化学体系迁移。为保持源域与目标域的输入定义一致，各迁移方向统一采用 $CCCT(3.8,\allowbreak 4.0)$ 和 $Q_{\mathrm{dch}}(3.8,\allowbreak 3.4)/C_{\mathrm{rated}}$ 两项健康指标。
```

英文译文：

```latex
CALCE CS2, CALCE CX2, and Oxford are treated as three data domains. CS2\_36, CX2\_36, and Oxford Cell1 are used for source-domain training or target-domain adaptation, while CS2\_38, CX2\_38, and Oxford Cell3 are used only for target-domain testing. CALCE CS2 and CALCE CX2 both use LCO chemistry, whereas Oxford uses a blended NCO-LCO chemistry. The experiments therefore cover both same-chemistry and cross-chemistry transfer. To keep the input definitions consistent between the source and target domains, all transfer directions use two HIs: $CCCT(3.8,\allowbreak 4.0)$ and $Q_{\mathrm{dch}}(3.8,\allowbreak 3.4)/C_{\mathrm{rated}}$.
```

### 源文件块 50

中文原文：

```latex
\subsubsection{不同迁移方向的性能比较}
```

英文译文：

```latex
\subsubsection{Performance across transfer directions}
```

### 源文件块 51

中文原文：

```latex
如\cref{tab:4-7}所示，CS2→CX2 和 CX2→CS2 的 $R^2$ 分别为 0.8421 和 0.7847，MAE 分别为 0.0697 和 0.0388，表明模型在两个 CALCE 数据域之间仍能较好地表征退化趋势。相比之下，四个涉及 Oxford 的迁移方向的 MAE 为 0.1530～0.6346，且 $R^2$ 均低于 0，显示直接迁移性能随数据域组合和迁移方向发生明显变化。
```

英文译文：

```latex
As shown in \cref{tab:4-7}, CS2→CX2 and CX2→CS2 achieve $R^2$ values of 0.8421 and 0.7847 and MAE values of 0.0697 and 0.0388, respectively, indicating that the model still represents degradation trends well when transferred between the two CALCE domains. In contrast, the four transfer directions involving Oxford yield MAE values of 0.1530–0.6346 and $R^2$ values below 0, showing that direct transfer performance varies considerably with the domain pair and transfer direction.
```

### 源文件块 52

中文原文：

```latex
少样本适应结果见\cref{tab:4-8}。适应后，六个迁移方向的 MAE、MAPE 和 RMSE 均有所降低。以 MAE 为例，两个 CALCE 数据域之间的降幅为 21.91\%～45.91\%，CALCE→Oxford 方向的降幅为 86.84\%～87.61\%，Oxford→CALCE 方向的降幅为 13.27\%～31.21\%。从 $R^2$ 看，适应后的 CS2→CX2 和 CX2→CS2 分别达到 0.9566 和 0.8806，而四个涉及 Oxford 的迁移方向仍低于 0，表明涉及 Oxford 的跨数据集迁移较两个 CALCE 数据域之间的迁移更具挑战性。
```

英文译文：

```latex
The few-shot adaptation results are presented in \cref{tab:4-8}. After adaptation, MAE, MAPE, and RMSE decrease in all six transfer directions. For MAE, the reductions are 21.91\%–45.91\% between the two CALCE domains, 86.84\%–87.61\% for CALCE→Oxford, and 13.27\%–31.21\% for Oxford→CALCE. After adaptation, $R^2$ reaches 0.9566 for CS2→CX2 and 0.8806 for CX2→CS2 but remains below 0 in all four directions involving Oxford. This indicates that cross-dataset transfer involving Oxford is more challenging than transfer between the two CALCE domains.
```

### 源文件块 54

中文原文：

```latex
\subsubsection{目标域适配比例的影响}
```

英文译文：

```latex
\subsubsection{Effect of the target-domain adaptation ratio}
```

### 源文件块 55

中文原文：

```latex
分别以 CS2\_36 和 CX2\_36 作为源域，使用 Oxford Cell1 的前置循环数据进行读出层适配，并将适配比例依次设置为 10\%、30\%、50\% 和 70\%，结果见\cref{tab:4-9}。
```

英文译文：

```latex
With CS2\_36 and CX2\_36 used as the respective source domains, the readout layer is adapted with early-cycle data from Oxford Cell1 at adaptation ratios of 10\%, 30\%, 50\%, and 70\%. The results are given in \cref{tab:4-9}.
```

### 源文件块 56

中文原文：

```latex
随着适配比例由 10\% 增至 70\%，两种源域设置下的 MAE、MAPE 和 RMSE 均持续下降。以 CS2 为源域时，MAE 由 0.0831 降至 0.0252，$R^2$ 由 -1.3934 提高至 0.7650，并在 50\% 适配比例下由负转正；以 CX2 为源域时，MAE 由 0.1095 降至 0.0559，$R^2$ 由 -3.2217 提高至 70\% 适配比例下的 -0.1268。四种适配比例下，CS2 源域的 $R^2$ 均高于 CX2 源域的对应结果。
```

英文译文：

```latex
As the adaptation ratio increases from 10\% to 70\%, MAE, MAPE, and RMSE decrease continuously for both source-domain settings. With CS2 as the source domain, MAE decreases from 0.0831 to 0.0252, while $R^2$ increases from -1.3934 to 0.7650 and becomes positive at an adaptation ratio of 50\%. With CX2 as the source domain, MAE decreases from 0.1095 to 0.0559, while $R^2$ increases from -3.2217 to -0.1268 at an adaptation ratio of 70\%. At all four adaptation ratios, the CS2 source domain yields higher $R^2$ values than the CX2 source domain.
```

### 源文件块 57

中文原文：

```latex
进一步比较相邻适配比例，CS2 和 CX2 源域从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。结果表明，增加目标域观测能够持续改善模型在 Oxford 数据域上的适配性能；在相同适配比例下，CS2 源域始终取得更低的估计误差和更高的 $R^2$，进一步体现了源域选择对跨数据集适配性能的影响。
```

英文译文：

```latex
Comparing adjacent adaptation ratios, increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively. Increasing it from 50\% to 70\% gives smaller reductions of 0.0114 and 0.0055. These results show that adding target-domain observations continuously improves adaptation performance on Oxford. At the same adaptation ratio, the CS2 source domain consistently yields lower estimation errors and higher $R^2$, further showing the effect of source-domain selection on cross-dataset adaptation performance.
```

### 源文件块 59

中文原文：

```latex
\subsection{模块消融与模型复杂度分析}
```

英文译文：

```latex
\subsection{Module ablation and model complexity analysis}
```

### 源文件块 60

中文原文：

```latex
为进一步验证 MS-AgentNet 的有效性和效率，在主对比实验基础上开展消融研究与复杂度分析。消融研究通过移除或组合关键模块，考察各模块对预测性能的作用；复杂度分析则从计算量、参数量和存储占用等方面评估模型开销。
```

英文译文：

```latex
Ablation studies and complexity analysis are conducted in addition to the main comparison experiments to further evaluate the effectiveness and efficiency of MS-AgentNet. The ablation studies examine the effects of individual modules on prediction performance by removing or combining key modules, while the complexity analysis evaluates computational cost, parameter count, and storage size.
```

### 源文件块 61

中文原文：

```latex
\subsubsection{模块消融分析}
```

英文译文：

```latex
\subsubsection{Module ablation analysis}
```

### 源文件块 62

中文原文：

```latex
高效注意力通过压缩信息交互降低标准注意力的计算开销\cite{ref39,ref40,ref43,ref44}，但这一过程可能削弱局部细粒度退化信息的表达\cite{ref31}；直接叠加标准卷积虽然能够增强局部特征建模，却会增加参数量和计算负担\cite{ref31,ref71}。为兼顾局部信息保留与计算效率，MS-AgentNet 结合多尺度 DSConv 与 RAA，分别完成局部特征提取和跨位置信息交互。为考察两类模块的单独作用及组合效果，消融实验设置 M1–M4 四种变体。其中，M1 仅保留基础骨干网络，M2 在 M1 基础上加入多尺度 DSConv，M3 在 M1 基础上加入 RAA，M4 则同时集成多尺度 DSConv 与 RAA。
```

英文译文：

```latex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref31,ref71}. To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

### 源文件块 63

中文原文：

```latex
如\cref{tab:4-10}所示，与基础模型 M1 相比，加入多尺度 DSConv 后，M2 在 CX2 和 Oxford 数据集上的综合平均误差分别降低约 1.20\% 和 8.45\%；加入 RAA 后，M3 在 CS2、CX2 和 Oxford 数据集上的综合平均误差分别降低约 3.18\%、11.60\% 和 15.49\%。两种模块单独使用时均改善了部分数据集上的估计结果，但未在四个数据集上同时取得更低误差。
```

英文译文：

```latex
As shown in \cref{tab:4-10}, compared with the basic model M1, adding multi-scale DSConv in M2 reduces the combined average error by approximately 1.20\% on CX2 and 8.45\% on Oxford. Adding RAA in M3 reduces the combined average error by approximately 3.18\%, 11.60\%, and 15.49\% on CS2, CX2, and Oxford, respectively. Each module improves estimation on some datasets when used alone, but neither yields lower errors on all four datasets.
```

### 源文件块 64

中文原文：

```latex
当多尺度 DSConv 与 RAA 共同集成后，完整模型 M4 在四个数据集上均取得最低或并列最低的综合平均误差。以 CX2 和 Oxford 数据集为例，其综合平均误差分别由 M1 的 0.0500 和 0.0071 降低至 0.0225 和 0.0059，相对降低 54.94\% 和 16.52\%。在 CS2 数据集上，M3 的 MAE 略低于 M4，而 M4 在 RMSE、MAPE 和综合平均误差上表现更优。总体结果表明，完整模型获得了比单模块变体更稳定的综合表现，体现了多尺度局部特征提取与跨位置信息交互的互补作用。
```

英文译文：

```latex
When multi-scale DSConv and RAA are integrated, the full model M4 achieves the lowest or jointly lowest combined average error on all four datasets. On CX2 and Oxford, for example, it reduces the combined average error from 0.0500 and 0.0071 for M1 to 0.0225 and 0.0059, corresponding to relative reductions of 54.94\% and 16.52\%, respectively. On CS2, M3 has a slightly lower MAE than M4, while M4 achieves lower RMSE, MAPE, and combined average error. The full model provides more consistent overall performance than the single-module variants, showing the complementary roles of multi-scale local feature extraction and cross-position information interactions.
```

### 源文件块 65

中文原文：

```latex
为进一步区分多尺度 DSConv 中两个卷积尺度的作用，固定 RAA 模块并仅调整卷积尺度，设置 S0（仅保留 RAA）、S5（RAA 与核长度为 5 的 DSConv-S）、S31（RAA 与核长度为 31 的 DSConv-L）和 SFull（RAA、DSConv-S 与 DSConv-L）四种尺度变体。其中，S0 和 SFull 分别与\cref{tab:4-10}中的 M3 和 M4 对应。
```

英文译文：

```latex
To further distinguish the roles of the two convolutional scales, RAA is held fixed while only the convolutional scale is changed. Four variants are considered: S0 (RAA only), S5 (RAA with DSConv-S of kernel size 5), S31 (RAA with DSConv-L of kernel size 31), and SFull (RAA, DSConv-S, and DSConv-L). S0 and SFull correspond to M3 and M4 in \cref{tab:4-10}, respectively.
```

### 源文件块 66

中文原文：

```latex
\Cref{tab:4-11}的结果显示，单一卷积尺度的收益随数据集而变化。在具有阶段性转折和非线性衰减尾部的 CX2 数据集上，S31 将综合平均误差由 S0 的 0.0442 降至 0.0348，相对降低 21.27\%，这一结果与 DSConv-L 进行长尺度特征细化的设计目标一致。在 MIT 数据集上，S5 相对 S0 降低约 3.85\%；在 CS2 和 Oxford 数据集上，S0 的综合平均误差仍低于两个单尺度变体。当两个卷积尺度共同使用时，SFull 在四个数据集上均取得最低的综合平均误差。与最佳单尺度变体相比，SFull 在 CX2 和 MIT 数据集上的误差分别降低 35.34\% 和 20.00\%。因此，同时保留短核与长核能够取得比单一尺度更一致的综合结果，支持多尺度 DSConv 的结构设计。
```

英文译文：

```latex
\Cref{tab:4-11} shows that the benefit of a single convolutional scale varies across datasets. On CX2, which has transitions between stages and a nonlinear degradation tail, S31 reduces the combined average error from 0.0442 for S0 to 0.0348, a relative reduction of 21.27\%. This result is consistent with the design goal of DSConv-L to refine features over longer time scales. On MIT, S5 reduces the error by approximately 3.85\% relative to S0. On CS2 and Oxford, S0 still has a lower combined average error than either single-scale variant. When both convolutional scales are used, SFull achieves the lowest combined average error on all four datasets. Compared with the best single-scale variant, SFull reduces the error by 35.34\% on CX2 and 20.00\% on MIT. Thus, retaining both small and large kernels provides more consistent overall results than using a single scale, supporting the multi-scale DSConv design.
```

### 源文件块 68

中文原文：

```latex
\subsubsection{模型复杂度分析}
```

英文译文：

```latex
\subsubsection{Model complexity analysis}
```

### 源文件块 69

中文原文：

```latex
在实际应用中，除估计精度外，模型的计算效率与存储需求也是重要的评价指标\cite{ref77}。本文选取 MS-AgentNet、CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 五种模型，从 FLOPs、训练时间、可训练参数量和权重存储占用四个方面比较模型的资源开销。其中，FLOPs 通过 THOP 库的 \texttt{profile} 函数统计，并在补计注意力运算后换算为单次前向传播所需的浮点运算次数；训练时间通过 Python 的 \texttt{time} 模块以秒为单位记录，反映模型完成规定训练轮次所需的时长；可训练参数总数通过 PyTorch 统计；权重存储占用通过 Python 的 \texttt{os.path.getsize} 函数测量，并换算为 KB，表示保存模型权重所需的存储空间。所有指标均在相同实验环境下测量。
```

英文译文：

```latex
In practical applications, computational efficiency and storage requirements are important evaluation criteria alongside estimation accuracy\cite{ref77}. This study compares the resource consumption of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM using four metrics: FLOPs, training time, trainable parameter count, and storage size. FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass. Training time is recorded in seconds using Python's \texttt{time} module and represents the time needed to complete the specified number of training epochs. The total number of trainable parameters is counted using PyTorch. Storage size is measured using Python's \texttt{os.path.getsize} function and converted to KB, representing the space required to save the model weights. All metrics are measured in the same experimental environment.
```

### 源文件块 70

中文原文：

```latex
为在相同输入数据和训练条件下比较不同模型结构的复杂度，五种模型统一采用 CS2\_36 的 HI1 和 HI2 作为输入，序列长度设为 5，训练轮次、学习率、批次大小和丢弃率分别设为 1000、0.01、128 和 0.1。在模型结构设置方面，MS-AgentNet、CNN-Transformer 和 Transformer 均采用 4 个注意力头；CNN-LSTM 和 LSTM 均设置为 4 层，使 LSTM 层数与注意力头数在数值上保持一致。各模型的表示维度或隐藏维度均设为 16。相应配置及复杂度比较结果见\cref{tab:4-12}。
```

英文译文：

```latex
To compare model complexity with the same input data and training conditions, all five models use HI1 and HI2 from CS2\_36 as inputs. The number of training epochs, learning rate, batch size, and dropout rate are set to 1000, 0.01, 128, and 0.1, respectively. MS-AgentNet, CNN-Transformer, and Transformer use 4 attention heads, while CNN-LSTM and LSTM use 4 LSTM layers, making the LSTM layer count numerically equal to the attention head count. The representation or hidden dimension is set to 16 for all models. The configurations and complexity results are given in \cref{tab:4-12}.
```

### 源文件块 71

中文原文：

```latex
尽管 LSTM 在统一复杂度测试中以 44.568 s 取得最短训练时间，但其对复杂退化模式的刻画仍有局限，整体 SOH 估计精度相对较低。相比之下，MS-AgentNet 的 FLOPs、参数量和存储占用分别为 0.045760 M、4,643 和 27.44 KB，均为五种模型中的最低值。与 LSTM 相比，MS-AgentNet 的前向计算量降低 50.5\%；与 CNN-Transformer 相比，其参数量和存储占用分别降低 25.6\% 和 25.8\%；与 CNN-LSTM 相比，二者分别降低 70.8\% 和 59.8\%。这些结果表明，MS-AgentNet 在保持较高 SOH 估计精度的同时，具有更低的前向计算量、参数量和权重存储开销。
```

英文译文：

```latex
Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its ability to capture complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low. In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models. It reduces forward-pass computation by 50.5\% compared with LSTM. Its parameter count and storage size are reduced by 25.6\% and 25.8\% compared with CNN-Transformer and by 70.8\% and 59.8\% compared with CNN-LSTM, respectively. These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and storage size.
```

### 源文件块 72

中文原文：

```latex
为考察模型宽度变化下的存储开销，将五种模型的表示维度或隐藏维度分别设置为 16、32、64 和 128，其余设置保持不变。如\cref{fig:4-4}所示，五种模型的存储占用均随模型宽度增加而上升，但 MS-AgentNet 在四种测试宽度下始终保持最低值。当维度增至 128 时，其存储占用为 714.37 KB，较同一维度下最接近的 Transformer 降低 32.2\%。综合来看，MS-AgentNet 在 SOH 估计精度与计算、存储开销之间取得了较好的平衡，体现出面向资源受限 BMS 的轻量化应用潜力。
```

英文译文：

```latex
To examine storage overhead as model width changes, the representation or hidden dimension of each model is set to 16, 32, 64, and 128, with all other settings unchanged. As shown in \cref{fig:4-4}, storage size increases with model width for all five models, but MS-AgentNet maintains the lowest value at all four tested widths. At a dimension of 128, its storage size is 714.37 KB, 32.2\% lower than that of Transformer, the closest model, at the same dimension. Overall, MS-AgentNet achieves a good balance between SOH estimation accuracy and computational and storage overhead, showing its potential for lightweight applications in resource-constrained BMS.
```

## chapter05.tex

### 源文件块 1

中文原文：

```latex
本文提出了一种面向资源受限电池管理系统的轻量化锂离子电池SOH估计框架，以缓解健康指标跨电池稳定性不足以及预测精度与计算效率难以兼顾的问题。研究从系统性健康指标构建和轻量化网络设计两个方面展开。所提出的多源健康指标提取与优化算法首先从充放电数据及其衍生曲线中构建多类候选健康指标，再基于特征开发电池集合的相关性结果，利用 MS-CCCT 对恒流充电电压窗口进行多尺度自适应标定，并通过 PCC/SCC 双阈值准入与冗余剔除确定模型输入。在保持特征定义与参数不变的条件下，最终入选指标在同一数据集的其他电池上仍与SOH保持较强的线性和单调关联。在序列建模方面，MS-AgentNet将ReLU²智能体注意力与小核和大核深度可分离卷积相结合，以协同表征局部退化变化、跨位置全局信息和长尺度退化趋势。在智能体数量固定时，RAA利用少量可学习静态智能体完成信息聚合与广播，将注意力相关性交互的理论复杂度由$O(N^2d)$降低至$O(Nn_a d)$。
```

英文译文：

```latex
This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-constrained battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset. For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales. With a fixed number of agents, RAA uses a small number of static learnable agents for information aggregation and broadcasting, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.
```

### 源文件块 2

中文原文：

```latex
在Oxford、CALCE CS2、CALCE CX2和MIT/Severson四个公开电池数据集上的实验结果表明，与CNN-Transformer、CNN-LSTM、Transformer和LSTM四种基线模型相比，MS-AgentNet总体上取得了更优的综合表现。具体而言，在CALCE CX2数据集的两节电池平均结果中，MS-AgentNet的MAPE相比CNN-Transformer降低了52.69\%。此外，MS-AgentNet具有较低的参数量和存储开销，体现了其轻量化优势。消融实验与卷积尺度补充实验显示，多尺度深度可分离卷积与RAA的互补融合能够提升模型在不同退化场景下的综合表现。总体来看，所提框架在SOH估计精度与资源开销之间取得了良好平衡；模型在同一数据集的其他电池上仍保持了较好的估计性能，体现出一定的域内跨电池泛化能力，并具备应用于资源受限电池管理系统的潜力。
```

英文译文：

```latex
Experiments on four public battery datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, show that MS-AgentNet achieves better overall performance than the four baseline models, CNN-Transformer, CNN-LSTM, Transformer, and LSTM. Specifically, the average MAPE of MS-AgentNet over the two cells in the CALCE CX2 dataset is 52.69\% lower than that of CNN-Transformer. It also has a low parameter count and storage overhead, showing its lightweight advantages. Ablation studies and additional convolutional-scale experiments show that the complementary fusion of multi-scale depthwise separable convolutions and RAA improves overall performance under different degradation scenarios. Overall, the proposed framework achieves a good balance between SOH estimation accuracy and resource consumption. It maintains good estimation performance on the test cells in the corresponding datasets, showing a degree of in-domain cross-cell generalization and potential for application in resource-constrained battery management systems.
```

### 源文件块 3

中文原文：

```latex
尽管取得了上述结果，所提框架仍依赖可辨识的充放电数据片段，且其跨数据集适应能力会受到数据域差异、源域选择和目标域数据量的影响。未来将重点研究面向不完整充电和动态运行片段的健康指标构建方法及轻量化域适应策略，并在更多电池体系、实际车辆运行数据和嵌入式硬件平台上开展验证，以进一步提升该框架的工程适用性与部署可靠性。
```

英文译文：

```latex
Despite these results, the framework still relies on identifiable charging and discharging data segments, and its cross-dataset adaptation performance is affected by domain differences, source-domain selection, and the amount of target-domain data. Future work will focus on HI construction for incomplete charging and dynamic operating segments, together with lightweight domain adaptation strategies. Further validation will cover more battery chemistries, real-vehicle operating data, and embedded hardware platforms to improve the framework's practical applicability and deployment reliability.
```
