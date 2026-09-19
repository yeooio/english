# Approved translations

## Chapter 1 health-indicator selection rationale — whole-paragraph confirmation 2026-09-16

- The author confirmed the paragraph's position and rhetorical role after comparison with JESSOHRUL's literature-need--challenge--solution--contribution progression. The paragraph states a general selection need; the later challenge explains the difficulty, and contribution (1) states the manuscript's concrete algorithm, operations, and results.
- Author-confirmed suggested Chinese: `单一健康指标所包含的退化信息相对有限，而多源特征能够从不同方面补充对电池退化的描述。然而，增加候选指标的数量并不必然提高估计精度。表征能力较弱、跨电池表现不一致或信息冗余的指标，可能限制多源信息的有效利用，并增加模型的学习负担。因此，有必要设计相应的健康指标筛选算法，将候选指标与SOH的相关性、跨电池表现以及指标间的冗余纳入统一的评价与筛选过程。该算法应保留具有稳定表征能力的指标，减少与SOH弱相关或包含冗余信息的输入，以帮助模型更有效地学习电池退化规律。` Frozen Chinese remains unchanged.
- The current English paragraph remains approved without change. Compilation deferred while introduction review continues.

## Chapter 1 multi-source indicators and Dai/Lin literature paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the current paragraph with a refinement to the Lin et al. sentence: `constructed multiple features from electrical, thermodynamic, and electrochemical perspectives` preserves the source relationship “从……角度构建多类特征” and follows ref55's terminology; `thereby` explicitly carries the source result relation.
- The opening and Dai et al. sentences remain unchanged. A three-reference and independent-agent audit confirmed the operating-data/derived-curve relation, candidate HIs, per-cycle statistics, feature-combination comparison, PCA, simulated annealing, retained dimensions, redundancy reduction, and SOH-performance wording.
- Working Chapter 1 and the bilingual English block were synchronized. Frozen Chinese remains unchanged; in this citation context, the source's `热学` is recorded as corresponding to ref55's `thermodynamic`. Compilation deferred while introduction review continues.

## Chapter 1 time-based health indicators and interval selection — whole-paragraph confirmation 2026-09-16

- The author confirmed the paragraph with one precision correction: `Constant current charge time (CCCT) can be obtained from the difference between the times corresponding to the two endpoints of a selected voltage interval.` This restores the frozen Chinese distinction between voltage endpoints and their corresponding times.
- All remaining sentences are retained. A three-reference and independent-agent audit confirmed the CCCT term, the Richardson/Lin/Tian/Li study roles, interval selection, progressively narrowed voltage windows, PCC values from multiple cells in the same group, correlation strength, and the final extraction purpose.
- Working Chapter 1 and the bilingual English block were synchronized; frozen Chinese remains unchanged. Compilation deferred while introduction review continues.

## Chapter 1 health-indicator sources and incremental-capacity paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the complete current English paragraph after comparing the frozen Chinese, first English/backtranslation, and current English/backtranslation. Existing sentence-level approvals remain in force; no manuscript wording changed in this confirmation.
- A three-reference and independent-agent audit confirmed the HI extraction/selection wording, recorded operating data and derived curves, impedance spectrum measurements, temperature-related limitations, incremental-capacity differentiation and noise amplification, smoothing, and Wen et al.'s correlation-based peak selection. The current syntax makes the modifier relationships explicit without adding technical content.
- Frozen Chinese and working English remain unchanged. Compilation deferred while introduction review continues.

## Chapter 1 Transformer literature and computational-bottleneck paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the complete current English paragraph after comparing the frozen Chinese, first English/backtranslation, and current English/backtranslation. Existing sentence-level approvals are retained, and no manuscript wording changed in this confirmation.
- A three-reference and independent-agent audit confirmed the RNN-to-Transformer transition, recurrence avoidance, self-attention mechanism, long-range dependencies, parallel computation, cited hybrid architectures, accuracy/resource trade-off, pairwise relationships, and quadratic time and memory complexity. `good`, `many`, and `often` preserve the source strength and scope; no unsupported mechanism or stronger reference claim was added.
- Frozen Chinese and working English remain unchanged. Compilation deferred while introduction review continues.

## Chapter 1 CNN--RNN limitations and hybrid-model paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the complete current English paragraph in `chapters/chapter01.tex` after comparing the frozen Chinese, first English/backtranslation, and current English/backtranslation. No manuscript wording changed.
- A three-reference and independent-agent audit confirmed the CNN receptive-field limitation, the RNN hidden-state mechanism, the LSTM/GRU gating description, the three hybrid-model examples, and the concluding sequential-update limitation. The current terms `fusing distant features`, `long-range connections`, `long-term dependencies`, and `sequential updates across time steps` preserve their distinct technical objects and the source claim strength.
- Frozen Chinese and working English remain unchanged. Compilation deferred while introduction review continues.

## Chapter 1 deep-learning and CNN literature paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the complete current English paragraph in `chapters/chapter01.tex` after comparing the frozen Chinese, first English/backtranslation, and current English/backtranslation. No manuscript wording changed.
- A three-reference and independent-agent audit confirmed `multilayer neural networks`, `nonlinear representational capabilities`, `complex battery degradation patterns`, the CNN/RNN/Transformer list, `convolutional kernels`, `feature dimensionality`, `pooling operations`, Qian et al.'s randomly selected charging-curve segments and low capacity-estimation errors, and Lee et al.'s across-cycle capacity-fade sequences transformed into two-dimensional images. `increasingly adopted` retains the trend implied by the opening development clause.
- Frozen Chinese and working English remain unchanged. Compilation deferred while introduction review continues.

## Chapter 1 data-driven traditional-machine-learning paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the complete current English paragraph in `chapters/chapter01.tex` after comparing the frozen Chinese, first English/backtranslation, and current English/backtranslation. No manuscript wording changed in this confirmation.
- A three-reference and independent-agent terminology audit confirmed the current uses of `data-driven approaches`, `historical operating data`, the HI-to-SOH mapping, the six Fei et al. models, `partial charging voltage--capacity data`, `historical cycling`, `predictive performance`, and `structural limitations`. The current paragraph preserves the 42-feature/100-cycle/six-model facts and citation placement.
- Frozen Chinese and working English remain unchanged. Compilation deferred while introduction review continues.

## Chapter 1 model-based approaches paragraph — whole-paragraph confirmation 2026-09-16

- The author confirmed the complete current English paragraph in `chapters/chapter01.tex` after comparing the frozen Chinese, the first English backtranslation, and the current backtranslation. The existing sentence-level approved English remains unchanged.
- Backtranslation decision: `maintain robust estimation performance throughout the battery aging process` is understood as `在整个电池老化过程中保持估计鲁棒性`; the Chinese backtranslation should use the established term `估计鲁棒性` rather than the more expansive wording `稳健的估计性能`. This is a backtranslation terminology decision and does not require an English manuscript change.
- A three-reference terminology audit and an independent agent review found no specialized-term, factual-scope, tense, or claim-strength issue. Frozen Chinese and working English were not changed; compilation remains deferred while introduction review continues.

## Chapter 1 opening paragraph — revised approval 2026-09-16

- Author-approved Chinese revision: `凭借高能量密度、长循环寿命和低自放电率，锂离子电池已成为最重要的电化学储能技术之一，广泛应用于消费电子、电动汽车、固定式储能及其他领域。尽管如此，锂离子电池在长期运行过程中并不能始终保持稳定状态，仍存在不容忽视的安全风险。充放电循环与复杂工况会引发固体电解质界面（SEI）膜增厚、活性锂损失和电极结构退化等老化现象，进而导致容量衰减和性能下降，严重时将诱发短路、热失控等故障。因此，精确估计锂离子电池的健康状态（SOH）对于保障电池的安全性、可靠性和运行性能至关重要。` The frozen Chinese source remains unchanged.
- Approved English: With high energy density, a long cycle life, and a low self-discharge rate, lithium-ion batteries have become one of the most important electrochemical energy storage technologies, widely used across consumer electronics, electric vehicles, stationary energy storage, and other domains\cite{ref1,ref2,ref3,ref4}. Nevertheless, lithium-ion batteries cannot always remain stable during long-term operation and continue to pose safety risks that cannot be overlooked. Charge-discharge cycling and complex operating conditions induce aging processes such as thickening of the solid electrolyte interphase (SEI) layer, loss of active lithium, and structural degradation of the electrodes\cite{ref5,ref6}. These processes, in turn, lead to capacity fade and performance degradation and, in severe cases, trigger failures such as short circuits and thermal runaway\cite{ref7,ref8}. Therefore, precise estimation of lithium-ion battery state of health (SOH) is essential for ensuring battery safety, reliability, and operational performance.
- Decisions: reuse reference-aligned terminology where meanings match (`high energy density`, `low self-discharge rate`, `electric vehicles`, `other domains`, `solid electrolyte interphase`, `capacity fade`, `precise estimation`, and `is essential`). Retain source-specific `long cycle life`, `stationary energy storage`, and `operational performance`; do not import the references' broader `long service life`, `latent safety hazards`, `guaranteeing`, or heterogeneous-degradation claims. `Nevertheless` avoids repeating the next paragraph's sentence-initial `However`; `induce` → `lead to` → `trigger` preserves the source progression and strength.
- Updated working Chapter 1 and bilingual English block. Frozen Chinese Chapter 1 SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 online-monitoring dual-challenge paragraph — revised approval 2026-09-16

- Exact frozen Chinese: 容量衰减是电池老化最直观的特征，健康状态（state of health, SOH）通常采用容量保持率定义\cite{ref13,ref14}。但电池最大可用容量的精确测算需要完整或近似完整的充放电循环，难以满足在线监测需求\cite{ref10,ref11}。因此，从可观测运行信号中间接估计SOH已成为在线健康监测的关键途径。然而，复杂工况增加了退化信息稳定提取的难度，而电池管理系统（battery management system, BMS）严格的计算与存储限制又制约了模型复杂度，使在线SOH估计面临退化信息提取与模型计算效率的双重挑战\cite{ref31}。
- Approved English: Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurately measuring a battery's maximum available capacity requires full or nearly full charge-discharge cycles, which are impractical for online monitoring\cite{ref10,ref11}. Consequently, indirectly inferring SOH from observable operating signals has become a key approach to online battery health monitoring. Nevertheless, complex operating conditions make it harder to consistently extract degradation information, while the limited computing power and storage space of battery management systems (BMS) constrain model complexity. Together, these factors pose a dual challenge for online SOH estimation: degradation information extraction and the computational efficiency of estimation models\cite{ref31}.
- Decisions: retain the natural reference-aligned `which are impractical for online monitoring` and `key approach`; restore explicit `indirectly` and source-aligned `observable`; keep the established direct phrase `make it harder to consistently extract degradation information`. The final colon names exactly the two source challenges and does not repeat `stable/reliable` or replace computational efficiency with computational cost. Engineering-AI, BMSFormer, and JESSOHRUL corresponding contexts were reread; an independent agent also checked the Engineering-AI context. Working chapter and bilingual English block synchronized; frozen Chinese unchanged. Compilation deferred while introduction editing continues.

## Chapter 1 comparison and model-resource paragraph — revised approval 2026-09-15

- Location: `chapters/chapter01.tex`, paragraph immediately before `\input{tables/table_1_comparison}`. This entry supersedes the four earlier sentence-level approvals for this paragraph.
- Author-approved Chinese changes relative to the frozen source: use one `是否` to govern the four comparison criteria: `重点考察各方法是否充分利用电池运行数据中的退化信息、采用有效的健康指标提取与选择策略、通过针对性的模型设计兼顾估计性能与计算效率，以及开展模型复杂度评价。` Replace the final Chinese sentence with `因此，SOH估计模型需要在保持有效表征能力的同时，向更紧凑、更高效的方向发展，以满足资源受限BMS的实时估计需求。` The intervening Chinese sentences are unchanged. The frozen `source-zh/` file was not edited.
- Approved English: A comparison of existing SOH estimation methods is summarized in \Cref{tab:soh-method-comparison}. Specifically, we examine whether these methods make full use of degradation information in battery operating data, adopt effective health indicator extraction and selection strategies, balance estimation performance and computational efficiency through targeted model design, and evaluate model complexity. Given differences in battery chemistries and operating conditions, the ability of selected indicators to represent degradation consistently across cells warrants further attention. In addition to estimation performance, model complexity is directly related to practical deployment. In recent years, a notable trend in deep model design has been to increase network depth, expand model size, or introduce more complex structures for feature interaction to enhance representational capability. These designs help models better capture complex degradation patterns but usually come with higher parameter counts, computational costs, and storage requirements. Therefore, SOH estimation models need to become more compact and efficient while retaining effective representational capability to meet the real-time estimation requirements of resource-limited BMS.
- Decisions: one `whether` governs the four parallel comparison criteria; `a notable trend` preserves `一个显著趋势` without copying BMSFormer's stronger `predominant`; `structures for feature interaction` retains `特征交互结构`; `better capture` retains improved degradation-modeling ability; `usually come with` retains the source's association rather than asserting a stronger causal requirement. The last sentence states a development need, not completed embedded deployment. Three introduction contexts were reread and sentence-level Chinese backtranslation checked before approval.
- Updated working Chapter 1 and bilingual English block. Compilation deferred at the author's standing request while introduction editing continues. Frozen Chinese Chapter 1 SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 subsection 1.2 challenges and contributions — approved 2026-09-15

- Approved changes: introduce the three challenges with `Three main challenges facing existing methods are summarized as follows.`; in contribution (1), place MS-CCCT voltage-window calibration before evaluation of the complete candidate HI pool, matching Chapter 2's method order; directly state the feature-development-cell correlation basis and PCC/SCC threshold plus redundancy selection; in contribution (2), state local extraction, long-term-dependency capture, and fusion of the resulting representations, and express the small-/large-kernel joint role in one English sentence.
- Reference-style basis: BMSFormer introduction puts `Three` before its challenge list and directly states the attention module's modeling function; JESSOHRUL contribution (3) makes the HI-selection method the subject of a direct correlation-evaluation sentence. The proposed English preserves the manuscript's own operations and claim strength rather than copying either reference.
- Author-approved Chinese adjustment for contribution (1): `该算法首先从充放电数据及其衍生曲线中提取多类候选健康指标，再利用MS-CCCT标定充电时间特征的电压窗口。随后，以特征开发电池集合上的相关性结果为依据，综合评价候选指标与SOH的关联及指标间的冗余，并通过PCC/SCC双阈值与冗余约束筛选候选指标。` This is an editorial alignment proposal; frozen `source-zh/` is unchanged.
- Formal English module name remains `Linear Local-Global Fusion Attention (LLGFA)` as in Chapter 3; the frozen Chinese source retains its historical `SLFA` name. The one-sentence large-kernel Chinese meaning and all three contribution results remain unchanged.
- Working Chapter 1 and the English blocks in `full-manuscript-bilingual.md` synchronized. Compilation deferred at author request while introduction editing continues. Frozen Chinese Chapter 1 SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 resource-limited BMS model direction — approved 2026-09-15

- Exact frozen Chinese: 因此，面向计算能力、存储空间和实时性受到限制的BMS，SOH估计模型需要在保持有效表征能力的同时控制模型规模与资源开销，进一步向紧凑化和高效化方向发展。
- Approved English: Therefore, SOH estimation models need to become more compact and efficient while retaining effective representational capability to meet the real-time demands of resource-limited BMS.
- Backtranslation: 因此，SOH估计模型需要在保持有效表征能力的同时，向更紧凑、更高效的方向发展，以满足资源受限BMS的实时估计需求。
- Decisions: reread BMSFormer, JESSOHRUL, and Engineering-AI in their model-size/resource/realtime contexts and compared the preceding design-trend and resource-cost sentences. State the model direction directly; `more compact and efficient` conveys smaller model size and lower resource use without repeating both abstractions and their mechanisms. Use `real-time demands` as a design need, not a claim of validated deployment. Working chapter and bilingual file synchronized; frozen Chinese source unchanged. Compilation deferred at author request.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 deep-model design trend and resource demands — approved 2026-09-15

- Exact frozen Chinese: 近年来，深度模型架构发展的一个显著趋势是通过增加网络深度、扩大模型规模或引入更复杂的特征交互结构来增强表征能力。这些设计有助于提升模型对复杂退化规律的建模能力，但通常也伴随着更高的参数量、计算开销和存储需求。
- Approved English: In recent years, researchers have increasingly used deeper networks, larger models, or more complex feature interactions to enhance the representational capability of deep models. These designs help models capture complex degradation patterns but usually require more parameters, computation, and storage.
- Decisions: reread BMSFormer's direct trend-in-depth-and-size passage and its later model-complexity limitation, plus the resource trade-off context in JESSOHRUL and Engineering-AI. Shift the overloaded `a notable trend ... has been to improve ... by` main clause to researchers' design actions, retain three alternative routes and purpose with `to enhance`, and keep the already direct second sentence unchanged. Do not copy BMSFormer's stronger `predominant` or unsupported `unnecessary parameter updates`. Working chapter and bilingual file synchronized; frozen Chinese source unchanged. Compilation deferred at author request.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 contribution 1 selected-HI outcome — approved 2026-09-15

- Exact frozen Chinese: 统一的筛选规则为各数据集确定相应的健康指标组合，入选指标在同一数据集的其他电池上仍保持较强的线性和单调相关性。
- Approved English: The same selection rules determine a health indicator combination for each dataset, and the selected indicators retain strong linear and monotonic correlations with SOH on other cells in that dataset.
- Decision: make the SOH correlation target explicit and simplify the rule/result transition; retain the same-dataset, other-cell boundary. Only this sentence is approved and applied. The preceding calibration/selection order remains under review. Frozen Chinese source unchanged; compilation deferred.

## Chapter 1 cross-cell HI stability and model deployment — approved 2026-09-15

- Exact frozen Chinese: 在健康指标方面，不同电池在材料体系和运行条件上存在差异，所选指标能否在不同电池间保持稳定的退化表征能力仍需进一步关注。在模型方面，除估计性能外，模型复杂度同样直接关系到实际部署。
- Approved English: For health indicators, differences in battery chemistries and operating conditions make it important to examine whether selected indicators consistently reflect degradation across multiple battery cells. In addition to estimation performance, model complexity is directly related to practical deployment.
- Decisions: remove the unclear `their degradation representations` reference; retain the open `whether` question and cross-cell condition. Reuse JESSOHRUL's `across multiple battery cells` and Engineering-AI's battery-chemistry vocabulary in matching contexts, while keeping the already approved `representational capability` wording in the preceding selection sentence. Move the performance qualifier before the model-complexity claim without strengthening its deployment conclusion. Frozen Chinese source unchanged; working chapter and bilingual file synchronized. Compilation deferred at author request.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 comparison-table introduction — approved 2026-09-15

- Exact frozen Chinese: 现有SOH估计方法之间的比较总结于\Cref{tab:soh-method-comparison}。具体而言，重点考察各方法是否充分利用电池运行数据中的退化信息，是否采用有效的健康指标提取与选择策略，是否通过针对性的模型设计兼顾估计性能与计算效率，以及是否开展模型复杂度评价。
- Approved English: Existing SOH estimation methods are compared in \Cref{tab:soh-method-comparison}. The comparison examines whether they fully use degradation information in battery operating data, apply effective health indicator extraction and selection strategies, balance estimation performance and computational efficiency through targeted model design, and evaluate model complexity.
- Decisions: put methods directly in the first main clause, keep the four Chinese evaluation criteria and their qualifiers, and avoid closely reproducing JESSOHRUL's `comparison ... is summarized` plus `Specifically, it is examined` sequence. JESSOHRUL uses `Efficiency considered` in its survey table while describing model-complexity experiments in the corresponding prose, so the project's broad efficiency column and the fourth prose criterion are retained rather than classified as a confirmed error. Frozen Chinese source and table unchanged; English chapter and bilingual file synchronized. Compilation deferred at author request.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 health indicator selection rationale — approved 2026-09-15

- Exact frozen Chinese: 因此，有必要设计相应的健康指标筛选算法，将SOH相关性、跨电池表现与冗余关系纳入统一的评价与筛选过程，保留具有稳定表征能力的指标，减少弱相关和重复信息的输入，以帮助模型更有效地学习电池退化规律。
- Approved English: Therefore, a health indicator selection algorithm should be developed to jointly evaluate candidates' correlations with SOH, performance across cells, and redundancy among indicators. It should retain indicators with stable representational capability and reduce inputs weakly correlated with SOH or containing redundant information, helping the model learn battery degradation patterns more effectively.
- Decisions: mirror JESSOHRUL's direct algorithm-first progression and reuse `jointly evaluate`, `retain`, and `redundant information` only where the backtranslation preserves the Chinese criteria and purpose. Keep the established `representational capability` term; `should be developed` expresses a needed design, not an already proposed method. No new robustness or elimination claim. Updated working chapter and bilingual file; frozen Chinese source unchanged. Compilation deferred at author request until the current introduction-editing round is complete.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.

## Chapter 1 candidate-HI count and input-quality limitation — approved 2026-09-15

- Exact frozen Chinese: 然而，增加候选指标并不必然提高估计精度，表征能力较弱、跨电池表现不稳定或相互重复的指标，可能限制多源信息的有效利用，并增加模型的学习负担。
- Author-approved Chinese wording for explanatory comparison (not written to frozen source): 然而，增加候选指标并不必然提高估计精度。表征能力较弱、跨电池表现不稳定或信息冗余的指标可能限制多源信息的有效利用，并增加模型的学习负担。
- Approved English: However, adding more candidate indicators does not necessarily improve estimation accuracy. Indicators with weak representational capability, inconsistent performance across cells, or redundant information may limit the effective use of multi-source information and increase the model's learning burden.
- Decisions: `adding more` states the action directly; `inconsistent performance across cells` expresses cross-cell instability; `redundant information` corresponds overlapping indicator information, without claiming indicators are identical. Preserve `does not necessarily` and `may`. Frozen Chinese source unchanged; working chapter and bilingual file synchronized. Compilation deferred at author request until the current introduction-editing round is complete.

## Chapter 1 Lin feature optimization sentence — approved 2026-09-15

- Exact Chinese: Lin等人\cite{ref55}从电学、热学和电化学等角度构建多类特征，采用主成分分析进行降维，并利用模拟退火算法优化保留的特征维数，从而减少冗余并改善SOH估计表现。
- Approved English: Lin et al.\cite{ref55} constructed multiple features from electrical, thermodynamic, and electrochemical perspectives, used principal component analysis to reduce dimensionality, and optimized the number of retained dimensions with simulated annealing, thereby reducing redundancy and improving SOH estimation performance.
- Decisions: preserve “从……角度构建多类特征” through `multiple features from ... perspectives`; use ref55's `thermodynamic` classification; express retained feature dimensionality as the number of retained dimensions; and preserve the Chinese result relationship with `thereby`. Frozen Chinese source unchanged; chapter and bilingual record synchronized.

## Chapter 1 Dai per-cycle statistical features — approved 2026-09-15

- Exact Chinese: 例如，Dai等人\cite{ref48}从电压、电流、温度以及增量容量、差分热伏安曲线中提取健康指标，并计算这些指标在各循环下的均值、中位数等统计特征。
- Approved English: For example, Dai et al.\cite{ref48} extracted health indicators from voltage, current, temperature, incremental capacity, and differential thermal voltammetry curves and calculated statistical features such as the per-cycle means and medians of these indicators.
- Decisions: retain the direct `extracted ... from ... curves` and `statistical features such as ...` patterns found in JESSOHRUL; explicitly attach per-cycle means and medians to the health indicators. Do not borrow JESSOHRUL's different curve names for Dai's study. Frozen Chinese source unchanged; chapter and bilingual record synchronized.

## Chapter 1 multi-source indicator paragraph opening — approved 2026-09-15

- Exact Chinese: 不同运行数据及其衍生曲线能够从不同方面反映电池退化。为更充分地利用这些信息，一些研究从多种运行信号中构建候选健康指标，并进一步优化模型输入。
- Approved English: Different types of operating data and the curves derived from them reflect different aspects of battery degradation. To use this information more fully, some studies construct candidate health indicators from multiple operating signals and further optimize model inputs.
- Decisions: use `types of operating data` to express different data categories, directly attach derived curves to these data, and replace `make fuller use of` with `use ... more fully`. Retain `reflect`, `candidate health indicators`, and `model inputs` without adding reference claims about complementary features or multi-sensor scope. Frozen Chinese source unchanged; working chapter and bilingual file synchronized.

## Chapter 1 time-based health indicators and interval selection — approved 2026-09-15

- Exact Chinese: 相比之下，时间类健康指标无需微分处理，提取过程更为简单。其中，恒流充电时间（CCCT）可由所选电压区间两端对应时刻的差值获得。Richardson等人\cite{ref28}利用恒流充电曲线中不同电压区间的时间特征估计电池容量，Lin等人\cite{ref63}则将CCCT作为随机森林的输入，估计电池SOH。由于时间特征与容量之间的相关性会受到所选电压区间影响，相关研究通常需要进一步确定合适的特征提取区间。Tian等人\cite{ref51}通过优化充电电压区间，提高所提取健康指标与容量之间的相关性。在充电时间特征的区间选择中，Li等人\cite{ref31}逐步缩小电压窗口，并利用组内多节电池的皮尔逊相关系数（PCC）评价候选区间，以从更短的充电片段中提取与SOH高度相关的时间特征。
- Approved English: In contrast, time-based health indicators do not require differentiation and are simpler to extract. Constant current charge time (CCCT) can be obtained from the difference between the times corresponding to the two endpoints of a selected voltage interval. Richardson et al.\cite{ref28} used time features from different voltage intervals of constant-current charging curves to estimate battery capacity, while Lin et al.\cite{ref63} used CCCT as the input to a random forest to estimate battery SOH. Because the correlation between time features and capacity depends on the selected voltage interval, researchers generally need to identify a suitable interval for feature extraction. Tian et al.\cite{ref51} optimized the charging voltage interval, strengthening the correlation between the extracted health indicator and capacity. In selecting intervals for charging-time features, Li et al.\cite{ref31} progressively narrowed the voltage window and evaluated candidates using Pearson correlation coefficient (PCC) values from multiple cells in the same group, aiming to extract time features highly correlated with SOH from shorter charging segments.
- Decisions: retain the first and Richardson/Lin sentences; use JESSOHRUL's `time difference` for the CCCT definition; make interval selection apply to related researchers rather than only the two preceding studies; express Tian's stated correlation improvement as a result; distinguish PCC values across cells from a pooled coefficient; retain Li's extraction purpose with `aiming to`. Frozen Chinese source unchanged. Working chapter and bilingual record synchronized.

## Chapter 1 health-indicator source and Wen selection syntax — approved 2026-09-15

- Exact Chinese: 这些指标主要从电池循环过程中的电压、电流、温度、时间和内阻等运行数据及其衍生曲线中提取\cite{ref47,ref48,ref49,ref50}。例如，Wen等人\cite{ref50}从平滑后的增量容量曲线中提取峰值、峰位和峰形斜率等候选特征，并根据相关性分析选择峰值作为BP神经网络输入。
- Approved English source sentence: These indicators are mainly extracted from voltage, current, temperature, time, and internal resistance data recorded during battery cycling, as well as curves derived from these data\cite{ref47,ref48,ref49,ref50}.
- Approved English Wen sentence: For example, Wen et al.\cite{ref50} extracted candidate features such as peak values, peak positions, and peak-shape slopes from smoothed incremental capacity curves and used correlation analysis to select the peak value as the input to a BP neural network.
- Decisions: keep the first `In addition to the prediction model` sentence and all intervening sentences unchanged; move `during battery cycling` to the recorded data and explicitly relate curves to the data; attach correlation analysis to the action of selecting the peak value. Preserve the source's `peak-shape slopes` and existing `the input` without unsupported assumptions about their correctness or exclusivity. Frozen Chinese source unchanged; working chapter and bilingual file synchronized.

## Chapter 1 Transformer computational trade-off and online-use conclusion — approved 2026-09-15

- Exact Chinese: 然而，现有方法多通过集成其他模块或模型提高Transformer的预测精度，这种性能提升往往以增加参数量和计算开销为代价\cite{ref31}。与此同时，标准自注意力的计算瓶颈依然存在：它需要计算所有序列位置之间的两两关系，时间和存储复杂度随序列长度$N$呈二次增长，即$O(N^2)$\cite{ref39,ref40}。这些计算与存储需求增加了模型在资源受限BMS中的在线应用难度\cite{ref31}。
- Approved English: However, many existing methods improve Transformer prediction accuracy by integrating other modules or models, often at the cost of more parameters and higher computational overhead\cite{ref31}. Meanwhile, the computational bottleneck of standard self-attention remains: it computes pairwise relationships among all sequence positions, with time and memory complexity growing quadratically with sequence length $N$, namely $O(N^2)$\cite{ref39,ref40}. These computational and storage demands make it challenging to use such models online in resource-limited BMS\cite{ref31}.
- Decisions: preserve the Chinese claim that accuracy gains can incur parameter and computational cost; retain pairwise-attention and both time and memory $O(N^2)$ details; use the BMSFormer/EAI `challenging` pattern with a direct `use such models online` action. The frozen Chinese source remains unchanged. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`.

## Chapter 2 symbol definitions and MLP table note — approved 2026-09-13

- Chinese source: 其中，$V_{\mathrm{ch}}(t)$、$|I_{\mathrm{ch}}(t)|$、$t_{\mathrm{ch}}$ 与 $V_{\mathrm{dch}}(t)$、$|I_{\mathrm{dch}}(t)|$、$t_{\mathrm{dch}}$ 分别表示充电与放电阶段的端电压、电流幅值和持续时间，充电与放电均取完整循环过程。该能量效率记为 HI15（$\eta$）。
- Approved English: where $V_{\mathrm{ch}}(t)$, $|I_{\mathrm{ch}}(t)|$, and $t_{\mathrm{ch}}$ denote the terminal voltage, current magnitude, and duration of charging, respectively; $V_{\mathrm{dch}}(t)$, $|I_{\mathrm{dch}}(t)|$, and $t_{\mathrm{dch}}$ denote those of discharging. The full charging and discharging phases of each cycle are used. This energy efficiency is denoted as HI15 ($\eta$).
- Updated chapter02:98 and full-manuscript-bilingual.md. Six symbols, energy-efficiency formula and full-phase condition retained; one paragraph remains one paragraph.
- Author-approved explanatory addition to tables/table_4_4.tex: MLP denotes multilayer perceptron.
- Chinese gloss of added table note: MLP表示多层感知机。This is a new author-approved abbreviation explanation, not text translated from frozen source. No model layers changed.
- Reference evidence: BMSFormer full.txt:741 and 788–789; JESSOHRUL full.txt:1771–1772. Symbol grouping is an adaptation, not a verbatim quotation. BP, SOC and FLOPs remain unchanged.

## Chapter 4 readout-layer adaptation sentence — approved 2026-09-13

- Exact Chinese: 分别以 CS2\_36 和 CX2\_36 作为源域，使用 Oxford Cell1 的前置循环数据进行读出层适配，并将适配比例依次设置为 10\%、30\%、50\% 和 70\%，结果见\cref{tab:4-9}。
- Approved English: With CS2\_36 and CX2\_36 used as the respective source domains, the readout layer is adapted with early-cycle data from Oxford Cell1 at adaptation ratios of 10\%, 30\%, 50\%, and 70\%. The results are given in \cref{tab:4-9}.
- Updated chapters/chapter04.tex:132 and full-manuscript-bilingual.md. Only Using ... as changed to With ... used as; all data, source-domain roles, paragraph boundaries and references retained. This is grammatical adaptation, not a verbatim reference sentence. Frozen source unchanged; build status in progress.md.

## Chapter 3 parameter comparison — approved 2026-09-13

- Exact Chinese: 相较于标准查询、键和值线性投影约$3d^2$的参数量，三组通道缩放向量仅包含$3d$个参数，从而降低了查询、键和值生成过程中的参数开销。
- Approved English: Compared with standard linear projections for queries, keys, and values, which require approximately $3d^2$ parameters, the three channel scaling vectors contain only $3d$ parameters, reducing the parameter overhead of query, key, and value generation.
- Author approved the immediately preceding proposal. Updated chapters/chapter03.tex:288 and full-manuscript-bilingual.md; preserved mathematical expressions and paragraph boundary. This adapts the method-to-method comparison relationship, not a verbatim reference sentence. Frozen source unchanged; build status in progress.md.

## Chapter 1 convolution-fusion sentence — approved 2026-09-13

- Exact Chinese target: 然而，传统CNN的单层卷积受局部感受野限制，相距较远的特征通常需要经过多层卷积才能融合\cite{ref31}。
- Approved English: However, a single convolutional layer in a traditional CNN is limited by its local receptive field, and multiple convolutional layers are generally needed to fuse features that are far apart\cite{ref31}.
- Author accepted the version closer to BMSFormer full.txt:191–192 (convolutional layers to fuse local features), superseding the unimplemented before-they-can-be-fused proposal. Updated chapters/chapter01.tex:15 and the exact full paragraph in full-manuscript-bilingual.md. Citation, paragraph boundary, remaining sentences and frozen source unchanged. Build status in progress.md.

## Figure 4 caption and panel IDs — approved 2026-09-13

- Author approved updating the caption after discussing the panel mapping: (a) Cell1 PCC, (b) Cell1 SCC, (c) Cell2 PCC, (d) Cell2 SCC. This is the author-approved mapping, not a fresh verification against raw plotting data.
- Previous caption: Correlation matrices of candidate HIs and SOH on the Oxford dataset.
- Updated caption: Correlation matrices of candidate HIs and SOH on the Oxford dataset: (a) Cell1, PCC; (b) Cell1, SCC; (c) Cell2, PCC; (d) Cell2, SCC.
- Chinese gloss of updated caption (not a replacement of frozen Chinese): Oxford数据集上候选健康指标与SOH的相关矩阵：(a) Cell1，PCC；(b) Cell1，SCC；(c) Cell2，PCC；(d) Cell2，SCC。
- Working file: figures/figure_2_4.tex. Panel IDs added using LaTeX; original PNG and source-zh unchanged. Verification status is recorded in progress.md.

## Abstract paragraph 1 sentence 1 — approved 2026-09-13

- Source: source-zh/chapters/abstract.tex, paragraph 1, sentence 1. This approval covers only sentence 1; subsequent approvals are recorded separately below.
- Source file SHA-256: 640A5FC4F001E78FBB0EF5086743B130093955E95CA1E2A4661D66E3CF36284B.
- Exact Chinese: 高效准确的锂离子电池健康状态估计，对保障电池安全运行和支持资源受限电池管理系统的在线应用至关重要。
- Approved English: Efficient and accurate estimation of lithium-ion battery state of health (SOH) is crucial for ensuring safe battery operation and supporting online applications in resource-limited battery management systems (BMS).
- Author requested consistency with Cover_Letter.docx: resource-limited battery management systems, with (BMS) on first mention.
- Verification: checker PASS; XeLaTeX build passed (33 pages), with no undefined references/citations or LaTeX errors in final log. Source hash unchanged; paragraph boundary preserved. Image ICC warning also present before edit.

## Abstract paragraph 1 sentence 2 — approved 2026-09-13

- Source: source-zh/chapters/abstract.tex, paragraph 1, sentence 2.
- Source file SHA-256: 640A5FC4F001E78FBB0EF5086743B130093955E95CA1E2A4661D66E3CF36284B.
- Exact Chinese: 然而，现有估计方法往往依赖跨电池稳定性有限的健康指标和资源开销较大的模型结构。
- Approved English: However, many existing SOH estimation approaches often rely on health indicators (HIs) with limited stability across cells and resource-consuming model structures.
- Author approved many existing as the modifier; many is an explicitly authorized addition to the Chinese wording. Preserve often for 往往; do not add recent or state-of-the-art. Use health indicators (HIs), not SOH metrics.
- Reference function: BMSFormer abstract supplies the problem-statement pattern and resource-consuming structures; the HI stability limitation is specific to this manuscript. No numerical evidence or additional mechanism is introduced.
- Verification: checker PASS; XeLaTeX build passed (33 pages). Source hash unchanged; paragraph boundary preserved. Existing image ICC warning remains.

## Abstract paragraph 1 sentence 3 — approved 2026-09-13

- Source: source-zh/chapters/abstract.tex, paragraph 1, sentence 3.
- Source file SHA-256: 640A5FC4F001E78FBB0EF5086743B130093955E95CA1E2A4661D66E3CF36284B.
- Exact Chinese: 为此，本文提出一种轻量化的SOH估计框架。
- Approved English: Therefore, this paper proposes a lightweight SOH estimation framework.
- Reference function: JESSOHRUL abstract, TXT line 37, introduces the framework after the problem statement. Reuse Therefore and this paper proposes; retain confirmed lightweight, without adding novel. No protocol details or numerical claims apply to this sentence.
- Verification: checker PASS; XeLaTeX build passed (33 pages). Source hash unchanged; paragraph boundary preserved. Existing image ICC warning remains.
- Subsequent approval: sentences 4–9 and keywords are recorded below.

## Abstract paragraph 1 sentences 4–9 and keywords — approved 2026-09-13

- Source: source-zh/chapters/abstract.tex, paragraph 1, sentences 4–9, and keyword line.
- Source file SHA-256: 640A5FC4F001E78FBB0EF5086743B130093955E95CA1E2A4661D66E3CF36284B.
- Exact Chinese: 首先，提出多源健康指标提取与优化算法，以筛选跨电池稳健的健康指标并减少特征冗余。随后，构建轻量化预测网络MS-AgentNet。该网络主要集成局部—全局融合注意力模块，通过小核深度可分离卷积与ReLU²智能体注意力协同捕获局部退化特征与长程退化依赖，同时将传统Transformer的二次注意力复杂度降至线性。此外，大核深度可分离卷积用于提取长尺度退化特征，并与小核卷积共同以较低参数开销融合多尺度和多通道特征，增强特征多样性。我们在四个涵盖不同化学体系和运行条件的公开电池数据集上，将所提模型与多种主流深度学习模型进行了比较。实验结果表明，MS-AgentNet总体上取得了更优的综合性能，同时保持了较低的计算与存储开销，进一步体现了其面向资源受限电池管理系统的轻量化优势。
- Approved English: First, a multi-source health indicator extraction and optimization algorithm is proposed to select HIs that are robust across cells and reduce feature redundancy. Subsequently, a lightweight prediction network, MS-AgentNet, is constructed. The network mainly integrates a local-global fusion attention module that combines small-kernel depthwise separable convolutions with ReLU² agent attention to capture local degradation features and long-range degradation dependencies, while reducing the quadratic attention complexity of traditional Transformers to linear complexity. Additionally, large-kernel depthwise separable convolutions are used to extract degradation features over longer time scales and work with small-kernel convolutions to fuse multi-scale and multi-channel features with low parameter overhead, enhancing feature diversity. We compared the proposed model with various mainstream deep learning models on four public battery datasets with different chemistries and operating conditions. The experimental results show that MS-AgentNet achieves better overall performance while maintaining low computational and storage overhead, further highlighting the advantages of its lightweight design for resource-limited BMS.
- Exact Chinese keywords: 锂离子电池；健康状态估计；线性复杂度；深度特征融合；轻量化深度学习
- Approved English keywords: lithium-ion batteries; state-of-health estimation; linear complexity; deep feature fusion; lightweight deep learning
- Author approved the complete remaining batch after review, including the sentence 7 refinement from with few parameters to with low parameter overhead.
- Reference alignment: BMSFormer abstract supplies module-operation-effect and multi-scale fusion patterns; Engineering-AI supplies lightweight and long-range dependency terminology; JESSOHRUL supplies the HI-selection purpose pattern. Retain our nine-sentence sequence, four datasets, and qualitative overall results; no reference numerical results, RUL task, hardware validation, or deployment-completion claim is added.
- Checks: exact approved text written; source hash unchanged; checker PASS. Compilation verification recorded in progress.md.

## Abstract LLGFA dependency wording — approved 2026-09-16

- Latest approved module wording: `to capture local degradation features and long-term dependencies`.
- This replaces `to capture local degradation features and long-range degradation dependencies` in the current abstract and aligns the proposed LLGFA description with BMSFormer's Local-Global Fusion Attention wording.
- The Chapter 1 contribution already uses `captures long-term dependencies` and remains unchanged. Uses of `long-range dependencies` in the literature review may remain when they describe other cited attention mechanisms.
- Updated `chapters/abstract.tex` and `translation-guides/full-manuscript-bilingual.md`; the frozen Chinese source remains unchanged.

## Chapter 1 terminology alignment — approved 2026-09-16

- Define the abbreviation at its first occurrence in the introduction: `health indicators (HIs)`.
- Use `impedance spectrum measurements, which are time-consuming and require specialized instruments`, following the corresponding JESSOHRUL introduction wording and preserving the Chinese meaning of 阻抗谱测试.
- Expand the first occurrence of `BP neural network` as `backpropagation (BP) neural network`.
- Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; the frozen Chinese source remains unchanged.

## Chapter 1 P01 — approved 2026-09-13

- Source: source-zh/chapters/chapter01.tex, first natural paragraph before the first subsection.
- Source file SHA-256: D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D.
- Exact Chinese: 锂离子电池凭借高能量密度、长循环寿命和低自放电率等优势，已广泛应用于电动汽车、便携式电子设备和规模化储能等领域\cite{ref1,ref2,ref3,ref4}，是支撑新能源交通、智能终端和能源存储行业发展的重要储能技术。尽管如此，电池在长期运行中仍存在不可忽视的安全风险。充放电循环与复杂工况会引发固体电解质界面（solid electrolyte interphase, SEI）膜增厚、活性锂损失和电极结构衰退等老化现象\cite{ref5,ref6}，进而导致容量衰减和性能下降，严重时将诱发短路、热失控等故障\cite{ref7,ref8}。因此，精确估计锂离子电池的健康状态对于保障电池的安全性、可靠性和运行性能至关重要。
- Approved English: With their high energy density, long cycle life, and low self-discharge rate, lithium-ion batteries have found widespread use in electric vehicles, portable electronic devices, and large-scale energy storage\cite{ref1,ref2,ref3,ref4}. As an important energy storage technology, they support the development of transportation powered by new energy sources, smart devices, and the energy storage industry. However, batteries still pose safety risks that cannot be ignored during long-term operation. Charge-discharge cycling and complex operating conditions lead to aging processes such as thickening of the solid electrolyte interphase (SEI) layer, loss of active lithium, and structural degradation of the electrodes\cite{ref5,ref6}. These processes cause capacity fade and reduced performance and, in severe cases, lead to failures such as short circuits and thermal runaway\cite{ref7,ref8}. Therefore, accurate estimation of the state of health of lithium-ion batteries is crucial for ensuring battery safety, reliability, and operating performance.
- Six English sentences remain one paragraph, preserving source information order and all citation keys. Approved refinements: thickening rather than growth for 膜增厚; support the development of rather than support advances in.
- 新能源交通 remains descriptively translated as transportation powered by new energy sources; exact industry scope remains pending final author clarification, without narrowing to electric mobility.
- Reference/context review: introduction-p01-reference-analysis.md; all three reference opening paragraphs checked against PDFs. No external experiments or additional manuscript citations imported.
- Verification: checker PASS; XeLaTeX build passed (33 pages); existing image ICC warning remains. No manuscript edits beyond P01.

## Chapter 1 P02 — approved 2026-09-13

- Source: source-zh/chapters/chapter01.tex, second natural paragraph before the first subsection.
- Source file SHA-256: D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D.
- Exact Chinese: 容量衰减是电池老化最直观的特征，健康状态（state of health, SOH）通常采用容量保持率定义\cite{ref13,ref14}。但电池最大可用容量的精确测算需要完整或近似完整的充放电循环，难以满足在线监测需求\cite{ref10,ref11}。因此，从可观测运行信号中间接估计SOH已成为在线健康监测的关键途径。然而，复杂工况增加了退化信息稳定提取的难度，而电池管理系统（battery management system, BMS）严格的计算与存储限制又制约了模型复杂度，使在线SOH估计面临退化信息提取与模型计算效率的双重挑战\cite{ref31}。
- Approved English: Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurate measurement of a battery's maximum available capacity requires full or nearly full charge-discharge cycles, a requirement that is difficult to meet in online monitoring\cite{ref10,ref11}. Consequently, indirect estimation of SOH from observable operating signals has become a key approach to online health monitoring. However, complex operating conditions make the stable extraction of degradation information more difficult, while the strict computational and storage constraints of battery management systems (BMS) limit model complexity. These limitations pose a dual challenge for online SOH estimation: extracting degradation information and maintaining model computational efficiency\cite{ref31}.
- Approval follows the author's explicit instruction to prioritize the three reference papers. This entry approves the last presented version, not earlier alternatives.
- Terms: capacity fade, capacity retention, maximum available capacity, state of health (SOH), battery management systems (BMS). Preserve commonly and full or nearly full; no inherited model lists or added experimental facts.
- Five English sentences remain one paragraph; citations ref13/ref14/ref10/ref11/ref31 unchanged. Reference/context review: introduction-p02-reference-analysis.md.
- Verification: checker PASS; final compilation status recorded in progress.md.

For each approved batch record: source file and stable paragraph ID, exact Chinese text, exact approved English text, source SHA-256 or equivalent change check, glossary decisions, approval date, and verification status. Supersede entries explicitly when changed; never silently reuse approval for a changed source.

## Chapter 1 model-based approaches paragraph, sentences 1--3 — approved 2026-09-15

- Exact Chinese: 模型驱动方法通过数学方程或等效电路模拟电池内部的电化学机制\cite{ref19}。其中，电化学模型以微分方程表示电池的反应与退化过程。例如，Li等人\cite{ref21}基于单粒子模型（SPM），构建了同时考虑化学退化与机械损伤的SOH估计框架。
- Approved English: Model-based approaches simulate the internal electrochemical mechanisms of batteries using mathematical equations or equivalent circuits\cite{ref19}. Electrochemical models use differential equations to represent electrochemical reactions and degradation processes in batteries. For instance, Li et al.\cite{ref21} developed an SOH estimation framework based on a single-particle model (SPM), incorporating both chemical degradation and mechanical damage.
- Decisions: retain the author's intentional umbrella term `internal electrochemical mechanisms`; use the BMSFormer-aligned action-first pattern `simulate ... using ...`; translate 其中 implicitly through the direct `Electrochemical models` subject; use author-integrated citation placement after `Li et al.`; use `incorporating` to avoid a relative `that` clause.
- Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged. Compilation status is recorded in `progress.md`.

## Chapter 1 model-based approaches paragraph, sentences 4--7 — approved 2026-09-15

- Exact Chinese: 虽然这类模型具有较好的物理可解释性和估计精度，但求解复杂方程需要较多计算资源，颗粒半径、扩散系数等参数也难以获取，限制了其在资源受限BMS中的在线应用\cite{ref20,ref22,ref23}。相比之下，等效电路模型（ECM）将复杂的电化学过程简化为由电阻、电容等元件组成的电路，以模拟电池充放电动态特性\cite{ref19}。例如，Chen等人\cite{ref24}采用递推最小二乘法辨识Thevenin模型参数，并根据欧姆内阻与容量衰减的关系估计SOH。
- Approved English: Although these models are physically interpretable and can achieve high estimation accuracy, solving their complex equations requires extensive computational resources. In addition, parameters such as particle radius and diffusion coefficients are difficult to obtain. These limitations hinder the online application of electrochemical models in resource-limited BMS\cite{ref20,ref22,ref23}. In contrast, equivalent circuit models (ECMs) simplify complex electrochemical processes into circuits composed of resistors, capacitors, and other components to simulate battery charge-discharge dynamics\cite{ref19}. For example, Chen et al.\cite{ref24} used recursive least squares to identify the parameters of a Thevenin model and estimated SOH based on the relationship between ohmic internal resistance and capacity fade.
- Decisions: use direct, common wording aligned with the model-based discussions in BMSFormer and Engineering-AI; retain the Chinese information order and split the limitations into three English sentences for clarity. `ohmic internal resistance` is the complete technical term, and `based on the relationship` follows the meaning of 根据 and the wording of ref24.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged. Compilation status is recorded in `progress.md`.

## Chapter 1 ECM simplification trade-off sentence — approved 2026-09-15

- Exact Chinese: 这种简化降低了模型的计算开销，但也使其难以全面刻画电池内部状态的变化。
- Author-reviewed Chinese wording: 这种简化降低了模型的计算开销，但也限制了ECM全面刻画电池内部状态变化的能力。
- Approved English: This simplification reduces computational cost, but it also limits the ability of ECMs to fully capture changes in the internal state of the battery.
- Decisions: omit sentence-initial `However` because `but it also` already carries the contrast; use a comma between the two independent clauses and the natural `the ability of ECMs to` structure. `fully capture` follows the corresponding BMSFormer wording, adapted to preserve the explicit trade-off in the Chinese source.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 ECM accuracy sentences — approved 2026-09-15

- Exact Chinese: 与电化学模型相比，ECM的估计精度可能较低，且依赖于所选电路结构与模型参数。
- Approved English: Compared with electrochemical models, ECMs may achieve lower estimation accuracy. Their accuracy depends on the selected circuit structure and model parameters.
- Decisions: use `achieve ... estimation accuracy` for consistency with the preceding paragraph wording and the reference-paper style; retain the Engineering-AI sentence spine `Their accuracy depends on ...`, adding `model parameters` from the Chinese source. Keep two sentences so the dependence statement clearly applies to ECM accuracy in general.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 ECM operating-condition sensitivity sentence — approved 2026-09-15

- Exact Chinese: 此外，ECM参数对温度和充放电倍率等工况高度敏感，使其难以在整个老化周期内保持良好的估计鲁棒性\cite{ref19}。
- Author-reviewed Chinese wording: 此外，ECM参数对温度和充放电倍率等工况高度敏感，使ECM难以在整个老化周期内保持稳健的估计性能\cite{ref19}。
- Approved English: Furthermore, ECM parameters are highly sensitive to operating conditions, including temperature and charge-discharge rate, making it difficult for ECMs to maintain robust estimation performance throughout the battery aging process\cite{ref19}.
- Decisions: follow the corresponding Engineering-AI progression and comma structure while retaining the more direct `are highly sensitive to`; explicitly identify ECMs as the affected models; preserve `operating conditions` and the manuscript-wide `charge-discharge rate` wording.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 data-driven approaches opening sentence — approved 2026-09-15

- Exact Chinese: 相较于模型驱动方法，数据驱动方法无需建立详细的电化学模型或深入分析电池内部的反应及老化机制\cite{ref11,ref14}。
- Approved English: In contrast to model-based approaches, data-driven approaches avoid the need to develop detailed electrochemical models or extensively analyze electrochemical reactions and battery aging mechanisms\cite{ref11,ref14}.
- Decisions: preserve the explicit comparison object with `In contrast to model-based approaches`; adapt the directly corresponding JESSOHRUL sentence spine and use direct verbs instead of `an in-depth analysis of`; retain the manuscript-wide term `approaches`.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 early machine-learning sentence — approved 2026-09-15

- Exact Chinese: 早期研究主要采用传统机器学习模型进行电池状态估计与寿命预测\cite{ref25}。
- Approved English: Earlier studies primarily employed traditional machine learning models for battery state estimation and lifetime prediction\cite{ref25}.
- Decisions: use `Earlier studies` to support the later transition to deep learning and the reference-aligned `primarily employed`; preserve both tasks and the established `traditional machine learning models` term.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 data-driven traditional-ML paragraph — approved 2026-09-15

- This full-paragraph approval supersedes the earlier sentence-level records for the data-driven opening and early machine-learning sentence.
- Exact Chinese: 相较于模型驱动方法，数据驱动方法无需建立详细的电化学模型或深入分析电池内部的反应及老化机制\cite{ref11,ref14}。这类方法利用历史运行数据训练模型，将提取的健康指标映射为SOH估计值。早期研究主要采用传统机器学习模型进行电池状态估计与寿命预测\cite{ref25}。例如，Fei等人\cite{ref26}从前100个循环的充放电数据中构造42个特征，经筛选后输入弹性网络、高斯过程回归（GPR）、支持向量机（SVM）、随机森林（RF）、梯度提升回归树（GBRT）和神经网络（NN）六种模型，比较其早期寿命预测表现。Li等人\cite{ref27}则利用局部充电过程中的电压和容量数据，通过随机森林实现在线容量估计。然而，当面对来自在线监测和历史循环的非线性、波动性数据时，传统机器学习模型因其结构限制而难以提供高性能。
- Approved English: In contrast, data-driven approaches avoid the need to develop detailed electrochemical models or extensively analyze electrochemical reactions and battery aging mechanisms\cite{ref11,ref14}. Instead, they train models on historical operating data to map extracted health indicators to SOH estimates. Earlier studies primarily employed traditional machine learning models to estimate battery states and predict battery lifetime\cite{ref25}. For instance, Fei et al.\cite{ref26} crafted 42 features from charge--discharge data collected over the first 100 cycles. After feature selection, the retained features were fed into six models: elastic net, Gaussian process regression (GPR), support vector machine (SVM), random forest (RF), gradient boosting regression tree (GBRT), and neural network (NN). Their performance in the early prediction of battery lifetime was then compared. Li et al.\cite{ref27} used a random forest to estimate battery capacity online from partial charging voltage--capacity data. However, when faced with nonlinear and fluctuating data from online monitoring and historical cycling, traditional machine learning models struggle to achieve high predictive performance because of their structural limitations.
- Decisions: retain the explicit contrast through paragraph context; use `Instead` for method progression, direct task verbs, the BMSFormer-aligned `For instance` and `crafted 42 features`, and a colon plus shorter sentences for the six-model comparison. All source quantities, algorithms, tasks, and citation keys are preserved.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 early deep-learning/CNN paragraph — approved 2026-09-15

- Exact Chinese: 随着深度学习的快速发展，研究者进一步采用多层神经网络，利用其较强的非线性表征能力捕捉复杂的电池退化模式，以提高估计精度\cite{ref14}。卷积神经网络（CNN）、循环神经网络（RNN）和Transformer是其中常用的模型。CNN利用卷积核提取局部特征，并通过池化操作降低特征维度。例如，Qian等人\cite{ref29}将随机选取的充电曲线片段输入一维CNN，用于电池容量估计。结果表明，该方法在随机片段输入条件下取得了较低的容量估计误差。Lee等人\cite{ref30}则将跨循环的容量衰减序列转换为二维图像，并采用二维CNN估计SOH。
- Approved English: With the rapid development of deep learning, researchers have increasingly adopted multilayer neural networks. These networks have strong nonlinear representational capabilities and can therefore capture complex battery degradation patterns and improve estimation accuracy\cite{ref14}. Common deep learning models include convolutional neural networks (CNNs), recurrent neural networks (RNNs), and Transformers. CNNs extract local features using convolutional kernels and reduce feature dimensionality through pooling operations. For example, Qian et al.\cite{ref29} fed randomly selected charging-curve segments into a one-dimensional CNN for battery capacity estimation. The results showed that the method achieved low capacity estimation errors with randomly selected segments as inputs. Lee et al.\cite{ref30} transformed capacity fade sequences across cycles into two-dimensional images and employed a two-dimensional CNN for SOH estimation.
- Decisions: split the long opening source sentence within the same paragraph; use plural `representational capabilities` for natural grammar; adopt the reference-aligned `Common ... include`, direct CNN operations, and author-integrated citation placement. No source claim or condition is removed.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 CNN--RNN limitations and hybrid-model paragraph — approved 2026-09-15

- Exact Chinese: 然而，传统CNN的单层卷积受局部感受野限制，相距较远的特征通常需要经过多层卷积才能融合\cite{ref31}。为建立这些远距离联系，RNN通过隐藏状态将历史信息传递到后续时间步；其变体长短期记忆网络（LSTM）和门控循环单元（GRU）进一步利用门控机制选择性地保留和更新历史信息，以捕捉长期依赖\cite{ref14}。为同时利用局部特征与历史信息，研究者将CNN与循环网络相结合。例如，Xu等人\cite{ref41}将CNN提取的特征输入LSTM，利用LSTM的时序记忆能力估计SOH。Tian等人\cite{ref42}在CNN与BiLSTM的组合中进一步引入注意力机制，构建了CNN-BiLSTM-AM预测模型。Zheng等人\cite{ref33}则采用CNN-GRU，根据随机充电过程中的电压、电流和温度曲线片段估计SOH。尽管如此，这类模型中的隐藏状态仍需按时间步串行更新，限制了训练和推理过程中的并行计算\cite{ref31}。
- Approved English: However, a single convolutional layer in a traditional CNN has a limited local receptive field, and fusing distant features generally requires multiple convolutional layers\cite{ref31}. RNNs establish these long-range connections by passing historical information to subsequent time steps through hidden states. RNN variants, including long short-term memory (LSTM) and gated recurrent unit (GRU) networks, further employ gating mechanisms to selectively retain and update historical information to capture long-term dependencies\cite{ref14}. Researchers have also combined CNNs with recurrent networks to capture local features while retaining historical information. For example, Xu et al.\cite{ref41} fed CNN-extracted features into an LSTM and used its temporal memory to estimate SOH. Tian et al.\cite{ref42} further incorporated an attention mechanism into a CNN-BiLSTM architecture to develop the CNN-BiLSTM-AM prediction model. Zheng et al.\cite{ref33} employed a CNN-GRU to estimate SOH using segments of voltage, current, and temperature curves obtained during random charging. Nevertheless, the hidden states in these models still require sequential updates across time steps, limiting parallel computation during training and inference\cite{ref31}.
- Decisions: follow the BMSFormer and Engineering-AI progression from limited CNN receptive fields to RNN sequential constraints; use direct action subjects, parenthetical `including`, and author-integrated citations. Preserve `further` for Tian et al., the random-charging condition, and both training and inference in the final limitation.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 Transformer transition sentence — approved 2026-09-15

- Exact Chinese: 为解决这一问题，Vaswani等人\cite{ref34}提出了Transformer。
- Approved English: To address this limitation, Vaswani et al.\cite{ref34} proposed the Transformer.
- Decisions: use `this limitation` to refer specifically to the immediately preceding sequential-update constraint. PDF-level review confirmed that BMSFormer uses `To address the above problem` for the same CNN/RNN-to-Transformer transition, while JESSOHRUL uses `To address this limitation` after a single stated defect; the Engineering-AI `computational bottleneck` wording frames a broader paper-level problem and is therefore not imported here.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 Transformer introduction and mechanism — approved 2026-09-15

- This entry supersedes the earlier sentence-level `Chapter 1 Transformer transition sentence` record; the preceding Park and Kim / Chen example remains unchanged.
- Exact Chinese: 为解决这一问题，Vaswani等人\cite{ref34}提出了Transformer。该模型避免循环递推，利用自注意力直接建立不同序列位置之间的联系，在捕捉长程依赖的同时支持并行计算。
- Approved English: To address this limitation, Vaswani et al.\cite{ref34} proposed the Transformer, which avoids recurrence and uses self-attention to directly connect different sequence positions, capturing long-range dependencies while supporting parallel computation.
- Decisions: combine the introduction and model explanation as in the corresponding BMSFormer passage, with a natural comma-plus-`which` construction. Sentence-level Chinese backtranslation confirmed that `directly`, long-range dependencies, and parallel computation are retained. Do not merge the subsequent literature example into this sentence.
- Source file SHA-256: `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`. Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 Transformer hybrid-model purpose verb — approved 2026-09-15

- Exact Chinese: 研究者还将Transformer与卷积或循环网络相结合，以提高预测精度。
- Previous English: Researchers have also combined Transformers with convolutional or recurrent networks to improve prediction accuracy.
- Approved English: Researchers have also combined Transformers with convolutional or recurrent networks to enhance prediction accuracy.
- Decision: use the JESSOHRUL introduction's `enhance prediction accuracy` for a literature-method purpose, retaining purpose rather than asserting a verified improvement. Surrounding Gu/Jia/Bai sentences remain unchanged.
- Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged.

## Chapter 1 SOH-method classification paragraph — approved 2026-09-14

- Exact Chinese: 近期的健康状态估计方法主要分为模型驱动和数据驱动两类\cite{ref10,ref11,ref12}。前者包括电化学模型和等效电路模型，后者包括传统机器学习和深度学习方法。
- Approved English: Recent approaches to SOH estimation can generally be classified as model-based or data-driven\cite{ref10,ref11,ref12}. The former include electrochemical models and equivalent circuit models, while the latter include traditional machine learning and deep learning methods.
- Reference alignment: `Recent approaches to SOH estimation` and `can generally be classified` follow the corresponding JESSOHRUL passage; `model-based` remains the manuscript-wide term supported by BMSFormer and Engineering-AI. The shorter `classified as` construction avoids switching between `approaches` and `methods` within the classification complement.
- Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`; frozen Chinese source unchanged. Compilation status is recorded in `progress.md`.

## Chapter 1 P01--P02 language revision — approved 2026-09-14

- This entry supersedes the English versions in the earlier `Chapter 1 P01` and `Chapter 1 P02` records. The frozen Chinese source remains unchanged; source SHA-256 remains `D001D1FC9CEAFB54A858181735DC20BDC018C3A80C238A2C5E405E1520C2652D`.
- P01 approved English: With high energy density, a long cycle life, and a low self-discharge rate, lithium-ion batteries have become one of the most important electrochemical energy storage technologies, widely used across consumer electronics, electric mobility, stationary energy storage, and other domains\cite{ref1,ref2,ref3,ref4}. Despite these advantages, lithium-ion batteries still pose considerable safety risks as they age. Charge-discharge cycling and complex operating conditions can induce degradation processes such as thickening of the solid electrolyte interphase (SEI), loss of active lithium, and structural degradation of the electrodes\cite{ref5,ref6}. These processes lead to capacity fade and performance degradation and can, in severe cases, trigger failures such as short circuits and thermal runaway\cite{ref7,ref8}. Therefore, precise estimation of lithium-ion battery state of health (SOH) is essential for maintaining battery safety, reliability, and performance.
- P01 author decisions: use `consumer electronics`, `electric mobility`, `stationary energy storage`, and `other domains`; omit `their`; use `one of the most important`; use reference wording `precise estimation` and `essential`; retain concrete failure wording rather than the broader `safety issues`.
- P02 approved English: Capacity fade is the most direct sign of battery aging, and state of health (SOH) is commonly defined in terms of capacity retention\cite{ref13,ref14}. However, accurately measuring a battery's maximum available capacity requires full or nearly full charge-discharge cycles, which are impractical for online monitoring\cite{ref10,ref11}. Consequently, inferring SOH from measurable operating signals has become a key approach to online battery health monitoring. Nevertheless, complex operating conditions make it harder to consistently extract degradation information, while the limited computing power and storage space of battery management systems (BMS) constrain model complexity. Together, these factors pose a dual challenge for online SOH estimation: extracting degradation information and achieving computational efficiency\cite{ref31}.
- P02 author decisions: prefer direct verb phrases and reference-like wording; retain the explicit effect of BMS resource limits on model complexity; use `achieving computational efficiency` for the second challenge.
- Updated `chapters/chapter01.tex` and `translation-guides/full-manuscript-bilingual.md`. Compilation status is recorded in `progress.md`.
# Whole-manuscript authorization record — 2026-09-13

2026-09-13 23:40 作者批准“有原因且不改原意即可采取”后，实施既定候选中的10处正文修改（第1章2处、第2章1处、第3章3处、第4章4处）；FLOPs句因实施前已有较新清楚表述而保留。两名agent原意复核、精确差异及保护项检查通过；中文源稿全部哈希不变。latexmk编译成功37页，9个受影响页面目视检查通过；第1/3章检查器提示与实施前一致，既有ICC/字体/locale警告保留，无溢出或未定义引用提示。全文中英对照未重建；当前英文以chapters为准。准确修改及验证见 [本轮落实记录](D:/MS-AgentNet-English/translation-guides/language-style-applied-2026-09-13.md)。
本记录按该次语言修改授权更新此前对应句批准版本；其余历史内容不被重新批准或覆盖。本轮未新增或更换技术术语。

2026-09-13 本任务后续明确批准：“可以改动”，对应english-style-audit-2026-09-13.md的A2、C1、F3、D1四处完整改前/改后。四处已应用，精确差异及独立复核通过，37页编译及表格页视觉检查通过。其他建议不在此批准范围；历史对照文件不是本批最新正文。

2026-09-13 作者明确选择的四类语言修改已落实六处；准确修改前后表达和验证见 language-fixes-batch-01.md，完整中英段落见 full-manuscript-bilingual.md。此批批准不包含图7、Oxford协议或其他审查建议。

The author later explicitly authorized autonomous translation and writing of the entire remaining manuscript. Exact source/target pairs for that scope are in full-manuscript-bilingual.md; batch checks are in autonomous-translation-log.md and final-translation-review.md. This authorization does not relabel the later paragraphs as individually approved. The earlier individual approval records below are retained.
# Whole-manuscript terminology consistency — authorized implementation 2026-09-16

作者在全文专业术语报告后明确要求：“再仔细思考一下我担心有漏，开agent再去找，我们现在来修改即可”。在本轮授权范围内，三名agent独立复查后实施3组8处术语一致性修改：charging-time feature(s)、battery chemistries、final HI subset。准确文件、原英文、新英文及三篇依据见 [本轮落实记录](technical-terminology-applied-2026-09-16.md)。正文7处已同步中英对照英文块；筛选表1处同步最终输出名称。此记录仅更新列明短语，不重新批准或改写其余历史版本。cross-position context等合理区别及作者已知旧图名保留；冻结中文未改。

# LGFA formal module name — approved 2026-09-16

作者明确确认将正式模块名称统一为 `Local-Global Fusion Attention (LGFA)`。活动英文中的 `Linear Local-Global Fusion Attention (LLGFA)`、`Slim Local-Global Fusion Attention (SLFA)`及模块简称`SLFA`据此更新；论文标题保留作者给定的概括性表达`local-global attention`。本次批准包括摘要、第一章、第三章、表4-4和图3-3图注；作者明确要求不修改位图本身。冻结中文源稿、内部LaTeX标签和旧审查记录不改。

# Chapter 1 contribution (3) — approved 2026-09-16

作者在重新对照BMSFormer、Engineering-AI和JESSOHRUL引言后批准更新贡献（3）。最终英文采用JESSOHRUL“多数据集验证→评价对象→结果”的表达路径，同时保留本文独有的模块消融、复杂度分析、跨电池泛化和跨数据集迁移边界。`provide a comprehensive evaluation of`替代原来的`together with ... jointly evaluate`结构；`cross-cell generalization capability`与`cross-domain adaptation capability`继续分别表示同数据集跨电池表现和跨数据集适应。中文源稿不改。


## Application-focused revisions — 2026-09-17

作者撤回引言综述补充后确认按原有改动落实。落实引言贡献（2）、3.3.2末段、3.3.3引入段，共3段；RAA可选补充未实施。下列中文为本轮确认内容，不覆盖冻结中文源稿；英文为按该授权落实的工作稿。完整中英对照文件未同步，本轮以此记录和正文为准。

### chapters/chapter01.tex:46

确认中文：

构建轻量级局部—全局网络 MS-AgentNet。局部—全局融合注意力（LGFA）模块结合小核深度可分离卷积与 ReLU² 智能体注意力，以较低参数开销将局部特征提取与全局上下文建模相结合。相较于标准自注意力，其注意力计算复杂度关于序列长度由 O(N²) 降低至 O(N)。模型进一步引入大核深度可分离卷积，与小核卷积共同提取不同时间尺度的退化特征。这些设计旨在增强模型对长期退化趋势和短期容量波动的表征能力，在控制计算与存储开销的同时提高 SOH 估计精度。

落实英文：

(2) \textbf{A lightweight local-global network, MS-AgentNet, is constructed.} A Local-Global Fusion Attention (LGFA) module combines small-kernel depthwise separable convolutions with ReLU$^2$ agent attention to integrate local feature extraction and global context modeling with low parameter overhead. Compared with standard self-attention, its attention computation reduces the complexity with respect to sequence length from $O(N^2)$ to $O(N)$. The model further introduces large-kernel depthwise separable convolutions, which, together with small-kernel convolutions, extract degradation features at different time scales. These designs aim to enhance the model's representation of long-term degradation trends and short-term capacity fluctuations and improve SOH estimation accuracy while limiting computational and storage overhead.

### chapters/chapter03.tex:267

确认中文：

上述线性注意力通过重组计算顺序降低了全局信息交互的开销，但其计算过程未显式引入局部邻域特征。在电池 SOH 估计中，健康指标序列不仅包含退化趋势，也包含相邻循环的局部变化。模型在建立循环间依赖关系时，仍需充分利用其中的细粒度退化信息。因此，有必要将局部特征提取与高效注意力机制相结合，在控制计算开销的同时增强对电池退化过程的表征。

落实英文：

The linear attention described above reduces the cost of global information interactions by rearranging the computation order, but it does not explicitly incorporate local neighborhood features\cite{ref31,ref39,ref64}. In battery SOH estimation, health indicator sequences contain both degradation trends and local variations between neighboring cycles. When modeling dependencies across cycles, the model still needs to make full use of the fine-grained degradation information in these sequences. Local feature extraction therefore needs to be combined with an efficient attention mechanism to enhance the representation of battery degradation while limiting computational overhead.

### chapters/chapter03.tex:271

确认中文：

为兼顾退化特征提取与计算效率，本文将小核深度可分离卷积 DSConv-S 与 ReLU² 智能体注意力（RAA）相结合，构建局部—全局融合注意力（LGFA）模块，如图 3-3(d) 所示。DSConv-S 增强健康指标序列的输入表征，在保留序列结构的同时丰富局部信息，所得表示分别进入局部分支与 RAA 分支。局部分支将局部增强表示直接传递至融合端，RAA 分支则基于这一表示进行全局上下文建模。两个分支的输出经加法融合，为 SOH 估计提供兼顾局部退化细节与全局上下文的特征表示。

落实英文：

To balance degradation feature extraction and computational efficiency, this study combines small-kernel depthwise separable convolution (DSConv-S) with ReLU² Agent Attention (RAA) to form the Local-Global Fusion Attention (LGFA) module, as shown in \cref{fig:3-3}(d). DSConv-S enhances the input representation of health indicator sequences by enriching local information while preserving the sequence structure. The resulting representation is fed into both the local and RAA branches. The local branch passes the locally enhanced representation directly to the fusion stage, while the RAA branch uses it to model global context. The outputs of the two branches are fused by addition to provide SOH estimation with a feature representation that incorporates both local degradation details and global context.


## DSConv introduction A — approved 2026-09-17

作者明确给定以下中文并要求采用，仅落实A项，B项DSConv-L和C项结论仍待审核。

位置：chapters/chapter03.tex:52。

确认中文：

为平衡特征提取能力与计算效率，采用大小核深度可分离卷积捕获多尺度局部依赖，在增强特征多样性的同时控制参数开销。本节首先介绍标准卷积与深度可分离卷积的计算特性，随后说明 DSConv-S 和 DSConv-L 的结构配置及作用。

落实英文：

To balance feature extraction capability and computational efficiency, small- and large-kernel depthwise separable convolutions are used to capture multi-scale local dependencies, enhancing feature diversity while limiting parameter overhead. This section first introduces the computational characteristics of standard and depthwise separable convolutions, followed by the configurations and roles of DSConv-S and DSConv-L.

保留作者删去的轻量级卷积先验等措辞的删除决定，不再补回。source-zh与完整中英对照文件未修改。


## DSConv application explanations — approved 2026-09-17

作者确认按最终清单落实，以操作与健康指标退化信息的联系为重点。实施DSConv-S两项功能、DSConv-L说明段及结论概括句，共4处。§3.2引入沿用作者已定稿版本。以下中文为本轮内容确认稿，英文为依此授权落实的工作稿；不覆盖冻结源稿。

### chapters/chapter03.tex

确认中文：

输入增强。为提取健康指标序列中的细粒度退化信息，DSConv-S 对相邻循环的特征表示进行局部建模，形成局部增强表示 X_S。其中，深度卷积提取各通道内的局部依赖，逐点卷积整合不同通道的特征。RAA 随后基于 X_S 构造查询、键和值，并通过智能体聚合与广播建立循环间关联，使上下文聚合能够利用卷积提取的局部变化信息。

落实英文：

1. \textbf{Input enhancement.} To extract fine-grained degradation information from health indicator sequences, DSConv-S models local relationships between the feature representations of neighboring cycles to form a locally enhanced representation $\mathbf X_S$. Depthwise convolution extracts local dependencies within each channel, while pointwise convolution integrates features across channels. RAA then constructs queries, keys, and values from $\mathbf X_S$ and establishes relationships across cycles through agent aggregation and broadcasting, allowing context aggregation to use the local variation information extracted by convolution.

### chapters/chapter03.tex

确认中文：

局部分支保留。在进行循环间信息交互的同时，X_S 还经层归一化后由局部分支传递至融合端，并与 RAA 分支输出相加。这一路径将局部增强后的健康指标表示直接送入融合端，与 RAA 建立的全局上下文共同形成 SOH 估计所需的局部—全局联合表征。

落实英文：

2. \textbf{Local branch preservation.} Alongside information interactions across cycles, $\mathbf X_S$ passes through layer normalization and is carried by the local branch to the fusion stage, where it is added to the RAA branch output. This path passes the locally enhanced health indicator representation directly to the fusion stage, combining it with the global context established by RAA to form a joint local-global representation for SOH estimation.

### chapters/chapter03.tex

确认中文：

DSConv-L 位于 LGFA 之后，用于进一步细化已融合局部信息与全局上下文的特征表示。该模块通过 1×1 逐点卷积将通道维度扩展至三倍，以提取丰富的表征，随后采用 1×31 深度卷积在各通道内捕获较长时间尺度的局部序列模式。第二个 1×1 逐点卷积跨通道整合这些特征，并恢复原始通道维度。整体变换顺序与 DSConv-S 一致，残差连接在 MS-AgentNet Block 层面实现，如相应公式所示。卷积输出经可学习系数缩放后，与原有 LGFA 输出相加，将进一步提取的序列特征融入已有表示。通过注意力前的局部增强与融合后的特征细化，大小核卷积共同丰富用于 SOH 估计的多尺度退化表征。

落实英文：

DSConv-L follows LGFA to further refine the feature representation that combines local information and global context. A $1\times1$ pointwise convolution first expands the channel dimension by a factor of three to extract rich representations, followed by a $1\times31$ depthwise convolution that captures local sequence patterns over longer time scales within each channel. A second $1\times1$ pointwise convolution integrates these features across channels and restores the original channel dimension. The transformation order is the same as in DSConv-S, and the residual connection is applied at the MS-AgentNet Block level, as shown in Eq.~\eqref{eq:block_dsconv_l}. The convolution output is scaled by a learnable factor and added to the original LGFA output, incorporating the further extracted sequence features into the existing representation. Through local enhancement before attention and feature refinement after fusion, the small- and large-kernel convolutions jointly enrich multi-scale degradation representations for SOH estimation.

### chapters/chapter05.tex

确认中文：

在序列建模方面，MS-AgentNet 将 ReLU² 智能体注意力与大小核深度可分离卷积相结合，通过局部特征提取与全局上下文建模，增强对局部退化变化和较长时间尺度退化趋势的表征能力。

落实英文：

For sequence modeling, MS-AgentNet combines ReLU² agent attention with small- and large-kernel depthwise separable convolutions to enhance the representation of local degradation variations and degradation trends over longer time scales through local feature extraction and global context modeling.


## 应用补充修改执行确认 — 2026-09-17

作者追问后续建议为什么未落实，明确要求完成此前引言、架构、逐点卷积、RAA、融合收束及两处精简。已写入chapter01第42行与chapter03第9、68、108、139、174、275、384行，共8个段落、9项文本替换；包括JE的local sequential patterns对齐。准确改前改后见 application-supplement-applied-2026-09-17.md，修改前快照及changes.json见build/application-supplement-applied-20260917/。本记录更新对应批准英文；此前8处成果不撤销，局部分支及DSConv-L说明以本轮精简版为准。完整中英对照旧文件未同步；现稿与本落实记录为准。

## 注意力数据语境修订批准落实 — 2026-09-17

作者批准将多源信号、长期循环数据与HI序列建模需求接入注意力引入，并要求尽可能避免“在本文中”等草稿式措辞。已替换chapter03.tex第267、271、275行；LGFA引入的this study combines亦改为无作者自指的组合说明。准确中文、旧英文和新英文见 attention-data-context-applied-2026-09-17.md。本记录更新这三段较早版本，其余批准内容不变。冻结中文不改，旧全文中英对照未同步。

## 注意力引入节奏调整 — 2026-09-17 最新确认

作者批准按原中文紧凑节奏重写chapter03:267/271/275，并要求第三段仍加入应用解释。已落实三段；第三段保留键值聚合与查询读取机制，再以一句窗口内健康指标表示共享退化信息、建立循环间联系收束。准确中英与历史英文见attention-rhythm-applied-2026-09-17.md。本记录取代attention-data-context-applied同位置的英文版本；不影响其他已确认段落。冻结中文与旧全文中英对照不改。

## 模型论述四处收束调整 — 2026-09-17

作者给出进一步修改意见并明确“然后改动，图不需要改动”。已落实chapter01:46贡献（2）、chapter03:1总导语、chapter03:271 LGFA引入及chapter03:174 DSConv-L段落。准确中英文与改前改后见application-flow-final-applied-2026-09-17.md。此记录更新上述四处历史版本，其余已确认内容保留。未新增RAA/ReLU²应用句，未将longer time scales全局替换。图片及图注按作者要求不改。

## 消融中文完整稿对应英文已落实 — 2026-09-17

作者提供3442a19b附件作为完整中文消融审核稿，按其段落顺序转换并落实：第4节导语句、4.6导语、4.6.1动机与M1–M4定义、Table16四段、Table17配置定义与三段结果。表16新增Average/Reduction注释，表17改为模块配置表题和DSConv-S/L表头。准确现稿及记录见ablation-final-applied-2026-09-17.md；中文原稿和修改前快照见build/ablation-final-applied-20260917/。复杂度正文、图及冻结中文未改。旧全文中英对照未同步。

## §3.3导语与RAA首段最终确认 — 2026-09-17

作者明确要求总导语原样采用、RAA末句去掉重复efficient并采用最终提供英文。已替换chapter03:191/275，准确中英文与改前改后见raa-intro-final-applied-2026-09-17.md。原Agent Attention文献键ref46保留，不硬编码附件中的显示编号66。中文agent统一代理，英文术语不变。该记录更新两段较早版本，其余批准内容不变。

## 消融与结论五处范文措辞收紧 — 2026-09-17

已按作者给定五处范围落实chapter04三段中的四项与chapter05结论一句。准确改前改后见ablation-wording-final-applied-2026-09-17.md。采用fine-grained local degradation patterns、complementary roles/effects及joint integration，不采用synergistic effect。Table17前两句已含DSConv-S/L分工，故第3项只替换连续处理过程句，不重复相同功能。结论采用作者推荐第二版，移除convolutional-scale experiments旧逻辑。结构、数字及两表不变。


## 复杂度九处最终方案落实 — 2026-09-17

作者确认后落实九处，包含正文n=4及两处电池应用术语补回。详见complexity-final-applied-2026-09-17.md。表格数字和引用不变，未改图、冻结中文或新增实验环境。
