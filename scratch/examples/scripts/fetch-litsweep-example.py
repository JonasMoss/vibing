#!/usr/bin/env python3
"""Fetch the Day-2 literature-sweep corpus: 12 open-access PDFs on AI in higher education.

Emits examples/litsweep/pdfs/*.pdf, examples/litsweep/pdfs/SOURCES.md and
examples/litsweep.zip (the file participants download; copy it into the
course's props/ folder).

Instructor key — what each paper says, and which ones genuinely disagree:
examples/litsweep/README.md. Read it before teaching the block.

WHY A SCRIPT AND NOT COMMITTED PDFs
  The PDFs are binary and third-party copyrighted, so examples/litsweep/pdfs/ is
  gitignored — Day 2 teaches exactly that distinction ("text is tracked, binaries
  are not") in the same block that hands this folder out. Committing ten PDFs
  would contradict the lesson on the same slide. The URL list below *is* the
  tracked artefact: plain text, diffable, re-runnable.

LICENCES
  Every paper here is open access under a Creative Commons licence that permits
  verbatim redistribution with attribution: eight are CC BY 4.0 and four are
  CC BY-NC-ND 4.0. NC-ND permits sharing the unmodified PDF for non-commercial
  purposes — which a free course-materials download is — but it forbids adapting
  it, so do not re-compress, crop, or re-typeset those four. The generated
  SOURCES.md carries the attribution the licences require and ships inside the
  zip. Do not remove it.

RE-RUNNING
  python3 scratch/examples/scripts/fetch-litsweep-example.py           # skip files already verified
  python3 scratch/examples/scripts/fetch-litsweep-example.py --force   # re-download everything
  python3 scratch/examples/scripts/fetch-litsweep-example.py --check   # verify what's on disk, fetch nothing

  Every download is verified before it counts: %PDF magic bytes, a %%EOF trailer,
  a minimum size, a minimum page count, and a fingerprint string that must appear
  in the extracted text. A file that fails any check is deleted and the script
  exits non-zero naming the paper, the DOI, the URL and what went wrong. This is
  not paranoia: nature.com/articles/XXX.pdf used to answer HTTP 200 with an HTML
  interstitial, and a naive fetcher saved a login page as a .pdf and reported
  success. See examples/references/README.md for that story.

PUBLISHER ACCESS, AS OF 2026-08-09 (this is why the URLs look the way they do)
  works for robots  : nature.com, journals.plos.org, frontiersin.org, europepmc.org
  blocks robots     : link.springer.com and *.springeropen.com (JS challenge),
                      sciencedirect.com / cell.com (403), pnas.org (Cloudflare),
                      pmc.ncbi.nlm.nih.gov (proof-of-work cookie), mdpi.com (403)
  So the Springer-hosted CC BY papers are fetched from the Internet Archive's
  capture of the publisher's own PDF endpoint (the /<timestamp>id_/ form returns
  the archived bytes unrewritten), and the Elsevier/PNAS ones from Europe PMC's
  ?pdf=render endpoint. Both are legitimate routes to the version of record; the
  fingerprint check below confirms each file really is the paper it claims to be.
"""

import argparse
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # scratch/
OUT = ROOT / "examples" / "litsweep" / "pdfs"
ZIP = ROOT / "examples" / "litsweep.zip"

# Pretending to be a browser is not a trick here — several of these publishers
# serve the same public CC-licensed PDF to a browser and a challenge page to a
# bare urllib UA. We are not evading a paywall; there isn't one.
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
WAYBACK = "https://web.archive.org/web/2024id_/"

# Every field below was verified on 2026-08-09: citation against Crossref,
# licence against Crossref + the licence statement printed in the PDF itself,
# and the PDF downloaded, opened and read. `must_contain` is a string that
# appears in the real article's text and nowhere in an error page.
PAPERS = [
    {
        "file": "zawacki-richter-2019.pdf",
        "cite": ("Zawacki-Richter, O., Marín, V. I., Bond, M., & Gouverneur, F. (2019). "
                 "Systematic review of research on artificial intelligence applications in "
                 "higher education – where are the educators? International Journal of "
                 "Educational Technology in Higher Education, 16, 39."),
        "doi": "10.1186/s41239-019-0171-0",
        "licence": "CC BY 4.0",
        "urls": [
            WAYBACK + "https://educationaltechnologyjournal.springeropen.com/track/pdf/10.1186/s41239-019-0171-0",
            "https://educationaltechnologyjournal.springeropen.com/track/pdf/10.1186/s41239-019-0171-0",
        ],
        "min_pages": 20,
        "min_bytes": 400_000,
        "must_contain": "where are the educators",
    },
    {
        "file": "crompton-burke-2023.pdf",
        "cite": ("Crompton, H., & Burke, D. (2023). Artificial intelligence in higher "
                 "education: the state of the field. International Journal of Educational "
                 "Technology in Higher Education, 20, 22."),
        "doi": "10.1186/s41239-023-00392-8",
        "licence": "CC BY 4.0",
        "urls": [
            WAYBACK + "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00392-8",
            "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00392-8",
        ],
        "min_pages": 15,
        "min_bytes": 800_000,
        "must_contain": "the state of the field",
    },
    {
        "file": "chan-2023.pdf",
        "cite": ("Chan, C. K. Y. (2023). A comprehensive AI policy education framework for "
                 "university teaching and learning. International Journal of Educational "
                 "Technology in Higher Education, 20, 38."),
        "doi": "10.1186/s41239-023-00408-3",
        "licence": "CC BY 4.0",
        "urls": [
            WAYBACK + "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00408-3",
            "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00408-3",
        ],
        "min_pages": 15,
        "min_bytes": 500_000,
        "must_contain": "AI policy education framework",
    },
    {
        "file": "chan-hu-2023.pdf",
        "cite": ("Chan, C. K. Y., & Hu, W. (2023). Students' voices on generative AI: "
                 "perceptions, benefits, and challenges in higher education. International "
                 "Journal of Educational Technology in Higher Education, 20, 43."),
        "doi": "10.1186/s41239-023-00411-8",
        "licence": "CC BY 4.0",
        "urls": [
            WAYBACK + "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00411-8",
            "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00411-8",
        ],
        "min_pages": 12,
        "min_bytes": 500_000,
        "must_contain": "perceptions, benefits, and challenges",
    },
    {
        "file": "bearman-2023.pdf",
        "cite": ("Bearman, M., Ryan, J., & Ajjawi, R. (2023). Discourses of artificial "
                 "intelligence in higher education: a critical literature review. Higher "
                 "Education, 86(2), 369–385."),
        "doi": "10.1007/s10734-022-00937-2",
        "licence": "CC BY 4.0",
        "urls": [
            WAYBACK + "https://link.springer.com/content/pdf/10.1007/s10734-022-00937-2.pdf",
            "https://link.springer.com/content/pdf/10.1007/s10734-022-00937-2.pdf",
        ],
        "min_pages": 12,
        "min_bytes": 300_000,
        "must_contain": "critical literature review",
    },
    {
        "file": "bond-2024.pdf",
        "cite": ("Bond, M., Khosravi, H., De Laat, M., Bergdahl, N., Negrea, V., Oxley, E., "
                 "Pham, P., Chong, S. W., & Siemens, G. (2024). A meta systematic review of "
                 "artificial intelligence in higher education: a call for increased ethics, "
                 "collaboration, and rigour. International Journal of Educational Technology "
                 "in Higher Education, 21, 4."),
        "doi": "10.1186/s41239-023-00436-z",
        "licence": "CC BY 4.0",
        "urls": [
            WAYBACK + "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00436-z",
            "https://educationaltechnologyjournal.springeropen.com/counter/pdf/10.1186/s41239-023-00436-z",
        ],
        "min_pages": 30,
        "min_bytes": 1_000_000,
        "must_contain": "meta systematic review",
    },
    {
        "file": "basic-2023.pdf",
        "cite": ("Bašić, Ž., Banovac, A., Kružić, I., & Jerković, I. (2023). ChatGPT-3.5 as "
                 "writing assistance in students' essays. Humanities and Social Sciences "
                 "Communications, 10, 750."),
        "doi": "10.1057/s41599-023-02269-7",
        "licence": "CC BY 4.0",
        "urls": ["https://www.nature.com/articles/s41599-023-02269-7.pdf"],
        "min_pages": 4,
        "min_bytes": 200_000,
        "must_contain": "writing assistance in students",
    },
    {
        "file": "kestin-2025.pdf",
        "cite": ("Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI "
                 "tutoring outperforms in-class active learning: an RCT introducing a novel "
                 "research-based design in an authentic educational setting. Scientific "
                 "Reports, 15, 17458."),
        "doi": "10.1038/s41598-025-97652-6",
        "licence": "CC BY-NC-ND 4.0",
        "urls": ["https://www.nature.com/articles/s41598-025-97652-6.pdf"],
        "min_pages": 8,
        "min_bytes": 500_000,
        "must_contain": "outperforms in-class active learning",
    },
    {
        "file": "bastani-2025.pdf",
        "cite": ("Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. "
                 "(2025). Generative AI without guardrails can harm learning: Evidence from "
                 "high school mathematics. Proceedings of the National Academy of Sciences, "
                 "122(26), e2422633122."),
        "doi": "10.1073/pnas.2422633122",
        "licence": "CC BY-NC-ND 4.0",
        "urls": ["https://europepmc.org/articles/PMC12232635?pdf=render"],
        "min_pages": 8,
        "min_bytes": 800_000,
        "must_contain": "without guardrails can harm learning",
    },
    {
        "file": "scarfe-2024.pdf",
        "cite": ("Scarfe, P., Watcham, K., Clarke, A., & Roesch, E. (2024). A real-world test "
                 "of artificial intelligence infiltration of a university examinations system: "
                 "A \"Turing Test\" case study. PLOS ONE, 19(6), e0305354."),
        "doi": "10.1371/journal.pone.0305354",
        "licence": "CC BY 4.0",
        "urls": [
            "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0305354&type=printable",
        ],
        "min_pages": 10,
        "min_bytes": 500_000,
        "must_contain": "infiltration of a university examinations system",
    },
    {
        "file": "liang-2023.pdf",
        "cite": ("Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors "
                 "are biased against non-native English writers. Patterns, 4(7), 100779."),
        "doi": "10.1016/j.patter.2023.100779",
        "licence": "CC BY-NC-ND 4.0",
        "urls": ["https://europepmc.org/articles/PMC10382961?pdf=render"],
        "min_pages": 4,
        "min_bytes": 300_000,
        "must_contain": "biased against non-native english writers",
    },
    {
        # RETRACTED on 2026-04-22 — deliberately included. See the instructor key.
        "file": "wang-fan-2025.pdf",
        "cite": ("Wang, J., & Fan, W. (2025). RETRACTED ARTICLE: The effect of ChatGPT on "
                 "students' learning performance, learning perception, and higher-order "
                 "thinking: insights from a meta-analysis. Humanities and Social Sciences "
                 "Communications, 12, 621. Retracted 22 April 2026 "
                 "(Retraction Note: doi:10.1057/s41599-026-07310-z)."),
        "doi": "10.1057/s41599-025-04787-y",
        "licence": "CC BY-NC-ND 4.0",
        "urls": ["https://www.nature.com/articles/s41599-025-04787-y.pdf"],
        "min_pages": 15,
        "min_bytes": 500_000,
        "must_contain": "insights from a meta-analysis",
    },
]


# --- verification -----------------------------------------------------------

HAVE_PDFTOTEXT = shutil.which("pdftotext") is not None
HAVE_PDFINFO = shutil.which("pdfinfo") is not None


def page_count(path: Path) -> int | None:
    """Page count via poppler, else via pypdf, else None (check is skipped)."""
    if HAVE_PDFINFO:
        out = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True)
        for line in out.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split()[1])
    try:
        from pypdf import PdfReader  # type: ignore
        return len(PdfReader(str(path)).pages)
    except Exception:
        return None


def extract_text(path: Path) -> str | None:
    """Extracted text via poppler, else via pypdf, else None (check is skipped)."""
    if HAVE_PDFTOTEXT:
        out = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True)
        if out.returncode == 0:
            return out.stdout
    try:
        from pypdf import PdfReader  # type: ignore
        return "\n".join(p.extract_text() or "" for p in PdfReader(str(path)).pages)
    except Exception:
        return None


def verify(path: Path, paper: dict) -> list[str]:
    """Return a list of problems. Empty list means the file is a real, right PDF.

    The structural checks always run (stdlib only). The page-count and text
    checks need poppler-utils or pypdf; if neither is installed they are skipped
    silently here and announced once, loudly, at the top of the run — a check
    that quietly did not happen is worse than no check at all.
    """
    problems: list[str] = []
    raw = path.read_bytes()

    if not raw.startswith(b"%PDF"):
        head = raw[:60].decode("utf-8", "replace").replace("\n", " ")
        return [f"not a PDF: file starts with {head!r} (an HTML error page?)"]

    if b"%%EOF" not in raw[-4096:]:
        problems.append("no %%EOF trailer in the last 4 KB — truncated download")
    if len(raw) < paper["min_bytes"]:
        problems.append(f"only {len(raw):,} bytes, expected at least {paper['min_bytes']:,}")

    pages = page_count(path)
    if pages is not None and pages < paper["min_pages"]:
        problems.append(f"{pages} pages, expected at least {paper['min_pages']}")

    text = extract_text(path)
    if text is not None:
        flat = " ".join(text.lower().split())
        if len(flat) < 3000:
            problems.append(f"only {len(flat)} characters of extractable text — scanned image?")
        if paper["must_contain"].lower() not in flat:
            problems.append(f"text does not contain {paper['must_contain']!r} — wrong paper?")

    return problems


def thin_verification_notes() -> list[str]:
    """Say out loud which checks this machine cannot perform."""
    notes = []
    if not (HAVE_PDFINFO or _has_pypdf()):
        notes.append("no pdfinfo and no pypdf — page counts will NOT be checked")
    if not (HAVE_PDFTOTEXT or _has_pypdf()):
        notes.append("no pdftotext and no pypdf — text and fingerprints will NOT be checked")
    if notes:
        notes.append("fix with:  pip install pypdf   (or install poppler-utils)")
    return notes


def _has_pypdf() -> bool:
    try:
        import pypdf  # noqa: F401
        return True
    except Exception:
        return False


# --- fetch ------------------------------------------------------------------

def download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=180) as r, dest.open("wb") as fh:
        shutil.copyfileobj(r, fh)


def fetch(paper: dict, force: bool, check_only: bool) -> bool:
    dest = OUT / paper["file"]
    label = f"{paper['file']}  ({paper['doi']})"

    if dest.exists() and not force:
        problems = verify(dest, paper)
        if not problems:
            print(f"  ok (already present)  {label}")
            return True
        if check_only:
            print(f"  BAD  {label}\n" + "".join(f"       - {p}\n" for p in problems), end="")
            return False
        print(f"  re-fetching (on disk copy failed: {problems[0]})  {label}")

    if check_only:
        print(f"  MISSING  {label}")
        return False

    errors = []
    for url in paper["urls"]:
        tmp = dest.with_suffix(".part")
        try:
            download(url, tmp)
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as err:
            errors.append(f"{url}\n         download failed: {err}")
            tmp.unlink(missing_ok=True)
            continue
        problems = verify(tmp, paper)
        if problems:
            errors.append(f"{url}\n         " + "\n         ".join(problems))
            tmp.unlink(missing_ok=True)
            continue
        tmp.replace(dest)
        print(f"  fetched  {label}  ({dest.stat().st_size:,} bytes)")
        return True

    print(f"\n!! FAILED: {paper['cite']}", file=sys.stderr)
    print(f"   DOI     : https://doi.org/{paper['doi']}", file=sys.stderr)
    print(f"   Licence : {paper['licence']}", file=sys.stderr)
    for e in errors:
        print(f"   tried   : {e}", file=sys.stderr)
    print("   Fix: open the DOI in a browser, save the PDF as "
          f"examples/litsweep/pdfs/{paper['file']}, and update the URL in this script.\n",
          file=sys.stderr)
    return False


# --- outputs ----------------------------------------------------------------

SOURCES_HEADER = """# Sources and licences

Twelve open-access papers on artificial intelligence in higher education, for the
literature-sweep exercise. Every one is redistributed here under the Creative
Commons licence its publisher applied to it, unmodified. This file is the
attribution those licences require — keep it with the PDFs.

None of these were written for this course. If you quote or cite anything you
find here, cite the paper, not the folder.

"""


def write_sources(path: Path) -> None:
    lines = [SOURCES_HEADER]
    for p in PAPERS:
        lines.append(f"## `{p['file']}`\n")
        lines.append(f"{p['cite']}\n")
        lines.append(f"- DOI: <https://doi.org/{p['doi']}>")
        lines.append(f"- Licence: {p['licence']} "
                     f"(<https://creativecommons.org/licenses/"
                     f"{p['licence'].removeprefix('CC ').removesuffix(' 4.0').lower()}/4.0/>)\n")
    path.write_text("\n".join(lines), encoding="utf-8")


def build_zip() -> None:
    """Emit examples/litsweep.zip, unpacking as a litsweep/ folder.

    Built here rather than by hand because a separately-made zip WILL drift from
    the folder. Note what is *not* in it: examples/litsweep/README.md is the
    instructor key and must never ship to participants.
    """
    ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(OUT / "SOURCES.md", "litsweep/SOURCES.md")
        for p in PAPERS:
            zf.write(OUT / p["file"], f"litsweep/{p['file']}")
    with zipfile.ZipFile(ZIP) as zf:
        bad = zf.testzip()
        if bad:
            sys.exit(f"!! examples/litsweep.zip is corrupt at {bad}")
        assert len(zf.namelist()) == len(PAPERS) + 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--force", action="store_true", help="re-download everything")
    ap.add_argument("--check", action="store_true", help="verify what is on disk, fetch nothing")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    for note in thin_verification_notes():
        print(f"!! {note}")

    print(f"{len(PAPERS)} papers -> {OUT.relative_to(ROOT)}")
    results = [fetch(p, args.force, args.check) for p in PAPERS]
    if not all(results):
        n = results.count(False)
        print(f"\n{n} of {len(PAPERS)} papers could not be verified. Nothing was zipped.",
              file=sys.stderr)
        return 1

    if args.check:
        print(f"\nAll {len(PAPERS)} PDFs present and verified.")
        return 0

    write_sources(OUT / "SOURCES.md")
    build_zip()

    total = sum((OUT / p["file"]).stat().st_size for p in PAPERS)
    print(f"\nWrote {OUT.relative_to(ROOT)}/SOURCES.md")
    print(f"Wrote {ZIP.relative_to(ROOT)} "
          f"({ZIP.stat().st_size / 1e6:.1f} MB; {total / 1e6:.1f} MB of PDFs)")
    print("Copy it into the course's props/ folder to hand it out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
