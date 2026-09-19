# 图7与Oxford协议核对 — 2026-09-13

仅整理，未改图、公式或协议。依据工作正文与冻结中文；没有核查实现代码，以下不代表代码结构已经确认。

## 图7(d)

已查看 figures/fig3_3_attention_comparison.png。依据 chapter03 的 eq:raa_qkv_scaling、eq:relu2_normalization、eq:raa_output、eq:slfa_fusion、eq:block_dsconv_l。

| 现图 | 正文定义及建议 |
| --- | --- |
| Skim | 应为 Slim |
| DSConv-L 接 K/V，Q绕过 | DSConv-S先生成X_S；RAA的Q/K/V均由X_S通道缩放生成；需重画路径，不能只改L为S |
| 输出Linear | 正文是多头Concat后逐通道乘s_o；标明Channel scaling，避免被理解为完整全连接投影 |
| ReLU² | 应明确ReLU² row normalization，即R_2，包含无正分数行的均匀回退 |
| 一条输出Add路径 | 正文有RAA内部残差和SLFA外部融合两层加法 |
| 无完整局部支路 | 需要LN(X_S)、RAA、Dropout、W_a及融合Add |

完整SLFA建议数据流：

    X -> DSConv-S -> X_S --+--> LN -----------------------+
                           +--> RAA -> Dropout -> × W_a ---+--> Add -> X_F

RAA内部：通道缩放与分头；两阶段智能体聚合/广播；Concat；输出通道缩放；加回输入X_S。两阶段得分按sqrt(d_h)缩放后做R_2；头内维度用d_h，智能体数统一n_a=2。

DSConv-L属于SLFA之后的Block步骤：X_F经LN、DSConv-L、W_l缩放后与X_F相加。

优先保持当前图题的完整SLFA含义，局部展开RAA；若只画RAA，需要同时确认图题和正文指图范围。注意力复杂度标签不应无说明地替代整个模块各项运算复杂度。

## Oxford

正文chapter02:29及冻结中文写CC-CV；表table_2_1的Oxford列写CC (2C)，冻结源表也如此。这是原稿冲突，不是翻译遗漏。

variance不能清楚命名放电协议。依照当前正文，建议Dynamic current profile (ARTEMIS)，尚未实施。

官方数据记录：[Oxford Battery Degradation Dataset 1](https://ora.ox.ac.uk/objects/uuid%3A03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac)。检索结果指向Readme.txt获取完整说明，但本次直接打开官方记录返回403，未读取官方README充电条款。因此尚未确认老化充电完整阶段与2C定义，不能将CC-CV (2C)当作已核实事实。

后续需读官方README/原始试验说明，区分老化循环与定期表征循环，再统一表文中的阶段、倍率和用途。三篇范文可提供表达习惯，不能代替实验协议证据。确认后修改工作稿并记录源稿勘误，source-zh保持冻结。

