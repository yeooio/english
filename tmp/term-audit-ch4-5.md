# 第4/5章及交叉图表术语核查（只读建议，2026-09-16）

范围：已完整阅读 chapter04.tex、chapter05.tex；交叉检索现行 chapters/tables/figures 的 TEX。重读三篇范文的复杂度/效率评价完整对应段落及结论相关语境，不将参考文献标题当正文术语证据。图1三处图内词由 root 实际看图提供，以下明确区分这些视觉证据与本 agent 读取的文本。

## 建议统一的同对象名称

1. **MIT/Severson / MIT**
   - 正式名称：chapter02.tex:23,35,37；chapter04.tex:73,85,103；chapter05.tex:3；table_4_6.tex:33,39 为 MIT/Severson。
   - 简称：chapter04.tex:65,101,158；table_4_3.tex:3,10；table_4_10.tex:19；table_4_11.tex:19 为 MIT。
   - 建议：正文、题名和表格均固定 MIT/Severson；若图面确需简称，首次明确 “MIT/Severson (MIT)” 后统一允许 MIT。当前不是两个数据集，但用户本轮要求严格单名，值得收录。
   - 依据/边界：三篇范文主要采用 Oxford/NASA/CALCE，不能据此冒充它们规定了 MIT/Severson 的命名。本文来源和已建立名称优先；未找到对此简称单独批准的条目。

2. **capacity fade curves / capacity degradation curves**
   - chapter02.tex:23 对图2使用 capacity fade curves；figures/figure_2_2.tex:6 对同一图使用 capacity degradation curves。chapter04.tex:94,103,105,109 使用 capacity fade。
   - 建议图题统一 capacity fade curves。不要把所有 degradation（电池整体退化、局部非线性轨迹等）批量改为 capacity fade。
   - 范文：EAI full.txt:145 有 capacity fade，:327 有 capacity degradation；BMS full.txt:434,479 和 JES full.txt:1415,1424 使用 capacity degradation curves。范文本身容许两词，因此这是项目同一对象的命名统一，不是英文错误。
   - 批准依据：terminology.md:169 已确认容量衰减为 capacity fade；approved-translations.md:212 同样记录。

3. **Cross-battery / Cross-cell**（图1为 root 视觉核实）
   - figures/fig1.png Generalization 框：Cross-battery and cross-dataset evaluation；本文 chapter04.tex:83,101,109、chapter05.tex:3 采用 cross-cell。
   - 建议图中 Cross-cell and cross-dataset evaluation。
   - 范文同条件：JES full.txt:1970–1990 完整跨电池实验段明确 cross-cell generalization performance（1981）；确为训练后评估其他 cells，与本文电池级泛化概念对应。BMS/EAI 也使用额外测试电池，但不能把它们的训练/验证划分照搬过来。
   - 项目规范：terminology.md:100 固定 cross-cell generalization；需要区分域内时才加 in-domain。是可建议统一的同概念异词，不是增加新协议。

4. **Source-only testing / source-only evaluation / Direct cross-dataset transfer**
   - figures/fig1.png：Source-only testing（root 视觉核实）；chapter04.tex:117：source-only evaluation；table_4_7.tex:3：Direct cross-dataset transfer results。
   - 建议图统一 Source-only evaluation；表题可统一 Source-only evaluation across datasets。source-only evaluation 保持为未用目标域数据更新参数的专门协议名；cross-dataset transfer 是包含它和 few-shot adaptation 的上位任务，不可相互全局替换。
   - 批准/规范：terminology.md:121,209 已固定 source-only evaluation。三篇当前对应实验语境没有与本文相同的 source-only/few-shot 协议可直接替换；必须以本文定义为准。不是声称三篇全文不存在这些词。

5. **Model size / Storage / storage size / weight storage size**
   - 图1效率框 Model size（root 视觉核实）；table_4_12.tex:10 为 Storage (KB)；figure_4_4.tex:4 为 Storage sizes / storage size；chapter04.tex:145,170,172 为 storage size；chapter04.tex:166 正式定义 weight storage size。
   - 建议正式指标统一 weight storage size；表头可写 Weight storage (KB)，图题写 Weight storage size。storage overhead 可在概括资源负担时保留，不必认为每次 overhead 都是新指标。chapter01.tex:27 的 expand model size 是一般模型规模，不属于此指标，不能批量替换。
   - 范文同条件：BMS full.txt:1344–1406 的效率段定义 Storage size（1368,1385–1386）为 os.path.getsize 测量；JES full.txt:3793–3849 完整复杂度段也以 os.path.getsize 定义 storage size（3806–3808），与本文口径相近。
   - EAI full.txt:2434–2435 明称 Model Size (Storage) 为 actual Flash memory footprint；结论:2821–2822 用 storage footprint。其硬件验证语境不同，不能因图1出现 Model size 就建议本文沿用 Flash/memory footprint。
   - 规范：terminology.md:63 首选 storage size，:64 禁止随意轮换 footprint，:212 在全文翻译口径下进一步指定 weight storage size。推荐按更明确的后项固定。当前 storage size 是上下文限定后的缩写，无测量对象混淆；严格统一为显示规范改进。

## 应保留或仅可选调整

- **parameter count / trainable parameter count / Parameters**：chapter04.tex:166 已明确定义统计可训练参数；:170 参数量与表4-12数值一致；table_4_12.tex:10 的 Parameters 是表头缩写。BMS full.txt:1365–1368 自己即用 Parameters 定义 total number of trainable parameters，EAI:2432 用 Number of Parameters (Params)，JES:3797 用 parameter count、:3804–3805 用 trainable parameters。范文也如此，同一条件无歧义，不应列为错误。若用户要求表头极严格，可以写 Trainable parameters；首次指标全称保留 trainable parameter count（terminology.md:211）。
- **FLOPs**：chapter04.tex:166 定义单次前向 floating-point operations，table_4_12.tex:10 FLOPs (M)，:170 0.045760 M FLOPs，相同对象，无拼写或单位名称多版本。BMS:1360–1362、JES:3800–3802 同为单次前向；EAI:2430 是完整充电周期累计开销，口径不同，不能为了复用把本文改成其累计 FLOPs。
- **CNN-LSTM / CNN-BiLSTM / CNN-BiLSTM-AM**：chapter01.tex:15 的 Tian 等工作先说 CNN-BiLSTM 架构、再说 CNN-BiLSTM-AM 模型；第4/5章及实验表使用 CNN-LSTM 基线。是不同引用模型与不同网络结构，不是同名漂移；不可统一删除 Bi 或 AM。当前 TEX 实验表中未发现 CNN-BiLSTM 误替代 CNN-LSTM。
- **training cell / configuration-selection cell / source-domain reference cell / target-domain reference cell**：chapter04.tex:73 给主实验训练及选配置角色；:117–119 给迁移训练/适应角色及具体电池。不能一刀切把 reference cell 改为 configuration-selection cell。若要更直接，source-domain training cell / target-domain adaptation cell 是候选角色名称，但属于新规范提案，不是已批准词。BMS:284–289,1081–1099 和 JES:1973–1979 为同电池早期训练、后期验证，本文不是同条件，不能把范文 validation sets 强套到配置电池。
- **table_4_5.tex:70 / table_4_6.tex:52 的 cells used for model configuration**：是 configuration-selection cell 的解释短语，同一含义；可为严格名称一致改为 configuration-selection cell(s)，但不是新增独立角色。
- **cross-dataset transfer / cross-domain adaptation / few-shot adaptation**：chapter04.tex:117 明确上下位关系，chapter05.tex:5 总述 domain adaptation；三者任务范围不同，不能全局替换为一个词。
- **capacity fade / battery degradation**：前者是容量降低，后者覆盖更广退化；只建议统一同一组曲线的两个称谓，不建议抹去概念区分。

## 核查限制

没有修改正文、表格或图片。此报告未独立逐张 OCR 所有栅格图；图1证据来自 root 实际查看。历史批准记录中，范文已核实词、全文授权词和单独作者确认词应区分，以上已分别注明。当前没发现第4/5章正文将权重文件指标误写为 runtime memory 或 inference latency；这是对本次范围的结论，不宣称整份外部材料没有这些词。
