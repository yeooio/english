# 本轮全文审查：三篇摘要的句级对照

2026-09-13。三篇摘要已回看首页PDF核对句界，范围仅从摘要首句至末句，不含关键词、引言或题名。句子编号以论文摘要顺序为准。全文审查意见见 whole-manuscript-review.md。

词数口径：清除PDF跨行软连字符，恢复被换行拆开的单词，按空白分词；连字符连接词算一个词，数字和括号缩写计词。原文State of-Health等既有写法不为计数改语法。EAI的Local–Global跨行合并后计一词。因此词数可能与期刊投稿系统的规则不同，不作为长度合规证明。

## BMSFormer

来源：style-references/BMSFormer/source.pdf p.1，配对 abstract.txt。精确范围：从“The efficient and accurate state-of-health (SOH) estimation”到“various hyperparameter combinations compared to alternative models.”。

| 句子 | 词数 | 功能 | 主语 | 主句时态/语态 | 衔接 |
| --- | --- | --- | --- | --- | --- |
| S1 | 24 | 背景 | SOH estimation | 现在/系表 | 提出需求 |
| S2 | 15 | 不足 | many ... approaches | 现在/主动 | However |
| S3 | 15 | 方法 | an efficient ... model | 现在/被动 | In this paper |
| S4 | 24 | 方法 | BMSFormer | 现在/主动 | 用模型名承接 |
| S5 | 24 | 方法 | two kinds ... convolution | 现在/被动 | Additionally |
| S6 | 20 | 验证范围 | Three ... datasets | 现在/被动 | 转向验证范围 |
| S7 | 25 | 结果 | The experiments results | 现在/主动 | 转向实验结果 |

共7句、147词，平均21.0词，句长范围15–25。方法3/7句（42.9%）、63/147词（42.9%）；结果1/7句（14.3%）、25/147词（17.0%）。

## JESSOHRUL

来源：style-references/JESSOHRUL/source.pdf p.1，配对 abstract.txt。精确范围：从“Accurate assessment of the State of-Health (SOH)”到“of SOH and RUL in lithium-ion batteries.”。

| 句子 | 词数 | 功能 | 主语 | 主句时态/语态 | 衔接 |
| --- | --- | --- | --- | --- | --- |
| S1 | 28 | 背景 | Accurate assessment | 现在/系表 | 提出需求 |
| S2 | 19 | 研究背景 | Recent studies | 现在完成/主动 | Recent studies |
| S3 | 18 | 不足 | many ... methods | 现在/主动 | However |
| S4 | 16 | 方法 | this paper | 现在/主动 | Therefore |
| S5 | 31 | 方法 | It | 现在/主动 | It承接框架 |
| S6 | 41 | 方法 | differential and integral methods / an ... algorithm | 现在/被动 | Furthermore / then |
| S7 | 38 | 验证范围/实验动作 | comparative experiments | 过去/被动 | Finally |
| S8 | 50 | 结果 | The experimental results | 现在/主动 | 转向结果 |

共8句、241词，平均30.1词，句长范围16–50。方法3/8句（37.5%）、88/241词（36.5%）；结果1/8句（12.5%）、50/241词（20.7%）。验证句独立列出，不重复计入方法。

## Engineering-AI

来源：style-references/Engineering-AI/source.pdf p.1，配对 abstract.txt。精确范围：从“To address the computational bottleneck of deep”到“0.3%, demonstrating its readiness for embedded deployment.”。

| 句子 | 词数 | 功能 | 主语 | 主句时态/语态 | 衔接 |
| --- | --- | --- | --- | --- | --- |
| S1 | 32 | 混合：问题/目标/框架 | this paper | 现在/主动 | To address |
| S2 | 19 | 方法 | a ... selection process | 现在/主动 | First |
| S3 | 21 | 方法 | we | 现在/主动 | Subsequently |
| S4 | 37 | 方法 | this AI model | 现在/主动 | By integrating |
| S5 | 40 | 结果 | Experiments | 现在/主动 | 转向数据集结果 |
| S6 | 42 | 结果/硬件验证 | the AI framework | 现在/主动 | With a model size |

共6句、191词，平均31.8词，句长范围19–42。明确方法3/6句（50.0%）、77/191词（40.3%）；结果2/6句（33.3%）、82/191词（42.9%）；首句混合功能单列1/6句、32/191词，不重复归入方法。

## 本文及审查决定

本文摘要9句、212词，句长28/21/9/23/8/40/33/22/28词，平均23.6词。背景S1，不足S2，框架/方法S3–S7，验证范围及实验动作S8，结果S9。方法5/9句（55.6%）、113/212词（53.3%）；结果1/9句（11.1%）、28/212词（13.2%）。这只是功能分布，不能据此要求增添数据或删除中文内容。

- 本文方法部分较突出，与研究同时涉及HI算法和轻量网络有关；不能仅为接近EAI的结果比例而添加中文摘要没有的量化结果。
- BMS多用模型或操作对象作主语，本文已有相应写法；其mainly integrates确实被复用，但不是不可改动的自然表达标准。
- JES的HI抽取—相关性筛选顺序可借鉴；其实验动作过去时、结果现在时说明本文We compared与results show并非必须统一成同一时态。
- EAI用First、Subsequently承接HI与模型设计，本文已有对应；其MCU验证、强结论与复杂缩写不应加入本文。
- 不复制BMS的The experiments results，也不继承EAI的proves或JES结果范围。本文普通show与必要限定继续保留。

这些结果不建立“达到母语水平”的数值阈值；单句长并不等于不自然，普通专业词重复也不自动构成问题。

