# 已批准的英文语言修改落实记录

日期：2026-09-13，北京时间23:40。

## 授权与实际范围

作者批准：“可以的，只要有原因且不改动我们原意的就可以采取”。本轮据此落实前述11项中仍需调整的10项，不将范文直接用词作为唯一改动依据。C04-L041与C04-L073虽然缺少直接范文替换依据，仍因减少嵌套、明确范围并经原意复核后采用。未扩展至其他可选项目、撤回项目或待核实图表。

C04-L166的现稿在实施前已更新，现句为：

```tex
Operation counts obtained using the \texttt{profile} function in the THOP library are supplemented with counts for attention operations and then converted to the number of floating-point operations required for a single forward pass.
```

这条较新表述已明确补加的是计数，符合中文所述流程。本轮保留，没有覆盖为旧对照中的拆句候选。此前报告的“尚未写入”属于历史状态，以下记录为本轮实际实施结果。

## 已实施的10项

### 1. LS-I01｜沿用

位置：[chapter01.tex:3](D:/MS-AgentNet-English/chapters/chapter01.tex:3)。

改前：

```tex
However, complex operating conditions make the stable extraction of degradation information more difficult, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity.
```

已写入：

```tex
However, complex operating conditions make it harder to extract degradation information consistently, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity.
```

原因：动词extract更早出现，consistently保留稳定提取要求。属于有收益的小修，原句并无语法错误。

### 2. LS-I04｜沿用

位置：[chapter01.tex:44](D:/MS-AgentNet-English/chapters/chapter01.tex:44)。

改前：

```tex
It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators using correlations on the feature-development cells.
```

已写入：

```tex
It then uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators.
```

原因：uses correlations ... to evaluate明确两个评价对象共同使用的依据，避免句末using只被暂读为修饰redundancy。中文以相关性结果为依据的次序亦一致。

### 3. LS-M02｜修订

位置：[chapter02.tex:90](D:/MS-AgentNet-English/chapters/chapter02.tex:90)。

改前：

```tex
Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

已写入：

```tex
Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V. These indicators are denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

原因：保留原被动构造句，只把末尾denoted的命名关系独立出来。明确命名的是两个指标，不是两个电压区间；不为主动语态新增We。段落仍为一段。

### 4. LS-M06｜沿用

位置：[chapter03.tex:57](D:/MS-AgentNet-English/chapters/chapter03.tex:57)。

改前：

```tex
Its computational cost can be expressed as:
```

已写入：

```tex
The computational cost of standard convolution can be expressed as:
```

原因：点明standard convolution，避免Its跨过parameter count与overfitting句再回找对象。只明确原公式所属对象，不改变成本、训练或过拟合判断。

### 5. LS-M07｜修订

位置：[chapter03.tex:108](D:/MS-AgentNet-English/chapters/chapter03.tex:108)。

改前：

```tex
The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

已写入：

```tex
The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

原因：只把passes it改为passes the normalized representation，保留其余句式，不必为此拆句。中文归一化后传递以及本稿LN(X_S)支持此对象。不得把RAA分支改写成不含自身残差的纯全局量。

### 6. LS-M08｜沿用

位置：[chapter03.tex:110](D:/MS-AgentNet-English/chapters/chapter03.tex:110)。

改前：

```tex
Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension.
```

已写入：

```tex
The input features are $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively. The input is first transposed so that the embedding dimension becomes the convolutional channel dimension.
```

原因：先完成输入张量及符号定义，再陈述转置，减少Given和where嵌套。2倍扩展→张量→B/N/d→转置→1×1/2d的顺序及全部信息保留。这是清晰度改善，不是Given结构有语法错误。

### 7. C04-L041｜修订

位置：[chapter04.tex:41](D:/MS-AgentNet-English/chapters/chapter04.tex:41)。

改前：

```tex
To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset.
```

已写入：

```tex
To evaluate how effectively group-level HI selection identifies inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset.
```

原因：将 the effectiveness of ... in identifying 改为 how effectively ... identifies，减少名词化与介词嵌套，仍评价有效程度；保留先交代评价目的、再说明比较的顺序。此项是本文清晰度调整，不声称范文要求替换 effectiveness。

### 8. C04-L073｜沿用

位置：[chapter04.tex:73](D:/MS-AgentNet-English/chapters/chapter04.tex:73)。

改前：

```tex
Within these ranges, two cells in the feature-development set of each dataset are used for model training and configuration: one for learning model parameters and the other for hyperparameter selection.
```

已写入：

```tex
For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges.
```

原因：将within these ranges贴近hyperparameter selection，范围所约束的对象更直接；一池学参数、另一池选配置的角色及四组编号不变。不改称独立测试或验证电池。

### 9. C04-L149｜沿用

位置：[chapter04.tex:149](D:/MS-AgentNet-English/chapters/chapter04.tex:149)。

改前：

```tex
To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively.
```

已写入：

```tex
To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions.
```

原因：preserve/extract与两个模块的动作配对更近，不靠respectively回配。may、计算代价、四个变体与其余内容不动，未新增机制或效率保证。

### 11. C04-L170｜沿用

位置：[chapter04.tex:170](D:/MS-AgentNet-English/chapters/chapter04.tex:170)。

改前：

```tex
In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models.
```

已写入：

```tex
In contrast, MS-AgentNet requires 0.045760 M FLOPs, has a parameter count of 4,643, and uses 27.44 KB to store its weights; all three values are the lowest among the five models.
```

原因：requires FLOPs、has a parameter count和uses ... to store weights分别对应运算、数量与存储；三个数就近关联，五模型最低范围和LSTM训练时间反例保留。

## 复核与验证

- 两名独立agent只读复核：一名负责引言/方法第1–6项，一名负责结果第7–11项，均结合中文源稿相应完整上下文。10项原意复核通过；FLOPs现稿保留。
- 四个章节相对实施前快照，差异恰好为上述10个目标句修改。数字序列、数学表达、LaTeX命令序列和段落边界均保持。标准卷积段指代被明确，DSConv段同名Its句保持。
- 中文source-zh目录全部文件哈希与实施前一致。没有修改图表、模型实现、实验、参考文献或其他论文文件。
- tools/check_translation.py：第2、4章PASS；第1章提示42/100，第3章提示$^2$及3/1，已在本轮实施前快照上重新运行并确认完全相同。未将这些既有提示误报为本轮新增，也未因检查器提示改变中文或技术内容。
- ./build.ps1（latexmk/XeLaTeX）成功，37页。日志无未定义引用、缺字、Overfull或Underfull提示。既有CJK字体重定义、ICC图片及运行环境locale警告仍在。
- 依PDF检查流程重新渲染并目视查看第1、5、10、15、16、21、23、29、31页，覆盖本轮10处修改；未见此次句子调整造成的遮挡、越界或公式/表格排版问题。不将这次局部版式检查称为全篇科学内容终审，既有图中文字和架构待核实项仍未处理。
- 当前英文以chapters及build/main.pdf为准。本轮未重建full-manuscript-bilingual.md，避免把其中已有旧批次内容误称为最新对照；准确本轮改前/改后由本记录承载。
- 为便于追溯，四个章节的实施前文本快照保存于build/language-apply-before/；其为本轮修改前内容，不是冻结中文源稿。

## 范文依据与批准链

[范文依据及适用边界](D:/MS-AgentNet-English/translation-guides/language-style-reference-reasons-2026-09-13.md)；[此前11项候选对照](D:/MS-AgentNet-English/translation-guides/language-style-before-after-2026-09-13.md)。本轮落实已讨论候选，不声称进行了新一轮范文通读。批准记录与progress.md已同步更新。

## 冻结中文源稿对应章节哈希

|文件|SHA-256|
|---|---|
|chapters/chapter01.tex|D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D|
|chapters/chapter02.tex|4C8B4C91A51FE86C53A20E95CD1949589E31F7282324A4935CC87759D33E1574|
|chapters/chapter03.tex|8C704EE04FA8BBC5EC3C9B9E9FBFC2E85C128B7DDF790E3573D2E39876FB67AE|
|chapters/chapter04.tex|2EE42E7208731779C60CA4C89811DB5969B1F52AFD57979B7D32301BFBDD860B|

