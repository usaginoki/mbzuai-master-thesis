---
title: 'Alignment Forecasting: Predicting Misalignment From Training Data'
citekey: Chen2026c
authors: Chen Yueh-Han et al. 2026
year: 2026
published: 2026-09-19
venue: arXiv preprint
url: https://arxiv.org/abs/2609.35805
arxiv: '2609.35805'
pdf_url: https://arxiv.org/pdf/2609.35805
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: 'Pre-training forecast from (target model, finetuning dataset, failure mode): an LLM reads the dataset and rates how strongly/broadly it pushes toward misbehaviour; logistic regression combines this with the failure-mode base rate and the target model''s prior tendency'
outcome: Whether SFT will significantly increase a given failure mode (deception, sycophancy, ...); decomposed forecaster AUROC 0.801, Brier 0.134, balanced accuracy 69.7% vs. 0.48-0.65 AUROC for directly prompted frontier models
timing: training-time
why: Names and benchmarks the exact task of this strand, with proper predictive metrics and honest limits.
summary: 'Introduces AlignmentForecastBench: over 5,000 forecasting questions across 17 target models, 32 datasets and 16 failure modes, with emergence defined as a significant increase over benign fine-tuning drift. Directly prompted frontier LLMs forecast poorly (AUROC 0.48-0.65; self-forecasting 0.448, below chance) while the decomposed scaffold reaches 0.801, beating a fine-tuned forecaster (0.682). Forecast-based filtering of UltraChat gave the least misalignment on multiple-choice evals, but the benefit in open-ended behavioural auditing was not clearly established; scope is SFT on 1,000-example datasets.'
found_by:
- search/pred-self-and-cross-model
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
