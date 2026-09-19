# §3.3导语与RAA首段：最终确认落实

2026-09-17。两处英文按作者最终版本原样落实，仅将显示文献编号映射为现稿Agent Attention对应的ref46。公式及复杂度推导不变。中文agent今后统一译为代理；英文名称不变，历史记录和冻结中文不批量重写。

## chapter03.tex:191

中文对应：

本节介绍多头自注意力的一般形式，简要比较Softmax注意力与线性注意力，并介绍LGFA，该模块将局部特征提取与计算复杂度随序列长度线性增长的全局交互相结合。

改前英文：

```tex
This section presents the general form of multi-head self-attention, briefly compares Softmax attention and linear attention, and then introduces the proposed LGFA module, which combines local-global feature modeling with computational efficiency.
```

落实英文：

```tex
This section presents the general form of multi-head self-attention, briefly compares Softmax attention and linear attention, and introduces LGFA, which combines local feature extraction with global interactions that scale linearly with sequence length.
```

## chapter03.tex:275

中文对应：

RAA通过少量代理介导全局交互，无需直接计算所有序列位置之间的两两注意力。在上下文聚合阶段，代理从键和值中汇聚信息；在信息广播阶段，各查询从代理上下文中读取信息。这两个阶段使退化相关信息能够在输入窗口内的健康指标表示之间共享，从而建立跨循环上下文联系。

改前英文：

```tex
Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into context aggregation and information broadcasting\cite{ref46}: the agents first aggregate sequence context from the keys and values, and each query position then reads information from the agent context. This process establishes relationships across cycles by sharing degradation-related information among health indicator representations within the input window.
```

落实英文：

```tex
RAA uses a small number of agents to mediate global interactions, avoiding direct pairwise attention between all sequence positions\cite{ref46}. During context aggregation, the agents gather information from the keys and values; during information broadcasting, each query retrieves information from the agent context. Together, these two stages enable degradation-related information to be shared among health indicator representations within the input window, thereby establishing cross-cycle context.
```
