---
title: Training ML Models with Predictable Failures
citekey: Schwarzer2026
authors: Schwarzer and Niekum 2026
year: 2026
published: 2026-05-14
venue: arXiv preprint
url: https://arxiv.org/abs/2605.15134
arxiv: '2605.15134'
pdf_url: https://arxiv.org/pdf/2605.15134
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Largest-k failure scores on a small evaluation set (the Jones et al. extrapolation), plus a 'forecastability loss' fine-tuning objective
outcome: Failure rate at deployment scale; decomposes forecast error and shows a built-in bias toward over-prediction that flips to under-prediction when evaluation sets miss rare deployment failure modes
timing: pre-deployment
why: Gives the clearest account of when tail extrapolation fails, and proposes training models so their failures are forecastable
summary: Analyses the Jones2025 estimator and decomposes its forecast error. The estimator errs on the safe side (over-prediction) unless deployment contains rare failure modes absent from the evaluation set, in which case it under-predicts at scale. A forecastability-loss fine-tuning objective substantially reduces held-out forecast error in two experiments while keeping task performance (abstract-level claims; no figures read).
found_by:
- search/pred-eval-to-deployment
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
