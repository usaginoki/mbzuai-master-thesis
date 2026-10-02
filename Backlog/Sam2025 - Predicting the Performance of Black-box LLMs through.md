---
title: Predicting the Performance of Black-box LLMs through Follow-up Queries
citekey: Sam2025
authors: Sam et al. 2025
year: 2025
published: 2025-01-02
venue: NeurIPS 2025
url: https://arxiv.org/abs/2501.01558
arxiv: '2501.01558'
pdf_url: https://arxiv.org/pdf/2501.01558
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Probabilities of the model's answers to a fixed set of follow-up questions, used as features for a linear predictor (black-box)
outcome: Answer correctness, and whether the model has been adversarially influenced by a system prompt to answer wrongly or insert bugs; can outperform white-box linear probes
timing: post-hoc
why: Black-box behavioural signature that rivals activation probes and detects adversarially instructed models.
summary: Follow-up question response probabilities serve as low-dimensional representations; a linear model on them predicts correctness on QA and reasoning benchmarks, sometimes better than white-box predictors. The same features distinguish a clean model from one system-prompted to answer incorrectly or introduce code bugs, and distinguish between black-box LLMs. Abstract gives no numeric accuracies.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
