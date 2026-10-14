# Sandboxing, privacy, and "is this safe?"

*The honest version. Two different worries hide under "is this safe" — what the AI
might do to your **files**, and what happens to your **data**. They have different
answers. Here are both, plus the handful of habits that cover you.*

---

## First, the right mental model

The agent is **a very fast intern sitting at your keyboard.** It can do what *you*
can do on your own machine: read the files in the folder you point it at, create and
change them, run commands. It is not magic, and it is not a stranger breaking in —
it's your own hands, moving faster. Everything below follows from that one picture.

> **The most useful habit in this whole course: when in doubt, ask the tool.** You don't
> have to memorise any of this. *"What can you access right now?"* · *"What permission
> mode am I in?"* · *"Is it safe to work in this folder?"* — it will just tell you. The
> tool is its own best manual, and you'll hear me say so all week.

---

## Worry 1 — "Will it wreck my files?"

It *can* touch files — that's the whole point — but you're protected by design and by
habit.

**By design:**

- The tools, **by default, ask before doing anything destructive** — running a
  command, deleting, overwriting. You see the action and approve or decline. Read
  before you click yes.
- It works where you **point** it. Start it inside a specific project folder, not your
  whole `Documents`.

**By habit — your three seatbelts:**

1. **Work on a copy.** Early on especially, point it at a *duplicate* of anything
   precious. Experiments are cheap when the original is safe elsewhere.
2. **Use git.** With a snapshot, any change is one step from undo (see
   `handouts/github.md`). This is what makes "let it try" genuinely safe.
3. **Ask for a plan first.** "Tell me what you'd do — don't change anything yet." Read
   it, argue with it, *then* let it act.

> You are always the one who says "go." The AI proposes; you approve.

---

## Auto mode, safely (you'll want it)

Approving every step gets tedious fast, so you'll probably switch to an **auto mode**
that stops asking. Do — but know what you're switching off. There are **two separate
dials:**

- **Approval** — *when it stops to ask you.* Auto mode turns this down.
- **The sandbox** — *what it can physically touch,* enforced by the operating system.
  This is the "just this folder" boundary.

The catch: **turning off the asking does not turn on the boundary** — and the two tools
differ on what's on by default.

- **Codex** sandboxes by default (edits stay in your folder, network off). So
  **`codex --full-auto`** stops the prompts *and* stays inside the sandbox — auto and
  safe at once. Change it mid-session with the **`/permissions`** command (choose *Auto*).
- **Claude Code** does **not** sandbox by default. **Shift+Tab → "accept edits"** is the
  safe everyday choice: it auto-approves edits inside the folder but still asks before a
  command reaches *outside* it. For fully hands-off auto, turn the sandbox on first with
  **`/sandbox`**. Never use the "bypass all permissions" mode.

> Auto mode is fine — recommended, even. Just pair "it stops asking" with a boundary:
> Codex has a sandbox built in, Claude Code's is one command away, and the seatbelts
> above (a project folder, copies, git) protect you either way.

---

## Worry 2 — "Where does my data go?"

Think hardest here, because it's the invisible one.

**The plain truth:** when you work with the agent, your **prompts and the contents of
any file it reads** are sent to the provider's servers (Anthropic for Claude, OpenAI
for Codex) to produce the reply. Treat anything you show it like something you've
**uploaded to a cloud service** — because you have.

**So the rule is simple:** don't feed it what you wouldn't put in a cloud document.
Keep the following *out* unless you've cleared it:

- **Personal data** — student names and grades, interview subjects, anything under
  GDPR. Anonymise first, or don't share it.
- **Confidential material** — unpublished work you don't control, contracts, NDAs,
  exam papers before the exam.
- **Secrets** — passwords, API keys, anything that logs you in.

**"Does it train on my data?"** Depends on your plan. Business, Team, and API tiers
generally **do not** train on your inputs by default; some **free/consumer** tiers may
— and it changes over time, so check your own plan's terms rather than assuming. When
unsure, assume it *could* be retained, and act accordingly.

---

## Worry 3 — "It's on my managed work laptop…"

- **Admin rights.** BI-managed Windows machines sometimes block installs. If you hit a
  wall, that's an IT-permissions issue, not you doing something wrong — flag it.
- **It runs as you.** The agent has exactly your permissions, no more. It cannot do
  what your own account cannot.
- **Content from outside.** If you have it act on text from an *untrusted* source (a
  random web page, a forwarded email), stay a little alert — instructions can hide
  inside content. For everyday course work on your own files, this isn't a concern.

---

## The whole thing, in five habits

1. Point it at a **project folder**, not your whole disk.
2. **Copy** precious originals before you experiment.
3. Keep a **git** history — your undo button.
4. Ask for a **plan**, read it, then approve.
5. Don't paste **personal, confidential, or secret** material. When unsure, don't.

> None of this is a reason to fear the tool. It's the same care you'd take with any
> capable assistant who has the keys to your office.
