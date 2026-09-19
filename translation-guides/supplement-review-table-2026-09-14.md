# 引言比较表补充核查：ref31、ref32和ref35

日期：2026-09-14。先读取当前中英表和BMSFormer实际方法，再检索旧记录去重；重新对照三篇范文相应功能语境。只写本报告，不修改论文。本次窄范围检查新增可确认问题为0项。

## ref31：Current ×、Voltage ✓、Temperature ×可以保留

位置：[中文表第12行](D:/MS-AgentNet-English/source-zh/tables/table_1_comparison.tex:12)、[英文表第12行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:12)。

中英现有对应单元均为：电流/Current ×；电压/Voltage ✓；温度/Temperature ×。建议：保留，不提供没有事实依据的改后勾叉。

本轮直接重读BMSFormer第3页§2.1完整步骤和第4—5页§2.3完整方法语境，定位为[full.txt269—299行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:269)、[441—459行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:441)以及[500—522行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:500)。其输入HI为恒流充、放电时间序列，窗口通过电压端点确定，正文确切短语为`constant current charge and discharge times`。筛选与建模描述没有把电流幅值或温度序列作为此HI的输入特征。

主动反驳：名称中出现constant current，是否因此必须把Current改成✓？不能。这里的“恒流”说明数据片段的运行条件，不等于电流幅值本身作为健康特征来源。识别运行阶段可能借助协议或记录，也不自动等同特征使用。相应地，Voltage ✓表示利用电压曲线确定时间区间，不能误读为模型直接吃入完整电压序列。表只列三类运行信号，时间未单列；这不证明作者声称不需要时间记录。

范文尺度校准：JESSOHRUL第4页Table 1的BMSFormer行也给出Current ×、Voltage ✓、Temperature ×，这一行及列对应已在上一轮直接查看原PDF核实；其第2页§1的[TXT128—138行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:128)也将该类方法表述为时间差、所选片段和电压窗口。Engineering-AI的[第2页§2.2.1，TXT161—180行](D:/MS-AgentNet-English/style-references/Engineering-AI/introduction.txt:161)将时间区间与电压积分列为几何特征，说明“数据类型/特征形式/运行条件”并非同一层次。因此现表在同类概括尺度下可以理解，不强求将表扩充到所有采样字段。

边界：这支持当前勾叉的合理性，不是对BMSFormer全部实现依赖作穷尽证明。若作者另行定义Source data considered为实验中采集过的全部字段，而非HI构建所用源信号，就应统一重定义全表；目前没有该定义的证据，不由审查者自行换表义。

## ref31：PCC（✓）不表示作者发明了PCC

位置同上，中文列名“健康指标选择方法（作者设计）”，英文列名“HI selection method (author-designed)”。现有单元为`PCC（✓）`／`PCC (✓)`。建议：保留。

BMSFormer§2.3实际先在电压区间内搜索，取各电池PCC最小值作baseline，再保留baseline最高的窗口并逐阶段细化。因此它既使用PCC，又确有作者构造的窗口选择过程。[full.txt447—457行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:447)所描述的是这一过程，而非宣称PCC统计量由该文创制。列标题已经限定为HI选择方法，✓合理指向选择过程。

反驳后结论：可以把标签写成“基于PCC的窗口搜索 / PCC-based window search”以更清楚地区分统计量和流程，但属于可选具体化，不是发现原标记错误。范文也如此：JESSOHRUL Table 1的BMSFormer行同样写`PCC (✓)`，见[TXT435—451行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:435)。Engineering-AI特征工程段也允许以核心统计准则概括筛选，不要求表格展开算法。没有理由要求本文颗粒度明显细于参照表，故本轮不新增这个可选标签建议。

## ref32与ref35：混合模型名称均有充分对应依据

| 位置 | 当前中英模型单元 | 结论 |
|---|---|---|
| [ref32，第13行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:13) | BiGRU-Transformer | 保留，两个核心组成齐全。 |
| [ref35，第17行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:17) | CNN-Transformer | 保留，两个核心组成齐全。 |

主来源核验：[ref32出版社摘要及模型节摘录](https://www.sciencedirect.com/science/article/pii/S0360544223027950)明确将其混合结构命名为`BiGRU-Transformer`；[ref35出版社摘要及引言](https://www.sciencedirect.com/science/article/pii/S0360544222023830)明确采用`CNN-Transformer`。本轮只用这些短名称和方法说明核对表项，没有继承原文关于优越性或首创性的宣传性表述。

三范文对照：BMSFormer第2页§1的[TXT104—116行](D:/MS-AgentNet-English/style-references/BMSFormer/introduction.txt:104)分别说明Jia的BiGRU/Transformer组合与Gu的CNN-Transformer；其[参考文献2465—2470行](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:2465)的DOI分别与本文ref32、ref35一致，未仅凭作者姓氏猜同篇。Engineering-AI第3页§2.2.2的[full.txt208—225行](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:208)也保留CNN-Transformer和BiGRU-Transformer两种标签。JESSOHRUL第2页§1的[TXT89—104行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:89)明确BiGRU与Transformer组合，而Table 1采用相同模型标签。

没有将ref35摘要中的PCA/缩放流程全部塞进模型名。它们属于数据预处理；模型名称正确不要求表内列出所有预处理步骤。同理，本次未重判ref32/ref35的原创性勾叉或所有数据来源勾叉，因为“原创”的分类口径和具体输入清单超出此次已核实证据；不能仅凭原文自称novel就自动改✓。

## 去重和结束判断

事后检索旧审查文件，相关命中多为原表快照、既有范文或方法讨论，未发现本次需要登记的新冲突。此前ref79滤波/回归对象与ref80漏Transformer仍由上一份报告处理，不在这里重新计数。

二次核查主动尝试了“恒流即使用电流输入”“PCC（✓）即宣称原创统计量”“混合模型名还应加所有预处理”三种反解释，均缺少足以推翻当前表义的证据，因此保留本次所查表项。结论仅覆盖ref31指定列与ref32/ref35模型名称，不能写成全表所有文献和勾叉已完成事实审计。
