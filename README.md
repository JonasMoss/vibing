# AI in the terminal — course materials

Materials for **AI in the terminal: Claude Code and Codex for research and
teaching**, a hands-on course for BI faculty taught by Jonas Moss. It runs
several times for different departments, and each run is built and kept on
its own.

## The courses

| Course | When | Length | Status |
|---|---|---|---|
| [Finance](courses/2026-10-finance/) | Fri 16 Oct 2026, 09–16 | 1 day | held, frozen |
| [Strategy & Entrepreneurship](courses/2026-10-strategy/) | Thu 22 Oct 12–16 + Fri 23 Oct 09–13 | 2 × 4 h | in preparation |
| [Marketing](courses/2026-12-marketing/) | Thu 3 Dec 2026, 12–16 | 4 h | not started |
| [All faculty, 2027](courses/2027-01-faculty/) | January 2027, dates TBD | probably 3 days | not started |

## Layout

```
courses/   one self-contained folder per course; frozen once it has been taught
scratch/   the pool to copy from (old decks, handouts, examples), research, reading
private/   gitignored: real student data
```

Each course folder holds Quarto sources (a `decks/` folder with one deck per
module, `handout.qmd`, `teacher-notes.qmd`), the single-file HTML they render
to, and a `props/` folder with what participants work on. Open
`decks/menu.html` to teach. Nothing in a course points outside its
folder, so building the next course can never change one already taught.

The full rules are in [AGENTS.md](AGENTS.md); the why of the course is in
[vision.md](vision.md); open questions are in [parking-lot.md](parking-lot.md).

## Render a course

Windows PowerShell or macOS/Linux, from the repo root:

```
quarto render courses/2026-10-finance
```

Every `.qmd` becomes one self-contained `.html` next to it, which you can open
offline, project, or email.

## After teaching a course

1. Render it one last time and commit.
2. Set `Status: held <date>, frozen` in its README.
3. Tag it: `git tag held/2026-10-finance`.
4. Write `debrief.md` in the folder: what worked, what to change. From then on
   that is the only file in the folder that changes.

## The web page

vibing.jonasmoss.com is a plain static page, served by GitHub Pages straight from
`main` (no build step): `index.html` here lists the courses, and each course folder
has its own `index.html` with the course files, the handout and every deck in a
pane. To add a course, copy the previous course's `index.html` and add a card to
the root `index.html`.

The old, bigger course site was taken down in October 2026; its last state is the
local git tag `site-final`. Never push that tag: see `AGENTS.md`.
