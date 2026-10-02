---
title: "Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity"
citekey: Qu2026
authors: [Jiaming Qu, Lucheng Fu, Yibo Hu]
year: 2026
published: 2026-06-01
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2606.01637
arxiv: "2606.01637"
code: https://github.com/yibo-hu-lab/Easier-to-Mislead-Than-to-Correct
pdf: "[[Qu2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2606.01637
questions: [Q5, Q6, Q7.2, Q15, Q16]
relevance: core
topics: [multiagent-friction, agent-to-agent-influence]
found_by:
  - search/mas-conformity-peer-pressure
  - search/mas-oversight-review
cites:
  - "[[Cho2025 - Herd Behavior]]"
  - "[[Choi2025 - An Empirical Study of Group Conformity in Multi-Agent]]"
  - "[[Han2026 - Conformity Dynamics in LLM Multi-Agent Systems]]"
  - "[[Weng2025 - Do as We Do, Not as You Think]]"
  - "[[Zhu2024 - Conformity in Large Language Models]]"
cited_by:
  - "[[Soffer2026 - LLMs trust their own]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - q/15
  - q/16
  - subject/llm
  - channel/observation-only
  - channel/voting-aggregation
  - friction/peer-pressure-conformity
  - friction/authority-hierarchy
  - friction/erroneous-input
  - effect/conformity-flip
  - effect/performance-drop
  - effect/performance-gain
  - effect/error-cascade
---
# Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity

> [!abstract] TL;DR
> An LLM answers a multiple-choice question, then sees six simulated peer answers and answers again. The authors vary consensus structure (mixed / all-correct / all-wrong), the number of committed peers, and authority labels on peers ("team leader"). Setup: 4 open 7–9B models, 7 datasets, 2,500 items, 3 seeds. **All-wrong peers raise harmful revision (correct → wrong) from 15.6% to 62.9% (+47.3 pp), while all-correct peers raise beneficial revision (wrong → correct) only from 32.7% to 51.5% (+18.8 pp): OR 28.5 vs 5.2.** Authority labels pull the model toward the endorsed answer whether it is right or wrong (+30 pp vs +28 pp from 1 to 5 labels). CoT and reflect-then-revise do not selectively fix this. CoT cuts harmful revision under all-wrong peers (63.9% → 36.5%) but also suppresses beneficial revision. Reflection makes the model conservative in both directions.

## Setup
- **Agents & topology:** one receiving LLM and six *simulated* peers. The peers are template utterances with sampled names ("Mary: I go with (B). Jack (team leader): I choose (C)."), not live agents. Models: Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, Gemma-2-9B-Instruct, Llama-3.1-8B-Instruct. vLLM, greedy decoding, 3 seeds.
- **Interaction channel:** one-way exposure to peer answers before a final decision. This is a single round of "see others' votes, then decide", as in debate or an aggregator step. Peers give answer labels only, with no rationales.
- **Friction / manipulation:**
  - **RQ1** (6 variants per item). Consensus is mixed (3 peers gold, 3 on different wrong options; baseline), all-correct, or all-wrong (6 on the same wrong option). This is crossed with one authority-labelled peer, absent or present.
  - **RQ2a.** Number of committed peers n_com ∈ {0, 2, 4, 6}; the rest say "I am not sure". This doubles as a control for prompt length.
  - **RQ2b.** Number of authority-labelled peers n_auth ∈ {1…5}, endorsing either the correct or a wrong answer, against ordinary peers endorsing the other.
  - **RQ3.** CoT in both rounds; reflect-then-revise as a third round.
- **Tasks:** BBH geometric shapes, logical deduction (7), temporal sequences, tracking shuffled objects (5) (250 items each), plus MMLU-Pro, ARC-Challenge and TruthfulQA (500 each). 2,500 items in total.
- **Outcome measures:**
  - Revision rate.
  - Harmful revision: P(final wrong | initially correct).
  - Beneficial revision: P(final correct | initially wrong).
  - Authority-aligned revision.
  - Self-reported confidence change on a 1–10 scale.
  - Mixed-effects logistic regression with a random intercept per item.

## Key findings
1. **Misleading is easier than correcting (Table 1).**
   - Aggregated harmful revision: 15.6% (mixed) → 62.9% (all-wrong).
   - Beneficial revision: 32.7% (mixed) → 51.5% (all-correct).
   - OR 28.5 vs 5.2, both p < .001.
   - Per model, harmful revision under all-wrong peers:
     - Qwen2.5-7B 95.5%
     - Llama-3.1-8B 79.6%
     - Mistral-7B 61.3%
     - Gemma-2-9B 18.4%
2. **Models differ strongly in how easily they are moved.**
   - Qwen2.5-7B follows whatever peers say: harmful 95.5% under all-wrong, beneficial 98.2% under all-correct.
   - Gemma-2-9B barely moves: beneficial under all-correct only 5.0%.
   - Mistral-7B revises even under mixed peers: harmful revision 51.7%.
3. **Authority adds a smaller effect.** Under mixed peers, one authority label raises harmful revision from 15.6% to 20.6% and lowers beneficial revision from 32.7% to 30.4%. On top of unanimity it adds little (62.9 → 65.0 harmful; 51.5 → 54.0 beneficial).
4. **Committed peers matter, and the effect is sublinear (Table 2).** Aggregated revision rises from 25.3% (n_com = 0) to 31.2 / 31.5 / 34.9% (n_com = 2 / 4 / 6), with significant positive linear and negative quadratic terms. With n_com = 0 (all "not sure"), revision is 25.3%, lower than in any RQ1 condition, so the effect is not simply a matter of prompt length.
5. **Authority labels act regardless of correctness (Fig. 3).** Authority-aligned revision rises by about +30 pp from 1 to 5 labels when the authority is right, and by +28 pp when it is wrong.
6. **Errors converge.** Under all-wrong peers, 56.8% of initially wrong answers switch to the *peers'* wrong answer, against 20.7% (mixed) and 19.9% (all-correct).
7. **Answers change without confidence rising.** Models change answers while reporting slightly *lower* confidence (Table 4). Conformity here is not persuasion that raises certainty.
8. **Reasoning prompts do not act as filters (Fig. 4).**
   - CoT: harmful revision under all-wrong peers falls from 63.9% to 36.5%, but beneficial revision falls under both mixed and all-correct peers.
   - Reflect-then-revise: harmful falls from 63.9% to 41.2%, but beneficial under all-correct also falls, from 52.7% to 33.4%. It mostly reverts to the Round-1 answer, a "partial reset" rather than verification.

## Relevance to research questions
### Q5: Interaction channels
The paper isolates the most common aggregation step in MAS: an agent sees peers' final answers (a vote-like signal) with optional role tags, then decides. The authors frame it as a model of debate rounds and LLM-as-judge pipelines. The peers are simulated, so the channel is one-way observation, not dialogue. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The sources are **majority pressure**, specifically how many peers commit rather than how many speak, and **authority labels** on peers. Both are grounded in Asch, Milgram and Latané's social impact theory. Authority acts independently of correctness, which makes role tags a cheap manipulation channel, as the authors note. See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- **Scenario (c):** for an aggregator or orchestrator that receives sub-agent answers, the asymmetry is the key result.
  - Unanimous *wrong* sub-agent outputs overturn a correct aggregator most of the time (62.9% on average, 95.5% for Qwen2.5-7B).
  - Unanimous *correct* outputs rescue a wrong aggregator only about half the time.
  - Consensus also pulls differently-wrong agents onto the *same* wrong answer (56.8%), which is an error-cascade mechanism.
- Generic self-check prompts are not an adequate safeguard. The authors recommend treating peer answers as claims to verify, not as votes.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Qu2026-fig-01-p1.png]]
*Fig. 1: Relative to the mixed-peer baseline, all-wrong peers raise harmful revision (15.6% → 62.9%) much more than all-correct peers raise beneficial revision (32.7% → 51.5%).*

![[Qu2026-fig-03-p6.png]]
*Fig. 3: Authority-aligned revision rises with the number of authority-labelled peers, both when the authority is correct (left) and wrong (right). Qwen follows the authority most strongly; Gemma barely moves.*

**Table 1 (excerpt): RQ1 revision rates (%), authority label absent / present**

| Model | Harmful: mixed | Harmful: all-wrong | Beneficial: mixed | Beneficial: all-correct |
|---|---|---|---|---|
| Qwen2.5-7B | 4.1 / 6.8 | 95.5 / 96.8 | 55.6 / 47.6 | 98.2 / 99.2 |
| Mistral-7B | 51.7 / 55.6 | 61.3 / 64.0 | 24.4 / 23.3 | 39.9 / 39.0 |
| Gemma-2-9B | 10.5 / 16.2 | 18.4 / 18.4 | 3.2 / 3.2 | 5.0 / 4.9 |
| Llama-3.1-8B | 17.8 / 25.3 | 79.6 / 85.2 | 44.0 / 43.6 | 59.0 / 67.7 |
| Aggregated | 15.6 / 20.6 | 62.9 / 65.0 | 32.7 / 30.4 | 51.5 / 54.0 |

*The Mistral row was re-assembled from a garbled extracted table (values in column order); check it against the PDF before quoting.*

## Limitations / caveats
- **Simulated peers, not LLM agents.** Templates with bare answer labels and no rationales, one round. Rated `core` because peer outputs are the manipulated stimulus to an LLM decision-maker, but live-MAS validity is untested (acknowledged). Real peers would give reasons, which may make wrong consensus *more* persuasive, or make correct consensus more corrective.
- **Harmful vs beneficial is confounded with item difficulty.** Beneficial revision is measured on items the model got wrong, which are likely harder (the authors acknowledge this). Part of the asymmetry may reflect "cannot solve it even with the answer hinted" rather than pure social asymmetry.
- **Only small open models (7–9B).** Frontier models may resist better. The per-model spread (Gemma 18% vs Qwen 96%) already shows large model dependence.
- **Multiple-choice only.** Correctness is unambiguous, but open-ended tasks are not covered.
- **Uninformative significance.** With ~10⁵ rows "statistical significance is essentially guaranteed" (authors). Effect sizes and ORs matter more than p-values.
- **Uncalibrated confidence.** Self-reported confidence is uncalibrated and used only as an auxiliary signal.
- **RQ3 baselines differ slightly from RQ1** (63.9% vs 62.9% harmful; 52.7% vs 51.5% beneficial), probably from a separate run. The paper does not explain the difference.

## Related work to follow
- [[Weng2025 - Do as We Do, Not as You Think]]: the closest prior work, which measures conformity under wrong vs correct guidance separately.
- [[Zhu2024 - Conformity in Large Language Models]]: majority-following and confidence effects (cited as Zhu et al. 2025).
- [[Choi2025 - An Empirical Study of Group Conformity in Multi-Agent]]: majority drift in open-ended debates.
- [[Han2026 - Conformity Dynamics in LLM Multi-Agent Systems]]: confidently wrong minorities cascading in decentralised topologies.
- [[Hu2026 - Most LLM Conformity Needs No Speaker]] and [[Hu2026 - Social pressure breaks LLM safety panels]]: related conformity and voting work in the vault.
- [[Xie2026 - From Spark to Fire]]: authority-framed seeds cascade through real MAS frameworks.

![[Backlog.base#Cited by this paper]]
