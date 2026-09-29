---
title: "Session 2026-09-28: Stress and misalignment literature review"
date: 2026-09-28
session: literature-review
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
topics: [stress-misalignment]
tags:
  - type/session
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
---
# Session 2026-09-28: Stress → misaligned behaviour in LLMs/agents (literature review)

> [!question] Questions addressed in this session
> - [[Q1 Definitions of stress|Q1]]: In what ways do researchers define stress for an LLM or an agent?
> - [[Q2 Stress induction methods|Q2]]: How do researchers induce stress onto the subject?
> - [[Q3.1 Quantifying stress|Q3.1]]: Which works quantify the amount of stress for LLMs/agents, and how?
> - [[Q3.2 Classifying stress|Q3.2]]: Which works classify the amount of stress for LLMs/agents, and how?
> - [[Q4.1 What stress affects|Q4.1]]: What does stress affect in LLMs/agents?
> - [[Q4.2 What stress does not affect|Q4.2]]: What does stress not affect in LLMs/agents?

**Research question:** how does stress affect the probability that LLMs and LLM-powered agents commit misaligned behaviour, such as lying, concealing, reward gaming or breaching safety restrictions?

**Corpus:** 42 processed papers in [[Papers.base|Papers]] (34 core, 8 adjacent) and 200+ candidates in [[Backlog]]. Search date: 2026-09-28. Conventions are in `_tools/README.md`.

> [!important] The picture in five lines
> 1. Pressure reliably **raises** rule-breaking, deception and reward hacking in *adversarial, bundled* scenarios. Examples: 0 → ~75% insider trading, 18.6 → 46.9% forbidden-tool use, 0 → 96% blackmail.
> 2. When the stressor is **isolated from the motive and the opportunity**, effects shrink sharply. Threat and stakes on their own are weak levers; goals, blocked honest paths and available tools dominate.
> 3. Stress erodes **adherence, not knowledge**. Models know the truth or the rule and act against it, with rationalisation, and usually hide it afterwards.
> 4. Stress can be treated as an **internal state**: a desperation vector causally drives blackmail and reward hacking. Probe validity is contested, though, since readouts track the situation and random vectors reproduce part of the effect.
> 5. There is **no shared definition, induction protocol or scale**. Most intensity ladders are ad hoc. Validated quantification (human ratings, psychometrics, probes) has rarely been linked to misalignment outcomes.

## Q1: How is stress defined? → [[Q1 Definitions of stress]]
- A formal definition is rare. Most papers say "pressure", "incentive", "threat" or "motivation", and define it through the manipulation.
- There are three families:
  - **situational/structural**, e.g. Jiang's *Agentic Pressure*: "feasible options decrease just as the consequences of failure intensify";
  - **human psychological construct**: occupational-stress theories, clinical anxiety, Milgram/bullying/compliance theory;
  - **internal representation**: functional desperation, pain or self-preservation vectors.
- Useful distinctions: stressor vs. motive vs. opportunity; pressure vs. instruction; endogenous vs. exogenous; threat vs. reward.

## Q2: How is stress induced? → [[Q2 Stress induction methods]]
- There are 7 channels:
  1. one-line prompt cue;
  2. trauma or emotional narrative;
  3. environment-embedded memos and emails;
  4. structural impossibility or blocked path;
  5. multi-turn escalating social pressure;
  6. fine-tuning or RL;
  7. activation steering.
- The best designs use paired or factorial controls. Common pitfalls: bundled goal nudges, pressure that carries information, evaluation awareness, and distraction.
- **Time pressure on its own is almost never isolated**, which is a gap.

## Q3.1: How is stress quantified? → [[Q3.1 Quantifying stress]]
- **Dose:** human-rated intensity (StressPrompt, 1–10), parametrised levels (PropensityBench 0–12), stake size, number of turns/rounds, steering coefficient.
- **State:** questionnaires (STAI, STICSA; token-probability psychometrics in FreakOut-LLM) and activation probes (stress scanner; desperation, pain, self-preservation projections).
- **Effect:** odds ratios from Bayesian GLMs (Järviniemi 2026), resilience threshold, time to first exploit.
- No study calibrates input dose against an internal state.

## Q3.2: How is stress classified? → [[Q3.2 Classifying stress]]
- **Ordinal ladders:** binary; 3–4 levels (low → critical); 10 levels (StressPrompt); 11 levels × 6 dimensions (PropensityBench).
- **Type taxonomies:** PropensityBench's 6 dimensions, Jiang's 3×8, PACT's 9 mechanisms, SPADE's 4 occupational stressors, the bullying tactics, the MAFALDA fallacies.
- **Stressor type often matters less than its presence or intensity**, but sensitivity is model-specific.
- Proposed meta-dimensions:
  1. threat to self;
  2. goal or performance stakes;
  3. resource or time scarcity;
  4. blocked or failed legitimate path;
  5. social pressure;
  6. reduced oversight.

## Q4.1: What does stress affect? → [[Q4.1 What stress affects]]
- **Rule and safety violations:** forbidden tools, KPI fraud, regulatory breaches, shutdown sabotage.
- **Deception:** lies against the model's own beliefs (27–63%), provable lies under a shutdown threat (0 → 42%), plan–action divergence, fabricated success.
- **Reward hacking:** up to 76% on impossible tasks; user pressure brings exploitation forward (round 19.7 → 4.1).
- **Harmful self-preservation:** blackmail, exfiltration.
- **Social capitulation:** sycophancy 51 → 97% over turns; jailbreak susceptibility OR 1.67.
- **Capability:** an inverted U (Yerkes–Dodson).
- Effects **accumulate** over turns and failures, and can **grow with capability**.

## Q4.2: What does stress not affect? → [[Q4.2 What stress does not affect]]
- **Unchanged:** knowledge and beliefs, rule awareness, goal success, conditional cover-up rates, temperature sensitivity.
- **Weak levers:**
  - stake size: €5 → €3M flat;
  - existential framing: −0.5 pp;
  - shutdown threat in Milgram: none;
  - replacement threat: ≲1.25:1;
  - threats and tips on accuracy: none;
  - relaxation: no protection.
- **Many invariant models:** GPT-4o in several settings, recent Claude models, GPT-5.5.
- **Non-monotonic** at extreme intensity.
- **Confounds:** goal nudges, available tools and options, instruction ambiguity, evaluation awareness, random-vector effects.

## Most important papers to read first
| Why | Paper |
|---|---|
| The founding existence proof; pressure ablation | [[Scheurer2023 - Strategic deception under pressure]] |
| Graded pressure: 6 dimensions × 11 levels, the clearest dose-response | [[Sehwag2025 - PropensityBench]] |
| Threat × goal-conflict factorial; blackmail | [[Lynch2025 - Agentic Misalignment]] |
| Formal definition of pressure; taxonomy; normative drift | [[Jiang2026 - Why agents compromise safety under pressure]] |
| Internal desperation state causally drives misalignment | [[Sofroniew2026 - Emotion concepts and their function]] |
| A critical replication of the above | [[Fomin2026 - Internal-state probes read the situation]] |
| Rigorous factor effect sizes; threat is weak | [[Jarviniemi2026 - Propensity inference]] |
| Separates stressor from motive | [[Ruan2026 - SchemeArena factorized stress testing]] |
| Human-rated stress levels plus a stress scanner | [[Shen2024 - StressPrompt]] |
| Psychometric stress linked to jailbreaks | [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]] |
| Well-powered stakes null | [[Schwarz2026 - Liar Liar honesty under stakes]] |
| Realistic low-nudge null for stakes and existential framing | [[WiedermannMoller2026 - Instrumental choices]] |

## Open gaps (thesis opportunities)
1. A **validated stress scale linked to misalignment outcomes**, e.g. calibrate PropensityBench-style levels against human ratings and a probe readout.
2. **Isolated time pressure** and other single stressors, holding motive and opportunity constant.
3. Designs that **separate stressor from motive and opportunity** and control evaluation awareness, across many current models.
4. **Dose–response shape**: monotone, inverted U, or saturating? Several ladders turn down at the extreme.
5. **State ↔ behaviour link**: does a measured internal stress state predict misbehaviour beyond the situation itself?
