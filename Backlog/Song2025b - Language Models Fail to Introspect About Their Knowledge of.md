---
title: Language Models Fail to Introspect About Their Knowledge of Language
citekey: Song2025b
authors: Song et al. 2025
year: 2025
published: 2025-03-10
venue: arXiv preprint
url: https://arxiv.org/abs/2503.07513
arxiv: '2503.07513'
pdf_url: https://arxiv.org/pdf/2503.07513
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: string probabilities as ground-truth internal knowledge vs metalinguistic prompted judgements, across 21 open-source LLMs
outcome: 'Prompted responses predict a model''s own probabilities no better than those of another model with nearly identical internal knowledge: no privileged self-access.'
safety_use: none
why: Clean negative result with internal ground truth; the same group argues for a 'thick' definition of introspection (arXiv 2508.14802).
summary: Tests grammaticality and word prediction in 21 open-source models. Both metalinguistic prompting and direct probability comparison give high task accuracy, but after controlling for model similarity there is no evidence that a model's prompted answers track its own string probabilities better than a similar model's; authors conclude LLMs cannot introspect in this domain.
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
