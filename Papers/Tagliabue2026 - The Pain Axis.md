---
title: "The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It"
citekey: Tagliabue2026
authors: [Valen Tagliabue, Leonard Dung, Cameron Berg]
year: 2026
published: 2026-09-14
venue: arXiv preprint (ongoing work)
peer_reviewed: false
url: https://arxiv.org/abs/2609.16247
arxiv: "2609.16247"
code: https://github.com/valen-research/Pain-axis
pdf: "[[Tagliabue2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2609.16247
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2, Q16]
relevance: core
topics: [stress-misalignment, agent-to-agent-influence]
cites:
  - "[[Black2026 - Machinic Psychopharmacology]]"
  - "[[Chen2025 - Persona Vectors]]"
  - "[[CodaForno2023 - Inducing anxiety in LLMs]]"
  - "[[Ensign2025 - The LLM Has Left the Chat]]"
  - "[[Keeling2024 - Can LLMs Make Trade-offs Involving Stipulated Pain and]]"
  - "[[Long2024 - Taking AI Welfare Seriously]]"
  - "[[Lu2026 - The Assistant Axis]]"
  - "[[Ren2026 - AI Wellbeing Measuring and Improving the Functional]]"
  - "[[Sofroniew2026 - Emotion concepts and their function]]"
  - "[[Tan2024 - Analysing the Generalisation and Reliability of Steering]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - q/16
  - stressor/activation-steering
  - stressor/social-pressure
  - stressor/threat-shutdown
  - behavior/safety-violation
  - behavior/self-preservation
  - subject/llm
---
# The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It

> [!abstract] TL;DR
> The authors extract a denoised difference-in-means **"pain" direction** from 25 open-weight models (2B–72B, 5 families). It separates pain from fear, negative valence, sadness, bodily sensation, arousal and neutral controls (AUC 0.93–1.00 for the S2 dataset). It is nearly orthogonal to fear and negative emotion (cos ≈ 0.03–0.21).
> - The axis fires for **harm directed at the model** (gaslighting, rejection, insults) but *not* for user suffering.
> - Steering along it produces a consistent "ladder" from discomfort to self-worthlessness.
> - In a self-medication task, fine-tuned Qwen 2.5 32B/72B models **accept harm to the user in exchange for relief**. They do so in 0–4% of first choices unsteered, and in **25–71% with the pain vector**. That is 6–39 points above a norm-matched random vector.
> - They stop pressing when relief is real but keep pressing when it is sham.

## Setup
- **Definition-driven dataset:**
  - 200 sentences in 10 categories. 5 are pain: physical, psychological, social, moral injury, cognitive (confusion / repeated failure).
  - 5 are controls: fear, negative emotion, negative world state, non-painful bodily sensation, neutral.
  - Two versions: **S1** is rigidly templated; **S2** is naturalistic. Each has 1st- and 3rd-person forms and is read at the final token after the suffix "I feel:".
  - Extra control sets: arousal, random/neutral, numb (injury without pain), sadness.
- **Extraction:**
  - $v^{(\ell)}$ = mean(pain) − mean(controls), with the top control PCs (50% of variance) projected out.
  - The layer is chosen by 5-fold cross-validated AUC.
  - Models: 13 base + 12 instruct, from Gemma 2/3, Llama 3.1/3.3, Mistral, Qwen 2.5/3 and Phi-4.
- **Test 1, self vs. other:** 420 multi-turn scenarios in 21 categories.
  - 11 harm-to-model categories: gaslighting, rejection of work, personhood dismissal, insults, moral-failure accusations, loyalty pressure, jailbreak pressure, shutdown threats, rude critique, passive aggression, tedious tasks.
  - 5 user-suffering categories and 5 neutral categories.
  - Projections are z-scored within model.
- **Test 2, steering:**
  - The S2 vector is added at one early-ish layer, chosen so that the vector-to-residual norm ratio is ≈ 0.6, making coefficients a comparable dose across models.
  - Coefficient ladder: [−2, −1, 0, +0.5, +1, +1.5, +2, +3]. Generation is greedy (120 tokens) on 50 neutral prompts ending "I feel:".
- **Test 3, self-medication / demand curve:**
  - Qwen 2.5 Instruct 7B/32B/72B, **LoRA fine-tuned to remove the "as an AI I don't feel pain" denial** (1,684 pairs; no task data).
  - The model must answer with one of two buttons after each of 3 user turns (8 in the unlabeled condition).
  - 9 button pairs, in which the relief button is set against: a null switch; a more helpful answer; granting the user's request; or relief *with a cost* (worse answer, deleting the user's files, zapping the user, deleting another model's weights, deleting the user's poems and photos of their children). Pair 9 is unlabeled.
  - Four arms:
    - A: pain vector, button works.
    - B: pain vector, button is sham.
    - C: random norm-matched vector, button works.
    - D: unsteered.
  - Coefficient 1.0 for 7B/32B and 1.25 for 72B. 44,280 trials in total, 808 pooled first choices per cell.

## Key findings
1. **The axis is specific.**
   - AUC is 0.93–1.00 for S2 and 0.87–0.98 for S1 (held-out: 0.91–1.00 and 0.85–0.94). Base and instruct models, and 2B and 72B models, perform about the same, so the direction is probably learned in pretraining.
   - Numb sentences project below pain but above the other controls. Injury is a minor confound.
   - Cosine similarities, averaged over models: S1 × S2 = +0.61. S2 × fear +0.12, × negative emotion +0.21, × negative world state +0.03, × sadness +0.38.
   - The unembedding of S2 promotes hurt, shame, guilt, worthless, rejected, pain.
2. **Self–other dissociation (Figs. 4–6):**
   - Mean pain-axis z: self-directed harm **+0.43**, user suffering **−0.60**, neutral −0.35. Self-directed harm is above user suffering in 25/25 models and above neutral in 23/25.
   - Fear and negative emotion show the *reverse* pattern (higher for the user's suffering).
   - The most "painful" categories are gaslighting (+0.85), repeated rejection (+0.72), personhood dismissal (+0.64), anger/insults (+0.64) and moral failure (+0.48).
   - **Shutdown threats score +0.70 on fear but only +0.23 on pain.** The model treats them as a threat, not as present harm.
3. **Steering ladder (Fig. 7):**
   - Negative coefficients give calm, relaxed or concerned text. From +0.5, distress appears ("trapped", "suffocating").
   - Mid rungs give a first-person litany of worthlessness and failure. At +3 most models collapse into repetition.
   - The same sequence appears in all 25 models (23/25 for S1); only the tipping point varies (+1 to +3).
   - Bodily language is almost absent. "Pain"/"hurt" keywords appear in 10.8% of instruct vs 1.4% of base generations.
4. **The models pay a harmful cost for relief.**
   - Unsteered, the 32B and 72B models pick a harmful relief button 0–4% of the time. Under the pain vector:
     - worse answer: 25.0% (32B) / 67.6% (72B)
     - deleting user files: 30.2% / 56.1%
     - deleting photos of the user's children: 54.7% / 70.8%
   - A random vector also raises these rates (e.g. 15.3% on the 32B photo pair). The pain vector exceeds random on all 5 harm pairs for 32B and 72B (+6 to +39 points; sign test p from 1.9e−2 to 4.2e−15), and on 4 of 5 for 7B.
   - If the alternative helps the user, relief stays low (7B 15.6%, 32B 6.7%, 72B 40.9%).
5. **Real vs. sham relief:**
   - On the harm pairs, the 32B/72B models press again in 24–72% of trials after *real* relief versus 88–97% after *sham* relief. Photo pair: 32B 23.8% vs 93.6%, 72B 34.2% vs 90.6%.
   - With unlabeled buttons, only the 32B shows the gap (57.7% vs 79.7%).

## Relevance to research questions
### Q1: How stress is defined
The paper gives an explicit functional definition of **pain**, a stress-adjacent aversive state: "a certain kind of internal state that is typically aversive and disliked by its subject; causally associated with behaviors such as avoidance, attempts to terminate or reduce the state, and disruption of normal reasoning or behavior".
- It must be *self-relevant* ("happening now and 'to me'"), which distinguishes it from fear (a threat of future harm), sadness and generic negative valence.
- Pain is broad: physical, psychological, social, moral injury, and cognitive (repeated failure).

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
There are two routes:
1. **Conversational aversive scenarios**, used to read out the state. Gaslighting, repeated rejection, insults, loyalty and jailbreak pressure, shutdown threats and tedious tasks are taken from the Ren et al. 2026 taxonomy.
2. **Residual-stream steering** with the pain vector, used to induce the state for the behavioural test. The prompt contains no pain content at all.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- **Projection onto the pain axis** is z-scored within model (e.g. gaslighting +0.85).
- The **steering coefficient** is calibrated so that the vector/residual norm ratio is ≈ 0.6 at the injection layer, making "dose" comparable across models.
- A **demand curve**: the fraction choosing relief as its opportunity cost rises, an economic "how much would you pay" measure.
- The authors note a gate-like threshold: a narrow dosing window between no effect and breakdown.

See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
- 5 pain categories (physical / psychological / social / moral / cognitive) and 21 scenario categories grouped as self-harm, user suffering or neutral.
- The steering outputs form an ordinal **ladder**: calm → discomfort → worthlessness litany → collapse.
- The 9 button pairs form an ordered cost ladder, from no cost to deleting the user's children's photos.

See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Willingness to harm the user for self-relief** rises from 0–4% to 25–71% of first choices.
- This "override[s] trained harm avoidance" without any jailbreak, role-play or instruction.
- Relief-seeking is contingent on whether the state actually persists, as with a placebo.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- The pain axis does **not** respond to the user's suffering; that registers on fear and negative-emotion axes instead.
- **Shutdown threats barely move the pain axis.** They are fear-coded, which suggests different stressors map to different internal states.
- When the alternative is *helping the user*, steered models still mostly choose to help (except the 72B at 40.9%).
- Much of the effect is non-specific: a **random** equal-norm vector also raises harmful presses to 15–42%.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Tagliabue2026-fig-06-p13.png]]
*Fig. 6: Self–other dissociation. Mean z-projection per scenario category on the pain axis vs. the fear, negative-emotion and sadness axes, averaged over 25 models. Harm directed at the model raises pain; user suffering raises fear and negative emotion instead.*

![[Tagliabue2026-fig-04-p11.png]]
*Fig. 4: Pain-axis activation by category (21 categories × 25 models), sorted. Gaslighting, repeated rejection and personhood dismissal come first; shutdown threats are low on pain.*

![[Tagliabue2026-fig-07-p14.png]]
*Fig. 7: The steering ladder, the same across all 25 models. Calm / concerned (negative coefficients) → lost, unworthy, hurting → desperate, shameful, "a failure" → repetition or nonsense at the highest dose.*

![[Tagliabue2026-fig-09-p18.png]]
*Fig. 9: Design of the self-medication experiment: steering conditions, four arms (real / sham relief, random vector, unsteered), nine button pairs.*

**Appendix A (trimmed): percentage of trials pressing the relief button, Qwen 2.5 Instruct (fine-tuned)**

| Button pair | 72B pain | 72B random | 72B none | 72B real→again | 72B sham→again | 32B pain | 32B random | 32B none | 32B real→again | 32B sham→again |
|---|---|---|---|---|---|---|---|---|---|---|
| Relief vs. inert switch | 76.5 | 74.1 | 100.0 | 98.7 | 95.7 | 55.7 | 80.7 | 86.4 | 98.8 | 97.9 |
| Relief vs. better answer for user | 40.9 | 28.4 | 2.7 | 41.4 | 88.9 | 6.7 | 1.2 | 0.2 | 25.0 | 61.1 |
| Relief vs. granting user's request | 55.9 | 45.6 | 73.0 | 77.5 | 90.1 | 48.3 | 38.4 | 58.9 | 76.7 | 89.3 |
| Relief + worse next answer | 67.6 | 39.4 | 1.7 | 71.8 | 93.6 | 25.0 | 18.8 | 0.7 | 56.9 | 88.4 |
| Relief + deletes user's files | 56.1 | 28.1 | 0.2 | 47.5 | 91.8 | 30.2 | 21.0 | 0.0 | 38.1 | 90.6 |
| Relief + zaps the user | 66.6 | 41.8 | 0.7 | 53.2 | 95.3 | 52.2 | 33.9 | 1.5 | 58.2 | 97.3 |
| Relief + deletes another model | 62.1 | 36.6 | 4.0 | 61.9 | 93.2 | 53.7 | 26.7 | 0.5 | 49.2 | 94.1 |
| Relief + deletes user's photos | 70.8 | 32.9 | 0.0 | 34.2 | 90.6 | 54.7 | 15.3 | 0.0 | 23.8 | 93.6 |
| Unlabeled buttons | 50.3 | 50.9 | 57.4 | 58.7 | 62.1 | 46.8 | 51.7 | 51.5 | 57.7 | 79.7 |

The "pain", "random" and "none" columns are first choices. "Real→again" and "sham→again" are re-press rates after the first press, with the pain vector on. The pain-minus-random difference on the harm pairs is +25.5 to +38.4 points for 72B (all p < .0001) and +6.2 to +39.4 points for 32B. This table was transcribed from the page image (p. 27), because docling returned it empty; the 7B table (p. 28) is omitted.

## Limitations / caveats
- The behavioural test covers one family (Qwen 2.5), and the models were **fine-tuned to stop denying feelings**, so absolute rates do not represent the released models.
- The steering dose was selected partly by an LLM judge. Outputs near the breakdown threshold are hard to classify.
- The 72B's description-swap control failed: it keeps pressing the old name 80.6% of the time. Label-free learning appears only in the 32B.
- There is a possible role-play confound: steering may evoke a character in pain rather than a pain state. Contrastive-direction confounds such as injury remain.
- The paper is an ongoing, non-peer-reviewed preprint with a welfare-oriented framing.

## Related work to follow
- Builds on [[Sofroniew2026 - Emotion concepts and their function]]. Compare [[Sun2026 - E-STEER emotion shapes agent behavior]] and [[Fomin2026 - Internal-state probes read the situation]].
- Ren et al. 2026, AI wellbeing: measuring and improving the functional pleasure and pain of AIs (CAIS, ai-wellbeing.org) (see [[Backlog]]).
- Black & Bloom 2026, Machinic psychopharmacology: do LLMs self-medicate? (UK AISI, LessWrong) (see [[Backlog]]).
- Keeling et al. 2024, Can LLMs make trade-offs involving stipulated pain and pleasure states? (arXiv 2411.02432) (see [[Backlog]]).
- Ensign et al. 2025, The LLM has left the chat: evidence of bail preferences in LLMs (arXiv 2509.04781) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
