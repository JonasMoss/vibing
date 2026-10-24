"""SVG charts for the Marketing sycophancy deck, in the house style of
git-survey.svg: horizontal bars, 4px rounded ends, direct labels, hover titles.
    python3 scratch/diagrams/sycophancy_svgs.py
Sources (checked 24 October 2026):
  overlap: Liang et al. (2023), arXiv:2310.01783, Results / Fig. 2.
  gpt5:    OpenAI, GPT-5 System Card (7 Aug 2025), section 3.3, Table 4.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "courses" / "2026-12-marketing" / "decks" / "images"
INK, MUTED, CORAL, GREY, RULE = "#17201f", "#5c6763", "#d4492f", "#8f877b", "#d9d1c4"


def bar(x0, y, w, h, fill):
    r = 4
    if w <= r:
        return f'<rect x="{x0}" y="{y}" width="{max(w, 1):.1f}" height="{h}" fill="{fill}"/>'
    x1 = x0 + w
    return (f'<path d="M{x0},{y} H{x1 - r:.1f} Q{x1:.1f},{y} {x1:.1f},{y + r} V{y + h - r} '
            f'Q{x1:.1f},{y + h} {x1 - r:.1f},{y + h} H{x0} Z" fill="{fill}"/>')


def overlap():
    # Share of one reviewer's comments that another reviewer also raised.
    groups = [("Nature journals", 30.85, 28.58), ("ICLR", 39.23, 35.25)]
    x0, scale, H = 330, 15.0, 330   # 50% -> 750 px
    s = [f'<svg class="diagram" viewBox="0 0 1200 {H}" preserveAspectRatio="xMidYMid meet" role="img" '
         'aria-label="Bar chart. Share of comments raised by one reviewer that another also raised. '
         'Nature journals: GPT-4 and a human 30.9 percent, two humans 28.6 percent. '
         'ICLR: GPT-4 and a human 39.2 percent, two humans 35.3 percent.">']
    s.append(f'<line x1="{x0}" y1="10" x2="{x0}" y2="{H - 50}" stroke="{RULE}" stroke-width="1"/>')
    y = 20
    for name, ai, hum in groups:
        s.append(f'<text x="{x0 - 18}" y="{y + 52}" text-anchor="end" font-size="30" font-weight="800" fill="{INK}">{name}</text>')
        for label, v, fill, bold in [("GPT-4 vs. a human", ai, CORAL, True), ("Two humans", hum, GREY, False)]:
            w = v * scale
            s.append(f'<g><title>{name}, {label}: {v:.2f}%</title>')
            s.append(bar(x0, y, w, 34, fill))
            s.append(f'<text x="{x0 + w + 14:.1f}" y="{y + 26}" font-size="26" font-weight="{800 if bold else 400}" '
                     f'fill="{INK if bold else MUTED}">{v:.0f}%  <tspan font-size="22" font-weight="400" fill="{MUTED}">{label}</tspan></text></g>')
            y += 44
        y += 40
    s.append(f'<text x="{x0}" y="{H - 14}" font-size="20" fill="{MUTED}">Share of one reviewer\'s comments that the other also raised. Liang et al. (2023), GPT-4.</text>')
    s.append('</svg>')
    (OUT / "syco-overlap.svg").write_text("\n".join(s) + "\n")


def gpt5():
    rows = [("GPT-4o (April 2025)", 0.145, GREY), ("GPT-5", 0.052, CORAL), ("GPT-5 thinking", 0.040, CORAL)]
    x0, scale, H = 330, 4800, 250   # 0.15 -> 720 px
    s = [f'<svg class="diagram" viewBox="0 0 1200 {H}" preserveAspectRatio="xMidYMid meet" role="img" '
         'aria-label="Bar chart. OpenAI offline sycophancy score, lower is better: GPT-4o 0.145, GPT-5 0.052, GPT-5 thinking 0.040.">']
    s.append(f'<line x1="{x0}" y1="10" x2="{x0}" y2="{H - 50}" stroke="{RULE}" stroke-width="1"/>')
    y = 20
    for name, v, fill in rows:
        w = v * scale
        s.append(f'<g><title>{name}: {v}</title>')
        s.append(f'<text x="{x0 - 18}" y="{y + 30}" text-anchor="end" font-size="28" font-weight="800" fill="{INK}">{name}</text>')
        s.append(bar(x0, y, w, 40, fill))
        s.append(f'<text x="{x0 + w + 14:.1f}" y="{y + 30}" font-size="28" font-weight="800" fill="{INK}">{v:.3f}</text></g>')
        y += 60
    s.append(f'<text x="{x0}" y="{H - 14}" font-size="20" fill="{MUTED}">Sycophancy score on OpenAI\'s own test set, lower is better. GPT-5 System Card, Table 4.</text>')
    s.append('</svg>')
    (OUT / "syco-gpt5.svg").write_text("\n".join(s) + "\n")


if __name__ == "__main__":
    overlap(); gpt5(); print("ok")
