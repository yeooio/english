# 第二章句式、动词与形容词审校 — 2026-09-16

状态：只读审校，未修改论文。按作者最新指示从第二章开始，第一章已完成，不再检查或推进此前第一章提案。

## 总体结论

已读取当前第二章及对应完整中文，按2.1、2.2、2.3总述、2.3.1、2.3.2、2.3.3逐段核对。建议1处最小句式修改；另有1处轻度可选动作化改写。未发现需要批量替换的动词或形容词，也不要求每句复刻范文。专业术语沿用已确认版本，B类及已知图内命名不重开。

本轮由主代理检查框架、数据集和总述，两名agent分别检查HI提取和窗口/指标筛选；主代理复核建议及对应范文。它是章节内分工审校，不是三人独立各读一遍全部材料。

## 本批范文依据与尺度

- BMS：methodology.txt:19–35、46–76（SOH、框架四步）、192–216、238–247（数据集及协议）；HI搜索相应full.txt:441–458、503–520。
- JE：methodology.txt:1109–1115（完整数据集总述）；full.txt:322–334（框架流程的可辨认连续句群）、1575–1590（HI与IC定义）、1667–1681、1773–1797、1799–1813、1822–1850、1874–1882（指标、相关性和选择）。另核对Oxford/CALCE数据介绍相应完整语境。
- SL：methodology.txt:35–48及数据集条目、SOH定义；full.txt:284–307、327–367、372–421（积分与特征标定/固定）。三篇按功能交叉使用。

范文同样采用被动句、目的前置、多个指标列表和较长限定，不能仅因本文有这些形式就要求改短。相比之下，是否明确“谁做什么”、是否保持中文范围，才决定修改价值。

数据集介绍样本的句级测量存于 `build/ch2-style-reference-sentence-check-20260916.json`：BMS Oxford完整段3句/102词，SL数据集总述2句/27词，JE数据集总述3句/56词；按空白分词、人工句界、去引文和版面断词计数。这些样本均为实验数据/方法介绍，没有结果句；记录逐句主语、时态/语态，不作为本文句数配额。范文中的不自然语法与过强评价（如authoritative、performance superiority）不要求本文继承。

## C2-S1：求导句让操作直接作主语——建议修改

位置：chapters/chapter02.tex:60，IC段第三句。

现有英文：
> By differentiating capacity with respect to voltage, it converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}.

建议英文：
> Differentiating capacity with respect to voltage converts relatively flat charging voltage plateaus into more distinct peaks whose positions and shapes change with battery aging\cite{ref50,ref64}.

类型：词汇简单但主语指代稍绕。前句主语为IC curve，it字面上让曲线执行求导；改用求导操作作主语，直接说明“什么将平台转化为峰”。现句可理解，不将其夸大为技术公式错误。

范文依据：JE full.txt:1584–1589先说明IC analysis，再用“曲线通过求导获得”明确运算与曲线的关系；SL284–307由methods执行计算；BMS的提取步骤也以明确操作/步骤推进。三篇允许By开头，本项只调整这个具体it指代，不禁止某一种句型。

中文原文：“该方法对容量关于电压求导，将平缓的充电电压平台转化为辨识度更高的特征峰，其位置与形状会随电池老化发生变化。”

回译核对：对容量关于电压求导，将相对平缓的充电电压平台转化为更明显的特征峰，峰位与形状随老化变化。保留操作、对象、比较限定、老化关系及引用；不改段落、不增删技术事实。

## C2-S2：固定后应用改为直接动作——可选，保留也可以

位置：chapters/chapter02.tex:160，第二句。

现有英文：
> Once the indicators are determined, their definitions and calculation parameters remain fixed and are directly applied to feature extraction for other cells within the same dataset.

可选英文：
> Once the indicators are determined, their definitions and calculation parameters remain fixed and are used directly to extract features from other cells within the same dataset.

类型：轻度动作化。applied to feature extraction for变成used directly to extract features from，减少名词和介词叠加，保持“定义/参数不变、直接用于同数据集其他电池”的范围。

范文尺度：JE full.txt:1874–1882自己就使用fixed and directly applied for feature extraction，因此原句已经有范文同类依据，不能报为错误；SL372–421可参考固定后明确陈述提取动作的表达路径。若只修改收益明显的地方，本项保留即可。

## 逐小节保留记录

| 小节 | 句式、动词、形容词及力度核对 | 结论 |
|---|---|---|
| 2.1框架概述 | is calculated/denote/shown、constructs/determines、used to segment/paired with、fed into/learned、applied/compare/analyze/examine；明确先后步骤。范文也用被动操作陈述，不需全改we。 | 保留 |
| 2.2数据集 | provided/contains、conducted、charged/discharged、followed by/after reaching；数据集总述与JE的选择—差异—表图顺序相近。considerably对应中文“明显差异”，approximately对应“约”。 | 保留；不为像范文加入authoritative或优越性主张 |
| 2.3总述 | presents、builds、optimizes、calibrates、used for描述方法链；长算法名为已确认术语。 | 保留 |
| 2.3.1提取 | records/shifts、reflects、maps、smoothed、extracted/defined均有具体对象；well-established对应经典分析手段，relatively/more保留中文比较含义；DTV的By calculating主语确为this method。 | 仅建议C2-S1，其余保留 |
| 2.3.2窗口搜索 | reflect/depends、proposes、measures、calculated、uses/searches/refines、exceeds/retained；R1/R2/R3与条件顺序直接。preventing/allowing对应中文可避免/使，不另加ensure或guarantee。 | 保留 |
| 2.3.3指标筛选 | show/indicate、decrease/maintain、retains/ranked/removed、remain fixed；相关差异与选择动作按中文推进。JE也有抽象鲁棒性论证，不将名词结构本身判错；same dataset/reported values/corresponding cells是必要边界。 | C2-S2仅可选，其余保留 |

明示保留：数据集段落的过去时实验动作和现在时数据属性可以并存；is defined as与is expressed as分别按定义/表达功能使用，无须机械统一；high/strong相关性有系数与原文支撑；通常、可以、相对、约等限定不删除或加强。

子审查记录：`build/ch2-style-hi-20260916.md`、`build/ch2-style-selection-20260916.md`。作者确认前不写入论文；本轮无需编译，因为没有改动LaTeX文件。


## 作者补充要求后的词汇复核

作者强调：2.1、2.2也要检查是否学到范文专有词汇和惯用搭配；2.3仔细对照JE。本轮再次读取三篇对应方法、数据集及JE筛选完整语境，结果如下。不是只判断语法通顺。

| 本文位置/功能 | 当前已使用的词或搭配 | 范文可定位依据 | 判断 |
|---|---|---|---|
| 2.1 数据获取 | Data acquisition | BMS methodology.txt:46–50 | 已复用流程名；不照搬其自行进行全生命周期实验的事实 |
| 2.1 特征工程 | Systematic feature engineering | SL methodology.txt:35–37 | 已复用；具体算法保持本文定义 |
| 2.1 划窗与标签 | sliding window、HI time series、label、next cycle | BMS methodology.txt:51–59 | 相同功能表达；next cycle对应本文下一循环标签 |
| 2.1 训练与评价 | Model training、Performance evaluation、fed into、directly applied、compare | BMS methodology.txt:60–76；SL:38–43；JE full.txt:322–334 | 已学到具体动作与步骤名；training/configuration-selection cell边界属于本文，不改成范文30/70划分 |
| 2.2 数据集用途 | generalization capability、operating conditions | SL methodology.txt:44–48；BMS:203–216；JE:1109–1115 | 已有范文同功能词；不加performance superiority、authoritative等原文没有的评价 |
| 2.2 数据集引介 | is provided by、contains aging data、main characteristics are summarized | BMS methodology.txt:238–247及203–216；JE:1109–1119 | 已复用数据集主体—来源/内容—表图的写法 |
| 2.2 电池与材料 | pouch/prismatic/cylindrical cells、nominal capacity、cathode/anode、blend | BMS methodology.txt:192–200、238–247；SL数据集条目；JE Oxford段 | 已对齐，额定/标称保持中文区别 |
| 2.2 实验协议 | aging tests、room temperature、constant-current--constant-voltage、dynamic current profile、cutoff voltage | BMS methodology.txt:192–200、238–247；SL Oxford段 | 操作动词charged/discharged/followed by及数值限定自然；不同充放电协议不能照搬 |
| 2.3 曲线与HI | characteristic curves、extract、defined as、listed in | JE full.txt:1575–1589 | 先给来源与曲线，再给HI及表格的推进已相近 |
| 2.3 曲线变化 | records、changes、peak value、voltage corresponding to the peak | JE full.txt:1684–1696、1799–1811 | 已复用技术对象和明确动作；新增半峰宽等保留本文定义 |
| 2.3 平滑 | smoothed using a moving average、window size | JE full.txt:1667–1670、1799–1802 | 同操作；不必改成范文更长的a smoothing process is applied |
| 2.3 PCC/SCC | calculated、linear correlation、monotonic relationship | JE full.txt:1671–1680 | 核心搭配已对齐；不要求每句都复制范文语序 |
| 2.3 相关性显示 | correlation strength、circle size and color intensity、Larger, darker circles indicate | JE full.txt:1773–1784 | 同图示功能、直接动作结构已复用 |
| 2.3 筛选操作 | retains、ranked by correlation strength、removed、reduce redundancy、preserving feature diversity | JE full.txt:1822–1841 | 先筛、再排序、再去冗余的表达链已一致；不借范文阈值改变本文算法 |
| 2.3 固定与评价隔离 | remain fixed、feature extraction、HI reselection | JE full.txt:1874–1882 | 已学到对应写法；只保留本文同数据集范围，不引入JE的unseen battery groups |

结论：2.1/2.2不是“没问题所以未对照”，它们已有上述范文词汇与句式对应。2.3已按JE从曲线—HI—相关性—排序/去冗余—固定后应用的完整功能链复核。无需为表现模仿而新增同义替换。C2-S1仍是本章最有价值的最小句式提案；C2-S2仍可选，不升级为错误。本次补查未新增论文改动。


## 作者确认及补充复查后的实施

作者确认“这个建议可以作为改正”，随后要求agent再检查是否还有遗漏。两名agent分别独立通读第二章，交换此前主审重点：一名重点2.1/2.2的主体、动作和形容词力度，另一名重点2.3.1及全章指代与抽象表达；均未读取对方本轮结论。主代理核对后没有新增值得修改的候选。记录见build/ch2-extra-hi-20260916.md和build/ch2-extra-model-20260916.md，定位以当前句子文本为准。

仅实施已批准C2-S1：By differentiating capacity with respect to voltage, it converts → Differentiating capacity with respect to voltage converts。正文1处、中英对照英文1处；C2-S2可选项未改。两文件精确允许差异比对通过，中文对照和中文源稿不变，第一章未改。

备份与验证：build/ch2-approved-s1-20260916-161300/。编译成功，当前PDF36页；第9页重新渲染查看，未见修改引入的裁切/重叠。最终日志无未定义引用、缺字或溢出提示；原ICC图片警告保留。本轮保护检查发现backmatter/references.tex在期间发生并发变化，本任务未写该文件，也未回滚；其余121个受保护文件哈希不变。不能把本轮编译页数相对旧轮次的变化归因于这一个短语替换。
