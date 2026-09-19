# 2026-09-14 语法、时态与语态审查：摘要、引言、第四章和结论

本记录是本轮独立审查结果，不覆盖或撤销历史记录，也未修改论文。重点负责摘要、引言、第四章、第五章及实验图表英文；第二、三章作全文上下文通读。结论：负责范围内未确认需要强制修改的主谓一致、时态或语态错误。少数表达可作最小调整，但不应把风格选择包装成语法错误。

## 实际阅读范围

- 本文：`main.tex` 1–24；`chapters/abstract.tex` 1–3；`chapter01.tex` 1–48；`chapter02.tex` 1–165；`chapter03.tex` 1–386；`chapter04.tex` 1–176；`chapter05.tex` 1–5。通读全部 `tables/*.tex` 的英文表题、表头、文字单元格及表注，及全部 `figures/*.tex` 的可编辑英文图题。数字表格用于理解比较对象，不作为此次完整数值复算；没有声称检查全部栅格图内文字。
- 规则：本轮读取 `AGENTS.md`、`style-references/usage-guide.md`、`translation-guides/terminology.md`、`scientific-boundaries.md`、`house-style.md`。
- Engineering-AI：`abstract.txt` 1–86；`introduction.txt` 1–193（实际引言在双栏中续到贡献条目）；`results.txt` 1–225、225–328、1317–1388；`conclusion.txt` 1–65。
- BMSFormer：`abstract.txt` 1–88；`introduction.txt` 1–260；`results.txt` 163–200、320–550、999–1125；`conclusion.txt` 1–25、333–406（原提取把第15页结论续文放在第14页结论前）。
- JESSOHRUL：`abstract.txt` 1–85；`introduction.txt` 85–360，结合摘要文件中引言开头52–77；`results.txt` 1–135、982–1024、1450–1474、1628–1664；`conclusion.txt` 1–190、288–330。
- PDF回查：实际渲染并查看 Engineering-AI PDF p.2、BMSFormer PDF p.2、JESSOHRUL PDF p.3，确认引言的两栏顺序和贡献条目连续关系。其余本轮依据只采用已读完整句段，不将跨栏断裂当成作者原句，也不宣称读遍三篇全文。本次未重新统计三篇全文句数。
- 为确认冗余与协议对象，核对冻结中文 `source-zh/chapters/chapter04.tex` 61、117–137；这不是重新翻译任务。

## 可选最小修改

### O1：词汇简单但重复解释——初始化句

位置：`chapters/chapter04.tex:61`。

现有英文：

> This initialization gives different agents small, nonidentical initial parameters, avoiding identical initial states.

建议英文：

> This initialization gives different agents small, nonidentical initial parameters.

中文原因：`nonidentical initial parameters` 已表达不处于相同参数初态；末尾再次说 `avoiding identical initial states`，没有增加独立操作或限定。仅删同一句中的重复解释，保留不同智能体、小幅值及非一致性。

范文校准：Engineering-AI §5.2.1，`results.txt` 108–118、139–169，说明初始化分布、零均值与截断理由，也存在对作用的展开说明；本例不能因为“多一句说明”就判错。其静态单智能体与本文两个智能体并非同条件，不继承它的截断策略或死神经元解释。BMSFormer §4实验设置，`results.txt` 171–198，和 JESSOHRUL §4.4.2，`conclusion.txt` 11–37，以对象、设置和用途直接组织句子；这些已读段落没有与本文两个智能体相同的初始化条件，不能用它们证明全文没有类似重复。**定为可选去冗余，不是语法错误。**

### O2：比较对象可更完整，但范文也常省略

位置：`chapters/chapter04.tex:96`、109。

现有英文开头（后续三个指标和全部百分比保持原样）：

> Compared with CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by ...

建议英文开头：

> Compared with the corresponding values for CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by ...

中文原因：补出“比较各模型的对应指标值”，让语法表面上的比较对象更对称；这会略增字数，因此不作为简化表达的重点。

范文校准：BMSFormer §4.2.1，`results.txt` 411–419，先以模型作主语，再连续列三指标相对四模型的降低率；§4.3.2，999–1013及1084–1086，也有估计值与其他模型比较的省略。JESSOHRUL §4.4.1，1628–1662，尤其1648–1655，使用平均误差降低率直接 `compared with M1, M2, and M3`。Engineering-AI §5.3.2，240–251，用模型作主语报告MAE及相对Transformer的降低率；§5.6.4，1317–1330，也直接连接模型、资源和误差比较。**三篇与本文都属于已明确指标的模型比较，同类省略能够理解；本文不是误把两个不同物理量比较。原句可保留，改写仅可选。**不为减少长句而删掉作者原有数字，也不机械拆成三句。

### O3：cell 与 domain 的层级名称可更精确

位置：`chapters/chapter04.tex:132`。

现有英文：

> With CS2\_36 and CX2\_36 used as the respective source domains, the readout layer is adapted with early-cycle data from Oxford Cell1 at adaptation ratios of 10\%, 30\%, 50\%, and 70\%.

建议英文：

> With CS2\_36 and CX2\_36 used as the respective source-domain training cells, the readout layer is adapted with early-cycle data from Oxford Cell1 at adaptation ratios of 10\%, 30\%, 50\%, and 70\%.

中文原因：119行把CS2、CX2、Oxford定义为域，把具体cell编号定义为训练/适应电池。这里补 `training cells` 与前文对象层级更一致，不改变实际数据角色。

范文校准：Engineering-AI §5.2.2，`results.txt` 171–192，以 `historical reference cell` 明确具体电池；BMSFormer §4，171–192，把Cell1等简称 `training sets`；JESSOHRUL §4.2.1，100–111，明确CS2–35为训练和验证电池，而§4.4.1，1648–1653，又用 `NASA B0005 dataset` 表示具体电池数据。三篇存在“电池/其数据集”的正常简写；已读对应段落并非本文这种跨数据集适应协议，不能将其简写规则直接当作严格定义。本文119行已足以消歧，且冻结中文132行也有同样简写。**属于可选统一，不是已确认的技术错误或新增角色要求。**

## 明确保留的时态、语态与句式

| 本文位置与现有表达 | 本轮判断 | 三篇对应原文及同条件比较 |
| --- | --- | --- |
| 摘要：`this paper proposes`、`is proposed`、`is constructed`；后接 `We compared` 和 `The experimental results show` | 保留。介绍本文方法用现在时，已完成比较用过去时，当前呈现的结果用现在时，功能不同。主动与被动切换都有明确主语。 | JES摘要33–50同样使用 `proposes`、`is proposed`、`were conducted`、`results demonstrate`。EAI摘要34–47以现在时报告方法和结果；BMS摘要30–40现在时主动/被动并用。不存在只能选择一种时态/语态的共同规范。 |
| 引言9–23行：通用机理/模型能力用现在时，具体研究用 `developed/used/proposed` 等过去时 | 保留，不统一改过去或现在时。 | EAI引言/相关工作90–181，BMS引言94–220，JES引言89–243；三篇都有一般陈述现在时和具体已发表研究过去时。PDF回查已排除跨栏错连。 |
| 第四章41、73、117、145、166–168：`is selected`、`are used`、`is trained`、`are conducted` | 保留。这里把协议作为本文正在说明的程序，使用一般现在时被动一致；不要求为了“实验已完成”逐项改过去时。 | BMS结果171–198、465–491以及JES结果25–42、76–98和复杂度11–37，也直接使用现在时被动说明实验配置。EAI结果18–30、108–118、173–192更偏过去时；这是论文选择差异。 |
| 第四章43、96、107、109、125、154、170：`results show`、`achieves`、`decrease`、`reduces` | 保留。表图结果及其比较统一使用现在时。 | EAI结果240–251、256–322，BMS结果1003–1013，JES结果112–120、1648–1662均有相同用法。BMS另有过去时报告结果，不要求本文也混用。 |
| 第五章：`This study proposes`、`Experiments ... show`；未来工作 `will focus`、`will cover` | 保留。当前贡献/证据与未来工作时态分工清楚。 | EAI结论56–59接24–42再65；BMS结论333–348接1–16；JES结论62–98接299–312。三篇都区分当前贡献和未来方向，过去时或现在完成时也可用于已完成验证。 |
| 第四章63：`Their R² values range from ..., RMSE from ..., and MAE from ...` | 保留。后两项省略可从前项恢复的 `values range`，属于正常并列省略。 | 三篇结果均有多指标并列及省略，尤其BMS结果411–419、JES复杂度38–57；本文各指标对象及区间清楚。没有因为省略动词就形成不完整句。 |
| 表题/图题：`SOH estimation errors/results ...`，表注 `denote/denotes`、`are shown` | 保留。标题使用名词短语，无需硬加谓语；表注主谓数在已读范围内一致。 | BMS Table 5（results502）、JES Table 14（conclusion99–100）、EAI Fig.11（results299）均采用简短名词短语表题/图题。不能把标题当正文残句处理。 |

## 可复用的范文功能句式（都是适配模板，不是整句原引文）

- 方法或贡献：`This study proposes [framework] to [address the stated problem].` 三篇摘要/结论均采用具体研究主体与明确动作；本文摘要和结论已实现，无需换句式。
- 历史研究：`[Author] used [method/data] to [task].` 三篇引言均有此结构；本文9–23行基本已采用，保留过去时。
- 实验程序：`[Cell/data] is used for [role], and [other cell/data] is used for [other role].` BMS实验段及JES实验段均有同类角色说明；本文用已定义的训练/配置角色适配，不照搬范文的30%/70%协议。
- 结果：`[Model] achieves [metric] on [scope], compared with [baseline].` BMS §4.3.2、JES §4.4.1、EAI §5.3.2提供功能依据。本文已经常以具体模型为主语，保留限定与比较对象即可。
- 结论边界：`The framework still relies on [required data]. Future work will focus on [specific next step].` 依据三篇结论限制/未来工作段适配；本文最后一段已经自然，不必把 `will` 改成现在时或新增防御性说明。

这里提炼的是主语、动作和时态功能，不是要求全文套同一模板。首轮负责范围没有确认“必须修复”项；上述三项均为低优先级可选，不应在汇总时升级成硬错误。

## 同日追加：仅正文的附着、指代与中文冗余复查

作者后续要求暂不处理图内文字。本次只复查正文，并重新读取三篇完整摘要：EAI `abstract.txt` 34–47、BMS 30–40、JES 33–50；引言对应完整语境：EAI `introduction.txt` 90–181、BMS 120–160及162–220、JES 89–121及232–352；实验总览完整语境：EAI `results.txt` 18–30、BMS 171–198（续页接回同段）、JES 25–42。同时重读本文目标英文句与冻结中文对应段；下列不依赖旧词表或旧报告作为范文证据。

### S1：摘要大核句——简化谓语管辖（建议采用，非硬语法错）

现有英文：

> Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity.

完整建议句：

> Additionally, large-kernel depthwise separable convolutions extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity.

原因：仅删除 `are used to`，主干成为 `large-kernel ... convolutions extract ... and work ...`，两项功能直接并列。长时间尺度特征、大核与小核共同作用、多尺度和多通道融合、低参数开销和增强多样性全部保留。**属于“词汇简单但句法绕”的最小修复。**

附着核实：原句既可读作 `are used [to extract ... and (to) work ...]`，也可读作 `[are used to extract ...] and [work ...]`。两种分析中 `work` 的主体都为大核卷积，没有出现把“退化特征”误作工作主体的必要读法；不能把主动/被动并列本身定为语法错误。修改的理由是减少处理负担。

三篇校准：BMS摘要30–40以卷积为主语使用 `are embedded to fuse ...`，这说明被动结构本身可保留；它没有本文“先提取长尺度特征，再与小核合作”的双重功能，不能机械照抄整句。EAI摘要34–47直接使用模块/模型主语陈述作用，JES摘要33–50直接并列 `capture ... improve ... reduce ...`。三篇与本文同属摘要功能句，但模块细节不同。借用明确对象与并列动作，不沿用其新模块或夸大词。

### S2：引言13行——消除 `their` 回指（建议采用，指代可改善）

现有英文：

> With the rapid development of deep learning, researchers have increasingly used multilayer neural networks to capture complex battery degradation patterns through their strong nonlinear representational capability and thereby improve estimation accuracy\cite{ref14}.

完整建议句：

> With the rapid development of deep learning, researchers have increasingly used multilayer neural networks with strong nonlinear representational capability to capture complex battery degradation patterns and thereby improve estimation accuracy\cite{ref14}.

原因：`their` 预期指向神经网络，但同句还有复数主语 `researchers`。技术语境足以使读者选中网络，因此不是已确认的错译；把能力直接放在 `multilayer neural networks` 后面，可消除语法上允许但语义上不合适的回指。保留研究者、近年来使用趋势、网络能力、捕捉退化模式和提高精度，不改成能力属于研究者。`have increasingly used` 保留，没有时态问题。

三篇校准：EAI引言98–103把网络应用与捕捉复杂老化动态直接相连；BMS引言137–160尤其155–159明确使用 `ability of CNNs`，把能力的拥有者写出；JES引言89–104分别直接以 `RNNs` 和 `Transformers` 描述建模能力。三篇对应语境都区分研究行为与模型能力，支持明确归属。范文使用代词并不意味着本文同句中的竞争先行词无需检查；本例能从技术常识消歧，所以定为建议采用的清晰度修复，而非硬语法错误。

### S3：引言27行——把退化表征的抽象名词链改为动作（建议采用）

现有英文：

> For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention.

完整建议句：

> For health indicators, differences in battery materials and operating conditions call for further attention to how consistently the selected HIs represent degradation across cells.

原因：`the stability of their degradation representations across cells` 连续叠加“稳定性—表征—跨电池”的名词限定，`their` 还要回指句首HIs。改成 `the selected HIs represent degradation` 的主谓结构，用 `consistently` 表示稳定性，保留材料和工况差异、跨电池范围与“仍需关注”的力度。没有改成已证实失稳，也没有增加“本文证明稳定”的结论。**这是简单词仍表达绕的候选，不仅是难词替换。**

三篇校准：JES引言105–121直接写温度HIs在不同工况下不稳定，实际断言比本文强，不能照搬其否定结论；其244–264也存在较抽象、较绕的必要性阐述，不能以范文存在这种写法要求本文保留名词链。BMS引言169–174也使用 `representational capabilities` 等抽象名词，但直接以模型面对的困难统领；EAI引言90–107、161–181常直接让特征承担敏感性或稳定性动作。与本文同为输入表征/剩余问题语境，建议只借“HI直接做什么”的句法，不扩大问题强度。原句语法成立，修改属于直接性改善。

同段末句也有主干较晚，但其中计算能力、存储空间、实时要求、有效表征和紧凑/高效目标均有独立含义，不能为了短句全部删除。此次不对整段重排。

### S4：第四章1行——保留总览收束，只缩短空泛名词结构（可选）

现有收束句：

> Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.

完整建议句：

> Together, these experiments comprehensively evaluate the effectiveness and applicability of MS-AgentNet for battery SOH estimation.

原因：把 `provide a comprehensive evaluation of` 改为 `comprehensively evaluate`，保留“综合评价”“有效性与适用性”和SOH任务范围。与段首 `systematically evaluates` 有重复，但段末还承担汇总各类实验用途的作用；**不能把整个末句直接删掉并声称没有损失信息**，除非另将其独有内容融入其他句子，而那已超出此次最小句法修复。

三篇校准：JES结果25–42与本文非常接近，同样按“总评估—实验类型—分项用途—综合评价”推进，末句 `Collectively ... thorough validation ...` 重申总评估；EAI结果18–30也以系统评价开头、全面评价实用性收尾。BMS结果171–198主要进一步说明协议，不同组织方式不能成为本文必须删结句的依据。本文和前两篇同条件，保留段落收束完全可接受。这里只提供可选的名词转动词，不把“还能更短”当正文错误。

### S5：第四章61行——复核O1，不新列重复问题

建议仍为：

> This initialization gives different agents small, nonidentical initial parameters.

冻结中文确实同时陈述“小幅值非一致参数”和“避免相同初态”；本句后半属于前半在参数初始化语境下的同义解释。作者本轮明确允许删中文冗余表达，可建议删尾部。EAI初始化段108–118及139–169存在初始化目的的重复展开，但它说的是不同机制/风险，不能据此否定本文这处同义重复。O1分类保持可选；不把一次重复计成两个问题。

本次追加没有发现应强制统一时态或语态的依据。S1–S3比纯同义词替换更有实际价值，可优先给作者选择；S4只属于轻量精简。仍未修改正文。

## 阅读覆盖补充：三篇结果部分余下文字

按作者希望仔细阅读三篇范文的要求，同日继续补读了原来未覆盖的结果文件部分。到本记录此处，三篇 `results.txt` 的全部行范围均已遍历，所有含英文文字的正文、标题、表头和表注均已阅读；为了专注语言，本次余下部分省略了纯数字表格行、空行及孤立公式符号行，未复算数字，也未检查图像内文字。三篇完整结果文件的范围分别为 EAI 1–1721、BMS 1–1449、JES 1–2213。它们包含少量前章方法尾部、结论及参考文献，也已随文件读到；不把这种覆盖等同于完整重读三篇全论文。

此次补读范围：

- EAI：329–954、955–1316、1389–1721；结合之前已读部分，覆盖所有结果段和统计检验段。
- BMS：1–162、201–319、551–998、1126–1449；补全效率、超参数组合、跨电池讨论及其续页。
- JES：136–981、1025–1449、1475–1627、1665–2213；补全CS2/NASA结果、RUL结果、消融衔接和复杂度段。

新增语言校准结论如下：

1. **现在时与过去时没有单一强制比例。** EAI955–967以 `were conducted`、`were assessed` 交代完成的消融，再用 `integrates`、`results ... indicate`、`suggests` 描述结构和结果。BMS763–793以现在时为主报告效率及配置变化。JES1064–1081用现在时介绍RUL实验，1047–1058又以 `we analyzed` 引出已完成分析，再回到现在时报告模型。本文按功能选择时态的保留结论没有改变。
2. **主动/被动并用不自动违规。** JES1923–1979以被动说明测量和配置，用模型作主语报告 `achieves`、`reduces`；EAI955–967也在同段并用主动结构说明、被动实验行为和主动结果。摘要S1的改写因此仍应归为简化结构，而非声称主动/被动不能并列。
3. **不能因模仿而引入更强的解释。** EAI1186–1196以较长的机制段解释模块互补，JES1047–1062由结果进一步讨论模型复杂度与学习能力。本文没有必要照搬其解释长度或因果力度。S2和S3只澄清能力归属与HI动作，不新增能力形成机制，也不把“需关注”改成已经证实的失效。
4. **“概述—分项—收束”的重复也出现在结果部分。** 除实验总览外，JES消融总览1460–1464接1445–1449仍以综合评估收束；EAI结果与各类模块讨论也常在分项后归纳。这支持S4保留总结功能、只缩短名词结构的处理，不支持无差别删去段末总结。

该补读未新增必须修复项，未改变S1–S5的分级；它补足范文语言尺度，不引入额外实验、因果解释或数字核算要求。结果文件仍有双栏错序；以上判断只使用能够明确接回的完整句段，未把错序视为范文的逻辑顺序。
