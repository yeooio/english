# 实验前模型论述：四处承接调整落实

2026-09-17。作者授权修改文字并明确图不需要改动。仅落实贡献（2）、第3节总导语、LGFA引入、DSConv-L引入。图及图注全部保持不变；不新增RAA/ReLU²收束，不更换时间尺度术语，不修改实验。

## chapters/chapter01.tex:46

中文对应：

构建轻量级局部—全局网络MS-AgentNet。为兼顾电池长期退化趋势与短期容量波动的表征，将小核深度可分离卷积与ReLU²智能体注意力相结合，构建LGFA模块，以较低参数开销整合局部特征提取与全局上下文建模。进一步引入大核深度可分离卷积，与小核卷积共同提取不同时间尺度的退化特征。在智能体数量与特征维度固定时，相较于标准自注意力，其注意力计算关于序列长度的复杂度由O(N²)降至O(N)。这些设计旨在兼顾SOH估计精度与计算、存储开销。

改前英文：

```tex
(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} A Local-Global Fusion Attention (LGFA) module combines small-kernel depthwise separable convolutions with ReLU$^2$ agent attention to integrate local feature extraction and global context modeling with low parameter overhead. Compared with standard self-attention, its attention computation reduces the complexity with respect to sequence length from $O(N^2)$ to $O(N)$. The model further introduces large-kernel depthwise separable convolutions, which, together with small-kernel convolutions, extract degradation features at different time scales. These designs aim to enhance the model's representation of long-term degradation trends and short-term capacity fluctuations and improve SOH estimation accuracy while limiting computational and storage overhead.
```

落实英文：

```tex
(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} To represent both long-term battery degradation trends and short-term capacity fluctuations, small-kernel depthwise separable convolutions are combined with ReLU$^2$ agent attention to form a Local-Global Fusion Attention (LGFA) module, integrating local feature extraction and global context modeling with low parameter overhead. The model further introduces large-kernel depthwise separable convolutions, which work with the small-kernel convolutions to extract degradation features at different time scales. With a fixed number of agents and feature dimension, its attention computation reduces the complexity with respect to sequence length from $O(N^2)$ for standard self-attention to $O(N)$. These designs aim to balance SOH estimation accuracy with computational and storage overhead.
```

## chapters/chapter03.tex:1

中文对应：

为兼顾电池退化过程中局部变化与长期趋势的表征，并降低序列建模的计算开销，提出轻量级多尺度智能体网络MS-AgentNet。其中，MS表示由小核DSConv-S和大核DSConv-L构成的多尺度卷积设计，用于在较低参数开销下提取不同尺度的退化特征。LGFA结合局部卷积增强与高效注意力，建立局部退化信息与循环间上下文之间的联系。下文介绍总体架构与工作流程、多尺度深度可分离卷积模块及LGFA模块。

改前英文：

```tex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Local-Global Fusion Attention (LGFA) module.
```

落实英文：

```tex
A lightweight Multi-Scale Agent Network (MS-AgentNet) is proposed to represent both local variations and long-term trends in battery degradation while reducing the computational overhead of sequence modeling. The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which extracts degradation features at different scales with low parameter overhead. Local-Global Fusion Attention (LGFA) combines local convolutional enhancement with efficient attention to connect local degradation information with context across cycles. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the LGFA module.
```

## chapters/chapter03.tex:271

中文对应：

针对上述需求，将小核深度可分离卷积DSConv-S与ReLU²智能体注意力RAA相结合，构建LGFA模块，其结构如图所示。DSConv-S首先对健康指标序列进行局部增强，所得表示分别进入局部分支和RAA分支。局部分支保留局部退化信息，RAA分支通过智能体聚合与广播建立输入窗口内的循环间联系。两个分支的输出经加法融合。

改前英文：

```tex
To capture both local degradation features and dependencies across cycles, small-kernel depthwise separable convolution (DSConv-S) is combined with ReLU² Agent Attention (RAA) to form the Local-Global Fusion Attention (LGFA) module, as shown in \cref{fig:3-3}(d). The module combines a local branch with an RAA branch: DSConv-S first extracts a locally enhanced representation, which is passed through the local branch to retain local information and fed into the RAA branch for global context modeling; the outputs of the two branches are then fused by addition. This design combines local feature extraction with global context modeling to provide SOH estimation with a feature representation that incorporates both degradation details and relationships across cycles.
```

落实英文：

```tex
To address these requirements, small-kernel depthwise separable convolution (DSConv-S) is combined with ReLU² Agent Attention (RAA) to form the Local-Global Fusion Attention (LGFA) module, as shown in \cref{fig:3-3}(d). DSConv-S first enhances local information in the health indicator sequences, and the resulting representation is fed into the local and RAA branches. The local branch preserves local degradation information, while the RAA branch establishes relationships across cycles within the input window through agent aggregation and broadcasting. The outputs of the two branches are fused by addition.
```

## chapters/chapter03.tex:174

中文对应：

DSConv-S在注意力交互前增强局部信息，DSConv-L则位于LGFA之后，进一步细化已融合局部信息与全局上下文的特征表示。首先，1×1逐点卷积将通道维度扩展至三倍，以提取丰富的表征；随后，1×31深度卷积在各通道内捕获较长时间尺度的局部序列模式。第二个1×1逐点卷积跨通道整合特征，并恢复原始通道维度。整体变换顺序与DSConv-S一致。在Block层，卷积输出经可学习系数缩放后，通过残差连接与原有LGFA输出相加，将进一步提取的序列特征融入已有表示，如相应公式所示。大小核卷积由此共同丰富用于SOH估计的多尺度退化表征。

改前英文：

```tex
DSConv-L follows LGFA to further refine the feature representation that combines local information and global context. A $1\times1$ pointwise convolution first expands the channel dimension by a factor of three to extract rich representations, followed by a $1\times31$ depthwise convolution that captures local sequential patterns over longer time scales within each channel. A second $1\times1$ pointwise convolution integrates these features across channels and restores the original channel dimension. The transformation order is the same as in DSConv-S. At the MS-AgentNet Block level, the convolution output is scaled by a learnable factor and added to the original LGFA output through a residual connection, incorporating the further extracted sequence features into the existing representation, as shown in Eq.~\eqref{eq:block_dsconv_l}. Through local enhancement before attention and feature refinement after fusion, the small- and large-kernel convolutions jointly enrich multi-scale degradation representations for SOH estimation.
```

落实英文：

```tex
DSConv-S enhances local information before attention, while DSConv-L follows LGFA to further refine the feature representation that combines local information and global context. A $1\times1$ pointwise convolution first expands the channel dimension by a factor of three to extract rich representations, followed by a $1\times31$ depthwise convolution that captures local sequential patterns over longer time scales within each channel. A second $1\times1$ pointwise convolution integrates these features across channels and restores the original channel dimension. The transformation order is the same as in DSConv-S. At the MS-AgentNet Block level, the convolution output is scaled by a learnable factor and added to the original LGFA output through a residual connection, incorporating the further extracted sequence features into the existing representation, as shown in Eq.~\eqref{eq:block_dsconv_l}. The small- and large-kernel convolutions thus jointly enrich multi-scale degradation representations for SOH estimation.
```
