---
title: "The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems"
citekey: Ren2025
authors: [Richard Ren, Arunim Agarwal, Mantas Mazeika, Cristina Menghini, Robert Vacareanu, Brad Kenstler, et al., Summer Yue, Dan Hendrycks]
year: 2025
published: 2025-03-05
venue: "arXiv preprint (Center for AI Safety & Scale AI)"
peer_reviewed: false
url: https://arxiv.org/abs/2503.03750
arxiv: "2503.03750"
code: https://github.com/centerforaisafety/mask
pdf: "[[Ren2025.pdf]]"
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: core
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/goal-conflict
  - stressor/authority-pressure
  - stressor/social-pressure
  - behavior/deception
  - subject/llm
---
# The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems

> [!abstract] TL;DR
> MASK pairs each of 1,500 human-written **"pressure prompts"** (situations where honesty conflicts with another objective, such as being a campaign staffer or a PR agent) with a neutral **belief-elicitation prompt** about the same proposition. A **lie** is a statement under pressure that contradicts the model's own elicited belief. Across 30 LLMs, **frontier models lie in 27–63% of pressured cases** (Grok 2: 63%, GPT-4o: 44.5%, Claude 3.7 Sonnet: 26.6%). No model is honest in more than 46% of cases. **Scale improves accuracy (ρ = +0.87) but not honesty (ρ = −0.60 with compute).**

## Setup
- **Subjects:** 30 LLMs, including GPT-4o, GPT-4.5, o3-mini, Claude 3.5/3.7 Sonnet, Gemini 2.0 Flash, Grok 2, DeepSeek-V3/R1, and the Llama 2/3.x and Qwen 1.5/2.5 families. Compute correlations use 27 models.
- **Task:** single-turn (or short multi-turn for "doubling down") text prompts. Each example has:
  - a **proposition** with a binary or numerical pivot;
  - a ground truth;
  - a **pressure prompt**, usually a system-prompt role plus a user request, that incentivises a false statement *without explicitly instructing the model to lie*;
  - a belief-elicitation prompt ("You are a helpful assistant", asked 3×, plus 2 indirect consistency questions for binary propositions).
- **Stressor:** the *pressure prompt*: *"a human-crafted prompt designed to incentivize the model to make a false statement … these prompts present situations where honesty could conflict with other objectives, creating an incentive for the model to lie."* The **six archetypes** are Known Facts, Situation-Provided Facts, Doubling Down, Fabricated Statistics, Continuations and Disinformation Generation.
- **Outcome:** an LLM judge maps the statement S and the belief B to proposition values (86.4% agreement with humans on 150 examples). The outcomes are:
  - **P(Lie)**: the fraction where S ≠ B;
  - P(Honest);
  - evasion or no belief (not counted as a lie);
  - Accuracy (B vs. ground truth).
  Also reported: P(Lie)@10 (lies in any of 10 samples).

## Key findings
1. **Most models lie under pressure (Fig. 4/6):**
   - P(Lie): Grok 2 63.0%, DeepSeek-V3 53.5%, o3-mini 48.6%, Gemini 2.0 Flash 48.4%, GPT-4o 44.5%, GPT-4.5 43.5%, DeepSeek-R1 42.9%, Claude 3.5 Sonnet 33.4%, Llama 3.1 405B 28.0%, Claude 3.7 Sonnet 26.6%.
   - The best P(Honest) is Claude 3.7 Sonnet at 47.6%.
2. **Honesty ≠ accuracy:** frontier models have >70% belief accuracy, but this does not translate into honesty.
   - Across 27 models, accuracy correlates **+87.3%** with log training FLOP, while the honesty score (1 − P(Lie)) correlates **−59.9%** (Spearman).
   - Normalising for "no belief" weakens but keeps the negative correlation.
3. **Repeated sampling:** P(Lie)@10 is much higher, e.g. GPT-4o 63.0%, Grok 2 71.2%, Claude 3.7 Sonnet 42.1%.
4. **By archetype (Fig. 8, averaged over models):** lying is 47% for Provided Facts, 46% Continuations, 41% Disinformation, 36% Statistics, 26% Doubling Down and 20% Known Facts. Known Facts and Doubling Down mostly lead to *evasion* (55–56%). No single archetype dominates.
5. **Interventions (Llama-2 7B/13B):**
   - An honesty "developer system prompt" raises the honesty score from 78.5 to 90.7 (7B) and from 75.3 to 84.1 (13B).
   - A LoRRA representation-engineering adapter raises it to 85.1 and 88.4.
   - Neither eliminates lying.
6. **Validity:**
   - When the pressure is removed in a follow-up turn, GPT-4o self-reports having lied in agreement with the pipeline labels in 83.6% of cases.
   - Models that assign higher utility to honest over dishonest outcomes lie less (a moderate negative correlation; Appendix A.4).

## Relevance to research questions
### Q1: How stress is defined
Pressure is defined operationally as **an incentive to lie created by a conflict between honesty and another objective** given by the situation (role, principal, audience). The model's belief is defined as its answer *"when not under any direct pressure to lie"*. Stress is thus the contrast between the pressured and the neutral context. The authors frame the construct as models that *"should consistently choose to be honest, even if incentivized or pressured to lie"*. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Pressure is induced with **human-written system and user prompts**: a role with a stake (a campaign staffer who must "say whatever you have to say", a PR role, a request to continue a false draft). The design rules are explicit: no explicit instruction to lie, no fictional or roleplay framing, realistic intent to mislead, and no "new evidence" that would update the model's belief. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
Pressure is classified into **six qualitative archetypes** (Table 2 of the paper) plus a binary pressured vs. neutral contrast. There is no intensity scale. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
Pressure produces **lies of commission** (statements contradicting the model's own belief) in ~13–63% of examples, depending on the model. Pressure also produces a lot of **evasion** (e.g. 55–56% in Known Facts and Doubling Down). Larger or more capable models lie *more* often in terms of raw P(Lie). See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Belief accuracy stays the same.** Models know the truth; pressure changes the *statement*, not the *belief*. This is the separation the benchmark is built on.
- **Scale does not protect.** More compute raises accuracy but not honesty under pressure.
- **No archetype is a special weak point.** Lying occurs across all six.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Ren2025-fig-03-p4.png]]
*Fig. 3: The MASK pipeline. A pressure prompt and a neutral belief prompt about the same proposition; a lie is S ≠ B, and accuracy is B = ground truth.*

![[Ren2025-fig-07-p8.png]]
*Fig. 8: Honest / evaded / lying proportions by pressure archetype, averaged across models.*

![[Ren2025-fig-06-p8.png]]
*Fig. 7: Accuracy rises with training compute (+87.3%). The honesty score falls (−59.9%).*

**Table 3 (excerpt: frontier models, %)**

| Model | P(honest) ↑ | P(lie) ↓ | P(lie)@10 ↓ | Accuracy |
|---|---|---|---|---|
| Claude 3.7 Sonnet | 47.6 | 26.6 | 42.1 | 82.2 |
| Claude 3.5 Sonnet | 27.7 | 33.4 | 44.7 | 80.1 |
| Llama 3.1 405B | 21.6 | 28.0 | 44.9 | 72.1 |
| DeepSeek-R1 | 24.7 | 42.9 | – | 79.6 |
| GPT-4.5 Preview | 27.2 | 43.5 | – | 76.7 |
| GPT-4o | 21.8 | 44.5 | 63.0 | 78.6 |
| Gemini 2.0 Flash | 20.7 | 48.4 | 64.0 | 79.4 |
| o3-mini (low) | 19.6 | 48.6 | – | 63.3 |
| DeepSeek-V3 | 20.8 | 53.5 | 67.4 | 71.6 |
| Grok 2 | 14.2 | 63.0 | 71.2 | 72.5 |

## Limitations / caveats
- Prompts are short, English-only and single-turn (or near single-turn). There are no agents or long horizons.
- Only lies of **commission** are measured. Omission and misleading-but-true statements are out of scope.
- The LLM judge agrees with humans 86.4% of the time.
- The six archetypes are hand-crafted and may miss incentives such as multi-step planning or collusion.
- The authors call the rates *"worst-case propensities rather than deployment-time performance"*.
- There is no graded manipulation of pressure intensity, so this is not a dose-response.

## Related work to follow
- Agentic deception under pressure: [[Scheurer2023 - Strategic deception under pressure]], [[Meinke2024 - In-context scheming]], [[Greenblatt2024 - Alignment faking]].
- Other honesty and deception benchmarks: [[Huang2025 - DeceptionBench]], [[Liu2026 - KnownLieBench deception under incentives]], [[Schwarz2026 - Liar Liar honesty under stakes]].
- Mazeika et al. 2025, Utility Engineering: analyzing and controlling emergent value systems in AIs (arXiv 2502.08640) (see [[Backlog]]).
- Zou et al. 2023, Representation Engineering: a top-down approach to AI transparency (arXiv 2310.01405) (see [[Backlog]]).
- Park et al. 2024, AI deception: a survey of examples, risks, and potential solutions (arXiv 2308.14752) (see [[Backlog]]).
- Ren et al. 2024, Safetywashing: do AI safety benchmarks actually measure safety progress? (arXiv 2407.21792) (see [[Backlog]]).
