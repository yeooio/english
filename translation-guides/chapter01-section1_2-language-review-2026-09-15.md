# 第1章 1.2「挑战分析与贡献」逐组审校记录

用途：保存本侧聊中逐句或按意思相连的整组审校结果，以便后续整合。**已确认**与**待确认**严格分开；本文件不是论文生产正文。技术原意以 `source-zh/chapters/chapter01.tex` 为准，当前工作英文以 `chapters/chapter01.tex` 为准。表格和图片命名备选另见 `module-name-pending-2026-09-15.md`。

## 1.2 开头：引出三项挑战（作者已确认；尚未写入正文）

- 原中文：现有方法面临的主要挑战可归纳为以下三点。
- 当前英文：The main challenges faced by existing methods can be summarized as follows.
- 作者确认建议：Three main challenges faced by existing SOH estimation methods can be summarized as follows:
- 回译：现有 SOH 估计方法面临的三项主要挑战可归纳如下。
- 范文依据：BMSFormer `introduction.txt` 第117–118行使用 `Three main problems ... can be summarized as follows`；JESSOHRUL `introduction.txt` 第265–266行使用 `the two main challenges ... can be summarized as below`。Engineering-AI 相同位置未设置挑战编号列表；不声称此句直接模仿三篇。范文中的多余逗号及 `as below` 不沿用。
- 状态：作者答复 `ok continue`；作为已确认审校措辞保存。论文正文目前仍为旧句，待本节整合时写入。

## 后续条目

每组记录原中文、当前英文、建议英文、范文可定位依据、回译核对、作者确认状态及是否已写入正文。没有明确批准的建议不得标成已确认。

## 挑战（1）：健康指标的跨电池稳定性（待作者确认；尚未写入正文）

- 原中文：从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。PCC和斯皮尔曼相关系数（SCC）分别用于评价线性关联与单调关联，仅采用其中一种，难以同时考察这两方面的表现。此外，即使多个指标均与SOH具有较强关联，它们之间仍可能包含重复信息。因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。
- 当前英文：Raw data collected from multiple sensors contain diverse features related to degradation. The relationship between a candidate health indicator and SOH may vary across cells, and an indicator that performs well on one cell may not retain the same representational capability on others. PCC and the Spearman correlation coefficient (SCC) evaluate linear and monotonic relationships, respectively; using only one makes it difficult to assess both aspects. Moreover, even indicators strongly associated with SOH may contain redundant information. Model input selection therefore needs to consider both correlations across cells and redundancy among indicators to reduce its dependence on the performance of a single cell.
- 待确认建议：Raw data collected from multiple sensors contain diverse degradation-related features. The relationship between a candidate health indicator and SOH may vary across cells, and an indicator that performs well on one cell may not retain the same representational capability on others. PCC and the Spearman correlation coefficient (SCC) evaluate linear and monotonic relationships, respectively; using only one makes it difficult to assess both aspects. Moreover, even indicators strongly associated with SOH may contain redundant information. Model inputs should therefore be selected based on their correlations with SOH across cells and redundancy among indicators, reducing reliance on how the indicators perform on any one cell.
- 范文依据：JESSOHRUL `introduction.txt` 挑战（1）使用 `raw data collected from multiple sensors contain diverse degradation-related features`；其后 `HI selection algorithm ... considers ... representation capabilities across all batteries in a group` 支持跨电池表现作为筛选对象。BMSFormer `introduction.txt` 的 `Estimation Accuracy Challenges` 包含 `representational capabilities of the extracted health indicators`，但不直接讨论本文的跨电池稳定性。Engineering-AI `introduction.txt` 的 `Structured Feature Selection Framework` 强调robust HI，但其指标、窗口和协议不同，不继承事实。
- 变化理由：第一句采用范文确切短搭配；末句将抽象的 `Model input selection ... its dependence` 改成明确的输入选择动作，维持跨电池相关性与指标冗余两个条件。
- 回译核对：模型输入应依据指标在不同电池上与SOH的相关性及指标间冗余来选择，以减少对指标在任一单节电池上表现的依赖。`should` 对应原中文“需要”；明确写 `how the indicators perform`，不将原文“指标表现”泛化为未限定的 `results`。
- 状态：待作者讨论确认；中间三句建议保留，非错误。此条不得作为已批准正文使用。

### 2026-09-15：依据 JESSOHRUL 对前两句及中文逻辑的重新检查（新候选；未批准）

上一候选只把 `features related to degradation` 缩成范文短搭配，未解决中文前两句的句间关系。第1.1节末已说明多源数据可提供互补退化信息；1.2挑战（1）首句重述数据多样性，却没有立即说明为何进入跨电池稳定性问题。JESSOHRUL 引言对应挑战先写多传感器特征多样性，随后用 `however` 转向其自身的“数据来源有限”缺口；本文不能照搬该缺口，但可以学习其“资源/信息丰富→现有筛选限制”的转折功能。

- 原中文前两句：从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。
- 新候选中文：多传感器数据包含多样的退化相关特征，但候选健康指标与SOH的关联可能因电池而异。在一节电池上表现良好的指标，未必能在其他电池上保持相同的表征能力。
- 新候选英文：Multi-sensor data contain diverse degradation-related features, but the relationships between candidate health indicators and SOH may vary across cells. An indicator that performs well on one cell may not retain the same representational capability on others.
- 回译核对：多传感器数据包含多样的退化相关特征，但候选健康指标与SOH的关系可能在不同电池之间变化；单节电池上表现好的指标，在其他电池上未必保持相同的表征能力。保留数据多样性、跨电池差异与单节电池表现三个事实；新增的 `but` 只将原文隐含的转折显性化，不宣称多传感器数据本身导致不稳定。
- 范文边界：JESSOHRUL 的后半句是“许多现有方法仍依赖单一或有限数据源”，与本文挑战不相同；不继承该事实，也不整句照抄前半句。其 §3.5.2 同时评价 PCC/SCC 并移除指标间冗余，功能上与本段后续推进匹配，但具体阈值和实验协议不继承。BMSFormer 对指标表征能力的讨论可作术语参照；Engineering-AI 的HI窗口和单代理设计不同，不移植其事实。
- 状态：新候选优先于上一条首句缩写方案，但**仍待作者确认**。原中文源稿及工作英文未修改；上一条保留为审校历史。

### 2026-09-15：作者偏好保留“从多传感器收集的原始数据”（待确认）

作者指出喜欢原中文的具体数据来源表达。上一候选将其缩为“多传感器数据”只是压缩，不涉及原意修复，应撤回这一缩写。`多样化` 与 `可能随电池个体而变化` 也无需仅因简洁改词。现在仅对句间逻辑提出最小候选：

- 改前中文：从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。
- 改后中文候选：从多传感器收集的原始数据包含多样化的退化相关特征。然而，候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。
- 改动理由：保留原句的数据来源、特征多样性和跨电池不确定性，只用 `然而` 标出“数据丰富不自动保证指标跨电池稳定”的隐含转折。JESSOHRUL 对应挑战用 `however` 转向其自身缺口，但本文后句改为本文的跨电池稳定性缺口，未借入“现有方法只用单一数据源”的事实。
- 状态：作者尚未确认 `然而` 是否需要；本条覆盖上一候选中缩写原始数据的建议。中文源稿和英文正文均未改。

### 2026-09-15：作者否定“然而”；撤回转折候选

作者指出 `然而` 突兀。复核后同意：多传感器数据含有多样特征与候选HI关联可能跨电池变化不是直接对立的判断；JESSOHRUL 原段的 `however` 指向其不同的“仍依赖有限数据源”缺口，不能机械移植到本文。因此撤回前两句合并或添加 `但/然而` 的候选，**保留冻结中文原文的两句及其顺序**。后续仅评估英文是否需要最小词组调整，不把中文连接词当作必改问题。所有前述候选保留为历史，不作为当前推荐稿。

### 前两句：作者认可的讨论稿（不加转折；待本节整合写入）

- 中文保持原文：从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。
- 英文讨论稿：Raw data collected from multiple sensors contain diverse degradation-related features. The relationship between a candidate health indicator and SOH may vary across cells, and an indicator that performs well on one cell may not retain the same representational capability on others.
- 作者答复：`可以的，仔细模仿范文`；认可不加突兀转折，并要求后续仍按三篇范文对应语境仔细审校。此处第一句采用JESSOHRUL确切短搭配；后半句只表达本文的跨电池稳定性问题，不复制JESSOHRUL的单一数据源缺口。
- 写入状态：仅记录，工作英文尚未修改。

## 挑战（1）后半：PCC/SCC、冗余与输入选择（待作者确认）

- 当前中文：PCC和斯皮尔曼相关系数（SCC）分别用于评价线性关联与单调关联，仅采用其中一种，难以同时考察这两方面的表现。此外，即使多个指标均与SOH具有较强关联，它们之间仍可能包含重复信息。因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。
- 建议中文：PCC衡量线性相关，斯皮尔曼相关系数（SCC）评估单调关系；单独采用其中任一种，都难以同时考察这两方面。此外，即使多个指标均与SOH具有较强关联，这些指标之间仍可能存在冗余。因此，模型输入的筛选需要同时考虑指标在不同电池上与SOH的相关性及指标间冗余，减少对单节电池上指标表现的依赖。
- 当前英文：PCC and the Spearman correlation coefficient (SCC) evaluate linear and monotonic relationships, respectively; using only one makes it difficult to assess both aspects. Moreover, even indicators strongly associated with SOH may contain redundant information. Model input selection therefore needs to consider both correlations across cells and redundancy among indicators to reduce its dependence on the performance of a single cell.
- 建议英文：PCC measures linear correlation, while the Spearman correlation coefficient (SCC) assesses monotonic relationships; using either one alone makes it difficult to evaluate both aspects. Moreover, indicators strongly correlated with SOH may still be redundant with one another. Model inputs should therefore be selected based on their correlations with SOH across cells and redundancy among indicators, reducing reliance on how the indicators perform on any one cell.
- 范文依据：JESSOHRUL `methodology.txt` §3.5.2 明确写 `PCC measures the linear correlation, while SCC assesses the monotonic relationship`，并在筛选流程中使用两种相关系数、按跨电池表现评估候选HI、移除指标间高度冗余信息。BMSFormer `introduction.txt` 挑战条目强调HI表征能力，但没有本文完整的跨电池筛选逻辑；Engineering-AI 引言的特征选择条目使用不同指标与窗口，不继承其事实。
- 改动理由：前句沿用同功能专业搭配并显式保留单独采用一种的局限；中句把“指标之间可能存在冗余”从易误读的 `contain redundant information` 改为 `redundant with one another`；末句明确SOH相关对象与单节电池上的指标表现，消除 `its` 回绕。中文建议亦仅澄清所指对象，不新增阈值、排序或实验角色。
- 回译核对：PCC衡量线性相关，SCC评估单调关系；单独使用任一种难以兼顾两方面。与SOH相关性较强的指标之间仍可能冗余。输入筛选需结合跨电池SOH相关性与指标间冗余，减少对任何一节电池上指标表现的依赖。
- 状态：待作者确认；中文冻结源稿及工作英文未修改。

### 2026-09-15：作者要求先审中文；撤回未经必要性核对的中文改写

作者指出上一条先借JESSOHRUL英文句式，再把中文改成“衡量/评估”“存在冗余”“模型输入的筛选”等，未先证明中文有逻辑问题。复核第1.1节和1.2整段后：挑战（1）的跨电池差异→PCC/SCC分别评价两类关联→指标间重复信息→联合筛选的顺序成立；`它们` 的先行词为“多个指标”，后句“单节电池表现”可由前文“在一节电池上表现良好的指标”消歧。上述中文换词没有必改理由，全部撤回，上一候选仅保留为历史。

唯一值得按作者偏好明确的中文表述是 `PCC和斯皮尔曼相关系数（SCC）` 的并列不对称。PCC已在第1.1节时间特征段定义为皮尔逊相关系数，因此原文使用缩写并非术语错误；但作者希望此处也写中文全称，使两项并列统一。

- 最小中文候选：**皮尔逊相关系数（PCC）和斯皮尔曼相关系数（SCC）**分别用于评价线性关联与单调关联，仅采用其中一种，难以同时考察这两方面的表现。
- 该句其余部分及后面两句中文保持冻结源稿原文。JESSOHRUL §3.5.2 同时给出 Pearson/Spearman 全称及PCC/SCC，再分别描述线性/单调度量，可作术语格式参照；不继承其阈值或单一数据源缺口。
- 状态：此项中文候选待作者明确确认；先定中文，再定对应英文。中文源稿及英文正文均未修改。

### 2026-09-15：挑战（1）中文整段复审结论（当前推荐；待确认）

重新读取第1.1节前文、1.2挑战及贡献（1），并对照三篇范文对应TXT后，中文段落的论证链成立。多传感器数据多样性是背景，候选指标的跨电池关联变化是本挑战；PCC/SCC分别评价线性/单调关系，多个指标仍可能含重复信息，末句将跨电池表现与指标间冗余一起纳入输入选择。两者并非直接对立，故不加“然而”。“它们”有清楚先行词；“单节电池表现”由前文指标表现限定，上下文足以消歧。无需为模仿范文强行重写“评价”“重复信息”或末句。

整段唯一当前推荐中文微调：在 `PCC和斯皮尔曼相关系数（SCC）` 中补足第一项中文名称为 `皮尔逊相关系数（PCC）和斯皮尔曼相关系数（SCC）`。PCC已在第1.1节定义，故原缩写并非错误；作者强调中文行文和并列对称，补足名称能使独立挑战条目更易读。JESSOHRUL §3.5.2 提供两全称及缩写的对应例子。其他句子维持原中文。

状态：仅当前推荐，仍待作者确认；冻结中文源稿和工作英文不修改。前述英文后半组候选需要按此中文结论重新核对，不当作已确认英文。

### 2026-09-15：挑战（1）整段中英文对照建议（中文微调已用于本轮译稿；英文待确认）

- 作者本轮答复“可以的翻译”，据此采用唯一的中文微调作为**本轮翻译目标**：`PCC和斯皮尔曼相关系数（SCC）` → `皮尔逊相关系数（PCC）和斯皮尔曼相关系数（SCC）`。其余中文维持冻结原文，不修改 `source-zh/`。
- 改后中文整段：（1）\textbf{健康指标的跨电池稳定性问题。} 从多传感器收集的原始数据包含多样化的退化相关特征。候选健康指标与SOH之间的关联可能随电池个体而变化，在一节电池上表现良好的指标，在其他电池上未必保持相同的表征能力。皮尔逊相关系数（PCC）和斯皮尔曼相关系数（SCC）分别用于评价线性关联与单调关联，仅采用其中一种，难以同时考察这两方面的表现。此外，即使多个指标均与SOH具有较强关联，它们之间仍可能包含重复信息。因此，模型输入的确定需要结合不同电池上的相关性表现与指标间的冗余关系，减少选择结果对单节电池表现的依赖。
- 改后英文候选整段：(1) \textbf{Cross-cell stability of health indicators.} Raw data collected from multiple sensors contain diverse degradation-related features. The relationship between a candidate health indicator and SOH may vary across cells, and an indicator that performs well on one cell may not retain the same representational capability on others. The Pearson correlation coefficient (PCC) measures linear correlation, while the Spearman correlation coefficient (SCC) assesses monotonic relationships. Using either one alone makes it difficult to evaluate both aspects. Moreover, indicators strongly associated with SOH may still be redundant with one another. Selecting model inputs therefore requires considering each indicator's correlation with SOH across cells and its redundancy with other indicators, reducing reliance on its performance in any single cell.
- 范文尺度与用途：JESSOHRUL `introduction.txt` 第334–340行提供 `raw data collected from multiple sensors` 与 `degradation-related features`；其后“有限数据来源”属于该文缺口，本文不移植。JESSOHRUL `methodology.txt` §3.5.2 第1320–1324行对应PCC线性、SCC单调的作用，第1468–1477行在候选指标中并列考虑跨电池相关性与指标冗余；本文不继承其阈值和筛选协议。BMSFormer `introduction.txt` 第169–174行提供HI `representational capabilities` 的术语支持，但其挑战对象与本文不同。Engineering-AI `introduction.txt` 第141–145行谈稳健指标，未提供本文跨电池/PCC/SCC的完整逻辑，故不强制借词。
- 回译自检：多传感器原始数据的退化特征多样；候选指标与SOH的关联可能跨电池变化；皮尔逊与斯皮尔曼系数分别衡量线性和单调关系，单用其一难以兼顾；与SOH关联较强的指标彼此仍可能冗余；模型输入需兼顾指标跨电池SOH相关性与指标间冗余，减少对其在单节电池上表现的依赖。未加入“单一数据源”或特定阈值，也未把“减少依赖”写成完全排除单节电池。
- 状态：中文微调被作者用于本轮译稿；**英文整段仅候选，待作者确认**。`chapters/chapter01.tex` 当前第36行仍为旧英文，未写入正文。

### 2026-09-15：挑战（1）英文确认状态更新

作者询问旧末句与新末句何者更好后，认可新句并说“可以的，continue”。据此，上条英文整段建议中的末句及整段候选作为**已确认审校措辞**保存；工作论文正文仍未写入，本侧聊按作者要求先保存记录。

## 挑战（2）：局部与长期退化信息的融合（英文建议待确认；尚未写入正文）

- 改前中文：（2）\textbf{局部与长期退化信息的融合问题。} 随着循环推进，电池容量整体呈下降趋势，并伴随相邻循环的波动和局部容量恢复。局部特征能够反映短期变化，但对长期衰减趋势的把握还需要建立跨循环联系；在聚合跨循环信息时，也需要保留局部退化细节，避免短期变化被弱化。因此，模型不仅需要提取不同时间尺度的退化特征，还需要使局部变化与长期趋势相互补充，以提高SOH估计的准确性。
- 改后中文：同改前中文。原文的“短期变化被弱化”结合模型特征聚合语境指短期变化的**表征**被弱化；这是英文需要明确的表达对象，不另改冻结中文。
- 改前英文：(2) \textbf{Fusion of local and long-term degradation information.} As cycling progresses, battery capacity generally declines, with fluctuations between neighboring cycles and local capacity recovery. Local features reflect short-term changes, but capturing long-term capacity fade trends also requires connections across cycles. When aggregating information across cycles, local degradation details must be retained so that short-term changes are not weakened. Therefore, the model needs not only to extract degradation features at different time scales but also to make local variations and long-term trends complement each other to improve SOH estimation accuracy.
- 改后英文候选：(2) \textbf{Fusion of local and long-term degradation information.} As cycling progresses, battery capacity generally declines, with fluctuations between neighboring cycles and local capacity recovery. Local features reflect short-term changes, but capturing long-term capacity fade trends also requires linking information across cycles. When information is aggregated across cycles, local degradation details must also be preserved to avoid weakening the representation of short-term changes. The model therefore needs to extract degradation features at different time scales and use local variations and long-term trends as complementary information to improve SOH estimation accuracy.
- 范文可定位依据：BMSFormer `introduction.txt` 第214–220行把 short-term/long-term features 与 Local-Global Fusion Attention、multi-scale convolution 的功能相连；但该文未给出本文完整的跨循环聚合条件，不能照搬整句。Engineering-AI `introduction.txt` 第98–107行先对比CNN的local receptive fields与Transformer的long-term dependencies，再说明 local degradation details 可能丢失；本文不移植rank collapse原因或故障检测用途。JESSOHRUL `introduction.txt` 第282–286行谈 long-term degradation patterns 和 short-term local capacity recovery behaviors；本文按已选术语保留capacity recovery，不轮换capacity regeneration，也不继承其RUL任务。
- 双轮核对：第一轮选取capacity recovery、local degradation details、短期/长期特征并置等匹配词与推进；第二轮保留“总体下降”“可能伴随波动与局部恢复”“跨循环联系”“聚合时保留局部细节”“多尺度提取及互补作用”的原意。未添加排名、因果机制或实际已改善精度的结论。
- 回译自检：容量整体下降并伴有相邻循环波动和局部容量恢复；局部特征反映短期变化，长期容量衰减趋势需要跨循环信息联系；聚合时仍保留局部退化细节，避免短期变化的表征被削弱；模型需要多时间尺度特征，并将局部变化与长期趋势用作互补信息，以提高SOH估计准确性。
- 状态：英文仅建议，待作者确认；`chapters/chapter01.tex` 第38行仍是改前英文，未写入论文正文。
