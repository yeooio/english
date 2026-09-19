# 方法段落：三篇范文句级复核

2026-09-13，自动翻译批次。以下是三个明确选定的完整功能段落，不是三篇全文统计。PDF双栏顺序已通过 p.4 / p.13 / p.7 页面图复核；仅修复跨行连字符及数学字符转写。句子手工切分，Fig.和小数不作句界。词数按空白分词，引用标记剔除，独立数学符号不计；连字符连接词计一个词。句数不作为本文配额。

## BMSFormer

位置：p. 4, §2.1, step (2), from 'The constant current' to 'corresponding subset.'

S1: The constant current charge and discharge times for each cycle are extracted as health indicators (HIs).

S2: Starting from the selected segments, the HI search process is refined using progressively smaller windows and steps until a 0.01V window is reached or no higher Pearson correlation coefficient (PCC) value is found.

S3: A sliding window is then used to divide the time series of HIs into subsets, moving forward one step at a time.

S4: The true SOH at the next step of each window serves as the label for its corresponding subset.

| 句号 | 功能 | 词数 | 主语 | 时态/语态 | 衔接 |
| --- | --- | --- | --- | --- | --- |
| S1 | 方法 | 16 | The ... times | 一般现在时，被动 | 起始定义 |
| S2 | 方法 | 33 | the HI search process | 一般现在时，被动 | Starting from；until |
| S3 | 方法 | 22 | A sliding window | 一般现在时，被动 | then |
| S4 | 方法 | 18 | The true SOH | 一般现在时，主动 | 由窗口过渡到标签 |

共4句、89词；句长16/33/22/18词，最短16、最长33、平均22.3词。方法4/4句（100.0%）、89/89词（100.0%）；结果0/4句、0/89词。

## JESSOHRUL

位置：p. 13, §3.5.2 first complete paragraph, from 'The extraction of HIs' to 'given as follows:'

S1: The extraction of HIs is a crucial step in the SOH estimation of lithium-ion batteries [60–62], as the quality of the extracted indicators directly determines the precise of the final SOH estimation.

S2: The Pearson (γ) correlation coefficient (PCC) and the Spearman (ρ) correlation coefficient (SCC) are calculated to analyze the correlation between HIs and SOH.

S3: PCC measures the linear correlation, while SCC assesses the monotonic relationship between variables, making it more suitable for capturing nonlinear dependencies.

S4: The formulas for PCC and SCC are given as follows:

| 句号 | 功能 | 词数 | 主语 | 时态/语态 | 衔接 |
| --- | --- | --- | --- | --- | --- |
| S1 | 背景 | 31 | The extraction of HIs | 一般现在时，系表 | as 解释重要性；原文 precise 不沿用 |
| S2 | 方法 | 23 | The Pearson ... and the Spearman ... coefficient | 一般现在时，被动 | 从重要性转计算 |
| S3 | 定义 | 21 | PCC / SCC | 一般现在时，主动 | while 对比两统计量 |
| S4 | 过渡 | 10 | The formulas | 一般现在时，被动 | 引出公式 |

共4句、85词；句长31/23/21/10词，最短10、最长31、平均21.3词。方法1/4句（25.0%）、23/85词（27.1%）；结果0/4句、0/85词。

## Engineering-AI

位置：p. 7, §4.2 complete opening paragraph, from 'Standard convolutions' to 'Fig. 5.'

S1: Standard convolutions often suffer from parameter redundancy and may be prone to overfitting on small-sample battery datasets.

S2: To mitigate this, two specialized Depthwise Separable Convolution (DSConv) modules are designed.

S3: The kernel scales (k = 5, k = 31) were determined empirically to capture multi-scale degradation features, as visualized in Fig. 5.

| 句号 | 功能 | 词数 | 主语 | 时态/语态 | 衔接 |
| --- | --- | --- | --- | --- | --- |
| S1 | 问题 | 17 | Standard convolutions | 一般现在时，含 may | often / may 保留限制 |
| S2 | 方法 | 12 | two ... modules | 一般现在时，被动 | To mitigate this |
| S3 | 方法 | 20 | The kernel scales | 一般过去时，被动 | 具体参数与图链接 |

共3句、49词；句长17/12/20词，最短12、最长20、平均16.3词。方法2/3句（66.7%）、32/49词（65.3%）；结果0/3句、0/49词。

## 对本译文的实际作用

BMS的操作对象做主语、then连接窗口与标签，用于第2章流程和第3章数据流。JES区分PCC线性与SCC单调关系、先说明计算再引公式，用于HI章节；不继承其语法错误或阈值。EAI先说参数/样本问题再说明卷积设计，用于轻量化设计；不继承其硬件验证和机制自证。本文中文段落及信息顺序保持不变，没有强制照搬句数。

