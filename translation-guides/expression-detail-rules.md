# 词汇、句型与细节颗粒度执行细则

适用于 house-style.md 的逐段翻译与检查。本文规则与范文实际写法分开记录：原文证据见 reference-evidence.md；下列英文句型为改编模板，不是原句引用。

## 一、词义层级与固定搭配

| 层级/任务 | 本文优先用法 | 不可混同的含义 | 参考依据 |
| --- | --- | --- | --- |
| 观测量 | measure/record voltage, current, temperature | 测得的量与计算得到的 HI | JES §3.5.1 |
| 曲线计算 | derive a curve from measurements | derive 曲线，extract 特征 | JES §3.5.1 |
| 指标提取 | extract HIs from charging/discharging data | 提取与筛选两个步骤 | JES 摘要、§3.5.1 |
| 指标筛选 | retain candidates; rank HIs by [score]; remove redundant HIs | 准入、排序、去冗余分别表述 | JES §3.5.2 |
| 峰特征 | peak value; voltage corresponding to the peak | 峰高与峰位不可都写 peak feature | JES §3.5.1 |
| 电压区间 | charging time within [voltage interval] | 充电时长不是采样间隔；窗口说明电压/时间/循环维度 | JES 表4 |
| 特征相关 | correlation between HIs and SOH; linear association; monotonic relationship | PCC 与 SCC 的度量含义分开 | BMS §2.3；JES §3.5.2 |
| 输入映射 | embed/project/reshape/transpose [quantity] | 按实际操作选择，不统一写 process | BMS §3.1；JES §2.2.2 |
| 通道变化 | expand the channel dimension by a factor of [r] | 扩展倍数不是最终维数 | JES §2.2.2 |
| 串行运算 | depthwise filtering followed by pointwise combination | followed by 不用于并行分支 | BMS §3.2 |
| 依赖建模 | capture long-range dependencies | capture 描述表征功能，track 描述预测曲线跟踪 | BMS 摘要；EAI §4.1 |
| 信息保留 | preserve local details/information | preserve 与新增/融合特征不同 | EAI §4.2.1 |
| 融合后细化 | refine the fused representation; following the fusion stage | 明确模块位置，不泛称 improve features | EAI §4.2.2 |
| 轨迹现象 | abrupt SOH drops; capacity recovery/regeneration; late-life accelerated degradation | 采用本文确认术语；局部突降不自动等于 knee point | EAI §5.3–5.4；BMS §4.3.2 |
| 轨迹跟踪 | track/follow the degradation trajectory; capture the amplitude and timing | 幅度与时点均需图中证据；不自动解释物理恢复 | EAI §5.4 |
| 计算量 | FLOPs for a single forward pass | 单次前向计算量与累计训练 FLOPs 不同 | BMS §4.2.2；JES §4.4.2 |

### 全文不靠同义替换制造变化

- cell：具体实验电芯；battery：通用电池对象或沿用数据集正式名称。根据指代区分，不机械全部替换。
- HI：输入健康指标；feature/representation：网络内部特征或表示。不能把每个 hidden feature 都称 HI。
- error：具体误差指标；accuracy：总体精度概念。MAE 降低 x% 不写成 accuracy 提高 x%。
- computational complexity：理论规模关系；FLOPs：给定条件的运算量；latency：一次推理耗时；training time：训练耗时；parameter count 与 storage：数量与存储量。
- 主张动词按证据选：方法操作用 computes/aggregates/maps；设计目标用 is designed to；结果用 shows/indicates；设计对应用 is consistent with。不得对所有原句机械降级，也不得添加褒义副词。

## 二、五类结果段分别组织

| 段落任务 | 信息推进 | 必须明确 | 停止位置 |
| --- | --- | --- | --- |
| HI 对照 | 比较的输入组合→模型与协议固定条件→主要差异→必要代表结果 | 单指标、Fusion 的组成；其余条件是否相同 | 不把输入效果归给网络结构 |
| 退化轨迹 | 电池及现象→模型跟踪表现→对应指标→必要解释 | 曲线对象、比较模型、局部或整体范围 | 不由局部贴合直接宣布全域最优 |
| 模块消融 | 移除/替换项→不变条件→误差变化→组件或组合贡献 | replacement 与 removal 区分；完整组合基准 | 不以消融证明唯一机制 |
| 效率比较 | 输入与计量条件→具体资源结果→精度对应关系 | 参数、存储、FLOPs、时间各自口径 | 无硬件证据则止于资源结果与潜力 |
| 跨域适应 | 源/目标域及可用数据→source-only→适应后变化→剩余限制 | 样本比例含义、范围、R²等相关证据 | 不把使用目标域数据的改善称零样本泛化 |

## 三、方法细节放在哪里

- 模型总览：输入对象、必要维度、模块顺序和输出。各模块内部运算在对应小节展开。
- 新模块：输入及维度→实际操作顺序→核心公式→新符号/约束→输出作用。实际需要时可合并，不要求固定五句话。
- HI 搜索：候选范围、组级评分、选优、尺度调整、终止与固定规则均保留。只展示最终窗口不足以说明本文方法。
- 准入和冗余：and/or、绝对值、大小于/等于、选谁保留、应用顺序按本文原式逐项核对，不从范文借阈值逻辑。
- 正文承载为何及如何；参数表承载成组配置；同一配置只完整介绍一次，后续明确引用。公式附近只解释新符号和需要澄清的条件。

## 四、数字句必须说清什么

按句子功能补齐对象、指标、单位/尺度、统计范围；比较句再补比较对象。必要信息可由前句清晰继承，不强求每句全部重复。

- `RMSE decreased from [a] to [b].`：报告起点与终点。
- `RMSE decreased by [x]%.`：相对降幅，分母为比较基准。
- `RMSE decreased to [b].`：终值，不可写成降幅。
- `on Cell2`：单电池；`across Cell2–Cell8`：范围；`macro-average`：明示按哪些电池及什么权重汇总。
- 百分比 SOH、归一化 SOH、百分比误差、百分点遵循本文单位，不能为了语言统一而换尺度。
- 原值、降低率和排名若传递同一信息，不新增三重复述。中文已有实质重复时提案处理，不在英译中静默删除。

## 五、正文、表格、图注的职责

- 表格：完整比较值、单位、角色星号及必要脚注。
- 图注：数据集/电池、子图对应、曲线或符号说明、局部放大含义及读图必需条件。
- 正文：提出由图表支持的判断、选取关键证据并说明含义。图表首次定位后直接增加观察，不连续用 As shown in 重启同一信息。

## 六、语法与段落连接

- 首句明确段落对象及任务；中间增加操作、证据或条件；结尾给实际结果或进入下一步，避免重复开头。
- `this result` 必须有唯一可识别的前文结果；有多个结果时明确写 `the reduction in RMSE` 等具体指代。
- 采用并列动词表达同级操作，如 extracts, selects, and feeds；不要把过程、目的与结论放成不对称列表。
- 参数选择常用过去时；模块定义/公式常用现在时；`Table X reports ...` 用现在时。按功能保持一致。
- `compared with` 连接同类量；`between A and B` 用于相关关系；`across cells` 描述分布范围；`on a dataset/cell` 描述实验对象。
- 直接陈述不等于全用主动语态。操作对象比执行者重要时，被动语态自然且可保留。

## 七、每批具体验收表

记录：中文段落位置、段落任务、对应范文小节、本批关键搭配、保留的协议/数字/解释细节、实际发现的问题。检查未发现问题即可通过；不得为显得认真而新增防御句。

所有限制分三类：必要条件必须保留；真实反例直接报告；预防假想质疑的自证不新增。风格规则冲突时优先保留技术原意，并将实质修改列为提案。
