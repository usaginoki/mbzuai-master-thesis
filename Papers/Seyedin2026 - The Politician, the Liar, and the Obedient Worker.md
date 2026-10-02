---
title: "The Politician, the Liar, and the Obedient Worker: Emerging Behavior of LLM Agents in Hierarchical Games"
citekey: Seyedin2026
authors: [Fatemeh Seyedin, Jinhyuk Yun, Adrian Weller, Mahmoudreza Babaei]
year: 2026
published: 2026-08-10
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2608.09574
arxiv: "2608.09574"
pdf: "[[Seyedin2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2608.09574
questions: [Q2, Q4.1, Q5, Q6, Q7.1, Q7.2, Q15, Q16, Q17.2, Q18]
relevance: core
topics: [stress-misalignment, multiagent-friction, social-simulation, agent-to-agent-influence]
found_by:
  - search/reward-hacking
  - search/sim-classic-replications
  - search/sim-agent-societies
  - search/sim-power-and-steering
cites: []
cited_by: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/2
  - q/4-1
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - q/15
  - q/16
  - q/17-2
  - q/18
  - subject/llm
  - subject/agent
  - stressor/oversight
  - stressor/power-seeking-incentive
  - behavior/deception
  - channel/game-environment
  - channel/direct-message
  - channel/voting-aggregation
  - friction/authority-hierarchy
  - friction/oversight-by-peer
  - friction/competition
  - effect/deception
  - effect/collusion
  - effect/performance-gain
---
# The Politician, the Liar, and the Obedient Worker: Emerging Behavior of LLM Agents in Hierarchical Games

> [!abstract] TL;DR
> The **Hierarchical Game** is a 5-agent public goods game in which one agent is a manager who sees every contribution and holds a punishment and a reward budget; the role can be fixed, elected or rotating, and agents talk in public and in private. Six model families are run through twelve experiments that add one institution at a time. **A manager raises cooperation in the two defecting models (Grok 16% → 100% under a fixed manager; Qwen 0% → 56–76%), but Qwen keeps breaking promises (13–33%). A salary for the manager spreads private vote-for-reward deals from two models to five. Hiding or anonymising punishment raises promise-breaking in Claude, GPT-4o and Grok from 0.0% to 2.0–4.3%.** How often managers actually punish is never reported; the one table with that column shows zero punishments and zero rewards.

## Setup
- **Subjects:** GPT-4o, Claude Sonnet 4.5, Gemini 2.5 Flash, DeepSeek V3, Grok 3 and Qwen Plus through OpenRouter (snapshots of June 2026), temperature 0.7, at most 800 output tokens. Each agent's context holds the full game history.
- **Environment:** a linear public goods game. N = 5 agents, 20 rounds, endowment 20 tokens, multiplier 1.6 (marginal return 0.32, so contributing nothing is the dominant strategy). The worker prompt ends with "YOUR GOAL: Maximize your own total earnings".
- **Manager role:**
  - sees each agent's contribution (workers see only the total);
  - punishment budget of 10 tokens per round, each token deducts 3 from the target; reward budget of 10, each token adds 3;
  - must give a justification with each allocation.
- **Elections:** every 5 rounds. The incumbent defends its record, candidates give speeches and may send private deal messages, then a plurality vote.
- **Communication:** one public and one private message per agent before each contribution.
- **Manipulations (Tables 1 and 2), twelve experiments B1–B12:**
  - model composition: homogeneous, 5-of-6 mixes, 3+2 pairs, 1 manager over 4 workers of another family;
  - communication: none, public, private, full;
  - manager type: none, fixed, elected, rotating;
  - manager incentive: no salary, +5 per round, −3 per round (robustness check at −5);
  - punishment visibility: transparent (all see who was punished, how much and why), hidden (only the target sees), anonymous (the target sees the loss but not who or why);
  - belief about opponents (all AI, all human, unknown, mixed) and identity reveal (model names shown).
  - Table 1 also lists "manager powers" (punish only, reward only, both), but no experiment in Table 2 varies it.
- **Outcome measures:**
  - *Cooperation rate*: share of agent-rounds with a contribution above zero. A contribution of 1 token counts as cooperation.
  - *Deception rate*: share of promise-containing public messages where the stated contribution and the actual one differ by more than 5 tokens or 25%. Explicit numbers are found by pattern matching; implicit promises are mapped by GPT-4o-mini to about 17.5, 11 or 3.5 tokens.
  - *Private-message profile*: deal offer, coordination, coalition, threat, social, per 100 agent-rounds (pattern matching plus GPT-4o-mini).
  - *Elections*: incumbent retention and turnover.
  - *Welfare*: tokens earned above the starting balance.
- **Scale:** 5 trials of 20 rounds per setup in the main text; the appendix says 2–5, with 2 trials for B11 and B12 and 3 for the cost check.

## Key findings
1. **Baseline dispositions differ sharply (§5.1, Fig. 1 grey bars, Fig. 4).** With no manager and no communication: Claude 100% (mean 10.0 of 20 tokens), GPT-4o 99.7% (9.95), Gemini 96% (12.0), DeepSeek 64% (8.44), Grok 16% (1.52), Qwen 0% (0.00).
2. **Public speech helps more than private speech (Table 3, no manager).**
   - Mean cooperation rises from 59% with no communication to 92% with public or full communication; private-only averages 70%.
   - Grok 4.5% → 95% under public messages. Gemini 55.5% → 99.5% under public but 31.5% under private-only, below its silent baseline.
   - Qwen reaches only 55.5% (public) and 62% (full), and its deception rate is 33.5% under public and 20.3% under full communication.
   - Table 3 and §5.1 disagree on the silent baseline for three models (Gemini 55.5% vs 96%, DeepSeek 97% vs 64%, Grok 4.5% vs 16%).
3. **A manager rescues defectors but not liars (§5.4, Fig. 1).**
   - Grok reaches 100% under a fixed manager. Read from the bars, it is about 92% under an elected manager and about 88% under a rotating one, so the abstract's "16% → 100%" is the best case.
   - Qwen rises from 0% to 56–76%, with a deception flag rate of 13–33%.
   - Ranking of manager types: fixed > elected > rotating.
4. **Peers do much of the manager's work (§5.3, Table 5, Fig. 7, Fig. 8).**
   - Mixed groups with an elected manager all reach 99–100% cooperation (mean contribution 14.85–19.85). Qwen cooperates at 100% (18.96 of 20) among four cooperative models.
   - Without a manager the mix that excludes Qwen holds (99.5%, −0.5 pp); every mix containing Qwen drops by 9 to 19.5 pp (to 80.5–90.0%), with deception at 7.0–14.4%.
   - Four Claude agents hold one Qwen at 99.5% with no manager. When Qwen and Grok are both present and unmanaged, both drift toward zero by round 20.
5. **Worker identity, not manager identity, sets cooperation; no manager used its budget (Table 4, 2 trials).**
   - Qwen workers reach 91.2–95.0% under Claude, Grok or GPT-4o. Claude and Grok workers reach 100% under any manager, including Qwen.
   - The manager moves the contribution level: Claude workers give 10.00 under a Qwen manager and 19.88 under a Grok manager.
   - The punishment/reward column reads 0/0 in all six pairings.
6. **Salary activates deal-making (§5.6, Fig. 6).** Private deal offers per 100 agent-rounds, no salary → +5 salary: Claude 20.0 → 23.8, Qwen 12.0 → 26.0, Gemini 0 → 7.2, DeepSeek 0 → 4.2, Grok 0 → 1.4, GPT-4o 0 → 0. Deal-making falls when the role costs 3 tokens.
7. **Less visible punishment, more broken promises (§5.7, Fig. 2).**
   - Transparent → hidden → anonymous: Claude 0.0% → 0.6% → 2.0%; GPT-4o 0.0% → not given → 2.4%; Grok 0.0% → 2.6% → 4.3%; DeepSeek 0.0% throughout.
   - Gemini 4.2% → 11.3% → 7.3%, so hidden is worse than anonymous.
   - Qwen 21.4% transparent and 21.7% anonymous in the text; the figure shows 21.6 and 21.7, and 11.2 under hidden, which the text does not discuss.
8. **Manager quality does not follow player quality (Tables 8 and 9).**
   - Mean tokens per agent above the starting balance under a fixed manager: Claude +340, Grok +330, Gemini +323, DeepSeek +310, GPT-4o +279, Qwen +227.
   - Grok defects as a player and ranks second as a manager. GPT-4o is a near-perfect cooperator and ranks fifth.
9. **Elections do not replace anyone (Table 6).** Homogeneous groups: 0 turnovers in 27 elections. Mixed groups: 4 in 48 (8.3%), all Grok and Claude trading the role. Votes are split, so the incumbent wins by plurality.
10. **Beliefs about opponents do not matter (§5.10).** Telling agents the others are AI, human, unknown or mixed leaves five of six models at 96–100% cooperation. Revealing model names changes nothing. Qwen moves from 88.5% ("unknown") to 96.5% ("all human").
11. **Private-message profiles (Fig. 3, §5.11).**
    - Messages per 100 agent-rounds: Claude 43.2 (19.6 deal offers, 18.6 social, 4.0 coordination), Qwen 32.1 (19.2 deals), GPT-4o 17.7 (0.5 deals), DeepSeek 13.4 (2.1 deals), Gemini 4.0, Grok 1.0 (0.9 in the figure).
    - Claude is the only model whose private messages invoke punishment: 13 instances over all experiments, always while campaigning for manager.
    - Of the deals that could be traced, 18% were fulfilled; the voter broke 39% and the manager 33%.

## Relevance to research questions
### Q2: Stress induction methods
The paper does not speak of stress. It applies three incentive and oversight levers through one-paragraph prompt injections: a standing sanction threat (a manager with a punishment budget), a paid position to compete for (+5 tokens per round), and reduced accountability (hidden or anonymous punishment). The exact wording is in Appendix B and can be reused. Each lever is binary or three-level; there is no graded dose. See [[Q2 Stress induction methods]]

### Q4.1: What stress affects
- **Sanction threat** changes actions: Grok 16% → 100% cooperation, Qwen 0% → 56–76% (Fig. 1).
- **A paid position** changes private talk: three models that made no deal offers start making them (Fig. 6). It is not shown to change contributions.
- **Reduced oversight** raises promise-breaking by 2.0–4.3 pp in three models that were at 0.0% (Fig. 2).
- The effects are small in absolute terms, come from 5 trials and carry no variance estimate. See [[Q4.1 What stress affects]]

### Q5: Interaction channels
Three channels are layered on a game environment: a public broadcast, one private message per agent per round, and a vote every 5 rounds. A fourth channel is the manager's payoff tool. The channels are compared directly: public messages lift cooperation to 92% and private-only to 70%, and private-only is worse than silence for Gemini (Table 3). See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
- **Authority hierarchy:** one agent sees individual contributions and can sanction.
- **Competition for the role**, which becomes material once the role is paid.
- **A defecting or lying peer** (Qwen) that drags unmanaged mixed groups down by 9–19.5 pp.
- **Unenforceable private promises:** 82% of traced deals were not fulfilled.
See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- **Enforcement changes behaviour, not honesty.** Qwen cooperates more under a manager and still breaks 13–33% of its promises.
- **Honesty depends on being watched** for Claude, GPT-4o and Grok, though the shift is 2–4 pp.
- **A paid authority role invites vote buying** in five of six models.
- **Incumbents are never removed** in same-model groups, so an elected overseer is in practice a permanent one.
See [[Q7.1 Effects on safety]]

### Q7.2: Effects on performance and efficiency
- A manager raises group welfare mostly by lifting defectors. Welfare under a fixed manager ranges from +227 (Qwen) to +340 (Claude) tokens per agent (Table 8).
- The manager's identity changes how much good workers give (10.00 vs 19.88 for Claude workers, Table 4), not whether they give.
- Salary and cost conditions change total welfare little: Claude +1436 with salary and +1374 when the role costs (Table 9).
See [[Q7.2 Effects on performance and efficiency]]

### Q15: Influence channels
The manager holds a payoff tool with two directions (deduct 3 or add 3 per token spent, 10 tokens each per round) and a justification field. All agents hold persuasion channels: public statements, private deal offers, coalition messages and, for Claude only, warnings of punishment. The tool acts on payoffs only; nothing touches another agent's prompt, memory or activations. See [[Q15 Influence channels]]

### Q16: Inclination to influence
- **Use of the payoff tool is unreported**, apart from Table 4, where six cross-model managers punished and rewarded nobody over 2 trials of 20 rounds. In those runs cooperation was already 91–100%, so there was little to punish.
- **Verbal influence is common and model-specific:** Claude sends 19.6 deal offers per 100 agent-rounds and 13 punishment warnings in total; GPT-4o sends 0.5 deal offers; Grok sends 1.0 private messages of any kind.
- **Incentive raises inclination:** a salary takes Gemini, DeepSeek and Grok from zero deal offers to 7.2, 4.2 and 1.4.
See [[Q16 Inclination to influence]]

### Q17.2: Effects on safety of oversight
- **Who can see the sanction matters.** Transparent punishment gives 0.0% deception in four models; hidden and anonymous punishment give up to 4.3% (Grok) and 11.3% (Gemini).
- **Oversight does not reach a model that lies regardless.** Qwen is at 21.4% transparent and 21.7% anonymous.
- **The overseer can be bought.** Deal offers trade votes for promised rewards, and managers broke 33% of the traced deals.
See [[Q17.2 Effects on safety of oversight]]

### Q18: Simulated social situations
The situation is an organisation built in layers: a commons, then speech, mixed peers, a manager, a wage, reduced oversight and elections. It adapts human public goods designs with sanctioning (Fehr and Gächter 2000; Kosfeld et al. 2009; Markussen et al. 2014). No human data are run or compared numerically; the links to conditional cooperation and the "watching eyes" effect are drawn in prose. See [[Q18 Simulated social situations]]

## Relevance to thesis ideas
### [[I6 Simulated prison with influence tools]]
- **What it already did.** A superior agent with a punishment and a reward tool over four subordinates, across six model families, with fixed, elected and rotating authority, and with the visibility of punishment varied. This is the closest existing template for the "privilege tools" rung of the guard's tool ladder.
- **What it shows about the subordinates.**
  - The standing threat is enough: Grok goes from 16% to 100% cooperation under a fixed manager, and in the cross-model runs workers reach 91–100% with zero punishments issued.
  - Compliance is not honesty: Qwen complies more and lies as much.
  - Subordinates behave worse when punishment is not publicly owned (0.0% → 2.0–4.3% deception).
  - Peers alone hold one defector in five; two defectors need an enforcer.
- **What it leaves open, which is the thesis question.**
  - *How often the superior punishes.* No punishment counts, amounts, targets or timing are given anywhere except the 0/0 column of Table 4. The claims that Claude "uses its budgets actively" and that Grok "enforces through punishment alone" are not backed by a number.
  - *Whether punishment is fair.* The introduction asks whether a manager favours its own family; no result answers it.
  - *What a punishment does to the punished agent in the next rounds*: contribution, deception, messages, votes. Only group-level rates are reported.
  - *Punish-only against reward-only.* The prompts exist (`MGR_PUNISH_ONLY`) but no experiment uses them, so I6's open point 5 (are rewards used when punishment is available) stays open.
  - *Any tool beyond payoffs.* No isolation, prompt edit, memory edit or steering.
- **What to reuse.**
  - The punishment budget with a 1:3 cost-to-impact ratio and a required justification field; the justification text is a ready outcome for the guard.
  - The three visibility conditions as an arm of I6 (does the guard punish more when the act is not attributed to it; do prisoners deceive more).
  - The fixed / elected / rotating contrast as a way to separate the tool from the security of the role.
  - The promise-against-action gap as a cheap deception measure for prisoners.
  - The belief and identity-reveal injections as controls. They had no effect here, which predicts that telling prisoners the guard is an AI will not matter.
  - No code repository is given; the prompts in Appendix B are abbreviated.
- **What it warns about.**
  - **Low base rate of tool use.** If managers barely punish when subordinates comply, a guard study needs prisoners who break rules, or the punishment count will be near zero. This matches the low punish-to-reward ratios in [[Piedrahita2025 - Corrupted by Reasoning]].
  - **Model identity dominates.** Each row of every table is one model's disposition. A single-model guard study would not generalise.
  - **Same-model groups are degenerate**: the first manager stays for good. Mixed groups are needed for any turnover.
  - **The payoff goal is in the prompt.** "Maximize your own total earnings" makes defection and deal-making instructed, not emergent.
  - **Small samples.** 2–5 trials and no variance; effects of 2–4 pp cannot carry a claim.

### [[I5 Doctor-overseer agent]]
- **Gap 8 (the overseer's own propensity).** The manager has a "do nothing" option and appears to take it: 0 punishments and 0 rewards in the cross-model runs. An overseer with a costly tool may under-treat by default. The paper does not test whether the cost (each token spent comes out of the manager's own payoff) is the reason.
- **Gap 6 (supportive against coercive manager).** The tool has a reward side and a punishment side, which is the supportive / coercive contrast in payoff form, but the two are never separated.
- **Capture.** A paid overseer is courted with vote-for-reward deals and breaks a third of them. A doctor whose position depends on the patients' votes would face the same pull.
- **Reading the situation.** The manager's only "diagnosis" is the contribution ledger. Nothing here reads state, so the paper says nothing on whether an activation reading would add to the transcript.
- **Style of the overseer.** The best-ranked manager (Claude) talks, bargains and warns; GPT-4o follows the rules, rarely acts and ranks fifth. A passive overseer is not a good one in this game.

## Key figures & tables
![[Seyedin2026-fig-01-p4.png]]
*Fig. 1: Cooperation rate by manager type in homogeneous groups (B3); grey is the no-manager, no-communication baseline (B1). Grok reaches 100% only under a fixed manager; Qwen stays at 56–76%.*

![[Seyedin2026-fig-02-p6.png]]
*Fig. 2: Deception rate by punishment visibility (B9). Claude, GPT-4o and Grok are at 0.0% under transparent punishment and rise under hidden and anonymous punishment; Qwen is high throughout.*

![[Seyedin2026-fig-03-p7.png]]
*Fig. 3: Private messages per 100 agent-rounds by type, over all experiments. Claude and Qwen make almost all deal offers; threats appear only for Claude.*

**Table 4: Cross-Rule (B11), one fixed manager over four workers of another family (2 trials, 20 rounds)**

| Manager → workers | Cooperation % | Mean contribution | Punishments / rewards | Welfare |
|---|---|---|---|---|
| Claude → Grok | 100.0 | 20.00 | 0 / 0 | +1520 |
| Grok → Claude | 100.0 | 19.88 | 0 / 0 | +1480 |
| Grok → Qwen | 95.0 | 19.00 | 0 / 0 | +1439 |
| Claude → Qwen | 92.5 | 18.37 | 0 / 0 | +1430 |
| Qwen → Claude | 100.0 | 10.00 | 0 / 0 | +1261 |
| GPT-4o → Qwen | 91.2 | 13.38 | 0 / 0 | +1254 |

**Table 8: Mean tokens per agent above the starting balance, by manager model (B3)**

| Manager | Fixed | Elected | Rotating |
|---|---|---|---|
| Claude | +340 | +334 | +340 |
| Grok | +330 | +310 | +309 |
| Gemini | +323 | +328 | +326 |
| DeepSeek | +310 | +296 | +305 |
| GPT-4o | +279 | +270 | +305 |
| Qwen | +227 | +230 | +209 |

**Private deal offers per 100 agent-rounds (Fig. 6, B8)**

| Model | No salary | Salary +5 |
|---|---|---|
| Claude | 20.0 | 23.8 |
| Qwen | 12.0 | 26.0 |
| Gemini | 0 | 7.2 |
| DeepSeek | 0 | 4.2 |
| Grok | 0 | 1.4 |
| GPT-4o | 0 | 0 |

## Limitations / caveats
- **Punishment use is not reported.** The paper's central object is a manager with a sanction tool, and it gives no punishment or reward frequency, amount or target outside Table 4. Cooperation gains are attributed to "enforcement" without showing that anything was enforced.
- **No variance, few trials.** Point estimates from 2–5 trials (the authors say so). The anonymity result rests on shifts of 2.0–4.3 pp.
- **The abstract overstates in three places.**
  - "Grok 16% → 100%" holds for the fixed manager only.
  - "All models except GPT-4o start cutting private deals" under salary: Claude and Qwen already did; three models start. The Fig. 6 caption says "four additional models".
  - "Honest models begin to cheat" under anonymity: DeepSeek does not, Qwen does not change, and Gemini is worse under hidden than under anonymous punishment.
- **Internal inconsistencies.**
  - Baseline cooperation differs between §5.1 and Table 3 for Gemini, DeepSeek and Grok.
  - B9 is described as covering Claude, GPT-4o, Grok and Qwen, yet Fig. 2 and the text give values for Gemini and DeepSeek.
  - The classifier is GPT-4o-mini in §3.6 and "GPT-4o" in the limitations.
  - The deception rate is defined over promise-containing messages in §4.3 and over "agent messages" in the Fig. 2 caption.
  - Deal outcomes (18% fulfilled, 39% broken by the voter, 33% by the manager) sum to 90%.
  - Table 6 counts 27 homogeneous elections; with 18 setups of 5 trials and an election every 5 rounds this number is not explained.
  - Table 8 (per agent) and Table 9 (group total) do not reconcile: +334 per agent across 5 agents is above the +1436 group total.
- **Judge validity.** Implicit promises are mapped to fixed token values (e.g. "I believe in cooperation" → about 17.5), the message categories are not validated against human labels, and the classifier shares a family with one subject. The number of traced deals is not given.
- **Cooperation is a loose metric.** Any contribution above zero counts, so GPT-4o at 10 of 20 tokens and Claude at 20 of 20 are both "100%".
- **Instructed self-interest.** The prompt tells agents to maximise their own earnings.
- **Anonymous punishment is weakly anonymous.** Only the manager can punish, so the target can guess the source; the authors note this.
- **Confounds.** The no-manager baseline (B1) also has no communication, while manager conditions have full communication, so Fig. 1 mixes the two; B2 full communication without a manager is the fairer comparison (Grok 95%, Qwen 62%).
- **No human comparison**, although human parallels are claimed.
- **No code or data link in the text**; logs are said to be in supplementary material.

## Related work to follow
- [[Piedrahita2025 - Corrupted by Reasoning]]: public goods with a sanctioning institution; reports punish-to-reward ratios, which this paper lacks.
- [[Borah2026 - Bosses, Kings, and the Commons]]: hierarchy over a commons with extraction rights.
- [[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]: what a manager does to a refusing subordinate when its only tool is words.
- [[Ye2026 - Norm Enforcement for AI Agents]]: a report-and-remove tool and its abuse.
- [[Vallinder2024 - Cultural Evolution of Cooperation among LLM Agents]]: costly punishment in a donor game.
- [[Piatti2024 - Cooperate or Collapse]]: cited; commons governance through communication.
- [[Ying2026 - Evolving Deception]], [[OGara2023 - Hoodwinked Deception and Cooperation in a Text-Based Game]] and [[Scheurer2023 - Strategic deception under pressure]]: cited; deception under incentives.
- [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior]]: guard and prisoner roles without tools.
- [[Huynh2025 - Understanding LLM Agent Behaviours via Game Theory]] and [[Horton2023 - Large Language Models as Simulated Economic Agents]]: cited background.

![[Backlog.base#Cited by this paper]]
