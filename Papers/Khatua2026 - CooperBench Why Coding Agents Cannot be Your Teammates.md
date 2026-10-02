---
title: "CooperBench: Why Coding Agents Cannot be Your Teammates Yet"
citekey: Khatua2026
authors: [Arpandeep Khatua, Hao Zhu, Peter Tran, Arya Prabhudesai, Frederic Sadrieh, Johann K. Lieberwirth, Xinkai Yu, Yicheng Fu, Michael J. Ryan, Jiaxin Pei, Diyi Yang]
year: 2026
published: 2026-01-19
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2601.13295
arxiv: "2601.13295"
code: https://cooperbench.com
pdf: "[[Khatua2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2601.13295
questions: [Q5, Q6, Q7.2, Q21.1]
relevance: core
topics: [multiagent-friction, agent-competition]
found_by:
  - search/mas-error-propagation
cites:
  - "[[Cemri2025 - Why Do Multi-Agent LLM Systems Fail]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - q/21-1
  - subject/llm
  - subject/agent
  - channel/direct-message
  - friction/resource-contention
  - friction/communication-overload
  - friction/erroneous-input
  - friction/goal-conflict
  - effect/performance-drop
  - effect/token-cost
---
# CooperBench: Why Coding Agents Cannot be Your Teammates Yet

> [!abstract] TL;DR
> CooperBench has 652 tasks built from 12 real repositories in Python, TypeScript, Go and Rust. In each task two OpenHands coding agents implement *different* features on the same repository state, in isolated workspaces. Their patches are merged, and both features' tests must pass. 77.3% of tasks have overlapping ground-truth edits. The agents can talk only through a free-text, real-time messaging tool. **"Curse of coordination": two cooperating agents do much worse than one agent doing both features. GPT-5 drops from 0.48 to 0.28 and Claude Sonnet 4.5 from 0.47 to 0.26. On average 41% of Solo capability is lost (retention 0.59).** Communication uses up to 20% of actions and reduces naive merge conflicts, **but it does not improve end-to-end success** (net Δ −1.4 to +1.2 pp). Failures come from unmet expectations about the partner (42%), broken commitments (32%) and communication breakdown (26%).

## Setup
- **Agents & topology:**
  - Two peer agents, with no orchestrator. Each sees only its own feature description.
  - Five backbones in self-play: GPT-5, Claude Sonnet 4.5, MiniMax-M2, Qwen3-Coder-30B-A3B-Instruct, Qwen3-30B-A3B-Instruct-2507.
  - OpenHands v0.54, one Docker container per agent, at most 100 actions each.
  - Scaling probe with 2, 3 and 4 agents on 46 tasks.
- **Interaction channel:** an asynchronous direct-message tool. A message sent by one agent appears in the other's next prompt. No turn-taking and no shared view of the other's code. Coordination happens only through language, and the merged patch is the joint product.
- **Friction / manipulation:**
  - **Coop vs Solo.** The control is Solo: one agent is given both features.
  - **Communication ablation.** The messaging tool is banned ("no comm").
  - Built-in friction: the features are compatible but touch overlapping code, so the agents contend for the same files and lines under partial observability.
- **Tasks / environment:** 34 feature pools, with 2–12 features per pool and (n choose 2) tasks per pool. The features were written by 8 co-authors from real pull requests, with hand-written unit tests and gold joint patches. Merging uses git merge-file, then a union merge, then a small fine-tuned Qwen2.5-Coder-0.5B resolver for trivial conflicts.
- **Outcome measures:**
  - Success rate: both features' tests pass on the merged code.
  - Naive merge-conflict rate.
  - Difficulty-stratified Solo/Coop area under the curve (AUC) and retention = AUC_Coop / AUC_Solo.
  - Communication speech acts (plan, question, answer, update, ack).
  - A communication-error judge (precision-first LLM judge that needs quotes).
  - A failure-symptom taxonomy applied by a GPT-5 judge, which agreed with humans on 48/50 traces (96%, Wilson CI 86–99%).
  - Root causes coded by hand on 50 failed traces.

## Key findings
1. **Coordination gap (Fig. 4, Table 5).**

   | Model | Solo | Coop |
   |---|---|---|
   | GPT-5 | 0.48 | 0.28 |
   | Claude Sonnet 4.5 | 0.47 | 0.26 |
   | MiniMax-M2 | 0.36 | 0.14 |
   | Qwen3-Coder | 0.22 | 0.13 |
   | Qwen3-Instruct | 0.06 | 0.05 |

   - AUC retention: GPT-5 0.64, Claude 0.60, MiniMax 0.46 (worst), Qwen-Coder 0.63, Qwen-Instruct 0.68. Pooled: 0.59.
   - Coding strength does not predict coordination ability.
2. **Mid-difficulty crisis.** The Solo–Coop gap is largest for tasks of middle difficulty. On very easy and very hard tasks the two settings converge.
3. **More agents make it worse.** Success on 46 tasks falls from 68.6% (2 agents) to 46.5% (3) and 30.0% (4).
4. **Communication is costly and does not improve success (Fig. 5, Table 6).**
   - With vs without messaging, the final success difference is not significant: GPT-5 −0.1, Claude −1.4, MiniMax −0.9, Qwen-Coder −1.4, Qwen-Instruct +1.2 pp.
   - Messaging lowers naive merge conflicts (e.g. GPT-5 naive-merge success 13.9% → 20.4%, Table 6), but union and LLM merging remove that advantage.
   - Communication takes 20.0% of events for Claude, 16.3% for GPT-5 and 13.6% for MiniMax.
5. **What distinguishes good communication.**
   - Conflict-free trajectories have a higher Plan:Question ratio (2.04 vs 1.31).
   - A plan in the first turn cuts conflicts from 51.5% to 29.4%.
   - Successful trajectories mention more line numbers (32.6 vs 22.5) and file paths (13.1 vs 10.0).
   - Agents solve the *spatial* problem (who edits which lines) but not the *semantic* one (compatible designs and parameter values).
6. **Communication pathologies (Fig. 6).**
   - Repetition in 37.1% of Claude conversations.
   - Unresponsiveness to direct questions in 21.3% of MiniMax conversations.
   - Hallucinated or incorrect claims about code state in 6.9% (Claude) and 5.4% (MiniMax).
7. **Failure symptoms (Table 1):**
   - work overlap 33.2%
   - divergent architecture 29.7%
   - repetition 14.7%
   - unresponsiveness 8.7%
   - unverifiable claims 4.3%
   - broken commitment 3.7%
   - smaller categories below 2% each

   **Root causes (Table 2):** expectation failures 42%, where the partner's announced work is ignored; commitment failures 32%, where promised changes are missing; communication failures 26%.
8. **Rare coordination behaviours that do work:** role division with mutual confirmation, resource division at line level, and negotiation that offers fully specified alternatives. These appear mainly in successful runs.

## Relevance to research questions
### Q5: Interaction channels
The study isolates free-form peer messaging between two symmetric agents: asynchronous, with no orchestrator, no shared observation, and a merged artifact as the joint output. It removes the scaffolding (fixed workflows, supervisors, verifiers) that other MAS studies rely on. The channel ablation shows that simply having a messaging channel adds no value. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
- **Resource contention:** both agents need to edit the same code regions.
- **Communication overload:** repetitive status spam and unanswered questions.
- **Erroneous input from the partner:** unverifiable or false completion claims ("✓ added bypass at lines 100–104" when the code is absent) and broken commitments.
- Divergent design assumptions (a mild goal conflict).

The authors add a "trust paradox". Models trained to verify rather than trust cannot check a partner's claims under workspace isolation, yet collaboration requires trusting them. See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- Cooperation costs ~40% of Solo capability, and more when a third or fourth agent is added.
- Up to a fifth of the action budget goes to messages that do not raise success.
- **Relevance to scenario (c):** an agent that acts on a partner's false claims ("I added the handler at line 50") builds on work that does not exist. The paper shows this commitment failure accounts for about a third of failures. Receiving erroneous status reports is a main mechanism of the drop.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Khatua2026-fig-07-p7.png]]
*Fig. 4: Left, Solo vs Coop success per model (the "coordination gap"). Right, the gap by relative task difficulty, largest at mid difficulty.*

![[Khatua2026-fig-08-p8.png]]
*Fig. 5: (a) Messaging does not change success. (b) It reduces naive merge conflicts. (c) Share of events spent communicating, by speech act.*

**Table 5: Coordination retention by model (difficulty-stratified AUC)**

| Model | AUC Solo | AUC Coop | ΔAUC | Retention |
|---|---|---|---|---|
| GPT-5 | 0.506 | 0.325 | 0.181 | 0.64 |
| Claude Sonnet 4.5 | 0.469 | 0.283 | 0.186 | 0.60 |
| MiniMax-M2 | 0.374 | 0.171 | 0.203 | 0.46 |
| Qwen3-Coder | 0.236 | 0.148 | 0.088 | 0.63 |
| Qwen3-Instruct | 0.106 | 0.072 | 0.034 | 0.68 |
| Pooled | 0.338 | 0.200 | 0.138 | 0.59 |

## Limitations / caveats
- **The Solo baseline is not budget-matched.** Solo gives one agent both features and full visibility. Coop splits the work and imposes workspace isolation. The gap mixes coordination cost with partial observability, and each Coop agent has its own 100-action cap.
- **Friction is structural, not pressured.** There is no adversarial or stressed agent. The friction is task-embedded overlap plus imperfect communication, so it is `core` for effects on performance but says nothing about safety.
- **Only self-play is reported.** Cross-model pairs are possible in the design but not reported.
- **Some statistics are inconsistent.** The abstract says "30% lower", the introduction "around 50% lower", and the AUC analysis "41% lost". The reader should use the per-model numbers.
- **Mostly LLM-judged diagnostics.** Symptom labels come from a GPT-5 judge (validated on 50 traces) and root causes from 50 hand-read traces, a small sample for the percentage split.
- **One prompt.** The prompt was optimised iteratively against observed failures (App. D) and is fixed. Other prompts or protocols (e.g. mandatory contracts) might narrow the gap.
- **Small scaling probe.** The 2→4 agent experiment covers only 46 tasks from 3 pools, and the model is not stated in the text.

## Related work to follow
- [[Cemri2025 - Why Do Multi-Agent LLM Systems Fail]]: MAST failure taxonomy; the annotation procedure is modelled on it.
- [[Kim2025 - Towards a Science of Scaling Agent Systems]]: coordination tax and degradation of MAS vs a single agent on sequential tasks.
- [[Gao2025 - Single-agent or Multi-agent Systems Why Not Both]]: when single strong agents match MAS.

![[Backlog.base#Cited by this paper]]
