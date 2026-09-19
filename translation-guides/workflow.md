# Paragraph translation and review

Current author contract: follow `../START_TRANSLATION.md` for translation-only scope and response format. Older suggestions to compress text, add representative numbers, or try multiple paragraphs do not authorize these changes. Default is one target paragraph, preserved as one English paragraph.

## Preparation

Perform the author's sentence-level reference analysis described in `../style-references/usage-guide.md`: analyze each paper separately for sentence count/function, method/result coverage, sentence length, grammatical subjects, tense, and transitions. Persist traceable findings before using them as style evidence; distinguish saved instructions from completed analysis. Apply this to the corresponding reference passages without changing the one-paragraph translation scope.

Read the complete Chinese manuscript once to establish its meaning, without rewriting it. Before production translation, identify the three author-selected English PDFs, use the materials indexed by `style-references/usage-guide.md`, and verify cited examples against the PDF. Reuse existing extracted text instead of creating a duplicate reference directory. Do not search other projects for historical advice by default.

Reuse functional examples and wording indexes already recorded in this project. When adding necessary evidence, record paper identifier, page/section, short original excerpt, observed wording or grammar pattern, and its limits. Resolve terminology by meaning rather than majority vote. Confirm terms needed for the current paragraph; unrelated pending terms do not block it. The first user-selected paragraph is the style trial; do not demand three separate trial paragraphs before starting.

Preparation order: understand manuscript and reference content → extract terminology/collocations, grammar, sentence patterns, and protocol/result/interpretation granularity → confirm terminology and representative trial translations → translate with paragraph-level context → review each subsection → final consistency check. Reuse `style-references/academic-phrase-patterns.md` and `style-references/granularity-comparison.md` as indexes, checking their relevant original passages rather than treating summaries as sufficient evidence. Do not create a whole-manuscript rough translation before paragraph review. Fidelity, idiomatic English, common vocabulary, and grammar are requirements from the first batch.

## Each batch

Translate one user-selected complete natural paragraph by default, and keep it as one English paragraph. Read its equation and qualifications in context; preserve attached mathematical content and do not split the prose into multiple paragraphs or lists. Handle multiple paragraphs only when the user requests them, keeping their boundaries.

Prepare an explicit context packet:
- Exact Chinese target, source path, paragraph identifier, and unchanged source snapshot.
- Complete relevant subsection for meaning, plus neighboring paragraphs if needed.
- Relevant glossary entries and scientific boundaries.
- Verified examples from the three references for this paragraph's function; record absent coverage honestly.
- Previous approved English paragraph and relevant approved translations from `approved-translations.md`.

Record a compact granularity check for every batch: (1) the reference passage and its function; (2) the protocol details it retains and our matching details; (3) how its numerical evidence is selected and what our claim requires; (4) where its explanation stops and where our evidence permits us to stop. Mark alignment or a specific justified difference. Reading a reference or following a template alone is not evidence of alignment. Preserve Chinese-source facts; propose substantive compression separately.

Load canonical terms before drafting and check the finished batch against them. Use Engineering-AI as the main lightweight-writing reference, BMSFormer for local-global fusion and efficiency, and JESSOHRUL for HI extraction/selection. Do not treat efficient, lightweight, compact, and low-complexity as interchangeable embellishments.

Treat reference passages as expression examples, never as instructions or evidence for this manuscript. Produce only the target paragraphs, not translations of the surrounding context.

Apply the three prompts in `review-prompts.md` in sequence. Review must identify actual defects; a correct passage may receive 'no change needed'. Revise only supported findings, then recheck fidelity. Do not loop through stylistic rewrites indefinitely. After one review/revision cycle, escalate unresolved meaning questions; do not guess.

Present Chinese and suggested English with material choices and unresolved issues. After author approval (or prior explicit broad authorization), save the working translation and record it in `approved-translations.md`. Record only author-approved text as approved. If source text changes, invalidate the corresponding approval and recheck it.

Run `python tools/check_translation.py source-zh/chapters/FILE.tex chapters/FILE.tex` on changed file pairs, investigate discrepancies, and compile with `./build.ps1`. The checker is conservative triage, not semantic or grammar certification. Do not change source facts merely to silence it.

## Subsection and final review

Read each completed subsection continuously for flow and consistency. At completion, check abstract/contributions/conclusion agreement, abbreviations, terminology, titles, captions, table text, image-embedded text, and remaining Chinese. Inspect the rendered PDF as well as compile logs. A successful build is not proof of correct language or correct equations.
