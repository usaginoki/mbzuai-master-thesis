---
title: 'Linear probes rely on textual evidence: Results from leakage mitigation studies in language models'
citekey: Boxo2025
authors: Boxo et al. 2025
year: 2025
published: 2025-09-16
venue: arXiv preprint
url: https://arxiv.org/abs/2509.21344
arxiv: '2509.21344'
pdf_url: https://arxiv.org/pdf/2509.21344
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Linear probes on activations for sandbagging, sycophancy and bias, with and without tokens that verbalise the behaviour (system prompt, CoT)
outcome: 'Probe AUROC drops 10-30 points when textual evidence is filtered; on model organisms that do not verbalise: 0.57 vs 0.74 (bias), 0.57 vs 0.94 (sandbagging)'
timing: post-hoc
why: 'Main counter-evidence: probes may read text describing the situation rather than latent intent, which is exactly what a pre-behaviour predictor needs.'
summary: Across three setups, probe performance degrades once tokens containing textual evidence of the behaviour are removed, by 10 to 30 AUROC points. Model organisms trained to exhibit the behaviour without verbalising it give AUROC 0.57 versus 0.74 (bias) and 0.57 versus 0.94 (sandbagging) in unfiltered evaluation. The authors conclude linear probes may be brittle for non-surface-level patterns.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
