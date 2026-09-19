# 第四章英文审查：逐节简表

覆盖词汇、句式、介词、从句及形容词力度。**作者已批准，以下10项已实施；按要求未编译。**表中保留改前→改后记录；S为C4-S编号，V/R同理。4.4两项待核内容未改。

## 4.1 评价指标

|编号/处理|现有表达 → 建议表达|理由及范文依据|
|---|---|---|
|S7 可选·本轮新增|`does not further amplify individual large deviations` → `does not assign extra weight to individual large errors`|以误差权重说明MAE，与RMSE段平行。BMS全文1233–1249；借其RMSE搭配适配，并非范文MAE原句。|

**小结：1项可选；其余指标名称、公式和限定保留。**

## 4.2 HI筛选结果

|编号/处理|现有表达 → 建议表达|理由及范文依据|
|---|---|---|
|S1 建议|`HI1 maintains high estimation accuracy` → `using HI1 consistently yields high estimation accuracy`|明确使用HI与结果的关系，保留“始终”。JE全文1960–1968。|
|S6 可选|`HI1 obtained through group-level selection` → `HI1, which is obtained through group-level selection,`|明确来源只修饰HI1；JE1888–1891使用同功能分词插入说明，此处适配为which。|

**小结：2项已有建议；不强换high/strong，也不强制所有HI都以using作主语。**

## 4.3 训练与超参数

|编号/处理|现有表达 → 建议表达|理由及范文依据|
|---|---|---|
|S5 建议|`the training stability of MS-AgentNet and the parameter settings of the lightweight model` → `the training stability and parameter settings of the lightweight MS-AgentNet model`|两个对象共享of，减少重复指代；lightweight仍修饰模型。JE3329–3333。|
|S2 建议·历史重复合并|`median late-stage loss standard deviations` → `median standard deviations of the late-stage loss`|展开名词堆叠，保留中位数统计。SL1319–1330；与9月13日G3合并。|
|S4 可选|`The comparison of three initialization schemes is presented in \cref{tab:4-3-initialization}.` → `\Cref{tab:4-3-initialization} compares the three initialization schemes.`|表作主语，动作更直接。JE1960、BMS1938；SL也允许原类被动句。|
|V1 可选|`Their configuration ranges are listed…` → `The hyperparameter search space is listed…`；后文`within these ranges` → `within this search space`|复用SL1260–1286。若采用，表4-1题名改为`Hyperparameter search space of MS-AgentNet.`，表头改为`Search space/Values`；不新增grid search声明。|

**小结：4项已有建议。保留at which、similar performance及small参数幅值含义，不改变初始化分布。**

## 4.4 模型比较

|旧待核项|处理|
|---|---|
|`local deviations in Cell4`|需明确指真实SOH变化还是预测误差；不擅自改成突降、膝点。旧方案同时调整lead to因果关系，需确认原意。|
|`more continuous trajectories`|连续与平滑不等义，不直接换成smoother。|

依据：BMS1309–1326、JE1970–1991、SL1363–1409；只借结果组织方式，不移植具体曲线现象。

**小结：无新增；两项旧语义问题继续保留标记。whose、relatively smooth、only及多组百分比保留。**

## 4.5 跨数据集迁移

- 保留source-only与few-shot边界，以及误差下降但部分R²仍负的限制。
- `with`表示设置/所用数据，`at`表示比例，`from…to…`表示变化起止，关系清楚。
- `continuously`承接四档已测比例；旧精确化选项不重复计数。三篇没有完全相同的迁移协议模板。

**小结：无新增；不批量换介词，不加强迁移成功的结论。**

## 4.6 消融与复杂度

|编号/处理|现有表达 → 建议表达|理由及范文依据|
|---|---|---|
|S3 建议|`its representation of complex degradation patterns remains limited` → `its ability to capture complex degradation patterns remains limited`|明确LSTM的能力与动作，不增加因果。BMS1670–1679。|
|R1 可选·旧项|154行`Overall, the full model provides more consistent combined performance` → `The full model provides more consistent overall performance`；158行`more consistent combined results` → `more consistent overall results`|普通“综合表现”采用overall，指标名combined average error不改。JE3514、2888。|
|S8 可选·本轮新增|`while M4 performs better in RMSE, MAPE, and combined average error` → `while M4 achieves lower RMSE, MAPE, and combined average error`|明确误差更低，保留前半句M3的MAE例外。SL1363–1374；表4-10支持。|

**小结：已有S3/R1，新增可选S8。保留may、并列最低、consistent with及应用potential。**

## 总结

原清单共 **4项建议、6项可选，现已全部获批实施**。正文12处、表4-1两处，并同步双语稿对应英文12处。数值与中文核对通过；章首和4.4待核内容保留。未编译，未做新版PDF排版检查。备份及精确差异：`build/ch4-approved-style-20260916-165619/`。

证据中的行号均指`style-references/论文名/full.txt`；SL对应Engineering-AI，JE对应JESSOHRUL。

[详细原句、证据与保真核对](chapter04-section-by-section-review-detailed-2026-09-16.md) · [历史去重台账](chapter04-style-review-ledger-2026-09-16.md)
