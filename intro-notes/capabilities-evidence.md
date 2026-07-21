# Capabilities evidence pack — sources for the 45-min POWER intro

Curated, source-linked evidence for the opening talk. Built from three research
passes (competitive programming, mathematics, research-workflow claims). Maps
onto the segments in the talk arc (see `plan`/discussion). Feeds
`current-capabilities.md`.

**Verification tiers** (state these honestly on slides):
- ✅ **Independently verified** — third-party organizer/grader/peer review.
- 🟡 **Sanctioned but company-reported** — real event, score reported by the lab.
- ⚠️ **Company-self-reported** — lab ran it and reported its own result.
- ❌ **Could not verify** — do not put on a slide as fact.

**(a) vs (b):** (a) = a general model a professor can actually use in a
terminal/chat (GPT-5.x, Claude, Gemini). (b) = a specialized lab system
(AlphaProof, AlphaEvolve, FunSearch) that is *not* a usable tool. Keep the line
clear or a skeptic will (rightly) call it blurry.

---

## POWER I — Competitive programming

**The one-story spine (use this):** July **2025**, one human (Przemysław "Psyho"
Dębiak) narrowly beats OpenAI's model at the AtCoder World Tour Finals Heuristic
division (~9.5%) and posts *"Humanity has prevailed (for now!)"*. July **2026**,
no human can beat the AI at **either** division. That slope *is* the thesis.

| Finding | When | Tier | Note |
|---|---|---|---|
| **AtCoder World Tour Finals 2026** — OpenAI system swept **both** divisions (Algorithm + Heuristic), beat every invited world-finalist human; Algorithm exhibition 5/5 problems (8,300 pts) vs top human 4,300. "Humanity Prevails Award" went **unclaimed**. | Jul 7–9 2026 | ✅ organizer-run, public scoreboard | Competing system "**comparable to** GPT-5.6" + compute harness, not provably the shipping SKU. No internet, fresh problems (judge-confirmed). |
| **AtCoder WTF 2025 (Heuristic)** — Psyho beats OpenAI's o3-class model by ~9.5%; *"Humanity has prevailed (for now!)"* | ~Jul 16 2025 | ✅ organizer-run | The narrative pair for 2026. Heuristic = open-ended optimization, where humans held out longest — say so. |
| **ICPC 2025 World Finals** (Baku) — OpenAI **12/12**, out-solving the human world champions (11/12); Gemini 2.5 Deep Think **10/12** gold, solved a problem **no human team** cracked. | Contest Sep 4 2025; announced Sep 17 | 🟡 human results official, AI scores lab-reported | The "Olympics of programming" for top universities. |
| **IOI 2025** (Bolivia) — OpenAI reasoning system **gold**, **#6 of 330** human contestants (~98th pct); up from ~49th pct in 2024. | Jul–Aug 2025; announced Aug 11 | ⚠️ company-self-reported | No independent IOI AI scoreboard found; treat rank as OpenAI's claim. |
| **Codeforces rating** — o3 ≈ **2727 Elo** (~top-175 in the world) vs o1 1891. | Dec 20 2024 | ⚠️ self-reported benchmark, not live | Use as the 2024 baseline the later live wins blow past. |
| *Baseline, (b):* DeepMind AlphaCode (2022, ~54th pct) → AlphaCode 2 (Dec 2023, 85th pct). | 2022–23 | 🟡 lab-reported | The slope: specialized engines needed years to reach "top 15%"; two years later **general** models beat champions. |

**"GPT-5.6" — verified.** Real OpenAI model, ~Jul 2026 (`https://openai.com/index/gpt-5-6/`).
Your "crushing two contests" = the two AtCoder WTF 2026 divisions. Keep the
"comparable to GPT-5.6" nuance so it can't be nitpicked.

**Skeptic answer to "it just memorized the problems":** all live 2025–26 contests
used fresh, never-seen problems released at start, no internet — confirmed by
AtCoder judges and ICPC.

**Freshest programming beats (2026) — add these for volume:**

- **Heuristics, the last human redoubt, fell hard.** At AtCoder WTF **2026** Heuristic
  (12 invited world-best heuristic programmers; one novel optimization problem) the
  OpenAI system scored **~7× the best human** (a score in the tens of billions); the
  "Humanity Prevails Award" for any human who could beat it went **unclaimed**. A year
  earlier the same event went to a *human* (Psyho) — so the one division where humans
  held out longest was gone within a year.
  `https://officechai.com/ai/openai-completely-demolishes-human-competitors-at-atcoder-2026-after-placing-2nd-last-year/`
- **An AI won a *public, open* contest in real time.** Sakana AI's **ALE-Agent** took
  **1st of 804** at **AtCoder Heuristic Contest 058** (Dec 14 2025) — the first known AI
  to win a major optimization contest live, not an invitational exhibition. **Honest
  caveat (say it out loud):** different conditions — ~**$1,300** compute, **4,773** API
  calls, special organizer permission; expert Yoichi Iwata noted its edge was exhaustive
  trial-and-error, "an advantage humans do not have." `https://sakana.ai/ahc058/`
- **Codeforces, recent:** GPT-5.5 (Apr 2026) logged the **first Div-1 "AK"** — all
  problems solved, including the hard problem G — by a *publicly accessible* AI model,
  well past the o3 ≈ 2727 baseline in the table; AtCoder WTF 2026 beat human finalists
  rated **>3700**. `https://codeforces.com/blog/entry/153267`

Key sources: `atcoder.jp/contests/awtf2026algo`, `atcoder.jp/contests/awtf2026heuristic`,
`codeforces.com/blog/entry/155048`, Euronews Psyho interview
`https://www.euronews.com/next/2025/07/22/humanity-has-won-so-far-meet-the-worlds-best-programmer-who-beat-ai-and-chatgpt`,
DeepMind ICPC `https://deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/`,
ICPC official `https://icpc.global/worldfinals/results-2025`, OpenAI IOI
`https://x.com/OpenAI/status/1954969035713687975`.

---

## POWER II — Mathematics

### ⭐ Flagship — and it's a *Claude* model: the Jacobian conjecture, disproved

**The story (July 19–20, 2026).** Number theorist **Levent Alpöge** (Harvard)
posted an explicit **counterexample to the Jacobian conjecture** — open since
**Keller, 1939 (87 years)** — found with **Claude Fable 5** (*"my close friend
fable, for working during the world cup final"*); Akhil Mathew suggested the
problem. It's a polynomial map ℂ³→ℂ³ whose Jacobian determinant is the constant
**−2** (so it *satisfies* the conjecture's hypothesis), yet **three different
points map to the same output** — so it is not invertible, exactly what the
conjecture said could never happen.

- Map (with `u = 1+xy`): `F = ( u³z + y²u(4+3xy),  y + 3xu²z + 3xy²(4+3xy),  2x − 3x²y − x³z )`,
  degrees (7,6,4). Collision: `F(0,0,−¼) = F(1,−3/2,13/2) = F(−1,3/2,13/2) = (−¼,0,0)`.
- **Why it's the perfect slide:** the counterexample is a *finite computation
  anyone can check*. Within a day **Paul Lezeau (Imperial) formalized it in Lean**
  and PR'd it to **DeepMind's `formal-conjectures` repo** — a *computer* has now
  verified it (plus independent Wolfram Alpha / SymPy checks). This is the cleanest
  possible reply to "but AI just makes things up": here it didn't, and we can
  *prove* it didn't.
- **Tier: ✅ formally (Lean) verified.** Not a lab press release — a checkable object.
- **Honest floor (keep it on the slide):** this kills the conjecture in dimension
  ≥3; the **2-variable ("plane") Jacobian conjecture is still open.** And Gowers'
  own framing is the right register — *"a counterexample, so not in 'end of
  mathematics' territory, but still pretty amazing."* A **counterexample** (exhibit
  one bad case) is far easier than a **proof** (rule out all cases). Say so.
- **Gowers on it:** *"Assuming this is correct, it is for me the first example of an
  LLM solving a problem not in my area that was nevertheless big enough that I had
  very definitely heard of it."*

Sources: Xena / Kevin Buzzard `https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/`,
Secret Blogging Seminar `https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/`,
plain explainer + exact formulas `https://jacobianfun.org/jacobian-explained`,
Lean formalization PR `https://github.com/google-deepmind/formal-conjectures/pull/4474`,
news `https://gigazine.net/gsc_news/en/20260721-claude-fable-5-jacobian-conjecture/`.
Primary tweets (Alpöge announcement + Gowers reaction) captured in `intro-notes/Pasted image (2).png`.

---

| Finding | (a)/(b) | When | Tier | Note |
|---|---|---|---|---|
| **IMO 2025 GOLD — Gemini Deep Think**, 35/42, 5/6 problems, **graded by official IMO coordinators**. | (a), exact model unreleased | Jul 2025 | ✅ IMO-graded | IMO President Dolinar confirmed the score. |
| **IMO 2025 GOLD — OpenAI**, also 35/42 | (a), unreleased | Jul 2025 | ⚠️ self-graded | Announced Jul 19, **before** the IMO's requested embargo — a great "read the fine print" slide. DeepMind waited. |
| **AlphaEvolve** — first improvement on **Strassen's 1969** algorithm (4×4 complex: 48 mults vs 49); kissing number in 11-D **592→593**; improved SOTA on ~20% of 50+ open problems. | (b) | May 14 2025 | ✅ constructions checkable | Incremental records, not a famous named conjecture — but genuinely *new* knowledge. Matrix multiply underlies all of ML. |
| **Erdős problems via GPT-5.2 Pro** — original proofs of previously-open problems, some **Lean-formalized and accepted by Terence Tao** ("most unambiguous instance" of AI solving an open problem). | (a) publicly usable | Jan 2026 | ✅ Lean-verified (mixed, see below) | **Cautionary tale attached** — see honesty note. |
| **FunSearch** — largest cap sets found in 20 years; first genuinely new math discovery made with an LLM. | (b) | Dec 2023 | ✅ *Nature* peer-reviewed | Origin story of "AI does new math." |
| **IMO 2024 SILVER — AlphaProof + AlphaGeometry 2**, 4/6 (28/42), cracked the hardest problem (only 5 of 609 humans solved it). | (b) | Jul 2024 | ✅ Lean, human-verified (Gowers + Myers) | **Off-clock** (up to 3 days/problem) and problems were **pre-formalized into Lean**. The 2024→2025 jump (slow/specialized/needs-formalizing → in-time/general/natural-language) is its own arc. |
| **FrontierMath** (Epoch AI; problems built by Fields medalists to be *too hard for AI*) — **<2%** at launch → **~29% single-run / 57% ever-solved** in ~1 year. | benchmark of (a) | Nov 2024 → Oct 2025 | ✅ third-party | Honest ceiling: Epoch estimates <~70% even with unlimited tries, growth slowing. Not solved. |

**IMO 2026 — gold is now a footnote (the "barely news" point).** On contest day
2026, **ChatGPT 5.6 Pro** — the *publicly available* app, web search disabled — went
**one-shot** on all six IMO problems and scored **~41/42** (full marks on five,
near-full on the sixth) in **~1 hour** total, per a write-up by Dutta, Hasan & Moon
(SignalPilot Labs), with an independent Gemini review scoring it 42/42. Tier: ⚠️
author/peer-graded, **not** official IMO coordinators (unlike the 2025 golds above) —
but the **full solutions are public and checkable**. The story isn't the medal; it's
that a *consumer chatbot* hitting IMO gold one-shot in an hour is, a year on, barely a
headline. That trend line *is* the point. Source (with full solutions):
`https://github.com/SignalPilot-Labs/AutoFyn/blob/production/results/imo-2026/pdfs/IMO_performance_by_GPT_5_6_sol.pdf`.

**The converted skeptics (your strongest anti-hype card):** Fields medalists now
use and endorse AI. **Gowers**: GPT-5 produced in ~20 s a proof that would've
taken him >1 hour; research will be *"changed out of all recognition"* for anyone
finishing a PhD by 2029; *"the lower bound for contributing to mathematics will
now be to prove something that LLMs can't prove."* **Tao**: Quanta's "evangelist
for AI in math," runs Lean+AI projects — but stresses today's LLMs grab
"lowest-hanging fruit" fast and still "behave like overconfident undergraduates"
at the true frontier. Use the optimism **and** the hedges.

**Why "formally verified" matters (the Lean thread):** the antidote to "but AI
makes things up" — when the output is a proof, a computer (Lean) checks it is
airtight; no trust in the AI required. Caveat: formalizing *into* Lean is itself
work, and the IMO-2025 gold proofs were graded in natural language, not Lean.

Key sources: DeepMind IMO 2025 gold
`https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/`,
AlphaEvolve `https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/`,
FunSearch (*Nature*) `https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/`,
IMO 2024 silver `https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/`,
FrontierMath `https://epoch.ai/frontiermath/the-benchmark`,
Tao profile `https://www.quantamagazine.org/how-terry-tao-became-an-evangelist-for-ai-in-math-20260608/`.

---

### The 2026 wave — five more results, with the *verify* lesson built in

Most of this broke **after** common training cutoffs, so it may be new to your AI
too — **cite it, don't ask the model to confirm it.** The through-line to teach:
**a counterexample is cheap to check; a proof is expensive to check** — and that
alone tells the audience how fast to trust each headline.

**1. Erdős' unit-distance conjecture — DISPROVED by an OpenAI model (May 2026). ✅ human-verified.**
Erdős (1946) conjectured that *n* points in the plane admit at most
`n^{1+c/loglog n}` unit distances — grid-like sets were believed essentially
optimal. An internal OpenAI reasoning model produced a construction beating that,
`≥ n^{1+δ}` for a fixed `δ>0`, via algebraic number theory (class-field towers,
Golod–Shafarevich). **Verified and written up by a who's-who** — Alon, Bloom,
**Gowers**, Litt, Sawin, Shankar, Tsimerman, Wang, Matchett Wood; Will Sawin pinned
`δ≈0.014`, later pushed to `≈0.032`. **Gil Kalai** ("truly amazing," likens it to the
1976 Four-Colour computer proof) and **Tao** both blogged it. Honest floor: it does
**not** close the gap to the classical `O(n^{4/3})` upper bound. Sources: Kalai
`https://gilkalai.wordpress.com/2026/05/21/amazing-erdos-unit-distance-problem-was-disproved-it-was-achieved-by-ai/`,
Tao `https://terrytao.wordpress.com/2026/07/03/a-digestion-of-unit-distance-constructions/`.

**2. Erdős problems, now at *scale* — dozens in 2026, every major lab, much of it Lean-verified. ✅ (mixed).**
Tao's `erdosproblems.com` tracker lists full 2026 resolutions across labs: **[38]**
GPT-5.5 Pro; **[90]** OpenAI-internal + Claude Mythos; **[205]/[457]** Aristotle+GPT-5.2
(Lean); **[619]** Claude Fable 5 / Codex / GPT-5.5 (Lean); OpenAI-internal batches
([960/987/990/1141], Apr 2026); plus ~a dozen Tao-in-the-loop collaborations. Human-
interest headline: a 23-year-old (Liam Price) got **GPT-5.4 Pro** to crack a 60-year
Erdős problem from a single prompt in ~80 min; **Tao** called it a *"meaningful
contribution to the anatomy of integers that goes well beyond"* the problem and
extended it into new theory within a day. **Keep the caveat** (see the Oct-2025
embarrassment in Corrections): "solved" on the tracker sometimes meant *rediscovered
a published solution* — the tracker now flags genuinely-new. Source:
`https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erdős-problems`.

**3. A flaw in Benjamini–Hochberg (the FDR / multiple-testing method) — GPT-5.6 Sol, Jul 2026. ✅ simulation-verified.**
*This is the one for a room of empirical social scientists.* The Benjamini–Hochberg
procedure (1995, **>130,000 citations** — the standard multiple-comparisons fix, and
the sibling of the **Bonferroni** correction) was long *conjectured* to control the
false-discovery rate for correlated Gaussian data under two-tailed tests. UPenn
statistician **Edgar Dobriban** had **GPT-5.6 Sol Pro** build a Gaussian factor-model
**counterexample** where the FDR *provably exceeds* the target (**0.104 vs 0.10**) —
in ~90 min, after GPT-5.5 failed for ~20 h. Confirmed by simulation; code on GitHub.
**Dobriban's own honest framing (use it verbatim):** the model *"combines known
methods rather than inventing new ones"* — the win was spotting the connection, not
new mathematics. Source:
`https://the-decoder.com/gpt-5-6-sol-reportedly-disproves-a-30-year-old-statistics-conjecture-in-90-minutes-after-humans-couldnt-crack-it/`.

**4. Cycle Double Cover Conjecture — CLAIMED proof by GPT-5.6 Sol Ultra (Jul 2026). ⚠️ NOT verified — the cautionary twin.**
OpenAI posted a short manuscript claiming a *full proof* of this famous graph-theory
conjecture, reportedly produced fast by a many-subagent run. **No peer review; no
independent specialist has checked it.** This is the deliberate contrast to items 1–3:
a **proof** of a hard conjecture can't be spot-checked the way a **counterexample**
can — you can't "just plug in the numbers." *"A posted proof is a proof claim, not yet
a settled theorem."* Teach the asymmetry: trust the checkable disproofs quickly,
withhold judgement on the proof claim. Source (appropriately skeptical):
`https://www.remio.ai/post/openai-paper-claims-gpt-5-6-sol-ultra-proved-the-cycle-double-cover-conjecture`
(OpenAI manuscript PDF exists at `cdn.openai.com/pdf/...cdc_proof.pdf`).

**5. Even the benchmark was wrong — FrontierMath's 42% error rate. ✅ Epoch-corrected.**
The "too hard for AI" benchmark (problems built by Fields medalists) turned out to
have **small but critical errors in ~42% of problems** — an **AI-assisted audit**
caught them where human review had flagged only ~5%. Fixed in **v2 (Jun 12 2026)**;
because the errors had been marking *correct* answers wrong, scores *jumped* after the
fix (e.g. GPT-5.5 ~35% → ~72% on Tier 4) — i.e. the apparent difficulty was partly
broken problems, and the "saturation" is partly the correction. Two lessons in one:
**benchmarks are fallible too — verify the yardstick**; and the tool that caught the
errors was itself an AI. (Confirm exact figures on Epoch's page.) Sources:
`https://epoch.ai/benchmarks/frontiermath-tier-4-v2`, analysis
`https://www.digitalapplied.com/blog/epoch-frontiermath-v2-error-corrected-ai-benchmark-analysis`.

> **The meta-lesson these five hand you for free:** the *form* of a result tells you
> how fast to trust it. Counterexample → you can check it in minutes (Jacobian,
> unit-distance, FDR). Proof of a famous conjecture → slow down (Cycle Double Cover).
> Benchmark number → the yardstick itself can be broken (FrontierMath). That *is* the
> verify spine of the whole course — taught with frontier examples.

---

## POWER III — Your research world (+ economics)

- **Jonas's own experience** (from `current-capabilities.md`): "relatively simple"
  stats problems just get solved; very hard ones too, less cleanly; correct C++/R
  packages and simulations are trivial; verification via simulation *exactly as in
  hand math*; exploration potential "obscene."
- **Korinek, "AI Agents for Economic Research"** (NBER WP 34202, Sep 2025) — a
  *Journal of Economic Literature* editor-commissioned series. Verbatim: agents
  can *"autonomously conduct literature reviews across myriads of sources, write
  and debug econometric code, fetch and analyze economic data, and coordinate
  complex research workflows"*; and — on-brand — *"by 'vibe coding' … any economist
  can build sophisticated research assistants … in minutes."* Peer-reviewed anchor:
  Korinek, JEL 61(4), Dec 2023 `https://www.aeaweb.org/articles?id=10.1257/jel.20231736`.
  NBER: `https://www.nber.org/papers/w34202`. (Discloses unpaid seat on Anthropic's
  Economic Advisory Board.)
- **AI already executes empirical econ near human level**: Ning Li 2026 — execution
  3.84/5.0 (AI) vs 4.38 (human). The gap is *ideas*, not competence (see honest floor).

---

## "Don't trust old takes" — the hallucinated-citation myth, updated

- **Canonical scare stat is from 2023 memory-only models:** Walters & Wilder,
  *Scientific Reports* 2023 — **55% of GPT-3.5 citations fabricated, 18% GPT-4**
  (data: first week of April 2023, no browsing).
  `https://www.nature.com/articles/s41598-023-41032-5`. One model generation cut
  fabrication by two-thirds — proof these studies age fast.
- **Retrieval/agentic tools cut it by ~an order of magnitude:** Rao, Wong &
  Callison-Burch (UPenn), arXiv:2604.03173 (Apr 2026) — search-augmented LLMs
  ~4.8% fabricated URLs; deep-research agents ~10.7% (OpenAI Deep Research 3.5%);
  and automatic URL-checking cuts non-resolving links *"to under 1%."*
  `https://arxiv.org/abs/2604.03173`.
- **But NOT zero — keep it honest:** Stanford RegLab/HAI 2024–25 — purpose-built
  *legal* RAG tools still hallucinated **17–34%**.
  `https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries`.
- **Framing:** say "largely removes / drops by roughly an order of magnitude,"
  **not** "eliminates." A Claude Code / Codex user with citation lookup is simply
  not running the 2023 memory-only configuration those scare studies measured. And
  the rising count of fabricated cites *in published papers* (2026) is author
  misuse of weak tools, not evidence against agentic tools — don't let anyone
  conflate them.

---

## The honest floor — where the human still lives (present the DISAGREEMENT)

The bottleneck is real, but reasonable people disagree on *what it is* — and
saying so is what makes the whole talk credible:

- **Writing (Maynard, Jul 2026):** co-wrote a paper with an AI, kept the ideas,
  spent **three days** only on prose. *"I changed relatively little of the
  substance … What I did change … was … the narrative form."* But a twist worth
  showing: four AI judges all preferred the AI's prose over his human-edited
  version. `https://www.futureofbeinghuman.com/p/publish-or-perish-ai-vs-human-vs-human`.
- **Ideation (Ning Li, arXiv:2604.03338, Apr 2026):** decomposing the AI-vs-human
  quality gap in economics papers, **ideation is ~71% of the gap, execution only
  ~29%.** *"The primary bottleneck … remains ideation."* This directly
  pressure-tests a "writing is the only thing left" claim. `https://arxiv.org/abs/2604.03338`.
- **Verification (Schmelzer, Forbes, Jul 2026):** AI *"can … turn weak work into
  prose that sounds more convincing than the evidence behind it."* The bottleneck
  is checking, not producing.

Honest synthesis for the slide: *"The last mile is human — but people disagree on
whether it's the writing, the ideas, or the verification. You supply judgement."*

> ⚠️ **This touches `vision.md`.** The vision doc currently states the bottleneck
> "moved to finalizing the writing." That's Jonas's lived experience and a fair
> headline, but the strongest systematic study (Ning Li) says *ideation*. Consider
> softening to "the last mile is human judgement — writing, ideas, and verification."

---

## Corrections & flags (READ THIS)

1. ✅ **The Gowers "last Fields Medal to a human ~2030" line is now SOURCED**
   (Jonas's screenshot, `intro-notes/Pasted image.png`). The thread: Alek Dimitriev
   → **Christian Szegedy** (@ChrSzegedy, Jul 19 2026), *"The fields medal awarded
   next week will be the last one [given to humans]."* **Gowers** (@wtgowers) replies:
   *"I've had similar thoughts. But there's a lag, so I think they'll probably make
   it to 2030."* ("Next week" = the Fields Medals at ICM 2026.)
   - **So the line is real — but present it as what it is:** a *casual, tweet-register*
     agreement-with-a-caveat, i.e. a vibe from a Fields medalist, **not** a methodical
     forecast. Attribute as "Gowers, agreeing (with a lag) to Szegedy's claim," not
     "Gowers predicts." Do not launder a tweet into a citation.
   - Pair it with his firmer on-record lines for weight: research *"changed out of all
     recognition"* for anyone finishing a PhD by 2029; *"the lower bound for
     contributing to mathematics will now be to prove something that LLMs can't prove."*
   - The aggressive "Fields-Medal-level is a matter of time, not capability" framing
     also traces to **Tao** (second-hand paraphrase of a talk) — attribute carefully.
2. ⚠️ **Erdős cautionary tale (feature it, don't hide it):** In **Oct 2025** an
   OpenAI staffer wrongly claimed GPT-5 "solved 10 open Erdős problems" — it had
   only *found existing published solutions* ("open" meant the database curator
   didn't know a solution). Corrected publicly; Hassabis called it "embarrassing."
   The **Jan 2026** GPT-5.2 Pro solves are the real ones (Lean-verified, Tao-vetted)
   — but Tao stresses they're "lowest-hanging fruit," speed not depth. This whole
   arc is a *gift* for teaching healthy skepticism.
3. **Much 2026 Erdős/Tao/Gowers coverage rests on tech-press secondary sources.**
   The load-bearing facts (IMO 2024/2025, AlphaEvolve, FunSearch, FrontierMath,
   the hallucination studies, Korinek) are anchored to primary lab/Epoch/Nature/NBER
   sources above and are solid.
