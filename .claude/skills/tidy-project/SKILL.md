---
name: tidy-project
description: >-
  Sort a project folder into roles — standing context, pending work, exploration,
  and products — using a convention declared in this file, never deleting anything.
  Unrecognised files go to a legacy/ holding pen, and the residue reveals whether
  the convention is complete. Use when a project folder has turned into a pile,
  when starting a new project, or when checking an existing one still matches its
  own structure. Trigger words: tidy, clean up, restructure, organise this folder,
  sort out this project, new project.
---

# Tidy project

Most folders are a pile because files with completely different *jobs* sit next to
each other: a half-finished thought beside a finished table, a note-to-self beside
the thing you'd send a co-author. Once they're mixed you can't tell at a glance
what's safe to change.

This skill separates files by **what kind of claim they are**, not by file type.

## The four questions

| Question | The role | Why it must be separate |
|---|---|---|
| What do I re-explain *every single time*? | **standing context** | So you say it once, not every session |
| Where does undone work live? | **pending work** | So state survives the conversation ending |
| Where am I allowed to be wrong? | **exploration** | So there is somewhere it is safe to be wrong |
| What could I not rebuild? | **products** | So nothing is asserted that can't be re-derived |

Four roles, but a real convention has **more folders than roles** — products
usually split into a manuscript and its tables, and inputs and code earn their own
rows because they fail differently. That's expected. The roles tell you *why* each
folder exists; the block below is where you say what they're called.

## YOUR CONVENTION — edit this block. It is the only opinionated part.

```
standing context  ->  AGENTS.md      [single file, at root]
pending work      ->  TODO.md        [single file, at root]
exploration       ->  notes/
products          ->  manuscript/    (the output of record — prose, the paper)
products          ->  results/       (tables, figures, rendered output)
code              ->  code/          (anything that regenerates a product)
inputs            ->  data/          (given to you; never edited by hand)
holding pen       ->  legacy/        (unrecognised — never deleted)
```

**Why `inputs` and `code` are separate rows.** An input you edited by hand is
unrecoverable; a product you edited by hand is merely unreproducible. And code is
what makes a product a product — bin the script and the figure stops being
re-derivable. Delete any row your projects don't have.

**The re-derivability test is mechanical, not a vibe — and it governs `results/`
only.** A *result* is a product if something else in this project regenerates it:
a script, a source document, a documented procedure. If nothing does, it belongs
in `notes/` until something does. The **manuscript is assigned by role, never by
this test** — nothing regenerates your paper, and it is obviously not exploration.
Do **not** classify by name-smell: `FINAL v3` tells you nothing, and a table with a
script behind it is a product no matter what it's called. When a hand-built table
does land in "exploration," say why out loud — it looks like a malfunction and it
isn't.

## What to do

1. **Check for an existing convention.** If a `README.md` already documents a
   *different* structure, stop and ask which wins.
   - **A file already at its convention destination is already correctly placed —
     do not inventory it, do not move it.** That includes the root-level files:
     `README.md`, `AGENTS.md`, `TODO.md`. Miss this and the second run buries the
     first run's own output in `legacy/`.
   - **Running twice must be safe and must change nothing the second time.** Check
     this before you report success.
   - On a re-run you *may* propose promotions — e.g. a table in `notes/` that a new
     script now regenerates belongs in `results/`. Propose; never move unasked.

2. **Inventory and propose, in one pass.** List every eligible file with its size
   and its proposed role, as a single table.
   - **Binaries** (`.docx`, `.xlsx`, `.pdf`, images): filename and extension are
     sufficient. Do not open them.
   - **Plain text** (`.txt`, `.md`, `.csv`, code): **skim it.** Contents beat the
     filename — a file called `notes to self.txt` whose body is a list of undone
     tasks is *pending work*, whatever it's named. Classifying text by filename
     alone is how the obvious case gets missed.
   - **Unrecognised is not the same as ambiguous**, and they go different places:
     *no* role fits → the holding pen; *two* roles fit → the questions list. Decide
     which before you propose anything.

3. **Wait for approval. Move nothing before it.** If a file could plausibly take
   two roles, it goes on the questions list. If *more than one* file maps to a
   single-file role (two candidates for `TODO.md`), all of them go on the questions
   list — never pick one silently.

4. **On approval, move.** Create the folders and move the files. Never copy-and-
   delete, never overwrite.
   - Preserve relative sub-paths inside the destination (`stuff/notes.pdf` →
     `notes/stuff/notes.pdf` — the sub-path is preserved; the *role* was decided
     separately), so provenance survives. **Unless the folder name carries no
     information** — anything matching `New folder`, `Ny mappe`, `Nytt`,
     `untitled`, `temp`, `Mappe1`, **including numbered variants like
     `Ny mappe (2)`** — in which case flatten it and say so. Treat that list as
     examples, not an exhaustive set: if the name tells you nothing about the
     contents, it's junk. Recreating a junk-named folder inside the clean structure
     is technically correct and reads as a bug.
   - On a name collision, keep both: the incoming file becomes `name-1.ext`
     (before the extension, so it still opens on a double-click). Flag it. Never
     overwrite.
   - For a **single-file role**, rename the file into place, and say so — a `.txt`
     becoming `.md` is fine; a `.docx` becoming `.md` is not, so leave binaries
     where they are and note it instead.
   - **Files still on the questions list do not move.** Leave them exactly where
     they are and list them. Never block, never guess.
   - **In a git repository, use `git mv`** so history follows the file — and
     `git add` the `README.md` you write in step 5. Skip that and the handback in
     step 7 lies: `git commit` silently omits the README, and `git reset --hard`
     leaves it orphaned, describing a structure that no longer exists — which
     deadlocks step 1 on the next run.
   - Once files are moved, **empty leftover directories may be removed.** Removing
     an empty directory is not deleting anything.
   - **Only create `legacy/` if something goes in it.** An empty one is noise, and
     git won't track it anyway.

5. **Write or update `README.md`** describing what now lives where and why, in the
   human's own words wherever they gave any.

6. **Report**, in this order: count of pre-existing files before and after, how
   many landed in each role, everything in the holding pen, and every unresolved
   question. **Count the same set both times** — eligible files only, excluding
   everything on the never-touch list and excluding the `README.md` you just
   wrote. Counting one way before and another way after raises a false alarm.

7. **Hand back the undo.** In a git repository the moves are now *staged but not
   committed*, which is a state a git novice cannot read. Say so, and give both
   commands in plain words:
   - keep it — `git commit -m "tidy project structure"`
   - undo all of it — `git reset --hard HEAD` *(warning: also discards any other
     uncommitted work)*

   Never run either one yourself. The whole safety argument rests on git, so
   leaving someone staring at "Changes to be committed" with no next move is a
   defect, not a detail.

## Never touch

Not eligible for inventory, moving, or the holding pen — **skip silently**:

```
.git/  .svn/  .hg/          version control internals
.Rproj.user/  renv/         R project + environment state
.venv/  venv/  __pycache__/ Python environment state
node_modules/               package installs
~$*                         Word/Excel lock files
.DS_Store  Thumbs.db        OS junk
```

Moving the inside of `.git/` into a holding pen destroys the repository — which is
the one thing in the project you were relying on to undo this. Anything else
starting with a dot: leave it where it is, don't move it.

**Skip them from the tidy, but say one sentence if any are tracked in git.** A
repository versioning a Word lock file or `renv/library/` is worth knowing about,
and silence is the only way the owner never finds out. Report it; don't fix it.

## Rules

- **Never delete a file. Ever.** Unrecognised is not the same as worthless, and
  this skill is not qualified to tell the difference.
- **Never edit file contents.** This skill moves files and writes one README. That
  is the entire blast radius.
- **Preserve the count.** If before and after differ, say so loudly rather than
  tidying the discrepancy away.
- **Prefer asking to guessing.** A short questions list is a success, not a failure.

## Reading the residue

The holding pen is the interesting output, not the leftovers.

**The unresolved questions are residue too.** An empty `legacy/` with three files
still sitting unsorted at the root is *not* a clean run — it's a run that moved the
easy files and left the hard ones. Report both, and never call it done while the
questions list has entries.

- **Nearly empty, no open questions** — the convention fits. You're done.
- **One recurring *kind* of file piling up** — the convention is missing a role.
  Add a row above and re-run. This is the normal way this file grows, and it is
  the whole reason a skill beats a template: a template is finished the day you
  write it.
- **Large and varied** — either this folder is several projects wearing a trench
  coat, or it's genuinely junk. Both are worth knowing; neither is fixed by moving
  files around.

## Starting from nothing

Same convention, no migration: create the folders, write the `README.md`, and leave
a one-line note in each about what belongs there. An empty structure with an
explanation beats a full structure nobody can interpret.
