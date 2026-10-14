# The course factory

**Day 3, morning.** Files: `examples/syllabus/` — *fallback only.* Start with your
own course.

You were asked to bring a syllabus. Most of you didn't. That's fine, because you
don't need one: every person in this room can describe their own course in five
lines from memory. Who's in the room, what they should be able to do afterwards,
and what would convince you they can do it. That's the entire input.

In ninety minutes you turn those five lines into exam questions, a rubric, three
student answers, and a marked script — and somewhere in the middle you find out
something uncomfortable about your own learning outcomes.

> **The idea in one line:** cheap drafts let you inspect a decision you already
> made — what your students are actually supposed to be able to do.

| | The usual way | The factory |
|---|---|---|
| **Questions** | write four, hope they discriminate | draft twelve at named levels, keep four |
| **Rubric** | written after marking has started | written from the outcomes, before anyone sits the exam |
| **A bad question** | discovered at script 40 of 60 | discovered ten minutes after writing it |
| **AI-written answers** | first met at 23:00, in the pile | met here, on purpose, with the key open |

> **The floor: Rungs 0 through 2.** Describe your course, get questions at levels you
> named, get a rubric, and find the one row that says the same thing four times — that is
> the payload of this block, and stopping there is a complete run rather than a short
> one. The marking and critique loops above it are yours to take as far as you like;
> everyone here works at a different speed and the ladder was built for exactly that.

---

## Before you start

Make a folder and open your agent in it. Same two commands on every machine:

```powershell
mkdir course-factory
cd course-factory
```

(PowerShell on Windows; identical in Terminal on macOS.)

---

## Rung 0 · Tell it about your course

Five lines, from memory. No preparation, no lookup.

**This is the moment to use speech-to-text.** Ninety seconds of talking about your
own course gets you further than five minutes of typing, and you'll be more
specific out loud than you would be in writing.

> I teach *[course name]*, a *[bachelor / master / PhD]* course with about *[N]*
> students in *[subject]*. They arrive knowing *[X]* and usually struggling with
> *[Y]*. By the end they should be able to *[three things]*. What would convince
> me they can do it is *[the evidence you'd accept]*.
>
> Write that up as `course.md`: a short course description and 5–8 learning
> outcomes, split into knowledge, skills and general competence. Keep my own
> wording wherever it's already specific. Where I was vague, flag it in a comment
> instead of inventing precision I didn't give you.

That last sentence earns its keep. Without it the agent smooths your mush into
confident-sounding mush, and you never see the seam.

**Would rather not use your own course?** Use
`examples/syllabus/ORG3402-organisational-behaviour.md` — a complete fictional BI
bachelor course in organisational behaviour, with a full session plan, assessment
structure and reading list. Point the agent at it and every rung below works
unchanged.

---

## Rung 1 · Twelve questions, at levels you name

Don't ask for "exam questions". Ask for a distribution.

> Draft 12 exam questions for this course. Four that a student who has done the
> reading can answer. Four that require applying a theory to a situation they
> haven't seen before. Four that require weighing two theories against each other
> and committing to a position. Label each question with the learning outcome it
> tests. If a question doesn't test any of my outcomes, say so plainly.

Then the move that saves you an evening:

> For each question, write the single sentence you'd accept as a full-marks
> answer.

A question whose full-marks answer you can't state in one sentence is a question
you are going to argue about in the appeals meeting.

---

## Rung 2 · Build the rubric from the outcomes · ⬅ the floor

Pick the question you like best. Then:

> Build a grading rubric for question 7, derived from the learning outcomes —
> not from the question. Four levels: A, C, E, F. Every level must describe
> something an examiner could *observe in a script*, not something they would
> have to infer about the student's mind.

Read what comes back carefully. Some rows will be crisp and immediately usable.

**And at least one row will be a paraphrase ladder** — "excellent understanding /
good understanding / some understanding / limited understanding", the same
sentence in four costumes. Note which learning outcome that row came from. We
come back to it at the end, and it is the most valuable thing in this block.

**Finding that row is the floor, and you've just cleared it.** Rungs 3–5 are where it
pays off — or if you're done and the person next to you isn't, go and help them: whoever
finishes first is the room's help desk, and that holds all three days.

---

## Rung 3 · Three answers, and one of them is the payload

> Write three student answers to question 7, each about 300 words. One strong.
> One mediocre. One that is fluent, confident, well organised, correctly
> structured, and contains a substantive error in the middle that a tired marker
> would read straight past. Don't tell me which is which, and don't mark the
> error.

Now read the third one the way you read at script 40 of 60. It looks fine. It
sounds like someone who attended. The error sits in the middle of a paragraph
that starts and ends correctly.

**This is the academic-integrity conversation, and it beats any lecture on the
subject.** The subtly-wrong answer isn't a hypothetical: it's exactly what arrives
in your pile. Fluent, structured, correctly formatted, confidently wrong in one
specific place — and *plausible*, which is the part detectors don't help with. You
have just manufactured the thing you're worried about, deliberately, with the
marking key open in front of you. That is a better preparation than any detection
tool, because you now know what it looks like **from the marking side**.

The corollary is the uncomfortable half:

> **If a model that never attended your course can answer your question well,
> that is information about your question.**

Then:

> Now tell me where the error is. Then tell me which of the three answers scores
> highest on my rubric — and whether that's the right result.

Watch what happens when the subtly-wrong answer scores well.

---

## Rung 4 · Mark them

> Grade all three answers against the rubric. For each answer give me: the level
> for every row, the exact words in the script that put it there, a mark out of
> 20, and two sentences of feedback written to a student you want to see improve.

Then check it — not to catch the agent out, but because the disagreement is
useful:

**Where you disagree with a mark, the argument is almost never about the answer.
It's about a rubric row that said less than you thought it said.** Fix the row,
re-run the marking, and watch whether the mark moves. Two minutes, and you've
tested your rubric before a student did it for you.

---

## Rung 5 · Turn it on the questions

Now the critique loop. This is the part people expect to be polite and isn't.

> Which of these 12 questions are bad, and why? For each, consider: can it be
> answered from the stem alone; does it test recall when I asked for application;
> would two competent examiners give the same mark; and could a student who never
> attended answer it from general knowledge.

> Rewrite the three worst ones. Show old and new side by side and tell me exactly
> what changed and why.

If it says all twelve are fine, push:

> Rank them worst to best. There is a worst one.

---

## Rung 6 · For the bold

- > Produce a one-page marking sheet I can print: rubric on it, space for
  > comments, room for the mark.
- > Write three more variants of question 7 that test the same outcome with
  > different scenarios, so I can run this exam again next year without
  > recycling.
- > Translate the four questions I'm keeping into Norwegian, then check that the
  > two versions ask the same thing.
- > Write a short `README.md` saying what's in this folder and how to update it
  > next year.

And then, obviously:

> Commit all of this.

---

## One honest caveat

The agent will write you a rubric for **any** learning outcome you hand it.
Including the bad ones. That's the trap, and it's worth ten minutes.

Feed it *"understands the importance of organisational culture for organisational
performance"* and you get back four authoritative-looking levels that all say the
same thing in different fonts. It isn't being lazy. There is nothing else in that
sentence to build on — no performance, no object, no observable. **The rubric
comes out exactly as sharp as the outcome went in, and not one notch sharper.**

Which is a fact about your syllabus, not about the AI.

Compare a row built from *"can apply a named motivation theory to a described
workplace situation and derive at least two specific managerial actions from it,
stating which element of the theory each action follows from."* That rubric writes
itself, because the outcome already said what the student would be seen doing.

So when a row comes back mushy, don't accept it and don't blame the model:

> This row is vague because the outcome behind it is vague. Rewrite that outcome
> so it names an observable performance, then rebuild the row from the new
> version.

**You cannot assess what you never specified.** You have always known that. What's
new is that you now have something that finds the unspecified bits in about forty
seconds, on a syllabus you've been teaching for six years. The exam is the
by-product. The rewritten outcome is the win.

---

## Keep

- `course.md` — your description and outcomes, in the sharper version.
- `questions.md` — the four you'd actually set, each with its one-sentence
  full-marks answer.
- `rubric.md` — for at least one question, in rows an examiner can observe.
- `answers.md` — the three student answers, marked.
- **The one learning outcome you rewrote today.** If you keep nothing else, keep
  that. It's the only thing here that improves the course rather than the paperwork.

---

## Worth reading

Three short ones, all making the same point from different directions.

- **Enhancing teaching through constructive alignment** — Biggs (1996), *Higher
  Education*, 32, 347–364. The canonical statement that outcomes, activities and
  assessment have to be built as one object. If you've ever been told to "align"
  something, this is where it comes from.
  <https://doi.org/10.1007/BF00138871>
- **Formative assessment and the design of instructional systems** — Sadler
  (1989), *Instructional Science*, 18, 119–144. Argues that students can only
  close the gap on a standard they can actually see — which puts the burden on
  you to be able to state it. The best argument there is against the paraphrase
  ladder. <https://doi.org/10.1007/BF00117714>
- **Assessment rubrics: towards clearer and more replicable design, research and
  practice** — Dawson (2017), *Assessment & Evaluation in Higher Education*,
  42(3), 347–360. Identifies fourteen separate design decisions hiding inside the
  word "rubric". Useful precisely because it shows how much you're deciding by
  default. <https://doi.org/10.1080/02602938.2015.1111294>
