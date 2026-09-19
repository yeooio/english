# 第4章结果分析最终审改基准（2026-09-16）

## 1. 本轮目标

第4章后续审改不再满足于“报告数字 + 总结性能好”。每个核心实验都要完成从**观测结果**到**技术解释**再到**使用含义**的闭环，同时如实保留不利结果和证据边界。

建议采用以下六层分析链，但不要求每一段机械写满六句：

1. **总体事实**：先说明总体排名或整体趋势。
2. **代表性好结果**：选择最能体现实验目的的电池、阶段或指标，而不是重复整张表。
3. **差结果或例外**：明确哪些电池、方向、模块或指标没有领先。
4. **技术解释**：把现象与退化轨迹、输入域差异或模块功能联系起来；只有消融能支持模块作用时才使用较强解释，其他情况用 `is consistent with`、`suggests` 等限定。
5. **实际含义**：回答该结果对跨电池复用、跨域校准、模型配置或资源受限BMS意味着什么。
6. **证据边界**：说明当前实验尚未测量或尚不能推出的内容。

这里的“应用层面”不是泛泛加入 `practical application`，而是把数字变成可执行判断，例如：

- 同一数据域中的新电池能否直接复用已训练模型；
- 跨数据集时是否必须提供目标域数据；
- 数据有限时应优先选择哪个源域；
- 单一卷积尺度是否需要随数据集重新选择；
- 当前复杂度证据支持的是较低前向计算和较小权重存储，还是实际低延迟部署。

## 2. 范文怎样分析模型对比结果

### 2.1 BMSFormer：好结果、差结果和应用意义的完整链条

BMSFormer在模型对比中采用的顺序是：

1. **先看误差分布，而不只看均值。** 它先写CNN-Transformer在Cell1上的IQR接近零，但上下须不对称且存在低值离群点，再用Cell2--Cell8的相似现象说明其稳定性可能不足（PDF第9页；`full.txt:1310--1319`）。这属于“看似不错但仍有问题”的分析。
2. **再写所提模型好在哪里。** 它用更小且更集中的误差分布说明准确性和鲁棒性，并专门分析Cell2和Cell6的突降区段，而不是只说平均指标最好（PDF第9页；`full.txt:1320--1326`）。
3. **明确承认基线的优势。** 在复杂度对比中，它承认LSTM类模型训练时间更低，但同时指出其准确率下降，随后才讨论BMSFormer在准确性与资源之间的权衡（PDF第11页；`full.txt:1670--1679`）。
4. **分析差结果的表现形态。** 在NASA和CALCE曲线中，它分别指出LSTM过度平滑、CNN-LSTM存在局部偏差、Transformer波动较大、CNN-Transformer在特定波动区段仍有偏差（PDF第13--14页；`full.txt:1991--2003, 2328--2338`）。
5. **从表现形态回到结构。** 它将过度平滑与局部特征敏感性不足联系起来，将Transformer波动与局部识别能力联系起来，并将CNN-Transformer的限制与较小卷积核联系起来。
6. **最后落到电池退化行为。** 结论把局部--全局建模和多尺度卷积分别联系到容量短期增长、随机波动和长期衰减趋势，并把资源结果表述为面向资源受限BMS的潜力，而把真实BMS集成与部署留作未来工作（PDF第14页；`full.txt:2340--2353`）。

可学习的表达力度：

- 直接观测：`shows`, `exhibits`, `remains lower`。
- 从结果到解释：`suggests`, `indicating that`, `is consistent with`。
- 应用潜力：`shows potential for ...`，不能在没有硬件测试时写成 `is suitable for real-time deployment`。

不能机械照搬之处：BMSFormer有些结构归因只依据模型间对比，因果力度偏强。本文只有在表4-10和表4-11的受控消融中才能较直接地讨论模块贡献；主模型对比应使用“与该设计目标一致”，不能声称某一结构唯一导致某个结果。

### 2.2 JESSOHRUL：怎样写总体领先和局部失败

JESSOHRUL的模型对比采用“任务定义—曲线表现—量化结果—基线失效方式—应用意义”的路径：

1. 先明确训练电池与测试电池，区分同电池精度和跨电池泛化（PDF第15页；`full.txt:1970--1979`）。
2. 用“最接近真实SOH”“误差分布最接近零轴”“能够跟踪短期容量波动”把三种证据分别对应到拟合程度、误差稳定性和局部变化捕捉（PDF第15页；`full.txt:1980--1990`）。
3. 用跨电池平均降幅概括总体领先，再挑出CNN-Transformer在CS2-35/36有竞争力但在CS2-38明显退化这一例外，从而把“好/差”与电池差异联系起来（PDF第16页；`full.txt:2086--2106`）。
4. 在Oxford结果中，它指出Transformer在训练电池表现较好但其他电池明显下降，LSTM曲线过度平滑且不能识别短期容量增长，由此解释不同模型的失效方式（PDF第20页；`full.txt:2863--2893`）。

可学习的是分析顺序和证据类型，不能照搬其较强结论。它从误差指标直接上升到“保障安全可靠运行”，以及由测试差异直接断言模型“学到了真正有用的信息”，都超过了结果本身能严格支持的范围。本文应改为“有利于”“支持潜在使用”或“表明仍需……”，并保留应用条件。

## 3. 本文模型对比的改进案例

### 3.1 Oxford：必须补写没有全部领先的Cell7和Cell8

当前第96行完整报告了总体平均值和降幅，但只写了领先电池，没有说明Cell7和Cell8的例外。因此最后一句 `good prediction robustness` 缺少限定。建议把这一段改成以下分析路径。

**中文候选：**

> 定量结果表明，MS-AgentNet在Cell2、Cell3、Cell5和Cell6的四项指标上均取得最优结果，并在Cell4上获得最高的$R^2$和最低的RMSE。对Cell2--Cell8取平均后，其$R^2$为0.98379，MAE、MAPE和RMSE分别为0.00524、0.00615和0.00638，四项平均指标均列五种模型首位。与CNN-Transformer、CNN-LSTM、Transformer和LSTM相比，其平均MAE分别降低2.42\%、8.87\%、4.20\%和12.52\%。然而，这种优势并未覆盖每个电池：在Cell7上，CNN-Transformer取得更高的$R^2$和更低的RMSE，而Transformer取得更低的MAE和MAPE；在Cell8上，Transformer的四项指标均优于MS-AgentNet。结合Cell4和Cell6局部变化区段中的跟踪结果，MS-AgentNet的优势主要体现在跨电池平均表现以及复杂退化区段中的整体稳定性，而不是对每个单体电池的绝对领先。这种整体表现支持模型在同一数据域内跨电池复用的潜力，但Cell7和Cell8的结果也表明，面向具体电池使用时仍需关注电池间差异造成的性能变化。

**英文候选：**

> The quantitative results show that MS-AgentNet achieves the best $R^2$, MAE, MAPE, and RMSE on Cell2, Cell3, Cell5, and Cell6, as well as the highest $R^2$ and lowest RMSE on Cell4. Averaged over Cell2--Cell8, its $R^2$ is 0.98379, and its MAE, MAPE, and RMSE are 0.00524, 0.00615, and 0.00638, respectively, ranking first among the five models for all four average metrics. Compared with CNN-Transformer, CNN-LSTM, Transformer, and LSTM, its average MAE is reduced by 2.42\%, 8.87\%, 4.20\%, and 12.52\%, respectively. However, this advantage is not uniform across all cells. On Cell7, CNN-Transformer gives a higher $R^2$ and a lower RMSE, whereas Transformer gives lower MAE and MAPE; on Cell8, Transformer outperforms MS-AgentNet on all four metrics. Together with the tracking results in the locally varying regions of Cell4 and Cell6, these findings indicate that the main advantage of MS-AgentNet lies in its average cross-cell performance and overall stability across different degradation patterns, rather than absolute superiority on every cell. This overall performance supports its potential reuse across cells within the same data domain, while the results on Cell7 and Cell8 show that cell-specific performance variation still needs to be considered in application.

说明：这里不把Cell7/8硬解释成某个模块失效，因为没有针对这两个电池的受控模块证据。应用结论限定为“同一数据域内的潜在复用”，不扩展成跨数据集泛化。

### 3.2 CALCE/MIT：把最佳结果对应到真正困难的退化区段

当前第107--109行已经比Oxford段更接近范文，因为它选择了CX2_38的阶段转变和非线性尾段。还需要在结尾增加“这对什么使用场景有意义”和“不能推出什么”。

**中文候选：**

> MS-AgentNet在六个测试电池中的五个上取得四项指标的最优结果，并在全部六个电池上的四项平均指标中均列首位。尤其是在包含多次阶段转变和非线性退化尾段的CX2_38上，其MAPE为0.037673，较CNN-Transformer和Transformer分别降低59.75\%和51.80\%。这一结果与模型同时建模局部变化和较长时间尺度退化信息的设计目标一致；表4-10和表4-11中完整模型在CX2上的明显改进进一步支持了两个模块互补的解释。不过，该优势仍有明确例外：在MIT/Severson的b3c13上，Transformer的四项指标均略优于MS-AgentNet。因而，结果支持的是跨多种退化场景的总体一致性，不能解释成对每个电池均绝对领先。对于实际SOH监测，模型的优势在退化加速或趋势发生转变、固定平滑趋势较难继续外推的区段尤为明显；但这些结果仍来自离线公开数据集，不能直接等同于在线BMS中的实时性能。

**英文候选：**

> MS-AgentNet achieves the best four metrics on five of the six test cells and ranks first for all four metrics averaged across the six cells. The advantage is particularly evident on CX2\_38, which contains several stage transitions and a nonlinear degradation tail: its MAPE is 0.037673, representing reductions of 59.75\% and 51.80\% relative to CNN-Transformer and Transformer, respectively. This result is consistent with the design goal of jointly modeling local variations and degradation information over longer time scales, and the marked improvement of the full model on CX2 in Tables~4-10 and 4-11 further supports the complementary roles of the two modules. The advantage nevertheless has a clear exception: Transformer is slightly better than MS-AgentNet on all four metrics for MIT/Severson b3c13. The results therefore support overall consistency across diverse degradation scenarios rather than absolute superiority on every cell. For SOH monitoring, the model appears particularly useful in regions where degradation accelerates or changes stage and a smooth trend becomes difficult to extrapolate. The evidence is nevertheless based on offline public datasets and does not directly establish real-time performance in an onboard BMS.

## 4. 范文怎样分析消融实验，以及本文应怎样改

### 4.1 JESSOHRUL的消融链条

JESSOHRUL的消融不是“模块A降低多少、模块B降低多少、完整模型最好”三步结束，而是五步：

1. 先提出结构矛盾：线性注意力提高效率但可能削弱表示能力；标准卷积可补局部信息但增加参数。
2. 定义每个变体在结构上改变了什么。
3. 用单模块变体说明功能：DSConv对应细粒度局部退化，DSCA对应长期依赖和全局趋势。
4. 指出缺失另一个模块时仍受什么限制，而不只说加入模块后变好。
5. 用完整模型跨多个数据集的一致领先说明两者互补，并回到异构电池退化模式（PDF第22--23页；`full.txt:3320--3532`）。

该写法能直接照搬的是“问题—变体—单模块作用—单模块限制—组合互补”的逻辑。其结论不能原样搬到本文，因为JE的单模块变体几乎呈单调改善，而本文M2和M3在部分数据集上会变差。本文的差结果恰好应成为分析重点：它说明单个结构并非普适增益，完整模型的价值是跨数据集一致性。

### 4.2 表4-10：把单模块变差解释为作用条件，而不是回避

**中文候选：**

> 表4-10还表明，两个模块单独使用时的贡献具有明显的数据集依赖性。相较于基础模型M1，多尺度DSConv构成的M2在CX2和Oxford上降低了综合平均误差，但在CS2和MIT上分别由0.0157升至0.0162、由0.0020升至0.0023。仅加入RAA的M3在CS2、CX2和Oxford上取得改进，但在MIT上误差升至0.0026。因此，单独增加局部多尺度特征或跨位置交互都不能保证在所有退化模式上获得一致收益。当两者共同使用时，M4在四个数据集上均取得最低或并列最低的综合平均误差，其中CX2和Oxford相对M1分别降低54.94\%和16.52\%。这种“单模块改进不一致、组合后跨数据集更稳定”的结果支持二者的互补关系：多尺度DSConv补充局部和不同时间尺度的信息，RAA提供跨位置的信息交互，而完整模型减少了仅依赖其中一种信息时对特定数据集的敏感性。对于需要用同一结构处理不同电池数据的场景，完整配置的价值主要在于减少跨数据集性能波动，而不是保证每个单模块在每个数据集上都独立有效。

**英文候选：**

> Table~4-10 also shows that the contribution of each module is dataset-dependent when it is used alone. Relative to the backbone M1, M2 with multi-scale DSConv reduces the combined average error on CX2 and Oxford, but increases it from 0.0157 to 0.0162 on CS2 and from 0.0020 to 0.0023 on MIT. M3 with RAA improves the results on CS2, CX2, and Oxford, but increases the error to 0.0026 on MIT. Thus, adding either local multi-scale features or cross-position interactions alone does not guarantee a consistent gain across all degradation patterns. When the two modules are combined, M4 achieves the lowest or jointly lowest combined average error on all four datasets, including reductions of 54.94\% on CX2 and 16.52\% on Oxford relative to M1. This pattern—dataset-dependent gains from either individual module but more consistent results from their combination—supports their complementary roles: multi-scale DSConv supplies local information at different temporal scales, while RAA enables cross-position information interactions. For a common architecture intended to process different battery datasets, the main value of the complete configuration is therefore its lower performance variation across datasets, rather than universal effectiveness of either module in isolation.

力度说明：`supports their complementary roles`由受控组合消融支持；不要写成 `proves that`。`reduces sensitivity`最好使用“更一致/较低波动”的结果表述，避免声称已直接测得模型敏感度。

### 4.3 表4-11：从卷积尺度结果得出配置意义

**中文候选：**

> 单尺度结果进一步说明，有效的局部感受范围随数据集中的退化模式而变化。长核S31在具有阶段转变和非线性尾段的CX2上相对S0降低21.27\%的综合平均误差，而短核S5在MIT上带来约3.85\%的改进；相反，在CS2和Oxford上，两个单尺度变体均未优于不含卷积的S0。单个卷积尺度因此更像是对特定退化模式的选择，而不是对所有数据集均有效的固定增强。结合两个尺度的SFull在四个数据集上均取得最低综合平均误差，并相对最佳单尺度变体在CX2和MIT上分别进一步降低35.34\%和20.00\%。这表明双尺度配置能够覆盖更不一致的时间模式，有助于在跨数据集使用同一模型结构时减少重新选择卷积尺度的需要。

**英文候选：**

> The single-scale results further show that the effective local receptive range varies with the degradation patterns in each dataset. S31 reduces the combined average error by 21.27\% relative to S0 on CX2, which contains stage transitions and a nonlinear degradation tail, whereas S5 gives an improvement of approximately 3.85\% on MIT. By contrast, neither single-scale variant outperforms S0 on CS2 or Oxford. A single convolutional scale therefore acts as a dataset-dependent choice rather than a uniform enhancement. SFull, which combines both scales, achieves the lowest combined average error on all four datasets and further reduces the error by 35.34\% on CX2 and 20.00\% on MIT relative to the best single-scale variant. These results suggest that the dual-scale configuration covers a broader range of temporal patterns and may reduce the need to select a different convolutional scale when the same architecture is applied across datasets.

边界：`may reduce the need`是配置层面的合理含义；本文没有直接测量超参数搜索成本，因此不能写成“无需针对数据集调参”。

## 5. 复杂度实验：不能只写三个最小值

### 5.1 范文的可用结构与不可照搬内容

JESSOHRUL先把复杂度指标分成前向FLOPs、训练时间、参数量和权重存储，再给出统一配置和两种训练条件，随后按基线逐项比较，最后回到资源受限设备（PDF第24页；`full.txt:3793--3849`）。这个“指标定义—公平条件—优势与代价—部署含义”的顺序可用。

但该段存在不能继承的数值问题：表中所提模型的参数量是6450，而正文写成6.45 million；正文还把11.15 s说成短于LSTM的8.60 s。本文必须以自己的表为准，并明确承认MS-AgentNet的训练时间最长。

BMSFormer在这一点上更值得借鉴：它承认某些LSTM模型训练更快，然后把结论限定为准确性与资源的权衡，而不是宣称所有效率指标都最好。

### 5.2 本文表4-12的完整分析候选

**中文候选：**

> 在统一测试条件下，MS-AgentNet的单次前向计算量为0.045760 M FLOPs，包含4,643个可训练参数，权重存储为27.44 KB，三项均为五种模型中的最低值。与CNN-Transformer相比，其参数量和存储分别降低25.6\%和25.8\%；与LSTM相比，其前向计算量降低50.5\%。这些指标直接对应模型推理时的算术量、需要保存的权重数量和权重文件大小，因此支持其在计算与存储资源受限BMS中的轻量化潜力。然而，MS-AgentNet的训练时间为123.338 s，是五种模型中最长的，而LSTM仅为44.568 s。这说明本文的效率优势集中在前向计算和模型紧凑性，而不包括训练速度。若模型主要在工作站离线训练、随后部署到电池管理设备，这种权衡仍具有实际意义；但当前实验没有测量目标硬件上的推理延迟、峰值运行内存或能耗，因此尚不能据此确认实时嵌入式部署性能。

**英文候选：**

> Under the unified test conditions, MS-AgentNet requires 0.045760 M FLOPs for one forward pass, contains 4,643 trainable parameters, and occupies 27.44 KB for weight storage, all of which are the lowest among the five models. Relative to CNN-Transformer, its parameter count and storage size are reduced by 25.6\% and 25.8\%, respectively, while its forward-pass computation is 50.5\% lower than that of LSTM. These metrics directly describe the arithmetic required for inference, the number of weights to be stored, and the model file size, thereby supporting the model's lightweight potential for BMS with limited computational and storage resources. However, MS-AgentNet has the longest training time, at 123.338 s, whereas LSTM requires only 44.568 s. Its efficiency advantage therefore lies in forward-pass computation and model compactness, rather than training speed. This trade-off remains relevant when the model is trained offline on a workstation and then transferred to a battery management device, but the present experiments do not measure inference latency, peak runtime memory, or energy consumption on target hardware and therefore do not establish real-time embedded performance.

这里“离线训练后部署”是基于训练/推理指标分工的应用解释，不声称本文实际完成了硬件部署。若中文源稿不允许增加这一解释，应先由作者确认后再同步中英文。

## 6. 迁移实验：把数字转化为跨域使用决策

三篇范文没有与本文完全同构的六方向“源域直接测试 + 少样本读出层适配”实验，因此不能硬套某一篇的句子。这里应沿用它们共同的分析方法：同时报告成功和失败方向，解释适用条件，并把结果转化为实际使用策略。

### 6.1 直接迁移与30\%适配

**中文候选：**

> 源域直接测试结果显示，CS2→CX2和CX2→CS2仍获得正的$R^2$（0.8421和0.7847），而涉及Oxford的四个方向均出现负$R^2$。前者表明模型在两个CALCE域之间仍能保留一定的退化趋势表示能力，但CS2→CX2的MAPE仍达到0.3974，因此正的$R^2$并不意味着绝对误差已经足够低或模型已经能够直接使用。后者进一步说明，当材料体系、充放电协议和退化轨迹同时发生较大变化时，直接复用源域模型并不可靠。使用目标域前30\%循环数据更新读出层后，六个方向的MAE、MAPE和RMSE均下降，其中两个CALCE方向的$R^2$提高到0.9566和0.8806；然而，四个涉及Oxford的方向仍为负$R^2$。尤其是CALCE→Oxford的MAE虽相对直接迁移降低86.84\%--87.61\%，负$R^2$仍表明目标域整体变化尚未得到可靠拟合。因此，少样本适配能够修正部分输出映射差异，但较大的相对降幅本身不能证明结果已达到可用水平，30\%目标域数据也仍不足以消除较大的域间偏移。对新电池域的实际使用而言，这些结果支持先评估源域与目标域的匹配程度，并在差异较大时采集目标域早期循环数据进行校准，而不支持将同一源域模型无条件直接部署到任意新数据集。

**英文候选：**

> In the source-only evaluation, CS2→CX2 and CX2→CS2 retain positive $R^2$ values of 0.8421 and 0.7847, whereas all four directions involving Oxford yield negative $R^2$ values. The former results indicate that the model retains some ability to represent degradation trends between the two CALCE domains. However, the MAPE for CS2→CX2 remains as high as 0.3974, so a positive $R^2$ does not mean that the absolute error is already sufficiently low or that the model is ready for direct use. The Oxford-related results further show that direct reuse of a source-domain model is unreliable when battery chemistry, cycling protocol, and degradation trajectory differ substantially. After the readout layer is updated using the first 30\% of the target-domain cycles, MAE, MAPE, and RMSE decrease in all six directions, and $R^2$ increases to 0.9566 and 0.8806 for the two CALCE directions. Nevertheless, $R^2$ remains negative in all four directions involving Oxford. In particular, although MAE decreases by 86.84\%--87.61\% for CALCE→Oxford, the negative $R^2$ values show that the overall target-domain variation is still not fitted reliably. Few-shot adaptation therefore corrects part of the output-mapping mismatch, but a large relative error reduction alone does not establish usable target-domain performance, and 30\% target-domain data are still insufficient to remove the larger domain shift. For use in a new battery domain, these findings support assessing source-target compatibility and calibrating the model with early target-domain cycles when the domains differ substantially, rather than directly applying one source-domain model to any new dataset.

解释边界：CALCE两域同为LCO，而Oxford为混合NCO-LCO，但材料、协议和退化轨迹同时变化，不能把差异唯一归因于化学体系。

### 6.2 适配比例与源域选择

**中文候选：**

> 随目标域数据比例增加，两种源域设置的误差均持续下降，但可达到的适配程度明显不同。以CS2为源域时，$R^2$在50\%适配比例时转为正值，并在70\%时达到0.7650；以CX2为源域时，即使使用70\%的目标域数据，$R^2$仍为-0.1268。与此同时，从30\%增加到50\%所带来的MAE降幅大于从50\%增加到70\%的降幅。这些结果说明，更多目标域数据能够提高适配性能，但数据量并非唯一决定因素，源域选择会影响适配上限和达到可用性能所需的数据量。对于实际校准流程，应同时考虑“选择更匹配的源模型”和“获取多少目标域早期数据”，而不能只通过持续增加目标数据来补偿不合适的源域。

**英文候选：**

> Increasing the amount of target-domain data continuously reduces the errors for both source-domain settings, but the attainable level of adaptation differs markedly. With CS2 as the source domain, $R^2$ becomes positive at an adaptation ratio of 50\% and reaches 0.7650 at 70\%. With CX2 as the source domain, $R^2$ remains negative at -0.1268 even when 70\% of the target-domain data are used. In addition, increasing the ratio from 30\% to 50\% produces a larger MAE reduction than the increase from 50\% to 70\%. These results show that more target-domain observations improve adaptation, but data volume is not the only determinant: source-domain selection affects both the attainable performance and the amount of target data required. A practical calibration procedure should therefore consider both the choice of a compatible source model and the required amount of early target-domain data, rather than relying only on additional target data to compensate for an unsuitable source domain.

## 7. 后续全文修改时的统一写法

后续逐段修改第4章时，以以下问题作为强制检查项：

| 实验类型 | 必须回答的好结果 | 必须回答的差结果 | 模块/技术解释 | 实际使用含义 | 必须保留的边界 |
|---|---|---|---|---|---|
| 模型对比 | 哪些电池、阶段、指标领先 | 哪些电池或指标没有领先；基线在哪里更好 | 主对比只写与设计目标一致；结合消融才加强模块解释 | 同域跨电池复用、复杂退化区段的稳定性 | 不能由公开数据直接推出在线安全或实时部署 |
| 消融 | 完整模型在哪些数据集最一致 | 单模块在哪些数据集变差 | 用受控变体说明局部多尺度与跨位置交互的互补作用 | 是否需要按数据集重新选择结构/尺度 | 不能把相关结果写成唯一因果机制 |
| 复杂度 | FLOPs、参数和存储均最低 | 训练时间最长 | 区分训练、前向计算和权重存储 | 离线训练后在受限设备上使用的潜力 | 未测延迟、运行内存、能耗和硬件部署 |
| 迁移 | 同类域方向和适配后的改善 | Oxford方向负$R^2$、适配后仍失败 | 域差异与源域匹配；不把原因归于单一化学因素 | 新域需要校准、选择源模型、确定数据量 | 少样本适配不等于任意跨域泛化 |

句式上优先采用以下推进，而不是堆叠百分比：

> overall result → representative difficult case → exception or failure → evidence-bounded explanation → application decision → limitation

同一段中数字应服务于判断。通常保留一个总体结果、一个最有代表性的好案例和一个关键例外即可，其余完整数值由表格承担。

## 8. 本轮结论

当前第4章并非“完全没有应用分析”，而是不同实验完成程度不一致：

- CALCE/MIT模型对比和多尺度消融已经出现“退化行为—结果”的联系，可在此基础上补应用含义和证据边界。
- Oxford模型对比缺少Cell7/8的例外，导致结论显得只报好结果。
- 模块消融已经承认单模块不能在所有数据集上改进，但尚未把这个差结果转化为“完整配置降低跨数据集波动”的核心价值。
- 复杂度段报告了LSTM更快，却没有明确写出MS-AgentNet训练时间最长，也没有把可支持的推理侧优势与未测的硬件性能分开。
- 迁移实验目前最接近“堆数字”：已经报告负$R^2$和适配改善，但还需要明确写出直接复用何时失败、目标域校准何时仍不足、源域选择如何影响所需数据量。

后续修改应优先把上述四类示范打磨为作者认可的最终版本，再按同一分析链检查其余结果段。中文新增分析需先确认，然后同步英文；不在英文中单独增加中文源稿没有的实质性结论。
