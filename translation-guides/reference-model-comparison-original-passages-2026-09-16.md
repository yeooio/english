# 三篇范文模型对比实验原文汇编（2026-09-16）

## 使用说明

本文件汇集三篇范文中直接承担“模型对比结果分析”功能的英文原段落。表格中的全部数值和图题不重复抄录；实验设置、曲线解释、具体电池解释、平均结果与基线失效分析均保留。双栏TXT出现错序时，已依据PDF页面恢复阅读顺序。每个原文块后附“对象核对”，用于回答作者关心的：范文是否分析了具体电池，还是只报告平均结果。

---

## 1. BMSFormer

来源：BMSFormer PDF第9页，Oxford模型对比；`full.txt:1309--1326`。

### 1.1 Oxford原文

> As shown in the figure, in the validation results for Cell1, CNN-Transformer’s estimation error IQR is close to zero. However, the asymmetry in the whiskers of the boxplot indicates a greater number of low outliers in the estimation results. This trend is also observed from Cell2 to Cell8, suggesting that the model’s estimation stability may be insufficient. The boxplot of prediction errors and the normal distribution plot across the eight batteries clearly show that BMSFormer has smaller and more concentrated prediction errors, illustrating superior prediction accuracy and robustness.
>
> Notably, in Cells 2 and 6, where there are several sudden drops, CNN-Transformer and BMSFormer were able to track the true values most accurately, with BMSFormer showing the smallest prediction errors in response to sudden changes in Cell6. For the other six batteries with relatively stable SOH changes (excluding Cell3 and Cell8), BMSFormer performed the best and ranked first in the mean prediction results across all eight batteries, showing improvements in the average MAE of 14.81%, 59.65%, 46.51%, 73.56%, the average RMSE of 16.21%, 62.19%, 44.64%, and 73.27%, and the average MAPE of 20.00%, 63.63%, 50.00%, 76.32% compared to CNN-Transformer, Transformer, CNN-LSTM, and LSTM, respectively.

### 1.2 Oxford对象核对

BMSFormer不是只报告八电池平均值。它明确分析了：

- **Cell1**：分析的是CNN-Transformer误差箱线图的IQR、须线不对称和低值离群点；
- **Cell2和Cell6**：分析突然下降，并承认CNN-Transformer和BMSFormer都能跟踪；
- **Cell6**：进一步指出BMSFormer在突然变化处误差最小；
- **Cell2--Cell8整体**：用箱线图趋势讨论稳定性；
- **八电池平均值**：最后才报告平均MAE、RMSE、MAPE降幅。

原文存在一个逻辑问题：`the other six batteries`按前句应排除Cell2和Cell6，但括号却写`excluding Cell3 and Cell8`。这不能作为严谨句式照搬。

### 1.3 NASA/CALCE泛化原文

来源：BMSFormer PDF第12--14页；`full.txt:1906--1920, 1991--2003`。原文被图10跨页分开，以下按句子连续关系合并。

> This section presents and compares the testing results obtained through the process of directly testing on the unseen test sets using the five optimal models with highest validation accuracies.
>
> As illustrated in Fig. 10 (a)-(c), the estimated SOH of BMSFormer is generally closer to the true SOH compared to other models, and the estimation error is also closer to zero, both indicating higher accuracy. The localized magnifications in the ‘SOH’ plots further illustrate the better stability of BMSFormer when encountering sudden SOH changes in the degradation process of ten batteries.
>
> As detailed in Table 9, BMSFormer achieves improvements of 37.15%, 42.65%, 23.67%, and 47.90% in average MAE, 27.30%, 48.20%, 20.42%, and 53.71% in average MAPE, and 34.29%, 40.69%, 18.84%, and 46.29% in average RMSE, compared to CNN-Transformer, CNN-LSTM, Transformer, and LSTM, respectively, across eight battery cells from NASA and CALCE datasets. Notably, the zoomed-in prediction curves reveal that BMSFormer performs exceptionally well even in scenarios with the most severe SOH fluctuations, such as those observed in B0018 and CS2-38.
>
> LSTM still exhibits the lowest prediction accuracy due to insufficient sensitivity to local features. Although CNN-LSTM partially addresses this issue, it still suffers from structural limitations, resulting in the loss of important information after convolution processing. Transformer also struggles with local feature recognition, leading to larger fluctuations in error curves and particularly noticeable deviations in B0005. CNN-Transformer and BMSFormer show similar performance, but CNN-Transformer’s small convolution kernel size of 1 × 3 and the lack of feature diversity constrain its ability to identify complex features pattern, resulting in slightly lower prediction accuracy compared to BMSFormer. Increasing the convolution kernel size in CNN-Transformer may improve its ability to extract local features, but this will also increase computational costs.

### 1.4 NASA/CALCE对象核对

这部分也不是只报平均值：

- 先明确是直接测试**未见测试集**；
- 用全部曲线概括预测是否接近真实值、误差是否接近零；
- 用局部放大图讨论突然SOH变化；
- 点名**B0018和CS2-38**作为波动最严重的场景；
- 点名**B0005**说明Transformer误差波动明显；
- 最后分别解释LSTM、CNN-LSTM、Transformer和CNN-Transformer的差异。

其中`due to`、`resulting in`等结构因果判断主要来自模型对比而非受控消融，力度偏强。本文不能原样照搬这种因果强度。

---

## 2. JESSOHRUL

### 2.1 CS2实验身份与图形分析原文

来源：JESSOHRUL PDF第15页；`full.txt:1970--1990`。

> To verify the effectiveness of the proposed model across different electrode materials and charge–discharge rates, additional experiments were conducted on the CS2 batteries. In particular, the CS2–35 cell was employed for model training and validation, where the first 30% of the cycle data were used for training and the remaining 70% for validation. This setup ensures that the model is evaluated on unseen data from the same cell. Furthermore, to assess the generalization capability and robustness of the model, the trained network was tested on three additional cells under identical operating conditions. This experimental design enables comprehensive verification of both within-cell prediction accuracy and cross-cell generalization performance.
>
> As illustrated in Fig. 8, the proposed model achieves the closest fit to the actual SOH values across the four CS2-series cells, which is of considerable importance for practical applications. Moreover, the boxplots in the upper-right corner reveal that the error distribution of the proposed model lies closest to the zero axis, indicating its superior predictive performance during the experiments. The detailed subfigures further demonstrate the model's ability to effectively capture short-term capacity fluctuations. These results highlight the strong predictive accuracy and generalization capability of the proposed model.

### 2.2 CS2表格和基线分析原文

来源：JESSOHRUL PDF第16--17页；`full.txt:2086--2106, 2524--2526`。最后一句被双栏表格分页分开，以下恢复连续顺序。

> Table 8 further summarizes the predictive performance of the proposed model and baseline methods across the four CS2-series cells. Overall, the proposed model achieves the lowest errors on all metrics, with average reductions of approximately 16.8% in MAE and 12.9% in RMSE compared with the best-performing baseline. For example, on CS2–35, the proposed method attains an MAE of 0.0141 and an RMSE of 0.0208, outperforming the CNN-Transformer with an MAE of 0.0147 and an RMSE of 0.0233, and substantially surpassing the conventional Transformer with an MAE of 0.0233 and an RMSE of 0.0294 as well as the MLP with an MAE of 0.0265 and an RMSE of 0.0416. A similar trend is observed across CS2–36, CS2–37, and CS2–38, further confirming the robustness and stability of the proposed architecture.
>
> In addition, although the CNN-Transformer exhibits relatively competitive performance on CS2–35 and CS2–36, its prediction accuracy degrades significantly on CS2–38, yielding a MAPE of 0.0528 compared to 0.0301 of the proposed model. This suggests that the CNN-Transformer is more sensitive to variations in cell characteristics, whereas the proposed model maintains stronger generalization ability.
>
> Finally, conventional deep learning models such as MLP, CNN, and LSTM show considerably higher prediction errors than attention-based approaches. In particular, CNN produces the largest errors across all cells, with an RMSE of 0.0643 on CS2–38, underscoring its limited capability in capturing long-term dependencies. LSTM performs better than CNN and MLP but still lags behind Transformer-based architectures.

### 2.3 CS2对象核对

JE明确区分并分析了：

- **CS2-35**：训练/同电池验证对象，同时作为表格中的代表数值案例；
- **CS2-36和CS2-37**：用于说明CNN-Transformer仍具有竞争力；
- **CS2-38**：用于说明CNN-Transformer在困难电池上性能下降，并进一步点名CNN的RMSE最大；
- **四电池平均值**：只承担总体汇总，不是全部分析内容；
- **完整曲线、箱线图和局部放大图**：分别解释长期拟合、误差偏差和短期容量波动。

### 2.4 Oxford完整分析原文

来源：JESSOHRUL PDF第19--20页；`full.txt:2841--2893`。标题和开头因双栏提取发生错序，以下按PDF阅读顺序恢复。

> To validate the effectiveness and stability of the proposed model, the widely used LSTM model, the Transformer model, and the CNN-Transformer model, which incorporates convolutional layers, were selected as benchmark models for comparison. The SOH estimation results of the five models are presented in Fig. 10.
>
> Overall, the proposed model achieves the closest match to the actual SOH values across all cells, demonstrating superior validation and test performance. Even for Cell2, where the degradation trend is highly unstable, the proposed model exhibits the best fit, with the absolute error remaining closest to the zero axis.
>
> In contrast, although the Transformer model performs well on Cell1, achieving results comparable to the proposed model, its estimation accuracy deteriorates significantly on other cells, indicating overfitting. This issue arises due to the Transformer's weak ability to extract local features, making it less effective in distinguishing different battery degradation patterns. While the CNN-Transformer model improves upon this aspect, its overall accuracy remains far below that of the proposed model. Similarly, the estimation results reveal the limited ability of LSTM model to capture local features. Its estimated SOH curves appear overly smooth, allowing only a rough approximation of the true SOH values without accurately identifying short-term capacity growth phenomena in batteries.
>
> Table 10 displays the estimation inaccuracies of eight cells for five models. In general, the proposed model shows higher estimation accuracy and achieves the smallest average estimation error. Specifically, the maximum estimation error of the proposed model remains within 1%, with a maximum MAE of 0.65% and a maximum RMSE of 0.87%, while the average MAE and RMSE are 0.32% and 0.40%, respectively. These outcomes suggest a more consistent performance in comparison to the other models, which is essential for maintaining the safe and reliable operation of batteries when handling substantial amounts of unseen data.
>
> Furthermore, Table 10 also reveals that although the Transformer model performs not too bad on the training data, with results only slightly inferior to the proposed model, it suffers from overfitting. This is evidenced by its significantly poorer performance on the other test data, whereas the proposed model effectively mitigates this issue, leading to better overall results. This suggests that our model learns genuinely useful information from health indicators rather than merely fitting the degradation trend of the current battery. In contrast, while the LSTM model exhibits better generalization than the Transformer model, its learning capability on training data is noticeably weaker. Across various battery datasets, the proposed model outperforms it consistently.

### 2.5 Oxford对象核对

JE不是只报告八电池平均结果。它具体分析了：

- **Cell1**：明确称其为Transformer表现良好、与所提模型接近的训练电池；
- **Cell2**：明确称退化趋势高度不稳定，并分析所提模型拟合与误差；
- **其他测试电池整体**：用于说明Transformer从训练电池到测试电池的性能下降；
- **LSTM曲线形态**：分析过度平滑以及不能识别短期容量增长；
- **八电池最大/平均指标**：用于讨论跨电池一致性。

但它遗漏了表10中的一个反例：Oxford Cell5上CNN-Transformer的MAE、RMSE和MAPE均优于所提模型。它也把汇总指标称为`maximum estimation error`，并把误差结果直接上升到安全可靠运行，措辞过强。

---

## 3. Engineering-AI

Engineering-AI没有只按Cell1到Cell8顺序逐个报告，而是按照退化行为分组。以下段落来自PDF第13--14页；`full.txt:1363--1445`。双栏中的小节顺序和跨页续句已按PDF恢复。

### 3.1 Oxford总述与瞬时下降原文

> Fig. 11 and Table 7 present the estimation results on the Oxford dataset. While all models capture the general linear decay trend, a granular analysis of the degradation trajectories reveals critical differences in dynamic response characteristics.
>
> **Responsiveness to instantaneous drops (Cells 2 & 6).** A challenge inherent to the Oxford dataset is the presence of abrupt SOH drops or local knee-points, which are particularly visible in Cell 2 and Cell 6.
>
> **Baseline Limitations (Hysteresis Effect):** As evidenced by the magnified regions of Fig. 11, sequential models such as the LSTM and CNN-LSTM often suffer from a pronounced hysteresis effect, or phase lag. Constrained by recurrent memory inertia, these architectures may struggle to synchronize with rapid downward transitions. This results in a negative time lag and a consistent underestimation of the instantaneous degradation magnitude.
>
> **SL-AgentNet Advantage:** In contrast, SL-AgentNet exhibits improved temporal alignment, closely tracking these abrupt drops with minimal lag. Mechanistically, this responsiveness is driven by the S-DSConv module embedded within the FLFA block. By executing convolution operations prior to attention aggregation, the S-DSConv acts as a high-frequency feature extractor. This component remains highly sensitive to immediate gradient changes, allowing the model to adapt rapidly to local structural shifts without the memory inertia typical of RNNs.

### 3.2 Oxford平滑线性退化原文

> **Precision in linear decay (Cells 1, 3, 7, & 8).** For cells exhibiting relatively smooth linear decay, such as Cells 1, 3, 7, and 8, the primary challenge involves minimizing steady-state error and jitter caused by measurement noise. SL-AgentNet achieves strong alignment with the ground truth, yielding R² values exceeding 0.998; for instance, Cell 3 achieves 0.9990. Here, the post-fusion L-DSConv module plays an important role. Its large receptive field smooths out sensor noise while preserving the dominant aging trend. Consequently, SL-AgentNet achieves a lower average MAE of 0.0029 and an RMSE of 0.0041, representing a 60.8% reduction in MAE compared to the Transformer baseline (0.0074). This demonstrates its capability to balance dynamic sensitivity via the S-DSConv with static stability via the L-DSConv.

### 3.3 NASA容量恢复原文

> **Capturing capacity regeneration (NASA case).** The NASA batteries, exemplified by B0005, are characterized by frequent capacity regeneration phenomena that appear as local upward spikes in the SOH curve.
>
> **Observation:** Standard Transformers often overreact to these local variations or treat them as noise due to a lack of structural regularization. In contrast, SL-AgentNet captures both the amplitude and timing of these regeneration peaks, achieving a low RMSE of 0.0072 on B0005.
>
> **Mechanism:** This fine-grained capture capability is attributed to the FDFA module. By introducing a non-linear pre-activation (ReLU) branch, the FDFA acts as a significance filter that highlights high-energy local changes, such as regeneration spikes, against the background of gradual decay. This enables the model to distinguish meaningful physical recovery from random measurement noise.

### 3.4 CALCE加速退化原文

> **Tracking accelerated aging trends (CALCE case).** The CALCE batteries, such as CS2_38, exhibit a rapid “diving” behavior or accelerated aging in the late life cycle.
>
> **Observation:** While the response of SL-AgentNet to minute instantaneous drops in this dataset is moderate compared to the NASA case, its overall fitting precision regarding the accelerated decay trajectory is significantly better than the baselines. For instance, on CS2_38, SL-AgentNet achieves an RMSE of 0.0249, outperforming both the Transformer (0.0344) and LSTM (0.0331).
>
> **Mechanism:** This robustness is attributed to the Global Agent Anchor. Unlike standard attention mechanisms which compute pairwise N × N dependencies and often dilute the trend with local noise, our FLFA module aggregates information into a single static agent. This agent learns the global degradation prototype, prioritizing the dominant accelerated aging trend over transient fluctuations. This contributes to the model maintaining a tight global fit even during highly non-linear late-life stages.
>
> In summary, SL-AgentNet achieves an average RMSE of 0.0169 across the combined datasets, outperforming the Transformer (0.0402) and LSTM (0.0260). This demonstrates that our “Local–Global” architectural design generalizes effectively across different battery chemistries and degradation modes.

### 3.5 Engineering-AI对象核对

它不是只报告Oxford八电池平均值，而是主动分组：

- **Cell1、Cell3、Cell7、Cell8**：归为平滑线性退化，分析稳态误差与测量噪声抖动；
- **Cell2、Cell6**：归为突然下降/局部拐点，分析LSTM类模型的相位滞后；
- **Cell3**：作为平滑退化中的具体数值例子；
- **B0005**：作为容量恢复案例；
- **CS2_38**：作为后期加速下降案例，并明确承认细小瞬时下降响应一般；
- **组合平均RMSE**：最后才用于整体收束。

它的解释比BMSFormer和JE更直接地连接到模块，但`driven by`、`is attributed to`等因果力度明显超过单纯模型对比能够支持的范围。本文必须结合消融结果并降低为`is consistent with`或`is supported by the ablation results`。

---

## 4. 对作者问题的直接答案

### 4.1 它们有没有分析Cell1？

有，但三篇的处理不同：

- **BMSFormer**具体分析Cell1：CNN-Transformer的IQR接近零，但须线不对称、低值离群点更多；随后扩展到Cell2--Cell8。
- **JESSOHRUL**具体分析Cell1：Transformer在训练电池Cell1上与所提模型接近，但在其他测试电池上明显下降；它用Cell1与其他电池的落差讨论过拟合。
- **Engineering-AI**把Cell1与Cell3、Cell7、Cell8归为平滑线性退化组，讨论稳态误差和噪声抖动，但具体数值例子主要使用Cell3。

### 4.2 它们是不是只报告八个电池平均结果？

不是。

- BMSFormer：Cell1误差分布 + Cell2/6突然下降 + Cell6局部误差 + 八电池平均。
- JESSOHRUL：Cell1训练表现 + Cell2不稳定退化 + 其他测试电池下降 + LSTM曲线过平滑 + 八电池最大/平均指标。
- Engineering-AI：按Cell1/3/7/8、Cell2/6分组 + B0005容量恢复 + CS2_38加速退化 + 最后组合平均。

共同规律是：平均指标只负责总结；真正的解释来自某个具体电池的曲线形态、误差分布或困难退化区段。
