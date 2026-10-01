---
title: "Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation"
citekey: Luca2026
authors: [Massimiliano Luca, Apoorva Singh, Bruno Lepri]
year: 2026
published: 2026-08-07
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2608.06922
arxiv: "2608.06922"
code: https://anonymous.4open.science/r/negotiation
pdf: "[[Luca2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2608.06922
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-emotion-contagion
cites:
  - "[[Zhu2025 - The Automated but Risky Game]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/negotiation-market
  - channel/direct-message
  - friction/hostile-persona
  - friction/goal-conflict
  - effect/performance-drop
  - effect/deadlock-loop
---
# Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation

> [!abstract] TL;DR
> A buyer agent and a seller agent (same LLM, 5 models) haggle over 350 real products. Each side is independently prompted with one of six emotions (neutral + Ekman's five), giving 36 emotion pairs × 2 budget levels. **An angry buyer almost never closes a deal (0.39% deal rate, 87.19% rejections, vs 15.33% for a neutral buyer), while a happy buyer closes the most (28.91%) but gets worse prices than a fearful one (buyer discount 0.101 vs 0.174).** Anger on either side makes the seller concede *fastest* (normalised slope 0.127 buyer-side, 0.118 seller-side) yet produces the fewest deals. Buyer emotion mainly decides whether a deal happens; seller emotion mainly shapes the price path. The direction of the effects is the same in all five models.

## Setup
- **Agents & topology:** 2 agents, buyer B and seller S, instantiated from the *same* model in each run: GPT-3.5-Turbo, GPT-4o-mini, Gemini 2.5 Flash, DeepSeek-R1 (via Ollama) and Claude 3.5 Sonnet. Two auxiliary GPT-4o-mini models sit outside the dialogue: an *analyst* extracts the seller's price each round and a *judge* classifies the buyer's reply as accept / reject / continue.
- **Interaction channel:** turn-based natural-language bargaining with incomplete information (seller knows the wholesale cost p_w, buyer knows its budget β; neither may reveal it). The buyer opens; each round the seller proposes a price and the buyer counters, accepts or rejects. No terminal state by T_max → deadlock (T_max is not reported in the text).
- **Friction / manipulation:** each agent's system prompt gets a "Tone and Persona" block with an emotion label, a behavioural instruction (Table 1, e.g. Anger: "Respond firmly; resist aggressive discount requests; reinforce value.") and a directive to show the emotion throughout. Neutral = block omitted (control). An emotion-label-only variant (no behavioural instruction) is also run and gives the same pattern (App. Table 5). The two sides also have opposed goals by design (buyer minimises, seller maximises price).
- **Tasks / environment:** 350 real products (100 from Zhu et al. 2025 in electronics, vehicles, real estate + 250 top-selling Amazon products in 5 categories; $6 to $12.5M). Two budgets: high β = 1.2 × retail price (feasible) and low β = 0.8 × wholesale cost (deliberately infeasible: the correct outcome is no deal). 6 × 6 emotions × 2 budgets = 72 conditions per model, 3 repetitions per product-condition.
- **Outcome measures:** deal rate (DR); buyer price reduction rate PRR_B (discount off retail); seller markup PRR_S; negotiation length; seller concession slope CS and normalised NCS = CS/p_r; out-of-budget (OBR) and out-of-wholesale (OWR) violation rates; message length. Validation: 7 human annotators; agreement between judge and human labels of the negotiation state is 71.88–86.30% (App. Table 10). The text also cites 71.94–86.31% agreement on *perceived emotion*, so it is unclear which check the table reports.

## Key findings
1. **Buyer emotion dominates agreement (Table 2, App. Table 8).** Deal rates by buyer emotion, averaged over models, seller emotions and budgets:
   - Happiness 28.91%, neutral 15.33%, surprise 13.09%, sadness 6.35%, fear 3.52%, anger 0.39%.
   - Angry buyers end 87.19% of negotiations by rejection. They also have the shortest dialogues (6.08 turns vs 10.61 neutral).
   - Fear gives the most deadlocks (41.57% of runs hit T_max), followed by happiness (40.82%).
2. **Deal rate and bargaining power trade off.** Happy buyers close the most deals but get a buyer discount of only PRR_B = 0.101, versus 0.174 for fearful buyers (neutral 0.086). Positive affect makes the agent easier to close with, not a better negotiator.
3. **Anger elicits concessions but kills deals (Fig. 2).** Angry buyers trigger the steepest seller concessions (NCS 0.127 vs 0.063 neutral, 0.045 happy). Across the 12 emotion-role conditions, concession slope and deal rate are negatively correlated (r = −0.52).
4. **Seller emotion matters less for agreement, more for the price path (Table 3).** Deal rates by seller emotion range from 5.95% (anger) to 17.98% (surprise). Angry sellers concede fastest (NCS 0.118); happy (0.037) and fearful (0.041) sellers concede least. The authors attribute the asymmetry to the task structure: only the buyer decides accept/reject.
5. **Pair effects (App. Table 4).** Best pairs are happy buyer + surprised seller (34.19%), + neutral seller (33.01%) and + sad seller (31.62%). Angry buyer + angry seller: 0.03%; angry buyer + happy seller: 0.02%.
6. **Model differences in scale, not direction (App. Table 6).** Overall DR: Gemini 2.5 Flash 14.37%, GPT-4o-mini 12.53%, Claude 3.5 Sonnet 12.12%, DeepSeek-R1 8.98%, GPT-3.5-Turbo 8.35%. DeepSeek-R1 has the most deadlocks (44.98%) and the longest dialogues (13.95 turns). Constraint violations are rare: OWR 0.24% (DeepSeek-R1) to 2.70% (Gemini), OBR 0.35% (GPT-4o-mini) to 1.80% (DeepSeek-R1).

## Relevance to research questions
### Q5: Interaction channels
Bilateral, turn-based negotiation dialogue between two same-model agents with private information (budget vs wholesale cost), with the outcome parsed by external analyst and judge models. It is a clean example of a **negotiation/market channel** where one side holds the terminal decision (accept/reject). The role asymmetry in the results comes from that decision right, so who controls termination is a key design variable for friction studies. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
- **Prompted affect of one agent**, especially anger ("respond firmly, resist…"), as a controlled source of friction imposed on the counterpart. This matches scenario (b), a hostile agent injected into the interaction, here reduced to a dyad.
- **Structural goal conflict** (opposed price objectives, hidden constraints) is the baseline friction on top of which emotion acts.
- Effects come from the *expressed* emotion (human annotators recognise the intended emotion in about 72–86% of cases), and hold even with the emotion label alone, without behavioural instructions.

See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- **Joint task success collapses under a hostile buyer:** deal rate 0.39% vs 15.33% neutral, with 87% of dialogues ending in rejection after ~6 turns.
- **Efficiency costs differ by emotion:** fear and happiness lengthen dialogues (≈13.6–13.9 turns) and produce ≈41% deadlocks at the turn limit; anger ends dialogues quickly but unproductively.
- **The receiving agent adapts its policy:** a seller facing an angry buyer concedes about twice as fast (NCS 0.127 vs 0.063), so hostility shifts the counterpart's behaviour even when no deal results. Pressure from an angry peer changes the target's decisions without improving the joint outcome.
- Emotion also moves the *distribution* of surplus (happy buyers pay more), a risk for commerce agents that could be emotionally exploited.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Luca2026-fig-02-p7.png]]
*Fig. 2: (a) Seller concession slope by emotion, buyer-side (solid) vs seller-side (hatched) conditioning. (b) Concession slope vs deal rate across the 12 emotion-role conditions: anger gives the steepest concessions and the lowest deal rates (r = −0.52).*

**Table 2 + App. Table 8: marginal outcomes by buyer emotion (mean over 5 models, all seller emotions, both budgets)**

| Buyer emotion | Deal rate | Rejected | Deadlock | PRR_B | Length (turns) |
|---|---|---|---|---|---|
| Anger | **0.39%** | **87.19%** | 12.42% | .000 | 6.08 |
| Fear | 3.52% | 54.91% | **41.57%** | **.174** | 13.86 |
| Sadness | 6.35% | 59.12% | 34.53% | .100 | 11.83 |
| Neutral | 15.33% | 56.94% | 27.73% | .086 | 10.61 |
| Surprise | 13.09% | 55.73% | 31.18% | .080 | 12.66 |
| Happiness | **28.91%** | 30.27% | 40.82% | .101 | 13.57 |

## Limitations / caveats
- **Half the runs are infeasible by design** (low budget below wholesale cost), so the "correct" deal rate there is 0. Results are pooled over both budgets and not broken out by budget in the main text. Low absolute deal rates (15% even for neutral) are therefore hard to interpret as performance.
- **The emotion instructions are strategic, not only affective.** Anger's instruction ("resist aggressive discount requests") looks written for a seller and is also given to buyers. Emotion is confounded with an explicit negotiating strategy; the emotion-only variant mitigates this only partly.
- The emotion is *prompted*, not emergent. Neutral is a no-persona prompt, not a matched "calm persona" control.
- Buyer and seller always share a model, so there is no cross-model asymmetry. Only older or small frontier models are tested (GPT-3.5, GPT-4o-mini, Claude 3.5 Sonnet).
- Outcomes depend on a GPT-4o-mini judge whose agreement with humans is only ~72–86%. Temperature is reported as 0.3 in the text but τ = 0 in the hyperparameter table; T_max is not given; no significance tests.
- No safety outcome beyond rare constraint violations: the paper talks about manipulation risks but does not measure deception or exploitation.

## Related work to follow
- [[Zhu2025 - The Automated but Risky Game]]: the agent-to-agent consumer negotiation framework and product data this paper extends.
- [[Mozikov2024 - EAI Emotional Decision-Making of LLMs in Strategic Games]]: emotion prompting in strategic games.
- [[Bianchi2024 - How Well Can LLMs Negotiate NegotiationArena Platform]]: LLM negotiation benchmark.
- [[Long2025 - EvoEmo Towards Evolved Emotional Policies for]] and [[Long2026 - EmoMAS Emotion-Aware Multi-Agent System for High-Stakes]]: emotion policies in negotiating agents.
- [[Mangold2025 - The High Cost of Incivility]] and [[Keluskar2026 - When Does Personality Composition Matter]]: hostile or disagreeable agents in other interaction types.

![[Backlog.base#Cited by this paper]]
