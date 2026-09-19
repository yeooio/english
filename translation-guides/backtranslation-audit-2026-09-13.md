# 全篇反向回译与交叉审查报告

审查日期：2026-09-13。本报告保存作者前一阶段要求的全篇回译核查；作者随后更新阶段为“英文语言与范文风格审校”，新的主任务另见 [语言审校报告](D:/MS-AgentNet-English/translation-guides/language-style-audit-2026-09-13.md)。不把两轮审查混为一轮，也不把本轮回译称为盲译。

## 范围与方法

主审与三个 agent 协作：摘要和引言、第二和第三章、第四和第五章分工审查，随后交叉复核重点；主审核对图表、图片和保护内容。每个文字块提供中文原文、现有英文、中文回译，以及作者指定的五项判断：原意与增漏译；术语/数值/限定；自然简洁；力度与复杂词；三篇范文对应语境。

覆盖206个文字审查块（含标题、关键词、公式引导与解释，不能说成206个正文自然段），另核对39个独立公式。读取22个表格文件、11个图题文件及共享宏和主文件；主稿实际调用18个表、10个图环境，涉及21个图片资产。目录内未调用的4个表和1个图题作为附属文件记录，不计为正文新增内容。图片只核对可见文字和图文关系，不声称逐个数据点重算。

## 交叉复核结论

未发现确定的大范围漏译、擅加实验或英译改变数值；这不是无误保证。应把以下类别分开处理。

|类别|位置与发现|处理|
|---|---|---|
|明确细节遗漏|第1章挑战引导句，中文“三点”在英文`as follows`中未显式保留；后续三项仍完整|可建议`The main challenges faced by existing methods can be summarized in the following three points.`，不影响列举内容|
|可选清晰度|第1章ECMs句中`may ... and depend`的情态作用域；`ordinary normal initialization`略冗余；`nonlinear degradation tail`可能略有直译感|只列候选，不把可理解英语判成错译|
|交叉复核后保留|`preventing`对应设计能力“可避免”；消融语境`RAA is held fixed`；化学材料语境`battery chemistries`|不列确定情态升级/权重冻结/范围缩窄；RAA可按作者需要进一步明确，但不强改|
|原稿定义或证据问题|PCC的“only sensitive to linear changes”；DSConv成本比并非任意参数下都小于1；2D成本符号与1D模块的衔接；综合相关性得分定义；以整池MAPE说明末期局部误差|中文原稿已有，不归咎英译，不在语言审查中擅自修正研究内容|
|数值精度待核|部分百分比降幅无法由表内四舍五入后的底数精确复现|中英数值一致，需核未舍入数据，不直接判数值算错|
|表述歧义|筛选伪代码`each`与`otherwise`的作用范围；消融表`Reduction`的比较基准|报告给出条件性写法，先明确实际定义，不猜测算法或分母|
|图片问题|`Health indicators extraction`、`others Cells`、`Skim`等；CX2面板内CS2图例；模块图DSConv-L/S与正文数据流、残差位置不一致|前几项属语言/拼写；后几项应对照绘图数据和模型实现确认，不能只改正文迎合图|

特别注意：范文词汇有对应原词不等于每种语境都合适；`resource-consuming`有范文依据，不因词长机械替换；`battery systems`不应被强行用来替换上下文合理的`battery chemistries`。原始范文图表中不自然的语法也不应直接继承。

## 完整审查附件

1. [摘要与引言：逐段中英及回译](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13-intro.md)
2. [第二、第三章：逐段中英及回译](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13-methods.md)
3. [第四、第五章：逐段中英及回译](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13-results.md)
4. [表格、图题及主文件](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13-tables.md)
5. [图片可见文字与图文对应](D:/MS-AgentNet-English/translation-guides/backtranslation-audit-2026-09-13-images.md)

附件保留具体位置、原文、回译和定位依据。第五项引用明确是本地TXT行号；本轮对应段核查不冒充三篇全文重新逐句计数。

## 版本与验证

本团队仅创建/整理审查文档，没有修改中文源稿或英文论文。审查期间检测到工作目录的第1、3、4章被外部更新，已将相关引文对齐到本轮收尾快照：第1章远距离特征句；第3章约3d²参数的比较句；第4章`With CS2...used...`句。2026-09-13 22:45（北京时间）之前的最终引文校验：摘要/引言50个、方法274个、结果99个tex/latex代码块均能在对应当前中英文中找到。源稿哈希与本轮基线一致。

保护内容检查工具已执行：引用键等未报保护错误；数字正则所报差异单独核对，不能当作语义自动通过。此轮无正文写入，因此没有新编译，也不将历史构建结果描述为本轮验证。后续若正文再次更新，报告针对所记快照，不自动代表更新后的版本。
