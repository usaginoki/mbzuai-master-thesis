---
title: 'Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence'
citekey: Saxena2026
authors: Saxena and Upadhyay 2026
year: 2026
published: 2026-09-28
venue: arXiv preprint
url: https://arxiv.org/abs/2609.34572
arxiv: '2609.34572'
pdf_url: https://arxiv.org/pdf/2609.34572
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: (a) a confidence / doubt signal is presented to the reasoning model (the paper frames the design space as where the reflective signal comes from, including hidden states or a separate predictor, how it is presented, and whether it changes the next action); outcome is the decision to answer unaided or delegate to a tool
outcome: 'Nine reasoning models, two tasks: confidence language moves tool delegation by a median 20.6 percentage points, but only 42% of induced changes align with the model''s actual competence versus a 40% random baseline'
safety_use: indirect
why: 'Cautionary result for any wearable design: models obey a shown self-state signal readily, so the loop is only as good as the signal, and compliance is not self-knowledge'
summary: Introduces 'nudgeability', how strongly confidence language shifts a model's decision to delegate. Expressing doubt raises delegation and confidence lowers it by a median 20.6 pp, yet the behavioural change is barely better than chance at tracking real competence (42% vs 40%). Read from the abstract only; whether a hidden-state probe was actually one of the tested signal sources was not verified.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
