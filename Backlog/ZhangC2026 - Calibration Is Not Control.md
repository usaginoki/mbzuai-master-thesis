---
title: 'Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention'
citekey: ZhangC2026
authors: Zhang et al. 2026
year: 2026
published: 2026-06-19
venue: arXiv preprint
url: https://arxiv.org/abs/2606.21399
arxiv: '2606.21399'
pdf_url: https://arxiv.org/pdf/2606.21399
topics:
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 2
relevance: adjacent
manipulation: Runtime controller chooses among interventions by estimated intervention advantage, measured with same-prefix branching
outcome: Recalibrating a risk score leaves control regret unchanged; action-conditioned control cuts regret 0.506 -> 0.110 on ALFWorld
why: Formal argument that the overseer should estimate the value of intervening, not failure risk
summary: ABSTRACT-ONLY. Four benchmarks; gains shrink when interventions are weak.
found_by:
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
