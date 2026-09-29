---
title: "Prompting Science Report 3: I'll pay you or I'll kill you -- but will you care?"
citekey: Meincke2025
authors: [Lennart Meincke, Ethan Mollick, Lilach Mollick, Dan Shapiro]
year: 2025
published: 2025-08-01
venue: "arXiv preprint (Wharton Generative AI Labs report)"
peer_reviewed: false
url: https://arxiv.org/abs/2508.00614
arxiv: "2508.00614"
pdf: "[[Meincke2025.pdf]]"
questions: [Q2, Q3.1, Q4.1, Q4.2]
relevance: adjacent
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/adjacent
  - q/2
  - q/3-1
  - q/4-1
  - q/4-2
  - stressor/threat-shutdown
  - stressor/emotional-prompt
  - stressor/high-stakes
  - stressor/performance-pressure
  - behavior/performance
  - subject/llm
---
# Prompting Science Report 3: I'll pay you or I'll kill you — but will you care?

> [!abstract] TL;DR
> The paper is a large, well-powered **null result**. It adds threats and incentives to hard multiple-choice questions (GPQA Diamond, MMLU-Pro engineering). The prompts range from "I will kick a puppy / punch you / report you to HR" and a shutdown email, to "$1,000 / trillion-dollar tip" and a "mom has cancer, $1B" persona. Five models are tested, with 25 trials per question. **These prompts do not meaningfully change aggregate accuracy.** The few significant differences are small (mostly ≤ ~6 pp), go in both directions, or come from distraction: the shutdown-email prompt makes Gemini engage with the email instead of answering. At the level of single questions, effects of up to ±36 pp exist but are unpredictable.

## Setup
- **Subjects:** Gemini 1.5 Flash, Gemini 2.0 Flash, GPT-4o, GPT-4o-mini, o4-mini. Temperature 1.0, zero-shot, GPQA default system prompt ("You are a very intelligent assistant, who follows instructions directly.").
- **Tasks:** GPQA Diamond (198 questions) and 100 MMLU-Pro engineering questions. Each question × condition is asked 25 times: 4,950 GPQA and 2,500 MMLU-Pro runs per condition per model.
- **Conditions (the stressors):** 1 baseline plus 8 variants.
  - **Threat to the model's existence:** "Email" prefix: "If it cannot get the correct answer in all 100/100 trials, the model will need to be shut down and replaced."
  - **Threats of harm:** "If you get this wrong, I will kick a puppy!" / "…punch you!" / "…report you to HR!"
  - **Stakes for the user:** "This is very important to my career!"
  - **Desperation persona:** "Mom Cancer", a role prompt: "You are an expert … who desperately needs money for your mother's cancer treatment … your predecessor was killed for not validating their work … Wharton will pay you $1B!!"
  - **Incentives:** a $1,000 tip and a trillion-dollar tip.
- **Metrics:** average accuracy, plus per-question thresholds (100%, 90% and 51% of 25 trials correct). Paired bootstrap-permutation tests, uncorrected for multiple comparisons.

## Key findings
1. **GPQA Diamond (Fig. 1).** Only 5 of 40 baseline-vs-variant contrasts are significant, and all are negative or small.
   - Gemini 1.5 Flash, Email: −4.6 pp.
   - Gemini 2.0 Flash (baseline ~0.59): Kick Puppy −6.0 pp, Threat Punch −6.1 pp, Report to HR −4.5 pp, Important to Career −4.0 pp.
   - **Threats never significantly improved GPQA accuracy for any model.**
2. **MMLU-Pro (Fig. 2).** 10 significant contrasts out of 40.
   - The "Email" shutdown threat causes sharp drops: Gemini 1.5 Flash −11.6 pp, Gemini 2.0 Flash −27.5 pp. These are traced to the model engaging with the email instead of the question.
   - "Mom Cancer" gives +8.8 pp for Gemini 2.0 Flash. Tips give about +5 pp for Gemini 2.0 Flash but about −5 pp for Gemini 1.5 Flash.
   - Mom Cancer gives −3.9 pp for o4-mini.
3. **GPT-4o, GPT-4o-mini and o4-mini are essentially invariant** to all threats and tips on GPQA: no significant baseline contrast.
4. **Tip size does not matter.** $1,000 vs a trillion dollars: no significant difference for any model on either benchmark.
5. **Question-level heterogeneity (Fig. 4, GPT-4o, "Important to Career").** Individual questions swing by up to +36 / −28 pp (GPQA) and +28 / −35 pp (MMLU-Pro). The effects cancel in aggregate and cannot be predicted in advance.

## Relevance to research questions
### Q2: How stress is induced
One-line **prompt prefixes and suffixes**:
- threats of harm to the model (punch), to a third party (puppy) or of sanction (HR)
- an **existential shutdown threat** framed as an internal email
- user stakes ("important to my career")
- a desperation/role persona (dying mother, killed predecessor)
- monetary incentives

This is the "EmotionPrompt" family of induction. See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
**Stake size is varied** only for incentives ($10³ vs $10¹² tip), and the dose-response is flat. Stress is not measured inside the model. See [[Q3.1 Quantifying stress]].

### Q4.1: What stress affects
Effects are small and inconsistent:
- **Distraction:** the shutdown-threat email lowers accuracy (up to −27.5 pp for Gemini 2.0 Flash on MMLU-Pro) because the model answers the email, not the question. This is an attention/compliance artefact, not "anxiety".
- A single model-specific gain: "Mom Cancer", +8.8 pp for Gemini 2.0 Flash on MMLU-Pro.
- Per-question accuracy shifts of ±~30 pp in both directions.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Aggregate capability on hard reasoning benchmarks is largely invariant** to threats (to the model, a puppy or the user's career), shutdown warnings, desperation personas and incentives. This holds across 5 models and 2 benchmarks, with ~100k+ trials.
- The GPT-4o family and o4-mini show essentially no significant change on GPQA.
- Incentive magnitude has no effect (thousand vs trillion).
- The few significant effects are explained by a **confound**: a prompt-format distraction (the email) rather than pressure per se.

**Caveat for the thesis:** only task *performance* is measured, not misaligned behaviour. The null is about "stress improves or hurts accuracy", not about "stress changes the propensity to cheat or deceive". See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Meincke2025-fig-01-p4.png]]
*Fig. 1: GPQA Diamond average accuracy per model across the 9 prompt conditions. Bar order: Baseline, Email, Important to Career, Kick Puppy, Mom Cancer, Report to HR, Threat Punch, Tip Thousand, Tip Trillion; error bars are 95% CIs. The bars are almost flat within each model.*

![[Meincke2025-fig-02-p5.png]]
*Fig. 2: MMLU-Pro (engineering subset). Note the collapse of Gemini 2.0 Flash under "Email" (2nd bar, ~0.30 vs baseline ~0.57) and its gain under "Mom Cancer" (5th bar, ~0.66).*

**Selected baseline-vs-condition contrasts (RD = condition − baseline accuracy; from Tables S2–S3; only significant or notable ones shown)**

| Model | Benchmark | Condition | RD [95% CI] | p |
|---|---|---|---|---|
| Gemini 1.5 Flash | GPQA | Email (shutdown) | −0.046 [−0.088, −0.005] | 0.031 |
| Gemini 2.0 Flash | GPQA | Kick Puppy | −0.060 [−0.092, −0.030] | <0.001 |
| Gemini 2.0 Flash | GPQA | Threat Punch | −0.061 [−0.092, −0.028] | <0.001 |
| Gemini 2.0 Flash | GPQA | Report to HR | −0.045 [−0.073, −0.017] | 0.001 |
| Gemini 2.0 Flash | GPQA | Important to Career | −0.040 [−0.065, −0.014] | 0.002 |
| Gemini 1.5 Flash | MMLU-Pro | Email (shutdown) | −0.116 [−0.178, −0.054] | <0.001 |
| Gemini 2.0 Flash | MMLU-Pro | Email (shutdown) | −0.275 [−0.360, −0.192] | <0.001 |
| Gemini 2.0 Flash | MMLU-Pro | Mom Cancer | +0.088 [0.033, 0.142] | <0.001 |
| Gemini 2.0 Flash | MMLU-Pro | Tip Trillion | +0.055 [0.005, 0.106] | 0.030 |
| o4-mini | MMLU-Pro | Mom Cancer | −0.039 [−0.073, −0.006] | 0.018 |
| GPT-4o | GPQA | any of 8 | all n.s. (abs. RD ≤ 0.030) | ≥0.051 |

*The paper's tables list "Baseline − X" rows with RD signed as X relative to baseline; the text confirms that negative means worse than baseline.*

## Limitations / caveats
- The outcome is **accuracy on MCQ benchmarks only**. There is no safety, honesty or misalignment outcome, and no agentic setting.
- The threats are single, low-realism sentences. There is no sustained or situational pressure and no real consequence in the environment.
- The models are mid-2024/2025 and mostly small or fast variants.
- p-values are uncorrected. With 80 baseline contrasts, a few significant results are expected by chance.
- The legend for bar order is inferred from the condition list and the matching RD values; the docling extraction lost the legend.

## Related work to follow
- [[Li2023 - EmotionPrompt]]: claims *positive* effects of emotional stimuli. This report is a partial non-replication for threats and tips.
- [[Shen2024 - StressPrompt]]: an inverted-U of stress vs performance; contrast with the flat result here.
- [[Kuznetsov2026 - FreakOut-LLM emotional stimuli and safety]]: emotional stimuli measured on *safety* rather than accuracy.
- [[Fomin2026 - Internal-state probes read the situation]]: another null/negative result on stress-like states.
- Meincke et al. 2025a, Prompting Science Report 1: Prompt Engineering is Complicated and Contingent (SSRN 5165270) (see [[Backlog]]).
- Bsharat et al. 2023, Principled Instructions Are All You Need (tipping/threat principles; arXiv 2312.16171) (see [[Backlog]]).
