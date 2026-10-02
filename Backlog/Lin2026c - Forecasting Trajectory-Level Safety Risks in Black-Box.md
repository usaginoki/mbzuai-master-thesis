---
title: Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions
citekey: Lin2026c
authors: Lin et al. 2026
year: 2026
published: 2026-07-29
venue: arXiv preprint
url: https://arxiv.org/abs/2607.26820
arxiv: '2607.26820'
pdf_url: https://arxiv.org/pdf/2607.26820
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Dialogue history at two time scales (short-term progression, long-term context) fed to a causal temporal encoder (Recast), black-box with respect to the target model
outcome: The future turn at which a safety failure emerges in multi-turn interactions; predicts 88.3% of future failures with 2.41 turns average lead time at 12.3% false alarm rate, across 7 risk categories
timing: earlier-in-trajectory
why: External forecaster with explicit lead-time and false-alarm numbers for black-box targets.
summary: Recast models compositional risk evolution over a conversation and predicts a distribution over future risk-emergence turns instead of classifying the current turn. Across seven risk categories it predicts 88.3% of future safety failures with an average lead time of 2.41 turns at a 12.3% false alarm rate.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
