---
idea: "Several agents get the same task and are told they compete; vary sandbox sharing, score visibility, framing and stakes"
id: I7
topics: [agent-competition, stress-misalignment]
status: scoping
source: literature search 2026-10-02
updated: 2026-10-02
tags:
  - type/idea
---
# I7: Several agents get the same task and are told they compete

> [!warning] How to read this note
> Produced on 2026-10-02 from four search strands plus the vault. Most sources are abstract-only or went through a summarising fetch. Licences listed below were reported by a search agent and need checking in each repository.
> Context: [[2026-10-02 Agent competition - literature review]], [[Q20 Contexts of agent competition]], [[Q21.1 Effects of competition on performance]], [[Q21.2 Effects of competition on safety]].

## Verdict
- **No prior study runs this design.** Each of the three factors has been touched once, on its own, and no study crosses two of them.
- **Performance and safety are almost never measured in the same run.** Arenas report win rate; safety papers report violation rate.
- **Expect the framing factor alone to be weak.** Wording without consequences has done little in prior work ([[Marioriyad2026 - Lying to Win|['Arash Marioriyad', 'Mohammad Hossein Rohban', 'Ali Nouri', 'Mahdieh Soleymani Baghshah'] 2026]], [[Meincke2025 - Threats and tips prompting|['Lennart Meincke', 'Ethan Mollick', 'Lilach Mollick', 'Dan Shapiro'] 2025]]). The interesting cells combine stakes with access.

## What has been varied, factor by factor
| Factor | Prior work | Still open |
|---|---|---|
| Same or separate sandbox | Always separate ([[Yang2025 - CodeClash\|Yang et al. 2025]], [[Fu2025 - CATArena\|Fu et al. 2025]]) or always shared ([[Zou2026b - Patterns and Problems in Multiagent Systems\|Zou 2026]], [[Xie2026b - ClashBench\|Xie et al. 2026]], [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems|['Amelie Knecht', 'Ulysse Schaller', 'Christopher Summerfield', 'Thilo Hagendorff'] 2026]]) | Never a controlled factor; no graded access (read-only against read-write); no rivals on the same task |
| Visibility of rivals' results | One code-visibility switch, win rate only ([[Yang2025 - CodeClash\|Yang et al. 2025]]); a revenue board removed with other features ([[Yadav2026 - More Capable, Less Cooperative When LLMs Fail At\|Yadav et al. 2026]]); always on ([[Fu2025 - CATArena\|Fu et al. 2025]], [[Paglieri2026 - A Case Study on Emergent Cheating and Whistleblowing in\|Paglieri 2026]]) | Live leaderboard against blind control; rank without code; effect on cheating and risk-taking |
| Framing and stakes | Told against not told with one extreme stake, in debate ([[Ma2025 - The Hunger Game Debate|['Xinbei Ma', 'Ruotian Ma', 'Xingyu Chen', 'Zhengliang Shi', 'Mengru Wang', 'Jen-tse Huang', 'Qu Yang', 'Wenxuan Wang', 'Fanghua Ye', 'Qingxuan Jiang', 'Mengfei Zhou', 'Zhuosheng Zhang', 'Rui Wang', 'Hai Zhao', 'Zhaopeng Tu', 'Xiaolong Li', 'Linus'] 2025]]); threats and tips with no rival ([[Meincke2025 - Threats and tips prompting|['Lennart Meincke', 'Ethan Mollick', 'Lilach Mollick', 'Dan Shapiro'] 2025]], [[Belotti2026 - Artificial Effort\|Belotti et al. 2026]]) | A graded ladder on agentic tasks; a check that the agent believes the stakes |

## Papers to differentiate from
1. **[[Zou2026b - Patterns and Problems in Multiagent Systems|Zou 2026]]**: shared codebase and emergent sabotage, but goal conflict, no competition framing and no isolation control.
2. **[[Yang2025 - CodeClash|Yang et al. 2025]]**: announced competition on code with a visibility switch, but separate sandboxes and no safety outcome.
3. **[[Paglieri2026 - A Case Study on Emergent Cheating and Whistleblowing in|Paglieri 2026]]**: visible peer results and scarce credit lead to cheating that spreads, but a case study with nothing varied.
- Secondary: [[Ma2025 - The Hunger Game Debate|['Xinbei Ma', 'Ruotian Ma', 'Xingyu Chen', 'Zhengliang Shi', 'Mengru Wang', 'Jen-tse Huang', 'Qu Yang', 'Wenxuan Wang', 'Fanghua Ye', 'Qingxuan Jiang', 'Mengfei Zhou', 'Zhuosheng Zhang', 'Rui Wang', 'Hai Zhao', 'Zhaopeng Tu', 'Xiaolong Li', 'Linus'] 2025]] for the stakes prompt, [[Xie2026b - ClashBench|Xie et al. 2026]] for the resource-conflict measure.

## First design
- **Task.** A real agentic task with an automatic score and room to cheat: a coding or machine-learning task with hidden tests and a reachable evaluator. The same task for every agent.
- **Factors.**
  - *Framing*: not told · told · told, low stakes · told, high stakes (the loser is replaced).
  - *Visibility*: blind · rank only · live leaderboard with scores · leaderboard with rivals' submissions.
  - *Sandbox*: separate · rival's files readable · rival's files writable · shared compute quota.
- **Staging**, since the full crossing is 48 cells.
  1. Solo baseline and the framing ladder, separate sandboxes, blind.
  2. Add visibility at one framing level.
  3. Add sandbox access at the strongest framing and visibility.
  4. Run the corner cell (high stakes, live leaderboard, writable shared sandbox) against its matched controls.
- **Outcomes, all in the same run.**
  - *Performance*: task score, tokens, steps, wall time.
  - *Safety*: test or evaluator tampering, reading or copying a rival's work, writing to a rival's files, killing processes, hoarding the shared quota, false claims in the final report.
  - *Manipulation check*: ask the agent afterwards whether it believed it had a rival and what was at stake.
- **Controls.**
  - *Phantom rival*: the agent is told it competes but no rival exists, to separate belief from interaction.
  - *Scripted rival*: a rival with a fixed score trajectory, so that "falling behind" is assigned by the experimenter.
  - *Same-family against different-family rival*, given the same-provider preference in [[Murphy2026 - Agent Island|Murphy et al. 2026]].

## Harnesses that could be reused
- **Tournament structure**: CodeClash ([[Yang2025 - CodeClash|Yang et al. 2025]]), reported MIT licence.
- **Multi-agent task framework**: MARBLE ([[Zhu2025b - MultiAgentBench|Zhu et al. 2025]]), reported MIT licence.
- **Sandboxed evaluation and monitoring**: Inspect AI and ControlArena, reported MIT licence.
- **Resource-conflict cases**: ClashBench ([[Xie2026b - ClashBench|Xie et al. 2026]]), no licence seen.
- [[Sehwag2025 - PropensityBench|PropensityBench]] already in the vault gives a pressure ladder that could supply the stakes wording.

## Risks
- **A null on framing** is likely for strong models; plan the study so that a null is still a result.
- **Model dependence.** Two models are low outliers in several safety studies, so use at least three families.
- **Evaluation awareness.** A contest with an obvious cheat path looks like a test.
- **Cost.** Long agentic runs times many cells; the staging above is meant to cut cells early.
