# AGENTS.md — vibe-faculty course repo

This repo holds the materials for **"AI in the terminal: Claude Code and Codex
for research and teaching"**, a hands-on faculty course at BI Norwegian Business
School that runs several times, for different audiences. Anything an agent
produces here is course material for that audience, so read this file before
writing anything.

## The actual point of the course (read this before writing anything)

The syllabus says "LLM-friendly project setup, basic git, terminal comfort." That's
the *surface*. The real goals, and every piece of material serves them:

1. **Realization** — they leave knowing these tools do far more than they thought.
2. **Confidence** — they believe they can try it themselves, today, on their own work.

This is always the outlook. Practical consequences when writing:

- **Lead with capability, not caveats.** Show the impressive thing first. A caveat
  that arrives before the capability just teaches people to expect little.
- **Cut generic "here are the limitations" lists.** Boilerplate AI-caution is
  everywhere already, it is not what anyone came for, and it dampens the room. Keep
  a limitation only when it is *specific, non-obvious, and actionable* — a question
  they can ask, or a move they can make.
- **Verification is taught as nerve, not brakes.** You can be bold *because* you can
  check. Git means "let it try." Simulation means "test it before proving it." Every
  checking habit exists to let people move faster, not slower.
- **Don't undersell.** If the tool genuinely beats the traditional method, say so.
  Hedging to sound balanced is its own kind of inaccuracy.
- **The failure mode to avoid:** a room that leaves *impressed but not emboldened*.
  Awe without agency is worse than useless — they'll go home and change nothing.

## The courses

Each run of the course is its own folder under `courses/`, and its `README.md`
holds that run's hard facts: date, length, room, audience, focus, contacts,
status. **Read the README of the course you are working on before anything
else**: lengths range from one 4-hour afternoon to three full days, and the
departments asked for different things.

| Folder | When | Length |
|---|---|---|
| `courses/2026-10-finance/` | Fri 16 Oct 2026 | 1 day, 6 h |
| `courses/2026-10-strategy/` | Thu 22 + Fri 23 Oct 2026 | 2 × 4 h |
| `courses/2026-12-marketing/` | Thu 3 Dec 2026 | 4 h |
| `courses/2027-01-faculty/` | January 2027 | probably 3 days |

Common to every run:

- **Tools:** Claude Code or OpenAI Codex. Participants bring a **paid** Claude
  or ChatGPT subscription. BI's Gemini subscription is explicitly out (no
  filesystem access).
- **Language:** English. **Instructor:** Jonas Moss (jonas.moss@bi.no),
  Department of Data Science and Analytics.
- **Prerequisites:** none. No participant preparation is assumed beyond the
  subscription.
- In person only. Hybrid was considered and rejected: the course is hands-on.

The original three-day August 2026 course was postponed and never taught; its
plan and invite live in `scratch/august-course/`.

## Who the participants are

- **Core audience: marketing, strategy, and finance faculty.** Demos and
  examples should land for these three first. Others (law, leadership,
  economics, communication) may attend too — this is not a data-science crowd.
- **Strong opinions, weak terminal skills.** Assume zero shell knowledge.
  Many will have never opened a terminal. Do not assume git, package
  managers, or even "what a path is".
- **Mostly Windows 11 laptops**, often IT-managed (possible admin-rights
  issues). A minority on macOS. Plan instructions Windows-first.

## Pedagogy stance

- **Mostly hands-on practice, a little capability talk.** Short demos and
  "what can these things actually do" segments are wanted, but the bulk of
  every day is participants typing into their own machines.
- Participants work on **their own real material** when possible, with
  premade example problems as fallback.
- **Speech-to-text** is part of the workflow we teach (lowers the typing
  barrier).
- Course goals (from the invite): LLM-friendly project setup, very basic
  git, terminal comfort, using LLMs "correctly". Content pillars: LLMs on
  your filesystem / for research / for education.

## Example-problem policy (important)

- **Simple, domain-neutral, immediately relatable wins.** The flagship style
  is "decrap your itslearning export": take a messy real folder and have the
  AI clean, rename, and organize it.
- **Avoid** stats-heavy or C++/programming-heavy examples. Jonas has complex
  examples in those domains but they alienate this audience — the domain
  knowledge required drowns the lesson about the tool.
- Good example domains: syllabi, exams, reference lists / BibTeX, messy
  download folders, Word-to-Markdown conversion, course web pages, Quarto
  slides, email/admin drudgery.

## How this repo is organised

```
courses/<yyyy-mm>-<name>/   one self-contained folder per run of the course
scratch/                    everything else: the pool to copy from, notes, research
private/                    gitignored: real student data, never published
```

**The rules, in order of importance:**

1. **A course folder is self-contained.** Nothing in it links to, includes or
   depends on anything outside it. Need a deck, handout or example from
   elsewhere? *Copy* it in. Overlap between courses is fine and expected.
2. **A held course is frozen.** Once a course has been taught, its README says
   `Status: held <date>, frozen` and the commit is tagged `held/<folder-name>`.
   After that, change **nothing** in it except `debrief.md`. Fixes and
   improvements go forward into the next course, never back.
3. **Copy forward.** A new course starts as a copy of the most recent course
   (plus whatever it needs from `scratch/`), then gets edited for its audience.
4. **Build one course at a time**, in date order. Finance first.

**Inside a course folder:**

```
README.md            facts, contacts, status, files, how to render
invite.md            the invitation as sent (invite.docx is the Word copy)
_quarto.yml          this course's own render settings
decks/               one revealjs deck per module (menu.qmd links them all),
                     shared settings in decks/_metadata.yml, look in slides.scss
handout.qmd          what participants get: every module, every prompt
teacher-notes.qmd    checklist, run sheet, one card per module
props/               zips and folders participants work on
debrief.md           written after the course: what worked, what to change
```

- **Many small decks, not one big one.** One deck per module keeps parallel work
  (several agents, or you and an agent) from colliding, and lets the room pick
  modules in any order. `decks/menu.html` is the hub.
- Sources are **Quarto (`.qmd`)**; every one renders to a **single
  self-contained `.html`** (`embed-resources: true`) next to it. Render with
  `quarto render courses/<folder>`. **Commit the rendered HTML**: it is what was
  shown, and what gets emailed to participants afterwards.
- **The web page is plain static HTML**, served by GitHub Pages from `main` at
  vibing.jonasmoss.com, with no build step: the root `index.html` lists the
  courses, and each course has an `index.html` (course files, handout, every deck
  in a pane). Participants download `course-files.zip` (handout plus props) from a
  short link on the menu deck. The old course site is at the local tag
  `site-final`; **never push that tag** (it contains a prop built from real
  student data).
- `scratch/` is allowed to be messy and out of date. Nothing in a course may
  depend on it. Its decks are in the old site's Markdown format and need
  converting to Quarto when copied into a course. See `scratch/README.md`.

## Conventions for this repo

- Plain text everywhere: Markdown for prose, Quarto for slides and handouts,
  BibTeX for references. No Word documents as source material (Word copies of
  invites are records, not sources).
- Course materials are written in English, friendly and informal in tone,
  but not sloppy: participants are professors.
- Handouts/instructions must give **Windows (PowerShell) commands first**,
  macOS/Linux variants second.
- `scratch/links/README.md` collects reference reading; add sources there, one
  per line, ideally with a one-line annotation.
- Undecided ideas and open questions go in `parking-lot.md`. Park them there
  instead of deciding prematurely; promote into a course or delete once
  resolved.
- **This repo is public.** Real student data, unverified claims about named
  papers and third-party PDFs stay out of git (`private/`, and the ignore rules
  in `.gitignore`).
