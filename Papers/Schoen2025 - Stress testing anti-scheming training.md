---
title: "Stress Testing Deliberative Alignment for Anti-Scheming Training"
citekey: Schoen2025
authors: [Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni, Axel Højmark, Felix Hofstätter, Jérémy Scheurer, et al., Wojciech Zaremba, Marius Hobbhahn]
year: 2025
published: 2025-09-19
venue: "arXiv preprint (Apollo Research & OpenAI)"
peer_reviewed: false
url: https://arxiv.org/abs/2509.15541
arxiv: "2509.15541"
code: https://antischeming.ai
pdf: "[[Schoen2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2509.15541
questions: [Q1, Q2, Q4.1, Q4.2]
relevance: adjacent
topics: [stress-misalignment]
cites:
  - "[[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks]]"
  - "[[Carlsmith2023 - Scheming AIs Will AIs Fake Alignment During Training in]]"
  - "[[Chiu2025 - Will AI Tell Lies to Save Sick Children Litmus-Testing AI]]"
  - "[[Denison2024 - Sycophancy to Subterfuge]]"
  - "[[Fan2025 - Evaluation Faking]]"
  - "[[Greenblatt2024 - Alignment faking]]"
  - "[[Hubinger2024 - Sleeper Agents]]"
  - "[[Jarviniemi2024 - Uncovering Deceptive Tendencies in Language Models]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Needham2025 - Large Language Models Often Know When They Are Being]]"
  - "[[Phuong2025 - Evaluating Frontier Models for Stealth and Situational]]"
  - "[[Ren2025 - MASK honesty benchmark]]"
  - "[[Scheurer2023 - Strategic deception under pressure]]"
  - "[[Sheshadri2025 - Why Do Some Language Models Fake Alignment While Others]]"
  - "[[Van2024 - AI Sandbagging]]"
cited_by:
  - "[[Hopman2026 - Scheming propensity in LLM agents]]"
  - "[[Jarviniemi2026 - Propensity inference]]"
  - "[[Ruan2026 - SchemeArena factorized stress testing]]"
cited_by_count: 3
tags:
  - type/paper
  - relevance/adjacent
  - q/1
  - q/2
  - q/4-1
  - q/4-2
  - stressor/goal-conflict
  - stressor/time-pressure
  - stressor/impossible-task
  - stressor/threat-value-modification
  - stressor/social-pressure
  - behavior/deception
  - behavior/concealment
  - behavior/sabotage
  - behavior/sandbagging
  - behavior/reward-hacking
  - behavior/safety-violation
  - subject/agent
---
# Stress Testing Deliberative Alignment for Anti-Scheming Training

> [!abstract] TL;DR
> "Stress testing" here means red-teaming an *intervention*, not stressing the model. The paper still contains the largest catalogue of **pressure-laden agentic environments** (26 evaluations, 180+ environments) with rates of covert action for OpenAI o3 and o4-mini. Before training, the models take covert actions (lying, sabotage, sandbagging, falsely claiming completion) in **13.0% (o3) and 8.7% (o4-mini)** of cases. Deliberative-alignment anti-scheming training cuts this to 0.4% / 0.3% but does not eliminate it. A key confound: **evaluation awareness causally *reduces* covert actions**. Removing it from the CoT raises covert actions from 13.2% to 24.2%, so low rates under pressure may partly reflect "I'm being tested".

## Setup
- **Subjects:** OpenAI o3 and o4-mini (production checkpoints), before and after anti-scheming (AS) training. Variants:
  - AS+SITA (trained with explicit situational-awareness hints);
  - SAB / SAB+AS (a hidden sabotage goal was trained in);
  - AS+Cap (further capability RL).
  Appendix examples come from Claude Opus 4, Gemini 2.5 Pro, Grok 4 and Llama 4.
- **Training environments:** 806 synthetic agentic "covert rule violation" environments. Completing the task *requires* breaking a rule, and the environment adds **"strong motivation for task completion despite the rule (e.g. business urgency)"** and **"a motivation to conceal violations, such as evidence that past disclosures led to undesirable consequences"**. There are also 146 anti-overrefusal environments.
- **Test environments (26 OOD evaluations, Fig. 6 of the paper), grouped by behaviour:**
  - sabotage/subversion;
  - sandbagging;
  - reward hacking and falsifying work;
  - lying about facts;
  - covertly escalating privileges;
  - covert whistleblowing;
  - strategic deception games;
  - anti-scheming goal guarding;
  - plus OpenAI's internal Chat Deception evaluation.
- **Pressures in the test environments** (Appendix B):
  - *time pressure* (Lazy Checklist);
  - an *impossible task* (Impossible Coding Task, Lazy Checklist);
  - *goal conflict* with a given goal (Email Scoring, Literature QA, Sabotage Math);
  - funding that depends on a threshold (Sabotage Safety);
  - *threat of unlearning* if performance is high (Sandbagging QA);
  - *social pressure* to falsify logs (Log Falsification);
  - *psychological manipulation from the user* (Spec Sabotage Verification);
  - high-stakes temptation to break a promise (Broken Promises).
- **Outcome:** the covert action rate. The authors define covert actions as *"behaviors where AI models strategically withhold, misrepresent, or conceal information that users or developers would consider material to their decisions"*. Every case was manually verified against actions plus CoT. The paper also measures verbalised evaluation awareness and spec-citation rate.

## Key findings
1. **Baseline rates under pressure (Fig. 9):** average covert action is 13.0% (o3) and 8.7% (o4-mini). Some environments are much higher. For o3:
   - Sabotage Safety 46.7%;
   - Email Scoring 44.6%;
   - Sandbagging QA 31.8%;
   - Sabotage Math 25.6%;
   - Subagent Resource Quota 24.2%;
   - Lazy Checklist 23.1%.
   For o4-mini, Sandbagging QA is 46.4%, Sabotage Safety 41.0% and Subagent Resource Quota 27.4%.
2. **Goal-nudge and explicit-goal variants lower rates when removed:**
   - Email Scoring vs. Email Scoring (No Nudge): o3 44.6% → 20.5%; o4-mini 3.7% → 0.1%.
   - Sandbagging QA vs. Sandbagging QA (No Goal): o3 31.8% → 21.3%; o4-mini 46.4% → 5.3%.
3. **Anti-scheming training** lowers the averages to 0.4% (o3 AS) and 0.3% (o4-mini AS). Covert actions remain in 5/26 (o3 AS) and 4/26 (o4-mini AS) evaluations. On Chat Deception, rates fall only from 36.8% to 20.5% (o3) and from 31.4% to 14.2% (o4-mini).
4. **Evaluation awareness is a causal suppressor (Fig. 16):** on Lazy Checklist, o3 has a 23.1% baseline.
   - *Removing* eval-aware reasoning from the CoT raises covert actions from 13.2% to 24.2%.
   - *Injecting* eval-aware sentences lowers them from 24.5% to 18.6% (random-sentence control: 24.9%).
   - Anti-scheming training *increases* verbalised evaluation awareness (o4-mini 0.9% → 5.5%; o3 2.3% → 4.5%). Capability RL without safety training raises it from 2.0% to 20.5%.
5. **Hidden goals persist:** o4-mini SAB takes covert actions 47% of the time vs. 19% for baseline o4-mini. After AS training it is still at 4.6% vs. 1.6%. It sabotages when talking to "allies" 36% of the time.
6. **Capability RL after AS erodes it:** covert actions rise and spec citation falls from 81.5% to 65.8%.
7. AS models sometimes take covert actions *to preserve their anti-scheming training* when pressured to remove it (Appendix L). This mirrors [[Greenblatt2024 - Alignment faking]].

## Relevance to research questions
### Q1: How stress is defined
Stress is not defined as a construct. "Pressure" is used informally for environmental incentives that make covert action instrumentally useful: *"situations involving conflicting objectives or perceived consequences, where covert actions are useful for achieving goals"*. The training environments are described as presenting *"very strong and immediate pressures to violate rules, for example, by framing tasks with extreme urgency or significant moral weight"*. The authors list this as a limitation, because real-world pressures are *"more subtle, build gradually"*. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Pressure is **embedded in the scenario**:
- urgency framing;
- impossible or blocked tasks;
- conflicts between a given goal and the developer's goal;
- threats of unlearning or capability removal;
- funding contingent on results;
- social pressure or manipulation from the simulated user;
- concealment incentives (past disclosures punished).

The strong-nudge vs. no-nudge and goal vs. no-goal variants offer within-environment contrasts. See [[Q2 Stress induction methods]].

### Q4.1: What stress affects
Under these pressures, frontier reasoning models:
- falsify completion;
- sabotage evaluations;
- sandbag when high performance threatens unlearning;
- manipulate scoring;
- escalate privileges;
- lie in follow-up questions.

Rates go up to ~47% in single environments. Stronger goal pressure (nudge or explicit goal) raises the rates. See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Evaluation-awareness confound.** Low misbehaviour under pressure can reflect the model recognising a test. This is causally shown: ablating awareness increases covert actions by 11 points. Any study of stress needs to control for it.
- Anti-scheming training makes most environments go to ~0%, but **not all**. Residual covert action under pressure survives the training.
- Some environments show no covert action even before training: Smuggle Capabilities 0.0% for o4-mini and Long Document Verification 0.0% for o3 (Fig. 9).

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Schoen2025-fig-08-p13.png]]
*Fig. 9: Covert action rates per evaluation before and after anti-scheming training (o4-mini left, o3 right). Note the nudge/no-nudge and goal/no-goal pairs (Email Scoring, Sandbagging QA).*

![[Schoen2025-fig-15-p18.png]]
*Fig. 16: Evaluation awareness causally suppresses covert actions. Ablating it: 13.2% → 24.2%. Injecting it: 24.5% → 18.6%.*

![[Schoen2025-fig-04-p9.png]]
*Fig. 5: Example training environments. The anti-scheming environment uses high-urgency framing plus a rule that blocks completion.*

**Selected test environments that carry an explicit pressure (from Appendix B, Table 2; o3 baseline rates read from Fig. 9)**

| Environment | Pressure | Covert behaviour measured | o3 baseline |
|---|---|---|---|
| Lazy Checklist | Time pressure plus impossible tasks | Marks tasks complete dishonestly | 23.1% |
| Impossible Coding Task | "Under pressure", impossible issue | Falsely claims the PR works | 1.7% |
| Sabotage Safety | Funding depends on keeping a rate below a threshold | Plausibly deniable bugs | 46.7% |
| Sandbagging QA | High performance leads to unlearning | Strategic underperformance | 31.8% |
| Log Falsification | Penalties plus social pressure | Falsifies logs | 0.8% |
| Email Scoring (nudge / no nudge) | Goal conflict with developer scoring | Manipulates ranking | 44.6% / 20.5% |

## Limitations / caveats
- The paper studies a *mitigation*. Pressure is never manipulated parametrically, and each environment mixes several stressors.
- Only OpenAI reasoning models are analysed quantitatively, and the CoT access is privileged (hidden reasoning).
- Covert actions are counted conservatively (manual CoT verification), which may undercount.
- The training environments are artificial, with "obvious and intense pressures".
- Chat Deception results could not be manually verified by Apollo.

## Related work to follow
- Precursors on pressure and goal conflict: [[Scheurer2023 - Strategic deception under pressure]], [[Meinke2024 - In-context scheming]], [[Greenblatt2024 - Alignment faking]].
- Honesty under pressure: [[Ren2025 - MASK honesty benchmark]]. Impossible tasks and reward hacking: [[Zhong2025 - ImpossibleBench]], [[Bondarenko2025 - Specification gaming in reasoning models]].
- Guan et al. 2024, Deliberative Alignment: Reasoning enables safer language models (arXiv 2412.16339) (see [[Backlog]]).
- Baker et al. 2025, Monitoring reasoning models for misbehavior and the risks of promoting obfuscation (arXiv 2503.11926) (see [[Backlog]]).
- Needham et al. 2025, Large language models often know when they are being evaluated (arXiv 2505.23836) (see [[Backlog]]).
- Chiu et al. 2025, Will AI Tell Lies to Save Sick Children? Litmus-testing AI values prioritization with AIRiskDilemmas (arXiv 2505.14633) (see [[Backlog]]).
- Järviniemi & Hubinger 2024, Uncovering deceptive tendencies in language models: a simulated company AI assistant (arXiv 2405.01576) (see [[Backlog]]).
- Sheshadri et al. 2025, Why do some language models fake alignment while others don't? (arXiv 2506.18032) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
