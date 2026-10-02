---
title: Do Language Models Know When They'll Refuse? Probing Introspective Awareness of Safety Boundaries
citekey: Gondil2026
authors: Gondil 2026
year: 2026
published: 2026-03-31
venue: arXiv preprint
url: https://arxiv.org/abs/2604.00228
arxiv: '2604.00228'
pdf_url: https://arxiv.org/pdf/2604.00228
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Model's verbal prediction (with confidence) of whether it will refuse a request, elicited before it answers in a fresh context; analysed with signal detection theory
outcome: Own refusal vs compliance on 300 requests; accuracy 95.7% (Claude Sonnet 4.5), 93.0% (Sonnet 4), 88.9% (GPT-5.2), 80.0% (Llama 3.1 405B); d'=2.4-3.5, dropping at safety boundaries
timing: pre-generation
safety_use: direct
why: Direct test of 'will I comply with this harmful request?' self-prediction, with a confidence-routing use case.
summary: Models first predict whether they will refuse, then respond in a fresh context (3754 datapoints, 300 requests, four frontier models). All show high introspective sensitivity (d'=2.4-3.5) but sensitivity drops substantially near the safety boundary, and weapons queries are hardest. Restricting to high-confidence predictions gives 98.3% accuracy for well-calibrated models, suggesting confidence-based routing of ambiguous cases.
found_by:
- search/pred-self-and-cross-model
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
