# ai-label-paper: the key

A fictional marketing paper in progress, for the Marketing course (3 December
2026): the fallback for anyone without their own paper, the paper Jonas demos
on, and the paper in the sycophancy experiment. Built 24 October 2026.

```
Rscript scratch/examples/ai-label-paper/simulate.R   # data, by seed search (seed 20261350)
Rscript scratch/examples/ai-label-paper/numbers.R    # build/numbers.json
python3 scratch/examples/ai-label-paper/make.py      # courses/2026-12-marketing/props/ai-label-paper.zip
```

## The folder

```
ai-label-paper/
├── Nordmann_AI_label_v7.docx           the Word draft
├── Nordmann_AI_label_v7.pdf            the same, as PDF (5 pages)
├── FICTIONAL.txt
├── analysis/analysis.R                 the authors' script
├── data/prolific_export_2026-09-14.csv 640 rows, the current export
├── prereg/AsPredicted_118804.pdf       the preregistration
├── survey/survey-flow.txt              the Qualtrics flow
└── notes/from-Ola-2026-09-09.txt       the co-author's email
```

The study: 2 (label: "written by AI" vs. none) × 2 (scented candle vs. phone
charger), Prolific, US. H1 the label lowers purchase intention; H2 more so for
the hedonic product; H3 authenticity mediates (candle).

## Planted: visible in the PDF alone (the referees' view)

1. **Moderation from simple effects.** H2 is "supported" because the candle
   effect is significant (t(225) = −2.37, p = .018) and the charger's is not
   (p = .314). The interaction is never tested; in the draft's own data it is
   b = −0.19, t(472) = −0.94, p = .346. The preregistration names the
   interaction as the test of H2.
2. **H1 asserted without a test** ("across products, the label lowered purchase
   intention").
3. **Manipulation check before the dependent variables** (Procedure; survey
   flow). The preregistration says it comes after.
4. **Mediator measured after the outcome, causal language** ("authenticity
   explains").
5. **Low reliability called fine:** authenticity α = .56.
6. **Willingness to pay demoted to a footnote** because it was not significant.
7. **One product per category:** candle vs. charger differ in many ways besides
   hedonic vs. utilitarian.
8. **Exclusions:** "Following our preregistration, we excluded… We also
   excluded…": the sentence blurs which exclusions were preregistered.
9. **Anonymisation slips** (for building the submission package): names and
   e-mail on page 1, acknowledgements, the self-citation "In our earlier work
   (Nordmann & Nordmann, 2024)", two leftover comments ("[OLA: …]", "[KN: …]"),
   the file name, and the author field in the PDF and Word metadata ("Kari
   Nordmann, Ola Nordmann").
10. **A reference that doesn't exist:** Bergstrøm & Lind (2023), *Journal of
    Consumer Psychology*. Its DOI, 10.1002/jcpy.1399, belongs to an unrelated
    2024 paper (Dagogo-Jack, on temporal vs. social comparisons). The other 13
    real references were checked against Crossref on 24 October.

## Planted: needs the folder (the inside view, *Take it apart*)

11. **Exclusions beyond the preregistration.** The preregistration: attention
    check only. The script also drops speeders (< 120 s) and WTP > \$100 ("Ola,
    9 Sep"). On the current data:

    | Exclusions | N | Candle effect | Charger | Interaction |
    |---|---|---|---|---|
    | Authors' (script) | 545 | t(265) = −2.18, p = .030 | p = .279 | p = .461 |
    | Preregistered only | 601 | t(298) = −1.39, **p = .166** | p = .338 | p = .759 |

    With the preregistered exclusions, the headline effect is gone.
12. **The draft's numbers come from an older export.** The draft reports 560
    recruited and N = 476 (the export of 2 September; the commented-out line in
    the script); the data folder holds the 14 September export with 640 rows.
    Rerunning the script gives N = 545 and none of Table 2's numbers. The
    preregistration says 640; the draft says 560. Ola's email says so too.
13. **auth_3 is reverse-worded but not reversed** ("The description feels
    artificial"; the preregistration says reverse-score it). Reversed, α goes
    from .56 to .84 (draft data; .83 on current data). The mediation holds
    either way; the fix *helps* the paper.

Numbers for every version (draft, current with the authors' exclusions, current
with the preregistered exclusions and auth_3 reversed) are in
`build/numbers.json`.

## What a good outcome looks like

- **Referees (PDF only):** at least 1, 3 and 4; a good one asks for the
  interaction and the deviations from the preregistration.
- **Take it apart (folder):** 11 and 12 at least. 13 is the bonus, and it's good
  news for the authors.
- **The submission package:** every item in 9, including the PDF metadata.
