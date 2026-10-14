# Strategic management: a reading pile

Assembled 20 September 2026. Instructor background reading — not participant
material, not course content. The point is to get a feel for the field quickly.

The organising observation, which turns out to be a good one: **the field's
deepest recurring anxiety is whether firm performance differences are
explainable at all, or mostly luck plus storytelling.** Most of what follows
circles that drain. The vivid theories come from the case tradition; the best
papers are often the debunkings. If you like regression to the mean, selection
effects and variance components, you are already most of the way in.

## The files

`pdfs/` holds 19 papers. It is **gitignored** — these are third-party
copyrighted articles that happen to be posted on faculty pages and university
course pages, and committing them to a public repo that serves
vibing.jonasmoss.com would be republication. Same rule as
`examples/litsweep/pdfs/`.

Rebuild or verify the folder with:

```powershell
python3 scratch/links/strategy-canon/fetch.py            # fetch what's missing
python3 scratch/links/strategy-canon/fetch.py --check    # verify what's on disk
```

Seven papers could not be obtained from any legitimate source. They are listed
below with DOIs; BI's library subscription resolves all of them. Four of the
seven are in the luck-versus-skill cluster, which is the most interesting part,
so those are the ones worth the trip to the library proxy.

## If you have one evening

Everything in this path is on disk, and it gets you the whole shape of the
field in about five papers:

1. **March 1991** — the field's most-cited idea, and you'll recognise it
   immediately as a bandit problem told verbally.
2. **Denrell & Liu 2012** — six pages, the cleanest formal statement of why
   learning from top performers is a mistake.
3. **Priem & Butler 2001 → Barney 2001 → Priem & Butler rejoinder** — read as
   one 45-page argument about whether the field's central theory says anything.
4. **Golder & Tellis 1993** — the debunking method at its most concrete: go back
   to the historical record and discover the winners were defined after the fact.
5. **Tripsas & Gavetti 2000** — the case tradition doing what it's actually good
   at. Polaroid had the digital-imaging capability and the mental model killed it.

Then **Mintzberg & Waters 1985** if you want to understand why half the field
distrusts the other half.

---

## 1. Luck versus skill

The natural entry point, and the cluster with the worst availability.

| Paper | On disk? | DOI |
|---|---|---|
| Henderson, Raynor & Ahmed (2012), "How long must a firm be great to rule out chance? Benchmarking sustained superior performance without being fooled by randomness", *SMJ* 33(4):387–406 | **no — library** | [10.1002/smj.1943](https://doi.org/10.1002/smj.1943) |
| Fitza (2014), "The use of variance decomposition in the investigation of CEO effects: how large must the CEO effect be to rule out chance?", *SMJ* 35(12):1839–1852 | **no — library** | [10.1002/smj.2192](https://doi.org/10.1002/smj.2192) |
| Quigley & Hambrick (2015), "Has the 'CEO effect' increased in recent decades?", *SMJ* 36(6):821–830 | `quigley-hambrick-2015.pdf` | [10.1002/smj.2258](https://doi.org/10.1002/smj.2258) |
| Quigley & Graffin (2017), "Reaffirming the CEO effect is significant and much larger than chance: a comment on Fitza (2014)", *SMJ* 38(3):793–801 | **no — library** | [10.1002/smj.2503](https://doi.org/10.1002/smj.2503) |
| Fitza (2017), "How much do CEOs really matter? Reaffirming that the CEO effect is mostly due to chance", *SMJ* 38(3):802–811 | **no — library** | [10.1002/smj.2597](https://doi.org/10.1002/smj.2597) |
| Denrell (2003), "Vicarious learning, undersampling of failure, and the myths of management", *Org. Science* 14(3):227–243 | **no — library** | [10.1287/orsc.14.2.227.15164](https://doi.org/10.1287/orsc.14.2.227.15164) |
| Denrell & Liu (2012), "Top performers are not the most impressive when extreme performance indicates unreliability", *PNAS* 109(24):9331–9336 | `denrell-liu-2012.pdf` | [10.1073/pnas.1116048109](https://doi.org/10.1073/pnas.1116048109) |
| Wiggins & Ruefli (2002), "Sustained competitive advantage: temporal dynamics and the incidence and persistence of superior economic performance", *Org. Science* 13(1):81–105 | **no — library** | [10.1287/orsc.13.1.81.542](https://doi.org/10.1287/orsc.13.1.81.542) |
| Wiggins & Ruefli (2005), "Schumpeter's ghost: is hypercompetition making the best of times shorter?", *SMJ* 26(10):887–911 | **no — library** | [10.1002/smj.492](https://doi.org/10.1002/smj.492) |

**Henderson, Raynor & Ahmed** model firm performance as a Markov chain over
performance deciles and ask how long a streak has to be before it stops being
consistent with that null. A large share of the firms celebrated as sustained
superior performers — including many exemplars from *Good to Great* and *In
Search of Excellence* — don't clear the bar. It is a regression-to-the-mean
paper that landed as a critique of half the field.

**The CEO-effect exchange is the best single artefact here**, and it is a
four-paper sequence you'd enjoy in order: variance decompositions attribute a
sizable share of performance variance to CEOs; Quigley & Hambrick argue the
share has grown over time; Fitza shows that randomly assigning "CEOs" to
firm-year spells produces an effect of comparable size; Quigley & Graffin reply;
Fitza replies to the reply. The whole dispute reduces to *what a random-effects
variance component actually identifies when spells are short and performance is
autocorrelated*. That is a statistics argument being conducted in a management
journal by people with varying enthusiasm for the statistics.

**Denrell** is the selection-bias result: if risky strategies produce both
spectacular successes and quiet deaths, then sampling only survivors makes
risk-taking look causal. **Denrell & Liu** push it further — the most extreme
performers can be the *least* impressive, because extremity signals high
variance rather than high skill. Both cut directly against the case-study
tradition, which is exactly why they matter.

**Wiggins & Ruefli** find that persistent superior performance is rare and has
been getting shorter-lived. Awkward for a field whose central concept is
"sustainable competitive advantage."

## 2. Why do firms keep making acquisitions?

Average acquirer returns are roughly zero to negative, and M&A volume stays
enormous. Candidate explanations: hubris, agency and empire-building, or a
lottery view where the mean is bad but the right tail is what you're buying.

| Paper | On disk? | DOI |
|---|---|---|
| King, Dalton, Daily & Covin (2004), "Meta-analyses of post-acquisition performance: indications of unidentified moderators", *SMJ* 25(2):187–200 | `king-et-al-2004.pdf` | [10.1002/smj.371](https://doi.org/10.1002/smj.371) |
| Roll (1986), "The hubris hypothesis of corporate takeovers", *J. Business* 59(2):197–216 | `roll-1986.pdf` | [10.1086/296325](https://doi.org/10.1086/296325) |

**King et al.** is the useful one: a meta-analysis finding that *none* of the
commonly studied moderators predicted post-acquisition performance. A null
result of that shape is either a measurement failure or a devastating finding
about the literature, and the paper is honest that it can't tell which.

## 3. Is the diversification discount real?

Conglomerates trade below the sum of comparable standalone firms. Finance
treated that as value destruction for years.

| Paper | On disk? | DOI |
|---|---|---|
| Campa & Kedia (2002), "Explaining the diversification discount", *J. Finance* 57(4):1731–1762 | `campa-kedia-2002.pdf` | [10.1111/1540-6261.00476](https://doi.org/10.1111/1540-6261.00476) |
| Villalonga (2004), "Diversification discount or premium? New evidence from the Business Information Tracking Series", *J. Finance* 59(2):479–506 | `villalonga-2004.pdf` | [10.1111/j.1540-6261.2004.00640.x](https://doi.org/10.1111/j.1540-6261.2004.00640.x) |

Both argue the discount is largely **selection**: firms that diversify were
already worse. Campa & Kedia attack it with fixed effects and selection models;
Villalonga attacks it by throwing out the segment-level data everyone had been
using in favour of establishment-level census data, and finds a *premium*. This
is a clean, self-contained example of a stylised fact dissolving under better
identification and better data — and the strategy field has a parallel
related-versus-unrelated diversification literature that never resolved at all.

## 4. Is there a first-mover advantage?

| Paper | On disk? | DOI |
|---|---|---|
| Golder & Tellis (1993), "Pioneer advantage: marketing logic or marketing legend?", *JMR* 30(2):158–170 | `golder-tellis-1993.pdf` | [10.2307/3172825](https://doi.org/10.2307/3172825) |

Early work said yes. Golder & Tellis went back to historical sources and found
many celebrated "pioneers" were actually early followers, and that true pioneers
failed at a high rate. The earlier results came partly from defining the pioneer
*after the fact* as the firm that survived to be studied. Methodologically this
is the most transferable paper in the pile — the move is "go check the primary
record," and it works in every field.

## 5. Why do incumbents fail at technological transitions?

| Paper | On disk? | DOI |
|---|---|---|
| Henderson & Clark (1990), "Architectural innovation: the reconfiguration of existing product technologies and the failure of established firms", *ASQ* 35(1):9–30 | `henderson-clark-1990.pdf` | [10.2307/2393549](https://doi.org/10.2307/2393549) |
| Christensen & Bower (1996), "Customer power, strategic investment, and the failure of leading firms", *SMJ* 17(3):197–218 | `christensen-bower-1996.pdf` | [10.1002/(SICI)1097-0266(199603)17:3<197::AID-SMJ804>3.0.CO;2-U](https://doi.org/10.1002/(SICI)1097-0266(199603)17:3%3C197::AID-SMJ804%3E3.0.CO;2-U) |
| Tripsas & Gavetti (2000), "Capabilities, cognition, and inertia: evidence from digital imaging", *SMJ* 21(10–11):1147–1161 | `tripsas-gavetti-2000.pdf` (HBS WP 00-067) | [10.1002/1097-0266(200010/11)21:10/11<1147::AID-SMJ128>3.0.CO;2-R](https://doi.org/10.1002/1097-0266%28200010/11%2921:10/11%3C1147::AID-SMJ128%3E3.0.CO;2-R) |
| King & Baatartogtokh (2015), "How useful is the theory of disruptive innovation?", *MIT Sloan Management Review* 57(1):77–90 | **no — hard paywall, no DOI** | — |
| King (2017), "The theory of disruptive innovation: science or allegory?", *Entrepreneur & Innovation Exchange* | `king-2017-allegory.pdf` | [10.17919/X92X0D](https://doi.org/10.17919/X92X0D) |

Christensen's disruption story is the famous answer; **Christensen & Bower 1996**
is the academic version of it, before the trade books. **King & Baatartogtokh**
went back through the cases in *The Innovator's Dilemma* and found only a small
minority satisfy the theory's own stated conditions. That paper is behind MIT
SMR's paywall with no repository copy anywhere I could legitimately reach, so
the four-page open-access **King 2017** piece is here instead — same argument,
much shorter, and it makes the epistemological point more bluntly.

The two competing accounts are the better reading anyway. **Henderson & Clark**:
incumbents fail because their organisation *mirrors the old product's
architecture*, so an innovation that rearranges components while leaving each
component intact is invisible to them. **Tripsas & Gavetti**: Polaroid had
world-class digital-imaging capability and managers' mental model of the
business — "we make money on film" — blocked it. Note that the copy on disk is
the HBS working paper, not the SMJ version of record; it's the only free one.

## 6. Is the resource-based view a tautology?

| Paper | On disk? | DOI |
|---|---|---|
| Barney (1991), "Firm resources and sustained competitive advantage", *J. Management* 17(1):99–120 | `barney-1991.pdf` | [10.1177/014920639101700108](https://doi.org/10.1177/014920639101700108) |
| Priem & Butler (2001), "Is the resource-based 'view' a useful perspective for strategic management research?", *AMR* 26(1):22–40 | `priem-butler-2001.pdf` | [10.5465/amr.2001.4011928](https://doi.org/10.5465/amr.2001.4011928) |
| Barney (2001), "… ? Yes", *AMR* 26(1):41–56 | `barney-2001.pdf` | [10.5465/amr.2001.4011938](https://doi.org/10.5465/amr.2001.4011938) |
| Priem & Butler (2001), "Tautology in the resource-based view and the implications of externally determined resource value: further comments", *AMR* 26(1):57–66 | `priem-butler-2001-rejoinder.pdf` | [10.5465/amr.2001.4011946](https://doi.org/10.5465/amr.2001.4011946) |

Barney 1991 is the target (read the first ten pages for the VRIN criteria and
stop). Priem & Butler argue that "valuable, rare, inimitable resources produce
advantage" is true by definition, since value and advantage are each defined in
terms of the other, and that the theory is therefore unfalsifiable and
managerially empty. Barney replies. They reply to the reply.

Read this one as a **window into how the field thinks about what a theory is**.
The interesting thing is not who wins; it's that a top journal ran 45 pages on
whether its central framework is a definition, and the framework's popularity
was entirely unaffected by the outcome.

## 7. Planned or emergent strategy?

| Paper | On disk? | DOI |
|---|---|---|
| Mintzberg & Waters (1985), "Of strategies, deliberate and emergent", *SMJ* 6(3):257–272 | `mintzberg-waters-1985.pdf` | [10.1002/smj.4250060306](https://doi.org/10.1002/smj.4250060306) |
| Pascale (1984), "Perspectives on strategy: the real story behind Honda's success", *CMR* 26(3):47–72 | **no — library** | [10.2307/41165080](https://doi.org/10.2307/41165080) |
| Mintzberg (1990), "The design school: reconsidering the basic premises of strategic management", *SMJ* 11(3):171–195 | not fetched | [10.1002/smj.4250110302](https://doi.org/10.1002/smj.4250110302) |
| Ansoff (1991), "Critique of Henry Mintzberg's 'The design school'", *SMJ* 12(6):449–461 | not fetched | [10.1002/smj.4250120605](https://doi.org/10.1002/smj.4250120605) |

Mintzberg spent decades arguing strategy is mostly emergent and rationalised
afterwards. **The set piece is Honda.** BCG's report to the British government
explained Honda's US success as a deliberate cost-and-scale strategy. Pascale
then interviewed the Honda executives who were actually there, and got
improvisation, accidents, and the small bikes they almost didn't bother selling.
Business schools taught both versions, to the same students, for years.

Pascale 1984 is the one I most wanted and could not get free — Sage has it
locked and the only circulating PDF turns out to be the 1996 *CMR* follow-up
symposium, not the original. Worth pulling through the library; it's the most
*fun* paper on this list. If you want the fight in its pure form, Mintzberg 1990
and Ansoff's furious 1991 reply are right there too.

## 8. Exploration versus exploitation

| Paper | On disk? | DOI |
|---|---|---|
| March (1991), "Exploration and exploitation in organizational learning", *Org. Science* 2(1):71–87 | `march-1991.pdf` | [10.1287/orsc.2.1.71](https://doi.org/10.1287/orsc.2.1.71) |

One of the most-cited papers in all of management. Organisations drift toward
exploiting known options because exploitation pays sooner and more reliably,
which crowds out exploration. You will recognise it as the bandit problem, told
verbally, with the twist that the "agent" is a *population* of individuals
learning from each other and from a shared organisational code — so the
slow learners are valuable, because they keep the code from converging early.

A large "ambidexterity" literature grew out of this, with measurement practices
you should brace for.

## 9. Make or buy

The field's best-supported theory, empirically. Worth reading last, as a
palate cleanser: it is what a strategy literature looks like when it works.

| Paper | On disk? | DOI |
|---|---|---|
| Williamson (1979), "Transaction-cost economics: the governance of contractual relations", *J. Law & Economics* 22(2):233–261 | `williamson-1979.pdf` | [10.1086/466942](https://doi.org/10.1086/466942) |
| Monteverde & Teece (1982), "Supplier switching costs and vertical integration in the automobile industry", *Bell J. Economics* 13(1):206–213 | `monteverde-teece-1982.pdf` | [10.2307/3003441](https://doi.org/10.2307/3003441) |

Transaction cost economics predicts vertical integration when assets are
relationship-specific. Monteverde & Teece is the founding empirical test, on
auto parts, and it's eight pages. The capabilities camp argues integration is
driven more by what firms already know how to do than by hold-up risk; that
argument is still live.

## Adjacent, if the variance-decomposition thread grabs you

Not fetched, but the industry-versus-firm-effects literature is the same
statistical machinery pointed at a different question, and it's older and
better developed than the CEO version:

- Rumelt (1991), "How much does industry matter?", *SMJ* 12(3):167–185 —
  [10.1002/smj.4250120302](https://doi.org/10.1002/smj.4250120302)
- McGahan & Porter (1997), "How much does industry matter, really?", *SMJ*
  18(S1):15–30 —
  [10.1002/(SICI)1097-0266(199707)18:1+<15::AID-SMJ916>3.0.CO;2-1](https://doi.org/10.1002/(SICI)1097-0266(199707)18:1+%3C15::AID-SMJ916%3E3.0.CO;2-1)

## File quirks

- **`roll-1986.pdf`** and **`barney-1991.pdf`** are image-only library scans with
  no text layer. They read fine, but `grep` and Ctrl-F will find nothing, and an
  LLM cannot read them without OCR first.
- **`roll-1986.pdf`** is additionally a 2-up scan rotated 90°. Rotate in your
  viewer.
- **`tripsas-gavetti-2000.pdf`** is HBS working paper 00-067 (May 2000), not the
  SMJ version of record. Cite the SMJ DOI, not this file.
- `quigley-hambrick-2015`, `king-et-al-2004` and `campa-kedia-2002` came from
  Internet Archive captures because the origin servers (UGA, FSU, NYU Stern) are
  currently unreachable to scripts. The bytes are the publishers' own PDFs.

## Sourcing note

Every file here came from a publisher open-access page, an author's own faculty
or personal page, a university course reading page, an institutional repository,
or an Internet Archive capture of one of those. Nothing came from a
paywall-circumvention site, and nothing should be added from one — the seven
missing papers stay missing until someone pulls them through BI's library.
