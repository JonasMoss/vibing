"""Build course-files.zip: what participants download on the day.

Contents: the handout (open it in a browser) and the practice folders, unpacked
from props/*.zip so nobody has to unzip a zip inside a zip. Rebuild after re-rendering the handout or changing a prop:

    quarto render courses/2026-12-marketing/handout.qmd
    python3 courses/2026-12-marketing/make-course-files.py
"""

import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOP = "ai-in-the-terminal"
FILES = {
    "handout.html": HERE / "handout.html",
}
PROPS = ["ai-label-paper", "decrap-me", "founders-study", "pivot-interviews", "messy-project", "references-practice"]
README = """AI in the terminal: Claude Code and Codex. BI, Department of Marketing,
3 December 2026.

Open handout.html in your browser: every prompt from the day, with a copy button.
The practice folders are in practice/, ready to use: copy one into your own
practice folder. (The handout also has a prompt that makes the agent fetch each
one.)

Questions: jonas.moss@bi.no
"""

out = HERE / "course-files.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    stamp = (2026, 12, 3, 12, 0, 0)
    info = zipfile.ZipInfo(f"{TOP}/README.txt", stamp)
    z.writestr(info, README, zipfile.ZIP_DEFLATED)
    for name, path in FILES.items():
        info = zipfile.ZipInfo(f"{TOP}/{name}", stamp)
        z.writestr(info, path.read_bytes(), zipfile.ZIP_DEFLATED)
    for prop in PROPS:
        with zipfile.ZipFile(HERE / "props" / f"{prop}.zip") as src:
            names = src.namelist()
            # Some props have a top folder named after them; some don't.
            prefix = "" if all(n.startswith(f"{prop}/") for n in names) else f"{prop}/"
            for n in names:
                info = zipfile.ZipInfo(f"{TOP}/practice/{prefix}{n}", stamp)
                if n.endswith("/"):
                    info.external_attr = 0o40755 << 16
                    z.writestr(info, b"")
                else:
                    z.writestr(info, src.read(n), zipfile.ZIP_DEFLATED)
print(f"Wrote {out.relative_to(HERE.parent.parent)} ({out.stat().st_size // 1024} KB)")
