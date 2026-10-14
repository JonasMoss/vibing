# Capabilities deck — review, 20 September 2026

Source: `content/slides/power.md`. The starting version had 27 slides, intended
for 45 minutes. Additions are now integrated; compaction is still deferred.
This is an update pass, not a fresh verification of every existing claim.

## Starting sequence (before this update)

- 1–2: the audience is underestimating these tools.
- 3–6: competitive programming, especially the 2025 → 2026 AtCoder contrast.
- 7–16: mathematics, followed by verification and benchmark quality.
- 17–21: security capabilities and incidents.
- 22–26: Jonas's research, simulation, social science, and human judgement.
- 27: transition to how models work.

## Author direction from this review

- Navier–Stokes is the most important addition.
- Astra at reasoning effort `none` on FrontierMath is another priority.
- Include enough benchmark literacy for participants to follow progress themselves.
- Epoch is Jonas's recommended landing page for benchmarks and capability
  tracking: in his view, the best aggregator. Include its index and explain
  what the scale means.
- Use little slide text. Compact exhibits and rewrite the existing prose later;
  the current prose is too recognizably AI-written.

## Earlier editorial suggestions — deferred

Keep the ambitious opening. Bring Jonas's own experience forward: slide 22 is
late for the first substantial connection between frontier capability and the
work a participant might undertake. Then use the frontier examples to expand
their sense of what is possible.

Choose the strongest examples rather than extending the talk with every new
result. The security section currently gets five slides; consider whether some
of that time would do more for this audience as a research-workflow example.

The opening two slides need a prose pass. Slide 22 has an unfinished heading.
Three evidence screenshots are still missing. Existing claims need their own
source checks as we review the corresponding slides.

## Priority additions: Navier–Stokes and benchmarks

**Navier–Stokes — 8 September.** OpenAI reports a solution of the Millennium
problem via finite-time blowup with smooth external forcing (statements C/D),
and publishes a paper and Lean formalization. Its account describes an internal
model stronger than Astra, roughly 10,000 concurrent agents in the successful
group, 88 hours to the result, and another 17 hours for Lean formalization and
verification using Astra. Put the mathematical achievement first. Keep the
model, scale, and precise formulation in instructor notes. This review checked
the announcement; it did not independently check the proof or establish prize
acceptance. The history also includes Alpöge and Buckmaster's related work;
do not erase that contribution when preparing the final account.

Source: https://openai.com/index/navier-stokes-solution/

**Astra with reasoning effort `none` — now verified and integrated.** Epoch's
downloaded Tier-4 v2 run table gives Astra `none` and Sol `max` 82.9%, and Astra
`medium` 97.6%. The selected rows, IDs and standard errors are preserved in
`links/epoch-2026-09-20/`. That folder documents an inconsistency in the archive's
separate ECI processed table; we use the benchmark-specific run table.
Epoch's methodology permits written working and Python; `none` must not be
described as answering instantly without working or tools.

Sources:
- https://epoch.ai/models/gpt-6-astra
- https://epoch.ai/benchmarks/frontiermath-tier-4-v2
- https://epoch.ai/benchmarks/use-this-data

**Epoch Capabilities Index.** Composite scale fitted across overlapping
benchmarks, intended to track progress even as individual tests saturate.
Possible teaching sequence: show the time trend, locate a familiar older model,
then open one component benchmark and an actual task. Explain that the index
is neither percentage correct nor the percentage of a professor's work an agent
can do. Use it to notice changes worth trying on one's own work.

Source: https://epoch.ai/data/eci-documentation

Integrated as a recommendation slide, a dated index scatterplot, and three
questions for reading a benchmark. Data and plotting provenance live in
`links/epoch-2026-09-20/`; rebuild with `python3 scratch/research/plot-capabilities.py`.

**Benchmark errors can hide capability.** Epoch's June v2 update addressed errors
in 42% of FrontierMath problems. The existing deck calls all of these wrong
answers; the slide now uses the supported wording "errors in problems".
A September physics audit supplies a second concrete example:
GPT-5.6 Sol's HLE-Physics mean@4 rose from 47.3% to 78.7% after expert correction
and filtering. These scores concern reviewed/retained subsets, not a clean
before/after on an unchanged full benchmark. Wrong keys, faulty grading, and
underspecified questions are separate failure sources.

Sources:
- https://epoch.ai/benchmarks/frontiermath-tier-4-v2
- https://arxiv.org/abs/2609.13009

## Mollick: humanities and social science

**18 September, The Overhang — integrated.** Mollick's reconstruction of Eco's
library gives the humanities a concrete artifact to explore. He reports using
Fable 5.1 to combine videos, photographs and catalogues; uncertainty is marked.
The public map says its geometry is estimated. Present this as a demonstration,
not an independently validated historical reconstruction. The article's wider
argument is that existing capabilities are underused and subject expertise helps
people commission and assess ambitious work.

Source: https://www.oneusefulthing.org/p/the-overhang
Demo: https://eco-library-map.netlify.app/
Code: https://github.com/emollick/eco-library

**9 June, What it feels like to work with Mythos — integrated as an older,
directly relevant example.** Mollick describes Concord, software for calibrating
human and AI coding of qualitative material. He reports 9½ hours of agent work
after specification, then inspection and corrections. This supports a concrete
research-tool example; the repository has not been validated in this review.

Source: https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos
Code: https://github.com/emollick/concord

**31 August, Agency and Agents — further reading.** Links to Mollick and
colleagues' July product-idea study. The abstract reports higher purchase-intent
ratings but reduced novelty and diversity, and ways to broaden the ideas.
Keep as a candidate for marketing/innovation; the models and experimental dates
need a full-text check before using it as evidence of September capability.

Sources:
- https://www.oneusefulthing.org/p/agency-and-agents
- https://arxiv.org/abs/2607.27553

## Other candidates, primary sources checked today

**Fermat formalization — announced 4 September.** Anthropic reports that a team
of Claude agents completed a Lean formalization in 11 days, with occasional
human guidance. The work follows an existing proof; the achievement is making
it fully computer-checkable. The report links the proof and a theorem-statement
comparator, and includes Kevin Buzzard's assessment. It used an internal model
roughly comparable to Fable 5.1, a specialized coordination platform, and about
six billion output tokens. Good candidate for the mathematics-to-verification
transition. We have read the report, not independently rebuilt the proof.

Source: https://www.anthropic.com/research/formalizing-fermats-last-theorem

**AI doing AI research — September report, August measurements.** Anthropic's
internal index places 26% of its AI R&D at the level where Claude completes most
of a task from a high-level prompt under human supervision. More than 90% is at
least collaborative. The index uses model-assisted task classification and
ratings; these are company-reported measurements. Good candidate for showing
that substantial research execution is already being delegated.

Source: https://www.anthropic.com/institute/measuring-pace-of-ai-development

## Preview workflow

- Build the static site and slides: `npm run build:pages`.
- Open `_site/slides/power.html` for the standalone capabilities deck.
- For a local site: `npm run dev`, then `http://localhost:3000/slides/power`.
- Arrow keys move between slides; `F` toggles fullscreen.
- The current dev command builds once. After source edits, stop and restart it.
- Markdown `---` separators define slides; shared appearance is in
  `site/styles.css`, and rendering is in `scripts/build-site.mjs`.
