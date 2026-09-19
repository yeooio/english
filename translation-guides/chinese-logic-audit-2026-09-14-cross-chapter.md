# 中文原稿逻辑审查：跨章节范围与术语指代

日期：2026-09-14。仅审查与提案，未修改中英文论文。主审已通读冻结中文及当前英文摘要、第1–5章；本附录集中处理两个跨章节问题，章节内问题见其他附录。

## X01｜“其他电池”和“数据隔离”的参照集合不够明确

性质：范围歧义；先确认中文意图，不据此判定实际实验泄漏。

位置：[中文第2章160行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:160)、[英文同段](D:/MS-AgentNet-English/chapters/chapter02.tex:160)；结合[第4章73行](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:73)及主对比表注。

中文改前：

> 健康指标筛选仅在特征开发阶段执行。指标确定后，其定义和计算参数保持不变，并直接用于同一数据集其他电池的特征提取。用于后续评价的其他电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发与后续评价之间的数据隔离。

上下文证据：Oxford特征开发集合包含Cell1和Cell2，而第4章将Cell2作为配置电池，并在Cell2–Cell8的主比较范围中报告其结果。其他数据集也报告配置电池。表注已经标明这种角色，不能把主比较中全部电池写成未参与开发的独立留出电池。

风险：这里的“其他”若相对特征开发集合，指Cell3–Cell8等，句子可成立；若读者按第4章相对训练电池理解，则包括Cell2，与前述开发使用不符。不是所有“后续评价”都与开发集合完全不重叠。原句结尾的概括让这种误读更容易发生。

中文建议（须确认“其他”确指开发集合之外）：

> 健康指标筛选仅在特征开发阶段执行。指标确定后，其定义和计算参数保持不变，并直接用于同一数据集中特征开发集合之外电池的特征提取。这些电池不参与相关性筛选、阈值确定或指标的重新选择，从而保持特征开发数据与这些电池的后续评价数据之间的隔离。

现有英文：

```tex
HI selection is performed only during feature development. Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for other cells within the same dataset. The other cells used for subsequent evaluation do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining data separation between feature development and subsequent evaluation.
```

英文建议（同一条件下）：

```tex
HI selection is performed only during feature development. Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for cells outside the feature-development set within the same dataset. These cells do not participate in correlation-based selection, threshold determination, or HI reselection, maintaining separation between the feature-development data and the data used for subsequent evaluation on these cells.
```

改动效果：明确集合，不更换电池、不删结果、不另造第三种协议角色。若作者原意是“包括配置池在内的全部主比较结果均属独立留出评价”，则不是上述语言修补能解决的，需要核实协议及相应结论；不能直接采用此候选掩盖问题。

范文参照：本轮重读Engineering-AI full.txt 333–409的相关语境，仅取可连续确认的338–342行，原文短语为“performed exclusively on available historical reference data”，中文释义“仅在可用历史参考数据上执行”。见[原文](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:340)。它支持在说明筛选时写清数据范围，但其training partition不等于本文两电池开发集合，不能照搬协议，也不继承其自证式措辞。

需要作者确认：本段数据隔离是否仅针对特征开发集合之外的电池？若是，以上属于范围显式化；若不是，先核协议。

## X02｜“不同电池体系和运行条件下的泛化”容易与跨数据集迁移混读

性质：可澄清的任务范围，不是确定语法错误。

位置：[中文第2章23行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:23)，结合第4章4.3.2、4.4、4.5以及结论。

中文改前（本段首句，后文不动）：

> 为考察所提方法在不同电池体系和运行条件下的泛化能力，选取 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四组公开电池老化数据开展实验。

上下文证据：第4章各数据集分别指定训练、配置电池，主比较为各自数据集内部的跨电池结果；另设第4.5节跨数据集source-only和适应实验，输入定义也另外统一。不能把“多种数据集上分别训练与评价”读成“一个模型直接跨化学体系泛化”。

中文建议（若本句主要介绍四组数据对域内实验的覆盖）：

> 为考察所提方法在不同电池体系和运行条件下的估计性能及各数据集内的跨电池泛化能力，选取 Oxford、CALCE CS2、CALCE CX2 和 MIT/Severson 四组公开电池老化数据开展实验。

现有英文：

```tex
Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, are selected to examine the generalization capability of the proposed method across different battery systems and operating conditions.
```

英文建议（上述意图下）：

```tex
Four public battery aging datasets, Oxford, CALCE CS2, CALCE CX2, and MIT/Severson, are selected to examine the estimation performance of the proposed method under different battery systems and operating conditions, as well as its cross-cell generalization within each dataset.
```

效果与边界：把工况覆盖与泛化范围分开，未新增实验。如果作者希望本句同时概括另设的迁移实验，可保留较宽概括并在后文明确域内与跨域实验分别进行；不要求机械增加所有限定。

范文参照：本轮完整读取BMSFormer full.txt 270–299的连续框架说明，284–293行把训练和配置后对其他电池的评价明确限定在“other batteries in the corresponding dataset”（对应数据集中的其他电池）。见[原文](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:290)。只借用数据集内范围的明确表达，不继承其30%/70%划分或384组设置。范文不证明本文实验正确。

## 不是本轮错误的内容

- 第4章已明确区分source-only与使用目标域数据的适应，不把二者混称零样本迁移。
- 结论保留“域内”“一定的”“潜力”，并把嵌入式硬件验证列为未来工作；不要求改成已完成部署。
- 主对比表已经标注配置电池身份，不能仅凭报告配置池结果断言数据泄漏或要求删行。
- 本附录不验证模型训练代码、实际数据访问日志或原始数据处理流程；仅指出稿件表述的范围与一致性风险。
