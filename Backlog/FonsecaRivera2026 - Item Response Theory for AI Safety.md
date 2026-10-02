---
title: Item Response Theory for AI Safety
citekey: FonsecaRivera2026
authors: Fonseca Rivera et al. 2026
year: 2026
published: 2026-08-05
venue: arXiv preprint
url: https://arxiv.org/abs/2608.05086
arxiv: '2608.05086'
pdf_url: https://arxiv.org/pdf/2608.05086
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: IRT models fitted to item-level results of eight safety benchmarks across 192 models
outcome: Full-benchmark safety scores from a handful of items; three latent factors (refusal strictness, truthfulness, contextual harm)
timing: pre-deployment
why: Psychometric route to predicting a model's safety profile from few observations; contrasts with Petrova2026's single factor
summary: Roughly ten psychometrically selected items reproduce several benchmarks, cutting evaluation cost by 97-99%, with lower error than random item sampling. The authors also claim the fitted models can flag sandbagging and API changes. Covers harmful compliance, over-refusal and truthfulness, not agentic scheming.
found_by:
- search/pred-eval-to-deployment
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
