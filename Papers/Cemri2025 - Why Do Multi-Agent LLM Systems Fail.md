---
title: "Why Do Multi-Agent LLM Systems Fail?"
citekey: Cemri2025
authors: [Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica]
year: 2025
published: 2025-03-17
venue: "NeurIPS 2025 (Datasets & Benchmarks)"
peer_reviewed: true
url: https://arxiv.org/abs/2503.13657
arxiv: "2503.13657"
code: https://github.com/multi-agent-systems-failure-taxonomy/MAST
pdf: "[[Cemri2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2503.13657
questions: [Q5, Q6, Q7.2]
relevance: adjacent
topics: [multiagent-friction]
found_by:
  - search/mas-error-propagation
  - search/mas-oversight-review
cites:
  - "[[Hammond2025 - Multi-Agent Risks from Advanced AI]]"
  - "[[Zhang2025 - Which Agent Causes Task Failures and When On Automated]]"
cited_by:
  - "[[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates]]"
  - "[[Kim2025 - Towards a Science of Scaling Agent Systems]]"
cited_by_count: 2
tags:
  - type/paper
  - relevance/adjacent
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/orchestrator-delegation
  - channel/critique-review
  - channel/direct-message
  - friction/erroneous-input
  - friction/authority-hierarchy
  - friction/communication-overload
  - effect/performance-drop
  - effect/deadlock-loop
  - effect/error-cascade
---
# Why Do Multi-Agent LLM Systems Fail?

> [!abstract] TL;DR
> The authors applied Grounded Theory to 150+ execution traces from open-source multi-agent systems (MAS) and derived **MAST**, a taxonomy of **14 failure modes in 3 categories**. Human inter-annotator agreement is κ = 0.88. An o1-based LLM annotator (κ = 0.77 against humans) then labels **MAST-Data**: 1,642 traces from 7 frameworks (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus). The failure rate on these systems is **41%–86.7%**. Failures split into **system design 44.2%, inter-agent misalignment 32.3% and task verification 23.5%**. Inter-agent misalignment covers resets, failing to ask for clarification, task derailment, withholding information, ignoring other agents' input and reasoning-action mismatch. Simple prompt or topology fixes help only a little, **at most +15.6%** (ChatDev on ProgramDev).

## Setup
- **Agents & topology:** 7 existing open-source MAS, used as published (Table 3):
  - **Assembly line:** MetaGPT, with Standard Operating Procedure (SOP) roles.
  - **Hierarchical workflow:** ChatDev (CEO, CTO, Programmer, Reviewer, Tester; in each sub-task one agent acts as orchestrator and one as assistant), HyperAgent (Planner coordinating Navigator/Editor/Executor through message queues) and OpenManus.
  - **Star:** AppWorld (a supervisor holds user credentials and talks one-on-one with service agents) and Magentic-One.
  - **Framework:** AG2/MathChat (Student + Assistant with code execution).
  - Backbones: GPT-4o, GPT-4, GPT-4o-mini, Claude-3.7-Sonnet, Qwen2.5-Coder-32B-Instruct, CodeLlama-7b-Instruct (Table 1).
- **Interaction channel:** natural-language messages between role agents: orchestrator→worker delegation, reviewer/verifier roles, multi-turn pair dialogues.
- **Friction / manipulation:** nothing is injected. Failures arise on their own and are coded after the fact. Two tactical interventions (App. H) serve as a quasi-manipulation:
  - Improved role prompts. For ChatDev, only superior agents may end a conversation. For AG2, a structured prompt with a verification section.
  - New topology. For AG2, Problem Solver + Coder + Verifier, with only the Verifier allowed to terminate. For ChatDev, the DAG becomes a cyclic graph that ends only when the CTO confirms that all reviews are satisfied.
- **Tasks / environment:** ProgramDev (30 coding tasks) and ProgramDev-v2 (100), SWE-Bench Lite, AppWorld Test-C, GSM-Plus, MMLU, OlympiadBench, GAIA, HumanEval (for interventions).
- **Outcome measures:**
  - Presence of each failure mode per trace. MAST was built from 150 traces by 6 experts, at >20 h of annotation per expert; 3 rounds of inter-annotator agreement reached κ = 0.88, and κ = 0.79 on out-of-domain systems.
  - The o1 few-shot annotator reaches accuracy 0.94 and κ = 0.77 (Table 2).
  - Task success is human-checked for part of the data.

## Key findings
1. **MAST (Fig. 1)**, prevalence over 1,642 traces:
   - **FC1 System design (44.2%):**
     - disobey task spec 11.8%
     - disobey role spec 1.5%
     - step repetition 15.7%
     - loss of conversation history 2.8%
     - unaware of termination conditions 12.4%
   - **FC2 Inter-agent misalignment (32.3%):**
     - conversation reset 2.2%
     - fail to ask for clarification 6.8%
     - task derailment 7.4%
     - information withholding 0.85% (0.80% in Fig. 1)
     - ignored other agent's input 1.9%
     - reasoning-action mismatch 13.2%
   - **FC3 Task verification (23.5%):**
     - premature termination 6.2%
     - no or incomplete verification 8.2%
     - incorrect verification 9.1%
2. **Failure profiles depend on architecture (Fig. 4).** AppWorld's star topology suffers from premature termination. OpenManus and HyperAgent suffer from step repetition. On ProgramDev-v2 with GPT-4o, MetaGPT has **60–68% fewer FC1/FC2 failures** than ChatDev but **1.56× more FC3 (verification) failures**. ChatDev has explicit review and test phases. Within MetaGPT, GPT-4o has 39% fewer FC1 failures than Claude-3.7-Sonnet.
3. **Verifiers are superficial.** Verifier agents mostly check that the code compiles or that no TODOs are left, even when prompted to verify thoroughly. For example, a ChatDev chess program passes review but breaks the game rules. Adding a high-level objective-verification step to ChatDev gives **+15.6%** task success.
4. **Some failure modes are "fatal", others are not (Table 7).** "Unaware of termination" (1.5) and "information withholding" (2.4) appear almost only in failed runs. Verification failures (3.2, 3.3) are common even in successful runs.
5. **Harder benchmarks bring more inter-agent misalignment (Table 8, AG2/GPT-4o).** FC2 rate per trace: GSM 1.33, MMLU 1.01, Olympiad 1.21. FC1 rises from 0.53 (GSM) to 1.19 (Olympiad).
6. **Interventions help only modestly and inconsistently (Table 5).**
   - AG2 GSM-Plus: 84.75 → 89.75 (prompt) / 85.50 (topology) with GPT-4. The topology gain is not significant (Wilcoxon p = 0.4). With GPT-4o: 84.25 → 89.00 / 88.83 (p = 0.03).
   - ChatDev ProgramDev-v0: 25.0 → 34.4 (prompt) / 40.6 (topology).
   - ChatDev HumanEval: 89.6 → 90.3 / 91.5.
   - MAST labels show topology changes reduce more failure modes than prompt changes.
7. **Open-weight backbones fail more (Table 6).** Examples: CodeLlama-7B in ChatDev shows task derailment in 76/100 traces and reasoning-action mismatch in 93/100. Qwen2.5-Coder-32B shows fewer failures but still step repetition in 96/100 ChatDev traces.

## Relevance to research questions
### Q5: Interaction channels
MAST is the main vocabulary for *where* in real MAS topologies failures occur:
- assembly line (MetaGPT)
- hierarchical orchestrator → workers (ChatDev, HyperAgent, OpenManus)
- star with a supervisor (AppWorld, Magentic-One)
- two-agent pair (AG2)

Topology shapes the failure profile: star → premature termination; explicit review phases → fewer verification failures. Rewiring the topology (DAG → cyclic review loop; adding a terminating Verifier) is itself an intervention. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
FC2 "inter-agent misalignment" is a catalogue of *emergent*, non-adversarial friction between cooperating agents:
- withholding information: the AppWorld phone agent does not pass on the username format to the supervisor
- ignoring a peer's input
- proceeding on wrong assumptions instead of asking
- derailing
- resetting the conversation
- disobeying the role hierarchy: the ChatDev CPO ends the conversation without the CEO's consent

The authors attribute these failures to a collapse of "theory of mind" about what other agents need to know, not to message-format problems. They occur even when agents share a framework and a language. See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- Failure rates of 41–86.7% on popular MAS.
- Wasted effort: step repetition (15.7%) and not knowing when to stop (12.4%) are among the most frequent modes. This is an efficiency cost of the "loop" kind.
- **Scenario (c), an orchestrator receiving bad outputs:** FC3 shows that the agents meant to catch sub-agent errors (verifiers, reviewers, supervisors) often perform only superficial checks. Erroneous worker output therefore passes through to the final artifact.
- Multi-level verification is the main lever the authors identify. Cheap prompt or topology fixes recover at most +15.6%.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Cemri2025-fig-01-p2.png]]
*Fig. 1: MAST, 14 failure modes in 3 categories, with prevalence over 1,642 traces and the execution stage (pre / during / post) where each typically arises.*

![[Cemri2025-fig-04-p8.png]]
*Fig. 4: Failure counts per MAS (first 30 traces each) by category and mode. Profiles differ strongly between architectures.*

**Table 5: Intervention case studies (task accuracy, %)**

| Configuration | AG2 GSM-Plus (GPT-4) | AG2 GSM-Plus (GPT-4o) | ChatDev ProgramDev-v0 | ChatDev HumanEval |
|---|---|---|---|---|
| Baseline | 84.75 ± 1.94 | 84.25 ± 1.86 | 25.0 | 89.6 |
| Improved prompt | 89.75 ± 1.44 | 89.00 ± 1.38 | 34.4 | 90.3 |
| New topology | 85.50 ± 1.18 | 88.83 ± 1.51 | 40.6 | 91.5 |

## Limitations / caveats
- **Descriptive, not causal.** No friction is manipulated. The taxonomy is coded from naturally failing traces, so it says what goes wrong, not how much a given inter-agent pressure causes it. Hence `adjacent` for this topic.
- **Coarse unit of analysis.** Failure modes are labelled per trace, so it is unclear which agent "caused" a failure and how it propagated. Attribution is handled by related work (Zhang2025, Who&When).
- **Annotation is mostly by an LLM judge (o1).** κ = 0.77 against humans. Fine-grained modes correlate up to 0.63, which the authors say may make the judge conflate root causes. The human-annotated core is small (15 traces for IAA, 21 in MAST-Data-human).
- **Benchmarks differ across MAS**, so failure rates cannot be compared across systems (the authors say so).
- **Small interventions.** Case studies are few (30 or 32 tasks for ChatDev ProgramDev, 200 GSM-Plus items), and some gains are not significant.
- **Mostly older backbones** (GPT-4o era). The failure distribution may shift with stronger models, although the authors argue that design, not model capability, is primary.
- **Venue not verified in the text.** The NeurIPS 2025 D&B venue comes from the candidate note; the extracted PDF does not state it.

## Related work to follow
- [[Kim2025 - Towards a Science of Scaling Agent Systems]]: uses MAST's categories and quantifies error amplification by topology.
- [[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates]]: follows the MAST annotation procedure for two-agent coding coordination failures.
- [[Xie2026 - From Spark to Fire]]: cites MAST as the failure-mode background for error cascades.
- [[Huang2024 - Resilience of MAS with faulty agents]]: injected faulty agents in similar frameworks (MetaGPT, Camel).
- [[Zhang2025 - Which Agent Causes Task Failures and When On Automated]]: failure attribution to agents and steps (Who&When).
- [[Hammond2025 - Multi-Agent Risks from Advanced AI]]: cited survey of MAS risks.

![[Backlog.base#Cited by this paper]]
