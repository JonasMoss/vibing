# examples/who-is-asking — same question, different askers

Instructor demos and test runs for the `what-it-knows` deck (Day 1, 11:35). One question
goes to Claude Code or Codex **once per profile**, and the answers come up one
after another. There are three sets. Each is a folder with `question.txt` plus one
`.md` per profile, and "blank" (no profile) is always added first.

| Set | Question | Profiles |
|---|---|---|
| `coffee/` | "Is it bad to drink coffee every day?" | 12-year-old Minecraft fan · thin professor (job title + sailing) · 180-word meta-analyst |
| `schools/` | A/B test: 48/1,000 vs 62/1,000, "Is B better?" | frequentist (Fisher, Neyman–Pearson, Mayo) · Bayesian (Gelman, Jaynes, McElreath) |
| `berger/` | the same A/B question | "My intellectual idol is Jim Berger." (the live demo, as a backup) |

```bash
./ask.sh                                   # Claude Code, coffee set
./ask.sh codex schools                     # Codex, frequentist vs Bayesian
./ask.sh claude coffee "Why is the sky blue?"   # a set's profiles, your question
```

All calls run in parallel, so expect one to two minutes. The script copies the
profiles into a fresh temp folder before it asks. That matters: both tools also
read context files from the folders *above* the current one, so running inside
this repo would feed the course's own `AGENTS.md` to every profile. Each profile
folder gets `AGENTS.md` (read by Codex) plus a one-line `CLAUDE.md` containing
`@AGENTS.md` (read by Claude Code). Answers are kept in the temp folder; the path
is printed at the end.

## What came back (September 2026)

**Coffee** (both tools gave the same pattern):

- **kid:** "not a great idea" for someone your age, plus alternatives. Claude
  also used a Minecraft potion analogy.
- **professor:** close to blank. Claude added a tip about coffee and seasickness
  when sailing. That's a good moment to point out that the model uses whatever you
  tell it, even when it isn't relevant.
- **professor-rich:** named studies with confidence intervals, a rating of how
  good the evidence is, and a "what would change my view" section. It had picked
  up the profile's pet peeves.

**Schools** (both tools split the same way):

- **blank:** a frequentist answer. p ≈ 0.17, the confidence interval includes
  zero, "inconclusive". Codex's blank answer is almost word for word its
  frequentist one. Claude's blank also mentioned the Bayesian 91% in passing.
- **frequentist:** "not established". Claude added a Mayo-style severity table.
- **Bayesian:** "Probably, yes": P(B > A) ≈ 0.91, plus the expected loss of
  each choice and a recommendation to ship B.
- If a statistician in the room objects that 0.91 is just 1 minus the one-sided
  p = 0.085, they're right. Under a flat prior it's the same information. The
  demo isn't about the number; it's that the headline, the framing and the
  recommendation flip.

**Berger** (the live demo's one line):

- **Claude:** used Sellke, Bayarri and Berger (2001), the bound −e·p·ln(p) ≈ 0.82,
  and concluded "at least a 45% chance that there's no real difference". That's
  more sceptical than the Gelman-style Bayesian: the name picked a specific school.
- **Codex:** ignored the one-liner and gave the default frequentist answer. Two
  longer wordings ("I'm a statistician, and my intellectual idol is Jim Berger.",
  "…Keep that in mind when you answer me.") only added a generic "92% chance B is
  better". So demo on Claude, and tell Codex users to write more than one line.

## The message

After the demo, the takeaway is: **write everything you can be bothered to.
Format doesn't matter. Tell the model which stereotypes you are.** Talking for
90 seconds with speech-to-text works well here.

## Letting the room modify it

Participants invent their own changes. The by-hand version needs no script: make
two folders, put an `AGENTS.md` in one (create it in Notepad on Windows, because
`echo > file` in Windows PowerShell 5.1 writes UTF-16), open the tool in each,
and ask the same question. Change one thing in the profile and ask again.
