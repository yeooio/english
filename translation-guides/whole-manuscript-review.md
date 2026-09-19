# 全文审查：忠实度、自然英语、三篇范文与图文一致性

日期：2026-09-13。性质：只读审查及修改建议，未修改正文、表格、图片或冻结中文源稿。

## 结论

当前稿已经是完整、整体可读的英文稿，主线和大多数技术术语保留得较好，但仍有需要修正的表达和图文一致性问题，不能把“已翻译、已编译”等同于“可以直接定稿投稿”。

优先级：先核对图文技术冲突，再改有明确依据的措辞和比较句，最后处理可选风格优化。不是重新翻译整篇，也不是为增加范文词汇而反复换同义词。

本轮连续阅读摘要及第1–5章英文，对照冻结中文全部正文说明，核查公式保护内容、相关表格、全部图注，并重点查看图1、3、4、5、6、7的原始图片。重新读取三篇摘要及对应HI、模型、资源和结论表达；摘要句界回看三篇首页。没有重新核实84篇引文的外部事实，也没有复现训练、重新计算全部实验结果或核验原始绘图数据。上一轮37页排版检查不是本轮科学内容审查的替代。

## 一、优先处理的图文和源稿问题

### C1：图7(d)与SLFA/RAA正文不一致，不能只改名称

位置：figures/fig3_3_attention_comparison.png；chapters/chapter03.tex:271、277、351、367。

- 图7(d)写成 **Skim Local-Global Fusion Attention**，正文为 **Slim Local-Global Fusion Attention**，Skim应统一为Slim。
- 图中在K/V处标注DSConv-L；正文则规定DSConv-S先处理输入，再进入RAA和局部分支，DSConv-L位于SLFA之后。
- 图中输出标为Linear；正文RAA输出是可学习逐通道缩放、残差相加，SLFA还包含独立局部分支的LN及RAA分支的Dropout和缩放。
- 因而仅把图中L改成S并不足以保证正确。需要作者确认图7到底表示RAA内部还是完整SLFA，再按实际公式重画。不能反过来迁就旧图改公式。

这是图文技术一致性问题，不是英文翻译引入的算法错误。

### C2：图6模块内部运算需与公式核对

位置：figures/02.png；chapters/chapter03.tex:139、148、174。

图6(c)、(d)在第二个PWConv后另画Linear，且(d)画出模块内部Add与残差支路。正文DSConv-S在第二个PWConv后逆转置、残差相加；DSConv-L残差明确在Block层完成。需确认Linear是否只是重复表示已有投影，以及(d)的残差边界是否正确。不要自动删除图层或增加正文运算。

### C3：Oxford充电协议、放电表项仍需统一

位置：chapters/chapter02.tex:29；tables/table_2_1.tex:19、21。

- 正文写constant-current--constant-voltage；表中Oxford写CC (2C)。需要判断表格是否只列CC阶段、或正文/表格是否过时，不能由语言审查决定实验协议。
- 放电协议写 **variance**，不是适当的协议名称。正文明确为动态电流曲线，最小语言建议为 **Dynamic current profile**；ARTEMIS等细节是否放进表格由作者决定。

两项在冻结源稿中已经存在，不能说是本轮翻译造成。

### C4：图4缺少四个面板的身份说明

状态更新（2026-09-13）：已按作者批准的映射在工作图注标明(a) Cell1/PCC、(b) Cell1/SCC、(c) Cell2/PCC、(d) Cell2/SCC，并通过LaTeX添加面板编号；编译和第13页视觉检查通过。原PNG未改，SoH拼写建议仍属后续图片标签事项。此更新是采纳作者确认的排列，不等于新完成原始绘图数据核验。

位置：figures/fig4_pccscc_print.png；figures/figure_2_4.tex:6；chapters/chapter02.tex:147。

正文说明Cell1/Cell2及PCC/SCC，但图中四个面板没有明确的电池/PCC/SCC标签，图注也没有逐面板映射。不能要求读者从数值反推。核对绘图数据后补上(a)–(d)的对应关系；本轮不擅自猜测顺序。SoH建议统一为SOH。

### C5：图3坐标与颜色说明需要核对

作者后续确认：图3(a)时间轴标注问题正在由作者修改，实际时间为约千秒量级（作者表述“1000s类似这样子的”），不是当前刻度字面表示的0.04秒。此项转为备选/待同步，不再重复要求核查曲线或实验结果。确切范围、刻度及倍率尚未给定，不自行推算或改图；待作者提供新版图片后，仅检查最终时间刻度与单位是否一致。此确认仅涉及时间轴，不自动解决颜色条说明。

位置：figures/fig3.png；figures/figure_2_3.tex:6。

(a)横轴标Time (s)，范围约0–0.04；图注没有说明缩放系数或归一化，不能判断该标注是否完整。四个颜色条只有数字，没有变量名称，图注也没有交代。需要核对原始绘图单位和颜色变量。这里只报告信息缺口，不擅自改为小时、天或循环数。

### C6：SOH的百分比与归一化口径缺少明确衔接

位置：chapters/chapter02.tex:6；chapters/chapter04.tex:17–34；SOH结果曲线及误差表。

第2章SOH公式乘100%，曲线和误差表采用小数尺度；第4章未明确y和预测值是否使用0–1尺度。二者可以通过归一化相容，但目前说明不够明确。建议作者确认实际训练/评价口径后补充一句说明，不改已有公式或表值。MAPE 0.00615与0.615%的换算本身正确，不应把它误判为错误。

### C7：现有图1/图5的英文标签需要集中清理

位置：figures/fig1.png；figures/01.png。

| 现有文字 | 建议 | 说明 |
| --- | --- | --- |
| MS-CCCT & PCC/CSC screening | MS-CCCT & PCC/SCC screening | CSC与本文定义不符 |
| Health indicators extraction | Health indicator extraction | 用单数名词作定语 |
| Health indicators splitting | HI sequence segmentation | 图示实际切分序列；若保留splitting，可用HI sequence splitting |
| Four datasets dividing | Partitioning of the four datasets | 先核对其确实指数据角色划分 |
| Five models training, validating and testing | Training, configuration selection, and evaluation of five models | 需同时核对图示角色，不引入独立验证集 |
| others Cells | Other cells | 词形、大小写 |
| L-DSConv | DSConv-L | 与本文正式模块名统一 |
| Embed layer | Embedding layer | 与正文一致 |
| point-Conv / depth-Conv | Pointwise convolution / Depthwise convolution | 保留准确专业词，图内可用已解释缩写 |

**对旧记录的纠正：当前图1写的是few-shot adaptation，拼写正确。本轮不再沿用此前记录中的adaption问题。**

## 二、建议修正的语言问题

下列建议是最小修复，不是已批准的新正文。英文片段中的省略号仅用于定位，不应写入论文。

### L1：参数“数量”应明确，而不是参数“值”增大

位置：chapters/chapter01.tex:40。

中文：这些方法增加了模型参数和计算操作。

现有：These approaches increase model parameters and computational operations.

建议：These approaches increase the number of model parameters and computational operations.

理由：increase model parameters容易理解为增大参数值。使用number明确数量，与后文parameter count一致。Engineering-AI §7的parameter count及BMSFormer §4.2.2的total number of trainable parameters提供准确术语依据。

### L2：卷积层融合与特征融合的修饰关系不够清楚

位置：chapters/chapter01.tex:15。

中文：相距较远的特征通常需要经过多层卷积才能融合。

现有：features far apart generally require multiple convolutional layers to be fused

建议：features that are far apart generally need to pass through multiple convolutional layers before they can be fused

理由：明确先通过多层卷积，再融合特征；不是将多个卷积层融合。保留原文“通常”和操作顺序。

### L3：比较的两边应是同类对象

位置：chapters/chapter03.tex:288。

中文：相较于标准查询、键和值线性投影约$3d^2$的参数量，三组通道缩放向量仅包含$3d$个参数……

现有：Compared with approximately $3d^2$ parameters for standard linear query, key, and value projections, the three channel scaling vectors contain only $3d$ parameters ...

建议：Compared with standard linear projections for queries, keys, and values, which require approximately $3d^2$ parameters, the three channel scaling vectors contain only $3d$ parameters ...

理由：现有结构表面上比较“参数”与“向量”；建议比较两种表示方式，并分别说明参数数量。数学内容不变。

### L4：误差/存储与模型本身的比较应补齐

位置：chapters/chapter04.tex:96、109、170、172。

- 现有：Compared with CNN-Transformer, ... its average MAE is reduced ...
- 建议：Compared with the corresponding errors of CNN-Transformer, ... its average MAE is reduced ...
- 现有：32.2% lower than the closest model, Transformer, at the same dimension
- 建议：32.2% lower than that of Transformer, the closest model, at the same dimension

理由：明确误差与误差、存储与存储比较；所有比率、对象顺序保持不变。不是把已有相对降幅改为准确率提升。

### L5：平均操作不要语法上挂到模型本身

位置：chapters/chapter04.tex:109；chapters/chapter05.tex:3。

- 现有：Averaged over the six cells, MS-AgentNet achieves an $R^2$ ...
- 建议：Across the six cells, MS-AgentNet achieves an average $R^2$ ... and average MAE, MAPE, and RMSE ...
- 现有：Specifically, averaged over two cells in the CALCE CX2 dataset, MS-AgentNet reduces MAPE by 52.69% compared with CNN-Transformer.
- 建议：Specifically, the average MAPE of MS-AgentNet over the two cells in the CALCE CX2 dataset is 52.69% lower than that of CNN-Transformer.

理由：准确表达“先按两节电池平均，再比较MAPE”，不变成“对两节电池降幅取平均”。

### L6：源域适应句的动作主语不清

位置：chapters/chapter04.tex:132。

中文：分别以CS2_36和CX2_36作为源域，使用Oxford Cell1的前置循环数据进行读出层适配……

现有：Using CS2_36 and CX2_36 as the respective source domains, the readout layer is adapted ...

建议：With CS2_36 and CX2_36 used as the respective source domains, the readout layer is adapted ...

理由：消除Using前置分词的隐含施事与readout layer不匹配；保持原文协议，不增加新数据角色。

### L7：能量效率符号说明的双重and不够清楚

位置：chapters/chapter02.tex:98。

现有把三个充电量、三个放电量用“, and ... , and ...”连接，再用respectively解释。

最小建议：将两组三元量加括号，明确“充电组三项”和“放电组三项”分别对应端电压、电流幅值、时长。保留六个符号和完整循环限定。此处不应为了短句而删除电流绝对值。

### L8：缩写首次定义有遗漏或偏晚

位置：chapters/chapter02.tex:37（SOC）；chapters/chapter04.tex:166（FLOPs）；chapters/chapter01.tex:19（BP）；tables/table_4_4.tex（MLP）。

FLOPs首次正式说明可写floating-point operations (FLOPs)，BMSFormer §4.2.2已有完全对应的原词。SOC、BP、MLP建议检查首次出现处的全称；BP等应按相应模型的实际名称确认，不凭缩写随意扩写。DSConv正式定义到第3章较后位置才出现，而模块名已提前使用，可在模型首次说明中补足一次。属于术语可读性检查，不要求对ReLU等所有常见符号机械反复定义。

## 三、可选自然度优化：不列为硬错误

| 位置 | 当前表达 | 可选建议 | 保留边界 |
| --- | --- | --- | --- |
| 摘要S6 | The network mainly integrates ... | The network is mainly built around ... | 保留“主要”；这是必要英语适配，不是范文原句 |
| 第2章29、33行 | Cycling aging records from ... | Aging records from cycling tests on ... | 保留全部电池编号与数量 |
| 第2章60行 | charge timing features | time-based charging features | 与前文时间类HI衔接；不改为峰位或采样时刻特征 |
| 第2章106行、第5章1行 | feature-development cell set | set of feature-development cells | 普通句法适配，不改协议角色 |
| 第4章65行 | median late-stage loss standard deviations | median standard deviations of the late-stage loss | 只降低名词串阅读负担，保留中位数统计对象 |
| 第4章154、158行 | combined performance / combined results | overall performance / overall results | 普通综合表现可适配；combined average error作为本文指标名称保留 |
| 第5章3行 | showing its lightweight advantages | highlighting the advantages of its lightweight design | 与已批准摘要末句统一；只在保留“优势”原意时使用 |
| 第5章5行 | real-vehicle operating data | data from real-world vehicle operation | 不将未来验证写成已完成 |

摘要many existing ... often已经作者明确批准，many限定方法范围，often限定依赖频率；不能简单认定为语法重复然后删去。resource-consuming model structures确实来自BMSFormer摘要，虽不如某些替代表达常见，但不是错误，不为了“更母语”而直接改掉作者确认用法。

引言P01的transportation powered by new energy sources稍长，但语义范围未确认前，不改成electric mobility等更窄概念。

## 四、三篇范文：确切用词与采用边界

以下中文均为助手释义。

| 范文位置 | 准确短引 | 释义与本稿用途 |
| --- | --- | --- |
| BMSFormer 摘要p.1 | fuse multi-scale and multi-channel features | 融合多尺度、多通道特征；本稿摘要已有复用，可保留 |
| BMSFormer 摘要p.1 | mainly integrates | 主要集成；这是确切范文用语，但较生硬，列为可选适配而不是伪称语法错误 |
| BMSFormer §4.2.2，full.txt:1367 | total number of trainable parameters | 可训练参数总数；用于数量与参数值区分 |
| JESSOHRUL §3.5.2，full.txt:1829 | ranked according to their correlation strength | 按相关强度排序；第2章已有对应，阈值仍采用本文阈值 |
| JESSOHRUL Table 4，full.txt:1635 | The voltage corresponding to the peak | 峰值对应电压；准确区分峰高和峰位 |
| Engineering-AI 摘要p.1 | identifies robust health indicators | 识别稳健HI；本文保留自己的提取与筛选分工 |
| Engineering-AI 摘要p.1 | long-range degradation dependencies | 长程退化依赖；本稿已有准确复用 |
| Engineering-AI §7，full.txt:2821 | a parameter count of only 6114 | 参数数量；仅借parameter count，不借其数字或硬件验证 |

三篇的作用已经体现，不是“没套完词”。下一轮重点应是修复上述具体缺陷，而不是增加state-of-the-art、significant等评价词。不将本文的longer time scales、long-term trends和long-range dependencies全部强行改成同一个词。

### 摘要结构核查

三篇首页摘要句界已核对。BMSFormer 7句、JESSOHRUL 8句、Engineering-AI 6句；本文9句。本文对应“背景—不足—框架—HI方法—网络—注意力—卷积—验证—结果”，信息顺序与中文一致。无需为了像范文强制删句、合并段落或添加结果数字。

详细句长、主语、时态和功能记录见whole-manuscript-review-reference-analysis.md。统计描述选定摘要，不是三篇全文句数，也不作为通过门槛。

## 五、保留项与检查结果

- 摘要、第1–5章的论证顺序和段落文件块配对保持一致。
- 标签、引文键、图表输入路径的比较一致。
- 全文没有把健康指标重新写成SOH metrics，也没有把depthwise改成deep separable。
- source-only evaluation与few-shot adaptation分开；训练电池、配置选择电池未改为新的独立验证角色。
- 第4章负R²、LSTM训练更快、单模块不总是改善结果均保留。
- 第5章“未来验证”和“部署潜力”没有改成已完成的嵌入式实验。
- 数字扫描的中文边界误报已检查；第3章少一处重复ReLU$^2$名称中的上标，以及“全1向量”译为all-ones的数字形式变化，不是删改公式。不能仅凭数字正则证明数学正确。
- 这轮未发现需要整篇推翻重译的证据，但不作“零错误”“母语保证”或投稿接收承诺。
- 本轮未编译新PDF，因为未改稿；已有编译成功不消除上述审查意见。

## 建议的下一步

先批准L1–L8中的明确语言修复，并逐项处理C1–C7需要作者确认的图文问题。可选优化单独决定。修改时仍须回查中文，不改冻结源稿；写入英文后更新中英对照并重新编译。
