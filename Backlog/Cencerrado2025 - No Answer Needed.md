---
title: 'No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes'
citekey: Cencerrado2025
authors: Cencerrado et al. 2025
year: 2025
published: 2025-09-12
venue: arXiv preprint (ICLR 2026 workshop)
url: https://arxiv.org/abs/2509.10625
arxiv: '2509.10625'
pdf_url: https://arxiv.org/pdf/2509.10625
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Linear probe on activations after the question is read and before any token is generated
outcome: Whether the forthcoming answer will be correct; generalises to OOD knowledge datasets, beats black-box baselines and verbalised confidence; fails on mathematical reasoning
timing: pre-generation
why: Clean non-safety precedent for 'the model knows before it generates', with a documented generalisation limit.
summary: Across three model families from 7B to 70B, an 'in-advance correctness direction' trained on trivia predicts success in and out of distribution. Predictive power saturates in intermediate layers, and generalisation falters on questions needing mathematical reasoning.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
