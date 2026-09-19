# 全文专业术语对齐与同概念多版本核查

日期：2026-09-16。状态：仅审查建议，未修改论文、图片、冻结中文或规范术语表。

后续状态：作者随后授权直接修改并要求独立agent再次查漏；T01、T02、T04已实施，T03保留原文。实际修改及验证见 [落实记录](technical-terminology-applied-2026-09-16.md)。以下保留本报告形成时的审查判断，不将历史建议重新写成当时已落实。

**作者最新范围**：重点是电池、健康指标、建模与实验中的专业概念及称谓，不把作者已知但尚未同步的 SLFA/LLGFA、L-DSConv/DSConv-L 图表旧名作为主要发现。不做一般句式润色，不以问题数量为目标。

本次通读当前摘要及第1—5章，并由三名审查者分查健康指标、建模、实验术语；检查当前实际引用的表格、图题和相关图中文字。当前英文以 chapters/、tables/ 和活动 figures/ 文件为准，不把历史对照稿、冻结中文、未引用表格、内部 LaTeX 标签或参考文献题名中的异名算作正文问题。三篇范文按对应完整语境重读；TXT 双栏错序不作为句间关系证据。

下列是本轮最终判断，覆盖 tmp/term-audit-ch2.md、term-audit-ch3.md、term-audit-ch4-5.md 中较早的候选优先级。历史候选保留，但旧图名称、合理简称、不同计算对象不计入本轮主要问题。

**总体判断**：没有发现正文核心专业术语大面积未对齐。比较明确的规范统一对象是充电时间特征和材料体系两组；全局上下文、最终HI子集属于可选的范文原词复用。以下不把“可以统一”写成“技术错误”。

## 一、建议统一的两组专业称谓

### T01 充电时间特征：time / duration / timing

- 当前：`chapters/chapter01.tex:21` 的 `charging-time features`、`:44` 的 `charging-time feature`；`chapters/chapter02.tex:58` 的 `charge duration feature`、`:60` 的 `charge timing features`。
- 对象：都在指由充电电压区间两端的时间差得到的时长类HI；第2章承接刚定义的CCCT。
- 建议：作为特征类别的名称统一为 **charging-time feature(s)**。HI1已明确时可直接称 **CCCT feature**，这是具体指标与类别的关系，不另立同义名称。
- 最小替换：第2章58行 `the resulting charge duration feature` → `the resulting charging-time feature`；60行 `In addition to charge timing features` → `In addition to charging-time features`。
- 中文核对：保留“充电时间/时长类特征”，不改成充电调度或事件时机。`timing` 在当前上下文仍能消歧，但比 `time` 更容易使人想到时机；因此建议统一，而非认定整个句子技术含义错误。
- 保留：第2章52行描述物理现象的 `charge duration` 是“充电持续时间”，不是给HI重新命名，不必替换。
- 三篇校准：BMSFormer §2.3，`full.txt:457–459` 使用 `constant current charge time (CCCT) series`，`:503–506` 使用 `constant current charging time`；JESSOHRUL 引言 `:122–138` 讨论基于时差的HI，表4 `:1637–1638` 使用 `The charge time within the voltage range`，与本文条件相同。Engineering-AI `:327` 的 `CC phase duration` 描述物理时长，但其HI是电压积分面积，不能把它的CCCA/CCDA名称替换本文CCCT。
- 批准状态：引言 `charging-time features` 已见 approved-translations.md 的对应批准段。此处是让第2章的特征称谓与已用名称一致，不改已确认技术定义。

### T02 电池材料体系：chemistries / material systems

- 当前：摘要使用 `different chemistries`；`chapters/chapter01.tex:27` 使用 `battery chemistries`；`chapters/chapter02.tex:13、23` 使用 `material systems`；`chapters/chapter05.tex:5` 又使用 `battery chemistries`。
- 建议：在指NCO/LCO/LFP等电化学材料体系的地方统一为 **battery chemistries**。第2章13行 `different material systems` → `different battery chemistries`；23行 `differ considerably in material systems` → `differ considerably in battery chemistries`。
- 跨章联动候选：第1章48行及第4章103行的 `battery materials` 若同样指这些数据集的化学体系，也采用 `battery chemistries`。不能不看对象就全局替换 materials。
- 保留：`cathode material`、`anode`、电极组成等具体材料名称；第2章的 `battery systems` 若概括封装、容量和工况，是更宽的概念，也不直接替换。
- 三篇校准：Engineering-AI §2.2.1 `full.txt:177–181` 明确以NCM/LFP说明 `battery chemistries`，数据采集 `:317–318` 和图2 `:369–371` 也使用该词；JESSOHRUL §3.5.2 `:1786–1796` 在跨电池HI筛选中用 `battery chemistries`；BMSFormer 摘要 `:37` 使用 `different chemistries and operating conditions`。不过BMSFormer数据集部分 `:426–439`、JESSOHRUL贡献部分 `:303–305` 也用 `materials`。因此现有 materials 并非没学范文，而是本文同一概念已有首选后仍出现不同称谓。
- 判定：建议规范统一，不认定现译构成科学错误。中文“材料体系”及全文LCO/NCO/LFP描述支持使用chemistries。

## 二、可选复用，不列为确定错误

### T03 跨位置上下文 → global context

- 当前：`chapters/chapter03.tex:108、384` 的 `cross-position context established by ...`。
- 可选：这两处指RAA在当前输入序列全部位置上聚合所得、再与局部特征融合的信息，可以使用 **global context**。
- 范文：Engineering-AI §4.3.2 `full.txt:1011–1014` 使用 `global context` 与 `local features` 进行融合；JESSOHRUL `:749–753` 使用 `local feature extraction` 与 `global context modeling`。BMSFormer §3.3.3 `:1072–1077` 的局部—全局注意力提供相近功能语境，但不能声称它也逐字使用此词组。
- 条件：三篇具体注意力结构不同；这里只复用“在序列范围内聚合所得上下文”的概念名，不继承Engineering-AI的rank-1结论或单智能体门控机制。global是当前N个输入位置的范围，不表示电池全寿命信息。
- 边界：中文原词是“跨位置上下文”，当前英文精确对应，且已有批准过的整句；因此只能列可选建议。`cross-position interactions` 是交互过程，不能一并替换成上下文这个结果名词。

### T04 最终HI子集的称谓

- 当前：第1章44行 `a health indicator combination`；`tables/table_2_hi_screening_steps.tex:17` 的 `the final selected HI set`。
- 可选：作为候选池筛选后的最终输出，可统一为 **final HI subset**。该词是 terminology.md 已收录的首选。
- 范文：JESSOHRUL §3.5.2 `full.txt:1822–1834` 从候选HI经相关性与冗余筛选，最后使用 `the final HI subset`；功能与本文相同，但阈值和数据角色不照搬。BMSFormer §2.3与Engineering-AI §3.3主要搜索时间/积分窗口，不能用它们的单指标命名覆盖本文多指标集合。
- 保留：表步骤4初始化的 `selected HI set` 是正在构造的集合，不加 final；第4章Fusion指实际组合输入，不是筛选输出的同义词。中文引言写“健康指标组合”，现译没有错，所以不是必须修改项。

## 三、逐章检查与保留结论

### 摘要

已核对 `state of health (SOH)`、`battery management systems (BMS)`、`health indicators (HIs)`、`multi-source health indicator extraction and optimization algorithm`、`depthwise separable convolutions`、`long-range degradation dependencies`、`linear complexity`、`feature diversity`、`computational and storage overhead`。

- 整体HI算法名称与第1、2、5章一致；局部步骤HI extraction/selection不是另外一套整体算法名。
- `SOH estimation framework` 包含HI处理和网络；`prediction network` 指MS-AgentNet网络本身，不强制统一成一个名称。
- `lightweight` 和 `efficient` 分别是轻量化与高效，不作为同义词轮换；当前使用与已批准区分一致。
- 三篇摘要均已重新读取。BMSFormer提供local-global、DSConv、multi-scale/multi-channel等术语；Engineering-AI提供lightweight、linear complexity、long-range degradation dependencies；JESSOHRUL提供multi-source HI及PCC/SCC筛选语境。未发现新增需改的核心术语。

### 第1章：电池机理、方法分类和研究问题

已核对以下组：

| 概念组 | 当前专业名称 | 判定及可定位依据 |
| --- | --- | --- |
| SEI机理 | solid electrolyte interphase (SEI)；thickening；loss of active lithium | 不把interphase改成interface，也不以范文lithium plating替换不同机理。Engineering-AI §2.1 `full.txt:115–124`；本文术语表有单独批准。 |
| 容量与安全 | capacity fade；capacity retention；maximum available capacity；thermal runaway | 对象不同，命名已稳定。Engineering-AI §3.1 `:271–276`支持capacity retention和maximum available capacity；不能合并fade与retention。 |
| 方法分类 | model-based / data-driven approaches | 已采用BMSFormer `:94–97`、Engineering-AI `:183–187`。JESSOHRUL的model-driven是另一范文变体，不要求本文跟换。 |
| 物理模型 | electrochemical models；single-particle model；equivalent circuit models；Thevenin model | 已采用对应专业名称，BMSFormer `:120–136`；不同模型不能合并。 |
| 机器学习模型 | elastic net；GPR；SVM；RF；GBRT；NN | 与文献对应模型各自命名，BMSFormer `:145–151`提供多项原词。不是必须改用一个“regression”后缀。 |
| 神经网络 | CNN、RNN、LSTM、GRU、Transformer及引用文献的混合模型 | BMSFormer `:153–160、191–207`、JESSOHRUL引言对应段均有原词。CNN-BiLSTM-AM不等于实验基线CNN-LSTM。 |
| 依赖与感受野 | local receptive field；long-term dependencies；long-range dependencies | Engineering-AI `:98–103、208–211`本身两种dependencies都用；不因long-term/long-range字面不同就判为错名。 |
| 表征能力 | representational capability / capabilities | 已复用Engineering-AI `:152–153`、BMSFormer `:170–173`；单复数不算多版本。 |
| HI和容量现象 | time-based health indicators；health indicator selection；capacity recovery | JESSOHRUL `:122–138、285–295`均有相同核心词。不需要改成capacity regeneration。 |

引言中的 `differential thermal voltammetry` 是介绍所引文献的称谓，已获对应段批准；不能因第2章自己的DTV用另一长名就静默改掉所引方法名称。

### 第2章：特征名称与筛选术语

主要建议为T01、T02；T04为可选。其余核对如下。

| 概念 | 当前用词 | 判定 |
| --- | --- | --- |
| 四类曲线 | charging voltage–time (CVT)；incremental capacity (IC)；differential temperature–voltage (DTV)；differential temperature–capacity (DTC) | 与JESSOHRUL §3.5.1 `full.txt:1575–1590`、表4 `:1634–1647`的核心名称一致。Charge/charging为词形适配；CVT曲线不能与提取出的CCCT时差混为一物。 |
| 时差指标 | constant current charge time (CCCT) | 与BMSFormer §2.3 `:457–459`一致，正文和表2-2一致。不改成电压积分面积CCCA。 |
| 峰值及峰位 | peak value；voltage/capacity corresponding to the peak；valley value | 与JESSOHRUL表4相同。peak position为概括，具体自变量需要保留，不把电压峰位和容量峰位合并。 |
| 本文其他HI | full width at half maximum；peak-to-valley difference；discharge capacity within a voltage window；energy efficiency | 对应不同数学定义；范文未列同一个特征不意味着应换成它列出的峰值/积分指标。不能声称所有长名均逐字取自范文。 |
| PCC/SCC | Pearson correlation coefficient；Spearman correlation coefficient | 全称和缩写一致；JESSOHRUL `:1669–1677`。 |
| PCC描述 | linear association / linear correlation | **保留或可选内部统一，撤回“未对齐”候选**：BMSFormer `:520–522`在PCC定义中直接使用linear association；JESSOHRUL `:1673–1675`用linear correlation。两篇在相同条件下都支持，不能把前者说成非专业用词。 |
| SCC描述 | monotonic relationship / monotonic correlation | 前者描述关系性质，后者结合相关系数结果；未混同为所有非线性关系。 |
| 提取与筛选 | extraction；selection；screening procedure | 不合并提取和选择。JESSOHRUL同一筛选段 `:1797、1833–1834`兼用selection与screening；当前不作为高优先级问题。 |
| 窗口 | voltage interval；voltage window；window width；step size | 范文也在同一搜索语境兼用window/interval（Engineering-AI §3.3.2 `:373–429`）。电压窗口、序列滑窗、平滑窗口是不同对象，不能批量改成一个称谓。 |
| 容量基准 | rated capacity；nominal capacity | 对应SOH分母和数据集规格描述；保持中文条件，不按近义词全局替换。 |

### 第3章：建模专业词

已重新对照BMSFormer §3.1–3.3、Engineering-AI §4.1–4.3、JESSOHRUL §2.1–2.2。T03是可选复用候选，其余核心术语保留。

| 当前用词 | 为何不统一成一个词 |
| --- | --- |
| depthwise separable convolution / depthwise convolution / pointwise convolution | 总体结构与两个内部操作不同。三篇相应卷积方法部分均作区分。 |
| channel scaling / channel expansion | 本文前者逐通道乘权重，后者增加通道数；不能把scaling改成linear projection。JESSOHRUL `full.txt:900–903`支持expansion语境。 |
| embedding dimension / feature embedding dimension / hidden dimension | 前两者是全称与简写；LSTM hidden dimension属于不同模型对象。Engineering-AI `:819`使用feature embedding dimension；JESSOHRUL `:901`使用embedding dimension。 |
| feature representation / feature embedding | 表示是广义结果；embedding还指输入映射阶段。BMSFormer `:883–890`描述attention representation，不能只为词统一删除阶段差别。 |
| locality bias | 已直接复用Engineering-AI `:875`，不用改成local inductive bias。 |
| feature refinement over longer time scales | feature refinement有Engineering-AI `:814、845、898`支持；时间尺度限定来自本文，不照搬其不同模块功能。 |
| agent aggregation / context aggregation / information broadcasting | agent和context分别说明执行者、对象；aggregation/broadcasting与Engineering-AI §4.3对应。不能照搬Gated Broadcasting这个不同机制的完整名称。 |
| feedforward neural network (FFN) / MLP | 本文FFN名称稳定；表中其他比较模型的MLP不必改成本文FFN。JESSOHRUL `:582–585`有feedforward neural networks。 |
| linear readout / readout layer | 结构限定与层名称，指向明确；不能为了范文复用改成别人的MLP结构。 |
| layer normalization / LN / LayerNorm；row normalization；Softmax normalization | 第一组为全称与缩写；后两种运算不同，必须保留区别。 |
| Softmax attention / linear attention / Agent Attention / ReLU² Agent Attention | 不同注意力机制，不因共同包含attention而统一名称。 |

ReLU²排版与普通句中的大小写已有批准，不属于核心术语多版本。作者已知旧图模块名不在本轮优先项中。

### 第4章：评估、资源和迁移

重新对照BMSFormer §4.2.2、JESSOHRUL §4.2与§4.4.2、Engineering-AI实验复杂度及部署部分。未发现应升级为主要问题的专业概念混用。

| 词组 | 判定 |
| --- | --- |
| mean absolute error / MAE；mean absolute percentage error / MAPE；root mean square error / RMSE；coefficient of determination / R² | 任务内完整名和缩写稳定。R²字符/数学排版不是不同指标。 |
| combined average error / average MAE, RMSE, and MAPE | 前者为综合指标（正文152、154、158行），后者为三个指标分别跨电池平均（43行等）；计算对象不同，不合并。表中Average可选写完整，非本轮重点。 |
| SOH estimation / prediction accuracy / predictive performance | SOH任务名称稳定；后两者是一般模型输出表现，JESSOHRUL同一SOH实验 `full.txt:1970–1990`也如此使用，不强行全部改成estimation。 |
| model complexity / computational complexity / computational cost | 总体模型复杂程度、理论运算规模关系、计算成本有不同用途，不视作同一专名多译。 |
| parameter count / trainable parameter count / Parameters | 首次定义统计可训练参数后可简写，未发现切换计算对象。 |
| weight storage size / storage size | 第166行已定义权重文件大小，后续简写未变成运行内存；完整名称可固定，但不是概念错误。 |
| memory complexity / storage requirements | 理论注意力矩阵内存与更广义资源需求，不把它们全部替换成权重文件storage size。 |
| cross-cell generalization / cross-dataset transfer / cross-domain adaptation / source-only evaluation / few-shot adaptation | 分别是域内泛化、跨数据集任务、适应能力与两类具体协议。与正文定义对应，不能借范文近义词抹去实验数据使用边界。 |
| training cell / configuration-selection cell / source-domain reference cell / target-domain reference cell | 主实验与迁移实验角色不同，不能一律改成training/validation cell。 |
| capacity fade / degradation trajectories | 具体容量下降与广义退化轨迹，当前对象区分合理；不把每个degradation改成fade。 |

MIT/Severson与MIT可统一显示方式，但属于数据集简称，本轮不把它当作重要专业概念问题。

### 第5章：结论与前文复核

- 整体HI算法、MS-CCCT、PCC/SCC、dual-threshold admission、redundancy removal与第2章对应，没有另起一套筛选方法名。
- RAA、static learnable agents、information aggregation and broadcasting、multi-scale depthwise separable convolutions与第3章对应。
- `in-domain cross-cell generalization`、`cross-dataset adaptation`、`lightweight domain adaptation`分别是已做的域内泛化、讨论中的跨域适应和未来工作方向，不应因含generalization/adaptation就统一。
- `computational efficiency`和电池`energy efficiency`不是同一个效率概念；结论无混用。

## 四、采用建议

优先处理T01、T02这两组正文专业称谓；T03、T04由作者选择是否进一步靠拢范文原词。其余已核查项目保留。尤其不要把上述“保留”清单再次转成同义词批量替换任务。

本轮只生成本审查记录；未实施任何论文或图片更改，也未将建议写成已批准规范。
