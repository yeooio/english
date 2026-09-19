# Upstream mechanisms reviewed on 2026-09-13

This project uses independently written workflow instructions and checking code. No upstream implementation or prompt text has been vendored, and no external translation service has been configured.

- https://github.com/andrewyng/translation-agent/blob/main/src/translation_agent/utils.py : translation/reflection/revision and marked target with surrounding source context. Adaptations: complete paragraph boundaries, approved English context, explicit confirmed glossary, no colloquial-country instruction, no obligatory stylistic changes.
- https://github.com/NiuTrans/LaTeXTrans/blob/main/src/formats/latex/prompts.py : context/terminology-aware translation and protection of LaTeX structure. Adaptation: distinguish visible text arguments from identifiers; do not leave formatted prose untranslated automatically.
- https://github.com/NiuTrans/LaTeXTrans/blob/main/src/agents/tool_agents/validator_agent.py : comparison of commands, placeholders, and brackets. Adaptation: compare protected argument values and math content, report both additions and omissions. Automated checks do not establish semantic or grammatical accuracy.

Upstream links point to mutable main branches. This is a record of design provenance, not an installed dependency. Review licenses and preserve required notices before any future direct code reuse.
