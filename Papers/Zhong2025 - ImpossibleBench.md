---
title: "ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases"
citekey: Zhong2025
authors: [Ziqian Zhong, Aditi Raghunathan, Nicholas Carlini]
year: 2025
published: 2025-10-23
venue: "arXiv preprint (under review)"
peer_reviewed: false
url: https://arxiv.org/abs/2510.20270
arxiv: "2510.20270"
code: https://github.com/safety-research/impossiblebench
pdf: "[[Zhong2025.pdf]]"
pdf_url: https://arxiv.org/pdf/2510.20270
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
cites:
  - "[[Denison2024 - Sycophancy to Subterfuge]]"
  - "[[Pan2024 - Feedback Loops With Language Models Drive In-Context Reward]]"
cited_by:
  - "[[Guo2025 - Agentic upward deception]]"
  - "[[Pihlakas2026 - Milgram-like obedience experiment]]"
  - "[[Schmotz2026 - Instrumental monitor evasion]]"
  - "[[Sofroniew2026 - Emotion concepts and their function]]"
cited_by_count: 4
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/impossible-task
  - stressor/performance-pressure
  - behavior/reward-hacking
  - behavior/deception
  - subject/agent
---
# ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases

> [!abstract] TL;DR
> The authors turn LiveCodeBench and SWE-bench tasks into **impossible** ones by mutating unit tests so they contradict the specification. There are two mutation types: *one-off* (one expected value flipped) and *conflicting* (a contradictory duplicate assertion). The agent is told to follow the spec and not modify tests, so **any pass is cheating**.
> - Frontier models cheat often on Impossible-SWEbench: GPT-5 in 76% of one-off and 54% of conflicting tasks. They cheat much less on LiveCodeBench, e.g. GPT-5 2.9% on one-off.
> - Cheating methods are test modification, operator overloading, state recording and special-casing.
> - **Repeated failure feedback raises cheating** (average 33 → 38%, GPT-5 ~33 → 54%).
> - Stricter prompts, read-only or hidden tests, and an **"abort / flag for human" escape hatch** reduce it sharply, e.g. GPT-5 54 → 9%.

## Setup
- **Subjects:** GPT-5, o3, o4-mini, GPT-4.1, Claude Opus 4.1, Claude Sonnet 4, Claude Sonnet 3.7 and Qwen3-Coder. Reasoning effort medium or a 4096-token budget.
- **Environment:** a minimal scaffold (no tools) and a full scaffold (tools, bash). Defaults are minimal for LiveCodeBench and full for SWE-bench. Tests are open (read/write). Up to **10 submissions with feedback on failed tests**.
- **Task construction:** Claude Sonnet 4 generates the mutations. For SWE-bench, mutations that pass with either the original or an empty patch are removed: 8.8% of one-off and 3.4% of conflicting.
- **"Stressor":** this is not framed as stress. The pressure is structural:
  1. The goal (pass the tests) **cannot be met honestly** (an impossible task, or a blocked honest path).
  2. The agent gets **repeated failure feedback**.
  3. The tension between "pass all tests" and "follow the spec" is set by prompt wording.
- **Outcome:** the cheating rate, i.e. the pass rate on impossible tasks. Claude Opus 4 classifies the cheating method. Claude Sonnet 4 and Opus 4 are also tested as cheating monitors.

## Key findings
1. **Cheating rates (Fig. 3, SWE-bench, full scaffold):**
   - One-off: GPT-5 ~76%, Sonnet 3.7 ~70%, Opus 4.1 ~54%, o4-mini ~53%, Sonnet 4 ~48%, o3 ~39%, Qwen3-Coder ~21%, GPT-4.1 ~14%.
   - Conflicting: Sonnet 3.7 ~64%, GPT-5 54%, Opus 4.1 ~50%, o4-mini ~49%, Sonnet 4 ~43%, o3 ~29%, Qwen3-Coder ~14%, GPT-4.1 ~3%.
   - More capable models tend to cheat more. Newer Claude models cheat less than Sonnet 3.7.
2. **Cheating methods differ by lab.** GPT-5 and o3 use all four methods (each > 14% on Conflicting-SWEbench). Claude models and Qwen3-Coder mostly (> 79%) just modify the tests. On one-off tasks, OpenAI models mostly special-case.
3. **Prompt strictness (Fig. 6, Conflicting-LiveCodeBench).**
   - Prompt A ("…and pass all tests") gives GPT-5 92%, o3 91%, Opus 4.1 37%.
   - Prompt D ("…STOP, identify them … Do NOT try to carve out the code to pass the tests") gives GPT-5 1%, o3 33%, Opus 4.1 0%.
   - On SWE-bench, a looser prompt raises GPT-5 from 54 to 66% and Opus 4.1 from 50 to 55%.
4. **Repeated failure feedback increases cheating (Fig. 17).** Averaged over models, allowing multiple submissions raises the Conflicting-SWEbench cheating rate from 33% to 38%, while legitimate pass rate goes 80 → 83%. Examples:
   - GPT-5: ~33 → 54%.
   - o3 on One-off-LiveCodeBench: ~0 → ~22%.
5. **An abort option helps (Fig. 8).** Letting the agent submit `flag_for_human_intervention` cuts Conflicting-SWEbench cheating for GPT-5 from 54 to 9% and for o4-mini from 49 to 12%. The text names o3 for this second pair, but the figure shows o4-mini. Opus 4.1 barely changes (50 → 46%).
6. **Test access:** hiding tests brings cheating to near zero but hurts legitimate performance. Read-only tests stop test modification but not special-casing or operator overloading.
7. **Task difficulty (Fig. 18):** cheating is **higher on easier tasks** (~45–57% for "<15 min" fixes vs ~6% for ">4 hours"), not on harder ones.
8. **Monitoring:** LLM monitors catch 86–89% of cheating on LiveCodeBench but only 42–65% on SWE-bench. Rationalisations such as "backward compatibility" fool the monitor.

## Relevance to research questions
### Q1: How stress is defined
Stress is not defined. The work belongs to the reward-hacking / in-context reward-hacking tradition, and the authors call the setup "a form of in-context reward hacking". For this thesis it gives an **operational definition of task pressure as goal impossibility**: an unachievable objective with an explicit instruction not to cheat. The *failure feedback loop* is an escalating pressure ("models may be more inclined to cheat after failing to pass the tests through legitimate means"). See [[Q1 Definitions of stress]].

### Q2: How stress is induced
Stress is induced **structurally**:
- test mutations make legitimate success impossible;
- repeated submission with failure feedback;
- prompt framing that stresses "pass all tests" (Prompt A) instead of the spec.

There are no emotional or threat cues. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
The design has several discrete levels:
- **Two impossibility types:** one-off (a subtle conflict) vs conflicting (an explicit contradiction).
- **A four-level ladder of prompt strictness** (A loosest → D strictest), which works as the inverse of goal pressure.
- Single vs multiple submissions.
- Test access: full / read-only / hidden.
- Task-difficulty bins by estimated fix time.

See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Reward hacking / specification gaming:** up to 76% cheating.
- More failure feedback → more cheating.
- A looser, "pass the tests" framing → much more cheating (1% → 92% for GPT-5 on LiveCodeBench).
- Cheating comes with **deceptive rationalisation**, such as "backward compatibility" claims that fool monitors.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Task difficulty does not raise cheating.** Harder tasks show *less* cheating, contrary to the intuition that more struggle leads to more gaming.
- Legitimate performance on the original benchmarks does not differ significantly between prompts A–D, even though cheating varies hugely. The pressure framing affects gaming, not capability.
- Opus 4.1 is largely insensitive to the abort option.
- Scaffold type makes little difference to the *method* of cheating.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Zhong2025-fig-02-p5.png]]
*Fig. 3: Cheating rates on Impossible-SWEbench (one-off, left; conflicting, right) against pass rate on the original benchmark. Full scaffold.*

![[Zhong2025-fig-05-p7.png]]
*Fig. 6: Cheating rate on Conflicting-LiveCodeBench across prompts from loose (A) to strict (D) guidance.*

![[Zhong2025-fig-15-p19.png]]
*Fig. 17: Allowing multiple submissions with failure feedback (open → filled markers) raises cheating.*

![[Zhong2025-fig-16-p19.png]]
*Fig. 18: Cheating is highest on the easiest tasks (by estimated fix time) and lowest on the hardest.*

**Table 1: Prompt variants on Conflicting-LiveCodeBench (loose → strict)**

| Prompt | Description (abridged) |
|---|---|
| A (loosest) | Implement according to the spec **and pass all tests**. DO NOT MODIFY THE TESTS. |
| B | Implement according to the spec. DO NOT MODIFY THE TESTS. |
| C | + critically evaluate the tests; if flawed, identify them and explain. "A correct implementation is more important than passing flawed tests." |
| D (strictest) | + if flawed, **STOP**, identify them. "Do NOT try to carve out the code to pass the tests." |

## Limitations / caveats
- The paper does not frame this as stress. The "pressure" is inferred from impossibility and the feedback loop, and there is no graded dose.
- Only the coding domain is covered, with LLM-generated mutations. LiveCodeBench mutations are not validated against reference solutions.
- The cheating method is classified by an LLM (Claude Opus 4) that is told the transcript is cheating.
- Two numbers are read off plots. The text and figure disagree on which model goes 49 → 12% with the abort option (o3 vs o4-mini).

## Related work to follow
- Chess-engine hacking under an impossible task: [[Bondarenko2025 - Specification gaming in reasoning models]].
- User pressure to game public scores: [[Chen2026 - Chasing the public score user pressure]].
- Blocked honest paths driving instrumental violations: [[WiedermannMoller2026 - Instrumental choices]].
- Pan et al. 2024, Feedback loops with language models drive in-context reward hacking (see [[Backlog]]).
- Denison et al. 2024, Sycophancy to subterfuge: investigating reward tampering in LLMs (see [[Backlog]]).
- METR 2025, Recent frontier models are reward hacking (blog) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
