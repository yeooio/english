# Engineering-AI 全文阅读与句式适配复核

日期：2026-09-14。只提建议，未修改中文或英文论文。

## 实际阅读范围

本轮分段读取 `style-references/Engineering-AI/full.txt` 第1–3163行至EOF，包括正文、图表、声明与参考文献。重新通读 `chapters/abstract.tex` 及 `chapter01.tex`–`chapter05.tex`、完整术语表。重点检查摘要、引言、结论；候选核对了冻结中文引言完整段落及本节上下文。没有把旧句式库代替本轮原文阅读。

按 PDF 技能渲染并目测 Engineering-AI 原PDF第1整页，核实摘要的连续句序、名称和句界。TXT有双栏错序：例如引言后半与Related work、方法模块Step 1–3在提取文本中穿插；不把它们当成原文的句间顺序。以下逐句统计只针对已目测的完整摘要。原PDF：`style-references/Engineering-AI/source.pdf`。

另重读 BMSFormer `full.txt` L136–204 的数据驱动综述、挑战和贡献引入，以及 JESSOHRUL L1746–1854 的相关分析、跨电池差异和筛选语境。后者穿插DTV/DTC另栏，筛选段按明确的段首和语义连续关系定位；不依据其伪代码条件裁定本文筛选算法。三篇对应语境由主审交叉核实后再入正式建议。

## 1. 完整代表段的逐句实测

来源：Engineering-AI，PDF第1页 Abstract，TXT L34–47；起点 `To address the computational bottleneck`，终点 `readiness for embedded deployment.`。共6句、191词。计数规则：修复PDF换行造成的 `Local– Global`，以空白分词，连字符复合词、缩写和数值各按一个词；小数点不是句界。这个数字不代表全文句数或全文字数。

|句ID/定位起点|词数|主语|主句时态/语态|功能|推进方式|
|---|---:|---|---|---|---|
|EAI-A1 `To address ...`|32|this paper|一般现在时/主动 presents|问题+研究目标（混合）|先交代计算瓶颈和BMS条件，再提出框架|
|EAI-A2 `First, a systematic ...`|19|a systematic feature selection process|一般现在时/主动 identifies|方法|First：从总框架进入HI选择|
|EAI-A3 `Subsequently, we propose ...`|21|we|一般现在时/主动 propose|方法|Subsequently：由输入转向网络设计|
|EAI-A4 `By integrating ...`|37|this AI model|一般现在时/主动 achieves|方法及设计能力|展开上一句架构组成和作用；不是独立实验结果|
|EAI-A5 `Experiments on ...`|40|Experiments|一般现在时/主动 demonstrate|实验结果|从方法转到数据集和数值比较|
|EAI-A6 `With a model size ...`|42|the AI framework|一般现在时/主动 proves；从句 implementation maintains|硬件验证方法+结果（混合）|接结果，补资源规模和实现验证|

词数分布：19、21、32、37、40、42；最短19、最长42、中位数34.5、平均31.83。方法句3/6=50%，方法词数77/191=40.31%；纯结果句1/6=16.67%，结果词数40/191=20.94%。混合句另列2/6=33.33%、74/191=38.74%，不把它们同时算入不相交的方法和结果比例。

可学习的是“框架→输入→模型→模块作用→结果→资源验证”的功能连接和具体主语，不是机械套6句或平均句长。本稿原段内容及次序仍优先。该摘要也有长前置成分、专名堆叠及强力度词，因此不能把全文都改成它的语气；`proves`、`superior`和已完成硬件部署不能移植到本稿。

## 2. 可追溯的适配句型

以下是抽象后的适配模板，不是范文原句，也不是新译文授权。

|适配结构|已核原文位置/功能|适合本文的用法和边界|
|---|---|---|
|`[Selection process] identifies/selects [HIs] from [data].`|摘要A2，L36–37；过程作主语说明选什么|用具体算法主语和筛选动词，保留本文跨电池与冗余条件；不把积分面积换给本文CCCT|
|`[Model/module] combines [A] with [B] to [function].`|摘要A3–A4，L37–41；模块组成和目标|保留DSConv-S/L、SLFA、RAA，不套入AFF/FLFA/FDFA/PIAF|
|`[Model] achieves [metric] on [dataset], compared with [baseline].`|摘要A5，L41–44；带比较对象的结果|保留实际指标、平均对象、数值及比较基线；不添加显著性|
|`With [resource condition], [model] [supported result].`|摘要A6，L44–47；资源与性能并列|本稿只能填已经测量的参数量/存储/运算量，不变成MCU部署或推理延迟证据|

## 3. 一处可选直接性改善

位置：`chapters/chapter01.tex:25`；冻结中文 `source-zh/chapters/chapter01.tex:25`。分类：**词汇简单但表达绕；可选，不是语法错误。**

中文完整段落：

> 单一健康指标所反映的退化信息相对有限，多源特征能够从不同方面补充电池退化的描述。然而，增加候选指标并不必然提高估计精度，表征能力较弱、跨电池表现不稳定或相互重复的指标，可能限制多源信息的有效利用，并增加模型的学习负担。因此，有必要设计相应的健康指标筛选算法，将SOH相关性、跨电池表现与冗余关系纳入统一的评价与筛选过程，保留具有稳定表征能力的指标，减少弱相关和重复信息的输入，以帮助模型更有效地学习电池退化规律。

现有英文完整句：

> It is therefore necessary to develop a health indicator selection algorithm that incorporates SOH correlation, cross-cell performance, and redundancy into a unified evaluation and selection process.

建议英文完整句：

> It is therefore necessary to develop a health indicator selection algorithm that jointly evaluates SOH correlation, cross-cell performance, and redundancy when selecting indicators.

中文原因：保留“有必要设计算法”的前半句，只把“算法将若干方面纳入统一评价与筛选过程”的抽象转述改为“算法在筛选时综合评价什么”。`It is therefore necessary to develop`完整保留必要性和设计意图；`jointly evaluates ... when selecting indicators`保留统一评价与筛选，不删除SOH相关性、跨电池表现或冗余。后一句关于保留稳定指标、减少弱相关/重复输入及帮助模型学习原样保留，不重排或合并段落。

简化的仅是 `incorporates ... into a unified evaluation and selection process` 的名词化结构，以 `jointly evaluates ... when selecting indicators`直接说明操作；不删除`develop`或技术信息。不得进一步简化成只按相关性选HI，也不能把“有必要设计”改成已经解决。

范文是否也如此：

- Engineering-AI 摘要A2直接用筛选过程作主语和 `identifies` 说明操作，但正文§3.3.3（L423–428）也采用抽象的“从静态筛选转向超参数搜索”说明，故抽象表达不是禁用项。
- BMSFormer L161–190挑战与引入仍有 `insufficient representational capabilities` 等名词结构，说明原句不是不符合所有范文的硬错误。
- JESSOHRUL L1784–1798也使用 `it is essential to introduce ... incorporates ... mechanism`，与本文现句结构接近；其接续的筛选方法段（L1821–1834）又直接用方法作主语说明 `jointly evaluate`、保留、排序和剔除。本文可借更直接的操作结构，但不借其平均相关、阈值或电池角色。

本文是引言中的筛选需求，范文后一个直接写法是方法操作，功能并非完全相同，所以保留“需要”而不写成本文已完成的操作。这也是只列可选、不升级为错误的原因。该建议需主审三文交叉确认和作者批准后才能写入正文。

## 4. 应明确保留的表达

- 摘要 `We compared ...` 后接 `The experimental results show ...`：已完成比较与当前结果陈述分工正常，不需统一成一种时态。Engineering-AI摘要本身全现在时只是另一种叙述选择。
- 引言报道具体先前研究用过去时，模型常规功能用现在时，研究趋势用现在完成时；这种切换有上下文功能，不是机械不一致。
- 结论中的固定agent数、同一数据集其他电池、in-domain cross-cell generalization、部署potential等边界保留，不能为短句删去。
- 未发现摘要/引言/结论中新的确定术语错译。本轮不为模仿范文而将resource-limited换为resource-constrained，或将capacity recovery换为capacity regeneration。
- 引言深度学习首句偏长，但“发展背景→采用多层网络→非线性能力→捕捉模式→改善精度”的信息均有中文来源；若仅靠删去发展、能力或效果来缩短，会丢信息。此处本轮保留，不凑新问题。

## 结论

新增1项可选句法简化；0项新确认的时态/语态或术语错误。此前两项可选直接性建议没有自动实施，也不在本报告重复计数。没有论文写入，没有重新翻译全文，没有新增技术解释或证据。
