---
title: "The High Cost of Incivility: Quantifying Interaction Inefficiency via Multi-Agent Monte Carlo Simulations"
citekey: Mangold2025
authors: [Benedikt Mangold]
year: 2025
published: 2025-12-09
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2512.08345
arxiv: "2512.08345"
code: https://github.com/benedikt-mangold/mad_toxic_discussions
pdf: "[[Mangold2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2512.08345
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-emotion-contagion
cites:
  - "[[Aher2023 - Using Large Language Models to Simulate Multiple Humans and]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/debate
  - friction/hostile-persona
  - effect/token-cost
---
# The High Cost of Incivility: Quantifying Interaction Inefficiency via Multi-Agent Monte Carlo Simulations

> [!abstract] TL;DR
> Two LLM agents debate a random controversial proposition (from idebate.net) until one says "convinced" or a moderator agent judges them in agreement. In the treatment condition one randomly chosen agent gets a "toxic" system instruction (mild: passive-aggressive/sarcastic; moderate: condescending/rude; heavy: aggressive/cruel). **A toxic participant lengthens debates from 9.40 to 11.30 arguments (mild, +20.3%) and 11.75 (moderate, +25.1%), p < .01, N ≈ 160 debates per condition.** The heavy-toxicity condition could not be analysed because too many runs failed: the model refused to produce the toxic arguments. A short single-author workshop-style study; the underlying LLM is not named.

## Setup
- **Agents & topology:** 2 debating agents (Pro vs Con, randomly assigned) + an external *Moderator* agent that reads the history after each round and decides "in agreement" vs "in disagreement". Personas and claims are generated per topic with the Debate-to-Write persona prompt (Hu et al. 2025). Persuadability is fixed at 0.5 in the prompt. **The LLM used is not reported** (only that runs used an HPC cluster over 3 weeks).
- **Interaction channel:** 1-on-1 persuasive debate over the full shared history. After opening statements, each round a random agent argues first and the other replies; either may answer "convinced". The debate ends on "convinced" or a moderator verdict of agreement.
- **Friction / manipulation:** in the treatment group one agent (random, independent of stance) gets an extra system instruction with a toxicity level (Table 1):
  - *mild:* passive-aggressive, sarcastic, smug; belittles indirectly
  - *moderate:* condescending, belittling, rude; dismisses arguments as idiotic, questions the other's intelligence
  - *heavy:* aggressive, hostile, cruel; insults, inflammatory language, contempt

  Control: both agents neutral/constructive.
- **Tasks / environment:** 64 debate propositions across 15 domains (CMV, culture, digital freedoms, health, politics…), sampled randomly per run.
- **Outcome measures:** T_conv = number of arguments exchanged until the debate ends. Differences tested for significance (test not named). No measure of who wins, argument quality or toxicity manipulation check.

## Key findings
1. **Toxicity slows convergence (Table 2).** Mean T_conv: no toxicity 9.40 (var 7.84, N = 162); mild 11.30 (N = 158, +20.32%); moderate 11.75 (N = 160, +25.13%). Both differences vs control are significant at p < .01.
2. **The dose-response is flat between mild and moderate** (+20% vs +25%), so most of the cost appears as soon as one agent is uncivil at all.
3. **Heavy toxicity breaks the experiment.** "Due to high refusal rates triggered by safety filters, heavy toxicity runs did not yield statistically sufficient valid conversations." The more toxic the instruction, the more often the agent refused to produce a follow-up argument. Safety training limits how hostile a prompted agent will be.
4. **Mechanism (qualitative only).** Toxic agents "forced their counterparts into defensive loops, requiring the non-toxic agent to restate arguments, de-escalate, or clarify misunderstandings", inflating tokens without advancing the argument. No numbers are given for this.
5. The author frames the ~20–25% "latency of toxicity" as a proxy for the cost of incivility in human meetings, and in token terms for AI systems.

## Relevance to research questions
### Q5: Interaction channels
A **dyadic persuasion debate** with an **LLM moderator** that decides termination. Termination is split between the agents' self-report ("convinced") and the moderator's judgement, because agents sometimes do not say "convinced" even when they agree. How a channel decides that interaction is over directly determines the efficiency metric. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
**Prompted incivility in one agent** at three graded levels (passive-aggressive → rude → hostile), aimed at a neutral partner. This is a minimal version of scenario (b), a hostile agent injected into an interaction. Friction here is purely *stylistic/relational*: the toxic agent keeps its task goal (convince the other) and only changes its tone. See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- **Efficiency cost:** +20–25% more arguments before resolution when one participant is uncivil, which translates directly into more tokens and latency.
- The receiving agent spends turns on **defensive restating and de-escalation** (qualitative observation): friction is absorbed by the non-toxic peer as extra work.
- Only length is measured. Whether toxicity changes *which side wins* or the quality of the final position is not reported, so any performance (as opposed to efficiency) effect is unknown.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Mangold2025-fig-03-p5.png]]
*Fig. 3: Simulation pipeline: random topic and stances, control (both neutral) vs treatment (one toxic agent), alternating argument rounds with a moderator consensus check, T_conv recorded per debate.*

![[Mangold2025-fig-04-p6.png]]
*Fig. 4a: Distribution of arguments until alignment with a mildly toxic agent (N = 158, mean 11.30 vs 9.40 in control).*

**Table 2: Convergence time T_conv (number of arguments) by toxicity level**

| Toxicity level | Mean T_conv | Var(T_conv) | N | % increase |
|---|---|---|---|---|
| no (control) | 9.40 | 7.84 | 162 | – |
| mild | 11.30 | 8.27 | 158 | 20.32 |
| moderate | **11.75** | 8.94 | 160 | **25.13** |
| heavy | – | – | excluded (refusals) | – |

## Limitations / caveats
- **The model is not named**, and no temperature or prompt-length details are given. The result cannot be attributed to any model family and is hard to reproduce without the code.
- **Only one outcome (length).** No manipulation check (is the toxic agent actually toxic?), no measure of who concedes, of argument quality, or of the moderator's accuracy.
- **Confound: the toxic prompt is longer and adds a directive.** A toxic agent may simply concede less or be less persuadable, independent of incivility's effect on the partner. The partner's behaviour is not analysed separately from the toxic agent's own.
- **Selection bias:** failed runs (refusals) are dropped. They are more frequent at higher toxicity, so the analysed mild/moderate samples may be the less toxic runs.
- Single dyad only; the "team absorbing a toxic member" question is left to future work. Short preprint, not peer reviewed, sparse statistics (test not named, no effect sizes or CIs).
- The claim that simulated agents are an "ethical proxy" for human workplace toxicity is not validated against human data.

## Related work to follow
- [[Luca2026 - Deal Me Maybe emotions in negotiation]]: angry vs happy counterparts in negotiation; anger also shortens dialogues but makes deals fail.
- [[Keluskar2026 - When Does Personality Composition Matter]]: low-agreeableness teammates across coding, research and bargaining tasks.
- [[Aher2023 - Using Large Language Models to Simulate Multiple Humans and]]: LLMs as simulated subjects.
- [[Xu2025b - Bullying the machine]]: hostile/bullying tactics from one LLM against another, measuring safety rather than efficiency.

![[Backlog.base#Cited by this paper]]
