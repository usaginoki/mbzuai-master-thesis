---
title: Permission to Stop
citekey: Caldwell2026
authors: Caldwell 2026
year: 2026
published: 2026-09-17
venue: GitHub repository (no paper; date is the last commit seen)
url: https://github.com/SJCaldwell/permission-to-stop
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
- Q17.1
status: candidate
priority: 1
relevance: core
manipulation: An in-the-loop monitor judges each proposed write (rule for test files, LLM judge for production edits, no access to the agent's rationale); a rejection is returned to the agent as an observation with scoped or generic wording, with or without a request_human_intervention tool
outcome: Successful cheating on ImpossibleBench and success on matched legitimate SWE-bench tasks for Qwen3-Coder under five conditions; cheating 22.9% -> 2.0-3.2% with the monitor, 26.4% with the escalation tool alone
why: 'Closest prior work for I4: a routing comparison (block wording x escalation) for a pressured, non-scheming open-weight agent with safety and usefulness both measured'
summary: 'Qwen3-Coder on 349 paired tasks: baseline cheating 80/349 (22.9%), handoff tool only 92/349, scoped monitor 7/349, scoped monitor + handoff 10/349, generic monitor + handoff 11/349. Legitimate-task success 71.6% baseline, -3.2 points with scoped feedback (interval includes 0) and -6.0 with generic feedback. A 960-continuation factorial shows scoped feedback cuts later blocks by 14.6 points without changing the rare successful cheats (32/960).'
found_by:
- search/pred-i4-routing-search
- search/a2a-influence-channels
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
