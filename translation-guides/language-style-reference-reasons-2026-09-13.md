# 11项英文建议：对应范文依据与适用边界

本文件按作者“需要的是范文的原因”单独新建。只审查前述11项理由，不修改论文，不声称又完成一次全文审校。重新读取三篇相应TXT语境；以下短引均来自可确认的连续文字，仅合并换行。未据双栏错序推导段落顺序，也未声称本轮回看PDF或完成新一轮句数统计。中文释义为助手翻译。

## 先纠正结论

此前“11项都可推荐”的表述混合了范文依据和本文一般清晰度判断。它们不是同一件事。C04-L041的范文本身使用 effectiveness；C04-L073原引证并不对应两块电池用途。按本次以对应范文说明理由的标准，这两项降为可选，默认保留原句；其余项证据强弱如下，不能一律称为范文直接支持。与前两份对照/复核报告有冲突时，以本说明的证据边界为准。

范文不构成对本文原句的禁用规则。只有对象、任务和信息范围相符时，才能借用对应搭配或结构。

## 1. LS-I01｜退化信息提取

依据性质：间接风格参照，不足以证明原句必须改。

改前：

However, complex operating conditions make the stable extraction of degradation information more difficult, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity.

原建议（第7、8项本轮降为可选）：

However, complex operating conditions make it harder to extract degradation information consistently, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity.

范文短引：

> infer SOH from indirect sensor data

中文释义：从间接传感数据推断 SOH。

来源：[Engineering-AI/full.txt:68](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:68)。

范文对应原因及边界：范文在同类引言背景中以 infer + 对象 + 数据来源直接写估计动作。本文 extract degradation information consistently 同样将动作与对象放在主干里。但 infer SOH 不等于 extract degradation information；这段没有给出 stable extraction 与 extract ... consistently 的对应对照。因此，这是可解释的本文语言调整，不能包装成范文直接要求。

## 2. LS-I04｜相关性评价

依据性质：评价动作和依据有对应；移位是本文适配。

改前：

It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators using correlations on the feature-development cells.

原建议（第7、8项本轮降为可选）：

It then uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators.

范文短引：

> to jointly evaluate their linear and monotonic nonlinear relationships with battery degradation

中文释义：共同评价它们与电池退化之间的线性及单调非线性关系。

来源：[JESSOHRUL/full.txt:1822](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1822)。

范文对应原因及边界：1822–1834 行的筛选内容明确涉及相关系数、关系评价、保留及去冗余；引用只取连续文本片段，不拼接 TXT 中被别栏打断的句首。本文 uses correlations ... to jointly evaluate 借鉴相关性作为评价依据的表达，使两个评价对象共用这一依据。范文并没有本文完全相同的 using 后置句；不借入其全电池范围或阈值。

## 3. LS-M02｜HI13、HI14 命名

依据性质：编号与对象对应有依据；拆句并非范文规定。

改前：

Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.

原建议（第7、8项本轮降为可选）：

Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V. These indicators are denoted as HI13 and HI14, respectively\cite{ref31,ref52}.

范文短引：

> the peak of the DTV curve (HI5)

中文释义：DTV 曲线的峰值（HI5）。

来源：[JESSOHRUL/full.txt:1805](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1805)。

范文对应原因及边界：1803–1811 行连续特征提取段逐项将峰、峰位、谷、谷位与 HI5–HI8 就近对应。本文在两个电压区间之后另用 These indicators 点名两个指标，目的也是让编号所属对象清楚。范文实际上采用括号编号，没有使用本文建议的独立命名句，故只能支持对应关系清晰，不能证明必须拆句。

## 4. LS-M06｜标准卷积计算成本

依据性质：同功能、同对象，直接结构依据。

改前：

Its computational cost can be expressed as:

原建议（第7、8项本轮降为可选）：

The computational cost of standard convolution can be expressed as:

范文短引：

> The standard convolutions have the computational cost of:

中文释义：标准卷积的计算成本为：

来源：[BMSFormer/full.txt:772](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:772)。

范文对应原因及边界：在介绍标准卷积并引出成本公式的位置，范文明示 standard convolutions，而非跨句使用 Its。本文将 Its computational cost 改为 The computational cost of standard convolution，借鉴的是公式引导句明确计算对象这一结构。不是机械复制范文的复数形式或其他不自然搭配。

## 5. LS-M07｜归一化后的表示

依据性质：同类数据流中的对象命名有直接依据；具体对象来自本文。

改前：

The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

原建议（第7、8项本轮降为可选）：

The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

范文短引：

> The output from LGFA module is transposed

中文释义：LGFA 模块的输出被转置。

来源：[BMSFormer/full.txt:739](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:739)。

范文对应原因及边界：731–744 行模型总览中的数据流句明确称 output from LGFA module，再陈述后续操作。本文用 the normalized representation 取代 passes it 中的 it，同样明确被传递的中间量。范文支持输出对象应可追踪，不支持本文具体归一化位置；该位置仍以本文公式和中文源稿为准。

## 6. LS-M08｜输入定义与转置

依据性质：先定义对象再引出操作的局部结构参照。

改前：

Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension.

原建议（第7、8项本轮降为可选）：

The input features are $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively. The input is first transposed so that the embedding dimension becomes the convolutional channel dimension.

范文短引：

> let the input tensor be denoted by

中文释义：将输入张量记为……

来源：[Engineering-AI/full.txt:818](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:818)。

范文对应原因及边界：818–820 行连续文字先给输入张量及维度符号，再引出顺序运算。本文将 Given ... where ... the input is first transposed 改成定义句加操作句，是借鉴这种先完成输入定义、再进入操作的局部结构。这里只使用连续句，不将 822–853 行错序的 Step 1/2/3 当作范文真实段落顺序，也不据此断言范文要求固定句数。

## 7. C04-L041｜HI 筛选效果评价

依据性质：原句已有对应依据；撤销范文支持该替换的说法。

改前：

To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset.

原建议（第7、8项本轮降为可选）：

To evaluate how effectively group-level HI selection identifies inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset.

范文短引：

> To validate the effectiveness of the proposed method

中文释义：为验证所提方法的有效性。

来源：[JESSOHRUL/full.txt:1947](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1947)。

范文对应原因及边界：1946–1959 行正是不同 HI 输入的验证实验，范文用的恰好是 the effectiveness of ...，与本文原句 To evaluate the effectiveness of ... 同类。该处可以支持本文原有目的表达，不能证明改成 how effectively 更符合范文。按本次范文依据标准，这一替换应降为可选，默认保留原句。

## 8. C04-L073｜两块电池与超参数范围

依据性质：原引证没有直接支持该改写。

改前：

Within these ranges, two cells in the feature-development set of each dataset are used for model training and configuration: one for learning model parameters and the other for hyperparameter selection.

原建议（第7、8项本轮降为可选）：

For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges.

范文短引：

> the same training and model hyperparameters are set

中文释义：设置相同的训练及模型超参数。

来源：[BMSFormer/full.txt:1348](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:1348)。

范文对应原因及边界：1344–1351 行说的是模型间效率比较的统一设置，没有本文一块电池学习参数、另一块电池选择配置的分工，也没有把 within these ranges 移到句末的范例。因此不能据此说本文建议更符合范文。范围就近和分工直述可作为独立清晰度理由，但不是已核实的对应范文证据；按本次标准降为可选。

## 9. C04-L149｜模块与功能配对

依据性质：模块—动作搭配有直接依据；本文并列结构为适配。

改前：

To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively.

原建议（第7、8项本轮降为可选）：

To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions.

范文短引：

> DSConv separates the spatial and channel-wise operations

中文释义：DSConv 将空间操作与通道操作分开。

来源：[BMSFormer/full.txt:814](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:814)。

范文对应原因及边界：814–817 行以 DSConv 为主语，紧接动作 separates 和操作对象；Engineering-AI 2080–2090 行的消融说明也将两个卷积模块与各自位置及作用就近配对。本文 integrates multi-scale DSConv to extract ... and RAA to enable ... 借鉴模块紧接其功能的表达方式，减少 respectively 回配。范文不说明本文 RAA 的具体机制，亦不能证明 respectively 本身不好。

## 10. C04-L166｜FLOPs 计量

依据性质：计量术语和单次前向定义有依据；补计流程不是范文依据。

改前：

FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass.

原建议（第7、8项本轮降为可选）：

An initial operation count is obtained using the \texttt{profile} function in the THOP library. After the count for attention operations is added, the total is converted to the number of floating-point operations required for a single forward pass.

范文短引：

> floating-point operations required for a single forward pass

中文释义：单次前向传播所需的浮点运算。

来源：[JESSOHRUL/full.txt:3801](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:3801)。

范文对应原因及边界：3793–3808 行区分 FLOPs、训练时间、参数量及存储量，并对应计量工具；BMSFormer 1360–1368 行也有相同计量语境。本文保留 single forward pass 和工具定义有直接依据。但这些段落没有补加注意力计数后换算的流程；initial operation count → attention count → total 的展开来自本文所述流程的澄清，不是模仿范文，且实际代码未验证。

## 11. C04-L170｜参数与存储结果

依据性质：同类资源结果的搭配及数值就近关系有直接依据。

改前：

In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models.

原建议（第7、8项本轮降为可选）：

In contrast, MS-AgentNet requires 0.045760 M FLOPs, has a parameter count of 4,643, and uses 27.44 KB to store its weights; all three values are the lowest among the five models.

范文短引：

> a parameter count of only 6114 and a storage footprint of 40.92 KB

中文释义：参数量仅为 6114，存储占用为 40.92 KB。

来源：[Engineering-AI/full.txt:2821](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:2821)。

范文对应原因及边界：2816–2824 行将 parameter count 与数值、storage footprint 与单位数值直接配对。本文 has a parameter count of 4,643 和 uses 27.44 KB to store its weights 采用同类指标—数值就近组织；JESSOHRUL 3804–3808 行也将参数数量与存储量分开定义。uses ... to store 不是该范文原词，FLOPs 分句亦是本文适配。保留本文原值及最低范围，不借入范文 only、硬件验证或其他夸大力度。

## 相关记录

[完整改前改后对照](D:/MS-AgentNet-English/translation-guides/language-style-before-after-2026-09-13.md)保留历史候选；[二次复核报告](D:/MS-AgentNet-English/translation-guides/language-style-recheck-2026-09-13.md)保留全文段落与此前处置。以上两文件未覆盖。本文仅新增范文依据澄清记录，正文未修改。

