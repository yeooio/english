# 英文上下文一致性专项：时态与语态

日期：2026-09-14。范围：通读当前 `chapters/abstract.tex` 和第 1–5 章全文，集中检查时态、语态、叙述主体是否出现无理由漂移；核对中文摘要、数据集与实验语境。只新建本报告，未改正文。

## 结论

本专项未发现需要强制修改的时态或语态问题，也不为统一形式另加可选改动。全文主要以现在时描述本文方法、流程和图表结果，以过去时叙述既有研究和原始数据采集，以将来时提出未来工作。这样的功能分工清楚。

“上下文一致”不是全文只能使用一种时态或一种语态。简单美式表达也不要求把所有被动句改成 `we + 动词`。以下记录容易被误判的位置及保留依据；其他代理负责术语和句子直接性，不能把本报告的零项理解为所有语言维度都没有建议。

## 本轮重新查看的范文语境

- BMSFormer `full.txt` 30–40：完整摘要；1078–1082 接 1092–1105：实验总述与训练环境（中间插入图题/页眉，非正文衔接）；1372–1376：比较实验开头；1387–1390：完整训练超参数条目；2014–2021：完整未来工作段。
- JESSOHRUL `full.txt` 33–50：完整摘要；1195–1226：模型配置、预处理与超参数搜索段；1408–1425：Oxford 老化协议后半段及完整 NASA 段；645–668：ReLU 设计说明连续段；4095–4100：完整未来工作段。
- Engineering-AI `full.txt` 1142–1153：完整结果章节总述两段；1332–1336：搜索结果与敏感性分析引入；1363–1374：完整平滑退化结果小节；1376–1378：选定最终配置的完整句。只把语法独立且连续明确的句段用于本报告，不把双栏插入段拼接为论证顺序。

本轮是语法审校，不是新增段落翻译；不宣称重新完成了三篇全文句数或句长测量。

## 1. 摘要：现在时方法 → 过去时比较 → 现在时结果

位置：`chapters/abstract.tex:1`。

现有英文：

> We compared the proposed model with various mainstream deep learning models on four public battery datasets with different chemistries and operating conditions. The experimental results show that MS-AgentNet achieves better overall performance while maintaining low computational and storage overhead, further highlighting the advantages of its lightweight design for resource-limited BMS.

建议英文：保留原句，不把 `compared` 改为 `compare`，也不把 `show / achieves` 连带改成过去时。

范文是否也如此：是。JESSOHRUL 摘要 33–50 先以 `this paper proposes`、`are applied` 和 `is proposed` 介绍本文方法，再以 `comparative experiments were conducted` 叙述已做实验，最后以 `experimental results demonstrate` 和 `achieves` 陈述结果。BMSFormer 摘要 30–40 采用现在时实验描述，说明范文没有单一统一模板。

同条件判断与中文原因：中文明确是“进行了比较”，英文过去时忠实；紧接的结果是论文当前呈现的发现，现在时自然。其功能转换与 JESSOHRUL 相同，并非润色遗漏。保留 `We compared` 也比改成名词化被动结构直接。

## 2. 数据集：历史采集与当前数据内容

位置：`chapters/chapter02.tex:29`。

现有英文：

> The aging tests were conducted at a constant temperature of 40 ℃. The cells were charged to 4.2 V using a constant-current--constant-voltage protocol and then discharged following a dynamic current profile derived from the urban ARTEMIS drive cycle until the voltage reached 2.7 V. Aging records from cycling tests on all 8 cells, Cell1–Cell8, are included in the experiments.

建议英文：保留原句（此处为显示方便省略 LaTeX 引文命令，正文不动）。

范文是否也如此：是。JESSOHRUL 1408–1425 用 `were conducted`、`were discharged`、`were taken` 或 `underwent` 叙述原始实验，而以 `contains` 说明数据内容、以 `are shown` 说明本文图表。不同语义对象使用不同时态。

同条件判断与中文原因：中文既述原始老化协议，也述本文纳入哪些记录。英文区分已完成的采集与论文当前使用的数据，恰当。Oxford/CALCE 的 `is provided` 表示来源，MIT 的 `was jointly released` 表示发布事件；后者接 `It uses` 描述数据集构成，不构成矛盾，无须机械替换。

## 3. 第 4 章实验流程：现在时并非不规范

位置：`chapters/chapter04.tex:73`、`:117`。

现有英文：

> For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges.

> In source-only evaluation, the model is trained only on the source-domain reference cell and directly tested on the target-domain cell without updating its parameters using target-domain data.

建议英文：保留原句，不开展全章 `is/are → was/were` 批量修改。

范文是否也如此：是。BMSFormer 1078–1105 使用 `are employed`、`is reserved`、`is then directly tested`、`is conducted`；1387–1390 使用 `are used`、`is trained`、`is ... set`。JESSOHRUL 1201–1226 使用 `are normalized`、`are ... partitioned`、`is employed`、`is selected` 描述实验及调参。Engineering-AI 1142–1153 则用 `we adhered`、`were trained`、`served` 回顾实验；1332–1336 同时使用 `covered`、`visualizes`、`was ... analyzed`、`reveals`。

同条件判断与中文原因：本文第 4 章持续按实验流程和图表说明的现在时叙述，未在同一功能中反复无理由切换。BMSFormer 与 JESSOHRUL 的同类流程支持保留；不能单凭 Engineering-AI 的另一种合法选择，要求整章改过去时。条件、训练/测试对象的准确性属于另一个核实维度，不由动词时态证明。

## 4. 方法步骤：主动和被动按信息焦点切换

位置：`chapters/chapter03.tex:110`、`:131`。

现有英文：

> The input is first transposed so that the embedding dimension becomes the convolutional channel dimension. The first $1\times1$ pointwise convolution then expands the channel dimension to $2d$.

> A ReLU activation is then applied to introduce nonlinearity:

建议英文：保留原句。

范文是否也如此：是。JESSOHRUL 645–668 在 `a ReLU activation function is applied`、`This design is primarily motivated` 与 `ReLU ensures`、`mapping alleviates` 等主动句之间切换。BMSFormer 806–817 在 `each channel is convolved`、`outputs ... are then combined` 与 `This step mixes`、`DSConv separates` 之间切换。两文的某些力度和用词未必适合本文，本报告只借其正常的信息焦点安排，不借其效果主张。

同条件判断与中文原因：本句中被动语态突出“输入/激活操作”，主动语态明确“卷积做什么”，主语可辨，动作顺序明确。全部改被动会削弱主干，全部改主动则会增加重复的 `we`。这里没有“词汇简单但表达绕”的独立语态缺陷。

## 5. 结果与未来工作：现在时发现、将来时计划

位置：`chapters/chapter05.tex:5`。

现有英文：

> Future work will focus on HI construction for incomplete charging and dynamic operating segments, together with lightweight domain adaptation strategies. Further validation will cover more battery chemistries, real-vehicle operating data, and embedded hardware platforms to improve the framework's practical applicability and deployment reliability.

建议英文：保留原句，不为了与前两段的现在时统一而改写。

范文是否也如此：是。BMSFormer 2014–2021 与 JESSOHRUL 4095–4100 都用 `Future research will focus` 表示后续工作，接现在时说明这些工作的目的。Engineering-AI 1363–1374 用 `achieves` 等现在时解读已有结果；本文结果章节和结论中的 `show / achieves / maintains` 属同类功能。

同条件判断与中文原因：明确区分当前已有结果与后续计划，尤其不能把尚未做的嵌入式验证改成已完成语气。

## 最终范围说明

确定需要修改的时态/语态问题：0 项。本结论不以“范文也这样”作为无条件放行，而是结合本文句子功能、明确主语、中文含义和上下文判断。可以结束本专项的机械时态统一检查；如其他专项改动了句子，实施前仍需在整段复查时态和语态是否自然。
