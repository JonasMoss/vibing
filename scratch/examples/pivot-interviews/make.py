"""Build props/pivot-interviews.zip for the Strategy course from src/.

The transcripts in src/ are fictional (written with Codex, 21 October 2026, then
checked by hand). KEY.md, next to this file, is the instructor key; it does not
go into the zip.

    python3 scratch/examples/pivot-interviews/make.py
"""

import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE.parents[2] / "courses" / "2026-10-strategy" / "props" / "pivot-interviews.zip"
STAMP = (2026, 2, 20, 9, 0, 0)

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(SRC.rglob("*")):
        if path.is_file():
            name = "pivot-interviews/" + path.relative_to(SRC).as_posix()
            z.writestr(zipfile.ZipInfo(name, STAMP), path.read_bytes(), zipfile.ZIP_DEFLATED)
print(f"Wrote {OUT.relative_to(HERE.parents[2])} ({OUT.stat().st_size // 1024} KB)")
