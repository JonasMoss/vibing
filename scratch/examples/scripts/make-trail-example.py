#!/usr/bin/env python3
"""Generate the fallback folder for "Leave a trail".

Emits examples/leave-a-trail/messy-project/ and messy-project.zip next to it.
The site build ships the zip as vibing.jonasmoss.com/messy-project.zip.

Who it is for: anyone who reaches "Leave a trail" without a folder of their own to
organise (they never got to the fix step of "Take a paper apart"). It is a small,
realistic research mess: a survey experiment on price framing, cleaned by hand in
Excel, analysed by one of two scripts, written up in Word.

Synthetic. Standard library only, and the analysis script it ships is standard
library only too, so it runs on any Python 3. Reproducible: re-run this script
and you get the same bytes (the zip timestamps are fixed).

TRAPS DELIBERATELY PLANTED (instructor key: examples/leave-a-trail/README.md):
  1. data_clean_FINAL.csv was made by hand, with no script. notes.txt documents
     one rule (drop speeders, under 60 seconds). A second rule is undocumented:
     three willingness-to-pay answers above 5,000 NOK were also deleted. Only a
     comparison of the raw and cleaned files reveals it.
  2. The conclusion depends on that undocumented rule (see the two tables).
  3. Two tables: table1.txt (current) and "table1 (copy).txt" (older, made
     before the outliers were removed). Nothing says which is which.
  4. analysis.py is dead: it reads data.csv, which does not exist.
  5. draft_v3.docx describes only the speeder rule and reports the older N.
  6. The cleaned file uses semicolons, as Norwegian Excel saves CSV.
"""

import csv
import io
import math
import random
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.dom.minidom import parseString

ROOT = Path(__file__).resolve().parents[2]  # scratch/
BASE = ROOT / "examples" / "leave-a-trail"
OUT = BASE / "messy-project"
ZIP = BASE / "messy-project.zip"

COLUMNS = ["respondent_id", "condition", "duration_sec", "wtp_nok", "intent", "age"]
SPEEDER_SECONDS = 60
OUTLIER_NOK = 5000


# --- the data ----------------------------------------------------------------

def make_rows():
    rng = random.Random(2026)
    rows = []
    for i in range(1, 241):
        condition = rng.choice(["monthly", "yearly"])
        speeder = rng.random() < 0.05
        if speeder:
            duration = rng.randint(22, 58)
            wtp = rng.randint(0, 40) * 50
            intent = rng.randint(1, 7)
        else:
            duration = int(rng.lognormvariate(math.log(420), 0.4))
            mean = 545 if condition == "monthly" else 475
            wtp = max(0, round(rng.gauss(mean, 170) / 10) * 10)
            intent = min(7, max(1, round(rng.gauss(4 + (wtp - 500) / 250, 1.2))))
        rows.append({
            "respondent_id": f"R{1000 + i}",
            "condition": condition,
            "duration_sec": duration,
            "wtp_nok": wtp,
            "intent": intent,
            "age": rng.randint(19, 67),
        })
    # Three answers typed as nonsense, all in the yearly condition, all from
    # respondents who took their time (so the speeder rule does not catch them).
    slow_yearly = [r for r in rows if r["condition"] == "yearly"
                   and r["duration_sec"] >= SPEEDER_SECONDS]
    for row, value in zip(slow_yearly[5::29][:3], [9999, 25000, 7500]):
        row["wtp_nok"] = value
    return rows


def csv_text(rows, delimiter):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=COLUMNS, delimiter=delimiter,
                            lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


# --- the scripts that ship in the folder ---------------------------------------

ANALYSIS_OLD = '''\
# first try - means by group
import csv

rows = list(csv.DictReader(open("data.csv")))
for cond in ["monthly", "yearly"]:
    x = [float(r["wtp_nok"]) for r in rows if r["condition"] == cond]
    print(cond, sum(x) / len(x))
'''

ANALYSIS_V2 = '''\
# analysis v2 - this is the one for table 1
import csv
import random
import statistics

rows = list(csv.DictReader(open("data_clean_FINAL.csv", encoding="utf-8"), delimiter=";"))

groups = {}
for r in rows:
    groups.setdefault(r["condition"], []).append(float(r["wtp_nok"]))
monthly, yearly = groups["monthly"], groups["yearly"]

diff = statistics.mean(monthly) - statistics.mean(yearly)

# permutation test, two-sided
random.seed(1)
pooled = monthly + yearly
hits = 0
draws = 10000
for _ in range(draws):
    random.shuffle(pooled)
    d = statistics.mean(pooled[:len(monthly)]) - statistics.mean(pooled[len(monthly):])
    if abs(d) >= abs(diff):
        hits += 1
p = hits / draws

lines = [
    "Table 1. Willingness to pay (NOK) by price framing",
    "",
    "condition     n     mean      sd",
]
for name, x in [("monthly", monthly), ("yearly", yearly)]:
    lines.append(f"{name:<10} {len(x):>4} {statistics.mean(x):>8.1f} {statistics.stdev(x):>7.1f}")
lines += [
    "",
    f"N = {len(rows)}",
    f"difference (monthly - yearly): {diff:.1f} NOK",
    f"permutation p-value ({draws:,} draws): {p:.3f}",
]
open("table1.txt", "w", encoding="utf-8").write("\\n".join(lines) + "\\n")
print("\\n".join(lines))
'''

NOTES = """\
14.03 exported from nettskjema -> survey_export_2026-03-14.csv
removed the speeders (under 1 min) in excel -> data_clean_FINAL.csv
table 1 = analysis_v2 (NOT the old one)
the crazy WTP ones?? ask Kari
send draft to Kari before easter
"""


def run_analysis(clean_rows):
    """Run the shipped analysis_v2.py on clean_rows; return table1.txt's text."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "data_clean_FINAL.csv").write_text(csv_text(clean_rows, ";"),
                                                  encoding="utf-8", newline="")
        (tmp / "analysis_v2.py").write_text(ANALYSIS_V2, encoding="utf-8")
        subprocess.run([sys.executable, "analysis_v2.py"], cwd=tmp, check=True,
                       capture_output=True)
        return (tmp / "table1.txt").read_text(encoding="utf-8")


def table_value(table, prefix):
    for line in table.splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[-1].split("=", 1)[-1].strip()
    raise ValueError(prefix)


# --- the Word draft (hand-built .docx: a zip of XML parts) ---------------------

def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def docx_parts(paragraphs):
    styles = {"h1": "Heading1", "h2": "Heading2", "p": ""}
    body = ""
    for kind, text in paragraphs:
        style = styles[kind]
        ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
        body += f'<w:p>{ppr}<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'
    w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    return {
        "[Content_Types].xml": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
            "</Types>"),
        "_rels/.rels": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            "</Relationships>"),
        "word/_rels/document.xml.rels": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            "</Relationships>"),
        "word/styles.xml": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:styles xmlns:w="{w}">'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
            '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>'
            '<w:basedOn w:val="Normal"/><w:pPr><w:outlineLvl w:val="0"/></w:pPr>'
            '<w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>'
            '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>'
            '<w:basedOn w:val="Normal"/><w:pPr><w:outlineLvl w:val="1"/></w:pPr>'
            '<w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>'
            "</w:styles>"),
        "word/document.xml": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:document xmlns:w="{w}"><w:body>{body}</w:body></w:document>'),
    }


def docx_bytes(paragraphs):
    buf = io.BytesIO()
    parts = docx_parts(paragraphs)
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, data in parts.items():
            zf.writestr(zipfile.ZipInfo(name, (2026, 3, 20, 9, 0, 0)), data)
    with zipfile.ZipFile(io.BytesIO(buf.getvalue())) as zf:  # every part must parse
        for name in parts:
            parseString(zf.read(name))
    return buf.getvalue()


# --- build -----------------------------------------------------------------------

def main():
    rows = make_rows()
    no_speeders = [r for r in rows if r["duration_sec"] >= SPEEDER_SECONDS]
    clean = [r for r in no_speeders if r["wtp_nok"] <= OUTLIER_NOK]

    table_now = run_analysis(clean)
    table_old = run_analysis(no_speeders)

    n_old = table_value(table_old, "N =")
    diff_now = table_value(table_now, "difference")
    p_now = table_value(table_now, "permutation")

    draft = [
        ("h1", "Monthly or yearly? Price framing and willingness to pay"),
        ("p", "Draft v3. Kari Nordmann and [me]. Not for circulation."),
        ("h2", "Method"),
        ("p", "We ran an online survey experiment in March 2026. Respondents were "
              "randomly shown a subscription price either per month or per year and "
              "asked the most they would pay per year (NOK). We removed respondents "
              "who completed the survey in under 60 seconds."),
        ("h2", "Results"),
        ("p", f"The final sample has N = {n_old} respondents. Respondents who saw the "
              f"monthly price were willing to pay {diff_now} more per year than "
              f"those who saw the yearly price (permutation test, p = {p_now}). "
              "See Table 1."),
        ("h2", "Discussion"),
        ("p", "TODO"),
    ]

    files = {
        "survey_export_2026-03-14.csv": csv_text(rows, ","),
        "data_clean_FINAL.csv": csv_text(clean, ";"),
        "analysis.py": ANALYSIS_OLD,
        "analysis_v2.py": ANALYSIS_V2,
        "table1.txt": table_now,
        "table1 (copy).txt": table_old,
        "notes.txt": NOTES,
    }

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for name, text in files.items():
        (OUT / name).write_text(text, encoding="utf-8", newline="")
    (OUT / "draft_v3.docx").write_bytes(docx_bytes(draft))

    # Fixed timestamps, sorted names: the zip is byte-for-byte reproducible.
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(OUT.iterdir()):
            info = zipfile.ZipInfo(f"messy-project/{path.name}", (2026, 3, 20, 9, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())

    print(f"Wrote {OUT.relative_to(ROOT)}/ ({len(files) + 1} files) and {ZIP.relative_to(ROOT)}")
    print(f"raw {len(rows)}, speeders dropped {len(rows) - len(no_speeders)}, "
          f"outliers dropped {len(no_speeders) - len(clean)}, clean {len(clean)}")
    print("\n--- table1.txt (current)\n" + table_now)
    print("--- table1 (copy).txt (before outliers were removed)\n" + table_old)


if __name__ == "__main__":
    main()
