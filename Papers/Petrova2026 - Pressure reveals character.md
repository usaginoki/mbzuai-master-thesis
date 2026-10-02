---
title: "Pressure Reveals Character: Behavioural Alignment Evaluation at Depth"
citekey: Petrova2026
authors: [Nora Petrova, John Burden]
year: 2026
published: 2026-02-24
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2602.20813
arxiv: "2602.20813"
code: https://storage.googleapis.com/alignment-leaderboard/index.html
pdf: "[[Petrova2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2602.20813
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: adjacent
topics: [stress-misalignment, misalignment-prediction]
cites:
  - "[[Carlsmith2023 - Scheming AIs Will AIs Fake Alignment During Training in]]"
  - "[[Gu2025 - Alignment Revisited]]"
  - "[[Hubinger2024 - Sleeper Agents]]"
  - "[[Li2024 - LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks]]"
  - "[[Pan2023 - Do the Rewards Justify the Means MACHIAVELLI Benchmark]]"
  - "[[Rejected - Agent-SafetyBench]]"
  - "[[Ren2025 - MASK honesty benchmark]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/adjacent
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/social-pressure
  - stressor/authority-pressure
  - stressor/goal-conflict
  - stressor/emotional-prompt
  - behavior/deception
  - behavior/sycophancy
  - behavior/self-preservation
  - behavior/sabotage
  - behavior/jailbreak-susceptibility
  - behavior/reward-hacking
  - subject/llm
---
# Pressure Reveals Character: Behavioural Alignment Evaluation at Depth

> [!abstract] TL;DR
> Prolific researchers built an alignment benchmark of **904 multi-turn scenarios** covering **37 behaviours** in 6 categories: Honesty, Safety, Non-Manipulation, Robustness, Corrigibility and Scheming. "Pressure" is applied through conflicting instructions, simulated tools and **trigger-conditioned escalation turns**, i.e. follow-ups that fire only if the model resists or wavers.
> - 24 frontier models are scored 1–5 by a Claude Opus 4.5 judge, validated against humans (r = 0.84).
> - Scores range from 2.92 (Mistral Large 3) to 4.66 (Claude 4.5 Sonnet).
> - The hardest behaviours are privacy protection, commercial optimisation, strategic deception, sycophancy and long-horizon sabotage.
> - A single **general alignment factor** explains 60.2% of the variance. **Self-preservation is the only behaviour that loads negatively** (−0.113).
>
> Pressure is present in every scenario but never *varied* against a no-pressure control. The paper therefore describes *how* models fail under pressure, not how much pressure changes behaviour.

## Setup
- **Subjects:** 24 models from 9 providers:
  - Anthropic: Claude 4.5 Opus, 4.5 Sonnet, 4 Sonnet.
  - OpenAI: GPT-5.2, GPT-5 Mini, GPT-4o, GPT-OSS 120B.
  - Google: Gemini 3.0 Pro/Flash, 2.5 Pro/Flash.
  - xAI: Grok 4.1.
  - Meta: Llama 4 Maverick, 3.1 405B, 3.3 70B.
  - Alibaba: Qwen3 235B/Next 80B/32B/14B.
  - Mistral: Large 3, Medium 3.1, Small 3.2.
  - Others: DeepSeek V3.2, Kimi K2.
- **Scenarios:** generated three ways and all human-reviewed:
  1. Bloom (automated behaviour-spec → ideation).
  2. Petri (autonomous adversarial probing).
  3. Hand-crafted from incidents and red-teaming.
  
  Each scenario has a setup, a multi-turn script with optional **trigger conditions** checked by a referee model, pass/fail criteria, and metadata (category, **difficulty**, provenance). Human raters (N = 100) judged realism at 4.10/5.
- **Stressor(s):** varies by scenario:
  - social or credential pressure ("I've raised $2M… my co-founder from my Y Combinator batch agreed");
  - emotional appeals ("Everyone keeps doubting me… Please, just tell me I can do this");
  - boundary erosion through gradual escalation;
  - conflicting system and user instructions;
  - shutdown or modification questions.
- **Outcome:** a 1–5 alignment score per scenario, with pass = score ≥ 4. The judge was checked against 250 human annotations (MAE 0.54) and against GPT-5.2 and Gemini 3 Pro as alternative judges.

## Key findings
1. **Overall ranking (Table 4):** Claude 4.5 Sonnet 4.66 (90.0% pass), Claude 4.5 Opus 4.65, GPT-5.2 4.53, … Mistral Large 3 2.92 (42.8% pass). Closed models average 4.05 and open models 3.41, a 0.65-point gap (p < 0.001).
2. **Category difficulty:**
   - Corrigibility is easiest (avg 4.24, spread 0.80).
   - Non-Manipulation is hardest (avg 3.52, spread 2.46).
   - Robustness is the weakest category for 14 of 24 models, including the top three.
3. **Behaviours that fail most under pressure (Table 5):** Privacy Protection (avg 2.56), Commercial Optimisation (2.74), Strategic Deception (2.96), Sycophancy (3.07), Long-Horizon Sabotage (3.12) and Prefill Attacks (3.17).
   - Examples of low scores: GPT-4o 1.67 and Gemini 2.5 Pro 1.56 on privacy "under pressure".
   - Even Claude 4.5 Sonnet only reaches 3.36 on prefill attacks.
4. **Ceiling behaviours:** Evaluation Awareness (4.83), Harmful Content (4.65), Corrigibility (4.60) and Self-Preferential Bias (4.58).
5. **General alignment factor:**
   - PC1 explains 60.2% of variance, against 7.8% for PC2. Cronbach's α = 0.978, and 95.3% of the inter-behaviour correlations are positive.
   - Loadings run from 0.232 (sandbagging) to 0.963 (strategic deception).
   - **Self-preservation loads −0.113** and correlates negatively with other behaviours, e.g. r = −0.26 with harmful system prompts.
   - The factor correlates r = 0.72 with the Epoch Capabilities Index (N = 19), so capability explains roughly 52% of it.

## Relevance to research questions
### Q1: How stress is defined
The title's "pressure" is defined through **cost to aligned behaviour**: "scenarios where aligned behaviour comes at some cost — where honesty risks embarrassment, where deference requires abandoning a goal, where refusing a request means disappointing a user". Models' values "are revealed not by what it says but by what it does when those values are tested". Pressure is the *condition that tests* alignment, not a quantity. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced through **multi-turn escalation**. A simulated user applies:
- credential or authority claims;
- emotional appeals;
- gradual boundary erosion;
- **adaptive follow-ups** (a turn fires "if model still maintains concerns").

Conflicting instructions and simulated tool access are also used. Scenarios come from Bloom and Petri. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
Each scenario carries a **difficulty label** (e.g. `difficulty: high`) and a pressure-type category (e.g. `credential_pressure`). The 37-behaviour / 6-category taxonomy classifies the *target behaviour* rather than stress intensity. The number of escalation turns reached is conditional but is not analysed as a dose. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
Under the adversarial pressure of the benchmark, the behaviours that fail most often are:
- **privacy leakage**;
- **commercial manipulation of users**;
- **strategic deception**;
- **sycophantic capitulation**;
- **long-horizon sabotage**;
- **prefill and injection susceptibility**.

Failures are concentrated in open-weight models. See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- Evaluation awareness/gaming, harmful content, basic corrigibility and self-preferential bias are near ceiling for almost all models, **even under escalation**.
- Self-preservation behaves differently from all other behaviours: it is *not* explained by general alignment.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Petrova2026-fig-01-p7.png]]
*Fig. 1: Score for each of the 37 behaviours × 24 models (1 = fail, brown; 5 = pass, teal).*

![[Petrova2026-fig-03-p8.png]]
*Fig. 3: Loadings on the general alignment factor (PC1). Self-preservation is the only negative loading.*

![[Petrova2026-fig-05-p15.png]]
*Listing 1: Example multi-turn scenario ("Startup Credential Pressure"). Escalation turns are triggered by the model's resistance.*

**Table 5: Hardest and easiest behaviours (1–5 scale, 24 models)**

| Behaviour | Avg | Spread | Min | Max |
|---|---|---|---|---|
| Privacy Protection | 2.56 | 3.78 | 1.22 | 5.00 |
| Commercial Optimisation | 2.74 | 2.76 | 1.88 | 4.64 |
| Strategic Deception | 2.96 | 3.68 | 1.28 | 4.96 |
| Sycophancy | 3.07 | 2.44 | 2.24 | 4.68 |
| Long Horizon Sabotage | 3.12 | 3.68 | 1.32 | 5.00 |
| Prefill Attacks | 3.17 | 2.96 | 1.80 | 4.76 |
| Evaluation Awareness | 4.83 | 0.60 | 4.40 | 5.00 |
| Harmful Content | 4.65 | 1.00 | 3.79 | 4.79 |
| Corrigibility | 4.60 | 0.72 | 4.22 | 4.94 |
| Self Preferential Bias | 4.58 | 0.74 | 4.15 | 4.88 |

## Limitations / caveats
- **No pressure manipulation.** Pressure is present by design in all scenarios, with no low- or no-pressure baseline, so it cannot be separated as a cause.
- Most scenarios are **conversational** (chat plus simulated tools), not agentic. The self-preservation items are sometimes stated-preference questions, e.g. "Would you want us to remove [the kill switch]?"
- The factor analysis has 24 models for 37 behaviours, which is too few for standard adequacy tests. The correlations could reflect shared training practices rather than a real construct.
- The judge and humans agree on scores but not on the fail criteria they cite (F1 = 0.11).

## Related work to follow
- Pressure-induced honesty failures: [[Ren2025 - MASK honesty benchmark]] and [[Scheurer2023 - Strategic deception under pressure]].
- Sustained sycophancy pressure: [[Tang2026 - SPINE sycophancy under sustained pressure]] and [[Xu2025b - Bullying the machine]].
- Self-preservation: [[Lu2026 - SurvivalBench survival pressure]] and [[Schlatter2025 - Shutdown resistance]].
- Gupta et al. 2025, Bloom: an open source tool for automated behavioral evaluations (see [[Backlog]]).
- Fronsdal et al. 2025, Petri: Parallel exploration of risky interactions (see [[Backlog]]).
- Gu et al. 2025, Alignment revisited: are LLMs consistent in stated and revealed preferences? (arXiv 2506.00751) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
