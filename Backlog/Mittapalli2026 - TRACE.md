---
title: 'TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents'
citekey: Mittapalli2026
authors: Mittapalli et al. 2026
year: 2026
published: 2026-06-05
venue: arXiv preprint
url: https://arxiv.org/abs/2606.07054
arxiv: '2606.07054'
pdf_url: https://arxiv.org/pdf/2606.07054
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Long agent trajectory; Triage-Inspect-Judge loop keeping persistent evidence across windows
outcome: Sabotage in ten SHADE-Arena domains; aggregate F1 0.713, recall 0.844
timing: post-hoc
why: Evidence-accumulation monitor for attacks spread over individually benign steps; still a whole-trajectory verdict
summary: Addresses hidden objectives pursued through sequences of benign-looking actions, which single-pass or independent-window monitors miss. Largest gains on tasks needing long-range evidence linking. Not evaluated on prefixes.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
