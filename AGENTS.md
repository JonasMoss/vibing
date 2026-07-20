# AGENTS.md — vibe-faculty course repo

This repo holds the materials for **"AI in the terminal: Claude Code and Codex
for research and teaching"** — a faculty course at BI Norwegian Business School.
Anything an agent produces here is course material for that audience, so read
this file before writing anything.

## Hard facts (from the official invite, `AITerminal.pdf`)

- **Dates:** Wed Aug 12 – Fri Aug 14, 2026. Three days, 10:00–16:00, lunch
  12:00–13:00. **15 hours total.** (An older `plan.md` says 4 days — that is
  outdated; the PDF wins.)
- **Room:** C2-040 "Harvard", Campus Oslo — an executive/MBA horseshoe room.
- **Capacity:** 30 registered; expect **~20 actual participants**.
- **Tools:** Claude Code or OpenAI Codex (participants bring a **paid** Claude
  or GPT subscription). BI's Gemini subscription is explicitly out (no
  filesystem access).
- **Language:** English. **Instructor:** Jonas Moss (jonas.moss@bi.no).
- **Prerequisites:** none, "but we will use the terminal actively".

## Who the participants are

- Faculty from *all* BI departments: marketing, law, finance, leadership,
  economics, communication — not just data science.
- **Strong opinions, weak terminal skills.** Assume zero shell knowledge.
  Many will have never opened a terminal. Do not assume git, package
  managers, or even "what a path is".
- **Mostly Windows 11 laptops**, often IT-managed (possible admin-rights
  issues). A minority on macOS. Plan instructions Windows-first.

## Pedagogy stance

- **Mostly hands-on practice, a little capability talk.** Short demos and
  "what can these things actually do" segments are wanted, but the bulk of
  every day is participants typing into their own machines.
- Participants work on **their own real material** when possible, with
  premade example problems as fallback.
- **Speech-to-text** is part of the workflow we teach (lowers the typing
  barrier).
- Course goals (from the invite): LLM-friendly project setup, very basic
  git, terminal comfort, using LLMs "correctly". Content pillars: LLMs on
  your filesystem / for research / for education.

## Example-problem policy (important)

- **Simple, domain-neutral, immediately relatable wins.** The flagship style
  is "decrap your itslearning export": take a messy real folder and have the
  AI clean, rename, and organize it.
- **Avoid** stats-heavy or C++/programming-heavy examples. Jonas has complex
  examples in those domains but they alienate this audience — the domain
  knowledge required drowns the lesson about the tool.
- Good example domains: syllabi, exams, reference lists / BibTeX, messy
  download folders, Word-to-Markdown conversion, course web pages, Quarto
  slides, email/admin drudgery.

## Conventions for this repo

- Plain text everywhere: Markdown for prose, Quarto for slides, BibTeX for
  references. No Word documents as source material.
- Course materials are written in English, friendly and informal in tone,
  but not sloppy: participants are professors.
- Handouts/instructions must give **Windows (PowerShell) commands first**,
  macOS/Linux variants second.
- A small printed/PDF **booklet** is a planned deliverable (see `plan.md`).
- `links.md` / `links/` collect reference reading; add sources there, one
  per line, ideally with a one-line annotation.
