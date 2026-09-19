# 表格、图题与图片文字回译审查

主审实际读取当前35个文件：22个表格、11个图题文件、1个共享排版宏和main.tex。所有源文和当前英文下列原样引用（仅统一换行）。原稿已有英文的部分不伪造中文源；提供助手中文回译供核对。数值本身不需要翻译，完整数值在原/英表中保留，回译集中于全部可见文字、指标、表头和脚注。

未进入当前主稿的文件：table_2_3、table_2_4、table_2_5、table_4_2、figure_4_1；仍作为目录内附属材料审查，不计入当前出版图表数量。正文当前引用18个表、10个图。

## 范文核实依据

主审核读了以下原TXT对应语义段，而非仅凭词库：BMSFormer full.txt 441–459（HI提取与CCCT），1344–1368（效率指标）；JESSOHRUL full.txt 1671–1679及1684–1696（相关性与峰/电压）；Engineering-AI full.txt 898–921（融合后大核细化）。TXT有双栏穿插，本处仅作词义及上下文核实，不据此报告新句数统计或PDF页序。

- BMSFormer full.txt:457–458：`constant current charge time`，助手释义：恒流充电时间。与本文表HI1对象相符，不继承其电压区间。
- BMSFormer full.txt:1367：`total number of trainable parameters`，助手释义：可训练参数总数。支持参数数量与存储大小分开，不等同推理延迟。
- JESSOHRUL full.txt:1677–1678：`linear correlation` / `monotonic relationship`，助手释义：线性相关/单调关系。与本文双相关解释相符，不借用具体阈值。
- Engineering-AI full.txt:900–901：`following the AFF feature fusion stage`，助手释义：位于AFF特征融合阶段之后。可借后置关系表达，AFF专名和物理解释不带入本文。

## 主审问题清单

|ID|位置|性质|具体发现与最小处理建议|
|---|---|---|---|
|T01|table_1_comparison表头|可选，需明确原意|“评估模型（是否为原创）”→“Estimation model (original design)”回译为“估计模型（原创设计）”。SOH语境下合理；若原意是“被评价的模型”，可写Model evaluated (original design)。不列确定错译。|
|T02|table_2_1 Oxford列|原表已有语言/协议问题|variance意为方差/差异，不是明确的动态放电协议。正文写源自ARTEMIS的动态电流，应核实后改为对应的dynamic discharge等；表中CC(2C)与正文CC-CV亦需作者核实。不能由英译自行选择真实协议。|
|T03|table_2_2 HI4/HI12|术语口径待定义核验|英文明确为full width at half maximum（半高全宽）；中文“半峰宽”本身未给计算边界。现有术语表已采用FWHM，未发现本轮不一致；不能仅凭中文简称改成half width，也不能宣称已核实实际计算公式。|
|T04|table_2_6 HI列|可选明确化|正文指HI1，表头只写HI；独立读表不够明确。建议HI1，属于源表既有标识问题。|
|T05|table_2_hi_screening_steps步骤5|原有英文流程歧义|“compare … with each HI …; if … remove; otherwise, add”没有明确otherwise是在全部比较结束后执行。可被理解为与某个已选HI不冗余就立即加入。若算法是遇任一冗余即剔除、所有比较均不冗余才加入，应明确any/already-selected与otherwise作用域；需按实际算法确认，不能将回译直接补写为确定事实。|
|T06|table_4_10 Average/Reduction|原表解释不足|Average对应综合平均误差；Reduction是完整模型相对该行的降幅，当前单词未标基准。建议表注明确计算式及精度来源。显示四位小数与Reduction列重算有微差不直接判数字错译。|
|T07|main.tex第3个节标题|可选准确化|“方法基础与数据准备”→Methodological framework and data preparation，framework回译为框架。章节包含框架概述，现译可解释；若严格保留“基础”，候选Methodological foundations and data preparation。|
|T08|figure_2_4图题|工作稿相对源稿的已有增加|当前英文比源图题增加(a)–(d)的Cell1/Cell2及PCC/SCC对应，图中也增加子图字母。信息与所示矩阵及正文相符，不是本轮审查所加；需与当前版本批准记录核对，不自动判成错误增译。|

## 逐文件原文、英文与回译

### tables/table_1_comparison.tex

源文件：source-zh/tables/table_1_comparison.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Comparison of existing SOH estimation methods.}
\label{tab:soh-method-comparison}
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}p{30pt}>{\centering\arraybackslash}p{26pt}>{\centering\arraybackslash}p{26pt}>{\centering\arraybackslash}p{26pt}p{130pt}p{128pt}>{\centering\arraybackslash}p{55pt}@{}}
\toprule
参考 & \multicolumn{3}{c}{考虑的源数据} & 健康指标选择方法（作者设计） & 评估模型（是否为原创） & 效率考量 \\
\cmidrule(lr){2-4}
 & 电流 & 电压 & 温度 & & & \\
\midrule
\cite{ref78} & \ding{51} & \ding{51} & \ding{55} & PCC（\ding{55}） & PINN（\ding{51}） & \ding{55} \\
\cite{ref31} & \ding{55} & \ding{51} & \ding{55} & PCC（\ding{51}） & BMSFormer（\ding{51}） & \ding{51} \\
\cite{ref32} & \ding{55} & \ding{51} & \ding{51} & PCC + SCC（\ding{55}） & BiGRU-Transformer（\ding{55}） & \ding{55} \\
\cite{ref37} & \ding{51} & \ding{51} & \ding{55} & PCC（\ding{55}） & Transformer（\ding{55}） & \ding{55} \\
\cite{ref79} & \ding{51} & \ding{51} & \ding{55} & LC（\ding{55}） & Gaussian filter（\ding{55}） & \ding{55} \\
\cite{ref27} & \ding{55} & \ding{51} & \ding{55} & LC（\ding{55}） & Random Forest Regression（\ding{55}） & \ding{55} \\
\cite{ref35} & \ding{51} & \ding{51} & \ding{51} & PCC（\ding{55}） & CNN-Transformer（\ding{55}） & \ding{51} \\
\cite{ref55} & \ding{51} & \ding{51} & \ding{51} & SA–PCA（\ding{51}） & CNN（\ding{55}） & \ding{51} \\
\cite{ref80} & \ding{55} & \ding{51} & \ding{55} & PCC（\ding{55}） & Bi-LSTM（\ding{55}） & \ding{55} \\
\cite{ref81} & \ding{55} & \ding{51} & \ding{55} & PCC + SCC（\ding{55}） & LSSVM-AdaBoost（\ding{55}） & \ding{55} \\
\cite{ref82} & \ding{55} & \ding{51} & \ding{55} & PCC（\ding{55}） & LSTM（\ding{55}） & \ding{55} \\
\cite{ref83} & \ding{51} & \ding{51} & \ding{51} & PCC（\ding{55}） & LSTM（\ding{55}） & \ding{55} \\
\cite{ref84} & \ding{51} & \ding{51} & \ding{51} & PCC + SCC（\ding{51}） & Extreme Learning Machine（\ding{55}） & \ding{55} \\
\cite{ref63} & \ding{55} & \ding{51} & \ding{55} & CCCT窗口搜索（\ding{51}） & Random Forest Regression（\ding{55}） & \ding{51} \\
\cite{ref48} & \ding{51} & \ding{51} & \ding{51} & 统计特征组合优化（\ding{51}） & NGO-Dualkernel-GPR（\ding{51}） & \ding{55} \\
\cite{ref51} & \ding{51} & \ding{51} & \ding{55} & QPSO区间优化（\ding{51}） & LSTM-BP（\ding{55}） & \ding{55} \\
本文 & \ding{51} & \ding{51} & \ding{51} & 多源健康指标提取与优化算法（\ding{51}） & MS-AgentNet（\ding{51}） & \ding{51} \\
\bottomrule
\end{tabular*}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Comparison of existing SOH estimation methods.}
\label{tab:soh-method-comparison}
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}>{\raggedright\arraybackslash}p{40pt}>{\centering\arraybackslash}p{31pt}>{\centering\arraybackslash}p{31pt}>{\centering\arraybackslash}p{48pt}>{\raggedright\arraybackslash}p{110pt}>{\raggedright\arraybackslash}p{111pt}>{\centering\arraybackslash}p{50pt}@{}}
\toprule
Reference & \multicolumn{3}{c}{Source data considered} & HI selection method (author-designed) & Estimation model (original design) & Efficiency considered \\
\cmidrule(lr){2-4}
 & Current & Voltage & Temperature & & & \\
\midrule
\cite{ref78} & \ding{51} & \ding{51} & \ding{55} & PCC (\ding{55}) & PINN (\ding{51}) & \ding{55} \\
\cite{ref31} & \ding{55} & \ding{51} & \ding{55} & PCC (\ding{51}) & BMSFormer (\ding{51}) & \ding{51} \\
\cite{ref32} & \ding{55} & \ding{51} & \ding{51} & PCC + SCC (\ding{55}) & BiGRU-Transformer (\ding{55}) & \ding{55} \\
\cite{ref37} & \ding{51} & \ding{51} & \ding{55} & PCC (\ding{55}) & Transformer (\ding{55}) & \ding{55} \\
\cite{ref79} & \ding{51} & \ding{51} & \ding{55} & LC (\ding{55}) & Gaussian filter (\ding{55}) & \ding{55} \\
\cite{ref27} & \ding{55} & \ding{51} & \ding{55} & LC (\ding{55}) & Random Forest Regression (\ding{55}) & \ding{55} \\
\cite{ref35} & \ding{51} & \ding{51} & \ding{51} & PCC (\ding{55}) & CNN-Transformer (\ding{55}) & \ding{51} \\
\cite{ref55} & \ding{51} & \ding{51} & \ding{51} & SA–PCA (\ding{51}) & CNN (\ding{55}) & \ding{51} \\
\cite{ref80} & \ding{55} & \ding{51} & \ding{55} & PCC (\ding{55}) & Bi-LSTM (\ding{55}) & \ding{55} \\
\cite{ref81} & \ding{55} & \ding{51} & \ding{55} & PCC + SCC (\ding{55}) & LSSVM-AdaBoost (\ding{55}) & \ding{55} \\
\cite{ref82} & \ding{55} & \ding{51} & \ding{55} & PCC (\ding{55}) & LSTM (\ding{55}) & \ding{55} \\
\cite{ref83} & \ding{51} & \ding{51} & \ding{51} & PCC (\ding{55}) & LSTM (\ding{55}) & \ding{55} \\
\cite{ref84} & \ding{51} & \ding{51} & \ding{51} & PCC + SCC (\ding{51}) & Extreme Learning Machine (\ding{55}) & \ding{55} \\
\cite{ref63} & \ding{55} & \ding{51} & \ding{55} & CCCT window search (\ding{51}) & Random Forest Regression (\ding{55}) & \ding{51} \\
\cite{ref48} & \ding{51} & \ding{51} & \ding{51} & Statistical feature combination optimization (\ding{51}) & NGO-Dualkernel-GPR (\ding{51}) & \ding{55} \\
\cite{ref51} & \ding{51} & \ding{51} & \ding{55} & QPSO interval optimization (\ding{51}) & LSTM-BP (\ding{55}) & \ding{55} \\
This study & \ding{51} & \ding{51} & \ding{51} & Multi-source health indicator extraction and optimization algorithm (\ding{51}) & MS-AgentNet (\ding{51}) & \ding{51} \\
\bottomrule
\end{tabular*}
\end{table}
```

中文回译（助手）：

表题：现有SOH估计方法比较。表头：参考文献；所考虑的源数据（电流、电压、温度）；HI筛选方法（作者设计）；估计模型（原创设计）；是否考虑效率。特有条目：CCCT窗口搜索；统计特征组合优化；QPSO区间优化；本研究；多源健康指标提取与优化算法。模型专名、引文及勾叉逐项保留。原中文“评估模型”在当前英文回译为“估计模型”，见T01。

五项核对：

①主体信息和各勾叉一致，“评估模型→Estimation model”是语义选择，见T01；②模型、引用不变，列宽数字不算实验数据；③表头可读，Statistical feature combination optimization略为名词密集但未损害含义；④无新增优势；⑤筛选名称是本文或所引研究专用名称，不冒称三篇共同术语。 图中文字的额外问题见图片审查附录。

### tables/table_2_1.tex

源文件：source-zh/tables/table_2_1.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Description of the four battery datasets.}
\label{tab:2-1}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.05}L{0.95}L{0.95}L{0.95}L{1.10}@{}}
\toprule
Data Sources & Oxford \cite{ref60} & CALCE CS2 \cite{ref18,ref61} & CALCE CX2 \cite{ref18,ref61} & MIT/Severson \cite{ref62} \\
\midrule
Manufacturer & Kokam & LG Chem & LG Chem & A123 Systems \\
\TableRowSpace
Cell types & Pouch & Prismatic & Prismatic & 18650 cylindrical \\
\TableRowSpace
Cathode material & NCO-LCO & LCO & LCO & LFP \\
\TableRowSpace
Rated capacity (Ah) & 0.74 & 1.10 & 1.35 & 1.10 \\
\TableRowSpace
Capacity failure\newline threshold & 70\% & 0.84 Ah (76.4\%) & 1.08 Ah (80\%) & 80\% \\
\TableRowSpace
Charge protocol\newline (rate) & CC (2C) & CC-CV\newline (0.5C, 4.2 V) & CC-CV\newline (0.5C, 4.2 V) & Two-step fast charge\newline + CC-CV (1C, 3.6 V) \\
\TableRowSpace
Discharge protocol\newline (rate) & variance & CC (1C) & CC (1C) & CC (4C) \\
\TableRowSpace
Cut-off voltage (V) & charge to 4.2\newline discharge to 2.7 & charge to 4.2\newline discharge to 2.7 & charge to 4.2\newline discharge to 2.7 & charge to 3.6\newline discharge to 2.0 \\
\TableRowSpace
Cut-off current (A) & --- & charge to 0.05 & charge to 0.05 & charge to 0.022\newline (C/50) \\
\TableRowSpace
Experiment\newline temperature ($^\circ$C) & 40 & 24 & 24 & 30 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Description of the four battery datasets.}
\label{tab:2-1}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.05}L{0.95}L{0.95}L{0.95}L{1.10}@{}}
\toprule
Data Sources & Oxford \cite{ref60} & CALCE CS2 \cite{ref18,ref61} & CALCE CX2 \cite{ref18,ref61} & MIT/Severson \cite{ref62} \\
\midrule
Manufacturer & Kokam & LG Chem & LG Chem & A123 Systems \\
\TableRowSpace
Cell types & Pouch & Prismatic & Prismatic & 18650 cylindrical \\
\TableRowSpace
Cathode material & NCO-LCO & LCO & LCO & LFP \\
\TableRowSpace
Rated capacity (Ah) & 0.74 & 1.10 & 1.35 & 1.10 \\
\TableRowSpace
Capacity failure\newline threshold & 70\% & 0.84 Ah (76.4\%) & 1.08 Ah (80\%) & 80\% \\
\TableRowSpace
Charge protocol\newline (rate) & CC (2C) & CC-CV\newline (0.5C, 4.2 V) & CC-CV\newline (0.5C, 4.2 V) & Two-step fast charge\newline + CC-CV (1C, 3.6 V) \\
\TableRowSpace
Discharge protocol\newline (rate) & variance & CC (1C) & CC (1C) & CC (4C) \\
\TableRowSpace
Cut-off voltage (V) & charge to 4.2\newline discharge to 2.7 & charge to 4.2\newline discharge to 2.7 & charge to 4.2\newline discharge to 2.7 & charge to 3.6\newline discharge to 2.0 \\
\TableRowSpace
Cut-off current (A) & --- & charge to 0.05 & charge to 0.05 & charge to 0.022\newline (C/50) \\
\TableRowSpace
Experiment\newline temperature ($^\circ$C) & 40 & 24 & 24 & 30 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：四个电池数据集的描述。表头/行头：数据来源；制造商；电芯类型；正极材料；额定容量(Ah)；容量失效阈值；充电协议（倍率）；放电协议（倍率）；截止电压(V)；截止电流(A)；实验温度(°C)。Pouch/Prismatic/18650 cylindrical分别为软包/方形/18650圆柱形；Two-step fast charge + CC-CV为两步快充加恒流恒压；charge/discharge to为充/放电至。Oxford放电单元的variance字面为“方差/差异”，无法准确回译为明确放电协议；见T02。所有数值和材料缩写与源表相同。

五项核对：

①源表原为英文，无本轮中译英漏增；②Oxford协议存在源稿表文差异；③variance不能清楚表达放电协议；④无新主张；⑤数据协议必须依数据来源确认，不能用范文替代。见T02。 图中文字的额外问题见图片审查附录。

### tables/table_2_2.tex

源文件：source-zh/tables/table_2_2.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Definitions of the candidate HIs.}
\label{tab:2-2}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}C{0.30}L{0.65}L{2.05}@{}}
\toprule
No. & Category & Health indicator \\
\midrule
HI1 & CVT & MS-CCCT 标定电压区间内的恒流充电时间 \\
HI2 & IC & 增量容量曲线的峰值 \\
HI3 & IC & 增量容量峰值对应的电压 \\
HI4 & IC & 增量容量特征峰的半峰宽 \\
HI5 & DTV & 微分温度--电压曲线的峰值 \\
HI6 & DTV & 微分温度--电压曲线峰值对应的电压 \\
HI7 & DTV & 微分温度--电压曲线的谷值 \\
HI8 & DTV & 微分温度--电压曲线谷值对应的电压 \\
HI9 & DTV & 微分温度--电压曲线的峰谷差 \\
HI10 & DTC & 微分温度--容量曲线的峰值 \\
HI11 & DTC & 微分温度--容量曲线峰值对应的容量 \\
HI12 & DTC & 微分温度--容量特征峰的半峰宽 \\
HI13 & 窗口放电容量 & 电压范围 3.80--3.40 V 内的放电容量 \\
HI14 & 窗口放电容量 & 电压范围 3.20--3.00 V 内的放电容量 \\
HI15 & 能量效率 & 单次循环放电能量与充电能量之比 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Definitions of the candidate HIs.}
\label{tab:2-2}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}C{0.30}L{0.65}L{2.05}@{}}
\toprule
No. & Category & Health indicator \\
\midrule
HI1 & CVT & Constant current charge time within the voltage interval calibrated by MS-CCCT \\
HI2 & IC & Peak value of the IC curve \\
HI3 & IC & Voltage corresponding to the IC peak \\
HI4 & IC & Full width at half maximum of the IC peak \\
HI5 & DTV & Peak value of the DTV curve \\
HI6 & DTV & Voltage corresponding to the DTV peak \\
HI7 & DTV & Valley value of the DTV curve \\
HI8 & DTV & Voltage corresponding to the DTV valley \\
HI9 & DTV & Peak-to-valley difference of the DTV curve \\
HI10 & DTC & Peak value of the DTC curve \\
HI11 & DTC & Capacity corresponding to the DTC peak \\
HI12 & DTC & Full width at half maximum of the DTC peak \\
HI13 & Discharge capacity within a voltage window & Discharge capacity within 3.80--3.40 V \\
HI14 & Discharge capacity within a voltage window & Discharge capacity within 3.20--3.00 V \\
HI15 & Energy efficiency & Ratio of discharge energy to charge energy in a single cycle \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：候选健康指标的定义。表头：编号；类别；健康指标。

|指标|按当前英文回译|
|---|---|
|HI1|MS-CCCT标定的电压区间内的恒流充电时间|
|HI2|IC曲线峰值|
|HI3|IC峰对应的电压|
|HI4|IC峰的半高全宽|
|HI5|DTV曲线峰值|
|HI6|DTV峰对应的电压|
|HI7|DTV曲线谷值|
|HI8|DTV谷对应的电压|
|HI9|DTV曲线的峰谷差|
|HI10|DTC曲线峰值|
|HI11|DTC峰对应的容量|
|HI12|DTC峰的半高全宽|
|HI13|电压窗口内的放电容量：3.80–3.40 V内的放电容量|
|HI14|电压窗口内的放电容量：3.20–3.00 V内的放电容量|
|HI15|能量效率：单次循环放电能量与充电能量之比|

IC、DTV、DTC按正文定义理解；峰值与峰位未混淆，分子分母未颠倒。FWHM明确表示全宽，见T03术语条件说明。

五项核对：

①15项顺序与对象一致；②HI编号、窗口端点、分母准确；FWHM采用现有术语表但实际宽度口径待原计算定义核实，见T03；③各短语自然；④无夸大；⑤CCCT在BMS原文可核，IC/DTV/DTC细项为按定义适配。 图中文字的额外问题见图片审查附录。

### tables/table_2_3.tex

源文件：source-zh/tables/table_2_3.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{MS-CCCT window calibration results on four datasets.}
\label{tab:4-hi-window-calibration}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.05}C{1.35}C{1.35}C{0.70}C{0.70}C{0.70}@{}}
\toprule
Dataset & Initial range (V) & MS-CCCT window (V) & $mPCC$ & $mSCC$ & $S_i$ \\
\midrule
Oxford & 3.50--4.20 & 3.55--3.75 & 0.997322 & 0.994447 & 0.994447 \\
CS2 & 3.50--4.20 & 3.80--4.00 & 0.990286 & 0.980124 & 0.980124 \\
CX2 & 3.50--4.20 & 3.85--4.05 & 0.985921 & 0.990832 & 0.985921 \\
MIT/Severson & 2.120--3.550 & 2.970--3.170 & 0.995272 & 0.994419 & 0.994419 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{MS-CCCT window calibration results on four datasets.}
\label{tab:4-hi-window-calibration}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.05}C{1.35}C{1.35}C{0.70}C{0.70}C{0.70}@{}}
\toprule
Dataset & Initial range (V) & MS-CCCT window (V) & $mPCC$ & $mSCC$ & $S_i$ \\
\midrule
Oxford & 3.50--4.20 & 3.55--3.75 & 0.997322 & 0.994447 & 0.994447 \\
CS2 & 3.50--4.20 & 3.80--4.00 & 0.990286 & 0.980124 & 0.980124 \\
CX2 & 3.50--4.20 & 3.85--4.05 & 0.985921 & 0.990832 & 0.985921 \\
MIT/Severson & 2.120--3.550 & 2.970--3.170 & 0.995272 & 0.994419 & 0.994419 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：四个数据集上的MS-CCCT窗口标定结果。表头：数据集、初始范围(V)、MS-CCCT窗口(V)、mPCC、mSCC、S_i。四组窗口和得分原样保留；英文未加入跨数据集使用统一窗口的说法。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_2_4.tex

源文件：source-zh/tables/table_2_4.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Selected HIs and their correlations on four datasets.}
\label{tab:4-hi-selected}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.10}C{0.80}L{1.50}C{0.80}C{0.80}@{}}
\toprule
Dataset & Selected HI & \mbox{Feature-development cell} & $\lvert\gamma\rvert$ & $\lvert\rho\rvert$ \\
\midrule
Oxford & HI1 & Cell1 & 0.998759 & 0.998710 \\
       &     & Cell2 & 0.997322 & 0.994447 \\
\TableGroupSpace
CS2    & HI1 & CS2\_36 & 0.990838 & 0.986319 \\
       &     & CS2\_37 & 0.990286 & 0.980124 \\
       & HI2 & CS2\_36 & 0.940029 & 0.989905 \\
       &     & CS2\_37 & 0.938326 & 0.988319 \\
\TableGroupSpace
CX2    & HI13 & CX2\_36 & 0.999080 & 0.998532 \\
       &      & CX2\_37 & 0.997987 & 0.996442 \\
\TableGroupSpace
MIT/Severson & HI14 & b3c8  & 0.972972 & 0.995614 \\
             &      & b3c13 & 0.970917 & 0.997651 \\
             & HI15 & b3c8  & 0.979188 & 0.988926 \\
             &      & b3c13 & 0.994096 & 0.995717 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Selected HIs and their correlations on four datasets.}
\label{tab:4-hi-selected}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.10}C{0.80}L{1.50}C{0.80}C{0.80}@{}}
\toprule
Dataset & Selected HI & \mbox{Feature-development cell} & $\lvert\gamma\rvert$ & $\lvert\rho\rvert$ \\
\midrule
Oxford & HI1 & Cell1 & 0.998759 & 0.998710 \\
       &     & Cell2 & 0.997322 & 0.994447 \\
\TableGroupSpace
CS2    & HI1 & CS2\_36 & 0.990838 & 0.986319 \\
       &     & CS2\_37 & 0.990286 & 0.980124 \\
       & HI2 & CS2\_36 & 0.940029 & 0.989905 \\
       &     & CS2\_37 & 0.938326 & 0.988319 \\
\TableGroupSpace
CX2    & HI13 & CX2\_36 & 0.999080 & 0.998532 \\
       &      & CX2\_37 & 0.997987 & 0.996442 \\
\TableGroupSpace
MIT/Severson & HI14 & b3c8  & 0.972972 & 0.995614 \\
             &      & b3c13 & 0.970917 & 0.997651 \\
             & HI15 & b3c8  & 0.979188 & 0.988926 \\
             &      & b3c13 & 0.994096 & 0.995717 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：四个数据集的入选HI及其相关性。表头：数据集、入选HI、特征开发电池、|γ|、|ρ|。每组特征开发电池、HI和两种绝对相关系数保留，不将特征开发电池译成独立测试电池。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_2_5.tex

源文件：source-zh/tables/table_2_5.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Correlations of selected HIs on other cells.}
\label{tab:4-hi-correlation}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.20}C{1.00}C{0.90}C{1.00}C{1.00}@{}}
\toprule
Dataset & Cell & Selected HI & $\lvert\gamma\rvert$ & $\lvert\rho\rvert$ \\
\midrule
Oxford & Cell3 & HI1 & 0.999052 & 0.999672 \\
        & Cell4 & HI1 & 0.998933 & 0.999884 \\
        & Cell5 & HI1 & 0.997874 & 1.000000 \\
        & Cell6 & HI1 & 0.998257 & 0.999877 \\
        & Cell7 & HI1 & 0.999337 & 0.999606 \\
        & Cell8 & HI1 & 0.999259 & 0.999699 \\
\TableGroupSpace
CS2 & CS2\_38 & HI1 & 0.986076 & 0.974359 \\
    & CS2\_38 & HI2 & 0.932937 & 0.986793 \\
\TableGroupSpace
CX2 & CX2\_38 & HI13 & 0.999576 & 0.999062 \\
\TableGroupSpace
MIT/Severson & b3c29 & HI14 & 0.973516 & 0.996569 \\
              & b3c29 & HI15 & 0.990303 & 0.992179 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Correlations of selected HIs on other cells.}
\label{tab:4-hi-correlation}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.20}C{1.00}C{0.90}C{1.00}C{1.00}@{}}
\toprule
Dataset & Cell & Selected HI & $\lvert\gamma\rvert$ & $\lvert\rho\rvert$ \\
\midrule
Oxford & Cell3 & HI1 & 0.999052 & 0.999672 \\
        & Cell4 & HI1 & 0.998933 & 0.999884 \\
        & Cell5 & HI1 & 0.997874 & 1.000000 \\
        & Cell6 & HI1 & 0.998257 & 0.999877 \\
        & Cell7 & HI1 & 0.999337 & 0.999606 \\
        & Cell8 & HI1 & 0.999259 & 0.999699 \\
\TableGroupSpace
CS2 & CS2\_38 & HI1 & 0.986076 & 0.974359 \\
    & CS2\_38 & HI2 & 0.932937 & 0.986793 \\
\TableGroupSpace
CX2 & CX2\_38 & HI13 & 0.999576 & 0.999062 \\
\TableGroupSpace
MIT/Severson & b3c29 & HI14 & 0.973516 & 0.996569 \\
              & b3c29 & HI15 & 0.990303 & 0.992179 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：入选HI在其他电池上的相关性。表头：数据集、电池、入选HI、|γ|、|ρ|。Oxford Cell3–Cell8、CS2_38、CX2_38、b3c29的各行值原样保留。“其他”不自动意味着新数据集。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_2_6.tex

源文件：source-zh/tables/table_2_6.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption[Absolute PCC comparison of different HIs on the Oxford dataset]{Absolute PCC comparison of different HIs on the Oxford dataset.}
\label{tab:2-hi-literature}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.65}C{0.95}C{1.20}C{0.80}C{0.80}C{1.40}C{1.20}@{}}
\toprule
Cell & HI & \makecell[c]{Sample entropy\\\cite{ref67}} & \makecell[c]{$PP_{\mathrm{DTV}}$\\\cite{ref68}} & \makecell[c]{$P_{\mathrm{IC}}$\\\cite{ref68}} & \makecell[c]{DTV peak position\\$FV_6$\cite{ref69}} & \makecell[c]{Voltage slope\\\cite{ref70}} \\
\midrule
Cell3 & \textbf{0.999052} & 0.9876 & 0.9393 & 0.9729 & 0.964 & 0.9980 \\
Cell4 & \textbf{0.998933} & 0.9885 & 0.9102 & 0.9817 & 0.972 & — \\
Cell5 & \textbf{0.997874} & 0.9133 & 0.9574 & 0.9034 & — & — \\
Cell6 & \textbf{0.998257} & 0.9848 & 0.9299 & 0.9788 & — & — \\
Cell7 & \textbf{0.999337} & 0.9896 & 0.9676 & 0.9748 & 0.983 & 0.9982 \\
Cell8 & \textbf{0.999259} & 0.9908 & 0.9654 & 0.9713 & 0.981 & 0.9979 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption[Absolute PCC comparison of different HIs on the Oxford dataset]{Absolute PCC comparison of different HIs on the Oxford dataset.}
\label{tab:2-hi-literature}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.65}C{0.95}C{1.20}C{0.80}C{0.80}C{1.40}C{1.20}@{}}
\toprule
Cell & HI & \makecell[c]{Sample entropy\\\cite{ref67}} & \makecell[c]{$PP_{\mathrm{DTV}}$\\\cite{ref68}} & \makecell[c]{$P_{\mathrm{IC}}$\\\cite{ref68}} & \makecell[c]{DTV peak position\\$FV_6$\cite{ref69}} & \makecell[c]{Voltage slope\\\cite{ref70}} \\
\midrule
Cell3 & \textbf{0.999052} & 0.9876 & 0.9393 & 0.9729 & 0.964 & 0.9980 \\
Cell4 & \textbf{0.998933} & 0.9885 & 0.9102 & 0.9817 & 0.972 & — \\
Cell5 & \textbf{0.997874} & 0.9133 & 0.9574 & 0.9034 & — & — \\
Cell6 & \textbf{0.998257} & 0.9848 & 0.9299 & 0.9788 & — & — \\
Cell7 & \textbf{0.999337} & 0.9896 & 0.9676 & 0.9748 & 0.983 & 0.9982 \\
Cell8 & \textbf{0.999259} & 0.9908 & 0.9654 & 0.9713 & 0.981 & 0.9979 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：Oxford数据集中不同HI的绝对PCC比较。表头：电池、HI、样本熵、PP_DTV、P_IC、DTV峰位置FV_6、电压斜率。空缺符号不译成零。表头HI未明确写HI1，正文可补足指代，见T04。

五项核对：

①源表既有英文保留；②数值与引文相同，缺项仍为缺项；③HI列可更明确，见T04；④比较范围未扩大；⑤sample entropy等为引文研究名称，保留。 图中文字的额外问题见图片审查附录。

### tables/table_2_hi_screening_steps.tex

源文件：source-zh/tables/table_2_hi_screening_steps.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}[!htb]
\TableStyle
\caption{Group-level health indicator screening steps.}
\label{tab:2-hi-screening-steps}
\begin{tabularx}{\linewidth}{@{}X@{}}
\toprule
\textbf{Procedure: Group-level health indicator screening} \\
\midrule
1. Calculate the PCC and SCC of each candidate HI on the cells in the feature-development set $\mathcal{B}$. \\
2. Obtain $mPCC_i=\min_{j\in\mathcal{B}}|\gamma_{i,j}|$ and $mSCC_i=\min_{j\in\mathcal{B}}|\rho_{i,j}|$ for each candidate HI $f_i$. \\
3. Retain the HIs satisfying $mPCC_i\geq\theta_{\mathrm{lin}}$ and $mSCC_i\geq\theta_{\mathrm{mono}}$, where $\theta_{\mathrm{lin}}=0.92$ and $\theta_{\mathrm{mono}}=0.96$, and sort them in descending order according to $R_i=\max(mPCC_i,mSCC_i)$. \\
4. Initialize the selected HI set $\mathcal{S}=\varnothing$. \\
5. For each retained candidate HI $f_i$: \\
\hspace*{1em}compare $f_i$ with each HI already contained in $\mathcal{S}$; \\
\hspace*{1em}if their group-average absolute PCC and SCC both reach $\theta_{\mathrm{co}}=0.95$, remove $f_i$; \\
\hspace*{1em}otherwise, add $f_i$ to $\mathcal{S}$. \\
6. Output the final selected HI set $\mathcal{S}$. \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}[!htb]
\TableStyle
\caption{Group-level health indicator screening steps.}
\label{tab:2-hi-screening-steps}
\begin{tabularx}{\linewidth}{@{}X@{}}
\toprule
\textbf{Procedure: Group-level health indicator screening} \\
\midrule
1. Calculate the PCC and SCC of each candidate HI on the cells in the feature-development set $\mathcal{B}$. \\
2. Obtain $mPCC_i=\min_{j\in\mathcal{B}}|\gamma_{i,j}|$ and $mSCC_i=\min_{j\in\mathcal{B}}|\rho_{i,j}|$ for each candidate HI $f_i$. \\
3. Retain the HIs satisfying $mPCC_i\geq\theta_{\mathrm{lin}}$ and $mSCC_i\geq\theta_{\mathrm{mono}}$, where $\theta_{\mathrm{lin}}=0.92$ and $\theta_{\mathrm{mono}}=0.96$, and sort them in descending order according to $R_i=\max(mPCC_i,mSCC_i)$. \\
4. Initialize the selected HI set $\mathcal{S}=\varnothing$. \\
5. For each retained candidate HI $f_i$: \\
\hspace*{1em}compare $f_i$ with each HI already contained in $\mathcal{S}$; \\
\hspace*{1em}if their group-average absolute PCC and SCC both reach $\theta_{\mathrm{co}}=0.95$, remove $f_i$; \\
\hspace*{1em}otherwise, add $f_i$ to $\mathcal{S}$. \\
6. Output the final selected HI set $\mathcal{S}$. \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：组级健康指标筛选步骤。程序：组级健康指标筛选。

1. 计算特征开发集合B中各电池上每个候选HI的PCC和SCC。
2. 对每个候选HI f_i，得到mPCC_i=min_j|γ_i,j|及mSCC_i=min_j|ρ_i,j|。
3. 保留同时满足mPCC_i≥θ_lin和mSCC_i≥θ_mono的HI，其中θ_lin=0.92，θ_mono=0.96，并按R_i=max(mPCC_i,mSCC_i)降序排列。
4. 初始化入选HI集合S为空集。
5. 对每个保留的候选HI f_i：将其与S中已有的每个HI比较；如果它们的组平均绝对PCC和SCC都达到θ_co=0.95，移除f_i；否则，将f_i加入S。
6. 输出最终入选HI集合S。

注意第5步的each/if/otherwise作用域，见T05；不能在回译中擅自加上英文没有明确写出的“任一/所有”控制逻辑。

五项核对：

①英文源与当前一致；②阈值0.92/0.96/0.95、min/max及and保留；③步骤5的otherwise存在控制流作用域歧义，见T05；④无新增主张；⑤JES支持PCC/SCC与冗余筛选表达，但本表流程须由本文自定，不能按范文暗改。 图中文字的额外问题见图片审查附录。

### tables/table_4_1.tex

源文件：source-zh/tables/table_4_1.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Hyperparameter configuration range of MS-AgentNet.}
\label{tab:4-1}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}L{1.10}@{}}
\toprule
超参数 & 配置范围 \\
\midrule
学习率 & 0.001, 0.01 \\
网络深度 $L$ & 1, 2, 4, 8 \\
嵌入维度 $d$ & 16, 32, 64, 128 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Hyperparameter configuration range of MS-AgentNet.}
\label{tab:4-1}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}L{1.10}@{}}
\toprule
Hyperparameter & Configuration range \\
\midrule
Learning rate & 0.001, 0.01 \\
Network depth $L$ & 1, 2, 4, 8 \\
Embedding dimension $d$ & 16, 32, 64, 128 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：MS-AgentNet的超参数配置范围。表头：超参数、配置范围。学习率：0.001、0.01；网络深度L：1、2、4、8；嵌入维度d：16、32、64、128。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_10.tex

源文件：source-zh/tables/table_4_10.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Ablation results on different datasets.}
\label{tab:4-10}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.80}C{1.00}C{1.00}C{1.18}C{0.60}C{1.04}C{1.04}C{1.04}C{1.10}C{1.20}@{}}
\toprule
Dataset & Model & Backbone & \makecell[c]{Multi-scale\\DSConv} & RAA & MAE & RMSE & MAPE & Average & Reduction \\
\midrule
CS2    & M1                           & \ding{51} & ---        & ---        & 0.0123 & 0.0183 & 0.0166 & 0.0157 & 3.74\%  \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0130 & 0.0184 & 0.0171 & 0.0162 & 6.49\%  \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0119 & 0.0178 & 0.0161 & 0.0152 & 0.62\%  \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0120 & 0.0174 & 0.0160 & \textbf{0.0151} & ---     \\
\TableGroupSpace
CX2    & M1                           & \ding{51} & ---        & ---        & 0.0170 & 0.0294 & 0.1035 & 0.0500 & 54.94\% \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0164 & 0.0284 & 0.1033 & 0.0494 & 54.40\% \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0156 & 0.0270 & 0.0899 & 0.0442 & 49.05\% \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0106 & 0.0193 & 0.0377 & \textbf{0.0225} & ---     \\
\TableGroupSpace
MIT    & M1                           & \ding{51} & ---        & ---        & 0.0019 & 0.0022 & 0.0020 & \textbf{0.0020} & 2.43\%  \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0021 & 0.0025 & 0.0023 & 0.0023 & 14.16\% \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0024 & 0.0028 & 0.0026 & 0.0026 & 23.91\% \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0018 & 0.0022 & 0.0020 & \textbf{0.0020} & ---     \\
\TableGroupSpace
Oxford & M1                           & \ding{51} & ---        & ---        & 0.0063 & 0.0076 & 0.0073 & 0.0071 & 16.52\% \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0058 & 0.0070 & 0.0067 & 0.0065 & 9.50\%  \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0054 & 0.0063 & 0.0062 & 0.0060 & 1.52\%  \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0053 & 0.0062 & 0.0062 & \textbf{0.0059} & ---     \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Ablation results on different datasets.}
\label{tab:4-10}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.80}C{1.00}C{1.00}C{1.18}C{0.60}C{1.04}C{1.04}C{1.04}C{1.10}C{1.20}@{}}
\toprule
Dataset & Model & Backbone & \makecell[c]{Multi-scale\\DSConv} & RAA & MAE & RMSE & MAPE & Average & Reduction \\
\midrule
CS2    & M1                           & \ding{51} & ---        & ---        & 0.0123 & 0.0183 & 0.0166 & 0.0157 & 3.74\%  \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0130 & 0.0184 & 0.0171 & 0.0162 & 6.49\%  \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0119 & 0.0178 & 0.0161 & 0.0152 & 0.62\%  \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0120 & 0.0174 & 0.0160 & \textbf{0.0151} & ---     \\
\TableGroupSpace
CX2    & M1                           & \ding{51} & ---        & ---        & 0.0170 & 0.0294 & 0.1035 & 0.0500 & 54.94\% \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0164 & 0.0284 & 0.1033 & 0.0494 & 54.40\% \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0156 & 0.0270 & 0.0899 & 0.0442 & 49.05\% \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0106 & 0.0193 & 0.0377 & \textbf{0.0225} & ---     \\
\TableGroupSpace
MIT    & M1                           & \ding{51} & ---        & ---        & 0.0019 & 0.0022 & 0.0020 & \textbf{0.0020} & 2.43\%  \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0021 & 0.0025 & 0.0023 & 0.0023 & 14.16\% \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0024 & 0.0028 & 0.0026 & 0.0026 & 23.91\% \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0018 & 0.0022 & 0.0020 & \textbf{0.0020} & ---     \\
\TableGroupSpace
Oxford & M1                           & \ding{51} & ---        & ---        & 0.0063 & 0.0076 & 0.0073 & 0.0071 & 16.52\% \\
       & M2                           & \ding{51} & \ding{51}  & ---        & 0.0058 & 0.0070 & 0.0067 & 0.0065 & 9.50\%  \\
       & M3                           & \ding{51} & ---        & \ding{51}  & 0.0054 & 0.0063 & 0.0062 & 0.0060 & 1.52\%  \\
       & \makecell[c]{M4\\(Proposed)} & \ding{51} & \ding{51}  & \ding{51}  & 0.0053 & 0.0062 & 0.0062 & \textbf{0.0059} & ---     \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：不同数据集上的消融结果。表头：数据集、模型、骨干网络、多尺度DSConv、RAA、MAE、RMSE、MAPE、平均值、降低幅度。Proposed为本文所提模型。数值及模块勾叉未改变。Average和Reduction含义在表内不够完整，见T06；不能回译时自行补成所有模型通用绝对优势。

五项核对：

①源表英文原样；②四组M1–M4数据保留，Reduction的计算基准需读正文，见T06；③Average/Reduction标题可更明确；④无自动将非最优数值改粗体；⑤消融表达功能匹配，具体降幅不是范文借来的证据。 图中文字的额外问题见图片审查附录。

### tables/table_4_11.tex

源文件：source-zh/tables/table_4_11.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Effects of different convolution scales.}
\label{tab:4-11}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}C{0.90}C{0.75}C{0.75}C{0.60}C{1.275}C{1.275}C{1.275}C{1.275}@{}}
\toprule
Dataset & Model & $K=5$ & $K=31$ & RAA & MAE & RMSE & MAPE & Average \\
\midrule
CS2    & S0    & ---       & ---       & \ding{51} & 0.0119 & 0.0178 & 0.0161 & 0.0152 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0128 & 0.0184 & 0.0170 & 0.0161 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0124 & 0.0179 & 0.0166 & 0.0156 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0120 & 0.0174 & 0.0160 & 0.0151 \\
\TableGroupSpace
CX2    & S0    & ---       & ---       & \ding{51} & 0.0156 & 0.0270 & 0.0899 & 0.0442 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0162 & 0.0285 & 0.1036 & 0.0494 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0135 & 0.0232 & 0.0677 & 0.0348 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0106 & 0.0193 & 0.0377 & 0.0225 \\
\TableGroupSpace
MIT    & S0    & ---       & ---       & \ding{51} & 0.0024 & 0.0028 & 0.0026 & 0.0026 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0023 & 0.0027 & 0.0025 & 0.0025 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0025 & 0.0028 & 0.0026 & 0.0026 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0018 & 0.0022 & 0.0020 & 0.0020 \\
\TableGroupSpace
Oxford & S0    & ---       & ---       & \ding{51} & 0.0054 & 0.0063 & 0.0062 & 0.0060 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0056 & 0.0066 & 0.0065 & 0.0062 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0055 & 0.0065 & 0.0064 & 0.0061 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0053 & 0.0062 & 0.0062 & 0.0059 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Effects of different convolution scales.}
\label{tab:4-11}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}C{0.90}C{0.75}C{0.75}C{0.60}C{1.275}C{1.275}C{1.275}C{1.275}@{}}
\toprule
Dataset & Model & $K=5$ & $K=31$ & RAA & MAE & RMSE & MAPE & Average \\
\midrule
CS2    & S0    & ---       & ---       & \ding{51} & 0.0119 & 0.0178 & 0.0161 & 0.0152 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0128 & 0.0184 & 0.0170 & 0.0161 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0124 & 0.0179 & 0.0166 & 0.0156 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0120 & 0.0174 & 0.0160 & 0.0151 \\
\TableGroupSpace
CX2    & S0    & ---       & ---       & \ding{51} & 0.0156 & 0.0270 & 0.0899 & 0.0442 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0162 & 0.0285 & 0.1036 & 0.0494 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0135 & 0.0232 & 0.0677 & 0.0348 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0106 & 0.0193 & 0.0377 & 0.0225 \\
\TableGroupSpace
MIT    & S0    & ---       & ---       & \ding{51} & 0.0024 & 0.0028 & 0.0026 & 0.0026 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0023 & 0.0027 & 0.0025 & 0.0025 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0025 & 0.0028 & 0.0026 & 0.0026 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0018 & 0.0022 & 0.0020 & 0.0020 \\
\TableGroupSpace
Oxford & S0    & ---       & ---       & \ding{51} & 0.0054 & 0.0063 & 0.0062 & 0.0060 \\
       & S5    & \ding{51} & ---       & \ding{51} & 0.0056 & 0.0066 & 0.0065 & 0.0062 \\
       & S31   & ---       & \ding{51} & \ding{51} & 0.0055 & 0.0065 & 0.0064 & 0.0061 \\
       & SFull & \ding{51} & \ding{51} & \ding{51} & 0.0053 & 0.0062 & 0.0062 & 0.0059 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：不同卷积尺度的影响。表头：数据集、模型、K=5、K=31、RAA、MAE、RMSE、MAPE、平均值。S0/S5/S31/SFull分别保持原标识和模块勾叉。Average对应正文综合平均误差，是否需要在表中解释属于原表自明性事项。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_12.tex

源文件：source-zh/tables/table_4_12.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Comprehensive performance of models under the same configuration.}
\label{tab:4-12}
\setlength{\tabcolsep}{2pt}
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}p{70pt}>{\centering\arraybackslash}p{28pt}>{\centering\arraybackslash}p{28pt}>{\centering\arraybackslash}p{28pt}>{\centering\arraybackslash}p{25pt}>{\centering\arraybackslash}p{25pt}>{\centering\arraybackslash}p{25pt}>{\centering\arraybackslash}p{42pt}>{\centering\arraybackslash}p{62pt}>{\centering\arraybackslash}p{43pt}>{\centering\arraybackslash}p{50pt}@{}}
\toprule
Models & \multicolumn{3}{c}{Training hyperparameters} & \multicolumn{3}{c}{Model hyperparameters} & \multicolumn{4}{c}{Performance indicators} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-11}
 & $e$ & $lr$ & $b$ & $d_e$ & $d_d$ & $n$ & FLOPs (M) & Training time (s) & Parameters & Storage (KB) \\
\midrule
MS-AgentNet & 1000 & 0.01 & 128 & 16 & 16 & 4 & \textbf{0.045760} & 123.338 & \textbf{4643} & \textbf{27.44} \\
Transformer & 1000 & 0.01 & 128 & 16 & 16 & 4 & 0.049760 & 80.638 & 4673 & 29.60 \\
CNN-Transformer & 1000 & 0.01 & 128 & 16 & 16 & 4 & 0.053024 & 90.195 & 6241 & 36.97 \\
CNN-LSTM & 1000 & 0.01 & 128 & -- & 16 & 4 & 0.067520 & 48.828 & 15912 & 68.33 \\
LSTM & 1000 & 0.01 & 128 & -- & 16 & 4 & 0.092512 & \textbf{44.568} & 8769 & 39.90 \\
\bottomrule
\end{tabular*}
\TableNote{注：$e$、$lr$、$b$和$d_e$分别表示训练轮次、学习率、批次大小和嵌入维度；$d_d$表示多层感知机的隐藏层维度或LSTM的隐藏状态维度；$n$表示注意力模型的注意力头数或基于LSTM模型的LSTM层数。最佳结果以粗体标出。}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Comprehensive performance of models under the same configuration.}
\label{tab:4-12}
\setlength{\tabcolsep}{2pt}
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}p{70pt}>{\centering\arraybackslash}p{28pt}>{\centering\arraybackslash}p{28pt}>{\centering\arraybackslash}p{28pt}>{\centering\arraybackslash}p{25pt}>{\centering\arraybackslash}p{25pt}>{\centering\arraybackslash}p{25pt}>{\centering\arraybackslash}p{42pt}>{\centering\arraybackslash}p{62pt}>{\centering\arraybackslash}p{43pt}>{\centering\arraybackslash}p{50pt}@{}}
\toprule
Models & \multicolumn{3}{c}{Training hyperparameters} & \multicolumn{3}{c}{Model hyperparameters} & \multicolumn{4}{c}{Performance indicators} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-11}
 & $e$ & $lr$ & $b$ & $d_e$ & $d_d$ & $n$ & FLOPs (M) & Training time (s) & Parameters & Storage (KB) \\
\midrule
MS-AgentNet & 1000 & 0.01 & 128 & 16 & 16 & 4 & \textbf{0.045760} & 123.338 & \textbf{4643} & \textbf{27.44} \\
Transformer & 1000 & 0.01 & 128 & 16 & 16 & 4 & 0.049760 & 80.638 & 4673 & 29.60 \\
CNN-Transformer & 1000 & 0.01 & 128 & 16 & 16 & 4 & 0.053024 & 90.195 & 6241 & 36.97 \\
CNN-LSTM & 1000 & 0.01 & 128 & -- & 16 & 4 & 0.067520 & 48.828 & 15912 & 68.33 \\
LSTM & 1000 & 0.01 & 128 & -- & 16 & 4 & 0.092512 & \textbf{44.568} & 8769 & 39.90 \\
\bottomrule
\end{tabular*}
\TableNote{Note: $e$, $lr$, $b$, and $d_e$ denote the number of training epochs, learning rate, batch size, and embedding dimension, respectively; $d_d$ denotes the MLP hidden-layer dimension or the LSTM hidden-state dimension; $n$ denotes the number of attention heads in attention-based models or the number of LSTM layers in LSTM-based models. The best results are shown in bold.}
\end{table}
```

中文回译（助手）：

表题：相同配置下各模型的综合性能。表头：模型、训练超参数、模型超参数、性能指标；e、lr、b、d_e、d_d、n；FLOPs(M)、训练时间(s)、参数量、存储(KB)。脚注：e、lr、b和d_e分别表示训练轮次、学习率、批次大小和嵌入维度；d_d表示MLP隐藏层维度或LSTM隐藏状态维度；n表示注意力模型的注意力头数或LSTM模型的LSTM层数。最佳结果用粗体标出。参数和训练时长未混淆，各模型并非所有结构相同，same configuration应在正文给定统一测试口径下理解。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_2.tex

源文件：source-zh/tables/table_4_2.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Final configurations of MS-AgentNet.}
\label{tab:4-2}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.25}C{0.85}C{0.95}C{1.10}C{0.85}@{}}
\toprule
数据集 & 网络深度 $L$ & 嵌入维度 $d$ & 全连接层维度 & 学习率 \\
\midrule
CALCE CS2 & 1 & 16 & 32 & 0.001 \\
CALCE CX2 & 1 & 16 & 16 & 0.001 \\
MIT/Severson & 1 & 16 & 16 & 0.001 \\
Oxford & 1 & 16 & 64 & 0.001 \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Final configurations of MS-AgentNet.}
\label{tab:4-2}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.25}C{0.85}C{0.95}C{1.10}C{0.85}@{}}
\toprule
Dataset & Network depth $L$ & Embedding dimension $d$ & Fully connected layer dimension & Learning rate \\
\midrule
CALCE CS2 & 1 & 16 & 32 & 0.001 \\
CALCE CX2 & 1 & 16 & 16 & 0.001 \\
MIT/Severson & 1 & 16 & 16 & 0.001 \\
Oxford & 1 & 16 & 64 & 0.001 \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：MS-AgentNet的最终配置。表头：数据集、网络深度L、嵌入维度d、全连接层维度、学习率。四组网络深度均为1、嵌入维度均为16、学习率均为0.001；全连接层维度分别为32、16、16、64。与源表一致。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_3_initialization.tex

源文件：source-zh/tables/table_4_3_initialization.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Initialization strategy comparison on Oxford Cell2.}
\label{tab:4-3-initialization}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.20}C{0.93}C{0.93}C{0.94}@{}}
\toprule
Initialization
& \makecell{$R^2$\\mean $\pm$ SD}
& \makecell{RMSE\\mean $\pm$ SD}
& \makecell{MAE\\mean $\pm$ SD} \\
\midrule
\makecell[tl]{Normal\\$\mathcal N(0,0.02^2)$}
& \makecell[c]{$0.98606$\\$\pm0.00411$}
& \makecell[c]{$0.00784$\\$\pm0.00116$}
& \makecell[c]{$0.00490$\\$\pm0.00054$} \\
\makecell[tl]{Truncated normal\\($\pm2\sigma$)}
& \makecell[c]{$0.98645$\\$\pm0.00371$}
& \makecell[c]{$0.00774$\\$\pm0.00103$}
& \makecell[c]{$0.00485$\\$\pm0.00048$} \\
Xavier uniform
& \makecell[c]{$0.98527$\\$\pm0.00462$}
& \makecell[c]{$0.00805$\\$\pm0.00126$}
& \makecell[c]{$0.00499$\\$\pm0.00058$} \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Initialization strategy comparison on Oxford Cell2.}
\label{tab:4-3-initialization}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.20}C{0.93}C{0.93}C{0.94}@{}}
\toprule
Initialization
& \makecell{$R^2$\\mean $\pm$ SD}
& \makecell{RMSE\\mean $\pm$ SD}
& \makecell{MAE\\mean $\pm$ SD} \\
\midrule
\makecell[tl]{Normal\\$\mathcal N(0,0.02^2)$}
& \makecell[c]{$0.98606$\\$\pm0.00411$}
& \makecell[c]{$0.00784$\\$\pm0.00116$}
& \makecell[c]{$0.00490$\\$\pm0.00054$} \\
\makecell[tl]{Truncated normal\\($\pm2\sigma$)}
& \makecell[c]{$0.98645$\\$\pm0.00371$}
& \makecell[c]{$0.00774$\\$\pm0.00103$}
& \makecell[c]{$0.00485$\\$\pm0.00048$} \\
Xavier uniform
& \makecell[c]{$0.98527$\\$\pm0.00462$}
& \makecell[c]{$0.00805$\\$\pm0.00126$}
& \makecell[c]{$0.00499$\\$\pm0.00058$} \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：Oxford Cell2上的初始化策略比较。表头：初始化；R²、RMSE和MAE的均值±标准差。正态N(0,0.02²)；截断正态（±2σ）；Xavier均匀初始化。均值、标准差和截断范围保留；没有将差异写为统计显著。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_3.tex

源文件：source-zh/tables/table_4_3.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Convergence characteristics of MS-AgentNet on the Oxford and MIT datasets.}
\label{tab:4-3}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.85}C{1.35}C{1.15}C{1.10}@{}}
\toprule
Dataset & \makecell[c]{10\% threshold epoch\\median [range]} & \makecell[c]{Late loss mean\\median} & \makecell[c]{Late loss SD\\median} \\
\midrule
Oxford & 26 [18--35] & $8.14\times10^{-4}$ & $2.38\times10^{-4}$ \\
MIT & 7 [6--8] & $5.84\times10^{-5}$ & $4.84\times10^{-6}$ \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Convergence characteristics of MS-AgentNet on the Oxford and MIT datasets.}
\label{tab:4-3}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.85}C{1.35}C{1.15}C{1.10}@{}}
\toprule
Dataset & \makecell[c]{10\% threshold epoch\\median [range]} & \makecell[c]{Late loss mean\\median} & \makecell[c]{Late loss SD\\median} \\
\midrule
Oxford & 26 [18--35] & $8.14\times10^{-4}$ & $2.38\times10^{-4}$ \\
MIT & 7 [6--8] & $5.84\times10^{-5}$ & $4.84\times10^{-6}$ \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：MS-AgentNet在Oxford和MIT数据集上的收敛特性。表头：数据集；10%阈值轮次的中位数[范围]；后期损失均值的中位数；后期损失标准差的中位数。Oxford为26[18–35]、8.14×10^-4、2.38×10^-4；MIT为7[6–8]、5.84×10^-5、4.84×10^-6。嵌套统计含义保留。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_4.tex

源文件：source-zh/tables/table_4_4.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}[H]
\TableStyle
\caption{Layer configurations of different deep learning models.}
\label{tab:4-4}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.96}L{1.10}L{1.03}L{1.18}L{0.73}@{}}
\toprule
MS-AgentNet & CNN-\newline Transformer & Transformer & CNN-LSTM & LSTM \\
\midrule
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Embedding layer\newline(16)\TableLayerSep
SLFA module\TableLayerSep
DSConv-L module\TableLayerSep
Add \& Norm\TableLayerSep
FFN\TableLayerSep
Add \& Norm\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Embedding layer\newline(16)\TableLayerSep
Positional encoder\TableLayerSep
Softmax attention\TableLayerSep
$2\times$ Conv1D + ReLU\TableLayerSep
MLP\TableLayerSep
Transformer decoder\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Embedding layer\newline(16)\TableLayerSep
Positional encoder\TableLayerSep
Softmax attention\TableLayerSep
Add \& Norm\TableLayerSep
MLP\TableLayerSep
Add \& Norm\TableLayerSep
Transformer decoder\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Conv1D + ReLU\TableLayerSep
MaxPooling1D\TableLayerSep
$3\times$ Conv1D + ReLU\TableLayerSep
$3\times$ LSTM layer (16)\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Linear layer (16)\TableLayerSep
$5\times$ LSTM layer (16)\TableLayerSep
Linear layer
\end{minipage}
\\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}[H]
\TableStyle
\caption{Layer configurations of different deep learning models.}
\label{tab:4-4}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.96}L{1.10}L{1.03}L{1.18}L{0.73}@{}}
\toprule
MS-AgentNet & CNN-\newline Transformer & Transformer & CNN-LSTM & LSTM \\
\midrule
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Embedding layer\newline(16)\TableLayerSep
SLFA module\TableLayerSep
DSConv-L module\TableLayerSep
Add \& Norm\TableLayerSep
FFN\TableLayerSep
Add \& Norm\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Embedding layer\newline(16)\TableLayerSep
Positional encoder\TableLayerSep
Softmax attention\TableLayerSep
$2\times$ Conv1D + ReLU\TableLayerSep
MLP\TableLayerSep
Transformer decoder\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Embedding layer\newline(16)\TableLayerSep
Positional encoder\TableLayerSep
Softmax attention\TableLayerSep
Add \& Norm\TableLayerSep
MLP\TableLayerSep
Add \& Norm\TableLayerSep
Transformer decoder\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Conv1D + ReLU\TableLayerSep
MaxPooling1D\TableLayerSep
$3\times$ Conv1D + ReLU\TableLayerSep
$3\times$ LSTM layer (16)\TableLayerSep
Linear layer
\end{minipage}
&
\begin{minipage}[t]{\hsize}\vspace{0pt}\raggedright\setlength{\parskip}{0pt}
Input\TableLayerSep
Linear layer (16)\TableLayerSep
$5\times$ LSTM layer (16)\TableLayerSep
Linear layer
\end{minipage}
\\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：不同深度学习模型的层配置。MS-AgentNet列：输入→嵌入层(16)→SLFA模块→DSConv-L模块→相加与归一化→FFN→相加与归一化→线性层。CNN-Transformer列：输入→嵌入层(16)→位置编码器→Softmax注意力→2×一维卷积+ReLU→MLP→Transformer解码器→线性层。Transformer列：输入→嵌入层(16)→位置编码器→Softmax注意力→相加与归一化→MLP→相加与归一化→Transformer解码器→线性层。CNN-LSTM列：输入→一维卷积+ReLU→一维最大池化→3×一维卷积+ReLU→3×LSTM层(16)→线性层。LSTM列：输入→线性层(16)→5×LSTM层(16)→线性层。该表为主性能对比的结构说明，不能与复杂度实验另设4层LSTM直接判矛盾。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_5.tex

源文件：source-zh/tables/table_4_5.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begingroup
\TableStyle
\renewcommand{\arraystretch}{0.98}
\setlength\LTleft{0pt plus 1fill}
\setlength\LTright{0pt plus 1fill}
\begin{longtable}{@{}p{16mm}p{41mm}>{\centering\arraybackslash}p{23mm}>{\centering\arraybackslash}p{23mm}>{\centering\arraybackslash}p{23mm}>{\centering\arraybackslash}p{23mm}@{}}
\caption{SOH estimation errors of different models on the Oxford dataset.}\label{tab:4-5}\\
\toprule
Cell & Method & $R^2$ & MAE & MAPE & RMSE \\
\midrule
\endfirsthead
\multicolumn{6}{@{}l}{\fontsize{8.5pt}{11pt}\selectfont Table~\thetable\ continued}\\
\toprule
Cell & Method & $R^2$ & MAE & MAPE & RMSE \\
\midrule
\endhead
\midrule
\multicolumn{6}{r}{\fontsize{8pt}{10pt}\selectfont Continued on next page}\\
\endfoot
\bottomrule
\endlastfoot
Cell2$^{*}$  & MS-AgentNet       & \textbf{0.98890} & \textbf{0.00437} & \textbf{0.00535} & \textbf{0.00706} \\
             & CNN-Transformer  & 0.98532          & 0.00497          & 0.00609          & 0.00812          \\
             & CNN-LSTM         & 0.98341          & 0.00521          & 0.00635          & 0.00863          \\
             & Transformer      & 0.98571          & 0.00512          & 0.00622          & 0.00800          \\
             & LSTM             & 0.97880          & 0.00590          & 0.00725          & 0.00977          \\
\TableGroupSpace
Cell3   & MS-AgentNet       & \textbf{0.99638} & \textbf{0.00295} & \textbf{0.00351} & \textbf{0.00366} \\
        & CNN-Transformer   & 0.99523          & 0.00335          & 0.00396          & 0.00420          \\
        & CNN-LSTM          & 0.99501          & 0.00343          & 0.00404          & 0.00429          \\
        & Transformer       & 0.99472          & 0.00362          & 0.00423          & 0.00440          \\
        & LSTM              & 0.99529          & 0.00327          & 0.00390          & 0.00418          \\
\TableGroupSpace
Cell4   & MS-AgentNet       & \textbf{0.97052} & 0.00838          & 0.00988          & \textbf{0.00898} \\
        & CNN-Transformer   & 0.96942          & \textbf{0.00819} & 0.00969          & 0.00914          \\
        & CNN-LSTM          & 0.96712          & 0.00871          & 0.01026          & 0.00949          \\
        & Transformer       & 0.96931          & 0.00820          & \textbf{0.00966} & 0.00916          \\
        & LSTM              & 0.96267          & 0.00937          & 0.01103          & 0.01011          \\
\TableGroupSpace
Cell5   & MS-AgentNet       & \textbf{0.99257} & \textbf{0.00314} & \textbf{0.00357} & \textbf{0.00362} \\
        & CNN-Transformer   & 0.99002          & 0.00344          & 0.00389          & 0.00417          \\
        & CNN-LSTM          & 0.98912          & 0.00351          & 0.00397          & 0.00434          \\
        & Transformer       & 0.98727          & 0.00391          & 0.00437          & 0.00468          \\
        & LSTM              & 0.99036          & 0.00355          & 0.00400          & 0.00412          \\
\TableGroupSpace
Cell6   & MS-AgentNet       & \textbf{0.96832} & \textbf{0.00619} & \textbf{0.00733} & \textbf{0.00860} \\
        & CNN-Transformer   & 0.96442          & 0.00646          & 0.00764          & 0.00911          \\
        & CNN-LSTM          & 0.96226          & 0.00650          & 0.00771          & 0.00939          \\
        & Transformer       & 0.96402          & 0.00696          & 0.00815          & 0.00917          \\
        & LSTM              & 0.95868          & 0.00626          & 0.00747          & 0.00983          \\
\TableGroupSpace
Cell7   & MS-AgentNet       & 0.97566          & 0.00777          & 0.00894          & 0.00804          \\
        & CNN-Transformer   & \textbf{0.97781} & 0.00731          & 0.00841          & \textbf{0.00766} \\
        & CNN-LSTM          & 0.97081          & 0.00841          & 0.00964          & 0.00880          \\
        & Transformer       & 0.97750          & \textbf{0.00719} & \textbf{0.00830} & 0.00769          \\
        & LSTM              & 0.96768          & 0.00886          & 0.01016          & 0.00926          \\
\TableGroupSpace
Cell8   & MS-AgentNet       & 0.99419          & 0.00389          & 0.00445          & 0.00469          \\
        & CNN-Transformer   & 0.99434          & 0.00384          & 0.00442          & 0.00462          \\
        & CNN-LSTM          & 0.99207          & 0.00445          & 0.00508          & 0.00548          \\
        & Transformer       & \textbf{0.99528} & \textbf{0.00326} & \textbf{0.00377} & \textbf{0.00422} \\
        & LSTM              & 0.99115          & 0.00474          & 0.00539          & 0.00579          \\
\TableGroupSpace
Average & MS-AgentNet       & \textbf{0.98379} & \textbf{0.00524} & \textbf{0.00615} & \textbf{0.00638} \\
        & CNN-Transformer   & 0.98237          & 0.00537          & 0.00630          & 0.00672          \\
        & CNN-LSTM          & 0.97997          & 0.00575          & 0.00672          & 0.00720          \\
        & Transformer       & 0.98197          & 0.00547          & 0.00639          & 0.00676          \\
        & LSTM              & 0.97780          & 0.00599          & 0.00703          & 0.00758          \\
\end{longtable}
\TableNote{Note: Cell2$^{*}$ denotes the cell used for model configuration, and its values are averages of five independent runs. The best results are shown in bold.}
\endgroup
```

当前英文：

```latex
\begingroup
\TableStyle
\renewcommand{\arraystretch}{0.98}
\setlength\LTleft{0pt plus 1fill}
\setlength\LTright{0pt plus 1fill}
\begin{longtable}{@{}p{16mm}p{41mm}>{\centering\arraybackslash}p{23mm}>{\centering\arraybackslash}p{23mm}>{\centering\arraybackslash}p{23mm}>{\centering\arraybackslash}p{23mm}@{}}
\caption{SOH estimation errors of different models on the Oxford dataset.}\label{tab:4-5}\\
\toprule
Cell & Method & $R^2$ & MAE & MAPE & RMSE \\
\midrule
\endfirsthead
\multicolumn{6}{@{}l}{\fontsize{8.5pt}{11pt}\selectfont Table~\thetable\ continued}\\
\toprule
Cell & Method & $R^2$ & MAE & MAPE & RMSE \\
\midrule
\endhead
\midrule
\multicolumn{6}{r}{\fontsize{8pt}{10pt}\selectfont Continued on next page}\\
\endfoot
\bottomrule
\endlastfoot
Cell2$^{*}$  & MS-AgentNet       & \textbf{0.98890} & \textbf{0.00437} & \textbf{0.00535} & \textbf{0.00706} \\
             & CNN-Transformer  & 0.98532          & 0.00497          & 0.00609          & 0.00812          \\
             & CNN-LSTM         & 0.98341          & 0.00521          & 0.00635          & 0.00863          \\
             & Transformer      & 0.98571          & 0.00512          & 0.00622          & 0.00800          \\
             & LSTM             & 0.97880          & 0.00590          & 0.00725          & 0.00977          \\
\TableGroupSpace
Cell3   & MS-AgentNet       & \textbf{0.99638} & \textbf{0.00295} & \textbf{0.00351} & \textbf{0.00366} \\
        & CNN-Transformer   & 0.99523          & 0.00335          & 0.00396          & 0.00420          \\
        & CNN-LSTM          & 0.99501          & 0.00343          & 0.00404          & 0.00429          \\
        & Transformer       & 0.99472          & 0.00362          & 0.00423          & 0.00440          \\
        & LSTM              & 0.99529          & 0.00327          & 0.00390          & 0.00418          \\
\TableGroupSpace
Cell4   & MS-AgentNet       & \textbf{0.97052} & 0.00838          & 0.00988          & \textbf{0.00898} \\
        & CNN-Transformer   & 0.96942          & \textbf{0.00819} & 0.00969          & 0.00914          \\
        & CNN-LSTM          & 0.96712          & 0.00871          & 0.01026          & 0.00949          \\
        & Transformer       & 0.96931          & 0.00820          & \textbf{0.00966} & 0.00916          \\
        & LSTM              & 0.96267          & 0.00937          & 0.01103          & 0.01011          \\
\TableGroupSpace
Cell5   & MS-AgentNet       & \textbf{0.99257} & \textbf{0.00314} & \textbf{0.00357} & \textbf{0.00362} \\
        & CNN-Transformer   & 0.99002          & 0.00344          & 0.00389          & 0.00417          \\
        & CNN-LSTM          & 0.98912          & 0.00351          & 0.00397          & 0.00434          \\
        & Transformer       & 0.98727          & 0.00391          & 0.00437          & 0.00468          \\
        & LSTM              & 0.99036          & 0.00355          & 0.00400          & 0.00412          \\
\TableGroupSpace
Cell6   & MS-AgentNet       & \textbf{0.96832} & \textbf{0.00619} & \textbf{0.00733} & \textbf{0.00860} \\
        & CNN-Transformer   & 0.96442          & 0.00646          & 0.00764          & 0.00911          \\
        & CNN-LSTM          & 0.96226          & 0.00650          & 0.00771          & 0.00939          \\
        & Transformer       & 0.96402          & 0.00696          & 0.00815          & 0.00917          \\
        & LSTM              & 0.95868          & 0.00626          & 0.00747          & 0.00983          \\
\TableGroupSpace
Cell7   & MS-AgentNet       & 0.97566          & 0.00777          & 0.00894          & 0.00804          \\
        & CNN-Transformer   & \textbf{0.97781} & 0.00731          & 0.00841          & \textbf{0.00766} \\
        & CNN-LSTM          & 0.97081          & 0.00841          & 0.00964          & 0.00880          \\
        & Transformer       & 0.97750          & \textbf{0.00719} & \textbf{0.00830} & 0.00769          \\
        & LSTM              & 0.96768          & 0.00886          & 0.01016          & 0.00926          \\
\TableGroupSpace
Cell8   & MS-AgentNet       & 0.99419          & 0.00389          & 0.00445          & 0.00469          \\
        & CNN-Transformer   & 0.99434          & 0.00384          & 0.00442          & 0.00462          \\
        & CNN-LSTM          & 0.99207          & 0.00445          & 0.00508          & 0.00548          \\
        & Transformer       & \textbf{0.99528} & \textbf{0.00326} & \textbf{0.00377} & \textbf{0.00422} \\
        & LSTM              & 0.99115          & 0.00474          & 0.00539          & 0.00579          \\
\TableGroupSpace
Average & MS-AgentNet       & \textbf{0.98379} & \textbf{0.00524} & \textbf{0.00615} & \textbf{0.00638} \\
        & CNN-Transformer   & 0.98237          & 0.00537          & 0.00630          & 0.00672          \\
        & CNN-LSTM          & 0.97997          & 0.00575          & 0.00672          & 0.00720          \\
        & Transformer       & 0.98197          & 0.00547          & 0.00639          & 0.00676          \\
        & LSTM              & 0.97780          & 0.00599          & 0.00703          & 0.00758          \\
\end{longtable}
\TableNote{Note: Cell2$^{*}$ denotes the cell used for model configuration, and its values are averages of five independent runs. The best results are shown in bold.}
\endgroup
```

中文回译（助手）：

表题：不同模型在Oxford数据集上的SOH估计误差。表头：电池、方法、R²、MAE、MAPE、RMSE；Average为平均值；continued/Continued on next page为续表/续下页。脚注：Cell2*表示用于模型配置的电池，其数值为五次独立运行的平均值。最佳结果以粗体标出。这个五次平均限定仅明确用于Cell2，不自动扩大到其他电池。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_6.tex

源文件：source-zh/tables/table_4_6.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{SOH estimation errors of different models on the CALCE and MIT/Severson datasets.}
\label{tab:4-6}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.85}L{1.55}C{0.90}C{0.90}C{0.90}C{0.90}@{}}
\toprule
Dataset & Method & $R^2$ & MAE & MAPE & RMSE \\
\midrule
\makecell[l]{CALCE CS2\\(CS2\_37$^{*}$)} & MS-AgentNet       & \textbf{0.9925} & \textbf{0.00733} & \textbf{0.009443} & \textbf{0.01172} \\
                                           & CNN-Transformer   & 0.9923          & 0.00742          & 0.009532          & 0.01182          \\
                                           & CNN-LSTM          & 0.9917          & 0.00800          & 0.010232          & 0.01229          \\
                                           & Transformer       & 0.9923          & 0.00737          & 0.009449          & 0.01182          \\
                                           & LSTM              & 0.9915          & 0.00795          & 0.010106          & 0.01246          \\
\TableGroupSpace
\makecell[l]{CALCE CS2\\(CS2\_38)} & MS-AgentNet       & \textbf{0.9798} & \textbf{0.01201} & \textbf{0.015984} & \textbf{0.01741} \\
                                    & CNN-Transformer   & 0.9779          & 0.01261          & 0.016928          & 0.01823          \\
                                    & CNN-LSTM          & 0.9778          & 0.01249          & 0.016680          & 0.01826          \\
                                    & Transformer       & 0.9787          & 0.01216          & 0.016434          & 0.01789          \\
                                    & LSTM              & 0.9776          & 0.01280          & 0.017085          & 0.01836          \\
\TableGroupSpace
\makecell[l]{CALCE CX2\\(CX2\_37$^{*}$)} & MS-AgentNet       & \textbf{0.9765} & \textbf{0.00916} & \textbf{0.013328} & \textbf{0.01845} \\
                                           & CNN-Transformer   & 0.9753          & 0.00981          & 0.014209          & 0.01891          \\
                                           & CNN-LSTM          & 0.9759          & 0.00974          & 0.014147          & 0.01868          \\
                                           & Transformer       & 0.9748          & 0.01004          & 0.014510          & 0.01909          \\
                                           & LSTM              & 0.9752          & 0.00987          & 0.014322          & 0.01895          \\
\TableGroupSpace
\makecell[l]{CALCE CX2\\(CX2\_38)} & MS-AgentNet       & \textbf{0.9947} & \textbf{0.01059} & \textbf{0.037673} & \textbf{0.01928} \\
                                    & CNN-Transformer   & 0.9895          & 0.01536          & 0.093595          & 0.02693          \\
                                    & CNN-LSTM          & 0.9785          & 0.02072          & 0.152435          & 0.03866          \\
                                    & Transformer       & 0.9916          & 0.01378          & 0.078160          & 0.02428          \\
                                    & LSTM              & 0.9804          & 0.02008          & 0.145055          & 0.03704          \\
\TableGroupSpace
\makecell[l]{MIT/Severson\\(b3c13$^{*}$)} & MS-AgentNet      & 0.9967          & 0.00148          & 0.001622          & 0.00229          \\
                                            & CNN-Transformer  & 0.9954          & 0.00167          & 0.001832          & 0.00262          \\
                                            & CNN-LSTM         & 0.9855          & 0.00284          & 0.003121          & 0.00476          \\
                                            & Transformer      & \textbf{0.9968} & \textbf{0.00146} & \textbf{0.001599} & \textbf{0.00220} \\
                                            & LSTM             & 0.9940          & 0.00184          & 0.002020          & 0.00309          \\
\TableGroupSpace
\makecell[l]{MIT/Severson\\(b3c29)} & MS-AgentNet      & \textbf{0.9972} & \textbf{0.00183} & \textbf{0.001960} & \textbf{0.00215} \\
                                      & CNN-Transformer  & 0.9960          & 0.00214          & 0.002302          & 0.00254          \\
                                      & CNN-LSTM         & 0.9879          & 0.00353          & 0.003808          & 0.00438          \\
                                      & Transformer      & 0.9971          & 0.00184          & 0.001976          & 0.00219          \\
                                      & LSTM             & 0.9952          & 0.00249          & 0.002667          & 0.00280          \\
\TableGroupSpace
Average                               & MS-AgentNet      & \textbf{0.9896} & \textbf{0.00707} & \textbf{0.013335} & \textbf{0.01188} \\
                                      & CNN-Transformer  & 0.9877          & 0.00817          & 0.023066          & 0.01351          \\
                                      & CNN-LSTM         & 0.9829          & 0.00955          & 0.033404          & 0.01617          \\
                                      & Transformer      & 0.9885          & 0.00778          & 0.020355          & 0.01291          \\
                                      & LSTM             & 0.9856          & 0.00917          & 0.031876          & 0.01545          \\
\bottomrule
\end{tabularx}
\TableNote{Note: CS2\_37$^{*}$, CX2\_37$^{*}$, and b3c13$^{*}$ denote the cells used for model configuration. The best results are shown in bold.}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{SOH estimation errors of different models on the CALCE and MIT/Severson datasets.}
\label{tab:4-6}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.85}L{1.55}C{0.90}C{0.90}C{0.90}C{0.90}@{}}
\toprule
Dataset & Method & $R^2$ & MAE & MAPE & RMSE \\
\midrule
\makecell[l]{CALCE CS2\\(CS2\_37$^{*}$)} & MS-AgentNet       & \textbf{0.9925} & \textbf{0.00733} & \textbf{0.009443} & \textbf{0.01172} \\
                                           & CNN-Transformer   & 0.9923          & 0.00742          & 0.009532          & 0.01182          \\
                                           & CNN-LSTM          & 0.9917          & 0.00800          & 0.010232          & 0.01229          \\
                                           & Transformer       & 0.9923          & 0.00737          & 0.009449          & 0.01182          \\
                                           & LSTM              & 0.9915          & 0.00795          & 0.010106          & 0.01246          \\
\TableGroupSpace
\makecell[l]{CALCE CS2\\(CS2\_38)} & MS-AgentNet       & \textbf{0.9798} & \textbf{0.01201} & \textbf{0.015984} & \textbf{0.01741} \\
                                    & CNN-Transformer   & 0.9779          & 0.01261          & 0.016928          & 0.01823          \\
                                    & CNN-LSTM          & 0.9778          & 0.01249          & 0.016680          & 0.01826          \\
                                    & Transformer       & 0.9787          & 0.01216          & 0.016434          & 0.01789          \\
                                    & LSTM              & 0.9776          & 0.01280          & 0.017085          & 0.01836          \\
\TableGroupSpace
\makecell[l]{CALCE CX2\\(CX2\_37$^{*}$)} & MS-AgentNet       & \textbf{0.9765} & \textbf{0.00916} & \textbf{0.013328} & \textbf{0.01845} \\
                                           & CNN-Transformer   & 0.9753          & 0.00981          & 0.014209          & 0.01891          \\
                                           & CNN-LSTM          & 0.9759          & 0.00974          & 0.014147          & 0.01868          \\
                                           & Transformer       & 0.9748          & 0.01004          & 0.014510          & 0.01909          \\
                                           & LSTM              & 0.9752          & 0.00987          & 0.014322          & 0.01895          \\
\TableGroupSpace
\makecell[l]{CALCE CX2\\(CX2\_38)} & MS-AgentNet       & \textbf{0.9947} & \textbf{0.01059} & \textbf{0.037673} & \textbf{0.01928} \\
                                    & CNN-Transformer   & 0.9895          & 0.01536          & 0.093595          & 0.02693          \\
                                    & CNN-LSTM          & 0.9785          & 0.02072          & 0.152435          & 0.03866          \\
                                    & Transformer       & 0.9916          & 0.01378          & 0.078160          & 0.02428          \\
                                    & LSTM              & 0.9804          & 0.02008          & 0.145055          & 0.03704          \\
\TableGroupSpace
\makecell[l]{MIT/Severson\\(b3c13$^{*}$)} & MS-AgentNet      & 0.9967          & 0.00148          & 0.001622          & 0.00229          \\
                                            & CNN-Transformer  & 0.9954          & 0.00167          & 0.001832          & 0.00262          \\
                                            & CNN-LSTM         & 0.9855          & 0.00284          & 0.003121          & 0.00476          \\
                                            & Transformer      & \textbf{0.9968} & \textbf{0.00146} & \textbf{0.001599} & \textbf{0.00220} \\
                                            & LSTM             & 0.9940          & 0.00184          & 0.002020          & 0.00309          \\
\TableGroupSpace
\makecell[l]{MIT/Severson\\(b3c29)} & MS-AgentNet      & \textbf{0.9972} & \textbf{0.00183} & \textbf{0.001960} & \textbf{0.00215} \\
                                      & CNN-Transformer  & 0.9960          & 0.00214          & 0.002302          & 0.00254          \\
                                      & CNN-LSTM         & 0.9879          & 0.00353          & 0.003808          & 0.00438          \\
                                      & Transformer      & 0.9971          & 0.00184          & 0.001976          & 0.00219          \\
                                      & LSTM             & 0.9952          & 0.00249          & 0.002667          & 0.00280          \\
\TableGroupSpace
Average                               & MS-AgentNet      & \textbf{0.9896} & \textbf{0.00707} & \textbf{0.013335} & \textbf{0.01188} \\
                                      & CNN-Transformer  & 0.9877          & 0.00817          & 0.023066          & 0.01351          \\
                                      & CNN-LSTM         & 0.9829          & 0.00955          & 0.033404          & 0.01617          \\
                                      & Transformer      & 0.9885          & 0.00778          & 0.020355          & 0.01291          \\
                                      & LSTM             & 0.9856          & 0.00917          & 0.031876          & 0.01545          \\
\bottomrule
\end{tabularx}
\TableNote{Note: CS2\_37$^{*}$, CX2\_37$^{*}$, and b3c13$^{*}$ denote the cells used for model configuration. The best results are shown in bold.}
\end{table}
```

中文回译（助手）：

表题：不同模型在CALCE和MIT/Severson数据集上的SOH估计误差。表头：数据集、方法、R²、MAE、MAPE、RMSE。Average为平均值。脚注：CS2_37*、CX2_37*和b3c13*表示用于模型配置的电池。最佳结果以粗体标出。没有把配置电池的误差改称完全未参与配置的测试误差。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_7.tex

源文件：source-zh/tables/table_4_7.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Direct cross-dataset transfer results.}
\label{tab:4-7}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}L{0.90}C{1.20}C{1.00}C{1.00}C{1.00}@{}}
\toprule
Source & Target & $R^2$ & MAE & MAPE & RMSE \\
\midrule
CS2 & CX2 & $0.8421$ & $0.0697$ & $0.3974$ & $0.1051$ \\
CS2 & Oxford & $-60.5701$ & $0.4761$ & $0.5573$ & $0.4778$ \\
CX2 & CS2 & $0.7847$ & $0.0388$ & $0.0557$ & $0.0568$ \\
CX2 & Oxford & $-108.6169$ & $0.6346$ & $0.7423$ & $0.6375$ \\
Oxford & CS2 & $-1.5309$ & $0.1530$ & $0.2196$ & $0.1950$ \\
Oxford & CX2 & $-1.4786$ & $0.3528$ & $1.5040$ & $0.4164$ \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Direct cross-dataset transfer results.}
\label{tab:4-7}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}L{0.90}C{1.20}C{1.00}C{1.00}C{1.00}@{}}
\toprule
Source & Target & $R^2$ & MAE & MAPE & RMSE \\
\midrule
CS2 & CX2 & $0.8421$ & $0.0697$ & $0.3974$ & $0.1051$ \\
CS2 & Oxford & $-60.5701$ & $0.4761$ & $0.5573$ & $0.4778$ \\
CX2 & CS2 & $0.7847$ & $0.0388$ & $0.0557$ & $0.0568$ \\
CX2 & Oxford & $-108.6169$ & $0.6346$ & $0.7423$ & $0.6375$ \\
Oxford & CS2 & $-1.5309$ & $0.1530$ & $0.2196$ & $0.1950$ \\
Oxford & CX2 & $-1.4786$ & $0.3528$ & $1.5040$ & $0.4164$ \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：直接跨数据集迁移结果。表头：源域、目标域、R²、MAE、MAPE、RMSE。六个方向及负R²全部保留，source/target没有对调；直接迁移在正文定义为source-only。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_8.tex

源文件：source-zh/tables/table_4_8.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Transfer results after 30\% target-domain adaptation.}
\label{tab:4-8}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}L{0.90}C{1.20}C{1.00}C{1.00}C{1.00}@{}}
\toprule
Source & Target & $R^2$ & MAE & MAPE & RMSE \\
\midrule
CS2 & CX2 & $0.9566$ & $0.0377$ & $0.1830$ & $0.0533$ \\
CS2 & Oxford & $-0.2679$ & $0.0590$ & $0.0722$ & $0.0685$ \\
CX2 & CS2 & $0.8806$ & $0.0303$ & $0.0406$ & $0.0422$ \\
CX2 & Oxford & $-1.6085$ & $0.0835$ & $0.1024$ & $0.0982$ \\
Oxford & CS2 & $-1.1030$ & $0.1327$ & $0.1935$ & $0.1777$ \\
Oxford & CX2 & $-0.4809$ & $0.2427$ & $1.2100$ & $0.3218$ \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Transfer results after 30\% target-domain adaptation.}
\label{tab:4-8}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{0.90}L{0.90}C{1.20}C{1.00}C{1.00}C{1.00}@{}}
\toprule
Source & Target & $R^2$ & MAE & MAPE & RMSE \\
\midrule
CS2 & CX2 & $0.9566$ & $0.0377$ & $0.1830$ & $0.0533$ \\
CS2 & Oxford & $-0.2679$ & $0.0590$ & $0.0722$ & $0.0685$ \\
CX2 & CS2 & $0.8806$ & $0.0303$ & $0.0406$ & $0.0422$ \\
CX2 & Oxford & $-1.6085$ & $0.0835$ & $0.1024$ & $0.0982$ \\
Oxford & CS2 & $-1.1030$ & $0.1327$ & $0.1935$ & $0.1777$ \\
Oxford & CX2 & $-0.4809$ & $0.2427$ & $1.2100$ & $0.3218$ \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：经过30%目标域适应后的迁移结果。表头：源域、目标域、R²、MAE、MAPE、RMSE。30%的分母及前置循环含义由正文提供。涉及Oxford的负R²仍保留。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_9.tex

源文件：source-zh/tables/table_4_9.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}
\TableStyle
\caption{Transfer results with different amounts of target-domain data.}
\label{tab:4-9}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.60}C{1.20}C{0.80}C{0.80}C{0.80}C{0.80}@{}}
\toprule
Transfer & Target data (\%) & $R^2$ & MAE & MAPE & RMSE \\
\midrule
CS2 $\to$ Oxford & 10 & $-1.3934$ & $0.0831$ & $0.1015$ & $0.0942$ \\
CS2 $\to$ Oxford & 30 & $-0.2679$ & $0.0590$ & $0.0722$ & $0.0685$ \\
CS2 $\to$ Oxford & 50 & $0.5094$ & $0.0366$ & $0.0445$ & $0.0426$ \\
CS2 $\to$ Oxford & 70 & $0.7650$ & $0.0252$ & $0.0305$ & $0.0293$ \\
\TableGroupSpace
CX2 $\to$ Oxford & 10 & $-3.2217$ & $0.1095$ & $0.1339$ & $0.1251$ \\
CX2 $\to$ Oxford & 30 & $-1.6085$ & $0.0835$ & $0.1024$ & $0.0982$ \\
CX2 $\to$ Oxford & 50 & $-0.3836$ & $0.0614$ & $0.0747$ & $0.0716$ \\
CX2 $\to$ Oxford & 70 & $-0.1268$ & $0.0559$ & $0.0677$ & $0.0646$ \\
\bottomrule
\end{tabularx}
\end{table}
```

当前英文：

```latex
\begin{table}
\TableStyle
\caption{Transfer results with different amounts of target-domain data.}
\label{tab:4-9}
\begin{tabularx}{\linewidth}{@{\extracolsep{\fill}}L{1.60}C{1.20}C{0.80}C{0.80}C{0.80}C{0.80}@{}}
\toprule
Transfer & Target data (\%) & $R^2$ & MAE & MAPE & RMSE \\
\midrule
CS2 $\to$ Oxford & 10 & $-1.3934$ & $0.0831$ & $0.1015$ & $0.0942$ \\
CS2 $\to$ Oxford & 30 & $-0.2679$ & $0.0590$ & $0.0722$ & $0.0685$ \\
CS2 $\to$ Oxford & 50 & $0.5094$ & $0.0366$ & $0.0445$ & $0.0426$ \\
CS2 $\to$ Oxford & 70 & $0.7650$ & $0.0252$ & $0.0305$ & $0.0293$ \\
\TableGroupSpace
CX2 $\to$ Oxford & 10 & $-3.2217$ & $0.1095$ & $0.1339$ & $0.1251$ \\
CX2 $\to$ Oxford & 30 & $-1.6085$ & $0.0835$ & $0.1024$ & $0.0982$ \\
CX2 $\to$ Oxford & 50 & $-0.3836$ & $0.0614$ & $0.0747$ & $0.0716$ \\
CX2 $\to$ Oxford & 70 & $-0.1268$ & $0.0559$ & $0.0677$ & $0.0646$ \\
\bottomrule
\end{tabularx}
\end{table}
```

中文回译（助手）：

表题：不同目标域数据量下的迁移结果。表头：迁移、目标域数据(%)、R²、MAE、MAPE、RMSE。CS2→Oxford与CX2→Oxford的10/30/50/70%各行保留，不将比例变成随机抽样比例。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### tables/table_4_hi_input.tex

源文件：source-zh/tables/table_4_hi_input.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{table}[!htb]
\TableStyle
\fontsize{7pt}{9pt}\selectfont
\setlength{\tabcolsep}{0.8pt}
\renewcommand{\arraystretch}{1.18}
\caption{SOH estimation errors of different health-indicator inputs on the Oxford dataset.}
\label{tab:4-hi-input}
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}l*{15}{c}@{}}
\toprule
& \multicolumn{5}{c}{MAE}
& \multicolumn{5}{c}{RMSE}
& \multicolumn{5}{c}{MAPE} \\
\cmidrule(lr){2-6}\cmidrule(lr){7-11}\cmidrule(lr){12-16}
Cell
& CCCT & IC & DTV & DTC & Fusion
& CCCT & IC & DTV & DTC & Fusion
& CCCT & IC & DTV & DTC & Fusion \\
\midrule
Cell2
& \textbf{\underline{0.00437}} & 0.01607 & 0.01941 & 0.01458 & 0.01256
& \textbf{\underline{0.00706}} & 0.02238 & 0.02145 & 0.01890 & 0.01634
& \textbf{\underline{0.00535}} & 0.02036 & 0.02344 & 0.01810 & 0.01542 \\
Cell3
& \textbf{\underline{0.00295}} & 0.00456 & 0.08852 & 0.01490 & 0.03835
& \textbf{\underline{0.00366}} & 0.00576 & 0.09371 & 0.01770 & 0.04087
& \textbf{\underline{0.00351}} & 0.00527 & 0.10174 & 0.01765 & 0.04466 \\
Cell4
& \textbf{\underline{0.00838}} & 0.00934 & 0.01614 & 0.02349 & 0.01751
& \textbf{\underline{0.00898}} & 0.01249 & 0.01679 & 0.02505 & 0.01898
& \textbf{\underline{0.00988}} & 0.01115 & 0.01867 & 0.02705 & 0.02027 \\
Cell5
& \textbf{\underline{0.00314}} & 0.00819 & 0.03244 & 0.02131 & 0.02085
& \textbf{\underline{0.00362}} & 0.00903 & 0.03532 & 0.02267 & 0.02353
& \textbf{\underline{0.00357}} & 0.00924 & 0.03672 & 0.02428 & 0.02378 \\
Cell6
& \textbf{\underline{0.00619}} & 0.00941 & 0.03163 & 0.00875 & 0.01381
& \textbf{\underline{0.00860}} & 0.01302 & 0.03414 & 0.01276 & 0.01670
& \textbf{\underline{0.00733}} & 0.01087 & 0.03556 & 0.01030 & 0.01604 \\
Cell7
& \textbf{\underline{0.00777}} & 0.01408 & 0.02278 & 0.02534 & 0.01837
& \textbf{\underline{0.00804}} & 0.01499 & 0.02650 & 0.03389 & 0.02344
& \textbf{\underline{0.00894}} & 0.01594 & 0.02619 & 0.03028 & 0.02154 \\
Cell8
& \textbf{\underline{0.00389}} & 0.00967 & 0.05388 & 0.02084 & 0.02694
& \textbf{\underline{0.00469}} & 0.01099 & 0.05597 & 0.02659 & 0.03201
& \textbf{\underline{0.00445}} & 0.01102 & 0.06297 & 0.02530 & 0.03159 \\
\addlinespace[2pt]
Average
& \textbf{\underline{0.00524}} & 0.01019 & 0.03783 & 0.01846 & 0.02120
& \textbf{\underline{0.00638}} & 0.01267 & 0.04055 & 0.02251 & 0.02455
& \textbf{\underline{0.00615}} & 0.01198 & 0.04361 & 0.02185 & 0.02476 \\
\bottomrule
\end{tabular*}
\TableNote{Note: CCCT, IC, DTV, and DTC correspond to HI1, HI4, HI9, and HI11, respectively.}
\end{table}
```

当前英文：

```latex
\begin{table}[!htb]
\TableStyle
\fontsize{7pt}{9pt}\selectfont
\setlength{\tabcolsep}{0.8pt}
\renewcommand{\arraystretch}{1.18}
\caption{SOH estimation errors of different health-indicator inputs on the Oxford dataset.}
\label{tab:4-hi-input}
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}l*{15}{c}@{}}
\toprule
& \multicolumn{5}{c}{MAE}
& \multicolumn{5}{c}{RMSE}
& \multicolumn{5}{c}{MAPE} \\
\cmidrule(lr){2-6}\cmidrule(lr){7-11}\cmidrule(lr){12-16}
Cell
& CCCT & IC & DTV & DTC & Fusion
& CCCT & IC & DTV & DTC & Fusion
& CCCT & IC & DTV & DTC & Fusion \\
\midrule
Cell2
& \textbf{\underline{0.00437}} & 0.01607 & 0.01941 & 0.01458 & 0.01256
& \textbf{\underline{0.00706}} & 0.02238 & 0.02145 & 0.01890 & 0.01634
& \textbf{\underline{0.00535}} & 0.02036 & 0.02344 & 0.01810 & 0.01542 \\
Cell3
& \textbf{\underline{0.00295}} & 0.00456 & 0.08852 & 0.01490 & 0.03835
& \textbf{\underline{0.00366}} & 0.00576 & 0.09371 & 0.01770 & 0.04087
& \textbf{\underline{0.00351}} & 0.00527 & 0.10174 & 0.01765 & 0.04466 \\
Cell4
& \textbf{\underline{0.00838}} & 0.00934 & 0.01614 & 0.02349 & 0.01751
& \textbf{\underline{0.00898}} & 0.01249 & 0.01679 & 0.02505 & 0.01898
& \textbf{\underline{0.00988}} & 0.01115 & 0.01867 & 0.02705 & 0.02027 \\
Cell5
& \textbf{\underline{0.00314}} & 0.00819 & 0.03244 & 0.02131 & 0.02085
& \textbf{\underline{0.00362}} & 0.00903 & 0.03532 & 0.02267 & 0.02353
& \textbf{\underline{0.00357}} & 0.00924 & 0.03672 & 0.02428 & 0.02378 \\
Cell6
& \textbf{\underline{0.00619}} & 0.00941 & 0.03163 & 0.00875 & 0.01381
& \textbf{\underline{0.00860}} & 0.01302 & 0.03414 & 0.01276 & 0.01670
& \textbf{\underline{0.00733}} & 0.01087 & 0.03556 & 0.01030 & 0.01604 \\
Cell7
& \textbf{\underline{0.00777}} & 0.01408 & 0.02278 & 0.02534 & 0.01837
& \textbf{\underline{0.00804}} & 0.01499 & 0.02650 & 0.03389 & 0.02344
& \textbf{\underline{0.00894}} & 0.01594 & 0.02619 & 0.03028 & 0.02154 \\
Cell8
& \textbf{\underline{0.00389}} & 0.00967 & 0.05388 & 0.02084 & 0.02694
& \textbf{\underline{0.00469}} & 0.01099 & 0.05597 & 0.02659 & 0.03201
& \textbf{\underline{0.00445}} & 0.01102 & 0.06297 & 0.02530 & 0.03159 \\
\addlinespace[2pt]
Average
& \textbf{\underline{0.00524}} & 0.01019 & 0.03783 & 0.01846 & 0.02120
& \textbf{\underline{0.00638}} & 0.01267 & 0.04055 & 0.02251 & 0.02455
& \textbf{\underline{0.00615}} & 0.01198 & 0.04361 & 0.02185 & 0.02476 \\
\bottomrule
\end{tabular*}
\TableNote{Note: CCCT, IC, DTV, and DTC correspond to HI1, HI4, HI9, and HI11, respectively.}
\end{table}
```

中文回译（助手）：

表题：Oxford数据集中不同健康指标输入的SOH估计误差。每组MAE、RMSE、MAPE依次列CCCT、IC、DTV、DTC及融合输入；Cell为电池，Average为平均值。脚注：CCCT、IC、DTV和DTC分别对应HI1、HI4、HI9和HI11。Fusion含哪些HI由正文给出，回译为融合输入；表中最小值粗体下划线保留。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/comparison_panel_layout.tex

源文件：source-zh/figures/comparison_panel_layout.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
% Shared physical geometry for Fig. 8 and Fig. 9.
% Every cell: 62 x 70 mm; axes frame: 48 x 54 mm at (13.5, 9).
% Titles are centered on the axes at x = 37.5 mm, not on label padding.
% Per-image transforms preserve all source annotations and equalize frame size.
\providecommand{\ComparisonPanel}[6]{%
  \begingroup\setlength{\unitlength}{1mm}%
  \begin{picture}(62,70)%
    \put(#3,#4){\includegraphics[width=#5mm,height=#6mm]{#2}}%
    \put(37.5,67){\makebox(0,0){\fontsize{10pt}{12pt}\selectfont\bfseries\strut #1}}%
  \end{picture}%
  \endgroup
}
```

当前英文：

```latex
% Shared physical geometry for Fig. 8 and Fig. 9.
% Every cell: 62 x 70 mm; axes frame: 48 x 54 mm at (13.5, 9).
% Titles are centered on the axes at x = 37.5 mm, not on label padding.
% Per-image transforms preserve all source annotations and equalize frame size.
\providecommand{\ComparisonPanel}[6]{%
  \begingroup\setlength{\unitlength}{1mm}%
  \begin{picture}(62,70)%
    \put(#3,#4){\includegraphics[width=#5mm,height=#6mm]{#2}}%
    \put(37.5,67){\makebox(0,0){\fontsize{10pt}{12pt}\selectfont\bfseries\strut #1}}%
  \end{picture}%
  \endgroup
}
```

中文回译（助手）：

共享的排版宏，无需语言回译；图片路径和各子图显示标题在调用处核对。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_2_1.tex

源文件：source-zh/figures/figure_2_1.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[htbp]
\centering
\makebox[\textwidth][c]{%
  \includegraphics[width=160mm,trim=0 75bp 0 5bp,clip]{figures/fig1.png}%
}
\caption{Flowchart of the developed SOH estimation approach.}
\label{fig:2-1}
\end{figure}
```

当前英文：

```latex
\begin{figure}[htbp]
\centering
\makebox[\textwidth][c]{%
  \includegraphics[width=160mm,trim=0 75bp 0 5bp,clip]{figures/fig1.png}%
}
\caption{Flowchart of the developed SOH estimation approach.}
\label{fig:2-1}
\end{figure}
```

中文回译（助手）：

所构建SOH估计方法的流程图。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_2_2.tex

源文件：source-zh/figures/figure_2_2.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=185mm,trim=0 10 10 10,clip]{figures/fig2.png}%
}
\caption{Four battery datasets: (a)--(d) capacity degradation curves of Oxford, CALCE CS2, CALCE CX2, and MIT/Severson cells, respectively; (e)--(h) charging voltage curves of the four datasets in the same order.}
\label{fig:2-2}
\end{figure}
```

当前英文：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=185mm,trim=0 10 10 10,clip]{figures/fig2.png}%
}
\caption{Four battery datasets: (a)--(d) capacity degradation curves of Oxford, CALCE CS2, CALCE CX2, and MIT/Severson cells, respectively; (e)--(h) charging voltage curves of the four datasets in the same order.}
\label{fig:2-2}
\end{figure}
```

中文回译（助手）：

四个电池数据集：(a)–(d)分别为Oxford、CALCE CS2、CALCE CX2和MIT/Severson电池的容量退化曲线；(e)–(h)按同样顺序给出四个数据集的充电电压曲线。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_2_3.tex

源文件：source-zh/figures/figure_2_3.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=175mm]{figures/fig3.png}%
}
\caption{Charge-side characteristic curves used for HI construction.}
\label{fig:2-3}
\end{figure}
```

当前英文：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=175mm]{figures/fig3.png}%
}
\caption{Charge-side characteristic curves used for HI construction.}
\label{fig:2-3}
\end{figure}
```

中文回译（助手）：

用于HI构建的充电侧特征曲线。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_2_4.tex

源文件：source-zh/figures/figure_2_4.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=185mm]{figures/fig4_pccscc_print.png}%
}
\caption{Correlation matrices of candidate HIs and SOH on the Oxford dataset.}
\label{fig:2-4}
\end{figure}
```

当前英文：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \setlength{\unitlength}{1mm}%
  \begin{picture}(185,181)
    \put(0,0){\includegraphics[width=185mm]{figures/fig4_pccscc_print.png}}
    \put(0,177){\makebox(0,0)[l]{\small (a)}}
    \put(98,177){\makebox(0,0)[l]{\small (b)}}
    \put(0,87){\makebox(0,0)[l]{\small (c)}}
    \put(98,87){\makebox(0,0)[l]{\small (d)}}
  \end{picture}%
}
\caption{Correlation matrices of candidate HIs and SOH on the Oxford dataset: (a) Cell1, PCC; (b) Cell1, SCC; (c) Cell2, PCC; (d) Cell2, SCC.}
\label{fig:2-4}
\end{figure}
```

中文回译（助手）：

Oxford数据集中候选HI和SOH的相关性矩阵：(a)Cell1，PCC；(b)Cell1，SCC；(c)Cell2，PCC；(d)Cell2，SCC。与源图题比较，英文工作稿新增了四个子图的对应说明；图像及正文可支持这些对应，但不是逐字保留原图题。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_3_1.tex

源文件：source-zh/figures/figure_3_1.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[!htb]
\centering
\includegraphics[width=0.92\textwidth]{figures/01.png}
\caption{Framework of MS-AgentNet. (a) Overall architecture; (b) core structure; (c) DSConv-L module.}
\label{fig:3-1}
\end{figure}
```

当前英文：

```latex
\begin{figure}[!htb]
\centering
\includegraphics[width=0.92\textwidth]{figures/01.png}
\caption{Framework of MS-AgentNet. (a) Overall architecture; (b) core structure; (c) DSConv-L module.}
\label{fig:3-1}
\end{figure}
```

中文回译（助手）：

MS-AgentNet框架。(a)整体架构；(b)核心结构；(c)DSConv-L模块。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_3_2.tex

源文件：source-zh/figures/figure_3_2.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=175mm]{figures/02.png}%
}
\caption{The fundamental structures of convolutional modules: (a) standard convolution; (b) standard depthwise separable convolution; (c) DSConv-S module; and (d) DSConv-L module.}
\label{fig:3-2}
\end{figure}
```

当前英文：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=175mm]{figures/02.png}%
}
\caption{The fundamental structures of convolutional modules: (a) standard convolution; (b) standard depthwise separable convolution; (c) DSConv-S module; and (d) DSConv-L module.}
\label{fig:3-2}
\end{figure}
```

中文回译（助手）：

卷积模块的基本结构：(a)标准卷积；(b)标准深度可分离卷积；(c)DSConv-S模块；(d)DSConv-L模块。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_3_3.tex

源文件：source-zh/figures/figure_3_3.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=190mm,trim=0 40bp 0 35bp,clip]{figures/fig3_3_attention_comparison.png}%
}
\caption{Comparison of (a) Softmax attention, (b) linear attention, (c) Agent Attention, and (d) the proposed SLFA module.}
\label{fig:3-3}
\end{figure}
```

当前英文：

```latex
\begin{figure}[!htb]
\centering
\noindent\makebox[\linewidth][c]{%
  \includegraphics[width=190mm,trim=0 40bp 0 35bp,clip]{figures/fig3_3_attention_comparison.png}%
}
\caption{Comparison of (a) Softmax attention, (b) linear attention, (c) Agent Attention, and (d) the proposed SLFA module.}
\label{fig:3-3}
\end{figure}
```

中文回译（助手）：

(a)Softmax注意力、(b)线性注意力、(c)Agent Attention和(d)所提SLFA模块的比较。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_4_1.tex

源文件：source-zh/figures/figure_4_1.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.62\textwidth]{figures/fig4_n_agents_sensitivity.pdf}
\caption{Mean validation RMSE of MS-AgentNet with different numbers of agents.}
\label{fig:4-1}
\end{figure}
```

当前英文：

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.62\textwidth]{figures/fig4_n_agents_sensitivity.pdf}
\caption{Mean validation RMSE of MS-AgentNet with different numbers of agents.}
\label{fig:4-1}
\end{figure}
```

中文回译（助手）：

MS-AgentNet在不同智能体数量下的平均验证RMSE。此文件当前未被主稿引用，不作为本次正文新增实验。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_4_2.tex

源文件：source-zh/figures/figure_4_2.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\input{figures/comparison_panel_layout}
\begin{figure}[H]
\centering
\makebox[\textwidth][c]{%
\resizebox{168mm}{!}{%
\begin{minipage}{190mm}\centering
\ComparisonPanel{Cell2}{figures/Oxford/cell2.png}{0.81070}{1.20686}{61.19060}{62.44257}%
\hspace{2mm}%
\ComparisonPanel{Cell3}{figures/Oxford/cell3.png}{7.42167}{1.42048}{54.51697}{62.23012}%
\\[2mm]
\ComparisonPanel{Cell4}{figures/Oxford/cell4.png}{0.78767}{1.25316}{61.21331}{62.39783}%
\hspace{2mm}%
\ComparisonPanel{Cell5}{figures/Oxford/cell5.png}{7.42167}{1.43870}{54.51697}{62.11298}%
\hspace{2mm}%
\ComparisonPanel{Cell6}{figures/Oxford/cell6.png}{7.46109}{1.37455}{54.47471}{62.28000}%
\\[2mm]
\ComparisonPanel{Cell7}{figures/Oxford/cell7.png}{0.34932}{1.72202}{61.65166}{62.18773}%
\hspace{2mm}%
\ComparisonPanel{Cell8}{figures/Oxford/cell8.png}{7.42167}{1.42048}{54.51697}{62.26265}%
\end{minipage}%
}%
}
\caption{SOH estimation results of different models on the Oxford dataset.}
\label{fig:4-2}
\end{figure}
```

当前英文：

```latex
\input{figures/comparison_panel_layout}
\begin{figure}[H]
\centering
\makebox[\textwidth][c]{%
\resizebox{168mm}{!}{%
\begin{minipage}{190mm}\centering
\ComparisonPanel{Cell2}{figures/Oxford/cell2.png}{0.81070}{1.20686}{61.19060}{62.44257}%
\hspace{2mm}%
\ComparisonPanel{Cell3}{figures/Oxford/cell3.png}{7.42167}{1.42048}{54.51697}{62.23012}%
\\[2mm]
\ComparisonPanel{Cell4}{figures/Oxford/cell4.png}{0.78767}{1.25316}{61.21331}{62.39783}%
\hspace{2mm}%
\ComparisonPanel{Cell5}{figures/Oxford/cell5.png}{7.42167}{1.43870}{54.51697}{62.11298}%
\hspace{2mm}%
\ComparisonPanel{Cell6}{figures/Oxford/cell6.png}{7.46109}{1.37455}{54.47471}{62.28000}%
\\[2mm]
\ComparisonPanel{Cell7}{figures/Oxford/cell7.png}{0.34932}{1.72202}{61.65166}{62.18773}%
\hspace{2mm}%
\ComparisonPanel{Cell8}{figures/Oxford/cell8.png}{7.42167}{1.42048}{54.51697}{62.26265}%
\end{minipage}%
}%
}
\caption{SOH estimation results of different models on the Oxford dataset.}
\label{fig:4-2}
\end{figure}
```

中文回译（助手）：

不同模型在Oxford数据集上的SOH估计结果。子图标题顺序：Cell2、Cell3、Cell4、Cell5、Cell6、Cell7、Cell8。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_4_3.tex

源文件：source-zh/figures/figure_4_3.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\input{figures/comparison_panel_layout}
\begin{figure}[H]
\centering
\makebox[\textwidth][c]{%
\resizebox{168mm}{!}{%
\begin{minipage}{190mm}\centering
\ComparisonPanel{CS2\_37}{figures/CSCXMIT/CS-37.png}{0.55160}{1.49007}{61.51274}{63.49308}%
\hspace{2mm}%
\ComparisonPanel{CX2\_37}{figures/CSCXMIT/CX-37.png}{7.42564}{1.68784}{54.57534}{61.95926}%
\hspace{2mm}%
\ComparisonPanel{b3c13}{figures/CSCXMIT/b3c13.png}{7.42167}{1.67467}{54.51697}{61.87635}%
\\[2mm]
\ComparisonPanel{CS2\_38}{figures/CSCXMIT/CS-38.png}{1.57045}{1.72202}{60.39922}{62.35018}%
\hspace{2mm}%
\ComparisonPanel{CX2\_38}{figures/CSCXMIT/CX-38.png}{7.42564}{1.66587}{56.42270}{62.66466}%
\hspace{2mm}%
\ComparisonPanel{b3c29}{figures/CSCXMIT/b3c29.png}{7.42167}{1.81726}{54.51697}{61.82984}%
\end{minipage}%
}%
}
\caption{SOH estimation results of different models on the CALCE and MIT/Severson datasets.}
\label{fig:4-3}
\end{figure}
```

当前英文：

```latex
\input{figures/comparison_panel_layout}
\begin{figure}[H]
\centering
\makebox[\textwidth][c]{%
\resizebox{168mm}{!}{%
\begin{minipage}{190mm}\centering
\ComparisonPanel{CS2\_37}{figures/CSCXMIT/CS-37.png}{0.55160}{1.49007}{61.51274}{63.49308}%
\hspace{2mm}%
\ComparisonPanel{CX2\_37}{figures/CSCXMIT/CX-37.png}{7.42564}{1.68784}{54.57534}{61.95926}%
\hspace{2mm}%
\ComparisonPanel{b3c13}{figures/CSCXMIT/b3c13.png}{7.42167}{1.67467}{54.51697}{61.87635}%
\\[2mm]
\ComparisonPanel{CS2\_38}{figures/CSCXMIT/CS-38.png}{1.57045}{1.72202}{60.39922}{62.35018}%
\hspace{2mm}%
\ComparisonPanel{CX2\_38}{figures/CSCXMIT/CX-38.png}{7.42564}{1.66587}{56.42270}{62.66466}%
\hspace{2mm}%
\ComparisonPanel{b3c29}{figures/CSCXMIT/b3c29.png}{7.42167}{1.81726}{54.51697}{61.82984}%
\end{minipage}%
}%
}
\caption{SOH estimation results of different models on the CALCE and MIT/Severson datasets.}
\label{fig:4-3}
\end{figure}
```

中文回译（助手）：

不同模型在CALCE和MIT/Severson数据集上的SOH估计结果。子图标题顺序：CS2_37、CX2_37、b3c13、CS2_38、CX2_38、b3c29。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### figures/figure_4_4.tex

源文件：source-zh/figures/figure_4_4.tex。定位：文件第1行起；下面为完整文件快照。

源稿与工作稿文字完全相同。源稿中本来就是英文的内容保持英文。

原稿：

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.78\linewidth]{figures/fig4_storage_scaling.pdf}
\caption{Storage sizes of five models at different model widths: (a) storage size at each width; (b) overall distribution across the tested widths.}
\label{fig:4-4}
\end{figure}
```

当前英文：

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.78\linewidth]{figures/fig4_storage_scaling.pdf}
\caption{Storage sizes of five models at different model widths: (a) storage size at each width; (b) overall distribution across the tested widths.}
\label{fig:4-4}
\end{figure}
```

中文回译（助手）：

五种模型在不同模型宽度下的存储大小：(a)每种宽度下的存储大小；(b)全部被测宽度上的总体分布。

五项核对：

①可见文字未见漏译、增译或改变原意（源为英文处按原文保留）；②数值、标识、限定已对照；③未见需要强制修改的英语问题；④未见新增夸大或不必要复杂词；⑤按此图表的定义、协议和结果功能使用，未将本文专用细节冒称三篇范文原句。 图中文字的额外问题见图片审查附录。

### main.tex

源文件：source-zh/main.tex。定位：文件第1行起；下面为完整文件快照。

原稿与工作稿分别如下。

原稿：

```latex
\documentclass[UTF8,11pt]{ctexart}
\input{preamble}
\begin{document}
\section*{摘要}
\input{chapters/abstract}
\section{引言}
\input{chapters/chapter01}
\input{figures/figure_2_1}
\FloatBarrier
\section{方法基础与数据准备}
\input{chapters/chapter02}
\FloatBarrier
\section{所提出的MS-AgentNet模型}
\input{chapters/chapter03}
\FloatBarrier
\section{实验结果与分析}
\input{chapters/chapter04}
\FloatBarrier
\section{结论}
\input{chapters/chapter05}
\FloatBarrier
\input{backmatter/references}
\end{document}
```

当前英文：

```latex
\documentclass[UTF8,11pt]{ctexart}
\input{preamble}
\renewcommand{\refname}{References}
\begin{document}
\section*{Abstract}
\input{chapters/abstract}
\section{Introduction}
\input{chapters/chapter01}
\input{figures/figure_2_1}
\FloatBarrier
\section{Methodological framework and data preparation}
\input{chapters/chapter02}
\FloatBarrier
\section{The proposed MS-AgentNet model}
\input{chapters/chapter03}
\FloatBarrier
\section{Experimental results and analysis}
\input{chapters/chapter04}
\FloatBarrier
\section{Conclusion}
\input{chapters/chapter05}
\FloatBarrier
\input{backmatter/references}
\end{document}
```

中文回译（助手）：

摘要；引言；方法框架与数据准备；所提出的MS-AgentNet模型；实验结果与分析；结论；参考文献。源标题“方法基础与数据准备”回译为“方法框架与数据准备”，见T07。

五项核对：

①标题有“方法基础→方法框架”的轻微侧重变化，见T07；②章节次序与输入路径一致；③其余标题自然；④无增强结论；⑤标题按本章实际内容适配，不强求范文标题。 图中文字的额外问题见图片审查附录。

