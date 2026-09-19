# 中文逻辑二次查漏：第2–3章（2026-09-14）

本轮只读复核中文及对应英文第2–3章、表2_1–2_6及筛选步骤表，然后对照上一轮methods报告。没有修改论文，没有检查训练代码或原始数据，不把复现细节缺失全部归为语法错误。新增4项：2项需作者核实的逻辑/适用范围，2项低优先级表意补充；同时收窄旧M02的定性。

## N-M01：曲线沿时间轴“偏移”不必然等于窗口时长改变

位置：[中文第2章L52](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:52)，[英文同段](D:/MS-AgentNet-English/chapters/chapter02.tex:52)。

中文改前：
> 随循环推进，CVT 曲线沿时间轴逐渐偏移，如\cref{fig:2-3}(a)所示。该偏移表现为固定电压区间内的充电时长随老化持续变化。

现英文：
> As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). This shift appears as a continuous change in charge duration within a fixed voltage interval as the battery ages.

问题：按紧接着的CCCT=t(V2)−t(V1)，若曲线仅作时间轴平移，即两端时刻都增加c，时长差不变。因此“偏移→时长改变”的指代连接不够精确。但“偏移”在中文中也可能泛指曲线形态改变，不能据此认定数据或HI定义错误。

条件建议（若图/提取记录确实显示窗口时长变化，保留两个观察而不把第二个说成纯平移结果）：
> 随循环推进，CVT曲线沿时间轴的位置发生变化，如\cref{fig:2-3}(a)所示；固定电压区间内的充电时长也随老化变化。

对应英文：
> As cycling progresses, the position of the CVT curve along the time axis changes, as shown in \cref{fig:2-3}(a); the charge duration within a fixed voltage interval also changes with aging.

效果：将未充分成立的等同关系改为并列观察。技术含义边界：不是单纯语法修复；需要作者确认两项观察及“持续”的实际含义，不擅自新增拉伸、斜率改变等机制。若原图只显示平移而无时长变化，不能采用此建议，需要回看提取数据。

范文依据：[JESSOHRUL表4，TXT L1637–1638](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1637)将特征直接定义为指定电压范围内的charge time。[BMSFormer TXT L440–459](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:440)也明确从电压片段提取时间序列。二者支持围绕“窗口内时长”描述，不证明本文图中变化；本问题的核心依据为本文自身差值公式。

## N-M02：统一15项候选与不同数据电压范围之间缺少适用规则

位置：[中文第2章L48](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:48)、[L90](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:90)、[MIT协议L37](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:37)；表2_2 HI13。

原句：
> ……形成包含15项候选健康指标的指标池……
> 本文进一步构造两个窗口放电容量候选指标，分别计算端电压由3.80 V降至3.40 V以及由3.20 V降至3.00 V过程中释放的电荷量，并记为HI13和HI14……

现英文对应：
> ...forming a pool of 15 candidate HIs...
> Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V.

内部疑点：MIT协议充电截止为3.6 V，不能按当前协议叙述完整经历3.8→3.4 V放电段。但集合积分公式仍可对实际记录落入[3.4,3.8]的部分积分，因此不能直接声称HI13在MIT上必为0、无法计算或已造成错误结果。真正缺口是：15项是否为统一定义清单；逐数据集是否排除不可完整提取的指标；还是允许按实际覆盖部分积分。现有最终MIT只选HI14/HI15不能反推前期如何处理HI13。

分支A（若确实先按完整可提取性排除）中文建议：
> 上述15项指标构成统一的候选定义清单；在每个数据集上，仅对能够按其完整定义提取的指标进行相关性筛选。

英文：
> The 15 indicators form a common list of candidate definitions. For each dataset, correlation-based selection is applied only to indicators that can be extracted according to their complete definitions.

分支B（若实际使用交集积分）中文建议：
> 窗口放电容量按实际放电记录中电压位于指定区间内的时间片段积分；当记录未覆盖完整区间时，其覆盖范围需单独说明。

英文：
> Discharge capacity within a voltage window is integrated over the recorded discharge segments whose voltages lie within the specified interval. The actual voltage coverage is reported separately when the record does not cover the full interval.

以上为条件方案，不能选择后直接写入。A补充了筛选准入，B澄清并要求报告实际定义范围，均涉及技术方法；不可静默把HI13改成3.6→3.4 V，也不可将异常项补0等处理当成既有事实。

范文对应：[Engineering-AI TXT L377–390](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:377)分数据集明确最终特征区间，L411–413说明预配置观察窗口依赖电池特征。支持明确适用范围，但范文没有规定本文对未覆盖窗口的处理。依据仍为本文MIT截止电压与HI13定义的交叉检查。

## N-M03：线性注意力矩阵商的逐行含义未显式说明（低优先级）

位置：[中文第3章L263](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:263)，前式linear_attention；现英文同位置。

中文改前：
> 其中，$\phi(\cdot)$表示非负特征映射，例如$\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$；$\mathbf 1$表示全1向量，用于计算对应的归一化项\cite{ref40}。

现英文：
> where $\phi(\cdot)$ is a nonnegative feature mapping, such as $\phi(\mathbf x)=\operatorname{ELU}(\mathbf x)+1$, and $\mathbf 1$ is an all-ones vector used to calculate the corresponding normalization term\cite{ref40}.

可选句末补充：
> 此处的除法表示分子各行分别除以分母中对应的标量。
> Here, division means dividing each row of the numerator by the corresponding scalar in the denominator.

理由：按本节维度，分子N×dh、分母N×1，不是一般矩阵除法。逐行缩放是可理解的惯用写法，不能把原式判为运算错误。此项只澄清记号，不改变算法。分母为0的处理仍与旧M07合并，不能借此添加epsilon。

范文：本轮查看的三个对应片段没有直接支持该补充句的原文，不硬引。依据是本文维度。一般注意力先前逐位置定义已为读者提供理解线索，所以不是必须修改项。

## N-M04：R3在哪个区域搜索可更明确（低优先级，需核实）

位置：[中文第2章L139](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:139)。

中文改前：
> R2阶段在该区域内采用0.20 V窗宽和0.05 V步长继续搜索；R3阶段进一步采用0.10 V窗宽和0.05 V步长细化搜索。

现英文：
> Stage R2 searches this region using a window width of 0.20 V and a step size of 0.05 V. Stage R3 further refines the search using a window width of 0.10 V and a step size of 0.05 V.

若R3确实限于R2得分最高窗口，建议：
> R2阶段在该区域内采用0.20 V窗宽和0.05 V步长继续搜索；R3阶段在R2得分最高的窗口内采用0.10 V窗宽和0.05 V步长细化搜索。
> Stage R2 searches this region using a window width of 0.20 V and a step size of 0.05 V. Stage R3 refines the search within the highest-scoring R2 window using a window width of 0.10 V and a step size of 0.05 V.

原因：当前R1明确把获胜窗口传给下一阶段；R2→R3仅“进一步”可由粗到细上下文推知，但没有同样明确。若R3仍搜索R1优胜区域，则上述改法错误，应写实际范围。不得仅凭“多尺度”推定嵌套规则。

范文：[BMSFormer TXT L450–457](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:450)明确将优胜段作为下一步搜索区间，再重复搜索。只支持把继承关系写清；该范文0.2步长与枚举0.1起点并不一致，不继承数值。这不是已发现实现错误，也不另报“全局最优”问题。

## 旧项再次核定

- M01保留为中文对应关系不够明确；现英文不用respectively已经避免一一对应暗示。不得把英文原句判为错译，分组版属于更明确而非必须扩写。
- M02降级：旧报告“导致特征与自己相加”的标题过强。中文“经……后输入……并与……”通常可理解为处理结果继续作主语，不必然说X''+X''。保留“可补FFN输出以减轻省略歧义”的建议；英文The result与公式一致，继续不改。
- M03成立：候选最高不保证绝对强相关；须保留Oxford实际高分作为具体结果，不能否定结果。
- M04与主报告X01合并，不双计。
- M05、M06仍需共同核定。二维成本、序列维度、比值条件不是单一换词能修复；不新增推理更快的主张。
- M07成立于一般非负相似度商；ELU+1例子理论上严格正，不能说该例子也必然有零分母。
- M08保留量词/加入时点待核。仍未从结果表推断实际程序。
- M09保留为表—文协议待核，不断言Oxford真实协议究竟是哪一个。
- M10保持可选精确化；“PCC衡量线性”本身正确。

## 本轮排除的假警报

1. R3与R2相等时已被“否则保留R2”覆盖，不报漏掉等值分支。
2. R1上界与步长可能造成尾部未覆盖，不足以认定搜索错误；本稿没有承诺覆盖连续域全部窗口，不列新增问题。
3. na=2的等效交互矩阵秩≤2，不推出整个残差RAA低秩；现稿限定正确，不重报。
4. 小核卷积保长需要相应边界配置，但未查实现，不把省略padding细节当作中文逻辑错误。
5. 不因3.6<3.8就说MIT的HI13积分必然空集。范围交集、完整窗口过程与最终入选是三个不同问题，已在N-M02区分。

## 本轮重读参考范围

Engineering-AI TXT332–426、838–853；JESSOHRUL1576–1686、1786–1849；BMSFormer426–460、671–735。只引用局部可定位语句或表项，不从双栏错序抽取跨段逻辑；没有声称本轮渲染PDF或确认曲线图形。以上参考中文解释均为助手释义。正文与方法事实的最终确认仍以作者及实际记录为准。
