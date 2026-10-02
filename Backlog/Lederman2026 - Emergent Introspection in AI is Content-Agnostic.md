---
title: Emergent Introspection in AI is Content-Agnostic
citekey: Lederman2026
authors: Lederman & Mahowald 2026
year: 2026
published: 2026-03-05
venue: arXiv preprint
url: https://arxiv.org/abs/2603.05414
arxiv: '2603.05414'
pdf_url: https://arxiv.org/pdf/2603.05414
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: replication of thought-injection detection in Qwen3-235B-A22B and Llama 3.1 405B Instruct
outcome: Models detect that something anomalous happened far more reliably than what it was; wrong identifications are confabulated high-frequency concrete words.
safety_use: indirect
why: 'Suggests the ''monitor'' is an anomaly alarm rather than a readout of content: it can say ''something is off'', not what.'
summary: Detection ranges 3.6-53.9% across layers in Qwen and 4.3-31.7% in Llama, but correct identification only 1.3-13.9% and 0.7-12.9%, with 0 control false positives (0/30, 0/50). When Qwen detects but misidentifies, it guesses 'apple' in about 75% of wrong answers; wrong guesses come earlier in the response than correct ones.
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
