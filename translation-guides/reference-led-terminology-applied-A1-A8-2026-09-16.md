# A1—A8 术语修改实施记录 — 2026-09-16

作者授权：“先改A1到A8”。本批仅落实 `reference-led-terminology-audit-2026-09-16.md` 中 A1—A8 的27处正文/表格替换；B项及其他候选未实施。范文证据与语境判断保留在原审查报告。

| 项目 | 原词 → 确认词 | 处数 | 文件与行号 |
|---|---|---:|---|
| A1 | health indicator screening → health indicator selection | 2 | tables/table_2_hi_screening_steps.tex:3、7 |
| A2 | repeated information → redundant information | 1 | chapters/chapter02.tex:155 |
| A3 | linear association → linear correlation | 2 | chapters/chapter02.tex:108 |
| A4 | time features → charging-time features | 4 | chapters/chapter01.tex:21；chapter02.tex:106 |
| A5 | representational capability → representational ability（仅HI） | 5 | chapters/chapter01.tex:25、36；chapter04.tex:45 |
| A6 | kernel length → kernel size；short and long kernels → small and large kernels | 3 | chapters/chapter04.tex:156、158 |
| A7 | capacity fade curves → capacity degradation curves | 1 | chapters/chapter02.tex:23 |
| A8 | resource-limited → resource-constrained | 9 | chapters/abstract.tex:1；chapter01.tex:9、17、27、40；chapter04.tex:172；chapter05.tex:1、3 |

共涉及6个论文源文件。中英对照文件 `full-manuscript-bilingual.md` 的英文部分同步25处（表4的两处不在该对照正文内），中文部分不变；未覆盖对照文件中的其他既有差异。术语表追加作者确认条目，并区分HI的 representational ability 与模型的 representational capability。普通 capacity fade 保留。

## 核验

- 以修改前备份逐行重建允许的27处替换，与当前6个论文文件精确比对通过；没有其他文字、公式、数字、引用或命令变化。
- 对照英文的25处修改精确重建通过；其余内容（含中文）不变。
- `source-zh/`、`figures/`、`backmatter/`、`投稿资料/` 及 chapter03 的98个文件哈希全部不变。
- `build.ps1` 编译成功，PDF共37页；最终日志未发现未定义引用、缺字、Overfull/Underfull或LaTeX错误。原有图片ICC配置警告仍存在。
- 已渲染并查看PDF第1—10、12—14、21、29—32页，覆盖改动及相邻页面；文字、表格、换行未见本批引入的裁切、重叠或溢出。
- 投稿信只读检查发现1处 resource-limited；本次27处论文修改不包含投稿信，因此未改。

备份、逐项修改清单与核验结果：`build/a1-a8-20260916-151016/`（`changes.json`、`verification.json`、`protected-before.json`、`qa/`）。保留修改前当前文件作为备份，未从较早审查快照恢复论文。
