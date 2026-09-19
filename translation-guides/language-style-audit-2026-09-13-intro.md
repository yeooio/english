# 英文语言与范文风格审校：摘要及第一章（2026-09-13）

本报告执行作者最新阶段要求：以现有英文的直接性、自然度和范文语境为主，中文仅用来约束信息与力度，不再次逐段回译。仅提出建议，论文正文未修改。

本批通读了当前abstract及chapter01–chapter05英文正文。目标覆盖摘要、关键词、第一章21个自然段及2个小节标题，共25块。建议只涉及其中5个自然段；其余20块逐项列为保留。对主要术语、算法/电池角色、比较范围、数字与引文的要求沿用现行术语表。五项建议不是五项确定错误：其中LS-I02收益较小，明确为可选。

本批重新查看的原文包括：BMSFormer full.txt摘要30–40、引言49–234；Engineering-AI full.txt摘要34–47、引言容量限制65–96、模型116–139、贡献141–159、深度模型197–225；JESSOHRUL full.txt摘要33–50、引言60–140、问题244–263、验证贡献303–309、HI筛选1671–1680与1786–1834。涉及跨页和双栏错序时，另外查看了JESSOHRUL PDF第13、14页的既有渲染，以及BMSFormer PDF第2页的既有渲染，确认段落接续。本轮没有把TXT中穿插的DTV说明接到HI筛选段中。每项以下均给重新核对的完整段落范围及短引；短引恢复跨行断词，中文释义为助手说明。

对齐范围为六层：术语、动词搭配、句子主干、句间推进、信息颗粒度、表达力度。参考论文也有绕写、冗余和强断言，优先借其明确对象—动作的对应表达，不为贴近范文删除本文必要内容或重排论证。

## LS-I01｜chapter01.tex:3

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:3)；[中文边界](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:3)。

现有英文：

```tex
Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurate measurement of a battery's maximum available capacity requires full or nearly full charge-discharge cycles, a requirement that is difficult to meet in online monitoring\cite{ref10,ref11}. Consequently, indirect estimation of SOH from observable operating signals has become a key approach to online health monitoring. However, complex operating conditions make the stable extraction of degradation information more difficult, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity. These limitations pose a dual challenge for online SOH estimation: extracting degradation information and maintaining model computational efficiency\cite{ref31}.
```

建议英文（仍为一个自然段）：

```tex
Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurate measurement of a battery's maximum available capacity requires full or nearly full charge-discharge cycles, a requirement that is difficult to meet in online monitoring\cite{ref10,ref11}. Consequently, indirect estimation of SOH from observable operating signals has become a key approach to online health monitoring. However, complex operating conditions make it harder to extract degradation information consistently, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity. These limitations pose a dual challenge for online SOH estimation: extracting degradation information and maintaining model computational efficiency\cite{ref31}.
```

范文依据：Engineering-AI full.txt:65–96（引言完整容量测量/HI限制段，本轮重读）：短引“infer SOH from indirect sensor data”（从间接传感数据推断SOH）。参考的是动词直接带对象的表达，不是把本文运行信号改成其传感器设定。BMSFormer full.txt:58–92对照BMS约束；JESSOHRUL full.txt:105–120对照提取限制。后两篇提供完整功能上下文，不宣称本句改法为其原句。

简短中文原因：词汇简单但表达绕：make + the stable extraction of… + more difficult把真正动作extract包进抽象名词。改为make it harder to extract，读者更早看到具体动作；consistently保留稳定提取的要求。只改这一分句，未删去段尾双重挑战总结。

六层复查：术语不变；extraction→extract仅词形变化。动词搭配更直接；主干负担减少；容量定义→在线限制→双重挑战顺序不变；信息颗粒度与力度不变。

## LS-I02｜chapter01.tex:25

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:25)；[中文边界](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:25)。

现有英文：

```tex
A single health indicator contains relatively limited degradation information, whereas multi-source features can describe complementary aspects of battery degradation. However, increasing the number of candidate indicators does not necessarily improve estimation accuracy. Indicators with weak representational capability, unstable cross-cell performance, or redundant information may limit the effective use of multi-source information and increase the learning burden on the model. It is therefore necessary to develop a health indicator selection algorithm that incorporates SOH correlation, cross-cell performance, and redundancy into a unified evaluation and selection process. Retaining indicators with stable representational capability and reducing inputs that are weakly correlated with SOH or redundant can help the model learn battery degradation patterns more effectively.
```

建议英文（仍为一个自然段）：

```tex
A single health indicator contains relatively limited degradation information, whereas multi-source features can describe complementary aspects of battery degradation. However, increasing the number of candidate indicators does not necessarily improve estimation accuracy. Indicators with weak representational capability, unstable cross-cell performance, or redundant information may limit the effective use of multi-source information and increase the learning burden on the model. We therefore need to develop a health indicator selection algorithm that incorporates SOH correlation, cross-cell performance, and redundancy into a unified evaluation and selection process. Retaining indicators with stable representational capability and reducing inputs that are weakly correlated with SOH or redundant can help the model learn battery degradation patterns more effectively.
```

范文依据：JESSOHRUL full.txt:1786–1797、1822–1834（同一HI筛选上下文，本轮重读）：短引“a HI selection algorithm is proposed”（提出HI筛选算法）。参考其算法作为明确操作对象的做法；范文上一段自身也使用较绕的it is essential，不把其所有写法都照搬。Engineering-AI full.txt:140–146的筛选贡献段以及BMSFormer full.txt:166–173的HI表征挑战用于交叉核对，不借用不同筛选协议。

简短中文原因：词汇简单但表达绕：It is necessary to develop用空主语先判断必要性，再交代研究动作。We need to develop直接说需要设计什么；保留develop、必要性、三个筛选维度和统一过程。收益较小，属于可选直接性修复，不判现句错误。

六层复查：术语和原动词develop保持；明确作者主体，不引入新事实；句间因果therefore保留；三个维度、统一评价筛选、后句目的完整；必要性need等同necessary，不改为已开发成功。

## LS-I03｜chapter01.tex:27

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:27)；[中文边界](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:27)。

现有英文：

```tex
A comparison of existing SOH estimation methods is summarized in \Cref{tab:soh-method-comparison}. Specifically, the comparison examines whether each method fully uses degradation information in battery operating data, employs effective health indicator extraction and selection strategies, balances estimation performance and computational efficiency through targeted model design, and evaluates model complexity. For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention. For models, complexity is directly related to practical deployment, in addition to estimation performance. In recent years, a notable trend in deep model design has been to improve representational capability by increasing network depth, enlarging model size, or introducing more complex feature interactions. These designs help models capture complex degradation patterns but usually require more parameters, computation, and storage. Therefore, for BMS with limited computing power and storage space and strict real-time requirements, SOH estimation models need to control model size and resource overhead while retaining effective representational capability, moving toward more compact and efficient designs.
```

建议英文（仍为一个自然段）：

```tex
A comparison of existing SOH estimation methods is summarized in \Cref{tab:soh-method-comparison}. Specifically, the comparison examines whether each method fully uses degradation information in battery operating data, employs effective health indicator extraction and selection strategies, balances estimation performance and computational efficiency through targeted model design, and evaluates model complexity. For health indicators, differences in battery materials and operating conditions mean that we need to further examine whether the selected indicators can consistently represent degradation across cells. For models, complexity is directly related to practical deployment, in addition to estimation performance. In recent years, a notable trend in deep model design has been to improve representational capability by increasing network depth, enlarging model size, or introducing more complex feature interactions. These designs help models capture complex degradation patterns but usually require more parameters, computation, and storage. Therefore, for BMS with limited computing power and storage space and strict real-time requirements, SOH estimation models need to control model size and resource overhead while retaining effective representational capability, moving toward more compact and efficient designs.
```

范文依据：JESSOHRUL full.txt:1786–1797（HI筛选前的完整问题段，本轮重读）：短引“an HI that performs well in one setting may not be suitable in another”（某HI在一种条件表现好，在另一种条件可能不适用）。该段用具体HI加行为描述跨条件表现；本文改为指标直接作represent的主语。BMSFormer full.txt:58–92及Engineering-AI full.txt:197–225用于本段余下资源/模型设计内容核对。

简短中文原因：词汇简单但表达绕：the stability of their degradation representations把稳定性、表征和跨电池范围连续名词化，their还需回找health indicators。改为selected indicators can consistently represent degradation，读者可直接辨认谁表征什么、是否稳定。其中selected显化中文本段已有的“所选指标”，有原文依据，不是英语语法必需的新增限定。保留材料/条件差异→进一步关注的推理，不把待考察问题改成已经稳定。

六层复查：不轮换health indicator/represent概念；用represent degradation明确搭配；解除抽象名词嵌套和their回指；材料差异→稳定性问题→模型复杂度→设计趋势仍原顺序；四项比较维度和BMS限制未删；whether保留问题未定性。

## LS-I04｜chapter01.tex:44

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:44)；[中文边界](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:44)。

现有英文：

```tex
(1) \textbf{A multi-source health indicator extraction and optimization algorithm is proposed.} The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It then jointly evaluates the relationships between candidate indicators and SOH and the redundancy among indicators using correlations on the feature-development cells. MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators. The unified selection rules determine a corresponding health indicator combination for each dataset, and the selected indicators retain strong linear and monotonic correlations on other cells within the same dataset.
```

建议英文（仍为一个自然段）：

```tex
(1) \textbf{A multi-source health indicator extraction and optimization algorithm is proposed.} The algorithm first extracts multiple types of candidate health indicators from charge-discharge data and their derived curves. It then uses correlations on the feature-development cells to jointly evaluate the relationships between candidate indicators and SOH and the redundancy among indicators. MS-CCCT calibrates the voltage window for the charging-time feature, after which PCC/SCC dual thresholds and redundancy constraints are used to select candidate indicators. The unified selection rules determine a corresponding health indicator combination for each dataset, and the selected indicators retain strong linear and monotonic correlations on other cells within the same dataset.
```

范文依据：JESSOHRUL full.txt:1797、1822–1834（HI算法完整跨页段，本轮重读）：短引“jointly evaluate their linear and monotonic nonlinear relationships”（联合评价其线性和单调非线性关系）。原段先交代相关系数计算，再交代评价、保留和去冗余；本文只借操作依据→评价对象的顺序，不借其全电池范围和阈值。Engineering-AI full.txt:140–146、BMSFormer full.txt:208–213提供筛选/窗口贡献的上下文对照。

简短中文原因：词汇简单但表达绕：句末using correlations要越过两个较长评价对象才能回接evaluates，且容易暂读为只修饰redundancy。改成uses…to evaluate先交代依据，再并列评价对象；与中文“以…结果为依据，综合评价…”吻合。算法步骤和评价内容不变。

六层复查：feature-development cells保持本文数据角色；uses correlations to evaluate搭配明确；依据与目的同一主干，无句末回挂；提取→评价→窗标定→筛选→其他电池相关性的段内顺序不变；两类关系、数据范围和结果强度完整。

## LS-I05｜chapter01.tex:48

位置：[当前英文](D:/MS-AgentNet-English/chapters/chapter01.tex:48)；[中文边界](D:/MS-AgentNet-English/source-zh/chapters/chapter01.tex:48)。

现有英文：

```tex
(3) \textbf{Comprehensive validation is conducted on multiple datasets.} Experiments on multiple public datasets with different battery materials, capacities, and charge-discharge protocols, together with module ablation and complexity analysis, jointly evaluate the estimation accuracy, computational efficiency, and cross-cell generalization of the proposed method. Cross-dataset transfer experiments further examine the model's cross-domain adaptation capability. The results show that the proposed model maintains high SOH estimation accuracy with low computational and storage overhead.
```

建议英文（仍为一个自然段）：

```tex
(3) \textbf{Comprehensive validation is conducted on multiple datasets.} Experiments are conducted on multiple public datasets with different battery materials, capacities, and charge-discharge protocols. These experiments, module ablation, and complexity analysis jointly evaluate the estimation accuracy, computational efficiency, and cross-cell generalization of the proposed method. Cross-dataset transfer experiments further examine the model's cross-domain adaptation capability. The results show that the proposed model maintains high SOH estimation accuracy with low computational and storage overhead.
```

范文依据：JESSOHRUL full.txt:303–309（完整验证贡献条目，本轮重读）：短引“Verification experiments were conducted on multiple battery datasets”（在多个电池数据集开展验证实验）。其experiments were conducted主干先出现，再接数据差异和评价目标。本文保留自己额外的消融、复杂度和跨数据集适应信息。BMSFormer full.txt:30–40与Engineering-AI full.txt:154–159的验证句用于对照；不照搬prove、superior或硬件完成主张。

简短中文原因：词汇简单但表达绕：Experiments与evaluate之间插入数据集长修饰及together with，谓语出现过晚。把实验范围单独成句，再用三个明确主语交代评价目的；仍处于同一个原自然段。这里分句是为减轻主干负担，不按固定句长机械切句。

六层复查：模型、数据集、charge-discharge protocols及cross-cell/cross-domain术语保持；conduct experiments更直接；两句各有简短主干；先范围后评价再跨域再结果的顺序不变；全部三类数据差异、三项评价、两类分析完整；无新实验，原时态与结论力度不变。

## 保留覆盖记录

以下并非只查难词：分别核对了动作主体、修饰范围、指代和句间推进。保留表示本轮没有足以支持改写的直接性问题；不表示所有原研究事实已由范文验证。

|文件行号|段落/文本块|本轮结论与理由|
|---|---|---|
|abstract:1|摘要|保留。网络模块句信息较多，但网络→模块→卷积/注意力→作用的依附可清楚恢复；大核句明确列提取和融合动作。mainly integrates、resource-consuming有BMS同语境原文，不机械判错。many为已批准限定；本轮不为新风格审校删除它或泛加generally/relatively。方法句现在时、实验We compared过去时、结果现在时按功能成立。|
|abstract:3|关键词|保留。deep feature fusion为已确认术语，不照BMS不同的depthwise feature fusion改名。|
|chapter01:1|背景与安全|保留。安全机制较长来自必要信息，主句主体与结果清楚。“新能源交通”是已批准描述译法，准确范围问题不靠风格替换解决。|
|chapter01:5|Literature review|保留，常规自然标题。|
|chapter01:7|方法分类|保留。two categories→former/latter的指代短且明确，没必要逐个重新写分类名。|
|chapter01:9|模型驱动综述|保留主体表述。参数和物理机制细节均是源稿信息；模型→特点→例子→限制清楚。ECMs may… and depend的情态作用域可在独立语义清晰化时改为their accuracy depends，但不是本轮“词简单而绕”的核心问题，不强制重写。|
|chapter01:11|数据驱动与传统ML|保留。六模型列表较长，但数字/模型名称必要，先有fed，谓语没有拖至列举之后。不得为短句删列表。|
|chapter01:13|CNN综述|保留。首句有发展背景、方法依据和目的，但主干researchers…used明确，后句和例子直接推进，不必为略长拆句。|
|chapter01:15|CNN/RNN联系|保留。采用当前已修改的multiple convolutional layers are generally needed to fuse…；已有明确动作与一般性限定。|
|chapter01:17|Transformer综述|保留。多个例子各有作者和动作；最后二次瓶颈明确N和复杂度，长段落是中文论证范围，不能拆段或删研究例子。|
|chapter01:19|HI来源与微分限制|保留。including插入项不短，但可清楚识别运行数据与衍生曲线；噪声→平滑→例子推进自然。|
|chapter01:21|时间HI与区间选择|保留。CCCT的times corresponding to endpoints略层叠，但准确表达两个时刻相减；改为time to traverse可能偷加轨迹假设，因此不为“直接”强换。末句PCC对象和组内范围清楚。|
|chapter01:23|多源HI文献|保留。提取、计算、比较、降维、优化均有明确对象，不能因动词多而删步骤。|
|chapter01:32|Challenges and contributions|保留。标题短并自然，是否补analysis属于标题细粒度选择，不是英语不地道。|
|chapter01:34|挑战引出句|语言保留。短引导句为下列三条提供结构，不算需删的空泛套话。源中文“三点”未显译已在回译报告列低影响漏译；若处理，可补three，不属于本轮风格改写。|
|chapter01:36|HI跨电池挑战|保留。相关类型与冗余分工清楚。its可从model input selection恢复，非必须消除的严重回绕；若作者另求极严格指代可用the selection results。|
|chapter01:38|局部/长期融合挑战|保留。局部→长期→聚合时保留→互补需求顺序清楚；generally与overall层级差异归此前可选语义细化，本轮不扩大。|
|chapter01:40|复杂度挑战|保留。模型加深/组合→参数计算→串行/两两→应用负担，主干直接；number of model parameters是当前已批准修订。|
|chapter01:42|框架过渡|保留。冒号把两层设计与作用直接配对，虽然有addresses，未构成绕写或无信息自证。|
|chapter01:46|网络贡献|保留。combines、reduces、extract、integrate依次描述操作，术语与模型章一致；小核/大核各角色不能靠合句删减。|

## 交付检查

五处建议保持原自然段边界；LS-I05仅在同段内把范围和评价分成两句。其余建议为句内动作或修饰调整。原引文键、数学符号、数值、评价对象及次序全部保留。未为直白新增保证、因果解释、数据角色或实验。建议来源均为本轮重新查看的上述原文；新组合语法明确属于本文适配，未冒充范文原句。

优先审阅LS-I04、LS-I05（依据回挂、谓语拖后）及LS-I03（抽象名词与指代）。LS-I01为动词化小修；LS-I02为可选小修。其余内容建议保留，避免因换agent而反复替换词汇。

## 本批文件快照（SHA-256）

这些快照用于识别本批实际审读版本，不代表正文获准修改。交付时五处建议的引文、数学与数字串已与原段程序核对一致。

|文件|SHA-256|
|---|---|
|chapters/abstract.tex|A0C6838EB034770D3282CE2AE4BD44572FD3BC392833124754D8F3E53ACD1251|
|chapters/chapter01.tex|99C4C4C74F76AF984405D0EAF9C0799070F96C2446A54DD98E5AD89749EA0626|
|style-references/BMSFormer/full.txt|79C5953DB52CCA55FE7950BCDC3F03886FD3D064241DBB5B4F4DD5C15C673482|
|style-references/Engineering-AI/full.txt|34779F53CF13504189F44BE922C39E4F6DFEC2607BD110B47BFACAA46F619209|
|style-references/JESSOHRUL/full.txt|A1F78CD4A4F6A9785C4A424A0F1381F507D72830277246F85FB5A9008EF614E4|
