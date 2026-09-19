# 三篇范文联合词库：原词与短搭配

逐章使用入口：[引言：三篇原词与本文逐段对应](introduction-vocabulary.md)。先按本文位置选词，再回查本库；引言入口中的复用词不重复计入本库120项。

[摘要及第二至第五章：词与搭配索引](section-expression-vocabulary.md)仅整理各章原词和使用细节；其中复用词不重复计入本库120项。

核对日期：2026-09-13。三个agent分别核对三篇正文，主审再对120项逐项进行三篇交叉检索。**本库是用词证据库，不是120项已全部冻结的本文译名。** 已确定首选词仍以 `terminology.md` 为准；不得为覆盖词库而向正文添加新概念、实验或主张。本轮未修改论文正文。

## 范围与定位

- 本轮收录120项不重复的完整词组/短搭配，覆盖输入与HI、预处理与序列、模型与数据流、训练与实验、结果与比较、操作与句间搭配。
- 其中13项在三篇均定位，25项在两篇定位，82项目前在一篇定位。“目前定位一篇”不等于其他论文没有相近表达，更不代表该词为作者独创。
- 检索忽略大小写、软连字符和排版换行；不拼接不同句子、不将近义改写算成原词。正常的连续长词组内片段可作为短搭配，但不冒充独立术语或完整句子。
- BMS、EAI、JES分别对应 `style-references/BMSFormer/full.txt`、`style-references/Engineering-AI/full.txt`、`style-references/JESSOHRUL/full.txt`。表中L是当前TXT行号，不是PDF页码。
- “语境出处”来自对应agent查看的正文位置；“交叉定位”是各篇正文中的首个匹配，可能在摘要、综述、图表或公式释义。出现次数不是推荐优先级。
- TXT存在双栏穿插。这里核实词组，不据此宣称已核实每段叙事顺序；正式翻译仍回看对应完整小节，必要时看PDF。
- 本库是前一轮HI基础词表的扩展，不替代原有lightweight、long-range dependencies、health indicator等词条，也不表示三篇所有可用表达已穷尽。

## 三篇共同出现的本轮新增表达

| 中文 | 原词/搭配 | 三篇定位 |
| --- | --- | --- |
| 标称容量 | `nominal capacity` | JES L1296；BMS L405；EAI L276 |
| 运行条件 | `operating conditions` | JES L116；BMS L37；EAI L97 |
| 标准卷积 | `standard convolution` | JES L740；BMS L36；EAI L2087 |
| 特征图 | `feature map` | JES L745；BMS L769；EAI L907 |
| 卷积核大小 | `kernel size` | JES L847；BMS L219；EAI L856 |
| 残差连接 | `residual connection` | JES L587；BMS L811；EAI L824 |
| 序列长度 | `sequence length` | JES L277；BMS L1024；EAI L103 |
| 嵌入维度 | `embedding dimension` | JES L795；BMS L1857；EAI L819 |
| 批量大小 | `batch size` | JES L743；BMS L1389；EAI L2462 |
| 学习率 | `learning rate` | JES L1216；BMS L287；EAI L1274 |
| 估计结果 | `estimation results` | JES L1958；BMS L174；EAI L1380 |
| 随后接 | `followed by` | JES L229；BMS L406；EAI L2463 |
| 汇总于表中 | `are summarized in Table` | JES L1195；BMS L434；EAI L2803 |

共同出现只是领域通用性的参考。专属功能仍按主参考选择：EAI的轻量化表达、BMS的局部—全局融合、JES的HI筛选。不能要求每个准确用词都必须三篇共有。

## 按写作功能联合提取

以下保留原词的大小写和连字符形式；正文可按正常句法处理大小写、单复数。最后一类是句法短搭配，不计作独立技术术语。

### 输入与HI（21项）

| 中文功能/对象 | 原词/短搭配 | 语境出处 | 交叉定位 | 采用边界 |
| --- | --- | --- | --- | --- |
| 放电片段 | `discharge segment` | BMS L445 | BMS L273 | 只在本文实际使用放电片段时采用 |
| 搜索过程 | `search procedures` | BMS L455 | BMS L455 | 描述实际执行的搜索步骤 |
| 逐渐缩小的窗口 | `progressively smaller windows` | BMS L455 | BMS L278 | 要求窗口确实逐步缩小 |
| HI序列 | `HI sequence` | BMS L500 | BMS L500 | 特指HI，不与所有feature sequence无差别轮换 |
| 电池SOH序列 | `battery SOH sequence` | BMS L501 | BMS L501 | 目标序列，不是输入HI |
| 标称容量 | `nominal capacity` | BMS L465 | JES L1296；BMS L405；EAI L276 | 不等于实测初始容量 |
| 运行条件 | `operating conditions` | BMS L433 | JES L116；BMS L37；EAI L97 | 描述实际工况 |
| 电压曲线 | `voltage profile` | EAI L374 | EAI L374 | 指电压随过程变化的曲线 |
| 不同粒度的滑动窗口 | `sliding windows with varying granularities` | EAI L374 | EAI L374 | 要求存在多粒度窗口 |
| 粗粒度窗口 | `Coarse-grained Windows` | EAI L391 | EAI L391 | 只借称谓，不借窗口数值 |
| 细粒度窗口 | `Fine-grained Windows` | EAI L393 | EAI L393 | 与粗粒度相对，按本文定义 |
| 相关性分析 | `Correlation Analysis` | EAI L396 | JES L1005；EAI L396 | 与特征筛选操作区分 |
| 真实SOH | `ground-truth SOH` | EAI L399 | EAI L399 | 指观测或计算标签，不声称无测量误差 |
| 特征提取规则 | `feature extraction rules` | EAI L413 | EAI L413 | 可用于规则确定后的固定应用 |
| 观测窗口 | `observation window` | EAI L414 | EAI L142 | 区别模型输入的序列窗口 |
| 最高绝对PCC | `highest absolute PCC` | EAI L417 | EAI L417 | 不能替代本文PCC/SCC双条件 |
| 充电过程 | `battery charging process` | JES L1578 | JES L1578 | 不扩成充放电过程 |
| 特征曲线 | `characteristic curves` | JES L1579 | JES L330 | 不泛称所有输入序列 |
| 基于相关性的HI筛选 | `correlation-based HI selection` | JES L1843 | JES L1843 | 不继承原文使用全部电池的角色设定 |
| 群体层面的退化模式 | `population-level degradation patterns` | JES L1847 | JES L1847 | 组级描述，不自动证明统计代表性 |
| 共同退化特征 | `common degradation characteristics` | JES L1849 | JES L1849 | 不等于已验证共同物理机制 |

### 预处理与序列（11项）

| 中文功能/对象 | 原词/短搭配 | 语境出处 | 交叉定位 | 采用边界 |
| --- | --- | --- | --- | --- |
| 预处理后的输入序列 | `preprocessed input sequences` | JES L1208 | JES L1208 | 预处理内容按本文 |
| 连续循环 | `consecutive cycles` | JES L1262 | JES L1262 | 要求循环连续 |
| 滑动窗口策略 | `sliding window strategy` | JES L1265 | JES L1265；EAI L227 | 序列窗口，区别HI电压窗口 |
| 序列输入 | `sequential inputs` | JES L1266 | JES L1266 | 按输入形式使用 |
| 固定长度窗口 | `fixed-length window` | JES L1267 | JES L1267 | 要求长度固定 |
| 序列滑动步长 | `sliding stride` | JES L1268 | JES L1268 | 序列域用词；HI窗口搜索已有moving step size |
| 历史循环 | `historical cycles` | JES L1273 | JES L1273 | 不附加初始化辩护 |
| 最小—最大归一化 | `min–max normalization` | JES L1280 | JES L1280 | 拟合统计量的数据范围按本文 |
| 特征间尺度差异 | `scale discrepancies among features` | JES L1281 | JES L1281 | 说明归一化对象 |
| 窗口分段 | `window splitting` | BMS L736 | BMS L736 | 模型输入分段，不是电压窗口搜索 |
| 窗口片段 | `window segment` | BMS L743 | BMS L743 | 用于模型序列窗口 |

### 模型与数据流（39项）

| 中文功能/对象 | 原词/短搭配 | 语境出处 | 交叉定位 | 采用边界 |
| --- | --- | --- | --- | --- |
| 高维空间 | `high-dimensional space` | BMS L737 | JES L614；BMS L737 | 要求存在对应嵌入空间 |
| 可学习权重参数 | `learnable weight parameter` | BMS L728 | BMS L728 | 不新增本文没有的参数 |
| 层归一化 | `layer normalization` | BMS L795 | EAI L853；BMS L795 | 遵循本文LayerNorm缩写 |
| 标准卷积 | `standard convolution` | BMS L764 | JES L740；BMS L36；EAI L2087 | 与DSConv区分 |
| 输入通道 | `input channels` | BMS L769 | JES L744；BMS L769 | 按张量轴定义 |
| 输出通道 | `output channels` | BMS L789 | BMS L789 | 按张量轴定义 |
| 特征图 | `feature map` | BMS L769 | JES L745；BMS L769；EAI L907 | 序列表示不一定适用此名称 |
| 卷积核大小 | `kernel size` | BMS L788 | JES L847；BMS L219；EAI L856 | 区别预测窗口长度 |
| 特征图尺寸 | `feature map size` | BMS L789 | BMS L789 | 不机械替代sequence length |
| 残差连接 | `residual connection` | BMS L811 | JES L587；BMS L811；EAI L824 | 连接端点以本文公式为准 |
| 通道维操作 | `channel-wise operations` | BMS L814 | BMS L814 | 与空间维操作区分 |
| 扩张倍数 | `expansion factor` | BMS L874 | BMS L874 | 原文指通道扩张，不是空洞卷积dilation |
| 特征表示 | `feature representation` | BMS L879 | BMS L879 | 不附加物理解释 |
| 全局感受野 | `global receptive field` | BMS L856 | BMS L856 | 要求实际全局交互范围 |
| 注意力权重 | `attention weights` | BMS L885 | JES L512；BMS L885 | 区别未归一化相似度 |
| 加权和 | `weighted sum` | BMS L888 | JES L513；BMS L888 | 公式确为加权求和 |
| 可学习线性投影 | `learnable linear projection` | BMS L945 | BMS L945 | 原文后接matrices，本文补足真实对象 |
| 相似度函数 | `similarity function` | BMS L947 | BMS L947 | 不随意改称核函数 |
| 矩阵乘法结合律 | `associative property of matrix multiplication` | BMS L970 | BMS L970 | 不据此跳过本文运算等价性检查 |
| 序列长度 | `sequence length` | BMS L1024 | JES L277；BMS L1024；EAI L103 | 区别电压窗口宽度及特征维度 |
| 多尺度特征 | `multi-scale features` | EAI L812 | EAI L812 | 多特征不自动等于多尺度 |
| 数据流 | `data flow` | EAI L815 | EAI L815 | 用于模块输入输出顺序 |
| 输入张量 | `input tensor` | EAI L818 | JES L742；EAI L818 | 张量维度按本文 |
| 特征嵌入维度 | `feature embedding dimension` | EAI L819 | EAI L819 | 不用于原始特征数量 |
| 非线性映射 | `non-linear mapping` | EAI L816 | EAI L816 | 不照搬PIAF结构 |
| 可学习缩放因子 | `learnable scaling factor` | EAI L834 | EAI L834 | 本文确有相应参数才用 |
| 参数冗余 | `parameter redundancy` | EAI L838 | EAI L838 | 存在冗余的判断仍需依据 |
| 核尺度 | `kernel scales` | EAI L840 | EAI L840 | 核大小按本文 |
| 中间特征 | `intermediate feature` | EAI L846 | EAI L846 | 指数据流中间表示 |
| 特征维度 | `feature dimension` | EAI L847 | JES L278；EAI L847 | 与序列长度区分 |
| 置换算子 | `permutation operator` | EAI L847 | EAI L847 | 必要时解释维度置换 |
| 大感受野 | `large receptive field` | EAI L914 | EAI L914 | 大不等于全局覆盖 |
| 序列建模任务 | `sequence modeling tasks` | JES L581 | JES L581 | 任务名称，不引入新任务 |
| 隐状态 | `hidden states` | JES L586 | JES L586 | 区别最终输出 |
| 嵌入层 | `Embedding layer` | JES L613 | JES L613；BMS L288 | 大小写可规范化 |
| 嵌入特征 | `embedded features` | JES L615 | JES L615 | 指嵌入后的表示 |
| 多尺度局部依赖 | `multi-scale local dependencies` | JES L880 | JES L880 | 区别长程依赖 |
| 嵌入维度 | `embedding dimension` | JES L901 | JES L795；BMS L1857；EAI L819 | 与feature embedding dimension按全称简称处理 |
| 通道维度 | `channel dimension` | JES L902 | JES L902 | 按张量轴，不与所有维度互换 |

### 训练与实验（19项）

| 中文功能/对象 | 原词/短搭配 | 语境出处 | 交叉定位 | 采用边界 |
| --- | --- | --- | --- | --- |
| 单次前向传播 | `single forward pass` | BMS L1362 | JES L3802；BMS L1362 | 适合本文单次前向FLOPs口径 |
| 训练超参数 | `training hyperparameters` | BMS L1394 | JES L3905；BMS L1387 | 与结构超参数区别 |
| 模型超参数 | `model hyperparameters` | BMS L1394 | JES L3907；BMS L1348 | 不新增搜索过程 |
| 批量大小 | `batch size` | BMS L1389 | JES L743；BMS L1389；EAI L2462 | 区分训练与测量批量 |
| 学习率 | `learning rate` | BMS L1389 | JES L1216；BMS L287；EAI L1274 | 数值按本文 |
| dropout比率 | `dropout rate` | BMS L1390 | JES L3812；BMS L1390 | 只用于实际dropout设置 |
| 数据驱动超参数搜索 | `data-driven hyperparameter search` | EAI L426 | EAI L426 | 确实执行搜索时采用 |
| 训练稳定性 | `training stability` | EAI L1195 | JES L937；EAI L1195 | 单次低误差不足以证明 |
| 超参数敏感性 | `hyperparameter sensitivity` | EAI L1196 | EAI L1196 | 仅适用于已有对应实验 |
| 初始化策略 | `initialization strategy` | EAI L1234 | EAI L1195 | 不因借词新增自证实验 |
| 收敛行为 | `convergence behavior` | EAI L1234 | EAI L1234 | 需要训练过程证据 |
| 收敛速度 | `convergence speed` | EAI L1302 | JES L996；EAI L1302 | 不能由最终误差推断速度 |
| 训练损失 | `training loss` | EAI L1303 | EAI L1256 | 区别验证误差 |
| 网络深度 | `network depth` | EAI L1335 | EAI L1275 | 按本文层数定义 |
| 训练轮数 | `number of training epochs` | JES L1219 | JES L1219 | 不照抄范文轮数 |
| 超参数调优 | `hyperparameter tuning` | JES L1226 | JES L1226；BMS L176 | 与既定训练操作区分 |
| Adam优化器 | `Adam optimizer` | JES L1282 | JES L1282 | 本文确用Adam才用 |
| 均方误差 | `mean squared error (MSE)` | JES L1282 | JES L1282 | 区别RMSE |
| 基准比较模型 | `benchmark models` | JES L2842 | JES L2842 | 选定后不为避重复与baseline models轮换 |

### 结果与比较（16项）

| 中文功能/对象 | 原词/短搭配 | 语境出处 | 交叉定位 | 采用边界 |
| --- | --- | --- | --- | --- |
| 估计结果 | `estimation results` | BMS L1375 | JES L1958；BMS L174；EAI L1380 | SOH任务优先estimation |
| SOH估计误差 | `SOH estimation errors` | BMS L1409 | EAI L1486；BMS L1409 | 可用于对应表图标题 |
| 突降 | `sudden drops` | BMS L1318 | BMS L1318 | 要求轨迹呈现下降 |
| 突变 | `sudden changes` | BMS L1320 | BMS L1320 | 比突降更宽，不作为同义轮换 |
| 退化轨迹 | `degradation trajectories` | EAI L1381 | JES L2902；EAI L1381 | 轨迹不是抽象依赖 |
| 瞬时下降 | `instantaneous drops` | EAI L1383 | EAI L1383 | 作为参考变体，不与已选sudden drops随意轮换 |
| 局部拐点 | `local knee-points` | EAI L1385 | EAI L1385 | 不能把全部波动称为拐点 |
| 容量恢复（范文变体） | `capacity regeneration` | EAI L1388 | JES L296；EAI L254 | 原词保留作证据；本文已选capacity recovery，不再作为平行首选。不等于普通噪声 |
| 加速老化趋势 | `accelerated aging trends` | EAI L1433 | EAI L261 | 不推断唯一物理机制 |
| 性能增益 | `performance gains` | EAI L1451 | JES L3317；EAI L1149 | 不自动意味着统计显著 |
| 消融研究 | `ablation study` | EAI L1450 | JES L3320；EAI L917 | 移除或替换方案按本文 |
| 实际SOH值 | `actual SOH values` | JES L1983 | JES L1983 | 与ground-truth SOH按同一目标对象统一 |
| 误差分布 | `error distribution` | JES L1985 | JES L1985 | 分布图不等于显著性检验 |
| 平均估计误差 | `average estimation error` | JES L2875 | JES L2875 | 注明平均范围 |
| 最大估计误差 | `maximum estimation error` | JES L2876 | JES L2876 | 不等于最大的单电池MAE |
| 相对降低 | `relative reduction` | JES L3523 | JES L3523 | 区别百分点差，保留比较分母 |

### 操作与句间搭配（14项）

| 中文功能/对象 | 原词/短搭配 | 语境出处 | 交叉定位 | 采用边界 |
| --- | --- | --- | --- | --- |
| 跟踪真实值 | `track the true values` | BMS L1318 | BMS L1318 | 不照抄最高级most accurately |
| 输入到 | `fed into` | BMS L737 | JES L483；BMS L737 | 写清输入对象和模块 |
| 转置回 | `transposed back` | BMS L740 | BMS L740 | 须确有恢复维度操作 |
| 随后接 | `followed by` | BMS L816 | JES L229；BMS L406；EAI L2463 | 按本文真实执行顺序 |
| 可表示为 | `can be expressed as` | BMS L823 | JES L774；BMS L823 | 仅作公式引导 |
| 可写为如下形式 | `can be formulated as follows` | BMS L891 | BMS L891 | 与上一项属于句法选择，非新术语 |
| 从二次降到线性 | `reduced from quadratic to linear` | BMS L971 | BMS L971 | 仅用于已建立的对应复杂度 |
| 作为输入 | `serve as input` | JES L613 | JES L613 | 主谓和单复数随语法调整 |
| 随后输入到 | `are then fed into` | JES L615 | JES L615 | 与fed into为同一动词搭配 |
| 依次经过处理 | `processed sequentially through` | JES L915 | JES L915 | 不改变模块顺序 |
| 汇总于表中 | `are summarized in Table` | JES L1584 | JES L1195；BMS L434；EAI L2803 | 接本文表格引用 |
| 观察到相似趋势 | `Similar trends are observed` | JES L3520 | JES L3520；BMS L437 | 确有跨对象相似趋势才用 |
| 将平均误差从……降低 | `reduces the average error from` | JES L3522 | JES L3522 | 补足from/to及比较对象 |
| 对应……的降幅 | `corresponding to reductions of` | JES L3519 | JES L3519 | 补足指标和相对降低分母 |

## 必须一起控制的细粒度差别

| 容易混用的表达 | 本文采用规则 |
| --- | --- |
| HI sequence / feature sequence | HI序列是特征序列的具体对象；相同对象不为避重复换词 |
| observation window / window size / sequence length | 分别看观测区间、窗口尺度和网络序列长度，先声明电压域/循环域和单位 |
| moving step size / sliding stride | 前者已用于HI电压搜索，后者可用于序列滑动；是分域命名，不是任意轮换 |
| selected HIs / retained HIs / final HI subset | 分清筛选中间状态、所选对象和最终集合 |
| ground-truth SOH / actual SOH values / true values | 同一标签对象正式翻译时确定一种主要称谓；其他原词保留作证据，不轮流替换 |
| feature embedding dimension / embedding dimension | 可按首次全称、后续简称处理；不把原始特征数称作嵌入维度 |
| feature dimension / channel dimension | 按本文张量轴定义，不机械当同义词 |
| sudden drops / instantaneous drops / sudden changes | 突降可优先采用BMS的sudden drops；instantaneous drops保留作参考变体；sudden changes含义更宽 |
| capacity regeneration / capacity recovery | 本文首选capacity recovery，regeneration仅保留范文变体；禁止把普通噪声写成容量恢复 |
| average estimation error / maximum estimation error | 明确逐点、逐电池或跨数据集聚合范围，不互换最大误差与最大MAE |
| benchmark models / baseline models | baseline models并未因出现在此对照中就算本轮原词证据；查清当前稿已有首选后统一 |
| parameter count / training time / single forward pass | 参数量、训练耗时、一次前向运算是不同口径，不合并成未经证明的推理速度结论 |

## 从词库到本文的执行顺序

1. 根据中文段落功能找本库对应组，优先选择对象和含义直接对应的范文原词。
2. 查 `terminology.md` 是否已有首选称谓：已有则复用，不因另一篇也有近义词而替换。
3. 新的核心概念先登记中文、首选词、出处、适用对象及状态；仅做冠词、词形和必要语序调整。
4. 结果动词和短搭配只组织本文已有证据，不继承范文最高级、强因果、统计显著性或硬件结论。
5. 新增条目不授权改正文。仍按原有逐批双语提案与确认流程执行。
