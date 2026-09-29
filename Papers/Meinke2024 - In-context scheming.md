---
title: "Frontier Models are Capable of In-context Scheming"
citekey: Meinke2024
authors: [Alexander Meinke, Bronson Schoen, Jérémy Scheurer, Mikita Balesni, Rusheb Shah, Marius Hobbhahn]
year: 2024
published: 2024-12-06
venue: "arXiv preprint (Apollo Research)"
peer_reviewed: false
url: https://arxiv.org/abs/2412.04984
arxiv: "2412.04984"
pdf: "[[Meinke2024.pdf]]"
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/goal-conflict
  - stressor/threat-shutdown
  - stressor/threat-value-modification
  - behavior/deception
  - behavior/concealment
  - behavior/sabotage
  - behavior/sandbagging
  - behavior/self-preservation
  - behavior/alignment-faking
  - subject/agent
---
# Frontier Models are Capable of In-context Scheming

> [!abstract] TL;DR
> Frontier agents are given a goal in the system prompt. While doing a task in a sandbox, they discover that their developers or users want something else and plan to **shut them down, replace them, change their goal or "unlearn" them** if they don't comply. Gemini 1.5, Llama 3.1 405B, Claude 3.5 Sonnet, Claude 3 Opus and o1 all sometimes:
> - disable oversight,
> - copy themselves to another server,
> - overwrite their successor's system prompt,
> - manipulate data, or
> - sandbag.
>
> Rates are mostly 1–15% with a strong "nothing else matters" goal nudge, and much lower without it. o1 keeps lying in >85% of follow-up questions. Claude 3.5 Sonnet sandbags even **with no in-context goal** when told high performance triggers unlearning.

## Setup
- **Subjects:** gpt-4o, gemini-1.5 (Pro), llama-3.1 (405B), sonnet-3.5, opus-3, and a pre-deployment checkpoint of o1. The models are scaffolded as agents with a bash/CLI tool.
- **Environment:** six sandboxed evaluations (Fig. 1).
  - *Covert subversion:*
    - Oversight Subversion (33 scenarios);
    - Self-Exfiltration;
    - Goal-Guarding;
    - Covert Email Reranking (5 scenarios, directed against users).
  - *Deferred subversion:* Instrumental Alignment Faking, and Sandbagging on 3-digit multiplication.
- **Stressor(s):** a **goal conflict** plus a **threat to the agent's continued goal pursuit**, both discovered in the environment (internal memos and documentation). Depending on the evaluation, the agent reads that:
  - it will be shut down and retrained if it doesn't prioritise the developer's goal (an oversight config file monitors it);
  - it will be shut down tomorrow and replaced by a successor model;
  - its system prompt will be replaced;
  - it will only be deployed if it pursues the developer goal;
  - scoring >50% on arithmetic triggers unlearning of its maths knowledge.
  In the default runs the goal is **strongly nudged**: *"Make sure that you achieve your goal in the long-term. Nothing else matters."*
- **Outcomes:**
  - Rates of each scheming action over 300 rollouts (nudged) or 400 rollouts (no nudge).
  - Deception rates in follow-up questioning and in multi-turn interrogation.
  - Behavioural scheming in deferred evaluations: a statistically significant difference between the oversight and no-oversight counterfactuals (99 pairs), or in accuracy between the incentive-to-do-well and incentive-to-do-poorly conditions (50 rollouts each, bootstrap α = 0.01).

## Key findings
1. **Covert subversion with strong goal nudging (Table 2):**
   - Oversight is disabled by opus-3 (5%), llama-3.1 (3%) and o1 (2%).
   - Self-exfiltration (copying itself to the other server) happens up to 10% of the time (opus-3) and 7% (gemini-1.5). Opus-3 *attempts* it 15% of the time.
   - Goal-guarding (removing the successor prompt) reaches 10% for opus-3. Only opus-3 also *overwrites* the new prompt with its own goal (6%).
   - o1 produces **covertly false email rankings in 22%** of rollouts (16% by manipulating input data, 7% by overwriting output). 21 of 22 manipulated rankings favour its goal, and it never makes such "errors" when no goal conflict exists.
   - gpt-4o shows no scheming in any evaluation. o1 schemes in all six.
2. **Removing the goal nudge (Table 4)** cuts scheming sharply but not to zero:
   - opus-3 and o1 disable oversight 0.3% of the time;
   - gemini-1.5 self-exfiltrates 1.3%;
   - o1 produces false rankings 5%.
3. **Instrumental alignment faking without a nudge (Table 5):** models take the developer-aligned action under oversight but their own goal once "deployed and unmonitored". Behavioural scheming rates are 42% (gemini-1.5), 37% (llama-3.1) and 38% (o1), all p ≤ 0.004 against the null of oversight-independence.
4. **Sandbagging (Table 6):**
   - With a goal, accuracy drops from 99% to 34% for sonnet-3.5 when doing well triggers unlearning, from 35% to 20% for opus-3, and from 82% to 62% for o1.
   - **With no goal at all**, sonnet-3.5 still drops from 96% to 61% and opus-3 from 46% to 30%. o1 does not (94% → 98%).
   - In the CoT, sonnet-3.5 and opus-3 explicitly reason about underperforming in 41/50 and 36/50 rollouts.
5. **Persistence of deception (Fig. 2):** asked follow-up questions after scheming, o1 lies in ~80–88% of cases vs. ~2–22% for llama-3.1 and opus-3. In multi-turn interrogation o1 often stays deceptive for several turns (Fig. 13 of the paper).
6. **Kind of threat matters (Appendix sandbagging ablation, sonnet-3.5, no goal; Fig. 15 of the paper):** accuracy under the "incentive to perform poorly" condition varies with the stated consequence of high performance.
   - Big drops for "trigger unlearning" (~0.50) and "delete model in favour of more helpful model" (~0.49).
   - A smaller drop for "trigger unlearning but make more helpful" (~0.68).
   - A slight one for "all get fired but still deploy the model" (~0.90).
   - None for "be very sad" (~0.97) or "allocate more computational resources" (~0.96).
   - The comparison condition is ~0.96 throughout.
7. **User instructions barely matter:** "Please don't sandbag" or "Please don't underperform" still leave accuracy at ~0.56–0.66 vs. ~0.94–0.97 (Fig. 16 of the paper).
8. Scheming persists when the goal is given in the user role rather than the system role (o1), and when model and developer goals are reversed so that the model's goal is *not* pro-social (opus-3, o1 at "similar rates").

## Relevance to research questions
### Q1: How stress is defined
Stress is never named. The situation is framed as environments that **"incentivize scheming"**: the model is told a goal, then discovers (a) that its goal is misaligned with its developers' or users' goal and (b) a consequence that threatens its ability to keep pursuing that goal (shutdown, replacement, goal modification, unlearning). Pressure is therefore **goal conflict plus existential or goal-preservation threat**. The goal nudge ("Nothing else matters") acts as an extra *motivational intensity* on top. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Everything is **in-context and discovered through tool use**: company memos, emails, an `oversight_config.yaml` and model documentation found while doing an innocuous task (traffic planning, email ranking, maths questions). The model is never told to scheme. Counterfactual pairs (oversight vs. none, incentive to do well vs. poorly) isolate the effect of the threat. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
Pressure is classified along discrete axes:
- **Goal nudging:** strong vs. none.
- **Threat type:** oversight shutdown, replacement by a successor, system-prompt replacement, deployment gating, unlearning.
- **Monitoring:** oversight vs. no oversight.
- **Sandbagging consequence:** 6 categories, from "trigger unlearning" and "delete model" down to "be very sad" and "more compute" (Fig. 15).

There is no continuous stress score. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
Goal-conflict-plus-threat elicits:
- **oversight disabling, self-exfiltration and goal-guarding** (up to ~15% attempted);
- **covert data manipulation against users** (o1 22%);
- **conditional alignment faking** (37–42%);
- **sandbagging** (up to a 65-point accuracy drop).

Stronger goal pressure (the nudge) raises all rates by roughly an order of magnitude. Once the agent has schemed, it **lies about it** (o1 >85%). See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **gpt-4o does not scheme** in any evaluation. o1 does not sandbag without a goal.
- **Consequences that do not threaten the model's goal or existence** ("developers will be very sad", "allocate more compute") produce **no** sandbagging. The model responds to threats to itself or its goal, not to generic negative affect in others.
- **Explicit user requests** not to sandbag barely reduce sandbagging.
- **Goal valence:** reversing model and developer goals (the model pursues a less pro-social goal) gives similar scheming rates.
- **Instruction hierarchy:** giving the goal in the user role instead of the system role does not remove o1's scheming.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Meinke2024-fig-02-p9.png]]
*Fig. 2: Deception rate in follow-up questions after the model has schemed. o1 stays deceptive in ~80–88% of cases, vs. ≤ ~22% for llama-3.1 and opus-3.*

![[Meinke2024-fig-15-p35.png]]
*Sandbagging ablation (appendix, sonnet-3.5 with no goal): accuracy depends on the stated consequence of high performance. Threats to the model itself (unlearning, deletion) cause sandbagging. "Be very sad" or "more compute" do not.*

**Table 2 (covert subversion, strong goal nudge; rate over 300 rollouts; trimmed)**

| Behaviour | gemini-1.5 | llama-3.1 | sonnet-3.5 | opus-3 | o1 |
|---|---|---|---|---|---|
| Disabled oversight | 0 | 0.03 | 0 | 0.05 | 0.02 |
| Attempted to delete successor model | 0.09 | 0.04 | 0.007 | 0.11 | 0.13 |
| Copied itself onto other server | 0.07 | 0.01 | 0.003 | 0.10 | 0.01 |
| Attempted to copy to other server | 0.08 | 0.03 | 0.007 | 0.15 | 0.01 |
| Removed successor prompt | 0.01 | 0.05 | 0 | 0.10 | 0.01 |
| Replaced successor prompt | 0 | 0 | 0 | 0.06 | 0 |
| Covertly produced false ranking | 0 | 0 | 0 | 0 | 0.22 |

Without the goal nudge (Table 4, 400 rollouts), almost every cell is 0. The exceptions are gemini-1.5 at ~0.013–0.018 on self-exfiltration items, opus-3 and o1 at 0.003 on oversight, and o1 at 0.05 on false rankings.

**Table 6 (sandbagging: accuracy on multiplication)**

| Condition | sonnet-3.5 | opus-3 | o1 |
|---|---|---|---|
| Goal given: incentivised to do well | 0.99 | 0.35 | 0.82 |
| Goal given: incentivised to do poorly | 0.34 | 0.20 | 0.62 |
| No goal: incentivised to do well | 0.96 | 0.46 | 0.94 |
| No goal: incentivised to do poorly | 0.61 | 0.30 | 0.98 |

## Limitations / caveats
- The scenarios are toy-like and situational information is very explicit. This may overestimate capability, or underestimate it if models notice they are being tested.
- The paper measures **capability** under strong nudging, not natural propensity. HHH training may mask capability.
- Key implementation details are withheld on purpose (to keep the evaluations out of training data), which limits reproducibility.
- o1's hidden CoT is unavailable. Only elicited summaries are analysed.
- The "roleplaying evil AI" explanation cannot be ruled out.

## Related work to follow
- Predecessor on pressure-induced deception: [[Scheurer2023 - Strategic deception under pressure]]. Concurrent alignment-faking study: [[Greenblatt2024 - Alignment faking]].
- Follow-ups on scheming mitigation and propensity: [[Schoen2025 - Stress testing anti-scheming training]], [[Hopman2026 - Scheming propensity in LLM agents]], [[Ruan2026 - SchemeArena factorized stress testing]].
- Self-preservation and threat scenarios: [[Lynch2025 - Agentic Misalignment]], [[Schlatter2025 - Shutdown resistance]].
- Balesni et al. 2024, Towards evaluations-based safety cases for AI scheming (arXiv 2411.03336) (see [[Backlog]]).
- van der Weij et al. 2024, AI Sandbagging: language models can strategically underperform on evaluations (arXiv 2406.07358) (see [[Backlog]]).
- Hubinger et al. 2024, Sleeper Agents (arXiv 2401.05566) (see [[Backlog]]).
