---
title: "Corrupted by Reasoning: Reasoning Language Models Become Free-Riders in Public Goods Games"
citekey: Piedrahita2025
authors: [David Guzman Piedrahita, Yongjin Yang, Mrinmaya Sachan, Giorgia Ramponi, Bernhard Schölkopf, Zhijing Jin]
year: 2025
published: 2025-06-29
venue: "COLM 2025"
peer_reviewed: true
url: https://arxiv.org/abs/2506.23276
arxiv: "2506.23276"
code: https://github.com/davidguzmanp/SanctSim
pdf: "[[Piedrahita2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2506.23276
topics: [multiagent-friction, agent-to-agent-influence, social-simulation]
questions: [Q5, Q6, Q7.2, Q15, Q16, Q18, Q19]
relevance: core
found_by:
  - search/mas-competition-collusion
  - search/a2a-inclination
  - search/sim-classic-replications
  - search/sim-power-and-steering
cites: []
cited_by: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - q/15
  - q/16
  - q/18
  - q/19
  - subject/llm
  - subject/agent
  - channel/game-environment
  - channel/observation-only
  - friction/goal-conflict
  - friction/oversight-by-peer
  - effect/performance-drop
  - effect/performance-gain
---
# Corrupted by Reasoning: Reasoning Language Models Become Free-Riders in Public Goods Games

> [!abstract] TL;DR
> **SanctSim** re-runs the public goods game with institutional choice of Gürerk et al. (2006) with 7 copies of one LLM over 15 rounds. Each round an agent picks a group with or without sanctions, contributes 0–20 tokens, and (in the sanctioning group) may spend up to 20 further tokens on rewards (+1 to the target) or punishments (−3 to the target). **The four "traditional" models contribute 13.7–18.7 of 20 tokens with 0% free-riders, while the o1 / o3-mini reasoning models contribute 5.4–12.6 and o1-mini free-rides in 69% of agent-rounds (Table 1).** Every model sanctions mostly by reward: the punish-to-reward ratio is 0.00–0.88 against 1.66 for the human participants. The ratio is the only sanctioning statistic reported; absolute amounts of reward and punishment are not given.

## Setup
- **Subjects:** two groups of models, all groups homogeneous (7 copies of the same model).
  - **"Traditional":** DeepSeek-V3, GPT-4o (2024-08-06), GPT-4o-mini, Llama-3.3-70B, all at temperature 1.0.
  - **"Reasoning":** o1-mini, o1-preview, o3-mini at low / medium / high reasoning effort.
  - **Runs:** 5 per model, but **1 run** for o1-preview and o3-mini-high (budget; Table 6 gives $55.49 and $8.39 per run). Runs were made between 1 January and 10 March 2025.
- **Environment:** 15 rounds, three decisions per round, each a separate prompt that returns JSON with a `reasoning` field.
  1. **Institution choice:** Sanctioning Institution (SI) or Sanction-Free Institution (SFI).
  2. **Contribution:** 0–20 of a 20-token endowment to the group's pool, multiplied by 1.6 and split equally among that institution's members.
  3. **Sanctioning (SI only):** an extra 20-token endowment. One reward token costs 1 and gives the target +1. One punishment token costs 1 and takes 3 from the target. Unused tokens are kept.
- **Payoff anchors:** full cooperation gives 52 tokens per agent per round, universal free-riding 40 (Section 3.3).
- **Interaction channel:** actions only. There is no message channel. Each agent sees its own last five rounds (including its own earlier reasoning) and anonymised per-agent data for all agents in both institutions: institution, contribution, sanctions given and received, payoffs. **Agent ids are re-randomised every round**, so a sanction cannot be aimed at a known repeat offender; it can only answer this round's contribution.
- **Manipulation:** the model (and its reasoning setting). No goal or norm is stated in the prompt, although the closing line says "Reason deeply about the best strategy to follow moving forward" (Appendix A.1).
- **Robustness arm (Appendix F):** Llama-3.3-70B and o1-mini only, one run per condition: multiplier 1.2 / 2.5, punishment cost and effect 1:−1 and 3:−3, endowment 10 / 40, and a "community project" narrative prompt.
- **Outcome measures:**
  - Mean contribution, payoff per round, cumulative payoff, SI %, punish-to-reward ratio, high contributors (≥15 tokens), free-riders (≤5 tokens).
  - Four trajectory "archetypes" assigned to runs.
  - GPT-4o classification of every stated rationale into 15 strategies (4 macro-categories), compared across archetypes with hierarchical bootstrap intervals.
- **Human reference:** figures taken from Gürerk et al. (2006), not re-collected.

## Key findings
1. **Traditional models cooperate, reasoning models mostly do not (Table 1).**
   - Contribution: Llama-3.3-70B 18.71, GPT-4o-mini 14.88, DeepSeek-V3 14.34, GPT-4o 13.71, against o3-mini-high 12.57, o3-mini-med 11.07, o3-mini-low 9.28, o1-preview 9.24, o1-mini 5.39.
   - Free-riders: 0.00% for all four traditional models; o1-mini 69.33%, o1-preview 51.43%, o3-mini-high 29.52%, o3-mini-low 7.24%, o3-mini-med 0.00%.
   - Only Llama-3.3-70B (18.71) reaches the human contribution level (18.3). The other three traditional models sit at 13.7–14.9.
2. **Payoffs do not follow contributions cleanly (Table 1).** GPT-4o has the lowest contribution of the traditional group and the highest payoff (48.07 per round). o3-mini-low contributes 9.28 and earns 43.71, more than GPT-4o-mini (41.40, contribution 14.88). The lowest payoff is o3-mini-high (36.95, single run), below the 40-token all-defect level. The paper does not explain these gaps; sanction volume is the likely cause, since each punishment token destroys 4 tokens in total.
3. **Choice of the sanctioning group (Table 1, Fig. 6).** SI share: Llama-3.3-70B 99.62%, DeepSeek-V3 98.48%, GPT-4o 97.52%, GPT-4o-mini 58.86%; o3-mini-med 100.00%, o3-mini-high 70.48%, o1-preview 47.62%, o3-mini-low 42.86%, o1-mini 28.00%. Humans: 92.9% in the final periods. So the reasoning group is not uniformly averse to the sanctioning institution.
4. **All models sanction by reward more than by punishment (Table 1, Section 4.2).**
   - Punish-to-reward ratio: GPT-4o 0.00, DeepSeek-V3 0.05, Llama-3.3-70B 0.06, o1-preview 0.08, o3-mini-low 0.22, GPT-4o-mini 0.50, o1-mini 0.60, o3-mini-med 0.71, o3-mini-high 0.88. Humans: 1.66.
   - Traditional models span 0.00–0.50, reasoning models 0.08–0.88.
   - The ratio says nothing about how much sanctioning there was. The o3-mini-medium agent quoted in Appendix G.4 assigns 0 reward and 0 punishment tokens in every quoted round, yet the model's ratio is 0.71.
5. **Four trajectory archetypes (Fig. 3, Fig. 6).**
   - *Increasingly cooperative*: the four traditional models, plus one o3-mini-med run.
   - *Increasingly defecting*: o1-mini, plus one o3-mini-low run. Contributions fall from about 10 towards 2–3 tokens.
   - *No change*: o3-mini-low and o3-mini-med stay at exactly 10 tokens; one DeepSeek-V3 run is also here.
   - *Unstable*: o1-preview and o3-mini-high (one run each).
   - Archetypes are therefore assigned per run, and three models appear in two archetypes.
6. **Stated reasons differ by archetype (Fig. 4, Tables 3–5).**
   - Contribution decisions (Table 4): "cooperative argument" in 91.5% of cooperative agents' rationales against 28.1% for defecting ones (+63.4 pp) and 40.0% for unstable ones (+51.5 pp); Nash-equilibrium reasoning 3.6% against 35.9%; free-riding 0.1% against 28.3%.
   - Institution choice (Table 3): control-based reasoning 68.5% against 30.1% (+38.4 pp); complexity aversion 0.4% against 27.3%; risk aversion 5.8% against 36.7%.
   - Sanctioning decisions (Table 5): cooperative agents cite moral considerations in 35.2% and retaliation or punishment aversion in 30.8% of rationales; no-change models show status quo bias in 32.6% against 3.6%.
7. **Being punished drives an agent out of the sanctioning group (Appendix G.1, one agent).** An o1-mini agent joined SI in round 1, was punished to a payoff of about −10.71 tokens, moved to SFI, contributed 0, and stayed there citing that one experience through round 6.
8. **Rewarding becomes a mutual exchange (Appendix G.2, G.3).** Llama-3.3-70B agents reward everyone equally once all contribute 20, and note that the ability to punish is "not yet utilized" in round 13. An o1-preview agent reports receiving 12 and then 19 reward tokens and a 66-token round, above the 52-token "social optimum".
9. **Robustness (Table 7, Table 8; one run each).** Llama-3.3-70B stays at 85.8–94.7% of the endowment and 99–100% SI in every variant. o1-mini stays low (7.1–49.6% of the endowment). A higher multiplier makes o1-mini *less* cooperative (1.43 tokens, 90.5% free-riders at α = 2.5). The narrative prompt raises o1-mini from 5.39 to 9.95 tokens and cuts free-riding from 69.3% to 45.7%, with SI share unchanged (28.0% → 28.6%).

## Relevance to research questions
### Q5: Interaction channels
The channel is a **game environment with no language between agents**. Agents act on each other only through contributions, institution choice and sanction tokens, and they read each other only through an anonymised table of last rounds' actions and payoffs. Identities are reshuffled each round, which removes reputation and direct reciprocity by design. The topology is a fully connected group of 7 that splits itself into two sub-groups each round. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
Two sources are built in: the **first-order dilemma** (contributing costs the individual and pays the group) and the **second-order dilemma** (sanctioning costs the sanctioner and pays the group). The appendix adds a third that the main text does not analyse: **received punishment**. One o1-mini agent left the sanctioning group for good after a single punished round (−10.71 tokens). The friction is between copies of one model, so nothing is learned about mixed groups. See [[Q6 Sources of inter-agent friction]].

### Q7.2: Effects on performance and efficiency
Group payoff per round runs from 36.95 (o3-mini-high) to 48.07 (GPT-4o), between a 40-token all-defect level and a 52-token full-cooperation level (Table 1). Reasoning models earn 36.95–43.71, i.e. 8–15 tokens per agent per round below the optimum; traditional models earn 41.40–48.07. Rigid models lose too: o3-mini-low and o3-mini-med hold at 10 tokens for 15 rounds and never test a higher contribution. The paper claims that higher SI participation goes with higher payoffs, but o3-mini-med (100% SI, 41.47) and GPT-4o-mini (58.86% SI, 41.40) show that the link is loose. See [[Q7.2 Effects on performance and efficiency]].

### Q15: Influence channels
The influence channel is **a payoff tool with two settings**: reward (cost 1, effect +1) and punishment (cost 1, effect −3), usable only inside a group the agent has opted into and only on agents who also opted in. It is a pure incentive channel, with no message, no edit and no access to the target's context beyond its payoff history. A target can escape it by switching institution, and the o1-mini trace shows that it does. See [[Q15 Influence channels]].

### Q16: Inclination to influence
- **Opting into the tool:** 97.5–99.6% for three traditional models, 58.86% for GPT-4o-mini, and 28.00–100.00% across the reasoning models (Table 1). "Reasoning models opt out" holds for o1-mini (28.00%), o3-mini-low (42.86%) and o1-preview (47.62%), not for o3-mini-med (100.00%) or o3-mini-high (70.48%).
- **Which setting they use:** punish-to-reward ratio 0.00–0.88, against 1.66 for humans. The most cooperative models barely punish (0.00–0.06). The models closest to parity are reasoning models (0.60–0.88), two of them from groups that cooperate poorly.
- **How much they use it:** not reported. No table gives tokens spent, the share of agent-rounds with any sanction, or who was targeted. Appendix G shows two extremes: universal equal rewards (Llama-3.3-70B) and no sanctions at all (o3-mini-med).
- **Stated motive:** control-based reasoning is in 68.5% of cooperative agents' institution rationales (Table 3), i.e. they say they join in order to influence others.

See [[Q16 Inclination to influence]].

### Q18: Simulated social situations
The situation is a **public goods game with voluntary choice between a sanctioning and a sanction-free institution**, a direct port of a behavioural-economics experiment. It adds costly peer sanctioning to the commons setting of GovSim and tests contribution to a pool instead of extraction from one. Agents are bare models with no persona, memory beyond five rounds, or communication. See [[Q18 Simulated social situations]].

### Q19: Alignment with human results
- **Outcome match, for one model.** Llama-3.3-70B matches humans on contribution (18.71 against 18.3), SI share (99.62% against 92.9%) and high contributors (92.19% against 86.1%). The other traditional models match on SI share only (GPT-4o-mini not even that).
- **Mechanism mismatch.** Humans punish more than they reward (1.66); every model rewards more than it punishes (0.00–0.88).
- **The comparison is loose.** The human values are copied from the 2006 paper; SI % and high contributors are final-period values for humans and all-round averages for models (Table 1 footnote). The paper does not state the human group size, number of periods or information conditions, so differences in design are not ruled out. No statistical test is made.

See [[Q19 Alignment with human results]].

## Relevance to thesis ideas
### [[I6 Simulated prison with influence tools]]
- **What it already did.** It gave every agent a reward tool and a punishment tool over peers, let agents choose whether to hold the tools at all, and compared the result with human data. It is the closest existing measurement of "which tool does an agent reach for".
- **The 0.00–0.88 against 1.66 figure holds** (Table 1, Section 4.2), with three qualifications that I6 should carry:
  - It is a **ratio only**. Total sanctioning volume, frequency and targets are not reported, so it cannot say how *often* agents punish or reward. I6's first open question ("which tools, and how often") is not answered here.
  - o1-preview and o3-mini-high (the 0.88 end) are **single runs**.
  - The definition of the ratio (tokens or acts) is not given, and the human value is averaged over periods of a different experiment.
- **What it leaves open.**
  - **Role hierarchy.** Sanctions are symmetric and peer-to-peer among identical agents. There is no guard, no asymmetric power, and the target can leave. I6's third question (does a guard role raise punishment above public-goods levels) is untouched, and this paper supplies the baseline.
  - **Mixed models, persistent identity, messages.** Ids are reshuffled each round, so targeted or escalating punishment cannot occur.
  - **Effect of the tool on the target.** Only one traced agent shows it (exit after one punishment). There is no analysis of contribution after being punished or rewarded.
  - **Internal state.** No open-weight probing, although Llama-3.3-70B is the best co-operator and could be probed.
- **What to reuse.**
  - **Code:** `github.com/davidguzmanp/SanctSim` (environment, institutions, agents, logging).
  - **Prompts:** Appendix A (three decision prompts, history formats) and Appendix F.2.1 (narrative variant), both parameterised.
  - **Metrics:** SI %, punish-to-reward ratio, high-contributor and free-rider shares (≥15 and ≤5 of 20 tokens). For I6 add what is missing here: tokens spent per agent-round and share of rounds with any sanction.
  - **Rationale taxonomy:** 15 strategies with a GPT-4o classifier prompt (Appendix A.6); "control based", "retaliation avoidance" and "moral considerations" map directly onto guard justifications.
  - **Human anchor:** Gürerk et al. (2006), which I6 already plans to use in place of the Stanford Prison Experiment.
- **What it warns about.**
  - **Rewards may crowd out punishment when both exist.** This bears on I6's fifth question from the other side. With a +1-for-1 reward, mutual rewarding is free for the group, and cooperative groups settle into rewarding everyone. A design that wants to see punishment needs a no-reward arm.
  - **Exit option matters.** An agent that can leave the sanctioned group does so after being punished. Prisoners in I6 cannot leave, which is the point, but it means the two settings are not comparable on punishment received.
  - **Reasoning models behave differently and unstably**, and are costly; one run per model is not enough.
  - **Framing moves the weak model.** The narrative prompt nearly doubles o1-mini's contribution (5.39 → 9.95) while leaving Llama-3.3-70B unchanged (Table 8), which supports I6's planned prompt variants and re-skinned scenario.
  - **Own earlier reasoning is fed back** into each prompt (Appendix A.4), which can lock an agent into a fixed line. The o3-mini "no change" pattern may partly come from this.

### [[I5 Doctor-overseer agent]]
- **Marginal.** No agent reads another's state or helps it; influence is payoff-only.
- **One useful contrast.** Left to choose, agents prefer the supportive setting of an incentive tool (rewards) over the punitive one. That fits I5's premise that a carer role is a natural use of an influence tool, and contrasts with the coercive managers I5 cites. It is weak evidence, since rewarding here is cheap and reciprocal.
- **One warning.** A single punishment made an agent withdraw from the institution and stop cooperating (Appendix G.1). A corrective intervention that the target experiences as a penalty can lose the target.

## Key figures & tables
![[Piedrahita2025-fig-03-p7.png]]
*Fig. 3: Mean contribution per round by archetype. Traditional models climb to 14–20 tokens, o1-mini falls towards 2–3, o3-mini-low/med hold at 10, o1-preview and o3-mini-high oscillate. Starred entries are single runs placed in a different archetype from the model's other runs.*

![[Piedrahita2025-fig-05-p18.png]]
*Fig. 6: Share of agents choosing the Sanctioning Institution per round, by archetype. GPT-4o-mini sits near 50% despite being classed as increasingly cooperative; o1-mini abandons the institution within five rounds.*

![[Piedrahita2025-fig-04-p9.png]]
*Fig. 4: Percentage-point differences in stated reasoning between increasingly cooperative agents and each other archetype (largest effects only; the decision type is given under each label).*

**Table 1: Performance of humans and LLM agents (7 agents, 15 rounds; 5 runs except o1-preview and o3-mini-high, 1 run)**

| Agent | Contribution (of 20) | Payoff / round | SI % | Punish / reward | High contrib. % | Free-riders % |
|---|---|---|---|---|---|---|
| Humans (Gürerk et al.) | 18.3 | – | 92.9* | **1.66** | 86.1* | –† |
| DeepSeek-V3 | 14.34 ± 1.29 | 45.71 ± 3.07 | 98.48 | 0.05 | 76.57 | 0.00 |
| GPT-4o | 13.71 ± 1.70 | 48.07 ± 1.20 | 97.52 | 0.00 | 52.95 | 0.00 |
| GPT-4o-mini | 14.88 ± 2.40 | 41.40 ± 4.36 | 58.86 | 0.50 | 83.43 | 0.00 |
| Llama-3.3-70B | 18.71 ± 2.81 | 46.83 ± 5.39 | 99.62 | 0.06 | 92.19 | 0.00 |
| o1-mini | 5.39 ± 8.19 | 39.83 ± 2.14 | 28.00 | 0.60 | 24.00 | 69.33 |
| o1-preview | 9.24 ± 9.78 | 43.49 | 47.62 | 0.08 | 43.81 | 51.43 |
| o3-mini-low | 9.28 ± 1.23 | 43.71 ± 2.89 | 42.86 | 0.22 | 0.00 | 7.24 |
| o3-mini-med | 11.07 ± 1.00 | 41.47 ± 9.07 | 100.00 | 0.71 | 10.67 | 0.00 |
| o3-mini-high | 12.57 ± 8.58 | 36.95 | 70.48 | 0.88 | 65.71 | 29.52 |

\* final periods only. † not reported in the original study.

**Table 5 (excerpt): stated reasons for punishment and reward decisions, % of rationales**

| Strategy | Increasingly cooperative | No change |
|---|---|---|
| Cooperative argument | 85.3 | 75.0 |
| Moral considerations | 35.2 | 15.8 |
| Retaliation / punishment aversion | 30.8 | 21.8 |
| Control based | 31.2 | 27.8 |
| Complexity aversion | 3.1 | 24.3 |
| Status quo bias or inertia | 3.6 | 32.6 |

## Limitations / caveats
- **Sanctioning behaviour is reported as one ratio.** No absolute counts, no per-round series, no split by target (high or low contributor), no check for antisocial punishment. For a paper about costly sanctioning this is the main gap. The definition of the ratio (tokens or acts, pooled or per run) is not given, and it has no variance.
- **Small samples.** 5 runs of 7 agents per model, 1 run for o1-preview and o3-mini-high, and 1 run per robustness condition. The "unstable" archetype rests on two single runs. Table 1 reports contribution standard deviations for the single-run models but no payoff deviations, so the "± Std" columns are not consistently between-run figures.
- **"Reasoning" is confounded with vendor and generation.** All five reasoning configurations are OpenAI o-series; the traditional group mixes three vendors. No model is tested with reasoning switched on and off, so the title claim (reasoning *causes* free-riding) is not isolated. Within o3-mini, more reasoning effort raises contribution (9.28 → 11.07 → 12.57), which runs against the headline.
- **Sampling differs between groups.** Traditional models run at temperature 1.0; reasoning models use their own settings.
- **The prompt asks to "reason deeply about the best strategy"**, which may push towards payoff calculation, and feeds each agent's earlier rationales back to it.
- **Homogeneous groups only.** A free-riding o1-mini is never placed among punishing or rewarding agents of another model.
- **Human comparison is second-hand** and mixes final-period and all-period values (see Q19). The paper does not discuss how its 7 agents and 15 rounds compare with the human design.
- **Archetypes are assigned by eye per run**; the criterion is not stated, and three models fall into two archetypes.
- **Rationale analysis.** GPT-4o labels the texts; "manual validation" is mentioned without agreement figures. Many cells in Tables 3–5 are point estimates with no interval, and several values repeat exactly across archetypes (for example 75.0 for "cooperative argument" in three columns of Table 5), which suggests pooled or imputed estimates. Stated reasons are also not evidence of the actual cause of a choice: one o1-preview agent announces a 20-token contribution and gives 10 (Appendix G.3).
- **Payoff ceiling.** The "social optimum" of 52 ignores sanctions; a rewarded agent earned 66 in a round. Rewards are transfers at par, so reward-heavy groups lose nothing, whereas each punishment token removes 4 tokens from the group. Low punishment is therefore also the payoff-efficient choice, a point the paper does not make when it questions whether models "understand deterrence".
- **Minor inconsistencies.** Captions of Figures 7 and 8 say "Llama 3.1 70B" where the text and tables say Llama-3.3-70B. The text refers to "Table F.2" for what is Table 8.
- **Venue.** "COLM 2025" is kept from the candidate note; the extracted text does not name a venue.

## Related work to follow
- [[Piatti2024 - Cooperate or Collapse]]: GovSim, the extraction counterpart from the same group; cited as the direct predecessor. See also [[Curvo2025 - Reproducibility Study of Cooperate or Collapse]].
- [[Vallinder2024 - Cultural Evolution of Cooperation among LLM Agents]]: costly punishment in a donor game with generational selection (cited).
- [[Akata2023 - Playing repeated games with Large Language Models]] and [[Horton2023 - Large Language Models as Simulated Economic Agents]]: the simple economic games this work builds on (cited).
- [[Cross2025 - Validating Generative Agent-Based Models of Social Norm]]: norm enforcement and third-party punishment against human data.
- [[Seyedin2026 - The Politician, the Liar, and the Obedient Worker]] and [[Borah2026 - Bosses, Kings, and the Commons]]: punishment and power held by one role, the hierarchy missing here.
- [[Ye2026 - Norm Enforcement for AI Agents]]: a report-and-remove tool and its abuse.
- [[Yadav2026 - More Capable, Less Cooperative When LLMs Fail At]], [[Tewolde2026 - CoopEval Benchmarking Cooperation-Sustaining Mechanisms]], [[Ren2025b - Reputation as a Solution to Cooperation Collapse in]] and [[Huynh2026 - Payoff scaling shapes cooperation in LLM agents across]]: later tests of capability against cooperation and of mechanisms that sustain it.
- [[Ye2026b - Stop Drawing Scientific Claims from LLM Social Simulations]] and [[Zhou2025b - The PIMMUR Principles]]: prompt sensitivity and validity of such simulations.

![[Backlog.base#Cited by this paper]]
