# 三篇范文消融实验原文与本文对应（2026-09-16）

## 使用说明

本文件采用与模型对比原文汇编相同的尺度：保留范文中直接承担消融分析功能的完整英文段落，并逐项说明它们分析了哪个变体、哪个数据集、哪种好结果或差结果。双栏TXT错序处以PDF阅读顺序恢复。

---

## 1. BMSFormer是否有对应的模块消融

BMSFormer没有与本文表4-10、表4-11同构的正式模块消融表。它包含：

- 不同网络深度、维度和头数的超参数比较；
- LGFA、DSConv-S和DSConv-L的结构及复杂度分析；
- BMSFormer与CNN-Transformer、Transformer、LSTM等完整模型的对比。

这些实验可以支持“某些配置更合适”或“完整架构表现更好”，但不能像受控消融那样单独证明LGFA、DSConv-S或DSConv-L的独立贡献。因此，本文的模块作用不应以BMSFormer模型对比中的强因果句为直接证据；对应的主要范文应是JESSOHRUL和Engineering-AI。

---

## 2. JESSOHRUL消融实验完整原文

来源：JESSOHRUL PDF第22--23页；`full.txt:3320--3327, 3492--3532`。原段落被双栏表格和分页分开，以下按照PDF连续阅读顺序恢复。

### 2.1 消融前先提出设计矛盾

> Linear attention mechanisms significantly reduce the computational and memory complexity of standard attention by employing techniques such as low-rank decomposition, kernel approximation, sparsification, and local attention strategies. While these approaches improve efficiency, they often compromise representation capacity and feature extraction ability to varying degrees. Conventional convolution operations can partially alleviate this limitation; however, they usually introduce a substantial number of additional parameters, resulting in an unfavorable trade-off between accuracy and efficiency. To address this issue, the proposed model incorporates DSConv as a lightweight convolutional prior to enhance feature diversity while avoiding excessive parameter growth, thereby achieving a balanced improvement in both performance and computational efficiency.

这段还没有讨论结果，而是先说明消融要回答的技术问题：

1. 线性注意力提高效率，但可能损失表示与特征提取能力；
2. 标准卷积可以补局部信息，但增加参数；
3. DSConv被设计为较轻量的卷积先验；
4. 后面的消融要验证的是准确性与效率之间的结构选择，而不只是“加入模块后数字是否下降”。

### 2.2 M1、M2、M3与完整模型原文

> Ablation experiments are conducted to further provide quantitative and qualitative comparisons between the proposed DSCA mechanism, the linear-attention-based backbone, and the DSConv module. As shown in Table 13, the backbone model with linear attention only (M1) exhibits the largest prediction errors across all datasets, which can be attributed to its limited sensitivity to battery-specific local capacity fluctuations. By enhancing the input representations to the backbone with the DSConv module (M2), the prediction error is significantly reduced, indicating that DSConv effectively captures fine-grained local degradation patterns.
>
> Furthermore, introducing the DSCA mechanism on the backbone while removing DSConv (M3) leads to noticeable performance improvements over both M1 and M2. This result confirms the effectiveness of DSCA in modeling long-term dependencies and capturing global degradation trends. Nevertheless, the absence of DSConv weakens the local learning conditions, thereby limiting the overall performance gains. When DSConv and DSCA are jointly integrated in the proposed model, the highest and most consistent prediction accuracy is achieved across the selected battery datasets.

### 2.3 代表数字和模块协同原文

> For example, on the NASA B0005 dataset, the average error is reduced to 0.0058, corresponding to reductions of 50.14%, 19.44%, and 7.94% compared with M1, M2, and M3, respectively. Similar trends are observed on the CALCE dataset: for battery CS2–35, the proposed method reduces the average error from 0.0322 (M1) to 0.0207, achieving a relative reduction of 38.35%. On CS2–36 and CS2–37, the proposed model further decreases the error by 30.34% and 47.04%, respectively, compared to the linear-attention-based backbone.
>
> These results clearly show that the complementary effects of DSConv and DSCA. DSConv reinforces local feature extraction by capturing fine-grained degradation dynamics, while DSCA enriches feature diversity and representation capacity based on linear attention, enabling effective modeling of both long-term degradation trends and short-term capacity fluctuations. Their synergistic integration allows the proposed model to achieve superior accuracy and generalization performance across heterogeneous battery datasets.

### 2.4 JE究竟怎样说“好的”和“差的”

JE对四个变体的安排非常明确：

| 变体 | JE报告的结果 | JE给出的解释 |
|---|---|---|
| M1：只有线性注意力骨干 | 所有数据集误差最大 | 对电池局部容量波动敏感性有限 |
| M2：骨干 + DSConv | 相对M1显著降低误差 | 提取细粒度局部退化模式 |
| M3：骨干 + DSCA，无DSConv | 优于M1和M2 | 建模长期依赖和全局退化趋势 |
| M3仍存在的不足 | 没有达到完整模型 | 缺少DSConv使局部学习条件减弱 |
| 完整模型 | 跨所选数据集最高且最一致 | DSConv与DSCA互补 |

JE写“差结果”的方式不是寻找某个数据集上数值变坏，因为它的表格基本呈单调改进；它写的是**结构残余缺口**：M3虽然改善长期与全局建模，但缺少DSConv，所以局部学习仍有限。随后完整模型才解决这个缺口。

JE的推进顺序是：

> 设计矛盾 → 基础模型最差 → 单独DSConv改善局部 → 单独DSCA改善长期/全局 → 单模块仍有缺口 → 完整组合最好 → 代表数据集数字 → 异质数据集意义。

但`can be attributed to`、`confirms`、`clearly show`等措辞偏强。表13支持模块加入与性能变化之间的关系，但不能唯一证明模块学习到的物理内容。本文宜用`supports`或`is consistent with`。

### 2.5 JE有没有逐个分析所有电池，以及表13的数值问题

JE没有逐个解释六节电池的退化现象。正文具体选择：

- B0005：报告完整模型相对M1、M2、M3的三个降幅；
- CS2-35：报告M1与完整模型的平均误差和相对降幅；
- CS2-36、CS2-37：只报告完整模型相对M1的降幅；
- B0006、B0007：没有单独分析，只包含在`across all datasets`和表13中。

它也没有对预测曲线的局部区段进行消融分析。所谓`quantitative and qualitative comparisons`主要仍是总体误差表与结构解释。

表13还存在明显的Average列算术或排版问题。以CS2-35为例，正文写M1从0.0322降至0.0207并降低38.35\%，但直接使用这两个显示值只能得到35.71\%。重新由三项误差计算，M1平均值约为0.0336，才与38.35\%基本一致。CS2-36和CS2-37的M1 Average也与三项指标重算结果不一致。由此可见：JE的递进逻辑可以学习，但不能把其Average列直接作为数值计算范例。

---

## 3. Engineering-AI消融实验完整原文

Engineering-AI的消融比JE更复杂，分为三层：HI与架构的宏观拆分、具体组件有效性、注意力模块交互。来源为PDF第15--17页；`full.txt:1450--1477, 2058--2090, 2275--2329, 2334--2395`。

### 3.1 三层消融设计原文

> To evaluate the contributions of the proposed framework and disentangle the sources of performance gains, a systematic ablation study was conducted. This analysis is structured into three tiers: a macro-level decoupling of Health Indicators (HIs) versus model architecture, a micro-level analysis of specific component effectiveness, and an interaction analysis of the attention mechanisms.
>
> Experimental Constraint (The “Early Prediction” Challenge): Importantly, to demonstrate data efficiency, an “Early Prediction” protocol was adopted where our model was trained using only the first 30% of cycle data. This stands in contrast to benchmark methods, which typically utilize 50%–70% of lifecycle data, thereby possessing an informational advantage.

### 3.2 宏观消融：HI贡献与架构贡献原文

> A pivotal research inquiry concerns the attribution of performance gains: do they arise from the proposed Systematic HIs (CCCA/CCDA) or the specialized SL-AgentNet architecture? To decouple these contributions and position our work within the landscape of state-of-the-art methods, our approach was benchmarked against recent results reported in the literature on identical datasets.
>
> **Contribution of Systematic HIs (High Information Density):** Standard LSTM models employing traditional manual/IC features and trained on 50% data achieve an RMSE of 0.0183, as reported by Yan et al. Importantly, when employing our proposed Systematic HIs (CCCA/CCDA) with a standard LSTM, even under the strict limitation of 30% training data, the model maintains a comparable RMSE of 0.0211. Moreover, equipping a standard Transformer with our HIs yields an RMSE of 0.0150, matching or marginally outperforming the baseline reported by Xu et al. (RMSE 0.0151), despite the data scarcity. These results suggest that our screened HIs possess high “information density”, enabling standard models to extract robust degradation patterns from sparse early-life data where traditional features often fail.
>
> **Contribution of SL-AgentNet Architecture (Architectural Efficacy):** A notable performance enhancement is attributed to the model architecture. Under the identical 30% data constraint, upgrading from a standard Transformer (RMSE 0.0150) to the proposed SL-AgentNet (RMSE 0.0052) yields a 65.3% error reduction. This suggests that while Systematic HIs provide a robust, noise-immune foundation, the architectural innovations, specifically the linear-complexity FLFA, the multi-branch PIAF, and the S-DSConv, play a key role in modeling the complex, non-linear dependencies required for high-precision early prediction.

这一层先固定标准LSTM/Transformer，再替换HI；随后在相同HI和30\%数据条件下替换架构。它试图区分“输入信息贡献”和“网络结构贡献”。不过，与不同文献结果比较仍可能受训练流程和实现差异影响，严格性弱于同一代码与同一划分下的受控消融。

### 3.3 卷积组件消融原文

> To validate the efficacy of key architectural components, ablation studies were conducted focusing on convolutional modules and activation functions across the Oxford, NASA, and CALCE datasets.
>
> **Impact of depthwise separable convolutions (S/L-DSConv).** The proposed framework integrates two distinct convolutional modules: the small-kernel S-DSConv embedded within the FLFA module for pre-attention local enhancement, and the large-kernel L-DSConv positioned after the AFF module for post-fusion refinement. Their specific contributions were assessed by substituting them with standard convolutions. Although standard convolutions possess higher parameter counts and theoretically larger capacities, the results in Table 10 indicate performance degradation, thereby supporting the efficiency of our design.
>
> **Pre-Attention Local Enhancement (S-DSConv):** Substituting the S-DSConv with a standard convolution corresponds to an accuracy drop, notably increasing the RMSE from 0.0041 to 0.0102 on the Oxford dataset. This suggests that the parameter-heavy standard convolution may be prone to overfitting on sparse battery data. In contrast, the S-DSConv functions as a structural regularizer; by decoupling spatial and channel correlations, it imposes a beneficial inductive bias that encourages the model to focus on essential high-frequency local patterns rather than noise.
>
> **Post-Fusion Global Refinement (L-DSConv):** Replacing the L-DSConv leads to a performance decline, particularly on the CALCE dataset where the RMSE increases to 0.0719. This suggests that a lightweight, large-kernel convolution is beneficial for smoothing fused attention features and extracting long-term degradation trends prior to the final regression stage.

这里比较的是“深度可分离卷积替换为标准卷积”，不是把卷积模块完全移除。因此它主要支持DSConv相对标准卷积的设计优势，不能单独证明没有该卷积时模型一定如何。

### 3.4 PIAF激活组件消融原文

> **Impact of heterogeneous activation (PIAF vs. Standard MLP).** The PIAF module functions as the final regression head. This heterogeneous design, which combines ReLU, Tanh, and Identity functions, was compared against a standard MLP baseline configured with homogeneous Gaussian Error Linear Unit (GeLU) activation. As summarized in Table 11, the results demonstrate the effectiveness of the heterogeneous strategy.
>
> On the NASA dataset, replacing the standard MLP with PIAF reduces the MAE from 0.0139 to 0.0066, representing a 52.5% reduction. This gain suggests that the Tanh branch in PIAF, with its saturation boundaries, captures the distinct voltage plateaus and abrupt degradation shifts typical of the NASA dataset, phenomena that the unbounded GeLU struggles to model accurately.
>
> On the Oxford dataset, PIAF achieves an RMSE of 0.0041 compared to 0.0068 for the baseline, corresponding to a 39.7% reduction. Even on the CALCE dataset, PIAF maintains its advantage, lowering the RMSE from 0.0264 to 0.0239.
>
> This widespread improvement suggests that the “mixture of activations” strategy captures complex non-linearities that a single homogeneous activation function fails to model, thereby validating the feature richness of our design.

这一段的写法是：先说明对照对象，再选择NASA的最大改善解释具体数据特征，然后补Oxford和CALCE证明改善不是单一数据集现象。其“Tanh捕捉电压平台”等机制解释仍缺少直接表征分析，因果力度偏强。

### 3.5 FDFA与FLFA交互消融原文

> **Micro-ablation II: Interaction analysis of attention modules.** To elucidate the interaction dynamics between the diversity-enhancing FDFA and the efficiency-focused FLFA modules, specifically regarding whether their contributions are additive or synergistic, a stepwise ablation was conducted on the CALCE and NASA datasets. The AAT-1d was utilized as the baseline and progressively integrated the modules. The results are detailed in Table 12.
>
> **Quantitative evidence of synergy.** Experimental results, particularly on the CALCE dataset, suggest a super-additive synergistic effect:
>
> **Individual Gains:** On the CALCE dataset, adding the FDFA alone improves the MAE by 0.0019, reducing it from 0.0200 to 0.0181. Similarly, the independent addition of the FLFA yields a marginal improvement of 0.0005, lowering the MAE from 0.0200 to 0.0195. Consequently, the arithmetic sum of these isolated gains is 0.0024.
>
> **Combined Gain:** When both modules are integrated into the full AFF framework, the MAE drops significantly to 0.0169. This represents a total gain of 0.0031.
>
> **Conclusion:** Since the combined gain of 0.0031 exceeds the arithmetic sum of 0.0024, this indicates a positive synergistic interaction. The modules do not merely operate in parallel; rather, they mutually reinforce the predictive capability of the model.
>
> **Mechanistic explanation: Orthogonality and complementarity.** This synergy arises because the two modules operate on nearly orthogonal feature dimensions, thereby generating complementary feature subspaces. The FDFA branch, utilizing non-linear ReLU pre-activation, targets the amplitude domain. It acts as a significance filter that isolates high-energy degradation signals from background noise. Conversely, the parallel FLFA branch, equipped with S-DSConv and linear attention, focuses on the spatio-temporal structural domain to capture local–global dependencies regardless of signal magnitude. By fusing these distinct perspectives, specifically amplitude significance and temporal structure, the model achieves a comprehensive representation where the strengths of one branch compensate for the limitations of the other. This results in robustness that transcends simple summation.

CALCE的MAE算术关系本身成立：0.0019 + 0.0005 = 0.0024，小于组合改善0.0031。但这不是所有指标和数据集的普遍结果：

- CALCE MAPE也呈超加性改善；
- CALCE RMSE和$R^2$的组合改善小于两个单模块改善的算术和；
- NASA的四项指标均不呈超加性。

因此最多可以说CALCE的MAE和MAPE显示正向交互迹象，不能声称已经证明跨数据集的普遍协同。仅凭误差差值也不能直接证明特征子空间“近似正交”；后者需要特征相关性、投影或表示分析支持。

---

## 4. 两篇范文消融写法的实质区别

| 范文 | 单模块结果 | 怎样写差结果 | 怎样写组合 | 应用/任务落点 |
|---|---|---|---|---|
| JE | M2、M3相对M1基本都改善 | 单模块仍缺少另一类能力 | 完整模型跨数据集最一致 | 异质数据集、长期趋势与短期波动 |
| Engineering-AI | 分别更换HI、卷积、激活和注意力分支 | 标准卷积/单一激活/单分支误差更高 | 用单独增益之和与组合增益比较协同 | 早期数据稀缺、不同退化形态、结构配置 |

本文的数据不像JE那样呈单调改善，也没有Engineering-AI那种完整的四组合交互表。因此必须使用不同叙述：单模块收益依赖数据集，完整模型的价值主要是跨数据集一致性。

---

## 5. 本文表4-10的逐项对应

### 5.1 M1基础模型

M1不是所有数据集上绝对最差：

- CS2：综合平均误差0.0157；
- CX2：0.0500，为四变体最高；
- MIT：0.0020，与完整模型M4并列最低；
- Oxford：0.0071，为四变体最高。

因此不能照搬JE的`M1 exhibits the largest prediction errors across all datasets`。本文只能说：M1在CX2和Oxford表现最弱，但在MIT已与完整模型的四舍五入平均值持平。

### 5.2 M2：单独加入多尺度DSConv

相对M1：

- CX2从0.0500降至0.0494，小幅改善；
- Oxford从0.0071降至0.0065，改善较明确；
- CS2从0.0157升至0.0162，变差；
- MIT从0.0020升至0.0023，变差。

因此不能写“DSConv independently improves all datasets”或直接确认它普遍提取了有效局部模式。可以写：多尺度DSConv单独使用时只在部分数据集降低误差，其收益取决于退化模式。

### 5.3 M3：单独加入RAA

相对M1：

- CS2从0.0157降至0.0152；
- CX2从0.0500降至0.0442；
- Oxford从0.0071降至0.0060；
- MIT从0.0020升至0.0026。

RAA在三个数据集上改善，但MIT明显变差。可以说跨位置信息交互在多数数据集有益，不能写成所有数据域均独立有效。

### 5.4 M4完整模型

M4在四个数据集上取得最低或并列最低综合平均误差：

- CS2为0.0151，但M3的MAE 0.0119略低于M4的0.0120；
- CX2由M1的0.0500降至0.0225，是最明显改善；
- MIT综合平均值0.0020与M1并列，但M4的MAE 0.0018优于M1的0.0019；
- Oxford为0.0059，较M1降低16.52\%（按论文当前报告）。

因此，完整模型的主要证据不是每一项指标都绝对最佳，而是四数据集综合平均值最一致，尤其在CX2中只有组合后才出现大幅下降。

### 5.5 表4-10真正能支持的模块解释

本文应写：

> 单独加入多尺度DSConv或RAA时，改善随数据集而变化；二者组合后才在四个数据集上得到最低或并列最低的综合平均误差。这种结果支持局部多尺度信息与跨位置信息之间具有互补关系。

不能写：

> 多尺度DSConv在所有数据集上都能有效提取局部退化特征；RAA在所有数据集上都能提高全局建模能力。

后两句与CS2、MIT上的实际结果冲突。

---

## 6. 本文表4-11的逐项对应

### 6.1 S5短核单尺度

相对不含卷积的S0：

- MIT从0.0026降至0.0025，略有改善；
- CS2从0.0152升至0.0161；
- CX2从0.0442升至0.0494；
- Oxford从0.0060升至0.0062。

所以短核不是普适增强，只在MIT上单独表现出小幅收益。

### 6.2 S31长核单尺度

相对S0：

- CX2从0.0442降至0.0348，改善21.27\%；
- MIT的综合平均值仍为0.0026，基本持平；
- CS2从0.0152升至0.0156；
- Oxford从0.0060升至0.0061。

因此长核的清晰优势集中在具有阶段转换和非线性尾段的CX2，不能概括为所有数据集的长期趋势建模均提高。

### 6.3 SFull双尺度

SFull在四个数据集上均取得最低综合平均误差。相对于最佳单尺度变体：

- CX2进一步降低35.34\%；
- MIT进一步降低20.00\%；
- CS2和Oxford也取得小幅最低值。

这支持的不是“每个尺度单独都有效”，而是：不同数据集偏好的单尺度不同，联合尺度提高了固定结构面对不同退化轨迹时的结果一致性。

---

## 7. 可直接审定的本文消融中英文候选

### 7.1 模块消融

**中文：**

> 表4-10表明，两类模块单独使用时均未产生一致的跨数据集收益。与M1相比，M2加入多尺度DSConv后，CX2和Oxford上的三项误差均有所降低，综合平均误差分别下降1.20\%和8.45\%；但在CS2和MIT上，MAE、RMSE和MAPE均有所升高。M3加入RAA后获得了更广泛的改善，在CS2、CX2和Oxford上的综合平均误差分别降低3.18\%、11.60\%和15.49\%，但其在MIT上的三项误差仍高于M1。因此，各模块单独使用时的作用取决于数据域，并未在四个数据集上表现出普遍一致的正向效果。
>
> 当多尺度DSConv与RAA在M4中共同使用时，模型在四个数据集上均取得最低或并列最低的综合平均误差，其中CX2上的交互作用最为明显。相对M1，M2和M3单独带来的误差降幅分别为0.0006和0.0058，而两类模块共同使用后，误差由0.0500降至0.0225，降幅达到0.0275。这一结果为两类模块在CX2上的正向交互提供了定量证据。该现象在其他数据集上并不同样突出：CS2上M3的MAE略低于M4，而MIT上M4在当前报告精度下仅与M1取得相同的综合平均误差。因此，完整配置的主要价值在于获得更加一致的跨数据集表现，而不是任一模块单独使用时均能带来统一改善。

**English:**

> Table~4-10 shows that neither module provides a uniform benefit when used alone. Compared with M1, adding multi-scale DSConv in M2 reduces all three error metrics on CX2 and Oxford, with the combined average error decreasing by 1.20\% and 8.45\%, respectively. However, M2 increases MAE, RMSE, and MAPE on both CS2 and MIT. Adding RAA in M3 produces broader improvements, reducing the combined average error by 3.18\%, 11.60\%, and 15.49\% on CS2, CX2, and Oxford, respectively, but all three errors increase on MIT. The effects of the individual modules are therefore dependent on the data domain rather than uniformly positive across the four datasets.
>
> When multi-scale DSConv and RAA are integrated in M4, the model achieves the lowest or jointly lowest combined average error on all four datasets. The interaction is most evident on CX2. Relative to M1, the isolated reductions produced by M2 and M3 are 0.0006 and 0.0058, whereas their joint integration reduces the error by 0.0275, from 0.0500 to 0.0225. This result provides evidence of a positive interaction between the two modules on CX2. The pattern is less pronounced on the other datasets: M3 has a slightly lower MAE than M4 on CS2, and M4 only matches the combined average error of M1 on MIT at the reported precision. The main benefit of the full configuration is therefore its more consistent performance across datasets, rather than a uniform improvement from either module in isolation.

### 7.2 卷积尺度消融

**中文：**

> 表4-11进一步表明，有效的卷积尺度随数据集中的退化模式而变化。短核S5仅在MIT上相对S0带来小幅改善，却在CS2、CX2和Oxford上增加误差；长核S31在CX2上将综合平均误差由0.0442降低至0.0348，但在CS2和Oxford上仍未优于S0。单一尺度因此不是对所有数据集均有效的固定增强。结合两个尺度后，SFull在四个数据集上均取得最低综合平均误差，并相对最佳单尺度变体在CX2和MIT上分别进一步降低35.34\%和20.00\%。这些结果支持双尺度配置覆盖更广泛的时间模式，并可能减少同一结构用于不同电池数据时重新选择卷积尺度的需要；但现有实验不能证明某个卷积核唯一对应某种物理退化机制。

**English:**

> Table~4-11 further shows that the effective convolutional scale varies with the degradation patterns in each dataset. S5 gives a small improvement over S0 only on MIT, while increasing the error on CS2, CX2, and Oxford. S31 reduces the combined average error on CX2 from 0.0442 to 0.0348, but still does not outperform S0 on CS2 or Oxford. A single scale is therefore not a uniform enhancement across datasets. When the two scales are combined, SFull achieves the lowest combined average error on all four datasets and further reduces the error by 35.34\% on CX2 and 20.00\% on MIT relative to the best single-scale variant. These results support the ability of the dual-scale configuration to cover a broader range of temporal patterns and suggest that it may reduce the need to select a different convolutional scale when the same architecture is applied to different battery data. The present ablation does not, however, establish a unique correspondence between either kernel and a specific physical degradation mechanism.

---

## 8. 消融怎样真正落到应用

JE的应用落点是“异质电池数据集上的一致准确性”；Engineering-AI的应用落点是“稀疏早期数据下区分HI贡献与架构贡献，并判断组件是否协同”。对应本文，最有证据的应用解释是：

1. 单模块结果随数据集变化，说明新电池数据的退化模式会影响某个结构是否单独有效；
2. 完整模型在四个数据集上更一致，说明固定完整结构比预选单模块更适合跨不同数据域复用；
3. 单尺度偏好在不同数据集之间变化，双尺度配置可能减少为每个数据集重新选核的需要；
4. CX2上的组合改善最明显，与主对比实验中CX2_38的持续阶段转换和非线性尾段优势相互印证；
5. MIT中M1与M4平均值并列、M2/M3单独变差，说明复杂模块并非在所有较易拟合数据上都带来明显收益。

不能从这些消融直接推出真实部署性能、物理机理识别或任意新数据集上的必然提升。
