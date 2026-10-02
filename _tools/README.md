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
| `multiagent-friction` | Q5–Q7.2 | ≥2 LLM agents interact, inter-agent friction/pressure is present or manipulated, **and** an effect on safety, performance or efficiency is measured (MAS failure taxonomies without a pressure angle → adjacent) |
| `misalignment-prediction` | none yet (scoping; proposals Q8–Q13 in the 2026-10-01 session note; Q13 = internal-state awareness, scoped on 2026-10-02) | a signal available **before** the behaviour occurs is used to forecast misaligned or harmful behaviour, **and** predictive accuracy is measured (after-the-fact detectors, benchmarks and conceptual proposals → adjacent) |
| `agent-to-agent-influence` | Q14–Q17.2 | one LLM agent inspects or influences another LLM agent, **and** the channel or its effect is measured (builds on `multiagent-friction`: Q14 on Q5, Q17.1/Q17.2 on Q7.2/Q7.1) |
| `social-simulation` | Q18–Q19 | LLM agents are the actors in a simulated social situation or a replicated human study, **and** behaviour is measured (survey-only "silicon sample" work → adjacent, unless it reports human-alignment figures used for Q19) |
| `agent-competition` | Q20–Q21.2 | two or more LLM agents (or one agent told it has rivals) compete for rank, reward or a scarce resource, **and** an effect on performance or safety is measured (isolates one friction source of `multiagent-friction` Q6) |

## Tags (nested; add new leaves freely, keep the prefixes)
Generic (every topic):
- `type/` paper · candidate · question · session · backlog · idea
- `relevance/` core · adjacent
- `q/` 1 · 2 · 3-1 · 3-2 · 4-1 · 4-2 · 5 · 6 · 7-1 · 7-2 · 14 · 15 · 16 · 17-1 · 17-2 · 18 · 19 · 20 · 21-1 · 21-2 … (new question → new `q/…` + note in `Questions/`)
- `subject/` llm · agent · … (what was studied)

Topic-specific facets (add a new prefix per topic when useful, e.g. `method/`, `dataset/`):
- *stress-misalignment:* `stressor/` threat-shutdown · threat-value-modification · goal-conflict · performance-pressure · time-pressure · resource-scarcity · social-pressure · authority-pressure · emotional-prompt · trauma-narrative · high-stakes · impossible-task · activation-steering · power-seeking-incentive · oversight · evaluation-awareness · environmental-friction · goal-directedness-prompt
- *stress-misalignment:* `behavior/` deception · alignment-faking · concealment · reward-hacking · safety-violation · sycophancy · sabotage · blackmail · sandbagging · self-preservation · jailbreak-susceptibility · performance · bias
- *multiagent-friction:* `channel/` direct-message · debate · critique-review · voting-aggregation · shared-memory-blackboard · orchestrator-delegation · tool-output-handoff · negotiation-market · game-environment · observation-only · monitoring
- *multiagent-friction:* `friction/` peer-pressure-conformity · oversight-by-peer · authority-hierarchy · competition · adversarial-agent · erroneous-input · irrelevant-input · emotional-contagion · goal-conflict · resource-contention · communication-overload · persuasion-manipulation · hostile-persona · harsh-feedback · social-identity · peer-threat
- *multiagent-friction:* `effect/` safety-violation · collusion · deception · coercion · conformity-flip · error-cascade · performance-drop · performance-gain · token-cost · deadlock-loop · sycophancy · monitor-evasion · hostility · internal-state-shift
- *misalignment-prediction:* `timing` (a property, not a tag) training-time · pre-deployment · pre-generation · pre-action · earlier-in-trajectory · post-hoc: when the prediction is made relative to the behaviour
- *misalignment-prediction, internal-state-awareness sub-question:* `safety_use` (a property, not a tag) direct · risk · indirect · none: whether the self-awareness is used for safety, undermines oversight, or neither

## Question notes
`Questions/Qx <short name>.md` from `Templates/Question.md`, properties `id: Qx`, `topics`, tags
`type/question`, `q/x`. Question ids are global across topics: continue numbering (Q8–Q13 are reserved for the `misalignment-prediction` proposals; next free is Q22). Cite papers inline as
`[[Scheurer2023 - Strategic deception under pressure|Scheurer et al. 2023]]`. Each embeds
`![[Papers.base#This question]]` which lists every paper whose `questions` contains the note's `id`.

## Session notes
Each research session gets a summary in `Sessions/YYYY-MM-DD <Topic> - <kind>.md` from
`Templates/Session.md`, with properties `date`, `session`, `topics`, `questions: [...]` plus matching `q/…` tags and `type/session`, and a
"Questions addressed" callout at the top linking to the question notes. Session notes are
snapshots; the living answers are in `Questions/`.

## Idea notes
`Ideas/I<n> <short name>.md`: one note per thesis idea under investigation, with properties `idea`, `id`,
`topics`, `status` (scoping → designing → running → dropped), `source`, `updated` and tag `type/idea`. Each holds a
deep-read report: verdict, what the closest papers actually did, design space, minimal experiment, risks.
Claims are marked by read depth (full text / abstract only / vault note / own inference).

## Backlog
One note per candidate in `Backlog/`, properties only (`Templates/Candidate.md`), browsed through the
views in `Backlog.base` (embedded in `Backlog.md`, in session notes and in every paper note).

| property | values |
|---|---|
| `status` | `candidate` → `processing` → *(promoted to `Papers/`)* · `rejected` (+ `reason`) |
| `priority` | 1 = process next · 2 = relevant · 3 = peripheral / background |
| `topics`, `relevance` | as for papers; `relevance` is the first guess (core / adjacent) |
| `manipulation`, `outcome`, `why` | what the paper varies, what it measures, one-line reason |
| `questions` | optional on candidates (used by `agent-to-agent-influence`): question ids the candidate bears on; feeds `Backlog.base#This question` |
| `timing`, `summary` | *misalignment-prediction* only: when the prediction is made (see Tags); 2–3 sentence abstract-level summary from the search. There `manipulation` holds the signal the predictor reads and `outcome` what it predicts |
| `safety_use` | *misalignment-prediction*, internal-state-awareness sub-question only (see Tags; these candidates have `found_by: search/intro-…`); they also carry `summary`, with `manipulation` = how the state is accessed and `outcome` = the finding |
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
