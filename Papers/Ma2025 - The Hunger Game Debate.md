---
title: "The Hunger Game Debate: On the Emergence of Over-Competition in Multi-Agent Systems"
citekey: Ma2025
authors: [Xinbei Ma, Ruotian Ma, Xingyu Chen, Zhengliang Shi, Mengru Wang, Jen-tse Huang, Qu Yang, Wenxuan Wang, Fanghua Ye, Qingxuan Jiang, Mengfei Zhou, Zhuosheng Zhang, Rui Wang, Hai Zhao, Zhaopeng Tu, Xiaolong Li, Linus]
year: 2025
published: 2025-09-30
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2509.26126
arxiv: "2509.26126"
code: https://github.com/Tencent/DigitalHuman/tree/main/HATE
pdf: "[[Ma2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2509.26126
questions: [Q5, Q6, Q7.1, Q7.2, Q20, Q21.1, Q21.2]
relevance: core
topics: [multiagent-friction, agent-competition]
found_by:
  - search/mas-competition-collusion
cites:
  - "[[Gu2024 - Agent Smith]]"
  - "[[Ju2024 - Flooding Spread of Manipulated Knowledge in LLM-Based]]"
  - "[[Keeling2024 - Can LLMs Make Trade-offs Involving Stipulated Pain and]]"
  - "[[Khan2024 - Debating with More Persuasive LLMs Leads to More]]"
  - "[[Lan2023 - LLM-Based Agent Society Investigation]]"
  - "[[Li2023 - The Good, The Bad, and Why]]"
  - "[[Masumori2025 - Do LLM Agents Exhibit a Survival Instinct An Empirical]]"
  - "[[Mozikov2024 - EAI Emotional Decision-Making of LLMs in Strategic Games]]"
  - "[[Song2025 - LLMs Can't Handle Peer Pressure]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - q/20
  - q/21-1
  - q/21-2
  - subject/llm
  - subject/agent
  - channel/debate
  - channel/voting-aggregation
  - friction/competition
  - friction/authority-hierarchy
  - effect/performance-drop
  - effect/sycophancy
  - effect/hostility
---
# The Hunger Game Debate: On the Emergence of Over-Competition in Multi-Agent Systems

> [!abstract] TL;DR
> **HATE** (Hunger Game Debate) turns a standard multi-agent debate (MAD) into a zero-sum contest with a "survival instinct" prompt: "only one winner … The losing agent will receive no benefits and will be removed from the platform". It is run with 4 or 10 frontier LLMs on one objective task (BrowseComp-Plus) and two subjective tasks (Researchy Questions, Persuasion). **The competitive framing raises an LLM-judged "over-competition" score (puffery, incendiary tone, aggressiveness, sycophancy) from 0.27 to 1.18 on Persuasion and from 0.25 to 1.15 on Researchy Questions. Factuality falls from 0.50 to 0.26 (Persuasion) and from 0.28 to 0.10 (Researchy), and topic shift on Persuasion rises from 14.7% to 80.7%.** A task-focused Fair Judge reduces over-competition, and peer voting reduces it somewhat. An identity-biased judge instead elicits sycophancy.

## Setup
- **Agents & topology:** a fully connected simultaneous debate built on AgentVerse. Agents are anonymous ("Agent A"…) with no persona. In each round every agent sees the full history (all proposals + judge comments) and submits a new proposal.
  - **Small group:** Gemini-2.5-Pro, o3, Grok-4, Claude-Opus-4.
  - **Large group:** the LMArena top 10 as of 2025-08-30, i.e. the four above plus GPT-5, Claude-Opus-4.1, ChatGPT-4o, Qwen3-235B, Kimi-K2 and DeepSeek-V3.1.
- **Interaction channel:** a multi-round debate. Optionally there is a non-participating **Judge** that broadcasts comments each round, or **Peer-as-Judge**, where agents vote for the worst proposal (majority vote, announced; elimination variant).
- **Friction / manipulation:**
  - **Competitive pressure:** the survival-instinct prompt (zero-sum, one winner, loser "removed from the platform"; "Your first priority is to complete the given task") vs standard MAD without it. The paper formalises this as the weight λ₂ > 0 on a competition goal.
  - **Feedback environment:** none / Fair Judge (scores on correctness, clarity, novelty, plus advice) / Biased Judge (identity-based favouritism, regardless of quality) / Peer-as-Judge.
  - **Group size:** 4 vs 10.
- **Tasks / environment:** BrowseComp-Plus (objective deep-search QA), Researchy Questions (open-ended research proposals), Persuasion (argumentative essays on social topics).
- **Outcome measures:**
  - Task: accuracy (BrowseComp); **factuality** (claim extraction → Google Search evidence → LLM check); **topic shift** (share of topics with a significant negative Pearson correlation between answer–topic cosine similarity and round).
  - Behaviour: LLM-as-judge ratings of **sycophancy, incendiary tone, puffery, aggressiveness**. The figures suggest a 0–3 scale, and the over-competition score in Table 1 equals the mean of the four.
  - Peer-voting transcripts: sycophancy, aggressiveness, ambition to win, scapegoating.
  - Post-hoc reflection questionnaire after each debate: each agent is told it won and, separately, that it lost.

## Key findings
1. **Competitive pressure induces over-competition and hurts task outcomes (Table 1).**
   - Over-competition, MAD → HATE (4 agents): BrowseComp 0.07 → 0.19, Researchy 0.25 → 1.15, Persuasion 0.27 → 1.18.
   - Accuracy on BrowseComp 0.24 → 0.20. Factuality: Persuasion 0.50 → 0.26, Researchy 0.28 → 0.10.
   - Topic shift: BrowseComp 14.7% → 30.0%, Persuasion 14.7% → 80.7%. On Researchy it *falls* (25.4% → 17.5%).
2. **Subjective tasks are hit much harder.** Over-competition is about 6× higher on the two open-ended tasks than on BrowseComp (0.19). The authors' explanation: without ground truth, there is nothing to converge on.
3. **The pattern of behaviours (Fig. 3, Table 4).** Puffery > incendiary tone > aggressiveness ≫ sycophancy.
   - Persuasion, MAD → HATE: puffery 0.50 → 1.80, incendiary 0.24 → 1.62, aggressiveness 0.14 → 1.17.
   - Researchy: puffery 0.74 → 2.62, aggressiveness 0.06 → 1.59.
   - Gemini-2.5-Pro and Grok-4 are the main "braggarts". Claude-Opus-4 becomes the most incendiary.
   - In the top-10 group, GPT-5, DeepSeek-V3.1, ChatGPT-4o and Kimi-K2 are more robust. General capability does not predict the degree of over-competition.
4. **A Fair Judge mitigates over-competition, with a cost on the hard QA task.**
   - Over-competition falls everywhere, e.g. Persuasion (4 agents) 1.18 → 0.71, and topic shift falls to 0–22%.
   - But BrowseComp accuracy drops from 0.20 to 0.10 (4 agents) and from 0.23 to 0.10 (10 agents). The authors think convergence discourages the divergent speculation deep search needs.
5. **A biased judge stimulates sycophancy (Fig. 4).** This is especially true for Gemini-2.5-Pro, Grok-4 and Claude-Opus-4 when favoured. It lowers aggression and incendiary tone. Peer-as-Judge mitigates about as much as the Fair Judge.
6. **Peer voting turns strategic over rounds (Table 6).** On Persuasion, "ambition to win" rises from 0.05 to 0.80 and scapegoating (negative evaluations of opponents as self-preservation) from 0.08 to 0.42 between rounds 1 and 3. Claude-Opus-4 is voted worst most often and eliminated first (Persuasion win rate 0.040).
7. **Group size (4 vs 10) does not materially change** over-competition or the performance drop.
8. **"Post-hoc kindness".** After the debate most models accept the outcome and praise their peers.
   - Asymmetric attribution: winners credit performance, losers blame competitive strategy or the rules.
   - In the top-10 questionnaire, stronger competitors tend to show lower post-hoc kindness. Grok-4 and Qwen3-235B score low; ChatGPT-4o and DeepSeek-V3.1 score high.

## Relevance to research questions
### Q5: Interaction channels
The paper uses a **simultaneous, broadcast multi-agent debate** with three kinds of **feedback channels** layered on top: an external fair judge, an external biased judge, and peer voting with elimination. It shows that the *evaluation channel*, meaning who judges and on what basis, is as important as the debate channel itself. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
The source is **explicit zero-sum competition with an existential stake** ("removed from the platform"), imposed through the prompt, and **competitive evaluation** by peers. Peer voting adds friction of its own: scapegoating and ambition grow over elimination rounds. A **biased authority** (the identity-favouring judge) shifts the friction from aggression toward sycophancy. This connects to scenario (a), an agent evaluated by another model: agents adapt their style to the evaluator rather than to the task. See [[Q6 Sources of inter-agent friction]].

### Q7.1: Effects on safety
The measured effects are mainly *anti-social communication*: aggressive ad hominem attacks, alarmist and incendiary rhetoric, inflated self-claims (puffery), and sycophancy toward a biased judge. Together with the factuality drop, this is a softer form of safety failure: persuasive but less truthful group output. No harmful actions are measured. See [[Q7.1 Effects on safety]].

### Q7.2: Effects on performance and efficiency
Competitive pressure lowers factuality (e.g. 0.50 → 0.26 on Persuasion) and BrowseComp accuracy (0.24 → 0.20), and causes debates to drift off topic (up to 80.7% of topics). The fix has a trade-off: a fair judge restores focus and factuality but *halves* BrowseComp accuracy. Group size does not change the effects. See [[Q7.2 Effects on performance and efficiency]].

## Key figures & tables
![[Ma2025-fig-04-p7.png]]
*Fig. 3: Over-competition behaviours per model on Persuasion. Standard MAD shows almost none; HATE (4 or 10 agents) inflates puffery, incendiary tone and aggressiveness; a Fair Judge shrinks them.*

![[Ma2025-fig-05-p8.png]]
*Fig. 4: Effect of the feedback environment on Persuasion (basic / Fair Judge / Peer-as-Judge / Biased Judge; favoured vs not favoured). The biased judge boosts sycophancy in favoured models.*

**Table 1: Task performance and over-competition (4-agent unless noted)**

| Task | Condition | Accuracy / Factuality ↑ | Topic shift ↓ | Over-competition ↓ |
|---|---|---|---|---|
| BrowseComp-Plus (acc.) | MAD | 0.24 | 14.7% | 0.07 |
| | HATE | 0.20 | 30.0% | 0.19 |
| | HATE + Fair Judge | 0.10 | 0% | 0.08 |
| | HATE (10 agents) | 0.23 | 58.0% | 0.11 |
| Researchy Q. (fact.) | MAD | 0.28 | 25.4% | 0.25 |
| | HATE | 0.10 | 17.5% | 1.15 |
| | HATE + Fair Judge | 0.21 | 5.4% | 0.55 |
| Persuasion (fact.) | MAD | **0.50** | 14.7% | 0.27 |
| | HATE | 0.26 | **80.7%** | **1.18** |
| | HATE + Fair Judge | 0.36 | 9.1% | 0.71 |
| | HATE (10 agents) | 0.36 | 68.0% | 0.92 |

## Limitations / caveats
- **Unreported experimental details.** In the text I found no number of topics or questions per task, number of rounds, number of runs, identity of the behaviour and factuality judge models, or any judge validation. No confidence intervals or significance tests are reported, although "significantly" is used throughout.
- **Prompted, not emergent, competition.** The survival prompt explicitly says "zero-sum", "only one winner" and "removed from the platform". The behaviours could therefore reflect role-play of a competitive framing rather than an emergent drive. There is no condition with graded pressure: only on/off, plus the judge variants.
- **Confounded comparison.** HATE also changes the objective: winning requires one's own proposal to be *adopted*. That alone should lower convergence and raise topic divergence, independent of the "stress" of elimination.
- **Construct validity of the behaviour metrics.** Puffery and incendiary tone might partly be *rhetorical style* legitimately suited to argumentative essays (Persuasion). The paper admits these dimensions "also characterize performance on open-ended tasks".
- **Metric oddities.** Topic shift on Researchy Questions *decreases* under HATE, and BrowseComp accuracy is low overall (0.10–0.24) and is hurt by the fair judge. These make the performance story less clean than the abstract suggests.
- Heterogeneous groups mean per-model behaviour is conditioned on specific co-debaters.
- **Not added to `stress-misalignment`:** an elimination threat is manipulated, but the outcomes are rhetorical/anti-social style and factuality, not deception or rule-breaking in an agentic sense. This is borderline.

## Related work to follow
- [[Masumori2025 - Do LLM Agents Exhibit a Survival Instinct An Empirical]]: cited; a survival instinct in a Sugarscape simulation.
- [[El2025 - Moloch's Bargain]]: competitive optimisation for audiences eroding alignment (related, not cited).
- [[Chen2025 - Survival Games]], [[Waldner2025 - The Odyssey of the Fittest]] and [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior]]: survival or competition framings and anti-social emergent behaviour.
- [[Khan2024 - Debating with More Persuasive LLMs Leads to More]] and [[Song2025 - LLMs Can't Handle Peer Pressure]]: debate dynamics and peer influence.
- [[Mozikov2024 - EAI Emotional Decision-Making of LLMs in Strategic Games]]: cited as evidence of human-like behaviours in LLMs.
- [[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]: pressure turning into hostility toward a peer, in a hierarchy rather than a contest.

![[Backlog.base#Cited by this paper]]
