# 引言：三篇原词与本文逐段对应

日期：2026-09-13。范围仅为引言。主审完整读取冻结中文 `source-zh/chapters/chapter01.tex` 与三篇引言TXT，并回查跨页内容；三个agent分别完成BMS、EAI、JES与现稿的只读对照。**本文件是用词选择依据，不是整段英译稿，也未授权改正文。**

## 本轮结论与取用顺序

不能只做范文词库：先看本文每段实际要说什么，再找三篇对应原词，最后检查语义是否相同。

- 保留本文“背景→模型综述→HI综述→比较收束→三项挑战→框架及三项贡献”的顺序，不用范文重排。
- 模型分类、局部—全局与卷积的用词以BMS为主；HI采集、时间特征、多源筛选动机以JES为主；轻量化、资源约束、二次复杂度以EAI为主。每段可按具体概念组合取词，不整段绑定一篇。
- 下面20处位置映射覆盖现稿13个正文段落、3项挑战、框架引出及3项贡献。中文是定位摘句，不是完整“修改前”；本轮没有提出删改原句。
- 随后80条为引言相关的来源证据，包含已收录词的引言语境和不适合直接替换的参考词，**不能计作80个全部新确定的译名**。
- 固定术语仍由 `terminology.md` 唯一维护。原词存在只意味着有出处，不意味着本文可无条件采用或必须复用所在整句。
- EAI的§2 Related work也承担本文引言中的综述功能，已明确标记，不冒充§1 Introduction。
- L为 `style-references/<paper>/full.txt` 当前行号，不是PDF页码。TXT有双栏穿插，章节归属按对应内容核对；本轮不宣称已做PDF逐段顺序或版面复核。

## 一、按我们的引言选择能用的表达

### 背景、模型综述及HI综述

| 本文位置（保持原顺序） | 本段语言任务 | 范文原词与出处 | 直接采用或必要适配 |
| --- | --- | --- | --- |
| P01 “锂离子电池凭借高能量密度……” | 高能量密度、应用与安全性能 | high energy density（BMS L50；JES L54）；electric vehicles（BMS L51）；battery safety, reliability, and performance（BMS L57–58） | 直接采用这些对象词。long service life和excellent cycling performance不能替代“长循环寿命”；lightweight在JES开头指电池重量，不是模型。 |
| P02 “容量衰减是电池老化最直观的特征……” | 容量测量条件→在线间接估计→资源限制 | direct measurement of capacity（EAI §1 L66–67）；full charge–discharge cycles（EAI §1 L68）；online monitoring（BMS L70）；limited storage space（BMS L64）；capacity retention / maximum available capacity（跨章节：EAI §3.1 L274–276） | 原词有明确落点。保留“完整或近似完整”；indirect sensor data不能自动等同所有可观测运行信号。容量术语现已从方法章节补足出处，不冒充引言原词。 |
| P03 “近期的健康状态估计方法主要分为……” | 两类方法的分类 | model-based approaches / data-driven approaches（BMS L95–96）；model-based and data-driven approaches（EAI §2 L185） | 此概念优先model-based；JES L61的model-driven作为参考变体，不轮换。保留本文分类，不额外插入empirical models。 |
| P04 “模型驱动方法通过数学方程……” | 物理模型、参数获取和ECM简化 | mathematical equations or circuit components（BMS L121）；differential equations（BMS L123–124）；particle radius and diffusion coefficients（BMS L127–128）；physical interpretability（EAI §2.1 L121）；temperature and C-rate（EAI §2.1 L132） | 首句的“数学方程或等效电路”不能整套原搭配：应取mathematical equations和equivalent circuit models准确组合，标为适配；circuit components留给后面的电阻电容说明。微分方程不擅改成偏微分方程；microscopic parameters不能删去具体参数例子。 |
| P05 “相较于模型驱动方法，数据驱动方法无需……” | 历史数据、输入映射、传统模型能力 | historical data（BMS L137）；detailed electrochemical models（JES L66–67）；mapping extracted features directly to SOH（EAI §2.2 L136–137）；structural constraints（BMS L72） | 可借词和映射搭配。BMS的unstable data不机械替换本文“波动性数据”；Fei的42项和六种模型按现稿，不照抄范文的列举数量。 |
| P06 “随着深度学习的快速发展……” | 深度表征与CNN局部提取 | capture complex aging dynamics（EAI §1 L99）；local feature extraction（BMS L155–156）；convolutional kernels（JES L76）；pooling operations（JES L89） | 直接映射现有CNN说明。各引文方法与结论仍以中文及其引文为准，不因范文出现end-to-end就补入端到端主张。 |
| P07 “然而，传统CNN的单层卷积受局部感受野限制……” | CNN局部限制→循环历史联系→串行瓶颈 | local receptive fields（EAI §1 L100）；previous time steps（JES L94–95）；from one time step to the next（BMS L196–197）；sequential processing constraints / hinder parallelization（EAI §1 L100） | 保留本文单层限定和混合模型例子。局部感受野不等于CNN完全不能建模长程；选择性更新、隐藏状态的完整机制不能冒充这些引言短语。 |
| P08 “为解决这一问题，Vaswani等人……” | Transformer全局交互与开销 | avoiding recurrence（BMS L206）；self-attention mechanism / global dependencies（BMS L99）；parallel computing（BMS L100）；long-range dependencies（EAI §2.2.2 L211）；time and memory complexity（EAI §2.2.2 L218–219） | 直接采用对应对象词。global与long-range不等义轮换；两两关系、参数增加及O(N²)主张仍按本文准确展开，不能声称全段为某篇原句。 |
| P09 “除了预测模型，健康指标的提取与选择……” | 模型转HI；采集、工况及微分限制 | In addition to model performance（JES L105）；impedance spectrum measurements / specialized instruments（JES L111–112）；charge-discharge rates（JES L114）；amplify sensor noise / smoothing preprocessing（EAI §2.2.1 L168） | 仅承接动作对应，不能整段原词照套：“预测模型”不等于model performance，必须适配连接对象，且本文另有selection。只说部分内阻HI依赖专用设备；不继承heavy smoothing、延迟或本文已解决噪声的结论。 |
| P10 “相比之下，时间类健康指标无需微分处理……” | 时间HI、CCCT定义与窗口选择 | time-based HIs / differentiation processing（JES L122–123）；constant current charging time（JES L129）；shorter charging segments（JES L138）；window size and step size（BMS L208） | 已有术语表CCCT首选constant current charge time来自BMS方法§2.3 L457–458，标明跨章节，不另换charging版本。time difference of selected segments不能代替“区间两端时刻差”的精确定义。 |
| P11 “不同运行数据及其衍生曲线能够……” | 多源候选、统计特征、降维与筛选 | multi-source inputs（JES L248）；statistical features（JES L124）；raw data（JES L189）；Multi-feature fusion strategies（EAI §2.2.1 L175） | 仅借对象与操作类别。Dai/Lin的特征、PCA和模拟退火不能由JES对其他研究的描述替换；这些专有词需另核。 |
| P12 “单一健康指标所反映的退化信息相对有限……” | 相关性、跨电池表现与冗余形成筛选动机 | weakly correlated health indicators（BMS L173）；informative health indicators（JES L339）；multiple correlation evaluation methods（JES L249–250）；input redundancy（EAI §2.2.1 L172） | 弱相关须明确对象为SOH，加入with SOH属于必要适配；不能与HI彼此低相关混淆。informative只表达信息价值，不等于跨电池稳定。三重条件的完整组合是本文表述；inter-feature correlation coefficients的证据来自JES方法§3.5.2，不能混称引言原词。 |
| P13 “现有SOH估计方法之间的比较总结于……” | 文献比较收束与精度—资源权衡 | existing SOH estimation methods（JES L310）；HI selection algorithms（JES L313）；increasing depth and size（BMS L76–77）；low computational cost（BMS L92）；trade-off between model complexity and accuracy（JES L259–260） | 词组与现稿有直接落点。不要把edge devices直接替换成BMS；模型规模、理论复杂度、训练耗时、存储分别描述。 |

### 挑战与贡献

| 本文位置（保持原顺序） | 本段语言任务 | 范文原词与出处 | 直接采用或必要适配 |
| --- | --- | --- | --- |
| T1 挑战（1）“健康指标的跨电池稳定性问题” | 原始信息→跨电池相关性→双相关与冗余 | raw data collected from multiple sensors（JES L334）；degradation-related features（JES L335）；HI representation capabilities（JES L350）；batteries in a group（JES L351） | 出处栏保留原词，本文表征能力仍采用已选representational capability，补HI限定为适配，不另换representation版本。相关性明确是HI–SOH还是HI–HI。across all batteries in a group不能照搬：本文在特征开发集合上定规则；完整三重筛选关系是本文组合。 |
| T2 挑战（2）“局部与长期退化信息的融合问题” | 局部变化和长期趋势的互补 | short-term local capacity recovery behaviors（JES L285–286）；long-term degradation patterns（JES L212）；fine-grained local degradation details（EAI §1 L107） | 容量恢复首选capacity recovery；capacity regeneration保留为原文变体。中文“长期趋势”继续用已选long-term degradation trends（跨章节JES §4.4.1 L3529），不因为此处引言有patterns就替换。不能继承相邻rank collapse或早期故障检测主张。 |
| T3 挑战（3）“计算复杂度限制” | 串行递推、二次交互及资源负担 | Computational Complexity Limitations（BMS L162）；computational resource demands（BMS L167）；quadratic computational complexity（EAI §1 L102）；time and memory complexity（EAI §2.2.2 L218–219） | 标题和对象词可用。不得继承BMS unnecessary parameter updates的无依据判断；不把理论复杂度直接写成实测部署性能。 |
| K0 “为应对上述挑战，本文提出一种……” | 从挑战引出整体框架 | To address these challenges（BMS L184；EAI §1 L108）；lightweight and efficient SOH estimation framework（EAI §1 L109）；balancing accuracy and efficiency（BMS L187） | 优先使用现成短搭配，接本文框架与两层设计。只在需要时使用一次承接，不反复自证。 |
| K1 贡献（1）“提出组级健康指标选择算法” | 候选评价、MS-CCCT与双相关筛选 | health indicator selection algorithm（JES L288–289）；correlations between various HIs and SOH（JES L290）；selected indicators（JES L295）；screening methodology（EAI §1 L142） | 保留本文特征开发集合、组级标定、PCC/SCC双阈值和冗余约束。CCCA/CCDA不等于CCCT；learnable hyperparameter不等于本文离线标定；统一规则不意味着统一HI组合。 |
| K2 贡献（2）“构建轻量级局部—全局网络MS-AgentNet” | 局部—全局、卷积尺度与低开销 | short-term and long-term features（BMS L215）；small kernel size / large kernel size（BMS L218–219）；depthwise separable convolution（BMS L218）；compact parameter set（EAI §1 L153） | 保留冻结中文的SLFA及ReLU²智能体机制，不改成范文LGFA/FLFA/DSCA。只取本文具备的功能；不借multi-channel给现稿额外增加贡献。 |
| K3 贡献（3）“开展多数据集综合验证” | 异质数据、精度效率及泛化评价 | multiple battery datasets（JES L303–304）；different materials, capacities, and charge–discharge protocols（JES L304–305）；accuracy, computational efficiency, and generalization capability（JES L305–306） | 三组与中文逐项对应。跨数据集迁移和跨域适应单独保留准确术语，不能被generalization capability替代；不继承范文硬件结果。 |

## 二、引言相关原词：80条按功能检索

原词保留可核实的拼写；大小写、单复数及必要的排版断词修复可规范化。只恢复软连字符断词与换行，不将同义改写称为逐字原词。来源限定在引言/相关工作；个别本文所需方法词在上一表明确标为跨章节补充。

### 背景与任务

| 中文概念或功能 | 确切原词/短搭配 | 对应来源 | 本文使用边界 |
| --- | --- | --- | --- |
| 高能量密度 | `high energy density` | BMS §1背景 L50 | 可直接描述电池特性，不借范文替代本文引文 |
| 长使用寿命 | `long service life` | BMS §1背景 L50 | 不等于中文长循环寿命；不能静默替换 |
| 储能设备 | `energy storage devices` | BMS §1背景 L51 | 不硬套为规模化储能系统 |
| 安全隐患 | `safety hazards` | BMS §1背景 L53 | 只用于背景已有的风险 |
| 内部状态 | `internal states` | BMS §1背景 L62 | 包括SOH，不新增待估状态 |
| 有限存储空间 | `limited storage space` | BMS §1背景 L64 | 用于设备约束，不表示本文已测运行内存 |
| 实际应用 | `practical applications` | BMS §1背景 L92 | 泛指应用，不等于完成部署 |
| 完整充放电循环 | `full charge–discharge cycles` | EAI §1背景 L68 | 保留本文完整或近似完整的限定 |
| 在线应用 | `online applications` | EAI §1背景 L68 | 不要把离线验证写成在线实测 |
| 间接传感器数据 | `indirect sensor data` | EAI §1背景 L68 | 本文可观测运行信号不必硬译成间接传感器 |
| 表征退化 | `characterize degradation` | EAI §1背景 L71 | 可用于HI功能，不等于解释唯一机理 |
| 电池老化机制 | `battery aging mechanisms` | JES §1方法分类 L68 | 只描述综述中的机制依赖 |

### 方法分类与模型综述

| 中文概念或功能 | 确切原词/短搭配 | 对应来源 | 本文使用边界 |
| --- | --- | --- | --- |
| 基于模型的方法 | `model-based approaches` | BMS §1方法分类 L95 | 对应本文模型驱动；不与model-driven轮换 |
| 数据驱动方法 | `data-driven approaches` | BMS §1方法分类 L96 | 可与methods按句法处理，但概念固定 |
| 电化学模型 | `electrochemical models` | BMS §1方法分类 L95 | 具体模型名称和引文以本文为准 |
| 经验模型 | `empirical models` | BMS §1方法分类 L96 | 只在中文有此分类时用，不新增分类 |
| 等效电路模型 | `equivalent circuit model (ECM)` | BMS §1模型综述 L129 | 首次定义后允许ECM/ECMs |
| 数学方程 | `mathematical equations` | BMS §1模型综述 L121 | 不用作具体方程形式的替代 |
| 电路元件 | `circuit components` | BMS §1模型综述 L121 | 与电化学参数区分 |
| 微分方程 | `differential equations` | BMS §1模型综述 L123 | 引言无需展开公式 |
| 颗粒半径 | `particle radius` | BMS §1模型综述 L127 | 不新增难以辨识参数 |
| 扩散系数 | `diffusion coefficients` | BMS §1模型综述 L128 | 按本文物理对象使用 |
| 参数辨识 | `parameter identification` | BMS §1模型综述 L133 | 不与模型训练等同 |
| 历史数据 | `historical data` | BMS §1数据驱动综述 L137 | 不擅加本文没有的历史样本范围 |
| 物理可解释性 | `physical interpretability` | EAI §2.1相关工作 L121 | 与预测精度分开，不自动声称本文具备 |
| 电路结构 | `circuit structure` | EAI §2.1相关工作 L130 | 对应ECM结构依赖 |
| 环境条件 | `environmental conditions` | EAI §2.1相关工作 L131 | 具体温度倍率以本文为准 |
| 高敏感性 | `high sensitivity` | EAI §2.1相关工作 L131 | 高的程度需要对应文献，不能随意加强 |
| 局部特征提取 | `local feature extraction` | BMS §1CNN综述 L155 | 已有feature extraction的具体功能，不另造同义词 |
| 池化操作 | `pooling operations` | JES §1CNN综述 L89 | 只描述被综述网络，不加到本文架构 |
| 时间序列数据 | `time series data` | JES §1RNN综述 L94 | 连字符按名词/定语句法处理 |
| 前面的时间步 | `previous time steps` | JES §1RNN综述 L94 | 适合历史信息传递的对象 |
| 并行计算 | `parallel computing` | BMS §1Transformer综述 L100 | 不等于实测吞吐量优势 |
| 全局依赖 | `global dependencies` | BMS §1Transformer综述 L99 | 全局范围不自动等于所有长期趋势 |
| 全局建模 | `global modeling` | BMS §1Transformer综述 L101 | 用于能力描述，避免把强表征当保证 |
| 局部感受野 | `local receptive fields` | EAI §1CNN限制 L100 | 单层局部限制不等于深层CNN完全不能捕捉长程 |
| 串行处理约束 | `sequential processing constraints` | EAI §1RNN限制 L100 | 对应递推计算，不延伸成所有硬件场景更慢 |
| 阻碍并行化 | `hinder parallelization` | EAI §1RNN限制 L100 | 限定对应串行操作 |
| 二次计算复杂度 | `quadratic computational complexity` | EAI §1注意力限制 L102 | 明确相对于序列长度 |
| 相对于序列长度 | `with respect to sequence length` | EAI §1注意力限制 L102 | 复杂度变量须明确 |
| 时间与内存复杂度 | `time and memory complexity` | EAI §2.2.2相关工作 L218 | 指注意力理论复杂度，不与权重文件大小混称 |
| 局部细粒度退化细节 | `fine-grained local degradation details` | EAI §1注意力限制 L107 | 原词已有基础词表，本轮给引言语境，不重复计为全新概念 |

### HI综述与输入局限

| 中文概念或功能 | 确切原词/短搭配 | 对应来源 | 本文使用边界 |
| --- | --- | --- | --- |
| 模型性能之外 | `In addition to model performance` | JES §1HI过渡 L105 | 原词的对象是模型性能；本文是预测模型，应取承接结构并适配对象，不可整套直用 |
| 电池循环过程 | `battery cycling process` | JES §1HI综述 L107–108 | 对应信号来源 |
| 阻抗谱测量 | `impedance spectrum measurements` | JES §1内阻HI L111 | 只说部分HI需要，不推广为所有内阻测量 |
| 专用仪器 | `specialized instruments` | JES §1内阻HI L112 | 保留本文采集条件 |
| 运行温度 | `operating temperatures` | JES §1温度HI L114 | 不与环境温度无条件等同 |
| 充放电倍率 | `charge-discharge rates` | JES §1温度HI L114 | 本文单位和充放电设置不变 |
| 高质量指标 | `high-quality indicators` | JES §1IC综述 L119 | 质量须有明确含义，不当作空泛褒义词 |
| 滤波方法 | `filtering methods` | JES §1IC综述 L120 | 区别本文实际平滑流程 |
| 基于时间的HI | `time-based HIs` | JES §1时间HI L122 | 从原文time-based HIs extraction取连续短语，修正其整句语法 |
| 微分处理 | `differentiation processing` | JES §1时间HI L123 | 原词可借；不能声称本文全部HI无需微分 |
| 统计特征 | `statistical features` | JES §1时间HI L124 | 不照搬范文具体特征集 |
| 时间差 | `time difference` | JES §1时间HI L130 | 与CCCT实际定义对应 |
| 噪声抑制处理 | `noise reduction` | JES §1时间HI L131 | 无此处理不等于对噪声天然鲁棒 |
| 表征能力 | `representational ability` | JES §1时间HI L133 | 与representational capability择定首选，不能轮换凑词 |
| 更短的充电片段 | `shorter charging segments` | JES §1时间HI L138 | 比较对象须清楚 |
| 测量噪声 | `measurement noise` | EAI §1HI限制 L90 | 本文未做抗噪实验，不宣称解决测量噪声 |
| 平滑预处理 | `smoothing preprocessing` | EAI §2.2.1相关工作 L168 | 取自heavy smoothing preprocessing，不继承heavy程度 |
| 输入冗余 | `input redundancy` | EAI §2.2.1相关工作 L172 | 多源不自动等于冗余，按实际筛选证据 |
| 经验固定电压窗口 | `empirically fixed voltage windows` | EAI §2.2.1相关工作 L178 | 针对具体已有研究，不断言全部现有方法如此 |
| 人工特征工程 | `handcrafted feature engineering` | JES §1联合估计综述 L181 | 可借普通操作名，不引入SOH-RUL联合任务 |
| 原始数据 | `raw data` | JES §1特征综述 L189 | 区别预处理后输入 |
| 退化相关特征 | `degradation-related features` | JES §1挑战 L335 | 相关不等于因果机制 |
| 信息丰富的HI | `informative health indicators` | JES §1挑战 L339 | 需对应退化信息，不能仅因特征多而使用 |

### 研究缺口与贡献

| 中文概念或功能 | 确切原词/短搭配 | 对应来源 | 本文使用边界 |
| --- | --- | --- | --- |
| 计算资源需求 | `computational resource demands` | BMS §1挑战 L167 | 区别参数量、FLOPs与实际耗时 |
| 弱相关健康指标 | `weakly correlated health indicators` | BMS §1挑战 L173 | 本文此处须明确与SOH弱相关；加入with SOH属于适配，不与HI彼此低相关混淆 |
| 超参数配置 | `hyperparameter configurations` | BMS §1挑战 L180 | 不借词新增超参数稳定性主张 |
| 兼顾精度与效率 | `balancing accuracy and efficiency` | BMS §1方法引出 L187 | 目标表述，不等于每项指标均最优 |
| 为应对这些挑战 | `To address these challenges` | BMS §1方法引出 L184 | 连接明确的挑战，不每段重复 |
| 通过逐步缩小 | `By progressively shortening` | BMS §1贡献 L208 | 后接真实窗口/步长操作，不扩为所有HI自适应 |
| 同时降低计算复杂度 | `while reducing computational complexity` | BMS §1贡献 L215 | 比较基准和复杂度分析须成立 |
| 融合多尺度与多通道特征 | `fuse multi-scale and multi-channel features` | BMS §1贡献 L220 | 本文相应模块确实有此功能时采用 |
| 紧凑的参数集合 | `compact parameter set` | EAI §1贡献 L153 | 描述模型规模，不自动等于更快推理 |
| 表征能力（另一原词） | `representational capability` | EAI §1贡献 L153 | 中文应按上下文译为表征能力；与ability统一，不作新概念 |
| 特征比较实验 | `feature comparison experiments` | JES §1贡献 L292 | 对应已有特征对照，不新增实验 |
| 多源输入 | `multi-source inputs` | JES §1缺口收束 L248 | 不等于跨数据集迁移，也不自动等于多模态 |
| 可用计算资源 | `available computational resources` | JES §1缺口收束 L261 | 不假定本文已测MCU限制 |
| 资源受限边缘设备 | `resource-constrained edge devices` | JES §1缺口收束 L262 | 研究场景词，不作为已部署结论 |
| 模型复杂度与精度之间的权衡 | `trade-off between model complexity and accuracy` | JES §1缺口收束 L259 | 不能把训练时间和理论复杂度混在一个指标里 |

## 三、对本文真正重要的词形与语义决定

| 项目 | 本轮决定 |
| --- | --- |
| 模型驱动 | 优先model-based，与BMS/EAI一致；JES的model-driven只作原文备选，不轮换 |
| CCCT | 继续使用现有术语表constant current charge time；JES的charging版本是原文变体，不另立译名 |
| 表征能力 | 首选候选固定为representational capability，允许语法所需复数capabilities；representational ability只保留为范文变体。已登记terminology.md，不再悬置为多个平行候选 |
| 模型→HI过渡 | In addition to可借承接动作；model performance与本文“预测模型”对象不同，需适配，且本文增加selection。不能只补selection就称完成忠实映射 |
| 局部与长期 | local / global描述范围；short-term / long-term描述时间；long-range描述距离。按中文含义选，不以范文同现为由混用 |
| 噪声与预处理 | 可以借measurement noise、smoothing preprocessing；不声称本文所有HI免微分、免平滑或已经提高抗噪性 |
| 复杂度与存储 | 注意力理论时间/内存用time and memory complexity；实验权重文件指标仍是storage size，不互换 |
| 模块名 | 当前冻结引言用SLFA及ReLU²智能体机制。不能被范文LGFA、FLFA、DSCA名称或旧总结覆盖 |
| 组级HI规则 | 保留特征开发电池与其他电池应用范围。JES的across all batteries in a group不是本文完整角色定义 |
| 迁移评价 | 跨数据集迁移和跨域适应不缩写成笼统generalization，也不借范文SOH-RUL或硬件任务扩展本文 |

## 四、仍需另查或明确适配的词

这些概念不能仅靠当前引言词条宣称已经全部确定：

- 长循环寿命：long service life和excellent cycling performance均不精确等同。
- 低自放电率：BMS提取文本有low selfdischarge rate，若修复为low self-discharge rate，标明排版/拼写规范化，不把修复前形式当推荐拼写。
- 容量保持率、最大可用容量：继续复核已定位capacity retention（EAI §3.1 L274）及maximum available capacity（L275–276），现已登记术语表。来源为方法章节，不在引言80条之内；不再标作未找到。
- 活性锂损失、热失控：本轮仍未建立准确原词出处，不能为套范文改成泛泛battery aging。SEI growth可参考EAI §2.1 L119，但不能概括全部老化过程。
- 具体HI峰值、峰位、峰形斜率、PCA及模拟退火：按本文所述研究与实际方法核实；三篇有相近操作，不等于对应引文做了同一件事。
- 组级标定、特征开发电池、PCC/SCC双阈值及冗余约束：完整组合属于本文方案，允许以范文核心词准确适配；方法章节已有原词需标跨章节来源。
- 跨数据集迁移、跨域适应：继续保留本文术语，不能将范文泛化描述当作同一实验协议。

## 五、继续复核：不是词数够了，就能直接翻译

### 采用判定

1. **同一技术对象、同一关系、同一强度**才算可以直接用；仅有字面相似不够。例如表征能力、容量保持率有明确落点，但long service life不能替代长循环寿命。
2. **只借常用词与搭配，不借文献事实。** 本文关于Fei、Dai、Lin等研究的模型数量、输入特征及结论，不能用范文对其他研究的句子替代。范文的词汇证据不是这些引文的事实核验。
3. **词、搭配和完整句子分开标记。** 如JES L105可借In addition to这一承接；后接model performance与本文“预测模型”不是同一对象，必须适配，此外还需保留selection。不能贴“原句直接沿用”标签。
4. **正向陈述不等于消除必要限制。** 中文的“可能”“通常”“单层”“部分”“在所用数据上”等决定适用范围，应保留；不把may造成的有限主张改成确定因果。避免反复防御，不等于避免所有however或转折。
5. **时间、范围与任务分别对齐。** 长期、长程、全局不是同义词；容量估计、SOH估计、早期寿命预测、RUL预测也不能为了统一estimation而改成一个任务。

### 引言各部分应借到的颗粒度

| 本文部分 | 范文可借的层级 | 不随词汇一并带入 |
| --- | --- | --- |
| 背景与SOH测量 | 应用对象、容量测量条件、资源限制；EAI §1 L65–71与BMS §1 L62–79 | 不扩写无关能源材料背景，不把容量定义从本文改为范文版本 |
| 模型综述 | BMS §1的模型类别、代表工作与具体结构限制；EAI §2.2.2的串行/二次开销 | 不把每类模型写成教材，不继承神经细胞比喻、rank collapse和硬件结论 |
| HI综述 | JES §1 L105–138的采集条件、工况影响、时间差提取与片段选择 | 不把本文候选HI概述扩成完整方法清单，不因时间HI简便而删除微分HI |
| 挑战 | 每项问题的对象、造成的具体限制；词汇服务本文已有三项挑战 | 不替换成BMS超参数稳定性、EAI三重问题或JES SOH-RUL联合估计挑战 |
| 贡献 | 新动作、关键机制、价值；多数据集验证的范围 | 不机械照搬范文精确百分比、单智能体、硬件实验或新增数值；本文已有O(N)分析保留其对象 |

尚不能宣称“引言用词已全部冻结”。当前完成的是可追溯取词和首选候选收敛；剩余专有名词及完整句法仍需要在逐段英译时核对，但不先生成整篇粗译稿。

## 六、第三轮独立复核：对象、搭配与颗粒度

2026-09-13：三个独立agent分别审计漏项、语义与颗粒度，初审均提出需调整。已收紧P04/P09/P12/T1/T2及术语表；本节记录新增证据与未解决项，不增加“已冻结词数”。

调整后由独立语义agent最终只读复核：通过。通过范围为本指南的语义与一致性，不代表逐句英译或全部专有术语确认完成。

### 1. 具体操作与名称的补充定位

| 本文落点 | 三篇中可定位的词或搭配 | 采用判定 |
| --- | --- | --- |
| P01：SEI增厚及电极结构衰退 | solid electrolyte interphase (SEI) growth（EAI §2.1 L119）；electrode degradation（JES方法§3.5.1 L1757–1758） | 前者有直接对应；后者不含结构限定。lithium plating不能替代活性锂损失 |
| P04：SPM、电阻电容、Thevenin | single-particle model（BMS §1 L122）；resistors and capacitors（L131）；Thevenin（L132） | 可借准确对象词；递推最小二乘、欧姆内阻、化学退化与机械损伤的完整表达尚未定位 |
| P05：六种传统模型 | Gaussian process regression (GPR)、support vector machine (SVM)、random forest (RF)、gradient boosting regression tree (GBRT)、neural network (NN)（BMS §1 L148–151） | 五种有原词，elastic net本轮未定位；必须保留本文六种，不能为贴范文删掉一种 |
| P07：训练与推理中的并行受限 | limits parallelization during training and inference（EAI §2.2.2 L199–200） | 比单独hinder parallelization覆盖更具体；接本文真实串行操作，不扩写硬件结论 |
| P08：两两关系 | pairwise similarity computation（JES方法复杂度段 L760–761） | 本文若描述序列位置需适配；范文宾语为queries and keys，不无条件替换成positions |
| P09：IC曲线、电压平台及微分 | incremental capacity (IC) curves（EAI §1 L70）；voltage plateaus（EAI方法 L327）；derivative of capacity (Q) with respect to voltage (V)（JES §3.5.1 L1588–1589） | 跨章节原词已标出。原词shifting只描述位移，不能概括中文所有平台变化；不向引言补入微分公式 |
| P09：峰值、峰位 | peak value of the incremental capacity (IC) curves（JES Table 4 L1634）；voltage corresponding to the peak（同表 L1635–1636） | 后者适用于电压坐标的峰位。峰形斜率尚未定位；Discharge voltage curve slope与slope standard deviation的对象/统计量都不同，不拿来顶替 |
| P11：均值、中位数、PCA和模拟退火 | statistical features（JES §1 L124）仅覆盖上位类别 | 具体操作未被此词覆盖；指标公式中的mean不等于该文HI统计均值的来源证据。需保留准确概念，另查或标标准术语适配 |

### 2. 从名词索引推进到关系索引

| 本文关系 | 范文可借的短搭配 | 必须保留的对象或限定 |
| --- | --- | --- |
| P05：将特征输入模型 | fed them into（BMS §1 L146） | them指向本文实际特征，模型列表和任务不变 |
| P06：曲线片段作为输入 | serve as the input（JES §1 L91） | 输入是片段，不把估计目标容量/SOH换成输入 |
| P07：历史信息递推 | recurrently connecting information from previous time steps（JES §1 L94–95） | 保留本文时间步和隐藏状态关系，不将Transformer隐藏表示冒称RNN机制出处 |
| P09：模型之外还考虑HI | In addition to（取自JES §1 L105） | 后接本文预测模型对象；不是直接套model performance |
| P10：时间HI与微分HI比较 | differentiation processing、time difference（JES §1 L123、L130） | 对比提取流程，不能据此宣布时间HI准确性或稳定性全面更好 |
| P12/T1：筛选HI | weakly correlated health indicators（BMS §1 L173）、input redundancy（EAI §2.2.1 L172） | 分别对应HI–SOH关联和HI–HI冗余。跨电池表现作为本文第三个限定；完整关系是本文适配组合 |
| P13：先指比较表，再交代维度 | is summarized in Table 1、Specifically, it is examined whether（JES §1 L310–312） | Table 1替换为本文引用属必要适配；whether后接本文四个比较维度，不照搬范文残缺括号或贬低其他研究的措辞 |

### 3. 三篇分别写到什么级别

| 范文对应部分 | 协议颗粒度 | 数字颗粒度 | 解释颗粒度 | 本文取舍 |
| --- | --- | --- | --- | --- |
| BMS §1贡献，L208–229 | 说明窗口和步长逐渐缩小及双尺度卷积，没有硬件测量协议 | HI贡献给平均PCC超过0.99；模型贡献不给完整误差表 | 说明局部—全局、特征融合和参数开销功能 | 借动作与对象，不移入0.99，不把本文多HI贡献缩成单HI |
| EAI §1贡献，L141–159 | 给单智能体n=1、30%早期训练数据、MCU实现等限定，比另两篇工程细节更密 | 给RMSE 0.0052、精度损失小于0.3%及复杂度量级 | 解释延伸至嵌入式可行性与特征塌缩补偿 | 本文不补训练比例、单智能体或硬件结论；保留现有模型设计与证据范围 |
| JES §1贡献，L268–309 | 给联合SOH–RUL任务、特征筛选与多数据集验证；复杂度比较带N≫d条件 | 给O(N²d)至O(Nd²)及数量级表述，此处不列SOH精度结果 | 将HI表征、卷积多尺度与多任务预测联系起来 | 本文只做已有SOH和迁移任务；O(N)的变量及适用条件以本文分析为准，不借其数量级结论 |

三篇没有共同的整章顺序模板：BMS主要按模型家族推进；EAI先提出HI/模型瓶颈，再单列相关工作；JES从模型转HI后还回到联合任务与模型复杂度。共同提取的是准确术语、短搭配与局部叙事动作，不是用一种抽象“顶刊顺序”重排本文。

### 4. 剩余问题的处理，不再循环堆词

- 对本表已定位的词，逐句英译时核对“谁—做什么—对谁—在什么条件下”，词库不再为同一意思追加同义项。
- 活性锂损失、热失控、elastic net、递推最小二乘、欧姆内阻、峰形斜率、PCA及模拟退火等本轮仍未定位准确来源。未定位不代表这些术语不成立；可以在后续作为准确的标准术语适配处理，但必须诚实标注，而非伪造范文出处。
- 即使解决所有名词，仍需完成句法、引文任务和限定范围检查，才能称对应句子的译法可采用。当前不把词库复核称为引言英译完成。

## 七、本轮完成状态与下一步

已完成：三篇对应内容阅读、本文20处位置映射、80条来源核查、语义差别记录。未完成：引言逐段英译、全部专有译名冻结、正文写入或翻译后编译。本轮只修改指南，因此没有新增LaTeX编译结果。

作者本轮要求继续仔细核对，因此仍停留在引言，不自动进入第2章。引言核对告一段落后，下一批再进入第2章“框架与健康指标”，仍执行“三篇对应部分→本文中文完整小节→能用原词→需适配项”，一次处理一个章节。未开始下一章提取，不能把总词库中已有方法词当作已完成第二章逐段对齐。
