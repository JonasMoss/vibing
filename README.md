# AI in the terminal — course materials

This repository contains the working materials and website for the BI faculty
course **AI in the terminal: Claude Code and Codex for research and teaching**,
12–14 August 2026.

The website and its slides draw their content from Markdown files in
[`content/`](content/). The web code is deliberately small: the material should
remain easy to inspect, edit, reuse, and hand to an AI agent.

## Run the website

Windows PowerShell:

```powershell
npm install
npm run dev
```

Then open <http://localhost:3000>.

macOS or Linux:

```bash
npm install
npm run dev
```

## Where to write

- `content/course-overview.md` — the short course introduction
- `content/day-1.md`, `day-2.md`, `day-3.md` — participant-facing day pages
- `content/slides/opening.md` — opening slide deck, separated by `---`
- `app/` and `components/` — website presentation and interaction

The opening deck is a normal webpage. Use the arrow keys to move through it and
`F` to enter or leave fullscreen. The site uses vinext so the same small
Next-style application builds directly for the course host.
