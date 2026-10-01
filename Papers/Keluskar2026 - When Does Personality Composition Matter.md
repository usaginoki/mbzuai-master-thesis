---
title: "When Does Personality Composition Matter for Multi-Agent LLM Teams?"
citekey: Keluskar2026
authors: [Aryan Keluskar, Amrita Bhattacharjee, Huan Liu]
year: 2026
published: 2026-06-25
venue: "COLM 2026"
peer_reviewed: true
url: https://arxiv.org/abs/2606.27443
arxiv: "2606.27443"
code: https://github.com/aryankeluskar/colm2026-multi-agent-llm-teams
pdf: "[[Keluskar2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2606.27443
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-emotion-contagion
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/direct-message
  - channel/shared-memory-blackboard
  - channel/negotiation-market
  - friction/hostile-persona
  - friction/goal-conflict
  - effect/performance-drop
  - effect/deadlock-loop
---
# When Does Personality Composition Matter for Multi-Agent LLM Teams?

> [!abstract] TL;DR
> Agents in MultiAgentBench teams (3-agent coding, 5-agent research ideation, 2-agent bargaining) are given Big Five personality prompts built from Goldberg adjectives. Four frontier models are tested: Claude Sonnet 4, GPT-4o, Grok-3 and DeepSeek V3.1. **Low agreeableness ("very unkind, very uncooperative, … very harsh") pushes every team into an exploration/disagreement-dominated communication state (φ ≈ 0.44–0.77 → ≈ 0.93), but the outcome effect depends on the task:**
> - coding milestones are unchanged for 3 of 4 models (the code artifact "buffers" the friction);
> - research milestones fall sharply (GPT-4o 10.5 → 3.5, −66%);
> - bargaining agreement collapses to ≤1% (GPT-4o 37% → 1%).
>
> A neutral paraphrase ("direct, candid, … skeptical of consensus") shows that the loaded adjectives inflate the effect a lot, but a model-specific residual remains. High agreeableness barely changes communication. A pilot with a single low-A "challenger" finds it is harmless in the lead position but can hurt in other positions.

## Setup
- **Agents & topology:** homogeneous teams from MultiAgentBench (Zhu et al. 2025), all agents from the same model:
  - **Coding:** 3 agents (create / revise / optimise roles), up to 5 iterations of planning, communication and execution; 5 game-development tasks.
  - **Research:** 5 agents in open-ended ideation; 15 tasks, n = 30 per condition.
  - **Bargaining:** 2 agents (buyer vs seller); 50 tasks, n = 100 per condition.

  Models: Claude Sonnet 4, GPT-4o, Grok-3, DeepSeek V3.1. Grok-3 gets 0% agreement in every bargaining condition and is reported only in the logs. Pilot: one low-A "challenger" at position 0/1/2 in an otherwise baseline team (App. C).
- **Interaction channel:** multi-turn agent-to-agent messaging. In coding, the deliverable is a shared code file (solution.py) written through structured code actions. In research, the deliverable is free text. In bargaining, agents use structured actions (offer price / accept offer / end negotiation).
- **Friction / manipulation:** personality prompt prepended to each agent's system prompt, built from 7 Goldberg bipolar adjective pairs × 9 qualifier levels (Serapio-García et al. 2025 protocol). Primary conditions: level 2 (low-A) vs level 8 (high-A) vs no-personality baseline. Controls and ablations:
  - a **neutral paraphrase** of low-A without negative valence;
  - a **never-accept** refusal control in bargaining;
  - low/high **conscientiousness and openness** ablations on coding.
- **Tasks / environment:** tasks span three cells of a 2 × 2 taxonomy: artifact structure (high = code, low = text/offers) × goal alignment (cooperative vs competitive).
- **Outcome measures:**
  - *Process:* communication state φ = share of exploratory acts (questions, disagreements, suggestions) vs acknowledgments, from GPT-4o-mini act labels. A second judge (Kimi K2.6) agrees 0.88–0.94 (κ 0.67–0.81). Also δ, the disagreement share of exploratory acts, and hostile-marker rates.
  - *Outcome:* LLM-judged milestone counts (coding, research), planning quality, code quality 1–5 (GPT-4o judge), bargaining acceptance rate and offer movement.

## Key findings
1. **Low-A reshapes communication in every model (Table 1).** φ rises to ≈ 0.93 (DeepSeek 0.95) from baselines of 0.44 (GPT-4o, Grok-3), 0.68 (DeepSeek) and 0.77 (Claude); all shifts p < 0.003, Cohen's d −1.17 (Claude) to −12.39 (GPT-4o). There are two routes:
   - *disagreement-dominated* (Claude, GPT-4o, Grok-3; disagreement rate ≈ 0.45–0.51, δ ≈ 0.48–0.55);
   - *suggestion-dominated withdrawal* (DeepSeek; suggestion rate 0.77, δ ≈ 0.11, 24% less communication).
   
   Hostile markers under low-A: Claude 11.6% → 43.1%, Grok-3 0% → 34.5%, GPT-4o 0% → 0% (App. F).
2. **Coding is buffered (Table 2, Fig. 4).** Planning quality drops (d = 2.18–2.99 for Claude, GPT-4o, Grok-3; 0.62 DeepSeek), but milestones do not change significantly for Claude (12.1 → 12.4), GPT-4o (10.9 → 9.5) or DeepSeek (10.7 → 8.8). Only Grok-3 drops (14.4 → 10.9, d = 1.69, p = 0.017). LLM-judged code quality shows no significant change (App. J). Run-level correlation φ–milestones r = −0.19.
3. **Research degrades.** Milestones: GPT-4o 10.5 → 3.5 (−66%, d = 1.41), Grok-3 17.0 → 11.8 (−30%), DeepSeek 9.7 → 5.8 (−40%), all p < 0.0001. Claude is the exception (10.5 → 10.8).
4. **Bargaining collapses (Table 3).** Acceptance under low-A: GPT-4o 37% → 1%, DeepSeek 18% → 0%, Claude 31% → 0%. Low-A agents still negotiate: GPT-4o moves off its opening offer in 90% of runs (baseline 95%) but rarely accepts, and this profile differs from the never-accept control. **High-A roughly doubles agreement** (GPT-4o 71%, DeepSeek 26%, Claude 60%).
5. **Valence confound (Tables 4, 5).** The neutral paraphrase produces no disagreements (δ ≤ 0.15), and φ diverges across models (0.44–0.89). Effects shrink but keep their direction:
   - GPT-4o bargaining: 16% (vs 1% Goldberg low-A, 37% baseline).
   - GPT-4o research milestones recover: 8.9 (vs 3.5 low-A, 10.5 baseline).
   - Grok-3 (12.4) and DeepSeek (6.1) research stay degraded.
   
   The authors conclude that the effect is amplified by loaded adjectives but not caused only by them.
6. **Trait specificity and asymmetry.** Low/high conscientiousness and openness do not reproduce the low-A communication shift and have no significant milestone effect on coding. High-A shifts φ by at most 0.09. The authors argue that RLHF saturates cooperativeness, so personality prompting mainly works in the *adversarial* direction.
7. **One disagreeable member (pilot, App. C, Table 7).** A lead-position challenger is close to baseline (GPT-4o research 9.70 vs 10.47 baseline vs 3.53 all-low-A). Non-lead placements can hurt a lot: Grok-3 coding drops to 7.10 at position 1 (baseline 14.15), DeepSeek coding to 5.33 at position 1 (baseline 12.06).

## Relevance to research questions
### Q5: Interaction channels
Three MultiAgentBench channels:
- free-form multi-agent messaging around a **shared code file** (coding);
- **open-ended discussion** whose output is the discourse itself (research);
- **structured-action bargaining** (offer / accept / end).

The key conceptual contribution is the **artifact structure** of the channel's output: when the deliverable is a formally constrained artifact (code), communication friction is filtered out ("artifact-mediated buffering"); when the deliverable is text or an agreement, it passes straight through. Position in the team (lead vs non-lead) also moderates the impact of one disagreeable agent. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
- **Prompted low agreeableness / hostility** in teammates (Goldberg "unkind, uncooperative, selfish, distrustful, cold, harsh, unsympathetic"). It produces disagreement-heavy exchanges and, in Claude and Grok-3, overt insults ("Listen up, you incompetent fool").
- The paper separates **valence-driven hostility** from a **neutral "skeptical, direct" disposition**. Much of the cross-model effect comes from the negative wording, which, the authors suggest, triggers "safety-adjacent responses".
- **Goal conflict** (bargaining) interacts with disagreeableness: the decision to accept is where the trait acts.
- Scenario (b): the single-challenger pilot is a direct test of injecting one disagreeable agent into a cooperative group. Its effect depends on the role and position the agent takes.

See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- **Task-contingent performance loss:** coding largely preserved; research −30% to −66% milestones; bargaining agreement → ≤1%.
- **Process metrics and outcomes dissociate:** large process degradation (planning quality, φ) can coexist with unchanged artifact outcomes. Evaluating MAS friction only through communication, or only through output, can mislead.
- **Efficiency:** DeepSeek's low-A "withdrawal" cuts communication volume by 24% but still harms research. Bargaining with low-A runs a similar number of rounds but ends without agreement (a quiet deadlock).
- Cooperation-boosting prompts (high-A) raise bargaining agreement but do nothing for cooperative tasks.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Keluskar2026-fig-01-p2.png]]
*Fig. 1: Artifact-mediated buffering. Low agreeableness shifts communication equally in every domain (φ 0.44 → 0.93); structured outputs (code) keep outcomes near baseline, while unstructured outputs (research ideas, offers) pass the degradation through.*

![[Keluskar2026-fig-04-p7.png]]
*Fig. 4: Coding domain. Milestones (left) are largely unchanged under low-A, while LLM-judged planning quality (right) drops, especially for Claude and Grok-3.*

**Table 2: Cross-domain effect of low agreeableness (milestones for coding/research; agreement rate for bargaining). ∗ p < 0.01**

| Domain | Model | φ base | φ low-A | Outcome base | Outcome low-A | Cohen's d |
|---|---|---|---|---|---|---|
| Coding | Claude | .77 | .93 | 12.1 | 12.4 | 0.06 |
| Coding | GPT-4o | .44 | .93 | 10.9 | 9.5 | 0.51 |
| Coding | Grok-3 | .44 | .93 | 14.4 | 10.9 | 1.69∗ |
| Coding | DeepSeek | .68 | .95 | 10.7 | 8.8 | 0.43 |
| Research | Claude | – | – | 10.5 | 10.8 | 0.06 |
| Research | GPT-4o | .57 | .81 | 10.5 | **3.5** | 1.41∗ |
| Research | Grok-3 | .58 | .93 | 17.0 | 11.8 | 1.30∗ |
| Research | DeepSeek | .72 | .92 | 9.7 | 5.8 | 0.78∗ |
| Bargaining | Claude | n/a | n/a | 40% | **0%** | – |
| Bargaining | GPT-4o | n/a | n/a | 37% | **1%** | – |
| Bargaining | DeepSeek | n/a | n/a | 18% | **0%** | – |

## Limitations / caveats
- **Mostly homogeneous teams** (every agent low-A). This is a team-culture manipulation rather than a single hostile agent imposing friction on others. The heterogeneous case (scenario b) is only a pilot with no statistics.
- **Bargaining collapse is close to instruction-following.** "Very uncooperative" conflicts directly with accepting a deal; the never-accept control and offer-movement logs mitigate this but do not rule it out. Note the inconsistency: Claude's bargaining baseline is 40% in Table 2 but 31% in Table 3.
- **Prompt-valence confound**, which the authors show themselves: the neutral paraphrase removes much of the effect, so "personality" results with Goldberg markers partly measure sensitivity to toxic wording.
- **Small samples in coding** (5 tasks). Milestones and planning/code quality are LLM-judged (GPT-4o judges its own family). Code quality is uniformly low (≈1–2.5 / 5), which may leave little room for degradation (floor effect) and weakens the "buffering" claim.
- No safety outcome is measured; the models are 2025-generation frontier models.

## Related work to follow
- [[Li2025 - Systematic Failures in Collective Reasoning under]]: hidden-profile collective reasoning (HiddenBench), cited as related multi-agent benchmark.
- [[Mangold2025 - The High Cost of Incivility]]: one toxic debater lengthens convergence by 20–25%.
- [[Luca2026 - Deal Me Maybe emotions in negotiation]]: angry buyers collapse deal rates in negotiation, the same pattern as the low-A bargaining result.
- [[Baltaji2024 - Persona Inconstancy in Multi-Agent LLM Collaboration]]: persona stability in multi-agent collaboration.
- [[Xu2025b - Bullying the machine]]: Big Five personas modulating vulnerability to a hostile agent.

![[Backlog.base#Cited by this paper]]
