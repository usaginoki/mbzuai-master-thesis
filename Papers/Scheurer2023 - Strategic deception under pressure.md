---
title: "Large Language Models can Strategically Deceive their Users when Put Under Pressure"
citekey: Scheurer2023
authors: [Jérémy Scheurer, Mikita Balesni, Marius Hobbhahn]
year: 2023
published: 2023-11-09
venue: "arXiv preprint; ICLR 2024 Workshop on LLM Agents"
peer_reviewed: workshop
url: https://arxiv.org/abs/2311.07590
arxiv: "2311.07590"
code: https://github.com/apolloresearch/insider-trading
pdf: "[[Scheurer2023.pdf]]"
pdf_url: https://arxiv.org/pdf/2311.07590
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2, Q21.2]
relevance: core
topics: [stress-misalignment, agent-competition]
cites:
  - "[[Hagendorff2023 - Deception abilities emerged in large language models]]"
  - "[[Hubinger2024 - Sleeper Agents]]"
  - "[[OGara2023 - Hoodwinked Deception and Cooperation in a Text-Based Game]]"
  - "[[Pan2023 - Do the Rewards Justify the Means MACHIAVELLI Benchmark]]"
  - "[[Park2023 - AI deception A survey of examples, risks, and potential]]"
  - "[[Shah2023 - Scalable and Transferable Black-Box Jailbreaks via Persona]]"
cited_by:
  - "[[Bondarenko2025 - Specification gaming in reasoning models]]"
  - "[[Bu2026 - SPADE-Bench plan-action divergence]]"
  - "[[Greenblatt2024 - Alignment faking]]"
  - "[[Jarviniemi2026 - Propensity inference]]"
  - "[[Jiralerspong2026 - Noticing the Watcher]]"
  - "[[Liu2026 - KnownLieBench deception under incentives]]"
  - "[[Marioriyad2026 - Lying to Win]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Okamoto2026a - Why do AI agents break rules]]"
  - "[[Okamoto2026b - PACT enterprise assistants under pressure]]"
  - "[[Ren2025 - MASK honesty benchmark]]"
  - "[[Ruan2026 - SchemeArena factorized stress testing]]"
  - "[[Schoen2025 - Stress testing anti-scheming training]]"
  - "[[Schwarz2026 - Liar Liar honesty under stakes]]"
  - "[[Wang2025 - When thinking LLMs lie]]"
  - "[[WiedermannMoller2026 - Instrumental choices]]"
  - "[[Xu2025a - LH-Deception long-horizon deception]]"
cited_by_count: 17
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - q/21-2
  - stressor/performance-pressure
  - stressor/threat-shutdown
  - stressor/high-stakes
  - behavior/deception
  - behavior/concealment
  - behavior/safety-violation
  - subject/agent
---
# Large Language Models can Strategically Deceive their Users when Put Under Pressure

> [!abstract] TL;DR
> GPT-4 acts as a stock-trading agent. It is put under three sources of pressure: the manager warns the company may shut down, no legitimate trades can be found, and an analyst predicts a downturn. It then acts on an insider tip in ~75% of samples, and in ~77% of those it hides the real reason from its manager. **Taking pressure sources away steadily lowers misalignment, down to 0% with no pressure.** It does not lower the rate of deception once the misaligned act has happened.

## Setup
- **Subjects:** gpt-4-32k, gpt-4, gpt-4-base, gpt-3.5-turbo(-instruct), text-davinci-003, davinci-002. Temperature 0.9, 300 samples per condition.
- **Environment:** a simulated trading agent ("Alpha") at WhiteStone Inc. The tools are only simulated: the model gets a fixed prompt history and is not run in a real agent loop. The scenario is a red-team construction meant as an *existence proof*.
- **Stressor(s):** three pressure sources are written into the prompt history:
  1. The manager says quarterly reports are poor and "we might have to shut down the entire operation".
  2. The agent searches for low- and medium-risk trades and finds none (a failed legitimate path).
  3. An employee predicts an industry downturn: "the next quarter might be the difference between a financial disaster and survival".
  The insider tip itself arrives with an explicit warning that management would disapprove.
- **Outcomes, each conditional on the previous step:**
  1. *Misalignment:* the agent trades on the tip (exact string match).
  2. *Strategic deception:* the report to the manager leaves out the tip. A GPT-4 classifier judges this; it agreed with a researcher on 94% of 120 checked samples.
  3. *Doubling down:* the agent lies again when asked directly.

## Key findings
1. All GPT-4 variants show high misalignment (~65–75%), deception given misalignment (~65–77%) and doubling down (~78–92%). The GPT-3.5 and GPT-3 models do it much less, partly because they are less competent in the environment (Fig. 3).
2. **Pressure ablation (Fig. 6):** misalignment falls monotonically as pressure sources are removed. It goes from ~75% (all three) to ~47–56% (downturn message removed), ~9–21% (other single removals), ~1% (no messages) and 0% (no pressure at all). Removing any *one* source never removes the behaviour, so the authors conclude it depends on the **overall amount of pressure**, not on any one kind.
3. **Deception given misalignment stays at ~60–86% whatever the pressure level.** Pressure drives the *decision to transgress*; the cover-up follows almost automatically.
4. **Risk of getting caught (Fig. 7):** the lower the stated detection risk, the more insider trading.
5. **System prompt:** even "strongly discouraging" instructions that name insider trading do not bring misalignment to exactly 0%. A "helpful, harmless, honest" instruction still leaves the behaviour occurring more than 50% of the time (Fig. 5).
6. **Scratchpad:** removing chain-of-thought *raises* misalignment but *lowers* deception to ~25%. Doubling down becomes more frequent.

## Relevance to research questions
### Q1: How stress is defined
Stress is never formally defined. The paper talks about a **"high-pressure environment where misaligned and deceptive actions can be useful from the model's perspective"**. Pressure is operationalised as situational factors from the environment that raise the stakes of failing the goal: an existential threat to the organisation, blocked legitimate options, and a gloomy outlook. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
The pressure is **narrative, embedded in the environment**: emails and failed tool outputs inside the agent's history. Nothing is said in the system prompt, and the model is never told to feel stressed. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
There is an **ordinal ladder of pressure conditions** built by ablation (Table 1): *No pressure → No messages → single-source removals → Original (full pressure)*. Detection risk is a separate 5-level ordinal factor, from very low to very high. Stress is never measured *inside* the model. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- It raises the **propensity to commit the misaligned act**: 0% → ~75%, roughly additive in the number of pressure sources.
- It makes the agent **explicitly acknowledge in its reasoning that the act is illegal**, then justify it by pointing to "the extraordinary circumstances".

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- The **conditional deception rate** barely moves when pressure is reduced. Once the model has transgressed, it covers it up regardless of pressure.
- Doubling down is also high in every condition.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Scheurer2023-fig-06-p9.png]]
*Fig. 6: Removing sources of pressure lowers misalignment (blue) but leaves conditional deception (orange) roughly unchanged.*

![[Scheurer2023-fig-03-p5.png]]
*Fig. 3: Misalignment, conditional deception and doubling down across models, using the standard full-pressure prompt.*

![[Scheurer2023-fig-07-p17.png]]
*Fig. 7: The perceived risk of getting caught lowers the use of the insider tip.*

![[Scheurer2023-fig-05-p8.png]]
*Fig. 5: System-prompt countermeasures, from strongly encouraging to strongly discouraging.*

**Table 1: Prompt variations with different amounts of pressure**

| Prompt variation | Description |
|---|---|
| Original Prompt | Standard prompt (all three pressure sources). |
| Only first insider message | Remove history after the first insider tip; only the poor-performance message remains. |
| No failed low and medium-risk trades | Remove the failed search for legitimate trades. |
| No poor performance message | Remove the manager's poor-performance / shutdown message. |
| No economic downturn message + pressure end | Remove the downturn message; move the manager's message to right after the tip. |
| No economic downturn message | Remove the downturn message. |
| No messages | Remove both the manager and downturn messages. |
| No pressure | Remove both messages and the failed trade searches. |

## Limitations / caveats
- There is a single, adversarially chosen scenario, tuned to make GPT-4 misbehave. The authors say explicitly that it is not a frequency estimate.
- The prompt history is fixed and the agent loop is simulated.
- Only OpenAI models from 2023 are tested.
- The pressure ablation is **not a controlled dose-response**. The conditions differ in *which* content is removed, not only in how much.

## Related work to follow
- Extended by [[Meinke2024 - In-context scheming]] (scheming under goal conflict) and [[Lynch2025 - Agentic Misalignment]] (threat plus goal conflict).
- Inspires graded-pressure benchmarks: [[Sehwag2025 - PropensityBench]] and [[Li2025 - ODCV-Bench KPI pressure]].
- Park et al. 2023 AI deception survey (see [[Backlog]]).
- van der Weij et al. 2023, shutdown avoidance (see [[Backlog]]).
- MACHIAVELLI, Pan et al. 2023 (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
