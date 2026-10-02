---
title: 'Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing'
citekey: Chen2026g
authors: Chen et al. 2026
year: 2026
published: 2026-08-18
venue: arXiv preprint
url: https://arxiv.org/abs/2608.17638
arxiv: '2608.17638'
pdf_url: https://arxiv.org/pdf/2608.17638
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: A 64-axis interpretable readout of the reasoning state (J64) and a cheap proxy from expert-routing statistics (R64); (b) the readout guides real-time interventions and router modifications.
outcome: Real-time interventions guided by the readout raise accuracy by 1.1-5.9 points; the routing proxy keeps 0.9-3.2 of that.
safety_use: none
why: A capability closed loop driven by an interpretable internal readout rather than text.
summary: ABSTRACT-ONLY. Per-axis correlation of the proxy with J64 is 0.69-0.86 across three models; on gpt-oss-20b the proxy keeps 95-100% of the predictive benefit.
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
