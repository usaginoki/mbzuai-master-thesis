---
title: A mechanistic study of language model introspection
citekey: Zou2026
authors: Zou et al. 2026
year: 2026
published: 2026-09-28
venue: arXiv preprint
url: https://arxiv.org/abs/2609.35108
arxiv: '2609.35108'
pdf_url: https://arxiv.org/pdf/2609.35108
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: core
manipulation: concept vector injected at one of ten token positions with fixed input text; attention-head analysis across three model families
outcome: Middle-layer 'gate' heads decide whether a change is reported; later 'router' heads select the position; concepts differ in how well they drive gate heads.
safety_use: none
why: Most recent circuit-level account; explains why detectability varies by concept.
summary: Fixed-input localisation task (ten positions or no intervention) across three model families. Identifies two small groups of attention heads; intervening on gate heads suppresses position reports even when router heads carry location information. Better-localised concept vectors produce stronger gate-head attention-score and output responses (QK/OV alignment).
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
