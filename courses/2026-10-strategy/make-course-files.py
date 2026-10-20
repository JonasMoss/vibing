"""Build course-files.zip: what participants download on the day.

Contents: the handout (open it in a browser) and the practice zips, in one
folder. Rebuild after re-rendering the handout or changing a prop:

    quarto render courses/2026-10-strategy/handout.qmd
    python3 courses/2026-10-strategy/make-course-files.py
"""

import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOP = "ai-in-the-terminal"
FILES = {
    "handout.html": HERE / "handout.html",
    "practice/founders-study.zip": HERE / "props" / "founders-study.zip",
    "practice/decrap-me.zip": HERE / "props" / "decrap-me.zip",
    "practice/messy-project.zip": HERE / "props" / "messy-project.zip",
    "practice/references-practice.zip": HERE / "props" / "references-practice.zip",
}
README = """AI in the terminal: Claude Code and Codex. BI, Strategy and Entrepreneurship,
22 and 23 October 2026.

Open handout.html in your browser: every prompt from the day, with a copy button.
The practice folders are in practice/. The handout tells the agent how to fetch
them, but you can also unzip them yourself.

Questions: jonas.moss@bi.no
"""

out = HERE / "course-files.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    stamp = (2026, 10, 22, 12, 0, 0)
    info = zipfile.ZipInfo(f"{TOP}/README.txt", stamp)
    z.writestr(info, README, zipfile.ZIP_DEFLATED)
    for name, path in FILES.items():
        info = zipfile.ZipInfo(f"{TOP}/{name}", stamp)
        z.writestr(info, path.read_bytes(), zipfile.ZIP_DEFLATED)
print(f"Wrote {out.relative_to(HERE.parent.parent)} ({out.stat().st_size // 1024} KB)")
