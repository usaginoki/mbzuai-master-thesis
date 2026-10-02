---
title: 'Self-Interpretability: LLMs Can Describe Complex Internal Processes that Drive Their Decisions'
citekey: Plunkett2025
authors: Plunkett et al. 2025
year: 2025
published: 2025-05-21
venue: arXiv preprint
url: https://arxiv.org/abs/2505.17120
arxiv: '2505.17120'
pdf_url: https://arxiv.org/pdf/2505.17120
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: GPT-4o and GPT-4o-mini fine-tuned to decide with randomly generated quantitative attribute weights; then asked to report the weights
outcome: Models accurately report the attribute weights they learned; further training improves this and generalises to decisions they were not fine-tuned on.
safety_use: indirect
why: 'Introspection is trainable and generalises: a route to making the ''self-reading'' more reliable.'
summary: Models are fine-tuned on choices (condos, loans, vacations) governed by random quantitative preferences never stated in text, and can then report those weights. Training on self-explanation improves accuracy and transfers to explaining other complex decisions (abstract-level; no figures read).
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
