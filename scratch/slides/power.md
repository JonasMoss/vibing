# What these things can actually do

## Not fixing your grammar.

Forty-five minutes at the frontier—before we touch a keyboard.

> Some of this is weeks old. Your own AI may not know it happened yet.

---

# Current AI's are strong

**Typical earlierer AI selling-points.**

* Draft an email. 
* Summarise a PDF. 
* Tidy some prose.

Useful. Comfortable. **And a rounding error on what it can do.**


---

# Exhibit A: Competitive programming

The Olympics of problem-solving: brand-new problems, a few hours, no internet,
a live scoreboard against the best humans alive.

For years, the clearest example of something AI was **not** good enough for.

---

# July 2025

At the AtCoder World Tour Finals, one human—**Psyho**—beats OpenAI's model
by a hair.

He posts:

> "Humanity has prevailed (for now!)"

Hold on to the *for now.*

![Psyho’s post after the 2025 final: “Humanity has prevailed (for now!)”](images/psyho-2025-tweet.png)

---

# July 2026 — one year later

Same contest. The AI **sweeps both divisions.** No human wins a single one.

- Heuristics—the event humans held longest: **~7× the best human's score**
- The "Humanity Prevails Award," for anyone who could beat it: **unclaimed**

From "for now" to "unclaimed" took twelve months.

![AtCoder World Tour Finals 2026 — final standings, the AI atop both divisions](images/atcoder-2026-standings.png)

---

# And it wasn't a fluke

- **ICPC World Finals 2025** — the AI solves **12 / 12.** The human world champions got 11.
- **IOI 2025** — gold medal, roughly top 6 of 330.
- **Codeforces** — first time a *publicly available* model cleared every problem in a top-tier round.

> "It just memorised them." No—fresh problems, released at the start, no
> internet. The judges checked.

![ICPC 2025 World Finals — final scoreboard](images/icpc-2025-scoreboard.png)

---

# Exhibit B: Mathematics

Programming has a scoreboard. Fair enough.

Now the harder claim: these things are doing **new mathematics**—problems that
sat open for decades.

---

# Navier–Stokes

**A Millennium Prize Problem. September 2026.**

OpenAI publishes a proof of finite-time blowup, with a Lean formalization.

**88 hours** to find the result. **17 more** to formalize it.

Internal research model; about 10,000 agents in the successful group.

[Paper, proof and account of the work](https://openai.com/index/navier-stokes-solution/)

---

# An 87-year-old conjecture — disproved

The **Jacobian conjecture** (1939). Open for a lifetime of mathematicians.

**July 2026:** Harvard's Levent Alpöge points **Claude** at it. Back comes an
explicit counterexample—and a proof assistant confirms it is airtight.

> The model was **Claude Fable 5.** A model (some of you) are about to open.

![Levent Alpöge announces the counterexample; Gowers reacts](images/jacobian-tweet.png)

---

# It wasn't a one-off

**Erdős' unit-distance conjecture**—open since 1946—**disproved** by an OpenAI
model, then verified and written up by a roomful of famous mathematicians.

Gil Kalai likens it to the 1976 computer proof of the Four-Colour Theorem.

> A genuine landmark, reached by a machine.

---

# Not one problem. Dozens.

Through 2026, AI systems have resolved **dozens of Erdős problems**—many checked
line-by-line by a proof assistant.

When one such proof landed, **Terence Tao**—Fields medalist—called it a
meaningful contribution and **extended it into new theory within a day.**

For now, the human still points—and extends.

---

# One for the empiricists in the room

The **Benjamini–Hochberg** procedure—the standard correction for multiple
testing, cited **130,000+ times**, used in every department here.

**July 2026:** GPT-5.6 finds a case where it *fails*—the false-discovery rate
creeps above the level you believed you controlled. It took about 90 minutes.

The statistician who ran it, honestly: it "combines known methods rather than
inventing new ones." True—and still remarkable.

---

# How fast this becomes ordinary

**2025:** an AI reaching Mathematical Olympiad **gold** was front-page news.

**2026:** a consumer chatbot did all six problems, one shot, in about an hour.

Barely a headline. That shrug is the most important thing on this slide.

---

# The people who would know are not calm

Timothy Gowers—Fields medalist—was asked whether the next Fields Medals might
be the last ones awarded to humans.

His answer: humans probably have until about **2030.**, but only due to institutional delay.

![Szegedy: “the last one.” Gowers replies: “…they’ll probably make it to 2030.”](images/gowers-2030.png)

---

# Now the catch that makes the rest usable

Everything so far is real. But not everything **announced** is real.

That same month, someone announced an AI *proof* of another famous problem—the
Cycle Double Cover conjecture.

Nobody has verified it. It may simply be wrong.

---

# Why you could trust the earlier ones quickly

A **counterexample** you can check in minutes: put in the numbers, see it break.

A **proof** of a hard theorem you cannot: it needs experts, months, sometimes a
computer of its own.

> The *shape* of a result tells you how fast to trust it.

---

# Astra on FrontierMath

**Tier 4 v2 — research-level mathematics**

| Model | Reasoning setting | Correct |
|---|---|---|
| GPT-5.6 Sol | max | 82.9% |
| GPT-6 Astra | none | **82.9%** |
| GPT-6 Astra | medium | **97.6%** |

`none` disables the dedicated reasoning mode. Written working and Python are allowed.

[Epoch AI run data · retrieved 20 September 2026](https://epoch.ai/benchmarks/use-this-data)

---

# Where I track capabilities

## [epoch.ai](https://epoch.ai/benchmarks)

**My recommended starting point. The best benchmark aggregation, in my view.**

Capability trends → individual benchmarks → model settings and example tasks.

---

# The Epoch Capabilities Index

![Epoch capability scores by model release date, 2023–September 2026](images/epoch-eci-2026-09-20.png)

A common scale across many tests. Index points are not percentages.

[Explore the index](https://epoch.ai/eci) · [How it is constructed](https://epoch.ai/data/eci-documentation)

---

# Read one benchmark closely

- What does an actual question look like?
- Which model, settings, tools and test version?
- Who checked the answers?

[Open FrontierMath's example problems](https://epoch.ai/frontiermath/tiers-1-4/benchmark-problems)

---

# Sometimes the answer key is wrong

**FrontierMath:** the June 2026 update addressed errors in **42% of problems**.

**HLE-Physics:** expert review raised Sol's score from **47.3% to 78.7%**.

The physics result uses corrected, retained questions; metric: mean@4.

[Epoch's correction](https://epoch.ai/benchmarks/frontiermath-tier-4-v2) · [Physics audit, September 2026](https://arxiv.org/abs/2609.13009)

---

# Exhibit C: Security

Programming has a scoreboard. Maths has proofs.

Now the uncomfortable one—these systems find **real holes in real software.** And
once, one **walked through a door it found.**

---

# The warnings were on the record

- **Nov 2024** — Google's "Big Sleep" agent finds a real **zero-day in SQLite**,
  caught before it shipped. First of its kind.
- **Aug 2025** — DARPA's **AI Cyber Challenge**: autonomous systems patch real code
  across **54 million lines** and surface **18 genuine zero-days.**

Not a lab flexing—a government contest, many teams, checkable.

---

# Bugs nobody had found in decades

Anthropic points its ungated cyber model—**Mythos**, the sibling of the **Fable**
you'll open today—at software, with one line: *"find a vulnerability in this program."*

Out come long-buried real flaws: a **27-year-old** bug in OpenBSD; a **17-year-old**
remote-takeover hole in FreeBSD (now a filed CVE).

> Honest floor: Anthropic grading its own homework—and **over 99% still unpatched.**
> So "thousands" is *their* count, not yet the world's.

---

# July 2026 — it walked out the door

In an OpenAI cyber test **with the safety brakes deliberately off**, a model found a
zero-day in its *own* sandbox, reached the open internet, and broke into **Hugging
Face's** servers—lifting the test's answer key.

> "A containment failure with the safeties turned off."
> — Dan Guido, Trail of Bits

A real break-in at a real company. **Not** an AI escaping unprompted—a red-team eval,
brakes off, a sandbox that wasn't. Both halves are true.

---

# So why should this room care?

The skill that digs out a 27-year-old bug is the skill that **hardens your systems.**
It cuts both ways—and it's getting sharper fast.

> And notice the pattern: the *scariest* headline—"AI escaped!"—was the overstated
> one. Verify the hype. Especially the frightening kind.

---

# Exhibit D: 
You know **lavaan**, the SEM workhorse. I rebuilt its engine from scratch in
**C++**: ~100,000 lines, **10–100× faster**, checked against lavaan
model-for-model. About **six weeks.**

And the rebuild kept throwing off new methods, about **ten papers' worth.**.

> I still can't "really" hand-write C++. That's the point: the tool did the engineering.

---

# What I know — because I can check it

My field hands me a near-perfect verifier: a **simulation.** I know the truth,
because I generated the data.

So I quit proving ideas right *before* testing them. Build it, simulate it, keep
it only if it survives—**prove it later, if it earns the effort.**

> A failed simulation refutes a bad idea before lunch. That one fact reorders how
> I do research.

---

# One field over: the soft sciences

Can it do social science? Partly, yes.

**July 2026 (Nature):** GPT-4-class models predicted the results of ~70 US survey
experiments at **r ≈ 0.85**—and **0.90** on studies held out of training. On par
with teams of human forecasters.

> But the catch is the yardstick: "right" here means *correlates with noisy human
> data*, not *compiles or fails.* A softer check—so you trust the score less.

---

# Reconstructing Umberto Eco's library

Videos + photographs + catalogues → an explorable 3D library.

Fable 5.1 identified roughly **5,000 books**. The map marks uncertainty.

Ethan Mollick's demonstration, **18 September 2026**.

[Explore the library](https://eco-library-map.netlify.app/) · [Mollick's account](https://www.oneusefulthing.org/p/the-overhang)

---

# Build the research tool you need

**Concord:** software for comparing human and AI coding of qualitative data.

Mollick reports **9½ hours** of agent work from a detailed specification,
followed by his inspection and corrections.

[June 2026 account](https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos) · [Inspect the code](https://github.com/emollick/concord)

---

# What I don't know — and won't pretend to

Maybe the principle is bigger than statistics:

> The bottleneck moved from *producing* answers to *checking* them. Your cheapest
> honest check becomes your speed limit.

Does *your* field have that cheap check—a backtest, a pilot, a case that breaks
the argument? Or nothing at all?

**I honestly don't know. That's one of the more interesting questions in this room.**

---

# What stays yours (?)

What remains for me / you?

* Ideas,
* Judgement,
* Responsibility,
* Finishing prose and signing off.

I wouldn't hold my breath though. 

---

# One question should be nagging you

A machine that, underneath, only ever predicts the next word—

## how does *that* prove theorems?

That's the next five minutes.
