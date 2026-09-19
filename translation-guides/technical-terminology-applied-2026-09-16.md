# 全文专业术语复查与修改记录（2026-09-16）

作者授权：在上一轮全文专业术语报告后要求“再仔细思考一下我担心有漏，开agent再去找，我们现在来修改即可”。本批据此复查并直接实施含义已核实的一致性修改。只改术语，不重写论证、公式、数值或协议。

## 已实施：3组、8处论文替换

| 文件与行 | 原英文 | 新英文 | 依据与中文意义 |
| --- | --- | --- | --- |
| chapters/chapter01.tex:44 | a health indicator combination | a final HI subset | 候选池经相关性与冗余筛选后的最终集合，复用JESSOHRUL §3.5.2 full.txt:1822–1834。保留中文“确定相应指标组合”的对象，不改输入数量。 |
| tables/table_2_hi_screening_steps.tex:17 | the final selected HI set | the final HI subset | 与引言同一最终输出；步骤4正在构造的selected HI set保留。 |
| chapters/chapter01.tex:48 | different battery materials, capacities | different battery chemistries, capacities | 这里指公开数据集的化学材料体系，统一前文已有用词。 |
| chapters/chapter02.tex:13 | different material systems and operating conditions | different battery chemistries and operating conditions | 中文“不同材料体系和运行工况”，指NCO/LCO/LFP等，含义不变。 |
| chapters/chapter02.tex:23 | differ considerably in material systems | differ considerably in battery chemistries | 中文“在材料体系……存在明显差异”；保留同段更宽的battery systems及nominal capacities。 |
| chapters/chapter04.tex:103 | differ from Oxford in battery materials | differ from Oxford in battery chemistries | 与数据集定义使用同一体系名称，保留比较对象Oxford及工况限定。 |
| chapters/chapter02.tex:58 | the resulting charge duration feature | the resulting charging-time feature | 统一HI1所属特征类别的名称，不改变CCCT定义。 |
| chapters/chapter02.tex:60 | In addition to charge timing features | In addition to charging-time features | 指充电时差类特征；time比timing更明确，避免充电时机/调度联想。 |

材料体系的三篇依据：BMSFormer摘要 full.txt:37，Engineering-AI §2.2.1:177–181、数据采集:317–318，JESSOHRUL §3.5.2:1786–1796。范文也用materials，所以本批是内部规范统一，不将旧词称为科学错误。具体正极材料等名称未替换。

充电时间特征的三篇校准：BMSFormer §2.3:457–459、503–506用constant current charge/charging time；JESSOHRUL引言:122–138和表4:1637–1638用时差/charge time；Engineering-AI:327用CC phase duration描述物理时长，但其面积指标不同，不继承CCCA/CCDA名称。正文普通物理时长charge duration保留。

最终HI子集的三篇校准：JESSOHRUL候选筛选后输出final HI subset，与本文功能相同；BMSFormer与Engineering-AI主要优化单个时间/积分窗口，不据此改变本文多指标候选池、阈值或电池角色。

## 本轮独立查漏结果

三名agent分别复查摘要/引言/第2章与HI表、第3章与模型配置表、第4/5章与实验表，并重读三篇对应完整语境。未找到应新增为确定专业术语错误的条目；不保证全文绝无遗漏。

额外核实后保留：

- `root mean square error`与Engineering-AI/JESSOHRUL一致，不追随另一范文的squared变体。
- 普通正态、截断正态、Xavier uniform是不同初始化方法，不照搬范文默认设置。
- `kernel function`/`nonnegative feature mapping`有中文及范文对应依据；逐通道scaling、projection、expansion是不同运算。
- `linear association`在BMSFormer PCC定义中是原词；不强制改linear correlation。
- `random forest`是算法名称，`Random Forest Regression`限定回归任务；不强制删除限定。
- `rated capacity`与`nominal capacity`按中文对象保留；DTV相关的引用文献称谓与本文定义保持区别。
- `combined average error`与各项指标分别跨电池平均的average不是同一统计对象。
- source-only/few-shot及训练、配置、迁移参考电池角色没有混称。
- 第3章`cross-position context`与冻结中文直接对应，本轮未采纳可选global context替换。
- 表1的LC目前只有缩写。JESSOHRUL用linear contrast，不据猜测将本文扩成linear correlation；需要展开时应另核实原引文。

作者已知待同步的SLFA/LLGFA等旧图名称未处理，也不计入本批查漏结果。

## 同步与保护

- 7处正文替换已同步至 `full-manuscript-bilingual.md` 的英文内容；表格不在该文件对应范围。
- `terminology.md`记录本轮三个统一称谓及适用边界；旧报告保留审查历史。
- 修改前文本及SHA-256清单存于 `build/term-consistency-20260916-141655/`，精确8项替换记录为该目录 `changes.json`。
- 冻结中文、图像、第3章及第5章本轮不修改。保护项与编译验证结果在本文件下方续记。

## 验证结果与后续授权边界

- 独立agent逐项核实本批8处替换及7处双语英文同步，意义、语法和中文技术信息保持。
- 工作目录期间另出现第1章及双语稿3处同步变化：HI缩写补充、impedance spectrum measurements、backpropagation (BP)展开；并非本批8项替换操作，予以保留，不计入本批修改数量。批准记录中有对应引言条目。本轮未回退或覆盖这些变化。
- 修改前后公式、数值、引用、标签、LaTeX命令及环境检查通过；冻结source-zh全部文件SHA-256不变。第3章、第5章与本批备份一致。
- 中文—英文检查器在第2章、第4章和筛选表无提示；第1章仍只有修改前已有的42/100数字分词提示，本批无新增提示。
- `build.ps1`执行成功，生成37页 `build/main.pdf`；编译日志未发现Overfull/Underfull、未定义引用、缺字或LaTeX错误，原有ICC/locale提示保留。
- 已渲染并检查受影响的第5、6、7、9、14、25页，术语显示正确，没有新增遮挡、溢出或表格排版问题。
- 作者在本轮实施后明确要求“后续需要经过我的同意再修改”。本轮未再追加正文修改；后续必须先提供原文、建议和理由，取得作者明确同意后才写入论文。本次授权不延续为后续自动修改权限。
