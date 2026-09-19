# 引言、卷积与注意力补充修改落实记录

2026-09-17。作者要求落实此前停留在建议中的修改。共9项文本替换，涉及8个正文段落（chapter01第42行；chapter03第9、68、108、139、174、275、384行）。

已落实引言桥接、架构Step1、两处逐点卷积用词、RAA应用说明、融合收束、局部分支精简、DSConv-L残差说明精简及local sequential patterns对齐。最后两项作用于同一DSConv-L段落。原有八处成果保留，其中局部分支与DSConv-L采用此次精简版。

公式块、行内数学、引用和交叉引用核验不变；source-zh哈希不变。未补回撤回的引言文献段，未修改实验设置或结果。

## 1. A — chapters/chapter01.tex

改前：

```tex
To address these challenges, this paper proposes a lithium-ion battery SOH estimation framework built around MS-AgentNet. The framework addresses health indicator construction and lightweight model design: group-level calibration and selection improve the cross-cell stability of model inputs, while local variations and long-term trends are extracted with low computational overhead. The main contributions are as follows.
```

改后：

```tex
To address these challenges, this paper proposes a lithium-ion battery SOH estimation framework built around MS-AgentNet. The framework addresses health indicator construction and lightweight model design: group-level calibration and selection improve the cross-cell stability of model inputs, while local feature extraction is combined with agent attention to represent local variations and long-term degradation trends with low computational overhead. The main contributions are as follows.
```

## 2. B — chapters/chapter03.tex

改前：

```tex
\textbf{Step 1: Local-global feature fusion.} The input $\mathbf X_l$ is processed by LGFA, which uses DSConv-S to extract local features and ReLU$^2$ Agent Attention (RAA) to establish global information interactions across positions:
```

改后：

```tex
\textbf{Step 1: Local-global feature fusion.} The input $\mathbf X_l$ is processed by LGFA, which combines DSConv-S for local degradation feature extraction with ReLU$^2$ Agent Attention (RAA) for global context modeling within the input window:
```

## 3. D — chapters/chapter03.tex

改前：

```tex
Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into two stages: context aggregation and information broadcasting\cite{ref46}. The agents first aggregate sequence context from the keys and values, and each query position then reads information from the agent context.
```

改后：

```tex
Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into two stages: context aggregation and information broadcasting\cite{ref46}. For the health indicator sequences considered here, agents aggregate context from the keys and values across cycles within the input window, and each cycle position uses its query to read information from the agent context.
```

## 4. E — chapters/chapter03.tex

改前：

```tex
This additive fusion preserves the local degradation features extracted by DSConv-S and combines them with the cross-position context established by RAA, forming a joint local-global representation while maintaining linear computational complexity with respect to the sequence length $N$.
```

改后：

```tex
This additive fusion combines the local degradation features extracted by DSConv-S with the global context established by RAA, providing a joint local-global representation for SOH estimation while maintaining linear computational complexity with respect to the sequence length $N$.
```

## 5. C — chapters/chapter03.tex

改前：

```tex
A $1\times1$ pointwise convolution then fuses features across channels
```

改后：

```tex
A $1\times1$ pointwise convolution then integrates features across channels
```

## 6. C — chapters/chapter03.tex

改前：

```tex
Next, the second $1\times1$ pointwise convolution fuses features across channels
```

改后：

```tex
Next, the second $1\times1$ pointwise convolution integrates features across channels
```

## 7. 局部分支精简 — chapters/chapter03.tex

改前：

```tex
2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is carried by the local branch to the fusion stage, where it is added to the RAA branch output. This path passes the locally enhanced health indicator representation directly to the fusion stage, combining it with the global context established by RAA to form a joint local-global representation for SOH estimation.
```

改后：

```tex
2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is sent directly through the local branch to the fusion stage, where it is added to the RAA branch output. This path combines the locally enhanced health indicator representation with the global context established by RAA within the input window to form a joint local-global representation for SOH estimation.
```

## 8. 残差说明精简 — chapters/chapter03.tex

改前：

```tex
The transformation order is the same as in DSConv-S, and the residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}. The convolution output is scaled by a learnable factor and added to the original LGFA output, incorporating the further extracted sequence features into the existing representation.
```

改后：

```tex
The transformation order is the same as in DSConv-S. At the MS-AgentNet Block level, the convolution output is scaled by a learnable factor and added to the original LGFA output through a residual connection, incorporating the further extracted sequence features into the existing representation, as shown in Eq.~\eqref{eq:block_dsconv_l}.
```

## 9. JE搭配对齐 — chapters/chapter03.tex

改前：

```tex
local sequence patterns over longer time scales
```

改后：

```tex
local sequential patterns over longer time scales
```
