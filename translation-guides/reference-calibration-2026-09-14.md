# 范文尺度校准：哪些旧建议审得过细

日期：2026-09-14。本次执行作者的新要求：问题入库前，不仅看范文有没有更好的表达，还要看范文是否也采用相同概括、省略或说明粒度。主审与3个agent重新比对对应语境；不新增论文问题，不修改正文。

## 结论

**之前部分建议确实偏细，应降级或撤回。** 范文常把技术条件留在方法段、依靠表头说明统计量、用概括句连接结果，不要求每句都完全自足。本文已有足够上下文时，不应为了“更严谨”反复添加限定、展开公式或改写自然表达。

下面的处置优先于旧报告对应项目的修改优先级；旧报告仍保留为审查历史，不应再按旧分类将这些项目全部视为待改。此处是审查建议的重新分级，不是作者批准修改论文。

## 具体纠正了什么

|原审查项|范文是否也这样|重新判断|
|---|---|---|
|摘要直接写线性复杂度，未重复固定代理数/维度（ZIC-02）|Engineering-AI摘要full.txt 35–41直接写linear complexity，方法910–912再给固定代理数|保留。至多可选补“随序列长度”，不强迫摘要塞入推导条件|
|DSConv成本降低未列完整不等式（M05）|BMSFormer 839–848同样直接说计算减少并给成本比，没有补比值小于1的条件|可选，不列必改。本文实际5/31核不是k=1反例，不用未采用设置制造错误|
|五项HI对应三类性质（M01）|JESSOHRUL 1803–1811也先列四个HI，再概括三类作用，未逐项展开；但没有respectively，不能说句式完全相同|现英文保留。中文可按组理解，不再定为明确5对3语法错误；删“分别”也只是可选|
|模型驱动方法以电化学机制总括（ZIC-03）|BMSFormer 120–136几乎同样总括，再区分电化学模型与ECM|可选术语精确化，不称确定概念错误|
|消融表只有Average/Reduction，没有另写算式（R03）|JESSOHRUL Table13和附近消融段也如此，并通过正文比较说明降幅对象|表头无公式不是错误，短表注可选。本文真实计算口径可内部确认，不要求冗长说明|
|纯资源表称comprehensive performance／same configuration（R05）|BMSFormer Table6标题就是同类用法，列FLOPs、时间、参数与存储|默认保留，不因无准确率列强制改题|
|整体误差用于讨论晚期轨迹（R02）|Engineering-AI 1433–1451也在晚期轨迹讨论中引用整体RMSE；本文前段已有局部图观察|降为可选证据衔接，不强迫“改整体结论或新增尾段实验”二选一；仍不能把整体值称作尾段MAPE|
|精度与资源实验采用不同配置（R04）|BMSFormer分别规定精度比较和效率测试配置，最后综合讨论权衡|这是有范文对应的实验组织；不要求全部同配置，来源补充为可选|
|每个初始化指标前都加mean（SR02）|范文也依靠表注/协议交代平均，后文不逐项重复|本文表头mean±SD已清楚，加mean可选，不必四次重复|
|多体系泛化、长期/全局、相关性一致性等总括（X02、S-IC01、S-IC02）|三篇存在相同或近似概括，具体范围放在方法与实验说明|正常上下文保留，不自动推导成无限范围或相同斜率的强断言；不要求逐句加免责声明|
|CVT的shift、R3的进一步细化（N-M01、N-M04）|范文也常从曲线变化直接引出特征，并用repeat概括下一搜索阶段，但未确认有完全相同shift等同句|可选澄清，不把shift必然解读为刚性平移，也不因没有重述搜索域就判错|

以上是主要变化，完整旧编号比对、出处和差异见三个附录。范文有同类表达，只证明其表达尺度有参考价值，不替本文外部引文或实验结果作事实验证。

## 哪些仍值得问，但只问最少必要信息

这些项目不是因为本文比范文写得少，而是本文有具体对象尚无法确定：

- **迁移结果TR01**：指标是否分别跨运行平均？如果是，不能套单次R²/RMSE恒等式指控错误；如果同样本单次计算，才继续核对原始结果。不声称已检查三篇范文所有数值都满足恒等式。
- **消融集合SR01、重复统计SR03**：只确认消融是否沿用前述电池集合、mean/median跨哪些单位及多少次。范文有只写Dataset/average的消融表，不能要求每张表都重写一套长协议；本文数值似乎对应单池及明确跨运行统计，才需要这几问。
- **MIT候选N-M02、最终输入T-P01**：只确认未完整覆盖电压窗的处理，以及CS2最终HI1窗口。无需把每个未选候选的过程全部写入正文，也不强制恢复所有辅助表。
- **M06/M08/M09**：分别核对成本记号含义、去冗余加入时点和Oxford协议标注。范文也有相同记号或省略，不直接认定公式/算法错；确认含义后能关闭就关闭。
- **X01**：只确认隔离总括指开发集合外电池；原文在局部上下文可读，补明确指代可选，不认定泄漏。
- **S-IC01**：主实验N作为实际参数可核一次；global/long-range保留，不由成本测试短窗口推导主实验错误，不重报图中已有step:1。
- **架构图旧问题**：本次未重做三篇图像的一一对照，不新增或升级。先前已记录的本文图—公式不同仍是条件性版本核实，不宣称范文没有类似画法，也不据旧图判断代码错误。

这种“待核”不等于要求你写一大段解释，更不等于要重做实验。能由已有记录与上下文解释的，就保留原文或只补最短必要说明。

## 今后的入库规则

已将以下规则写入[项目审查要求](D:/MS-AgentNet-English/AGENTS.md)：

1. 先读三篇范文功能对应的完整语境，既找详细写法，也找相同省略；不能只挑更理想的一句。
2. 问“本文会不会因此被合理误解”，而不是“能不能写得更细”。
3. 范文也这样、本文上下文也清楚：默认保留或可选，不进入必要修改清单。
4. 有原意偏移、实际条件下的内部矛盾或明确不同计算对象：仍核实；范文同样存在不能免除核实。
5. 比对不充分，标为未确认，不当成已经成立的错误。每条留下“范文是否也如此—语境是否相同—为什么仍需改或无需改”。
6. 历史建议允许降级或撤回；当前校准结论优先，不按问题数量评价审查质量。

## 文件及证据边界

只更新项目审查要求并创建本次校准记录；中英文正文、公式、表格与图片前后哈希一致，未重新编译PDF。旧报告未删除。

本次读取三篇对应局部语境和表项，并区分直接同类、仅功能相似、尚未确认。没有从TXT双栏错序推断范文算法错误，没有声称三篇全部事实与数值都已验证。表格列归属不能确认时保留待核，不把“局部未见”说成“全文没有”。

---

## 附录1

# 范文反向校准：方法类旧审查项

日期：2026-09-14。只新增本文件，不修改论文及旧报告。本次不新增问题，而是回答：范文是否同样概括、同样省略，旧审查是否要求过细？

## 校准结论

此前若只找“范文更明确的句子”，不能据此要求本文处处扩写。本轮确实查到范文也有相同概括及同类未展开条件，应下调若干项目。尤其不应把数学上可以构造的边界反例，直接当作本文实际设置已有错误。

|旧编号|本轮范文实际做法及可定位证据|相似度与不同条件|新的处置|
|---|---|---|---|
|M01 五项HI对应三类属性|JESSOHRUL full.txt 1803–1811先列四个DTV指标，再笼统说这些HI反映产热、内阻变化和相变，没有逐项分组。|与本文现英文“提取这些指标以描述几类属性”相似；范文并未证明每项都须展开，但它没有respectively，故不是完全相同结构。中文“分别”亦可按幅值/位置/范围的自然分组理解，不必然是5对3错误。|现英文保留；不要求扩为两句。中文可保留，若要减轻对应暗示，仅可选删除“分别”，不必增加分组说明。撤回首轮“明确语言问题”的过强分类。|
|M02 FFN残差省略主语|Engineering-AI 822–826明确残差取第一阶段输出，但其对象有特殊选择，所以详细点明有实际功能。BMSFormer 735–751主要用流程概述加公式。|本文公式与英文The result已经明确；不能因范文一处详细，就判中文常见承接省略错误。|沿用已降级结论：中文可选澄清，英文保留，不列未解决错误。|
|M03 取最高最小相关→两池强相关|BMSFormer 447–459只陈述minimum baseline再选highest baseline。JESSOHRUL 1822–1834则在双相关均>0.8的准入条件后写“strong and robust relevance”。|范文同样把筛选和强相关相联系，但有实际阈值。本文后文也有高相关结果及准入阈值，不应脱离全文，把本句理解为对所有假想候选的定理。|降为可选作用范围澄清，不认定结果错误。只有作者明确声称得分函数无条件保证强相关，才需要收窄。可以在本段实际筛选语境保留现句，无需强塞0.2反例。|
|M04／X01 其他电池及开发/测试隔离|JESSOHRUL 1843–1849用同组多池设计，1875–1882再说设计阶段固定、测试不重新选择及数据互斥。Engineering-AI 338–342、377–400则明确training partition及固定时点。|范文也有概括性隔离陈述，但本文开发集Cell1/Cell2与报告集合含Cell2，是本稿具体集合关系；不能借范文通用措辞自动证明所有报告池独立。|保留为具体指代待确认，不上升为已发现泄漏。优先确认“其他”指开发集合外；确认即能关闭，不要求另造更复杂协议。|
|M05 DSConv低成本未列比值<1条件|BMSFormer 839–848写“a reduction is achieved”并给1/Nout+1/k²，没有逐句补<1；874–895的实际小核为1×3，819–823大核为1×31。|与本文同类概述高度相似；本文实际5/31核及多通道不是k=1反例。此前要求正文加完整不等式过细。|降为可选限定；不建议加入长不等式，不单列必须处理的错误。若要润色，限定“本文所用配置下”即可，但也非当前必改。M06的计量含义另核，不由此推断实测成本错。|
|M06 一维序列与二维成本记号|BMSFormer 784–789用k×k和NF×NF；832–833以及893–896在1×31/1×3扩展模块成本中仍写NF×NF、称feature map size。Engineering-AI 818–849则明确N×d到d×N转置。|范文确有几乎相同的记号混用/未展开适配；不能再说“范文不这样写”。但相同范例不能解释本文DF²到底代表N、二维面积还是背景示意。|保留为低优先级记号含义核对，不直接判为公式错误或代码错误。先确认DF²含义；若本来表示总位置数，定义即可；只有确实错误计数才改公式。撤回“必须全面一维重推”作为默认要求。|
|M07 非负相似度零分母条件|BMSFormer 891–947给一般相似度归一化，938–968给ReLU乘积商；本次所读局部未展开零分母处理。Engineering-AI 923–927则明确ReLU可出零，引入epsilon。|三篇并非统一要求逐个概述公式列零分支。本文一般线性例子ELU+1理论上为正，实际RAA另有均匀回退，不存在已确认的RAA未处理零行问题。|降为一般商式的可选数学说明；不要当实际算法缺陷，不补epsilon，不强制重复RAA已有说明。需要严格自足定义时才补“分母为正”，不是语言审校必改。|
|M08 去冗余each/otherwise加入时点|JESSOHRUL 1829–1834概述排序后去冗余；Table 5 TXT 1854–1867呈现循环与阈值，文本/伪代码条件表面并不完全一致。这里不据TXT错序断言范文算法错误。|范文自身也没有提供足以直接套用本文量词的可靠完整模板。本文表是可执行规则描述，any与每对otherwise若真按不同方式实现会改变集合，故不完全是风格问题。|保留为低负担的一次实现意图核实；确认任一高冗余即拒绝后可用any澄清。不能声称范文要求此措辞，也不需因此重做实验。|
|M09 Oxford CC/CC-CV表文|BMSFormer 461–470正文同样写constant-current and then constant-voltage；其Table 1 TXT 301–360中出现CC (2C)，但本轮没有PDF核对该跨栏表的列归属。|存在范文同类表文差异线索，不能宣布已确认范文同错，也不能用CC-CV正文替本文决定老化/表征阶段。|保留为协议标注待核；不称已证实错误。应先核验范文表格列与数据阶段，再决定是否只是CC阶段简称。此项没有得到“范文没有同问题”的结论。|
|M10 PCC仅敏感于线性|JESSOHRUL 1671–1680以“PCC measures the linear correlation”对照SCC单调关系，没有额外讨论PCC对非线性函数也可非零。|领域论文通常直接采用线性/单调的概括对比；本文上下文也非声称所有非线性必零。“only”可精确化但不需要长讲统计反例。|保留现意，删除only属可选小改；不列中文逻辑漏洞，不要求添加反例/证明。|
|ZIC-02 摘要/引言未重复固定条件|Engineering-AI摘要full.txt 35–41直接写linear complexity；方法910–912才明确agent count fixed to n=1。BMSFormer 858–864、970–985亦直接说线性/二次而不逐句展开固定维度。|与本文方法已经给定代理数、维度及随N阶数的情况相近。摘要省略推导条件是有范文依据的层级取舍。|改为保留；不强制把固定代理数、维度、比较对象全塞入摘要。若希望更自足，至多可选补“随序列长度”，不能将未重复条件算错误。|
|S-IC02 高相关→敏感性/一致性|JESSOHRUL 1835–1849由PCC/SCC>0.99写“consistently high performance”，并由多池相关筛选写common degradation characteristics；Engineering-AI 354–358亦宽泛使用high sensitivity，但后者不是单凭相关系数的同构证明。|“跨电池一致性”作为本段相关表现一致，确有近似范文惯例；并不自动声称两池同斜率、截距或正负方向。本文原句也未作这些强断言。|保留广义语境，不要求改为冗长统计定义；敏感性若作者另有量纲化定义才需相应证据。旧符号反转/极小斜率反例只防止扩大解读，不构成本文已错的依据。|

## 本轮核对边界

重新读取了三篇对应方法完整局部语境，而非只查关键词：Engineering-AI 332–426、810–933及完整摘要；BMSFormer 426–460、461–477、725–1008及完整摘要，另读表1 TXT 299–365；JESSOHRUL 1620–1695、1786–1910。相关段存在双栏提取穿插，本表仅依可独立连续阅读的短句，不将穿插行硬接成原段，不以公式提取碎片判范文算法错误。没有重渲染PDF；M09表格对应与M08伪代码因而保留核验边界。没有断言三个全文均不存在某个细节。

本文件校准的是“是否值得入问题清单”，不是给原论文贴完美标签。较合理的后续清单应把M04、M06、M08、M09保留为少量具体核实事项，其余多为保留或可选措辞；不能继续将这一组统称十二处论文错误。

---

## 附录2

# 结果类旧问题的范文反向校准（2026-09-14）

本报告只重新分级旧 R02–R08、SR01–SR03、TR01，不增加问题，不修改论文。检查目标不是找一句“更理想”的范文，而是检查范文是否也省略相同细节、是否采用相同概括方式，以及本文是否存在额外的实质歧义。以下“保留”指保留现有表述；“待核”是核实真实口径，不等于确认论文错误。

## 主要校准结论

以前把“没有写得最完整”当作“需要补充”的倾向应纠正。最明显的是：JESSOHRUL 也直接使用 Average/Reduction；BMSFormer 的纯资源表也称 comprehensive performance，并使用 same configuration；Engineering-AI 的微观消融也只列 Dataset 和 average results。不能再只引用范文其他地方的详细定义来要求本文一律写得更细。

|旧编号|范文实际相似做法、可定位依据|语境差异与此次裁定|
|---|---|---|
|R02 整体误差与寿命后期讨论|Engineering-AI/full.txt L1433–1451 在 accelerated aging trends 段直接用 CS2_38 整体 RMSE 0.0249 与两基线数值说明加速衰减轨迹的拟合；L1393–1409 也用局部放大图作定性观察。不是所有局部描述都另设区间指标。BMSFormer/full.txt L1307–1326 同段讨论突降跟踪与跨电池平均排名。|本文 L105 已明确 enlarged views 支持尾段轨迹观察，因此旧建议要求“只能改成整体或新增尾段指标”过于二选一。**降为可选衔接澄清**：如图确实支持，可保留尾段定性结论，把结论明确归于图表共同观察；无需为语言审查新增尾段实验。仍不能把 0.037673 称作尾段 MAPE。|
|R03 Average/Reduction 定义|JESSOHRUL/full.txt L3476–3534 完整消融说明及 L3536–3788 Table 13，直接列 MAE/RMSE/MAPE/Average/Reduction；本次所读消融段及表附近未另给 Average 运算公式或 Reduction 公式。L3518–3526 通过 Proposed 与 M1/M2/M3 的比较说明降幅对象。|**拆分分级**：表头没有公式本身降为可选表注，不是确定错误。本文正文 M2 vs M1 与表列 M4 vs 各行不必采用同一基准，分工不同可成立，不能称其本身逻辑冲突。实际 Average 如何计算、未舍入降幅是否一致仍可内部核实，但不自动要求写三句长表注。范文自身的数值未被本轮逐项重算，不能据范文格式证明本文算式或数值正确。|
|R04 精度和复杂度来自不同配置|BMSFormer/full.txt L1344–1394 明确先谈准确率，再单独规定效率测试配置；L1670–1697 将资源结果与精度权衡综合讨论，并不在资源表给出每一配置的准确率。Engineering-AI/full.txt L2440–2456 也综合精度和开销讨论权衡。|分别做精度与标准化开销实验是范文实际做法，不能要求所有实验必须同配置。本文已在 L79/L168 分开规定配置，**降为可选来源澄清**，不把原总结判为已证实的虚假同配置主张；如作者意在声称“资源表的精确配置取得前述全部精度”，才保留针对该解释的核实。学习率不同不使参数量/FLOPs结果无效。|
|R05 comprehensive performance / same configuration 表题|BMSFormer/full.txt L1764–1803 Table 6 标题就是 The comprehensive performance of models under the same and optimal configurations，指标只列 FLOPs/training time/parameters/storage；L1670 又写 almost same configuration。JESSOHRUL/full.txt L3799–3824 使用 identical training and architectural hyperparameters 后分别列 Transformer 4 heads 与 LSTM 4 layers。|**默认保留**。这属于范文功能对应的标题/比较约定，不是因为“没有准确率列”就必须改标题。本文正文已解释同输入、训练设置及数值对应，不声称异构结构数学等价。换成 resource costs 可以更精确，但只能作为个人偏好的可选命名，退出必要问题清单。|
|R06 Fusion 隐含比较基准|JESSOHRUL/full.txt L1946–1968 定义单输入及 Fusion，L1961–1969 将 Fusion 平均排名与单指标结果连接，未每一句重列比较基准；完整 HI 结果开头还跨栏延续至 L1874–1891。|本文前句明确 HI1 最好，后句进一步增益最自然承接 HI1，表中也给排名。**默认保留**；加 over HI1 alone 只是可选精确化。不能说论文已经断言所有融合方法无效。|
|R07 continuously improves 只试四档|本轮未定位三范文中与本文同协议的适配比例试验，不能声称范文对该实验也这么写。Engineering-AI/full.txt L1330–1378 的超参数敏感性讨论在列出搜索范围后用 consistent trends 概括观察，并非每句复述 tested 范围。|本文同一小节已经列10/30/50/70%，后续对这些比例作总结，**默认保留、可选加 tested**。不能只因未逐句复述范围就认定无限外推。该裁定依据本文上下文为主，范文只提供功能相近的概括粒度。|
|R08 comprehensive evaluation|JESSOHRUL/full.txt L1895–1914 实验章开头使用 comprehensively evaluate / thorough validation；Engineering-AI/full.txt L1141–1153 的结果章开头更有 holistic assessment 和 validates practical viability。|本文已用 evaluation 而不是保证所有情形成立，**保留现英文**。不机械继承范文更强的机制或实用性保证，也不要求再加 from the aspects considered here 使句子防御性变长。|
|SR01 消融评价电池集合|Engineering-AI/full.txt L2077–2090、L2153–2269 的微观消融按 Dataset 报 average results；L2356–2357 起 Table 12 也为 Avg. results。该局部没有每表列电池或细讲聚合。相反，其宏观表 L2097–2098 明写 NASA B0005；JESSOHRUL/full.txt L3536 起 Table13 用 Battery 和具体编号，L3518–3526 正文也逐电池说明。|“范文全部要求每表列电池”不成立。**缩小保留为待核**：本文若消融沿用既有评价集合，可不重复长协议；但旧检查发现 CS2/CX2/MIT 全模型值近于单节结果而非主比较两节平均，这构成具体识别疑问。只问实际对象是否变化，确认后必要时加一句/表头标电池，不强制展开先后聚合公式。|
|SR02 初始化指标值其实均值|JESSOHRUL/full.txt L1306–1313 全局说明五次运行后报告平均，后续结果段并不在每个指标前都重写 mean。BMSFormer/full.txt L1707–1709 以表注说明 Cell1 的十次平均，结果段直接讨论其指标。范文也依赖协议/表头提供均值身份。|本文表头 mean±SD 已清楚，当前范围自然可理解为三方案表中中心值。**降为可选**，不判确定语法错误；如采用，只在首次概括加 mean，不必三个指标及 performance 重复四次 mean。|
|SR03 初始化/收敛重复次数和统计单元|JESSOHRUL/full.txt L1306–1313 确实给 independent runs/random seeds/averaging；Engineering-AI/full.txt L1251–1330 的收敛段则给两个代表电池、单曲线阈值和末20轮SD，没有在这段报告重复次数。BMSFormer/full.txt L1707–1709 的十次只在 Cell1 表注，而非全稿每节重申。|范文并非每种收敛图都交代重复数，旧要求若泛化为所有段必须重复则过细。但本文明确报 mean±SD、median[range]、every training run，涉及跨运行层，和范文单轨迹描述不同。**保留最小待核**：这些统计跨什么、多少个单位；已写的最后20轮不要再次要求补。无需新增实验、显著性检验或复制范文五次。|
|TR01 R²/RMSE 隐含方差关系|BMSFormer/full.txt L1232–1305 把 ARMSE 表述为跨子集/划分平均，又把 m 解释为电池数，说明范文也可能存在统计层表述不完全精确，不能视作无歧义标准。JESSOHRUL/full.txt L1306–1313 的独立运行平均则说明汇总指标本就可能不服从单次恒等式。|**保留待核，不判错数**。本文问题基于同一测试电池、本文公式和两组具体显示数值的条件性冲突，不是要求比范文写得细。若确认为分别跨运行平均，则不能用单次恒等式指控错误；只需最小说明其均值身份。本轮未重算三范文全部 R²/RMSE，因此绝不声称范文数值完全满足该恒等式。|

## 相似省略不等于相同错误

本次确实找到相同写法和相同省略，但未把范文当作正确性豁免。应区分：

1. **可由相邻上下文消解的省略**：R05/R06/R07/R08/SR02 不应继续列为需要作者逐项确认的错误。
2. **建议可更清楚、但并不必需**：R02/R03 的表注部分/R04，默认保留原意和正常篇幅，不要求增加实验或冗长限制语。
3. **有本文具体证据触发的事实核实**：SR01 的评价集合可能变化、SR03 的跨运行统计、TR01 的指标层级。问最少必要信息，确认后再决定是否改文。

R03 过去引用 JESSOHRUL 的 FLOPs 定义只能说明某种指标定义方式，不能证明它对 Average/Reduction 也要求逐项定义。本报告用真正对应的消融表校正该不足。R02 过去只选范文局部图论证，也漏看了同篇直接把整体 RMSE 用在晚期轨迹讨论的实际做法，此次一并纠正。

## 读取边界

本次读取了当前英文第4章结果/消融/复杂度上下文、两张消融表、三轮结果报告；范文重点重新读取 Engineering-AI 结果的初始化、局部轨迹、完整微观消融及资源权衡上下文，JESSOHRUL 运行协议、HI比较、完整消融和复杂度小节，BMSFormer 评价指标、Oxford结果及效率配置/表格上下文。TXT双栏提取错序没有拼接作“完整连续原句”；以上引用采用可识别的内部连续段或表题/表头。未渲染PDF或重排跨栏逻辑，未声称完成三篇数值审计。报告只做旧问题分级，不新增范文问题清单。

---

## 附录3

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

---


