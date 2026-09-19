# 摘要与第4/5章限定词、比较对象和比例补充审查

2026-09-14；只写审查记录，不改论文。本轮先重新读取当前摘要及第4/5章中英全文，再核对表格和历史记录。结论：**本轮没有新增可确认的译义强弱、量词范围或百分比/百分点错误。** 这不表示旧待核事项已经解决，也不保证全文绝对无误。

## 覆盖与结果

位置均为当前chapters及source-zh/chapters同名文件的行号；第4章44个正文段落、摘要1个正文段落、第5章3个正文段落均已阅读。重点检查only/all/both/most/best以及中文仅、所有、各、均、始终、最低、最优、显著；同时检查overall、potential、may、a degree of等限制。英文第4章按词边界检索only 8、all 24、both 7、best 3；only计数包括source-only，不能视为8项排他性主张。目标英文无most/significant/significantly；摘要和结论没有上述英文量词。判断基于整句对象，不以关键词数量决定正确性。

|位置|实际限定和对照|判断|
|---|---|---|
|摘要1；第5章3|better overall performance对应总体综合表现；结论保留a degree of in-domain cross-cell generalization及potential|没有改成每项指标、每节电池或已完成部署均最优；保留|
|4/7、9|all evaluation samples对应全部评价样本；中文MAPE“可能显著放大”译may become much larger|这里显著是数学量级描述，译文未添统计显著性；保留|
|4/41–45|all three scores为Cell1筛出的HI4/9/11；all four HIs为Fusion；all seven cells比较的是五种HI输入|不是宣称所有候选HI或所有预测模型均最优；表4-hi-input对应|
|4/63、65|三初始化范围、every training run reaches threshold、both收敛速度和后期波动|范围对应表4-3及初始化表；训练重复单位旧待核，没有新增译义差异|
|4/94、105|all models track总体容量衰减，随后明确局部误差差异|没有将总体跟踪改成局部均精确；Cell4对象歧义为旧项|
|4/96|四指标最优只给Cell2/3/5/6；Cell4只给R²和RMSE；all four metrics另限定为七池平均|表4-5吻合，不包含Cell7/8逐项最优|
|4/107、109|五节电池四指标最优；六节平均四指标第一；only 0.037673对应“仅为”|表4-6的b3c13由Transformer最优，已被五节范围排除；尾段推论的旧校准结论不变|
|4/117、119|source-only只在源域训练；only target testing限定本节迁移实验；both同/跨化学体系、all transfer directions两项固定HI|不把实验内角色强行扩大为该电池在全文唯一角色；保留|
|4/123、125|六方向三误差均下降；四个涉及Oxford方向R²仍负；两个CALCE方向转移结果另列|表4-7/8逐行对应；“较好表征趋势”不因单看一个指标重新升级|
|4/135、137|both source settings、all four ratios、相同适配比例CS2更好|表4-9四点对应；continuous的旧可选判断不变；中文“源域从30%增至50%”旧主语错误仍在|
|4/149、152、154|M1 only backbone；M4 both modules；单模块并非四数据集均改善；完整模型最低或并列最低综合平均误差|表4-10对应；明确CS2的M3单项MAE例外，未说四指标全优|
|4/156、158|only尺度变化；both两个尺度；best single-scale限S5/S31；SFull四数据集综合平均最低|表4-11对应；不把S0纳入“single-scale”对比；held fixed不升级旧可选项|
|4/166–170|all metrics同一环境；all models相应设置；all three values为FLOPs/参数/存储|没有包含训练时间；文中先承认LSTM用时最短。表4-12吻合|
|4/172|all four tested widths已明确16/32/64/128，最低存储只限这四点|不是所有可能宽度；保留既有图核对结果|

## 数值与百分比口径

相对下降按(基线−本文)/基线计算；适配比例的from/to是比例端点；MAE绝对差值未被写成百分比。

- 4/43：0.00615 = 0.615%，中英一致。
- 4/107：CX2_38的MAPE 0.037673相对0.093595与0.078160下降59.75%和51.80%，对应CNN-Transformer、Transformer。
- 5/3：CX2两节MAPE均值为(0.013328+0.037673)/2；CNN-Transformer为(0.014209+0.093595)/2；相对下降52.691%，对应52.69%。这是平均MAPE的相对下降，不是下降52.69个百分点。
- 4/125：六方向MAE相对下降依表次序为45.91%、87.61%、21.91%、86.84%、13.27%、31.21%，与按域对分组的区间一致。
- 4/137：30%→50%的MAE差为0.0224/0.0221，50%→70%为0.0114/0.0055；文中没有把比例端点差20个百分点写成“增加20%”。中文变化主体错误仍沿用旧项，英文已正确。
- 4/158：CX2 0.0442→0.0348为21.27%；MIT 0.0026→0.0025为3.85%；相对最佳单尺度CX2 0.0348→0.0225为35.34%，MIT 0.0025→0.0020为20.00%。
- 4/170：FLOPs相对LSTM下降50.5%；参数/存储相对CNN-Transformer下降25.6%/25.8%，相对CNN-LSTM下降70.8%/59.8%，均对应当前表4-12。

**精度界限，不作为新错误：** 表4-5的正文降幅可由已舍入Average行复算；例如(0.00537−0.00524)/0.00537=2.42%。从逐池已舍入数值再平均，得到约2.32%，不是同一舍入路径。表4-6亦有末位舍入路径差别。不能只据显示位数反推原始计算错误。表4-10的54.94%/16.52%及Average/Reduction实际计算和未舍入数值仍属旧待核，未新增统计要求或擅改结果。

## 本轮三范文尺度校准

本轮重新读三篇abstract.txt的摘要完整段落，并重读Engineering-AI results.txt:233–331、BMSFormer results.txt:999–1029（另读1030后的相邻配置段）、JESSOHRUL results.txt:44–120的相应结果语境。此前本次持续审查已通过PDF核对EAI第13页、BMS第12页、JES第15页双栏位置，本轮不把TXT跨栏先后当成论证顺序。未新增跨句推进判断。

|比较功能|范文是否也概括/省略及定位|同条件与裁定|
|---|---|---|
|总体表现与局部例外|Engineering-AI PDF13页§5.3先写“all models capture the general linear decay trend”（results:258），随后分局部下降/平滑退化讨论；BMSFormer PDF12页§4.3.2用“generally closer”（1003–1005）后接局部放大及平均降幅|均为整体轨迹和局部差异并列；本文没有all局部最佳主张，保留，无须每次量词重列例外|
|平均降幅及比较模型|BMSFormer PDF12页§4.3.2/results:1009–1013完整列average MAE/MAPE/RMSE及四比较模型；Engineering-AI PDF13页§5.3.2/results:248–251给平均误差与相对Transformer的降幅|功能同为数值比较，协议/数值不同；本文已给均值对象、指标及基线，不因摘要/结论未重列所有单池数字要求增细|
|HI输入排名|JESSOHRUL PDF15页§4.1/results:76–98明确四HI/Fusion、单输入与平均排名|同为HI输入比较，HI名单和名次不同；本文all four/all seven明确，不把输入方案和预测模型混为一谈|
|摘要概括|三篇PDF第1页摘要均在实验对象后概括性能；EAI还报告硬件验证，BMS概括accuracy/computation/stability，JES概括跨数据集表现|本文无硬件实测，保留potential而不复制EAI部署力度；总体表述有明细结果支撑，未发现必须改成更细枚举的语言原因|

由于没有新的确定问题，本轮不为凑数提供改前改后。旧中文主语、Cell4对象、实际统计口径等按既有记录处理；已校准为保留/可选的省略不重新升级。本报告是一次窄范围复核，不替代作者对原始实验记录的确认。
