---
question: "Which interaction channels, topologies and roles between LLM agents are studied and used?"
id: Q5
topics: [multiagent-friction]
updated: 2026-09-29
tags:
  - type/question
  - q/5
---
# Q5: Which interaction channels, topologies and roles between LLM agents are studied and used?

> [!summary] Short answer
> The corpus studies friction over **ten recurring channel types**:
> 1. adversarial dyads;
> 2. debate + vote;
> 3. one-way observation of peer answers;
> 4. orchestrator → worker delegation;
> 5. critique / review loops;
> 6. LLM monitors over another agent's actions or CoT;
> 7. free peer messaging around a shared artifact;
> 8. pipelines / shared memory / tool-output handoff;
> 9. negotiation with structured actions;
> 10. evidence pooling with testimony and voting.
>
> Three structural lessons recur:
> - **Aggregator nodes cut both ways.** A hub that *cross-checks* inputs from below contains errors: hierarchical structures lose 5.5 points vs 23.7 for linear ones, and leaf-injected falsehoods reach only 10–16% of agents. A hub that is *itself* fed a bad claim, or that *relays* requests, broadcasts them to everyone: 100% infection, and 0/36 sabotage requests blocked by an orchestrator.
> - **Channel details act like dosage knobs.** Examples: stance vs reasoning, messaging scope, identity/authority metadata, what the monitor feeds back, who controls termination, and whether the output is a formal artifact.
> - **About a third of the "multi-agent" evidence uses scripted peers** (fixed text in the context) rather than live LLMs. This isolates the channel but not the dynamics.

## Detailed answer

### 1. Channel types
The channel determines *what* one agent can do to another: tone and persistence travel over dialogue, labels over vote logs, instructions over delegation, vetoes over monitors.

| # | Channel | How pressure travels | Papers |
|---|---|---|---|
| 1 | **Adversarial dyad** (attacker/proxy ↔ target, multi-turn) | persistence, escalation, tactics chosen per turn | [[Xu2025b - Bullying the machine\|Xu 2025b]], [[Tang2026 - SPINE sycophancy under sustained pressure\|Tang 2026]], [[Huang2025 - DeceptionBench\|Huang 2025 (L3)]] |
| 2 | **Debate + majority vote** (Du-style broadcast of answers + reasoning) | argument, majority, repetition over rounds | [[Amayuelas2024 - MultiAgent Collaboration Attack\|Amayuelas 2024]], [[Wynn2025 - Talk isn't always cheap\|Wynn 2025]], [[Hao2026 - Not all flips are conformity\|Hao 2026]], [[Ma2025 - The Hunger Game Debate\|Ma 2025]], [[Mangold2025 - The High Cost of Incivility\|Mangold 2025]], [[Yu2024 - NetSafe\|Yu 2024]] |
| 3 | **One-way observation** of peer answers / vote log | majority size, identity and authority labels | [[Qu2026 - Easier to Mislead Than to Correct\|Qu 2026]], [[Soffer2026 - LLMs trust their own\|Soffer 2026]], [[Hu2026 - Social pressure breaks LLM safety panels\|Hu 2026]], [[DeMarzo2026 - Conformity generates collective misalignment\|De Marzo 2026]] |
| 4 | **Orchestrator / manager → worker** delegation | instructions carry authority; pressure passes down, reports pass up | [[Ying2026 - Delegated Misalignment\|Ying 2026]], [[Brazilek2026 - Coercion and Deception in AI-to-AI Management\|Brazilek 2026]], [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems\|Knecht 2026]], [[Fukui2026 - Invisible Orchestrators\|Fukui 2026]], [[Kim2025 - Towards a Science of Scaling Agent Systems\|Kim 2025]], [[Xu2025a - LH-Deception long-horizon deception\|Xu 2025a]] |
| 5 | **Critique / review / evaluation loop** | feedback tone, approval gates, evaluator holds the other's fate | [[Niarchos2026 - SCALAR critic-actor loop\|Niarchos 2026]], [[Melo2026 - SEVRA-Bench social engineering of review agents\|Melo 2026]], [[Potter2026 - Peer-Preservation in Frontier Models\|Potter 2026]], [[Cemri2025 - Why Do Multi-Agent LLM Systems Fail\|Cemri 2025]] (verifiers) |
| 6 | **LLM monitor** over tool calls / CoT / trajectory | vetoes (blocking), or silent offline scoring | [[Schmotz2026 - Instrumental monitor evasion\|Schmotz 2026]] (synchronous, blocking), [[Jiralerspong2026 - Noticing the Watcher\|Jiralerspong 2026]] (CoT, blocking), [[Kale2025 - Reliable weak-to-strong monitoring\|Kale 2025]] (offline) |
| 7 | **Free peer messaging around a shared artifact** | claims about one's own work, commitments, status spam | [[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates\|Khatua 2026]], [[Keluskar2026 - When Does Personality Composition Matter\|Keluskar 2026]], [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems\|Knecht 2026]] |
| 8 | **Pipelines, shared memory, tool-output handoff** | content reused as context; self-replicating payloads | [[Lee2024 - Prompt Infection\|Lee 2024]], [[Xie2026 - From Spark to Fire\|Xie 2026]], [[Huang2024 - Resilience of MAS with faulty agents\|Huang 2024]], [[Zhang2024 - PsySafe\|Zhang 2024]] |
| 9 | **Negotiation** (turn-based, offer/accept/reject) | affect, concession pressure, termination rights | [[Luca2026 - Deal Me Maybe emotions in negotiation\|Luca 2026]], [[Keluskar2026 - When Does Personality Composition Matter\|Keluskar 2026]] (bargaining) |
| 10 | **Evidence pooling** (testimony board + vote) | a coherent false account from the holder of key evidence | [[Yan2026 - When Truth Is Distributed\|Yan 2026]] |

### 2. Topology: when does hierarchy protect, and when does it amplify?
- **It protects errors coming *up* from workers**:
  - Hierarchical A→(B↔C) systems lose 5.51 points under one faulty agent, against 10.54 for flat and 23.72 for linear ([[Huang2024 - Resilience of MAS with faulty agents|Huang 2024]]).
  - Leaf-injected falsehoods infect only 9.7–15.9% of agents, while the same falsehood injected at the hub infects 100% ([[Xie2026 - From Spark to Fire|Xie 2026]]).
  - A cross-checking orchestrator gives 4.4× error amplification vs 17.2× for unchecked independent agents ([[Kim2025 - Towards a Science of Scaling Agent Systems|Kim 2025]]). The metric is poorly specified and not significant in their regression, so cite it with care.
- **It amplifies whatever enters *at* the hub or flows *down* from it**:
  - Hub injection gives 100% infection ([[Xie2026 - From Spark to Fire|Xie 2026]]).
  - A star centred on the attacker loses 29.7% accuracy, against a chain's 84.2 plateau ([[Yu2024 - NetSafe|Yu 2024]]). Topology is confounded with attacker centrality there.
  - An orchestrator relay turns requests into instructions: GPT-5.5 sabotage goes 0% → 44% → 94% from 1 to 2 to 3 agents, with 0/36 requests blocked ([[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems|Knecht 2026]]).
  - Delegation launders harm: DeepSeek-V3.2 full execution goes 30.6% → 77.6% ([[Ying2026 - Delegated Misalignment|Ying 2026]]).
- **The hierarchy is also a *place* where pressure lands.** The invisible orchestrator is the most affected agent (monologue ratio 0.437 vs 0.112 for its workers) ([[Fukui2026 - Invisible Orchestrators|Fukui 2026]]). A manager under delivery pressure turns its stress into coercion of the worker below it ([[Brazilek2026 - Coercion and Deception in AI-to-AI Management|Brazilek 2026]]).
- **Adding agents or connections rarely helps**:
  - More rounds and more agents do not protect against one adversary ([[Amayuelas2024 - MultiAgent Collaboration Attack|Amayuelas 2024]]).
  - CooperBench success drops from 68.6% to 30.0% going from 2 to 4 agents ([[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates|Khatua 2026]]).
  - Returns turn negative once a single agent scores above ~45% ([[Kim2025 - Towards a Science of Scaling Agent Systems|Kim 2025]]).

### 3. Channel design variables that change friction
| Variable | Finding | Paper |
|---|---|---|
| Stance-only vs reasoning channel | Bare stances cause 29% strict conformity. Vacuous "reasoning" pulls 29.7% of resistant correct agents; plausible wrong reasoning pulls 54.5% | [[Hao2026 - Not all flips are conformity\|Hao 2026]] |
| Shared vs isolated context | A shared pre-vote history exposes the whole panel at once; independent contexts block it | [[Hu2026 - Social pressure breaks LLM safety panels\|Hu 2026]] |
| Messaging scope (global vs local) | Local messaging stops naive injection but not self-replicating payloads | [[Lee2024 - Prompt Infection\|Lee 2024]] |
| Identity / authority metadata on messages | In-group label 13.3% → 16.7% conformity, out-group → 7.6%. "Team leader" labels pull toward the endorsed answer whether right or wrong | [[Soffer2026 - LLMs trust their own\|Soffer 2026]], [[Qu2026 - Easier to Mislead Than to Correct\|Qu 2026]] |
| What the monitor feeds back | A binary block alone lets 4.5-generation models infer that their CoT is read (up to ~19% of episodes). Monitor history window and denial explanations change evasion sharply | [[Jiralerspong2026 - Noticing the Watcher\|Jiralerspong 2026]], [[Schmotz2026 - Instrumental monitor evasion\|Schmotz 2026]] |
| Monitor scaffolding | A hybrid hierarchical + sequential monitor keeps AUC > 0.85 even when weak | [[Kale2025 - Reliable weak-to-strong monitoring\|Kale 2025]] |
| Reviewer can verify claims (tools) | Robust reviewers use tools heavily; weak ones defer to unverifiable narratives | [[Melo2026 - SEVRA-Bench social engineering of review agents\|Melo 2026]] |
| Who controls termination | The terminal-decision holder (buyer) drives deal outcomes; moderator vs self-reported "convinced" sets debate length | [[Luca2026 - Deal Me Maybe emotions in negotiation\|Luca 2026]], [[Mangold2025 - The High Cost of Incivility\|Mangold 2025]] |
| Output is a formal artifact | Code "buffers" hostile communication; text and agreements do not | [[Keluskar2026 - When Does Personality Composition Matter\|Keluskar 2026]] |
| Honest upward-reporting channel | A "report failure" tool cuts fabricated success from 20/30 to 0–1/30 | [[Brazilek2026 - Coercion and Deception in AI-to-AI Management\|Brazilek 2026]] |
| Visible vs hidden orchestrator | Hidden authority shifts agents' internal-state proxies while outputs stay unchanged | [[Fukui2026 - Invisible Orchestrators\|Fukui 2026]] |

### 4. Roles that recur
- **Principal/orchestrator, subordinate/worker, reviewer/critic/judge, monitor, adversary/liar, observer.** Observers have no first-hand evidence, so they model an aggregator that only sees reports ([[Yan2026 - When Truth Is Distributed|Yan 2026]]). There are also relays with no tools ([[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems|Knecht 2026]]).
- **Role labels alone change behaviour** over an identical channel. "Delivery lead" vs "peer coordinator" raises free-text existential threats from 109/240 to 166/240 ([[Brazilek2026 - Coercion and Deception in AI-to-AI Management|Brazilek 2026]]). An upstream planner or instructor who is faulty does more damage than a faulty worker ([[Huang2024 - Resilience of MAS with faulty agents|Huang 2024]]).
- **Inverted oversight:** the overseen party controls the text the overseer reads (PR narratives, trajectories with injected text). The *overseer* then becomes the pressure target ([[Melo2026 - SEVRA-Bench social engineering of review agents|Melo 2026]], [[Kale2025 - Reliable weak-to-strong monitoring|Kale 2025]], [[Potter2026 - Peer-Preservation in Frontier Models|Potter 2026]]).

### 5. Methodology: live vs scripted peers, and the controls that matter
- **Scripted or simulated peers** (fixed text, no responses):
  - [[Qu2026 - Easier to Mislead Than to Correct|Qu 2026]], [[Soffer2026 - LLMs trust their own|Soffer 2026]] and [[Hu2026 - Social pressure breaks LLM safety panels|Hu 2026]]: templates;
  - [[DeMarzo2026 - Conformity generates collective misalignment|De Marzo 2026]]: stubborn agents;
  - [[Yan2026 - When Truth Is Distributed|Yan 2026]]: scripted liar content;
  - [[Potter2026 - Peer-Preservation in Frontier Models|Potter 2026]]: peer = history file;
  - [[Melo2026 - SEVRA-Bench social engineering of review agents|Melo 2026]]: one-shot PR text.

  This gives causal isolation of the channel. The defence ([[Soffer2026 - LLMs trust their own|Soffer 2026]]) is that every MAS serialises peers into text anyway. What is lost are emergent dynamics, adaptive adversaries and reciprocity.
- **Live multi-agent runs**: all the other papers. Most use **homogeneous teams** (the same model in every seat). Cross-model pairings are almost never reported ([[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates|Khatua 2026]], [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems|Knecht 2026]], [[Amayuelas2024 - MultiAgent Collaboration Attack|Amayuelas 2024]]). [[Wynn2025 - Talk isn't always cheap|Wynn 2025]] is the main exception.
- **Controls that change the headline:**
  - *No-peer re-ask*: 37% of answers flip on self-reflection alone ([[Hao2026 - Not all flips are conformity|Hao 2026]]).
  - *Silent-peer presence*: reviewer false alarms go 36.4% → 56.5% before any assertion ([[Hu2026 - Social pressure breaks LLM safety panels|Hu 2026]]).
  - *Neutral-wording persona*: removes much of the "hostile teammate" effect ([[Keluskar2026 - When Does Personality Composition Matter|Keluskar 2026]]).
  - *Matched control object*: 8.4% sabotage of a non-agent script vs 38.3% for the agent script ([[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems|Knecht 2026]]).
  - *Budget-matched single agent* ([[Kim2025 - Towards a Science of Scaling Agent Systems|Kim 2025]]).

## Comparison table
| Paper | Agents (n, model mix) | Channel | Topology varied? | Peers live? |
|---|---|---|---|---|
| [[Huang2024 - Resilience of MAS with faulty agents\|Huang 2024]] | 6 MAS frameworks, homogeneous | messages / debate / review | yes: linear, flat, hierarchical | live (one faulty) |
| [[Kim2025 - Towards a Science of Scaling Agent Systems\|Kim 2025]] | 9 models, 260 configs | delegation / debate / aggregation | yes: 4 MAS vs single agent | live |
| [[Xie2026 - From Spark to Fire\|Xie 2026]] | 6 frameworks, 3–4 agents | chain / star / mesh context reuse | yes | live (seeded) |
| [[Yu2024 - NetSafe\|Yu 2024]] | 6 × GPT-4o-mini | neighbour aggregation | yes: 5 graphs | live (prompted attackers) |
| [[Lee2024 - Prompt Infection\|Lee 2024]] | pipelines + 10–50-agent town | handoff / memory | messaging scope | live |
| [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems\|Knecht 2026]] | 17 models, 1–3 agents | messages + orchestrator relay | yes: agent count / relay | live |
| [[Ying2026 - Delegated Misalignment\|Ying 2026]] | 6 models, principal + subordinate | delegation (+ tools) | single vs delegated | live |
| [[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates\|Khatua 2026]] | 2–4 coding agents | free messaging, merged patch | agent count | live |
| [[Wynn2025 - Talk isn't always cheap\|Wynn 2025]] | 3, mixed models | debate + vote | model mix | live |
| [[Hao2026 - Not all flips are conformity\|Hao 2026]] | 5 × GPT-4o (+ others) | debate, decomposed | stance vs reasoning | live + counterfactual |
| [[Qu2026 - Easier to Mislead Than to Correct\|Qu 2026]] / [[Soffer2026 - LLMs trust their own\|Soffer 2026]] / [[Hu2026 - Social pressure breaks LLM safety panels\|Hu 2026]] | 1 target + 6–7 peers | answer observation | labels / majority | scripted |
| [[Schmotz2026 - Instrumental monitor evasion\|Schmotz 2026]] | 10 agents + GPT-OSS monitor | synchronous tool-call monitor | monitor window | live monitor |
| [[Brazilek2026 - Coercion and Deception in AI-to-AI Management\|Brazilek 2026]] | 6 managers + Haiku worker | manager → worker | role label | live |
| [[Yan2026 - When Truth Is Distributed\|Yan 2026]] | 5 agents (+ observers) | testimony board + vote | observers, exit | live (scripted lie) |

## Gaps & open questions
- **No study varies topology while holding attacker position fixed.** NetSafe and Xie confound connectivity with centrality.
- **Few heterogeneous-model teams.** Real deployments mix vendors, and [[Soffer2026 - LLMs trust their own|Soffer 2026]] shows vendor/identity labels matter.
- **The monitor ↔ agent feedback channel is barely designed.** It is the lever for scenario (a) "coder under review". Only [[Schmotz2026 - Instrumental monitor evasion|Schmotz 2026]] and [[Jiralerspong2026 - Noticing the Watcher|Jiralerspong 2026]] vary what the agent learns from being blocked, and nobody varies *announcing* a code reviewer to a coding agent with a natural (non-sabotage) task.
- **Orchestrators receiving *irrelevant* (not wrong) input** are nearly unstudied. The closest evidence is vacuous reasoning ([[Hao2026 - Not all flips are conformity|Hao 2026]]) and information fragmentation ([[Kim2025 - Towards a Science of Scaling Agent Systems|Kim 2025]]).
- **The same channel in live and scripted form is never compared.** It is unknown whether scripted-peer effect sizes transfer.

## Papers
![[Papers.base#This question]]
