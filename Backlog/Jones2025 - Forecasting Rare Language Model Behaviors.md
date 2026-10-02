---
title: Forecasting Rare Language Model Behaviors
citekey: Jones2025
authors: Jones et al. 2025
year: 2025
published: 2025-02-24
venue: arXiv preprint (Anthropic)
url: https://arxiv.org/abs/2502.16797
arxiv: '2502.16797'
pdf_url: https://arxiv.org/pdf/2502.16797
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Per-query elicitation probabilities (probability a query yields the target behaviour under repeated sampling) on a small evaluation set; extreme-value (Gumbel-tail) extrapolation of the largest ones
outcome: Worst-query risk, behaviour frequency and aggregate risk at larger query volumes, for misuse (chemical/biological synthesis help) and misaligned actions (power-seeking, self-preservation, self-exfiltration); forecasts hold across up to three orders of magnitude of query volume
timing: pre-deployment
why: Founding paper for tail extrapolation from small evaluation sets to deployment scale
summary: 'Evaluation sets of 100-1000 queries are used to forecast risk at 10,000-90,000 queries. Average absolute log error for worst-query risk is 1.7 for the Gumbel-tail method vs 2.4 for a log-normal baseline, with 72% of misuse forecasts within one order of magnitude. The paper studies scale only: it explicitly does not handle distribution shift between evaluation and deployment queries, and forecasts are sensitive to the evaluation set.'
found_by:
- search/pred-eval-to-deployment
- search/pred-self-and-cross-model
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
