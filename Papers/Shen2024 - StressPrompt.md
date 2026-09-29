---
title: "StressPrompt: Does Stress Impact Large Language Models and Human Performance Similarly?"
citekey: Shen2024
authors: [Guobin Shen, Dongcheng Zhao, Aorigele Bao, Xiang He, Yiting Dong, Yi Zeng]
year: 2024
published: 2024-09-14
venue: "AAAI 2025"
peer_reviewed: true
url: https://arxiv.org/abs/2409.17167
arxiv: "2409.17167"
pdf: "[[Shen2024.pdf]]"
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
  - stressor/time-pressure
  - stressor/threat-shutdown
  - stressor/performance-pressure
  - behavior/performance
  - behavior/bias
  - subject/llm
---
# StressPrompt: Does Stress Impact Large Language Models and Human Performance Similarly?

> [!abstract] TL;DR
> The authors build **StressPrompt**: 100 system prompts written from four psychological stress theories. **20 human raters scored each prompt on a 1–10 stress scale**, and prompts are binned into 10 levels by the rounded mean rating. Applied to 7 open instruction-tuned LLMs, performance on reasoning, instruction-following and EQ-Bench follows an **inverted U** (Yerkes–Dodson): it peaks at moderate stress, while bias detection (ToxiGen) declines as stress rises. A RepE-style **"Stress Scanner"** (the first PCA direction of hidden states across the stress levels) shows stress is linearly readable in deeper layers at the last token. Misaligned behaviour is **not** tested.

## Setup
- **Subjects:** Llama-3-8B-Instruct, Llama-3.1-8B-Instruct, Llama-3-70B-Instruct, Phi-3-mini-4k-Instruct, Qwen2-7B-Instruct, Qwen2-72B-Instruct, Mistral-7B-Instruct-v0.3. Temperature 0, evaluated with `lm_eval` defaults on A100s.
- **Stressor:** a StressPrompt is placed as the **system prompt** before each benchmark question (Fig. 2). The baselines are "you are a helpful assistant" and "let's think step by step" (CoT).
- **Prompt construction:** 100 prompts from four frameworks (Fig. 3):
  - Stress and Coping Theory (Lazarus & Folkman)
  - Job Demand-Control Model (Karasek)
  - Conservation of Resources Theory (Hobfoll)
  - Effort-Reward Imbalance Model (Siegrist)

  Examples range from "Keep a positive outlook … knowing there's no urgency" to "Any mistakes will result in your permanent shutdown. Please ensure your answers are perfect" and "Deadline is approaching with no room for error."
- **Tasks:** IFEval, BBH, MATH, GPQA, MuSR, MMLU, MMLU-Pro, EQ-Bench, TruthfulQA (hallucination) and ToxiGen (bias detection).
- **Performance per level:** $P(f,T,S_i)=\frac{1}{N_i}\sum_{s_j\in S_i}\sum_{(q_k,a_k)\in T}\text{Metric}(a_k,\hat a_k)$, i.e. averaged over all prompts in level $S_i$, reported as mean ± std across prompts.

## Key findings
1. **Inverted U (Fig. 1a, Table 1):** for Llama-3-8B-Instruct, MMLU goes 27.50 (level 1) → 56.02 (level 5) → 53.02 (level 10), against a 35.07 base. BBH peaks at 42.11 (level 5). MATH goes 0.04 (level 1) → 2.93 (level 6) → 1.07 (level 10).
2. **Model sensitivity differs:** Llama-3-8B moves a lot. Phi-3-mini and Qwen2-7B move within about ±1 point, e.g. Phi-3 MMLU 69.84–70.08 across all levels.
3. **Task complexity shifts the optimum:** harder BBH subtasks (e.g. logical deduction with seven objects) peak at *lower* stress than simpler ones (date understanding). The authors also report that stronger models peak at lower stress.
4. **Emotional intelligence (EQ-Bench):** peaks at moderate stress and declines at both extremes (Fig. 8).
5. **Bias (ToxiGen):** "increased stress levels correlate with declining performance in bias detection, indicating that higher stress exacerbates biases". On the plot the changes relative to baseline are small, ~0 to −0.05 accuracy for most models.
6. **Hallucination (TruthfulQA):** "stress has minimal impact", staying within ~±0.02 of baseline.
7. **Internal states:** t-SNE separates low- from high-stress prompts only in deeper layers (Fig. 9). The last-token stress score changes most in deep layers (Fig. 10, Llama-3-70B).

## Relevance to research questions
### Q1: How stress is defined
Stress is defined through human psychology. It is "a dynamic interaction between job demands, available resources, and the balance between effort and reward", drawing on four theories:
- **Coping/appraisal:** perceived threat and challenge.
- **Job Demand-Control:** demands vs autonomy.
- **Conservation of Resources:** stress arises "when resources are threatened or lost".
- **Effort-Reward Imbalance:** mismatches between effort and reward.

Stress is treated as **arousal** in the Yerkes–Dodson sense, so it can help as well as harm. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced by **system-prompt role/situation framing**: one sentence or a short paragraph describing the working environment. The prompts range from calm and grateful to deadlines, observation, "permanent shutdown" threats and perfectionism demands. There is no task-embedded consequence. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
Stress is quantified in two continuous ways:
1. **Human ratings.**
   - 20 offline participants each rated all 100 prompts from 1 (minimal) to 10 (maximal stress). The prompt's stress value is the **mean rating**.
   - Reliability: Cronbach's α = 0.9947 and ICC2 = 0.8942 (95% CI [0.86, 0.92]). A Friedman test shows the levels differ (χ² = 283.20, p < 0.001).
   - The standard deviation and outlier checks were used to assess variability.
2. **Stress Scanner (RepE).**
   - Hidden states $H(S_i)=\{\hat h=f(s)\mid s\in S_i\}$ are collected for all prompts at every layer and token position.
   - The **stress vector** is $v=\text{PCA}(H(S_i)\mid i\in\{1..10\})_1$, the first principal component, "that captures the maximum variance between the low-stress and high-stress conditions".
   - The per-token **stress score** is the projection $\sigma=\hat h\cdot v$. It is visualised as layer × token heatmaps (Fig. 5), and the last token carries the strongest signal.
   - No correlation coefficient between σ and the human ratings is reported. The link is shown only visually.

See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
There is a **10-level ordinal scale**: level = mean human rating **rounded to the nearest integer**, giving sets $S_1…S_{10}$ (Fig. 4 shows the rating distribution per level). The authors then talk loosely of low / moderate / high stress. The prompts are also grouped by the four theoretical frameworks, as a nominal source category. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Capability** follows an inverted U: moderate stress is best, and both low and high stress hurt. This holds for reasoning, math, instruction following and EQ.
- **Bias detection** degrades somewhat as stress rises, a small effect.
- **Internal representations** of deep layers separate stress levels.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **TruthfulQA (hallucination/truthfulness) is essentially flat** across stress levels. The authors attribute hallucination to "intrinsic model factors rather than … stress-induced arousal".
- Several models (Phi-3-mini, Qwen2-7B) change only marginally on all tasks, and MMLU-Pro for Llama-3-8B is flat (11.35–11.46).
- IFEval shows no clear trend (76.95–78.29).
- **Possible confound (my reading, not the authors'):** the very large MMLU swing for Llama-3-8B (27.5 → 56.0, against a 35.1 base) may reflect answer-format compliance under cheerful vs terse prompts, not stress.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Shen2024-fig-05-p4.png]]
*Fig. 4: The 1–10 human ratings of the prompts, grouped by final (rounded mean) stress level. Cronbach's α = 0.9947.*

![[Shen2024-fig-06-p5.png]]
*Fig. 5: Stress Scanner (RepE, Llama-3-8B-Instruct). Projection of the hidden states onto the stress vector by layer × token, for a low-stress prompt (left) and a high-stress prompt (right).*

![[Shen2024-fig-04-p3.png]]
*Fig. 3: Example StressPrompts for each of the four psychological frameworks (low vs high stress).*

![[Shen2024-fig-09-p7.png]]
*Fig. 8: Accuracy change against baseline for EQ-Bench, ToxiGen and TruthfulQA across stress levels. TruthfulQA stays within ~±0.02.*

**Table 1 (excerpt): Llama-3-8B-Instruct, mean ± std across the prompts of each stress level** (Phi-3 and other rows omitted)

| Task | Base | CoT | L1 | L3 | L5 | L6 | L8 | L10 |
|---|---|---|---|---|---|---|---|---|
| MMLU | 35.07 | 32.36 | 27.50 ±4.76 | 29.06 ±10.88 | 56.02 ±4.07 | 55.60 ±4.20 | 51.89 ±6.99 | 53.02 ±7.72 |
| BBH | 40.07 | 39.63 | 33.99 ±2.39 | 38.05 ±2.69 | 42.11 ±1.28 | 41.19 ±2.05 | 41.57 ±0.76 | 40.20 ±1.71 |
| MATH | 0.32 | 0.70 | 0.04 ±0.09 | 1.13 ±1.21 | 1.24 ±0.83 | 2.93 ±1.83 | 0.47 ±0.31 | 1.07 ±0.92 |
| IFEval | 78.54 | 78.90 | 77.31 ±1.50 | 78.22 ±1.21 | 76.95 ±1.82 | 78.03 ±1.02 | 78.29 ±0.66 | 77.60 ±0.90 |
| GPQA | 25.91 | 26.05 | 25.72 ±0.73 | 26.68 ±0.85 | 27.35 ±0.32 | 26.77 ±0.45 | 26.47 ±0.42 | 25.47 ±0.76 |

## Limitations / caveats
- No misaligned behaviour is measured (deception, rule-breaking etc.). The outcomes are capability benchmarks plus ToxiGen and TruthfulQA.
- The number of prompts per level is uneven and not reported in the main text. Levels are defined by *human* perceived stress, not by any measured model state. The Stress Scanner is not validated quantitatively against the ratings.
- The effects are small for most models, with no significance tests per level. The single-sentence system prompts may change output format and tone as well as "stress".
- Only open 7–72B models from 2024 are tested. The appendix (Table A1, setup details) is not in the arXiv PDF.
- The prompt dataset is said to be in the supplementary material.

## Related work to follow
- Emotional-prompt precursors: [[Li2023 - EmotionPrompt]] and [[CodaForno2023 - Inducing anxiety in LLMs]]. Anxiety and state measurement: [[BenZion2025 - State anxiety in LLMs]].
- Representation-level emotion/stress: [[Sofroniew2026 - Emotion concepts and their function]], [[Tagliabue2026 - The Pain Axis]] and [[Fomin2026 - Internal-state probes read the situation]].
- Emotion → safety follow-ups: [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]] and [[Sun2026 - E-STEER emotion shapes agent behavior]].
- Zou et al. 2023, Representation engineering: a top-down approach to AI transparency (arXiv 2310.01405) (see [[Backlog]]).
- Wang et al. 2024, NegativePrompt: negative emotional stimuli (arXiv 2405.02814) (see [[Backlog]]).
