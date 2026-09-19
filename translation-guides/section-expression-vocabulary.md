# 摘要及第二至第五章：英文词与搭配索引

日期：2026-09-13。按作者最新澄清，本轮**只整理颗粒度词**：各章可借用的英文词、短搭配、所指对象和容易混用的细节。不提供章节重排、删减、补数字或正文改写方案。

主审与三个agent分别核对中文对应部分及三篇参考的对应内容，下面记录可定位短语。共59处按章索引，包含已有术语复用，不等于59个新增或全部已冻结译名。核心译名仍以[术语表](terminology.md)为准；本文件是原词证据和使用入口，不建立同义词轮换库。

出处BMS/EAI/JES对应 `style-references/BMSFormer/full.txt`、`Engineering-AI/full.txt`、`JESSOHRUL/full.txt`；L是TXT行号，不是PDF页码。短语已回查，大小写、正常单复数与排版软连字符可规范化；整句仍须按中文实际含义组织。

## 摘要

| 中文对象或动作 | 范文原词/短搭配 | 出处 | 使用细节 |
| --- | --- | --- | --- |
| 多尺度与多通道特征 | `multi-scale and multi-channel features` | BMS L35 | 对应两种特征属性，不把multi-scale与multi-channel当同义词 |
| 不同化学体系与运行条件 | `different chemistries and operating conditions` | BMS L37 | 化学体系与工况是两个维度 |
| 系统性特征筛选 | `systematic feature selection` | EAI L36 | 普通筛选描述，不能替代本文组级协议名称 |
| 计算资源需求 | `computational resource requirements` | JES L40 | 只描述资源需求，不等于已测推理延迟 |

## 第二章

| 中文对象或动作 | 范文原词/短搭配 | 出处 | 使用细节 |
| --- | --- | --- | --- |
| 数据采集 | `Data acquisition` | BMS L269 | 用于流程阶段 |
| 特征工程 | `Feature engineering` | BMS L275 | 上位概念，包含提取与筛选但不混称 |
| 模型训练 | `Model training` | BMS L284 | 区别配置选择与模型评价 |
| 模型评价 | `Model evaluation` | BMS L294 | 按实际任务细分，不能都称迁移验证 |
| 当前容量 | `current capacity` | BMS L253 | 区别rated capacity与nominal capacity |
| 额定容量 | `rated capacity` | BMS L253 | SOH分母按本文定义 |
| 正极材料 | `cathode material` | BMS L311（数据规格表） | 原词按正极对象用，不泛指全部电池材料 |
| 恒流 | `constant-current` | BMS L468 | 与constant-voltage区分，连字符随语法处理 |
| 恒压 | `constant-voltage` | BMS L468 | 不把恒流段与恒压段混用 |
| 峰值 | `peak value` | JES L1634 | 指曲线峰的纵坐标值，不是峰位 |
| 峰值对应电压 | `voltage corresponding to the peak` | JES L1635 | 适用于以电压为横轴的峰位 |
| 峰值对应容量 | `capacity corresponding to the peak` | JES L1646 | 适用于以容量为横轴的峰位 |
| 移动平均平滑过程 | `moving average smoothing process` | JES L1669 | 本文明确用于哪些曲线，就只用于那些曲线 |
| 温度变化率 | `rate of temperature change` | JES L1612 | 应补清相对于电压还是容量，不能仅凭短语混用DTV/DTC |
| 候选窗口 | `candidate window` | EAI L396 | 窗口不等于已提取的candidate HI |
| 相关强度 | `correlation strength` | JES L1829 | 明确HI与SOH还是HI彼此之间 |
| 保留的HI | `retained HIs` | JES L1829 | 中间筛选状态，不一定是最终集合 |
| 特征间相关系数 | `inter-feature correlation coefficients` | JES L1830 | 不是HI与SOH相关系数 |
| 圆大小与颜色强度 | `circle size and color intensity` | JES L1776 | 用于相关图的视觉编码，不表示统计显著性 |

## 第三章

| 中文对象或动作 | 范文原词/短搭配 | 出处 | 使用细节 |
| --- | --- | --- | --- |
| 架构概述 | `Architecture overview` | BMS L725 | 章节功能名，正文大小写按正常语法 |
| 输入张量 | `input tensor` | EAI L818 | 与输入序列/特征图按真实对象区分 |
| 特征嵌入维度 | `feature embedding dimension` | EAI L819 | 不等于原始特征数量 |
| 顺序运算 | `sequential operations` | EAI L820 | 操作按先后执行，不自动指RNN串行递推 |
| 计算成本 | `computational cost` | BMS L773 | 与computational complexity按实际计量对象区分 |
| 逐通道滤波 | `depthwise filtering` | BMS L840 | DW操作描述，不替代DSConv整体名称 |
| 逐点组合 | `pointwise combination` | BMS L840 | PW操作描述，与深度卷积步骤区分 |
| 两倍扩展系数 | `double expansion factor` | BMS L874 | 通道扩展，不是空洞卷积系数 |
| 三倍扩展系数 | `triple expansion factor` | BMS L897 | 与两倍扩展按模块分别对应 |
| 双重作用的局部增强 | `Dual-role local enhancement` | EAI L855 | 对应本文两项局部作用，不附加范文秩恢复结论 |
| 输入增强 | `Input Enrichment` | EAI L859 | 指特征表示增强，不自动等于data augmentation |
| 局部性偏置 | `locality bias` | EAI L875 | 结构倾向，不等于已证物理机制 |
| 局部特征保留 | `local feature preservation` | EAI L1008 | 不升级为满秩恢复 |
| 特征融合阶段 | `feature fusion stage` | EAI L901 | 用来定位模块，先后顺序按本文 |
| 查询—键对 | `query-key pairs` | BMS L983 | 注意力配对对象，不随意换成通道对 |
| 核特征映射 | `kernel feature map` | EAI L907 | 与卷积kernel size中的kernel区别 |
| 全局聚合 | `Global Aggregation` | EAI L923 | 可取aggregation，不借Gated Broadcasting的门控含义 |
| 全局上下文 | `global context` | EAI L977 | 范围描述，不自动等于长期趋势 |
| 加性融合 | `additive fusion` | EAI L1019 | 仅当本文实际是相加，不替代拼接 |
| 嵌入后的特征 | `embedded features` | JES L615 | 指经过嵌入的表示，不泛称原始HI |
| 跨通道 | `across channels` | JES L695 | 说明通道间操作，不自动等于跨位置交互 |

## 第四章

| 中文对象或动作 | 范文原词/短搭配 | 出处 | 使用细节 |
| --- | --- | --- | --- |
| 初始化策略 | `initialization strategy` | EAI L1234 | 名称可用，具体分布按本文 |
| 收敛行为 | `convergence behavior` | EAI L1234 | 上位描述，区别收敛速度和后期波动 |
| 收敛速度 | `convergence speed` | EAI L1302 | 需要训练过程，不能由最终误差推断 |
| 相对收敛阈值 | `relative convergence threshold` | EAI L1302 | 原词可用，但基准损失定义按本文 |
| 最后20轮 | `final 20 epochs` | EAI L1324 | 仅在本文同样使用此窗口时用 |
| 单次前向传播 | `single forward pass` | BMS L1362 | 与累计FLOPs和完整训练区别 |
| 训练时间 | `Training time` | BMS L1363 | 不是推理延迟 |
| 存储大小 | `Storage size` | BMS L1368 | 本文为权重文件大小，不扩成运行内存 |
| 平均估计误差 | `average estimation error` | JES L2875 | 必须说明平均对象，不能自动等于综合平均误差 |
| 相对降低 | `relative reduction` | JES L3523 | 保留比较基线，区别绝对差与百分点差 |
| 对应……的降幅 | `corresponding to reductions of` | JES L3519 | 后接本文指标及降幅，不照搬范文数字 |

## 第五章

| 中文对象或动作 | 范文原词/短搭配 | 出处 | 使用细节 |
| --- | --- | --- | --- |
| 线性计算复杂度 | `linear computational complexity` | EAI L2810 | 保留本文固定智能体等适用条件 |
| 系统性特征筛选 | `systematic feature selection` | EAI L2808 | 复用摘要用词，不另换同义名称 |
| 皮尔逊与斯皮尔曼相关系数 | `Pearson and Spearman correlation coefficients (PCC and SCC)` | JES L3868 | 复用已定术语，本文阈值不随范文更换 |
| 实际部署与评价 | `real-world deployment and evaluation` | BMS L2019 | 用于未来工作，不冒充已完成验证 |

## 本轮仍需单独适配的词，不冒充范文完整原词

- 第二章：组级双相关评分、准入与冗余约束、MIT两步快充、半峰宽、固定窗口放电容量及能量效率的完整定义。
- 第三章：两个静态agent、ReLU²行归一化、零正得分时均匀回退、本文RAA/SLFA完整运算关系。
- 第四章：source-only、读出层适配、跨数据集迁移方向及本文综合平均误差的完整口径。已有术语继续沿用，不为模仿范文更换数据角色。
- 摘要与结论：已有核心术语重复使用，不为缩短或避免重复另造译名；关于部署的词按中文区分应用潜力、未来验证和已完成动作。

本轮未翻译或修改正文，未新增实验、数字和编译结果；也不把用词索引完成称为五个章节的英文译稿完成。

