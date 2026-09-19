# 第4章模型对比实验深度拆解（2026-09-16）

## 1. 为什么上一版仍然不够

上一版虽然提出了“总体结果—好案例—差案例—应用含义”的结构，但没有回答三个关键问题：

1. 图中的哪一种现象对应哪一种模型能力；
2. 表中哪些电池是真正未见测试电池，哪些只是配置或验证电池；
3. MS-AgentNet的平均优势究竟来自所有电池普遍领先，还是主要由某个困难电池贡献。

本文件只审查模型对比实验，不讨论消融、复杂度和迁移。审查依据包括三篇范文的对比实验原文、本文图4-2/图4-3以及表4-5/表4-6。

## 2. 三篇范文的对比实验到底怎样写

### 2.1 BMSFormer：从误差形态进入困难区段

BMSFormer的Oxford段（PDF第9页，`full.txt:1309--1326`）不是先列平均值，而是逐层使用图和表：

| 原文推进 | 观察对象 | 实际回答的问题 |
|---|---|---|
| CNN-Transformer在Cell1上的IQR接近0 | 箱线图中心区域 | 该基线是否具有局部优点 |
| 箱线图须不对称且负向离群点较多 | 分布尾部 | 中心误差较好是否等于全周期稳定 |
| Cell2--Cell8出现相似现象 | 多电池箱线图 | 该分布问题是否只是单电池偶然现象 |
| BMSFormer误差更小、更集中 | 误差大小与离散程度 | 准确性和跨周期一致性 |
| Cell2和Cell6有突然下降 | SOH局部放大区段 | 哪些区段真正具有辨识力 |
| CNN-Transformer和BMSFormer都能跟踪 | 困难区段中的两种强模型 | 承认最接近基线的局部能力 |
| BMSFormer在Cell6突变处误差最小 | 具体电池、具体区段 | 所提方法的优势究竟出现在哪里 |
| 最后报告八电池平均降幅 | 表5 | 用汇总数字收束前面的观察 |

它写“好”并非只有 `outperforms`，而是分别写：

- `smaller`：误差幅度；
- `more concentrated`：误差离散程度；
- `track the true values`：轨迹跟踪；
- `in response to sudden changes in Cell6`：困难事件中的局部表现。

NASA/CALCE段（PDF第12--14页，`full.txt:1906--1920, 1991--2003`）进一步形成基线层级：

1. LSTM最弱；
2. CNN-LSTM部分补充局部特征，但仍有明显误差；
3. Transformer的误差曲线在局部变化处波动较大；
4. CNN-Transformer最接近BMSFormer，但在复杂变化下仍有差距；
5. B0018和CS2-38被选作严重波动案例，而不是随机挑一个最好数字。

BMSFormer的不足也必须看到。表中Cell1、Cell2、Cell3、Cell7、Cell8均存在某些指标由其他模型领先，但正文只充分讨论了基线的不足，没有系统报告自己的非最优结果。其Oxford段还有“其余六个电池”与括号排除电池编号不一致的问题。因此本文应学习它具体到图形和电池的写法，不能学习它对自身例外的省略。

### 2.2 JESSOHRUL：先定义泛化，再分别使用曲线、分布和局部图

JE的CS2段（PDF第15--17页，`full.txt:1970--1990, 2086--2106`）先界定实验对象：

- CS2-35前30\%用于训练，后70\%用于同电池验证；
- 已训练模型直接用于CS2-36、CS2-37和CS2-38；
- 因而同电池未见循环回答 `within-cell prediction accuracy`；
- 另外三节完全未参与训练的电池回答 `cross-cell generalization`。

随后它让图中不同部分承担不同功能：

| 图形证据 | JE的解释 | 不能混为一谈的含义 |
|---|---|---|
| 完整SOH曲线接近真实值 | closest fit | 长期退化轨迹拟合 |
| 箱线图靠近零轴 | error distribution closest to zero | 整体偏差大小 |
| 局部放大图跟踪短期波动 | capture short-term capacity fluctuations | 局部动态响应 |
| 三种证据在未见电池重复 | accuracy and generalization | 从单电池拟合扩展到跨电池复用 |

表格分析也不是重复所有数值，而是：平均优势 → CS2-35代表数字 → 其余电池是否维持趋势 → 最接近基线在哪里失效。具体而言，CNN-Transformer在CS2-35和CS2-36上被承认为 `relatively competitive`，随后用其在CS2-38上的MAPE恶化说明它对电池差异更敏感。

JE的Oxford段（PDF第19--20页，`full.txt:2841--2893`）又增加了两个维度：

- Transformer在训练电池上较好、在其他电池上明显下降，用来分析训练到测试的落差；
- LSTM预测曲线过度平滑，用来说明它能近似长期趋势但会漏掉短期容量增长。

JE也并非没有遗漏。其表10中，CNN-Transformer在Oxford Cell5上的MAE、RMSE和MAPE均优于所提模型，但正文仍使用近似“所有电池均最好”的措辞。它还把汇总误差指标称为“maximum estimation error”，并从离线误差直接上升到安全可靠运行，力度超过证据。因此本文必须比JE更完整地报告Cell7、Cell8等反例。

### 2.3 Engineering-AI：按退化形态分案例，但结构归因明显过强

Engineering-AI（PDF第13--14页，`full.txt:1363--1445`）采用另一种组织方法：不按数据集逐表叙述，而是按退化行为分组。

1. `Precision in linear decay`：Cell1、3、7、8用于讨论平滑线性衰减中的稳态误差与测量噪声；
2. `Responsiveness to instantaneous drops`：Cell2、6用于讨论突然下降和局部拐点；
3. `Capturing capacity regeneration`：NASA B0005用于讨论局部向上恢复峰；
4. `Tracking accelerated aging trends`：CALCE CS2-38用于讨论后期加速下降。

这种写法的优点是每个数字都对应一个电池退化问题。它甚至承认所提模型在CALCE细小瞬时下降上的响应弱于NASA案例，再把优势限定到整体加速退化轨迹。

但它大量使用 `is driven by`、`is attributed to`，把对比图直接解释成某个模块的确定作用；这些模块作用只有结合消融实验才能较有力地陈述。本文主对比段只能写 `is consistent with the design objective`，随后引用表4-10/4-11作为补充证据。

### 2.4 范文原文怎样从结果进入解释：逐例对应

本节不再只概括范文结构，而是把范文的原文短句、前后证据和本文对应位置并排说明。短引文后均给出完整定位，可回到PDF核对上下文。

#### 2.4.1 BMSFormer Oxford：先承认基线局部优点，再找分布缺陷

**范文原文短句：**

> `CNN-Transformer’s estimation error IQR is close to zero.`

> `the model’s estimation stability may be insufficient.`

位置：BMSFormer PDF第9页，`full.txt:1309--1314`。

这两句不能分开读。第一句不是在夸所提模型，而是承认CNN-Transformer的箱体中心接近零；下一句依据须线不对称和负向离群点，把判断从“中心误差较小”推进到“分布尾部仍不稳定”。它的实际逻辑是：

> 一个中心统计量看起来较好 → 检查分布两端 → 发现低值离群点较多 → 因而只谨慎地说稳定性“可能不足”。

对应到本文Cell4，不能只因为MS-AgentNet的RMSE最低就写整体最好。本文应同时写：其RMSE最低，说明较大偏差受到较好控制；但MAE和MAPE并非最低，且图中存在持续负偏差，所以全周期平均误差没有全面领先。

#### 2.4.2 BMSFormer Oxford：把优势限定到具体突变区段

**范文原文短句：**

> `smallest prediction errors in response to sudden changes in Cell6`

位置：BMSFormer PDF第9页，`full.txt:1318--1320`。

它没有写“BMSFormer更能处理所有复杂退化”，而是把优势限定为：Cell6、sudden changes、prediction errors三个同时成立的条件。前一句还承认CNN-Transformer与BMSFormer都能较准确地跟踪Cell2和Cell6。其完整推进是：

> 两个模型都能跟踪困难区段 → 再比较哪一个在Cell6突变处误差更小 → 最后才汇总八电池平均值。

本文Cell6应采用同样粒度：所有模型都跟随总体下降，但末段快速下降时误差扩大；MS-AgentNet的RMSE比次优CNN-Transformer低5.60\%，因此更适合写“减少快速变化区段中的较大跟踪偏差”，不能扩展成“对所有局部变化均具有明显优势”。

#### 2.4.3 BMSFormer NASA/CALCE：怎样解释“差模型”

BMSFormer在`full.txt:1994--2003`不是把四个基线合并为“均较差”，而是分别安排角色：

- LSTM：预测精度最低，作者把它联系到局部特征敏感性不足；
- CNN-LSTM：局部建模有所补充，但仍有结构限制；
- Transformer：B0005误差曲线波动更明显；
- CNN-Transformer：整体最接近BMSFormer，但单一小卷积核可能限制复杂模式识别。

范文这里的分析价值是“不同基线差在不同现象”，但因果用语偏强。本文不能在没有对应消融时直接写“Transformer由于缺少卷积所以Cell8更好或更差”。本文真正能观察到的是：

- Cell7中不同指标由CNN-Transformer和Transformer分别领先；
- Cell8中Transformer全面领先；
- CX2_38中各基线在后期持续高估SOH，而差距明显扩大。

因此本文应描述可见的失效形态，再用 `is consistent with` 与模块目标联系，而不是直接写唯一结构原因。

#### 2.4.4 JE CS2：怎样写“基线原本不错，到了困难电池才变差”

**范文原文短句：**

> `although the CNN-Transformer exhibits relatively competitive performance`

> `its prediction accuracy degrades significantly on CS2-38`

位置：JESSOHRUL PDF第16页，`full.txt:2097--2103`。

这组句子是JE对比实验中最值得本文学习的地方。它没有从平均排名直接断言CNN-Transformer差，而是先承认它在CS2-35和CS2-36上有竞争力，再指出CS2-38的MAPE扩大到0.0528，而所提模型为0.0301。于是“差”的含义变成：

> 普通电池上接近 → 困难电池上差距扩大 → 相对性能对电池差异更敏感。

本文更适合用同样方法比较Transformer：

- 在CS2_38上，Transformer与MS-AgentNet接近，三项误差差距只有1.23\%--2.74\%；
- 在b3c29上也近似持平，差距只有0.54\%--1.83\%；
- 到CX2_38的持续阶段转换和非线性尾段，差距扩大到MAE 23.15\%、MAPE 51.80\%、RMSE 20.59\%。

由此应得出的解释不是“Transformer整体较差”，而是：两者在相对平稳或较易拟合的测试电池上接近，MS-AgentNet的附加价值主要在持续改变的退化轨迹上显现。

#### 2.4.5 JE Oxford：怎样从曲线形态解释LSTM的不足

**范文原文短句：**

> `estimated SOH curves appear overly smooth`

位置：JESSOHRUL PDF第20页，`full.txt:2868--2872`。

JE随后解释：过度平滑的曲线能够近似总体SOH趋势，却不能识别短期容量增长。这里的关键不是“LSTM误差大”，而是：

> 曲线形态过度平滑 → 保留长期趋势 → 丢失短期变化 → 对应一种具体能力限制。

本文图4-3也必须按可见形态解释。CS2和MIT曲线含有孤立突降点，但所有模型主要跟随整体趋势，没有完整复现这些瞬时点。因此不能只挑MS-AgentNet的平均指标并写“能够捕捉短期容量波动”。更准确的说法是：模型能保持总体退化趋势，但现有结果不支持它已恢复每一个短时异常点。

#### 2.4.6 JE Oxford：怎样同时比较训练拟合与未见电池表现

JE在`full.txt:2883--2893`先指出Transformer在训练电池上与所提模型接近，再指出其在其他电池上明显下降；随后又承认LSTM的跨电池表现优于Transformer，但训练电池拟合更弱。它实际建立了二维比较：

| 模型 | 训练/配置电池拟合 | 未见电池表现 |
|---|---|---|
| Transformer | 较好 | 部分电池下降明显 |
| LSTM | 训练拟合较弱 | 相对更稳定 |
| 所提模型 | 训练拟合较好 | 跨电池下降较小 |

对应本文，Cell2、CS2_37、CX2_37和b3c13的结果只能说明配置阶段的表现；Cell3--Cell8、CS2_38、CX2_38和b3c29才能回答未见电池表现。不能用包含配置电池的平均值直接完成跨电池泛化论证。

#### 2.4.7 Engineering-AI：怎样按退化行为定义“问题”

**范文原文短句：**

> `the primary challenge involves minimizing steady-state error and jitter caused by measurement noise`

> `overall fitting precision regarding the accelerated decay trajectory is significantly better than the baselines`

位置：Engineering-AI PDF第13--14页，`full.txt:1363--1374, 1433--1445`。

第一句先为平滑线性退化定义评价目标：不是只看能否下降，而是看稳态误差和测量噪声造成的抖动。第二句则明确承认所提模型对CALCE细小瞬时下降的响应一般，但对整体加速下降轨迹的拟合更好。它实际区分了：

- 单个瞬时点能否响应；
- 持续退化轨迹能否跟踪。

这正对应本文图4-3：孤立容量突降没有被任何模型完整恢复，但CX2_38持续非线性尾段由MS-AgentNet跟踪得更好。因此本文的优势应定位为“持续阶段变化与后期下降趋势”，不能扩大成“瞬时变化响应均更强”。

### 2.5 范文原文与本文最终写法的一一对应

| 范文原文所做的解释 | 范文具体证据 | 本文对应证据 | 本文应写出的判断 |
|---|---|---|---|
| IQR接近零但尾部分布不对称 | BMSFormer Cell1箱线图 | Cell4 RMSE最好但MAE/MAPE非最好，误差长期偏负 | 较好控制大偏差，但平均绝对偏差并非最低 |
| 突然下降时误差最小 | BMSFormer Cell6局部变化 | 本文Cell6后段快速下降，RMSE改善5.60\% | 快速下降区段减少较大跟踪偏差 |
| 基线在普通电池有竞争力，在困难电池退化 | JE CNN-Transformer从CS2-35/36到CS2-38 | Transformer在CS2_38、b3c29接近，在CX2_38差距扩大 | 附加结构的主要收益集中在持续阶段变化与非线性尾段 |
| 曲线过度平滑，漏掉短期容量增长 | JE LSTM Oxford曲线 | 本文CS2/MIT孤立突降未被完整恢复 | 不宣称已经捕捉所有瞬态变化 |
| 区分训练电池与未见电池 | JE CS2实验设置 | 本文配置电池与测试电池混在平均值中 | 配置拟合与跨电池泛化分开报告 |
| 区分瞬时响应和整体加速下降拟合 | Engineering-AI CALCE解释 | 本文CX2_38后期持续下降、其他数据存在孤立突降 | 优势定位到持续趋势变化，不外推到每个瞬时点 |

这一对照表说明，范文的“解释”不是在数字后加一个模块名，而是先从图中识别一种误差形态，再说明这种形态对应哪个退化问题，最后才讨论模型结构可能提供的能力。

## 3. 本文实验对象必须先分清

当前两张对比表都把配置电池和未见测试电池放在同一张表中。

| 数据域 | 训练电池 | 配置/验证电池 | 真正未见测试电池 |
|---|---|---|---|
| Oxford | Cell1 | Cell2 | Cell3--Cell8 |
| CALCE CS2 | CS2_36 | CS2_37 | CS2_38 |
| CALCE CX2 | CX2_36 | CX2_37 | CX2_38 |
| MIT/Severson | b3c8 | b3c13 | b3c29 |

因此：

- 表4-5中Cell2--Cell8平均值可以称为“七节报告电池的平均表现”，但不能全部称为未见电池泛化；
- 表4-6的六电池平均值包含三个配置电池和三个真正测试电池；
- “五节电池四项指标均最优”是整体比较事实，却不能直接作为“五节未见电池均泛化最好”的证据；
- 跨电池泛化结论应重点建立在Cell3--Cell8、CS2_38、CX2_38和b3c29上。

重新仅对真正未见电池求平均后，MS-AgentNet仍保持最优，因此结论不会被推翻：

| 范围 | 模型 | 平均$R^2$ | 平均MAE | 平均MAPE | 平均RMSE |
|---|---|---:|---:|---:|---:|
| Oxford Cell3--Cell8 | MS-AgentNet | 0.982940 | 0.005387 | 0.006280 | 0.006265 |
|  | CNN-Transformer | 0.981873 | 0.005432 | 0.006335 | 0.006483 |
|  | Transformer | 0.981350 | 0.005523 | 0.006413 | 0.006553 |
| CS2_38、CX2_38、b3c29 | MS-AgentNet | 0.990567 | 0.008143 | 0.018539 | 0.012947 |
|  | CNN-Transformer | 0.987800 | 0.010037 | 0.037608 | 0.015900 |
|  | Transformer | 0.989133 | 0.009260 | 0.032190 | 0.014787 |

这些是本轮核查计算值，当前表格没有单列。若进入正文，需要作者确认是否补报测试电池平均值，或只用逐电池结果进行定性收束。

## 4. Oxford逐电池结果究竟说明什么

### 4.1 Cell3和Cell5：平滑退化中的整体领先

MS-AgentNet在Cell3和Cell5的四项指标均最优，说明它不仅在复杂变化电池上有效，在部分相对平滑的轨迹上也能保持较低误差。但不能据此概括“越平滑优势越大”，因为同样较平滑的Cell8由Transformer全面领先。

### 4.2 Cell4：较好控制大偏差，但平均绝对偏差不是最低

Cell4中：

- MS-AgentNet的$R^2=0.97052$和RMSE=0.00898为最优；
- CNN-Transformer的MAE=0.00819优于MS-AgentNet的0.00838；
- Transformer的MAPE=0.00966优于MS-AgentNet的0.00988。

MS-AgentNet的MAE和MAPE分别比对应最优值高2.32\%和2.28\%。由于RMSE更强调较大偏差，而MAE反映平均绝对偏差，这组结果可以谨慎解释为：MS-AgentNet较好地限制了较大的局部偏差，但没有在全周期平均绝对偏差上领先。图中其误差在较长区段偏负，也不适合写成“始终最接近真实值”。

### 4.3 Cell6：真正可用于分析快速下降的Oxford案例

Cell6后段出现快速下降，MS-AgentNet四项指标均最优。相对于各项最强基线：

- MAE降低1.12\%；
- MAPE降低1.87\%；
- RMSE降低5.60\%。

RMSE改善大于MAE/MAPE改善，适合写成“在后段快速变化中减少了较大的跟踪偏差”，不适合写成压倒性全面优势。图中所有模型在末段均出现负误差，MS-AgentNet是相对更接近，而不是完全消除了偏差。

### 4.4 Cell7：不同指标由不同基线领先

Cell7中：

- CNN-Transformer具有最高$R^2$和最低RMSE；
- Transformer具有最低MAE和MAPE；
- MS-AgentNet四项均不是第一。

MS-AgentNet的MAE和MAPE分别比Transformer高8.07\%和7.71\%，RMSE比CNN-Transformer高4.96\%。该结果说明模型排名取决于评价指标，也说明所提结构并不对每个电池都带来一致收益。

### 4.5 Cell8：最明确的非最优电池

Transformer在Cell8四项指标全部最优。MS-AgentNet相对Transformer：

- MAE高19.33\%；
- MAPE高18.04\%；
- RMSE高11.14\%；
- $R^2$低0.00109。

这是Oxford段必须报告的限制。由于Cell3、Cell5和Cell8都相对平滑，却出现不同排名，不能把Cell8结果简单归因于“轨迹平滑”。现有证据只能说具体电池差异仍会改变模型的相对表现。

### 4.6 Oxford真正能支持的总体结论

只计算Cell3--Cell8时，MS-AgentNet仍具有最优平均值，但相对CNN-Transformer：

- MAE仅降低0.83\%；
- MAPE仅降低0.87\%；
- RMSE降低3.37\%。

因此最准确的结论是：MS-AgentNet在Oxford未见电池上获得小幅但一致的平均优势，在Cell6快速下降区段控制较大误差的表现较好，但在Cell7和Cell8上没有保持领先。

## 5. CALCE和MIT结果究竟说明什么

### 5.1 CS2_38：小幅领先，不是主要优势来源

相对表现最接近的Transformer，MS-AgentNet在CS2_38上：

- MAE降低1.23\%；
- MAPE降低2.74\%；
- RMSE降低2.68\%。

这属于稳定的小幅改善。图中存在若干孤立的容量突降，所有模型主要跟踪整体退化趋势，未完整复现每一个瞬时尖峰。因此不能写MS-AgentNet已经解决短时异常变化识别。

### 5.2 CX2_38：整体平均优势的主要来源

CX2_38具有多次持续阶段转折和明显的非线性后期下降。其他模型在后期逐渐高估SOH，而MS-AgentNet更接近持续下降的真实轨迹。相对最强基线Transformer：

- MAE降低23.15\%；
- MAPE降低51.80\%；
- RMSE降低20.59\%。

因此，真正有技术解释价值的不是“MS-AgentNet在五节电池上最优”，而是：它的优势在退化斜率持续变化和非线性尾段中明显扩大。结合后续消融，才可以进一步说明该现象与多尺度局部建模和跨位置信息交互的互补作用一致。

### 5.3 b3c13：配置电池上的轻微落后

b3c13不是未见测试电池，而是模型配置电池。Transformer四项指标均略优于MS-AgentNet，但差距很小：MS-AgentNet的MAE、MAPE和RMSE分别高1.37\%、1.44\%和4.09\%。该结果可以说明整体比较并非每节都领先，但不能用作跨电池泛化失败案例。

### 5.4 b3c29：真正测试电池上与Transformer近似持平

b3c29中MS-AgentNet四项指标最优，但相对Transformer：

- MAE仅降低0.54\%；
- MAPE仅降低0.81\%；
- RMSE仅降低1.83\%。

因此该电池支持的是“至少保持竞争力和小幅领先”，不是显著性能提升。

### 5.5 三个真正测试电池的总体含义

对CS2_38、CX2_38和b3c29重新求平均后，MS-AgentNet仍在四项指标上最优。但差距主要由CX2_38贡献：CS2_38和b3c29均接近Transformer。应用分析应聚焦持续阶段转换和非线性尾段，不能把CX2_38上的大幅改善外推成所有电池上的统一大幅领先。

## 6. 可直接审定的Oxford改进案例

**中文：**

> Oxford结果表明，MS-AgentNet的相对优势随电池个体而变化。在用于模型配置的Cell2上，该模型的四项指标均为最优；在六节未见测试电池中，它在Cell3、Cell5和Cell6上取得全部四项最优结果，并在Cell4上取得最高$R^2$和最低RMSE。其中，Cell6后段快速下降时，MS-AgentNet的RMSE比次优CNN-Transformer低5.60\%，表明其在该变化区段减少了较大的跟踪偏差。不过，这种优势并未出现在所有电池上：在Cell4上，其MAE和MAPE分别比对应最优值高2.32\%和2.28\%；在Cell7上，Transformer取得最低MAE和MAPE，CNN-Transformer取得最高$R^2$和最低RMSE；在Cell8上，Transformer的四项指标均为最优，MS-AgentNet的MAE、MAPE和RMSE分别高19.33\%、18.04\%和11.14\%。仅对Cell3--Cell8计算时，MS-AgentNet的平均MAE、MAPE和RMSE仍为最低，但相对CNN-Transformer的降幅分别只有0.83\%、0.87\%和3.37\%。因此，Oxford实验支持的是MS-AgentNet在多节未见电池上的小幅平均优势，以及其在Cell6快速下降区段对较大偏差的较好控制，而不是对每节电池的统一领先。

**English:**

> The Oxford results show that the relative advantage of MS-AgentNet varies across cells. On Cell2, which is used for model configuration, it achieves the best values for all four metrics. Among the six unseen test cells, it also ranks first for all four metrics on Cell3, Cell5, and Cell6, and obtains the highest $R^2$ and the lowest RMSE on Cell4. During the rapid late-stage decline of Cell6, its RMSE is 5.60\% lower than that of the second-best CNN-Transformer, indicating fewer large tracking deviations in this changing region. This advantage, however, is not uniform across all cells. On Cell4, its MAE and MAPE are 2.32\% and 2.28\% higher than the respective best results. On Cell7, Transformer gives the lowest MAE and MAPE, whereas CNN-Transformer gives the highest $R^2$ and the lowest RMSE. On Cell8, Transformer performs best for all four metrics, and the MAE, MAPE, and RMSE of MS-AgentNet are 19.33\%, 18.04\%, and 11.14\% higher, respectively. When only Cell3--Cell8 are averaged, MS-AgentNet still has the lowest MAE, MAPE, and RMSE, but the reductions over CNN-Transformer are only 0.83\%, 0.87\%, and 3.37\%. The Oxford experiment therefore supports a small average advantage across multiple unseen cells and better control of large deviations during the rapid decline of Cell6, rather than uniform superiority on every cell.

## 7. 可直接审定的CALCE/MIT改进案例

**中文：**

> CALCE和MIT/Severson结果表明，三个未见测试电池上的平均优势主要由困难电池CX2_38贡献，而不是来自每节电池上的大幅领先。在CS2_38上，MS-AgentNet相对Transformer的MAE、MAPE和RMSE仅分别降低1.23\%、2.74\%和2.68\%；在b3c29上，相应降幅仅为0.54\%、0.81\%和1.83\%，两者均表现为小幅领先。相比之下，CX2_38经历多次持续的退化阶段转折，并在寿命后期形成非线性下降。其他模型在该阶段逐渐高估SOH，而MS-AgentNet更接近真实下降轨迹，使其MAE、MAPE和RMSE相对Transformer分别降低23.15\%、51.80\%和20.59\%。图中CS2和MIT电池还存在若干孤立的容量突降，所有模型的预测均主要跟随整体衰减趋势，未能完整复现这些瞬时变化。因此，现有结果更明确地支持MS-AgentNet对持续阶段转折和非线性退化尾段的建模能力，而不能说明其能够恢复每一个短时容量波动。

**English:**

> The CALCE and MIT/Severson results show that the average advantage across the three unseen test cells is driven mainly by the difficult CX2\_38 cell rather than by a large margin on every cell. On CS2\_38, MS-AgentNet reduces MAE, MAPE, and RMSE relative to Transformer by only 1.23\%, 2.74\%, and 2.68\%, respectively. On b3c29, the corresponding reductions are only 0.54\%, 0.81\%, and 1.83\%, representing small improvements. A different pattern is observed on CX2\_38, which undergoes several sustained degradation-stage transitions followed by a nonlinear late-life decline. The baseline models increasingly overestimate SOH in this region, whereas MS-AgentNet follows the declining trajectory more closely. Consequently, it reduces MAE, MAPE, and RMSE by 23.15\%, 51.80\%, and 20.59\%, respectively, relative to Transformer. The CS2 and MIT curves also contain several isolated capacity drops, and the predictions of all models mainly follow the overall degradation trend without fully reproducing these transient changes. The current results therefore provide clearer evidence for modeling sustained stage transitions and nonlinear degradation tails than for recovering every short-term capacity fluctuation.

## 8. 应用回归和模块作用怎样写才不空

“应用回归”不能写成通用句 `This is useful for practical BMS applications.`，而应由具体结果推出具体使用判断：

**中文：**

> 综合上述结果，MS-AgentNet的实际价值主要体现在退化模式发生持续变化时保持较稳定的趋势跟踪，而不是在所有电池或所有局部波动上始终取得最低误差。CX2_38上的明显改善与模型联合建模局部多尺度变化和跨位置信息的设计目标一致，表4-10和表4-11的消融结果还需用于判断两个模块的具体贡献。对于SOH监测，这种在后期非线性下降中的较小偏差有助于减少模型在退化加速后继续高估SOH的风险。Cell7和Cell8上的结果则表明，在模型用于新的单体电池前仍需评估电池差异；图中未被完整跟踪的孤立突降也不能被解释为模型已经解决了瞬时异常变化识别。

**English:**

> Taken together, these results indicate that the practical value of MS-AgentNet lies mainly in maintaining stable trend tracking when the degradation pattern changes persistently, rather than in producing the lowest error for every cell or every local fluctuation. Its marked improvement on CX2\_38 is consistent with the design objective of jointly modeling local variations at multiple scales and information across positions, while the ablation results in Tables~4-10 and 4-11 are needed to assess the specific contribution of the two modules. For SOH monitoring, the smaller errors during the nonlinear late-life decline help reduce the risk of continuing to overestimate SOH after degradation accelerates. The results on Cell7 and Cell8 also show that cell-specific performance should still be evaluated before the model is applied to a new cell, and the isolated drops that are not fully tracked in the figures should not be presented as a solved transient-anomaly recognition problem.

最后一句中的“减少高估SOH的风险”直接来自CX2_38图中基线在后期高于真实轨迹的现象，比泛泛的“适合实际应用”更具体；但它仍只是估计层面的风险，不应扩大为已经证明电池安全得到改善。

## 9. 对比实验后续统一检查项

每一段模型对比必须回答以下问题，而不是只满足句式模板：

1. 该电池是训练、配置还是未见测试电池？
2. 图中差异发生在完整生命周期、持续阶段变化还是孤立瞬时点？
3. 误差表现是系统性高估、系统性低估、过度平滑、相位滞后，还是少数大偏差？
4. 哪个基线最接近，在哪些指标或区段反而更好？
5. 平均改善是否由单个困难电池主导？
6. 模块解释是否有表4-10/4-11支持？如果没有，只能写与设计目标一致。
7. 应用含义是否指向明确决策，例如新电池使用前评估、后期高估风险或瞬态变化仍未解决？

这一尺度才是后续审改模型对比实验的最终基准。
