## Today’s finish line

Before we leave, you will have pointed an AI agent at a real folder, asked it to
understand the mess, changed its proposed plan, and watched it carry out the
work.

No previous terminal experience is assumed.

## Morning — first contact

### 10:00 · See the whole thing

We begin with a short live demonstration: a chaotic course folder goes in; a
clean, documented project comes out. Do not worry about how each step works yet.
First, see the shape of the possibility.

### 11:05 · Find your feet

First, learn to move around — four commands, no agent yet: open a terminal, `ls`
to look, `mkdir` a practice folder, `cd` into it. Round 1 of the warm-up sheet
(`handouts/warmup.md`) walks you through it; the cheat sheet is your map.

Then start Claude Code or Codex and ask:

> What files can you see here? Do not change anything.

That small exchange contains most of the technical foundation we need. Warm up with
one tiny, harmless job: have it make a `hello.md`, look at it, and delete it.

### If you are set up early · find the edge

Now play. You saw this morning what these can do; go find out for yourself. Point the
agent at something you think is *too hard* and watch:

- something from your **own field** you'd assume needs a specialist;
- something you suspect it will get **wrong** — then check the answer;
- something deliberately **vague**, to see it ask questions or make choices.

Try speaking your instructions instead of typing. **Useful failure is welcome:** if
something breaks, ask the agent what happened and what to try next. Round 2 of the
warm-up sheet has the full menu — and jot down one answer that surprised you and one
you did not trust.

### 11:35 · What it knows about you

The model only knows what is in its context window: this conversation, the files it
has read, and two files it loads at every start. It does not know who you are, so it
answers the typical person who might type your question. The fix is to write down
who you are, once:

- **Your profile** is about you: your field, your school, what you read, what annoys
  you. It lives in your home folder (`.claude\CLAUDE.md` for Claude Code,
  `.codex\AGENTS.md` for Codex) and is read in every project. It's the same idea
  as custom instructions in the chat apps.
- **A project file** (`CLAUDE.md` or `AGENTS.md` inside a folder) is about that
  project. We get to those on Day 3.

Two short exercises:

1. Tell it one thing about yourself, type `/clear`, and ask what it knows about you.
2. Ask a question from your field where the answer depends on your school or
   method. Write two or three sentences about yourself and ask the agent: *"Save
   these as my personal profile, the file you read in every project."* Type
   `/clear`, ask again, and compare with your neighbour.

**Homework:** talk for 90 seconds about who you are, with speech-to-text, and ask
the agent to add it to your profile.

## Afternoon — decrap a folder

One minute on safety first — you're about to let an agent change real files.

The question everyone has is *"what if it wrecks everything?"*, and it has a straight
answer: **it can't do anything you can't undo — provided you made a save point
first.** So before the agent touches anything, say:

> Commit this before we start.

That saves a snapshot of the whole folder. If you hate the result, you go back to it
— not "mostly back", but exactly back, every file as it was. Note the order, because
it's the part people skip: a snapshot taken *after* the mess is a snapshot of the
mess. Save point, then courage.

Belt and braces today: you're working on a provided copy anyway, so nothing of yours
is at risk. The rest — including where your data actually goes — is in
`handouts/security.md`.

You will receive the same deliberately awful folder as everyone else:
duplicates, mystery names, old exams, stray images, and several competing
versions of “final”.

Work through this loop:

1. **Inspect:** “Describe what is here. Do not change anything.”
2. **Plan:** “Propose a sensible structure and explain your choices.”
3. **Disagree:** Change at least one part of the plan.
4. **Act:** Let the agent carry it out.
5. **Check:** Open the result and inspect a few files.
6. **Document:** Ask for a short `README.md` explaining the new structure.

## Afternoon — leave a trail

The morning was about *where files live*. This block is about *what is inside them*,
and about leaving a record of what you did.

> Write it down, so it can be checked. Including by you, in six months.

Two kinds of writing-down, one idea. For **prose**: a Word file hides its own
changes, while text shows them. For **data**: clicking in Excel leaves no record,
while a script *is* the record. You are not learning to code — you are learning to
ask for the trail.

Everyone works on a messy course handbook: get it into text, then ask it the
questions a Word file cannot answer about itself — *every deadline in a table*, *do
the weights sum to 100?*, *are any of these promises inconsistent?* Then restructure
it, and render it as both a web page and a PDF from the one source.

If you analyse data, there is a second track: a filthy survey export, and one
instruction that matters — ask for a **script** that cleans it, not a cleaned file.
Change one decision, re-run it, and the difference is visible.

Both tracks end on the same question: **could someone else re-run this and get
exactly what you got?**

An honest caveat, because it matters: the agent's script can be wrong, so read it.
But a wrong script you can read still beats a right click you cannot remember.
Reproducible is not the same as correct — it is what makes correctness checkable.

Full walkthrough: `handouts/plain-text.md`.

## Late afternoon — checkpoints, and your grievances

You already used git once today, for nerve: the save point that made the afternoon
safe. Now the other half. The same tool shows you *exactly* what changed between one
version and the next — the promise from the last block, delivered — and gives you a
readable history of your own decisions. Ask the agent to do the git-ing; you only
need to know to ask. Details: `handouts/github.md`.

Then the floor is yours. Bring your objections — cheating, hallucination,
deskilling, energy, copyright. Some we answer on Friday; all of them get aired.

## The two-minute terminal kit

The same four moves work on Windows and Mac:

| Intent | Type this |
|---|---|
| List what's here | `ls` *(Windows: `dir` works too)* |
| Enter a folder | `cd folder-name` *(and `cd ..` to go back)* |
| Make a new folder | `mkdir name` |
| Start the agent | `claude` *or* `codex` |

**Tab** completes names (use it always). **Ctrl+C** stops anything. Lost? `pwd` shows
where you are. There are hundreds of other commands — ignore them; the agent runs them
for you. Full card: `handouts/terminal-cheatsheet.md`.

## Before you leave

- Keep the cleaned folder.
- Keep the `README.md`.
- Write down one instruction that worked surprisingly well.
- Write down one thing you did not trust.

Tomorrow we take the same inspect–plan–act–check loop into research.

