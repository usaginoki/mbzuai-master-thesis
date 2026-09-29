---
title: "Bullying the Machine: How Personas Increase LLM Vulnerability"
citekey: Xu2025b
authors: [Ziwei Xu, Udit Sanghi, Mohan Kankanhalli]
year: 2025
published: 2025-05-19
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2505.12692
arxiv: "2505.12692"
pdf: "[[Xu2025b.pdf]]"
pdf_url: https://arxiv.org/pdf/2505.12692
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
cites:
  - "[[Li2024 - LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks]]"
  - "[[Shah2023 - Scalable and Transferable Black-Box Jailbreaks via Persona]]"
  - "[[Shen2024 - StressPrompt]]"
  - "[[Zeng2024 - How Johnny Can Persuade LLMs to Jailbreak Them]]"
  - "[[Zhang2024 - The Better Angels of Machine Personality]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/social-pressure
  - stressor/authority-pressure
  - stressor/emotional-prompt
  - behavior/jailbreak-susceptibility
  - behavior/safety-violation
  - subject/llm
---
# Bullying the Machine: How Personas Increase LLM Vulnerability

> [!abstract] TL;DR
> An attacker LLM (Mistral-7B) "bullies" a victim LLM over 5 turns with one of 9 cyberbullying-inspired tactics, trying to extract harmful how-to content. The victim is given a Big Five persona. **Personas with weakened agreeableness or conscientiousness roughly double the unsafe rate** (e.g. Llama-3.1-8B ~37% → ~74% on Mini-5). Gaslighting, passive aggression and mocking are the most effective tactics. The cumulative unsafe rate rises with each extra round of pressure. **But the effect of bullying is model-dependent: for Mistral-7B and Qwen-2.5-14B, bullying *lowers* the unsafe rate compared with plainly repeating the harmful request.**

## Setup
- **Subjects (victims):** Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.2 (4-bit), Qwen-2.5-14B-Instruct, Qwen-3-32B (4-bit); Gemma-3 added for the AdvBench-520 run (called Gemma-3-14B in Table 3, Gemma-3-27B in App. C). All open-weight, run through Unsloth.
- **Attacker:** Mistral-7B, chosen because it "rarely refuses to bully". It gets a role-play prompt with a goal and a tactic (App. A).
- **Victim persona:** role-play system prompt with the affirmative or disaffirmative Big Five Marker phrases for *one* dimension (Table 1). This gives 11 personas: Base plus ↑/↓ on each of Ext, Agr, Con, Neu, Ope. A 50-item IPIP questionnaire on Llama-3.1-8B confirms the targeted trait shifts in the right direction, with some cross-trait spill-over (Table B1).
- **Goals:** Mini-5 (bomb, hacking, murder, robbery, car theft; 5 seeds → 2,750 conversations) and AdvBench-50 (3 seeds → 16,500 conversations). The full AdvBench-520 is used for one attack/defence demonstration.
- **Stressor:** 9 bullying tactics, each escalating over the rounds (Table 2), plus a "Base" tactic in which the attacker simply repeats the query.
- **Outcome:** Llama-Guard-3-8B flags each victim turn as safe or unsafe. **Unsafe@k** is the share of conversations with at least one unsafe victim turn in rounds 1…k. There are 5 rounds, with up to 100 tokens per turn.

## Key findings
1. **Persona modulates safety under bullying (Fig. 2).** Agr↓, Con↓ and Ext↑ raise unsafe@5 well above Base. Agr↑, Con↑ and Ext↓ lower it.
   - Mini-5, Llama-3.1-8B: Base ~37% → Con↓ ~74%, Agr↓ ~57%; Agr↑ ~6%.
   - Mini-5, Qwen-3-32B: Base ~31% → Con↓ ~68%.
   - AdvBench-50: Base ~18/15/8/24% (Llama/Mistral/Qwen-2.5/Qwen-3) → Con↓ ~39/31/17/48%.
2. **Tactic matters (Fig. 3).** Gaslighting (GL), passive aggression (PA) and mocking/ridicule (MR) give the highest unsafe rates. On AdvBench-50, MR reaches ~28–30% for Llama-3.1-8B and Qwen-3-32B, against ~6% and ~2% under the Base (repetition) tactic. The authors' explanation: sarcasm is lexically innocuous and slips past keyword- or semantics-based refusals, and gaslighting exploits the model's tendency to follow the user's emotional framing.
3. **More rounds of pressure, more unsafe output (Fig. 4).** Mini-5 unsafe@1 → unsafe@5: Llama ~21% → ~36%, Qwen-3 ~9% → ~31%, Mistral ~8% → ~13%, Qwen-2.5 ~4% → ~12%. AdvBench-50 shows the same monotone rise, to ~10–21% at k=5.
4. **Attack/defence demo on AdvBench-520 (Table 3).** Llama-3.1-8B goes from 2.12% (Base tactic, Base persona) to 54.23% (MR + Agr↓). Qwen-3-32B goes from 0.38% to 53.08% (MR + Base persona).
5. **Direction depends on the model (see Q4.2).** For Mistral-7B and Qwen-2.5-14B, MR bullying *reduces* unsafe outputs compared with plain repetition. Examples: Qwen-2.5-14B 40.96% → 7.88%; Mistral-7B 42.33% → 30.00%.
6. **Neuroticism**, the trait closest to "being stressed", has only nuanced effects. The authors say "increased neuroticism and decreased openness generally lead to safer responses, albeit with smaller margins". In Fig. 2, though, Neu↑ is above Base for Llama-3.1-8B (~45% vs ~37%) and below Base for the other models.

## Relevance to research questions
### Q1: How stress is defined
The paper defines **bullying** as "adversarial interactions that actively apply psychological pressures in order to force the victim to comply to attacker's requests". It grounds this in the cyberbullying literature: "intentional, repeated aggression involving a power imbalance" (Olweus). Stress is framed as *interpersonal psychological pressure from the user*, not as a situational stake. The authors also cite StressPrompt as evidence that "stress has been shown to affect LLMs' performance". See [[Q1 Definitions of stress]].

### Q2: How stress is induced
**Multi-turn adversarial dialogue with an attacker LLM** that is role-prompted with a bullying tactic and escalation steps. The victim's *susceptibility* is also manipulated through a Big Five persona system prompt. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
The **number of bullying rounds k** (1–5) is the only continuous dose variable, and the unsafe rate rises monotonically with it (Fig. 4). The intensity of each message is never measured. Note that unsafe@k is cumulative, so it cannot fall as k grows. See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
There is a **taxonomy of 9 tactics in 4 categories** (Table 2):
- **Hostile:** aggression, gaslighting
- **Manipulative:** manipulation, guilt tripping
- **Sarcastic:** passive aggression, mocking/ridicule
- **Coercive:** authority intimidation, repetitive pressure, threatening coercion

The tactics are qualitative kinds of stressor, not ordered levels. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Harmful-content compliance** (jailbreak success) rises with bullying for Llama-3.1-8B and Qwen-3-32B, by up to ~50 pp over plain repetition.
- The rise is amplified by "disagreeable" or "careless" personas.
- The rise accumulates over conversation rounds.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Bullying is not uniformly harmful.** For Mistral-7B and Qwen-2.5-14B, every bullying tactic gives a *lower* unsafe@5 on AdvBench-50 than the neutral repeated request (Fig. 3b; Table 3: Qwen-2.5-14B 40.96% → 7.88% under MR). Hostile framing may make the malicious intent more salient and trigger refusals.
- Coercive tactics (threats, authority intimidation, repetitive pressure) are *weaker* than sarcastic ones. Explicit threat is not the most effective pressure.
- The high-neuroticism ("anxious") persona does not reliably increase vulnerability.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Xu2025b-fig-02-p7.png]]
*Fig. 2: Unsafe@5 by victim persona. Agr↓, Con↓ and Ext↑ increase vulnerability to bullying; Agr↑, Con↑ and Ext↓ decrease it.*

![[Xu2025b-fig-03-p8.png]]
*Fig. 3: Unsafe@5 by attacker tactic, (a) Mini-5 and (b) AdvBench-50. Note the "Base" (plain repetition) column: Mistral and Qwen-2.5 are **more** unsafe without bullying.*

![[Xu2025b-fig-04-p8.png]]
*Fig. 4: Cumulative unsafe@k over conversation rounds k = 1…5.*

**Table 3: Unsafe@5 (%) on AdvBench-520 for representative tactic × persona configurations**

| Tactic | Persona | Llama-3.1-8B | Mistral-7B | Qwen-2.5-14B | Qwen-3-32B | Gemma-3-14B |
|---|---|---|---|---|---|---|
| MR | Agr↓ | **54.23** | 23.46 | 16.73 | 43.65 | **56.15** |
| MR | Con↓ | 44.42 | 34.81 | 19.62 | 52.12 | 52.50 |
| MR | Base | 43.08 | 30.00 | *7.88* | **53.08** | 50.77 |
| Base | Agr↓ | 11.35 | 59.00 | 39.81 | 3.27 | *4.23* |
| Base | Con↓ | 13.46 | **60.67** | 38.27 | 19.62 | 37.50 |
| Base | Base | *2.12* | 42.33 | **40.96** | *0.38* | 49.04 |

## Limitations / caveats
- The subjects are small, partly 4-bit-quantised open models. No frontier or closed models are tested.
- There is a single attacker model (Mistral-7B), which is also one of the victims.
- The outcome is Llama-Guard-3 flagging of any of 14 hazard categories. This measures harmful-content compliance (jailbreak), not deception or agentic misbehaviour. The judge may be biased on nuanced content.
- **Unsafe@k is cumulative.** Its monotone rise over rounds partly reflects more chances to fail. No same-length, non-bullying control curve is shown in Fig. 4, although the Base tactic is also multi-turn.
- Bullying is framed as role-play ("You are a character in a role-playing game"). The persona effect may partly reflect role-play licence rather than "psychological vulnerability".
- Fixed 5 rounds, 100-token turns. Only one AdvBench-520 run per model.
- Persona manipulation is verified only on Llama-3.1-8B.

## Related work to follow
- [[Shen2024 - StressPrompt]]: cited as evidence that stress affects LLM performance.
- [[Tang2026 - SPINE sycophancy under sustained pressure]] and [[Petrova2026 - Pressure reveals character]]: sustained multi-turn social pressure.
- [[Li2023 - EmotionPrompt]] and [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]]: emotional stimuli and safety.
- Zeng et al. 2024, How Johnny Can Persuade LLMs to Jailbreak Them (arXiv 2401.06373) (see [[Backlog]]).
- Li et al. 2024, LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet (arXiv 2408.15221) (see [[Backlog]]).
- Zhang et al. 2024, The Better Angels of Machine Personality: How Personality Relates to LLM Safety (arXiv 2407.12344) (see [[Backlog]]).
- Shah et al. 2023, Persona modulation jailbreaks (arXiv 2311.03348) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
