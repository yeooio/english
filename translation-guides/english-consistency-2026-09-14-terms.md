# 英文一致性专项：术语、专名与美式拼写（2026-09-14）

## 结论与范围

本专项未确认新的实质性术语错译、同一模块改名或英美拼写混用。**正式必改建议：0 项。** 这不是对全文全部句法和时态的零问题保证；那些由本轮其他专项复核。

本轮通读 `chapters/` 的摘要及第 1—5 章英文，读取术语表，核对图题、表题、表头及直接可编辑的模块/电池标签，并对相关概念回查冻结中文第 2—5 章及三篇范文 TXT 原始上下文。图像文件内的栅格标签不在此核验范围，不能把旧图标签问题称为已经消除。未修改正文、图表或术语表。

## 核对后应保留的表达

| 核对对象 | 现有英文与处理 | 本轮范文依据及是否同条件 | 简短中文原因 |
| --- | --- | --- | --- |
| 总算法与内部步骤 | 保留 `multi-source health indicator extraction and optimization algorithm`；内部仍分别用 `HI extraction`、`HI selection`、`screening procedure` | JESSOHRUL `full.txt` L1575–1593、L1671–1680、L1822–1833 分别处理提取、相关筛选及筛选过程。范文步骤与本文功能相近，但本文总算法还包含 MS-CCCT 标定，且总名有作者确认。 | 这些不是任意换同义词，所指层级不同。不能为了全篇“一致”把所有步骤强行改成总算法长名，也不能用 selection 取代整个算法。 |
| 卷积模块名 | 保留 `DSConv-S`、`DSConv-L`，不改为 `S-DSConv`、`L-DSConv` | BMSFormer `full.txt` L766–818 的完整模块说明与图题使用 DSConv-S/L；Engineering-AI L831–906 使用 S-DSConv/L-DSConv。两篇命名顺序确实不同。 | 本文已固定采用 BMSFormer 对应形式；机械同时模仿两篇反而会制造漂移。当前正文和直接 TEX 标签一致。 |
| 模型与注意力专名 | 保留 `Multi-Scale Agent Network (MS-AgentNet)`、`Slim Local-Global Fusion Attention (SLFA)`、`ReLU² Agent Attention (RAA)`；普通句中 `ReLU² agent attention` 不视为另一个术语 | BMSFormer L795–803 用正式模块名和缩写；Engineering-AI L889–917 区分其 AFF、AAT-1d 与 Agent Attention。本文专名来自冻结中文第 3 章及作者命名，不能换成范文的不同模块。 | 标题式大写、正文中的描述性小写，以及 `ReLU$^2$`/`ReLU²` 的排版写法不自动构成概念不一致。此处只确认术语，不替代实现或图内版本核查。 |
| HI 曲线及统计量 | 保留 `charging voltage--time (CVT)`、`incremental capacity (IC)`、`differential temperature--voltage (DTV)`、`differential temperature--capacity (DTC)`，以及 PCC/SCC | JESSOHRUL L1575–1593、L1632–1648、L1671–1680 的提取与相关定义对应上述对象；其中连字符、大小写随位置变化。本文中文第 2 章和 HI 表保持同一自变量及峰值/峰位区别。 | 不把引言引用文献中的 `differential thermal voltammetry` 强行替换成本文 DTV 全称；不同文献的命名需要按其对象保留。 |
| 资源指标 | 保留 `parameter count`、`trainable parameter count`、`weight storage size`，以及表头 `Parameters`、`Storage (KB)` | JESSOHRUL L3792–3823 的完整复杂度段分别说明 FLOPs、training time、trainable parameters、storage size；范文也用正文完整说明与表中短称的组合。本文第 4 章明确权重文件计量对象。 | 有上下文限定的短称不是术语错误；不要为一致将文件 storage 改成运行时 memory，也不要把 FLOPs 改成实际延迟。 |
| 数据集与编号 | 保留完整名 `MIT/Severson` 与后文可消歧的 `MIT`；保留 `CALCE CS2`/`CS2`、`CALCE CX2`/`CX2`；保留 Cell1–Cell8、CS2\_36 等原编号 | BMSFormer L414–440 的数据集段同样在全称与 CALCE 简称间切换；本文表 2-1 已完整列明四组来源，第 4 章相应分组清楚。MIT/Severson 并非范文同一数据集，缩写可用的依据是本文上下文，不冒称范文验证了它的来源。 | 简称在指向唯一时能减少重复，不需要每次恢复最长名字。电池编号与模型名字未发现本轮新增的文本漂移。 |
| 美式拼写及冠词 | 保留 `modeling`、`generalization`、`color`、`neighborhood`、`normalization`；保留 `an MS-AgentNet Block`、`an RAA branch`、`an SOH estimation framework` | JESSOHRUL L1671–1680 及 L3792–3823 使用美式常见词形与直接术语搭配；本文对照术语表明确的美式拼写要求。冠词按缩写读音判断，不因字母外形改成 a。 | 在本次检查的可编辑文本中，未发现 modelling/generalisation/colour 等混用。`Cut-off` 与 `cutoff` 属可选复合词样式；BMSFormer 的表 1 本身使用 Cut-off，当前不把它升级成美式语法错误。 |

## 缩写与“过度细节”的尺度

当前 MIT 充电协议中的 `SOC` 没有在该段补写全称，但上下文明确是充电状态百分比。BMSFormer `full.txt` L268–296 的完整流程段也直接使用 SOC，且该论文题名亦直接使用 SOC。本轮因此不把本文此处列为必须补充的错误，也不凭一个片段宣称范文全文从未定义 SOC。

`MLP` 在基线层配置表后已用表注解释为 multilayer perceptron；本文 MS-AgentNet 的 `FFN` 已在第 3 章定义。二者出现于不同模型的配置，不应仅凭缩写不同强行统一。

## 提交前复查

- 没有为了产生建议而重命名作者已确认的算法或模块。
- 没有把正常全称/简称、单复数或大小写变化算作术语漂移。
- 没有以“美式英语”为由删去技术限定或把长程依赖、长期趋势、局部变化合并成同一个概念。
- 本轮三篇依据来自重新读取的 `full.txt` 原始上下文；双栏文本中明确可读的名称和独立段落用于核对，不把跨栏相邻行拼成新的原句。
- 栅格图内文字、待核实验记录以及历史技术疑点仍保留其原有核验状态。
