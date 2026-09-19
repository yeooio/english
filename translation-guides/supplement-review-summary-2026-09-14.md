# 全文审查后的定向补查

日期：2026-09-14。接续全文终审，主审与三名agent再次检查可能遗漏的分类对象、否定与量词、比较范围和程度。先读取当前稿，再检索历史去重；本轮未修改论文。

## 新增一项分类澄清建议，不计为新的确定语法错误

位置：[英文比较表第11行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:11)及[冻结中文对应行](D:/MS-AgentNet-English/source-zh/tables/table_1_comparison.tex:11)，ref78（PINN）。

|项目|内容|
|---|---|
|中文现状|“健康指标选择方法（作者设计）”列中写PCC（×）。|
|英文现状|“HI selection method (author-designed)”列中写PCC (×)。|
|建议中文单元|固定16项特征；PCC相关性分析（×）。|
|建议英文单元|Fixed 16-feature set; PCC analysis (×).|
|改后效果|说明该文报告的输入集合与PCC用途，避免把相关性分析直接读成按PCC删选输入。|
|分类|可选的分类澄清；不是已证实的中文语法错误或英译遗漏，也不把“未见阈值”当成不存在筛选的证明。|

原论文的Feature extraction节说明提取16项特征并分析它们与SOH的PCC；SOH estimation节明确以这16项特征及循环数为输入。因此，现有证据支持“进行了PCC分析”，不足以把PCC具体表述为删除部分输入特征的步骤。[原论文](https://www.nature.com/articles/s41467-024-48779-z)，DOI：10.1038/s41467-024-48779-z。

主审实际取得PMC BioC全文并读取上述两节，文本保存在[原文提取记录](D:/MS-AgentNet-English/build/reference-learning/PINN-ref78-full.txt:59)。这份提取用于段落内容核对，公式排版不在此次检查范围。没有声称已经审计其补充材料与代码，也没有据此修改原创勾叉：建议中的×只是暂沿现表，不能视为本轮验证了其全部分类。

### 范文是否也如此，以及为什么仅列澄清

- **JESSOHRUL也如此。** 第4页Table 1把PINN行写成PCC（×），见[introduction.txt第435行起](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:435)；第2页引言则描述从电压、电流片段提取统计特征。其自身§3.5.2才明确区分相关性计算、准入和冗余剔除，本轮重读[methodology.txt第1317行起](D:/MS-AgentNet-English/style-references/JESSOHRUL/methodology.txt:1317)及1420—1528行对应语境。不能说范文不采用宽泛表头或简称。
- **BMSFormer有实际PCC窗口选择。** 重读§2.3完整语境，[methodology.txt第218行起](D:/MS-AgentNet-English/style-references/BMSFormer/methodology.txt:218)：以组内最低PCC评价并选择候选窗口，再逐步细化。它支持“PCC可用于选择”，但不证明所有使用PCC的文章都以它删选模型输入。
- **Engineering-AI明确把PCC用于窗口选择。** 重读§3.3.2至§3.3.3，[methodology.txt第140行起](D:/MS-AgentNet-English/style-references/Engineering-AI/methodology.txt:140)：候选窗的相关性用于确定并固定后续输入窗口。它与ref78的16项统计输入并非同一方法条件，不能拿它的详细流程要求ref78补写不存在的步骤。

主动反驳：HI selection在综述表中可以宽泛概括特征设计和相关性评价，范文也采用这种写法，因此仅凭列名不能断言原单元必错；即使最终保留全部16项，也不能逻辑上排除更早的特征设计曾参考相关性。本建议仅把已经能由原文确认的对象写得更明确。不要改成“该文没有任何特征选择”，也不要要求全表增加每篇的详细筛选流程。

另一名agent独立重读原论文后同意以上分级。若希望尽量保持单元宽度，也可保留PCC并加星号表注：中文“此处PCC用于特征与SOH的相关性分析；提取的16项特征全部作为模型输入。”英文“PCC was used for feature–SOH correlation analysis; all 16 extracted features were used as model inputs.” 两种方案择一即可，无须同时堆入表格。

## 本轮明确保留的项目

- BMSFormer数据列的Current ×、Voltage ✓、Temperature ×：恒流说明运行条件，不自动等于使用电流幅值作为HI来源。PCC（✓）可指作者设计的窗口选择流程，不意味着宣称发明PCC。
- ref32与ref35的BiGRU-Transformer、CNN-Transformer名称：与本轮取得的出版社方法说明对应；不必把全部数据预处理并入模型名。
- 第2—3章的否定、数量、条件与respectively：没有确认新的译义偏移。weights已经表达“加权”，不机械再加weighted；两组数值沿用同一电池顺序，不强求重复respectively。
- 摘要及第4—5章的总体比较、局部all/best、训练时间与资源最优对象：本轮没有确认新的范围错配。52.69%指MAPE的相对下降，不是下降52.69个百分点；舍入后的表值与均值末位差异不另计为语法错误。

## 报告与结束状态

- [表格指定条目补查](D:/MS-AgentNet-English/translation-guides/supplement-review-table-2026-09-14.md)。
- [方法量词与限定补查](D:/MS-AgentNet-English/translation-guides/supplement-review-methods-2026-09-14.md)。
- [摘要、结果与结论补查](D:/MS-AgentNet-English/translation-guides/supplement-review-results-2026-09-14.md)。

与上一轮相比，本轮新增的是上述分类澄清建议，没有新确认的中文语法错误或英文译义错误。上一轮两个已确认表项和此前未处理事项仍按[全文终审总报告](D:/MS-AgentNet-English/translation-guides/exhaustive-review-summary-2026-09-14.md)保留，不重复计数。42个已记录基线的论文TeX文件复核哈希均未改变；未修改冻结中文、正文、表格或图片。
