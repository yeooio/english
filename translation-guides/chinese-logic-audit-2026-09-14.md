# 全篇中文语法、论证逻辑与英文承接审查

日期：2026-09-14。本轮新建审查报告；没有修改中文源稿、英文论文、图表、公式或实验。这里的“改后”均指建议效果，不是已执行修改。

## 先说结论

确实发现了一些中文自身的问题，但没有证据支持“中文全文有大量明显语法错误”。本轮最重要的收获不是多换连接词，而是分清：主语/指代错误、公式适用条件、实验与比较范围、以及证据能支持到哪一步。已有英文消解的中文问题，明确保留，不再改一轮。

三名agent分别完整审查摘要/引言/结论、第2–3章及方法表注、第4章及结果表注；主审通读全部中英文正文，交叉核对两个跨章范围问题、核心公式与表格，并检查建议是否漏比较对象或擅改力度。按章节分工后再按语法、逻辑、技术证据交叉审查，而不是机械投票。范文仅作对应表达参照，不能证明本文技术内容。

## 分类汇总：23个审查条目，不是23处确定错误

|类别|数量|处理|
|---|---:|---|
|中文语言/对应关系问题|4|3项英文已修好；DTV分组在中文不清，英文未机械使用respectively，可选展开|
|已有技术限定的显式化|1|摘要/贡献补方法中已有固定条件，保留原比较对象|
|技术、定义、证据或协议范围需确认|12|不能用“润色不改原意”直接批准；先明确真实含义/数据口径|
|可选范围及表达精确化|5|原文有上下文时可理解，不作为硬错误|
|中文强度与英文已处理的保留提醒|1|不必再修改现英文|

M04与X01为同一问题，合并计1项；ZIC-02涉及摘要和贡献两处，按一个共性问题计1项。数字只是本轮分类，不是全文质量评分。

## 全部条目索引

|编号|类别|问题|建议处置|
|---|---|---|---|
|ZIC-01|语言关系|实时性不应与计算、存储一起写成受到限制|英文已修好，保留|
|M01|语言对应|5个DTV指标与3类属性未明确分组|中文建议分组；英文已避开respectively，展开仅为可读性|
|M02|语言主语|FFN残差相加的对象隐含|英文已按公式写The result，保留|
|R01|语言主语|增加的是适配比例，不是CS2/CX2源域|英文已修好，保留|
|ZIC-02|已有条件显式化|摘要及贡献的线性复杂度未自足说明固定维度及相对N|可补方法章已有条件；不新增模型设定|
|ZIC-03|技术/证据待确认|ECM与电化学模型是否都可总括为模拟电化学机制|核对意图与ref19后择词|
|ZIC-04|技术/证据待确认|传统ML整个类别因结构限制难以高性能的因果/范围|有证据保留；否则确认后收窄，may不是证据|
|M03|技术/证据待确认|取最小值后选最高分不自动保证绝对强相关|规则目标与实测结果分开|
|X01（并入M04）|技术/范围待确认|其他电池与数据隔离的参照集合|明确相对开发集合；不凭配置池被报告判泄漏|
|M05|技术/数学待确认|仅通道配置一致不足以推出DSConv成本比值<1|与M06共同确认适用条件|
|M06|技术/公式待确认|二维D_F²成本式与一维序列N未衔接|先确认维度与计数口径，不直接改公式|
|M07|技术/数学待确认|非负相似度不排除分母为零|补一般商式适用条件；不改RAA既有零行分支|
|M08|技术/算法待确认|each/otherwise不明确任何一项冗余即剔除与最终加入时点|作者/代码确认量词再写；冻结表原本就是英文|
|M09|技术/协议待确认|Oxford充电协议正文CC-CV、表CC(2C)|核实阶段与实际协议，不猜哪一方对|
|R02|技术/证据待确认|全程MAPE直接支持寿命后期局部低误差|全程指标与局部证据分开|
|R03|技术/定义待确认|Average与Reduction的公式、比较基准、舍入口径未定义|确认后加表注，不由显示数值臆造算法|
|R04|技术/证据待确认|主精度与资源测试配置不同，综合句易被读成同配置同时达到|保留两类结果，明确各自证据来源|
|M10|可选精确化|PCC仅对线性变化敏感的only过强|保留线性度量与SCC互补论点|
|R05|可选范围澄清|资源表标题same configuration/comprehensive performance过宽|说明是指定设置下资源指标，不改配置|
|R06|可选范围澄清|Fusion无进一步增益的比较对象隐含|明确相对HI1，不推广为多特征普遍无效|
|R07|可选范围澄清|持续改善应限于所测试比例|四档趋势保留，不外推任意数据量|
|X02|可选任务澄清|多体系数据覆盖与域内泛化/跨数据集迁移容易混读|按第4章分别训练与迁移的设置解释|
|R08|保留提醒|中文全面验证较强，英文已用evaluation|默认保留英文；改中文力度须确认|

## 四个直接可理解的改前—改后例子

### 例1：中文主语有误，英文已经处理正确

改前：

> CS2 和 CX2 源域从30%增至50%时，MAE分别降低……

中文建议：

> 在分别以CS2和CX2为源域的设置下，适配比例从30%增至50%时，MAE分别降低……

原因：增加的是适配比例，不是源域。本例以省略号示意后文数值不改；完整原句、英文及数字见附录R01。现英文已经以ratio为变化对象，应保留。没有直接同协议范文句，不能凑依据。

### 例2：五项指标不能直接用“分别”对三个属性

改前：

> 提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围。

中文建议：

> 提取上述五项指标。其中，HI5和HI7描述热响应的幅值，HI6和HI8描述特征位置，HI9描述波动范围。

原因：把5→3的分组补清。这里“上述”仅为展示缩略，完整候选保留所有名称、编号和引用，见附录M01。范文JESSOHRUL 1803–1811逐项连接特征实体与编号，支持明确对应，不能替本文证明HI9的物理机理。

### 例3：选得分最高者，不等于保证得分足够高

改前：

> ……使入选窗口在两节电池上均保持较强的相关性。

待确认建议：

> ……并以提高两节电池中的最低相关水平为窗口选择目标。

原因：若所有候选最低相关值只有0.2–0.3，选最高者也不能保证强相关。Oxford实测0.994447仍然支持该实例强相关，不否定它。BMSFormer 447–457写选择最低相关水平最高的区间，支持规则表达而非无条件效果。这是收窄论断，不是纯语法替换，见M03。

### 例4：全程指标与局部阶段证据不能混用

改前：

> ……MAPE为0.037673……表明模型在寿命后期加速衰减阶段仍能保持较低的预测误差。

若该值为全程指标，待确认建议：

> ……表明模型在该电池上的整体预测误差较低。

原因：全程平均不能单独确定尾段误差；原前段的局部图形跟踪讨论可保留。范文Engineering-AI在讨论局部响应时明确引用局部放大区域（1393行），本文也应让局部论断有局部证据。不能擅自把0.037673改称尾段MAPE。完整数值、比较模型及分支见R02。

## 如何决定哪些可改

1. 语言含义唯一：给最小修正；英文已正确则保留。
2. 限定在正文已有：可提议显式化，但不漏原比较对象或改变运算。
3. 原句结论超过已列证据：明确标注“收窄主张/需确认”，不能假称完全不改变原意。
4. 事实或实现不确定：给条件分支和需要核实的材料，不代作者选答案。加may或换therefore也不能弥补缺失证据。
5. 范文没有直接对应表达：坦白标注；有同类表达也要说明借鉴哪一层、不能借什么。

## 本轮覆盖与边界

完整通读：冻结中文及当前英文摘要、关键词、第1–5章。三个分报告分别列出各小节覆盖与保留点，关联表格和TeX图注均纳入对应检查；未调用的辅助表/图已注明，不算作PDF正文。文献综述核查了句内逻辑和所给范文参照，不声称已外部核验每一条被引论文。未重审栅格图中的所有文字，未运行或核验模型代码、训练日志和原始预测数据，未开展实际数据泄漏审计。

本轮按局部连续原文重读范文；TXT双栏错序没有当作真实句间推进。本报告没有重做范文逐句统计或宣称重排PDF，也不拿这些未做的工作充当证据。所有范文中文释义均为助手译释。

## 分报告（后附全文）

- [摘要、引言、结论](D:/MS-AgentNet-English/translation-guides/chinese-logic-audit-2026-09-14-intro-conclusion.md)
- [第2–3章与方法表注](D:/MS-AgentNet-English/translation-guides/chinese-logic-audit-2026-09-14-methods.md)
- [第4章与结果表注](D:/MS-AgentNet-English/translation-guides/chinese-logic-audit-2026-09-14-results.md)
- [跨章节范围](D:/MS-AgentNet-English/translation-guides/chinese-logic-audit-2026-09-14-cross-chapter.md)

附录为本轮详细证据及全部改前/建议改后。M04以跨章X01整段候选为准，不重复实施。


## 文件保护验证

本轮抽取保护目录source-zh、chapters、tables、figures、backmatter中的123个文件哈希，收尾与本轮读取后快照一致。只写入本轮审查文档；没有编译或改变既有PDF。不将上一轮编译与页面检查冒充本轮验证。

## 附录A：详细审查记录

### 中文语法与逻辑审查：摘要、引言和结论

日期：2026-09-14。独立分工审查；仅建议，不修改中文源稿或英文论文。

#### 结论与完整覆盖范围

逐段核对了 source-zh/chapters/abstract.tex 全部正文与关键词、chapter01.tex 第1—48行（背景、文献综述、挑战与贡献全部）、chapter05.tex 第1—5行（三段结论），并对应读取当前英文。另通读当前英文第2—4章，核对注意力复杂度、指标开发与跨电池协议、消融和资源指标的边界。

本范围并不存在“大量明显中文语法错误”的证据。可靠发现为：1项明确中文搭配问题（英文已修好）、1项摘要/引言的限定省略（正文方法和结论已写清，建议局部补齐），2项需作者确认的概念或论断范围问题。不将可读的长句、被动句或“因此”本身当成错误；没有为增加数量列出纯换词建议。

|编号|分类|位置|英文是否继承|处理|
|---|---|---|---|---|
|ZIC-01|明确语言问题|引言27行：实时性受到限制|否，当前英文已修好|仅记录中文最小修正，不重复改英文|
|ZIC-02|已知技术限定省略|摘要1行、引言46行：线性复杂度|是，简述也省略条件|建议补回方法已有的固定参数及序列长度限定|
|ZIC-03|需作者技术确认|引言9行：ECM是否模拟电化学机制|是|作者确认后调整总括句的概念层级|
|ZIC-04|需作者证据范围确认|引言11行：传统机器学习难以提供高性能|是|不因范文有类似写法就认可广泛结论；条件性收窄|

#### ZIC-01：并列对象不适用同一个“受到限制”

位置：[中文引言第27行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:27)；[英文同位置](D:/MS-AgentNet-English/chapters/chapter01.tex:27)。

中文改前：

> 因此，面向计算能力、存储空间和实时性受到限制的BMS，SOH估计模型需要在保持有效表征能力的同时控制模型规模与资源开销，进一步向紧凑化和高效化方向发展。

中文最小建议：

> 因此，面向计算能力和存储空间有限、实时性要求严格的BMS，SOH估计模型需要在保持有效表征能力的同时控制模型规模与资源开销，进一步向紧凑化和高效化方向发展。

现有英文（建议保留，不改）：

> Therefore, for BMS with limited computing power and storage space and strict real-time requirements, SOH estimation models need to control model size and resource overhead while retaining effective representational capability, moving toward more compact and efficient designs.

原因与效果：计算能力、存储空间是有限资源；实时性在此处表达的是必须满足的时限要求。原句用一个“受到限制”支配三项，第三项的含义不够准确。英文已经分别使用 limited 和 strict requirements，未照搬缺陷。本项不改变研究主张，也不需要新增事实。

范文依据：本轮重新读取 [BMSFormer全文第64—79、92—93行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:64)。其中写“performed in real-time”和“limited resource mobile devices”（分别意为实时执行、资源有限的移动设备），把实时执行要求与资源限制分开。它支持概念区分，不意味着本文完成了实时硬件实验。

#### ZIC-02：复杂度结论的自足性不足，不是公式推导已被证明错误

位置：[中文摘要第1行](D:/MS-AgentNet-English/source-zh/chapters/abstract.tex:1)、[中文引言第46行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:46)。

摘要中文改前（受影响整句）：

> 该网络主要集成局部—全局融合注意力模块，通过小核深度可分离卷积与ReLU²智能体注意力协同捕获局部退化特征与长程退化依赖，同时将传统Transformer的二次注意力复杂度降至线性。

摘要中文建议：

> 该网络主要集成局部—全局融合注意力模块，通过小核深度可分离卷积与ReLU²智能体注意力协同捕获局部退化特征与长程退化依赖，同时在智能体数量和特征维度固定时，将注意力相关性交互相对于序列长度的理论计算复杂度由传统Transformer标准自注意力的二次复杂度降至线性。

当前摘要英文：

> The network mainly integrates a local-global fusion attention module that combines small-kernel depthwise separable convolutions with ReLU² agent attention to capture local degradation features and long-range degradation dependencies, while reducing the quadratic attention complexity of traditional Transformers to linear complexity.

摘要英文建议：

> The network mainly integrates a local-global fusion attention module that combines small-kernel depthwise separable convolutions with ReLU² agent attention to capture local degradation features and long-range degradation dependencies, while reducing the theoretical computational complexity of attention-based correlation interactions from the quadratic complexity of standard Transformer attention to linear complexity in sequence length when the agent count and feature dimension are fixed.

引言中文改前：

> 所构建的注意力机制将计算复杂度由$O(N^2)$降低至$O(N)$。

引言中文建议：

> 在智能体数量和特征维度固定时，所构建的注意力机制将相关性交互的理论计算复杂度由$O(N^2)$降低至$O(N)$，其中$N$为序列长度。

当前引言英文：

> The attention mechanism reduces computational complexity from $O(N^2)$ to $O(N)$.

引言英文建议：

> With a fixed agent count and feature dimension, the attention mechanism reduces the theoretical computational complexity of correlation interactions from $O(N^2)$ to $O(N)$, where $N$ is the sequence length.

原因与效果：方法章已给出$O(Nn_a d)$，固定$n_a$与$d$后才能简记为关于$N$的$O(N)$。原简述在论文整体语境下可以理解，不应夸称公式错误；但摘要单独阅读时缺少条件，可能被理解为对所有模型维度或全部运行成本的无条件结论。补充是更精确而非更短，不能只以词数评价。原稿结论已写“在智能体数量固定时”及含$d$的完整量级，因此结论保留。本项仅展开正文已有理论限定，不改变模型或实验数据；仍由作者确认措辞。

范文依据：本轮重新读取 [Engineering-AI第146—153行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:146)及[第903—912行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:903)。它用“with the agent count fixed to”并给出$n=1$，将线性量级与智能体设置联系起来。本文采用$n_a=2$而非范文的1；不能继承其具体设置或硬件速度结论。本文的固定特征维度限定来自本文$O(Nn_a d)$的含义，不冒充范文逐字表述。

#### ZIC-03：总括句把两个模型类别放在过窄的“机制”对象下

位置：[中文引言第9行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:9)；[英文第9行](D:/MS-AgentNet-English/chapters/chapter01.tex:9)。

中文改前：

> 模型驱动方法通过数学方程或等效电路模拟电池内部的电化学机制\cite{ref19}。

当前英文：

> Model-based approaches simulate the electrochemical mechanisms inside batteries using mathematical equations or equivalent circuits\cite{ref19}.

待确认问题：作者是否要总括“电化学模型描述内部机制、等效电路模型描述电学动态”？本段后面本来就将ECM写为“以模拟电池充放电动态特性”，因此开头的总括对象可能过窄，不是中文句法不通。

若上述含义成立，中文最小建议：

> 模型驱动方法通过数学方程或等效电路描述电池的电化学或电学动态行为\cite{ref19}。

对应英文建议：

> Model-based approaches describe the electrochemical or electrical dynamics of batteries using mathematical equations or equivalent circuits\cite{ref19}.

若作者确指特定具有机制解释的ECM，则应保留相应限定并核对ref19，不应机械应用本建议。这里调整了概念覆盖范围，属于需作者确认的技术表述，不伪装成不涉及科学含义的润色。

范文依据：本轮重新读取 [Engineering-AI第114—134行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:114)。总括词为“electrochemical or electrical dynamics”；随后EM分项谈internal degradation mechanisms，ECM分项谈battery dynamics及电阻、电容。这是与本文同一分类功能的直接表达参照。但它不能代替核实本文ref19的实际内容；本轮不声称已对ref19作外部原文核验。

#### ZIC-04：宽泛结论即使源自范文，仍需核对适用范围

位置：[中文引言第11行](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:11)；[英文第11行](D:/MS-AgentNet-English/chapters/chapter01.tex:11)。

中文改前：

> 然而，当面对来自在线监测和历史循环的非线性、波动性数据时，传统机器学习模型因其结构限制而难以提供高性能。

当前英文：

> However, when handling nonlinear and fluctuating data from online monitoring and historical cycles, traditional machine learning models struggle to achieve high performance because of their structural constraints.

问题：中文前面列举多类机器学习模型并介绍在线容量估计实例，最后一句直接把整个类别归纳为“因结构限制难以高性能”，但没有说哪类结构、在哪种任务条件下及何种性能指标。“然而”的转折功能成立，问题不是应换成Therefore，而是转折后结论的范围与因果依据未交代。不能据此反向断言传统机器学习必然足够好。

条件性中文建议（作者确认确有部分模型受限、但不足以支持全类别结论时）：

> 然而，面对来自在线监测和历史循环的非线性、波动性数据，部分传统机器学习模型的估计性能仍可能受到模型结构的限制。

对应英文建议：

> However, when handling nonlinear and fluctuating data from online monitoring and historical cycles, the estimation performance of some traditional machine learning models may still be limited by their structure.

效果与科学主张：这会将“整个类别的确定性原因判断”收窄为“部分模型的条件性局限”，因此确实调整论断范围，不应未经作者确认写入。若作者有充分原始文献支持原范围，应补充可定位证据并保留；若连部分模型的结构限制也没有证据，则上述弱化版也不能当作已证明的事实，应继续核实，不能用may掩盖无依据。

范文依据与反例：本轮重新读取 [BMSFormer第64—79、92—93行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:64)。该文确有“traditional models struggle to provide high performance due to their structural constraints”，前面总括还包括物理模型、ECM及机器学习，而不单是机器学习。因此范文可以解释现稿写法的来源，却不能证明本文把该论断用于所有传统机器学习模型就成立。本项的建议是证据范围控制，没有“范文要求加some/may”的直接句式依据。

#### 已审但保留的逻辑关系与边界

- 摘要“然而—为此—首先—随后—此外—实验结果”：问题、应对、方法、补充模块、结果推进合理。模型与HI双线符合正文；不因出现多个连接词机械删改。
- 引言第1行的“尽管如此—因此”：优势转安全风险、风险转状态估计需求，关系可理解。安全机制具体引文正确性需另行文献核验；本轮不以推测判为错误。
- 引言第3行“容量测量需要完整循环—在线难满足—间接估计”：论证衔接成立；英文已明确难以满足的是测量要求。
- 引言第15—17行：CNN局部感受野、RNN串行限制、Transformer并行性的过渡有明确技术对象。“为解决这一问题”指紧邻的并行限制，不认定为声称Transformer专为SOH而发明。
- 引言第19—25行：微分噪声→平滑、时间特征无需微分→较易提取、多源信息增加不必然提高精度→需筛选，连接关系成立。第25行保留“可能”“帮助”，没有将相关性写成因果证据。
- 引言第27行除ZIC-01外：性能与资源权衡是并列考虑，不是参数少自动推出推理快。
- 引言第36—40行三项挑战：区分指标稳定性、局部与长期融合、运行资源限制；没有要求PCC/SCC说明所有非线性依赖。
- 引言第42—48行：贡献与三项挑战对应；第44行“同一数据集”限定及第48行将跨电池与跨数据集适应分开，应保留。第46行限定问题见ZIC-02。
- 结论第1行：指标定义与参数固定、同数据集其他电池、固定智能体数量及含$d$量级均已写出，不重复加免责声明。
- 结论第3行：52.69%明确指CX2两节电池平均MAPE与CNN-Transformer比较；总体综合表现不等于所有指标、每个电池均最优。保留“总体”“一定”“潜力”，不改成已部署或最短推理时延。
- 结论第3行消融支持模块联合表现，不写成证明唯一因果机制；现句未使用“证明”或排他机制解释，暂保留。
- 结论第5行：限制与未来工作对应，分别处理可用片段、跨域适应、实际数据及嵌入式验证；没有把未来工作写成已完成结果。

范文补充交叉检查：本轮还读取 [JESSOHRUL第1843—1849行](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1843)与[第1875—1882行](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1875)，其描述先组内选指标再固定使用。本文仍仅按自己的开发/配置电池角色和同数据集边界表述，不照搬其unseen battery groups范围。Engineering-AI第2810—2825行的性能、资源与未来限制也作了对照，但其实际硬件验证不能支持本文声称完成部署。TXT中相邻列错序片段不拼成新句，也不用于推导段落推进统计。本报告为逻辑审查，未新做全文范文句长统计，未声称完成外部引文事实审计。

#### 写入边界

只新增本审查文档。中文源稿、英文正文、图表、LaTeX命令、数字、公式和参考文献均未改动。上述技术确认项须先获作者答复，不能因为作者希望“找问题”便直接修成审查者猜测的意思。


## 附录B：详细审查记录

### 中文原稿语法与逻辑审查：第2–3章（2026-09-14）

本轮为独立重新阅读，不以既往语言建议作为发现依据。只提出建议，不修改 source-zh、chapters、tables 或 figures。范文只能支持表达方法，不能代替本文技术实现与实验依据。

#### 范围与结论

完整读取 source-zh/chapters/chapter02.tex（165行）、chapter03.tex（386行）及对应现英文；读取表 table_2_1–table_2_6、table_2_hi_screening_steps 的中英文件，图 figure_2_1–figure_2_4、figure_3_1–figure_3_3 的中英 TeX 图注。关联读取第4章 L41、L73、L79 的输入与配置协议。图内栅格文字不是本报告完整覆盖范围，不宣称已重审所有图像。

覆盖：框架四步骤；四组数据；15项HI定义；PCC/SCC与三阶段MS-CCCT；准入/排序/去冗余；模型三步骤；标准DSConv成本；DSConv-S/L结构；一般/Softmax/线性注意力；RAA归一化、聚合、广播、残差、复杂度；SLFA融合。

发现不是“中文到处有错”：大部分衔接顺畅。以下包括1项明确对应关系语言问题、1项中文问题但英文已修好、7项需确认的逻辑/技术表述、1项可选澄清。不得将全部建议一次写入论文。

#### M01：五个指标与三个属性使用“分别”却未分组（明确语言问题）

位置：[中文第2章L74](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:74)，[现英文同位置](D:/MS-AgentNet-English/chapters/chapter02.tex:74)。

中文改前：
> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9），分别描述热响应的幅值、特征位置及波动范围\cite{ref64}。

中文最小改后：
> 据此提取峰值（HI5）、峰值对应电压（HI6）、谷值（HI7）、谷值对应电压（HI8）和峰谷差（HI9）。其中，HI5和HI7描述热响应的幅值，HI6和HI8描述特征位置，HI9描述波动范围\cite{ref64}。

现英文：
> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted to describe the amplitude, characteristic positions, and range of variation of the thermal response\cite{ref64}.

英文建议：
> The peak value (HI5), voltage corresponding to the peak (HI6), valley value (HI7), voltage corresponding to the valley (HI8), and peak-to-valley difference (HI9) are extracted. HI5 and HI7 describe the amplitude of the thermal response, HI6 and HI8 describe its characteristic positions, and HI9 describes its range of variation\cite{ref64}.

原因/效果：不是简单嫌句长；5→3的对应在中文“分别”后缺失。英文已没有机械翻成 respectively，不属误译，但仍可将分组显式化。分组由既有指标定义直接确定，不新增电化学机制。两句仍在同一自然段。

范文：[JESSOHRUL TXT L1803–1811](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1803)逐项列出“the peak of the DTV curve (HI5)”以及对应峰位、谷值、谷位。助手释义：用指标实体与编号直接对应。它支持明确对应的写法，不含本文HI9，不能用它证明HI9机制；本项分组依据本文定义。

#### M02：残差句中省略主语导致“特征与自己相加”（中文问题，现英文保留）

位置：[中文第3章L33](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:33)。

中文改前：
> 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN），并与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：

中文建议：
> 特征$\mathbf X_l''$经$\operatorname{LN}_0$处理后输入前馈神经网络（FFN）；FFN的输出与$\mathbf X_l''$进行残差相加，得到Block输出$\mathbf Y_l$：

现英文（保留，无再次改动）：
> The features $\mathbf X_l''$ are processed by $\operatorname{LN}_0$ and then a feedforward neural network (FFN). The result is added to $\mathbf X_l''$ through a residual connection to produce the Block output $\mathbf Y_l$:

原因/效果：中文后一分句的隐含主语容易继续承接“特征X''”；公式明确相加的是FFN输出和X''。现英文The result已经依据公式消解，不需为了凑改动再次改。中文修正不改变计算。

范文：[Engineering-AI TXT L822–826](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:822)明确说明残差连接使用哪个阶段输出（“the output of the first stage”）。只借“点明相加对象”的表达；范文残差取X'、本文取X''，不得照搬对象。此短段可独立读取，不依据TXT跨栏顺序推断算法。

#### M03：最小值得分≠无条件保证两个电池均强相关（逻辑边界，需确认）

位置：[中文第2章L137](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:137)。

中文改前：
> 该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，使入选窗口在两节电池上均保持较强的相关性。

建议（将末项准确表达为选择目标）：
> 该得分由两节电池中的最低相关水平决定，可避免单一电池的局部高相关性主导窗口选择，并以提高两节电池中的最低相关水平为窗口选择目标。

现英文：
> This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and allowing the selected window to maintain strong correlations on both cells.

建议英文：
> This score is determined by the lowest correlation across the two cells, preventing a locally high correlation on a single cell from dominating window selection and favoring windows with a higher minimum correlation across the two cells.

原因：式S_i=min(...)及选择最大S只能提高所考察候选中的最差项。如果所有候选S均为0.2–0.3，最大者仍不是“强”。后文Oxford实测0.994447以及筛选阈值可以支持该结果，但不能倒推得分函数自身保证强相关。本项收窄“必然效果”为准则目标，涉及力度，需作者确认，不按纯语法自动处理。

范文：[BMSFormer TXT L447–457](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:447)先取跨电池最小PCC作baseline，再选择“the segment with the highest baseline value”。助手释义：选择最小相关水平最高的候选段。支持描述实际选择规则，不证明所有数据都强相关。该范文窗口步长与列举区间存在不一致，不继承其数值。

#### M04：‘其他电池’相对于开发集还是训练池？（协议指代待确认）

汇总说明：本项与主审跨章 X01 重叠，最终以主审 X01 的整段版本为准，不重复计为两项发现；以下保留独立核对依据。

位置：[中文第2章L160](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:160)；表2_4、第4章L41/L73。

中文改前：
> 用于后续评价的其他电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发与后续评价之间的数据隔离。

现英文：
> The other cells used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between feature development and subsequent evaluation.

若这里“其他”明确指开发集合之外，中文建议：
> 特征开发集合之外、用于后续评价的电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持这些电池与特征开发之间的数据隔离。

对应英文：
> Cells outside the feature-development set that are used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between these cells and feature development.

原因：开发集含Cell1/Cell2，第4章报告范围又含Cell2。前文亦用“训练后的模型用于其他电池”，彼处“其他”相对训练池。不能把不同“其他”合并理解为所有报告池均未参与开发。不是认定泄漏，更不是要求新增第三类协议角色；只是明确集合。若实际意图声称所有报告池未参与开发，则与现稿表/协议冲突，应先核对而非采用上述句子。

范文：[Engineering-AI TXT L396–400](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:396)明确相关计算用“only the calibration/training data”；L377–379说区间在后续测试前固定。借明确数据集合和冻结时点的表达；不能借其training partition替换本文两电池开发集。

#### M05：DSConv低成本结论缺少比值<1的条件（数学逻辑，需确认）

位置：[中文第3章L100](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:100)，公式L81–98。

中文改前：
> 由式\eqref{eq:dsconv_cost_ratio}可知，在输入、输出通道配置一致的情况下，DSConv的计算成本低于标准卷积，为后续小核与大核卷积模块的构建提供了基础。

现英文：
> Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and output channel configurations, DSConv has a lower computational cost than standard convolution, providing the basis for the small- and large-kernel modules described below.

保留现式的条件建议：
> 由式\eqref{eq:dsconv_cost_ratio}可知，在输入、输出通道配置一致且$1/C_{\mathrm{out}}+1/k^2<1$时，DSConv的计算成本低于标准卷积，为后续小核与大核卷积模块的构建提供了基础。

对应英文：
> Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and output channel configurations and $1/C_{\mathrm{out}}+1/k^2<1$, DSConv has a lower computational cost than standard convolution, providing the basis for the small- and large-kernel modules described below.

原因：直接由现式代入k=1得1+1/Cout>1；仅通道一致不充分。这是本文公式自身可验证的反例，不依赖外部结论。实际小核5/大核31可能满足相应一维条件，不等于无条件通式结论成立。增加技术限定，需作者确认；先处理M06以免保留错误维度的限定。

范文：[BMSFormer TXT L784–825](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:784)有同类二维成本记号，L814–817说明分离空间/通道运算。范文能说明公式来源风格，不能豁免本文比值小于1的条件，更不能据此证明本文带扩展的模块在任意配置都低成本。

#### M06：二维通式与一维序列尺寸没有接上（技术定义待确认）

位置：[中文第3章L57–100](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:57)、L110–170、L176–185；现英文同位置。

中文原句：
> 其中，$2C_{\mathrm{out}}$和$D_F\times D_F$分别表示扩展后的通道数和特征图尺寸。

现英文：
> where $2C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of channels and the feature map size, respectively.

冲突：前面输入B×N×d，转置B×2d×N、深度核1×5/1×31，均只有N个序列位置；成本却一直乘D_F×D_F，基础核面积k×k。没有说明这是二维示例再适配一维，或D_F²被特殊定义为位置数。无法单纯换“size”修好。

分支A（确实希望先介绍二维背景）：先明确中文“上述通式以二维方形特征图为例；以下模块沿序列维度进行一维卷积。”英文“ The preceding formulas use a square two-dimensional feature map as an example; the following modules apply one-dimensional convolution along the sequence dimension.” 随后必须由实现核实并统一后续实际成本式，不能只加此句了事。

分支B（全文只应给实际一维成本）：在确认计算计数口径、单样本、忽略偏置/激活、Cin=Cout=d后，将位置因子写N；基础核写k而非k²。例如现有结构的乘加级项可写DSConv-S：N(4d²+10d)，DSConv-L：N(6d²+93d)。这是根据两逐点+一深度的代数推导示意，不是可直接替换的FLOPs数值或已核实代码，不提供正式批准式。

原因/效果：消除“套范文公式但维度未适配”。涉及公式、定义及计量，必须核实后改；当前不选分支、不写论文。

范文：[BMSFormer TXT L784–789](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:784)确有k×k与NF×NF，[Engineering-AI TXT L845–849](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:845)明确N×d↔d×N转置。它们提示需要区分空间模板与序列实现，不证明两者可无说明混用。

#### M07：非负相似度不足以保证归一化分母有效（条件缺失）

位置：[中文第3章L207](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:207)，L209–223公式。

中文改前：
> 在采用非负相似度函数构造归一化注意力权重时，第$i$个注意力头在第$p$个位置的输出可表示为：

现英文：
> When a nonnegative similarity function is used to construct normalized attention weights, the output at the $p$th position of the $i$th attention head can be expressed as:

最小中文建议：
> 在采用非负相似度函数构造归一化注意力权重且该查询对应的相似度之和为正时，第$i$个注意力头在第$p$个位置的输出可表示为：

对应英文：
> When a nonnegative similarity function is used to construct normalized attention weights and the sum of similarities for the query is positive, the output at the $p$th position of the $i$th attention head can be expressed as:

原因：全行0满足非负，但现式为0/0；本文自己的RAA L294–311特意规定零正值行返回均匀分布，说明确有这一分支。建议只补一般商式成立条件，不改变RAA已写的分支，也不擅自新增epsilon。属于数学适用条件，需确认。范文未找到能直接支持该补充条件的对应完整表达；依据是现式与本文章节内定义，不硬凑范文。

#### M08：去冗余表each/otherwise的量词与加入时点不明（原稿已英文，算法待确认）

位置：[冻结表L13–16](D:/MS-AgentNet-English/source-zh/tables/table_2_hi_screening_steps.tex:13)与[现表同位置](D:/MS-AgentNet-English/tables/table_2_hi_screening_steps.tex:13)。这不是中文翻错，冻结稿该表原本就用英文。

原文：
> For each retained candidate HI $f_i$: compare $f_i$ with each HI already contained in $\mathcal{S}$; if their group-average absolute PCC and SCC both reach $\theta_{\mathrm{co}}=0.95$, remove $f_i$; otherwise, add $f_i$ to $\mathcal{S}$.

问题：先每一项比较，再otherwise加入，可能读成“某一对未超过阈值就加入”，即使下一对高度冗余；S为空时比较不执行，何时加入亦不明。需明确“存在一项/不存在任何项”及加入发生在全部检查后。

若实现是通常的任一高冗余即拒绝，中文建议（助手表达，非冻结原文）：
> 对每个保留候选$f_i$，若$\mathcal S$中存在至少一个指标，使其与$f_i$的组平均绝对PCC和SCC均达到$\theta_{\mathrm{co}}=0.95$，则剔除$f_i$；否则将$f_i$加入$\mathcal S$。

对应英文建议：
> For each retained candidate HI $f_i$, remove it if there is any HI in $\mathcal{S}$ for which the group-average absolute PCC and SCC with $f_i$ both reach $\theta_{\mathrm{co}}=0.95$; otherwise, add $f_i$ to $\mathcal{S}$.

该版本空集自然进入otherwise。仍需代码/作者确认，不能用“通常”推定实现。

范文：[JESSOHRUL TXT L1829–1834](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1829)确实先排序再剔除高特征间相关指标；它支持步骤顺序，不直接规定本文跨两电池聚合、PCC/SCC同时、存在量词。无直接证据处不得称范文标准算法。

#### M09：Oxford充电协议表—文不一致（事实待核，不强制择一）

位置：[中文第2章L29](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:29)、[冻结表2_1L19](D:/MS-AgentNet-English/source-zh/tables/table_2_1.tex:19)、对应现英文。

中文原句：
> 电池采用恒流–恒压方式充电至4.2 V……

现英文：
> The cells were charged to 4.2 V using a constant-current--constant-voltage protocol ...

表中原/现：Oxford Charge protocol (rate) = CC (2C)。

若实际全程CC-CV，表需写CC-CV（2C恒流阶段），是否保留2C亦核实；英文可为“CC-CV (2C during the CC phase)”。
若原数据所指是仅CC老化循环，正文对应中文应为“电池以2C恒流充电至4.2 V”，英文“The cells were charged at a constant current of 2C to 4.2 V.”
若表与正文分别描述老化与定期表征，二者可都正确但须标明各自阶段，不能强行同一。

没有选择上述分支。范文不能证明本文采用的数据阶段；本轮未查数据发布方协议，结论仅是现稿内部不一致。此前variance→Dynamic current profile的现表已改好，不重复列入实施建议。

#### M10：‘PCC仅对线性变化敏感’容易被理解成完全无法反映非线性（可选精确化）

位置：[中文第2章L108](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:108)。

中文原句：
> PCC是衡量CCCT与SOH线性关联强度的常用统计指标，但该指标仅对线性变化敏感，单独使用难以反映单调非线性关系。

现英文：
> PCC is a common statistical measure of the strength of the linear association between CCCT and SOH. However, it is sensitive only to linear changes and is insufficient on its own to characterize monotonic nonlinear relationships.

建议中文：
> PCC是衡量CCCT与SOH线性关联强度的常用统计指标，但单独使用难以充分刻画单调非线性关系。

对应英文：
> PCC is a common statistical measure of the strength of the linear association between CCCT and SOH. However, it is insufficient on its own to fully characterize monotonic nonlinear relationships.

原因：保留“衡量线性、需要SCC补充”的真正论点，避免将only解释成非线性关联一定没有PCC响应。此项不是否认PCC线性指标身份，也不改变筛选公式。若作者“仅对线性变化敏感”只是指标定义的简称，原句并非不可理解；精确化优先级低于上述逻辑问题。

范文：[JESSOHRUL TXT L1674–1680](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1674)：“PCC measures the linear correlation, while SCC assesses the monotonic relationship”。助手释义：分别说明两统计量测量的关系，不说PCC完全不响应非线性。此处支持删去过度限定only，不把范文“nonlinear dependencies”泛化为全部非线性。

#### 重点保留与不应强改

- 第2章L60“除……外”、L76“与DTV……不同”、L106“然而”、L149“相比之下”均有实际对象关系，不因连接词出现就认定错误。
- 第2章L139的R3优于R2取R3、否则保留R2，包含等分时的处理，保留；未凭搜索层级推断全电压连续域全局最优。
- 第2章L158四项相关系数确实接近1，不能因M03否定该具体样本结果；“跨电池一致性”在其两池语境可读，不擅自增成跨数据集。
- 第2章L90 HI13/14命名已被英文分清；L98充放电变量定义现英文已分组；不重复修改。
- 第3章L18与公式DSConv-L残差一致；L174明确残差在Block级，不将DSConv-S内部残差机械复制给L。
- 第3章L265明确映射维度等于dh、dh固定，线性复杂度条件已给，不再加冗余声明。
- 第3章L294、311共同正比例缩放、正值行归一化及全非正回退在公式层面一致；不把ReLU²称为Softmax的等价替换，不声称权重区分本身保证更高精度。
- 第3章L349低秩仅指等效序列交互映射Phi_q Phi_k，不说整个含残差RAA映射秩≤na，保留。
- 第3章L363固定h和na且上下文固定维度的复杂度表述可保留；理论复杂度不改写实际推理速度。
- 图2_4现图注已明确四子图Cell/PCC/SCC对应，保留；未把历史图注问题当成现稿未修。
- 表2_3各S=min(mPCC,mSCC)、表2_4所列HIs均满足给定准入阈值，未见须靠语言修复的数值冲突。去冗余是否导致全部所列最终集合仍需原始矩阵/代码，不能仅凭最终表保证。
- 其余表2_2、2_5、2_6已读，未发现新的中文语法错误；英文表头HI可更明确为HI1属可选表意，不计入本次可靠发现。

#### 本轮范文重读及证据边界

重读三篇TXT完整相应局部上下文：JESSOHRUL 1658–1686、1786–1849；BMSFormer435–459、735–825；Engineering-AI332–425、818–853。跨栏穿插已识别，本报告仅引用可独立定位的完整短语/小段，不根据穿插片段推断范文论证顺序、式号先后或跨页句法；未声称本轮重渲染PDF，亦未以旧词表代替原文。所有中文释义为助手译释。无直接参考依据项明确标示，不能因范文也这么写就沿用逻辑缺口。


## 附录C：详细审查记录

### 第4章中文逻辑与英文承接审查（2026-09-14）

本轮只提建议，未修改中文源稿、英文正文、表格或图片。中文全文第4章、对应当前英文及全部 table_4*.tex、figure_4*.tex 已逐项读取；图注审查不等于重新核验原始预测数据或逐像素图像。主审负责跨章协议一致性，本报告不把配置电池进入报告范围直接判为数据泄漏。

结论不是“中文很多语法错误”：发现 1 项确定中文主语问题（英文已经处理），3 项需要作者确认的证据/定义问题，3 项可选范围澄清，另有 1 项中文较强、英文已收窄的保留说明。以下编号 R01–R08。没有为了改动数量重复上轮已批准的修改。

#### 覆盖与保留

| 范围 | 核查结果 |
| --- | --- |
| 开头与评价指标，L1–37 | MAE/RMSE/MAPE/R² 定义及说明顺序无明显中文语法错误；MAPE 采用比例值与 L43 的 0.00615=0.615% 一致，不擅加乘100。开头强度见R08。 |
| HI筛选，L39–46 | 表中 HI1 七节均最低、Fusion 平均第四、HI9/HI11 在 Cell7/8 排序反转均成立。“不能保证”不是绝对否定，保留。Fusion的比较基准可更明确，见R06。 |
| 初始化/收敛/超参数，L48–81 | 初始化性能“较为接近”未写统计等效；默认正态是选择理由，不是声称其精度最优；收敛结论已有“当前实验设置下”。两电池用途英文已澄清，保留。 |
| Oxford与CALCE/MIT，L83–113 | 表中最佳电池数与整体排名吻合。全曲线指标不能单独证明局部阶段误差，见R02。主比较包含配置电池的范围交主审跨章说明。 |
| 跨数据集，L115–140 | source-only/适应的数据角色分开，负R²没有掩盖，30%适应未被写成全面成功。R01为中文主语问题，R07为趋势范围可选澄清。 |
| 消融，L143–162 | 单模块并非处处改善、M4在MIT并列最低、SFull在四组最低均与显示数值相符。互补不是唯一因果证明；“与设计目标一致”保留。指标定义见R03。 |
| 复杂度，L164–末尾 | LSTM训练最短、MS-AgentNet最低三项及相对降幅与表值吻合。未把FLOPs低写成实测推理最快。精度与成本来自不同配置需防混读，见R04；表标题见R05。 |
| 关联表图 | 读取14个table_4*.tex（含未被当前章调用的table_4_2）和4个figure_4*.tex（含未调用的figure_4_1）。已调用结果图注未见新增语法错误；不把未调用文件误算成论文展示内容。 |

#### R01｜确定中文语法问题；当前英文已修好，保留

位置：[中文第4章L137](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:137)、[英文L137](D:/MS-AgentNet-English/chapters/chapter04.tex:137)。

中文改前：

> 进一步比较相邻适配比例，CS2 和 CX2 源域从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。

中文最小建议：

> 进一步比较相邻适配比例，在分别以 CS2 和 CX2 为源域的设置下，适配比例从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。

当前英文（建议不改）：

> A comparison of adjacent adaptation ratios shows that increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively. Increasing it from 50\% to 70\% gives smaller reductions of 0.0114 and 0.0055.

原因：增加的是适配比例，不是源域本身。原句省略了真正主语；英文已明确 ratio，所以不能因为中文有病句，再把正常英文改一轮。不涉及研究主张或数字变更。三篇范文中本轮未定位与本适配比例协议直接对应的句子；这是本文表4-9与语法主语共同支持的修正，不能伪称范文原句。

#### R02｜需确认：整体MAPE推至寿命后期，证据粒度发生跳转

位置：[中文L107](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:107)、[英文L107](D:/MS-AgentNet-English/chapters/chapter04.tex:107)、[表4-6](D:/MS-AgentNet-English/tables/table_4_6.tex:27)。

中文改前相关完整句：

> 值得注意的是，在具有阶段性转折和非线性衰减尾部的 CX2\_38 上，MS-AgentNet 的 MAPE 仅为 0.037673，较 CNN-Transformer 和 Transformer 分别降低了 59.75\% 和 51.80\%，表明模型在寿命后期加速衰减阶段仍能保持较低的预测误差。

当前英文末句：

> This shows that the model maintains low prediction errors during accelerated late-life degradation.

问题与分支：表4-6列的是电池整体评价指标，没有单列寿命后期区间。前段图形描述可以支持轨迹跟踪，但不能由这一个全程MAPE直接推出某局部阶段数值误差低。这不是证明模型尾段表现差，而是证据范围没有接好。

- 若仅有当前全程指标：数字句不变，末尾中文建议“表明模型在该电池上的整体预测误差较低。”对应英文：`This shows that the model has low overall prediction errors on this cell.` 原L105关于尾段轨迹的图形描述保留，不删除。
- 若作者确有尾段区间误差：先明确区间定义和结果，再给英文；不能把0.037673擅自改称尾段MAPE。

这涉及结论证据范围收窄，必须确认，不能标成不改原意的纯润色。

范文依据及限度：本轮重新读取 Engineering-AI L1379–1450。其L1393明确说 `As evidenced by the magnified regions of Fig. 11`（依据图11的局部放大区域），局部响应的讨论明确指向局部图；L1437–1440另报整体平均RMSE。可借鉴的是“局部讨论对应局部证据”，不能继承其中强机制归因，也不能将双栏TXT交错的段落当成连续论证。本文建议的主要依据仍是表4-6实际统计范围。

#### R03｜需确认：综合平均误差及Reduction没有定义，正文与表格比较基准不同

位置：[中文L152–158](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:152)、[英文L152](D:/MS-AgentNet-English/chapters/chapter04.tex:152)、[表4-10表头L7](D:/MS-AgentNet-English/tables/table_4_10.tex:7)、[表4-11表头L7](D:/MS-AgentNet-English/tables/table_4_11.tex:7)。

改前：中文反复使用“综合平均误差”；英文使用 `combined average error`，表头为 `Average` 与 `Reduction`，没有运算定义/Reduction分母说明。

现有证据：CX2 M1的三个显示指标算术均值为(0.0170+0.0294+0.1035)/3≈0.0500，与Average一致；正文M2相对M1约1.20%，但M2行Reduction为54.40%，明显不是同一比较。后者很可能是M4相对M2的下降比例，而不是M2相对M1。表中MIT M1/M4同显0.0020仍列2.43%，也提示百分比可能来自未舍入数值。不能据显示精度直接判算错。

作者确认定义后，建议新增中文表注（条件式草案，不直接写入）：

> 综合平均误差为 MAE、RMSE 和 MAPE（比例形式）的算术平均值。Reduction 表示 M4 相对于该行模型的综合平均误差降幅，按（该行误差−M4误差）/该行误差计算；百分比基于未舍入结果。

对应英文条件式草案：

> Average is the arithmetic mean of MAE, RMSE, and MAPE expressed as a ratio. Reduction is the relative decrease in this average achieved by M4 compared with the model in that row. Percentages are calculated from unrounded results.

如实际采用加权平均/先跨电池后跨指标/不同舍入口径，必须按实际改写，不能采用上述猜测。补充定义不改变真实实验，但尚未确认的定义属于科学信息，不能当普通语法自动补入。正文M2对M1的比较有明确基准，保留，不为了与表列相同而改掉实验问题。

范文：本轮重读JESSOHRUL L3793–3808，范文逐项说明计量含义，其中 `floating-point operations required for a single forward pass` 把测量对象和范围写清。可借的是“先定义指标口径再比较”的做法；该段不能证明本文Average或Reduction应采用哪条公式。本项的直接依据是本文表头与数值，不是范文有同名列就足够。

#### R04｜需确认：精度与开销来自不同配置，综合句可能被读成同一配置同时实现

位置：[中文L170](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:170)、[英文L170](D:/MS-AgentNet-English/chapters/chapter04.tex:170)，关联L79、L168和表4-4/4-12。

中文改前：

> 这些结果表明，MS-AgentNet 在保持较高 SOH 估计精度的同时，具有更低的前向计算量、参数量和权重存储开销。

现有英文：

> These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.

核实：主性能比较学习率0.001；复杂度测试0.01。表4-4 CNN-LSTM为3层、LSTM为5层；复杂度设置两者均4层。不同测试配置本身不构成错误，但表4-12不列此配置下精度，因此不能无条件读成“最低资源这一个精确配置同时取得前述全部精度”。

若作者是在综合两组不同目的实验，中文建议：

> 主性能比较显示 MS-AgentNet 具有较高的 SOH 估计精度；在本节统一复杂度测试设置下，其前向计算量、参数量和权重存储开销均低于四种基线模型。

对应英文：

> MS-AgentNet achieves high SOH estimation accuracy in the main performance comparisons. Under the common settings used for the complexity test, it has lower forward-pass computation, parameter count, and weight storage overhead than the four baseline models.

效果：保留两类积极结果，明确各自来自哪里；不是新增实验或承诺同配置精度。如果实际已有相同配置下精度结果，可保留原意并补具体依据。此项关系到结论范围，须作者确认。前句“LSTM刻画复杂模式局限”也只能依据前面的预测结果，不应暗示最短训练时间导致精度低；目前although仅为权衡对比，不能自动判成因果错误。

范文：重新读取BMSFormer L1344–1351、1360–1365与JESSOHRUL L3793–3810：二者分别交代复杂度指标和比较配置。Engineering-AI L2455–2472也明确延迟测试的环境和输入尺寸。本轮不引用其“fair/identical”作为本文公平性证明，只参考把指标与实际测试条件绑定的写法。

#### R05｜可选范围澄清：same configuration标题过宽，四头与四层不是同一结构参数

位置：[表4-12标题L3](D:/MS-AgentNet-English/tables/table_4_12.tex:3)，中文源表标题本来也是英文；正文[中文L168](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:168)。

改前：`Comprehensive performance of models under the same configuration.`

建议：`Model resource costs under the specified comparison settings.`

中文效果对照：“相同配置下模型的综合性能”→“指定比较设置下的模型资源开销”。原因：表中实际只有资源指标，并不包含精度；模型本身结构不同，n对两类模型含义也不同。正文已经诚实限定“在数值上保持一致”，这一句不判错、不建议擅改4层或4头。标题收窄是信息准确性改进，不改变任何配置值。

范文：JESSOHRUL L3796–3798分列training cost/hardware cost；BMSFormer L1345–1351说明训练、硬件成本及配置。可参考“成本指标＋设置”命名，不机械继承same/identical来宣称结构等价。

#### R06｜可选范围澄清：Fusion“没有增益”缺少显式比较基准

位置：[中文L43](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:43)、[英文L43](D:/MS-AgentNet-English/chapters/chapter04.tex:43)。

中文改前：

> 当四项健康指标共同作为输入时，Fusion 的三项平均误差均排名第四，说明多类健康指标的直接组合没有形成进一步的性能增益。

中文建议：

> 当四项健康指标共同作为输入时，Fusion 的三项平均误差均排名第四，说明与单独使用 HI1 相比，直接组合这四项健康指标没有形成进一步的性能增益。

现英文：

> When all four HIs are used together, Fusion ranks fourth for all three average errors, showing that directly combining multiple types of HIs does not provide further performance gains.

建议英文：

> When all four HIs are used together, Fusion ranks fourth for all three average errors, showing that directly combining these four HIs does not improve performance over using HI1 alone.

原因：Fusion优于DTV平均结果，并不是对所有单指标都没有收益。根据前句正在讨论HI1，最自然解释原本就是相对HI1；因此这不是原结论必错，只是把隐含基准写明。若作者意指所有多特征融合策略普遍无效，需收窄主张而不只是改连接词。

范文：JESSOHRUL L1946–1962本轮重新读取，L1956–1959明确定义四项共同输入为Fusion，并将结果限定为 `each selected HI using the proposed model`。可参考其具体输入方案/模型绑定；不能借其Fusion结果替代本文表中排序。

#### R07｜可选范围限定：“持续改善”应理解为已测试比例，不外推无限加数据

位置：[中文L137](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:137)、[英文L137](D:/MS-AgentNet-English/chapters/chapter04.tex:137)。

中文改前：`结果表明，增加目标域观测能够持续改善模型在 Oxford 数据域上的适配性能`。

中文可选建议：`结果表明，在所测试的适配比例下，增加目标域观测能够持续改善模型在 Oxford 数据域上的适配性能`。

现英文：`These results show that adding target-domain observations continuously improves adaptation performance on Oxford.`

建议英文：`These results show that adding target-domain observations improves adaptation performance on Oxford across the tested adaptation ratios.`

原因：四档结果确实全部改善，故“持续”不直接判错；加范围可防读成对任意比例的普遍保证。没有改动70%时CX2源域R²仍为负的限制。三篇本轮未定位同适配比例实验的直接句型，依据是本文表4-9离散测试范围，不能硬套范文。

#### R08｜中文强度偏大，现英文已弱化，不再机械修改

位置：[中文L1](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:1)、[英文L1](D:/MS-AgentNet-English/chapters/chapter04.tex:1)。

中文改前：`综合上述多维度实验结果，可全面验证所提 MS-AgentNet 模型在电池 SOH 估计任务中的有效性与适用性。`

中文可选建议：`综合上述实验结果，可从所考察的方面评价所提 MS-AgentNet 模型在电池 SOH 估计任务中的有效性与适用性。`

现英文：`Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.`

处理：英文已用evaluation而不是完全证实所有适用场景；comprehensive此处可理解为列出的多维度覆盖，不必过度改动。如果作者希望中英文都明确限定，可将英文改为 `Together, these experiments evaluate the effectiveness and applicability of MS-AgentNet for battery SOH estimation from the aspects considered here.` 但较现稿更重，默认保留当前英文。

原因：本研究已经公开跨Oxford迁移限制，不能把“全面验证”理解成各种场景都有效。该处主要是中文措辞提醒，不计入必要英文改动。如果采用建议，属于主张措辞力度的收窄，而不是纯语法修正，需作者确认。无须用范文可能更强的demonstrate等自证词作为改强理由。

#### 本轮范文读取记录与边界

- Engineering-AI/full.txt：L1288–1332（校准、阈值、末期损失）、L1376–1450（Oxford与跨域轨迹讨论）、L2334–2355（FLOPs/延迟对象）、L2455–2472（硬件测试设置）。
- JESSOHRUL/full.txt：L1940–1985（HI与Fusion对比完整目标及操作段，结果段出现双栏交错，不拼接作引证）、L3780–3832（复杂度指标及完整配置段）。
- BMSFormer/full.txt：L1330–1394（复杂度小节目标、指标和训练设置；页间错序不作为写作推进范例）。
- 本轮没有研究范文句间顺序或报告新的逐句计数；Engineering-AI TXT明显含双栏错序，只采用内部连续、语义完整的短引及独立段落，不拼接错序文本建立论证。需要完整段落顺序时应回PDF，本报告没有声称已做该PDF重排检查。
- 范文提供表达/定义方式参照，不证明本文技术结论。R01、R03、R07没有直接等同的范文方法，已明确标注；不能为了“最好有范文依据”而捏造来源。

#### 待作者确认的最小清单

1. R02的0.037673是全程还是尾段指标？若全程，建议让该数只支持整体误差，将尾段观察留在图形段。
2. R03综合平均误差具体公式、Reduction分母及舍入规则是什么？确认后加定义表注。
3. R04资源表配置是否另有配套精度结果？若没有，按两类实验分别归属表述，不暗示同一配置共同获得所有指标。

R01仅说明中文已发现真实主语问题且英文已解决；R05–R07可由主审决定是否采纳；R08默认保留英文。所有条目都保留自然段边界，建议中的句级调整不构成段落拆并。


## 附录D：详细审查记录

### 中文原稿逻辑审查：跨章节范围与术语指代

日期：2026-09-14。仅审查与提案，未修改中英文论文。主审已通读冻结中文及当前英文摘要、第1–5章；本附录集中处理两个跨章节问题，章节内问题见其他附录。

#### X01｜“其他电池”和“数据隔离”的参照集合不够明确

性质：范围歧义；先确认中文意图，不据此判定实际实验泄漏。

位置：[中文第2章160行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:160)、[英文同段](D:/MS-AgentNet-English/chapters/chapter02.tex:160)；结合[第4章73行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:73)及主对比表注。

中文改前：

> 健康指标筛选仅在特征开发阶段执行。指标确定后，其定义和计算参数保持不变，并直接用于同一数据集其他电池的特征提取。用于后续评价的其他电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发与后续评价之间的数据隔离。

上下文证据：Oxford特征开发集合包含Cell1和Cell2，而第4章将Cell2作为配置电池，并在Cell2–Cell8的主比较范围中报告其结果。其他数据集也报告配置电池。表注已经标明这种角色，不能把主比较中全部电池写成未参与开发的独立留出电池。

风险：这里的“其他”若相对特征开发集合，指Cell3–Cell8等，句子可成立；若读者按第4章相对训练电池理解，则包括Cell2，与前述开发使用不符。不是所有“后续评价”都与开发集合完全不重叠。原句结尾的概括让这种误读更容易发生。

中文建议（须确认“其他”确指开发集合之外）：

> 健康指标筛选仅在特征开发阶段执行。指标确定后，其定义和计算参数保持不变，并直接用于同一数据集中特征开发集合之外电池的特征提取。这些电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发数据与这些电池的后续评价数据之间的隔离。

现有英文：

```tex
HI selection is performed only during feature development. Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for other cells within the same dataset. The other cells used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between feature development and subsequent evaluation.
```

英文建议（同一条件下）：

```tex
HI selection is performed only during feature development. Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for cells outside the feature-development set within the same dataset. These cells do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining separation between the feature-development data and the data used for subsequent evaluation on these cells.
```

改动效果：明确集合，不更换电池、不删结果、不另造第三种协议角色。若作者原意是“包括配置池在内的全部主比较结果均属独立留出评价”，则不是上述语言修补能解决的，需要核实协议及相应结论；不能直接采用此候选掩盖问题。

范文参照：本轮重读Engineering-AI full.txt 333–409的相关语境，仅取可连续确认的338–342行，原文短语为“performed exclusively on available historical reference data”，中文释义“仅在可用历史参考数据上执行”。见[原文](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:340)。它支持在说明筛选时写清数据范围，但其training partition不等于本文两电池开发集合，不能照搬协议，也不继承其自证式措辞。

需要作者确认：本段数据隔离是否仅针对特征开发集合之外的电池？若是，以上属于范围显式化；若不是，先核协议。

#### X02｜“不同电池体系和运行条件下的泛化”容易与跨数据集迁移混读

性质：可澄清的任务范围，不是确定语法错误。

位置：[中文第2章23行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:23)，结合第4章4.3.2、4.4、4.5以及结论。

中文改前（本段首句，后文不动）：

> 为考察所提方法在不同电池体系和运行条件下的泛化能力，选取 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四组公开电池老化数据开展实验。

上下文证据：第4章各数据集分别指定训练、配置电池，主比较为各自数据集内部的跨电池结果；另设第4.5节跨数据集source-only和适应实验，输入定义也另外统一。不能把“多种数据集上分别训练与评价”读成“一个模型直接跨化学体系泛化”。

中文建议（若本句主要介绍四组数据对域内实验的覆盖）：

> 为考察所提方法在不同电池体系和运行条件下的估计性能及各数据集内的跨电池泛化能力，选取 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四组公开电池老化数据开展实验。

现有英文：

```tex
Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, are selected to examine the generalization capability of the proposed method across different battery systems and operating conditions.
```

英文建议（上述意图下）：

```tex
Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, are selected to examine the estimation performance of the proposed method under different battery systems and operating conditions, as well as its cross-cell generalization within each dataset.
```

效果与边界：把工况覆盖与泛化范围分开，未新增实验。如果作者希望本句同时概括另设的迁移实验，可保留较宽概括并在后文明确域内与跨域实验分别进行；不要求机械增加所有限定。

范文参照：本轮完整读取BMSFormer full.txt 270–299的连续框架说明，284–293行把训练和配置后对其他电池的评价明确限定在“other batteries in the corresponding dataset”（对应数据集中的其他电池）。见[原文](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:290)。只借用数据集内范围的明确表达，不继承其30%/70%划分或384组设置。范文不证明本文实验正确。

#### 不是本轮错误的内容

- 第4章已明确区分source-only与使用目标域数据的适应，不把二者混称零样本迁移。
- 结论保留“域内”“一定的”“潜力”，并把嵌入式硬件验证列为未来工作；不要求改成已完成部署。
- 主对比表已经标注配置电池身份，不能仅凭报告配置池结果断言数据泄漏或要求删行。
- 本附录不验证模型训练代码、实际数据访问日志或原始数据处理流程；仅指出稿件表述的范围与一致性风险。


