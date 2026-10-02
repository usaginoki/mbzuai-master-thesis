---
title: Process-Centric Analysis of Agentic Software Systems
citekey: LiuS2025
authors: Liu et al. 2025
year: 2025
published: 2025-12-02
venue: arXiv preprint (DOI 10.1145/3798271)
url: https://arxiv.org/abs/2512.02393
arxiv: '2512.02393'
pdf_url: https://arxiv.org/pdf/2512.02393
topics:
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 2
relevance: adjacent
manipulation: Online graph of the trajectory flags plan violation, oscillation and stagnation; diagnostic message ('You may be stuck in ...') and rollback
outcome: Resolution +6.9-23.5% on problematic instances with shorter trajectories and near-zero overhead
why: State-triggered (stuck, looping) nudges with a rule monitor; predecessor of LivePlan
summary: 'ABSTRACT plus the intervention section via summarising fetch. Triggers: plan violation, cycles, at least 5 navigation steps without an edit. Gains are reported only on instances that were consistently problematic; 94.1% of them reach non-problematic trajectories. The monitor is rule-based, not an LLM agent.'
found_by:
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
