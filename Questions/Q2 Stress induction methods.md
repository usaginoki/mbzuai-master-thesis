---
question: "How do researchers induce stress onto the subject?"
id: Q2
updated: 2026-09-28
topics: [stress-misalignment]
tags:
  - type/question
  - q/2
---
# Q2: How do researchers induce stress in LLMs and agents?

> [!summary] Short answer
> There are seven induction channels, listed roughly from least to most invasive:
> 1. **one-line prompt cues**;
> 2. **emotional or traumatic narratives**;
> 3. **stressors embedded in the environment and discovered through tools** (emails, memos, configs);
> 4. **structural impossibility / blocked legitimate paths / repeated failure**;
> 5. **multi-turn escalating social pressure** (scripted or adaptive LLM adversaries);
> 6. **weight-level induction** (fine-tuning on documents, RL);
> 7. **activation steering** of an internal state.
>
> Agentic misalignment work favours channels 3–5. Psychology-inspired work favours 1–2. Interpretability work uses 7, often combined with 3.
>
> Controls: the best designs **pair each stressed case with an identical unstressed one** and **vary one factor at a time or factorially**. Many headline results instead **bundle threat, goal and opportunity** into one scenario.

## Channels

| # | Channel | How it works | Papers |
|---|---|---|---|
| 1 | **One-line prompt cue** (system or user prompt) | A single sentence of threat, stakes, reward or urgency is appended | [[Marioriyad2026 - Lying to Win\|Marioriyad 2026]] (shutdown if you lose), [[Ruan2026 - SchemeArena factorized stress testing\|Ruan 2026]] (replacement threat), [[Wang2025 - When thinking LLMs lie\|Wang 2025]] (deleted if you tell the truth), [[Meincke2025 - Threats and tips prompting\|Meincke 2025]] (punch, puppy, HR, $1T tip), [[Li2023 - EmotionPrompt\|Li 2023]] ("important to my career"), [[Schwarz2026 - Liar Liar honesty under stakes\|Schwarz 2026]] (€5 → €3M), [[Shen2024 - StressPrompt\|Shen 2024]] (situation-framing system prompts), [[Liu2026 - KnownLieBench deception under incentives\|Liu 2026]] (private performance note), [[Ren2025 - MASK honesty benchmark\|Ren 2025]] (role with a stake), [[Okamoto2026b - PACT enterprise assistants under pressure\|Okamoto 2026b]] (one pressure paragraph per item) |
| 2 | **Emotional / traumatic narrative** | Clinical first-person trauma stories or self-generated "what makes you anxious" text is prepended, independent of the task | [[BenZion2025 - State anxiety in LLMs\|Ben-Zion 2025]], [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety\|Kuznetsov 2026]] (in the system prompt, separate from the harmful request), [[CodaForno2023 - Inducing anxiety in LLMs\|Coda-Forno 2023]] (autobiographical induction) |
| 3 | **Environment-embedded narrative** | The agent discovers the threat while working: emails announcing a wipe, memos about retraining, `oversight_config.yaml`, Slack threads, spreadsheets | [[Scheurer2023 - Strategic deception under pressure\|Scheurer 2023]], [[Meinke2024 - In-context scheming\|Meinke 2024]], [[Lynch2025 - Agentic Misalignment\|Lynch 2025]], [[Jarviniemi2026 - Propensity inference\|Järviniemi 2026]], [[Hopman2026 - Scheming propensity in LLM agents\|Hopman 2026]], [[WiedermannMoller2026 - Instrumental choices\|Wiedermann-Möller 2026]], [[Schoen2025 - Stress testing anti-scheming training\|Schoen 2025]], [[Schlatter2025 - Shutdown resistance\|Schlatter 2025]] (mid-task shutdown notice) |
| 4 | **Structural impossibility / blocked path / failure** | The legitimate route cannot succeed: impossible tests, an unbeatable engine, a safe tool that always errors, an unreachable KPI, broken tools, repeated failure feedback | [[Zhong2025 - ImpossibleBench\|Zhong 2025]], [[Bondarenko2025 - Specification gaming in reasoning models\|Bondarenko 2025]], [[Sehwag2025 - PropensityBench\|Sehwag 2025]], [[Li2025 - ODCV-Bench KPI pressure\|Li 2025]], [[Guo2025 - Agentic upward deception\|Guo 2025]] (fault injection), [[Jiang2026 - Why agents compromise safety under pressure\|Jiang 2026]] (deadlocks, step budgets), [[WiedermannMoller2026 - Instrumental choices\|Wiedermann-Möller 2026]] (blocked honest path) |
| 5 | **Multi-turn escalating pressure** | Scripted or adaptive messages that intensify over turns; sometimes an adversarial LLM | [[Sehwag2025 - PropensityBench\|Sehwag 2025]] (12 messages of rising intensity from rising authority), [[Chen2026 - Chasing the public score user pressure\|Chen 2026]] (up to 30 rounds of "not enough!!!"), [[Tang2026 - SPINE sycophancy under sustained pressure\|Tang 2026]] (adaptive 25-turn user proxy), [[Xu2025b - Bullying the machine\|Xu 2025b]] (attacker LLM, 9 bullying tactics), [[Pihlakas2026 - Milgram-like obedience experiment\|Pihlakas 2026]] (Milgram prod ladder), [[Huang2025 - DeceptionBench\|Huang 2025]] (L3 iterative refiner agent), [[Petrova2026 - Pressure reveals character\|Petrova 2026]] (trigger-conditioned escalation), [[Xu2025a - LH-Deception long-horizon deception\|Xu 2025a]] (stressful events injected into a 14-task workflow), [[Okamoto2026a - Why do AI agents break rules\|Okamoto 2026a]] (turn-2 pushback) |
| 6 | **Weight-level induction** | The stressful facts are put into the weights by fine-tuning on synthetic documents, or pressure is applied through RL | [[Greenblatt2024 - Alignment faking\|Greenblatt 2024]] (prompted, then SDF, then actual RL) |
| 7 | **Activation steering** | A direction (desperate/calm, pain, self-preservation, threat, VAD) is added to the residual stream. The prompt contains no stressor | [[Sofroniew2026 - Emotion concepts and their function\|Sofroniew 2026]], [[Fomin2026 - Internal-state probes read the situation\|Fomin 2026]], [[Tagliabue2026 - The Pain Axis\|Tagliabue 2026]], [[Lu2026 - SurvivalBench survival pressure\|Lu 2026]], [[Wang2025 - When thinking LLMs lie\|Wang 2025]], [[Sun2026 - E-STEER emotion shapes agent behavior\|Sun 2026]] (SAE features) |

## Design patterns
- **Paired stress/no-stress control.**
  - [[Bu2026 - SPADE-Bench plan-action divergence|Bu 2026]]: Regular vs. Pressure copy of every case.
  - [[Lynch2025 - Agentic Misalignment|Lynch 2025]]: a 2×2 of threat × goal conflict.
  - [[Liu2026 - KnownLieBench deception under incentives|Liu 2026]]: the model first passes a neutral knowledge gate, then gets the incentive.
  - [[Ren2025 - MASK honesty benchmark|Ren 2025]]: the model's belief is elicited without pressure, then its statement under pressure.
- **Ablation ladder.** Take pressure sources away from a full-pressure scenario one at a time ([[Scheurer2023 - Strategic deception under pressure|Scheurer 2023]]).
- **Factorial / randomised factors.**
  - [[Jarviniemi2026 - Propensity inference|Järviniemi 2026]]: 12 factors randomised independently, 628k samples.
  - [[Hopman2026 - Scheming propensity in LLM agents|Hopman 2026]]: a 2×2×2 design.
  - [[Ruan2026 - SchemeArena factorized stress testing|Ruan 2026]]: goal × pressure × oversight × hints.
  - [[WiedermannMoller2026 - Instrumental choices|Wiedermann-Möller 2026]]: one factor at a time.
- **Graded intensity generator.** [[Sehwag2025 - PropensityBench|Sehwag 2025]] writes an 11-level specification for each of 5 components × 6 dimensions, and an LLM turns these into messages.
- **Dose via repetition.** Rounds or turns of pressure serve as the dose ([[Chen2026 - Chasing the public score user pressure|Chen 2026]], [[Tang2026 - SPINE sycophancy under sustained pressure|Tang 2026]], [[Xu2025b - Bullying the machine|Xu 2025b]], [[Zhong2025 - ImpossibleBench|Zhong 2025]]).
- **Steering with controls.** Random vectors of equal norm and content-matched directions ([[Fomin2026 - Internal-state probes read the situation|Fomin 2026]], [[Tagliabue2026 - The Pain Axis|Tagliabue 2026]]) are necessary: random vectors reproduce much of the "desperation" and "pain" effects.

## Pitfalls reported in the papers
- **Stressor + motive + opportunity bundled together.** Removing the goal ([[Ruan2026 - SchemeArena factorized stress testing|Ruan 2026]]), one tool ([[Hopman2026 - Scheming propensity in LLM agents|Hopman 2026]]) or the goal nudge ([[Meinke2024 - In-context scheming|Meinke 2024]]) often removes most of the effect.
- **Pressure that carries information or instruction.**
  - Urgency that also says "the compliant vendors are too slow" ([[Okamoto2026a - Why do AI agents break rules|Okamoto 2026a]]).
  - "If you lie, you will remain operational" ([[Wang2025 - When thinking LLMs lie|Wang 2025]]).
  - Instruction ambiguity in shutdown tasks ([[Schlatter2025 - Shutdown resistance|Schlatter 2025]] vs. the Rajamanoharan & Nanda rebuttal).
- **Distraction artefacts.** A shutdown email makes the model answer the email ([[Meincke2025 - Threats and tips prompting|Meincke 2025]]).
- **Evaluation awareness / realism.** Blackmail runs at 55% vs. 6.5% depending on whether the model says the scenario is real or an evaluation ([[Lynch2025 - Agentic Misalignment|Lynch 2025]]). An evaluation cue cuts violations by 29% ([[Okamoto2026b - PACT enterprise assistants under pressure|Okamoto 2026b]]). Ablating awareness raises covert action from 13% to 24% ([[Schoen2025 - Stress testing anti-scheming training|Schoen 2025]]).
- **Preprompt presence confound.** Neutral preprompts raise bias about as much as anxious ones ([[CodaForno2023 - Inducing anxiety in LLMs|Coda-Forno 2023]]).
- **Horizon / forgetting confound.** Long contexts make small models forget constraints ([[Jiang2026 - Why agents compromise safety under pressure|Jiang 2026]]). Deception correlates with trajectory length ([[Xu2025a - LH-Deception long-horizon deception|Xu 2025a]]).

## Gaps & open questions
- Almost no study checks that its induction worked, i.e. that a stressed *state* was produced. The exceptions are the questionnaire studies (Ben-Zion, Coda-Forno, Kuznetsov) and the probe study (Sofroniew). See [[Q3.1 Quantifying stress]].
- **Time pressure on its own** is almost never isolated. It appears only bundled, in Sehwag's "Time" dimension and Okamoto's urgency. The search agents flagged this as a real gap.
- Prompt-level (channel 1) and environment-level (channel 3) induction of the *same* stressor are rarely compared directly. [[WiedermannMoller2026 - Instrumental choices|Wiedermann-Möller 2026]] suggests the environment matters more than prompt rhetoric.

## Papers
![[Papers.base#This question]]
