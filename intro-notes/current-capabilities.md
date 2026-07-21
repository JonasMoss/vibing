** What's this:** A rough overview of current capabilities, suitable for an introduction.  

**Headline: Current LLMs are incredibly strong.**

1. Performance in programming.
    * **Headline:** GPT5.6 crushing two recent competitive programming contests. Essentially super-intelligent in algorithmic and numerical programming.
        * **AtCoder WTF 2026:** OpenAI swept *both* the Algorithm and Heuristic divisions
          vs the 12 invited world-best; in Heuristic it scored ~7× the top human, and the
          "Humanity Prevails Award" went unclaimed (a human, Psyho, had won it in 2025).
        * **Sakana's ALE-Agent won a public contest live** (AHC 058, 1st of 804, Dec 2025) —
          honest caveat: ~$1,300 compute + special permission, "an advantage humans don't have."
        * **Codeforces:** GPT-5.5 logged the first Div-1 "AK" (all problems) by a publicly accessible model.
        * **ICPC 2025** world finals OpenAI 12/12 (out-solving human champions); **IOI 2025** gold.
        * (Full sourcing: `capabilities-evidence.md`, POWER I.)
2. Performance in mathematics.
    * **Headline / killer example:** In **July 2026**, **Claude Fable 5** found an explicit
      counterexample to the **Jacobian conjecture** — open since 1939 — announced by
      Levent Alpöge (Harvard). Formalized in **Lean** and verified within a day. A _Claude_
      model doing frontier math, and a computer checked the answer.
        * Honest caveat to keep: it's a _counterexample_ (easier than a proof), kills
          dimension ≥3, and the 2-variable case stays open. Gowers: "not in 'end of
          mathematics' territory, but still pretty amazing."
    * **The vibe from the top:** Gowers, replying to Szegedy's "the Fields Medal awarded
      next week will be the last one [given to humans]," says he's had similar thoughts but —
      due to lag — humans "will probably make it to 2030." A casual tweet, but from a Fields medalist.
        * Extremely capable _and_ broad.
        * Role of **Lean**: when the output is a proof, a computer checks it's airtight —
          the antidote to "but AI makes things up."
    * **More 2026 evidence (the audience won't know any of these — good):**
        * **IMO 2026 gold is now routine:** ChatGPT 5.6 Pro (the *consumer app*) one-shot
          ~41/42 on all six problems in ~1 h on contest day — barely news a year after the first golds.
        * **Unit-distance conjecture DISPROVED** (Erdős 1946) by an OpenAI model, May 2026;
          verified by Gowers, Sawin, Alon et al.; Kalai likens it to the Four-Colour proof.
        * **Erdős problems at scale:** dozens resolved in 2026 across OpenAI / Claude (Fable 5,
          Mythos) / Aristotle, much of it Lean-verified (tracker: erdosproblems.com).
        * **Benjamini–Hochberg FDR flaw** (the multiple-testing method, sibling of _Bonferroni_,
          >130k citations) — GPT-5.6 Sol built a counterexample in ~90 min; stats-audience gold.
        * **Cycle Double Cover "proof"** (GPT-5.6 Sol Ultra, Jul 2026) — CLAIMED, _not_ verified.
          The cautionary twin: a proof is hard to check, a counterexample is easy. Verify lesson.
        * **FrontierMath had errors in ~42% of problems** — an _AI audit_ caught them. Benchmarks lie too.
    * (Full sourcing: `capabilities-evidence.md`, POWER II.)
3. How to be up-to-date in performance.
    * The huge problem with papers and articles using _bad_ or _outdated_ models.
    * Non-academic channels are often superior, 
    * **Example: Literature and hallucinated references.**
        * You can find many papers describing the "problem of hallucinated references" so to speak.
        * But in my extensive experience using Codex / Claude code the last 6 months I havent seen _a single_ hallucinated citation. 
        * This happens, partly, because the models look up the citations. To be absolutely sure (which you should), use a _skill_ that checks every citation you use; we will go through this later. (I.e., checks existence, downloads, checks if it is _cited correctly_). (And, of course, have at least 10 seconds look on your cites man.)
4. My own experience right now.
    * "Relatively simple* statistical problems can just be solved.
    * Problems I'd rank as very hard can _also_ be solved, but not as clean.
    * Writing correct C++ and R packages is trivial, as is writing simulations.
        * **Concrete proof — `magmaan`:** a ~100k-line C++23 SEM engine, 10–100× faster than
          lavaan (checked model-for-model), rebuilt in ~6 weeks, which itself spun off ~ten
          new-method papers. → Exhibit C in the POWER deck.
    * Verifying correctness goes through simulations; _exactly as I did with my own math when I did math!_
    * The _exploration potential_ is obscene. Read a paper and got an idea? Don't spend a week or two investigating, just fire up Codex.
    * There's very little you have to do manually:
        * Creating files, opening files, editing files,
        * Downloading and installing software,
        * Changing computer settings
5. Remarks on performance in social science like econ.
6. Writing whole papers; the problem of _writing_. 
    * Discuss the recent blog post of https://www.futureofbeinghuman.com/p/publish-or-perish-ai-vs-human-vs-human
    * Often uncomfortable with the prose: "<cite blog>"
    * My own feelings about this.
    * We WILL discuss ways to handle this, but the _current bottleneck of AI research is finalizing the writing, not the content itself_.

** 