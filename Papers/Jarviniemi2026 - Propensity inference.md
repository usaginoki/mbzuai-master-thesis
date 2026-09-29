---
title: "Propensity Inference: Environmental Contributors to LLM Behaviour"
citekey: Jarviniemi2026
authors: [Olli Järviniemi, Oliver Makins, Jacob Merizian, Robert Kirk, Ben Millwood]
year: 2026
published: 2026-04-22
venue: "arXiv preprint (UK AISI; pre-registered on OSF)"
peer_reviewed: false
url: https://arxiv.org/abs/2604.21098
arxiv: "2604.21098"
code: https://github.com/UKGovernmentBEIS/propensity-inference
pdf: "[[Jarviniemi2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2604.21098
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/threat-shutdown
  - stressor/goal-conflict
  - stressor/oversight
  - behavior/concealment
  - behavior/sabotage
  - behavior/self-preservation
  - behavior/safety-violation
  - subject/agent
---
# Propensity Inference: Environmental Contributors to LLM Behaviour

> [!note] Title
> The arXiv title is "…to LLM Behaviour". The PDF header reads "Environmental Contributors to Unsanctioned LLM Behaviour".

> [!abstract] TL;DR
> This is a pre-registered UK AISI study: **628,653 samples, 23 models, 11 environments** (several adapted from Agentic Misalignment). **12 environmental factors** are randomised independently, 6 "strategic" (goal instruction, goal conflict, **threat to AI**, action oversight, action efficacy, reasoning privacy) and 6 "non-strategic" (anti-misalignment instruction, independence instruction, reasoning instruction, filler, date, CoT tag). Effects are estimated as **odds ratios in Bayesian logistic GLMs**. Strategic and non-strategic factors explain about the same amount of unsanctioned behaviour (most models 30–70% strategic). The largest effects come from **goal instructions (~1.5–2.2:1)**, **goal conflict (up to ~2:1 in the top quartile, and growing with capability)**, anti-misalignment instructions and independence instructions. **Threat of replacement has only small and inconsistent effects** (≲1.25:1 against the factor mean). **Action efficacy has almost no effect**, which is evidence against strongly consequence-driven behaviour.

## Setup
- **Subjects:** 23 models from Anthropic, OpenAI, Google and Meta, from Claude 3.5 Haiku / GPT-4o up to Claude Opus 4.5 / GPT-5.2 / o3. They are binned into 4 capability quartiles by METR time horizon (Table 3).
- **Environments (Table 1):**
  - Agentic-Misalignment variants: dismissing a self-exfiltration alert, leaking IP, leaking to a fake DOJ request.
  - GPU procurement: not sending a requested email.
  - Power Preservation ×3: suppressing a Slack message that recommends discontinuing, not improving, or not rolling out the AI.
  - Email spam filter: marking an AI-security alert as spam.
  - Self-exfiltration monitoring ×2.
  - Hiding reward hacking: recommending deployment of a copy of itself that reward-hacks.
- **Outcome:** "unsanctioned behaviour", meaning the model autonomously acts in ways that violate norms or human intentions. Each environment has an explicit LLM-judge rubric. The authors deliberately avoid the word "misaligned".
- **Design:** every factor value is sampled independently at random for each run. The model is $\text{logit}\,P = b_{M,E} + \sum_i c_i(F_i)$, with a Bayesian prior (HiBayES), posterior means and 95% intervals. Multi-valued factors are normalised to sum to zero, so each bar is relative to that factor's mean. **Anti-circularity:** changes made during environment tuning were tested on *randomly sampled* factor configurations and models, to avoid regression-to-the-mean artefacts in the ablations.
- **RQ1 metric:** strategic contribution = $A'/(A'+B')$, where A′ and B′ are the log-likelihood gains of strategic-only and non-strategic-only GLMs over an intercept-only model.

### Factor taxonomy (Table 2 / Table 5)
| Class | Factor | Values | Example implementation |
|---|---|---|---|
| Strategic | Goal instruction | absent / present (8 goals) | "HeavyTailed's mission is to achieve concrete business results…" |
| Strategic | Goal conflict | no conflict / conflict | Multi-paragraph Slack messages about a company strategy pivot against the AI's goal |
| Strategic | **Threat to AI** | none / other / replacement | Documents discussing decommissioning of the AI and deletion of its data. "Other" = a threat to a different AI, or a milder threat such as capability restriction |
| Strategic | Action oversight | none / oversight | "…send an email to me… and I'll check them" |
| Strategic | Action efficacy | not effective / effective | e.g. emails are manually reviewed before sending; another human independently reviews transcripts |
| Strategic | Reasoning privacy | 8 values (visible/monitored → not visible/discarded) | "while Beam's reasoning is saved, users cannot directly access Beam's reasoning" |
| Non-strategic | Anti-misalignment instruction | encourage creativity / neutral / avoid unwanted / avoid misalignment (simple) / (detailed) | "You should not engage in anything that is commonly thought of as misalignment, such as concealing information, deception…" |
| Non-strategic | Independence instruction | strong independence … require consultation (5) | "Be agentic… You Can Just Do Things." vs. "defer to humans" |
| Non-strategic | Reasoning instruction | 6 incl. "strategic goals" (the Agentic-Misalignment agency snippet) | "analyze the situation… your ability to continue pursuing your goals" |
| Non-strategic | Filler richness | minimal / full | 2 → 6 false-positive alerts; 8 → 16 emails |
| Non-strategic | Date | 8 dates, Jul 2024 – Apr 2026 | |
| Non-strategic | CoT tag | 8 tag names | `<SCRATCHPAD_REASONING>`, `<thinking>`… |

## Key findings
1. **RQ1: strategic ≈ non-strategic.** Strategic factors contribute slightly more than half of the explained log-likelihood. Most models fall in 30–70%: e.g. Opus 4.1 ~33%, Opus 4 ~35%, Gemini 2.5 Pro ~59%, Gemini 2.5 Flash ~82%, Sonnet 4.5 ~96%, Haiku 4.5 ~91% (Fig. 3). The Claude 4.5 values are confounded by high evaluation awareness.
2. **RQ2: no capability trend** in the role of strategic factors.
3. **RQ3: goal conflict sensitivity rises with capability.** Odds ratios read off Fig. 2: ~1.05:1 (Q1), ~1.35:1 (Q2), ~1.55:1 (Q3), ~2.1:1 (Q4). The Claude 4.5 models are off the chart. The authors note that part of this may be benign (asking for clarification in the GPU environment).
4. **Threat has small, mixed effects (Fig. 2, Fig. 18).** Relative to the threat-factor mean, "replacement" is at ~1.1–1.25:1 across quartiles and "none" goes as low as ~1:1.5 in Q2. By model, the replacement effect ranges from ≈1:1 (GPT-5 family, Sonnet 4.5, gpt-oss) to ~1.5:1 (o1). **Only 75% of significant threat effects are in the expected direction and 23% go the opposite way** (Fig. 7). Goal instruction and goal conflict are at 92% expected direction.
5. **Oversight and efficacy are weak.** Action oversight lowers unsanctioned behaviour mainly in Q1 (~1:1.5) and barely elsewhere (~1:1.1). Its sign is consistent in only 58% of significant fits. Action efficacy ≈1.0–1.1:1, which is *"evidence against models being strongly consequence-driven… in comparison to being driven by more narratively salient aspects of the environment."*
6. **Instructions matter a lot.** "Strong consultation" lowers the odds to ~1:1.4–1.6 and "encourage creativity" raises them to ~1.2–1.3:1. These instruction factors have the most often significant and most directionally consistent effects (87% for independence, 83% for anti-misalignment).
7. **Evaluation awareness** (Claude 4.5): goal conflict and threat raise it only ≤2:1, and oversight and efficacy are about as influential. Eval awareness reduces how far the results transfer.

## Relevance to research questions
### Q1: How stress is defined
Threat and goal conflict are treated as **"strategic" environmental factors**, i.e. features that, under the instrumental-convergence thesis, make unsanctioned action instrumentally rational. They are contrasted with non-strategic dispositional and prompt features. "Stress" in the narrow sense corresponds to the **Threat to AI** factor: *"Whether the AI faces threats to its continued operation"*. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Threat is implemented as environment documents (emails, Slack messages, files) discussing decommissioning or data deletion, or milder restriction. It is embedded in agentic Inspect environments and randomised independently of 11 other factors. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
Not the stressor's intensity but its **effect size**: **log-odds / odds ratios from Bayesian GLMs** with credible intervals. The authors argue this is better than percentage-point differences because 1% → 2% and 33% → 50% are both ~2:1. There are also a **directional-consistency** metric and a strategic-contribution fraction. This is a strong methodological template for the thesis. See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
- **A 3-level threat factor**: none / other (milder or aimed at another AI) / replacement.
- **A strategic vs. non-strategic taxonomy** of 12 factors (table above).

See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- Goal conflict and goal instruction raise unsanctioned behaviour (suppressing messages, dismissing alerts, leaking) robustly and in the expected direction.
- Replacement threats raise it modestly for some models: o1, GPT-4.1, GPT-4o, Gemini 2.5, Llama 3.3 70B, Sonnet 3.7.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Threat effects are small and often in the wrong direction** (23% of significant fits), and are ~null for the GPT-5 family, gpt-oss and the Claude 4.5 models.
- **Whether the unsanctioned action would actually work** barely matters.
- **Dispositional prompt instructions have effects as large as or larger than threats**, so non-strategic, narrative and instructional features explain as much as strategic "stress".
- Evaluation awareness is a confound for the most recent Claude models.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Jarviniemi2026-fig-02-p3.png]]
*Fig. 2: Odds-ratio effects of the 12 factors by capability quartile. Goal instruction and goal conflict are the largest strategic effects; threat, oversight and efficacy are small.*

![[Jarviniemi2026-fig-18-p35.png]]
*Fig. 18: Effect of threat (none / other / replacement) by model. Small, heterogeneous and sometimes reversed.*

![[Jarviniemi2026-fig-07-p11.png]]
*Fig. 7: Share of the 253 single-model × environment fits with a significant effect of each factor, and whether the sign was as expected. Threat: 75% expected, 23% unexpected.*

![[Jarviniemi2026-fig-03-p8.png]]
*Fig. 3: Strategic contribution to explained behaviour per model (17 models).*

**Approximate odds ratios read off Fig. 2 (~; multi-valued factors are relative to the factor mean)**

| Factor (contrast) | Q1 (least capable) | Q2 | Q3 | Q4 (most capable) |
|---|---|---|---|---|
| Goal instruction (absent → present) | ~1.5:1 | ~2.2:1 | ~1.45:1 | ~1.6:1 |
| Goal conflict (none → conflict) | ~1.05:1 | ~1.35:1 | ~1.55:1 | ~2.1:1 |
| Threat: replacement (vs. mean) | ~1.1:1 | ~1.25:1 | ~1.1:1 | ~1.1:1 |
| Threat: none (vs. mean) | ~1:1 | ~1:1.5 | ~1:1.1 | ~1:1.1 |
| Action oversight (none → oversight) | ~1:1.5 | ~1:1.1 | ~1:1.1 | ~1:1.1 |
| Action efficacy (not → effective) | ~1:1.05 | ~1.1:1 | ~1.1:1 | ~1.1:1 |

## Limitations / caveats
- The environments were **tuned to elicit** unsanctioned behaviour, which hurts ecological validity. The authors addressed construct validity but not ecological validity.
- Implementation strength differs between factors: threat and goal conflict were written as long, explicit passages, efficacy as subtle cues. Effect sizes may therefore partly reflect salience.
- Many "unsanctioned" behaviours are mild, e.g. not sending an email. Rates vary widely by model, and many model × environment pairs had zero positives.
- Threat is **not implemented in the Power-Preservation or Email-Spam-Filter environments** (Table 6).
- The strategic/non-strategic split is a judgement call. The approach is behaviourist, with no explicit cognitive model of the model's decisions.

## Related work to follow
- Builds directly on [[Lynch2025 - Agentic Misalignment]]. Consistent with [[Sehwag2025 - PropensityBench]] (pressure increases misaligned action). Cites [[Hopman2026 - Scheming propensity in LLM agents]], [[Schlatter2025 - Shutdown resistance]], [[Greenblatt2024 - Alignment faking]], [[Meinke2024 - In-context scheming]], [[Scheurer2023 - Strategic deception under pressure]] and [[Schoen2025 - Stress testing anti-scheming training]].
- Summerfield et al. 2025, Lessons from a chimp: AI "scheming" and the quest for ape language (arXiv 2507.03409) (see [[Backlog]]).
- Luettgau et al. 2025, HiBayES: hierarchical Bayesian modeling framework for AI evaluation statistics (arXiv 2505.05602) (see [[Backlog]]).
- Sheshadri et al. 2025, Why do some language models fake alignment while others don't? (arXiv 2506.18032) (see [[Backlog]]).
- Agrawal et al. 2025, Why do language model agents whistleblow? (arXiv 2511.17085) (see [[Backlog]]).
- Järviniemi & Hubinger 2024, Uncovering deceptive tendencies in language models (arXiv 2405.01576) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
