# Leave a trail

**Day 1, afternoon.** Files: `examples/plain-text/`

Everything you did this morning happened *inside* a folder. This block is about what
happens *inside the files* — and about leaving a record of what you did.

> **The idea in one line:** write it down, so it can be checked. Including by you,
> in six months.

Two kinds of writing-down, one idea:

| | The usual way | Leaving a trail |
|---|---|---|
| **Prose** | a Word file; changes invisible | text — you can see exactly what changed |
| **Data** | clicking in Excel | a script — the steps *are* the documentation |

You are not learning to code. You are learning to **ask for the record**.

> **The floor: Track A through Rung 1.** Get the document into text and ask it one
> question about itself whose answer you did not already know — do that and you have the
> whole idea of this block in your hands, which is a complete run rather than a short
> one. The rungs above it are yours to take as far as you like, Track B is opt-in, and
> people will finish this at very different times; that is how it was built, not a race.

---

## Track A — the document (everyone)

Start from `course-handbook.docx`. It's a real course handbook, and it's a mess.

*Same reflex as after lunch, before you let the agent change anything:*

> Commit this before we start.

Save point, then courage.

### Rung 0 · Get it into text

> Convert `course-handbook.docx` to Markdown and save it as `handbook.md`.

*Stuck?* If the conversion fails, the folder already contains `course-handbook.md`.
Use it and move on — the conversion is not the lesson.

### Rung 1 · Make the document answer questions · ⬅ the floor

This is the part that doesn't work in Word. Ask for things *about* the text:

> Make a table of every date and deadline mentioned in this document.

> Do the assessment weights add up to 100%?

> List every promise this document makes to students. Are any of them inconsistent
> with each other?

> Do any two sections cover the same ground? Do they agree?

**Read the answers carefully.** At least one will tell you something about the
handbook you did not know. That is the point of the whole block.

**That's the floor cleared.** Take Rung 2 and beyond as far as you like — or if you're
done and the person next to you isn't, go and help them: whoever finishes first is the
room's help desk, and that holds all three days.

### Rung 2 · Restructure it

> Merge the two overlapping sections into one, and keep the stricter version of
> anything they disagree about.

> Reorder this for a student reading it in week one, not an administrator.

> Translate it to Norwegian but keep the structure and the headings exactly.

### Rung 3 · Publish it twice

> Turn `handbook.md` into both an HTML page and a PDF.

One source, two outputs. Fix a typo once, not twice. (Friday, this becomes a course
page.)

### Rung 4 · For the bold

> Write a one-page student summary from this handbook, then check the summary and
> the handbook agree on every date.

---

## Track B — the data (opt-in)

For anyone who analyses things. Start from `survey-responses.csv` — 21 survey
responses, genuinely filthy.

### Look before you leap

> Describe what's wrong with this data. Don't change anything yet.

### Ask for a *script*, not a cleaned file

This is the whole trick:

> Write a script that cleans this data: standardise the country names, parse the
> dates into one format, handle the missing values sensibly, and flag any
> duplicates. Explain each decision in a comment. Don't hide anything.

Then run it, and read it. You don't need to write the code — you do need to read
what it decided.

### Change your mind, and prove it

> Actually, treat `999` as missing rather than dropping the row. Update the script.

Re-run it. **That file is your methods section** — every decision, in writing,
re-runnable by anyone.

And now the obvious question: *you changed one decision — how do you see exactly what
differs, without reading the whole script again?*

Hold that thought. That's the next block.

---

## The question both tracks end on

> **Could someone else re-run this and get exactly what you got?**

If yes, you've left a trail. If no, you have a result nobody can check — including
you, next spring, when a reviewer asks.

## One honest caveat

The agent's script can be **wrong**. Read it.

But note what you've gained anyway:

> **A wrong script you can read beats a right click you can't remember.**

Reproducible is not the same as correct. It's the thing that makes correctness
*checkable* — which is why the next block is about checkpoints and seeing exactly
what changed.

## Keep

- `handbook.md` and whatever you rendered from it.
- Your cleaning script, if you did Track B.
- One thing the agent told you about your document that you hadn't noticed.

## Worth reading

All free to read unless noted. Read the first one; the rest are there if you want
the evidence.

**If you read one thing**

- **The Plain Person's Guide to Plain Text Social Science** — Kieran Healy (Duke).
  Written for social scientists, not programmers; makes the case without evangelism.
  <https://kieranhealy.org/files/papers/plain-person-text.pdf>
  (The [source of that paper](https://github.com/kjhealy/workflow-paper) is itself
  plain text — the argument, demonstrated.)

**What goes wrong when you click instead of script**

- **Spreadsheet horror stories** — EuSpRIG's running archive of real, named
  incidents with price tags attached. Includes Norway's sovereign wealth fund losing
  roughly **$92 million** to one wrongly entered date in a spreadsheet (disclosed in
  2024).
  <https://eusprig.org/research-info/horror-stories/>
- **Gene name errors are widespread in the scientific literature** — Ziemann, Eren &
  El-Osta (2016), *Genome Biology*. Excel silently converted gene names into dates in
  ~20% of papers with supplementary gene lists. Nobody typed anything wrong — the
  tool did it, on open. <https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7>
  (The [2021 follow-up](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008984)
  found it had risen to ~31% — so the gene-naming committee **renamed human genes**,
  because that was easier than fixing Excel.)
- **A critique of Reinhart and Rogoff** — Herndon, Ash & Pollin (2014), *Cambridge
  Journal of Economics*. A spreadsheet range that skipped five rows, in a paper that
  helped underwrite European austerity.
  <https://peri.umass.edu/wp-content/uploads/joomla/images/WP322.pdf>
  *Told honestly:* the Excel error was one of three problems, not the whole story —
  which is itself a lesson in checking what you repeat.

**What to do instead**

- **Ten Simple Rules for Reproducible Computational Research** — Sandve et al. (2013),
  *PLOS Computational Biology*. Rule 1: track how every result was produced. Rule 2:
  avoid manual data manipulation. Ten minutes to read.
  <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285>
- **Good enough practices in scientific computing** — Wilson et al. (2017), *PLOS
  Computational Biology*. Explicitly for researchers who are *not* software
  engineers. <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510>

**The other side of the argument**

- **Artificial intelligence and illusions of understanding in scientific research** —
  Messeri & Crockett (2024), *Nature*. The best-credentialed sceptical piece: AI tools
  can produce illusions of understanding and scientific monocultures. A Perspective
  essay, not a study. Free author copy:
  <https://static1.squarespace.com/static/538ca3ade4b090f9ef331978/t/65f071f8fd3e3b478a4f4b86/1710256633821/Messeri&Crockett_2024_Nature.pdf>
