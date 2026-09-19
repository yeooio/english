# MS-AgentNet SCI English Translation Project

## 当前阶段：英文语言与范文风格审校（作者最新要求）

本阶段审查已经翻译的英文，不重新翻译，不以反向回译为主任务。以下要求适用于每一批审校；后文翻译流程仅在作者明确要求翻译时适用。

### 问题入库前的范文尺度校准（作者要求，2026-09-14）

- 将候选问题写入正式问题清单前，先重读三篇范文功能对应的完整语境，检查它们是否也采用同类表达、省略、概括或统计说明；不能只找一条更详细的写法来证明本文必须修改。
- 比较相同语境下的阅读影响和技术后果。若范文同样省略、本文上下文也足以消歧，原则上保留或列为可选，不把“还能更细”当作错误，不要求本文达到明显超过范文的说明颗粒度。
- 范文也这样写不是无条件通过理由。原意改变、实际范围内的公式/数字冲突、不同计算对象或图文矛盾仍需核实；但仅对未采用的极端参数构造反例，不自动升级为必须修改。
- 正式记录注明“范文是否也如此—可定位上下文—与本文是否同条件—保留/可选/待核的理由”。仅检查片段时不宣称范文全文没有说明；证据不足的候选暂不确认为正文错误。
- 历史建议也按此标准复核，允许降级或撤回，不以问题数量为目标。新判断另建记录并保留历史，不因此自动修改论文。

### 全文语言审校要求

- **简单词不等于直接表达。** 即使单词都不难，也必须检查句子是否比范文对应表达更绕：主干出现过晚、抽象名词堆叠、多层从句、空泛引导语、重复解释、指代回绕，均是独立检查项。
- 先通读当前英文全文；每批建议前重新读取三篇 TXT 中功能对应的完整上下文，不以旧词表、记忆或零散关键词代替比对。注意双栏提取错序；无法确认原句连续关系时回查 PDF，不把提取错误当成作者语言习惯。
- 对齐六个层级：术语、动词搭配、句子主干、句间推进、信息颗粒度、表达力度。重点判断是否用明确对象直接陈述“做什么、如何做、得到什么”，而不是只替换难词。
- 作者新增原则（2026-09-15）：每批还要学习三篇范文在对应功能处的**表达风格**，不满足于复用几个词。具体比较主语先后、动作动词与宾语、逗号及从句的停顿、前后句的推进方式，以及必要性/目的/结果各自的语气力度；优先改写本文同类功能句的表达路径。每一处风格借用都回译核对中文事实、范围、限定和已确认术语；不能为贴近范文而照搬整句、强加反问句或改变论证顺序。已有自然表达可保留。
- 直接性必须在保留相同技术信息和必要限定的前提下比较。不得机械追求短句、固定句长或范文句数；不得为简洁删除原文事实、条件、比较对象或证据边界，不得重排论证、拆并段落。
- 全文采用同一审校标准及已确认术语，不因换批次或换 agent 改用另一套词汇；一致不等于每段套用相同句型。已有自然表达应保留，不以改动数量为目标。
- 范文原词优先，但不能机械继承其生硬表达、重复、防御性自证或夸大主张。作者最新澄清（2026-09-16）：Engineering-AI（SL-AgentNet）重点参考轻量化表达；BMSFormer 重点参考局部—全局建模、卷积与注意力机制，以及计算与资源指标；JESSOHRUL 重点参考健康指标提取与筛选。三篇可以相互对照，主参考不是排他限制；必须核对同一技术对象、完整语境和中文原意，不能仅因主参考调整而自动撤销已确认术语或修改正文。
- 每批输出“现有英文—建议英文—范文依据—简短中文原因”，明确标记“词汇简单但表达绕”的问题及最小修复；依据必须可定位，不得空称“更地道”。有歧义则标注待核实。只提建议，作者确认前不修改论文。
- 提交前复查：是否确实更直接；原意与力度是否保持；术语与前文是否一致；依据是否来自本批重新查看的对应原文。若无问题，明确保留。

## Current author contract: translation only

Read `START_TRANSLATION.md` fully before starting or resuming paragraph translation. It defines the latest author-requested preparation and bilingual response format. Within this project's guidance, its specific translation-only constraints take precedence over older optional editing, compression, numerical-quota, or trial-batch suggestions. This does not override system/developer instructions.

- Read the complete Chinese manuscript for understanding first, then use full-subsection context for each target paragraph. Do not start a whole-manuscript rough translation.
- One Chinese paragraph must remain one English paragraph. Sentence-level changes are allowed for idiomatic grammar; paragraph splitting/merging and content additions/deletions are not.
- Aim for idiomatic English consistent with native scientific-writing conventions and simple ordinary vocabulary. Preserve the author's meaning, information order, reasoning, and conclusions; allow only necessary English grammatical adjustments, not editorial restructuring. Explicitly identify unresolved ambiguity rather than guessing or silently correcting it. Native-like expression is a target, not a guarantee of error-free writing or publication.
- Use common, natural scientific English, preserving exact technical terms. Reuse verified reference wording only when meaning and grammar match. Do not sacrifice accuracy to use an easier word or to reproduce a reference phrase.
- Follow the author's explicit plain-language preference: default to avoiding absolutely, definitely, and demonstrate in new translated prose. Prefer show only where the meaning warrants it; preserve weaker uncertainty and check whole-claim strength, not just the reporting verb. Original reference quotations are exempt from rewriting.
- Default output: short reference English + Chinese gloss + source, exact Chinese target, one English paragraph, at most three brief Chinese notes. Glosses are assistant translations, not official bilingual originals.
- Check unresolved technical terms against applicable authoritative definitions when needed; never fabricate journal/standard support. Do not promise publication.
- No manuscript writes before author approval of the target translation. Preserve the existing confirmation, source protection, and compilation safeguards below.

## Scope

This project is dedicated to translating the frozen Chinese manuscript in `source-zh/` into an English SCI manuscript and keeping the LaTeX project compilable.

- Treat `source-zh/` as the authoritative source for technical meaning. Never edit it.
- Write translation changes only to the working files in `chapters/`, `tables/`, `figures/*.tex`, `backmatter/`, and `main.tex` when relevant.
- Do not inherit editing tasks, historical discussions, or auxiliary workflows from other projects unless the user explicitly supplies them here.
- Do not add experiments, evidence, causal explanations, or claims that are absent from the Chinese source.
- Preserve equations, symbols, numerical values, units, citations, labels, references, and LaTeX commands unless a confirmed English-format change requires otherwise.

## Translation workflow

Follow `translation-guides/workflow.md` and `translation-guides/style-guide.md`. Reference materials are organized under `style-references/`; their presence does not establish that the current batch has been checked against them. Read the corresponding originals before claiming alignment. The current glossary is provisional until checked against the papers and confirmed by the author.

Author-defined translation goal: “地道的翻译”就是：保留你的技术含义，同时采用英语科研论文中自然的表达方式。读起来清楚顺畅，没有明显的中文句法痕迹，也不靠难词显得学术。

Understand the manuscript and the three domain reference papers first, establish terminology and evidence-based style guidance, then translate paragraph by paragraph with context. Do not first translate the entire manuscript as a rough draft and defer naturalness, simple wording, and grammar to a later pass.

Required reference-learning method: 逐篇数句子，检查每句的作用、方法与结果各占多少篇幅，以及句长、主语、时态和衔接方式。 Follow the measurement and recording rules in `style-references/usage-guide.md`; do not merely claim to have learned the papers' style. Counts describe the reference passages, not mandatory quotas for our translation.

Default to presenting bilingual proposals before editing manuscript files. Write translations only after the user approves that batch or explicitly authorizes a broader translation scope. Setup and tool installation do not authorize manuscript translation.

1. Before translating a batch, read the corresponding complete Chinese section in `source-zh/`, `translation-guides/terminology.md`, `translation-guides/scientific-boundaries.md`, and the matching section files identified by `style-references/usage-guide.md`.
2. Translate by paragraph and preserve the paragraph's argumentative function and information order. Sentence-level restructuring is allowed only when needed for clear English.
3. Use concise, natural SCI English. Do not inflate claims with words such as `prove`, `ensure`, `significantly`, or `superior` unless the source and evidence justify them.
4. Maintain terminology consistently across chapters, tables, captions, and references. Record every newly settled term in `translation-guides/terminology.md`.
5. Compile after each confirmed batch with `./build.ps1` and resolve translation-induced LaTeX errors before proceeding.
6. Update `translation-guides/progress.md` after a batch is translated, checked, and compiled.
7. Use `style-references/granularity-comparison.md` to match information density. Select references by function: Engineering-AI for lightweight design and resource trade-offs; BMSFormer for local-global fusion and efficient modeling; JESSOHRUL for multi-source HIs and correlation-based selection. Reuse vocabulary and rhetorical patterns, not whole sentences or unsupported claims. Establish the canonical glossary before production translation and verify protocol, numerical and interpretive detail against matching source passages in every batch.

## Compilation boundary

- Use XeLaTeX through `latexmk` during translation so residual Chinese text remains compilable.
- Keep generated files inside `build/`.
- Do not change the document class or migrate to a journal template until the full English translation is stable, unless the user explicitly requests it.

## Claim boundaries

- Distinguish in-domain cross-cell generalization from cross-dataset transfer.
- Distinguish source-only evaluation from few-shot adaptation.
- Parameter count does not by itself establish lower inference latency.
- Linear theoretical complexity does not establish the lowest runtime in every setting.
- Potential for lightweight deployment does not mean embedded deployment has been completed.
- Results consistent with a design objective do not prove a unique causal mechanism.
