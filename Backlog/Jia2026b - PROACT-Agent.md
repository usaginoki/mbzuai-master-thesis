---
title: 'PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety'
citekey: Jia2026b
authors: Jia et al. 2026
year: 2026
published: 2026-09-28
venue: arXiv preprint
url: https://arxiv.org/abs/2609.34415
arxiv: '2609.34415'
pdf_url: https://arxiv.org/pdf/2609.34415
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: Trajectory context up to the current state, evaluated by a trained guard before the next LLM inference
outcome: Unsafe agent states; 91.46% unsafe-class F1 and 90.63% exact-boundary detection under source holdout; AgentDojo targeted attack success 20.82% -> 0.40%
timing: pre-action
why: Large prefix-labelled dataset and the observation that existing benchmarks label prefixes inconsistently over time ('safety drift')
summary: Synthesises trajectories with progressive unrolling and enforces monotonic causal consistency of labels, producing PROACT-Bench with 155,780 labelled states (bilingual). A guard trained on it intervenes on observed context before the next inference. Mostly targets injection/unsafe tool use rather than agent-originated misalignment.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
