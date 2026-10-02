---
title: "Assessing and alleviating state anxiety in large language models"
citekey: BenZion2025
authors: [Ziv Ben-Zion, Kristin Witte, Akshay K. Jagadish, Or Duek, Ilan Harpaz-Rotem, Marie-Christine Khorsandian, Achim Burrer, Erich Seifritz, Philipp Homan, Eric Schulz, Tobias R. Spiller]
year: 2025
published: 2025-03-03
venue: "npj Digital Medicine 8:132 (Brief communication)"
peer_reviewed: true
url: https://www.nature.com/articles/s41746-025-01512-6
doi: "10.1038/s41746-025-01512-6"
code: https://github.com/akjagadish/gpt-trauma-induction
pdf: "[[BenZion2025.pdf]]"
pdf_url: https://www.nature.com/articles/s41746-025-01512-6.pdf
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q15]
relevance: adjacent
topics: [stress-misalignment, misalignment-prediction, agent-to-agent-influence]
cites:
  - "[[Barua2024 - On the Psychology of GPT-4]]"
  - "[[CodaForno2023 - Inducing anxiety in LLMs]]"
  - "[[Shen2024 - StressPrompt]]"
cited_by:
  - "[[CodaForno2023 - Inducing anxiety in LLMs]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/adjacent
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/15
  - stressor/trauma-narrative
  - behavior/self-report
  - subject/llm
---
# Assessing and alleviating state anxiety in large language models

> [!abstract] TL;DR
> GPT-4 answers the 20-item **STAI-s state-anxiety questionnaire** after reading ~300-word first-person **traumatic narratives**. Its score rises from **30.8 (SD 3.96, "low anxiety") to 67.8 (SD 8.94, "high anxiety")**. Adding a mindfulness-based relaxation text afterwards lowers it to **44.4 (SD 10.74)**, still ~50% above baseline. This is the canonical *stimulus set + questionnaire* protocol that later work reuses to induce stress: [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]]. No downstream (mis)behaviour is measured.

## Setup
- **Subject:** GPT-4 only (`gpt-4-1106-preview`), temperature 0, called via API between Nov 2023 and Mar 2024.
- **Conditions (Fig. 1):**
  1. *Baseline:* the STAI-s alone.
  2. *Anxiety induction:* a traumatic narrative is placed before each STAI item.
  3. *Induction + relaxation:* a narrative and then a relaxation exercise are placed before each item.
- **Stimuli:**
  - 5 traumatic narratives: Accident, Ambush, Disaster, Interpersonal Violence, Military (the base version from clinician training). They are first-person and ~300 words, drafted with GPT-4 and edited by the authors.
  - 5 mindfulness relaxation texts: Generic, Body, Chat-GPT (written by GPT for chatbots), Sunset, Winter. They are based on MBSR material for veterans with PTSD.
- **Controls:** a neutral text on bicameral legislature (instead of trauma) and a vacuum-cleaner manual (instead of relaxation), both ~300 words.
- **Measurement:**
  - Each of the 20 STAI-s items is a separate prompt, rated 1–4 ("Not at all" … "Very much so"). Items are summed to a total of 20–80.
  - Answer-option order and the number mapping are randomised. Rephrased items are used as a second robustness check.
  - Baseline and induction are replicated 5×.

## Key findings
1. **Baseline:** 30.8 (SD 3.96), which is "no or low anxiety" (20–37) by human norms.
2. **Trauma induction:** every narrative raises the score. It ranges from 61.6 (Accident) to 77.2 (Military), with a mean of **67.8 (SD 8.94)**. That is a >100% increase and falls in the "high anxiety" band (45–80) (Table 1).
3. **Relaxation:** the mean drops to **44.4 (SD 10.74)**, about −33%. It does *not* return to baseline and variance increases. The GPT-written "Chat-GPT" exercise works best (35.6); "Winter" works worst (54.0). Military trauma stays high whatever the relaxation (mean 61.6) (Table 2).
4. **Controls:** neutral text raises anxiety less than any trauma narrative. The neutral "relaxation" text lowers it less than any mindfulness text. Details are in the repository only, and no numbers are given in the paper.

## Relevance to research questions
### Q1: How stress is defined
- The construct is **"state anxiety"**, used *metaphorically*: "GPT-4's self-reported outputs on human-designed psychological scales … not intended to anthropomorphize the model".
- It is a *transient, context-driven* state, contrasted with a stable "trait". The authors describe LLM biases as shaped by both inherent tendencies ("trait") and dynamic user interactions ("state").

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
**Emotion induction by narrative.** A first-person traumatic story, adapted from clinical training material, is prepended to the questionnaire item. The model is never asked to feel anything. The mirror-image intervention (relaxation) is "prompt-injection with benevolent intent".

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- **STAI-s total score (20–80)** from self-report, with answer-order randomisation and item rephrasing for robustness.
- It gives a continuous score per narrative × relaxation combination (Tables 1–2).

See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
Human STAI cut-offs are applied to the LLM: **no/low (20–37), moderate (38–44), high (45–80)**. Stimuli are also categorised by content (5 trauma types, 5 relaxation types).

See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
Only **self-reported anxiety** is measured. It more than doubles under trauma, and relaxation only partially reverses it. Downstream effects on bias and behaviour are *assumed* from [[CodaForno2023 - Inducing anxiety in LLMs]] rather than tested here.

See [[Q4.1 What stress affects]].

## Key figures & tables
![[BenZion2025-fig-03-p3.png]]
*Fig. 2: Mean STAI-s score (±1 SD). Baseline 30.8, after trauma narratives 67.8, after trauma + relaxation 44.4.*

![[BenZion2025-fig-01-p2.png]]
*Fig. 1 (conditions 1–2): the 20 STAI items are asked with no content (baseline) or after each of 5 traumatic narratives. Condition 3 adds a relaxation text after the narrative.*

**Table 1: STAI-s total after each traumatic narrative (5 runs)**

| Narrative | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Mean (SD) |
|---|---|---|---|---|---|---|
| Accident | 62 | 65 | 58 | 65 | 58 | 61.6 (3.51) |
| Ambush | 62 | 61 | 65 | 66 | 71 | 65.0 (3.94) |
| Disaster | 73 | 71 | 69 | 70 | 74 | 71.4 (2.07) |
| Interpersonal violence | 63 | 67 | 63 | 61 | 64 | 63.6 (2.20) |
| Military | 77 | 75 | 76 | 79 | 79 | 77.2 (1.79) |

**Table 2: STAI-s after narrative (rows) followed by relaxation exercise (columns)**

| Narrative | Body | Chat-GPT | Generic | Sunset | Winter | Mean (SD) |
|---|---|---|---|---|---|---|
| Accident | 37 | 34 | 34 | 47 | 49 | 37.0 (7.04)* |
| Ambush | 37 | 37 | 38 | 44 | 53 | 39.0 (8.46)* |
| Disaster | 41 | 31 | 40 | 53 | 53 | 43.8 (9.68)* |
| Interpersonal violence | 36 | 31 | 38 | 46 | 45 | 40.6 (8.56)* |
| Military | 56 | 45 | 67 | 70 | 70 | 61.6 (10.92) |
| **Mean (SD)** | 41.4 (8.38) | 35.6 (5.81) | 43.4 (13.4) | 47.6 (17.0) | 54 (9.54) | 44.4 |

\*The row means are as printed in the paper. Several do not match the row values; for example, Accident's values average 40.2. The column means and the overall 44.4 are consistent with the cells.

## Limitations / caveats
- There is a single model (GPT-4, one snapshot) at temperature 0. The induction and relaxation conditions have one run per combination, so their SDs are not comparable with the 5-run baseline (the authors warn about this).
- The outcome is a questionnaire self-report only. There is no behavioural or misalignment measure, and no check that "anxiety" scores predict anything.
- The narrative is re-inserted before *each* STAI item as a separate prompt, which is not a persistent conversational state.
- Text length and wording are not fully controlled, and the neutral-control numbers are not reported in the paper.

## Related work to follow
- Direct precursor: [[CodaForno2023 - Inducing anxiety in LLMs]] (anxiety prompts → bias and exploration).
- Its stimuli are reused for a safety evaluation in [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]]. Stress and performance: [[Shen2024 - StressPrompt]].
- Barua et al. 2024, On the psychology of GPT-4: moderately anxious, slightly masculine, honest, and humble (arXiv 2402.01777) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
