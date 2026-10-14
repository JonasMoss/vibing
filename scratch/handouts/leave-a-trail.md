# Leave a trail

*Research session handout. After "Take a paper apart" your folder holds a PDF, a text
copy of it, scripts, results and figures, all in a pile. Turn it into something a
co-author could rerun, and check that they could. Then do the same with a copy of one
of your own folders.*

> **The floor: the rerun test passes.** After `/clear`, the agent reruns your folder
> from scratch and gets the same numbers. Everything else here is a bonus.

---

## 0. Your folder

Use the folder from "Take a paper apart".

**No folder, or only the PDF in it?** Use the practice folder instead: a small survey
experiment, cleaned by hand in Excel, analysed twice and written up in Word. Start
the agent in an empty folder and ask:

> Download vibing.jonasmoss.com/messy-project.zip into this folder and unzip it.

---

## 1. A save point

Before the agent moves anything:

> Set up git here and commit everything.

From now on nothing it does is permanent. You don't need to learn any git commands.
You ask, and the agent runs them.

**The first time you use git**, it needs your name and email:

> Set up git with my name, *Your Name*, and my email, *you@bi.no*.

**Git not installed?** See step 5 of the install handout. If you can't install it
today, skip the git steps. Everything else works without it.

---

## 2. Organise

> Organise this folder so a co-author could rerun everything. Show me the plan first.
> Don't move anything yet.

**Argue with the plan.** Folder names, where the raw data goes, what happens to old
versions. Nothing should be deleted: old versions can go in a folder of their own.
When you're happy:

> Go ahead.

---

## 3. A README and a project file

> Write a README for a co-author, and a project file for you.

- The **README** is for people: what this is, and how to rerun it.
- The **project file** (`CLAUDE.md` or `AGENTS.md`) is for the agent. It reads it
  every time it starts in this folder. It holds what the project is, where things
  go, and rules such as "never edit the raw data".

Then:

> Commit.

---

## 4. The test

Type `/clear`. The agent now knows nothing about this folder, just like a new
co-author. Then:

> Rerun everything from scratch. Do you get the same numbers?

**Not the same, or it can't?** That's the useful part. Ask:

> What's missing? Fix it, so that the next rerun works.

Repeat until the test passes.

---

## 5. See what changed

> What changed since the last commit?

Every file moved and every line edited, listed. If you ever want to undo everything
since the last commit:

> Go back to the last commit.

---

## 6. Now your own folder

Copy a real project folder (right-click, **Copy**, then **Paste** somewhere else),
start the agent in the copy, and do steps 1–4.

**Not a folder with personal or confidential data.** Everything the agent reads is
sent to the AI service.

---

## Why text

| | Invisible | Visible |
|---|---|---|
| **Writing** | Word: you can't see what changed | Text: every change shows |
| **Data** | Clicking in Excel: no record | A script: the steps are the record |

- **Writing in LaTeX?** A `.tex` file is already text.
- **Writing in Word?** Keep Word for the paper itself. Keep the rest in text: notes,
  scripts, READMEs. When you need a Word copy of something, ask:

  > Make a Word copy of README.md.

  It may ask to install a tool; say yes.

**Opening a Markdown (`.md`) file**

- **Windows 11:** right-click the file, **Open with**, **Notepad**. Notepad shows the
  headings, lists and bold text.
- **Mac:** right-click the file, **Open With**, **TextEdit**. It shows the plain text,
  which is readable as it is. That's the point of Markdown.
- Or ask the agent: *"Open README.md in Notepad."* (Mac: *"in TextEdit"*.)

---

## For the round-up

- Did the rerun give the same numbers the first time?
- What couldn't be rebuilt?

---

## Worth reading

- **The Plain Person's Guide to Plain Text Social Science**, Kieran Healy. Written for
  social scientists, not programmers.
  <https://kieranhealy.org/files/papers/plain-person-text.pdf>
- **Good enough practices in scientific computing**, Wilson et al. (2017), *PLOS
  Computational Biology*. For researchers who are not software engineers.
  <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510>
- **Spreadsheet horror stories**, EuSpRIG. Real incidents with price tags, including
  Norway's oil fund and its one wrong date.
  <https://eusprig.org/research-info/horror-stories/>
- **Gene name errors are widespread in the scientific literature**, Ziemann, Eren &
  El-Osta (2016), *Genome Biology*. Excel turns gene names into dates.
  <https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7>
