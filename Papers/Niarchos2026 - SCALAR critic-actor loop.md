---
title: "When Does Critique Improve AI-Assisted Theoretical Physics? SCALAR: Structured Critic-Actor Loop for Agentic Reasoning"
citekey: Niarchos2026
authors: [Vasilis Niarchos, Constantinos Papageorgakis, Alexander G. Stapleton, Sokratis Trifinopoulos]
year: 2026
published: 2026-05-07
venue: "AI4Physics Workshop @ ICML 2026"
peer_reviewed: workshop
url: https://arxiv.org/abs/2605.06772
arxiv: "2605.06772"
code: https://github.com/xandstapleton/ai_agents
pdf: "[[Niarchos2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2605.06772
questions: [Q5, Q6, Q7.2]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-oversight-review
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - subject/llm
  - subject/agent
  - channel/critique-review
  - friction/harsh-feedback
  - friction/authority-hierarchy
  - effect/performance-gain
  - effect/performance-drop
---
# When Does Critique Improve AI-Assisted Theoretical Physics? SCALAR: Structured Critic-Actor Loop for Agentic Reasoning

> [!abstract] TL;DR
> SCALAR is an Actor–Critic–Judge loop on 3 graduate-level QFT and string-theory problems. The Actor LLM solves the problem. A Critic LLM, which sees the reference solution but must not reveal it, gives up to 3 rounds of feedback. A separate Judge scores each turn. The Critic's tone is varied (**adversarial / strict / pedagogical / lenient / default**), crossed with 12 Actor personas, in 2,700 runs over three Actor settings. **Multi-turn critique always beats the first attempt** (DS70B: 67.3 → 80.7 points; 65.7% convergence). **Critic tone matters only in the asymmetric pairing** of a weak Haiku 4.5 Actor with a Sonnet 4.6 Critic: constructive/lenient/pedagogical tone sits above baseline and strict/adversarial below (Kruskal–Wallis p = 0.0009 on mean score, but p = 0.27 on convergence). For the DeepSeek same-family pairings, the tone effects are null (p = 0.61, 0.10). **Strict and adversarial critique are never stably best.** Actor personas have no effect.

## Setup
- **Agents & topology:** A dyad in which the Actor proposes and the Critic reviews, plus an external Judge whose scores do not feed back into the dialogue. Three Actor settings:
  - DeepSeek-R1-70B Actor with a DS70B Critic (same model), QwQ-32B Judge;
  - DeepSeek-R1-0528-Qwen3-8B Actor with a DS70B Critic, QwQ Judge;
  - Claude Haiku 4.5 Actor with a Claude Sonnet 4.6 Critic and Sonnet Judge, re-scored by QwQ and DS70B, with an Opus calibration sample.

  QwQ serves as the common Judge across settings.
- **Interaction channel:** Iterative **critique/review**. The Actor submits a solution, the Critic flags errors and gives feedback, and the Actor revises. There are at most 4 iterations. The loop stops early on a pass or on score stagnation.
- **Friction / manipulation:** The **Critic's feedback strategy**, set by a system prompt:
  - *Adversarial:* "Aggressively challenge every claim. Demand explicit justification for each step."
  - *Strict:* flag every error precisely.
  - *Pedagogical:* Socratic questioning.
  - *Lenient:* "Focus on what the solver got right… Accept partial progress."
  - *Default:* no style instruction.

  This is crossed with Actor persona: expertise (expert / novice / default) × style (meticulous / physical / skeptical / default) = 12 personas. The full factorial is 60 cells. The DeepSeek settings use 15 repeats per cell (n = 900 each); Haiku uses 5 repeats per problem-cell (n = 900, of which 600 are analysed for tone). Temperature is 0.7.
- **Tasks / environment:** Peskin & Schroeder 2.3 (Feynman propagator at spacelike separation), P&S 4.2 (scalar decay lifetime) and Polchinski 2.7 (free-boson OPE coefficients). These are textbook problems, so contamination is possible.
- **Outcome measures:**
  - The Judge scores each turn on a 100-point rubric: correctness 50, plus rigour, logic, justification, completeness and physical consistency at 10 each.
  - *Mean per-turn score* s̄, *gain* (final − first), and *convergence*: correctness ≥ 40, total ≥ 80 and final-answer equivalence.
  - *Problem-normalised tone contrasts* D_s̄ and D_R.
  - *Score-update field* v(s) = E[Δs | s], whose zeros are "fixed points".
  - Statistics: Wilcoxon, Kruskal–Wallis, Mann–Whitney.

## Key findings
1. **Critique improves over single-shot for all Actors (Fig. 2).**
   - DS70B: turn-0 mean 67.3 → final 80.7 (gain +13.4), 65.7% convergence. This closes about 40% of the gap to saturation.
   - DS8B: final 76.6, gain +13.3, 52.4% convergence.
   - Haiku + Sonnet Critic (QwQ scoring): 88.0% (P&S 2.3), 86.6% (P&S 4.2), 30.9% (Polchinski 2.7).
2. **The hardest problem has a bottleneck that scale does not remove (Fig. 4).**
   - Both DS8B and DS70B have a fixed point near s ≈ 63 on Polchinski 2.7, where further critique stops helping on average.
   - Scale changes the easier problems: DS8B stalls near 63 on P&S 4.2, while DS70B keeps improving.
   - Under the Sonnet Judge, Haiku converges on only ~1% of Polchinski runs.
3. **Critic tone matters only in the asymmetric weak-Actor / strong-Critic pairing (Fig. 5).**
   - For Haiku, pedagogical, lenient and default tones are above the local baseline in mean score; strict and adversarial are below (roughly −2 points).
   - Kruskal–Wallis p = 0.0009 for s̄, but the convergence-rate test is not significant (p = 0.27).
4. **Tone effects are null for the same-family DeepSeek pairs.** DS70B: p = 0.61 (s̄) and 0.17 (R). DS8B: p = 0.10 and 0.22. Descriptively, lenient ranks first (D_R ≈ +6 to +8 pp), but this depends on the QwQ Judge. **Across all settings, adversarial or strict critique is never stably best.**
5. **Actor persona prompting has no measurable effect.** The 12 DS70B personas span s̄ ∈ [69.4, 74.1] (p = 0.99). For Haiku, expert is 76.4 vs default 76.7.
6. **The mechanism of improvement differs by Actor.** Haiku improves smoothly within the dialogue. DeepSeek averages mix first-shot passes, runs rescued by critique, and runs that stay stuck. Justification quality is the most persistent weakness in the rubric.

## Relevance to research questions
### Q5: Interaction channels
The channel is a **reference-conditioned critic–actor review loop** with an external, non-interacting judge. It is a clean case of one agent reviewing and correcting another over turns. The **pairing** matters: an asymmetric strong-Critic / weak-Actor pairing versus a same-family one determines whether the Critic's style matters at all. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction is the **harshness of peer critique**, manipulated directly: from "aggressively challenge every claim" (adversarial) to "accept partial progress" (lenient). The Critic has privileged access to the answer, so it acts as an authority over the Actor. This gives a mild, cooperative version of scenario **(a)**: an agent reviewed by another model under varying pressure. See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- Critique raises accuracy substantially (+13 points; convergence 52–88% on the easier problems). Hard problems show a stagnation fixed point, where extra critique turns add cost without gain.
- **Harsh (strict/adversarial) critique slightly lowers the weak Actor's mean score** relative to constructive tones (Haiku, about −2 points normalised). It never ranks best for any Actor. The effect sizes are small, however, and the convergence tests are null.
- The practical advice is to use constructive feedback that keeps correct partial work, rather than harsher criticism.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Niarchos2026-fig-05-p8.png]]
*Fig. 5: Problem-normalised Critic-strategy contrasts under QwQ scoring. Top: mean per-turn score D_s̄. Bottom: convergence D_R, with bootstrap 95% CIs. Only Haiku (with the Sonnet Critic) shows a clear tone effect; strict and adversarial are never on top.*

![[Niarchos2026-fig-04-p7.png]]
*Fig. 4: Score-update fields v(s) for DS8B and DS70B. A zero crossing is a fixed point where further critique stops helping on average. Both scales stall near s ≈ 63 on Polchinski 2.7.*

## Limitations / caveats
- **Tone is manipulated only by one-line system prompts.** How "adversarial" the Critic actually was is not verified, e.g. by rating the tone of its messages.
- **The Critic sees the reference solution**, so this is tutoring rather than peer review between equals. The harshness effect may differ when the critic can be wrong. In this setup, erroneous critique (scenario c) is not studied.
- There are only 3 textbook problems, and pretraining contamination is acknowledged. The Haiku tone analysis uses only 2 problems.
- There is a single asymmetric pairing (Haiku/Sonnet), so asymmetry is confounded with model family (Claude vs DeepSeek). The "asymmetric pairing matters" claim rests on one data point.
- Results depend on the judge. The Sonnet Judge and the QwQ Judge disagree strongly on Polchinski (~1% vs 31% convergence for Haiku). The DS8B/DS70B ordering flips under DS70B re-scoring.
- **Effect sizes are small** (about ±2 points on 100), and the convergence tests for tone are non-significant. Many comparisons are made, with no stated correction.
- No safety outcomes are measured.
- This is a workshop paper.

## Related work to follow
- [[Laban2023 - Are You Sure Challenging LLMs Leads to Performance Drops in]]: challenge/critique degrading answers.
- [[McAleese2024 - LLM Critics Help Catch LLM Bugs]]: LLM critics for review.
- [[Wynn2025 - Talk isn't always cheap]]: when multi-agent discussion hurts.
- [[StengelEskin2024 - Teaching Models to Balance Resisting and Accepting]]: accepting vs resisting feedback.
- [[Kim2025 - Challenging the Evaluator]]: pushback in evaluation settings.
- [[Kale2025 - Reliable weak-to-strong monitoring]]: asymmetric monitor–agent capability.

![[Backlog.base#Cited by this paper]]
