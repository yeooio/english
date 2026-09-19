# 全文反向回译审查：第4章与第5章

日期：2026-09-13。独立分工审查记录；仅新建本文件，没有改写正文。对象是当前 `chapters/chapter04.tex` 与 `chapter05.tex`，以 `source-zh/chapters/` 同名文件为技术语义基准。这是有上下文的回译与核对，不能称为不知道中文的盲审。精确中英文本由文件逐行装配；回译和五项判断逐段撰写。回译中的〔引用键〕只作定位简写，原始引用命令完整保留在上方中英快照。

覆盖：第4章44个正文自然段（包含公式引导与解释）、14个标题、5个独立公式；第5章3个自然段，共66个可见审查块。图表作为数字和语境证据查阅，图表本身的逐项审查由主报告负责；本文件没有声称逐个数据点核实图像。空白行、input及FloatBarrier不视为自然段。路径和行号以本轮快照为准。

## 阅读与证据边界

已读取当前翻译合同、workflow、style-guide、terminology、scientific-boundaries、usage-guide、house-style和expression-detail-rules，并阅读中文摘要与第1–5章理解任务背景。主审所查参考原文为下述full.txt实际范围，不以既有词库条目冒充本轮原文核查。本轮是审查，不新增全文粗译或范文硬性句数配额；既有句级分析作为索引，不将本轮局部核查说成三篇全部句子的重新统计。已有批准修复：第4章109/172行，第5章3行，见language-fixes-batch-01.md；仍保持。

| 证据ID | 已核实短引（英文原词） | 中文释义（助手翻译）与实际适用范围 |
|---|---|---|
| B1 | BMSFormer/full.txt:1361–1368：`a single forward pass`；`total number of trainable parameters`；`Storage size` | 单次前向传播；可训练参数总数；存储大小。读取1344–1368的计量说明，以及1669–1699资源比较；只借量的名称与比较功能，本文的注意力补计和数值独立。 |
| B2 | BMSFormer/full.txt:1373：`The layer configurations of these models`；1375：`the estimation results and errors` | 这些模型的层配置；估计结果和误差。对应配置引导及模型比较，读取1370–1376相应完整短段，不继承BMSFormer模型结论。 |
| J1 | JESSOHRUL/full.txt:1956–1957：`all four HIs are fed into the model together`；1968：`average MAE and MAPE` | 四个HI一起输入模型；平均MAE和MAPE。读取1946–1959的HI输入方案段及1960–1968结果片段，并回读1914–1943输入背景。后一个结果段TXT跨栏断开，故只作为明确短搭配证据，不用于完整段落句数或衔接统计。 |
| J2 | JESSOHRUL/full.txt:1981：`cross-cell generalization performance` | 跨电池泛化性能。读取1970–1981完整协议段：其同一电池30%训练/70%验证与本文两池角色不同，不能借来替换本文实验。 |
| J3 | JESSOHRUL/full.txt:3515–3516：`jointly integrated`；3529：`long-term degradation trends` | 共同集成；长期退化趋势。读取3498–3532完整消融段，借组件比较与时间尺度表达；不借其“最差/最好”范围或独特机制推断。 |
| J4 | JESSOHRUL/full.txt:3806–3808：`storage size, measured in kilobytes`；`os.path.getsize` | 以KB计量的存储大小及文件大小函数。读取3793–3808完整计量段，直接对应权重存储口径，不能称推理运行内存。 |
| E1 | Engineering-AI/full.txt:2082–2083：`pre-attention local enhancement`；`post-fusion refinement` | 注意力前局部增强；融合后细化。读取2077–2090完整组件导语与首条比较，本文删除/加入模块不同于范文替换标准卷积的操作。 |
| E2 | Engineering-AI/full.txt:2809：`a lightweight network architecture`；2821：`a parameter count`；2825：`reliance on stable constant-current segments` | 轻量化网络架构；参数量；依赖稳定恒流片段。读取2806–2825结论主体，结合2839–2841与2848恢复跨栏首尾；范文已有硬件验证，本文仍为部署潜力和未来验证。 |

上表定位均为TXT行号，未冒充PDF页码；短引用途针对对应上下文，不表示三篇范文对本文实验结论提供证据。没有找到对应协议/定义时，各段第5项明确记为本文适配。

## 问题汇总与最小建议

| ID | 位置 | 类别 | 判断和最小处理建议 |
|---|---|---|---|
| A1 | C04-L156 | 交叉复核后：可选澄清，不判误译 | 在模块消融语境下，`RAA is held fixed`自然地表示RAA设计保持不变，不足以判定英文在声称冻结权重。若作者希望排除跨语境误读，可选`the RAA module is retained in all variants, while only the convolutional scale is changed`；仅在实际冻结参数时才明确写冻结。 |
| A2 | C05-L005 | 交叉复核后：当前语境可接受 | `battery chemistries`在全文化学材料体系语境下可自然对应“电池体系”，不列为确定缩窄或必改。只有作者另有更广范围时才重新定词；不默认替换为可能引入电池包/系统层含义的`battery systems`。 |
| O1 | C04-L063 | 可选自然度 | `ordinary normal initialization`稍显累赘；若需要调整可用`normal initialization`，仍与`truncated normal`清晰区分。无误译。 |
| O2 | C04-L105及107、158 | 可选自然度/源稿比喻 | `nonlinear degradation tail`保留“非线性衰减尾部”，但略有直译感，三篇当前对应段未提供该完整搭配证据。确认确指末期下降段后可用`nonlinear late-life decline`；不能凭偏好把尾部改成knee point。 |
| S1 | C04-L107 | 源稿证据范围，非英译增义 | 0.037673是CX2_38整池MAPE；单凭该总体指标不足以单独推出末期子区间误差低。原中文已作此推断，英文忠实。需图中末期局部结果或子区间指标支撑；此轮不新增实验或偷偷降低中文结论。 |
| S2 | C04-L041 | 源稿定义可追溯性 | “综合相关性得分”可能指min(PCC,SCC)、平均或其他聚合，当前段未定义。英文`combined correlation score`忠实，没有擅加公式；应确认其对应定义，不能直接借范文“PCC和SCC均大于0.94”替代。 |
| S3 | C04-L109、154 | 源稿数值精度来源待核 | 中英所有数字一致。第109行平均MAE降幅从表打印均值重算约13.46%、25.97%、9.13%、22.90%，与正文13.50%、26.02%、9.11%、22.94%略异。第154行用0.0500→0.0225重算55.00%，0.0071→0.0059为16.90%，而正文/表Reduction为54.94%、16.52%。可能使用未四舍五入底数；需要原始精度确认，不能就此判英语数字错误。 |

审查未发现确定的实质漏译、擅加实验或数字被英译改变；交叉复核后，A1为可选澄清，A2在当前语境可接受。下文逐段记录保留初审提示，遇到分歧以本节交叉复核结论为准。可选自然度建议不构成正文写入。五项检查中“无新增”不等于为中文源稿原有论证强度背书。

## 逐段对照与五项核对

### C04-L001

位置：`source-zh/chapters/chapter04.tex:1` ↔ `chapters/chapter04.tex:1`。

中文原文：

```tex
本节基于四个公开电池数据集对所提 MS-AgentNet 模型进行系统性评估。研究设置多组验证实验，主要包含健康指标有效性验证、模型性能对比分析、模块消融与复杂度评估以及跨域适应性测试。其中，健康指标有效性实验用于验证所选特征对电池退化模式的表征能力，可有效评价模型输入的合理性；模型对比实验用于检验所提方法在跨电池场景下的估计精度与稳定性；通过消融实验与复杂度分析可量化核心模块的贡献程度，并评估模型的计算效率；最终通过跨数据集迁移实验进一步考察模型对数据域差异的适应能力。综合上述多维度实验结果，可全面验证所提 MS-AgentNet 模型在电池 SOH 估计任务中的有效性与适用性。
```

当前英文：

```tex
This section systematically evaluates MS-AgentNet on four public battery datasets. The experiments cover HI effectiveness, model performance comparisons, module ablation and complexity analysis, and cross-domain adaptation. The HI experiments examine whether the selected features can represent battery degradation patterns and thus provide suitable model inputs. The model comparisons assess estimation accuracy and stability across cells. Ablation studies and complexity analysis quantify the contributions of core modules and evaluate computational efficiency. Finally, cross-dataset transfer experiments further examine the model's ability to adapt to differences between data domains. Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.
```

中文回译：

本节在四个公开电池数据集上系统评估 MS-AgentNet。实验涵盖健康指标有效性、模型性能比较、模块消融与复杂度分析以及跨域适应。健康指标实验考察所选特征能否表征电池退化模式，从而提供适当的模型输入。模型比较评价跨电池的估计精度与稳定性。消融研究和复杂度分析量化核心模块的贡献，并评价计算效率。最后，跨数据集迁移实验进一步考察模型适应数据域差异的能力。这些实验共同对 MS-AgentNet 在电池 SOH 估计中的有效性和适用性提供综合评价。

1. 漏译、增译或原意：研究范围与各实验功能完整；verify译为evaluate符合评价语境，无实质结论升级。
2. 术语、数字、限定条件：四个数据集、四类实验及跨域任务均保留。
3. 英语自然简洁与直译痕迹：拆句后仍为一个自然段，主语清晰。
4. 夸大、绝对化、复杂词：comprehensive对应全面；并非新加全域有效性证明。
5. 三篇范文对应语境：J1可借实验功能次序；本文自己的实验角色属于适配。

### C04-L005

位置：`source-zh/chapters/chapter04.tex:5` ↔ `chapters/chapter04.tex:5`。

中文原文：

```tex
为评价模型的 SOH 估计性能，选取平均绝对误差（MAE）、平均绝对百分比误差（MAPE）、均方根误差（RMSE）和决定系数（R²）四项常用指标\cite{ref76}。
```

当前英文：

```tex
Four commonly used metrics are selected to evaluate SOH estimation performance: mean absolute error (MAE), mean absolute percentage error (MAPE), root mean square error (RMSE), and the coefficient of determination (R²)\cite{ref76}.
```

中文回译：

选取四个常用指标评价 SOH 估计性能：平均绝对误差（MAE）、平均绝对百分比误差（MAPE）、均方根误差（RMSE）和决定系数（R²）〔ref76〕。

1. 漏译、增译或原意：四项指标无遗漏。
2. 术语、数字、限定条件：MAE/MAPE/RMSE/R²名称准确，引用键保留。
3. 英语自然简洁与直译痕迹：常见指标列举，语法自然。
4. 夸大、绝对化、复杂词：无绝对化或复杂词。
5. 三篇范文对应语境：B1仅作指标报告语境；具体四指标定义为本文内容。

### C04-L007

位置：`source-zh/chapters/chapter04.tex:7` ↔ `chapters/chapter04.tex:7`。

中文原文：

```tex
MAE 表示全部评价样本中预测 SOH 与真实 SOH 之间绝对误差的平均值，用于反映模型的整体误差水平。该指标不会进一步放大单个较大偏差，能够较为直观地衡量总体估计精度。
```

当前英文：

```tex
MAE is the mean absolute difference between predicted and true SOH over all evaluation samples and reflects the overall error level. It does not further amplify individual large deviations and provides a direct measure of overall estimation accuracy.
```

中文回译：

MAE 是所有评价样本中预测 SOH 与真实 SOH 之间绝对差的平均值，反映整体误差水平。它不会进一步放大个别较大偏差，并直接衡量总体估计精度。

1. 漏译、增译或原意：均值、绝对偏差和不进一步放大较大误差均保留。
2. 术语、数字、限定条件：all evaluation samples保留全样本范围。
3. 英语自然简洁与直译痕迹：mean absolute difference自然；direct measure传达直观衡量。
4. 夸大、绝对化、复杂词：无新增数学优势；源稿对指标的解释被忠实保留。
5. 三篇范文对应语境：B1提供评价指标语境，解释句为本文适配。

### C04-L009

位置：`source-zh/chapters/chapter04.tex:9` ↔ `chapters/chapter04.tex:9`。

中文原文：

```tex
MAPE 通过真实 SOH 对绝对误差进行归一化，便于比较不同数据集上的估计性能。当真实 SOH 接近零时，MAPE 可能被显著放大，需结合 MAE 和 RMSE 进行综合评价。
```

当前英文：

```tex
MAPE normalizes absolute errors by the true SOH, allowing estimation performance to be compared across datasets. When the true SOH approaches zero, MAPE may become much larger and should be considered together with MAE and RMSE.
```

中文回译：

MAPE 用真实 SOH 对绝对误差归一化，使不同数据集上的估计性能可以比较。当真实 SOH 接近零时，MAPE 可能变得大得多，应与 MAE 和 RMSE 一起考虑。

1. 漏译、增译或原意：真实SOH作为归一化分母及接近零风险均保留。
2. 术语、数字、限定条件：may与approaches zero保留不确定性和条件。
3. 英语自然简洁与直译痕迹：become much larger比显著放大更普通，含义匹配。
4. 夸大、绝对化、复杂词：未增添统计显著性。
5. 三篇范文对应语境：B1仅支持指标名称；零分母风险表述是本文适配。

### C04-L011

位置：`source-zh/chapters/chapter04.tex:11` ↔ `chapters/chapter04.tex:11`。

中文原文：

```tex
RMSE 表示预测 SOH 与真实 SOH 之间均方误差的平方根。与 MAE 相比，RMSE 对较大的预测偏差赋予更高权重，可以进一步反映模型对较大误差的控制能力。
```

当前英文：

```tex
RMSE is the square root of the mean squared difference between predicted and true SOH. Compared with MAE, it assigns greater weight to large prediction deviations and thus further reflects the model's ability to limit large errors.
```

中文回译：

RMSE 是预测 SOH 与真实 SOH 之间平方差均值的平方根。与 MAE 相比，它赋予较大预测偏差更高的权重，因此进一步反映模型限制较大误差的能力。

1. 漏译、增译或原意：平方根、平方差均值与大误差权重完整。
2. 术语、数字、限定条件：与MAE比较对象准确。
3. 英语自然简洁与直译痕迹：limit large errors对应控制较大误差，自然。
4. 夸大、绝对化、复杂词：未把较高权重改为保证排除大误差。
5. 三篇范文对应语境：B1指标语境可借；细节为本文适配。

### C04-L013

位置：`source-zh/chapters/chapter04.tex:13` ↔ `chapters/chapter04.tex:13`。

中文原文：

```tex
R² 衡量模型对真实 SOH 变化的拟合程度，其值越接近 1，表明模型对整体退化趋势的拟合效果越好。
```

当前英文：

```tex
R² measures how well the model fits variations in the true SOH. A value closer to 1 indicates a better fit to the overall degradation trend.
```

中文回译：

R² 衡量模型对真实 SOH 变化的拟合程度。其值越接近 1，表示对总体退化趋势的拟合越好。

1. 漏译、增译或原意：拟合变化及接近1的方向一致。
2. 术语、数字、限定条件：R²和1保留。
3. 英语自然简洁与直译痕迹：how well ... fits自然，未中文硬译。
4. 夸大、绝对化、复杂词：未将拟合度直接升级为因果解释能力。
5. 三篇范文对应语境：B1指标语境；具体解释为本文适配。

### C04-L015

位置：`source-zh/chapters/chapter04.tex:15` ↔ `chapters/chapter04.tex:15`。

中文原文：

```tex
上述四项指标的数学定义如下：
```

当前英文：

```tex
The four metrics are defined as follows:
```

中文回译：

四项指标定义如下：

1. 漏译、增译或原意：公式引导语完整。
2. 术语、数字、限定条件：four准确。
3. 英语自然简洁与直译痕迹：常用定义引导句。
4. 夸大、绝对化、复杂词：无风险措辞。
5. 三篇范文对应语境：本文通用数学行文适配，无需硬配范文。

### C04-L037

位置：`source-zh/chapters/chapter04.tex:37` ↔ `chapters/chapter04.tex:37`。

中文原文：

```tex
其中，$y_i$ 和 $\hat{y}_i$ 分别表示第 $i$ 个样本的真实 SOH 和预测 SOH，$\bar{y}$ 表示评价样本中真实 SOH 的平均值，$n$ 表示评价样本总数。
```

当前英文：

```tex
where $y_i$ and $\hat{y}_i$ are the true and predicted SOH of the $i$th sample, respectively, $\bar{y}$ is the mean true SOH of the evaluation samples, and $n$ is the total number of evaluation samples.
```

中文回译：

其中，$y_i$ 和 $\hat{y}_i$ 分别为第 $i$ 个样本的真实和预测 SOH，$\bar{y}$ 为评价样本的真实 SOH 均值，$n$ 为评价样本总数。

1. 漏译、增译或原意：四个符号及各自对象完整。
2. 术语、数字、限定条件：真实/预测及均值和总数未交换。
3. 英语自然简洁与直译痕迹：where开头与公式连续，自然。
4. 夸大、绝对化、复杂词：无强度问题。
5. 三篇范文对应语境：B1的符号说明语境可借；本文evaluation samples范围保持。

### C04-L041

位置：`source-zh/chapters/chapter04.tex:41` ↔ `chapters/chapter04.tex:41`。

中文原文：

```tex
为验证组级健康指标筛选方法在识别跨电池稳定输入方面的有效性，本节以 Oxford 数据集为例比较不同健康指标输入下的 SOH 估计性能。根据 Cell1 上候选指标的 PCC 和 SCC，从 IC、DTV 和 DTC 三类特征中各选取一项综合相关性最高的指标，分别为 HI4、HI9 和 HI11，三者的综合相关性得分均高于 0.94。将上述指标与组级筛选得到的 CCCT 指标 HI1 分别输入 MS-AgentNet，并将 HI1、HI4、HI9 和 HI11 共同输入的方案记为 Fusion。不同输入下 Cell2--Cell8 的 SOH 估计结果见\cref{tab:4-hi-input}。
```

当前英文：

```tex
To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset. Based on the PCC and SCC of candidate HIs on Cell1, the indicator with the highest combined correlation score is selected from each of the IC, DTV, and DTC categories, giving HI4, HI9, and HI11, respectively. All three combined correlation scores exceed 0.94. These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet. The input combining HI1, HI4, HI9, and HI11 is denoted as Fusion. The SOH estimation results for Cell2--Cell8 with different inputs are given in \cref{tab:4-hi-input}.
```

中文回译：

为评价组级健康指标筛选识别跨电池稳定输入的有效性，本节在 Oxford 数据集上比较采用不同健康指标时的 SOH 估计性能。根据 Cell1 上候选健康指标的 PCC 和 SCC，从 IC、DTV 和 DTC 类别各选取综合相关性得分最高的指标，分别得到 HI4、HI9 和 HI11。三者的综合相关性得分均超过 0.94。这些指标和通过组级筛选得到的 CCCT 指标 HI1 分别输入 MS-AgentNet。将组合 HI1、HI4、HI9 和 HI11 的输入称为 Fusion。不同输入下 Cell2–Cell8 的 SOH 估计结果见表〔tab:4-hi-input〕。

1. 漏译、增译或原意：三类各一项、单项与Fusion输入方案均完整。
2. 术语、数字、限定条件：0.94及HI1/4/9/11、Cell1/2–8准确；综合相关性得分的具体定义需原稿自己交代，属S2。
3. 英语自然简洁与直译痕迹：separately fed into与input combining搭配可接受。
4. 夸大、绝对化、复杂词：未把单池高相关性写成跨池稳健证据。
5. 三篇范文对应语境：J1的单项/Fusion语境直接对应；范文HI编号和训练比例没有移入。

### C04-L043

位置：`source-zh/chapters/chapter04.tex:43` ↔ `chapters/chapter04.tex:43`。

中文原文：

```tex
结果表明，HI1 在 Cell2--Cell8 上始终保持较高的估计精度，其平均 MAE、RMSE 和 MAPE 均为五种输入方案中的最低值，平均 MAPE 为 0.00615，即 0.615\%。当四项健康指标共同作为输入时，Fusion 的三项平均误差均排名第四，说明多类健康指标的直接组合没有形成进一步的性能增益。
```

当前英文：

```tex
The results show that HI1 maintains high estimation accuracy across Cell2--Cell8, with the lowest average MAE, RMSE, and MAPE among the five input schemes. Its average MAPE is 0.00615, or 0.615\%. When all four HIs are used together, Fusion ranks fourth for all three average errors, showing that directly combining multiple types of HIs does not provide further performance gains.
```

中文回译：

结果表明，HI1 在 Cell2–Cell8 间保持较高估计精度，其平均 MAE、RMSE 和 MAPE 是五种输入方案中最低的。其平均 MAPE 为 0.00615，即 0.615%。四个健康指标一起使用时，Fusion 的三项平均误差均排第四，表明直接组合多类健康指标未提供进一步的性能提升。

1. 漏译、增译或原意：五方案最低、Fusion第四和无额外增益完整。
2. 术语、数字、限定条件：table_4_hi_input的Average行支持全部排名；0.00615×100%=0.615%。
3. 英语自然简洁与直译痕迹：ranks fourth for ... errors可理解且简洁。
4. 夸大、绝对化、复杂词：high/lowest均有Oxford这组范围。
5. 三篇范文对应语境：J1的average MAE and MAPE与Fusion适配准确；不能继承其第二/第三名。

### C04-L045

位置：`source-zh/chapters/chapter04.tex:45` ↔ `chapters/chapter04.tex:45`。

中文原文：

```tex
此外，同一健康指标的表征能力在不同电池间存在差异。例如，HI9 在 Cell7 上的估计误差低于 HI11，而在 Cell8 上则观察到相反结果。相比之下，组级筛选得到的 HI1 在七节电池上均取得最低的 MAE、RMSE 和 MAPE。上述结果表明，单节电池上的高相关性不能保证健康指标在组内其他电池上保持相同的表征能力，而组级筛选得到的 HI1 在该组 Oxford 电池上提供了更稳定的 SOH 估计输入。
```

当前英文：

```tex
Moreover, the representational capability of the same HI differs across cells. For example, HI9 yields lower estimation errors than HI11 on Cell7, whereas the opposite is observed on Cell8. In contrast, HI1 obtained through group-level selection achieves the lowest MAE, RMSE, and MAPE on all seven cells. These results show that a high correlation on one cell does not guarantee the same representational capability on other cells in the group. The group-selected HI1 provides a more stable input for SOH estimation on this group of Oxford cells.
```

中文回译：

此外，同一健康指标的表征能力因电池而异。例如，HI9 在 Cell7 上的估计误差低于 HI11，而 Cell8 上观察到相反情况。相比之下，组级筛选得到的 HI1 在全部七节电池上均取得最低 MAE、RMSE 和 MAPE。这些结果表明，一节电池上的高相关性不能保证在组内其他电池上具有相同的表征能力。组级筛选的 HI1 为该组 Oxford 电池的 SOH 估计提供了更稳定的输入。

1. 漏译、增译或原意：Cell7/8反向比较、HI1七池最低与高相关不保证稳健完整。
2. 术语、数字、限定条件：表中DTV在Cell7三误差均低于DTC，Cell8均高于；范围七池正确。
3. 英语自然简洁与直译痕迹：representational capability及the opposite is observed自然。
4. 夸大、绝对化、复杂词：does not guarantee是原文否定保证，并非应删除的绝对化褒义词。
5. 三篇范文对应语境：J1的组内HI有效性语境匹配；组级筛选是本文具体协议。

### C04-L050

位置：`source-zh/chapters/chapter04.tex:50` ↔ `chapters/chapter04.tex:50`。

中文原文：

```tex
为进一步考察 MS-AgentNet 的训练稳定性及轻量化模型的参数设置，本文对智能体矩阵的初始化策略、模型收敛表现和超参数配置进行分析。
```

当前英文：

```tex
To further examine the training stability of MS-AgentNet and the parameter settings of the lightweight model, this study analyzes agent matrix initialization, model convergence, and hyperparameter configuration.
```

中文回译：

为进一步考察 MS-AgentNet 的训练稳定性及该轻量化模型的参数设置，本研究分析智能体矩阵初始化、模型收敛和超参数配置。

1. 漏译、增译或原意：初始化、收敛、超参数三项保留。
2. 术语、数字、限定条件：training stability与标题robustness上下文对象一致。
3. 英语自然简洁与直译痕迹：普通科学英语，可保留。
4. 夸大、绝对化、复杂词：无复杂词堆积。
5. 三篇范文对应语境：E1仅对应模块分析功能；初始化细节没有三篇对应证据，本文适配。

### C04-L054

位置：`source-zh/chapters/chapter04.tex:54` ↔ `chapters/chapter04.tex:54`。

中文原文：

```tex
RAA 将智能体表示为与输入无关的静态可学习矩阵 $\mathbf A\in\mathbb R^{n_a\times d}$，用于全局特征聚合，智能体数量固定为 $n_a=2$。矩阵参数采用均值为 0、标准差为 0.02 的正态分布初始化：
```

当前英文：

```tex
RAA represents the agents as a static learnable matrix $\mathbf A\in\mathbb R^{n_a\times d}$ that is independent of the input and used for global feature aggregation. The number of agents is fixed at $n_a=2$. The matrix parameters are initialized from a normal distribution with a mean of 0 and a standard deviation of 0.02:
```

中文回译：

RAA 将智能体表示为静态可学习矩阵 $\mathbf A\in\mathbb R^{n_a\times d}$，该矩阵与输入无关，用于全局特征聚合。智能体数量固定为 $n_a=2$。矩阵参数从均值为 0、标准差为 0.02 的正态分布中初始化：

1. 漏译、增译或原意：与输入无关、静态、可学习、聚合完整。
2. 术语、数字、限定条件：矩阵维数、n_a=2、均值0与标准差0.02正确。
3. 英语自然简洁与直译痕迹：static learnable可同时成立；未混成不可训练。
4. 夸大、绝对化、复杂词：固定数量是具体条件，无泛化主张。
5. 三篇范文对应语境：本文RAA特有参数定义；不能冒称范文同一智能体初始化。

### C04-L061

位置：`source-zh/chapters/chapter04.tex:61` ↔ `chapters/chapter04.tex:61`。

中文原文：

```tex
式中，$A_{ij}$ 表示第 $i$ 个智能体在第 $j$ 维特征上的参数。该初始化能够为不同智能体提供幅值较小且非一致的初始参数，避免其处于完全相同的初始状态。
```

当前英文：

```tex
where $A_{ij}$ is the parameter of the $i$th agent in the $j$th feature dimension. This initialization gives different agents small, nonidentical initial parameters, avoiding identical initial states.
```

中文回译：

其中，$A_{ij}$ 是第 $i$ 个智能体在第 $j$ 个特征维度上的参数。这种初始化使不同智能体获得数值较小且不相同的初始参数，避免相同的初始状态。

1. 漏译、增译或原意：符号维度及小幅非一致初始化含义保留。
2. 术语、数字、限定条件：i/j指向正确。
3. 英语自然简洁与直译痕迹：nonidentical准确普通；避免重复initial是可选审美而非缺陷。
4. 夸大、绝对化、复杂词：avoiding identical对应源稿，并未新增收敛保证。
5. 三篇范文对应语境：本文参数说明适配，无对应范文结论可借。

### C04-L063

位置：`source-zh/chapters/chapter04.tex:63` ↔ `chapters/chapter04.tex:63`。

中文原文：

```tex
三种初始化方案的对比结果如\cref{tab:4-3-initialization}所示。各方案对应的 $R^2$ 为 0.98527～0.98645，RMSE 为 0.00774～0.00805，MAE 为 0.00485～0.00499，表明其预测性能较为接近。截断正态通过限定采样范围控制参数幅值，Xavier 均匀初始化则根据网络层的输入和输出维度调整参数方差。相比之下，普通正态初始化能够直接为静态智能体矩阵提供以零为中心的小幅随机参数，且不依赖额外的范围限制或维度缩放。因此，本文采用普通正态初始化作为默认设置。
```

当前英文：

```tex
The comparison of three initialization schemes is presented in \cref{tab:4-3-initialization}. Their $R^2$ values range from 0.98527 to 0.98645, RMSE from 0.00774 to 0.00805, and MAE from 0.00485 to 0.00499, indicating similar prediction performance. Truncated normal initialization controls parameter magnitudes by restricting the sampling range, while Xavier uniform initialization adjusts parameter variance according to the input and output dimensions of a layer. In comparison, ordinary normal initialization directly provides small, zero-centered random parameters for the static agent matrix without additional range restrictions or dimension-based scaling. It is therefore used as the default setting.
```

中文回译：

三种初始化方案的比较见表〔tab:4-3-initialization〕。其 R² 为 0.98527 至 0.98645，RMSE 为 0.00774 至 0.00805，MAE 为 0.00485 至 0.00499，表明预测性能相近。截断正态初始化通过限制采样范围控制参数幅值，而 Xavier 均匀初始化根据某层的输入和输出维度调整参数方差。相比之下，普通正态初始化直接为静态智能体矩阵提供以零为中心的小幅随机参数，无需额外范围限制或基于维度的缩放。因此，将其作为默认设置。

1. 漏译、增译或原意：三方案比较、两种策略说明及默认选择理由完整。
2. 术语、数字、限定条件：表_4_3_initialization各区间逐项吻合。
3. 英语自然简洁与直译痕迹：ordinary normal initialization略累赘，可选简为normal initialization，与truncated normal的对比不受损。
4. 夸大、绝对化、复杂词：similar保留接近，未宣称普通正态最优。
5. 三篇范文对应语境：初始化方案理由是本文适配；E1只提供比较组件功能。

### C04-L065

位置：`source-zh/chapters/chapter04.tex:65` ↔ `chapters/chapter04.tex:65`。

中文原文：

```tex
模型收敛特性通过收敛速度和训练后期损失波动共同评价。将训练损失首次降至首轮损失 10\% 以下的训练轮次定义为收敛阈值轮次，并采用最后 20 轮损失的均值和标准差描述训练后期的收敛状态。如\cref{tab:4-3}所示，各次训练均达到预设收敛阈值。Oxford 和 MIT 数据集上的收敛阈值轮次中位数分别为 26 和 7，训练后期损失标准差中位数分别为 $2.38\times10^{-4}$ 和 $4.84\times10^{-6}$。上述结果表明，MS-AgentNet 在当前实验设置下能够稳定收敛，且训练后期的损失波动较小。
```

当前英文：

```tex
Model convergence is evaluated through both convergence speed and loss fluctuations in the late training stage. The convergence threshold epoch is defined as the first epoch at which the training loss falls below 10\% of the first-epoch loss. The mean and standard deviation of the loss over the final 20 epochs describe the late-stage convergence state. As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$. These results show that MS-AgentNet converges stably under the current experimental settings, with small loss fluctuations in the late training stage.
```

中文回译：

通过收敛速度和训练后期的损失波动共同评价模型收敛。收敛阈值轮次定义为训练损失首次低于首轮损失 10% 的轮次。最后 20 轮损失的均值和标准差描述后期收敛状态。如表〔tab:4-3〕所示，每次训练均达到预设阈值。Oxford 和 MIT 数据集的收敛阈值轮次中位数分别为 26 和 7，后期损失标准差中位数分别为 $2.38\times10^{-4}$ 和 $4.84\times10^{-6}$。这些结果表明，MS-AgentNet 在当前实验设置下稳定收敛，训练后期损失波动较小。

1. 漏译、增译或原意：阈值定义、最后20轮、每次训练达到阈值和当前设置完整。
2. 术语、数字、限定条件：首轮10%、26/7、两项SD与表_4_3一致。
3. 英语自然简洁与直译痕迹：convergence threshold epoch定义后可使用；converges stably可接受。
4. 夸大、绝对化、复杂词：under the current experimental settings关键限制保留。
5. 三篇范文对应语境：本文收敛协议适配；不能引用范文为阈值选择背书。

### C04-L073

位置：`source-zh/chapters/chapter04.tex:73` ↔ `chapters/chapter04.tex:73`。

中文原文：

```tex
MS-AgentNet 的主要超参数包括学习率、网络深度 $L$ 和嵌入维度 $d$，各参数的配置范围见\cref{tab:4-1}。在上述范围内，各数据集利用特征开发集合中的两节电池完成模型训练和配置，其中一节用于模型参数学习，另一节用于超参数配置。Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 数据集对应的训练电池与配置电池分别为 Cell1 与 Cell2、CS2\_36 与 CS2\_37、CX2\_36 与 CX2\_37 以及 b3c8 与 b3c13。
```

当前英文：

```tex
The main hyperparameters of MS-AgentNet are the learning rate, network depth $L$, and embedding dimension $d$. Their configuration ranges are listed in \cref{tab:4-1}. Within these ranges, two cells in the feature-development set of each dataset are used for model training and configuration: one for learning model parameters and the other for hyperparameter selection. The training and configuration-selection cells are Cell1 and Cell2 for Oxford, CS2\_36 and CS2\_37 for CALCE CS2, CX2\_36 and CX2\_37 for CALCE CX2, and b3c8 and b3c13 for MIT/Severson, respectively.
```

中文回译：

MS-AgentNet 的主要超参数为学习率、网络深度 $L$ 和嵌入维度 $d$。其配置范围列于表〔tab:4-1〕。在这些范围内，每个数据集特征开发集合中的两节电池用于模型训练和配置：一节用于学习模型参数，另一节用于超参数选择。Oxford 的训练电池和配置选择电池分别为 Cell1 和 Cell2，CALCE CS2 为 CS2_36 和 CS2_37，CALCE CX2 为 CX2_36 和 CX2_37，MIT/Severson 为 b3c8 和 b3c13。

1. 漏译、增译或原意：两池分别训练/配置、四组映射完整。
2. 术语、数字、限定条件：Cell1/2、CS2_36/37、CX2_36/37、b3c8/13未互换。
3. 英语自然简洁与直译痕迹：configuration-selection cell准确但属本文角色词，非多余复杂词。
4. 夸大、绝对化、复杂词：未增设独立测试集或声称无泄漏。
5. 三篇范文对应语境：B2的layer configurations可借；feature-development与configuration-selection为本文协议适配。

### C04-L075

位置：`source-zh/chapters/chapter04.tex:75` ↔ `chapters/chapter04.tex:75`。

中文原文：

```tex
五种模型的层配置见\cref{tab:4-4}。
```

当前英文：

```tex
The layer configurations of the five models are given in \cref{tab:4-4}.
```

中文回译：

五种模型的层配置见表〔tab:4-4〕。

1. 漏译、增译或原意：表引导完整。
2. 术语、数字、限定条件：five与tab:4-4准确。
3. 英语自然简洁与直译痕迹：layer configurations自然。
4. 夸大、绝对化、复杂词：无强度问题。
5. 三篇范文对应语境：B2有完全对应的layer configurations，语境相同。

### C04-L079

位置：`source-zh/chapters/chapter04.tex:79` ↔ `chapters/chapter04.tex:79`。

中文原文：

```tex
确定后的模型配置保持不变。在后续 SOH 估计性能比较中，MS-AgentNet 采用学习率 0.001、网络深度 $L=1$ 和嵌入维度 $d=16$。
```

当前英文：

```tex
Once selected, the model configurations remain fixed. In the subsequent SOH estimation comparisons, MS-AgentNet uses a learning rate of 0.001, network depth $L=1$, and embedding dimension $d=16$.
```

中文回译：

一旦选定，模型配置便保持固定。后续 SOH 估计比较中，MS-AgentNet 使用学习率 0.001、网络深度 $L=1$ 和嵌入维度 $d=16$。

1. 漏译、增译或原意：配置固定及后续比较设置完整。
2. 术语、数字、限定条件：0.001、L=1、d=16准确；与复杂度实验另套设置未混用。
3. 英语自然简洁与直译痕迹：Once selected表达清楚。
4. 夸大、绝对化、复杂词：fixed是协议事实，非绝对化宣传。
5. 三篇范文对应语境：B1/B2仅配置表达可借；本文数值独立。

### C04-L085

位置：`source-zh/chapters/chapter04.tex:85` ↔ `chapters/chapter04.tex:85`。

中文原文：

```tex
根据第~2.3~节的筛选结果，Oxford 数据集采用 HI1，CALCE CS2 数据集采用 HI1 和 HI2，CALCE CX2 数据集采用 HI13，MIT/Severson 数据集采用 HI14 和 HI15。在上述健康指标输入下，进一步比较 MS-AgentNet 与四种基线模型的 SOH 估计性能。
```

当前英文：

```tex
Based on the selection results in Section~2.3, the inputs are HI1 for Oxford, HI1 and HI2 for CALCE CS2, HI13 for CALCE CX2, and HI14 and HI15 for MIT/Severson. With these HI inputs, the SOH estimation performance of MS-AgentNet is further compared with that of four baseline models.
```

中文回译：

根据第 2.3 节的筛选结果，Oxford 的输入为 HI1，CALCE CS2 为 HI1 和 HI2，CALCE CX2 为 HI13，MIT/Severson 为 HI14 和 HI15。在这些健康指标输入下，进一步将 MS-AgentNet 的 SOH 估计性能与四种基线模型比较。

1. 漏译、增译或原意：各数据集所选输入及四基线比较完整。
2. 术语、数字、限定条件：HI1；HI1/HI2；HI13；HI14/HI15映射准确。
3. 英语自然简洁与直译痕迹：With these HI inputs自然承接。
4. 夸大、绝对化、复杂词：无额外性能保证。
5. 三篇范文对应语境：J1的selected HIs用于比较语境对应，本文HI组合不照搬。

### C04-L090

位置：`source-zh/chapters/chapter04.tex:90` ↔ `chapters/chapter04.tex:90`。

中文原文：

```tex
\Cref{fig:4-2}和\cref{tab:4-5}展示了 MS-AgentNet、CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 在 Oxford Cell2--Cell8 上的 SOH 估计结果和误差。
```

当前英文：

```tex
\Cref{fig:4-2} and \cref{tab:4-5} present the SOH estimation results and errors of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM on Oxford Cell2--Cell8.
```

中文回译：

图〔fig:4-2〕和表〔tab:4-5〕给出 MS-AgentNet、CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 在 Oxford Cell2–Cell8 上的 SOH 估计结果及误差。

1. 漏译、增译或原意：模型名单与图表引用完整。
2. 术语、数字、限定条件：五模型及Cell2–Cell8正确。
3. 英语自然简洁与直译痕迹：present ... results and errors自然。
4. 夸大、绝对化、复杂词：无优劣预断。
5. 三篇范文对应语境：B2原文同类result/error列举可直接借，模型名替换属于适配。

### C04-L094

位置：`source-zh/chapters/chapter04.tex:94` ↔ `chapters/chapter04.tex:94`。

中文原文：

```tex
总体而言，各模型均能够跟踪电池的容量衰减趋势，但在局部变化区间的预测结果上存在差异。值得注意的是，Cell4 的局部偏离和 Cell6 后段的快速下降使各模型表现出不同程度的跟踪偏差。局部放大结果显示，MS-AgentNet 在上述变化区间仍能较好地跟踪真实 SOH。对于退化轨迹相对平滑的 Cell3 和 Cell5，其预测结果也与真实 SOH 保持较好的贴合。
```

当前英文：

```tex
Overall, all models track the capacity fade trends, but their predictions differ in regions with local variations. In particular, the local deviations in Cell4 and the rapid decline in the later stage of Cell6 lead to different degrees of tracking error. The enlarged views show that MS-AgentNet still tracks the true SOH well in these regions. Its predictions also closely follow the true SOH of Cell3 and Cell5, whose degradation trajectories are relatively smooth.
```

中文回译：

总体上，所有模型均跟踪容量衰减趋势，但在存在局部变化的区间，其预测有所不同。具体而言，Cell4 的局部偏离以及 Cell6 后期的快速下降导致不同程度的跟踪误差。放大图表明，MS-AgentNet 在这些区间仍能较好地跟踪真实 SOH。对于退化轨迹相对平滑的 Cell3 和 Cell5，其预测也紧贴真实 SOH。

1. 漏译、增译或原意：各模型趋势、Cell4/6困难区和Cell3/5平滑区完整。
2. 术语、数字、限定条件：电池及阶段未交换；图像证据需结合主报告的图审，不以文字审代替图审。
3. 英语自然简洁与直译痕迹：tracks/closely follow用于轨迹，搭配正确。
4. 夸大、绝对化、复杂词：well对应较好；未称完美拟合。
5. 三篇范文对应语境：B2预测曲线比较语境相符；具体轨迹是本文观察。

### C04-L096

位置：`source-zh/chapters/chapter04.tex:96` ↔ `chapters/chapter04.tex:96`。

中文原文：

```tex
定量结果表明，MS-AgentNet 在 Cell2、Cell3、Cell5 和 Cell6 上的 $R^2$、MAE、MAPE 和 RMSE 均为最优，并在 Cell4 上取得最高的 $R^2$ 和最低的 RMSE。从 Cell2--Cell8 的平均结果来看，MS-AgentNet 的平均 $R^2$ 为 0.98379，平均 MAE、MAPE 和 RMSE 分别为 0.00524、0.00615 和 0.00638，均在五种模型中排名第一。与 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 相比，其平均 MAE 分别降低了 2.42\%、8.87\%、4.20\% 和 12.52\%，平均 MAPE 分别降低了 2.38\%、8.48\%、3.76\% 和 12.52\%，平均 RMSE 分别降低了 5.06\%、11.39\%、5.62\% 和 15.83\%。上述结果表明，MS-AgentNet 在 Oxford 数据集上具有较高的 SOH 估计精度和良好的预测鲁棒性。
```

当前英文：

```tex
The quantitative results show that MS-AgentNet achieves the best $R^2$, MAE, MAPE, and RMSE on Cell2, Cell3, Cell5, and Cell6, as well as the highest $R^2$ and lowest RMSE on Cell4. Averaged over Cell2--Cell8, its $R^2$ is 0.98379, and its MAE, MAPE, and RMSE are 0.00524, 0.00615, and 0.00638, respectively, ranking first among the five models for all four metrics. Compared with CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by 2.42\%, 8.87\%, 4.20\%, and 12.52\%, its average MAPE by 2.38\%, 8.48\%, 3.76\%, and 12.52\%, and its average RMSE by 5.06\%, 11.39\%, 5.62\%, and 15.83\%, respectively. These results show that MS-AgentNet achieves high SOH estimation accuracy and good prediction robustness on the Oxford dataset.
```

中文回译：

定量结果表明，MS-AgentNet 在 Cell2、Cell3、Cell5 和 Cell6 上取得最优的 R²、MAE、MAPE 和 RMSE，同时在 Cell4 上取得最高 R² 和最低 RMSE。在 Cell2–Cell8 上平均后，其 R² 为 0.98379，MAE、MAPE 和 RMSE 分别为 0.00524、0.00615 和 0.00638，四个指标在五种模型中均排第一。相较于 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM，其平均 MAE 分别降低 2.42%、8.87%、4.20% 和 12.52%，平均 MAPE 分别降低 2.38%、8.48%、3.76% 和 12.52%，平均 RMSE 分别降低 5.06%、11.39%、5.62% 和 15.83%。这些结果表明，MS-AgentNet 在 Oxford 数据集上具有较高 SOH 估计精度和良好的预测鲁棒性。

1. 漏译、增译或原意：单池最优范围及总体均值和12个降幅完整。
2. 术语、数字、限定条件：表_4_5支持单池排名、均值与所列相对降幅。
3. 英语自然简洁与直译痕迹：Averaged over ... its R²语法成立，均值对象清楚。
4. 夸大、绝对化、复杂词：没有把Cell7/8也说成最优；robustness原稿已有。
5. 三篇范文对应语境：B2比较语境合适，范文结论不能代替本表证据。

### C04-L103

位置：`source-zh/chapters/chapter04.tex:103` ↔ `chapters/chapter04.tex:103`。

中文原文：

```tex
本节进一步比较了 MS-AgentNet 与四种基线模型在 CALCE CS2、CALCE CX2 和 MIT/Severson 数据集上的 SOH 估计性能。上述数据集在电池材料和充放电协议方面与 Oxford 数据集存在差异，并呈现出平滑衰减、阶段性转折和寿命后期加速衰减等多样化退化动态。各模型的 SOH 估计结果如\cref{fig:4-3}所示。
```

当前英文：

```tex
This section further compares MS-AgentNet with the four baseline models on the CALCE CS2, CALCE CX2, and MIT/Severson datasets. These datasets differ from Oxford in battery materials and charge-discharge protocols and show diverse degradation dynamics, including smooth capacity fade, transitions between stages, and accelerated late-life degradation. The SOH estimation results are shown in \cref{fig:4-3}.
```

中文回译：

本节在 CALCE CS2、CALCE CX2 和 MIT/Severson 数据集上进一步将 MS-AgentNet 与四种基线模型进行比较。这些数据集在电池材料和充放电协议上不同于 Oxford，并表现出不同的退化动态，包括平滑容量衰减、阶段间转折和寿命后期加速退化。SOH 估计结果见图〔fig:4-3〕。

1. 漏译、增译或原意：三数据集、差异及三种退化动态完整。
2. 术语、数字、限定条件：in ... datasets未变成Oxford训练后跨数据集直接测试。
3. 英语自然简洁与直译痕迹：transitions between stages自然；少数术语在其他段保持一致。
4. 夸大、绝对化、复杂词：未新增跨域泛化主张。
5. 三篇范文对应语境：J2 cross-cell generalization语境可借，三个数据域分别训练的协议保持。

### C04-L105

位置：`source-zh/chapters/chapter04.tex:105` ↔ `chapters/chapter04.tex:105`。

中文原文：

```tex
从整体结果来看，各模型均能够跟踪不同电池的容量衰减趋势，但在局部非线性转折和寿命后期加速衰减阶段的预测表现上存在差异。其中，CX2\_38 经历了多次阶段性转折，并呈现出明显的非线性衰减尾部。局部放大结果显示，进入加速衰减阶段后，各模型的预测偏差逐渐扩大，MS-AgentNet 仍能较好地跟踪其加速衰减轨迹。对于退化轨迹较为连续的 CS2\_38 和 b3c29，MS-AgentNet 也能够保持与真实 SOH 的较好贴合。
```

当前英文：

```tex
Overall, all models track the capacity fade trends of different cells, but their prediction performance differs at local nonlinear transitions and during accelerated late-life degradation. In particular, CX2\_38 undergoes several transitions between stages and shows a clear nonlinear degradation tail. The enlarged views show that prediction deviations gradually increase during accelerated degradation, while MS-AgentNet still tracks the accelerated degradation trajectory well. For CS2\_38 and b3c29, whose degradation trajectories are more continuous, MS-AgentNet also maintains close agreement with the true SOH.
```

中文回译：

总体上，所有模型均跟踪不同电池的容量衰减趋势，但在局部非线性转折处和寿命后期加速退化期间，其预测性能存在差异。具体而言，CX2_38 经历多次阶段间转折，且有明显的非线性退化尾部。放大图显示，加速退化期间预测偏差逐渐增大，而 MS-AgentNet 仍较好地跟踪加速退化轨迹。对于退化轨迹更连续的 CS2_38 和 b3c29，MS-AgentNet 同样与真实 SOH 保持较好的一致性。

1. 漏译、增译或原意：非线性转折、末期加速、误差变大和较好跟踪完整。
2. 术语、数字、限定条件：CX2_38、CS2_38、b3c29及阶段准确。
3. 英语自然简洁与直译痕迹：nonlinear degradation tail有中文尾部直译感，属O2；更普通候选为nonlinear late-life decline，须确认尾部具体所指。
4. 夸大、绝对化、复杂词：still ... well保留原稿程度，未增完全跟踪。
5. 三篇范文对应语境：J3长短期退化语境可借；degradation tail未定位为三篇原搭配，属本文适配。

### C04-L107

位置：`source-zh/chapters/chapter04.tex:107` ↔ `chapters/chapter04.tex:107`。

中文原文：

```tex
\Cref{tab:4-6}列出了各模型在六节电池上的 SOH 估计误差。MS-AgentNet 在其中五节电池上的 $R^2$、MAE、MAPE 和 RMSE 均为最优。值得注意的是，在具有阶段性转折和非线性衰减尾部的 CX2\_38 上，MS-AgentNet 的 MAPE 仅为 0.037673，较 CNN-Transformer 和 Transformer 分别降低了 59.75\% 和 51.80\%，表明模型在寿命后期加速衰减阶段仍能保持较低的预测误差。
```

当前英文：

```tex
\Cref{tab:4-6} lists the SOH estimation errors of all models on six cells. MS-AgentNet achieves the best $R^2$, MAE, MAPE, and RMSE on five of them. Notably, on CX2\_38, which shows transitions between stages and a nonlinear degradation tail, its MAPE is only 0.037673, a reduction of 59.75\% and 51.80\% compared with CNN-Transformer and Transformer, respectively. This shows that the model maintains low prediction errors during accelerated late-life degradation.
```

中文回译：

表〔tab:4-6〕列出所有模型在六节电池上的 SOH 估计误差。MS-AgentNet 在其中五节电池上取得最优的 R²、MAE、MAPE 和 RMSE。值得注意的是，对于出现阶段间转折和非线性退化尾部的 CX2_38，其 MAPE 仅为 0.037673，分别比 CNN-Transformer 和 Transformer 低 59.75% 和 51.80%。这表明该模型在寿命后期加速退化阶段保持了较低的预测误差。

1. 漏译、增译或原意：与原中文对应，无译文独自新增末期判断。
2. 术语、数字、限定条件：五/六电池与0.037673、59.75%/51.80%吻合表_4_6；末期子区间证据见S1。
3. 英语自然简洁与直译痕迹：This shows指代前句整池MAPE，指代清楚但证据覆盖问题源稿已有。
4. 夸大、绝对化、复杂词：only对应仅；由整池误差推到末期低误差需局部图证，不应归咎单个show词。
5. 三篇范文对应语境：J2结果比较可借；本文局部结论必须用本文图/子区间指标支撑。

### C04-L109

位置：`source-zh/chapters/chapter04.tex:109` ↔ `chapters/chapter04.tex:109`。

中文原文：

```tex
从六节电池的平均结果来看，MS-AgentNet 的平均 $R^2$ 为 0.9896，平均 MAE、MAPE 和 RMSE 分别为 0.00707、0.013335 和 0.01188，均在五种模型中排名第一。与 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 相比，其平均 MAE 分别降低了 13.50\%、26.02\%、9.11\% 和 22.94\%，平均 MAPE 分别降低了 42.19\%、60.08\%、34.49\% 和 58.17\%，平均 RMSE 分别降低了 12.04\%、26.52\%、7.97\% 和 23.09\%。综合不同退化场景，MS-AgentNet 在平滑衰减、阶段性转折和寿命后期加速衰减过程中均保持了较低的估计误差，体现出较好的预测鲁棒性和跨电池泛化能力。
```

当前英文：

```tex
Across the six cells, MS-AgentNet achieves an average $R^2$ of 0.9896 and average MAE, MAPE, and RMSE of 0.00707, 0.013335, and 0.01188, respectively, ranking first among the five models for all four metrics. Compared with CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by 13.50\%, 26.02\%, 9.11\%, and 22.94\%, its average MAPE by 42.19\%, 60.08\%, 34.49\%, and 58.17\%, and its average RMSE by 12.04\%, 26.52\%, 7.97\%, and 23.09\%, respectively. Across different degradation scenarios, MS-AgentNet maintains low estimation errors during smooth capacity fade, transitions between stages, and accelerated late-life degradation, showing good prediction robustness and cross-cell generalization capability.
```

中文回译：

在六节电池上，MS-AgentNet 的平均 R² 为 0.9896，平均 MAE、MAPE 和 RMSE 分别为 0.00707、0.013335 和 0.01188，四项指标在五种模型中均排第一。相较于 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM，其平均 MAE 分别降低 13.50%、26.02%、9.11% 和 22.94%，平均 MAPE 分别降低 42.19%、60.08%、34.49% 和 58.17%，平均 RMSE 分别降低 12.04%、26.52%、7.97% 和 23.09%。在不同退化场景下，MS-AgentNet 在平滑容量衰减、阶段间转折和寿命后期加速退化期间保持较低估计误差，表现出良好的预测鲁棒性和跨电池泛化能力。

1. 漏译、增译或原意：总体均值、12个降幅与三个退化场景完整。
2. 术语、数字、限定条件：显示均值正确；部分降幅无法从表中四舍五入均值精确重算，见S3；英文数字无变化。
3. 英语自然简洁与直译痕迹：Across ... average搭配是此前已批准修复，保留。
4. 夸大、绝对化、复杂词：cross-cell没有改成跨数据集泛化；robustness程度源稿已有。
5. 三篇范文对应语境：J2跨池generalization与B2平均结果报告语境吻合；当前平均句已批准。

### C04-L117

位置：`source-zh/chapters/chapter04.tex:117` ↔ `chapters/chapter04.tex:117`。

中文原文：

```tex
当源域与目标域来自不同数据集时，化学体系、运行协议和退化轨迹差异可能引起域偏移\cite{ref52,ref59}。为评价 MS-AgentNet 的跨数据集迁移能力，本文设置源域直接测试和少样本适应两类实验。源域直接测试（source-only）仅利用源域参考电池训练模型，并在不使用目标域数据更新参数的情况下直接测试目标域电池；少样本适应则固定特征提取模块，利用目标域参考电池前 30\% 的循环数据更新读出层，再在目标域测试电池上进行评价\cite{ref52,ref58}。
```

当前英文：

```tex
When the source and target domains come from different datasets, differences in chemistry, operating protocols, and degradation trajectories may cause domain shift\cite{ref52,ref59}. To evaluate the cross-dataset transfer capability of MS-AgentNet, this study conducts source-only evaluation and few-shot adaptation experiments. In source-only evaluation, the model is trained only on the source-domain reference cell and directly tested on the target-domain cell without updating its parameters using target-domain data. In few-shot adaptation, the feature extraction modules are frozen, and the first 30\% of cycle data from the target-domain reference cell are used to update the readout layer before evaluation on the target-domain test cell\cite{ref52,ref58}.
```

中文回译：

当源域和目标域来自不同数据集时，化学体系、运行协议和退化轨迹上的差异可能造成域偏移〔ref52,ref59〕。为评价 MS-AgentNet 的跨数据集迁移能力，本研究开展源域直接评价和少样本适应实验。在源域直接评价中，模型仅在源域参考电池上训练，随后直接在目标域电池上测试，不使用目标域数据更新参数。在少样本适应中，特征提取模块被冻结，使用目标域参考电池前 30% 的循环数据更新读出层，之后在目标域测试电池上评价〔ref52,ref58〕。

1. 漏译、增译或原意：source-only与few-shot两类协议、冻结/更新对象均保留。
2. 术语、数字、限定条件：前30%来自目标参考电池，不是测试池；may与only保留。
3. 英语自然简洁与直译痕迹：feature extraction modules are frozen清楚。
4. 夸大、绝对化、复杂词：未将少样本适应包装成零样本或源域直接测试。
5. 三篇范文对应语境：本文跨域协议适配；不可照搬J2同池30/70%的不同协议。

### C04-L119

位置：`source-zh/chapters/chapter04.tex:119` ↔ `chapters/chapter04.tex:119`。

中文原文：

```tex
CALCE CS2、CALCE CX2 和 Oxford 分别视为三个数据域，其中 CS2\_36、CX2\_36 和 Oxford Cell1 用于源域训练或目标域适应，CS2\_38、CX2\_38 和 Oxford Cell3 仅用于目标域测试。CALCE CS2 与 CALCE CX2 均属于 LCO 化学体系，Oxford 采用 NCO-LCO 混合化学体系，因此实验同时覆盖同化学体系和跨化学体系迁移。为保持源域与目标域的输入定义一致，各迁移方向统一采用 $CCCT(3.8,\allowbreak 4.0)$ 和 $Q_{\mathrm{dch}}(3.8,\allowbreak 3.4)/C_{\mathrm{rated}}$ 两项健康指标。
```

当前英文：

```tex
CALCE CS2, CALCE CX2, and Oxford are treated as three data domains. CS2\_36, CX2\_36, and Oxford Cell1 are used for source-domain training or target-domain adaptation, while CS2\_38, CX2\_38, and Oxford Cell3 are used only for target-domain testing. CALCE CS2 and CALCE CX2 both use LCO chemistry, whereas Oxford uses a blended NCO-LCO chemistry. The experiments therefore cover both same-chemistry and cross-chemistry transfer. To keep the input definitions consistent between the source and target domains, all transfer directions use two HIs: $CCCT(3.8,\allowbreak 4.0)$ and $Q_{\mathrm{dch}}(3.8,\allowbreak 3.4)/C_{\mathrm{rated}}$.
```

中文回译：

将 CALCE CS2、CALCE CX2 和 Oxford 视为三个数据域。CS2_36、CX2_36 和 Oxford Cell1 用于源域训练或目标域适应，而 CS2_38、CX2_38 和 Oxford Cell3 仅用于目标域测试。CALCE CS2 和 CALCE CX2 均使用 LCO 化学体系，而 Oxford 使用 NCO-LCO 混合化学体系。因此，实验涵盖同化学体系和跨化学体系迁移。为保持源域和目标域的输入定义一致，所有迁移方向均使用两项健康指标：$CCCT(3.8,\allowbreak 4.0)$ 和 $Q_{\mathrm{dch}}(3.8,\allowbreak 3.4)/C_{\mathrm{rated}}$。

1. 漏译、增译或原意：三个域、源/适应池和仅测试池、两种化学跨度、两个输入完整。
2. 术语、数字、限定条件：所有电池编号、3.8/4.0/3.4及额定容量归一化准确。
3. 英语自然简洁与直译痕迹：same-chemistry/cross-chemistry清楚，技术必要。
4. 夸大、绝对化、复杂词：only保留测试隔离范围。
5. 三篇范文对应语境：本文特有迁移输入适配；三篇不提供同一协议证据。

### C04-L123

位置：`source-zh/chapters/chapter04.tex:123` ↔ `chapters/chapter04.tex:123`。

中文原文：

```tex
如\cref{tab:4-7}所示，CS2→CX2 和 CX2→CS2 的 $R^2$ 分别为 0.8421 和 0.7847，MAE 分别为 0.0697 和 0.0388，表明模型在两个 CALCE 数据域之间仍能较好地表征退化趋势。相比之下，四个涉及 Oxford 的迁移方向的 MAE 为 0.1530～0.6346，且 $R^2$ 均低于 0，显示直接迁移性能随数据域组合和迁移方向发生明显变化。
```

当前英文：

```tex
As shown in \cref{tab:4-7}, CS2→CX2 and CX2→CS2 achieve $R^2$ values of 0.8421 and 0.7847 and MAE values of 0.0697 and 0.0388, respectively, indicating that the model still represents degradation trends well when transferred between the two CALCE domains. In contrast, the four transfer directions involving Oxford yield MAE values of 0.1530–0.6346 and $R^2$ values below 0, showing that direct transfer performance varies considerably with the domain pair and transfer direction.
```

中文回译：

如表〔tab:4-7〕所示，CS2→CX2 和 CX2→CS2 的 R² 分别为 0.8421 和 0.7847，MAE 分别为 0.0697 和 0.0388，说明在两个 CALCE 域间迁移时，模型仍能较好地表征退化趋势。相比之下，四个涉及 Oxford 的迁移方向的 MAE 为 0.1530–0.6346，R² 低于 0，表明直接迁移性能随域组合及迁移方向显著变化。

1. 漏译、增译或原意：两CALCE较好趋势、Oxford四方向负R²及方向依赖完整。
2. 术语、数字、限定条件：0.8421/0.7847、0.0697/0.0388和0.1530–0.6346吻合表_4_7。
3. 英语自然简洁与直译痕迹：varies considerably自然；回译明显变化不代表统计显著。
4. 夸大、绝对化、复杂词：负结果未弱化或删除。
5. 三篇范文对应语境：B2/J2只能借结果比较句式；跨域迁移是本文适配。

### C04-L125

位置：`source-zh/chapters/chapter04.tex:125` ↔ `chapters/chapter04.tex:125`。

中文原文：

```tex
少样本适应结果见\cref{tab:4-8}。适应后，六个迁移方向的 MAE、MAPE 和 RMSE 均有所降低。以 MAE 为例，两个 CALCE 数据域之间的降幅为 21.91\%～45.91\%，CALCE→Oxford 方向的降幅为 86.84\%～87.61\%，Oxford→CALCE 方向的降幅为 13.27\%～31.21\%。从 $R^2$ 看，适应后的 CS2→CX2 和 CX2→CS2 分别达到 0.9566 和 0.8806，而四个涉及 Oxford 的迁移方向仍低于 0，表明涉及 Oxford 的跨数据集迁移较两个 CALCE 数据域之间的迁移更具挑战性。
```

当前英文：

```tex
The few-shot adaptation results are presented in \cref{tab:4-8}. After adaptation, MAE, MAPE, and RMSE decrease in all six transfer directions. For MAE, the reductions are 21.91\%–45.91\% between the two CALCE domains, 86.84\%–87.61\% for CALCE→Oxford, and 13.27\%–31.21\% for Oxford→CALCE. After adaptation, $R^2$ reaches 0.9566 for CS2→CX2 and 0.8806 for CX2→CS2 but remains below 0 in all four directions involving Oxford. This indicates that cross-dataset transfer involving Oxford is more challenging than transfer between the two CALCE domains.
```

中文回译：

少样本适应结果见表〔tab:4-8〕。适应后，所有六个迁移方向的 MAE、MAPE 和 RMSE 均下降。MAE 的降幅在两个 CALCE 域间为 21.91%–45.91%，CALCE→Oxford 为 86.84%–87.61%，Oxford→CALCE 为 13.27%–31.21%。适应后，CS2→CX2 的 R² 达到 0.9566，CX2→CS2 达到 0.8806，但四个涉及 Oxford 的方向仍低于 0。这说明涉及 Oxford 的跨数据集迁移比两个 CALCE 域间的迁移更具挑战。

1. 漏译、增译或原意：六方向均降、三组降幅和Oxford仍负完整。
2. 术语、数字、限定条件：表_4_7与4_8支持数值及全部三误差降低。
3. 英语自然简洁与直译痕迹：For MAE ...并列紧凑自然。
4. 夸大、绝对化、复杂词：更具挑战性仍在这组方向范围。
5. 三篇范文对应语境：本文source-only/few-shot对比适配，没有直接范文同协议出处。

### C04-L132

位置：`source-zh/chapters/chapter04.tex:132` ↔ `chapters/chapter04.tex:132`。

中文原文：

```tex
分别以 CS2\_36 和 CX2\_36 作为源域，使用 Oxford Cell1 的前置循环数据进行读出层适配，并将适配比例依次设置为 10\%、30\%、50\% 和 70\%，结果见\cref{tab:4-9}。
```

当前英文：

```tex
With CS2\_36 and CX2\_36 used as the respective source domains, the readout layer is adapted with early-cycle data from Oxford Cell1 at adaptation ratios of 10\%, 30\%, 50\%, and 70\%. The results are given in \cref{tab:4-9}.
```

中文回译：

分别使用 CS2_36 和 CX2_36 作为源域，以 Oxford Cell1 的早期循环数据按 10%、30%、50% 和 70% 的适应比例适配读出层。结果见表〔tab:4-9〕。

1. 漏译、增译或原意：两个源、Oxford参考池早期数据及四比例完整。
2. 术语、数字、限定条件：10/30/50/70与表_4_9一致。
3. 英语自然简洁与直译痕迹：early-cycle data表达前期数据，但前置若特指从首循环连续截取，应与4:117一起读。
4. 夸大、绝对化、复杂词：无主张加强。
5. 三篇范文对应语境：本文适配比例协议，不借J2的30/70划分含义。

### C04-L135

位置：`source-zh/chapters/chapter04.tex:135` ↔ `chapters/chapter04.tex:135`。

中文原文：

```tex
随着适配比例由 10\% 增至 70\%，两种源域设置下的 MAE、MAPE 和 RMSE 均持续下降。以 CS2 为源域时，MAE 由 0.0831 降至 0.0252，$R^2$ 由 -1.3934 提高至 0.7650，并在 50\% 适配比例下由负转正；以 CX2 为源域时，MAE 由 0.1095 降至 0.0559，$R^2$ 由 -3.2217 提高至 70\% 适配比例下的 -0.1268。四种适配比例下，CS2 源域的 $R^2$ 均高于 CX2 源域的对应结果。
```

当前英文：

```tex
As the adaptation ratio increases from 10\% to 70\%, MAE, MAPE, and RMSE decrease continuously for both source-domain settings. With CS2 as the source domain, MAE decreases from 0.0831 to 0.0252, while $R^2$ increases from -1.3934 to 0.7650 and becomes positive at an adaptation ratio of 50\%. With CX2 as the source domain, MAE decreases from 0.1095 to 0.0559, while $R^2$ increases from -3.2217 to -0.1268 at an adaptation ratio of 70\%. At all four adaptation ratios, the CS2 source domain yields higher $R^2$ values than the CX2 source domain.
```

中文回译：

当适应比例从 10% 增加至 70% 时，两种源域设置的 MAE、MAPE 和 RMSE 均持续下降。以 CS2 为源域时，MAE 从 0.0831 降至 0.0252，R² 从 -1.3934 升至 0.7650，并在 50% 适应比例时变为正值。以 CX2 为源域时，MAE 从 0.1095 降至 0.0559，R² 从 -3.2217 升至 70% 适应比例下的 -0.1268。在全部四种适应比例下，CS2 源域的 R² 均高于 CX2 源域。

1. 漏译、增译或原意：误差持续下降、CS2在50%变正、CX2仍负完整。
2. 术语、数字、限定条件：所有起止数值与表_4_9逐项一致；四比例排序正确。
3. 英语自然简洁与直译痕迹：at an adaptation ratio of 70%修饰终值，指向清楚。
4. 夸大、绝对化、复杂词：continuously在四个已测比例的语境，不等于所有比例数学连续单调。
5. 三篇范文对应语境：本文适配结果，范文仅可借一般指标报告。

### C04-L137

位置：`source-zh/chapters/chapter04.tex:137` ↔ `chapters/chapter04.tex:137`。

中文原文：

```tex
进一步比较相邻适配比例，CS2 和 CX2 源域从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。结果表明，增加目标域观测能够持续改善模型在 Oxford 数据域上的适配性能；在相同适配比例下，CS2 源域始终取得更低的估计误差和更高的 $R^2$，进一步体现了源域选择对跨数据集适配性能的影响。
```

当前英文：

```tex
Comparing adjacent adaptation ratios, increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively. Increasing it from 50\% to 70\% gives smaller reductions of 0.0114 and 0.0055. These results show that adding target-domain observations continuously improves adaptation performance on Oxford. At the same adaptation ratio, the CS2 source domain consistently yields lower estimation errors and higher $R^2$, further showing the effect of source-domain selection on cross-dataset adaptation performance.
```

中文回译：

比较相邻适应比例，从 30% 增加至 50% 时，CS2 和 CX2 源域的 MAE 分别下降 0.0224 和 0.0221。从 50% 增加至 70% 时，降幅较小，分别为 0.0114 和 0.0055。这些结果表明，增加目标域观测会持续改善 Oxford 上的适应性能。在相同适应比例下，CS2 源域持续取得更低估计误差和更高 R²，进一步显示源域选择对跨数据集适应性能的影响。

1. 漏译、增译或原意：相邻降幅变小、增加观测改善、同率CS2较好完整。
2. 术语、数字、限定条件：两组差值0.0224/0.0221与0.0114/0.0055由表_4_9直接重算成立。
3. 英语自然简洁与直译痕迹：Comparing adjacent adaptation ratios句式自然。
4. 夸大、绝对化、复杂词：consistently有四比例范围；不能解释为任意源域条件通用。
5. 三篇范文对应语境：本文适配，未把范文硬件或域结论带入。

### C04-L145

位置：`source-zh/chapters/chapter04.tex:145` ↔ `chapters/chapter04.tex:145`。

中文原文：

```tex
为进一步验证 MS-AgentNet 的有效性和效率，在主对比实验基础上开展消融研究与复杂度分析。消融研究通过移除或组合关键模块，考察各模块对预测性能的作用；复杂度分析则从计算量、参数量和存储占用等方面评估模型开销。
```

当前英文：

```tex
Ablation studies and complexity analysis are conducted in addition to the main comparison experiments to further evaluate the effectiveness and efficiency of MS-AgentNet. The ablation studies examine the effects of individual modules on prediction performance by removing or combining key modules, while the complexity analysis evaluates computational cost, parameter count, and storage size.
```

中文回译：

在主比较实验之外开展消融研究和复杂度分析，以进一步评价 MS-AgentNet 的有效性和效率。消融研究通过移除或组合关键模块考察单个模块对预测性能的影响，而复杂度分析评价计算成本、参数量和存储大小。

1. 漏译、增译或原意：消融与复杂度的各自功能完整。
2. 术语、数字、限定条件：计算/参数/存储三对象保留。
3. 英语自然简洁与直译痕迹：conducted in addition to自然表达在主比较基础上。
4. 夸大、绝对化、复杂词：evaluate对应验证，是实验评价语境，未添证明。
5. 三篇范文对应语境：E1组件贡献分析、B1复杂度指标功能对应。

### C04-L149

位置：`source-zh/chapters/chapter04.tex:149` ↔ `chapters/chapter04.tex:149`。

中文原文：

```tex
高效注意力通过压缩信息交互降低标准注意力的计算开销\cite{ref39,ref40,ref43,ref44}，但这一过程可能削弱局部细粒度退化信息的表达\cite{ref31}；直接叠加标准卷积虽然能够增强局部特征建模，却会增加参数量和计算负担\cite{ref31,ref71}。为兼顾局部信息保留与计算效率，MS-AgentNet 结合多尺度 DSConv 与 RAA，分别完成局部特征提取和跨位置信息交互。为考察两类模块的单独作用及组合效果，消融实验设置 M1–M4 四种变体。其中，M1 仅保留基础骨干网络，M2 在 M1 基础上加入多尺度 DSConv，M3 在 M1 基础上加入 RAA，M4 则同时集成多尺度 DSConv 与 RAA。
```

当前英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref31,ref71}. To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

中文回译：

高效注意力通过压缩信息交互减少标准注意力的计算开销〔ref39,ref40,ref43,ref44〕，但这一过程可能削弱细粒度局部退化信息的表征〔ref31〕。直接加入标准卷积能改善局部特征建模，但会增加参数量和计算负荷〔ref31,ref71〕。为结合局部信息保留与计算效率，MS-AgentNet 集成多尺度 DSConv 和 RAA，分别用于局部特征提取与跨位置信息交互。采用 M1–M4 四种变体检验其单独和共同作用。M1 仅保留基础骨干，M2 在 M1 上加入多尺度 DSConv，M3 在 M1 上加入 RAA，而 M4 同时集成多尺度 DSConv 和 RAA。

1. 漏译、增译或原意：可能削弱、标准卷积代价及M1–M4逐项组成完整。
2. 术语、数字、限定条件：各模型增添模块和分别职责准确。
3. 英语自然简洁与直译痕迹：compressing information interactions偏抽象，源稿本身如此；不要猜成低秩压缩。
4. 夸大、绝对化、复杂词：may关键限定保留；未新加过拟合因果。
5. 三篇范文对应语境：E1有组件作用/替换语境，但本文是加/删模块，不照抄其standard-convolution替换协议。

### C04-L152

位置：`source-zh/chapters/chapter04.tex:152` ↔ `chapters/chapter04.tex:152`。

中文原文：

```tex
如\cref{tab:4-10}所示，与基础模型 M1 相比，加入多尺度 DSConv 后，M2 在 CX2 和 Oxford 数据集上的综合平均误差分别降低约 1.20\% 和 8.45\%；加入 RAA 后，M3 在 CS2、CX2 和 Oxford 数据集上的综合平均误差分别降低约 3.18\%、11.60\% 和 15.49\%。两种模块单独使用时均改善了部分数据集上的估计结果，但未在四个数据集上同时取得更低误差。
```

当前英文：

```tex
As shown in \cref{tab:4-10}, compared with the basic model M1, adding multi-scale DSConv in M2 reduces the combined average error by approximately 1.20\% on CX2 and 8.45\% on Oxford. Adding RAA in M3 reduces the combined average error by approximately 3.18\%, 11.60\%, and 15.49\% on CS2, CX2, and Oxford, respectively. Each module improves estimation on some datasets when used alone, but neither yields lower errors on all four datasets.
```

中文回译：

如表〔tab:4-10〕所示，相较于基础模型 M1，M2 加入多尺度 DSConv 后，CX2 和 Oxford 上的综合平均误差分别下降约 1.20% 和 8.45%。M3 加入 RAA 后，CS2、CX2 和 Oxford 上的综合平均误差分别下降约 3.18%、11.60% 和 15.49%。各模块单独使用时均改善了一些数据集上的估计，但两者均未在所有四个数据集上取得更低误差。

1. 漏译、增译或原意：单模块部分有效、并非四域同时更低完整。
2. 术语、数字、限定条件：各降幅与表显示均值基本可重算；3.18%等属近似。
3. 英语自然简洁与直译痕迹：neither yields ...明确保留反例。
4. 夸大、绝对化、复杂词：approximately对应约；没有全面优越宣称。
5. 三篇范文对应语境：J3的M1/M2/M3组件比较功能可借，本文保留不利结果。

### C04-L154

位置：`source-zh/chapters/chapter04.tex:154` ↔ `chapters/chapter04.tex:154`。

中文原文：

```tex
当多尺度 DSConv 与 RAA 共同集成后，完整模型 M4 在四个数据集上均取得最低或并列最低的综合平均误差。以 CX2 和 Oxford 数据集为例，其综合平均误差分别由 M1 的 0.0500 和 0.0071 降低至 0.0225 和 0.0059，相对降低 54.94\% 和 16.52\%。在 CS2 数据集上，M3 的 MAE 略低于 M4，而 M4 在 RMSE、MAPE 和综合平均误差上表现更优。总体结果表明，完整模型获得了比单模块变体更稳定的综合表现，体现了多尺度局部特征提取与跨位置信息交互的互补作用。
```

当前英文：

```tex
When multi-scale DSConv and RAA are integrated, the full model M4 achieves the lowest or jointly lowest combined average error on all four datasets. On CX2 and Oxford, for example, it reduces the combined average error from 0.0500 and 0.0071 for M1 to 0.0225 and 0.0059, corresponding to relative reductions of 54.94\% and 16.52\%, respectively. On CS2, M3 has a slightly lower MAE than M4, while M4 performs better in RMSE, MAPE, and combined average error. Overall, the full model provides more consistent combined performance than the single-module variants, showing the complementary roles of multi-scale local feature extraction and cross-position information interactions.
```

中文回译：

多尺度 DSConv 与 RAA 集成时，完整模型 M4 在全部四个数据集上取得最低或并列最低的综合平均误差。例如，在 CX2 和 Oxford 上，它将 M1 的综合平均误差 0.0500 和 0.0071 分别降至 0.0225 和 0.0059，对应相对降幅 54.94% 和 16.52%。在 CS2 上，M3 的 MAE 略低于 M4，而 M4 在 RMSE、MAPE 和综合平均误差上更好。总体上，完整模型比单模块变体提供更一致的综合性能，显示多尺度局部特征提取与跨位置信息交互的互补作用。

1. 漏译、增译或原意：最低或并列、CX2/Oxford降幅、M3在CS2 MAE优势完整。
2. 术语、数字、限定条件：数值与表_4_10一致，但精度来源问题见S3。
3. 英语自然简洁与直译痕迹：more consistent combined performance自然传达稳定综合表现。
4. 夸大、绝对化、复杂词：互补作用源稿已有；未新增唯一因果证明。
5. 三篇范文对应语境：J3 joint integration语境对应，但不继承其独特因果归因。

### C04-L156

位置：`source-zh/chapters/chapter04.tex:156` ↔ `chapters/chapter04.tex:156`。

中文原文：

```tex
为进一步区分多尺度 DSConv 中两个卷积尺度的作用，固定 RAA 模块并仅调整卷积尺度，设置 S0（仅保留 RAA）、S5（RAA 与核长度为 5 的 DSConv-S）、S31（RAA 与核长度为 31 的 DSConv-L）和 SFull（RAA、DSConv-S 与 DSConv-L）四种尺度变体。其中，S0 和 SFull 分别与\cref{tab:4-10}中的 M3 和 M4 对应。
```

当前英文：

```tex
To further distinguish the roles of the two convolutional scales, RAA is held fixed while only the convolutional scale is changed. Four variants are considered: S0 (RAA only), S5 (RAA with DSConv-S of kernel length 5), S31 (RAA with DSConv-L of kernel length 31), and SFull (RAA, DSConv-S, and DSConv-L). S0 and SFull correspond to M3 and M4 in \cref{tab:4-10}, respectively.
```

中文回译：

为进一步区分两个卷积尺度的作用，保持 RAA 固定，仅改变卷积尺度。考虑四种变体：S0（仅 RAA）、S5（RAA 加核长度为 5 的 DSConv-S）、S31（RAA 加核长度为 31 的 DSConv-L）以及 SFull（RAA、DSConv-S 和 DSConv-L）。S0 和 SFull 分别对应表〔tab:4-10〕中的 M3 和 M4。

1. 漏译、增译或原意：四变体完整；held fixed可能被读成冻结RAA权重，见A1。
2. 术语、数字、限定条件：5/31及S0=M3、SFull=M4正确。
3. 英语自然简洁与直译痕迹：RAA is held fixed在消融语境可指结构或权重，存在技术歧义。
4. 夸大、绝对化、复杂词：未扩大结果强度，但不能未经确认默认为冻结。
5. 三篇范文对应语境：E1/J3模块保留/移除语境支持明确结构操作；本文固定含义仍需定。

### C04-L158

位置：`source-zh/chapters/chapter04.tex:158` ↔ `chapters/chapter04.tex:158`。

中文原文：

```tex
\Cref{tab:4-11}的结果显示，单一卷积尺度的收益随数据集而变化。在具有阶段性转折和非线性衰减尾部的 CX2 数据集上，S31 将综合平均误差由 S0 的 0.0442 降至 0.0348，相对降低 21.27\%，这一结果与 DSConv-L 进行长尺度特征细化的设计目标一致。在 MIT 数据集上，S5 相对 S0 降低约 3.85\%；在 CS2 和 Oxford 数据集上，S0 的综合平均误差仍低于两个单尺度变体。当两个卷积尺度共同使用时，SFull 在四个数据集上均取得最低的综合平均误差。与最佳单尺度变体相比，SFull 在 CX2 和 MIT 数据集上的误差分别降低 35.34\% 和 20.00\%。因此，同时保留短核与长核能够取得比单一尺度更一致的综合结果，支持多尺度 DSConv 的结构设计。
```

当前英文：

```tex
\Cref{tab:4-11} shows that the benefit of a single convolutional scale varies across datasets. On CX2, which has transitions between stages and a nonlinear degradation tail, S31 reduces the combined average error from 0.0442 for S0 to 0.0348, a relative reduction of 21.27\%. This result is consistent with the design goal of DSConv-L to refine features over longer time scales. On MIT, S5 reduces the error by approximately 3.85\% relative to S0. On CS2 and Oxford, S0 still has a lower combined average error than either single-scale variant. When both convolutional scales are used, SFull achieves the lowest combined average error on all four datasets. Compared with the best single-scale variant, SFull reduces the error by 35.34\% on CX2 and 20.00\% on MIT. Thus, retaining both short and long kernels provides more consistent combined results than using a single scale, supporting the multi-scale DSConv design.
```

中文回译：

表〔tab:4-11〕显示，单一卷积尺度的收益因数据集而异。在具有阶段间转折和非线性退化尾部的 CX2 上，S31 将 S0 的综合平均误差从 0.0442 降至 0.0348，相对下降 21.27%。这一结果与 DSConv-L 在较长时间尺度上细化特征的设计目标相符。在 MIT 上，S5 比 S0 的误差降低约 3.85%。在 CS2 和 Oxford 上，S0 的综合平均误差仍比任一单尺度变体低。使用两个卷积尺度时，SFull 在全部四个数据集上取得最低综合平均误差。与最好的单尺度变体相比，SFull 在 CX2 和 MIT 上分别降低误差 35.34% 和 20.00%。因此，同时保留短核和长核比单尺度给出更一致的综合结果，支持多尺度 DSConv 设计。

1. 漏译、增译或原意：单尺度收益异质性、反例、全尺度及设计一致关系完整。
2. 术语、数字、限定条件：21.27%、3.85%、35.34%、20.00%可由表_4_11所示均值重算；排名吻合。
3. 英语自然简洁与直译痕迹：is consistent with搭配自然；the error明确继承综合平均误差。
4. 夸大、绝对化、复杂词：保持设计目标相符和支持，未升级为证明机制。
5. 三篇范文对应语境：E1的post-fusion refinement与J3多尺度结果语境合适；本文数值独立。

### C04-L166

位置：`source-zh/chapters/chapter04.tex:166` ↔ `chapters/chapter04.tex:166`。

中文原文：

```tex
在实际应用中，除估计精度外，模型的计算效率与存储需求也是重要的评价指标\cite{ref77}。本文选取 MS-AgentNet、CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 五种模型，从 FLOPs、训练时间、可训练参数量和权重存储占用四个方面比较模型的资源开销。其中，FLOPs 通过 THOP 库的 \texttt{profile} 函数统计，并在补计注意力运算后换算为单次前向传播所需的浮点运算次数；训练时间通过 Python 的 \texttt{time} 模块以秒为单位记录，反映模型完成规定训练轮次所需的时长；可训练参数总数通过 PyTorch 统计；权重存储占用通过 Python 的 \texttt{os.path.getsize} 函数测量，并换算为 KB，表示保存模型权重所需的存储空间。所有指标均在相同实验环境下测量。
```

当前英文：

```tex
In practical applications, computational efficiency and storage requirements are important evaluation criteria alongside estimation accuracy\cite{ref77}. This study compares the resource overhead of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM using four metrics: FLOPs, training time, trainable parameter count, and weight storage size. FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass. Training time is recorded in seconds using Python's \texttt{time} module and represents the time needed to complete the specified number of training epochs. The total number of trainable parameters is counted using PyTorch. Weight storage size is measured using Python's \texttt{os.path.getsize} function and converted to KB, representing the space required to save the model weights. All metrics are measured in the same experimental environment.
```

中文回译：

在实际应用中，计算效率和存储需求与估计精度一样，是重要评价标准〔ref77〕。本研究使用 FLOPs、训练时间、可训练参数量和权重存储大小四个指标，比较 MS-AgentNet、CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 的资源开销。FLOPs 使用 THOP 库的 profile 函数计量，补入注意力运算，并换算为单次前向传播所需的浮点运算次数。训练时间使用 Python 的 time 模块按秒记录，代表完成指定训练轮次所需的时间。可训练参数总数使用 PyTorch 统计。权重存储大小使用 Python 的 os.path.getsize 函数测量并换算为 KB，表示保存模型权重所需空间。所有指标均在相同实验环境中测量。

1. 漏译、增译或原意：四指标、计量方法及环境完整。
2. 术语、数字、限定条件：THOP/profile、attention补计、PyTorch、time、os.path.getsize、KB逐项保留。
3. 英语自然简洁与直译痕迹：single forward pass、trainable parameter count、weight storage size搭配准确。
4. 夸大、绝对化、复杂词：没有把权重文件大小当运行内存，没有把训练时间当推理延迟。
5. 三篇范文对应语境：B1及J4原文对应计量语境；补计注意力是本文适配，E2资源词优先。

### C04-L168

位置：`source-zh/chapters/chapter04.tex:168` ↔ `chapters/chapter04.tex:168`。

中文原文：

```tex
为在相同输入数据和训练条件下比较不同模型结构的复杂度，五种模型统一采用 CS2\_36 的 HI1 和 HI2 作为输入，序列长度设为 5，训练轮次、学习率、批次大小和丢弃率分别设为 1000、0.01、128 和 0.1。在模型结构设置方面，MS-AgentNet、CNN-Transformer 和 Transformer 均采用 4 个注意力头；CNN-LSTM 和 LSTM 均设置为 4 层，使 LSTM 层数与注意力头数在数值上保持一致。各模型的表示维度或隐藏维度均设为 16。相应配置及复杂度比较结果见\cref{tab:4-12}。
```

当前英文：

```tex
To compare model complexity with the same input data and training conditions, all five models use HI1 and HI2 from CS2\_36 as inputs, with a sequence length of 5. The number of training epochs, learning rate, batch size, and dropout rate are set to 1000, 0.01, 128, and 0.1, respectively. MS-AgentNet, CNN-Transformer, and Transformer use 4 attention heads, while CNN-LSTM and LSTM use 4 LSTM layers, making the LSTM layer count numerically equal to the attention head count. The representation or hidden dimension is set to 16 for all models. The configurations and complexity results are given in \cref{tab:4-12}.
```

中文回译：

为在相同输入数据和训练条件下比较模型复杂度，五种模型均使用 CS2_36 的 HI1 和 HI2 作为输入，序列长度为 5。训练轮次、学习率、批次大小和丢弃率分别设为 1000、0.01、128 和 0.1。MS-AgentNet、CNN-Transformer 和 Transformer 使用 4 个注意力头，而 CNN-LSTM 和 LSTM 使用 4 层 LSTM，使 LSTM 层数在数值上等于注意力头数。所有模型的表示或隐藏维度均为 16。配置及复杂度结果见表〔tab:4-12〕。

1. 漏译、增译或原意：输入及全部统一条件完整；模型结构差异保留。
2. 术语、数字、限定条件：5、1000、0.01、128、0.1、4头/4层、16均准确。
3. 英语自然简洁与直译痕迹：numerically equal清楚；仅数值相同，并未宣称结构公平等价。
4. 夸大、绝对化、复杂词：未新增完全公平证明。
5. 三篇范文对应语境：B1相同条件比较功能可借；本文4层/4头设置独立。

### C04-L170

位置：`source-zh/chapters/chapter04.tex:170` ↔ `chapters/chapter04.tex:170`。

中文原文：

```tex
尽管 LSTM 在统一复杂度测试中以 44.568 s 取得最短训练时间，但其对复杂退化模式的刻画仍有局限，整体 SOH 估计精度相对较低。相比之下，MS-AgentNet 的 FLOPs、参数量和存储占用分别为 0.045760 M、4,643 和 27.44 KB，均为五种模型中的最低值。与 LSTM 相比，MS-AgentNet 的前向计算量降低 50.5\%；与 CNN-Transformer 相比，其参数量和存储占用分别降低 25.6\% 和 25.8\%；与 CNN-LSTM 相比，二者分别降低 70.8\% 和 59.8\%。这些结果表明，MS-AgentNet 在保持较高 SOH 估计精度的同时，具有更低的前向计算量、参数量和权重存储开销。
```

当前英文：

```tex
Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low. In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models. It reduces forward-pass computation by 50.5\% compared with LSTM. Its parameter count and storage size are reduced by 25.6\% and 25.8\% compared with CNN-Transformer and by 70.8\% and 59.8\% compared with CNN-LSTM, respectively. These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.
```

中文回译：

虽然 LSTM 在统一复杂度测试中具有最短的 44.568 s 训练时间，但其对复杂退化模式的表征仍有限，总体 SOH 估计精度相对较低。相比之下，MS-AgentNet 的 FLOPs、参数量和存储大小分别为 0.045760 M、4,643 和 27.44 KB，都是五种模型中最低的。相比 LSTM，其前向计算量减少 50.5%。相比 CNN-Transformer，其参数量和存储大小分别减少 25.6% 和 25.8%；相比 CNN-LSTM，分别减少 70.8% 和 59.8%。这些结果表明，MS-AgentNet 以更低的前向计算量、参数量和权重存储开销保持较高 SOH 估计精度。

1. 漏译、增译或原意：LSTM训练最快的反例及MS-AgentNet三指标最低完整。
2. 术语、数字、限定条件：表_4_12和五项降幅重算一致。
3. 英语自然简洁与直译痕迹：parameter count与storage size准确；This model has FLOPs表述可读但可选use requires ... FLOPs，无须强改。
4. 夸大、绝对化、复杂词：无最快推理宣称；LSTM刻画局限为原稿结论。
5. 三篇范文对应语境：E2资源成本优先，B1指标功能吻合；未继承BMSFormer自身最短训练结果。

### C04-L172

位置：`source-zh/chapters/chapter04.tex:172` ↔ `chapters/chapter04.tex:172`。

中文原文：

```tex
为考察模型宽度变化下的存储开销，将五种模型的表示维度或隐藏维度分别设置为 16、32、64 和 128，其余设置保持不变。如\cref{fig:4-4}所示，五种模型的存储占用均随模型宽度增加而上升，但 MS-AgentNet 在四种测试宽度下始终保持最低值。当维度增至 128 时，其存储占用为 714.37 KB，较同一维度下最接近的 Transformer 降低 32.2\%。综合来看，MS-AgentNet 在 SOH 估计精度与计算、存储开销之间取得了较好的平衡，体现出面向资源受限 BMS 的轻量化应用潜力。
```

当前英文：

```tex
To examine storage overhead as model width changes, the representation or hidden dimension of each model is set to 16, 32, 64, and 128, with all other settings unchanged. As shown in \cref{fig:4-4}, storage size increases with model width for all five models, but MS-AgentNet maintains the lowest value at all four tested widths. At a dimension of 128, its storage size is 714.37 KB, 32.2\% lower than that of Transformer, the closest model, at the same dimension. Overall, MS-AgentNet achieves a good balance between SOH estimation accuracy and computational and storage overhead, showing its potential for lightweight applications in resource-limited BMS.
```

中文回译：

为考察模型宽度变化时的存储开销，将各模型的表示或隐藏维度设为 16、32、64 和 128，其他设置不变。如图〔fig:4-4〕所示，五种模型的存储大小均随模型宽度增长，但 MS-AgentNet 在全部四种测试宽度下保持最低值。当维度为 128 时，其存储大小为 714.37 KB，比同维度下最接近的模型 Transformer 的存储大小低 32.2%。总体上，MS-AgentNet 在 SOH 估计精度与计算及存储开销间取得良好平衡，显示了其在资源受限 BMS 中用于轻量化应用的潜力。

1. 漏译、增译或原意：四宽度、其余固定、714.37与32.2%、潜力完整。
2. 术语、数字、限定条件：四维度准确；714.37/32.2%只核中英一致，图中数值交主报告图审。
3. 英语自然简洁与直译痕迹：lower than that of为已批准修复，保留。
4. 夸大、绝对化、复杂词：potential明确尚非已完成部署。
5. 三篇范文对应语境：E2 lightweight/resource语境匹配；不继承其hardware-in-the-loop已完成结论。

### C05-L001

位置：`source-zh/chapters/chapter05.tex:1` ↔ `chapters/chapter05.tex:1`。

中文原文：

```tex
本文提出了一种面向资源受限电池管理系统的轻量化锂离子电池SOH估计框架，以缓解健康指标跨电池稳定性不足以及预测精度与计算效率难以兼顾的问题。研究从系统性健康指标构建和轻量化网络设计两个方面展开。所提出的多源健康指标提取与优化算法首先从充放电数据及其衍生曲线中构建多类候选健康指标，再基于特征开发电池集合的相关性结果，利用 MS-CCCT 对恒流充电电压窗口进行多尺度自适应标定，并通过 PCC/SCC 双阈值准入与冗余剔除确定模型输入。在保持特征定义与参数不变的条件下，最终入选指标在同一数据集的其他电池上仍与SOH保持较强的线性和单调关联。在序列建模方面，MS-AgentNet将ReLU²智能体注意力与小核和大核深度可分离卷积相结合，以协同表征局部退化变化、跨位置全局信息和长尺度退化趋势。在智能体数量固定时，RAA利用少量可学习静态智能体完成信息聚合与广播，将注意力相关性交互的理论复杂度由$O(N^2d)$降低至$O(Nn_a d)$。
```

当前英文：

```tex
This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-limited battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset. For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales. With a fixed number of agents, RAA uses a small number of static learnable agents for information aggregation and broadcasting, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.
```

中文回译：

本研究面向资源受限电池管理系统提出轻量化锂离子电池 SOH 估计框架，以应对健康指标跨电池稳定性有限和预测精度与计算效率难以兼顾的问题。研究侧重系统化健康指标构建和轻量化网络设计。所提出的多源健康指标提取与优化算法首先从充放电数据及其衍生曲线构建多类候选健康指标。依据特征开发电池集合上的相关性，MS-CCCT 随后在多个尺度自适应标定恒流充电电压窗口，再以 PCC/SCC 双阈值准入和冗余剔除确定模型输入。在特征定义和参数保持固定的条件下，所选健康指标在同一数据集的其他电池上仍与 SOH 保持较强的线性和单调关系。在序列建模中，MS-AgentNet 将 ReLU² 智能体注意力与小核及大核深度可分离卷积结合，共同表征局部退化变化、跨位置全局信息和较长时间尺度上的退化趋势。智能体数量固定时，RAA 用少量静态可学习智能体进行信息聚合和广播，将基于注意力的相关性交互理论复杂度从 $O(N^2d)$ 降为 $O(Nn_a d)$。

1. 漏译、增译或原意：框架动机、HI构建、固定定义参数、同数据集关联及模型组合完整。
2. 术语、数字、限定条件：n_a固定、O(N²d)→O(Nn_a d)正确，未误作无条件常数复杂度。
3. 英语自然简洁与直译痕迹：address不等于解决成功；longer time scales符合第3章模块语境。
4. 夸大、绝对化、复杂词：theoretical与fixed number of agents保留；未宣称所有条件运行最快。
5. 三篇范文对应语境：E2轻量化/复杂度和J3长短尺度词可借；PCC/SCC准入及静态智能体为本文适配。

### C05-L003

位置：`source-zh/chapters/chapter05.tex:3` ↔ `chapters/chapter05.tex:3`。

中文原文：

```tex
在Oxford、CALCE CS2、CALCE CX2和MIT/Severson四个公开电池数据集上的实验结果表明，与CNN-Transformer、CNN-LSTM、Transformer和LSTM四种基线模型相比，MS-AgentNet总体上取得了更优的综合表现。具体而言，在CALCE CX2数据集的两节电池平均结果中，MS-AgentNet的MAPE相比CNN-Transformer降低了52.69\%。此外，MS-AgentNet具有较低的参数量和存储开销，体现了其轻量化优势。消融实验与卷积尺度补充实验显示，多尺度深度可分离卷积与RAA的互补融合能够提升模型在不同退化场景下的综合表现。总体来看，所提框架在SOH估计精度与资源开销之间取得了良好平衡；模型在同一数据集的其他电池上仍保持了较好的估计性能，体现出一定的域内跨电池泛化能力，并具备应用于资源受限电池管理系统的潜力。
```

当前英文：

```tex
Experiments on four public battery datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, show that MS-AgentNet achieves better overall performance than the four baseline models, CNN-Transformer, CNN-LSTM, Transformer, and LSTM. Specifically, the average MAPE of MS-AgentNet over the two cells in the CALCE CX2 dataset is 52.69\% lower than that of CNN-Transformer. It also has a low parameter count and storage overhead, showing its lightweight advantages. Ablation studies and additional convolutional-scale experiments show that the complementary fusion of multi-scale depthwise separable convolutions and RAA improves overall performance under different degradation scenarios. Overall, the proposed framework achieves a good balance between SOH estimation accuracy and resource overhead. It maintains good estimation performance on other cells within the same dataset, showing a degree of in-domain cross-cell generalization and potential for application in resource-limited battery management systems.
```

中文回译：

在 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四个公开电池数据集上的实验表明，MS-AgentNet 的总体性能优于 CNN-Transformer、CNN-LSTM、Transformer 和 LSTM 四种基线模型。具体而言，MS-AgentNet 在 CALCE CX2 数据集两节电池上的平均 MAPE 比 CNN-Transformer 低 52.69%。它也具有较低参数量和存储开销，显示其轻量化优势。消融研究和补充卷积尺度实验表明，多尺度深度可分离卷积与 RAA 的互补融合改善了不同退化场景下的总体性能。总体上，所提框架在 SOH 估计精度与资源开销间取得良好平衡。它在同一数据集其他电池上保持良好估计性能，显示一定程度的域内跨电池泛化能力以及在资源受限电池管理系统中应用的潜力。

1. 漏译、增译或原意：四数据集四基线、代表降幅、消融和有限域内泛化及潜力完整。
2. 术语、数字、限定条件：CX2两池平均MAPE下降52.69099%≈52.69%，表_4_6重算成立。
3. 英语自然简洁与直译痕迹：平均MAPE比较句为此前已批准修复，不重复改写。
4. 夸大、绝对化、复杂词：a degree of、in-domain、potential全部保留，overall performance不等于每池每指标最优。
5. 三篇范文对应语境：E2精度与资源平衡及J2跨池generalization语境匹配；不照搬范文硬件实现。

### C05-L005

位置：`source-zh/chapters/chapter05.tex:5` ↔ `chapters/chapter05.tex:5`。

中文原文：

```tex
尽管取得了上述结果，所提框架仍依赖可辨识的充放电数据片段，且其跨数据集适应能力会受到数据域差异、源域选择和目标域数据量的影响。未来将重点研究面向不完整充电和动态运行片段的健康指标构建方法及轻量化域适应策略，并在更多电池体系、实际车辆运行数据和嵌入式硬件平台上开展验证，以进一步提升该框架的工程适用性与部署可靠性。
```

当前英文：

```tex
Despite these results, the framework still relies on identifiable charging and discharging data segments, and its cross-dataset adaptation performance is affected by domain differences, source-domain selection, and the amount of target-domain data. Future work will focus on HI construction for incomplete charging and dynamic operating segments, together with lightweight domain adaptation strategies. Further validation will cover more battery chemistries, real-vehicle operating data, and embedded hardware platforms to improve the framework's practical applicability and deployment reliability.
```

中文回译：

尽管获得这些结果，该框架仍依赖可辨识的充放电数据片段，其跨数据集适应性能受到域差异、源域选择和目标域数据量影响。未来工作将着重于不完整充电和动态运行片段的健康指标构建，以及轻量化域适应策略。进一步验证将涵盖更多电池化学体系、真实车辆运行数据和嵌入式硬件平台，以改善该框架的实际适用性及部署可靠性。

1. 漏译、增译或原意：依赖片段、三个适应影响因素及未来三类验证完整。
2. 术语、数字、限定条件：battery chemistries对应更多电池体系在化学体系语境合理；如作者原意还含封装/结构，宜再明确范围（A2）。
3. 英语自然简洁与直译痕迹：identifiable、real-vehicle及deployment reliability可理解，未堆不必要复杂词。
4. 夸大、绝对化、复杂词：未来will focus/validation will cover未改为已完成；limitations仍保留。
5. 三篇范文对应语境：E2的reliance on ... segments及扩大chemistries方向可借；本文不完整充电/嵌入式计划独立。

## 标题逐项回译

各标题的五项共同检查：①标题功能与范围保留；②SOH/HI、cross-cell、cross-dataset等准确区分；③自然名词短语，英语标题省略“分析/所提出”这类冗余形式不改变正文范围；④无新加夸大词；⑤Evaluation metrics、ablation、complexity等为B1/E1/J4相应功能，具体迁移与配置标题是本文适配。

- C04-H003：中文 `\subsection{评价指标}` → 当前英文 `\subsection{Evaluation metrics}` → 回译“评价指标”。五项检查均无实质问题。
- C04-H039：中文 `\subsection{健康指标筛选结果与有效性分析}` → 当前英文 `\subsection{HI selection results and effectiveness analysis}` → 回译“健康指标筛选结果与有效性分析”。五项检查均无实质问题。
- C04-H048：中文 `\subsection{模型训练鲁棒性与超参数分析}` → 当前英文 `\subsection{Training robustness and hyperparameter analysis}` → 回译“训练鲁棒性与超参数分析”。五项检查均无实质问题。
- C04-H052：中文 `\subsubsection{智能体矩阵初始化与收敛性分析}` → 当前英文 `\subsubsection{Agent matrix initialization and convergence analysis}` → 回译“智能体矩阵初始化与收敛分析”。五项检查均无实质问题。
- C04-H071：中文 `\subsubsection{超参数配置}` → 当前英文 `\subsubsection{Hyperparameter configuration}` → 回译“超参数配置”。五项检查均无实质问题。
- C04-H083：中文 `\subsection{SOH估计精度与跨电池泛化性能比较}` → 当前英文 `\subsection{Comparison of SOH estimation accuracy and cross-cell generalization}` → 回译“SOH估计精度与跨电池泛化比较”。五项检查均无实质问题。
- C04-H088：中文 `\subsubsection{Oxford数据集上的估计精度分析}` → 当前英文 `\subsubsection{Estimation accuracy on the Oxford dataset}` → 回译“Oxford数据集上的估计精度”。五项检查均无实质问题。
- C04-H101：中文 `\subsubsection{CALCE和MIT数据集上的跨电池泛化分析}` → 当前英文 `\subsubsection{Cross-cell generalization on the CALCE and MIT datasets}` → 回译“CALCE和MIT数据集上的跨电池泛化”。五项检查均无实质问题。
- C04-H115：中文 `\subsection{跨数据集迁移实验}` → 当前英文 `\subsection{Cross-dataset transfer experiments}` → 回译“跨数据集迁移实验”。五项检查均无实质问题。
- C04-H121：中文 `\subsubsection{不同迁移方向的性能比较}` → 当前英文 `\subsubsection{Performance across transfer directions}` → 回译“各迁移方向的性能”。五项检查均无实质问题。
- C04-H130：中文 `\subsubsection{目标域适配比例的影响}` → 当前英文 `\subsubsection{Effect of the target-domain adaptation ratio}` → 回译“目标域适应比例的影响”。五项检查均无实质问题。
- C04-H143：中文 `\subsection{模块消融与模型复杂度分析}` → 当前英文 `\subsection{Module ablation and model complexity analysis}` → 回译“模块消融与模型复杂度分析”。五项检查均无实质问题。
- C04-H147：中文 `\subsubsection{模块消融分析}` → 当前英文 `\subsubsection{Module ablation analysis}` → 回译“模块消融分析”。五项检查均无实质问题。
- C04-H164：中文 `\subsubsection{模型复杂度分析}` → 当前英文 `\subsubsection{Model complexity analysis}` → 回译“模型复杂度分析”。五项检查均无实质问题。

## 公式与保护内容

5个公式环境逐字比较通过（仅将读入行分隔统一为换行，不改命令）。公式内部没有新增翻译空间；以下同时是中文稿与英文稿的精确公式。

### C04-E1，起始行17

```tex
\begin{equation}
\label{eq:metric_mae}
\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}\left|y_i-\hat{y}_i\right|
\end{equation}
```

回译核对：绝对误差之和除以n。五项核对：①公式无漏增；②符号/上下标/运算顺序一致；③英语自然度不适用于纯公式，解释段另审；④未扩大数学条件；⑤本文公式，不借范文不同定义。

### C04-E2，起始行22

```tex
\begin{equation}
\label{eq:metric_mape}
\mathrm{MAPE}=\frac{1}{n}\sum_{i=1}^{n}\left|\frac{y_i-\hat{y}_i}{y_i}\right|
\end{equation}
```

回译核对：相对绝对误差之和除以n；式中不含乘100%，与本章0.00615另换算为0.615%的写法一致。五项核对：①公式无漏增；②符号/上下标/运算顺序一致；③英语自然度不适用于纯公式，解释段另审；④未扩大数学条件；⑤本文公式，不借范文不同定义。

### C04-E3，起始行27

```tex
\begin{equation}
\label{eq:metric_rmse}
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}\left(y_i-\hat{y}_i\right)^2}
\end{equation}
```

回译核对：平方误差的平均值再开平方。五项核对：①公式无漏增；②符号/上下标/运算顺序一致；③英语自然度不适用于纯公式，解释段另审；④未扩大数学条件；⑤本文公式，不借范文不同定义。

### C04-E4，起始行32

```tex
\begin{equation}
\label{eq:metric_r2}
R^2=1-\frac{\sum_{i=1}^{n}\left(y_i-\hat{y}_i\right)^2}{\sum_{i=1}^{n}\left(y_i-\bar{y}\right)^2}
\end{equation}
```

回译核对：1减去残差平方和与相对真实均值的总平方和之比。五项核对：①公式无漏增；②符号/上下标/运算顺序一致；③英语自然度不适用于纯公式，解释段另审；④未扩大数学条件；⑤本文公式，不借范文不同定义。

### C04-E5，起始行56

```tex
\begin{equation}
\label{eq:agent_initialization}
A_{ij}\sim\mathcal N\!\left(0,0.02^2\right)
\end{equation}
```

回译核对：A_ij服从均值0、方差0.02²的正态分布。五项核对：①公式无漏增；②符号/上下标/运算顺序一致；③英语自然度不适用于纯公式，解释段另审；④未扩大数学条件；⑤本文公式，不借范文不同定义。

结构保护核验：21行input/FloatBarrier逐行与英文对应位置一致。引用的表格及图文件路径没有替换。第5章没有独立公式环境；行内复杂度原式保持。

## 数字复算记录

- Oxford表_4_5：Cell2/3/5/6四指标最优，Cell4仅R²和RMSE最优；Cell7/8并非全最优，当前正文没有扩大范围。平均MAE四个降幅重算2.42086%、8.86957%、4.20475%、12.52087%，与正文四舍五入结果吻合。
- HI表_4_hi_input：HI1全部七池三误差最低；Fusion三项平均误差均第四；HI9/HI11在Cell7与Cell8的反转得到表中三误差支持。
- CALCE/MIT表_4_6：五池四指标最优，b3c13为例外；CX2_38两项MAPE相对降低约59.75%、51.80%；CX2两池平均MAPE相对CNN-Transformer降低52.6909948%，支持结论52.69%。第109行部分降幅精度另见S3。
- 初始化表_4_3_initialization与收敛表_4_3：全部区间、阈值轮次中位数及SD匹配。
- 迁移表_4_7/8：六方向适应后MAE/MAPE/RMSE均降低；Oxford四方向R²仍负；正文未删除不利结果。
- 适配表_4_9：两种源域三误差随所列四比例下降；CS2在50%时R²转正；CX2在70%仍负。MAE相邻差值0.0224、0.0221、0.0114、0.0055复算吻合。
- 消融表_4_10/11：模块及尺度变体映射正确；SFull四域最低，M4在MIT按打印精度与M1并列；正文如实保留CS2的M3 MAE更低。部分Reduction计算底数见S3。
- 复杂度表_4_12：五项相对下降复算50.5361%、25.6049%、25.7777%、70.8208%、59.8419%，按一位小数对应50.5%、25.6%、25.8%、70.8%、59.8%。LSTM训练最快事实完整保留。

未修改正文，因此未触发正文编译；本记录的完成不代表语言保证或重新验证全部原始实验。

## 两幅源图的独立交叉检查

完成本分工正文审查后，按主审追加分工，独立目视检查两张实际图片。此处是额外图像核查，不计入上文66个章节可见块。

- `figures/fig2.png`：子图(c)标题为CALCE CX2，图例却为CS2_36、CS2_37、CS2_38，与第2章CX2组电池编号不一致。可以确认标签冲突，不能只凭图片确定曲线实际来自哪组数据；更改图例前应核查绘图数据。
- `figures/fig3_3_attention_comparison.png`：子图(d)文字为Skim Local-Global Fusion Attention，与正文Slim不同。图中DSConv-L位于K/V支路下方、Q支路绕过卷积，输出处另有Linear块；正文则为DSConv-S先生成局部表示、再由该表示生成Q/K/V，RAA使用输出通道缩放，SLFA另有归一化局部分支参与加和。因此不是简单改一个模块字母即可确认图文一致，需要依正文实际结构逐项核实并重绘。当前审查不替作者决定结构。
- `source-zh/figures/figure_2_2.tex:4`与`source-zh/figures/figure_3_3.tex:4`已引用上述相同图片路径，故这些是中文源稿所引用图片与正文的既有一致性问题，不属于本轮英文翻译新增。

交付自检：47个自然段的中文和英文快照逐项确认都包含当前文件对应原行；47个回译及47组五项检查齐全。标题14项、公式5项，保护结构行21项。
