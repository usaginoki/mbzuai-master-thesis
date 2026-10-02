---
title: 'Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics'
citekey: Chrabaszcz2026
authors: Chrabaszcz et al. 2026
year: 2026
published: 2026-05-18
venue: arXiv preprint
url: https://arxiv.org/abs/2605.18549
arxiv: '2605.18549'
pdf_url: https://arxiv.org/pdf/2605.18549
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: A probe evaluated at every generated token of prompt and CoT ('probe trajectory') plus signal-processing features (volatility, trend, steady state)
outcome: Future behaviour of reasoning models in safety and maths; trajectory beats a single static prediction; max-pooling reaches up to 95% AUROC while mean-pooling and last-token collapse to near random
timing: pre-generation
why: Says the temporal shape of the signal matters, and that the readout position choice can make or break a predictor.
summary: Four datasets and four reasoning models. Future model behaviour is more distinguishable from the full probe trajectory than from one static prediction. Template-based training data nearly matches on-policy responses; pooling choice is critical, with max-pooling up to 95% AUROC and average/last-token near random.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
