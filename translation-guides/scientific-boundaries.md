# Scientific and Protocol Boundaries

These boundaries have priority when translating experimental protocols and conclusions.

## Experimental roles in Chapter 4

Use three explicit protocol roles: **training cell**, **validation cell**, and **test cell**. The validation cell is used for validation and comparison to select the best-performing hyperparameter configuration; it is not a test cell. The selected model is then directly tested on the remaining cells.

- Oxford: Cell1 is the training cell; Cell2 is the validation cell; Cell3--Cell8 are the test cells.
- CALCE CS2: CS2_36 is the training cell; CS2_37 is the validation cell; CS2_38 is the test cell.
- CALCE CX2: CX2_36 is the training cell; CX2_37 is the validation cell; CX2_38 is the test cell.
- MIT/Severson: b3c8 is the training cell; b3c13 is the validation cell; b3c29 is the test cell.

Do not use internal code fields such as `pure_validation` as manuscript terminology. Validation-cell results may be reported alongside test-cell results, but tables and discussion must identify their different roles. Tables may mark the validation cell with an asterisk. Cross-cell generalization conclusions must refer to the test cells rather than treating validation cells as independent tests.

## Central narrative

The manuscript jointly addresses unstable health-indicator construction and the overhead of local-global sequence modeling for resource-constrained BMSs.

- Input level: MS-CCCT performs group-level multi-scale calibration, followed by PCC/SCC admission and redundancy constraints to obtain stable, complementary inputs.
- Model level: DSConv-S preserves short-range local information, RAA enables agent-mediated cross-position interaction with linear complexity, and DSConv-L refines the fused representation over a longer scale.
- Evidence level: in-domain experiments report cross-cell performance under strict data separation; cross-dataset experiments distinguish source-only limitations from improvements after few-shot adaptation.

## Strength of claims

Prefer `show`, `indicate`, `suggest`, `support`, and `is consistent with` when they match the evidence. Do not translate cautious Chinese claims into causal proof, universal superiority, or completed deployment.
