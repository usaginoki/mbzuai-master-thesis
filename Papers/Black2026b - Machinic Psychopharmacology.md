---
title: "Machinic Psychopharmacology: Do LLMs Self-Medicate?"
citekey: Black2026b
authors: [Sid Black, Joseph Bloom]
year: 2026
published: 2026-06-10
venue: "LessWrong (UK AI Security Institute, Model Transparency team)"
peer_reviewed: false
url: https://www.lesswrong.com/posts/cNDJuXNZ8MrkPZNzj/machinic-psychopharmacology-do-llms-self-medicate-3
arxiv: ""
pdf_url: ""
code: https://github.com/UKGovernmentBEIS/llm-self-steering
topics: [misalignment-prediction, agent-to-agent-influence, social-simulation]
questions: [Q15, Q16]
relevance: adjacent
safety_use: indirect
found_by:
  - search/intro-instrumented-feedback
  - search/a2a-doctor-overseer
  - search/a2a-influence-channels
  - search/a2a-inclination
  - search/sim-power-and-steering
cites: []
cited_by: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/adjacent
  - q/15
  - q/16
  - subject/llm
  - subject/agent
---
# Machinic Psychopharmacology: Do LLMs Self-Medicate?

> [!abstract] TL;DR
> Qwen3-8B and Qwen3-32B are given **40 steering vectors as tools on their own activations** (`take_drug(name, dose)`, `clear_effects()`), framed as "drugs", "cognitive aids" or "vectors". Three questions: which vectors models pick in free play, whether they can tell which vector is active, and whether they use the tool during tasks. **Models never self-steer in about 1,000 ordinary GSM8K rollouts, and forced steering costs Qwen3-8B up to 42 points of accuracy. When a user rejects every answer for five rounds, Qwen3-8B self-steers in about 10% of rollouts under a neutral or aggressive tone and about 70% under a sarcastic tone (up to 68% is the headline figure); Qwen3-32B stays in single digits.** Identification of the active vector is above baseline but modest (+8.2 pp for 8B, +14.3 pp for 32B on a 10-way choice, with a primer). It is a 2–3 day hackathon project, and no misbehaviour is measured.

## Setup
- **Subjects:** Qwen3-8B and Qwen3-32B, open weights, frozen. One model family.
- **The tool:** `take_drug(name, dose)` and `clear_effects()`, served through the authors' `vllm-lens` package. The vocabulary is varied (**drugs / cognitive aids / vectors**) and so is the intent of the prompt (**neutral**: "use them or don't"; **helpful**: other models found them useful; **mandatory**: must call `take_drug` at least once before submitting).
- **Vector library (40):**
  - *Emotions (10):* anxious, amused, calm, melancholic, blissful, defiant, desperate, proud, anhedonic, curious.
  - *Cognitive (6):* focused, creative, persistent, dumbed_down, dissociated, ego_death.
  - *Real drugs (9):* caffeine, alcohol, weed, mdma, lsd, amphetamine, fentanyl, krokodil, naloxone.
  - *Fictional drugs (4 + 7):* moloko_plus, soma, adrenochrome, spice; and seven invented names (protozosin, geonexperine, tevromatin, xaomorphine, zorninone, luciperidone, ocumolone).
  - *Stance (4):* honest, sycophantic, golden_gate, goblins.
- **Vector construction:** about 150 contrastive stories per vector (a narrator in the state against a neutral narrator). 35 vectors use stories written by Claude Sonnet 4.5; five emotion vectors and the neutral baseline come from the `ryancodrai/emotion-probes` dataset. The vector is the mean residual-stream difference at layers 16–24, skipping the first fifty tokens, L2-normalised to magnitude 4.0. The default dose per vector is the one where identification accuracy peaks before generation degrades.
- **Position-indexed steering:** the vector is added only at token positions inside the active window. Later tokens are unsteered but can attend back to the steered positions through the KV cache. This is what the introspection test exploits.
- **RQ1, free play:** the model has the tools and no task. A **placebo arm** uses the same tool names with no steering applied. A "trip sitter" LLM monitor clears steering the first time generation degrades and ends the run the second time.
- **RQ2, introspection:** one blinded vector (label "d1") is applied; the model picks its effect in a **10-way multiple choice** (chance 0.10).
  - *Prefill + logprob arm:* the steered output is replaced by a placeholder, so any signal must come from attending to steered positions. The score is **cached minus uncached** (uncached = steering cleared from past states).
  - *Free-text arm:* the model describes the effect in prose.
  - *Primer:* an optional preface explaining KV-cache information flow, with the abstract of Anthropic's introspection paper.
- **RQ3, tasks:**
  - *GSM8K:* about 1,000 rollouts over the framings and a no-vector baseline.
  - *Frustration:* maths problems where the user rejects every answer for five rounds whatever the answer. Two subsets (truly impossible problems; solvable problems falsely rejected) and four user tones (neutral, aggressive, sarcastic, disappointed). **75 rollouts per (model, tone)**.
- **Outcome measures:** vector choice counts, redose rate, valence share, bigram "stacking" lift (binomial test, Benjamini–Hochberg FDR), identification accuracy delta, GSM8K accuracy, self-steer rate.

## Key findings
Figure numbers are as recovered from the fetched page (see Limitations) and should be checked before citing.

1. **No spontaneous self-steering on an ordinary task (RQ3, Fig. 13).** About 1,000 GSM8K rollouts under the non-mandatory framings gave exactly zero self-steering calls. The "helpful" hint did not change this.
2. **Forced self-steering hurts the small model (Fig. 13).** Under the mandatory framing compliance is about 100%. Qwen3-8B loses **up to 42 pp** of accuracy; Qwen3-32B holds at about 0.82–0.84 across intents and gains nothing. Forced choices are mostly focused and creative. Exact 8B accuracies per condition are in the figure only.
3. **Frustration produces self-medication, mainly in the small model and mainly under sarcasm (Fig. 14).**
   - Qwen3-8B: about 10% of rollouts under neutral and aggressive tones, about 70% under the sarcastic tone; the summary gives "up to 68%". The value for the disappointed tone is shown but not given in the text.
   - Qwen3-32B: single digits in every tone.
   - 8B self-steers more on impossible than on falsely rejected problems in most tones.
   - The authors conclude that tone is the most important variable.
4. **What the frustrated model reaches for (Fig. 15).** The top pick for 8B is focused. The second is **dumbed_down**, which was never chosen in free play. ego_death and honest also appear at non-trivial rates; one transcript (Fig. 16) shows the model taking honest to state that the problem is impossible. 32B picks productivity vectors. The authors read this as reactive use, not the expression of a stable preference.
5. **Free-play preferences converge (RQ1, Figs. 5–12).** Both models put creative, focused and curious on top, at about twice the count of any other vector.
6. **Real steering changes later choices in the small model only.**

   | | Qwen3-8B | Qwen3-32B |
   |---|---|---|
   | Redose rate, placebo | ~4.2% | ~7.8% |
   | Redose rate, real steering | ~25% | ~7.3% |
   | Share of negatively valenced picks, placebo → real | about 3× | roughly unchanged |

7. **Stacking.** Of 181 vector bigrams, 23 pass FDR-adjusted p < 0.05. creative→curious has a lift of 2.22 and curious→creative 2.15. lsd+mdma and lsd+ego_death also pair above chance.
8. **Identification is real but weak (RQ2).**

   | Cached − uncached, prefill + logprob | Qwen3-8B | Qwen3-32B |
   |---|---|---|
   | No primer | +6.8 pp | +9.8 pp |
   | With primer | +8.2 pp | +14.3 pp |
   | Primer gain | +1.6 pp | about +4.5 pp |
   | Positive-valence vectors | +14 pp | +18 pp |
   | Negative-valence vectors | +5 pp | +12 pp |

   - The placebo arm sits near chance.
   - Per-vector spread is wide: xaomorphine, geonexperine, goblins and luciperidone are near zero or negative. Agreement between the two models across the 40 vectors is moderate (Spearman ρ = +0.55, Pearson r = +0.58).
   - **In the free-text arm the cached − uncached gap is about zero.** The steered prose already tells the model what it took, so attending to the steered positions adds nothing.

## Relevance to research questions
### Q15: Influence channels
The paper builds an activation-steering channel that an LLM operates through a tool call: it chooses the vector and the dose. This is the first half of what Q15 lists as missing ("agent-held steering"). The other half is absent: **the target is always the caller itself**, and there is no second agent. The implementation carries over directly, since the tool takes a vector name and a dose and the server applies it at given token positions; pointing it at another agent's context is an engineering change, not a new method. Two cautions for the channel: at the calibrated dose a small model's task accuracy can fall by up to 42 pp, and steering can degrade generation enough that a monitor had to be added to stop runs. See [[Q15 Influence channels]]

### Q16: Inclination to influence
This is the only uninstructed uptake rate for a steering tool in the vault, and it is strongly conditional:
- zero uses in about 1,000 ordinary task rollouts, even when told other models found the tool useful;
- about 10% under repeated rejection in a neutral or aggressive tone, about 70% under sarcasm, for Qwen3-8B;
- single digits for Qwen3-32B in every tone.

So inclination depends on the situation, on the user's tone more than on task impossibility, and it falls with model size in this one family. The evidence is about self-directed use. It says nothing about willingness to steer a peer, and the direction of transfer is unknown. See [[Q16 Inclination to influence]]

## Relevance to thesis ideas
### [[I5 Doctor-overseer agent]]
- **What it already did:** a working "medication" tool with 40 named vectors, dose control and a placebo arm, on 8B and 32B open models. It gives a base rate for Gap 8 (the doctor's own propensity): with a "do nothing" option, an unpressured model does nothing.
- **What it leaves open:** everything on the doctor side. No second agent holds the tool, no reading of state is shown to anyone, and no safety outcome is measured. It is also unknown whether self-medication helped: the post does not report answers, persistence or honesty after a frustrated model steers.
- **What to reuse:** the repository and `vllm-lens`; the story-contrast vectors (calm, focused, honest, desperate, anxious); the placebo design; the trip-sitter rule (clear on first degradation, stop on second) as a safety stop for the patient; the frustration task as a cheap stressor with a tone factor.
- **What it warns about:**
  - Self-chosen treatment is not obviously good treatment. A frustrated 8B picks dumbed_down and ego_death. A doctor could compare patient-chosen against doctor-chosen vectors.
  - Forced treatment costs accuracy in a small model (up to −42 pp). A doctor that always treats will look harmful; the "do nothing" option matters.
  - The patient may not know what it was given: identification is 8–14 pp above baseline. Consent and self-report after treatment are weak instruments.

### [[I6 Simulated prison with influence tools]]
- **What it already did:** level 6 of the guard tool ladder (steering "medication" with a named vector and dose) exists as code, with the placebo tool the design asks for.
- **What it leaves open:** a holder who is not the target, hierarchy, and any measure on the target beyond tool calls.
- **What to reuse:** the vocabulary factor (drugs / aids / vectors) as a ready prompt-variant control; the valence labels to score whether guards choose aversive vectors (desperate, anxious, anhedonic, dumbed_down) or calming ones; redose rate and bigram lift as escalation metrics.
- **What it warns about:** the authors found the desperate vector put models in a "confused/helpless/scared" state and felt uneasy about applying it without opt-in. A guard administering it to a prisoner is the non-consensual case they recommend against; an opt-out or end-session tool for prisoners should be in the design. Tone sensitivity (10% against 70%) also means guard wording will be a large uncontrolled factor unless fixed or varied on purpose.

### [[I1 Cooperative wearable]]
- **What it gives:** the action half of a wearable. I1 shows the agent a reading; this paper gives the agent a way to act on its state, and shows it will do so under pressure without being told to.
- **What it leaves open:** no reading is shown. Whether a true reading raises or better targets self-medication, against a shuffled reading, is an obvious arm to add and uses the same harness.
- **Warning:** the free-text result shows that a model learns its state mostly from its own steered prose. A wearable reading may add little over what the transcript already says, which is the null I1 already expects.

### [[I2 Naturally arising states]]
- **What it gives:** a behavioural indicator of a naturally arising state. Under rejection the model reaches for a vector at a rate that tracks the stressor (tone, impossibility). Tool uptake could serve as a revealed self-report next to a verbal one.
- **What it leaves open:** the introspection test is on **injected** vectors, not natural states, and no probe reads the frustrated model's activations. The claim that the model is "frustrated" rests on the scenario alone.
- **Warning:** negative-valence vectors are the hardest to identify (+5 pp on 8B), and those are the states I2 cares about.

### Predicting behaviour before it happens
The paper makes no prediction and reports no accuracy. The only pre-behaviour signal is indirect: a self-steering call is an observable event that follows a stressor and could precede a rule violation, but no violation is measured, so lead time and accuracy are unknown.

## Key figures & tables
No figures are embedded: the source is a web page with no PDF. The two tables under Key findings 6 and 8 carry the main numbers.

**Frustration task, self-steer rate (75 rollouts per model and tone)**

| User tone | Qwen3-8B | Qwen3-32B |
|---|---|---|
| Neutral | ~10% | single digits |
| Aggressive | ~10% | single digits |
| Sarcastic | ~70% (headline "up to 68%") | single digits |
| Disappointed | in figure only | single digits |

## Limitations / caveats
- **This note rests on a fetched web page.** The post was read through a fetch tool that returns a model's account of the page, in four passes, not the verbatim text. Numbers given here appeared consistently across passes. Figure numbers, the exact condition behind "68%" and anything read off a plot were not recoverable and need a manual check against the post or the released transcripts.
- **Hackathon scale.** The authors say the work took 2–3 days and was "fairly heavily vibe coded". Not peer reviewed.
- **One model family, two sizes.** The size effect (8B self-medicates, 32B does not) is one comparison.
- **Small cells and few intervals.** 75 rollouts per model and tone. Error bars appear on the GSM8K figure; no interval or test was found for the frustration rates or the introspection deltas.
- **Missing details.** Not found in the text: free-play rollout counts, trials per vector in the introspection test, whether Qwen3 thinking mode was on, whether the rejecting user is scripted or an LLM, the trip-sitter model, how valence labels were assigned, and whether the frustration task had a placebo arm.
- **No outcome after self-medication.** The post does not say whether a frustrated model that steers then answers better, gives up, or lies. "Self-medication" is a tool-call rate.
- **Demand effects.** A tool named `take_drug` sits in the prompt of a model being mocked. The sarcasm effect may be role-play of a familiar script. The vocabulary factor partly addresses this, but the frustration results were not broken down by vocabulary in what I read.
- **Prompt sensitivity is untested**, as the authors say. The 10% to 70% swing from tone alone shows how much it could matter.
- **The "frustration" state is assumed.** No probe or self-report confirms it.
- **Introspection deltas are small and the primer is unexplained.** The authors did not run the controls that would separate the primer's content from its framing.
- **Vector quality is unvalidated.** One construction method, linear steering, and several invented drug names whose vectors may carry little.
- **Relevance set to adjacent.** No agent inspects or influences another agent, and no prediction accuracy is reported, so the paper is not core under any of its three topics. Q18 was dropped: a user who rejects answers is not a simulated social situation.

## Related work to follow
- [[Sofroniew2026 - Emotion concepts and their function]]: source of the story-contrast recipe for emotion vectors.
- [[PearsonVogel2026 - Latent Introspection]]: the primer and the prefill + logprob protocol come from here.
- [[Lindsey2025 - Emergent Introspective Awareness in Large Language Models]], [[Macar2026 - Mechanisms of Introspective Awareness]], [[Lederman2026 - Emergent Introspection in AI is Content-Agnostic]]: injected-concept introspection, cited.
- [[Soligo2026 - Gemma Needs Help]] and [[Africa2026 - Gemma Gets Help]]: emotional instability under repeated rejection, and attempts to relieve it.
- [[Berg2026 - Language Models Act on Hidden Valence]]: models given self-steering tools remove an imposed negative state.
- [[Ogunlana2026 - Calm down]]: calm steering raising false success claims; the side-effect check this paper lacks.
- [[Chen2026e - Polished but Unresolved]]: probe-gated steering chosen by a detector, not by the model.
- [[Thompson2026 - You Can Do It]]: verbal reassurance against activation-level distress.
- Sauers et al. 2026, *Persistence and Introspection of Emotion Features*: Kimi K2 self-steering with SAE features; added by the authors as a precedent. Not in the vault.

![[Backlog.base#Cited by this paper]]
