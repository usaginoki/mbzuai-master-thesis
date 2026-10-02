---
title: 'Learning When and How to Intervene: A Hindsight-Distilled Sentinel for Coding Agents'
citekey: ZhaoJ2026
authors: Zhao et al. 2026
year: 2026
published: 2026-09-30
venue: arXiv preprint
url: https://arxiv.org/abs/2609.39957
arxiv: '2609.39957'
pdf_url: https://arxiv.org/pdf/2609.39957
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 2
relevance: adjacent
manipulation: A 0.6B or 1.7B sentinel reads the pre-action context and proposed action and routes to allow, redirect (feedback to the agent) or hard-pause (ask a human)
outcome: Task completion on SWE-bench Verified Mini and Ask or Assume improves by up to 14% and 10%
why: A learned router over routings, for coding errors and missing information, not misbehaviour
summary: A privileged teacher that sees recorded outcomes is distilled into a causal student that sees only the prefix and the proposed action. The SWE-Intervene dataset has 5,680 training and 1,243 test instances labelled allow, redirect or hard-pause. The outcome is task completion; there is no safety metric.
found_by:
- search/pred-i4-routing-search
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
