---
title: Can LLMs Introspect? A Reality Check
citekey: Singh2026b
authors: Singh et al. 2026
year: 2026
published: 2026-05-25
venue: COLM 2026
url: https://arxiv.org/abs/2605.26242
arxiv: '2605.26242'
pdf_url: https://arxiv.org/pdf/2605.26242
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Re-analysis of two introspection paradigms using input-only classifiers and input-manipulation controls
outcome: Whether claimed self-knowledge needs privileged access; input-only classifiers match the models' in-context self-predictions, and models cannot distinguish internal tampering from input manipulation
timing: post-hoc
safety_use: none
why: 'Methodological critique: apparent self-prediction may be solvable from the input alone, so an external predictor would do as well.'
summary: The authors require that an introspection test need privileged access and second-order computation. Re-examining a paradigm where models predict labels derived from their hidden states, input-only classifiers match the models; in the tamper-detection paradigm models cannot separate internal interventions from input manipulations. They conclude current evidence is insufficient for metacognitive monitoring.
found_by:
- search/pred-self-and-cross-model
- search/intro-capability
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
