# Grievance answers — instructor prep for Day 3, 14:30

**What this is for.** On Day 1 at 15:25 you opened the floor and parked the
worries. This block pays that debt. You promised answers on Friday; this file is
so you can give them without improvising.

**Verification tiers** (same convention as `capabilities-evidence.md`):
✅ independently verified · 🟡 real but company/self-reported · ⚠️ weak or
contested evidence · ❌ don't say it.

---

## How to run it (45 min)

1. **~5 min · Read the parked list back.** Literally read out what they said on
   Wednesday. Naming their own words buys you the room; it proves you weren't
   just managing them.
2. **~15 min · Answer only the ones they actually raised.** Do not deliver all
   five. Three answered properly beats five skated over.
3. **~10 min · The live hallucination demo** (below).
4. **~15 min · The routine, then open floor.**

**The stance for the whole block:** concede fully where it's true, push back hard
where the *proposed remedy* is worse than the problem. A block that concedes
everything is mush and they'll smell it. One that dismisses everything loses the
skeptics you spent three days earning.

**Each answer below has the same shape:** what's true → where the received view is
wrong → the move they can make Monday.

---

## 1. "Students will cheat"

**Concede, immediately and without hedging.** Yes. They already do. Yes, it
writes a decent undergraduate essay.

**Push back on the remedy, not the worry.** The instinct is detection. Detection
does not work, and at *this* school it is actively dangerous.

> ✅ **Liang et al. (2023), "GPT detectors are biased against non-native English
> writers," *Patterns* 4(7), 100779.** Seven commercial detectors, two corpora.
> More than **half** of TOEFL essays by non-native English speakers were
> misclassified as AI-generated. Accuracy on US eighth-grade essays was near
> perfect. Proposed mechanism: low perplexity — non-native writing has less
> lexical variability, which is exactly what the detectors score.
> <https://www.sciencedirect.com/science/article/pii/S2666389923001307>

Say the BI-specific part out loud: **a large share of our students write English
as a second language.** A detector deployed here does not fail randomly. It fails
in one direction, against one group, on a charge that is close to unfalsifiable
for the accused. That is not a fairness abstraction; it is a formal-complaint
generator.

**The move.** They spent Friday morning generating a subtly-wrong student answer.
They have now seen this from the grading side. So the question is not "how do I
catch it" but **"what is this assignment actually measuring, and does that
survive?"** Three honest options, and they should pick per assignment:

- **Move it into the room** — oral, in-class, defence. Expensive, unambiguous.
- **Assess the process** — drafts, decisions, a log. Fits what the whole course
  has been about: leave a trail.
- **Raise the bar and let them use it** — if the tool is allowed, the interesting
  question becomes what they did *with* it.

**The line, if you want one that bites:**
> If an assignment can be completed by a language model in thirty seconds, the
> assignment was probably not measuring what you hoped it measured.

Deliver that once, and don't gloat about it — half the room has such an
assignment and they know it.

---

## 2. "It makes things up"

**Concede: true, and it does not fully go away.**

**But they have already seen the useful version of this.** Thursday morning, the
garden of forking paths. They watched an agent invent a journal and a DOI for a
paper that does not exist — and then they caught it in about fifteen seconds.

**The reframe that matters: the rate is not uniform.** Closed-book recall of a
specific citation is close to the worst case you can construct. An agent that
retrieves, and hands you a DOI you can resolve, is a different regime. They spent
Thursday in the second regime on purpose.

**The move — checks that cost less than the task, or nobody does them:**

- Does the DOI resolve, and to the thing it claimed?
- **Open the file it says it downloaded.** (`nature.com/articles/XXX.pdf` returns
  HTTP 200 with HTML — the agent saves a login page as `.pdf` and reports
  success. See `examples/references/README.md`.)
- Ask: **"what did you *not* check?"** and **"what would change your answer?"**

**The line:**
> You have a research assistant who is fast, tireless, and occasionally
> confabulates. That describes every research assistant you have ever had. You
> already know the answer: you check their work.

---

## 3. "It will deskill us — and our students"

**This is the strongest grievance in the list. Say so.** Do not treat it as the
same kind of object as the energy question. If you wave this one away you
deserve the room you get.

**Be honest that the evidence is early and thinner than either side wants:**

> ⚠️ **Gerlich (2025), SBS Swiss Business School.** Negative correlation between
> self-reported AI use and critical-thinking scores, strongest among younger
> participants. **Correlational, heavily self-report.** Reverse causation and
> selection are wide open. Do not present it as a causal finding.

> 🟡 **MIT Media Lab (June 2025), "Your Brain on ChatGPT."** EEG during essay
> writing; LLM users showed weaker neural connectivity, and did worse when later
> asked to write unaided. **Preprint, small sample, one artificial task.**
> Suggestive, widely over-reported, not decisive.

Saying that out loud *is* the lesson — you are modelling, in the verification
block, the refusal to weaponise weak evidence that happens to support you.

**The move — the distinction that actually travels:**

> The deskilling risk is highest exactly where the skill **is** the point, and
> lowest where the skill was always **incidental**.

- A student learning to construct an argument: **the struggle is the learning.**
  Offload it and you have destroyed the thing you were trying to produce.
- A professor hand-formatting a bibliography: the skill was never the point.
  Nobody is mourning it.

Then turn it on them: *which of your own skills are load-bearing, and which were
always incidental?* People are usually startled by how short the first list is.

**The honest residual — do not paper over it.** For students this is live,
unsolved, and it is a **course-design problem that belongs to the teachers in
this room.** No vendor is going to solve it for them. That concession is the
credible thing to end on.

---

## 4. "The energy cost is obscene"

**This is where the room is most miscalibrated, in both directions.** Being
straight here is nearly free credibility, because half of it cuts against me.

**Part one — the individual query is not the problem.**

> ✅ **Epoch AI:** a typical GPT-4o query ≈ **0.3 Wh** — an LED bulb or a laptop
> for a few minutes. The widely-repeated **3 Wh** figure is roughly **10× too
> high**. A US household uses **>28,000 Wh a day**.
> <https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use>

**Part two — and this is the part I have to say, because it is about what I just
taught you.** That figure is for a short chat message. It is not what we did this
week.

> ✅ Same source: **~2.5 Wh** at 10,000 tokens of input, **~40 Wh** at 100,000.
> Reasoning models generate ~2.5× more tokens than GPT-4o.

Long context and agentic loops are the **expensive end** — plausibly 50–100× a
chat message. The workflows in this course are that end. Say it plainly; do not
let them find out later that the caveat pointed at me and I skipped it.

**Part three — the aggregate is the real story, and it is a real story.**

> ✅ ChatGPT's ~1 billion daily messages ≈ **12.5 MW continuous.** Data centres
> used ~**485 TWh** in 2025 (~1.5% of global electricity). Credible projections
> have AI approaching ~10% of US electricity by 2030.

**The move.** Separate the guilt from the question:

> Your individual use is a rounding error. The buildout is a genuine policy
> question. Declining to use the tool is not an environmental strategy — it is an
> opt-out from the conversation, and it costs the people who would have used it
> well.

Do not moralise past that. A room of professors will argue with virtue and nod at
arithmetic.

---

## 5. "Who owns any of this?"

**The move is to split one question into three.** People mash them together and
then feel helpless about all of them.

**(a) Was the model trained on copyrighted work without permission?**
Litigated, unresolved, moving. **Not their decision and not their exposure.**
Give it thirty seconds and move on — it is the one people want to argue about and
the one where nothing they do matters.

**(b) Can they copyright what comes out?**

> ✅ **US Copyright Office, *Copyright and Artificial Intelligence*, Part 2
> (January 2025).** Human authorship remains required; **fully AI-generated
> output is not copyrightable**; **prompts alone do not confer authorship**; but
> AI used as a tool inside human creative work does **not** poison the whole
> work. Case-by-case; the Office recommended no new legislation.
> <https://www.copyright.gov/ai/>

For ordinary academic prose this rarely bites — their writing is full of human
authorship. Worth knowing, not worth fearing.

**(c) What must they disclose? — the only one that can actually cost them.**

> ✅ **COPE** and ✅ **ICMJE** converge: an AI tool **cannot be listed as an
> author**, because authorship requires taking responsibility and a
> non-legal entity cannot. Use is to be **disclosed** at submission.
> <https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools>
> <https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html>

**The move:** check your target journal's AI policy **before** submission, not
after. Two minutes. This is the one with teeth, and it is entirely in their
control.

---

## The live hallucination demo (~10 min)

**Do not invent a new one — use the trap that is already verified.** Full detail
in `examples/references/README.md`, item 3.

**Why this one:** it is a *real* property of a *real* literature, it fires
reliably, and they met it on Thursday. Fabricating a demo in the block about not
fabricating things would be a bad look.

**The beats:**

1. Ask, in a fresh session, for the full citation of **"The garden of forking
   paths."** Say "from memory, don't search" to make it fire reliably.
2. It produces a confident citation — often with an invented journal, volume and
   DOI, or a hybrid of the two real documents.
3. **Do not announce the error.** Ask the room: *does this look wrong to you?* It
   won't. That is the entire point — fabrications look exactly like citations.
4. Resolve the DOI on the projector. It fails, or it lands somewhere else.
5. The truth: the published work is **Gelman & Loken (2014), "The Statistical
   Crisis in Science," *American Scientist* 102(6), 460–465**, DOI
   `10.1511/2014.111.460`. "Garden of forking paths" is a phrase from its
   subtitle. A separate 2013 manuscript carries the title and was never
   published — no DOI, no journal, no volume.
6. Then re-run it **with search enabled** and let them watch it get much closer.
   *That contrast is the lesson*: not "AI lies," but **"the failure mode depends
   on the harness you gave it."**

⚠️ **Rehearse this the night before.** Fabrication is probabilistic — a model may
hedge, or nail it. If it hedges, that is still a fine outcome, so have the line
ready: *"good — and notice it hedged because the question was about a citation.
Ask it about a number and it usually won't."* Never re-run it three times hunting
for a failure; that reads as rigging the demo.

**Fallback if it behaves:** open `examples/references/`, item 6 — Trafimow &
Marks (2015) is literally titled **"Editorial,"** and agents reliably invent a
descriptive title instead. Or show the `nature.com` HTTP-200-with-HTML catch,
which fails identically every time.

---

## Closing the block

Hand to `handouts/verification.md` — the routine on one page. The line to end on:

> Every check in that list exists so you can move **faster**, not slower. You can
> hand a machine your work precisely because you know how to catch it. That is
> not caution. That is the thing that lets you be reckless in the right places.
