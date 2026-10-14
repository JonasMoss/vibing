# Building a reference library your agent can trust

*Day 2 handout. By the end you can say "get me these papers" and your agent
fetches them, notes what each one is, and hands you a tidy list of DOIs for the
ones it couldn't — and you'll have turned that whole routine into a reusable
**skill**. No file formats to memorise.*

> **The floor: turn a wishlist into real citations with verified DOIs, and catch one
> thing that is wrong.** That is the day's actual skill, and stopping there is a complete
> run — the reusable `gather-refs` skill below is for whoever wants it. People will get
> to very different places in this block, which is how it was built rather than a race.

---

## Why this block exists

Fabricated citations are in the published literature right now. An audit of
**2.5 million biomedical papers** checked 97 million references and found
fabrications in **1 paper in 277** in early 2026 — up from 1 in 2,828 in 2023.[^1]
Closer to home: a paper in *Structural Equation Modeling* cites a method
attributed to a colleague of mine that **does not exist**.

Now the part that matters, and it cuts the other way from what you'd expect:

> **The models got better. The practice didn't.**

A current model *with search enabled* does not invent a DOI. Its honest failure
modes are now different — it hands you the *wrong* paper, or it fails to fetch
one — and **both take seconds to catch.** The rise isn't frontier models getting
worse. It's people prompting from memory, on a free tier, and pasting the result
without looking.

Which makes this block the answer rather than the warning. In the next hour you
will catch fabrications yourself, in a real literature, using checks that cost one
prompt each. After that, "I didn't have time to verify" stops being true.

[^1]: Topaz et al. (2026), "Fabricated citations: an audit across 2·5 million
biomedical papers," *The Lancet*, 1779–1781. A Letter, not a study — and its
methodology has been questioned, which is itself worth noticing in a handout about
citing carefully.

---

## First, a 30-second recap

You met these in the "plain text and git" bit. Here they are again, together:

| Thing | What it is |
|---|---|
| **`.bib`** | A bibliography stored as plain text — one block per paper. Diffable, durable, boring in the best way. |
| **`.qmd`** | A Quarto document: prose, code, and citations in a single readable text file. |
| **git** | A save button with history — every change recoverable. |
| **`.gitignore`** | A short list that tells git *"don't track these files."* We'll use it for PDFs. |

> You don't need to understand these deeply. You need to know they are **text** —
> and text is what these tools, and git, handle beautifully.

---

## Two jobs, one folder

Managing references is really two tasks, and your agent is good at both:

1. **Gather what you need** — find and pull in papers you don't have yet.
2. **Clean what you have** — fix a messy, error-riddled bibliography.

We'll do the first as the worked example, because it shows off skills, plain
text, and git all at once.

---

## The gather workflow · ⬅ the floor

Open your project folder in Claude Code or Codex and paste something like this
(swap in your own wishlist at the end):

> Build a small reference library in this folder. For each paper I list:
> 1. Identify the real paper — title, authors, year, DOI. If you can't confirm it
>    exists, tell me; never invent a citation.
> 2. If an open-access PDF exists (arXiv, publisher OA), download it into
>    `references/pdf/`, and make sure that folder is in `.gitignore`.
> 3. Write a 1–2 sentence note on what it's about in `references/notes.md`.
> 4. Add a verified BibTeX entry to `references.bib`.
> 5. For anything you can't download, add its title, authors, and **DOI** to
>    `references/to-fetch.md`, so I can get it through the library.
>
> Then tell me: how many you added, and how many I need to fetch myself.
>
> Here's my list: *[your papers or topic here]*

That's the whole trick. The agent does the finding, reading, noting, and
BibTeX-ing; you get back a working library and a short shopping list of DOIs.

**The floor isn't the list — it's the list you checked.** So do that now, here, before
anything else. It takes two minutes:

> Take three of those DOIs. Open <https://doi.org> and paste each one in. Does it
> resolve — and does it resolve to **the paper the entry claims**, same title, same
> authors, same year?

At least one will be off. That is not the agent failing; this literature is genuinely
a minefield, and finding the crack yourself is the entire point of the morning.

**That's the floor cleared.** Everything below — the reusable skill, the gitignore
rules, the paywall rule — is yours to take as far as you like. (The fuller checklist
is "Verify before you trust" at the bottom, when you want it.) And if you're done
while the person next to you isn't, go and help them: whoever finishes first is the
room's help desk, and that holds all three days.

---

## Now make it a skill

First, the honest disclaimer: **you don't need skills to get things done.** Almost
everything in this course works with plain conversation. Skills are just for the
handful of routines you catch yourself repeating — a way to stop re-explaining
yourself.

Here's the idea. With a colleague you'd say *"do it like last time"* — they
remember. An AI has some memory too, but for a routine you want to come out
**identical every time, and be shareable**, memory is the wrong tool. It's why
surgeons and pilots use checklists even though they haven't forgotten anything.

> **Memory is the AI remembering you. A skill is you writing it down** — so it
> happens the same way every time, and so you can hand it to a colleague.

So once the gather workflow above works, tell your agent:

> Turn the workflow above into a skill called `gather-refs`.

Claude Code writes a `SKILL.md`; Codex does its equivalent. **You never touch the
file format** — that's the whole point. From now on, *"gather refs for my paper
on X"* triggers the entire routine, the same way every time.

> A skill is just a saved workflow with a name and a one-line note about when to
> use it. If you can describe a routine, you can make it one — but only bother for
> the ones you actually repeat.

---

## What git keeps, what it ignores

This example quietly teaches the most useful git habit there is:

| Track it (commit) | Ignore it (`.gitignore`) |
|---|---|
| `references.bib` — text | `references/pdf/` — the PDFs |
| `references/notes.md` — text | (binary, large, copyrighted) |
| `references/to-fetch.md` — text | |

The line the skill adds to `.gitignore` is simply:

```
references/pdf/
```

**The lesson in one sentence:** track the text you *wrote*; ignore the big binary
files you merely *downloaded*. Your repository stays small, legal, and readable.

---

## The paywall rule (and why it's the *right* answer)

Notice what the agent does **not** do: it won't bypass paywalls or pull from
pirate sites. For anything it can't get openly, it hands you the **DOI** and lets
*you* fetch it through BI's library access.

That's not a limitation to apologise for — it's the honest, correct workflow. The
agent knows its limits and routes cleanly around them, and you stay on the right
side of copyright. (We come back to "using these tools correctly" on Day 3.)

---

## Verify before you trust

A reference library is only useful if it's true. Before you lean on it:

- Open `references/to-fetch.md` — each DOI should resolve to a real paper at
  <https://doi.org>. Spot-check one or two.
- Skim `references.bib` — do the entries match the notes?
- Pick one paper you know well and check the note didn't overstate it.

> A polished bibliography is not evidence of a correct bibliography.
