# 第四章范文对齐：持续审查与去重总台账

实施状态（2026-09-16）：作者确认“可以修改”后，S1—S8、V1、R1共10项已实施；英文正文12处、表4-1两处、双语稿对应英文12处。4.4待核项未动。按作者要求未编译；以下各轮“未修改/待确认”均为历史审查状态。备份：`build/ch4-approved-style-20260916-165619/`。

最新逐节阅读入口：[第四章一次性交付：4.1—4.6及各小结](chapter04-section-by-section-review-2026-09-16.md)。该版归并已有项，新增C4-S7和C4-S8两项低优先可选，仍未应用正文修改。

状态：只写审查记录，未改论文或表格，未编译。当前范围仍为第四章，不扩展到已完成的第一章；B类既有术语和已知图内名称不重新报项。

## 本轮方法及判断标准

三名 agent 分别通读第四章，按词汇搭配、句式推进、力度限定三个视角检查；主代理读报告、重看涉及的中文和三篇完整功能语境、检查历史记录并作最终取舍。这是三个互补视角的通读，不称为三人完全不知前次结论的盲审。

逐项核对：名词对应的技术对象；动词与主语/宾语；形容词程度；主干和停顿；句间推进；事实、比较范围、因果与可能性。未使用范文的某个词，不自动构成遗漏；只有对象和意思相同、在本句有实际改善价值时才建议借用。

查重键采用“位置＋技术对象＋修改目的”，不只看字面是否相同。一个问题的不同改写版本合并，历史保留项重新提出时注明重审，不统计为新增。新旧依据冲突时允许降级，不因旧报告已写过就直接判通过。

本轮主要历史检索范围：sentence-style-chapter04两份记录；english-style-audit、language-style-audit及recheck（9月13日）；source-language-review-results、exhaustive-review-results、supplement-review-results、review-convergence-results（9月14日）；terminology相关记录；此前第四章agent报告。只搜索命中原句不等于发现旧建议，需再读建议内容及状态。

## 当前建议入口

|编号/位置|处理|查重结果|
|---|---|---|
|C4-S1，43行|建议：using HI1 consistently yields；全文改前/改后见第二轮记录|已有第二轮建议，本轮不新增|
|C4-S2，66行|建议：median standard deviations of the late-stage loss|**与9月13日G3重复**。旧方案拆两句，新方案仅展开修饰关系；采用一个即可|
|C4-S3，170行|建议：ability to capture complex degradation patterns|已有第二轮建议，本轮不新增|
|C4-V1，73行及表4-1|新增可选：超参候选范围采用search space|本轮所查历史未发现相同替换建议；详见下文|
|C4-S4，初始化比较段首句|第四轮新增低优先可选：用表作比较主语|详见第四轮记录，不作为语法错误|
|C4-R1，154/158行|第四轮补入旧项：普通综合表现采用overall|whole-manuscript-review.md:178已有，不计新增|
|C4-S5，50行|共享of修饰对象，减少同一模型的重复指代|句内结构专项新增建议|
|C4-S6，41行|HI1来源改为which插入说明，明确单数附着|句内结构专项新增低优先可选，不是语法纠错|
|C4-S7，7行|MAE不额外加重大误差权重，与RMSE说明平行|逐节审查新增低优先可选；详见逐节报告4.1|
|C4-S8，154行|performs better in误差指标→achieves lower，明确数值方向|逐节审查新增低优先可选；详见逐节报告4.6.1|

前三项完整内容见 [第二轮记录](sentence-style-chapter04-secondlook-2026-09-16.md)。没有将此前三项重新包装成第三轮的新发现。

## C4-V1：超参数候选范围与SL的search space对齐——新增可选

位置：chapters/chapter04.tex:73，tables/table_4_1.tex:3、7。表格仅为核对对象及提出联动建议，本轮未修改。

现有英文：
> Their configuration ranges are listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges.

建议英文：
> The hyperparameter search space is listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within this search space.

若采纳，表格一起采用：

- 表题：`Hyperparameter configuration range of MS-AgentNet.` → `Hyperparameter search space of MS-AgentNet.`
- 表头：`Configuration range` → `Search space/Values`。

中文核对：原意是各参数的可选配置范围，并在其中选择超参；表内确实列离散候选值（0.001/0.01，1/2/4/8，16/32/64/128）。search space对应允许选择的候选集合，不改变数值、训练/配置电池角色，也不改变已选模型配置。

范文原词及完整语境：SL full.txt:1260–1286表6题名含 Hyperparameter grid search space，表头为 Search space/Values；1294–1338上下文说明先选择、后固定配置。本文借用search space/Values，不添加grid。JE:1208–1226明确predefined hyperparameter values及grid search；BMS:1867–1903、1930–1947用组合及超参设置说明候选与评价，两篇并没有要求任何候选列表都必须叫search space。

范文是否也如此/同条件：三篇都区分候选值和选定配置，与本文是同类超参选择功能。但JE/SL明确grid search，本文本段未声明穷举，因此不能照搬完整方法名或声称评价全部组合。configuration ranges原文可理解，故只列为优先复用范文词汇的可选项，不报术语错误。

表达收益：将“参数配置”与“供选择的候选空间”区分，正文、表题、表头统一使用一个对象名。不是把全文所有configuration换成search；已选定的configuration继续保留。

## 本轮识别的重复候选及处理

|位置/候选|历史出处|本轮结论|
|66：median late-stage loss standard deviations|english-style-audit-2026-09-13.md，G3|已与C4-S2合并；纠正第二轮新旧属性|
|152：As shown…compared with…adding…|同文件C4；第一轮第四章记录已有撤回；第二轮agent也讨论|旧项可选句式，不列新增。范文本身同时使用动作主语及模型主语；任何重写都应保留M1比较基准|
|94：local deviations / lead to tracking error|source-language-review-results及exhaustive-review-results（9月14日）|旧对象澄清候选；不是新的范文词汇遗漏，不擅改成容量恢复或膝点|
|105：more continuous → smoother|上述9月14日记录|不采用：连续程度和平滑程度不是同一概念，不能仅凭范文用smooth替换|
|105：maintains close agreement → predictions closely follow|build/ch4-results-review-20260916.md已对照并保留|重复检查，原表达自然。JE:2895–2912虽有closely follow但属于RUL容量曲线，不能当作更优SOH模板的充分证据|
|123：represents degradation trends → fits…|source-language-review-results-2026-09-14.md|旧可选，不重复计数，不把表征含义自动缩成拟合|
|135/137：continuously → at each successive ratio|9月14日同类记录|已有四档上下文限定；旧精确化候选，不报新的力度错误|
|156：held fixed → retain RAA|9月14日同类记录|旧结构/权重对象澄清；此处四变体已消歧，不升级为确定冻结误译|

## 力度与形容词检查

本轮新增保留证据：SL full.txt:258–261的CALCE数据集完整条目直接采用 `rapid non-linear degradation tail`，后接寿命后期和加速老化说明。因此 `backtranslation-audit-2026-09-13-results.md` O2 中“未找到完整搭配”的疑虑可由该证据撤回。本文105/107/158行的 `nonlinear degradation tail` 不属于未复用范文词汇。SL此处描述CS2，本文部分段落描述CX2；证据只支持表达搭配，不证明不同电池的曲线事实，不移植其diving称谓。

- 107行only与中文“仅”一致，具体数值与比较对象存在，不因范文用词强就删除或强化。
- 96/109行high/good/low来自中文评价；不自动换为superior、excellent、significant。
- 149行may weaken保留可能性；158行is consistent with / supporting保留设计目标支持，不能改为prove或唯一因果。
- 125行负R²及迁移困难已明说；不因降幅大而改成成功解决跨域迁移。
- 172行potential for lightweight applications符合中文“应用潜力”；SL的硬件可行性、时延及安全推断不移植。
- show/indicate/suggest/maintain/achieve/yield需按对象和力度用，不能因希望词汇一致而全篇换成一个动词。

本轮结论：新增1项可选词汇对齐建议；合并已有建议，记录重复候选和保留理由。没有新增需要强制加强/削弱的力度问题。此为限定材料与范围下的审查结果，不承诺绝无遗漏。

分视角证据记录：build/ch4-round3-lexical.md、build/ch4-round3-syntax.md、build/ch4-round3-strength.md。

## 第四轮补查：普通综合表现与指标名分开（旧项补入）

本轮继续读第四章引导/设置句、消融比较及资源描述；一名agent独立复核1–85行，主代理核对后半及历史来源。不将本轮定向检查称为新一轮三人独立全文审查。

### C4-R1：combined performance / combined results → overall——旧项可选

来源：`whole-manuscript-review.md:178` 已提出同一建议；此次补入总台账，不计新发现。

154行现句：
> Overall, the full model provides more consistent combined performance than the single-module variants, showing the complementary roles of multi-scale local feature extraction and cross-position information interactions.

建议句：
> The full model provides more consistent overall performance than the single-module variants, showing the complementary roles of multi-scale local feature extraction and cross-position information interactions.

158行现句：
> Thus, retaining both small and large kernels provides more consistent combined results than using a single scale, supporting the multi-scale DSConv design.

建议句：
> Thus, retaining both small and large kernels provides more consistent overall results than using a single scale, supporting the multi-scale DSConv design.

中文保真：两处均为普通“综合表现/综合结果”，不是定义一个新的组合运算。overall表达总体结果；154句首Overall的概括功能移入overall performance，避免重复。保留更一致、单模块/单尺度比较对象、互补及支持力度，不改数字。

范文依据及尺度：本轮重读JE full.txt:3493–3533消融完整语境，3514出现overall performance，3515–3517给出组合后更一致的准确性；另读2877–2893，2888使用overall results。BMS:1670–1700按多个资源及精度指标概括综合表现；SL:2288–2332区分单模块和combined gain。因此三篇允许combined描述组合效果，原句不是硬错。本文这两处中文强调总体表现，overall可更明确，属于可选搭配对齐。

范围约束：全文的 `combined average error` 作为既有指标名保持；不能批量替换combined。本文前句已经交代模块组合，改overall不删组合事实。也不能从SL的combined gain引入超加性、唯一机制或更强因果。

其他本轮校准：`convergence behavior`虽为SL full.txt:1234原词，但本文“late-stage convergence state”描述末20轮的状态，不必全部替换为过程行为；正常的表引导被动句也不自动视为错误。

### C4-S4：初始化比较表直接作主语——新增低优先可选

定位：第四章初始化比较段首句（本轮当前文件约63行，以原句定位为准）。

现句：
> The comparison of three initialization schemes is presented in \cref{tab:4-3-initialization}.

建议：
> \Cref{tab:4-3-initialization} compares the three initialization schemes.

中文原意：三种初始化方案的对比结果如表所示。建议用表作主语、compares作动作，直接指出三种比较对象，减少comparison + is presented的名词化被动。表内实际列三种初始化；不改数值、指标、比较结论或段落划分。

范文完整语境：本轮重读JE full.txt:1946–1968及1884–1893，1960以Table 7 shows引出比较指标；BMS:1927–1947，1938以Table 8 presents引出超参表并解释各列。SL:1451–1479也有As presented in Table 9, the comparison reveals，说明原句同类结构并非不合范文。三个例子比较的实验不同，只借表引导功能，不声称三篇比较了本文的三种初始化。

判断：有轻度直接性收益，列可选，不能升级为“词汇简单但严重绕”。也不因此把所有is presented in批量替换。查重命中原句快照，但本轮检索未发现历史明确提出这一个表主语版本；与初始化删尾、S2统计修饰和R1整体表现并非同一问题。

第四轮小结：新增1项低优先风格选项，补入1项历史可选（涉及两句），其余已知项不重计。`small parameters`在标准差0.02及同段parameter magnitudes语境中指幅值，改写with small magnitudes收益不足，保留。已读取分审记录 `build/ch4-round4-setups.md` 并核对证据；未改论文、未编译。

## 句内结构专项：of、关系从句、介词及形容词

本轮根据作者新增要求，主代理核对并列of关系及形容词，一名agent通读第四章检查关系从句/分词附着。重新读取JE full.txt:1884–1893、1946–1968、3315–3335、3826–3842，BMS:1233–1249、1344–1368、1991–2007，SL:1231–1241、1316–1330、2058–2075。跨栏段落按实际功能续接，不把提取顺序视作作者句法。

### C4-S5：两个并列对象共享同一个of限定——建议

位置：chapter04.tex:50。

现句：
> To further examine the training stability of MS-AgentNet and the parameter settings of the lightweight model, this study analyzes agent matrix initialization, model convergence, and hyperparameter configuration.

建议：
> To further examine the training stability and parameter settings of the lightweight MS-AgentNet model, this study analyzes agent matrix initialization, model convergence, and hyperparameter configuration.

理由：MS-AgentNet与the lightweight model指同一模型。将training stability与parameter settings并列，共享of the lightweight MS-AgentNet model，减少重复指代；lightweight仍修饰model，未把“轻量化”限定到参数设置或训练稳定性。保留目的、三个分析项目和原顺序。这是词汇简单但表达有可减少重复的局部改善，不是原句语法错。

范文依据/尺度：JE full.txt:3329–3333以effectiveness and efficiency of the proposed model组织两个评价维度的共同对象，属于同功能实验导语；SL:1231–1236以同一模型的初始化和收敛行为并列介绍；BMS:1344–1351也并列评价对象，但其后同时使用多个of，说明不能机械删除所有重复介词。此处改动成立的关键是本文两次指向同一模型，而不是of数量。

中文核对：“MS-AgentNet的训练稳定性及轻量化模型的参数设置”，其中模型同一。没有删除轻量化或改变参数的技术身份。历史检索命中原句快照，未找到同一共享of改法；不与S2的统计量of展开混算。

### C4-S6：将HI1来源作为which插入说明——低优先可选

位置：chapter04.tex:41，第四句。

现句：
> These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet.

建议：
> These HIs and the CCCT indicator HI1, which is obtained through group-level selection, are separately fed into MS-AgentNet.

理由：长复合主语中，which is明确以单数HI1为先行词；两个逗号把“组级筛选所得”作为来源补充，之后返回整组主语的are fed。三项HIs来自Cell1筛选，HI1来自组级筛选，关系保持。原句就近附着也能读懂，因此只列低优先可选；不要求为了出现which而增加从句。

范文依据/尺度：JE full.txt:1888–1891用CVT feature, extracted using …, consistently achieves …，同为特定HI来源的插入说明。JE采用省略关系词的分词形式，不应谎称它原句使用which。本文复合主语较长，显式which is用于突出仅修饰HI1，是有理由的适配。BMS:1359–1368用which are测量从句插在指标名与主干之间；JE:3829–3840用which补充基线属性；SL:1326–1330也用which说明模块作用。后几例仅支持说明性从句功能，不代表本文需要追加其测量或机制事实。

不同时采用另一个“, obtained through …,”版本；与which版是同一问题，不分开计数。历史原句快照未见这项明确改写建议。

### 已逐例核对的关系从句：保留

|位置|现有结构|指代/作用及处理|
|---|---|---|
|41|inputs that remain stable across cells|that限定要识别的输入；不是陈述所有输入均稳定，保留|
|54|a static learnable matrix … that is independent of the input and used for…|两个并列谓语均修饰矩阵；定义性质，不为模仿which改变句法层次|
|65|the first epoch at which the training loss falls below…|at which对应epoch的时间位置，不能换成裸which；保留|
|94/105|cells, whose degradation trajectories…|whose明确轨迹属于哪些电池；which不能直接取代所有格关系|
|107/158|CX2_38/CX2, which shows/has…|补充该电池/数据集退化特征，先行词明确；保留，不能移植范文的具体电池现象|
|166|Operation counts obtained using… / time needed to…|分词修饰计数、时间，主干及对象清楚；补which只会增加词数，保留|

### 介词关系：按对象使用，不按范文出现频率替换

|结构|本文实例|判断|
|---|---|---|
|of：归属/组成/统计对象|representational ability of the same HI；standard deviation of the loss|S2展开统计对象，S5合并重复对象；其余并非of越多越好|
|for：用途/评价对象|inputs for SOH estimation；results for Cell2--Cell8|任务用途与结果对象明确，保留|
|in：内部/阶段/维度差异|loss fluctuations in the late training stage；differ in battery chemistries|保留，不能一律改成on或across|
|across：跨多个成员的范围|accuracy across cells；performance across datasets|保留；不改为只在单个数据集内部的in|
|with：伴随数值/模型配置|with a mean of 0；with a sequence length of 5|保留，与BMS/JE的配置及资源数值句同功能；不能当冗余介词删除|

### 形容词逐对象校准

|位置/搭配|结论与依据|
|---|---|
|63 similar prediction performance|similar修饰性能接近，不是等效性声明；BMS:2000有similar performance。SL:2060采用comparable RMSE不构成本文必须换comparable的理由|
|94 relatively smooth trajectories|smooth修饰轨迹，relatively保留中文“相对”；不移去修饰预测精度|
|105 more continuous trajectories|旧待解释项，连续性不是平滑性；不借SL smooth linear decay擅改smoother|
|61/63 small parameters|前后分布及magnitudes已表明幅值小，不指参数量少；保留，不换lightweight parameters|
|43/45 high accuracy / high correlation / stable input|精度、相关性、跨电池输入稳定性分别修饰不同对象；JE同时用high correlation与strong correlation，不强制所有high换strong|
|149 fine-grained local degradation information|fine-grained/local修饰信息粒度与范围；不因范文有global或long-term而替换对象|
|154/158 consistent overall performance/results|沿用C4-R1旧项可选；consistent不改成统计方差意义的stable，不替换combined average error|
|172 good balance / lightweight applications / resource-constrained BMS|三个形容词各有明确对象与中文支持；不升级为optimal balance或已部署结论|

专项结论：1项共享of建议、1项which插入说明的低优先可选；其余从句和形容词给出具体保留理由。没有发现需系统提高形容词力度的依据。未改正文、未编译。

## 第四轮继续复查

两名 agent 分别复查前半与后半，主代理重新检查章首、指标、模型比较、迁移及新候选相关范文语境，并审查历史出处。仍只写记录、不编译、不改正文。

覆盖核对：当前第四章44个文字段（包括公式引导与符号解释）的起始行为1、5、7、9、11、13、15、37、41、43、45、50、54、61、63、65、73、75、79、85、90、94、96、103、105、107、109、117、119、123、125、132、135、137、145、149、152、154、156、158、166、168、170、172。该清单用于避免跳段，不意味着公式或数字另做了计算验证。早期记录把初始化/收敛段写作62/64/66，目前为61/63/65；定位以原句为准，编号不随行号漂移重复建立。

### 收敛统计前半句：再次命中旧建议

现有 `The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively`，曾考虑展开为 `The convergence threshold epoch has a median of 26 on Oxford and 7 on MIT`。

准确历史出处是 `language-style-audit-2026-09-13.md` 的 C04-L065（约625–646行），以及 `language-style-recheck-2026-09-13.md` 相应记录。不是 english-style-audit 的G3：G3仅展开后半并拆句。该差别已核实，避免错引。

处理：不新增编号，归入C4-S2同一统计句的旧可选呈现方案。前文已定义 convergence threshold epoch，因此不认定该复合名称本身错误；当前最小方案仍可只展开loss SD后半，不强制合并所有历史改法。

### 消融导语目的前置：保留项重审，不新增建议

位置：145行。

现句：
> Ablation studies and complexity analysis are conducted in addition to the main comparison experiments to further evaluate the effectiveness and efficiency of MS-AgentNet.

本轮曾考虑：
> To further evaluate the effectiveness and efficiency of MS-AgentNet, ablation studies and complexity analysis supplement the main comparison experiments.

JE full.txt:3330–3335及SL:1451–1462确实先给目的再交代消融；BMS:1344–1351在效率实验中也使用目的与设置说明。但它们不要求所有实验导语都固定目的前置。本文以本节实验类型起句、随后说明目的同样清楚。备选将conducted换为supplement，不显著改善动作的具体性；中文“主比较基础上”的关系原句已保留。

最终保留原句。此处已在第一轮及round3-syntax中被检查，不以首次写出另一改句为新增问题。

### 指标名与词汇复用的反查

本批重读BMS full.txt:1233–1249、JE:1140–1146、SL:1199–1205：BMS采用Root Mean Squared Error，JE/SL采用Root Mean Square Error。本文root mean square error有直接范文支持；不能只看BMS版本便再造一次全篇替换。三篇的指标解释粒度不同，不据最短范文删中文已有的解释，也不借SL添加安全后果。

第四轮结果：新增正式建议0项。保留现有C4-S1–S3及可选C4-V1；补充了重复出处、44段覆盖与候选撤回理由。不是撤销已有建议，也不代表宣告绝无遗漏。

其他反查记录：`ordinary normal initialization`中的ordinary承担与截断正态对照的作用，删除它是9月13日旧可选，不重报；更不能替换成可能改变分布含义的standard normal。章首`provide a comprehensive evaluation`动作化是9月14日旧S4，JE实验总述本身有类似名词化收束，保留。172行`the closest model`补为closest storage size曾在9月13日明确撤回，本段对象已清楚，不重复加入。

子审：build/ch4-round4-front.md、build/ch4-round4-back.md。
