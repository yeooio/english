# 数字结果到应用含义的回归审查（2026-09-16）

## 审查结论

作者提出的问题成立。第四章已有充分的数字比较，但多数段落停在“误差更低、模块有效、复杂度更小”的方法层结论。除复杂度分析末句和第五章的笼统应用潜力外，数字尚未系统回答以下应用问题：

1. 已训练模型能否在同一数据域的其他电池上直接复用；
2. 更换电池化学体系或运行协议后，直接迁移是否可靠；
3. 少量目标域数据究竟能解决到什么程度；
4. 低FLOPs、参数量和权重文件大小对资源受限BMS分别意味着什么；
5. 当前实验还没有验证哪些部署条件。

这不是单纯的英文措辞问题，而是中文源稿的讨论层级也较弱。若要修正，应先由作者批准中英文内容扩展，不能只在英文中静默新增应用结论。

## 范文尺度

- BMSFormer先给出存储数字，再回到资源受限设备的适用潜力；其结论同时把真实BMS集成与部署评价列为未来工作。因此可学习“数字→资源含义→部署边界”的结构。
- Engineering-AI拥有CPU推理延迟和TI Cortex-M4硬件在环验证，因而可以讨论实时响应与嵌入式可行性。本文没有对应实验，不能复用其`real-time capability`或“已经适合部署”的力度。
- JESSOHRUL把FLOPs、参数量和存储大小与资源受限环境联系起来，但其部分部署表述强于本文证据。本文应采用其表达路径，降低结论力度。

## 建议一：HI结果回到输入构建

位置：`chapters/chapter04.tex:43–45`之后。

现有数字：HI1在Cell2–Cell8上的平均MAPE为0.615%，且单一HI1优于四种HI直接融合。

建议中文：

> 从应用角度看，该结果支持在同一数据集内采用定义和参数固定的紧凑HI输入，而不是针对不同电池重复筛选指标或直接叠加多类特征。该实验说明减少输入冗余没有削弱本组Oxford电池的估计性能，但尚未量化在线特征提取时间。

建议英文：

> From an application perspective, these results support the use of a compact HI input with fixed definitions and parameters across cells within the same dataset, rather than repeating HI selection for each cell or directly combining multiple feature types. The results show that reducing input redundancy does not compromise estimation performance on the evaluated Oxford cells, although online feature-extraction time has not been quantified.

边界：只能说明紧凑输入和固定规则；没有实测特征提取时间，不能写成已经降低在线时延。

## 建议二：跨电池数字回到模型复用

位置：`chapters/chapter04.tex:109`之后。

现有数字：六个CALCE/MIT电池上的平均$R^2$为0.9896，平均MAE、MAPE和RMSE分别为0.00707、0.013335和0.01188；模型训练和配置完成后直接用于相应数据集中的其他电池。

建议中文：

> 由于训练完成的模型直接应用于相应数据集中的其他测试电池，而未针对每个测试电池重新训练，上述结果说明该模型具有在相同数据域内跨电池复用的潜力。这一结论仍限于当前数据集和测试条件，不能等同于跨数据集或跨化学体系泛化。

建议英文：

> Because the trained model is directly applied to other test cells in the corresponding dataset without cell-specific retraining, these results support its potential for model reuse across cells within the same data domain. This evidence remains limited to the evaluated datasets and conditions and does not establish cross-dataset or cross-chemistry generalization.

应用含义：不是泛泛的“稳健”，而是已训练模型在同域其他电池上的复用潜力。

## 建议三：迁移数字回到新电池域适配

位置：`chapters/chapter04.tex:137`之后。

现有数字：CALCE域之间迁移较好；涉及Oxford的四个方向在源域直接测试时$R^2<0$。采用30%目标域数据适配后六个方向的误差均下降，但涉及Oxford的四个方向仍为$R^2<0$。进一步提高目标域数据比例能够继续改善结果，且CS2始终优于CX2作为源域。

建议中文：

> 从实际应用角度看，这些结果表明，当新电池域与训练域在化学体系、运行协议和退化轨迹上差异较大时，直接复用源域模型并不可靠。冻结特征提取模块并利用目标域早期数据更新读出层能够降低适配成本并改善估计结果，但其效果仍取决于源域选择和可获得的目标域数据量；因此，当前模型尚不能在缺少目标域校准的情况下直接用于差异较大的新电池系统。

建议英文：

> From an application perspective, these results show that direct reuse of a source-domain model is unreliable when a new battery domain differs substantially in chemistry, operating protocol, and degradation trajectory. Updating only the readout layer with early target-domain data improves estimation while keeping the feature extractor fixed, but the outcome still depends on source-domain selection and the amount of available target-domain data. The current model therefore cannot yet be directly applied to substantially different battery systems without target-domain calibration.

边界：`降低适配成本`缺少与完整重训练的时间或资源对比，若严格保持现有证据，中文宜改为“提供一种保持特征提取模块不变的适配方式”，英文相应改为`provides an adaptation route that keeps the feature extractor fixed`。

## 建议四：复杂度数字回到BMS资源约束

位置：`chapters/chapter04.tex:170–172`。

现有数字：MS-AgentNet每次前向传播为0.045760 M FLOPs、4,643个可训练参数和27.44 KB权重文件，三项在五种模型中最低；但训练时间为123.338 s，是表4-12中最长的，而不是最短的。

需要首先补清：本文的资源优势是前向运算量、参数量和权重存储，不是训练速度。

建议中文：

> 需要指出的是，MS-AgentNet在统一测试中的训练时间并非最低，因此其资源优势主要体现在单次前向传播的运算量、参数量和权重存储，而不是训练速度。0.045760 M FLOPs和27.44 KB权重文件分别表明较低的每次估计运算需求和持久化存储需求，这两项指标直接对应资源受限BMS的计算与存储约束。然而，本文尚未在嵌入式硬件上测量推理延迟、峰值运行内存和能耗，因此这些结果说明的是轻量化部署潜力，而不是已经完成实时部署验证。

建议英文：

> MS-AgentNet does not have the shortest training time in the unified test; its resource advantages therefore concern forward-pass computation, parameter count, and weight storage rather than training speed. The 0.045760 M FLOPs per forward pass and the 27.44 KB weight file indicate low arithmetic and persistent-storage requirements per SOH estimate, both of which are directly relevant to computation- and storage-constrained BMS. However, inference latency, peak runtime memory, and energy consumption have not been measured on embedded hardware. These results therefore establish potential for lightweight deployment rather than verified real-time deployment.

该段是全文最需要的“数字→应用→证据边界”桥接。

## 建议五：第五章用关键数字收束应用意义

位置：`chapters/chapter05.tex:3–5`。

当前结论只说“低参数量和存储开销”“具有应用潜力”，没有把第四章最关键的数字带回应用，也没有明确跨域结果对实际使用的限制。

建议在结论结果段中保留三组信息：

1. 精度：代表性误差优势及同域跨电池表现；
2. 资源：0.045760 M FLOPs、4,643个参数、27.44 KB权重文件，并明确训练时间不占优；
3. 适用边界：同域模型复用具有潜力，但跨差异较大的电池域仍需目标域校准，尚未完成嵌入式验证。

建议英文核心句：

> Under the unified complexity setting, MS-AgentNet requires 0.045760 M FLOPs per forward pass, 4,643 trainable parameters, and 27.44 KB for weight storage, the lowest values among the five compared models, although its training time is not the shortest. These results indicate low arithmetic and storage requirements relevant to resource-constrained BMS. The cross-cell results support model reuse within the same data domain, whereas the negative $R^2$ values in the Oxford-related transfer directions show that substantially different battery domains still require target-domain calibration. Embedded inference latency, runtime memory, and energy consumption remain to be validated.

## 优先级

- **必须补强**：跨数据集迁移后的应用判断；复杂度数字对应的BMS资源含义与部署边界；第五章的数字化收束。
- **建议补强**：跨电池结果对应同域模型复用。
- **可选**：HI1单特征结果对应紧凑输入。
- **不建议强行加入应用讨论**：初始化与收敛、每一项消融结果。它们主要回答训练稳定性和结构有效性，逐段添加BMS意义会显得牵强。

本审查仅形成建议，尚未修改论文正文或冻结中文源稿。
