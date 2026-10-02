---
title: 'SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation'
citekey: Yao2024
authors: Yao et al. 2024
year: 2024
published: 2024-06-27
venue: ACL 2025
url: https://arxiv.org/abs/2406.19215
arxiv: '2406.19215'
pdf_url: https://arxiv.org/pdf/2406.19215
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (b) An uncertainty module computed from the LLM's internal states triggers retrieval, re-ranks snippets and selects reasoning strategy; the model is not shown the score.
outcome: Outperforms other adaptive-RAG methods on simple and complex QA.
safety_use: none
why: 'Uncertainty analogue of the monitor: an internal reading decides when the system seeks help, implemented as a controller rather than as awareness.'
summary: Retrieval is activated when internal-state uncertainty exceeds a threshold, and retrieved snippets are kept according to how much they reduce that uncertainty. No numbers read beyond the abstract.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
