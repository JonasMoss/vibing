"""Build founders-study.zip: a fictional research project for the .gitignore exercise.

Everything in it is made up: names, firms, papers, data. It is built to contain
the things a real project folder holds that should never go into git: personal
data (named transcripts, audio, consent forms, survey e-mails), big files,
copyrighted PDFs, a password, and junk files. See README.md for the key.

    python3 scratch/examples/founders-study/make.py
"""

import io
import random
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "courses" / "2026-10-strategy" / "props" / "founders-study.zip"
TOP = "founders-study"
STAMP = (2026, 3, 20, 9, 0, 0)
rng = random.Random(20261022)
FICTION = "FICTIONAL PRACTICE MATERIAL. Not a real paper, person or firm."


def pdf(lines):
    """A one-page PDF with plain Helvetica text, built by hand (no dependencies)."""
    def esc(s):
        return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    ops, y = ["BT"], 760
    for size, text in lines:
        ops.append(f"/F1 {size} Tf 1 0 0 1 60 {y} Tm ({esc(text)}) Tj")
        y -= size + 10
    ops.append("ET")
    stream = "\n".join(ops).encode("latin-1")
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
        b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out, offsets = io.BytesIO(), []
    out.write(b"%PDF-1.4\n")
    for i, body in enumerate(objs, 1):
        offsets.append(out.tell())
        out.write(f"{i} 0 obj\n".encode() + body + b"\nendobj\n")
    xref = out.tell()
    out.write(f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode())
    for off in offsets:
        out.write(f"{off:010d} 00000 n \n".encode())
    out.write(f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return out.getvalue()


def paper(title, authors, journal):
    words = ("founders pivot identity early-stage ventures sensemaking resources "
             "legitimacy markets imprinting search learning teams").split()
    abstract = " ".join(rng.choice(words) for _ in range(60))
    lines = [(18, title), (12, authors), (11, journal), (10, ""), (10, FICTION), (10, "")]
    lines += [(10, abstract[i:i+90]) for i in range(0, len(abstract), 90)]
    return pdf(lines)


def docx(markdown):
    with tempfile.TemporaryDirectory() as d:
        src, dst = Path(d) / "in.md", Path(d) / "out.docx"
        src.write_text(markdown)
        subprocess.run(["pandoc", str(src), "-o", str(dst)], check=True)
        return dst.read_bytes()


FIRMS = ["Fjordtech", "Havbris", "Lysning", "Nordlys Labs", "Skarv", "Tindra",
         "Vardø Robotics", "Bølge", "Kvist", "Moltebær", "Fyr", "Polarkraft"]
PEOPLE = ["Kari Nordmann", "Ola Nordmann", "Ingrid Bakke", "Lars Fjell", "Siv Holm",
          "Erik Sand", "Mona Dahl", "Tor Lund", "Hanne Vik", "Jon Strand",
          "Eva Berg", "Nils Aas"]


def transcript(person, firm, date):
    turns = []
    for q in ["Tell me how the company started.", "When did you first change direction?",
              "Who did you talk to before deciding?", "What would you do differently?"]:
        turns.append(f"INTERVIEWER: {q}")
        turns.append(f"{person.split()[0].upper()}: " + " ".join(
            rng.choice("we they I the market customers investors pivot product team "
                       "money time early idea changed decided".split()) for _ in range(45)) + ".")
    return (f"Interview with {person}, founder of {firm} AS\nDate: {date}\n"
            f"Phone: +47 9{rng.randint(1000000, 9999999)}\n{FICTION}\n\n" + "\n\n".join(turns) + "\n")


files = {}

files["ABOUT THIS FOLDER.txt"] = (
    f"{FICTION}\n\nA practice project for the course 'AI in the terminal' (BI). It looks like a "
    "real study of how founders change direction in their first two years: interviews, a survey, "
    "literature, a draft. Nothing in it is real.\n").encode()

draft = ("# Founder identity and early pivots\n\n*Draft. " + FICTION + "*\n\n"
         "## Introduction\n\nWhy do some founders change direction early, and others never?\n\n"
         "## Method\n\nWe interviewed 14 founders, including two pilot interviews, and surveyed 220 firms.\n")
files["Draft_v3_FINAL.docx"] = docx(draft)
files["Draft_v3_FINAL (2).docx"] = docx(draft + "\n## Results\n\nTODO\n")
files["draft_v2_old.docx"] = docx(draft.replace("14", "12"))
files["~$aft_v3_FINAL.docx"] = b"\x0bJ. Moss" + bytes(155)
files["interview guide.docx"] = docx(
    "# Interview guide\n\n1. Tell me how the company started.\n2. When did you first change "
    "direction?\n3. Who did you talk to before deciding?\n4. What would you do differently?\n")
files["notes from supervisor meeting.txt"] = (
    "- drop the two pilots? they used the old guide\n- check the survey for duplicates\n"
    "- send Table 2 before Easter\n").encode()

for i, (person, firm) in enumerate(zip(PEOPLE, FIRMS), 1):
    date = f"2026-02-{i+2:02d}"
    files[f"interviews/{date} {person} ({firm}).txt"] = transcript(person, firm, date).encode()
    files[f"interviews/audio/{date}_{person.split()[0].lower()}.m4a"] = bytes(1_500_000)
files["interviews/pilot 1 - Per Olsen.txt"] = transcript("Per Olsen", "Testfirma", "2026-01-20").encode()
files["interviews/pilot 2 - Anne Lie.txt"] = transcript("Anne Lie", "Prøve", "2026-01-22").encode()
files["interviews/consent forms (signed).pdf"] = pdf(
    [(16, "Signed consent forms, interviews Feb 2026"), (10, FICTION)] +
    [(11, f"{p}  -  signed {d}") for p, d in zip(PEOPLE, [f"2026-02-{i+2:02d}" for i in range(12)])])

files["coding/codebook.md"] = (
    "# Codebook\n\n- **TRIGGER**: what made the founder reconsider\n- **ADVICE**: who they asked\n"
    "- **IDENTITY**: talk about who they are as a founder\n- **REGRET**: what they would change\n").encode()
rows = ["participant,code,excerpt"]
for i in range(1, 13):
    for code in rng.sample(["TRIGGER", "ADVICE", "IDENTITY", "REGRET"], 2):
        rows.append(f"F{i:02d},{code},\"we changed the product after talking to customers\"")
files["coding/coded_excerpts.csv"] = ("\n".join(rows) + "\n").encode()

head = "response_id,email,firm_age,team_size,pivoted,wtp_nok"
raw = [head] + [f"{i},founder{i}@example.com,{rng.randint(1,8)},{rng.randint(1,30)},"
                f"{rng.randint(0,1)},{rng.randint(0,5000)}" for i in range(1, 241)]
files["data/survey_export_2026-03-14 (with emails).csv"] = ("\n".join(raw) + "\n").encode()
clean = ["response_id,firm_age,team_size,pivoted,wtp_nok"] + [
    ",".join(r.split(",")[0:1] + r.split(",")[2:]) for r in raw[1:221]]
files["data/survey_clean.csv"] = ("\n".join(clean) + "\n").encode()
reg = ["orgnr,name,founded,employees,revenue_nok,municipality"]
for i in range(160_000):
    reg.append(f"9{i:08d},Firma {i % 997} AS,{2000 + i % 25},{i % 40},{(i * 7919) % 9_000_000},"
               f"{['Oslo','Bergen','Trondheim','Tromsø','Stavanger'][i % 5]}")
files["data/registry_extract_full.csv"] = ("\n".join(reg) + "\n").encode()

papers = [
    ("1-s2.0-S0883902619301234-main.pdf", "When Founders Change Course: A Process Model (fictional)",
     "A. Placeholder and B. Example", "Journal of Imaginary Venturing 34 (2019)"),
    ("ssrn-4412345.pdf", "Identity Anchors and the Timing of Pivots (fictional)",
     "C. Sample", "Working paper, 2023"),
    ("download (3).pdf", "Advice Networks of First-Time Founders (fictional)",
     "D. Dummy and E. Test", "Strategic Pretend Journal 41 (2020)"),
    ("download (4).pdf", "Sensemaking Under Ambiguity in New Ventures (fictional)",
     "F. Mock", "Organization Fiction 12 (2018)"),
    ("case study methods FINAL.pdf", "Building Theories From Pretend Cases (fictional)",
     "G. Stand-In", "Academy of Make-Believe Review 14 (1999)"),
    ("paper.pdf", "Imprinting and Early Strategic Change (fictional)",
     "H. Proxy and I. Dummy", "Journal of Invented Management 50 (2024)"),
]
for name, title, authors, journal in papers:
    files[f"literature/{name}"] = paper(title, authors, journal)

files["analysis/table2.R"] = (
    'd <- read.csv("data/survey_clean.csv")\n'
    'summary(lm(wtp_nok ~ pivoted + firm_age + team_size, data = d))\n').encode()
files["analysis/.Rhistory"] = b'd <- read.csv("data/survey_clean.csv")\nView(d)\nq()\n'
files["api_key.txt"] = b"OPENAI_API_KEY=FAKE-practice-key-0000-not-real\n"
files[".DS_Store"] = bytes(6148)
files["Thumbs.db"] = bytes(4096)

OUT.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name, data in sorted(files.items()):
        z.writestr(zipfile.ZipInfo(f"{TOP}/{name}", STAMP), data, zipfile.ZIP_DEFLATED)
print(f"Wrote {OUT.relative_to(ROOT)}: {len(files)} files, {OUT.stat().st_size // 1024} KB zipped, "
      f"{sum(len(v) for v in files.values()) // 1024 // 1024} MB unzipped")
