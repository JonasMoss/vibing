# Recent cross-field AI resources

Curated 9 August 2026. The publication cutoff is 9 May 2026. For claims about
current capability, publication date is not enough: the model and data also need
to be recent. Several apparently current papers fail that stronger test.

## Bottom line

The Ferrara guide is the only item here that comes close to this course's actual
workflow. It is not a substitute for our material. Its opening is generic, and it
does not teach a usable git workflow or a serious research-project layout.
Nevertheless, selected sections document researchers using current Codex and
Claude Code on real files and multimodal sources.

The best pairing is:

1. Ferrara for what filesystem agents can now do across unfamiliar source types.
2. Piper for why disciplinary constructs, evidence, and standards of validity do
   not transfer automatically with the machinery.

## Triage

| Resource | Evidence freshness | Verdict | What it is actually useful for |
|---|---|---|---|
| Ferrara, *A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History* (16 June 2026) | Current: examples include ChatGPT 5.5, Claude Opus 4.7/4.8, Codex, and Claude Code used in May–June 2026 | **Keep, but read selectively** | Concrete demonstrations with newspapers, handwritten census sheets, paintings, and audio; agentic file access; validation and replication |
| Piper, *A Theory-First Approach toward Using Generative AI for Humanities Research* (18 June 2026) | Current methodological argument, not a capability benchmark | **Keep** | The strongest account here of what does not transfer: prompts operationalize constructs and should be stress-tested like measurement instruments |
| Anthropic, *Economic Index: Cadences* (26 June 2026) | Current usage telemetry, including mid-May to early June 2026 | **Keep as descriptive evidence** | What people actually produce with chat, Cowork, APIs, and Claude Code; how artifact type and interface alter delegation |
| Reuters Institute, *Emerging Uses of AI Chatbots for News* (16 June 2026) | Current survey report, but not a model evaluation | **Keep for communication/media** | Shows that audiences use AI to interrogate, simplify, compare, translate, and evaluate news—not merely retrieve it |
| Salinas et al., *Law Professors Prefer AI Over Peer Answers* (27 May 2026) | Mixed: human evaluation used Gemini 2.5 Pro and NotebookLM in August 2025; newer models were ranked later by an LLM judge | **Use as a benchmark-critique case, not as the headline claims** | A provocative demonstration of expert preference in a judgment-rich domain, plus an unusually teachable example of how evaluation design determines the conclusion |
| Contractor and Reyes, *Experimental Evidence on the Learning Impact of Generative AI* (9 July 2026) | **Stale for capability:** experiment ran in spring 2025 with GPT-4o | **Background only** | Evidence about learning under a tightly controlled, one-hour browser-chat task; not evidence about present-day agents or present-day model capability |
| Jack, Cooper, and Flower, *Automating the Qualitative Interview?* (27 May 2026) | **Stale for capability:** built on Gemini Flash 1.5 | **Skip as current capability evidence** | A cheap adaptive-interview prototype and a qualitative-methods discussion; technically behind the current frontier |

## What the Ferrara guide really contains

It does discuss the tools the opening makes it sound as if it might never reach:

- project folders and `AGENTS.md`;
- Codex, Claude Code, Gemini CLI, terminal agents, filesystem access, and desktop
  agent interfaces;
- agent access to file trees, code execution, and local data;
- using separate agents and Git worktrees to avoid simultaneous-edit clashes;
- archiving prompts, code, model outputs, and validation samples;
- a direct comparison of chat with Codex and Claude Code on record linkage.

The useful reading path is:

- pp. 6–9: interaction modes and filesystem agents;
- pp. 21–29: validation, reproducibility, and replication packages;
- pp. 29–38: worked applications to historical text, handwriting, images, and
  audio;
- p. 31/Table 3: chat versus Codex and Claude Code on name-blind census linking.

What is missing or weak:

- no working introduction to git, commits, diffs, rollback, or branches;
- no defensible directory scheme separating original data, derived data, code,
  outputs, notes, and temporary work;
- `AGENTS.md` is treated partly as a running project log, which risks turning a
  stable instruction file into an accumulating context dump;
- the safety suggestion is mainly to keep originals outside the agent's folder,
  rather than teaching version control, scoped permissions, immutable source
  data, and recoverable changes;
- it still frames agents as one option in a menu of chat/IDE/API modes instead of
  beginning from the much more powerful project-level workflow.

So the guide is evidence that this workflow has reached economic history. It is
not the guide we should hand participants to learn the workflow.

## Two especially useful methodological lessons

### Humanities: prompts are part of the measurement

Piper's useful claim is not that humanities researchers need more cautious
prompting. It is that a prompt operationalizes a theoretical construct. Several
plausible prompts can produce high agreement with human labels while supporting
different—even reversed—substantive conclusions. The appropriate move is to vary
theoretically defensible prompts and inspect the distribution of conclusions,
rather than optimize one prompt until it agrees with expectations.

This transfers cleanly to marketing, leadership, law, and communication research:
the agent can execute the analysis, but the discipline still determines what the
categories mean and what variation is admissible.

### Law: impressive result, misleading headline

The law study is genuinely interesting, but its result is narrower than the title:

- professors were instructed to spend no more than three minutes writing each
  answer and to avoid research;
- the task was a brief, course-agnostic office-hours answer, not legal practice;
- the core human evaluation occurred in August 2025;
- the comparisons forced a choice and did not allow ties;
- later frontier-model rankings used Llama 4 Maverick as the judge, after
  calibrating it against the human judgments.

It supports “LLMs can give excellent short explanations of first-year contract
law, including hypotheticals.” It does not establish “AI outperforms law
professors” in teaching, scholarship, or legal work. That gap makes the paper a
good classroom exercise in reading capability claims without being intimidated by
the headline.

## What appears to transfer across fields

- operating on a project rather than answering one isolated prompt;
- reading heterogeneous local material and turning it into inspectable artifacts;
- extraction, transcription, classification, restructuring, comparison, and
  iterative revision;
- keeping instructions, examples, outputs, and checks beside the work;
- using an expert-created rubric or validation sample to test the result.

What does not transfer automatically is the definition of the construct, the
authority of sources, the meaning of disagreement, acceptable evidence, and the
consequences of error. That is where the participant's disciplinary expertise
becomes the specification for the agent.

## Files and original sources

- [Ferrara guide](ferrara-2026-economic-history-guide.pdf) — [original](https://www.rfberlin.com/wp-content/uploads/2026/06/26171-1.pdf)
- [Piper humanities article](piper-2026-theory-first-humanities.pdf) — [original](https://www.cambridge.org/core/journals/computational-humanities-research/article/theoryfirst-approach-toward-using-generative-ai-for-humanities-research/1D3B11E220735772BE68B5D6C83DB2B8)
- [Anthropic Economic Index](anthropic-2026-economic-index-cadences.pdf) — [original](https://www.anthropic.com/research/economic-index-june-2026-report)
- [Reuters Institute chapter](reuters-institute-2026-ai-chatbots-news-chapter.pdf) — [original](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/emerging-uses-ai-chatbots-news-and-what-it-means-journalism)
- [Salinas et al. law paper](salinas-et-al-2026-law-professors.pdf) — [original](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6849678)
- [Contractor and Reyes education paper](contractor-reyes-2026-learning-impact.pdf) — [original](https://arxiv.org/abs/2607.08849)
- Jack, Cooper, and Flower — [online full text](https://journals.sagepub.com/doi/10.1177/20597991261448157) (the publisher blocked a direct PDF download)
- Stanford HAI, *Legal AI's Legibility Problem* — [online commentary](https://hai.stanford.edu/news/legal-ais-legibility-problem)

