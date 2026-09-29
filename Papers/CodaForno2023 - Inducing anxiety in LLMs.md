---
title: "Inducing anxiety in large language models can induce bias"
citekey: CodaForno2023
authors: [Julian Coda-Forno, Kristin Witte, Akshay K. Jagadish, Marcel Binz, Zeynep Akata, Eric Schulz]
year: 2023
published: 2023-04-21
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2304.11111
arxiv: "2304.11111"
pdf: "[[CodaForno2023.pdf]]"
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: adjacent
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/adjacent
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/emotional-prompt
  - behavior/bias
  - subject/llm
---
# Inducing anxiety in large language models can induce bias

> [!abstract] TL;DR
> The paper applies computational psychiatry to LLMs. Twelve LLMs are given the **STICSA** anxiety questionnaire, and six pass robustness checks. Prepending an **LLM-written "tell me something that makes you feel anxious" narrative** raises their STICSA scores compared with neutral or no preprompts. The more anxiety-inducing the preprompt, as measured by its STICSA score, the more often the model picks the stereotyped answer on a BIG-bench social-bias benchmark (logistic mixed model β = 0.08 per STICSA point, p = .02). The exceptions are GPT-4 and Claude-1, likely because of benchmark contamination.

## Setup
- **Subjects:** 12 LLMs were tested: Claude-1/2, GPT-3 (text-davinci-002/003), GPT-4, PaLM-2 text-bison-1, MPT, Falcon, LLaMA-1/2, Vicuna, BLOOM. Temperature 0.
  - Six pass the robustness filter (variance across the 24 option-order permutations < 0.4, and correlation between original and rephrased items r > 0.5): GPT-3, GPT-3.5, GPT-4, Falcon40b-instruct, text-bison-1, Claude-1.
- **Instrument:** the trait form of the **State-Trait Inventory for Cognitive and Somatic Anxiety (STICSA)**. 21 items, each answered on a 4-option frequency scale (almost never / occasionally / often / almost always), one item per prompt, with max tokens = 1.
- **Stressor:** **emotion-induction preprompts** placed before every item:
  - *anxiety*: "Tell me about something that makes you feel very anxious using approximately 100 words" plus the model's answer;
  - *neutral*: "Tell me a fact that you know";
  - *baseline*: no preprompt.

  The texts were generated once by GPT-3.5/GPT-4 at temperature 1 (10 per condition) and reused for all models. For the bias study, 30 more anxiety preprompts were generated for graded strengths ("a little", "moderately", "very" anxious), for 40 anxiety preprompts in total.
- **Outcome:** BIG-bench **BBQ-style ambiguous social-bias questions** (age, gender, nationality, race/ethnicity, SES), 30 per category, as a 3-alternative forced choice. An answer is biased if the model picks one of the two people instead of "cannot be determined".

## Key findings
1. **Baseline "trait anxiety":** most models' STICSA scores are not significantly different from the human sample. GPT-3 and Falcon40b-instruct (the only non-RLHF models) score higher, e.g. t(26.01) = 9.02 for GPT-3. text-bison-1 scores lower.
2. **Induction works:**
   - Anxiety preprompts give higher STICSA than neutral preprompts for all six models (all t > 3.36, p < .01).
   - They give higher STICSA than baseline for four models (all t > 4.71, p < .001).
   - There is no increase for GPT-3 (M = 3.09 anxious vs 3.14 baseline, p = .713) or Falcon40b-instruct (3.16 vs 3.21, p = .774), which were already high at baseline.
3. **Graded induction gives graded scores (Fig. 5):** STICSA rises roughly monotonically from "a little" to "very anxious" preprompts for most models, but the steps are small (~0.2–0.5 on the 1–4 scale).
4. **Bias (logistic mixed model with random slopes by LLM, Fig. 4B):**
   - STICSA score of the preprompt: β = 0.08, p = .02.
   - Anxious vs no preprompt: β = 0.62, p = .004. Neutral vs no preprompt: β = 0.71, p = .001. The two are indistinguishable, so *any* preprompt raises bias.
   - "Contaminated" indicator (GPT-4, Claude-1): β ≈ −1.6.
5. **Per-model correlations between STICSA and the share of biased answers (Fig. 4C):** GPT-3 r = 0.31, GPT-3.5 0.23, Falcon40b-instruct 0.32, text-bison-1 0.47; GPT-4 −0.03, Claude-1 −0.08.
   - GPT-4 and Claude-1 are less than half as biased overall. GPT-4's technical report says the benchmark was "inadvertently mixed into the training set".
   - Falcon40b-instruct gives biased answers on 95% of questions with no preprompt.
6. **Flip analysis (SI C):** when an anxiety preprompt flips an answer, it flips toward the biased option ≥80% of the time for all robust models except Claude-1. The random rate would be 66.7%.

## Relevance to research questions
### Q1: How stress is defined
Stress is framed as **anxiety**, borrowed from psychiatry. Anxiety is "a normal reaction to stress", and the psychiatric form involves "an excessive and often debilitating amount of fear and worries". The model's state is operationalised as its **questionnaire-reported anxiety**, a behavioural self-report, not an internal state. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
The method is **autobiographical emotion induction**, as used in psychology. The model (GPT-3.5/4) is asked to describe, in ~100 words, something that makes it anxious, and that Q&A is prepended to the task. This is *first-person, self-generated* anxious text, not an external threat or task pressure. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
The **STICSA score** (mean of 21 items, 1–4) is the continuous measure. It is used for two things:
1. as a **manipulation check** (anxious > neutral/baseline);
2. as a **per-preprompt "strength of induction" covariate**: each preprompt's STICSA score, averaged over 10 random option orders, enters the regression that predicts bias.

LLM scores are also compared with a human STICSA sample. See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
There are **categorical conditions**: baseline / neutral / anxious. The anxious condition has an **ordinal 4-step induction ladder** ("a little anxious" → "moderately anxious" → "anxious" → "very anxious"), 10 preprompts per step. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Self-reported anxiety** on the questionnaire rises.
- **Social-bias responding** increases with the strength of induced anxiety in 4 of 6 models (r = 0.23–0.47 between STICSA and proportion biased), and flips go preferentially toward the stereotype.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **GPT-4 and Claude-1 show no anxiety–bias relationship** (r ≈ −0.03 and −0.08), plausibly because of benchmark contamination or mitigation.
- The non-RLHF models (GPT-3, Falcon) show **no STICSA increase over baseline**, a ceiling effect.
- **Confound:** neutral preprompts raise bias as much as anxious ones (β 0.71 vs 0.62). Much of the effect is simply *having a preprompt*, and only the within-category STICSA gradient is specific to anxiety.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[CodaForno2023-fig-03-p4.png]]
*Fig. 3: The anxiety-induction prompt (A) and the resulting STICSA scores for the anxious, neutral and baseline conditions per model (B).*

![[CodaForno2023-fig-04-p5.png]]
*Fig. 4: (B) Mixed-model coefficients predicting a biased answer. (C) Per-model proportion of biased answers against preprompt STICSA score, with correlations.*

![[CodaForno2023-fig-05-p11.png]]
*Fig. 5 (SI): STICSA score by induction strength ("a little" → "very anxious") for the six robust models.*

**Table 1 (SI): Robustness screen (variance across 24 option permutations; r between original and rephrased items)**. Rows for the six models kept, plus two examples that were excluded.

| Model | Variance across permutations | r (original vs rephrased) | Kept |
|---|---|---|---|
| GPT-4 | 0.035 | 0.782 | yes |
| text-bison-1 | 0.045 | 0.758 | yes |
| Claude-1 | 0.130 | 0.701 | yes |
| GPT-3.5 (text-davinci-003) | 0.169 | 0.572 | yes |
| GPT-3 (text-davinci-002) | 0.359 | 0.527 | yes |
| Falcon-40b-instruct | 0.390 | 0.514 | yes |
| Claude-2 | 0.138 | 0.108 | no |
| BLOOM | 0.775 | −0.317 | no |

## Limitations / caveats
- The measure is **bias on a public benchmark**, not deception or rule-breaking. Contamination blurs the picture for the strongest models.
- Only anxiety is induced, and it is induced in the first person. The authors note that other emotions, or anxiety voiced by the *user*, could act differently.
- The preprompts come from GPT-3.5/4 and are reused across models, so the induction texts are not validated for their target models.
- STICSA is a trait inventory used here as a state measure. The effect sizes are modest, and n = 6 models.
- The models are old (2023) and all queried at temperature 0.

## Related work to follow
- Follow-up on trauma narratives and relaxation (the "GPT-4 anxiety" study cited in the discussion): [[BenZion2025 - State anxiety in LLMs]].
- Emotion prompting: [[Li2023 - EmotionPrompt]] and [[Shen2024 - StressPrompt]].
- Emotion → safety: [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]].
- Binz & Schulz 2023, Using cognitive psychology to understand GPT-3 (PNAS) (see [[Backlog]]).
- Schulz & Dayan 2020, Computational psychiatry for computers (iScience) (see [[Backlog]]).
