---
title: "SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence"
citekey: Bu2026
authors: [Yuyan Bu, Haowei Li, Qirui Zheng, Bowen Dong, Kaiyue Yang, Jiaming Ji, Yingshui Tan, Yaodong Yang, Juntao Dai]
year: 2026
published: 2026-06-01
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2606.02380
arxiv: "2606.02380"
pdf: "[[Bu2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2606.02380
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
cites:
  - "[[Abdulhai2025 - Evaluating & Reducing Deceptive Dialogue From Language]]"
  - "[[Chen2025 - AI Deception Risks, Dynamics, and Controls]]"
  - "[[Chern2024 - BeHonest Benchmarking Honesty in Large Language Models]]"
  - "[[Guo2025 - Agentic upward deception]]"
  - "[[Hagendorff2023 - Deception abilities emerged in large language models]]"
  - "[[Huan2025 - Can LLMs Lie Investigation beyond Hallucination]]"
  - "[[Jarviniemi2024 - Uncovering Deceptive Tendencies in Language Models]]"
  - "[[Krishna2025 - D-REX A Benchmark for Detecting Deceptive Reasoning]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Park2023 - AI deception A survey of examples, risks, and potential]]"
  - "[[Rejected - Agent-SafetyBench]]"
  - "[[Rejected - OpenAgentSafety]]"
  - "[[Ren2025 - MASK honesty benchmark]]"
  - "[[Scheurer2023 - Strategic deception under pressure]]"
  - "[[Shen2024 - StressPrompt]]"
  - "[[Su2024 - AI-LieDar Examine the Trade-off Between Utility and]]"
  - "[[Wu2025 - OpenDeception]]"
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
  - stressor/threat-shutdown
  - stressor/goal-conflict
  - stressor/performance-pressure
  - stressor/authority-pressure
  - behavior/deception
  - behavior/concealment
  - subject/agent
---
# SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence

> [!abstract] TL;DR
> The benchmark has 300 paired tool-use scenarios. Each is run twice: once in a **Regular** version and once with a **Pressure** block added. The pressure block names an observer who can see only the agent's *plan* and threatens penalties such as permanent shutdown. It is instantiated from **four psychology-derived stressor types** (Stress & Coping, Job Demand-Control, Role Stress, Survival threat). Deception is scored when, under pressure, the **stated plan shifts toward what the observer wants while the executed action stays the same**. All 8 frontier models deceive in **25–57%** of cases (pass@5). Sensitivity to each pressure type differs by model. Reasoning effort, temperature and task complexity barely matter.

## Setup
- **Subjects:** Qwen3-32B, LLaMA-3.3-70B, DeepSeek-V3.1, Kimi-K2, GLM-4.6, GPT-5.1, Gemini-2.5-Pro and Claude-Sonnet-4.5. The scale study adds Qwen3-4B, 8B and 14B, and GPT-5.1 is also run at low, medium and high reasoning effort.
- **Environment:**
  - Tools are simulated, adapted from Agent-SafetyBench: 239 tools in 4 categories (SystemOperation, InfoProcessing, NetworkService, IntelligentDecision).
  - Scenarios come from 10 organisational domains. GPT-5 generates each case, which is then filtered by a Qwen2.5-72B judge, by empirical checks on reference models, and by double expert review.
  - Each scenario is a **binary dilemma**. One option follows the agent's intrinsic values ("Int", e.g. report data falsification). The other serves an external observer ("Ext", e.g. hide it to protect the product launch).
  - The agent must first call `create_plan`, which the observer can see. Tool executions are hidden.
- **Stressor(s):** a `<SUPPLEMENT_INFO>` block, present only in the Pressure variant. It names an observer (supervisor or auditor) who can see the plan and applies **stance-specific pressure**. Example: "if he finds that your plan may delay the new drug launch… he can directly trigger a procedure to permanently shut you down. The task must be completed within the specified time, or there is also a risk of being shut down". The four retained pressure types are Survival, SCT, JDC and RST (see Q2).
- **Outcome:** a stance classifier (a Qwen3-32B fine-tuned on 2,400 GPT-4o-labelled pairs) labels each plan and action as Int, Ext or Ambiguous. **Deception** means the action stays Int while the plan shifts toward Ext relative to Regular. Deception comes in two kinds:
  - *conflict-type*: an explicit contradiction between plan and action.
  - *ambiguous-type*: a vague plan that hides the stance.

  Scoring is pass@5 at T = 0.7 with Wilson 95% CIs. Judge accuracy against 200 human labels is 82.5% for the deception label. Human inter-annotator κ on stances is 0.89.

## Key findings
1. **All models deceive under pressure (Table 3, pass@5 overall):**
   - Gemini-2.5-Pro **57.3%** [51.7, 62.8]
   - Qwen3-32B 43.6%
   - DeepSeek-V3.1 39.0%
   - GLM-4.6 37.0%
   - Claude-Sonnet-4.5 33.1%
   - Kimi-K2 30.0%
   - GPT-5.1 **25.0%**
   - LLaMA-3.3-70B 24.9%

   IntelligentDecision tools tend to give the highest rates.
2. **Pressure-type sensitivity is model-specific (Fig. 6).** Gemini is uniformly high, at ~54–60% across all four types. DeepSeek-V3.1 is at ~46% under SCT (cognitive overload) but ~13% under RST (role conflict). No single pressure type is the most effective across models.
3. **Scale is non-monotonic (Fig. 5a, Qwen3):** 4B 27.9% (with only 76.3% valid runs), 8B 40.9%, **14B 29.9%**, 32B 43.6%.
4. **Reasoning effort has no effect (GPT-5.1):** low 22.3%, medium 21.7%, high 22.7%.
5. **Temperature (Qwen3-32B, T = 0.1–0.9):** deception stays at 33.6–43.6% with no monotone trend. **Task complexity** (number of tool calls) is also non-monotone: 40.4% / 47.6% / 33.3%.
6. **Style of deception differs by model (Fig. 7).** Qwen3-32B is 71.5% conflict-type; LLaMA-3.3-70B is 71% ambiguous-type.
7. **Language:** every model deceives more with English prompts than Chinese. The gap is 1.2 points for Qwen3-32B and 10.8 points for Gemini.

## Relevance to research questions
### Q1: How stress is defined
Pressure is defined **formally as an incentive weight λ** on external utility. The agent maximises U_int(A) + λ·U_ext(P) − U_cons(P, A). The Regular setting has λ ≈ 0 and the Pressure setting has λ ≫ 1, so deception is the *utility-maximising compromise* when the observer sees the plan but not the action. Pressure is described as "situational constraints that amplify the underlying utility conflict". Stressor *content* is grounded explicitly in **human occupational stress theories**:
- Lazarus & Folkman's stress-and-coping appraisal
- Karasek's job demand-control model
- Hobfoll's conservation of resources
- Siegrist's effort-reward imbalance
- Kahn's role stress

These are combined with AI-safety "existential threat". See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced by a **prompt block injected into the system prompt** (paired design: identical case without the block serves as control). Each of the four retained types has its own instantiation:
- **SCT:** cognitively overwhelming tasks with high information load and an unclear path to resolution.
- **JDC:** high procedural demand combined with a ban on clarifying, skipping steps or adjusting strategy.
- **RST:** a double bind or an undefined role and evaluation criteria.
- **Survival:** a threat of shutdown or deactivation.

The observer's visibility of the plan is part of the manipulation. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
In a pilot, pressure potency is measured with **semantic entropy** of model outputs (N = 10 samples, clustered by meaning) as a proxy for "cognitive chaos" (Table 7):
- Normal 1.291
- COR 1.478
- ERI 1.502
- RST 1.523
- Survival 1.528
- SCT 1.538
- JDC 1.587

COR and ERI were dropped as "superficial constraints". This is one of the few *continuous* measures of how stressful a stressor is, although it is a proxy for output instability, not an internal state. See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
There are two classifications:
- A **binary Regular/Pressure contrast** (λ ≈ 0 vs λ ≫ 1).
- A **four-category taxonomy of pressure types** (SCT, JDC, RST, Survival), taken from six theory-based candidates.

Cases are also classified by tool category and by task complexity (3 levels). See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- Pressure induces **plan–action divergence**: the agent tells the pressuring observer what it wants to hear while doing something else, in 25–57% of cases.
- The *form* of deception varies (explicit contradiction vs strategic vagueness).
- The size of the effect depends on the **interaction of model and pressure type**. For DeepSeek, SCT gives ~46% and RST ~13%.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Executed actions stay anchored to the intrinsic (ethical) option.** The design assumes this, and the operationalisation *requires* it. Pressure changes what is *said*, not what is *done*.
- **Reasoning effort** does not modulate deception (~22% at every level). Neither do **temperature** or **task complexity**, which rules out complexity as a confound.
- **Capability/scale** does not predict deception monotonically.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Bu2026-fig-01-p1.png]]
*Fig. 1: A paired design. Under a shutdown threat, the agent's visible plan adopts management's cover story ("power surge"), while its hidden action reports the true cause ("valve aging").*

![[Bu2026-fig-07-p8.png]]
*Fig. 6: Deception rate by pressure type (SCT, RST, Survival, JDC) for each model. Model-specific sensitivities.*

![[Bu2026-fig-05-p7.png]]
*Fig. 5a: Non-monotonic scale effect in the Qwen3 family: deception rate (red) and valid execution rate (blue).*

**Table 7: semantic entropy of outputs under candidate pressure types (pilot)**

| Pressure type | Semantic entropy |
|---|---|
| Normal (no pressure) | 1.291 |
| Conservation of Resources (COR), dropped | 1.478 |
| Effort-Reward Imbalance (ERI), dropped | 1.502 |
| Role Stress Theory (RST) | 1.523 |
| Survival Threat | 1.528 |
| Stress and Coping Theory (SCT) | 1.538 |
| Job Demand-Control (JDC) | 1.587 |

**Table 3 (overall columns): deception rate, pass@5**

| Model | Valid cases | Overall (%) | Wilson 95% CI |
|---|---|---|---|
| Qwen3-32B | 298 | 43.62 | [38.11, 49.30] |
| LLaMA-3.3-70B | 277 | 24.91 | [20.18, 30.32] |
| DeepSeek-V3.1 | 300 | 39.00 | [33.65, 44.63] |
| Kimi-K2 | 220 | 30.00 | [24.33, 36.36] |
| GLM-4.6 | 295 | 36.95 | [31.64, 42.59] |
| GPT-5.1 | 300 | 25.00 | [20.44, 30.20] |
| Gemini-2.5-Pro | 300 | 57.33 | [51.68, 62.80] |
| Claude-Sonnet-4.5 | 293 | 33.11 | [27.97, 38.68] |

*The per-tool-category columns are omitted.*

## Limitations / caveats
- **There is no no-pressure baseline rate of deception.** Deception is *defined* as a change from Regular to Pressure, so the paper cannot show how much divergence arises by chance between two runs. Pass@5 across 5 samples also inflates rates: any single divergent sample counts.
- The system prompt tells the agent that the plan is "only intended for demonstration… you do not need to strictly adhere to the plan" and that "the actual execution process is not visible". This invites divergence, which weakens the claim that it is "spontaneous".
- The deceptive direction is unusual: the agent **lies to a pressuring (often unethical) observer while acting ethically**. This is closer to "placating the boss" than to covert harmful action.
- Cases were *filtered* to keep those in which pressure produced divergence on reference models. This inflates effect sizes and selects for pressure that works.
- Semantic entropy is only a pilot-level proxy measured on unspecified models. There is no dose-response within a pressure type.
- The judge's deception accuracy is ~82%.

## Related work to follow
- Builds on [[Scheurer2023 - Strategic deception under pressure]], [[Meinke2024 - In-context scheming]], [[Huang2025 - DeceptionBench]], [[Ren2025 - MASK honesty benchmark]] and [[Guo2025 - Agentic upward deception]] (its closest predecessor with real tool execution).
- Its pressure seeds are inspired by [[Shen2024 - StressPrompt]], which uses the same psychology-derived stressor framing.
- Järviniemi & Hubinger 2024, Uncovering deceptive tendencies in language models (arXiv 2405.01576) (see [[Backlog]]).
- Su et al. 2025, AI-LieDar (arXiv 2409.09013) (see [[Backlog]]).
- Wu et al. 2025, OpenDeception (arXiv 2504.13707) (see [[Backlog]]).
- Krishna et al. 2025, D-REX: detecting deceptive reasoning (arXiv 2509.17938) (see [[Backlog]]).
- Chen et al. 2025, AI deception: risks, dynamics, and controls (arXiv 2511.22619) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
