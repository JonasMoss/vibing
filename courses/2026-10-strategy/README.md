# AI in the terminal — Department of Strategy and Entrepreneurship

**Status: held 22 and 23 October 2026, frozen.** Tagged `held/2026-10-strategy`.
Change nothing here except `debrief.md`; fixes go forward into the next course.

Copied forward from Finance on 20 October, reworked 20–21 October; see the
checklist below.

## Facts

- **When:** Thursday 22 October 2026, 12:00–16:00, and Friday 23 October
  2026, 09:00–13:00. Two half-days, 8 hours. The second day builds on the
  first.
- **Room:** not booked yet as of 5 October. A2 was nearly full; Line Nilsen
  said C2 had space.
- **Who:** Department of Strategy and Entrepreneurship. By 7 October: 17 yes,
  8 tentative, 5 not answered. Not everyone has accepted both days; Siri's line
  is that day one is what matters.
- **Focus:** research is the main focus, **qualitative and quantitative**
  (Birgitte asked explicitly that both groups are served). Teaching is only a
  **short, optional block at the end of day two**: several of them have already
  taken BI's AI-for-teaching course, and Birgitte did not want overlap.
- **Contacts:** Line Nilsen (head of administration, Strategy), Birgitte
  Grøgaard (head of department), Siri Johnsen (DS administration).

The invitation as sent is `invite.md` (`invite.docx` is the Word copy).

## Changes from Finance (tentative plan)

From the Finance debrief (`courses/2026-10-finance/debrief.md`). More notes may
follow. TAs: Ludvik Slipersæter and Leonardo.

- [x] **(a) A mandatory git deck right after setup** (`decks/git.qmd`, "Save
  points"): 25 short slides and four exercises. What git is, where it comes from
  (timeline, two charts), why it's mainly for the agent, OneDrive vs git, a
  `.gitignore` exercise on a new prop (`props/founders-study.zip`, built by
  `scratch/examples/founders-study/make.py`), the cloud, five words, "unsure?
  ask", GitHub and GitHub Pages. Handout section 2; later handout sections and
  deck references renumbered. Facts checked, exercise tested 20 October.
- [x] **(c) An access deck right after git** (`decks/access.qmd`, "What it can
  touch"): 19 slides, three exercises. How far each tool reaches, what leaves the
  laptop, the dial, auto mode's second model, a matrix of what we tested, my
  stance, three ways to say no (with the deny-rule gap we found), the training
  switches, personal data. Handout section 3; later sections renumbered again.
  Behaviour tested and facts checked 20 October.
- [x] **(b) The agent opening the PDFs in the cleanup:** the exam export can be
  renamed from the names alone, so the cleanup prompts now say "names only; don't
  open the submissions", and a new last slide ("You decide what it reads") makes it
  the point. "Done early?": rename the fake papers in `founders-study/literature/`,
  where reading is needed, without opening `interviews/`.
- [x] **Course files:** `course-files.zip` holds the practice folders unpacked, not
  zips inside a zip. The handout's download links point at this folder, not
  Finance's.
- [x] **(d) Level differences and derailments** (21 October): a "Derailments"
  page in the teacher notes. One-laptop questions go to a TA, a parking-lot
  flipchart answered before each break, "Done early?" on the exercises, FAQ slides
  as quick answers.
- [x] **(e) Nobody sits idle** (21 October): sticky notes (yellow fine, pink stuck),
  Ludvik's laptop check at 13:05, a fallback after 15 minutes stuck, install
  drop-ins Thursday 11:00 and Friday 08:30.
- [x] **A TA brief** for Ludvik and Leonardo in the teacher notes ("For Ludvik and
  Leonardo"): Ludvik owns installs, Leonardo owns the room's questions.
- [x] **Handout:** `codex --full-auto` no longer exists (Codex 0.162); the
  "Working safely" tip now points to section 3.
- [x] **Strategy examples** (21 October): "Your field, as I imagine it" opens
  `knows` (three cards, then "tell me what I got wrong"); the schools question is
  planned vs emergent; Denrell replaces Campbell Harvey; a luck-test card replaces
  the Fama–French replication; a strategy early task in setup; checks for
  interview papers in `paper` and `more`. Schools question and luck test tested
  with Codex.
- [x] **Two half-days** (21 October): run sheets for Thursday and Friday; the menu,
  the course page and the handout split by day.
- [x] **Interviews** (new deck `interviews`, handout section 7): eight fictional,
  pseudonymised founder interviews (`props/pivot-interviews.zip`, built from
  `scratch/examples/pivot-interviews/`), a codebook, coding, themes, every quote
  checked by a script. Planted: three pseudonymisation slips, a contradiction, a
  planned-or-emergent story, a case that doesn't fit.
- [x] **Teaching** (new deck `teaching`, handout section 14): optional, end of
  Friday. The exam factory, a course page, an animation; a fictional syllabus as
  fallback (`props/ORG3402-organisational-behaviour.md`).
- [x] **Friday without a research menu** (21 October; Finance debrief, note 6):
  References is mandatory (30 minutes), and the room chooses among *Words you've
  heard* instead (new deck `words`, handout section 9): skills, connectors,
  subagents, the project file, plan mode, context and /compact, worktrees, GitHub,
  agents in the cloud. Referee panel, Leave a trail, and Notes and structure move
  to "Any time". The menu's title-slide "Invalid Date" is fixed.
- [x] **Room:** Jonas handles it with Line (21 October). Background: Line wrote on
  5 October that A2 was nearly full and C2 had space.
- [x] **Before Thursday, Jonas's part** (21 October): send the TA page to Ludvik and
  Leonardo (Ludvik: GitHub account and `gh` for the pull-request demo), test on a
  BI-managed laptop, pre-run the backup demos.

## Open questions from email

- **Espen Andersen** (teaching both days, so can't attend) asked whether
  slides or documentation will be available afterwards. Line passed the
  question to Jonas. The rendered single-file HTML answers it.

## Starting material

- Copy forward from Finance.
- Qualitative research: `scratch/examples/pivot-interviews/` (built 21 October).
- `scratch/links/strategy-canon/` is a strategic-management reading pile,
  instructor background.
- For the teaching block: `scratch/handouts/course-factory.md` and
  `scratch/examples/syllabus/`.
