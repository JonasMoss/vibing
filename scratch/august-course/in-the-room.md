# In the room — the decision card

*Print this. It is the only page you hold while standing up.*

Everything here is **pre-decided**, so that when the room splits you are
*selecting* a move rather than inventing one. Improvisation feels bad because it
happens under pressure. This removes the pressure, not the improvisation.

---

## 1. The opening — Wednesday, 10:00, before anything else

Sixty seconds. Do not skip it; it pays out for three days.

> Quick thing before we start, and it matters for all three days.
>
> Look around. Some of you have never opened a terminal. Some of you write code
> for a living. Six departments in this room. I am **not** going to fix that
> spread by teaching at the speed of the middle — that gives you a course that
> bores half the room and drowns the other half.
>
> So instead: every exercise is a **ladder**. There is a floor — I'll tell you
> what it is each time — and there is no ceiling. You climb until I stop you. If
> you clear the floor in ten minutes and your neighbour takes fifty, **you both
> did it right.**
>
> And when you're done: turn to the person next to you and get them running. I am
> one person and there are twenty of you. The fastest way through this is that the
> room teaches itself — and you will learn more fixing someone else's problem than
> watching your own thing work.

**Why it works:** unnamed variance gets read as failure by both ends — the fast
decide it's remedial, the slow decide they're drowning. Named, the same variance
reads as design to everyone.

---

## 2. Standing rules — all three days

| Rule | Say it like this |
|---|---|
| **The floor** | "Floor for this one is *X*. Past that, go as far as you like." |
| **The deputy** | "You're done — get your neighbour running." Status, never a chore. |
| **Hands up, not heads down** | "Nobody debugs alone and nobody debugs silently." |
| **No such thing as done** | There is no finish line to fail to reach. Only rungs. |

---

## 3. The four branches

Four moves. That is the whole repertoire — pick one, say it out loud, move on.

| # | Move | Fire it when | Say |
|---|---|---|---|
| **1** | **Drop to the floor** | >1/3 of the room is below the floor with <10 min left | "Everyone stop where you are. If you've hit the floor, go help someone who hasn't." |
| **2** | **Pair up** | 3+ machines broken, or one person stuck twice | "Two to a laptop for this one. Whoever's typing is not the one who understands it." |
| **3** | **Demote to demo** | The exercise is failing for environmental reasons (wifi, install, accounts) | "Everyone watch my screen for five minutes — then you do it." |
| **4** | **Plenary early** | Spread is unmanageable, or the energy drops | "Stop. Two of you show me what you got." Harvest, then move on. |

**Branch 3 is the underused one.** A demo everyone sees beats an exercise a third
of the room can't run. It is not a defeat.

---

## 4. Per-block: floor, first cut, and the 20-minutes-behind move

### Day 1 — Wednesday

| Block | The floor | Cut first | If 20 min behind |
|---|---|---|---|
| 10:00 POWER + how-it-works | *(talk)* | Exhibit C (security) — most self-contained | Skip how-it-works; it's recoverable Friday morning |
| 11:15 Install | Tool launches and answers one question | Nothing — this *is* the floor | Pair the unfixed and **break at 12:00 regardless**; fix over lunch |
| 13:00 **Decrap** 🔒 | Commit, let it execute, look at the result | Step 5 (the README) | Shorten the plenary to one volunteer, not two |
| 14:30 Leave a trail | Track A rung 1: into text + **one** question you didn't know the answer to | Track B entirely (it's opt-in) | Then rung 3 → demo the render on the projector |
| 15:25 Git + **grievances** 🔒 | See one `git diff` land | Step 3 (rest of git) → one sentence | Git becomes *"ask the AI to set up git; we'll use it Friday"* |

🔒 = never cut. **The grievances slot is load-bearing for Days 2 and 3** — it's the
debt Friday afternoon pays off. Day 1 runs ~30 min over on paper; it pays out of
the cut column, not out of the locks.

### Day 2 — Thursday

| Block | The floor | Cut first | If 20 min behind |
|---|---|---|---|
| 10:00 Recap | *(discussion)* | Homework debrief → one story | Straight to 10:30; fix machines during the next block |
| 10:30 **References** 🔒 | Resolve the wishlist; **catch one thing that's wrong** | The "make it a skill" step | Then drop the messy-list half — the wishlist alone carries the lesson |
| 13:00 Literature sweep | Comparison table + **verify one row** | The `explore.md` opening (20 min) | Give the table columns instead of letting them derive them |
| 14:30 The interval nobody reports | Watch it happen *(I-drive)* | The coverage-check escalation | Skip the sample-size table; keep the CI reveal |
| 15:15 Open lab | Take **one** existing thing further | — | This block absorbs the overruns. That's its job. |

### Day 3 — Friday

| Block | The floor | Cut first | If 20 min behind |
|---|---|---|---|
| 10:00 Landscape + connectors | *(talk)* | Slides 5–7 (scaling/benchmarks/pricing) | Drop the connectors demo |
| 10:30 Course factory | Rungs 0–2: your course → questions → rubric, and **notice the mushy row** | Rung 5 (critique loop) | Then rung 4 (marking) → demo on one answer |
| 13:00 Slides + page | A deck you rendered, opened, and changed once by talking | Rung 3 | Rung 2 (Pages) → demo-only |
| 14:30 Using LLMs correctly | Three grievances answered + the hallucination demo | Answer 3, not 5 | Cut to the demo + the routine sheet |
| 15:15 **Artifact + wrap** 🔒 | One thing finished and committed | — | Protect this. Take it from 14:30. |

---

## 5. When *not* to intervene

Half of running a heterogeneous room is leaving it alone.

- **Someone finished in ten minutes.** Fine. Deputise them.
- **Someone is on rung 1 while others are on rung 4.** Fine. That's the ladder.
- **The room has gone quiet.** Usually people working, not people stuck. Walk
  around before you announce anything.
- **Someone is off doing their own thing entirely.** *That is the best outcome in
  the course.* Do not herd them back.
- **Two people are arguing about a prompt.** Leave them. That's the seminar.

**The one thing that always needs intervening:** somebody sitting with a broken
machine and no partner. That is the only real failure state in the room — and it
is fixed in ten seconds by pairing them.

---

## 6. What success actually looks like

Not a smooth room. Not everyone finishing together — that was never available
with this group, and chasing it makes the content generic, which satisfies
nobody.

**Two or three "I could use this on Monday" moments per person.** That's what
they remember, and it's what they tell their colleagues.

If someone leaves having only cleaned one folder and rewritten one learning
outcome — but *believes they can do it again on Monday* — that person is a
success. Awe without agency is the failure mode. Agency without polish is fine.
