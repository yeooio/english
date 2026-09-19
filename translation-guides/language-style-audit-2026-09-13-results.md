# 英文语言与三篇范文风格审校：第4–5章

2026-09-13，新阶段独立报告。按照最新AGENTS，本轮以英文语言和六层风格审校为主，不重新回译。只提出建议，正文未改。

已通读当前英文摘要及第1–5章，并在本批重新读取三篇范文相应TXT上下文。第4章132行使用当前`With CS2...`版本；不沿用旧反向回译报告中的`Using...`。之前RAA held fixed和battery chemistries的交叉复核结论保留：分别为语境可接受/可选进一步明确，不重新列为确定误译。

本批覆盖47个自然段、14个小节标题及5个纯公式。列出7项段落级候选，其中6项建议、1项明确可选，另40段明确保留；7项均提供现有完整段与候选完整段。所有候选仍为一个连续自然段，没有删掉数字、条件、比较对象或源稿事实。是否更长或更短不能代替直接性判断。

## 本批重新阅读的范文证据

| ID | 论文与TXT位置 | 已读完整上下文及所用层级 |
|---|---|---|
| J-HI | JESSOHRUL/full.txt:1946–1959 | 完整单项/Fusion输入实验段。借具体对象→选择/输入动作，保持本文HI编号及协议；不模仿其首句长目的语和大写The错误。 |
| J-A | JESSOHRUL/full.txt:3498–3532 | 完整消融结果各段，含3512–3514换行续句。指标→数值→比较对象；不继承significantly/superior或其机制因果解释。 |
| J-C | JESSOHRUL/full.txt:3793–3808 | 完整复杂度导语与计量段。FLOPs/单次前向、训练时间、参数与权重存储分别计量；不添加范文使用的不同库或硬件含义。 |
| B-C | BMSFormer/full.txt:1344–1351 | 完整效率比较导语，训练/模型参数的配置与比较目的。范文首句it is important并不自动更优，不复制其自证公平句。 |
| B-D | BMSFormer/full.txt:814–817 | 完整DSConv操作引导句，已回看source.pdf第7页确认与前后公式和双栏的关系。模块直接作主语、separates明确动作；不把范文2D结构套入本文。 |
| E-A | Engineering-AI/full.txt:2077–2090 | 完整组件导语及首条比较，卷积位置→功能→替换结果。这里的标准卷积替换与本文消融加/删操作不同。 |
| E-C | Engineering-AI/full.txt:2839–2841＋2806–2824 | 结论首段跨栏错序，已回看source.pdf第20页：先左下Conclusion首句，接右栏direct measurement...，随后方法段与资源结果完整段。借框架→对象→方法以及资源量表达，不借硬件已实现主张。 |

PDF核对图保存于`build/eai-results-style-page20.png`及`build/bms-results-style-page7.png`。这些页面仅用于确认范文阅读顺序，不是论文正文修改。以下每项短引为准确原文，中文解释为助手释义。建议句为本文适配，未冒充范文原句。

## 7项候选：6项建议与1项可选

### C04-L041：词汇简单但表达绕：主干后置及抽象名词层叠

位置：`chapters/chapter04.tex:41`。

现有英文：

```tex
To evaluate the effectiveness of group-level HI selection in identifying inputs that remain stable across cells, this section compares SOH estimation performance with different HIs on the Oxford dataset. Based on the PCC and SCC of candidate HIs on Cell1, the indicator with the highest combined correlation score is selected from each of the IC, DTV, and DTC categories, giving HI4, HI9, and HI11, respectively. All three combined correlation scores exceed 0.94. These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet. The input combining HI1, HI4, HI9, and HI11 is denoted as Fusion. The SOH estimation results for Cell2--Cell8 with different inputs are given in \cref{tab:4-hi-input}.
```

建议英文：

```tex
This section evaluates whether group-level HI selection identifies stable inputs across cells by comparing SOH estimation performance with different HIs on the Oxford dataset. Based on the PCC and SCC of candidate HIs on Cell1, the indicator with the highest combined correlation score is selected from each of the IC, DTV, and DTC categories, giving HI4, HI9, and HI11, respectively. All three combined correlation scores exceed 0.94. These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet. The input combining HI1, HI4, HI9, and HI11 is denoted as Fusion. The SOH estimation results for Cell2--Cell8 with different inputs are given in \cref{tab:4-hi-input}.
```

范文依据：JESSOHRUL/full.txt:1946–1959，HI输入对照完整段；短引1952–1953：`only one feature is selected from each type of curve`（助手释义：每类曲线仅选一项特征）。

简短中文原因：保留评价目的→比较方式的逻辑，去掉effectiveness of ... in identifying这一名词套层，让evaluates与identifies直接交代审查动作和对象。范文该段首句也有长目的语和不够自然的写法，不能机械复制；借用其随后明确交代选择对象和操作的方式。

六层复查：术语：group-level HI selection、SOH、HI保留；搭配：evaluate whether、identify inputs直接；主干：This section evaluates提前；推进：仍先引出验证，再列特征及Fusion；颗粒度：Oxford、跨电池稳定性及比较方式完整；力度：仍为评价问题，未改为成功结论。

### C04-L065：明确可选——展开统计量与数值配对，原句可保留

位置：`chapters/chapter04.tex:65`。

现有英文：

```tex
Model convergence is evaluated through both convergence speed and loss fluctuations in the late training stage. The convergence threshold epoch is defined as the first epoch at which the training loss falls below 10\% of the first-epoch loss. The mean and standard deviation of the loss over the final 20 epochs describe the late-stage convergence state. As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$. These results show that MS-AgentNet converges stably under the current experimental settings, with small loss fluctuations in the late training stage.
```

建议英文：

```tex
Model convergence is evaluated through both convergence speed and loss fluctuations in the late training stage. The convergence threshold epoch is defined as the first epoch at which the training loss falls below 10\% of the first-epoch loss. The mean and standard deviation of the loss over the final 20 epochs describe the late-stage convergence state. As shown in \cref{tab:4-3}, every training run reaches the predefined threshold. The convergence threshold epoch has a median of 26 on Oxford and 7 on MIT. The median standard deviations of the loss in the late training stage are $2.38\times10^{-4}$ on Oxford and $4.84\times10^{-6}$ on MIT. These results show that MS-AgentNet converges stably under the current experimental settings, with small loss fluctuations in the late training stage.
```

范文依据：JESSOHRUL/full.txt:3518–3525，两个连续数值结果段；短引3521–3522：`the proposed method reduces the average error from 0.0322 (M1) to 0.0207`（助手释义：所提方法将平均误差从0.0322降至0.0207）。

简短中文原因：交叉复核后降为明确可选。两项统计量已在前文定义，当前连续名词修饰在本段语境中可解，不构成必须修复的“表达绕”。候选仅展开指标与数值配对，属于呈现偏好；原句可以保留。范文依据只展示直接报告指标和数值的方式，不能证明本文原句有缺陷。

六层复查：术语：convergence threshold epoch、standard deviation不换名；搭配：has a median of准确；主干：指标直接作主语；推进：阈值→后期波动不变；颗粒度：两域、全部数值和先前定义的首轮10%/最后20轮完整；力度：当前实验设置下收敛的限制不变。

### C04-L073：词汇简单但表达绕：范围短语关联不直接

位置：`chapters/chapter04.tex:73`。

现有英文：

```tex
The main hyperparameters of MS-AgentNet are the learning rate, network depth $L$, and embedding dimension $d$. Their configuration ranges are listed in \cref{tab:4-1}. Within these ranges, two cells in the feature-development set of each dataset are used for model training and configuration: one for learning model parameters and the other for hyperparameter selection. The training and configuration-selection cells are Cell1 and Cell2 for Oxford, CS2\_36 and CS2\_37 for CALCE CS2, CX2\_36 and CX2\_37 for CALCE CX2, and b3c8 and b3c13 for MIT/Severson, respectively.
```

建议英文：

```tex
The main hyperparameters of MS-AgentNet are the learning rate, network depth $L$, and embedding dimension $d$. Their configuration ranges are listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges. The training and configuration-selection cells are Cell1 and Cell2 for Oxford, CS2\_36 and CS2\_37 for CALCE CS2, CX2\_36 and CX2\_37 for CALCE CX2, and b3c8 and b3c13 for MIT/Severson, respectively.
```

范文依据：BMSFormer/full.txt:1344–1351，完整效率比较导语；短引1348–1349：`training and model hyperparameters are set to evaluate the comprehensive performance of different models`（助手释义：设置训练和模型超参数以评价不同模型的综合性能）。JESSOHRUL/full.txt:1946–1959重新核对输入实验角色。

简短中文原因：当前Within these ranges紧邻two cells，要读到句末才知道范围约束的是超参数；将范围直接放到select hyperparameters后，并把learning/selection恢复为learn/select。只使关系明确，不将配置电池改称独立验证或测试电池。

六层复查：术语：feature-development、configuration-selection等既定角色保留；搭配：learn parameters/select hyperparameters直接；主干：one cell ... a second并列；推进：参数范围→两池分工→四组编号不变；颗粒度：两节电池及全部映射不删；力度：未增添独立测试/公平性证明。

### C04-L149：词汇简单但表达绕：模块动作被名词化

位置：`chapters/chapter04.tex:149`。

现有英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref31,ref71}. To combine local information preservation with computational efficiency, MS-AgentNet integrates multi-scale DSConv and RAA for local feature extraction and cross-position information interactions, respectively. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

建议英文：

```tex
Efficient attention reduces the computational overhead of standard attention by compressing information interactions\cite{ref39,ref40,ref43,ref44}, but this process may weaken the representation of fine-grained local degradation information\cite{ref31}. Directly adding standard convolutions can improve local feature modeling but increases the parameter count and computational load\cite{ref31,ref71}. To preserve local information while maintaining computational efficiency, MS-AgentNet integrates multi-scale DSConv to extract local features and RAA to enable cross-position information interactions. Four variants, M1–M4, are used to examine their individual and combined effects. M1 retains only the basic backbone, M2 adds multi-scale DSConv to M1, M3 adds RAA to M1, and M4 integrates both multi-scale DSConv and RAA.
```

范文依据：BMSFormer/full.txt:814–817，完整DSConv操作说明（已回看PDF第7页确认段序）；短引814：`DSConv separates the spatial and channel-wise operations`（助手释义：DSConv将空间操作与通道操作分开）。Engineering-AI/full.txt:2080–2090完整组件作用导语与首条结果，短引2082–2083：`post-fusion refinement`（融合后细化）。

简短中文原因：将local information preservation和for local feature extraction改成preserve与extract，两个模块分别紧邻各自动作；读者无需读到respectively才回配角色。保留information interactions这一既定技术表达，避免擅改成另一机制。

六层复查：术语：MS-AgentNet、multi-scale DSConv、RAA及cross-position information interactions一致；搭配：extract local features与enable interactions直接；主干：模块→动词→对象；推进：代价问题→组合设计→消融定义不变；颗粒度：两模块作用与效率目的均保留；力度：原句may、标准卷积代价及后续不利结果不变。

### C04-L166：词汇简单但表达绕：三项被动操作共用一个不精确主语

位置：`chapters/chapter04.tex:166`。

现有英文：

```tex
In practical applications, computational efficiency and storage requirements are important evaluation criteria alongside estimation accuracy\cite{ref77}. This study compares the resource overhead of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM using four metrics: FLOPs, training time, trainable parameter count, and weight storage size. FLOPs are measured using the \texttt{profile} function in the THOP library, supplemented with attention operations, and converted to the number of floating-point operations required for a single forward pass. Training time is recorded in seconds using Python's \texttt{time} module and represents the time needed to complete the specified number of training epochs. The total number of trainable parameters is counted using PyTorch. Weight storage size is measured using Python's \texttt{os.path.getsize} function and converted to KB, representing the space required to save the model weights. All metrics are measured in the same experimental environment.
```

建议英文：

```tex
In practical applications, computational efficiency and storage requirements are important evaluation criteria alongside estimation accuracy\cite{ref77}. This study compares the resource overhead of MS-AgentNet, CNN-Transformer, CNN-LSTM, Transformer, and LSTM using four metrics: FLOPs, training time, trainable parameter count, and weight storage size. FLOPs are measured using the \texttt{profile} function in the THOP library. After attention operations are added to the count, the result is converted to the number of floating-point operations required for a single forward pass. Training time is recorded in seconds using Python's \texttt{time} module and represents the time needed to complete the specified number of training epochs. The total number of trainable parameters is counted using PyTorch. Weight storage size is measured using Python's \texttt{os.path.getsize} function and converted to KB, representing the space required to save the model weights. All metrics are measured in the same experimental environment.
```

范文依据：JESSOHRUL/full.txt:3799–3808，完整计量方法段；短引3801–3802：`quantify the floating-point operations required for a single forward pass`（助手释义：量化单次前向传播所需的浮点运算次数）。BMSFormer/full.txt:1344–1351完整资源比较导语。

简短中文原因：现句将测量、补计、换算全挂在FLOPs上，supplemented和converted指代需回读；建议明确补充的是计数，换算的是补计后的结果。三个步骤顺序保持，仅在同一自然段内分句。范文不含本文注意力补计步骤，不能为模仿其短句删去该步骤。

六层复查：术语：FLOPs、THOP/profile和single forward pass保留；搭配：add ... to the count明确；主干：measurement→count→result；推进：原三步骤次序不变；颗粒度：注意力补计与换算均保留，其余计量段原样；力度：未把FLOPs换作耗时或推理延迟。

### C04-L170：用词搭配与直接性：has FLOPs混合不同量的关系

位置：`chapters/chapter04.tex:170`。

现有英文：

```tex
Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low. In contrast, MS-AgentNet has FLOPs, parameter count, and storage size of 0.045760 M, 4,643, and 27.44 KB, respectively, the lowest among all five models. It reduces forward-pass computation by 50.5\% compared with LSTM. Its parameter count and storage size are reduced by 25.6\% and 25.8\% compared with CNN-Transformer and by 70.8\% and 59.8\% compared with CNN-LSTM, respectively. These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.
```

建议英文：

```tex
Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low. In contrast, MS-AgentNet requires 0.045760 M FLOPs, has a parameter count of 4,643, and uses 27.44 KB to store its weights; all three values are the lowest among the five models. It reduces forward-pass computation by 50.5\% compared with LSTM. Its parameter count and storage size are reduced by 25.6\% and 25.8\% compared with CNN-Transformer and by 70.8\% and 59.8\% compared with CNN-LSTM, respectively. These results show that MS-AgentNet maintains high SOH estimation accuracy with lower forward-pass computation, parameter count, and weight storage overhead.
```

范文依据：Engineering-AI/full.txt:2816–2824完整结果段（已回看PDF第20页）；短引2821：`a parameter count of only 6114 and a storage footprint of`（助手释义：参数量仅6114，存储占用为……）。JESSOHRUL/full.txt:3799–3808完整计量段，短引3807–3808：`the space required to store model parameters`（存储模型参数所需空间）。

简短中文原因：分别使用requires计算量、has参数量和uses权重存储，让三个数紧邻所属指标，避免has FLOPs和跨三项respectively回配。沿用本文parameter count，不为照搬范文而把storage size全篇换成storage footprint。

六层复查：术语：参数量与权重存储对象保持；搭配：requires FLOPs/has a parameter count更明确；主干：MS-AgentNet的三个并列动词；推进：LSTM训练时间反例→本模型资源优势→降低率不变；颗粒度：三值、单位和五模型范围完整；力度：未暗示训练/推理最快。

### C05-L001：词汇简单但表达绕——仅将尾句聚合与广播恢复为动词

位置：`chapters/chapter05.tex:1`。

现有英文：

```tex
This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-limited battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset. For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales. With a fixed number of agents, RAA uses a small number of static learnable agents for information aggregation and broadcasting, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.
```

建议英文：

```tex
This study proposes a lightweight lithium-ion battery SOH estimation framework for resource-limited battery management systems to address limited cross-cell HI stability and the difficulty of balancing prediction accuracy with computational efficiency. The study focuses on systematic HI construction and lightweight network design. The proposed multi-source health indicator extraction and optimization algorithm first constructs multiple types of candidate HIs from charging and discharging data and their derived curves. Based on correlations on the feature-development cell set, MS-CCCT then adaptively calibrates the constant-current charging voltage window at multiple scales, and PCC/SCC dual-threshold admission and redundancy removal determine the model inputs. With feature definitions and parameters held fixed, the selected HIs retain strong linear and monotonic relationships with SOH on other cells within the same dataset. For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to jointly represent local degradation variations, global information across positions, and degradation trends over longer time scales. With a fixed number of agents, RAA uses a small number of static learnable agents to aggregate and broadcast information, reducing the theoretical complexity of attention-based correlation interactions from $O(N^2d)$ to $O(Nn_a d)$.
```

范文依据：Engineering-AI/full.txt:2839–2841、2806–2824，已回看PDF第20页恢复完整结论段序；短引2840–2841：`This study presents a practical, computationally efficient framework for battery SOH estimation`（助手释义：本研究提出一个实用且计算高效的电池SOH估计框架）。BMSFormer/full.txt:814–817完整模块操作说明，短引814：`DSConv separates the spatial and channel-wise operations`。

简短中文原因：原首句主干This study proposes靠前，应用对象与研究目的层级清楚，保持原句，不拆成额外It句。建议仅将尾句for information aggregation and broadcasting改为to aggregate and broadcast information，使RAA通过智能体执行的动作更直接；不改变机制、信息顺序或结论细节。

六层复查：术语：框架全名、RAA及其余既定术语不变；搭配：aggregate/broadcast information对应实际作用；主干：仅尾句RAA的动作改用动词；推进：首句及其余句子原样，信息顺序完全保持；颗粒度：全部条件、同数据集范围和复杂度式完整；力度：fixed number、theoretical及强关联条件不变。

## 保留覆盖记录

下列每段均检查了术语、动词搭配、句子主干、句间推进、信息颗粒度及力度。保留不表示逐句照抄范文，而表示未发现值得在当前授权内修改的直接性或搭配缺陷。当前已有show/indicate、only、may、in-domain、potential等按真实语义保留；不新增absolutely/definitely/demonstrate。

| 位置 | 结论与理由 |
|---|---|
| C04-L001 | 保留。研究任务逐项展开、每句主语清楚；首尾评价范围是原稿信息，不能仅为减少重复删除。 |
| C04-L005 | 保留。四指标直接列出，全称必要；无绕行。 |
| C04-L007 | 保留。MAE定义→对大误差的性质，推进直接。 |
| C04-L009 | 保留。归一化对象与接近零条件清楚，may保留。 |
| C04-L011 | 保留。RMSE定义→与MAE区别，虽含名词但数学定义需要。 |
| C04-L013 | 保留。fits variations主干直接，1的方向明确。 |
| C04-L015 | 保留。简短公式引导，保留。 |
| C04-L037 | 保留。符号解释虽有并列但指向清楚，保留。 |
| C04-L043 | 保留。HI1表现→三均值→Fusion反例，顺序自然。 |
| C04-L045 | 保留。差异→Cell7/8例子→HI1→边界结论，指代清楚。 |
| C04-L050 | 保留。目的引导略长但三项分析对象清楚，没有多层回绕；保留。 |
| C04-L054 | 保留。静态可学习及与输入无关的条件紧邻矩阵，保留。 |
| C04-L061 | 保留。参数符号及初始化结果直接。nonidentical/identical有重复，但分别表达参数和状态，非本轮必要修复。 |
| C04-L063 | 保留。三初始化策略对比完整。ordinary normal略累赘属于可选词汇压缩，不再单列为必要语言缺陷。 |
| C04-L075 | 保留。表格引导简单直接，保留。 |
| C04-L079 | 保留。配置选定→固定→具体值；已直接。 |
| C04-L085 | 保留。数据集/HI映射→比较目的清楚，passive comparison不是自动判绕的理由。 |
| C04-L090 | 保留。图表主语直接引出模型与结果，保留。 |
| C04-L094 | 保留。各模型趋势→代表区间→平滑电池；track/follow搭配匹配对象。 |
| C04-L096 | 保留。长降低率句信息量大，但中文原有三个指标×四基线，不为短句删除；对象和respectively可解，保留。 |
| C04-L103 | 保留。数据集→差异→图，跨池与跨域含义未混淆。 |
| C04-L105 | 保留。主干直接，nonlinear degradation tail是源稿形象表达；本轮不凭未找到完全同词就强换成更窄现象。 |
| C04-L107 | 保留。数值主张清楚；旧审查中的末期证据范围问题仍属科学核实，语言审校不通过换show来偷改结论。 |
| C04-L109 | 保留。已有批准average修复保留。数值密集是源稿颗粒度，不能当纯赘述删除。 |
| C04-L117 | 保留。四句依次定义域偏移、两任务及各协议，限定准确，保留。 |
| C04-L119 | 保留。域→电池角色→化学体系→一致输入，清楚；公式是必要技术内容。 |
| C04-L123 | 保留。两CALCE结果→Oxford对照与范围，虽第一句较长但主干和数量对应清楚。 |
| C04-L125 | 保留。六方向结果→MAE分组→R²限制，直接且完整。 |
| C04-L132 | 保留。当前为With CS2_36 and CX2_36 used ...，已无此前Using修饰错误；协议句可读，保留。 |
| C04-L135 | 保留。源域分别报告起止值与50%转正，前置条件必要，不强行压缩。 |
| C04-L137 | 保留。相邻比例→差值缩小→同率源域结论，指代可解。 |
| C04-L145 | 保留。首句目的内容与后两类功能对应；有轻度名词化但结构清楚，修复收益不足以要求改写。 |
| C04-L152 | 保留。加入DSConv/RAA→部分域改善→反例完整，主干已直接。 |
| C04-L154 | 保留。完整模块→具体下降→CS2 MAE反例→互补结论，保留。 |
| C04-L156 | 保留。RAA is held fixed在四变体上下文可接受；如日后需强调仅结构可再明确，不当作已确定误译。 |
| C04-L158 | 保留。单尺度异质性→四组结果→全尺度结果，复杂信息有明确对象；is consistent with保持审慎。 |
| C04-L168 | 保留。统一实验设置并列准确，4头与4层数值相同的解释为源稿事实，不能删。 |
| C04-L172 | 保留。宽度设置→四值范围→代表值→部署潜力，已有lower than that of修复保留。 |
| C05-L003 | 保留。框架总体表现→CX2两池平均MAPE→资源→消融→域内泛化与潜力，主干清楚；已有平均MAPE批准修复保留。信息重复仍承载原稿结论，不自行删减。 |
| C05-L005 | 保留。依赖片段→跨域影响因素→未来HI/域适应→验证方向，顺序明确。battery chemistries在当前材料体系语境可接受，不当已确定漏译；未来验证未改成已完成。 |

14个标题全部保留：

| 行 | 当前标题 | 结论 |
|---|---|---|
| 3 | `\subsection{Evaluation metrics}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 39 | `\subsection{HI selection results and effectiveness analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 48 | `\subsection{Training robustness and hyperparameter analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 52 | `\subsubsection{Agent matrix initialization and convergence analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 71 | `\subsubsection{Hyperparameter configuration}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 83 | `\subsection{Comparison of SOH estimation accuracy and cross-cell generalization}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 88 | `\subsubsection{Estimation accuracy on the Oxford dataset}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 101 | `\subsubsection{Cross-cell generalization on the CALCE and MIT datasets}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 115 | `\subsection{Cross-dataset transfer experiments}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 121 | `\subsubsection{Performance across transfer directions}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 130 | `\subsubsection{Effect of the target-domain adaptation ratio}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 143 | `\subsection{Module ablation and model complexity analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 147 | `\subsubsection{Module ablation analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |
| 164 | `\subsubsection{Model complexity analysis}` | 保留，名词短语与节内功能相符，没有新添绝对性评价。 |

第4章第17、22、27、32、56行起的5个公式保持；纯数学表达不做英语风格替换，相邻定义与解释段已计入47段。章节引用与结构命令保持。

## 提交前复查

- 直接性：改变的是主干、名词化关系或指标与数值的配对，不以改动数、难词数或固定句长衡量。
- 信息及力度：7个候选段所有原有数值、数学内容、引用键与模型/电池范围保留；第5章首句原样保留，只在尾句将聚合与广播改用动词。
- 术语：既定HI选择、配置电池、RAA、参数量、权重存储术语保持；不因参考来源不同换成另一套词汇。
- 段落及推进：所有建议保持一段；句内展开没有调整章节论证次序，没有删改证据边界或不利结果。
- 范文：短引来自本批实际重读的完整上下文；被双栏错序影响的B-D/E-C已回PDF；不把范文本身生硬或夸大写法列为必须学习的目标。
