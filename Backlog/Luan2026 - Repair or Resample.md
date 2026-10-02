---
title: Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems
citekey: Luan2026
authors: Luan et al. 2026
year: 2026
published: 2026-08-26
venue: arXiv preprint
url: https://arxiv.org/abs/2608.25920
arxiv: '2608.25920'
pdf_url: https://arxiv.org/pdf/2608.25920
topics:
- agent-to-agent-influence
questions:
- Q15
status: candidate
priority: 2
relevance: core
manipulation: replay-anchored intervention on a failing agent in a multi-agent trajectory (repair vs plain resample)
outcome: Existing repair methods succeed in only 6.90% of cases; symptom-driven intervention fixes 20.15%
why: Warns that much apparent agent-on-agent repair is resampling luck
summary: ABSTRACT-ONLY. SymTrace records multi-agent trajectories and sets intervention anchors so failures can be replayed; SymFail has 536 annotated failures. The proposed symptom-driven method is reported as a 191.89% improvement over the best prior repair method.
found_by:
- search/a2a-influence-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
