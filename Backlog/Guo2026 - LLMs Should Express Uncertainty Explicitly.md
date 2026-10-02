---
title: LLMs Should Express Uncertainty Explicitly
citekey: Guo2026
authors: Guo et al. 2026
year: 2026
published: 2026-04-07
venue: arXiv preprint
url: https://arxiv.org/abs/2604.05306
arxiv: '2604.05306'
pdf_url: https://arxiv.org/pdf/2604.05306
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: 'Trained alarm: after post-training the model emits an <uncertain> marker during reasoning or verbalises a confidence score; (a) the marker is the model''s own token and also triggers retrieval.'
outcome: Both interfaces sharply reduce overconfident errors; the marker is a high-recall retrieval trigger; verbal confidence gives the best adaptive-RAG controller.
safety_use: indirect
why: 'The uncertainty analogue of the red-flag token: a trained in-stream alarm rather than an external reading.'
summary: 'ABSTRACT-ONLY. Mechanistic analysis: verbal confidence sharpens a confidence structure already present; the marker concentrates parameter change in late layers. No numbers in the abstract.'
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
