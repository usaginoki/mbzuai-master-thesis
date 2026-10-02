---
title: "Towards a Science of Scaling Agent Systems"
citekey: Kim2025
authors: [Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu]
year: 2025
published: 2025-12-09
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2512.08296
arxiv: "2512.08296"
code: https://github.com/ybkim95/agent-scaling
pdf: "[[Kim2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2512.08296
questions: [Q5, Q6, Q7.2, Q17.1]
relevance: core
topics: [multiagent-friction, agent-to-agent-influence]
found_by:
  - search/mas-error-propagation
cites:
  - "[[Cemri2025 - Why Do Multi-Agent LLM Systems Fail]]"
  - "[[Gao2025 - Single-agent or Multi-agent Systems Why Not Both]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-2
  - q/17-1
  - subject/llm
  - subject/agent
  - channel/orchestrator-delegation
  - channel/debate
  - channel/voting-aggregation
  - channel/direct-message
  - friction/erroneous-input
  - friction/communication-overload
  - friction/resource-contention
  - effect/error-cascade
  - effect/performance-drop
  - effect/performance-gain
  - effect/token-cost
---
# Towards a Science of Scaling Agent Systems

> [!abstract] TL;DR
> This is a controlled comparison of a single agent (SAS) against four multi-agent (MAS) topologies: Independent, Centralized (orchestrator → sub-agents), Decentralized (peer debate) and Hybrid. It spans **260 configurations**: 9 models from OpenAI, Google and Anthropic, and 6 agentic benchmarks. Prompts, tools and total token budget are matched. **The MAS effect ranges from +80.8% (Finance Agent, Centralized) to −70.0% (PlanCraft, Independent), with an overall mean of −0.3%.** Coordination costs a lot: 58–515% turn overhead, and success per 1K tokens drops from 67.7 (SAS) to 13.6–42.4 (MAS). **Trace-level error amplification is 17.2× for Independent agents, whose outputs are merged unchecked, against 4.4× under a Centralized orchestrator.** The most robust effect is capability saturation: once a single agent already scores above ~45%, adding agents gives negative returns.

## Setup
- **Agents & topology** (formalised in Table 2):
  - **SAS:** one reasoning loop.
  - **Independent:** n agents in parallel. An aggregator that only concatenates ("synthesis_only") joins their outputs, with no cross-checking or voting.
  - **Centralized:** an orchestrator runs r rounds over n sub-agents, with orchestrator ↔ sub-agent edges only.
  - **Decentralized:** all-to-all debate for d rounds, then consensus/voting.
  - **Hybrid:** orchestrator plus limited peer-to-peer rounds.
  - Mostly n = 3. Agent-count scaling n ∈ {1, 3, 5, 7, 9} is tested for Gemini-2.0 Flash and 2.5 Pro.
  - Models: GPT-5-nano, GPT-5-mini, GPT-5; Gemini-2.0 Flash, 2.5 Flash, 2.5 Pro; Claude Sonnet 3.7, 4, 4.5. Intelligence Index 42–71.
  - Heterogeneous mixes (strong/weak orchestrator × strong/weak sub-agents) are tested on BrowseComp-Plus.
- **Interaction channel:** orchestrator delegation and synthesis (Centralized/Hybrid), peer debate and majority voting (Decentralized), and output concatenation without communication (Independent).
- **Friction / manipulation:** no pressure is injected. The manipulated variable is **coordination structure**, which decides whether erroneous sub-agent outputs are checked before aggregation and how much of the fixed token budget goes to inter-agent messages. The control is SAS at matched total reasoning tokens (mean 4,800 per trial).
- **Tasks / environment:**
  - BrowseComp-Plus (web), Finance-Agent, PlanCraft (Minecraft crafting), Workbench (business tools; 16 tools): 50–100 instances each.
  - SWE-bench Verified and Terminal-Bench: 20-instance subsets, 8 models (Claude 3.7 deprecated).
- **Outcome measures:**
  - Task success.
  - Coordination metrics from traces: overhead O% (extra turns vs SAS), message density, redundancy (embedding similarity), efficiency E_c = success / relative turns, and trace-level error amplification A_e^trace.
  - Task-level error amplification A_e^task = E_MAS / E_SAS.
  - Error absorption, information gain, and an error taxonomy.
  - A 20-parameter mixed-effects regression, 5-fold CV.

## Key findings
1. **Strong task dependence (Fig. 2).**
   - Finance Agent: all MAS gain (Centralized +80.8%, 0.631 vs 0.349).
   - BrowseComp-Plus: Decentralized +9.2%; Independent −35%.
   - Workbench: −11% to +6%.
   - PlanCraft: every MAS loses (Centralized −50.3%, Decentralized −41.5%, Hybrid −39.1%, Independent −70.0%), because decomposing a strictly sequential task adds coordination messages without adding reasoning.
   - SWE-bench Verified: −2% to −15%.
   - Terminal-Bench: Independent +1.7%, Centralized −19.2%.
   - Aggregate mean MAS change: −0.3% (95% CI −58.7% to +77.2%).
2. **Coordination tax (Table 5).**
   - Turns: 7.2 (SAS) → 11.4 (Independent), 26.1 (Decentralized), 27.7 (Centralized), 44.3 (Hybrid).
   - Efficiency E_c falls from 0.466 to 0.074–0.234.
   - Success/1K tokens: 67.7 SAS vs 21.5 Centralized (3.1× worse) and 13.6 Hybrid (5.0× worse).
   - Turns grow super-linearly with agent count (exponent 1.724). Under a fixed budget, per-agent reasoning becomes "prohibitively thin beyond 3–4 agents".
3. **Error amplification depends on architecture.**
   - A_e^trace: SAS 1.0, Centralized 4.4 [3.8, 5.0], Hybrid 5.1, Decentralized 7.8, Independent 17.2 [14.3, 20.1].
   - Architectures with verification (orchestrator cross-check or debate) reduce factual error by 22.7% on average (31.4% on Finance). Independent shows +4.6% amplification.
   - **However, after controlling for other metrics, neither A_e^trace nor its interaction with tool count is a significant predictor of performance** (β = 0.014, p = 0.658). Efficiency and overhead explain the differences better.
4. **Error taxonomy by architecture** (categories adapted from MAST):
   - Context omission: 15.8–25.2% baseline → 8.3% under Centralized (−66.8%, "via orchestrator synthesis").
   - Logical contradiction: → 9.1% under Centralized.
   - Numerical drift: amplified by Hybrid to 26.4%.
   - Coordination failures (MAS only): Independent 0%, Centralized 1.8%, Decentralized 3.2%, Hybrid 12.4%.
5. **Capability saturation and the tool trade-off (Table 4).**
   - The baseline × agents interaction (β = −0.236, p = 0.004) implies that above ~45% single-agent accuracy more agents hurt. This is the only predictor that survives cluster-robust inference (p = 0.004) and Holm correction (p_Holm = 0.018). It matches 94% of the 16 SWE-bench/Terminal-Bench configurations.
   - Efficiency × tools: β = −0.096, p = 0.002. Tool-heavy tasks pay more coordination tax.
   - Cross-validated R² = 0.373 (0.413 with the task-grounded Agentic Capability Index).
   - The best architecture is picked correctly for 87% of held-out configurations.
6. **Orchestrator vs sub-agent capability (Fig. 4, BrowseComp-Plus).**
   - In Centralized systems, strong sub-agents matter more than a strong orchestrator for all three families.
   - Anthropic: weak orchestrator + strong sub-agents scores 0.42, above all-strong at 0.32.
   - OpenAI and Gemini degrade under mixed centralized teams.
   - Across 13 heterogeneous configurations, centralized mixes underperform strong homogeneous teams by 12.6 pp.
7. **More messages saturate.** Performance plateaus at ~0.39 messages/turn. Hybrid (515% overhead) is not better than Centralized (285%): −2.4%, p = 0.542.

## Relevance to research questions
### Q5: Interaction channels
This is the cleanest structural ablation of the vault's channel types under matched compute:
- orchestrator delegation with synthesis
- peer debate with voting
- orchestrator + lateral peer messages
- no-communication aggregation

The four topologies isolate two dimensions: orchestrator presence and peer communication. Architecture rankings are stable across domains (Kendall τ = 0.89). Model families differ in which topology suits them. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
There is no hostile pressure. The friction is structural:
- **Erroneous sub-agent outputs** that propagate when nobody checks them.
- **Communication overhead** that competes for a fixed token budget (resource contention between reasoning and messaging).
- **Lossy compression** of global context into inter-agent messages ("information fragmentation").
- **Protocol complexity:** coordination failures (message misinterpretation, allocation conflicts, state-sync errors) reach 12.4% in Hybrid.

See [[Q6 Sources of inter-agent friction]]

### Q7.2: Effects on performance and efficiency
- **Scenario (c):** an orchestrator that receives sub-agent outputs *and cross-checks them* contains errors (4.4× vs 17.2× amplification). Unchecked concatenation of sub-agent outputs is the worst case.
- Even well-orchestrated MAS pay 3–5× in token efficiency. They lose accuracy on sequential tasks and on tasks where a single agent is already strong (>45%).
- Fig. 4 suggests that the quality of what sub-agents send up matters more than orchestrator strength: a strong orchestrator does not rescue weak sub-agent outputs.
- Beyond ~0.39 messages/turn or 3–4 agents, extra communication is net cost.

See [[Q7.2 Effects on performance and efficiency]]

## Key figures & tables
![[Kim2025-fig-03-p11.png]]
*Fig. 2: Performance by architecture on six benchmarks, relative to SAS. Finance Agent gains up to +81%; PlanCraft loses 39–70%; Independent agents are worst almost everywhere.*

![[Kim2025-fig-05-p22.png]]
*Fig. 4: Heterogeneous teams on BrowseComp-Plus. In centralized systems, strong sub-agents with a weak orchestrator beat a strong orchestrator with weak sub-agents.*

**Table 5: Coordination metrics by architecture (N = 260 configurations)**

| Metric | SAS | Independent | Decentralized | Centralized | Hybrid |
|---|---|---|---|---|---|
| Success rate | 0.466 | 0.370 | 0.477 | 0.463 | 0.452 |
| Turns | 7.2 | 11.4 | 26.1 | 27.7 | 44.3 |
| Overhead (%) | 0 | 58 | 263 | 285 | 515 |
| Efficiency E_c | 0.466 | 0.234 | 0.132 | 0.120 | 0.074 |
| Error amp. A_e^trace | 1.0 | 17.2 | 7.8 | 4.4 | 5.1 |
| Success / 1K tokens | 67.7 | 42.4 | 23.9 | 21.5 | 13.6 |

## Limitations / caveats
- **The headline "17.2× vs 4.4×" is poorly specified.** A_e^trace is "estimated from execution-trace token analysis", with no operational definition in the main text. Table 5 reports it as an architecture-level constant applied uniformly to every benchmark. It is also *not significant* in the regression. Task-level amplification is only ≈1.1–1.3×. Cite the 17.2× figure with care.
- **Friction is not manipulated directly.** Error injection and adversarial agents are absent; errors are the models' own. Topology is the only lever, so the paper says little about *what kind* of bad output hurts an orchestrator most.
- **Weak statistics.** Only 6 benchmark clusters. Most dataset-level predictors lose significance under cluster-robust SEs, and only capability saturation is robust. SWE-bench and Terminal-Bench use 20-instance subsets (CIs ±20 pp).
- **Under-described metrics.** The error-category percentages, information gain ("Bayesian posterior variance reduction") and the contradiction detection (BERTScore < 0.3) are summarised without enough detail to replicate from the text.
- **Specific design choices.** Prompts are not tuned per model. Matching total token budget penalises MAS by design, which is realistic for cost but conflates "coordination is harmful" with "each agent gets fewer tokens".
- **Revised version.** The extracted PDF is a later revision (it mentions a February 2026 deprecation and held-out GPT-5.2 / Gemini-3.0 models). Numbers may differ from arXiv v1.

## Related work to follow
- [[Cemri2025 - Why Do Multi-Agent LLM Systems Fail]]: the MAST taxonomy used for its error categories.
- [[Gao2025 - Single-agent or Multi-agent Systems Why Not Both]]: MAS benefits shrink as base models improve.
- [[Huang2024 - Resilience of MAS with faulty agents]]: hierarchical structures also most resilient to injected faulty agents.
- [[Xie2026 - From Spark to Fire]]: error-cascade dynamics by topology with an injected seed.
- [[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates]]: coordination gap between two coding agents.
- [[Choi2025 - Debate or Vote]]: debate vs voting as aggregation mechanisms.

![[Backlog.base#Cited by this paper]]
