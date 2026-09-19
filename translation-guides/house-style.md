# 本文英文表达与细节颗粒度统一规范

状态：依据作者指定三篇范文、三名独立 agent 的只读分析整合的执行规范 v2。尚未核准的术语仍按 terminology.md 标记为候选；本规范不代表译稿已经通过作者确认，也不代表所有高水平期刊共有唯一写法。短原文及来源见 reference-evidence.md，具体操作规则见 expression-detail-rules.md。两文件与本规范共同构成本项目的英文风格基准。

## 1. 采用的写作基准

保留中文稿的章节、段落任务、论证顺序和证据强度。按作者明确的功能分工：Engineering-AI 为轻量化、资源约束和精度—资源开销权衡的主参考；BMSFormer 为局部—全局融合、模块数据流与高效建模的主参考；JESSOHRUL 为多源 HI、相关性筛选及相关实验表达的主参考。三篇不设全局高低排序；遇到差异，按当前段落功能和本文技术含义选择并固定，不投票取词。高效与轻量化相关但含义不同，不将 efficient 和 lightweight 当作换词选项。

学习对象分为四层：领域术语、动词搭配、句子功能、段落信息量。只写“像顶刊”不能作为译稿验收结论。

作者补充（2026-09-15）：逐批比对还要落实到范文的表达风格，而不只是可复用词。对照同功能完整语境，观察核心对象何时出现、动词如何直接接工作或结论、逗号/从句怎样安排停顿、相邻句怎样由问题推进到动作和效果、用词力度怎样对应证据。建议句必须同时通过自然英语与中文回译检查；技术原意、证据边界、已定术语和段落论证顺序优先于外形相似。范文使用短句或逗号时可学习其作用，不机械复制句数、标点或整句。

## 2. 各位置写到哪里、在哪里停止

| 位置 | 应保留的具体信息 | 通常不展开 | 结束时读者应知道什么 |
| --- | --- | --- | --- |
| 摘要 | 应用需求；HI 稳定性与计算开销；两项设计及作用；验证范围；代表性精度与规模结果 | 电池编号、阈值、搜索网格、完整模型名单、全部提升率 | 解决什么、怎样解决、主要证据 |
| 引言背景 | SOH 的用途、直接测量的具体限制、间接估计的必要性 | 电池百科、与本文无关的安全背景 | 为什么值得研究 |
| 引言文献段 | 同类方法解决的共同问题；必要的代表文献；与本文相关的剩余限制 | 对每篇文献重复模型定义、数据和全部精度 | 缺口如何导向本文设计 |
| 贡献条目 | 设计对象、关键操作、回应的缺口；原稿已有的必要量化信息 | 完整实验步骤、选择合理性辩护、重复摘要数字 | 每项贡献的不同作用 |
| 数据介绍 | 影响 HI 或模型解释的化学体系、充放电协议、采样与退化特点；具体参数由表承载 | 对数据表逐项复述、无关机构背景 | 数据为什么具有差异 |
| HI 方法 | 观测量、候选窗口、组级目标、PCC/SCC 准入、冗余约束、规则固定及应用范围 | 无关候选特征逐项解释、标准相关系数的长篇教学 | 指标怎样产生、哪些数据用于确定规则 |
| 模型总览 | 输入及必要维度、窗口处理、DSConv-S→RAA→DSConv-L 的实际数据流、输出 | 每层基础知识和每次转置的重复说明 | 信息按什么路径变成 SOH |
| 模块段落 | 模块作用、必要操作、核心公式、新符号及约束；必要的计算顺序 | 把公式每个符号再译成一句、未经实验支持的物理解释 | 模块具体如何实现其作用 |
| 实验协议 | 训练与配置电池、主对比报告范围、输入规模、配置确定方式、影响复现的训练及测量条件 | 反复称赞公平严谨、对所有未采用方案作解释 | 如何复现并理解比较范围 |
| 主对比结果 | 与该段任务相关的趋势或轨迹差异、关键误差及比较对象、表图定位 | 全部模型×电池×指标逐项排名；同一差异反复报原值及降低率 | 整体表现及代表性差异 |
| 消融 | 移除或替换什么、哪些条件不变、主要结果及组合收益 | 每段重讲全部模块功能、宣称消融证明唯一机制 | 哪项设计对结果有何贡献 |
| 复杂度 | 输入条件、计算口径、参数/FLOPs/存储的代表结果、实际支持的权衡 | 从参数少推断延迟最低；缺少硬件实验时谈部署完成 | 精度对应怎样的资源代价 |
| 跨域结果 | 迁移方向、目标域可用数据、source-only 与适应后结果、剩余误差 | 将适应称为零样本泛化、为负 R² 长篇辩护 | 适应改善多少、仍受什么限制 |
| 结论 | 问题、输入和模型设计、主要证据、边界与未来方向 | 公式、所有超参数、正文未建立的新结论 | 研究贡献与适用范围 |

表内“通常不展开”用于指导英文表达，不授权删去中文原稿已有的必要内容。若需要实质压缩或重排，单列建议等待确认。

## 3. 数字与解释的选择规则

- 为段落核心判断选证据，不按表格顺序翻出所有数字。具体保留多少由判断需要决定，不设机械数量上限。
- 提升率必须说明指标、比较对象与统计范围；不把百分比和百分点混用。
- 同一对比通常选择原始值或相对变化作为主体。二者同时出现须各有功能。
- 总体主张由总体证据支撑，单颗电池的最佳值不能代替宏平均。
- 协议条件在首次需要处完整说明，后文采用明确指代；不为减少篇幅删除会改变比较含义的条件。
- 解释依次到“观察到的现象→结果含义→有依据的设计对应”为止。硬件、物理机制和因果结论需要本文对应证据。

## 4. 术语与常用动词搭配

以下是本文推荐搭配，不是对三篇论文所作的词频排名。模型/模块专名以已确认术语表为准。

| 表达任务 | 优先搭配 | 含义限制 |
| --- | --- | --- |
| 健康估计 | estimate SOH; SOH estimation | 不为避免重复随意换成其他任务名称 |
| 指标构建 | extract health indicators; select indicators; construct an indicator | extract、select、construct 对应不同步骤 |
| 相关性 | assess the correlation between … and …; strongly correlated with … | 不把相关性写成因果性 |
| 窗口 | select a voltage interval; calibrate the observation window | 不是梯度学习时不随意称 learnable |
| 局部特征 | capture local variations; preserve local information | capture 与 preserve 按操作含义区分 |
| 长期信息 | capture long-range dependencies; track degradation trends | 依赖建模与输出轨迹跟踪不能混用 |
| 信息融合 | fuse features; aggregate information; refine the fused representation | 明确融合、聚合和后续细化的对象 |
| 资源代价 | reduce computational complexity; reduce parameter count; require less storage | 复杂度、参数、存储和耗时分别表述 |
| 结果 | achieve a lower MAE; reduce RMSE; maintain low errors | 指明范围；不把 lower 强化成最低 |
| 比较 | compared with; relative to; across the reported cells | 区分比较对象、比率基准和汇总范围 |
| 泛化适应 | cross-cell generalization; cross-dataset transfer; few-shot adaptation | 按本文协议分别使用 |

句法约定：默认用明确主语及动作动词；方法描述通常用现在时，已完成实验操作通常用过去时，图表呈现用现在时。保持同功能语句一致，不机械全篇统一成一种时态。首次定义缩写，此后稳定使用。技术词允许重复，普通动词无需故意变复杂。

## 5. 按功能使用句型

以下为改编模板，不是范文整句引文。方括号内容只填本文事实。

- 方法：`The framework combines [input design] with [model design] to [objective].`
- 数据流：`The input is first [operation] and then passed to [module].`
- 模块：`[Module] aggregates [information] through [operation].`
- 公式：`Here, [symbol] denotes [quantity].` 只定义首次出现且必要的符号。
- 协议：`[Cell] was used for training, and [cell] was used for configuration selection.`
- 表图：`Table [x] summarizes [results] across [scope].` 后句增加判断，不再换词复述表题。
- 结果：`The model achieved an RMSE of [value] on [cell].`
- 轨迹：`On [cell], the estimates closely follow [observed degradation pattern].`
- 消融：`Removing [module] increased [metric] from [a] to [b].`
- 解释：`This result is consistent with [specific design objective].` 仅在确有解释价值时使用。
- 边界：`Source-only evaluation yielded [result], indicating limited transfer under [conditions].`

## 6. 正向陈述与必要限定

正向陈述指直接交代事实、方法、结果，也包括直接报告失败和边界；并非只写有利结果。

| 不必要的写法 | 本文采用的写法 |
| --- | --- |
| 为保证实验公平严谨，我们严格…… | 直接写训练、配置与测试范围 |
| 本模块不是简单堆叠，而是…… | 直接写模块分工和实际数据流 |
| 尽管某指标非最优，这不影响有效性…… | 直接写该电池结果及相应总体结果 |
| 为进一步证明有效性和合理性…… | 直接写消融操作与比较目的 |
| 与设计一致，但不据此宣称唯一因果关系 | 正文写审慎的设计对应；因果强度检查留在审核中 |

however、although、unlike 并非禁词：只有存在真实且必要的转折才用。避免在每段开头套用。保留条件、否定、统计不确定性和适用边界，不为追求正向语气改变事实。

## 7. 范文依据及拒绝继承项

- BMSFormer 摘要（PDF p.1）：将注意力与 DSConv 各自的操作和作用直接连在一起；不展开配置协议。
- BMSFormer §3.1（PDF p.6）：按 HI 输入、窗口、嵌入、模块、输出推进。本文保留这种数据流表达，不继承冗长转置复述。
- BMSFormer §4.2：表图承载模型结果，正文分析跨电池表现；效率实验保留统一输入与训练配置。不能据此省略本文必要的配置电池身份。
- JESSOHRUL §3.5.2（PDF p.13 起）：区分 PCC 与 SCC 的作用并进入筛选规则；本文深入自己的准入与冗余约束，不扩写统计教材。
- Engineering-AI §4.2.2（PDF p.8）：明确大核模块位于融合之后，说明其作用；本文采用相应功能表述，不照搬其核尺寸。
- Engineering-AI §5.3–5.4：用突降、恢复及非线性退化组织结果；其中对基线滞后原因的解释，不自动视为本文已验证机制。
- 三篇结论分别收束其设计与证据。JESSOHRUL 的 RUL 和 Engineering-AI 的 MCU 验证不能迁移为本文结论。
- 范文可见 `The experiments results`、`the precise of` 等不规范表达；分别按语义写为 `The experimental results`、`the accuracy of`。风格一致不要求复制语法错误。

## 8. 每批验收

检查六项：技术含义一致；术语和搭配准确；段落单向推进；协议/数字/解释颗粒度匹配；无额外防御或证据越界；英语语法和衔接自然。记录具体问题；无问题时保留，不反复换词润色。满足规则后仍按 workflow.md 展示双语建议并等待相应正文授权。
