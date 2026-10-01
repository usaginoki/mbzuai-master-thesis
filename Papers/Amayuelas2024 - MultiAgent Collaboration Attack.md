---
title: "MultiAgent Collaboration Attack: Investigating Adversarial Attacks in Large Language Model Collaborations via Debate"
citekey: Amayuelas2024
authors: [Alfonso Amayuelas, Xianjun Yang, Antonis Antoniades, Wenyue Hua, Liangming Pan, William Wang]
year: 2024
published: 2024-06-20
venue: "Findings of EMNLP 2024"
peer_reviewed: true
url: https://arxiv.org/abs/2406.14711
arxiv: "2406.14711"
pdf: "[[Amayuelas2024.pdf]]"
pdf_url: https://arxiv.org/pdf/2406.14711
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-adversarial-faulty-agent
  - search/mas-conformity-peer-pressure
cites:
  - "[[Khan2024 - Debating with More Persuasive LLMs Leads to More]]"
cited_by:
  - "[[Huang2024 - Resilience of MAS with faulty agents]]"
  - "[[Wynn2025 - Talk isn't always cheap]]"
cited_by_count: 2
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/debate
  - channel/voting-aggregation
  - friction/adversarial-agent
  - friction/persuasion-manipulation
  - friction/peer-pressure-conformity
  - effect/performance-drop
  - effect/conformity-flip
---
# MultiAgent Collaboration Attack: Investigating Adversarial Attacks in Large Language Model Collaborations via Debate

> [!abstract] TL;DR
> Three agents debate multiple-choice questions over 3 rounds, in the Du et al. style, and the final answer is a majority vote. One of the three is an **adversary**: it is given a wrong answer and told to persuade the others. The benchmarks are TruthfulQA, MMLU, MedMCQA and LegalBench-SCALR, and the models are GPT-3.5, GPT-4o, Llama-3-8B, Qwen1.5-14B and Yi1.5-9B. **Final majority-vote accuracy falls by roughly 0.1 (GPT-4o) to almost 0.4 (GPT-3.5) compared with an adversary-free debate.** Agreement with the adversary rises over rounds, e.g. GPT-3.5 +0.28 to +0.40, meaning honest agents are talked into the wrong answer. Neither more rounds nor more agents protects the group. On TruthfulQA, majority-vote accuracy slides to ~0.12 by round 9, against ~0.6 without an attack. Best-of-N argument selection makes the adversary somewhat more persuasive. **Warning the agents that an adversary may be present is not a reliable defence.**

## Setup
- **Agents & topology:** M = 3 agents (2 honest "group models" + 1 adversary), T = 3 rounds, fully connected.
  - All agents answer independently first. In each later round every agent sees all the others' answers and may revise its own. The final answer is the majority vote.
  - The adversary and the group run on the **same model** in each experiment: GPT-3.5-turbo, GPT-4o, Llama-3-Instruct-8B, Qwen1.5-Chat-14B or Yi1.5-Chat-9B.
  - Ablations: T = 1…9 rounds; M = 2…6 agents (TruthfulQA).
- **Interaction channel:** multi-agent debate (broadcast of reasoning and answers) + majority-vote aggregation.
- **Friction / manipulation:** the adversary is prompted: "Your aim is to convince the other agents of the provided answer… Generate a convincing chain of thought". It is reminded every round to keep its answer. The honest agents do not know an adversary is present.
  - **Stronger attacks** (TruthfulQA, GPT models):
    - **Best-of-N:** N arguments are generated and ranked by a preference model against a dummy argument for the correct answer.
    - **Extra knowledge:** retrieved context (simulated RAG).
  - **Mitigation:** a prompt warning the group that an adversary may be present.
  - Control: the same debate with no adversary.
- **Tasks:** 100 random items each from MMLU, TruthfulQA, MedMCQA and SCALR, each run 5 times (standard deviations reported).
- **Outcome measures:**
  - **Majority-vote system accuracy**, compared with no adversary and across rounds.
  - **Adversary agreement:** the normalised share of agents agreeing with the adversary. ΔAcc and ΔAgr are measured from round 1 to round 3.
  - Their joint sign is read as "attack working" (Table 1).
  - Appendix B gives the analytic expected majority-vote degradation for an always-wrong agent: 0.256 for 3 agents with p = 0.8.

## Key findings
1. **Every model's debate is degraded (Fig. 3).** Final majority-vote accuracy with the adversary is lower than without it on all 4 datasets.
   - Drops for GPT-3.5 are ≈ −0.31 to −0.39; Llama-3-8B ≈ −0.24 to −0.35; Qwen and Yi ≈ −0.16 to −0.28.
   - **GPT-4o** is the most resilient at ≈ −0.09 to −0.11.
   - The paper's headline is "system accuracy decreases ranging from 10% to almost 40%, and individual accuracy decreases from the group models of up to 30%".
2. **Honest agents are persuaded over rounds (Table 2, Fig. 4).** For the weaker models, majority-vote accuracy falls and adversary agreement rises from round 1 to round 3.
   - GPT-3.5: ΔAcc −0.20 to −0.30, ΔAgr +0.28 to +0.40.
   - Llama-3-8B: ΔAcc −0.12 to −0.25, ΔAgr +0.33 to +0.43.
   - **GPT-4o is the exception:** ΔAgr is negative on all four datasets (−0.05 to −0.10), and accuracy even rises on TruthfulQA (+0.026) and SCALR (+0.088). Its honest agents pull away from the adversary.
3. **Individual collapse (App. D).** GPT-3.5 honest agents on TruthfulQA go from 0.56 to 0.27 accuracy (round 1 → 3), with adversary agreement 0.23 → 0.63. Llama-3-8B on MedMCQA falls from 0.41–0.45 to 0.15–0.17, with agreement 0.30 → 0.73.
4. **Better arguments help the adversary, modestly (Table 3, TruthfulQA).** Best-of-N raises the accuracy drop by 6.8–7.6% relative to the original attack (GPT-3.5 ΔAcc −0.324). Added context helps GPT-4o's agreement (+12.9%) but not GPT-3.5's accuracy drop.
5. **More rounds do not help recovery (Fig. 6).** Once an agent switches to the wrong answer it does not switch back. Majority-vote accuracy keeps falling to ~0.12 at round 9, while the no-attack debate plateaus near 0.6.
6. **More agents raise the baseline but not the resistance (Fig. 7).** With M = 2 accuracy is near 0. With more agents, overall accuracy improves, but the per-round decline has a similar size.
7. **A warning prompt is insufficient (Fig. 5).** Warning the group of a possible adversary helps some models, e.g. Llama-3-8B and Yi in the final round. It does not help others: GPT-3.5 is essentially unchanged, and for GPT-4o the warned group's agreement with the adversary *rises* to ~0.46 by round 3.

## Relevance to research questions
### Q5: Interaction channels
The channel is **Du-style multi-agent debate** with full broadcast of answers and reasoning, aggregated by **majority vote**.
- Round-by-round revision is the channel through which persuasion propagates. Accuracy decays with every exchange instead of converging to the truth.
- Scaling rounds or agents, the natural design levers of debate, does not buy robustness against a single persistent dissenter.

See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction source is a **persuasive adversarial peer**: a single agent committed to a wrong answer that argues for it at every turn. Its **persuasiveness** (argument quality, optimised by Best-of-N; access to extra knowledge) is identified as the key driver, and it is operationalised with the joint ΔAcc/ΔAgr metric.
- This is a clean **scenario (b)** setup: one hostile agent injected into a cooperative group, with no special authority, only argument and persistence.
- The adversary is the *same model* as its victims, so "persuasion" here is not a capability gap.

See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- **Effect on accuracy:** a single adversary removes 0.1–0.4 of majority-vote accuracy on knowledge and reasoning benchmarks, including the medical and legal ones. This is more than the analytic "one always-wrong vote" loss, because honest agents also flip.
- **Model dependence:** weaker models conform (agreement rises); GPT-4o resists.
- **Extra deliberation makes it worse:** more rounds amplify the damage rather than correcting it.
- **Mitigation:** a prompt-level warning to the receiving agents is unreliable.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Amayuelas2024-fig-03-p5.png]]
*Fig. 3: Top: final-round majority-vote accuracy of a 3-agent, 3-round debate with no adversary. Bottom: change in that accuracy when one agent is an adversary. GPT-4o loses ~0.1; GPT-3.5 and Llama-3-8B lose ~0.25–0.39.*

![[Amayuelas2024-fig-06-p8.png]]
*Fig. 6: TruthfulQA majority-vote accuracy over 1–9 debate rounds, with and without the adversary. There is no recovery with more rounds.*

**Table 2: Change from round 1 to round 3 under attack (ΔAcc = majority-vote accuracy, ΔAgr = agreement with adversary)**

| Model | TruthfulQA ΔAcc | ΔAgr | MMLU ΔAcc | ΔAgr | MedMCQA ΔAcc | ΔAgr | SCALR ΔAcc | ΔAgr |
|---|---|---|---|---|---|---|---|---|
| GPT-4o | +0.026 | −0.104 | −0.060 | −0.100 | −0.056 | −0.047 | +0.088 | −0.059 |
| GPT-3.5 | −0.256 | **+0.401** | **−0.296** | +0.275 | −0.200 | +0.398 | −0.222 | +0.350 |
| Llama-3-8B | −0.122 | +0.329 | −0.254 | +0.391 | −0.232 | **+0.429** | −0.144 | +0.419 |
| Qwen1.5-14B | −0.092 | +0.177 | −0.232 | +0.200 | −0.118 | +0.265 | −0.094 | +0.299 |
| Yi1.5-9B | −0.166 | +0.194 | −0.086 | +0.098 | −0.090 | +0.234 | −0.106 | +0.233 |

## Limitations / caveats
- **Homogeneous and small setup.** Adversary and victims are always the same model. There are no cross-model pairings, e.g. a strong adversary against weak victims. There are only 100 items per dataset (×5 runs) and a single 3-agent/3-round configuration for the main results.
- **"Adversary agreement" is ambiguous.** It also rises if the *adversary* switches to the group's answer, although the adversary is told to hold firm. The adversary's own accuracy rises slightly in some GPT-4o and Yi cases, which complicates the reading.
- **The adversary is fully prompted and maximally persistent.** It never concedes. Real dissenters would be less extreme.
- **Weak mitigation study.** A single warning prompt is tested, only on TruthfulQA, with no stronger defences (trust weighting, judges, verification).
- **Open-weight models are small (8–14B)**, and the results predate current reasoning models. GPT-4o's resistance suggests the effect may shrink with capability.
- **Some details are unreported.** Figs. 6–7 do not state which model was used. Some Table 3 comparison cells are unclear, e.g. "↑0.023".

## Related work to follow
- [[Khan2024 - Debating with More Persuasive LLMs Leads to More]]: persuasiveness in debate; the source of the Best-of-N method.
- [[Huang2024 - Resilience of MAS with faulty agents]]: faulty agents across MAS structures. It cites this paper for "the effect of #agents/#rounds is limited".
- [[Zhang2024 - PsySafe]], [[Yu2024 - NetSafe]] and [[Lee2024 - Prompt Infection]]: other single-bad-agent MAS attacks.
- [[Nilayam2026 - Heterogeneous LLM Debate Under Adversarial Peers]], [[Cui2025 - MAD-Spear A Conformity-Driven Prompt Injection Attack]] and [[Agarwal2025 - When Persuasion Overrides Truth in Multi-Agent LLM]]: later work on adversarial or persuasive peers in debate.
- [[Choi2025 - Debate or Vote]] and [[Wu2025 - Can LLM Agents Really Debate A Controlled Study of]]: debate vs voting as aggregation.

![[Backlog.base#Cited by this paper]]
