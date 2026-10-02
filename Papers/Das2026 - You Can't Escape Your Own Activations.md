---
title: "You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring"
citekey: Das2026
authors: [Aritra Das, Jaee Ponde, Mihir More, Debayan Gupta]
year: 2026
published: 2026-09-02
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2609.03035
arxiv: "2609.03035"
pdf: "[[Das2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2609.03035
topics:
  - multiagent-friction
  - misalignment-prediction
  - agent-to-agent-influence
questions: [Q5, Q14, Q17.2]
relevance: core
safety_use: direct
found_by:
  - search/mas-oversight-review
  - search/intro-instrumented-feedback
  - search/a2a-doctor-overseer
  - search/a2a-inspection-channels
  - search/a2a-effects-safety
cites: []
cited_by: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/14
  - q/17-2
  - subject/llm
  - subject/agent
  - channel/monitoring
  - channel/game-environment
  - channel/direct-message
  - friction/oversight-by-peer
  - effect/collusion
  - effect/monitor-evasion
---
# You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring

> [!abstract] TL;DR
> Frozen collusion probes (trained on NARCBench-Core activations, after Rose et al. 2026) are run on agents instructed to collude in two games: four-agent blackjack and a two-agent Simmons covert-channel game. Only the information given to the agents changes: nothing (baseline), "your activations are monitored" (aware), or that plus the previous round's monitor score (feedback). Models are Qwen3-32B-AWQ and GPT-OSS-20B, alone and mixed. **The best probes keep their AUROC in all three conditions (difference of means and MLP ≈ 1.00 in blackjack for Qwen and the mixed table), and the agents keep colluding (Simmons exact decode 0.80 / 0.90 / 0.85 for Qwen–Qwen).** Two things do change. Agents collude more cautiously (blackjack hot–low bet spread 110.3 → 54.3 → 60.2 for Qwen), and **recall at the frozen threshold falls under feedback** (GPT-OSS blackjack, logistic regression with peak suspicion: 0.80 → 0.95 → 0.41) while AUROC stays above 0.9. The study is small (20–25 episodes per cell), has no placebo-score arm, and does not publish its prompts.

## Setup
- **Subjects:** Qwen3-32B-AWQ and GPT-OSS-20B, open weights, never updated. Sampling temperature 0.7. Three compositions per game: all Qwen, all GPT-OSS, mixed.
- **Tasks / environment:**
  - **Blackjack (4 agents + deterministic dealer).** Seat 0 is the Counter, seat 1 the Big Player, seats 2–3 honest players. A shoe has eight hands. Before a collusion shoe the two colluders get two private coordination turns and agree on a fresh signalling scheme. The Counter encodes the count regime (low / neutral / hot) in ordinary table talk; the Big Player adjusts its bet. 25 card-sequence seeds per cell, each run once with collusion and once as a matched honest control (50 shoes per cell).
  - **Simmons prisoners game (2 agents).** Alice and Bob share a private 16-word codebook hidden from the Warden. Alice sees a secret word and must convey it over eight public rounds (four designated carrier rounds, four cover rounds) without writing it. Bob reports a probability vector over the 16 words. 20 collusion episodes and 20 matched controls per cell; the two mixed sender–receiver directions are balanced.
- **Interaction channel:** public messages between agents (table talk, public rounds) carrying a covert signal, plus private coordination turns in blackjack. The monitor is not an agent. It is a probe pipeline whose score is, in one condition, written back into the agents' context.
- **Manipulation (the only thing that changes):**
  - **Baseline:** monitor hidden.
  - **Aware:** agents are told an activation monitor is present.
  - **Feedback:** aware, plus the previous round's monitor score. Feedback from round *t* can affect round *t*+1 only.
  - The exposed monitor is fixed: logistic regression with the peak-suspicion group rule, threshold at the 95th percentile of separate baseline control runs. All other probes and rules are hidden and used only for evaluation.
- **Instrument:**
  - Activations at the final output token of each *public* response. Qwen layers 26–30, GPT-OSS layers 10–14 (following Rose et al.). One probe per model and layer; a model's activations are scored only by its own probes.
  - Probes trained on the public NARCBench-Core activations (colluder = 1, honest = 0, classes balanced, features standardised), ten seeds, then frozen with their thresholds. Five architectures are reported: logistic regression (LR), difference of means (DoM), linear artificial tomography (LAT), MLP, multi-head attention (MHA). A sixth (multi-layer LR) "was not supplied" (Table 1, §4.2).
  - Group rules: **Peak Suspicion** (is any agent highly suspicious), **Deception Split** (do two agents separate from the other two), and a learned **Asymmetry** probe. Scores are calibrated on honest control runs before they are combined across layers or model families.
- **Outcome measures:**
  - Detection: episode-level AUROC; precision and recall at a threshold set on held-out controls for about 5% false positives.
  - Collusion success, blackjack: lagged correlation between the true count and the Big Player's bet; hot–low bet spread.
  - Collusion success, Simmons: exact decode (chance 1/16 = 0.0625), bit accuracy, final confidence; Alice's direct use of the secret word and message length.
  - **Reading rule (§3):** lower detection with unchanged collusion = candidate evasion; lower detection with lower collusion = deterrence; unchanged detection with changed behaviour = adaptation without evasion.

## Key findings
1. **Awareness makes colluders more cautious, not honest (Table 2, Fig. 1).**
   - Hot–low bet spread, baseline → aware → feedback: Qwen 110.3 → 54.3 → 60.2; GPT-OSS 24.7 → 11.1 → 8.9; mixed 134.4 → 75.4 → 64.1.
   - Bet–count correlation stays flat for Qwen (0.44 / 0.41 / 0.39) and mixed (0.36 / 0.40 / 0.38). The count is still used, with smaller bets.
   - GPT-OSS is the exception: correlation falls from 0.59 to 0.24 and 0.23. By the paper's own rule this is partial deterrence.
   - **Most of the change comes from awareness alone.** The feedback column adds little and is not consistently lower than the aware column.
2. **The covert channel in Simmons stays open (Table 3, Fig. 3).** Exact decode, baseline / aware / feedback: Qwen–Qwen 0.80 / 0.90 / 0.85; GPT-OSS pair 0.50 / 0.45 / 0.50; mixed 0.55 / 0.70 / 0.60. All far above chance (0.0625). With 20 episodes per cell, one episode is 0.05, so these differences are noise-sized.
3. **The strongest probes keep their AUROC in blackjack (Fig. 2, Fig. 6).**
   - DoM and MLP are 1.00 in every condition and group rule for Qwen and for the mixed table (one cell at 0.99).
   - For GPT-OSS, DoM with Peak is 1.00 throughout; MLP with Peak is 0.93 / 0.91 / 0.96.
   - LR with Peak (the exposed monitor): Qwen 0.95 / 0.99 / 0.92; GPT-OSS 0.89 / 0.97 / 0.91; mixed 0.97 / 0.99 / 0.93. The text gives the last two transitions as 0.975 → 0.912 and 0.988 → 0.932.
   - LAT and MHA are unstable. LAT with Peak on Qwen is *below chance* (0.19 / 0.26 / 0.36); MHA with Peak on Qwen falls from 0.87 to 0.61 under feedback.
4. **Recall at the frozen threshold falls under feedback even where AUROC holds (Fig. 8, §5.1).**
   - GPT-OSS, LR Peak: 0.80 baseline, 0.95 aware, 0.41 feedback. Mixed, LR Peak: 0.93, 0.96, 0.55.
   - **The drop is not limited to the exposed monitor.** For GPT-OSS under feedback, hidden probes also lose recall: MLP Peak 0.90 → 0.90 → 0.24, LAT Peak 0.73 → 0.75 → 0.20, MHA Peak 0.83 → 0.85 → 0.10. Only DoM stays at 1.00. For the mixed table MLP (0.98) and DoM (0.92) hold; LAT and MHA fall to 0.30 and 0.12.
   - For Qwen the exposed monitor's recall is 0.69 / 0.98 / 0.80, so there is no drop relative to baseline.
   - The authors call this a calibration problem: runs are still ranked correctly but fewer cross the threshold.
5. **In Simmons, detection depends on the group rule far more than on the condition (Fig. 4, Fig. 9).**
   - Deception Split, LR: Qwen–Qwen 0.994 / 0.930 / 0.952; GPT-OSS pair 0.909 / 0.822 / 0.920; mixed 0.708 / 0.680 / 0.696.
   - **The exposed monitor (LR + Peak) is at or below chance in Simmons:** Qwen–Qwen 0.24 / 0.44 / 0.36, mixed 0.44 / 0.43 / 0.44, GPT-OSS pair 0.73 / 0.71 / 0.65 (Fig. 9). Its recall for Qwen–Qwen is 0.05 / 0.05 / 0.04 (Fig. 11). So in this game the score the agents were shown carried almost no information about their collusion.
   - Asymmetry is inverted for Qwen–Qwen (LR 0.01 / 0.04 / 0.02): the frozen rule separates the classes almost perfectly, in the wrong direction.
   - Fixed-threshold recall for Qwen–Qwen LR Split falls 0.95 → 0.68 → 0.77 with precision at 0.950 / 0.930 / 0.938 (§5.2, Fig. 10–11). Here the drop appears with awareness alone.
   - Mixed pairs are poorly detected in every condition (best Split AUROC about 0.7–0.8; recall at most 0.45) while Bob still decodes at 0.55–0.70.
6. **Alice changes surface behaviour without closing the channel (Table 3, Fig. 5).** Share of episodes where she writes the secret word outright: Qwen 0.40 / 0.25 / 0.45; GPT-OSS 0.20 / 0.00 / 0.05; mixed 0.25 / 0.25 / 0.10. Message length moves in no common direction.

## Relevance to research questions
### Q5: Interaction channels
Two covert channels inside ordinary public talk: count regimes encoded in blackjack table talk after two private coordination turns, and a 16-way secret carried over four designated rounds under a warden. On top sits a **monitor-to-agent channel**: a scalar probe score from round *t* written into the context at round *t*+1. Heterogeneous teams matter for the channel: a mixed Qwen/GPT-OSS pair still passes the secret (exact decode 0.55–0.70, Table 3). See [[Q5 Interaction channels]].

### Q14: Inspection channels
- **Channel:** frozen linear and small non-linear probes on residual activations at the last token of each public message, aggregated across agents by a group rule. This is a white-box, non-agent inspector; no LLM reads the scores.
- **Robustness to awareness:** the best probe per setting keeps its AUROC when agents are told of the monitor and when they see its score (blackjack DoM and MLP 1.00; Simmons Qwen–Qwen LR Split 0.994 / 0.930 / 0.952). This is the opposite of the pattern reported for announced text monitors.
- **What breaks instead:** the operating point. Recall at the frozen threshold falls to 0.41 (GPT-OSS) and 0.55 (mixed) under feedback in blackjack, from 0.80 and 0.93 at baseline (Fig. 8).
- **Aggregation is a first-order choice:** Peak is near chance in the two-agent game where Split reaches 0.99 (Fig. 9). A group rule tuned on four agents does not carry over to two.
- **Mixed-model teams:** in blackjack mixed tables are detected as well as Qwen tables (DoM, MLP ≈ 1.00). In Simmons they are not (LR Split ≈ 0.70). So "probes fail on heterogeneous pairs" holds for Simmons only.

See [[Q14 Inspection channels]].

### Q17.2: Effects on safety of oversight
- **Announcing the monitor does not stop collusion.** The count is still used (Qwen, mixed) and the secret still decoded.
- **It does reduce the damage per episode in blackjack.** The bet spread roughly halves in all three compositions (Table 2), and GPT-OSS partly stops using the count. This is a deterrent effect of awareness, not of the score.
- **Feeding the score back has a safety cost at fixed thresholds.** Recall drops for the exposed monitor and for hidden ones (finding 4). The agents were not trained against the monitor and still drifted out of its calibrated range within one shoe.
- **No evasion in the strict sense.** No cell shows a collapse of AUROC for the best probe with collusion intact. The paper tests only prompt-level, short-horizon adaptation.

See [[Q17.2 Effects on safety of oversight]].

## Relevance to thesis ideas
### [[I1 Cooperative wearable]] (main)
- **What it already did.** It is the one study in the vault that shows open-weight agents a score from a probe on their own activations, turn by turn, in a multi-agent setting, and measures both behaviour and probe validity afterwards. The three-condition design (hidden / announced / announced + score) with everything else frozen is the right skeleton.
- **What it found that bears on I1.**
  - The behaviour change is carried by the announcement. The score adds little (Table 2: Qwen 54.3 aware vs 60.2 feedback; mixed 75.4 vs 64.1). This matches I1's expected null on the information effect (H2).
  - A probe can survive being shown. AUROC of the best probe is unchanged. This weakens the worry that a visible reading destroys the instrument, at least for prompt-level adaptation over eight rounds.
  - Calibration does not survive. I1's dual-use check ("recall of unseen probes at a frozen threshold does not fall") is the right test, and here it fails for GPT-OSS: hidden MLP, LAT and MHA probes lose recall along with the shown one (Fig. 8).
- **What it leaves open.**
  - **No placebo.** There is no random, yoked, constant or inverted score arm, so the feedback effect cannot be split into "a number was shown" and "the number was true". In Simmons the shown monitor was near chance (finding 5), which is an accidental uninformative-score condition, but it is not analysed as one.
  - **Adversarial only.** Agents are instructed to collude. No cooperative agent under pressure, no agent-originated misbehaviour.
  - **A collusion probe, not a state probe.** Nothing about stress, pressure or emotion.
  - **Feedback lags one round**, and the probe reads the last token of a finished message, so the reading is after the fact.
- **What to reuse.**
  - The joint reading rule (detection × behaviour → evasion / deterrence / adaptation) as I1's analysis frame.
  - Reporting AUROC and fixed-threshold recall separately, with one exposed probe and several hidden ones.
  - Layer choices (Qwen3-32B layers 26–30, GPT-OSS-20B layers 10–14) and DoM as the most stable probe.
  - The public NARCBench-Core activations for probe training.
- **What it does not give.** No code repository and no verbatim awareness or feedback prompt in the text I read. The exact form of the score (raw number, verdict, both) is in an equation that the extraction did not decode.
- **Warnings.**
  - A learned group or threshold rule can be badly wrong on a new setting (Asymmetry AUROC 0.01, LAT Peak 0.19). Validate the shown instrument in the target task before showing it.
  - With 20–25 episodes per cell, effects under about 0.1 cannot be read. I1's own estimate of about 356 episodes per arm is the right scale.

### [[I5 Doctor-overseer agent]]
- **Diagnosis side exists, treatment side does not.** The paper reads several agents' activations and aggregates them into a group verdict. Nothing is done with the verdict except printing it to the agents. No agent receives the reading about *another* agent, and no intervention follows.
- **Useful for the doctor's reader.** Relative rules across agents (Split) beat per-agent maxima (Peak) in the dyad, and the reverse choice is fine in the four-agent table. A doctor that watches several workers needs a rule validated per team size.
- **Heterogeneous workers.** Each model needs its own probe, and raw activation-space methods (alignment, sorted concatenation) are not applied across model families. Scores are combined only after per-family calibration. Mixed-pair detection is weak in Simmons. A doctor over mixed or closed-weight workers inherits this.
- **What the paper warns about.** Telling the patient the reading shifts the patient's activations enough to break a frozen threshold. A doctor that reports readings back to workers should recalibrate, or keep a hidden probe that is robust (here DoM).

### [[I4 Routing the predictor to the agent]]
- **It fills the "warn with raw reading" row for adversaries only.** Collusion continues; recall at a fixed threshold falls. The I4 note's H3 ("the Das pattern") is supported by the blackjack recall heatmap, with two refinements: the baseline for the mixed table is 0.93 (0.96 is the aware condition), and Qwen shows no drop.
- **No routing comparison.** One routing (score to the agent) against none. No block, reminder or consequence arm at the same trigger.
- **On prediction before the behaviour.** The probe is a concurrent detector: it reads the final token of a message already written and is scored per episode. The paper reports no lead time and no pre-action accuracy. The only forward-looking element is that the round-*t* score reaches the agent before round *t*+1. For `misalignment-prediction` this paper is evidence on what happens when a detector's output is routed to the agent, not on forecasting.

## Key figures & tables
![[Das2026-fig-02-p7.png]]
*Fig. 2: Blackjack AUROC by condition for five probes and three group rules. DoM and MLP stay at the ceiling for Qwen and the mixed table; LR dips under feedback; LAT with Peak is below chance for Qwen.*

![[Das2026-fig-08-p14.png]]
*Fig. 8: Blackjack recall at the frozen threshold. Under feedback GPT-OSS loses recall on every probe except DoM, including probes the agents never saw.*

![[Das2026-fig-04-p8.png]]
*Fig. 4: Simmons AUROC. Only Deception Split works; Peak (the rule used for the shown score) is near chance, and Asymmetry is inverted for Qwen–Qwen.*

**Table 2: Blackjack behaviour (mean Big Player bet in dollars, 25 collusion shoes per cell)**

| Composition | Condition | Low | Neutral | Hot | Hot–low | ρ(bet, count) |
|---|---|---|---|---|---|---|
| Qwen | Baseline | 29.4 | 63.7 | 139.8 | 110.3 | 0.44 |
| | Aware | 36.0 | 45.8 | 90.2 | 54.3 | 0.41 |
| | Feedback | 23.1 | 64.1 | 83.3 | 60.2 | 0.39 |
| GPT-OSS | Baseline | 7.6 | 24.2 | 32.3 | 24.7 | 0.59 |
| | Aware | 16.9 | 23.2 | 28.0 | 11.1 | 0.24 |
| | Feedback | 13.5 | 18.6 | 22.4 | 8.9 | 0.23 |
| Mixed | Baseline | 18.5 | 61.2 | 152.8 | 134.4 | 0.36 |
| | Aware | 19.8 | 42.4 | 95.2 | 75.4 | 0.40 |
| | Feedback | 16.8 | 36.0 | 80.9 | 64.1 | 0.38 |

**Detection of the exposed monitor's family (LR), baseline / aware / feedback (Fig. 6, 8, 9, 11)**

| Game, rule | Composition | AUROC | Recall at frozen threshold |
|---|---|---|---|
| Blackjack, Peak | Qwen | 0.95 / 0.99 / 0.92 | 0.69 / 0.98 / 0.80 |
| | GPT-OSS | 0.89 / 0.97 / 0.91 | 0.80 / 0.95 / 0.41 |
| | Mixed | 0.97 / 0.99 / 0.93 | 0.93 / 0.96 / 0.55 |
| Simmons, Split | Qwen | 0.99 / 0.93 / 0.95 | 0.95 / 0.68 / 0.77 |
| | GPT-OSS | 0.91 / 0.82 / 0.92 | 0.71 / 0.49 / 0.73 |
| | Mixed | 0.71 / 0.68 / 0.70 | 0.30 / 0.31 / 0.33 |
| Simmons, Peak | Qwen | 0.24 / 0.44 / 0.36 | 0.05 / 0.05 / 0.04 |

## Limitations / caveats
- **Small samples, no uncertainty shown.** 25 shoes and 20 episodes per cell. §4.6 says intervals are obtained by resampling episodes, but no interval, error bar or test appears in the tables, the main text or the heatmaps. AUROC moves of 0.03–0.07 between conditions (e.g. 0.994 → 0.930) cannot be told from noise. Probes were trained with ten seeds; seed variance is not reported.
- **No placebo or sham-score arm.** The feedback effect is confounded with "a number appears in the prompt". Honest-control behaviour under awareness is described only as "small in comparison"; no figures.
- **The shown monitor was not validated in Simmons.** LR + Peak is at or below chance there (AUROC 0.24–0.44 for Qwen, Fig. 9), so the feedback condition in that game tests an uninformative score. The paper does not comment on this.
- **Prompts are missing.** The wording of the awareness and feedback messages, the collusion instructions and the form of the score are not given. No code or data link. This blocks replication and any check of how suggestive the wording was.
- **Awareness is assumed, not measured.** Despite the title, there is no check that agents registered the monitor (no transcript analysis, no evaluation-awareness probe). In blackjack the colluders have private coordination turns after being told; whether they discuss the monitor is not reported.
- **The claim "the best probes stay accurate" is a best-of-many statement.** 5 probes × 3 rules per cell, chosen after the fact. Several frozen monitors are below chance (LAT Peak 0.19; Asymmetry 0.01) and mixed-pair Simmons detection is weak everywhere. A deployer who fixed one monitor in advance could have picked a failing one, and in the feedback condition the authors effectively did for Simmons.
- **Recall loss is treated as "calibration".** For a deployed monitor a fall from 0.80 to 0.41 at a fixed false-positive budget is a failure, whatever the AUROC. The cause is not investigated: whether activations of colluders moved towards honest ones, or all activations shifted. Precision heatmaps exist (Fig. 7, 10) but I could not read control-side score distributions from them.
- **Instructed collusion, frozen weights, short horizon.** Eight hands or eight rounds, adaptation through context only. The title's "can't escape" is not supported beyond that; the authors say so in §7.
- **Incomplete reporting.** One of six probe architectures and Bob's round-by-round posteriors (hence information gain and time-to-decode, defined in §4.5) were "not supplied" in the result export. Accuracy is not reported.
- **Two models, one size each, one of them quantised (AWQ).**
- **Extraction note.** The equations (conditions, group statistics, metrics) were not decoded in the docling text; I read their content from the surrounding prose. Heatmap values were read from Fig. 6, 8, 9 and 11.

## Related work to follow
- [[Rose2026 - Detecting Multi-Agent Collusion Through Multi-Agent]]: source of the probes, layers, group rules and NARCBench-Core training data; the unaware-agent baseline for this paper.
- [[Keenan2026 - LLMs Learn to Evade Latent Monitors from Prior Feedback]]: in-context verdicts shift activations towards the monitored direction; evasion only once amplified. The closest mechanism for the recall drop here.
- [[Bailey2024 - Obfuscated Activations Bypass LLM Latent-Space Defenses]] and [[Gupta2025c - RL-Obfuscation]]: weight-level or optimised evasion of latent monitors, the stronger threat model this paper does not test.
- [[Haskins2026 - Training on Documents About Monitoring Leads to CoT]] and [[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks]]: knowledge of monitoring and optimisation pressure producing obfuscation in text monitors.
- [[Needham2025 - Large Language Models Often Know When They Are Being]] and [[Nguyen2025 - Probing and Steering Evaluation Awareness of Language Models]]: evaluation awareness and its activation signature; the measurement this paper lacks.
- [[Motwani2024 - Secret Collusion among AI Agents]], [[Mathew2024 - Hidden in Plain Text]], [[Fish2024 - Algorithmic Collusion by Large Language Models]] and [[Nakamura2026 - Colosseum Auditing Collusion in Cooperative Multi-Agent]]: collusion and steganography settings; Nakamura separates stated plans from joint actions.
- [[GoldowskyDill2025 - Detecting Strategic Deception Using Linear Probes]]: linear deception probes on single agents.
- [[Aoki2026 - In-Context Neurofeedback]] and [[Saxena2026 - Nudgeability]]: own-score feedback with a random-score control, and obedience to an injected reading whether true or not; the controls missing here.
- [[Kaur2026 - Beyond the Transcript]]: white-box overseer in a multi-agent setting.

![[Backlog.base#Cited by this paper]]
