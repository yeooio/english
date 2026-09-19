# 注意力引入：多源数据与退化表征修订

2026-09-17。作者确认三段修订，并要求尽可能避免“在本文中”等草稿式自指引导语。当前英文第267、271、275行已原位替换；其他正文不变。

## chapter03.tex:267

确认中文：

上述线性注意力通过重组计算顺序降低了全局信息交互的开销，但其计算过程未显式引入局部邻域特征。健康指标由电池长期循环过程中采集的多源信号及其衍生曲线构建并筛选得到，用于表征电池退化过程。对这些健康指标序列进行建模时，除建立循环间依赖关系外，还需要提取相邻循环局部变化中包含的细粒度退化信息。因此，有必要将局部特征提取与高效注意力机制相结合，在控制计算开销的同时增强对电池退化过程的表征。

改前英文：

```tex
The linear attention described above reduces the cost of global information interactions by rearranging the computation order, but it does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref64}. In battery SOH estimation, health indicator sequences contain both degradation trends and local variations between neighboring cycles. When modeling dependencies across cycles, the model still needs to make full use of the fine-grained degradation information in these sequences. Local feature extraction therefore needs to be combined with an efficient attention mechanism to enhance the representation of battery degradation while limiting computational overhead.
```

落实英文：

```tex
The linear attention described above reduces the cost of global information interactions by rearranging the computation order, but it does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref64}. Health indicators are constructed and selected from multi-source signals collected during long-term battery cycling and their derived curves to characterize battery degradation. Modeling these health indicator sequences requires both establishing dependencies across cycles and extracting fine-grained degradation information from local variations between neighboring cycles. Local feature extraction therefore needs to be combined with an efficient attention mechanism to enhance the representation of battery degradation while limiting computational overhead.
```

## chapter03.tex:271

确认中文：

为满足上述建模需求，将小核深度可分离卷积（DSConv-S）与ReLU²智能体注意力（RAA）相结合，构建局部—全局融合注意力（LGFA）模块，其结构如图所示。DSConv-S提取健康指标序列中的局部退化特征，在保留序列结构的同时丰富局部信息。所得表示分别进入局部分支与RAA分支，用于局部特征保留和全局上下文建模。两个分支的输出通过加法融合，为SOH估计提供兼顾局部退化细节与循环间依赖关系的特征表示。

改前英文：

```tex
To balance degradation feature extraction and computational efficiency, this study combines small-kernel depthwise separable convolution (DSConv-S) with ReLU² Agent Attention (RAA) to form the Local-Global Fusion Attention (LGFA) module, as shown in \cref{fig:3-3}(d). DSConv-S enhances the input representation of health indicator sequences by enriching local information while preserving the sequence structure. The resulting representation is fed into both the local and RAA branches. The local branch passes the locally enhanced representation directly to the fusion stage, while the RAA branch uses it to model global context. The outputs of the two branches are fused by addition to provide SOH estimation with a feature representation that incorporates both local degradation details and global context.
```

落实英文：

```tex
To meet these modeling requirements, small-kernel depthwise separable convolution (DSConv-S) is combined with ReLU² Agent Attention (RAA) to form the Local-Global Fusion Attention (LGFA) module, as shown in \cref{fig:3-3}(d). DSConv-S extracts local degradation features from health indicator sequences, enriching local information while preserving the sequence structure. The resulting representation is fed into the local and RAA branches for local feature preservation and global context modeling, respectively. The outputs of the two branches are fused by addition to provide SOH estimation with a feature representation that incorporates both local degradation details and dependencies across cycles.
```

## chapter03.tex:275

确认中文：

Agent Attention以少量智能体作为信息中介，将序列位置之间的全局交互分解为上下文聚合与信息广播两个阶段。智能体汇集输入窗口内健康指标表示中的退化相关信息，并将所得上下文传递至各循环的特征表示，从而建立循环间联系。

改前英文：

```tex
Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into two stages: context aggregation and information broadcasting\cite{ref46}. For the health indicator sequences considered here, agents aggregate context from the keys and values across cycles within the input window, and each cycle position uses its query to read information from the agent context.
```

落实英文：

```tex
Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into two stages: context aggregation and information broadcasting\cite{ref46}. The agents aggregate degradation-related information from health indicator representations within the input window and distribute the resulting context to the feature representation of each cycle, establishing connections across cycles.
```
