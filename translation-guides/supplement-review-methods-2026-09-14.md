# 第2—3章中英限定与遗漏补查

日期：2026-09-14。范围：当前 chapters/chapter02.tex、chapter03.tex 及 source-zh/chapters 同名全文；只审查否定、限定词、数量/范围、respectively和指代，不修改论文。

## 结论

本轮未确认新的译义偏移或必须修改项。先从当前中英文逐段对照，再查看自己既有 exhaustive-review-methods 报告去重；不把旧的中文概念表述问题重新算作翻译遗漏。以下记录值得保留的对应关系，而非制造改前改后。

## 全文覆盖与重点核验

|范围（中英同名文件行号）|核验结果|
|---|---|
|第2章1–43：框架、数据集和特征工程总述|相应数据集/其他电池、下一循环、两种CALCE组、8/6/3节电池、约1.1 Ah及三种充电策略的归属一致。英文approximately保留“约”；configuration-selection cell没有改变配置电池功能。|
|第2章47–98：六类特征及定义|15项候选、恒流阶段、通常缓慢、200个采样点、两个放电电压窗口及完整充放电阶段均保留。HI2–4、HI10–12、HI13–14的列举顺序一致。HI5–9英文没有照搬中文五项对三属性的“分别”，避免错误的一一配对，不应补回respectively。|
|第2章106–139：双相关标定|同一数据集两节、部分/多数研究、min绝对相关、两系数取较小值、三阶段窗宽/步长和若高于否则保留均对应。PCC仅线性、稳健评分使强相关的概括是中英共同旧项，不是本轮新译义偏移。|
|第2章143–165：HI筛选|only、all、already selected、same dataset、do not participate逐项保留准入范围及数据隔离。四个数值及Cell1/2顺序一致。比较保留listed、reported、corresponding cells、remaining six，不扩张为全部文献或全部电池。|
|第3章1–46：架构和Block|three steps、immediately following、next Block及LN0不使用额外scale or bias均对应。FFN英文“The result”明确残差相加对象，保留。|
|第3章50–185：卷积|each/all、may过拟合、same通道配置、two/three倍扩展、两层逐点/一层深度卷积、mainly计算来源及Block层残差对应。两层卷积“expand and restore…respectively”按先后顺序可理解，无错配。|
|第3章191–267：一般/Softmax/线性注意力|单头与所有头、nonnegative、all-ones、full矩阵、映射维度等于dh和fixed dh两条件、does not explicitly均保留。未把不显式引入局部特征改成绝对不能建模局部。|
|第3章271–386：RAA与SLFA|约3d²、仅3d、两个可学习智能体、跨样本共享、两个阶段、共同正比例、含正得分/无正得分、非正截断、秩不超过na、固定h和na、训练阶段Dropout均对应。Phi矩阵尺寸的respectively与聚合/广播顺序一致。|

## 两处主动反驳后保留

1. 第3章347行中文“加权组合”，英文“broadcasting weights, which combine the two agent contexts”。虽然未另加weighted，weights已是combine的施事，紧邻公式也是权重矩阵乘上下文；信息没有丢失。建议英文：保留现有句子，不改为重复的weights…weighted combination。
2. 第2章158行respectively置于PCC和SCC并列句末。Cell1 and Cell2在前已给出顺序，两组各两个数值也对应同一顺序；不能仅因没有给每个分句都补respectively就判错。建议英文：保留现有句子。

## 本轮范文尺度校准

重新读取以下连续语义段落；TXT跨栏插入的图题、公式及其他段落不作为连续句序依据。本轮没有基于错序作段落修改建议。

- Engineering-AI methodology.txt 184–197完整“Feature Selection & Fixation & Deployment”步骤及203–208相关性计算句：短语“frozen as a fixed hyperparameter”“using only the calibration/training data”。它也以步骤上下文承载固定参数/数据范围，而不在每句重复全部协议。本文160行已明确三种不参与活动，保留，其实际数据划分以本文为准。
- BMSFormer methodology.txt 806–814完整Softmax/linear比较段、833–839公式后的完整复杂度说明段，并读至845行下一段结尾。短语“results can be reused for each query”。其复杂度段也依赖公式和前文对象，未每句重述全部维度。本文265、363行固定量限定更明确，无需再扩写。本轮不继承范文关于梯度/运行时间的额外主张。
- JESSOHRUL methodology.txt 290–314三个完整ReLU动机、稳定性及表达能力段。短语“non-negative representations”“By truncating negative responses”。范文也用局部上下文承接限定；本文311行比该段明确地区分nonpositive、含正得分和无正得分，因此不能凭范文用negative而把本文nonpositive改掉。两篇使用的注意力构造不同，不将范文的物理解释或噪声结论移植过来。

复查结论：否定和范围不是仅凭关键词一致就通过，上述判断同时核对了它们修饰的对象与邻近公式。未发现本轮可确认新增项；这不构成全文零错误保证。
