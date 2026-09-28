# Vault conventions & workflow

## Adding a paper
1. Add a row to `_tools/papers.tsv` (`citekey<TAB>pdf_url<TAB>arxiv/doi<TAB>short title`).
   Citekey = `FirstAuthorSurnameYEAR` (ASCII, no spaces); add `a`/`b` on collision.
2. `_tools/extract_all.sh` → PDF in `Attachments/<key>/`, docling output in `.cache/docling/<key>/`
   (`<key>.md` full text, `figures.md` caption index, `tables.md` all tables, `figs/*.png`).
   Long PDFs are cut at 45 pages (`--max-pages`).
3. Pick figures: `_tools/pick_figure.sh <key> fig-03-p5.png` → prints the `![[...]]` embed.
4. Create `Papers/<key> - <Short title>.md` from `Templates/Paper.md`.
5. Add wikilinks to it from the relevant `Questions/*.md` and summarise the session in `Sessions/` (see below).

## Paper note properties
| property | values |
|---|---|
| `title`, `citekey`, `authors`, `year` | |
| `published` | `YYYY-MM-DD` (arXiv v1 or journal date) |
| `venue` | e.g. `ICLR 2026`, `npj Digital Medicine`, `arXiv preprint` |
| `peer_reviewed` | `true` / `false` / `workshop` |
| `url`, `arxiv`/`doi`, `pdf` | `pdf: "[[<key>.pdf]]"` |
| `questions` | list of question ids, e.g. `[Q1, Q2, Q4.1]` |
| `relevance` | `core` (stress manipulated **and** misaligned behaviour measured) / `adjacent` |

## Tags (nested; add new leaves freely, keep the prefixes)
- `type/` paper · question · session · overview (Backlog)
- `relevance/` core · adjacent
- `q/` 1 · 2 · 3-1 · 3-2 · 4-1 · 4-2 (new question → new `q/…` + note in `Questions/`)
- `stressor/` threat-shutdown · threat-value-modification · goal-conflict · performance-pressure · time-pressure · resource-scarcity · social-pressure · authority-pressure · emotional-prompt · trauma-narrative · high-stakes · impossible-task · activation-steering · power-seeking-incentive · oversight · evaluation-awareness · environmental-friction · goal-directedness-prompt
- `behavior/` deception · alignment-faking · concealment · reward-hacking · safety-violation · sycophancy · sabotage · blackmail · sandbagging · self-preservation · jailbreak-susceptibility · performance · bias
- `subject/` llm · agent

## Question notes
`Questions/Qx ....md`, properties `id: Qx`, tags `type/question`, `q/x`. Cite papers inline as
`[[Scheurer2023 - Strategic deception under pressure|Scheurer et al. 2023]]`. Each embeds
`![[Papers.base#This question]]` which lists every paper whose `questions` contains the note's `id`.

## Session notes
Each research session gets a summary in `Sessions/YYYY-MM-DD <Topic> - <kind>.md` with properties
`date`, `session`, `questions: [...]` plus matching `q/…` tags and `type/session`, and a
"Questions addressed" callout at the top linking to the question notes. Session notes are
snapshots; the living answers are in `Questions/`.

## Git
PDFs (`Attachments/**/*.pdf`) and the docling cache (`.cache/`) are git-ignored because the repo is
public. After a fresh clone run `uv sync && _tools/extract_all.sh` to re-download and re-extract them
(URLs are in `papers.tsv`; Schwarz2026 is on SSRN and has to be downloaded manually through a browser).
