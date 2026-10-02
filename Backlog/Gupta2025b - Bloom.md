---
title: 'Bloom: an open source tool for automated behavioral evaluations'
citekey: Gupta2025b
authors: Gupta et al. 2025
year: 2025
published: 2025-12-19
venue: Anthropic Alignment Science Blog
url: https://alignment.anthropic.com/2025/bloom-auto-evals/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Automatically generated scenario suites for one researcher-specified behaviour, scored by a judge model
outcome: Frequency and severity of a behaviour; separates system-prompted model organisms from baselines for 9/10 quirks
timing: pre-deployment
why: Turns a behaviour description into a rate estimate, the building block of propensity measurement
summary: 16 models on four behaviours with 100 rollouts per suite. Judge scores correlate 0.86 (Spearman) with human labels on 40 transcripts. Cannot capture behaviours that depend on real consequences, and flags evaluation awareness as a growing concern.
found_by:
- search/pred-eval-to-deployment
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
