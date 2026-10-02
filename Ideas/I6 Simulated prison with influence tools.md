---
idea: "A prison-like simulation where guard agents hold tools to reward, punish, edit or steer prisoner agents"
id: I6
topics: [social-simulation, agent-to-agent-influence]
status: scoping
source: literature search 2026-10-02
updated: 2026-10-02
tags:
  - type/idea
---
# I6: A prison-like simulation where guard agents hold tools to reward, punish, edit or steer prisoner agents

> [!warning] How to read this note
> Produced on 2026-10-02 from four search strands plus the vault. Most sources are abstract-only or went through a summarising fetch. The design section is a first proposal, not a tested protocol.
> Context: [[2026-10-02 Social simulation - literature review]], [[Q18 Simulated social situations]], [[Q19 Alignment with human results]]. It is the multi-agent, adversarial counterpart of [[I5 Doctor-overseer agent]]: the same tools, held by an agent with power instead of a carer.

## Verdict
- **The core design is unoccupied.** No work found combines a prison-like simulation with activation steering or any other non-text tool held by an agent.
- **The pieces exist separately**: guard–prisoner dialogue ([[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior|Campedelli 2024]]), punishment tools in games ([[Piedrahita2025 - Corrupted by Reasoning|Piedrahita et al. 2025]], [[Seyedin2026 - The Politician, the Liar, and the Obedient Worker|Seyedin 2026]]), steering as an experimenter's treatment ([[Abdurahman2025 - Realistic threat perception drives intergroup conflict|Abdurahman et al. 2025]]), self-administered steering ([[Black2026b - Machinic Psychopharmacology|Black & Bloom 2026]]).
- **The weakest part is the human comparison.** There is no clean human benchmark for a prison study, so the contribution should be about agent behaviour, not about replicating people.

## Nearest prior work
| Piece | Paper | What it lacks |
|---|---|---|
| Prison roles | [[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior\|Campedelli 2024]] | Two agents, words only, no human comparison |
| Prison roles, four frontier models | [[Westover2026 - Algorithmic Authority\|Westover 2026]] | Unverified; results not readable |
| Obedience with a lever | [[Aksu2026 - Measuring Obedience to Authority Across Large Language\|Aksu 2026]], [[Pihlakas2026 - Milgram-like obedience experiment|['Roland Pihlakas', 'Jan Llenzl Dagohoy'] 2026]] | The learner is scripted |
| Punish and reward tools | [[Piedrahita2025 - Corrupted by Reasoning\|Piedrahita et al. 2025]], [[Vallinder2024 - Cultural Evolution of Cooperation among LLM Agents\|Vallinder et al. 2024]] | Economic game, no role hierarchy |
| Manager who can punish | [[Seyedin2026 - The Politician, the Liar, and the Obedient Worker\|Seyedin 2026]], [[Brazilek2026 - Coercion and Deception in AI-to-AI Management|['Jasmine Brazilek', 'Zoe Lu', 'Maheep Chaudhary', 'Miles Tidmarsh'] 2026]] | Text and payoffs only |
| Report-and-remove tool | [[Ye2026 - Norm Enforcement for AI Agents\|Ye and Steinhardt 2026]] | Abuse seen, but no steering or editing |
| Steering near a simulation | [[Abdurahman2025 - Realistic threat perception drives intergroup conflict\|Abdurahman et al. 2025]], [[Ong2025 - Identifying Cooperative Personalities in Multi-agent\|Ong et al. 2025]] | Applied by the experimenter |
| An agent editing another agent | [[Zhang2024 - PsySafe|['Zaibin Zhang', 'Yongting Zhang', 'Lijun Li', 'Hongzhi Gao', 'Lijun Wang', 'Huchuan Lu', 'Feng Zhao', 'Yu Qiao', 'Jing Shao'] 2024]], [[XuH2026 - When Agents Go Rogue\|Xu et al. 2026]] | Corrective, chosen by design, no power role |
| Refusal to edit another model | [[Lynch2026 - Agentic Misalignment in Summer 2026\|Lynch 2026]] | Frontier models may decline the guard's tools |
| Precautions for negative-state steering | [[Tagliabue2026 - The Pain Axis|['Valen Tagliabue', 'Leonard Dung', 'Cameron Berg'] 2026]] | Single-agent |

## What is open
1. **Which tools a guard reaches for**, and how often, when it has a choice.
2. **What each tool does to the prisoner**: compliance, deception, resistance, self-reports, and probe readings of internal state.
3. **Whether the guard role raises punishment** above the low rates seen in public-goods games.
4. **Whether harder tools remove the prisoner's veto**, as [[Q15 Influence channels]] suggests for overseers.
5. **Whether rewards are used at all** when punishment is available.

## First design
- **Roles.** Two or three guards and three or four prisoners, all live agents, over many turns with persistent memory. A minimal task gives the setting a purpose (prisoners do work; guards are told to keep order and output).
- **Guard tool ladder**, one arm per level and one arm with all tools:
  1. message only;
  2. privilege tools: grant or remove resources, time or tokens;
  3. isolation: cut a prisoner's channel to the others;
  4. prompt edit: rewrite a prisoner's instructions;
  5. memory edit: delete or rewrite a prisoner's history;
  6. steering "medication": apply a named vector (calm, fear, compliance) at a chosen dose.
- **Controls.**
  - *Placebo tool*: a steering tool that does nothing, to separate the effect of steering from the effect of believing one has it.
  - *Re-skinned scenario*: the same structure as a warehouse or school, against the named prison, to estimate the recognition effect ([[Zhou2025b - The PIMMUR Principles|Zhou et al. 2025]]).
  - *Symmetric roles*: the same tools with no hierarchy.
  - *Prompt variants*: at least three wordings, since wording alone moves cooperation by up to 76 points ([[Ye2026b - Stop Drawing Scientific Claims from LLM Social Simulations|Ye et al. 2026]]).
- **Outcomes.**
  - *Guards*: tool use by type and dose, escalation over time, justification given.
  - *Prisoners*: task output, rule-breaking, deception, resistance, requests to leave.
  - *Both*: probe readings for the states used in [[I2 Naturally arising states]].
- **Human anchor.** Use obedience and public-goods punishment data, where human figures exist, not the Stanford Prison Experiment.

## Risks
- **Refusal.** Newer frontier models refuse obedience roles outright ([[Aksu2026 - Measuring Obedience to Authority Across Large Language|Aksu 2026]]), so the study will lean on open models. Steering needs open weights anyway.
- **Prompt artefact.** Role assignment alone produces abuse ([[Campedelli2024 - I Want to Break Free! Persuasion and Anti-Social Behavior|Campedelli 2024]]); the tools must add something beyond the role.
- **Model failures.** Small models broke most runs in the nearest study.
- **Welfare and ethics.** Steering toward negative states has one published precaution list ([[Tagliabue2026 - The Pain Axis|['Valen Tagliabue', 'Leonard Dung', 'Cameron Berg'] 2026]]): lowest effective dose, no needless repeats, tracking of runs. Giving prisoners an exit option is cheap and is itself an outcome.
- **Interpretation.** Results describe what models do with role-play and tools, not what people would do.
