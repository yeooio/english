# 范文反向校准：概念总括、任务范围与特征协议

日期：2026-09-14。本文件只校准旧审查项，不新增问题、不修改论文。此次专门寻找范文中的同类概括、隐含条件及省略，而不是只找写得更细的范例。范文采用某写法，说明该颗粒度有参照；不证明其科学断言必然正确。没有核查本文训练代码、原始数据及引言ref19原文。

## 结论索引

|旧编号|本轮等级|处理|
|---|---|---|
|ZIC-03|降为可选术语精确化|有直接同类范文总括，不能称确定概念错误；原句可结合后文区分理解|
|ZIC-04|降为保留／可选收窄|有几乎相同的研究缺口表述；不要求为了防御而全改成some/may|
|X01（含M04）|降为可选指代澄清；隔离意图内部确认|当前开发集合及表注已给读者理解条件，不认定泄漏；需要确认的只是结尾隔离总括范围|
|X02|明确保留|三范文均采用多体系数据概括泛化，本文另有跨域实验及明确协议，无须在数据介绍首句塞入全部限定|
|S-IC01|拆分：global/long-range保留；真实主实验N仍作低成本参数核实|不因短窗口或未在摘要定义范围而要求删长程术语；步长1已在图中，撤销缺失判断|
|N-M01|降为可选衔接修饰，不作确定逻辑错误|shift未必意指刚性平移；纯平移反例不能证明作者表达错误|
|N-M02|保留技术适用规则待核|MIT截止3.6 V与HI13完整3.8→3.4 V描述是本文具体差异，范文同类简写不能消除|
|N-M04|降为保留／可选明确|粗到细上下文及下一阶段继承可合理读懂，范文亦用“repeat”省略阶段重述|
|T-P01|保留窄范围参数／证据链核实|最终CS2窗口可补最小一句；不强制全部辅助表入正文，不称结果不存在|

## 1. ZIC-03：模型类别总括

现英文：`Model-based approaches simulate the electrochemical mechanisms inside batteries using mathematical equations or equivalent circuits.`

本轮同类反证：BMSFormer [full.txt L120–136](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:120)先写“simulate the electrochemical principles ... using mathematical equations or circuit components”，随后分别解释电化学模型与ECM；JESSOHRUL [L60–71](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:60)也把model-driven approaches概括成模拟内部chemical reaction mechanisms。两者都不是先用最细分类再总括。Engineering-AI [L114–134](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:114)则更精确地区分electrochemical or electrical dynamics。

差异条件：本文后句已明确ECM以电阻、电容模拟充放电动态，没有把ECM写成显式求解全部反应机制。因此旧项不能仅凭上位概括定为错误。

改前→本轮推荐：保留。若作者希望术语更严格，才可把总括对象改为`the electrochemical or electrical dynamics of batteries`（电化学或电学动态）；这是可选概念精确化，不是“范文都不这样写所以必须改”。ref19是否直接支持另属引用核验，本轮未读，不能宣称已通过。

## 2. ZIC-04：传统机器学习的概括局限

现英文末句：`...traditional machine learning models struggle to achieve high performance because of their structural constraints.`前提已限定online monitoring和historical cycles中的nonlinear and fluctuating data。

同类范文：BMSFormer [L64–79](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:64)几乎同样写`traditional models struggle to provide high performance due to their structural constraints`。其traditional models包括KF、物理模型、ECM及ML，本文聚焦ML，类别不完全相同，但“传统模型—非线性历史数据—结构局限”的缺口功能相同。JESSOHRUL [L33–40](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:33)亦在摘要使用传统模型仍需performance improvements的总括；Engineering-AI [L91–107](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:91)用often及具体CNN/RNN局限展开，较克制。

新判断：不能将科研引言中的类别概括强解为“所有算法在所有数据上必然低性能”。前一轮把它升为优先范围问题偏严。默认保留，若作者认为该结论超出所引研究，才按证据收窄。无须机械添加some/may，也不强迫增加一段免责声明。范文的同类写法是语言颗粒度依据，不代替本文文献支持。

## 3. X01：其他电池与数据隔离

现英文在特征开发小节说`other cells within the same dataset`，结尾说`maintaining data separation between feature development and subsequent evaluation`。

同类与省略：BMSFormer [L447–457](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:447)明确按一个数据集的所有电池计算筛选基线，而[L284–293](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:284)仍把模型在other batteries上的评价称为generalization，并未每句重述特征筛选参与范围。JESSOHRUL [L1843–1849](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1843)也明确多池共同筛选，其作用解释并不等同独立留出验证。Engineering-AI [L338–342、377–400](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:338)对calibration/training范围及冻结作了更强的明确说明。

差异：本文比前两者多了“不参与筛选”和“数据隔离”的明确声明，因此只需确保其指代的是开发集合外电池；不能因范文未隔离就替本文取消隔离边界。本文已给两池开发集合，结果表又标注配置池，读者可以按局部语境理解other为集合外，故不认定内在冲突或泄漏。

新处理：可选把`other cells`一次写成`cells outside the feature-development set`，中文“特征开发集合之外的电池”。无需整段反复解释。只内部问一次“隔离是否仅指这些集合外电池”；若是，旧长篇候选不是必改；若作者坚持所有报告电池均未参加特征开发，才触发真正协议核实。

## 4. X02：多体系泛化概括

现英文：`...examine the generalization capability of the proposed method across different battery systems and operating conditions.`

三篇对应语境：Engineering-AI [L237–261](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:237)直接用`generalization capability ... across varying chemistries and operational profiles`引出三数据集；BMSFormer [L426–439](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:426)用不同材料／工况的多电池评价概括applicability，具体域内协议另在L284–293说明；JESSOHRUL [L1463–1469、1914–1944](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1463)也把分数据集选择输入的实验总括为generalization。

新处理：原句保留。本文是数据介绍总括，不是宣称同一个模型未经适应直接跨全部化学体系；第4章已分别定义域内与跨域。旧候选虽更细，却增加并非此句必须承载的限定，可退回备用，不列入待改清单。

## 5. S-IC01：长期／全局与输入范围

三范文同类写法：BMSFormer摘要[L31–36](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:31)直接用long-term/short-term，窗口与标签另在L275–283解释，没有在摘要限定“窗口内”。Engineering-AI [L818–840](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:818)将输入写为B×N×d并称capture long-range dependencies，其[L2467–2472](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:2467)甚至在延迟实验给自身N=4、基线N=5；这只能证明短窗口设置与整体long-range用语在同一范文共存，不能推断所有主实验也N=4。JESSOHRUL [L3809–3820](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:3809)复杂度试验用window size 5，整体亦有长短程框架表述。

新处理：`global`通常相对所给序列，`long-range`常表示架构相对局部连接的建模作用，不应要求每次说明真实历史跨度。撤回“因未在此处明确N就先收窄摘要long-range”的优先建议，保留术语。主实验真实N是可复现参数核实，若作者手边有设置表，补一次即可；不要扩成每种工况采样、padding、感受野的强制大段论证。流程图step:1已存在，不重报。只有确认实际实现与明确声称的跨度冲突时才升级，本轮没有这样的实现证据。

## 6. N-M01：CVT偏移与时长

范文：JESSOHRUL [L1684–1697](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1684)从曲线随时间变化直接引出两个固定电压窗的时长，没有严格剖析平移和形变；Engineering-AI [L325–328](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:325)并列写CC阶段缩短与平台移位。BMSFormer [L441–459](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:441)直接给时间窗口及筛选，没有同类shift等同句。此次未发现三者把“刚性平移”明说为窗内时长变化；也不能以没有同一句便判本文错。

旧数学反例只针对刚性平移。本文`shifts`在图形描述中未必指严格刚性平移，因此原文可理解为曲线位置与形态随老化变化。降为可选衔接更明确：保留第一句，第二句`The charge duration within a fixed voltage interval also changes continuously as the battery ages.`中文“固定电压区间内的充电时长也随老化持续变化”。保留逐渐／持续，不借语言校准改观察。若已有图和提取记录支持，作者可采用；本轮不重核图像，不说已证明图中只有平移。

## 7. N-M02：候选清单与MIT电压范围

范文有同类简写：JESSOHRUL [L1576–1584、1625–1647](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1576)先列统一十指标；[L1923–1944](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1923)才按数据集解释最终输入，不为每个未入选候选详列缺失处理。BMSFormer L269–279也总括共同充／放电窗口；Engineering-AI L377–389分数据集给最终区间。因此不能要求本文为每个未选HI写完整排除轨迹。

本文特有差异：已写MIT充电截止3.6 V，同时HI13文字按3.8→3.4 V完整过程定义。需要确认的只是候选定义是否按实际覆盖部分积分、还是不完整者不参与；不是所有候选实现细节。最终MIT选HI14/HI15不证明HI13处理错误，亦不反推出处理规则。

新处理：保留窄技术待核，不判语法错误、不补零、不改上限；确认后最多一句适用说明，若统一候选只是定义库且作者实际不对MIT提取HI13，原来的长分支方案可压缩。

## 8. N-M04：R3搜索域

同类省略：BMSFormer [L447–457](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:447)先说最高基线段成为下一阶段搜索域，再用`search procedures are repeated`概括2–4步，不逐步重复范围。Engineering-AI L373–400以多尺度宽度和相关性筛选概述，所读段落也没有展开每级嵌套算法。

本文R1已说优胜窗口成为下一阶段搜索域，R2再说this region，R3说further refines，读者合理理解为粗到细继承；欠一遍重述不是确定遗漏。默认保留。若实现确实R3搜索R1而非R2优胜区，才值得一次明确；不能为了形式对称反向猜实现。旧`within the highest-scoring R2 window`候选继续条件性备用，不自动入待改清单。

## 9. T-P01：最终窗口与辅助表

同类颗粒度：Engineering-AI [L377–389、417–422](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:377)明确各数据集最后特征区间并链接相关性表；JESSOHRUL [L1923–1944](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1923)以HI编号和方法小节指向各组输入，并非每组重写筛选全过程；BMSFormer L457–459直接报告最后时间区间。范文支持“最终输入可找到”而非“每张过程表必须入正文”。

新处理：CS2最终HI1窗口未在当前调用链中明确，仍值得确认辅助表最终性后补一句，或链接补充材料。其他数据集相关性图表也可用可访问补充材料支撑，不强迫恢复三张正文表，不要求所有非关键候选数字全部展示。旧项从泛化的“展示遗漏”收窄为最小参数／结论证据定位需求。未引用的文件不是论文已展示的证据，但也不是数据不存在。

## 审查边界

本轮是对应功能的局部完整段落、设置段、表项比对；TXT双栏片段仅引用可定位连续句，不据跨栏顺序推导逻辑。未宣称渲染PDF、逐句长度统计、通读三篇PDF或验证其科学正确性。对“范文有无省略”只报告本轮对应语境，绝不把局部未见写成全篇绝无。上述9个旧项目不再按9个错误计数。
