# 英文全文语言一致性专项复核

日期：2026-09-14。按作者本轮要求检查简单词、直接句式、清楚结构、美式英语、上下文时态与语态，以及术语和专名一致性。只提建议，不修改正文。

## 结论

三位 agent 按时态语态、术语与美式拼写、句子直接性分工，各自先通读当前摘要及第1—5章。主审通读英文，复核候选的中文原意，并重读三篇范文相关语境。

- 未确认新的、需要强制修正的时态或语态不一致。
- 未确认可编辑正文及直接图表 TEX 中新的实质性术语错译、专名漂移或英美拼写混用。
- 保留 **2项可选的直接性改善**，不是2个确定的语法错误；均不改技术含义、论证次序、限定或段落划分。

此前“未发现新的充分修改理由”的结论不是零错误保证。本轮针对作者新强调的简单句式重新检查，以下可选句式不是对旧技术疑点的重新定级。

## 1. 引言：减少抽象名词叠加（可选）

位置：`chapters/chapter01.tex:27`。

中文原句：

> 在健康指标方面，不同电池在材料体系和运行条件上存在差异，所选指标能否在不同电池间保持稳定的退化表征能力仍需进一步关注。

现有英文：

> For health indicators, differences in battery materials and operating conditions mean that the stability of their degradation representations across cells requires further attention.

建议英文：

> Given differences in battery materials and operating conditions, further attention is needed to how consistently the selected HIs represent degradation across cells.

简短中文原因：这是“词汇不难，但表达较绕”的可选改善。原句通过 `differences ... mean that the stability of their degradation representations ...` 层层推进；建议直接落到“所选HI能否稳定地表征退化”。`selected` 对应中文“所选”，不是新增筛选条件；`requires further attention` 的力度保留，不改成已经证明不稳定。现在时不变。

范文依据与尺度：JESSOHRUL `full.txt` L1835–1849直接以所选HI为对象，说明跨电池表现及能否表征群体退化模式；BMSFormer L169–183也采用 representational capabilities、performance stability 等抽象名词，说明抽象名词本身不是错误。本文可借前者“指标—表征什么”的直接关系，但不搬入其具体相关数值或效果结论。三范文对应范围及补充比较见直接性分报告。建议是本文语境适配，不声称范文存在整句相同模板。

## 2. 模型命名：直接说明组成与作用（可选）

位置：`chapters/chapter03.tex:1`。

中文原句：

> 其命名中的“MS”源于由小核DSConv-S与大核DSConv-L构成的多尺度卷积设计，用于高效提取不同时间尺度的退化特征。

现有英文：

> The name MS refers to the multi-scale convolutional design comprising small-kernel DSConv-S and large-kernel DSConv-L, which efficiently extracts degradation features over different time scales.

建议英文：

> MS refers to the multi-scale convolutional design: small-kernel DSConv-S and large-kernel DSConv-L efficiently extract degradation features over different time scales.

简短中文原因：去掉 `comprising ... , which ...` 的长修饰链，冒号后直接说两个模块做什么。MS含义、小核/大核配对、高效提取及不同时间尺度全部保留；专名不改。`extracts → extract` 是主语从单数design变成两个模块后的正常主谓一致调整，不是原句时态错误。原句which可以指design，不能称其原本一定存在指代错误。

范文依据与尺度：Engineering-AI摘要 `full.txt` L34–41将小核/大核组成与多尺度特征作用相连，支持相同说明功能；不把其SL改成本稿MS的词源依据，本文命名以中文为准。BMSFormer L735–744及JESSOHRUL L610–623也使用包含关系和关系从句描述模块，说明原句并非违反范文规范。建议仅将本文的一处组成/作用关系说得更直接，并不是要求全面禁用which或comprising。未凭跨栏提取拼接Engineering-AI的完整命名句。

## 应保留的时态、语态与术语

|检查项|本轮判断及理由|
|---|---|
|摘要 `We compared ... The experimental results show ...`|保留。前者报告已完成比较，后者说明当前呈现的结果。JESSOHRUL完整摘要L33–50也以过去时实验接现在时结果，不是时态混乱。|
|第4章 `is used / is trained / are measured`|保留。目前以现在时说明实验流程，内部一致。BMSFormer L1078–1105、L1387–1390和JESSOHRUL L1201–1226也如此；Engineering-AI偏用过去时不构成全文必须改过去时的理由。|
|数据集 `were charged` 与 `contains / are included`|保留。分别指历史老化操作、数据内容和本文采用范围。|
|方法中主动与被动交替|保留。模块做什么时用主动，输入怎样处理时用被动；只要对象、主语和先后顺序清楚，无须全改成we。|
|DSConv-S/L、MS-AgentNet、SLFA、RAA|保持本文已确认名称。三篇范文模块不同，不能为了模仿而改成本稿没有的模块。|
|modeling、generalization、normalization、color等|在本轮可编辑文本检查中未发现相应英式词形混用。技术专名和引用题名不机械替换。|
|MIT/Severson与MIT；全称与缩写|上下文可唯一识别时保留简称；不把正常简称、词形或大小写变化误报成另一个概念。|
|HI/feature、extraction/selection、FLOPs/training time/storage|各有不同对象或步骤，不强行统一成一个词。|

## 详细独立记录

- [时态与语态](./english-consistency-2026-09-14-tense.md)：五类完整实例、范文定位和保留原因。
- [术语、专名与美式拼写](./english-consistency-2026-09-14-terms.md)：七类保留判断及缩写边界。
- [简单句式与直接性](./english-consistency-2026-09-14-directness.md)：两处可选修改与三篇对应语境。

## 审查边界

本轮不是对原始引文、实验实现和统计记录的重新认证，也没有重新目测全部栅格图内文字。历史技术疑点及图像版本事项不因语言检查通过而自动关闭。范文用于校准表达、信息颗粒度和措辞，不用于证明本文数据正确。

本轮仅新增本汇总及三份分报告；论文中文、英文、表格、公式和图像未修改。作者如采纳建议，实施前仍需回读整段并编译；本轮没有正文变更，因此不编译。
