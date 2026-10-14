# The terminal, on one page

**Four commands, two keys. Everything else, you ask the AI to do for you.**

You are not expected to memorise any of this — that's what this paper is for. The
good news: these commands are the *same* on Windows, Mac, and Linux. And there are
*hundreds* of other terminal commands — you can safely ignore them, because the agent
knows them all and runs them for you.

---

## The four commands

| Type this | And it… |
|---|---|
| `cd foldername` | moves **into** a folder (*change directory*). Use `cd ..` to step back out one level. |
| `ls` | **lists** what's in this folder *(on Windows, `dir` also works)* |
| `mkdir projectname` | **makes** a new folder |
| `claude`  *or*  `codex` | **starts the AI agent**, right here |

## The two keys that save you

- **Tab** — autocomplete. Type the first few letters of a name and press **Tab**; it
  finishes it for you. Use it every single time: it kills typos and handles spaces in
  folder names so you never have to think about them.
- **Ctrl + C** — stop. Halts whatever is running. Press it twice (or type `/exit`) to
  leave the agent and get your ordinary prompt back.

---

## Start a fresh project — the whole thing

```
cd Desktop            # go somewhere you'll find again
mkdir my-project      # make a home for it
cd my-project         # step inside
claude                # start the agent   (or: codex)
```

Then just talk to it:

> What files are here? Don't change anything yet — just tell me what you see.

---

## Opening a terminal *already in the right folder*

- **Windows:** open the folder in File Explorer, click the **address bar**, type
  `powershell`, and press **Enter**. The terminal opens right in that folder.
- **Mac:** right-click the folder → **New Terminal at Folder**. (Or open Terminal and
  drag the folder onto its window.)

## If you feel lost

- Not sure where you are? Type `pwd` — it prints the folder you're standing in.
- Everything looks wrong? **Close the window and open a new one.** Nothing breaks, and
  you can always start over.
- Unsure about *anything else* — a command, what the agent can do, what just happened?
  **Just ask the agent.** It's your best manual, and asking is the habit that matters most.
