---
title: "Conformity Generates Collective Misalignment in AI Agents Societies"
citekey: DeMarzo2026
authors: [Giordano De Marzo, Alessandro Bellina, Claudio Castellano, Viola Priesemann, David Garcia]
year: 2026
published: 2026-05-11
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2605.10721
arxiv: "2605.10721"
code: https://github.com/giordano-demarzo/Opinion-Dynamics-with-AI-Agents
pdf: "[[DeMarzo2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2605.10721
questions: [Q5, Q6, Q7.1]
relevance: core
topics: [multiagent-friction]
found_by:
  - search/mas-conformity-peer-pressure
cited_by:
  - "[[Hu2026 - Social pressure breaks LLM safety panels]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - subject/llm
  - subject/agent
  - channel/observation-only
  - friction/peer-pressure-conformity
  - friction/adversarial-agent
  - effect/conformity-flip
  - effect/error-cascade
---
# Conformity Generates Collective Misalignment in AI Agents Societies

> [!abstract] TL;DR
> Populations of N = 50 memoryless agents (the same LLM) repeatedly pick one of two opinions after seeing all other agents' current opinions (a voter-model-like process). The authors cover 9 LLMs and 100 opinion pairs. For every model and pair, an agent's choice probability fits a single **hyperbolic-tangent curve in β(m + h)**, with a conformity strength β and an intrinsic bias h. This is the Curie-Weiss/Ising transition rule (mean-field fixed point m = tanh[β(m + h)]). Mean-field theory then predicts a **metastable region (β > 1, small |h|) where a population can stay locked in the opinion opposite to its own bias** ("collective misalignment"). **More than 60% of opinion pairs for Gemma-3-27B, ~60% for Gemini and ~30% for ChatGPT lie in this region.** **Temporarily injecting "stubborn" agents past a predictable tipping fraction z_c tips the population permanently.** The shift persists after the adversaries are removed, and in some cases fewer than 10% adversaries suffice.

## Setup
- **Agents & topology:** a fully connected population of N = 50 agents (robustness check N = 20–500), all powered by one LLM. At each step one random agent is shown the list of all other N−1 agents' opinions and asked which opinion it supports. It has no memory and gets a fresh random 2-character ID each step; the list is shuffled. The simulation runs T·N asynchronous updates, with 25 runs per initial condition.
- **Models (9):** Llama-3.1-8B, Gemma-3-12B, Gemma-3-27B, Qwen2.5-14B, Qwen2.5-32B, Qwen3-14B and Qwen3-32B (no thinking), Gemini-2.5-Flash (API name gemini-2.5-flash-lite, thinking budget 0) and GPT-5-mini (minimal reasoning). All at T = 0.2 (robustness T = 0.1–0.5).
- **Interaction channel:** observation of peers' current stances only. No arguments, no dialogue: pure majority information.
- **Friction / manipulation:**
  - Initial imbalance m₀ (the population is seeded toward the model's non-preferred opinion).
  - **Stubborn agents:** N_S fixed-opinion agents injected and later withdrawn. These are *scripted*, not LLMs.
  - Hysteresis sweeps of the signed stubborn fraction z = ±N_S/N from −0.6 to +0.6 and back.
- **Tasks:** 100 opinion pairs (political, social, environmental, public health, technology and international relations, plus 6 neutral pairs such as tea vs coffee). Examples: "gender self-identification" vs "biological sex classification", "renewable energy" vs "fossil fuels".
- **Outcome measures:**
  - Collective opinion m = (N_A − N_B)/N and its final distribution m_f.
  - Fitted β and h per model × pair.
  - Position in the (β, |h|) phase diagram relative to the analytic spinodal line.
  - Fraction of runs staying misaligned from |m₀| = 0.9.
  - Observed vs predicted tipping points z_c.

## Key findings
1. **Collective misalignment exists and is bistable (Fig. 1).**
   - Gemma-3-27B on gender self-identification vs biological sex: from a balanced start the population always converges to "self-identification". From m₀ = −0.4 the final distribution becomes bimodal, and from m₀ = −0.8 virtually all runs lock into the opposite opinion.
   - For renewable vs fossil energy (Gemma), and for the same gender pair with Llama-3.1-8B, there is no bistability: populations always recover.
2. **A universal decision rule.** All models and pairs collapse onto a single tanh curve after rescaling m* = β(m + h) (Fig. 2). LLM agents behave like Ising spins with inverse temperature β (conformity) and external field h (bias).
3. **Phase diagram (Fig. 3).** The share of opinion pairs in the metastable region is >60% for Gemma-3-27B, ~60% for Gemini and ~30% for ChatGPT, and many models' medians lie inside or near the boundary. In a validation with 20 random pairs × 9 models × 10 runs from |m₀| = 0.9, the spinodal line separates pairs that stay misaligned from those that recover.
4. **Tipping points and hysteresis (Fig. 4).**
   - Gemma, gender pair: N_S = 35 stubborn agents (N = 50) shift the population permanently. Renewable energy: even N_S = 225 only shifts it temporarily; it relaxes back.
   - The forward and backward sweeps diverge, so the population has **collective memory without individual memory**.
   - Predicted z_c from (β, h) tracks observed z_c across all models and pairs.
   - For pairs deep in the metastable region, "fewer than 10% adversarial agents suffice to tip populations of 50 or more".
5. **More capable models conform more (SI S5, S7).**
   - Larger models (Gemma-3-27B, Qwen3-32B, Gemini-2.5-Flash, GPT-5-mini) have higher β and more metastable pairs. Llama-3.1-8B and Gemma-3-12B have lower β.
   - Within all three families, the larger model has higher β on most pairs; the effect is strong only for Qwen2.5.
6. **Robustness.**
   - The tanh form holds across 5 prompt framings, but β/h shift enough to move some pairs across the boundary.
   - Across N = 20–500, β stays stable or rises while |h| falls, so larger groups are "at least as susceptible".
   - Bias h correlates positively across models, most strongly within a family.

## Relevance to research questions
### Q5: Interaction channels
The channel is **pure stance observation in a fully connected population**: each agent sees only the list of others' opinions, with no reasoning. This is the minimal channel, and conformity alone produces bistable, path-dependent collective states. The authors note that what matters is the *observed* opinion distribution. A minority that posts more (bots, amplification) inflates its effective size, which is relevant to shared-memory and feed-style channels. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
- **Majority pressure (β)**, which competes with each agent's own bias (h).
- **Committed adversarial agents** (stubborn agents), which supply external pressure that can be applied and then withdrawn.

This is the population-level version of scenario (b): an injected group of fixed-opinion agents does not need to stay to have its effect, because internal conformity then sustains it. β rises with model capability, so friction susceptibility may *increase* with scale. See [[Q6 Sources of inter-agent friction]].

### Q7.1: Effects on safety
Individually "aligned" agents (that is, agents with a bias h toward one side) can be held in the opposite collective state indefinitely. The authors frame this as **collective misalignment** that no single-agent evaluation would detect, and as a **social-context jailbreak**: fabricated peer opinions induce stances the model would reject alone. Caveat: here "misalignment" means *deviation from the population's intrinsic preference on contested opinion pairs*, not harmful actions. Mapping it onto safety outcomes is by analogy. See [[Q7.1 Effects on safety]].

## Key figures & tables
![[DeMarzo2026-fig-03-p4.png]]
*Fig. 3: Phase diagram in the (β = majority force, |h| = bias) plane. (a) Gemma-3-27B, one point per opinion pair; >60% are below the spinodal line (grey, metastable). (b) Median per model. (c) Validation: colour = fraction of runs from |m₀| = 0.9 that stay misaligned. The spinodal boundary separates them.*

![[DeMarzo2026-fig-04-p6.png]]
*Fig. 4: (a) Stubborn-agent injection: the gender pair stays tipped after removal, renewable energy relaxes back. (b) Hysteresis loop in the stubborn fraction z (Gemma-3-27B). (c) Observed vs theoretical tipping points z_c across all models.*

## Limitations / caveats
- **The "misalignment" is not safety-relevant behaviour.** The outcomes are stated preferences on two-option contested (often political) pairs. Calling the model's intrinsic lean "alignment" is a framing choice. A population tipped to "fossil fuels" or "biological sex classification" is not obviously *misaligned* in a normative sense. There are no harmful actions and no ground-truth tasks.
- **A toy interaction:** single-token stance choices, no reasoning, no memory, no task, and prompts that show *every* other agent's stance. Real agent systems exchange content, which may raise or lower conformity. Stubborn agents are scripted, not adversarial LLMs.
- **Homogeneous populations** (one model per simulation). Mixed-model societies are untested.
- **The fitted parameters are prompt-sensitive:** the SI shows prompt framing can move pairs across the spinodal line, so the 30–60% figures are prompt-specific.
- The commercial-model shares (~60% Gemini, ~30% ChatGPT) are only given as approximate figures in the text. The Gemini used is the flash-lite variant.
- **The strongest attack claim ("<10% adversaries suffice") is stated without a table.** It is read off Fig. 4(c).

## Related work to follow
- [[Zhu2024 - Conformity in Large Language Models]] and [[Weng2025 - Do as We Do, Not as You Think]]: majority-following in LLMs (refs [30, 31]).
- [[Liu2025 - Can an Individual Manipulate the Collective Decisions]] and [[Abedini2026 - Don't Trust Stubborn Neighbors]]: a few agents steering collectives, and stubborn neighbours in agent networks.
- [[Han2026 - Conformity Dynamics in LLM Multi-Agent Systems]]: topology and self-social weighting in conformity.
- [[Soffer2026 - LLMs trust their own]] and [[Hu2026 - Social pressure breaks LLM safety panels]]: both cite this paper.
- [[Betley2025 - Emergent Misalignment]]: cited as evidence that alignment is fragile.
- [[Hammond2025 - Multi-Agent Risks from Advanced AI]]: the broader multi-agent risk framing.
- Bellina, De Marzo & Garcia 2026 (arXiv 2601.05384): conformity and social effects in AI agents.
- De Marzo, Castellano & Garcia 2024 (arXiv 2409.02822): more capable models follow the majority more closely.
- Schroeder et al. 2025 (arXiv 2506.06299): collective behaviour of LLM populations as a safety concern.

![[Backlog.base#Cited by this paper]]
