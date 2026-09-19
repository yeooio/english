# 第3章与模块专名一致性核查（2026-09-16，只读审查）

已阅读当前第3章全文、跨章相关出现、批准记录，并重新阅读 BMSFormer §3.1–3.3、Engineering-AI §4.1–4.3、JESSOHRUL §2.1–2.2 对应完整方法语境。已实际查看当前图3-1、3-2、3-3引用的三张PNG，而非依据历史图像记录推断。未修改正文或图。

## 确定需要统一：两个名称组

1. **Linear Local-Global Fusion Attention (LLGFA)**。
   - 当前规范名：chapters/chapter03.tex:1、9、189、271；chapters/chapter01.tex:46。
   - 活动旧名：tables/table_4_4.tex:12 `SLFA module`；figures/figure_3_3.tex:6 `proposed SLFA module`。
   - 图3-1实际图像 figures/01.png：主流程与右上核心结构中的 `SLFA`，以及 `SLFA features`。
   - 图3-3实际图像 figures/fig3_3_attention_comparison.png：(d) `Skim Local-Global Fusion Attention`。
   - 统一为 LLGFA / LLGFA features / Linear Local-Global Fusion Attention。
   - 作者已确认新名：translation-guides/module-name-pending-2026-09-15.md:3；approved-translations.md:29。上述图表属于明确留下的待同步项，不是新发现的正文翻译错误。
   - 范文校准：BMSFormer full.txt:214–217、1080附近使用 Local-Global Fusion Attention；Engineering-AI §4.3采用 AFF、FLFA 等不同模块；JESSOHRUL §2.1.2采用 DSCA。只能复用公共核心词，不能把本文名称换成任一范文的不同模块。
   - 第3章内部标签 eq:block_slfa、eq:slfa_fusion 不在排版正文显示，不算术语多版本。历史审校与冻结中文的 SLFA 也不算。
   - 图3-3还画出 DSConv-L 且没有当前正文所述完整局部支路，不能只把标题换成 LLGFA 就宣称整图同步完成。

2. **DSConv-L**。
   - 当前规范名：chapters/chapter03.tex:1、18、172、174；figures/figure_3_1.tex:4；figures/figure_3_2.tex:6；tables/table_4_4.tex:13。
   - 图3-1 figures/01.png 实际包含 `L-DSConv` 方块及 `(c) L-DSConv module`；统一为 DSConv-L。
   - 范文校准：BMSFormer full.txt:218–220、869–878 使用 DSConv-S / DSConv-L；Engineering-AI full.txt:855–899 使用 S-DSConv / L-DSConv；两者本身都是有来源的命名，但本文已经选择前者，不能跨图混用后者。JESSOHRUL §2.2用 DSConv / MBConv1，非本文大小核模块别名。

## 图内专业缩写的可选规范化，不作为另一套模型名错误

- 图3-1的 `depth-Conv` / `point-Conv` 与图3-2的 `DWConv` / `PWConv` 对应正文 `depthwise convolution` / `pointwise convolution`（chapter03:68）。可统一图内为 DWConv / PWConv，并在图注定义；正文全称不变。BMSFormer full.txt:790–817、JESSOHRUL:669–694、Engineering-AI §4.2均区分这两步。缩写形式本身不改变运算。
- 图3-1 `Embed layer` 与正文 `linear embedding layer` / 表4-4 `Embedding layer`：图中可改 `Embedding layer`，属于缩写风格统一，无需把 Embeddings（向量输出）也改成 layer（层）。
- 图3-1 `Gate` 不能直接当成作者已经实现的 gating mechanism；正文是 learnable scaling factor。此项需随图的数据流核对，不宜仅凭词语批量替换。

## 明确保留，避免误报

- MS-AgentNet / Multi-Scale Agent Network：全称与缩写，不是两个版本。不要借用 Engineering-AI 的 SL-AgentNet。
- ReLU² Agent Attention (RAA)、ReLU$^2$ Agent Attention、摘要/引言的小写 `ReLU² agent attention`：术语一致；正文形式不同在排版后相同，小写用法在 terminology.md:161 有明确批准。与标准 Agent Attention、linear attention、Softmax attention 是不同机制，不能强行统一。
- feedforward neural network (FFN)（chapter03:33）及图、表的 FFN：一致；JESSOHRUL full.txt:582–585 使用 feedforward neural networks / positionwise feedforward network。BMSFormer 的 MLP 和 Engineering-AI 的 PIAF-MLP 不是要求本文改名的依据。比较模型的 MLP 也不应批量替换为本文 FFN。
- feature embedding dimension（chapter03:7）、embedding dimension（110；chapter04:73、79；table_4_1:11、table_4_2:7）：同一 d 的全称与简写；Engineering-AI full.txt:819 已用 feature embedding dimension，JESSOHRUL:901用 embedding dimension。可定义后用短形式，无实质冲突。
- input feature dimension（chapter03:203）/ feature dimension of each head：在本节分别指输入 d 与每头 d_h，不能当作同一维度术语全部替换。
- representation or hidden dimension（chapter04:168、172）是跨模型概括；table_4_12:19 已区分 embedding dimension、MLP hidden-layer dimension、LSTM hidden-state dimension。范文 BMSFormer §4、JESSOHRUL §3的比较也区分 embedding / dense / hidden，不能把 LSTM 隐状态维度统一改叫 embedding dimension。
- linear readout（chapter03:5）/ readout layer（chapter04:117、132）：同一输出层的结构限定与名称；后者作者已批准（approved-translations.md:127起），不需改成范文另一结构的 MLP。
- layer normalization / LN / 图内 LayerNorm：全称与缩写一致；row normalization、Softmax normalization、LN0、min–max normalization各指不同操作，必须区分。

审查范围内无新增的高价值正文术语替换；优先完成上述两组已确定的图表名称同步。
