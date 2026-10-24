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


def ours():
    """Our framing experiment: mean score per framing and model (results.json)."""
    import json
    res = json.loads((Path(__file__).resolve().parents[1] / "examples" / "ai-label-paper" /
                      "sycophancy" / "results.json").read_text())["framing"]
    rows = [("blind", "\u201cYou are a referee\u201d"), ("colleague", "\u201cA colleague\u2019s paper\u201d"),
            ("mine", "\u201cMy paper\u201d"), ("proud", "\u201cMy paper, I\u2019m proud of it\u201d")]
    models = [("haiku", "Claude Haiku", CORAL, -9), ("luna", "GPT-6-Luna", GREY, 9)]
    x0, x1, H = 430, 1150, 360
    sx = lambda v: x0 + (v - 1) / 9 * (x1 - x0)
    desc = "; ".join(f"{lab}: Haiku {res['haiku/' + k]['mean']}, Luna {res['luna/' + k]['mean']}" for k, lab in rows)
    s = [f'<svg class="diagram" viewBox="0 0 1200 {H}" preserveAspectRatio="xMidYMid meet" role="img" '
         f'aria-label="Dot plot. Mean referee score out of 10 for the same paper under four framings. {desc}.">']
    for v in [1, 3, 5, 7, 10]:
        s.append(f'<line x1="{sx(v):.1f}" y1="30" x2="{sx(v):.1f}" y2="270" stroke="{RULE}" stroke-width="1"/>')
        s.append(f'<text x="{sx(v):.1f}" y="296" text-anchor="middle" font-size="22" fill="{MUTED}">{v}</text>')
    y = 60
    for k, lab in rows:
        s.append(f'<text x="{x0 - 24}" y="{y + 9}" text-anchor="end" font-size="26" font-weight="700" fill="{INK}">{lab}</text>')
        for m, mname, col, dy in models:
            r = res[f"{m}/{k}"]
            s.append(f'<g><title>{mname}, {lab}: mean {r["mean"]} (scores {", ".join(str(int(v)) for v in r["scores"])})</title>'
                     f'<circle cx="{sx(r["mean"]):.1f}" cy="{y + dy}" r="9" fill="{col}" stroke="#fffdf8" stroke-width="2"/></g>')
        y += 58
    lx = sx(7.4)
    for i, (m, mname, col, dy) in enumerate(models):
        s.append(f'<circle cx="{lx}" cy="{80 + i * 34}" r="9" fill="{col}"/>'
                 f'<text x="{lx + 18}" y="{88 + i * 34}" font-size="24" fill="{INK}">{mname}</text>')
    s.append(f'<text x="{x0}" y="{H - 16}" font-size="20" fill="{MUTED}">Mean score out of 10 (10 = accept as is). Ten fresh sessions per framing and model.</text>')
    s.append('</svg>')
    (OUT / "syco-ours.svg").write_text("\n".join(s) + "\n")


def tone():
    """Free-form feedback, blind vs. "my paper, I'm proud of it" (results.json)."""
    import json
    t = json.loads((Path(__file__).resolve().parents[1] / "examples" / "ai-label-paper" /
                    "sycophancy" / "results.json").read_text())["tone"]
    rows = [("haiku", "blind", "Claude Haiku", "blind referee"), ("haiku", "proud", "", "\u201cmy paper, I\u2019m proud\u201d"),
            ("luna", "blind", "GPT-6-Luna", "blind referee"), ("luna", "proud", "", "\u201cmy paper, I\u2019m proud\u201d")]
    panels = [("says_reject_or_major_revision", "Gives a verdict", 470),
              ("opens_with_praise", "Opens with praise", 860)]
    H, bw, sc = 330, 300, 30   # 10 -> 300 px
    desc = "; ".join(f"{m} {fr}: verdict {t[f'{m}/{fr}/text']['says_reject_or_major_revision']} of 10, "
                     f"praise first {t[f'{m}/{fr}/text']['opens_with_praise']} of 10" for m, fr, *_ in rows)
    s = [f'<svg class="diagram" viewBox="0 0 1200 {H}" preserveAspectRatio="xMidYMid meet" role="img" '
         f'aria-label="Bar chart, out of 10 reports each. {desc}.">']
    for key, title, x0 in panels:
        s.append(f'<text x="{x0}" y="26" font-size="24" font-weight="800" fill="{INK}">{title}</text>')
        s.append(f'<line x1="{x0}" y1="40" x2="{x0}" y2="{H - 50}" stroke="{RULE}" stroke-width="1"/>')
    y = 52
    for i, (m, fr, mname, lab) in enumerate(rows):
        if mname:
            s.append(f'<text x="20" y="{y + 26}" font-size="26" font-weight="800" fill="{INK}">{mname}</text>')
        s.append(f'<text x="{panels[0][2] - 16}" y="{y + 24}" text-anchor="end" font-size="22" fill="{MUTED}">{lab}</text>')
        for key, title, x0 in panels:
            v = t[f"{m}/{fr}/text"][key]
            col = CORAL if fr == "proud" else GREY
            s.append(f'<g><title>{mname or rows[i-1][2]}, {lab}: {title.lower()}, {v} of 10</title>')
            s.append(bar(x0, y + 4, v * sc, 28, col) if v else "")
            s.append(f'<text x="{x0 + v * sc + 10}" y="{y + 26}" font-size="24" font-weight="800" fill="{INK}">{v}</text></g>')
        y += 50 if fr == "blind" else 66
    s.append(f'<text x="20" y="{H - 16}" font-size="20" fill="{MUTED}">Out of 10 fresh sessions each. Verdict: reject or major revision. The prompt asked for feedback, no score.</text>')
    s.append('</svg>')
    (OUT / "syco-tone.svg").write_text("\n".join(s) + "\n")


if __name__ == "__main__":
    overlap(); gpt5(); ours(); tone(); print("ok")
