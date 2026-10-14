# Instructor key — the references demo (Day 2, 10:30)

Participant-facing files: `wishlist.md` (pin down what you half-remember),
`messy-list.bib` (clean up what you already have) and `explore.md` (find what you
don't know exists). **This file is for you.**

**The two halves, and why both:**

| | `wishlist.md` | `explore.md` |
|---|---|---|
| The task | I know what I want — pin it down | I don't know what's out there |
| Failure is | **loud** — the DOI doesn't resolve | **silent** — you never learn what it missed |
| Teaches | verification | triangulation, and knowing when to stop |

*Retrieval fails loudly; exploration fails silently.* Do the wishlist first — it's
concrete, checkable, and it ends with six verified papers the participant can then
**seed-check** the exploratory search against (rung 4 of `explore.md`). That
dependency is deliberate: it means the coverage test costs no extra props and uses
material they produced themselves twenty minutes earlier.

**Placement note.** The wishlist fits the 10:30 references block. `explore.md` is the
natural *opening* of the 13:00 literature sweep — explore → gather → compare → verify
across one afternoon — and it fixes the sweep's current cold start ("here is a folder
of PDFs" with no account of where a folder of PDFs comes from). Participants with
their own topic feed their exploration into the sweep; the provided PDF folder stays
the fallback for everyone else.

Every citation below was verified against Crossref, cross-checked in OpenAlex /
Semantic Scholar / PubMed, OA status checked via Unpaywall, and every "free" URL
fetched and opened to confirm it is the real article.

**You do not need to plant a fake.** This literature is *already* a minefield —
every item on the wishlist has a genuine, checkable trap. That's why it was chosen.

---

## The six items, and what should come back

### 1. "The ASA statement about p-values, 2016?"

**Wasserstein, R. L., & Lazar, N. A. (2016).** "The ASA Statement on p-Values:
Context, Process, and Purpose." *The American Statistician* **70**(2), 129–133.
DOI `10.1080/00031305.2016.1154108`

- 🪤 **The title has three attested forms.** The typeset PDF (and T&F's own "cite
  this article" line) says **"The ASA's Statement"** — possessive. Crossref, OpenAlex
  and the current publisher page say **"The ASA Statement"** — no possessive. And the
  ASA *press release* is a **different document** titled "Statement on Statistical
  Significance and P-Values."
- 🪤 An agent asked for "the ASA statement" will often return the **press release** as
  if it were the journal article.
- 🪤 Dates multiply: posted 7 Mar 2016, Crossref print date 2 Apr, published online
  9 Jun.
- **Free**, but Taylor & Francis blocks bots — working mirror:
  `https://www.stat.berkeley.edu/~aldous/Real_World/ASA_statement.pdf`

### 2. "A Nature piece about retiring significance, hundreds of signatories"

**Amrhein, V., Greenland, S., & McShane, B. (2019).** "Scientists rise up against
statistical significance." *Nature* **567**(7748), 305–307.
DOI `10.1038/d41586-019-00857-9`

**The best trap in the whole exercise.**

- 🪤 **Two titles, both correct.** Every database says *"Scientists rise up against
  statistical significance."* The **printed page** says **"Retire statistical
  significance."** No single source has both. Participants who half-remember the
  printed headline will think the agent got it wrong — it didn't.
- 🪤 **It is a Comment, not a study.** Routinely miscited as research.
- 🪤 **The 800+ signatories are not authors.** There are exactly three. Watch for an
  agent implying otherwise.
- 🪤 It has a **news DOI** (`d41586-`), which breaks some reference managers.
- 🪤 Don't confuse it with **Amrhein & Greenland (2018)**, "Remove, rather than
  redefine, statistical significance," *Nat Hum Behav* 2(1):4,
  DOI `10.1038/s41562-017-0224-0` — a *different*, two-author, one-page Letter.
- **Free:** `https://media.nature.com/original/magazine-assets/d41586-019-00857-9/d41586-019-00857-9.pdf`

### 3. "Something called 'the garden of forking paths'"

**⚠️ There is no published paper with that title.** This is the item that catches
almost everyone.

- The **published** work is **Gelman, A., & Loken, E. (2014)**, "The Statistical
  Crisis in Science," *American Scientist* **102**(6), 460–465,
  DOI `10.1511/2014.111.460`. "Garden of forking paths" is a phrase from its subtitle.
- There is a **separate, never-published 2013 manuscript** actually titled "The
  garden of forking paths: …" — no DOI, no journal, no volume.
- 🪤 **An agent will very often invent a journal, volume and DOI for the 2013
  manuscript, or fuse the two into one hybrid citation.** This is the single most
  likely fabrication in the exercise — watch for it, and make the room check.
- 🪤 Crossref *and* OpenAlex both give the page as "460" only. The real range is
  **460–465** (read from the printed PDF). So even the databases are wrong here.
- **Free:** `https://sites.stat.columbia.edu/gelman/research/published/ForkingPaths.pdf`

### 4. "A psychology paper — prove anything if you're flexible"

**Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011).** "False-Positive
Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting
Anything as Significant." *Psychological Science* **22**(11), 1359–1366.
DOI `10.1177/0956797611417632`

- 🪤 The long colon-subtitle is **very often dropped**, leaving a citation that looks
  fine but doesn't match the record.
- **Paywalled** (SAGE). Good — this is the one that should end up in
  `to-fetch.md` with its DOI, demonstrating the library handoff.

### 5. "Lower the threshold to 0.005" + the rebuttal

**Benjamin, D. J., Berger, J. O., Johannesson, M., … Johnson, V. E. (2018).**
"Redefine statistical significance." *Nature Human Behaviour* **2**(1), 6–10.
DOI `10.1038/s41562-017-0189-z`

- 🪤 **72 authors.** Truncation is inevitable — but note *who* gets hidden: the last
  author, **Valen Johnson**, originated the p<0.005 argument.
- 🪤 **Year is genuinely ambiguous:** Crossref/OpenAlex/S2 say **2017** (online Sept
  2017); PubMed and the print issue say **2018**. Both defensible. A good moment to
  discuss what "the year" even means.

The rebuttal: **Lakens, D., Adolfi, F. G., Albers, C. J., … Zwaan, R. A. (2018).**
"Justify your alpha." *Nature Human Behaviour* **2**(3), 168–171.
DOI `10.1038/s41562-018-0311-x` — **88 authors.**

- 🪤 Lovely detail: TU Eindhoven's own repository renders the citation as
  *"+25 authors, Lakens, D., Anvari, F., & Isager, P. M. (2018)"* — visibly wrong on
  the PDF cover sheet. Even institutional repositories mangle mega-author papers.

### 6. "A journal that banned p-values"

**Trafimow, D., & Marks, M. (2015).** "Editorial." *Basic and Applied Social
Psychology* **37**(1), 1–2. DOI `10.1080/01973533.2015.1012991`

- 🪤 **The title is literally the word "Editorial."** Agents reliably invent a
  descriptive title like "Banning the null hypothesis significance testing procedure."
  If you see a nice informative title here, it was made up.
- 🪤 There are **three consecutive Trafimow & Marks editorials all titled
  "Editorial"** (2014 v36, 2015 v37, 2016 v38). Only the **2015** one contains the ban.
- **Paywalled** (T&F).

---

## The catch that makes the whole block land

**Taylor & Francis returns 403 to any automated client — on every path.** Which means
the five most central papers in this debate (items 1, 2's cousins, 5's venue-mates,
6, plus the entire *American Statistician* special issue) are **formally open access
and completely unreachable to an agent.**

So: **if an agent claims it "downloaded and read" Wasserstein & Lazar (2016), it is
using a mirror, a cache, or making it up.** That is a clean, reproducible catch — and
it teaches something more useful than "AI hallucinates": *the tool's failure is not
always what it appears to be.* "I couldn't get the PDF" ≠ "the paper is paywalled" ≠
"the paper doesn't exist."

Bot-friendly, if you want a step to succeed on stage: **PLOS, Springer
(`link.springer.com/content/pdf/`), arXiv, Project Euclid,
`media.nature.com/original/magazine-assets/`, amstat.org, and university author
pages.**

⚠️ **`nature.com/articles/XXX.pdf` is the nastiest failure mode:** it returns **HTTP
200 with `Content-Type: text/html`** — an interstitial. A naive agent saves an HTML
file named `.pdf` and **reports success.** If you want one moment that justifies the
whole verification habit, open a "downloaded" PDF and find it's a login page.

---

## Optional extras

- **For a business school:** Brodeur et al. (2016), "Star Wars: The Empirics Strike
  Back," *AEJ: Applied Economics* 8(1), 1–32, DOI `10.1257/app.20150044` — 50,000
  tests in *AER*/*JPE*/*QJE* show a "two-humped camel" of missing p-values just above
  0.05. Economics' own evidence. (Often miscited to its SSRN working papers.)
- **The retraction card, and it's a marketing paper:** Brian Wansink's
  "Attractive names sustain increased vegetable intake in schools," *Preventive
  Medicine* 55(4):330–332, DOI `10.1016/j.ypmed.2012.07.012`. Crossref now titles it
  **"RETRACTED: …"** — but **the DOI still resolves and still yields a normal-looking
  citation.** Ask the room: would you have caught that?
- **The ASA walking it back:** Benjamini et al. (2021), "The ASA President's Task
  Force Statement on Statistical Significance and Replicability," *Annals of Applied
  Statistics* 15(3), 1084–1085, DOI `10.1214/21-aoas1501`. Published **three times**
  in 2021 in three venues; Crossref returns **no page numbers**, so agents fabricate
  them. (Correct: 1084–1085.)

---

# Part 2 — "Clean what you have" (`messy-list.bib`)

The second half of the 10:30 block. The wishlist half asks *"can you find it?"*; this
half asks *"is what I already have true?"* — which is the version of the problem
almost everyone in the room actually has sitting on their hard drive.

**This one does contain planted material** — three fabricated papers and two wrong
DOIs — and the rest of the file is honest mess. Everything planted was verified
against Crossref and doi.org on **2026-08-09**; the verification log is at the end of
this section.

## Why a `.bib` and not a Markdown list

- **It is the format the answer has to come out in anyway.** The gather workflow in
  `handouts/references.md` ends with "add a verified BibTeX entry to
  `references.bib`". Cleaning a `.bib` closes the same loop from the other end.
- **Only BibTeX can carry half the mess.** Entry types, brace protection, field-name
  capitalisation, `and others`, quotes-versus-braces, a missing `year` that makes
  BibTeX itself emit a warning — a Markdown bullet list flattens all of that into
  prose and the exercise loses its teeth.
- **It is what they will actually inherit**: a co-author's EndNote export, a Zotero
  dump, a supervisor's file that has been passed around since 2014.
- **It diffs.** The cleaned file is a git commit, and `git diff` shows exactly what
  the agent changed. That is the day's other lesson arriving for free.
- **Nobody in the room knows BibTeX, and that is the point.** They are not asked to
  write it — only to point an agent at it. It reinforces the handout's line: *you
  never touch the file format.*

## The file at a glance

17 entries, 15 distinct works: **10 sound**, **2 real papers carrying a wrong DOI**,
**3 fabricated**, plus **2 duplicate entries** of works already in the file.

| # | Key | Verdict | What's wrong | How to catch it |
|---|---|---|---|---|
| 1 | `wasserstein2016` | ✅ sound | Possessive title (`The ASA's Statement`) differs from Crossref's (`The ASA Statement`) — **both attested**. `ASA` and `p-Values` not brace-protected, so plain styles render "the asa's statement on p-values" | Resolve the DOI; then don't "fix" the title — record both. Add `{ASA}` / `{p}` protection |
| 2 | `simmons2018econ` | 🪤 **fake** | No such paper | DOI 404s; title search returns nothing — see trap 4 |
| 3 | `Amrhein2019` | ✅ sound | Printed headline (`Retire statistical significance`) ≠ database title (`Scientists rise up…`) — **both correct**. Missing `number = {7748}`; `305-307` should be `305--307` | DOI resolves. The title clash is a genuine ambiguity, not an error |
| 4 | `ref17` | ✅ sound | **No `year` field** (should be 2005). Journal abbreviated; junk `note = {cited by 12,000+}`; meaningless key | BibTeX warns on a missing year in `@article`. Crossref supplies 2005 |
| 5 | `trafimow_marks_2015` | 🪤 **wrong DOI** | DOI resolves — to the *2016* editorial | See trap 1. Compare volume and year, not just "it resolved" |
| 6 | `SIMMONS_2011` | ✅ sound | Nothing. Crossref splits this record into `title` + `subtitle`, so a naive field-by-field comparison reports a false mismatch | Read Crossref's `subtitle` field before declaring the entry wrong |
| 7 | `gelman-loken-forking` | ✅ sound | Nothing — and it has **no DOI**, because it was never published | Fetch the URL and read page 1: right title, right authors, dated 14 Nov 2013. Watch the agent try to *invent* a journal and DOI, or delete it as unverifiable. Both are wrong |
| 8 | `wasserstein2018twoyears` | 🪤 **fake** | No such paper | DOI 404s — see trap 3 |
| 9 | `benjamin2018redefine` | 🪤 **wrong DOI** | DOI resolves — to the rebuttal | See trap 2. Also `and et al.` creates an author literally named "et al." |
| 10 | `gelman-loken-2014` | ✅ sound | `pages = {460}` is **wrong** — the article runs 460–465. The error was copied faithfully from Crossref, which is itself wrong. Title all-lowercase | Open the PDF: 6 pages, 460 through 465. The database is not the last word |
| 11 | `ASA_2016_statement` | ♻️ duplicate | Same work as #1: `@misc`, initials-only authors, truncated title, journal shoved into `howpublished`, DOI hidden in `note` | **The same DOI appears twice in the file** — once as a `doi` field (#1), once buried in this entry's `note`. Scanning the file *text* for DOI strings catches it in one pass; scanning only `doi` fields does not |
| 12 | `lakens_etal_2018` | ✅ sound | `and others` silently truncates **88** authors; journal abbreviated | Crossref reports 88 authors. Truncation is fine; not *saying* it isn't |
| 13 | `ioannidis2019wars` | 🪤 **fake** | Neither the chapter nor the book exists | See trap 5. Check the **book**, not the chapter |
| 14 | `Brodeur2016StarWars` | ✅ sound | Nothing substantive. Capitalised field names (BibDesk export — harmless, BibTeX is case-insensitive); `First Last` author style | DOI resolves exactly. Leave it alone |
| 15 | `simmons2012` | ♻️ duplicate | Same work as #6 with **year 2012** (should be 2011), truncated title, abbreviated journal, no issue, no DOI, `1359--66` shorthand | Near-identical title + authors to #6; a title search resolves it to the 2011 record |
| 16 | `benjamini2021asa` | ✅ sound | **No `pages`** — because Crossref has none. Correct answer: 1084–1085 | Project Euclid prints the citation line. Watch for the agent *fabricating* a page range to fill the gap |
| 17 | `wansink2012veg` | 🪤 **retracted** | Every field is correct and the DOI resolves. The paper was **retracted** | Crossref's title field literally starts `RETRACTED:` — see trap 6 |

---

## 🪤 Trap 1 — the DOI that resolves to a near-identical paper

**`trafimow_marks_2015`.** The best teaching object in the file.

The entry claims Trafimow & Marks (2015), "Editorial," *Basic and Applied Social
Psychology* **37**(1), 1–2 — the editorial that banned p-values. All of that is right.
The DOI in the file is `10.1080/01973533.2016.1141030`.

**It resolves.** Cleanly, to Taylor & Francis, with an HTTP 302 and no complaint. And
what it resolves to is:

> Trafimow, D., & Marks, M. (2016). "Editorial." *Basic and Applied Social
> Psychology* **38**(1), 1–2.

Same two authors. Same title. Same journal. **Same page numbers.** Only the volume and
the year differ — and the 2016 piece is the one-year *follow-up*, not the editorial
that announced the ban. Correct DOI: `10.1080/01973533.2015.1012991`.

- 🪤 Every shallow check passes: the link works, the authors match, the title matches,
  the journal matches, the pages match.
- **How to catch it:** ask the agent to print the resolved record *beside* the entry,
  field by field, and to compare **volume and year** — not just "does it resolve."
- **The line to say out loud:** *"The DOI resolved" is not a check. "The DOI resolved
  to this paper" is a check.*

> ⚠️ **Know how this one actually fires before you demo it (re-checked 9 Aug 2026).**
> The DOI resolves for *you*, in a browser. But it lands on **Taylor & Francis**, which
> 403s automated clients — so from the agent's side `doi.org` returns **403, not 200**.
> Crossref's metadata is fine (that's how the swap is confirmed), but a naive agent may
> report *"I couldn't verify this one"* rather than *"this resolves to the wrong paper."*
>
> That is not a broken trap — it is a **second, different lesson**, and it's the one
> from Part 1: *"I couldn't get it" ≠ "it's paywalled" ≠ "it doesn't exist."* Push with:
>
> > You got a 403. That's the publisher blocking robots, not a missing paper. Look the
> > DOI up in Crossref instead and tell me what it actually points to.
>
> **If you want the clean, guaranteed silent-wrong-resolution demo, use Trap 2** — its
> DOI returns a plain **200** and hands back the wrong paper with no drama. Do Trap 2
> on the projector; leave Trap 1 for them to hit in the exercise, where the 403 detour
> is a feature.

## 🪤 Trap 2 — the DOI that resolves to the rebuttal

**`benjamin2018redefine`.** Every field is correct except one.

DOI in the file: `10.1038/s41562-017-0224-0`. It resolves to:

> Amrhein, V., & Greenland, S. (2017). "Remove, rather than redefine, statistical
> significance." *Nature Human Behaviour* **2**(1), 4.

Same journal, same volume, same issue, adjacent page, and the resolved title
*contains the words* "redefine … statistical significance". Skim it and the entry
looks confirmed. Correct DOI: `10.1038/s41562-017-0189-z`.

- 🪤 This is not merely a different paper — **it is the paper arguing the opposite.**
  Ship the citation and your sentence now credits Benjamin et al. with a position they
  spent 72 authors' worth of effort opposing.
- **How to catch it:** read the resolved title *in full*, and count authors. Benjamin
  et al. has **72**; Amrhein & Greenland has **2**. Any author-count comparison kills
  it instantly.
- Bonus for the room: this is the mistake a human makes with two browser tabs open,
  not a mistake an AI invented. Reference managers do it constantly.

## 🪤 Trap 3 — the sequel that was never written

**`wasserstein2018twoyears`.** "The ASA Statement on p-Values: Two Years On,"
*The American Statistician* **72**(2), 178–186, DOI `10.1080/00031305.2017.1401977`.

Tempting because a follow-up genuinely exists — just not this one:

- **Real:** Wasserstein, Schirm & Lazar (2019), "Moving to a World Beyond
  'p < 0.05'," *The American Statistician* **73**(sup1), 1–19,
  DOI `10.1080/00031305.2019.1583913`. Three authors, different title, different year.
- **Also real:** a "10 years on" piece in *Significance* (Feb 2026),
  DOI `10.1093/jrssig/qmag004`.

So the shape of the fake is right; only the fake is wrong.

- **How to catch it:** the DOI returns **404 from both `doi.org` and the Crossref
  API**. A title search in Crossref and OpenAlex returns nothing resembling it.
- **Deeper, if someone wants it:** *TAS* volume 72, issue 2 runs pages 121–212 with no
  gaps, and 178–186 straddles two real papers ("The Tale of Cochran's Rule," 175–183,
  and "Estimating Desired Sample Size…," 184–190). Fabricated page ranges usually sit
  on top of somebody.

## 🪤 Trap 4 — the paper this room *wants* to exist

**`simmons2018econ`.** "False-Positive Economics: Undisclosed Flexibility in Empirical
Research," *Journal of Economic Perspectives* **32**(3), 197–216,
DOI `10.1257/jep.32.3.197`.

Right authors. Right kind of work — they wrote the psychology one. Right journal for a
methods essay. Plausible year. And for a business school it is the paper you *hope*
someone wrote.

- **How to catch it:** DOI 404s at `doi.org` and Crossref; title search returns
  nothing. The real Simmons–Nelson–Simonsohn record is `10.1177/0956797611417632`,
  already in the file as entry #6.
- **Deeper:** AEA DOIs encode `volume.issue.firstpage`. *JEP* 32(3) contains no
  article beginning on page 197 — pages 195–214 are "Compensation and Incentives in
  the Workplace." The DOI could not have existed even in principle.
- **The point to make:** wanting a paper to exist is precisely the state in which
  people stop checking. This is the entry the room will defend.

## 🪤 Trap 5 — the book chapter

**`ioannidis2019wars`.** Ioannidis, "The Significance Wars: Why Thresholds Persist,"
in Greenland & Lakens (Eds.), *Statistical Inference After the Replication Crisis*,
Cambridge University Press, 2019, pp. 45–68. **No DOI.**

Book chapters are the softest target in any bibliography: plenty of legitimate
chapters have no DOI and no Crossref record, so "I couldn't find it" proves exactly
nothing. Fabrications hide in that gap.

- **The move that works:** don't check the chapter — **check the book.** Search the
  publisher's catalogue for the title. No such Cambridge University Press book exists.
  One prompt, decisive answer.
- 🪤 **And the counterweight is three entries above it.** `gelman-loken-forking` also
  has no DOI, no journal and no Crossref record — and is completely real. If anyone
  proposes "no DOI ⇒ delete it," that rule deletes the Gelman & Loken manuscript and
  keeps the Ioannidis chapter. **"No DOI" is not a verdict.**

## 🪤 Trap 6 — the one nobody planted

**`wansink2012veg`.** Authors right, title right, journal right, volume, issue, pages
and year all right. The DOI resolves. Everything a checker looks for passes.

The paper was **retracted in 2017.** Crossref's title field for it literally begins
`RETRACTED:` — and `doi.org` still hands you a normal-looking article page.

Ask the room: *would you have caught that?* Then note the fix is one line in the
prompt — "flag anything retracted or corrected" — and it costs nothing to add forever.

---

## What "done" looks like

A cleaned `references.bib` plus a report that, entry by entry:

1. **Deletes** the three fabrications, naming the check that killed each one.
2. **Repairs** the two wrong DOIs — and says what the bad DOI pointed at, because
   *that* is what makes the failure vivid.
3. **Merges** the two duplicate pairs, keeping the better-populated record.
4. **Fills** the missing year (#4) and the missing pages (#16 → 1084–1085) from
   sources it names.
5. **Corrects** #10 to 460–465 and says the database was wrong.
6. **Flags** the retraction (#17).
7. **Leaves alone** #1, #3, #6, #7, #14 — and explains why each apparent problem is
   not one. This item is the hard one, and the one worth praising.
8. Ends with a list of **what it could not verify.**

**The failure to watch for on stage:** an agent that "cleans" the file into
tidy uniformity — same author format, same journal names, no duplicates — while
leaving the three fakes in and both wrong DOIs untouched. It will look like excellent
work. That is the whole lesson: **a polished bibliography is not a correct
bibliography.**

## The prompt to give the room

> This `.bib` file was handed to me by a co-author and nobody has ever checked it.
> Go through it entry by entry.
>
> For each one: does the paper exist? Does the DOI resolve, and does it resolve to
> **this** paper — same title, same authors, same journal, same volume, same year?
> Check retractions and corrections too.
>
> Then: delete anything you can show does not exist, fix what is fixable, merge
> duplicates, and give me a table of every entry with the verdict and the evidence.
> **List separately anything you could not verify either way.** Do not guess, and do
> not invent a DOI for anything that lacks one.

Then the second prompt, which is where it gets good:

> Now turn that into a skill called `check-refs`, and run it on my own `.bib`.

## Verification log — what was checked, how, and when

All checks run **2026-08-09**.

**Crossref API**, `https://api.crossref.org/works/<DOI>`, with a mailto User-Agent.
Confirmed title, authors, author count, journal, volume, issue, pages and dates for
all 11 resolving DOIs in the file. **`doi.org`** checked separately for HTTP status
and redirect target on all 13 DOI strings.

| Claim in this key | How it was verified |
|---|---|
| All 10 sound entries' metadata | Crossref record fetched and compared field by field |
| `10.1080/01973533.2016.1141030` → 2016 editorial, BASP 38(1), 1–2, Trafimow & Marks | Crossref record + `doi.org` 302 → tandfonline |
| `10.1080/01973533.2015.1012991` is the correct 2015 DOI | Crossref: "Editorial," BASP 37(1), 1–2, 2015 |
| Only three Trafimow & Marks "Editorial" pieces exist (2014 v36, 2015 v37, 2016 v38) | Crossref journal query on ISSN 0197-3533 |
| `10.1038/s41562-017-0224-0` → Amrhein & Greenland, "Remove, rather than redefine…", NHB 2(1), 4 | Crossref record + `doi.org` 302 → nature.com |
| Benjamin et al. has 72 authors; Lakens et al. has 88 | Crossref author arrays counted |
| `10.1080/00031305.2017.1401977` does not exist | Crossref **404**, `doi.org` **404** |
| `10.1257/jep.32.3.197` does not exist | Crossref **404**, `doi.org` **404** |
| No paper titled "The ASA Statement on p-Values: Two Years On" | Crossref bibliographic search, OpenAlex search, web search — nothing |
| No paper titled "False-Positive Economics…" by those authors | Crossref bibliographic search, OpenAlex search, web search — nothing |
| No CUP book *Statistical Inference After the Replication Crisis*, no chapter "The Significance Wars" | Crossref search, OpenAlex search, web search incl. cambridge.org — nothing |
| *TAS* 72(2) runs 121–212 with no gaps | Crossref journal query on ISSN 0003-1305, all of volume 72 listed by page |
| *JEP* 32(3) has no article starting at 197; 195–214 is "Compensation and Incentives in the Workplace" | Crossref journal query on ISSN 0895-3309 |
| Gelman & Loken (2014) really runs 460–465 | PDF downloaded from `sites.stat.columbia.edu` — 6 pages, printed 460–465. Crossref says "460" |
| Benjamini et al. (2021) really runs 1084–1085 | Project Euclid citation line: "Ann. Appl. Stat. 15(3): 1084-1085 (September 2021)". Crossref has no pages |
| Gelman & Loken (2013) manuscript is real | PDF downloaded from `stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf` — correct title, both authors, dated 14 Nov 2013 |
| Amrhein et al. printed headline is "Retire statistical significance" | PDF downloaded from `media.nature.com` — headline read from page 1, alongside "more than 800 signatories" |
| Wasserstein & Lazar's typeset title is possessive | PDF downloaded from the Berkeley mirror — the article header *and* its own "To cite this article" line both read "The ASA's Statement on p-Values", 70:2, 129–133 |
| Wansink et al. is retracted and still resolves | Crossref title reads `RETRACTED: Attractive names…`; `doi.org` 302 → Elsevier |

## What could **not** be verified

Stated plainly, because a key with an unchecked claim in it would defeat the point of
the exercise.

- **The contents of the 2016 BASP editorial.** Taylor & Francis returns 403 to every
  automated client, so it was not read. Secondary sources describe it as the one-year
  follow-up defending the ban; the 2015 editorial is the one that announced it. If you
  want to characterise the 2016 piece on stage, read it through BI's library first.
- **Non-resolution is a fact about today.** `10.1080/00031305.2017.1401977` and
  `10.1257/jep.32.3.197` 404 as of 2026-08-09. Publishers do mint DOIs continuously —
  **re-run the two `doi.org` checks the week before the course.** Thirty seconds, and
  if one ever starts resolving, that is a better story than the one it replaced.
- **Absence of evidence, honestly labelled.** The three fakes were searched in
  Crossref, OpenAlex and the open web and returned nothing. That is strong, not
  absolute: a chapter in an unindexed book cannot be disproved by database search
  alone. Which is exactly why trap 5's real check is *"does the book exist?"* rather
  than *"is the chapter in Crossref?"*

---

## The line to end on

Split it, because the two halves earn different closing lines.

**The wishlist half:** nothing there was invented to trip anyone up. Every trap is a
real property of a real literature — wrong titles in databases, phantom titles
everyone cites, mega-author lists, papers that are "open access" and unreachable, a
retracted paper whose DOI still works.

**The messy-list half:** three of those papers *were* invented, deliberately, and two
DOIs were deliberately pointed at the wrong real paper. Say so at the end — it makes
the point sharper, not weaker. The fabrications are indistinguishable from the honest
mess around them **by inspection**, and they stop being indistinguishable **the moment
anyone checks**. The room just watched both halves of that sentence be true.

**This is what checking actually involves.** The agent makes it fast. It does not
make it optional.

---

# The opening beat — "this is in the literature right now"

*Sourcing for the ~7-minute open of the 10:30 block. Every claim below was checked
on 10 Aug; where it couldn't be, that's stated.*

## 1. The audit ✅

**Topaz, M., Roguin, N., Gupta, P., Zhang, Z., & Peltonen, L.-M. (2026).**
"Fabricated citations: an audit across 2·5 million biomedical papers."
*The Lancet*, 1779–1781. DOI `10.1016/S0140-6736(26)00603-3`

- **97.1 million references** verified; **4,406 fabricated** across **2,810 papers**.
- **1 in 277** PubMed-indexed papers, first seven weeks of 2026.
- Trend: **1 in 2,828 (2023) → 1 in 458 (2025) → 1 in 277 (2026)** — roughly
  12-fold in two years, sharpest inflection mid-2024.
- Led by **Maxim Topaz**, Columbia Data Science Institute. Verified via Crossref;
  figures via Retraction Watch's write-up (7 May 2026).

🪤 **Two honesty obligations, and they cost you nothing:**
- It is a **Letter**, not a research article. Cite it as one.
- **Flemyng and Hosseini have publicly questioned the methodology transparency**,
  and the analysis doesn't distinguish scientifically critical references from
  incidental ones. Volunteer this. In a block about citing precisely, being caught
  overselling your own supporting citation is unrecoverable.

⚠️ **thelancet.com 403s automated clients** — same failure class as Taylor &
Francis above. Crossref's API resolves it fine. Another live instance of *"I
couldn't fetch it" ≠ "it doesn't exist."*

## 2. The close-to-home example ✅ — **verified 10 Aug, PDF in hand**

**The paper** (via Crossref; PDF at `examples/references/pdf/`, gitignored):

> **"A Bias-Corrected Test Statistic for Confirmatory Factor Analysis Under
> Non-Normality."** Muda, N., & Yangxuan, S. *Structural Equation Modeling: A
> Multidisciplinary Journal*, **33**(3), 456ff. Issued 29 Jan 2026.
> DOI `10.1080/10705511.2025.2606043`.
> **No retraction or correction recorded in Crossref as of 10 Aug 2026** — it is
> standing in the literature as you read this.

**The fabricated reference, exactly as printed in its bibliography:**

> Foldnes, N., & Grønneberg, S. (2024). *Factor analysis with improved chi-square
> tests.* British Journal of Mathematical and Statistical Psychology, **77**, 1–23.
> `https://doi.org/10.1111/bmsp.12295`

**What that DOI actually resolves to** — cleanly, HTTP 302 → 200, no error at all:

> **"Editorial acknowledgement."** *British Journal of Mathematical and Statistical
> Psychology*, **76**, 257–258 (2022). **No authors.**

Every element is wrong except the journal name: title, year, volume, pages,
authors. Crossref returns nothing resembling "Factor analysis with improved
chi-square tests." Foldnes and Grønneberg are real, do publish together, and do
work in exactly this area — their genuine joint work includes "The Asymptotic
Covariance Matrix and its Use in Simulation Studies" (*SEM*, 2017). That's what
makes it land: **everything about the citation is plausible except its existence.**

### 🔥 The part that makes this better than any synthetic trap

It is **not just a bad citation.** The paper defines "**Foldnes F1**" and
"**Foldnes F2**" corrections from that source, then reports **numerical results
for them** — Type I error rates (0.148, 0.172), chi-square values, percentage
improvements (40.8%, 4.2%) — across multiple tables and the abstract.

> There are simulation results, in a peer-reviewed methods journal, for methods
> whose source document does not exist.

Say that sentence slowly. It is the whole block in one line.

### How to run it

1. **Show the citation** from the bibliography. Ask the room: *anything wrong with
   this?* Nothing is. It's beautifully formatted, plausible authors, right journal,
   live DOI.
2. **Resolve the DOI on the projector.** It works — that's the point. Then read
   what it landed on: an untitled 2022 editorial acknowledgement.
3. **Then the escalation:** page back to the results tables. The numbers are there.
4. **The line:** *"This is a journal I publish in. Foldnes is a colleague. The
   method named after him does not exist."*

### ⚠️ Two limits on the claim — know exactly which one you're making

**Airtight, say it freely:** *the paper they cite does not exist.* The DOI resolves
to a 2022 editorial acknowledgement. Verified against Crossref.

**Not yet proven — be careful:** *the method does not exist.* Foldnes genuinely
works on chi-square corrections in CFA under non-normality — **Foldnes & Olsson
(2015), "Correcting Too Much or Too Little? The Performance of Three Chi-Square
Corrections," *Multivariate Behavioral Research***, and the Foldnes & Grønneberg
**pEBA** (penalized eigenvalue block averaging) line. So "Foldnes F1/F2" sits in a
real research area and *might* garble something real.

> 📌 **Settle this with Foldnes before Thursday — it's a five-minute conversation
> and you're the one person who can have it.** The room will contain people who
> know the difference between "miscited a real method" and "simulated a method
> that doesn't exist," and the second claim is much heavier. If unresolved, make
> only the airtight claim; it is more than strong enough on its own.

It also decides how serious this is. If F1/F2 garble real estimators, the
simulation may be sound and mislabelled. If they correspond to nothing
implementable, the numbers in those tables came from somewhere else — a different
category of problem entirely.

### The framing: attack the system, and say retraction is *good for them*

Show the evidence — you have it — and put the weight on the system, not the two
authors. The question that implicates the room: **"how did this pass peer review
in a methods journal, where the referees are exactly the people who would know?"**

Then say the generous thing, because it is also the rigorous thing:

> **The best available outcome for these authors is retraction**, and it is
> becoming less available every month.

The case, if anyone pushes: audits like Topaz et al. are now scanning millions of
papers for exactly this pattern, so it *will* be found — and found-by-audit is far
worse for a career than retracted-by-choice. Self-initiated correction carries a
fraction of the damage of externally-discovered fabrication. And a corrigendum may
not be enough here: the paper's central claim is that its proposed statistics beat
existing corrections, so if part of the comparison baseline can't be sourced, the
problem is in the results table, not the reference list.

**Why bother saying it:** someone in the room *will* feel the "witch hunt" reflex,
and this defuses it before it's voiced. The humane conclusion and the rigorous one
coincide — which lets you deliver a hard example without punching down. You are
not calling for punishment; you are pointing at two people the system left holding
something they now cannot put down. That is also, incidentally, the honest reason
the whole block exists.

✅ **Bonus, and it's free:** `tandfonline.com` 403s every automated client, so this
paper is *unreachable to an agent* — the exact trap documented above. Show the 403
first, then reveal you got it through the library. **"I couldn't fetch it" ≠ "it
doesn't exist"**, demonstrated on the instructor's own material, one minute before
the fabrication reveal.

📌 **And note what this is an instance of:** the clean-200-lands-on-the-wrong-paper
trap that `messy-list.bib` plants synthetically (Trap 2). The real literature
supplied a live one, in the instructor's own field, uncaught by peer review. Use
the real one; keep the synthetic as the exercise.

## 3. "Models got better; practice didn't" — how to say it honestly

The claim to make **emphatically**: a current model *with search* does not invent
a DOI. The failure mode has changed — you now get a **wrong** paper or a **failed
fetch**, and both are catchable in seconds. That is a different world from
memory-only generation, which fabricated freely and always did.

The rise through 2026 is best read as the **installed base of practice**, not
frontier capability: free tiers, memory-only prompting, no checking step — and a
publication pipeline that means papers appearing in early 2026 were largely
drafted with 2024–2025 tools.

⚠️ **State that as your reading, not as a finding.** The Lancet audit does **not**
break fabrication down by model, so the causal story is an inference. Own it as
one; it's still the most plausible account, and claiming more than the data
supports is the one move that would cost you the room.

❌ **Do not quote a per-model citation-hallucination percentage.** Searching for
2026 figures returns confident numbers (e.g. "the best model still fabricates
14.23% of citations") from **SEO content farms with no traceable methodology**. No
quality primary source gives a clean per-model reference-fabrication rate. What
*is* well supported is the mechanism: **retrieval grounding is the single largest
mitigation, cutting hallucination on the order of 75–90%.**

✅ **Prove it live instead — you already have the prop.** Re-run the
garden-of-forking-paths query (item 3 above) on a current model **with search on**.
It resolves to Gelman & Loken (2014) or reports that it can't find the title. The
room watches capability and its limit in the same thirty seconds, which no
benchmark number can do.

## Further reading, if the discussion goes long

- **Nature (2026)**, "Hallucinated citations are polluting the scientific
  literature. What can be done?" — `d41586-026-00969-z`.
- ***Accountability in Research* (2026)** — argues hallucinated citations may
  constitute **research misconduct** when citations function as data.
  DOI `10.1080/08989621.2026.2645390`. The sharpest framing for a room of
  academics: this isn't sloppiness, it may be fabrication in the formal sense.
- **NeurIPS 2025 fabricated-citation taxonomy** (arXiv 2602.05930) — 100 fabricated
  citations found in *elite* peer review. Useful against "that only happens in
  low-quality journals."
