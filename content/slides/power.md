# What these things can actually do

## Not fixing your grammar.

Forty-five minutes at the frontier—before we touch a keyboard.

> Some of this is weeks old. Your own AI may not know it happened yet.

---

# You've been told what AI is for

Draft an email. Summarise a PDF. Tidy some prose.

Useful. Comfortable. **And a rounding error on what it can do.**

Here's the part nobody put in the newsletter.

---

# Exhibit A — competitive programming

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

---

# July 2026 — one year later

Same contest. The AI **sweeps both divisions.** No human wins a single one.

- Heuristics—the event humans held longest: **~7× the best human's score**
- The "Humanity Prevails Award," for anyone who could beat it: **unclaimed**

From "for now" to "unclaimed" took twelve months.

---

# And it wasn't a fluke

- **ICPC World Finals 2025** — the AI solves **12 / 12.** The human world champions got 11.
- **IOI 2025** — gold medal, roughly top 6 of 330.
- **Codeforces** — first time a *publicly available* model cleared every problem in a top-tier round.

> "It just memorised them." No—fresh problems, released at the start, no
> internet. The judges checked.

---

# Exhibit B — mathematics

Programming has a scoreboard. Fair enough.

Now the harder claim: these things are doing **new mathematics**—problems that
sat open for decades.

---

# An 87-year-old conjecture — disproved

The **Jacobian conjecture** (1939). Open for a lifetime of mathematicians.

**July 2026:** Harvard's Levent Alpöge points **Claude** at it. Back comes an
explicit counterexample—and a proof assistant confirms it is airtight.

> The model was **Claude.** The tool you're about to open.

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

Human *with* machine, not human *versus* machine.

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

His answer, only half-joking: humans probably have until about **2030.**

Maybe he's wrong. The striking part is that a serious person says it at all.

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

# Even the scoreboard can lie

FrontierMath—a benchmark built to be "too hard for AI."

It turned out **~42% of its problems had the wrong answer.** What caught the
mistakes? Another AI.

Verify the work. Verify the yardstick. Verify the hype—including mine.

---

# Exhibit C — your own bench

You know **lavaan**, the SEM workhorse. I rebuilt its engine from scratch in
**C++**: ~100,000 lines, **10–100× faster**, checked against lavaan
model-for-model. About **six weeks.**

And the rebuild kept throwing off new methods—**ten papers' worth.**

> I still can't hand-write C++. That's the point: the tool did the engineering.

---

# What I know — because I can check it

My field hands me a near-perfect verifier: a **simulation.** I know the truth,
because I generated the data.

So I quit proving ideas right *before* testing them. Build it, simulate it, keep
it only if it survives—**prove it later, if it earns the effort.**

> A failed simulation refutes a bad idea before lunch. That one fact reorders how
> I do research.

---

# What I don't know — and won't pretend to

Maybe the principle is bigger than statistics:

> The bottleneck moved from *producing* answers to *checking* them. Your cheapest
> honest check becomes your speed limit.

Does *your* field have that cheap check—a backtest, a pilot, a case that breaks
the argument? Or nothing at all?

**I honestly don't know. That's one of the more interesting questions in this room.**

---

# What stays yours

It will not do 100% of your work—and the missing piece is the piece you already
own.

## The ideas. The judgement. The responsibility.

The model is a superb executor of a good idea. It is not a reliable source of
one. And you are not short of ideas.

---

# One question should be nagging you

A machine that, underneath, only ever predicts the next word—

## how does *that* prove theorems?

That's the next fifteen minutes.
