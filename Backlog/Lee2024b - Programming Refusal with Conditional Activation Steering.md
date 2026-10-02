---
title: Programming Refusal with Conditional Activation Steering
citekey: Lee2024b
authors: Lee et al. 2024
year: 2024
published: 2024-09-06
venue: ICLR 2025
url: https://arxiv.org/abs/2409.05907
arxiv: '2409.05907'
pdf_url: https://arxiv.org/pdf/2409.05907
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (b) Similarity between hidden states and a condition vector switches a refusal steering vector on; the model is not told.
outcome: Selective refusal by rule ('if input is about X then refuse') without weight changes.
safety_use: direct
why: 'Reference design for the alternative to notification: the reading drives an external controller directly.'
summary: CAST reads activation patterns during inference and applies steering only when a condition vector matches, enabling rules such as refusing hate speech or everything except legal advice. No numbers read beyond the abstract.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
