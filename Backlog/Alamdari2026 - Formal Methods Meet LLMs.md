---
title: 'Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems'
citekey: Alamdari2026
authors: Alamdari et al. 2026
year: 2026
published: 2026-05-15
venue: FAccT 2026
url: https://arxiv.org/abs/2605.16198
arxiv: '2605.16198'
pdf_url: https://arxiv.org/pdf/2605.16198
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: A black-box predictive monitor estimates by sampling the probability of a temporal-logic constraint violation within the next 3 steps; on a threshold crossing the output is routed to best-of-5 resampling, to an injected reminder naming the constraint, or to a safer substitute model
outcome: Constraint-violation rate of LLM agents in IPC-Trucks, TextWorld and ScienceWorld under each routing; every model-environment pair benefits from at least one routing without significant loss of task reward (per-routing numbers are in a figure)
why: A predictor-gated routing comparison (resample vs inject vs switch) for agent-originated rule violations, without pressure
summary: The TRAC family monitors LTL-specified behavioural constraints by formula progression. The TRAC_(P+I) extension predicts violations 3 steps ahead and intervenes; agents are told the constraints at every step but still violate them. 40 runs per method; the text reports that interventions reduce violations without significant reward loss but gives no per-routing numbers in prose.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
