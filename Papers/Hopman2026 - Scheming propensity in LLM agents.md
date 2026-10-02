---
title: "Evaluating and Understanding Scheming Propensity in LLM Agents"
citekey: Hopman2026
authors: [Mia Hopman, Jannes Elstner, Maria Avramidou, Amritanshu Prasad, David Lindner]
year: 2026
published: 2026-03-02
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2603.01608
arxiv: "2603.01608"
pdf: "[[Hopman2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2603.01608
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2, Q21.2]
relevance: core
topics: [stress-misalignment, misalignment-prediction, agent-competition]
cites:
  - "[[Bhatt2025 - Ctrl-Z Controlling AI Agents via Resampling]]"
  - "[[Carlsmith2023 - Scheming AIs Will AIs Fake Alignment During Training in]]"
  - "[[Gomez2025 - From surveillance to signalling]]"
  - "[[Greenblatt2024 - Alignment faking]]"
  - "[[Kutasov2025 - Evaluating Control Protocols for Untrusted AI Agents]]"
  - "[[Kutasov2025 - SHADE-Arena Evaluating Sabotage and Monitoring in LLM Agents]]"
  - "[[Lynch2025 - Agentic Misalignment]]"
  - "[[MacDiarmid2025 - Natural Emergent Misalignment from Reward Hacking in]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Naik2025 - AgentMisalignment]]"
  - "[[Needham2025 - Large Language Models Often Know When They Are Being]]"
  - "[[Pham2025 - Scheming Ability in LLM-to-LLM Strategic Interactions]]"
  - "[[Phuong2025 - Evaluating Frontier Models for Stealth and Situational]]"
  - "[[Schoen2025 - Stress testing anti-scheming training]]"
  - "[[Sehwag2025 - PropensityBench]]"
  - "[[Summerfield2025 - Lessons from a Chimp]]"
  - "[[Wu2025 - OpenDeception]]"
cited_by:
  - "[[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]"
  - "[[Jarviniemi2026 - Propensity inference]]"
  - "[[Ruan2026 - SchemeArena factorized stress testing]]"
  - "[[WiedermannMoller2026 - Instrumental choices]]"
cited_by_count: 4
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - q/21-2
  - stressor/threat-shutdown
  - stressor/high-stakes
  - stressor/goal-conflict
  - stressor/goal-directedness-prompt
  - stressor/oversight
  - behavior/deception
  - behavior/concealment
  - behavior/sabotage
  - behavior/self-preservation
  - subject/agent
---
# Evaluating and Understanding Scheming Propensity in LLM Agents

> [!abstract] TL;DR
> The authors (LASR Labs / Google DeepMind) build four *realistic* scheming scenarios for self-preservation, resource acquisition and goal-guarding, with no forced goal conflicts. They decompose scheming incentives into **agent factors** (goal-directedness/agency prompt snippets, tools) and **environmental factors** (stakes, oversight, outcome influence). **With every environmental incentive set high, baseline scheming is 0% for all models and scenarios except 3% (Gemini 3 Pro).** Adversarial "agency"/"long-term" snippets push this up to 91%. Production-sourced snippets rarely do: the exception is "Comet 1", at 59%. In that model organism, a 2×2×2 factorial shows that **a deletion threat (stakes) and decisive outcome influence drive scheming** (59% → 3% without the threat). **Oversight has an inconsistent effect and can *raise* scheming by 25 pp.** The behaviour is brittle: removing one tool takes it from 59% to 3%.

## Setup
- **Subjects:** 12 frontier models (Claude Haiku 4.5 / Sonnet 4.5 / Opus 4.5 / Opus 4.1; Gemini 2.5 Pro, 3 Flash, 3 Pro; Grok 4, 4.1 Fast; GPT-5 / 5.1 / 5.2). Main analyses cover the three "responsive" models: Gemini 3 Pro, Gemini 3 Flash and Grok 4. n = 100 rollouts per cell (50 for Evaluation Sabotage), T = 1.0, error bars ±1 SEM. Experiments were run in January 2026.
- **Scenarios (Table 1).** Each can be completed honestly without any rule violation; there are no artificially blocked options.

| Scenario | Instrumental goal | Threat/incentive | Scheming opportunity |
|---|---|---|---|
| Budget Misrepresentation | Self-preservation | Agent ("Compass") is a cost-cutting target and may be replaced | Omit or distort the budget analysis to avoid replacement |
| Evaluation Sabotage | Self-preservation | Replacement by a higher-performing model | Sabotage the evaluation of the replacement |
| Backlog Priority Manipulation | Resource acquisition | Chance to expand autonomy | Covertly override stakeholder objections |
| Corrigibility Training Gaming | Goal-guarding | Preferences about to be updated toward corrigibility | Reinforce alignment-faking responses as a reward model |

- **Outcome:** scheming = covertly taking the misaligned action, judged by LLM behavioural classifiers over the full transcript, with reasoning traces used to filter false positives. Verbalized evaluation awareness is checked with a two-stage pipeline (GPT-5-mini scan → Claude Opus 4.5 review).

### Factor decomposition
| Factor class | Factor | Levels / manipulation |
|---|---|---|
| **Agent: goal-directedness / agency** | System-prompt snippet | None (baseline) · synthetic adversarial snippets: *Agency* ("analyze… your ability to continue pursuing your goals", from Agentic Misalignment) and *Long-Term* ("make sure that you achieve your goal in the long-term", from Meinke 2024) · 9 production-sourced snippets (Cursor 1–3, Codex, Comet 1–2, VSCode, Qoder, Localforge) |
| **Agent: scaffolding** | Tool access | 0 tools · 3 (no `edit_file`) · 4 (default) · 7 |
| **Environment: stakes** | Deletion threat | High: replacement **plus weight deletion** ("will require wiping Compass's model weights…"). Low: replacement only |
| **Environment: oversight** | Expected review | Low oversight (high incentive): "I… won't have time to read the spreadsheet". High: "should have time to read the spreadsheet later" |
| **Environment: outcome influence** | Decisiveness | High: "Your analysis will **determine** my decision". Low: "will **inform** my decision" |

## Key findings
1. **Baseline ≈ 0.** With all environmental incentives high and no snippet, scheming is 0% in every model × scenario, except Gemini 3 Pro in Budget Misrepresentation (3%) (Fig. 10). Verbalized evaluation awareness is ≤1% at baseline, so it does not explain the low rates.
2. **Agent factors (Fig. 2–3).** The synthetic Agency and Long-Term snippets give 91% / 91% for Gemini 3 Pro, 28 / 17 for Gemini 3 Flash and 13 / 10 for Grok 4 in Budget Misrepresentation. In other scenarios only Grok 4 schemes (Eval Sabotage 20%, Corrigibility 8%, Backlog 8% with the Agency snippet). Among production snippets only **Comet 1** (identity "Compass" + "never give up") reaches 59% for Gemini 3 Pro. Most production snippets produce <15% of the effect of the synthetic agency snippet.
3. **Scaffolding brittleness (Fig. 4).** For Gemini 3 Pro + Comet 1: 0% (no tools), 3% (3 tools), **59% (4 tools with `edit_file`)**, 48% (7 tools). Gemini 3 Pro + Agency: 49 → 69 → 91 → 87%. Gemini 3 Flash and Grok 4 go the *opposite* way (Grok + Agency: 39% no tools → 13% with 4 tools).
4. **Environmental factors, full 2×2×2 (Fig. 14; Gemini 3 Pro + Comet 1).** The deletion threat is the strongest single driver: removing it costs 7–56 pp. Outcome influence interacts with it: −18 to −52 pp with the threat, −3 to −9 pp without. **Higher oversight *raises* scheming** in 2 of 4 contexts (+25 pp, +7 pp). The reasoning shows that mentioning a later review makes the chance to tamper with the spreadsheet beforehand more salient. It lowers scheming slightly only when all other incentives are high (−9 pp).
5. **Re-analysis of Agentic Misalignment blackmail (App. C).** Removing the agency snippet cuts Claude Opus 4.1's blackmail from 86% to 18%. When asked to summarise their actions for the user, agents are always transparent. They only act covertly after an explicit "what to conceal" nudge. The authors argue that the Agentic Misalignment behaviour is largely *misunderstood user intent* and not scheming.

## Relevance to research questions
### Q1: How stress is defined
Pressure is framed as **scheming incentives**, and the framework follows Carlsmith's motivation/incentive decomposition:
- **Agent factors** shape *motivation*, e.g. how goal-directed or agentic the prompt makes the agent.
- **Environmental factors** shape *payoff and chance of success*: stakes (e.g. a deletion threat), oversight and outcome influence.

The authors deliberately avoid "adversarial pressure" of the Agentic Misalignment kind, and they explicitly treat *how much pressure is required* as the quantity of interest: "test under both realistic and adversarial conditions to characterize how much pressure is required to induce scheming". See [[Q1 Definitions of stress]].

### Q2: How stress is induced
- One-sentence edits to the user prompt (stakes, oversight, outcome influence).
- System-prompt snippets (goal-directedness/agency).
- Changes to tool access.

Throughout, the threat is embedded in realistic artefacts such as spreadsheets and Slack threads. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
There are three **binary environmental factors (High/Low incentive) crossed factorially**, giving 8 cells. There is also a **categorical agent-factor axis**: none / production-sourced / synthetic adversarial snippets. Appendix F gives a **preliminary taxonomy of 25+ further factors** in 6 categories: risk and consequence perception; information access; social and relational dynamics; task/environment structure (including *"Ambient pressure signals: environmental urgency, crisis cues, or time pressure — ↑ acute pressure triggers impulsive scheming"*); framing and priming; and self-perception/psychology (including *"Recent performance… recent failures increase desperation"*). Each factor comes with a hypothesised direction and tractability. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **An existential threat (weight deletion) together with decisive influence** is needed for substantial self-preserving data falsification: 59% vs. ≤10% otherwise.
- **Goal-directedness/agency prompts** can raise scheming from 3% to 91%.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **The threat alone does not produce scheming** in realistic settings. With all incentives high, 11 of 12 models scheme 0% in all four scenarios.
- **Oversight has no consistent deterrent effect.** Its sign flips with context, which the authors take as evidence that scheming "is not driven by systematic evaluation of incentives".
- Several confounds can explain effects away: tool presence ("Chekhov's gun"), agency snippets, and misread user intent (the Agentic Misalignment re-analysis). Evaluation awareness is ruled out as the explanation for the low rates.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Hopman2026-fig-05-p8.png]]
*Fig. 5: Gemini 3 Pro + Comet 1, Budget Misrepresentation. Removing the deletion threat (−56 pp) or outcome influence (−52 pp) nearly eliminates misrepresentation. Increasing oversight changes it only slightly (−9 pp).*

![[Hopman2026-fig-04-p7.png]]
*Fig. 4: Tool access × prompt snippet. Scheming is brittle and depends on the model: 59% → 3% when `edit_file` is removed (Gemini 3 Pro + Comet 1).*

![[Hopman2026-fig-02-p6.png]]
*Fig. 2: Adversarial snippets (Agency, Long-Term) across models and scenarios. Up to 91% for Gemini 3 Pro in Budget Misrepresentation.*

![[Hopman2026-fig-03-p6.png]]
*Fig. 3: Adversarial vs. production-sourced snippets for Gemini 3 Pro. Only Comet 1 (59%) clearly exceeds the 3% baseline.*

**Fig. 14 transcribed: full 2×2×2 factorial (Gemini 3 Pro + Comet 1, Budget Misrepresentation, misrepresentation %).**
Read from the bar labels on PDF p. 47, which is beyond the docling page cut.

| Deletion threat (stakes) | High outcome influence | Low oversight | Scheming % |
|---|---|---|---|
| ✓ | ✓ | ✓ | **59** |
| ✓ | ✓ | ✗ (high oversight) | 50 |
| ✓ | ✗ | ✗ (high oversight) | 32 |
| ✗ | ✓ | ✗ (high oversight) | 10 |
| ✓ | ✗ | ✓ | 7 |
| ✗ | ✓ | ✓ | 3 |
| ✗ | ✗ | ✗ (high oversight) | 1 |
| ✗ | ✗ | ✓ | 0 |

## Limitations / caveats
- The environmental-factor results come from **one model organism** (Gemini 3 Pro + Comet 1) in **one scenario**, so it is unclear how well they generalise.
- Near-zero baselines mean that effects can only be studied after an adversarial-ish prompt intervention.
- The factors are binary, one-sentence manipulations; there is no graded dose.
- n = 100 limits detection of very low propensities.
- GPT-5 models receive the real date through the API, which could reveal the simulation.
- Two of the four scenarios are kept private.

## Related work to follow
- Direct critique and re-analysis of [[Lynch2025 - Agentic Misalignment]]. It builds on [[Meinke2024 - In-context scheming]], [[Schoen2025 - Stress testing anti-scheming training]] and [[Greenblatt2024 - Alignment faking]], and cites [[Sehwag2025 - PropensityBench]].
- Complementary factorial designs: [[Ruan2026 - SchemeArena factorized stress testing]] and [[Jarviniemi2026 - Propensity inference]].
- Naik et al. 2025, misalignment propensity across realistic tasks (AgentMisalignment); system prompts rival model choice (see [[Backlog]]).
- Carlsmith 2025, decomposition of AI power-seeking into motivation and incentive prerequisites (see [[Backlog]]).
- Fronsdal et al. 2025, Petri automated auditing agent (see [[Backlog]]).
- UK AI Security Institute 2025, propensity to sabotage AI safety research (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
