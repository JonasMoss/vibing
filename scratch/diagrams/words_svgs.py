"""Diagrams for the Strategy course's 'Words you've heard' deck.

Writes six SVGs into courses/2026-10-strategy/decks/images/. Deck palette:
ink #17201f, muted #5c6763, coral #f0674d, coral-dark #b8432d, deep #e8e0d3,
white #fffdf8, coral-light #fbd9d1, rule #c9c0b2.

    python3 scratch/diagrams/words_svgs.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "courses" / "2026-10-strategy" / "decks" / "images"
INK, MUTED, CORAL, CDARK, DEEP, WHITE, CLIGHT, RULE = (
    "#17201f", "#5c6763", "#f0674d", "#b8432d", "#e8e0d3", "#fffdf8", "#fbd9d1", "#c9c0b2")


def svg(name, h, label, body):
    defs = (f'<defs><marker id="{name}-i" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<marker id="{name}-c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{CORAL}"/></marker></defs>')
    s = (f'<svg class="diagram" viewBox="0 0 1200 {h}" preserveAspectRatio="xMidYMid meet" role="img" '
         f'aria-label="{label}">\n{defs}\n' + body.replace("@", name) + '\n</svg>\n')
    (OUT / f"words-{name}.svg").write_text(s)


def box(x, y, w, h, fill=WHITE, stroke=INK, sw=3, rx=14, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def t(x, y, s, size=22, weight=None, fill=INK, anchor="middle", italic=False):
    w = f' font-weight="{weight}"' if weight else ""
    i = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}"{w}{i} fill="{fill}">{s}</text>'


def arrow(x1, y1, x2, y2, color="i", sw=4):
    c = INK if color == "i" else CORAL
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" marker-end="url(#@-{color})"/>'


def path(d, color="i", sw=4):
    c = INK if color == "i" else CORAL
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" marker-end="url(#@-{color})"/>'


# 1. Skills: a folder with SKILL.md, picked up when the task matches.
b = []
b.append(box(60, 40, 420, 270, fill=DEEP))
b.append(t(90, 84, "check-quotes/", 28, 800, anchor="start"))
b.append(box(90, 106, 360, 180, fill=WHITE, rx=8))
b.append(t(110, 142, "SKILL.md", 22, 800, anchor="start"))
b.append(t(110, 178, "When: quotes in a report", 21, anchor="start"))
b.append(t(110, 210, "1. pull out every quote", 21, anchor="start"))
b.append(t(110, 240, "2. match it word for word", 21, anchor="start"))
b.append(t(110, 270, "3. list what doesn't match", 21, anchor="start"))
b.append(arrow(500, 175, 700, 175, "c"))
b.append(t(600, 145, "the task matches,", 21, fill=MUTED))
b.append(t(600, 215, "or you type its name", 21, fill=MUTED))
b.append(box(720, 95, 420, 160, fill=CLIGHT))
b.append(t(930, 160, "The agent follows it", 30, 800))
b.append(t(930, 200, "the same way, every time", 22))
b.append(t(600, 350, "A routine, written down once. Both tools use the same format.", 22, fill=MUTED))
svg("skills", 370, "A skill is a folder with a SKILL.md file: when to use it and the steps. The agent follows it when the task matches, or when you type its name.", "\n".join(b))

# 2. Subagents: one agent fans out to four helpers, summaries come back.
b = []
b.append(box(40, 130, 230, 110, fill=CLIGHT))
b.append(t(155, 178, "Main agent", 28, 800))
b.append(t(155, 212, "splits the job", 21))
ys = [30, 115, 200, 285]
labels = ["F01–F02", "F03–F04", "F05–F06", "F07–F08"]
for y, lab in zip(ys, labels):
    b.append(path(f"M 272 185 C 330 185, 330 {y+32}, 388 {y+32}"))
    b.append(box(400, y, 300, 66, fill=WHITE))
    b.append(t(550, y + 31, f"helper: {lab}", 22, 800))
    b.append(t(550, y + 56, "its own context", 18, fill=MUTED))
    b.append(path(f"M 702 {y+32} C 770 {y+32}, 770 185, 828 185", "c"))
b.append(box(840, 130, 320, 110, fill=DEEP))
b.append(t(1000, 178, "Summaries back", 28, 800))
b.append(t(1000, 212, "one line per founder", 21))
b.append(t(600, 382, "Faster, and the main conversation stays uncluttered. It also uses your limit faster.", 21, fill=MUTED))
svg("subagents", 400, "A main agent splits a job between four helper agents, each with its own context window. Only their summaries come back.", "\n".join(b))

# 3. Plan mode: plan, you approve, then it acts.
b = []
b.append(box(40, 70, 330, 190, fill=DEEP))
b.append(t(205, 122, "Plan mode", 30, 800))
b.append(t(205, 162, "reads, asks, proposes", 22))
b.append(t(205, 196, "changes nothing", 22, 800, fill=CDARK))
b.append(arrow(375, 165, 445, 165))
b.append(box(455, 90, 290, 150, fill=CLIGHT, stroke=CORAL, sw=4))
b.append(t(600, 145, "You", 30, 800))
b.append(t(600, 182, "approve the plan,", 22))
b.append(t(600, 210, "or change it", 22))
b.append(arrow(750, 165, 820, 165))
b.append(box(830, 70, 330, 190, fill=WHITE))
b.append(t(995, 122, "Then it acts", 30, 800))
b.append(t(995, 162, "edits, runs, commits", 22))
b.append(t(995, 196, "the plan you agreed", 22))
b.append(t(600, 320, "For big or risky jobs: read the plan before anything changes.", 22, fill=MUTED))
svg("plan", 345, "Plan mode: the agent reads, asks and proposes a plan without changing anything. You approve or change the plan. Then it acts.", "\n".join(b))

# 4. Context window and /compact: a full bar, then a compacted one.
b = []
def bar(y, segs, title):
    out = [t(60, y - 14, title, 22, 800, anchor="start")]
    x = 60
    for w, fill, lab in segs:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="64" fill="{fill}" stroke="{INK}" stroke-width="2"/>')
        if lab:
            out.append(t(x + w / 2, y + 40, lab, 20, fill=INK))
        x += w
    out.append(f'<rect x="60" y="{y}" width="1080" height="64" rx="0" fill="none" stroke="{INK}" stroke-width="3"/>')
    return out
b += bar(60, [(110, DEEP, "profile"), (130, DEEP, "project"), (520, CLIGHT, "the conversation so far"), (250, WHITE, "files it read"), (70, "#f4f0e8", "")], "A long session: the window is almost full")
b += bar(230, [(110, DEEP, "profile"), (130, DEEP, "project"), (180, CLIGHT, "a summary"), (660, "#f4f0e8", "room to work")], "After /compact")
b.append(arrow(600, 140, 600, 196, "c"))
b.append(t(620, 176, "/compact", 22, 800, fill=CDARK, anchor="start"))
b.append(t(600, 345, "/compact keeps a summary and frees room. /clear empties it: a fresh start.", 22, fill=MUTED))
svg("compact", 365, "The context window fills up during a long session with the conversation and the files read. Compact replaces the conversation with a short summary and frees room. Clear empties it.", "\n".join(b))

# 5. Worktrees: one history, two folders on two branches, two agents.
b = []
b.append(box(470, 20, 260, 80, fill=DEEP))
b.append(t(600, 58, ".git", 28, 800))
b.append(t(600, 86, "one project's history", 19, fill=MUTED))
b.append(path("M 520 102 C 480 140, 340 140, 300 168"))
b.append(path("M 680 102 C 720 140, 860 140, 900 168"))
b.append(box(110, 175, 380, 130, fill=WHITE))
b.append(t(300, 222, "paper/", 28, 800))
b.append(t(300, 256, "branch: main", 21, fill=MUTED))
b.append(t(300, 286, "agent 1 works here", 21))
b.append(box(710, 175, 380, 130, fill=CLIGHT))
b.append(t(900, 222, "paper-experiment/", 28, 800))
b.append(t(900, 256, "branch: experiment", 21, fill=MUTED))
b.append(t(900, 286, "agent 2 works here", 21))
b.append(path("M 710 280 C 640 330, 560 330, 492 280", "c"))
b.append(t(600, 352, "merge it back, if you like it", 21, fill=CDARK))
b.append(t(600, 392, "Two folders, one project: two agents at once, without touching each other's files.", 21, fill=MUTED))
svg("worktrees", 410, "A worktree is a second folder for the same git project, on its own branch. Two agents can work at once, one in each folder, and the experiment can be merged back.", "\n".join(b))

# 6. Agents in the cloud: GitHub copy, cloud agent, pull request back.
b = []
b.append(box(40, 110, 250, 150, fill=WHITE, dash="10 8"))
b.append(t(165, 170, "Your laptop", 28, 800))
b.append(t(165, 206, "can be closed", 22, fill=MUTED))
b.append(box(470, 110, 260, 150, fill=DEEP))
b.append(t(600, 170, "GitHub", 28, 800))
b.append(t(600, 206, "your repository", 22))
b.append(box(910, 110, 250, 150, fill=CLIGHT))
b.append(t(1035, 162, "Agent in", 28, 800))
b.append(t(1035, 196, "the cloud", 28, 800))
b.append(t(1035, 230, "works on a copy", 21))
b.append(path("M 732 150 C 800 110, 840 110, 906 150"))
b.append(t(820, 98, "a copy", 21, fill=MUTED))
b.append(path("M 906 225 C 840 265, 800 265, 734 225", "c"))
b.append(t(820, 292, "a pull request", 21, 800, fill=CDARK))
b.append(path("M 466 185 L 296 185", "c"))
b.append(t(380, 172, "you review it,", 20, fill=MUTED))
b.append(t(380, 210, "phone or laptop", 20, fill=MUTED))
b.append(t(600, 345, "Claude Code on the web (claude.ai/code) and Codex cloud (chatgpt.com/codex).", 22, fill=MUTED))
svg("cloud", 365, "Agents in the cloud: the agent works on a copy of your GitHub repository in the provider's cloud while your laptop can be closed, and sends back a pull request for you to review.", "\n".join(b))

print("wrote", sorted(p.name for p in OUT.glob("words-*.svg")))
