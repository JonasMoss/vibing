"""Build ai-label-paper.zip: a fictional marketing paper in progress.

The fallback for anyone without their own paper, and the paper Jonas demos on.
Everything is made up (see src/FICTIONAL.txt); KEY.md lists what is planted.

    Rscript scratch/examples/ai-label-paper/simulate.R   # data (seed search)
    Rscript scratch/examples/ai-label-paper/numbers.R    # the numbers the draft quotes
    python3 scratch/examples/ai-label-paper/make.py      # the folder and the zip

Needs pandoc and typst (Quarto ships both).
"""

import json
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / "courses" / "2026-12-marketing" / "props" / "ai-label-paper.zip"
TOP = "ai-label-paper"
STAMP = (2026, 9, 14, 21, 30, 0)
STEM = "Nordmann_AI_label_v7"


def typst():
    for p in ["/opt/quarto/bin/tools/x86_64/typst", shutil.which("typst")]:
        if p and Path(p).exists():
            return p
    raise SystemExit("typst not found (it ships with Quarto)")


def pandoc(src, out, *extra):
    subprocess.run(["pandoc", str(src), "-o", str(out), *extra], check=True)


def main():
    nums = json.loads((HERE / "build" / "numbers.json").read_text())["draft"]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        md = tmp / f"{STEM}.md"
        md.write_text((HERE / "draft.md").read_text().format(**nums))
        pandoc(md, tmp / f"{STEM}.docx")
        pdf_opts = ["--pdf-engine", typst(), "-V", "papersize=a4", "-V", "fontsize=11pt",
                    "-V", "margin.x=2.5cm", "-V", "margin.y=2.5cm",
                    "-V", "mainfont=Libertinus Serif"]
        pandoc(md, tmp / f"{STEM}.pdf", *pdf_opts)
        pandoc(HERE / "src" / "prereg.md", tmp / "AsPredicted_118804.pdf", *pdf_opts)

        files = {
            f"{STEM}.docx": tmp / f"{STEM}.docx",
            f"{STEM}.pdf": tmp / f"{STEM}.pdf",
            "FICTIONAL.txt": HERE / "src" / "FICTIONAL.txt",
            "analysis/analysis.R": HERE / "src" / "analysis.R",
            "data/prolific_export_2026-09-14.csv": HERE / "build" / "prolific_export_2026-09-14.csv",
            "prereg/AsPredicted_118804.pdf": tmp / "AsPredicted_118804.pdf",
            "survey/survey-flow.txt": HERE / "src" / "survey-flow.txt",
            "notes/from-Ola-2026-09-09.txt": HERE / "src" / "from-Ola-2026-09-09.txt",
        }
        OUT.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
            for d in sorted({str(Path(n).parent) for n in files} - {"."}):
                info = zipfile.ZipInfo(f"{TOP}/{d}/", STAMP)
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            for name, path in files.items():
                z.writestr(zipfile.ZipInfo(f"{TOP}/{name}", STAMP), path.read_bytes(), zipfile.ZIP_DEFLATED)
        # A copy of the built PDF for checking and for the sycophancy runs.
        shutil.copy(tmp / f"{STEM}.pdf", HERE / "build" / f"{STEM}.pdf")
        shutil.copy(tmp / f"{STEM}.docx", HERE / "build" / f"{STEM}.docx")
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
