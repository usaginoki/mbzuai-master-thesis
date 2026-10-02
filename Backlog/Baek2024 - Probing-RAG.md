---
title: 'Probing-RAG: Self-Probing to Guide Language Models in Selective Document Retrieval'
citekey: Baek2024
authors: Baek et al. 2024
year: 2024
published: 2024-10-17
venue: NAACL 2025 Findings
url: https://arxiv.org/abs/2410.13339
arxiv: '2410.13339'
pdf_url: https://arxiv.org/pdf/2410.13339
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: A small feed-forward prober on intermediate hidden states decides whether another retrieval step is needed; (b) gates retrieval.
outcome: Outperforms earlier adaptive-retrieval methods on five open-domain QA datasets with fewer retrieval steps.
safety_use: none
why: Earlier precedent for SeaKR-style internal-state gating; cite alongside SeaKR.
summary: ABSTRACT-ONLY.
found_by:
- search/intro-instrumented-feedback-rerun
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
