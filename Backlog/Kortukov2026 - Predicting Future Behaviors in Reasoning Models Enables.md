---
title: Predicting Future Behaviors in Reasoning Models Enables Better Steering
citekey: Kortukov2026
authors: Kortukov et al. 2026
year: 2026
published: 2026-06-09
venue: arXiv preprint
url: https://arxiv.org/abs/2606.11172
arxiv: '2606.11172'
pdf_url: https://arxiv.org/pdf/2606.11172
topics:
- misalignment-prediction
status: processing
priority: 1
relevance: core
manipulation: Activation probes at intermediate reasoning steps trained on the likelihood of future behaviours (not on behaviour already visible in text)
outcome: Most likely future behaviour of a reasoning model, 64%-91% accuracy; 'detection' features are poor predictors of future outcomes
timing: pre-generation
why: 'Separates detection features from prediction features: a probe that detects a behaviour is not automatically a forecaster of it.'
summary: The authors argue that steering work relies on features that detect behaviour in already-generated text, and show these are poor predictors of future behavioural outcomes. Probes trained explicitly to predict future behaviour likelihood from intermediate reasoning reach 64%-91% accuracy on the most likely behaviour. They use the predictor for Future Probe Controlled Generation (sampling candidate sentences and picking by predicted future behaviour), steering with almost no quality loss.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
