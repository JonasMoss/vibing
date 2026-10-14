#!/usr/bin/env python3
"""Generate the Day-3 email-demo input: a graded course scored by group.

Emits examples/grades/scores.csv and examples/grades/scores.xlsx from one table.
Synthetic — same Nordic Style / ELE37911 world as the decrap example, so the
story carries across days ("you cleaned the folder, you graded them, now email
the results"). Safe to commit and hand out.

The .xlsx is hand-built with the standard library only (no openpyxl / no pandas)
so this runs anywhere Python does. It uses inline strings and a minimal style
sheet — the smallest thing Excel and the agents will open cleanly. Reproducible:
edit `POINTS` / `COMMENTS` and re-run `python3 scratch/examples/scripts/make-scores-example.py`.
"""

import csv
import zipfile
from pathlib import Path
from xml.dom.minidom import parseString

ROOT = Path(__file__).resolve().parents[2]  # scratch/
OUT = ROOT / "examples" / "grades"

COURSE = "ELE37911 Business Intelligence with Power BI"

# Group -> exam points (out of 100). Grades are derived, so the two files agree.
POINTS = {
    1: 78, 2: 63, 3: 91, 4: 55, 5: 84, 6: 48, 7: 34, 8: 72,
    9: 88, 10: 69, 11: 76, 12: 95, 13: 61, 14: 81, 15: 66,
}

# A few graded comments, to give the summarised email something to say.
COMMENTS = {
    3: "Strong analysis; clear DAX model.",
    12: "Excellent - best in the cohort.",
    6: "Below the pass line; core analysis missing.",
    7: "Incomplete; dashboard not functional.",
}


def grade(points: int) -> str:
    """Standard A-F scale (A best, E lowest pass, F fail)."""
    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D"), (50, "E")):
        if points >= cutoff:
            return letter
    return "F"


ROWS = [
    (g, POINTS[g], grade(POINTS[g]), COMMENTS.get(g, ""))
    for g in sorted(POINTS)
]
HEADER = ("Group", "Points", "Grade", "Comment")


def write_csv(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(HEADER)
        w.writerows(ROWS)


# --- minimal .xlsx (Open Packaging Convention: a zip of XML parts) -----------

def esc(text: str) -> str:
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def col_letter(idx: int) -> str:  # 0 -> A, 1 -> B, ...
    return chr(ord("A") + idx)


def cell(col: int, row: int, value) -> str:
    ref = f"{col_letter(col)}{row}"
    if isinstance(value, (int, float)):
        return f'<c r="{ref}"><v>{value}</v></c>'
    if value == "":
        return ""  # omit empty cells entirely
    return f'<c r="{ref}" t="inlineStr"><is><t xml:space="preserve">{esc(value)}</t></is></c>'


def sheet_xml() -> str:
    body = [HEADER, *ROWS]
    rows_xml = []
    for r, record in enumerate(body, start=1):
        cells = "".join(cell(c, r, v) for c, v in enumerate(record))
        rows_xml.append(f'<row r="{r}">{cells}</row>')
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f'<dimension ref="A1:D{len(body)}"/>'
        f'<sheetData>{"".join(rows_xml)}</sheetData>'
        "</worksheet>"
    )


PARTS = {
    "[Content_Types].xml": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        "</Types>"
    ),
    "_rels/.rels": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        "</Relationships>"
    ),
    "xl/workbook.xml": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<sheets><sheet name="Grades" sheetId="1" r:id="rId1"/></sheets>'
        "</workbook>"
    ),
    "xl/_rels/workbook.xml.rels": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        "</Relationships>"
    ),
    "xl/styles.xml": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
        '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
        '<borders count="1"><border/></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>'
        "</styleSheet>"
    ),
    "xl/worksheets/sheet1.xml": sheet_xml(),
}


def write_xlsx(path: Path) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, data in PARTS.items():
            zf.writestr(name, data)
    # self-check: reopen and parse every XML part so a malformed file fails loudly
    with zipfile.ZipFile(path) as zf:
        for name in PARTS:
            parseString(zf.read(name))


OUT.mkdir(parents=True, exist_ok=True)
write_csv(OUT / "scores.csv")
write_xlsx(OUT / "scores.xlsx")

passed = sum(1 for _, p, *_ in ROWS if grade(p) != "F")
avg = round(sum(p for _, p, *_ in ROWS) / len(ROWS), 1)
print(f"Wrote {OUT.relative_to(ROOT)}/scores.csv and scores.xlsx "
      f"({len(ROWS)} groups, {passed} passed, class average {avg}).")
print("xlsx XML parts validated OK.")
