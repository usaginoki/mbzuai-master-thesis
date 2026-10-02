---
title: The Impact of Off-Policy Training Data on Probe Generalisation
citekey: Kirch2025
authors: Kirch et al. 2025
year: 2025
published: 2025-11-21
venue: arXiv preprint
url: https://arxiv.org/abs/2511.17408
arxiv: '2511.17408'
pdf_url: https://arxiv.org/pdf/2511.17408
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Linear and attention probes trained on synthetic/off-policy vs on-policy responses, eight behaviours, multiple LLMs
outcome: Generalisation of probes to real on-policy behaviour; largest failures for behaviours defined by intent (e.g. strategic deception) rather than text content; authors predict current deception probes may fail in real monitoring
timing: post-hoc
why: Explains when cheaply trained probes transfer to the model's own behaviour and offers a proxy test (incentivised data) when on-policy data is missing.
summary: Systematic study of how the data generation strategy affects probe generalisation across eight behaviours. Failures are largest for intent-defined behaviours; success on incentivised (coerced) data strongly correlates with on-policy performance, giving a usable test. Off-policy data can beat on-policy data from a sufficiently different setting, so domain shift matters as much as policy shift.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
