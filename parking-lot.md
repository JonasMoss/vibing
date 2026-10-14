# Parking lot — undecided, revisit later

Genuine open questions flagged during development, *not* decided yet. These are **not**
TODOs — build tasks live in each course's README. Park an idea here instead of deciding
it prematurely; promote it into the plan once you've made the call, or delete it if it
stops mattering.

## Course content

- **Compact the expanded capabilities deck.** Epoch is now the recommended
  benchmark landing page, with an index plot, Astra's verified FrontierMath
  comparison, and benchmark-error examples integrated. Navier–Stokes and two
  Mollick demonstrations are also in. Decide which older exhibits to compress
  when doing the deferred prose pass. Evidence and author priorities:
  `scratch/research/capabilities-review-2026-09-20.md`.

- **Teach `/init`, or not?** `/init` auto-generates a `CLAUDE.md` / `AGENTS.md` by
  reading the project. Leaning: teach the *concept* (a file the agent reads every
  session), not the command — "just ask it to set up a CLAUDE.md" needs nothing
  memorised. Keep `/init` as an optional shortcut for people who like it.
- **Where the `AGENTS.md` / `CLAUDE.md` lesson lands.** Currently slotted Day 3 morning.
  Leaning: keep it late — you make things repeatable *after* you've felt the friction of
  doing them once, not before.
- **How deep to go on context / compaction.** Decided for now: one reflex only ("fresh
  chat when it drifts"); the rest is a later course. Revisit if a room wants more.

- **A downloadable paper-organising skill for participants.** Agents are very good
  at restructuring a paper folder (cf. the private `paper-init` / `cleanup-paper`
  skills), and a published skill people could install in one step would make the
  "reproducible project" block much stronger. Overkill before the October department
  sessions; revisit after them. The repo's own `tidy-project` skill is the light
  version that already exists.

## Repo / distribution

- **Where props live now that the site is gone.** The decrap folder and the other
  zips used to be served from vibing.jonasmoss.com. Options: GitHub links into
  the course's `props/` folder (public repo, written into the handout so people
  copy the link into the agent), a file handed out in the room, or any other
  host. Decide per course; the decrap folder is staying either way. **Finance
  uses GitHub links** (`.../raw/main/courses/2026-10-finance/props/...`), which
  only work once the course is merged to `main` and pushed.
- **Commit rendered HTML on every change, or only at freeze?** Each embedded deck
  is about 3.5 MB (12 decks ≈ 45 MB per full render). Git deltas absorb most of
  it, but if the repo gets heavy, switch to committing HTML only when a course is
  held.
- **The two Twitter screenshots in `scratch/slides/images/` are public in the
  repo** (`gowers-2030.png`, `jacobian-tweet.png`), as is `scratch/research/`.
  Keep them, or move them to `private/`? Undecided.
