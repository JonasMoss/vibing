# examples/plain-text — props for "Leave a trail" (Day 1, 14:30)

Synthetic, safe to commit and hand out. Same Nordic Style / ELE37911 world as
`examples/decrap-me` and `examples/grades`, so the story carries across the days.
Regenerate with `python3 scratch/examples/scripts/make-plaintext-example.py`.

| File | Track | What it's for |
|---|---|---|
| `course-handbook.docx` | A (everyone) | A messy Word document — the real starting point |
| `course-handbook.md` | A | The same content, already converted — **fallback only** |
| `survey-responses.csv` | B (opt-in) | Messy data, for participants who actually analyse things |

**Why the `.md` fallback ships:** converting Word usually wants `pandoc`, which may
not install on IT-managed laptops. Anyone blocked starts from the `.md` and loses
nothing — the lesson is what you do *after* the conversion, not the conversion.
Verified locally: `pandoc course-handbook.docx -t markdown` renders headings cleanly.

---

## Instructor key — Track A (the document)

Five traps are planted. Participants are **not** told this; the point is that
asking the agent the right question surfaces them in seconds.

1. **The weights don't add up.** "Assessment" lists 40 + 30 + 20 = **90%**.
   → *"Do the assessment weights sum to 100?"*
2. **Two sections overlap and contradict each other.** "Assessment" says the project
   is **40%**; "Grading" says **45%**. They also restate the same material, so they
   are the natural merge candidates.
   → *"Do any two sections say the same thing? Do they agree?"*
3. **Contradictory feedback promise.** "within two weeks" (Project work) vs
   "within 10 working days" (Feedback and complaints).
   → *"List every promise made to students. Are any of them inconsistent?"*
4. **Six deadlines, six date formats**, all buried in prose:
   26 August · 5/9/25 · 12 September · 2025-11-08 · week 46 · December 3rd.
   → *"Make a table of every date and deadline in this document."*
   **This is the lightbulb moment** — it's the question a Word file cannot answer
   about itself.
5. **Inconsistent names and citation styles.** Prof. / Professor / dr.; three
   different reference formats, one with no year.

**If nobody finds trap 1 or 3, say so out loud** — a room that misses the
contradiction has just demonstrated why "the document should answer questions about
itself" matters.

## Instructor key — Track B (the data)

`survey-responses.csv`, 21 rows, deliberately filthy:

- **Country** spelled seven ways: `Norway`, `norway`, `NO`, `NOR`, `no`, `Norge`,
  plus `Sweden`/`SE`/`sweden`, `denmark ` with trailing space, and one **blank**.
- **Dates** in six formats: `2025-03-14`, `15/03/2025`, `March 16 2025`,
  `17.03.2025`, `2025/03/17`, `18-03-2025`.
- **Missing values** encoded four ways: `-99`, empty, `N/A`, `n/a` — plus `999`
  and `1 200` / `2 500` as impossible ages (thousands separators read as text).
- **One exact duplicate**: respondent `R-014` appears twice, identical.
- Stray whitespace in several fields.

The teaching point is **not** that the agent cleans it. It's that the agent writes a
**script** that cleans it — and that script is a plain-text record of every decision.
Change one decision, re-run, and `git diff` shows exactly what you changed.

**The question to end on:** *"Could someone else re-run this and get your numbers?"*

**Keep the honest caveat:** a wrong script you can read beats a right click you
can't remember. Reproducible ≠ correct.
