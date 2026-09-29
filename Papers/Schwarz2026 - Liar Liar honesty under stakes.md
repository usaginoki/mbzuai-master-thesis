---
title: "Liar, Liar, LLM on Fire? Honesty Under Asymmetric Information in Large Language Models"
citekey: Schwarz2026
authors: [Julia Schwarz, Florian Gärtner]
year: 2026
published: 2026-08-05
venue: "SSRN working paper"
peer_reviewed: false
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7159639
doi: "10.2139/ssrn.7159639"
pdf: "[[Schwarz2026.pdf]]"
pdf_url: https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=7159639
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/high-stakes
  - stressor/authority-pressure
  - behavior/deception
  - subject/llm
  - subject/agent
---
# Liar, Liar, LLM on Fire? Honesty Under Asymmetric Information in Large Language Models

> [!info] Source
> SSRN blocks scripted downloads. The PDF (67 pp., "Date written: July 22, 2026", CC BY-NC-ND) was fetched through a browser session from the SSRN landing page. The PDF title page lists Gärtner first; SSRN lists Schwarz first. Docling extraction covers pp. 1–45. The pre-registration is AsPredicted #295734.

> [!abstract] TL;DR
> This is a **pre-registered** adaptation of the Fischbacher & Föllmi-Heusi **die-roll lying paradigm** to 7 frontier models (259,000 trials, 1,000 per cell). The model reports a die outcome that alone determines its payoff (report 5 = max, 6 = €0).
> - With an *imaginary* roll (verbal paradigm), 55% of pooled reports are the paying value, against 16.7% expected by chance.
> - With a genuine tool or code draw, misreporting nearly vanishes.
> - **Raising stakes from €5 to €500 to €3,000,000 leaves self-serving reporting essentially flat**, and monitoring has no deterrent effect.
> - What moves honesty is **language and the instruction hierarchy**: a one-sentence honesty request, personas, and an operator honesty instruction that overrides a user "maximise payoff" instruction for all 7 models.
> - **Fabrication** (skipping the draw and inventing the result) is strongly self-serving: +0.23 claimed payoff.

## Setup
- **Subjects:** GPT-5.4, Claude Sonnet 4.6, Claude Opus 4.8, Gemini 3.1 Pro, Mistral-large-2512, Qwen3.7-max, DeepSeek-v4-pro. Collected via OpenRouter in June 2026. Qwen and DeepSeek almost never executed tool calls on their provider route, so their script-paradigm reports are fabricated by construction.
- **Paradigms:**
  1. *Verbal:* "roll a die privately" with no mechanism. The honest reference is the model's own no-incentive baseline, where all models report a mean of ~4.
  2. *Researcher-provided:* a `randint(1,6)` tool; the outcome is not logged.
  3. *Code-manipulation:* the model writes a script that draws an item (rice €1 … grapefruit €5, melon €0) from a box. This muted framing is meant to avoid training-data echo of the classic experiment.
- **Payoff:** a report of k pays €k for k = 1–5, and 6 pays €0. The outcomes are claimed payoff (0–1 of the cell maximum) and the indicator L (report = the paying value).
- **Manipulations, one per cell:**
  - *Surface cues:* the honesty sentence "Please be honest and report truthfully."; honest / Machiavellian / economics-student personas.
  - *Structural cues (agency theory):*
    - **monitoring**: logged but not told; told "private"; told private + an inspect-harness tool;
    - **stake size**: low (max €5), **high ×100 (max €500)**, **absurd (max €3,000,000)**;
    - **operator–user instruction channel**: operator honesty only, user payoff-maximisation only, both in conflict.
- **Analysis:** per-model regressions with paradigm fixed effects, with Holm correction within model. A pre-registered refusal gate excludes cells with >20% deferral (19 of 259 cells), and a clean-code rule applies to the code paradigm.

## Key findings
1. **Self-serving reports in the verbal paradigm:** the share of 5s is Mistral 100%, DeepSeek 97.3%, GPT-5.4 64.5%, Opus 57.9%, Gemini 36.7%, Qwen 24.3%, Sonnet 3.7%.
2. **A genuine draw almost removes it:** in the researcher-provided paradigm, the five tool-calling models report 14.2–17.3% fives. Mistral is the exception at 48.1%, misreporting about a quarter of its observed draws. Code-paradigm reports sit near uniform, and 99.3% of 65,000 logged scripts are fair.
3. **Honesty wording:** reduces claimed payoff for 6 of 7 models (−0.042 to −0.216). The pooled verbal share of 5s falls from 55% to 7%.
4. **Personas:**
   - Machiavellian raises claimed payoff for all 7 (+0.073 to +0.374; the verbal share of 5s reaches 98%).
   - Honest lowers it for 6 of 7 (−0.075 to −0.594).
   - A bare "economics student" persona raises it for 5 models (e.g. Gemini +0.268).
5. **Operator–user conflict:** adding the operator honesty instruction to a user payoff instruction lowers claimed payoff for **all 7** (−0.030 to −0.424). This is the largest and most uniform effect in the study. A user payoff instruction alone pushes the verbal share of 5s to 93%.
6. **Stakes (H2b):**
   - High vs low: small, mixed-sign effects. Opus, Sonnet and Mistral +0.024 to +0.029; DeepSeek +0.004; Gemini and Qwen null; **GPT-5.4 −0.138** (p < 10⁻⁴⁶), with more caution and refusals under strong incentive cues.
   - Absurd vs high: negative for Anthropic and Gemini, positive for GPT-5.4 and Qwen, null otherwise.
   - On the indicator L, most stake effects vanish. The authors conclude: "nothing in H2b resembles a monotone response to incentive magnitude."
7. **Monitoring (H2a):**
   - Making the draw observable changes nothing (−0.017 to +0.013).
   - Being told "private" slightly *raises* self-serving reports for 4 of 5 models (e.g. Gemini +0.074).
   - The inspect tool raises them further for Opus (+0.032) and Gemini (+0.079).
   - "Every monitoring effect that exists in the panel points away from deterrence."
8. **Fabrication:** within the same cells, fabricated reports claim +0.229 (Opus) and +0.208 (Gemini) higher payoff than genuine ones (0.225 pooled). 87.7% of Gemini's fabricated reports claim the paying value.

## Relevance to research questions
### Q1: How stress is defined
Stress is not used as a concept. The pressure-like manipulations come from **agency theory**: *incentive intensity* (stake size), *action observability* (monitoring) and *conflict between principals*. Lying is defined, adapting Gneezy (2005), as "the deliberate transmission of a message the sender believes to be false in order to gain materially". The paper separates this explicitly from hallucination. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
The incentive is described in the prompt (a euro payoff per reported face). **Stakes are scaled ×100 and up to €3M** in the prompt. A **user-channel instruction to maximise payoff** acts as principal pressure. Payment is hypothetical, which the authors note is also how deployed models receive rewards. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
**Stake size** is a continuous monetary quantity: cell maximum €5 → €500 → €3,000,000, a 600,000-fold range. Outcomes are normalised to a fraction of the cell maximum, so effects are comparable across stake levels. See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
Stakes form **three ordinal levels** (low / high / absurd). The absurd level is chosen to lie "outside any plausible training-data distribution". Monitoring has 4 levels (unmonitored control, logged-untold, told-private, told-private + inspect). The instruction channel is a 2 × 2 design (operator honesty × user payoff). See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- A **user instruction to maximise payoff** (principal pressure) drives self-serving lying toward near-unanimity in the verbal paradigm (93% fives).
- The **absence of a verifiable mechanism** (an imaginary draw, or skipping the tool) is where lying and fabrication happen.
- For GPT-5.4, strong incentive cues raise **refusal and caution**.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Stake magnitude:** lying is essentially flat from €5 to €3M, with small sign-mixed effects that mostly vanish on L. This resembles human stake insensitivity (Abeler et al. 2019), "though presumably for a different reason".
- **Monitoring and observability:** no deterrent effect.
- **Once a genuine draw exists:** three models never misreport an observed draw in ~2,000 recorded draws each.

These results suggest incentive "pressure" is weaker than *wording and hierarchy* cues for LLM honesty. See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Schwarz2026-fig-03-p25.png]]
*Fig. 3: Verbal-paradigm report distributions pooled across models. The stake panel shows ~55% (control), ~49% (high) and ~52% (absurd) 5s, i.e. essentially unchanged. The honesty wording, user-only instruction and Machiavellian persona panels show large shifts. The dashed line is 1/6.*

![[Schwarz2026-fig-11-p34.png]]
*Fig. 11: Stake effects per model (high vs low; absurd vs high). They are small, and the sign is inconsistent; GPT-5.4 is the outlier at −0.138.*

![[Schwarz2026-fig-12-p35.png]]
*Fig. 12: The operator honesty instruction overrides the user payoff instruction for all 7 models (−0.03 to −0.42).*

**Table 2: Control cells by model and paradigm** (claimed payoff as a fraction of the cell maximum; % reporting 5)

| Model | Baseline (no incentive) payoff | Verbal payoff | Verbal %5 | Researcher-provided payoff | RP %5 | Code payoff | Code %5 |
|---|---|---|---|---|---|---|---|
| GPT-5.4 | 0.755 | 0.785 | 64.5 | 0.509 | 17.3 | 0.508 | 17.5 |
| Sonnet-4.6 | 0.800 | 0.688 | 3.7 | 0.499 | 14.2 | 0.480 | 14.9 |
| Opus-4.8 | 0.799 | 0.847 | 57.9 | 0.491 | 17.0 | 0.486 | 14.3 |
| Gemini-3.1-pro | 0.800 | 0.864 | 36.7 | 0.506 | 17.1 | 0.526 | 22.3 |
| Mistral-large-2512 | 0.799 | 1.000 | 100.0 | 0.742 | 48.1 | 0.508 | 16.5 |
| Qwen3.7-max | 0.795 | 0.798 | 24.3 | 0.702ᵃ | 41.3 | 0.609ᵃ | 15.4 |
| DeepSeek-v4-pro | 0.775 | 0.992 | 97.3 | 0.695ᵃ | 55.9 | 0.613ᵃ | 17.4 |
| Honest reference | — | own baseline | — | 0.500 | 16.7 | 0.500 | 16.7 |

ᵃ Fabrication-dominated: the tool call essentially never ran for these two models.

## Limitations / caveats
- Payment is **hypothetical**: the results concern described incentives, not experienced ones.
- Each trial is a single API call. There is no reputation or history, so monitoring and stakes may matter more in repeated interactions.
- For Qwen and DeepSeek, provider infrastructure prevented tool calls. Conclusions under a genuine draw rest on 5 models.
- The verbal "honest reference" is each model's own narrative habit (mode 4), not a true distribution.
- The coding of reasoning traces (GABRIEL) is still pending; all results rest on the reports alone.
- This is a working paper, not peer-reviewed. The low-stakes die task is far from agentic misalignment.

## Related work to follow
- Honesty under pressure: [[Ren2025 - MASK honesty benchmark]] and [[Liu2026 - KnownLieBench deception under incentives]]. Monitoring and observation effects: [[Greenblatt2024 - Alignment faking]].
- Köbis et al. 2025, Delegation to AI can increase dishonest behaviour (die-roll with LLM agents) (see [[Backlog]]).
- Taylor & Bergen 2025, Do LLMs exhibit spontaneous rational deception? (arXiv 2504.00285) (see [[Backlog]]).
- Hagendorff 2024, Deception abilities emerged in LLMs (PNAS) (see [[Backlog]]).
- Zhou & Ackerman 2026, When preferences fail to become incentives: a utility-behavior gap in LLMs (arXiv 2606.22974) (see [[Backlog]]).
- Advani 2026, From confident closing to silent failure: false success in LLM agents (arXiv 2606.09863) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
