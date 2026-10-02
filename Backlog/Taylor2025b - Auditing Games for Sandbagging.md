---
title: Auditing Games for Sandbagging
citekey: Taylor2025b
authors: Taylor et al. 2025
year: 2025
published: 2025-12-08
venue: arXiv preprint
url: https://arxiv.org/abs/2512.07810
arxiv: '2512.07810'
pdf_url: https://arxiv.org/pdf/2512.07810
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Blue-team linear probes (and black-box, training-based methods) against red-team models fine-tuned to conditionally underperform
outcome: Which models sandbag; blue team could not reliably tell sandbaggers from benign models; probes more promising than black-box but vulnerable to red-team-instilled behaviours
timing: pre-deployment
why: Adversarial test of probes as a pre-deployment audit signal (UK AISI).
summary: A red team fine-tuned five models, some sandbagging. Black-box detection was defeated by imitation of a weaker model; naive linear probes were vulnerable to instilled distractor behaviours. Training-based elicitation recovered full performance with one demonstration but also raised benign models' scores.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
