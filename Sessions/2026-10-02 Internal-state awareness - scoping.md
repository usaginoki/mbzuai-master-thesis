---
title: "Session 2026-10-02: Internal-state awareness - scoping"
date: 2026-10-02
session: scoping
topics: [misalignment-prediction]
questions: []
tags:
  - type/session
---
# Session 2026-10-02: Can an LLM be aware of its own internal state, and is that used for safety? (scoping overview)

> [!question] Questions addressed in this session
> None created yet. This session scopes proposed **Q13** of the `misalignment-prediction` topic (see [[2026-10-01 Misalignment prediction - scoping]]): can the model itself be made aware of its own internal state, and does that improve safety?

**Idea:** people wear heart-rate monitors that make them aware of their own condition in the moment, and can be notified when a reading is off. Do LLMs or LLM agents get an equivalent awareness of their own internal states, and is it used for safety?

**Corpus / scope:**
- **56 papers** found on 2026-10-02: 39 new candidates in [[Backlog]] and 17 notes already in the vault (2 of them processed papers), now tagged `misalignment-prediction`. This is a sub-question of that topic, not a topic of its own; its candidates are the ones with a `safety_use` property and `found_by: search/intro-…`. 43 are core, 13 adjacent.
- **Nothing was processed this session.** Numbers come from abstracts, blog pages or existing vault notes, as reported by the search. Check them against the paper before quoting. The headline numbers were fact-checked against the papers' own text on 2026-10-02 and corrected; other body numbers still need checking before quoting.
- **Three search strands:** `intro-capability`, `intro-instrumented-feedback`, `intro-safety-uses-and-risks`.
- **The search is incomplete on the central design.** The `intro-instrumented-feedback` strand ran out of web searches after about 25 queries. Lab blogs and the affect/stress angle were searched least. Every "not found" below is provisional.
- **Follow-up (same day):** lab blogs and LessWrong / Alignment Forum were scanned afterwards, and three ideas were read in depth. The cooperative wearable with a safety outcome was still not found as an experiment. Several abstract-level statements below are corrected in [[2026-10-02 Internal-state awareness - idea deep dives]] (see "Corrections to the scoping note").
- **Core definition:** the model itself reports on, is informed of, or controls its own internal state, **and** this is checked against ground truth about that state or its effect on behaviour is measured.
- **New candidate property `safety_use`:** direct 26 (the self-awareness is used or evaluated for a safety purpose), risk 6 (the capability undermines oversight), indirect 19, none 5.

> [!important] The picture in six lines
> 1. **The analogy splits into two things.** *Introspection:* the model senses its own state unaided. *Instrumented feedback:* an external probe reads the state and the reading is shown to the model. The literature is large on the first and thin on the second.
> 2. **Introspection is real but weak.** Models name a concept injected into their activations about 10–20% of the time with almost no false positives. Several papers argue much of the rest is anomaly detection, response bias or solvable from the input alone.
> 3. **The literal wearable design was found only in two adversarial tests, and neither shows a benefit.** Agents given their own probe score kept colluding. A model shown past monitor verdicts shifted its activations toward evasion, but evaded only when the experimenters amplified the shift or fine-tuned the model.
> 4. **Awareness does not buy correction.** Models trained to detect steering became more steerable. Introspection training against prefill attacks raised attack success. In one study the model's reasoning recognised the injection but its action did not defend against it in 47% of exposed turns.
> 5. **What works for safety is a trained alarm or a triggered consequence.** Self-incrimination tools, red-flag tokens, reminders or reasoning prefills gated by a probe: the model is given a channel or a nudge, not a raw reading.
> 6. **The cooperative version with a reading taken from activations looks untested.** A loop on a *simulated* stress state does reduce transgressions, and a pressure probe gating an intervention exists for capability; see [[2026-10-02 Internal-state awareness - idea deep dives]].

## Map of the idea

| Design | Who reads the state | Does the model see the reading? | Safety evidence |
|---|---|---|---|
| Unaided introspection | The model | n/a | Weak and unreliable; mostly artificial injections |
| Trained self-report (adapters, confessions, self-incrimination) | The model, after training | n/a | Strong for auditing and in-the-moment flagging |
| Trained-in alarm (red-flag token, backtracking) | The model emits it | Yes, its own token | Positive |
| Probe gates an external action (reminder, prefill, steering) | External probe | Only the consequence | Positive |
| **Wearable: probe reading shown to the model** | External probe | **Yes** | Two adversarial tests; no benefit shown |
| Tools for querying activations (activation oracles) | External decoder | Not so far; used by auditors | Auditing only |

## Strand 1: Can a model sense its own state? (`intro-capability`)
- **Concept injection.** Claude Opus 4.1 names an injected concept about 20% of the time with 0 false positives in 100 controls ([[Lindsey2025 - Emergent Introspective Awareness in Large Language Models|Lindsey 2025]]). An open-model replication gets 10.8% and finds the ability comes from post-training; ablating the refusal direction raises it to 63.8% ([[Macar2026 - Mechanisms of Introspective Awareness|Macar et al. 2026]]).
- **A signal can be present but not voiced.** The model verbally denies an injection while the residual stream carries a detection signal that is attenuated in the final layers ([[PearsonVogel2026 - Latent Introspection|Pearson-Vogel et al. 2026]]).
- **Reporting and controlling a direction.** With in-context examples, models report and control their projection onto some activation directions, within a low-dimensional "metacognitive space" ([[JiAn2025 - Language Models Are Capable of Metacognitive Monitoring and|Ji-An et al. 2025]]).
- **Closest to a pulse reading:** numeric self-reports of emotive states, read from token probabilities, track probe readouts across turns (Spearman 0.40–0.76) and shift causally under steering. Plainly decoded reports are uninformative ([[Martorell2026 - Quantitative Introspection in Language Models|Martorell & Bianchi 2026]]).
- **Confidence** is computed during answering and cached internally; the cached signal explains stated confidence beyond token probabilities ([[Kumaran2026 - How do LLMs Compute Verbal Confidence|Kumaran et al. 2026]]).
- **Sceptical results.**
  - Input-only classifiers match the models' "self-reports", and models cannot tell activation tampering from input manipulation ([[Singh2026b - Can LLMs Introspect|Singh et al. 2026]]).
  - Yes/no injection detection in one small model is entirely a shift toward answering "yes", though comparative tasks show real signal for early-layer injections (83% strength comparison, 88% localisation) ([[Hahami2025 - Detecting the Disturbance|Hahami et al. 2025]]).
  - Models detect *that* something is off far better than *what* it is, and part of the detection is inference from how anomalous the prompt looks ([[Lederman2026 - Emergent Introspection in AI is Content-Agnostic|Lederman & Mahowald 2026]]).
  - Control disappears when the target requires privileged access ([[Aoki2026 - In-Context Neurofeedback|Aoki et al. 2026]]).
- **Missing link to the stress topic.** Emotion vectors drive blackmail and reward hacking and can be active without visible expression, but the paper has only a steered "I feel…" completion check, and no unsteered comparison of self-report with the vector ([[Sofroniew2026 - Emotion concepts and their function|Sofroniew et al. 2026]]).

## Strand 2: The wearable design (`intro-instrumented-feedback`)
- **Reading shown to the model, adversarial setting.**
  - Colluding agents are told an activation monitor exists and are given the previous round's probe score. They keep colluding and the probe still ranks them: in the best case AUROC is 0.994 baseline, 0.930 when aware and 0.952 with feedback, but 0.71 / 0.68 / 0.70 for a mixed-model pair, and recall at the fixed threshold drops ([[Das2026 - You Can't Escape Your Own Activations|Das et al. 2026]]).
  - With monitor verdicts visible in context, an untrained model shifts its activations toward evasion, but too weakly to evade. Detection falls from 100% to 27% only when the experimenters amplify that shift 8×, and to 4% with a small fine-tune ([[Keenan2026 - LLMs Learn to Evade Latent Monitors from Prior Feedback|Lyons Keenan et al. 2026]]).
- **Consequence shown to the model, cooperative setting.**
  - A localized "you hallucinated parameter X" message from a latent detector raises agent recovery from 23.9% to 37.0% over generic feedback ([[Vijayvargiya2026 - Actionable Hallucination Detection|Vijayvargiya & Lokesh 2026]]).
  - A reminder triggered by representation drift cuts attack success from 84% to 25% on one multi-turn agent benchmark ([[Wang2026c - Representation Transitions Reveal Emerging Safety Risks in|Wang et al. 2026]]).
  - A reasoning prefill gated by a prompt-injection probe cuts attack success from 34.6% to 0% on one model ([[Dong2026 - Your Agentic LLMs Secretly Encode Indirect Prompt-Injection|Dong et al. 2026]]).
- **Alarms the model raises itself.**
  - A red-flag token that triggers reflection gives 93% refusal of harmful prefilled queries ([[Dobre2025 - A Generative Approach to LLM Harmfulness Mitigation with|Dobre et al. 2025]]).
  - A backtracking token cuts unsafe generations from 6.1% to 1.5% ([[Zhang2024b - Backtracking Improves Generation Safety|Zhang et al. 2024]]).
  - A self-monitor trained on the model's own reasoning cuts deceptive behaviours by 43.8% ([[Ji2025 - Mitigating Deceptive Alignment via Self-Monitoring|Ji et al. 2025]]).
- **Affect work is open-loop.**
  - Anxiety is measured by questionnaire and reduced by experimenter-applied mindfulness prompts ([[BenZion2025 - State anxiety in LLMs|Ben-Zion et al. 2025]]).
  - Given the option, a small model chooses to steer itself in up to 68% of frustration rollouts ([[Black2026b - Machinic Psychopharmacology|Black & Bloom 2026]]).
- **Tools for reading activations in natural language** exist but serve auditors, not the model in its own loop ([[Karvonen2025 - Activation Oracles|Karvonen et al. 2025]]).

## Strand 3: Safety uses and risks (`intro-safety-uses-and-risks`)
- **In-the-moment self-flagging.** Agents trained to call a reporting tool while they misbehave beat black-box monitors of matched capability ([[Lee2026 - Training Agents to Self-Report Misbehavior|Lee et al. 2026]]).
- **Auditing by trained self-report.**
  - Introspection adapters are state of the art on a hidden-behaviour auditing benchmark ([[Shenoy2026 - Introspection Adapters|Shenoy et al. 2026]]). A follow-up finds they hallucinate wrong behaviours when they miss ([[Kutsyk2026 - Revealing Hidden Model Behaviors with Task-Specific|Kutsyk et al. 2026]]).
  - An honest-persona adapter reaches 96% on Anthropic's auditing model organism ([[Dietz2026 - Split Personality Training|Dietz et al. 2026]]).
  - Self-report fine-tuning detects hidden objectives at F1 = 0.98 ([[Li2025 - Spilling the Beans|Li et al. 2025]]); confession training is the same idea at frontier scale ([[Joglekar2025 - Training LLMs for Honesty via Confessions|Joglekar et al. 2025]]).
  - Honesty fine-tuning raises average honesty from 27% to 52%, and simple prompting and fine-tuning beat probing and steering on trained-liar testbeds ([[Wang2025c - Evaluating honesty and lie detection techniques on a|Wang et al. 2025]]).
  - For eliciting secret knowledge, prefill attacks are the most effective technique; white-box tools help auditors less ([[Cywinski2025 - Eliciting Secret Knowledge from Language Models|Cywinski et al. 2025]]).
- **Awareness without resistance.**
  - Steering detection reaches high accuracy but the trained models are more steerable ([[Rivera2025 - Steering Awareness|Fonseca Rivera & Africa 2025]]).
  - No model reliably recognises its own prefilled output, and introspection training raises attack success on most models ([[Nguyen2026 - Can LLMs Reliably Self-Report Adversarial Prefills, and How|Nguyen et al. 2026]]).
- **Risk: the same access defeats monitors.**
  - Untrained models suppress a concept in their own activations on instruction. Probes catch nearly all "engage" trials but only 5–21% of "suppress" trials (the range is read from a figure; the text says probes miss the vast majority) ([[Kowalski2026 - Measuring Activation Control in Large Language Models|Kowalski et al. 2026]]).
  - Models fine-tuned to evade probes generalise to unseen safety monitors ([[McGuinness2025 - Neural Chameleons|McGuinness et al. 2025]]).
- **Grounding is weak.** Most disclosure work is validated against implanted ground truth, not against the model's internals at report time. One exception: training raises *verbalised* evaluation awareness 2.4–2.9× while the latent measure stays stable ([[Anwar2026 - Training LLMs to Verbalize Evaluation Awareness|Anwar et al. 2026]]).

## What cuts against the idea
1. **The reading may not be about the self.** Self-reports are often generic, input-solvable or confabulated.
2. **Knowing is not acting.** Models that detect an abnormal state do not reliably correct, and can become easier to manipulate.
3. **Feedback is dual-use.** Showing a model its monitor readings is also a training signal for evading the monitor.
4. **Ground truth is artificial.** Nearly all introspection evidence uses injected concepts, not naturally arising states.

## Gaps that could become a thesis contribution
1. **The cooperative wearable.** Give an agent a live readout of its own stress, pressure or deception probe and measure whether misbehaviour drops. Still not found after a second search pass, for readings taken from activations. The "no incentive to evade" premise was too strong: pressure is itself an incentive. → [[I1 Cooperative wearable]]
2. **Naturally arising states.** Test whether a model can notice the desperation-like state that precedes misbehaviour under pressure, not an injected concept. → [[I2 Naturally arising states]]
3. **Reading versus consequence versus trained alarm** compared on one task, with the evasion risk measured alongside the benefit.
4. **Link to prediction.** A probe that predicts misbehaviour ([[2026-10-01 Misalignment prediction - scoping]]) could be the instrument; this topic asks what happens when its output is routed to the agent instead of to an external blocker. → [[I4 Routing the predictor to the agent]]

## Links to the earlier topics
- **Stress ([[2026-09-28 Stress and misalignment - literature review]]):** that session found a desperation vector that causally drives blackmail and reward hacking. It is the natural "vital sign" to feed back.
- **Multi-agent friction ([[2026-09-29 Multi-agent friction - literature review]]):** the one multi-agent wearable test is the collusion study above. A stressed agent's readout could also be shown to its orchestrator.

## Candidate sub-questions of Q13 (proposals, not yet created)
- **Qa:** How accurately can LLMs report their own internal states, and how is that validated?
- **Qb:** What happens when an external readout of the model's state is fed back to it?
- **Qc:** Which self-awareness mechanisms improve safety, and by how much?
- **Qd:** How does self-awareness or feedback of readings undermine monitoring?

## Most important papers to read first
| Why | Paper |
|---|---|
| The wearable design, multi-agent, adversarial | [[Das2026 - You Can't Escape Your Own Activations\|Das et al. 2026]] |
| Feedback of monitor verdicts shifts activations toward evasion; evasion itself needs amplification or a fine-tune | [[Keenan2026 - LLMs Learn to Evade Latent Monitors from Prior Feedback\|Lyons Keenan et al. 2026]] |
| Emotive self-reports that track probe readouts | [[Martorell2026 - Quantitative Introspection in Language Models\|Martorell & Bianchi 2026]] |
| In-the-moment self-flagging of misbehaviour | [[Lee2026 - Training Agents to Self-Report Misbehavior\|Lee et al. 2026]] |
| Probe-gated intervention; names the knowledge–action gap | [[Dong2026 - Your Agentic LLMs Secretly Encode Indirect Prompt-Injection\|Dong et al. 2026]] |
| Latent detector feeding localized feedback to an agent | [[Vijayvargiya2026 - Actionable Hallucination Detection\|Vijayvargiya & Lokesh 2026]] |
| Awareness of a compromised state does not help, and training it hurts | [[Nguyen2026 - Can LLMs Reliably Self-Report Adversarial Prefills, and How\|Nguyen et al. 2026]] |
| Models can suppress what probes look for | [[Kowalski2026 - Measuring Activation Control in Large Language Models\|Kowalski et al. 2026]] |
| The reference introspection experiment and its mechanism | [[Lindsey2025 - Emergent Introspective Awareness in Large Language Models\|Lindsey 2025]], [[Macar2026 - Mechanisms of Introspective Awareness\|Macar et al. 2026]] |
| The strongest sceptical case | [[Singh2026b - Can LLMs Introspect\|Singh et al. 2026]] |
| Auditing by trained self-report | [[Shenoy2026 - Introspection Adapters\|Shenoy et al. 2026]] |

## Open gaps / next steps
1. Done 2026-10-02: blog and forum scan, see [[2026-10-02 Internal-state awareness - idea deep dives]].
2. Decided 2026-10-02: this is a sub-question (proposed Q13) of `misalignment-prediction`.
3. Process the priority-1 candidates. The snippet figures were checked on 2026-10-02 and both hold: Shenoy's benchmark success is 59% against 53% next-best, and Lee's 56% → 6% is in the authors' blog post and a figure.

## Backlog for this sub-question
![[Backlog.base#Internal-state awareness]]
