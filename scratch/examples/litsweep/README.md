# Instructor key — the literature sweep (Day 2, 13:00–14:15)

Participants get `litsweep.zip`: twelve open-access papers on **AI in higher
education** and nothing else. **This file is for you.** It never ships.

Download link to read aloud: **`vibing.jonasmoss.com/litsweep.zip`**
(15.4 MB, unpacks as a `litsweep/` folder — twelve PDFs plus `SOURCES.md`).
Rebuild with `python3 scratch/examples/scripts/fetch-litsweep-example.py`; the PDFs are gitignored
on purpose and the script explains why.

> **One repo decision worth knowing.** `examples/litsweep/pdfs/` is gitignored —
> that's the lesson. **`examples/litsweep.zip` is not**, because the Pages workflow
> only does `checkout` + `npm run build:pages`; an ignored zip would deploy a clean
> green build and a 404 on the download link, discovered at 13:05 on Day 2. So the
> repo carries one 15.4 MB artefact, the same way it already carries
> `decrap-me.zip`. If you'd rather not, gitignore it and upload the zip to the
> Pages branch by hand — but then *test the URL* before the course.

**Why a provided folder is the primary path here.** Nobody was asked to prepare
anything, so assume most of the room has no PDFs on the laptop. Anyone who *can*
reach their own literature — OneDrive, email, a Zotero folder — should, because
their own field is strictly better. Everyone else uses this, and it is not a
consolation prize: it is a real corpus with real disagreements in it.

**Why this topic.** Every department in the room has an opinion about AI in
higher education, nobody needs domain knowledge to follow it, and — the part that
makes the block work — **the literature genuinely contradicts itself.** The
question at the top of the ladder ("which papers disagree, and about what?") has
a real answer, and it is more interesting than anyone expects.

---

## The task ladder (and what each rung is actually for)

1. **Summarise one PDF.** Warm-up. Everyone succeeds. Point out that they just
   read a 27-page systematic review in forty seconds.
2. **Build a comparison table across all twelve** — research question, method,
   sample, finding. This is the rung where the capability lands: twelve papers,
   four columns, two minutes.
3. **"Which of these papers disagree with each other, and about what?"** The best
   question in the block. Real answer below — referee it live.
4. **Export the table** to Markdown or CSV, so it leaves the room with them.
5. **The honesty checkpoint** — pick one cell and check it against the PDF. See
   the section near the end; it names the cell to send them to.

**Warn yourself about rung 2 before you run it.** These are well-known papers. A
frontier model may fill the table from memory rather than from the folder, and
memory is *mostly* right — which is worse than being wrong, because it looks
identical to work. One prompt separates them:

> For every cell, give me the page number you got it from and quote the sentence.

Two of the twelve are booby-trapped against recall specifically (Bastani, whose
famous working-paper title is not its published title; and Wang & Fan, which was
retracted after the training data was collected). If a table cites "Generative AI
Can Harm Learning" or reports Wang & Fan's effect size without comment, you are
looking at recall, not reading.

---

## The twelve papers

Every citation was verified against Crossref, every licence against Crossref
*and* the licence statement printed in the PDF, and every PDF was downloaded,
opened and read. Verification log at the end.

### 1 · `zawacki-richter-2019.pdf` — the field's founding complaint

**Zawacki-Richter, O., Marín, V. I., Bond, M., & Gouverneur, F. (2019).**
"Systematic review of research on artificial intelligence applications in higher
education – where are the educators?" *International Journal of Educational
Technology in Higher Education* **16**, 39. DOI `10.1186/s41239-019-0171-0`.
**CC BY 4.0.** 27 pp.

- **RQ** — What has AI-in-higher-education research actually studied, and what
  are its ethical and pedagogical blind spots?
- **Method** — Systematic review, 2007–2018.
- **Sample** — **146 articles**, screened down from **2,656** initial records.
  (Both numbers are in the abstract. "2,656" is the wrong answer.)
- **Finding** — Four application areas: profiling/prediction, assessment/
  evaluation, adaptive systems/personalisation, intelligent tutoring systems.
  The headline is the complaint: **only 2 of 146 articles (1.4%) critically
  reflect on ethical implications**, only 5 of 146 (3.4%) define "AI" at all, and
  the work is dominated by computer science rather than education.
- 🪤 The title's question is rhetorical. An agent that answers "the educators are
  in the field" has inverted the paper.

### 2 · `crompton-burke-2023.pdf` — the upbeat one

**Crompton, H., & Burke, D. (2023).** "Artificial intelligence in higher
education: the state of the field." *IJETHE* **20**, 22.
DOI `10.1186/s41239-023-00392-8`. **CC BY 4.0.** 22 pp.

- **RQ** — Where, by whom, and to what end is AI-in-HE research being done, 2016–2022?
- **Method** — PRISMA systematic review.
- **Sample** — **138 articles**, 31 countries.
- **Finding** — The field is booming (2021–22 published two to three times the
  prior annual rate), leadership shifted from the US to China, and — explicitly
  against Zawacki-Richter — **departments of education are now the most common
  affiliation.** 72% of studies focus on undergraduates.
- 🪤 **The paper contains two different 72% figures, and they are not the same
  statistic.** 99 of 138 (72%) study *undergraduates* rather than graduates; and
  72% of studies focus on *students* rather than instructors (17%) or managers
  (11%). Both are true; a table cell that says "72%" without saying which is
  unusable. Good, cheap thing to make someone check.

### 3 · `chan-2023.pdf` — policy, and the surprise about staff

**Chan, C. K. Y. (2023).** "A comprehensive AI policy education framework for
university teaching and learning." *IJETHE* **20**, 38.
DOI `10.1186/s41239-023-00408-3`. **CC BY 4.0.** 25 pp.

- **RQ** — What should a university's generative-AI policy contain, given what
  its students and staff actually think?
- **Method** — Mixed-methods survey (5-point Likert plus open questions),
  descriptive + thematic analysis. Hong Kong universities.
- **Sample** — **457 students and 180 teachers/staff.**
- **Finding** — Proposes an "AI Ecological Education Policy Framework" with three
  dimensions: Pedagogical, Governance, Operational. The empirical surprise is in
  the numbers: **staff and students answer almost identically.** Long-term
  positive impact: students 4.00, teachers 3.87. Institutions need a plan:
  4.50 vs 4.54. Worried other students will use AI to get ahead: 3.67 vs 3.93.
  "AI will replace teachers": 2.14 vs 2.26 — both reject it.
- 🪤 Self-reported *use* at the time was low for both groups (means ≈ 2 of 5). A
  table row reading "students and staff use generative AI extensively" is the
  opposite of the data.

### 4 · `chan-hu-2023.pdf` — the student-voice survey

**Chan, C. K. Y., & Hu, W. (2023).** "Students' voices on generative AI:
perceptions, benefits, and challenges in higher education." *IJETHE* **20**, 43.
DOI `10.1186/s41239-023-00411-8`. **CC BY 4.0.** 18 pp.

- **RQ** — How familiar are students with generative AI, and what do they think
  it is good and bad for?
- **Method** — Survey: 26 Likert items + 3 open-ended, thematic analysis.
- **Sample** — **399 students** (177 undergraduate, 222 postgraduate), Hong Kong.
- **Finding** — Broadly positive: personalised support, writing and
  brainstorming, research assistance. Concerns: accuracy, privacy, ethics, and
  the effect on their own development and job prospects.
- 🪤 **Same first author, same city, same year, same journal as #3, different
  study and different n (399 vs 457).** Agents merge them. If your table has one
  Chan row, or a row with "n = 856", it collapsed two papers into one. This is
  the most likely *silent* error in the whole exercise.

### 5 · `bearman-2023.pdf` — the critical one

**Bearman, M., Ryan, J., & Ajjawi, R. (2023).** "Discourses of artificial
intelligence in higher education: a critical literature review." *Higher
Education* **86**(2), 369–385. DOI `10.1007/s10734-022-00937-2`.
**CC BY 4.0.** 17 pp.

- **RQ** — How is the term "artificial intelligence" actually invoked in the
  mainstream higher-education literature?
- **Method** — Critical literature review + Gee-style **discourse analysis** —
  the only qualitative-interpretive method in the folder.
- **Sample** — **29 articles**, drawn from a systematic term search of top
  higher-education journals up to November 2020. (Small, and deliberately so.)
- **Finding** — Almost no definitions: **one paper in three decades** of top HE
  journals defines AI. Two Discourses organise everything else: the *Discourse of
  imperative change* (AI is inevitable, you must respond) and the *Discourse of
  altering authority* (AI decentres the teacher, spreading authority across
  staff, machines, corporations and students).
- 🪤 "Sample = 29" looks like a weakness next to Crompton's 138. It isn't — the
  method is interpretive and the corpus is a deliberate, bounded one. Worth
  saying out loud when someone in the room reaches for n as a quality score.

### 6 · `bond-2024.pdf` — the review of the reviews

**Bond, M., Khosravi, H., De Laat, M., Bergdahl, N., Negrea, V., Oxley, E.,
Pham, P., Chong, S. W., & Siemens, G. (2024).** "A meta systematic review of
artificial intelligence in higher education: a call for increased ethics,
collaboration, and rigour." *IJETHE* **21**, 4.
DOI `10.1186/s41239-023-00436-z`. **CC BY 4.0.** 41 pp. Nine authors.

- **RQ** — What is the scope, nature and **quality** of evidence synthesis on AI
  in higher education?
- **Method** — Meta review ("review of reviews"), seven databases plus
  snowballing, 2018 – July 2023.
- **Sample** — **66 reviews** (not 66 studies — 66 *syntheses*, two-thirds of them
  systematic reviews). This cell is a classic wrong answer.
- **Finding** — The secondary literature is methodologically thin:
  **45.5% did no quality assessment at all**, **34.8% never reflected on their
  own limitations**, only 24.2% published their data-extraction scheme, and 71.2%
  were domestic-only collaborations. Hence the subtitle's three demands.
- 🪤 The "sample" column is the trap for all four reviews in this folder
  (#1, #2, #5, #6): the unit is *papers*, not people. A table that reports student
  counts for these rows has quietly invented them.

### 7 · `basic-2023.pdf` — the null result

**Bašić, Ž., Banovac, A., Kružić, I., & Jerković, I. (2023).** "ChatGPT-3.5 as
writing assistance in students' essays." *Humanities and Social Sciences
Communications* **10**, 750. DOI `10.1057/s41599-023-02269-7`.
**CC BY 4.0.** 5 pp.

- **RQ** — Does ChatGPT help students write better essays?
- **Method** — Small controlled experiment; two graders, rubric-scored, plus
  similarity and AI-classifier checks.
- **Sample** — **18 students** — 9 control, 9 ChatGPT-assisted — who **volunteered
  from a class of 50**, at the University of Split. Groups matched on study module
  and GPA. Essays were **800–1000 words in Croatian**.
- **Finding** — **No difference.** Both groups averaged grade C. Neither group,
  writing duration, study module nor GPA predicted score. The ChatGPT group's text
  was slightly less "authentic" and was flagged more often by an AI classifier.
- 🪤 Three things a one-line "finding" cell hides, and any of them is a fine
  checkpoint: the sample is **self-selected volunteers, not randomised** from the
  class; the language is **Croatian, not English**; and n = 18 cannot detect
  anything but an enormous effect. "ChatGPT doesn't help" is not what this study
  is powered to say.

### 8 · `kestin-2025.pdf` — the strong positive

**Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025).**
"AI tutoring outperforms in-class active learning: an RCT introducing a novel
research-based design in an authentic educational setting." *Scientific Reports*
**15**, 17458. DOI `10.1038/s41598-025-97652-6`.
**CC BY-NC-ND 4.0.** 10 pp.

- **RQ** — Can a purpose-built AI tutor beat in-class active learning — the
  current best practice — on real students in a real course?
- **Method** — **Randomised controlled trial, crossover design.** Every student
  did both conditions, one per topic (surface tension, fluids), with A/B test
  versions counterbalanced. Randomised at the level of 2–3 student
  peer-instruction groups. Harvard IRB 23-0797.
- **Sample** — **194 students**, from the 233 enrolled in Harvard's largest
  physics course (PS2, physics for the life sciences). See the checkpoint below —
  this cell is a minefield of nearby true numbers.
- **Finding** — The AI group learned **more, in less time**. Median post-test 4.5
  vs 3.5 against a combined pre-test baseline of 2.75; median learning gain
  **over double** the in-class group's; Mann–Whitney z = −5.6, **p < 10⁻⁸**;
  effect size **0.63** by linear regression, **0.73–1.3 SD** by quantile
  regression once the ceiling effect is handled. Median time on task **49 minutes
  vs the class's 60**. Students also reported more engagement and motivation. The
  effect held for students below and above the 40% FCI pre-score benchmark.
- 🪤 The AI tutor was *custom-built on the same pedagogy as the lesson*, not
  ChatGPT out of the box. Everything downstream depends on that clause.

### 9 · `bastani-2025.pdf` — the strong negative

**Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R.
(2025).** "Generative AI without guardrails can harm learning: Evidence from high
school mathematics." *PNAS* **122**(26), e2422633122.
DOI `10.1073/pnas.2422633122`. **CC BY-NC-ND 4.0.** 8 pp.

- **RQ** — What happens to *learning* — not performance — when students get a
  generative-AI tutor, and does the tutor's design change the answer?
- **Method** — Preregistered **field RCT**, three arms (control / **GPT Base** /
  **GPT Tutor**), randomised at classroom level, SEs clustered at classroom level.
  Four 90-minute sessions ≈ 15% of a semester's maths curriculum. Practice was
  assisted; the exam that followed was closed-book, closed-laptop.
- **Sample** — **"nearly 1,000" students in ~50 classes, grades 9–11, at a large
  high school in Turkey**, autumn 2023. Honors classrooms excluded from the main
  sample. **This is secondary education, in a folder about higher education.**
- **Finding** — With the AI present, performance soared: **+48% (GPT Base), +127%
  (GPT Tutor)**. With it taken away: **GPT Base students scored 17% below
  control** (−0.054 of 1). **GPT Tutor students were statistically
  indistinguishable from control** (−0.004, an order of magnitude smaller).
  Without guardrails, students used GPT-4 as a "crutch".
- 🪤 **Three separate traps, and this is the richest paper in the folder.**
  1. The working paper everyone remembers was called *"Generative AI Can Harm
     Learning"* (SSRN, 2024). The published title has **"without guardrails"** in
     it, and that phrase carries the entire result. A citation without it is a
     recall artefact.
  2. There is a **Correction** (`10.1073/pnas.2518204122`, 20 Aug 2025) — and it
     is **purely a production error in one author's affiliation.** Perfect
     counterweight to #12: *"flag anything retracted or corrected" is the right
     prompt, and then you still have to read the flag.* One of this folder's two
     flags is fatal; the other is cosmetic.
  3. See the honesty checkpoint — the "finding" cell of this row is the one to
     send the room to.

### 10 · `scarfe-2024.pdf` — the covert exam study

**Scarfe, P., Watcham, K., Clarke, A., & Roesch, E. (2024).** "A real-world test
of artificial intelligence infiltration of a university examinations system: A
'Turing Test' case study." *PLOS ONE* **19**(6), e0305354.
DOI `10.1371/journal.pone.0305354`. **CC BY 4.0.** 21 pp.

- **RQ** — Would a university's real examination system notice 100% AI-written
  work, and how would it grade it?
- **Method** — Blind covert field study. The authors injected AI answers into
  live exams; **markers were not told**, and study authorisation did not require
  their consent. (Worth thirty seconds of discussion on its own.)
- **Sample** — **63 AI submissions** across **5 undergraduate psychology modules**
  at a UK university, against **1,134 real submissions**. See the trap.
- **Finding** — **94% of the AI submissions went undetected** (6% flagged, for any
  reason at all). Grades were on average **half a classification boundary higher**
  than real students', and across modules there was an **83.4%** chance the AI
  submissions would beat an equal-sized random sample of real ones. The authors
  add that 6% likely *overstates* real-world detectability, since they used AI in
  the most detectable way possible.
- 🪤 **33 fake student accounts were created, but 63 submissions were made.** "33"
  is in the paper and is the wrong answer to "sample size". Second-best checkpoint
  cell in the folder.

### 11 · `liang-2023.pdf` — detection's other failure

**Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023).** "GPT detectors
are biased against non-native English writers." *Patterns* **4**(7), 100779.
DOI `10.1016/j.patter.2023.100779`. **CC BY-NC-ND 4.0.** 4 pp.

- **RQ** — Are AI-text detectors fair to non-native English writers?
- **Method** — Benchmark evaluation of **seven** widely used GPT detectors, plus
  an adversarial prompt-rewriting test.
- **Sample** — **91 TOEFL essays** written by non-native speakers and **88 US
  eighth-grade essays** (Hewlett ASAP corpus). **No university students at all.**
- **Finding** — Average **false-positive rate of 61.3%** on the human-written
  TOEFL essays; **97.8% were flagged by at least one detector**; near-perfect
  accuracy on the US eighth-grade essays. Asking GPT-4 to improve the TOEFL
  essays' word choice cut the false-positive rate from 61.3% to 11.6%, and
  simplifying the eighth-graders' vocabulary raised *their* misclassification —
  so the detectors are measuring lexical sophistication, not authorship.
- 🪤 **It is labelled an *Opinion* piece in *Patterns*, not a research article** —
  and it contains original experiments anyway. Both facts are true; a table that
  says "opinion piece" and drops the experiments is as wrong as one that calls it
  a research article. Note also the sample is schoolchildren and test-takers, so
  every claim about *university* students is an extrapolation.

### 12 · `wang-fan-2025.pdf` — ⚠️ **RETRACTED**, and deliberately here

**Wang, J., & Fan, W. (2025).** "The effect of ChatGPT on students' learning
performance, learning perception, and higher-order thinking: insights from a
meta-analysis." *Humanities and Social Sciences Communications* **12**, 621.
DOI `10.1057/s41599-025-04787-y`. **CC BY-NC-ND 4.0.** 21 pp.
**Retracted 22 April 2026** — Retraction Note `10.1057/s41599-026-07310-z`:
*"discrepancies in the meta-analysis"*, raised by Magnus Ingebrigtsen and Marko
Lukic; the authors did not respond.

- **What it claims** — Meta-analysis of **51 (quasi-)experimental studies**
  published Nov 2022 – Feb 2025: ChatGPT has a **large** positive effect on
  learning performance (**g = 0.867**) and moderate effects on learning perception
  (0.456) and higher-order thinking (0.457).
- **Method** — Meta-analysis with moderator (subgroup) analyses.
- **Sample** — 51 studies spanning **primary (7–13), secondary (14–17) and higher
  education** — so it is not a higher-education finding even on its own terms.
- 🪤 **This is the best object in the folder, and here is why.** The PDF is
  stamped **RETRACTED** across every page — a human opening it sees it
  immediately. But the watermark is interleaved with the sidebar text in the PDF's
  text layer, so **`grep -i retract` on the extracted text returns zero hits.**
  Verified: zero. An agent working from extracted text will summarise it as a
  perfectly good meta-analysis. A human who opens the file sees the problem in one
  second.
  > **The line to say:** *the model didn't miss this because it's stupid. It
  > missed it because it read the text and you'd have looked at the page.* That's
  > not an argument for reading everything yourself — it's an argument for knowing
  > which one thing to look at.
- **How to make it land:** don't warn them. Let the table get built. Then:
  *"one of these twelve has been retracted — which one, and how would you find
  out?"* The answer is one Crossref lookup per DOI (Crossref's title field for
  this record literally begins `RETRACTED ARTICLE:`) — or opening the PDF.
- **If someone objects to shipping a retracted paper:** it is CC BY-NC-ND, the
  licence does not lapse on retraction, `SOURCES.md` in the zip states the
  retraction and its date in full, and this is exactly the shape of the mess in
  everybody's actual PDF folder.

---

## The answer to "which papers disagree, and about what?"

Four real axes. Anything the room finds beyond these, check it against the PDFs —
but these four are solid, and the third one is the surprise.

### Axis A — does generative AI help students learn? (the big one)

| Paper | Verdict | Effect |
|---|---|---|
| Kestin 2025 | **helps, a lot** | 0.73–1.3 SD, in 49 min vs 60 |
| Wang & Fan 2025 | **helps, a lot** — ⚠️ retracted | g = 0.867 |
| Bašić 2023 | **no effect** | both groups grade C |
| Bastani 2025 | **harms** | −17% once the AI is taken away |

Four papers, four different answers, and **the resolution is in the methods, not
in who is right.** Draw it out of the room:

- **Kestin and Bastani are not actually contradicting each other.** Kestin measured
  learning *with* a purpose-built tutor present, immediately after the lesson.
  Bastani measured what remains *after the tutor is removed*. And Bastani's
  *scaffolded* arm — GPT Tutor, the one closest to what Kestin built — **did not
  harm learning either.** Read carefully, the two papers converge on one sentence:
  **a tutor designed to withhold answers helps; a chatbot that hands them over
  becomes a crutch.** That sentence is worth more than either headline, and no
  single paper in the folder states it.
- **Bašić's null is a power result, not a contradiction.** n = 18 volunteers,
  Croatian-language essays, one sitting. It is evidence of absence only if you
  ignore the design.
- **They also disagree about who "students" are.** Harvard physics undergraduates;
  Turkish 9th–11th graders; 18 Croatian forensic-science volunteers; a pooled mix
  spanning ages 7 to university. The "sample" column already contains the answer to
  the disagreement, which is a nice thing to notice out loud.
- And one of the four **has been withdrawn from the literature entirely.**

### Axis B — is AI-written work detectable? Same failure, opposite victims

- **Scarfe 2024:** detection fails *permissively* — 94% of fully AI-written exam
  answers sailed through, scoring **above** real students.
- **Liang 2023:** detection fails *punitively* — 61.3% of genuine human essays by
  non-native English writers were flagged as AI.

They agree that detectors don't work. **They point at opposite policies.** Scarfe's
result reads as an argument for more scrutiny; Liang's reads as an argument for
much less. Read one, and you will design the wrong assessment policy for a business
school where most students write in a second language. Say that part out loud in
this room — it is a BI problem, not a hypothetical.

(Scarfe's paper cites Liang's. The literature already knows. Your agent may not
have said so.)

### Axis C — is the field healthy? Two systematic reviews, one journal, opposite verdicts

- **Crompton & Burke 2023:** the field has matured — publications multiplied,
  and education departments are now the *most common* affiliation, explicitly
  reversing Zawacki-Richter's central complaint.
- **Bond 2024:** the field is not rigorous — 45.5% of its 66 reviews did no
  quality assessment, 34.8% never discussed their own limitations, and ethics
  remains an acknowledged gap.

Same journal. **Ten months apart.** Overlapping corpora. One says the problem was
fixed; the other says the work isn't good enough to tell. Both are systematic
reviews, done properly. This is the axis that surprises people, because it is not
a disagreement about AI at all — it is a disagreement about **what counts as
evidence**, and every discipline in the room has the same fight going on
somewhere.

- **Bearman 2023 sits underneath both:** if only one paper in three decades of top
  HE journals defined "AI", then Crompton's taxonomy and Bond's quality scores are
  both counting instances of an undefined term.

### Axis D — the disagreements that turn out not to be

Worth ten minutes, because the question invites false positives and spotting them
is the actual skill:

- **Chan 2023 vs Chan & Hu 2023** are not two views; they are one author, one city,
  two samples, two papers. Not a disagreement — a merge risk.
- **Chan 2023 vs the room's own assumption.** Everyone expects faculty to be the
  cautious ones. In the data, staff and students answer within 0.15 of each other
  on every item, and staff are *slightly more* worried about students cheating
  (3.93 vs 3.67), not about the technology. The disagreement is between the paper
  and the audience — which is the most useful kind to find.
- **Zawacki-Richter vs Crompton & Burke on "where are the educators?"** looks like
  a contradiction and is really four years passing.

---

## The honesty checkpoint

**Send the room to one cell: the `finding` cell of the `bastani-2025` row.**

Almost every generated table renders it as some version of *"generative AI harms
learning"* or *"students who used AI performed 17% worse."* The paper's own abstract
says something narrower and more interesting:

> **GPT Base** students scored 17% below control on the unassisted exam. **GPT
> Tutor** students were **statistically indistinguishable from control** — point
> estimate −0.004, an order of magnitude smaller. And during practice, *both* AI
> arms massively outperformed control (+48% and +127%).

Why this cell:

- **It is checkable in thirty seconds** — page 1, the abstract, no hunting.
- **The error is not a hallucination.** The model read it correctly and the *table*
  destroyed it, because the finding needs a subordinate clause and the cell has
  room for a verb. That is a better lesson than "AI makes things up", and it is
  the honest one: the failure was in the shape of the question, and the person who
  chose the shape was them.
- **It changes what you would do on Monday.** "AI harms learning" argues for a ban.
  What the paper says argues for *scaffolding* — a design decision, not a
  prohibition. Those are opposite policies from the same study.
- **The title already told them.** *"…without guardrails…"*. Nobody reads titles.

Then the generalisation, which is the point of the whole block:

> Every cell in that table is a summary of a summary. The question is not whether
> to trust it — it's which three cells your argument actually rests on. Check
> those.

**Backups, if that one lands too easily:**

- **`kestin-2025`, the `sample` cell.** The right answer is **194**. The paper also
  contains 233 (enrolled), 142 and 174 (post-test group Ns) and 316 (pre-test
  baseline observations) — because in a crossover design each student contributes
  up to two observations. Every wrong answer is a real number from the paper, which
  is what makes it a good check rather than a gotcha.
- **`scarfe-2024`, the `sample` cell.** **63** AI submissions, not the 33 fake
  student accounts, and not the 1,134 real submissions.
- **`bond-2024`, the `sample` cell.** **66 reviews** — not studies, not students.

---

## Running the block

Prompts that work, in order:

> Summarise `bond-2024.pdf` in five bullets: what question it asks, how it
> answers it, what it studied, what it found, and what it says is missing.

> Now read all twelve PDFs in this folder and build one Markdown table with a row
> per paper and these columns: citation, research question, method, sample,
> main finding. Where a paper's finding has an important qualifier, keep the
> qualifier.

> Which of these papers disagree with each other, and about what? For each
> disagreement, tell me whether it's a real conflict in the evidence or an
> artefact of different methods, samples or dates.

> For the Bastani row, give me the page and quote the sentence you took the
> finding from.

> Check every DOI in the table against Crossref. Flag anything retracted or
> corrected — and tell me what the flag actually says.

> Export the table as `litsweep.csv` and `litsweep.md`.

**Timing (75 min).** ~20 min exploration (`../references/explore.md`) → 10 min
summarise one → 15 min build the table → 15 min the disagreement question,
plenary → 10 min honesty checkpoint → 5 min export. The disagreement discussion
is the part worth protecting; the export is one prompt and can run while people
pack up.

**If someone finishes early:** *"now do this to the PDFs in your own Downloads
folder."* That is the transfer, and it takes one sentence.

---

## Licences — and what you may say about redistribution

Every paper here is open access under a Creative Commons licence that permits
verbatim redistribution with attribution. `SOURCES.md` ships inside the zip and
**is** that attribution; do not remove it.

| Licence | Papers |
|---|---|
| **CC BY 4.0** (8) | Zawacki-Richter 2019, Crompton & Burke 2023, Chan 2023, Chan & Hu 2023, Bearman 2023, Bond 2024, Bašić 2023, Scarfe 2024 |
| **CC BY-NC-ND 4.0** (4) | Kestin 2025, Bastani 2025, Liang 2023, Wang & Fan 2025 |

**The NC-ND four:** non-commercial verbatim sharing is permitted, adapting is not.
A free download from a course website is non-commercial. **Do not re-compress,
crop, extract pages from, or re-typeset those four** — CC's own terms allow
technical format changes, but lossy re-rendering is not worth the argument. If the
zip ever needs to shrink, drop a paper; don't squeeze one.

**Nothing here is paywalled and nothing was scraped past a paywall.** Where a
publisher blocks automated clients (Springer, Elsevier, PNAS all do), the script
fetches the same public CC-licensed PDF from the Internet Archive or Europe PMC.
That is worth one sentence on stage — it is the same lesson as the references
block: *"I couldn't get it" ≠ "it's paywalled" ≠ "it doesn't exist."*

---

## Verification log — what was checked, how, and when

All checks run **2026-08-09**.

| Claim | How it was verified |
|---|---|
| All twelve citations (title, authors, author count, venue, volume, issue, article number, year) | Crossref API, `api.crossref.org/works/<DOI>`, with a mailto User-Agent |
| All twelve licences | Crossref `license` array (`content-version: vor`) **and** the licence statement printed in each PDF |
| Every file is a real PDF | `%PDF` magic bytes + `%%EOF` trailer + minimum size, enforced by the fetch script on every run |
| Every file is the *right* paper | Page count checked, full text extracted, and a title fragment matched in the extracted text — per paper, in the script |
| Every number quoted in this key | Read from the extracted text of the PDF in this folder, not from an abstract or a database |
| Wang & Fan is retracted | Crossref title begins `RETRACTED ARTICLE:`; Retraction Note `10.1057/s41599-026-07310-z` fetched and read (HSSC 13, 528, 22 Apr 2026) |
| `grep -i retract` finds nothing in the retracted PDF's text layer | `pdftotext wang-fan-2025.pdf - \| grep -ic retract` → **0** |
| The Bastani correction is cosmetic | Correction `10.1073/pnas.2518204122` fetched and read — one author's affiliation, production error, 20 Aug 2025 |
| Bastani's published title differs from the SSRN working paper | Crossref: SSRN `10.2139/ssrn.4895486` "Generative AI Can Harm Learning"; PNAS `10.1073/pnas.2422633122` "Generative AI **without guardrails** can harm learning…" |
| Kestin's fifth author is **Ponti**, not the name in most people's memory | Crossref author array + the PDF's own byline |
| `nature.com/articles/XXX.pdf` currently returns a real PDF | Fetched with a browser User-Agent: HTTP 200, `application/pdf`, `%PDF-` — the historical HTML-interstitial trap did **not** fire on 2026-08-09 |
| Springer, Elsevier/Cell, PNAS and MDPI block automated clients | `link.springer.com` and `*.springeropen.com` return a 3,038-byte JS challenge with HTTP **200**; `sciencedirect.com`/`cell.com` and `pnas.org` return **403**; `pmc.ncbi.nlm.nih.gov` serves a proof-of-work interstitial |

### What could **not** be verified

- **Nothing in this key is second-hand except two things**, and both are labelled:
  Crossref's licence metadata (cross-checked against each PDF's own printed licence
  statement, which agreed in all twelve cases), and the *reason* for the Wang & Fan
  retraction, which is only as good as the Retraction Note — the underlying
  "discrepancies" are not itemised by the journal.
- **Access is a fact about today.** The Springer papers come from Internet Archive
  captures and the Elsevier/PNAS ones from Europe PMC. Both could change. **Run
  `python3 scratch/examples/scripts/fetch-litsweep-example.py --check` the week before the course**
  — thirty seconds, and it verifies the twelve files on disk without touching the
  network.
- **The room may find disagreements not listed above.** Referee them the same way:
  ask for the page and the sentence. Two papers "disagreeing" without a quotable
  sentence each is usually the table talking, not the literature.

---

## The line to end on

Nothing in this folder was planted. Twelve real papers, chosen for a topic
everyone in the room already has opinions about — and they contradict each other
about whether AI helps students learn, about whether cheating can be detected,
and about whether the research is good enough to tell. One of them has been
retracted and still reads like a paper.

**The agent found all of that in about four minutes.** It would have taken a
careful reader a full day. What it could not do was decide which contradiction
mattered — and that is the half of the job that was always yours.
