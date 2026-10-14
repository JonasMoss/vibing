# git & GitHub, without the jargon

*You will never have to memorise a git command — the agent runs them for you. But
these ideas are worth holding in your head, because they quietly make everything
else safer and easier.*

---

## "But what if it wrecks my files?"

It is the first question everyone asks, and it deserves a straight answer:

> **It can't do anything you can't undo — provided you made a save point first.**

That's the whole point of git. Before you let the agent loose, you save a snapshot
of the folder. If the result is wrong, ugly, or simply not what you wanted, you go
back to the snapshot. Not "mostly back" — *exactly* back, every file, as it was.

This is what turns "I'd rather not risk it" into "let's see what it does." Most of
the value of git, for you, is the **nerve it gives you**.

**The reflex, in two steps:**

1. **"Commit this before we start."** ← the save point
2. Now let it do something bold.

Step 1 is the part people skip, and it is the part that matters: git can only restore
what you saved *before* things went wrong. A snapshot taken after the mess is a
snapshot of the mess.

> Save point, then courage. In that order.

---

## Two words, two different things

- **git** is an **undo button with unlimited history**, living on *your* computer.
  Each time you (or the agent) "commit", git saves a snapshot of your whole folder.
  You can return to any snapshot, forever. Nothing is ever truly lost.
- **GitHub** is a **copy of that folder in the cloud** — a backup you can share. Push
  your snapshots there and they survive a dead laptop, reach collaborators, and can
  even become a web page.

> git = the time machine on your desk. GitHub = the safe copy in the sky.

---

## Why a non-programmer should care

- **A real undo.** Let the AI make a bold change; if you hate it, roll back to the
  last snapshot in one step. This is what makes "just let it try" safe.
- **A history you can read.** Every change is a labelled, dated entry. "What did I
  change last Tuesday, and why?" finally has an answer.
- **A backup that isn't your inbox.** Your work lives in the cloud — not in
  `final_v3_REALLY_final.docx`.
- **Sharing and publishing.** A colleague can pull your whole project from one link;
  a course page can go live on the web. (That's exactly how *this* course's site is
  built — see Day 3.)

---

## What you actually do (the agent does the rest)

Three ideas, not three commands — just *ask*:

1. **"Set up git here and make a first commit."** Starts the history.
2. **"Commit this, with a message describing what changed."** Saves a snapshot,
   whenever you've done something worth keeping.
3. **"Put this on GitHub"** (once per project) — creates the cloud copy. After that,
   **"push my latest changes."**

You never type the commands. You decide *when* to snapshot; the agent snapshots.

---

## A healthy rhythm

Commit at every "this is a good state" moment — before a big change, after something
works, at the end of a session. Small, frequent snapshots with plain-English
messages beat one giant "stuff" commit.

> Rule of thumb: if losing the last hour would annoy you, commit.

---

## Two honest cautions

- **Public vs private.** A GitHub repository is either **public** (anyone can read it)
  or **private** (only you and people you invite). Check before you push anything with
  student data, unfinished drafts, or personal notes. When in doubt, **private**.
- **git remembers everything.** Because history is forever, something you commit and
  later "delete" still sits in the history. So don't commit passwords, keys, or
  sensitive data in the first place — see `handouts/security.md`.
