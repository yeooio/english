# 第4章中文句法、句间逻辑与英文承接复核

2026-09-14。仅提出建议，不修改论文。本报告区分“中文有确定病句”“对象有歧义”“结果到结论跨越了证据范围”；不把偏好短句当作语法规则。

本轮阅读中英文各章以理解全文，重点复核第4章及表图标题、表注；重新查看三篇 results.txt 中对应的结果描述上下文。旧三轮结果报告只用于去重。本次报告主体保留1项新对象歧义与1项本轮独立复核的操作歧义；后者经主审去重，旧语言报告已有，不计新增。未读取原始预测数组或核验曲线像素，不能将图中现象称为本轮已经证实。

## 1. “局部偏离”指真实轨迹还是预测误差？【新增：待核实对象歧义】

定位：`source-zh/chapters/chapter04.tex:94`；`chapters/chapter04.tex:94`。

**改前中文**

> 值得注意的是，Cell4 的局部偏离和 Cell6 后段的快速下降使各模型表现出不同程度的跟踪偏差。

**现有英文**

> In particular, the local deviations in Cell4 and the rapid decline in the later stage of Cell6 lead to different degrees of tracking error.

**问题与原因**

前一句讲“预测结果存在差异”，本句却没有说明 Cell4 的“局部偏离”是谁偏离谁。若指真实 SOH 轨迹偏离平滑趋势，它是待跟踪的变化；若指预测曲线偏离真实 SOH，它已经是跟踪误差，后面的“使……跟踪偏差”便把同一现象写成了原因和结果。英文 local deviations 继承了这一歧义，lead to 又把未分清对象的关系固定成因果。

这属于**词汇简单但表达绕：对象省略＋因果回绕风险**，不是“deviation 这个词难”。不能直接擅改为容量恢复、膝点或突降，因为现有句子没有确认具体曲线形态。

**条件式改后中文——若作者所指为真实 SOH 的局部变化**

> 值得注意的是，在 Cell4 的真实 SOH 出现局部变化的区间，以及 Cell6 的真实 SOH 在后段快速下降的区间，各模型表现出不同程度的跟踪偏差。

**对应建议英文**

> In particular, the models show different degrees of tracking error in regions with local changes in the true SOH of Cell4 and a rapid late-stage decline in the true SOH of Cell6.

**改后效果**

“真实 SOH 的变化区间→该区间内模型的跟踪表现”成为明确的观察关系。所有电池、阶段和比较对象保留。这里把“导致”改成“在……区间内”，是对证据关系的谨慎调整，不能宣称只是无损换词。若原意确为预测偏差，应改为“Cell4 的局部区间以及 Cell6 后段快速下降区间内，各模型的跟踪偏差程度不同”，并按实际曲线确认具体范围。

**本轮范文依据**

- Engineering-AI `results.txt:261–263`，§5.3.1，用短语 `abrupt SOH drops or local knee-points` 明确所说的是 SOH 本身的变化。这里只借鉴对象明确性，不能把其 Cell2/Cell6 现象移植给本文 Cell4。
- BMSFormer `results.txt:1003–1008`，§4.3.2，分别陈述 `estimated SOH` 与 `true SOH`，再把局部讨论绑定到 `localized magnifications`。可借鉴“先区分真实变化与估计误差”，不继承其强弱评价。
- JESSOHRUL `results.txt:112–120`，§4.2.1，先说明整体曲线及误差分布，再将 `short-term capacity fluctuations` 对应到细节子图。它提供观察对象和图形范围的写法，不证明本文发生了同类波动。

## 2. “固定RAA”容易被理解为冻结权重【本轮独立复核：旧语言报告已有候选】

定位：`source-zh/chapters/chapter04.tex:156`；`chapters/chapter04.tex:156`。

**改前中文**

> 为进一步区分多尺度 DSConv 中两个卷积尺度的作用，固定 RAA 模块并仅调整卷积尺度，设置 S0（仅保留 RAA）、S5（RAA 与核长度为 5 的 DSConv-S）、S31（RAA 与核长度为 31 的 DSConv-L）和 SFull（RAA、DSConv-S 与 DSConv-L）四种尺度变体。

**现有英文**

> To further distinguish the roles of the two convolutional scales, RAA is held fixed while only the convolutional scale is changed. Four variants are considered: S0 (RAA only), S5 (RAA with DSConv-S of kernel length 5), S31 (RAA with DSConv-L of kernel length 31), and SFull (RAA, DSConv-S, and DSConv-L).

**建议中文**

> 为进一步区分多尺度 DSConv 中两个卷积尺度的作用，在各变体中均保留 RAA 模块，仅调整卷积尺度，设置 S0（仅保留 RAA）、S5（RAA 与核长度为 5 的 DSConv-S）、S31（RAA 与核长度为 31 的 DSConv-L）和 SFull（RAA、DSConv-S 与 DSConv-L）四种尺度变体。

**建议英文**

> To further distinguish the roles of the two convolutional scales, all variants retain RAA, while only the convolutional scale is changed. Four variants are considered: S0 (RAA only), S5 (RAA with DSConv-S of kernel length 5), S31 (RAA with DSConv-L of kernel length 31), and SFull (RAA, DSConv-S, and DSConv-L).

**修改原因与效果**

“固定模块”可能指结构保留，也可能指参数不更新。第117行刚在迁移实验中介绍过特征提取模块冻结，使此处 held fixed 更容易发生操作层级混淆。S0/S5/S31/SFull 的定义能直接支持“四种变体均包含RAA”，却不能证明其参数被冻结。最小改法明确保留的是模块，将权重训练规则留给真实实验记录，不凭文字补“重新训练”或“共同初始化”。若作者实际冻结了RAA权重，则应另交代冻结方案，不能采用本句来隐去该实验事实。

范文提供的是**结构配置的表述依据，不是本文权重更新规则的依据**。本轮重新查看 Engineering-AI results.txt:954–967 的卷积消融说明，以 `substituting them with standard convolutions` 明确结构替换操作。只能参考明确结构层面操作的写法，不能从模块配置推断参数冻结。本文本句最直接的依据仍为同段四种变体的明确组成。

## 独立补查后未上升为确定错误的表达

- 第105行中文“退化轨迹较为连续”，英文 `degradation trajectories are more continuous`：连续性与平滑程度不是一回事，英文也不适合不加说明地比较“更连续”。但在未看图确认前，不能擅改成更平滑或没有转折。若作者想说变化更平缓，可对应改为“退化轨迹较为平滑”与 `smoother degradation trajectories`。这是一个待确认原意的候选，不计作已证实语法错误。
- 第123行 `represents degradation trends well` 对应“较好地表征退化趋势”，结合本章R²定义可以理解为预测拟合。若需要消除与潜在特征表示能力的混读，可改为 `fits the degradation trends well`／“较好地拟合退化趋势”；并无证据需要改变0.8421、0.7847及MAE，故不把普通搭配优化计成新的逻辑错误。
- 第135/137行 continuously：四档比例均改善是表4-9的真实展示，不能因取值离散便宣布趋势句为假。第137行限定tested ratios已在旧报告出现，不计新发现。若作者希望英文更准确，135行可写 `MAE, MAPE, and RMSE decrease at each successive adaptation ratio for both source-domain settings`，中文对应“在两种源域设置下，随着适配比例逐档增加，三项误差均下降”。这是范围精确化，不是发现了新的结果矛盾。

## 保留与范围说明

- 保留第125行涉及 Oxford 的负R²与迁移困难说明；没有因积极结论而遮掩失败方向。
- 保留第152行“单模块只改善部分数据集”，以及第158行“与设计目标一致”；不能升级为唯一机制的因果证明，也不需为了谨慎而取消所有解释。
- 保留第170行 LSTM 最短训练时间、MS-AgentNet 最低 FLOPs/参数/权重存储的不同指标归属。旧报告关于主精度配置与复杂度配置不同的澄清仍有价值，此处不重复扩为新错误。
- 初始化均值/重复统计、消融Average/Reduction定义和评价电池集合、迁移R²/RMSE统计口径均为旧报告待核实项。本轮不从未舍入结果缺失推断数值造假或计算错误。
- 结果图标题未发现需要新增的中文语法修改；图注审查不等于图形事实核验。

本轮范文重新阅读范围：Engineering-AI results.txt 233–331、954–1036及1080–1140，BMSFormer results.txt 972–1029，JESSOHRUL results.txt 44–120。TXT存在双栏顺序问题：例如Engineering-AI §5.3.2出现在§5.3之前、JESSOHRUL §4.1出现在§4.2之后。本报告只借用内部连续完整的观察句和定位短语，不据该提取顺序论证范文段落推进；未声称完成PDF阅读顺序复原或新句长计数。


主审补充核验：主审已查看 figures/Oxford/cell4.png 与 cell6.png，确认真实曲线存在本项所说的局部变化/尾段快速下降。故第1项可以采用真实SOH变化区间的写法；曲线观察仍不单独证明 lead to 的因果关系。本子审未自行查看这些图像。

