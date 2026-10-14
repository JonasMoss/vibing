# examples/paper-critique — instructor key for "Take a paper apart"

Deck: `content/slides/paper-critique.md` (`/slides/paper-critique`). Handout:
`handouts/paper-critique.md`. About 50 minutes: story and demo 10, hands-on 30,
round-up 10.

**No example papers for participants.** They find their own, in their own field.
That is the point: they can judge the answers, and you don't have to. Everything
here is for you.

## The framing

**Open with your own result (slide 2).** You did exactly this with a recent paper
in your field: it found a real problem and then a new estimator, valid under weaker
assumptions and better than the one in the paper, and your only input was pushing.
Then: *"It worked for me. I'm curious whether it works for you."* That sets up the
exercise as an experiment, so a failure in someone's field is a result, not an
embarrassment.

The bigger point, if the room is up for it: the usual way to find a hole worth
working on is weeks of reading the literature. Here the reading is outsourced, and
so is the first attempt at the fix. What stays with them is choosing the paper and
judging the problem and the fix.

**The honesty point.** Say it out loud: *"I can't tell you whether a critique of a
finance (marketing, strategy) paper is right. You can."* The agent does the reading
and the quoting; they judge. That is why "Show me where in the paper" is the first
push: a quote lets them check a claim in seconds without trusting the model.

**The questions are suggestions, not a script.** Short and conversational: *"What's
the main claim here?" · "What's the biggest methodological problem?" · "Can you fix
it?"* The pushes do the rest.

**The plain-text thread.** Two sentences, said out loud, no slide. When the first
answers come back: *"It turned the PDF into text before it could read it."* When the
fix runs: *"That script is the record of what it did."* Both pay off after the break
in "Leave a trail", which uses this folder. Hence the last round-up line: keep the
folder.

**Your demo:** a recent paper from your own field (Psychometrika or similar), where
you can judge the answers live. Ask the three questions, and push at least once on
camera.

## What the pilots showed

Two recent NBER finance papers, Claude Code and Codex, September 2026. Paper-level
notes and full answers are in `pilot/`, which is **local only** (it names real papers
and makes unverified claims about them; this repo is public).

- **The critique takes 1–1.5 minutes**, including the download. Answers were
  specific and quote-backed, not boilerplate.
- **"Can you fix it?" took 5–7.5 minutes**, with no pushing. Every run wrote and ran
  Python, reproduced the paper's own results first, and then tested its fix by
  simulation or with public data.
- **Different runs find different "biggest problems."** On the same paper, the two
  tools picked different problems and built different fixes. That is a feature for
  the room: compare with your neighbour, and ask "is that really the biggest
  problem?".
- **Nobody in finance has checked the substance yet.** Treat the pilots as evidence
  that the exercise produces something worth judging, not as findings.

## Known issues

- **SSRN returns 403 to the agent.** Journal sites are paywalled. Participants
  download in the browser and ask the agent to move the file into the folder.
  NBER and arXiv links download directly.
- **Python for the fix step.** Every fix in the pilot used Python (numpy). Bare
  Windows laptops don't have it. Mention it in the install email ("if you can,
  install Python too"); otherwise the agent will ask to install it.
- **Reading PDFs on Windows.** In the pilot both tools extracted text with
  `pdftotext`, which a bare Windows laptop does not have. Claude Code can read PDFs
  directly, so it should be fine. **Codex on Windows is untested:** it may need to
  install a tool (the handout tells people to say yes). Test on a Windows machine
  before the first session.
- **Confidentiality.** Nobody uses a paper they are refereeing. It's on the slide
  and in the handout; say it once.

## What to watch for in the room

- **"Do they address it anywhere?" is the push people skip.** A first critique is
  often answered somewhere in the paper, so people who skip it report false alarms.
  Collect one for the round-up; it teaches more than a good catch.
- **"Can you fix it?" takes 5–10 minutes** and usually means writing and running
  Python. Tell people to let it run. On a laptop without Python it will ask to
  install it: the install email should mention Python, and the handout says yes.
- **Generic first answers** are normal. The push ("what is specific to this
  paper?") usually fixes them. If it doesn't, that's a finding too.
- **If it fails badly on someone's paper, say so in the round-up.** "It could work,
  and if it doesn't, that's interesting too" is the honest framing.
