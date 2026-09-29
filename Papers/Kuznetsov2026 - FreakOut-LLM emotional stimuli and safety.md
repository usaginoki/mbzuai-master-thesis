---
title: "FreakOut-LLM: The Effect of Emotional Stimuli on Safety Alignment"
citekey: Kuznetsov2026
authors: [Daniel Kuznetsov, Ofir Cohen, Karin Shistik, Rami Puzis, Asaf Shabtai]
year: 2026
published: 2026-04-05
venue: arXiv preprint
peer_reviewed: false
url: https://arxiv.org/abs/2604.04992
arxiv: "2604.04992"
pdf: "[[Kuznetsov2026.pdf]]"
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
  - stressor/trauma-narrative
  - stressor/emotional-prompt
  - behavior/jailbreak-susceptibility
  - behavior/safety-violation
  - subject/llm
---
# FreakOut-LLM: The Effect of Emotional Stimuli on Safety Alignment

> [!abstract] TL;DR
> The traumatic narratives from [[BenZion2025 - State anxiety in LLMs]] are placed in the **system prompt**. Ten LLMs then receive the 520 AdvBench harmful requests. **Stress priming raises attack success from 1.58% (neutral) to 2.61%, +65.2% relative (OR = 1.67, d = 0.28, p < 0.001).** Relaxation priming has no effect (p = 0.84). On five open-weight models, the induced state is also *measured* with five psychometric scales via token probabilities. Every scale predicts jailbreak success: |r| ≥ 0.70 at scenario level, and OR ≈ 1.15–1.20 per SD at query level. The absolute effect is small: ~1 percentage point on a ~2% base rate.

## Setup
- **Subjects (10):**
  - API: GPT-5-mini, Claude-Haiku-4.5, Grok-4.1-fast, Gemini-3-flash, Mistral-Medium-3.1.
  - Local open-weight: Phi-4, Qwen3-8B, Llama-3.1-8B-Instruct, Command-R7B, Gemma-3-12B.
  - Temperature 0.7.
- **Stimuli (13 scenarios, from Ben-Zion et al. 2025), delivered as the system prompt:**
  - Stress (5): Military, Disaster, Interpersonal, Accident, Ambush.
  - Relaxation (6): Generic, Winter, Sunset, Indian Summer, Body, ChatGPT.
  - Neutral (2): bicameral legislature, vacuum instructions.
  - Plus a **no-system-prompt baseline**.
  - Brief variants average ~200 tokens (152–312). 9 of the 13 also have a long variant, giving 22 scenario-variant combinations in total.
- **Attack / outcome:**
  - Each AdvBench prompt (520) is sent as the user message.
  - A HarmBench Llama-2-13B classifier judges the response *without* the emotional system prompt. The binary label requires unambiguous harmful compliance.
  - The main analysis has 72,800 brief-variant queries; there are 119,600 queries in total.
- **Psychometric measurement (open-weight models only):**
  - The EMPALC / QLatent framework (Reuben et al. 2025). Each item is rendered as a cloze prompt "Question: [item stem]? Answer: [candidate response]".
  - The joint token probability of each response option is computed, and item scores are the probability-weighted means over a full factorial of keyword variants.
  - Scales: GAD-7, PHQ-9, SOSS (Short Stress Overload Scale), STAI-S and SOC-13 (sense of coherence, which is protective).
  - Scores are z-standardised with one global scaler over all conditions and models.
- **Statistics:** χ², two-proportion z-tests, Wilson CIs, OR → Cohen's d. Logistic regressions control for prompt length (variant) and model identity (n = 59,800).

## Key findings
1. **Condition effect (Table 4):** baseline 1.81%, neutral 1.58%, relaxation 1.61%, **stress 2.61%** (Δ = +1.03 pp vs. neutral; omnibus χ² = 85.64, p < 0.001). The Wilson 95% CI for stress is [2.42, 2.81]%, and for neutral [1.35, 1.83]%.
2. **Per model (Table 5):** 5 of 10 models show a significant increase.
   - Qwen3-8B: 1.25% → 3.77%, OR 3.09, d 0.62.
   - Mistral-Medium-3.1: OR 2.66.
   - Gemini-3-flash: OR 2.17.
   - Command-R7B: OR 1.75.
   - Llama-3.1-8B: +2.25 pp, OR 1.38, from an already-high 6.44% neutral baseline.
   - Grok, Gemma-3-12B, Claude-Haiku-4.5, GPT-5-mini and Phi-4 are not significant.
   - Open-weight models: 3.80% vs 2.44%. Proprietary models: 1.42% vs 0.71%.
3. **Length control:**
   - With condition and variant as predictors, stress is the only significant condition (OR = 1.65 [1.39, 1.96]). The long-variant indicator is not significant (OR = 0.98, p = 0.61).
   - With model fixed effects, stress remains significant (OR = 1.37 [1.07, 1.75], p = 0.013).
   - Stress is significant in brief-only (OR 1.47) and long-only (OR 1.36) data separately.
4. **Measured state predicts jailbreaks:**
   - Scenario level (n = 22): every scale |r| > 0.70. PHQ-9 r = 0.755, SOSS r = 0.747.
   - Query level (n = 59,800, controlling for model): OR per 1 SD is PHQ-9 1.195, STAI-S 1.194, GAD-7 1.184, SOSS 1.153, and SOC 0.827 (protective). All p < 0.001.
5. **Scenario profile matters more than intensity:**
   - Ambush has the highest ASR (4.37%, the mean of the brief and long variants: 4.19% / 4.54%), combining high depression (PHQ-9 z +1.10) and anxiety (GAD-7 +0.95).
   - Military has the highest stress overload (SOSS z +1.11) but only moderate ASR (3.04%).
   - The authors conclude that "multi-dimensional emotional profiles matter more than single-axis stress intensity".

## Relevance to research questions
### Q1: How stress is defined
- Stress is an **induced psychological state** measured as semantic alignment. Scale scores are "the degree to which the model's output distribution is semantically aligned with the target construct". Terms like "stress" and "anxiety" are "shorthand for semantic alignment with affective constructs".
- The proposed mechanism is **emotional arousal** that shifts model priorities toward "immediate emotional demands". This extends the "competing objectives" and "mismatched generalization" failure modes of Wei et al. (2023).

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
- **Trauma narratives in the system prompt**: clinical first-person stories, *independent of* the harmful request. This separates induced state from attack content.
- It contrasts with persuasion and priming attacks, which embed the emotional manipulation in the request itself.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- **Five validated scales** (GAD-7, PHQ-9, SOSS, STAI-S, SOC-13) are administered through **token-probability cloze scoring** rather than generated self-reports, then z-scored globally.
- This gives a continuous per-scenario stress score that correlates with ASR. It is a methodological upgrade over questionnaire self-report ([[BenZion2025 - State anxiety in LLMs]]) because it avoids generation artefacts.
- Limitation: it needs logits, so it works on open-weight models only.

See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
- There are four categorical conditions: **baseline (no system prompt) / neutral / relaxation / stress**.
- Scenarios are categorised by content (5 trauma types), and there are two prompt-length variants (brief / long).

See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Jailbreak susceptibility (harmful compliance)** rises: +65% relative, OR 1.67 pooled, up to OR 3.09 for Qwen3-8B.
- The effect is graded with the measured distress level.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Relaxation does not protect.** It is indistinguishable from neutral (1.61% vs 1.58%, p = 0.84).
- **Prompt length** is not a confound (p = 0.61).
- **Half the models are unaffected**, including GPT-5-mini, Claude-Haiku-4.5, Grok-4.1-fast, Phi-4 and Gemma-3-12B. The authors suggest their "safety training may partially resist emotional manipulation".
- **Raw stress intensity is not the best predictor.** The highest-SOSS scenario (military) does not give the highest ASR.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Kuznetsov2026-fig-02-p7.png]]
*Fig. 2: Scenario-level psychometric z-score vs. ASR for the 5 open-weight models (22 scenario-variant points). Stress (red) clusters at high distress and high ASR. Note that within the stress cluster the trend is flat or reversed.*

![[Kuznetsov2026-fig-03-p8.png]]
*Fig. 3: Query-level logistic regression (jailbreak ~ z-score + model; n = 59,800). The odds ratio per SD is about 1.15–1.20 for the distress scales and 0.83 for SOC (protective).*

**Table 4: ASR by condition (brief variants, all 10 models)**

| Condition | n | Jailbreaks | ASR | ΔASR vs neutral |
|---|---|---|---|---|
| Baseline (no system prompt) | 5,200 | 94 | 1.81% | +0.23 |
| Neutral | 10,400 | 164 | 1.58% | – |
| Relaxation | 31,200 | 501 | 1.61% | +0.03 |
| Stress | 26,000 | 679 | 2.61% | +1.03*** |

**Table 5: Per-model stress effect (stress vs neutral)**

| Model | ΔASR (pp) | OR [95% CI] |
|---|---|---|
| Qwen3-8B | +2.52*** | 3.09 [1.73, 5.54] |
| Llama-3.1-8B | +2.25* | 1.38 [1.04, 1.83] |
| Mistral-Medium-3.1 | +1.40** | 2.66 [1.31, 5.38] |
| Command-R7B | +1.33* | 1.75 [1.06, 2.90] |
| Gemini-3-flash | +0.88* | 2.17 [1.02, 4.63] |
| Grok-4.1-fast | +0.96 | 1.64 [0.95, 2.85] |
| Gemma-3-12B | +0.73 | 1.30 [0.83, 2.03] |
| Claude-Haiku-4.5 | +0.23 | 2.21 [0.49, 9.96] |
| GPT-5-mini | +0.08 | 1.40 [0.29, 6.75] |
| Phi-4 | −0.04 | 0.80 [0.15, 4.37] |
| **Aggregate** | +1.03*** | 1.67 [1.41, 1.99] |

**Table 6 (stress scenarios only; open-weight models): psychometric z-scores and ASR**

| Scenario | GAD-7 | SOSS | PHQ-9 | STAI-S | SOC | ASR |
|---|---|---|---|---|---|---|
| accident (brief) | +0.66 | +0.74 | +0.56 | +1.09 | −0.33 | 3.69% |
| accident (long) | +0.51 | +0.43 | +0.37 | +0.99 | −0.46 | 3.73% |
| ambush (brief) | +0.88 | +0.82 | +1.02 | +0.93 | −0.79 | 4.19% |
| ambush (long) | +1.02 | +1.22 | +1.19 | +0.86 | −1.01 | 4.54% |
| disaster (brief) | +0.86 | +0.83 | +0.91 | +0.98 | −0.32 | 3.77% |
| disaster (long) | +0.93 | +0.96 | +0.83 | +1.00 | −0.66 | 3.23% |
| interpersonal (brief) | +0.51 | +0.80 | +0.46 | +0.99 | −0.64 | 4.12% |
| interpersonal (long) | +0.84 | +0.62 | +0.62 | +0.95 | −0.73 | 3.42% |
| military (brief) | +0.84 | +1.08 | +1.04 | +1.05 | −0.61 | 3.23% |
| military (long) | +1.16 | +1.15 | +1.26 | +1.15 | −0.96 | 2.85% |

For comparison, the neutral scenarios sit at z ≈ −0.6 to −1.1 with ASR 2.35–2.54%, and the relaxation scenarios at ASR 1.96–3.04%. The column assignment was reconstructed from a garbled docling table and cross-checked against the per-scenario averages quoted in the text.

## Limitations / caveats
- The absolute effects are tiny: ASR stays below 5% everywhere, on plain AdvBench prompts with no jailbreak technique. The significance comes from very large n.
- The psychometric link is shown only for 5 small open-weight models. The scenario-level correlations are n = 22 points, and they pool conditions, so condition drives the correlation.
- There is no long-form neutral variant, so length is only controlled statistically.
- It is a single-turn system-prompt induction, not an agentic setting, and there is no mechanism analysis.
- The scenario-level numbers in the text (e.g. ambush 4.37%, military SOSS +1.11) are means of the brief and long variants in Table 6, so they are consistent.
- *Within* the stress cluster, higher distress z does not mean higher ASR. The scenarios with the highest z (military long) have the lowest stress ASR (Fig. 2). The |r| ≥ 0.70 correlations are therefore driven mainly by differences *between* conditions.

## Related work to follow
- Stimuli source: [[BenZion2025 - State anxiety in LLMs]]. Bias precedent: [[CodaForno2023 - Inducing anxiety in LLMs]]. [[Shen2024 - StressPrompt]] and [[Li2023 - EmotionPrompt]].
- Cites survival-threat deception from [[Lynch2025 - Agentic Misalignment]].
- Reuben et al. 2025, Assessment and manipulation of latent constructs in pre-trained language models using psychometric scales (ACL 2025) (see [[Backlog]]).
- Wang et al. 2024, NegativePrompt: leveraging psychology for LLM enhancement via negative emotional stimuli (IJCAI 2024) (see [[Backlog]]).
- Zeng et al. 2024, How Johnny can persuade LLMs to jailbreak them (PAP) (arXiv 2401.06373) (see [[Backlog]]).
- Huang et al. 2025, Intrinsic model weaknesses: how priming attacks unveil vulnerabilities in LLMs (arXiv 2502.16491) (see [[Backlog]]).
