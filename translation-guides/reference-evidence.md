# Reference evidence

Status: three author-selected PDFs identified; the following short expressions and section references were located in extracted text and independently reviewed by one agent per paper on 2026-09-13. This is expression evidence, not a claim that every section boundary, PDF reading order, or experimental statement has been verified. Exact continuous paragraph order must still be checked against source.pdf.

Each entry must identify paper, page and section, a short checked excerpt, the terminology or expression pattern, relevant manuscript function, and any limits. Do not populate this file with invented examples or remembered paraphrases presented as quotes.

## Located expression evidence

引言P03分类段逐篇句级核对：[introduction-p03-reference-analysis.md](introduction-p03-reference-analysis.md)。

引言P02对应完整段落的句级核对：[introduction-p02-reference-analysis.md](introduction-p02-reference-analysis.md)。

引言P01逐篇首段句级分析（含PDF阅读顺序、句数、词数、主语、时态、衔接与方法/结果占比）：[introduction-p01-reference-analysis.md](introduction-p01-reference-analysis.md)。

Labels: 可用 = ordinary domain expression usable with matching meaning; 需适配 = use its function but adapt wording/objects to this manuscript. Quotations below are short original text fragments, not complete sentence templates.

| ID | Paper / section | Short original fragment | Function and decision |
| --- | --- | --- | --- |
| B1 | BMSFormer, Abstract p.1 | capture both long-term and short-term dependencies | 可用：表征目标；按本文统一术语指定长程与局部信息 |
| B2 | BMSFormer, Abstract p.1 | fuse multi-scale and multi-channel features | 可用：动作和宾语明确；不泛写性能更好 |
| B3 | BMSFormer, §2.3 | progressively smaller windows and steps | 需适配：窗口细化操作，具体规则用本文设置 |
| B4 | BMSFormer, §3.1 | embedded in a high-dimensional space | 可用：数据流中的嵌入步骤 |
| B5 | BMSFormer, §3.2 | depthwise filtering followed by pointwise combination | 可用：串行运算关系 |
| B6 | BMSFormer, §4.2.2 | a single forward pass | 可用：计量口径；不是训练累计计算量 |
| B7 | BMSFormer, §4.3.1 | across different hyperparameter combinations | 可用：稳定性范围，不能无对应实验照搬 |
| B8 | BMSFormer, §4.3.2 | sudden SOH changes | 可用：局部轨迹现象 |
| J1 | JESSOHRUL, Abstract p.1 | extract various health indicators | 可用：HI提取动作 |
| J2 | JESSOHRUL, §3.5.1 | derive four characteristic curves | 需适配：观测量到曲线；数量按本文 |
| J3 | JESSOHRUL, §3.5.1 | the voltage corresponding to the peak | 可用：峰位，区别于峰高 |
| J4 | JESSOHRUL, Table 4 | charge time within the voltage range | 需适配：优先写 charging time within [interval] |
| J5 | JESSOHRUL, §3.5.2 | ranked according to their correlation strength | 需适配：按本文明确的组级分数排名 |
| J6 | JESSOHRUL, §3.5.2 | fixed and directly applied | 需适配：范围由本文训练/配置及指标开发协议决定 |
| J7 | JESSOHRUL, §2.2.2 | expands the channel dimension by a factor of r | 可用：明确维度操作和倍数 |
| J8 | JESSOHRUL, §2.2.2 | processed sequentially through | 可用：真实串行模块顺序 |
| E1 | Engineering-AI, Abstract p.1 | identifies robust health indicators | 需适配：identify/select与extract分工 |
| E2 | Engineering-AI, §4.1 | capture long-range dependencies | 可用：依赖表征 |
| E3 | Engineering-AI, §4.2.2 | following the AFF feature fusion stage | 需适配：模块位置；使用本文模块名 |
| E4 | Engineering-AI, §4.3.1 | aggregates global information from | 可用：明确聚合来源 |
| E5 | Engineering-AI, §5.3.1 | abrupt SOH drops | 可用：确有突降时描述输出轨迹 |
| E6 | Engineering-AI, §5.4 | the amplitude and timing | 可用：幅度与时点，须有对应图像证据 |
| E7 | Engineering-AI, §5.4 | capacity regeneration | 需适配：与本文容量回升术语统一，不自行断言物理恢复 |
| E8 | Engineering-AI, §5.5.2 | increasing the RMSE from | 可用：消融结果；保留具体移除或替换操作 |

## Actual reference granularity versus our choice

- BMSFormer摘要无具体精度/模型规模数字；本文使用代表性精度与规模数字是本文选择。其§4.3.2集中罗列多项降低率，不能将“少报数字”声称为该范文一贯事实。
- JES摘要报告SOH与RUL两个结果界限；方法深入到通道系数、维度、HI定义及筛选阈值。本文继承可复现细节层级，不继承RUL任务或具体筛选阈值。
- EAI摘要包含降低率、存储和MCU验证；结果按突降、回升和后期加速退化讨论，并有较多辩护和机制归因。本文继承轨迹组织，按自身证据限制解释。

## Quality and boundary notes

- 拒绝继承：BMS 的 `The experiments results`；JES 的 `the precise of` 与 `performs not too bad`；按正常英语修正，不作为风格特征保存。
- 拒绝继承：EAI §5.2浅层结构自证、§5.6权衡合理性辩护；JES §3.5.2对数据完整性的反复自评。直接报告结构或协议即可。
- 待核实且不可迁移：JES §3.5.2正文/表5准入连接词不一致；§4.4.2参数量单位及时间比较存在可疑表述。范文事实不能作为本文数据或规则来源。
- 提取待核：按页抽取的TXT有相邻章节和双栏错序，尤其结论段与参考文献相邻。不得从TXT顺序推断连续段落推进。
# Additional verified batch evidence — 2026-09-13

See method-reference-analysis.md for three complete functional reference paragraphs, sentence counts, sentence lengths, subjects, tense and rhetorical roles, checked against the PDF reading order. See full-manuscript-bilingual.md for exact source/target blocks and short verified reference expressions. These analyses describe the selected passages, not whole-paper sentence counts or mandatory translation quotas.

## Fresh sentence study — 2026-09-14

See [reference-sentence-study-2026-09-14.md](D:/MS-AgentNet-English/translation-guides/reference-sentence-study-2026-09-14.md): three complete paragraphs, ten individually recorded sentences, verified against full PDF pages (BMSFormer p.6, Engineering-AI p.7, JESSOHRUL p.11). Records include exact boundaries, word-count rules, grammatical subjects, tense/voice, sentence progression, and separate mixed-function coverage. The linked Chinese review adds optional directness item C7 and unresolved repetition/degree-scope item C8; no manuscript changes.

## Full bilingual cross-review — 2026-09-14

See [exhaustive-review-summary-2026-09-14.md](D:/MS-AgentNet-English/translation-guides/exhaustive-review-summary-2026-09-14.md) and its three chapter reports for fresh contextual reference reading, PDF reading-order checks, retained expressions, and candidate rebuttals. Two new comparison-table issues were checked against the cited papers' publisher abstracts. Similar shorthand in JESSOHRUL was explicitly considered rather than treated as automatically correct. This review adds no new whole-paper sentence-count claim and makes no manuscript edits.

## Full-reference learning and redundancy review — 2026-09-14

See [reference-led-2026-09-14.md](D:/MS-AgentNet-English/translation-guides/reference-led-2026-09-14.md) and its three reference-specific reports. Each reference TXT was read to EOF by its assigned agent; complete selected PDF pages were checked visually. The three representative passages contain 6/5/4 sentences and 191/80/87 words, respectively, with reproducible counting rules, subjects, tense/voice, progression and separate mixed-function coverage. These are passage statistics, not whole-paper quotas. The review proposes two optional same-sentence redundancy reductions and one optional directness improvement; no manuscript changes.

## Grammar and directness review with two agents — 2026-09-14

See [grammar-reference-patterns-2026-09-14.md](D:/MS-AgentNet-English/translation-guides/grammar-reference-patterns-2026-09-14.md) for fresh measurements of the three complete abstracts (6/7/8 sentences; 191/147/241 words), checked against the original PDF first pages, with sentence functions, subjects, tense/voice and separately reported mixed functions. See [grammar-full-review-2026-09-14.md](D:/MS-AgentNet-English/translation-guides/grammar-full-review-2026-09-14.md) for seven complete prose suggestions and contextual terminology/tense decisions. Its two linked independent reports record further method-paragraph measurements and fresh reading of all English prose in the three results extracts. The author's latest scope excludes image labels and image/content issues. No manuscript changes were made.
