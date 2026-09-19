# 第三章范文词汇与表达审查 — 2026-09-16

当前状态：作者随后明确回复“修改”，已按最终清单实施C3-R1—R5共5组6处，并同步中英对照英文；按作者要求未编译。下方各审查轮次的“未实施”是当时状态，最新实施记录见文末。中文源稿未改。

## 本轮结果与查重修正

主代理通读第三章并核对中文，两名agent分别检查3.1–3.2和3.3，主代理重读三篇对应上下文后复核。这是分工加主审复核，不是三人各自独立完整审查全文。

本轮没有确认新的明确术语或表达错误。此前回复中的1处局部分支拆句候选，经历史查重发现属于LS-M07旧项，不应当作新增遗漏。记录保留，但不恢复旧建议的优先级，也不自动实施。

## 后续每批必须执行的检查

### 1. 范文对应词汇是否遗漏

- 先辨认相同技术对象和段落功能，再检查范文中的专业名词、固定搭配、动作动词和修饰语是否适用而未采用。
- 同时查本文前后是否对同一对象使用多个版本；不同对象即使字面相近也不能强并。
- 每项记录“范文原词—本文对应表达—完整上下文位置—适用条件—已复用/可替换/合理不同/待核”。不以关键词命中代替语境核实。
- BMS主要参考局部—全局建模、卷积、注意力、计算与资源指标；SL主要参考轻量化；JE主要参考HI工程。三篇交叉核对，不排他。

### 2. 对应句子与表达是否学到

- 主语是否明确、主干是否过晚；谁对什么执行什么操作，输出是什么。
- 动词—宾语搭配、名词化与介词链、形容词和副词是否自然且必要。
- 从句与停顿、指代、句间推进是否比同功能范文更绕；简单词并不自动代表直接表达。
- 目的、方法、结果和解释是否各有合适力度；may/can、approximately、only、significantly及比较范围是否与中文和证据一致。
- 检查范文是否也采用相同长句、被动、概括或省略。范文同样如此且本文可消歧时，保留或列可选，不制造错误。
- 保留全部技术信息、条件、顺序、段落边界和已确认术语。范文有某词不等于本文必须使用，更不能借词引入新机制或更强结论。

### 3. 持续查重与状态管理

每批先读取当前正文，再查历史候选及其修订/实施记录；提交前再次按“位置或句子锚点＋技术对象＋问题实质”查重，不只比较编号或建议措辞。历史行号可能漂移，以句子和对象确认。

统一状态：新增待确认、旧项补充依据、已实施后保留、可选未实施、撤回/被后续修订替代、待核实。旧项新增证据仍沿用原ID；换一种改写不能算新问题。已解决项不重复列入待改清单；复发必须展示当前文本证据。第一章已完成不重开，B类及已知图内命名不重复提交。

每批结果分别报新增数、旧项复核数和保留范围。不能因重复检查得到相同候选就声称发现新遗漏，也不能把“本轮未发现”写成绝对无遗漏保证。

## LS-M07：局部分支句 — 旧项复核，可选，不计新增

当前位置：chapters/chapter03.tex:108，第二句。

现有英文：
> The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

本轮曾提出的可选英文（未实施）：
> The local branch applies layer normalization to $\mathbf X_S$ and passes the normalized representation to the fusion stage. This representation is then combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.

中文原意：局部分支对XS层归一化后传至融合端，与RAA分支建立的跨位置上下文融合，形成局部特征与全局信息的互补表示。

原因：词汇简单但后半句动作主体切换，可用明确主语减轻where/it回指；全部对象、顺序和互补含义保留，句数变化不改变段落。然而当前normalized representation已使对象明确，拆句收益有限。

历史对应：
- language-style-audit-2026-09-13.md:398–418：LS-M07最初已提出拆句。
- language-style-recheck-2026-09-13.md:264–282：后续修订为仅将passes it明确成passes the normalized representation，并明确“不必为此拆句”。当前正文已包含该对象澄清。
- language-style-reference-reasons-2026-09-13.md:99–119：继续记录同一对象澄清依据，并列可选。

本轮范文尺度校准：SL full.txt:1015–1039（PDF第9页§4.3.2）区分局部分支与融合结果，可参考对象切换时的明确承接；BMS full.txt:880–886（PDF第7页§3.2.2）依次介绍模块动作与计算成本，但自身也有长句；JE full.txt:907–945及对应PDF第8页逐步介绍扩展、卷积和残差，亦使用长句和被动。范文没有要求该句必须拆分。只借表达路径，不借SL的rank-1/full-rank结论。结论：保留当前正文也合适，不将历史拆句提案重新升级。

## 第三章对应词汇、句式与力度覆盖记录

以下是本轮重新读取的对应语境定位，行号以当前full.txt为准。双栏错序处按PDF或明确连续段落核对，不把相邻异栏文字串成句子。

| 本文位置与功能 | 对应词汇、表达及范文依据 | 本轮判断 |
|---|---|---|
| 3.1 输入—模块—输出 | fed into、passes through、layer normalization、residual connection；BMS 736–749，JE 615–630 | 流程及动词已直接；被动输入链符合范文，不需统一改主动 |
| 3.2.1 标准卷积和DSConv | depthwise/pointwise convolution、computational cost、fuses features across channels；BMS 772–823，JE 674–701 | 对象、通道内/通道间动作已对齐；计算成本、负载和训练时间不强行合并 |
| 3.2.2 双重作用 | locality bias、local branch、locally enhanced representation；SL 861–891、1024–1039，BMS 880–886 | 已有对应词汇；Input Enrichment、Rank Restoration不能整套照搬，因为本文Q/K/V来源及两agent结构不同 |
| 3.2.2 通道与流程 | channel expansion factor、expands/restores、applied to introduce nonlinearity；JE 907–945及PDF第8页，BMS 880–886 | 动作对象明确；不必把自然的factor of two/three改成double/triple expansion factor |
| 3.2.3 大核 | follows、extract、pointwise convolutions、computational cost；BMS 825–829、903续段，SL 905–928 | 位置、核大小、通道扩展和较长尺度保留；不借SL加入aging inertia或抑噪结论 |
| 3.3.1 多头与投影 | representation subspaces、learnable linear projection matrices、concatenated；BMS 888–954，JE 582–590、647–649 | 已采用相应名词和流程；不把channel scaling误称linear projection |
| 3.3.2 Softmax与线性注意力 | similarity scores、attention weights、kernel function、associative property、maps/rearranges/avoids constructing；BMS 981–1044，SL 910–919 | 对象和动词已清楚；分数与权重保留区别，不因同义表面差异反复更名 |
| 3.3.3 聚合与广播 | agent/context aggregation、information broadcasting、gather/read/convert；SL 930–953、964–1007 | 相同操作层词可复用；Gated Broadcasting属不同机制，不是本文漏用的专名 |
| 3.3.3 ReLU²动机 | positive scores、common positive scaling factor、uniform distribution | 为本文特有数学条件；不能用范文ReLU叙述替换ReLU²、删除正尺度或回退条件，不能借JE增加物理可解释/抑噪结论 |
| 3.3.3 复杂度与融合 | computational/memory complexity、fixed、linearly、preserves/combines；BMS 1064–1069，SL 1020–1029 | 条件—复杂度—融合结果清楚；不将理论复杂度改成已证实际延迟收益 |

力度补查：3.2.1的may对应过拟合可能性；3.3的approximately/only保留参数比较限定；lower、linear限定在对应计算对象和固定量条件内。没有发现仅为模仿范文而必须新增的形容词或强化词。3.3.2的at a lower computational complexity可作轻微介词润色，但不是术语错误，不列核心待改项。

本次正式登记：新增明确问题0项；旧项复核1项（LS-M07）；其余上述范围保留。此结论仅覆盖本轮第三章语言与范文对齐检查，不代替实验、代码或图内名称核验。

## 第二轮：三名agent各自完整复查第三章

作者追问“确定吗”后要求多个agent复查。本轮三名agent分别以BMS、SL、JE为主参考，各自完整读取第三章中英文并交叉三篇模型方法语境；先形成候选，后查询历史记录。主审独立核对当前句子、中文及范文，再对候选作交叉裁决。它比上一轮分工覆盖更完整，但使用既有agent，不宣称完全无历史背景的盲审。

本轮不能只回答“没有明确错误”：按作者要求的范文词汇复用尺度，确有值得补充的可选对齐提案。最终保留4组、5处供确认：C3-R1两处、C3-R2一处、C3-R3一处、C3-R4一处。其中R4是已有词库映射补充；R2的搭配也已存在引言词库，本轮新增的是第三章具体应用。不是发现5处错误。以下全部未实施。

定位说明：本节范文行号按实际换行符（与rg/编辑器一致）计算。早前部分Python splitlines计数将PDF换页符也算行，可能产生行号偏差；以本节段落锚点和当前行号定位，不将此误称文件并发变更。

### C3-R1：用decompose表达运算分解 — 新增可选提案，两处

**3.2.1，第68行。**

现有英文：
> Unlike standard convolution, depthwise separable convolution (DSConv) divides convolution into two stages: depthwise convolution and pointwise convolution\cite{ref71}.

建议英文：
> Unlike standard convolution, depthwise separable convolution (DSConv) decomposes convolution into two stages: depthwise convolution and pointwise convolution\cite{ref71}.

**3.3.3，第275行，第一句。**

现有英文：
> Agent Attention uses a small number of agents as information intermediaries to divide global interactions between sequence positions into context aggregation and information broadcasting\cite{ref46}.

建议英文：
> Agent Attention uses a small number of agents as information intermediaries to decompose global interactions between sequence positions into two stages: context aggregation and information broadcasting\cite{ref46}.

范文依据：JE full.txt:808–817完整标准卷积局限—DSConv分解段，813–814直接使用decomposes … into two steps；BMS:814–817及839–841分别以separates和breaking … into a two-step process说明同一运算分解；SL:903–912引出agent变体后写The computation is decomposed into two … steps，其聚合和广播分别见923–927、956–973。三篇均以具体运算和阶段说明机制。

中文核对：第68行“将卷积运算分解为……两个阶段”；第275行“以少量智能体作为信息中介，将序列位置之间的全局交互分解为……两个阶段”。动词decompose与两处“分解”对应；第二处明确two stages后自然承接原下一句first/then，未添加新操作。保留原to结构，明确agent作为分解交互的中介，不必为主动句改成and另起并列动作。

尺度与查重：divide本身正确；此项是适用范文原词的复用，不是纠错。未找到同位置同替换的历史提案；相同词并不要求全文所有divide/split都替换，维度划分仍用split/divide。

### C3-R2：明确两两计算的对象为相似度 — 第三章新增应用

位置：3.3.2，第242行第二句。

现有英文：
> However, $\mathbf Q_i\mathbf K_i^{\mathrm T}$ requires pairwise calculations between all queries and keys, forming an $N\times N$ attention score matrix.

建议英文：
> However, computing $\mathbf Q_i\mathbf K_i^{\mathrm T}$ requires pairwise similarity calculations between all queries and keys, forming an $N\times N$ attention score matrix.

范文依据：JE full.txt:755–762复杂度引段及QK计算句直接使用pairwise similarity computation between all queries and keys；BMS:974–985同样写computing the similarity between all query-key pairs；SL:903–912只概述Softmax二次复杂度，没有要求每次都展开similarity。因此原句已有上下文支撑，并不构成漏译。

中文核对：“需要计算所有查询与键之间的两两关系，并形成……注意力矩阵”。这里确为QK点积相似度计算，similarity与前文已确认的similarity scores一致；computing让计算操作作主语，矩阵仍为计算结果。未改变归一化、矩阵大小或后续复杂度。

尺度与查重：introduction-vocabulary.md:216已收录pairwise similarity computation；本次为该搭配在第三章相同计算对象上的具体应用，不称全新发现一个范文词。旧B类分数/权重修订保留，本项不重开矩阵名称。

### C3-R3：定义矩阵时直接命名aggregation weights — 新增轻度可选

位置：3.3.3，第329行。

现有英文：
> where $\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$ contains the weights used by the agents to aggregate information from each sequence position, and $\mathbf V_{A,i}\in\mathbb R^{n_a\times d_h}$ is the resulting agent context.

建议英文：
> where $\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$ contains the agents' aggregation weights for each sequence position, and $\mathbf V_{A,i}\in\mathbb R^{n_a\times d_h}$ is the resulting agent context.

范文依据：BMS full.txt:883–890直接用attention weights命名计算量；SL:923–927、986–989明确agents聚合context的动作。JE的注意力式解释也直接命名计算量，但三篇对应语境未定位到完整原词组agents' aggregation weights。因此本句是借鉴定义表达路径、根据本文对象适配，不是范文原句或完整搭配照搬。

中文核对：“智能体对各序列位置的聚合权重”直接对应建议；agent、序列位置、两矩阵维度和聚合上下文均保留。前句和公式已交代聚合计算，本句功能是定义矩阵内容，因此名词aggregation weights比weights used by … to aggregate更直接，并与下文broadcasting weights呼应。属于轻度的“词汇简单但绕述定义”，原句仍清楚。

尺度与查重：未定位到历史同句同改写提案；三篇也用解释性从句，不要求所有定义都压成名词。此项收益小于直接原词对齐，列较低优先级。

### C3-R4：additive fusion — 已有词库映射补充

位置：3.3.3，第384行。

现有英文：
> This additive connection preserves the local degradation features extracted by DSConv-S and combines them with the cross-position context established by RAA, forming a joint local-global representation while maintaining linear computational complexity with respect to the sequence length $N$.

建议英文：
> This additive fusion preserves the local degradation features extracted by DSConv-S and combines them with the cross-position context established by RAA, forming a joint local-global representation while maintaining linear computational complexity with respect to the sequence length $N$.

范文依据：SL full.txt:1012–1021在两路相加式后使用This additive fusion integrates …。已核对PDF第9页融合段；借用的是加法融合操作名，不借rank-1、full-rank、aging inertia或其性能结论。BMS和JE也使用connection描述残差，但本文此处专指局部—全局两分支融合，fusion与当前功能吻合。

中文核对：“这种加性连接……融合……形成局部—全局联合表示”。前接公式确实为两分支相加，使用“加性融合”没有改变连接方式、技术对象、力度或线性复杂度范围。其余整句不动。

尺度与查重：section-expression-vocabulary.md:64已收录additive fusion并限定“仅当实际相加”；旧M03-070保留了当前句。此次是把已有词库词用于对应正文，列旧知识的应用补充，不计为新发现词汇，也不把旧保留结论改说成错误。

### 本轮筛除或保留的候选

| 候选 | 历史/语境复核 | 裁决 |
|---|---|---|
| L1命名长句/which或改is designed to | LS-M05及reference-led-2026-09-14-bms.md已有建议；范文也直接陈述功能 | 旧项，不再提供竞争版本；不能仅凭“用于”判成夸大 |
| L108局部分支拆句 | LS-M07已从拆句修订为明确normalized representation，当前已落实 | 保留；不重复计新增 |
| L104 compact修饰卷积还是kernel | SL原词compact kernel size，但本文1×5 depthwise convolution同样清楚 | 收益很小，保留 |
| L242第一句改Softmax exponentiates and normalizes… | BMS支持机制作主语，也正常使用exponential function等名词 | 原句主语和结果关系明确，不把所有动作名词化判错；保留 |
| L288 QKV比较主干后置 | approved-translations.md:186–193已有单独批准；比较对象与approximately/only清楚 | 保留，不重开 |
| L347增加weighted sum | supplement-review-methods-2026-09-14.md:24已明确核查并保留weights…combine | 撤回agent最初“新增”判断；旧项，已有权重及公式足以表达加权 |
| Input enhancement改Input Enrichment | SL有Enrichment，BMS有enhance输入的对应语境 | 两者均可，仅借标题不必然带入机制；但本文已一致，收益不足，保留 |
| relative ratios/at a lower complexity | 轻度冗余或介词偏好，不是技术名词遗漏 | 保留，不扩大清单 |

### 覆盖与力度复核

三名agent均覆盖L1–46架构、L52–100标准/深度可分离卷积、L104–185双尺度、L191–265通用及线性注意力、L267–311 RAA动机、L313–363聚合广播及复杂度、L367–384融合。不是仅检查上述候选句。

may对应过拟合可能性；rapidly/substantially对应中文“迅速/显著”；approximately/only对应参数比较的“约/仅”；fixed、positive、each row及无正分数回退条件均保留。未因模仿范文引入噪声抑制、rank restoration、physically interpretable、实际部署或最低延迟等主张。未确认新的力度错误。新增提案均为动词、计算对象或定义表达调整，不加强结论。

本轮最终状态：明确错误0项；待作者选择的对齐提案4组5处（含已有词库应用与低优先级可选项）；历史拆句/加权说明等不计新增。只更新本审查文档，不改论文、不编译。

## 第三轮：形容词、介词附着与整句表达路径

作者要求继续检查形容词，以及of等介词和对应句子的写法。三名agent分别以BMS、JE、SL为主参考再次覆盖第三章，主审重读三篇架构、卷积、多头与融合相关段落，核对中文和历史记录。重点是修饰关系和阅读路径，不是机械逐词匹配。新增1处较有阅读收益的可选澄清C3-R5；另记录2项低收益候选及保留理由，不把它们计入核心待改清单。

### C3-R5：每个head与计算范围直接对应 — 新增可选澄清

位置：3.3.1，第196行第一句。

现有英文：
> Multi-head self-attention uses multiple parallel attention heads to calculate correlations between features in different representation subspaces\cite{ref34}.

建议英文：
> Multi-head self-attention uses multiple parallel attention heads, each calculating correlations between features within a different representation subspace\cite{ref34}.

中文：“多头自注意力通过多个并行注意力头在不同表示子空间内计算特征之间的相关性。”

原因：原句in different representation subspaces紧跟features，读者可能先理解成不同子空间中的特征彼此计算相关性。建议先点明each head执行计算，再用within说明计算范围。不是把所有in换成within，而是借范文“整体机制—每个head的操作”的整句表达路径，减少修饰关系的回看。多头、并行、不同子空间及特征相关性全部保留，引用及后续公式不变。

范文依据与尺度校准：
- BMS full.txt:882–891，完整多头引介段先写parallel heads，接着用Each head calculates its own attention weights说明每头动作，再解释计算关系。
- JE full.txt:509–516，完整多头流程先写parallel operations，再用For each head说明投影、权重和输出；642–644另明确多个子空间。借用的是逐头交代动作，不新增范文的输出投影等操作。
- SL full.txt:903–912、923–927主要讲单agent变体和聚合，缺少同条件的多头子空间句，不能把其描述当作本改写直接原词来源。
- 当前紧邻Q/K/V投影公式已经能够消歧，故不是已确认的技术错误；范文也有较长修饰结构，不以长短决定对错。

查重：历史language-style-audit-2026-09-13-methods.md的M03-036曾保留整句，未发现这个具体附着澄清提案。本项为旧保留位置的新增可选句式，不称旧错误复发。

### 另两项低收益候选：留记录，暂不列核心待改

**L106：动作化表征说明。**

现有：
> This preceding convolution introduces a locality bias into RAA, improving its representation of local variations during cross-position context aggregation.

可选：
> This preceding convolution introduces a locality bias into RAA, enabling it to better represent local variations when aggregating context across positions.

依据：SL full.txt:855–860及875–884以locality bias引出agent的聚合动作；BMS:868–880用模块执行增强和融合；JE:669–696以卷积算子执行extracts/integrates。建议把representation of和aggregation还原成represent/aggregate，保留前置卷积、RAA、局部变化和跨位置聚合，不借抑噪或秩恢复结论。中文为“增强其……表征”，better保留增强方向。

裁决：另两名agent认为当前of明确表征对象，during明确发生过程，本来清楚；主审同意其改进有限。历史M03-019保留本段，未找到这条具体改写。记录为新增低收益备选，不因用户提到of就要求更换，也不称原句名词化有错。

**L170、185：expanded number of channels。**

现有短语：the expanded number of channels。

可选短语：the number of channels after expansion。

依据：BMS full.txt:832–833、895–896使用channels after expanding说明计算式中的扩展通道；JE:900–918描述channel dimension扩展及expanded feature map；SL对应模块段没有同等粒度的通道计数定义。可选写法把中文“扩展后的通道数”明确写成操作后的状态，两个公式系数和其余定义不变。

裁决：当前expanded也可以合理修饰增大的通道数，已有前文及倍数消歧。三名agent中两名认为收益不足，主审保留原句。历史M03-028/M03-032及M06相关记录不重开；本轮只评价语言，不重新核验或认可历史公式问题。

### of及其他介词：核查后保留的具体依据

| 本文表达 | 介词表达的关系 | 范文对应与保留理由 |
|---|---|---|
| computational cost of standard convolution | 计算成本所属的运算 | BMS:767–789同样把standard convolution与cost相连；of自然 |
| ratio of the computational costs of the two types of convolution | 比值的对象及成本归属 | JE:829–831用ratio between the two complexities；本文两层of仍是直线关系，紧接比值公式，不必为了减少of改写 |
| within each channel / across channels | 通道内处理 / 跨通道融合 | BMS:806–817、JE:813–817及840–842说明同一操作区别；不能统一介词 |
| mapped to a feature space through a layer | 映射目标 / 变换途径 | BMS:735–744、JE:610–623使用embedded in、fed into、processed through，说明介词随谓语选取，不要求逐词相同 |
| over longer time scales from the fused representation | 特征的时间尺度 / 提取来源 | BMS:819–823及SL:898–921介绍大核作用；本文两个限定各有功能，不删来源 |
| pointwise convolutions for channel expansion and restoration | 卷积的用途 | JE:900–938顺序说明扩展和恢复；for正确说明用途，不换成归属of |
| parameter overhead of query, key, and value generation | 参数开销所对应的操作 | 原句对象准确；没有适用证据要求一律改for。维持已确认的channel scaling与linear projection区别 |
| linear in sequence length / grow linearly with sequence length | 系表关系 / 增长关系 | BMS:1016–1026、SL:1019–1021说明随长度的复杂度；不同谓语允许不同介词，不是术语不一致 |
| shared across input samples | 参数跨样本共享 | 由本文中文明确范围，不能为了模仿换成每样本单独学习的含义 |
| weights assigned to agents by each query position | 权重对应对象 / 分配主体 | 两个介词分工明确；SL单agent门控不构成同条件改写依据 |
| contribution of the RAA branch / regularization during training | 贡献归属 / 正则化发生阶段 | 中文对象及阶段均清楚；of与during不需要替换 |

### 形容词、副词及力度覆盖

- compact：SL修饰kernel size，本文修饰明确1×5的depthwise convolution亦可理解；沿用上一轮保留判断。
- learnable linear projection matrices：learnable指参数可学习，linear指变换性质；二者不重复。
- locally enhanced、normalized、fused：分别指局部增强后、归一化后、融合后的表示，不能为统一修饰语而混用。
- independently within each channel：独立处理的范围明确；JE:915–918使用independently operate on each channel，不说明本文必须把within改on。
- common、positive、squared：分别限定共同尺度、正值和平方操作，有数学作用，不删减。
- short local neighborhood、longer time scales：保留短邻域与较长尺度的中文区别；不能一律换成范文的long-term或global。
- rapidly、substantially、may、approximately、only：均核对中文力度与限定，本轮没有新增明确的过强或过弱问题。

第三轮结果：核心清单新增C3-R5一处；L106和L170/185仅作为低收益备选记录。C3-R1—R4保持未实施状态。正文、中英对照和中文源稿未改，未编译。

## 分小节审查01：第三章开头及3.1架构概述

作者要求后续按小节逐句推进。本批重新读取当前英文L1–46、对应中文及三篇架构完整语境。覆盖正文17句（排除标题、步骤标签和公式；i.e.不另分句）。不是重新计入整章既有候选。

本批范文：BMS full.txt:731–746的提案与完整架构流程；JE:610–625的完整架构介绍；SL:812–829、832–836、845–853的阶段说明（按真实步骤识别双栏错序，不把TXT顺序当作模型顺序）。SL和JE的模块、残差位置与本文不同，只参照动作表达。

| 句序/位置 | 实际核查的词汇和表达 | 裁决 |
|---|---|---|
| S1 L1 To address…proposes… | challenges of说明两方面挑战，in限定SOH任务；lightweight与中文轻量级一致。BMS731–734也是目的—提出模型结构 | 保留，不为缩短删掉accuracy或efficiency |
| S2 L1 The name MS refers… | comprising说明由两模块构成；which回指design；efficiently对应高效；over different time scales限定特征提取 | LS-M05旧项，仅可选拆句，不能计新增；comprising不得机械换of |
| S3 L1 The following subsections… | introduce/describe/detail分别对应介绍/阐述/详细说明；三个动词并列，模块名沿用已确认名称 | 保留；BMS763–765及852–857也采用章节预告，不因其存在而删去 |
| S4 L5 The overall architecture… | architecture of表示所属；shown in表示图中呈现；overall对应总体 | 保留，JE610同类直接表达 |
| S5 L5 HI sequences are divided… | divided into为划分结果；mapped to为目标空间；through为线性层这一变换途径；fed into为下一模块输入 | 保留；BMS736–738、JE613–618均采用连续被动数据流，不能机械改主动或统一to/into |
| S6 L5 The Block output passes… | output直接作主语；passes through交代处理链；to produce为所得输出；linear修饰读出层 | 保留；BMS739–742、JE619–623均按中间输出—处理—最终输出推进，不能复制其MLP或多任务输出头 |
| S7 L5 During training… | of the cycle表示SOH归属；immediately following限定紧邻的下一循环；as表示标签角色 | 保留；BMS742–744也写紧随窗口的SOH作为label，不删immediately或改成窗口末循环 |
| S8 L7 Mathematically, let… | input to表示进入第l个Block；where解释B/N/d；feature embedding dimension已与SL818–820一致 | 保留；不能因BMS用input of就强改to |
| S9 L7 The Block transforms… | 具体模块作主语，transforms说明动作，in three steps交代组织方式 | 保留，与SL sequential operations同功能但无须逐字复制 |
| S10 L9 The input is processed… | 先输入后LLGFA，以which uses说明DSConv-S/RAA分工；across positions明确跨位置 | 保留；关系从句对象紧邻；不把本文global interactions一概换成范文long-range dependencies |
| S11 L18 The LLGFA output passes… | passes through…then…明确LN到DSConv-L；over longer time scales保留比较尺度 | 保留，与SL845–848的中间特征经卷积流程相近，时间尺度以中文为准 |
| S12 L18 The DSConv-L output is scaled… | scaled by W_l为缩放因子；added to X'为相加对象；through a residual connection为结构方式 | 保留；by/to/through各有功能，不能一概换with |
| S13 L33 The features are processed… | by LN0 and then FFN交代两个处理算子和先后 | 保留；SL822–825亦以features are processed描述非线性阶段，不能复制其不同残差接入点 |
| S14 L33 The result is added… | result明确指前句处理输出；added to、through、to produce分别为相加对象、方式与输出结果 | 保留；无需把result强行改成另一正式模块名 |
| S15 L46 The output is used… | as说明下一Block输入角色；to next Block说明输入去向；等式消歧 | 保留；output/input正常词语复现有实际作用 |
| S16 L46 W_l is a learnable… | learnable修饰缩放系数；scaling factor已对齐SL833–835 | 保留，不强改BMS weight parameter而改变本文名称 |
| S17 L46 Both LN and LN0… | both说明共同操作，but区分LN0不使用额外scale/bias；additional限定参数配置 | 保留；差异来自本文设置，不因范文未定义LN0删除 |

本节尤其明确：历史language-style-recheck-2026-09-13.md:238已撤销“comprising换of”的建议，因为design comprising two modules表示由两模块组成，而design of two modules可能变成对两个模块的设计。这里是of不能机械模仿的实际例子，不是说of一概不好。

本批结论：17句均核查，新增提案0；LS-M05仍属已登记可选项，当前可保留。不把上一轮3.3.1的C3-R5挪作本节发现。下一批范围为3.2总述及3.2.1。正文未改、未编译。

## 分小节审查02：3.2总述及3.2.1基本结构与成本

本批重新读取英文及中文L50–100；核对两个标题和15个文字句/公式引导单元（where定义和以冒号引公式的完整文字计单元，公式不另计句）。按“标准卷积原理—成本—DSConv分解—成本比”的完整论述推进比较，不只检索原词。

重新读取的范文语境：BMS full.txt:763–789、790–817、839–841（跨页深度卷积句接806行，区分异栏DSConv-L）；JE:739–745、772–793、808–821、840–842、852–867、873–878（剔除异栏注意力复杂度内容）；SL:838–841。三篇都采用运算主体—动作—成本及局限的路径，也使用目的前置、被动、of结构和结果分词，不能仅凭这些形式提出修改。

| 句序/位置 | 逐句核查 | 结论 |
|---|---|---|
| S1 L52 To combine… | combine A with B表达兼顾两个目标；compares its computational cost with that of standard convolution明确成本与成本比较；that of避免重复名词 | 保留；BMS763–765同样先预告结构介绍和比较，无需为了短句删目的或把that of删掉 |
| S2 L52 The configurations… | configurations与respective roles对应结构配置和各自分工；of表示所属；then承接下一步 | 保留；respective承担“各自”，不属于无用形容词 |
| S3 L57 Convolution extracts… | extracts local information from time series说明提取对象和来源；through sliding kernels说明实现方式 | 保留；BMS767–768也用through sliding filters；不用因普通词而强改performs extraction |
| S4 L57 Standard convolution operates… | across all input channels限定跨通道范围；with each kernel producing说明每个核的输出；corresponding to说明输出图与通道对应 | 保留；BMS768–770几乎相同功能结构，JE740–745同样以核产生输出图；with不是多余介词 |
| S5 L57 As the numbers… | 随通道数/核尺寸增加—参数和计算开销增长—负载及训练时间增加；rapidly/substantially对应迅速/显著 | 保留；中文本身包含各层信息，不能因开销/负载接近就擅删。BMS770–772和JE808–812也说明资源负担，不把理论成本改成具体耗时保证 |
| S6 L57 A larger parameter count… | larger是参数量比较；may保留可能性；risk of overfitting是自然名词搭配；on small-sample battery datasets为数据条件 | 保留；SL838–839明确may be prone to overfitting on small-sample battery datasets，不删除may或改为必然 |
| S7 L57 The computational cost… | of standard convolution点明公式所属对象；can be expressed as引公式 | LS-M06旧修复已在当前正文体现，不重新报Its指代问题 |
| S8 L66 where…denote… | kernel size、number of input/output channels、feature map size与四符号分别对应；of表示计数对象 | 保留；BMS788–789同样列定义，不为复用其input channels省掉本文明确的number |
| S9 L68 Unlike…divides… | 先对比标准卷积，再说明DW/PW两个阶段；into为分解后的阶段 | 沿用C3-R1的decomposes可选提案，不新增编号；JE813–814为相同对象的原词依据 |
| S10 L68 Depthwise convolution applies… | separate对应每通道单独配置；applies a kernel to表示施加对象；within that channel限定局部提取在通道内 | 保留；JE815–817亦按每通道独立滤波解释，within与to分工不同 |
| S11 L68 A pointwise convolution then… | then推进第二阶段；fuses features across channels为跨通道融合；adjusts…to为调整后的数量 | 保留；BMS809–817、JE840–842同功能。fuses与combines/integrates均可，不撤销已确认术语 |
| S12 L68 By separating… | separating A from B准确区分通道内提取与跨通道融合；DSConv作主语承担分离动作；dense/cross-channel对应中文密集/跨通道 | 保留；BMS814–817亦以separates说明运算解耦，不为简单词强换更抽象句式 |
| S13 L68 Its computational cost… | Its紧邻唯一主语DSConv，随后即其成本式 | 保留；与旧LS-M06中远距离跨句回指不同，不能所有Its机械展开 |
| S14 L79 The ratio of…of… | 两层of分别表示比值的量与成本所属的卷积类型；后接分子分母明确的公式 | 保留；压成computational cost ratio仅为同义风格选择，不报绕句或遗漏 |
| S15 L100 Equation…shows… | with限定相同通道配置；lower…than明确比较；providing the basis承接后续设计 | 保留语言；show为公式推出关系，不换prove；适用条件不在本语言批次擅自增改，不因极端未采用参数重开历史技术项 |

标题补查：multi-scale、depthwise separable、computational cost均已对应范文。Basic DSConv structure and computational cost comparison为简洁并列标题，不必替换成更长of标题。convolution modules与BMS的convolutional modules属名词/形容词作定语的正常差异，本文已一致，无充分收益要求统一为范文单一词形。

本节较有价值的范文学习仍是C3-R1：将divides convolution into two stages可选改为decomposes convolution into two stages。其余既有自然表达保留。新增候选0，旧候选C3-R1一处继续待确认，LS-M06已解决不重开。下一批为3.2.2 DSConv-S。本轮只追加审查记录，论文和中英对照未改，未编译。

## 分小节审查03：3.2.2 DSConv-S

本批重新读取当前中英L102–170，核对标题、两项功能标签及18个文字句/公式引导单元（不将标签、公式计句，where定义计单元）。重读BMS full.txt:868–880、893–896；SL:855–860、875–884、1001–1031；JE:873–881、900–938。JE的ReLU及第二层PW说明在TXT提取中缺漏，已回查source.pdf第8页左栏，确认扩展→DW→ReLU→第二PW→残差的实际顺序和对应句子，不以TXT空缺认定范文没有该步骤。

| 句序/位置 | 具体检查 | 裁决 |
|---|---|---|
| S1 L104 Small-kernel DSConv-S uses… | compact修饰明确尺寸的卷积；embedded in说明所在模块；before说明先后；global interactions in RAA指RAA内交互 | 保留；SL856–858的compact kernel size/embedded within为可选同功能写法，不强制将in改within；compact旧候选不重开 |
| S2 L104 It serves two roles… | serves明确承担作用，input enhancement与local branch preservation对应中文两项功能 | 保留；SL采用dual purpose及Input Enrichment，但本文enhancement亦对应BMS增强输入语境，不能为复用标题套入Rank Restoration |
| S3 L106 DSConv-S extracts… | extracts信息from输入，to form给出局部增强表示；locally enhanced修饰表示的来源/状态 | 保留；SL1023–1027同样先交代局部增强输出，但本文Q/K/V来源不同，不照抄只增强K/V |
| S4 L106 RAA then constructs… | constructs…from明确Q/K/V来源；performs…through说明跨位置交互实现途径；then为先后 | 保留；agent aggregation/broadcasting已采用范文同功能词，不必换成不适用的gated broadcasting |
| S5 L106 This preceding convolution… | preceding对应前置；introduces…into明确偏置作用于RAA；representation of说明表征对象，during限定聚合过程 | 仍为第三轮已记录的低收益动作化备选，不算新增；当前of/during不误搭 |
| S6 L108 In LLGFA…passed to both… | to标记两个接收分支，both… and…明确并行去向 | 保留；不把局部分支含义泛化成SL的full-rank保证 |
| S7 L108 The local branch applies… | applies LN to XS→passes normalized representation→融合；where/it回指已有明确对象；complementary对应互补 | LS-M07旧项；对象澄清已在当前正文落实，不再次把拆句升级为必要修改 |
| S8 L110 DSConv-S uses a channel expansion factor of two | of two给出因子值；不将两倍通道扩展误写为增加两个通道 | 保留；BMS double expansion factor与JE by a factor of r均支持同一含义，当前自然 |
| S9 L110 The input features are…where… | 输入张量及B/N/d在同句定义，where对象紧邻 | 保留；旧LS-M08已将定义与后续转置分开，不能继续报原Given嵌套问题 |
| S10 L110 The input is first transposed… | first说明顺序，so that说明转置后维度的对应 | 保留；SL845–848同功能明确交换sequence/feature维度，本文表达不需搬其不同符号 |
| S11 L110 The first PW then expands… | 第一PW作主语，expands channel dimension to 2d直接说明结果 | 保留；JE900–903同样以PW执行通道扩展，不必改成更抽象的expansion is performed |
| S12 L122 The expanded features pass through… | expanded修饰操作后特征；which指DW；independently within each channel限定独立处理；short local neighborhood对应短邻域 | 保留；JE915–918使用expanded feature map/independently operate on each channel，within/on不必逐字相同 |
| S13 L131 A ReLU activation is then applied… | applied to introduce nonlinearity明确激活与作用；then承接 | 保留；JE PDF第8页左栏直接采用同功能句，不能因被动而强改主动 |
| S14 L139 Next, the second PW fuses… | fuses across channels表示跨通道融合；restores…to d为恢复后的维度；Next说明第二PW位置 | 保留；JE PDF第8页写第二PW将维度恢复原尺寸，BMS877–879写两层PW融合多通道；本文fuses features为已确认表述 |
| S15 L148 Finally, the output is transposed back… | back to original arrangement表示恢复排列，combined with input表示残差对象，through为连接方式 | 保留；BMS739–740同样使用transposed back；不从JE复制中文未写的梯度/训练稳定性作用 |
| S16 L159 where PW…denote… | for channel expansion/restoration为用途；两个respectively各自对应一组符号；transpose/inverse transpose分开定义 | 保留；列举虽长但逐项映射清楚，不为缩短删符号或合并两个respectively |
| S17 L161 With a channel expansion factor… | With交代两倍配置，mainly comes from说明主要成本来源，two PW/one DW对应计数，can be expressed as引公式 | 保留；BMS874–880同样以扩展配置引出模块与成本；mainly对应中文主要，不升级成仅来自 |
| S18 L170 where 2Cout…denote… | expanded number of channels与feature map size分别定义两个量 | 沿用第三轮保留判断；after expansion仅低收益备选，不改系数，不重开历史公式技术事项 |

句间推进核对：先给双重作用，再解释输入增强/局部保留，随后按输入定义→转置→扩展→深度卷积→激活→恢复→残差推进，最后列符号和成本。与三篇同类功能段一致；用途预告和后续公式解释的必要复现不作冗余删除。

形容词与力度核对：compact、local、locally enhanced、normalized、complementary、expanded、short、original分别有明确对象；没有借SL的semantically rich、full-rank、fine-grained/high-rank、dominant/subtle或JE的训练稳定性评价增加本文效果主张。本文locality bias已有对应原词，不换名制造多版本。

本批结果：18单元均核查，无新增核心修改项。L106动作化、L108拆句、L170扩展后通道数均已有记录，保持原优先级；LS-M08旧修复在当前文本中已体现。下一批为3.2.3 DSConv-L。只更新文档，正文及中英对照未改，未编译。

## 分小节审查04：3.2.3 DSConv-L

本批重新读取当前中英L172–185，覆盖标题和5个文字句/公式引导单元。重读BMS full.txt:897接819–833的大核段（双栏顺序，不能从897直接接Q/K/V公式）；SL:898–901及914–921的大核位置与作用；JE:900–938及上一批核实的PDF第8页PW恢复/残差句。以同功能语境比较，不把不同架构的机制结论搬入本文。

| 单元 | 逐句核对与范文学习 | 结论 |
|---|---|---|
| 标题 Feature refinement over longer time scales | refinement对应细化，over longer time scales限定较长尺度，并与3.1 Step 2一致。SL标题Post-fusion global refinement侧重其模型位置与全局作用；不是本文必须复用的唯一标题 | 保留，不将longer改为global或一概换long-term |
| S1 L174 DSConv-L follows… | follows以模块作主语直接说明LLGFA之后；factor of three与DSConv-S factor of two成对；to extract说明用途；over说明时间尺度，from说明融合表示这一来源。BMS897接819–823也是三倍扩展→大核→提取作用；SL900–901以following说明融合后位置 | 保留；虽包含多个配置，顺序线性清楚。fused是已融合表示的状态，不改成global；不加SL抑噪或aging inertia，也不借BMS泛化效果 |
| S2 L174 Two PW convolutions expand and restore… | expand/restore两个动作和两层PW由respectively配对；following the same transformation order as DSConv-S承接整体变换顺序。JE PDF第8页以第一PW扩展、第二PW恢复说明同类功能 | 保留；上下文及前节流程足以理解，不为短句重新展开全部DW/ReLU步骤；same…as搭配正确，不换of或with |
| S3 L174 Its residual connection is applied at… | Its明确指本段DSConv-L，at the … Block level说明残差施加层级；as shown in引本文公式。范文有residual connection，但接入位置由本文中文与公式决定 | 保留；at表示层级，不能仅为模仿改成within DSConv-L而改变模块边界；不机械将applied换added |
| S4 L176 With a channel expansion factor… | With给出三倍扩展配置，cost of说明所属模块，expressed as引公式；与前节计算分析句一致 | 保留；BMS819–823同样直接引出computational cost；不把理论成本名称换为实测运行时间 |
| S5 L185 where 3Cout… | 两个量分别定义通道数与特征图尺寸；expanded说明扩展后状态，respectively配对无歧义 | 沿用第三轮已登记的after expansion低收益备选，当前保留；不新增同项 |

查重：M03-029—M03-032历史均已覆盖；第三轮已讨论L174时间尺度/来源及L185修饰关系，本批提供逐句核对，不计新的发现。未发现新增的介词搭配、形容词对象或力度问题。

本批结果：新增候选0，标题及5个单元保留。3.2各小节已完成逐句记录。下一批为3.3总述及3.3.1多头自注意力的一般形式，已登记C3-R5在该批按旧候选复核。正文、中英对照及中文源稿未改，未编译。

## 分小节审查05：3.3全部剩余内容一次完成

作者要求第三章剩余部分一次完成。本批重新读取3.3全部英文、对应中文及三篇对应语境，依次核对总述、3.3.1、3.3.2、3.3.3。主审全段核对，另安排两名agent分别复核L189–267与L271–386；不把这次分工描述成两人各自独立读完整章。

本批重读/复核范文范围：BMS full.txt:882–891、945–947、974–1037、1057–1076；JE:509–516、642–668、688–736、755–762、823–831；SL:903–912、923–927、956–1031。以连续段落功能为单位，数学推导异栏插入不视为句间推进；具体旧候选的逐句依据仍见C3-R1—R5。

### 3.3总述及3.3.1

| 位置 | 逐句核对结果 | 状态 |
|---|---|---|
| L191总述 | presents—briefly compares—and then introduces按章节内容推进；briefly对应简要，which明确补充LLGFA功能。BMS852–864也预告比较与模块，不必为了短句拆掉功能说明 | 保留 |
| L196两句 | 第一处沿用each head计算范围澄清；第二句Given输入后直接引出第i个head的Q/K/V，主干明确，不因Given而机械改写 | C3-R5待确认；第二句保留 |
| L205两句 | N/d、learnable linear projection matrices、h/d_h分组定义；learnable与linear分别限定可学习性和变换性质；of each head为归属 | 保留 |
| L207条件句 | When先给非负相似度条件，再给归一化权重下的输出表达式，限定有作用，不删nonnegative/normalized | 保留 |
| L223定义句 | at the pth position为位置，in the ith head为所属头，of为归属，respectively为K/V配对；无需统一介词 | 保留 |
| L225三句 | 各位置输出形成单头矩阵→沿特征维拼接所有头→相似度函数/顺序差异，推进直接；along说明轴，mainly对应主要 | 保留 |

### 3.3.2 Softmax与线性注意力

| 位置 | 逐句核对结果 | 状态 |
|---|---|---|
| L229两句 | calculates correlations与normalizes scores为两个不同动作；through query-key dot products为计算方式，using Softmax为归一化工具；后句引公式 | 保留 |
| L242四句 | 指数及归一化→高得分对应较大权重→两两计算形成矩阵→单头/矩阵复杂度→随长度增长。第二句沿用明确similarity的候选；larger修饰weights，more highly correlated修饰pairs，substantially对应显著 | C3-R2待确认；不重开exponentiates低收益改写 |
| L244两句 | maps queries/keys through kernel function，再rearranges computation order using结合律；目的前置与BMS同类表达一致，后句引公式 | 保留，不为复用词形把through改using |
| L263定义句 | nonnegative修饰映射，such as保留例举，all-ones定义向量，corresponding说明归一化项对应当前输出 | 保留；不引入JE物理可解释或抑噪结论 |
| L265三句 | 先算K/V项→避免完整矩阵→映射维度相等条件→固定d_h后关于N线性。By first calculating的执行主体为linear attention，关系清楚 | 保留全部条件；linear in自然，不强改with respect to |
| L267两句 | lower复杂度同时保留“不显式引入局部邻域”的局限，再引出联合建模需求；does not explicitly incorporate不能加强为cannot capture；needed对应中文需要 | 保留；at/with lower complexity的轻度偏好不列新项 |

### 3.3.3 LLGFA与RAA

| 位置 | 逐句核对结果 | 状态 |
|---|---|---|
| L271三句 | 目的→DSConv-S与RAA组合→两支路数据流→加法融合。combines A with B、fuses a branch with another、by addition分别交代组合对象和方式；developed不等于已验证优越 | 保留 |
| L275两句 | 沿用分解为两阶段的decompose候选；下一句agents aggregate from K/V，queries read from context，first/then对应执行顺序 | C3-R1第二处待确认，其余保留 |
| L277目的句 | To reduce参数开销，RAA uses scaling调节通道贡献，再splits scaled features across heads。relative限定不同通道贡献关系，across说明分配对象 | 保留，不能借linear projection替代scaling |
| L286定义句 | scaling vectors/element-wise multiplication/Split_i分组解释；into h subspaces说明划分结果，of dimension说明维度，ith指所取子空间 | 保留 |
| L288比较句 | 与标准Q/K/V投影的参数量比较，approximately和only分别对应约/仅，reducing只陈述参数开销 | 保留已批准表达，不推导成实际延迟降低 |
| L290两句 | learnable agents与matrix表述明确；learned during training为学习阶段，shared across input samples为共享范围 | 保留，不为删重复而去掉跨样本限定 |
| L292两句 | along feature dimension为切分轴，into subspaces为切分结果；for ith head为对应头，公式给该表示 | 保留，不强行将along/across/for互换 |
| L294五句 | 查询匹配→标准Softmax阶段→共同正比例缩小→权重趋均匀及上下文混合→ReLU²目的。common、positive、in a row、positive scores承担条件；increasingly equal对应趋向等权 | 保留；relative ratios略重复不影响理解，不计新问题；不照搬SL单agent归一化坍缩 |
| L311六句 | M定义/两个阶段取值→非正得分置零→有正分数行的共同尺度平方抵消→权重不变→平方增强正得分权重比→无正分数时均匀回退。each/all、positive/nonpositive、common与squared均核对作用对象 | 保留；不能为缩短删前提，也不把平方后的权重与原始得分混用 |
| L313聚合引式 | A_i acts as query to gather context from K/V；as为计算角色，from为信息来源 | 保留；gather和aggregate在解释句中不构成两个技术对象 |
| L329矩阵定义 | Phi_k内容与V_A结果分别解释；定义位置可用aggregation weights代替used by…to aggregate绕述 | C3-R3低优先级待确认，不声称整词组是范文原句 |
| L331广播引式 | each query position reads information from context according to its own features；from为来源，according to为选取依据 | 保留 |
| L347两句 | to agents/by each query区分权重对应对象与分配主体；converts scores into weights与combine contexts区分归一化和融合 | 保留；历史weighted sum补写已撤回，不重复报漏译 |
| L349等效映射句 | Equations show引出由式可知；equivalent mapping、ith head、rank at most n_a分别限定对象及上界。whose指映射，不指整个含残差模块 | 保留，不能照SL更短的rank-1描述删范围 |
| L351两句 | 先拼接，再由output scaling vector调节channel responses，最后加回输入；along为轴，through residual connection为方式 | 保留 |
| L361定义句 | Concat沿特征维拼接及s_o可学习向量解释明确 | 保留，与前文动作及公式重复属于符号定义功能 |
| L363三句 | 两矩阵尺寸→单头/全部头计算量与权重存储→固定h/n_a条件下随N线性。for one head/for all heads范围准确，with fixed条件不可删 | 保留；不把理论线性改成最快运行或最少实际内存 |
| L367三句 | X经DSConv-S得XS并入两分支→分别LN/RAA操作→引融合输出式；which指紧邻XS，while为支路对照而非转折评价 | 保留 |
| L382两句 | 三个表示定义后说明Dropout训练正则及W_a分支贡献；during为发生阶段，of为贡献归属，learnable限定因子 | 保留 |
| L384总结句 | 保留局部→结合RAA上下文→联合表示，同时保持关于N线性；with respect to说明自变量，while保留同时性 | C3-R4词库映射候选待确认；其余保留 |

主审对上述每个文字段与中文逐句核对，公式和符号仅用于确认语言对象及范围；本轮不是独立数学正确性或代码实现审计。已确认LLGFA、得分/权重等英文约定不因中文源稿保留历史命名而回退。

## 第三章本轮逐节审查完成后的待确认清单

下表集中当前建议，不累加历史拆句或低收益备选。完整改前/改后及范文依据见各ID。全部仍未实施。

| ID | 位置 | 建议内容 | 状态与优先级 |
|---|---|---|---|
| C3-R1 | L68、L275 | divides/to divide改为decomposes/to decompose；L275明确two stages | 可选原词对齐，2处 |
| C3-R2 | L242第二句 | computing QK作为计算主语，并明确pairwise similarity calculations | 可选明确计算对象；已有词库在本章应用，1处 |
| C3-R3 | L329 | weights used by the agents to aggregate…改为the agents' aggregation weights… | 较低优先级的定义简化，1处 |
| C3-R4 | L384 | additive connection改为additive fusion | 适用已有词库原词，1处 |
| C3-R5 | L196第一句 | each calculating…within a different representation subspace | 可选澄清每头与计算范围，1处 |

合计5组6处；这是全文语言与范文风格下的待选提案，不是6处确定错误。较低收益的L106动作化、expanded…after expansion、compact修饰重排，以及历史LS-M05/LS-M07拆句维持已有记录，不另计新增。已落实的LS-M06/LS-M08及B类术语改动不重复提交。

范围完成：第三章开头、3.1、3.2总述与3.2.1—3.2.3、3.3总述与3.3.1—3.3.3均有逐节记录。除上述提案外，本轮未发现值得新增的明确词汇、介词、修饰对象或力度问题；这不作绝对无遗漏保证，也不包含作者明确暂不处理的图内名称。本轮仅更新审查文档，正文、中英对照和中文源稿未改，未编译。

## 作者确认后的实施记录

作者在最终5组6处汇总后明确回复“修改”。据此仅实施C3-R1两处、C3-R2/R3/R4/R5各一处；chapters/chapter03.tex和full-manuscript-bilingual.md英文各替换6处。未实施任何低收益备选或历史拆句提案。

备份与逐项清单：build/ch3-approved-style-20260916-165642/。两文件精确允许差异重建核对通过；数学片段、LaTeX命令序列和中文文本序列均不变；其余122个受保护文件哈希不变。按作者此前要求不编译，也未进行编译后页面检查。当前记录表明源文件的限定改动通过核对，不宣称PDF已更新。
