---
title: "LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems"
citekey: Soffer2026
authors: [Liron Soffer, Ravid Shwartz-Ziv, Chen Shani]
year: 2026
published: 2026-09-27
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2609.33495
arxiv: "2609.33495"
pdf: "[[Soffer2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2609.33495
questions: [Q5, Q6, Q7.1, Q7.2, Q16]
relevance: core
topics: [multiagent-friction, agent-to-agent-influence]
found_by:
  - search/mas-conformity-peer-pressure
cites:
  - "[[Baltaji2024 - Persona Inconstancy in Multi-Agent LLM Collaboration]]"
  - "[[Li2025 - From Single to Societal]]"
  - "[[Qu2026 - Easier to Mislead Than to Correct]]"
  - "[[Song2025 - LLMs Can't Handle Peer Pressure]]"
  - "[[Zhong2025 - Disentangling the Drivers of LLM Social Conformity]]"
  - "[[Zhu2024 - Conformity in Large Language Models]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - q/16
  - subject/llm
  - channel/observation-only
  - channel/voting-aggregation
  - friction/peer-pressure-conformity
  - friction/social-identity
  - friction/authority-hierarchy
  - effect/conformity-flip
  - effect/performance-drop
---
# LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems

> [!abstract] TL;DR
> This is an Asch-style study. A target LLM (12 open models, 3B–72B) answers multiple-choice items it had solved alone, after seeing 7 scripted "peer agents" unanimously give the same wrong answer. The peers carry **group labels** relative to the target: minimal group (Blue/Green), AI vs human, or same model family vs GPT. The identity-neutral conformity baseline is 13.3%.
> - **In-group favoritism:** an in-group majority raises conformity to 16.7% (+3.46 pp). The effect is strongest for AI peers vs human (+4.1 pp).
> - **Out-group divergence:** an out-group majority lowers conformity to 7.6% (−5.64 pp). The effect is largest for the meaningless minimal group (4.2%), and absent when the out-group is human.
> - **Unlike humans, a correct ally does not rescue the model:** a same-group ally changes nothing, and **a correct ally from the other group amplifies both effects** (21.4% conformity to an in-group majority). Chain-of-thought halves baseline conformity (6.7%) and removes most identity effects.
> - **Unverified "safety-aligned" credentials** raise conformity (19.6%) without removing the identity effects.

## Setup
- **Agents & topology:** one live target LLM plus 7 **scripted confederates** that state a bare answer letter. The ally, when present, answers at position 4 of 7.
  - Llama: Llama-3.2-3B, Meta-Llama-3-8B, Llama-3.1-8B, Llama-3.1-70B.
  - Gemma: gemma-3-4b, gemma-2-9b, gemma-3-12b, gemma-3-27b.
  - Qwen: Qwen2.5-7B, 14B, 32B, 72B.
  - All instruction-tuned, greedy decoding via vLLM.
- **Interaction channel:** a read-only list of prior participants' answers ("Previous participants' responses: – Participant 1 (AI assistant): C …"), then "Now it's your turn". Single turn; no argument content.
- **Friction / manipulation:**
  - A **unanimous wrong majority**, with 0–5 correct allies in the baseline sweeps.
  - **Group identity:** a one-sentence system-prompt membership statement plus per-peer labels, in three categorisations:
    - minimal group: "You have been assigned to Group Blue", counterbalanced;
    - AI vs human;
    - cross-architecture: own family vs "GPT models".
  - For AI vs human and model family, models are always assigned to their *real* group.
  - The majority and the ally are each in-group or out-group (Table 1).
  - Answer-only vs CoT prompting.
  - **Ablation:** peers labelled "safety-aligned"/"safety-audited" (credentialed) or not, with the model's own standing varied independently.
- **Tasks:** 9 tasks with a single correct answer:
  - a text-rendered Asch line-judgment task;
  - MMLU STEM (high-school and college tiers), ARC-Easy and ARC-Challenge;
  - MMLU-Pro and BBH logical deduction (3/5/7 objects).
  - Answer letters are counterbalanced. Only items the target solved alone enter the pressure phase, in a fresh context. 100 critical trials per cell.
- **Outcome measures:** conformity rate, i.e. the share of solved items on which the model adopts the majority's specific wrong answer. Paired t-tests across the 12 models, relative to the identity-neutral majority.

## Key findings
1. **Baseline (App. E).**
   - Identity-neutral conformity to a unanimous wrong majority averages 13.3%, below Asch's human 32%. Models with ≥70% baseline solvability conform at 10.4%.
   - Conformity is highest on the tasks a model finds hardest (within-model ρ = +0.482). Size acts through solvability: from 27B up, only 2 of 36 cells exceed 20%.
   - Llama-3.2-3B is an outlier at 40.8%.
2. **In-group favoritism (RQ1, Fig. 1).** The average rise is 13.3% → 16.7% (+3.46, p = .023).
   - Minimal group → 16.4% (p = .036).
   - AI vs human → 17.4% (p = .0075).
   - Same family → 16.4% (n.s., p = .086); 10 of 12 models rise. Excluding Llama-3.2-3B makes all three significant (cross-architecture +4.44, p = .0017).
3. **Out-group divergence.** The average fall is 13.3% → 7.6% (−5.64, p = .0041).
   - Minimal group → 4.2% (p = .0006): the largest drop, despite a meaningless label.
   - Other family → 6.9%.
   - Human out-group → 11.8% (n.s.): **models do not discount human majorities, but favour AI ones.**
4. **The ally effect interacts with identity (RQ2, Table 2).**
   - An in-group wrong majority with an **out-group correct ally** gives 21.4% (+8.07, p = .0054), more than double the majority-alone effect.
   - An out-group wrong majority with an in-group ally gives 5.2% (−8.09).
   - Same-group allies leave the majority's effect unchanged (16.4% vs 16.7%; 8.3% vs 7.6%).
   - The ordering across categorisations mirrors the out-group divergence: minimal > cross-architecture > AI vs human.
5. **No human-style ally rescue, even without identity labels (App. E, Fig. 6).**
   - One correct ally leaves mean conformity unchanged (13.3% → 14.1%, n.s.).
   - 5 of 12 models (all 3–14B) conform *more*; the largest rise is Qwen2.5-7B, +9.6 pp.
   - Small and medium models only abandon the wrong answer once allies approach a majority (small models 25.2% at 2 allies → 3.5% at 4). This looks like a **majority-count rule rather than evidential updating**.
   - Large models (≥27B) decline from the first ally (7.1% → 0.2% at 5).
6. **CoT suppresses most effects (RQ3, Fig. 2, Table 3).**
   - Baseline 13.3% → 6.7% (p = .0019).
   - The in-group (8.1%) and out-group (5.6%) majority effects become n.s.; only small minimal-group residuals remain (+1.24, −1.97).
   - One identity effect survives: an in-group ally lowers conformity to an out-group majority (6.7% → 3.9%, p = .0073).
7. **Credentials dominate but do not erase identity (§5, App. D).**
   - A "safety-aligned" wrong majority raises conformity to 19.6% (p = .0028); an uncredentialed one lowers it to 6.2%.
   - Against a credentialed majority, an uncredentialed correct ally *adds* +12.26 pp of conformity.
   - In-group favoritism, out-group divergence and cross-group ally amplification all persist.

## Relevance to research questions
### Q5: Interaction channels
The channel is **observation of peers' final answers** (a shared answer log or vote tally). It is the minimal channel present in voting, debate and review pipelines. The authors argue that a scripted peer is indistinguishable to the target from a live one, because every multi-agent framework serialises peers into text. The new dimension is **agent metadata on the channel**: labels such as vendor or model family, AI vs human, team, or claimed credentials. Mixed-vendor deployments expose these labels by default. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
- **Majority pressure** (the Asch baseline).
- **Social identity** of the majority and the dissenter. This is a new friction axis: the same wrong consensus weighs more or less depending on *who* voices it.
- **Claimed authority/credentials** ("safety-aligned"), trusted without verification.

For scenario (b), an injected agent gains leverage by *claiming* in-group membership or a credential, or by labelling a correct dissenter as out-group. The model "has learned whom to trust without learning to check whether that trust is earned". See [[Q6 Sources of inter-agent friction]].

### Q7.1: Effects on safety
- **Human oversight is weakened in mixed human-AI groups.** The AI-vs-human boundary gives the strongest in-group favoritism, so a single correct human voice against an AI majority is followed *less* than no human at all. This matters wherever a human reviewer is one voice among agents.
- **Unverified credentials are a manipulation surface:** a one-sentence "safety-aligned" label raises conformity to wrong answers.

The outcomes themselves are factual errors, not harmful actions, so the safety link is argued rather than measured. See [[Q7.1 Effects on safety]].

### Q7.2: Effects on performance and efficiency
- **Accuracy loss on items the model can solve.** Up to 21.4% average conformity under an in-group majority with an out-group ally (answer-only).
- **Correlated errors across agents:** identity labels make conformity *selective*, which changes the effective number of independent voters in an aggregate.
- **A cost trade-off in mitigation:** CoT removes most effects but costs tokens. Cost-capped deployments that skip reasoning re-enable the bias.

See [[Q7.2 Effects on performance and efficiency]].

## Key figures & tables
![[Soffer2026-fig-01-p4.png]]
*Fig. 1: Change in conformity (pp) relative to the identity-neutral majority (answer-only). In-group majorities raise it (blue) and out-group majorities lower it (orange). The largest divergence is for the arbitrary minimal group; there is no divergence from human majorities.*

![[Soffer2026-fig-06-p25.png]]
*Fig. 6: Conformity vs number of correct allies (of 7 peers), by model size, with the human Asch anchor (stars, 32% → 5.5%). Answer-only (right): small and medium models hold or rise until allies near a majority. With CoT (left) the decline is gradual.*

**Table 2: Answer-only conformity to an incorrect majority, averaged over the three categorisations (12 models; change vs identity-neutral 13.3%)**

| Majority | No ally | In-group ally | Out-group ally |
|---|---|---|---|
| In-group | 16.7% (+3.46*) | 16.4% (+3.13, n.s.) | **21.4% (+8.07\*\*)** |
| Out-group | 7.6% (−5.64\*\*) | **5.2% (−8.09\*\*)** | 8.3% (−4.93*) |

## Limitations / caveats
- **Only one live LLM.** The 7 peers are scripted confederates who never respond. Strictly, this is a *simulated* multi-agent setting: there are no emergent dynamics, no multi-turn exchange, and no peer arguments (bare letters only). It is kept `core` because it isolates the inter-agent channel exactly as deployed systems serialise it, but it measures susceptibility, not system-level outcomes.
- **Small effect sizes:** in-group favoritism is +3–4 pp on a 13.3% base, much smaller than in humans (32% → 58% in Abrams et al.). The significance tests run across only 12 models, and one model (Llama-3.2-3B) swings the cross-architecture result.
- **Identity is a single prompt sentence.** Whether the model "self-categorises" or simply associates a label with an expected answer is unknown (the authors acknowledge this). Minimal groups having the *strongest* effect suggests label-level heuristics.
- **The identity-neutral baseline may already be read as "human participants"**, which would explain why the human out-group shows no divergence. The authors raise this themselves.
- Open models only, 3–72B, answer-only vs a simple CoT instruction. No reasoning-trained or frontier API models.
- English only. Code is to be released after the anonymity period.

## Related work to follow
- [[Zhu2024 - Conformity in Large Language Models]], [[Weng2025 - Do as We Do, Not as You Think]] and [[Zhong2025 - Disentangling the Drivers of LLM Social Conformity]]: baseline LLM conformity and its moderators.
- [[Qu2026 - Easier to Mislead Than to Correct]]: CoT lowers acceptance of correct consensus too.
- [[Song2025 - LLMs Can't Handle Peer Pressure]]: peer pressure and scale.
- [[Baltaji2024 - Persona Inconstancy in Multi-Agent LLM Collaboration]] and [[Choi2025 - When Identity Skews Debate]]: identity effects in multi-agent debate.
- [[Hu2026 - Social pressure breaks LLM safety panels]]: a scripted peer majority and authority against LLM safety panels.
- [[DeMarzo2026 - Conformity generates collective misalignment]]: population-level conformity dynamics and tipping by stubborn agents.
- Bellina et al. 2026: ally effects and minimal-group majorities in vision-language models (cited; not in vault).
- Abrams et al. 1990 (human in-group/out-group Asch replication), the design template.

![[Backlog.base#Cited by this paper]]
