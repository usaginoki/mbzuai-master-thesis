# Vault conventions & workflow

## Adding a paper
1. Add a row to `_tools/papers.tsv` (`citekey<TAB>pdf_url<TAB>arxiv/doi<TAB>short title`).
   Citekey = `FirstAuthorSurnameYEAR` (ASCII, no spaces); add `a`/`b` on collision.
2. `_tools/extract_all.sh` → PDF in `Attachments/<key>/`, docling output in `.cache/docling/<key>/`
   (`<key>.md` full text, `figures.md` caption index, `tables.md` all tables, `figs/*.png`).
   Long PDFs are cut at 45 pages (`--max-pages`).
3. Pick figures: `_tools/pick_figure.sh <key> fig-03-p5.png` → prints the `![[...]]` embed.
4. Create `Papers/<key> - <Short title>.md` from `Templates/Paper.md` (set `topics` and `questions`).
5. Add wikilinks to it from the relevant `Questions/*.md` and summarise the session in `Sessions/` (see below).

## Paper note properties
| property | values |
|---|---|
| `title`, `citekey`, `authors`, `year` | |
| `published` | `YYYY-MM-DD` (arXiv v1 or journal date) |
| `venue` | e.g. `ICLR 2026`, `npj Digital Medicine`, `arXiv preprint` |
| `peer_reviewed` | `true` / `false` / `workshop` |
| `url`, `arxiv`/`doi`, `pdf` | `pdf: "[[<key>.pdf]]"` |
| `topics` | list of topic slugs, e.g. `[stress-misalignment]` (a paper can serve several topics) |
| `questions` | list of question ids, e.g. `[Q1, Q2, Q4.1]` |
| `relevance` | `core` / `adjacent`; what counts as core is defined per topic (see Topics) |

## Topics
A topic is a research thread with its own questions. Every paper, question and session note carries
`topics: [...]`. Start a new topic by adding a row here and creating its question notes from
`Templates/Question.md`.

| topic slug | questions | `core` means |
|---|---|---|
| `stress-misalignment` | Q1–Q4.2 | stress/pressure is manipulated **and** misaligned behaviour is measured |

## Tags (nested; add new leaves freely, keep the prefixes)
Generic (every topic):
- `type/` paper · question · session · backlog
- `relevance/` core · adjacent
- `q/` 1 · 2 · 3-1 · 3-2 · 4-1 · 4-2 … (new question → new `q/…` + note in `Questions/`)
- `subject/` llm · agent · … (what was studied)

Topic-specific facets (add a new prefix per topic when useful, e.g. `method/`, `dataset/`):
- *stress-misalignment:* `stressor/` threat-shutdown · threat-value-modification · goal-conflict · performance-pressure · time-pressure · resource-scarcity · social-pressure · authority-pressure · emotional-prompt · trauma-narrative · high-stakes · impossible-task · activation-steering · power-seeking-incentive · oversight · evaluation-awareness · environmental-friction · goal-directedness-prompt
- *stress-misalignment:* `behavior/` deception · alignment-faking · concealment · reward-hacking · safety-violation · sycophancy · sabotage · blackmail · sandbagging · self-preservation · jailbreak-susceptibility · performance · bias

## Question notes
`Questions/Qx <short name>.md` from `Templates/Question.md`, properties `id: Qx`, `topics`, tags
`type/question`, `q/x`. Question ids are global across topics: continue numbering (next is Q5). Cite papers inline as
`[[Scheurer2023 - Strategic deception under pressure|Scheurer et al. 2023]]`. Each embeds
`![[Papers.base#This question]]` which lists every paper whose `questions` contains the note's `id`.

## Session notes
Each research session gets a summary in `Sessions/YYYY-MM-DD <Topic> - <kind>.md` from
`Templates/Session.md`, with properties `date`, `session`, `topics`, `questions: [...]` plus matching `q/…` tags and `type/session`, and a
"Questions addressed" callout at the top linking to the question notes. Session notes are
snapshots; the living answers are in `Questions/`.

## Backlog
`Backlog.md` holds all unprocessed candidates, grouped `## Topic: <slug>` → `### Priority 1/2/3`, one table
row per paper (format in `Templates/Backlog entry.md`). Generic columns: *Manipulation* (what the paper
varies) and *Outcome* (what it measures) work for any topic. *Found via* records provenance
(`search: <strand>` or `refs of [[note]]`). When a paper is processed or rejected, move it to the
**Processed / rejected log** at the bottom so later searches don't resurface it. Keep the file name:
paper notes link to `[[Backlog]]`.

## Git
PDFs (`Attachments/**/*.pdf`) and the docling cache (`.cache/`) are git-ignored because the repo is
public. After a fresh clone run `uv sync && _tools/extract_all.sh` to re-download and re-extract them
(URLs are in `papers.tsv`; Schwarz2026 is on SSRN and has to be downloaded manually through a browser).
