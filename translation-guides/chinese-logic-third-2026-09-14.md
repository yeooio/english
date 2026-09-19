# 全篇第三轮查漏：新增、历史未解决事项与纠偏

日期：2026-09-14。主审与3个agent分工交叉审查。仅创建新报告，不修改论文。

## 本轮结论

与前两轮及9月13日早期全文报告去重后，**真正新增2项需核实的问题**；另补充1个旧图文问题的定位，并纠正1处上一轮判断。不是又发现一批确定中文语法错误。不要将技术信息未交代、图文版本不一致与英文翻译错误混为一谈。

|类别|编号|结论|如何处理|
|---|---|---|---|
|新增，优先核实|TR01|迁移表部分R²/RMSE在固定样本、同次计算前提下不满足内部恒等关系|查原始指标与聚合方式，不反算一个替代数字写回|
|新增，展示遗漏|T-P01|CS2主实验HI1窗口及多数据集相关性证据位于未调用的辅助表|确认表为最终版本后补正文/补充材料引用，不称结果不存在|
|历史未解决，补定位|T-M01|架构图与公式不一致；补图3-1的Gate与SLFA层级疑点|选定最终技术版本后统一图文，不能迁就旧图改公式|
|纠正上一轮|S-IC01|流程图已标step:1，不能说全稿未交代步长|保留N和记录间隔待核，撤回过宽的步长缺失判断|
|历史保留|旧C6|SOH百分表示与MAE/RMSE数值口径可更清楚|按真实计算方式说明，不判已有数字相差100倍|

## 1．最需要先查的新增项：迁移表指标口径

本文自己的公式给出：

`RMSE²/(1−R²)=Σ(yᵢ−ȳ)²/n`。

在同一组真实测试样本上，若R²和RMSE由同一次预测计算，右侧应固定。主审独立复算了附录TR01的两个例子：

- CS2→CX2：source-only反推0.069955731，30%适配反推0.065458295。
- CS2→Oxford：10%适配反推0.003707546，70%适配反推0.003653149。

两组差异均不能仅用四位小数四舍五入解释，详细可能区间见附录。但**这还不能决定哪一列错了**：若分别跨运行平均，或实际评价样本/尺度有变化，须按真实统计方式解释。不能把可能解释当成已确认事实。

改前效果：读者只知道测试电池名称，不知道表值是否为重复运行均值，也不知道各设置是否使用相同评价样本。

条件改后效果：保留经核实的数值，明确“每次在哪些样本上计算，再跨哪些运行平均”；若确为同样本单次结果，先核指标导出与原始数组，再确定是否修改数字及引用结论。完整中英模板见TR01，未核实占位符不能入稿。

范文原因：BMSFormer明确区分RMSE与跨子集平均的ARMSE；JESSOHRUL明确交代重复运行与结果平均。这里只借鉴统计层级的说明方式，不借用其运行次数，更不让范文替本文数字背书。

## 2．另一项新增：有辅助结果，但读者目前看不到对应证据

当前正文引用链没有纳入table_2_3、table_2_4、table_2_5。它们分别包含各数据集窗口、入选HI及其他电池相关性。主文已报告CS2采用HI1，却只明确给出Oxford标定窗口；迁移实验另设的3.8–4.0 V不能自动充当主实验CS2窗口定义。

改前：“CALCE CS2数据集采用HI1和HI2。”

条件补充：“在主对比实验中，CALCE CS2的HI1采用MS-CCCT标定的3.80–4.00 V充电窗口。”

英文：“In the main comparison experiments, HI1 for CALCE CS2 uses the 3.80–4.00 V charging window calibrated by MS-CCCT.”

数值来自现有辅助表，**仍须确认该表是否为最终版本**。同时为多数据集相关性结论提供已确认、可访问的正文或补充表引用。不能未经批准恢复全部表格或改变结构。

范文原因：Engineering-AI在窗口固定后分别说明各数据集的具体特征区间。可参考这种写清实际使用参数的做法，不照搬其区间或机制解释。

## 3．历史问题不重复计数，错误判断必须撤回

### 架构图问题

本轮实际查看了流程图fig1.png、架构图01.png、卷积图02.png、注意力图fig3_3_attention_comparison.png及特征曲线fig3.png。9月13日已记录的DSConv-L位置、Linear框、残差层级、Skim拼写等仍存在，属于未解决事项，**不是本轮新发现**。

补充的定位是图3-1蓝色SLFA框后仍画Add、Gate、Dropout、W_a及局部旁路，而当前公式已将后几项包含在SLFA内。需要明确这究竟是内部展开还是外部串联，不据此认定代码重复运算。改后应让图中的模块边界与最终确认的公式一一对应；中英文正文若与最终实现一致，应保留。

### 上一轮S-IC01纠偏

流程图Step2明确标了“step:1”。因此撤回“全稿没有交代步长”的宽泛判断，改为“图示已给步长1，正文未显式写出；主实验N与记录间隔仍待核”。不要要求作者补一个其实已经出现的信息。

### 已由作者解释的图轴不再重复催问

更早报告已记录作者确认图3(a)实际为约千秒量级，并正在修改时间轴。本轮仍看到旧图片，但不再问“是否真是0.04秒”，也不擅自换成天、小时或填确切倍率。等待作者新版后核对标注即可。颜色条说明是另一个旧事项，不与时间确认混同。

## 范围、边界与文件保护

三个agent分别完整复核中英方法/协议/结果范围；主审复核新增证据、实际图像、引用链、历史记录，并独立计算TR01舍入边界。已重新读取三篇范文相关上下文，但没有把双栏TXT错序拼成新论证，未声称重做范文PDF解析。

本轮未读取实际训练实现、预测数组或所有原始绘图数据。因此TR01及技术版本问题仍需原始记录，继续文本审查不能代替它们。没有承诺零遗漏，也没有要求新增实验。

source-zh、chapters、tables、figures、backmatter逐文件前后哈希完全一致；正文、公式、表格和图片未改，未重新编译PDF。

历史报告：
[9月13日全文报告](D:/MS-AgentNet-English/translation-guides/whole-manuscript-review.md)；
[中文逻辑第一轮](D:/MS-AgentNet-English/translation-guides/chinese-logic-audit-2026-09-14.md)；
[中文逻辑第二轮](D:/MS-AgentNet-English/translation-guides/chinese-logic-second-2026-09-14.md)。

以下完整收录三个复核附录，包含原文、条件修改效果、原因、范文依据和保留项。

---

## 附录1

# 第三轮查漏：第4–5章、结果表及图注

日期：2026-09-14。仅审查，未修改论文、中文源稿、表图或实验数据。本轮重新读取中英文第4–5章、当前第4章实际调用的13个结果/配置表和3个图的TeX文件，并对照前两轮报告及9月13日whole-manuscript-review.md。没有查看曲线像素、原始预测数组、训练脚本或未舍入结果；图注检查不等于核实图中现象。

## 结论

本范围新增 **1项需要核实的数值/统计口径问题**，不新增普通语法错误。它不是已证明某个数值抄错，也不是可以靠润色解决的问题。前两轮的聚合定义、消融评价集合、初始化运行次数、配置与资源归属等问题仍保留，不重复计数。

## TR01｜同一目标电池的R²与RMSE隐含评价方差不一致，需核原始指标口径

### 改前及定位

协议原中文（第4章119行）：

> CALCE CS2、CALCE CX2 和 Oxford 分别视为三个数据域，其中 CS2\_36、CX2\_36 和 Oxford Cell1 用于源域训练或目标域适应，CS2\_38、CX2\_38 和 Oxford Cell3 仅用于目标域测试。

现英文相应句：

> CS2\_36, CX2\_36, and Oxford Cell1 are used for source-domain training or target-domain adaptation, while CS2\_38, CX2\_38, and Oxford Cell3 are used only for target-domain testing.

相关结果原中文（第4章135行）：

> 以 CS2 为源域时，MAE 由 0.0831 降至 0.0252，$R^2$ 由 -1.3934 提高至 0.7650，并在 50\% 适配比例下由负转正。

现英文：

> With CS2 as the source domain, MAE decreases from 0.0831 to 0.0252, while $R^2$ increases from -1.3934 to 0.7650 and becomes positive at an adaptation ratio of 50\%.

协议给出了固定测试电池，正文没有说明改变目标测试样本，也没有说明这些迁移指标是否分别跨多次运行取平均。需要核实以下关系，而不能默认其中任一解释。

### 本文公式直接给出的内部检查

按第4章MAE/RMSE/R²定义，对于同一组真实SOH样本，且R²、RMSE由同一组预测逐样本计算：

`RMSE² / (1 − R²) = Σ(yᵢ − ȳ)² / n`。

右侧只取决于真实评价样本，不取决于模型、源域或适配比例。因此，在真实样本及尺度完全一致、指标不是分别跨运行平均的条件下，该比值应固定。本轮只使用此代数恒等式，不调用外部理论或推测模型实现。

|结果位置|R²|RMSE|反推的评价SOH方差|考虑四位小数四舍五入后的可能范围|
|---|---:|---:|---:|---:|
|表4-7第9行，CS2→CX2，source-only|0.8421|0.1051|0.069955731|[0.069867062, 0.070044488]|
|表4-8第9行，同向30%适配|0.9566|0.0533|0.065458295|[0.065260357, 0.065656805]|
|表4-9第9行，CS2→Oxford，10%|−1.3934|0.0942|0.003707546|[0.003703534, 0.003711560]|
|表4-9第12行，同向70%|0.7650|0.0293|0.003653149|[0.003639917, 0.003666408]|

同一比较对的区间不重叠，不能仅以表格显示到四位小数解释。范围计算令R²和RMSE各自允许±0.00005，再取比值的极限；这只是显示舍入检查，不是统计置信区间。

尤其第一对差异较大，而第二对虽较小也超过这种显示舍入范围。另有几组细小差异，本报告不逐个夸大为独立错误，统一交同一指标导出核查。

### 必须保留的解释分支

1. **若表中是同一固定样本上的一次逐样本评价**：需回查预测文件、标签、指标计算及表格导出，至少有一处数值/口径不能同时符合当前定义。但现有文字不足以判断应该改R²还是RMSE，不能从一个数反算另一个数后直接替换。
2. **若R²与RMSE分别跨重复运行或不同划分取平均**：平均RMSE的平方不等于平均RMSE平方，上述单次恒等式不能直接用于两项均值；因此不应判为算错，应交代真实运行数、样本范围及聚合次序。尤其不能把初始化表的均值规则自动搬到迁移表。
3. **若适配后评价样本、缺失值掩码、归一化尺度或时间区间改变**：须写明真实范围；前后降幅对应的比较含义也需要重新核对，不能只改连接词便声称同样本改善。

### 条件式改后效果——不能现在给出替代数值

如果确认为重复运行均值，保留真实结果，在协议或表注补写以下模板（方括号必须据记录填写）：

中文建议：

> 迁移结果中的各项指标均先在每次运行的〔实际评价电池及循环区间〕上分别计算，再对〔实际次数与重复方式〕取算术平均。〔明确各设置是否使用相同评价样本；如不同，说明范围。〕

英文建议：

> For the transfer results, each metric is calculated on [confirmed evaluation cells and cycle ranges] for each run and then averaged over [confirmed number and type of runs]. [State whether the evaluation samples are identical across settings and specify any differences.]

如果确认为同样本单次计算：现在不改正文，先重算/核对后依据真实结果同步修改表与所有引用该数字的句子。**不建议把0.0293“修成”某个反算值，因为现阶段没有证据判断哪一列可靠。**

修改原因：让数值、评价对象和统计层级符合本文自己的定义；避免把跨运行均值当作单次指标，或把不同评价范围的变化全归因于适配。此项涉及实验报告，不能保证所有分支都“不改结论”；应先核实真实情况，再决定文字与数字是否需要变化。

### 本轮范文依据及其限度

- 本轮重新读取[BMSFormer评价指标上下文](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:1232)至约1305行。其1246–1249行将ARMSE说明为多个子集/划分上的RMSE平均。可参考的是区分“每组指标”和“跨组聚合”，不能把范文ARMSE擅自套作本文RMSE定义。
- 本轮重新读取[JESSOHRUL训练与重复运行上下文](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1271)至1325行。1308–1311行明确交代独立运行、随机种子及测试结果平均。只借鉴显式报告聚合方式，不继承五次，也不继承其保证统计显著性的强说法。
- 本轮重新读取[Engineering-AI配置与收敛上下文](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:1251)至1334行，1296–1315行明确训练/验证/固定部署的角色。可参考数据角色需要绑定到真实区间，不能据此替本文选择30/70划分。
- 三篇范文均不能证明本文哪一个数字正确。本项直接证据是本文公式和表4-7至4-9的内部关系。TXT存在跨栏提取错序，只采用可确认的内部连续说明，不把交错公式当作连续原句；本轮未做PDF重排。

## 重查后保留的内容，不为凑新增而改

- Oxford的四节电池四指标最优、Cell4的R²/RMSE最优，与表4-5对应；未把“总体第一”误判成“所有电池均第一”。
- CALCE/MIT六节中五节四指标最优，b3c13例外，与表4-6一致。
- CX2两节平均MAPE降低52.69%与结论对象对应；不混成CX2_38单节59.75%。
- 表4-9的30%行与表4-8对应行相同；MAE随四档比例下降、50%首次R²转正这些文字与显示值相符。TR01核的是统计口径，不在核实前宣布这些观察已推翻。
- M3↔S0、M4↔SFull数值对应；最低/并列最低及单尺度只改善部分数据集的限定保留。Average与Reduction定义仍是第一轮旧问题。
- 主复杂度表的最低FLOPs/参数/权重文件存储，以及LSTM最短训练时间，表文对应。没有声称MS-AgentNet训练最快或实测推理最快。
- 图4-2、4-3的TeX面板电池名覆盖正文所列集合；图4-4图注限定tested widths。未从TeX核验曲线形状、32.2%图形原始值或分布图统计，不能将其称为已核实。
- 不把主结果中配置电池的标注遗漏重新拆成第三轮新问题；两轮数据角色边界说明仍需作者确认。

## 覆盖和交付边界

此次新增1项核实请求，不是发现1处确定中文语法错误。只创建本报告。未运行训练、重算实际评价指标、渲染图或编译论文。若没有原始结果与统计定义，继续文本审查不能替代本项最终确认。

---

## 附录2

# 第三轮独立查漏：HI展示链、数值口径与跨域协议

日期：2026-09-14。只创建报告，未改中文、英文、图表或PDF。

本轮重读中英摘要、第1–2章、第4章（重点为跨域协议），核对第2章相关表格及实际input关系，并查看流程图fig1.png；随后对照前两轮报告和9月13日whole-manuscript-review.md去重。以下新增1项正文展示链待补。数值表示说明已在旧报告C6提出，仅复核保留，不算新增；另纠正前轮1处检查遗漏，并列1个不计入错误数的实现核验问题。未读取训练代码或原始数据；没有将缺少说明自动定性为实验错误。

## T-P01｜CS2最终HI1窗口及跨数据集相关性证据存在于辅助表，但未进入正文引用链

性质：可定位的展示/可复现说明缺口，不是“这些结果不存在”，也不是第二轮N-M02的MIT电压覆盖问题。

位置：[第2章HI1定义L58](D:/MS-AgentNet-English/chapters/chapter02.tex:58)、[Oxford窗口L141](D:/MS-AgentNet-English/chapters/chapter02.tex:141)、[第4章输入L85](D:/MS-AgentNet-English/chapters/chapter04.tex:85)、[引言贡献L44](D:/MS-AgentNet-English/chapters/chapter01.tex:44)。

中文原句：

> CCCT 的电压区间由 MS-CCCT 标定，具体方法见第~\ref{sec:ms-ccct}~节，标定所得充电时长特征记为 HI1。
> 根据第~2.3~节的筛选结果，Oxford 数据集采用 HI1，CALCE CS2 数据集采用 HI1 和 HI2，CALCE CX2 数据集采用 HI13，MIT/Severson 数据集采用 HI14 和 HI15。
> 统一的筛选规则为各数据集确定相应的健康指标组合，入选指标在同一数据集的其他电池上仍保持较强的线性和单调相关性。

现有英文：

> The CCCT voltage interval is calibrated by MS-CCCT, as described in Section~\ref{sec:ms-ccct}, and the resulting charge duration feature is denoted as HI1.
> Based on the selection results in Section~2.3, the inputs are HI1 for Oxford, HI1 and HI2 for CALCE CS2, HI13 for CALCE CX2, and HI14 and HI15 for MIT/Severson.
> The unified selection rules determine a corresponding health indicator combination for each dataset, and the selected indicators retain strong linear and monotonic correlations on other cells within the same dataset.

具体核对：

- 主文第2章只引入table_2_1、table_2_2、table_2_hi_screening_steps及table_2_6。全文input/label检索未找到table_2_3、table_2_4、table_2_5被纳入的路径。
- [辅助表2_3](D:/MS-AgentNet-English/tables/table_2_3.tex:10)已有CS2最终窗口3.80–4.00 V；正文只明确Oxford为3.55–3.75 V。跨域实验确有统一3.8–4.0 V，但它属于另设协议，不能让读者据此反推主实验的CS2 HI1一定同窗。
- [辅助表2_4](D:/MS-AgentNet-English/tables/table_2_4.tex:1)已有四组筛选结果，[辅助表2_5](D:/MS-AgentNet-English/tables/table_2_5.tex:1)已有各组其他电池的绝对PCC/SCC。当前被纳入的table_2_6只有Oxford各电池绝对PCC，没有其SCC及其他数据集的对应数字。
- 因此，贡献中的概括有工作区数据表可供支撑，但读者当前正文中的证据路径不完整。不能断言概括为假，也不应把未引用表称为论文中已展示的结果。

条件性最小修改效果（先确认辅助表仍是当前最终结果；原有输入列表与结论句保留）：

中文补充候选：

> 在主对比实验中，CALCE CS2 的 HI1 采用 MS-CCCT 标定的 3.80–4.00 V 充电窗口。

英文补充候选：

> In the main comparison experiments, HI1 for CALCE CS2 uses the 3.80–4.00 V charging window calibrated by MS-CCCT.

然后将已确认的筛选结果及其他电池相关性表纳入正文或明确引用的补充材料，并在贡献对应方法段建立引用。不建议未经作者确认直接恢复所有辅助表或改变章节结构。若作者选择只补文字，也需给出支撑“其他数据集仍有强线性/单调关联”的可访问证据位置。

原因：这是补“具体使用哪个窗口、结论对应哪份结果”的链条，不是把“根据”改成“因此”。原句在语法上可读，靠润色不能补足缺失参数。

范文依据（本轮重读）：[Engineering-AI full.txt L377–390](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:377)在确定窗口后逐数据集报告最后的特征区间，例如CALCE的“partial segment (3.4–3.8 V CCDA)”。可借鉴“固定规则后报告各组实际区间”的写法；不能套用其3.4–3.8 V、物理解释或CCDA特征。本文3.80–4.00 V来自本文辅助表，不来自范文。TXT片段跨栏次序不用于重建搜索步骤。

## 旧C6复核（不计新增）｜SOH百分表示与误差表比例表示之间可补一条数值口径说明

性质：低优先级、待核的单位/表示澄清，不判公式或误差数值错误。此项已见[9月13日全文报告C6](D:/MS-AgentNet-English/translation-guides/whole-manuscript-review.md:57)，本轮仅提供条件候选并澄清不必限制SOH为[0,1]，不得报告为第三轮新发现。

位置：[第2章SOH定义L3–9](D:/MS-AgentNet-English/chapters/chapter02.tex:3)、[第4章指标变量L35](D:/MS-AgentNet-English/chapters/chapter04.tex:35)、[Oxford结果L95](D:/MS-AgentNet-English/chapters/chapter04.tex:95)。

中文原句：

> 为统一后续实验中的计算口径，SOH 按容量保持率进行计算，即电池当前可用容量与额定容量之比……
> 其中，$y_i$ 和 $\hat{y}_i$ 分别表示第 $i$ 个样本的真实 SOH 和预测 SOH……

公式为SOH=C_current/C_rated×100%。现英文对应：

> To use a consistent definition in the following experiments, SOH is calculated as capacity retention, namely the ratio of the current available capacity to the rated capacity...
> where $y_i$ and $\hat{y}_i$ are the true and predicted SOH of the $i$th sample, respectively...

证据及边界：表4_5的平均MAE=0.00524、RMSE=0.00638，图1嵌入结果曲线纵坐标也为约0.8–1.0；这些与容量比数值表示一致。第4章明确MAPE=0.00615对应0.615%，这项转换正确。现在缺少的是说明MAE/RMSE中的SOH按0.9还是90计算。百分比定义本身常规且不必改；数学上100%=1，也不能据它声称结果相差100倍。SOH亦不应机械写成“被限制在[0,1]”，因为定义没有引入裁剪。

条件补充（只有核实计算记录确按容量比数值计算时，保留原句及公式，在指标定义后补）：

> 计算上述指标时，真实和预测 SOH 均以容量比的数值形式表示，例如90%记为0.90；MAPE在表中以比例形式报告。

> For these metrics, true and predicted SOH are expressed numerically as capacity ratios, with 90% represented as 0.90; MAPE is reported as a ratio in the tables.

改后效果：明确0.00524 MAE在这种口径下相当于0.524个百分点，而不是0.00524个百分点；不修改现有任何数字，不强制给MAPE公式再乘100%。如果实际另有目标标准化，需说明评估前如何还原，不能套用此句掩盖不同计算口径。

范文对应：本轮重读[Engineering-AI L271–282](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:271)、[BMSFormer L241–254](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:241)和[JESSOHRUL L1293–1303](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1293)，三者以容量比乘100%定义SOH。这支持保留百分定义，不证明本文误差采用何种内部数值尺度。建议的指标说明是本文定义与结果表达之间的澄清，无完全对应的范文原句，不硬称“范文要求这样改”。

## 对第二轮S-IC01的纠偏：步长并非全稿完全未交代

本轮实际查看[fig1.png](D:/MS-AgentNet-English/figures/fig1.png)，其Step2滑动窗口图清楚标注“step:1”。因此上一轮若概括为“主实验的窗口移动步长全稿缺失”，范围过宽，应改为：正文未明确写出，流程图已给出步长1；主实验N和相邻记录的实际循环间隔仍需核实。无需为了修补已存在的图信息再要求作者凭空增加步长设置。

若作者确认图示适用于全部主实验，可选将第2章第15行“采用滑动窗口划分……”明确为“采用步长为1的滑动窗口划分……”，英文“a sliding window with a step size of 1”。这只是把已有图信息写入正文，不是新方法。若图仅为示意则另核真实设置。N=5在复杂度测试中明确，不据此推广至所有实验；“长期”与有效输入范围的其余问题仍待核。

本轮重读[BMSFormer L275–292](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:275)的完整步骤语境，其滑窗说明“moving forward one step at a time”并配下一步标签，可参照图文对应方式，不继承其30%/70%协议。

## 不计为新增错误的核验事项：跨域预处理参数来源

第4章source-only已明确不使用目标域数据更新模型参数；两项跨域HI定义也统一，应保留。正文未另外说明是否做HI尺度预处理、若做则拟合在哪些数据上。这不是已知泄漏，更不能强制所有模型必须归一化。

如作者确认确有预处理，可在协议中补真实变换、拟合集合、目标域适应时是否重拟合；若原始HI直接输入，则说明无需此步骤即可。本轮不提供伪装成已确认实施的完整句子，也不猜min–max或z-score。

本轮重读[JESSOHRUL L1270–1283](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1270)，其明确数据在输入模型前进行min–max normalization。只能借鉴“有此操作就说明”的写法，不能把范文归一化方法移植到本文；该片段也没有给本文提供source-only预处理权限的证据。

## 核对后保留

- HI13/HI14放电容量积分使用电流绝对值，s→Ah的1/3600已明确；HI15是能量比，分子分母单位相同，转换因子可抵消，不新增“遗漏1/3600”的假问题。
- 跨域统一HI不是主实验逐数据集筛选HI，这是正文已明确的另设实验，不应强行统一回主实验特征组合。
- 目标域适应参考电池和目标域测试电池已经区分；30%是参考电池的前置数据，不说成只测试目标池后70%。
- 源域选择影响适应性能的描述并未声称仅由化学体系单一因素导致，不强添因果机制。
- 第一轮M09的Oxford CC/CC-CV对照疑点仍需数据协议核实；第二轮N-M02的MIT候选窗口适用规则仍待核，本轮不重复计数。

以上建议均为报告内条件提案，没有写回论文。

---

## 附录3

# 第三轮查漏：第3章数学、数据流与架构图

日期：2026-09-14。只新增本报告，不修改正文、公式或图片。

## 结论与覆盖

完整复读中英第3章以及前两轮methods、第二轮intro-cross报告，逐式核对维度、运算顺序、残差对象、非负归一化与复杂度。进一步直接查看正文实际引用的三张栅格图 `01.png`、`02.png`、`fig3_3_attention_comparison.png`，而非只读图注。提交前追加完整读取9月13日 `whole-manuscript-review.md`，完成更早历史记录去重。

**历史未闭环事项再确认：架构图与当前文字/公式的运算边界未充分对齐。** 9月13日报告C1/C2已记录图3-3、图3-2的核心冲突及Skim拼写，不能再次算作新发现。本轮在同一主题下补充图3-1的Gate/SLFA展开边界及图3-2通道标签位置，下分三个定位点，不计作多个独立算法错误。这不是中文翻译错误，也不能据此断言代码错误。未发现值得另外列为确定错误的全新公式问题。

## T-M01：架构图与当前公式版本／模块边界待对齐（历史C1/C2复核，并补图3-1定位）

### A．图3-2的DSConv模块边界

位置：[图源02.png](D:/MS-AgentNet-English/figures/02.png)、[现英文第3章L148](D:/MS-AgentNet-English/chapters/chapter03.tex:148)、[L174](D:/MS-AgentNet-English/chapters/chapter03.tex:174)，中文同位置。

中文改前：

> 最后，输出经逆转置恢复至原始排列，并与输入通过残差连接融合：

> DSConv-L置于SLFA之后，采用三倍通道扩展和$1\times31$深度卷积，从融合表示中提取较长时间尺度的退化特征。两层$1\times1$逐点卷积分别完成通道扩展与恢复，整体变换顺序与DSConv-S一致；其残差连接在MS-AgentNet Block层完成，如式\eqref{eq:block_dsconv_l}所示。

现英文：

> Finally, the output is transposed back to its original arrangement and combined with the input through a residual connection:

> DSConv-L follows SLFA and uses a channel expansion factor of three and a $1\times31$ depthwise convolution to extract degradation features over longer time scales from the fused representation. Two $1\times1$ pointwise convolutions expand and restore the channel dimension, respectively, following the same transformation order as DSConv-S. Its residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}.

图中改前：图(c)、(d)均在第二个 `1 × 1 PWConv` 后另列 `Linear`；图(d)标作 `DSConv-L` 且自身画了旁路与 `Add`。扩展后的 `2C_out channels`、`3C_out channels` 标签位于第一个PWConv下方，而正文是经过该PWConv后扩展。图上前后箭头均向上。

问题及原因：正文DSConv-S的第二PW后只有逆转置和相加，没有额外可学习Linear；DSConv-L明确将残差放在Block级。若图(d)只是把Block级连接一起画入模块示意，并不代表代码多加一次，但图题没有区分这两个层级。Linear也可能被作者用作无激活的线性瓶颈标记，不应直接断言实现多了一层。通道标签则易被读为输入已扩展。

条件改后效果（若当前正文与公式确为最终实现）：

- 图(c)改为 `Transpose → PW expansion → DW5 → ReLU → PW restoration → Inverse transpose → Add with X`；不再以独立算子框表示未定义的Linear。若Linear只是强调PW输出无激活，改作该PW的注释，不画作额外层。
- 图(d)明确模块只含三倍扩展、DW31、ReLU、通道恢复及对应转置；Block级的缩放与残差放在Block图，或虚线框并注释其属于Block级，不画成模块自身另有残差。
- `2d/3d` 或经作者确认的 `2C_out/3C_out` 标签移到首PW的输出连线上；维度记号与旧M06一并核定。

中文正文建议：上述原句保留，不为迁就旧图改成双残差。

英文正文建议：上述原句保留。若图(d)有意保留Block级旁路，可在图注增加条件说明：

> 图(d)中的旁路表示Block级残差连接，而非DSConv-L模块内部的另一条残差连接。

> The bypass in panel (d) denotes the Block-level residual connection, not an additional residual connection within DSConv-L.

此说明仅当作者确认图的意图且图中缩放/归一化边界亦能解释清楚时适用。不能只补注释而留下彼此矛盾的算子。

### B．图3-3(d)与SLFA定义

位置：[图源](D:/MS-AgentNet-English/figures/fig3_3_attention_comparison.png)、[中文第3章L271](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:271)、[英文同位置](D:/MS-AgentNet-English/chapters/chapter03.tex:271)，以及L106、L351、L367和slfa_fusion公式。

中文改前：

> 该模块采用局部分支与RAA分支的融合形式：DSConv-S首先提取局部表示，RAA随后以该表示为输入完成跨位置特征交互，两个分支的输出经加法融合。

现英文：

> The module fuses a local branch with an RAA branch: DSConv-S first extracts a local representation, and RAA then uses this representation to establish cross-position feature interactions. The outputs of the two branches are fused by addition.

正文另明确Q、K、V都由X_S构造，RAA末端采用输出通道缩放s_o，而SLFA输出为LN(X_S)+W_a Dropout(RAA(X_S))。

图中改前：图(d)下方模块标为 `DSConv-L`，位于K/V一侧，Q单独进入广播路径；RAA乘法输出之上另有 `Linear` 和 `Add`。图(d)标题与图注明确把它称为所提SLFA，但没有将当前局部LN分支、W_a和Dropout的融合层级表达清楚。

另有一处可直接确认的图内拼写问题：图(d)底部实际写为 `Skim Local-Global Fusion Attention`，正文术语为 `Slim Local-Global Fusion Attention`。改前→改后：`Skim` → `Slim`；中文名称和技术含义不变。这不是需要范文裁定的词汇偏好，直接依据本文已确认全称；与上述结构核实合并记录，不另计一个算法问题。

原因：这里不只是“S/L一个字母”。卷积位于全部QKV之前，还是只接K/V，是不同的数据流；RAA的输入残差与SLFA的局部分支相加也是不同层级。若图是抽象注意力内核图，可省略某些外层算子，但应标清其边界，不能用完整SLFA的标题让读者推断完整计算。

条件改后（若正文公式代表最终结构）：图(d)以X为起点，先画 `DSConv-S → X_S`，再分为 `LN(X_S)` 和 `RAA(X_S)` 两支；Q/K/V均源于X_S；RAA内输出标记 `Channel scaling s_o`，残差与X_S相加；RAA输出经Dropout及W_a，再与LN(X_S)相加。也可主图仅画两支、另用嵌入图展开RAA，避免把两次相加画成一个。

中文改后效果：**先提取局部表示，再从该表示进行全部QKV交互，最后按公式融合**。

英文图内核心候选标签：`DSConv-S`、`Channel scaling s_o`、`Local branch: LN(X_S)`、`RAA branch: W_a Dropout(RAA(X_S))`。

正文中英原句保留；此处应优先核实并更新图，而不是把正确对应公式的文字改成图中旧路径。若实际代码采用图中路径，则需作者明确选定技术版本；不是可直接批准的语言替换。

### C．图3-1的SLFA框与外部融合层级

位置：[图源01.png](D:/MS-AgentNet-English/figures/01.png)，第3章block_slfa、slfa_fusion公式。

中文改前：

> 输入$\mathbf X_l$经SLFA模块处理。SLFA利用DSConv-S提取局部特征，并通过ReLU$^2$智能体注意力（ReLU$^2$ Agent Attention，RAA）建立跨位置全局信息交互：

现英文：

> The input $\mathbf X_l$ is processed by SLFA, which uses DSConv-S to extract local features and ReLU$^2$ Agent Attention (RAA) to establish global information interactions across positions:

图中改前：图(a)蓝色 `SLFA` 框之后继续排列 `Add`、`Gate`、`Dropout`、`W_a`及加法结点，并有LayerNorm旁路。当前公式的SLFA自身已经包含局部LN旁路、Dropout和W_a，正文亦没有定义独立Gate算子。

原因：可能这些方框是在展开SLFA内部运算，而不是在完整SLFA之后再做一次；现图边界却容易让读者按串联重复理解。不能据此认定模型重复残差或确实使用了未说明门控。

条件改后效果：若此图意在展开SLFA内部，使用一个总外框注明 `SLFA`，将内部算子按slfa_fusion归属其中；若蓝框是完整SLFA，则外面不再重复画其内部融合。`Gate` 若只是W_a的示意，合并为同一缩放标签；若是另一算子，必须先核实定义和公式，不默认为已有设计。

中文/英文正文原句保留；可用中英图内说明“SLFA内部展开 / Expanded SLFA structure”明确层级，但须先确保内部节点确与当前公式对应。

## 范文依据及其限度

本轮重新读取 Engineering-AI TXT L815–853、L851–933，BMSFormer L671–826，JESSOHRUL L1658–1687。双栏穿插不拼作连续论证，只用可独立定位的短句。

- [Engineering-AI L845–849](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:845)将转置、卷积和外部残差明确写入同一公式；[L822–826](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:822)明确残差所取阶段输出。支持“图、公式、残差来源应相互对应”的写法，不支持把它的残差来源照抄给本文。
- [BMSFormer L735–769](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:735)按窗口、embedding、Block、输出交代架构，并给局部模块公式；只能借鉴模块边界与数据流说明，不证明本文图里的Gate或Linear存在。
- JESSOHRUL这次所读HI统计片段没有直接架构图依据，明确不引用它证明上述改图。

这些发现的直接证据是**本文实际图像与本文当前公式的交叉核对**，不是范文相似度。没有把范文的原图结构当作本文实现的正确答案。

## 旧项复核、未新增问题

- M02继续按第二轮降级为可选中文主语澄清；现英文The result无问题。
- M05/M06仍是原成本条件/一二维记号问题；本轮图3-2使其维度歧义更直观，但不再次计数。
- 一般非负归一化零分母是旧M07；RAA已给均匀回退，不能重复给RAA报错或擅加epsilon。
- 低秩上界限定于Phi_q Phi_k，未扩展到整个含残差模型；保留。
- RAA平方归一化正比例不变及权重比描述，与公式一致；不由该性质推断必然精度提高。
- “线性注意力以较低计算复杂度”承接上句固定d_h时关于N的复杂度，现上下文能理解为渐近阶比较。虽然不能推出任意短窗口实际运算更少，本轮不另列错误，不新增硬性N>d_h条件，也不以大O直接断言实际运行快慢。
- 正文DSConv-S明确ReLU，DSConv-L说同变换顺序，图中ReLU并无已查明冲突；不猜测应为GELU。
- 图中Gate、Linear只能标为未对齐/未定义，不推出实际代码参数遗漏或原结果无效。图3-1的箭头拥挤也不自动等于数据泄漏。

本轮没有核验训练实现，也没有修改、重新生成图片。三图可疑节点必须先由作者确定最终结构再统一图文。

---


