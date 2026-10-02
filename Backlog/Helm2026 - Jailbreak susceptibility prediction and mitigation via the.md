---
title: Jailbreak susceptibility prediction and mitigation via the behavioral geometry of models
citekey: Helm2026
authors: Helm et al. 2026
year: 2026
published: 2026-05-26
venue: arXiv preprint
url: https://arxiv.org/abs/2605.26409
arxiv: '2605.26409'
pdf_url: https://arxiv.org/pdf/2605.26409
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: 'Black-box ''behavioural geometry'': a model''s position relative to previously evaluated models from a small number of probe responses'
outcome: Jailbreak susceptibility of 79 models from 24 providers and 100 system configurations of one base model; AUPRC 0.94 with about 98% fewer probes than a full evaluation
timing: pre-deployment
why: Cross-model behavioural fingerprinting to forecast unsafe behaviour of an unevaluated model or configuration.
summary: Embeds models by behaviour so that previously evaluated models predict the susceptibility of new ones. Simple geometry-based methods reach AUPRC 0.94 for susceptibility detection with roughly 98% fewer probes, and geometry-guided defence transfer beats same-provider assignment by 2% (p=0.03).
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
