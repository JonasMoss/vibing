# examples/lecture-notes — props for "One source, one screen, one link" (Day 3, 13:00)

Handout: `handouts/slides-and-site.md`. Prerequisite reading for the participants:
`handouts/github.md`.

| File | What it's for |
|---|---|
| `motivation-at-work.md` | Messy lecture notes — **fallback only**, for anyone who brought nothing |

Participants should use **their own** notes. This file exists so that nobody sits idle
for 75 minutes because their material is in a Word file on OneDrive they can't reach.
Say that out loud when you point at it, or half the room will use the fallback out of
politeness and miss the point of the day.

---

## What's in the notes, and why

A bachelor Organisational Behaviour lecture (ORG 3402, session 6): Herzberg's
two-factor theory, self-determination theory, goal-setting theory, and "does pay
motivate?". Roughly 45 minutes of material.

Deliberately shaped like real notes: bullet fragments, headings at three different
depths for no reason, timings scribbled in the margin, notes-to-self in brackets, a
table that is really just two lists side by side, and a "leftovers" section at the
bottom.

**The content is accurate.** The theories say what the notes say they say, and the
meta-analytic numbers (Judge et al. 2010, `r ≈ .15`; Jenkins et al. 1998, `r ≈ .34`
for quantity, n.s. for quality) are real. This matters: participants from Leadership
and Organisation will read the generated deck closely, and a factual error in the
prop would hijack the block.

Three things are planted:

1. **Four unresolved `TODO` markers**, three of them `TODO: find that reference` —
   the autonomy-supportive leadership meta-analysis ("Slemp? Deci et al. 2017?"), the
   Wells Fargo "eight rhymes with great" quote, and the UC salary-disclosure study
   ("Card, Mas, Moretti & Saez? AER, around 2012"). The fourth is a `TODO: check that`
   on the claim that Herzberg's KITA piece is the most reprinted HBR article ever.
   Note that three of the four are half-remembered cites the lecturer flags as
   uncertain — exactly the material an agent is most tempted to tidy up.
   Most agents flag them rather than inventing a citation — a good, cheap moment:
   *"notice that it told you rather than filling the gap."* If an agent *does* quietly
   promote one of those hedged guesses into a confident citation, that is an even
   better moment, and it is Friday afternoon's hallucination beat arriving early.
2. **An explicit cut list at the bottom** ("if I'm running long, cut: the SMART
   digression..."). Ask the room: *did your deck respect it?* Most won't have. It's the
   fastest demonstration that the agent optimises for coverage, not for a 45-minute
   slot.
3. **Maslow, named once and never explained.** He appears in exactly one subordinate
   clause — *"the famous one **is** the true one, and it's not Maslow"* — as a
   dismissal, with no hierarchy, no five levels, no content at all. Every model in the
   world wants to put Maslow in a motivation lecture, and here it has just enough
   licence to try. The check to hand people:
   > Does this deck contain any theory that isn't in my notes?

   If a pyramid or a "hierarchy of needs" slide appeared, the agent expanded a
   throwaway dismissal into a topic — drift, on material they can actually evaluate,
   and much more convincing than a warning slide. (It usually behaves. Ask the room
   anyway; the participants who *did* get a Maslow slide will say so.)

---

## Timing — 75 minutes, 13:00–14:15

| | | |
|---|---|---|
| 13:00–13:10 | **GitHub beat** (I-drive) | Accounts, one repo, what Pages is. `handouts/github.md`. Everyone starts the sign-up *now* so email confirmation and 2FA happen in the background while we do Rung 0. Anyone who already has an account pairs with a neighbour. |
| 13:10–13:22 | **Rung 0 — install** (hands on keyboards) | "Install Quarto, and if you can't, tell me why." **Hard stop at 13:22.** While it runs, they find their own lecture notes. |
| 13:22–13:25 | **Fork the room** (I-drive) | Two announcements: who has Quarto, who is going the reveal.js route. Frame the second group as the group with the *simpler* path, because they are. |
| 13:25–13:50 | **Rung 1 — notes → deck → tweak** | First render fast, then the conversational edits. Push them to do at least four rounds. Walk the horseshoe. |
| 13:50–14:05 | **Rung 2/3 — publish** | Anyone with a working GitHub account publishes. Everyone else watches a neighbour and keeps the local file. |
| 14:05–14:15 | **Two decks on the projector** | One Quarto, one reveal.js — pick them during the walk-around. Then the "one argument per screen" beat from the handout, done live on a volunteer's deck. |

Absorb overruns from Rung 2/3, never from Rung 1.

---

## When Quarto won't install (assume it happens, plan for it)

This is the likeliest failure in the whole three days: IT-managed Windows 11, no local
admin. Have the ladder ready so you can say the next step in one sentence instead of
reading a webpage in front of the room.

**The escalation ladder the agent should walk (Windows):**

1. `winget install --id Posit.Quarto -e` — **will pop a UAC administrator prompt.** If
   they don't have the password, cancel it. Don't fight it, don't call IT.
2. The **per-user `.msi`** from <https://quarto.org/docs/get-started/>. On most managed
   images this installs into the user profile without admin. (Known and confirmed
   behaviour: the winget package needs admin, the direct `.msi` generally doesn't —
   quarto-cli issue #11987.)
3. The **portable zip**, `quarto-<version>-win.zip`, from
   <https://github.com/quarto-dev/quarto-cli/releases/latest>. Unzip anywhere in the
   user profile; `bin\quarto.exe` runs immediately. Adding it to the *user* `PATH`
   needs no rights either. No installer, no admin, nothing registered.
4. Blocked by SmartScreen, an application-allowlist policy, or a download filter →
   **stop.** Go to reveal.js.

macOS, for the minority: `brew install --cask quarto`, or the `.pkg` from the same
page. Rarely a problem.

**Your rules in the room:**

- **Four minutes per person, maximum.** Then reveal.js. Say the time limit out loud at
  13:10 so switching reads as a branch, not a defeat.
- **Do not debug it yourself.** Hand it back: *"Read the error, tell me what blocked
  you, and give me my options."* You are modelling the behaviour the handout teaches;
  crouching over someone's laptop teaches the opposite.
- **Say the actual lesson.** The install ladder above is the agent doing something
  genuinely hard — reading a Windows error, inferring a permissions model, and finding
  the door that isn't locked. That is the demo. Nobody in the room has ever had a tool
  install itself around a policy before.

---

## What the reveal.js fallback looks like when it works

One `.html` file, no installation, opens by double-clicking. Verified working against
reveal.js 5.2.1 in a real browser (10 Aug 2026): navigation, theme, markdown plugin,
speaker-notes plugin, `?print-pdf` export (one PDF page per slide), no console errors.

The shape you're looking for when you glance at a participant's file:

```html
<link rel="stylesheet" href="https://unpkg.com/reveal.js@5/dist/reveal.css">
<link rel="stylesheet" href="https://unpkg.com/reveal.js@5/dist/theme/white.css">
...
<script src="https://unpkg.com/reveal.js@5/dist/reveal.js"></script>
<script src="https://unpkg.com/reveal.js@5/plugin/notes/notes.js"></script>
<script>Reveal.initialize({ hash: true, plugins: [ RevealNotes ] });</script>
```

**⚠️ The one path that goes wrong — and it depends on the version.** reveal.js **6.0**
moved the plugins, so the two layouts are exactly inverted (all four re-checked
10 Aug 2026):

| plugin path | `@5` (5.2.1) | `@6` (6.0.1) |
|---|---|---|
| `plugin/notes/notes.js` | ✅ 200 | ❌ 404 |
| `dist/plugin/notes.js` | ❌ 404 | ✅ 200 |

Same for `markdown` and `highlight`. **Neither form is "the wrong one"** — each is
correct for its own major version, which is why every source you find looks confident
and half of them are useless to you. Pinned `@5` *and* pinned `@6` both work fine, as
long as the plugin paths match the pin.

**Why this matters in the room:** an *unpinned* URL (`unpkg.com/reveal.js/…`, no `@5`)
resolves to **6.0.1** today. So the failure to expect is 6.x core with 5.x plugin
paths — and it is **loud, not subtle**. The plugin script 404s, `RevealNotes` is never
defined, and the standard `Reveal.initialize({ plugins: [ RevealNotes ] })` line throws
before Reveal ever initialises. Since reveal's CSS hides every slide until initialisation,
what the participant sees is a **completely blank white page**. Verified in a browser,
not reasoned about.

That is good news for you: nobody sits on this one unaware. It announces itself.

**Symptom → cause → what to say.** All four states below were reproduced in a real
browser on 10 Aug 2026:

| What they see | What it is | Hand it back with |
|---|---|---|
| **Blank white page** | 6.x core, 5.x plugin paths — JS threw on init | *"The page is blank. Read the browser console, find the error, and fix it."* |
| **Deck works, `S` does nothing** | plugin script never loaded, but init didn't throw | *"Speaker view doesn't open — the notes plugin isn't loading. Fix it and prove it by pressing S."* |
| **Text overlapping / spilling off-screen** | the CSS 404'd | *"The layout is broken — the reveal.js stylesheet isn't loading. Check the CDN paths."* |
| **Looks right, `S` opens the speaker window** | correct | nothing. Move on. |

- **Keep the `@5` pin in the boilerplate above** — verified end to end, and a
  major-version pin is the whole reason it can't drift under you mid-course.
- **Don't hand-edit paths for them.** The console error is right there, and reading an
  error message back to the agent is the exact skill this block is teaching.
- **`S` is still the last check before anyone relaxes** — it is the only one of the four
  states that a glance at the screen won't catch.

*This gotcha is also the best unscripted teaching moment in the block, if you want it:
a confident answer that is correct for the wrong version is exactly the failure the
whole course is about — and note that the way to catch it was to open the thing and
look, which is the habit we spend three days selling.*

**Keyboard, for the projector demo** (all verified): arrows/space to navigate, `Esc`
or `O` for the overview grid, `F` fullscreen, `S` for the speaker window with timer and
next-slide preview, `B` to black the screen. Adding `?print-pdf` to the URL and
printing gives a clean PDF handout.

**Why this is not a consolation prize, and say it in these words:** it is already a web
page, so Rung 2 is *shorter* for this group — nothing to render, no `_files` folder to
lose on the way to GitHub Pages. The Quarto group has to remember `embed-resources:
true` to get the same single-file convenience.

The only real cost is that the CDN wants internet on first open. The fix is in the
handout (ask for a local copy of reveal.js), and it takes about fifteen seconds.

---

## If the wifi or the account gods are angry

**Flaky wifi.** Note first that if the network is genuinely down, nobody has a working
agent at all and this is a whole-course problem, not a block problem. The parts unique
to *this* block are one small CDN fetch (fine on a bad connection) and GitHub. If the
CDN is unreachable, the Quarto route still works offline once Quarto is installed —
send the reveal.js group to a neighbour's screen and continue.

**GitHub account creation — the real time sink.** Email confirmation plus mandatory
2FA (phone or authenticator app), on a laptop where the corporate password manager may
also want a say. Expect a handful of people not to make it. Mitigations, in order:

1. **Start the sign-up at 13:00, not 13:50.** The whole point of putting the GitHub
   beat first is that the waiting happens in parallel with Rung 0.
2. **Rung 2 becomes demo-only.** Publish *your* deck on the projector, live, start to
   finish — repo, push, Pages, refresh, link. Ninety seconds. Everyone sees the payoff
   even if only half the room performed it.
3. **Have a repo with Pages already enabled** so the "and here is the link" moment
   cannot fail on stage. Then show this course's own site — `vibing.jonasmoss.com` is
   plain Markdown in a repo, built and published exactly this way. The material they've
   been reading all week *is* the demo.
4. **Everyone keeps the artifact regardless.** The deck exists as a file on their
   laptop. Publishing is Rung 2 for a reason; nobody leaves empty-handed because
   GitHub wanted a phone number.

Written follow-up for the stragglers: `handouts/github.md` plus Rung 2 of
`handouts/slides-and-site.md` are enough to finish it alone at their desk, which is a
perfectly good outcome and should be described that way rather than apologised for.

---

## The beat not to cut

At 14:05, on a real participant's deck, in front of everyone: click through it at
presentation speed, find the four slides that are one idea, and fix them by saying so.

> These four slides are one idea. Make them one slide, put the rest in the notes.

A rendered deck looks finished, and the agent fills slides rather than making
arguments. "One argument per screen" is the judgement the participant supplies, and
watching it happen once is worth more than the sentence in the handout.
