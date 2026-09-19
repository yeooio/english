# 三篇范文逐句学习与本稿复核（2026-09-14）

状态：审校依据与建议，未修改论文。此记录新读原文并按PDF核对连续段落，不以旧词表代替本次比对。范围是三篇论文各一个完整功能段落，共10句，不是三篇全文的计量研究，也不代表完成了全文新一轮审校。

## 计数与核验口径

已查看三张完整PDF页面：BMSFormer第6页、Engineering-AI第7页、JESSOHRUL第11页，核对栏位、段落起止、Fig.缩写和跨行连字符。逐句转录仅用于学习，不复制进论文。保留原文framwork拼写；PDF换行断词合并，数学核尺度规范为空格分隔的k = 5, k = 31。

句号按语义人工分句；Fig.不另断句，冒号不另计句。词数按空白分词，只计含英文字母或数字的项：连字符词算1项，缩写和数字计入，单独等号不计。这是本记录的可复算口径，不是语言学唯一标准。统计分母均为各自选段；混合功能句单列，不将其同时计入两个互斥比例。“输出result”及设计目的不计作实验结果。

## BMSFormer

来源：[PDF，第6页](D:/MS-AgentNet-English/style-references/BMSFormer/source.pdf)，§3.1 Architecture overview，左栏第二段（The entire framwork…至…optimization.）。核验图：[页面](D:/MS-AgentNet-English/build/reference-learning/BMSFormer-p6.png)。

**B1（43词）**

> The entire framwork is illustrated in Fig. 4 and described as follows: HIs are taken as input, segmented into fragments via window splitting, embedded in a high-dimensional space, and then fed into a BMSFormer block, which includes the LGFA module and DSConv-L module.

**B2（15词）**

> The output from LGFA module is transposed, passed through a DSConv-L module, and transposed back.

**B3（19词）**

> Finally, the output from all BMSFormer blocks is fed into a Multilayer Perceptron (MLP) layer before outputting the result.

**B4（28词）**

> During the training process, the true SOH value right following each window segment is utilized as a label, which guides the model to adjust the gradient descent optimization.

| 句号 | 功能 | 主语 | 时态／语态 | 与前句的连接及信息增量 |
| --- | --- | --- | --- | --- |
| B1 | 混合：过渡＋方法 | The entire framwork；冒号后 HIs | 一般现在时、被动；which includes 为主动 | 先以图定位，再以 HIs 串联输入处理；then 表示实际操作顺序 |
| B2 | 方法 | The output from LGFA module | 一般现在时、被动 | 承接上一句模块名，以明确输出为下一步操作对象 |
| B3 | 方法 | the output from all BMSFormer blocks | 一般现在时、被动 | Finally 结束前向数据流；result 是预测输出，不是实验结果陈述 |
| B4 | 方法 | the true SOH value；从句 which 指 label | 一般现在时、主句被动、从句主动 | 时间状语切换到训练阶段；窗口对应关系承接输入分段 |

长度：43、15、19、28词；共4句、105词；均值26.3词；范围15—43词。

功能覆盖：纯方法3/4句（75.0%）、62/105词（59.0%）；过渡＋方法混合1/4句（25.0%）、43/105词（41.0%）；实验结果0/4句、0/105词。B4中的标签作用属于训练机制说明。推进为“输入流程→模块输出处理→预测出口→训练标签”。值得学习的是明确说明每次处理的对象，不能由此要求本文复制其43词长句或其所有被动语态。framwork是拼写问题；before outputting the result、adjust the gradient descent optimization也不作为优选搭配照搬。

## Engineering-AI

来源：[PDF，第7页](D:/MS-AgentNet-English/style-references/Engineering-AI/source.pdf)，§4.2 Multi-scale depthwise separable convolutions，右栏标题下完整首段。核验图：[页面](D:/MS-AgentNet-English/build/reference-learning/Engineering-AI-p7.png)。

**E1（17词）**

> Standard convolutions often suffer from parameter redundancy and may be prone to overfitting on small-sample battery datasets.

**E2（12词）**

> To mitigate this, two specialized Depthwise Separable Convolution (DSConv) modules are designed.

**E3（20词）**

> The kernel scales (k = 5, k = 31) were determined empirically to capture multi-scale degradation features, as visualized in Fig. 5.

| 句号 | 功能 | 主语 | 时态／语态 | 与前句的连接及信息增量 |
| --- | --- | --- | --- | --- |
| E1 | 局限 | Standard convolutions | 一般现在时、主动；may 表示可能 | 提出参数冗余及小样本过拟合风险；未声称必然过拟合 |
| E2 | 混合：目的＋方法 | two specialized Depthwise Separable Convolution (DSConv) modules | 一般现在时、被动 | this 回指上一句局限；目的置于句首，接着直接说明设计对象 |
| E3 | 混合：方法＋目的 | The kernel scales | 一般过去时、被动 | 由模块设计推进至具体核尺度及选择方式；to capture 是设计目的，不能当成已验证结果 |

长度：17、12、20词；共3句、49词；均值16.3词；范围12—20词。

功能覆盖：纯方法0/3句、0/49词；方法＋目的混合2/3句（66.7%）、32/49词（65.3%）；局限1/3句（33.3%）、17/49词（34.7%）；实验结果0/3句、0/49词。推进为“具体局限→应对设计→配置和选取目的”。不能把to capture读成结果证明，也不能把范文may be prone改成本文必然过拟合的依据。它没有在这段提供训练时间测量，因此不支持本文训练时长的程度判断。

## JESSOHRUL

来源：[PDF，第11页](D:/MS-AgentNet-English/style-references/JESSOHRUL/source.pdf)，§3.5.1 Health indicators extraction，右栏标题下完整首段。核验图：[页面](D:/MS-AgentNet-English/build/reference-learning/JESSOHRUL-p11.png)。

**J1（44词）**

> In this section, voltage, temperature, time, and capacity data from the battery charging process are analyzed and processed to derive four characteristic curves: Incremental Capacity (IC), Charge Voltage Time (CVT), Differential Temperature Voltage (DTV), and Differential Temperature Capacity (DTC), as shown in Fig. 5(a)-(d).

**J2（15词）**

> From these curves, ten representative HIs are extracted, capturing key features related to battery degradation.

**J3（12词）**

> The ten HIs and their corresponding descriptions are summarized in Table 4.

| 句号 | 功能 | 主语 | 时态／语态 | 与前句的连接及信息增量 |
| --- | --- | --- | --- | --- |
| J1 | 方法 | voltage, temperature, time, and capacity data | 一般现在时、被动 | 先交代数据来源及处理输出；冒号后列的是四类曲线 |
| J2 | 混合：方法＋作用说明 | ten representative HIs | 一般现在时、被动；capturing 为分词补充 | From these curves 明确承接上一句输出，再交代指标数量与作用 |
| J3 | 过渡 | The ten HIs and their corresponding descriptions | 一般现在时、被动 | 以相同指标集合接入定义表；不重复提取过程 |

长度：44、15、12词；共3句、71词；均值23.7词；范围12—44词。

功能覆盖：纯方法1/3句（33.3%）、44/71词（62.0%）；方法＋作用说明混合1/3句（33.3%）、15/71词（21.1%）；表格过渡1/3句（33.3%）、12/71词（16.9%）；实验结果0/3句、0/71词。推进为“数据→四类曲线→十项指标→定义表”。第一句虽长，但列举承担具体信息，没有仅凭长度判错的理由。本文有额外的容量、效率指标，应保留相应来源，不能套成只有曲线这一条提取路径；十项数量及Charge Voltage Time命名也不替换本文已确认术语。

## 对本稿的实际影响

1. 第2章44行：中文“围绕……展开”可直接落到“提出什么、用于什么”。JESSOHRUL首句也有In this section，但紧接着就说数据如何处理，不再叠加一层“本节围绕某主题展开”。这是可选的直接性改善，英文现稿已做到，保留。
2. 第3章57行：“计算开销迅速累积→显著推高计算负载”没有说明两个不同对象，形成同义重复；英文也有相同问题。同时，英文substantially明确覆盖training time，中文“显著推高计算负载并延长训练时间”的范围存在歧义。这是需要作者确定力度范围的审校项，范文不能替作者决定。
3. 第2章48行：本稿已经区分数据、曲线、提取特征及另行计算的容量/效率指标，保留；不可为了与JESSOHRUL一致而删除本文额外信息。
4. 第3章局部分支：BMSFormer明确写the output from…，支持此前C2所建议的把“归一化后的表示”写成传递对象；这是对已有建议的证据加固，不计为新问题。

详见[中文语法与范文对照审查C7—C8](D:/MS-AgentNet-English/translation-guides/chinese-grammar-reference-review-2026-09-14.md)。以上仅借鉴表达结构；中文是否合语法仍需根据中文自身的搭配和上下文判断，不能用英文范文直接证明中文错误。

