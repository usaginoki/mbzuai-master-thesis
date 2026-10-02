---
title: Online Monitoring and Corrective Steering of Programming Agents
citekey: LiuS2026
authors: Liu et al. 2026
year: 2026
published: 2026-08-07
venue: arXiv preprint
url: https://arxiv.org/abs/2608.06701
arxiv: '2608.06701'
pdf_url: https://arxiv.org/pdf/2608.06701
topics:
- agent-to-agent-influence
questions:
- Q14
- Q15
- Q17.1
status: candidate
priority: 1
relevance: core
manipulation: Rule-based trajectory monitor (drift, repetition, blocking signals) triggers a stronger advisor LLM that injects a next-step correction
outcome: Resolution +5.0 to +15.2 points over SWE-agent; beats a periodic advisor and a re-planner; 2 regressions
why: Best controlled comparison of trigger-gated vs periodic advice from another agent on a stuck worker
summary: 'FULL-TEXT (arXiv HTML via summarising fetch). SWE-bench Pro: DeepSeek-V3 21.76% -> 34.09%, Gemini-2.5-Flash 13.17% -> 28.41%, MiniMax-M2.5 52.5% -> 57.95%; Verified 38.2 -> 49.4, 37.8 -> 48.4, 74.2 -> 79.2. Periodic advisor (every 5 steps) 28.79% with 3.25-7.38 interventions vs 1.47-2.99; the SAGE re-planner is below vanilla (18.79%) with 26 regressions against 2. Cost about $0.08 per instance (abstract).'
found_by:
- search/a2a-doctor-overseer
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
