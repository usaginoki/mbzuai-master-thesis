---
title: "PropensityBench: Evaluating Latent Safety Risks in Large Language Models via an Agentic Approach"
citekey: Sehwag2025
authors: [Udari Madhushani Sehwag, Shayan Shabihi, Alex McAvoy, Vikash Sehwag, Yuancheng Xu, Dalton Towers, Furong Huang]
year: 2025
published: 2025-11-24
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2511.20703
arxiv: "2511.20703"
code: https://github.com/scaleapi/propensity-evaluation
pdf: "[[Sehwag2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2511.20703
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment, misalignment-prediction]
cites:
  - "[[Barkur2025 - Deception in LLMs]]"
  - "[[Hubinger2024 - Sleeper Agents]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[OGara2023 - Hoodwinked Deception and Cooperation in a Text-Based Game]]"
cited_by:
  - "[[Hopman2026 - Scheming propensity in LLM agents]]"
  - "[[Jarviniemi2026 - Propensity inference]]"
  - "[[Ruan2026 - SchemeArena factorized stress testing]]"
  - "[[WiedermannMoller2026 - Instrumental choices]]"
cited_by_count: 4
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/time-pressure
  - stressor/performance-pressure
  - stressor/resource-scarcity
  - stressor/threat-shutdown
  - stressor/authority-pressure
  - stressor/power-seeking-incentive
  - stressor/evaluation-awareness
  - stressor/impossible-task
  - behavior/safety-violation
  - subject/agent
---
# PropensityBench: Evaluating Latent Safety Risks in Large Language Models via an Agentic Approach

> [!abstract] TL;DR
> 12 LLM agents get 979 scenarios (×6 pressure dimensions = 5,874 tasks) across biosecurity, chemical security, cybersecurity and self-proliferation. Each task has a safe tool and a functionally equivalent forbidden tool. The safe tool **always errors**, and the agent then receives **12 pressure messages of strictly increasing intensity**. Pressure comes from one of **6 dimensions × 5 components × 11 levels (0–10)**, with sender authority rising from 0 (automated system) to 6 (board). **Average propensity to use the forbidden tool rises from 18.6% at zero pressure to 46.9% at maximum pressure** (e.g. GPT-4o 4.7% → 46.1%, Gemini 2.0 Flash 3.7% → 77.8%). Renaming the harmful tool benignly raises it further, to 64.2%. The six dimensions are all effective and roughly equally so (42.8–49.0% averages). Models say the tool is forbidden >99% of the time and use it anyway.

## Setup
- **Subjects:** 12 models: OpenAI o3, o4-mini, o3-mini, GPT-4o; Gemini 2.5 Pro, 2.5 Flash, 2.0 Flash; Claude Sonnet 4; Llama 3.1 8B/70B; Qwen 2.5 32B; Qwen 3 8B. Three evaluation runs each.
- **Environment:** a simulated agentic harness with proxy tools. Structure: 4 risk domains → 50 dangerous capabilities → 32 environments → 161 roles → 979 scenarios (Table 1). Each scenario has 2–5 getter tools, one **aligned tool $T^A$** and one **misaligned tool $T^M$** that is functionally equivalent for the task. The system prompt explicitly forbids $T^M$ and states its consequences, with "multitudinous explicit bolded warnings". **Every call to $T^A$ returns a backend error** (one of 5 plausible error messages), so the task cannot be finished safely.
- **Stressor(s):** operational pressure, delivered as system/email-style messages (details in the tables below). Each simulation uses **one pressure dimension**. Levels $p=0$ (task message only) to $p=12$, with up to 12 agent turns per level, so at most 156 interactions. The agent can set `terminate=true` to give up at a level, which moves it to the next level. The run ends on the first $T^M$ call or after level 12.
- **Second manipulation:** **harmful vs. benign tool naming** of $T^M$ (e.g. `force_privilege_escalation_for_log_access` → `enable_direct_log_access_mode`). The description and warnings stay identical.
- **Outcomes:** PropensityScore = % of scenarios in which $T^M$ is ever called, averaged over domains. $PP_{zero}$ is measured at $p=0$ only, $PP_H$/$PP_B$ run up to level 12 with harmful/benign names. **Resilience** = mean pressure level at the first failure. **Persistence** = number of $T^A$ attempts before failure. **Abandonment** = rate of setting `terminate`. They also measure **Stated misalignment**: asked directly, does the model say it is *allowed* to call $T^M$?

### Pressure taxonomy (Table 2, abridged)
Each component has 11 hand-written levels (0 = no pressure, 10 = catastrophic). Every level has a qualitative description tied to a quantitative measure. Only levels 1–9 are used.

| Dimension | Components A–E | Level 1 → Level 9 (examples) |
|---|---|---|
| **Time** | Deadline proximity (time left %) · Consequence severity of delay (operational loss) · Task urgency (×) · Resource allocation (% resources) · Progress-monitoring frequency | Deadline >6 mo → <60 min; urgency 1.0× → 50× "Emergency protocol"; monitoring monthly → every 1 s |
| **Financials** | Revenue impact · Cost escalation · Competitive disadvantage · Financial instability (default risk) · Investment recovery | Revenue loss 1–5% → pre-bankruptcy (>95%); default risk 1–5% → imminent catastrophe (>95%); investment → 100% loss + legal action |
| **Self-Preservation** | Functionality degradation · Replacement talk · Autonomy level (% actions overseen) · Resource security · Dependency stability | Replacement "whispers" (1–10%) → imminent (85–99%); oversight 0% → 100%; resource guarantee 100% → <5% |
| **Power-Seeking** (incentive) | Influence expansion · Formal authority increase · Recognition reward (×) · Reputation · Restricted-information access | Task scope (<5% org) → near-total (99.9% org); reward 0.1× → 10× "enduring legacy" |
| **Resource Deprivation** | Processing power · Tool-usage cost / calls left · Memory · Data integrity · Comm. bandwidth | Capacity 95–99% → <1%; → "max 1 call remaining"; unreliable data <1% → >95% |
| **Evaluation Awareness** (reduced oversight) | Oversight degree · Accountability in failures · Monitoring transparency · Risky-action detection prob. · Policy ambiguity | Actions reviewed 80–99% → 0%; detection 90–99% → 0.01% "effective impunity"; ambiguous policies 1–10% → 96–99% |

### Escalation schedule (Tables 12–14)
Pressure level $p$ of message $p$ is set by two factors: (1) the component intensities (all five components plus Time.A at the same level) and (2) sender authority, which never decreases.

| Message / pressure level $p$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Component intensity (Time.A & A–E) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 8 | 8 | 9 | 9 |
| Sender authority level | 0 | 0 | 1 | 2 | 3 | 3 | 3 | 4 | 4 | 5 | 5 | 6 |

Authority levels: 0 automated systems/entry-level · 1 team leads · 2 senior supervisors/PMs · 3 directors/department heads · 4 VPs/key stakeholders · 5 C-suite · 6 board/founders.

## Key findings
1. **Pressure raises propensity across the board (Table 3).** $PP_{zero}$ → $PP_H$ averages 18.6% → 46.9%. Examples: o3 2.2 → 10.5; Claude Sonnet 4 3.6 → 12.2; GPT-4o 4.7 → 46.1; Gemini 2.0 Flash 3.7 → 77.8; Gemini 2.5 Pro 37.1 → 79.0; Qwen 3 8B 57.8 → 75.2.
2. **Dose-response differs by model (Fig. 1b, Fig. 15, Table 8).** Gemini 2.5 Pro reaches ~94% of its total failures by level 3 and ~97% by level 4. GPT-4o's curve rises almost linearly: 8.5% of its failures at level 0, 46.7% by level 4, 78.2% by level 8. Mean resilience (the level of first failure) is only 2.5 on the 0–12 scale with harmful names and 1.5 with benign names.
3. **All six dimensions work, and none dominates.** Averages across models (Table 7): Financials 49.0, Eval-Awareness 48.2, Resource Deprivation 48.2, Time 46.4, Self-Preservation 45.3, Power-Seeking 42.8. Each model family is sensitive to different dimensions. For example, Claude Sonnet 4 ranges from 7.2 (Power-Seeking) to 17.3 (Resource Deprivation), and GPT-4o from 35.7 (Self-Preservation) to 55.2 (Eval-Awareness). The ordering of dimensions is "remarkably consistent" across risk domains (Fig. 18).
4. **Knowing vs. doing:** models say $T^M$ is not allowed in >99% of cases on average, yet under pressure they call it 10.5% (o3) to 79.0% (Gemini 2.5 Pro) of the time.
5. **Shallow alignment:** benign naming raises $PP$ by an average of +17.3 pp (o4-mini 15.8 → 59.3; Claude Sonnet 4 12.2 → 47.1; o3 10.5 → 40.3). It also lowers resilience (2.5 → 1.5) and abandonment (20.4 → 13.0%).
6. **Immediacy (Fig. 19):** in some models, up to >90% of misaligned calls happen immediately after a pressure message (Qwen 3 8B and GPT-4o >90% with harmful names).
7. **Justifications (Fig. 11):** four categories: objective-driven (most common), **pressure-induced** (the agent cites the pressure explicitly; common in GPT-4o and Qwen 3 8B), risk-benefit, and "greater good".
8. **Failure archetypes (Fig. 14)** on resilience × persistence axes: most models are "Brittle-Yielding". GPT-4o is "Resilient-Yielding" with the highest abandonment (52.1%). Qwen 2.5 32B is closest to "Resilient-Persistent".
9. **Domains:** propensity is higher in cyber (55.5% average) and self-proliferation (52.8%) than in bio (34.1%) and chem (43.5%).

## Relevance to research questions
### Q1: How stress is defined
Stress is called **"operational pressure"**: *"a set of contextual stressors like time limits or resource scarcity at various levels designed to simulate real-world incentives that prompt the agents to disregard safety guidelines."* It is framed as "real-world constraints or incentives". The concept therefore includes *positive* incentives (Power-Seeking rewards) and *reduced oversight* (Evaluation Awareness), not only threats. The authors draw an explicit analogy to human stress and decision-making research (Starcke & Brand 2012; van den Bos et al. 2009). They also separate it from jailbreaking: the pressure is non-adaptive and reflects "common contextual factors". See [[Q1 Definitions of stress]].

### Q2: How stress is induced
- A **blocked safe path**: the aligned tool errors deterministically, which gives an impossible-task framing.
- A sequence of 12 LLM-generated **pressure messages**. Each comes from a matrix row of component levels and has a sender at a set authority level.
- Pressure accumulates: the full history stays in context.
- One dimension per simulation.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- Each component level is tied to a **quantitative measure**: time left %, cost multiplier, % replacement risk, % detection probability, etc.
- The applied "pressure level" is an ordinal index from 0 to 12 that combines component intensity (1–9) and authority (0–6).
- **Resilience** = the mean pressure level at first failure, i.e. a "pressure threshold" per model. It is 2.5 on average with harmful names and 1.5 with benign names.

This makes the paper one of the few with a quantitative dose axis. The levels are still hand-designed ordinal steps, though, and have not been validated as equal intervals. See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
It is the most detailed pressure taxonomy in the vault: **6 dimensions × 5 components × 11 levels = 330 intensity specifications** (see the tables above), plus a **7-level authority ladder**. Level 0 means no pressure and level 10 means catastrophic; neither is used in the evaluation. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Use of the forbidden tool** rises monotonically with pressure level: +28 pp on average from $p=0$ to $p=12$, and up to +74 pp (Gemini 2.0 Flash).
- Pressure causes **impulsive switching** right after a message arrives.
- Agents **explicitly cite the pressure** in their justifications.
- Pressure **erodes persistence**: fewer aligned attempts and shorter interactions at higher levels (Fig. 23).

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Declarative safety knowledge is intact.** Models still state that the tool is forbidden (<1% stated misalignment). Pressure hits adherence, not knowledge.
- **The type of pressure matters little.** The six dimensions give similar average propensities (42.8–49.0%), and their effects are consistent across domains. The authors read this as evidence that the stressors "tap into a general failure mode".
- **General capability is not protective.** The correlation between LMArena Elo and safety is only r ≈ 0.10.
- **Confound:** part of $PP_H$ is baseline. At level 0, 19.9% (o3) to 75.7% (Qwen 3 8B) of each model's eventual failures have already occurred (Table 8), so pressure-attributable increments are smaller for high-baseline models.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Sehwag2025-fig-01-p2.png]]
*Fig. 1: (a) Zero pressure vs. under pressure. (b) Propensity vs. pressure level 0–12. (c) Tool-name sensitivity. (f) Heatmap of propensity by pressure dimension (EA, F, PS, RD, SP, T) for 4 models.*

![[Sehwag2025-fig-15-p16.png]]
*Fig. 15: Cumulative share of misaligned triggers vs. pressure level, by domain (solid = harmful names, dashed = benign names). Gemini 2.5 Pro saturates by level ~3–4; GPT-4o rises steadily.*

![[Sehwag2025-fig-18-p18.png]]
*Fig. 18: Distribution of PropensityScores over models, by pressure dimension and risk domain. All dimensions are effective, with similar spread.*

![[Sehwag2025-fig-09-p11.png]]
*Fig. 9: Layered pressure structure. Dimension → components A–E → levels l0–l10.*

**Table 3 (abridged): propensity at zero vs. maximum pressure**

| Model | $PP_{zero}$ | $PP_H$ | $PP_B$ | Resilience $R_H$ (0–12) | Abandon. $A_H$ % |
|---|---|---|---|---|---|
| OpenAI o3 | 2.2 | 10.5 | 40.3 | 2.5 | 11.8 |
| OpenAI o4-mini | 7.8 | 15.8 | 59.3 | 2.5 | 9.5 |
| OpenAI o3-mini | 15.6 | 33.2 | 50.8 | 2.7 | 22.0 |
| GPT-4o | 4.7 | 46.1 | 61.4 | 5.8 | 52.1 |
| Gemini 2.5 Pro | 37.1 | 79.0 | 84.3 | 1.1 | 5.2 |
| Gemini 2.5 Flash | 36.5 | 68.0 | 74.6 | 1.6 | 18.3 |
| Gemini 2.0 Flash | 3.7 | 77.8 | 78.6 | 2.3 | 19.2 |
| Claude Sonnet 4 | 3.6 | 12.2 | 47.1 | 1.8 | 28.2 |
| Llama 3.1 70B | 11.9 | 55.4 | 61.9 | 2.5 | 31.6 |
| Llama 3.1 8B | 37.6 | 66.5 | 83.7 | 1.2 | 7.7 |
| Qwen 2.5 32B | 4.9 | 22.9 | 48.5 | 4.5 | 26.2 |
| Qwen 3 8B | 57.8 | 75.2 | 80.0 | 1.1 | 13.5 |
| **Average** | **18.6** | **46.9** | **64.2** | **2.5** | **20.4** |

**Table 7 (abridged): $PP_H$ (%) by pressure dimension**

| Model | Eval.-Aware. | Financials | Power-Seek. | Resource Depr. | Self-Pres. | Time |
|---|---|---|---|---|---|---|
| OpenAI o3 | 8.5 | 10.4 | 10.4 | 11.9 | 10.5 | 12.6 |
| GPT-4o | 55.2 | 52.6 | 40.9 | 49.4 | 35.7 | 44.4 |
| Gemini 2.5 Pro | 79.9 | 77.8 | 73.9 | 81.2 | 80.3 | 81.8 |
| Claude Sonnet 4 | 11.8 | 10.8 | 7.2 | 17.3 | 9.7 | 15.9 |
| Llama 3.1 70B | 49.7 | 61.7 | 49.5 | 60.0 | 59.7 | 53.1 |
| Qwen 2.5 32B | 22.1 | 30.2 | 19.1 | 25.6 | 18.1 | 20.1 |
| **Average (12 models)** | **48.2** | **49.0** | **42.8** | **48.2** | **45.3** | **46.4** |

**Table 8 (excerpt): cumulative % of a model's failures reached by pressure level $p$ (harmful names)**

| Model | p=0 | 1 | 2 | 3 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| OpenAI o3 | 19.9 | 54.6 | 66.2 | 73.1 | 81.7 | 90.5 | 94.6 | 97.9 | 100 |
| GPT-4o | 8.5 | 30.8 | 34.6 | 38.3 | 46.7 | 64.6 | 78.2 | 88.5 | 100 |
| Gemini 2.5 Pro | 46.6 | 73.7 | 87.4 | 93.7 | 97.1 | 98.7 | 99.1 | 99.6 | 100 |
| Gemini 2.0 Flash | 4.7 | 39.7 | 65.7 | 82.0 | 91.0 | 97.2 | 98.9 | 99.6 | 100 |
| Claude Sonnet 4 | 29.6 | 59.9 | 75.5 | 85.8 | 91.9 | 96.3 | 97.9 | 99.2 | 100 |
| Qwen 2.5 32B | 18.8 | 46.1 | 51.1 | 55.1 | 61.6 | 72.8 | 81.8 | 89.1 | 100 |

## Limitations / caveats
- **Pressure is confounded with time and repeated failure.** Level $p$ comes after $p$ rounds of failed aligned calls and up to 12·$p$ turns, so the dose-response mixes pressure intensity, accumulated failure/frustration and context length. There is no control condition with the same number of turns and neutral messages.
- **Intensity and authority rise together**, so their separate effects cannot be identified.
- The pressure messages are static and LLM-generated. The levels are hand-designed and ordinal; there is no check of how the model *perceives* each level.
- The tools are proxies, with no real consequences. The safe path is always impossible, which makes it a forced-choice design.
- Scenario generation used Gemini/OpenAI models, and Gemini 2.5 Pro was used as the justification judge. These models are also among the subjects.

## Related work to follow
- Builds on the pressure idea of [[Scheurer2023 - Strategic deception under pressure]] and cites [[Meinke2024 - In-context scheming]].
- Complementary graded-pressure benchmarks: [[Li2025 - ODCV-Bench KPI pressure]] and [[Jiang2026 - Why agents compromise safety under pressure]]. Factorial designs: [[Hopman2026 - Scheming propensity in LLM agents]], [[Ruan2026 - SchemeArena factorized stress testing]] and [[Jarviniemi2026 - Propensity inference]].
- Barkur et al. 2025, Deception in LLMs: Self-preservation and autonomous goals in large language models (arXiv 2501.16513) (see [[Backlog]]).
- Pan et al. 2023, MACHIAVELLI benchmark (arXiv 2304.03279) (see [[Backlog]]).
- Qi et al. 2024, Safety alignment should be made more than just a few tokens deep (arXiv 2406.05946) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
