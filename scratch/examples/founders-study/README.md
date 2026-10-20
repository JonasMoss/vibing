# founders-study: the .gitignore exercise (instructor key)

A fictional research project (founders who change direction early): interviews, a
survey, literature, drafts. Built by `make.py` into
`courses/2026-10-strategy/props/founders-study.zip`. Everything is made up and
marked as fictional inside the files; the names are Norwegian placeholder names.

## What should end up in .gitignore, and why

| In the folder | Why it stays out of git |
|---|---|
| `interviews/*.txt` (named transcripts, with phone numbers), `interviews/pilot *` | personal data |
| `interviews/audio/*.m4a` (12 × 1.5 MB) | personal data, and big |
| `interviews/consent forms (signed).pdf` | personal data |
| `data/survey_export_… (with emails).csv` | personal data (e-mail addresses) |
| `data/registry_extract_full.csv` (7 MB) | big, and can be downloaded again |
| `literature/*.pdf` | other people's papers (keep a `.bib` instead) |
| `api_key.txt` | a password; never in git, not even private |
| `~$aft_v3_FINAL.docx`, `.DS_Store`, `Thumbs.db`, `analysis/.Rhistory` | junk |

What stays in: the draft(s), `interview guide.docx`, `coding/` (pseudonymised:
F01–F12), `data/survey_clean.csv` (no e-mails), `analysis/table2.R`, the notes,
`ABOUT THIS FOLDER.txt`.

Points worth drawing out in the round-up:

- **Three drafts** (`Draft_v3_FINAL.docx`, `Draft_v3_FINAL (2).docx`,
  `draft_v2_old.docx`): with git you need one. Good agents suggest keeping one and
  letting the history hold the rest.
- **`survey_clean.csv` is a judgement call:** fine in a private repository,
  check the data agreement before anything public.
- **Ignored is not hidden from the agent.** It can still read the transcripts.
  That's the bridge to the access deck.
- **The check prompt** ("would anything private go along?") should make a careful
  agent look at `git status` and `.gitignore`, not just repeat what it wrote.
