# One source, one screen, one link

**Day 3, afternoon.** Files: `examples/lecture-notes/`

You have spent two days getting text into a shape a machine can work with. This block
is where that pays off in public: rough notes go in, a slide deck comes out, and — if
you want it — a link your students can open tonight.

> **The idea in one line:** one plain-text source, one rendered artifact, one URL. Fix
> the source once; everything downstream updates.

| | The usual way | This way |
|---|---|---|
| **Slides** | PowerPoint; the content lives inside the design | text; the design is a setting you change in one line |
| **Course page** | email an attachment, then email it again | a link that is always current |

The point is **not** Quarto. Quarto is one renderer and you will meet another one in
ten minutes. The point is the shape: *source → render → publish*, with the agent doing
every awkward step in between.

> **The floor: Rung 1 — rough notes in, and a deck you actually rendered, opened, looked
> at, and changed once by talking to it.** Either route there counts, install or no
> install; clear it and this block has done its job for you. GitHub and Pages, from Rung
> 2 on, are for whoever wants them — and the room will end up in very different places
> this afternoon, which is the design and not a race.

---

## First, ten minutes on GitHub

Before the rungs, we do accounts, one repository, and what GitHub Pages is. Read
`handouts/github.md` — the non-technical version, "a safe copy in the sky" — and don't
try to memorise anything. You will not type a git command today.

If you already have an account: help the person next to you. It is the single biggest
time sink of the day and it goes much faster in pairs.

---

## What you are working from

**Your own lecture notes, if you can get to them.** You brought nothing — fine. Notes
live in email, in OneDrive, in a Word file called `lecture6_v2_FINAL.docx`, in a
PowerPoint from 2021, or in your head. Any of those work:

> I'm going to give you the notes for one lecture. They're a mess and that's fine.

Then paste them, drop the file in the folder, or dictate the outline out loud and let
speech-to-text do the typing.

**Fallback:** `examples/lecture-notes/motivation-at-work.md` — a real-shaped set of
messy notes for a bachelor Organisational Behaviour lecture. Fragments, inconsistent
headings, four unresolved `TODO`s and a couple of half-remembered citations. Use it and
lose nothing.

---

## Rung 0 · Make the agent fix its own environment

Rendering slides needs a renderer, and you don't have one. Good — this is the most
useful thing you will watch all afternoon.

> Install Quarto on this machine so I can render slide decks. I'm on Windows and I may
> not have admin rights. Try what you can. When you're done, prove it works by
> rendering a one-slide test file. If you get stuck, stop and tell me exactly what
> blocked you and what my options are.

Then **watch the terminal**. It will work out which operating system it is on, try
`winget`, notice when Windows demands an administrator password it isn't going to get,
back off, and go looking for a way in that doesn't need one — the per-user installer,
or the portable zip that is just a folder you unzip and point at. Then it checks
whether the new command is actually reachable, and fixes the `PATH` if it isn't.

That is not a script. That is something reading an error message, forming a theory, and
trying the next thing. **This is the capability, not the preamble to it.** The install
is a genuine, boring, hostile little problem — exactly the kind that has stopped you
adopting a tool before — and you just delegated it.

*Do this the same way when you get back to your office.* "Install X, and if you can't,
tell me why" is a complete instruction. You no longer need to be the person who reads
the installation page.

**If it succeeds**, you have `quarto`. Go to Rung 1.

**If it fails** — managed laptop, locked-down policy, IT says no — you have lost
nothing at all. Read on.

---

## Rung 0b · The no-install path (and it is not a consolation prize)

Every browser on earth already knows how to display a slide deck. It just needs the
file.

> Quarto won't install. Instead, build my slides as a single self-contained HTML file
> that loads reveal.js from a CDN. One file, no installation, opens in any browser.
> Use my notes in `motivation-at-work.md`.

You get **one `.html` file**. Double-click it. It's a full presentation: arrow keys or
space to move, `Esc` or `O` for the overview grid, `F` for fullscreen, `S` for a
speaker-notes window with a timer and your next slide, `B` to black the screen when you
want the room looking at you instead.

*If you get a blank white page*, nothing is broken that a sentence won't fix — the deck
loaded a newer reveal.js than the rest of the file expected. Don't go hunting:

> The deck opens as a blank white page. Check the browser console, find the error, and
> fix it.

Two things worth knowing, because they are advantages and not apologies:

- **It publishes to GitHub Pages as-is.** It is already a web page. There is no build
  step to get wrong, nothing to render on the day, no `_files` folder to lose. Rung 2
  is *easier* from here, not harder.
- **A PDF is one question away.** Add `?print-pdf` to the end of the address in your
  browser and print to PDF, or just ask:

  > Give me a PDF of this deck for the students.

The one thing to actually do something about: loading reveal.js from a CDN means the
file wants internet the first time it opens. Lecture halls have opinions about wifi. So
before you present:

> Make this deck work with no internet — put reveal.js next to the file instead of
> loading it from the web.

Now it's a folder you can carry on a USB stick into a basement. (Quarto's equivalent is
one line, `embed-resources: true`, which packs the whole deck into a single file.)

---

## Rung 1 · Notes → deck → argue with it (everyone) · ⬅ the floor

Save point first, always:

> Commit this before we start.

Then:

> Turn these lecture notes into a slide deck. It's a 45-minute bachelor lecture. Put
> the detail in the speaker notes, not on the slides.

Render it, **open it**, and look. It will be roughly right and specifically wrong. Good
— the first version was never the deliverable. The deliverable is what you do next, and
what you do next is *talk*:

> More slides, less on each one.

> Bigger font. I'm in a lecture hall, not a meeting room.

> Slide 6 is a wall of text. Split it and move the explanation into the notes.

> One joke per section. Nothing about deans.

> Add a five-minute pair exercise after the goal-setting section. Write the
> instructions so they work without me in the room.

> Build the title slide from the course code and my name, and use the same theme
> throughout.

Re-render after each round and look again. Thirty seconds a cycle. This is the whole
skill: **you are editing by describing, and checking with your eyes.**

Then ask it something it can answer better than you can:

> What did my notes promise to cover that the slides don't actually cover?

> Which slide is doing the least work?

*Stuck?* If nothing renders, do not debug it yourself:

> That didn't render. Read the error, fix it, and try again.

**That's the floor: a deck you rendered, opened, looked at, and changed by talking to
it.** Rung 2 puts it on the internet — or if you're done and the person next to you
isn't, go and help them: whoever finishes first is the room's help desk, and that holds
all three days.

---

## Rung 2 · Put it where students can see it (ambitious)

The mechanics are in `handouts/github.md`. In practice you ask for the outcome and let
the agent do the plumbing:

> Put this on GitHub and publish it with GitHub Pages, then give me the link.

> Write a one-page course site: what the course is, when we meet, the reading list, and
> a link to the slides. Same look as the deck.

> Check every link on that page actually resolves.

Two decisions are yours, and the agent should not make them for you:

- **Public or private.** Pages needs a public repository unless you pay. If the deck
  contains exam material, student names, or half-formed opinions about colleagues,
  decide that *now*, not after you push. (`handouts/github.md`, "two honest cautions".)
- **Whose material is it.** Figures from a textbook do not become yours by being
  rendered nicely.

Then update something small — a date, a typo — and ask:

> Push the change.

Refresh the page. That loop, which took a minute, is the thing that makes a course page
survive contact with a semester. It is why nobody ever emails you `syllabus_v4_final`
again.

---

## Rung 3 · For the bold

Both of the above, plus yesterday's work:

> Take the verified reference list from Tuesday and add it to the site as its own page.
> Group it by theme, link every DOI, and mark which ones are open access.

> Make a printable one-page handout from the deck, and check it agrees with the slides
> on every claim.

> Write a `README.md` in this folder explaining what's here and how I update it in
> January when I've forgotten all of this.

That last one is not busywork. It is the message you leave for the version of you who
comes back to this in five months.

---

## One honest caveat

A rendered deck looks finished. That is exactly the problem.

The agent optimises for **filling slides** — every bullet in your notes finds a home,
every section gets its screen, and the result is handsome, complete, and possibly
saying nothing. It has no way to know that slides 7 through 11 are all one idea, or
that the argument you actually care about is the half-sentence you scribbled in
brackets.

> **"One argument per screen" is a judgement, and it is yours.**

The move, after every render: click through it once at presentation speed and ask
yourself what each slide is *for*. Then say so out loud —

> These four slides are one idea. Make them one slide and put the rest in the notes.

You will do this three or four times per deck. It takes two minutes and it is the
entire difference between a deck that was generated and a lecture that was designed.

## Keep

- The source file — the `.qmd`, or the single `.html`, or both.
- The link, if you got one. Send it to someone before you leave the room.
- One slide you rewrote by hand after looking at it. That's the one that proves you
  were driving.

## Worth reading

Nothing long. These are the four pages you'll actually want open later.

- **Quarto — Get Started** — the install page, including the Windows `.msi` and the
  portable `.zip` that need no administrator. <https://quarto.org/docs/get-started/>
- **Quarto — Revealjs presentations** — every option you might want to ask for
  (themes, columns, incremental bullets, speaker notes), so you know what to name.
  <https://quarto.org/docs/presentations/revealjs/>
- **reveal.js** — the presentation engine underneath both routes. Its own site is a
  deck, which tells you most of what you need to know. <https://revealjs.com/>
- **GitHub Pages quickstart** — the ten-minute version of what we did in Rung 2.
  <https://docs.github.com/en/pages/quickstart>
