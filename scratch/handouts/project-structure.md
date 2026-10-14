# Write down where things go

**Day 3, morning.** Skill: `.claude/skills/tidy-project/SKILL.md`

*Read the top half — the four questions and the convention block. That's the part
that's yours. Everything below it is safety plumbing (don't delete, don't touch
`.git`, preserve the count), which you can ignore today and never write yourself.*

Wednesday you let an agent clean a folder. Wednesday night, some of you did it again
on your own material. Thursday you turned a workflow into a skill for the first time.

This is the third time you clean a folder — except this time you write it down once
and stop doing it by hand.

> **Memory is the AI remembering you. A skill is you writing it down.**

---

## You are not getting a template

There is a folder layout in the skill file. **It is not yours and you should
overwrite it.**

That isn't false modesty. Every person in this room already has a filing
convention — you can find your own 2023 exam in eight seconds and nobody else in
the building can. The convention is real. It has simply never been written down,
which is why it lives in your hands, dies when you take a co-author, and can't be
delegated to anything, human or otherwise.

**The skill is where your judgement gets written down.** The agent supplies the
execution. You supply the convention. That division is the whole course in one
file.

---

## Rung 1 · Answer four questions

Answer these about a project you actually have. Out loud, badly, in your own
vocabulary — this is not a form.

> **1.** What do you have to re-explain to a new collaborator *every single time*?

> **2.** Where does the stuff you haven't done yet currently live?
> (If the honest answer is "my inbox" or "my head," say so. That's the finding.)

> **3.** Where are you allowed to be wrong?

> **4.** What in here could you not rebuild if you lost it?

Those are the four roles. In the skill file they're called **standing context**,
**pending work**, **exploration** and **products** — but the names don't matter and
yours are probably better.

**Question 3 is the one people stall on**, and the stall is informative. If there
is nowhere in your project that it's safe to be wrong, you are either not
exploring or you're doing it somewhere that will eventually embarrass you.

**Question 4 has a sharp edge.** A table you built by hand, in a spreadsheet, over
two afternoons, is *not* rebuildable. It's a claim you can no longer check. Notice
how many of those you have — that's Wednesday's lesson arriving by a different road.

---

## Rung 2 · Turn the answers into the skill

Open the skill file, look at the convention block, then:

> Rewrite the convention block in `tidy-project` to match how I actually work:
> [your four answers]. Keep the rules and the holding pen exactly as they are.

That's it. You never learn the file format; the agent writes it.

**Keep the holding pen.** Everything unrecognised goes to `legacy/` and *nothing is
ever deleted*. It's the same reflex as committing before you let it loose — you can
be bold because the mistake is recoverable.

---

## Rung 3 · Run it on something real, and check it

Pick a genuinely messy folder. Then:

> Tidy this project.

It will show you a mapping and **stop, waiting for you.** Read it. Argue with it.
This is the part where you're the boss — the same beat as Wednesday afternoon.

Then the check that makes this trustworthy:

> How many files were there before, and how many are there now?

They must match. A tidy-up that loses three files is not a tidy-up. This costs one
prompt and it's the difference between a tool you trust with your archive and one
you don't.

---

## Rung 4 · Read the leftovers

The holding pen is the interesting output, not the leftovers.

| What you see | What it means |
|---|---|
| `legacy/` nearly empty | your convention fits — you're done |
| one *kind* of file piling up | your convention is missing a role — add it |
| `legacy/` large and varied | this was several projects in a trench coat |

The third one is common and it is not a failure of the skill. It's a folder telling
you something true that you already half-knew.

**Add the missing role and re-run it.** That's the entire lifecycle of a skill:
it gets better because you used it and it annoyed you. This is the difference
between a skill and a template — a template is finished on the day you write it.

---

## One honest caveat

Your first convention will be wrong in a way you can't see yet. Mine was — the
`inputs` role in that file exists because I spent a year conflating "data someone
gave me" with "output I produced," and hand-edited an input I could never get back.

That's an argument for writing it down *sooner*, not later. A convention you can
read is a convention you can fix. The one in your hands can only be lost.

---

## Keep

- Your skill file — specifically the eight-line convention block in the middle of
  it, which is now the most portable thing you made this week. It works on every
  project you own, forever, and it fits on a Post-it.
- One folder that's now tidy.
- The list of what didn't fit, and what you're going to do about it.
