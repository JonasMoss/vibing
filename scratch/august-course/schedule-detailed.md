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

> 🎯 **The page you actually hold while standing up: `intro-notes/in-the-room.md`.**
> Print it. It has the Wednesday opening script, the four pre-decided branches for
> when the room splits, and a per-block table of *floor rung · first cut · the
> 20-minutes-behind move*. This file is the reasoning; that one is the interface.
>
> **Why it exists:** the room is extremely heterogeneous and nobody prepared, so
> you *will* be adapting live. Improvisation only feels bad when you have to invent
> under pressure — pre-deciding the branches turns it into selection.

## Time budget — where the slack actually is

Each day has **300 teaching minutes** (10:00–16:00 minus lunch). Counted block by
block, including the 15-minute break:

| | Talk | Hands-on | Discussion | Total |
|---|---|---|---|---|
| **Day 1** | 107 | 158 | 35 | **315 — over by 15** |
| **Day 2** | 65 | 205 | 45 | 300 — fits |
| **Day 3** | 60 | 200 | 55 | 300 — fits |

**Day 1 is the only over-committed day, and it is worse than 15 minutes looks.**
The 11:05 install block is now ~20 people installing from **zero** on IT-managed Windows
(no pre-course email), which realistically runs 60+, not 45. Plan for Day 1 to be
**~30 minutes over** and decide *in advance* what pays for it — the cut list at the
end of Day 1 is ordered for exactly that. Do not improvise it at 15:20.

Days 2 and 3 fit on paper but have two optimistic sub-blocks worth watching:
Day 2's 10:00 recap, and Day 3's 10-minute GitHub-account beat (never 10 minutes
for people who have never made an account — the neighbour-helps-neighbour move
from Day 1 is what saves it).

**The discussion slots are not padding and they are not the slack.** Day 1's
grievances (20 min) is load-bearing for Days 2 and 3 — it's the debt Friday
afternoon pays off. Day 2's plenaries and Day 3's answer-the-grievances block are
where the room decides whether it believes any of this. When behind: **cut content,
never cut hands-on time, and never cut the discussion.** Talk is what gives.

---

## Before the course (logistics, not optional)

> **⚠️ DECIDED: there is no pre-course email and no participant preparation.**
> Participants arrive with a paid subscription and nothing else. They are *not*
> asked to install anything, bring a messy folder, or bring a syllabus. The messy
> folder is our prop, not their homework, and every professor can describe their
> own course from memory in five lines — no prep required for that either.
>
> **Consequences, all of them already applied below:** everyone installs in the
> room on Day 1; there is no "group A who installed at home"; every provided prop
> is the *primary* path, not a fallback. Don't re-introduce prep assumptions.

- **~~T−2 weeks~~ → do it NOW, T−3 days.** Confirm that managed Windows 11 laptops
  can install Claude Code / Codex without admin rights and that the campus network
  doesn't block the APIs. This was always the single biggest failure mode; with no
  pre-course install it now lands **live, in the room, on ~20 machines at once**,
  so it is the one item genuinely worth chasing before Wednesday.
  - **The version that fits in the time you have:** borrow *one* IT-managed BI
    laptop (a colleague's, on campus, on campus wifi) and run the handout end to
    end — install, launch, log in, one prompt. One real managed machine tells you
    more than any email from IT, and it tells you on Monday instead of never.
  - **What you're actually looking for**, in order of how badly it hurts:
    (1) does the PowerShell script get blocked by security software;
    (2) does login open a browser and come back cleanly;
    (3) is `claude` / `codex` on the PATH in a fresh shell.
  - **Mitigations already in the handout** if it fails: `claude doctor`,
    `winget install Anthropic.ClaudeCode`, and pairing two-to-a-laptop.
  - ✅ **Install commands re-verified 9 Aug** — both PowerShell URLs live, npm
    engine requirements current. The *commands* are not the risk; the *laptops* are.
- **T−1 day:** print the **one-page cheat sheet** (`handouts/terminal-cheatsheet.md`)
  — the 10 terminal commands they'll ever need + how to start/quit the tool. Print
  `handouts/warmup.md` too; laptops won't all be working when it's needed.
  (**The booklet is dropped** — it assembled material that isn't finished, and the
  cheat sheet is the only page that genuinely needs to be on paper.)
- **The decrap download is `vibing.jonasmoss.com/decrap-me.zip`** — short enough to
  read aloud, deploys with the site on push, no shortener to fail mid-exercise.
  Rebuild it with `node scratch/examples/scripts/make-decrap-example.mjs` if the folder changes.
- **Room:** horseshoe = good for discussion, bad for screen-following.
  Check power outlets reach every seat; bring extension cords.

---

## Day 1 (Wed) — Your filesystem, your terminal, your new intern

**Goal of the day:** everyone leaves having watched an AI rummage
through *their* files and clean them up. Terminal fear → terminal
curiosity.

### 10:00–11:05 · Welcome + capability talk #1 (I-drive)

> **Re-timed — the decks outgrew the old 45-min slot.** POWER alone is ~50 min,
> plus how-it-works ~5. Honest budget: *triage + welcome 10 · POWER 50 ·
> how-it-works 5* = **65 min**, so this block runs to **11:05**, setup gets
> 11:05–11:35, and the hands-on context block gets 11:35–12:00.
> **`landscape` moved to Day 3** (capability talk #2) — by then they've
> actually used a model, so "they're not interchangeable" lands on experience
> instead of theory. Pull it back to Day 1 only if the morning is somehow ahead.
> The thing this protects is the 15:25 **grievances** slot — don't let the morning
> eat it.

- **Recommended open (banked — then feel it out live):**
  1. *~10 min · start the downloads, then close the lids.* **Nobody has installed
     anything** (no pre-course email — see the decision box above), and 20 laptops
     hitting the network at 11:15 is the bottleneck that eats the afternoon. So:
     hand out the printed install sheet (`handouts/install.md`), get everyone to
     *start* the download, then **lids stay open, eyes forward, don't touch it.**
     The download runs through the deck.
     - ⚠️ *Judgement call, decide in the room:* this trades ~10 minutes of deck
       time and a bit of attention discipline for removing the worst setup
       bottleneck. If the room looks like it will fiddle rather than watch, skip
       it and take the hit at 11:15 instead — **the deck matters more.** Don't let
       an install sheet cost you the awe.
     - No green/red triage any more — there is nothing yet to triage.
  2. *POWER deck, lids open but ignored* (~40 min) — undivided attention. The awe
     **is** the motivation, so don't split it with setup struggle.
  3. *how-it-works* immediately after — the deck's last slide hands straight into it.
     Four slides, ~5 min: the three stages (diagram with click steps), why that is
     enough to prove theorems, and Good vs Fast models ("use Good by default"; say
     the effort/cost point out loud, and that the model names change monthly). The
     hands-on half (context, profiles) is its own deck at 11:35.
  4. *setup + first contact* for the rest of the morning — demo as the launch,
     pairs (A helps the reds), full runway. Demo goes **after** how-it-works: model
     first, then the model made visible.
- Who I am, what the three days look like, why "in the terminal" at all.
- The pitch: chat AIs are consultants behind glass; filesystem AIs are
  interns at your desk. Same brain, hands attached.
- **Live demo, no slides for this part:** open Claude Code in a messy
  folder and clean it up by talking to it (speech-to-text, ideally) —
  the whole course in 5 minutes. Don't explain, just show.
- Expectation-setting: this course is typing, not listening.
- **Spine of this block is the POWER deck** (`content/slides/power.md`,
  `/slides/power`) — 27 slides (Exhibits A–D + security). On its own it's a full
  ~50 min, so keep
  welcome + demo tight or let this slot breathe into the next one.
- **The "what I don't know" beat — resist opening the floor (the monologue trap).**
  After that slide: (a) show of hands — "whose field has a cheap, honest
  check?" — narrate the split; (b) 30-sec neighbour turn — "what's your verifier,
  or is there none?"; (c) park it — "back to this Thursday." Take a plenary answer
  only if the room is contained: one sentence, hard stop at two. The pair-share is
  the pressure valve — the monologuer gets a listener without costing the room.
- **The "human still points and extends" line (Tao/Erdős slide) — don't let it turn
  into a group hug.** The old "human *with* machine, not *versus*" coda was softened
  to just "*for now*, the human still points—and extends." Someone will raise a hand
  to deliver the comforting version. Honest counter, if you want it: today's human
  edge on *ideation* looks like a **cost / harness limit, not a capability ceiling** —
  nobody's yet paying to let the model run its own research loop. And the ideation
  studies cut both ways and are **on a timer**: Si et al. (ICLR 2025) found LLM ideas
  judged *more novel* than experts'; the same team's follow-up (Jun 2025) found that
  edge *vanished once the ideas were built*. Present it as a **snapshot, not a
  fundamental limit** — the "there's the human moat" reading is the cope. 60 seconds;
  voice a suspicion, don't open a debate.
- *Note:* stragglers will trickle in until 10:20 — front-load the
  things that are fine to miss.

### 11:05–11:35 · Setup triage & first contact (You-drive, chaos expected)

> **This is now a full install party, not a triage.** Nobody installed at home,
> so the old A/B/C split is gone — everyone starts from zero at the same moment.
> The scarce resource is *you*, and 30 minutes across ~20 machines is about 90
> seconds each. The mechanic below is what makes that survivable.

- **Deputise the first finishers — this is the whole plan.** The moment someone's
  tool starts, hand them the warm-up sheet *and* a job: **get your neighbour
  running.** Five deputies by 11:20 turns one instructor into six. Say it out loud
  at the start so the fast people expect it and it reads as status, not chores.
- **Warm-up sheet** (`handouts/warmup.md`) — the reward for finishing, and the
  thing that stops the fast people getting bored and loud: start the tool in a
  folder, ask "what files are here?", ask it to make `hello.md` with a limerick
  about your department, open it, delete it. Small, silly, zero stakes.
- Terminal survival kit on the projector on a loop while you work the room: what
  a path is, `cd`, `ls`/`dir`, tab completion, up-arrow, Ctrl+C. **That's the
  whole list.** Everything else, they ask the AI itself.
- **Hard rule: nobody debugs alone and nobody debugs silently.** Hand up = a
  deputy comes. You take only what the deputies bounce.
- *Fallback:* anyone still broken at 11:35 pairs for the afternoon and gets fixed
  at lunch (field hospital). **The hero exercise works fine two-to-a-laptop** —
  arguably better, since they have to talk about the prompt. Nobody sits out.

### 11:35–12:00 · What it knows about you (I-drive ~12 · You-drive ~13)

Deck `content/slides/what-it-knows.md` (`/slides/what-it-knows`). Demo material and
test results: `examples/who-is-asking/`.

- **Why this block exists:** the complaint "the AI gives me bad answers" usually
  comes from people who never told it who they are. It hits hardest in fields split
  into schools (qualitative vs quantitative, frequentist vs Bayesian), because the
  default answer belongs to one school.
- **Order:** context diagram (two click steps: `/clear`, then "write it down") →
  **Exercise 1** (`/clear`, 2 min) → "Who is asking?" diagram (click: the curve
  narrows onto you) → coffee table (click: highlight) → stereotyping → **live demo**
  → "Two files" (profile vs project file) → **Exercise 2** (~8 min) →
  homework slide. The last slide is a backup for the demo.
- **Profile vs project file — keep the words straight.** Day 1 is about *you*: the
  personal profile in the home folder, read in every project. The project file
  (`AGENTS.md` / `CLAUDE.md` in a folder) belongs to Day 3. Never say "instructions
  file"; the chat-app comparison (custom instructions vs Project instructions)
  makes the split land in one sentence.
- **Live demo, on Claude Code:** the A/B question with no profile, then add
  "My intellectual idol is Jim Berger." to the demo folder's `CLAUDE.md` (say that
  it normally belongs in your profile; a folder file keeps it off your own machine's
  profile), `/clear`, ask again. In
  testing, the one line was enough for Claude to bring in Sellke, Bayarri and Berger
  (2001) and conclude "at least a 45% chance there's no real difference". **Codex
  ignored the one-liner**, so demo on Claude, and say it: "if nothing changes,
  write more."
- **The stereotyping slide will draw objections.** The answer is on the slide: it
  stereotypes you either way, and the only choice is whether you pick the type.
- **Exercise 2 wording is tested:** "save these as my personal profile, the file you
  read in every project" made Claude go for `~/.claude/CLAUDE.md` (it asks permission
  first, because the file is outside the folder: tell people to approve it) and
  Codex write `~/.codex/AGENTS.md` without asking. Both checked for an existing file
  before writing, and Claude said it would add to one rather than overwrite it.
- **If setup overran (likely):** keep the talk (~10 min: context, who is asking,
  coffee, demo) and move Exercise 2 into the homework, where it pairs naturally with
  the personal profile. Don't take the time from the 13:00 hero exercise.

### 12:00–13:00 · Lunch

(Also: installation field hospital, 15 min, volunteers only.)

### 13:00–14:15 · Hero exercise: decrap a messy folder (You-drive)

- **First ~8 minutes: let the fear arrive, then answer it (git, beat 1 of 2).**
  Don't teach git preemptively — nobody feels the need yet, and it lands as
  housekeeping. Stage it in three moves:
  1. **Brief the task, don't start it** (~2 min). "This folder. Your job: let the
     agent reorganise the whole thing. Ready?"
  2. **Let the room say it** (~1 min). Someone will. If nobody does, prompt:
     *"Before you hit enter — does anything about this make you nervous?"* This room
     will bite. You want the words **"what if it ruins something?"** spoken out loud,
     by a participant, not by you.
  3. **Answer with git** (~5 min). *"Commit this before we start."* One instruction,
     no theory, no `git log`, no branches — just the snapshot. Then the line that
     unlocks the whole afternoon: **"now it can't do anything you can't undo."**
  - *Why the order matters:* the answer has to arrive when the question is live. Ask
    → answer beats answer → ask, and the fear is genuinely theirs — this is the
    single biggest brake on this audience. The full git block still lands at 15:25;
    this is just the reflex, delivered at the moment of need.
  - *Bonus:* it doubles as an early pressure valve for the skeptics — a real worry,
    voiced and satisfyingly answered, buys you goodwill for the rest of the day.
  - *Be honest about the order:* git restores only what was saved **before** things
    went wrong. Save point, then courage. A snapshot taken after the mess is a
    snapshot of the mess.
  - Belt *and* braces: they're on a provided copy anyway, so nobody's real work is at
    risk today. Say that too — but let them feel the reflex on a safe folder, so it's
    automatic when they run this on their own stuff at home.
  - *Don't stage a real disaster to make the point.* Tempting, but with 20
    non-technical people it burns time and sours the room. Anticipatory fear is
    enough, and it's genuine.
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

### 14:30–15:25 · Leave a trail (I-drive 17 min, You-drive 38)

*Retitled from "plain text is king" — the format was never the point. The spine is
**write it down so it can be checked**, which covers prose* and *data and sets up
git. Handout `handouts/plain-text.md`; props `examples/plain-text/`.*

- **~5 min · the argument.** Two kinds of writing-down, one idea: prose in Word hides
  its changes, text shows them; clicking in Excel leaves no record, a script *is* the
  record. Table it on the projector — it lands in ten seconds.
- **~12 min · live demo, two halves.**
  (a) *Never open Word:* talk a small handout into existence (speech-to-text —
  dogfood the workflow), then hit it with the three superpowers — **query** it
  ("every deadline in a table"), **restructure** it, **render** it as HTML *and* PDF.
  (b) *The 3-minute data beat:* messy CSV → "write me a script that cleans this" →
  run it → **"that file is your methods section."** Punchline: *you never learned to
  code, and your cleaning is now better documented than most published papers.*
- **~38 min · two tracks** (everyone starts A; B is opt-in, not a stream):
  - **A — the document.** `course-handbook.docx` → text → interrogate → restructure
    → render twice. Five traps planted (weights sum to 90%, two sections that
    disagree 40% vs 45%, contradictory feedback promise, six deadlines in six date
    formats, inconsistent names). Instructor key in `examples/plain-text/README.md`.
  - **B — the data.** `survey-responses.csv` → ask for a *script*, not a cleaned
    file → change one decision → re-run.
- **Light evangelism, cost-framed — don't moralise.** Not "you should share your
  work" but *"you can't reconstruct your own work."* Not "open science is good" but
  *"a reviewer asks what you did, and you answer in 30 seconds instead of a
  weekend."* The tools made this hard; that excuse just expired. A room of professors
  will argue with virtue and nod at self-interest.
- **Two stories that do the persuading for you** (both verified, links in the
  handout). Use one, not both:
  - **The Norwegian one.** Norway's sovereign wealth fund lost roughly **$92 million**
    to one wrongly entered date in a spreadsheet, 1 December for 1 November (disclosed
    2024; EuSpRIG's incident archive). Hard to
    dismiss as an academic's hobby-horse in *this* building.
  - **The one that gets a laugh.** Excel silently turns gene names into dates —
    found in ~20% of papers with supplementary gene lists (2016), ~31% by 2021. The
    ending: the gene-naming committee **renamed human genes**, because that was
    easier than fixing Excel. Nobody mistyped anything; the *tool* did it, on open.
  - *Available but handle with care:* Reinhart–Rogoff. The famous "Excel error that
    caused austerity" was **one of three** problems — tell it that way, or you model
    the exact sloppiness this block is against.
- **Keep the honest caveat or it turns into cheerleading:** reproducible ≠ correct.
  Best line in the block, and the answer to "but the AI's script might have bugs":
  ***a wrong script you can read beats a right click you can't remember.***
- **End on the promise, don't deliver it:** "there's a third thing — you can see
  exactly what changed. That's next." The git block opens by cashing it.
- ✅ **The pandoc worry is smaller than it looks — and the workaround is a better
  demo than the tool.** Word→Markdown *usually* wants **pandoc**, which nobody has
  installed (no prep) and which may not install on a managed laptop. But a `.docx`
  is just a **zip full of XML**, and an agent that can't get pandoc will simply
  unzip it and parse it — no install, no admin rights.
  - **Verified on the actual prop (9 Aug):** unzipping `course-handbook.docx` and
    stripping tags recovers all **23 paragraphs**, headings and body text intact.
    On Windows the agent has a native route with nothing to install at all
    (`Expand-Archive` + PowerShell's built-in XML parsing).
  - **So don't pre-empt it.** Let them ask for the conversion and let the agent hit
    the wall — *"pandoc isn't installed, so I'll open it directly"* is the block's
    best unscripted moment, and it makes the same point as Friday's Quarto rung:
    **the agent solves its own tooling problems.** Frame it as capability, not
    apology.
  - **Belt and braces:** `examples/plain-text/course-handbook.md` still ships, so
    anyone stuck starts from the `.md` and loses nothing. Reach for it after ~3
    minutes of watching, not before.

### 15:25–16:00 · Baby git + grievances (I-drive, discussion)

*Git, beat 2 of 2. They met it at 13:00 as **courage** (the save point that made the
decrap safe); now they meet it as **clarity** (seeing exactly what changed). Same
tool, two reasons, spaced so neither becomes a lecture. Lead by calling back: "you
already used this — here's what else it does."*

> **⚠️ Run this block in the order below — git is deliberately split around the
> grievances.** Day 1 is over-committed by ~15 min on paper and the install block
> will overrun, so *something* here gets squeezed. The old order (git 15 →
> grievances 20) makes **grievances** the thing that dies, which is precisely
> backwards: git already landed its essential beat at 13:00, and the grievances
> slot is load-bearing for Days 2 and 3. Split git so the **elastic part is last.**

**1. Cash the promise (~5 min, non-negotiable).** They were told "you can see
exactly what changed" — so *show it*, on the handbook or cleaning script they just
made: change one line, `git diff`, there it is. Git stops being an abstract lecture
about version control and becomes the payoff to something they already care about.
This is the whole reason the block exists; five minutes buys it.

**2. Grievances (20 min, scheduled on purpose, protected on purpose).** Air the AI
worries — cheating, hallucination, deskilling, energy, copyright. **Write them down
where the room can see you do it**; you are going to read them back on Friday
afternoon, and the visible list is what makes that promise credible. Park what
we'll answer on Day 3, contain the rest. Prepared answers, all sourced:
`intro-notes/grievance-answers.md`. Skeptics who get airtime on day 1 don't hijack
exercises on day 2.

**3. The rest of git (~10 min, and this is the elastic part — cut it freely).**
Three commands, no branches, no GitHub: `git init` (start tracking), `git commit`
(save a checkpoint), `git log` (see history). Frame: an undo button the AI can also
use. **Have the AI do the git-ing** — they only need to know to ask. If you're out
of time, one sentence covers it: *"ask the AI to set up git and commit; we'll use
it Friday."* Nothing is lost — they already committed once, at 13:00, for real.

- *GitHub accounts are **not** attempted here* — that time sink moved to Day 3
  morning, right before the course page that actually needs it.
- Homework (optional, sell it well): run the decrap exercise on a real
  folder of your own — e.g. your itslearning export.
- Homework, the 10-minute version: **write your profile.** Talk for 90 seconds
  (speech-to-text) about who you are, what you read, which school you belong to and
  what annoys you. Have the agent save it as the user-level `CLAUDE.md` / `AGENTS.md`.
  Then ask one question from your field, with and without it.

**Day 1 cut list**, in the order to reach for them:
1. Plain-text exercise → 25 min (drop Track B; it's opt-in anyway).
2. Step 3 above → one sentence, as written.
3. POWER deck → drop Exhibit C (security); it's the most self-contained exhibit.
**Never cut:** the hero exercise, the 13:00 git reflex, or the grievances slot.

---

## Day 2 (Thu) — LLMs for research

**Goal of the day:** every participant does one real research-adjacent
task on their own material. Demo the heavy stuff, hands-on the
universal stuff.

### 10:00–10:30 · Recap + homework debrief (discussion)

- Show of hands: who wrote a profile, and whose answer changed? One example,
  30 seconds.
- Two volunteers tell their real-folder decrap story (triumph or
  disaster, both teach).
- **~5 min · the framing that earns skills (do this off the back of the debrief).**
  You have just heard two people describe cleaning a folder **for the second time**
  — once here, once at home. Say the obvious thing out loud:
  > *"That's twice now, by hand. Do it a third time — or write it down once."*
  That is the entire argument for skills, and this is the only moment in the course
  where the room has actually *felt* a routine repeat. **Don't build anything here**
  — the folder skill gets built Friday morning (`handouts/project-structure.md`).
  This is 5 minutes of motivation, and it's what makes `gather-refs` land at 11:00
  as an answer to a question they now have.
  - *Why it matters:* without this, the first skill in the course is built the very
    first time anyone gathers references — i.e. the course argues "skills are for
    repeated routines" while demonstrating one on a routine that never repeated.
- Fix lingering setup issues *now*; day 2 has no slack for it later.

### 10:30–12:00 · References + your first skill (open 7 · I-drive 20 · You-drive 63)

> **Open with the stakes, not the exercise (~7 min).** This block used to begin
> "references make the ideal first skill," which is true and motivates nobody. It
> now opens with the fact that fabricated citations are *in the literature right
> now*, including next to people in this building. Twenty minutes later they will
> have caught fabrications themselves — so the hook has an answer, and the answer
> is the block. Full sourcing: `examples/references/README.md`.

**The opening, in three beats:**

1. **The audit (~2 min).** Topaz et al. (2026), "Fabricated citations: an audit
   across 2·5 million biomedical papers," *The Lancet*, 1779–1781. **97.1 million
   references checked; 4,406 fabrications across 2,810 papers.** The trend is the
   payload: **1 in 2,828 (2023) → 1 in 458 (2025) → 1 in 277 (2026).**
   - *Cite it precisely, in the block about citing precisely:* it is a **Letter**,
     not a study. Flemyng and Hosseini have publicly questioned its methodology
     transparency, and it doesn't separate load-bearing citations from incidental
     ones. Say both — you're modelling the behaviour, not just describing it.
2. **The one that came close to home (~3 min). ✅ Verified, PDF in hand.** Muda &
   Yangxuan (2026), *SEM* 33(3), cites **Foldnes & Grønneberg (2024), "Factor
   analysis with improved chi-square tests," BJMSP 77, 1–23,
   `doi.org/10.1111/bmsp.12295`**. That DOI resolves cleanly — to an **untitled
   2022 editorial acknowledgement**, volume 76, pages 257–258. The paper does not
   exist. Foldnes is a colleague and close collaborator: one step from the room.
   - **The escalation that makes it land:** the paper then reports **numerical
     results** for "Foldnes F1" and "Foldnes F2" — Type I error rates, chi-square
     values, percentage improvements — across several tables. *There are simulation
     results in a peer-reviewed methods journal for methods whose source does not
     exist.* Still unretracted.
   - **Attack the system, not the two authors**, then say the generous thing —
     which is also the rigorous one: **retraction is the best remaining outcome
     *for them*,** and it gets less available every month that audits keep
     scanning. Defuses the "witch hunt" reflex before anyone voices it, and lets
     you land a hard example without punching down.
   - ⚠️ **Two different claims — know which you're making.** *"The paper they cite
     doesn't exist"* is airtight. *"The method doesn't exist"* is **not yet
     proven** — Foldnes really does work on chi-square corrections (Foldnes &
     Olsson 2015; the pEBA line), so F1/F2 might garble something real.
     **Settle it with Foldnes before Thursday**; if unresolved, make only the
     airtight claim. It's more than strong enough alone.
   - Full walkthrough, with the beat order and the free T&F-403 bonus, in the key.
3. **The correction that matters most, and be emphatic (~2 min).** Models have
   improved *enormously*. **A current model with search does not invent a DOI** —
   the honest failure mode is now a *wrong* paper or a *failed fetch*, both of
   which you catch in seconds. The rise through 2026 is the **installed base of
   practice**, not frontier capability: free tiers, memory-only prompting, and no
   checking step, on papers drafted a year or more before they appeared.
   > **The models got better. The practice didn't.**
   - **Then prove it live rather than asserting it.** Re-run the garden-of-forking-
     paths query on a current model *with search on*. It resolves correctly, or it
     says it can't find it. They watch it happen — worth more than any benchmark
     number, and unarguable in the room.
   - ⚠️ **Do not quote a per-model hallucination percentage.** The 2026 citation
     figures circulating online come from SEO content farms with no traceable
     method. Grounding-cuts-hallucination is well supported; a specific "X% of
     citations" number is not. Using an unsourceable statistic *here* would be
     self-refuting.
   - The landing: **the tool was never the problem — the missing check was.** That
     is exactly what the next 70 minutes teach, so the hook resolves into the
     exercise instead of just frightening people.

- Frame: references make the ideal first *skill* — real, universal, and
  *checkable*, so hallucination has nowhere to hide.
- **The demo topic: the `p < 0.05` debate** (`examples/references/wishlist.md`,
  instructor key in that folder's `README.md`). Chosen because it's *about*
  statistics rather than technically statistical — a law professor can follow "should
  we stop saying significant?"; nobody can follow cube-root asymptotics. You're the
  domain expert, so you can referee the output live.
  - **Framed as half-remembered titles, not a clean topic** ("there's that ASA
    statement… a Nature piece signed by hundreds… something called the garden of
    forking paths…"). That's how literature searches actually start, it tests
    *resolution* rather than listing, and it gives them the template for their own turn.
  - **Interactive open:** ask the room what *they* half-remember about p-values before
    showing the list. Live suggestions are a bonus; the banked wishlist means the demo
    runs identically if nobody bites.
  - **No fabricated traps needed — the literature supplies them.** "Garden of forking
    paths" is not the title of any published paper (agents invent a journal and DOI
    for it); the Nature comment has two equally-correct titles; Trafimow & Marks is
    literally titled "Editorial" (agents invent a descriptive one); Benjamin et al.
    has 72 authors and a genuinely ambiguous year. All verified — see the key.
  - ⚠️ **The catch worth building the block around:** Taylor & Francis 403s every
    automated client, so the *most central papers in the debate are formally open
    access and unreachable to an agent*. And `nature.com/…​.pdf` returns **HTTP 200
    with HTML** — a naive agent saves a login page as `.pdf` and **reports success**.
    Open one "downloaded" PDF on the projector and find an interstitial: that single
    moment justifies the whole verification habit. Lesson: *"I couldn't get the PDF"
    ≠ "it's paywalled" ≠ "it doesn't exist."*
- **Gather what you need (the worked example):** point the AI at a short
  wishlist; it resolves each to a real paper (title/authors/year/DOI),
  downloads the open-access PDFs into a **gitignored** `references/pdf/`,
  writes a one-line note per paper, builds `references.bib`, and lists the
  DOIs it *couldn't* get in `references/to-fetch.md` for manual library fetch.
- **Make it a skill:** once it works, say "turn that workflow into a skill" —
  the AI writes the skill file; they never learn the format. Frame with the
  checklist analogy ("memory is the AI remembering you; a skill is you writing it
  down"), and be honest that skills are an *optional* power-up for repeated
  routines — you can do a lot without them.
- **Clean what you have:** the provided trap list (15 entries, 3 subtly
  fake, 2 wrong DOIs) — verify against the web, produce clean BibTeX with a
  report. Then bring-your-own-bibliography.
- Teaching payoff: `.bib` and notes are text → tracked; PDFs are binary and
  copyrighted → gitignored. The gitignore lesson lands on real stakes.
- Handout: `handouts/references.md`.

### 12:00–13:00 · Lunch

### 13:00–14:15 · Literature sweep (You-drive)

*Full key — twelve papers, what each actually found, and the real answer to "which
ones disagree?": `examples/litsweep/README.md`. Rebuild the folder with
`python3 scratch/examples/scripts/fetch-litsweep-example.py`.*

- **Open with exploration (~20 min, `examples/references/explore.md`).** This fixes
  the block's cold start — it currently begins "here is a folder of PDFs" with no
  account of where such a folder comes from. Now the afternoon runs
  **explore → gather → compare → verify.**
  - The contrast with the morning is the teaching point: *retrieval fails loudly
    (the DOI doesn't resolve), exploration fails silently (you never learn what it
    missed).* Exploration is where the agent is most useful and least checkable.
  - Ladder: ask wide → **ask for the opposition** (a leading question returns a
    literature that agrees with you) → ask the same thing three ways and compare →
    **seed-check** → follow citations → ask what it *couldn't* find.
  - **Rung 4 is the one that matters.** They already resolved six papers this
    morning, so: *"which of these did your search surface, and which did it miss?"*
    If it misses things you know are there, it's missing things you don't know are
    there **in the same proportion.** Costs one prompt, uses no new props, and
    transfers directly to their own field.
  - **Don't undersell this half.** It routinely surfaces work people didn't know
    existed *in fields they know well* — expect a "how did I not know about this?"
    per serious search. That's the headline, not a consolation prize.
  - The distinction to draw, because someone will raise it: **"systematic" names a
    method, not a quality level.** An agent can genuinely find *more* than a
    systematic search and still not be one — because nobody wrote down the system. A
    systematic review's product is the **protocol** (pre-specified terms, named
    databases, inclusion criteria, a date), not superior recall.
  - **Then close the loop to yesterday:** *"log the queries you ran, what you
    excluded and why, and the date."* Write it down so it can be checked — it doesn't
    make it systematic, but it makes it defensible and repeatable.
  - **Skip the generic-limitations lecture.** Two questions do more work than any
    caveat list: *"did you read the full text or only the abstract?"* and *"that was
    shallow — go deeper."* The second reliably produces a visibly better map, which
    teaches the real lesson: **the first pass was never the ceiling.** Depth is a
    decision you make, not a limit you accept.
  - Those with their own topic feed their exploration into the sweep below; the
    provided PDF folder is the fallback for everyone else.
- **Provided: `vibing.jonasmoss.com/litsweep.zip`** — twelve open-access papers on
  **AI in higher education** (meta, relatable, every department has opinions), all
  CC-licensed, all verified. 15.4 MB.
- Task ladder: summarize one PDF → build a comparison table across
  all (research question, method, sample, finding) → ask "which papers
  disagree with each other and about what?" → export the table to
  Markdown/CSV for their own use.
- **The disagreement question has a real answer, and it's the best fifteen minutes
  of the block.** Four axes, in the key. Headline: Kestin (AI tutoring beats
  active learning, 0.73–1.3 SD) vs Bastani (−17% once the AI is taken away) *look*
  like a flat contradiction and aren't — Bastani's *scaffolded* arm did no harm
  either, so both papers converge on **"a tutor that withholds answers helps; a
  chatbot that hands them over becomes a crutch."** No single paper says that
  sentence. The room gets there by reading methods, which is the whole point.
- **Honesty checkpoint baked in:** send them to the **`finding` cell of the
  Bastani row**. Nearly every table renders it "generative AI harms learning";
  the abstract says only the *unguarded* arm did. Checkable in thirty seconds, and
  the failure is the table's shape, not a hallucination — which is the more honest
  and more useful lesson. This plants day 3's verification lesson.
- **One of the twelve has been retracted** (Wang & Fan 2025, a meta-analysis
  claiming g = 0.867) — and `grep -i retract` on its extracted text returns
  **zero hits**, because the RETRACTED watermark scrambles in the text layer. A
  human opening the PDF sees it instantly. Don't warn them; ask afterwards.
- Those with their own PDF stash use it instead — better, it's *their*
  literature. **But assume most won't have one on the machine** (no prep was
  asked for), so the provided folder is the *primary* path here, not the
  fallback. Anyone who can reach their own PDFs via OneDrive/email should be
  nudged to — it's strictly better when it's available.

### 14:15–14:30 · Break

### 14:30–15:15 · The interval nobody reports (I-drive, then the room joins)

*Full key + verified numbers: `examples/simulation/README.md`. Reference script
`examples/simulation/partial-r2.R` — **don't hand it out**, the agent writes it live;
it's there to check against and as a wifi-failure fallback.*

- **This is the day's "much more than you think" block.** Everything else on Day 2 is
  handling other people's work — finding, checking, tabulating, which is roughly what
  people expect AI to do. Here it does **methodology**, live, and that's a different
  category.
- **Hook:** *"Everyone here has reported an R². Hands up if you've ever reported a
  confidence interval for it."* No hands. *"Why not?"* — because there's no button for
  it in SPSS and the formula is awkward. The objection was never principled; it was
  **tooling**. And the tooling problem is over.
- **The ask, one sentence:** simulate a survey study (satisfaction ~ salary +
  autonomy + commute, correlated predictors, n = 100), fit it, compute partial R² for
  autonomy, bootstrap a 95% CI.
- **The reveal (verified):** partial R² = 0.119, **p = 0.0005** — sails through any
  review — and the 95% CI is **[2.4%, 27.3%]**, an order of magnitude wide.
  > **Significance and precision are different things.** We report the first and stay
  > quiet about the second, because one had a button and the other didn't.
- Then the sample-size table: at **n = 50** the lower bound is **0.001** (can't rule
  out essentially nothing); even at **n = 1000** it's still [5.7%, 12.1%].
- **The escalation, if the room is hot (~10 min): "does the interval actually work?"**
  This is the beat that separates *automating a known method* from *probing an open
  question*. Simulate 2000 studies where the truth is known, count how often the 95%
  interval contains it — runs in ~30 s. **Verified (pairs bootstrap):** normal
  **94.1%**, heteroskedastic **95.3%** — both fine; **heavy-tailed (t₃) 90.3% — it
  breaks.** Say the business-school part out loud: **heavy tails are the normal
  condition** — returns, incomes, sales, firm sizes. There's no clean off-the-shelf
  fix for a heavy-tail-robust interval on this quantity: *that's a gap in the
  literature, found in ten minutes.* Script: `examples/simulation/coverage-check.R`.
- **Tell the cautionary tale on yourself** (it's in the key): the first run used 400
  reps and reported 97% for heteroskedasticity — "the bootstrap turns conservative."
  At 2000 reps it's 95.3%. **The finding was noise, and re-running it bigger cost
  thirty seconds.** Cheap simulations are cheap to get wrong; the old excuse that a
  proper one was expensive has expired. Also worth a sentence: the heteroskedastic
  row has a different true value (0.037 vs 0.083) — *the estimand moved.*
- **Let the room drive the variations (~10 min)** — each is a one-line re-run: bigger
  n, more correlated predictors, overall R², true effect of zero, exact noncentral-F
  instead of bootstrap. **Say the payload out loud:** a methodological question that
  used to mean hunting for the right formula or a week of RA time is now a sentence.
- **Their turn (~15 min), and this is the generalization that travels:** *"what do you
  report without an interval?"* Cohen's d, an indirect effect, Cronbach's alpha, a
  difference in fit, a marginal effect, an elasticity. One technique on the board:
  **resample the data, redo the whole calculation, look at the spread.**
- Honest note, kept short: the bootstrap isn't always the right interval (small
  samples, bounded quantities like R² are where it wobbles). Then the useful half —
  *a rough interval you actually computed beats a point estimate reported alone.*
- *Fallback if the room is cold or non-quant:* the old plan still works — messy CSV →
  clean → fit → "explain this to a reviewer" → figure, with the punchline that the
  same loop runs on interview transcripts, legal texts and marketing copy.

### 15:15–16:00 · Open lab (You-drive)

> **⚠️ Retitled from "your own research mess" — that title assumed prep nobody
> did.** This was the last block still expecting them to have brought something.
> **Lead with "finish something you already have."** By 15:15 Thursday every
> person in the room has made a cleaned folder, a handbook, possibly a cleaning
> script, a `references.bib`, a cleaned trap list and a 12-paper comparison table.
> That is more than enough raw material for 45 minutes, and continuing your own
> half-finished work is a *better* exercise than starting something cold.

- **Open with the menu of things they already have** (full list in
  `content/day-2.md`): extend the comparison table into a synthesis; run the
  cleaning workflow over a bibliography that actually matters to them; change one
  decision in yesterday's cleaning script and read the diff; render the handbook
  somewhere readable; re-run the decrap on a real folder of their own.
- **Then** the bring-your-own list, for anyone who can reach real material via
  email/OneDrive/USB — always the better exercise when it's available.
- **This is the elastic block.** It absorbs every overrun from earlier in the day
  by design, and it is also where the fast people go deep while you finish
  helping the slow ones. Both of those are the block working, not failing.
- Point at `handouts/security.md` before anyone uploads anything real.
- Last 15 min plenary: one win and one fail per table section.

**Day 2 cut list:** stats demo → 20 min; open lab absorbs all other
overruns (it's elastic by design). Never cut the references block.

---

## Day 3 (Fri) — LLMs for teaching, and using them correctly

**Goal of the day:** everyone leaves with one real artifact for their
autumn course, and a working bullshit-detection routine.

### 10:00–10:45 · Recap + capability talk #2 + write down where things go

> **⚠️ This block was 30 minutes and is now 45 — course factory moves to
> 10:45–12:00 (75 min).** The folder skill has to be built somewhere on Friday and
> this is its only honest home: it *is* the AGENTS.md lesson, and "make it
> repeatable after you've felt the friction" is exactly this block's theme.
> Course factory at 75 min is still the longest hands-on block of the day, and the
> Day 3 cut list already nominated capability talk #2 for trimming — so if you'd
> rather not borrow the 15 minutes, cut `landscape` slides 5–7 instead and keep
> 10:30. **Decide before Friday, not during it.**

**The skill build (~25 min, You-drive)** — handout `handouts/project-structure.md`,
skill `.claude/skills/tidy-project/SKILL.md`.

- **Callback to open with:** Thursday morning they agreed that cleaning a folder
  twice by hand is silly. This is where they stop doing it.
- **Do not hand out a layout — ask the four questions.** *What do you re-explain
  every time · where does undone work live · where are you allowed to be wrong ·
  what could you not rebuild?* Those are the four roles (standing context, pending
  work, exploration, products) in their own vocabulary. **The answers are the
  skill.** Handing them a structure would answer the questions for them and destroy
  the entire lesson — this is the most literal "you are in control" moment in three
  days, and it only works if the convention is unmistakably theirs.
- ⚠️ **Do not demo the real `cleanup-paper`/`paper-init` skills as the build
  target** — they're a year of maturation (templates, migration maps, conformance
  checks) and dumping them is too much at once. Show one for **60 seconds at the
  end**, as *"same four roles, after a year of being annoyed by it."* Payoff, not
  spec.
- **Question 3 is the one that stalls people**, and the stall is the finding: if
  nowhere in your project is safe to be wrong, you aren't exploring — or you're
  doing it somewhere that will embarrass you later.
- **Question 4 has the sharp edge:** a table built by hand in Excel over two
  afternoons is not rebuildable. It's Wednesday's "leave a trail" lesson arriving
  by a different road, and it lands harder here because it's *their* folder.
- **The check that makes it trustworthy:** *"how many files before, how many now?"*
  They must match. One prompt, and it's the difference between a tool you'd trust
  with your archive and one you wouldn't.
- **Reading the residue is rung 4 and it's the best part:** a `legacy/` pile of one
  *kind* of file means the convention is missing a role — add it and re-run. That's
  the whole lifecycle of a skill, felt in ten minutes: it improves because it
  annoyed you. A template is finished the day you write it; a skill isn't.

**Then the rest of the block (~20 min, I-drive):**

- **`landscape` deck (`content/slides/landscape.md`, `/slides/landscape`, ~15 min)** —
  moved here from Day 1: rent-a-brain, the makers, **not interchangeable**,
  subscription-vs-API + what a token costs, prompting-isn't-magic. Lands better now
  that they've *used* a model for two days. If time's short, slides 5–7
  (scaling / benchmarks / pricing) are the cut candidates.
- Where this is going: agents that run longer, scheduled tasks,
  AGENTS.md/CLAUDE.md — "how I tell the AI about my project once
  instead of every time". **This now follows straight on from the skill they just
  wrote** — `AGENTS.md` is simply the *standing context* role, which they already
  named themselves twenty minutes ago. Show this very course repo as the example
  (yes, the course is built the way the course teaches — including
  `.claude/skills/tidy-project/`, which is the skill they just built, in the wild).
- **Connectors mini-demo (reach into your world):** point the agent at
  `examples/grades/scores.xlsx` and ask it to draft a results email —
  summary + per-group table, straight into a Gmail draft. Punchline: it
  *drafts*, it doesn't *send* — connectors prepare, you approve. Nothing
  leaves the machine but the draft you choose to send.

### 10:45–12:00 · Course factory (You-drive, 75 min)

- **They brought nothing — and it doesn't matter.** No prep was asked for, but
  every professor in this room can describe their own course from memory in five
  lines: who the students are, what they should learn, what evidence would
  convince you they learned it. **That's rung 0, and it's their real material** —
  which is what `vision.md` actually asks for. The provided syllabus
  (`examples/syllabus/`) is the fallback for anyone who'd rather not use their own,
  not the default path.
- Handout: `handouts/course-factory.md`. Instructor key: `examples/syllabus/README.md`.
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
- **GitHub beat first (~10 min, before the rungs):** accounts, one repo, what Pages
  is. This moved *here* deliberately — Day 1 teaches git as an undo button with no
  GitHub at all, and the account-creation time sink lands where it's actually needed.
  Frame it the non-technical way (`handouts/github.md`): a safe copy in the sky, and
  the agent runs the commands. Anyone who already has an account helps a neighbour.
- Rung 2 (ambitious): publish a one-page course site on GitHub Pages —
  this is where day 1's git quietly pays off, AI does the heavy lifting.
- Rung 3 (the bold): both, plus their day-2 literature table as a page.
- *Fallback:* GitHub account creation is a known time sink; rung 2 is
  demo-only if the wifi or account gods are angry.

### 14:15–14:30 · Break

### 14:30–15:15 · Using LLMs "correctly" (I-drive + discussion)

*Full prep, with every factual claim sourced and tiered:
`intro-notes/grievance-answers.md`. Participant take-home: `handouts/verification.md`.*

- **Answer the parked day-1 grievances explicitly — close that loop.** Read their
  own words back to them first; it proves Wednesday wasn't crowd control. Then
  answer **only the ones they actually raised** — three done properly beats five
  skated over. The five prepared, with sources: cheating (detectors are biased
  against non-native English writers — a live risk at *this* school), hallucination,
  deskilling (**the strongest of the five — concede it**), energy (the room is
  miscalibrated in both directions, and the honest version indicts the agentic
  workflows *we just taught*), copyright (split into three questions; only the
  disclosure one has teeth).
- **Stance:** concede fully where it's true, push back hard where the proposed
  *remedy* is worse than the problem. Conceding everything is mush; dismissing
  everything loses the skeptics you spent three days earning.
- The verification habits, distilled from the three days: plan before
  execute; save first then be reckless; show-me-your-evidence; spot-check one
  row; never paste what you haven't read. One page, `handouts/verification.md`.
- **Live hallucination demo — don't invent one, use the verified trap.** Ask for a
  citation for "the garden of forking paths" (`examples/references/README.md`,
  item 3): agents reliably invent a journal, volume and DOI for a manuscript that
  was never published. Don't announce the error — ask the room if it looks wrong.
  It won't. *That's* the lesson. Then re-run **with search on** and let them watch
  it get much closer: the failure mode depends on the harness you gave it.
  ⚠️ Rehearse the night before; fabrication is probabilistic. Fallbacks in the key.

### 15:15–16:00 · Take-home artifact + wrap-up (You-drive)

- Finish and "ship" one artifact: cleaned course folder, verified
  bibliography, exam + rubric, slide deck, or course page. Committed
  to git, naturally.
- Wrap-up: the cheat sheet, `handouts/verification.md`, where to get help, what's
  worth automating first when they're back at their desk. (No booklet — dropped.)
- Course evaluation (yes, you may ask the AI to draft your feedback,
  no, please write it yourself).

**Day 3 cut list:** capability talk #2 → 15 min; rung 2/3 of the
Quarto block → demo. Never cut the take-home artifact time.

---

## Materials to build (extracted TODO)

**Status at T−3 days (9 Aug).** Days 1 and 3 have a plan *and* a prop for every
block. What's left is two Day-2 props and three screenshots. Ordered by how much
they'd hurt:

- [x] **`decrap-me.zip`** — `scratch/examples/scripts/make-decrap-example.mjs` now emits it alongside
      the folder (so they can't drift), and `scripts/build-pages.mjs` ships it with
      the site. Live at **`vibing.jonasmoss.com/decrap-me.zip`** after the next push.
      Verified: unpacks as a `decrap-me/` folder, 87 files.
- [ ] **Three leaderboard screenshots** for the POWER deck — currently rendering as
      "📷 screenshot needed" placeholders: AtCoder WTF 2026 standings, Psyho's 2025
      "Humanity has prevailed" post, ICPC 2025 scoreboard. Sources are mapped in
      `content/slides/images/README.md`. Must be real captures — do not fabricate
      evidence in a deck whose thesis is "verify the claim".
- [x] ~~Pre-course email~~ — **decided against.** No participant prep beyond having
      a paid subscription. Everyone installs in the room; `handouts/install.md` is
      printed and handed out at 10:00 instead. See the decision box at the top.
- [ ] **Test pandoc on one IT-managed Windows laptop** (T−2 weeks) — Word→Markdown
      needs it for the 14:30 block. `examples/plain-text/course-handbook.md` is the
      unblocking fallback either way.
- [x] One-page terminal cheat sheet (print) — `handouts/terminal-cheatsheet.md`
- [x] `decrap-me` — synthetic WISEflow grading export (`examples/decrap-me/`,
      generator `scratch/examples/scripts/make-decrap-example.mjs`); **zip still outstanding, above**
- [x] Email/scores connectors demo — read `scores.xlsx`, draft a results email
      inline (`examples/grades/`, generator `scratch/examples/scripts/make-scores-example.py`)
- [x] Warm-up exercise sheet (day 1 morning) — `handouts/warmup.md`
- [x] git & GitHub intro (non-technical) — `handouts/github.md`
- [x] Sandboxing & security handout — `handouts/security.md`
- [x] "Leave a trail" props (day 1, 14:30) — messy `course-handbook.docx` (+ `.md`
      fallback) with five planted traps, and `survey-responses.csv` for the data
      track: `examples/plain-text/`, generator `scratch/examples/scripts/make-plaintext-example.py`,
      handout `handouts/plain-text.md`, instructor key in the example README.
- [x] "Gather-refs" wishlist + instructor key (day 2) — `examples/references/`,
      the `p < 0.05` debate as half-remembered titles; 16 verified citations, all
      traps genuine (no fabrication needed), OA/paywall mix so the DOI-handoff fires
- [x] Reference list with 3 fakes + 2 wrong DOIs (day 2, "clean what you have") —
      `examples/references/messy-list.bib`, 17 entries, key in that folder's README
      (Part 2). Both wrong DOIs **resolve to a different real paper** rather than
      404-ing, which is the far nastier trap: Trafimow & Marks' swapped DOI lands on
      the *2016* editorial with the same authors, title, journal **and pages** — only
      volume and year differ. All 3 fakes verified absent from Crossref, OpenAlex and
      web search; both fake DOIs 404 at Crossref *and* doi.org. Re-verified 9 Aug.
      ⚠️ Demo **Trap 2** on the projector (clean 200 → wrong paper); Trap 1 hits a
      T&F 403 from an agent, which is a different — also useful — lesson. Noted in key.
- [ ] Folder of ~10 open-access PDFs on AI in higher education (day 2)
- [x] Day-2 methodology demo — "the interval nobody reports" (partial R² + bootstrap
      CI): `examples/simulation/` (key with verified numbers + reference R script)
- [ ] Reviewer-suggestion example (day 2): own abstract + real journal (main);
      synthetic journal — fake editorial board + candidate pool with planted traps
      (a great-fit reviewer secretly on the board, one co-author COI) as the offline
      fallback. Frame it as *verify*, not *decide*.
- [ ] Anonymise-for-double-blind example (day 2): strip author names, self-citations,
      and identifying acknowledgements from a draft, then verify it caught them all.
      Self-contained, no web needed.
- [x] **The structure skill (Thu 10:00 framing + Fri 10:00 build)** —
      `.claude/skills/tidy-project/SKILL.md` (a real, working skill, shipped in this
      repo so Friday's "the course is built the way the course teaches" is literal)
      and `handouts/project-structure.md`. Four questions → four roles; the
      participant's answers *become* the convention block, so the judgement is
      unmistakably theirs. Deliberately **not** a template — handing out a layout
      would answer the questions for them.
      ⚠️ **Adversarially tested three times on messy git repos; 24 defects found and
      fixed.** The first version relocated the inside of `.git/` into `legacy/` and
      destroyed the repository — in a course that teaches git as the safety net.
      Verified now: git survives (`git mv`, history follows, `git fsck` clean),
      file counts preserved, running it twice changes nothing, and both handback
      commands (`git commit` / `git reset --hard`) do what they claim.
      **Do not "simplify" the never-touch list or the git handback** — that's where
      the damage was.
- [x] Day-3 "using LLMs correctly" (14:30) — sourced grievance answers with
      verification tiers (`intro-notes/grievance-answers.md`) and the one-page
      participant routine (`handouts/verification.md`). Live hallucination demo
      reuses the *verified* garden-of-forking-paths trap rather than a new one.
      All five grievance answers carry live sources (Liang et al. 2023 on detector
      bias; Epoch AI on energy; USCO Part 2; COPE/ICMJE).
- [x] Day-3 course factory (10:30) — fictional ORG 3402 syllabus with deliberately
      planted mush outcomes (`examples/syllabus/`), participant ladder
      (`handouts/course-factory.md`), instructor key with the Herzberg brief and a
      minute-by-minute 90-min plan. **Rung 0 is their own course from memory**, so
      the syllabus is a genuine fallback. All DOIs Crossref-verified.
- [x] Day-3 slides + course page (13:00) — messy ORG 3402 lecture notes
      (`examples/lecture-notes/`), participant ladder (`handouts/slides-and-site.md`),
      instructor key with a minute-by-minute plan and the Quarto-install escalation
      ladder. **Rung 0 is "make the agent install its own renderer"** — framed as the
      capability, not an apology — with a verified reveal.js-from-CDN path if it
      can't. Quarto render tested end to end on the real notes (1.9.38, 8 sections).
      ⚠️ reveal.js **6.0 moved the plugin paths**; boilerplate pins `@5`, and the
      silent-failure check is in the key: **press `S`.**
- [x] ~~The booklet~~ — **dropped.** It assembled material that isn't finished.
      Print `handouts/terminal-cheatsheet.md` and `handouts/warmup.md` only.
- [x] **Handouts published to the site** (`/handouts`, linked in nav). With no
      booklet and no pre-course email this was the only delivery route left.
      Auto-discovers `handouts/*.md`, so new ones appear without touching the build.
- [x] `handouts/install.md` re-pointed for **in-room** use (it read as a
      pre-course email). Both PowerShell install URLs re-verified live on 9 Aug;
      Node requirement corrected to 22+; stale `developers.openai.com/codex/*`
      links replaced; `claude doctor` and the WinGet fallback added.
