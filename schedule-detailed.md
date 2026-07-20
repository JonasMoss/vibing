# Detailed schedule — AI in the terminal

Block-by-block plan with instructor notes, materials, and fallbacks.
The one-page version is in `schedule.md`. Timings are aspirational;
the rule when behind is **cut content, never cut hands-on time**.

**Recurring cast:**

- *You-drive* = participants type on their own machines.
- *I-drive* = instructor demo on the projector.
- *Pairs* = terminal-comfortable person seated next to terminal-scared
  person (assign on day 1, keep all three days).

**Per-day cut list** (what to drop when — not if — we run late) is at the
end of each day.

---

## Before the course (logistics, not optional)

- **T−2 weeks:** confirm with BI IT that managed Windows 11 laptops can
  install Node/Claude Code/Codex without admin rights, and that the
  campus network doesn't block the APIs. This is the single biggest
  failure mode of the whole course.
- **T−1 week:** pre-course email: (1) get a paid Claude or GPT
  subscription, (2) install instructions with screenshots, PowerShell
  first, (3) a one-line "did it work?" verification command, (4) bring
  a real messy folder and a syllabus from one of your courses.
- **T−1 day:** print the booklet (or at least a one-page cheat sheet:
  the 10 terminal commands they'll ever need + how to start/quit the
  tool). Zip up `decrap-me/` example folder, put it on a short URL.
- **Room:** horseshoe = good for discussion, bad for screen-following.
  Check power outlets reach every seat; bring extension cords.

---

## Day 1 (Wed) — Your filesystem, your terminal, your new intern

**Goal of the day:** everyone leaves having watched an AI rummage
through *their* files and clean them up. Terminal fear → terminal
curiosity.

### 10:00–10:45 · Welcome + capability talk #1 (I-drive)

- Who I am, what the three days look like, why "in the terminal" at all.
- The pitch: chat AIs are consultants behind glass; filesystem AIs are
  interns at your desk. Same brain, hands attached.
- **Live demo, no slides for this part:** open Claude Code in a messy
  folder and clean it up by talking to it (speech-to-text, ideally) —
  the whole course in 5 minutes. Don't explain, just show.
- Expectation-setting: this course is typing, not listening.
- *Note:* stragglers will trickle in until 10:20 — front-load the
  things that are fine to miss.

### 10:45–12:00 · Setup triage & first contact (You-drive, chaos expected)

- Triage into three groups: (A) installed at home, works — give them
  the warm-up exercise sheet immediately so they're not bored;
  (B) installed but broken — pair with A-people and me;
  (C) ignored the email — install party in the back of the horseshoe.
- **Warm-up sheet** (for A, then everyone): start the tool in a folder,
  ask "what files are here?", ask it to make a file `hello.md` with a
  limerick about your department, open the file, delete it. Small,
  silly, zero stakes.
- Terminal survival kit on the projector while triaging: what a path
  is, `cd`, `ls`/`dir`, tab completion, up-arrow, Ctrl+C. **That's the
  whole list.** Everything else, they ask the AI itself.
- *Fallback:* anyone unfixable by 11:30 pairs up for the rest of the
  day and we fix them during lunch.

### 12:00–13:00 · Lunch

(Also: installation field hospital, 15 min, volunteers only.)

### 13:00–14:15 · Hero exercise: decrap a messy folder (You-drive)

- Everyone downloads `decrap-me.zip` — a premade horror show:
  `final_FINAL_v2 (3).docx`, `Notat fra møte.pdf`, duplicate images,
  an exam from 2019, lecture notes scattered over 4 subfolders.
- Task ladder (each step on the handout, go at your own pace):
  1. Ask the AI to describe what's in the folder.
  2. Ask for a cleanup *plan* — don't let it touch anything yet.
  3. Argue with the plan. Change it. (The lesson: you're the boss.)
  4. Let it execute. Watch it work.
  5. Ask it to write a `README.md` describing the new structure.
- Premade folder, not their own files: nobody risks real data on day 1,
  and everyone has the *same* mess so neighbors can compare.
- **Plenary moment (~14:00):** two volunteers show their before/after.
  Different prompts → different (both fine) results. That's the point.

### 14:15–14:30 · Break

### 14:30–15:25 · Plain text is king (I-drive 15 min, You-drive 40)

- Why AIs (and you, in 10 years) prefer Markdown/LaTeX/BibTeX over
  Word: diffable, versionable, greppable, no formatting landmines.
- Exercise: take a Word document of *theirs* (or a provided one),
  have the AI convert it to Markdown, then ask for restructuring
  tricks that are painful in Word: "merge these two sections",
  "make a table of all deadlines mentioned", "translate to Norwegian
  but keep the structure".

### 15:25–16:00 · Baby git + grievances (I-drive, discussion)

- Git in 15 minutes, three commands, no branches, no GitHub:
  `git init` (start tracking), `git commit` (save a checkpoint),
  `git log` (see history). Frame: an undo button the AI can also use.
  Have the AI do the git-ing — they just need to know to ask for it.
- **Grievances slot (20 min, scheduled on purpose):** air your AI
  worries — cheating, hallucination, deskilling, energy, copyright.
  Park what we'll answer on day 3, contain the rest. Skeptics who get
  airtime on day 1 don't hijack exercises on day 2.
- Homework (optional, sell it well): run the decrap exercise on a real
  folder of your own — e.g. your itslearning export.

**Day 1 cut list:** shorten plain-text exercise → 25 min; git demo can
shrink to 5 min ("ask the AI to set up git and commit, details Friday").
Never cut the hero exercise.

---

## Day 2 (Thu) — LLMs for research

**Goal of the day:** every participant does one real research-adjacent
task on their own material. Demo the heavy stuff, hands-on the
universal stuff.

### 10:00–10:30 · Recap + homework debrief (discussion)

- Two volunteers tell their real-folder decrap story (triumph or
  disaster, both teach).
- Fix lingering setup issues *now*; day 2 has no slack for it later.

### 10:30–12:00 · References that don't lie (I-drive 20 min, You-drive 70)

- The hook: hallucinated citations are the most famous LLM failure —
  and the most fixable, because references are *checkable*.
- Demo: take a reference list (provided: 15 entries, 3 subtly fake,
  2 with wrong DOIs), ask the AI to verify every entry against the
  web, produce a clean BibTeX file with a verification report.
- Exercise: they do the same on the provided list, then on a reference
  list from one of their own papers. Bring-your-own-bibliography.
- Sub-skills that ride along: what BibTeX is, asking the AI to fetch
  and check DOIs, "show me your evidence" prompting.

### 12:00–13:00 · Lunch

### 13:00–14:15 · Literature sweep (You-drive)

- Provided: folder of ~10 open-access PDFs on one accessible topic
  (e.g. AI in higher education — meta, relatable, every department
  has opinions on it).
- Task ladder: summarize one PDF → build a comparison table across
  all (research question, method, sample, finding) → ask "which papers
  disagree with each other and about what?" → export the table to
  Markdown/CSV for their own use.
- **Honesty checkpoint baked in:** pick one row of the table and
  verify it against the actual PDF. Find the inevitable wobble.
  This plants day 3's verification lesson.
- Those with their own PDF stash use it instead — better, it's *their*
  literature.

### 14:15–14:30 · Break

### 14:30–15:15 · Demo: data analysis in the terminal (I-drive, explicitly a demo)

- *Deliberately not hands-on:* stats alienates half the room, so they
  watch me drive instead of suffering themselves.
- Storyline demo on a simple, readable dataset (e.g. student grades or
  Norwegian public data): load a messy CSV → AI cleans it → asks AI to
  check assumptions → fit something simple → "explain this result to a
  reviewer" → generate the figure. Emphasis on the *conversation*, not
  the statistics.
- Punchline for the non-quants: the same loop works on interview
  transcripts, legal texts, marketing copy — code is just one dialect.

### 15:15–16:00 · Open lab: your own research mess (You-drive)

- Free work on their own material with a menu of suggestions: clean a
  dataset, check a bibliography, summarize PDFs, convert a paper draft
  to Markdown/LaTeX.
- Last 15 min plenary: one win and one fail per table section.

**Day 2 cut list:** stats demo → 20 min; open lab absorbs all other
overruns (it's elastic by design). Never cut the references block.

---

## Day 3 (Fri) — LLMs for teaching, and using them correctly

**Goal of the day:** everyone leaves with one real artifact for their
autumn course, and a working bullshit-detection routine.

### 10:00–10:30 · Recap + capability talk #2 (I-drive)

- Where this is going: agents that run longer, scheduled tasks,
  AGENTS.md/CLAUDE.md — "how I tell the AI about my project once
  instead of every time". Show this very course repo as the example
  (yes, the course is built the way the course teaches).

### 10:30–12:00 · Course factory (You-drive)

- They brought a syllabus (fallback: a provided one).
- Task ladder: generate 10 exam questions at stated difficulty levels →
  generate the *grading rubric* → generate three student answers
  (good/mediocre/subtly-wrong) and grade them with the rubric →
  critique loop: "which of these questions are bad, and why?"
- The subtly-wrong generated student answer doubles as an academic-
  integrity discussion: this is what AI-written student work looks
  like from the other side.

### 12:00–13:00 · Lunch

### 13:00–14:15 · Quarto slides + course page (You-drive, ladder by ambition)

- Rung 1 (everyone): AI turns a lecture's notes into a Quarto slide
  deck; render to HTML; tweak by conversation ("more slides, bigger
  font, one joke per section, remove the joke about deans").
- Rung 2 (ambitious): publish a one-page course site on GitHub Pages —
  this is where day 1's git quietly pays off, AI does the heavy lifting.
- Rung 3 (the bold): both, plus their day-2 literature table as a page.
- *Fallback:* GitHub account creation is a known time sink; rung 2 is
  demo-only if the wifi or account gods are angry.

### 14:15–14:30 · Break

### 14:30–15:15 · Using LLMs "correctly" (I-drive + discussion)

- Answer the parked day-1 grievances explicitly — close that loop.
- The verification habits, distilled from the three days: plan before
  execute; show-me-your-evidence; spot-check one row; git as undo;
  never paste what you haven't read.
- Live hallucination demo: make the model confidently produce a fake
  citation, then catch it with the day-2 checking workflow. Fear →
  procedure.

### 15:15–16:00 · Take-home artifact + wrap-up (You-drive)

- Finish and "ship" one artifact: cleaned course folder, verified
  bibliography, exam + rubric, slide deck, or course page. Committed
  to git, naturally.
- Wrap-up: the cheat sheet, the booklet, where to get help, what's
  worth automating first when they're back at their desk.
- Course evaluation (yes, you may ask the AI to draft your feedback,
  no, please write it yourself).

**Day 3 cut list:** capability talk #2 → 15 min; rung 2/3 of the
Quarto block → demo. Never cut the take-home artifact time.

---

## Materials to build (extracted TODO)

- [ ] Pre-course email with install instructions (PowerShell first)
- [ ] One-page terminal cheat sheet (print)
- [ ] `decrap-me.zip` — the premade horror folder
- [ ] Warm-up exercise sheet (day 1 morning)
- [ ] Reference list with 3 fakes + 2 wrong DOIs (day 2)
- [ ] Folder of ~10 open-access PDFs on AI in higher education (day 2)
- [ ] Readable demo dataset + demo script outline (day 2 stats demo)
- [ ] Fallback syllabus for the course factory (day 3)
- [ ] Quarto slide template (day 3)
- [ ] The booklet (assembles most of the above)
