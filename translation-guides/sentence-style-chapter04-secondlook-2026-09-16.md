# 第四章第二轮：从纠错进一步到范文风格优化

状态：建议，未改正文，未编译。保留上一轮记录；本记录修正上一轮“没有值得修改的新语言问题”的过宽结论，不将风格建议冒充语法错误。

本轮重新读取第四章英文与中文、JE的HI结果及资源分析、BMS的指标/结果/效率比较、SL的初始化/收敛及精度—资源权衡完整对应段。上一轮的句级样本仍有效；本轮重点是主语与动作的选择、名词堆叠及搭配，不以句长或修改数量为指标。

## C4-S1：HI结果采用JE的动作主语——建议

位置：chapter04.tex:43第一句。

现句：
> The results show that HI1 maintains high estimation accuracy across Cell2--Cell8, with the lowest average MAE, RMSE, and MAPE among the five input schemes.

建议：
> The results show that using HI1 consistently yields high estimation accuracy across Cell2--Cell8, with the lowest average MAE, RMSE, and MAPE among the five input schemes.

理由：将“HI维持精度”改为“使用HI得到精度”，直接写出输入选择与估计结果的关系；consistently保留中文“始终”，所有指标及比较范围不变。

范文依据：JE full.txt:1960–1968 用 using the CVT feature 作主语推进高精度及Fusion比较，是相同的HI输入比较功能。JE:1884–1893同时也允许直接用feature作主语，因此原句不是错误，建议是更贴近其对应结果句。BMS:1309–1326、SL:1363–1401常以模型作结果主语；不是相同HI对比对象，不强制套用。

## C4-S2：拆开收敛统计的连续名词——建议

第三轮查重补注：本项与 `english-style-audit-2026-09-13.md` 的 G3（约375–390行）属于同一问题。第二轮采用不拆句的最小版本；保留 C4-S2 作为当前引用编号，但不再计作独立新发现，也不同时应用两个版本。

位置：chapter04.tex:66，数值汇总句。

现句：
> The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

建议：
> The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median standard deviations of the late-stage loss are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

理由：这是“词汇简单但表达绕”的局部问题：median / late-stage / loss / standard deviations 连续前置，读者要回头判断修饰关系。改用 of 明确统计对象；median仍然修饰各次训练的SD，未改成先取loss中位数再算SD。前句已定义最后20轮，本句不重复扩写。

范文依据：SL full.txt:1319–1330在末20轮稳定性说明中采用 The standard deviation of the loss；同一统计对象，本文另保留跨运行的median限定。BMS:1937–1947、JE:1201–1226的训练设置并非相同SD统计，不提供强制模板，也不借其均值/验证方法改本文。SL自身也用紧凑名词短语，不能据此把所有名词组合列错。

## C4-S3：LSTM局限采用BMS的能力—动作搭配——建议

位置：chapter04.tex:170第一句。

现句：
> Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low.

建议：
> Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its ability to capture complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low.

理由：representation既可指表征行为也可指表征产物；这里中文说的是模型刻画模式的局限。ability to capture明确表达能力及动作，比抽象representation of更贴合这句话。保留“仍有局限”、相对较低、具体时间及统一测试范围，不增加因果。

范文依据：BMS full.txt:1670–1679在LSTM训练时间—精度权衡中使用 ability to capture complex degradation patterns，技术对象和句子功能均对应。JE:3826–3849及SL:2440–2453也讨论容量/资源权衡，但并不要求都采用同一个能力名词。仅借BMS局部搭配，不复制其顺序结构导致训练时间优势的解释，不将本文并列结论改成因果。

## 仍不建议改的类型

多组百分比、必要目的限定、source-only/few-shot边界、负R²以及轻量化应用potential继续保留。动词show/indicate/yield/achieve在三篇中共存，不轮换或强行统一。没有证据支持系统加强形容词或加入significantly、superior等评价。
