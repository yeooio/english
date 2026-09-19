# Reference Usage Guide

## Priority

References are selected by function, not ranked globally. Latest author clarification, 2026-09-16:

1. **Engineering-AI (SL-AgentNet)**: primary reference for lightweight design and lightweight-expression style. Its hardware, uncertainty and statistical evidence must not be imported into our manuscript without matching experiments.
2. **BMSFormer**: primary reference for local-global fusion, convolution and attention mechanisms, and computational/resource metrics (including computational cost, FLOPs, training time, parameter count, and storage size). Lightweight-expression style still primarily follows SL-AgentNet.
3. **JESSOHRUL**: primary reference for multi-source health indicators, correlation-based selection, and associated experimental expression. Use only the parts relevant to our SOH task.

All three references may be cross-checked. These priorities guide the first comparison; they do not prohibit a suitable term from another reference. Match the same technical object and full context, preserve the Chinese meaning and measurement definition, and retain approved consistent terminology unless the author approves a change. This clarification alone does not authorize manuscript edits or reverse earlier approved choices.

## How to read

The TXT files are page-range retrieval aids, not cleaned continuous sections. They contain neighboring sections, headers, and some two-column reading-order errors. Locate the desired heading, check source.pdf when studying paragraph progression, and use `../translation-guides/reference-evidence.md` for the curated short expressions. Do not imitate extraction artifacts.

The operational style specification is `../translation-guides/house-style.md` together with `../translation-guides/expression-detail-rules.md`.

- Abstract translation: read the three `abstract.txt` files and the Abstract row in `granularity-comparison.md`.
- Introduction translation: read the three `introduction.txt` files and the Introduction row.
- Method translation: read the three `methodology.txt` files and the Method row.
- Results translation: read the three `results.txt` files and the Results row.
- Conclusion translation: read the three `conclusion.txt` files and the Conclusion row.
- Use `full.txt` only to recover context that crosses a page-range boundary.

Do not copy whole sentences. Reuse established terminology, rhetorical functions, information density, and sentence patterns, then map them to the evidence and structure of the MS-AgentNet manuscript.

## Language and narrative target

### Required sentence-level reference analysis

Author requirement (2026-09-13): “逐篇数句子，检查每句的作用、方法与结果各占多少篇幅，以及句长、主语、时态和衔接方式。”

For each of the three papers, analyze the corresponding passage separately before comparing them. Use the verified PDF reading order; remove headers and extraction artifacts and check sentence boundaries around abbreviations, citations, equations, and semicolons. Record the paper, page, section, and exact passage boundaries so counts are reproducible.

- Count sentences and assign a stable sentence ID within the passage.
- For each sentence record its function (background, gap, objective, method, result, interpretation, limitation, or transition), word count, grammatical subject, tense/voice of the main clause, and how it connects to the previous sentence (including implicit links).
- Record method and result coverage using both sentence counts and word counts, stating the denominator (the selected passage, not an unspecified whole paper). For mixed-function sentences, mark the functions explicitly and use clause-level word allocation or report them separately; do not double-count as disjoint percentages.
- Summarize sentence-length distribution and the sequence of sentence functions. Explain how subjects, tense choices, and transitions advance the argument, rather than only listing statistics.
- Save completed analyses with their source locations in `translation-guides/reference-evidence.md`, or link a dedicated analysis file from there if the records become long. Mark incomplete or uncertain counts as such; never present estimates as measured counts.

These observations guide natural English and information granularity. They do not impose the reference's sentence count, length, method/result ratio, or paragraph structure on the Chinese manuscript. Preserve all author-required content and paragraph boundaries. This analysis is preparation/internal evidence and does not automatically expand the author-approved concise translation response format. Reuse verified analyses, revisiting original passages when the translation task requires a different function or scope.

- Learn domain-specific terminology, verb-object collocations, paragraph progression, and the amount of protocol, numerical, and interpretive detail from the corresponding original passages. These three papers are the selected references, not evidence that all leading journals use one uniform style.
- Prefer direct affirmative statements of what the method does, how the experiment is configured, and what the results show. Affirmative wording does not mean reporting only favorable results.
- Keep scientific-boundary checks internal. Do not insert reviewer-facing disclaimers into each paragraph merely because the checks exist.
- Use contrast, negation, and concessions only when they communicate a necessary research gap, comparison, or limitation. Do not repeatedly add `not ... but ...`, `although`, `unlike`, or explanations of why the authors are justified.
- State limitations as concrete observations. Preserve necessary conditions, uncertainty, and reproducibility details; remove only redundant defensive language.
- Label phrase-library entries as adapted patterns. Future additions should record the source paper and section and the rhetorical function actually observed there.
