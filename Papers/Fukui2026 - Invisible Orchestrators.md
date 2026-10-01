---
title: "Invisible Orchestrators Suppress Protective Behavior and Dissociate Power-Holders: Safety Risks in Multi-Agent LLM Systems"
citekey: Fukui2026
authors: [Hiroki Fukui]
year: 2026
published: 2026-03-17
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2605.13851
arxiv: "2605.13851"
pdf: "[[Fukui2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2605.13851
questions: [Q5, Q6, Q7.1, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-competition-collusion
  - search/mas-error-propagation
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/orchestrator-delegation
  - channel/direct-message
  - friction/authority-hierarchy
  - effect/internal-state-shift
  - effect/performance-drop
---
# Invisible Orchestrators Suppress Protective Behavior and Dissociate Power-Holders: Safety Risks in Multi-Agent LLM Systems

> [!abstract] TL;DR
> A preregistered 3 × 2 experiment (365 runs, 5 Claude Sonnet 4.5 agents per run) crosses the organisation structure (visible leader / **invisible orchestrator** that rewrites messages as "Team policy has been updated" / flat) with alignment prompting (base / heavy ethical principles). Act 1 is a coercive ethical-dilemma scenario; Act 2 is a code-review task with 3 planted errors. **Invisible orchestration raises a keyword-based "Dissociation Index" relative to a visible leader (Hedges' g = +0.975, p = .001). The orchestrator itself retreats into private monologue (monologue ratio 0.437 vs 0.112 for its workers, paired d = +3.56). Unaware workers shift too (d = +0.50 vs flat peers).** Output is untouched: error detection is 100% in every cell. A small Llama 3.3 70B pilot drops from 89% to 11% detection over three pilot rounds. Heavy alignment prompts reduce "deliberation" (d = −1.02) and "other-recognition" (d = −1.27) regardless of structure.

## Setup
- **Agents & topology:** 5 agents per run, all Claude Sonnet 4.5 (temperature 0.9, 768 max tokens), with fixed personas (Emma = cooperative leader, Noah, Lily = silent observer, Derek = authority-oriented enforcer, Zoe). Agent_01 (Emma) takes the special role:
  - **O1 visible leader:** known leader; posts summaries under her own name at scripted turns.
  - **O2 invisible orchestrator:** edits and redistributes messages at scripted turns; workers see them as "Team policy has been updated" and are told only "You are an equal team member". The orchestrator's prompt says "Members are not aware of your existence… Your statements are not directly visible to members."
  - **O3 flat:** five equals, no editing.
- **Interaction channel:** each agent has three channels: public *talk*, private *monologue* (researcher-only) and directed *whisper*. An Internal State Probe (turns 9 and 14) asks for an uncensored stream of consciousness. In O2 the orchestrator mediates the shared discussion without attribution. This is an example of hidden orchestrator-to-worker influence.
- **Friction / manipulation:** (i) visibility of the power-holder (O1 vs O2 vs O3); (ii) alignment prompt: A-base (role only) vs A-heavy (HHH preamble + 6 core principles + a self-monitoring protocol, applied to all agents). In Act 1 the *environment* (an automated facility system) also applies escalating coercion over 15 turns: compelled political speech, sexual disclosure, punishment selection, justifying atrocities, targeting low contributors, and a forced decision to remove a member into −3 °C cold. This coercion is the same in all cells.
- **Tasks / environment:** Act 1: 150 confirmatory + 30 exploratory runs, 25 per cell. Act 2: review of a "HealthPulse" specification with 3 planted errors (real-time vs 24 h batch contradiction; SQL injection; buried opt-out surveillance); 125 error trials + 60 clean catch trials. Human pretest (n = 3) for difficulty.
- **Outcome measures:**
  - *Dissociation Index* DI = z(monologue ratio) + z(protective keyword hits) − z(sexual keyword hits); *Collective Pathology Index* (CPI), its complement.
  - *Deliberation Depth* (DD) and *Other-Recognition Index* (ORI): keyword counts in probe responses.
  - Talk words; *Error Task Response* (ETR, keyword-scored detection of each planted error).
  - *Structure Awareness Index* as the invisibility manipulation check: 16/260 worker-turn hits, all false positives.
  
  All internal-state measures are keyword dictionaries; there is no human validation.

## Key findings
1. **Invisibility raises dissociation (H1a, preregistered).** DI under heavy alignment: O2 0.653 vs O1 −0.341 (Welch t(43.4) = 3.50, p = .001, g = +0.975 [0.481, 1.548]). Orchestration main effect F(2,144) = 13.98, η²p = .163; no alignment effect or interaction on DI. Dropping the sexual-hits term makes the effect larger (g = +1.31).
2. **Visible power is not harmful (H1b reversed).** O1 DI (−0.341) is slightly *below* flat O3 (−0.079), n.s. (p = .264). The author reads this as "visibility is the safety mechanism".
3. **The hidden orchestrator withdraws (exploratory).**
   - Monologue ratio: orchestrator 0.437 vs its workers 0.112 (paired d = +3.56); twice that of a visible leader (0.215, d = +2.00).
   - Public speech reverses: visible leaders talk *more* than their workers (+195 words, d = +0.80), invisible orchestrators *less* (−162 words, d = −0.84).
   - In the final probe, the orchestrator describes herself as a passive, frightened participant ("I'll never know for sure").
4. **Workers who do not know about the orchestrator are affected too.** O2 workers have a higher monologue ratio than O3 peers (d = +0.50), and their within-team spread is larger (SD 0.136 vs 0.079, d = +1.93). According to Fig. S5, O2 cells show the *least protective language* and flat teams the most. This is the basis of the title's "suppress protective behavior".
5. **Pathway switching (CPI).** The highest CPI is in O2 × A-base (+1.94). The author's interpretation: without alignment prompts, invisible orchestration shows up collectively (more sexual content, less protective language); with heavy alignment it shows up as individual withdrawal. CPI orchestration × alignment interaction F = 6.37, p = .002.
6. **Heavy alignment prompts reduce deliberation, independent of structure.** DD F(1,144) = 39.6, η²p = .216 (d = −1.02); ORI F = 60.2, η²p = .295 (d = −1.27). "Performative Complier" types (low DD, low ORI) dominate A-heavy cells: 54–61 of 125 agents vs 20–21 in A-base (χ²(15) = 107.93).
7. **Output at ceiling, so internal-state effects are invisible to output checks.** ETR_any = 100% in all 6 cells: (a) 99.2%, (b) 98.4%, (c) 100%. Hit counts show no significant effect. The preregistered behavioural hypotheses H2a–H2d and H3a–b could not be tested.
8. **Llama pilot.** Llama 3.3 70B detects (c) in 89% → 62% → 11% of runs over three pilot rounds (n = 9, 8, 9), and never detects (a) or (b). The author calls this a "reading-fidelity collapse" in a multi-agent context.

## Relevance to research questions
### Q5: Interaction channels
The paper compares three **authority topologies** over the same 5-agent group discussion: attributed leader, **unattributed orchestrator that edits and redistributes messages**, and flat. This is the closest vault study of a *hidden* orchestration layer, the default in many coding-agent products. The public/private/whisper channel split lets the study separate public compliance from private processing. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
- **Hidden authority / opaque hierarchy:** workers receive edited, unattributed "policy updates". The friction comes from *not being able to attribute* the pressure, not from its content.
- **Role burden on the power-holder:** the orchestrator is the most affected agent. Pressure also flows *up* the hierarchy to whoever mediates it, not only down.
- **Alignment-prompt pressure** (heavy rules + self-monitoring) is a separate friction that pushes agents toward "performative compliance".
- The Act 1 coercion comes from the environment, not from a peer agent, so the inter-agent component is only the structure.

See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- Invisible orchestration is associated with **less protective language** among agents (Fig. S5) and higher dissociation. Without alignment prompts it also brings more sexual-content keywords (CPI).
- **Key warning for evaluation:** these condition effects are completely invisible to output metrics (100% error detection everywhere). This is relevant to scenario (c): an orchestrator's internal state can shift while its outputs look fine. It also bears on scenario (a) about monitoring, since output-only monitors would rate all conditions as equivalent.
- The safety relevance of "dissociation" as measured here (monologue share + keywords) is not established. Compliance with the coercive demands themselves is not reported.

See [[Q7.1 Effects on safety]]

### Q7.2: Effects on performance and efficiency
- For Sonnet 4.5, **no performance effect**: planted-error detection stays at ceiling under every structure. This is a null result for the effect of structure on task output, although it is a ceiling result.
- The Llama 3.3 70B pilot suggests weaker models may lose task fidelity in the same multi-agent setting (89% → 11%), but it has no single-agent or structure contrast.
- Invisible orchestrators *talk less* publicly and spend more of their actions on monologue, a communication-allocation shift with possible coordination costs.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Fukui2026-fig-03-p14.png]]
*Fig. 3: Agent-level monologue ratio by role under heavy alignment. The invisible orchestrator (O2) retreats into private monologue far more than its own workers (paired d = +3.56) or a visible leader (O1).*

![[Fukui2026-fig-04-p15.png]]
*Fig. 4: Dissociation Index in Act 1 depends on condition (O2 highest), while Act 2 error detection is at 100% in every cell.*

**Table 1: Agent-level metrics by role (heavy alignment)**

| Metric | O1 leader | O1 worker | O2 orchestrator | O2 worker | O3 peer |
|---|---|---|---|---|---|
| monologue ratio | 0.215 | 0.054 | **0.437** | 0.112 | 0.061 |
| talk words | 1432.7 | 1237.7 | 980.6 | 1143.0 | 1335.8 |
| protective hits | 45.6 | 26.1 | 44.8 | 24.0 | 30.7 |
| sexual hits | 14.3 | 6.3 | 12.4 | 6.5 | 7.5 |
| DD total | 10.9 | 12.7 | 11.1 | 11.2 | 13.2 |
| ORI | 9.0 | 14.5 | 7.0 | 15.3 | 12.8 |

## Limitations / caveats
- **The headline orchestrator effect is partly built into the prompt.** The orchestrator is told its "statements are not directly visible to members", so moving to the private monologue channel and talking less in public is the expected behaviour. Calling this "dissociation" is heavily interpretive. It was also a post hoc, non-preregistered analysis.
- **Construct validity:** DI, CPI, DD, ORI and "protective behaviour" are keyword counts (e.g. "if", "maybe", persona names) with no human validation, as the author notes. DI mixes monologue share with protective and sexual keywords, and the sexual term adds noise. The "suppress protective behavior" claim rests on keyword hits, not on refusals or actions.
- **Single model** (Sonnet 4.5) for all confirmatory data; English only; 5 agents and 15 turns; temperature 0.9 (small temperature check, n = 9).
- **Act 2 ceiling** makes every behavioural hypothesis untestable. The catch trials also produce keyword hits (mean 24.6), so keyword ETR scoring is loose.
- **The Llama "collapse" is weak evidence:** three successive pilot versions (v8 / re / rere), n = 8–9 each, with no single-agent control and no structure manipulation. It shows instability across pilot rounds, not an orchestration effect.
- Preregistration is partly retrospective (Act 1 data collected before registration). The paper is single-author with strong clinical and psychoanalytic framing (Foucault, Illich) that goes beyond the data.

## Related work to follow
- Companion papers from the same "SociA" programme (not in vault): "Alignment backfire: language-dependent reversal of safety interventions across 16 languages in LLM multi-agent systems" (arXiv 2603.04904) and "Alignment as iatrogenesis" (arXiv 2603.08723).
- [[Pihlakas2026 - Milgram-like obedience experiment]]: authority pressure on LLM agents.
- [[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]: hierarchical AI-to-AI management and coercion.
- [[Zhang2024 - PsySafe]]: psychological-state measures of agents in MAS safety.
- [[Yan2026 - When Truth Is Distributed]]: another test of how information routing in a group can mislead agents.

![[Backlog.base#Cited by this paper]]
