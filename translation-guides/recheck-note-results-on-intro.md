# 引言语言候选独立复核：结果章节审查者交叉检查

2026-09-13。本记录复核上一轮intro分册的5个候选，不默认初审结论正确；没有修改旧报告或正文。当前摘要与chapter01的SHA-256与上一轮分册快照一致。当前英文全文背景已读，本轮重新读取目标引言完整英文及完整中文边界，并回读其余章节英文相关全篇背景；重点依据当前文件，未拿建议稿冒充已写入正文。

| 候选 | 本轮结论 | 直接性、信息及证据复核 |
|---|---|---|
| LS-I01 / chapter01:3 | 确认 | make the stable extraction of ... more difficult改为make it harder to extract ... consistently，具体动作extract更早出现，减少动作名词化。consistently保留稳定提取要求；复杂工况、BMS限制、原引用和段尾双重挑战未变。属于有收益的小修，不是原句语法错误。EAI的infer SOH from indirect sensor data只支持具体动词带对象这一方式，不能声称它证明了本文exact替换。 |
| LS-I02 / chapter01:25 | 可选，默认不采纳 | It is therefore necessary to develop本身是常见、清楚的科研论证句，空主语不自动等于绕写。We therefore need to develop只把一般研究必要性转为作者主体，没有降低后续算法定语从句负担，也没有给算法对象新增清晰度。JES原上下文自己用it is essential，所引a HI selection algorithm is proposed是已提出方法，与本文“有必要设计”的阶段不同，不能据此要求We。保留现句更稳妥；候选可作为人称偏好，而非质量修复。 |
| LS-I03 / chapter01:27 | 需要修订，当前候选不采纳 | 发现原句抽象名词偏多这一观察可以成立，但候选mean that we need to further examine whether ...又叠入need、examine及whether层，主问题反而更晚出现。selected indicators can consistently represent degradation这一局部更具体，并不足以证明整句更直接。selected有中文“所选指标”依据，信息未丢；主要问题是修复没有通过整句直接性复查。范文直接写an HI ... may not be suitable ...，并未提供mean that we need to examine whether的绕层依据。若后续修订，应整句减少嵌套，而不是只将一个名词改成动词。 |
| LS-I04 / chapter01:44 | 确认 | uses correlations on the feature-development cells to jointly evaluate ...把两种评价共同使用的依据前置，减少句末using correlations越过长对象回挂的负担。中文“以…相关性结果为依据，综合评价…”顺序也与候选一致。HI–SOH关系及HI间冗余两对象完整，feature-development角色和其后窗口标定、筛选及结果次序保持。JES方法段先计算两相关系数再评价/筛选，确实支持依据→评价的功能顺序；但本文数据范围与范文all battery cells不同，候选正确保留本文范围。 |
| LS-I05 / chapter01:48 | 需要修订，当前候选不确认优于原句 | 原句Experiments到evaluate之间有较长数据限定与together with插入，确有阅读负担。候选虽把谓语提前，却在粗体Comprehensive validation is conducted on multiple datasets之后再次Experiments are conducted...，再以These experiments...第三次启动实验对象，句间推进更松散。事实/三类差异/三项评价/消融及复杂度/跨域/结果均保存，所以不是误译；问题是用拆句换来的直接性收益不足，增加重复引出。JES303–309的验证条目用一个实验句交代范围和目标，不能为本文重复三次启动背书。应重新处理一句内主干，或保留原句；不将当前分句版直接列作已确认优化。 |

## 本轮重新读取的原文及核对方式

- Engineering-AI/full.txt:65–97：容量完整循环限制→间接SOH估计→HI与预处理限制。TXT65–71跨页面脚注接90–97，连续语义可确认，未把73–84脚注当正文。短引68：`infer SOH from indirect sensor data`。141–145完整筛选贡献条目、146–153架构条目及154–159验证条目同时重读，区分方法操作和结论力度。
- JESSOHRUL/full.txt:1786–1796：完整筛选不足段；1797与1822–1834：完整算法段。已重新渲染并目视source.pdf第13–14页，确认13页右栏末尾This method first接14页左栏calculates...，operating接右栏conditions；没有接入DTV/DTC或表格步骤。短引1791–1793含`it is essential`，并非必须改成we；1790–1791含`an HI that performs well in one setting may not be suitable in another`；1822–1824包含先计算相关系数再`jointly evaluate`。303–309完整验证贡献条目已重读，范围→评价目标→结果的结构没有重复实验启动句。
- BMSFormer/full.txt:169–174完整精度挑战条目及208–213完整HI窗口贡献条目重读。前者说明HI表征与低相关输入的挑战，后者将窗口调整与识别HI动作连接。只作为问题/贡献语境交叉检查，不能证明We优于It，也不能证明拆成两句就更地道。

本轮PDF确认文件：build/jes-recheck-intro-13.png和build/jes-recheck-intro-14.png。短引均为本轮真实重读的原文；中文解释为助手分析。范文是功能和表达依据，不是现句与候选孰优的自动裁判；整句和上下文仍须独立判断。

最终处置：2项确认（I01、I04），1项可选且默认保留原句（I02），2项撤回旧候选并暂保留现稿（I03、I05）。I03、I05的局部负担可以记录，但本轮没有找到同时明显更直接、保持原信息顺序且更小幅的可靠修复，不为维持候选数量再造句型。未改动任何论文段落或上一轮报告。
