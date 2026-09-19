# 全篇英文语言与范文风格审校

> 后续复核：作者要求再次仔细确认后，19项候选已重新分级并收窄。请以[二次复核报告](D:/MS-AgentNet-English/translation-guides/language-style-recheck-2026-09-13.md)为准；下文保留上一轮历史记录，不应直接照单应用。

审校日期：2026-09-13。收尾快照：北京时间23:12。按作者最新AGENTS.md，本轮以现有英文语言及三篇范文的对应表达为主，不重新翻译，也不以反向回译代替语言审校。主审与三个agent协同完成全文审查及重点交叉复核。所有建议尚未获准写入；本团队未修改论文正文、图表或中文源稿。

## 结论先读

全文大部分英文可以保留。较值得修改的地方集中在抽象名词嵌套、长修饰使主干推迟、指代回绕，以及指标/数值和模块/动作的配对不够直接，而不只是“单词太难”。

本轮共审查206个文字块，提出19个段落级候选：16项建议、3项可选；其余187块保留。文字块包含标题、关键词、步骤和公式解释，不能将206说成206个正文自然段。39个独立公式不作语言改写，相邻定义与限制已审查。图表文字另有建议，不混入19个正文候选的计数。

|范围|文字块|候选段落|其中可选|明确保留|
|---|---:|---:|---:|---:|
|摘要、关键词与引言|25|5|1|20|
|第二、第三章|120|7|1|113|
|第四、第五章|61|7|1|54|
|合计|206|19|3|187|

图表范围：读取22个表格、11个图题文件、共享排版宏和主文件；主稿实际调用18表和10图环境，其余为目录附属材料。图中明确拼写/搭配错误、命名一致性与技术歧义分别列出。本轮重新查看了三个重点问题图片，其余图片的完整目视核查记录见前一轮图片附件，不冒称全部再次重看。

## 建议先看这些位置

|问题类型|位置/编号|具体修复方向|
|---|---|---|
|依据置尾、长主语拖后|引言LS-I04、LS-I05|使相关性依据紧邻评价动作；把实验范围与评价目的在同段内清楚展开|
|抽象名词嵌套|引言LS-I03；第4章C04-L041|明确HI表征什么、评价什么，避免stability of…/effectiveness of…层叠|
|指代及融合步骤回绕|方法LS-M06、LS-M07|点名standard convolution；明确归一化后的局部表示进入融合|
|定义插入使动作推迟|方法LS-M08|先完整定义张量与符号，再陈述转置，保留原信息次序|
|模块与动作需要回配|第4章C04-L149|让DSConv/RAA紧邻extract/enable，不靠句末respectively回配|
|计量步骤和数值归属不直接|第4章C04-L166、C04-L170|明确测量、补计、换算的对象；FLOPs、参数量、权重存储分别对应动作与数值|

三项明确可选：LS-I02（必要性句的主语形式）、LS-M01（charge timing→charging time）、C04-L065（统计量与数值展开）。这些不应计作三处确定错误，也不是必须全部采纳。其余建议同样是待作者确认的语言提案，不是对原句均有语法错误的宣告。

## 统一审校标准与交叉复核

每个候选均提供“现有英文—建议英文—范文依据—简短中文原因”，再复查六层：术语、动词搭配、句子主干、句间推进、信息颗粒度、表达力度。依据来自各审查者本批重新查看的功能对应TXT上下文；双栏顺序有疑问的相关段回查PDF。范文释义是助手解释，不是官方中英对照。

Engineering-AI主要用于轻量化和资源权衡，BMSFormer用于局部—全局建模与数据流，JESSOHRUL用于HI提取与筛选。不是每段强凑三篇短引；未能直接沿用的语法明确标为本文适配。既有句级学习记录可作索引，本轮不虚称将三篇全文再次逐句计数。

主审复读各分章候选并核查当前版本；另一agent独立交叉复核图表及第4–5章重点。复核中执行了以下取舍：

- 撤销方法LS-M03：目录中的充/放电符号定义已被外部更新为清楚分组，旧“六符号and链”意见不再适用。保留撤销记录，避免同一问题反复修改。
- 第4章C04-L065降为可选：统计量已有前文定义，展开是清晰度偏好，不是必须纠错。
- 第5章C05-L001收窄：保留原首句，不增加有潜在回指问题的It，只将尾句aggregation/broadcasting恢复为动词。
- 引言LS-I03的selected来自中文“所选指标”，不是为风格擅加限定；报告已说明。
- 保留语境合理的RAA is held fixed、battery chemistries、preventing，以及已确认专业词；不因某个agent偏好不同换词。
- 保留所有实验条件、负面结果、比较对象、数值和段落边界。长列表若确有必要，不以固定句长或删信息换取“简洁”。

## 图表中需要单独处理的事项

明确语言项包括others Cells、Health indicators extraction以及Skim/Slim；图内L-DSConv与本稿DSConv-L也须统一。但CX2图例、模块连接/残差位置、variance协议名称、筛选算法量词和Reduction分母属于技术核实事项，不靠一句“更地道”的改稿直接定案。细节见附录D和前一轮图片记录。

## 阅读入口

本文件已合并全部完整对照及保留清单，不必另开多个文件才能看到建议。

- [附录A：摘要与引言](#appendix-a)
- [附录B：第二、第三章](#appendix-b)
- [附录C：第四、第五章](#appendix-c)
- [附录D：图表文字与术语一致性](#appendix-d)

分册也保留，便于单章查看：[摘要/引言](D:/MS-AgentNet-English/translation-guides/language-style-audit-2026-09-13-intro.md)、[方法](D:/MS-AgentNet-English/translation-guides/language-style-audit-2026-09-13-methods.md)、[结果/结论](D:/MS-AgentNet-English/translation-guides/language-style-audit-2026-09-13-results.md)、[图表](D:/MS-AgentNet-English/translation-guides/language-style-audit-2026-09-13-tables.md)。

前一阶段工作另存：[全篇回译审查](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13.md)、[图片完整核查](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13-images.md)。旧报告不被本轮覆盖，也不混作当前语言建议。

## 版本与交付验证

19个有效候选的“现有英文”均与收尾时当前文件一致。每对原/建议段的数字序列、行内数学表达和引用/交叉引用命令序列经程序对照一致；另对语义、条件、信息顺序及段落边界逐项人工复核。程序通过不等于英语或科学结论无误，多agent也不能保证发现全部问题。

源稿及论文相关124个文件在本轮保存的哈希基线与收尾对照之间无变化；本团队只创建和整理审查文档。读稿期间发现的外部修订已按实际版本处理，不称整个工作目录没有其他人编辑。未修改正文，因此本轮没有重新编译；不以历史编译结果冒充当前审校验收。

后续每次审校沿用这种独立记录方式，新建对应轮次文档，保留已确认术语与既有批准结果，不把旧建议反复当新问题。以下完整建议以所记快照为准；正文后续更新后应重新匹配，不能机械套用。


### 正文快照（SHA-256）

|文件|SHA-256|
|---|---|
|chapters/abstract.tex|A0C6838EB034770D3282CE2AE4BD44572FD3BC392833124754D8F3E53ACD1251|
|chapters/chapter01.tex|99C4C4C74F76AF984405D0EAF9C0799070F96C2446A54DD98E5AD89749EA0626|
|chapters/chapter02.tex|953255897E1506656EC067E45920450DCD784EEE99415EAE239026C8EEBE83E9|
|chapters/chapter03.tex|CEBA52AF67567506077F6DF6EE73C825786297BF322BF489FC540FF6F415FBE7|
|chapters/chapter04.tex|21B96DCF50DCB2D972202581FB164C304A7F2FC264A195179AF3D81F7259E3B8|
|chapters/chapter05.tex|FF0FBE7740CD495D05512E57BA0F67503AFF357E50710A87E1D9FD8AF5A3F808|

## Appendix A

### 英文语言与范文风格审校：摘要及第一章（2026-09-13）

本报告执行作者最新阶段要求：以现有英文的直接性、自然度和范文语境为主，中文仅用来约束信息与力度，不再次逐段回译。仅提出建议，论文正文未修改。

本批通读了当前abstract及chapter01–chapter05英文正文。目标覆盖摘要、关键词、第一章21个自然段及2个小节标题，共25块。建议只涉及其中5个自然段；其余20块逐项列为保留。对主要术语、算法/电池角色、比较范围、数字与引文的要求沿用现行术语表。五项建议不是五项确定错误：其中LS-I02收益较小，明确为可选。

本批重新查看的原文包括：BMSFormer full.txt摘要30–40、引言49–234；Engineering-AI full.txt摘要34–47、引言容量限制65–96、模型116–139、贡献141–159、深度模型197–225；JESSOHRUL full.txt摘要33–50、引言60–140、问题244–263、验证贡献303–309、HI筛选1671–1680与1786–1834。涉及跨页和双栏错序时，另外查看了JESSOHRUL PDF第13、14页的既有渲染，以及BMSFormer PDF第2页的既有渲染，确认段落接续。本轮没有把TXT中穿插的DTV说明接到HI筛选段中。每项以下均给重新核对的完整段落范围及短引；短引恢复跨行断词，中文释义为助手说明。

对齐范围为六层：术语、动词搭配、句子主干、句间推进、信息颗粒度、表达力度。参考论文也有绕写、冗余和强断言，优先借其明确对象—动作的对应表达，不为贴近范文删除本文必要内容或重排论证。

#### LS-I01｜chapter01.tex:3

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

#### LS-I02｜chapter01.tex:25

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

#### LS-I03｜chapter01.tex:27

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

#### LS-I04｜chapter01.tex:44

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

#### LS-I05｜chapter01.tex:48

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

#### 保留覆盖记录

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

#### 交付检查

五处建议保持原自然段边界；LS-I05仅在同段内把范围和评价分成两句。其余建议为句内动作或修饰调整。原引文键、数学符号、数值、评价对象及次序全部保留。未为直白新增保证、因果解释、数据角色或实验。建议来源均为本轮重新查看的上述原文；新组合语法明确属于本文适配，未冒充范文原句。

优先审阅LS-I04、LS-I05（依据回挂、谓语拖后）及LS-I03（抽象名词与指代）。LS-I01为动词化小修；LS-I02为可选小修。其余内容建议保留，避免因换agent而反复替换词汇。

#### 本批文件快照（SHA-256）

这些快照用于识别本批实际审读版本，不代表正文获准修改。交付时五处建议的引文、数学与数字串已与原段程序核对一致。

|文件|SHA-256|
|---|---|
|chapters/abstract.tex|A0C6838EB034770D3282CE2AE4BD44572FD3BC392833124754D8F3E53ACD1251|
|chapters/chapter01.tex|99C4C4C74F76AF984405D0EAF9C0799070F96C2446A54DD98E5AD89749EA0626|
|style-references/BMSFormer/full.txt|79C5953DB52CCA55FE7950BCDC3F03886FD3D064241DBB5B4F4DD5C15C673482|
|style-references/Engineering-AI/full.txt|34779F53CF13504189F44BE922C39E4F6DFEC2607BD110B47BFACAA46F619209|
|style-references/JESSOHRUL/full.txt|A1F78CD4A4F6A9785C4A424A0F1381F507D72830277246F85FB5A9008EF614E4|

## Appendix B

### 英文语言与三篇范文风格审校：第二、三章

日期：2026-09-13。按作者最新AGENTS审校现有英文，不重新翻译，不以反向回译为主。仅写建议，未修改论文正文。

本轮重新通读chapters/abstract.tex及chapter01.tex至chapter05.tex。第二、三章50+70=120个文字块（含标题、步骤、公式说明）按术语、动词搭配、句子主干、句间推进、信息颗粒度、表达力度六层审查。7个段落给出有效建议，113块保留；LS-M03因外部更新已修复而撤销，保留编号用于版本追踪。34个独立数学公式不作风格改写，外部图表input文件和栅格文字不纳入本册覆盖分母。

#### 本批重新阅读的范文上下文

以下均为本轮重新查看的full.txt对应完整段落，不以旧词表替代。另直接从原PDF按页保留布局回读Engineering-AI第7–8页、JESSOHRUL第13–14页、BMSFormer第6页，以辨明双栏顺序。这是PDF文字布局核对，不声称新做全PDF视觉审查。

- JESSOHRUL：L1576–1590（HI构建、IC定义引段）；L1634–1647（Table 4）；L1671–1680（PCC/SCC完整段）；L1751–1760、L1773–1797、L1799–1811、L1822–1849（DTV及筛选完整相关段）。L1797的This method first接L1822的calculates，中间另一栏温度公式说明不可连入。
- BMSFormer：L731–746（模型引入和架构数据流完整段）；L766–789（标准卷积、计算量引导及符号）；L806–817、L837–841（深度/逐点卷积和符号上下文）。第6页左栏数据流与右栏卷积说明不能按TXT穿插顺序串读。
- Engineering-AI：L332–342（窗口标定引段）；L838–841（完整DSConv引段）；L845–849、L853及L828–829（置换和归一化说明）；L855–860接L875–884（小核双作用段）；L898–901及L914–921（大核细化）；L903–912、L923–927（智能体注意力上下文）。PDF第7–8页确认跨栏/跨页衔接，不能把AFF/AAT段混入DSConv段。

范文只提供匹配语境的短搭配及结构观察；本文建议不是范文原句。不照搬范文的长引导、生硬语法、ensure、aging inertia或rank restoration。没有把“范文也这么写”当作忽略直接性的理由。

#### 完整段落建议

##### LS-M01 — 可选搭配修复：charge timing容易联想到充电时机

位置：[chapter02.tex L60](D:/MS-AgentNet-English/chapters/chapter02.tex:60)；覆盖ID M02-023。

现有英文：

```latex
In addition to charge timing features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:
```

建议英文（完整段落，未写入）：

```latex
In addition to charging time features, changes in capacity with voltage also contain battery degradation information. The incremental capacity (IC) curve is a well-established tool for analyzing electrochemical degradation in batteries. By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}. IC is expressed as:
```

范文依据：JESSOHRUL full.txt L1585–1590（完整IC定义引段）及Table 4 L1634–1647（时间与峰特征对应）；BMSFormer full.txt L275–283（窗口/标签完整步骤）。本批核实短引：“The charge time within the voltage range”。完整建议句属于本文适配，不是范文原句。

简短中文原因：这里对应前文CCCT时长特征，timing容易让读者先想到充电时机。charging time与本章charge duration的物理对象更明确。其余原句已经直接，保留。

六层复查：仅调整时间特征的搭配；IC、容量对电压求导、平台转峰、峰位和形状、引文与力度全保留。句子主干、段内推进及信息颗粒度不变。不是为简洁任意换术语。

##### LS-M02 — 词汇简单但表达绕：长被动名词链与末尾编号回指

位置：[chapter02.tex L90](D:/MS-AgentNet-English/chapters/chapter02.tex:90)；覆盖ID M02-030。

现有英文：

```latex
where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge voltage and current, respectively, and integration is performed over the discharge time segments in which the voltage lies within $[V_l,V_h]$. Time is measured in s, and $Q_{\mathrm{dch}}$ is measured in Ah. Two candidate indicators of discharge capacity within a voltage window are further constructed by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V, denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

建议英文（完整段落，未写入）：

```latex
where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge voltage and current, respectively, and integration is performed over the discharge time segments in which the voltage lies within $[V_l,V_h]$. Time is measured in s, and $Q_{\mathrm{dch}}$ is measured in Ah. We further construct two candidate indicators of discharge capacity within a voltage window by calculating the charge released as the terminal voltage decreases from 3.80 V to 3.40 V and from 3.20 V to 3.00 V. These indicators are denoted as HI13 and HI14, respectively\cite{ref31,ref52}.
```

范文依据：JESSOHRUL full.txt L1799–1811（完整DTV处理/提取上下文），特别L1803–1811按特征逐一对应HI编号。本批核实短引：“four HIs are extracted”。完整建议句属于本文适配，不是范文原句。

简短中文原因：现句用Two candidate indicators of discharge capacity within a voltage window作长主语，等读完两个电压区间后才出现denoted as，编号需向前回找。建议以We construct明确动作，并把编号对齐单独成句；仍为同一自然段。

六层复查：术语与搭配：discharge capacity、voltage window、charge released保留；主干：We construct前置；推进：积分范围→单位→两个窗口→编号不变；颗粒度：四电压值、s/Ah、两个HI以及绝对电流公式指代保留；力度：未新增测量/因果结论。范文仅支持对象和编号贴近的功能，不是此完整句的原文来源。

##### LS-M03 — 已撤销：外部更新已修复，保留当前段落

位置：[chapter02.tex L98](D:/MS-AgentNet-English/chapters/chapter02.tex:98)；覆盖ID M02-032。

末次重新读取的当前英文：

```latex
where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$ denote the terminal voltage, current magnitude, and duration of charging, respectively; $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote those of discharging. The full charging and discharging phases of each cycle are used. This energy efficiency is denoted as HI15 ($\eta$).
```

版本说明：审查期间该段由外部操作更新，现以分号分开充电和放电两组符号；respectively仅完成充电三符号的局部配对，放电组用those of discharging明确回指相同三个物理量。原“六符号and链”的问题已不存在。该正文更新不是本审校agent实施。

处置：撤销原LS-M03建议并保留现稿，不再为拆句或改写完整充放电阶段的表达而提出新修订。术语、六符号、完整循环条件、HI15及表达力度均保留。本编号仅作撤销记录，不计入7项有效建议。

##### LS-M04 — 词汇简单但表达绕：结果被用于构造、再由which指定窗口

位置：[chapter02.tex L106](D:/MS-AgentNet-English/chapters/chapter02.tex:106)；覆盖ID M02-034。

现有英文：

```latex
Constant current charge time can reflect changes in battery capacity with cycling, but its correlation with SOH depends on the voltage interval used for extraction. Some studies directly extract time features from predefined local voltage intervals\cite{ref28,ref63}. However, degradation-sensitive intervals differ across datasets, and a fixed window used for one dataset is difficult to apply directly to others. To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT). Two cells from the same dataset form the feature-development set $\mathcal{B}$. Correlation results within this set are used to construct a group-level robust score, which determines the extraction window for HI1.
```

建议英文（完整段落，未写入）：

```latex
Constant current charge time can reflect changes in battery capacity with cycling, but its correlation with SOH depends on the voltage interval used for extraction. Some studies directly extract time features from predefined local voltage intervals\cite{ref28,ref63}. However, degradation-sensitive intervals differ across datasets, and a fixed window used for one dataset is difficult to apply directly to others. To improve the correlation between CCCT and SOH and its stability across cells within the same dataset, this study proposes a group-level dual-correlation multi-scale search method (MS-CCCT). Two cells from the same dataset form the feature-development set $\mathcal{B}$. The method constructs a group-level robust score from correlations within this set and uses this score to determine the extraction window for HI1.
```

范文依据：JESSOHRUL full.txt L1671–1680（PCC/SCC段）及L1843–1849（完整跨电池选择解释段）；Engineering-AI full.txt L332–342（完整窗口/离线标定引段）。本批核实短引：“By evaluating candidates across several cells”。完整建议句属于本文适配，不是范文原句。

简短中文原因：最后一句把Correlation results作被动主语，再靠which转到窗口选择。以The method作主语并列constructs/uses，明确两步及得分的中介作用；不改变前面先说明动机、再定义方法和集合的顺序。

六层复查：术语：group-level robust score及HI1固定；搭配：constructs a score/uses this score；主干：The method执行两动作；推进和颗粒度：两电池、同数据集及集合B、评分后选窗全保留；力度：不从稳健得分推断额外泛化结果。本文最小绝对相关评分不同于三范文，仍标适配。

##### LS-M05 — 词汇简单但表达绕：长设计名词串后which指向不够就近

位置：[chapter03.tex L1](D:/MS-AgentNet-English/chapters/chapter03.tex:1)；覆盖ID M03-001。

现有英文：

```latex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Slim Local-Global Fusion Attention (SLFA) module.
```

建议英文（完整段落，未写入）：

```latex
To address the challenges of both accuracy and computational efficiency in battery SOH estimation, this study proposes a lightweight Multi-Scale Agent Network (MS-AgentNet). The name MS refers to the multi-scale convolutional design of small-kernel DSConv-S and large-kernel DSConv-L. This design efficiently extracts degradation features over different time scales. The following subsections introduce the overall architecture and workflow of MS-AgentNet, describe the designed multi-scale depthwise separable convolution modules, and detail the Slim Local-Global Fusion Attention (SLFA) module.
```

范文依据：Engineering-AI full.txt L838–841（完整DSConv小节引段）；BMSFormer full.txt L731–746（完整模型引入与架构段）。本批核实短引：“The kernel scales”。完整建议句属于本文适配，不是范文原句。

简短中文原因：第二句which前隔着DSConv-S与DSConv-L，读者需回溯它指的是整个多尺度设计。明确写This design作下一句主语，且不用comprising叠加名词串；名称→组成→作用顺序不变。

六层复查：术语/专名MS、DSConv-S/L、SLFA全保留；搭配extracts features不变；主干指向整个设计；推进保持名称→两尺度→作用→后文安排；不同时间尺度/高效和全部信息保留；不新增硬件或精度结果。

##### LS-M06 — 指代回绕：Its computational cost越过parameter count回指

位置：[chapter03.tex L57](D:/MS-AgentNet-English/chapters/chapter03.tex:57)；覆盖ID M03-012。

现有英文：

```latex
Convolution extracts local information from time series through sliding kernels\cite{ref71}. Standard convolution operates across all input channels, with each kernel producing one output feature map corresponding to one output channel. As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time. A larger parameter count may also increase the risk of overfitting on small-sample battery datasets. Its computational cost can be expressed as:
```

建议英文（完整段落，未写入）：

```latex
Convolution extracts local information from time series through sliding kernels\cite{ref71}. Standard convolution operates across all input channels, with each kernel producing one output feature map corresponding to one output channel. As the numbers of input and output channels and the kernel size increase, the parameter count and computational overhead grow rapidly, substantially increasing the computational load and training time. A larger parameter count may also increase the risk of overfitting on small-sample battery datasets. The computational cost of standard convolution can be expressed as:
```

范文依据：BMSFormer full.txt L766–789（完整标准卷积成本引段，公式穿插处只用明确语句）；Engineering-AI full.txt L838–841（完整过拟合/DSConv设计段）。本批核实短引：“The standard convolutions have”。完整建议句属于本文适配，不是范文原句。

简短中文原因：最后一句Its最近的名词是parameter count或overfitting risk，实际要指standard convolution。直接点名对象比强求少词更清楚；这是独立于词难度的指代问题。其余段落保留。

六层复查：术语、所有成本/训练/过拟合判断不变；只明确公式主语的对象，后接同一公式。may保留，未升级因果或参数-实际耗时结论。句间推进与信息颗粒度保持。

##### LS-M07 — 词汇简单但表达绕：融合句嵌套where及it回指

位置：[chapter03.tex L108](D:/MS-AgentNet-English/chapters/chapter03.tex:108)；覆盖ID M03-020。

现有英文：

```latex
2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes it to the fusion stage, where it is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

建议英文（完整段落，未写入）：

```latex
2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to both the RAA branch and the local branch. The local branch applies layer normalization to $\mathbf X_S$ and passes the result to the fusion stage. There, the normalized local representation is combined with the cross-position context established by the RAA branch to form a complementary representation of local features and global information.
```

范文依据：BMSFormer full.txt L735–744（完整数据流段）；Engineering-AI full.txt L855–860及L875–884（小核双作用段，跨页延续，顺序另见本册阅读说明）。本批核实短引：“output from LGFA module”。完整建议句属于本文适配，不是范文原句。

简短中文原因：第二句从归一化一路串到passes、where、it、to form，局部表示的对象在后半句只剩it。将融合动作单独成句并明确the normalized local representation；数据仍按分支→归一化→融合→互补表示推进，段落不拆。

六层复查：术语与模块位置不变；搭配passes the result/is combined与数据流匹配；主干按真实操作分开；局部/RAA两分支、LN、融合端和互补作用都保留；无额外rank restoration或噪声机制。

##### LS-M08 — 词汇简单但表达绕：Given+where推迟真正的转置操作

位置：[chapter03.tex L110](D:/MS-AgentNet-English/chapters/chapter03.tex:110)；覆盖ID M03-021。

现有英文：

```latex
DSConv-S uses a channel expansion factor of two. Given input features $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively, the input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:
```

建议英文（完整段落，未写入）：

```latex
DSConv-S uses a channel expansion factor of two. The input features are $\mathbf X\in\mathbb R^{B\times N\times d}$, where $B$, $N$, and $d$ denote the batch size, sequence length, and embedding dimension, respectively. The input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$:
```

范文依据：BMSFormer full.txt L735–746（输入/嵌入完整上下文）；Engineering-AI full.txt L845–849与L853、L828–829（置换段跨栏，见阅读说明）。本批核实短引：“The refined feature”。完整建议句属于本文适配，不是范文原句。

简短中文原因：原第二句在the input is first transposed之前放入给定输入、张量维度和三个符号定义。把张量及符号定义独立成句，再说明转置；不是删掉维度来求短。范文仅支持按输入→转置→后续运算说明，具体B×N×d保持本文。

六层复查：2倍扩展、B/N/d含义、转置目的、第一层1×1及2d都保留；语法主干更早完成；定义→转置→扩展顺序不变；没有段落拆并或新增张量操作。

#### 全部文字块覆盖

编号沿用方法回译分册仅方便定位；审校标准为本轮六层语言审校。“保留”不是只检查简单词，也不是宣称母语无误。专业名称、维度、必要条件和有功能的重复不机械删除。

| 覆盖ID | 行号 | 当前段落开头 | 处置 |
|---|---|---|---|
| M02-001 | 1 | \subsection{Overview of the SOH estimation framework} | 保留；标题/专名及层级准确。 |
| M02-002 | 3 | To use a consistent definition in the following experiments, SOH is calcula… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-003 | 9 | where $C_{\mathrm{current}}$ and $C_{\mathrm{rated}}$ denote the current av… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-004 | 11 | The proposed SOH estimation framework is shown in \cref{fig:2-1}. | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-005 | 13 | (1) \textbf{Data acquisition.} Public battery aging data covering different… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-006 | 15 | (2) \textbf{Systematic feature engineering.} The proposed multi-source heal… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-007 | 17 | (3) \textbf{Model training.} Samples of the selected HIs are fed into MS-Ag… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-008 | 19 | (4) \textbf{Performance evaluation.} The trained model is directly applied … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-009 | 21 | \subsection{Typical battery datasets} | 保留；标题/专名及层级准确。 |
| M02-010 | 23 | Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/S… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-011 | 27 | \subsubsection*{(1) Oxford dataset} | 保留；标题/专名及层级准确。 |
| M02-012 | 29 | The Oxford dataset is provided by the Battery Intelligence Laboratory at th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-013 | 31 | \subsubsection*{(2) CALCE dataset} | 保留；标题/专名及层级准确。 |
| M02-014 | 33 | The CALCE dataset is provided by the Center for Advanced Life Cycle Enginee… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-015 | 35 | \subsubsection*{(3) MIT/Severson dataset} | 保留；标题/专名及层级准确。 |
| M02-016 | 37 | The MIT/Severson dataset was jointly released by the Massachusetts Institut… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-017 | 42 | \subsection{Feature engineering} | 保留；标题/专名及层级准确。 |
| M02-018 | 44 | This section presents the multi-source health indicator extraction and opti… | 保留；全称及筛选步骤有功能，仅主动化未见确定收益，不凑改动。 |
| M02-019 | 46 | \subsubsection{Health indicator extraction} | 保留；标题/专名及层级准确。 |
| M02-020 | 48 | Charging voltage--time (CVT), incremental capacity (IC), differential tempe… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-021 | 52 | The charging voltage--time (CVT) curve records changes in terminal voltage … | 保留；偏移→时长→原因→定义清楚，continuous/ongoing仅可选，不升级为必改。 |
| M02-022 | 58 | where $t(V_1)$ and $t(V_2)$ are the times when the charging voltage reaches… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-023 | 60 | In addition to charge timing features, changes in capacity with voltage als… | 建议LS-M01。 |
| M02-024 | 66 | where $V_k$ and $Q_k$ are the terminal voltage and charge capacity at the $… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-025 | 68 | Temperature is another important measure of the internal state of a battery… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-026 | 74 | where $V_k$ and $T_k$ are the terminal voltage and battery surface temperat… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-027 | 76 | While DTV characterizes the thermal response in the voltage domain, DTC cha… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-028 | 82 | where $T_k$ and $Q_k$ are the battery surface temperature and charge capaci… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-029 | 84 | Discharge capacity within a voltage window is obtained by integrating the d… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-030 | 90 | where $V_{\mathrm{dch}}(t)$ and $I_{\mathrm{dch}}(t)$ are the discharge vol… | 建议LS-M02。 |
| M02-031 | 92 | Energy efficiency reflects the energy conversion characteristics of a batte… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-032 | 98 | where $V_{\mathrm{ch}}(t)$, $\|I_{\mathrm{ch}}(t)\|$, and $t_{\mathrm{ch}}$ d… | 保留；L98外部新版本已用分号和those of discharging完成配对。LS-M03已撤销。 |
| M02-033 | 103 | \subsubsection{Group-level dual-correlation MS-CCCT} | 保留；标题/专名及层级准确。 |
| M02-034 | 106 | Constant current charge time can reflect changes in battery capacity with c… | 建议LS-M04。 |
| M02-035 | 108 | Most existing CCCT window optimization methods use PCC to evaluate candidat… | 保留语言；PCC/SCC对比直接，only对应中文已有技术表述，不能风格名义改科学含义。 |
| M02-036 | 122 | where $f_{i,j,k}$ is the CCCT extracted from the $i$th candidate window at … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-037 | 124 | To account for the correlation performance of each candidate window on both… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-038 | 131 | The smaller of these two values is then used as the group-level robust scor… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-039 | 137 | This score is determined by the lowest correlation across the two cells, pr… | 保留；preventing在方法语境表达作用，can仅可选，不当误译。 |
| M02-040 | 139 | MS-CCCT uses a three-stage coarse-to-fine search. For the Oxford dataset, t… | 保留；R1/R2/R3及判定条件各句承载信息，数值不能为缩短删除。 |
| M02-041 | 141 | For the Oxford dataset, the 3.55--3.75 V window is finally selected with th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-042 | 143 | \subsubsection{Health indicator selection} | 保留；标题/专名及层级准确。 |
| M02-043 | 145 | HI selection is a key step in lithium-ion battery SOH estimation\cite{ref60… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-044 | 147 | The correlation results for Oxford Cell1 and Cell2 are shown in \cref{fig:2… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-045 | 149 | The same candidate HI does not show identical correlation performance on th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-046 | 151 | Existing studies usually select HIs based on the magnitude of their correla… | 保留；长目的状语有衔接功能，仅移后不足以确立明显改善。 |
| M02-047 | 155 | Accordingly, this study develops a group-level HI selection method. It firs… | 保留；准入→排序→去冗余直接，重复操作词承担步骤对应。 |
| M02-048 | 158 | After correlation-based admission and redundancy removal, HI1 is retained f… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M02-049 | 160 | HI selection is performed only during feature development. Once the indicat… | 保留；only、固定定义/参数和三项排除均是必要协议范围。 |
| M02-050 | 162 | With its definition fixed, HI1 achieves absolute PCC values of 0.997874--0.… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-001 | 1 | To address the challenges of both accuracy and computational efficiency in … | 建议LS-M05。 |
| M03-002 | 3 | \subsection{Architecture overview of MS-AgentNet} | 保留；标题/专名及层级准确。 |
| M03-003 | 5 | The overall architecture of MS-AgentNet is shown in \cref{fig:3-1}. Health … | 保留；HI→窗口→嵌入→Block→读出→标签清楚，被动句适合处理对象。 |
| M03-004 | 7 | Mathematically, let the input to the $l$th MS-AgentNet Block be $\mathbf X_… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-005 | 9 | \textbf{Step 1: Local-global feature fusion.} The input $\mathbf X_l$ is pr… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-006 | 18 | \textbf{Step 2: Feature refinement over longer time scales.} The SLFA outpu… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-007 | 33 | \textbf{Step 3: Nonlinear mapping.} The features $\mathbf X_l''$ are proces… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-008 | 46 | The output $\mathbf Y_l$ is used as the input to the next Block, i.e., $\ma… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-009 | 50 | \subsection{The designed multi-scale depthwise separable convolution module… | 保留；标题/专名及层级准确。 |
| M03-010 | 52 | To combine multi-scale local feature extraction with computational efficien… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-011 | 55 | \subsubsection{Basic DSConv structure and computational cost comparison} | 保留；标题/专名及层级准确。 |
| M03-012 | 57 | Convolution extracts local information from time series through sliding ker… | 建议LS-M06。 |
| M03-013 | 66 | where $k$, $C_{\mathrm{in}}$, $C_{\mathrm{out}}$, and $D_F$ denote the kern… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-014 | 68 | Unlike standard convolution, depthwise separable convolution (DSConv) divid… | 保留；通道内与跨通道分工清楚，术语重复承担对比。 |
| M03-015 | 79 | The ratio of the computational costs of the two types of convolution is: | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-016 | 100 | Equation \eqref{eq:dsconv_cost_ratio} shows that, with the same input and o… | 保留语言；成本比适用条件是源技术事项，不在风格稿中擅补。 |
| M03-017 | 102 | \subsubsection{DSConv-S: Dual-role local enhancement} | 保留；标题/专名及层级准确。 |
| M03-018 | 104 | Small-kernel DSConv-S uses a compact $1\times5$ depthwise convolution and i… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-019 | 106 | 1. \textbf{Input enhancement.} DSConv-S extracts local neighborhood informa… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-020 | 108 | 2. \textbf{Local branch preservation.} In SLFA, $\mathbf X_S$ is passed to … | 建议LS-M07。 |
| M03-021 | 110 | DSConv-S uses a channel expansion factor of two. Given input features $\mat… | 建议LS-M08。 |
| M03-022 | 122 | The expanded features pass through a $1\times5$ depthwise convolution, whic… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-023 | 131 | A ReLU activation is then applied to introduce nonlinearity: | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-024 | 139 | Next, the second $1\times1$ pointwise convolution fuses information across … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-025 | 148 | Finally, the output is transposed back to its original arrangement and comb… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-026 | 159 | where $\operatorname{PW}_{\uparrow}$ and $\operatorname{PW}_{\downarrow}$ d… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-027 | 161 | \textbf{Computational analysis.} With a channel expansion factor of two, th… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-028 | 170 | where $2C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-029 | 172 | \subsubsection{DSConv-L: Feature refinement over longer time scales} | 保留；标题/专名及层级准确。 |
| M03-030 | 174 | DSConv-L follows SLFA and uses a channel expansion factor of three and a $1… | 保留；位置、3倍、1×31、Block层残差清楚，必要细节不是冗词。 |
| M03-031 | 176 | \textbf{Computational analysis.} With a channel expansion factor of three, … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-032 | 185 | where $3C_{\mathrm{out}}$ and $D_F\times D_F$ denote the expanded number of… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-033 | 189 | \subsection{The proposed Slim Local-Global Fusion Attention module} | 保留；标题/专名及层级准确。 |
| M03-034 | 191 | This section presents the general form of multi-head self-attention, briefl… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-035 | 194 | \subsubsection{General form of multi-head self-attention} | 保留；标题/专名及层级准确。 |
| M03-036 | 196 | Multi-head self-attention uses multiple parallel attention heads to calcula… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-037 | 205 | where $N$ is the sequence length, $d$ is the input feature dimension, and $… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-038 | 207 | When a nonnegative similarity function is used to construct normalized atte… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-039 | 223 | where $\mathbf Q_{i,p}$ is the query at the $p$th position in the $i$th att… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-040 | 225 | The outputs at all positions form the output matrix $\mathbf O_i\in\mathbb … | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-041 | 227 | \subsubsection{Softmax attention and linear attention} | 保留；标题/专名及层级准确。 |
| M03-042 | 229 | Standard Softmax attention calculates correlations between sequence positio… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-043 | 242 | The exponential mapping and normalization in Softmax assign larger attentio… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-044 | 244 | To address the quadratic computational cost of Softmax attention, linear at… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-045 | 263 | where $\phi(\cdot)$ is a nonnegative feature mapping, such as $\phi(\mathbf… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-046 | 265 | By first calculating $\phi(\mathbf K_i)^{\mathrm T}\mathbf V_i$, linear att… | 保留；先KᵀV、避免N×N、映射维度及固定dh各有必要，顺序直接。 |
| M03-047 | 267 | Linear attention enables global information interactions at a lower computa… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-048 | 269 | \subsubsection{The proposed SLFA module} | 保留；标题/专名及层级准确。 |
| M03-049 | 271 | To capture both local neighborhood features and cross-position interactions… | 保留；局部表示、RAA和加法融合清楚，不为仿范文增加修饰。 |
| M03-050 | 273 | \textbf{(1) ReLU² Agent Attention.} | 保留；标题/专名及层级准确。 |
| M03-051 | 275 | Agent Attention uses a small number of agents as information intermediaries… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-052 | 277 | To reduce the parameter overhead of query, key, and value generation, RAA u… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-053 | 286 | where $\mathbf s_q,\mathbf s_k,\mathbf s_v\in\mathbb R^d$ are learnable cha… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-054 | 288 | Compared with standard linear projections for queries, keys, and values, wh… | 保留当前已修订句；线性投影与通道缩放向量比较对象清楚，不报旧版问题。 |
| M03-055 | 290 | RAA uses $n_a=2$ learnable agents, represented by a matrix $\mathbf A\in\ma… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-056 | 292 | The global agent matrix $\mathbf A$ is divided into $h$ subspaces along the… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-057 | 294 | During information broadcasting, each query assigns context weights accordi… | 保留；共同缩小→权重均匀→等权读取→RAA动机清楚，非每个长解释都绕。 |
| M03-058 | 311 | where $M$ is the number of elements normalized in each row: $M=N$ during ag… | 保留；M条件、截断、抵消、平方、无正得分回退各为独立必要信息。 |
| M03-059 | 313 | During agent aggregation, $\mathbf A_i$ acts as the query to gather context… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-060 | 329 | where $\boldsymbol{\Phi}_{k,i}\in\mathbb R^{n_a\times N}$ contains the weig… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-061 | 331 | During information broadcasting, each query position reads information from… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-062 | 347 | where $\boldsymbol{\Phi}_{q,i}\in\mathbb R^{N\times n_a}$ contains the broa… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-063 | 349 | Equations \eqref{eq:agent_aggregation} and \eqref{eq:agent_broadcast} show … | 保留；等效映射与秩上界明确，数学对象长度不是改写理由。 |
| M03-064 | 351 | The outputs of all attention heads are concatenated along the feature dimen… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-065 | 361 | where $\operatorname{Concat}(\cdot)$ concatenates the outputs of all attent… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-066 | 363 | RAA generates correlation matrices of size $n_a\times N$ and $N\times n_a$ … | 保留；单/多头计算、内存及固定h/na均明确，未推断实测速度。 |
| M03-067 | 365 | \textbf{(2) Local-global feature fusion.} | 保留；标题/专名及层级准确。 |
| M03-068 | 367 | The input features $\mathbf X$ first pass through DSConv-S to obtain the lo… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-069 | 382 | where $\mathbf X_F$ is the fused SLFA output, $\operatorname{LN}(\mathbf X_… | 保留；术语/搭配合适，对象与动作/定义清楚，推进与必要限定有功能，无需换词重排。 |
| M03-070 | 384 | This additive connection preserves the local degradation features extracted… | 保留；局部保留、全局融合、线性复杂度各有功能。 |

#### 交付复查

7项有效建议保持原段落边界及信息次序；数学表达、全部引用键和数字保持。LS-M03已撤销，不纳入有效建议。LS-M08仍按“2倍扩展→输入张量→B/N/d定义→转置目的→1×1扩展2d”推进，只在符号定义后完成一句，再开始转置，不把操作先移到定义前。LS-M02改成We construct不是收益的唯一理由，主要修复是将末尾HI编号配对从长句中独立，避免远距离回指。

7项有效建议不是7项误译。LS-M01为可选术语搭配消歧，其余针对名词被动链、主干或指代。对于2章L44和L151，已拒绝仅主动化或更换目的状语位置的候选；L98的外部新版本配对已清楚，保留。先前回译报告里的源数学/协议问题不自动成为本阶段语言修改。

仅新增本审校文档。作者确认前不写入论文。

## Appendix C

### 英文语言与三篇范文风格审校：第4–5章

2026-09-13，新阶段独立报告。按照最新AGENTS，本轮以英文语言和六层风格审校为主，不重新回译。只提出建议，正文未改。

已通读当前英文摘要及第1–5章，并在本批重新读取三篇范文相应TXT上下文。第4章132行使用当前`With CS2...`版本；不沿用旧反向回译报告中的`Using...`。之前RAA held fixed和battery chemistries的交叉复核结论保留：分别为语境可接受/可选进一步明确，不重新列为确定误译。

本批覆盖47个自然段、14个小节标题及5个纯公式。列出7项段落级候选，其中6项建议、1项明确可选，另40段明确保留；7项均提供现有完整段与候选完整段。所有候选仍为一个连续自然段，没有删掉数字、条件、比较对象或源稿事实。是否更长或更短不能代替直接性判断。

#### 本批重新阅读的范文证据

| ID | 论文与TXT位置 | 已读完整上下文及所用层级 |
|---|---|---|
| J-HI | JESSOHRUL/full.txt:1946–1959 | 完整单项/Fusion输入实验段。借具体对象→选择/输入动作，保持本文HI编号及协议；不模仿其首句长目的语和大写The错误。 |
| J-A | JESSOHRUL/full.txt:3498–3532 | 完整消融结果各段，含3512–3514换行续句。指标→数值→比较对象；不继承significantly/superior或其机制因果解释。 |
| J-C | JESSOHRUL/full.txt:3793–3808 | 完整复杂度导语与计量段。FLOPs/单次前向、训练时间、参数与权重存储分别计量；不添加范文使用的不同库或硬件含义。 |
| B-C | BMSFormer/full.txt:1344–1351 | 完整效率比较导语，训练/模型参数的配置与比较目的。范文首句it is important并不自动更优，不复制其自证公平句。 |
| B-D | BMSFormer/full.txt:814–817 | 完整DSConv操作引导句，已回看source.pdf第7页确认与前后公式和双栏的关系。模块直接作主语、separates明确动作；不把范文2D结构套入本文。 |
| E-A | Engineering-AI/full.txt:2077–2090 | 完整组件导语及首条比较，卷积位置→功能→替换结果。这里的标准卷积替换与本文消融加/删操作不同。 |
| E-C | Engineering-AI/full.txt:2839–2841＋2806–2824 | 结论首段跨栏错序，已回看source.pdf第20页：先左下Conclusion首句，接右栏direct measurement...，随后方法段与资源结果完整段。借框架→对象→方法以及资源量表达，不借硬件已实现主张。 |

PDF核对图保存于`build/eai-results-style-page20.png`及`build/bms-results-style-page7.png`。这些页面仅用于确认范文阅读顺序，不是论文正文修改。以下每项短引为准确原文，中文解释为助手释义。建议句为本文适配，未冒充范文原句。

#### 7项候选：6项建议与1项可选

##### C04-L041：词汇简单但表达绕：主干后置及抽象名词层叠

位置：`chapters/chapter04.tex:41`。

现有英文：

```tex
To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset. Based on the PCC and SCC of candidate HIs on Cell1, the indicator with the highest combined correlation score is selected from each of the IC, DTV, and DTC categories, giving HI4, HI9, and HI11, respectively. All three combined correlation scores exceed 0.94. These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet. The input combining HI1, HI4, HI9, and HI11 is denoted as Fusion. The SOH estimation results for Cell2--Cell8 with different inputs are given in \cref{tab:4-hi-input}.
```

建议英文：

```tex
This section evaluates whether group-level HI selection identifies stable inputs across cells by comparing SOH estimation performance with different HIs on the Oxford dataset. Based on the PCC and SCC of candidate HIs on Cell1, the indicator with the highest combined correlation score is selected from each of the IC, DTV, and DTC categories, giving HI4, HI9, and HI11, respectively. All three combined correlation scores exceed 0.94. These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet. The input combining HI1, HI4, HI9, and HI11 is denoted as Fusion. The SOH estimation results for Cell2--Cell8 with different inputs are given in \cref{tab:4-hi-input}.
```

范文依据：JESSOHRUL/full.txt:1946–1959，HI输入对照完整段；短引1952–1953：`only one feature is selected from each type of curve`（助手释义：每类曲线仅选一项特征）。

简短中文原因：保留评价目的→比较方式的逻辑，去掉effectiveness of ... in identifying这一名词套层，让evaluates与identifies直接交代审查动作和对象。范文该段首句也有长目的语和不够自然的写法，不能机械复制；借用其随后明确交代选择对象和操作的方式。

六层复查：术语：group-level HI selection、SOH、HI保留；搭配：evaluate whether、identify inputs直接；主干：This section evaluates提前；推进：仍先引出验证，再列特征及Fusion；颗粒度：Oxford、跨电池稳定性及比较方式完整；力度：仍为评价问题，未改为成功结论。

##### C04-L065：明确可选——展开统计量与数值配对，原句可保留

位置：`chapters/chapter04.tex:65`。

现有英文：

```tex
Model convergence is evaluated through both convergence speed and loss fluctuations in the late training stage. The convergence threshold epoch is defined as the first epoch at which the training loss falls below 10\% of the first-epoch loss. The mean and standard deviation of the loss over the final 20 epochs describe the late-stage convergence state. As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$. These results show that MS-AgentNet converges stably under the current experimental settings, with small loss fluctuations in the late training stage.
```

建议英文：

```tex
Model convergence is evaluated through both convergence speed and loss fluctuations in the late training stage. The convergence threshold epoch is defined as the first epoch at which the training loss falls below 10\% of the first-epoch loss. The mean and standard deviation of the loss over the final 20 epochs describe the late-stage convergence state. As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The convergence threshold epoch has a median of 26 on Oxford and 7 on MIT. The median standard deviations of the loss in the late training stage are $2.38\times10^{-4}$ on Oxford and $4.84\times10^{-6}$ on MIT. These results show that MS-AgentNet converges stably under the current experimental settings, with small loss fluctuations in the late training stage.
```

范文依据：JESSOHRUL/full.txt:3518–3525，两个连续数值结果段；短引3521–3522：`the proposed method reduces the average error from 0.0322 (M1) to 0.0207`（助手释义：所提方法将平均误差从0.0322降至0.0207）。

简短中文原因：交叉复核后降为明确可选。两项统计量已在前文定义，当前连续名词修饰在本段语境中可解，不构成必须修复的“表达绕”。候选仅展开指标与数值配对，属于呈现偏好；原句可以保留。范文依据只展示直接报告指标和数值的方式，不能证明本文原句有缺陷。

六层复查：术语：convergence threshold epoch、standard deviation不换名；搭配：has a median of准确；主干：指标直接作主语；推进：阈值→后期波动不变；颗粒度：两域、全部数值和先前定义的首轮10%/最后20轮完整；力度：当前实验设置下收敛的限制不变。

##### C04-L073：词汇简单但表达绕：范围短语关联不直接

位置：`chapters/chapter04.tex:73`。

现有英文：

```tex
The main hyperparameters of MS-AgentNet are the learning rate, network depth $L$, and embedding dimension $d$. Their configuration ranges are listed in \cref{tab:4-1}. Within these ranges, two cells in the feature-development set of each dataset are used for model training and configuration: one for learning model parameters and the other for hyperparameter selection. The training and configuration-selection cells are Cell1 and Cell2 for Oxford, CS2\_36 and CS2\_37 for CALCE CS2, CX2\_36 and CX2\_37 for CALCE CX2, and b3c8 and b3c13 for MIT/Severson, respectively.
```

建议英文：

```tex
The main hyperparameters of MS-AgentNet are the learning rate, network depth $L$, and embedding dimension $d$. Their configuration ranges are listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges. The training and configuration-selection cells are Cell1 and Cell2 for Oxford, CS2\_36 and CS2\_37 for CALCE CS2, CX2\_36 and CX2\_37 for CALCE CX2, and b3c8 and b3c13 for MIT/Severson, respectively.
```

范文依据：BMSFormer/full.txt:1344–1351，完整效率比较导语；短引1348–1349：`training and model hyperparameters are set to evaluate the comprehensive performance of different models`（助手释义：设置训练和模型超参数以评价不同模型的综合性能）。JESSOHRUL/full.txt:1946–1959重新核对输入实验角色。

简短中文原因：当前Within these ranges紧邻two cells，要读到句末才知道范围约束的是超参数；将范围直接放到select hyperparameters后，并把learning/selection恢复为learn/select。只使关系明确，不将配置电池改称独立验证或测试电池。

六层复查：术语：feature-development、configuration-selection等既定角色保留；搭配：learn parameters/select hyperparameters直接；主干：one cell ... a second并列；推进：参数范围→两池分工→四组编号不变；颗粒度：两节电池及全部映射不删；力度：未增添独立测试/公平性证明。

##### C04-L149：词汇简单但表达绕：模块动作被名词化

位置：`chapters/chapter04.tex:149`。

现有英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref31,ref71}. To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

建议英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref31,ref71}. To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

范文依据：BMSFormer/full.txt:814–817，完整DSConv操作说明（已回看PDF第7页确认段序）；短引814：`DSConv separates the spatial and channel-wise operations`（助手释义：DSConv将空间操作与通道操作分开）。Engineering-AI/full.txt:2080–2090完整组件作用导语与首条结果，短引2082–2083：`post-fusion refinement`（融合后细化）。

简短中文原因：将local information preservation和for local feature extraction改成preserve与extract，两个模块分别紧邻各自动作；读者无需读到respectively才回配角色。保留information interactions这一既定技术表达，避免擅改成另一机制。

六层复查：术语：MS-AgentNet、multi-scale DSConv、RAA及cross-position information interactions一致；搭配：extract local features与enable interactions直接；主干：模块→动词→对象；推进：代价问题→组合设计→消融定义不变；颗粒度：两模块作用与效率目的均保留；力度：原句may、标准卷积代价及后续不利结果不变。

##### C04-L166：词汇简单但表达绕：三项被动操作共用一个不精确主语

位置：`chapters/chapter04.tex:166`。

现有英文：

```tex
In practical applications, computational efficiency and storage requirements are important evaluation criteria alongside estimation accuracy\cite{ref77}. This study compares the resource overhead of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM using four metrics: FLOPs, training time, trainable parameter count, and weight storage size. FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass. Training time is recorded in seconds using Python's \texttt{time} module and represents the time needed to complete the specified number of training epochs. The total number of trainable parameters is counted using PyTorch. Weight storage size is measured using Python's \texttt{os.path.getsize} function and converted to KB, representing the space required to save the model weights. All metrics are measured in the same experimental environment.
```

建议英文：

```tex
In practical applications, computational efficiency and storage requirements are important evaluation criteria alongside estimation accuracy\cite{ref77}. This study compares the resource overhead of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM using four metrics: FLOPs, training time, trainable parameter count, and weight storage size. FLOPs are measured using the \texttt{profile} function in the THOP library. After attention operations are added to the count, the result is converted to the number of floating-point operations required for a single forward pass. Training time is recorded in seconds using Python's \texttt{time} module and represents the time needed to complete the specified number of training epochs. The total number of trainable parameters is counted using PyTorch. Weight storage size is measured using Python's \texttt{os.path.getsize} function and converted to KB, representing the space required to save the model weights. All metrics are measured in the same experimental environment.
```

范文依据：JESSOHRUL/full.txt:3799–3808，完整计量方法段；短引3801–3802：`quantify the floating-point operations required for a single forward pass`（助手释义：量化单次前向传播所需的浮点运算次数）。BMSFormer/full.txt:1344–1351完整资源比较导语。

简短中文原因：现句将测量、补计、换算全挂在FLOPs上，supplemented和converted指代需回读；建议明确补充的是计数，换算的是补计后的结果。三个步骤顺序保持，仅在同一自然段内分句。范文不含本文注意力补计步骤，不能为模仿其短句删去该步骤。

六层复查：术语：FLOPs、THOP/profile和single forward pass保留；搭配：add ... to the count明确；主干：measurement→count→result；推进：原三步骤次序不变；颗粒度：注意力补计与换算均保留，其余计量段原样；力度：未把FLOPs换作耗时或推理延迟。

##### C04-L170：用词搭配与直接性：has FLOPs混合不同量的关系

位置：`chapters/chapter04.tex:170`。

现有英文：

```tex
Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low. In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models. It reduces forward-pass computation by 50.5\% compared with LSTM. Its parameter count and storage size are reduced by 25.6\% and 25.8\% compared with CNN-Transformer and by 70.8\% and 59.8\% compared with CNN-LSTM, respectively. These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.
```

建议英文：

```tex
Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low. In contrast, MS-AgentNet requires 0.045760 M FLOPs, has a parameter count of 4,643, and uses 27.44 KB to store its weights; all three values are the lowest among the five models. It reduces forward-pass computation by 50.5\% compared with LSTM. Its parameter count and storage size are reduced by 25.6\% and 25.8\% compared with CNN-Transformer and by 70.8\% and 59.8\% compared with CNN-LSTM, respectively. These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.
```

范文依据：Engineering-AI/full.txt:2816–2824完整结果段（已回看PDF第20页）；短引2821：`a parameter count of only 6114 and a storage footprint of`（助手释义：参数量仅6114，存储占用为……）。JESSOHRUL/full.txt:3799–3808完整计量段，短引3807–3808：`the space required to store model parameters`（存储模型参数所需空间）。

简短中文原因：分别使用requires计算量、has参数量和uses权重存储，让三个数紧邻所属指标，避免has FLOPs和跨三项respectively回配。沿用本文parameter count，不为照搬范文而把storage size全篇换成storage footprint。

六层复查：术语：参数量与权重存储对象保持；搭配：requires FLOPs/has a parameter count更明确；主干：MS-AgentNet的三个并列动词；推进：LSTM训练时间反例→本模型资源优势→降低率不变；颗粒度：三值、单位和五模型范围完整；力度：未暗示训练/推理最快。

##### C05-L001：词汇简单但表达绕——仅将尾句聚合与广播恢复为动词

位置：`chapters/chapter05.tex:1`。

现有英文：

```tex
This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-limited battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset. For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales. With a fixed number of agents, RAA uses a small number of static learnable agents for information aggregation and broadcasting, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.
```

建议英文：

```tex
This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-limited battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset. For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales. With a fixed number of agents, RAA uses a small number of static learnable agents to aggregate and broadcast information, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.
```

范文依据：Engineering-AI/full.txt:2839–2841、2806–2824，已回看PDF第20页恢复完整结论段序；短引2840–2841：`This study presents a practical, computationally efficient framework for battery SOH estimation`（助手释义：本研究提出一个实用且计算高效的电池SOH估计框架）。BMSFormer/full.txt:814–817完整模块操作说明，短引814：`DSConv separates the spatial and channel-wise operations`。

简短中文原因：原首句主干This study proposes靠前，应用对象与研究目的层级清楚，保持原句，不拆成额外It句。建议仅将尾句for information aggregation and broadcasting改为to aggregate and broadcast information，使RAA通过智能体执行的动作更直接；不改变机制、信息顺序或结论细节。

六层复查：术语：框架全名、RAA及其余既定术语不变；搭配：aggregate/broadcast information对应实际作用；主干：仅尾句RAA的动作改用动词；推进：首句及其余句子原样，信息顺序完全保持；颗粒度：全部条件、同数据集范围和复杂度式完整；力度：fixed number、theoretical及强关联条件不变。

#### 保留覆盖记录

下列每段均检查了术语、动词搭配、句子主干、句间推进、信息颗粒度及力度。保留不表示逐句照抄范文，而表示未发现值得在当前授权内修改的直接性或搭配缺陷。当前已有show/indicate、only、may、in-domain、potential等按真实语义保留；不新增absolutely/definitely/demonstrate。

| 位置 | 结论与理由 |
|---|---|
| C04-L001 | 保留。研究任务逐项展开、每句主语清楚；首尾评价范围是原稿信息，不能仅为减少重复删除。 |
| C04-L005 | 保留。四指标直接列出，全称必要；无绕行。 |
| C04-L007 | 保留。MAE定义→对大误差的性质，推进直接。 |
| C04-L009 | 保留。归一化对象与接近零条件清楚，may保留。 |
| C04-L011 | 保留。RMSE定义→与MAE区别，虽含名词但数学定义需要。 |
| C04-L013 | 保留。fits variations主干直接，1的方向明确。 |
| C04-L015 | 保留。简短公式引导，保留。 |
| C04-L037 | 保留。符号解释虽有并列但指向清楚，保留。 |
| C04-L043 | 保留。HI1表现→三均值→Fusion反例，顺序自然。 |
| C04-L045 | 保留。差异→Cell7/8例子→HI1→边界结论，指代清楚。 |
| C04-L050 | 保留。目的引导略长但三项分析对象清楚，没有多层回绕；保留。 |
| C04-L054 | 保留。静态可学习及与输入无关的条件紧邻矩阵，保留。 |
| C04-L061 | 保留。参数符号及初始化结果直接。nonidentical/identical有重复，但分别表达参数和状态，非本轮必要修复。 |
| C04-L063 | 保留。三初始化策略对比完整。ordinary normal略累赘属于可选词汇压缩，不再单列为必要语言缺陷。 |
| C04-L075 | 保留。表格引导简单直接，保留。 |
| C04-L079 | 保留。配置选定→固定→具体值；已直接。 |
| C04-L085 | 保留。数据集/HI映射→比较目的清楚，passive comparison不是自动判绕的理由。 |
| C04-L090 | 保留。图表主语直接引出模型与结果，保留。 |
| C04-L094 | 保留。各模型趋势→代表区间→平滑电池；track/follow搭配匹配对象。 |
| C04-L096 | 保留。长降低率句信息量大，但中文原有三个指标×四基线，不为短句删除；对象和respectively可解，保留。 |
| C04-L103 | 保留。数据集→差异→图，跨池与跨域含义未混淆。 |
| C04-L105 | 保留。主干直接，nonlinear degradation tail是源稿形象表达；本轮不凭未找到完全同词就强换成更窄现象。 |
| C04-L107 | 保留。数值主张清楚；旧审查中的末期证据范围问题仍属科学核实，语言审校不通过换show来偷改结论。 |
| C04-L109 | 保留。已有批准average修复保留。数值密集是源稿颗粒度，不能当纯赘述删除。 |
| C04-L117 | 保留。四句依次定义域偏移、两任务及各协议，限定准确，保留。 |
| C04-L119 | 保留。域→电池角色→化学体系→一致输入，清楚；公式是必要技术内容。 |
| C04-L123 | 保留。两CALCE结果→Oxford对照与范围，虽第一句较长但主干和数量对应清楚。 |
| C04-L125 | 保留。六方向结果→MAE分组→R²限制，直接且完整。 |
| C04-L132 | 保留。当前为With CS2_36 and CX2_36 used ...，已无此前Using修饰错误；协议句可读，保留。 |
| C04-L135 | 保留。源域分别报告起止值与50%转正，前置条件必要，不强行压缩。 |
| C04-L137 | 保留。相邻比例→差值缩小→同率源域结论，指代可解。 |
| C04-L145 | 保留。首句目的内容与后两类功能对应；有轻度名词化但结构清楚，修复收益不足以要求改写。 |
| C04-L152 | 保留。加入DSConv/RAA→部分域改善→反例完整，主干已直接。 |
| C04-L154 | 保留。完整模块→具体下降→CS2 MAE反例→互补结论，保留。 |
| C04-L156 | 保留。RAA is held fixed在四变体上下文可接受；如日后需强调仅结构可再明确，不当作已确定误译。 |
| C04-L158 | 保留。单尺度异质性→四组结果→全尺度结果，复杂信息有明确对象；is consistent with保持审慎。 |
| C04-L168 | 保留。统一实验设置并列准确，4头与4层数值相同的解释为源稿事实，不能删。 |
| C04-L172 | 保留。宽度设置→四值范围→代表值→部署潜力，已有lower than that of修复保留。 |
| C05-L003 | 保留。框架总体表现→CX2两池平均MAPE→资源→消融→域内泛化与潜力，主干清楚；已有平均MAPE批准修复保留。信息重复仍承载原稿结论，不自行删减。 |
| C05-L005 | 保留。依赖片段→跨域影响因素→未来HI/域适应→验证方向，顺序明确。battery chemistries在当前材料体系语境可接受，不当已确定漏译；未来验证未改成已完成。 |

14个标题全部保留：

| 行 | 当前标题 | 结论 |
|---|---|---|
| 3 | `\subsection{Evaluation metrics}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 39 | `\subsection{HI selection results and effectiveness analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 48 | `\subsection{Training robustness and hyperparameter analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 52 | `\subsubsection{Agent matrix initialization and convergence analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 71 | `\subsubsection{Hyperparameter configuration}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 83 | `\subsection{Comparison of SOH estimation accuracy and cross-cell generalization}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 88 | `\subsubsection{Estimation accuracy on the Oxford dataset}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 101 | `\subsubsection{Cross-cell generalization on the CALCE and MIT datasets}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 115 | `\subsection{Cross-dataset transfer experiments}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 121 | `\subsubsection{Performance across transfer directions}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 130 | `\subsubsection{Effect of the target-domain adaptation ratio}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 143 | `\subsection{Module ablation and model complexity analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 147 | `\subsubsection{Module ablation analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 164 | `\subsubsection{Model complexity analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |

第4章第17、22、27、32、56行起的5个公式保持；纯数学表达不做英语风格替换，相邻定义与解释段已计入47段。章节引用与结构命令保持。

#### 提交前复查

- 直接性：改变的是主干、名词化关系或指标与数值的配对，不以改动数、难词数或固定句长衡量。
- 信息及力度：7个候选段所有原有数值、数学内容、引用键与模型/电池范围保留；第5章首句原样保留，只在尾句将聚合与广播改用动词。
- 术语：既定HI选择、配置电池、RAA、参数量、权重存储术语保持；不因参考来源不同换成另一套词汇。
- 段落及推进：所有建议保持一段；句内展开没有调整章节论证次序，没有删改证据边界或不利结果。
- 范文：短引来自本批实际重读的完整上下文；被双栏错序影响的B-D/E-C已回PDF；不把范文本身生硬或夸大写法列为必须学习的目标。

## Appendix D

### 图表文字与全篇术语一致性：英文语言审校

日期：2026-09-13。按作者最新阶段要求，仅审校现有英文，不重新翻译，不修改论文。本轮主审重新通读英文摘要及第1–5章，读取22个表格、11个图题、共享宏及主文件的现有文字；重点语言问题所在的fig1.png、01.png和fig3_3_attention_comparison.png再次目视核对。其余图片沿用同日已完成的图片记录，不声称本轮再次逐图复查。

#### 本批重新阅读的范文依据

- BMSFormer：full.txt 441–459、500–524，HI提取/选择及PCC比较；1344–1376、1385–1398，资源指标、训练设置和层配置。1344段后的公式定义及1370标题存在双栏穿插，本报告只取明确连贯句/短语，不据TXT次序模仿段落推进。
- JESSOHRUL：full.txt 1576–1588、1640–1696、1797–1834、1946–1959，HI曲线、筛选操作、输入方案比较。1797与1822跨栏恢复仅作为算法背景，以下引用的1829–1834连续表达可辨识；不照搬范文阈值或电池角色。
- Engineering-AI：full.txt 878–926、2806–2850，局部/全局模块与资源总结。仅用于功能/术语边界；有跨栏片段，未把TXT行顺序当完整结论段落顺序。本文不引入其硬件验证结果。
- 术语以本目录terminology.md为统一表，不新建另一套词汇。范文短引的中文解释均为助手释义。

#### 建议项

##### LT01：输入本身不会产生估计误差，明确输入与模型结果的关系

位置：tables/table_4_hi_input.tex，表题。

现有英文：

> SOH estimation errors of different health-indicator inputs on the Oxford dataset.

建议英文：

> SOH estimation errors with different health-indicator inputs on the Oxford dataset.

范文依据：JESSOHRUL full.txt 1946–1959完整输入方案比较，1956–1957的短语“all four HIs are fed into the model together”（四个HI一起送入模型）明确输入→模型→结果关系。本句是语义适配，不冒充范文原句。

简短中文原因：不是词难，而是of把errors归属于inputs；改为with直接说明使用不同输入时的误差。保留SOH、不同输入、Oxford及比较功能，不更名HI或增加结果。六层复核：仅修搭配关系；短表题无需模拟句间推进，其余信息和力度不变。

##### LT02：表头用具体指标编号，减少来回查正文

位置：tables/table_2_6.tex，第二列表头。

现有英文：

> HI

建议英文：

> HI1

范文依据：BMSFormer full.txt 503–507在PCC比较中明确所选HI的具体恒流时间指标；523–524表题“PCC comparison of different HIs”说明比较功能。本文第2章最后小节已明确该列为HI1，编号取自本文，不从范文迁移。

简短中文原因：可选清晰度，不是误译。单独的HI需读者回看正文才能确定所指，HI1直接定位该列，数值和比较对象不变。六层复核：术语缩写一致；只显化现有指代，不改变主干/颗粒度/力度。

##### LG01：流程图的名词修饰与动作顺序

位置：figures/fig1.png。以下均为图中短标签，不合并为新正文段落。

|现有英文|建议英文|性质及简短中文原因|
|---|---|---|
|Health indicators extraction|Health indicator extraction|建议修正名词修饰搭配；不改变提取对象或整个算法的正式名称|
|others Cells|Other cells|明确语法错误；other修饰cells，others不能直接修饰名词|
|Four datasets dividing|Data partitioning for the four datasets|建议修正搭配，让划分的对象/操作可读；four保留；具体角色仍按正文，不新增独立测试集|
|Health indicators splitting|Windowing of HI sequences|条件性建议：图中确为HI序列的滑窗切分，与第2、3章一致；若绘图作者另有所指则先核实|
|Five models training, validating and testing|Training, validation, and testing of five models|仅修名词短语，五个模型保留；validation与本文configuration-selection的关系仍需按实际图示角色核实，不能把这条语言建议当作数据划分已通过|

范文依据：BMSFormer full.txt 441–459的HI extraction和window size，以及JESSOHRUL full.txt 1576–1584的数据→曲线→HIs的提取过程，支持具体操作+明确对象。BMS标题本身使用复数修饰的“Health indicators extraction”，此处不机械照抄其语法。数据划分的精确角色为本文特有协议，三篇范文不提供代换依据。

六层复核：修的是名词修饰和动作—对象顺序；窗口术语显化图中已有操作。没有改变阶段次序、模型数量、训练条件或结果力度。需核实的协议项不作为可直接写入的定稿。

##### LG02：图内模块名称与正文统一

位置：figures/01.png及figures/fig3_3_attention_comparison.png。

|现有英文|建议英文|性质及简短中文原因|
|---|---|---|
|L-DSConv|DSConv-L|01.png内名称与本文第3章定义不一致；统一为本文已用名称，不能因EAI用L-DSConv改正文|
|Skim Local-Global Fusion Attention|Slim Local-Global Fusion Attention|注意力对比图(d)的Skim与SLFA正式定义不符，应修拼写|
|Embed layer|Embedding layer|与正文和配置表统一层名称；不新增层|

范文依据：BMSFormer full.txt 508–514明确使用DSConv-L、DSConv-S及Local-Global Fusion Attention；Engineering-AI full.txt 898–901使用L-DSConv，但它是另一篇模型的命名，不能作为本稿轮换词。Slim全称是本文专名，以本稿定义为准，不虚构范文同名。

六层复核：仅术语/拼写一致性，不动图的运算路径或模型边界。特别是图(d)DSConv-L放在K/V支路与正文DSConv-S→局部表示→双分支不一致，必须核实际实现，不能只把图上L改成S便宣称已解决。

#### 待核实，不提交确定改稿

|位置|现有英文/问题|为何不能仅凭语言偏好修复|
|---|---|---|
|table_2_1，Oxford放电协议|variance|这是“方差”而不是清晰协议名称；正文为动态ARTEMIS工况，但需确认表格原始意图后才替换，不能凭近义猜成variable|
|table_2_hi_screening_steps，第5步|compare ... each；if ... both ...；otherwise ...|需要明确是否“任意一个已选HI同时满足两个组平均阈值便排除”，以及otherwise发生在每次比较还是全部比较后。JES full.txt 1829–1834支持排序和冗余剔除功能，不能证明本文量词逻辑|
|table_4_10，Average/Reduction|缺少显式比较基准和聚合口径|数字精度与Reduction分母应由实际计算确认；不能为了表题简洁猜公式|
|fig1，Battery role assignment|下面是Prismatic/Cylindrical/Pouch类型|若表示封装类型，Cell types更贴切；若设计者要表达实验角色，需调整图示含义，不是单纯换词|
|01.png，Turn/Back/Gate|非标准操作名或与可学习缩放混淆|确认转置与逆转置的实际位置后再命名；Gate不得擅解读为额外门控|

这些问题在前一轮回译附件也有记录；本轮将其保留为歧义/图文核实项，不用语言建议掩盖技术未决事项。

#### 全覆盖保留记录

以下“保留”指本轮未发现需新提语言修改的明确问题，不代表实验或数据经重新验证。所有数据、引用键、公式、图片路径、命令均不建议修改。

|文件|本轮结论|
|---|---|
|table_1_comparison|保留；Estimation model在SOH语境成立，既有HI算法全称不得简化|
|table_2_1|除上述variance待核，其他表头/材料/协议名称保留；排版大小写不作必改|
|table_2_2|15项定义保留，FWHM、DTV/DTC、discharge capacity等不因词长简化|
|table_2_3、table_2_4、table_2_5|保留；当前主稿未调用，仅目录附属文件|
|table_2_6|LT02可选，其余保留；绝对PCC与一般相关性不混称|
|table_2_hi_screening_steps|第5步量词待核，其余保留；retain/sort/output已经直接|
|table_4_1、table_4_2、table_4_3、table_4_3_initialization|保留；table_4_2未调用；标题/阈值与聚合名称可读，不能只为短改去必要限定|
|table_4_4|保留；Layer configurations有BMS对应原词依据|
|table_4_5、table_4_6|保留；误差比较表题与配置电池脚注对象清晰，不能把配置电池改称独立测试电池|
|table_4_7、table_4_8、table_4_9|保留；直接迁移与目标域适应在上下文可区分，不强行给每个短题加全套协议|
|table_4_10、table_4_11|Average/Reduction的定义待核；其他模块/指标名保留|
|table_4_12|保留；FLOPs、training time、parameters、storage是四种不同资源量，不能宣称全部速度最优|
|table_4_hi_input|LT01，其余保留|
|figure_2_1、figure_2_2、figure_2_3、figure_2_4|图题保留；面板映射具体，charge-side已明确侧别，不只为偏好换词|
|figure_3_1、figure_3_2、figure_3_3|图题保留；图内LG02及技术路径另列，不通过改图题隐藏|
|figure_4_1|保留；未调用的附属文件，不把validation RMSE嫁接为当前实验|
|figure_4_2、figure_4_3、figure_4_4|保留；数据集、模型比较、测过的宽度范围明确|
|comparison_panel_layout.tex|共享排版宏，无待审学术行文|
|main.tex|章节名称保留；Methodological framework在章内容语境可接受，不为逐字回译改名|

#### 统一边界

保留health indicator extraction与selection的区别；完整算法始终使用作者确认的multi-source health indicator extraction and optimization algorithm。保留lightweight/efficient、cross-cell/cross-dataset、source-only/few-shot、weight storage/memory、parameter count/training time的概念边界。already clear的句子不为了“更像范文”换近义词。图内错误可修，但当前只交付建议，无任何图/表/正文写入。
