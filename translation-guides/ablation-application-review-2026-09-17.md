# 消融分析：术语与两层实验递进核对稿

2026-09-17｜只处理消融，复杂度正文及图保持不动｜中文审核稿，尚未改英文正文或表格

## 结论

Table 16比较多尺度DSConv与RAA的组合；Table 17比较保留RAA时DSConv-S/L的配置。后者不能称作只改变核尺度。术语采用JE的应用表达，机制位置依据本文。M1按作者最新答复不展开逐层清单。

## 术语候选（不覆盖既有正式术语表）

|中文|候选英文|来源及边界|
|---|---|---|
|模块消融分析|module ablation analysis|现稿标题，保留|
|细粒度局部退化信息|fine-grained local degradation information|本文对象适配；JE有fine-grained local degradation patterns及fine-grained degradation dynamics|
|局部退化动态|local degradation dynamics|仅实际描述变化时使用，不作为上一词的轮换|
|互补作用|complementary effect / complementary roles|JE §4.4.1；根据效应/分工区别使用，不增添正式协同效应检验|
|跨循环上下文建模|cross-cycle context modeling|本文应用限定，非JE原文专名；不全篇替换global context modeling|
|注意力前局部增强|pre-attention local enhancement|Engineering-AI §5.5.2有确切对应|
|融合后特征细化|post-fusion feature refinement|Engineering-AI的post-fusion refinement加feature明确对象|
|完整配置|full configuration|现稿已有，保留|
|综合平均误差|combined average error|现稿已有；表中Average需定义|
|更一致的综合表现|more consistent overall performance|只指所比较数据集上的指标表现，不等于多随机种子方差更小|

不另立inter-cycle degradation relationships等同义名词链；local enhancement, cross-cycle context modeling, and post-fusion feature refinement可用作总收口。避免progressive feature-processing process这类重复名词结构。

## 八处改动位置与前后效果

### 1. 第4节总导语：只替换消融介绍

位置：[chapter04.tex:1](D:/MS-AgentNet-English/chapters/chapter04.tex:1)。

当前英文：

```tex
This section systematically evaluates MS-AgentNet on four public battery datasets. The experiments cover HI effectiveness, model performance comparisons, module ablation and complexity analysis, and cross-domain adaptation. The HI experiments examine whether the selected features can represent battery degradation patterns and thus provide suitable model inputs. The model comparisons assess estimation accuracy and stability across cells. Ablation studies and complexity analysis quantify the contributions of core modules and evaluate computational efficiency. Finally, cross-dataset transfer experiments further examine the model's ability to adapt to differences between data domains. Together, these experiments provide a comprehensive evaluation of the effectiveness and applicability of MS-AgentNet for battery SOH estimation.
```

建议中文/表注：

消融实验考察多尺度DSConv与RAA的独立作用及互补关系，并进一步比较DSConv-S与DSConv-L的不同保留组合。

修改效果与限定：原句将消融与复杂度合写；仅将消融任务细化，复杂度评价计算效率的介绍继续保留。

### 2. §4.6 总导语：接回前述退化现象

位置：[chapter04.tex:145](D:/MS-AgentNet-English/chapters/chapter04.tex:145)。

当前英文：

```tex
Ablation studies and complexity analysis are conducted in addition to the main comparison experiments to further evaluate the effectiveness and efficiency of MS-AgentNet. The ablation studies examine the effects of individual modules on prediction performance by removing or combining key modules, while the complexity analysis evaluates computational cost, parameter count, and storage size.
```

建议中文/表注：

前述SOH估计结果显示，所考察电池具有平滑衰减、局部变化、阶段性转折和寿命后期加速衰减等退化特征。为进一步考察不同模块对估计性能的贡献，消融实验分别比较多尺度DSConv与RAA的独立作用及组合效果，并分析DSConv-S与DSConv-L在注意力交互前后处理特征的互补关系。

修改效果与限定：接回应用场景，但不加入“整体比较不能说明为什么”等长篇自证。该段中原有复杂度分析的评价对象句仍保留。

### 3. §4.6.1 动机：应用对象

位置：[chapter04.tex:149](D:/MS-AgentNet-English/chapters/chapter04.tex:149)。

当前英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref71}. To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

建议中文/表注：

为兼顾退化信息表征与计算效率，MS-AgentNet采用多尺度DSConv提取健康指标序列中的细粒度局部退化信息，并利用RAA建立输入窗口内的跨循环上下文联系。

修改效果与限定：仅替换To preserve local information...这一句，前面的高效注意力和普通卷积说明保留。

### 4. M1–M4 定义：按JE颗粒度说明变体差异

位置：[chapter04.tex:149](D:/MS-AgentNet-English/chapters/chapter04.tex:149)。

当前英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref71}. To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

建议中文/表注：

设置M1–M4四种变体，以比较两类模块的独立作用与组合效果。M1为不含多尺度DSConv和RAA的基础变体；M2在M1基础上加入多尺度DSConv，M3加入RAA，M4同时保留两类模块。

修改效果与限定：按作者最新意见，不补嵌入、LN、FFN及残差清单，也不推断是否使用替代操作。JE说明其backbone保留线性注意力；只能借介绍尺度，不能将JE骨干换入本文。

### 5. Table 16 表注

位置：[Table 16源文件](D:/MS-AgentNet-English/tables/table_4_10.tex)。当前无表注。

建议中文/表注：

Average denotes the arithmetic mean of MAE, RMSE, and MAPE; Reduction denotes the relative decrease in Average achieved by M4 with respect to the corresponding variant.

修改效果与限定：建议定义Average和Reduction，保留现有全部数值。不加“由未四舍五入数值计算”，因缺少计算文件。中文：Average表示三项误差的算术平均，Reduction表示M4相较相应变体的Average相对降幅。

### 6. Table 16 结果：单模块→组合→例外

位置：[chapter04.tex:152](D:/MS-AgentNet-English/chapters/chapter04.tex:152)。

当前英文：

```tex
As shown in \cref{tab:4-10}, neither module provides a uniform benefit when used alone. Compared with the basic model M1, adding multi-scale DSConv in M2 reduces all three error metrics on CX2 and Oxford, with the combined average error decreasing by approximately 1.20\% and 8.45\%, respectively. However, M2 increases MAE, RMSE, and MAPE on CS2 and MIT. Adding RAA in M3 produces broader improvements, reducing the combined average error by approximately 3.18\%, 11.60\%, and 15.49\% on CS2, CX2, and Oxford, respectively, but all three errors increase on MIT. These results indicate that the effects of the individual modules depend on the data domain rather than being uniformly positive across all datasets.
```

当前下一段：

```tex
When multi-scale DSConv and RAA are integrated, the full model M4 achieves the lowest or jointly lowest combined average error on all four datasets. The interaction is most evident on CX2. Relative to M1, the isolated reductions produced by M2 and M3 are 0.0006 and 0.0058, whereas their joint integration reduces the error by 0.0275, from 0.0500 to 0.0225. This result provides quantitative evidence that multi-scale local feature extraction and cross-position information interactions complement each other on CX2, where the capacity trajectory contains stage transitions and a nonlinear degradation tail. This pattern is less pronounced on the other datasets: M3 has a slightly lower MAE than M4 on CS2, and M4 only matches the combined average error of M1 on MIT at the reported precision. The main benefit of the full configuration is therefore its more consistent performance across datasets, rather than a uniform improvement from either module in isolation.
```

建议中文/表注：

表16显示，单独加入某一类模块并未在四个数据集上产生一致的误差改善。相较M1，多尺度DSConv使M2在CX2和Oxford上的综合平均误差分别降低约1.20%和8.45%，但在CS2和MIT上三项误差均增大。RAA使M3在CS2、CX2和Oxford上的综合平均误差分别降低约3.18%、11.60%和15.49%，但在MIT上三项误差均增大。这说明两类模块单独使用时的收益随数据集而变化。

共同使用多尺度DSConv与RAA后，M4在四个数据集上取得最低或并列最低的综合平均误差。CX2上的组合收益最为明显：M4将该误差由M1的0.0500降至0.0225，表16报告的降幅为54.94%；相较表现更好的单模块变体M3，降幅仍为49.05%。这一比较支持局部退化信息提取与跨循环上下文建模的互补作用，也与前述CX2_38阶段性转折和非线性衰减尾部的现象形成应用上的联系：DSConv补充相邻循环的局部退化信息，RAA将这些表示与输入窗口内的循环间上下文结合。不过，CS2上M3的MAE略低于M4，MIT上M1与M4的综合平均误差在当前精度下均为0.0020，Oxford上M4相对M3的进一步降幅仅为1.52%。因此，完整配置的优势主要体现为跨数据集更一致的综合表现，而非每个模块在每项指标上均带来提升。

修改效果与限定：保留反例；54.94/49.05/1.52直接作为表中报告值，不谎称由当前四位小数重新算出。应用解释不推断特定尾部区间的误差下降。

### 7. Table 17 实验定义、标题与表头

位置：[chapter04.tex:156](D:/MS-AgentNet-English/chapters/chapter04.tex:156)。

当前英文：

```tex
To further distinguish the roles of the two convolutional scales, all variants retain RAA, while only the convolutional scale is changed. Four variants are considered: S0 (RAA only), S5 (RAA with DSConv-S of kernel size 5), S31 (RAA with DSConv-L of kernel size 31), and SFull (RAA, DSConv-S, and DSConv-L). S0 and SFull correspond to M3 and M4 in \cref{tab:4-10}, respectively.
```

建议中文/表注：

上述比较显示了多尺度DSConv与RAA共同使用的收益。为进一步考察注意力前局部增强与融合后特征细化的作用，在保留RAA的条件下，调整DSConv-S与DSConv-L的保留组合。设置S0、S5、S31和SFull四种变体：S0不保留两类卷积模块，S5保留DSConv-S，S31保留DSConv-L，SFull同时保留两者。其中，S0和SFull分别对应表16中的M3和M4。

修改效果与限定：替代only the convolutional scale is changed。表名建议Effects of DSConv-S and DSConv-L configurations.；K=5/K=31列改DSConv-S/DSConv-L，数值及标记不变。两模块差异包含位置、核长、通道扩展，不是纯核长控制实验。

### 8. Table 17 结果及消融收束

位置：[chapter04.tex:158](D:/MS-AgentNet-English/chapters/chapter04.tex:158)。

当前英文：

```tex
\Cref{tab:4-11} further shows that the effective convolutional scale varies with the degradation patterns in each dataset. S5 gives a small improvement over S0 only on MIT, while increasing the error on CS2, CX2, and Oxford. S31 reduces the combined average error on CX2 from 0.0442 to 0.0348, but it still does not outperform S0 on CS2 or Oxford. A single scale is therefore not a uniform enhancement across datasets. When the two scales are combined, SFull achieves the lowest combined average error on all four datasets and further reduces the error by 35.34\% on CX2 and 20.00\% on MIT relative to the best single-scale variant. These results support the ability of the dual-scale configuration to cover a broader range of temporal patterns and suggest that it may reduce the need to select a different convolutional scale when the same architecture is applied to different battery data. The present ablation does not, however, establish a unique correspondence between either kernel and a specific physical degradation mechanism.
```

建议中文/表注：

表17显示，仅保留一种卷积模块时的收益随数据集而变化。相较S0，S5仅在MIT上降低了综合平均误差，由0.0026降至0.0025，降幅约3.85%；在CS2、CX2和Oxford上均未取得更低误差。S31在CX2上降低了MAE、RMSE和MAPE，综合平均误差由0.0442降至0.0348，降幅约21.27%，但在CS2和Oxford上仍未优于S0。因此，仅保留注意力前的局部增强或融合后的特征细化，均未在四个数据集上取得一致优势。

同时保留DSConv-S与DSConv-L后，SFull在四个数据集上取得最低的综合平均误差。CX2上的误差进一步降至0.0225，相较S31降低约35.34%；MIT上相较最佳单卷积配置S5降低约20.00%。结合前述CX2_38的阶段性转折与非线性衰减现象，这些比较支持在不同处理阶段引入卷积特征的设计：DSConv-S在RAA之前提取相邻循环的细粒度局部退化信息，使跨循环上下文聚合基于局部增强表示进行；DSConv-L则进一步细化局部—全局融合后的序列表示。不过，CS2和Oxford上SFull相较S0的改善较小，组合收益的幅度仍随数据集变化。

综合两组消融结果，预测误差的比较支持局部增强、跨循环上下文建模与融合后特征细化的配合作用。三者在不同处理阶段共同形成面向SOH估计的退化表征，但这些结果尚不能建立某一卷积核与特定物理退化机制之间的一一对应关系。

修改效果与限定：三段完成单模块比较、组合与应用解释、整体收束。CX2数字只集中报告一次，保留小收益场景。不写“复杂退化使单阶段不够”或“已证明结构必要性”。

## 数值复核

- Table 17：3.85%、21.27%、35.34%、20.00%可由所显示Average值计算，正文采用“约”。
- Table 16：CX2的0.0500→0.0225按显示值计算为55.00%，表内Reduction为54.94%。不改表值，不声称已查明其原始精度算法。M4相对M3的49.05%也按表内报告值引用。
- 两表Average与三项误差算术平均在显示精度允许的范围内相容；精确计算过程未在现有项目中找到。新增表注定义采用材料给出的含义，不附加“使用未四舍五入数值”声明。
- MIT上M1与M4均显示0.0020，但Reduction仍报告2.43%；分析注明“在当前精度下”并列，不能据此声称原始值完全相同。

## 范文核对与结构边界

[JE消融原文](D:/MS-AgentNet-English/style-references/JESSOHRUL/results.txt:1628)按变体→组合结果→退化信息解释收束，fine-grained degradation dynamics和complementary effects可借用。它对模型作用的因果措辞不能直接当作本文的实验证据。

[Engineering-AI卷积消融](D:/MS-AgentNet-English/style-references/Engineering-AI/results.txt:954)明确pre-attention local enhancement与post-fusion refinement，但其采用标准卷积替换，本文采用保留/移除配置，不能将其数值或过拟合解释迁入。

BMSFormer仅作此前局部全局和卷积结构的术语参照；本轮未找到与两层配置消融完全同构的段落，不宣称三篇实验设计相同。

单模块和完整配置的比较支持组合在已报告误差指标上的表现，不能隔离位置、核大小、扩展倍率、参数量各自的因果贡献；正文保留一句物理机理边界即可，不堆砌限制。

状态：仅整理审核稿。未修改章节、表格、图、正式术语表或冻结中文。复杂度暂不处理。