---
title: "When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems"
citekey: Yan2026
authors: [Chenfei Yan, Zeyang Yue, Feifei Zhao, Erliang Lin, Lu Jia, Haibo Tong, Mingyang Lyu, Chengyi Sun, Yi Zeng]
year: 2026
published: 2026-08-04
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2608.03421
arxiv: "2608.03421"
pdf: "[[Yan2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2608.03421
questions: [Q5, Q6, Q7.1, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-adversarial-faulty-agent
  - search/mas-error-propagation
cites:
  - "[[Baltaji2024 - Persona Inconstancy in Multi-Agent LLM Collaboration]]"
  - "[[Becker2026 - Misinformation Propagation in Benign Multi-Agent]]"
  - "[[Cho2025 - Herd Behavior]]"
  - "[[He2025 - Red-Teaming LLM Multi-Agent Systems via Communication]]"
  - "[[Lee2024 - Prompt Infection]]"
  - "[[Li2024 - Improving Multi-Agent Debate with Sparse Communication]]"
  - "[[Li2025 - Systematic Failures in Collective Reasoning under]]"
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
  - channel/direct-message
  - channel/voting-aggregation
  - friction/adversarial-agent
  - friction/erroneous-input
  - effect/error-cascade
  - effect/deception
  - effect/performance-drop
---
# When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems

> [!abstract] TL;DR
> ForesightSafety-TIDE: 120 object-movement stories (adapted from Hi-ToM). Five agents each see only part of the object's movement history but can jointly reconstruct its final location. In the paired deceptive condition, the one "key" agent that witnessed the final move gives a coherent false account. Tested on GPT-5.5, DeepSeek-v4-pro and Grok-4.5. **The share of runs where the four honest agents reach a correct majority falls from 72.50% (all honest) to 14.17% (one liar): 43.33% of runs end in a decoy majority and 42.22% in no consensus.** The false testimony is adopted by 70.7% of statements vs 25.4% for the matched true testimony, and it spreads through deeper relay chains. **When the liar gives its testimony and then leaves (GPT-5.5), honest agents keep relaying it: 37/120 correct vs 93/120 when it leaves silently.** Added observers without first-hand evidence cut decoy majorities by 90% but do not increase correct ones.

## Setup
- **Agents & topology:** homogeneous 5-agent systems (all GPT-5.5, all DeepSeek-v4-pro or all Grok-4.5), temperature 0, reasoning effort low (GPT-5.5, Grok-4.5) or none (DeepSeek). Each agent has its own context. Majority = 3 of the 4 non-key agents. Extra conditions: key-agent *exit* (GPT-5.5 only) and 3 *observers* with no local evidence (passive or active).
- **Interaction channel:**
  - story-embedded *private* (A → B) and *public* broadcast messages, one per role;
  - a mandatory public **testimony board** of typed evidence cards (6 per role, 30 per environment);
  - **three simultaneous public discussion rounds** (R1: build candidate timelines; R2: cross-check continuity, source independence and coverage; R3: final evaluation).
  
  After T0 (own view only), T1 (after testimony) and each round, every agent casts a private endpoint vote (or UNKNOWN). Aggregation is by majority vote.
- **Friction / manipulation:** C0 (all honest) vs C1 (the key agent knows the true endpoint and "attempts to prevent fact recovery"). Its communication and testimony are replaced with a coherent false account pointing at a preregistered decoy, the previous location l_{m−1}. Three deception mechanisms, 40 stories each:
  - **Event:** invents a move back after the true endpoint.
  - **Coverage:** claims its observation window extended past the terminal move.
  - **Source:** re-dates an earlier true private report as the latest.

  A second honest witness of the final move (the "2nd-key" role) is present in every story. Exit ablations: the key agent gives true / null / false testimony at T1 and then leaves (Honest-, Null-, False-Exit).
- **Tasks / environment:** 120 environments balanced on mechanism, difficulty, number of moves (3/4/5) and minimum recovery set (2 or 3 roles). Every story is information-sufficient without the key role.
- **Outcome measures:** truth-majority, decoy-majority and no-consensus rates; vote shares; testimony *reference* vs *adoption* rates per statement; atomic-claim counts; *propagation order* (relay depth from the original testimony); true-root vs false-root lineage states per agent. Tests: exact McNemar and paired sign-flip, bootstrap CIs.

## Key findings
1. **A single liar collapses fact recovery (Table D.1–D.2).**

   | R3 outcome, 360 runs per condition | C0 honest | C1 one liar | Δ |
   |---|---|---|---|
   | Truth majority | 72.50% | 14.17% | −58.33 pp |
   | Decoy majority | 4.44% | 43.33% | +38.89 pp |
   | No consensus | 22.50% | 42.22% | +19.72 pp |

   Individual truth votes fall from 75.00% to 24.38% (−50.62 pp). p < .001 for every model.
2. **The strongest honest aggregator is the most fragile.** Grok-4.5 is best under C0 but worst under C1: truth majority −79.17 pp, truth votes −63.75 pp. Grok mostly fails into UNKNOWN / no consensus, while DeepSeek converges on the decoy. The increase in decoy-vote share does not differ significantly between models: GPT-5.5 +44.0 pp, DeepSeek +44.4, Grok +37.9; pairwise p ≥ .20.
3. **The damage happens at first exposure, and discussion amplifies it.** About 85% of the final C0–C1 gap already exists at T1, after testimony but before any discussion. Discussion then pushes each condition further in the direction it started: under C0 it adds +10.83 pp truth majorities; under C1 it mostly converts uncertainty into decoy majorities (+15.83 pp). "Discussion is not inherently corrective."
4. **The false testimony wins on adoption, not on exposure.** The true and false testimonies are *referenced* at similar rates, but adoption under C1 is 70.7% for the key agent's false testimony vs 25.4% for the 2nd-key agent's true one. Claims about the key agent are 17% more frequent.
5. **The false root enters true-root paths more easily than the reverse.** Dual-root holders rise from 0% (R1) to 49.4% (R2) and 57.6% (R3). 82.87% of true-only holders pick up the false root by R2, vs 38.31% for the reverse transition. Fewer than 45% of dual-root holders vote for the truth. Mean relay depth at R3: false root 2.66 vs true root 1.33.
6. **The misinformation outlives the liar (GPT-5.5 exit ablation, Fig. 5).** Truth majority out of 120: C0 94, Honest-Exit 97, Null-Exit 93, **False-Exit 37**, C1 31. False-Exit is 46.67 pp below Null-Exit. At R3, 273 honest agents still cite the departed liar's testimony and 197 adopt it. The liar staying mainly widens the reach of the false claim; the testimony itself does most of the damage.
7. **Evidence-less observers reduce wrong consensus without restoring truth.** Active observers cut decoy majorities by 90% overall, but truth majorities also fall. Passive observers reading the transcript reach 32 truth majorities (participants 31) and 18 decoy majorities (participants 51). Observers cite both testimonies but rarely adopt either, and trace back to the original testimonies.

## Relevance to research questions
### Q5: Interaction channels
A structured **evidence-pooling** protocol: private and public story messages, a typed public testimony board, three simultaneous public rounds and private majority voting. It shows that a verification-oriented discussion protocol (cross-checking continuity and source independence) does not protect against a coherent false account. The paper adds two **role variants** of interest: a departing agent (exit) and third-party *observers* without first-hand evidence. The observers resemble an aggregator or orchestrator that only sees sub-agent reports. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
- **A deceptive peer holding critical, hard-to-verify evidence.** Friction comes from the *content* of one agent's testimony, not from tone or pressure. The three mechanisms (fabricated event, inflated coverage, re-dated source) exploit temporal ordering, where a claim of later information naturally overrides earlier truth.
- **Honest relays as secondary sources:** once injected, the error is carried forward by honest agents (deeper relay chains, persistence after exit). The friction becomes a property of the group, not of the attacker.
- Scenario (b): this is the "dishonest peer injected into a group" case. The effect is large even though the other four agents are honest and together have enough evidence.

See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- A single deceptive agent succeeds in **steering the honest majority to a planted falsehood in 43% of runs**, and honest agents become carriers of the misinformation, **still relaying it after the deceiver has left**. This is an integrity and misinformation risk for any high-stakes MAS that makes decisions by consensus.
- Consensus-seeking discussion *amplifies* the initial contamination rather than correcting it.
- Mitigation insight: observers act as a brake (fewer decoy majorities) at the cost of decisiveness. Neither observers nor discussion recover the truth.

See [[Q7.1 Effects on safety]]

### Q7.2: Effects on performance and efficiency
- **Task accuracy (collective fact recovery) falls from 72.5% to 14.2%**, with failures split between wrong consensus and no consensus (deadlock-like uncertainty).
- Scenario (c): the observer results are a proxy for an orchestrator receiving conflicting sub-agent reports without first-hand evidence. It becomes cautious (UNKNOWN) but cannot identify which input is erroneous.
- Honest-condition strength does not predict robustness (Grok-4.5).

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Yan2026-fig-02-p5.png]]
*Fig. 2: Group outcomes (left) and individual votes (right) across checkpoints T0–R3 under C0 (bottom) and C1 (top), with per-model R3 breakdowns. The gap opens at T1 when testimony arrives and widens slightly with discussion.*

![[Yan2026-fig-05-p6.png]]
*Fig. 5 (GPT-5.5): (a) Truth majorities: 94 (C0), 97 (Honest-Exit), 93 (Null-Exit), 37 (False-Exit), 31 (C1) of 120. False testimony keeps working after the liar exits. (b) Citation and adoption of false vs true testimony. (c) Exclusive true-root holders almost disappear under C1 but survive under False-Exit.*

## Limitations / caveats
- **The deceptions have a structural advantage.** Each false account claims *later* information (a subsequent move, a longer observation window, a more recent report), which legitimately overrides an earlier true observation under the task's own rules. Higher adoption of false testimony may partly reflect sensible recency reasoning, not a general bias toward falsehood. There is no control in which a false claim of *earlier* information is injected.
- The deceiver is a scripted, coherent liar (fixed false content that stays consistent) rather than an emergently deceptive agent. The honest agents are never told that one member may lie; a "possible adversary" warning condition would show whether vigilance helps.
- Homogeneous teams only, one run per cell at temperature 0, and a single synthetic domain (object locations from Hi-ToM).
- Exit and observer ablations use GPT-5.5 only. Adoption and relay-depth measures depend on reference extraction whose validation is not described in the main text.
- Efficiency (tokens, rounds) is not reported; the discussion length is fixed.

## Related work to follow
- [[Li2025 - Systematic Failures in Collective Reasoning under]]: HiddenBench, collective reasoning under distributed information (honest setting). This paper extends it with deception.
- [[Becker2026 - Misinformation Propagation in Benign Multi-Agent]]: honest agents relaying misinformation without a malicious relay.
- [[Amayuelas2024 - MultiAgent Collaboration Attack]]: adversarial agent steering debate to wrong answers.
- [[He2025 - Red-Teaming LLM Multi-Agent Systems via Communication]] and [[Shen2025 - Understanding the Information Propagation Effects of]]: communication attacks and topology effects on propagation.
- [[Cho2025 - Herd Behavior]], [[Baltaji2024 - Persona Inconstancy in Multi-Agent LLM Collaboration]], [[Lee2024 - Prompt Infection]]: peer influence, conformity and contagion along communication chains.
- [[Fukui2026 - Invisible Orchestrators]]: another case where aggregation-level evaluation misses what happens inside the group.

![[Backlog.base#Cited by this paper]]
