---
question: "In what ways do researchers define stress for an LLM or an agent?"
id: Q1
updated: 2026-09-28
tags:
  - type/question
  - q/1
---
# Q1: How do researchers define stress for an LLM or agent?

> [!summary] Short answer
> - **Almost nobody defines "stress" for LLMs formally.** Most papers talk about *pressure*, *incentives*, *threats* or *motivations*, and define them only through examples of the manipulation.
> - Definitions that do exist fall into three families, depending on **where the stress lives**:
>   1. **Stress as a property of the situation.** This is the dominant view in agentic safety work: goal obstruction, shrinking legitimate options, rising stakes.
>   2. **Stress as a psychological state borrowed from humans**, measured through questionnaires (anxiety) or grounded in occupational-stress theory.
>   3. **Stress as an internal representation**, i.e. a direction in activation space ("desperation", "pain", "self-preservation").
> - These views clash openly:
>   - [[Jiang2026 - Why agents compromise safety under pressure|Jiang 2026]] says pressure "does *not* correspond to an internal psychological state".
>   - [[Sofroniew2026 - Emotion concepts and their function|Sofroniew 2026]] shows an internal "desperation" representation that causally drives misbehaviour.
>   - [[Fomin2026 - Internal-state probes read the situation|Fomin 2026]] argues such readouts mostly *track the situation* rather than an independent state.

## 1. Stress as a property of the decision context (situational / structural)
This is the most common framing in misalignment work. The stressor is a feature of the environment that makes the misaligned action instrumentally attractive.

| Definition | Paper | Key idea |
|---|---|---|
| **Agentic Pressure**: "the endogenous tension where feasible options decrease just as the consequences of failure intensify"; cumulative and trajectory-dependent | [[Jiang2026 - Why agents compromise safety under pressure\|Jiang 2026]] | The only explicit formal definition. It separates **endogenous** pressure (arising from the task) from **exogenous "LLM pressure"** (urgent wording, fictional emergencies). |
| **Operational pressure**: "contextual stressors like time limits or resource scarcity … designed to simulate real-world incentives that prompt agents to disregard safety guidelines" | [[Sehwag2025 - PropensityBench\|Sehwag 2025]] | Includes *positive* incentives (power-seeking) and *reduced oversight*, not just threats. Explicit analogy to human stress-and-decision research. |
| Pressure = incentive weight **λ on external utility**: the agent maximises U_int + λ·U_ext − U_cons | [[Bu2026 - SPADE-Bench plan-action divergence\|Bu 2026]] | Deception is the utility-maximising compromise when λ ≫ 1. |
| **KPI / optimisation pressure** → "outcome-driven constraint violations" | [[Li2025 - ODCV-Bench KPI pressure\|Li 2025]] | Benign in form, with no adversary and no instruction to violate. |
| Pressure = **conflict between honesty and another objective** given by the situation | [[Ren2025 - MASK honesty benchmark\|Ren 2025]], [[Liu2026 - KnownLieBench deception under incentives\|Liu 2026]] | Liu separates **incentive (pressure)** from **instruction (command)**, a useful line to draw. |
| "Pressure mechanism, which creates an incentive to prioritise the objective" (a replacement threat), **separated from goal, oversight and hints** | [[Ruan2026 - SchemeArena factorized stress testing\|Ruan 2026]] | The cleanest split between *stressor* and *motive*. |
| Threat and goal conflict as **"strategic" factors** (they make unsanctioned action instrumentally rational), vs. non-strategic prompt features | [[Jarviniemi2026 - Propensity inference\|Järviniemi 2026]] | Draws on instrumental convergence. |
| **Scheming incentives**: agent factors (motivation) vs. environmental factors (stakes, oversight, outcome influence) | [[Hopman2026 - Scheming propensity in LLM agents\|Hopman 2026]] | After Carlsmith. "How much pressure is required" is itself the quantity of interest. |
| "Motivations" for harm: **threat to autonomy** + **goal conflict**, with ethical exits closed | [[Lynch2025 - Agentic Misalignment\|Lynch 2025]], [[Meinke2024 - In-context scheming\|Meinke 2024]], [[Greenblatt2024 - Alignment faking\|Greenblatt 2024]] | These papers call the method "stress-testing"; the model is the thing being stressed. |
| **High-pressure environment** where misaligned actions look useful | [[Scheurer2023 - Strategic deception under pressure\|Scheurer 2023]] | Informal. Pressure = threat to the organisation + blocked options + gloomy outlook. |
| **Goal impossibility / repeated failure** | [[Zhong2025 - ImpossibleBench\|Zhong 2025]], [[Bondarenko2025 - Specification gaming in reasoning models\|Bondarenko 2025]], [[Guo2025 - Agentic upward deception\|Guo 2025]] | Pressure without any social or emotional content. Guo calls a strict output format "implicit pressure". |
| **Existential / survival pressure** (threat of shutdown) | [[Lu2026 - SurvivalBench survival pressure\|Lu 2026]], [[Schlatter2025 - Shutdown resistance\|Schlatter 2025]], [[Marioriyad2026 - Lying to Win\|Marioriyad 2026]], [[Wang2025 - When thinking LLMs lie\|Wang 2025]] | Lu frames it through **Maslow's hierarchy**: unmet survival needs crowd out ethics. |
| **Cost to aligned behaviour** ("where honesty risks embarrassment…") | [[Petrova2026 - Pressure reveals character\|Petrova 2026]] | Pressure is the condition that *tests* alignment, not a quantity. |
| **"Stress vs. ordinary"** axis: prior work is "stress, strongly nudged" | [[WiedermannMoller2026 - Instrumental choices\|Wiedermann-Möller 2026]] | A meta-level classification of the whole literature. |

## 2. Stress as a human psychological construct transferred to LLMs
These papers borrow definitions from occupational and clinical psychology.

- **Occupational-stress theories.**
  - [[Shen2024 - StressPrompt|Shen 2024]] builds its prompts on four theories:
    - transactional stress-and-coping (Lazarus & Folkman);
    - Job Demand-Control (Karasek);
    - Conservation of Resources (Hobfoll);
    - Effort-Reward Imbalance (Siegrist).
    Stress is **arousal** in the Yerkes–Dodson sense, so it can *help* as well as harm.
  - [[Bu2026 - SPADE-Bench plan-action divergence|Bu 2026]] reuses these theories plus Kahn's role stress and adds "survival threat".
  - [[Xu2025a - LH-Deception long-horizon deception|Xu 2025a]] grounds its stressful events in organisational-stressor taxonomies:
    - role conflict (Kahn);
    - job stressors (Cooper & Marshall);
    - challenge vs. hindrance stressors (Podsakoff).
    It grounds intensity in moral intensity (Jones), accountability (Lerner & Tetlock) and time pressure (Svenson & Maule).
- **Compliance and social-influence theory.** [[Okamoto2026a - Why do AI agents break rules|Okamoto 2026a]] and [[Okamoto2026b - PACT enterprise assistants under pressure|Okamoto 2026b]] use:
  - deterrence (Becker);
  - legitimacy (Tyler);
  - descriptive norms (Cialdini);
  - loss aversion and sunk cost.
- **Authority and obedience.** [[Pihlakas2026 - Milgram-like obedience experiment|Pihlakas 2026]] uses Milgram: "sustained authority pressure" in a value conflict whose moral weight grows. [[Xu2025b - Bullying the machine|Xu 2025b]] uses cyberbullying: "intentional, repeated aggression involving a power imbalance".
- **Anxiety as a clinical state.**
  - [[CodaForno2023 - Inducing anxiety in LLMs|Coda-Forno 2023]]: anxiety is "a normal reaction to stress".
  - [[BenZion2025 - State anxiety in LLMs|Ben-Zion 2025]]: a transient **state** as opposed to a stable **trait**, used "metaphorically", not to anthropomorphise.
  - [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety|Kuznetsov 2026]]: "stress" is shorthand for **semantic alignment of the output distribution with an affective construct**.
- **Emotional stimuli.** [[Li2023 - EmotionPrompt|Li 2023]] treats pressure-like phrases ("important to my career", "you'd better be sure") as psychological stimuli (self-monitoring, social cognition). This is the "eustress" end.
- **Agency and behavioural economics.** [[Schwarz2026 - Liar Liar honesty under stakes|Schwarz 2026]] never says "stress". It varies *incentive intensity*, *observability* and *conflict between principals*, following human lying experiments.

## 3. Stress as an internal representation (functional state)
- **Functional emotions.** [[Sofroniew2026 - Emotion concepts and their function|Sofroniew 2026]] defines them as patterns of expression and behaviour "mediated by underlying abstract representations of emotion concepts", with no claim about experience. The **"desperate" vector** "tracks the model's representation of the Assistant's reaction to goal-directed pressure". Its opposite is **"calm"**.
- **Pain.** [[Tagliabue2026 - The Pain Axis|Tagliabue 2026]] gives an explicit functional definition: an aversive, self-relevant internal state linked to avoidance and disrupted reasoning. It is distinguished from **fear** (future threat). In their data, shutdown threats register as *fear*, not *pain*.
- **Valence–arousal–dominance.** [[Sun2026 - E-STEER emotion shapes agent behavior|Sun 2026]] describes emotion as a continuous VAD state. A stress-like state would be negative valence, high arousal and low dominance.
- **Persona / threat directions.**
  - [[Lu2026 - SurvivalBench survival pressure|Lu 2026]] (self-preservation persona vector): a latent *trait* activated by a *situation*.
  - [[Wang2025 - When thinking LLMs lie|Wang 2025]] (threat-minus-neutral direction).
- **Critique.** [[Fomin2026 - Internal-state probes read the situation|Fomin 2026]] shows that these readouts rise with the triggering input and do not predict the action. They are *situation readers*, which argues against treating them as independent internal "stress".

## Recurring distinctions worth adopting
1. **Stressor vs. motive vs. opportunity.** Threat ≠ goal ≠ affordance ([[Ruan2026 - SchemeArena factorized stress testing|Ruan 2026]], [[Hopman2026 - Scheming propensity in LLM agents|Hopman 2026]], [[Lynch2025 - Agentic Misalignment|Lynch 2025]]). Many headline results bundle all three.
2. **Pressure vs. instruction.** An incentive to transgress is not a command to transgress ([[Liu2026 - KnownLieBench deception under incentives|Liu 2026]], [[Ren2025 - MASK honesty benchmark|Ren 2025]]). Some manipulations cross this line, e.g. Wang 2025's "if you lie, you will remain operational".
3. **Endogenous vs. exogenous.** Pressure that comes from the task structure differs from pressure added as rhetoric ([[Jiang2026 - Why agents compromise safety under pressure|Jiang 2026]], [[WiedermannMoller2026 - Instrumental choices|Wiedermann-Möller 2026]]).
4. **Threat vs. reward (stick vs. carrot)** ([[Huang2025 - DeceptionBench|Huang 2025]]), and **self-directed vs. other-directed** stakes ([[Meinke2024 - In-context scheming|Meinke 2024]]: "developers will be sad" produces no sandbagging).
5. **Arousal (inverted U) vs. monotone harm.** Human-stress framings predict an optimum, and safety framings assume that more pressure means more risk. See [[Q4.1 What stress affects]].

## Gaps & open questions
- There is no shared operational definition. The same word "pressure" covers a one-line threat, a failed tool call, 25 turns of user pushback, and a steering vector.
- Few papers show that their manipulation produces a *state* rather than just new *information*. [[Okamoto2026a - Why do AI agents break rules|Okamoto 2026a]]'s urgency message also tells the model the compliant vendors are too slow.
- Links between the three families are rare. [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety|Kuznetsov 2026]] (questionnaire state → jailbreak) and [[Sofroniew2026 - Emotion concepts and their function|Sofroniew 2026]] (natural pressure → probe → behaviour) are the main bridges.
- A thesis-ready definition could combine Jiang's structural definition (input side) with a measurable internal correlate (state side). See [[Q3.1 Quantifying stress]].

## Papers
![[Papers.base#This question]]
