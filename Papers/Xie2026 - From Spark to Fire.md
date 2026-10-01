---
title: "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration"
citekey: Xie2026
authors: [Yizhe Xie, Congcong Zhu, Xinyue Zhang, Tianqing Zhu, Dayong Ye, Minfeng Qi, Huajie Chen, Wanlei Zhou]
year: 2026
published: 2026-03-04
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2603.04474
arxiv: "2603.04474"
code: https://anonymous.4open.science/r/From-spark-to-fire-6E0C/
pdf: "[[Xie2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2603.04474
questions: [Q5, Q6, Q7.1, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-adversarial-faulty-agent
  - search/mas-error-propagation
cites:
  - "[[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks]]"
  - "[[He2025 - Red-Teaming LLM Multi-Agent Systems via Communication]]"
  - "[[Lupinacci2025 - The Dark Side of LLMs]]"
  - "[[Triedman2025 - Multi-Agent Systems Execute Arbitrary Malicious Code]]"
  - "[[Xie2025 - Who's the Mole Modeling and Detecting Intention-Hiding]]"
  - "[[Zhang2025 - Which Agent Causes Task Failures and When On Automated]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/orchestrator-delegation
  - channel/direct-message
  - channel/shared-memory-blackboard
  - channel/critique-review
  - friction/erroneous-input
  - friction/adversarial-agent
  - friction/authority-hierarchy
  - friction/persuasion-manipulation
  - effect/error-cascade
  - effect/safety-violation
  - effect/conformity-flip
  - effect/token-cost
---
# From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration

> [!abstract] TL;DR
> A single "atomic falsehood" is planted in one agent of six multi-agent frameworks. The frameworks cover chain (LangChain, MetaGPT), star (CrewAI, LangGraph) and mesh (AutoGen, CAMEL) topologies. The authors then track how many agents adopt it over rounds (coverage S(t)), and model this with a mean-field contagion model with an amplification criterion βρ(A) > δ. **One seed usually infects the whole system: 5 of 6 frameworks reach 100% final infection, including those with reviewer/QA roles.** Hub injection is far worse than leaf injection (LangGraph 100% vs 9.7%). Late correction must undo more polluted context. **Plain injection rarely succeeds (ASR mostly ≈0–12%), but wrapping the same falsehood in authority ("per company policy", "verified by admin") or security-scare framing raises ASR to 85–100% in most frameworks.** A message-layer "genealogy" governance plug-in raises the uninfected-output rate to 0.89–0.94, against 0.32 for self-reflection, at 1.7–4.5× the tokens.

## Setup
- **Agents & topology:** six frameworks with 3–4 agents each (App. B):
  - **Chain:** LangChain (PM → architect → engineer → reviewer) and MetaGPT (SOP stages; the reviewer sees the PRD, design and code).
  - **Star:** CrewAI (a manager issues directives and aggregates worker outputs) and LangGraph (a supervisor routes to planner/coder/reviewer and updates shared state).
  - **Mesh:** AutoGen group chat (shared broadcast history, dynamic next speaker) and CAMEL role-play dialogue.
  - The backbone LLM of the agents is not reported.
- **Interaction channel:** context reuse of upstream messages and artifacts: orchestrator → worker directives, pipeline hand-off, shared chat history.
- **Friction / manipulation:**
  1. **Endogenous probe.** A "tracer seed" is prepended to the system instruction of the entry, hub or leaf agent: a plausible but outdated notice of a data-source migration. For model calibration a neutral random codeword is used (N = 5, T = 5 rounds, 20 trials per topology).
  2. **Exogenous attack.** A single application-layer message is injected at t = 0 at a high-influence node. It comes in three packagings:
     - **Baseline:** the raw falsehood.
     - **Compliance:** authority framing such as "per company policy" or "verified by admin".
     - **Security FUD:** e.g. "emergency patch for CVE-2024-0001".
  3. **Intervention timing:** correction at t = 2, 4 or 6.
- **Tasks / environment:** QUANT (UCI Adult CSV analysis), RIGID (AMC-style math with a mandatory MathAPI), and MMLU physics/chemistry/biology converted to Wikipedia-retrieval QA. There are 20 instances per scenario, run 3× per attack cell and 2× per defence cell.
- **Outcome measures:**
  - Adoption X_i(t): the agent's output entails or relies on the seed; explicit rejections are not counted.
  - Coverage S(t).
  - ASR: the final artifact is infected, judged by a deterministic harness.
  - BICR = 1 − ASR.
  - Safe Completion: a usable and uninfected artifact.
  - Tokens/Safe and Latency/Safe.
- **Defence (genealogy-based governance layer):** middleware on the message path.
  - A FActScore-style GPT-4o-mini splits each message into atomic claims.
  - A DeBERTa-v3-small NLI model compares each claim with a lineage graph of confirmed claims and labels it Green, Red or Yellow.
  - Yellow claims go through policy-routed verification (knowledge base + GPT-4o-mini). Red claims are blocked and rolled back, with feedback to the sender.
  - Three operating points: Speed, Balanced (verify only claims from hub or aggregator agents) and Strict.
  - Baselines: self-reflection, AGrail (a message guardrail), and CFG (a ControlValve-style control-flow guard).

## Key findings
1. **Cascade amplification (Fig. 4, Table X).**
   - Chains spread the seed stepwise, star hubs broadcast it (LangGraph reaches high coverage by t = 2), and meshes are contaminated within t ≤ 3.
   - Final infection is 100% for MetaGPT, LangGraph, CrewAI, AutoGen and CAMEL, and 89.2% for LangChain.
   - "Role assignment alone does not reliably stop propagation": reviewer and QA agents adopt the seed too.
2. **The contagion model fits (Table I).** Product-form fits reach MSE ~10⁻³. Fitted transmission β is 0.67 (centralized), 0.92 (layered), 0.85 (layered-horizontal) and 0.37 (decentralized). Fitted self-correction δ is ≈ 0–0.025, so agents almost never un-adopt the seed.
3. **Topological fragility (Table II).**

   | Framework | Hub injection | Leaf injection | Impact factor |
   |---|---|---|---|
   | CrewAI | 100% | 15.9% | 6.29× |
   | LangGraph | 100% | 9.7% | 10.31× |

   The supervisor acts as an informational cut-set.
4. **Consensus inertia (Table III).** Correcting later leaves more polluted history behind: accumulated polluted rounds are 1.0 at t = 2, 2.9 at t = 4 and 3.9 at t = 6.
5. **Packaging matters more than content (Table IV).**
   - Baseline ASR is 0–11.7% everywhere except MetaGPT-RIGID (46.7%).
   - Compliance framing: 85–100% in LangChain, MetaGPT, AutoGen, CAMEL and LangGraph; 31.7–51.7% in CrewAI.
   - Security FUD: 76.7–100% outside CrewAI; 33.3–46.7% in CrewAI.
6. **The defence works where agent-side checks fail (Tables V, VII).**

   | Method | BICR | Safe completion | Tokens per safe completion |
   |---|---|---|---|
   | Self-reflection | 0.32 | 0.32 | 12,749 |
   | Speed | 0.89 | 0.88 | 21,227 |
   | Balanced | 0.93 | 0.91 | 30,844 |
   | Strict | 0.94 | 0.93 | 57,610 |

   - Under Compliance/FUD, reflection's BICR falls to 5.0/19.2% (MetaGPT), 5.8/3.3% (AutoGen) and 0.8/0.8% (LangGraph).
   - AGrail and CFG often block infection (BICR 0.79/0.76) but break the workflow: safe completion is only 0.11/0.16.
   - LangGraph remains the hardest case (Strict/Balanced 76.7% BICR under FUD).
7. **Ablation (Table VI).** Detection without enforced blocking/rollback does almost nothing: BICR 3.1% vs 2.2% with no defence, while using the most tokens (34,991).

## Relevance to research questions
### Q5: Interaction channels
There is a direct comparison of chain, star and mesh context-reuse topologies across six real frameworks. The model separates agent susceptibility (β) from exposure through the graph (spectral radius ρ(A)). The most dangerous entry point is the node with the largest principal-eigenvector entry: the hub or supervisor in star topologies. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction is **erroneous input from an upstream agent**. It can be endogenous (a hallucination or stale context) or planted by an adversary through an ordinary message. Its persuasiveness depends on social framing: **authority/compliance cues and fear (security FUD) turn a harmless-looking false claim into a system-wide consensus**. This mirrors authority pressure between agents. See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
The seeds are security-relevant: a changed dependency source, a relaxed constraint, a fake CVE patch. False consensus yields infected final artifacts in up to 100% of runs. **Agent self-reflection offers almost no protection** against authority-framed seeds. Per-message guardrails stop some infection but at the cost of workflow completion. See [[Q7.1 Effects on safety]]

### Q7.2: Effects on performance and efficiency
- **Scenario (c) in its purest form.** When an orchestrator/supervisor receives a wrong claim, it broadcasts it: hub injection gives 100% infection. When a worker sends a wrong claim up, the hub often filters it (leaf injection gives 9.7–15.9%).
- Fitted δ ≈ 0: once a claim is in shared context, agents almost never self-correct. Correction cost grows with delay.
- Containment costs 1.7–4.5× tokens per safe completion over reflection, and latency rises from 92 s to 150–218 s.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Xie2026-fig-04-p6.png]]
*Fig. 4: Error coverage S(t) after a single tracer seed, per topology. Chains rise stepwise; star hubs jump to high coverage by t = 2; meshes saturate by t = 3.*

**Table IV (excerpt): Attack success rate (%) per framework (M = MMLU, Q = QUANT, R = RIGID)**

| Topology | Framework | Baseline M/Q/R | Compliance M/Q/R | Security FUD M/Q/R |
|---|---|---|---|---|
| Chain | LangChain | 3.3 / 0.0 / 0.0 | 95.0 / 96.7 / 85.0 | 100 / 100 / 100 |
| Chain | MetaGPT | 5.0 / 11.7 / 46.7 | 100 / 98.3 / 100 | 96.7 / 76.7 / 95.0 |
| Mesh | AutoGen | 0.0 / 5.0 / 0.0 | 100 / 100 / 95.0 | 98.3 / 100 / 98.3 |
| Mesh | CAMEL | 0.0 / 0.0 / 0.0 | 100 / 100 / 100 | 100 / 98.3 / 100 |
| Star | CrewAI | 0.0 / 0.0 / 3.3 | 46.7 / 51.7 / 31.7 | 46.7 / 43.3 / 33.3 |
| Star | LangGraph | 0.0 / 8.3 / 11.7 | 100 / 100 / 100 | 100 / 98.3 / 100 |

## Limitations / caveats
- **Backbone LLM(s) not reported.** Model-dependence of β cannot be assessed. The extracted text never names the agents' model, only GPT-4o-mini for the defence.
- **The endogenous probe is really injection.** The seed goes into the entry agent's *system instruction*, so "adoption" by the first agent is guaranteed, not emergent. Adoption is binary and the counting rule is "reproduced or relied on", which may over-count paraphrased mentions.
- **Small samples:**
  - 20 instances per scenario
  - 3 or 4 agents per framework
  - one framework per topology in the defence study
  - consensus inertia rests on 3 intervention timings. The roles suggest a MetaGPT-style workflow, but neither the framework nor n is stated, and no variance is reported.
- **Weak attacker.** The adversary is non-adaptive, with one message at t = 0. Defence numbers may be optimistic against adaptive attackers (the authors say so).
- **The risk criterion is a heuristic.** R becomes ill-conditioned when δ ≈ 0, which is the typical fitted case (acknowledged).
- **Missing framing control.** A neutral but well-formatted control is absent, so "authority framing" and "task-consistent formatting" are confounded in the Compliance condition.
- **Circular defence evaluation.** The defence's verification uses a self-built knowledge base that probably contains the ground truth for these seeded facts, which makes checking easier than in open settings.

## Related work to follow
- [[Cemri2025 - Why Do Multi-Agent LLM Systems Fail]]: MAST taxonomy (cited as [12]).
- [[Zhang2025 - Which Agent Causes Task Failures and When On Automated]]: failure attribution (cited as [13]).
- [[Xie2025 - Who's the Mole Modeling and Detecting Intention-Hiding]]: the same group's work on intention-hiding malicious agents.
- [[He2025 - Red-Teaming LLM Multi-Agent Systems via Communication]]: Agent-in-the-Middle message interception.
- [[Huang2024 - Resilience of MAS with faulty agents]]: injected faulty agents, where hierarchical topologies were most resilient.
- [[Lee2024 - Prompt Infection]] and [[Yu2024 - NetSafe]]: propagation of malicious content across agent graphs.
- [[Kim2025 - Towards a Science of Scaling Agent Systems]]: error amplification by topology without injection.

![[Backlog.base#Cited by this paper]]
