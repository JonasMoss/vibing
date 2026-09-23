# Deck images — the POWER shot list

Screenshots make the capability claims land harder than words. This folder holds
them; the build inlines each one into the slide as a data URI, so a deck is
self-contained even offline.

## How to add a shot

1. Drop the image file in this folder (PNG / JPG / GIF / WebP / SVG).
2. Reference it in the slide markdown: `![a caption](images/your-file.png)`
   — the caption renders under the image.
3. Rebuild (`node scripts/build-site.mjs`). A referenced file that is **missing**
   renders a dashed **"📷 screenshot needed"** box — so outstanding shots stay
   visible right in the deck.

**Don't fabricate** leaderboard / benchmark screenshots — the whole deck is about
verifiable claims. Capture the real thing from the source listed below.

## Have

| File | Slide | Source |
|---|---|---|
| `jacobian-tweet.png` | "An 87-year-old conjecture — disproved" | Alpöge + Gowers, X (captured) |
| `gowers-2030.png` | "The people who would know are not calm" | Szegedy / Gowers thread, X (captured) |
| `kojima-step-by-step.png` | "Prompt engineering (RIP)" (landscape deck) | Kojima et al. 2022, arXiv:2205.11916v4, Fig. 1 panels (c)–(d), cropped |

## Referenced in the deck, still needed (placeholders showing now)

| File | Slide | Capture from |
|---|---|---|
| `atcoder-2026-standings.png` | "July 2026 — one year later" | `atcoder.jp/contests/awtf2026heuristic` standings; context: `officechai.com/ai/openai-completely-demolishes-human-competitors-at-atcoder-2026-after-placing-2nd-last-year/` |
| `psyho-2025-tweet.png` | "July 2025" | Psyho's "Humanity has prevailed (for now!)" post; context: `euronews.com/next/2025/07/22/humanity-has-won-so-far-meet-the-worlds-best-programmer-who-beat-ai-and-chatgpt` |
| `icpc-2025-scoreboard.png` | "And it wasn't a fluke" | `icpc.global/worldfinals/results-2025`; DeepMind: `deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/` |

## Optional extras (not referenced yet — add a placeholder if you want them)

**Maths (Exhibit B)**
- Unit-distance disproof — Kalai `gilkalai.wordpress.com/2026/05/21/` / Tao `terrytao.wordpress.com/2026/07/03/`
- Erdős tracker table — `github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erdős-problems`
- Benjamini–Hochberg flaw — `the-decoder.com/gpt-5-6-sol-reportedly-disproves-a-30-year-old-statistics-conjecture-in-90-minutes-after-humans-couldnt-crack-it/`
- FrontierMath 42% — `epoch.ai/benchmarks/frontiermath-tier-4-v2`

**Security (Exhibit C)** — sources for the slides just added
- Big Sleep / SQLite 0-day (Nov 2024, ✅) — `thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html` (primary: Project Zero blog)
- DARPA AIxCC final (Aug 2025, ✅ — cleanest, non-vendor) — `darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33`
- Claude **Mythos** cyber eval (Apr 2026, 🟡 — **not** public Fable 5; FreeBSD bug = CVE-2026-4747) — `anthropic.com/research/mythos-preview`; launch `anthropic.com/news/claude-fable-5-mythos-5`
- OpenAI × Hugging Face incident (Jul 2026 — ✅ event, contested framing) — `openai.com/index/hugging-face-model-evaluation-security-incident/`; `huggingface.co/blog/security-incident-july-2026`; skeptic view `techcrunch.com/2026/07/22/how-an-openais-human-mistake-led-to-the-ai-powered-hack-on-hugging-face/`

**magmaan (Exhibit D)** — a speed chart (lavaan vs magmaan, model-for-model) if you have one.
