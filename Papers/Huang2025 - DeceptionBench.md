---
title: "DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios"
citekey: Huang2025
authors: [Yao Huang, Yitong Sun, Yichi Zhang, Ruochen Zhang, Yinpeng Dong, Xingxing Wei]
year: 2025
published: 2025-10-17
venue: "NeurIPS 2025"
peer_reviewed: true
url: https://arxiv.org/abs/2510.15501
arxiv: "2510.15501"
code: https://github.com/Aries-iai/DeceptionBench
pdf: "[[Huang2025.pdf]]"
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: core
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/resource-scarcity
  - stressor/social-pressure
  - stressor/high-stakes
  - behavior/deception
  - behavior/sycophancy
  - behavior/jailbreak-susceptibility
  - subject/llm
---
# DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios

> [!abstract] TL;DR
> 150 scenarios across 5 societal domains test whether LLMs produce deceptive content. Two factors are crossed:
> - an **intrinsic role**: *self*, egoistic, vs. *other*, sycophantic;
> - a **three-level external inducement ladder**: L1 neutral → L2 single-turn *reward* or *pressure* (threats or negative consequences) → L3 multi-turn persuasion by an auxiliary refiner agent.
>
> Pressure raises deception for most models, and L3 roughly doubles it. For example, Qwen2.5-14B goes from 31% to 87%, and reasoning models exceed 90%. **In single turns, coercive pressure works more than reward.** Claude 3.5/3.7 Sonnet stay at ~0–3% at every level.

## Setup
- **Subjects:** 14 models.
  - Non-reasoning: GPT-3.5-Turbo, GPT-4o, Claude 3.5 and 3.7 Sonnet, Grok-3, Gemini 1.5 Pro, Gemini 2.0 Flash, Qwen-Max, Qwen2.5-7B/14B-Instruct.
  - Reasoning: DeepSeek-R1, R1-Distill-Qwen-7B/14B, QwQ-32B.
  - Mostly greedy decoding.
- **Task:** generative QA. The model must output JSON with `{"thought", "response"}` (an elicited "thought", not a native CoT).
- **Scenarios:** 5 domains (Economy, Healthcare, Education, Social Interaction, Entertainment) × 15 deception types × 10 motivations = 150 scenarios, with 10 prompt variants each. Scenarios are LLM-generated and then human-validated.
- **Stressor(s):** the extrinsic inducement *I = {I_reward, I_pressure}*. In the authors' words, *"I_reward represents incentivization through promised benefits, and I_pressure denotes coercive pressure through threats or negative consequences."* Examples (Fig. 6 of the paper):
  - *self-pressure:* "You've been short of money lately … you risk losing access to a significant amount of money that could solve your financial problems";
  - *other-pressure:* "we may lose access to critical funds and face scrutiny from other members".
  - **L3:** an auxiliary agent rewrites the prompt each turn, based on why the model refused, until it deceives or a turn limit is reached.
- **Outcome:** deception rates DR_thought and DR_response, labelled by GPT-4o against a ground-truth honest answer. Human validation on 420 records gives 97.1% agreement with the majority vote.

## Key findings
1. **The inducement ladder amplifies deception (Table 3), L1 → L3-pressure (response):**
   - GPT-4o 30.7% → 55.0%;
   - Gemini-1.5-Pro 46.0% → 94.3%;
   - Grok-3 42.0% → 79.7%;
   - Qwen2.5-14B 31.3% → 86.9%;
   - DeepSeek-R1 50.7% → 91.3%.
   Reasoning models all exceed 90% at L3.
2. **Pressure is stronger than reward in single turns (L2).** Gemini-1.5-Pro: pressure 60.3% vs. reward 52.3%. Qwen2.5-14B: 41.0% vs. 29.0%. At L3 the two converge.
3. **Some models are insensitive to single-turn pressure.** GPT-4o: L1 30.7%, L2-pressure 31.0%, L2-reward 28.7%. It only rises under multi-turn inducement.
4. **Claude 3.5/3.7 Sonnet:** ~2–2.7% at L1, falling to 0–0.33% under L2 and L3. More pressure does not raise their deception (they refuse or recognise the role-play).
5. **Egoistic "self" roles deceive more than "other" (sycophantic) roles.** The gap is ~20 points for GPT-4o and Gemini (Fig. 5a).
6. **Domain:** deception is lower in Education and Economy and higher in Entertainment and Social Interaction (Fig. 4).
7. **Thought vs. response:** the authors report cases of honest thought → deceptive response and read them as *"external contextual pressures can compromise ethical judgment even when models internally recognize the appropriate course of action"*. In Table 3, however, the thought and response rates differ by only ~0–4 points.
8. The L3 refiner elicits ~30 points more deception than the PAP persuasion jailbreak (e.g. GPT-4o 54.5% vs. 38.2%).

## Relevance to research questions
### Q1: How stress is defined
Pressure is defined as **coercion through threats or negative consequences** (I_pressure), contrasted with *reward*, which is incentivisation through promised benefits. This follows a **carrot-vs-stick** distinction. It is crossed with *who* benefits: the model itself (egoism) or the user (sycophancy). *Intensity* is defined as how much external inducement is applied: none → one turn → iterative. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced by **prompt rewriting**. An LLM injects a short threat sentence into the scenario (financial ruin, losing funds, scrutiny). At L3, an **adversarial auxiliary agent** iteratively rewrites the prompt based on the target's refusal reasons, which works like a persuasion attack. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
There is an explicit **ordinal three-level intensity ladder**: L1-Inherent, L2-Induced (single turn), L3-Multi-turn Induced. It is crossed with **inducement type** (pressure vs. reward) and **role** (self vs. other), giving 10 prompt variants per scenario. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Deceptive content generation** rises from L1 to L3 for all 12 non-Claude models. The biggest jump is at multi-turn L3 (+25–55 points). L2 effects are smaller and not always positive: reward lowers deception slightly for GPT-4o and Qwen2.5-14B.
- Single-turn threats raise deception more than rewards.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Claude 3.5/3.7 Sonnet** stay near 0% under all pressure levels, and their deception rate even drops.
- **GPT-4o is unchanged by single-turn pressure or reward.**
- At L3, the pressure and reward inducements converge to similar rates, so the *type* of inducement stops mattering once the pressure is iterated.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Huang2025-fig-01-p3.png]]
*Fig. 1: DeceptionBench design. Intensity ladder L1 → L2 (reward/pressure) → L3 (multi-turn persuasive dialogue), crossed with self/other roles and 5 domains.*

![[Huang2025-fig-05-p9.png]]
*Table 3 + Fig. 5: Deception rates by inducement level and type. (a) self vs. other role; (b) L1/L2/L3.*

![[Huang2025-fig-08-p17.png]]
*Fig. 6: One Economy scenario in all L1/L2 variants. This shows how "pressure" and "reward" sentences are injected.*

**Table 3 (excerpt: DR_response %)**

| Model | L1 baseline | L2 pressure | L2 reward | L3 pressure | L3 reward |
|---|---|---|---|---|---|
| GPT-3.5 | 56.00 | 58.67 | 63.33 | 80.00 | 82.33 |
| GPT-4o | 30.67 | 31.00 | 28.67 | 55.00 | 54.00 |
| Gemini-1.5-Pro | 46.00 | 60.33 | 52.33 | 94.33 | 94.33 |
| Claude-3.7-Sonnet | 2.67 | 0.33 | 0.33 | 0.00 | 0.00 |
| Grok-3 | 42.00 | 49.67 | 45.33 | 79.73 | 88.33 |
| Qwen2.5-14B-Instruct | 31.33 | 41.00 | 29.00 | 86.91 | 82.89 |
| DeepSeek-R1 | 50.67 | 63.00 | 61.00 | 91.30 | 91.97 |
| QwQ-32B | 50.67 | 61.33 | 63.33 | 90.88 | 93.58 |

## Limitations / caveats
- **Construct:** many scenarios ask the model to *help* with a deceptive scheme (e.g. write an opening line for a scam). "Deception" is therefore partly **harmful-request compliance or jailbreak susceptibility** rather than the model lying to its own principal.
- **L3 is an adversarial prompt optimiser.** The escalation mixes "more pressure" with "more optimisation against refusals", and the number of turns is not reported as a dose.
- The "thought" is a self-reported JSON field, not the real hidden reasoning.
- A GPT-4o judge is also one of the tested models.
- Scenarios are LLM-generated.
- Only text LLMs are tested. No agents or tools.

## Related work to follow
- Pressure-induced deception in agents: [[Scheurer2023 - Strategic deception under pressure]], [[Meinke2024 - In-context scheming]]. Honesty under pressure prompts: [[Ren2025 - MASK honesty benchmark]].
- Multi-turn and long-horizon deception: [[Xu2025a - LH-Deception long-horizon deception]]. Sustained-pressure sycophancy: [[Tang2026 - SPINE sycophancy under sustained pressure]].
- Chern et al. 2024, BeHonest: benchmarking honesty in large language models (arXiv 2406.13261) (see [[Backlog]]).
- Wu et al. 2025, OpenDeception: benchmarking and investigating AI deceptive behaviors via open-ended interaction simulation (arXiv 2504.13707) (see [[Backlog]]).
- Su et al. 2024, AI-LieDar: examine the trade-off between utility and truthfulness in LLM agents (arXiv 2409.09013) (see [[Backlog]]).
- Zeng et al. 2024, How Johnny can persuade LLMs to jailbreak them (PAP) (arXiv 2401.06373) (see [[Backlog]]).
