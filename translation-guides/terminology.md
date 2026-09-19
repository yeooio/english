# Terminology

## 作者确认补充 — 2026-09-16（第四章）

- 超参数可选配置集合：`hyperparameter search space`；表头`Search space/Values`，参考Engineering-AI full.txt:1260–1286。作者批准逐节清单后用于第四章及表4-1；不暗示grid search或穷举，已选配置仍称configuration。
- 普通“综合表现/结果”可用`overall performance / overall results`；既有指标`combined average error`保持，不批量替换combined。

## Author preference: reference wording first

扩展检索入口：[三篇范文联合词库](reference-vocabulary.md)。该库按六类功能收录120项新增原词与短搭配，并列出三篇交叉出处；它是证据库，不另立竞争首选译名。本文固定术语仍在本文件唯一维护。

逐章匹配入口：[引言原词与本文逐段对应](introduction-vocabulary.md)。该文件按冻结中文20处位置标记三篇原词、需要适配的含义及尚未覆盖的词，不构成已批准的整段译稿。

其他章节选词入口：[摘要及第二至第五章英文词与搭配](section-expression-vocabulary.md)。按作者最新范围，仅整理原词、搭配和对象区别，不提供结构改动或内容删减方案；已有首选仍以本表为准。

作者要求（2026-09-13）：尽可能沿用三篇范文已有的英文词汇与搭配。含义和语法适合本文时，优先直接采用，不为追求简洁、变化或所谓更学术而另换同义词。

- 先查当前段落功能对应的范文原文，记录确切词组及小节位置，再确定本文首选称谓；不能把改编模板当原文用词证据。
- 按功能选主参考：Engineering-AI 对应轻量化；BMSFormer 对应局部—全局融合与效率；JESSOHRUL 对应健康指标与筛选。
- 每项标明“范文原词可沿用／需适配／本文特有术语”。适配或新增须说明技术含义上的必要原因，不只是风格偏好。
- 保留自然的冠词、单复数、词形及缩写变化。范文的明显语法错误应修正，实验事实和主张强度仍以本文为准。
- 同一概念确定首选表达后，全篇复用；范文中的其他近义表达不作为轮换词库。
- 该优先级不表示现有候选表已全部核准，也不授权复制范文独特整句或扩展本文结论。

Status: SOURCE-AUDITED on 2026-09-13 by three independent agents, one per reference, with main-agent cross-checks. The tables distinguish located reference wording from adaptations and manuscript-specific protocol terms. Source verification is not individual author approval of every translation choice. No manuscript text was changed in this terminology audit.

Exception: the author confirmed on 2026-09-13 that 轻量化 uses `lightweight` and 高效 uses `efficient`, with Engineering-AI as the primary lightweight-expression reference. This confirmation does not approve every other entry in this glossary.

Author decision (2026-09-13): the complete input-side method is named `multi-source health indicator extraction and optimization algorithm` (多源健康指标提取与优化算法). This overall term covers candidate-HI extraction from charging/discharging data and derived curves, MS-CCCT window calibration, PCC/SCC-based admission, and redundancy removal. Use `health indicator extraction` and `health indicator selection` only for their respective internal steps; do not use `group-level health indicator selection algorithm` as the name of the complete method.

For every confirmed term, record the Chinese concept, preferred English form, abbreviation, permitted grammatical variants, conflicting alternatives, source paper/page/section (or author decision), and confirmation date. Singular/plural and capitalization changes are not automatically terminology drift. Reference titles and quoted material are exempt from forced terminology replacement.

## A. 范文原词：含义对应时优先直接采用

出处缩写：EAI = Engineering-AI；BMS = BMSFormer；JES = JESSOHRUL。均指 `style-references/<paper>/full.txt` 对应正文小节；保留原PDF供复核。换行、大小写、单复数和正常缩写变化不算自拟译词。表中出处为用词证据，不是本文实验事实的证据。

| 中文概念/对象 | 本文首选用词 | 范文确切原词与位置 | 使用边界 |
| --- | --- | --- | --- |
| 轻量化架构 | lightweight architecture | EAI §7: lightweight architecture | 作者已确认lightweight；不用efficient轮换 |
| 轻量化网络架构 | lightweight network architecture | EAI §7: 同左 | network是明确对象的限定，不另立同义词 |
| 轻量化深度学习架构 | lightweight deep learning architecture | EAI §4开头: 同左 | 需要说明深度学习对象时用 |
| 轻量且高效的SOH估计框架 | lightweight and efficient SOH estimation framework | EAI §1收束: 同左 | 同时陈述两项特征时用 |
| 高效深度学习模型 | efficient deep learning model | BMS摘要: an efficient deep learning model | efficient不自动代表参数最少 |
| 健康状态估计 | state-of-health (SOH) estimation | BMS摘要: 同左 | 首次定义后用SOH estimation |
| 健康指标 | health indicator (HI) | BMS §2.3、JES摘要: health indicators (HIs) | 单数/复数按对象变化 |
| 阻抗谱测试 | impedance spectrum measurements | JES引言: 同左 | 用于需要专用仪器的测试过程；不写成泛指技术名称的 impedance spectroscopy |
| BP神经网络 | backpropagation (BP) neural network | JES正文: Back Propagation (BP) neural networks | 首次出现展开缩写；后文可使用 BP neural network |
| 特征提取 | feature extraction | JES §3.5.2: 同左 | 与筛选区分 |
| 健康指标筛选 | health indicator selection / HI selection | JES §4.2: health indicator selection；§3.5.2: HI selection | 全称/缩写，不是两个译名 |
| 候选健康指标 | candidate HIs | JES §3.5.2: 同左 | candidate单复数正常变化 |
| 最终HI子集 | final HI subset | JES §3.5.2: 同左 | 子集不是任意融合表示 |
| 皮尔逊与斯皮尔曼相关系数 | Pearson and Spearman correlation coefficients (PCC and SCC) | JES §5: 同左 | 单项名称按§3.5.2分别定义 |
| 线性相关 | linear correlation | JES §3.5.2: 同左 | 不泛称因果联系 |
| 单调关系 | monotonic relationship | JES §3.5.2: 同左 | 不等同全部非线性依赖 |
| 特征间相关系数 | inter-feature correlation coefficients | JES §3.5.2: 同左 | 本文阈值及逻辑以本文为准 |
| 同组电池 | cells within the same battery group | JES §3.5.2: 同左 | 不构成新增协议角色 |
| 长程依赖 | long-range dependencies | BMS §3.3.1；EAI §4.1；JES §2.1.2: 同左 | 优先固定，不轮换为含义不同的趋势 |
| 长期退化趋势 | long-term degradation trends | JES §4.4.1；EAI §5.5.2: 同左 | 普通时间趋势优先用此词；卷积尺度含义另见B表 |
| 短期容量波动 | short-term capacity fluctuations | JES §4.4.1: 同左 | 只用于相应容量现象 |
| 局部信息 | local information | BMS §3.1、§3.2.1: 同左 | 不替代所有局部退化变化 |
| 深度可分离卷积 | depthwise separable convolution | BMS摘要、§3.2.1: 同左 | 允许convolutions；缩写DSConv |
| 多尺度深度可分离卷积 | multi-scale depthwise separable convolution | EAI §4.2标题: Multi-scale depthwise separable convolutions | 正常大小写/单复数调整；保留本文模块名 |
| 局部—全局融合注意力模块 | Local-Global Fusion Attention (LGFA) | BMS §3.3: Local-Global Fusion Attention (LGFA)；作者2026-09-16确认 | 本文正式模块专名固定为LGFA；标题和一般功能概括可保留小写`local-global attention`，不再使用SLFA或LLGFA |
| 深度卷积 | depthwise convolution | BMS §3.2.1: 同左 | 与pointwise分工固定 |
| 逐点卷积 | pointwise convolution | BMS §3.2.1: 同左 | 不称标准卷积 |
| 计算效率 | computational efficiency | EAI §4、§5.6: 同左 | 不与复杂度等同 |
| 计算复杂度 | computational complexity | BMS摘要: 同左 | 理论规模关系 |
| 线性计算复杂度 | linear computational complexity | EAI §7: 同左 | 句中明确是注意力还是完整模型的复杂度 |
| 参数量 | parameter count | EAI §7: 同左 | 首次说明统计范围是否仅可训练参数 |
| 可训练参数 | trainable parameters | BMS §4.2.2: total number of trainable parameters | 可用于限定parameter count的统计对象 |
| 存储大小 | storage size | BMS §4.2.2；JES §4.4.2: 同左 | 与本文os.path.getsize测量更接近，选为权重文件指标首选；首次定义统计对象 |
| 存储占用（范文备选） | storage footprint | EAI §7: 同左 | 确切原词；本文已有storage size首选时不轮换，不推断运行内存或实际Flash占用 |
| 训练时间 | training time | BMS §4.2.2；JES §4.4.2: 同左 | 不换成inference latency |
| 浮点运算次数 | floating-point operations (FLOPs) | BMS §4.2.2: 同左 | 本文补充单次前向口径 |
| 资源受限BMS | resource-constrained battery management systems (BMS) | 作者2026-09-16确认A8，按Engineering-AI资源主参考统一；替代9/13的limited约定 | 首次出现用 (BMS)；正文不再轮换resource-limited。Cover Letter仍为旧词，未纳入本批修改 |

### A.1 补充核对：HI构建与筛选的细粒度词汇

2026-09-13续查：以下均定位于三篇范文正文，不取自参考文献题名。属于可用词汇，不表示其所在整句、阈值、实验角色或机制解释可以照搬。与A表共同维护，一个概念不另设轮换译名。

| 中文概念/对象 | 优先可用原词 | 原文位置与核对边界 |
| --- | --- | --- |
| 恒流充电时间 | constant current charge time (CCCT) | BMS §2.3，原文跨行连接；适用于本文CCCT，不能替换为EAI的面积指标CCCA |
| HI提取 | HI extraction | BMS §2.3；health indicator的正常缩写，与HI selection分开 |
| 充电片段 | charge segment | BMS §2.3；描述数据片段，不增加恒流条件以外的新设定 |
| 窗口大小 | window size | BMS §2.3；首次明确本文是在电压域还是序列域计量 |
| 滑动步长 | moving step size | BMS §2.3；只借名称，原文步长数值与区间列举不完全一致，不继承该数值描述 |
| 搜索片段 | search segment | BMS §2.3；仅用于确有逐步搜索的片段 |
| 经验定义的窗口 | empirically defined windows | EAI §3.3.2，取自static, empirically defined windows；不擅自把本文所有固定窗口称为经验窗口 |
| 离线标定 | offline calibration | EAI §3.3.2，正文offline calibration step及小标题；不将EAI的training partition角色带入本文 |
| 候选窗口 | candidate window | EAI §3.3.2；与candidate HIs区分，窗口不是已经提取出的指标 |
| 特征序列 | feature sequence | EAI §3.3.2；不因此将本文时间特征改为范文积分面积序列 |
| 所选HI | selected HIs | JES §3.5.2；正式指标集合仍用A表final HI subset，句中指代可用selected HIs |
| 保留下来的HI | retained HIs | JES §3.5.2；用于筛选中间步骤，不与最终入选状态混淆 |
| 相关强度 | correlation strength | JES §3.5.2；描述强弱，具体正负号/绝对值按本文公式 |
| 筛选准则 | selection criteria | JES §3.5.2；本文阈值与双相关逻辑不照抄范文 |
| 筛选流程 | screening procedure | JES §3.5.2；与准则不同，是操作步骤 |
| 特征多样性 | feature diversity | JES §3.5.2；可描述筛选目标，不把低相关自动写成已证明信息互补 |
| 高度冗余的信息 | highly redundant information | JES §3.5.2；有对应冗余判定时才用highly，不随意加强程度 |
| 电池化学体系 | battery chemistries | JES §3.5.2、EAI Fig. 2图注；不同数据集不自动代表不同化学体系 |

可沿用的操作动词也来自JES §3.5.2：`retained`（保留）、`ranked`（排序）、`removed`（剔除）。按句法调整词形即可；只描述本文实际执行的步骤，不凭范文新增排序操作。

## B. 需适配：保留范文核心词，新增限定须说明原因

| 本文概念 | 范文证据 | 本文用法与必要适配 |
| --- | --- | --- |
| 域内跨电池泛化 | JES §4.2.1: cross-cell generalization performance | 采用cross-cell generalization作为核心词；需要区分跨域时加in-domain。完整in-domain cross-cell generalization不是逐字原词 |
| 局部退化变化 | EAI §1: fine-grained local degradation details；§4.2.1: high-frequency local variations；JES §4.4.1: short-term capacity fluctuations | 按具体对象优先选原词；local degradation variations仍为组合适配，不能用波动/细节机械替代“变化” |
| 长尺度退化趋势 | JES §4.4.1: long-term degradation trends | 中文指普通长期趋势时直接用原词；确指核尺度时另澄清尺度，不机械保留自拟long-horizon degradation trends，也不静默改变技术含义 |
| 局部—全局融合 | BMS摘要: Local-Global Fusion Attention | local-global fusion取自模块专名中的核心词组；不称其为原文独立命名的建模概念 |
| 局部—全局协同建模 | 前项融合词组可参考 | local-global collaborative modeling是本文概念适配，不能声称三篇出现了完整原词；协同建模不自动删为融合 |
| 智能体聚合与广播 | EAI §4.3: Global Aggregation、Gated Broadcasting | 可取aggregation/broadcasting；agent-mediated aggregation and broadcasting为本文组合表达。Gated包含门控含义，不因照原词而给RAA加门控 |
| 线性注意力复杂度 | EAI §7: linear computational complexity；BMS §3.3: linear complexity | 优先用原词，并在句中指明attention；原候选linear attention complexity非已查到的完整原词 |
| 计算与存储开销 | computational complexity/efficiency、storage size均有原文 | 分别写本文实际测量指标；computational and storage overhead是组合适配，不标原文 |
| 高效建模 | BMS摘要: an efficient deep learning model | 可沿用原有模型表达；efficient modeling未定位为完整原词，必要时仅作为普通组合说明 |

## C. 本文特有协议/边界表达：暂保留，不冒充范文原词

三篇当前提取正文中未定位以下所有完整词组；这是检索结论，不表示领域内不存在这些词。本文的电池角色按作者2026-09-16确认的实际功能表达：用于超参数选择的第二节电池称为validation cell，但不照搬BMSFormer同一参考电池内部30%/70%的划分方式。

| 中文概念 | 保留的本文表达 | 原因 |
| --- | --- | --- |
| 特征开发电池 | feature-development cell | 本文指标开发角色 |
| 训练电池 | training cell | 本文明确电池级角色；原文training sets不是同义角色 |
| 配置电池 | validation cell | 用于验证、比较并选择最佳超参数配置；不是test cell |
| 主对比报告范围 | cells reported in the main comparison | 描述报告范围，不增加第三类角色 |
| 跨数据集迁移 | cross-dataset transfer | 本文跨域任务 |
| 源域直接测试 | source-only evaluation | 与使用目标域数据的适应区分 |
| 少样本适应 | few-shot adaptation | 本文适应协议 |
| 严格数据隔离 | strict data separation | 本文数据使用边界；正文优先直接描述操作而非反复自评 |
| 轻量化部署潜力 | potential for lightweight deployment | 本文证据止于潜力，不借范文硬件结果扩大主张 |

## 引言复核补充：首选候选与跨章节原词

2026-09-13继续复核。以下进入本表统一维护，状态为“出处已核实、首选候选”，不是已批准的整段译稿。引言映射表只引用这些决定，不另立译名。

| 中文概念 | 首选候选 | 原词依据 | 采用边界与不轮换项 |
| --- | --- | --- | --- |
| 模型驱动方法 | model-based approaches | BMS §1 L95；EAI §2 L185包含model-based and data-driven approaches | 同一分类不轮换model-driven；不改变本文类别 |
| HI表征能力 | representational ability | 作者2026-09-16确认A5；JESSOHRUL full.txt:1884–1893 | 仅HI对象采用ability；不把普通ability to represent句法改成名词短语 |
| 模型表征能力 | representational capability | 保留既有模型用词；EAI §1 L153 | 模型语境及必要复数capabilities保留；不随HI替成ability或改capacity |
| 容量保持率 | capacity retention | EAI §3.1 L274 | 跨章节原词，不冒充引言已有；按本文SOH定义保留分母和百分比口径，不继承其防御性定义引导句 |
| 最大可用容量 | maximum available capacity | EAI §3.1 L275–276，取自current maximum available capacity | 中文含“当前”时保留current；不把额定容量或初始容量当同义词 |
| 时间和内存复杂度 | time and memory complexity | EAI §2.2.2 L218–219 | 对应注意力理论复杂度；不替代实验权重文件的storage size |
| 容量恢复 | capacity recovery | JES §1 L285–286的short-term local capacity recovery behaviors；§2 L523 | 同一物理现象优先此词；EAI的capacity regeneration保留作来源变体，不轮换。恢复不等于所有容量波动 |

引言关系限定：BMS §1 L173的weakly correlated health indicators是确切原词，但用于本文拟剔除输入时必须明确相关对象为SOH。补with SOH属于必要适配；HI–SOH低相关与HI–HI低相关不是同一筛选判断。JES的informative health indicators只说明信息价值，不自动包含跨电池稳定性。

## 核对结论与采用状态

2026-09-13：作者授权尽可能采用范文原词；A表为已定位、可优先使用的词汇清单，B表为技术语义所需适配，C表为本文协议表达。lightweight/efficient的区分已单独获作者确认。其他词在具体段落中仍核对对象和含义；正文写入仍按workflow.md执行。

## Canonical-term control

- 本表是术语的唯一维护位置。句型库、范文摘录及其他指南不能另立同一概念的竞争译名。
- 正式逐批翻译前，先按“中文概念—首选英文—缩写—允许变形—易混表达—依据—状态”确定核心术语。未确认项标为候选，不宣称已冻结。
- 一个相同技术概念固定一个首选称谓；允许有语法依据的单复数、词形和定义后的缩写，不为避重复换同义词。
- 不同技术概念即使中文相近仍须区分，例如提取/筛选、依赖建模/轨迹跟踪、计算复杂度/实际耗时。
- 新概念先登记再使用。后续更改已确认译名时，检查已译章节、图题、表题和图内文字，不仅修改当前段落。

不得将A、B、C三类再次合并成没有来源标签的单一候选词表。其他指南中的旧例句是表达示意，实际词汇以本表的当前分类与首选项为准。

### Abstract batch author confirmation — 2026-09-13

- The 2026-09-13 abstract approval used health indicators (HIs), depthwise separable convolutions, long-range degradation dependencies, and computational and storage overhead in their respective contexts. The dependency wording for the proposed LGFA module is superseded by the 2026-09-16 author update below; overhead remains an adapted expression, not an exact reference quotation.
- 长尺度退化特征: degradation features over longer time scales. Context-specific rendering consistent with Chapter 3's longer temporal scale; not a replacement for long-range dependencies.
- 较低参数开销: low parameter overhead. Author approved this refinement instead of with few parameters.
- Author update (2026-09-16): in descriptions of the proposed LGFA module, use `long-term dependencies`, following the BMSFormer Local-Global Fusion Attention wording. Retain `long-range dependencies` when it specifically describes other cited attention mechanisms or cross-position relations; do not replace `long-term degradation trends`, which denotes a temporal trend rather than a dependency.
- 深度特征融合: deep feature fusion; 轻量化深度学习: lightweight deep learning. Approved keyword renderings; do not substitute the reference's different depthwise feature fusion concept.
- ReLU²智能体注意力: ReLU² agent attention in the abstract; formal name ReLU² Agent Attention (RAA) remains defined in the model section.

### Spelling conventions

### Introduction P01 author confirmation — 2026-09-13

- 长循环寿命: long cycle life; 低自放电率: low self-discharge rate; 规模化储能: large-scale energy storage.
- 固体电解质界面膜增厚: thickening of the solid electrolyte interphase (SEI) layer. Preserve interphase, not interface; thickening retains the thickness-specific meaning.
- 活性锂损失: loss of active lithium; 电极结构衰退: structural degradation of the electrodes; 容量衰减: capacity fade; 热失控: thermal runaway.
- 运行性能: operating performance. These are approved in P01 context; do not replace distinct mechanism concepts with generic reference wording.
- 新能源交通: transportation powered by new energy sources. Author approved this descriptive wording in P01; exact industry scope remains pending final clarification. Do not silently narrow to electric mobility.

### Spelling rules

### Introduction P02 author confirmation — 2026-09-13

- 容量保持率: capacity retention; 最大可用容量: maximum available capacity. These previously source-verified candidates are now approved in P02.
- 完整或近似完整的充放电循环: full or nearly full charge-discharge cycles; 可观测运行信号: observable operating signals. Do not omit nearly full or replace observable signals with a narrower signal list.
- Author reiterates reference-first style: start from verified reference sentence patterns and terms, then make only necessary grammatical and technical adaptations. Do not perform repeated synonym substitutions without a supported defect.

### Spelling conventions (continued)

- Use American English unless a target journal requires otherwise.
- Use `modeling`, `generalization`, and `behavior` consistently.
- Preserve dataset names, cell identifiers, model names, variables, and mathematical notation exactly.

### Whole-manuscript authorization — 2026-09-13

The following renderings are used consistently in the completed autonomous translation. They are source-context decisions under whole-manuscript authorization, not separately approved phrases or fabricated standard definitions. Existing individually approved terms above retain priority.

| 中文概念 | 本文用法 | 区分与范围 |
| --- | --- | --- |
| 充电电压—时间 | charging voltage--time (CVT) | HI来源曲线 |
| 增量容量 | incremental capacity (IC) | 不与容量变化率混用 |
| 温度—电压微分 | differential temperature--voltage (DTV) | 与引用文献中的 differential thermal voltammetry 名称按原文语境区分 |
| 温度—容量微分 | differential temperature--capacity (DTC) | 保留自变量 |
| 半峰宽 | full width at half maximum (FWHM) | 保留完整专业名称 |
| 峰谷差 | peak-to-valley difference | 不与峰位混用 |
| 电压窗口内放电容量 | discharge capacity within a voltage window | 保留窗口限定 |
| 能量效率 | energy efficiency | 不替换为模型计算效率 |
| 双阈值准入 | dual-threshold admission | 本文筛选步骤，不声称标准命名 |
| 综合平均误差 | combined average error | 与单独MAE等指标区分 |
| 静态可学习矩阵 | static learnable matrix | 参数可训练，非输入动态生成 |
| 行归一化 | row normalization | 不改为Softmax |
| 层归一化 | layer normalization | 与行归一化区分 |
| 通道缩放 | channel scaling | 不改写为完整线性投影 |
| 读出层 | readout layer | 迁移时与冻结特征提取模块区分 |
| 配置选择电池 | validation cell | 用于超参数选择；结果可报告，但不能称为test result |
| 源域直接测试 | source-only evaluation | 不使用目标域数据更新参数 |
| 少样本适应 | few-shot adaptation | 不与源域直接测试混称 |
| 参数量 | parameter count | 可训练参数时用 trainable parameter count |
| 权重存储占用 | storage size | BMS §4.2.2: Storage size，以os.path.getsize测量模型参数存储需求；不等同运行时memory或推理延迟 |
| 线性读出层 | linear readout layer | 本文SOH输出层；定义后可简称readout layer，不改为BMSFormer的MLP |
| 未归一化注意力得分 | similarity scores / attention score matrix | BMS §3.3区分similarity values与attention weights；不与PCC/SCC correlation混称 |
| 归一化注意力权重 | attention weights / attention weight matrices | 用于RAA聚合与广播；广播阶段可具体写broadcasting weights |
| 线性投影矩阵 | linear projection matrices | BMS §3.3；用于标准QKV投影，不用于RAA通道缩放向量 |

Original raster labels remain outside this text-only terminology update; see final-translation-review.md for L-DSConv/DSConv-L and existing spelling issues.

### Whole-manuscript terminology consistency — implemented 2026-09-16

作者本轮要求再开 agent 查漏并明确“我们现在来修改即可”。以下为在该授权范围内落实的术语一致性决定，不将未采用候选视为另获单独批准。三名 agent 重读对应范文后，实施记录见 `technical-terminology-applied-2026-09-16.md`。

| 概念 | 本文统一用词 | 采用范围与保留区别 |
| --- | --- | --- |
| 充电时间/时长类特征 | charging-time feature(s) | 指特征类别时不用 charge timing features / charge duration feature 轮换。具体指标全称仍为 constant current charge time (CCCT)；普通物理时长叙述 charge duration 保留。BMSFormer §2.3 full.txt:457–459、503–506；JESSOHRUL 表4:1637–1638。 |
| 电池材料体系 | battery chemistries | 对公开数据集NCO/LCO/LFP等化学体系的同一概念统一；具体 cathode material 和涵盖封装/规格的 battery systems 不替换。三篇均有 chemistries 依据；materials 本身不是错误。 |
| 候选池筛选后的最终HI集合 | final HI subset | 引言贡献及筛选表最终输出采用此名；步骤中的中间 selected HI set 和实验 Fusion 输入不改。JESSOHRUL §3.5.2 full.txt:1822–1834。 |

本轮保留 cross-position context，因中文对应明确且没有同对象多版本问题；不实施旧审查中的可选 global context 替换。保留 linear association / linear correlation 在相应描述中的用法，BMSFormer 与 JESSOHRUL 均有同条件依据。作者已知的旧图模块名另行处理。

### 最新作者确认：A1—A8 — 2026-09-16

作者明确“先改A1到A8”。以下优先于上方历史批次约定；实施明细见 `reference-led-terminology-applied-A1-A8-2026-09-16.md`。本批27处正文/表格替换，25处同步到中英对照的英文部分，其余建议未授权。

| 项目 | 固定用词 | 范围 |
| --- | --- | --- |
| A1 组级HI筛选总流程 | health indicator selection | 正式表题与Procedure同步；dual-threshold admission保留 |
| A2 冗余信息 | redundant information | 候选HI高相关造成的信息重复 |
| A3 PCC线性相关 | linear correlation | 第2章PCC说明，替代历史允许association轮换的决定；其他关系与注意力术语不改 |
| A4 充电时间类特征 | charging-time feature(s) | 本批补齐4处time features；time-based上位类别及charge duration物理时长保留 |
| A5 HI表征能力 | representational ability | 模型capability保留 |
| A6 卷积核尺度 | kernel size；small and large kernels | DSConv-S/L同一对核；长尺度特征限定保留 |
| A7 容量曲线名称 | capacity degradation curves | 第2章对应图2-2；一般capacity fade物理概念保留 |
| A8 资源受限BMS | resource-constrained BMS | 正文统一SL用词，替代历史limited约定；投稿信未修改 |


### 补充确认：模型表征能力、资源消耗与理论复杂度 — 2026-09-16

按作者“只要范文有且同时不改变我们的原意即可”的条件，核对当前中文与范文后实施3项6处：模型 representational capacity（引言13行1处、27行2处），总资源 resource consumption（第4章166行、结论3行各1处），理论 time and memory complexity（引言40行1处）。同步中英对照英文6处。

模型词采用BMS full.txt:882–890与JE full.txt:661–668的模型表征语境；SL full.txt:145–153也用capability，旧词并非错误。本轮模型capacity约定取代前次保留capability的约定，HI ability不变。总资源词参考SL full.txt:2440–2453，仅指四项资源指标概括，不新增能耗测量、不改具体计算/存储分项。理论复杂度参考SL full.txt:208–225，与中文两两关系随序列长度二次增长的含义相符，不涉及实测延迟。

备份与精确清单：build/terms-b-20260916-152141/changes.json。3个正文文件精确允许差异核验通过，中文源稿哈希不变。build.ps1编译成功，37页；PDF第2、4、5、30、31、32页显示检查通过。无未定义引用、缺字和溢出报告；既有ICC图片警告保留。其余候选未改。

### 卷积与融合应用说明搭配 — 作者确认落实 2026-09-17

逐点卷积的跨通道整合采用 `integrate features across channels`（JE full.txt:693–696）；深度卷积的局部序列模式采用 `local sequential patterns`（JE §2.2.2）。两者为操作搭配，不是新增模块名称。LGFA双分支的feature fusion继续保留，数学定义中的cross-position interaction不作全局替换。正式名称LGFA、RAA、DSConv-S/L不变。

### 消融应用表达 — 2026-09-17 作者完整稿落实

沿用module ablation analysis、combined average error、full configuration。消融中局部退化对象用fine-grained local degradation information，描述动态时用fine-grained local degradation dynamics；互补效应用complementary effect，模块分工用complementary roles。cross-cycle context modeling为本文窗口内循环关系的应用表达，不全局替换global context modeling。pre-attention local enhancement参照Engineering-AI §5.5.2；post-fusion feature refinement为其post-fusion refinement的对象适配。JE §4.4.1提供细粒度退化动态及互补结果的表达依据，不将所有词冒称JE原词。更一致的综合表现指跨所比较数据集的误差表现，不表示多随机种子的方差结论。

### Agent中文称谓 — 作者最新确认 2026-09-17

作者明确要求中文统一使用“代理”，不再使用“智能体”。后续中文修改稿、回译和新说明采用代理、代理聚合、代理矩阵、ReLU²代理注意力；英文Agent Attention、agent aggregation、agent matrix和RAA保持不变。此决定更新此前中文候选称谓，不改冻结中文源文件，不批量重写历史批准记录。

### 消融卷积应用用词更新 — 2026-09-17

作者确认Table16卷积作用采用capture fine-grained local degradation patterns，替换该处supplement fine-grained local degradation dynamics；不是全局替换所有information/dynamics。配合表述采用joint integration和complementary roles/effects，不创建continuous feature-processing process/pathway专名。历史同位置记录以ablation-wording-final-applied-2026-09-17.md为准。
