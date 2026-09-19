# 摘要、引言及比较表：本轮完整中英文复核

日期：2026-09-14。只新增本报告，论文未改。先重读当前稿提出候选，再查旧记录去重；已读取AGENTS.md新增的“问题入库前的范文尺度校准”。结论是本轮找到2个新的实质候选，均位于比较表，分别属于方法对象误归类与混合模型名称遗漏；摘要和引言叙述正文没有新增可确认的语法或译义错误。该结论不等于保证没有遗漏。

## 覆盖与检查项

完整覆盖以下6个文件：

- `source-zh/chapters/abstract.tex`与`chapters/abstract.tex`：第1行整段及第3行全部关键词。
- `source-zh/chapters/chapter01.tex`与`chapters/chapter01.tex`：全部48行，包括全部20个实质正文段、34行引导句、两个小节标题、表格引用和排版命令。
- `source-zh/tables/table_1_comparison.tex`与`tables/table_1_comparison.tex`：表题、表头、17条比较行（16篇参考文献及本文）、引文、勾叉、模型和HI名称。

各段均检查：中文主谓宾与并列搭配；指代对象；因果/转折/递进及总分层级；英文主谓一致、时态、修饰范围、主动/被动主体；信息对应、程度与不确定性；术语及摘要—引言一致性。表格另检查单元内容与列名对象是否相符。全文阅读不等于对全部16篇比较文献完成原文事实核验；本轮对发现疑点的ref79、ref80及相邻ref81补做出版社摘要/方法摘录核验。

| 段落位置（中英相同） | 内容与本轮结论 |
|---|---|
| abstract:1、3 | 问题—HI—网络—实验—结论推进、9句对应和5个关键词均保留；复杂度与长期信息范围属既有事项。many与often不重复判错。 |
| chapter01:1 | 优势转安全风险，再引出状态估计需要，关系成立；英文拆句没有丢失后半信息。 |
| chapter01:3 | 容量定义—直接测量限制—间接估计—双重挑战成立；两个However承担不同层次转折。 |
| chapter01:7 | 模型分类与前者/后者回指明确。 |
| chapter01:9 | 数学模型与ECM比较顺序成立；机制总括范围为旧可选精确化项，不算新语法错误。 |
| chapter01:11 | 训练映射、六个模型和实例对应；全类别结构局限按最新范文校准默认保留。 |
| chapter01:13 | 深度学习—CNN原理—两个实例，语法与信息对应保留。 |
| chapter01:15 | CNN限制、循环状态、融合模型及串行限制回指成立。 |
| chapter01:17 | Transformer回应的是紧邻的串行限制；实例—精度代价—标准注意力瓶颈关系成立。 |
| chapter01:19 | 输入来源、阻抗/温度/IC限制及平滑实例；英文未把全部内阻指标说成都需阻抗谱。 |
| chapter01:21 | 时间差定义、文献实例与窗口优化动机关系成立；PCC相关对象可由全段明确，不要求每次展开变量。 |
| chapter01:23 | 多源信号与统计/降维实例，动作及先后对应。各实例科学细节不在无原文时判错。 |
| chapter01:25 | 多源信息不必然提高精度，因此需要筛选；保留may/can及其中文力度。 |
| chapter01:27 | 比较维度、HI稳定性与资源权衡；旧并列搭配和英文修饰建议按下表校准，不重复计新。 |
| chapter01:34 | 三项挑战引导与后续数量一致。 |
| chapter01:36 | 跨池相关、PCC/SCC、冗余与输入确定形成合理推进；旧英文省略候选降级。 |
| chapter01:38 | 局部变化和长期趋势协同是建模需求；不把“使…相互补充”机械判为物理因果错误。实际历史跨度属旧方法范围事项。 |
| chapter01:40 | 循环串行与标准注意力二次增长分别对应模型类别；中文“其”的近接对象清楚。 |
| chapter01:42 | 两层面与两种操作可理解；明确第二动作主体属于旧可选直接性改善。 |
| chapter01:44 | 标定/筛选总分关系可读，改连接词属旧可选事项；末句SOH相关对象可回指。 |
| chapter01:46 | SLFA、RAA、两尺度卷积与摘要对应；线性复杂度限定属旧自足性建议。 |
| chapter01:48 | 多数据集、消融复杂度、跨数据集迁移分工明确；没有把所有结果说成跨域直接泛化成功。 |
| table_1_comparison:1—30 | 中英勾叉、文献和17行逐项对应，表头译义旧项保留为可选；ref79与ref80模型单元提出本轮新候选，ref81名称完整化仅作可选。 |

## 本轮重读的范文及尺度

重新读取三篇摘要和引言TXT中相应完整功能语境：Engineering-AI摘要34—47行、引言49—112行及贡献141—159行，另读相关工作114—180行作模型/输入对象校准；BMSFormer摘要30—40行、引言49—240行；JESSOHRUL摘要33—50行、引言52—352行及Table 1相关上下文。JESSOHRUL原PDF第3—4页另用pypdf的layout模式按左右栏核对引言收束、挑战/贡献、工作流程和Table 1，不从TXT相邻行推断段落顺序。

三篇都会在摘要/引言省略完整实验参数、使用被动语态、概括长期与局部建模目标，且并非每句都重复HI–SOH相关对象。因而本轮没有以“还能展开得更具体”为由要求摘要增加实现细节，也没有强制将全部被动句改成主动句。范文只作为表达尺度参照；对象不同或与原始文献冲突的内容仍需独立核实。

## 新候选 E-I01：Gaussian filter被放入估计模型列

位置：[中文比较表第15行](D:/MS-AgentNet-English/source-zh/tables/table_1_comparison.tex:15)、[英文比较表第15行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:15)；列名在第7行；对应文献为[references.tex第169行](D:/MS-AgentNet-English/backmatter/references.tex:169)的ref79。

分类：中英共同的方法对象误归类，非中文语法错误，非英译新造错误。英文忠实继承了源表问题。

原中文单元（源表本来即用英文名称）：

> Gaussian filter（×）

所属中文列：

> 评估模型（是否为原创）

建议中文单元：

> 基于IC特征的线性回归（×）

现有英文单元及列名：

> Gaussian filter (×)
>
> Estimation model (original design)

建议英文单元：

> Linear regression based on IC features (×)

这是只替换模型名称的最小建议，其他列及勾叉暂保持原样；并不表示已核实该行全部分类或“原创”的操作定义。若作者希望保留高斯滤波信息，可将同一个单元写为“基于高斯滤波IC特征的线性回归 / Linear regression using Gaussian-filtered IC features”，但需要避免误读为直接回归完整曲线。短版本已足以明确模型对象，不必为完整性把所有预处理塞进模型列。

直接证据来自ref79的[出版社原文摘要与Highlights](https://www.sciencedirect.com/science/article/pii/S0378775317314532)。Highlights写：`Gaussian filter is used to obtain IC curves with improved smoothness.`（高斯滤波用于获得更平滑的IC曲线。）摘要另写：`A linear regression relationship is found`，并明确该回归联系电池容量与IC曲线感兴趣特征的位置。由此可区分平滑操作与SOH估计映射。文献为Journal of Power Sources 373 (2018), 40–53，DOI 10.1016/j.jpowsour.2017.10.092。此处只对方法对象作结论，不声称读完该文全部实验或重新计算其结果。

改后效果：读者看到的模型列将回答“用什么关系从IC特征估计容量/SOH”，而不是“先怎样平滑曲线”。这不是要求更复杂的英文，也不是只因filter不能出现在模型列就判错——某些滤波器确实用于状态估计；本项依据是这篇被引论文对Gaussian filter实际作用的明确说明。

### 范文是否也如此，以及为什么仍保留候选

- **JESSOHRUL确实也如此。** 原PDF第4页Table 1的Assessment model列同样出现`Gaussian filter (x)`，对应[TXT第431、454行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:431)。因此不能说“范文都把预处理和模型分得更清楚”。但该文第2页§1的[TXT119—121行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:119)又将Li等人的处理介绍为比较过滤方法并从IC曲线取特征，使用`different filtering methods`。本文ref79的出版社原始摘要提供了更直接的对象依据。
- **Engineering-AI采用另一种层次。** 第2页§2.2的[TXT135—139行](D:/MS-AgentNet-English/style-references/Engineering-AI/introduction.txt:135)描述数据驱动方法为`mapping extracted features directly to SOH`；相邻§2.2.1另谈微分及平滑预处理。该处不是同一篇被引研究的逐项模型表，故只能支持区分输入处理和估计映射，不能替ref79作事实背书。
- **BMSFormer同样区分输入与输出映射，但没有对应同一表格单元。** 第2页§1的[TXT137—151行](D:/MS-AgentNet-English/style-references/BMSFormer/introduction.txt:137)将输入HI、输出SOH与后续学习模型区分。不存在据此要求本文额外增加统计信息的理由。

与范文的条件比较：这是相同“比较表模型列”的分类问题，且范文存在同样写法；但本轮核实的原始文献表明两类操作的对象不同，满足AGENTS.md所说不能因范文也如此而自动放行的情形。JESSOHRUL该表行标[16]，引言中Li等人的滤波研究标[19]，本报告不声称两者指向同一文献，也不以范文表格编号支持本文ref79的事实。主审已独立复核ref79出版社摘要并认可该对象区别；仍仅提交作者建议，不直接写入论文。

另核对[2018年勘误的作者机构记录](https://researchportal.vub.be/en/publications/erratum-to-a-quick-on-line-state-of-health-estimation-method-for-/)：其处理的是误显示的排版代码，不涉及高斯滤波与线性回归的功能说明，不改变本项判断。

### 主动反驳后二次复核

1. 反驳“Gaussian filter也可能是状态估计器”：这一一般可能性成立，所以不能只看名称判错；回查ref79明确是在IC曲线上去噪，而容量映射采用线性回归，候选仍成立。
2. 反驳“模型列可以只列整套方法最显著的组件”：若列名改成“方法组成”，可以容纳预处理；当前两语言列名及相邻LSTM/Transformer/RF单元都在比较估计模型，因此只列高斯滤波会改变对象。最小修复是该单元，而非重写整个表。
3. 反驳“这是不是旧回译表头T01”：事后检索全部translation-guides，Gaussian filter只出现在旧回译报告的原/英文表快照；T01讨论Estimation model与Model evaluated的译名，没有讨论滤波/回归误归类，故不是重复包装旧项。

## 新候选 E-I02：ref80的BiLSTM-Transformer被缩成Bi-LSTM

位置：[中文比较表19行](D:/MS-AgentNet-English/source-zh/tables/table_1_comparison.tex:19)、[英文比较表19行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:19)。对应[文献表171行](D:/MS-AgentNet-English/backmatter/references.tex:171)的ref80。

原中文单元：`Bi-LSTM（×）`。建议中文单元：`BiLSTM-Transformer（×）`。

现有英文单元：`Bi-LSTM (×)`。建议英文单元：`BiLSTM-Transformer (×)`。

分类：中英共同的模型名称遗漏。文献标题已指明混合模型；本轮进一步取得[出版社摘要及方法节摘录](https://www.sciencedirect.com/science/article/pii/S0360544224031943)，明确所提方法是`BiLSTM-Transformer`，并说明它结合BiLSTM与Transformer，以四个特征为输入、SOH为输出。出处为Energy 311 (2024), 133418，DOI 10.1016/j.energy.2024.133418。本项不因题名含某个词就机械要求表中逐字复制，而是方法摘录也确认两种网络共同构成该估计模型。

最小修复只补回Transformer，不改其他列或原创勾叉。作用是避免把卷积/循环/注意力结构的资源比较建立在少列一个核心网络组成的标签上；不据此推断原论文实际效率、也不要求补充新实验。

范文尺度校准：JESSOHRUL第4页Table 1也有简写`Bi-LSTM`的单元，说明不能要求每个文献方法名都毫无省略。但该表行编号[23]不能未经核实直接等同本文ref80。另一方面，该文第2页§1介绍Z. Li的方法时明确并列BiLSTM和Transformer，见[TXT150—152行](D:/MS-AgentNet-English/style-references/JESSOHRUL/introduction.txt:150)。BMSFormer第2页§1的[TXT104—116行](D:/MS-AgentNet-English/style-references/BMSFormer/introduction.txt:104)介绍混合网络时也保留两个核心组成。Engineering-AI对应引言则以CNN/RNN/Transformer类别概括，本身没有对同一ref80给出逐项表格。本文同一表内对BiGRU-Transformer、CNN-Transformer都保留两类网络，故只将本项写成Bi-LSTM会掩盖实际混合架构，与只省略某个训练优化器不同。

主动反驳：如果该列明确是“主要骨干类别”，Bi-LSTM可作为一种归类，不必复制全名；但当前列名是“估计模型”，且相邻行保留混合结构，因此这里补回Transformer有实质区分价值。事后检索旧报告仅发现原表快照，无此前指出该遗漏的条目。

### 相邻ref81：仅列可选名称完整化，不另计实质错误

[中英比较表20行](D:/MS-AgentNet-English/tables/table_1_comparison.tex:20)为`LSSVM-AdaBoost`；[出版社摘要与Highlights](https://www.sciencedirect.com/science/article/pii/S0360544224027671)称`GWO-LSSVM-AdaBoost`。若作者要在表中统一完整命名，中英均可改为`GWO-LSSVM-AdaBoost`，勾叉不动。其出处为Energy 308 (2024), 132993，DOI 10.1016/j.energy.2024.132993。

但现单元仍保留了LSSVM估计器与AdaBoost集成骨干，省略GWO优化组件并不必然把核心估计架构变成另一种模型。因此按范文简写尺度，此项仅为可选名称完整化，不与ref80同级计错。ref82/83/84的标题分别指LSTM变体、带注意力LSTM、改进ELM，而表里用LSTM/ELM家族名；本轮没有因标题较长就再扩大为三个错误，也没有对其原文做超出此边界的事实判定。

## 其他候选在第二次通读后撤下或保留

- 摘要“many existing…often”：数量与频率限定不同，并有既有作者确认；撤下“同义重复”的疑点，保留。BMSFormer摘要也用many和resource-consuming，JESSOHRUL摘要也概括many existing，不能机械以字数删词。
- 引言23行电压、电流、温度、IC、DTV曲线的并列：可以理解为不同曲线来源，英文curve后置统摄并列项；没有证据判遗漏“数据”，保留。
- 引言38行“使局部变化与长期趋势相互补充”：上下文已经限定为模型表征，不是声称改变实际电池的退化规律；三篇均有局部/全局特征共同建模概括，不为抽象名词替换增加一项。
- 表格LC等简称：可读性可以改进，但文献比较表保留模型缩写常见，当前不靠猜测扩写；尤其LC的原词在范文存在但技术定义仍不够明确，不将其擅自解释为某个已知算法。没有作为本轮确认错误。
- 摘要和引言“长期/长程/长尺度”：在功能上分别对应依赖和卷积尺度，未发现新译义矛盾。真实输入跨度由既有方法协议审查处理，不在本轮反复给摘要加限定。

## 旧记录状态：不重复作为本轮新发现

以下计数只针对本轮范围直接对应的10条旧记录/已提交建议，不包括其他章节的跨章证据主项。依据最新[范文反向校准记录](D:/MS-AgentNet-English/translation-guides/reference-calibration-2026-09-14-scope.md)，10条中2条默认保留、6条仅为可选表达或自足性建议、1条是英文已修好而冻结中文仍保留的搭配问题；真正剩余的技术参数核实仅1项，即主实验真实N，不是摘要long-range用语错误。不将“未采用可选润色”计为未解决错误。

| 旧项 | 本轮尺度校准与状态 |
|---|---|
| ZIC-01 实时性受到限制 | 中文并列搭配问题仍成立；英文已分别写资源有限与实时要求严格，不再改英文。 |
| ZIC-02 摘要/贡献线性复杂度条件 | 可选自足性说明。三篇摘要/贡献也会简写复杂度，本文方法及结论已有条件；不列成公式错误，不要求摘要塞入全部变量。 |
| ZIC-03 ECM机制总括 | 可选概念精确化，默认可保留。BMSFormer也有同类机制概括，EAI用electrochemical or electrical dynamics；范文存在差异，本文后句已解释ECM动态，不能将本项重新作为必需作者闭环问题。 |
| ZIC-04 传统ML宽泛局限 | 默认保留。BMSFormer和JESSOHRUL也有同功能、类似前提的局限概括；不要求机械加some/may。本轮没有核实全部引文，不因此宣称原始文献审计通过。 |
| S-IC01 长期/全局实际输入范围 | global/long-range保留；仅主实验真实N仍作低成本参数核实。流程图已有步长1，不再报步长遗漏，不强制摘要补N或核填充。 |
| I-01 引言27行英文后置in addition to | 可选清晰化。原意结合上下文可恢复，改Both…and有助明确并列因素，但不升级为已证实译义反转。 |
| I-02 引言36行correlations across cells | 本轮建议保留原文。整段已明确HI–SOH关系，范文也有跨电池概括及省略；补HI–SOH可选，但不再将不重复对象本身列成待修错误。 |
| I-03 引言44行总述—分述 | 可选衔接改善，原文没有明确断言最终评价早于标定。范文同样会先总述功能、后述步骤，不能以可能误读认定真实流程错。 |
| 口头续查 引言42行分别/并以 | 可选直接性。分别可以统摄两个谓语，主语可从该框架承接；不判缺主语。 |
| T01 比较表Estimation model/Model evaluated | 可选表头译义澄清；SOH上下文已有理由使用Estimation model，与本轮新发现的具体方法误归类不同。 |

在以上指定文本及本轮证据范围内，二次通读及主审交叉复核后保留E-I01、E-I02两个新增实质候选，ref81仅列可选。没有为了持续审查而新增同义改写，也没有将本轮未发现更多问题写成论文已经零错误。

