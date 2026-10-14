# Epoch AI snapshot — 20 September 2026

Source: https://epoch.ai/data/benchmark_data.zip, downloaded 20 September 2026.
Landing page: https://epoch.ai/benchmarks/use-this-data.
Credit: Epoch AI, *Capabilities & Benchmarking*. Data licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

- `eci_scores.csv`: complete index table from the archive.
- `frontiermath_tier_4_v2.csv`: three selected rows, otherwise unchanged, from
  that benchmark's run table. Includes settings, run IDs, dates and standard errors.
- `../../research/plot-capabilities.py`: generates the slide image from the
  index table, showing models released from 2023 onward. Labels are selected
  for audience familiarity; all models in that date range are plotted.

The index graph shows point estimates, not uncertainty intervals or a fitted
growth curve. Use it to discuss the broad change, not small differences in rank.

## Astra comparison

The benchmark-specific run table gives Astra `none` and Sol `max` the same
mean score, 0.8292682926829268. Astra `medium` scores 0.975609756097561.
The slide rounds to 82.9%, 82.9%, and 97.6%. The first two rows have standard
errors of about 5.95 percentage points; the third about 2.44.

The archive's separate `processed_data_for_eci.csv` associates a 0.976 Tier-4
score with Astra `none`, inconsistent with the benchmark-specific run table.
The slide uses the run table, with explicit settings and run IDs, rather than
that processed entry. No claims about statistical superiority between Astra
`none` and Sol `max` are made.

Epoch's evaluation allows written working and Python tool calls. A `none`
reasoning setting is not evidence of answering without intermediate work.
