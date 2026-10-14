# Exploring — when you don't know what you're looking for

*The other half of the job. The wishlist exercise was "I know what I want, pin it
down." This one is "I don't know what's out there — show me."*

## Why this half is harder

| | Pinning down | Exploring |
|---|---|---|
| You know the target | yes | no |
| A mistake is | **visible** — the DOI doesn't resolve | **invisible** — you never learn what it missed |
| You can check it by | resolving the DOI | …that's the problem |

**Retrieval fails loudly. Exploration fails silently.**

This is exactly where an agent is most useful *and* least checkable. You cannot
verify completeness from inside the search. What you can do is **triangulate** — and
that's a skill.

---

## The ladder

### Rung 1 · Ask wide

> What is the current state of the argument about statistical significance? What has
> actually happened since 2019 — has the field moved, or is it a stalemate?

Read it as a *map*, not an answer. You're looking for the shape of the terrain: the
camps, the turning points, the vocabulary.

### Rung 2 · Ask for the opposition

> Who argues the thresholds should stay? Give me the strongest version of that case,
> with citations.

An agent asked a leading question returns a literature that agrees with you. Force it
out of a single narrative — deliberately go looking for the people who'd object.

### Rung 3 · Ask the same thing differently

Run your question again in different words — "p-value controversy", "null hypothesis
significance testing critique", "reforming statistical inference". Compare the sets.

**What appears in all three phrasings is probably central. What appears in only one
is either a gem or a distraction — and you have to look to find out which.**

### Rung 4 · The seed check (the one that actually tests coverage)

You already know six papers in this literature — you resolved them this morning.

> Here is a list of papers I already know are central. Which of them did your search
> surface, and which did it miss? Why do you think it missed them?

If a search misses things you *know* should be there, it is missing things you don't
know should be there — **in the same proportion.** That is the closest you will get
to measuring coverage, and it costs one prompt.

This is also the move that transfers: on your own topic, seed it with the three
papers you'd expect any competent reader to name.

### Rung 5 · Follow the citations

> Take the two most central papers. What do they cite, and what cites them since?
> What keeps reappearing that we haven't discussed?

Snowballing. The literature's own structure is more reliable than any search — a
paper everyone cites is central whether or not a search engine likes it.

### Rung 6 · Push it

Two questions that change the answer:

> For each of these — did you read the full text, or only the abstract?

> That was shallow. Go deeper: other phrasings, other databases, books and chapters,
> non-English work, working papers.

Depth is a decision, not a limit. It will usually take the second instruction and
come back with a visibly better map — which tells you the first pass was never the
ceiling.

---

## Then: your own field

The general debate is the demo. The useful version is local:

> What does this argument look like in **my** field specifically? Who are the people
> in [marketing / law / finance / management / economics] making this case, and what
> did they find?

Every discipline has its own version of this fight, with its own culprits and its own
evidence. Find yours — then seed-check it with whoever you'd expect to be there.

---

## What this is actually good at

Do not undersell this half. An agent reads more than you ever will, and it routinely
surfaces work you did not know existed — **including in fields you know well.** That
is not a consolation prize for failing to be a systematic review; it is the point.
Expect at least one "how did I not know about this?" per serious search.

## What it doesn't give you

Not *completeness* — but note that a systematic review doesn't guarantee that either.
What a systematic review gives you is a **protocol**: pre-specified search terms,
named databases, stated inclusion criteria, a documented date. Auditable, and
repeatable by someone else.

> **"Systematic" names a method, not a quality level.** An agent can genuinely find
> more than a systematic search would, and still not be one — because nobody wrote
> down the system.

So don't call twenty minutes of this a systematic review. Not because it found less,
but because you can't hand anyone the recipe.

**Unless you write the recipe down.** Which you can:

> Log what you just did: the exact queries you ran, what you searched, what you
> excluded and why, and today's date. Put it in `search-log.md`.

Same move as yesterday — *write it down so it can be checked*. It doesn't turn a
search into a systematic review, but it turns "I asked an AI" into something you can
defend, repeat, and improve.


## Keep

- Your map: the camps, the turning points, the names that kept reappearing.
- The seed-check result — what it missed, and your guess at why.
- Your `search-log.md`.
- **One thing you found that you did not know existed.** There is almost always one,
  even in your own field. That's the whole reason to do this.
