---
title: Overtrained, Not Misaligned
citekey: Schreiber2026
authors: Schreiber et al. 2026
year: 2026
published: 2026-05-12
venue: arXiv preprint
url: https://arxiv.org/abs/2605.12199
arxiv: '2605.12199'
pdf_url: https://arxiv.org/pdf/2605.12199
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Checkpoint-level behavioural evaluation along the training run; model size
outcome: EM appears late, after near-convergence of the primary task; only 2 of 12 open-source models (17%) show consistent EM; early stopping removes EM while keeping 93% of task performance on average
timing: training-time
why: 'Gives base rates and a timing regularity: there is a window between task convergence and misalignment onset in which a predictor could act.'
summary: 'Largest EM replication: GPT-4o plus 12 open models (8B-671B) across 4 families, over one million responses. EM is not universal and correlates with model size (r=0.90 in the medical cross-domain check); early stopping avoids overgeneralisation to untruthfulness in 67% of medical cases, with semantically close domains less separable.'
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
