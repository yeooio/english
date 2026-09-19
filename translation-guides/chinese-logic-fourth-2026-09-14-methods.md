# 第四轮查漏：第2–3章及旧建议保真复核

日期：2026-09-14。仅新增本报告；没有修改中英文正文、公式、表格、图片或旧报告。

## 结论

本范围没有确认值得独立新增的正文问题（0项新增）。发现一处旧候选可做更小的保真调整：第二轮N-M01修复CVT句间关系时，可以保留原文“持续/continuous”，不要顺带删除尚未确认要删除的限定。这是审查建议自身的质量控制，不计作又发现一处论文错误。

完整复读冻结中文与当前英文第2–3章；对照第一轮methods、第二轮methods及intro-cross、第三轮math以及9月13日whole-manuscript-review，核对既有议题。主要检查定义、连接词、指代、比较对象、运算对象、条件和力度。本轮未读取训练实现、预测数组或重审架构图像，不声称再次核实图内所有节点。

## Q-M01：N-M01旧候选保留“持续”的最小版本

位置：[中文第2章52行](D:/MS-AgentNet-English/source-zh/chapters/chapter02.tex:52)、[英文同位置](D:/MS-AgentNet-English/chapters/chapter02.tex:52)、[第二轮N-M01](D:/MS-AgentNet-English/translation-guides/chinese-logic-second-2026-09-14-methods.md:7)。

中文原句：

> 随循环推进，CVT 曲线沿时间轴逐渐偏移，如\cref{fig:2-3}(a)所示。该偏移表现为固定电压区间内的充电时长随老化持续变化。

现英文：

> As cycling progresses, the CVT curve gradually shifts along the time axis, as shown in \cref{fig:2-3}(a). This shift appears as a continuous change in charge duration within a fixed voltage interval as the battery ages.

第二轮候选：

> 随循环推进，CVT曲线沿时间轴的位置发生变化，如\cref{fig:2-3}(a)所示；固定电压区间内的充电时长也随老化变化。

> As cycling progresses, the position of the CVT curve along the time axis changes, as shown in \cref{fig:2-3}(a); the charge duration within a fixed voltage interval also changes with aging.

本轮更小的条件候选（只替换第二句，第一句原样保留）：

> 固定电压区间内的充电时长也随老化持续变化。

> The charge duration within a fixed voltage interval also changes continuously as the battery ages.

原因及改后效果：原审查根据CCCT=t(V2)−t(V1)指出，纯时间平移不改变差值，故不能把窗口时长变化无条件等同于平移结果。本轮不撤销这一条件性疑点。但去掉“该偏移表现为/This shift appears as”足以解除等同关系，不必同时改写第一句或删除“持续/continuous”。更小候选保留原第一句的“逐渐/gradually”和第二句的变化持续性，只把两种现象并列。

采用条件：必须确认图或提取记录确实支持第二项时长观察，且作者仍意指持续变化；否则不能用“also changes”补造观察。第二轮已经明确要求核实“持续”的实际含义，本轮是把保留分支写得更具体，不是指控旧报告未经说明改稿。此处continuous/continuously不扩写为“单调变化”“每个循环都变化”或数学意义的处处连续；这几种含义均非现有文本可以自动推出。主审将初稿被动表达“A continuous change ... is also observed”改为以charge duration作主语的直接表达，避免抽象名词与空泛观察引导；两者都不是范文原句。

范文依据及限度：本轮重新读取[JESSOHRUL TXT1625–1686](D:/MS-AgentNet-English/style-references/JESSOHRUL/full.txt:1625)的HI表与相关性定义上下文，表项“The charge time within the voltage range of 3.8–4.2 V”直接命名窗口内充电时长。另读[BMSFormer TXT426–460](D:/MS-AgentNet-English/style-references/BMSFormer/full.txt:426)的完整HI提取语境，以及[Engineering-AI TXT333–426](D:/MS-AgentNet-English/style-references/Engineering-AI/full.txt:333)的窗口筛选语境。它们支持明确描述窗口特征对象，但都不能证明本文时长持续变化，也没有要求使用上述候选整句。保留continuous的依据是本文原意保护，而非范文中存在同词。TXT跨栏穿插不重组为连续论证，未以摘词代替窗口语境。

## 本轮再次核对后保留、不新增为问题

1. 第2章“除充电时序特征外”从时间类HI转到容量—电压HI，关系成立；不因“时序”二字就改成循环预测特征。现英文charge timing features能理解，旧报告的time-based charging features只是可选表达。
2. DTV到DTC的“与……不同/While”对比的是自变量域，不是说两者完全没有共同点；后面的“同样/also”描述相同平滑处理并不矛盾。DTC文字中的rate of temperature change在紧接dT/dQ定义的上下文可理解，不强行判为误指dT/dt，也不为补字制造新增缺陷。
3. HI13/14的两项命名和数值对应没有漏译；MIT完整电压窗适用问题继续归入旧N-M02，不因重读再计一项。
4. 第2章“若仅依据Cell1”明确条件比较；HI5在Cell2降低的例子支持单池排序代表性有限，并未声称所有指标都降低。两池绝对相关能证明什么的范围继续归入旧S-IC02。
5. R3优于R2采用R3、“否则”包含相等分支；不另加一条等值规则。R3搜索区域仍为旧N-M04条件核实，不由“进一步”擅自决定嵌套实现。
6. 第3章FFN的The result明确为处理输出；中文省略主语可读，延续第二轮对旧M02的降级，不恢复“必然自己与自己相加”的过重诊断。
7. DSConv-L说“整体变换顺序一致”，后半句立即明确残差在Block层；合读不等于要求复制DSConv-S的内部残差。旧图文边界问题由图—公式核实处理，不改这段去迁就图。
8. RAA正比例不变性仅针对共同正尺度，零正值行已给均匀回退；不是所有形式的得分变化都不变。现中英均保留该条件，不新增epsilon或其他归一化算法。
9. Phi_q Phi_k的秩上界明确限定等效序列交互，不覆盖带输入残差的整个RAA输出；此处现稿保留，不能把低秩反例用错对象。
10. 局部—全局融合段的“这种加性连接/This additive connection”直接承接slfa_fusion，指代清楚；既有长程范围疑点归旧S-IC01，不重复要求删除global术语。

## 旧候选的采用边界继续有效

- M03把“均强相关”收窄为选择目标；M05补成本条件；M06涉及维度/计量；M07补商式成立条件；M08明确存在量词。这些不能全部称为不改力度的语言润色。仍须逐项确认，不由于已生成建议就视作已经批准。
- M04按X01整段范围版本处理，不只替换最后一句造成段内“其他电池”的指代前后不一致。
- 不能用范文的窗口、padding、运行次数或层参数填本文空缺；未在本轮确认的实现事实保持待核。
- 本轮没有发现新的、可直接认定为“词汇简单但表达绕”且足以必须修改的句子。已有自然表达保留，不以持续审查等于持续改写。

这轮0项新增正文问题并不证明全文零遗漏；它只说明上述范围经过再读，没有找到足够证据支持另列新问题。原始实验口径、图文版本等未闭环事项仍要依靠对应记录核实，继续换一种语言复述不会使其自行解决。
