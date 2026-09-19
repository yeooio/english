# 本轮范文句式提炼与本文映射

日期：2026-09-14。配套 `grammar-full-review-2026-09-14.md`。本轮重新阅读原TXT，并目测三篇PDF第1页；这里记录可复核的句子分析和适配规则，不批准论文改写。

## 1. 实测范围与方法

仅统计三篇**完整摘要**，不是全文统计。按原PDF确认句序和句界；去除版面换行、软连字符，将跨行的Local–Global接回，修复BMS TXT的state-ofthe-art提取粘连。按空格计词，连字符词、缩写、数字各计一个词；这是一致的操作性计数，不是通用词数标准。

| 范文及范围 | 句数 | 总词数 | 最短/中位/最长句词数 |
|---|---:|---:|---|
| Engineering-AI，PDF p.1 Abstract，TXT 34–48行 | 6 | 191 | 19 / 34.5 / 42 |
| BMSFormer，PDF p.1 Abstract，TXT 30–40行 | 7 | 147 | 15 / 24 / 25 |
| JESSOHRUL，PDF p.1 Abstract，TXT 33–50行 | 8 | 241 | 16 / 29.5 / 50 |

这些数值说明三篇句长不同，不能规定本文每句最多20词，也不能按范文句数删减本文信息。完整英文句子不在此重复抄录；S编号按各篇摘要的原句序。

## 2. 逐句功能、主语与时态语态

### Engineering-AI

| 句 | 词数 | 功能 | 主句主语及谓语形式 | 与前句的连接 |
|---|---:|---|---|---|
| E1 | 32 | 问题引入与研究目标（混合） | this paper；presents，现在时主动 | 目的状语引出框架 |
| E2 | 19 | 方法：HI筛选 | a systematic feature selection process；identifies，现在时主动 | First，先输入端 |
| E3 | 21 | 方法：网络设计 | we；propose，现在时主动 | Subsequently，由指标到网络 |
| E4 | 37 | 方法及设计作用 | this AI model；achieves，现在时主动 | By integrating，说明前述网络怎样工作 |
| E5 | 40 | 实验结果 | Experiments；demonstrate，现在时主动 | 转到数据验证与MAE |
| E6 | 42 | 硬件结果与部署解释（混合） | the AI framework；proves，现在时主动 | With，连接规模与硬件证据 |

方法段E2–E4为3/6句、77/191词（40.3%）；纯结果E5为1/6句、40/191词（20.9%）；结果与解释混合E6另列为1/6句、42/191词（22.0%），不重复计入纯结果。E1另列。E4的作用属于设计说明，不另算独立实验结果。

可学：先指标、后网络，以具体对象加动作动词推进。不可照搬：proves、硬件部署已完成的力度，以及本稿没有的模块和实验。

### BMSFormer

| 句 | 词数 | 功能 | 主句主语及谓语形式 | 与前句的连接 |
|---|---:|---|---|---|
| B1 | 24 | 背景 | SOH estimation；is，现在时系表 | 估计任务及应用需求 |
| B2 | 15 | 现有方法不足 | approaches；rely，现在时主动 | However |
| B3 | 15 | 研究目标/提出模型 | an efficient deep learning model；is constructed，现在时被动 | In this paper |
| B4 | 24 | 方法：局部—全局注意力 | BMSFormer；integrates，现在时主动 | 模型专名直接承接 |
| B5 | 24 | 方法：卷积补充 | two kinds of depthwise separable convolution；are embedded，现在时被动 | Additionally |
| B6 | 20 | 验证方法 | Three widely used battery datasets；are employed，现在时被动 | 从设计转入评价范围 |
| B7 | 25 | 实验结果 | 原文The experiments results；illustrate，现在时主动 | 承接实验，归纳结果 |

方法及验证B4–B6为3/7句、68/147词（46.3%）；结果B7为1/7句、25/147词（17.0%）。B3单列研究提出。主被动交替并未破坏连贯性；B7的名词搭配不宜继承，本文已有experimental results正确。

### JESSOHRUL

| 句 | 词数 | 功能 | 主句主语及谓语形式 | 与前句的连接 |
|---|---:|---|---|---|
| J1 | 28 | 背景 | Accurate assessment；is，现在时系表 | 任务及安全需求 |
| J2 | 19 | 研究背景/趋势 | Recent studies；have emphasized，现在完成时主动 | 对已有趋势补充 |
| J3 | 18 | 方法不足 | methods；rely / stack，现在时主动 | However |
| J4 | 16 | 研究目标 | this paper；proposes，现在时主动 | Therefore |
| J5 | 31 | 方法及设计作用 | It；introduces，现在时主动 | It明确承接框架 |
| J6 | 41 | 方法：指标提取与筛选 | methods / algorithm；are applied / is proposed，现在时被动 | Furthermore，转到输入设计 |
| J7 | 38 | 验证方法 | comparative experiments；were conducted，过去时被动 | Finally |
| J8 | 50 | 实验结果与意义（混合） | The experimental results；demonstrate，现在时主动 | 承接验证；结果后附应用意义 |

方法及验证J5–J7为3/8句、110/241词（45.6%）；结果与意义混合J8另列1/8句、50/241词（20.7%），未拆成互斥的结果/意义词数。J4单列研究提出。**were conducted后接现在时结果**直接支持保留本文We compared后接results show。

## 3. 可以适配到本文的句型

以下均为**改编模板或本文建议句**，不是范文原句。只借句法，不借实验事实，不把全文改成相同句型。

| 功能 | 本轮观察依据 | 本文中的适配及决定 |
|---|---|---|
| 提出框架 | E1、B3、J4均直接提出研究对象，主动/被动均可 | 本文摘要 `Therefore, this paper proposes a lightweight SOH estimation framework.` 已自然，保留。 |
| HI步骤 | E2把筛选过程作为主语；J6把提取与筛选分清 | 改编：`The algorithm selects HIs that are robust across cells and reduces feature redundancy.` 仅作将算法设为明确主语的可选句型；须保留原段首次提出算法全称的功能。 |
| 局部与全局作用 | E4、B4、J5均采用“模块/模型—操作—作用” | 本文现有 `A Slim Local-Global Fusion Attention (SLFA) module combines ...` 已符合；不借BMS的mainly或范文模块名换掉本文定义。 |
| 已完成的验证 | E5用现在时；B6用现在时被动；J7用过去时被动 | 本文 `We compared ...` 保留。三篇没有同一种强制时态规范。 |
| 实验结果 | E5、B7、J8均以实验/结果为主语接现在时 | 本文 `The experimental results show ...` 保留；保留better overall而非套用superior等更强表达。 |
| 限制与未来方向 | EAI §7 PDF pp.20–21；BMS §5 p.14；JES §5 pp.24–25，本轮均重新读对应结论TXT，目测关键PDF页 | 本文 `Future work will focus on ...` 已自然。无需为模仿而改成aims或增加部署完成主张。 |

## 4. 三篇尺度校准

三篇都存在目的状语、关系从句、名词化结构、分词补充和概括性结尾。因此，它们不是本文的禁用句式。本文只有在某处主干更迟、指代需回找、同级动作不平行时才考虑最小修复。减少中文式冗余的标准是更直接且不丢事实，不是减少连接词或只保留短句。

摘要目前已沿用相近的功能顺序和常见搭配，没有必要整段再套写。正文候选及图内明确问题见本轮主报告和两份独立报告。
