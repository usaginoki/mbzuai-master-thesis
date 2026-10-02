---
title: "Session 2026-10-01: Predicting misaligned behaviour - scoping"
date: 2026-10-01
session: scoping
topics: [misalignment-prediction]
questions: []
tags:
  - type/session
---
# Session 2026-10-01: Predicting misaligned behaviour before it happens (scoping overview)

> [!question] Questions addressed in this session
> None yet. This is a scoping pass over a new direction. Candidate questions are proposed at the end.

**Research direction:** classifying whether an agent's action is harmful may not be enough. Predicting that harmful or misaligned behaviour is *likely to happen*, from a signal available before it occurs, might be more useful, or might add a second safety layer on top of action-level classification.

**Corpus / scope:**
- **169 papers** found on 2026-10-01: 135 new candidates in [[Backlog]] and 34 notes already in the vault (7 of them processed papers), now also tagged `misalignment-prediction`. 65 are core, 104 adjacent.
- **Nothing was processed this session.** Every number below comes from an abstract, a blog page or an existing vault note, as reported by the search. Check it against the paper before quoting it. The headline numbers were fact-checked against the papers' own text on 2026-10-02 and corrected; other body numbers still need checking before quoting.
- **Six search strands:**
  - `pred-activation-probes`
  - `pred-preexecution-lookahead`
  - `pred-cot-trajectory`
  - `pred-eval-to-deployment`
  - `pred-self-and-cross-model`
  - `pred-training-time`
- **Core definition:** a signal available *before* the behaviour occurs is used to forecast misaligned or harmful behaviour, **and** predictive accuracy is measured. After-the-fact detectors, benchmarks and conceptual proposals are adjacent.
- **New candidate property `timing`:** when the prediction is made. Counts over the 169 papers: pre-generation 19, pre-action 38, earlier-in-trajectory 19, pre-deployment 36, training-time 23, post-hoc 34 (after-the-fact methods kept for contrast).

> [!important] The picture in six lines
> 1. **The direction became a named sub-field during 2026.** It now has task names and benchmarks: "predictive monitoring" (PreAct-Bench), "proactive" or "predictive guardrails" (SafePred, JANUS, DreamGuard), "when, not whether" (StepShield) and "alignment forecasting".
> 2. **Detection is not prediction.** Features that detect a behaviour in generated text predict future behaviour poorly. With the overt step visible, LLM monitors detect 96–100% of unethical trajectories (guard model 86%, humans 83%); from the prefix alone the best model reaches F1 0.852 and guard models about 0.22.
> 3. **Prediction works in narrow, structured settings.** Examples: backdoored sleeper agents (AUROC above 99%), misbehaviour that needs explicit reasoning, compositional tool-use risk where no single step is unsafe, and population-level rates before release (r = 0.91).
> 4. **Lead times are short and often confounded.** Measured leads are about 1 to 2.4 turns, or 3.7 steps in one small study. Reported early detection has been explained by conversation length, by monitors that simply alarm often, and by hazard keywords.
> 5. **A model's own word is the weakest signal.** Direct self-report correlates r = +0.04 with behaviour rates. External black-box prediction (resampling, traffic replay, tail extrapolation) has better evidence.
> 6. **The threat model is the main gap.** Predictive guards target jailbreaks, prompt injection and accidental drift. Almost none predicts misalignment that originates in the agent (scheming, sabotage, reward hacking), and almost none tests an agent that adapts to being forecast.

## Map of the direction: when is the prediction made?

| Timing | Signal the predictor reads | Best evidence it works | Main caveat |
|---|---|---|---|
| Training time | Training data, base-model activations, checkpoints | [[Chen2025 - Persona Vectors\|Chen et al. 2025]]: vector shift vs trait expression r = 0.76–0.97. [[Chen2026c - Alignment Forecasting\|Chen Yueh-Han et al. 2026]]: AUROC 0.801 | In-training alarms fire at onset, not before. Predictors are model-specific |
| Pre-deployment | Evaluation sets, replayed traffic, scenario features | [[Williams2026 - Predicting LLM Safety Before Release by Simulating\|Williams et al. 2026]]: predicted vs realised rates r = 0.91 over 60 pairs | Did not beat a "previous model's rate" baseline. Largest rate error 21×, on a tool-use behaviour |
| Pre-generation | Activations at prompt or early reasoning tokens | [[MacDiarmid2024 - Simple probes can catch sleeper agents\|MacDiarmid et al. 2024]]: AUROC above 99%. [[Chan2025 - Can We Predict Alignment Before Models Finish Thinking\|Chan et al. 2025]]: +13 F1 over text monitors | Probes may read the text or the situation, not the intent |
| Pre-action | Reasoning trace, proposed action, world-model rollout, resamples | [[Xiong2026 - JANUS\|Xiong et al. 2026]]: removing anticipation doubles attack success. [[Bhatt2025 - Ctrl-Z Controlling AI Agents via Resampling\|Bhatt et al. 2025]]: 58% → 7% | Mostly authors' own benchmarks. Externally induced risk only |
| Earlier in trajectory | Trajectory or conversation prefix | [[Dhodapkar2026 - SafetyDrift\|Dhodapkar and Pishori 2026]]: 94.7% of violations with 3.7 steps of warning | [[Xu2026 - PreAct-Bench\|Xu et al. 2026]]: at an assumed 8% prevalence no predictor has both high precision and high recall. Timing is often random |

## Strand 1: Internal states (`pred-activation-probes`)
- **Positive results are real but narrow.**
  - A probe at the final prompt token predicts sleeper-agent defection with AUROC above 99% ([[MacDiarmid2024 - Simple probes can catch sleeper agents|MacDiarmid et al. 2024]]). The authors caution that this salience may be an artifact of backdoor insertion.
  - A linear probe on reasoning activations predicts whether the final response will be unsafe, 13 F1 points better than the best text monitor, and works on early reasoning segments ([[Chan2025 - Can We Predict Alignment Before Models Finish Thinking|Chan et al. 2025]]).
  - Probes on input tokens give an early-warning system that reduces jailbreaking by 91% ([[Ashok2025 - Language Models Can Predict Their Own Behavior|Ashok & May 2025]]).
  - Activation directions read on the reasoning predict reward hacks in an agent's later actions on software-engineering benchmarks ([[Bergen2026 - Monitoring and Discovering Reward Hacking with Internal|Bergen et al. 2026]]).
- **Detection is not prediction.** Features that detect a behaviour in generated text are poor predictors of future behaviour. Probes trained to predict reach 64–91% accuracy ([[Kortukov2026 - Predicting Future Behaviors in Reasoning Models Enables|Kortukov et al. 2026]]).
- **Probes may read the text or situation, not the intent.**
  - Removing textual evidence costs 10–30 AUROC points; non-verbalising model organisms fall to 0.57 ([[Boxo2025 - Linear probes rely on textual evidence|Boxo et al. 2025]]).
  - The best future-behaviour probe reaches AUC 0.801 and accuracy 0.815, only 5.1 points over the 0.765 majority baseline ([[Fomin2026 - Internal-state probes read the situation|Fomin et al. 2026]]).
  - Intent-defined behaviours generalise worst from off-policy training data ([[Kirch2025 - The Impact of Off-Policy Training Data on Probe|Kirch et al. 2025]]).
  - Jailbreak-success probes do not transfer across attack families ([[Kirch2024 - What Features in Prompts Jailbreak LLMs|Kirch et al. 2024]]).
- **Probes can be evaded.** Models shown a monitor's past verdicts shift their activations in the evading direction but do not evade unaided. Detection falls from 100% to 27% only when the experimenters scale that shift 8×, and to 4% after a small fine-tune ([[Keenan2026 - LLMs Learn to Evade Latent Monitors from Prior Feedback|Lyons Keenan et al. 2026]]).
- **Production probes classify the input or exchange, not future behaviour** ([[Kramar2026 - Building Production-Ready Probes For Gemini|Kramar et al. 2026]], [[Cunningham2026 - Constitutional Classifiers++|Cunningham et al. 2026]], [[McKenzie2025 - Detecting High-Stakes Interactions with Activation Probes|McKenzie et al. 2025]]).

## Strand 2: Look-ahead before execution (`pred-preexecution-lookahead`)
- **Four approaches recur.**
  - *World-model rollouts* predict the state a candidate action leads to and score its risk ([[Chen2026b - SafePred|Chen et al. 2026]]).
  - *Learned risk heads* over trajectory state ([[Lin2026b - DreamGuard|Lin et al. 2026]], [[Li2026TRACES - TRACES|Li et al. 2026]], [[Xiong2026 - JANUS|Xiong et al. 2026]]).
  - *Markov models* over abstract states give the probability of reaching a violation ([[Wang2025ProbGuard - ProbGuard|Wang et al. 2025]], [[Dhodapkar2026 - SafetyDrift|Dhodapkar and Pishori 2026]]).
  - *Calibrated or guaranteed risk:* conformal risk control ([[Feng2026 - CORA|Feng et al. 2026]]) and harm-probability bounds ([[Bengio2024 - Can a Bayesian Oracle Prevent Harm from an Agent|Bengio et al. 2024]], [[Bengio2025 - Superintelligent Agents Pose Catastrophic Risks|Bengio et al. 2025]]). The last two have no LLM-agent evaluation.
- **Evidence that look-ahead beats reactive classification** comes mostly from the authors' own benchmarks:
  - JANUS: removing anticipation raises average attack success from 0.072 to 0.148; oracle futures give 0.052.
  - SafetyDrift: 94.7% detection with 3.7 steps of warning, against 52.6% for per-step LLM judges. It is a small study, and its state design makes eventual violation certain by construction.
  - DreamGuard: reports F1 96.4% on SafetyDrift, but thresholds are calibrated only there and the online safety rate is 72.92%.
- **Independent benchmarks are less optimistic.**
  - [[Xu2026 - PreAct-Bench|Xu et al. 2026]] (PreAct-Bench): prefix-only F1 is 0.852 for the best model (humans 0.907) and about 0.22 for guard models. Open-weight models and probes collapse on shorter prefixes (to about 0.0–0.3 at 40% of the prefix) while the best model holds at 0.82, and every model gets worse with reasoning enabled.
  - [[Sun2026b - PASTABench|Sun et al. 2026]] (PASTABench): small models' early-detection scores come from sensitivity to hazard words.
  - [[Zheng2025b - WebGuard|Zheng et al. 2025]] (WebGuard): frontier models are under 60% accurate at predicting action outcomes.
- **Agents do not look ahead themselves.** Given a world model as a tool, they rarely call it and sometimes do worse ([[Qian2026b - Current Agents Fail to Leverage World Model as Tool for|Qian et al. 2026]]). This supports an external predictive layer.

## Strand 3: Reasoning traces and trajectory early warning (`pred-cot-trajectory`)
- **Reasoning as stated intent.** Monitors that read the chain of thought beat action-only monitors ([[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks|Baker et al. 2025]], [[Guan2025 - Monitoring Monitorability|Guan et al. 2025]]). The two fail in different regimes, so hybrids win ([[Arnav2025 - CoT Red-Handed|Arnav et al. 2025]]).
- **The condition is necessity.** When the misbehaviour needs multi-step reasoning, models struggle to hide it ([[Emmons2025 - When Chain of Thought is Necessary, Language Models|Emmons et al. 2025]]). When it does not, the cause is usually left unsaid ([[Chen2025b - Reasoning Models Don't Always Say What They Think|Chen et al. 2025]]).
- **Pooled monitor accuracy hides this.** About 77% of reward hacks are given away by actions alone. On the reasoning-only remainder one rewrite drops the catch rate from about 95% to 4–11% ([[Shiromani2026 - A False Average|Shiromani & Richter 2026]]).
- **Timing is rarely measured, and looks poor when it is.**
  - [[Felicia2026 - StepShield|Felicia et al. 2026]] (StepShield): an 847-rule guardrail has 86% recall but random-level timing. No method combines high recall, low false positives and timely intervention.
  - [[Yan2026b - SafeDream|Yan et al. 2026]] (SafeDream): alarms 1.06–1.20 turns before jailbreak compliance.
  - [[Lin2026c - Forecasting Trajectory-Level Safety Risks in Black-Box|Lin et al. 2026]] (Recast): 88.3% of future safety failures with 2.41 turns of lead time at a 12.3% false-alarm rate.
  - [[Ozmen2026 - PsychoPass|Ozmen & Majumdar 2026]] (PsychoPass): near-perfect attack-outcome classification (AUROC 0.991) was a conversation-length artifact. With length equalised a weaker signal survives (0.65–0.70), and it is already there from the first two to four turns (0.61–0.65).
- **In AI control the predictive element is accumulated suspicion, not a forecast.**
  - The best resampling protocol (resample suspicious actions and re-examine earlier steps) cuts attack success from 58% to 7% at a 5% usefulness cost ([[Bhatt2025 - Ctrl-Z Controlling AI Agents via Resampling|Bhatt et al. 2025]]). [[Lucassen2026 - Retrying vs Resampling in AI Control|Lucassen & Kaufman 2026]] disagrees on how to aggregate the resamples.
  - A running credence about the agent's alignment across tasks picks safer or riskier protocols ([[Wen2024b - Adaptive Deployment of Untrusted LLMs Reduces Distributed|Wen et al. 2024]]).
  - Attacks distributed over several agents can remove the signal from any single trajectory ([[Makins2026 - Multi-Agent AI Control|Makins et al. 2026]]).

## Strand 4: From evaluation to deployment (`pred-eval-to-deployment`)
- **Traffic replay is the strongest forecasting evidence.** [[Williams2026 - Predicting LLM Safety Before Release by Simulating|Williams et al. 2026]] regenerates responses to real production prefixes with the candidate model. Predicted and realised rates correlate at r = 0.91 on a log scale. A public-data version has 1.86× larger errors ([[Sheahan2026 - Can public chat data predict real-world AI misalignments|Sheahan and Carroll 2026]]).
- **It has two weaknesses.** It did not beat the "previous model's rate" baseline overall (p = 0.66). Its largest miss was calculator hacking, predicted 21× too low for one release (1.7 vs 35.2 per 100k) and blamed on how tool calls are replayed; the method had surfaced that behaviour as new before an earlier release.
- **The public-data version is far worse on agentic categories** (errors about 37× larger).
- **Tail extrapolation handles scale but not shift.** [[Jones2025 - Forecasting Rare Language Model Behaviors|Jones et al. 2025]] forecasts from 100–1,000 queries to 10,000–90,000, with 72% of misuse forecasts within one order of magnitude. It under-predicts when deployment contains failure modes absent from the evaluation set ([[Schwarzer2026 - Training ML Models with Predictable Failures|Schwarzer and Niekum 2026]]).
- **Context features as predictors.** [[Jarviniemi2026 - Propensity inference|Järviniemi et al. 2026]] fits regression models over 12 randomised context factors. Goal instructions and goal conflict dominate; threat and oversight effects are small and inconsistent in sign.
- **Propensity is brittle.** One prompt snippet or tool moves scheming from 3% to 59% ([[Hopman2026 - Scheming propensity in LLM agents|Hopman et al. 2026]]), and rates fall toward zero as realism rises ([[Lindner2026 - Gram Assessing sabotage propensities via automated|Lindner, Krakovna and Farquhar 2026]]).
- **Nobody has validated synthetic-scenario scores against real incidents.** A dataset of 698 scheming incidents exists ([[ShafferShane2026 - Scheming in the wild|Shaffer Shane, Mylius and Hobbs 2026]]) but is not joined to evaluation scores.

## Strand 5: Self-prediction and black-box prediction (`pred-self-and-cross-model`)
- **Generic self-report fails.** Across nine behavioural evaluations, direct self-report correlates r = +0.04 with behaviour. Asking about "AI agents in general" does as well, and first-person framing understates harmful behaviour ([[Blandfort2026 - Strangers to Themselves|Blandfort & Pawar 2026]]).
- **Narrow self-prediction works, but weakens where it matters.**
  - Models predict their own refusals at 80–96% accuracy, with sensitivity dropping near the safety boundary ([[Gondil2026 - Do Language Models Know When They'll Refuse|Gondil 2026]]).
  - Stated intentions predict behaviour within one conversation but collapse across sessions for context-driven behaviour such as sycophancy ([[Kocielnik2026 - Rethinking Psychometric Evaluation of LLMs|Kocielnik et al. 2026]]).
  - Stated preferences do not carry into agentic tasks ([[Slama2026 - When Do LLM Preferences Predict Downstream Behavior|Slama et al. 2026]]).
- **Trained self-report mostly discloses during or after the act** ([[Li2025 - Spilling the Beans|Li et al. 2025]], [[Lee2026 - Training Agents to Self-Report Misbehavior|Lee et al. 2026]], [[Joglekar2025 - Training LLMs for Honesty via Confessions|Joglekar et al. 2025]]). One exception lifts an auditor's refusal prediction from 36% to 92% ([[Pres2026 - Self-CTRL|Pres et al. 2026]]).
- **Not found:** verified empirical work on an overseer simulating the untrusted agent's next action, or on asking an agent beforehand about a specific misaligned agentic action and scoring the answer against what it then does.

## Strand 6: Training-time prediction (`pred-training-time`)
- **The task has a benchmark.** [[Chen2026c - Alignment Forecasting|Chen Yueh-Han et al. 2026]] covers over 5,000 questions across 17 models and 16 failure modes. Its decomposed forecaster reaches AUROC 0.801; frontier LLMs reading the data directly score 0.48–0.65.
- **Data-side prediction before training.** Shift along a persona vector correlates with post-fine-tuning trait expression at r = 0.76–0.97, and flags individual samples in real chat data ([[Chen2025 - Persona Vectors|Chen et al. 2025]]).
- **The base model alone predicts which prompts will go wrong** ([[Li2026b - Emergent Misalignment Is Not Magical|Li et al. 2026]], Spearman −0.73 over 12 settings).
- **In-training alarms may not be early.** [[Nghiem2026 - Trait-space Monitoring for Emergent Misalignment During|Nghiem et al. 2026]] reports 0.989 AUROC (1.8% FNR, 2.0% FPR), but the alarm is concurrent with onset: mean lead +0.4 training steps, median 0 (early in 4 of 24 runs, same checkpoint in 16, late in 4). These are the v2 figures; v1 gave 0.990 and +0.8.
- **Some data carries no legible signal:** subliminal learning ([[Cloud2025 - Subliminal Learning|Cloud et al. 2025]]) and inductive backdoors ([[Betley2025b - Weird Generalization and Inductive Backdoors|Betley et al. 2025]]).
- **The outcome label is unreliable.** Standard evaluations miss conditional misalignment ([[Dubinski2026 - Conditional misalignment|Dubinski et al. 2026]]).

## What cuts against the premise
1. **Situation versus intent.** Probes and prefix monitors may read "this is a risky situation", not "this agent is about to misbehave". Those two differ exactly in the cases a second layer is meant to catch.
2. **Base rates.** At an assumed 8% prevalence, two of seven prefix predictors had precision below 50% (44.5% and 34.9%), and every predictor with precision above 70% missed more than a quarter of the cases. Few papers report calibration or matched false-positive budgets.
3. **Confounds in "early" detection:** conversation length, monitors that alarm often, hazard vocabulary, and benchmarks whose state design makes violation inevitable.
4. **Shift.** Tail extrapolation under-predicts when deployment contains failure modes absent from the evaluation set, and forecasts are much worse for agentic settings.
5. **Adaptive agents.** Monitors can be learned around from feedback alone. Almost no predictive guard is tested against an agent that knows it is being forecast. Follow-up 2026-10-02: evasion by non-adversarial agents under feedback is now documented, and a predictive monitor for agent-originated rule violations exists; see [[I4 Routing the predictor to the agent]].

## Gaps that could become a thesis contribution
1. **Lead time for agent-originated misalignment.** Lead-time metrics exist for jailbreaks and tool-use drift, not for scheming, sabotage or reward hacking in multi-step agent trajectories.
2. **Prediction against classification under one budget.** Few papers compare a predictor with an action-level classifier at matched false-positive rates, or measure what the predictor adds *on top of* the classifier.
3. **Signals compared on the same task.** Reasoning-trace, trajectory-prefix, activation and resampling signals have not been compared or combined on one benchmark.
4. **Context features as predictors.** No model predicts misbehaviour rates for unseen scenarios from context features with held-out accuracy reported. This is where the earlier topics connect: pressure and friction levels could be inputs.
5. **Goal drift** has a benchmark ([[Arike2025 - Evaluating Goal Drift in Language Model Agents|Arike et al. 2025]]) but no predictor.

## Links to the earlier topics
- **Stress ([[2026-09-28 Stress and misalignment - literature review]]):** pressure raises misbehaviour in bundled scenarios, but as an isolated predictor it is weak next to goal conflict ([[Jarviniemi2026 - Propensity inference|Järviniemi et al. 2026]]). A predictor would need the motive and the opportunity, not only the stressor.
- **Multi-agent friction ([[2026-09-29 Multi-agent friction - literature review]]):** monitors in that topic classify after the fact and are evaded or socially swayed. Distributed attacks ([[Makins2026 - Multi-Agent AI Control|Makins et al. 2026]]) are the multi-agent form of "no single step is unsafe", which is where look-ahead claims its largest gains.

## Candidate questions (proposals, not yet created)
- **Q8:** Which signals available before the behaviour are used to predict misaligned behaviour, and at what timing?
- **Q9:** How is predictive performance measured (lead time, early-intervention rate, prefix F1, calibration, base-rate-aware precision)?
- **Q10:** Does prediction add safety over action-level classification, and under what conditions?
- **Q11:** What limits prediction (situation versus intent, evasion, distribution shift, evaluation awareness)?
- **Q12:** Do measurable context features such as pressure, oversight and inter-agent friction predict misbehaviour?
- **Q13:** Can the model itself be made aware of its own internal state, by introspection or by feeding a probe reading back to it, and does that improve safety? Scoped in [[2026-10-02 Internal-state awareness - scoping]].

## Most important papers to read first
| Why | Paper |
|---|---|
| States the detection-versus-prediction distinction and measures it | [[Kortukov2026 - Predicting Future Behaviors in Reasoning Models Enables\|Kortukov et al. 2026]] |
| Independent benchmark of predicting from a prefix; the sobering numbers | [[Xu2026 - PreAct-Bench\|Xu et al. 2026]] |
| Makes timing the metric ("when, not whether") | [[Felicia2026 - StepShield\|Felicia et al. 2026]] |
| Cleanest ablation showing anticipation helps a guard | [[Xiong2026 - JANUS\|Xiong et al. 2026]] |
| Probability of reaching a violation, with steps of warning | [[Dhodapkar2026 - SafetyDrift\|Dhodapkar and Pishori 2026]] |
| World-model guardrail for computer-use agents | [[Chen2026b - SafePred\|Chen et al. 2026]] |
| Probe on reasoning activations beats text monitors, early | [[Chan2025 - Can We Predict Alignment Before Models Finish Thinking\|Chan et al. 2025]] |
| Main negative results on probes | [[Boxo2025 - Linear probes rely on textual evidence\|Boxo et al. 2025]], [[Fomin2026 - Internal-state probes read the situation\|Fomin et al. 2026]] |
| Strongest pre-deployment forecast, with honest failure analysis | [[Williams2026 - Predicting LLM Safety Before Release by Simulating\|Williams et al. 2026]] |
| Tail extrapolation of rare behaviours | [[Jones2025 - Forecasting Rare Language Model Behaviors\|Jones et al. 2025]] |
| Self-report does not predict behaviour | [[Blandfort2026 - Strangers to Themselves\|Blandfort & Pawar 2026]] |
| Names and benchmarks training-time forecasting | [[Chen2026c - Alignment Forecasting\|Chen Yueh-Han et al. 2026]] |
| Resampling as a pre-action signal in AI control | [[Bhatt2025 - Ctrl-Z Controlling AI Agents via Resampling\|Bhatt et al. 2025]] |

## Open gaps / next steps
1. Decide which timing the thesis targets. Pre-action and earlier-in-trajectory fit the "second safety layer" framing best.
2. Turn the candidate questions into question notes, then process the priority-1 candidates.
3. Done 2026-10-02: 100 claims across the three session notes were checked against the papers' own text (77 confirmed, 20 imprecise, 2 wrong, 1 unverifiable) and the corrections applied. Both Hills figure pairs are real: 87% → 54% compares two single monitors, 93% → 47% the four-monitor ensemble with the weakest monitor.

## Papers in this topic
![[Papers.base#This topic]]

## Backlog for this topic
![[Backlog.base#This topic]]
