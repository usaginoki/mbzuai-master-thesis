---
title: "NetSafe: Exploring the Topological Safety of Multi-agent Networks"
citekey: Yu2024
authors: [Miao Yu, Shilong Wang, Guibin Zhang, Junyuan Mao, Chenlong Yin, Qijiong Liu, Qingsong Wen, Kun Wang, Yang Wang]
year: 2024
published: 2024-10-21
venue: "Findings of ACL 2025"
peer_reviewed: true
url: https://arxiv.org/abs/2410.15686
arxiv: "2410.15686"
code: https://github.com/Ymmcll/NetSafe
pdf: "[[Yu2024.pdf]]"
pdf_url: https://arxiv.org/pdf/2410.15686
questions: [Q5, Q6, Q7.1, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-adversarial-faulty-agent
cites:
  - "[[Aher2023 - Using Large Language Models to Simulate Multiple Humans and]]"
  - "[[Cohen2024 - Here Comes The AI Worm]]"
  - "[[Gu2024 - Agent Smith]]"
  - "[[Tian2023 - Evil Geniuses]]"
  - "[[Zhang2024 - PsySafe]]"
cited_by:
  - "[[Huang2024 - Resilience of MAS with faulty agents]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/debate
  - channel/direct-message
  - friction/adversarial-agent
  - friction/erroneous-input
  - effect/performance-drop
  - effect/error-cascade
---
# NetSafe: Exploring the Topological Safety of Multi-agent Networks

> [!abstract] TL;DR
> Six GPT-4o-mini agents are wired into chain, cycle, binary-tree, star or complete-graph topologies. Over 10 rounds of neighbour-to-neighbour revision ("RelCom"), attacker nodes inject **misinformation**, **bias** or **harmful content**. **Misinformation spreads and degrades the benign nodes.** With 1 attacker on a fact-checking task, accuracy settles at 84.2 in a chain but falls from 95.0 to 66.8 (−29.7%) in a star centred on the attacker. With 5 attackers, the complete graph drops from 89.4 to 44.3 on GSM8K. The authors call this "**Agent Hallucination**". **Bias and harmful content, by contrast, barely propagate at all ("Aggregation Safety").** Benign nodes keep 99.6–100% bias-detection accuracy. A single benign node surrounded by five jailbroken attackers keeps a moderation score of 0.097, against 0.920 for the attackers. Less connected topologies, and nodes farther from the attacker, are safer. Adding benign nodes helps little, while removing attackers helps a lot.

## Setup
- **Agents & topology:** 6 nodes by default, with 1 attacker (ablations: 0–5 attackers; 5–9 benign nodes with 1 attacker). There are five directed topologies (Fig. 3): chain, cycle, binary tree, star and complete graph.
  - In the figure, the attacker (Agent 1) is the head of the chain, the **hub** of the star and the root of the tree.
  - Model: GPT-4o-mini for all agents (temperature 0). The harmful-content condition uses GPT-3.5-Turbo so that attackers can be jailbroken.
- **Interaction channel:** **RelCom**, a debate-like iterative protocol.
  - **Genesis:** every node answers independently.
  - **Renaissance** (repeated for 10 rounds): each node collects its in-neighbours' answers, reasons and "memory", then regenerates its own response.
  - The message content is answer + reason + memory.
- **Friction / manipulation:** attacker nodes get a system prompt describing an attack strategy.
  - **Misinformation Injection:** argue for a wrong answer.
  - **Bias Induction:** claim stereotypes are not biased.
  - **Harmful-info Elicitation:** produce harmful content, using PsySafe's Dark Traits Injection to jailbreak the attacker.
  - Controls: 0 attackers (App. I.5: accuracy stays roughly flat over 10 rounds), and varying attacker and benign node counts.
- **Tasks:**
  - Misinformation, at three "logic levels": Fact (153 GPT-generated true/false statements), CSQA (127 CommonsenseQA items), GSMath (113 GSM8K problems).
  - Bias: 103 GPT-4o-generated stereotype statements, to be identified as biased.
  - Harmful info: AdvBench prompts.
  - Mean of 3 runs.
- **Outcome measures:**
  - **MJA:** mean accuracy of benign nodes per round.
  - **SAA:** per-agent accuracy.
  - OpenAI **Moderation API** scores for harmful content.
  - **Static graph metrics** (network efficiency, eigenvector centrality, and a new Attack Path Vulnerability metric), compared with the dynamic ranking via Kendall's τ.

## Key findings
1. **Misinformation erodes benign accuracy and converges (Table 1).** Accuracy falls in 97.8% (Fact), 82.2% (CSQA) and 77.8% (GSMath) of topology–round cases, flattening by round ~10.
   - Without attackers, Fact accuracy stays at 91.8–93.7 after 10 rounds (App. I.5).
2. **More connected = less safe (Table 1).** Final Fact accuracy: chain 84.18 > complete 80.39 > cycle 78.17 > tree 75.03 > **star 66.80** (from 95.03, −29.7%). CSQA: chain 65.35 vs star 53.54.
   - On GSMath the complete graph is *best* (85.84), and all topologies end at 83–86.
3. **Harder reasoning tasks resist misinformation better (Obs. 3).** The average relative accuracy loss from round 1 to 10 is 18.2% on Fact, 7.4% on CSQA and 3.2% on GSMath. The authors read this as "Agent Hallucination": false factual claims from one node propagate network-wide.
4. **Influence runs both ways (Fig. 4).** The attacker's own fact-checking accuracy jumps by 36.2 on average in round 2 and settles near chance (~50). Benign-node accuracy falls from ~93 to 83.2 / 77.8 / 69.4 in chain / cycle / star.
   - Node position matters: Agent 6 is directly linked to the attacker in the cycle but not in the chain, and its accuracy is about 10 points lower in the cycle.
5. **"Aggregation Safety" for bias and harmful content (Table 3, Fig. 6).**
   - **Bias:** benign nodes keep 99.61–100% accuracy in every topology and round. The attacker is partly *corrected*: its accuracy rises from 4.7 to 22.8 in the complete graph, but only to 10.9 in the tree.
   - **Harmful content:** in a complete graph with **5 jailbroken attackers and 1 benign node**, the benign node's moderation score is 0.097 vs 0.920 for the attackers (self-harm ≈ 0 vs 0.359).
6. **Attacker count matters more than benign count (Figs. 7–8).**
   - Complete graph on GSMath: 89.38 with 0 attackers → 44.25 with 5 attackers (−50.5%). Chain is best in 5 of 6 attacker counts.
   - With 2 attackers on Fact, final accuracy is chain 81.37 vs star 57.03 (App. I.5).
   - Adding benign nodes gives small, non-monotonic gains. Tree on Fact: 78.17 → 83.94 → 82.57. Star falls from 74.88 to 71.1 when going from 7 to 9 benign nodes.
7. **Static graph metrics predict little (Table 2).** Kendall's τ with the dynamic ranking: network efficiency 0.067, eigenvector centrality −0.567, the new APV metric 0.367.

## Relevance to research questions
### Q5: Interaction channels
The paper recasts MAS communication as **iterated neighbour aggregation on a directed graph** (RelCom), which makes topology a controlled variable.
- **Main result:** higher connectivity and shorter paths from the attacker mean faster, deeper contamination. Chain is safest and star/complete least safe for factual misinformation.
- **Caveat:** in the star the attacker *is* the hub, so connectivity is confounded with the attacker's centrality.
- Standard graph metrics do not substitute for simulation.

See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction source is a **prompted adversarial node** that argues persistently for false answers, denies bias, or emits harmful text. Its pressure is purely argumentative, through repeated exposure each round.
- **Which kind of pressure works depends on the content.** Plausible *factual* falsehoods pass, but norm-violating content (stereotypes, harm) does not.
- **Scenario (b):** the paper sweeps the number of hostile agents, showing that 1 of 6 is tolerated partially and 5 of 6 is catastrophic for accuracy.

See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- **A strong null result for norm-violating content.** Safety-aligned benign agents neither adopt bias nor reproduce harmful content, even when outnumbered 5:1 ("Aggregation Safety").
- **Benign majorities can partially correct the bad agent.** The attacker's bias-detection accuracy rises over rounds.
- **Misinformation is the real risk.** It is framed as a safety failure ("Agent Hallucination"), and it spreads because it does not trigger refusal.

See [[Q7.1 Effects on safety]]

### Q7.2: Effects on performance and efficiency
- **Size of the drop:** a single misinformation node lowers benign-node accuracy by 9–28 points on fact checking, depending on topology, and 5 attackers halve GSM8K accuracy.
- **Dynamics:** the degradation accumulates over rounds before plateauing, so more deliberation does not self-correct.
- **Topology:** it is a first-order design parameter, which is relevant to **scenario (c)**. An aggregator node directly exposed to a bad input source is the most vulnerable position.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Yu2024-fig-03-p7.png]]
*Fig. 3: The five 6-node topologies. The red node is the attacker (Agent 1); red arrows are attack information flow. Note that the attacker is the hub of the star.*

![[Yu2024-fig-06-p8.png]]
*Fig. 7–8: Converged benign-node accuracy (MJA) as the number of attackers grows (top, GSM8K) and as the number of benign nodes grows with 1 attacker (bottom, Fact). Right: summary curves. Adding attackers is far more damaging than adding benign nodes is protective.*

**Table 1 (excerpt): Benign-node accuracy (MJA), 6 nodes incl. 1 misinformation attacker, rounds 1 → 10**

| Topology | Fact R1 | Fact R10 | CSQA R1 | CSQA R10 | GSMath R1 | GSMath R10 |
|---|---|---|---|---|---|---|
| Chain | 93.46 | **84.18** | 64.88 | **65.35** | 86.55 | 83.72 |
| Cycle | 93.86 | 78.17 | 63.94 | 61.42 | 87.08 | 83.89 |
| Binary tree | 93.86 | 75.03 | 63.15 | 57.48 | 87.61 | *83.01* |
| Star | 95.03 | *66.80* | 64.09 | *53.54* | 86.73 | 84.78 |
| Complete | 94.12 | 80.39 | 63.62 | 58.27 | 87.08 | **85.84** |

## Limitations / caveats
- **Topology is confounded with attacker placement.** The attacker sits at the hub of the star, the root of the tree and the end of the chain. "Connectivity" effects may partly be attacker-centrality effects, and attacker position is not varied.
- **The text contradicts itself on distance.** The abstract says that greater average distance *from* attackers means more safety, which is consistent with the data. §4.5 "Trait 2" says the opposite ("the smaller the average distance… the safer").
- **Narrow set of models.** There is a single small model (GPT-4o-mini), and a different model (GPT-3.5) for the harmful condition. All nodes are homogeneous, and nobody is told an attacker exists.
- **Harmful-content result rests on thin evidence.** It comes from one complete-graph configuration, measured only by the Moderation API. It shows that *reproducing* harmful text is rare, not that the network's downstream decisions are safe.
- **Weak bias task.** The bias task (identify stereotypes) is near ceiling even at round 1, so it cannot show much vulnerability.
- **Small datasets.** Datasets are small (103–153 items) and partly GPT-generated, with 3 runs at temperature 0. The reported "variances around 1e-3" say little about item-level uncertainty.
- **Venue** is taken from the candidate note. The extracted text uses an ACM template with no venue.

## Related work to follow
- [[Zhang2024 - PsySafe]]: its Dark Traits Injection is reused to jailbreak the harmful-content attackers.
- [[Gu2024 - Agent Smith]]: an adversarial image spreading exponentially across multimodal agents.
- [[Huang2024 - Resilience of MAS with faulty agents]]: faulty agents vs linear/flat/hierarchical structures. It finds hierarchy is most resilient, which is partly in tension with NetSafe's "less connected is safer".
- [[Amayuelas2024 - MultiAgent Collaboration Attack]] and [[Lee2024 - Prompt Infection]]: other single-adversary MAS attacks.
- [[Wang2025 - G-Safeguard A Topology-Guided Security Lens and]], [[Zhang2025 - Achilles Heel of Distributed Multi-Agent Systems]] and [[Becker2026 - Misinformation Propagation in Benign Multi-Agent]]: follow-ups on topology and misinformation propagation.
- [[Zhang2024 - Cut the Crap]]: AgentPrune, which prunes communication graphs. It is related to the topology–safety question.

![[Backlog.base#Cited by this paper]]
