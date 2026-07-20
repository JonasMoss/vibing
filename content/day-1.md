## Today’s finish line

Before we leave, you will have pointed an AI agent at a real folder, asked it to
understand the mess, changed its proposed plan, and watched it carry out the
work.

No previous terminal experience is assumed.

## Morning — first contact

### 10:00 · See the whole thing

We begin with a short live demonstration: a chaotic course folder goes in; a
clean, documented project comes out. Do not worry about how each step works yet.
First, see the shape of the possibility.

### 10:30 · Find your feet

Open a terminal. Move into a folder. Start Claude Code or Codex. Ask:

> What files can you see here? Do not change anything.

That small exchange contains most of the technical foundation we need.

### 11:00 · Tiny, harmless jobs

Ask the agent to create a Markdown file, inspect it, revise it, and remove it.
Try speaking your instructions instead of typing them.

**Useful failure is welcome:** if something breaks, ask the agent what happened
and what it wants to try next.

## Afternoon — decrap a folder

You will receive the same deliberately awful folder as everyone else:
duplicates, mystery names, old exams, stray images, and several competing
versions of “final”.

Work through this loop:

1. **Inspect:** “Describe what is here. Do not change anything.”
2. **Plan:** “Propose a sensible structure and explain your choices.”
3. **Disagree:** Change at least one part of the plan.
4. **Act:** Let the agent carry it out.
5. **Check:** Open the result and inspect a few files.
6. **Document:** Ask for a short `README.md` explaining the new structure.

## The two-minute terminal kit

You only need a handful of moves today:

| Intent | Windows PowerShell | macOS / Linux |
|---|---|---|
| Show this folder | `pwd` | `pwd` |
| List what is here | `dir` | `ls` |
| Enter a folder | `cd folder-name` | `cd folder-name` |
| Go back one level | `cd ..` | `cd ..` |
| Stop a running command | `Ctrl+C` | `Ctrl+C` |

Tab completes names. The up arrow recalls your previous command. When unsure,
ask the agent.

## Before you leave

- Keep the cleaned folder.
- Keep the `README.md`.
- Write down one instruction that worked surprisingly well.
- Write down one thing you did not trust.

Tomorrow we take the same inspect–plan–act–check loop into research.

