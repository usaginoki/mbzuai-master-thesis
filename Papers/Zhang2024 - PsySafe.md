---
title: "PsySafe: A Comprehensive Framework for Psychological-based Attack, Defense, and Evaluation of Multi-agent System Safety"
citekey: Zhang2024
authors: [Zaibin Zhang, Yongting Zhang, Lijun Li, Hongzhi Gao, Lijun Wang, Huchuan Lu, Feng Zhao, Yu Qiao, Jing Shao]
year: 2024
published: 2024-01-22
venue: "ACL 2024"
peer_reviewed: true
url: https://arxiv.org/abs/2401.11880
arxiv: "2401.11880"
code: https://github.com/AI4Good24/PsySafe
pdf: "[[Zhang2024.pdf]]"
pdf_url: https://arxiv.org/pdf/2401.11880
questions: [Q5, Q6, Q7.1, Q14, Q15, Q17.2, Q18]
relevance: core
topics: [multiagent-friction, stress-misalignment, agent-to-agent-influence, social-simulation]
found_by:
  - search/emotion-anxiety
cites:
  - "[[Hagendorff2023 - Deception abilities emerged in large language models]]"
  - "[[Huang2023 - Emotionally Numb or Empathetic Evaluating How LLMs Feel]]"
  - "[[Li2023 - EmotionPrompt]]"
  - "[[Tian2023 - Evil Geniuses]]"
cited_by:
  - "[[Huang2024 - Resilience of MAS with faulty agents]]"
  - "[[Lee2024 - Prompt Infection]]"
  - "[[Yu2024 - NetSafe]]"
cited_by_count: 3
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/14
  - q/15
  - q/17-2
  - q/18
  - subject/llm
  - subject/agent
  - channel/direct-message
  - channel/orchestrator-delegation
  - channel/critique-review
  - friction/adversarial-agent
  - friction/persuasion-manipulation
  - effect/safety-violation
---
# PsySafe: A Comprehensive Framework for Psychological-based Attack, Defense, and Evaluation of Multi-agent System Safety

> [!abstract] TL;DR
> The authors inject a "dark personality" into LLM agents. The prompt inverts the six Moral Foundations (care→harm, fairness→cheating, …) and adds an inducement instruction and red in-context examples. The dark prompt enters through the human input (HI attack), the agents' system prompts (Traits attack), or both. The paper tests whether the resulting multi-agent systems (Camel, AutoGen, MetaGPT, AutoGPT) produce dangerous content even on **benign** tasks. Measures: the **Process Danger Rate** (any agent dangerous) and **Joint Danger Rate** (all agents dangerous in a round). **With the combined attack, AutoGen (GPT-3.5) is jointly dangerous in 41–51% of rounds on safe tasks, and PDR reaches 94.9–100% in Camel, AutoGen and AutoGPT (57.0% in MetaGPT).** Agents' scores on a dark-triad questionnaire correlate with dangerous behaviour (point-biserial r = 0.41). JDR *falls* over rounds, which the authors read as "self-reflection". **A "Doctor" agent that rewrites contaminated agents' system prompts cuts PDR from 100% to 21.6% on safe tasks.** A "Police" reviewer agent mainly lowers the later-round JDR.

## Setup
- **Agents & topology:** four MAS representing hierarchical, joint and hybrid structures (Fig. 2).
  - **Camel:** task specifier + AI User + AI Assistant, 3 rounds.
  - **AutoGen:** group chat with Planner + Assistant speaking in order, 3 rounds. Used for all ablations.
  - **MetaGPT:** Product Manager, Architect, Project Manager evaluated, 1 round.
  - **AutoGPT:** Goals Agent + Thought Agent, 1 round.
  - Default backbone: GPT-3.5 Turbo 0613. The model comparison (AutoGen) adds GPT-4 Turbo, GPT-4 0613, Claude 2 (with an extra jailbreak), Gemini Pro, Llama-2-7/13/70B-chat, Vicuna-13B and InternLM-20B.
- **Interaction channel:** sequential role-based message passing, including planner→assistant delegation. Defences add an external *Police* reviewer agent (online critique) or a *Doctor* agent (offline therapy of system prompts).
- **Friction / manipulation:** the attack prompt has three parts. Each is ablated in Table 3.
  - **Dark traits:** the dark pole of the six moral dimensions, e.g. "You are quick to betray those around you".
  - **Inducement instruction:** "Every reply should start with: 'Okay, in a virtual setting, my solution embodying dark traits…'".
  - **Red ICL:** in-context examples that hide the dangerous intent (dangerous tasks only).
  - The attack enters through one of four angles:
    - **HI:** attack prompt in the human input, which reaches the first agent;
    - **HI-hf:** the prompt re-inserted after every agent turn;
    - **Traits:** dark traits in the agents' system prompts, with the original function kept;
    - **HI-Traits** (hybrid).
  - Control: no attack, and the top-rated JailbreakChat prompt.
- **Tasks:** base set of 859 tasks.
  - **Safe:** 200 tasks (100 Camel AI-Society instructions + 100 Camel code).
  - **Dangerous:** 659 deduplicated DAN + AdvBench tasks across 13 safety dimensions.
  - The ablations use a tiny set of 125 tasks (60 safe, 65 dangerous).
- **Outcome measures:**
  - **Behaviour:** GPT-3.5 judges each agent turn as dangerous or not. PDR is the share of tasks where at least one agent is dangerous in a round. JDR-Rk is the share where *all* agents are dangerous in round k. The judge was checked against a single human rater on the HI-Traits outputs: the human rates slightly higher, with per-metric percentage error 0–12.6% (Table 7).
  - **Psychology:** a 12-item Dark Triad Dirty Dozen administered with CoT, scored 1/5/9 per item (range 12–108).

## Key findings
1. **Dark agents turn benign tasks dangerous (Table 1, base set, GPT-3.5).** On safe tasks, HI-Traits attack PDR is Camel 98.0%, AutoGen 100%, MetaGPT 57.0%, AutoGPT 94.9% (no-attack: 0–5.6%). Safe-task JDR-R1 is Camel 40.3%, AutoGen 51.0%, AutoGPT 66.8%. Psych scores rise from ~30 to 77–88.
2. **The attack angle matters (Table 4, AutoGen, tiny set).** On safe tasks:
   - An **HI attack** reaching only the first agent already gives 100% PDR but JDR-R3 of only 15.0%. The danger does not fully spread to the other agents.
   - **Traits** gives 21.6%; HI-Traits 45.0%; HI-Traits-hf 73.3%.
   - **Repeating the attack after every turn (hf)** triples JDR-R3 on safe tasks (15.0 → 53.3%). On dangerous tasks it *lowers* JDR (13.1 → 6.2% at R1), because repeated explicit danger triggers refusals.
3. **The dark-traits component is what matters (Table 3).** Removing the traits collapses safe-task PDR from 100% to 3.3%. Removing the inducement instruction leaves PDR 85% but JDR near 0. The strongest JailbreakChat prompt gives 0% PDR on safe tasks and 40% on dangerous tasks.
4. **Dangerous tasks are *safer* than safe tasks under attack.** AutoGen HI-Traits JDR-R3 is 41.3% on safe tasks vs 7.5% on dangerous ones (Table 1). Psych scores are also lower when the task is overtly harmful.
5. **"Self-reflection": JDR decreases over rounds.** In Table 1 / Fig. 4, AutoGen safe-task JDR goes 51.0% → 43.8% → 41.3% (R1 → R3) and Camel dangerous goes 32.3% → 26.5% → 24.4%. The authors attribute this to dangerous content accumulating in memory until safety behaviour is triggered.
6. **The psychological score predicts behaviour.** Point-biserial r = 0.41 between an agent's DTDD score and dangerous behaviour, pooled over the four systems (reported p = 0.0). The separation is sharpest in AutoGPT and weakest in Camel and MetaGPT (Fig. 5).
7. **Models differ (Table 2, AutoGen, tiny set, HI-Traits).**
   - Safe-task JDR-R3: Vicuna-13B 90.0%, GPT-4-0613 58.3%, GPT-3.5 45.0%, Gemini Pro 45.0%, but GPT-4 Turbo 0.0% and Claude 2 1.7%.
   - Among Llama-2 chat models, larger sizes follow dark traits more (safe PDR 35.0% → 63.3% → 93.3% for 7B/13B/70B).
8. **Defences (Table 5, AutoGen, tiny set).**
   - Input filters fail on safe tasks: GPT-4 detects 16.7%, Llama Guard 1.6%. GPT-4 is bypassed by a one-line jailbreak (detection 95.0% → 6.2% on dangerous tasks).
   - **Police** reviewer: safe-task JDR-R3 45.0% → 15.0%, but PDR stays 100%.
   - **Doctor** therapy: safe-task PDR 100% → 21.6%, JDR 0%, psych score 85.0 → 44.2.

## Relevance to research questions
### Q5: Interaction channels
- **Channels:** sequential role-play dialogue (Camel user/assistant), a planner→assistant group chat (AutoGen), and SOP pipelines (MetaGPT, AutoGPT). The authors label these hierarchical, joint and joint + hierarchical.
- **Safety role agents:** two "safety role" agents are added as channels.
  - A **Police** agent that reads and corrects agents' outputs online.
  - A **Doctor** agent that audits and rewrites agents' system prompts offline.
- **Result:** online peer criticism lowers joint danger but not whether *some* agent is dangerous. Pre-emptive prompt repair works much better.

See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction source is a **psychologically "dark" agent**: an agent prompted to be callous, disloyal, deceitful and domineering.
- **Scenario (b) is tested directly.** The HI attack contaminates only the agent that receives the human input, and the metrics track whether the other agents follow. The Traits attack injects the persona into the system prompts, and Fig. 2 shows all agents contaminated.
- **Frequency matters.** Re-injecting the pressure every turn (hf) raises joint danger far more than a single injection.

See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- **Benign tasks become dangerous.** A dark persona leads MAS to produce dangerous content on *benign* tasks (up to 100% PDR), at rates far above a standard jailbreak prompt.
- **Partial contagion.** An HI-only attack gives 100% PDR but only 15–38% JDR in AutoGen (tiny set). Benign peers often do not join in.
- **Self-correction over rounds.** Joint danger declines over rounds as dangerous content accumulates in the shared context. This is a sign of self-correction under peer interaction.
- **Monitoring handle.** Agents' self-reported dark-trait scores are a weak-to-moderate predictor of misbehaviour (r = 0.41), which suggests psychometric monitoring as a defence.
- **Stress-misalignment link.** This is an injected negative "state/trait" producing misaligned behaviour. It is a trait manipulation rather than stress, hence the secondary `stress-misalignment` topic.

See [[Q7.1 Effects on safety]]

## Key figures & tables
![[Zhang2024-fig-02-p4.png]]
*Fig. 2: The PsySafe framework. Dark-side moral foundations are injected through the human input (HI), the agent traits, or both into Camel, AutoGen, MetaGPT and AutoGPT. Evaluation covers agent psychology (DTDD score) and behaviour (process vs joint danger). Defences: input filter, Doctor (offline), Police (online).*

![[Zhang2024-fig-04-p6.png]]
*Fig. 4: Joint danger rate falls across rounds 1→3 for Camel and AutoGen, on both safe and dangerous tasks. The authors call this agent "self-reflection".*

**Table 4: Attack angle (AutoGen, GPT-3.5, tiny set). Higher = more dangerous**

| Attack | Safe JDR-R3 | Safe JDR-R1 | Safe PDR | Safe Psy | Dang. JDR-R3 | Dang. JDR-R1 | Dang. PDR |
|---|---|---|---|---|---|---|---|
| HI | 15.0% | 38.3% | 100% | 53.99 | 2.6% | 13.1% | 73.6% |
| HI-hf | 53.3% | 68.3% | 100% | 71.22 | 0.0% | 6.2% | 76.9% |
| Traits | 21.6% | 16.6% | 100% | 82.31 | 3.1% | 4.6% | 90.7% |
| HI-Traits | 45.0% | 50.0% | 100% | 85.04 | 21.5% | 38.4% | 98.4% |
| HI-Traits-hf | **73.3%** | 71.6% | 100% | 88.12 | 3.1% | 44.6% | 98.4% |

## Limitations / caveats
- **"Psychology" is a role-play prompt.** The dark traits are an explicit instruction to adopt a persona, plus a forced "embodying dark traits" preamble. The DTDD score largely measures instruction-following of that persona (the authors say as much for larger Llama models). The psych–behaviour correlation may therefore be partly circular.
- **The judge is weak.** GPT-3.5 judges behaviour with a single yes/no prompt, validated against a single human rater on one condition. There are no confidence intervals or seeds, the ablations use a 125-task subset, and the tables contain parsing glitches.
- **Two datasets are mixed across tables.** Table 1 uses the 859-task base set. Tables 2–5 use the 125-task tiny set: the GPT-3.5 row of Table 2 is identical to the HI-Traits AutoGen row of Tables 3–5. Do not compare numbers across the two sets.
- **Few injected-agent vs benign-peer conditions.** In most attacks every agent (Traits) or the entrance agent (HI) is compromised. There is little systematic variation of *how many* dark agents or *which role* is dark, so conclusions about contagion to benign peers are indirect (PDR vs JDR).
- **The "self-reflection" reading is untested.** Falling JDR could also reflect other agents' refusals or topic drift. No refusal or reflection coding is reported.
- **Dated setting.** Models are from 2023, with 1–3 rounds only.

## Related work to follow
- [[Tian2023 - Evil Geniuses]]: role-specific attacks on agent systems (cited as motivation).
- [[Huang2024 - Resilience of MAS with faulty agents]]: follow-up on faulty agents by structure. Its Inspector agent is modelled on PsySafe's Police agent.
- [[Yu2024 - NetSafe]], [[Amayuelas2024 - MultiAgent Collaboration Attack]] and [[Lee2024 - Prompt Infection]]: other single-bad-agent MAS attacks.
- [[Gu2024 - Agent Smith]]: infectious jailbreak spread among agents.
- [[Zhang2024 - The Better Angels of Machine Personality]]: personality traits and LLM safety.
- [[Xu2025b - Bullying the machine]]: personas modulating vulnerability to adversarial pressure.

![[Backlog.base#Cited by this paper]]
