---
title: 'SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing'
citekey: ChenT2026
authors: Chen et al. 2026
year: 2026
published: 2026-07-15
venue: arXiv preprint
url: https://arxiv.org/abs/2607.13594
arxiv: '2607.13594'
pdf_url: https://arxiv.org/pdf/2607.13594
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: A guard model reads each proposed action and routes it to execute, ask the user, or refuse, with a decoding-time threshold
outcome: Higher overall accuracy and safety-related recall than open-weight and closed baselines on the routing decision
why: Frames guard output as a three-way routing decision; measures classification, not the downstream effect
summary: The guard reduces inference to a single decoding call and can be repositioned across risk tolerances without retraining. No agent-behaviour outcome is reported in the abstract.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
