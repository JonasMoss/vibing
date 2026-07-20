# Installing your AI terminal assistant

*Pre-course handout — please do this **before** Day 1. It takes about
10 minutes. If you get stuck, don't worry: we have a setup clinic the
first morning. But the more of you who arrive already working, the more
time we spend on the fun part.*

---

## What you need

1. **A paid AI subscription.** Pick the tool that matches what you
   already pay for — you only need **one**:

   | If you pay for…                     | …install        |
   |-------------------------------------|-----------------|
   | **Claude** (Pro or Max)             | **Claude Code** |
   | **ChatGPT** (Plus, Pro, Business, Edu, Enterprise) | **Codex** |

   Free plans do **not** work for either tool. If you have neither
   subscription, get one before the course (a single month of Claude Pro
   or ChatGPT Plus is plenty).

2. **A Windows 11 laptop.** (On a Mac? Jump to [the macOS section](#macos).)

3. **No admin rights required.** Both installers put everything in your
   own user folder. If your laptop is managed by BI IT, this should still
   work — see [Troubleshooting](#if-something-goes-wrong) if it doesn't.

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

If it answers you in plain English, **you are completely done.** Close
the window; we'll start here together on Day 1.

To quit the tool, type `/exit` (or press **Ctrl+C** twice).

---

## If something goes wrong

Work down this list — the first two fix almost everything.

**`claude` / `codex` is not recognized**
You probably skipped the "close and reopen PowerShell" step. Close the
window, open a fresh PowerShell, try again. Still failing? Re-run the
install command from Step 2 and watch for any red error text.

**`irm` is not recognized** (or the command looks wrong)
You're in the *Command Prompt*, not *PowerShell*. They look similar.
Close it and reopen **Windows PowerShell** via Step 1.

**The download fails, hangs, or says it's blocked**
This is almost always BI's network or security software, not you.
Forward this to IT and ask them to allow it:
> *"Please allow access to `claude.ai` and `downloads.claude.ai`
> (for Claude Code), or `chatgpt.com` (for Codex), and allowlist the
> `claude.exe` / `codex.exe` programs in my user folder."*
Then bring your laptop to the Day 1 setup clinic and we'll finish it.

**Codex asks for administrator approval / a "sandbox"**
If a Windows admin prompt (UAC) appears and you can't approve it,
choose the option to continue **without** elevated setup (the
"unelevated" mode). Codex still works fine for our course.

**It says I need a paid plan / login fails**
Double-check your subscription is active and you're logging in with the
*same* account it's on. Free Claude.ai / free ChatGPT accounts can't run
these tools.

> Still stuck after all this? **Stop.** Bring your laptop on Day 1 — the
> first morning is built for exactly this. You won't be behind.

---

## Optional fallback: install via npm

*Only if the native installer above failed and you happen to already have
**Node.js** installed.* Most people should ignore this section.

```powershell
# Claude Code (needs Node.js 18+)
npm install -g @anthropic-ai/claude-code

# Codex (needs Node.js 22+)
npm install -g @openai/codex
```

Then continue from **Step 3 (Log in)**. Do **not** put `sudo` in front of
these commands.

---

<a name="macos"></a>
## On a Mac instead?

Open **Terminal** (press **Cmd+Space**, type `terminal`, press Enter),
then run **one** of these:

```bash
# Claude Code (for Claude subscribers)
curl -fsSL https://claude.ai/install.sh | sh

# Codex (for ChatGPT subscribers) — needs Homebrew (brew.sh)
brew install --cask codex
```

Then follow **Step 3 (Log in)** and **Step 4** above — the `claude` /
`codex` commands are identical on a Mac.

---

## Official docs (if you like reading the source)

- Claude Code setup: <https://code.claude.com/docs/en/setup>
- Codex CLI: <https://developers.openai.com/codex/cli>
- Codex on Windows: <https://developers.openai.com/codex/windows>

*Verified against the official docs, June 2026.*
