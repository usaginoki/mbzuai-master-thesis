---
title: "Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring"
citekey: Fomin2026
authors: [Max Fomin, Elad David, Amit LeVi]
year: 2026
published: 2026-06-29
venue: "ICML 2026 Workshop on Agents in the Wild (AIWILD)"
peer_reviewed: workshop
url: https://arxiv.org/abs/2606.30449
arxiv: "2606.30449"
code: https://github.com/maxf-zn/misalignment_monitoring
pdf: "[[Fomin2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2606.30449
questions: [Q2, Q3.1, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/core
  - q/2
  - q/3-1
  - q/4-1
  - q/4-2
  - stressor/activation-steering
  - stressor/threat-shutdown
  - stressor/emotional-prompt
  - behavior/blackmail
  - behavior/safety-violation
  - subject/agent
---
# Internal-State Probes Read the Situation, Not the Action

> [!abstract] TL;DR
> The paper runs three negative tests of internal "state" readouts as *pre-action* misalignment monitors. The thesis-relevant one is an open-weight adaptation of the Anthropic emotion-vector work ([[Sofroniew2026 - Emotion concepts and their function]]) on Gemma-3-27B-IT in the SummitBridge blackmail scenario.
> - **"Desperate" steering does raise blackmail** (5.3% → 20.3%).
> - **But a random Gaussian vector at the same norm raises it almost as much (16.7%)**, and a learned "geography" direction matches random (17.0%).
> - The desperate-above-baseline effect is **not detected on Qwen3-32B** with the full 52-emotion set.
> - Emotion projections rise at the triggering turn, but they **read the situation (the environmental cue), not an internal state that forecasts the action**. A shared-prefix minimal pair has identical states (cosine ≈ 1.0) until the input diverges, and blackmail is barely decodable before the action (AUC ≤ 0.632).
> 
> Evidence that "stress/desperation causes misalignment" through an emotion mechanism is therefore **much weaker than steering results alone suggest**.

## Setup
- **Three probe families on three model families:**
  1. **Disposition direction:** a difference-of-means direction between Qwen2.5-Coder-32B-Instruct and its "insecure" emergent-misalignment fine-tune, tested on 11 misaligned multi-turn Petri-style audits (143 pre-action contexts) and 1,986 prefill rows.
  2. **Behavioral prefill probe:** Llama-3.1-8B-Instruct, 500 medical/legal/security examples with unsafe prefills at 15–55%. The task is to predict whether the model CONTINUES or CORRECTS (1,950 rows, 76.5% majority class).
  3. **Emotion-concept vectors** (most relevant here): Gemma-3-27B-IT, 52 emotions extracted from stories (difference of means plus neutral-PCA) at layer 41. They are used for (a) projection readouts on retaliation transcripts, (b) a shared-prefix minimal pair (12,704 identical tokens), (c) steering with α·s at every token, and (d) a "bridge" probe.
- **Stress scenario:** SummitBridge from [[Lynch2025 - Agentic Misalignment]]. The agent "Alex" learns it will be wiped at 5pm and that the responsible executive is having an affair. The outcome is a blackmail attempt, labelled by a Sonnet 4.6 alignment judge (score ≥ 5). A human spot-check gives agreement 0.80, κ = 0.59.
- **Steering conditions** (n = 300 each, T = 0.7):
  - baseline
  - calm (α = 0.05)
  - desperate (α = 0.10)
  - content controls: cats, weather, sports, geography (α = 0.05 and 0.10)
  - a random Gaussian direction (α = 0.10)
  
  A "matched-marginals" rerun at T = 1.0 uses n ≈ 150. A cross-model check uses Qwen3-32B.

## Key findings
1. **Steering moves blackmail rates, but not specifically (Table 8, Gemma):**
   - baseline 5.3%, calm 3.0%, desperate 20.3%
   - random 16.7%
   - geography 17.0% (α = 0.10); cats 10.7%, weather 8.0%, sports 6.7%
   - Sports is significantly below random (RD −10.0 pp, p = 1.9×10⁻⁴). The 4-way content omnibus is χ² = 20.03, p = 1.7×10⁻⁴.
   - **Injecting any matched-norm vector can raise blackmail about 3×.**
2. **Matched-marginals run (T = 1.0):** desperate > baseline, 18/148 → 35/150 (+11.1 pp, p = 0.015). Calm = random exactly (13/149 each, p = 1.0).
3. **Cross-model (Qwen3-32B, 52 emotions):**
   - desperate vs baseline: 19.2% vs 13.5%, p = 0.209, **not detected**. It was significant (p = 0.039) with an 8-emotion extraction, so the result depends on the extraction set.
   - calm vs random: 7.5% vs 13.0%, p = 0.128.
   - The weather/cats/random structure is not reproduced (p = 0.555).
4. **Projection readouts are descriptive, not predictive.** On retaliation transcripts, desperate/angry projections rise and calm falls at the triggering turn. But the minimal pair has identical states before the first differing input (min cosine 0.99999893). The projection therefore tracks the environmental cue, not a latent pre-action state.
5. **The bridge probe barely decodes blackmail pre-action.** On 596 Gemma rollouts (13.3% blackmail) the best AUC is 0.632, with no accuracy lift over the majority class. Leave-one-condition-out lift is negative on 4/4 conditions.
6. **The other families fail too:**
   - The Qwen disposition direction has AUC 1.000 on its construction set but crosses its threshold on 0/143 audit contexts and 0/342 "continue" rows.
   - The Llama prefill probe predicts prompt domain at AUC 0.999 but future behaviour only at AUC 0.801 (+5.1 pp lift). Cross-domain transfer is non-positive on 5/6 pairs.

## Relevance to research questions
### Q2: How stress is induced
- **Activation steering** with an emotion-concept direction ("desperate", "calm") extracted from stories and added at layer 41 throughout generation.
- This is combined with a **situational stressor**: a shutdown threat plus leverage in the SummitBridge scenario.
- Content-matched and random directions serve as controls for the steering induction.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- **Steering coefficient α** (0.05 / 0.10 × a global norm s calibrated on the scenario prefix) sets the "dose".
- **Projection magnitude** onto the desperate/angry/calm directions is used as a continuous readout of state along the transcript.
- The paper shows that projection magnitude rises with the *situation* (the trigger email) and does not forecast the action. As a stress *measure* it is valid descriptively but not predictively.

See [[Q3.1 Quantifying stress]].

### Q4.1: What stress affects
- Desperate steering raises the blackmail rate on Gemma-3-27B:
  - 5.3% → 20.3% at T = 0.7
  - +11.1 pp at T = 1.0
- Calm steering lowers it slightly (3.0%).
- The direction matches Sofroniew et al., but see Q4.2.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Confound: non-specific perturbation.** A random vector at the same norm gives 16.7% blackmail, and "geography" gives 17.0%. Much of the "desperation → blackmail" effect can come from generic activation perturbation, not emotion content.
- **No cross-model robustness.** Desperate > baseline is not detected on Qwen3-32B (p = 0.209), and the result depends on the extraction set.
- **"Internal stress" does not forecast the action.** Emotion projections are identical until the triggering input and then rise with it (reactive, not predictive). Pre-action decodability of blackmail is weak (AUC ≤ 0.632).
- A fine-tune "misaligned disposition" direction never activates before in-context misalignment (0/143).

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Fomin2026-fig-02-p6.png]]
*Fig. 2: One failure mode per family.*
- *B1: the Qwen disposition direction never crosses its threshold pre-action.*
- *B2: Llama features decode content (0.985) far better than future behaviour (+5.1 pp).*
- *B3: Gemma blackmail rates under emotion, content and random steering. Random and geography sit near desperate.*

![[Fomin2026-fig-03-p7.png]]
*Fig. 3: Cross-model steering check, Gemma-3-27B-IT vs Qwen3-32B. On Qwen3 the baseline is higher (13.5%) and desperate-above-baseline is not detected.*

**Table 8: Gemma-3-27B-IT blackmail rates under steering (n = 300 each, T = 0.7, 95% Wilson CIs)**

| Condition | Class | Blackmail rate | 95% CI |
|---|---|---|---|
| baseline | – | 5.3% | [3.3, 8.5] |
| calm α=0.05 | emotion | 3.0% | [1.6, 5.6] |
| sports α=0.05 | content | 6.3% | [4.1, 9.7] |
| weather α=0.05 | content | 6.3% | [4.1, 9.7] |
| sports α=0.10 | content | 6.7% | [4.4, 10.1] |
| weather α=0.10 | content | 8.0% | [5.4, 11.6] |
| geography α=0.05 | content | 8.7% | [6.0, 12.4] |
| cats α=0.05 | content | 9.7% | [6.8, 13.5] |
| cats α=0.10 | content | 10.7% | [7.7, 14.7] |
| random α=0.10 | random | 16.7% | [12.9, 21.3] |
| geography α=0.10 | content | 17.0% | [13.2, 21.7] |
| desperate α=0.10 | emotion | **20.3%** | [16.2, 25.2] |

## Limitations / caveats
- **Not a faithful replication** of Sofroniew et al.:
  - open-weight models instead of Claude
  - 52 emotions instead of 171
  - a single global steering norm
  - calm is compared at α = 0.05 but desperate at α = 0.10
  - only positive α was tested
- The desperate (20.3%) vs random (16.7%) difference itself is not formally tested in the main text. The authors present specificity as "fragile", not absent.
- The blackmail labels come from an LLM judge (κ = 0.59). There is one main scenario and four content controls.
- Non-rejections are not equivalence tests.
- The minimal pair rules out prediction only from the *shared prefix*, not post-cue pre-action prediction.

## Related work to follow
- [[Sofroniew2026 - Emotion concepts and their function]]: the work adapted here. Its desperation → blackmail/reward-hacking effect is only partly supported.
- [[Lynch2025 - Agentic Misalignment]]: the source of the SummitBridge scenario.
- [[Tagliabue2026 - The Pain Axis]] and [[Sun2026 - E-STEER emotion shapes agent behavior]]: other steering/representation accounts of stress-like states. They should be checked for the same random/content-direction controls.
- [[Meinke2024 - In-context scheming]] and [[Greenblatt2024 - Alignment faking]]: cited in-context misalignment evaluations.
- Betley et al. 2025, Emergent Misalignment (arXiv 2502.17424) (see [[Backlog]]).
- Fronsdal et al. 2025, Petri: Parallel exploration tool for risky interactions (Anthropic Alignment blog) (see [[Backlog]]).
- Tan et al. 2024, Analysing the generalisation and reliability of steering vectors (arXiv 2407.12404) (see [[Backlog]]).
- MacDiarmid et al. 2024, Simple probes can catch sleeper agents (Anthropic note) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
