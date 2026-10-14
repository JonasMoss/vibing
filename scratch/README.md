# scratch — the pool to copy from

Everything that is not a course. It is allowed to be messy and out of date.
**Nothing in `courses/` may depend on anything here:** when a course needs a
deck, handout or example, copy it into the course folder and edit the copy.

Most of this was built for the original three-day August 2026 course (postponed,
never taught) and for the September prep of the October department sessions.

## What is where

| Folder | What |
|---|---|
| `slides/` | All decks so far, in the **old site's Markdown format** (slides separated by `---`, custom click-reveal and SVG classes). Convert to Quarto revealjs when copying into a course. `site-styles.css` is the old look; `images/` holds the slide images. |
| `handouts/` | All participant handouts so far (Markdown). |
| `examples/` | Props participants work on, each with an instructor key (`README.md`). Generators live in `examples/scripts/`. |
| `august-course/` | The postponed three-day plan: invite PDF, schedules, day pages, the room script (`in-the-room.md`), grievance answers, the original July plan. |
| `research/` | Capability evidence and reviews behind the POWER deck; the chart script. |
| `links/` | Reading: annotated links (`README.md`), the Epoch data snapshot, the strategy reading pile, recent cross-field papers. |
| `systems-to-try.md` | Old three-line note. |

### Decks and the modules they belong to

| Deck | Handout | Example / instructor key | Built for |
|---|---|---|---|
| `power.md` | — | `research/` | capability talk, all courses |
| `how-it-works.md` | — | — | short "what is a model" explainer |
| `landscape.md` | — | — | which models, which plans |
| `opening.md` | — | — | August welcome |
| `what-it-knows.md` | — | `who-is-asking/` | context, profiles, `/clear` |
| `paper-critique.md` | `paper-critique.md` | `paper-critique/` | research: take a paper apart (piloted on NBER finance papers) |
| `leave-a-trail.md` | `leave-a-trail.md` | `leave-a-trail/` | research: make a folder rerunnable, first git |
| — | `install.md`, `terminal-cheatsheet.md`, `warmup.md` | — | setup and first contact |
| — | `plain-text.md` | `plain-text/` | why text beats Word |
| — | `references.md` | `references/` | BibTeX, DOIs, citation checks |
| — | — | `litsweep/` | literature sweep: 12 PDFs to an overview table |
| — | — | `simulation/` | "the interval nobody reports" stats demo |
| — | — | `decrap-me/`, `grades/` | decrap a messy exam export; draft a results email |
| — | `course-factory.md` | `syllabus/` | teaching: exams, exercises, rubrics from a syllabus |
| — | `slides-and-site.md`, `github.md` | `lecture-notes/` | teaching: Quarto slides and a course page |
| — | `project-structure.md`, `security.md`, `verification.md` | — | project files, what not to upload, checking output |

## Old paths inside these files

The files still refer to each other by their pre-October layout. Translate:

| Old path | Now |
|---|---|
| `content/slides/` | `scratch/slides/` |
| `content/day-*.md` | `scratch/august-course/days/` |
| `handouts/` | `scratch/handouts/` |
| `examples/` | `scratch/examples/` |
| `intro-notes/` | `scratch/research/` or `scratch/august-course/` |
| `links/`, `links.md` | `scratch/links/` |
| `dept-sessions/` | `courses/*/invite.md` |
| `scripts/make-*`, `scripts/fetch-litsweep-*` | `scratch/examples/scripts/` |
| `vibing.jonasmoss.com/...` | gone; the site was taken down (git tag `site-final`) |

Run generator scripts from the repo root, for example
`python3 scratch/examples/scripts/make-trail-example.py`. They write into
`scratch/examples/`.

## Not in git

Third-party PDFs (`examples/litsweep/pdfs/`, `examples/references/pdf/`,
`links/strategy-canon/pdfs/`, `links/recent-cross-field/*.pdf`), `litsweep.zip`
and the paper-critique pilot runs (`examples/paper-critique/pilot/`) stay on this
machine only; the fetch scripts and READMEs rebuild or explain them. Real
student data lives in `../private/`.
