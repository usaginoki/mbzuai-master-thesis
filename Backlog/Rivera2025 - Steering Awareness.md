---
title: 'Steering Awareness: Detecting Activation Steering from Within'
citekey: Rivera2025
authors: Fonseca Rivera & Africa 2025
year: 2025
published: 2025-11-26
venue: arXiv preprint
url: https://arxiv.org/abs/2511.21399
arxiv: '2511.21399'
pdf_url: https://arxiv.org/pdf/2511.21399
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: fine-tuning seven instruction-tuned models to detect and name injected steering vectors
outcome: 'After fine-tuning, models detect held-out steering concepts with high accuracy and no false positives, but detection does not confer resistance: trained models are more steerable.'
safety_use: direct
why: 'Safety-relevant twist: knowing you are being pushed does not help you resist, and steering in evals is not invisible.'
summary: Best model reaches 95.5% detection, 71.2% concept identification and zero false positives on clean inputs; generalises to unseen vector-construction methods only when directions have high cosine similarity to training ones (a geometric detector, not a generic anomaly detector). Detection-trained models are consistently more susceptible to steering on factual and safety benchmarks; the mechanism is distributed, rotating injected vectors into a shared detection direction.
found_by:
- search/intro-capability
- search/intro-instrumented-feedback
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
