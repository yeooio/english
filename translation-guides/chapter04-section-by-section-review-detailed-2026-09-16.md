# 第四章逐小节范文对齐审查：一次性交付

2026-09-16。状态：仅建议，未修改英文正文、中文源稿或表格，未编译。覆盖章首与4.1

## 章首总述

覆盖第1行完整实验总览。保留systematically、comprehensive及实验类别—各自用途—总结的层次，中文已有这些内容。JE实验章导语采用相似总述和分类；不能因词汇简单就删掉段落功能，也不能要求每篇范文同句数。

**小结：保留；无新增建议。**

## 4.1 评价指标

覆盖5—37行，含四个指标说明、公式引导与符号解释。公式和数字未重算；语言检查不替代计算验证。

### C4-S7：用误差权重表述MAE的特点——本轮新增低优先可选

现句：
> It does not further amplify individual large deviations and provides a direct measure of overall estimation accuracy.

建议：
> It does not assign extra weight to individual large errors and provides a direct measure of overall estimation accuracy.

中文核对：“不会进一步放大单个较大偏差”，在此指不对大误差额外加重影响。assign extra weight把这一解释落到指标对误差的处理上，与下一段RMSE assigns greater weight平行；保留后半句总体精度解释。不是要求更改MAE定义，也不声称误差大小不影响MAE。

范文尺度：BMS full.txt:1233–1249的完整指标段用giving larger weight to larger errors解释RMSE；这里是根据本文MAE原意作相应改写，**不是范文MAE原句**。JE:1140–1146主要列公式，SL:1199–1205强调RMSE penalizes larger prediction errors，三篇并未统一使用本建议。旧报告保留原“不放大”写法，原句可理解；本项仅是新表达路径，不把旧判断变成数学错误。

保留：root mean square error在JE/SL有依据；of the mean squared difference关系明确；true/predicted修饰SOH；may保留可能性。of/which不为配额增加，RMSE解释不照搬SL安全后果。

**小结：新增1项可选；其余保留，不改指标名和公式。**

## 4.2 HI筛选结果与有效性

覆盖41、43、45行。比较对象是单项HI与Fusion；不是模型结构消融。保留across cells、for SOH estimation、representational ability of the same HI及原有指标。

### C4-S6：将HI1来源作为which插入说明——低优先可选

位置：chapter04.tex:41，第四句。

现句：
> These HIs and the CCCT indicator HI1 obtained through group-level selection are separately fed into MS-AgentNet.

建议：
> These HIs and the CCCT indicator HI1, which is obtained through group-level selection, are separately fed into MS-AgentNet.

理由：长复合主语中，which is明确以单数HI1为先行词；两个逗号把“组级筛选所得”作为来源补充，之后返回整组主语的are fed。三项HIs来自Cell1筛选，HI1来自组级筛选，关系保持。原句就近附着也能读懂，因此只列低优先可选；不要求为了出现which而增加从句。

范文依据/尺度：JE full.txt:1888–1891用CVT feature, extracted using …, consistently achieves …，同为特定HI来源的插入说明。JE采用省略关系词的分词形式，不应谎称它原句使用which。本文复合主语较长，显式which is用于突出仅修饰HI1，是有理由的适配。BMS:1359–1368用which are测量从句插在指标名与主干之间；JE:3829–3840用which补充基线属性；SL:1326–1330也用which说明模块作用。后几例仅支持说明性从句功能，不代表本文需要追加其测量或机制事实。

不同时采用另一个“, obtained through …,”版本；与which版是同一问题，不分开计数。历史原句快照未见这项明确改写建议。

### C4-S1：HI结果采用JE的动作主语——建议

位置：chapter04.tex:43第一句。

现句：
> The results show that HI1 maintains high estimation accuracy across Cell2--Cell8, with the lowest average MAE, RMSE, and MAPE among the five input schemes.

建议：
> The results show that using HI1 consistently yields high estimation accuracy across Cell2--Cell8, with the lowest average MAE, RMSE, and MAPE among the five input schemes.

理由：将“HI维持精度”改为“使用HI得到精度”，直接写出输入选择与估计结果的关系；consistently保留中文“始终”，所有指标及比较范围不变。

范文依据：JE full.txt:1960–1968 用 using the CVT feature 作主语推进高精度及Fusion比较，是相同的HI输入比较功能。JE:1884–1893同时也允许直接用feature作主语，因此原句不是错误，建议是更贴近其对应结果句。BMS:1309–1326、SL:1363–1401常以模型作结果主语；不是相同HI对比对象，不强制套用。

补充保留：inputs that remain stable限定目标输入；high correlation与strong correlation范文共存，不能一律改strong；more stable input保留本组电池范围。并未为复用范文补significantly/greatly。

**小结：保留已有S1建议、S6低优先可选；无本轮新增，不重复编号。**

## 4.3 训练鲁棒性与超参数

覆盖50、54、61、63、65、73、75、79行；当前行号与早期记录可能相差1，以原句定位。

### C4-S5：两个并列对象共享同一个of限定——建议

位置：chapter04.tex:50。

现句：
> To further examine the training stability of MS-AgentNet and the parameter settings of the lightweight model, this study analyzes agent matrix initialization, model convergence, and hyperparameter configuration.

建议：
> To further examine the training stability and parameter settings of the lightweight MS-AgentNet model, this study analyzes agent matrix initialization, model convergence, and hyperparameter configuration.

理由：MS-AgentNet与the lightweight model指同一模型。将training stability与parameter settings并列，共享of the lightweight MS-AgentNet model，减少重复指代；lightweight仍修饰model，未把“轻量化”限定到参数设置或训练稳定性。保留目的、三个分析项目和原顺序。这是词汇简单但表达有可减少重复的局部改善，不是原句语法错。

范文依据/尺度：JE full.txt:3329–3333以effectiveness and efficiency of the proposed model组织两个评价维度的共同对象，属于同功能实验导语；SL:1231–1236以同一模型的初始化和收敛行为并列介绍；BMS:1344–1351也并列评价对象，但其后同时使用多个of，说明不能机械删除所有重复介词。此处改动成立的关键是本文两次指向同一模型，而不是of数量。

中文核对：“MS-AgentNet的训练稳定性及轻量化模型的参数设置”，其中模型同一。没有删除轻量化或改变参数的技术身份。历史检索命中原句快照，未找到同一共享of改法；不与S2的统计量of展开混算。

### 4.3.1 智能体初始化与收敛

以下S4和S2均为已有建议，不计本轮新增。

#### C4-S4：初始化比较表直接作主语——已有低优先可选

定位：第四章初始化比较段首句（本轮当前文件约63行，以原句定位为准）。

现句：
> The comparison of three initialization schemes is presented in \cref{tab:4-3-initialization}.

建议：
> \Cref{tab:4-3-initialization} compares the three initialization schemes.

中文原意：三种初始化方案的对比结果如表所示。建议用表作主语、compares作动作，直接指出三种比较对象，减少comparison + is presented的名词化被动。表内实际列三种初始化；不改数值、指标、比较结论或段落划分。

范文完整语境：本轮重读JE full.txt:1946–1968及1884–1893，1960以Table 7 shows引出比较指标；BMS:1927–1947，1938以Table 8 presents引出超参表并解释各列。SL:1451–1479也有As presented in Table 9, the comparison reveals，说明原句同类结构并非不合范文。三个例子比较的实验不同，只借表引导功能，不声称三篇比较了本文的三种初始化。

判断：有轻度直接性收益，列可选，不能升级为“词汇简单但严重绕”。也不因此把所有is presented in批量替换。查重命中原句快照，但本轮检索未发现历史明确提出这一个表主语版本；与初始化删尾、S2统计修饰和R1整体表现并非同一问题。

#### C4-S2：拆开收敛统计的连续名词——已有建议

第三轮查重补注：本项与 `english-style-audit-2026-09-13.md` 的 G3（约375–390行）属于同一问题。第二轮采用不拆句的最小版本；保留 C4-S2 作为当前引用编号，但不再计作独立新发现，也不同时应用两个版本。

位置：chapter04.tex:66，数值汇总句。

现句：
> The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median late-stage loss standard deviations are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

建议：
> The median convergence threshold epochs are 26 and 7 on the Oxford and MIT datasets, respectively, and the median standard deviations of the late-stage loss are $2.38\times10^{-4}$ and $4.84\times10^{-6}$.

理由：这是“词汇简单但表达绕”的局部问题：median / late-stage / loss / standard deviations 连续前置，读者要回头判断修饰关系。改用 of 明确统计对象；median仍然修饰各次训练的SD，未改成先取loss中位数再算SD。前句已定义最后20轮，本句不重复扩写。

范文依据：SL full.txt:1319–1330在末20轮稳定性说明中采用 The standard deviation of the loss；同一统计对象，本文另保留跨运行的median限定。BMS:1937–1947、JE:1201–1226的训练设置并非相同SD统计，不提供强制模板，也不借其均值/验证方法改本文。SL自身也用紧凑名词短语，不能据此把所有名词组合列错。

**4.3.1小结：S2建议、S4可选；定义性质的that、时间关系at which和分布属性with均保留。**

### 4.3.2 超参数配置

#### C4-V1：超参数候选范围与SL的search space对齐——已有可选

位置：chapters/chapter04.tex:73，tables/table_4_1.tex:3、7。表格仅为核对对象及提出联动建议，本轮未修改。

现有英文：
> Their configuration ranges are listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within these ranges.

建议英文：
> The hyperparameter search space is listed in \cref{tab:4-1}. For each dataset, one cell in the feature-development set is used to learn model parameters, and a second is used to select hyperparameters within this search space.

若采纳，表格一起采用：

- 表题：`Hyperparameter configuration range of MS-AgentNet.` → `Hyperparameter search space of MS-AgentNet.`
- 表头：`Configuration range` → `Search space/Values`。

中文核对：原意是各参数的可选配置范围，并在其中选择超参；表内确实列离散候选值（0.001/0.01，1/2/4/8，16/32/64/128）。search space对应允许选择的候选集合，不改变数值、训练/配置电池角色，也不改变已选模型配置。

范文原词及完整语境：SL full.txt:1260–1286表6题名含 Hyperparameter grid search space，表头为 Search space/Values；1294–1338上下文说明先选择、后固定配置。本文借用search space/Values，不添加grid。JE:1208–1226明确predefined hyperparameter values及grid search；BMS:1867–1903、1930–1947用组合及超参设置说明候选与评价，两篇并没有要求任何候选列表都必须叫search space。

范文是否也如此/同条件：三篇都区分候选值和选定配置，与本文是同类超参选择功能。但JE/SL明确grid search，本文本段未声明穷举，因此不能照搬完整方法名或声称评价全部组合。configuration ranges原文可理解，故只列为优先复用范文词汇的可选项，不报术语错误。

表达收益：将“参数配置”与“供选择的候选空间”区分，正文、表题、表头统一使用一个对象名。不是把全文所有configuration换成search；已选定的configuration继续保留。

保留：at which对应阈值轮次；matrix that is independent…两个谓语同指矩阵；with a mean of 0说明分布；small修饰幅值，lightweight修饰模型。similar performance不升级为统计等效。普通正态不能改成standard normal或范文的截断正态。训练电池与配置电池的角色不变。

**小结：已有2项建议（S5、S2）和2项可选（S4、V1）；无本轮新增。S2与9月13日旧建议合并，只选一个版本。**

## 4.4 精度与跨电池泛化

覆盖85、90、94、96、103、105、107、109行；包含Oxford及CALCE/MIT两个小节。

### 4.4.1 Oxford

保留“总体趋势—局部变化—量化结果”的推进。BMS full.txt:1309–1326同样在具体电池观察后列多组误差降幅；JE:1970–1991、SL:1363–1409也以真实曲线与局部表现组织结果。多组数值长句不因为长就删比较对象。whose degradation trajectories中whose明确所属关系；relatively smooth修饰轨迹，保留中文相对程度。

**旧对象澄清仍单列，不当作新发现或已解决：**

现句：
> In particular, the local deviations in Cell4 and the rapid decline in the later stage of Cell6 lead to different degrees of tracking error.

若作者所指为真实SOH局部变化，旧建议是：
> In particular, the models show different degrees of tracking error in regions with local changes in the true SOH of Cell4 and a rapid late-stage decline in the true SOH of Cell6.

来源：source-language-review-results-2026-09-14.md第1项。该改法同时把lead to的因果改为区间内的观察，不能当成纯介词修复自动应用。旧主审曾查看曲线，但本轮没有重新核验图形；原意与是否采用观察关系仍按作者确认处理。

**4.4.1小结：无新增；保留local deviations旧对象澄清项。**

### 4.4.2 CALCE与MIT

保留which指向CX2_38、whose指向两节电池；only对应“仅”，best对应“最优”，不升级为superior。nonlinear degradation tail有SL full.txt:258–261支持，但范文的具体电池事实不能迁移。

more continuous与smoother意义不同，旧语义候选仍不能靠范文词形盲改。maintains close agreement与closely follow都与三篇对应结果表述相容，不强制统一。107行整体MAPE与尾段观察的旧衔接候选保留历史状态：前段已有放大图，不要求新增尾段实验。

**小结：无本轮新增；有旧对象/语义候选需保留标记，不能写成整节“绝无问题”。数字、比较范围和限定保留。**

## 4.5 跨数据集迁移

覆盖117、119、123、125、132、135、137行。两个子节分别检查方向比较与目标域比例。

### 4.5.1 不同迁移方向

source-only与few-shot定义、source/target角色及参数更新范围清楚。between用于两个域之间，in用于某方向/条件内部，without限定不使用目标数据更新参数。MAE下降与Oxford方向R²仍负同时保留。三篇的跨电池评价不是相同迁移实验，因此只参考设置—结果—解释的句式，不伪造同协议模板。

represents degradation trends→fits/captures属于旧可选偏好，不新立编号；中文“表征”不必全部改成“拟合”。

**4.5.1小结：无新增；改善与仍有负R²的限制同时保留。**

### 4.5.2 适配比例

with引入各源域设置，from…to…表示比例和数值变化，at限定具体比例，across/all four范围不扩展。continuously承接已列四档结果；改成at each successive ratio是旧精确化选项，不报为无限外推错误。137行A comparison是历史修复产物，不改回缺比较主体的Comparing…结构。

**小结：无本轮新增；已有边界清楚，保留旧可选记录，不批量替换介词或把改善写成迁移已成功。**

## 4.6 消融与模型复杂度

覆盖145、149、152、154、156、158、166、168、170、172行。

### 4.6.1 模块及卷积尺度消融

### C4-R1：combined performance / combined results → overall——旧项可选

来源：`whole-manuscript-review.md:178` 已提出同一建议；此次补入总台账，不计新发现。

154行现句：
> Overall, the full model provides more consistent combined performance than the single-module variants, showing the complementary roles of multi-scale local feature extraction and cross-position information interactions.

建议句：
> The full model provides more consistent overall performance than the single-module variants, showing the complementary roles of multi-scale local feature extraction and cross-position information interactions.

158行现句：
> Thus, retaining both small and large kernels provides more consistent combined results than using a single scale, supporting the multi-scale DSConv design.

建议句：
> Thus, retaining both small and large kernels provides more consistent overall results than using a single scale, supporting the multi-scale DSConv design.

中文保真：两处均为普通“综合表现/综合结果”，不是定义一个新的组合运算。overall表达总体结果；154句首Overall的概括功能移入overall performance，避免重复。保留更一致、单模块/单尺度比较对象、互补及支持力度，不改数字。

范文依据及尺度：本轮重读JE full.txt:3493–3533消融完整语境，3514出现overall performance，3515–3517给出组合后更一致的准确性；另读2877–2893，2888使用overall results。BMS:1670–1700按多个资源及精度指标概括综合表现；SL:2288–2332区分单模块和combined gain。因此三篇允许combined描述组合效果，原句不是硬错。本文这两处中文强调总体表现，overall可更明确，属于可选搭配对齐。

范围约束：全文的 `combined average error` 作为既有指标名保持；不能批量替换combined。本文前句已经交代模块组合，改overall不删组合事实。也不能从SL的combined gain引入超加性、唯一机制或更强因果。

### C4-S8：把better明确为误差更低——本轮新增低优先可选

现句：
> On CS2, M3 has a slightly lower MAE than M4, while M4 performs better in RMSE, MAPE, and combined average error.

建议：
> On CS2, M3 has a slightly lower MAE than M4, while M4 achieves lower RMSE, MAPE, and combined average error.

理由：保留while的两模型对照及M3在MAE上的例外，用achieves lower直接陈述其余误差量方向，减少better in的笼统评价；不加显著性。中文“其余指标表现更优”在误差量语境中就是更低。表4-10的CS2行也支持这三个方向。

范文尺度：SL full.txt:1363–1374用achieves a lower average MAE报告结果；JE:3493–3533消融段同时使用泛称performance improvements及具体误差降低；BMS:1309–1326也同时概括performed the best和给出误差。原句是允许的概括，本建议只使比较更具体，不报语法错。历史检索未找到同一替换建议；与R1的overall搭配不是同一问题。

保留：may weaken / can improve保持可能性；which has…附着CX2；lowest or jointly lowest保留并列最低；is consistent with/supporting不加强成prove。152双前置是旧可选；156 held fixed由四变体组成帮助消歧，retain RAA是旧结构澄清选项，不当作新增冻结误译。

**4.6.1小结：新增S8可选，R1为旧可选；不改变例外、并列最低及设计支持力度。**

### 4.6.2 模型复杂度

### C4-S3：LSTM局限采用BMS的能力—动作搭配——建议

位置：chapter04.tex:170第一句。

现句：
> Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its representation of complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low.

建议：
> Although LSTM has the shortest training time of 44.568 s in the unified complexity test, its ability to capture complex degradation patterns remains limited, and its overall SOH estimation accuracy is relatively low.

理由：representation既可指表征行为也可指表征产物；这里中文说的是模型刻画模式的局限。ability to capture明确表达能力及动作，比抽象representation of更贴合这句话。保留“仍有局限”、相对较低、具体时间及统一测试范围，不增加因果。

范文依据：BMS full.txt:1670–1679在LSTM训练时间—精度权衡中使用 ability to capture complex degradation patterns，技术对象和句子功能均对应。JE:3826–3849及SL:2440–2453也讨论容量/资源权衡，但并不要求都采用同一个能力名词。仅借BMS局部搭配，不复制其顺序结构导致训练时间优势的解释，不将本文并列结论改成因果。

保留：指标定义中obtained using与required for都明确修饰对象；不为增加which将所有分词展开。BMS full.txt:1344–1398、JE:3795–3849定义单次前向、时间、参数和存储；SL:2410–2453有不同的整周期/延迟口径，只借资源权衡表达。with说明输入长度/设置，of说明参数数量/时间长度，for说明前向用途。good balance不换optimal，potential不改已部署。

**小结：本轮新增S8低优先可选；已有S3建议、R1旧可选继续保留。指标名、数值及部署潜力限定不变。**

## 全章汇总

|小节|当前建议|可选|旧对象/范围说明|
|---|---|---|---|
|4.1|无硬性修改要求|S7（本轮新增）|指标定义和公式保留|
|4.2|S1|S6|特定HI来源与全组范围不变|
|4.3|S5、S2|S4、V1|S2历史重复合并；只改一个版本|
|4.4|无本轮新增|历史衔接可选留档|local deviations、more continuous不冒充已解决|
|4.5|无本轮新增|旧fits/比例限定选项不重计|适应与source-only边界保留|
|4.6|S3|R1、S8（本轮新增）|152/156旧项不重计|

共集中展示4项风格建议（S1/S2/S3/S5）及6项可选（S4/S6/S7/S8/V1/R1）；这是当前选择清单，不是本轮新发现数。R1覆盖两个句子、V1含表格联动，也不因此拆成多条新问题。本轮新表达选项为S7与S8，均低优先，未发现需人为强化形容词的依据。

分审记录：build/ch4-final-41-42.md、build/ch4-final-43-44.md、build/ch4-final-45-46.md。按本轮材料完成逐小节核对，不保证绝无潜在遗漏；不以反复同义替换作为审查成效。
