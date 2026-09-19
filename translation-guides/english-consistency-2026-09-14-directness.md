# 英文一致性专项：简单句式与直接表达

日期：2026-09-14。范围：完整通读当前 `chapters/abstract.tex` 及 `chapter01.tex`—`chapter05.tex`，专项检查主干、名词化表达、指代、修饰层次和自然表达。时态及术语由其他分项交叉核对。本报告不修改正文。

结论：本分项未确认新增必须修改的硬性语法问题；有 2 处可选的最小简化。它们是对作者“简单词、简单句式”的进一步适配，不应将原句追认成错误。不能用本分项结论代表统计与实现疑点已解决。

## D01：将抽象名词短语改为明确动作（可选）

位置：`chapters/chapter01.tex:27`，方法比较后的 HI 稳定性讨论。

中文原句：

> 在健康指标方面，不同电池在材料体系和运行条件上存在差异，所选指标能否在不同电池间保持稳定的退化表征能力仍需进一步关注。

现有英文：

> For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention.

建议英文：

> Given differences in battery materials and operating conditions, further attention is needed to how consistently the selected HIs represent degradation across cells.

简短原因：属于“词汇基本简单，但表达较绕”。`mean that the stability of their degradation representations` 包含解释引导和抽象名词叠加。改为 `how consistently ... represent degradation`，直接说明“指标能否稳定表征退化”。`selected` 对应中文“所选”，不是新加筛选条件；仍只提出需要关注，不升级为已确认的跨电池失效。保留材料、工况、跨电池范围及原段位置。

本批范文尺度校准：

- JESSOHRUL，`full.txt:1773–1796`（§3.5.2）：完整的跨电池相关性例子及条件差异讨论，先说明同一 HI 在另一电池上相关性可能减弱，再说明不同化学体系和温度下的适用性问题。其中 `an HI that performs well in one setting may not be suitable in another` 用 HI 作明确主语。本文借鉴其对象明确的表达方式，不引入其阈值、性能差异或更强的不适用结论。
- Engineering-AI，`full.txt:170–181`（§2.2.1）：完整的原始数据与几何特征条目说明固定电压窗口未必适应不同化学体系。范文也使用概括性措辞，不逐一补充每类工况。因此本文无需新增工况例子，仅简化句法。
- BMSFormer，`full.txt:162–174`（引言挑战列表的前两项）：也使用 `representational capabilities` 等抽象名词概括特征和模型限制。这说明原句的抽象表达并非不规范，也不能仅凭更直接的范文句子强制改写。本文问题只是此处名词嵌套可以更顺，不是术语本身错误。

判定：范文既有直接陈述，也有抽象概括；本文上下文足够明确，故列为可选，不列硬性错误。

## D02：模块命名解释减少修饰层次（可选）

位置：`chapters/chapter03.tex:1`，模型名称解释。

中文原句：

> 其命名中的“MS”源于由小核DSConv-S与大核DSConv-L构成的多尺度卷积设计，用于高效提取不同时间尺度的退化特征。

现有英文：

> The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales.

建议英文：

> MS refers to the multi-scale convolutional design: small-kernel DSConv-S and large-kernel DSConv-L efficiently extract degradation features over different time scales.

简短原因：原句 `design comprising ... , which ...` 先修饰设计的组成，再回到设计的作用。改为冒号后的明确主语，按“MS 的含义—两个模块—提取什么”推进，保留小核/大核、两模块名称、高效及不同时间尺度全部信息。不是禁止 `comprising` 或 `which`，也不是要求全篇套用冒号句。

本批范文尺度校准：

- Engineering-AI，`full.txt:34–47`（完整摘要）：`SL-AgentNet (integrating Small-kernel and Large-kernel convolutions)` 直接说明名称所涉及的两类卷积，随后陈述架构作用。可参考其明确交代组成的方式；不能照搬单智能体机制、硬件验证或摘要的强结果措辞。§4.1 的命名句在 TXT 中跨表格/栏分散，未把其拼接顺序作为本条句法证据。
- BMSFormer，`full.txt:731–744`（§3.1 架构开头完整说明）：既使用较长的目的引导，也使用 `The output ... is transposed, passed ...` 直接交代对象和处理。范文并不要求全部短句；本文只降低名称解释这一句的修饰层次。
- JESSOHRUL，`full.txt:610–623`（架构说明完整段落）：`These embedded features ...` 和后续模块作用的关系从句，表明 `which` 从句在对应架构语境中完全正常。原句没有必须修复的 `which` 语法错误；建议只是让作用主体更显眼。

判定：范文也有长修饰和关系从句，原句可理解；按本轮简单句式偏好列为可选，不列必须修改。

## 明确保留，不将正常科研表达当作问题

- 摘要 `many existing ... often rely`：`many` 限定方法范围，`often` 限定发生频率；虽可斟酌删词，不能直接判为语法重复或强制去掉一个。本轮不正式提出改动。
- 方法中的被动式 `is defined as`、`is calculated as`、`are fed into`：对象和步骤清楚，范文方法也采用；不为追求美式英语机械全部改主动。
- 第 3 章数据流中连续使用 `first`、`then`、`Next`、`Finally`：有真实操作顺序，不是应删除的空泛衔接。
- 长句中的条件、数值、比较对象和对应关系：不为句长目标删减。结果段的 `respectively` 在多模型多数值对应中有必要，保留。
- `depthwise separable convolution`、`representational capability`、`computational complexity`：属于当前术语体系，不因词长而替换为不准确的简单词。
- 已自然的 `The result is added ...`、`The outputs ... are then concatenated ...`、`Stage R2 searches this region ...`：主语或指代可由紧邻上下文确定，保留。

以上判断基于本批重读的对应上下文；未把三篇范文当作统一的美式英语语法规范，也未声称范文全文不存在其他写法。仅可选建议，须作者确认后才能写入论文。
