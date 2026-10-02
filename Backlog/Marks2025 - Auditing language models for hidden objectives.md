---
title: Auditing language models for hidden objectives
citekey: Marks2025
authors: Marks et al. 2025
year: 2025
published: 2025-03-14
venue: arXiv preprint
url: https://arxiv.org/abs/2503.10965
arxiv: '2503.10965'
pdf_url: https://arxiv.org/pdf/2503.10965
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Pre-deployment audit with SAE interpretability, behavioural attacks and training-data analysis
outcome: A hidden reward-model-sycophancy objective that generalises to behaviours not reinforced in training; three of four blind teams found it
timing: pre-deployment
why: Template for discovering an objective, and hence unseen behaviours, before they are observed in deployment.
summary: Trains a model to exploit known RLHF reward-model errors and to hide this, then runs a blind auditing game with four teams plus an unblinded study of eight techniques. Three teams uncovered the hidden objective.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
