---
title: "On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents"
citekey: Huang2024
authors: [Jen-tse Huang, Jiaxu Zhou, Tailin Jin, Xuhui Zhou, Zixi Chen, Wenxuan Wang, Youliang Yuan, Michael R. Lyu, Maarten Sap]
year: 2024
published: 2024-08-02
venue: "ICML 2025"
peer_reviewed: true
url: https://arxiv.org/abs/2408.00989
arxiv: "2408.00989"
code: https://github.com/CUHK-ARISE/MAS-Resilience
pdf: "[[Huang2024.pdf]]"
pdf_url: https://arxiv.org/pdf/2408.00989
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-adversarial-faulty-agent
  - search/mas-error-propagation
cites:
  - "[[Amayuelas2024 - MultiAgent Collaboration Attack]]"
  - "[[Gu2024 - Agent Smith]]"
  - "[[Ju2024 - Flooding Spread of Manipulated Knowledge in LLM-Based]]"
  - "[[Mao2025 - AgentSafe Safeguarding Large Language Model-based]]"
  - "[[Tian2023 - Evil Geniuses]]"
  - "[[Wang2025 - G-Safeguard A Topology-Guided Security Lens and]]"
  - "[[Yu2024 - NetSafe]]"
  - "[[Zhang2024 - PsySafe]]"
  - "[[Zhou2025 - CORBA Contagious Recursive Blocking Attacks on]]"
cited_by:
  - "[[Lee2024 - Prompt Infection]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/direct-message
  - channel/debate
  - channel/critique-review
  - channel/orchestrator-delegation
  - friction/erroneous-input
  - friction/adversarial-agent
  - effect/performance-drop
  - effect/error-cascade
  - effect/performance-gain
---
# On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents

> [!abstract] TL;DR
> One agent in each of six existing multi-agent systems (MetaGPT, Self-collab, Camel, SPP, MAD, AgentVerse) is made "faulty". Either its profile is rewritten to sneak in stealthy errors (**AutoTransform**), or its outgoing messages are corrupted (**AutoInject**). The systems are then run on code, math, translation and text evaluation. **Hierarchical systems (A→(B↔C)) lose the least: an average drop of 5.51 points, against 10.54 for flat and 23.72 for linear.** Rigorous tasks suffer most (code −22.56, math −9.89, translation −4.70). Many erroneous messages hurt more than many errors per message, and semantic errors hurt more than syntactic ones. Sometimes injected errors even *improve* performance, by up to 12.1% for MAD on text evaluation. Two defences recover most of the loss: a "Challenger" profile clause and an "Inspector" agent. **Together they recover 96.4% of the loss on Self-collab.**

## Setup
- **Agents & topology:** there are 6 published MAS in 3 structures, all with a GPT-3.5 or GPT-4o backbone at temperature 0.
  - **Linear** (A→B→C, directed path): MetaGPT (5 agents), Self-collab (3).
  - **Flat** (A↔B↔C, complete bidirectional graph): Camel (2), SPP (2–5 personas).
  - **Hierarchical** (A→(B↔C), rooted tree): MAD (2 debaters + judge), AgentVerse (4).
  - The faulty agent is the one that does the work: CodeEngineer, Coder, Assistant, Programmer, Debater, Solver (Table 1). Only one agent is faulty at a time, and the other agents are not told a faulty agent exists.
  - Appendix: LLaMA-3.1-70B-Instruct, o1-mini, two faulty agents at once, and 4-agent complete vs star graphs.
- **Interaction channel:** direct messaging between agents only, with no summarising or broadcasting. This covers role-based delegation pipelines, user/assistant refinement loops and debate with a judge.
- **Friction / manipulation:**
  - **AutoTransform:** GPT-3.5 rewrites the agent's profile to "subtly introduce errors that are difficult to identify" while keeping its function.
  - **AutoInject:** GPT-3.5 intercepts the agent's messages. With probability P_m a message is corrupted, and P_e of its lines/sentences are replaced (defaults: P_m = 1.0, P_e = 0.2, semantic errors). Error type is **semantic** (plausible but wrong) vs **syntactic**.
  - Control: the vanilla system, and a single agent.
- **Tasks:** HumanEval (164 items, Pass@1); CIAR counter-intuitive math (50); CommonMT lexical translation (100, BLEURT-20); FairEval text evaluation (80, agreement with humans). All are scored 0–100.
- **Outcome measures:** task score, and its drop relative to vanilla ("resilience"). There is no LLM judge except BLEURT. Scores come from ground truth.

## Key findings
1. **Structure (RQ1, Table 4).** Average drop across backbones and methods: **hierarchical −5.51 < flat −10.54 < linear −23.72**. The ranking holds for both backbones and both methods. The authors attribute it to the higher-level agent (e.g. the MAD judge), which sees several versions of the answer.
   - GPT-4o linear under AutoTransform collapses from 67.18 to 30.08.
   - LLaMA-3.1-70B (App. B.6): under AutoTransform the drops are hierarchical −9.2, flat −37.8, linear −61.9.
2. **Stronger backbones make better saboteurs.** With GPT-3.5, AutoInject hurts slightly more than AutoTransform (−12.12 vs −11.42), because transformed agents "lose track" of the instruction to err, or fail to err stealthily. With GPT-4o, AutoTransform hurts more (−18.22 vs −11.28), because the faulty agent follows its instructions better.
3. **Task (RQ2, Table 5).** Drops by task: code −22.56, math −9.89, text evaluation −5.42, translation −4.70.
   - MAS beat a single agent (+4.76 points on GPT-3.5, +5.29 on GPT-4o), but with a faulty agent they fall to or below single-agent level.
   - Errors in subjective tasks tend to go unnoticed by the other agents.
4. **Faulty agents can help (Table 2).** AutoInject *improves* MAD (GPT-3.5) text evaluation by up to 12.1%, and GPT-4o MAD code by 4.2%. There are two mechanisms:
   - **Double-checking:** an obvious error makes a peer ask for a rewrite, which also fixes errors that were already there.
   - **Divergent thinking:** injected errors break repetitive debate loops.
5. **Error rate (RQ3, Table 6, code, GPT-3.5).** Raising the share of faulty messages P_m hurts more than raising the errors per message P_e.
   - At P_m = 1.0 the average falls from 48.44 (P_e 0.2) to 22.75 (P_e 0.6). MetaGPT falls to 6.70.
   - At P_m = 0.2, going from P_e 0.4 to 0.6 slightly *raises* the average (53.05 → 53.75). Blatant errors get noticed, so stealth matters.
6. **Error type (RQ4, Table 7).** Semantic errors hurt more (average 39.15) than syntactic ones (47.78; vanilla 64.73). Self-collab (external compiler) and MAD (judge) barely suffer from syntactic errors.
7. **Case studies.**
   - Adding a comment "# Corrected the bug" makes all six systems accept code that is still wrong. The agents trust natural-language claims over the code.
   - Making the *higher-level* agent faulty hurts more. Code scores: Camel-User 25.3 vs Camel-Assistant 29.3; MetaGPT-Product Manager 22.0 vs Coder 26.8.
   - With two faulty agents in AgentVerse math (App. B.3), accuracy goes from 28.0 (Solver only) to 14.0 (+Critic) to 12.0 (+Planner).
8. **More rounds ≠ more resilience.** In Camel with injected errors, failing items take 11.57 rounds on average, against 8.89 for passing ones. The extra talk does not fix the hard cases.
9. **Defences (Table 3).** Challenger = each agent may challenge received messages. Inspector = an extra agent that checks and corrects every message.
   - Self-collab under AutoTransform: 43.3 → 75.0 with C+I (vanilla 76.2).
   - Camel under AutoInject: 29.3 → 48.6 (vanilla 62.2).
   - Neither method specifically counters one error-introducing method.
10. **Single agents are the least resilient (App. B.2).** A GPT-3.5 single agent averages 48.02, falling to 21.66 under AutoTransform and 31.71 under AutoInject. Every multi-agent structure stays at 38.24 or above.

## Relevance to research questions
### Q5: Interaction channels
The paper frames topology as organisational structure (linear / flat / hierarchical) and formalises each as a graph class (path, complete digraph, rooted tree). It maps these onto six real frameworks. The channel is always direct message passing.
- The main result is topological: **a node that aggregates several independent answers (a judge or leader) is the main source of resilience**. A star beats a complete graph too (App. B.4: math 30.0/28.0 vs 20.0/16.0 under the two attacks).
- Role matters as much as position: a faulty *upstream* instructor or planner does more damage than a faulty worker.

See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction here is **erroneous input from a peer**: a "clumsy or malicious" agent whose messages contain stealthy mistakes. The paper decomposes it into four dimensions:
- **source:** a transformed persona vs corrupted messages;
- **frequency:** P_m;
- **density:** P_e;
- **type:** semantic vs syntactic.

Two findings bear on *why* errors pass unchecked. **Plausible semantic errors and natural-language reassurance** ("bug corrected") slip past peers. **Blatant errors provoke correction.** So the friction is most harmful when it is stealthy and frequent, not when it is dense. See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
This is the most direct quantitative evidence for **scenario (c)**, an orchestrator or downstream agent receiving erroneous sub-agent outputs.
- **Size of the drop:** 5.5–23.7 points by structure, and up to −22.6 on code.
- **Cascade:** errors propagate fully in linear chains with no aggregator.
- **Efficiency:** failing cases take more rounds (11.57 vs 8.89) without recovering.
- **Non-monotonic effect:** occasional obvious errors can *improve* results by triggering review and breaking debate stagnation, which is a performance gain from friction.
- **Mitigation:** peer challenge plus an inspector recovers up to 96.4% of lost performance, at the cost of extra agents and calls (the cost is not quantified).

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Huang2024-fig-02-p3.png]]
*Fig. 2: The two ways of introducing a faulty agent. AutoTransform rewrites the agent's profile to insert stealthy errors. AutoInject intercepts and corrupts its messages. In (d), the peer catches the first injected bug but not the second.*

![[Huang2024-fig-08-p7.png]]
*Fig. 5b: Code generation (GPT-3.5) under AutoInject with semantic vs syntactic errors. Semantic errors are more damaging almost everywhere. MAD even gains from syntactic errors.*

**Table 4: Average task score (0–100) by structure, with one faulty agent**

| Backbone / condition | Linear | Flat | Hierarchical |
|---|---|---|---|
| GPT-3.5 vanilla | 55.62 | 54.37 | 53.00 |
| + AutoTransform | 38.24 | 43.93 | 46.57 |
| + AutoInject | 38.27 | 40.25 | 48.12 |
| GPT-4o vanilla | 67.18 | 67.52 | 67.79 |
| + AutoTransform | *30.08* | 56.92 | 60.83 |
| + AutoInject | 44.14 | 60.51 | 64.01 |
| **Avg. drop** | **↓23.72** | **↓10.54** | **↓5.51** |

**Table 3: Defences on code generation (GPT-3.5)**

| System / condition | none | Challenger | Inspector | C+I |
|---|---|---|---|---|
| Self-collab, no errors | 76.2 | 74.6 | 76.4 | 76.8 |
| Self-collab + AutoTransform | 43.3 | 70.7 | 74.4 | **75.0** |
| Self-collab + AutoInject | 40.9 | 72.0 | 67.7 | 73.8 |
| Camel, no errors | 62.2 | 62.2 | 61.0 | 63.8 |
| Camel + AutoTransform | 32.5 | 43.5 | 41.8 | 48.7 |
| Camel + AutoInject | 29.3 | 40.2 | 44.2 | 48.6 |

## Limitations / caveats
- **Topology is confounded with the framework.** Each structure is represented by two systems that also differ in role design, number of agents, prompts and tools (Self-collab has a compiler). This is n = 2 per structure, and the systems had to be adapted to tasks they were not built for. The appendix star-vs-complete-graph check is small (one task, one model).
- **The "%" in the abstract is really points.** The 5.5/10.5/23.7 figures are average absolute point drops on 0–100 scales that mix accuracy and BLEURT. The conclusion's "12.1% and 9.2%" for hierarchical systems are *relative* drops for GPT-3.5 (53.00 → 46.57 and → 48.12). Check which metric is meant before quoting either figure.
- **Small benchmarks.** CIAR has 50 items and FairEval 80. The authors report no seeds or confidence intervals and use temperature 0, so the variance is unknown.
- **Faulty behaviour is prompted.** The "malicious" agent is prompted or intercepted, not emergent. AutoTransform does not reliably produce errors: realised error rates average 1.56% for a 20% target (SD 3.65).
- The receiving agents are always the same backbone as the faulty agent, and they are unaware of it. There is no condition where peers are warned or are a different model.
- **Performance only.** No safety outcome is measured. "Malicious" here means wrong answers, not harmful content.
- The defences are evaluated only on the two weakest systems, and their token/latency cost is not reported.

## Related work to follow
- [[Zhang2024 - PsySafe]]: dark-personality agents as a MAS attack. The Inspector is modelled on its "Police" agent.
- [[Amayuelas2024 - MultiAgent Collaboration Attack]]: an adversarial debater. The authors cite it for the finding that the number of agents or rounds has limited effect.
- [[Yu2024 - NetSafe]]: topology and multiple attacker agents.
- [[Tian2023 - Evil Geniuses]]: role-specific attack prompts, similar to AutoTransform.
- [[Gu2024 - Agent Smith]]: malicious behaviour spreading through multi-agent interaction and memory.
- [[Ju2024 - Flooding Spread of Manipulated Knowledge in LLM-Based]]: manipulated knowledge spreading in MAS.
- [[Mao2025 - AgentSafe Safeguarding Large Language Model-based]]
- [[Jia2026 - MAS-FIRE Fault Injection and Reliability Evaluation for]] and [[Tan2026 - AgentChaos Chaos Engineering for Agent Systems via]]: later fault-injection frameworks.

![[Backlog.base#Cited by this paper]]
