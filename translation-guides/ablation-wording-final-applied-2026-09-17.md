# 消融与结论五处措辞调整

2026-09-17。按作者指定五处调整，结构、段落顺序及全部数字不变。第3处保留前两句已清楚给出的DSConv-S/L分工，仅替换连续特征处理过程句，避免重复；第4处采用作者最后核心句的不带明显修饰版本，不引入统计显著性主张；结论采用作者推荐第二版。表格、图和冻结中文未改。

## 1. chapters/chapter04.tex

改前：

```tex
Multi-scale DSConv supplements fine-grained local degradation dynamics in the health indicator sequences, while RAA establishes cross-cycle context within the input window through agent aggregation and broadcasting.
```

改后：

```tex
Multi-scale DSConv captures fine-grained local degradation patterns in the health indicator sequences, while RAA establishes cross-cycle context within the input window.
```

## 2. chapters/chapter04.tex

改前：

```tex
This allows local variations between neighboring cycles and degradation relationships across cycles to jointly contribute to the SOH representation, making the combined structure better suited to describing complex degradation trajectories that contain both local variations and overall evolution.
```

改后：

```tex
Their joint integration allows the model to use both fine-grained local degradation patterns and cross-cycle context, providing a more complete representation of complex degradation trajectories.
```

## 3. chapters/chapter04.tex

改前：

```tex
Acting before and after information interaction, the two modules form a continuous sequence of local enhancement, cross-cycle context modeling, and post-fusion feature refinement, enriching degradation representations at different levels.
```

改后：

```tex
The two convolutional modules thus play complementary roles at different feature-processing stages, further enriching the model's degradation representations.
```

## 4. chapters/chapter04.tex

改前：

```tex
Across the two ablation studies, the prediction error comparisons support the complementary effects between multi-scale DSConv and RAA and between DSConv-S and DSConv-L. Through pre-attention local enhancement, cross-cycle context modeling within the input window, and feature refinement after local-global fusion, MS-AgentNet combines feature processing at different stages to form degradation representations for SOH estimation. The current ablation results support the contributions of these structures in combination at the prediction-error level, but do not establish a one-to-one correspondence between a particular convolutional kernel and a specific physical degradation mechanism.
```

改后：

```tex
Together, the two ablation studies show complementary effects between multi-scale DSConv and RAA and between DSConv-S and DSConv-L. DSConv-S enhances fine-grained local degradation features before cross-cycle interaction, RAA establishes cross-cycle context within the input window, and DSConv-L further refines the feature representation after local-global fusion. Their joint integration provides a more complete degradation representation for SOH estimation. The current results do not establish a one-to-one correspondence between a specific convolutional kernel size and a physical degradation mechanism.
```

## 5. chapters/chapter05.tex

改前：

```tex
Ablation studies and additional convolutional-scale experiments show that the complementary fusion of multi-scale depthwise separable convolutions and RAA improves overall performance under different degradation scenarios.
```

改后：

```tex
Ablation studies further show complementary effects between multi-scale DSConv and RAA and between DSConv-S and DSConv-L, contributing to more consistent overall performance across degradation scenarios.
```
