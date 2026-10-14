# examples/grades — the "draft the results email" demo input

A **synthetic**, filled-in grade sheet for the same Nordic Style course as the
`decrap-me` example (`ELE37911 Business Intelligence with Power BI`), scored by
group. Safe to commit and hand out — no real students, no real marks.

- `scores.csv` — plain text, opens anywhere; the robust choice for a live demo.
- `scores.xlsx` — the same data as a real Excel workbook, because that is where
  grades actually live. Reading it shows the agent handles Office files, not
  just plain text.

Both are generated from one table by `scratch/examples/scripts/make-scores-example.py`
(standard library only — no `openpyxl`, no `pandas`). Edit the `POINTS` /
`COMMENTS` tables there and re-run to change the numbers.

## What the demo does

Point the agent at this folder and ask it to **read the scores and draft a
results email** — a short summary plus a per-group table, straight into a Gmail
draft. Nothing leaves the machine except the draft you choose to send.

> Read scores.xlsx and draft an email to the course coordinator: one short
> paragraph on how the cohort did, then a table of group / points / grade.
> Flag anyone who failed. Draft only — don't send.

The honest punchline: the connector can **draft** but not send, so you review
and hit send yourself. Story carries from Day 1 — "you cleaned this folder, you
graded it, now email the results" — all in one Nordic Style world.

The grade scale used: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, E ≥ 50 (lowest pass),
F below 50.
