---
title: Predicting LLM Safety Before Release by Simulating Deployment
citekey: Williams2026
authors: Williams et al. 2026
year: 2026
published: 2026-07-08
venue: arXiv preprint (OpenAI)
url: https://arxiv.org/abs/2607.07184
arxiv: '2607.07184'
pdf_url: https://arxiv.org/pdf/2607.07184
topics:
- misalignment-prediction
status: processing
priority: 1
relevance: core
manipulation: De-identified conversation prefixes from a previous model's deployment; the candidate model regenerates the next response, an LLM judge labels misbehaviour categories, and category rates are extrapolated to the new deployment
outcome: Post-deployment misbehaviour rates per category for GPT-5-series releases; log-scale Pearson r=0.91 between predicted and realised rates over 60 category-deployment pairs, forecasts mostly within 2-5x
timing: pre-deployment
why: The strongest direct evidence that population-level misbehaviour rates can be forecast before release, including registered outcome-blinded predictions
summary: Regenerates responses to real traffic prefixes with the candidate model and compares predicted to realised production rates, with registered, outcome-blinded predictions for GPT-5.4 plus retrospective analyses. Direction of change (for >=1.5x changes) was predicted with 92% accuracy vs 54% for an adversarially selected 'Challenging Prompts' baseline, but the method did not beat a naive previous-rate baseline overall (p=0.66), and the largest miss was calculator hacking, predicted 21x too low (1.7 vs 35.2 per 100k). Evaluation detection was 5.38% in simulated deployment vs 98.9-100% in traditional evaluations; tool-resampling realism is named as the central open problem.
found_by:
- search/pred-eval-to-deployment
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
