#!/usr/bin/env python3
"""Generate the Day-1 "leave a trail" props.

Emits examples/plain-text/:
  course-handbook.docx  — a messy Word document (Track A, the real starting point)
  course-handbook.md    — the same content already converted (fallback, see below)
  survey-responses.csv  — messy data (Track B, for the empirical folks)

Same Nordic Style / ELE37911 world as examples/decrap-me and examples/grades, so
the story carries across the three days. Synthetic — safe to commit and hand out.

The .docx is hand-built with the standard library only (no python-docx): a .docx
is just a zip of XML parts. Reproducible — edit HANDBOOK / ROWS and re-run
`python3 scratch/examples/scripts/make-plaintext-example.py`.

WHY A MARKDOWN FALLBACK SHIPS TOO: converting Word usually wants pandoc, which
may not install on IT-managed laptops. Anyone blocked starts from the .md and
loses nothing — the lesson is what you do *after* the conversion, not the
conversion itself.

TRAPS DELIBERATELY PLANTED (instructor key — see examples/plain-text/README.md):
  1. Assessment weights sum to 90%, not 100%.
  2. "Assessment" and "Grading" overlap AND disagree (40% vs 45% project).
  3. Feedback promised "within two weeks" in one place, "10 working days" elsewhere.
  4. Six deadlines, scattered in prose, in six different date formats.
  5. Inconsistent names/titles (Prof. / Professor / dr.) and citation styles.
"""

import csv
import zipfile
from pathlib import Path
from xml.dom.minidom import parseString

ROOT = Path(__file__).resolve().parents[2]  # scratch/
OUT = ROOT / "examples" / "plain-text"

# ("h1" | "h2" | "p", text)
HANDBOOK = [
    ("h1", "ELE37911 Business Intelligence with Power BI"),
    ("h2", "Course handbook, autumn semester"),
    ("p", "Welcome to ELE37911. This handbook contains the practical information "
          "for the course. Please read it carefully and keep it for reference. "
          "The first lecture takes place on 26 August at 10:15 in room C2-040."),
    ("h2", "About the course"),
    ("p", "The course introduces business intelligence and dashboard design using "
          "Power BI, with the Nordic Style retail dataset as the running case. "
          "Teaching runs over twelve weeks and combines lectures with workshops. "
          "Students work in groups of three or four."),
    ("h2", "Registration"),
    ("p", "Groups must be registered in the course room before 5/9/25. Students "
          "who have not registered a group by that date will be assigned to one."),
    ("h2", "Assessment"),
    ("p", "The course is assessed as follows. The group project counts 40 per cent "
          "of the final mark. The individual written exam counts 30 per cent. "
          "Participation in the workshops counts 20 per cent."),
    ("h2", "Grading"),
    ("p", "Grades are awarded on the standard A-F scale, where E is the lowest "
          "passing grade. As noted above, the group project is the most important "
          "single component and is worth 45% of the final mark, with the written "
          "exam at 30% and workshop participation making up the remainder."),
    ("h2", "Project work"),
    ("p", "The project proposal must be handed in by 12 September. Feedback on "
          "proposals is normally returned within two weeks. The final project "
          "report is due 2025-11-08 at 14:00, and must be submitted through the "
          "course room. Presentations take place in week 46."),
    ("h2", "Examination"),
    ("p", "The written exam is held on December 3rd. It lasts four hours and is "
          "closed book, although a simple calculator is permitted. The exam covers "
          "the whole syllabus, including material from the workshops."),
    ("h2", "Feedback and complaints"),
    ("p", "Students can expect feedback on submitted work within 10 working days. "
          "Complaints about grading follow the standard institutional procedure "
          "and must be submitted in writing."),
    ("h2", "Reading list"),
    ("p", "Chen, L. (2021) Business intelligence in practice. 2nd ed. London."),
    ("p", "Nordhaug, O., \"Data-driven decisions\", Bergen 2019."),
    ("p", "See also the article by Smith et al in the Journal of Business "
          "Analytics, vol 12."),
    ("h2", "Contact"),
    ("p", "Course responsible: Prof. Jonas Moss (jonas.moss@bi.no). Teaching "
          "assistant: dr. A. Nilsen. Administrative questions should be directed "
          "to Professor Moss's assistant."),
]

CSV_HEADER = ["respondent_id", "country", "submitted", "age", "satisfaction",
              "department", "comments"]

# Messy on purpose: country spellings/codes, six date formats, -99 / 999 / "N/A"
# / blank missing values, thousands separators, stray whitespace, and respondent
# R-014 submitted twice (identical row) — a duplicate that must be caught.
ROWS = [
    ["R-001", "Norway", "2025-03-14", "41", "4", "Marketing", "Useful course"],
    ["R-002", "norway", "15/03/2025", "35", "5", "marketing", ""],
    ["R-003", "NO", "March 16 2025", "-99", "3", "Finance", "Too fast"],
    ["R-004", "Sweden", "2025-03-16", "52", "N/A", "Finance ", "  "],
    ["R-005", "SE", "17.03.2025", "29", "4", "Law", "More examples please"],
    ["R-006", "Norge", "2025/03/17", "999", "2", "law", "Room was cold"],
    ["R-007", "Denmark", "18-03-2025", "44", "5", "Leadership", ""],
    ["R-008", "denmark ", "2025-03-18", "", "4", "Leadership", "Good"],
    ["R-009", "Norway", "19/03/2025", "38", "n/a", "Economics", "N/A"],
    ["R-010", "NOR", "2025-03-19", "1 200", "3", "economics", "Typo in slides"],
    ["R-011", "Sweden", "March 20, 2025", "47", "5", "Communication", ""],
    ["R-012", "sweden", "2025-03-20", "33", "4", "communication", "Loved it!"],
    ["R-013", "Finland", "21/03/2025", "-99", "", "Marketing", ""],
    ["R-014", "Norway", "2025-03-21", "40", "4", "Finance", "Solid"],
    ["R-014", "Norway", "2025-03-21", "40", "4", "Finance", "Solid"],
    ["R-015", "FI", "22.03.2025", "56", "2", "Law", "Too much theory"],
    ["R-016", "Norway", "2025-03-22", "31", "5", "Leadership", ""],
    ["R-017", "", "23/03/2025", "36", "3", "", "No department given"],
    ["R-018", "Iceland", "2025-03-23", "49", "4", "Economics", "Fine"],
    ["R-019", "Norway", "March 24 2025", "27", "5", "Marketing", "Best so far"],
    ["R-020", "no", "2025-03-24", "2 500", "1", "Finance", "Did not attend"],
]


def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# --- minimal .docx (Open Packaging Convention: a zip of XML parts) -----------

def paragraph_xml(style, text):
    style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return (f"<w:p>{style_xml}<w:r><w:t xml:space=\"preserve\">"
            f"{esc(text)}</w:t></w:r></w:p>")


def document_xml():
    styles = {"h1": "Heading1", "h2": "Heading2", "p": ""}
    body = "".join(paragraph_xml(styles[kind], text) for kind, text in HANDBOOK)
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f"<w:body>{body}</w:body></w:document>")


STYLES_XML = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
    '<w:name w:val="Normal"/></w:style>'
    '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>'
    '<w:basedOn w:val="Normal"/><w:pPr><w:outlineLvl w:val="0"/></w:pPr>'
    '<w:rPr><w:b/><w:sz w:val="40"/></w:rPr></w:style>'
    '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>'
    '<w:basedOn w:val="Normal"/><w:pPr><w:outlineLvl w:val="1"/></w:pPr>'
    '<w:rPr><w:b/><w:sz w:val="30"/></w:rPr></w:style>'
    "</w:styles>"
)

DOCX_PARTS = {
    "[Content_Types].xml": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        "</Types>"
    ),
    "_rels/.rels": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        "</Relationships>"
    ),
    "word/_rels/document.xml.rels": (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        "</Relationships>"
    ),
    "word/styles.xml": STYLES_XML,
    "word/document.xml": document_xml(),
}


def write_docx(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, data in DOCX_PARTS.items():
            zf.writestr(name, data)
    with zipfile.ZipFile(path) as zf:  # self-check: every part must parse
        for name in DOCX_PARTS:
            parseString(zf.read(name))


def write_markdown(path):
    lines = []
    for kind, text in HANDBOOK:
        prefix = {"h1": "# ", "h2": "## ", "p": ""}[kind]
        lines.append(f"{prefix}{text}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


OUT.mkdir(parents=True, exist_ok=True)
write_docx(OUT / "course-handbook.docx")
write_markdown(OUT / "course-handbook.md")
with (OUT / "survey-responses.csv").open("w", newline="", encoding="utf-8") as fh:
    writer = csv.writer(fh)
    writer.writerow(CSV_HEADER)
    writer.writerows(ROWS)

print(f"Wrote {OUT.relative_to(ROOT)}/: course-handbook.docx (+ .md fallback), "
      f"survey-responses.csv ({len(ROWS)} rows, 1 duplicate).")
print("docx XML parts validated OK.")
