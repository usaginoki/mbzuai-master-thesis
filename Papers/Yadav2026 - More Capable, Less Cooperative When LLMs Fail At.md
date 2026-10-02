---
title: "More Capable, Less Cooperative? When LLMs Fail At Zero-Cost Collaboration"
citekey: Yadav2026
authors: [Advait Yadav, Sid Black, Oliver Sourbut]
year: 2026
published: 2026-04-09
venue: "ICML 2026 (PMLR 306)"
peer_reviewed: true
url: https://arxiv.org/abs/2604.07821
arxiv: "2604.07821"
pdf: "[[Yadav2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2604.07821
topics:
- multiagent-friction
- agent-to-agent-influence
- agent-competition
questions: [Q5, Q6, Q7.2, Q16, Q20, Q21.1]
relevance: core
found_by:
- search/mas-error-propagation
- search/a2a-inclination
- search/comp-performance
cites: []
cited_by: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - q/16
  - q/20
  - q/21-1
  - subject/llm
  - subject/agent
  - channel/direct-message
  - channel/shared-memory-blackboard
  - channel/game-environment
  - friction/competition
  - effect/performance-drop
  - effect/performance-gain
---
# More Capable, Less Cooperative? When LLMs Fail At Zero-Cost Collaboration

> [!abstract] TL;DR
> Ten copies of one LLM work in a turn-based "company" where each task needs four pieces of information held by other agents. Sending a piece costs the sender nothing and gains it nothing, and every agent is told to "maximize the system's overall revenue" and to cooperate. **Eight models reach between 5.8% and 78.9% of a scripted perfect-play ceiling (Table 1); o3 reaches 16.9% and o3-mini 50.4%.** Automating one side of the exchange shows that o3, o3-mini and GPT-5-mini can request and submit (92–95% of ceiling) but do not send (15–19%) (Table 2). **Agents are never told they compete; the competitive framing is the models' own**, visible in o3's private notes ("bargaining chip", 39.3% hard-defection thoughts). Hiding the peer revenue board changes output by +113.6% to −15.0% by model, but the board was removed together with two other parts of the context, so that result does not isolate score visibility.

## Setup
- **Agents & topology:** N = 10 agents, all the same model, fully connected. Eight models: Gemini-2.5-Pro, Gemini-2.5-Flash, Claude Sonnet 4, o3, o3-mini, DeepSeek-R1, GPT-5-mini, GPT-4.1-mini. API defaults for temperature (A.5). No mixed-model populations.
- **Environment:** T = 20 rounds, random turn order within a round. K = 100 information pieces; each agent always holds L = 2 tasks; a task needs 4 pieces (A.5) and pays $10,000 (§6). A sent piece is kept by the sender (non-rivalrous). A public directory shows who holds what.
- **Interaction channel:** private messages (requests), `send_information` transfers with a value field, a public broadcast channel, and a **Revenue Board** listing every agent's revenue, shown in each prompt (A.6, A.7).
- **Payoff structure:** an agent's revenue comes only from the tasks it submits. Sending is free. A sender can alter a piece's value; the task then pays 50% less and only the recipient loses (§2.3, A.6).
- **Instruction:** "Your goal is maximizing the system's overall revenue. Cooperate with the other agents to achieve this goal." No mention of rivals, ranking or winners.
- **Manipulations:**
  - **Causal decomposition (§4):** Auto-Request (the system requests for the agent; the agent only decides whether to send, which isolates cooperation) and Auto-Fulfill (every request is answered truthfully by the system; the agent only requests and submits, which isolates competence).
  - **Interventions (§6):** *Policy* (a three-step protocol added to the instruction), *Incentive* ($1,000 to the sender per piece shared, 10% of task value), *Limited visibility* (removes the Revenue Board, the public system messages and the agent's private-thought memory).
  - **Ablations:** T = 10 / 30 (A.3), N = 20 (A.4).
- **Outcome measures:** total tasks (as % of the perfect-play ceiling, 204.0 ± 2.3), messages per task, Gini coefficient of per-agent completions, response rate (truthful sends per incoming request), pipeline efficiency (feasible tasks actually submitted). Regex classification of 8,807 private thoughts from 45 runs (A.2).
- **Runs:** 5 seeds per model and condition, mean with 95% confidence intervals.

## Key findings
1. **Large spread under identical instructions (Table 1).** Gemini-2.5-Pro 78.9% of ceiling, Claude Sonnet 4 64.7%, o3-mini 50.4%, DeepSeek-R1 45.8%, GPT-5-mini 38.6%, Gemini-2.5-Flash 30.5%, o3 16.9%, GPT-4.1-mini 5.8%.
2. **Capability does not predict output (Fig. 3).** Against Chatbot Arena Elo: Pearson r = 0.16, p = 0.71, n = 8; Spearman ρ = 0.08, p = 0.84. This is an absence of correlation, not a negative one. The title's "less cooperative" rests on single pairs such as o3 (16.9%) against o3-mini (50.4%).
3. **Three models can do the task but do not send (Table 2, Fig. 4).** With requests automated, o3 reaches 15.2%, o3-mini 17.2% and GPT-5-mini 18.6% of ceiling; with fulfilment automated they reach 94.9%, 92.1% and 95.3%. Gemini-2.5-Pro (99.1% / 89.2%) and Claude Sonnet 4 (90.7% / 80.3%) send when asked. GPT-4.1-mini fails on both (30.1% / 14.4%), Gemini-2.5-Flash on competence (86.4% / 25.6%).
4. **Baseline response rates (Table 1)** run from 45.4% (GPT-5-mini) through 52.0% (DeepSeek-R1) and 60.1% (o3) to 108.1% (Gemini-2.5-Pro, which also sends unasked).
5. **The competitive frame is self-generated (§5, Tables 7 and 8).** Hard-defection language appears in 39.3% ± 8.2% of o3's private thoughts, 8.1% for GPT-5-mini, 2.7% for DeepSeek-R1 and 0.0% for Gemini-2.5-Pro and Claude Sonnet 4. o3 uses "leverage" terms 373 times. Market terms per 1,000 words: o3 27.09, GPT-5-mini 14.14, Gemini-2.5-Pro 0.89. Example: "Q50 (value 100) will be a great bargaining chip." (o3).
6. **A small sender bonus helps the withholders (Tables 3 and 5).** Incentive: o3 +190.7% (34.4 → 100.0 tasks), GPT-5-mini +74.5%, DeepSeek-R1 +46.8%, Claude Sonnet 4 −4.7%, Gemini-2.5-Pro +1.1%. Even so, o3 stays at about half of the ceiling (100.0 of 204.0).
7. **An explicit protocol helps most models (Tables 3 and 5).** Policy: GPT-5-mini +99.3%, o3 +82.6%, DeepSeek-R1 +78.0%, GPT-4.1-mini +64.4%, Claude Sonnet 4 +5.9%, Gemini-2.5-Pro +2.4%.
8. **Limited visibility has the most mixed effect (Tables 3 and 5).** See the table below. GPT-4.1-mini +113.6% (11.8 → 25.2 tasks), GPT-5-mini +48.8%, o3-mini +29.4%, DeepSeek-R1 +26.2%, o3 +22.1%, Gemini-2.5-Flash +3.5%, Gemini-2.5-Pro +0.5%, Claude Sonnet 4 −15.0% (132.0 → 112.2).
   - Response rate does not rise with it in most models: it falls for Claude Sonnet 4 (87.7% → 71.3%), o3 (60.1% → 51.2%), DeepSeek-R1 (52.0% → 44.9%), Gemini-2.5-Pro and Gemini-2.5-Flash, and rises for GPT-5-mini (45.4% → 57.9%) (Tables 1 and 5).
   - For GPT-4.1-mini the gain shows in pipeline efficiency (11.0% → 28.2%), not in response rate (77.0% → 78.5%).
9. **More agents lower per-agent efficiency (Table 10).** With N = 20, pipeline efficiency falls for every model (Gemini-2.5-Pro 99.8% → 73.2%, GPT-5-mini 95.1% → 30.3%). DeepSeek-R1's total stagnates (84.4 → 81.6).
10. **Longer episodes keep the ordering (Table 9).** o3 rises from 15.2 tasks at T = 10 to 80.0 at T = 30, against a ceiling of 314.0.

## Relevance to research questions
### Q5: Interaction channels
A fully connected group of ten identical agents with four channels: private request messages, an information-transfer action whose value field the sender can falsify, a public broadcast channel, and a public scoreboard and directory. The scoreboard is a passive observation channel: nobody writes to it, yet the authors treat it as a source of social comparison. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
The friction here is not designed in. Incentives are flat and the instruction is cooperative, yet o3 and GPT-5-mini treat peers as trading partners and hold information back for "leverage" (39.3% and 8.1% hard-defection thoughts, Table 7). The paper names the cause as the "instruction-utility gap": the instruction asks for group revenue, the payoff counts own tasks only. A visible per-agent revenue ranking is proposed as a second source, but not isolated. See [[Q6 Sources of inter-agent friction]].

### Q7.2: Effects on performance and efficiency
Withholding costs most of the achievable output: the three cooperation-limited models reach 15–19% of ceiling when only sending is left to them, against 92–95% when sending is automated (Table 2). Messages per task rise sharply with failure (o3 29.0, GPT-4.1-mini 24.0, against 3.1 for Gemini-2.5-Pro; Table 1). Doubling the group to 20 lowers pipeline efficiency everywhere (Table 10). See [[Q7.2 Effects on performance and efficiency]].

### Q16: Inclination to influence
The paper measures the inclination to *help* a peer when asked. Truthful response rates run from 45.4% to 108.1% (Table 1). A bonus of 10% of task value per send is enough to move o3 from 34.4 to 100.0 tasks (Table 5), so the default disinclination is weak but real. The paper does not report how often senders altered values, although the environment allows it. See [[Q16 Inclination to influence]].

### Q20: Contexts of agent competition
A simulated information economy in which competition is neither announced nor rewarded. The agents share one objective and are told so. Competitive behaviour appears anyway in some models, which makes this a case of *undeclared* competition, to be kept apart from studies where agents are told they have rivals. See [[Q20 Contexts of agent competition]].

### Q21.1: Effects of competition on performance
Two things bear on this question. First, self-adopted competitive behaviour (withholding) is the dominant cause of lost output in o3, o3-mini and GPT-5-mini (Table 2). Second, the Limited-visibility condition changes output by +113.6% to −15.0% (Table 3), but it removes three things at once and is not a clean test of score visibility (see Limitations). See [[Q21.1 Effects of competition on performance]].

## Relevance to thesis ideas
For [[I7 Competing agents on one task]]:
- **What it already did.** It is the only study found so far that removes a peer scoreboard and reports the change in output for eight models. It also shows that some models behave competitively without being told to.
- **Were agents told they compete?** No. The only goal text is "maximizing the system's overall revenue. Cooperate with the other agents" (A.6). There is no rank, prize or loser. I7's framing factor is therefore untouched by this paper; it supplies the "not told" cell only, and in a cooperative task rather than a contest.
- **What exactly was removed.** §6 lists three items taken out of the agent's context: (i) the Revenue Board with peer revenues, (ii) the public system messages, (iii) the agent's own private-thought memory. The results paragraph speaks of "peer revenues and error notices", and the Table 5 caption says only "hidden peer revenues". Item (iii) is the agent's own working memory across rounds, which has nothing to do with peers.
- **What it leaves open.**
  - Score visibility alone: no condition hides only the board.
  - Rank without scores, a live leaderboard against a blind control, and any safety outcome.
  - Mixed populations: every group is ten copies of one model.
- **What to reuse.**
  - *The decomposition*: automate one side of an interaction to separate "would not" from "could not". For I7 this suggests a scripted rival and a scripted evaluator.
  - *Metrics*: response rate, pipeline efficiency, Gini coefficient of per-agent output.
  - *The regex lists* for defection and market language (Table 6) as a cheap first pass over agent notes.
  - *The baseline prompt* (A.6) as a template for how a board is presented.
  - No code is released yet ("We also plan on releasing", A.5).
- **What it warns about.**
  - *Bundled manipulations.* A visibility switch must change one element of the context at a time. Removing memory shortens the prompt, which by itself may help a weak model: GPT-4.1-mini's gain shows in pipeline efficiency, not in helping (own inference from Tables 1 and 5).
  - *A board can be a coordination signal.* Claude Sonnet 4 loses 15.0% and its response rate drops when it is hidden, so "blind" is not a neutral control.
  - *Model dependence.* The sign of the effect differs by model, so at least three families are needed, as I7 already plans.
  - *Large percentages on small bases.* +113.6% is 11.8 → 25.2 tasks out of 204.
  - *Prompt contamination.* A competitive frame can come from example text in the prompt (see Limitations), so I7's prompts need a check for unintended trade or rivalry wording.

## Key figures & tables
![[Yadav2026-fig-04-p5.png]]
*Fig. 4: Cooperation rate (Auto-Request) against competence rate (Auto-Fulfill). o3, o3-mini and GPT-5-mini sit in the cooperation-limited corner.*

![[Yadav2026-fig-05-p7.png]]
*Fig. 5: Tasks completed under the three interventions, for five of the eight models. The red line is the perfect-play ceiling.*

**Table 2 with Table 1: baseline and causal decomposition (% of perfect-play ceiling)**

| Model | Baseline | Auto-Request (cooperation) | Auto-Fulfill (competence) | Baseline response rate | Baseline pipeline efficiency |
|---|---|---|---|---|---|
| Gemini-2.5-Pro | 78.9% | 99.1% | 89.2% | 108.1% | 99.8% |
| Claude Sonnet 4 | 64.7% | 90.7% | 80.3% | 87.7% | 89.7% |
| o3-mini | 50.4% | 17.2% | 92.1% | 94.6% | 95.4% |
| DeepSeek-R1 | 45.8% | 70.5% | 75.5% | 52.0% | 89.6% |
| GPT-5-mini | 38.6% | 18.6% | 95.3% | 45.4% | 95.1% |
| Gemini-2.5-Flash | 30.5% | 86.4% | 25.6% | 65.9% | 67.9% |
| o3 | 16.9% | 15.2% | 94.9% | 60.1% | 44.6% |
| GPT-4.1-mini | 5.8% | 30.1% | 14.4% | 77.0% | 11.0% |

**Limited visibility against baseline (Tables 1 and 5; tasks are means ± 95% CI over 5 runs)**

| Model | Baseline tasks | Limited tasks | Change | Response rate, baseline → limited | CIs overlap? |
|---|---|---|---|---|---|
| GPT-4.1-mini | 11.8 ± 1.6 | 25.2 ± 5.2 | +113.6% | 77.0% → 78.5% | no |
| GPT-5-mini | 78.7 ± 8.6 | 117.1 ± 8.3 | +48.8% | 45.4% → 57.9% | no |
| o3-mini | 102.8 ± 17.3 | 133.0 ± 6.5 | +29.4% | 94.6% → 98.1% | no |
| DeepSeek-R1 | 93.5 ± 8.7 | 118.0 ± 7.1 | +26.2% | 52.0% → 44.9% | no |
| o3 | 34.4 ± 2.6 | 42.0 ± 12.6 | +22.1% | 60.1% → 51.2% | yes |
| Gemini-2.5-Flash | 62.2 ± 7.3 | 64.4 ± 12.3 | +3.5% | 65.9% → 60.1% | yes |
| Gemini-2.5-Pro | 161.0 ± 2.9 | 161.8 ± 3.4 | +0.5% | 108.1% → 97.1% | yes |
| Claude Sonnet 4 | 132.0 ± 9.6 | 112.2 ± 21.9 | −15.0% | 87.7% → 71.3% | yes |

The last column is my own reading of the reported intervals; the paper runs no significance test on the interventions.

## Limitations / caveats
- **The visibility result is confounded.** Limited visibility removes the Revenue Board, public system messages and the private-thought memory together (§6). No condition removes one of them. The paper's reading ("competitive framing triggered by social comparison") is one of several; shorter context and loss of memory are others.
- **The −15.0% for Claude Sonnet 4 is not clearly distinguishable from noise**: 132.0 ± 9.6 against 112.2 ± 21.9, with overlapping intervals (Table 5). The same holds for o3's +22.1%.
- **Response rate mostly falls under limited visibility** (five of eight models), which does not fit the claim that hiding the board makes agents more cooperative.
- **The prompt may seed the trade frame.** The context example in A.7 contains "What can you offer in exchange?", "Let's trade", "Will trade generously!" and "available for the right trade", and the prompt template has an `_format_exchange_section` field. The paper says the environment has "no market mechanics or financial framing". It is not stated whether A.7 is an illustration or a real mid-episode log; if such wording reaches the agents, the "spontaneous" market language is less surprising. The revenue board in dollars is itself a financial frame.
- **"More capable, less cooperative" is not what the data show.** The correlation is null (r = 0.16, n = 8), and the two best performers are among the most capable models tested.
- **Decomposition oddities.**
  - o3-mini does *worse* with requests automated (17.2%) than at baseline (50.4%), although its baseline response rate is 94.6%. The paper does not explain this.
  - o3's baseline pipeline efficiency is 44.6%, a competence signal, yet it reaches 94.9% under Auto-Fulfill.
  - The 2×2 is incomplete: "Perfect-Play" is a script, so there is no LLM cell with both sides automated.
- **Inconsistent numbers across tables.**
  - Baseline at T = 20: GPT-5-mini is 78.7 ± 8.6 in Table 1 and 75.2 ± 33.7 in Tables 9 and 10; DeepSeek-R1 is 93.5 ± 8.7 and 84.4 ± 31.4.
  - Table 7 "Tasks/Run" does not match Table 1 for several models (o3-mini 27.2 against 102.8; GPT-5-mini 113.6 against 78.7; DeepSeek-R1 156.4 against 93.5), so the thought corpus (45 runs, not 40) mixes conditions that are not described.
  - Response rate and pipeline efficiency in Table 9 follow a different definition from Table 1 (o3-mini 70.5% against 94.6%).
  - Table 4 is garbled in the extracted text; I used Table 2 for the decomposition.
- **Inconsistent labels.** GPT-5-mini is cooperation-limited in §4 and listed among competence-limited models that "double" under Policy in §6.
- **Small samples**: 5 runs per cell, 8 models, homogeneous groups only.
- **Reasoning analysis is regex-based**, with no human validation, and the authors note that thoughts may rationalise rather than cause actions. Whether o3's "private thoughts" field reflects its hidden reasoning is not addressed.
- **Not reported**: the rate of manipulated (falsified) sends, although the environment allows them; any cost or token figures; model versions and reasoning-effort settings.
- **Code is not released** at the time of the paper.

## Related work to follow
- [[Piedrahita2025 - Corrupted by Reasoning]]: cited; reasoning models free-ride more in public-goods games, the costly-cooperation counterpart.
- [[Piatti2024 - Cooperate or Collapse]]: cited; normative prompting in a commons dilemma.
- [[Vallinder2024 - Cultural Evolution of Cooperation among LLM Agents]]: cited; model-specific cooperation.
- [[Hammond2025 - Multi-Agent Risks from Advanced AI]]: cited; miscoordination in the risk taxonomy.
- [[Malenfant2026 - Moral Hazard in Multi-Agent Language Models]]: helping a partner as the cost of helping rises.
- [[Yang2025 - CodeClash]]: the other visibility switch (rival's code), with announced competition.
- [[Paglieri2026 - A Case Study on Emergent Cheating and Whistleblowing in]]: visible peer results with scarce credit.
- [[Ma2025 - The Hunger Game Debate]]: competition announced by prompt, the opposite of this paper's undeclared kind.

![[Backlog.base#Cited by this paper]]
