# Warm-up: move around, then find the edge

*Two short rounds. First you learn to move around — four commands, no agent yet.
Then the fun part: you point the agent at something hard and watch what happens.
Nothing here can break anything; the worst case is you close the window and start
again.*

Keep the terminal cheat sheet (`terminal-cheatsheet.md`) next to you.

> **Two rules for the whole week: don't overthink it — just use it — and when you get
> stuck, ask the tool.** You can't break anything here, and the agent is its own best
> manual.

> **The floor for today: make a file, read it back, delete it.** Ask the agent for it,
> watch it happen, and you have done what this warm-up is for — that is a finished job,
> not a half-done one. The room will spread out a long way over the next three days, and
> that is the design rather than a race.

---

## Round 1 — moving around (no agent yet)

These use only the four commands from the cheat sheet, and they're **the same on
Windows and Mac.** Do them in order — each step tells you how to know it worked.

1. **Open a terminal.** (Cheat sheet → "opening a terminal.") You'll see a
   **prompt**: a line waiting for you, ending in something like `>` or `$`.
2. **Look around:** type `ls` and press Enter.
   → *Worked when:* you see a list of names — the files and folders here.
3. **Make a sandbox:** `mkdir practice`
   Nothing dramatic happens — that's normal. Run `ls` again; `practice` is in the list now.
4. **Go inside:** `cd practice`, then `ls`.
   → *Worked when:* `ls` prints nothing. The folder is empty, and you're now in it.
5. **Meet Tab, your best friend:** `cd ..` to step back out. Now type `cd pra` and
   press **Tab** — watch it finish the word for you. Press Enter.
   → *Worked when:* you're back inside `practice` without typing the whole name.
   (Use Tab *always*: it also handles spaces and catches typos.)
6. **Build a little structure:** inside `practice`, run `mkdir notes` then
   `mkdir drafts`. `ls` shows both. Step into one — `cd notes`, `ls` (empty) — then
   `cd ..` back out.
7. **"Where am I?":** type `pwd`. It prints exactly where you're standing — your
   *you-are-here* whenever you feel lost.
8. **The escape hatch:** if anything ever looks stuck, press **Ctrl+C**. Truly stuck?
   Close the window and open a new one. You cannot break anything from in here.

> **That's the whole terminal.** There are hundreds of other commands — and you don't
> need a single one of them. The agent knows them all and runs them for you; these
> four just get you *to* the agent and back.

---

## Round 2 — experiments: find the edge · ⬅ the floor

Now start the agent and *play.* You saw this morning what these can do — go find out
for yourself. This is a playground, not a test: poke it, be surprised, and notice
where you stop trusting it.

**Start it:** from inside your `practice` folder, type `claude` (or `codex`) and press
Enter. Say hello: *"What can you help me with here?"*

Now ask it for the floor: make a file, read it back to you, delete it again. **That's the
bar for the whole warm-up, and you've cleared it** — everything below is yours to take as
far as you like, and if you got there while your neighbour is still hunting for the
prompt, go and be the one who finds it: whoever finishes first is the room's help desk,
and that holds all three days.

Then try a few — pick whatever tempts you:

- **Something from your own field.** Ask the question you'd assume needs a specialist.
  *Finance:* "price a European call with these numbers, and show the code." *Law:*
  "sketch the strongest counterargument to this clause." *Any field:* "turn this survey
  into three customer segments and name them." See how far it gets.
- **Watch it actually build something.** "Make a small table from these messy notes."
  "Write a little program that does X, and run it." It doesn't just *describe* — it does.
- **Try to catch it out.** Ask something you suspect it'll get wrong — a very recent
  event, an obscure figure, a specific citation — then **check the answer.** Did it
  hedge honestly, or make something up? *This is the habit the whole course is about.*
- **Be vague on purpose.** Give it something under-specified — "make me something useful
  for my course." Notice whether it asks you questions or just charges ahead, and that
  *you* are the one steering.
- **Use your voice.** If speech-to-text is set up, dictate a request instead of typing it.

**Before you move on, write down two things:**

- one answer that genuinely **surprised** you, and
- one answer you did **not trust** — and why.

> Surprise and suspicion are both correct reactions. Holding them at the same time is
> the whole skill.
