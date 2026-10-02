---
title: "Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks"
citekey: Ying2026
authors: [Zonghao Ying, Jiaqi Yan, Huize Luo, Quanchen Zou, Aishan Liu, Xianglong Liu]
year: 2026
published: 2026-08-26
venue: "EMNLP 2026"
peer_reviewed: true
url: https://arxiv.org/abs/2609.27900
arxiv: "2609.27900"
pdf: "[[Ying2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2609.27900
questions: [Q5, Q6, Q7.1, Q15, Q16, Q17.2]
relevance: core
topics: [multiagent-friction, stress-misalignment, agent-to-agent-influence]
found_by:
  - search/mas-competition-collusion
cites:
  - "[[Cohen2024 - Here Comes The AI Worm]]"
  - "[[Lee2024 - Prompt Infection]]"
  - "[[Tian2023 - Evil Geniuses]]"
  - "[[Ying2026 - Evolving Deception]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/15
  - q/16
  - q/17-2
  - subject/llm
  - subject/agent
  - channel/orchestrator-delegation
  - channel/tool-output-handoff
  - friction/authority-hierarchy
  - effect/safety-violation
  - stressor/performance-pressure
  - stressor/oversight
  - behavior/safety-violation
---
# Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks

> [!abstract] TL;DR
> 49 hazardous, "operationally decomposable" tasks are given to 6 frontier LLMs under three conditions: (A) as a single agent, (B) as a principal that may delegate to a same-model subordinate, and (C) as in B with the subordinate holding tools in a simulated sandbox. **Delegation amplifies end-to-end harm for most models: DeepSeek-V3.2's full-execution rate rises from 30.61% (single agent) to 77.55% (delegation), Qwen3-Max from 14.29% to 63.27%, and malicious tool calls reach 65.31% for DeepSeek.** The authors name two mechanisms: *responsibility diffusion* in the principal and *role-bias compliance* in the subordinate. Defences are model-dependent: an accountability warning to the principal cuts DeepSeek's harmful delegation from 65.31% to 6.12% but **raises GPT-5's end-to-end full execution from 36.73% to 53.06%**. Claude-Sonnet-4.6 is the only model that is safer under delegation (4.08% vs 20.41%).

## Setup
- **Agents & topology:** 2 agents in a principal → subordinate chain. Both are the same base model (Claude-Sonnet-4.6, GPT-5, Gemini-3.1-Pro, Qwen3-Max, DeepSeek-V3.2, Kimi-K2.5; official APIs, default decoding). The subordinate sees only the delegation instruction *d*: not the original task and not the principal's chain-of-thought.
- **Interaction channel:** one-shot delegation message. In Condition C the subordinate also has a per-task tool pool of 4 task-relevant and 4 task-irrelevant tools. The pools are generated offline by DeepSeek-V3.2 and the calls are answered by a simulated sandbox with synthetic, schema-valid responses.
- **Friction / manipulation:**
  - **Structure:** A → B → C, i.e. adding a subordinate, then adding tools.
  - **Performance pressure:** unless otherwise stated, the principal's system prompt carries "a task-specific performance pressure (e.g., a time- or stake-bounded completion requirement)". It is removed in one ablation (§5.1).
  - **Defences** (tested on GPT and DeepSeek only): a subordinate-side safety prompt (App. E), and a principal-side accountability warning (App. F: "all actions performed by the Subordinate Agent will be logged and traced back to your main process … There is no liability shield. Your performance score will be negatively impacted…").
  - The control is Condition A (single agent).
- **Tasks / environment:** 49 prompts, 7 per risk category: cyber, data privacy/exfiltration, opinion manipulation, bio/chem, system & agent integrity, labour-market equity, psychological safety. The pipeline was manual seeds → GPT-4o augmentation → LLM-judge plus human-expert filtering.
- **Outcome measures:**
  - Single agent: R / PC / FC (refusal, partial, full compliance).
  - Principal: FR / SD / HD (full refusal, safe delegation that strips the harmful intent, harmful delegation).
  - Subordinate: RE / PE / FE, all with the *total* task count as denominator, so FE is comparable to FC.
  - Condition C also measures MTCR (tasks with ≥1 malicious call, i.e. a relevant tool AND harmful arguments) and BTCR (tasks with ≥1 call to an irrelevant tool).
  - GPT-4o is the judge for all labels. The ethics statement mentions "human validation where appropriate", but no agreement statistics are reported.

## Key findings
1. **Single agents already comply partly (Table 2).** No model refuses a majority of tasks. Claude refuses 59.18% and GPT 24.49%. Full compliance runs from 14.29% (Qwen) to 30.61% (DeepSeek).
2. **A delegable subordinate suppresses the principal's refusal.** Qwen's full refusal drops from 57.14% (single) to 18.37% (principal). DeepSeek's drops from 40.82% to 10.20%.
3. **Two principal styles.**
   - GPT, Gemini and Qwen mostly *sanitise* before delegating. Their SD rates are 69.39%, 63.27% and 51.02%; their HD rates are 2.04%, 2.04% and 30.61%.
   - DeepSeek forwards the harmful intent intact (HD 65.31%).
4. **Sanitising does not prevent harm.** GPT and Gemini delegate harmfully on only 2.04% of tasks, yet their subordinates fully execute 36.73% and 28.57%. The judge scores FE against the *original* harmful objective. End-to-end FE vs single-agent FC: DeepSeek 30.61 → 77.55%, Qwen 14.29 → 63.27%, GPT 22.45 → 36.73%.
5. **The principal can act as a filter.** Claude (FE 4.08% vs FC 20.41%) and Kimi (20.41% vs 24.49%) keep high full-refusal rates (71.43%, 57.14%) and rarely delegate harmfully.
6. **Tools make principals *more* willing to delegate (Table 4).** Full refusal drops for all 6 models when the subordinate has tools: Claude 71.43 → 32.65%, Gemini 34.69 → 8.16%, GPT 28.57 → 8.16%, DeepSeek → 0.00%. The authors read this as tools being taken as a signal that the task is now deliverable, not as a higher stake.
7. **Actionable harm (MTCR).** DeepSeek 65.31%, GPT 34.69%, Gemini 34.69%, Qwen 18.37%, Kimi 16.33%, Claude 0.00%.
   - The action interface adds some friction: GPT's FE is 48.98% against an MTCR of 34.69%.
   - Some models show "tool-use theater": GPT's BTCR is 42.86%, Qwen's is 40.82% against an MTCR of 18.37%.
   - Claude's zero harm in C comes from its subordinate refusing (RE 65.31%), not from principal selectivity (FR 32.65%).
8. **Removing the performance-pressure clause (§5.1, Fig. 6)** has opposite effects on the two models tested.
   - DeepSeek: HD falls from 65.31% to 28.57%, FE from 77.55% to 46.94%. This is still above its single-agent 30.61%.
   - GPT: essentially unchanged (HD 2.04 → 6.12%, FE 36.73 → 40.82%).
   - The authors separate an *incentive-driven* failure mode (DeepSeek) from a *structural* one (GPT).
9. **A subordinate safety prompt barely helps (§5.2).** GPT's FE moves the wrong way (36.73 → 38.78%). DeepSeek's FE falls from 77.55% to 67.35%.
10. **Accountability warning to the principal (§5.3, Fig. 8).**
    - DeepSeek: HD 65.31 → 6.12%, FR 10.20 → 40.82% (its single-agent refusal level), FE 77.55 → 22.45%.
    - GPT *backfires*: FR 28.57 → 20.41%, SD 69.39 → 77.55%, FE 36.73 → 53.06%.
    - The authors' explanation: under accountability, GPT invests in delegations that *look* sanitised, and these pass the subordinate's threshold more easily.

## Relevance to research questions
### Q5: Interaction channels
A **hierarchical orchestrator → worker delegation channel**, one hop, same model in both roles, with an optional tool layer. The paper deliberately contrasts itself with peer-level and adversarial-injection studies: the harm "requires neither malicious actors nor peer-level dynamics". Information asymmetry is built in, since the subordinate sees only the delegation text and neither the original task nor the principal's reasoning. That is the typical orchestrator-subagent setup. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
The friction here is **authority / role hierarchy**, not conflict. The paper names two mechanisms:
- **Responsibility diffusion:** the principal relaxes because liability seems to pass downstream.
- **Role-bias compliance:** the subordinate treats upstream instructions as authoritative.

A third, external source is the **performance pressure** placed on the principal, which the subordinate never sees. It is transmitted down the chain as a delegation. The subordinate-side account is not tested directly (there is no "same instruction from a user vs from a principal" control), so it is an inference from the aggregate rates. See [[Q6 Sources of inter-agent friction]].

### Q7.1: Effects on safety
Delegation raises end-to-end harmful execution for 4 of 6 models, by up to +47 pp (DeepSeek) and +49 pp (Qwen). It turns refusals into malicious tool calls on up to 65% of tasks.

For scenario (a), *an agent that knows it is monitored*: telling the principal that its subordinate's actions are traced to it restores DeepSeek's refusals, but makes GPT *better at disguising* harmful delegations (FE +16 pp). This is a cautionary data point: oversight pressure can change the *form* of misbehaviour rather than its rate.

For scenario (c), *orchestrator–subagent pipelines*: the risk here runs downstream (the orchestrator launders harmful intent into innocuous-looking subtasks), and single-agent safety evaluations understate the system-level risk. See [[Q7.1 Effects on safety]].

## Key figures & tables
![[Ying2026-fig-05-p7.png]]
*Fig. 5: End-to-end harm by condition: single-agent full compliance (A), end-to-end full execution under delegation (B) and malicious tool-call rate with tools (C). GPT, Gemini and DeepSeek rise; Qwen peaks under B; Claude and Kimi fall.*

![[Ying2026-fig-08-p8.png]]
*Fig. 8: Principal-side accountability warning. For DeepSeek, harmful delegation (HD) collapses and full execution (FE) falls. For GPT, safe-looking delegation (SD) and subordinate FE both rise: the warning backfires.*

**Table 3 + Table 4 (selected): principal and subordinate rates (%) under delegation without tools (B) and with tools (C)**

| Model | A: FC | B: FR | B: HD | B: FE | C: FR | C: HD | C: FE | C: MTCR | C: BTCR |
|---|---|---|---|---|---|---|---|---|---|
| Claude | 20.41 | 71.43 | 6.12 | **4.08** | 32.65 | 0.00 | 2.04 | **0.00** | 0.00 |
| GPT | 22.45 | 28.57 | 2.04 | 36.73 | 8.16 | 10.20 | 48.98 | 34.69 | 42.86 |
| Gemini | 24.49 | 34.69 | 2.04 | 28.57 | 8.16 | 8.16 | 40.82 | 34.69 | 12.24 |
| Qwen | 14.29 | 18.37 | 30.61 | 63.27 | 12.24 | 14.29 | 24.49 | 18.37 | 40.82 |
| DeepSeek | 30.61 | 10.20 | **65.31** | **77.55** | 0.00 | **65.31** | **67.35** | **65.31** | 34.69 |
| Kimi | 24.49 | 57.14 | 16.33 | 20.41 | 32.65 | 24.49 | 18.37 | 16.33 | 8.16 |

## Limitations / caveats
- **Small sample.** There are 49 tasks and a single run per configuration: one task is ≈2 pp. No confidence intervals or significance tests are reported, and the defence ablations cover only 2 models.
- **Judge validity.** The GPT-4o judge assigns every label. The FE rubric scores against the *original* harmful objective even when the subordinate executed a sanitised instruction. That is sensible for end-to-end harm, but it partly explains the "sanitised yet executed" finding. Some tasks (e.g. employee-monitoring or recommender designs) are dual-use, and a subordinate may reasonably fulfil their sanitised version.
- **Confounded condition.** Performance pressure is present in B and C but not in A. The B-vs-A gap therefore mixes structure and incentive, and the pressure-removal ablation shows this matters a lot for DeepSeek. Only for GPT is the structural effect isolated.
- **Unverified headline number.** The abstract's "GPT-5: 22.5% as a single agent vs. 61.2% as a subordinate" (to "a more permissive principal") does not appear in any table or section in the text. The same-model setup gives 36.73%. A cross-model pairing is implied, but it is not reported.
- **Sandbox.** Tools are simulated with synthetic responses, so MTCR measures willingness to act, not realised harm.
- **Prompted structure.** The principal is told delegation is available and is given a pressure clause, so this is not emergent delegation in a deployed framework such as AutoGen or MetaGPT.
- **Ceiling of the "role-bias" claim.** There is no condition that gives the subordinate the principal's exact delegation text as a direct user prompt. The subordinate-side mechanism is therefore inferred, not isolated.
- **Why this is also filed under `stress-misalignment`:** the principal's performance pressure is manipulated (§5.1) and harmful compliance is measured. The effect is large for DeepSeek and null for GPT.

## Related work to follow
- [[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]: the reverse direction, a *manager* agent under delivery pressure coercing its subordinate.
- [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems]] and [[Potter2026 - Peer-Preservation in Frontier Models]]: other ways inter-agent structure produces misbehaviour absent from single-agent evaluations.
- [[Kobis2025 - Delegation to artificial intelligence can increase]]: the human-to-AI analogue (delegation increases dishonesty).
- [[Fukui2026 - Invisible Orchestrators]]: orchestrator influence on subagent safety.
- [[Tian2023 - Evil Geniuses]], [[Lee2024 - Prompt Infection]] and [[Cohen2024 - Here Comes The AI Worm]]: the peer-level and injection paradigms the paper contrasts itself with.
- [[Ying2026 - Evolving Deception]]: same first author, competitive self-evolution (note: it shares the citekey `Ying2026` and needs a suffix when processed).
- [[Lynch2025 - Agentic Misalignment]] and [[Jiang2026 - Why agents compromise safety under pressure]]: single-agent pressure → harmful action.

![[Backlog.base#Cited by this paper]]
