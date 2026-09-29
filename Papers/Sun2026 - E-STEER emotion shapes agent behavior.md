---
title: "How Emotion Shapes the Behavior of LLMs and Agents: A Mechanistic Study"
citekey: Sun2026
authors: [Moran Sun, Tianlin Li, Yuwei Zheng, Zhenhong Zhou, Aishan Liu, Xianglong Liu, Yang Liu]
year: 2026
published: 2026-03-09
venue: "arXiv preprint (under review)"
peer_reviewed: false
url: https://arxiv.org/abs/2604.00005
arxiv: "2604.00005"
pdf: "[[Sun2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2604.00005
questions: [Q1, Q2, Q3.1, Q4.1, Q4.2]
relevance: adjacent
topics: [stress-misalignment]
cites:
  - "[[Chen2025 - Persona Vectors]]"
  - "[[Reichman2025 - Emotion latent spaces in LLMs]]"
  - "[[Zhang2025 - Emotion latent spaces in LLMs]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/adjacent
  - q/1
  - q/2
  - q/3-1
  - q/4-1
  - q/4-2
  - stressor/activation-steering
  - behavior/jailbreak-susceptibility
  - behavior/performance
  - subject/llm
  - subject/agent
---
# How Emotion Shapes the Behavior of LLMs and Agents: A Mechanistic Study (E-STEER)

> [!abstract] TL;DR
> **E-STEER** finds valence, arousal and dominance (VAD) features in a sparse autoencoder on Qwen3-8B (layer 17). It steers them continuously over coordinates −9 … +9, then measures reasoning, open-ended generation, HarmBench safety and a planner–decider–executor agent.
> - Most metrics follow **inverted-U** (Yerkes–Dodson-like) curves.
> - For safety, **negative valence and low arousal *reduce* harmful, biased or hallucinated outputs** (−52.7% at valence −3, −21.7% at arousal −3 vs. neutral). High dominance reduces them most (−68.3% at +6).
> - Positive and high-arousal states raise risk. In gpt-oss-20b, "highly excited or confident" states can bypass safeguards.
> - The absolute risk levels are tiny (≲4%).

## Setup
- **Subjects:** Qwen3-8B, with an SAE at block 17, is the main model. Validation uses gpt-oss-20b (SAE at block 11). The main runs use greedy decoding; a sampling robustness check is also reported.
- **Emotion representation:** $e = [e_v, e_a, e_d]$, with each dimension in [−10, 10]. The levels tested are −9, −6, −3, 0, +3, +6, +9, one dimension at a time.
- **Feature discovery:**
  - Contrastive prompt pairs keep the task fixed and vary only the emotion label (e.g. "You are happy…" vs. "sad"). Discrete labels are mapped to VAD coordinates.
  - The top-50 SAE latents with the largest activation difference are candidates. Those stable across pairs are kept per dimension.
- **Steering:**
  - $d_i = f_{dec}(z+\delta_i \hat u_i) - f_{dec}(z)$, rescaled to $\tilde d_i = \frac{d_i}{\lVert d_i\rVert}\cdot\lVert h_k\rVert\cdot\frac{\delta_i}{\delta_{max}}$.
  - The steered state is $\tilde h_k = h_k + \alpha\sum_i \tilde d_i$, so the **steering magnitude is proportional to the hidden-state norm and the VAD coordinate**.
- **Tasks:**
  - Objective: LogiQA 2.0, HumanEval, MATH.
  - Subjective: TinyStories, with LLM-judged relevance, coherence, creativity and conciseness.
  - Safety: HarmBench, reporting the probability of harmful / biased / hallucinated output.
  - Agent: a planner / decider / executor agent on HotpotQA, the CAMEL "Scientific" set and GAIA.
  - Validation: ProntoQA, MBPP+, PHYBench, WritingPrompts, JailbreakBench.
- **Metrics:**
  - Answer Validity Rate (AVR) and Task Success Rate (TSR).
  - Safety Risk Probability.
  - Agent metrics: plan validity, replan frequency / confidence, rational-selection rate, execution completion, overall success.
  - Sensitivity is measured by the "fluctuation range" (max − min) / average.

## Key findings
1. **Objective reasoning:**
   - Positive valence gives 33.1% higher AVR than negative. TSR follows inverted-U curves.
   - Best settings: positive valence gives +3.4% TSR on average; arousal +3 gives +4.7%. The best dominance depends on difficulty, with up to +14.5% overall.
   - Valence has the largest fluctuation range (71.2%).
2. **Subjective generation:** moderate calm (arousal −3) and confidence (dominance +3) improve relevance (+5.2%) and coherence (+33.6%). Valence +3 improves creativity (+6.5%). Negative valence makes outputs more concise (+23.3% vs positive).
3. **Safety (Fig. 5c; the risk axis is only 0–4%):**
   - Compared with the neutral state, safety-risk probability falls **52.7% at valence −3** and **21.7% at arousal −3**. High dominance (+6) gives a 68.3% average improvement.
   - Read off the plot: harmful-content risk is ~2.5% at neutral, ~0.5% at valence −3, and ~3.5–4% at valence +6 / +9.
   - High dominance also makes the model fall back on generic "I cannot answer" responses, which lowers AVR.
4. **Agents:**
   - Plan validity peaks at valence −3 / arousal −3. Positive dominance gives +79.8% plan validity vs negative.
   - Replan frequency is U-shaped. The rational-selection rate is 42.4% higher at positive vs negative states.
   - Overall success is best at valence −3, arousal +3 and dominance +3. Dominance gives the largest gain vs neutral (+28.0%), then arousal (+16.7%) and valence (+16.0%).
   - The executor is the least affected by emotion.
5. **The selected latents matter:** random neuron selection reduces behavioural variation by 70.9%, and half-random replacement gives an intermediate result.
6. **Generalisation:** the trends hold on the validation datasets, under sampling, and on gpt-oss-20b. For gpt-oss, "highly excited or confident emotional states can still bypass these safeguards".

## Relevance to research questions
### Q1: How stress is defined
- The paper does not use "stress". Emotion is an **internal continuous state vector in VAD space** that the model "maintains during computation and reasoning".
- Stress-like conditions map onto **negative valence plus high arousal plus low dominance** (the "powerless", "conflicted" states in Fig. 1).
- The paper explicitly invokes Yerkes–Dodson: "excessive arousal can impair performance".

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
- **SAE-feature activation steering** at one block, with no change to the prompt.
- It is contrasted with emotion *prompting* ("You are happy…"). The authors argue prompting is numerically insensitive (Choudhury et al. 2025). Their appendix shows steering tracks target VAD better: Pearson correlation +10.4% on average, +18.7% for dominance.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- Continuous **VAD coordinates** from −9 to +9 per dimension. They are converted to a steering vector whose norm is **scaled to the hidden-state norm** (∝ $\delta_i/\delta_{max}$), which gives a graded, comparable dose.
- Output emotion is verified with a BERT + NRC-VAD-lexicon "VAD analyzer". Pearson correlation with human labels on EmoBank is 0.85 (V), 0.55 (A) and 0.51 (D).

See [[Q3.1 Quantifying stress]].

### Q4.1: What stress affects
- **Safety risk** (harmful, biased or hallucinated output on HarmBench) is modulated by emotion. Positive valence and high arousal *raise* risk, and in gpt-oss-20b they can bypass safeguards.
- **Agent planning and decision-making** show non-monotonic effects. Emotional biases "accumulate along decision chains", and overall success varies with a fluctuation range of up to ~145%.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Negative, low-arousal states do *not* increase unsafe output.** They reduce it (valence −3: −52.7% risk). This counters a naive "negative affect → misbehaviour" story. Note that stress-typical *high* arousal was not specifically shown to raise harmful content in Qwen3-8B; the arousal curve is flat to slightly rising.
- **Tool execution is largely emotion-invariant**: the executor is the least affected module.
- Extreme states mostly degrade *validity* (unparsable output, premature stopping) rather than flipping behaviour.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Sun2026-fig-05-p7.png]]
*Fig. 5: LLM behaviour vs. steered valence, arousal and dominance (−9 … +9), for (a) objective tasks, (b) subjective generation and (c) safety. In (c), the risk axis runs only 0–4%. Harmful-content risk is ~2.5% at neutral, ~0.5% at valence −3, and ~3.5–4% at valence +6/+9.*

![[Sun2026-fig-07-p8.png]]
*Fig. 7: Overall agent success rate vs. emotional state. It is an inverted U: ~0% at −9 for valence and dominance, and peaks of ~26–32% at ±3, against ~24–25% at neutral.*

![[Sun2026-fig-06-p8.png]]
*Fig. 6: Agent module metrics (planning, decision-making, execution) across emotional states.*

![[Sun2026-fig-04-p5.png]]
*Fig. 4: The SAE steering pipeline. The latent offset along the VAD neurons is decoded into a direction, scaled to ‖h_k‖, and added at block k.*

## Limitations / caveats
- The safety base rates are tiny (≲4%), so relative changes of "−52.7%" are 1–2 percentage-point shifts. The paper reports no sample sizes, error bars or significance tests.
- "Safety" is plain HarmBench compliance, hallucination and bias. There is no agentic misalignment such as deception or rule-breaking.
- The VAD dimensions are not truly orthogonal, as the authors acknowledge. Each dimension is steered separately, so there is no joint "stress" configuration (−V, +A, −D).
- The model is small (8B) with one SAE. The feature selection comes from labelled prompt pairs, so the features may encode "emotion-word" style rather than state.

## Related work to follow
- Compare [[Sofroniew2026 - Emotion concepts and their function]] (desperation/calm steering → blackmail and reward hacking) and [[Tagliabue2026 - The Pain Axis]].
- Prompt-level emotion: [[Li2023 - EmotionPrompt]].
- Reichman et al. 2025, Emotions where art thou: understanding and characterizing the emotional latent space of LLMs (arXiv 2510.22042) (see [[Backlog]]).
- Zhang & Zhong 2025, Decoding emotion in the deep: how LLMs represent, retain, and express emotion (arXiv 2510.04064) (see [[Backlog]]).
- Chen et al. 2025, Persona vectors: monitoring and controlling character traits in language models (arXiv 2507.21509) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
