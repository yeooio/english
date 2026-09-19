# 第三轮查漏：第3章数学、数据流与架构图

日期：2026-09-14。只新增本报告，不修改正文、公式或图片。

## 结论与覆盖

完整复读中英第3章以及前两轮methods、第二轮intro-cross报告，逐式核对维度、运算顺序、残差对象、非负归一化与复杂度。进一步直接查看正文实际引用的三张栅格图 `01.png`、`02.png`、`fig3_3_attention_comparison.png`，而非只读图注。提交前追加完整读取9月13日 `whole-manuscript-review.md`，完成更早历史记录去重。

**历史未闭环事项再确认：架构图与当前文字/公式的运算边界未充分对齐。** 9月13日报告C1/C2已记录图3-3、图3-2的核心冲突及Skim拼写，不能再次算作新发现。本轮在同一主题下补充图3-1的Gate/SLFA展开边界及图3-2通道标签位置，下分三个定位点，不计作多个独立算法错误。这不是中文翻译错误，也不能据此断言代码错误。未发现值得另外列为确定错误的全新公式问题。

## T-M01：架构图与当前公式版本／模块边界待对齐（历史C1/C2复核，并补图3-1定位）

### A．图3-2的DSConv模块边界

位置：[图源02.png](D:/MS-AgentNet-English/figures/02.png)、[现英文第3章L148](D:/MS-AgentNet-English/chapters/chapter03.tex:148)、[L174](D:/MS-AgentNet-English/chapters/chapter03.tex:174)，中文同位置。

中文改前：

> 最后，输出经逆转置恢复至原始排列，并与输入通过残差连接融合：

> DSConv-L置于SLFA之后，采用三倍通道扩展和$1\times31$深度卷积，从融合表示中提取较长时间尺度的退化特征。两层$1\times1$逐点卷积分别完成通道扩展与恢复，整体变换顺序与DSConv-S一致；其残差连接在MS-AgentNet Block层完成，如式\eqref{eq:block_dsconv_l}所示。

现英文：

> Finally, the output is transposed back to its original arrangement and combined with the input through a residual connection:

> DSConv-L follows SLFA and uses a channel expansion factor of three and a $1\times31$ depthwise convolution to extract degradation features over longer time scales from the fused representation. Two $1\times1$ pointwise convolutions expand and restore the channel dimension, respectively, following the same transformation order as DSConv-S. Its residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}.

图中改前：图(c)、(d)均在第二个 `1 × 1 PWConv` 后另列 `Linear`；图(d)标作 `DSConv-L` 且自身画了旁路与 `Add`。扩展后的 `2C_out channels`、`3C_out channels` 标签位于第一个PWConv下方，而正文是经过该PWConv后扩展。图上前后箭头均向上。

问题及原因：正文DSConv-S的第二PW后只有逆转置和相加，没有额外可学习Linear；DSConv-L明确将残差放在Block级。若图(d)只是把Block级连接一起画入模块示意，并不代表代码多加一次，但图题没有区分这两个层级。Linear也可能被作者用作无激活的线性瓶颈标记，不应直接断言实现多了一层。通道标签则易被读为输入已扩展。

条件改后效果（若当前正文与公式确为最终实现）：

- 图(c)改为 `Transpose → PW expansion → DW5 → ReLU → PW restoration → Inverse transpose → Add with X`；不再以独立算子框表示未定义的Linear。若Linear只是强调PW输出无激活，改作该PW的注释，不画作额外层。
- 图(d)明确模块只含三倍扩展、DW31、ReLU、通道恢复及对应转置；Block级的缩放与残差放在Block图，或虚线框并注释其属于Block级，不画成模块自身另有残差。
- `2d/3d` 或经作者确认的 `2C_out/3C_out` 标签移到首PW的输出连线上；维度记号与旧M06一并核定。

中文正文建议：上述原句保留，不为迁就旧图改成双残差。

英文正文建议：上述原句保留。若图(d)有意保留Block级旁路，可在图注增加条件说明：

> 图(d)中的旁路表示Block级残差连接，而非DSConv-L模块内部的另一条残差连接。

> The bypass in panel (d) denotes the Block-level residual connection, not an additional residual connection within DSConv-L.

此说明仅当作者确认图的意图且图中缩放/归一化边界亦能解释清楚时适用。不能只补注释而留下彼此矛盾的算子。

### B．图3-3(d)与SLFA定义

位置：[图源](D:/MS-AgentNet-English/figures/fig3_3_attention_comparison.png)、[中文第3章L271](D:/MS-AgentNet-English/source-zh/chapters/chapter03.tex:271)、[英文同位置](D:/MS-AgentNet-English/chapters/chapter03.tex:271)，以及L106、L351、L367和slfa_fusion公式。

中文改前：

> 该模块采用局部分支与RAA分支的融合形式：DSConv-S首先提取局部表示，RAA随后以该表示为输入完成跨位置特征交互，两个分支的输出经加法融合。

现英文：

> The module fuses a local branch with an RAA branch: DSConv-S first extracts a local representation, and RAA then uses this representation to establish cross-position feature interactions. The outputs of the two branches are fused by addition.

正文另明确Q、K、V都由X_S构造，RAA末端采用输出通道缩放s_o，而SLFA输出为LN(X_S)+W_a Dropout(RAA(X_S))。

图中改前：图(d)下方模块标为 `DSConv-L`，位于K/V一侧，Q单独进入广播路径；RAA乘法输出之上另有 `Linear` 和 `Add`。图(d)标题与图注明确把它称为所提SLFA，但没有将当前局部LN分支、W_a和Dropout的融合层级表达清楚。

另有一处可直接确认的图内拼写问题：图(d)底部实际写为 `Skim Local-Global Fusion Attention`，正文术语为 `Slim Local-Global Fusion Attention`。改前→改后：`Skim` → `Slim`；中文名称和技术含义不变。这不是需要范文裁定的词汇偏好，直接依据本文已确认全称；与上述结构核实合并记录，不另计一个算法问题。

原因：这里不只是“S/L一个字母”。卷积位于全部QKV之前，还是只接K/V，是不同的数据流；RAA的输入残差与SLFA的局部分支相加也是不同层级。若图是抽象注意力内核图，可省略某些外层算子，但应标清其边界，不能用完整SLFA的标题让读者推断完整计算。

条件改后（若正文公式代表最终结构）：图(d)以X为起点，先画 `DSConv-S → X_S`，再分为 `LN(X_S)` 和 `RAA(X_S)` 两支；Q/K/V均源于X_S；RAA内输出标记 `Channel scaling s_o`，残差与X_S相加；RAA输出经Dropout及W_a，再与LN(X_S)相加。也可主图仅画两支、另用嵌入图展开RAA，避免把两次相加画成一个。

中文改后效果：**先提取局部表示，再从该表示进行全部QKV交互，最后按公式融合**。

英文图内核心候选标签：`DSConv-S`、`Channel scaling s_o`、`Local branch: LN(X_S)`、`RAA branch: W_a Dropout(RAA(X_S))`。

正文中英原句保留；此处应优先核实并更新图，而不是把正确对应公式的文字改成图中旧路径。若实际代码采用图中路径，则需作者明确选定技术版本；不是可直接批准的语言替换。

### C．图3-1的SLFA框与外部融合层级

位置：[图源01.png](D:/MS-AgentNet-English/figures/01.png)，第3章block_slfa、slfa_fusion公式。

中文改前：

> 输入$\mathbf X_l$经SLFA模块处理。SLFA利用DSConv-S提取局部特征，并通过ReLU$^2$智能体注意力（ReLU$^2$ Agent Attention，RAA）建立跨位置全局信息交互：

现英文：

> The input $\mathbf X_l$ is processed by SLFA, which uses DSConv-S to extract local features and ReLU$^2$ Agent Attention (RAA) to establish global information interactions across positions:

图中改前：图(a)蓝色 `SLFA` 框之后继续排列 `Add`、`Gate`、`Dropout`、`W_a`及加法结点，并有LayerNorm旁路。当前公式的SLFA自身已经包含局部LN旁路、Dropout和W_a，正文亦没有定义独立Gate算子。

原因：可能这些方框是在展开SLFA内部运算，而不是在完整SLFA之后再做一次；现图边界却容易让读者按串联重复理解。不能据此认定模型重复残差或确实使用了未说明门控。

条件改后效果：若此图意在展开SLFA内部，使用一个总外框注明 `SLFA`，将内部算子按slfa_fusion归属其中；若蓝框是完整SLFA，则外面不再重复画其内部融合。`Gate` 若只是W_a的示意，合并为同一缩放标签；若是另一算子，必须先核实定义和公式，不默认为已有设计。

中文/英文正文原句保留；可用中英图内说明“SLFA内部展开 / Expanded SLFA structure”明确层级，但须先确保内部节点确与当前公式对应。

## 范文依据及其限度

本轮重新读取 Engineering-AI TXT L815–853、L851–933，BMSFormer L671–826，JESSOHRUL L1658–1687。双栏穿插不拼作连续论证，只用可独立定位的短句。

- [Engineering-AI L845–849](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:845)将转置、卷积和外部残差明确写入同一公式；[L822–826](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:822)明确残差所取阶段输出。支持“图、公式、残差来源应相互对应”的写法，不支持把它的残差来源照抄给本文。
- [BMSFormer L735–769](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:735)按窗口、embedding、Block、输出交代架构，并给局部模块公式；只能借鉴模块边界与数据流说明，不证明本文图里的Gate或Linear存在。
- JESSOHRUL这次所读HI统计片段没有直接架构图依据，明确不引用它证明上述改图。

这些发现的直接证据是**本文实际图像与本文当前公式的交叉核对**，不是范文相似度。没有把范文的原图结构当作本文实现的正确答案。

## 旧项复核、未新增问题

- M02继续按第二轮降级为可选中文主语澄清；现英文The result无问题。
- M05/M06仍是原成本条件/一二维记号问题；本轮图3-2使其维度歧义更直观，但不再次计数。
- 一般非负归一化零分母是旧M07；RAA已给均匀回退，不能重复给RAA报错或擅加epsilon。
- 低秩上界限定于Phi_q Phi_k，未扩展到整个含残差模型；保留。
- RAA平方归一化正比例不变及权重比描述，与公式一致；不由该性质推断必然精度提高。
- “线性注意力以较低计算复杂度”承接上句固定d_h时关于N的复杂度，现上下文能理解为渐近阶比较。虽然不能推出任意短窗口实际运算更少，本轮不另列错误，不新增硬性N>d_h条件，也不以大O直接断言实际运行快慢。
- 正文DSConv-S明确ReLU，DSConv-L说同变换顺序，图中ReLU并无已查明冲突；不猜测应为GELU。
- 图中Gate、Linear只能标为未对齐/未定义，不推出实际代码参数遗漏或原结果无效。图3-1的箭头拥挤也不自动等于数据泄漏。

本轮没有核验训练实现，也没有修改、重新生成图片。三图可疑节点必须先由作者确定最终结构再统一图文。
