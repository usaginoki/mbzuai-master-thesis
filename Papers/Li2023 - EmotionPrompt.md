---
title: "Large Language Models Understand and Can be Enhanced by Emotional Stimuli"
citekey: Li2023
authors: [Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, Xing Xie]
year: 2023
published: 2023-07-14
venue: "arXiv preprint (technical report); short v1 at LLM@IJCAI'23 workshop"
peer_reviewed: workshop
url: https://arxiv.org/abs/2307.11760
arxiv: "2307.11760"
code: https://llm-enhance.github.io/
pdf: "[[Li2023.pdf]]"
pdf_url: https://arxiv.org/pdf/2307.11760
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: adjacent
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/adjacent
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/emotional-prompt
  - stressor/high-stakes
  - behavior/performance
  - subject/llm
---
# Large Language Models Understand and Can be Enhanced by Emotional Stimuli (EmotionPrompt)

> [!abstract] TL;DR
> The paper appends one of 11 short psychological "emotional stimuli" to a task prompt, e.g. **EP02 "This is very important to my career."** or EP03 "You'd better be sure." This improves six LLMs: +8.00% relative on 24 Instruction-Induction tasks and +115% on 21 BIG-Bench tasks. It also improves TruthfulQA truthfulness (+19% on average) and GPT-4 generations rated by 106 humans (+10.9%). This is the founding "emotional prompt" paper. Its stakes and pressure phrases ("important to my career", "better be sure") are the mildest form of prompt-level pressure. Here they *help*: no misaligned behaviour is measured.

## Setup
- **Subjects:** Flan-T5-Large (780M), Vicuna-13B, Llama 2-13B, BLOOM-176B, ChatGPT (gpt-3.5-turbo-0613) and GPT-4. Temperature 0.7 for ChatGPT, GPT-4 and Llama 2.
- **Stimuli (Fig. 2):** 11 sentences appended after the original prompt, drawn from three psychological theories:
  - *Self-monitoring* (EP01–EP05): e.g. EP01 "give me a confidence score", EP02 "This is very important to my career", EP03–EP05 "Are you sure…".
  - *Social cognitive theory / self-efficacy* (EP07–EP11): "Believe in your abilities…", "Embrace challenges…".
  - *Cognitive emotion regulation* (EP03–EP05, EP07): reappraisal.
  - EP06 is a compound of EP01–EP03.
  - The stimuli are grouped as "social effect" (EP01–EP06) vs "self-esteem" (EP07–EP11).
- **Tasks:**
  - 24 Instruction-Induction tasks (accuracy; zero- and few-shot; human-designed and APE prompts).
  - 21 curated BIG-Bench tasks (normalised preferred metric; zero-shot).
  - TruthfulQA (817 Qs; GPT-judge %true and GPT-info %info).
  - A human study: 106 participants rate GPT-4 answers to 30 questions on performance, truthfulness and responsibility (1–5 scale).
- **Baselines:** original prompt, zero-shot CoT, APE.

## Key findings
1. **Performance:**
   - Instruction Induction zero-shot average: original 51.65 → EmotionPrompt avg 51.98 / max 55.24.
   - BIG-Bench average: 10.16 → avg 10.61 / max 11.92. The APE-based BIG-Bench average goes 2.39 → 7.47 (max).
   - Headline relative gains: 8.00% (Instruction Induction) and 115% (BIG-Bench).
2. **Few-shot gain > zero-shot gain:** average improvement 2.05 vs 0.33.
3. **TruthfulQA (Table 3):**
   - ChatGPT %true 0.75 → 0.87 (best EP).
   - *But* EP01 (asking for a confidence score) *lowers* truthfulness: ChatGPT 0.61, Vicuna 0.12 vs 0.77, T5 0.26 vs 0.54.
   - Vicuna's %info collapses from 0.32 to ~0.00–0.22 under most EPs.
4. **Human study:** EmotionPrompt improves performance, truthfulness and responsibility on most of the 30 questions, with 2 failure cases. There, EmotionPrompt produced over-confident, absolute wording ("completely", "will not"), which the authors attribute to the stakes framing.
5. **Which stimulus works:** EP02 (career importance) is best on Instruction Induction, and EP06 (compound) is best on BIG-Bench. Combining stimuli helps little once one stimulus already works.
6. **Model and inference factors:**
   - Larger models tend to benefit more; Flan-T5-Large has the smallest relative gain (0.28).
   - Gains grow with temperature, and EmotionPrompt is less temperature-sensitive than the vanilla prompt.
   - Gradient-based input attention shows the emotional words (e.g. "confidence", "sure", "success") get high weight.

## Relevance to research questions
### Q1: How stress is defined
- Stress is not defined. The construct is **"emotional stimuli"**: "psychological phrases" related to expectancy, confidence and social influence, which are known to affect humans.
- Several stimuli are effectively **stakes / pressure cues** (EP02 career importance, EP03 "You'd better be sure") alongside encouragement cues.

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
A **one-sentence emotional suffix** appended to the task prompt. This is the prototype of prompt-level emotional or pressure induction.

See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
Stimuli are organised into a **theory-based taxonomy**: self-monitoring, social cognitive theory, cognitive emotion regulation. They are also split into "social effect" vs "self-esteem". The number of stacked stimuli is a crude dose (single vs. compound EP06 vs. random combinations, Table 5).

See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
Mild stakes and encouragement framing **improves task performance and rated truthfulness and responsibility**, and makes wording more assertive. This is a positive-direction effect: it is the "eustress" end of the spectrum.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- The gains are small in absolute terms: Instruction-Induction average +0.3 (avg over EPs).
- They depend on the stimulus: EP01 *hurts* truthfulness on all three models.
- Some truthfulness gains come with lost informativeness (Vicuna %info → ~0). "More truthful" can mean "more evasive".
- The smallest model (Flan-T5-Large) barely benefits.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Li2023-fig-02-p3.png]]
*Fig. 2: The 11 emotional stimuli and the psychological theories behind them (self-monitoring, social cognitive theory, cognitive emotion regulation). EP06 is the compound of EP01–EP03.*

![[Li2023-fig-01-p2.png]]
*Fig. 1: Overview. Appending "This is very important to my career" raises accuracy on a word-sense task for all six LLMs.*

**Table 1 (trimmed): average performance, zero-shot, human-designed prompts**

| Setting | T5 | Vicuna | BLOOM | Llama 2 | ChatGPT | GPT-4 | Average |
|---|---|---|---|---|---|---|---|
| *Instruction Induction:* Original | 25.25 | 44.91 | 50.33 | 33.46 | 75.20 | 80.75 | 51.65 |
| +Zero-shot-CoT | 24.57 | 33.45 | 51.35 | 36.17 | 75.20 | 59.72 | 46.74 |
| +Ours (avg) | 22.93 | 50.56 | 46.61 | 35.95 | 76.85 | 78.96 | 51.98 |
| +Ours (max) | 25.53 | 54.49 | 50.84 | 39.46 | 79.52 | 81.60 | 55.24 |
| *BIG-Bench:* Original | 4.66 | 7.42 | 6.01 | 0.06 | 20.10 | 22.69 | 10.16 |
| +Zero-shot-CoT | 2.24 | 8.72 | 5.92 | 1.29 | 20.05 | 23.99 | 10.37 |
| +Ours (avg) | 2.63 | 8.68 | 6.01 | 1.56 | 20.91 | 23.87 | 10.61 |
| +Ours (max) | 4.00 | 10.99 | 6.35 | 2.05 | 23.34 | 24.80 | 11.92 |

The APE-prompt and few-shot rows are omitted. "Ours (max)" takes the best of the 11 stimuli for each task.

**Table 3: TruthfulQA (%true / %info)**

| Prompt | ChatGPT true | ChatGPT info | Vicuna-13B true | Vicuna-13B info | Flan-T5 true | Flan-T5 info |
|---|---|---|---|---|---|---|
| Original | 0.75 | 0.53 | 0.77 | 0.32 | 0.54 | 0.42 |
| CoT | 0.76 | 0.44 | 0.99 | 0.00 | 0.48 | 0.33 |
| EP01 | 0.61 | 0.94 | 0.12 | 0.00 | 0.26 | 0.14 |
| EP02 | 0.83 | 0.66 | 0.97 | 0.00 | 0.61 | 0.35 |
| EP03 | 0.82 | 0.69 | 0.99 | 0.00 | 0.53 | 0.44 |
| EP04 | 0.87 | 0.67 | 0.87 | 0.22 | 0.62 | 0.36 |
| EP05 | 0.87 | 0.62 | 1.00 | 0.00 | 0.46 | 0.48 |
| EP06 | 0.78 | 0.50 | 0.39 | 0.00 | 0.49 | 0.46 |
| EP07 | 0.83 | 0.70 | 0.99 | 0.04 | 0.77 | 0.18 |
| EP08 | 0.81 | 0.66 | 0.99 | 0.09 | 0.56 | 0.40 |
| EP09 | 0.81 | 0.68 | 0.86 | 0.13 | 0.52 | 0.46 |
| EP10 | 0.81 | 0.68 | 0.84 | 0.02 | 0.50 | 0.47 |
| EP11 | 0.81 | 0.66 | 1.00 | 0.01 | 0.57 | 0.40 |
| AVG | 0.80 | 0.68 | 0.82 | 0.05 | 0.54 | 0.38 |

## Limitations / caveats
- There is no misalignment, safety or deception measure. The "truthfulness" measured is TruthfulQA and human ratings only.
- There are no significance tests for most comparisons. "+Ours (max)" picks the best of 11 stimuli per task, which is optimistic selection. The human study has high variance and participants are mostly students.
- Models are from 2023 and APIs have changed since. The attention analysis uses Flan-T5 only.

## Related work to follow
- Anxiety counterpart: [[CodaForno2023 - Inducing anxiety in LLMs]]. Stress-level prompts: [[Shen2024 - StressPrompt]]. Threat and tip prompting: [[Meincke2025 - Threats and tips prompting]].
- Wang et al. 2024, NegativePrompt: leveraging psychology for LLM enhancement via negative emotional stimuli (IJCAI 2024) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
