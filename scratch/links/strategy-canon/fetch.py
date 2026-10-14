#!/usr/bin/env python3
"""Fetch the strategic-management reading pile into links/strategy-canon/pdfs/.

This is background reading for the instructor, not participant material. The
annotated index — what each paper argues, what it debunks, suggested reading
order — is links/strategy-canon/README.md. Read that, not this file.

WHY A SCRIPT AND NOT COMMITTED PDFs
  Same reason as scratch/examples/scripts/fetch-litsweep-example.py: these are third-party
  copyrighted journal articles. Unlike the litsweep corpus, none of them is
  Creative Commons — they are paywalled classics from 1979-2017 that happen to
  be posted on faculty pages, university course pages and institutional
  repositories. Downloading one to read is ordinary scholarly practice;
  committing nineteen of them into a public GitHub repo that serves
  vibing.jonasmoss.com is republication, and the course teaches the opposite
  on Day 2. So links/strategy-canon/pdfs/ is gitignored and this URL list is
  the tracked artefact.

  If a link rots, do not go hunting on Sci-Hub. Every one of these has a DOI in
  the README; BI's library subscription resolves all of them.

SOURCE POLICY
  Every URL below is a publisher open-access page, an author's own faculty or
  personal page, a university course reading page, an institutional repository,
  or an Internet Archive capture of one of those. No paywall-circumvention
  sites were used to build this list, and none should be added to it.

RE-RUNNING
  python3 scratch/links/strategy-canon/fetch.py           # skip files already verified
  python3 scratch/links/strategy-canon/fetch.py --force   # re-download everything
  python3 scratch/links/strategy-canon/fetch.py --check   # verify what's on disk, fetch nothing

  Every download is verified before it counts: %PDF magic bytes, a minimum
  size, a minimum page count, and — for files with a text layer — a fingerprint
  string that must appear in the extracted text. Two of these (Roll 1986,
  Barney 1991) are image-only library scans with no text layer at all, so they
  are fingerprinted on page count alone and flagged NO-TEXT. That is not a
  failure; it is why `grep` will find nothing in them.

  A file that fails any check is deleted and the script exits non-zero naming
  the paper, the DOI, the URL and what went wrong. This matters: several of
  these publishers answer HTTP 200 with an HTML login interstitial, and a naive
  fetcher will happily save a login page as a .pdf and report success.

  Nine of the nineteen come from web.archive.org, which rate-limits hard when
  you pull that many files in a row: it answers 503, and occasionally a bogus
  404, for captures that demonstrably exist. Those are retried with a growing
  delay (5s, 15s, 40s) and then from alternative captures, so a --force run
  takes a couple of minutes and will print "retrying" a few times. That is
  normal. A paper only counts as failed once every URL is exhausted.

KNOWN QUIRKS, AS OF 2026-09-20
  wiley, informs, sloanreview, sage : 403 to any script, including with browser
                                      headers. Nothing here comes from them.
  europepmc.org ?pdf=render         : 403 to scripts, and it returns a ~5 KB
                                      HTML error page with HTTP 200 — exactly
                                      the trap the size check exists to catch.
  terry.uga.edu, repository.lib.fsu.edu, pages.stern.nyu.edu/~eofek
                                    : origin unreachable or moved; fetched from
                                      the Internet Archive `id_`/`if_` raw
                                      capture endpoint, which returns the
                                      archived bytes unrewritten.
  roll-1986.pdf                     : a 2-up scan rotated 90 degrees. Readable,
                                      but rotate it in your viewer.
  tripsas-gavetti-2000.pdf          : HBS working paper 00-067, not the SMJ
                                      version of record. Same argument, and the
                                      only legitimately free copy.
  king-baatartogtokh-2015           : NOT here. MIT Sloan Management Review is
                                      hard-paywalled with no repository copy
                                      anywhere. King's 2017 EIX piece, which is
                                      open access and makes the same argument in
                                      four pages, is fetched instead.
"""

import argparse
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

DEST = Path(__file__).resolve().parent / "pdfs"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# key, (url, fallback url, ...), doi, min_pages, fingerprint
#
# The URL field is a tuple tried in order. Fallbacks are alternative Wayback
# captures of the same origin file, added after a --force run showed the single
# "best" capture 503-ing under load. fingerprint is a lowercased substring that
# must appear in the extracted page-1/2 text; None means the file is an
# image-only scan with no text layer, so only magic bytes and page count can be
# checked.
PAPERS = [
    # --- Luck versus skill -------------------------------------------------
    (
        "denrell-liu-2012",
        (
            "https://web.archive.org/web/2018id_/https://www.pnas.org/content/pnas/109/24/9331.full.pdf",
            "https://web.archive.org/web/20180926170526id_/http://www.pnas.org/content/pnas/109/24/9331.full.pdf",
            "https://web.archive.org/web/20210812181320id_/https://www.pnas.org/content/pnas/109/24/9331.full.pdf",
        ),
        "10.1073/pnas.1116048109",
        5,
        "extreme performance indicates unreliability",
    ),
    (
        "quigley-hambrick-2015",
        (
            "https://web.archive.org/web/20240418035712id_/https://www.terry.uga.edu/wp-content/uploads/2015-QuigleyHambrick-CEO-Effect-Increased.pdf",
        ),
        "10.1002/smj.2258",
        9,
        "ceo effect",
    ),
    # --- Acquisitions and diversification ----------------------------------
    (
        "king-et-al-2004",
        (
            "https://web.archive.org/web/20250614052951if_/https://repository.lib.fsu.edu/islandora/object/fsu:536625/datastream/PDF/download",
        ),
        "10.1002/smj.371",
        13,
        "post-acquisition performance",
    ),
    (
        "roll-1986",
        (
            "https://www.anderson.ucla.edu/documents/areas/fac/finance/1986-1.pdf",
        ),
        "10.1086/296325",
        11,
        None,  # image-only scan, rotated 90 degrees
    ),
    (
        "campa-kedia-2002",
        (
            "https://web.archive.org/web/20220124000719if_/http://pages.stern.nyu.edu/~eofek/PhD/papers/CK_Explaining_JF.pdf",
            "https://web.archive.org/web/20170813081230if_/http://pages.stern.nyu.edu/~eofek/PhD/papers/CK_Explaining_JF.pdf",
            "https://web.archive.org/web/20030714062238if_/http://pages.stern.nyu.edu:80/~eofek/PhD/papers/CK_Explaining_JF.pdf",
        ),
        "10.1111/1540-6261.00476",
        30,
        "explaining the diversification discount",
    ),
    (
        "villalonga-2004",
        (
            "https://pages.stern.nyu.edu/~bvillalo/Villalonga_DivPremium_JF2004.pdf",
        ),
        "10.1111/j.1540-6261.2004.00640.x",
        26,
        "diversification discount or premium",
    ),
    (
        "golder-tellis-1993",
        (
            "https://gtellis.net/wp-content/uploads/2020/09/pioneering-advantage-marketing-logic-or-marketing-legend.pdf",
        ),
        "10.2307/3172825",
        13,
        "marketing logic or marketing legend",
    ),
    # --- Incumbents and technological transitions --------------------------
    (
        "henderson-clark-1990",
        (
            "http://www.iot.ntnu.no/innovation/norsi-pims-courses/tushman/Handerson%20&%20Clark%20(1990).pdf",
        ),
        "10.2307/2393549",
        20,
        "architectural innovation",
    ),
    (
        "christensen-bower-1996",
        (
            "http://www.iot.ntnu.no/innovation/norsi-pims-courses/tushman/Christensen%20&%20Bower%20(1996).pdf",
        ),
        "10.1002/(SICI)1097-0266(199603)17:3<197::AID-SMJ804>3.0.CO;2-U",
        20,
        "customer power",
    ),
    (
        "tripsas-gavetti-2000",
        (
            "https://www.hbs.edu/ris/Publication%20Files/00-067_cdcafdf1-d946-44ec-96ad-558ad606477d.pdf",
        ),
        "10.1002/1097-0266(200010/11)21:10/11<1147::AID-SMJ128>3.0.CO;2-R",
        25,
        "evidence from digital imaging",
    ),
    (
        "king-2017-allegory",
        (
            "https://eiexchange.com/api/submissions/299?type=pdf",
        ),
        "10.17919/X92X0D",
        3,
        "disruptive innovation",
    ),
    # --- Theory fights -----------------------------------------------------
    (
        "priem-butler-2001",
        (
            "https://courses.umass.edu/marta/schmgmt802-marta/priem%20and%20butler%20resource%20based.pdf",
        ),
        "10.5465/amr.2001.4011928",
        17,
        "resource-based",
    ),
    (
        "barney-2001",
        (
            "https://courses.umass.edu/marta/schmgmt802-marta/barney%20resource-based.pdf",
        ),
        "10.5465/amr.2001.4011938",
        14,
        "barney",
    ),
    (
        "priem-butler-2001-rejoinder",
        (
            "https://courses.umass.edu/marta/schmgmt802-marta/priem%20and%20butler%20resource%20based%202.pdf",
        ),
        "10.5465/amr.2001.4011946",
        9,
        "tautology in the resource-based view",
    ),
    (
        "barney-1991",
        (
            "https://josephmahoney.web.illinois.edu/BA545_Fall%202022/Barney%20(1991).pdf",
        ),
        "10.1177/014920639101700108",
        21,
        None,  # image-only scan
    ),
    (
        "mintzberg-waters-1985",
        (
            "http://strategy.sjsu.edu/www.stable/B290/reading/Mintzberg,%20H,%201985,%20Strategic%20Management%20Journal.%206%20pp%20257-272.pdf",
        ),
        "10.1002/smj.4250060306",
        16,
        "deliberate and emergent",
    ),
    (
        "march-1991",
        (
            "http://strategy.sjsu.edu/www.stable/pdf/March,%20J.%20G.%20%281991%29.%20Organization%20Science%202%281%29%2071-87.pdf",
        ),
        "10.1287/orsc.2.1.71",
        17,
        "exploration and exploitation",
    ),
    (
        "williamson-1979",
        (
            "https://josephmahoney.web.illinois.edu/BA549_Fall%202010/Session%203/Williamson%20(1979).pdf",
        ),
        "10.1086/466942",
        28,
        "transaction-cost economics",
    ),
    (
        "monteverde-teece-1982",
        (
            "https://josephmahoney.web.illinois.edu/BA545_Fall%202013/Monteverde%20and%20Teece%20(1982).pdf",
        ),
        "10.2307/3003441",
        7,
        "vertical integration",
    ),
]

MIN_BYTES = 50_000


def page_count(path: Path) -> int:
    try:
        out = subprocess.run(
            ["pdfinfo", str(path)], capture_output=True, text=True, timeout=30
        ).stdout
    except (FileNotFoundError, subprocess.SubprocessError):
        return -1
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return -1


def first_page_text(path: Path) -> str:
    """Page-1/2 text, lowercased and whitespace-collapsed.

    The collapse matters: a title that wraps across two lines in the PDF comes
    out of pdftotext with a newline in the middle of it, so a fingerprint like
    "evidence from digital imaging" would spuriously fail.
    """
    try:
        raw = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "2", str(path), "-"],
            capture_output=True,
            text=True,
            timeout=60,
        ).stdout
    except (FileNotFoundError, subprocess.SubprocessError):
        return ""
    return " ".join(raw.lower().split())


def verify(path: Path, min_pages: int, fingerprint: str | None) -> str | None:
    """Return an error string, or None if the file is good."""
    if not path.exists():
        return "missing"
    size = path.stat().st_size
    if size < MIN_BYTES:
        return f"only {size} bytes (expected > {MIN_BYTES}) — probably an error page"
    with path.open("rb") as fh:
        if fh.read(5) != b"%PDF-":
            return "not a PDF (no %PDF- magic) — probably an HTML login interstitial"
    pages = page_count(path)
    if pages < 0:
        return "pdfinfo unavailable or could not read the file"
    if pages < min_pages:
        return f"{pages} pages, expected at least {min_pages} — likely truncated"
    if fingerprint is not None:
        text = first_page_text(path)
        if not text.strip():
            return "no text layer, but one was expected"
        if " ".join(fingerprint.lower().split()) not in text:
            return f"page-1 text does not contain {fingerprint!r} — wrong paper?"
    return None


# web.archive.org rate-limits hard when you fetch twenty files in a row: it
# answers 503, and sometimes a spurious 404, for captures that demonstrably
# exist. Both are transient, so they are worth retrying with a growing delay
# rather than reporting as a dead link.
TRANSIENT = {429, 500, 502, 503, 504}
RETRY_DELAYS = (5, 15, 40)


def download_once(url: str, path: Path) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            path.write_bytes(resp.read())
    except urllib.error.HTTPError as exc:
        transient = exc.code in TRANSIENT or (
            exc.code == 404 and "web.archive.org" in url
        )
        return f"{'TRANSIENT ' if transient else ''}HTTP {exc.code} {exc.reason}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return f"TRANSIENT {exc}"
    return None


def fetch(urls: tuple[str, ...], path: Path, min_pages: int,
          fingerprint: str | None) -> tuple[str | None, str | None]:
    """Try each URL in turn, retrying transient failures. -> (error, url_used)."""
    last = None
    for url in urls:
        for delay in (0, *RETRY_DELAYS):
            if delay:
                print(f"\n          retrying in {delay}s ...", end="", flush=True)
                time.sleep(delay)
            err = download_once(url, path)
            if err is None:
                err = verify(path, min_pages, fingerprint)
                if err is None:
                    return None, url
                # A real PDF that isn't the right paper: retrying won't help.
                path.unlink(missing_ok=True)
                last = err
                break
            path.unlink(missing_ok=True)
            last = err
            if not err.startswith("TRANSIENT"):
                break  # hard 403/404: this URL is dead, move on
    return (last or "no URL succeeded"), None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true", help="re-download everything")
    ap.add_argument("--check", action="store_true", help="verify only, fetch nothing")
    args = ap.parse_args()

    DEST.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    ok = skipped = 0

    for key, urls, doi, min_pages, fingerprint in PAPERS:
        path = DEST / f"{key}.pdf"
        flag = "" if fingerprint is not None else "  [NO-TEXT scan]"

        if path.exists() and not args.force:
            err = verify(path, min_pages, fingerprint)
            if err is None:
                print(f"  ok      {key}{flag}")
                skipped += 1
                continue
            if args.check:
                print(f"  BAD     {key}: {err}")
                failures.append(f"{key} ({doi}): {err}\n          {urls[0]}")
                continue
            print(f"  refetch {key}: {err}")
            path.unlink(missing_ok=True)

        if args.check:
            if not path.exists():
                print(f"  MISSING {key}")
                failures.append(f"{key} ({doi}): not on disk")
            continue

        print(f"  get     {key} ...", end="", flush=True)
        err, used = fetch(urls, path, min_pages, fingerprint)
        if err is not None:
            print(f" FAILED — {err}")
            failures.append(f"{key} ({doi}): {err}\n          {urls[0]}")
            continue
        via = "" if used == urls[0] else f"  [fallback: {used}]"
        print(f" {path.stat().st_size:,} bytes{flag}{via}")
        ok += 1

    print(f"\n{ok} fetched, {skipped} already present, {len(failures)} failed.")
    if failures:
        print("\nFailures — resolve these through BI's library using the DOI:")
        for f in failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
