# 第4章中文逻辑与英文承接审查（2026-09-14）

本轮只提建议，未修改中文源稿、英文正文、表格或图片。中文全文第4章、对应当前英文及全部 table_4*.tex、figure_4*.tex 已逐项读取；图注审查不等于重新核验原始预测数据或逐像素图像。主审负责跨章协议一致性，本报告不把配置电池进入报告范围直接判为数据泄漏。

结论不是“中文很多语法错误”：发现 1 项确定中文主语问题（英文已经处理），3 项需要作者确认的证据/定义问题，3 项可选范围澄清，另有 1 项中文较强、英文已收窄的保留说明。以下编号 R01–R08。没有为了改动数量重复上轮已批准的修改。

## 覆盖与保留

| 范围 | 核查结果 |
| --- | --- |
| 开头与评价指标，L1–37 | MAE/RMSE/MAPE/R² 定义及说明顺序无明显中文语法错误；MAPE 采用比例值与 L43 的 0.00615=0.615% 一致，不擅加乘100。开头强度见R08。 |
| HI筛选，L39–46 | 表中 HI1 七节均最低、Fusion 平均第四、HI9/HI11 在 Cell7/8 排序反转均成立。“不能保证”不是绝对否定，保留。Fusion的比较基准可更明确，见R06。 |
| 初始化/收敛/超参数，L48–81 | 初始化性能“较为接近”未写统计等效；默认正态是选择理由，不是声称其精度最优；收敛结论已有“当前实验设置下”。两电池用途英文已澄清，保留。 |
| Oxford与CALCE/MIT，L83–113 | 表中最佳电池数与整体排名吻合。全曲线指标不能单独证明局部阶段误差，见R02。主比较包含配置电池的范围交主审跨章说明。 |
| 跨数据集，L115–140 | source-only/适应的数据角色分开，负R²没有掩盖，30%适应未被写成全面成功。R01为中文主语问题，R07为趋势范围可选澄清。 |
| 消融，L143–162 | 单模块并非处处改善、M4在MIT并列最低、SFull在四组最低均与显示数值相符。互补不是唯一因果证明；“与设计目标一致”保留。指标定义见R03。 |
| 复杂度，L164–末尾 | LSTM训练最短、MS-AgentNet最低三项及相对降幅与表值吻合。未把FLOPs低写成实测推理最快。精度与成本来自不同配置需防混读，见R04；表标题见R05。 |
| 关联表图 | 读取14个table_4*.tex（含未被当前章调用的table_4_2）和4个figure_4*.tex（含未调用的figure_4_1）。已调用结果图注未见新增语法错误；不把未调用文件误算成论文展示内容。 |

## R01｜确定中文语法问题；当前英文已修好，保留

位置：[中文第4章L137](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:137)、[英文L137](D:/MS-AgentNet-English/chapters/chapter04.tex:137)。

中文改前：

> 进一步比较相邻适配比例，CS2 和 CX2 源域从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。

中文最小建议：

> 进一步比较相邻适配比例，在分别以 CS2 和 CX2 为源域的设置下，适配比例从 30\% 增至 50\% 时，MAE 分别降低 0.0224 和 0.0221；从 50\% 增至 70\% 时，降幅分别缩小至 0.0114 和 0.0055。

当前英文（建议不改）：

> A comparison of adjacent adaptation ratios shows that increasing the ratio from 30\% to 50\% reduces MAE by 0.0224 and 0.0221 for the CS2 and CX2 source domains, respectively. Increasing it from 50\% to 70\% gives smaller reductions of 0.0114 and 0.0055.

原因：增加的是适配比例，不是源域本身。原句省略了真正主语；英文已明确 ratio，所以不能因为中文有病句，再把正常英文改一轮。不涉及研究主张或数字变更。三篇范文中本轮未定位与本适配比例协议直接对应的句子；这是本文表4-9与语法主语共同支持的修正，不能伪称范文原句。

## R02｜需确认：整体MAPE推至寿命后期，证据粒度发生跳转

位置：[中文L107](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:107)、[英文L107](D:/MS-AgentNet-English/chapters/chapter04.tex:107)、[表4-6](D:/MS-AgentNet-English/tables/table_4_6.tex:27)。

中文改前相关完整句：

> 值得注意的是，在具有阶段性转折和非线性衰减尾部的 CX2\_38 上，MS-AgentNet 的 MAPE 仅为 0.037673，较 CNN-Transformer 和 Transformer 分别降低了 59.75\% 和 51.80\%，表明模型在寿命后期加速衰减阶段仍能保持较低的预测误差。

当前英文末句：

> This shows that the model maintains low prediction errors during accelerated late-life degradation.

问题与分支：表4-6列的是电池整体评价指标，没有单列寿命后期区间。前段图形描述可以支持轨迹跟踪，但不能由这一个全程MAPE直接推出某局部阶段数值误差低。这不是证明模型尾段表现差，而是证据范围没有接好。

- 若仅有当前全程指标：数字句不变，末尾中文建议“表明模型在该电池上的整体预测误差较低。”对应英文：`This shows that the model has low overall prediction errors on this cell.` 原L105关于尾段轨迹的图形描述保留，不删除。
- 若作者确有尾段区间误差：先明确区间定义和结果，再给英文；不能把0.037673擅自改称尾段MAPE。

这涉及结论证据范围收窄，必须确认，不能标成不改原意的纯润色。

范文依据及限度：本轮重新读取 Engineering-AI L1379–1450。其L1393明确说 `As evidenced by the magnified regions of Fig. 11`（依据图11的局部放大区域），局部响应的讨论明确指向局部图；L1437–1440另报整体平均RMSE。可借鉴的是“局部讨论对应局部证据”，不能继承其中强机制归因，也不能将双栏TXT交错的段落当成连续论证。本文建议的主要依据仍是表4-6实际统计范围。

## R03｜需确认：综合平均误差及Reduction没有定义，正文与表格比较基准不同

位置：[中文L152–158](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:152)、[英文L152](D:/MS-AgentNet-English/chapters/chapter04.tex:152)、[表4-10表头L7](D:/MS-AgentNet-English/tables/table_4_10.tex:7)、[表4-11表头L7](D:/MS-AgentNet-English/tables/table_4_11.tex:7)。

改前：中文反复使用“综合平均误差”；英文使用 `combined average error`，表头为 `Average` 与 `Reduction`，没有运算定义/Reduction分母说明。

现有证据：CX2 M1的三个显示指标算术均值为(0.0170+0.0294+0.1035)/3≈0.0500，与Average一致；正文M2相对M1约1.20%，但M2行Reduction为54.40%，明显不是同一比较。后者很可能是M4相对M2的下降比例，而不是M2相对M1。表中MIT M1/M4同显0.0020仍列2.43%，也提示百分比可能来自未舍入数值。不能据显示精度直接判算错。

作者确认定义后，建议新增中文表注（条件式草案，不直接写入）：

> 综合平均误差为 MAE、RMSE 和 MAPE（比例形式）的算术平均值。Reduction 表示 M4 相对于该行模型的综合平均误差降幅，按（该行误差−M4误差）/该行误差计算；百分比基于未舍入结果。

对应英文条件式草案：

> Average is the arithmetic mean of MAE, RMSE, and MAPE expressed as a ratio. Reduction is the relative decrease in this average achieved by M4 compared with the model in that row. Percentages are calculated from unrounded results.

如实际采用加权平均/先跨电池后跨指标/不同舍入口径，必须按实际改写，不能采用上述猜测。补充定义不改变真实实验，但尚未确认的定义属于科学信息，不能当普通语法自动补入。正文M2对M1的比较有明确基准，保留，不为了与表列相同而改掉实验问题。

范文：本轮重读JESSOHRUL L3793–3808，范文逐项说明计量含义，其中 `floating-point operations required for a single forward pass` 把测量对象和范围写清。可借的是“先定义指标口径再比较”的做法；该段不能证明本文Average或Reduction应采用哪条公式。本项的直接依据是本文表头与数值，不是范文有同名列就足够。

## R04｜需确认：精度与开销来自不同配置，综合句可能被读成同一配置同时实现

位置：[中文L170](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:170)、[英文L170](D:/MS-AgentNet-English/chapters/chapter04.tex:170)，关联L79、L168和表4-4/4-12。

中文改前：

> 这些结果表明，MS-AgentNet 在保持较高 SOH 估计精度的同时，具有更低的前向计算量、参数量和权重存储开销。

现有英文：

> These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.

核实：主性能比较学习率0.001；复杂度测试0.01。表4-4 CNN-LSTM为3层、LSTM为5层；复杂度设置两者均4层。不同测试配置本身不构成错误，但表4-12不列此配置下精度，因此不能无条件读成“最低资源这一个精确配置同时取得前述全部精度”。

若作者是在综合两组不同目的实验，中文建议：

> 主性能比较显示 MS-AgentNet 具有较高的 SOH 估计精度；在本节统一复杂度测试设置下，其前向计算量、参数量和权重存储开销均低于四种基线模型。

对应英文：

> MS-AgentNet achieves high SOH estimation accuracy in the main performance comparisons. Under the common settings used for the complexity test, it has lower forward-pass computation, parameter count, and weight storage overhead than the four baseline models.

效果：保留两类积极结果，明确各自来自哪里；不是新增实验或承诺同配置精度。如果实际已有相同配置下精度结果，可保留原意并补具体依据。此项关系到结论范围，须作者确认。前句“LSTM刻画复杂模式局限”也只能依据前面的预测结果，不应暗示最短训练时间导致精度低；目前although仅为权衡对比，不能自动判成因果错误。

范文：重新读取BMSFormer L1344–1351、1360–1365与JESSOHRUL L3793–3810：二者分别交代复杂度指标和比较配置。Engineering-AI L2455–2472也明确延迟测试的环境和输入尺寸。本轮不引用其“fair/identical”作为本文公平性证明，只参考把指标与实际测试条件绑定的写法。

## R05｜可选范围澄清：same configuration标题过宽，四头与四层不是同一结构参数

位置：[表4-12标题L3](D:/MS-AgentNet-English/tables/table_4_12.tex:3)，中文源表标题本来也是英文；正文[中文L168](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:168)。

改前：`Comprehensive performance of models under the same configuration.`

建议：`Model resource costs under the specified comparison settings.`

中文效果对照：“相同配置下模型的综合性能”→“指定比较设置下的模型资源开销”。原因：表中实际只有资源指标，并不包含精度；模型本身结构不同，n对两类模型含义也不同。正文已经诚实限定“在数值上保持一致”，这一句不判错、不建议擅改4层或4头。标题收窄是信息准确性改进，不改变任何配置值。

范文：JESSOHRUL L3796–3798分列training cost/hardware cost；BMSFormer L1345–1351说明训练、硬件成本及配置。可参考“成本指标＋设置”命名，不机械继承same/identical来宣称结构等价。

## R06｜可选范围澄清：Fusion“没有增益”缺少显式比较基准

位置：[中文L43](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:43)、[英文L43](D:/MS-AgentNet-English/chapters/chapter04.tex:43)。

中文改前：

> 当四项健康指标共同作为输入时，Fusion 的三项平均误差均排名第四，说明多类健康指标的直接组合没有形成进一步的性能增益。

中文建议：

> 当四项健康指标共同作为输入时，Fusion 的三项平均误差均排名第四，说明与单独使用 HI1 相比，直接组合这四项健康指标没有形成进一步的性能增益。

现英文：

> When all four HIs are used together, Fusion ranks fourth for all three average errors, showing that directly combining multiple types of HIs does not provide further performance gains.

建议英文：

> When all four HIs are used together, Fusion ranks fourth for all three average errors, showing that directly combining these four HIs does not improve performance over using HI1 alone.

原因：Fusion优于DTV平均结果，并不是对所有单指标都没有收益。根据前句正在讨论HI1，最自然解释原本就是相对HI1；因此这不是原结论必错，只是把隐含基准写明。若作者意指所有多特征融合策略普遍无效，需收窄主张而不只是改连接词。

范文：JESSOHRUL L1946–1962本轮重新读取，L1956–1959明确定义四项共同输入为Fusion，并将结果限定为 `each selected HI using the proposed model`。可参考其具体输入方案/模型绑定；不能借其Fusion结果替代本文表中排序。

## R07｜可选范围限定：“持续改善”应理解为已测试比例，不外推无限加数据

位置：[中文L137](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:137)、[英文L137](D:/MS-AgentNet-English/chapters/chapter04.tex:137)。

中文改前：`结果表明，增加目标域观测能够持续改善模型在 Oxford 数据域上的适配性能`。

中文可选建议：`结果表明，在所测试的适配比例下，增加目标域观测能够持续改善模型在 Oxford 数据域上的适配性能`。

现英文：`These results show that adding target-domain observations continuously improves adaptation performance on Oxford.`

建议英文：`These results show that adding target-domain observations improves adaptation performance on Oxford across the tested adaptation ratios.`

原因：四档结果确实全部改善，故“持续”不直接判错；加范围可防读成对任意比例的普遍保证。没有改动70%时CX2源域R²仍为负的限制。三篇本轮未定位同适配比例实验的直接句型，依据是本文表4-9离散测试范围，不能硬套范文。

## R08｜中文强度偏大，现英文已弱化，不再机械修改

位置：[中文L1](D:/MS-AgentNet-English/source-zh/chapters/chapter04.tex:1)、[英文L1](D:/MS-AgentNet-English/chapters/chapter04.tex:1)。

中文改前：`综合上述多维度实验结果，可全面验证所提 MS-AgentNet 模型在电池 SOH 估计任务中的有效性与适用性。`

中文可选建议：`综合上述实验结果，可从所考察的方面评价所提 MS-AgentNet 模型在电池 SOH 估计任务中的有效性与适用性。`

现英文：`Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.`

处理：英文已用evaluation而不是完全证实所有适用场景；comprehensive此处可理解为列出的多维度覆盖，不必过度改动。如果作者希望中英文都明确限定，可将英文改为 `Together, these experiments evaluate the effectiveness and applicability of MS-AgentNet for battery SOH estimation from the aspects considered here.` 但较现稿更重，默认保留当前英文。

原因：本研究已经公开跨Oxford迁移限制，不能把“全面验证”理解成各种场景都有效。该处主要是中文措辞提醒，不计入必要英文改动。如果采用建议，属于主张措辞力度的收窄，而不是纯语法修正，需作者确认。无须用范文可能更强的demonstrate等自证词作为改强理由。

## 本轮范文读取记录与边界

- Engineering-AI/full.txt：L1288–1332（校准、阈值、末期损失）、L1376–1450（Oxford与跨域轨迹讨论）、L2334–2355（FLOPs/延迟对象）、L2455–2472（硬件测试设置）。
- JESSOHRUL/full.txt：L1940–1985（HI与Fusion对比完整目标及操作段，结果段出现双栏交错，不拼接作引证）、L3780–3832（复杂度指标及完整配置段）。
- BMSFormer/full.txt：L1330–1394（复杂度小节目标、指标和训练设置；页间错序不作为写作推进范例）。
- 本轮没有研究范文句间顺序或报告新的逐句计数；Engineering-AI TXT明显含双栏错序，只采用内部连续、语义完整的短引及独立段落，不拼接错序文本建立论证。需要完整段落顺序时应回PDF，本报告没有声称已做该PDF重排检查。
- 范文提供表达/定义方式参照，不证明本文技术结论。R01、R03、R07没有直接等同的范文方法，已明确标注；不能为了“最好有范文依据”而捏造来源。

## 待作者确认的最小清单

1. R02的0.037673是全程还是尾段指标？若全程，建议让该数只支持整体误差，将尾段观察留在图形段。
2. R03综合平均误差具体公式、Reduction分母及舍入规则是什么？确认后加定义表注。
3. R04资源表配置是否另有配套精度结果？若没有，按两类实验分别归属表述，不暗示同一配置共同获得所有指标。

R01仅说明中文已发现真实主语问题且英文已解决；R05–R07可由主审决定是否采纳；R08默认保留英文。所有条目都保留自然段边界，建议中的句级调整不构成段落拆并。
