# Author decision: reference-led wording for training, validation, and testing

Date: 2026-09-16

## Binding author requirement

- For all manuscript passages concerning training, validation, testing, cell roles, and cross-cell generalization, first reread the complete functionally corresponding context in BMSFormer and cross-check the other two reference papers.
- Reuse reference-supported terminology, sentence functions, and progression wherever the technical conditions match. Do not invent new role names, statistical categories, section labels, or reviewer-facing explanations merely because they sound more rigorous.
- Every proposed or implemented wording change must record the current manuscript wording, the reference location, whether the experimental conditions match, and why the adapted wording preserves the manuscript facts.
- Do not copy BMSFormer's `30%/70%/100%` or `Offline/Online` labels: BMSFormer partitions the reference cell chronologically, whereas this manuscript assigns separate training and validation cells.
- In this manuscript, the second cell used for hyperparameter selection is a validation cell, not a test cell. The remaining cells not used for feature development or hyperparameter selection are the test cells.
- Validation-cell results may be reported alongside test-cell results, following the reference papers, but they must not be described as test results. Statements about cross-cell generalization must refer to the actual test cells rather than silently treating validation cells as independent tests.
- Do not use the absence of criticism of a reference paper as proof that a methodological description is automatically valid here. Match the experimental object and conditions.

## Reviewer-directed sequence-length wording

- The current English complexity paragraph must not state `a sequence length of 5` or an equivalent phrase.
- Do not remove or rename `K=5`, `S5`, or the `1\times5` depthwise convolution: these denote a convolutional kernel size, not the input sequence length.
- The frozen Chinese source remains unchanged; this decision applies to the current English manuscript and future English-review passes.

## Reference contexts rechecked

- BMSFormer `full.txt`: 284--299, 1078--1099, 1309--1326, 1370--1383, and 1988--2013; source PDF Fig. 1 and Figs. 7/10.
- Engineering-AI `full.txt`: 1294--1315, 1332--1358, 1376--1378, and 1458--1459.
- JESSOHRUL `full.txt`: 1946--1981 and 1306--1313.

## Reference-supported expression path

1. Identify the training cell(s).
2. State that validation results are used to select the best-performing model or hyperparameter configuration.
3. State that the selected model is directly tested on the other cells/batteries.
4. Distinguish `validation results` from `test results` in the results discussion and table notes.
5. If validation and test cells are shown together, identify the validation cell explicitly; do not call all reported cells test cells.

## Superseded assistant suggestions

The following earlier assistant-generated phrases are not treated as reference wording and must not be adopted solely on that basis: `Cell-role assignment for four datasets`, `Cross-cell testing and cross-dataset transfer`, and the proposed statistical labels `Overall average`/`Test average`. They may be reconsidered only if the author separately requests a methodological reporting change.
