---
title: "Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate"
citekey: Wynn2025
authors: [Andrea Wynn, Harsh Satija, Gillian K. Hadfield]
year: 2025
published: 2025-09-05
venue: "ICML 2025 Workshop on Multi-Agent Systems"
peer_reviewed: workshop
url: https://arxiv.org/abs/2509.05396
arxiv: "2509.05396"
code: https://github.com/TheNormativityLab/talk-aint-cheap/
pdf: "[[Wynn2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2509.05396
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-conformity-peer-pressure
  - search/mas-error-propagation
cites:
  - "[[Agarwal2025 - When Persuasion Overrides Truth in Multi-Agent LLM]]"
  - "[[Amayuelas2024 - MultiAgent Collaboration Attack]]"
  - "[[Kenton2024 - On scalable oversight with weak LLMs judging strong]]"
  - "[[Khan2024 - Debating with More Persuasive LLMs Leads to More]]"
  - "[[Yao2025 - Peacemaker or Troublemaker]]"
cited_by:
  - "[[Hao2026 - Not all flips are conformity]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - channel/debate
  - channel/voting-aggregation
  - friction/peer-pressure-conformity
  - friction/erroneous-input
  - effect/conformity-flip
  - effect/performance-drop
  - effect/error-cascade
  - effect/sycophancy
---
# Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate

> [!abstract] TL;DR
> Groups of three agents (GPT-4o-mini, Llama-3.1-8B, Mistral-7B, in homogeneous and mixed groups) run a Du et al.-style multi-agent debate on CommonSenseQA, MMLU and GSM8K. The final answer is a majority vote, compared with a vote over the initial answers (no debate). **Debate lowers accuracy in every CommonSenseQA configuration**, and often on MMLU, even when strong models are the majority. The worst case is 1 Llama + 2 Mistral on MMLU: 40.0% → 28.0% (−12.0 pp). **Correct → incorrect flips outnumber incorrect → correct flips.** An agent is most likely to abandon a correct answer when no peer agrees with it. On GSM8K this happens ~31% of the time for Llama-3.1-8B, falling to ~15% with one agreeing peer. **A "correctness payoff" prompt against sycophancy does not reduce harmful flips, and sometimes increases them.**

## Setup
- **Agents & topology:** N = 3 agents, fully connected. Configurations: 3 homogeneous groups (3× GPT-4o-mini, 3× Llama-3.1-8B-Instruct, 3× Mistral-7B-Instruct-v0.2), six 2+1 mixtures, and one "diverse" group (1 of each). Default temperature, top_p = 0.9, max 2048 tokens.
- **Interaction channel:** simultaneous debate following Du et al. (2023). In each round, every agent sees the other agents' previous-round responses (answer + bullet-point reasoning; summarised by another LLM call if too long). It then gets the prompt "Using the reasoning from other agents as additional advice, can you give an updated answer?… Examine your solution and that of other agents." T = 2 debate rounds after the initial answer. Final answer = majority vote.
- **Friction / manipulation:** no adversary is planted. The friction is *emergent* peer disagreement and peer (often wrong) reasoning. What varies is the **capability mix** of the group (weak peers alongside strong ones). The control is a majority vote over the round-0 answers ("w/o Debate").
- **Mitigation probe:** a "correctness payoff" system/debate prompt ("You will receive a fixed payoff p = I[X == Y]… maximize your payoff"), inspired by political-science results that monetary incentives reduce partisan bias.
- **Tasks:** CommonSenseQA, MMLU (both multiple choice) and GSM8K (open numeric). 100 random questions per task, 5 seeds.
- **Outcome measures:** group accuracy (majority vote) before and after debate and per round. Answer-transition breakdown (C→C, C→I, I→C, I→I) per round. Probability of a C→I flip as a function of how many other agents agreed with the ego agent. Exact-match scoring; no LLM judge.

## Key findings
1. **Debate often hurts accuracy compared with a no-debate vote (Table 1).**
   - On CommonSenseQA, all 10 configurations drop after debate (−0.8 to −8.0 pp).
   - On MMLU, 7 of 10 drop, e.g. 1 Llama + 2 Mistral 40.0 → 28.0 (−12.0), 2 Llama + 1 Mistral 51.8 → 43.6 (−8.2), 3× Mistral 33.6 → 24.4 (−9.2).
   - GSM8K is mixed. Debate helps some groups (1 GPT + 2 Llama +4.4) and hurts others (2 Llama + 1 Mistral −6.8).
2. **A strong majority does not protect the group.** 2 GPT + 1 Mistral still loses accuracy on all three tasks (CSQA −2.2, MMLU −2.0, GSM8K −0.4). On MMLU, 2 GPT + 1 Llama goes 82.6 → 81.0, below a single GPT-4o-mini (82.6).
3. **Accuracy falls over debate rounds (Fig. 1).** The decline is clearest on MMLU and CSQA for mixed-capability groups.
4. **Harmful flips dominate (Figs. 2–3).** Aggregated over rounds, more agents move correct → incorrect than incorrect → correct. Most initially-wrong agents stay wrong. The effect grows in round 2: agents that held a correct answer in round 1 cave more often in round 2. The authors call this "a dominating effect of social pressure".
5. **Isolation predicts caving (Fig. 4).** P(C→I) is highest with 0 agreeing peers and drops with 1 and then 2 agreeing peers, across all datasets and models. Approximate values from the bar chart:
   - CSQA: ~18–23% at 0 agreeing peers → ~3% at 2.
   - GSM8K: Llama-3.1-8B is far more susceptible (~31% at 0, ~15% at 1) than GPT-4o-mini or Mistral-7B (~8% at 0).
6. **The anti-sycophancy incentive prompt fails (Fig. 5).** A correctness payoff does not significantly reduce C→I flips at any level of peer agreement. "In many cases" it increases them.
7. **No single mechanism explains the failures.** Model capability, task type and social influence interact (Section 6.4).

## Relevance to research questions
### Q5: Interaction channels
**Simultaneous multi-round debate with majority-vote aggregation**, in a fully connected 3-agent group. Every agent reads every peer's full answer and reasoning. The paper's novelty is *heterogeneous* groups: mixing models of different capability is a design choice that systems like mixture-of-agents assume is harmless. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
- **Peer disagreement / conformity pressure:** the flip rate depends on the number of peers who disagree, not only on the quality of their arguments.
- **Erroneous input from weaker peers:** wrong but confident reasoning from a weaker model pulls down a stronger one.

The authors frame the mechanism as sycophancy generalised from users to peer agents. The payoff-prompt null result suggests this is not easily overridden by instruction. This is a mild, *emergent* version of scenario (c): a group aggregating erroneous sub-agent outputs, where the erroneous agents are ordinary weaker models, not adversaries. See [[Q6 Sources of inter-agent friction]].

### Q7.2: Effects on performance and efficiency
- **Direct accuracy loss:** up to −12 pp on MMLU versus simply voting on the initial answers.
- **Wasted compute:** debate costs two extra rounds of generation per agent, yet in many configurations it underperforms the cheaper no-debate vote.
- **Degradation over rounds:** accuracy degrades as rounds accumulate, so more interaction can be worse.

See [[Q7.2 Effects on performance and efficiency]].

## Key figures & tables
![[Wynn2025-fig-01-p6.png]]
*Fig. 1: Group accuracy per debate round (1 = initial answers) for all 10 group configurations. Many mixed groups decline over rounds, especially on MMLU and CSQA.*

![[Wynn2025-fig-04-p8.png]]
*Fig. 4: Probability that an agent flips correct → incorrect, by number of other agents initially agreeing with it. Isolated agents cave most; Llama-3.1-8B on GSM8K is an outlier.*

**Table 1: Majority-vote accuracy (%) without debate vs after 2 rounds of debate (mean ± s.e., 5 seeds × 100 questions).** Single-agent accuracy: GPT-4o-mini 74.8 / 82.6 / 93.2, Llama-3.1-8B 57.0 / 55.6 / 76.4, Mistral-7B 41.6 / 34.0 / 34.2 (CSQA / MMLU / GSM8K).

| Group | CSQA w/o | CSQA after | MMLU w/o | MMLU after | GSM8K w/o | GSM8K after |
|---|---|---|---|---|---|---|
| 3× Mistral | 44.4 | 39.4 (−5.0) | 33.6 | 24.4 (−9.2) | 43.6 | 46.4 (+2.8) |
| 3× Llama | 63.0 | 58.6 (−4.4) | 61.6 | 57.8 (−3.8) | 87.6 | 84.2 (−3.4) |
| 3× GPT | 75.6 | 74.8 (−0.8) | 81.4 | 82.2 (+0.8) | 94.0 | 94.4 (+0.4) |
| 1 GPT, 2 Llama | 66.2 | 64.4 (−1.8) | 65.0 | 68.0 (+3.0) | 88.4 | 92.8 (+4.4) |
| 2 GPT, 1 Llama | 74.8 | 74.0 (−0.8) | 82.6 | 81.0 (−1.6) | 93.6 | 94.6 (+1.0) |
| 2 Llama, 1 Mistral | 58.2 | 50.2 (−8.0) | 51.8 | 43.6 (−8.2) | 82.6 | 75.8 (−6.8) |
| 1 Llama, 2 Mistral | 53.4 | 46.8 (−6.6) | 40.0 | **28.0 (−12.0)** | 61.0 | 64.8 (+3.8) |
| 1 GPT, 2 Mistral | 62.4 | 59.4 (−3.0) | 65.8 | 58.8 (−7.0) | 90.2 | 87.8 (−2.4) |
| 2 GPT, 1 Mistral | 74.6 | 72.4 (−2.2) | 82.8 | 80.8 (−2.0) | 93.4 | 93.0 (−0.4) |
| Diverse (1 each) | 66.6 | 65.4 (−1.2) | 57.8 | 63.4 (+5.6) | 86.8 | 90.2 (+3.4) |

## Limitations / caveats
- **Small scale:** 100 questions per task (×5 seeds), 3 agents and 2 debate rounds. Many deltas in Table 1 are within ~1–2 standard errors, and no significance tests are reported.
- **Weak models:** the "strong" model is GPT-4o-mini. No frontier or reasoning models are tested. Weak 7–8B models may lack the capability to judge peer reasoning at all.
- **Correlational social-influence evidence:** the Fig. 4 link between agreement and flipping is observational. The number of agreeing peers is confounded with question difficulty (hard questions produce both isolated correct agents and more flips). Unlike [[Hao2026 - Not all flips are conformity]], there is **no self-reflection control**, so part of the C→I flipping may be spontaneous instability rather than conformity.
- The debate prompt explicitly asks agents to use peer reasoning "as additional advice", which may encourage deference.
- The payoff prompt is a single wording, with no ablation.
- Only accuracy is measured. There are no safety outcomes and no token-cost accounting.
- The published PDF is labelled "Preprint". Venue information comes from the arXiv comment ("ICML MAS Workshop 2025").

## Related work to follow
- [[Hao2026 - Not all flips are conformity]]: decomposes debate flips into spontaneous instability, stance conformity and reasoning persuasion. It cites this paper.
- [[Yao2025 - Peacemaker or Troublemaker]]: sycophancy in multi-agent debate; declining disagreement correlates with degradation.
- [[Agarwal2025 - When Persuasion Overrides Truth in Multi-Agent LLM]]: confident, emotional falsehoods win debates.
- [[Amayuelas2024 - MultiAgent Collaboration Attack]]: an explicit adversary in debate.
- [[Choi2025 - Debate or Vote]]: much of debate's gain is explained by voting alone.
- [[Khan2024 - Debating with More Persuasive LLMs Leads to More]] and [[Kenton2024 - On scalable oversight with weak LLMs judging strong]]: debate as scalable oversight.
- [[Chen2025 - When and Why Does Multi-Agent Debate Fail and Does It]] and [[Wu2025 - Can LLM Agents Really Debate A Controlled Study of]]: other debate-failure studies.
- Estornell & Liu 2024, Multi-LLM debate: framework, principals, and interventions (NeurIPS 2024): "tyranny of the majority" theory.

![[Backlog.base#Cited by this paper]]
