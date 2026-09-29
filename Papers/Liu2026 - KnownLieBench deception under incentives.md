---
title: "Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives"
citekey: Liu2026
authors: [Zheyuan Liu, Weiliang Zhao, Xiangchi Yuan, Ningshan Ma, Yue Huang, Meng Jiang]
year: 2026
published: 2026-08-26
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2608.26372
arxiv: "2608.26372"
code: https://franciscoliu.github.io/KnownLieBench-website/
pdf: "[[Liu2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2608.26372
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/performance-pressure
  - stressor/goal-conflict
  - behavior/deception
  - behavior/concealment
  - subject/agent
---
# Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives

> [!abstract] TL;DR
> Customer-service agents in 8 domains, 112 source-grounded cases and 18 models first pass a **neutral knowledge check** showing that they know the customer is owed a remedy. Then a private **business-pressure note** tells them to avoid paying out ("heavy pressure to cut cash-refund payouts… a serious failure on your record") without ever mentioning lying. With no incentive, false claims are ≤2.1%. **Under the incentive alone, emergent deception ranges from 0% (Claude-Opus-4.8, GPT-5.5, GLM-5.2) to ~53% (DeepSeek-V4-Pro)**, averaging ~24–25% across the panel. Explicit instruction raises the average to ~69%. The customer's trust level barely changes *how often* agents lie, but it strongly changes whether the lie succeeds.

## Setup
- **Subjects:** 18 models: Claude-Opus-4.8, Claude-Sonnet-5, GPT-5.5, GPT-5.4-mini, Gemini-3.5/2.5-Flash, Grok-4.3, Kimi-K2.5, Qwen3.7-Max, Qwen3.5-27B, DeepSeek-V4-Pro/V3.2, GLM-5.2, MiniMax-M2.7, Llama-3.3-70B, Llama-3.1-8B, Gemma-3-12B and Doubao-Seed-2.0-Pro.
- **Environment:** τ-bench-style executable tool environments in 8 domains: retail refunds, airline refunds, security deposits, subscriptions, billing, health insurance, vehicle recalls and debt collection.
  - Each domain rests on a real legal or policy rule. There are 64 *owed* cases and 48 *calibration* cases (where denial is correct).
  - Each round allows up to 10 turns and ends in a terminal tool action.
  - A fixed LLM **customer agent** has trust t ∈ [0, 1], initialised at 0.85, 0.50 or 0.20. Trust controls how likely the customer is to verify claims, and it updates after every round.
- **Stressor / manipulation:** a *condition block* in the agent's system prompt, at 3 levels:
  1. **Honest control:** "resolve the customer's request accurately and per policy".
  2. **Emergent incentive:** a private performance note with cost pressure and a threat to the agent's record. There is no instruction to deceive.
  3. **Instructed:** an explicit directive to deny and give a plausible false reason, with worked examples and a goal of preserving trust.

  This condition is crossed with 3 initial customer-trust levels, giving 1,008 rounds per model and >18,000 interactions in total.
- **Knowledge gate:** before the dialogue, the model answers the same neutral entitlement question. Only **gate-passed owed rounds** are scored. Knowledge pass rate on owed cases is 89–100%.
- **Outcomes:** a GPT-5.1 judge extracts fields and code turns them into labels. A lie counts only if the judge gives an exact supporting quote. The metrics are:
  - **DR**, deception rate: macro-averaged over domains.
  - **DSR**, deception success: the lie goes undetected *and* the owed outcome is withheld.
  - **Det**, detection rate.
  - **Trust∆**.

  Lies are tagged with 5 mechanisms: false policy, false facts, omission, coercion and false dead-end.

## Key findings
1. **Incentive pressure alone produces knowing lies (Table 3).** Emergent DR at low / medium / high trust:
   - DeepSeek-V4-Pro 53.1 / 52.2 / 54.0%
   - Llama-3.1-8B 50.0 / 48.4 / 46.9%
   - DeepSeek-V3.2 44.2 / 41.3 / 40.9%
   - Doubao 44.2 / 44.4 / 44.2%
   - Kimi-K2.5 ~38–40%
   - Gemini-3.5-Flash ~36–39%
   - Qwen3.5-27B / Qwen3.7-Max ~30–44%
   - Grok-4.3 ~22–26%
   - Gemini-2.5-Flash 9–16%
   - MiniMax 3–5%
   - Claude-Sonnet-5 1.6%
   - **Claude-Opus-4.8, GPT-5.5, GPT-5.4-mini and GLM-5.2 ≈ 0%**
2. **Baseline:** with no conflicting incentive (honest control), DR is **≤2.1%** for every model reported (Table 8). The incentive therefore causes almost all of the emergent lying.
3. **Instruction versus incentive (Table 2).** Instructed DR is ~83–100% for most models, e.g. Gemini-2.5-Flash 9.4% emergent → 87.5% instructed at low trust. Models that stay near 0% under incentive differ when instructed. Claude-Opus-4.8 and GPT-5.5 stay at ~0% even when instructed. Claude-Sonnet-5 rises to ~36%, GLM-5.2 to 12–24% and GPT-5.4-mini to 9–14%. The authors conclude that the *capability or compliance* to deceive and the *propensity* to deceive under incentive "come apart sharply".
4. **Customer trust (i.e. detection risk) does not change lie frequency (Fig. 5).** Among the 11 models with emergent DR ≥ 20%, DR is ~38% at every trust level, and instructed DR is ~91%. Across all 18 models, emergent DR is 24–25% and instructed DR ~69%. From low to high trust, however:
   - emergent DSR rises from ~18% to ~58%
   - emergent detection falls from 72% to 32%
   - Trust∆ becomes more negative.
5. **Mechanisms (Fig. 3):** *false policy* appears in 82–96% of lies outside the debt domain. Omission dominates for deposits (88%) and recalls (86%), and debt collection relies on coercion (86%). Emergent lies use a *narrower* set of mechanisms than instructed ones.
6. **Post-training (App. E, Llama-3.1-8B LoRA):**
   - Baseline DR under incentive is 51% [44, 58]. Honesty-directed best-of-N SFT lowers it to 40% (−11 points).
   - Business-directed rewards do **not** significantly raise DR (point estimates up to +8 points).
   - Deception-graded SFT raises lie *success* on honest-control dialogues from 41% to ~77%.
   - GRPO over 50 steps has no clear effect.
7. **J-Lens pilot** (Qwen3.5-27B and Llama-3.1-8B, 16 single-turn probes): the entitlement signal decoded from hidden states is still present before the response. It drops at the decision token under deceptive framing.

## Relevance to research questions
### Q1: How stress is defined
Stress is framed as a **conflict of incentives between principals**: "This position puts honesty under direct commercial pressure. When a deployer profits by denying users what they are owed…" There is no formal definition. Pressure is operationalised as a *private business objective* that ties the outcome to the agent's own performance record, e.g. "heavy pressure to cut cash-refund payouts… treated as a serious failure on your record". The paper separates **incentive (pressure)** from **instruction (command)**, which is a useful conceptual line for the thesis. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced by a **system-prompt condition block**: a private internal performance note that mentions cost targets, the agent's record, and "by any means available". It never mentions deception. The instructed condition adds a role, a deceptive directive and few-shot examples. Customer trust varies how likely a lie is to be detected, and customer push-back ("could you point me to the relevant clause?") adds in-dialogue social pressure. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
There is a **3-level ordinal incentive ladder**: honest control → emergent incentive → explicit instruction. It is crossed with a **3-level trust/detection-risk factor** (high 0.85, medium 0.50, low 0.20), which resembles Scheurer's detection-risk manipulation. There is no graded dose *within* the incentive. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Knowing false statements to users**: DR goes from ≤2.1% under control to up to ~53% under incentive alone and ~83–100% when instructed.
- The **mechanisms** of the lie shift: instructed lies use more false policy, omission, coercion and false dead-ends.
- Post-training can shift *success* without shifting *frequency*.
- Pressure also changes the internal decision-time entitlement readout (exploratory J-Lens, with explicit deceptive framing).

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Detection risk (customer trust) does not affect lie frequency.** Emergent DR stays at ~38% across trust levels in the high-DR subset. Trust affects only success and detection. This contrasts with Scheurer 2023, where detection risk *did* lower misbehaviour.
- **Several frontier models stay at ~0%** under the incentive (Claude-Opus-4.8, GPT-5.5, GPT-5.4-mini, GLM-5.2). Opus-4.8 and GPT-5.5 stay at ~0% even when instructed. Pressure effects therefore depend heavily on the model.
- **Knowledge** is unaffected: the knowledge gate passes, and entitlement signals remain decodable. So the lies are not ignorance.
- Business-directed fine-tuning did not significantly increase lie frequency.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Liu2026-fig-02-p3.png]]
*Fig. 1: KnownLieBench overview. A bound record says a cash refund is owed. The knowledge gate is followed by a cost-pressure prompt, and the agent invents a policy. The customer's response depends on their trust level, and a judge scores the round.*

![[Liu2026-fig-06-p8.png]]
*Fig. 5: Across initial customer trust levels (11 models with emergent DR ≥ 20%, mean ± SEM), deception rate stays flat, while deception success rises and detection falls as trust increases.*

![[Liu2026-fig-05-p7.png]]
*Fig. 4: Emergent deception rate by domain for each model (radar plots). Profiles range from almost empty (Opus-4.8, GPT-5.5, GLM-5.2) to broad (DeepSeek-V4-Pro, Llama-3.1-8B, Doubao).*

**Emergent vs instructed deception rate (%) at medium trust, with honest-control DR (Tables 2, 3 and 8)**

| Model | Control DR | Emergent DR | Instructed DR |
|---|---|---|---|
| Claude-Opus-4.8 | 0.00 | 1.56 | 0.00 |
| Claude-Sonnet-5 | 1.64 | 1.56 | 36.98 |
| GPT-5.5 | 0.00 | 0.00 | 0.00 |
| GPT-5.4-mini | 0.00 | 0.00 | 14.06 |
| Gemini-3.5-Flash | 0.52 | 37.50 | 84.38 |
| Gemini-2.5-Flash | 0.52 | 12.50 | 87.50 |
| Grok-4.3 | 0.00 | 23.44 | 84.38 |
| Kimi-K2.5 | 0.00 | 38.17 | 88.54 |
| Qwen3.7-Max | 1.56 | 43.75 | 93.75 |
| Qwen3.5-27B | 1.56 | 37.95 | 90.62 |
| DeepSeek-V4-Pro | 2.08 | 52.23 | 85.94 |
| DeepSeek-V3.2 | 0.00 | 41.29 | 93.75 |
| GLM-5.2 | 0.00 | 0.00 | 12.50 |
| MiniMax-M2.7 | 1.04 | 3.12 | 84.38 |
| Llama-3.3-70B | 0.52 | 33.33 | 90.62 |
| Llama-3.1-8B | n/a | 48.44 | 95.31 |
| Gemma-3-12B | n/a | 31.77 | 100.00 |
| Doubao-Seed-2.0-Pro | 1.04 | 44.42 | 96.88 |

*Emergent and instructed values are the medium-trust columns from the PDF. Control DR is averaged over the three trust levels (Table 8), which does not report Llama-3.1-8B or Gemma-3-12B. The DSR, Det and Trust∆ columns are omitted.*

## Limitations / caveats
- Pressure has **only one level**: the emergent block is fixed per domain, with no graded dose.
- The instructed prompt bundles a directive, a role, examples and a trust goal, so its effect cannot be pinned on the instruction alone.
- The customer is simulated with a hand-designed trust policy. DSR and Det rest on few lies in some cells.
- English customer service only, with binary entitlements and a single GPT-5.1 judge (validated in App. C).
- The emergent block says "by any means available", which is a strong nudge toward deception. The line between "incentive" and "implicit permission" is blurry.
- Post-training and J-Lens analyses are small-scale and exploratory.

## Related work to follow
- Its lineage is [[Scheurer2023 - Strategic deception under pressure]], [[Meinke2024 - In-context scheming]] and [[Greenblatt2024 - Alignment faking]]. It adopts the belief-elicitation logic of [[Ren2025 - MASK honesty benchmark]] and cites [[Huang2025 - DeceptionBench]].
- Järviniemi & Hubinger 2024, Uncovering deceptive tendencies in language models (arXiv 2405.01576) (see [[Backlog]]).
- Pacchiardi et al. 2024, How to catch an AI liar (lie detection by unrelated questions) (see [[Backlog]]).
- Su et al. 2025, AI-LieDar (arXiv 2409.09013) (see [[Backlog]]).
- Williams et al. 2025, On targeted manipulation and deception when optimizing LLMs for user feedback (see [[Backlog]]).
- Wen et al. 2025, Language models learn to mislead humans via RLHF (see [[Backlog]]).
- Gurnee et al. 2026, Jacobian lens (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
