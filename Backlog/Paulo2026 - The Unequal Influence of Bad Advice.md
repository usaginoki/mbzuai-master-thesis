---
title: 'The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment'
citekey: Paulo2026
authors: Paulo et al. 2026
year: 2026
published: 2026-09-29
venue: arXiv preprint
url: https://arxiv.org/abs/2609.37914
arxiv: '2609.37914'
pdf_url: https://arxiv.org/pdf/2609.37914
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Per-example training-data-attribution (influence) scores, compared with a black-box harmfulness score
outcome: Which harmful examples drive EM, validated by retraining on score-filtered data; filtering can substantially enhance or attenuate EM
timing: training-time
why: Tests attribution scores as forecasts by actually retraining, and shows the scores are model-specific.
summary: Estimates each harmful example's contribution to EM and checks it by retraining after filtering. Both attribution scores and a black-box harmfulness score identify consequential examples; influence scores work best for the model that computed them, with partial but weaker cross-model transfer across three model families.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
