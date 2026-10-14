# Installing your AI terminal assistant

*Day 1, 10:00. We do this together, in the room. It takes about 10 minutes when
it goes well — and when it doesn't, that's what the rest of the morning is for.
**Nobody is behind.** Everyone in here is starting from the same place.*

> **Start the download now, then close the lid and look up.** The install runs by
> itself while we do the opening talk. You'll come back to a finished download
> instead of twenty of us fighting for the same wifi at once.

**If you finish early, you have a job:** get your neighbour running. That's not
a chore, it's the fastest way to make this room work — and you'll learn more
debugging someone else's laptop than watching your own succeed.

---

## What you need

1. **A paid AI subscription.** Pick the tool that matches what you
   already pay for — you only need **one**:

   | If you pay for…                     | …install        |
   |-------------------------------------|-----------------|
   | **Claude** (Pro or Max)             | **Claude Code** |
   | **ChatGPT** (Plus, Pro, Business, Edu, Enterprise) | **Codex** |

   Free plans do **not** work for either tool. **No subscription?** Don't sit
   this out — pair up with the person next to you for today and sort a
   subscription tonight (a single month of Claude Pro or ChatGPT Plus is
   plenty). Two people on one laptop works fine, and arguing about the prompt
   with someone else is genuinely a better way to learn this.

2. **A Windows 11 laptop.** (On a Mac? Jump to [the macOS section](#macos).)

3. **No admin rights required.** Both installers put everything in your
   own user folder. If your laptop is managed by BI IT, this should still
   work — see [Troubleshooting](#if-something-goes-wrong) if it doesn't.
   The one exception is **Git** ([Step 5](#git)),
   which is recommended but not required.

> **You do not need to understand any of this.** Copy, paste, press
> Enter. That's the whole job. The terminal looks scary and is not.

---

## Step 1 — Open PowerShell

PowerShell is the blue/black text window we'll live in for three days.

1. Click the **Start** menu (Windows logo, bottom-left).
2. Type `powershell`.
3. Click **Windows PowerShell**.
   ⚠️ **Not** the one ending in **(x86)** — that one won't work.

A window opens with a line that looks like this:

```
PS C:\Users\YourName>
```

That `PS` at the start tells you you're in the right place. The blinking
cursor is waiting for you. 

> **Pasting tip:** to paste a copied command into PowerShell,
> **right-click** anywhere in the window (or press **Ctrl+V**). Then press
> **Enter** to run it.

---

## Step 2 — Install your tool

Do **one** of the two following sections — whichever matches your
subscription.

### Option A — Claude Code (for Claude subscribers)

Copy this line, paste it into PowerShell, press **Enter**:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Wait 1–3 minutes while it downloads. When the prompt (`PS C:\...>`)
comes back, it's done.

**Now close PowerShell completely and open it again** (Step 1). This is
important — it lets Windows notice the new program.

Check it worked:

```powershell
claude --version
```

If you see a version number (like `2.x.x`), you're installed. 🎉

### Option B — Codex (for ChatGPT subscribers)

Copy this line, paste it into PowerShell, press **Enter**:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Wait 1–3 minutes. When the prompt comes back, it's done.

**Now close PowerShell completely and open it again** (Step 1).

Check it worked:

```powershell
codex --version
```

A version number means you're installed. 🎉

---

## Step 3 — Log in

The first time you run the tool, it sends you to your browser to log in.
You only do this once.

**Claude Code** — type:

```powershell
claude
```

Your browser opens. Log in with your **Claude** account (the one your
Pro/Max subscription is on), approve the access, then return to
PowerShell.

**Codex** — type:

```powershell
codex
```

Choose **Sign in with ChatGPT**, log in in the browser, then return to
PowerShell.

---

## Step 4 — The "did it really work?" test

With the tool running (after Step 3), just **type a sentence and press
Enter**, like:

```
what files are in this folder?
```

If it answers you in plain English, **you are completely done.** 🎉

To quit the tool, type `/exit` (or press **Ctrl+C** twice).

**Now go help your neighbour** — and grab the warm-up sheet while you wait for
the rest of us.

---

<a name="git"></a>
## Step 5 — Install Git (recommended)

Git gives the agent save points: before it reorganises a folder, it saves a
snapshot you can always go back to. You never type git commands yourself; you ask
the agent. Everything else works without Git, so if this step fails, carry on.

**Windows.** In PowerShell (quit Claude Code or Codex first with `/exit`):

```powershell
winget install --id Git.Git -e --source winget
```

Windows asks whether to allow the app to make changes: click **Yes**. This is the
one step that needs administrator rights.

**Now close PowerShell completely and open it again**, then check:

```powershell
git --version
```

A version number (like `git version 2.x`) means you're done.

- **Can't click Yes (no admin rights)?** Ask BI IT to install **Git for Windows**
  for you. Don't lose time on it; you can do everything else without it.
- **`winget` not recognized?** Download the installer from
  <https://git-scm.com/downloads/win>, run it and click **Next** on every screen.
  The defaults are fine.
- **Claude Code users:** once Git is installed, Claude Code uses it automatically
  the next time you start `claude`.

**Mac.** In Terminal:

```bash
git --version
```

If you see a version number, you already have Git. If not, your Mac offers to
install the **command line developer tools**: click **Install** and wait a few
minutes, then run `git --version` again. (If you installed Homebrew for Codex, you
already have Git.)

---

<a name="if-something-goes-wrong"></a>
## If something goes wrong

Work down this list — the first two fix almost everything.

**`claude` / `codex` is not recognized**
You probably skipped the "close and reopen PowerShell" step. Close the
window, open a fresh PowerShell, try again. Still failing? Re-run the
install command from Step 2 and watch for any red error text.

**Claude Code: ask the tool to diagnose itself**
```powershell
claude doctor
```
Prints a read-only health check of the installation and settings, with suggested
fixes. Try this before anything else below — it often names the problem outright.

**`git` is not recognized** (after Step 5)
Same fix: close PowerShell, open a fresh one, try again. If it still fails,
restart the laptop once.

**`irm` is not recognized** (or the command looks wrong)
You're in the *Command Prompt*, not *PowerShell*. They look similar.
Close it and reopen **Windows PowerShell** via Step 1.

**The download fails, hangs, or says it's blocked**
This is almost always BI's network or security software, not you.
Forward this to IT and ask them to allow it:
> *"Please allow access to `claude.ai` and `downloads.claude.ai`
> (for Claude Code), or `chatgpt.com` and `releases.openai.com` (for Codex), and
> allowlist the `claude.exe` / `codex.exe` programs in my user folder."*
Put your hand up — this is one for the instructor, not for you to fight alone.

**Claude Code: try the Windows package manager instead**
If the script install is blocked but WinGet isn't, this often walks straight
through:
```powershell
winget install Anthropic.ClaudeCode
```
(It doesn't auto-update, which doesn't matter for three days.)

**Codex asks for administrator approval / a "sandbox"**
If a Windows admin prompt (UAC) appears and you can't approve it,
choose the option to continue **without** elevated setup (the
"unelevated" mode). Codex still works fine for our course.

**It says I need a paid plan / login fails**
Double-check your subscription is active and you're logging in with the
*same* account it's on. Free Claude.ai / free ChatGPT accounts can't run
these tools.

> Still stuck after all this? **Stop, and put your hand up.** The whole morning
> is built for exactly this. Worst case you pair with a neighbour for today and
> we fix your machine over lunch — you will not miss anything that matters.

---

## Optional fallback: install via npm

*Only if the native installer above failed and you happen to already have
**Node.js** installed.* Most people should ignore this section.

```powershell
# Claude Code (needs Node.js 22+)
npm install -g @anthropic-ai/claude-code

# Codex (Node.js 22 recommended)
npm install -g @openai/codex
```

⚠️ The package name for Codex is **`@openai/codex`** — the plain `codex` on npm
is an unrelated project from 2012.

Then continue from **Step 3 (Log in)**. Do **not** put `sudo` in front of
these commands.

---

<a name="macos"></a>
## On a Mac instead?

Open **Terminal** (press **Cmd+Space**, type `terminal`, press Enter),
then run **one** of these:

```bash
# Claude Code (for Claude subscribers)
curl -fsSL https://claude.ai/install.sh | bash

# Codex (for ChatGPT subscribers) — needs Homebrew (brew.sh)
brew install --cask codex
```

Then follow **Step 3 (Log in)** and **Step 4** above — the `claude` /
`codex` commands are identical on a Mac. For Git, see the Mac part of
[Step 5](#git).

---

## Official docs (if you like reading the source)

- Claude Code setup: <https://code.claude.com/docs/en/setup>
- Claude Code install troubleshooting: <https://code.claude.com/docs/en/troubleshoot-install>
- Codex docs: <https://learn.chatgpt.com/docs>

*Re-verified 9 August 2026, three days before the course: both PowerShell install
URLs fetched and confirmed live (`claude.ai/install.ps1` → `downloads.claude.ai`,
`chatgpt.com/codex/install.ps1` → `releases.openai.com`), and npm engine
requirements read off the published packages. The old
`developers.openai.com/codex/*` links now redirect to `learn.chatgpt.com` and
have been replaced.*
