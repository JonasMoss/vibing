## Today’s finish line

Use an agent for one genuine research task and verify at least one important
part of its output against the source.

The point is neither blind trust nor ritual scepticism. The point is a workflow
in which fast work can still be checked.

## Morning — references, and your first *skill*

You have already met plain text and git: `.bib` is a bibliography as text, `.qmd`
mixes prose, code, and citations in one readable file, and `.gitignore` tells git
which files to leave alone. We put all three to work — and package the result so
you never explain it twice.

### Gather what you need

Point the agent at a topic, a rough reading list, or a pile of half-remembered
titles, and have it:

1. resolve each work to a real paper — title, authors, year, DOI (inventing a
   citation is failure, not a shortcut);
2. download the open-access PDFs into a **gitignored** `references/pdf/` folder;
3. write a one- or two-line note on each into `references/notes.md`;
4. add a verified BibTeX entry to `references.bib`;
5. list what it *could not* get — with DOIs — in `references/to-fetch.md`, so you
   can grab those through the library yourself.

Then say: **"turn that workflow into a skill."** The agent writes the skill file;
you never learn its format. Next time, "gather refs on X" just works.

Skills aren't essential — you can do most of this course without them. They earn
their keep only for routines you *repeat* and want done identically.

> Memory is the AI remembering you. A skill is you writing it down — so it happens
> the same way every time, and you can hand it to a colleague.

### Clean what you have

Now the other direction. We start from a reference list with deliberate traps —
nonexistent papers, wrong DOIs, missing details, inconsistent formatting — and
ask the agent to identify every work, verify it against an independent source,
produce clean BibTeX, and record what it could not confirm. Then run it on a
bibliography from your own work.

> A polished bibliography is not evidence of a correct bibliography.

Full walkthrough: `handouts/references.md`.

## Afternoon — a literature sweep

Give the agent a folder of papers and a concrete comparison question. Begin with
one paper, settle on useful fields, and only then scale up.

Possible columns:

- research question;
- setting and sample;
- method or material;
- central finding;
- limitation noted by the authors;
- page supporting the summary.

Ask which papers genuinely disagree and which merely ask different questions.
Export the result as Markdown or CSV so it remains useful outside the session.

## The honesty checkpoint

Choose one row that matters. Open the original paper and verify it manually.
Check the page reference, wording, and strength of the claim.

If the row is wrong, that is useful course material. Diagnose why:

- Was the question vague?
- Was the PDF read incorrectly?
- Did the summary overstate cautious language?
- Did the agent infer something the authors never claimed?

Improve the workflow, not just the sentence.

## Open lab

Free work. Nobody is starting from nothing — you have spent a day and a half
making things, and the most useful hour of this course is often the one where you
take one of them further.

### Finish something you already have

Pick whichever is closest to real work you actually do:

- the **comparison table** from this afternoon — add the columns you wished it
  had, or turn it into a short synthesis you could put in a proposal;
- the **bibliography** — run the cleaning workflow over a reference list that
  matters to you, or make the gather-and-verify routine into a skill;
- the **cleaning script** from yesterday — change a decision, re-run it, and read
  the diff;
- the **handbook** — render it somewhere it can be read, or write the one-page
  student version and check the two agree;
- the **cleaned folder** — do it again on a real folder of your own.

### Or bring your own mess

If you can reach your own material — email, OneDrive, a USB stick — it is always
the better exercise:

- an untidy bibliography;
- a folder of PDFs;
- rough project notes;
- interview or meeting material you are allowed to process;
- a table that needs documenting;
- a draft that needs structural criticism.

### One thing worth stopping for

Before sharing material with any service, consider confidentiality, personal
data, contracts, and research ethics. `handouts/security.md` is the honest
version — including what actually leaves your machine, and what doesn't.

## Before you leave

Save one useful artifact and a short verification note. Tomorrow we use the
same workflow to build teaching material—and make it presentable.

