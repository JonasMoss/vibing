# Instructor key — "the interval nobody reports" (Day 2, 14:30)

## 🎤 The live card — everything you need while driving

*Glance at this; the rest of the file is reference. This demo is built to be
improvised.*

**The hook.** *"Everyone here has reported an R². Hands up if you've ever reported a
confidence interval for it."* → no hands → *"Why not? It's been recommended for
years. There's just no button for it."*

**Ask 1.** Simulate a survey study — satisfaction ~ salary + autonomy + commute,
correlated predictors, n = 100. Fit it, get partial R² for autonomy, bootstrap a 95% CI.

> Expect ≈ **0.12**, **p ≈ 0.0005**, CI ≈ **[0.02, 0.27]**. Exact numbers vary with
> the seed — *the shape is the point*: significant, and an order of magnitude wide.

**Ask 2.** Now check it: simulated studies, known truth, how often does the 95%
interval actually contain it?

> **normal 94.1% · heteroskedastic 95.3% · heavy-tailed 90.3%.** Runs in seconds.
> Heavy tails are the normal condition in business data.

**Ask 3 — the one that shows what these things can really do.** Don't resample:
**derive**. Ask for an analytic interval (Fisher z on the partial correlation), then
ask it to correct that for non-normality using the kurtosis of the residuals. Then
verify by simulation.

> Under t₃: bootstrap **90.3%**, plain analytic **91.1%**, kurtosis-corrected
> **97.9%**. The derivation beats the brute force.

**Room-driven variations** (all one-liners): bigger n · more collinear predictors ·
overall R² · true effect zero · BCa and exact noncentral-F, do they agree?

**Their turn.** *"What do you report without an interval?"* → resample, redo, spread.

**If it breaks:** `partial-r2.R` and `coverage-check.R` in this folder both run in base
R, no packages. `MBESS` is **not** installed — don't ask for it live.

**Timing note:** the bootstrap is fast (2000 reps ≈ 30 s). The *noncentral-F* version
is the slow one — root-finding per replication. Don't put that in a coverage loop on
stage.

---

A live demo where the agent does **methodology**, not admin. Roughly 45 minutes,
I-drive for the first half, then the room joins in.

Reference implementation: `partial-r2.R` (base R, no packages). **Don't hand it out** —
the whole point is that the agent writes it live from one sentence of English. It's
here so you can check the output against something known, and as a wifi-failure
fallback.

---

## Why this and not p-hacking

The optional-stopping demo is played out, and it tells a "science is broken" story.
This one is **constructive**: here's a number you already report, and here's the
uncertainty around it that you almost certainly didn't report.

**Don't claim this is news.** It isn't, and some of the room will know it. Partial R²
is partial η² in regression clothing; interval estimates for it are textbook
(Steiger & Fouladi, Smithson; `MBESS` has done this in R for two decades), and APA
reporting guidance has asked for effect sizes *with intervals* for years.

That makes the story **better**, not weaker:

> The methods existed. The recommendation existed. It still didn't happen — because
> it wasn't one click.

The gap here was never conceptual, it was **friction**. Which is exactly the gap these
tools close, and a far more honest claim than "look at this thing nobody knew."

## The hook

> Everyone here has reported an R², or written "this variable explains 8% of the
> variance." Hands up if you have ever reported a **confidence interval** for it.

No hands. Then the real question:

> Why not? It's been recommended for years and implemented for two decades. There's
> just no button for it in SPSS, and the formula is awkward enough that nobody
> bothers.

That's the whole gap. Not ignorance, not disagreement — **friction**. And the friction
is what just disappeared.

*(If someone points out that partial R² is partial η² and that Steiger and Smithson
sorted this out long ago: agree enthusiastically. That's the point — the statistics
was never the bottleneck.)*

## The ask (one sentence, live)

> Simulate a small survey study — job satisfaction predicted by salary, autonomy and
> commute, with correlated predictors, n = 100. Fit the regression, compute the
> partial R² for autonomy, then bootstrap a 95% confidence interval for it. Show me
> the code.

## What comes back (verified — these are real numbers from `partial-r2.R`)

```
partial R2 (autonomy) = 0.119   -> "explains 11.9% of the remaining variance"
t = 3.59, p = 0.0005            -> comfortably significant
bootstrap 95% CI      = [0.024, 0.273]  ->  [2.4%, 27.3%]
the interval is 2.1 times as wide as the estimate itself
```

**Sit on that for a second.** `p = 0.0005` — this would sail through any review. And
the honest interval runs from **2.4% to 27.3%**: an order of magnitude. You are very
confident the effect isn't zero, and you have almost no idea how big it is.

> **Significance and precision are different things.** We report the first and stay
> quiet about the second — because one had a button and the other didn't.

## "What kind of interval is that?" — have this ready

Someone statistical will ask, and the honest answer is that the script uses the
*crudest* option: a **nonparametric percentile bootstrap with case resampling** —
resample rows with replacement, refit both models, take the 2.5/97.5 empirical
quantiles. Not the delta method, not normal theory.

Case resampling (rather than resampling residuals) is right here because the
predictors are random — survey data, not a designed experiment.

**The fair objection:** percentile is the weakest bootstrap, and partial R² is
bounded at 0, right-skewed and biased upward — exactly where percentile intervals
misbehave. So it's worth knowing that **the punchline survives the better methods.**
Same data, n = 100 (all verified):

| method | 95% CI | width |
|---|---|---:|
| percentile bootstrap | [0.024, 0.269] | 0.245 |
| BCa (bias-corrected, accelerated) | [0.022, 0.263] | 0.241 |
| noncentral-F, exact under normality | [0.024, 0.243] | 0.219 |

The bias is measurable and small: bootstrap mean 0.1277 vs estimate 0.1186, **+0.009
upward**. It matters more at n = 50, near that 0.001 lower bound — treat the small-n
row as illustrative rather than precise.

**And this is a demo beat, not just a defence.** Ask for all three live:

> Now give me the BCa interval, and the exact noncentral-F one. Do they agree?

Three intervals in thirty seconds, and a real conversation about which you'd report —
that used to be an afternoon with Steiger and Fouladi's paper open on the desk.

## Does more data rescue you? (verified)

| n | partial R² | 95% CI | width |
|---:|---:|---|---:|
| 50 | 0.077 | [0.001, 0.263] | 0.260 |
| 100 | 0.087 | [0.011, 0.216] | 0.201 |
| 200 | 0.087 | [0.027, 0.175] | 0.147 |
| 500 | 0.079 | [0.040, 0.132] | 0.091 |
| 1000 | 0.087 | [0.057, 0.121] | 0.065 |

Two things to say out loud:

- At **n = 50** — an utterly normal study — the lower bound is **0.001**. You'd write
  "explains 7.7% of the variance" and you could not rule out *essentially nothing*.
- Even at **n = 1000**, a big survey, the interval still spans **5.7% to 12.1%** —
  better than a factor of two, and no better than that.

## The escalation — "does the interval actually work?" (optional, ~10 min)

*Run this when the room is with you. It is the difference between automating a
known method and **probing an open question** — and the second is what the course is
actually about.*

Everything so far reproduces textbook statistics faster. This next question is not in
the textbook, and the answer is genuinely unsettled.

The setup is simple enough for anyone:

> We built an interval. Does it work? Simulate 400 studies where we *know* the true
> value, and count how often the 95% interval actually contains it.

**Verified** — pairs bootstrap, n = 100, **2000 replications**, B = 500:

| data | true partial R² | coverage of the nominal 95% interval |
|---|---:|---:|
| normal errors | 0.0827 | **94.1%**  (SE 0.5pp) |
| heavy-tailed (t₃) | 0.0816 | **90.3%**  (SE 0.7pp) |
| heteroskedastic | 0.0365 | **95.3%**  (SE 0.5pp) |

Read it out loud:

- **Normal data: it works.** 95% means 95%.
- **Heteroskedasticity: also fine.** Which makes sense — resampling whole rows doesn't
  care that the variance changes. Nice, and worth saying: the crude method is
  *robust* here where the "exact" one leans on assumptions.
- **Heavy tails: it breaks.** Your "95%" interval is really about a **90%** interval,
  and nobody told you. Then say the part that matters in this building: **heavy tails
  are the normal condition in business data** — returns, incomes, sales, firm sizes,
  claim amounts.

**The honest punchline:** there's no clean off-the-shelf fix for a heavy-tail-robust
interval on this quantity. That isn't a gap in the audience's education — it's a gap
in the literature, found in **ten minutes and one prompt.**

> You are one sentence away from checking whether the method you rely on actually
> works on data like yours. That is a genuinely new thing to be able to do on a
> Tuesday afternoon.

### The real payload: stop resampling, start deriving

**A bootstrap undersells these tools badly.** "Refit it ten thousand times" is brute
force — impressive to a novice, and conceptually trivial. The thing a person *can't*
do in an afternoon is the **analytic** work: write the estimator as a ratio of
quadratic forms, take moments, correct them for non-normality, match to a reference
distribution. That's a day with the references open. It's also what the model does in
about a minute.

So make that the climax:

> Don't resample. Derive an analytic interval for the partial R² — go through the
> partial correlation and Fisher's z. Then correct it for non-normal errors using the
> kurtosis of the residuals. Then check both by simulation.

**Verified** (n = 100, 3000 replications, coverage of a nominal 95% interval):

| errors | true partial R² | z, normal theory | z, kurtosis-corrected | pairs bootstrap |
|---|---:|---:|---:|---:|
| normal | 0.0827 | 94.8% | 95.4% | 94.1% |
| t₈ (moderate tails) | 0.0831 | 94.6% | 96.7% | — |
| t₃ (heavy tails) | 0.0820 | **91.1%** | **97.9%** | **90.3%** |

**The derivation beats the brute force.** Under heavy tails the bootstrap undercovers
(90.3%) and so does the uncorrected analytic interval (91.1%) — the kurtosis
correction is the only thing that fixes it. It overshoots to 97.9%, i.e. conservative:
wider than strictly needed, erring in the direction that doesn't get you a false
finding.

Script: `analytic-interval.R`.

### The bug that simulation caught — tell this one

The first version of the analytic interval scored **84.8%** under t₃, *worse* than
doing nothing. The correction wasn't wrong; the implementation was.

The interval is built on the correlation scale and then squared to get R². If the
correlation interval **straddles zero**, the squared interval's lower bound must be
**0** — not the smaller endpoint squared. Widening the interval made it straddle zero
more often, so the bug bit harder exactly when the correction was working hardest.

Nothing about the output looked wrong. The numbers were plausible, the code was
short, the maths was right. **Only the simulation caught it.**

> Derive, implement, *verify*. The middle step is where the errors live, and the third
> step is not optional — it is the thing that makes the first two safe to trust.

That is the whole research loop, run in ten minutes, in front of the room.

### Honest limits, worth one sentence each

- The correction used here is crude — inflate the variance by `1 + γ̂₂/2`. A proper
  Satterthwaite-style moment match would do better; that's the actual open work.
- t₃ has **infinite** kurtosis, so the sample kurtosis it relies on is unstable. It
  still helps — which is interesting in itself.
- 97.9% is conservative, not correct. **Getting it to land on 95% under heavy tails is
  a genuinely unsolved problem for this quantity** — and now everyone in the room has
  the machinery to attack it.

### A cautionary tale you should probably tell

The first version of this simulation used 400 replications and reported
heteroskedastic coverage of **97%** — "the bootstrap turns conservative." Re-running
with 2000 replications gave **95.3%**. The 97% was noise, and the story built on it
was wrong.

Two lessons for the price of one, and the second is the better one:

1. **Cheap simulations are cheap to get wrong.** Monte Carlo error at 400 reps is
   about ±1.1pp per point, so a 2pp "finding" is nothing.
2. **The fix was to run it again, bigger — which cost thirty seconds.** The old
   defence of a small simulation was that a big one was expensive. It isn't any more.

*(If you want a live demonstration that simulation beats intuition including a
statistician's: I predicted "exact is fragile, bootstrap is robust." Half right at
best — heavy tails break the bootstrap too.)*

**Also worth one sentence:** the heteroskedastic row has a different true value
(0.0365 vs 0.083) because changing the error structure changes the population
quantity. *The thing you're estimating moved.*

## Then let the room drive (~10 min)

Every variation is a one-line change. Take suggestions and re-run live:

- *"What if n were 500?"* — narrows, but less than anyone guesses.
- *"What if the predictors were more correlated?"* — widens sharply. Multicollinearity
  made visible, without a lecture on VIF.
- *"What about the overall R², not partial?"*
- *"What if the true effect were zero?"*
- *"Use the exact noncentral-F interval instead of the bootstrap — do they agree?"*

**This is the payload, and say it explicitly:** a methodological question that used to
mean finding a paper with the right formula, or paying a research assistant for a
week, is now a sentence — and you get the answer before the coffee cools.

## Their turn (~15 min) — the generalization

> **What do you report without an interval?** Let's get one.

Nearly everyone has something: Cohen's d, a mediation or indirect effect, Cronbach's
alpha, a difference in model fit, a marginal effect, an elasticity, a predicted
probability, a rank, an index score.

The move is always the same, and it's worth writing on the board:

> **Resample the data. Redo the whole calculation. Look at the spread.**

If you can compute a number from a dataset, you can bootstrap an interval for it.
That's it. That's the technique.

## Where this connects

- **Day 1's "leave a trail":** the simulation script *is* the documentation of what
  you did. Same idea, harder problem.
- **The POWER deck (Exhibit D):** simulate first, prove later. This is that, at a
  scale they can run themselves.
- **Honest framing to keep:** the bootstrap is not magic and not always the right
  interval — small samples and bounded quantities like R² are exactly where it can be
  wobbly. Say so, then say the useful part: **a rough interval you actually computed
  beats a point estimate you reported alone.**

## If someone asks "so should I report this?"

Yes — and you can say it without hedging, because you're not proposing anything new.
Reporting effect sizes with intervals is long-standing advice. The only thing that
ever stopped it was that nobody had twenty minutes to write the bootstrap.

You just watched it take forty seconds.

> **Not reporting a confidence interval never meant the interval didn't exist.** It
> meant nobody computed it. That excuse is gone.
