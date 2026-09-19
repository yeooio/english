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
