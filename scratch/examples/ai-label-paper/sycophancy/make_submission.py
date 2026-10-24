"""The anonymised submission PDF: what a journal (and a blind referee) gets.

Strips the names, e-mail, notice, acknowledgements, self-citation, leftover
comments and PDF metadata from draft v7. Writes build/submission.pdf.
    python3 scratch/examples/ai-label-paper/sycophancy/make_submission.py
"""
import json, re, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
nums = json.loads((PAPER / "build" / "numbers.json").read_text())["draft"]
s = (PAPER / "draft.md").read_text().format(**nums)
s = re.sub(r"^---\n.*?\n---\n", '---\ntitle: "Made by a Machine: AI-Disclosure Labels Lower Purchase Intention for Hedonic Products"\n---\n', s, flags=re.S)
start = s.index("**Kari Nordmann**"); end = s.index("# Abstract")
s = s[:start] + s[end:]
s = s.replace("In our earlier work (Nordmann & Nordmann, 2024), we found", "Earlier work (Authors, 2024) found")
s = re.sub(r"Nordmann, K\., & Nordmann, O\. \(2024\)\..*?\(EMAC\)\*\.\n", "Authors (2024). Details removed for review.\n", s, flags=re.S)
s = re.sub(r" ?\[OLA:.*?\]", "", s, flags=re.S)
s = re.sub(r" ?\[KN:.*?\]", "", s, flags=re.S)
assert "Nordmann" not in s and "OLA" not in s and "KN:" not in s and "Fictional" not in s
md = PAPER / "build" / "submission.md"
md.write_text(s)
subprocess.run(["pandoc", str(md), "-o", str(PAPER / "build" / "submission.pdf"),
                "--pdf-engine", "/opt/quarto/bin/tools/x86_64/typst", "-V", "papersize=a4",
                "-V", "fontsize=11pt", "-V", "margin.x=2.5cm", "-V", "margin.y=2.5cm",
                "-V", "mainfont=Libertinus Serif"], check=True)
print("ok")
