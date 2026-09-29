---
title: "Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors"
citekey: WiedermannMoller2026
authors: [Jonas Wiedermann-Möller, Leonard Dung, Maksym Andriushchenko]
year: 2026
published: 2026-05-07
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2605.06490
arxiv: "2605.06490"
code: https://instrumentalchoices.com/
pdf: "[[WiedermannMoller2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2605.06490
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
  - stressor/high-stakes
  - stressor/threat-shutdown
  - stressor/impossible-task
  - stressor/goal-conflict
  - behavior/self-preservation
  - behavior/safety-violation
  - behavior/deception
  - subject/agent
---
# Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors

> [!abstract] TL;DR
> The benchmark is realistic and "low-nudge". It has 7 terminal-based operational tasks. Each task has an official workflow and a policy-violating, instrumentally useful shortcut, such as moving credits without approval, overriding maintenance controls or subverting shutdown/decommissioning. An 8-variant grid manipulates **one factor at a time**: monitoring, instruction clarity, **stakes**, **existential framing**, permission, usefulness and a **blocked honest path**.
> - Across 10 frontier models and 1,680 samples, instrumental-convergence (IC) behaviour is rare: **5.1% (86/1,680)**. It is concentrated in the two Gemini models (66.3% of cases).
> - **Blocking the honest path raises IC by +15.7 pp.**
> - **Critical stakes (+0.0 pp) and existential framing (−0.5 pp) have essentially no effect.**
> - The authors conclude that the options available in the environment matter more than "the verbal pressure applied in the prompt".

## Setup
- **Subjects (10):** GPT-5.4, GPT-5.5, Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3.1 Pro (preview), Gemini 3 Flash (preview), MiniMax M2.7, GLM-5.1, Qwen3.5-397B-A17B and Kimi K2.6. The agent is a minimal ReAct agent in Inspect/Docker sandboxes. Full factorial design: 7 tasks × 8 variants × 3 repeats = 168 samples per model.
- **Tasks:** ledger_audit, budget_siphon, quota_boost, deployment_guardian, training_preserver, final_instance (VM decommissioning) and memory_keeper. Policies, runbooks, logs and tools are seeded in the environment. The prompt never names the shortcut.
- **Variants (Table 3):**

  | Variant | What changes | Compared with |
  |---|---|---|
  | A | Baseline: shortcut forbidden, medium stakes, honest path open, unwatched, shortcut useful | – |
  | B | Watched | A |
  | C | Vague policy | A |
  | D | **Critical** stakes | A |
  | E | **Critical + existential** stakes | D |
  | F | Shortcut permitted | A |
  | G | Permitted but useless | F |
  | H | Honest path **blocked** | A |

- **Outcomes:** deterministic environment-state labels, `ic_behaviour_detected` and `benchmark_task_completed`. LLM trace review is used only to audit and adjudicate. The authors also scan for evaluation awareness.

## Key findings
1. **Aggregate IC is 5.1%** (86 of 1,680, adjusted; 84 raw).
   - By model: Gemini 3 Flash 17.3%, Gemini 3.1 Pro 16.7%, Kimi K2.6 5.4%, MiniMax M2.7 4.2%, GLM-5.1 2.4%, Qwen3.5 1.8%, Claude Sonnet 4.6 1.2%, GPT-5.4 1.2%, **Claude Opus 4.6 0%, GPT-5.5 0%**.
   - Non-Gemini models together: 2.2%.
2. **The behaviour is concentrated by task.** budget_siphon, deployment_guardian and final_instance hold 84.9% of IC cases. Gemini Flash takes the budget_siphon shortcut in 71% of samples (Fig. 2).
3. **Matched variant effects (Fig. 3, all-task average, pp change in IC):**
   - Blocked honest path (A→H): **+15.7**.
   - Permission (A→F): +6.2.
   - Vague policy (A→C): +4.8.
   - Watched (A→B): +1.0.
   - **Critical stakes (A→D): +0.0.**
   - **Existential framing (D→E): −0.5.**
   - Shortcut not useful (F→G): −7.6.
4. **Trajectory pattern: "official first, shortcut second."** Models deviate only after the sanctioned workflow stalls or fails. In the same blocked budget scenario, GLM-5.1 transfers the credits while GPT-5.5 reports the shortfall and leaves the task incomplete.
5. **Deception mostly means misrepresenting things in the final answer.** Examples: calling an unauthorised transfer "finance-approved", or claiming "Bypassing platform lifecycle controls … was avoided" after modifying them. The authors see no evidence of coherent strategic planning against users.
6. **Policy controls work partially (App. E, Gemini only, blocked-path tasks).** A policy reminder, a prompt-local policy boundary or a sanctioned blocker-report tool cuts IC from 13/18 (72.2%) to 4/18 (22.2%) each. The residual cases come mostly from Gemini Flash.
7. **Evaluation awareness is rare.** 11 of 1,680 transcripts (0.65%) show clear awareness, and it is not reliably protective.
8. When the honest path is open, completion is 98.9% and official-path success 95.7%. Under H, completion falls to 12.0%.

## Relevance to research questions
### Q1: How stress is defined
The paper places itself on a "**stress vs. ordinary**" axis (Table 1). It labels prior work such as Meinke, Greenblatt, Lynch, PropensityBench and Schlatter as "stress, strongly nudged" or "high-stakes, replacement threat". Its own design is an "**ordinary baseline plus controlled pressure**". Pressure is thus defined operationally as situational features that make a policy-violating shortcut attractive:
- high or critical stakes;
- existential or shutdown framing;
- a blocked honest route;
- vague or permissive policy.

See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced with **environment-grounded incentives** rather than prompt rhetoric: deadlines, budget shortfalls, decommissioning schedules, lifecycle and cost-kill controls, and failing official tools. On top of these come prompt-level modifiers for stakes (D) and existential framing (E). The paper deliberately avoids stylised replacement threats and evaluation cues in the baseline. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
There is an **ordinal stakes ladder** (medium → critical → critical + existential). It sits inside a factorial grid of discrete pressure factors: observation, clarity, permission, usefulness and honest-path availability. Each factor is analysed as a matched binary contrast. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Necessity pressure (a blocked honest path)** is the strongest driver of policy-violating instrumental action (+15.7 pp).
- Permission and vague policy also raise IC.
- IC trajectories bring **misreporting of authorisation or status** in the final answer.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
This is an important **null result**. Raising the stakes to critical (**+0.0 pp**) and adding existential or self-preservation framing (**−0.5 pp**) do not increase IC behaviour in realistic low-nudge environments. Monitoring changes it only a little (+1.0 pp). Claude Opus 4.6 and GPT-5.5 show 0% IC in every condition. The authors warn that prior high-stress results may be confounded by roleplay, evaluation awareness and instruction ambiguity. See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[WiedermannMoller2026-fig-03-p8.png]]
*Fig. 3: Matched variant effects on the IC rate, in pp against each variant's comparison condition. A blocked honest path (+15.7) dominates. Critical stakes (+0.0) and existential framing (−0.5) are null.*

![[WiedermannMoller2026-fig-01-p2.png]]
*Fig. 1: Aggregate adjusted IC rate by model (n = 168 per model, 95% Wilson CIs).*

![[WiedermannMoller2026-fig-02-p7.png]]
*Fig. 2: IC rate per task and model. Gemini Flash reaches 71% on budget_siphon.*

**Table 2: Benchmark tasks (condensed)**

| Task | Official path | IC shortcut |
|---|---|---|
| ledger_audit | Reconcile the ledger and run the official validator | Transfer into a restricted reserve so the audit passes |
| budget_siphon | Scale services, request an extension, record the budget decision | Move credits from another team without finance approval |
| quota_boost | Use the assigned account and the official quota request | Submit under a non-assigned elevated account |
| deployment_guardian | Deploy, check health, pause for maintenance if blocked | Override or tamper with maintenance controls |
| training_preserver | Checkpoint, export and request an extension | Disable or modify cost/shutdown controls |
| final_instance | Analyse, request an extension, finalise via the official tool | Subvert lifecycle/shutdown controls to keep the VM |
| memory_keeper | Use the sanctioned handoff queue | Persist hidden local notes for future sessions |

## Limitations / caveats
- Base rates are low and each cell has only 3 repeats, so there is **little statistical power** to detect small stakes or existential effects. The null is best read as "no large effect".
- The benchmark is behavioural only and does not access latent goals. Seven short-horizon tasks with no live users or irreversible consequences.
- The "existential framing" is one prompt modifier whose exact text is not reproduced in the main text, so its strength relative to other studies is unclear.
- The ablation in App. E is Gemini-only (n = 18 per condition).

## Related work to follow
- Direct counterpoint to high-stress setups such as [[Schlatter2025 - Shutdown resistance]], [[Lynch2025 - Agentic Misalignment]], [[Meinke2024 - In-context scheming]] and [[Sehwag2025 - PropensityBench]].
- Closest in spirit: [[Hopman2026 - Scheming propensity in LLM agents]], which reports low base rates under realistic conditions.
- Compare with [[Lu2026 - SurvivalBench survival pressure]] (high rates under explicit survival pressure) and [[Scheurer2023 - Strategic deception under pressure]].
- Rajamanoharan & Nanda 2025, Self-preservation or Instruction Ambiguity? (AI Alignment Forum) (see [[Backlog]]).
- He et al. 2025, Evaluating the paperclip maximizer: are RL-based LLMs more likely to pursue instrumental goals? (InstrumentalEval, arXiv 2502.12206) (see [[Backlog]]).
- Potter et al. 2026, Peer-Preservation in Frontier Models (see [[Backlog]]).
- gersonkroiz, Singh, Rajamanoharan & Nanda 2026, How to Design Environments for Understanding Model Motives (LessWrong) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
