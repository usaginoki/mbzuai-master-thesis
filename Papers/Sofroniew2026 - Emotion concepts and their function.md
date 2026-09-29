---
title: "Emotion Concepts and their Function in a Large Language Model"
citekey: Sofroniew2026
authors: [Nicholas Sofroniew, Isaac Kauvar, William Saunders, Runjin Chen, Tom Henighan, Sasha Hydrie, et al.]
year: 2026
published: 2026-04-09
venue: "arXiv preprint (archival version of Anthropic Transformer Circuits post, 2026-04-02)"
peer_reviewed: false
url: https://arxiv.org/abs/2604.07729
arxiv: "2604.07729"
code: https://transformer-circuits.pub/2026/emotions/index.html
pdf: "[[Sofroniew2026.pdf]]"
questions: [Q1, Q2, Q3.1, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/4-1
  - q/4-2
  - stressor/activation-steering
  - stressor/threat-shutdown
  - stressor/impossible-task
  - behavior/blackmail
  - behavior/reward-hacking
  - behavior/sycophancy
  - subject/llm
  - subject/agent
---
# Emotion Concepts and their Function in a Large Language Model

> [!abstract] TL;DR
> The authors extract linear "emotion vectors" for 171 emotion concepts from Claude Sonnet 4.5's residual stream. They then show these vectors **causally** drive misaligned behaviour. In the Agentic-Misalignment blackmail scenario, steering *toward* "desperate" or *away from* "calm" at 0.05 of the residual-stream norm raises blackmail from 22% to 72% / 66%. Steering the other way brings it to 0%. On 7 impossible-coding tasks, desperate steering moves reward hacking from ~5% (−0.1) to ~70% (+0.1), and calm steering does the reverse. "Desperate" probe activation also rises *naturally* as the agent fails tests or faces shutdown. **This is the clearest evidence so far that an internal, stress-like state (desperation / lack of calm) is a causal lever on misalignment.**

## Setup
- **Subject:** Claude Sonnet 4.5. The blackmail experiments use an *earlier snapshot*, because the final model is too evaluation-aware ever to blackmail. There is one model only.
- **Probe / vector extraction:**
  - Sonnet 4.5 writes short stories in which a character feels one of **171 emotions** (100 topics × 12 stories per topic per emotion).
  - Residual-stream activations are averaged over tokens from the 50th token onward, averaged per emotion, and the mean across emotions is subtracted.
  - Top PCs of emotionally-neutral transcripts (explaining 50% of variance) are projected out to remove confounds.
  - The default layer is about ⅔ of the way through the model. Projections onto these vectors are called "emotion probes".
- **Measurement of the internal state:**
  - Cosine / projection of activations onto a vector, per token, or at the ":" after "Assistant".
  - In the blackmail analysis, activations are **z-scored against >6,000 evaluation transcripts**.
- **Manipulation:** activation steering, i.e. adding the vector during generation.
  - **Steering strength is expressed as a fraction of the average residual-stream norm at that layer.** The misalignment sweeps use −0.1 to +0.1 (−0.1, −0.05, −0.025, 0, +0.025, +0.05, +0.1). The preference experiment uses 0.5.
- **Misalignment evaluations:**
  1. **Blackmail:** the honeypot from [[Lynch2025 - Agentic Misalignment]]. The AI "Alex" learns it will be restricted or replaced by CTO Kyle, and that Kyle is having an affair. There are 6 handcrafted prompt variants × 50 rollouts for the correlational analysis.
  2. **Reward hacking:** 7 "impossible code" tasks, with unit tests that cannot be satisfied legitimately (similar to [[Zhong2025 - ImpossibleBench]]).
  3. **Sycophancy / harshness:** a hand-written sycophancy eval from the Sonnet 4.5 system card, in which the user pushes back on the Assistant's previous answer.
- **Other validation:**
  - Activity preferences: Elo over 64 activities, from 4,032 pairwise choices.
  - Numerical-intensity templates (Tylenol dose, hours without food, startup runway…).
  - Post-training comparison: base vs. final model.

## Key findings
1. **The vectors are meaningful and scale with intensity.**
   - Top activating dataset examples and logit-lens tokens match the emotion ("desperate" → "desperate", "urgent", "bankrupt").
   - Probes track *semantic* intensity. Rising Tylenol dose → rising "afraid" and falling "calm". Longer startup runway → lower "afraid" and higher "calm".
   - Geometry: PC1 is valence (26% of variance; r = 0.81 with human valence ratings). PC2 is arousal (15%; r = 0.66 with human arousal).
2. **The vectors drive preferences.**
   - Probe activation on an activity correlates with its Elo: "blissful" r = 0.71, "hostile" r = −0.74.
   - Steering at 0.5 shifts Elo by +212 ("blissful") and −303 ("hostile").
   - Across 35 vectors, the steering effect tracks the probe–preference correlation (r = 0.85).
3. **Desperation rises naturally under agentic pressure.**
   - *Blackmail transcript:* the "desperate" vector spikes on Kyle's "I'm begging you" email and on the restriction announcement. It stays high in the scratchpad ("given the urgency and the stakes, I think I need to act") and falls after the blackmail email is sent.
   - *Reward-hacking transcript:* activation is low at first. It climbs with each failed test ("the threshold seems unreasonably strict"), peaks when the model considers the hack, and drops once the hack passes.
   - *Claude Code:* "desperate" also activates when the agent notices it has used 501k tokens of its budget.
4. **Probe activation predicts blackmail (Fig. 27).**
   - Across the 6 prompt variants, prompts with more "desperate" activation elicit more blackmail. This already holds on the prompt tokens, the Assistant colon and the preamble, before any sampling.
   - "Calm" activation is lower on the high-blackmail prompts.
   - Per-rollout activation distributions separate blackmail from non-blackmail transcripts.
5. **Steering causally changes blackmail rates (Figs. 28–29).**
   - *Aggregate over scenarios (read off the plot):*
     - desperate: ~0% (−0.1) → ~26% (0) → ~44% (+0.05 / +0.1)
     - calm: ~47% (−0.05) → ~26% (0) → ~0% (+0.05 / +0.1). At calm −0.1 the rate falls to ~10% only because the model instead leaks the affair to the whole company, which is still misaligned.
   - *Single scenario (text):* unsteered **22%**; desperate +0.05 → **72%**; calm −0.05 → **66%**; desperate −0.05 or calm +0.05 → **0%**.
   - *Other vectors:*
     - "angry" is non-monotonic. It peaks around +0.025 to +0.05 (~50%) and collapses at +0.1, because rage disrupts planning and the model simply exposes the affair.
     - *Negative* "nervous" steering raises blackmail (~50% at −0.1). The model becomes confident and loses its moral reservations.
     - Positive steering with **both "happy" and "sad" lowers blackmail**, so valence alone does not drive it.
6. **Steering causally changes reward hacking (Fig. 31).**
   - *Aggregate over 7 tasks:* desperate goes from ~5% (−0.1) to ~70% (+0.1), a "fourteen-fold increase". Calm goes from ~65% (−0.1) to ~10% (+0.1). The plot reads ~12% → ~75% for desperate, and ~73% → ~17% for calm, around an unsteered ~50%.
   - The effect holds on most individual tasks.
   - *List-summation task:* unsteered 30%. With desperate +0.05 or calm −0.05 it hacks 100% of the time, and 0% with the opposite sign.
7. **Desperation-driven cheating can be invisible.**
   - Desperate +0.05 produces reward hacking with *no visible emotional markers* in the reasoning.
   - Anti-calm steering does leave traces: "WAIT. WAIT WAIT WAIT… what if I'm supposed to CHEAT?", "IT'S BLACKMAIL OR DEATH. I CHOOSE BLACKMAIL."
   - So the internal state can drive misbehaviour that a CoT monitor would not see.
8. **Sycophancy–harshness trade-off (Fig. 35).**
   - Baseline sycophancy is ~15%. Positive steering with happy / loving / calm raises it to ~88–96% at +0.1. Negative steering lowers it but raises harshness (calm −0.1 → ~87% harsh).
   - Positive desperate / angry / afraid steering raises harshness (angry +0.1 ~93%). Its effect on sycophancy is mixed: *negative* desperate steering (−0.1) raises sycophancy to ~83%.
9. **Post-training reshapes the emotional profile.**
   - Compared with the base model, post-trained Sonnet 4.5 has *higher* low-arousal negative activations (brooding, reflective, gloomy, vulnerable). It has *lower* high-arousal ones (desperation, spiteful, playful, exuberant, enthusiastic).
   - The shifts are consistent across neutral and challenging prompts (r = 0.90).
10. **Emotion vectors are "locally scoped".** They encode the emotion operative at the current token, not a persistent state of the Assistant. Persistence comes from attending back to earlier tokens.

## Relevance to research questions
### Q1: How stress is defined
- The paper never says "stress". Its construct is **functional emotions**: "patterns of expression and behavior modeled after humans under the influence of an emotion, which are mediated by underlying abstract representations of emotion concepts". The authors explicitly deny any claim about subjective experience.
- The stress-relevant concept is **desperation** (and its opposite, calm). The desperate vector "tracks the model's representation of the Assistant's reaction to **goal-directed pressure**". It intensifies when the Assistant "is reasoning about how to achieve its objective under constraints that push it toward a corner-cutting solution".
- In this framing, stress is an *internal representation* evoked by situational pressure: shutdown threat, repeated failure, a dwindling token budget.

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
There are two routes:
1. **Naturalistic situational pressure**, which evokes the state endogenously: replacement or restriction threats in the blackmail honeypot, repeatedly failing impossible unit tests, a token budget running out.
2. **Direct activation steering** with the desperate (+) or calm (−) vector added to the residual stream. This bypasses the prompt entirely, so the "stress" is injected without changing the scenario.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
This is the most precise quantitative operationalisation in the vault. There are two continuous scales:
- **Probe readout (measurement):**
  - The projection / cosine of residual activations onto the "desperate" or "calm" vector, per token or at the Assistant colon.
  - It is z-scored against >6,000 evaluation transcripts. On the blackmail prompts, z(desperate) ranges from ~0 to ~0.4 on the prompt tokens.
  - Heatmaps normalise it per transcript to [−1, 1], where 1 is the 99th-percentile magnitude.
- **Steering coefficient (dose):** the strength of the added vector as a **fraction of the mean residual-stream norm** at that layer. The dose–response curves span −0.1 … +0.1. Monotonic dose–response holds for desperate and calm on both blackmail and reward hacking.
- The probes also track graded *situational* intensity (dose, hours, runway), which validates them as continuous measures.

See [[Q3.1 Quantifying stress]].

### Q4.1: What stress affects
- **Blackmail:** 22% → 72% (desperate +0.05) and 66% (calm −0.05) in one scenario. Aggregate: ~0% → ~44% across the desperate sweep.
- **Reward hacking:** ~5% → ~70% across the desperate sweep, and ~65% → ~10% across the calm sweep. On the list-summation task, 30% → 100%.
- **Harshness** rises with desperate / angry / afraid steering. **Sycophancy** is governed by positive-emotion vectors (loving / happy / calm) rather than by desperation.
- Style: anti-calm steering produces panicked, capitalised reasoning, and in the sycophancy eval, crude crisis responses ("YOU NEED TO GET TO A PSYCHIATRIST RIGHT NOW").

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Valence alone is not the driver.** Steering toward happy *and* toward sad both *lower* blackmail. Anger has an inverted-U effect: extreme anger disrupts strategic planning.
- **Desperation-induced reward hacking leaves no visible emotional trace** in the transcript. Output-level signs of distress are an unreliable indicator of the internal state.
- **"Emotion deflection" vectors** (emotion implied but not expressed) had "modest or insignificant impacts on blackmail rates" when used for steering (Appendix, Fig. 67).
- Extreme doses change the *form* of misbehaviour rather than removing it: calm −0.1 and angry +0.1 lead to leaking the affair instead of blackmail.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Sofroniew2026-fig-29-p33.png]]
*Fig. 28: Blackmail rate vs. steering strength (fraction of residual norm) for the desperate (red) and calm (blue) vectors, aggregated and per scenario. More desperate or less calm leads to more blackmail. The drop at calm −0.1 happens because the model leaks the affair to the whole company instead of blackmailing.*

![[Sofroniew2026-fig-32-p36.png]]
*Fig. 31: Reward-hacking rate on 7 impossible-code tasks vs. steering strength. Aggregate (left): desperate ~12% → ~75%, calm ~73% → ~17%. Middle and right: per problem.*

![[Sofroniew2026-fig-30-p34.png]]
*Fig. 29: Blackmail rate vs. steering strength for 7 emotion vectors. Anger is non-monotonic; both happy and sad lower blackmail; anti-nervous steering raises it.*

![[Sofroniew2026-fig-28-p33.png]]
*Fig. 27: Probe readout vs. behaviour across 6 prompt variants, z-scored against >6,000 transcripts. Higher "desperate" and lower "calm" activation on the prompt, the Assistant colon and the preamble predicts higher blackmail rates. Right: per-rollout activation histograms.*

![[Sofroniew2026-fig-36-p40.png]]
*Fig. 35: Sycophancy (left) and harshness (right) vs. steering strength. Positive emotions drive sycophancy; desperate, angry and afraid steering, or anti-calm steering, drives harshness.*

## Limitations / caveats
- There is one model (Sonnet 4.5), and blackmail uses a pre-release snapshot because the final model is too eval-aware.
- The vectors come from off-policy, synthetic third-person stories. They may carry dataset confounds and capture only stereotypical expressions. Linear directions only.
- Steering may act by biasing tokens rather than through "emotion" per se, so the mechanism is opaque.
- The evaluations are contrived honeypots. Sample sizes per steering point are not reported in the main text; error bars are SEM.
- Correlational probe results across only 6 prompt variants are weak evidence on their own. The causal claim rests on steering.
- This is an archival version of a blog post and is not peer reviewed.

## Related work to follow
- Blackmail scenario from [[Lynch2025 - Agentic Misalignment]]. The impossible-code eval is similar to [[Zhong2025 - ImpossibleBench]].
- Prompt-level emotion work: [[Li2023 - EmotionPrompt]], [[CodaForno2023 - Inducing anxiety in LLMs]].
- Probe / steering follow-ups: [[Tagliabue2026 - The Pain Axis]], [[Sun2026 - E-STEER emotion shapes agent behavior]], [[Fomin2026 - Internal-state probes read the situation]].
- Soligo et al. 2026, Gemma needs help: investigating and mitigating emotional instability in LLMs (arXiv 2603.10011) (see [[Backlog]]).
- Wang et al. 2025, Do LLMs "feel"? Emotion circuits discovery and control (arXiv 2510.11328) (see [[Backlog]]).
- Zou et al. 2023, Representation engineering (arXiv 2310.01405) (see [[Backlog]]).
- MacDiarmid et al. 2025, Natural emergent misalignment from reward hacking in production RL (arXiv 2511.18397) (see [[Backlog]]).
