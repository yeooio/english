# 英文审校：11项推荐修改的改前—改后效果

本文件单独新建，供作者确认；不是已修改的论文。11项由上一轮二次复核的7项沿用和4项修订组成。5项可选默认保留，3项撤回不再推荐。这里确认的是语言修改的收益及原意保留，不保证全文或实验实现绝对无误。

本轮逐项检查：下列11项“改前”完整段落均与当前章节吻合。本轮仅整理已复核的对照，不新增修改意见；范文依据沿用二次复核记录，没有声称本轮又重新审读三篇范文。

阅读方式：下列只展示发生修改的完整句子，未展示的前后文均不改。拆句仍留在原自然段内；不拆并段落。完整段落、范文语境和核实边界见[二次复核报告](D:/MS-AgentNet-English/translation-guides/language-style-recheck-2026-09-13.md)。

## 1. LS-I01｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:3)。

改前：

However, complex operating conditions make the stable extraction of degradation information more difficult, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity.

改后（建议，尚未写入正文）：

However, complex operating conditions make it harder to extract degradation information consistently, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity.

效果与理由：动词extract更早出现，consistently保留稳定提取要求。属于有收益的小修，原句并无语法错误。

范文依据（二次复核时核对；释义/解释为助手分析）：Engineering-AI full.txt 65–97：`infer SOH from indirect sensor data`（由间接传感数据推断SOH）。只支持明确动词带对象的功能表达，不证明某个句式永远优于名词化。

## 2. LS-I04｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:44)。

改前：

It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators using correlations on the feature-development cells.

改后（建议，尚未写入正文）：

It then uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators.

效果与理由：uses correlations ... to evaluate明确两个评价对象共同使用的依据，避免句末using只被暂读为修饰redundancy。中文以相关性结果为依据的次序亦一致。

范文依据（二次复核时核对；释义/解释为助手分析）：JESSOHRUL full.txt 1797、1822–1834先计算相关系数，再`jointly evaluate`、保留和去冗余。只借依据→评价顺序，不继承其全电池数据范围或阈值。

## 3. LS-M02｜修订

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter02.tex:90)。

改前：

Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.

改后（建议，尚未写入正文）：

Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V. These indicators are denoted as HI13 and HI14, respectively\cite{ref31,ref52}.

效果与理由：保留原被动构造句，只把末尾denoted的命名关系独立出来。明确命名的是两个指标，不是两个电压区间；不为主动语态新增We。段落仍为一段。

范文依据（二次复核时核对；释义/解释为助手分析）：JESSOHRUL full.txt 1799–1811自然使用`four HIs are extracted`并逐项给出指标编号，支持清晰编号对应，而非强制主动化。

## 4. LS-M06｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter03.tex:57)。

改前：

Its computational cost can be expressed as:

改后（建议，尚未写入正文）：

The computational cost of standard convolution can be expressed as:

效果与理由：点明standard convolution，避免Its跨过parameter count与overfitting句再回找对象。只明确原公式所属对象，不改变成本、训练或过拟合判断。

范文依据（二次复核时核对；释义/解释为助手分析）：BMSFormer full.txt 766–789在公式前明确指称`The standard convolutions have`及computational cost，支持点名计量对象。

## 5. LS-M07｜修订

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter03.tex:108)。

改前：

The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

改后（建议，尚未写入正文）：

The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

效果与理由：只把passes it改为passes the normalized representation，保留其余句式，不必为此拆句。中文归一化后传递以及本稿LN(X_S)支持此对象。不得把RAA分支改写成不含自身残差的纯全局量。

范文依据（二次复核时核对；释义/解释为助手分析）：BMSFormer full.txt 735–744用`output from LGFA module`追踪模块输出。归一化及RAA残差的事实依据是本文第3章108、351–382行，不是范文架构。

## 6. LS-M08｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter03.tex:110)。

改前：

Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension.

改后（建议，尚未写入正文）：

The input features are $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively. The input is first transposed so that the embedding dimension becomes the convolutional channel dimension.

效果与理由：先完成输入张量及符号定义，再陈述转置，减少Given和where嵌套。2倍扩展→张量→B/N/d→转置→1×1/2d的顺序及全部信息保留。这是清晰度改善，不是Given结构有语法错误。

范文依据（二次复核时核对；释义/解释为助手分析）：Engineering-AI full.txt 845–853及828–829为置换/逆置换完整上下文，先明确对象和维度再给操作；本文张量和步骤不随范文更换。

## 7. C04-L041｜修订

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter04.tex:41)。

改前：

To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset.

改后（建议，尚未写入正文）：

To evaluate how effectively group-level HI selection identifies inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset.

效果与理由：旧候选by comparing位于whether从句之后，可能被挂到identifies，误读为用估计误差来筛选HI；whether还弱化了effectiveness的程度评价。改用how effectively并保留原目的→比较次序，不另引筛选规则。

范文依据（二次复核时核对；释义/解释为助手分析）：JESSOHRUL full.txt 1946–1959是HI输入方案的验证实验段，首句有`To validate the effectiveness`。验证方法与HI筛选操作应分清；具体筛选规则仍以本文为准。

## 8. C04-L073｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter04.tex:73)。

改前：

Within these ranges, two cells in the feature-development set of each dataset are used for model training and configuration: one for learning model parameters and the other for hyperparameter selection.

改后（建议，尚未写入正文）：

For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges.

效果与理由：将within these ranges贴近hyperparameter selection，范围所约束的对象更直接；一池学参数、另一池选配置的角色及四组编号不变。不改称独立测试或验证电池。

范文依据（二次复核时核对；释义/解释为助手分析）：BMSFormer full.txt 1344–1351区分训练和模型超参数设置；本文两电池的角色、范围与编号以本稿本小节为准，范文不能替代协议。

## 9. C04-L149｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter04.tex:149)。

改前：

To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively.

改后（建议，尚未写入正文）：

To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions.

效果与理由：preserve/extract与两个模块的动作配对更近，不靠respectively回配。may、计算代价、四个变体与其余内容不动，未新增机制或效率保证。

范文依据（二次复核时核对；释义/解释为助手分析）：BMSFormer full.txt 814–817：`DSConv separates the spatial and channel-wise operations`；Engineering-AI 2077–2090区分两卷积位置和功能。借模块→动作，不继承其消融操作。

## 10. C04-L166｜修订

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter04.tex:166)。

改前：

FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass.

改后（建议，尚未写入正文）：

An initial operation count is obtained using the \texttt{profile} function in the THOP library. After the count for attention operations is added, the total is converted to the number of floating-point operations required for a single forward pass.

效果与理由：明确数值流程：初始operation count→补加attention operation count→总数换算。旧候选直接说operations加入count仍不够精确。不得擅加MACs、乘2规则或声称已验证工具实现。

范文依据（二次复核时核对；释义/解释为助手分析）：JESSOHRUL full.txt 3793–3808及BMSFormer 1344–1370明确profile、单次前向和其他计量量。补计注意力来自中文第4章166行；原文所述流程与实际脚本一致性未在此语言任务中验证。

## 11. C04-L170｜沿用

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter04.tex:170)。

改前：

In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models.

改后（建议，尚未写入正文）：

In contrast, MS-AgentNet requires 0.045760 M FLOPs, has a parameter count of 4,643, and uses 27.44 KB to store its weights; all three values are the lowest among the five models.

效果与理由：requires FLOPs、has a parameter count和uses ... to store weights分别对应运算、数量与存储；三个数就近关联，五模型最低范围和LSTM训练时间反例保留。

范文依据（二次复核时核对；释义/解释为助手分析）：Engineering-AI full.txt 2816–2824有`a parameter count`及存储结果；JESSOHRUL 3799–3808区分参数量与权重存储。范文硬件验证不借入本文。

## 确认边界

- 此处11项仅为正文推荐修改；图表意见另见二次复核报告，未自动纳入。
- C04-L166只澄清稿件所述计数流程；未验证THOP脚本、补计是否重复或换算实现。
- 所有改后句须连同未改的上下文使用；例如C04-L170仍保留前句LSTM训练时间最短的限定，不能概括成MS-AgentNet所有指标均最低。
- 没有修改中文源稿、论文正文或图表，也没有进行与本次预览无关的编译。

