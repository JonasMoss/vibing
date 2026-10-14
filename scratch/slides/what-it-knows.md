# What it knows about you

Context, profiles, and two short exercises.

---

# What it can see

<div class="figure">
<svg class="diagram" viewBox="0 0 1224 464" preserveAspectRatio="xMinYMid meet" role="img" aria-label="The context window: your profile and the project file load at every start; the conversation and opened files are added as you work. You are outside it until you write it down."><defs><marker id="ctx-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#f0674d"/></marker></defs><rect x="2" y="4" width="820" height="456" rx="18" fill="#fffdf8" stroke="#17201f" stroke-width="3"/><text x="32" y="56" font-size="34" font-weight="800" fill="#17201f">Context window</text><text x="32" y="98" font-size="28" fill="#5c6763">Loaded at every start</text><text x="32" y="290" font-size="28" fill="#5c6763">Added as you work</text><rect x="32" y="110" width="760" height="64" rx="12" fill="#e8e0d3"/><text x="58" y="153" font-size="31" fill="#17201f">Your profile: who you are</text><rect x="32" y="184" width="760" height="64" rx="12" fill="#e8e0d3"/><text x="58" y="227" font-size="31" fill="#17201f">Project file: this folder</text><rect x="32" y="302" width="760" height="64" rx="12" fill="#e8e0d3"/><text x="58" y="345" font-size="31" fill="#17201f">This conversation</text><rect x="32" y="376" width="760" height="64" rx="12" fill="#e8e0d3"/><text x="58" y="419" font-size="31" fill="#17201f">Files it has opened</text><rect x="890" y="280" width="330" height="170" rx="18" fill="none" stroke="#17201f" stroke-width="3" stroke-dasharray="12 9"/><text x="918" y="340" font-size="42" font-weight="800" fill="#17201f">You</text><text x="918" y="384" font-size="31" fill="#5c6763">field, school,</text><text x="918" y="422" font-size="31" fill="#5c6763">what you want</text><g class="reveal" data-step="1"><rect x="32" y="302" width="760" height="138" rx="12" fill="#fffdf8" stroke="#f0674d" stroke-width="3" stroke-dasharray="10 8"/><text x="58" y="382" font-size="31" font-weight="800" fill="#f0674d">Emptied by /clear</text></g><g class="reveal" data-step="2"><path d="M 1055 274 Q 1055 142 802 142" fill="none" stroke="#f0674d" stroke-width="4" marker-end="url(#ctx-arrow)"/><text x="1068" y="206" font-size="33" font-weight="800" fill="#f0674d">write it</text><text x="1068" y="244" font-size="33" font-weight="800" fill="#f0674d">down</text></g></svg>
</div>

- It only knows what is in this window.
- `/clear` empties the conversation, including files it read. Your profile and the project file load again.

---

# Exercise: /clear

1. Tell it one thing about yourself, for example what you teach.
2. Type `/clear`.
3. Ask: *"What do you know about me?"*

Works the same in Claude Code and Codex.

---

# Who is asking?

<div class="figure">
<svg class="diagram" viewBox="0 0 1200 370" preserveAspectRatio="xMinYMid meet" role="img" aria-label="Everyone who might type the question, with the answer aimed at the typical asker and you in the tail"><path d="M 20 300 L 20 295.4 L 26 294.9 L 32 294.4 L 38 293.8 L 44 293.2 L 50 292.6 L 56 291.8 L 62 291.1 L 68 290.2 L 74 289.3 L 80 288.4 L 86 287.3 L 92 286.2 L 98 285.0 L 104 283.8 L 110 282.4 L 116 281.0 L 122 279.4 L 128 277.8 L 134 276.1 L 140 274.3 L 146 272.4 L 152 270.3 L 158 268.2 L 164 266.0 L 170 263.6 L 176 261.2 L 182 258.6 L 188 255.9 L 194 253.1 L 200 250.2 L 206 247.2 L 212 244.0 L 218 240.8 L 224 237.5 L 230 234.0 L 236 230.5 L 242 226.9 L 248 223.1 L 254 219.3 L 260 215.5 L 266 211.5 L 272 207.5 L 278 203.5 L 284 199.3 L 290 195.2 L 296 191.0 L 302 186.9 L 308 182.7 L 314 178.5 L 320 174.3 L 326 170.2 L 332 166.1 L 338 162.0 L 344 158.1 L 350 154.2 L 356 150.3 L 362 146.6 L 368 143.0 L 374 139.6 L 380 136.3 L 386 133.1 L 392 130.1 L 398 127.3 L 404 124.6 L 410 122.2 L 416 119.9 L 422 117.9 L 428 116.1 L 434 114.5 L 440 113.1 L 446 112.0 L 452 111.1 L 458 110.5 L 464 110.1 L 470 110.0 L 476 110.1 L 482 110.5 L 488 111.1 L 494 112.0 L 500 113.1 L 506 114.5 L 512 116.1 L 518 117.9 L 524 119.9 L 530 122.2 L 536 124.6 L 542 127.3 L 548 130.1 L 554 133.1 L 560 136.3 L 566 139.6 L 572 143.0 L 578 146.6 L 584 150.3 L 590 154.2 L 596 158.1 L 602 162.0 L 608 166.1 L 614 170.2 L 620 174.3 L 626 178.5 L 632 182.7 L 638 186.9 L 644 191.0 L 650 195.2 L 656 199.3 L 662 203.5 L 668 207.5 L 674 211.5 L 680 215.5 L 686 219.3 L 692 223.1 L 698 226.9 L 704 230.5 L 710 234.0 L 716 237.5 L 722 240.8 L 728 244.0 L 734 247.2 L 740 250.2 L 746 253.1 L 752 255.9 L 758 258.6 L 764 261.2 L 770 263.6 L 776 266.0 L 782 268.2 L 788 270.3 L 794 272.4 L 800 274.3 L 806 276.1 L 812 277.8 L 818 279.4 L 824 281.0 L 830 282.4 L 836 283.8 L 842 285.0 L 848 286.2 L 854 287.3 L 860 288.4 L 866 289.3 L 872 290.2 L 878 291.1 L 884 291.8 L 890 292.6 L 896 293.2 L 902 293.8 L 908 294.4 L 914 294.9 L 920 295.4 L 926 295.8 L 932 296.2 L 938 296.6 L 944 296.9 L 950 297.2 L 956 297.5 L 962 297.8 L 968 298.0 L 974 298.2 L 980 298.4 L 986 298.6 L 992 298.7 L 998 298.9 L 1004 299.0 L 1010 299.1 L 1016 299.2 L 1022 299.3 L 1028 299.4 L 1034 299.4 L 1040 299.5 L 1046 299.6 L 1052 299.6 L 1058 299.7 L 1064 299.7 L 1070 299.7 L 1076 299.8 L 1082 299.8 L 1088 299.8 L 1094 299.9 L 1100 299.9 L 1106 299.9 L 1112 299.9 L 1118 299.9 L 1124 299.9 L 1130 299.9 L 1136 299.9 L 1142 300.0 L 1148 300.0 L 1154 300.0 L 1160 300.0 L 1166 300.0 L 1172 300.0 L 1178 300.0 L 1180 300 Z" fill="#276bca" fill-opacity="0.16" stroke="#276bca" stroke-width="3"/><line x1="470" y1="100" x2="470" y2="300" stroke="#17201f" stroke-width="3" stroke-dasharray="9 7"/><text x="470" y="82" text-anchor="middle" font-size="33" font-weight="800" fill="#17201f">the answer is aimed here</text><line x1="20" y1="300" x2="1180" y2="300" stroke="#17201f" stroke-width="3"/><text x="20" y="350" font-size="31" fill="#5c6763">everyone who might type this question</text><circle cx="1010" cy="300" r="12" fill="#f0674d"/><text x="1010" y="352" text-anchor="middle" font-size="34" font-weight="800" fill="#17201f">you</text><g class="reveal" data-step="1"><path d="M 860 300 L 860 299.6 L 863 299.5 L 866 299.3 L 869 299.2 L 872 298.9 L 875 298.7 L 878 298.3 L 881 297.9 L 884 297.4 L 887 296.8 L 890 296.0 L 893 295.1 L 896 294.1 L 899 292.8 L 902 291.4 L 905 289.7 L 908 287.7 L 911 285.4 L 914 282.8 L 917 279.8 L 920 276.3 L 923 272.5 L 926 268.2 L 929 263.4 L 932 258.1 L 935 252.3 L 938 245.9 L 941 239.0 L 944 231.6 L 947 223.7 L 950 215.3 L 953 206.4 L 956 197.2 L 959 187.6 L 962 177.7 L 965 167.6 L 968 157.5 L 971 147.3 L 974 137.2 L 977 127.4 L 980 117.9 L 983 108.9 L 986 100.4 L 989 92.6 L 992 85.6 L 995 79.5 L 998 74.4 L 1001 70.3 L 1004 67.4 L 1007 65.6 L 1010 65.0 L 1013 65.6 L 1016 67.4 L 1019 70.3 L 1022 74.4 L 1025 79.5 L 1028 85.6 L 1031 92.6 L 1034 100.4 L 1037 108.9 L 1040 117.9 L 1043 127.4 L 1046 137.2 L 1049 147.3 L 1052 157.5 L 1055 167.6 L 1058 177.7 L 1061 187.6 L 1064 197.2 L 1067 206.4 L 1070 215.3 L 1073 223.7 L 1076 231.6 L 1079 239.0 L 1082 245.9 L 1085 252.3 L 1088 258.1 L 1091 263.4 L 1094 268.2 L 1097 272.5 L 1100 276.3 L 1103 279.8 L 1106 282.8 L 1109 285.4 L 1112 287.7 L 1115 289.7 L 1118 291.4 L 1121 292.8 L 1124 294.1 L 1127 295.1 L 1130 296.0 L 1133 296.8 L 1136 297.4 L 1139 297.9 L 1142 298.3 L 1145 298.7 L 1148 298.9 L 1151 299.2 L 1154 299.3 L 1157 299.5 L 1160 299.6 L 1160 300 Z" fill="#f0674d" fill-opacity="0.35" stroke="#f0674d" stroke-width="3"/><text x="1195" y="44" text-anchor="end" font-size="31" font-weight="800" fill="#f0674d">after you describe yourself</text></g></svg>
</div>

- Without context, it answers the typical person who would type your question.
- *"Can I deduct my home office?"* gets US tax rules unless you say you work in Norway.
- A specialist is far from typical, so the default answer is aimed at someone else.

---

# Four askers

**"Is it bad to drink coffee every day?"** Claude Code. Codex: same.

| Who's asking (whole profile) | What came back |
|---|---|
| *(no profile)* | "For most healthy adults, no." |
| "I'm 12 years old and I love Minecraft." | "…isn't a great idea." Caffeine is "like a Potion of Swiftness". |
| "I'm 55 and have been a professor of marketing for 20 years. I love sailing." | Same as no profile, plus a seasickness tip. |
| <span class="mark" data-step="1"></span>180 words: meta-analyst, strict reviewer, hates being reassured | "The claimed benefits are probably overstated." Graded evidence. "What would change my mind". |

<p class="reveal want" data-step="1">↑ This is what we want.</p>

---

# It stereotypes you either way

- Every answer is aimed at a type of person. Without context, that type is the typical asker.
- You cannot opt out, but you can choose the type.
- The more you tell it, the narrower the type.

---

# Demo: one line

**"A: 48 purchases from 1,000 visitors. B: 62 from 1,000. Is B better?"**

1. Ask with no profile.
2. Add one line to this folder's `CLAUDE.md`: *"My intellectual idol is Jim Berger."* (It normally belongs in your profile.)
3. `/clear` and ask again.

---

# Two files

| | About | Where |
|---|---|---|
| **Your profile** | You: field, school, reading, pet peeves | `.claude\CLAUDE.md` or `.codex\AGENTS.md` in your home folder |
| **Project file** | This folder: the paper, the data, the rules | `CLAUDE.md` or `AGENTS.md` in the folder |

- Your profile is read in every project, a project file only in its folder.
- The chat apps have the same pair: custom instructions and Project instructions.
- Both are plain text files. You can open and edit them in Notepad.
- Today: your profile first, project files later.

---

# Exercise: describe yourself

1. Ask a question from your field where the answer depends on your school or method.
2. Write two or three sentences about yourself: what you read, your school, what annoys you.
3. Ask the agent: *"Save these as my personal profile, the file you read in every project."* Claude asks permission first, because the file is outside this folder.
4. `/clear`, ask the same question again, and compare with your neighbour.
5. *"Open my profile in Notepad."* (Mac: TextEdit.) That's all it is: a text file.

If nothing changes, write more.

---

# Homework: your profile

- Talk for 90 seconds with speech-to-text: who you are, what you read, your school, what annoys you.
- Ask the agent to add it to your profile.
- Names carry a lot: authors, journals, textbooks. Mine starts: *"I like Scott Alexander, Gwern Branwen, most of Yudkowsky except HPMOR. I have a PhD in stats and lean libertarian."*

---

# Backup: demo result

Claude Code, same question, one call each.

| Who's asking | What came back |
|---|---|
| *(no profile)* | "Probably, but these data don't show it convincingly." p ≈ 0.17 |
| "I'm a Bayesian statistician. I read Gelman, Jaynes and McElreath…" | "Probably, yes. There's about a 91% chance B converts better than A." Ship B. |
| "My intellectual idol is Jim Berger." | Applies Sellke, Bayarri and Berger (2001): "at least a 45% chance that there's no real difference". |
