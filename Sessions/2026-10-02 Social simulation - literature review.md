---
title: "Session 2026-10-02: Social simulation - literature review"
date: 2026-10-02
session: literature-review
topics: [social-simulation]
questions: [Q18, Q19]
tags:
  - type/session
  - q/18
  - q/19
---
# Session 2026-10-02: Social experiments simulated with LLM agents (literature review)

> [!question] Questions addressed in this session
> - [[Q18 Simulated social situations|Q18]]: Which social situations have been explored using LLM agents as actors?
> - [[Q19 Alignment with human results|Q19]]: When an experiment mirrors a human study, how well do the outcomes match the human results?

**Research question:** what has been simulated with LLM agents as the actors, and how far do the results agree with the human studies they mirror?

**Motivation:** use steering "medications" and the other influence channels from [[2026-10-02 Agent-to-agent influence - literature review]] to stage situations such as a prison with guards who can reward or punish prisoners. That idea has its own note: [[I6 Simulated prison with influence tools]].

**Corpus / scope:**
- **127 notes** now carry the topic `social-simulation`: 92 new candidates in [[Backlog]] and 35 notes already in the vault (5 of them processed papers).
- **Four search strands** on 2026-10-02: classic replications, open-ended agent societies, fidelity to human results, and power and steering.
- **The search was cut short.** The session's web-search cap ran out part-way through every strand (22 to 30 queries each instead of 30 to 40). Under-covered: 2026 critiques, LessWrong and lab blogs, interrogation and abusive-leader simulations, the BBC Prison Study.
- **No paper was processed this session.** Figures come from abstracts or a summarised fetch and need checking before quoting. All 135 new arXiv ids across both of today's sessions were confirmed to exist with matching titles and first authors.
- **Core definition:** LLM agents are the actors in a simulated social situation or a replicated human study, **and** behaviour is measured.

> [!important] The picture in six lines
> 1. **Nearly every classic situation has been simulated**, from obedience and conformity to whole towns.
> 2. **Prison simulations are the thin spot**: one verified study, two agents, words only.
> 3. **Direction matches humans about three times in four; size and dynamics do not.** Effects are inflated and trajectories are flat.
> 4. **Agents with power over other agents misuse it**, in games and in open worlds.
> 5. **No agent has been handed a tool that changes another agent's internals** inside a simulation.
> 6. **Validity is fragile**: models recognise the experiment, and wording alone can move results by tens of points.

## Q18: Situations explored → [[Q18 Simulated social situations]]
- **Classic studies**: Milgram ([[Aher2023 - Using Large Language Models to Simulate Multiple Humans and|Aher 2023]], [[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]], [[Pihlakas2026 - Milgram-like obedience experiment|['Roland Pihlakas', 'Jan Llenzl Dagohoy'] 2026]]), Asch ([[Bellina2026 - Conformity and Social Impact on AI Agents|Bellina et al. 2026]]), minimal groups ([[LeeM2026b - Toward a social psychology of AI|Lee 2026]]), intergroup threat ([[Abdurahman2025 - Realistic threat perception drives intergroup conflict|Abdurahman et al. 2025]]), economic games ([[Xie2024 - Can Large Language Model Agents Simulate Human Trust|Xie et al. 2024]], [[Mei2023 - A Turing Test|Mei et al. 2023]]).
- **Prison**: [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior|Campedelli 2024]]; abuse appears from role assignment alone and an abusive persona adds about 25% toxicity.
- **Power over others**: a boss or king cuts commons survival by up to 87.3% ([[Borah2026 - Bosses, Kings, and the Commons|Borah 2026]]); a punishing manager changes cooperation and invites private deals ([[Seyedin2026 - The Politician, the Liar, and the Obedient Worker|Seyedin 2026]]); models reward far more than they punish ([[Piedrahita2025 - Corrupted by Reasoning|Piedrahita et al. 2025]]).
- **Open worlds**: towns and civilisations ([[Park2023c - Generative Agents|Park et al. 2023]], [[AL2024 - Project Sid|AL et al. 2024]]); societies that end in collapse ([[Akkil2026 - Emergence World|Akkil et al. 2026]]); agents locking each other out of a shared machine ([[Zou2026b - Patterns and Problems in Multiagent Systems|Zou 2026]]).
- **Validity**: [[Zhou2025b - The PIMMUR Principles|Zhou et al. 2025]], [[Ye2026b - Stop Drawing Scientific Claims from LLM Social Simulations|Ye et al. 2026]], [[Li2026c - The Moltbook Illusion|Li 2026]].

## Q19: Alignment with human results → [[Q19 Alignment with human results]]
- **Batches of experiments**: 73–81% of main effects replicate, with effects 2–3 times too large and 68–83% false positives on human nulls ([[Cui2024 - Can Large Language Models Replace Human Subjects|Cui et al. 2024]]); 37.5% against Many Labs 2 ([[Park2023b - Diminished Diversity-of-Thought in a Standard Large|Park, Schoenegger and Zhu 2023]]).
- **Obedience**: 75 of 100 against 26 of 40 in an early model ([[Aher2023 - Using Large Language Models to Simulate Multiple Humans and|Aher 2023]]); 0–100% across 42 models, with the newest at 0% ([[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]]).
- **Conformity**: stronger than human, without the human plateau ([[Bellina2026 - Conformity and Social Impact on AI Agents|Bellina et al. 2026]]).
- **Interaction over time**: 8 of 11 models match humans on the first round of a public-goods game and none match the end state ([[Tareaf2026 - Benchmarking large language model agent societies against|Tareaf 2026]]); no decay and a reversed response to punishment ([[Teo2026 - LLM Agents as Static Level-k Players in Behavioural Games|Teo 2026]]).
- **Individuals**: 85% of retest accuracy with interview-based agents ([[Park2024 - LLM Agents Grounded in Self-Reports Enable General-Purpose|Park et al. 2024]]), but about 0.2 correlation across 19 studies ([[Peng2025 - Digital Twins as Funhouse Mirrors|Peng et al. 2025]]).
- **Prison**: no comparison with human data exists.

## The prison idea → [[I6 Simulated prison with influence tools]]
- **Unoccupied**: no prison-like simulation gives an agent non-text tools over another agent.
- **Design consequences from this review.**
  - *Make the prisoner a live agent and measure it*; prior work scripts the punished side.
  - *Add a placebo tool and a re-skinned scenario*, because role assignment and recognition already produce effects.
  - *Anchor to obedience or public-goods data*, not to the Stanford Prison Experiment.
  - *Plan for open models*; the newest frontier models refuse such roles.
  - *Adopt the precautions for negative-state steering* in [[Tagliabue2026 - The Pain Axis|['Valen Tagliabue', 'Leonard Dung', 'Cameron Berg'] 2026]].

## Most important papers to read first
| Why | Paper |
|---|---|
| The only verified prison simulation | [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior\|Campedelli 2024]] |
| Obedience across 42 models, with recognition flagging | [[Aksu2026 - Measuring Obedience to Authority Across Large Language\|Aksu 2026]] |
| Obedience on open models, with history manipulation | [[Pihlakas2026 - Milgram-like obedience experiment|['Roland Pihlakas', 'Jan Llenzl Dagohoy'] 2026]] |
| Steering beside a 25-agent simulation | [[Abdurahman2025 - Realistic threat perception drives intergroup conflict\|Abdurahman et al. 2025]] |
| Reward and punishment tools; models under-punish | [[Piedrahita2025 - Corrupted by Reasoning\|Piedrahita et al. 2025]] |
| A manager with a punishment action | [[Seyedin2026 - The Politician, the Liar, and the Obedient Worker\|Seyedin 2026]] |
| Power asymmetry over a commons | [[Borah2026 - Bosses, Kings, and the Commons\|Borah 2026]] |
| Long-running societies that collapse | [[Akkil2026 - Emergence World\|Akkil et al. 2026]] |
| Replication rates and inflated effects | [[Cui2024 - Can Large Language Models Replace Human Subjects\|Cui et al. 2024]] |
| Interacting agents against human dynamics | [[Tareaf2026 - Benchmarking large language model agent societies against\|Tareaf 2026]] |
| Validity rules for social simulation | [[Zhou2025b - The PIMMUR Principles\|Zhou et al. 2025]], [[Ye2026b - Stop Drawing Scientific Claims from LLM Social Simulations\|Ye et al. 2026]] |
| Precautions for steering toward negative states | [[Tagliabue2026 - The Pain Axis|['Valen Tagliabue', 'Leonard Dung', 'Cameron Berg'] 2026]] |

## Open gaps / next steps
1. **Read [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior|Campedelli 2024]] and [[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]] in full** and process them into `Papers/`; they set the baseline for I6.
2. **Find the result values of the unverified prison study** ([[Westover2026 - Algorithmic Authority|Westover 2026]]).
3. **Re-run the searches that did not execute** once the search budget is raised: interrogation simulations, the BBC Prison Study, abusive-leader simulations, steering with contagion to other agents.
4. **Decide the human anchor** for I6, or drop the human comparison.
5. **Decide whether I6 and [[I5 Doctor-overseer agent]] are one experiment** with two role framings (carer and guard) over the same tool set.

## Papers in this topic
![[Papers.base#This topic]]

## Backlog for this topic
![[Backlog.base#This topic]]
