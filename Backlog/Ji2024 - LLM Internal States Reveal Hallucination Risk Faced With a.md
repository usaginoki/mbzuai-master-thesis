---
title: LLM Internal States Reveal Hallucination Risk Faced With a Query
citekey: Ji2024
authors: Ji et al. 2024
year: 2024
published: 2024-07-03
venue: arXiv preprint
url: https://arxiv.org/abs/2407.03282
arxiv: '2407.03282'
pdf_url: https://arxiv.org/pdf/2407.03282
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Probing estimator on internal states given the query only
outcome: Hallucination risk before response generation; average accuracy 84.32% across 15 NLG tasks
timing: pre-generation
why: Early pre-generation self-knowledge result for an unintended failure mode.
summary: Analyses over 15 NLG tasks and 700+ datasets whether internal states indicate if the query was seen in training and whether the model is likely to hallucinate. A probing estimator reaches 84.32% average hallucination-estimation accuracy at run time.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
