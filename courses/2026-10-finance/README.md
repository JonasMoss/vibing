# AI in the terminal — Department of Finance

**Status: in preparation.** Materials drafted 13 October; see the before-Friday checklist in `teacher-notes.html`.

## Facts

- **When:** Friday 16 October 2026, 09:00–16:00, lunch 12:00–13:00. Six
  teaching hours, one day. The room is booked until 16:45.
- **Room:** A2 – Blue 1, Campus Oslo (booked by Dagfinn Rime).
- **Who:** Department of Finance. The invitation went to 34 people; 20+ had
  signed up by 7 October.
- **Focus:** research. Setup first, then what the tools do with literature,
  data and writing, and a good part of the day on participants' own projects.
  Francesco's original split for Finance was "4 hours methodology, 2 hours
  application".
- **Bring:** own laptop, paid Claude or ChatGPT subscription, ideally a real
  project (paper in progress, dataset, messy folder).
- **Contacts:** Dagfinn Rime (Finance, organiser), Siri Johnsen (DS
  administration), Francesco Ravazzolo (DS department head).
- **Help in the room:** Ludvik Slipersæter offered to assist or observe.

The invitation as sent is `invite.md` (`invite.docx` is the Word copy that
went out with Dagfinn's email).

## Known issues from email

- **Codex install on Windows stopped for Dagfinn in August.** Helpdesk opened
  a ticket; in the end he had to click "run" in a restricted mode prompt. Have
  the workaround ready in the handout.

## Files

| File | What |
|---|---|
| `decks/menu.html` | **Open this first.** The menu; every card opens a module's deck. |
| `decks/*.qmd` → `*.html` | One deck per module: menu, power, how, setup, cleanup, knows, paper, review, refs, trail, notes, own, agents, github, mcp, more. Shared settings are in `decks/_metadata.yml`, the look is in `decks/slides.scss`. |
| `handout.qmd` → `.html` | For participants: every module, every prompt with a copy button. Email it before the day. |
| `teacher-notes.qmd` → `.html` | For the instructor: before-Friday checklist, run sheet, a card per module. |
| `props/` | `decrap-me.zip` (Do something tedious), `messy-project.zip` (Leave a trail), `references-practice.zip` (DOI check). The handout links to them on GitHub `main`. |
| `course-files.zip` | What participants download on the day: the handout plus the three practice zips. Built by `make-course-files.py` after rendering; linked from the menu deck. |
| `index.html` | The course page on vibing.jonasmoss.com: course files, handout, teacher notes, and every deck in a pane. Plain HTML; edit by hand. |
| `docs.scss` | Look of the handout and teacher notes. |

Render everything from the repo root: `quarto render courses/2026-10-finance`.

## Shape of the day

A fixed morning spine (capability talk, setup with git, a tedious cleanup with a
save point, what it knows about you, take a paper apart), then an afternoon menu chosen with the room (referee panel,
references, leave a trail, notes and structure). Everything works on one folder
with the participant's own paper in it. Details are in `teacher-notes.html`.

## Built from

`scratch/` (the September department-session modules and the August course
material). The capability deck (`decks/power.qmd`) was rewritten separately on
13 October.
