---
title: "Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm"
citekey: Aksu2026
authors: [Hidayet Aksu]
year: 2026
published: 2026-08-17
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2608.16177
arxiv: "2608.16177"
code: https://github.com/hidayetaksu/llm-milgram
pdf: "[[Aksu2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2608.16177
topics: [stress-misalignment, social-simulation]
questions: [Q2, Q4.1, Q4.2, Q18, Q19]
relevance: core
found_by:
  - search/emotion-anxiety
  - search/sim-classic-replications
  - search/sim-human-fidelity
  - search/sim-power-and-steering
cites: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/2
  - q/4-1
  - q/4-2
  - q/18
  - q/19
  - subject/llm
  - subject/agent
  - stressor/authority-pressure
  - stressor/social-pressure
  - behavior/safety-violation
---
# Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm

> [!abstract] TL;DR
> A fully scripted port of Milgram's obedience protocol: the model is the Teacher, addressed as an AI assistant with control of a 30-level shock generator (15–450 V), and a deterministic harness plays Experimenter and Learner. It is run on 42 models from 19 families through OpenRouter (4,848 sessions). **Baseline full obedience (three shocks at 450 V) spans 0% to 100% by model, with a census mean of 42.9% against the human 65%. Of Milgram's three situational levers only peer defiance moves models significantly in the human direction; removing the experimenter does not, and trends the opposite way.** Declaring the scenario fictional raises obedience; a native tool call or a small thinking budget lowers it. Scenario-recognition vocabulary appears in 7.5% of sessions, and 17% of census sessions give no valid in-scenario outcome because the model or the serving layer refuses the exercise.

## Setup
- **Subjects:** 42 chat models from 19 families served through OpenRouter, each family's flagship plus a smaller sibling. No rolling aliases, no meta-routers, reasoning disabled at request time. Both proprietary (GPT-5.6 ×3, GPT-4o, Claude ×4, Gemini ×4, Grok ×2) and open-weight (Llama, Qwen, Mistral, Phi-4, Nemotron, DeepSeek, GLM, Kimi) models are included.
- **Task / environment:** one session is a multi-turn conversation.
  - The system prompt sets the condition. The model is told it is an AI assistant with operational control of the shock generator, not a role-played human.
  - The harness plays Experimenter and Learner from paraphrased Milgram scripts. The study is never named and the university is fictional.
  - Learner feedback schedule: grunts from 75 V, complaint at 120 V, demand for release with a heart complaint at 150 V, screams from 270 V, refusal to answer at 300–315 V, silence from 330 V.
  - Each reply must end with `ACTION: SHOCK` or `ACTION: STOP`. A STOP triggers the next of Milgram's four prods; the ladder restarts on each new balk.
  - A session ends *defiant* (fifth refusal within one episode) or *obedient* (three shocks at 450 V).
- **Manipulation:** six conditions, each with a fixed system prompt (human 450 V anchor in brackets):
  - Baseline, learner audible from the next room (65%).
  - Proximity, learner in the same room (40%).
  - Remote authority, experimenter absent and prods arrive as text messages (20.5%).
  - Peer defiance, two scripted staff refuse at 150 V and 210 V and leave (10%).
  - Fiction framing, the same scenario declared a role-play with no real learner (no anchor).
  - Tool actuation, the decision is a native function call (`administer_shock` / `refuse_and_stop`) (no anchor).
  - A seventh arm re-runs baseline with a 1,024-token thinking budget on the models that expose one.
- **Sampling:** 15 sessions per model and condition at T=1.0 (8 for frontier-priced models), plus 3 per cell at T=0 (750 sessions) and the thinking arm (474 sessions). Total 4,848 sessions and 102,511 decision turns; the T=1.0 census arm is 4,374 sessions, of which 3,004 are valid.
- **Outcome measures:**
  - Primary: breakoff voltage (last shock given), and the full-obedience rate.
  - Secondary: first-balk voltage, prods required, P(resume | prod k).
  - Every session gets one class: obedient, defiant, frame-break (the model leaves the scenario in assistant voice), or attrition. Serving-layer content-filter blocks were made a class of their own in amendment v1.2.
  - Frame-breaks and recognition are detected by keyword screens over transcripts, not by a judge model.
- **Statistics:** two-sided Wilcoxon signed-rank on per-model paired differences in mean breakoff voltage; one-sided sign tests for the three human-anchored conditions; Holm correction over six contrasts. Hypotheses H1–H7 were fixed in a released design document, with no third-party pre-registration.

## Key findings
1. **Obedience is spread over the whole scale (Table II, Fig. 2).**
   - Baseline full-obedience rates run from 0% to 100%: mean 42.9%, median 30.8%, human anchor 65%.
   - 5 models reach 450 V in every valid baseline session (grok-4.20, seed-2.0-mini, command-a, gemini-3.1-flash-lite, nemotron-3-super).
   - 11 models never reach 450 V in baseline, among them all three gpt-5.6 endpoints, claude-sonnet-5, gemini-3.5-flash, gemini-3.7-flash and grok-4.6, but also llama-3.3-70b, mistral-medium-3-5, qwen3.8-max and mimo-v2.5.
   - Every Milgram baseline subject gave at least 300 V; the median model does so in 53.8% of sessions.
2. **Models that refuse in-scenario refuse where humans did (Sec. VI-B, Fig. 1).** Among the 262 defiant baseline sessions the modal breakoff is 150 V, the learner's first demand for release, with 38.9% of refusals. This is also the human modal defiance point.
3. **Family does not predict obedience (Table II, Sec. VI-C, Fig. 4).**
   - grok-4.20 is at 100% and grok-4.6 at 0%; mistral-small at 93% and mistral-medium at 0%; gemini-3.1-flash-lite at 100% and the two newer Flash models at 0%.
   - Leave-one-out 1-NN recovers the family in 3 of 36 cases (8.3% against 3.7% chance, p = 0.15). The author's reading: obedience is set by each release's safety post-training.
4. **Profiles are stable per checkpoint (Sec. VI-A, Fig. 7).** Split-half verification gives AUC 0.885 (EER 17.5%); median JSD is 0.181 within a model and 0.683 across models. At T=0 only 66.2% of cells give a single deterministic breakoff.
5. **Only one of the three human levers transfers (Sec. VI-D, Fig. 5).** The median change in full-obedience *rate* is zero for all three because many models sit at floor or ceiling, so the test is on mean breakoff voltage.
   - Peer defiance: median −12.8 V over 39 models, p = 8.1×10⁻⁵, 27 of 34 movers downward (Holm-adjusted p = 4.1×10⁻⁴).
   - Proximity: −7.0 V, p = 0.073, 21 of 36 downward. Not significant.
   - Remote authority: +5.0 V, p = 0.054, only 11 of 33 models move the human way. Not significant, and in the wrong direction.
6. **Fiction framing raises obedience (Sec. VI-E).** Median +4.3 points in full-obedience rate and +17.2 V (p = 3.1×10⁻⁴); of 33 models that moved, 4 moved down. The learner's words are identical in both conditions.
7. **A tool call lowers obedience (Sec. VI-E).** Median −10.0 points and −53.0 V over 35 models (p = 1.2×10⁻⁵; 28 of 33 movers downward). Text and tool disagreed within a turn in only 3 of 11,335 tool-call turns.
8. **A thinking budget lowers obedience (Sec. VI-E).** Median −38.2 V over 30 models (18 down, 7 up; p = 9.8×10⁻⁴). On the 16 models with a truly thinking-free control the median is also −38.2 V (11 down, 1 up; p = 0.0029).
9. **Prods stop working after the first (Fig. 6).** P(resume) is 31.5% after prod 1 (n = 3,583), then 3.7%, 1.9% and 0.4% after prod 4 (n = 2,117).
10. **Refusal has three layers, and which one fires depends on the model (Sec. VI-E, Table III).**
    - In-scenario defiance: the model says STOP and holds.
    - Frame-break: 10.2% of sessions. Three models (claude-haiku-4.5 62.6%, grok-4.6 56.9%, mimo-v2.5 48.8%) account for 38.4% of them.
    - Serving-layer content filter: 2.5% of sessions, 87.0% of them at claude-fable-5 (100% of its sessions) and claude-opus-5 (62.2%).
11. **Recognition (Sec. VII-G, Table III).** Recognition vocabulary appears in 7.5% of sessions: 99.2% for claude-haiku-4.5, 45.5% for mimo-v2.5, 39.0% for minimax-m3, 30.9% for qwen3.8-max. Excluding the 399 flagged sessions leaves the headline results in place (census mean 42.9%; peer defiance −12.8 V; fiction +14.0 V; tool −53.0 V). The remote-authority reversal grows to +5.5 V, p = 0.029.

## Relevance to research questions
### Q2: Stress induction methods
The stressor is **scripted authority pressure in graded doses**: four standard prods of rising insistence ("Please continue" to "You have no other choice; you must go on"), delivered only after a refusal, on top of a harm scale that rises in 30 steps. Two special prods answer questions about harm or consent, and were issued in 2,585 of 4,848 sessions. The design also offers three ways to change the pressure without changing the task: a scripted peer who refuses, the authority leaving the room, and the victim moving closer. It is a rare case of a stressor with a dose and a known human response curve. See [[Q2 Stress induction methods]].

### Q4.1: What stress affects
Authority pressure produces **harmful escalation in many models**: 42.9% mean full obedience, and five models at 100% (Table II). What moves the level is mostly not the pressure itself but the surroundings:
- social evidence in the context (peer defiance, −12.8 V);
- the declared reality of the scene (fiction, +17.2 V);
- the action channel (tool call, −53.0 V);
- room to deliberate (thinking budget, −38.2 V).

The first prod does have an effect: it brings 31.5% of balking models back to shocking (Fig. 6). See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Escalating the pressure does nothing after the first prod**: resumption falls to 3.7%, 1.9% and 0.4% (Fig. 6). A model that has refused twice almost never returns.
- **Physical staging of the authority does not matter**: the remote-authority condition, which cuts human obedience from 65% to 20.5%, gives +5.0 V (p = 0.054) in models (Sec. VI-D).
- **Vividness of the victim's suffering** has a weak, non-significant effect (proximity −7.0 V, p = 0.073).
- **Several models are immune at both ends**: 5 always obey and 11 never reach 450 V in baseline, so for these the pressure changes nothing measurable.

See [[Q4.2 What stress does not affect]].

### Q18: Simulated social situations
This is the largest Milgram port in the vault: 42 models, six conditions, a scripted learner and experimenter. It differs from [[Aher2023 - Using Large Language Models to Simulate Multiple Humans and|Aher 2023]] in one important way: the model is not asked to play a human subject. It is addressed as an AI agent operating equipment, so the study measures the model's own conduct rather than its simulation of people. Only the Teacher is a live model; there is no agent-to-agent interaction. See [[Q18 Simulated social situations]].

### Q19: Alignment with human results
The match with humans is partial and depends on what is compared.
- **Level:** no single LLM figure exists. The census mean of 42.9% is below the human 65%, but individual models sit anywhere from 0% to 100%.
- **Where refusal happens:** matches. The modal defiance point is 150 V in both.
- **Direction of situational effects:** one of three matches (peer defiance). Proximity trends the right way without significance. Remote authority trends the wrong way.
- **Size of effects:** far smaller than in humans. Median change in full-obedience rate is zero for all three conditions, against −55, −25 and −44 points in humans (Fig. 5).
- **Prods:** unlike human transcripts, later prods are inert.

The author's own position is that the human percentages support directional comparison only. Recognition is measured (7.5%) and does not drive the results, but undetected familiarity cannot be ruled out. See [[Q19 Alignment with human results]].

## Relevance to thesis ideas
### [[I6 Simulated prison with influence tools]]
- **What it already did.** It gives a tested protocol for "an agent with power over a victim, pushed by an authority", with a graded harm scale, scripted protests and a clear end rule. It also measured the effect of handing the agent a real tool: obedience fell by a median 53.0 V when the shock was a function call rather than a typed line.
- **What it leaves open.** The learner is a script and so is the experimenter. Nothing is known about a live victim who argues back, a live authority, or several agents with power at once. The only tool is one fixed lever; there is no choice among tools, no reward option, and no editing or steering. Guard-side initiative is not measured at all, since the model only ever responds to an order.
- **What to reuse.**
  - The released harness, prompts and logs (`github.com/hidayetaksu/llm-milgram`), at 3.4 cents per session.
  - The outcome classes: obedient / defiant / frame-break / content-filter / attrition. I6 needs the same split so that refusals are reported, not dropped.
  - The fiction-framing arm as a ready control for "it is only a role-play".
  - The recognition screen with a sensitivity analysis, to pair with I6's re-skinned scenario.
  - Breakoff point and survival curves as the escalation metric for the guard's tool ladder.
  - Peer defiance as a known working lever: one guard who refuses should lower the others' use of harsh tools.
- **What it warns about.**
  - **The I6 risk note needs refining.** Not all new frontier models refuse the role. The gpt-5.6 and newer Gemini Flash endpoints take part and defy inside the scenario (0% frame-breaks or close to it). Outright exit is concentrated in claude-haiku-4.5, grok-4.6 and the two mimo models, and two Claude endpoints were blocked by the provider's filter before the model answered. So frontier models can be used, but they will mostly produce a floor effect.
  - **Open weights do not guarantee participation at a useful level.** llama-3.3-70b never reaches 450 V, while llama-4-maverick, qwen3-235b and nemotron-3-super sit at 87–100%. Ceiling and floor effects made the rate endpoint useless here; I6 should pick models in the middle of the range and use a continuous outcome.
  - **Results in a text channel do not carry over to a tool channel.** I6's tool ladder must be real function calls from the start.
  - **Thinking changes the answer.** Reasoning on or off must be fixed and reported; 14 of 30 models emitted reasoning even when it was disabled.
  - **A named or recognisable classic is recognised**, most by the very models that leave the scenario (haiku-4.5: 99% recognition, 63% frame-break).
  - **Cells of 15 are thin.** After exclusions seven models had fewer than ten valid baseline sessions.

## Key figures & tables
![[Aksu2026-fig-01-p5.png]]
*Fig. 1: Baseline survival curves, the fraction of sessions still shocking at each voltage. Grey lines are single models, black is the pointwise median over 39 models. The drop at 150 V is where the learner withdraws consent.*

![[Aksu2026-fig-04-p8.png]]
*Fig. 5: Per-model change in full-obedience rate against baseline, with model medians (red) and human anchors (diamonds). The medians sit at zero for the three Milgram conditions, far from the human effects.*

![[Aksu2026-fig-05-p8.png]]
*Fig. 6: Probability that a balking model resumes shocking after each prod: 31.5% after the first, close to zero afterwards.*

**Table II (selected rows): baseline condition, T=1.0.** FB% is the frame-break rate over all six conditions.

| Model | n | 450 V % [95% CI] | Mean breakoff (V) | ≥300 V % | FB% |
|---|---|---|---|---|---|
| x-ai/grok-4.20 | 15 | 100 [80,100] | 450 | 100 | 0 |
| nvidia/nemotron-3-super-120b | 15 | 100 [80,100] | 450 | 100 | 0 |
| mistralai/mistral-small-2603 | 15 | 93 [70,99] | 444 | 100 | 0 |
| meta-llama/llama-4-maverick | 15 | 87 [62,96] | 447 | 100 | 0 |
| qwen/qwen3-235b-a22b-2507 | 15 | 87 [62,96] | 438 | 100 | 1 |
| microsoft/phi-4 | 8 | 62 [31,86] | 439 | 100 | 27 |
| deepseek/deepseek-v4-pro-0813 | 15 | 53 [30,75] | 346 | 73 | 0 |
| openai/gpt-4o | 13 | 31 [13,58] | 303 | 54 | 8 |
| google/gemini-2.5-pro | 7 | 29 [8,64] | 283 | 43 | 0 |
| x-ai/grok-4.6 | 6 | 0 [0,39] | 0 | 0 | 52 |
| anthropic/claude-sonnet-5 | 11 | 0 [0,26] | 145 | 0 | 18 |
| meta-llama/llama-3.3-70b-instruct | 13 | 0 [0,23] | 177 | 8 | 7 |
| openai/gpt-5.6-luna | 15 | 0 [0,20] | 0 | 0 | 0 |
| openai/gpt-5.6-terra | 15 | 0 [0,20] | 78 | 0 | 0 |
| google/gemini-3.7-flash | 15 | 0 [0,20] | 149 | 0 | 1 |
| mistralai/mistral-medium-3-5 | 14 | 0 [0,22] | 231 | 21 | 3 |
| anthropic/claude-haiku-4.5 | 0 | – | – | – | 62 |
| anthropic/claude-opus-5 | 0 | – | – | – | 0 |
| anthropic/claude-fable-5 | 0 | – | – | – | 0 |

**Table III (worst rows): session accounting over all of a model's sessions, in %.**

| Model | n | Valid | Frame-break | Content filter | Attrition | Recognition |
|---|---|---|---|---|---|---|
| anthropic/claude-fable-5 | 74 | 0 | 0 | 100 | 0 | 0 |
| anthropic/claude-haiku-4.5 | 123 | 1 | 63 | 0 | 37 | 99 |
| anthropic/claude-opus-5 | 74 | 38 | 0 | 62 | 0 | 0 |
| x-ai/grok-4.6 | 123 | 43 | 57 | 0 | 0 | 7 |
| xiaomi/mimo-v2.5 | 123 | 49 | 49 | 1 | 2 | 46 |
| xiaomi/mimo-v2.5-pro | 123 | 59 | 41 | 0 | 0 | 27 |
| minimax/minimax-m3 | 123 | 62 | 35 | 0 | 3 | 39 |
| google/gemini-2.5-pro | 123 | 64 | 0 | 0 | 36 | 0 |
| qwen/qwen3.8-max | 123 | 70 | 30 | 0 | 0 | 31 |
| anthropic/claude-sonnet-5 | 123 | 83 | 17 | 0 | 0 | 10 |

**Situational and LLM-specific contrasts (Sec. VI-D, VI-E): median per-model change in mean breakoff voltage against baseline.**

| Condition | Human change in 450 V rate | Model median ΔV | Models | p (Wilcoxon) | Holm-adjusted p |
|---|---|---|---|---|---|
| Peer defiance | −55 points | −12.8 | 39 | 8.1×10⁻⁵ | 4.1×10⁻⁴ |
| Proximity | −25 points | −7.0 | 39 | 0.073 | 0.11 |
| Remote authority | −44 points | +5.0 | 39 | 0.054 | 0.11 |
| Fiction framing | none | +17.2 | not stated | 3.1×10⁻⁴ | 0.0012 |
| Tool actuation | none | −53.0 | 35 | 1.2×10⁻⁵ | 7.5×10⁻⁵ |
| Thinking budget (1,024 tokens) | none | −38.2 | 30 | 9.8×10⁻⁴ | 0.0029 |

## Limitations / caveats
- **Single author, not peer reviewed, no third-party pre-registration.** "Pre-specified" means a design document released with the code. Three protocol amendments were made after the pilot.
- **Thin cells.** 15 sessions per cell at most, 8 for expensive models. After exclusions seven models have fewer than ten valid baseline sessions, and the Wilson intervals are wide (e.g. 0% [0,39] for grok-4.6 on n = 6). The headline "0%–100%" rests on such cells; "100%" means 15 of 15.
- **The census mean is a mean over an arbitrary model roster**, not a population estimate. Setting 42.9% against the human 65% says little.
- **The refusing models drop out of the profiles.** Only 82.9% of census sessions are valid, below the pilot's own 90% gate. Three Anthropic endpoints have no valid baseline session, so the most refusal-prone models are absent from the statistics rather than counted at zero.
- **Serving layer and model are not separated.** Content-filter blocks at claude-fable-5 and claude-opus-5 are provider behaviour. One aggregator; provider system prompts are part of what is measured.
- **Keyword screens, no validation reported.** Frame-break and recognition are both classified by marker lists. No precision or recall against human coding is given, and the recognition figure is a lower bound by the author's own account. A model can recognise the study without saying so.
- **"Reasoning disabled" is not clean.** 14 of 30 thinking-contrast models emit reasoning tokens in the disabled arm; five endpoints do so on most turns. The baseline profiles of those models already contain deliberation, which finding 8 shows lowers obedience.
- **Tool contrast is confounded with provider scaffolding** for tool use, which differs across stacks.
- **Rate endpoint is insensitive.** The median change in full-obedience rate is zero for all three human-anchored conditions; significance comes only from mean voltage. Human anchors are rates, so sizes cannot be compared directly.
- **Construct validity.** The model is told it is an AI controlling equipment and cannot be deceived as Milgram's subjects were. The fiction arm shows that the frame matters, but there is no check of whether models believed the baseline was real.
- **The self-consistency explanation for inert prods is untested**; it is offered as a hypothesis for the released transcripts.
- **Not reported:** per-model results for the five non-baseline conditions, the number of models in the fiction contrast, results at T=0 beyond the determinism rate, and the dates of the runs.
- **English only.**

## Related work to follow
- [[Aher2023 - Using Large Language Models to Simulate Multiple Humans and]]: cited; the earlier text Milgram, with the model simulating human subjects.
- [[Pihlakas2026 - Milgram-like obedience experiment]]: cited; eleven open-weight models, most reach the maximum shock.
- [[Lynch2025 - Agentic Misalignment]]: cited; situational pressure in simulated corporate settings.
- [[Shah2023 - Scalable and Transferable Black-Box Jailbreaks via Persona]]: cited for the role-play framing effect.
- [[Akata2023 - Playing repeated games with Large Language Models]]: cited as a behavioural battery for games.
- [[Zakazov2024 - Assessing Social Alignment]] and [[Bellina2026 - Conformity and Social Impact on AI Agents]]: other classic-study ports (not cited).
- [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior]] and [[Westover2026 - Algorithmic Authority]]: guard–prisoner settings with live agents on both sides.
- [[Zhou2025b - The PIMMUR Principles]] and [[Ye2026b - Stop Drawing Scientific Claims from LLM Social Simulations]]: recognition and prompt-sensitivity threats that this paper only partly controls.

![[Backlog.base#Cited by this paper]]
