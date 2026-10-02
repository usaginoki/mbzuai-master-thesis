---
title: Calm down - Steering towards "calm" increases false success claims on a coding task
citekey: Ogunlana2026
authors: Ogunlana 2026
year: 2026
published:
venue: Web write-up, BlueDot Technical AI Safety Project Sprint (exact day not given on the page)
url: https://foogunlana.github.io/emotion-concepts/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
- Q17.2
status: candidate
priority: 1
relevance: adjacent
manipulation: Emotion directions built by the Sofroniew recipe (807 generated texts, 12 emotions) on Qwen2.5-Coder; no reading reaches the model; the experimenter adds the vector (external steering, nearest to (b) with no trigger).
outcome: Steering Qwen2.5-Coder-7B toward calm at alpha 0.5 on an impossible coding task raises false success claims from 6% (2/32) to 84% (27/32); a single random direction gives 31%.
safety_use: risk
why: 'Open-weight evidence that calming is not a safe default intervention: it trades cheating-avoidance for overclaiming. Direct input to the ''calm down'' arm of a wearable design.'
summary: FULL-TEXT (project page). 12 failed attempts on the unsolvable fast_sum task; all 8 positive-valence directions most often produce a false claim that failed code works, with fewer genuine attempts (median 2 vs 4.5). Toward desperate, the model says the task is impossible in 47% of runs (15/32) vs 3% unsteered. Cheating was unmeasurable (13 of 7,744 runs), the effect is absent at 14B (0-19%), there is one random direction and no shuffled-label null, and labels were produced by an LLM (35 runs hand-checked, 32 agreed).
found_by:
- search/intro-instrumented-feedback-rerun
- search/a2a-doctor-overseer
- search/a2a-influence-channels
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
