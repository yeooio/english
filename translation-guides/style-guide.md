# Clear scientific English

Use `house-style.md` as the operational specification for paragraph-level detail, terminology/collocations, rhetorical patterns, and direct factual statements. It complements this guide and does not authorize substantive manuscript changes.

## Author-defined goal

“地道的翻译”就是：保留你的技术含义，同时采用英语科研论文中自然的表达方式。读起来清楚顺畅，没有明显的中文句法痕迹，也不靠难词显得学术。

Before translation, study the three domain references for technical vocabulary and collocations, grammar and tense by sentence function, sentence structure, paragraph connections, and information granularity. Granularity means how much protocol, numerical result, and interpretation detail a passage includes; it is not merely word difficulty. Map these observations to the manuscript without deleting necessary details or changing the author's organization. Keep short, traceable examples and refer back to the matching originals for each batch.

Aim for natural, precise English using common words and direct syntax. Preserve necessary technical terms even if they are long. Avoid an arbitrary vocabulary blacklist or a hard sentence-length limit.

- Prefer verified reference vocabulary and collocations when technically and grammatically appropriate, subject to the author's latest plain-language preferences in START_TRANSLATION.md. Avoid `absolutely`, `definitely`, and `demonstrate` (including inflections) in newly translated prose by default. Prefer `show` only when the intended evidence strength supports it; use `indicate`, `suggest`, `support`, or `is consistent with` when those better preserve the source. This is an author style preference, not a rule that demonstrate is reserved for professional institutions. Preserve original reference quotations and titles. For ordinary prose, use a simpler natural equivalent when meaning is unchanged; do not simplify established technical terms into vague language.
- Keep a clear subject and verb. Split overloaded sentences at meaningful boundaries while preserving cause, contrast, scope, and logical connections. Do not produce disconnected short sentences.
- Do not replace fixed technical terms with synonyms to avoid repetition. Allow grammatical inflections and meaningful distinctions.
- Check articles, countability, number, subject-verb agreement, tense, prepositions, parallel structure, modifier attachment, and pronoun antecedents.
- Use present tense for definitions and equations; usually use past tense for completed experimental actions. Decide result-reporting tense from sentence function and keep comparable statements consistent.
- Prefer direct descriptions of results to praise. Preserve hedging and limits; neither strengthen nor weaken them without reason.
- Avoid decorative transitions and adjective stacking. `Significant` must retain its intended statistical or non-statistical meaning; do not insert it as praise.
- Follow verified reference usage only where compatible with the author's meaning and these preferences. Do not copy distinctive sentences or inherit reference errors.

Apply natural English, simple wording, grammar checks, and confirmed terminology to every first proposed batch. The final whole-manuscript pass checks consistency and remaining defects; it is not a mandatory rewrite of already approved paragraphs. Do not claim 'native-level', 'journal-equivalent', or 'error-free' on the basis of a prompt or automated check alone.

## 作者表达偏好补充 — 2026-09-17

方法及应用解释尽可能避免“在本文中”“对于本文的……”及 In this study / In this paper / For ... considered here 等自指引导语；优先直接以数据、特征表示或模块为主语。避免将Q/K/V运算口头复述作为模块的应用解释。应说明数据来源、退化信息及后续用途。此偏好不授权机械删除全篇必要的贡献归属表述，也不要求无差别全局替换。
