# 已批准语言修订 — 2026-09-13

作者选定四类语言问题，共修改六处。完整中文与修改后英文段落见 full-manuscript-bilingual.md：chapter01:40、chapter02:29/33、chapter04:109/172、chapter05:3。

## 1

原表达：These approaches increase model parameters and computational operations.

现表达：These approaches increase the number of model parameters and computational operations.

## 2

原表达：Cycling aging records from all 8 cells,

现表达：Aging records from cycling tests on all 8 cells,

## 3

原表达：Cycling aging records from 6 cells,

现表达：Aging records from cycling tests on 6 cells,

## 4

原表达：Averaged over the six cells, MS-AgentNet achieves an $R^2$ of 0.9896 and MAE, MAPE, and RMSE

现表达：Across the six cells, MS-AgentNet achieves an average $R^2$ of 0.9896 and average MAE, MAPE, and RMSE

## 5

原表达：lower than the closest model, Transformer, at the same dimension

现表达：lower than that of Transformer, the closest model, at the same dimension

## 6

原表达：Specifically, averaged over two cells in the CALCE CX2 dataset, MS-AgentNet reduces MAPE by 52.69\% compared with CNN-Transformer.

现表达：Specifically, the average MAPE of MS-AgentNet over the two cells in the CALCE CX2 dataset is 52.69\% lower than that of CNN-Transformer.

## 用词依据与验证

BMSFormer full.txt:1367：total number of trainable parameters（可训练参数总数）；Engineering-AI full.txt:2821：a parameter count（参数量）；JESSOHRUL results.txt:98：average MAE and MAPE（平均MAE和MAPE）。中文为助手释义。复用数量与平均指标搭配，不借用范文实验结论。Aging records from cycling tests on、lower than that of 是本文语法适配，不冒充范文原句。

六处中英对照已同步；数字、公式、引用、段落边界未改。XeLaTeX/latexmk编译通过，37页；第5、7、26、31、32页已重新渲染目视检查，无新增遮挡或溢出；日志无溢出、未定义引用或缺字提示。原有图片ICC警告仍在。图7和协议表未修改。

