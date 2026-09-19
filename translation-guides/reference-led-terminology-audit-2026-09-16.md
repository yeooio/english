# 按三篇主范文重新清查全文术语（2026-09-16）

实施状态更新：作者随后确认“先改A1到A8”，A1—A8已按范围落实，见 `reference-led-terminology-applied-A1-A8-2026-09-16.md`。下文保留原审查提案记录；B项及其他候选仍未实施。

本报告只提出建议，未修改论文、图像、术语表或中文源稿。作者确认后才可实施。审查基于 `build/reference-term-audit-20260916-144409` 固定快照；行号指该版本，当前工作稿相同位置仍可定位。

## 审查标准和实际范围

同一技术对象优先采用指定主范文的现成词汇：特征工程以 JESSOHRUL（JE）为主，机制和卷积以 BMSFormer 为主，轻量化和资源以 Engineering-AI（SL-AgentNet）为主。准确但另换近义词，也可提出统一；不同物理量、运算阶段、评价协议不能为了相同词形强行合并。

三名新 agent 分别通读摘要及第1—5章、当前引用的表格和图题。第一阶段不读取旧审计、旧术语表或其他人的结论；随后保留独立清单，第二阶段互读、交换异议，并核对旧作者约定。每人都读全文，主参考侧重不等于章节分工。根代理另外通读正文和活动表图文字，并目视核对20个当前引用PNG及存储图PDF。

活动输入链共36份TeX：6份章节、18份表格、10份图及1份共用布局、main。未引用的历史表图不作为当前正文问题。三篇范文按对应功能重读完整段落；不宣称三人都逐字重读了三篇论文的每一页。图内检查由根代理补充，不能说三名agent都独立检查了全部图片。

独立清单中的自动命中包括正常全称/简称和少量检索噪声，例如label里的hi、coefficient里的efficient；这些不是问题数量，也不能用作批量替换指令。本报告以下逐项裁决优先于独立清单的初步建议。

## 一、建议优先确认的范文术语对齐

以下A1—A8共涉及27处文字，已在当前工作稿逐处重新定位；这是候选改动数，不是错误数。对应记录为 `build/reference-term-audit-20260916-144409/proposed-occurrences.json`，没有执行替换。

### A1. 同一HI筛选算法的正式名称统一用 selection

- 现有英文：`Group-level health indicator screening steps.`；`Procedure: Group-level health indicator screening`。
- 建议英文：`Group-level health indicator selection steps.`；`Procedure: Group-level health indicator selection`。
- 位置：`tables/table_2_hi_screening_steps.tex:3,7`；正文第2章143、145、155行已经使用 selection。
- 范文依据：JE `full.txt:1797,1822–1856`，方法称 HI selection，表5也以 selection 命名。
- 范文是否也用 screening：是，JE同时有 screening mechanism/procedure。因此这不是错词判定，而是本文同一算法在正文、正式表题中应采用同一名称。
- 中文理由：统一“组级健康指标筛选”总流程名。`dual-threshold admission`仍保留，它是冗余剔除前的准入子步骤，不能一起改成整个 selection。

### A2. 冗余信息统一用 redundant information

- 现有英文 → 建议英文：`repeated information` → `redundant information`。
- 位置：`chapters/chapter02.tex:155`，1处。第1章已使用 redundant information。
- 范文依据：JE `full.txt:1822–1834`，候选HI按相关强度排序后去除高度互相关特征，以减少 redundant information。
- 同条件：是，本文也是候选HI之间高相关导致的信息重复。只统一名词，不额外增加 highly，也不改变 reduce/remove 的力度。

### A3. PCC所衡量的线性相关统一用 linear correlation

- 现有英文 → 建议英文：`linear association` → `linear correlation`。
- 位置：`chapters/chapter02.tex:108`，2处。
- 范文依据：JE `full.txt:1669–1679`，PCC measures the linear correlation；BMS `full.txt:520–522`则确实用 linear association。
- 同条件：两篇均描述HI与SOH的PCC；按本次“特征工程以JE为主”，建议选 correlation。原词并非统计错误。
- 旧约定：旧术语表曾允许两词并存，本次为重新统一的提案。SCC的 monotonic relationship、普通关系描述及注意力得分不在此替换范围内。

### A4. 充电时间类特征统一用 charging-time features

- 现有英文 → 建议英文：`time features` → `charging-time features`。
- 位置：`chapters/chapter01.tex:21`，3处；`chapters/chapter02.tex:106`，1处。
- 范文依据：JE `full.txt:125–138,1637–1638,1689–1697`，此类HI来自充电电压区间对应的时间；BMS `full.txt:441–459,503–506`提供相同充电时间语境。`charging-time features`是本文已经确定的类别名，并非声称两篇所有地方逐字都用该复合短语。
- 同条件：四处上下文均指充电过程的时间特征，同段及第2章58、60行已有 charging-time feature(s)，因此有现成统一版本。
- 中文理由：不再把同一类别轮换写成泛指 time features；保留 time-based health indicators 这个上位类别及普通物理时长 charge duration。不把整个类别缩窄成HI1或CCCT feature。

### A5. HI的表征能力采用JE的 representational ability

- 现有英文 → 建议英文：`representational capability` → `representational ability`，仅HI语境。
- 位置：`chapters/chapter01.tex:25`，2处；`:36`，1处；`chapters/chapter04.tex:45`，2处，共5处。
- 范文依据：JE `full.txt:1884–1893`直接比较同一HI在不同电池上的 representational ability，与本文第4章该段功能一致。
- 范文是否有其他版本：BMS `full.txt:170–173`对HI也用 representational capabilities；本轮仍按HI主参考JE选 ability。
- 旧约定：旧术语表135行曾统一 capability，本提案改变该约定，须由作者确认。
- 范围：不改模型的表达能力，也不把普通 `ability of selected indicators to represent degradation` 强制名词化。否则只是制造额外改写。

### A6. 卷积核尺度采用BMS的 small/large 和 kernel size

- `chapters/chapter04.tex:156`：两处 `kernel length` → `kernel size`，保留数值5和31及一维卷积含义。
- `chapters/chapter04.tex:158`：`short and long kernels` → `small and large kernels`。
- 范文依据：BMS `full.txt:868–900`明确 small kernel size、large kernel size，并以DSConv-S/L命名；本文第3章已采用 small/large-kernel。
- 同条件：是，同为DSConv-S/L的核尺度。原文 length 不是数学错误，但同一对模块无需再换一组描述词。
- 保留：`features over longer time scales`不改成 `long-term features`。前者保留中文“较长尺度”的限定，不能借范文词把较大的局部核夸为长期或全局建模。

### A7. 图2-2同一组容量曲线采用 capacity degradation curves

- 现有英文 → 建议英文：`capacity fade curves` → `capacity degradation curves`。
- 位置：`chapters/chapter02.tex:23`，1处；`figures/figure_2_2.tex:6`图题已有建议版本。
- 范文依据：JE `full.txt:1409–1425`的数据集曲线介绍采用 capacity degradation curves；BMS相应数据介绍亦使用该名称。
- 同条件：是，正文和图题指同一组容量随循环变化曲线。
- 范围：仅统一曲线名。不把全文的 capacity fade、battery degradation、performance degradation 全部合并；旧稿对物理容量损失的 capacity fade 约定仍保留。

### A8. 资源受限采用SL的 resource-constrained

- 现有英文 → 建议英文：`resource-limited` → `resource-constrained`。
- 位置：`chapters/abstract.tex:1`，2处；`chapters/chapter01.tex:9,17,27,40`各1处；`chapters/chapter04.tex:172`，1处；`chapters/chapter05.tex:1,3`各1处，共9处。
- 范文依据：SL `full.txt:34–46,60–64,118–125`均采用 resource-constrained BMS。BMS的 limited 并非错词；本轮按资源主参考SL统一。
- 同条件：均指计算和存储受限的BMS，中文事实及力度不变。
- 旧约定：术语表69行记载作者曾为与Cover Letter一致选择 limited。若批准本项，应另核对投稿材料中的同词；本轮没有修改或声称已检查Cover Letter。

## 二、需要选定一种名称后同步的同对象项目

### B1. 权重文件大小：建议采用SL的 model size，但保留本文测量定义

- 现有版本：正文 `weight storage size / storage size`，表头 `Storage (KB)`，图轴 `Storage size (KB)`，流程图效率框 `Model size`。
- 建议：作为本实验正式指标统一为 `model size`；表头/图轴 `Model size (KB)`。第一次定义仍明确它是保存模型权重所需的文件空间，保留 `os.path.getsize` 测量说明。
- 位置：`chapters/chapter04.tex:145,166,170,172`中的该项指标；`tables/table_4_12.tex:10`；`figures/figure_4_4.tex:4`；`figures/fig4_storage_scaling.pdf`主图和内嵌图纵轴。`figures/fig1.png`已有Model size，可与新名称对齐。
- 范文依据：SL `full.txt:2430–2439`正式列出 Model Size (Storage)；BMS `full.txt:1359–1387`采用storage size及getsize，后者测量方式与本文更接近。
- 条件并非完全相同：SL把该量解释为Flash占用，本文测量的是保存后的权重文件。借用指标名，不复制Flash、运行时内存或已部署声明。第1章27行“扩大模型规模”的 model size 是架构规模语境，不批量改写。
- 另一可行方案是全部统一 `weight storage size`，更贴合当前定义；按本次SL词汇优先，推荐上述 model size 方案，留待作者选定。

### B2. 本文输出层明确为 linear readout layer

- 建议：`chapters/chapter03.tex:5`的 `a linear readout` → `a linear readout layer`；`tables/table_4_4.tex:17`仅MS-AgentNet列末层的 `Linear layer` → `Linear readout layer`。
- `chapters/chapter04.tex:117,132`等在定义后使用 `readout layer`是正常简称，可保留。
- 依据：本文结构说明和迁移实验明确是同一输出层；BMS `full.txt:729–745`的MLP输出设计不等于本文线性读出层，不能为仿范文改为MLP。此项是内部命名对齐，并非宣称范文有相同层名。

### B3. 源域直接测试统一标作 source-only evaluation

- 表题建议：`tables/table_4_7.tex:3`的 `Direct cross-dataset transfer results.` → `Results of source-only evaluation across datasets.`。
- 流程图建议：`figures/fig1.png` Transfer框的 `Source-only testing` → `Source-only evaluation`。
- 依据：`chapters/chapter04.tex:117–125`已明确定义训练后不使用目标域数据更新参数的source-only协议；两处指同实验。三篇所读对应段没有与本文完全相同的两域实验，不伪称这是照搬范文术语。
- 保留：few-shot adaptation及target-domain adaptation ratio属于另一设置和其参数，不并入此词。

### B4. 组合平均误差采用 combined average error

- 位置：`tables/table_4_10.tex:7`、`tables/table_4_11.tex:7`，两列 `Average` → `Combined average error`。
- 依据：正文 `chapters/chapter04.tex:152–158`以此名称指相同的跨指标组合平均。BMS的ARMSE等并非该量，不能套其简称。
- 范围：其他表对不同电池的 `Average` 行是另一平均对象，保留。

### B5. 流程图跨电池名称采用 cross-cell

- 位置：`figures/fig1.png` Generalization analysis框。
- 现有英文 → 建议英文：`Cross-battery and cross-dataset evaluation` → `Cross-cell and cross-dataset evaluation`。
- 依据：本文第4章83、101行的正式设置名为cross-cell generalization；JE `full.txt:1970–1985`讨论跨电池表现。这里按本文同对象既有词统一，不把cross-dataset transfer也改成cross-cell。

### B6. 注意力得分、广播权重和权重矩阵分层统一

| 对象 | 现有英文 → 建议英文 | 范围 |
|---|---|---|
| 未归一化匹配得分 | correlation scores → similarity scores | chapter03:229，1处；:311，3处 |
| 查询与智能体的匹配得分 | query-agent matching scores → query-agent similarity scores | chapter03:347，1处；可随上一项同步，保留匹配双方限定 |
| 未归一化得分矩阵 | correlation matrix → attention score matrix | chapter03:242，1处；可随得分名称同步，不能改成weight matrix |
| 广播阶段归一化权重 | context weights → broadcasting weights | chapter03:294，1处；:347已有broadcasting weights |
| RAA归一化后的两矩阵 | correlation matrices → attention weight matrices | chapter03:363，1处，对应前述Phi_k和Phi_q |
| 这些矩阵的权重 | correlation weights → attention weights | chapter03:363，1处 |

- 范文依据：BMS `full.txt:974–1035`区分query-key similarity、similarity values和attention weights；BMS不是逐字使用similarity scores，完整短语由JE `full.txt:550–559`补充支持。必须如实区分主参考词义依据与补充参考原词。
- 同条件：均为注意力归一化前后量，但本文RAA采用ReLU²归一化，不能照搬Softmax公式。此项只统一数值对象名称，不改运算。
- 不动：第2章PCC/SCC的correlation matrices；第3章242行原始QKᵀ矩阵不能改成attention weight matrix。普通scores/weights作为上下文已经明确的简称可保留。
- 定性：当前语境多能判断所指，属于加强统一和分层，不把所有correlation表述判为数学错误。

### B7. 逐点卷积融合的对象统一称 features

- `chapters/chapter03.tex:139`：`fuses information across channels` → `fuses features across channels`。
- 依据：同章68行已用建议词组；BMS `full.txt:800–818`说明逐点卷积mixes the features across all channels，两处同为PW卷积融合通道特征。
- 不把所有information全改成features：原始退化信息、注意力上下文和神经网络特征具有不同指向。这里仅统一同一种卷积操作的宾语。

### B8. QKV投影矩阵采用完整的 linear projection 名称

- `chapters/chapter03.tex:205`：`learnable projection matrices` → `learnable linear projection matrices`。
- 依据：BMS `full.txt:945–949`的完整名称为learnable linear projection matrices；本文式Q=XW等确为同种线性映射，288行已用standard linear projections。
- 保留：RAA的逐通道缩放不是这些完整线性投影矩阵，不能把channel scaling vectors也改成projection matrices。

## 三、已经核查，但不建议直接批量改的候选

| 候选 | 最终处理及理由 |
|---|---|
| 模型 representational capability → capacity | 单列选择项。BMS `full.txt:882–890`确有capacity，但主范文不只一个版本，且旧稿已有capability约定。若要按对象固定，可模型capacity、HI ability；不将正常句法can represent全部改写。涉及第1章13行1处复数、27行2处模型语境。 |
| parameter count / number of parameters | 保留正文parameter count：SL结论 `full.txt:2821`已有原词。Parameters表头是简称，最多在表4-12:10补为Trainable parameters以呼应测量对象，不进行全文同义替换。 |
| computational cost / load / overhead | DSConv公式量已经采用computational cost；普通负担叙述并非新指标定义。渐近阶computational complexity、前向FLOPs、训练秒数不能合并。 |
| resource overhead / resource consumption | SL资源权衡段 `full.txt:2440–2453`支持consumption，可对第4章166行和结论3行的总资源概念提案；不必替换所有computational and storage overhead，更不能把计算和存储两个分项删成笼统resource。 |
| time and memory overhead → complexity | 第1章40行描述随N增长的复杂度，可统一为time and memory complexity，与第1章17行呼应；原句也可解释为实际开销趋势，列可选，不报明确错误。 |
| CVT的charging / charge | 保留charging voltage–time。JE同时有charge voltage和charging voltage time，正常构词不必再造一套全称。CVT是曲线，CCCT是时长指标。 |
| voltage window / interval / input window | 搜索窗口、物理端点区间、时序采样窗口不同；保留明确限定。同一已定义窗口的正常简称不强制展开。 |
| cross-cell stability / consistency | 前者为方法期望的跨电池稳定性，后者第2章158行具体描述两个电池相关系数接近；不凭词形一概认定两个专名。 |
| long-term / long-range dependencies | BMS摘要和方法本身采用不同词；本文RNN长期记忆、Transformer跨位置关系及近期确认的LLGFA表述分别保留。不能全篇替成单一版本。 |
| context / feature / information aggregation | RAA正式阶段可固定agent aggregation和information broadcasting；一般聚合对象/含义描述不强制改成一个专名。不要借SL的Gated Broadcasting给本文新增门控结构。 |
| global interactions / cross-position interactions / context | 操作、覆盖范围及操作输出分别核对，context不能改成interactions或dependencies。RAA为本文机制，BMS没有这个相同模块，缺少可直接复制的唯一同对象词。 |
| prediction / estimation | 正式任务名SOH estimation已一致。predicted SOH是输出值，文献寿命prediction是另一任务；JE自己的SOH段也用prediction。结果段局部统一estimation可选，不批量改预测相关词。 |
| MIT / MIT/Severson | 同一数据集的全称和简称，可在首次定义简称或将第4章65、101、158行及表4-3/10/11统一全称。没有证据表明误指另一数据集，不能等同错误标签。 |
| Training robustness / stability、收敛统计简称 | 泛化稳健性、训练稳定性和阈值epoch有各自对象。表4-3可把Late loss写成Late-stage loss，保留median、SD及末20轮定义；属于标签精细化，本轮不列核心改动。 |
| 特征开发set / cell set / cells | 首次定义、集合简称和成员的语法差异，保留。不能借范文all cells改掉本文特征开发集与测试集边界。 |
| FFN / MLP；embedding / hidden dimension | 不同模型模块及维度对象，保留。数值相同不代表同一技术量。 |
| IC/DTV/DTC、peak/valley value、峰位、FWHM | 自有HI名称总体已对齐；DTC峰位对应容量，IC/DTV峰位对应电压。新增半峰宽不因范文未用而删除；文献表FV6需来源定义支持，不能盲改。 |
| rated / nominal capacity | 按中文和定义保留额定/标称区别。相同数值不能单凭词形强并。 |
| local capacity recovery | 已采用JE相同词，不再跟SL改成capacity regeneration。 |

## 四、图内另行记录的专名问题

这些与上面的范文词汇统一分开，避免把作者已知旧图问题充当本轮主要新发现。

1. **明确标签冲突**：`figures/fig2.png` 的(c)标题为CALCE CX2，图例却写CS2_36、CS2_37、CS2_38。需核对生成数据归属后改为相应CX2标签；不能只改图例就宣称曲线数据也正确。
2. **已知旧模块名**：`figures/figure_3_3.tex:6`和`tables/table_4_4.tex:12`仍有SLFA；`figures/01.png`及图1内嵌结构图有SLFA、L-DSConv，图3-3内有Skim Local-Global Fusion Attention。按作者已确认名字同步LLGFA、DSConv-L；不改LaTeX内部label，也不改冻结中文稿。
3. **流程图对象名称**：图1 `Health indicators splitting` 实际是HI时间序列切窗，可提案 `HI sequence segmentation`。这不是JE逐字原词证据，而是让标签所指对象和正文一致。
4. 存储图内嵌坐标 `MS-A / CNN-T / Trans. / CNN-L / LSTM`属于空间受限的短标签，与同图完整图例一一对应，不再定义新模型。
5. 13幅结果图的模型图例名称一致；`Reference`与正文true SOH为图例角色名和具体物理量称谓，可保留。热图SoH/SOH大小写是次要格式项，不挤占本轮核心术语清查。

## 五、审查记录与修改边界

按章节查阅：摘要主要见A8；引言见A4、A5、A8；第2章见A2—A4、A7；第3章见B2、B6—B8及机制边界裁决；第4章见A5、A6、A8、B1、B3、B4；结论见A8。表格和图片另见A1、B1—B5及第四节。

- 独立第一阶段记录位于固定快照目录：`independent-je.md/json`、`independent-sl.md/json`、`independent-bms.md/json`。
- 第二阶段裁决分别为 `peer-je.md`、`peer-sl.md`、`peer-bms.md`。初始候选被撤回或缩小范围均保留痕迹；不把三人一致当成无需核对原文的证据。
- 三方交叉复核已完成。主要分歧的最终处理：保留LLGFA的long-term、DSConv-L的longer time scales、准入admission、原有cross-position context；不把global interactions标成范文原词；注意力得分/权重分层列入B6。存储指标名称保留两方案及不同测量条件，明确推荐范围，交作者决定。
- 本轮没有改正文，不需要用“编译通过”替代术语证据，也未重新编译论文。
- 审查期间chapter01第21行CCCT定义句发生外部更新，根代理已对照；术语位置未变。实施时必须在最新工作稿逐处核对，不用快照覆盖当前文件。
- 本轮清查不能保证绝对零遗漏。可审计的依据是全文覆盖、概念位置清单、对应范文语境、同行异议与逐项裁决，而不是agent数量或搜索命中数量。

## 六、作者确认后的B项实施状态 — 2026-09-16

作者确认按BMSFormer的同对象用词实施B1、B2、B3、B5、B6、B7、B8，并明确B4不应采用超过范文说明颗粒度的处理。已据此完成以下文字订正：

- B1以BMSFormer的`storage size`为正式指标名，保留`os.path.getsize`及“保存模型权重所需空间”的测量定义；表4-12改为`Storage size (KB)`。
- B2统一本文输出层为`linear readout layer`；不套用BMSFormer的MLP结构。
- B3表4-7统一为`source-only evaluation`；流程图中的`Source-only testing`由作者另行修改。
- B4保持原表头`Average`和正文`combined average error`，未增加定义或公式。BMSFormer仅用于校准说明颗粒度，不作为相同平均对象的逐字术语依据。
- B5正文既有`cross-cell`保持；流程图中的`Cross-battery`由作者另行修改。
- B6区分归一化前的`similarity scores / attention score matrix`与归一化后的`attention weights / attention weight matrices`。
- B7按BMSFormer相同逐点卷积语境统一为`fuses features across channels`。
- B8标准QKV矩阵统一为`learnable linear projection matrices`，RAA通道缩放向量不变。

本批未实施第三节其他可选候选；中文源稿未修改。XeLaTeX编译成功，生成37页PDF；第3章相关页面及表4-4、表4-7、表4-12页面检查通过，无新增溢出、缺字或未定义引用。
