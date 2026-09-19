# 第一章句式与动词审校：开头两段 — 2026-09-16

状态：仅提案，未改正文。第一批范围为chapter01.tex第1、3行两段（文献综述标题之前），共10句；其余引言读取作为上下文，不宣称其句式审校已完成。当前英文全文阅读复用刚完成的术语审查；此次重新读当前引言和对应中文背景。

## 范文尺度与本批新读证据

重新读取BMS full.txt:50–79、92–97（完整首段、跨页第二段）；SL:50–71、90–97（完整前两段，跳过页脚）；JE:53–71、105–121（背景及HI提取限制的完整对应段）。沿用已按PDF核对的段落边界与句级测量，见introduction-p01-reference-analysis.md、introduction-p02-reference-analysis.md：BMS首段4句/87词，SL首段7句/158词，JE首段2句/59词。它们本身句长、细节量不同，本文不按句数裁剪。相关功能是背景—风险—估计必要性和测量限制—间接估计—应用约束。

- BMS将电池作为主语，直接用pose陈述风险，随后回指hazards说明来源；没有要求先增加运行稳定性的否定句。
- SL的容量测量段使用requires、impractical及infer SOH，接续测量限制与间接估计；本文对应路径已经相近。
- JE首段也用precise estimation和is essential；HI段直接描述测量耗时、设备要求和工况限制。不能因本文使用precise/essential/require就判其过强。
- 范文也有抽象名词主语及长句，所以本文出现estimation、efficiency等名词不自动成为错误。

## 建议S1：风险句 — 建议修改

位置：chapter01.tex:1，第二句。类型：词汇简单但表达绕；伴随中文范围核对。

现有英文：
> Nevertheless, lithium-ion batteries cannot always remain stable during long-term operation and continue to pose safety risks that cannot be overlooked.

建议英文：
> Nevertheless, during long-term operation, lithium-ion batteries still pose safety risks that cannot be overlooked.

中文原文：尽管如此，电池在长期运行中仍存在不可忽视的安全风险。

建议回译：尽管如此，在长期运行中，锂离子电池仍存在不可忽视的安全风险。

依据：BMS full.txt:50–58在同一开篇风险功能处使用电池主语+pose+风险宾语；SL50–64和JE53–59也直接由具体对象转入退化/安全与监测需求，没有要求这一额外否定层。本文现有cannot always remain stable并非中文这一句的独立事实，不必额外保留。建议保留Nevertheless、长期运行、仍然、不可忽视四项限定；没有改成“必然故障”或“完全不安全”。用时间短语安排停顿，主干直接落到batteries still pose safety risks。

## 可选S2：间接估计句 — 不作为必要修改

位置：chapter01.tex:3，第三句。

现有英文：
> Consequently, indirectly inferring SOH from observable operating signals has become a key approach to online battery health monitoring.

可选英文：
> Consequently, estimating SOH indirectly from observable operating signals has become a key approach to online battery health monitoring.

原因：将任务动词提前，并与SOH estimation呼应，保持间接、可观测运行信号及关键途径含义。但SL full.txt:65–71本身就使用infer SOH from indirect sensor data；现有infer有准确依据且句子清楚，因此优先保留，不为了动词字面一致制造必改项。

## 其余句子处理

| 句子 | 动词/形容词与结构核对 | 结论 |
|---|---|---|
| P1S1 优势与应用 | With前置条件、have become、widely used；与BMS50–52功能路径相近 | 本批不为句长改写；不是全句逐词来自范文的声明 |
| P1S3 老化机制 | induce连接明确过程对象；三类老化现象保持 | 保留，中文有引发含义 |
| P1S4 衰减及故障 | lead to/trigger与中文导致/引发对应，保留in severe cases | 保留，不增强因果范围 |
| P1S5 必要性 | precise estimation/is essential与BMS56–58、JE56–59对应；是需求句非模型成果保证 | 保留 |
| P2S1 SOH定义 | commonly defined限定一般定义；capacity retention不变 | 保留 |
| P2S2 直接测量限制 | requires及impractical与SL65–69对应，完整/近完整限定保留 | 保留 |
| P2S4 两类限制 | make it harder to/constrain直接对应提取难度与模型资源边界 | 保留，不能把constrain擅改成prevent |
| P2S5 双重挑战 | 总结两个前述对象，名词并列并非自动错误；不为更短新增提高/确保等目的动词 | 保留 |

目前建议确认的修改仅S1。S2为可选且推荐保留。已确认的专业术语不重开；不改段落顺序、技术名词、数值、引文或公式。本批没有修改或编译论文。下一批为1.1文献综述，按模型方法/HI方法分别呈现建议，仍需作者确认后才写入。
