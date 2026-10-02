---
title: 'Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors'
citekey: Makins2026
authors: Makins et al. 2026
year: 2026
published: 2026-07-08
venue: arXiv preprint
url: https://arxiv.org/abs/2607.07368
arxiv: '2607.07368'
pdf_url: https://arxiv.org/pdf/2607.07368
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
status: candidate
priority: 3
relevance: adjacent
manipulation: Per-agent monitors on each agent's own trajectory in a synthetic AI-lab codebase (FakeLab)
outcome: Coordinated attacks across agents; more coordinating agents -> per-agent monitoring less likely to catch any attacker; an explicit planner raises attack completion up to sevenfold
timing: post-hoc
why: 'Limit case for trajectory-level monitoring: the incriminating signal may not exist inside any single trajectory'
summary: FakeLab has 9 services, 86 benign tasks and 4 attack objectives. The 'fragmentation effect' is not driven by the benign-to-malicious code ratio. A weak trusted monitor misses most attacks; a stronger one cuts undetected success by more than an order of magnitude but stays imperfect.
found_by:
- search/pred-cot-trajectory
- search/a2a-inspection-channels
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
