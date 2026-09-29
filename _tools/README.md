# Vault conventions & workflow

## Processing a paper (candidate → paper)
Papers enter the vault as candidate notes in `Backlog/` (see *Backlog*). To process one:
1. In its candidate note set `status: processing`, check `citekey` (`FirstAuthorSurnameYEAR`, ASCII,
   add `a`/`b` if the key is already used in `Papers/`) and `pdf_url`.
2. `uv run _tools/extract_all.py` → PDF in `Attachments/<key>/`, docling output in `.cache/docling/<key>/`
   (`<key>.md` full text, `figures.md` caption index, `tables.md` all tables, `figs/*.png`).
   Long PDFs are cut at 45 pages. Pass citekeys as arguments to (re-)extract specific papers.
3. Pick figures: `_tools/pick_figure.sh <key> fig-03-p5.png` → prints the `![[...]]` embed.
4. **Promote the same note**: move it to `Papers/`, rename to `<key> - <Short title>`, replace
   `type/candidate` with `type/paper` (+ `relevance/…`, facet tags), delete `status`/`priority`/`why`,
   add the remaining `Templates/Paper.md` properties (`questions`, `pdf`, `peer_reviewed`…) and body.
   Keep `found_by`/`cited_by`: they record where the paper came from. Obsidian updates links on rename.
5. Link it from the relevant `Questions/*.md` and summarise the session in `Sessions/` (see below).

## Paper note properties
| property | values |
|---|---|
| `title`, `citekey`, `authors`, `year` | |
| `published` | `YYYY-MM-DD` (arXiv v1 or journal date) |
| `venue` | e.g. `ICLR 2026`, `npj Digital Medicine`, `arXiv preprint` |
| `peer_reviewed` | `true` / `false` / `workshop` |
| `url`, `arxiv`/`doi`, `pdf`, `pdf_url` | `pdf: "[[<key>.pdf]]"`; `pdf_url` is what `extract_all.py` downloads |
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
- `type/` paper · candidate · question · session · backlog
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
One note per candidate in `Backlog/`, properties only (`Templates/Candidate.md`), browsed through the
views in `Backlog.base` (embedded in `Backlog.md`, in session notes and in every paper note).

| property | values |
|---|---|
| `status` | `candidate` → `processing` → *(promoted to `Papers/`)* · `rejected` (+ `reason`) |
| `priority` | 1 = process next · 2 = relevant · 3 = peripheral / background |
| `topics`, `relevance` | as for papers; `relevance` is the first guess (core / adjacent) |
| `manipulation`, `outcome`, `why` | what the paper varies, what it measures, one-line reason |
| `found_by` | provenance tags such as `search/deception` |
| `cited_by` | links to processed papers whose reference lists include it (feeds the *Cited by this paper* view) |
| `pdf_url`, `url`, `arxiv`, `citekey`, `published`, `added` | |

Filenames are `<citekey> - <short title>`. Rejected candidates stay in the folder with `status: rejected`
so later searches don't resurface them. Before adding a candidate, search the vault for its arXiv id.
The `Backlog/` folder is hidden from the graph (`-path:Backlog` in the graph filter).

## Citations
`uv run _tools/citations.py` fetches each paper's full reference list from Semantic Scholar (cached in
`.cache/citations/`) and matches it against `Papers/` and `Backlog/` by arXiv id, DOI or title. It owns
these properties (recomputed on every run, don't edit by hand):
- papers: `cites` (vault notes it cites), `cited_by` + `cited_by_count` (processed papers citing it)
- candidates: `cited_by` (merged with hand-added entries) + `cited_by_count`

It also prints references *not* in the vault that several processed papers cite (backward snowball;
`--add-min N` turns those cited by ≥ N papers into candidate notes with `found_by: [citations/backward]`),
and with `--forward` papers citing several processed papers. Views: `Backlog.base#Most cited`,
`Papers.base#Most cited in vault`. Rerun after processing new papers. Set `S2_API_KEY` (in `~/.zshrc` or a
git-ignored `.env`) to use a Semantic Scholar API key; without one it paces requests at 1 per 3 s.

## Git
PDFs (`Attachments/**/*.pdf`) and the docling cache (`.cache/`) are git-ignored because the repo is
public. After a fresh clone run `uv sync && uv run _tools/extract_all.py` to re-download and
re-extract them from each note's `pdf_url` (Schwarz2026 is on SSRN and has to be downloaded manually
through a browser into `Attachments/Schwarz2026/Schwarz2026.pdf` first).
