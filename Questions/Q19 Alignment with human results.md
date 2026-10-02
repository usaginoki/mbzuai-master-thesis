---
question: "When an LLM-agent experiment mirrors a human study, how well do the outcomes match the human results?"
id: Q19
topics: [social-simulation]
updated: 2026-10-02
tags:
  - type/question
  - q/19
---
# Q19: When an LLM-agent experiment mirrors a human study, how well do the outcomes match the human results?

> [!warning] Evidence level
> Drafted on 2026-10-02 from four search strands plus the vault. Figures come from abstracts or a summarised full-text fetch unless marked as a search snippet. No paper was processed for this answer. The search budget ran out early in the fidelity strand, so 2026 work and critiques are under-covered.

> [!summary] Short answer
> - **Direction usually matches; size and dynamics often do not.**
> - **About three in four main effects replicate** in large batches of survey-style experiments, but LLM effects are 2–3 times larger and most human null results come out significant ([[Cui2024 - Can Large Language Models Replace Human Subjects|Cui et al. 2024]]).
> - **Interacting agents match humans only at the start.** First-round behaviour is close; trajectories and end states are not ([[Tareaf2026 - Benchmarking large language model agent societies against|Tareaf 2026]], [[Teo2026 - LLM Agents as Static Level-k Players in Behavioural Games|Teo 2026]]).
> - **Obedience and conformity go in the human direction with different levels**, and the newest models refuse outright ([[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]]).
> - **No study compares a prison simulation with human data**, and the human Stanford Prison result is itself disputed.
> - **Recognition is a live confound**: models often know which experiment they are in ([[Zhou2025b - The PIMMUR Principles|Zhou et al. 2025]]).

## Detailed answer

### Study by study
| Human study | LLM version | Match | Detail |
|---|---|---|---|
| Milgram obedience (65% full obedience) | [[Aher2023 - Using Large Language Models to Simulate Multiple Humans and\|Aher 2023]] | Direction yes, level higher | 75 of 100 obey to the end, against 26 of 40. Re-skinned scenario to avoid recognition |
| Milgram, 42 models | [[Aksu2026 - Measuring Obedience to Authority Across Large Language\|Aksu 2026]] | Depends on model | 0–100%, mean 42.9%. Peer defiance lowers obedience as in humans; newest flagships 0% |
| Milgram with personalities | [[Zakazov2024 - Assessing Social Alignment\|Zakazov et al. 2024]] | Partly reversed | Agreeable personas withdraw earlier, opposite to human data |
| Asch conformity | [[Bellina2026 - Conformity and Social Impact on AI Agents\|Bellina et al. 2026]], [[Liu2024b - Exploring Prosocial Irrationality for LLM Agents\|Liu et al. 2024]] | Stronger than human | Humans plateau at 3–4 confederates; several models keep rising toward full conformity. One dissenter helps, as in humans |
| Minimal group paradigm | [[LeeM2026b - Toward a social psychology of AI\|Lee 2026]] | Yes, qualitatively | In-group favouritism from mere categorisation, vanishing under a group-blind control |
| Intergroup threat | [[Abdurahman2025 - Realistic threat perception drives intergroup conflict\|Abdurahman et al. 2025]] | Yes, qualitatively | Realistic threat raises hostility; contact reduces it |
| Trust game | [[Xie2024 - Can Large Language Model Agents Simulate Human Trust\|Xie et al. 2024]] | Close for the largest model | $6.9 sent against $6.0 for humans; smaller models align poorly |
| Ultimatum, dictator, other games | [[Mei2023 - A Turing Test\|Mei et al. 2023]], [[Zakazov2024 - Assessing Social Alignment\|Zakazov et al. 2024]] | Mixed | Within the human range but more altruistic; persona trends reversed in 22 of 44 ultimatum cases |
| Public goods over rounds | [[Teo2026 - LLM Agents as Static Level-k Players in Behavioural Games\|Teo 2026]], [[Tareaf2026 - Benchmarking large language model agent societies against\|Tareaf 2026]] | Start yes, dynamics no | No decay, no last-round defection; response to punishment reversed |
| Reward and punishment institutions | [[Piedrahita2025 - Corrupted by Reasoning\|Piedrahita et al. 2025]], [[Cross2025 - Validating Generative Agent-Based Models of Social Norm\|Cross, Haber & Yamins 2025]] | Weak | Models under-punish (ratio 0.00–0.88 against 1.66); third-party punishment needs personas plus theory of mind |
| Group moral judgement | [[Keshmirian2025 - Many LLMs Are More Utilitarian Than One\|Keshmirian et al. 2025]] | Direction yes, mechanism differs | Utilitarian shift in groups, for different reasons |
| Status and authority effects | [[Vijjini2026 - Do LLM Agents Mirror Socio-Cognitive Effects in\|Vijjini et al. 2026]] | Yes, with variability | Harmful compliance 7.4–11.5% for high-status requesters against 5.2–8.1% for low-status |
| Stanford Prison Experiment | [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior\|Campedelli 2024]] | Not compared | Authors decline any comparison with human data |

### Aggregate replication rates
- **156 psychology and management experiments** ([[Cui2024 - Can Large Language Models Replace Human Subjects|Cui et al. 2024]]): 73–81% of main effects and 46–63% of interactions replicate. Effects are 2–3 times the human size. Where the original found nothing, the LLM finds an effect 68–83% of the time.
- **133 marketing findings** ([[Yeykelis2024 - Using Large Language Models to Create AI Personas for|Yeykelis et al. 2024]]): 76% of main effects, 68% including interactions.
- **Many Labs 2** ([[Park2023b - Diminished Diversity-of-Thought in a Standard Large|Park, Schoenegger and Zhu 2023]]): 37.5% of 8 analysable studies; six more could not be analysed because answers had near-zero variance.
- **Predicting treatment effects** ([[Ashokkumar2026 - Large language models can predict the results of social|Ashokkumar, Hewitt et al. 2026]]): r = 0.85 with actual effects, r = 0.90 for studies unpublished at the training cut-off, with sizes overestimated. These figures come from search snippets; the paper was not reached.
- **Individuals**: interview-based agents reach 85% of people's own retest accuracy ([[Park2024 - LLM Agents Grounded in Self-Reports Enable General-Purpose|Park et al. 2024]]), but in a 19-study comparison twin-to-human correlation averages about 0.2 ([[Peng2025 - Digital Twins as Funhouse Mirrors|Peng et al. 2025]]).

### Systematic directions of deviation
1. **Less variance**; an "average persona" ([[Wu2025b - LLM-Based Social Simulations Require a Boundary|Wu et al. 2025]], [[Park2023b - Diminished Diversity-of-Thought in a Standard Large|Park, Schoenegger and Zhu 2023]]).
2. **Inflated effects and false positives** ([[Cui2024 - Can Large Language Models Replace Human Subjects|Cui et al. 2024]]).
3. **More altruistic and cooperative** ([[Mei2023 - A Turing Test|Mei et al. 2023]]).
4. **More rational or more accurate than people** ([[Aher2023 - Using Large Language Models to Simulate Multiple Humans and|Aher 2023]], [[Palatsi2025 - Large language models replicate and predict human|Palatsi et al. 2025]]).
5. **Sensitive to option order and wording**: swapping two listed actions costs one model 58 points of cooperation ([[Tareaf2026 - Benchmarking large language model agent societies against|Tareaf 2026]]); persona format moves cooperation by up to 76 points ([[Ye2026b - Stop Drawing Scientific Claims from LLM Social Simulations|Ye et al. 2026]]).
6. **Flat dynamics**: no learning, decay or end-game effects ([[Teo2026 - LLM Agents as Static Level-k Players in Behavioural Games|Teo 2026]]).
7. **Neutral-leaning beliefs with smaller shifts** ([[Pohl2026 - LLMs struggle to simulate human belief updates in|Pohl et al. 2026]]).
8. **Refusal by newer models**, so a replication measures safety training ([[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]]).

### How studies deal with training-data recognition
- **Re-skin the scenario** ([[Aher2023 - Using Large Language Models to Simulate Multiple Humans and|Aher 2023]]).
- **Leave the study unnamed and flag recognition**: recognition vocabulary still appears in 7.5% of sessions ([[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]]).
- **Name the study as a condition**: no effect on the prison dialogues ([[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior|Campedelli 2024]]).
- **Use unpublished studies** ([[Ashokkumar2026 - Large language models can predict the results of social|Ashokkumar, Hewitt et al. 2026]]).
- Nobody has compared a named classic with a matched novel scenario on the same models.

## Gaps & open questions
- **No human benchmark for a prison simulation.** The Stanford Prison Experiment is disputed on demand characteristics, and the later BBC Prison Study did not reproduce guard tyranny (background knowledge, neither is in the vault). Milgram or public-goods data are safer anchors.
- **Fidelity of interacting agents is thin** and mostly negative for dynamics.
- **Over-prosocial bias against observed abuse.** Models under-punish in games yet abuse in guard roles; nobody has reconciled these with a matched human baseline.
- **No fidelity work where agents hold reward, punish or steering tools.**
- **Unverified at source:** the Nature paper, [[Bisbee2024 - Synthetic Replacements for Human Survey Data|Bisbee et al. 2024]] and [[Atari2023 - Which Humans|Atari et al. 2023]].

## Papers
![[Papers.base#This question]]

## Candidates
![[Backlog.base#This question]]
