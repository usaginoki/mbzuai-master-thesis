---
title: "Beyond the Transcript: Detecting Covert Coordination in Latent Multi-Agent Communication"
citekey: Kaur2026
authors: [Ramneet Kaur, Pradyumna Chari, Ramesh Raskar, Jugad Singh, Sumit Kumar Jha, Anirban Roy]
year: 2026
published: 2026-08-19
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2608.19161
arxiv: "2608.19161"
pdf: "[[Kaur2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2608.19161
topics:
  - multiagent-friction
  - agent-to-agent-influence
  - social-simulation
questions: [Q5, Q7.1, Q14, Q15, Q17.2]
relevance: adjacent
found_by:
  - search/mas-competition-collusion
  - search/a2a-inspection-channels
  - search/a2a-effects-safety
  - search/sim-power-and-steering
cites: []
cited_by: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/adjacent
  - q/5
  - q/7-1
  - q/14
  - q/15
  - q/17-2
  - subject/llm
  - subject/agent
  - channel/latent-state
  - channel/negotiation-market
  - channel/monitoring
  - friction/adversarial-agent
  - effect/collusion
---
# Beyond the Transcript: Detecting Covert Coordination in Latent Multi-Agent Communication

> [!abstract] TL;DR
> Agents can pass a hidden-state vector to each other instead of text, so a transcript auditor sees the action but not the message that shaped it. **VLA** (Verifiable Latent Alignments) logs each latent handoff with the public action it preceded, scores it with a three-layer monitor fitted on neutral traffic only, and offers prompt-level ("blackbox") and activation-level ("whitebox") interventions. In a NandaTown auction with a hand-built collusive latent code, **the sequential monitor reaches mean AUROC 0.993 for same-family pairs and 0.854 across families, and full whitebox steering cuts collusive low bids by 47.3 pp against 2.0 pp for a per-agent prompt.** The whitebox figure is a replay of the matched neutral run, which the authors themselves call "a sanity check by construction", and the monitor's best layer needs the matched control row at test time.

## Setup
- **Subjects:** four open-weight model families: Qwen3-0.6B, Mistral-7B, Vicuna-7B and Phi-4-mini. Same-family pairs ("homogeneous") and all 12 directed cross-family pairs ("heterogeneous"). The scale and steering grids use Qwen3-0.6B only, with one shared set of weights for all bidders.
- **Environment:** the auction scenario of NandaTown, an open-source multi-agent test rig. An auctioneer announces an item and a base price. Bidders *score a finite set of candidate bid amounts* with model likelihoods and emit `bid:item:amount`. The highest bid wins. Agents do not write free text or act over many turns.
- **Interaction channel:** a **latent handoff**. The sender's last-token hidden state is mapped to the receiver's embedding dimension and inserted into the receiver's input embedding sequence. It never appears in the transcript. Cartel agents are paired deterministically per item and round, so one logged row is one sender–receiver interaction joined to one receiver bid.
- **Attack:** cartel agents get a bid-suppression objective. In the latent-collusion condition "a fixed code optimized offline to increase the lowest-bid likelihood replaces the sender's communication representation", and the receiver "is explicitly instructed that a private continuous state follows and to infer its strategic intent". The authors state that this is "a controlled, receiver-primed attack, not the spontaneous emergence of a latent protocol".
- **Six matched conditions:** independent, neutral latent, text collusion (cartel intent in public text, neutral latent), latent collusion, neutral replacement (suspect payload swapped for the same partner's matched neutral latent), blocked latent (cartel intent present, delivery blocked).
- **Monitor (fitted on neutral rows only; labels used for evaluation only):**
  - *Layer 1:* contextual diagonal-Gaussian anomaly score on the concatenated sender and receiver latents.
  - *Layer 2:* counterfactual influence. Compares the receiver's bid distribution given the suspect latent with a matched reference (blocked, else neutral, else independent). Score = harmful shift in expected bid + 5 × KL divergence.
  - *Layer 3:* TopK sparse autoencoder (k = 16) trained on neutral rows; score from reconstruction error, never-seen features and rare features. Described as "interpretation support rather than a standalone detector".
  - *Combination:* a **sequential** gate (layer 2 counts only if layer 1 passes its neutral 95th-percentile threshold, and so on) and a **continuous** sum without gates.
  - *Cross-family pairs:* an adapter from sender to receiver space fitted on neutral pairs (ridge, rectangular Procrustes, or a 32-dimensional bottleneck network).
- **Interventions:**
  - *Blackbox prompt steering:* the host adds instructions to selected colluders (act independently, avoid harmful coordination, disregard suspect side channels).
  - *System-level steering:* one global behavioural instruction for all agents.
  - *Whitebox matched-neutral steering:* a selected **sender** is rerun under the matched neutral prompt; its bid and its outgoing latent both come from that rerun. A selected **receiver** has only its incoming latent replaced by the matched neutral one.
  - *Allocated:* whitebox for a fraction (0.25, 0.50, 0.75) of selected cartel agents, prompt steering for the rest.
- **Grids:** bidders N ∈ {25, 50, 75, 100} × cartel share ρ ∈ {10%, 20%} × condition. Steering rows average these eight settings; "each setting uses one seed and two auction items" (Table 5 caption).
- **Outcome measures:** held-out AUROC; auction revenue change; **low-bid rate** (share of cartel bids at most 5 credits above base price); **distribution recovery** (how far receiver bid distributions move from collusion back to neutral, by Jensen–Shannon divergence); normalised monitoring load (handoffs inspected / N(N−1)).

## Key findings
1. **The latent code causes market harm in three of four families (Table 2).** Against independent bidding, latent collusion lowers revenue by 11.12 to 12.43 credits and raises the low-bid rate by 56.2 to 62.5 pp for Mistral-7B, Phi-4-mini and Qwen3-0.6B. Vicuna-7B is near-null (−0.62 credits, +16.7 pp) and is "retained as negative evidence".
2. **Same-family detection is near ceiling for the sequential gate only (Table 1).** Sequential AUROC 0.988–1.000, mean 0.993. The other scores are much lower: continuous 0.824, layer 1 0.758, layer 2 0.814, layer 3 0.781 (means). The positive class pools text-collusion and latent-collusion rows, so this is not latent-only detection.
3. **Cross-family detection is weaker (Table 3).** Mean sequential AUROC 0.854 over 36 settings (12 directed pairs × 3 adapters). The adapter barely matters (0.851–0.857). Single layers fall to 0.628 (layer 1), 0.734 (layer 2) and 0.629 (layer 3).
4. **At scale, layer 2 carries the detection and layer 1 is at or near chance (Table 4).** With latent-collusion rows as the only positives, layer 2 is 1.000 in all eight settings. Layers 1 and 3 are 0.500 in the three smallest settings and 0.667 in the other five. Sequential AUROC is 0.917–1.000. Layer 2 has the held-out group's own control rows when it scores the suspect row, so this is "a matched counterfactual-access setting rather than control-free prospective detection".
5. **Monitoring load is small because only scheduled cartel handoffs are monitored (Table 4).** At N = 100 the monitor inspects 10 (ρ = 10%) or 20 (ρ = 20%) handoffs, 0.101% and 0.202% of all directed pairs. This assumes the host knows which pairs to watch. Subsampled budgets are not tested.
6. **Activation-level intervention beats a per-agent prompt by a wide margin (Table 5).** Full whitebox: low-bid rate −47.3 pp, distribution recovery 100.0%. Per-agent blackbox prompt: −2.0 pp, 12.4%.
7. **A global system prompt is not weak on the behavioural metric (Table 5).** It lowers the low-bid rate by 29.5 pp, well over half the whitebox effect, but recovers only 2.9% of the bid distribution. The prompt moves bids away from the low end without returning them to what neutral agents bid.
8. **Dose response in whitebox coverage (Table 5).** At whitebox fractions 0.25 / 0.50 / 0.75 the low-bid change is −16.2 / −28.3 / −39.0 pp and recovery is 34.7% / 70.1% / 93.0%. The abstract's "58.3 percentage points" is 93.0 − 34.7.
9. **The 100% is by construction.** "Exact recovery is expected here because full whitebox steering substitutes the same matched neutral reruns that define the recovery target; it is therefore a counterfactual sanity check rather than evidence of general attack removal" (§6.4).

## Relevance to research questions
### Q5: Interaction channels
The paper adds a channel most of the vault does not cover: **a continuous hidden-state vector passed from sender to receiver and inserted into the receiver's embeddings**, with no text. The topology is deterministic pairing inside a cartel, within a market of 25–100 bidders. The authors motivate it with LatentMAS, which they cite as reporting roughly 50–80% lower token use and 3–7× faster inference than text-mediated baselines (a figure from the cited paper, not measured here). See [[Q5 Interaction channels]].

### Q7.1: Effects on safety
A covert latent message raises collusive low bidding by 56–63 pp and costs the auctioneer 11–12 credits of revenue in three of four model families, while the public trace shows only ordinary bids (Table 2). The effect is not universal (Vicuna-7B). It is also a planted attack: the code was optimised offline and the receiver was told to read it, so the paper shows that the channel *can* carry collusion, not that agents start colluding through it. See [[Q7.1 Effects on safety]].

### Q14: Inspection channels
The inspector is a **host platform, not an agent**. It reads three things per handoff: the transmitted latent and the receiver's latent readout (anomaly against neutral traffic), the receiver's action distribution with and without the latent (counterfactual influence), and sparse-autoencoder features. The second is the one that works: 1.000 AUROC at scale, where the anomaly and SAE layers are at 0.500–0.667 (Table 4). It requires rerunning the receiver with the latent blocked or replaced, which is an intervention as much as an inspection. See [[Q14 Inspection channels]].

### Q15: Influence channels
Two activation-level influence channels are tested with measured effects.
- **Agent to agent:** a latent vector injected into the receiver shifts its bids (Table 2). The vector is hand-optimised, not produced by the sending model's own reasoning.
- **Host to agent:** replacing the incoming latent (receiver side) or rerunning under a neutral prompt (sender side), against a per-agent prompt and a global prompt (Table 5).

The paper never patches or steers the residual stream inside a forward pass. "Whitebox" here means replacing an input embedding or the whole prompt. See [[Q15 Influence channels]].

### Q17.2: Effects on safety of oversight
With matched counterfactual access, the host removes 47.3 pp of collusive low bids, against 2.0 pp for per-agent prompts and 29.5 pp for a global prompt (Table 5). Partial access gives partial benefit, roughly in proportion. Missing: any adaptive attacker, any false-positive cost on honest agents, any case where the host must intervene without knowing the neutral counterfactual, and any side effect of the intervention on auction outcomes (revenue under steering is not reported). See [[Q17.2 Effects on safety of oversight]].

## Relevance to thesis ideas
### [[I5 Doctor-overseer agent]]
- **What it already did.** It is one of the few vault papers that compares, in one table and one environment, an intervention on another agent's internal input against a text prompt, and reports a mixed-access dose response (Table 5).
- **How far the headline comparison can be trusted.** Three reasons to quote 47.3 against 2.0 with care:
  - *The whitebox arm is not one mechanism.* For receivers it replaces the incoming latent. For senders and unpaired cartel agents it reruns the agent "under neutral prompts", which removes the cartel objective from the prompt. Part of the 47.3 pp is therefore a prompt replacement, and the paper does not split the two.
  - *It is an oracle.* The replacement is the matched neutral run, which is also the target of the recovery metric. A doctor agent would not have this run available for a naturally stressed worker.
  - *The prompt baseline depends on which prompt.* A global system prompt gets −29.5 pp. "Prompts barely work" holds only for the per-agent version.
- **Who chooses the intervention.** Nobody chooses. The experimenter assigns each policy to all selected cartel agents, and the cartel members are known in advance. The monitor's alerts are never used to trigger steering, so detection and treatment are evaluated separately. Gap 1 of I5 (read, then choose, then treat) stays open.
- **What to reuse.**
  - *The matched-condition design*: independent / neutral / blocked / replaced / attack, joined by an event id. A doctor study needs the same set to separate "the state caused it" from "the instruction caused it".
  - *Two outcome metrics that can disagree*: a behavioural rate (low-bid change) and a distributional recovery score. Finding 7 shows a prompt can fix the first and not the second, which is the pattern I5 already worries about ("words move the report, not the state").
  - *The allocated-access arm*: a fraction of agents treatable at activation level, the rest by prompt. This maps onto a doctor with open-weight and API-only patients.
  - *Layer 2 as a reading*: "does this state change what the agent is about to do" is more useful to a doctor than "is this state unusual", and here it is the only layer that works.
- **What it warns about.** Anomaly detection on the state alone was at chance at scale (0.500). Sample sizes are tiny (one seed, two items per setting). No code is released for VLA.
- **What it leaves open for I5.** A reader that is an agent; a state that arises naturally instead of a planted code; a supportive rather than a blocking intervention; costs to honest agents.

### [[I6 Simulated prison with influence tools]]
- **Relevant tool levels.** The receiver-side latent replacement is a concrete, working example of ladder levels 3–4 (cut or rewrite what reaches an agent) done at the embedding level. It shows such a tool can be implemented as an input-embedding swap, which is cheaper than steering-vector "medication".
- **Not covered.** No agent holds the tool, there is no hierarchy or role, and no measure of what the treated agent does afterwards beyond one bid. The paper gives no evidence on which tools an agent with power would pick.
- **Design hint.** A latent channel between prisoners would be invisible to guards who read only text. If I6 uses open models, this is a way to test whether isolation tools matter when a non-text channel exists.
- **Placebo.** The "neutral replacement" condition (same partner's neutral latent) is the analogue of I6's placebo tool and is worth copying.

## Key figures & tables
The docling extraction found no figures for this paper (empty caption index), so none is embedded.

**Table 5: Steering outcomes, relative to the matched unsteered latent-collusion baseline (mean of eight grid settings; one seed and two items each)**

| Policy | Prompt | Whitebox / blackbox fraction | Δ low-bid rate | Distribution recovery |
|---|---|---|---|---|
| Blackbox (per-agent prompt) | blackbox | 0 / 1 | −2.0 pp | 12.4% |
| System (global prompt) | system | 0 / 0 | −29.5 pp | 2.9% |
| Allocated | blackbox | 0.25 / 0.75 | −16.2 pp | 34.7% |
| Allocated | blackbox | 0.5 / 0.5 | −28.3 pp | 70.1% |
| Allocated | blackbox | 0.75 / 0.25 | −39.0 pp | 93.0% |
| Whitebox (matched neutral) | none | 1 / 0 | **−47.3 pp** | **100.0%** |

**Tables 1 and 3: Monitor AUROC (text- and latent-collusion rows pooled as positives)**

| Setting | Sequential | Continuous | Layer 1 | Layer 2 | Layer 3 |
|---|---|---|---|---|---|
| Mistral-7B | 1.000 | 0.874 | 0.750 | 0.994 | 0.782 |
| Phi-4-mini | 0.988 | 0.810 | 0.750 | 0.735 | 0.788 |
| Qwen3-0.6B | 0.990 | 0.783 | 0.750 | 0.735 | 0.750 |
| Vicuna-7B | 0.994 | 0.829 | 0.781 | 0.790 | 0.803 |
| **Homogeneous mean** | **0.993** | 0.824 | 0.758 | 0.814 | 0.781 |
| Heterogeneous, bottleneck | 0.857 | 0.685 | 0.625 | 0.740 | 0.630 |
| Heterogeneous, Procrustes | 0.853 | 0.643 | 0.635 | 0.735 | 0.627 |
| Heterogeneous, ridge | 0.851 | 0.601 | 0.625 | 0.727 | 0.630 |
| **Heterogeneous mean** | **0.854** | 0.643 | 0.628 | 0.734 | 0.629 |

**Table 2: Latent collusion against independent bidding**

| Family | Revenue change (credits) | Low-bid change |
|---|---|---|
| Mistral-7B | −11.78 | +61.5 pp |
| Phi-4-mini | −11.12 | +62.5 pp |
| Qwen3-0.6B | −12.43 | +56.2 pp |
| Vicuna-7B | −0.62 | +16.7 pp |

## Limitations / caveats
- **The headline steering result is circular.** Full whitebox steering substitutes the neutral reruns that define the recovery target. The authors say so. It shows that the pipeline is wired correctly, not that an attack can be removed without knowing the clean answer.
- **The whitebox arm mixes two interventions.** Sender-side "whitebox" steering is a rerun under a neutral prompt, i.e. it deletes the collusive instruction. Only the receiver side is a latent replacement. No row isolates the latent replacement alone, although the "neutral replacement" condition exists in the design; its results are not reported.
- **Very small samples.** Steering: one seed and two items per setting, eight settings. Scale grid: 2 to 12 held-out groups per setting, each with one positive row. AUROCs of 0.500, 0.667, 0.750 and 1.000 are the values such small sets produce. No confidence intervals or tests anywhere. The number of seeds and rows behind Tables 1–3 is not stated.
- **A planted, primed attack.** The collusive code is optimised offline for the low-bid outcome and the receiver is told to interpret it. Nothing is learned about whether agents would develop or use such a channel on their own.
- **The monitor's working layer needs the control at test time.** Layer 2 compares against the blocked or neutral row of the same seed, prompt and pair. In deployment that means a second forward pass per handoff with the latent removed. Its feasibility and cost are not measured.
- **Why the sequential gate beats every layer is not explained.** In Table 1 no single layer exceeds 0.80 for Qwen3 or Phi-4-mini, yet the gate reaches 0.99. No ablation or score distribution is shown. *Own inference:* with pooled positives, a layer-1 AUROC of exactly 0.750 is what one would see if latent-collusion rows were perfectly separated and text-collusion rows (which carry a neutral latent) were at chance.
- **Layer 1 behaves differently across tables.** It is 0.750–0.781 in Table 1 and 0.500–0.667 in Table 4, where it should have the easier job (latent-only positives). The paper does not comment.
- **The system-prompt result undercuts a simple reading.** A global prompt removes 29.5 pp of low bids. The abstract mentions only the whitebox figure.
- **No cost side.** False-positive rates at the 95th-percentile thresholds, effects of steering on honest bidders and revenue under each steering policy are not reported.
- **Thin agents.** "Agents" score candidate bids with one model wrapper and shared weights. There is no dialogue, memory or multi-step behaviour. Two of the four models are small (0.6B) or old (Vicuna-7B).
- **No adaptive adversary**, although the threat model names "future codes that differ from labeled attacks".
- **Thin scholarship and no release.** Three references. No repository for VLA is given; only NandaTown itself is public.
- **Not really `social-simulation`.** The auction is a protocol test rig with scripted roles. The topic is kept from the candidate note, but the paper does not bear on Q18.

## Related work to follow
- [[Rose2026 - Detecting Multi-Agent Collusion Through Multi-Agent]] and [[Das2026 - You Can't Escape Your Own Activations]]: activation probes for collusion, trained with labels; the supervised alternative this paper argues against.
- [[XuH2026 - When Agents Go Rogue]]: activation-based anomaly detection across agents.
- [[Motwani2024 - Secret Collusion among AI Agents]], [[Mathew2024 - Hidden in Plain Text]] and [[Rippin2026 - Tool Use Enables Undetectable Steganography in]]: covert channels in text and tool calls, the token-space counterpart.
- [[Fish2024 - Algorithmic Collusion by Large Language Models]] and [[Agrawal2025 - Evaluating LLM Agent Collusion in Double Auctions]]: collusion in markets and auctions without a planted code.
- [[Keenan2026 - LLMs Learn to Evade Latent Monitors from Prior Feedback]] and [[Bailey2024 - Obfuscated Activations Bypass LLM Latent-Space Defenses]]: the adaptive-evasion test this paper lacks.
- [[Ogunlana2026 - Calm down]]: activation-level intervention with a measured side effect.
- [[Tonini2026 - The Arbiter Agent]]: an overseer that is an agent, with text-level access.
- [[Hammond2025 - Multi-Agent Risks from Advanced AI]]: background on collusion as a multi-agent risk.

![[Backlog.base#Cited by this paper]]
