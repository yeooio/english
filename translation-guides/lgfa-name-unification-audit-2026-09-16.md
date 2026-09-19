# LGFA 名称统一审查（2026-09-16）

## 实施状态与命名口径

- 作者已确认正式名称。摘要、第一章、第三章、表4-4、图3-3图注、完整中英对照英文块及术语表已经同步；三张位图按作者要求不修改。本轮未编译。
- 作者要求统一采用缩写 `LGFA`，并将论文标题中的方法概括写为 `local-global attention`。
- 按英文缩写对应关系，建议将正式模块专名统一为 **Local-Global Fusion Attention (LGFA)**。若正式全称写成 **Local-Global Attention**，通常对应缩写应为 `LGA`，不能自然推出 `LGFA`。
- 因此建议区分两类表达：
  - 正式模块专名：`Local-Global Fusion Attention (LGFA)`，后文简称 `LGFA`；
  - 论文标题及普通功能概括：`local-global attention`、`local-global feature fusion`、`local-global feature modeling` 等，按句子对象保留，不强行全部改成模块专名。
- BMSFormer 的对应完整语境明确使用 `Local-Global Fusion Attention (LGFA)`：`style-references/BMSFormer/full.txt:512, 738–739, 795, 827, 855, 862`。这支持正式专名与缩写的组合，但不等于照搬其结构或结论。

## 一、当前活动论文中需要统一的可见文字

按上述口径，活动 `.tex` 文件共有 **17 个可见位置**需要同步。

| 文件与位置 | 现有英文 | 建议英文 | 处理理由 |
| --- | --- | --- | --- |
| `chapters/abstract.tex:1` | `Linear Local-Global Fusion Attention module` | `Local-Global Fusion Attention (LGFA) module` | 摘要首次出现正式模块名；去掉不能纳入 `LGFA` 的 `Linear`，并定义缩写。若摘要后文不用缩写，也可不在摘要定义，最终排版时二选一固定。 |
| `chapters/chapter01.tex:46` | `Linear Local-Global Fusion Attention (LLGFA)` | `Local-Global Fusion Attention (LGFA)` | 正式全称与缩写同步。 |
| `chapters/chapter03.tex:1` | `Linear Local-Global Fusion Attention (LLGFA)` | `Local-Global Fusion Attention (LGFA)` | 第三章首次定义模块名。 |
| `chapters/chapter03.tex:9, 18, 104, 108, 174, 191, 269, 271, 367, 382` | `LLGFA` | `LGFA` | 同一模块的后续简称统一。 |
| `chapters/chapter03.tex:14` | `\operatorname{LLGFA}` | `\operatorname{LGFA}` | 公式中的读者可见算子名称也属于正式简称。 |
| `chapters/chapter03.tex:189` | `The proposed Linear Local-Global Fusion Attention module` | `The proposed Local-Global Fusion Attention module` | 小节标题采用完整正式名称。 |
| `tables/table_4_4.tex:12` | `SLFA module` | `LGFA module` | 消融表中的模块名称与正文统一。 |
| `figures/figure_3_3.tex:6` | `the proposed SLFA module` | `the proposed LGFA module` | 图注与正文统一。 |

说明：`chapter03.tex` 共涉及 13 个位置；加上摘要、第一章、表4-4和图3-3图注后，共17个可见位置。

## 二、需要修改的图内文字

图内文字不是由 LaTeX 图注自动生成，三张位图必须分别修改。合计 **7 个可见文字项**。

| 图片 | 当前可见名称 | 建议名称 | 数量与注意事项 |
| --- | --- | --- | --- |
| `figures/01.png` | `SLFA`；`SLFA features` | `LGFA`；`LGFA features` | `SLFA`两处、`SLFA features`一处，共3处。 |
| `figures/fig1.png` | `SLFA`；`SLFA features` | `LGFA`；`LGFA features` | 内嵌了一份独立的结构图副本，共3处；修改 `01.png` 不会自动更新本图。 |
| `figures/fig3_3_attention_comparison.png` | `Skim Local-Global Fusion Attention` | `Local-Global Fusion Attention (LGFA)` | 1处；保留旁边复杂度标注并另行核对。 |

`fig3_3_attention_comparison.png` 还存在 `DSConv-L` 与当前正文中 `DSConv-S + RAA` 数据路径不一致的问题。该问题属于结构内容核验，不能通过单纯改成 `LGFA` 解决，也不应在本次名称同步中反向改正文公式。

## 三、应保留、不需要强制改成 LGFA 的表达

1. `main.tex:4` 的标题应保留：
   `A linear-complexity deep learning network with local-global attention for efficient state-of-health estimation of lithium-ion batteries using optimized multi-source health indicators`
   
   这里的 `local-global attention` 是标题中的方法概括，不是首次定义完整模块专名；保持简洁且与作者给定标题一致。
2. `Local-global feature fusion`、`local-global feature modeling`、`joint local-global representation` 等表达描述操作、能力或表示，不是模块的正式名称，不应机械替换为 `LGFA`。
3. 第五章目前只概括该机制的功能，没有出现旧模块专名；无需为了增加简称而强行插入 `LGFA`。
4. `chapter03.tex` 内部标签 `eq:block_slfa`、`eq:slfa_fusion` 不会显示给读者，也没有形成可见术语冲突，建议保留，避免无意义的交叉引用键改动。
5. `source-zh/` 是冻结中文源稿，其中的 `SLFA` 保留，不修改。

## 四、正文修改后必须同步的活动辅助文档

### 4.1 完整中英对照

`translation-guides/full-manuscript-bilingual.md` 的英文块有 **14 个位置**需要同步：

- 第28行附近摘要英文：`local-global fusion attention module`同步为最终批准的摘要写法；
- 第352行：`Linear Local-Global Fusion Attention (LLGFA)`改为`Local-Global Fusion Attention (LGFA)`；
- 第1086行：`Slim Local-Global Fusion Attention (SLFA)`改为`Local-Global Fusion Attention (LGFA)`；
- 第1142、1156、1324、1352、1492、1548、1744、1758、2024、2038行：`SLFA`改为`LGFA`；
- 第1534行：`The proposed Slim Local-Global Fusion Attention module`改为`The proposed Local-Global Fusion Attention module`。

对应中文块继续保留冻结源稿中的 `SLFA`，不能用全文替换改动中文。

### 4.2 术语表与进度记录

- 在 `translation-guides/terminology.md` 中新增正式术语：`局部—全局融合注意力模块 | Local-Global Fusion Attention (LGFA)`，并把活动说明第165、168行的 `LLGFA` 更新为 `LGFA`。
- `translation-guides/progress.md:33` 是旧决定的历史实施记录，不静默改写；名称同步完成后追加一条新记录，说明 `LGFA` 取代此前的 `LLGFA/SLFA`。

## 五、历史记录的处理边界

`approved-translations.md`、`module-name-pending-2026-09-15.md`、`sentence-style-chapter03-2026-09-16.md` 以及带日期的旧审查、回译和实施报告，记录的是当时使用 `SLFA` 或 `LLGFA` 的审查状态。它们不属于当前投稿正文，不做全局替换；必要时仅追加“已被2026-09-16新命名决定取代”的说明，以保留决策轨迹。

## 审查与实施结论

作者已确认正式全称为 **Local-Global Fusion Attention (LGFA)**。实际实施范围为：

- 论文 `.tex` 可见文字：17处；
- 三张位图中的可见旧名称：7处，按作者要求暂不修改；
- 完整中英对照英文块：14处；
- 术语表中的正式条目与2处活动说明；
- 进度文档追加1条新决定记录。

标题中的 `local-global attention` 已保留；普通功能描述、内部LaTeX标签、冻结中文源稿和历史审查记录未进行机械替换。本轮没有编译或更新PDF。
