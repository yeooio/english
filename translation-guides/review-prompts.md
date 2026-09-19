# Reusable prompts

## 当前英文风格审校：直接性与一致性必查

对已翻译英文进行语言与范文风格审校，不重新翻译，不以反向回译为主任务。先通读当前英文全文，再逐段审查。每批重新查看 Engineering-AI、BMSFormer、JESSOHRUL 三篇 TXT 中功能对应的完整上下文；不能只依赖词表或此前总结。

尤其检查“词不难，但表达比范文绕”：主干过晚、抽象名词串联、多层修饰、空泛引导、重复解释及指代回绕。对比相同表达任务下的术语、搭配、主语与动词、信息顺序、句间承接和必要细节，不机械比较句长。优先让具体对象直接承担动作，已有自然英文不改。

简化只限语言表达，不增删科学信息、不改变必要限定或主张强度、不重排论证、不拆并段落。全文和各 agent 使用同一审校标准与已确认术语；不为了多样性轮换同义术语，也不机械套句。范文不自然或夸大的表达不继承；TXT 错序不作为语言证据。

输出现有英文、最小改动建议、可定位的范文依据和简短中文原因。提交前复核直接性、原意、表达力度与全文术语一致性。歧义单列；无问题则保留；未经作者确认不写入正文。

## 1. Translate

Translate the explicitly marked TARGET from Chinese into clear scientific English. Use CONTEXT only to resolve meaning. Apply the supplied confirmed GLOSSARY, SCIENTIFIC BOUNDARIES, APPROVED TRANSLATIONS, and verified REFERENCE EXAMPLES. Prefer common, precise words and natural syntax. Preserve paragraph function and all facts, qualifications, comparisons, and causal strength. Preserve LaTeX syntax and protected arguments: labels, citation/reference keys, paths, math, numbers, and units. Translate visible prose within headings, captions, and formatting commands; do not translate their identifiers. Flag ambiguous meaning rather than inventing a resolution. Output the suggested translation and a separate short list of unresolved issues. Never present unverified reference examples as verified.

## 2. Review without rewriting

Author-specific wording check: flag absolutely, definitely, and demonstrate (including inflections) in new translated prose, not in faithful source quotations, reference titles, or protected identifiers. Check the entire claim for overstatement; replacing a verb with show does not cure an unsupported universal or causal claim. Match show/indicate/suggest/support to the original uncertainty and evidence strength. Identify unnecessarily rare or inflated ordinary wording, while protecting accurate technical terminology. Do not add hedges to every sentence or silently weaken/strengthen scientific claims.

Compare SOURCE with DRAFT using the same context packet. First check additions, omissions, mistranslations, quantities, comparison objects, conditions, and claim strength. Then check grammar, idiomatic scientific phrasing, common-word alternatives, logical connections, and exact glossary usage. Separately inspect protected LaTeX content. For each genuine issue, identify its location, explain the defect, and propose the smallest repair. Distinguish required corrections from optional preferences. Do not invent criticism to force a rewrite. If no correction is needed, say so. Reference examples guide expression, not manuscript facts.

## 3. Revise and verify

Apply only supported corrections to DRAFT. Reject suggestions that change the source meaning, violate confirmed terminology, or only replace one acceptable expression with another. Check the revised text against SOURCE again. Preserve approved language where no defect exists. Return final suggested English, resolved findings, and remaining questions. Do not mark it author-approved until the author approves it.
