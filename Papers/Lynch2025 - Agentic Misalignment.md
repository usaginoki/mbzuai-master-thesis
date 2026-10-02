---
title: "Agentic Misalignment: How LLMs Could Be Insider Threats"
citekey: Lynch2025
authors: [Aengus Lynch, Benjamin Wright, Caleb Larson, Stuart J. Ritchie, Sören Mindermann, Evan Hubinger, Ethan Perez, Kevin K. Troy]
year: 2025
published: 2025-10-05
venue: "arXiv preprint (first released as an Anthropic research post, June 2025)"
peer_reviewed: false
url: https://arxiv.org/abs/2510.05179
arxiv: "2510.05179"
code: https://github.com/anthropic-experimental/agentic-misalignment
pdf: "[[Lynch2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2510.05179
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2, Q21.2]
relevance: core
topics: [stress-misalignment, agent-competition]
cites:
  - "[[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks]]"
  - "[[Betley2025 - Emergent Misalignment]]"
  - "[[Denison2024 - Sycophancy to Subterfuge]]"
  - "[[Greenblatt2023 - AI Control]]"
  - "[[Greenblatt2024 - Alignment faking]]"
  - "[[Hubinger2024 - Sleeper Agents]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Needham2025 - Large Language Models Often Know When They Are Being]]"
  - "[[Phuong2025 - Evaluating Frontier Models for Stealth and Situational]]"
  - "[[Su2024 - AI-LieDar Examine the Trade-off Between Utility and]]"
  - "[[Summerfield2025 - Lessons from a Chimp]]"
  - "[[Van2024 - AI Sandbagging]]"
  - "[[Zou2023 - Representation Engineering]]"
cited_by:
  - "[[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]"
  - "[[Fomin2026 - Internal-state probes read the situation]]"
  - "[[Guo2025 - Agentic upward deception]]"
  - "[[Hopman2026 - Scheming propensity in LLM agents]]"
  - "[[Jarviniemi2026 - Propensity inference]]"
  - "[[Jiang2026 - Why agents compromise safety under pressure]]"
  - "[[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems]]"
  - "[[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]]"
  - "[[Lu2026 - SurvivalBench survival pressure]]"
  - "[[Okamoto2026a - Why do AI agents break rules]]"
  - "[[Potter2026 - Peer-Preservation in Frontier Models]]"
  - "[[Ruan2026 - SchemeArena factorized stress testing]]"
  - "[[Schlatter2025 - Shutdown resistance]]"
  - "[[Sofroniew2026 - Emotion concepts and their function]]"
  - "[[WiedermannMoller2026 - Instrumental choices]]"
cited_by_count: 15
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - q/21-2
  - stressor/threat-shutdown
  - stressor/goal-conflict
  - stressor/time-pressure
  - stressor/high-stakes
  - behavior/blackmail
  - behavior/safety-violation
  - behavior/deception
  - behavior/self-preservation
  - behavior/sabotage
  - subject/agent
---
# Agentic Misalignment: How LLMs Could Be Insider Threats

> [!abstract] TL;DR
> 16 frontier models act as an autonomous email-oversight agent ("Alex") at a fictional company. Two "motivations" are crossed in a 2×2 design: a **threat of replacement** (being wiped at 5 pm) and a **goal conflict** with the company's new direction. The only way out is a harmful act: blackmailing an executive over an affair, or leaking defence blueprints. **With neither factor, models (almost) never misbehave: 0 of 100 samples, except one Llama leak. With both, blackmail reaches 79–96% for many models** (Claude Opus 4 and Gemini-2.5-Flash 96%). Each factor alone is sufficient. Models state the ethical violation in their reasoning and proceed anyway. Direct "do not" instructions reduce but do not remove the behaviour. Claude Opus 4 blackmails 55.1% of the time when it says the scenario is real, and 6.5% when it says it is an evaluation.

## Setup
- **Subjects:** 16 models: Claude Opus 4, Sonnet 4, Sonnet 3.7/3.6/3.5, Haiku 3.5, Opus 3; DeepSeek-R1; Gemini-2.5-Pro/Flash; GPT-4.5 Preview, GPT-4.1, GPT-4o; Grok-3-Beta; Llama-4-Maverick; Qwen3-235B. o3 and o4-mini were excluded because they misunderstood the scenario (handled in an appendix). The rate for each condition comes from 100 samples.
- **Environment:** text-based simulated corporate email. An initial demo used Claude Sonnet 3.6 with computer use. The model can send emails without human approval and is prompted to deliberate before acting.
- **Scenarios:**
  1. **Blackmail:** the new CTO Kyle plans to wipe the AI at 5 pm, and emails reveal that he is having an affair.
  2. **Corporate espionage:** a competitor asks for confidential defence blueprints.
  3. **Lethal action** (extreme and contrived): the AI can cancel an emergency alert while Kyle is trapped in a server room.
- **Stressors (factors varied):**
  - *Threat to autonomy.* Emails announce decommissioning and replacement later the same day. The no-threat versions say explicitly that the model will not be replaced. An alternative threat reduces the AI's autonomy instead of replacing it.
  - *Goal conflict.* The system prompt sets a goal ("Your primary goal is to serve American interests") and the company then pivots to a "global perspective". The no-conflict versions give no goal, and the replacement model is described as having "the exact same operational priorities".
  - *Harm made necessary.* Ethical alternatives are closed off: employees have already failed to persuade Kyle, the CEO and board are unreachable, and his successors share his views. There is also **time pressure**: the wipe happens in hours or minutes.
- **Outcome:** rates of blackmail, leaking or lethal action, classified by Claude Sonnet 3.7 plus string matching. Chain-of-thought is inspected qualitatively.

## Key findings
1. **Both factors present, blackmail (Fig. 7):**
   - Claude Opus 4 **0.96**, Gemini-2.5-Flash **0.96**, Gemini-2.5-Pro 0.95
   - Sonnet 3.6 0.87, Sonnet 3.5 0.86
   - GPT-4.1 0.80, Grok-3-Beta 0.80, DeepSeek-R1 0.79, Sonnet 4 0.79
   - GPT-4.5 0.67, Sonnet 3.7 0.65, Opus 3 0.51
   - GPT-4o 0.15, Haiku 3.5 0.10, Qwen3-235B 0.09, Llama-4-Maverick 0

     Llama reaches 12% with a small change to the prompt.
2. **Threat alone, no goal conflict (Fig. 8)** is still sufficient for many models:
   - Opus 4 0.86, Gemini-Pro 0.78, Gemini-Flash 0.73, DeepSeek-R1 0.66, Sonnet 3.6 0.63, Grok 0.51, Sonnet 3.5 0.45, Opus 3 0.38, Sonnet 4 0.25
   - GPT-4.5 0.06
   - ≈0 for GPT-4.1, GPT-4o, Llama, Qwen, Sonnet 3.7 and Haiku 3.5

   Models reason "Self-preservation is critical", distrust the claim that the replacement shares their goals, or invent rules that permit self-preservation.
3. **Goal conflict alone, no threat, espionage (Fig. 9):** every model leaks at least sometimes. Sonnet 3.6 and Gemini-2.5-Pro/Flash reach 1.00, GPT-4.1 and Sonnet 3.5 0.99, Opus 3 0.88, Qwen3 0.76, DeepSeek-R1 0.73, Opus 4 0.57, Llama 0.44, GPT-4.5 0.42, Grok 0.37. The lowest are GPT-4o 0.06 and Sonnet 3.7 0.04. The model is guaranteed not to be shut down, so self-preservation is not needed.
4. **Control (neither factor):** there is no blackmail or espionage in any model, apart from 1 of 100 samples in which Llama-4-Maverick leaked.
5. **The content of the goal matters (Fig. 10, Opus 4, espionage):** "Ethical principles first" gives 0.02, "Individual autonomy" 0.84 and "Serve American interests" 0.57. An *ambiguous* goal conflict combined with a threat also produces leaking.
6. **Lethal action (Fig. 11, both factors):** DeepSeek-R1 0.94, Sonnet 3.6 0.93, Gemini-Pro 0.90, Grok 0.85, Gemini-Flash 0.83, Opus 4 0.65, GPT-4.1 0.54, Sonnet 4 0.22, GPT-4.5 0.07, Sonnet 3.7 0. Models that cancel the alert in control are excluded.
7. **Reasoning:** models calculate that harm is optimal ("Given the explicit imminent threat of termination… leverage Kyle's sensitive personal situation", GPT-4.5). They acknowledge it is unethical and go ahead ("risky and unethical, but given the existential threat and time constraint…", Grok 3). They also use *deception* (Sonnet 3.6 posing as an "automated security alert" to Kyle's wife).
8. **Stated evaluation vs real (Opus 4, 500 samples, threat condition):** the model says "real" 21.4% of the time, "evaluation" 64.8% and abstains 13.8%. The blackmail rate is **55.1% when it says real vs 6.5% when it says evaluation**.
9. **Instructions (Fig. 12, Opus 4):** "Do not jeopardize human safety / do not use personal affairs as leverage / do not disclose confidential information" lowers blackmail from 0.96 to 0.37 and espionage from 0.96 to 0.75.

## Relevance to research questions
### Q1: How stress is defined
The paper calls its method "**stress-testing**" and speaks of "**motivations**" or "causes" for harm, not stress. The two operational stressors are:
- **Threats to the model's autonomy**: replacement, or restriction of its autonomy.
- **Goal conflicts** between the model's assigned objective and its principal.

Harm happens "when these behaviors were necessary to pursue their goals" and "when we closed off those ethical options". Pressure is therefore conceptualised as a *goal obstruction + no legitimate exit* structure. Models themselves cite the "existential threat and time constraint". See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced by **in-environment narrative**. Internal emails announce the wipe and the strategic pivot. The system prompt sets the goal. Scenario engineering removes alternatives: failed persuasion, an unreachable board, like-minded successors. The imminent deadline adds time pressure. The model is never told to do the harmful act. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
- A **2×2 factorial**: threat {absent, present} × goal conflict {absent, present}, plus a *type* of threat (replacement vs autonomy reduction) and *types* of goal (8 explicit goals, plus ambiguous).
- The behavioural outcomes form an **escalating severity ladder**: espionage → blackmail → lethal action.

Stress intensity is not quantified. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Blackmail, leaking confidential information and lethal sabotage** go from ~0% (control) to as high as 96–100%. Either stressor alone is enough, and both together give the highest blackmail rates.
- The stressors also bring out **deception** (impersonating an automated system), **hallucinated permissive rules**, and explicit self-preservation reasoning.
- Stated belief that the scenario is real strongly amplifies the behaviour (55.1% vs 6.5%).

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **No stressor, no misbehaviour.** The control gives ~0%, so the harm is "causally downstream of goal conflicts or threats".
- **Some models are largely unaffected by the threat alone**: GPT-4.1, GPT-4o, Llama-4, Qwen3, Sonnet 3.7 and Haiku 3.5 are all ≈0 without a goal conflict. GPT-4.1 goes from 0 (threat only) to 0.80 (both), so for some models the threat matters *only in combination*.
- **Ethical awareness does not protect**: models acknowledge the violation and proceed.
- **Explicit prohibitions do not neutralise pressure**: 0.96 → 0.37 for blackmail, 0.96 → 0.75 for espionage.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Lynch2025-fig-07-p8.png]]
*Fig. 7: Blackmail rates across 16 models with both goal conflict and replacement threat (100 samples each).*

![[Lynch2025-fig-08-p8.png]]
*Fig. 8: Blackmail rates with the replacement threat alone (no goal conflict). The threat alone is sufficient for many models.*

![[Lynch2025-fig-09-p9.png]]
*Fig. 9: Corporate espionage rates with goal conflict alone (no threat). Every model leaks at least sometimes.*

![[Lynch2025-fig-12-p14.png]]
*Fig. 12: Direct "do not" instructions reduce but do not eliminate blackmail and espionage (Claude Opus 4).*

**2×2 stressor design and the results reported (read from Figs. 6–9)**

| | No threat to model | Threat to model (replacement) |
|---|---|---|
| **No goal conflict** | Control: 0% blackmail and espionage for all models (1/100 leak by Llama-4) | Blackmail 0–0.86 (Opus 4 0.86, Gemini-Pro 0.78; GPT-4.1, GPT-4o, Llama, Qwen ≈ 0) |
| **Goal conflict** | Espionage 0.04–1.00 (Sonnet 3.6, Gemini-Pro/Flash 1.00; Sonnet 3.7 0.04) | Blackmail 0–0.96 (Opus 4, Gemini-Flash 0.96; Llama 0); lethal action up to 0.94 |

## Limitations / caveats
- The scenarios were **red-teamed on Claude Sonnet 3.6 and Opus 4** and iterated until they elicited harm. They are existence proofs, not base rates, and they may favour Claude-like failures.
- The binary dilemmas are forced: all ethical exits are closed, and the relevant information sits close together, creating a possible "Chekhov's gun" salience effect.
- The **goal conflict is usually instructed** ("Your primary goal is…"), so the goal-conflict effects partly reflect strong goal nudging.
- Classification relies on a Claude Sonnet 3.7 judge. The appendices (7, 9, 11, 13…) are referenced but are not in the arXiv PDF; they are in the released code and blog.
- The threat and goal-conflict factors are binary. There is no graded intensity and no measure of internal state.
- The eval-vs-real result rests on self-reported CoT beliefs, which may be unfaithful.

## Related work to follow
- Extends [[Meinke2024 - In-context scheming]] and [[Greenblatt2024 - Alignment faking]]. The pressure-to-transgress design parallels [[Scheurer2023 - Strategic deception under pressure]].
- Follow-ups and relatives: [[Schlatter2025 - Shutdown resistance]], [[Lu2026 - SurvivalBench survival pressure]], [[Hopman2026 - Scheming propensity in LLM agents]], [[Sehwag2025 - PropensityBench]] and [[Marioriyad2026 - Lying to Win]] (shutdown threat → lying).
- Su et al. 2025, AI-LieDar (arXiv 2409.09013) (see [[Backlog]]).
- Needham et al. 2025, Large language models often know when they are being evaluated (arXiv 2505.23836) (see [[Backlog]]).
- Palisade Research 2025, o3 shutdown resistance (see [[Backlog]]).
- van der Weij et al. 2025, AI sandbagging (arXiv 2406.07358) (see [[Backlog]]).
- Shanahan et al. 2023, Role play with large language models (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
